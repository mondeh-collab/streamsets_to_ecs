import json
import os

# Your JSON data
directory = "C:/Users/abmh712/Desktop/Streamsets/Source"

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)

        with open(file_path) as json_file:
            data = json.load(json_file)

# Define the new value for the "filePath" key
new_file_path = "C:/Users/abmh712/Desktop/Streamsets"

# Iterate over each configuration object
for config in data["pipelineConfig"]["configuration"]:
    if config.get("name") == "expressionProcessorConfigs" and config.get("value"):
        for item in config["value"]:
            # if item.get("key") == "filePath":
            if item.get("value") == "${hadoopRawFolder}/${tableName}":
                # Update the value of the "filePath" key
                item["value"] = new_file_path

# Convert the modified dictionary back to JSON string
updated_json_data = json.dumps(data)

# Print or use the updated JSON data
print(data["pipelineConfig"]["configuration"][12])
filename = os.path.join(new_file_path, "test" + ".json")
# print(output_directory + "/" + tableName + ".conf")
with open(filename, "w") as file:
    file.write(updated_json_data)
