# Payment Cryptography Data Payment Cryptography Data Classes

# AmexAttributes

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
- **Type**: <class 'NoneType'>


# AmexCardSecurityCodeVersion1

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes


# AmexCardSecurityCodeVersion2

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes


# AsymmetricEncryptionAttributes

### PaddingType
- **Type**: typing.Optional[typing.Literal['OAEP_SHA1', 'OAEP_SHA256', 'OAEP_SHA512', 'PKCS1']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CardGenerationAttributes

### AmexCardSecurityCodeVersion1
- **Type**: <class 'NoneType'>

### AmexCardSecurityCodeVersion2
- **Type**: <class 'NoneType'>

### CardVerificationValue1
- **Type**: <class 'NoneType'>

### CardVerificationValue2
- **Type**: <class 'NoneType'>

### CardHolderVerificationValue
- **Type**: <class 'NoneType'>

### DynamicCardVerificationCode
- **Type**: <class 'NoneType'>

### DynamicCardVerificationValue
- **Type**: <class 'NoneType'>


# CardHolderVerificationValue

### UnpredictableNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# CardVerificationAttributes

### AmexCardSecurityCodeVersion1
- **Type**: <class 'NoneType'>

### AmexCardSecurityCodeVersion2
- **Type**: <class 'NoneType'>

### CardVerificationValue1
- **Type**: <class 'NoneType'>

### CardVerificationValue2
- **Type**: <class 'NoneType'>

### CardHolderVerificationValue
- **Type**: <class 'NoneType'>

### DynamicCardVerificationCode
- **Type**: <class 'NoneType'>

### DynamicCardVerificationValue
- **Type**: <class 'NoneType'>

### DiscoverDynamicCardVerificationCode
- **Type**: <class 'NoneType'>


# CardVerificationValue1

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes


# CardVerificationValue2

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes


# CryptogramAuthResponse

### ArpcMethod1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.CryptogramVerificationArpcMethod1]

### ArpcMethod2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.CryptogramVerificationArpcMethod2]


# CryptogramVerificationArpcMethod1

### AuthResponseCode
- **Type**: <class 'str'>
- **Required**: Yes


# CryptogramVerificationArpcMethod2

### CardStatusUpdate
- **Type**: <class 'str'>
- **Required**: Yes

### ProprietaryAuthenticationData
- **Type**: typing.Optional[str]


# CurrentPinAttributes

### CurrentPinPekIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentEncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes


# DecryptDataInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CipherText
- **Type**: <class 'str'>
- **Required**: Yes

### DecryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.EncryptionDecryptionAttributes'>
- **Required**: Yes

### WrappedKey
- **Type**: <class 'NoneType'>


# DecryptDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# DerivationMethodAttributes

### EmvCommon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.EmvCommonAttributes]

### Amex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.AmexAttributes]

### Visa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.VisaAttributes]

### Emv2000
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.Emv2000Attributes]

### Mastercard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MasterCardAttributes]


# DiscoverDynamicCardVerificationCode

### CardExpiryDate
- **Type**: <class 'str'>
- **Required**: Yes

### UnpredictableNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# DukptAttributes

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### DukptDerivationType
- **Type**: typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']
- **Required**: Yes


# DukptDerivationAttributes

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### DukptKeyDerivationType
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']]

### DukptKeyVariant
- **Type**: typing.Optional[typing.Literal['BIDIRECTIONAL', 'REQUEST', 'RESPONSE']]


# DukptEncryptionAttributes

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


# DynamicCardVerificationCode

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


# DynamicCardVerificationValue

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


# EcdhDerivationAttributes

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


# Emv2000Attributes

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


# EmvCommonAttributes

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


# EmvEncryptionAttributes

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


# EncryptDataInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PlainText
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.EncryptionDecryptionAttributes'>
- **Required**: Yes

### WrappedKey
- **Type**: <class 'NoneType'>


# EncryptDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionDecryptionAttributes

### Symmetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SymmetricEncryptionAttributes]

### Asymmetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.AsymmetricEncryptionAttributes]

### Dukpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.DukptEncryptionAttributes]

### Emv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.EmvEncryptionAttributes]


# GenerateCardValidationDataInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.CardGenerationAttributes'>
- **Required**: Yes

### ValidationDataLength
- **Type**: typing.Optional[int]


# GenerateCardValidationDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateMacEmvPinChangeInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.DerivationMethodAttributes'>
- **Required**: Yes


# GenerateMacEmvPinChangeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.VisaAmexDerivationOutputs'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateMacInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MessageData
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MacAttributes'>
- **Required**: Yes

### MacLength
- **Type**: typing.Optional[int]


# GenerateMacOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# GeneratePinDataInput

### GenerationKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.PinGenerationAttributes'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKey]


# GeneratePinDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.PinData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# Ibm3624NaturalPin

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# Ibm3624PinFromOffset

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


# Ibm3624PinOffset

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


# Ibm3624PinVerification

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


# Ibm3624RandomPin

### DecimalizationTable
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationDataPadCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### PinValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# MacAlgorithmDukpt

### KeySerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### DukptKeyVariant
- **Type**: typing.Literal['BIDIRECTIONAL', 'REQUEST', 'RESPONSE']
- **Required**: Yes

### DukptDerivationType
- **Type**: typing.Optional[typing.Literal['AES_128', 'AES_192', 'AES_256', 'TDES_2KEY', 'TDES_3KEY']]


# MacAlgorithmEmv

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyDerivationValue'>
- **Required**: Yes


