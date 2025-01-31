# Meteringmarketplace Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchMeterUsageRequestRequestTypeDef

### UsageRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordTypeDef]
- **Required**: Yes

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes


# BatchMeterUsageResultTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordResultTypeDef]
- **Required**: Yes

### UnprocessedRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MeterUsageRequestRequestTypeDef

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### UsageDimension
- **Type**: <class 'str'>
- **Required**: Yes

### UsageQuantity
- **Type**: typing.Optional[int]

### DryRun
- **Type**: typing.Optional[bool]

### UsageAllocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageAllocationTypeDef]]


# MeterUsageResultTypeDef

### MeteringRecordId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterUsageRequestRequestTypeDef

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


# ResolveCustomerRequestRequestTypeDef

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


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UsageAllocationTypeDef

### AllocatedUsageQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.TagTypeDef]]


# UsageRecordResultTypeDef

### UsageRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageRecordTypeDef]

### MeteringRecordId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CustomerNotSubscribed', 'DuplicateRecord', 'Success']]


# UsageRecordTypeDef

### Timestamp
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.meteringmarketplace_classes.UsageAllocationTypeDef]]


