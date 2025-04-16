# Route53Domains Classes

# AcceptDomainTransferFromAnotherAwsAccountRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptDomainTransferFromAnotherAwsAccountResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateDelegationSignerToDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SigningAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.DnssecSigningAttributes'>
- **Required**: Yes


# AssociateDelegationSignerToDomainResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingRecord

### DomainName
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[typing.Literal['ADD_DNSSEC', 'CHANGE_DOMAIN_OWNER', 'CHANGE_PRIVACY_PROTECTION', 'DELETE_DOMAIN', 'DISABLE_AUTORENEW', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'EXPIRE_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'PUSH_DOMAIN', 'REGISTER_DOMAIN', 'RELEASE_TO_GANDI', 'REMOVE_DNSSEC', 'RENEW_DOMAIN', 'RESTORE_DOMAIN', 'TRANSFER_IN_DOMAIN', 'TRANSFER_ON_RENEW', 'TRANSFER_OUT_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER']]

### InvoiceId
- **Type**: typing.Optional[str]

### BillDate
- **Type**: typing.Optional[datetime.datetime]

### Price
- **Type**: typing.Optional[float]


# CancelDomainTransferToAnotherAwsAccountRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDomainTransferToAnotherAwsAccountResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# CheckDomainAvailabilityRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### IdnLangCode
- **Type**: typing.Optional[str]


# CheckDomainAvailabilityResponse

### Availability
- **Type**: typing.Literal['AVAILABLE', 'AVAILABLE_PREORDER', 'AVAILABLE_RESERVED', 'DONT_KNOW', 'INVALID_NAME_FOR_TLD', 'PENDING', 'RESERVED', 'UNAVAILABLE', 'UNAVAILABLE_PREMIUM', 'UNAVAILABLE_RESTRICTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# CheckDomainTransferabilityRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthCode
- **Type**: typing.Optional[str]


# CheckDomainTransferabilityResponse

### Transferability
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.DomainTransferability'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# Consent

### MaxPrice
- **Type**: <class 'float'>
- **Required**: Yes

### Currency
- **Type**: <class 'str'>
- **Required**: Yes


# ContactDetail

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### ContactType
- **Type**: typing.Optional[typing.Literal['ASSOCIATION', 'COMPANY', 'PERSON', 'PUBLIC_BODY', 'RESELLER']]

### OrganizationName
- **Type**: typing.Optional[str]

### AddressLine1
- **Type**: typing.Optional[str]

### AddressLine2
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[typing.Literal['AC', 'AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TP', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### ZipCode
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Fax
- **Type**: typing.Optional[str]

### ExtraParams
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.ExtraParam]]


# ContactDetailOutput

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### ContactType
- **Type**: typing.Optional[typing.Literal['ASSOCIATION', 'COMPANY', 'PERSON', 'PUBLIC_BODY', 'RESELLER']]

### OrganizationName
- **Type**: typing.Optional[str]

### AddressLine1
- **Type**: typing.Optional[str]

### AddressLine2
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[typing.Literal['AC', 'AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TP', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### ZipCode
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Fax
- **Type**: typing.Optional[str]

### ExtraParams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53domains_classes.ExtraParam]]


# ContactDetailUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTagsForDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToDelete
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisableDomainAutoRenewRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDomainTransferLockRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDomainTransferLockResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateDelegationSignerFromDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateDelegationSignerFromDomainResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# DnssecKey

### Algorithm
- **Type**: typing.Optional[int]

### Flags
- **Type**: typing.Optional[int]

### PublicKey
- **Type**: typing.Optional[str]

### DigestType
- **Type**: typing.Optional[int]

### Digest
- **Type**: typing.Optional[str]

### KeyTag
- **Type**: typing.Optional[int]

### Id
- **Type**: typing.Optional[str]


# DnssecSigningAttributes

### Algorithm
- **Type**: typing.Optional[int]

### Flags
- **Type**: typing.Optional[int]

### PublicKey
- **Type**: typing.Optional[str]


# DomainPrice

### Name
- **Type**: typing.Optional[str]

### RegistrationPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrency]

### TransferPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrency]

### RenewalPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrency]

### ChangeOwnershipPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrency]

### RestorationPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrency]


# DomainSuggestion

### DomainName
- **Type**: typing.Optional[str]

### Availability
- **Type**: typing.Optional[str]


# DomainSummary

### DomainName
- **Type**: typing.Optional[str]

### AutoRenew
- **Type**: typing.Optional[bool]

### TransferLock
- **Type**: typing.Optional[bool]

### Expiry
- **Type**: typing.Optional[datetime.datetime]


# DomainTransferability

### Transferable
- **Type**: typing.Optional[typing.Literal['DOMAIN_IN_ANOTHER_ACCOUNT', 'DOMAIN_IN_OWN_ACCOUNT', 'DONT_KNOW', 'PREMIUM_DOMAIN', 'TRANSFERABLE', 'UNTRANSFERABLE']]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# EnableDomainAutoRenewRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# EnableDomainTransferLockRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# EnableDomainTransferLockResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# ExtraParam

### Name
- **Type**: typing.Literal['AU_ID_NUMBER', 'AU_ID_TYPE', 'AU_PRIORITY_TOKEN', 'BIRTH_CITY', 'BIRTH_COUNTRY', 'BIRTH_DATE_IN_YYYY_MM_DD', 'BIRTH_DEPARTMENT', 'BRAND_NUMBER', 'CA_BUSINESS_ENTITY_TYPE', 'CA_LEGAL_REPRESENTATIVE', 'CA_LEGAL_REPRESENTATIVE_CAPACITY', 'CA_LEGAL_TYPE', 'DOCUMENT_NUMBER', 'DUNS_NUMBER', 'ES_IDENTIFICATION', 'ES_IDENTIFICATION_TYPE', 'ES_LEGAL_FORM', 'EU_COUNTRY_OF_CITIZENSHIP', 'FI_BUSINESS_NUMBER', 'FI_ID_NUMBER', 'FI_NATIONALITY', 'FI_ORGANIZATION_TYPE', 'IT_NATIONALITY', 'IT_PIN', 'IT_REGISTRANT_ENTITY_TYPE', 'RU_PASSPORT_DATA', 'SE_ID_NUMBER', 'SG_ID_NUMBER', 'UK_COMPANY_NUMBER', 'UK_CONTACT_TYPE', 'VAT_NUMBER']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# FilterCondition

### Name
- **Type**: typing.Literal['DomainName', 'Expiry']
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BEGINS_WITH', 'GE', 'LE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetContactReachabilityStatusRequest

### domainName
- **Type**: typing.Optional[str]


# GetContactReachabilityStatusResponse

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DONE', 'EXPIRED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainDetailRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainDetailResponse

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Nameservers
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.NameserverOutput]
- **Required**: Yes

### AutoRenew
- **Type**: <class 'bool'>
- **Required**: Yes

### AdminContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutput'>
- **Required**: Yes

### RegistrantContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutput'>
- **Required**: Yes

### TechContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutput'>
- **Required**: Yes

### AdminPrivacy
- **Type**: <class 'bool'>
- **Required**: Yes

### RegistrantPrivacy
- **Type**: <class 'bool'>
- **Required**: Yes

### TechPrivacy
- **Type**: <class 'bool'>
- **Required**: Yes

### RegistrarName
- **Type**: <class 'str'>
- **Required**: Yes

### WhoIsServer
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrarUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AbuseContactEmail
- **Type**: <class 'str'>
- **Required**: Yes

### AbuseContactPhone
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExpirationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Reseller
- **Type**: <class 'str'>
- **Required**: Yes

### DnsSec
- **Type**: <class 'str'>
- **Required**: Yes

### StatusList
- **Type**: typing.List[str]
- **Required**: Yes

### DnssecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DnssecKey]
- **Required**: Yes

### BillingContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutput'>
- **Required**: Yes

### BillingPrivacy
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainSuggestionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SuggestionCount
- **Type**: <class 'int'>
- **Required**: Yes

### OnlyAvailable
- **Type**: <class 'bool'>
- **Required**: Yes


# GetDomainSuggestionsResponse

### SuggestionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DomainSuggestion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# GetOperationDetailRequest

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# ListDomainsRequest

### FilterConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.FilterCondition]]

### SortCondition
- **Type**: <class 'NoneType'>

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListDomainsRequestPaginate

### FilterConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.FilterCondition]]

### SortCondition
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfig]


# ListDomainsResponse

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DomainSummary]
- **Required**: Yes

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# ListOperationsResponse

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.OperationSummary]
- **Required**: Yes

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# ListPricesRequest

### Tld
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPricesRequestPaginate

### Tld
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfig]


