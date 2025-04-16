# Acm Classes

# AddTagsToCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.Tag]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateOptions

### CertificateTransparencyLoggingPreference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CertificateSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequestWait

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCertificateResponse

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.CertificateDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# DomainValidation

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
- **Type**: <class 'NoneType'>

### ValidationMethod
- **Type**: typing.Optional[typing.Literal['DNS', 'EMAIL']]


# DomainValidationOption

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationDomain
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# ExpiryEventsConfiguration

### DaysBeforeExpiry
- **Type**: typing.Optional[int]


# ExportCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Passphrase
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.Blob'>
- **Required**: Yes


# ExportCertificateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# ExtendedKeyUsage

### Name
- **Type**: typing.Optional[typing.Literal['ANY', 'CODE_SIGNING', 'CUSTOM', 'EMAIL_PROTECTION', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'NONE', 'OCSP_SIGNING', 'TIME_STAMPING', 'TLS_WEB_CLIENT_AUTHENTICATION', 'TLS_WEB_SERVER_AUTHENTICATION']]

### OID
- **Type**: typing.Optional[str]


# Filters

### extendedKeyUsage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANY', 'CODE_SIGNING', 'CUSTOM', 'EMAIL_PROTECTION', 'IPSEC_END_SYSTEM', 'IPSEC_TUNNEL', 'IPSEC_USER', 'NONE', 'OCSP_SIGNING', 'TIME_STAMPING', 'TLS_WEB_CLIENT_AUTHENTICATION', 'TLS_WEB_SERVER_AUTHENTICATION']]]

### keyUsage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANY', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'CUSTOM', 'DATA_ENCIPHERMENT', 'DECIPHER_ONLY', 'DIGITAL_SIGNATURE', 'ENCIPHER_ONLY', 'KEY_AGREEMENT', 'KEY_ENCIPHERMENT', 'NON_REPUDIATION']]]

### keyTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1', 'RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096']]]


# GetAccountConfigurationResponse

### ExpiryEvents
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ExpiryEventsConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# GetCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateResponse

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# ImportCertificateRequest

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.Blob'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.Blob'>
- **Required**: Yes

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.Blob]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.Tag]]


# ImportCertificateResponse

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# KeyUsage

### Name
- **Type**: typing.Optional[typing.Literal['ANY', 'CERTIFICATE_SIGNING', 'CRL_SIGNING', 'CUSTOM', 'DATA_ENCIPHERMENT', 'DECIPHER_ONLY', 'DIGITAL_SIGNATURE', 'ENCIPHER_ONLY', 'KEY_AGREEMENT', 'KEY_ENCIPHERMENT', 'NON_REPUDIATION']]


# ListCertificatesRequest

### CertificateStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]]

### Includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.Filters]

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListCertificatesRequestPaginate

### CertificateStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]]

### Includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.Filters]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATED_AT']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.PaginatorConfig]


# ListCertificatesResponse

### CertificateSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_classes.CertificateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForCertificateResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAccountConfigurationRequest

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiryEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.ExpiryEventsConfiguration]


# RemoveTagsFromCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.Tag]
- **Required**: Yes


# RenewCertificateRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# RenewalSummary

### RenewalStatus
- **Type**: typing.Literal['FAILED', 'PENDING_AUTO_RENEWAL', 'PENDING_VALIDATION', 'SUCCESS']
- **Required**: Yes

### DomainValidationOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_classes.DomainValidation]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RenewalStatusReason
- **Type**: typing.Optional[typing.Literal['ADDITIONAL_VERIFICATION_REQUIRED', 'CAA_ERROR', 'DOMAIN_NOT_ALLOWED', 'DOMAIN_VALIDATION_DENIED', 'INVALID_PUBLIC_DOMAIN', 'NO_AVAILABLE_CONTACTS', 'OTHER', 'PCA_ACCESS_DENIED', 'PCA_INVALID_ARGS', 'PCA_INVALID_ARN', 'PCA_INVALID_DURATION', 'PCA_INVALID_STATE', 'PCA_LIMIT_EXCEEDED', 'PCA_NAME_CONSTRAINTS_VALIDATION', 'PCA_REQUEST_FAILED', 'PCA_RESOURCE_NOT_FOUND', 'SLR_NOT_FOUND']]


# RequestCertificateRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.DomainValidationOption]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_classes.CertificateOptions]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_classes.Tag]]

### KeyAlgorithm
- **Type**: typing.Optional[typing.Literal['EC_prime256v1', 'EC_secp384r1', 'EC_secp521r1', 'RSA_1024', 'RSA_2048', 'RSA_3072', 'RSA_4096']]


# RequestCertificateResponse

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.ResponseMetadata'>
- **Required**: Yes


# ResendValidationEmailRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationDomain
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRecord

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[str]


# UpdateCertificateOptionsRequest

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_classes.CertificateOptions'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


