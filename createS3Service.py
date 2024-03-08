import os
import json

dataFormat = "DELIMITED"
charset = "UTF-8"
csvFileFormat = "CSV"
csvHeader = "WITH_HEADER"
csvReplaceNewLines = False
csvReplaceNewLinesString = ""
csvCustomDelimiter = "|"
csvCustomEscape = "\\"
csvCustomQuote = "\""
jsonMode = "MULTIPLE_OBJECTS"
textFieldPath = "/text"
textRecordSeparator = "\\n"
textFieldMissingAction = "ERROR"
textEmptyLineIfNull = False
avroSchemaSource = None
avroSchema = None
registerSchema = False
schemaRegistryUrlsForRegistration = []
schemaRegistryUrls = []
schemaLookupMode = "SUBJECT"
subject = None
subjectToRegister = None
schemaId = None
includeSchema = True
avroCompression = None
binaryFieldPath = "/"
protoDescriptorFile = None
messageType = None
fileNameEL = None
wholeFileExistsAction = "TO_ERROR"
includeChecksumInTheEvents = False
checksumAlgorithm = "MD5"
xmlPrettyPrint = True
xmlValidateSchema = False
xmlSchema = None
displayFormats = "AVRO,BINARY,DELIMITED,JSON,PROTOBUF,SDC_JSON,TEXT,WHOLE_FILE"

dataFormat = {'name': 'dataFormat',
              'value': dataFormat}
charset = {'name': 'dataGeneratorFormatConfig.charset',
           'value': charset}
csvFileFormat = {'name': 'dataGeneratorFormatConfig.csvFileFormat',
                 'value': csvFileFormat}
csvHeader = {'name': 'dataGeneratorFormatConfig.csvHeader',
             'value': csvHeader}
csvReplaceNewLines = {'name': 'dataGeneratorFormatConfig.csvReplaceNewLines',
                      'value': csvReplaceNewLines}
csvReplaceNewLinesString = {'name': 'dataGeneratorFormatConfig.csvReplaceNewLinesString',
                            'value': csvReplaceNewLinesString}
csvCustomDelimiter = {'name': 'dataGeneratorFormatConfig.csvCustomDelimiter',
                      'value': csvCustomDelimiter}
csvCustomEscape = {'name': 'dataGeneratorFormatConfig.csvCustomEscape',
                   'value': csvCustomEscape}
csvCustomQuote = {'name': 'dataGeneratorFormatConfig.csvCustomQuote',
                  'value': csvCustomQuote}
jsonMode = {'name': 'dataGeneratorFormatConfig.jsonMode',
            'value': jsonMode}
textFieldPath = {'name': 'dataGeneratorFormatConfig.textFieldPath',
                 'value': textFieldPath}
textRecordSeparator = {'name': 'dataGeneratorFormatConfig.textRecordSeparator',
                       'value': textRecordSeparator}
textFieldMissingAction = {'name': 'dataGeneratorFormatConfig.textFieldMissingAction',
                          'value': textFieldMissingAction}
textEmptyLineIfNull = {'name': 'dataGeneratorFormatConfig.textEmptyLineIfNull',
                       'value': textEmptyLineIfNull}
avroSchemaSource = {'name': 'dataGeneratorFormatConfig.avroSchemaSource',
                    'value': avroSchemaSource}
avroSchema = {'name': 'dataGeneratorFormatConfig.avroSchema',
              'value': avroSchema}
registerSchema = {'name': 'dataGeneratorFormatConfig.registerSchema',
                  'value': registerSchema}
schemaRegistryUrlsForRegistration = {'name': 'dataGeneratorFormatConfig.schemaRegistryUrlsForRegistration',
                                     'value': schemaRegistryUrlsForRegistration}
schemaRegistryUrls = {'name': 'dataGeneratorFormatConfig.schemaRegistryUrls',
                      'value': schemaRegistryUrls}
schemaLookupMode = {'name': 'dataGeneratorFormatConfig.schemaLookupMode',
                    'value': schemaLookupMode}
subject = {'name': 'dataGeneratorFormatConfig.subject',
           'value': subject}
subjectToRegister = {'name': 'dataGeneratorFormatConfig.subjectToRegister',
                     'value': subjectToRegister}
schemaId = {'name': 'dataGeneratorFormatConfig.schemaId',
            'value': schemaId}
includeSchema = {'name': 'dataGeneratorFormatConfig.includeSchema',
                 'value': includeSchema}
avroCompression = {'name': 'dataGeneratorFormatConfig.avroCompression',
                   'value': avroCompression}
binaryFieldPath = {'name': 'dataGeneratorFormatConfig.binaryFieldPath',
                   'value': binaryFieldPath}
protoDescriptorFile = {'name': 'dataGeneratorFormatConfig.protoDescriptorFile',
                       'value': protoDescriptorFile}
messageType = {'name': 'dataGeneratorFormatConfig.messageType',
               'value': messageType}
fileNameEL = {'name': 'dataGeneratorFormatConfig.fileNameEL',
              'value': fileNameEL}
wholeFileExistsAction = {'name': 'dataGeneratorFormatConfig.wholeFileExistsAction',
                         'value': wholeFileExistsAction}
includeChecksumInTheEvents = {'name': 'dataGeneratorFormatConfig.includeChecksumInTheEvents',
                              'value': includeChecksumInTheEvents}
checksumAlgorithm = {'name': 'dataGeneratorFormatConfig.checksumAlgorithm',
                     'value': checksumAlgorithm}
xmlPrettyPrint = {'name': 'dataGeneratorFormatConfig.xmlPrettyPrint',
                  'value': xmlPrettyPrint}
xmlValidateSchema = {'name': 'dataGeneratorFormatConfig.xmlValidateSchema',
                     'value': xmlValidateSchema}
xmlSchema = {'name': 'dataGeneratorFormatConfig.xmlSchema',
             'value': xmlSchema}
displayFormats = {'name': 'displayFormats',
                  'value': displayFormats}

services_object = [dataFormat, charset, csvFileFormat, csvHeader, csvReplaceNewLines, csvReplaceNewLinesString, csvCustomDelimiter,
                   csvCustomEscape,
                   csvCustomQuote, jsonMode, textFieldPath, textRecordSeparator, textFieldMissingAction,
                   textEmptyLineIfNull,
                   avroSchemaSource, avroSchema, registerSchema, schemaRegistryUrlsForRegistration, schemaRegistryUrls,
                   schemaLookupMode, subject, subjectToRegister, schemaId, includeSchema, avroCompression,
                   binaryFieldPath, protoDescriptorFile,
                   messageType, fileNameEL, wholeFileExistsAction, includeChecksumInTheEvents, checksumAlgorithm,
                   xmlPrettyPrint, xmlValidateSchema, xmlSchema, displayFormats]

modified_list = [{
    "service": "com.streamsets.pipeline.api.service.dataformats.DataFormatGeneratorService",
    "serviceVersion": 1,
    "configuration": services_object
}]

updated_service_data = json.dumps(modified_list, indent=2)

