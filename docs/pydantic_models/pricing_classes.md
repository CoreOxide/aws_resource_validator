# Pricing Classes

# AttributeValueTypeDef

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeServicesRequestPaginateTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### FormatVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfigTypeDef]


# DescribeServicesRequestTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### FormatVersion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeServicesResponseTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.pricing_classes.ServiceTypeDef]
- **Required**: Yes

### FormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# FilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAttributeValuesRequestPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfigTypeDef]


# GetAttributeValuesRequestTypeDef

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


# GetAttributeValuesResponseTypeDef

### AttributeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.pricing_classes.AttributeValueTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPriceListFileUrlRequestTypeDef

### PriceListArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileFormat
- **Type**: <class 'str'>
- **Required**: Yes


# GetPriceListFileUrlResponseTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProductsRequestPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pricing_classes.FilterTypeDef]]

### FormatVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfigTypeDef]


# GetProductsRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pricing_classes.FilterTypeDef]]

### FormatVersion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetProductsResponseTypeDef

### FormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PriceList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPriceListsRequestPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveDate
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.TimestampTypeDef'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### RegionCode
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pricing_classes.PaginatorConfigTypeDef]


# ListPriceListsRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveDate
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.TimestampTypeDef'>
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


# ListPriceListsResponseTypeDef

### PriceLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.pricing_classes.PriceListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pricing_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PriceListTypeDef

### PriceListArn
- **Type**: typing.Optional[str]

### RegionCode
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### FileFormats
- **Type**: typing.Optional[typing.List[str]]


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


# ServiceTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.List[str]]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

