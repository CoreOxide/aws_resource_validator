# Billing Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### BillingViewArn
- **Type**: string
- **Pattern**: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,59}[a-zA-Z0-9]`

### BillingViewDescription
- **Type**: string
- **Pattern**: `([ a-zA-Z0-9_\+=\.\-@]+)?`
- **Min Length**: 0
- **Max Length**: 1024

### BillingViewName
- **Type**: string
- **Pattern**: `[ a-zA-Z0-9_\+=\.\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws[a-z-]*:(billing)::[0-9]{12}:[a-zA-Z0-9/:_\+=\.\@-]{0,70}[a-zA-Z0-9]`

### TagKey
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### Value
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

