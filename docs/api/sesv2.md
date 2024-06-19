# Sesv2 Service

### AdditionalContactEmailAddress
- **Type**: string
- **Pattern**: `^(.+)@(.+)$`
- **Min Length**: 6
- **Max Length**: 254

### MessageHeaderName
- **Type**: string
- **Pattern**: `^[!-9;-@A-~]+$`
- **Min Length**: 1
- **Max Length**: 126

### MessageHeaderValue
- **Type**: string
- **Pattern**: `[ -~]*`
- **Min Length**: 1
- **Max Length**: 870

### PrivateKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+\/]+={0,2}$`
- **Min Length**: 1
- **Max Length**: 20480

### S3Url
- **Type**: string
- **Pattern**: `^s3:\/\/([^\/]+)\/(.*?([^\/]+)\/?)$`

### Selector
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]))$`
- **Min Length**: 1
- **Max Length**: 63

### WebsiteURL
- **Type**: string
- **Pattern**: `^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?`
- **Min Length**: 1
- **Max Length**: 1000

