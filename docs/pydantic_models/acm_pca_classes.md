# Acm Pca Classes

# ASN1SubjectOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.CustomAttributeTypeDef]]


# ASN1SubjectTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.CustomAttributeTypeDef]]


# ASN1SubjectUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessDescriptionOutputTypeDef

### AccessMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.AccessMethodTypeDef'>
- **Required**: Yes

### AccessLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.GeneralNameOutputTypeDef'>
- **Required**: Yes


# AccessDescriptionTypeDef

### AccessMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.AccessMethodTypeDef'>
- **Required**: Yes

### AccessLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.GeneralNameTypeDef'>
- **Required**: Yes


# AccessMethodTypeDef

### CustomObjectIdentifier
- **Type**: typing.Optional[str]

### AccessMethodType
- **Type**: typing.Optional[typing.Literal['CA_REPOSITORY', 'RESOURCE_PKI_MANIFEST', 'RESOURCE_PKI_NOTIFY']]


# ApiPassthroughTypeDef

### Extensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ExtensionsTypeDef]

### Subject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectUnionTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateAuthorityConfigurationOutputTypeDef

### KeyAlgorithm
- **Type**: typing.Literal['EC_prime256v1', 'EC_secp384r1', 'RSA_2048', 'RSA_4096', 'SM2']
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['SHA256WITHECDSA', 'SHA256WITHRSA', 'SHA384WITHECDSA', 'SHA384WITHRSA', 'SHA512WITHECDSA', 'SHA512WITHRSA', 'SM3WITHSM2']
- **Required**: Yes

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectOutputTypeDef'>
- **Required**: Yes

### CsrExtensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.CsrExtensionsOutputTypeDef]


# CertificateAuthorityConfigurationTypeDef

### KeyAlgorithm
- **Type**: typing.Literal['EC_prime256v1', 'EC_secp384r1', 'RSA_2048', 'RSA_4096', 'SM2']
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['SHA256WITHECDSA', 'SHA256WITHRSA', 'SHA384WITHECDSA', 'SHA384WITHRSA', 'SHA512WITHECDSA', 'SHA512WITHRSA', 'SM3WITHSM2']
- **Required**: Yes

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectTypeDef'>
- **Required**: Yes

### CsrExtensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.CsrExtensionsTypeDef]


# CertificateAuthorityConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateAuthorityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCertificateAuthorityAuditReportRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### AuditReportResponseFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# CreateCertificateAuthorityAuditReportResponseTypeDef

### AuditReportId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCertificateAuthorityRequestTypeDef

### CertificateAuthorityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.CertificateAuthorityConfigurationUnionTypeDef'>
- **Required**: Yes

### CertificateAuthorityType
- **Type**: typing.Literal['ROOT', 'SUBORDINATE']
- **Required**: Yes

### RevocationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.RevocationConfigurationTypeDef]

### IdempotencyToken
- **Type**: typing.Optional[str]

### KeyStorageSecurityStandard
- **Type**: typing.Optional[typing.Literal['CCPC_LEVEL_1_OR_HIGHER', 'FIPS_140_2_LEVEL_2_OR_HIGHER', 'FIPS_140_2_LEVEL_3_OR_HIGHER']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.TagTypeDef]]

### UsageMode
- **Type**: typing.Optional[typing.Literal['GENERAL_PURPOSE', 'SHORT_LIVED_CERTIFICATE']]


# CreateCertificateAuthorityResponseTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePermissionRequestTypeDef

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


# CrlConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.CrlDistributionPointExtensionConfigurationTypeDef]

### CrlType
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'PARTITIONED']]

### CustomPath
- **Type**: typing.Optional[str]


# CrlDistributionPointExtensionConfigurationTypeDef

### OmitExtension
- **Type**: <class 'bool'>
- **Required**: Yes


# CsrExtensionsOutputTypeDef

### KeyUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.KeyUsageTypeDef]

### SubjectInformationAccess
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.AccessDescriptionOutputTypeDef]]


# CsrExtensionsTypeDef

### KeyUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.KeyUsageTypeDef]

### SubjectInformationAccess
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.AccessDescriptionTypeDef]]


# CustomAttributeTypeDef

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# CustomExtensionTypeDef

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# DeleteCertificateAuthorityRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermanentDeletionTimeInDays
- **Type**: typing.Optional[int]


# DeletePermissionRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### SourceAccount
- **Type**: typing.Optional[str]


# DeletePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateAuthorityAuditReportRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuditReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateAuthorityAuditReportRequestWaitTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuditReportId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.WaiterConfigTypeDef]


# DescribeCertificateAuthorityAuditReportResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCertificateAuthorityRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateAuthorityResponseTypeDef

### CertificateAuthority
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.CertificateAuthorityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EdiPartyNameTypeDef

### PartyName
- **Type**: <class 'str'>
- **Required**: Yes

### NameAssigner
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExtendedKeyUsageTypeDef

### ExtendedKeyUsageType
- **Type**: typing.Optional[typing.Literal['CERTIFICATE_TRANSPARENCY', 'CLIENT_AUTH', 'CODE_SIGNING', 'DOCUMENT_SIGNING', 'EMAIL_PROTECTION', 'OCSP_SIGNING', 'SERVER_AUTH', 'SMART_CARD_LOGIN', 'TIME_STAMPING']]

### ExtendedKeyUsageObjectIdentifier
- **Type**: typing.Optional[str]


# ExtensionsTypeDef

### CertificatePolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.PolicyInformationTypeDef]]

### ExtendedKeyUsage
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.ExtendedKeyUsageTypeDef]]

### KeyUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.KeyUsageTypeDef]

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.GeneralNameUnionTypeDef]]

### CustomExtensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.CustomExtensionTypeDef]]


# GeneralNameOutputTypeDef

### OtherName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.OtherNameTypeDef]

### Rfc822Name
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### DirectoryName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectOutputTypeDef]

### EdiPartyName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.EdiPartyNameTypeDef]

### UniformResourceIdentifier
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### RegisteredId
- **Type**: typing.Optional[str]


# GeneralNameTypeDef

### OtherName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.OtherNameTypeDef]

### Rfc822Name
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### DirectoryName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ASN1SubjectUnionTypeDef]

### EdiPartyName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.EdiPartyNameTypeDef]

### UniformResourceIdentifier
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### RegisteredId
- **Type**: typing.Optional[str]


# GeneralNameUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetCertificateAuthorityCertificateRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateAuthorityCertificateResponseTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCertificateAuthorityCsrRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateAuthorityCsrRequestWaitTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.WaiterConfigTypeDef]


# GetCertificateAuthorityCsrResponseTypeDef

### Csr
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCertificateRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCertificateRequestWaitTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.WaiterConfigTypeDef]


# GetCertificateResponseTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportCertificateAuthorityCertificateRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.BlobTypeDef'>
- **Required**: Yes

### CertificateChain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.BlobTypeDef]


# IssueCertificateRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Csr
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.BlobTypeDef'>
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['SHA256WITHECDSA', 'SHA256WITHRSA', 'SHA384WITHECDSA', 'SHA384WITHRSA', 'SHA512WITHECDSA', 'SHA512WITHRSA', 'SM3WITHSM2']
- **Required**: Yes

### Validity
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ValidityTypeDef'>
- **Required**: Yes

### ApiPassthrough
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ApiPassthroughTypeDef]

### TemplateArn
- **Type**: typing.Optional[str]

### ValidityNotBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.ValidityTypeDef]

### IdempotencyToken
- **Type**: typing.Optional[str]


# IssueCertificateResponseTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KeyUsageTypeDef

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


# ListCertificateAuthoritiesRequestPaginateTypeDef

### ResourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.PaginatorConfigTypeDef]


# ListCertificateAuthoritiesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]


# ListCertificateAuthoritiesResponseTypeDef

### CertificateAuthorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.CertificateAuthorityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequestPaginateTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.PaginatorConfigTypeDef]


# ListPermissionsRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionsResponseTypeDef

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.PermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestPaginateTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.PaginatorConfigTypeDef]


# ListTagsRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.acm_pca_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OcspConfigurationTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OcspCustomCname
- **Type**: typing.Optional[str]


# OtherNameTypeDef

### TypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionTypeDef

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


# PolicyInformationTypeDef

### CertPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyQualifiers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.PolicyQualifierInfoTypeDef]]


# PolicyQualifierInfoTypeDef

### PolicyQualifierId
- **Type**: typing.Literal['CPS']
- **Required**: Yes

### Qualifier
- **Type**: <class 'aws_resource_validator.pydantic_models.acm_pca_classes.QualifierTypeDef'>
- **Required**: Yes


# PutPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# QualifierTypeDef

### CpsUri
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


# RestoreCertificateAuthorityRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes


# RevocationConfigurationTypeDef

### CrlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.CrlConfigurationTypeDef]

### OcspConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.OcspConfigurationTypeDef]


# RevokeCertificateRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateSerial
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationReason
- **Type**: typing.Literal['AFFILIATION_CHANGED', 'A_A_COMPROMISE', 'CERTIFICATE_AUTHORITY_COMPROMISE', 'CESSATION_OF_OPERATION', 'KEY_COMPROMISE', 'PRIVILEGE_WITHDRAWN', 'SUPERSEDED', 'UNSPECIFIED']
- **Required**: Yes


# TagCertificateAuthorityRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# UntagCertificateAuthorityRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.acm_pca_classes.TagTypeDef]
- **Required**: Yes


# UpdateCertificateAuthorityRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.acm_pca_classes.RevocationConfigurationTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DISABLED', 'EXPIRED', 'FAILED', 'PENDING_CERTIFICATE']]


# ValidityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


