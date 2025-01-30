# marketplace_entitlement_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntitlementTypeDef

### ProductCode
- **Type**: typing.Optional[str]

### Dimension
- **Type**: typing.Optional[str]

### CustomerIdentifier
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_entitlement_classes.EntitlementValueTypeDef]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]


# EntitlementValueTypeDef

### IntegerValue
- **Type**: typing.Optional[int]

### DoubleValue
- **Type**: typing.Optional[float]

### BooleanValue
- **Type**: typing.Optional[bool]

### StringValue
- **Type**: typing.Optional[str]


# GetEntitlementsRequestGetEntitlementsPaginateTypeDef

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CUSTOMER_IDENTIFIER', 'DIMENSION'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_entitlement_classes.PaginatorConfigTypeDef]


# GetEntitlementsRequestRequestTypeDef

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CUSTOMER_IDENTIFIER', 'DIMENSION'], typing.Sequence[str]]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetEntitlementsResultTypeDef

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_entitlement_classes.EntitlementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_entitlement_classes.ResponseMetadataTypeDef'>
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


