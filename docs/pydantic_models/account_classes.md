# Account Classes

# AcceptPrimaryEmailUpdateRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Otp
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryEmail
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptPrimaryEmailUpdateResponseTypeDef

### Status
- **Type**: typing.Literal['ACCEPTED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AlternateContactTypeDef

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

# ContactInformationTypeDef

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


# DeleteAlternateContactRequestRequestTypeDef

### AlternateContactType
- **Type**: typing.Literal['BILLING', 'OPERATIONS', 'SECURITY']
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DisableRegionRequestRequestTypeDef

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableRegionRequestRequestTypeDef

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# GetAlternateContactRequestRequestTypeDef

### AlternateContactType
- **Type**: typing.Literal['BILLING', 'OPERATIONS', 'SECURITY']
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# GetAlternateContactResponseTypeDef

### AlternateContact
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.AlternateContactTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactInformationRequestRequestTypeDef

### AccountId
- **Type**: typing.Optional[str]


# GetContactInformationResponseTypeDef

### ContactInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ContactInformationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPrimaryEmailRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrimaryEmailResponseTypeDef

### PrimaryEmail
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegionOptStatusRequestRequestTypeDef

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# GetRegionOptStatusResponseTypeDef

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### RegionOptStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRegionsRequestListRegionsPaginateTypeDef

### AccountId
- **Type**: typing.Optional[str]

### RegionOptStatusContains
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.account_classes.PaginatorConfigTypeDef]


# ListRegionsRequestRequestTypeDef

### AccountId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RegionOptStatusContains
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']]]


# ListRegionsResponseTypeDef

### Regions
- **Type**: typing.List[aws_resource_validator.pydantic_models.account_classes.RegionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
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


# PutAlternateContactRequestRequestTypeDef

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


# PutContactInformationRequestRequestTypeDef

### ContactInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ContactInformationTypeDef'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# RegionTypeDef

### RegionName
- **Type**: typing.Optional[str]

### RegionOptStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLED_BY_DEFAULT', 'ENABLING']]


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


# StartPrimaryEmailUpdateRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryEmail
- **Type**: <class 'str'>
- **Required**: Yes


# StartPrimaryEmailUpdateResponseTypeDef

### Status
- **Type**: typing.Literal['ACCEPTED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.account_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


