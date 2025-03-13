# Iotfleetwise Classes

# AssociateVehicleFleetRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateVehicleRequestTypeDef

### vehicles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.CreateVehicleRequestItemTypeDef]
- **Required**: Yes


# BatchCreateVehicleResponseTypeDef

### vehicles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.CreateVehicleResponseItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.CreateVehicleErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateVehicleRequestTypeDef

### vehicles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.UpdateVehicleRequestItemTypeDef]
- **Required**: Yes


# BatchUpdateVehicleResponseTypeDef

### vehicles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.UpdateVehicleResponseItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.UpdateVehicleErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BranchTypeDef

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]


# CampaignSummaryTypeDef

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


# CanDbcDefinitionTypeDef

### networkInterface
- **Type**: <class 'str'>
- **Required**: Yes

### canDbcFiles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.BlobTypeDef]
- **Required**: Yes

### signalsMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CanInterfaceTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### protocolName
- **Type**: typing.Optional[str]

### protocolVersion
- **Type**: typing.Optional[str]


# CanSignalTypeDef

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


# CloudWatchLogDeliveryOptionsTypeDef

### logType
- **Type**: typing.Literal['ERROR', 'OFF']
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]


# CollectionSchemeTypeDef

### timeBasedCollectionScheme
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.TimeBasedCollectionSchemeTypeDef]

### conditionBasedCollectionScheme
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.ConditionBasedCollectionSchemeTypeDef]


# ConditionBasedCollectionSchemeTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### minimumTriggerIntervalMs
- **Type**: typing.Optional[int]

### triggerMode
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'RISING_EDGE']]

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# ConditionBasedSignalFetchConfigTypeDef

### conditionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### triggerMode
- **Type**: typing.Literal['ALWAYS', 'RISING_EDGE']
- **Required**: Yes


# CreateCampaignRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.CollectionSchemeTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.TimestampTypeDef]

### expiryTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.TimestampTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalInformationTypeDef]]

### dataExtraDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]

### dataDestinationConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.DataDestinationConfigTypeDef]]

### dataPartitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.DataPartitionTypeDef]]

### signalsToFetch
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalFetchInformationUnionTypeDef]]


# CreateCampaignResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDecoderManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### signalDecoders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalDecoderUnionTypeDef]]

### networkInterfaces
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NetworkInterfaceTypeDef]]

### defaultForUnmappedSignals
- **Type**: typing.Optional[typing.Literal['CUSTOM_DECODING']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]


# CreateDecoderManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetRequestTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]


# CreateModelManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nodes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]


# CreateModelManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSignalCatalogRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### nodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NodeUnionTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]


# CreateSignalCatalogResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStateTemplateRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### signalCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateProperties
- **Type**: typing.Sequence[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### dataExtraDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### metadataExtraDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]


# CreateVehicleErrorTypeDef

### vehicleName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# CreateVehicleRequestItemTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### associationBehavior
- **Type**: typing.Optional[typing.Literal['CreateIotThing', 'ValidateIotThingExists']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]

### stateTemplates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateAssociationUnionTypeDef]]


# CreateVehicleRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### associationBehavior
- **Type**: typing.Optional[typing.Literal['CreateIotThing', 'ValidateIotThingExists']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]

### stateTemplates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateAssociationUnionTypeDef]]


# CreateVehicleResponseItemTypeDef

### vehicleName
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### thingArn
- **Type**: typing.Optional[str]


# CreateVehicleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDecodingInterfaceTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CustomPropertyTypeDef

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


# CustomStructTypeDef

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### deprecationMessage
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]


# DataDestinationConfigTypeDef

### s3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.S3ConfigTypeDef]

### timestreamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.TimestreamConfigTypeDef]

### mqttTopicConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.MqttTopicConfigTypeDef]


# DataPartitionStorageOptionsTypeDef

### maximumSize
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StorageMaximumSizeTypeDef'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'str'>
- **Required**: Yes

### minimumTimeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StorageMinimumTimeToLiveTypeDef'>
- **Required**: Yes


# DataPartitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataPartitionUploadOptionsTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# DecoderManifestSummaryTypeDef

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


# DeleteCampaignRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCampaignResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDecoderManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDecoderManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFleetRequestTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSignalCatalogRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSignalCatalogResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStateTemplateRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVehicleRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVehicleResponseTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateVehicleFleetRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# FleetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormattedVssTypeDef

