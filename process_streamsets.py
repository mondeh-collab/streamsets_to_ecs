import json
import os
from createS3Service import modified_list
from createS3Config import json_objects

script_text = "resources/script.csv"
directory = "input_workflows"
outdirectory = "output_workflows"
updated_params1 = [{"key": "accessKey", "value": "AKIA4139A57D4ED44392"},
                   {"key": "secretKey", "value": "NVMHywjIiIlSiGjvcerVydFOBOwBItddrktgtt0p"},
                   {"key": "bucket", "value": "s3a://ursamajor-abs1-uat-edla-dm9s-za"},
                   {"key": "jceksFile", "value": "jceks:///ecs/dm9s/za/dm9s-za-ecs.jceks"},
                   {"key": "filePrefix", "value": "data-file-${uuid:uuid()}"},
                   {"key": "endpoint", "value": "https://ecs-hadoop.gslb.absa.africa:9021"}]

# accessing streamsets workflows from directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path) as json_file:
            data = json.load(json_file)
            title = data["pipelineConfig"]["title"]
            print(filename)

    # accessing updated script config
    with open(script_text, 'r') as file:
        updatedScript = file.read()

    # Accessing filePath & tempPath in Shell_01 stage
    for stage in data["pipelineConfig"]["stages"]:
        if stage["stageName"] == "com_streamsets_pipeline_stage_executor_shell_ShellDExecutor":
            for config in stage["configuration"]:
                if config["name"] == "config.environmentVariables":
                    for env_var in config["value"]:
                        if env_var["key"] == "filePath":
                            env_var["value"] = "s3a://${bucket}${hadoopRawFolder}/${tableName}"
                        if env_var["key"] == "tempPath":
                            env_var["value"] = "s3a://${bucket}/${record:value('/filePath')}"

    # Replace data file path with s3 target
    for stageTarget in data["pipelineConfig"]["stages"]:
        if stageTarget["stageName"] == "com_streamsets_pipeline_stage_destination_hdfs_HdfsDTarget":
            stageTarget["stageName"] = "com_streamsets_pipeline_stage_destination_s3_AmazonS3DTarget"
            stageTarget["library"] = "streamsets-datacollector-aws-lib"
            stageTarget["stageVersion"] = 11
            stageTarget["configuration"] = json_objects
            stageTarget["services"] = modified_list

        if stageTarget["instanceName"] == "HadoopFS_02":
            stageTarget["configuration"] = json_objects
            stageTarget["services"] = modified_list

    # change dataFilePath to objectKey
    for stage in data["pipelineConfig"]["stages"]:
        if stage["stageName"] == "com_streamsets_pipeline_stage_processor_javascript_JavaScriptDProcessor":
            for config in stage["configuration"]:
                if config["name"] == "script":
                    config["value"] = updatedScript.replace('\n', '')
                    newScript = config["value"]
                    prettyScript = json.dumps(newScript, indent=4)

    # append constants list
    constants = data["pipelineConfig"]["configuration"][9]["value"]
    constants.extend(updated_params1)

    # Convert the modified dictionary back to JSON string
    updated_json_data = json.dumps(data, indent=2)

    output_directory = "C:/Users/abmh712/Desktop/streamsets/output/"
    # save updated workflow as json
    workflowName = os.path.join(outdirectory, filename)
    with open(filename, "w") as updatedJson:
        updatedJson.write(updated_json_data)
        print(f"Application for {workflowName} created")
