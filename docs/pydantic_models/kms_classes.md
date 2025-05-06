# Kms Classes

# AliasListEntry

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

# CancelKeyDeletionRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelKeyDeletionResponse

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ConnectCustomKeyStoreRequest

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAliasRequest

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomKeyStoreRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.XksProxyAuthenticationCredentialType]

### XksProxyConnectivity
- **Type**: typing.Optional[typing.Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE']]


# CreateCustomKeyStoreResponse

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGrantRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteePrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.List[typing.Literal['CreateGrant', 'Decrypt', 'DeriveSharedSecret', 'DescribeKey', 'Encrypt', 'GenerateDataKey', 'GenerateDataKeyPair', 'GenerateDataKeyPairWithoutPlaintext', 'GenerateDataKeyWithoutPlaintext', 'GenerateMac', 'GetPublicKey', 'ReEncryptFrom', 'ReEncryptTo', 'RetireGrant', 'Sign', 'Verify', 'VerifyMac']]
- **Required**: Yes

### RetiringPrincipal
- **Type**: typing.Optional[str]

### Constraints
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kms.kms_classes.GrantConstraints, aws_resource_validator.pydantic_models.kms.kms_classes.GrantConstraintsOutput, NoneType]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]

### DryRun
- **Type**: typing.Optional[bool]


# CreateGrantResponse

### GrantToken
- **Type**: <class 'str'>
- **Required**: Yes

### GrantId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeyRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.Tag]]

### MultiRegion
- **Type**: typing.Optional[bool]

### XksKeyId
- **Type**: typing.Optional[str]


# CreateKeyResponse

### KeyMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.KeyMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# CustomKeyStoresListEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.XksProxyConfigurationType]


# DecryptRequest

### CiphertextBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### KeyId
- **Type**: typing.Optional[str]

### EncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.RecipientInfo]

### DryRun
- **Type**: typing.Optional[bool]


# DecryptResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAliasRequest

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomKeyStoreRequest

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportedKeyMaterialRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeriveSharedSecretRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyAgreementAlgorithm
- **Type**: typing.Literal['ECDH']
- **Required**: Yes

### PublicKey
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.RecipientInfo]


# DeriveSharedSecretResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomKeyStoresRequest

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### CustomKeyStoreName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCustomKeyStoresRequestPaginate

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### CustomKeyStoreName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# DescribeCustomKeyStoresResponse

### CustomKeyStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.CustomKeyStoresListEntry]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeKeyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]


# DescribeKeyResponse

### KeyMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.KeyMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# DisableKeyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableKeyRotationRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DisconnectCustomKeyStoreRequest

### CustomKeyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# EnableKeyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableKeyRotationRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationPeriodInDays
- **Type**: typing.Optional[int]


# EncryptRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Plaintext
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### EncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### DryRun
- **Type**: typing.Optional[bool]


# EncryptResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateDataKeyPairRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPairSpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.RecipientInfo]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyPairResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateDataKeyPairWithoutPlaintextRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPairSpec
- **Type**: typing.Literal['ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyPairWithoutPlaintextResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateDataKeyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### NumberOfBytes
- **Type**: typing.Optional[int]

### KeySpec
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_256']]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.RecipientInfo]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateDataKeyWithoutPlaintextRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### KeySpec
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_256']]

### NumberOfBytes
- **Type**: typing.Optional[int]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateDataKeyWithoutPlaintextResponse

### CiphertextBlob
- **Type**: <class 'bytes'>
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateMacRequest

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### MacAlgorithm
- **Type**: typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# GenerateMacResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateRandomRequest

### NumberOfBytes
- **Type**: typing.Optional[int]

### CustomKeyStoreId
- **Type**: typing.Optional[str]

### Recipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.RecipientInfo]


# GenerateRandomResponse

### Plaintext
- **Type**: <class 'bytes'>
- **Required**: Yes

### CiphertextForRecipient
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyPolicyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: typing.Optional[str]


# GetKeyPolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyRotationStatusRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyRotationStatusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GetParametersForImportRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingAlgorithm
- **Type**: typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'RSAES_PKCS1_V1_5', 'RSA_AES_KEY_WRAP_SHA_1', 'RSA_AES_KEY_WRAP_SHA_256', 'SM2PKE']
- **Required**: Yes

