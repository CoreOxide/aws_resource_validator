# Iotfleetwise Iotfleetwise Classes

# Actuator

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### min
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### assignedValue
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### structFullyQualifiedName
- **Type**: typing.Optional[str]


# ActuatorOutput

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### min
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### assignedValue
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### structFullyQualifiedName
- **Type**: typing.Optional[str]


# AssociateVehicleFleetRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# Attribute

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### min
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### assignedValue
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]


# AttributeOutput

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### min
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### assignedValue
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateVehicleRequest

### vehicles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CreateVehicleRequestItem]
- **Required**: Yes


# BatchCreateVehicleResponse

### vehicles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CreateVehicleResponseItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CreateVehicleError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateVehicleRequest

### vehicles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.UpdateVehicleRequestItem]
- **Required**: Yes


# BatchUpdateVehicleResponse

### vehicles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.UpdateVehicleResponseItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.UpdateVehicleError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# Branch

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]


# CampaignSummary

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### signalCatalogArn
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'RUNNING', 'SUSPENDED', 'WAITING_FOR_APPROVAL']]


# CanDbcDefinition

### networkInterface
- **Type**: <class 'str'>
- **Required**: Yes

### canDbcFiles
- **Type**: typing.List[typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]]
- **Required**: Yes

### signalsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# CanInterface

### name
- **Type**: <class 'str'>
- **Required**: Yes

### protocolName
- **Type**: typing.Optional[str]

### protocolVersion
- **Type**: typing.Optional[str]


# CanSignal

### messageId
- **Type**: <class 'int'>
- **Required**: Yes

### isBigEndian
- **Type**: <class 'bool'>
- **Required**: Yes

### isSigned
- **Type**: <class 'bool'>
- **Required**: Yes

### startBit
- **Type**: <class 'int'>
- **Required**: Yes

### offset
- **Type**: <class 'float'>
- **Required**: Yes

### factor
- **Type**: <class 'float'>
- **Required**: Yes

### length
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### signalValueType
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]


# CloudWatchLogDeliveryOptions

### logType
- **Type**: typing.Literal['ERROR', 'OFF']
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]


# CollectionScheme

### timeBasedCollectionScheme
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimeBasedCollectionScheme]

### conditionBasedCollectionScheme
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ConditionBasedCollectionScheme]


# ConditionBasedCollectionScheme

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### minimumTriggerIntervalMs
- **Type**: typing.Optional[int]

### triggerMode
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'RISING_EDGE']]

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# ConditionBasedSignalFetchConfig

### conditionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### triggerMode
- **Type**: typing.Literal['ALWAYS', 'RISING_EDGE']
- **Required**: Yes


# CreateCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### collectionScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CollectionScheme'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### expiryTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### postTriggerCollectionDuration
- **Type**: typing.Optional[int]

### diagnosticsMode
- **Type**: typing.Optional[typing.Literal['OFF', 'SEND_ACTIVE_DTCS']]

### spoolingMode
- **Type**: typing.Optional[typing.Literal['OFF', 'TO_DISK']]

### compression
- **Type**: typing.Optional[typing.Literal['OFF', 'SNAPPY']]

### priority
- **Type**: typing.Optional[int]

### signalsToCollect
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalInformation]]

### dataExtraDimensions
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]

### dataDestinationConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DataDestinationConfig]]

### dataPartitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DataPartition]]

### signalsToFetch
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalFetchInformation, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalFetchInformationOutput]]]


# CreateCampaignResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDecoderManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### signalDecoders
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoder, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoderOutput]]]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NetworkInterface]]

### defaultForUnmappedSignals
- **Type**: typing.Optional[typing.Literal['CUSTOM_DECODING']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]


# CreateDecoderManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetRequest

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]


# CreateFleetResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nodes
- **Type**: typing.List[str]
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]


# CreateModelManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSignalCatalogRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### nodes
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Node, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NodeOutput]]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]


# CreateSignalCatalogResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStateTemplateRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateProperties
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### dataExtraDimensions
- **Type**: typing.Optional[typing.List[str]]

### metadataExtraDimensions
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]


# CreateStateTemplateResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVehicleError

