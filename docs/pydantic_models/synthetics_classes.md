# Synthetics Classes

# ArtifactConfigInput

### S3Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.S3EncryptionConfig]


# ArtifactConfigOutput

### S3Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.S3EncryptionConfig]


# AssociateResourceRequest

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseScreenshot

### ScreenshotName
- **Type**: <class 'str'>
- **Required**: Yes

### IgnoreCoordinates
- **Type**: typing.Optional[typing.List[str]]


# BaseScreenshotOutput

### ScreenshotName
- **Type**: <class 'str'>
- **Required**: Yes

### IgnoreCoordinates
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Canary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryCodeOutput]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryScheduleOutput]

### RunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRunConfigOutput]

### SuccessRetentionPeriodInDays
- **Type**: typing.Optional[int]

### FailureRetentionPeriodInDays
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryStatus]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryTimeline]

### ArtifactS3Location
- **Type**: typing.Optional[str]

### EngineArn
- **Type**: typing.Optional[str]

### RuntimeVersion
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.VpcConfigOutput]

### VisualReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.VisualReferenceOutput]

### ProvisionedResourceCleanup
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'OFF']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ArtifactConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ArtifactConfigOutput]


# CanaryCodeInput

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# CanaryCodeOutput

### SourceLocationArn
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]


# CanaryLastRun

### CanaryName
- **Type**: typing.Optional[str]

### LastRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRun]


# CanaryRun

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRunStatus]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRunTimeline]

### ArtifactS3Location
- **Type**: typing.Optional[str]


# CanaryRunConfigInput

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### MemoryInMB
- **Type**: typing.Optional[int]

### ActiveTracing
- **Type**: typing.Optional[bool]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# CanaryRunConfigOutput

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### MemoryInMB
- **Type**: typing.Optional[int]

### ActiveTracing
- **Type**: typing.Optional[bool]


# CanaryRunStatus

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'PASSED', 'RUNNING']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonCode
- **Type**: typing.Optional[typing.Literal['CANARY_FAILURE', 'EXECUTION_FAILURE']]


# CanaryRunTimeline

### Started
- **Type**: typing.Optional[datetime.datetime]

### Completed
- **Type**: typing.Optional[datetime.datetime]


# CanaryScheduleInput

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInSeconds
- **Type**: typing.Optional[int]


# CanaryScheduleOutput

### Expression
- **Type**: typing.Optional[str]

### DurationInSeconds
- **Type**: typing.Optional[int]


# CanaryStatus

### State
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'ERROR', 'READY', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonCode
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'INVALID_PERMISSIONS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'SYNC_DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_IN_PROGRESS', 'UPDATE_PENDING']]


# CanaryTimeline

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastStarted
- **Type**: typing.Optional[datetime.datetime]

### LastStopped
- **Type**: typing.Optional[datetime.datetime]


# CreateCanaryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryCodeInput'>
- **Required**: Yes

### ArtifactS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryScheduleInput'>
- **Required**: Yes

### RuntimeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRunConfigInput]

### SuccessRetentionPeriodInDays
- **Type**: typing.Optional[int]

### FailureRetentionPeriodInDays
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.VpcConfigInput]

### ResourcesToReplicateTags
- **Type**: typing.Optional[typing.List[typing.Literal['lambda-function']]]

### ProvisionedResourceCleanup
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'OFF']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ArtifactConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ArtifactConfigInput]


# CreateCanaryResponse

### Canary
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.Canary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCanaryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteLambda
- **Type**: typing.Optional[bool]


# DeleteGroupRequest

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCanariesLastRunRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Names
- **Type**: typing.Optional[typing.List[str]]


# DescribeCanariesLastRunResponse

### CanariesLastRun
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryLastRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeCanariesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Names
- **Type**: typing.Optional[typing.List[str]]


# DescribeCanariesResponse

### Canaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.Canary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRuntimeVersionsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRuntimeVersionsResponse

### RuntimeVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.RuntimeVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateResourceRequest

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCanaryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCanaryResponse

### Canary
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.Canary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes


# GetCanaryRunsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetCanaryRunsResponse

### CanaryRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetGroupRequest

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes


# Group

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


# GroupSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# ListAssociatedGroupsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssociatedGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.GroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupResourcesRequest

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupResourcesResponse

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.GroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ResponseMetadata'>
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


# RuntimeVersion

### VersionName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### DeprecationDate
- **Type**: typing.Optional[datetime.datetime]


# S3EncryptionConfig

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# StartCanaryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopCanaryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCanaryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryCodeInput]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### RuntimeVersion
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryScheduleInput]

### RunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.CanaryRunConfigInput]

### SuccessRetentionPeriodInDays
- **Type**: typing.Optional[int]

### FailureRetentionPeriodInDays
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.VpcConfigInput]

### VisualReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.VisualReferenceInput]

### ArtifactS3Location
- **Type**: typing.Optional[str]

### ArtifactConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.ArtifactConfigInput]

### ProvisionedResourceCleanup
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'OFF']]


# VisualReferenceInput

### BaseCanaryRunId
- **Type**: <class 'str'>
- **Required**: Yes

### BaseScreenshots
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.BaseScreenshot, aws_resource_validator.pydantic_models.synthetics.synthetics_classes.BaseScreenshotOutput]]]


# VisualReferenceOutput

### BaseScreenshots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.synthetics.synthetics_classes.BaseScreenshotOutput]]

### BaseCanaryRunId
- **Type**: typing.Optional[str]


# VpcConfigInput

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


# VpcConfigOutput

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


