# Marketplace Entitlement Marketplace Entitlement Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Entitlement

### ProductCode
- **Type**: typing.Optional[str]

### Dimension
- **Type**: typing.Optional[str]

### CustomerIdentifier
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_entitlement.marketplace_entitlement_classes.EntitlementValue]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]


# EntitlementValue

### IntegerValue
- **Type**: typing.Optional[int]

### DoubleValue
- **Type**: typing.Optional[float]

### BooleanValue
- **Type**: typing.Optional[bool]

### StringValue
- **Type**: typing.Optional[str]


# GetEntitlementsRequest

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[typing.Dict[typing.Literal['CUSTOMER_IDENTIFIER', 'DIMENSION'], typing.List[str]]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetEntitlementsRequestPaginate

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[typing.Dict[typing.Literal['CUSTOMER_IDENTIFIER', 'DIMENSION'], typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_entitlement.marketplace_entitlement_classes.PaginatorConfig]


# GetEntitlementsResult

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_entitlement.marketplace_entitlement_classes.Entitlement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_entitlement.marketplace_entitlement_classes.ResponseMetadata'>
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