### vehicleName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# CreateVehicleRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### decoderManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### associationBehavior
- **Type**: typing.Optional[typing.Literal['CreateIotThing', 'ValidateIotThingExists']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]

### stateTemplates
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociation, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociationOutput]]]


# CreateVehicleRequestItem

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### decoderManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### associationBehavior
- **Type**: typing.Optional[typing.Literal['CreateIotThing', 'ValidateIotThingExists']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]

### stateTemplates
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociation, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociationOutput]]]


# CreateVehicleResponse

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### thingArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVehicleResponseItem

### vehicleName
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# CustomDecodingInterface

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CustomDecodingSignal

### id
- **Type**: <class 'str'>
- **Required**: Yes


# CustomProperty

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### dataEncoding
- **Type**: typing.Optional[typing.Literal['BINARY', 'TYPED']]

### description
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### structFullyQualifiedName
- **Type**: typing.Optional[str]


# CustomStruct

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]


# DataDestinationConfig

### s3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.S3Config]

### timestreamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimestreamConfig]

### mqttTopicConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.MqttTopicConfig]


# DataPartition

### id
- **Type**: <class 'str'>
- **Required**: Yes

### storageOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DataPartitionStorageOptions'>
- **Required**: Yes

### uploadOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DataPartitionUploadOptions]


# DataPartitionStorageOptions

### maximumSize
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StorageMaximumSize'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'str'>
- **Required**: Yes

### minimumTimeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StorageMinimumTimeToLive'>
- **Required**: Yes


# DataPartitionUploadOptions

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# DecoderManifestSummary

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### modelManifestArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']]

### message
- **Type**: typing.Optional[str]


# DeleteCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCampaignResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDecoderManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDecoderManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFleetRequest

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteModelManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSignalCatalogRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSignalCatalogResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStateTemplateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateTemplateResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVehicleRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVehicleResponse

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateVehicleFleetRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# FleetSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### lastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# FormattedVss

### vssJson
- **Type**: typing.Optional[str]


# GetCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'RUNNING', 'SUSPENDED', 'WAITING_FOR_APPROVAL']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### postTriggerCollectionDuration
- **Type**: <class 'int'>
- **Required**: Yes

### diagnosticsMode
- **Type**: typing.Literal['OFF', 'SEND_ACTIVE_DTCS']
- **Required**: Yes

### spoolingMode
- **Type**: typing.Literal['OFF', 'TO_DISK']
- **Required**: Yes

### compression
- **Type**: typing.Literal['OFF', 'SNAPPY']
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### signalsToCollect
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalInformation]
- **Required**: Yes

### collectionScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CollectionScheme'>
- **Required**: Yes

### dataExtraDimensions
- **Type**: typing.List[str]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataDestinationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DataDestinationConfig]
- **Required**: Yes

### dataPartitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DataPartition]
- **Required**: Yes

### signalsToFetch
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalFetchInformationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetDecoderManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDecoderManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetEncryptionConfigurationResponse

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionStatus
- **Type**: typing.Literal['FAILURE', 'PENDING', 'SUCCESS']
- **Required**: Yes

### encryptionType
- **Type**: typing.Literal['FLEETWISE_DEFAULT_ENCRYPTION', 'KMS_BASED_ENCRYPTION']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetFleetRequest

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFleetResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoggingOptionsResponse

### cloudWatchLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CloudWatchLogDeliveryOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegisterAccountStatusResponse

### customerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### accountStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### timestreamRegistrationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimestreamRegistrationResponse'>
- **Required**: Yes

### iamRegistrationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.IamRegistrationResponse'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetSignalCatalogRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSignalCatalogResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### nodeCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NodeCounts'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetStateTemplateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetStateTemplateResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateProperties
- **Type**: typing.List[str]
- **Required**: Yes

### dataExtraDimensions
- **Type**: typing.List[str]
- **Required**: Yes

### metadataExtraDimensions
- **Type**: typing.List[str]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetVehicleRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetVehicleResponse

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### decoderManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### stateTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociationOutput]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# GetVehicleStatusRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetVehicleStatusRequestPaginate

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# GetVehicleStatusResponse

### campaigns
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.VehicleStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# IamRegistrationResponse

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]