### WrappingKeySpec
- **Type**: typing.Literal['RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
- **Required**: Yes


# GetParametersForImportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicKeyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]


# GetPublicKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# GrantConstraints

### EncryptionContextSubset
- **Type**: typing.Optional[typing.Dict[str, str]]

### EncryptionContextEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# GrantConstraintsOutput

### EncryptionContextSubset
- **Type**: typing.Optional[typing.Dict[str, str]]

### EncryptionContextEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# GrantListEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.GrantConstraintsOutput]


# ImportKeyMaterialRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportToken
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### EncryptedKeyMaterial
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### ValidTo
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ExpirationModel
- **Type**: typing.Optional[typing.Literal['KEY_MATERIAL_DOES_NOT_EXPIRE', 'KEY_MATERIAL_EXPIRES']]


# KeyListEntry

### KeyId
- **Type**: typing.Optional[str]

### KeyArn
- **Type**: typing.Optional[str]


# KeyMetadata

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
- **Type**: <class 'NoneType'>

### PendingDeletionWindowInDays
- **Type**: typing.Optional[int]

### MacAlgorithms
- **Type**: typing.Optional[typing.List[typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']]]

### XksKeyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.XksKeyConfigurationType]


# ListAliasesRequest

### KeyId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListAliasesRequestPaginate

### KeyId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# ListAliasesResponse

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.AliasListEntry]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ListGrantsRequest

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


# ListGrantsRequestPaginate

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantId
- **Type**: typing.Optional[str]

### GranteePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# ListGrantsResponse

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.GrantListEntry]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ListKeyPoliciesRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListKeyPoliciesRequestPaginate

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# ListKeyPoliciesResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ListKeyRotationsRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListKeyRotationsRequestPaginate

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# ListKeyRotationsResponse

### Rotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.RotationsListEntry]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ListKeysRequest

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListKeysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# ListKeysResponse

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.KeyListEntry]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ListResourceTagsRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListResourceTagsRequestPaginate

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# ListResourceTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.Tag]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# ListRetirableGrantsRequest

### RetiringPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListRetirableGrantsRequestPaginate

### RetiringPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.PaginatorConfig]


# MultiRegionConfiguration

### MultiRegionKeyType
- **Type**: typing.Optional[typing.Literal['PRIMARY', 'REPLICA']]

### PrimaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.MultiRegionKey]

### ReplicaKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.MultiRegionKey]]


# MultiRegionKey

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutKeyPolicyRequest

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


# ReEncryptRequest

### CiphertextBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### DestinationKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### SourceKeyId
- **Type**: typing.Optional[str]

### DestinationEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### SourceEncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### DestinationEncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE', 'SYMMETRIC_DEFAULT']]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# ReEncryptResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# RecipientInfo

### KeyEncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['RSAES_OAEP_SHA_256']]

### AttestationDocument
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# ReplicateKeyRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.Tag]]


# ReplicateKeyResponse

### ReplicaKeyMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.KeyMetadata'>
- **Required**: Yes

### ReplicaPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicaTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
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


# RetireGrantRequest

### GrantToken
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]

### GrantId
- **Type**: typing.Optional[str]

### DryRun
- **Type**: typing.Optional[bool]


# RevokeGrantRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantId
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# RotateKeyOnDemandRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# RotateKeyOnDemandResponse

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# RotationsListEntry

### KeyId
- **Type**: typing.Optional[str]

### RotationDate
- **Type**: typing.Optional[datetime.datetime]

### RotationType
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'ON_DEMAND']]


# ScheduleKeyDeletionRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PendingWindowInDays
- **Type**: typing.Optional[int]


# ScheduleKeyDeletionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# SignRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['DIGEST', 'RAW']]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# SignResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kms.kms_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAliasRequest

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCustomKeyStoreRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kms.kms_classes.XksProxyAuthenticationCredentialType]

### XksProxyConnectivity
- **Type**: typing.Optional[typing.Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE']]


# UpdateKeyDescriptionRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePrimaryRegionRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyMacRequest

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### MacAlgorithm
- **Type**: typing.Literal['HMAC_SHA_224', 'HMAC_SHA_256', 'HMAC_SHA_384', 'HMAC_SHA_512']
- **Required**: Yes

### Mac
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# VerifyMacResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyRequest

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### Signature
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### SigningAlgorithm
- **Type**: typing.Literal['ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'SM2DSA']
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['DIGEST', 'RAW']]

### GrantTokens
- **Type**: typing.Optional[typing.List[str]]

### DryRun
- **Type**: typing.Optional[bool]


# VerifyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kms.kms_classes.ResponseMetadata'>
- **Required**: Yes


# XksKeyConfigurationType

### Id
- **Type**: typing.Optional[str]


# XksProxyAuthenticationCredentialType

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RawSecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes


# XksProxyConfigurationType

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