# ListPricesResponse

### Prices
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DomainPrice]
- **Required**: Yes

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForDomainResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# Nameserver

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GlueIps
- **Type**: typing.Optional[typing.Sequence[str]]


# NameserverOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GlueIps
- **Type**: typing.Optional[typing.List[str]]


# NameserverUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OperationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PriceWithCurrency

### Price
- **Type**: <class 'float'>
- **Required**: Yes

### Currency
- **Type**: <class 'str'>
- **Required**: Yes


# PushDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInYears
- **Type**: <class 'int'>
- **Required**: Yes

### AdminContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion'>
- **Required**: Yes

### RegistrantContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion'>
- **Required**: Yes

### TechContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion'>
- **Required**: Yes

### IdnLangCode
- **Type**: typing.Optional[str]

### AutoRenew
- **Type**: typing.Optional[bool]

### PrivacyProtectAdminContact
- **Type**: typing.Optional[bool]

### PrivacyProtectRegistrantContact
- **Type**: typing.Optional[bool]

### PrivacyProtectTechContact
- **Type**: typing.Optional[bool]

### BillingContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion]

### PrivacyProtectBillingContact
- **Type**: typing.Optional[bool]


# RegisterDomainResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# RejectDomainTransferFromAnotherAwsAccountRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# RejectDomainTransferFromAnotherAwsAccountResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# RenewDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentExpiryYear
- **Type**: <class 'int'>
- **Required**: Yes

