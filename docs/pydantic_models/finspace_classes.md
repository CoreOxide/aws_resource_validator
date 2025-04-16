# Finspace Classes

# AutoScalingConfiguration

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

# CapacityConfiguration

### nodeType
- **Type**: typing.Optional[str]

### nodeCount
- **Type**: typing.Optional[int]


# ChangeRequest

### changeType
- **Type**: typing.Literal['DELETE', 'PUT']
- **Required**: Yes

### dbPath
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: typing.Optional[str]


# CodeConfiguration

### s3Bucket
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### s3ObjectVersion
- **Type**: typing.Optional[str]


# CreateEnvironmentRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.FederationParametersUnion]

### superuserParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.SuperuserParameters]

### dataBundles
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateEnvironmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxChangesetRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### changeRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.ChangeRequest]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateKxChangesetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.ChangeRequest]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ErrorInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxClusterRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.VpcConfigurationUnion'>
- **Required**: Yes

### azMode
- **Type**: typing.Literal['MULTI', 'SINGLE']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tickerplantLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.TickerplantLogConfigurationUnion]

### databases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationUnion]]

### cacheStorageConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxCacheStorageConfiguration]]

### autoScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.AutoScalingConfiguration]

### clusterDescription
- **Type**: typing.Optional[str]

### capacityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.CapacityConfiguration]

### initializationScript
- **Type**: typing.Optional[str]

### commandLineArguments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgument]]

### code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.CodeConfiguration]

### executionRole
- **Type**: typing.Optional[str]

### savedownStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxSavedownStorageConfiguration]

### availabilityZoneId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### scalingGroupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupConfiguration]


# CreateKxClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TickerplantLogConfigurationOutput'>
- **Required**: Yes

### volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.Volume]
- **Required**: Yes

### databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationOutput]
- **Required**: Yes

### cacheStorageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCacheStorageConfiguration]
- **Required**: Yes

### autoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.AutoScalingConfiguration'>
- **Required**: Yes

### clusterDescription
- **Type**: <class 'str'>
- **Required**: Yes

### capacityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CapacityConfiguration'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### vpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.VpcConfigurationOutput'>
- **Required**: Yes

### initializationScript
- **Type**: <class 'str'>
- **Required**: Yes

### commandLineArguments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgument]
- **Required**: Yes

### code
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CodeConfiguration'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### savedownStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxSavedownStorageConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxDatabaseRequest

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


# CreateKxDatabaseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxDataviewRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationUnion]]

### autoUpdate
- **Type**: typing.Optional[bool]

### readWrite
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKxDataviewResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxEnvironmentRequest

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


# CreateKxEnvironmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxScalingGroupRequest

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


# CreateKxScalingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxUserRequest

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


# CreateKxUserResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKxVolumeRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxNAS1Configuration]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKxVolumeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxNAS1Configuration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDNSServer

### customDNSServerName
- **Type**: <class 'str'>
- **Required**: Yes

### customDNSServerIP
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxClusterNodeRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxClusterRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxDatabaseRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKxDataviewRequest

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


# DeleteKxEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxScalingGroupRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxUserRequest

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKxVolumeRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# Environment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.FederationParametersOutput]


# ErrorInfo

### errorMessage
- **Type**: typing.Optional[str]

### errorType
- **Type**: typing.Optional[typing.Literal['A user recoverable error has occurred', 'An internal error has occurred.', 'Cancelled', 'Missing required permission to perform this request.', 'One or more inputs to this request were not found.', 'Service limits have been exceeded.', 'The inputs to this request are invalid.', 'The system temporarily lacks sufficient resources to process the request.']]


# FederationParameters

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


# FederationParametersOutput

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


# FederationParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxChangesetRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxChangesetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.ChangeRequest]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ErrorInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxClusterRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TickerplantLogConfigurationOutput'>
- **Required**: Yes

### volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.Volume]
- **Required**: Yes

### databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationOutput]
- **Required**: Yes

### cacheStorageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCacheStorageConfiguration]
- **Required**: Yes

### autoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.AutoScalingConfiguration'>
- **Required**: Yes

### clusterDescription
- **Type**: <class 'str'>
- **Required**: Yes

### capacityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CapacityConfiguration'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### vpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.VpcConfigurationOutput'>
- **Required**: Yes

### initializationScript
- **Type**: <class 'str'>
- **Required**: Yes

### commandLineArguments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgument]
- **Required**: Yes

### code
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CodeConfiguration'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### savedownStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxSavedownStorageConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroupConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxConnectionStringRequest

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxConnectionStringResponse

### signedConnectionString
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxDatabaseRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxDatabaseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxDataviewRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### dataviewName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxDataviewResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutput]
- **Required**: Yes

### activeVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewActiveVersion]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxEnvironmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutput'>
- **Required**: Yes

### customDNSConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServer]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxScalingGroupRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxScalingGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxUserRequest

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxUserResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetKxVolumeRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKxVolumeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxNAS1Configuration'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxAttachedCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# IcmpTypeCode

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxAttachedCluster

### clusterName
- **Type**: typing.Optional[str]

### clusterType
- **Type**: typing.Optional[typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']]

### clusterStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'PENDING', 'RUNNING', 'UPDATING']]


# KxCacheStorageConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxChangesetListEntry

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


# KxCluster

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.Volume]]

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


# KxClusterCodeDeploymentConfiguration

### deploymentStrategy
- **Type**: typing.Literal['FORCE', 'NO_RESTART', 'ROLLING']
- **Required**: Yes


# KxCommandLineArgument

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# KxDatabaseCacheConfiguration

### cacheType
- **Type**: <class 'str'>
- **Required**: Yes

### dbPaths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### dataviewName
- **Type**: typing.Optional[str]


# KxDatabaseCacheConfigurationOutput

### cacheType
- **Type**: <class 'str'>
- **Required**: Yes

### dbPaths
- **Type**: typing.List[str]
- **Required**: Yes

### dataviewName
- **Type**: typing.Optional[str]


# KxDatabaseCacheConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDatabaseConfiguration

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### cacheConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseCacheConfigurationUnion]]

### changesetId
- **Type**: typing.Optional[str]

### dataviewName
- **Type**: typing.Optional[str]

### dataviewConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewConfigurationUnion]


# KxDatabaseConfigurationOutput

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### cacheConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseCacheConfigurationOutput]]

### changesetId
- **Type**: typing.Optional[str]

### dataviewName
- **Type**: typing.Optional[str]

### dataviewConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewConfigurationOutput]


# KxDatabaseConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDatabaseListEntry

### databaseName
- **Type**: typing.Optional[str]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KxDataviewActiveVersion

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutput]]

### attachedClusters
- **Type**: typing.Optional[typing.List[str]]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]

### versionId
- **Type**: typing.Optional[str]


# KxDataviewConfiguration

### dataviewName
- **Type**: typing.Optional[str]

### dataviewVersionId
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationUnion]]


# KxDataviewConfigurationOutput

### dataviewName
- **Type**: typing.Optional[str]

### dataviewVersionId
- **Type**: typing.Optional[str]

### changesetId
- **Type**: typing.Optional[str]

### segmentConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutput]]


# KxDataviewConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDataviewListEntry

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutput]]

### activeVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewActiveVersion]]

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


# KxDataviewSegmentConfiguration

### dbPaths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### onDemand
- **Type**: typing.Optional[bool]


# KxDataviewSegmentConfigurationOutput

### dbPaths
- **Type**: typing.List[str]
- **Required**: Yes

### volumeName
- **Type**: <class 'str'>
- **Required**: Yes

### onDemand
- **Type**: typing.Optional[bool]


# KxDataviewSegmentConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxDeploymentConfiguration

### deploymentStrategy
- **Type**: typing.Literal['NO_RESTART', 'ROLLING']
- **Required**: Yes


# KxEnvironment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutput]

### customDNSConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServer]]

### creationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### updateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### availabilityZoneIds
- **Type**: typing.Optional[typing.List[str]]

### certificateAuthorityArn
- **Type**: typing.Optional[str]


# KxNAS1Configuration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxNode

### nodeId
- **Type**: typing.Optional[str]

### availabilityZoneId
- **Type**: typing.Optional[str]

### launchTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['PROVISIONING', 'RUNNING']]


# KxSavedownStorageConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KxScalingGroup

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


# KxScalingGroupConfiguration

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


# KxUser

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


# KxVolume

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


# ListEnvironmentsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsResponse

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.Environment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxChangesetsRequest

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


# ListKxChangesetsResponse

### kxChangesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxChangesetListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxClusterNodesRequest

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


# ListKxClusterNodesResponse

### nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxNode]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxClustersRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterType
- **Type**: typing.Optional[typing.Literal['GATEWAY', 'GP', 'HDB', 'RDB', 'TICKERPLANT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKxClustersResponse

### kxClusterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxDatabasesRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxDatabasesResponse

### kxDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxDataviewsRequest

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


# ListKxDataviewsResponse

### kxDataviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxEnvironmentsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxEnvironmentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.PaginatorConfig]


# ListKxEnvironmentsResponse

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxEnvironment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxScalingGroupsRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKxScalingGroupsResponse

### scalingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxScalingGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxUsersRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKxUsersResponse

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxUser]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKxVolumesRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[typing.Literal['NAS_1']]


# ListKxVolumesResponse

### kxVolumeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxVolume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# NetworkACLEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.PortRange]

### icmpTypeCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.IcmpTypeCode]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortRange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SuperuserParameters

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### firstName
- **Type**: <class 'str'>
- **Required**: Yes

### lastName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TickerplantLogConfiguration

### tickerplantLogVolumes
- **Type**: typing.Optional[typing.Sequence[str]]


# TickerplantLogConfigurationOutput

### tickerplantLogVolumes
- **Type**: typing.Optional[typing.List[str]]


# TickerplantLogConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransitGatewayConfiguration

### transitGatewayID
- **Type**: <class 'str'>
- **Required**: Yes

### routableCIDRSpace
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentNetworkAclConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.NetworkACLEntry]]


# TransitGatewayConfigurationOutput

### transitGatewayID
- **Type**: <class 'str'>
- **Required**: Yes

### routableCIDRSpace
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentNetworkAclConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_classes.NetworkACLEntry]]


# TransitGatewayConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.FederationParametersUnion]


# UpdateEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKxClusterCodeConfigurationRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.CodeConfiguration'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### initializationScript
- **Type**: typing.Optional[str]

### commandLineArguments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxCommandLineArgument]]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxClusterCodeDeploymentConfiguration]


# UpdateKxClusterDatabasesRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### databases
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDatabaseConfigurationUnion]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxDeploymentConfiguration]


# UpdateKxDatabaseRequest

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


# UpdateKxDatabaseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKxDataviewRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationUnion]]


# UpdateKxDataviewResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewSegmentConfigurationOutput]
- **Required**: Yes

### activeVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxDataviewActiveVersion]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKxEnvironmentNetworkRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### transitGatewayConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationUnion]

### customDNSConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServer]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateKxEnvironmentNetworkResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutput'>
- **Required**: Yes

### customDNSConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServer]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKxEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateKxEnvironmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.TransitGatewayConfigurationOutput'>
- **Required**: Yes

### customDNSConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.CustomDNSServer]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKxUserRequest

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


# UpdateKxUserResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKxVolumeRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_classes.KxNAS1Configuration]


# UpdateKxVolumeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.KxNAS1Configuration'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_classes.KxAttachedCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_classes.ResponseMetadata'>
- **Required**: Yes


# Volume

### volumeName
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[typing.Literal['NAS_1']]


# VpcConfiguration

### vpcId
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['IP_V4']]


# VpcConfigurationOutput

### vpcId
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['IP_V4']]


# VpcConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

