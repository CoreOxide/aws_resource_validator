# Rbin Rbin Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateRuleRequest

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.RetentionPeriod'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.Tag]]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]

### LockConfiguration
- **Type**: <class 'NoneType'>

### ExcludeResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]


# CreateRuleResponse

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.RetentionPeriod'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.Tag]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.LockConfiguration'>
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRuleRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.RetentionPeriod'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.LockConfiguration'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes


# ListRulesRequest

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]

### LockState
- **Type**: typing.Optional[typing.Literal['locked', 'pending_unlock', 'unlocked']]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]


# ListRulesRequestPaginate

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]

### LockState
- **Type**: typing.Optional[typing.Literal['locked', 'pending_unlock', 'unlocked']]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rbin.rbin_classes.PaginatorConfig]


# ListRulesResponse

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes


# LockConfiguration

### UnlockDelay
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.UnlockDelay'>
- **Required**: Yes


# LockRuleRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.LockConfiguration'>
- **Required**: Yes


# LockRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.RetentionPeriod'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.LockConfiguration'>
- **Required**: Yes

### LockState
- **Type**: typing.Literal['locked', 'pending_unlock', 'unlocked']
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTag

### ResourceTagKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagValue
- **Type**: typing.Optional[str]


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


# RetentionPeriod

### RetentionPeriodValue
- **Type**: <class 'int'>
- **Required**: Yes

### RetentionPeriodUnit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes


# RuleSummary

### Identifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RetentionPeriod
- **Type**: <class 'NoneType'>

### LockState
- **Type**: typing.Optional[typing.Literal['locked', 'pending_unlock', 'unlocked']]

### RuleArn
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.Tag]
- **Required**: Yes


# UnlockDelay

### UnlockDelayValue
- **Type**: <class 'int'>
- **Required**: Yes

### UnlockDelayUnit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes


# UnlockRuleRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# UnlockRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.RetentionPeriod'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['available', 'pending']
- **Required**: Yes

### LockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.LockConfiguration'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateRuleRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]

### ExcludeResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]]


# UpdateRuleResponse

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.RetentionPeriod'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['EBS_SNAPSHOT', 'EC2_IMAGE']
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rbin.rbin_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rbin.rbin_classes.ResponseMetadata'>
- **Required**: Yes