### DurationInYears
- **Type**: typing.Optional[int]


# RenewDomainResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# ResendContactReachabilityEmailRequest

### domainName
- **Type**: typing.Optional[str]


# ResendContactReachabilityEmailResponse

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### isAlreadyVerified
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# ResendOperationAuthorizationRequest

### OperationId
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


# RetrieveDomainAuthCodeRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveDomainAuthCodeResponse

### AuthCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# SortCondition

### Name
- **Type**: typing.Literal['DomainName', 'Expiry']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransferDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInYears
- **Type**: <class 'int'>
- **Required**: Yes

### AdminContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion'>
- **Required**: Yes

### RegistrantContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion'>
- **Required**: Yes

### TechContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion'>
- **Required**: Yes

### IdnLangCode
- **Type**: typing.Optional[str]

### Nameservers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.NameserverUnion]]

### AuthCode
- **Type**: typing.Optional[str]

### AutoRenew
- **Type**: typing.Optional[bool]

### PrivacyProtectAdminContact
- **Type**: typing.Optional[bool]

### PrivacyProtectRegistrantContact
- **Type**: typing.Optional[bool]

### PrivacyProtectTechContact
- **Type**: typing.Optional[bool]

### BillingContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion]

### PrivacyProtectBillingContact
- **Type**: typing.Optional[bool]


# TransferDomainResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# TransferDomainToAnotherAwsAccountRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# TransferDomainToAnotherAwsAccountResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainContactPrivacyRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AdminPrivacy
- **Type**: typing.Optional[bool]

### RegistrantPrivacy
- **Type**: typing.Optional[bool]

### TechPrivacy
- **Type**: typing.Optional[bool]

### BillingPrivacy
- **Type**: typing.Optional[bool]


# UpdateDomainContactPrivacyResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainContactRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AdminContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion]

### RegistrantContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion]

### TechContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion]

### Consent
- **Type**: <class 'NoneType'>

### BillingContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailUnion]


# UpdateDomainContactResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainNameserversRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Nameservers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.NameserverUnion]
- **Required**: Yes

### FIAuthKey
- **Type**: typing.Optional[str]


# UpdateDomainNameserversResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTagsForDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.Tag]]


# ViewBillingRequest

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.Timestamp]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.Timestamp]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ViewBillingRequestPaginate

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.Timestamp]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.Timestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfig]


# ViewBillingResponse

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### BillingRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.BillingRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadata'>
- **Required**: Yes


