general_params = [{"key": "accessKey", "value": "AKIA4139A57D4ED44392"},
                  {"key": "secretKey", "value": "NVMHywjIiIlSiGjvcerVydFOBOwBItddrktgtt0p"},
                  {"key": "bucket", "value": "ursamajor-abs1-uat-edla-dm9s-za"},
                  {"key": "jceksFile", "value": "/ecs/dm9s/za/dm9s-za-ecs.jceks"},
                  {"key": "filePrefix", "value": "data-file-${uuid:uuid()}"},
                  {"key": "endpoint", "value": "https://ecs-hadoop.gslb.absa.africa:9021"}]

infoFile_params = [{"key": "S3_ACCESS_KEY", "value": "${accessKey}"},
                   {"key": "S3_SECRET_KEY", "value": "${secretKey}"},
                   {"key": "S3_JCEKS_FILE", "value": "${jceksFile}"},
                   {"key": "FILE_PREFIX", "value": "${filePrefix}"},
                   {"key": "S3_ENDPOINT", "value": "${endpoint}"},
                   {"key": "S3_BUCKET", "value": "${bucket}"}]
