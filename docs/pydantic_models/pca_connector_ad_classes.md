# Pca Connector Ad Classes

# AccessControlEntry

### AccessRights
- **Type**: <class 'NoneType'>

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


# AccessControlEntrySummary

### AccessRights
- **Type**: <class 'NoneType'>

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


# AccessRights

### AutoEnroll
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### Enroll
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# ApplicationPolicies

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ApplicationPolicy]
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# ApplicationPoliciesOutput

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ApplicationPolicy]
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# ApplicationPolicy

### PolicyObjectIdentifier
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[typing.Literal['ALL_APPLICATION_POLICIES', 'ANY_PURPOSE', 'ATTESTATION_IDENTITY_KEY_CERTIFICATE', 'CERTIFICATE_REQUEST_AGENT', 'CLIENT_AUTHENTICATION', 'CODE_SIGNING', 'CTL_USAGE', 'DIGITAL_RIGHTS', 'DIRECTORY_SERVICE_EMAIL_REPLICATION', 'DISALLOWED_LIST', 'DNS_SERVER_TRUST', 'DOCUMENT_ENCRYPTION', 'DOCUMENT_SIGNING', 'DYNAMIC_CODE_GENERATOR', 'EARLY_LAUNCH_ANTIMALWARE_DRIVER', 'EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION', 'ENCLAVE', 'ENCRYPTING_FILE_SYSTEM', 'ENDORSEMENT_KEY_CERTIFICATE', 'FILE_RECOVERY', 'HAL_EXTENSION', 'IP_SECURITY_END_SYSTEM', 'IP_SECURITY_IKE_INTERMEDIATE', 'IP_SECURITY_TUNNEL_TERMINATION', 'IP_SECURITY_USER', 'ISOLATED_USER_MODE', 'KDC_AUTHENTICATION', 'KERNEL_MODE_CODE_SIGNING', 'KEY_PACK_LICENSES', 'KEY_RECOVERY', 'KEY_RECOVERY_AGENT', 'LICENSE_SERVER_VERIFICATION', 'LIFETIME_SIGNING', 'MICROSOFT_PUBLISHER', 'MICROSOFT_TIME_STAMPING', 'MICROSOFT_TRUST_LIST_SIGNING', 'OCSP_SIGNING', 'OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION', 'PLATFORM_CERTIFICATE', 'PREVIEW_BUILD_SIGNING', 'PRIVATE_KEY_ARCHIVAL', 'PROTECTED_PROCESS_LIGHT_VERIFICATION', 'PROTECTED_PROCESS_VERIFICATION', 'QUALIFIED_SUBORDINATION', 'REVOKED_LIST_SIGNER', 'ROOT_LIST_SIGNER', 'ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION', 'ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION', 'ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL', 'SECURE_EMAIL', 'SERVER_AUTHENTICATION', 'SMART_CARD_LOGIN', 'SPC_ENCRYPTED_DIGEST_RETRY_COUNT', 'SPC_RELAXED_PE_MARKER_CHECK', 'TIME_STAMPING', 'WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION', 'WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION', 'WINDOWS_HARDWARE_DRIVER_VERIFICATION', 'WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION', 'WINDOWS_KITS_COMPONENT', 'WINDOWS_RT_VERIFICATION', 'WINDOWS_SOFTWARE_EXTENSION_VERIFICATION', 'WINDOWS_STORE', 'WINDOWS_SYSTEM_COMPONENT_VERIFICATION', 'WINDOWS_TCB_COMPONENT', 'WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT', 'WINDOWS_UPDATE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateValidity

### RenewalPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ValidityPeriod'>
- **Required**: Yes

### ValidityPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ValidityPeriod'>
- **Required**: Yes


# Connector

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.VpcInformationOutput]


# ConnectorSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.VpcInformationOutput]


# CreateConnectorRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInformation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.VpcInformation, aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.VpcInformationOutput]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectorResponse

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDirectoryRegistrationRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDirectoryRegistrationResponse

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServicePrincipalNameRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateTemplateGroupAccessControlEntryRequest

### AccessRights
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.AccessRights'>
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


# CreateTemplateRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateDefinition, aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateDefinitionOutput]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTemplateResponse

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConnectorRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryRegistrationRequest

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServicePrincipalNameRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateGroupAccessControlEntryRequest

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequest

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DirectoryRegistration

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


# DirectoryRegistrationSummary

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# EnrollmentFlagsV2

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


# EnrollmentFlagsV3

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


# EnrollmentFlagsV4

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


# ExtensionsV2

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsage'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: <class 'NoneType'>


# ExtensionsV2Output

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsage'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ApplicationPoliciesOutput]


# ExtensionsV3

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsage'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: <class 'NoneType'>


# ExtensionsV3Output

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsage'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ApplicationPoliciesOutput]


# ExtensionsV4

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsage'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: <class 'NoneType'>


# ExtensionsV4Output

### KeyUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsage'>
- **Required**: Yes

### ApplicationPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ApplicationPoliciesOutput]


# GeneralFlagsV2

### AutoEnrollment
- **Type**: typing.Optional[bool]

### MachineType
- **Type**: typing.Optional[bool]


# GeneralFlagsV3

### AutoEnrollment
- **Type**: typing.Optional[bool]

### MachineType
- **Type**: typing.Optional[bool]


# GeneralFlagsV4

### AutoEnrollment
- **Type**: typing.Optional[bool]

### MachineType
- **Type**: typing.Optional[bool]


# GetConnectorRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectorResponse

### Connector
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.Connector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# GetDirectoryRegistrationRequest

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectoryRegistrationResponse

### DirectoryRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.DirectoryRegistration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# GetServicePrincipalNameRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetServicePrincipalNameResponse

### ServicePrincipalName
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ServicePrincipalName'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateGroupAccessControlEntryRequest

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateGroupAccessControlEntryResponse

### AccessControlEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.AccessControlEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateRequest

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateResponse

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.Template'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# KeyUsage

### UsageFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsageFlags'>
- **Required**: Yes

### Critical
- **Type**: typing.Optional[bool]


# KeyUsageFlags

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


# KeyUsageProperty

### PropertyFlags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsagePropertyFlags]

### PropertyType
- **Type**: typing.Optional[typing.Literal['ALL']]


# KeyUsagePropertyFlags

### Decrypt
- **Type**: typing.Optional[bool]

### KeyAgreement
- **Type**: typing.Optional[bool]

### Sign
- **Type**: typing.Optional[bool]


# ListConnectorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PaginatorConfig]


# ListConnectorsResponse

### Connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ConnectorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDirectoryRegistrationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDirectoryRegistrationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PaginatorConfig]


# ListDirectoryRegistrationsResponse

### DirectoryRegistrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.DirectoryRegistrationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicePrincipalNamesRequest

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServicePrincipalNamesRequestPaginate

### DirectoryRegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PaginatorConfig]


# ListServicePrincipalNamesResponse

### ServicePrincipalNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ServicePrincipalNameSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplateGroupAccessControlEntriesRequest

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTemplateGroupAccessControlEntriesRequestPaginate

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PaginatorConfig]


