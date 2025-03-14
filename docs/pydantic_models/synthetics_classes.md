# Synthetics Classes

# ArtifactConfigInputTypeDef

### S3Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.S3EncryptionConfigTypeDef]


# ArtifactConfigOutputTypeDef

### S3Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.S3EncryptionConfigTypeDef]


# AssociateResourceRequestTypeDef

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseScreenshotOutputTypeDef

### ScreenshotName
- **Type**: <class 'str'>
- **Required**: Yes

### IgnoreCoordinates
- **Type**: typing.Optional[typing.List[str]]


# BaseScreenshotTypeDef

### ScreenshotName
- **Type**: <class 'str'>
- **Required**: Yes

### IgnoreCoordinates
- **Type**: typing.Optional[typing.Sequence[str]]


# BaseScreenshotUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CanaryCodeInputTypeDef

### Handler
- **Type**: <class 'str'>
- **Required**: Yes

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3Version
- **Type**: typing.Optional[str]

### ZipFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.BlobTypeDef]


# CanaryCodeOutputTypeDef

### SourceLocationArn
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]


# CanaryLastRunTypeDef

### CanaryName
- **Type**: typing.Optional[str]

### LastRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunTypeDef]


# CanaryRunConfigInputTypeDef

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### MemoryInMB
- **Type**: typing.Optional[int]

### ActiveTracing
- **Type**: typing.Optional[bool]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CanaryRunConfigOutputTypeDef

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### MemoryInMB
- **Type**: typing.Optional[int]

### ActiveTracing
- **Type**: typing.Optional[bool]


# CanaryRunStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'PASSED', 'RUNNING']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonCode
- **Type**: typing.Optional[typing.Literal['CANARY_FAILURE', 'EXECUTION_FAILURE']]


# CanaryRunTimelineTypeDef

### Started
- **Type**: typing.Optional[datetime.datetime]

### Completed
- **Type**: typing.Optional[datetime.datetime]


# CanaryRunTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunStatusTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunTimelineTypeDef]

### ArtifactS3Location
- **Type**: typing.Optional[str]


# CanaryScheduleInputTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInSeconds
- **Type**: typing.Optional[int]


# CanaryScheduleOutputTypeDef

### Expression
- **Type**: typing.Optional[str]

### DurationInSeconds
- **Type**: typing.Optional[int]


# CanaryStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'ERROR', 'READY', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonCode
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'INVALID_PERMISSIONS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'SYNC_DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_IN_PROGRESS', 'UPDATE_PENDING']]


# CanaryTimelineTypeDef

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastStarted
- **Type**: typing.Optional[datetime.datetime]

### LastStopped
- **Type**: typing.Optional[datetime.datetime]


# CanaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryCodeOutputTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryScheduleOutputTypeDef]

### RunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunConfigOutputTypeDef]

### SuccessRetentionPeriodInDays
- **Type**: typing.Optional[int]

### FailureRetentionPeriodInDays
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryStatusTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryTimelineTypeDef]

### ArtifactS3Location
- **Type**: typing.Optional[str]

### EngineArn
- **Type**: typing.Optional[str]

### RuntimeVersion
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.VpcConfigOutputTypeDef]

### VisualReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.VisualReferenceOutputTypeDef]

### ProvisionedResourceCleanup
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'OFF']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ArtifactConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.ArtifactConfigOutputTypeDef]


# CreateCanaryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.CanaryCodeInputTypeDef'>
- **Required**: Yes

### ArtifactS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.CanaryScheduleInputTypeDef'>
- **Required**: Yes

### RuntimeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunConfigInputTypeDef]

### SuccessRetentionPeriodInDays
- **Type**: typing.Optional[int]

### FailureRetentionPeriodInDays
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.VpcConfigInputTypeDef]

### ResourcesToReplicateTags
- **Type**: typing.Optional[typing.Sequence[typing.Literal['lambda-function']]]

### ProvisionedResourceCleanup
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'OFF']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ArtifactConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.ArtifactConfigInputTypeDef]


# CreateCanaryResponseTypeDef

### Canary
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.CanaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCanaryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteLambda
- **Type**: typing.Optional[bool]


# DeleteGroupRequestTypeDef

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCanariesLastRunRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeCanariesLastRunResponseTypeDef

### CanariesLastRun
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics_classes.CanaryLastRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeCanariesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeCanariesResponseTypeDef

### Canaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics_classes.CanaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRuntimeVersionsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRuntimeVersionsResponseTypeDef

### RuntimeVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics_classes.RuntimeVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateResourceRequestTypeDef

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCanaryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCanaryResponseTypeDef

### Canary
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.CanaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCanaryRunsRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetCanaryRunsResponseTypeDef

### CanaryRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetGroupRequestTypeDef

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# GroupTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ListAssociatedGroupsRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssociatedGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics_classes.GroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupResourcesRequestTypeDef

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupResourcesResponseTypeDef

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics_classes.GroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics_classes.ResponseMetadataTypeDef'>
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


# RuntimeVersionTypeDef

### VersionName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### DeprecationDate
- **Type**: typing.Optional[datetime.datetime]


# S3EncryptionConfigTypeDef

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# StartCanaryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopCanaryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCanaryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryCodeInputTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### RuntimeVersion
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryScheduleInputTypeDef]

### RunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.CanaryRunConfigInputTypeDef]

### SuccessRetentionPeriodInDays
- **Type**: typing.Optional[int]

### FailureRetentionPeriodInDays
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.VpcConfigInputTypeDef]

### VisualReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.VisualReferenceInputTypeDef]

### ArtifactS3Location
- **Type**: typing.Optional[str]

### ArtifactConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics_classes.ArtifactConfigInputTypeDef]

### ProvisionedResourceCleanup
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'OFF']]


# VisualReferenceInputTypeDef

### BaseCanaryRunId
- **Type**: <class 'str'>
- **Required**: Yes

### BaseScreenshots
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.synthetics_classes.BaseScreenshotUnionTypeDef]]


# VisualReferenceOutputTypeDef

### BaseScreenshots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.synthetics_classes.BaseScreenshotOutputTypeDef]]

### BaseCanaryRunId
- **Type**: typing.Optional[str]


# VpcConfigInputTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


# VpcConfigOutputTypeDef

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


