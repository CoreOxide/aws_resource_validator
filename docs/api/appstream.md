# Appstream Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d+$`

### EmbedHostDomain
- **Type**: string
- **Pattern**: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
- **Max Length**: 128

### Name
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`

### S3Bucket
- **Type**: string
- **Pattern**: `^[0-9a-z\.\-]*(?<!\.)$`
- **Min Length**: 3
- **Max Length**: 63

### StreamingUrlUserId
- **Type**: string
- **Pattern**: `[\w+=,.@-]*`
- **Min Length**: 2
- **Max Length**: 32

### TagKey
- **Type**: string
- **Pattern**: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### ThemeFooterLinkDisplayName
- **Type**: string
- **Pattern**: `^[-@./#&+\w\s]*$`
- **Min Length**: 1
- **Max Length**: 300

### ThemeTitleText
- **Type**: string
- **Pattern**: `^[-@./#&+\w\s]*$`
- **Min Length**: 1
- **Max Length**: 300

### UsbDeviceFilterString
- **Type**: string
- **Pattern**: `^((\w*)\s*(\w*)\s*\,\s*(\w*)\s*\,\s*\*?(\w*)\s*\,\s*\*?(\w*)\s*\,\s*\*?\d*\s*\,\s*\*?\d*\s*\,\s*[0-1]\s*\,\s*[0-1]\s*)$`
- **Min Length**: 0
- **Max Length**: 100

### UserAttributeValue
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_\-\s]+$`
- **Max Length**: 2048

### Username
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

