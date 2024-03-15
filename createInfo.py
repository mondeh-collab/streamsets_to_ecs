import json
import os
config = None

datasetName = "${dataSetName}"
dataFile = "${record:value('/dataFile')}"
controlFile = "${record:value('/controlFile')}"
reportDate = "${reportDate}"
kerberosPrincipal = "${kerberosPrincipal}"
kerberosKeytab = "${kerberosKeytab}"
HADOOP_PROXY_USER = "${kerberosPrincipal}"
userName = "${record:value('/userName')}"
tempPath = "s3a://${bucket}/${record:value('/filePath')}"
filePath = "s3a://${bucket}${hadoopRawFolder}/${tableName}"
S3_ACCESS_KEY = "${accessKey}"
S3_SECRET_KEY = "${secretKey}"
S3_ENDPOINT = "${endpoint}"
S3_JCEKS_FILE = "${jceksFile}"
FILE_PREFIX = "${filePrefix}"
config.timeout = "300000"
config.script = "kinit -kt $SDC_CONF/sdc.keytab sdc@CORP.DSARENA.COM\nhdfs dfs -get /user/${userName}/${userName}.keytab $SDC_HOME/scripts/\nunset HADOOP_PROXY_USER\nexport kerberosKeytab=$SDC_HOME/scripts/${userName}.keytab\n$SDC_HOME/scripts/run_info_file.sh\nrm -f $SDC_HOME/scripts/${userName}.keytab"
stageOnRecordError = "TO_ERROR"
stageRequiredFields = []
stageRecordPreconditions = []

datasetName = {'name': 'datasetName',
               'value': datasetName}
dataFile = {'name': 'dataFile',
            'value': dataFile}
controlFile = {'name': 'controlFile',
               'value': controlFile}
reportDate = {'name': 'reportDate',
              'value': reportDate}
kerberosPrincipal = {'name': 'kerberosPrincipal',
                     'value': kerberosPrincipal}
kerberosKeytab = {'name': 'kerberosKeytab',
                  'value': kerberosKeytab}
HADOOP_PROXY_USER = {'name': 'HADOOP_PROXY_USER',
                     'value': HADOOP_PROXY_USER}
userName = {'name': 'userName',
            'value': userName}
tempPath = {'name': 'tempPath',
            'value': tempPath}
filePath = {'name': 'filePath',
            'value': filePath}
filePath = {'name': 'S3_ACCESS_KEY',
            'value': S3_ACCESS_KEY}
S3_SECRET_KEY = {'name': 'S3_SECRET_KEY',
                 'value': S3_SECRET_KEY}
S3_ENDPOINT = {'name': 'S3_ENDPOINT',
               'value': S3_ENDPOINT}
S3_JCEKS_FILE = {'name': 'S3_JCEKS_FILE',
                 'value': S3_JCEKS_FILE}
FILE_PREFIX = {'name': 'FILE_PREFIX',
               'value': FILE_PREFIX}
config.timeout = {'name': 'config.timeout',
                  'value': config.timeout}
config.script = {'name': 'config.script',
                 'value': config.script}
stageOnRecordError = {'name': 'stageOnRecordError',
                      'value': stageOnRecordError}
stageRequiredFields = {'name': 'stageRequiredFields',
                       'value': stageRequiredFields}
stageRecordPreconditions = {'name': 'stageRecordPreconditions',
                            'value': stageRecordPreconditions}

info_file_objects = [datasetName, dataFile, controlFile, reportDate, kerberosPrincipal, kerberosKeytab,
                     HADOOP_PROXY_USER, userName, tempPath, filePath, filePath, S3_SECRET_KEY, S3_ENDPOINT,
                     S3_JCEKS_FILE, FILE_PREFIX, config.timeout, config.script, stageOnRecordError, stageRequiredFields,
                     stageRecordPreconditions]

modified_info_list = {
    "instanceName": "Shell_01",
    "library": "streamsets-datacollector-basic-lib",
    "stageName": "com_streamsets_pipeline_stage_executor_shell_ShellDExecutor",
    "stageVersion": "1",
    "configuration": info_file_objects,
    "uiInfo": {
        "description": "",
        "label": "Create INFO file",
        "xPos": 1862.2694091796875,
        "yPos": 380.542236328125,
        "stageType": "EXECUTOR"
    },
    "inputLanes": ["ExpressionEvaluator_01OutputLane17004981139260"],
    "outputLanes": [],
    "eventLanes": [],
    "services": []
}

info_file_object = json.dumps(modified_info_list, indent=2)

output_directory = "C:/Users/abmh712/Desktop/streamsets/output/"
filename = "info.json"
# save updated workflow as json
workflowName = os.path.join(output_directory, filename)
with open(filename, "w") as updatedJson:
    updatedJson.write(info_file_object)
    print(f"Application for {workflowName} created")
