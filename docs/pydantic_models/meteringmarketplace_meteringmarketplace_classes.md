# Meteringmarketplace Meteringmarketplace Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchMeterUsageRequest

### UsageRecords
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageRecord, aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageRecordOutput]]
- **Required**: Yes

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes


# BatchMeterUsageResult

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageRecordResult]
- **Required**: Yes

### UnprocessedRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageRecordOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.ResponseMetadata'>
- **Required**: Yes


# MeterUsageRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageAllocation, aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageAllocationOutput]]]


# MeterUsageResult

### MeteringRecordId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterUsageRequest

### ProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### PublicKeyVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Nonce
- **Type**: typing.Optional[str]


# RegisterUsageResult

### PublicKeyRotationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Signature
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.ResponseMetadata'>
- **Required**: Yes


# ResolveCustomerRequest

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes


# ResolveCustomerResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.ResponseMetadata'>
- **Required**: Yes


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


# UsageAllocation

### AllocatedUsageQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.Tag]]


# UsageAllocationOutput

### AllocatedUsageQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.Tag]]


# UsageRecord

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageAllocation, aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageAllocationOutput]]]


# UsageRecordOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageAllocationOutput]]


# UsageRecordResult

### UsageRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_classes.UsageRecordOutput]

### MeteringRecordId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CustomerNotSubscribed', 'DuplicateRecord', 'Success']]


