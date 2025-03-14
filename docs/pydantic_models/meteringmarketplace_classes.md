# Meteringmarketplace Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchMeterUsageRequestTypeDef

### UsageRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordUnionTypeDef]
- **Required**: Yes

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes


# BatchMeterUsageResultTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordResultTypeDef]
- **Required**: Yes

### UnprocessedRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MeterUsageRequestTypeDef

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.TimestampTypeDef'>
- **Required**: Yes

### UsageDimension
- **Type**: <class 'str'>
- **Required**: Yes

### UsageQuantity
- **Type**: typing.Optional[int]

### DryRun
- **Type**: typing.Optional[bool]

### UsageAllocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageAllocationUnionTypeDef]]


# MeterUsageResultTypeDef

### MeteringRecordId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterUsageRequestTypeDef

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### PublicKeyVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Nonce
- **Type**: typing.Optional[str]


# RegisterUsageResultTypeDef

### PublicKeyRotationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Signature
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolveCustomerRequestTypeDef

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes


# ResolveCustomerResultTypeDef

### CustomerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerAWSAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.ResponseMetadataTypeDef'>
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


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsageAllocationOutputTypeDef

### AllocatedUsageQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.meteringmarketplace_classes.TagTypeDef]]


# UsageAllocationTypeDef

### AllocatedUsageQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.TagTypeDef]]


# UsageAllocationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsageRecordOutputTypeDef

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CustomerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Dimension
- **Type**: <class 'str'>
- **Required**: Yes

### Quantity
- **Type**: typing.Optional[int]

### UsageAllocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageAllocationOutputTypeDef]]


# UsageRecordResultTypeDef

### UsageRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordOutputTypeDef]

### MeteringRecordId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CustomerNotSubscribed', 'DuplicateRecord', 'Success']]


# UsageRecordTypeDef

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.TimestampTypeDef'>
- **Required**: Yes

### CustomerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Dimension
- **Type**: <class 'str'>
- **Required**: Yes

### Quantity
- **Type**: typing.Optional[int]

### UsageAllocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageAllocationUnionTypeDef]]


# UsageRecordUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

