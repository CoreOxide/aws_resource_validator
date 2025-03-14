# Pca Connector Ad Classes

# AccessControlEntrySummaryTypeDef

### AccessRights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.AccessRightsTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### GroupDisplayName
- **Type**: typing.Optional[str]

### GroupSecurityIdentifier
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# AccessControlEntryTypeDef

### AccessRights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.AccessRightsTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### GroupDisplayName
- **Type**: typing.Optional[str]

### GroupSecurityIdentifier
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# AccessRightsTypeDef

### AutoEnroll
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### Enroll
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# ApplicationPoliciesOutputTypeDef

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPolicyTypeDef]
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# ApplicationPoliciesTypeDef

### Policies
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPolicyTypeDef]
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# ApplicationPolicyTypeDef

### PolicyObjectIdentifier
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[typing.Literal['ALL_APPLICATION_POLICIES', 'ANY_PURPOSE', 'ATTESTATION_IDENTITY_KEY_CERTIFICATE', 'CERTIFICATE_REQUEST_AGENT', 'CLIENT_AUTHENTICATION', 'CODE_SIGNING', 'CTL_USAGE', 'DIGITAL_RIGHTS', 'DIRECTORY_SERVICE_EMAIL_REPLICATION', 'DISALLOWED_LIST', 'DNS_SERVER_TRUST', 'DOCUMENT_ENCRYPTION', 'DOCUMENT_SIGNING', 'DYNAMIC_CODE_GENERATOR', 'EARLY_LAUNCH_ANTIMALWARE_DRIVER', 'EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION', 'ENCLAVE', 'ENCRYPTING_FILE_SYSTEM', 'ENDORSEMENT_KEY_CERTIFICATE', 'FILE_RECOVERY', 'HAL_EXTENSION', 'IP_SECURITY_END_SYSTEM', 'IP_SECURITY_IKE_INTERMEDIATE', 'IP_SECURITY_TUNNEL_TERMINATION', 'IP_SECURITY_USER', 'ISOLATED_USER_MODE', 'KDC_AUTHENTICATION', 'KERNEL_MODE_CODE_SIGNING', 'KEY_PACK_LICENSES', 'KEY_RECOVERY', 'KEY_RECOVERY_AGENT', 'LICENSE_SERVER_VERIFICATION', 'LIFETIME_SIGNING', 'MICROSOFT_PUBLISHER', 'MICROSOFT_TIME_STAMPING', 'MICROSOFT_TRUST_LIST_SIGNING', 'OCSP_SIGNING', 'OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION', 'PLATFORM_CERTIFICATE', 'PREVIEW_BUILD_SIGNING', 'PRIVATE_KEY_ARCHIVAL', 'PROTECTED_PROCESS_LIGHT_VERIFICATION', 'PROTECTED_PROCESS_VERIFICATION', 'QUALIFIED_SUBORDINATION', 'REVOKED_LIST_SIGNER', 'ROOT_LIST_SIGNER', 'ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION', 'ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION', 'ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL', 'SECURE_EMAIL', 'SERVER_AUTHENTICATION', 'SMART_CARD_LOGIN', 'SPC_ENCRYPTED_DIGEST_RETRY_COUNT', 'SPC_RELAXED_PE_MARKER_CHECK', 'TIME_STAMPING', 'WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION', 'WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION', 'WINDOWS_HARDWARE_DRIVER_VERIFICATION', 'WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION', 'WINDOWS_KITS_COMPONENT', 'WINDOWS_RT_VERIFICATION', 'WINDOWS_SOFTWARE_EXTENSION_VERIFICATION', 'WINDOWS_STORE', 'WINDOWS_SYSTEM_COMPONENT_VERIFICATION', 'WINDOWS_TCB_COMPONENT', 'WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT', 'WINDOWS_UPDATE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateValidityTypeDef

### RenewalPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ValidityPeriodTypeDef'>
- **Required**: Yes

### ValidityPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ValidityPeriodTypeDef'>
- **Required**: Yes


# ConnectorSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CertificateEnrollmentPolicyServerEndpoint
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DirectoryId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['CA_CERTIFICATE_REGISTRATION_FAILED', 'DIRECTORY_ACCESS_DENIED', 'INSUFFICIENT_FREE_ADDRESSES', 'INTERNAL_FAILURE', 'INVALID_SUBNET_IP_PROTOCOL', 'PRIVATECA_ACCESS_DENIED', 'PRIVATECA_RESOURCE_NOT_FOUND', 'SECURITY_GROUP_NOT_IN_VPC', 'VPC_ACCESS_DENIED', 'VPC_ENDPOINT_LIMIT_EXCEEDED', 'VPC_RESOURCE_NOT_FOUND']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### VpcInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.VpcInformationOutputTypeDef]


# ConnectorTypeDef

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CertificateEnrollmentPolicyServerEndpoint
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DirectoryId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['CA_CERTIFICATE_REGISTRATION_FAILED', 'DIRECTORY_ACCESS_DENIED', 'INSUFFICIENT_FREE_ADDRESSES', 'INTERNAL_FAILURE', 'INVALID_SUBNET_IP_PROTOCOL', 'PRIVATECA_ACCESS_DENIED', 'PRIVATECA_RESOURCE_NOT_FOUND', 'SECURITY_GROUP_NOT_IN_VPC', 'VPC_ACCESS_DENIED', 'VPC_ENDPOINT_LIMIT_EXCEEDED', 'VPC_RESOURCE_NOT_FOUND']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### VpcInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.VpcInformationOutputTypeDef]


# CreateConnectorRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.VpcInformationUnionTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConnectorResponseTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDirectoryRegistrationRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDirectoryRegistrationResponseTypeDef

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServicePrincipalNameRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateTemplateGroupAccessControlEntryRequestTypeDef

### AccessRights
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.AccessRightsTypeDef'>
- **Required**: Yes

### GroupDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateTemplateRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateDefinitionUnionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTemplateResponseTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConnectorRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryRegistrationRequestTypeDef

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServicePrincipalNameRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateGroupAccessControlEntryRequestTypeDef

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DirectoryRegistrationSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DirectoryId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['DIRECTORY_ACCESS_DENIED', 'DIRECTORY_NOT_ACTIVE', 'DIRECTORY_NOT_REACHABLE', 'DIRECTORY_RESOURCE_NOT_FOUND', 'DIRECTORY_TYPE_NOT_SUPPORTED', 'INTERNAL_FAILURE']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# DirectoryRegistrationTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DirectoryId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['DIRECTORY_ACCESS_DENIED', 'DIRECTORY_NOT_ACTIVE', 'DIRECTORY_NOT_REACHABLE', 'DIRECTORY_RESOURCE_NOT_FOUND', 'DIRECTORY_TYPE_NOT_SUPPORTED', 'INTERNAL_FAILURE']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnrollmentFlagsV2TypeDef

### EnableKeyReuseOnNtTokenKeysetStorageFull
- **Type**: typing.Optional[bool]

### IncludeSymmetricAlgorithms
- **Type**: typing.Optional[bool]

### NoSecurityExtension
- **Type**: typing.Optional[bool]

### RemoveInvalidCertificateFromPersonalStore
- **Type**: typing.Optional[bool]

### UserInteractionRequired
- **Type**: typing.Optional[bool]


# EnrollmentFlagsV3TypeDef

### EnableKeyReuseOnNtTokenKeysetStorageFull
- **Type**: typing.Optional[bool]

### IncludeSymmetricAlgorithms
- **Type**: typing.Optional[bool]

### NoSecurityExtension
- **Type**: typing.Optional[bool]

### RemoveInvalidCertificateFromPersonalStore
- **Type**: typing.Optional[bool]

### UserInteractionRequired
- **Type**: typing.Optional[bool]


# EnrollmentFlagsV4TypeDef

### EnableKeyReuseOnNtTokenKeysetStorageFull
- **Type**: typing.Optional[bool]

### IncludeSymmetricAlgorithms
- **Type**: typing.Optional[bool]

### NoSecurityExtension
- **Type**: typing.Optional[bool]

### RemoveInvalidCertificateFromPersonalStore
- **Type**: typing.Optional[bool]

### UserInteractionRequired
- **Type**: typing.Optional[bool]


# ExtensionsV2OutputTypeDef

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageTypeDef'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPoliciesOutputTypeDef]


# ExtensionsV2TypeDef

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageTypeDef'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPoliciesTypeDef]


# ExtensionsV3OutputTypeDef

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageTypeDef'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPoliciesOutputTypeDef]


# ExtensionsV3TypeDef

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageTypeDef'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPoliciesTypeDef]


# ExtensionsV4OutputTypeDef

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageTypeDef'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPoliciesOutputTypeDef]


# ExtensionsV4TypeDef

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageTypeDef'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ApplicationPoliciesTypeDef]


# GeneralFlagsV2TypeDef

### AutoEnrollment
- **Type**: typing.Optional[bool]

### MachineType
- **Type**: typing.Optional[bool]


# GeneralFlagsV3TypeDef

### AutoEnrollment
- **Type**: typing.Optional[bool]

### MachineType
- **Type**: typing.Optional[bool]


# GeneralFlagsV4TypeDef

### AutoEnrollment
- **Type**: typing.Optional[bool]

### MachineType
- **Type**: typing.Optional[bool]


# GetConnectorRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectorResponseTypeDef

### Connector
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDirectoryRegistrationRequestTypeDef

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectoryRegistrationResponseTypeDef

### DirectoryRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.DirectoryRegistrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServicePrincipalNameRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetServicePrincipalNameResponseTypeDef

### ServicePrincipalName
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ServicePrincipalNameTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateGroupAccessControlEntryRequestTypeDef

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateGroupAccessControlEntryResponseTypeDef

### AccessControlEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.AccessControlEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateResponseTypeDef

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KeyUsageFlagsTypeDef

### DataEncipherment
- **Type**: typing.Optional[bool]

### DigitalSignature
- **Type**: typing.Optional[bool]

### KeyAgreement
- **Type**: typing.Optional[bool]

### KeyEncipherment
- **Type**: typing.Optional[bool]

### NonRepudiation
- **Type**: typing.Optional[bool]


# KeyUsagePropertyFlagsTypeDef

### Decrypt
- **Type**: typing.Optional[bool]

### KeyAgreement
- **Type**: typing.Optional[bool]

### Sign
- **Type**: typing.Optional[bool]


# KeyUsagePropertyTypeDef

### PropertyFlags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsagePropertyFlagsTypeDef]

### PropertyType
- **Type**: typing.Optional[typing.Literal['ALL']]


# KeyUsageTypeDef

### UsageFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsageFlagsTypeDef'>
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# ListConnectorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.PaginatorConfigTypeDef]


# ListConnectorsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponseTypeDef

### Connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ConnectorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDirectoryRegistrationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.PaginatorConfigTypeDef]


# ListDirectoryRegistrationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDirectoryRegistrationsResponseTypeDef

### DirectoryRegistrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad_classes.DirectoryRegistrationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicePrincipalNamesRequestPaginateTypeDef

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.PaginatorConfigTypeDef]


# ListServicePrincipalNamesRequestTypeDef

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServicePrincipalNamesResponseTypeDef

### ServicePrincipalNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad_classes.ServicePrincipalNameSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.PaginatorConfigTypeDef]


# ListTemplateGroupAccessControlEntriesRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTemplateGroupAccessControlEntriesResponseTypeDef

### AccessControlEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad_classes.AccessControlEntrySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequestPaginateTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.PaginatorConfigTypeDef]


# ListTemplatesRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesResponseTypeDef

### Templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ResponseMetadataTypeDef'>
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


# PrivateKeyAttributesV2OutputTypeDef

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]


