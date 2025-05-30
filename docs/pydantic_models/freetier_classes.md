# Freetier Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DimensionValues

### Key
- **Type**: typing.Literal['DESCRIPTION', 'FREE_TIER_TYPE', 'OPERATION', 'REGION', 'SERVICE', 'USAGE_PERCENTAGE', 'USAGE_TYPE']
- **Required**: Yes

### MatchOptions
- **Type**: typing.List[typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# Expression

### And
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier.freetier_classes.DimensionValues]

### Not
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ExpressionPaginator

### And
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier.freetier_classes.DimensionValues]

### Not
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FreeTierUsage

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


# GetFreeTierUsageRequest

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier.freetier_classes.Expression]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFreeTierUsageRequestPaginate

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier.freetier_classes.ExpressionPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.freetier.freetier_classes.PaginatorConfig]


# GetFreeTierUsageResponse

### freeTierUsages
- **Type**: typing.List[aws_resource_validator.pydantic_models.freetier.freetier_classes.FreeTierUsage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.freetier.freetier_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


