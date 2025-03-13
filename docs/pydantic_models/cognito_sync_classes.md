# Cognito Sync Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BulkPublishRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# BulkPublishResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CognitoStreamsTypeDef

### StreamName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### StreamingStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DatasetTypeDef

### IdentityId
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### DataStorage
- **Type**: typing.Optional[int]

### NumRecords
- **Type**: typing.Optional[int]


# DeleteDatasetRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetResponseTypeDef

### Dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.DatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### Dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.DatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIdentityPoolUsageRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityPoolUsageResponseTypeDef

### IdentityPoolUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.IdentityPoolUsageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIdentityUsageRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityUsageResponseTypeDef

### IdentityUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.IdentityUsageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBulkPublishDetailsRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBulkPublishDetailsResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### BulkPublishStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BulkPublishCompleteTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BulkPublishStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SUCCEEDED']
- **Required**: Yes

### FailureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCognitoEventsRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCognitoEventsResponseTypeDef

### Events
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityPoolConfigurationRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityPoolConfigurationResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.PushSyncOutputTypeDef'>
- **Required**: Yes

### CognitoStreams
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.CognitoStreamsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityPoolUsageTypeDef

### IdentityPoolId
- **Type**: typing.Optional[str]

### SyncSessionsCount
- **Type**: typing.Optional[int]

### DataStorage
- **Type**: typing.Optional[int]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# IdentityUsageTypeDef

### IdentityId
- **Type**: typing.Optional[str]

### IdentityPoolId
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### DatasetCount
- **Type**: typing.Optional[int]

### DataStorage
- **Type**: typing.Optional[int]


# ListDatasetsRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync_classes.DatasetTypeDef]
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoolUsageRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIdentityPoolUsageResponseTypeDef

### IdentityPoolUsages
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync_classes.IdentityPoolUsageTypeDef]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecordsRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### LastSyncCount
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SyncSessionToken
- **Type**: typing.Optional[str]


# ListRecordsResponseTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync_classes.RecordTypeDef]
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### DatasetSyncCount
- **Type**: <class 'int'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### MergedDatasetNames
- **Type**: typing.List[str]
- **Required**: Yes

### DatasetExists
- **Type**: <class 'bool'>
- **Required**: Yes

### DatasetDeletedAfterRequestedSyncCount
- **Type**: <class 'bool'>
- **Required**: Yes

### SyncSessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PushSyncOutputTypeDef

### ApplicationArns
- **Type**: typing.Optional[typing.List[str]]

### RoleArn
- **Type**: typing.Optional[str]


# PushSyncTypeDef

### ApplicationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleArn
- **Type**: typing.Optional[str]


# PushSyncUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordPatchTypeDef

### Op
- **Type**: typing.Literal['remove', 'replace']
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### SyncCount
- **Type**: <class 'int'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]

### DeviceLastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_sync_classes.TimestampTypeDef]


# RecordTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### SyncCount
- **Type**: typing.Optional[int]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### DeviceLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# RegisterDeviceRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'GCM']
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterDeviceResponseTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
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


# SetCognitoEventsRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetIdentityPoolConfigurationRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_sync_classes.PushSyncUnionTypeDef]

### CognitoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_sync_classes.CognitoStreamsTypeDef]


# SetIdentityPoolConfigurationResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.PushSyncOutputTypeDef'>
- **Required**: Yes

### CognitoStreams
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.CognitoStreamsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubscribeToDatasetRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnsubscribeFromDatasetRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRecordsRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncSessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: typing.Optional[str]

### RecordPatches
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_sync_classes.RecordPatchTypeDef]]

### ClientContext
- **Type**: typing.Optional[str]


# UpdateRecordsResponseTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync_classes.RecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