# ListTemplateGroupAccessControlEntriesResponse

### AccessControlEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.AccessControlEntrySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequestPaginate

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PaginatorConfig]


# ListTemplatesResponse

### Templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ResponseMetadata'>
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


# PrivateKeyAttributesV2

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]


# PrivateKeyAttributesV2Output

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]


# PrivateKeyAttributesV3

### Algorithm
- **Type**: typing.Literal['ECDH_P256', 'ECDH_P384', 'ECDH_P521', 'RSA']
- **Required**: Yes

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### KeyUsageProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsageProperty'>
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]


# PrivateKeyAttributesV3Output

### Algorithm
- **Type**: typing.Literal['ECDH_P256', 'ECDH_P384', 'ECDH_P521', 'RSA']
- **Required**: Yes

### KeySpec
- **Type**: typing.Literal['KEY_EXCHANGE', 'SIGNATURE']
- **Required**: Yes

### KeyUsageProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.KeyUsageProperty'>
- **Required**: Yes

### MinimalKeyLength
- **Type**: <class 'int'>
- **Required**: Yes

### CryptoProviders
- **Type**: typing.Optional[typing.List[str]]


# PrivateKeyAttributesV4

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
- **Type**: <class 'NoneType'>


# PrivateKeyAttributesV4Output

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
- **Type**: <class 'NoneType'>


# PrivateKeyFlagsV2

### ClientVersion
- **Type**: typing.Literal['WINDOWS_SERVER_2003', 'WINDOWS_SERVER_2008', 'WINDOWS_SERVER_2008_R2', 'WINDOWS_SERVER_2012', 'WINDOWS_SERVER_2012_R2', 'WINDOWS_SERVER_2016']
- **Required**: Yes

### ExportableKey
- **Type**: typing.Optional[bool]

### StrongKeyProtectionRequired
- **Type**: typing.Optional[bool]


# PrivateKeyFlagsV3