### vssJson
- **Type**: typing.Optional[str]


# GetCampaignRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalInformationTypeDef]
- **Required**: Yes

### collectionScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.CollectionSchemeTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.DataDestinationConfigTypeDef]
- **Required**: Yes

### dataPartitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.DataPartitionTypeDef]
- **Required**: Yes

### signalsToFetch
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalFetchInformationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDecoderManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDecoderManifestResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEncryptionConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFleetRequestTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingOptionsResponseTypeDef

### cloudWatchLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.CloudWatchLogDeliveryOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelManifestResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegisterAccountStatusResponseTypeDef

### customerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### accountStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### timestreamRegistrationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.TimestreamRegistrationResponseTypeDef'>
- **Required**: Yes

### iamRegistrationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.IamRegistrationResponseTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSignalCatalogRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSignalCatalogResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.NodeCountsTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStateTemplateRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetVehicleRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetVehicleResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateAssociationOutputTypeDef]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVehicleStatusRequestPaginateTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# GetVehicleStatusRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetVehicleStatusResponseTypeDef

### campaigns
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.VehicleStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# IamRegistrationResponseTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]


# IamResourcesTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ImportDecoderManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### networkFileDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NetworkFileDefinitionTypeDef]
- **Required**: Yes


# ImportDecoderManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportSignalCatalogRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### vss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.FormattedVssTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]]


# ImportSignalCatalogResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCampaignsRequestPaginateTypeDef

### status
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListCampaignsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListCampaignsResponseTypeDef

### campaignSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.CampaignSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListDecoderManifestNetworkInterfacesRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDecoderManifestNetworkInterfacesResponseTypeDef

### networkInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.NetworkInterfaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestSignalsRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListDecoderManifestSignalsRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDecoderManifestSignalsResponsePaginatorTypeDef

### signalDecoders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalDecoderPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestSignalsResponseTypeDef

### signalDecoders
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalDecoderOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDecoderManifestsRequestPaginateTypeDef

### modelManifestArn
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListDecoderManifestsRequestTypeDef

### modelManifestArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListDecoderManifestsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.DecoderManifestSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsForVehicleRequestPaginateTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListFleetsForVehicleRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetsForVehicleResponseTypeDef

### fleets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsRequestPaginateTypeDef

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListFleetsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListFleetsResponseTypeDef

### fleetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.FleetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelManifestNodesRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListModelManifestNodesRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListModelManifestNodesResponseTypeDef

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.NodeOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelManifestsRequestPaginateTypeDef

### signalCatalogArn
- **Type**: typing.Optional[str]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListModelManifestsRequestTypeDef

### signalCatalogArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListModelManifestsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.ModelManifestSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSignalCatalogNodesRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### signalNodeType
- **Type**: typing.Optional[typing.Literal['ACTUATOR', 'ATTRIBUTE', 'BRANCH', 'CUSTOM_PROPERTY', 'CUSTOM_STRUCT', 'SENSOR']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListSignalCatalogNodesRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### signalNodeType
- **Type**: typing.Optional[typing.Literal['ACTUATOR', 'ATTRIBUTE', 'BRANCH', 'CUSTOM_PROPERTY', 'CUSTOM_STRUCT', 'SENSOR']]


# ListSignalCatalogNodesResponseTypeDef

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.NodeOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSignalCatalogsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListSignalCatalogsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSignalCatalogsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalCatalogSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateTemplatesRequestPaginateTypeDef

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListStateTemplatesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListStateTemplatesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVehiclesInFleetRequestPaginateTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListVehiclesInFleetRequestTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListVehiclesInFleetResponseTypeDef

### vehicles
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVehiclesRequestPaginateTypeDef

### modelManifestArn
- **Type**: typing.Optional[str]

### attributeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### attributeValues
- **Type**: typing.Optional[typing.Sequence[str]]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PaginatorConfigTypeDef]


# ListVehiclesRequestTypeDef

### modelManifestArn
- **Type**: typing.Optional[str]

### attributeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### attributeValues
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### listResponseScope
- **Type**: typing.Optional[typing.Literal['METADATA_ONLY']]


# ListVehiclesResponseTypeDef

### vehicleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.VehicleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MessageSignalOutputTypeDef

### topicName
- **Type**: <class 'str'>
- **Required**: Yes

### structuredMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageOutputTypeDef'>
- **Required**: Yes


# MessageSignalPaginatorTypeDef

### topicName
- **Type**: <class 'str'>
- **Required**: Yes

### structuredMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessagePaginatorTypeDef'>
- **Required**: Yes


# MessageSignalTypeDef

### topicName
- **Type**: <class 'str'>
- **Required**: Yes

### structuredMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageUnionTypeDef'>
- **Required**: Yes


# ModelManifestSummaryTypeDef

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


# MqttTopicConfigTypeDef

### mqttTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# NetworkFileDefinitionTypeDef

### canDbc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.CanDbcDefinitionTypeDef]


# NetworkInterfaceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeCountsTypeDef

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


# NodeOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ObdInterfaceTypeDef

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


# ObdSignalTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PeriodicStateTemplateUpdateStrategyTypeDef

### stateTemplateUpdateRate
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.TimePeriodTypeDef'>
- **Required**: Yes


# PrimitiveMessageDefinitionTypeDef

### ros2PrimitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.ROS2PrimitiveMessageDefinitionTypeDef]


# PutEncryptionConfigurationRequestTypeDef

### encryptionType
- **Type**: typing.Literal['FLEETWISE_DEFAULT_ENCRYPTION', 'KMS_BASED_ENCRYPTION']
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# PutEncryptionConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutLoggingOptionsRequestTypeDef

### cloudWatchLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.CloudWatchLogDeliveryOptionsTypeDef'>
- **Required**: Yes


# ROS2PrimitiveMessageDefinitionTypeDef

### primitiveType
- **Type**: typing.Literal['BOOL', 'BYTE', 'CHAR', 'FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'INT64', 'INT8', 'STRING', 'UINT16', 'UINT32', 'UINT64', 'UINT8', 'WSTRING']
- **Required**: Yes

### offset
- **Type**: typing.Optional[float]

### scaling
- **Type**: typing.Optional[float]

### upperBound
- **Type**: typing.Optional[int]


# RegisterAccountRequestTypeDef

### timestreamResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.TimestreamResourcesTypeDef]

### iamResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.IamResourcesTypeDef]


# RegisterAccountResponseTypeDef

### registerAccountStatus
- **Type**: typing.Literal['REGISTRATION_FAILURE', 'REGISTRATION_PENDING', 'REGISTRATION_SUCCESS']
- **Required**: Yes

### timestreamResources
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.TimestreamResourcesTypeDef'>
- **Required**: Yes

### iamResources
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.IamResourcesTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

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


# S3ConfigTypeDef

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'PARQUET']]

### storageCompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### prefix
- **Type**: typing.Optional[str]


# SignalCatalogSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# SignalDecoderOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalDecoderPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalDecoderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalFetchConfigTypeDef

### timeBased
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.TimeBasedSignalFetchConfigTypeDef]

### conditionBased
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.ConditionBasedSignalFetchConfigTypeDef]


# SignalFetchInformationOutputTypeDef

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### signalFetchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalFetchConfigTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.List[str]
- **Required**: Yes

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# SignalFetchInformationTypeDef

### fullyQualifiedName
- **Type**: <class 'str'>
- **Required**: Yes

### signalFetchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalFetchConfigTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### conditionLanguageVersion
- **Type**: typing.Optional[int]


# SignalFetchInformationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalInformationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### maxSampleCount
- **Type**: typing.Optional[int]

### minimumSamplingIntervalMs
- **Type**: typing.Optional[int]

### dataPartitionId
- **Type**: typing.Optional[str]


# StateTemplateAssociationOutputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateUpdateStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateUpdateStrategyOutputTypeDef'>
- **Required**: Yes


# StateTemplateAssociationTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### stateTemplateUpdateStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateUpdateStrategyUnionTypeDef'>
- **Required**: Yes


# StateTemplateAssociationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StateTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StateTemplateUpdateStrategyOutputTypeDef

### periodic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PeriodicStateTemplateUpdateStrategyTypeDef]

### onChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# StateTemplateUpdateStrategyTypeDef

### periodic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PeriodicStateTemplateUpdateStrategyTypeDef]

### onChange
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# StateTemplateUpdateStrategyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StorageMaximumSizeTypeDef

### unit
- **Type**: typing.Literal['GB', 'MB', 'TB']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# StorageMinimumTimeToLiveTypeDef

