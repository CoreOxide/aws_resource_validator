# Pydantic Models in route53domains_classes

# AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateDelegationSignerToDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SigningAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.DnssecSigningAttributesTypeDef'>
- **Required**: Yes


# AssociateDelegationSignerToDomainResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingRecordTypeDef

### DomainName
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[typing.Literal['ADD_DNSSEC', 'CHANGE_DOMAIN_OWNER', 'CHANGE_PRIVACY_PROTECTION', 'DELETE_DOMAIN', 'DISABLE_AUTORENEW', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'EXPIRE_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'PUSH_DOMAIN', 'REGISTER_DOMAIN', 'RELEASE_TO_GANDI', 'REMOVE_DNSSEC', 'RENEW_DOMAIN', 'TRANSFER_IN_DOMAIN', 'TRANSFER_ON_RENEW', 'TRANSFER_OUT_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER']]

### InvoiceId
- **Type**: typing.Optional[str]

### BillDate
- **Type**: typing.Optional[datetime.datetime]

### Price
- **Type**: typing.Optional[float]


# CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDomainTransferToAnotherAwsAccountResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CheckDomainAvailabilityRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### IdnLangCode
- **Type**: typing.Optional[str]


# CheckDomainAvailabilityResponseTypeDef

### Availability
- **Type**: typing.Literal['AVAILABLE', 'AVAILABLE_PREORDER', 'AVAILABLE_RESERVED', 'DONT_KNOW', 'INVALID_NAME_FOR_TLD', 'PENDING', 'RESERVED', 'UNAVAILABLE', 'UNAVAILABLE_PREMIUM', 'UNAVAILABLE_RESTRICTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CheckDomainTransferabilityRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthCode
- **Type**: typing.Optional[str]


# CheckDomainTransferabilityResponseTypeDef

### Transferability
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.DomainTransferabilityTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConsentTypeDef

### MaxPrice
- **Type**: <class 'float'>
- **Required**: Yes

### Currency
- **Type**: <class 'str'>
- **Required**: Yes


# ContactDetailOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53domains_classes.ExtraParamTypeDef]]


# ContactDetailTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.ExtraParamTypeDef]]


# DeleteDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTagsForDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToDelete
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisableDomainAutoRenewRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDomainTransferLockRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDomainTransferLockResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateDelegationSignerFromDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateDelegationSignerFromDomainResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DnssecKeyTypeDef

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


# DnssecSigningAttributesTypeDef

### Algorithm
- **Type**: typing.Optional[int]

### Flags
- **Type**: typing.Optional[int]

### PublicKey
- **Type**: typing.Optional[str]


# DomainPriceTypeDef

### Name
- **Type**: typing.Optional[str]

### RegistrationPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrencyTypeDef]

### TransferPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrencyTypeDef]

### RenewalPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrencyTypeDef]

### ChangeOwnershipPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrencyTypeDef]

### RestorationPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PriceWithCurrencyTypeDef]


# DomainSuggestionTypeDef

### DomainName
- **Type**: typing.Optional[str]

### Availability
- **Type**: typing.Optional[str]


# DomainSummaryTypeDef

### DomainName
- **Type**: typing.Optional[str]

### AutoRenew
- **Type**: typing.Optional[bool]

### TransferLock
- **Type**: typing.Optional[bool]

### Expiry
- **Type**: typing.Optional[datetime.datetime]


# DomainTransferabilityTypeDef

### Transferable
- **Type**: typing.Optional[typing.Literal['DOMAIN_IN_ANOTHER_ACCOUNT', 'DOMAIN_IN_OWN_ACCOUNT', 'DONT_KNOW', 'PREMIUM_DOMAIN', 'TRANSFERABLE', 'UNTRANSFERABLE']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableDomainAutoRenewRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# EnableDomainTransferLockRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# EnableDomainTransferLockResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExtraParamTypeDef

### Name
- **Type**: typing.Literal['AU_ID_NUMBER', 'AU_ID_TYPE', 'AU_PRIORITY_TOKEN', 'BIRTH_CITY', 'BIRTH_COUNTRY', 'BIRTH_DATE_IN_YYYY_MM_DD', 'BIRTH_DEPARTMENT', 'BRAND_NUMBER', 'CA_BUSINESS_ENTITY_TYPE', 'CA_LEGAL_REPRESENTATIVE', 'CA_LEGAL_REPRESENTATIVE_CAPACITY', 'CA_LEGAL_TYPE', 'DOCUMENT_NUMBER', 'DUNS_NUMBER', 'ES_IDENTIFICATION', 'ES_IDENTIFICATION_TYPE', 'ES_LEGAL_FORM', 'EU_COUNTRY_OF_CITIZENSHIP', 'FI_BUSINESS_NUMBER', 'FI_ID_NUMBER', 'FI_NATIONALITY', 'FI_ORGANIZATION_TYPE', 'IT_NATIONALITY', 'IT_PIN', 'IT_REGISTRANT_ENTITY_TYPE', 'RU_PASSPORT_DATA', 'SE_ID_NUMBER', 'SG_ID_NUMBER', 'UK_COMPANY_NUMBER', 'UK_CONTACT_TYPE', 'VAT_NUMBER']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# FilterConditionTypeDef

### Name
- **Type**: typing.Literal['DomainName', 'Expiry']
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BEGINS_WITH', 'GE', 'LE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetContactReachabilityStatusRequestRequestTypeDef

### domainName
- **Type**: typing.Optional[str]


# GetContactReachabilityStatusResponseTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DONE', 'EXPIRED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainDetailRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainDetailResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Nameservers
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.NameserverOutputTypeDef]
- **Required**: Yes

### AutoRenew
- **Type**: <class 'bool'>
- **Required**: Yes

### AdminContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutputTypeDef'>
- **Required**: Yes

### RegistrantContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutputTypeDef'>
- **Required**: Yes

### TechContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutputTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DnssecKeyTypeDef]
- **Required**: Yes

### BillingContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailOutputTypeDef'>
- **Required**: Yes

### BillingPrivacy
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainSuggestionsRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SuggestionCount
- **Type**: <class 'int'>
- **Required**: Yes

### OnlyAvailable
- **Type**: <class 'bool'>
- **Required**: Yes


# GetDomainSuggestionsResponseTypeDef

### SuggestionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DomainSuggestionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOperationDetailRequestRequestTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationDetailResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ERROR', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCESSFUL']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ADD_DNSSEC', 'CHANGE_DOMAIN_OWNER', 'CHANGE_PRIVACY_PROTECTION', 'DELETE_DOMAIN', 'DISABLE_AUTORENEW', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'EXPIRE_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'PUSH_DOMAIN', 'REGISTER_DOMAIN', 'RELEASE_TO_GANDI', 'REMOVE_DNSSEC', 'RENEW_DOMAIN', 'TRANSFER_IN_DOMAIN', 'TRANSFER_ON_RENEW', 'TRANSFER_OUT_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER']
- **Required**: Yes

### SubmittedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusFlag
- **Type**: typing.Literal['PENDING_ACCEPTANCE', 'PENDING_AUTHORIZATION', 'PENDING_CUSTOMER_ACTION', 'PENDING_PAYMENT_VERIFICATION', 'PENDING_SUPPORT_CASE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsRequestListDomainsPaginateTypeDef

### FilterConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.FilterConditionTypeDef]]

### SortCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.SortConditionTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfigTypeDef]


# ListDomainsRequestRequestTypeDef

### FilterConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.FilterConditionTypeDef]]

### SortCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.SortConditionTypeDef]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListDomainsResponseTypeDef

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DomainSummaryTypeDef]
- **Required**: Yes

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOperationsRequestListOperationsPaginateTypeDef

### SubmittedSince
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ERROR', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCESSFUL']]]

