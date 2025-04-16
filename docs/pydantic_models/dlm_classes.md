# Dlm Classes

# Action

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CrossRegionCopy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyAction]
- **Required**: Yes


# ActionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CrossRegionCopy
- **Type**: typing.List[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyAction]
- **Required**: Yes


# ArchiveRetainRule

### RetentionArchiveTier
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.RetentionArchiveTier'>
- **Required**: Yes


# ArchiveRule

### RetainRule
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ArchiveRetainRule'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLifecyclePolicyRequest

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### PolicyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.PolicyDetailsUnion]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DefaultPolicy
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'VOLUME']]

### CreateInterval
- **Type**: typing.Optional[int]

### RetainInterval
- **Type**: typing.Optional[int]

### CopyTags
- **Type**: typing.Optional[bool]

### ExtendDeletion
- **Type**: typing.Optional[bool]

### CrossRegionCopyTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTarget]]

### Exclusions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ExclusionsUnion]


# CreateLifecyclePolicyResponse

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRule

### Location
- **Type**: typing.Optional[typing.Literal['CLOUD', 'LOCAL_ZONE', 'OUTPOST_LOCAL']]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['HOURS']]

### Times
- **Type**: typing.Optional[typing.Sequence[str]]

### CronExpression
- **Type**: typing.Optional[str]

### Scripts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Script]]


# CreateRuleOutput

### Location
- **Type**: typing.Optional[typing.Literal['CLOUD', 'LOCAL_ZONE', 'OUTPOST_LOCAL']]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['HOURS']]

### Times
- **Type**: typing.Optional[typing.List[str]]

### CronExpression
- **Type**: typing.Optional[str]

### Scripts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.ScriptOutput]]


# CrossRegionCopyAction

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.EncryptionConfiguration'>
- **Required**: Yes

### RetainRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRetainRule]


# CrossRegionCopyDeprecateRule

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# CrossRegionCopyRetainRule

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# CrossRegionCopyRule

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### TargetRegion
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### CmkArn
- **Type**: typing.Optional[str]

### CopyTags
- **Type**: typing.Optional[bool]

### RetainRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRetainRule]

### DeprecateRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyDeprecateRule]


# CrossRegionCopyTarget

### TargetRegion
- **Type**: typing.Optional[str]


# DeleteLifecyclePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecateRule

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# EncryptionConfiguration

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### CmkArn
- **Type**: typing.Optional[str]


# EventParameters

### EventType
- **Type**: typing.Literal['shareSnapshot']
- **Required**: Yes

### SnapshotOwner
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DescriptionRegex
- **Type**: <class 'str'>
- **Required**: Yes


# EventParametersOutput

### EventType
- **Type**: typing.Literal['shareSnapshot']
- **Required**: Yes

### SnapshotOwner
- **Type**: typing.List[str]
- **Required**: Yes

### DescriptionRegex
- **Type**: <class 'str'>
- **Required**: Yes


# EventSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventSourceOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Exclusions

### ExcludeBootVolumes
- **Type**: typing.Optional[bool]

### ExcludeVolumeTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Tag]]


# ExclusionsOutput

### ExcludeBootVolumes
- **Type**: typing.Optional[bool]

### ExcludeVolumeTypes
- **Type**: typing.Optional[typing.List[str]]

### ExcludeTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.Tag]]


# ExclusionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FastRestoreRule

### AvailabilityZones
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# FastRestoreRuleOutput

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# GetLifecyclePoliciesRequest

### PolicyIds
- **Type**: typing.Optional[typing.Sequence[str]]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ERROR']]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['INSTANCE', 'VOLUME']]]

### TargetTags
- **Type**: typing.Optional[typing.Sequence[str]]

### TagsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultPolicyType
- **Type**: typing.Optional[typing.Literal['ALL', 'INSTANCE', 'VOLUME']]


# GetLifecyclePoliciesResponse

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.dlm_classes.LifecyclePolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadata'>
- **Required**: Yes


# GetLifecyclePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecyclePolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.LifecyclePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadata'>
- **Required**: Yes


# LifecyclePolicy

### PolicyId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ERROR']]

### StatusMessage
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]

### PolicyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.PolicyDetailsOutput]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PolicyArn
- **Type**: typing.Optional[str]

### DefaultPolicy
- **Type**: typing.Optional[bool]


# LifecyclePolicySummary

### PolicyId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ERROR']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PolicyType
- **Type**: typing.Optional[typing.Literal['EBS_SNAPSHOT_MANAGEMENT', 'EVENT_BASED_POLICY', 'IMAGE_MANAGEMENT']]

### DefaultPolicy
- **Type**: typing.Optional[bool]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadata'>
- **Required**: Yes


# Parameters

### ExcludeBootVolume
- **Type**: typing.Optional[bool]

### NoReboot
- **Type**: typing.Optional[bool]

### ExcludeDataVolumeTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Tag]]


# ParametersOutput

### ExcludeBootVolume
- **Type**: typing.Optional[bool]

### NoReboot
- **Type**: typing.Optional[bool]

### ExcludeDataVolumeTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.Tag]]


# PolicyDetails