# IamResources

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ImportDecoderManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### networkFileDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NetworkFileDefinition]
- **Required**: Yes


# ImportDecoderManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# ImportSignalCatalogRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### vss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.FormattedVss]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]]


# ImportSignalCatalogResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# ListCampaignsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListCampaignsRequestPaginate

### status
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListCampaignsResponse

### campaignSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CampaignSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestNetworkInterfacesRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDecoderManifestNetworkInterfacesRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListDecoderManifestNetworkInterfacesResponse

### networkInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NetworkInterface]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestSignalsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDecoderManifestSignalsRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListDecoderManifestSignalsResponse

### signalDecoders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoderOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestSignalsResponsePaginator

### signalDecoders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoderPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestsRequest

### modelManifestArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListDecoderManifestsRequestPaginate

### modelManifestArn
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListDecoderManifestsResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.DecoderManifestSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsForVehicleRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetsForVehicleRequestPaginate

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListFleetsForVehicleResponse

### fleets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListFleetsRequestPaginate

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListFleetsResponse

### fleetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.FleetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelManifestNodesRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListModelManifestNodesRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListModelManifestNodesResponse

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NodeOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelManifestsRequest

### signalCatalogArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListModelManifestsRequestPaginate

### signalCatalogArn
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListModelManifestsResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ModelManifestSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSignalCatalogNodesRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### signalNodeType
- **Type**: typing.Optional[typing.Literal['ACTUATOR', 'ATTRIBUTE', 'BRANCH', 'CUSTOM_PROPERTY', 'CUSTOM_STRUCT', 'SENSOR']]


# ListSignalCatalogNodesRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### signalNodeType
- **Type**: typing.Optional[typing.Literal['ACTUATOR', 'ATTRIBUTE', 'BRANCH', 'CUSTOM_PROPERTY', 'CUSTOM_STRUCT', 'SENSOR']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListSignalCatalogNodesResponse

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NodeOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSignalCatalogsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSignalCatalogsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListSignalCatalogsResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalCatalogSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateTemplatesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListStateTemplatesRequestPaginate

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListStateTemplatesResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# ListVehiclesInFleetRequest

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListVehiclesInFleetRequestPaginate

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListVehiclesInFleetResponse

### vehicles
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVehiclesRequest

### modelManifestArn
- **Type**: typing.Optional[str]

### attributeNames
- **Type**: typing.Optional[typing.List[str]]

### attributeValues
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListVehiclesRequestPaginate

### modelManifestArn
- **Type**: typing.Optional[str]

### attributeNames
- **Type**: typing.Optional[typing.List[str]]

### attributeValues
- **Type**: typing.Optional[typing.List[str]]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PaginatorConfig]


# ListVehiclesResponse

### vehicleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.VehicleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MessageSignal

### topicName
- **Type**: <class 'str'>
- **Required**: Yes

### structuredMessage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessage, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageOutput]
- **Required**: Yes


# MessageSignalOutput

### topicName
- **Type**: <class 'str'>
- **Required**: Yes

### structuredMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageOutput'>
- **Required**: Yes


# MessageSignalPaginator

### topicName
- **Type**: <class 'str'>
- **Required**: Yes

### structuredMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessagePaginator'>
- **Required**: Yes


# ModelManifestSummary

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### signalCatalogArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']]


# MqttTopicConfig

### mqttTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# NetworkFileDefinition

### canDbc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CanDbcDefinition]


# NetworkInterface

### interfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CAN_INTERFACE', 'CUSTOM_DECODING_INTERFACE', 'OBD_INTERFACE', 'VEHICLE_MIDDLEWARE']
- **Required**: Yes

### canInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CanInterface]

### obdInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ObdInterface]

### vehicleMiddleware
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.VehicleMiddleware]

### customDecodingInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomDecodingInterface]


# Node

### branch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Branch]

### sensor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Sensor, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SensorOutput, NoneType]

### actuator
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Actuator, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ActuatorOutput, NoneType]

### attribute
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Attribute, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.AttributeOutput, NoneType]

### struct
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomStruct]

### property
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomProperty]


# NodeCounts

### totalNodes
- **Type**: typing.Optional[int]

