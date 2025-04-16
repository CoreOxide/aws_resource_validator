# Pricing Classes

# AttributeValue

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeServicesRequest

### ServiceCode
- **Type**: typing.Optional[str]

### FormatVersion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeServicesRequestPaginate

### ServiceCode
- **Type**: typing.Optional[str]

### FormatVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfig]


# DescribeServicesResponse

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.pricing_classes.Service]
- **Required**: Yes

### FormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Filter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAttributeValuesRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAttributeValuesRequestPaginate

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfig]


# GetAttributeValuesResponse

### AttributeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.pricing_classes.AttributeValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPriceListFileUrlRequest

### PriceListArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileFormat
- **Type**: <class 'str'>
- **Required**: Yes


# GetPriceListFileUrlResponse

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadata'>
- **Required**: Yes


# GetProductsRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pricing_classes.Filter]]

### FormatVersion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetProductsRequestPaginate

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pricing_classes.Filter]]

### FormatVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfig]


# GetProductsResponse

### FormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PriceList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPriceListsRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveDate
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.Timestamp'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### RegionCode
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPriceListsRequestPaginate

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveDate
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.Timestamp'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### RegionCode
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfig]


# ListPriceListsResponse

### PriceLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.pricing_classes.PriceList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PriceList

### PriceListArn
- **Type**: typing.Optional[str]

### RegionCode
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### FileFormats
- **Type**: typing.Optional[typing.List[str]]


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


# Service

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.List[str]]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