### PolicyType
- **Type**: typing.Optional[typing.Literal['EBS_SNAPSHOT_MANAGEMENT', 'EVENT_BASED_POLICY', 'IMAGE_MANAGEMENT']]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['INSTANCE', 'VOLUME']]]

### ResourceLocations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOUD', 'LOCAL_ZONE', 'OUTPOST']]]

### TargetTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Tag]]

### Schedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Schedule]]

### Parameters
- **Type**: <class 'NoneType'>

### EventSource
- **Type**: <class 'NoneType'>

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Action]]

### PolicyLanguage
- **Type**: typing.Optional[typing.Literal['SIMPLIFIED', 'STANDARD']]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'VOLUME']]

### CreateInterval
- **Type**: typing.Optional[int]

### RetainInterval
- **Type**: typing.Optional[int]

### CopyTags
- **Type**: typing.Optional[bool]

### CrossRegionCopyTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTarget]]

### ExtendDeletion
- **Type**: typing.Optional[bool]

### Exclusions
- **Type**: <class 'NoneType'>


# PolicyDetailsOutput

### PolicyType
- **Type**: typing.Optional[typing.Literal['EBS_SNAPSHOT_MANAGEMENT', 'EVENT_BASED_POLICY', 'IMAGE_MANAGEMENT']]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['INSTANCE', 'VOLUME']]]

### ResourceLocations
- **Type**: typing.Optional[typing.List[typing.Literal['CLOUD', 'LOCAL_ZONE', 'OUTPOST']]]

### TargetTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.Tag]]

### Schedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.ScheduleOutput]]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ParametersOutput]

### EventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.EventSourceOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.ActionOutput]]

### PolicyLanguage
- **Type**: typing.Optional[typing.Literal['SIMPLIFIED', 'STANDARD']]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'VOLUME']]

### CreateInterval
- **Type**: typing.Optional[int]

### RetainInterval
- **Type**: typing.Optional[int]

### CopyTags
- **Type**: typing.Optional[bool]

### CrossRegionCopyTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTarget]]

### ExtendDeletion
- **Type**: typing.Optional[bool]

### Exclusions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ExclusionsOutput]


# PolicyDetailsUnion

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


# RetainRule

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# RetentionArchiveTier

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# Schedule

### Name
- **Type**: typing.Optional[str]

### CopyTags
- **Type**: typing.Optional[bool]

### TagsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Tag]]

### VariableTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.Tag]]

### CreateRule
- **Type**: <class 'NoneType'>

### RetainRule
- **Type**: <class 'NoneType'>

### FastRestoreRule
- **Type**: <class 'NoneType'>

### CrossRegionCopyRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRule]]

### ShareRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.ShareRule]]

### DeprecateRule
- **Type**: <class 'NoneType'>

### ArchiveRule
- **Type**: <class 'NoneType'>


# ScheduleOutput

### Name
- **Type**: typing.Optional[str]

### CopyTags
- **Type**: typing.Optional[bool]

### TagsToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.Tag]]

### VariableTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.Tag]]

### CreateRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CreateRuleOutput]

### RetainRule
- **Type**: <class 'NoneType'>

### FastRestoreRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.FastRestoreRuleOutput]

### CrossRegionCopyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRule]]

### ShareRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dlm_classes.ShareRuleOutput]]

### DeprecateRule
- **Type**: <class 'NoneType'>

### ArchiveRule
- **Type**: <class 'NoneType'>


# Script

### ExecutionHandler
- **Type**: <class 'str'>
- **Required**: Yes

### Stages
- **Type**: typing.Optional[typing.Sequence[typing.Literal['POST', 'PRE']]]

### ExecutionHandlerService
- **Type**: typing.Optional[typing.Literal['AWS_SYSTEMS_MANAGER']]

### ExecuteOperationOnScriptFailure
- **Type**: typing.Optional[bool]

### ExecutionTimeout
- **Type**: typing.Optional[int]

### MaximumRetryCount
- **Type**: typing.Optional[int]


# ScriptOutput

### ExecutionHandler
- **Type**: <class 'str'>
- **Required**: Yes

### Stages
- **Type**: typing.Optional[typing.List[typing.Literal['POST', 'PRE']]]

### ExecutionHandlerService
- **Type**: typing.Optional[typing.Literal['AWS_SYSTEMS_MANAGER']]

### ExecuteOperationOnScriptFailure
- **Type**: typing.Optional[bool]

### ExecutionTimeout
- **Type**: typing.Optional[int]

### MaximumRetryCount
- **Type**: typing.Optional[int]


# ShareRule

### TargetAccounts
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UnshareInterval
- **Type**: typing.Optional[int]

### UnshareIntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# ShareRuleOutput

### TargetAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### UnshareInterval
- **Type**: typing.Optional[int]

### UnshareIntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLifecyclePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Description
- **Type**: typing.Optional[str]

### PolicyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.PolicyDetailsUnion]

### CreateInterval
- **Type**: typing.Optional[int]

### RetainInterval
- **Type**: typing.Optional[int]

### CopyTags
- **Type**: typing.Optional[bool]

### ExtendDeletion
- **Type**: typing.Optional[bool]

### CrossRegionCopyTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTarget]]

### Exclusions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ExclusionsUnion]