### totalBranches
- **Type**: typing.Optional[int]

### totalSensors
- **Type**: typing.Optional[int]

### totalAttributes
- **Type**: typing.Optional[int]

### totalActuators
- **Type**: typing.Optional[int]

### totalStructs
- **Type**: typing.Optional[int]

### totalProperties
- **Type**: typing.Optional[int]


# NodeOutput

### branch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Branch]

### sensor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SensorOutput]

### actuator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ActuatorOutput]

### attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.AttributeOutput]

### struct
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomStruct]

### property
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomProperty]


# ObdInterface

### name
- **Type**: <class 'str'>
- **Required**: Yes

### requestMessageId
- **Type**: <class 'int'>
- **Required**: Yes

### obdStandard
- **Type**: typing.Optional[str]

### pidRequestIntervalSeconds
- **Type**: typing.Optional[int]

### dtcRequestIntervalSeconds
- **Type**: typing.Optional[int]

### useExtendedIds
- **Type**: typing.Optional[bool]

### hasTransmissionEcu
- **Type**: typing.Optional[bool]


# ObdSignal

### pidResponseLength
- **Type**: <class 'int'>
- **Required**: Yes

### serviceMode
- **Type**: <class 'int'>
- **Required**: Yes

### pid
- **Type**: <class 'int'>
- **Required**: Yes

### scaling
- **Type**: <class 'float'>
- **Required**: Yes

### offset
- **Type**: <class 'float'>
- **Required**: Yes

### startByte
- **Type**: <class 'int'>
- **Required**: Yes

### byteLength
- **Type**: <class 'int'>
- **Required**: Yes

### bitRightShift
- **Type**: typing.Optional[int]

### bitMaskLength
- **Type**: typing.Optional[int]

### isSigned
- **Type**: typing.Optional[bool]

### signalValueType
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PeriodicStateTemplateUpdateStrategy

### stateTemplateUpdateRate
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimePeriod'>
- **Required**: Yes


# PrimitiveMessageDefinition

### ros2PrimitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ROS2PrimitiveMessageDefinition]


# PutEncryptionConfigurationRequest

### encryptionType
- **Type**: typing.Literal['FLEETWISE_DEFAULT_ENCRYPTION', 'KMS_BASED_ENCRYPTION']
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# PutEncryptionConfigurationResponse

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionStatus
- **Type**: typing.Literal['FAILURE', 'PENDING', 'SUCCESS']
- **Required**: Yes

### encryptionType
- **Type**: typing.Literal['FLEETWISE_DEFAULT_ENCRYPTION', 'KMS_BASED_ENCRYPTION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# PutLoggingOptionsRequest

### cloudWatchLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CloudWatchLogDeliveryOptions'>
- **Required**: Yes


# ROS2PrimitiveMessageDefinition

### primitiveType
- **Type**: typing.Literal['BOOL', 'BYTE', 'CHAR', 'FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'INT64', 'INT8', 'STRING', 'UINT16', 'UINT32', 'UINT64', 'UINT8', 'WSTRING']
- **Required**: Yes

### offset
- **Type**: typing.Optional[float]

### scaling
- **Type**: typing.Optional[float]

### upperBound
- **Type**: typing.Optional[int]


# RegisterAccountRequest

### timestreamResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimestreamResources]

### iamResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.IamResources]


# RegisterAccountResponse

### registerAccountStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### timestreamResources
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimestreamResources'>
- **Required**: Yes

### iamResources
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.IamResources'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# S3Config

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'PARQUET']]

### storageCompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### prefix
- **Type**: typing.Optional[str]


# Sensor

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### min
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### structFullyQualifiedName
- **Type**: typing.Optional[str]


# SensorOutput

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'BOOLEAN_ARRAY', 'DOUBLE', 'DOUBLE_ARRAY', 'FLOAT', 'FLOAT_ARRAY', 'INT16', 'INT16_ARRAY', 'INT32', 'INT32_ARRAY', 'INT64', 'INT64_ARRAY', 'INT8', 'INT8_ARRAY', 'STRING', 'STRING_ARRAY', 'STRUCT', 'STRUCT_ARRAY', 'UINT16', 'UINT16_ARRAY', 'UINT32', 'UINT32_ARRAY', 'UINT64', 'UINT64_ARRAY', 'UINT8', 'UINT8_ARRAY', 'UNIX_TIMESTAMP', 'UNIX_TIMESTAMP_ARRAY', 'UNKNOWN']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### min
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### structFullyQualifiedName
- **Type**: typing.Optional[str]


