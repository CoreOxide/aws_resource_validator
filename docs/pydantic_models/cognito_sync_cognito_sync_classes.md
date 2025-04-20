# Cognito Sync Cognito Sync Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BulkPublishRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# BulkPublishResponse

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# CognitoStreams

### StreamName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### StreamingStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# Dataset

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


# DeleteDatasetRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetResponse

### Dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.Dataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### Dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.Dataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIdentityPoolUsageRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityPoolUsageResponse

### IdentityPoolUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.IdentityPoolUsage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIdentityUsageRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityUsageResponse

### IdentityUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.IdentityUsage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# GetBulkPublishDetailsRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBulkPublishDetailsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# GetCognitoEventsRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCognitoEventsResponse

### Events
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityPoolConfigurationRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityPoolConfigurationResponse

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.PushSyncOutput'>
- **Required**: Yes

### CognitoStreams
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.CognitoStreams'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityPoolUsage

### IdentityPoolId
- **Type**: typing.Optional[str]

### SyncSessionsCount
- **Type**: typing.Optional[int]

### DataStorage
- **Type**: typing.Optional[int]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# IdentityUsage

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


# ListDatasetsRequest

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


# ListDatasetsResponse

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.Dataset]
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoolUsageRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIdentityPoolUsageResponse

### IdentityPoolUsages
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.IdentityPoolUsage]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecordsRequest

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


# ListRecordsResponse

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.Record]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PushSync

### ApplicationArns
- **Type**: typing.Optional[typing.List[str]]

### RoleArn
- **Type**: typing.Optional[str]


# PushSyncOutput

### ApplicationArns
- **Type**: typing.Optional[typing.List[str]]

### RoleArn
- **Type**: typing.Optional[str]


# Record

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


# RecordPatch

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


# RegisterDeviceRequest

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


# RegisterDeviceResponse

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
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


# SetCognitoEventsRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetIdentityPoolConfigurationRequest

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.PushSync, aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.PushSyncOutput, NoneType]

### CognitoStreams
- **Type**: <class 'NoneType'>


# SetIdentityPoolConfigurationResponse

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PushSync
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.PushSyncOutput'>
- **Required**: Yes

### CognitoStreams
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.CognitoStreams'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


# SubscribeToDatasetRequest

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


# UnsubscribeFromDatasetRequest

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


# UpdateRecordsRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.RecordPatch]]

### ClientContext
- **Type**: typing.Optional[str]


# UpdateRecordsResponse

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.Record]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_classes.ResponseMetadata'>
- **Required**: Yes


