# Acm Classes

# AddTagsToCertificateRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateOptionsTypeDef

### CertificateTransparencyLoggingPreference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CertificateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteCertificateRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequestWaitTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.WaiterConfigTypeDef]


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


# ExportCertificateRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Passphrase
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.BlobTypeDef'>
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


# GetCertificateRequestTypeDef

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


# ImportCertificateRequestTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.BlobTypeDef'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.BlobTypeDef'>
- **Required**: Yes

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.BlobTypeDef]

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


# ListCertificatesRequestPaginateTypeDef

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


# ListCertificatesRequestTypeDef

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


# ListTagsForCertificateRequestTypeDef

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


# PutAccountConfigurationRequestTypeDef

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiryEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.ExpiryEventsConfigurationTypeDef]


# RemoveTagsFromCertificateRequestTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.TagTypeDef]
- **Required**: Yes


# RenewCertificateRequestTypeDef

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


# RequestCertificateRequestTypeDef

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


# ResendValidationEmailRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# UpdateCertificateOptionsRequestTypeDef

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