# SignalCatalogSummary

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# SignalDecoder

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CAN_SIGNAL', 'CUSTOM_DECODING_SIGNAL', 'MESSAGE_SIGNAL', 'OBD_SIGNAL']
- **Required**: Yes

### interfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### canSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CanSignal]

### obdSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ObdSignal]

### messageSignal
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.MessageSignal, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.MessageSignalOutput, NoneType]

### customDecodingSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomDecodingSignal]


# SignalDecoderOutput

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CAN_SIGNAL', 'CUSTOM_DECODING_SIGNAL', 'MESSAGE_SIGNAL', 'OBD_SIGNAL']
- **Required**: Yes

### interfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### canSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CanSignal]

### obdSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ObdSignal]

### messageSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.MessageSignalOutput]

### customDecodingSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomDecodingSignal]


# SignalDecoderPaginator

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CAN_SIGNAL', 'CUSTOM_DECODING_SIGNAL', 'MESSAGE_SIGNAL', 'OBD_SIGNAL']
- **Required**: Yes

### interfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### canSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CanSignal]

### obdSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ObdSignal]

### messageSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.MessageSignalPaginator]

### customDecodingSignal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.CustomDecodingSignal]


# SignalFetchConfig

### timeBased
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.TimeBasedSignalFetchConfig]

### conditionBased
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ConditionBasedSignalFetchConfig]


# SignalFetchInformation

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### signalFetchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalFetchConfig'>
- **Required**: Yes

### actions
- **Type**: typing.List[str]
- **Required**: Yes

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# SignalFetchInformationOutput

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### signalFetchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalFetchConfig'>
- **Required**: Yes

### actions
- **Type**: typing.List[str]
- **Required**: Yes

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# SignalInformation

### name
- **Type**: <class 'str'>
- **Required**: Yes

### maxSampleCount
- **Type**: typing.Optional[int]

### minimumSamplingIntervalMs
- **Type**: typing.Optional[int]

### dataPartitionId
- **Type**: typing.Optional[str]


# StateTemplateAssociation

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateUpdateStrategy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateUpdateStrategy, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateUpdateStrategyOutput]
- **Required**: Yes


# StateTemplateAssociationOutput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateUpdateStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateUpdateStrategyOutput'>
- **Required**: Yes


# StateTemplateSummary

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### signalCatalogArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastModificationTime
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]


# StateTemplateUpdateStrategy

### periodic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PeriodicStateTemplateUpdateStrategy]

### onChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# StateTemplateUpdateStrategyOutput

### periodic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PeriodicStateTemplateUpdateStrategy]

### onChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# StorageMaximumSize

### unit
- **Type**: typing.Literal['GB', 'MB', 'TB']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# StorageMinimumTimeToLive

### unit
- **Type**: typing.Literal['DAYS', 'HOURS', 'WEEKS']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# StructuredMessage

### primitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PrimitiveMessageDefinition]

### structuredMessageListDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageListDefinition, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageListDefinitionOutput, NoneType]

### structuredMessageDefinition
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePair, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePairOutput]]]


# StructuredMessageFieldNameAndDataTypePair

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# StructuredMessageFieldNameAndDataTypePairOutput

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# StructuredMessageFieldNameAndDataTypePairPaginator

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# StructuredMessageListDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### memberType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### listType
- **Type**: typing.Literal['DYNAMIC_BOUNDED_CAPACITY', 'DYNAMIC_UNBOUNDED_CAPACITY', 'FIXED_CAPACITY']
- **Required**: Yes

### capacity
- **Type**: typing.Optional[int]


# StructuredMessageListDefinitionOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### memberType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### listType
- **Type**: typing.Literal['DYNAMIC_BOUNDED_CAPACITY', 'DYNAMIC_UNBOUNDED_CAPACITY', 'FIXED_CAPACITY']
- **Required**: Yes

### capacity
- **Type**: typing.Optional[int]


