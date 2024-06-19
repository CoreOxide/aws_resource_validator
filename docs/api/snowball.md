# Snowball Service

### AddressId
- **Type**: string
- **Pattern**: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 40
- **Max Length**: 40

### AmiId
- **Type**: string
- **Pattern**: `(ami-[0-9a-f]{8})|(ami-[0-9a-f]{17})`
- **Min Length**: 12
- **Max Length**: 21

### ClusterId
- **Type**: string
- **Pattern**: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 39
- **Max Length**: 39

### DevicePickupId
- **Type**: string
- **Pattern**: `DPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 40
- **Max Length**: 40

### Email
- **Type**: string
- **Pattern**: `^(?=.{3,100}$).+@.+[.].+$`
- **Min Length**: 3
- **Max Length**: 320

### GSTIN
- **Type**: string
- **Pattern**: `\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}`
- **Min Length**: 15
- **Max Length**: 15

### JobId
- **Type**: string
- **Pattern**: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 39
- **Max Length**: 39

### KmsKeyARN
- **Type**: string
- **Pattern**: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`
- **Max Length**: 255

### LongTermPricingId
- **Type**: string
- **Pattern**: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 41
- **Max Length**: 41

### PhoneNumber
- **Type**: string
- **Pattern**: `^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$`
- **Min Length**: 7
- **Max Length**: 30

### ResourceARN
- **Type**: string
- **Pattern**: `arn:aws.*:*`
- **Max Length**: 255

### RoleARN
- **Type**: string
- **Pattern**: `arn:aws.*:iam::[0-9]{12}:role/.*`
- **Max Length**: 255

### SnsTopicARN
- **Type**: string
- **Pattern**: `arn:aws.*:sns:.*:[0-9]{12}:.*`
- **Max Length**: 255

### String
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

