# Payment Cryptography Classes

# Alias

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAliasInput

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# CreateAliasOutput

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Alias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeyInput

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyAttributes'>
- **Required**: Yes

### Exportable
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Tag]]


# CreateKeyOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAliasInput

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteKeyInDays
- **Type**: typing.Optional[int]


# DeleteKeyOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# ExportAttributes

### ExportDukptInitialKey
- **Type**: <class 'NoneType'>

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]


# ExportDukptInitialKey

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes


# ExportKeyCryptogram

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### WrappingSpec
- **Type**: typing.Optional[typing.Literal['RSA_OAEP_SHA_256', 'RSA_OAEP_SHA_512']]


# ExportKeyInput

### KeyMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ExportKeyMaterial'>
- **Required**: Yes

### ExportKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportAttributes
- **Type**: <class 'NoneType'>


# ExportKeyMaterial

### Tr31KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ExportTr31KeyBlock]

### Tr34KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ExportTr34KeyBlock]

### KeyCryptogram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ExportKeyCryptogram]


# ExportKeyOutput

### WrappedKey
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.WrappedKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# ExportTr31KeyBlock

### WrappingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### KeyBlockHeaders
- **Type**: <class 'NoneType'>


# ExportTr34KeyBlock

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
- **Type**: <class 'NoneType'>


# GetAliasInput

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAliasOutput

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Alias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# GetParametersForExportInput

### KeyMaterialType
- **Type**: typing.Literal['KEY_CRYPTOGRAM', 'ROOT_PUBLIC_KEY_CERTIFICATE', 'TR31_KEY_BLOCK', 'TR34_KEY_BLOCK', 'TRUSTED_PUBLIC_KEY_CERTIFICATE']
- **Required**: Yes

### SigningKeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes


# GetParametersForExportOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# GetParametersForImportInput

### KeyMaterialType
- **Type**: typing.Literal['KEY_CRYPTOGRAM', 'ROOT_PUBLIC_KEY_CERTIFICATE', 'TR31_KEY_BLOCK', 'TR34_KEY_BLOCK', 'TRUSTED_PUBLIC_KEY_CERTIFICATE']
- **Required**: Yes

### WrappingKeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'ECC_NIST_P256', 'ECC_NIST_P384', 'RSA_2048', 'RSA_3072', 'RSA_4096', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes


# GetParametersForImportOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicKeyCertificateInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyCertificateOutput

### KeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCertificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# ImportKeyCryptogram

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyAttributes'>
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


# ImportKeyInput

### KeyMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ImportKeyMaterial'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Tag]]


# ImportKeyMaterial

### RootCertificatePublicKey
- **Type**: <class 'NoneType'>

### TrustedCertificatePublicKey
- **Type**: <class 'NoneType'>

### Tr31KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ImportTr31KeyBlock]

### Tr34KeyBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ImportTr34KeyBlock]

### KeyCryptogram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ImportKeyCryptogram]


# ImportKeyOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# ImportTr31KeyBlock

### WrappingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WrappedKeyBlock
- **Type**: <class 'str'>
- **Required**: Yes


# ImportTr34KeyBlock

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


# Key

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyAttributes'>
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


# KeyAttributes

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyModesOfUse'>
- **Required**: Yes


# KeyBlockHeaders

### KeyModesOfUse
- **Type**: <class 'NoneType'>

### KeyExportability
- **Type**: typing.Optional[typing.Literal['EXPORTABLE', 'NON_EXPORTABLE', 'SENSITIVE']]

### KeyVersion
- **Type**: typing.Optional[str]

### OptionalBlocks
- **Type**: typing.Optional[typing.Dict[str, str]]


# KeyModesOfUse

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


# KeySummary

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyState
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']
- **Required**: Yes

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyAttributes'>
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


# ListAliasesInput

### KeyArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAliasesInputPaginate

### KeyArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.PaginatorConfig]


# ListAliasesOutput

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Alias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeysInput

### KeyState
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListKeysInputPaginate

### KeyState
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_PENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.PaginatorConfig]


# ListKeysOutput

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceInputPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.PaginatorConfig]


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
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


# RestoreKeyInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreKeyOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# RootCertificatePublicKey

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyAttributes'>
- **Required**: Yes

### PublicKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes


# StartKeyUsageInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartKeyUsageOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# StopKeyUsageInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopKeyUsageOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Key'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Tag]
- **Required**: Yes


# TrustedCertificatePublicKey

### KeyAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.KeyAttributes'>
- **Required**: Yes

### PublicKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAliasInput

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# UpdateAliasOutput

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.Alias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_classes.ResponseMetadata'>
- **Required**: Yes


# WrappedKey

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


