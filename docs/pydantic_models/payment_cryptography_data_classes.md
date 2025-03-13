# Payment Cryptography Data Classes

# AmexAttributesTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationRequestKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentPinAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CurrentPinAttributesTypeDef]


# AmexCardSecurityCodeVersion1TypeDef

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes


# AmexCardSecurityCodeVersion2TypeDef

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes


# AsymmetricEncryptionAttributesTypeDef

### PaddingType
- **Type**: typing.Optional[typing.Literal['OAEP_SHA1', 'OAEP_SHA256', 'OAEP_SHA512', 'PKCS1']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CardGenerationAttributesTypeDef

### AmexCardSecurityCodeVersion1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.AmexCardSecurityCodeVersion1TypeDef]

### AmexCardSecurityCodeVersion2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.AmexCardSecurityCodeVersion2TypeDef]

### CardVerificationValue1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardVerificationValue1TypeDef]

### CardVerificationValue2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardVerificationValue2TypeDef]

### CardHolderVerificationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardHolderVerificationValueTypeDef]

### DynamicCardVerificationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DynamicCardVerificationCodeTypeDef]

### DynamicCardVerificationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DynamicCardVerificationValueTypeDef]


# CardHolderVerificationValueTypeDef

### UnpredictableNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# CardVerificationAttributesTypeDef

### AmexCardSecurityCodeVersion1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.AmexCardSecurityCodeVersion1TypeDef]

### AmexCardSecurityCodeVersion2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.AmexCardSecurityCodeVersion2TypeDef]

### CardVerificationValue1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardVerificationValue1TypeDef]

### CardVerificationValue2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardVerificationValue2TypeDef]

### CardHolderVerificationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardHolderVerificationValueTypeDef]

### DynamicCardVerificationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DynamicCardVerificationCodeTypeDef]

### DynamicCardVerificationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DynamicCardVerificationValueTypeDef]

### DiscoverDynamicCardVerificationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DiscoverDynamicCardVerificationCodeTypeDef]


# CardVerificationValue1TypeDef

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes


# CardVerificationValue2TypeDef

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes


# CryptogramAuthResponseTypeDef

### ArpcMethod1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CryptogramVerificationArpcMethod1TypeDef]

### ArpcMethod2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CryptogramVerificationArpcMethod2TypeDef]


# CryptogramVerificationArpcMethod1TypeDef

### AuthResponseCode
- **Type**: <class 'str'>
- **Required**: Yes


# CryptogramVerificationArpcMethod2TypeDef

### CardStatusUpdate
- **Type**: <class 'str'>
- **Required**: Yes

### ProprietaryAuthenticationData
- **Type**: typing.Optional[str]


# CurrentPinAttributesTypeDef

### CurrentPinPekIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentEncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes


# DecryptDataInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CipherText
- **Type**: <class 'str'>
- **Required**: Yes

### DecryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.EncryptionDecryptionAttributesTypeDef'>
- **Required**: Yes

### WrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]


# DecryptDataOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### PlainText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DerivationMethodAttributesTypeDef

### EmvCommon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.EmvCommonAttributesTypeDef]

### Amex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.AmexAttributesTypeDef]

### Visa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.VisaAttributesTypeDef]

### Emv2000
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.Emv2000AttributesTypeDef]

### Mastercard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MasterCardAttributesTypeDef]


# DiscoverDynamicCardVerificationCodeTypeDef

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### UnpredictableNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# DukptAttributesTypeDef

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### DukptDerivationType
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes


# DukptDerivationAttributesTypeDef

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### DukptKeyDerivationType
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']]

### DukptKeyVariant
- **Type**: typing.Optional[typing.Literal['BIDIRECTIONAL', 'REQUEST', 'RESPONSE']]


# DukptEncryptionAttributesTypeDef

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['CBC', 'ECB']]

### DukptKeyDerivationType
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']]