### unit
- **Type**: typing.Literal['DAYS', 'HOURS', 'WEEKS']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# StructuredMessageFieldNameAndDataTypePairOutputTypeDef

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# StructuredMessageFieldNameAndDataTypePairTypeDef

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# StructuredMessageFieldNameAndDataTypePairUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StructuredMessageListDefinitionOutputTypeDef

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


# StructuredMessageListDefinitionPaginatorTypeDef

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


# StructuredMessageListDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### memberType
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### listType
- **Type**: typing.Literal['DYNAMIC_BOUNDED_CAPACITY', 'DYNAMIC_UNBOUNDED_CAPACITY', 'FIXED_CAPACITY']
- **Required**: Yes

### capacity
- **Type**: typing.Optional[int]


# StructuredMessageListDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StructuredMessageOutputTypeDef

### primitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PrimitiveMessageDefinitionTypeDef]

### structuredMessageListDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageListDefinitionOutputTypeDef]

### structuredMessageDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePairOutputTypeDef]]


# StructuredMessagePaginatorTypeDef

### primitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PrimitiveMessageDefinitionTypeDef]

### structuredMessageListDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageListDefinitionPaginatorTypeDef]

### structuredMessageDefinition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef]]


# StructuredMessageTypeDef

### primitiveMessageDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.PrimitiveMessageDefinitionTypeDef]

### structuredMessageListDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageListDefinitionUnionTypeDef]

### structuredMessageDefinition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.StructuredMessageFieldNameAndDataTypePairUnionTypeDef]]


# StructuredMessageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimeBasedCollectionSchemeTypeDef

### periodMs
- **Type**: <class 'int'>
- **Required**: Yes


# TimeBasedSignalFetchConfigTypeDef

### executionFrequencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# TimePeriodTypeDef

### unit
- **Type**: typing.Literal['HOUR', 'MILLISECOND', 'MINUTE', 'SECOND']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestreamConfigTypeDef

### timestreamTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# TimestreamRegistrationResponseTypeDef

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


# TimestreamResourcesTypeDef

### timestreamDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### timestreamTableName
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCampaignRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['APPROVE', 'RESUME', 'SUSPEND', 'UPDATE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### dataExtraDimensions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateCampaignResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDecoderManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### signalDecodersToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalDecoderUnionTypeDef]]

### signalDecodersToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.SignalDecoderUnionTypeDef]]

### signalDecodersToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### networkInterfacesToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NetworkInterfaceTypeDef]]

### networkInterfacesToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NetworkInterfaceTypeDef]]

### networkInterfacesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']]

### defaultForUnmappedSignals
- **Type**: typing.Optional[typing.Literal['CUSTOM_DECODING']]


# UpdateDecoderManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFleetRequestTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateModelManifestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### nodesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### nodesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INVALID', 'VALIDATING']]


# UpdateModelManifestResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSignalCatalogRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### nodesToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NodeUnionTypeDef]]

### nodesToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.NodeUnionTypeDef]]

### nodesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateSignalCatalogResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStateTemplateRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### stateTemplatePropertiesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### stateTemplatePropertiesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### dataExtraDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### metadataExtraDimensions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateVehicleErrorTypeDef

### vehicleName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# UpdateVehicleRequestItemTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: typing.Optional[str]

### decoderManifestArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### attributeUpdateMode
- **Type**: typing.Optional[typing.Literal['Merge', 'Overwrite']]

### stateTemplatesToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateAssociationUnionTypeDef]]

### stateTemplatesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateVehicleRequestTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### modelManifestArn
- **Type**: typing.Optional[str]

### decoderManifestArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### attributeUpdateMode
- **Type**: typing.Optional[typing.Literal['Merge', 'Overwrite']]

### stateTemplatesToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotfleetwise_classes.StateTemplateAssociationUnionTypeDef]]

### stateTemplatesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateVehicleResponseItemTypeDef

### vehicleName
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# UpdateVehicleResponseTypeDef

### vehicleName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleetwise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VehicleMiddlewareTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### protocolName
- **Type**: typing.Literal['ROS_2']
- **Required**: Yes


# VehicleStatusTypeDef

### campaignName
- **Type**: typing.Optional[str]

### vehicleName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'DELETING', 'HEALTHY', 'READY', 'SUSPENDED']]


# VehicleSummaryTypeDef

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


