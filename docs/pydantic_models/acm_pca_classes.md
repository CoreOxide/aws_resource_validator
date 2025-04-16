# Acm Pca Classes

# ASN1Subject

### Country
- **Type**: typing.Optional[str]

### Organization
- **Type**: typing.Optional[str]

### OrganizationalUnit
- **Type**: typing.Optional[str]

### DistinguishedNameQualifier
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CommonName
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Locality
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### Initials
- **Type**: typing.Optional[str]

### Pseudonym
- **Type**: typing.Optional[str]

### GenerationQualifier
- **Type**: typing.Optional[str]

### CustomAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.CustomAttribute]]


# ASN1SubjectOutput

### Country
- **Type**: typing.Optional[str]

### Organization
- **Type**: typing.Optional[str]

### OrganizationalUnit
- **Type**: typing.Optional[str]

### DistinguishedNameQualifier
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CommonName
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Locality
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### Initials
- **Type**: typing.Optional[str]

### Pseudonym
- **Type**: typing.Optional[str]

### GenerationQualifier
- **Type**: typing.Optional[str]

### CustomAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.CustomAttribute]]


# ASN1SubjectUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessDescription

### AccessMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.AccessMethod'>
- **Required**: Yes

### AccessLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.GeneralName'>
- **Required**: Yes


# AccessDescriptionOutput

### AccessMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.AccessMethod'>
- **Required**: Yes

### AccessLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.GeneralNameOutput'>
- **Required**: Yes


# AccessMethod

### CustomObjectIdentifier
- **Type**: typing.Optional[str]

### AccessMethodType
- **Type**: typing.Optional[typing.Literal['CA_REPOSITORY', 'RESOURCE_PKI_MANIFEST', 'RESOURCE_PKI_NOTIFY']]


# ApiPassthrough

### Extensions
- **Type**: <class 'NoneType'>

### Subject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectUnion]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateAuthority

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateAuthorityConfiguration

### KeyAlgorithm
- **Type**: typing.Literal['EC_prime256v1', 'EC_secp384r1', 'RSA_2048', 'RSA_4096', 'SM2']
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['SHA256WITHECDSA', 'SHA256WITHRSA', 'SHA384WITHECDSA', 'SHA384WITHRSA', 'SHA512WITHECDSA', 'SHA512WITHRSA', 'SM3WITHSM2']
- **Required**: Yes

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ASN1Subject'>
- **Required**: Yes

### CsrExtensions
- **Type**: <class 'NoneType'>


# CertificateAuthorityConfigurationOutput

### KeyAlgorithm
- **Type**: typing.Literal['EC_prime256v1', 'EC_secp384r1', 'RSA_2048', 'RSA_4096', 'SM2']
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['SHA256WITHECDSA', 'SHA256WITHRSA', 'SHA384WITHECDSA', 'SHA384WITHRSA', 'SHA512WITHECDSA', 'SHA512WITHRSA', 'SM3WITHSM2']
- **Required**: Yes

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectOutput'>
- **Required**: Yes

### CsrExtensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.CsrExtensionsOutput]


# CertificateAuthorityConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCertificateAuthorityAuditReportRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### AuditReportResponseFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# CreateCertificateAuthorityAuditReportResponse

### AuditReportId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCertificateAuthorityRequest

### CertificateAuthorityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.CertificateAuthorityConfigurationUnion'>
- **Required**: Yes

### CertificateAuthorityType
- **Type**: typing.Literal['ROOT', 'SUBORDINATE']
- **Required**: Yes

### RevocationConfiguration
- **Type**: <class 'NoneType'>

### IdempotencyToken
- **Type**: typing.Optional[str]

### KeyStorageSecurityStandard
- **Type**: typing.Optional[typing.Literal['CCPC_LEVEL_1_OR_HIGHER', 'FIPS_140_2_LEVEL_2_OR_HIGHER', 'FIPS_140_2_LEVEL_3_OR_HIGHER']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.Tag]]

### UsageMode
- **Type**: typing.Optional[typing.Literal['GENERAL_PURPOSE', 'SHORT_LIVED_CERTIFICATE']]


# CreateCertificateAuthorityResponse

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePermissionRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[typing.Literal['GetCertificate', 'IssueCertificate', 'ListPermissions']]
- **Required**: Yes

### SourceAccount
- **Type**: typing.Optional[str]


# CrlConfiguration

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ExpirationInDays
- **Type**: typing.Optional[int]

### CustomCname
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### S3ObjectAcl
- **Type**: typing.Optional[typing.Literal['BUCKET_OWNER_FULL_CONTROL', 'PUBLIC_READ']]

### CrlDistributionPointExtensionConfiguration
- **Type**: <class 'NoneType'>

### CrlType
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'PARTITIONED']]

### CustomPath
- **Type**: typing.Optional[str]


# CrlDistributionPointExtensionConfiguration

### OmitExtension
- **Type**: <class 'bool'>
- **Required**: Yes


# CsrExtensions

### KeyUsage
- **Type**: <class 'NoneType'>

### SubjectInformationAccess
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.AccessDescription]]


# CsrExtensionsOutput

### KeyUsage
- **Type**: <class 'NoneType'>

### SubjectInformationAccess
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.AccessDescriptionOutput]]


# CustomAttribute

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# CustomExtension

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# DeleteCertificateAuthorityRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermanentDeletionTimeInDays
- **Type**: typing.Optional[int]


# DeletePermissionRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### SourceAccount
- **Type**: typing.Optional[str]


# DeletePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateAuthorityAuditReportRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuditReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateAuthorityAuditReportRequestWait

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuditReportId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCertificateAuthorityAuditReportResponse

### AuditReportStatus
- **Type**: typing.Literal['CREATING', 'FAILED', 'SUCCESS']
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificateAuthorityRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateAuthorityResponse

### CertificateAuthority
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.CertificateAuthority'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# EdiPartyName

### PartyName
- **Type**: <class 'str'>
- **Required**: Yes

### NameAssigner
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# ExtendedKeyUsage

### ExtendedKeyUsageType
- **Type**: typing.Optional[typing.Literal['CERTIFICATE_TRANSPARENCY', 'CLIENT_AUTH', 'CODE_SIGNING', 'DOCUMENT_SIGNING', 'EMAIL_PROTECTION', 'OCSP_SIGNING', 'SERVER_AUTH', 'SMART_CARD_LOGIN', 'TIME_STAMPING']]

### ExtendedKeyUsageObjectIdentifier
- **Type**: typing.Optional[str]


# Extensions

### CertificatePolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.PolicyInformation]]

### ExtendedKeyUsage
- **Type**: typing.Optional[typing.Sequence[NoneType]]

### KeyUsage
- **Type**: <class 'NoneType'>

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.GeneralNameUnion]]

### CustomExtensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.CustomExtension]]


# GeneralName

### OtherName
- **Type**: <class 'NoneType'>

### Rfc822Name
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### DirectoryName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectUnion]

### EdiPartyName
- **Type**: <class 'NoneType'>

### UniformResourceIdentifier
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### RegisteredId
- **Type**: typing.Optional[str]


# GeneralNameOutput

### OtherName
- **Type**: <class 'NoneType'>

### Rfc822Name
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### DirectoryName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectOutput]

### EdiPartyName
- **Type**: <class 'NoneType'>

### UniformResourceIdentifier
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### RegisteredId
- **Type**: typing.Optional[str]


# GeneralNameUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetCertificateAuthorityCertificateRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateAuthorityCertificateResponse

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# GetCertificateAuthorityCsrRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateAuthorityCsrRequestWait

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetCertificateAuthorityCsrResponse

### Csr
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# GetCertificateRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateRequestWait

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetCertificateResponse

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# ImportCertificateAuthorityCertificateRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.Blob'>
- **Required**: Yes

### CertificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.Blob]


# IssueCertificateRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Csr
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.Blob'>
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['SHA256WITHECDSA', 'SHA256WITHRSA', 'SHA384WITHECDSA', 'SHA384WITHRSA', 'SHA512WITHECDSA', 'SHA512WITHRSA', 'SM3WITHSM2']
- **Required**: Yes

### Validity
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.Validity'>
- **Required**: Yes

### ApiPassthrough
- **Type**: <class 'NoneType'>

### TemplateArn
- **Type**: typing.Optional[str]

### ValidityNotBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.Validity]

### IdempotencyToken
- **Type**: typing.Optional[str]


# IssueCertificateResponse

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes


# KeyUsage

### DigitalSignature
- **Type**: typing.Optional[bool]

### NonRepudiation
- **Type**: typing.Optional[bool]

### KeyEncipherment
- **Type**: typing.Optional[bool]

### DataEncipherment
- **Type**: typing.Optional[bool]

### KeyAgreement
- **Type**: typing.Optional[bool]

### KeyCertSign
- **Type**: typing.Optional[bool]

### CRLSign
- **Type**: typing.Optional[bool]

### EncipherOnly
- **Type**: typing.Optional[bool]

### DecipherOnly
- **Type**: typing.Optional[bool]


# ListCertificateAuthoritiesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]


# ListCertificateAuthoritiesRequestPaginate

### ResourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.PaginatorConfig]


# ListCertificateAuthoritiesResponse

### CertificateAuthorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.CertificateAuthority]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequestPaginate

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.PaginatorConfig]


# ListPermissionsResponse

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.Permission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestPaginate

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.PaginatorConfig]


# ListTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OcspConfiguration

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OcspCustomCname
- **Type**: typing.Optional[str]


# OtherName

### TypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Permission

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Principal
- **Type**: typing.Optional[str]

### SourceAccount
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[typing.Literal['GetCertificate', 'IssueCertificate', 'ListPermissions']]]

### Policy
- **Type**: typing.Optional[str]


# PolicyInformation

### CertPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyQualifiers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.PolicyQualifierInfo]]


# PolicyQualifierInfo

### PolicyQualifierId
- **Type**: typing.Literal['CPS']
- **Required**: Yes

### Qualifier
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.Qualifier'>
- **Required**: Yes


# PutPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# Qualifier

### CpsUri
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


# RestoreCertificateAuthorityRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# RevocationConfiguration

### CrlConfiguration
- **Type**: <class 'NoneType'>

### OcspConfiguration
- **Type**: <class 'NoneType'>


# RevokeCertificateRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateSerial
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationReason
- **Type**: typing.Literal['AFFILIATION_CHANGED', 'A_A_COMPROMISE', 'CERTIFICATE_AUTHORITY_COMPROMISE', 'CESSATION_OF_OPERATION', 'KEY_COMPROMISE', 'PRIVILEGE_WITHDRAWN', 'SUPERSEDED', 'UNSPECIFIED']
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagCertificateAuthorityRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.Tag]
- **Required**: Yes


# UntagCertificateAuthorityRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.Tag]
- **Required**: Yes


# UpdateCertificateAuthorityRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationConfiguration
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DISABLED', 'EXPIRED', 'FAILED', 'PENDING_CERTIFICATE']]


# Validity

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


