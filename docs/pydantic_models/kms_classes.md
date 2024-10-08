# Pydantic Models in kms_classes

# AliasListEntryTypeDef

### AliasName
- **Type**: typing.Optional[str]

### AliasArn
- **Type**: typing.Optional[str]

### TargetKeyId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelKeyDeletionRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelKeyDeletionResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectCustomKeyStoreRequestRequestTypeDef

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAliasRequestRequestTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomKeyStoreRequestRequestTypeDef

### CustomKeyStoreName
- **Type**: <class 'str'>
- **Required**: Yes

### CloudHsmClusterId
- **Type**: typing.Optional[str]

### TrustAnchorCertificate
- **Type**: typing.Optional[str]

### KeyStorePassword
- **Type**: typing.Optional[str]

### CustomKeyStoreType
- **Type**: typing.Optional[typing.Literal['AWS_CLOUDHSM', 'EXTERNAL_KEY_STORE']]

### XksProxyUriEndpoint
- **Type**: typing.Optional[str]

### XksProxyUriPath
- **Type**: typing.Optional[str]

### XksProxyVpcEndpointServiceName
- **Type**: typing.Optional[str]

### XksProxyAuthenticationCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.XksProxyAuthenticationCredentialTypeTypeDef]

### XksProxyConnectivity
- **Type**: typing.Optional[typing.Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE']]


# CreateCustomKeyStoreResponseTypeDef

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGrantRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteePrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.Sequence[typing.Literal['CreateGrant', 'Decrypt', 'DeriveSharedSecret', 'DescribeKey', 'Encrypt', 'GenerateDataKey', 'GenerateDataKeyPair', 'GenerateDataKeyPairWithoutPlaintext', 'GenerateDataKeyWithoutPlaintext', 'GenerateMac', 'GetPublicKey', 'ReEncryptFrom', 'ReEncryptTo', 'RetireGrant', 'Sign', 'Verify', 'VerifyMac']]
- **Required**: Yes

### RetiringPrincipal
- **Type**: typing.Optional[str]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.GrantConstraintsTypeDef]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### Name
- **Type**: typing.Optional[str]

### DryRun
- **Type**: typing.Optional[bool]


# CreateGrantResponseTypeDef

### GrantToken
- **Type**: <class 'str'>
- **Required**: Yes

### GrantId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeyRequestRequestTypeDef

### Policy
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KeyUsage
- **Type**: typing.Optional[typing.Literal['ENCRYPT_DECRYPT', 'GENERATE_VERIFY_MAC', 'KEY_AGREEMENT', 'SIGN_VERIFY']]

### CustomerMasterKeySpec
- **Type**: typing.Optional[typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2', 'SYMMETRIC_DEFAULT']]

### KeySpec
- **Type**: typing.Optional[typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2', 'SYMMETRIC_DEFAULT']]

### Origin
- **Type**: typing.Optional[typing.Literal['AWS_CLOUDHSM', 'AWS_KMS', 'EXTERNAL', 'EXTERNAL_KEY_STORE']]

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### BypassPolicyLockoutSafetyCheck
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kms_classes.TagTypeDef]]

### MultiRegion
- **Type**: typing.Optional[bool]

### XksKeyId
- **Type**: typing.Optional[str]


# CreateKeyResponseTypeDef

### KeyMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.KeyMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomKeyStoresListEntryTypeDef

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### CustomKeyStoreName
- **Type**: typing.Optional[str]

### CloudHsmClusterId
- **Type**: typing.Optional[str]

### TrustAnchorCertificate
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'CONNECTING', 'DISCONNECTED', 'DISCONNECTING', 'FAILED']]

