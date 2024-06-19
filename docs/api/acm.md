# Acm Service

### Arn
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`
- **Min Length**: 20
- **Max Length**: 2048

### CertificateBody
- **Type**: string
- **Pattern**: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`
- **Min Length**: 1
- **Max Length**: 32768

### CertificateChain
- **Type**: string
- **Pattern**: `(-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}\u000D?\u000A)*-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`
- **Min Length**: 1
- **Max Length**: 2097152

### DomainNameString
- **Type**: string
- **Pattern**: `^(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 253

### IdempotencyToken
- **Type**: string
- **Pattern**: `\w+`
- **Min Length**: 1
- **Max Length**: 32

### NextToken
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]*`
- **Min Length**: 1
- **Max Length**: 10000

### PcaArn
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`
- **Min Length**: 20
- **Max Length**: 2048

### PrivateKey
- **Type**: string
- **Pattern**: `-{5}BEGIN PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END PRIVATE KEY-{5}(\u000D?\u000A)?`
- **Min Length**: 1
- **Max Length**: 524288

### TagKey
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:\/=+\-@]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:\/=+\-@]*`
- **Min Length**: 0
- **Max Length**: 256

