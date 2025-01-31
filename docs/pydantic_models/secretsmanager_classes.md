# Secretsmanager Classes

# APIErrorTypeTypeDef

### SecretId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetSecretValueRequestRequestTypeDef

### SecretIdList
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# BatchGetSecretValueResponseTypeDef

### SecretValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.SecretValueEntryTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.APIErrorTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CancelRotateSecretRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelRotateSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecretRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### SecretBinary
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### SecretString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.TagTypeDef]]

### AddReplicaRegions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.ReplicaRegionTypeTypeDef]]

### ForceOverwriteReplicaSecret
- **Type**: typing.Optional[bool]


# CreateSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.ReplicationStatusTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSecretRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryWindowInDays
- **Type**: typing.Optional[int]

### ForceDeleteWithoutRecovery
- **Type**: typing.Optional[bool]


# DeleteSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSecretRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RotationLambdaARN
- **Type**: <class 'str'>
- **Required**: Yes

### RotationRules
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.RotationRulesTypeTypeDef'>
- **Required**: Yes

### LastRotatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastChangedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAccessedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeletedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextRotationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.TagTypeDef]
- **Required**: Yes

### VersionIdsToStages
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### OwningService
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.ReplicationStatusTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Key
- **Type**: typing.Optional[typing.Literal['all', 'description', 'name', 'owning-service', 'primary-region', 'tag-key', 'tag-value']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetRandomPasswordRequestRequestTypeDef

### PasswordLength
- **Type**: typing.Optional[int]

### ExcludeCharacters
- **Type**: typing.Optional[str]

### ExcludeNumbers
- **Type**: typing.Optional[bool]

### ExcludePunctuation
- **Type**: typing.Optional[bool]

### ExcludeUppercase
- **Type**: typing.Optional[bool]

### ExcludeLowercase
- **Type**: typing.Optional[bool]

### IncludeSpace
- **Type**: typing.Optional[bool]

### RequireEachIncludedType
- **Type**: typing.Optional[bool]


# GetRandomPasswordResponseTypeDef

### RandomPassword
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecretValueRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]

### VersionStage
- **Type**: typing.Optional[str]


# GetSecretValueResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretBinary
- **Type**: <class 'bytes'>
- **Required**: Yes

### SecretString
- **Type**: <class 'str'>
- **Required**: Yes

### VersionStages
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSecretVersionIdsRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeDeprecated
- **Type**: typing.Optional[bool]


# ListSecretVersionIdsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.SecretVersionsListEntryTypeDef]
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecretsRequestListSecretsPaginateTypeDef

### IncludePlannedDeletion
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.FilterTypeDef]]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'desc']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.secretsmanager_classes.PaginatorConfigTypeDef]


# ListSecretsRequestRequestTypeDef

### IncludePlannedDeletion
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.FilterTypeDef]]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'desc']]


# ListSecretsResponseTypeDef

### SecretList
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.SecretListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### BlockPublicPolicy
- **Type**: typing.Optional[bool]


# PutResourcePolicyResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSecretValueRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SecretBinary
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### SecretString
- **Type**: typing.Optional[str]

### VersionStages
- **Type**: typing.Optional[typing.Sequence[str]]

### RotationToken
- **Type**: typing.Optional[str]


# PutSecretValueResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionStages
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveRegionsFromReplicationRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoveReplicaRegions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveRegionsFromReplicationResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.ReplicationStatusTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicaRegionTypeTypeDef

### Region
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# ReplicateSecretToRegionsRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### AddReplicaRegions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.ReplicaRegionTypeTypeDef]
- **Required**: Yes

### ForceOverwriteReplicaSecret
- **Type**: typing.Optional[bool]


# ReplicateSecretToRegionsResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.ReplicationStatusTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicationStatusTypeTypeDef

### Region
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'InSync']]

### StatusMessage
- **Type**: typing.Optional[str]

### LastAccessedDate
- **Type**: typing.Optional[datetime.datetime]


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


# RestoreSecretRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RotateSecretRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### RotationLambdaARN
- **Type**: typing.Optional[str]

### RotationRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.secretsmanager_classes.RotationRulesTypeTypeDef]

### RotateImmediately
- **Type**: typing.Optional[bool]


# RotateSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RotationRulesTypeTypeDef

### AutomaticallyAfterDays
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[str]

### ScheduleExpression
- **Type**: typing.Optional[str]


# SecretListEntryTypeDef

### ARN
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### RotationEnabled
- **Type**: typing.Optional[bool]

### RotationLambdaARN
- **Type**: typing.Optional[str]

### RotationRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.secretsmanager_classes.RotationRulesTypeTypeDef]

### LastRotatedDate
- **Type**: typing.Optional[datetime.datetime]

### LastChangedDate
- **Type**: typing.Optional[datetime.datetime]

### LastAccessedDate
- **Type**: typing.Optional[datetime.datetime]

### DeletedDate
- **Type**: typing.Optional[datetime.datetime]

### NextRotationDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.TagTypeDef]]

### SecretVersionsToStages
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### OwningService
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### PrimaryRegion
- **Type**: typing.Optional[str]


# SecretValueEntryTypeDef

### ARN
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### SecretBinary
- **Type**: typing.Optional[bytes]

### SecretString
- **Type**: typing.Optional[str]

### VersionStages
- **Type**: typing.Optional[typing.List[str]]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]


# SecretVersionsListEntryTypeDef

### VersionId
- **Type**: typing.Optional[str]

### VersionStages
- **Type**: typing.Optional[typing.List[str]]

### LastAccessedDate
- **Type**: typing.Optional[datetime.datetime]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### KmsKeyIds
- **Type**: typing.Optional[typing.List[str]]


# StopReplicationToReplicaRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationToReplicaResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.secretsmanager_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSecretRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### SecretBinary
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### SecretString
- **Type**: typing.Optional[str]


# UpdateSecretResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecretVersionStageRequestRequestTypeDef

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionStage
- **Type**: <class 'str'>
- **Required**: Yes

### RemoveFromVersionId
- **Type**: typing.Optional[str]

### MoveToVersionId
- **Type**: typing.Optional[str]


# UpdateSecretVersionStageResponseTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateResourcePolicyRequestRequestTypeDef

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### SecretId
- **Type**: typing.Optional[str]


# ValidateResourcePolicyResponseTypeDef

### PolicyValidationPassed
- **Type**: <class 'bool'>
- **Required**: Yes

### ValidationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager_classes.ValidationErrorsEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidationErrorsEntryTypeDef

### CheckName
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


