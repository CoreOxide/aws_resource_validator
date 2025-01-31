# Acm Classes

# AddTagsToCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateDetailTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.List[str]]

### DomainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_classes.DomainValidationTypeDef]]

### Serial
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### IssuedAt
- **Type**: typing.Optional[datetime.datetime]

### ImportedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]

### RevokedAt
- **Type**: typing.Optional[datetime.datetime]

### RevocationReason
- **Type**: typing.Optional[typing.Literal['AFFILIATION_CHANGED', 'A_A_COMPROMISE', 'CA_COMPROMISE', 'CERTIFICATE_HOLD', 'CESSATION_OF_OPERATION', 'KEY_COMPROMISE', 'PRIVILEGE_WITHDRAWN', 'REMOVE_FROM_CRL', 'SUPERCEDED', 'UNSPECIFIED']]

### NotBefore
- **Type**: typing.Optional[datetime.datetime]

### NotAfter
- **Type**: typing.Optional[datetime.datetime]

### KeyAlgorithm
- **Type**: typing.Optional[typing.Literal['EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1', 'RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096']]

### SignatureAlgorithm
- **Type**: typing.Optional[str]

### InUseBy
- **Type**: typing.Optional[typing.List[str]]

### FailureReason
- **Type**: typing.Optional[typing.Literal['ADDITIONAL_VERIFICATION_REQUIRED', 'CAA_ERROR', 'DOMAIN_NOT_ALLOWED', 'DOMAIN_VALIDATION_DENIED', 'INVALID_PUBLIC_DOMAIN', 'NO_AVAILABLE_CONTACTS', 'OTHER', 'PCA_ACCESS_DENIED', 'PCA_INVALID_ARGS', 'PCA_INVALID_ARN', 'PCA_INVALID_DURATION', 'PCA_INVALID_STATE', 'PCA_LIMIT_EXCEEDED', 'PCA_NAME_CONSTRAINTS_VALIDATION', 'PCA_REQUEST_FAILED', 'PCA_RESOURCE_NOT_FOUND', 'SLR_NOT_FOUND']]

### Type
- **Type**: typing.Optional[typing.Literal['AMAZON_ISSUED', 'IMPORTED', 'PRIVATE']]

### RenewalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.RenewalSummaryTypeDef]

### KeyUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_classes.KeyUsageTypeDef]]

### ExtendedKeyUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_classes.ExtendedKeyUsageTypeDef]]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### RenewalEligibility
- **Type**: typing.Optional[typing.Literal['ELIGIBLE', 'INELIGIBLE']]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.CertificateOptionsTypeDef]


# CertificateOptionsTypeDef

### CertificateTransparencyLoggingPreference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CertificateSummaryTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### SubjectAlternativeNameSummaries
- **Type**: typing.Optional[typing.List[str]]

### HasAdditionalSubjectAlternativeNames
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]

### Type
- **Type**: typing.Optional[typing.Literal['AMAZON_ISSUED', 'IMPORTED', 'PRIVATE']]

### KeyAlgorithm
- **Type**: typing.Optional[typing.Literal['EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1', 'RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096']]

### KeyUsages
- **Type**: typing.Optional[typing.List[typing.Literal['ANY', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'CUSTOM', 'DATA_ENCIPHERMENT', 'DECIPHER_ONLY', 'DIGITAL_SIGNATURE', 'ENCIPHER_ONLY', 'KEY_AGREEMENT', 'KEY_ENCIPHERMENT', 'NON_REPUDIATION']]]

### ExtendedKeyUsages
- **Type**: typing.Optional[typing.List[typing.Literal['ANY', 'CODE_SIGNING', 'CUSTOM', 'EMAIL_PROTECTION', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'NONE', 'OCSP_SIGNING', 'TIME_STAMPING', 'TLS_WEB_CLIENT_AUTHENTICATION', 'TLS_WEB_SERVER_AUTHENTICATION']]]

### InUse
- **Type**: typing.Optional[bool]

### Exported
- **Type**: typing.Optional[bool]

### RenewalEligibility
- **Type**: typing.Optional[typing.Literal['ELIGIBLE', 'INELIGIBLE']]

### NotBefore
- **Type**: typing.Optional[datetime.datetime]

### NotAfter
- **Type**: typing.Optional[datetime.datetime]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### IssuedAt
- **Type**: typing.Optional[datetime.datetime]

### ImportedAt
- **Type**: typing.Optional[datetime.datetime]

### RevokedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequestCertificateValidatedWaitTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.WaiterConfigTypeDef]


# DescribeCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResponseTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.CertificateDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainValidationOptionTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationDomain
- **Type**: <class 'str'>
- **Required**: Yes


# DomainValidationTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationEmails
- **Type**: typing.Optional[typing.List[str]]

### ValidationDomain
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]

### ResourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.ResourceRecordTypeDef]

### ValidationMethod
- **Type**: typing.Optional[typing.Literal['DNS', 'EMAIL']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExpiryEventsConfigurationTypeDef

### DaysBeforeExpiry
- **Type**: typing.Optional[int]


# ExportCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Passphrase
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# ExportCertificateResponseTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExtendedKeyUsageTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['ANY', 'CODE_SIGNING', 'CUSTOM', 'EMAIL_PROTECTION', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'NONE', 'OCSP_SIGNING', 'TIME_STAMPING', 'TLS_WEB_CLIENT_AUTHENTICATION', 'TLS_WEB_SERVER_AUTHENTICATION']]

### OID
- **Type**: typing.Optional[str]


# FiltersTypeDef

### extendedKeyUsage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANY', 'CODE_SIGNING', 'CUSTOM', 'EMAIL_PROTECTION', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'NONE', 'OCSP_SIGNING', 'TIME_STAMPING', 'TLS_WEB_CLIENT_AUTHENTICATION', 'TLS_WEB_SERVER_AUTHENTICATION']]]

### keyUsage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANY', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'CUSTOM', 'DATA_ENCIPHERMENT', 'DECIPHER_ONLY', 'DIGITAL_SIGNATURE', 'ENCIPHER_ONLY', 'KEY_AGREEMENT', 'KEY_ENCIPHERMENT', 'NON_REPUDIATION']]]

### keyTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1', 'RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096']]]


# GetAccountConfigurationResponseTypeDef

### ExpiryEvents
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ExpiryEventsConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateResponseTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportCertificateRequestRequestTypeDef

### Certificate
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### PrivateKey
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]]


# ImportCertificateResponseTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KeyUsageTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['ANY', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'CUSTOM', 'DATA_ENCIPHERMENT', 'DECIPHER_ONLY', 'DIGITAL_SIGNATURE', 'ENCIPHER_ONLY', 'KEY_AGREEMENT', 'KEY_ENCIPHERMENT', 'NON_REPUDIATION']]


# ListCertificatesRequestListCertificatesPaginateTypeDef

### CertificateStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]]

### Includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.FiltersTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.PaginatorConfigTypeDef]


# ListCertificatesRequestRequestTypeDef

### CertificateStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]]

### Includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.FiltersTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListCertificatesResponseTypeDef

### CertificateSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_classes.CertificateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForCertificateResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAccountConfigurationRequestRequestTypeDef

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiryEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.ExpiryEventsConfigurationTypeDef]


# RemoveTagsFromCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]
- **Required**: Yes


# RenewCertificateRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# RenewalSummaryTypeDef

### RenewalStatus
- **Type**: typing.Literal['FAILED', 'PENDING_AUTO_RENEWAL', 'PENDING_VALIDATION', 'SUCCESS']
- **Required**: Yes

### DomainValidationOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_classes.DomainValidationTypeDef]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RenewalStatusReason
- **Type**: typing.Optional[typing.Literal['ADDITIONAL_VERIFICATION_REQUIRED', 'CAA_ERROR', 'DOMAIN_NOT_ALLOWED', 'DOMAIN_VALIDATION_DENIED', 'INVALID_PUBLIC_DOMAIN', 'NO_AVAILABLE_CONTACTS', 'OTHER', 'PCA_ACCESS_DENIED', 'PCA_INVALID_ARGS', 'PCA_INVALID_ARN', 'PCA_INVALID_DURATION', 'PCA_INVALID_STATE', 'PCA_LIMIT_EXCEEDED', 'PCA_NAME_CONSTRAINTS_VALIDATION', 'PCA_REQUEST_FAILED', 'PCA_RESOURCE_NOT_FOUND', 'SLR_NOT_FOUND']]


# RequestCertificateRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationMethod
- **Type**: typing.Optional[typing.Literal['DNS', 'EMAIL']]

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### IdempotencyToken
- **Type**: typing.Optional[str]

### DomainValidationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.DomainValidationOptionTypeDef]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.CertificateOptionsTypeDef]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]]

### KeyAlgorithm
- **Type**: typing.Optional[typing.Literal['EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1', 'RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096']]


# RequestCertificateResponseTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResendValidationEmailRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationDomain
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRecordTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['CNAME']
- **Required**: Yes

### Value
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


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# UpdateCertificateOptionsRequestRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.CertificateOptionsTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


