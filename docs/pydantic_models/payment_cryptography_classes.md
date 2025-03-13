# Payment Cryptography Classes

# AliasTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAliasInputTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# CreateAliasOutputTypeDef

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.AliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeyInputTypeDef

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyAttributesTypeDef'>
- **Required**: Yes

### Exportable
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.payment_cryptography_classes.TagTypeDef]]


# CreateKeyOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAliasInputTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteKeyInDays
- **Type**: typing.Optional[int]


# DeleteKeyOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportAttributesTypeDef

### ExportDukptInitialKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ExportDukptInitialKeyTypeDef]

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]


# ExportDukptInitialKeyTypeDef

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes


# ExportKeyCryptogramTypeDef

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingSpec
- **Type**: typing.Optional[typing.Literal['RSA_OAEP_SHA_256', 'RSA_OAEP_SHA_512']]


# ExportKeyInputTypeDef

### KeyMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ExportKeyMaterialTypeDef'>
- **Required**: Yes

### ExportKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ExportAttributesTypeDef]


# ExportKeyMaterialTypeDef

### Tr31KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ExportTr31KeyBlockTypeDef]

### Tr34KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ExportTr34KeyBlockTypeDef]

### KeyCryptogram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ExportKeyCryptogramTypeDef]


# ExportKeyOutputTypeDef

### WrappedKey
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.WrappedKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportTr31KeyBlockTypeDef

### WrappingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### KeyBlockHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyBlockHeadersTypeDef]


# ExportTr34KeyBlockTypeDef

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### ExportToken
- **Type**: <class 'str'>
- **Required**: Yes

### KeyBlockFormat
- **Type**: typing.Literal['X9_TR34_2012']
- **Required**: Yes

### RandomNonce
- **Type**: typing.Optional[str]

### KeyBlockHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyBlockHeadersTypeDef]


# GetAliasInputTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAliasOutputTypeDef

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.AliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetParametersForExportInputTypeDef

### KeyMaterialType
- **Type**: typing.Literal['KEY_CRYPTOGRAM', 'ROOT_PUBLIC_KEY_CERTIFICATE', 'TR31_KEY_BLOCK', 'TR34_KEY_BLOCK', 'TRUSTED_PUBLIC_KEY_CERTIFICATE']
- **Required**: Yes

### SigningKeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes


# GetParametersForExportOutputTypeDef

### SigningKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### SigningKeyCertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### SigningKeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes

### ExportToken
- **Type**: <class 'str'>
- **Required**: Yes

### ParametersValidUntilTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetParametersForImportInputTypeDef

### KeyMaterialType
- **Type**: typing.Literal['KEY_CRYPTOGRAM', 'ROOT_PUBLIC_KEY_CERTIFICATE', 'TR31_KEY_BLOCK', 'TR34_KEY_BLOCK', 'TRUSTED_PUBLIC_KEY_CERTIFICATE']
- **Required**: Yes

### WrappingKeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes


# GetParametersForImportOutputTypeDef

### WrappingKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingKeyCertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingKeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes

### ImportToken
- **Type**: <class 'str'>
- **Required**: Yes

### ParametersValidUntilTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicKeyCertificateInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyCertificateOutputTypeDef

### KeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportKeyCryptogramTypeDef

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyAttributesTypeDef'>
- **Required**: Yes

### Exportable
- **Type**: <class 'bool'>
- **Required**: Yes

### WrappedKeyCryptogram
- **Type**: <class 'str'>
- **Required**: Yes

### ImportToken
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingSpec
- **Type**: typing.Optional[typing.Literal['RSA_OAEP_SHA_256', 'RSA_OAEP_SHA_512']]


# ImportKeyInputTypeDef

### KeyMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ImportKeyMaterialTypeDef'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.payment_cryptography_classes.TagTypeDef]]


# ImportKeyMaterialTypeDef

### RootCertificatePublicKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.RootCertificatePublicKeyTypeDef]

### TrustedCertificatePublicKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.TrustedCertificatePublicKeyTypeDef]

### Tr31KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ImportTr31KeyBlockTypeDef]

### Tr34KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ImportTr34KeyBlockTypeDef]

### KeyCryptogram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.ImportKeyCryptogramTypeDef]


# ImportKeyOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportTr31KeyBlockTypeDef

### WrappingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WrappedKeyBlock
- **Type**: <class 'str'>
- **Required**: Yes


# ImportTr34KeyBlockTypeDef

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SigningKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### ImportToken
- **Type**: <class 'str'>
- **Required**: Yes

### WrappedKeyBlock
- **Type**: <class 'str'>
- **Required**: Yes

