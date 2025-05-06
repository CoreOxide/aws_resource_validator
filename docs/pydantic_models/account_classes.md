# Account Classes

# AcceptPrimaryEmailUpdateRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Otp
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryEmail
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptPrimaryEmailUpdateResponse

### Status
- **Type**: typing.Literal['ACCEPTED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


# AlternateContact

### AlternateContactType
- **Type**: typing.Optional[typing.Literal['BILLING', 'OPERATIONS', 'SECURITY']]

### EmailAddress
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContactInformation

### AddressLine1
- **Type**: <class 'str'>
- **Required**: Yes

### City
- **Type**: <class 'str'>
- **Required**: Yes

### CountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### FullName
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PostalCode
- **Type**: <class 'str'>
- **Required**: Yes

### AddressLine2
- **Type**: typing.Optional[str]

### AddressLine3
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### DistrictOrCounty
- **Type**: typing.Optional[str]

### StateOrRegion
- **Type**: typing.Optional[str]

### WebsiteUrl
- **Type**: typing.Optional[str]


# DeleteAlternateContactRequest

### AlternateContactType
- **Type**: typing.Literal['BILLING', 'OPERATIONS', 'SECURITY']
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DisableRegionRequest

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


# EnableRegionRequest

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# GetAlternateContactRequest

### AlternateContactType
- **Type**: typing.Literal['BILLING', 'OPERATIONS', 'SECURITY']
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# GetAlternateContactResponse

### AlternateContact
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.AlternateContact'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactInformationRequest

### AccountId
- **Type**: typing.Optional[str]


# GetContactInformationResponse

### ContactInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ContactInformation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


# GetPrimaryEmailRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrimaryEmailResponse

### PrimaryEmail
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegionOptStatusRequest

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# GetRegionOptStatusResponse

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### RegionOptStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


# ListRegionsRequest

### AccountId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RegionOptStatusContains
- **Type**: typing.Optional[typing.List[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']]]


# ListRegionsRequestPaginate

### AccountId
- **Type**: typing.Optional[str]

### RegionOptStatusContains
- **Type**: typing.Optional[typing.List[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.account.account_classes.PaginatorConfig]


# ListRegionsResponse

### Regions
- **Type**: typing.List[aws_resource_validator.pydantic_models.account.account_classes.Region]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
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


# PutAlternateContactRequest

### AlternateContactType
- **Type**: typing.Literal['BILLING', 'OPERATIONS', 'SECURITY']
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# PutContactInformationRequest

### ContactInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ContactInformation'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# Region

### RegionName
- **Type**: typing.Optional[str]

### RegionOptStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']]


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


# StartPrimaryEmailUpdateRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryEmail
- **Type**: <class 'str'>
- **Required**: Yes


# StartPrimaryEmailUpdateResponse

### Status
- **Type**: typing.Literal['ACCEPTED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account.account_classes.ResponseMetadata'>
- **Required**: Yes


