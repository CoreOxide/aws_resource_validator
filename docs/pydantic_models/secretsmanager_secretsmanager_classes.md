# Secretsmanager Secretsmanager Classes

# APIErrorType

### SecretId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetSecretValueRequest

### SecretIdList
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# BatchGetSecretValueResponse

### SecretValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.SecretValueEntry]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.APIErrorType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CancelRotateSecretRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelRotateSecretResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecretRequest

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### SecretString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Tag]]

### AddReplicaRegions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ReplicaRegionType]]

### ForceOverwriteReplicaSecret
- **Type**: typing.Optional[bool]


# CreateSecretResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ReplicationStatusType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSecretRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryWindowInDays
- **Type**: typing.Optional[int]

### ForceDeleteWithoutRecovery
- **Type**: typing.Optional[bool]


# DeleteSecretResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSecretRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecretResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.RotationRulesType'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Tag]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ReplicationStatusType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Key
- **Type**: typing.Optional[typing.Literal['all', 'description', 'name', 'owning-service', 'primary-region', 'tag-key', 'tag-value']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# GetRandomPasswordRequest

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


# GetRandomPasswordResponse

### RandomPassword
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecretValueRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]

### VersionStage
- **Type**: typing.Optional[str]


# GetSecretValueResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ListSecretVersionIdsRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeDeprecated
- **Type**: typing.Optional[bool]


# ListSecretVersionIdsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.SecretVersionsListEntry]
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecretsRequest

### IncludePlannedDeletion
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Filter]]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'desc']]


# ListSecretsRequestPaginate

### IncludePlannedDeletion
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Filter]]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'desc']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.PaginatorConfig]


# ListSecretsResponse

### SecretList
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.SecretListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### BlockPublicPolicy
- **Type**: typing.Optional[bool]


# PutResourcePolicyResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# PutSecretValueRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SecretBinary
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### SecretString
- **Type**: typing.Optional[str]

### VersionStages
- **Type**: typing.Optional[typing.List[str]]

### RotationToken
- **Type**: typing.Optional[str]


# PutSecretValueResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveRegionsFromReplicationRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoveReplicaRegions
- **Type**: typing.List[str]
- **Required**: Yes


# RemoveRegionsFromReplicationResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ReplicationStatusType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ReplicaRegionType

### Region
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# ReplicateSecretToRegionsRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### AddReplicaRegions
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ReplicaRegionType]
- **Required**: Yes

### ForceOverwriteReplicaSecret
- **Type**: typing.Optional[bool]


# ReplicateSecretToRegionsResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ReplicationStatusType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ReplicationStatusType

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


# RestoreSecretRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreSecretResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# RotateSecretRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### RotationLambdaARN
- **Type**: typing.Optional[str]

### RotationRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.RotationRulesType]

### RotateImmediately
- **Type**: typing.Optional[bool]


# RotateSecretResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# RotationRulesType

### AutomaticallyAfterDays
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[str]

### ScheduleExpression
- **Type**: typing.Optional[str]


# SecretListEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.RotationRulesType]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Tag]]

### SecretVersionsToStages
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### OwningService
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### PrimaryRegion
- **Type**: typing.Optional[str]


# SecretValueEntry

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


# SecretVersionsListEntry

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


# StopReplicationToReplicaRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationToReplicaResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateSecretRequest

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### SecretString
- **Type**: typing.Optional[str]


# UpdateSecretResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecretVersionStageRequest

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


# UpdateSecretVersionStageResponse

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateResourcePolicyRequest

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### SecretId
- **Type**: typing.Optional[str]


# ValidateResourcePolicyResponse

### PolicyValidationPassed
- **Type**: <class 'bool'>
- **Required**: Yes

### ValidationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ValidationErrorsEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ValidationErrorsEntry

### CheckName
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


