general_params = [{"key": "accessKey", "value": "AKIA14C4F831EFE5ED87"},
                  {"key": "secretKey", "value": "aTVWHyKPkrCzhvkzqqh462BBTuXmmHd9bMPa1ZPY"},
                  {"key": "bucket", "value": "ingesttest"},
                  {"key": "jceksFile", "value": "jceks:///tmp/s3_test/ingesttest.jceks"},
                  {"key": "filePrefix", "value": "data-file-${uuid:uuid()}"},
                  {"key": "endpoint", "value": "https://ecs-hadoop.gslb.absa.africa:9021"}]

infoFile_params = [{"key": "S3_ACCESS_KEY", "value": "${accessKey}"},
                   {"key": "S3_SECRET_KEY", "value": "${secretKey}"},
                   {"key": "S3_JCEKS_FILE", "value": "${jceksFile}"},
                   {"key": "FILE_PREFIX", "value": "${filePrefix}"},
                   {"key": "S3_ENDPOINT", "value": "${endpoint}"}]
