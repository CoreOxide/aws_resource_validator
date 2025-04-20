# Invoicing Invoicing Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetInvoiceProfileRequest

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetInvoiceProfileResponse

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInvoiceUnitRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InvoiceReceiver
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnitRule, aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnitRuleOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TaxInheritanceDisabled
- **Type**: typing.Optional[bool]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResourceTag]]


# CreateInvoiceUnitResponse

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInvoiceUnitRequest

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInvoiceUnitResponse

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes


# Filters

### Names
- **Type**: typing.Optional[typing.List[str]]

### InvoiceReceivers
- **Type**: typing.Optional[typing.List[str]]

### Accounts
- **Type**: typing.Optional[typing.List[str]]


# GetInvoiceUnitRequest

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes

### AsOf
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetInvoiceUnitResponse

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvoiceReceiver
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### TaxInheritanceDisabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnitRuleOutput'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes


# InvoiceProfile

### AccountId
- **Type**: typing.Optional[str]

### ReceiverName
- **Type**: typing.Optional[str]

### ReceiverAddress
- **Type**: <class 'NoneType'>

### ReceiverEmail
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### TaxRegistrationNumber
- **Type**: typing.Optional[str]


# InvoiceUnit

### InvoiceUnitArn
- **Type**: typing.Optional[str]

### InvoiceReceiver
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### TaxInheritanceDisabled
- **Type**: typing.Optional[bool]

### Rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnitRuleOutput]

### LastModified
- **Type**: typing.Optional[datetime.datetime]


# InvoiceUnitRule

### LinkedAccounts
- **Type**: typing.Optional[typing.List[str]]


# InvoiceUnitRuleOutput

### LinkedAccounts
- **Type**: typing.Optional[typing.List[str]]


# ListInvoiceUnitsRequest

### Filters
- **Type**: <class 'NoneType'>

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AsOf
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListInvoiceUnitsRequestPaginate

### Filters
- **Type**: <class 'NoneType'>

### AsOf
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.PaginatorConfig]


# ListInvoiceUnitsResponse

### InvoiceUnits
- **Type**: typing.List[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReceiverAddress

### AddressLine1
- **Type**: typing.Optional[str]

### AddressLine2
- **Type**: typing.Optional[str]

### AddressLine3
- **Type**: typing.Optional[str]

### DistrictOrCounty
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### StateOrRegion
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]


# ResourceTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResourceTag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateInvoiceUnitRequest

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TaxInheritanceDisabled
- **Type**: typing.Optional[bool]

### Rule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnitRule, aws_resource_validator.pydantic_models.invoicing.invoicing_classes.InvoiceUnitRuleOutput, NoneType]


# UpdateInvoiceUnitResponse

### InvoiceUnitArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.invoicing.invoicing_classes.ResponseMetadata'>
- **Required**: Yes


