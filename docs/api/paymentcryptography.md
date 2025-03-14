# Paymentcryptography Service

### AliasName
- **Type**: string
- **Pattern**: `alias/[a-zA-Z0-9/_-]+`
- **Min Length**: 7
- **Max Length**: 256

### CertificateType
- **Type**: string
- **Pattern**: `[^\[;\]<>]+`
- **Min Length**: 1
- **Max Length**: 32768

### EvenHexLengthBetween16And32
- **Type**: string
- **Pattern**: `(?:[0-9a-fA-F][0-9a-fA-F])+`
- **Min Length**: 16
- **Max Length**: 32

### ExportTokenId
- **Type**: string
- **Pattern**: `export-token-[0-9a-zA-Z]{16,64}`

### HexLength20Or24
- **Type**: string
- **Pattern**: `[0-9A-F]{20}$|^[0-9A-F]{24}`
- **Min Length**: 20
- **Max Length**: 24

### ImportTokenId
- **Type**: string
- **Pattern**: `import-token-[0-9a-zA-Z]{16,64}`

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

### KeyVersion
- **Type**: string
- **Pattern**: `[0-9A-Z]{2}+`
- **Min Length**: 2
- **Max Length**: 2

### OptionalBlockId
- **Type**: string
- **Pattern**: `[0-9A-Z]{2}+`
- **Min Length**: 2
- **Max Length**: 2

### OptionalBlockValue
- **Type**: string
- **Pattern**: `[0-9A-Z]+`
- **Min Length**: 1
- **Max Length**: 108

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
- **Min Length**: 70
- **Max Length**: 150

### Tr31WrappedKeyBlock
- **Type**: string
- **Pattern**: `[0-9A-Z]+`
- **Min Length**: 56
- **Max Length**: 9984

### Tr34WrappedKeyBlock
- **Type**: string
- **Pattern**: `[0-9A-F]+`
- **Min Length**: 2
- **Max Length**: 4096

### WrappedKeyCryptogram
- **Type**: string
- **Pattern**: `[0-9A-F]+`
- **Min Length**: 16
- **Max Length**: 4096

