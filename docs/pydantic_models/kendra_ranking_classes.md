# Kendra Ranking Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityUnitsConfigurationTypeDef

### RescoreCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes


# CreateRescoreExecutionPlanRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_ranking_classes.CapacityUnitsConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_ranking_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateRescoreExecutionPlanResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRescoreExecutionPlanRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRescoreExecutionPlanRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRescoreExecutionPlanResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityUnits
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.CapacityUnitsConfigurationTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalScore
- **Type**: <class 'float'>
- **Required**: Yes

### GroupId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Body
- **Type**: typing.Optional[str]

### TokenizedTitle
- **Type**: typing.Optional[typing.Sequence[str]]

### TokenizedBody
- **Type**: typing.Optional[typing.Sequence[str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRescoreExecutionPlansRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRescoreExecutionPlansResponseTypeDef

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking_classes.RescoreExecutionPlanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RescoreExecutionPlanSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# RescoreRequestTypeDef

### RescoreExecutionPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchQuery
- **Type**: <class 'str'>
- **Required**: Yes

### Documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_ranking_classes.DocumentTypeDef]
- **Required**: Yes


# RescoreResultItemTypeDef

### DocumentId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# RescoreResultTypeDef

### RescoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking_classes.RescoreResultItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking_classes.ResponseMetadataTypeDef'>
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


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_ranking_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRescoreExecutionPlanRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_ranking_classes.CapacityUnitsConfigurationTypeDef]