# PrivateKeyAttributesV2TypeDef

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.Sequence[str]]


# PrivateKeyAttributesV3OutputTypeDef

### Algorithm
- **Type**: typing.Literal['ECDH_P256', 'ECDH_P384', 'ECDH_P521', 'RSA']
- **Required**: Yes

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### KeyUsageProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsagePropertyTypeDef'>
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]


# PrivateKeyAttributesV3TypeDef

### Algorithm
- **Type**: typing.Literal['ECDH_P256', 'ECDH_P384', 'ECDH_P521', 'RSA']
- **Required**: Yes

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### KeyUsageProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsagePropertyTypeDef'>
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.Sequence[str]]


# PrivateKeyAttributesV4OutputTypeDef

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### Algorithm
- **Type**: typing.Optional[typing.Literal['ECDH_P256', 'ECDH_P384', 'ECDH_P521', 'RSA']]

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]

### KeyUsageProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsagePropertyTypeDef]


# PrivateKeyAttributesV4TypeDef

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### Algorithm
- **Type**: typing.Optional[typing.Literal['ECDH_P256', 'ECDH_P384', 'ECDH_P521', 'RSA']]

### CryptoProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### KeyUsageProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.KeyUsagePropertyTypeDef]


# PrivateKeyFlagsV2TypeDef