### DukptKeyVariant
- **Type**: typing.Optional[typing.Literal['BIDIRECTIONAL', 'REQUEST', 'RESPONSE']]

### InitializationVector
- **Type**: typing.Optional[str]


# DynamicCardVerificationCodeTypeDef

### UnpredictableNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes

### TrackData
- **Type**: <class 'str'>
- **Required**: Yes


# DynamicCardVerificationValueTypeDef

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# EcdhDerivationAttributesTypeDef

### CertificateAuthorityPublicKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PublicKeyCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### KeyAlgorithm
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes

### KeyDerivationFunction
- **Type**: typing.Literal['ANSI_X963', 'NIST_SP800']
- **Required**: Yes

### KeyDerivationHashAlgorithm
- **Type**: typing.Literal['SHA_256', 'SHA_384', 'SHA_512']
- **Required**: Yes

### SharedInformation
- **Type**: <class 'str'>
- **Required**: Yes


# Emv2000AttributesTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# EmvCommonAttributesTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationCryptogram
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Literal['CBC', 'ECB']
- **Required**: Yes

### PinBlockPaddingType
- **Type**: typing.Literal['ISO_IEC_7816_4', 'NO_PADDING']
- **Required**: Yes

### PinBlockLengthPosition
- **Type**: typing.Literal['FRONT_OF_PIN_BLOCK', 'NONE']
- **Required**: Yes


# EmvEncryptionAttributesTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### SessionDerivationData
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['CBC', 'ECB']]

### InitializationVector
- **Type**: typing.Optional[str]


# EncryptDataInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PlainText
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.EncryptionDecryptionAttributesTypeDef'>
- **Required**: Yes

### WrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]


# EncryptDataOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### CipherText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionDecryptionAttributesTypeDef

### Symmetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SymmetricEncryptionAttributesTypeDef]

### Asymmetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.AsymmetricEncryptionAttributesTypeDef]

### Dukpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DukptEncryptionAttributesTypeDef]

### Emv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.EmvEncryptionAttributesTypeDef]


# GenerateCardValidationDataInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardGenerationAttributesTypeDef'>
- **Required**: Yes

### ValidationDataLength
- **Type**: typing.Optional[int]


# GenerateCardValidationDataOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationData
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateMacEmvPinChangeInputTypeDef

### NewPinPekIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NewEncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### PinBlockFormat
- **Type**: typing.Literal['ISO_FORMAT_0', 'ISO_FORMAT_1', 'ISO_FORMAT_3']
- **Required**: Yes

### SecureMessagingIntegrityKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SecureMessagingConfidentialityKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MessageData
- **Type**: <class 'str'>
- **Required**: Yes

### DerivationMethodAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DerivationMethodAttributesTypeDef'>
- **Required**: Yes


# GenerateMacEmvPinChangeOutputTypeDef

### NewPinPekArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecureMessagingIntegrityKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecureMessagingConfidentialityKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Mac
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### NewPinPekKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### SecureMessagingIntegrityKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### SecureMessagingConfidentialityKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### VisaAmexDerivationOutputs
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.VisaAmexDerivationOutputsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateMacInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MessageData
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MacAttributesTypeDef'>
- **Required**: Yes

### MacLength
- **Type**: typing.Optional[int]


# GenerateMacOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### Mac
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GeneratePinDataInputTypeDef

### GenerationKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.PinGenerationAttributesTypeDef'>
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PinBlockFormat
- **Type**: typing.Literal['ISO_FORMAT_0', 'ISO_FORMAT_3', 'ISO_FORMAT_4']
- **Required**: Yes

### PinDataLength
- **Type**: typing.Optional[int]

### EncryptionWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]


# GeneratePinDataOutputTypeDef

### GenerationKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### PinData
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.PinDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# Ibm3624NaturalPinTypeDef

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# Ibm3624PinFromOffsetTypeDef

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes

### PinOffset
- **Type**: <class 'str'>
- **Required**: Yes


# Ibm3624PinOffsetTypeDef

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# Ibm3624PinVerificationTypeDef

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes

### PinOffset
- **Type**: <class 'str'>
- **Required**: Yes


# Ibm3624RandomPinTypeDef

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# MacAlgorithmDukptTypeDef

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### DukptKeyVariant
- **Type**: typing.Literal['BIDIRECTIONAL', 'REQUEST', 'RESPONSE']
- **Required**: Yes

### DukptDerivationType
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']]


# MacAlgorithmEmvTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### SessionKeyDerivationMode
- **Type**: typing.Literal['AMEX', 'EMV2000', 'EMV_COMMON_SESSION_KEY', 'MASTERCARD_SESSION_KEY', 'VISA']
- **Required**: Yes

### SessionKeyDerivationValue
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyDerivationValueTypeDef'>
- **Required**: Yes


# MacAttributesTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['CMAC', 'HMAC_SHA224', 'HMAC_SHA256', 'HMAC_SHA384', 'HMAC_SHA512', 'ISO9797_ALGORITHM1', 'ISO9797_ALGORITHM3']]

### EmvMac
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MacAlgorithmEmvTypeDef]

### DukptIso9797Algorithm1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MacAlgorithmDukptTypeDef]

### DukptIso9797Algorithm3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MacAlgorithmDukptTypeDef]

### DukptCmac
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MacAlgorithmDukptTypeDef]


# MasterCardAttributesTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationCryptogram
- **Type**: <class 'str'>
- **Required**: Yes


# PinDataTypeDef

### PinOffset
- **Type**: typing.Optional[str]

### VerificationValue
- **Type**: typing.Optional[str]


# PinGenerationAttributesTypeDef

### VisaPin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.VisaPinTypeDef]

### VisaPinVerificationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.VisaPinVerificationValueTypeDef]

### Ibm3624PinOffset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.Ibm3624PinOffsetTypeDef]

### Ibm3624NaturalPin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.Ibm3624NaturalPinTypeDef]

### Ibm3624RandomPin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.Ibm3624RandomPinTypeDef]

### Ibm3624PinFromOffset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.Ibm3624PinFromOffsetTypeDef]


# PinVerificationAttributesTypeDef

### VisaPin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.VisaPinVerificationTypeDef]

### Ibm3624Pin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.Ibm3624PinVerificationTypeDef]


# ReEncryptDataInputTypeDef

### IncomingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OutgoingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CipherText
- **Type**: <class 'str'>
- **Required**: Yes

### IncomingEncryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ReEncryptionAttributesTypeDef'>
- **Required**: Yes

### OutgoingEncryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ReEncryptionAttributesTypeDef'>
- **Required**: Yes

### IncomingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]

### OutgoingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]


# ReEncryptDataOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### CipherText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReEncryptionAttributesTypeDef

### Symmetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SymmetricEncryptionAttributesTypeDef]

### Dukpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DukptEncryptionAttributesTypeDef]


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


# SessionKeyAmexTypeDef

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyDerivationTypeDef

### EmvCommon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyEmvCommonTypeDef]

### Mastercard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyMastercardTypeDef]

### Emv2000
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyEmv2000TypeDef]

### Amex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyAmexTypeDef]

### Visa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyVisaTypeDef]


# SessionKeyDerivationValueTypeDef

### ApplicationCryptogram
- **Type**: typing.Optional[str]

### ApplicationTransactionCounter
- **Type**: typing.Optional[str]


# SessionKeyEmv2000TypeDef

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyEmvCommonTypeDef

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyMastercardTypeDef

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes

### UnpredictableNumber
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyVisaTypeDef

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes


# SymmetricEncryptionAttributesTypeDef

### Mode
- **Type**: typing.Literal['CBC', 'CFB', 'CFB1', 'CFB128', 'CFB64', 'CFB8', 'ECB', 'OFB']
- **Required**: Yes

