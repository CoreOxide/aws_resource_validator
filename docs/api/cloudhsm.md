# Cloudhsm Service

### AZ
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]*`

### Certificate
- **Type**: string
- **Pattern**: `[\w :+=./\n-]*`
- **Min Length**: 600
- **Max Length**: 2400

### CertificateFingerprint
- **Type**: string
- **Pattern**: `([0-9a-fA-F][0-9a-fA-F]:){15}[0-9a-fA-F][0-9a-fA-F]`

### ClientArn
- **Type**: string
- **Pattern**: `arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\-]*:[0-9]{12}:client-[0-9a-f]{8}`

### ClientLabel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]{2,64}`

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{1,64}`

### EniId
- **Type**: string
- **Pattern**: `eni-[0-9a-f]{8}`

### ExternalId
- **Type**: string
- **Pattern**: `[\w :+=./-]*`

### HapgArn
- **Type**: string
- **Pattern**: `arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\-]*:[0-9]{12}:hapg-[0-9a-f]{8}`

### HsmArn
- **Type**: string
- **Pattern**: `arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\-]*:[0-9]{12}:hsm-[0-9a-f]{8}`

### HsmSerialNumber
- **Type**: string
- **Pattern**: `\d{1,16}`

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-iso)?:iam::[0-9]{12}:role/[a-zA-Z0-9_\+=,\.\-@]{1,64}`

### IpAddress
- **Type**: string
- **Pattern**: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

### Label
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]{1,64}`

### PaginationToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+/]*`

### PartitionArn
- **Type**: string
- **Pattern**: `arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\-]*:[0-9]{12}:hsm-[0-9a-f]{8}/partition-[0-9]{6,12}`

### PartitionSerial
- **Type**: string
- **Pattern**: `\d{6,12}`

### SshKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+/= ._:\\@-]*`

### String
- **Type**: string
- **Pattern**: `[\w :+=./\\-]*`

### SubnetId
- **Type**: string
- **Pattern**: `subnet-[0-9a-f]{8}`

### Timestamp
- **Type**: string
- **Pattern**: `\d*`

### VpcId
- **Type**: string
- **Pattern**: `vpc-[0-9a-f]{8}`