### ClientVersion
- **Type**: typing.Literal['WINDOWS_SERVER_2003', 'WINDOWS_SERVER_2008', 'WINDOWS_SERVER_2008_R2', 'WINDOWS_SERVER_2012', 'WINDOWS_SERVER_2012_R2', 'WINDOWS_SERVER_2016']
- **Required**: Yes

### ExportableKey
- **Type**: typing.Optional[bool]

### StrongKeyProtectionRequired
- **Type**: typing.Optional[bool]


# PrivateKeyFlagsV3TypeDef

### ClientVersion
- **Type**: typing.Literal['WINDOWS_SERVER_2008', 'WINDOWS_SERVER_2008_R2', 'WINDOWS_SERVER_2012', 'WINDOWS_SERVER_2012_R2', 'WINDOWS_SERVER_2016']
- **Required**: Yes

### ExportableKey
- **Type**: typing.Optional[bool]

### RequireAlternateSignatureAlgorithm
- **Type**: typing.Optional[bool]

### StrongKeyProtectionRequired
- **Type**: typing.Optional[bool]


# PrivateKeyFlagsV4TypeDef

### ClientVersion
- **Type**: typing.Literal['WINDOWS_SERVER_2012', 'WINDOWS_SERVER_2012_R2', 'WINDOWS_SERVER_2016']
- **Required**: Yes

