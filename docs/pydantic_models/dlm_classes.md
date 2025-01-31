# Dlm Classes

# ActionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CrossRegionCopy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyActionTypeDef]
- **Required**: Yes


# ArchiveRetainRuleTypeDef

### RetentionArchiveTier
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.RetentionArchiveTierTypeDef'>
- **Required**: Yes


# ArchiveRuleTypeDef

### RetainRule
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ArchiveRetainRuleTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLifecyclePolicyRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.PolicyDetailsTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTargetTypeDef]]

### Exclusions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ExclusionsTypeDef]


# CreateLifecyclePolicyResponseTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleTypeDef

### Location
- **Type**: typing.Optional[typing.Literal['CLOUD', 'OUTPOST_LOCAL']]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['HOURS']]

### Times
- **Type**: typing.Optional[typing.Sequence[str]]

### CronExpression
- **Type**: typing.Optional[str]

### Scripts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.ScriptTypeDef]]


# CrossRegionCopyActionTypeDef

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### RetainRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRetainRuleTypeDef]


# CrossRegionCopyDeprecateRuleTypeDef

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# CrossRegionCopyRetainRuleTypeDef

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# CrossRegionCopyRuleTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRetainRuleTypeDef]

### DeprecateRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyDeprecateRuleTypeDef]


# CrossRegionCopyTargetTypeDef

### TargetRegion
- **Type**: typing.Optional[str]


# DeleteLifecyclePolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecateRuleTypeDef

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# EncryptionConfigurationTypeDef

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### CmkArn
- **Type**: typing.Optional[str]


# EventParametersTypeDef

### EventType
- **Type**: typing.Literal['shareSnapshot']
- **Required**: Yes

### SnapshotOwner
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DescriptionRegex
- **Type**: <class 'str'>
- **Required**: Yes


# EventSourceTypeDef

### Type
- **Type**: typing.Literal['MANAGED_CWE']
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.EventParametersTypeDef]


# ExclusionsTypeDef

### ExcludeBootVolumes
- **Type**: typing.Optional[bool]

### ExcludeVolumeTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.TagTypeDef]]


# FastRestoreRuleTypeDef

### AvailabilityZones
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# GetLifecyclePoliciesRequestRequestTypeDef

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


# GetLifecyclePoliciesResponseTypeDef

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.dlm_classes.LifecyclePolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecyclePolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecyclePolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.LifecyclePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LifecyclePolicySummaryTypeDef

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


# LifecyclePolicyTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.PolicyDetailsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PolicyArn
- **Type**: typing.Optional[str]

### DefaultPolicy
- **Type**: typing.Optional[bool]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dlm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ParametersTypeDef

### ExcludeBootVolume
- **Type**: typing.Optional[bool]

### NoReboot
- **Type**: typing.Optional[bool]

### ExcludeDataVolumeTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.TagTypeDef]]


# PolicyDetailsTypeDef

### PolicyType
- **Type**: typing.Optional[typing.Literal['EBS_SNAPSHOT_MANAGEMENT', 'EVENT_BASED_POLICY', 'IMAGE_MANAGEMENT']]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['INSTANCE', 'VOLUME']]]

### ResourceLocations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOUD', 'OUTPOST']]]

### TargetTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.TagTypeDef]]

### Schedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.ScheduleTypeDef]]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ParametersTypeDef]

### EventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.EventSourceTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.ActionTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTargetTypeDef]]

### ExtendDeletion
- **Type**: typing.Optional[bool]

### Exclusions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ExclusionsTypeDef]


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


# RetainRuleTypeDef

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# RetentionArchiveTierTypeDef

### Count
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### IntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# ScheduleTypeDef

### Name
- **Type**: typing.Optional[str]

### CopyTags
- **Type**: typing.Optional[bool]

### TagsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.TagTypeDef]]

### VariableTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.TagTypeDef]]

### CreateRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.CreateRuleTypeDef]

### RetainRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.RetainRuleTypeDef]

### FastRestoreRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.FastRestoreRuleTypeDef]

### CrossRegionCopyRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyRuleTypeDef]]

### ShareRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.ShareRuleTypeDef]]

### DeprecateRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.DeprecateRuleTypeDef]

### ArchiveRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ArchiveRuleTypeDef]


# ScriptTypeDef

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


# ShareRuleTypeDef

### TargetAccounts
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UnshareInterval
- **Type**: typing.Optional[int]

### UnshareIntervalUnit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLifecyclePolicyRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.PolicyDetailsTypeDef]

### CreateInterval
- **Type**: typing.Optional[int]

### RetainInterval
- **Type**: typing.Optional[int]

### CopyTags
- **Type**: typing.Optional[bool]

### ExtendDeletion
- **Type**: typing.Optional[bool]

### CrossRegionCopyTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dlm_classes.CrossRegionCopyTargetTypeDef]]

### Exclusions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dlm_classes.ExclusionsTypeDef]