### ConnectionErrorCode
- **Type**: typing.Optional[typing.Literal['CLUSTER_NOT_FOUND', 'INSUFFICIENT_CLOUDHSM_HSMS', 'INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET', 'INTERNAL_ERROR', 'INVALID_CREDENTIALS', 'NETWORK_ERRORS', 'SUBNET_NOT_FOUND', 'USER_LOCKED_OUT', 'USER_LOGGED_IN', 'USER_NOT_FOUND', 'XKS_PROXY_ACCESS_DENIED', 'XKS_PROXY_INVALID_CONFIGURATION', 'XKS_PROXY_INVALID_RESPONSE', 'XKS_PROXY_INVALID_TLS_CONFIGURATION', 'XKS_PROXY_NOT_REACHABLE', 'XKS_PROXY_TIMED_OUT', 'XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION', 'XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CustomKeyStoreType
- **Type**: typing.Optional[typing.Literal['AWS_CLOUDHSM', 'EXTERNAL_KEY_STORE']]

### XksProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.XksProxyConfigurationTypeTypeDef]


# DecryptRequestRequestTypeDef

### CiphertextBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### KeyId
- **Type**: typing.Optional[str]

### EncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.RecipientInfoTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# DecryptResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Plaintext
- **Type**: <class 'bytes'>
- **Required**: Yes

### EncryptionAlgorithm
- **Type**: typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']
- **Required**: Yes

### CiphertextForRecipient
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAliasRequestRequestTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomKeyStoreRequestRequestTypeDef

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportedKeyMaterialRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeriveSharedSecretRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyAgreementAlgorithm
- **Type**: typing.Literal['ECDH']
- **Required**: Yes

### PublicKey
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.RecipientInfoTypeDef]


# DeriveSharedSecretResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedSecret
- **Type**: <class 'bytes'>
- **Required**: Yes

### CiphertextForRecipient
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyAgreementAlgorithm
- **Type**: typing.Literal['ECDH']
- **Required**: Yes

### KeyOrigin
- **Type**: typing.Literal['AWS_CLOUDHSM', 'AWS_KMS', 'EXTERNAL', 'EXTERNAL_KEY_STORE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateTypeDef

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### CustomKeyStoreName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# DescribeCustomKeyStoresRequestRequestTypeDef

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### CustomKeyStoreName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCustomKeyStoresResponseTypeDef

### CustomKeyStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.CustomKeyStoresListEntryTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeKeyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeKeyResponseTypeDef

### KeyMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.KeyMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableKeyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableKeyRotationRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DisconnectCustomKeyStoreRequestRequestTypeDef

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableKeyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableKeyRotationRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationPeriodInDays
- **Type**: typing.Optional[int]


# EncryptRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Plaintext
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### EncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### DryRun
- **Type**: typing.Optional[bool]


# EncryptResponseTypeDef

### CiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionAlgorithm
- **Type**: typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateDataKeyPairRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPairSpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.RecipientInfoTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyPairResponseTypeDef

### PrivateKeyCiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### PrivateKeyPlaintext
- **Type**: <class 'bytes'>
- **Required**: Yes

### PublicKey
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPairSpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes

### CiphertextForRecipient
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPairSpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyPairWithoutPlaintextResponseTypeDef

### PrivateKeyCiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### PublicKey
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPairSpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateDataKeyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NumberOfBytes
- **Type**: typing.Optional[int]

### KeySpec
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_256']]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.RecipientInfoTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyResponseTypeDef

### CiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### Plaintext
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### CiphertextForRecipient
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateDataKeyWithoutPlaintextRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KeySpec
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_256']]

### NumberOfBytes
- **Type**: typing.Optional[int]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyWithoutPlaintextResponseTypeDef

### CiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateMacRequestRequestTypeDef

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### MacAlgorithm
- **Type**: typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateMacResponseTypeDef

### Mac
- **Type**: <class 'bytes'>
- **Required**: Yes

### MacAlgorithm
- **Type**: typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateRandomRequestRequestTypeDef

### NumberOfBytes
- **Type**: typing.Optional[int]

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.RecipientInfoTypeDef]


# GenerateRandomResponseTypeDef

### Plaintext
- **Type**: <class 'bytes'>
- **Required**: Yes

### CiphertextForRecipient
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyPolicyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: typing.Optional[str]


# GetKeyPolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyRotationStatusRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyRotationStatusResponseTypeDef

### KeyRotationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes

### NextRotationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OnDemandRotationStartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetParametersForImportRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingAlgorithm
- **Type**: typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'RSAES_PKCS1_V1_5', 'RSA_AES_KEY_WRAP_SHA_1', 'RSA_AES_KEY_WRAP_SHA_256', 'SM2PKE']
- **Required**: Yes

### WrappingKeySpec
- **Type**: typing.Literal['RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes


# GetParametersForImportResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportToken
- **Type**: <class 'bytes'>
- **Required**: Yes

### PublicKey
- **Type**: <class 'bytes'>
- **Required**: Yes

### ParametersValidTo
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicKeyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]


# GetPublicKeyResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PublicKey
- **Type**: <class 'bytes'>
- **Required**: Yes

### CustomerMasterKeySpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2', 'SYMMETRIC_DEFAULT']
- **Required**: Yes

### KeySpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2', 'SYMMETRIC_DEFAULT']
- **Required**: Yes

### KeyUsage
- **Type**: typing.Literal['ENCRYPT_DECRYPT', 'GENERATE_VERIFY_MAC', 'KEY_AGREEMENT', 'SIGN_VERIFY']
- **Required**: Yes

### EncryptionAlgorithms
- **Type**: typing.List[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]
- **Required**: Yes