# StructuredMessageListDefinitionPaginator

### name
- **Type**: <class 'str'>
- **Required**: Yes

### memberType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### listType
- **Type**: typing.Literal['DYNAMIC_BOUNDED_CAPACITY', 'DYNAMIC_UNBOUNDED_CAPACITY', 'FIXED_CAPACITY']
- **Required**: Yes

### capacity
- **Type**: typing.Optional[int]


# StructuredMessageOutput

### primitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PrimitiveMessageDefinition]

### structuredMessageListDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageListDefinitionOutput]

### structuredMessageDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePairOutput]]


# StructuredMessagePaginator

### primitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.PrimitiveMessageDefinition]

### structuredMessageListDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageListDefinitionPaginator]

### structuredMessageDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePairPaginator]]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Tag]
- **Required**: Yes


# TimeBasedCollectionScheme

### periodMs
- **Type**: <class 'int'>
- **Required**: Yes


# TimeBasedSignalFetchConfig

### executionFrequencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# TimePeriod

### unit
- **Type**: typing.Literal['HOUR', 'MILLISECOND', 'MINUTE', 'SECOND']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# TimestreamConfig

### timestreamTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# TimestreamRegistrationResponse

### timestreamDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### timestreamTableName
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### timestreamDatabaseArn
- **Type**: typing.Optional[str]

### timestreamTableArn
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# TimestreamResources

### timestreamDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### timestreamTableName
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['APPROVE', 'RESUME', 'SUSPEND', 'UPDATE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### dataExtraDimensions
- **Type**: typing.Optional[typing.List[str]]


# UpdateCampaignResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'RUNNING', 'SUSPENDED', 'WAITING_FOR_APPROVAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDecoderManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### signalDecodersToAdd
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoder, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoderOutput]]]

### signalDecodersToUpdate
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoder, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.SignalDecoderOutput]]]

### signalDecodersToRemove
- **Type**: typing.Optional[typing.List[str]]

### networkInterfacesToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NetworkInterface]]

### networkInterfacesToUpdate
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NetworkInterface]]

### networkInterfacesToRemove
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']]

### defaultForUnmappedSignals
- **Type**: typing.Optional[typing.Literal['CUSTOM_DECODING']]


# UpdateDecoderManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFleetRequest

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateFleetResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateModelManifestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### nodesToAdd
- **Type**: typing.Optional[typing.List[str]]

### nodesToRemove
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']]


# UpdateModelManifestResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSignalCatalogRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### nodesToAdd
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Node, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NodeOutput]]]

### nodesToUpdate
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.Node, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.NodeOutput]]]

### nodesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateSignalCatalogResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStateTemplateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### stateTemplatePropertiesToAdd
- **Type**: typing.Optional[typing.List[str]]

### stateTemplatePropertiesToRemove
- **Type**: typing.Optional[typing.List[str]]

### dataExtraDimensions
- **Type**: typing.Optional[typing.List[str]]

### metadataExtraDimensions
- **Type**: typing.Optional[typing.List[str]]


# UpdateStateTemplateResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVehicleError

### vehicleName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# UpdateVehicleRequest

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: typing.Optional[str]

### decoderManifestArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### attributeUpdateMode
- **Type**: typing.Optional[typing.Literal['Merge', 'Overwrite']]

### stateTemplatesToAdd
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociation, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociationOutput]]]

### stateTemplatesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateVehicleRequestItem

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: typing.Optional[str]

### decoderManifestArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### attributeUpdateMode
- **Type**: typing.Optional[typing.Literal['Merge', 'Overwrite']]

### stateTemplatesToAdd
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociation, aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.StateTemplateAssociationOutput]]]

### stateTemplatesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateVehicleResponse

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVehicleResponseItem

### vehicleName
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# VehicleMiddleware

### name
- **Type**: <class 'str'>
- **Required**: Yes

### protocolName
- **Type**: typing.Literal['ROS_2']
- **Required**: Yes


# VehicleStatus

### campaignName
- **Type**: typing.Optional[str]

### vehicleName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'DELETING', 'HEALTHY', 'READY', 'SUSPENDED']]


# VehicleSummary

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### decoderManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