### InitializationVector
- **Type**: typing.Optional[str]

### PaddingType
- **Type**: typing.Optional[typing.Literal['OAEP_SHA1', 'OAEP_SHA256', 'OAEP_SHA512', 'PKCS1']]


# TranslatePinDataInputTypeDef

### IncomingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OutgoingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### IncomingTranslationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.TranslationIsoFormatsTypeDef'>
- **Required**: Yes

### OutgoingTranslationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.TranslationIsoFormatsTypeDef'>
- **Required**: Yes

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### IncomingDukptAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DukptDerivationAttributesTypeDef]

### OutgoingDukptAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DukptDerivationAttributesTypeDef]

### IncomingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]

### OutgoingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]


# TranslatePinDataOutputTypeDef

### PinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TranslationIsoFormatsTypeDef

### IsoFormat0
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.TranslationPinDataIsoFormat034TypeDef]

### IsoFormat1
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IsoFormat3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.TranslationPinDataIsoFormat034TypeDef]

### IsoFormat4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.TranslationPinDataIsoFormat034TypeDef]


# TranslationPinDataIsoFormat034TypeDef

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyAuthRequestCryptogramInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionData
- **Type**: <class 'str'>
- **Required**: Yes

### AuthRequestCryptogram
- **Type**: <class 'str'>
- **Required**: Yes

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### SessionKeyDerivationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.SessionKeyDerivationTypeDef'>
- **Required**: Yes

### AuthResponseAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CryptogramAuthResponseTypeDef]


# VerifyAuthRequestCryptogramOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### AuthResponseValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyCardValidationDataInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CardVerificationAttributesTypeDef'>
- **Required**: Yes

### ValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyCardValidationDataOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyMacInputTypeDef

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MessageData
- **Type**: <class 'str'>
- **Required**: Yes

### Mac
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.MacAttributesTypeDef'>
- **Required**: Yes

### MacLength
- **Type**: typing.Optional[int]


# VerifyMacOutputTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyPinDataInputTypeDef

### VerificationKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.PinVerificationAttributesTypeDef'>
- **Required**: Yes

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PinBlockFormat
- **Type**: typing.Literal['ISO_FORMAT_0', 'ISO_FORMAT_3', 'ISO_FORMAT_4']
- **Required**: Yes

### PinDataLength
- **Type**: typing.Optional[int]

### DukptAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.DukptAttributesTypeDef]

### EncryptionWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyTypeDef]


# VerifyPinDataOutputTypeDef

### VerificationKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VisaAmexDerivationOutputsTypeDef

### AuthorizationRequestKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationRequestKeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentPinPekArn
- **Type**: typing.Optional[str]

### CurrentPinPekKeyCheckValue
- **Type**: typing.Optional[str]


# VisaAttributesTypeDef

### MajorKeyDerivationMode
- **Type**: typing.Literal['EMV_OPTION_A', 'EMV_OPTION_B']
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationRequestKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentPinAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.CurrentPinAttributesTypeDef]


# VisaPinTypeDef

### PinVerificationKeyIndex
- **Type**: <class 'int'>
- **Required**: Yes


# VisaPinVerificationTypeDef

### PinVerificationKeyIndex
- **Type**: <class 'int'>
- **Required**: Yes

### VerificationValue
- **Type**: <class 'str'>
- **Required**: Yes


# VisaPinVerificationValueTypeDef

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### PinVerificationKeyIndex
- **Type**: <class 'int'>
- **Required**: Yes


# WrappedKeyMaterialTypeDef

### Tr31KeyBlock
- **Type**: typing.Optional[str]

### DiffieHellmanSymmetricKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data_classes.EcdhDerivationAttributesTypeDef]


# WrappedKeyTypeDef

### WrappedKeyMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data_classes.WrappedKeyMaterialTypeDef'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]


