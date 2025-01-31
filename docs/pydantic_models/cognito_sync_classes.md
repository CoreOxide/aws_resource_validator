# Cognito Sync Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BulkPublishRequestRequestTypeDef

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


# DeleteDatasetRequestRequestTypeDef

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


# DescribeDatasetRequestRequestTypeDef

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


# DescribeIdentityPoolUsageRequestRequestTypeDef

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


# DescribeIdentityUsageRequestRequestTypeDef

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


# GetBulkPublishDetailsRequestRequestTypeDef

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


# GetCognitoEventsRequestRequestTypeDef

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


# GetIdentityPoolConfigurationRequestRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityPoolConfigurationResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.PushSyncTypeDef'>
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


# ListDatasetsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdentityPoolUsageRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecordsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
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


# PushSyncTypeDef

### ApplicationArns
- **Type**: typing.Optional[typing.List[str]]

### RoleArn
- **Type**: typing.Optional[str]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# RegisterDeviceRequestRequestTypeDef

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

### HostId
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


# SetCognitoEventsRequestRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetIdentityPoolConfigurationRequestRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_sync_classes.PushSyncTypeDef]

### CognitoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_sync_classes.CognitoStreamsTypeDef]


# SetIdentityPoolConfigurationResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.PushSyncTypeDef'>
- **Required**: Yes

### CognitoStreams
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.CognitoStreamsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubscribeToDatasetRequestRequestTypeDef

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


# UnsubscribeFromDatasetRequestRequestTypeDef

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


# UpdateRecordsRequestRequestTypeDef

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