# MacAttributes

### Algorithm
- **Type**: typing.Optional[typing.Literal['CMAC', 'HMAC_SHA224', 'HMAC_SHA256', 'HMAC_SHA384', 'HMAC_SHA512', 'ISO9797_ALGORITHM1', 'ISO9797_ALGORITHM3']]

### EmvMac
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MacAlgorithmEmv]

### DukptIso9797Algorithm1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MacAlgorithmDukpt]

### DukptIso9797Algorithm3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MacAlgorithmDukpt]

### DukptCmac
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MacAlgorithmDukpt]


# MasterCardAttributes

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


# PinData

### PinOffset
- **Type**: typing.Optional[str]

### VerificationValue
- **Type**: typing.Optional[str]


# PinGenerationAttributes

### VisaPin
- **Type**: <class 'NoneType'>

### VisaPinVerificationValue
- **Type**: <class 'NoneType'>

### Ibm3624PinOffset
- **Type**: <class 'NoneType'>

### Ibm3624NaturalPin
- **Type**: <class 'NoneType'>

### Ibm3624RandomPin
- **Type**: <class 'NoneType'>

### Ibm3624PinFromOffset
- **Type**: <class 'NoneType'>


# PinVerificationAttributes

### VisaPin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.VisaPinVerification]

### Ibm3624Pin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.Ibm3624PinVerification]


# ReEncryptDataInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ReEncryptionAttributes'>
- **Required**: Yes

### OutgoingEncryptionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ReEncryptionAttributes'>
- **Required**: Yes

### IncomingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKey]

### OutgoingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKey]


# ReEncryptDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# ReEncryptionAttributes

### Symmetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SymmetricEncryptionAttributes]

### Dukpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.DukptEncryptionAttributes]


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


# SessionKeyAmex

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyDerivation

### EmvCommon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyEmvCommon]

### Mastercard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyMastercard]

### Emv2000
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyEmv2000]

### Amex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyAmex]

### Visa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyVisa]


# SessionKeyDerivationValue

### ApplicationCryptogram
- **Type**: typing.Optional[str]

### ApplicationTransactionCounter
- **Type**: typing.Optional[str]


# SessionKeyEmv2000

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyEmvCommon

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationTransactionCounter
- **Type**: <class 'str'>
- **Required**: Yes


# SessionKeyMastercard

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


# SessionKeyVisa

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PanSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes


# SymmetricEncryptionAttributes

### Mode
- **Type**: typing.Literal['CBC', 'CFB', 'CFB1', 'CFB128', 'CFB64', 'CFB8', 'ECB', 'OFB']
- **Required**: Yes

### InitializationVector
- **Type**: typing.Optional[str]

### PaddingType
- **Type**: typing.Optional[typing.Literal['OAEP_SHA1', 'OAEP_SHA256', 'OAEP_SHA512', 'PKCS1']]


# TranslatePinDataInput

### IncomingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OutgoingKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### IncomingTranslationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.TranslationIsoFormats'>
- **Required**: Yes

### OutgoingTranslationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.TranslationIsoFormats'>
- **Required**: Yes

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### IncomingDukptAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.DukptDerivationAttributes]

### OutgoingDukptAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.DukptDerivationAttributes]

### IncomingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKey]

### OutgoingWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKey]


# TranslatePinDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# TranslationIsoFormats

### IsoFormat0
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.TranslationPinDataIsoFormat034]

### IsoFormat1
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IsoFormat3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.TranslationPinDataIsoFormat034]

### IsoFormat4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.TranslationPinDataIsoFormat034]


# TranslationPinDataIsoFormat034

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyAuthRequestCryptogramInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.SessionKeyDerivation'>
- **Required**: Yes

### AuthResponseAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.CryptogramAuthResponse]


# VerifyAuthRequestCryptogramOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyCardValidationDataInput

### KeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryAccountNumber
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.CardVerificationAttributes'>
- **Required**: Yes

### ValidationData
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyCardValidationDataOutput

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyMacInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.MacAttributes'>
- **Required**: Yes

### MacLength
- **Type**: typing.Optional[int]


# VerifyMacOutput

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyCheckValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyPinDataInput

### VerificationKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.PinVerificationAttributes'>
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
- **Type**: <class 'NoneType'>

### EncryptionWrappedKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKey]


# VerifyPinDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.ResponseMetadata'>
- **Required**: Yes


# VisaAmexDerivationOutputs

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


# VisaAttributes

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
- **Type**: <class 'NoneType'>


# VisaPin

### PinVerificationKeyIndex
- **Type**: <class 'int'>
- **Required**: Yes


# VisaPinVerification

### PinVerificationKeyIndex
- **Type**: <class 'int'>
- **Required**: Yes

### VerificationValue
- **Type**: <class 'str'>
- **Required**: Yes


# VisaPinVerificationValue

### EncryptedPinBlock
- **Type**: <class 'str'>
- **Required**: Yes

### PinVerificationKeyIndex
- **Type**: <class 'int'>
- **Required**: Yes


# WrappedKey

### WrappedKeyMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.WrappedKeyMaterial'>
- **Required**: Yes

### KeyCheckValueAlgorithm
- **Type**: typing.Optional[typing.Literal['ANSI_X9_24', 'CMAC']]


# WrappedKeyMaterial

### Tr31KeyBlock
- **Type**: typing.Optional[str]

### DiffieHellmanSymmetricKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_classes.EcdhDerivationAttributes]