### ClientVersion
- **Type**: typing.Literal['WINDOWS_SERVER_2008', 'WINDOWS_SERVER_2008_R2', 'WINDOWS_SERVER_2012', 'WINDOWS_SERVER_2012_R2', 'WINDOWS_SERVER_2016']
- **Required**: Yes

### ExportableKey
- **Type**: typing.Optional[bool]

### RequireAlternateSignatureAlgorithm
- **Type**: typing.Optional[bool]

### StrongKeyProtectionRequired
- **Type**: typing.Optional[bool]


# PrivateKeyFlagsV4

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


# ServicePrincipalName

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


# ServicePrincipalNameSummary

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


# SubjectNameFlagsV2

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


# SubjectNameFlagsV3

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


# SubjectNameFlagsV4

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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Template

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateDefinitionOutput]

### Name
- **Type**: typing.Optional[str]

### ObjectIdentifier
- **Type**: typing.Optional[str]

### PolicySchema
- **Type**: typing.Optional[int]

### Revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateRevision]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TemplateDefinition

### TemplateV2
- **Type**: <class 'NoneType'>

### TemplateV3
- **Type**: <class 'NoneType'>

### TemplateV4
- **Type**: <class 'NoneType'>


# TemplateDefinitionOutput

### TemplateV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateV2Output]

### TemplateV3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateV3Output]

### TemplateV4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateV4Output]


# TemplateRevision

### MajorRevision
- **Type**: <class 'int'>
- **Required**: Yes

### MinorRevision
- **Type**: <class 'int'>
- **Required**: Yes


# TemplateSummary

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateDefinitionOutput]

### Name
- **Type**: typing.Optional[str]

### ObjectIdentifier
- **Type**: typing.Optional[str]

### PolicySchema
- **Type**: typing.Optional[int]

### Revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateRevision]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TemplateV2

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.CertificateValidity'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.EnrollmentFlagsV2'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ExtensionsV2'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.GeneralFlagsV2'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyAttributesV2'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyFlagsV2'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.SubjectNameFlagsV2'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV2Output

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.CertificateValidity'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.EnrollmentFlagsV2'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ExtensionsV2Output'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.GeneralFlagsV2'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyAttributesV2Output'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyFlagsV2'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.SubjectNameFlagsV2'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV3

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.CertificateValidity'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.EnrollmentFlagsV3'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ExtensionsV3'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.GeneralFlagsV3'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Literal['SHA256', 'SHA384', 'SHA512']
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyAttributesV3'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyFlagsV3'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.SubjectNameFlagsV3'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV3Output

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.CertificateValidity'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.EnrollmentFlagsV3'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ExtensionsV3Output'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.GeneralFlagsV3'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Literal['SHA256', 'SHA384', 'SHA512']
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyAttributesV3Output'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyFlagsV3'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.SubjectNameFlagsV3'>
- **Required**: Yes

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV4

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.CertificateValidity'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.EnrollmentFlagsV4'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ExtensionsV4'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.GeneralFlagsV4'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyAttributesV4'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyFlagsV4'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.SubjectNameFlagsV4'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA256', 'SHA384', 'SHA512']]

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# TemplateV4Output

### CertificateValidity
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.CertificateValidity'>
- **Required**: Yes

### EnrollmentFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.EnrollmentFlagsV4'>
- **Required**: Yes

### Extensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.ExtensionsV4Output'>
- **Required**: Yes

### GeneralFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.GeneralFlagsV4'>
- **Required**: Yes

### PrivateKeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyAttributesV4Output'>
- **Required**: Yes

### PrivateKeyFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.PrivateKeyFlagsV4'>
- **Required**: Yes

### SubjectNameFlags
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.SubjectNameFlagsV4'>
- **Required**: Yes

### HashAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA256', 'SHA384', 'SHA512']]

### SupersededTemplates
- **Type**: typing.Optional[typing.List[str]]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateTemplateGroupAccessControlEntryRequest

### GroupSecurityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccessRights
- **Type**: <class 'NoneType'>

### GroupDisplayName
- **Type**: typing.Optional[str]


# UpdateTemplateRequest

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateDefinition, aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_classes.TemplateDefinitionOutput, NoneType]

### ReenrollAllCertificateHolders
- **Type**: typing.Optional[bool]


# ValidityPeriod

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### PeriodType
- **Type**: typing.Literal['DAYS', 'HOURS', 'MONTHS', 'WEEKS', 'YEARS']
- **Required**: Yes


# VpcInformation

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4']]


# VpcInformationOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4']]