### Type
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADD_DNSSEC', 'CHANGE_DOMAIN_OWNER', 'CHANGE_PRIVACY_PROTECTION', 'DELETE_DOMAIN', 'DISABLE_AUTORENEW', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'EXPIRE_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'PUSH_DOMAIN', 'REGISTER_DOMAIN', 'RELEASE_TO_GANDI', 'REMOVE_DNSSEC', 'RENEW_DOMAIN', 'TRANSFER_IN_DOMAIN', 'TRANSFER_ON_RENEW', 'TRANSFER_OUT_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER']]]

### SortBy
- **Type**: typing.Optional[typing.Literal['SubmittedDate']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfigTypeDef]


# ListOperationsRequestRequestTypeDef

### SubmittedSince
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ERROR', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCESSFUL']]]

### Type
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADD_DNSSEC', 'CHANGE_DOMAIN_OWNER', 'CHANGE_PRIVACY_PROTECTION', 'DELETE_DOMAIN', 'DISABLE_AUTORENEW', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'EXPIRE_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'PUSH_DOMAIN', 'REGISTER_DOMAIN', 'RELEASE_TO_GANDI', 'REMOVE_DNSSEC', 'RENEW_DOMAIN', 'TRANSFER_IN_DOMAIN', 'TRANSFER_ON_RENEW', 'TRANSFER_OUT_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER']]]

### SortBy
- **Type**: typing.Optional[typing.Literal['SubmittedDate']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListOperationsResponseTypeDef

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.OperationSummaryTypeDef]
- **Required**: Yes

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPricesRequestListPricesPaginateTypeDef

