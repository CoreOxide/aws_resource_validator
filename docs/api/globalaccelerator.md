# Globalaccelerator Service

### AttachmentName
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Max Length**: 64

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### HealthCheckPath
- **Type**: string
- **Pattern**: `^/[-a-zA-Z0-9@:%_\\+.~#?&/=]*$`
- **Max Length**: 255

### Principal
- **Type**: string
- **Pattern**: `(^\d{12}$|arn:.*)`
- **Max Length**: 256

