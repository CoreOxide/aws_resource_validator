# Finspace Classes

# AutoScalingConfigurationTypeDef

### minNodeCount
- **Type**: typing.Optional[int]

### maxNodeCount
- **Type**: typing.Optional[int]

### autoScalingMetric
- **Type**: typing.Optional[typing.Literal['CPU_UTILIZATION_PERCENTAGE']]

### metricTarget
- **Type**: typing.Optional[float]

### scaleInCooldownSeconds
- **Type**: typing.Optional[float]

### scaleOutCooldownSeconds
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityConfigurationTypeDef

### nodeType
- **Type**: typing.Optional[str]

### nodeCount
- **Type**: typing.Optional[int]


# ChangeRequestTypeDef

### changeType
- **Type**: typing.Literal['DELETE', 'PUT']
- **Required**: Yes

### dbPath
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: typing.Optional[str]


# CodeConfigurationTypeDef

### s3Bucket
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### s3ObjectVersion
- **Type**: typing.Optional[str]


# CreateEnvironmentRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### federationMode
- **Type**: typing.Optional[typing.Literal['FEDERATED', 'LOCAL']]

### federationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.FederationParametersUnionTypeDef]

### superuserParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.SuperuserParametersTypeDef]

### dataBundles
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateEnvironmentResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxChangesetRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### changeRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.ChangeRequestTypeDef]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateKxChangesetResponseTypeDef

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### changeRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.ChangeRequestTypeDef]
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'PENDING', 'PROCESSING']
- **Required**: Yes

### errorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ErrorInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxClusterRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterType
- **Type**: typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### vpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.VpcConfigurationUnionTypeDef'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tickerplantLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.TickerplantLogConfigurationUnionTypeDef]

### databases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationUnionTypeDef]]

### cacheStorageConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxCacheStorageConfigurationTypeDef]]

### autoScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.AutoScalingConfigurationTypeDef]

### clusterDescription
- **Type**: typing.Optional[str]

### capacityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.CapacityConfigurationTypeDef]

### initializationScript
- **Type**: typing.Optional[str]

### commandLineArguments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgumentTypeDef]]

### code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.CodeConfigurationTypeDef]

### executionRole
- **Type**: typing.Optional[str]

### savedownStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxSavedownStorageConfigurationTypeDef]

### availabilityZoneId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### scalingGroupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupConfigurationTypeDef]


# CreateKxClusterResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'PENDING', 'RUNNING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterType
- **Type**: typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']
- **Required**: Yes

### tickerplantLogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TickerplantLogConfigurationOutputTypeDef'>
- **Required**: Yes

### volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.VolumeTypeDef]
- **Required**: Yes

### databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationOutputTypeDef]
- **Required**: Yes

### cacheStorageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCacheStorageConfigurationTypeDef]
- **Required**: Yes

### autoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.AutoScalingConfigurationTypeDef'>
- **Required**: Yes

### clusterDescription
- **Type**: <class 'str'>
- **Required**: Yes

### capacityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CapacityConfigurationTypeDef'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### vpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.VpcConfigurationOutputTypeDef'>
- **Required**: Yes

### initializationScript
- **Type**: <class 'str'>
- **Required**: Yes

### commandLineArguments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgumentTypeDef]
- **Required**: Yes

### code
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CodeConfigurationTypeDef'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### savedownStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxSavedownStorageConfigurationTypeDef'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### scalingGroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxDatabaseRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKxDatabaseResponseTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxDataviewRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZoneId
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationUnionTypeDef]]

### autoUpdate
- **Type**: typing.Optional[bool]

### readWrite
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKxDataviewResponseTypeDef

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### segmentConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutputTypeDef]
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### autoUpdate
- **Type**: <class 'bool'>
- **Required**: Yes

### readWrite
- **Type**: <class 'bool'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxEnvironmentRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateKxEnvironmentResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_REQUESTED', 'CREATING', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATING_NETWORK', 'RETRY_DELETION', 'SUSPENDED', 'UPDATE_NETWORK_REQUESTED', 'UPDATING_NETWORK']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxScalingGroupRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### hostType
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKxScalingGroupResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### hostType
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxUserRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateKxUserResponseTypeDef

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKxVolumeRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeType
- **Type**: typing.Literal['NAS_1']
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### nas1Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxNAS1ConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKxVolumeResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### volumeType
- **Type**: typing.Literal['NAS_1']
- **Required**: Yes

