# Cur Service

### BillingViewArn
- **Type**: string
- **Pattern**: `(arn:aws(-cn)?:billing::[0-9]{12}:billingview/)?[a-zA-Z0-9_\+=\.\-@].{1,30}`
- **Max Length**: 128

### GenericString
- **Type**: string
- **Pattern**: `[A-Za-z0-9_\.\-=]*`
- **Max Length**: 256

### LastDelivery
- **Type**: string
- **Pattern**: `[0-9]{8}[T][0-9]{6}([Z]|[+-][0-9]{4})`
- **Min Length**: 16
- **Max Length**: 20

### ReportName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z!\-_.*\'()]+$`
- **Max Length**: 256

### S3Bucket
- **Type**: string
- **Pattern**: `[A-Za-z0-9_\.\-]+`
- **Max Length**: 256

### S3Prefix
- **Type**: string
- **Pattern**: `^[0-9A-Za-z!\-_.*\'()\/]+$`
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256