### Tld
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfigTypeDef]


# ListPricesRequestRequestTypeDef

### Tld
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPricesResponseTypeDef

### Prices
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.DomainPriceTypeDef]
- **Required**: Yes

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForDomainResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NameserverOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GlueIps
- **Type**: typing.Optional[typing.List[str]]


# NameserverTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GlueIps
- **Type**: typing.Optional[typing.Sequence[str]]


# OperationSummaryTypeDef

### OperationId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'FAILED', 'IN_PROGRESS', 'SUBMITTED', 'SUCCESSFUL']]

### Type
- **Type**: typing.Optional[typing.Literal['ADD_DNSSEC', 'CHANGE_DOMAIN_OWNER', 'CHANGE_PRIVACY_PROTECTION', 'DELETE_DOMAIN', 'DISABLE_AUTORENEW', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'EXPIRE_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'PUSH_DOMAIN', 'REGISTER_DOMAIN', 'RELEASE_TO_GANDI', 'REMOVE_DNSSEC', 'RENEW_DOMAIN', 'TRANSFER_IN_DOMAIN', 'TRANSFER_ON_RENEW', 'TRANSFER_OUT_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER']]

### SubmittedDate
- **Type**: typing.Optional[datetime.datetime]

### DomainName
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### StatusFlag
- **Type**: typing.Optional[typing.Literal['PENDING_ACCEPTANCE', 'PENDING_AUTHORIZATION', 'PENDING_CUSTOMER_ACTION', 'PENDING_PAYMENT_VERIFICATION', 'PENDING_SUPPORT_CASE']]

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PriceWithCurrencyTypeDef

### Price
- **Type**: <class 'float'>
- **Required**: Yes

### Currency
- **Type**: <class 'str'>
- **Required**: Yes


# PushDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInYears
- **Type**: <class 'int'>
- **Required**: Yes

### AdminContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef'>
- **Required**: Yes

### RegistrantContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef'>
- **Required**: Yes

### TechContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef]

### PrivacyProtectBillingContact
- **Type**: typing.Optional[bool]


# RegisterDomainResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# RejectDomainTransferFromAnotherAwsAccountResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RenewDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentExpiryYear
- **Type**: <class 'int'>
- **Required**: Yes

### DurationInYears
- **Type**: typing.Optional[int]


# RenewDomainResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResendContactReachabilityEmailRequestRequestTypeDef

### domainName
- **Type**: typing.Optional[str]


# ResendContactReachabilityEmailResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResendOperationAuthorizationRequestRequestTypeDef

### OperationId
- **Type**: <class 'str'>
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


# RetrieveDomainAuthCodeRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveDomainAuthCodeResponseTypeDef

### AuthCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SortConditionTypeDef

### Name
- **Type**: typing.Literal['DomainName', 'Expiry']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TransferDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInYears
- **Type**: <class 'int'>
- **Required**: Yes

### AdminContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef'>
- **Required**: Yes

### RegistrantContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef'>
- **Required**: Yes

### TechContact
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef'>
- **Required**: Yes

### IdnLangCode
- **Type**: typing.Optional[str]

### Nameservers
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.route53domains_classes.NameserverTypeDef, aws_resource_validator.pydantic_models.route53domains_classes.NameserverOutputTypeDef]]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef]

### PrivacyProtectBillingContact
- **Type**: typing.Optional[bool]


# TransferDomainResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TransferDomainToAnotherAwsAccountRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# TransferDomainToAnotherAwsAccountResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainContactPrivacyRequestRequestTypeDef

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


# UpdateDomainContactPrivacyResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainContactRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AdminContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef]

### RegistrantContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef]

### TechContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef]

### Consent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ConsentTypeDef]

### BillingContact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.ContactDetailTypeDef]


# UpdateDomainContactResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainNameserversRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Nameservers
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.route53domains_classes.NameserverTypeDef, aws_resource_validator.pydantic_models.route53domains_classes.NameserverOutputTypeDef]]
- **Required**: Yes

### FIAuthKey
- **Type**: typing.Optional[str]


# UpdateDomainNameserversResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTagsForDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53domains_classes.TagTypeDef]]


# ViewBillingRequestRequestTypeDef

### Start
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### End
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ViewBillingRequestViewBillingPaginateTypeDef

### Start
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### End
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53domains_classes.PaginatorConfigTypeDef]


# ViewBillingResponseTypeDef

### NextPageMarker
- **Type**: <class 'str'>
- **Required**: Yes

### BillingRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53domains_classes.BillingRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53domains_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


