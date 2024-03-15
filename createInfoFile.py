import json

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

datasetName = {'name': 'datasetName',
               'value': datasetName},
dataFile = {'name': 'dataFile',
            'value': dataFile},
controlFile = {'name': 'controlFile',
               'value': controlFile},
reportDate = {'name': 'reportDate',
              'value': reportDate},
kerberosPrincipal = {'name': 'kerberosPrincipal',
                     'value': kerberosPrincipal},
kerberosKeytab = {'name': 'kerberosKeytab',
                  'value': kerberosKeytab},
HADOOP_PROXY_USER = {'name': 'HADOOP_PROXY_USER',
                     'value': HADOOP_PROXY_USER},
userName = {'name': 'userName',
            'value': userName},
tempPath = {'name': 'tempPath',
            'value': tempPath},
filePath = {'name': 'filePath',
            'value': filePath},
filePath = {'name': 'S3_ACCESS_KEY',
            'value': S3_ACCESS_KEY},
S3_SECRET_KEY = {'name': 'S3_SECRET_KEY',
                 'value': S3_SECRET_KEY},
S3_ENDPOINT = {'name': 'S3_ENDPOINT',
               'value': S3_ENDPOINT},
S3_JCEKS_FILE = {'name': 'S3_JCEKS_FILE',
                 'value': S3_JCEKS_FILE},
FILE_PREFIX = {'name': 'FILE_PREFIX',
               'value': FILE_PREFIX}

info_file_objects = [datasetName, dataFile, controlFile, reportDate, kerberosPrincipal, kerberosKeytab,
                     HADOOP_PROXY_USER, userName, tempPath, filePath, filePath, S3_SECRET_KEY, S3_ENDPOINT,
                     S3_JCEKS_FILE, FILE_PREFIX]

info_file_object = json.dumps(info_file_objects, indent=2)
