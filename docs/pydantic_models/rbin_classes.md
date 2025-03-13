# Rbin Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateRuleRequestTypeDef

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.TagTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]

### LockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rbin_classes.LockConfigurationTypeDef]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]


# CreateRuleResponseTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.TagTypeDef]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.LockConfigurationTypeDef'>
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRuleRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleResponseTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.LockConfigurationTypeDef'>
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### LockEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRulesRequestPaginateTypeDef

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]

### LockState
- **Type**: typing.Optional[typing.Literal['locked', 'pending_unlock', 'unlocked']]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rbin_classes.PaginatorConfigTypeDef]


# ListRulesRequestTypeDef

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]

### LockState
- **Type**: typing.Optional[typing.Literal['locked', 'pending_unlock', 'unlocked']]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]


# ListRulesResponseTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.RuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LockConfigurationTypeDef

### UnlockDelay
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.UnlockDelayTypeDef'>
- **Required**: Yes


# LockRuleRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.LockConfigurationTypeDef'>
- **Required**: Yes


# LockRuleResponseTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.LockConfigurationTypeDef'>
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTagTypeDef

### ResourceTagKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagValue
- **Type**: typing.Optional[str]


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


# RetentionPeriodTypeDef

### RetentionPeriodValue
- **Type**: <class 'int'>
- **Required**: Yes

### RetentionPeriodUnit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes


# RuleSummaryTypeDef

### Identifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef]

### LockState
- **Type**: typing.Optional[typing.Literal['locked', 'pending_unlock', 'unlocked']]

### RuleArn
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UnlockDelayTypeDef

### UnlockDelayValue
- **Type**: <class 'int'>
- **Required**: Yes

### UnlockDelayUnit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes


# UnlockRuleRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# UnlockRuleResponseTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.LockConfigurationTypeDef'>
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### LockEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRuleRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef]

### Description
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]]


# UpdateRuleResponseTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### LockEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