### ExportableKey
- **Type**: typing.Optional[bool]

### RequireAlternateSignatureAlgorithm
- **Type**: typing.Optional[bool]

### RequireSameKeyRenewal
- **Type**: typing.Optional[bool]

### StrongKeyProtectionRequired
- **Type**: typing.Optional[bool]

### UseLegacyProvider
- **Type**: typing.Optional[bool]


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


# ServicePrincipalNameSummaryTypeDef

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DirectoryRegistrationArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['DIRECTORY_ACCESS_DENIED', 'DIRECTORY_NOT_REACHABLE', 'DIRECTORY_RESOURCE_NOT_FOUND', 'INTERNAL_FAILURE', 'SPN_EXISTS_ON_DIFFERENT_AD_OBJECT', 'SPN_LIMIT_EXCEEDED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ServicePrincipalNameTypeDef

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DirectoryRegistrationArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['DIRECTORY_ACCESS_DENIED', 'DIRECTORY_NOT_REACHABLE', 'DIRECTORY_RESOURCE_NOT_FOUND', 'INTERNAL_FAILURE', 'SPN_EXISTS_ON_DIFFERENT_AD_OBJECT', 'SPN_LIMIT_EXCEEDED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# SubjectNameFlagsV2TypeDef

### RequireCommonName
- **Type**: typing.Optional[bool]

### RequireDirectoryPath
- **Type**: typing.Optional[bool]

### RequireDnsAsCn
- **Type**: typing.Optional[bool]

### RequireEmail
- **Type**: typing.Optional[bool]

### SanRequireDirectoryGuid
- **Type**: typing.Optional[bool]

### SanRequireDns
- **Type**: typing.Optional[bool]

### SanRequireDomainDns
- **Type**: typing.Optional[bool]

### SanRequireEmail
- **Type**: typing.Optional[bool]

### SanRequireSpn
- **Type**: typing.Optional[bool]

### SanRequireUpn
- **Type**: typing.Optional[bool]


# SubjectNameFlagsV3TypeDef

### RequireCommonName
- **Type**: typing.Optional[bool]

### RequireDirectoryPath
- **Type**: typing.Optional[bool]

### RequireDnsAsCn
- **Type**: typing.Optional[bool]

### RequireEmail
- **Type**: typing.Optional[bool]

### SanRequireDirectoryGuid
- **Type**: typing.Optional[bool]

### SanRequireDns
- **Type**: typing.Optional[bool]

### SanRequireDomainDns
- **Type**: typing.Optional[bool]

### SanRequireEmail
- **Type**: typing.Optional[bool]

### SanRequireSpn
- **Type**: typing.Optional[bool]

### SanRequireUpn
- **Type**: typing.Optional[bool]


# SubjectNameFlagsV4TypeDef

### RequireCommonName
- **Type**: typing.Optional[bool]

### RequireDirectoryPath
- **Type**: typing.Optional[bool]

### RequireDnsAsCn
- **Type**: typing.Optional[bool]

### RequireEmail
- **Type**: typing.Optional[bool]

### SanRequireDirectoryGuid
- **Type**: typing.Optional[bool]

### SanRequireDns
- **Type**: typing.Optional[bool]

### SanRequireDomainDns
- **Type**: typing.Optional[bool]

### SanRequireEmail
- **Type**: typing.Optional[bool]

### SanRequireSpn
- **Type**: typing.Optional[bool]

### SanRequireUpn
- **Type**: typing.Optional[bool]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateDefinitionOutputTypeDef

### TemplateV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateV2OutputTypeDef]

### TemplateV3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateV3OutputTypeDef]

### TemplateV4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateV4OutputTypeDef]


# TemplateDefinitionTypeDef

### TemplateV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateV2TypeDef]

### TemplateV3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateV3TypeDef]

### TemplateV4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateV4TypeDef]


# TemplateDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateRevisionTypeDef

### MajorRevision
- **Type**: <class 'int'>
- **Required**: Yes

### MinorRevision
- **Type**: <class 'int'>
- **Required**: Yes


# TemplateSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateDefinitionOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### ObjectIdentifier
- **Type**: typing.Optional[str]

### PolicySchema
- **Type**: typing.Optional[int]

### Revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateRevisionTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TemplateTypeDef

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateDefinitionOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### ObjectIdentifier
- **Type**: typing.Optional[str]

### PolicySchema
- **Type**: typing.Optional[int]

### Revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateRevisionTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TemplateV2OutputTypeDef

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.CertificateValidityTypeDef'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.EnrollmentFlagsV2TypeDef'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ExtensionsV2OutputTypeDef'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.GeneralFlagsV2TypeDef'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyAttributesV2OutputTypeDef'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyFlagsV2TypeDef'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.SubjectNameFlagsV2TypeDef'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV2TypeDef

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.CertificateValidityTypeDef'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.EnrollmentFlagsV2TypeDef'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ExtensionsV2TypeDef'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.GeneralFlagsV2TypeDef'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyAttributesV2TypeDef'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyFlagsV2TypeDef'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.SubjectNameFlagsV2TypeDef'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.Sequence[str]]


# TemplateV3OutputTypeDef

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.CertificateValidityTypeDef'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.EnrollmentFlagsV3TypeDef'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ExtensionsV3OutputTypeDef'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.GeneralFlagsV3TypeDef'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Literal['SHA256', 'SHA384', 'SHA512']
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyAttributesV3OutputTypeDef'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyFlagsV3TypeDef'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.SubjectNameFlagsV3TypeDef'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV3TypeDef

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.CertificateValidityTypeDef'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.EnrollmentFlagsV3TypeDef'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ExtensionsV3TypeDef'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.GeneralFlagsV3TypeDef'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Literal['SHA256', 'SHA384', 'SHA512']
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyAttributesV3TypeDef'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyFlagsV3TypeDef'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.SubjectNameFlagsV3TypeDef'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.Sequence[str]]


# TemplateV4OutputTypeDef

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.CertificateValidityTypeDef'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.EnrollmentFlagsV4TypeDef'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ExtensionsV4OutputTypeDef'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.GeneralFlagsV4TypeDef'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyAttributesV4OutputTypeDef'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyFlagsV4TypeDef'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.SubjectNameFlagsV4TypeDef'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA256', 'SHA384', 'SHA512']]

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV4TypeDef

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.CertificateValidityTypeDef'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.EnrollmentFlagsV4TypeDef'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.ExtensionsV4TypeDef'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.GeneralFlagsV4TypeDef'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyAttributesV4TypeDef'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.PrivateKeyFlagsV4TypeDef'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad_classes.SubjectNameFlagsV4TypeDef'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA256', 'SHA384', 'SHA512']]

### SupersededTemplates
- **Type**: typing.Optional[typing.Sequence[str]]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateTemplateGroupAccessControlEntryRequestTypeDef

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccessRights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.AccessRightsTypeDef]

### GroupDisplayName
- **Type**: typing.Optional[str]


# UpdateTemplateRequestTypeDef

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad_classes.TemplateDefinitionUnionTypeDef]

### ReenrollAllCertificateHolders
- **Type**: typing.Optional[bool]


# ValidityPeriodTypeDef

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### PeriodType
- **Type**: typing.Literal['DAYS', 'HOURS', 'MONTHS', 'WEEKS', 'YEARS']
- **Required**: Yes


# VpcInformationOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4']]


# VpcInformationTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4']]


# VpcInformationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

