import json

bucketTemplate = "${bucket}"
awsAccessKeyId = "${accessKey}"
awsSecretAccessKey = "${secretKey}"
region = "OTHER"
endpoint = "${endpoint}"
commonPrefix = "${tempLandingFolder}/${tableName}"
delimiter = "/"
useSSE = False
encryption = "S3"
kmsKeyId = ""
encryptionContext = [{}]
customerKey = ""
customerKeyMd5 = ""
connectionTimeout = 10
socketTimeout = 50
retryCount = 3
useProxy = False
proxyHost = None
proxyPort = 0
proxyUser = ""
proxyPassword = ""
threadPoolSize = 1
multipartUploadThreshold = 268435456
minimumUploadPartSize = 5242880
partitionTemplate = ""
timeZoneID = "UTC"
timeDriverTemplate = "${time:now()}"
fileNamePrefix1 = "${filePrefix}"
fileNamePrefix2 = "_CTRL"
fileNameSuffix = None
compress = False
stageOnRecordError = "TO_ERROR"
stageRequiredFields = []
stageRecordPreconditions = []

bucketTemplate = {'name': 's3TargetConfigBean.s3Config.bucketTemplate',
                  'value': bucketTemplate}
awsAccessKeyId = {'name': 's3TargetConfigBean.s3Config.awsConfig.awsAccessKeyId',
                  'value': awsAccessKeyId}
awsSecretAccessKey = {'name': 's3TargetConfigBean.s3Config.awsConfig.awsSecretAccessKey',
                      'value': awsSecretAccessKey}
region = {'name': 's3TargetConfigBean.s3Config.region',
          'value': region}
endpoint = {'name': 's3TargetConfigBean.s3Config.endpoint',
            'value': endpoint}
commonPrefix = {'name': 's3TargetConfigBean.s3Config.commonPrefix',
                'value': commonPrefix}
delimiter = {'name': 's3TargetConfigBean.s3Config.delimiter',
             'value': delimiter}
useSSE = {'name': 's3TargetConfigBean.sseConfig.useSSE',
          'value': useSSE}
encryption = {'name': 's3TargetConfigBean.sseConfig.encryption',
              'value': encryption}
kmsKeyId = {'name': 's3TargetConfigBean.sseConfig.kmsKeyId',
            'value': kmsKeyId}
encryptionContext = {'name': 's3TargetConfigBean.sseConfig.encryptionContext',
                     'value': encryptionContext}
customerKey = {'name': 's3TargetConfigBean.sseConfig.customerKey',
               'value': customerKey}
customerKeyMd5 = {'name': 's3TargetConfigBean.sseConfig.customerKeyMd5',
                  'value': customerKeyMd5}
connectionTimeout = {'name': 's3TargetConfigBean.proxyConfig.connectionTimeout',
                     'value': connectionTimeout}
socketTimeout = {'name': 's3TargetConfigBean.proxyConfig.socketTimeout',
                 'value': socketTimeout}
retryCount = {'name': 's3TargetConfigBean.proxyConfig.retryCount',
              'value': retryCount}
useProxy = {'name': 's3TargetConfigBean.proxyConfig.useProxy',
            'value': useProxy}
proxyHost = {'name': 's3TargetConfigBean.proxyConfig.proxyHost',
             'value': proxyHost}
proxyPort = {'name': 's3TargetConfigBean.proxyConfig.proxyPort',
             'value': proxyPort}
proxyUser = {'name': 's3TargetConfigBean.proxyConfig.proxyUser',
             'value': proxyUser}
proxyPassword = {'name': 's3TargetConfigBean.proxyConfig.proxyPassword',
                 'value': proxyPassword}
threadPoolSize = {'name': 's3TargetConfigBean.tmConfig.threadPoolSize',
                  'value': threadPoolSize}
multipartUploadThreshold = {'name': 's3TargetConfigBean.tmConfig.multipartUploadThreshold',
                            'value': multipartUploadThreshold}
minimumUploadPartSize = {'name': 's3TargetConfigBean.tmConfig.minimumUploadPartSize',
                         'value': minimumUploadPartSize}
partitionTemplate = {'name': 's3TargetConfigBean.partitionTemplate',
                     'value': partitionTemplate}
timeZoneID = {'name': 's3TargetConfigBean.timeZoneID',
              'value': timeZoneID}
timeDriverTemplate = {'name': 's3TargetConfigBean.timeDriverTemplate',
                      'value': timeDriverTemplate}
fileNamePrefix1 = {'name': 's3TargetConfigBean.fileNamePrefix',
                   'value': fileNamePrefix1}
fileNamePrefix2 = {'name': 's3TargetConfigBean.fileNamePrefix',
                   'value': fileNamePrefix2}
fileNameSuffix = {'name': 's3TargetConfigBean.fileNameSuffix',
                  'value': fileNameSuffix}
compress = {'name': 's3TargetConfigBean.compress',
            'value': compress}
stageOnRecordError = {'name': 'stageOnRecordError',
                      'value': stageOnRecordError}
stageRequiredFields = {'name': 'stageRequiredFields',
                       'value': stageRequiredFields}
stageRecordPreconditions = {'name': 'stageRecordPreconditions',
                            'value': stageRecordPreconditions}

dataFile_json_objects = [bucketTemplate, awsAccessKeyId, awsSecretAccessKey, region, endpoint, commonPrefix, delimiter,
                         useSSE,
                         encryption, kmsKeyId, encryptionContext, customerKey, customerKeyMd5, connectionTimeout,
                         socketTimeout,
                         retryCount, useProxy, proxyHost,
                         proxyPort, proxyUser, proxyPassword, threadPoolSize, multipartUploadThreshold,
                         minimumUploadPartSize,
                         partitionTemplate,
                         timeZoneID, timeDriverTemplate, fileNamePrefix1, fileNameSuffix, compress, stageOnRecordError,
                         stageRequiredFields, stageRecordPreconditions]

controlFile_json_objects = [bucketTemplate, awsAccessKeyId, awsSecretAccessKey, region, endpoint, commonPrefix,
                            delimiter, useSSE,
                            encryption, kmsKeyId, encryptionContext, customerKey, customerKeyMd5, connectionTimeout,
                            socketTimeout,
                            retryCount, useProxy, proxyHost,
                            proxyPort, proxyUser, proxyPassword, threadPoolSize, multipartUploadThreshold,
                            minimumUploadPartSize,
                            partitionTemplate,
                            timeZoneID, timeDriverTemplate, fileNamePrefix2, fileNameSuffix, compress,
                            stageOnRecordError,
                            stageRequiredFields, stageRecordPreconditions]

dataFile_json_data = json.dumps(dataFile_json_objects, indent=2)
