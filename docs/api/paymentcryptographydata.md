# Paymentcryptographydata Service

### ApplicationCryptogramType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 16
- **Max Length**: 16

### AuthRequestCryptogramType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 16
- **Max Length**: 16

### AuthResponseValueType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 1
- **Max Length**: 16

### CardExpiryDateType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 4
- **Max Length**: 4

### CertificateType
- **Type**: string
- **Pattern**: `[^\[;\]<>]+`
- **Min Length**: 1
- **Max Length**: 32768

### CipherTextType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 2
- **Max Length**: 4096

### CommandMessageDataType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 16
- **Max Length**: 1024

### DecimalizationTableType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 16
- **Max Length**: 16

### EncryptedPinBlockType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 16
- **Max Length**: 32

### HexEvenLengthBetween16And32
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 16
- **Max Length**: 32

### HexLengthBetween10And24
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 10
- **Max Length**: 24

### HexLengthBetween2And4
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 2
- **Max Length**: 4

### HexLengthBetween2And8
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 2
- **Max Length**: 8

### HexLengthEquals1
- **Type**: string
- **Pattern**: `[0-9A-F]+`
- **Min Length**: 1
- **Max Length**: 1

### HexLengthEquals4
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 4
- **Max Length**: 4

### HexLengthEquals8
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 8
- **Max Length**: 8

### InitializationVectorType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{32})`
- **Min Length**: 16
- **Max Length**: 32

### KeyArn
- **Type**: string
- **Pattern**: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
- **Min Length**: 70
- **Max Length**: 150

### KeyArnOrKeyAliasType
- **Type**: string
- **Pattern**: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
- **Min Length**: 7
- **Max Length**: 322

### KeyCheckValue
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 4
- **Max Length**: 16

### MacOutputType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 4
- **Max Length**: 128

### MacType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 4
- **Max Length**: 128

### MessageDataType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 2
- **Max Length**: 4096

### NumberLengthEquals2
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 2
- **Max Length**: 2

### PinBlockLengthEquals16
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 16
- **Max Length**: 16

### PinChangeMacOutputType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 8
- **Max Length**: 16

### PinOffsetType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 4
- **Max Length**: 12

### PinValidationDataType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 4
- **Max Length**: 16

### PlainTextOutputType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 2
- **Max Length**: 4096

### PlainTextType
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 2
- **Max Length**: 4064

### PrimaryAccountNumberType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 12
- **Max Length**: 19

### ProprietaryAuthenticationDataType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 1
- **Max Length**: 16

### ServiceCodeType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 3
- **Max Length**: 3

### SessionDerivationDataType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 16
- **Max Length**: 16

### SharedInformation
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 2
- **Max Length**: 2048

### Tr31WrappedKeyBlock
- **Type**: string
- **Pattern**: `[0-9A-Z]+`
- **Min Length**: 56
- **Max Length**: 9984

### TrackDataType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 2
- **Max Length**: 160

### TransactionDataType
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 2
- **Max Length**: 1024

### ValidationDataType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 3
- **Max Length**: 5

### VerificationValueType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 4
- **Max Length**: 12

