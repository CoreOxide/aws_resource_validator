# Sesv2 Service

### AdditionalContactEmailAddress
- **Type**: string
- **Pattern**: `^(.+)@(.+)$`
- **Min Length**: 6
- **Max Length**: 254

### ArchiveArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-[a-z-]+):ses:[a-z]{2}-[a-z-]+-[0-9]:[0-9]{1,20}:mailmanager-archive/a-[a-z0-9]{24,62}`
- **Min Length**: 20
- **Max Length**: 1011

### EndpointName
- **Type**: string
- **Pattern**: `^[\w\-_]+$`
- **Min Length**: 1
- **Max Length**: 64

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

### NextTokenV2
- **Type**: string
- **Pattern**: `^^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
- **Min Length**: 1
- **Max Length**: 5000

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

