# Worklink Service

### AcmCertificateArn
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=/,.@-]+)*`

### AuditStreamArn
- **Type**: string
- **Pattern**: `^arn:aws:kinesis:.+:[0-9]{12}:stream/AmazonWorkLink-.*$`

### Certificate
- **Type**: string
- **Pattern**: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`
- **Min Length**: 1
- **Max Length**: 8192

### CertificateChain
- **Type**: string
- **Pattern**: `(-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}\u000D?\u000A)*-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`
- **Min Length**: 1
- **Max Length**: 32768

### DomainName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]?((?!-)([A-Za-z0-9-]*[A-Za-z0-9])\.)+[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 253

### FleetName
- **Type**: string
- **Pattern**: `^[a-z0-9](?:[a-z0-9\-]{0,46}[a-z0-9])?$`
- **Min Length**: 1
- **Max Length**: 48

### NextToken
- **Type**: string
- **Pattern**: `[\w\-]+`
- **Min Length**: 1
- **Max Length**: 4096

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-([0-9a-f]{8}|[0-9a-f]{17})$`

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-([0-9a-f]{8}|[0-9a-f]{17})$`

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### VpcId
- **Type**: string
- **Pattern**: `^vpc-([0-9a-f]{8}|[0-9a-f]{17})$`