### volumeArn
- **Type**: <class 'str'>
- **Required**: Yes

### nas1Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxNAS1ConfigurationTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.List[str]
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDNSServerTypeDef

### customDNSServerName
- **Type**: <class 'str'>
- **Required**: Yes

### customDNSServerIP
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxClusterNodeRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxClusterRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxDatabaseRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxDataviewRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxScalingGroupRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxUserRequestTypeDef

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxVolumeRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EnvironmentTypeDef

### name
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATE_REQUESTED', 'CREATING', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATING_NETWORK', 'RETRY_DELETION', 'SUSPENDED', 'UPDATE_NETWORK_REQUESTED', 'UPDATING_NETWORK']]

### environmentUrl
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentArn
- **Type**: typing.Optional[str]

### sageMakerStudioDomainUrl
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### dedicatedServiceAccountId
- **Type**: typing.Optional[str]

### federationMode
- **Type**: typing.Optional[typing.Literal['FEDERATED', 'LOCAL']]

### federationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.FederationParametersOutputTypeDef]


# ErrorInfoTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### errorType
- **Type**: typing.Optional[typing.Literal['A user recoverable error has occurred', 'An internal error has occurred.', 'Cancelled', 'Missing required permission to perform this request.', 'One or more inputs to this request were not found.', 'Service limits have been exceeded.', 'The inputs to this request are invalid.', 'The system temporarily lacks sufficient resources to process the request.']]


# FederationParametersOutputTypeDef

### samlMetadataDocument
- **Type**: typing.Optional[str]

### samlMetadataURL
- **Type**: typing.Optional[str]

### applicationCallBackURL
- **Type**: typing.Optional[str]

### federationURN
- **Type**: typing.Optional[str]

### federationProviderName
- **Type**: typing.Optional[str]

### attributeMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# FederationParametersTypeDef

### samlMetadataDocument
- **Type**: typing.Optional[str]

### samlMetadataURL
- **Type**: typing.Optional[str]

### applicationCallBackURL
- **Type**: typing.Optional[str]

### federationURN
- **Type**: typing.Optional[str]

### federationProviderName
- **Type**: typing.Optional[str]

### attributeMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FederationParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxChangesetRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxChangesetResponseTypeDef

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### changeRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.ChangeRequestTypeDef]
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### activeFromTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'PENDING', 'PROCESSING']
- **Required**: Yes

### errorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ErrorInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxClusterRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxClusterResponseTypeDef

### status
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'PENDING', 'RUNNING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterType
- **Type**: typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']
- **Required**: Yes

### tickerplantLogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TickerplantLogConfigurationOutputTypeDef'>
- **Required**: Yes

### volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.VolumeTypeDef]
- **Required**: Yes

### databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationOutputTypeDef]
- **Required**: Yes

### cacheStorageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCacheStorageConfigurationTypeDef]
- **Required**: Yes

### autoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.AutoScalingConfigurationTypeDef'>
- **Required**: Yes

### clusterDescription
- **Type**: <class 'str'>
- **Required**: Yes

### capacityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CapacityConfigurationTypeDef'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### vpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.VpcConfigurationOutputTypeDef'>
- **Required**: Yes

### initializationScript
- **Type**: <class 'str'>
- **Required**: Yes

### commandLineArguments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgumentTypeDef]
- **Required**: Yes

### code
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CodeConfigurationTypeDef'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### savedownStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxSavedownStorageConfigurationTypeDef'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### scalingGroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxConnectionStringRequestTypeDef

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxConnectionStringResponseTypeDef

### signedConnectionString
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxDatabaseRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxDatabaseResponseTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastCompletedChangesetId
- **Type**: <class 'str'>
- **Required**: Yes

### numBytes
- **Type**: <class 'int'>
- **Required**: Yes

### numChangesets
- **Type**: <class 'int'>
- **Required**: Yes

### numFiles
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxDataviewRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxDataviewResponseTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### segmentConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutputTypeDef]
- **Required**: Yes

### activeVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewActiveVersionTypeDef]
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### autoUpdate
- **Type**: <class 'bool'>
- **Required**: Yes

### readWrite
- **Type**: <class 'bool'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxEnvironmentResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_REQUESTED', 'CREATING', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATING_NETWORK', 'RETRY_DELETION', 'SUSPENDED', 'UPDATE_NETWORK_REQUESTED', 'UPDATING_NETWORK']
- **Required**: Yes

### tgwStatus
- **Type**: typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']
- **Required**: Yes

### dnsStatus
- **Type**: typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### dedicatedServiceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### transitGatewayConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutputTypeDef'>
- **Required**: Yes

### customDNSConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServerTypeDef]
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.List[str]
- **Required**: Yes

### certificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxScalingGroupRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxScalingGroupResponseTypeDef

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### hostType
- **Type**: <class 'str'>
- **Required**: Yes

### clusters
- **Type**: typing.List[str]
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxUserRequestTypeDef

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxUserResponseTypeDef

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKxVolumeRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxVolumeResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### volumeType
- **Type**: typing.Literal['NAS_1']
- **Required**: Yes

### volumeArn
- **Type**: <class 'str'>
- **Required**: Yes

### nas1Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxNAS1ConfigurationTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.List[str]
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### attachedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxAttachedClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IcmpTypeCodeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxAttachedClusterTypeDef

### clusterName
- **Type**: typing.Optional[str]

### clusterType
- **Type**: typing.Optional[typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']]

### clusterStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'PENDING', 'RUNNING', 'UPDATING']]


# KxCacheStorageConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxChangesetListEntryTypeDef

### changesetId
- **Type**: typing.Optional[str]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### activeFromTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'PENDING', 'PROCESSING']]


# KxClusterCodeDeploymentConfigurationTypeDef

### deploymentStrategy
- **Type**: typing.Literal['FORCE', 'NO_RESTART', 'ROLLING']
- **Required**: Yes


# KxClusterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'PENDING', 'RUNNING', 'UPDATING']]

### statusReason
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### clusterType
- **Type**: typing.Optional[typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']]

### clusterDescription
- **Type**: typing.Optional[str]

### releaseLabel
- **Type**: typing.Optional[str]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.VolumeTypeDef]]

### initializationScript
- **Type**: typing.Optional[str]

### executionRole
- **Type**: typing.Optional[str]

### azMode
- **Type**: typing.Optional[typing.Literal['MULTI', 'SINGLE']]

### availabilityZoneId
- **Type**: typing.Optional[str]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KxCommandLineArgumentTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# KxDatabaseCacheConfigurationOutputTypeDef

### cacheType
- **Type**: <class 'str'>
- **Required**: Yes

### dbPaths
- **Type**: typing.List[str]
- **Required**: Yes

### dataviewName
- **Type**: typing.Optional[str]


# KxDatabaseCacheConfigurationTypeDef

### cacheType
- **Type**: <class 'str'>
- **Required**: Yes

### dbPaths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### dataviewName
- **Type**: typing.Optional[str]


# KxDatabaseCacheConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDatabaseConfigurationOutputTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### cacheConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseCacheConfigurationOutputTypeDef]]

### changesetId
- **Type**: typing.Optional[str]

### dataviewName
- **Type**: typing.Optional[str]

### dataviewConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewConfigurationOutputTypeDef]


# KxDatabaseConfigurationTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### cacheConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseCacheConfigurationUnionTypeDef]]

### changesetId
- **Type**: typing.Optional[str]

### dataviewName
- **Type**: typing.Optional[str]

### dataviewConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewConfigurationUnionTypeDef]


# KxDatabaseConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDatabaseListEntryTypeDef

### databaseName
- **Type**: typing.Optional[str]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KxDataviewActiveVersionTypeDef

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutputTypeDef]]

### attachedClusters
- **Type**: typing.Optional[typing.List[str]]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### versionId
- **Type**: typing.Optional[str]


# KxDataviewConfigurationOutputTypeDef

### dataviewName
- **Type**: typing.Optional[str]

### dataviewVersionId
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutputTypeDef]]


# KxDataviewConfigurationTypeDef

### dataviewName
- **Type**: typing.Optional[str]

