# Kendra Ranking Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityUnitsConfiguration

### RescoreCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes


# CreateRescoreExecutionPlanRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.CapacityUnitsConfiguration]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateRescoreExecutionPlanResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRescoreExecutionPlanRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRescoreExecutionPlanRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRescoreExecutionPlanResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.CapacityUnitsConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.ResponseMetadata'>
- **Required**: Yes


# Document

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
- **Type**: typing.Optional[typing.List[str]]

### TokenizedBody
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.ResponseMetadata'>
- **Required**: Yes


# ListRescoreExecutionPlansRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRescoreExecutionPlansResponse

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.RescoreExecutionPlanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.ResponseMetadata'>
- **Required**: Yes


# RescoreExecutionPlanSummary

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


# RescoreRequest

### RescoreExecutionPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchQuery
- **Type**: <class 'str'>
- **Required**: Yes

### Documents
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.Document]
- **Required**: Yes


# RescoreResult

### RescoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.RescoreResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.ResponseMetadata'>
- **Required**: Yes


# RescoreResultItem

### DocumentId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


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


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateRescoreExecutionPlanRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_classes.CapacityUnitsConfiguration]


