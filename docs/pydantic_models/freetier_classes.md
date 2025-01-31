# Freetier Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DimensionValuesTypeDef

### Key
- **Type**: typing.Literal['DESCRIPTION', 'FREE_TIER_TYPE', 'OPERATION', 'REGION', 'SERVICE', 'USAGE_PERCENTAGE', 'USAGE_TYPE']
- **Required**: Yes

### MatchOptions
- **Type**: typing.Sequence[typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ExpressionTypeDef

### And
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier_classes.DimensionValuesTypeDef]

### Not
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Or
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]


# FreeTierUsageTypeDef

### actualUsageAmount
- **Type**: typing.Optional[float]

### description
- **Type**: typing.Optional[str]

### forecastedUsageAmount
- **Type**: typing.Optional[float]

### freeTierType
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[float]

### operation
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[str]


# GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier_classes.ExpressionTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier_classes.PaginatorConfigTypeDef]


# GetFreeTierUsageRequestRequestTypeDef

### filter
- **Type**: typing.Optional[ForwardRef('ExpressionTypeDef')]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFreeTierUsageResponseTypeDef

### freeTierUsages
- **Type**: typing.List[aws_resource_validator.pydantic_models.freetier_classes.FreeTierUsageTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.freetier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