### dataviewVersionId
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationUnionTypeDef]]


# KxDataviewConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDataviewListEntryTypeDef

### environmentId
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]

### dataviewName
- **Type**: typing.Optional[str]

### azMode
- **Type**: typing.Optional[typing.Literal['MULTI', 'SINGLE']]

### availabilityZoneId
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutputTypeDef]]

### activeVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewActiveVersionTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### description
- **Type**: typing.Optional[str]

### autoUpdate
- **Type**: typing.Optional[bool]

### readWrite
- **Type**: typing.Optional[bool]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### statusReason
- **Type**: typing.Optional[str]


# KxDataviewSegmentConfigurationOutputTypeDef

### dbPaths
- **Type**: typing.List[str]
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### onDemand
- **Type**: typing.Optional[bool]


# KxDataviewSegmentConfigurationTypeDef

### dbPaths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### onDemand
- **Type**: typing.Optional[bool]


# KxDataviewSegmentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDeploymentConfigurationTypeDef

### deploymentStrategy
- **Type**: typing.Literal['NO_RESTART', 'ROLLING']
- **Required**: Yes


# KxEnvironmentTypeDef

### name
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATE_REQUESTED', 'CREATING', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATING_NETWORK', 'RETRY_DELETION', 'SUSPENDED', 'UPDATE_NETWORK_REQUESTED', 'UPDATING_NETWORK']]

### tgwStatus
- **Type**: typing.Optional[typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']]

### dnsStatus
- **Type**: typing.Optional[typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']]

### errorMessage
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentArn
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### dedicatedServiceAccountId
- **Type**: typing.Optional[str]

### transitGatewayConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutputTypeDef]

### customDNSConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServerTypeDef]]

### creationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### updateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### availabilityZoneIds
- **Type**: typing.Optional[typing.List[str]]

### certificateAuthorityArn
- **Type**: typing.Optional[str]


# KxNAS1ConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxNodeTypeDef

### nodeId
- **Type**: typing.Optional[str]

### availabilityZoneId
- **Type**: typing.Optional[str]

### launchTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['PROVISIONING', 'RUNNING']]


# KxSavedownStorageConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxScalingGroupConfigurationTypeDef

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### memoryReservation
- **Type**: <class 'int'>
- **Required**: Yes

### nodeCount
- **Type**: <class 'int'>
- **Required**: Yes

### memoryLimit
- **Type**: typing.Optional[int]

### cpu
- **Type**: typing.Optional[float]


# KxScalingGroupTypeDef

### scalingGroupName
- **Type**: typing.Optional[str]

### hostType
- **Type**: typing.Optional[str]

### clusters
- **Type**: typing.Optional[typing.List[str]]

### availabilityZoneId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']]

### statusReason
- **Type**: typing.Optional[str]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KxUserTypeDef

### userArn
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]

### iamRole
- **Type**: typing.Optional[str]

### createTimestamp
- **Type**: typing.Optional[datetime.datetime]

### updateTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KxVolumeTypeDef

### volumeName
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[typing.Literal['NAS_1']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']]

### description
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### azMode
- **Type**: typing.Optional[typing.Literal['MULTI', 'SINGLE']]

### availabilityZoneIds
- **Type**: typing.Optional[typing.List[str]]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ListEnvironmentsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.EnvironmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxChangesetsRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxChangesetsResponseTypeDef

### kxChangesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxChangesetListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxClusterNodesRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxClusterNodesResponseTypeDef

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxNodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxClustersRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterType
- **Type**: typing.Optional[typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKxClustersResponseTypeDef

### kxClusterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxDatabasesRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxDatabasesResponseTypeDef

### kxDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxDataviewsRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxDataviewsResponseTypeDef

### kxDataviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxEnvironmentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.PaginatorConfigTypeDef]


# ListKxEnvironmentsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxEnvironmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxScalingGroupsRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKxScalingGroupsResponseTypeDef

### scalingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxUsersRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxUsersResponseTypeDef

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxUserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxVolumesRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[typing.Literal['NAS_1']]


# ListKxVolumesResponseTypeDef

### kxVolumeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxVolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NetworkACLEntryTypeDef

### ruleNumber
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: <class 'str'>
- **Required**: Yes

### ruleAction
- **Type**: typing.Literal['allow', 'deny']
- **Required**: Yes

### cidrBlock
- **Type**: <class 'str'>
- **Required**: Yes

### portRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.PortRangeTypeDef]

### icmpTypeCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.IcmpTypeCodeTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortRangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SuperuserParametersTypeDef

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### firstName
- **Type**: <class 'str'>
- **Required**: Yes

### lastName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TickerplantLogConfigurationOutputTypeDef

### tickerplantLogVolumes
- **Type**: typing.Optional[typing.List[str]]


# TickerplantLogConfigurationTypeDef

### tickerplantLogVolumes
- **Type**: typing.Optional[typing.Sequence[str]]


# TickerplantLogConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransitGatewayConfigurationOutputTypeDef

### transitGatewayID
- **Type**: <class 'str'>
- **Required**: Yes

### routableCIDRSpace
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentNetworkAclConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.NetworkACLEntryTypeDef]]


# TransitGatewayConfigurationTypeDef

### transitGatewayID
- **Type**: <class 'str'>
- **Required**: Yes

### routableCIDRSpace
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentNetworkAclConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.NetworkACLEntryTypeDef]]


# TransitGatewayConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### federationMode
- **Type**: typing.Optional[typing.Literal['FEDERATED', 'LOCAL']]

### federationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.FederationParametersUnionTypeDef]


# UpdateEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKxClusterCodeConfigurationRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CodeConfigurationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### initializationScript
- **Type**: typing.Optional[str]

### commandLineArguments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgumentTypeDef]]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxClusterCodeDeploymentConfigurationTypeDef]


# UpdateKxClusterDatabasesRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### databases
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationUnionTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxDeploymentConfigurationTypeDef]


# UpdateKxDatabaseRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateKxDatabaseResponseTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKxDataviewRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationUnionTypeDef]]


# UpdateKxDataviewResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### segmentConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutputTypeDef]
- **Required**: Yes

### activeVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewActiveVersionTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### autoUpdate
- **Type**: <class 'bool'>
- **Required**: Yes

### readWrite
- **Type**: <class 'bool'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKxEnvironmentNetworkRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### transitGatewayConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationUnionTypeDef]

### customDNSConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServerTypeDef]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateKxEnvironmentNetworkResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_REQUESTED', 'CREATING', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATING_NETWORK', 'RETRY_DELETION', 'SUSPENDED', 'UPDATE_NETWORK_REQUESTED', 'UPDATING_NETWORK']
- **Required**: Yes

### tgwStatus
- **Type**: typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']
- **Required**: Yes

### dnsStatus
- **Type**: typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### dedicatedServiceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### transitGatewayConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutputTypeDef'>
- **Required**: Yes

### customDNSConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServerTypeDef]
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKxEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateKxEnvironmentResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_REQUESTED', 'CREATING', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATING_NETWORK', 'RETRY_DELETION', 'SUSPENDED', 'UPDATE_NETWORK_REQUESTED', 'UPDATING_NETWORK']
- **Required**: Yes

### tgwStatus
- **Type**: typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']
- **Required**: Yes

### dnsStatus
- **Type**: typing.Literal['FAILED_UPDATE', 'NONE', 'SUCCESSFULLY_UPDATED', 'UPDATE_REQUESTED', 'UPDATING']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### environmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### dedicatedServiceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### transitGatewayConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutputTypeDef'>
- **Required**: Yes

### customDNSConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServerTypeDef]
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKxUserRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateKxUserResponseTypeDef

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKxVolumeRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### nas1Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxNAS1ConfigurationTypeDef]


# UpdateKxVolumeResponseTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### volumeType
- **Type**: typing.Literal['NAS_1']
- **Required**: Yes

### volumeArn
- **Type**: <class 'str'>
- **Required**: Yes

### nas1Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxNAS1ConfigurationTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### availabilityZoneIds
- **Type**: typing.List[str]
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### attachedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxAttachedClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VolumeTypeDef

### volumeName
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[typing.Literal['NAS_1']]


# VpcConfigurationOutputTypeDef

### vpcId
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['IP_V4']]


# VpcConfigurationTypeDef

### vpcId
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['IP_V4']]


# VpcConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