### SigningAlgorithms
- **Type**: typing.List[typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']]
- **Required**: Yes

### KeyAgreementAlgorithms
- **Type**: typing.List[typing.Literal['ECDH']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrantConstraintsExtraOutputTypeDef

### EncryptionContextSubset
- **Type**: typing.Optional[typing.Dict[str, str]]

### EncryptionContextEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# GrantConstraintsOutputTypeDef

### EncryptionContextSubset
- **Type**: typing.Optional[typing.Dict[str, str]]

### EncryptionContextEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# GrantConstraintsTypeDef

### EncryptionContextSubset
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EncryptionContextEquals
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GrantListEntryTypeDef

### KeyId
- **Type**: typing.Optional[str]

### GrantId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### GranteePrincipal
- **Type**: typing.Optional[str]

### RetiringPrincipal
- **Type**: typing.Optional[str]

### IssuingAccount
- **Type**: typing.Optional[str]

### Operations
- **Type**: typing.Optional[typing.List[typing.Literal['CreateGrant', 'Decrypt', 'DeriveSharedSecret', 'DescribeKey', 'Encrypt', 'GenerateDataKey', 'GenerateDataKeyPair', 'GenerateDataKeyPairWithoutPlaintext', 'GenerateDataKeyWithoutPlaintext', 'GenerateMac', 'GetPublicKey', 'ReEncryptFrom', 'ReEncryptTo', 'RetireGrant', 'Sign', 'Verify', 'VerifyMac']]]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.GrantConstraintsOutputTypeDef]


# ImportKeyMaterialRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportToken
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### EncryptedKeyMaterial
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### ValidTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ExpirationModel
- **Type**: typing.Optional[typing.Literal['KEY_MATERIAL_DOES_NOT_EXPIRE', 'KEY_MATERIAL_EXPIRES']]


# KeyListEntryTypeDef

### KeyId
- **Type**: typing.Optional[str]

### KeyArn
- **Type**: typing.Optional[str]


# KeyMetadataTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Enabled
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### KeyUsage
- **Type**: typing.Optional[typing.Literal['ENCRYPT_DECRYPT', 'GENERATE_VERIFY_MAC', 'KEY_AGREEMENT', 'SIGN_VERIFY']]

### KeyState
- **Type**: typing.Optional[typing.Literal['Creating', 'Disabled', 'Enabled', 'PendingDeletion', 'PendingImport', 'PendingReplicaDeletion', 'Unavailable', 'Updating']]

### DeletionDate
- **Type**: typing.Optional[datetime.datetime]

### ValidTo
- **Type**: typing.Optional[datetime.datetime]

### Origin
- **Type**: typing.Optional[typing.Literal['AWS_CLOUDHSM', 'AWS_KMS', 'EXTERNAL', 'EXTERNAL_KEY_STORE']]

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### CloudHsmClusterId
- **Type**: typing.Optional[str]

### ExpirationModel
- **Type**: typing.Optional[typing.Literal['KEY_MATERIAL_DOES_NOT_EXPIRE', 'KEY_MATERIAL_EXPIRES']]

### KeyManager
- **Type**: typing.Optional[typing.Literal['AWS', 'CUSTOMER']]

### CustomerMasterKeySpec
- **Type**: typing.Optional[typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2', 'SYMMETRIC_DEFAULT']]

### KeySpec
- **Type**: typing.Optional[typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2', 'SYMMETRIC_DEFAULT']]

### EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]]

### SigningAlgorithms
- **Type**: typing.Optional[typing.List[typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']]]

### KeyAgreementAlgorithms
- **Type**: typing.Optional[typing.List[typing.Literal['ECDH']]]

### MultiRegion
- **Type**: typing.Optional[bool]

### MultiRegionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.MultiRegionConfigurationTypeDef]

### PendingDeletionWindowInDays
- **Type**: typing.Optional[int]

### MacAlgorithms
- **Type**: typing.Optional[typing.List[typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']]]

### XksKeyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.XksKeyConfigurationTypeTypeDef]


# ListAliasesRequestListAliasesPaginateTypeDef

### KeyId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListAliasesRequestRequestTypeDef

### KeyId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListAliasesResponseTypeDef

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.AliasListEntryTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGrantsRequestListGrantsPaginateTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantId
- **Type**: typing.Optional[str]

### GranteePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListGrantsRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### GrantId
- **Type**: typing.Optional[str]

### GranteePrincipal
- **Type**: typing.Optional[str]


# ListGrantsResponseTypeDef

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.GrantListEntryTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeyPoliciesRequestListKeyPoliciesPaginateTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListKeyPoliciesRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListKeyPoliciesResponseTypeDef

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeyRotationsRequestListKeyRotationsPaginateTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListKeyRotationsRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListKeyRotationsResponseTypeDef

### Rotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.RotationsListEntryTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeysRequestListKeysPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListKeysRequestRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListKeysResponseTypeDef

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.KeyListEntryTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceTagsRequestListResourceTagsPaginateTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListResourceTagsRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListResourceTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.TagTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRetirableGrantsRequestListRetirableGrantsPaginateTypeDef

### RetiringPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.PaginatorConfigTypeDef]


# ListRetirableGrantsRequestRequestTypeDef

### RetiringPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# MultiRegionConfigurationTypeDef

### MultiRegionKeyType
- **Type**: typing.Optional[typing.Literal['PRIMARY', 'REPLICA']]

### PrimaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.MultiRegionKeyTypeDef]

### ReplicaKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kms_classes.MultiRegionKeyTypeDef]]


# MultiRegionKeyTypeDef

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutKeyPolicyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: typing.Optional[str]

### BypassPolicyLockoutSafetyCheck
- **Type**: typing.Optional[bool]


# ReEncryptRequestRequestTypeDef

### CiphertextBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### DestinationKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SourceKeyId
- **Type**: typing.Optional[str]

### DestinationEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SourceEncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### DestinationEncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# ReEncryptResponseTypeDef

### CiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### SourceKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEncryptionAlgorithm
- **Type**: typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']
- **Required**: Yes

### DestinationEncryptionAlgorithm
- **Type**: typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecipientInfoTypeDef

### KeyEncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_256']]

### AttestationDocument
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# ReplicateKeyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: typing.Optional[str]

### BypassPolicyLockoutSafetyCheck
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kms_classes.TagTypeDef]]


# ReplicateKeyResponseTypeDef

### ReplicaKeyMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.KeyMetadataTypeDef'>
- **Required**: Yes

### ReplicaPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicaTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
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


# RetireGrantRequestRequestTypeDef

### GrantToken
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]

### GrantId
- **Type**: typing.Optional[str]

### DryRun
- **Type**: typing.Optional[bool]


# RevokeGrantRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantId
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# RotateKeyOnDemandRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# RotateKeyOnDemandResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RotationsListEntryTypeDef

### KeyId
- **Type**: typing.Optional[str]

### RotationDate
- **Type**: typing.Optional[datetime.datetime]

### RotationType
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'ON_DEMAND']]


# ScheduleKeyDeletionRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PendingWindowInDays
- **Type**: typing.Optional[int]


# ScheduleKeyDeletionResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KeyState
- **Type**: typing.Literal['Creating', 'Disabled', 'Enabled', 'PendingDeletion', 'PendingImport', 'PendingReplicaDeletion', 'Unavailable', 'Updating']
- **Required**: Yes

### PendingWindowInDays
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SignRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['DIGEST', 'RAW']]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# SignResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Signature
- **Type**: <class 'bytes'>
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kms_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAliasRequestRequestTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCustomKeyStoreRequestRequestTypeDef

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### NewCustomKeyStoreName
- **Type**: typing.Optional[str]

### KeyStorePassword
- **Type**: typing.Optional[str]

### CloudHsmClusterId
- **Type**: typing.Optional[str]

### XksProxyUriEndpoint
- **Type**: typing.Optional[str]

### XksProxyUriPath
- **Type**: typing.Optional[str]

### XksProxyVpcEndpointServiceName
- **Type**: typing.Optional[str]

### XksProxyAuthenticationCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms_classes.XksProxyAuthenticationCredentialTypeTypeDef]

### XksProxyConnectivity
- **Type**: typing.Optional[typing.Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE']]


# UpdateKeyDescriptionRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePrimaryRegionRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyMacRequestRequestTypeDef

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### MacAlgorithm
- **Type**: typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
- **Required**: Yes

### Mac
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# VerifyMacResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### MacValid
- **Type**: <class 'bool'>
- **Required**: Yes

### MacAlgorithm
- **Type**: typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyRequestRequestTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### Signature
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['DIGEST', 'RAW']]

### GrantTokens
- **Type**: typing.Optional[typing.Sequence[str]]

### DryRun
- **Type**: typing.Optional[bool]


# VerifyResponseTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SignatureValid
- **Type**: <class 'bool'>
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# XksKeyConfigurationTypeTypeDef

### Id
- **Type**: typing.Optional[str]


# XksProxyAuthenticationCredentialTypeTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RawSecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes


# XksProxyConfigurationTypeTypeDef

### Connectivity
- **Type**: typing.Optional[typing.Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE']]

### AccessKeyId
- **Type**: typing.Optional[str]

### UriEndpoint
- **Type**: typing.Optional[str]

### UriPath
- **Type**: typing.Optional[str]

### VpcEndpointServiceName
- **Type**: typing.Optional[str]