### KeyBlockFormat
- **Type**: typing.Literal['X9_TR34_2012']
- **Required**: Yes

### RandomNonce
- **Type**: typing.Optional[str]


# KeyAttributesTypeDef

### KeyUsage
- **Type**: typing.Literal['TR31_B0_BASE_DERIVATION_KEY', 'TR31_C0_CARD_VERIFICATION_KEY', 'TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY', 'TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION', 'TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS', 'TR31_E1_EMV_MKEY_CONFIDENTIALITY', 'TR31_E2_EMV_MKEY_INTEGRITY', 'TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS', 'TR31_E5_EMV_MKEY_CARD_PERSONALIZATION', 'TR31_E6_EMV_MKEY_OTHER', 'TR31_K0_KEY_ENCRYPTION_KEY', 'TR31_K1_KEY_BLOCK_PROTECTION_KEY', 'TR31_K2_TR34_ASYMMETRIC_KEY', 'TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT', 'TR31_M1_ISO_9797_1_MAC_KEY', 'TR31_M3_ISO_9797_3_MAC_KEY', 'TR31_M6_ISO_9797_5_CMAC_KEY', 'TR31_M7_HMAC_KEY', 'TR31_P0_PIN_ENCRYPTION_KEY', 'TR31_P1_PIN_GENERATION_KEY', 'TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE', 'TR31_V1_IBM3624_PIN_VERIFICATION_KEY', 'TR31_V2_VISA_PIN_VERIFICATION_KEY']
- **Required**: Yes

### KeyClass
- **Type**: typing.Literal['ASYMMETRIC_KEY_PAIR', 'PRIVATE_KEY', 'PUBLIC_KEY', 'SYMMETRIC_KEY']
- **Required**: Yes

### KeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes

### KeyModesOfUse
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyModesOfUseTypeDef'>
- **Required**: Yes


# KeyBlockHeadersTypeDef

### KeyModesOfUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyModesOfUseTypeDef]

### KeyExportability
- **Type**: typing.Optional[typing.Literal['EXPORTABLE', 'NON_EXPORTABLE', 'SENSITIVE']]

### KeyVersion
- **Type**: typing.Optional[str]

### OptionalBlocks
- **Type**: typing.Optional[typing.Mapping[str, str]]


# KeyModesOfUseTypeDef

### Encrypt
- **Type**: typing.Optional[bool]

### Decrypt
- **Type**: typing.Optional[bool]

### Wrap
- **Type**: typing.Optional[bool]

### Unwrap
- **Type**: typing.Optional[bool]

### Generate
- **Type**: typing.Optional[bool]

### Sign
- **Type**: typing.Optional[bool]

### Verify
- **Type**: typing.Optional[bool]

### DeriveKey
- **Type**: typing.Optional[bool]

### NoRestrictions
- **Type**: typing.Optional[bool]


# KeySummaryTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyState
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']
- **Required**: Yes

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyAttributesTypeDef'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### Exportable
- **Type**: <class 'bool'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# KeyTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyAttributesTypeDef'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Literal['ANSI_X9_24', 'CMAC']
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Exportable
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyState
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']
- **Required**: Yes

### KeyOrigin
- **Type**: typing.Literal['AWS_PAYMENT_CRYPTOGRAPHY', 'EXTERNAL']
- **Required**: Yes

### CreateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UsageStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UsageStopTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DeletePendingTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DeleteTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ListAliasesInputPaginateTypeDef

### KeyArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.PaginatorConfigTypeDef]


# ListAliasesInputTypeDef

### KeyArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAliasesOutputTypeDef

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography_classes.AliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeysInputPaginateTypeDef

### KeyState
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.PaginatorConfigTypeDef]


# ListKeysInputTypeDef

### KeyState
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListKeysOutputTypeDef

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography_classes.KeySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
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


# RestoreKeyInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreKeyOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RootCertificatePublicKeyTypeDef

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyAttributesTypeDef'>
- **Required**: Yes

### PublicKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes


# StartKeyUsageInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartKeyUsageOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopKeyUsageInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopKeyUsageOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.payment_cryptography_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TrustedCertificatePublicKeyTypeDef

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.KeyAttributesTypeDef'>
- **Required**: Yes

### PublicKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAliasInputTypeDef

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# UpdateAliasOutputTypeDef

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.AliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WrappedKeyTypeDef

### WrappingKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### WrappedKeyMaterialFormat
- **Type**: typing.Literal['KEY_CRYPTOGRAM', 'TR31_KEY_BLOCK', 'TR34_KEY_BLOCK']
- **Required**: Yes

### KeyMaterial
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: typing.Optional[str]

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]


