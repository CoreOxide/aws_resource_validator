# Wafv2 Service

### APIKey
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### CreationPathString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### CustomHTTPHeaderName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._$-]+$`
- **Min Length**: 1
- **Max Length**: 64

### CustomHTTPHeaderValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### EntityDescription
- **Type**: string
- **Pattern**: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
- **Min Length**: 1
- **Max Length**: 256

### EntityId
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 36

### EntityName
- **Type**: string
- **Pattern**: `^[\w\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### FailureValue
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 100

### FieldIdentifier
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 512

### FieldToMatchData
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### FieldToProtectKeyName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### ForwardedIPHeaderName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 255

### IPAddress
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 50

### JsonPointerPath
- **Type**: string
- **Pattern**: `([/])|([/](([^~])|(~[01]))+)`
- **Min Length**: 1
- **Max Length**: 512

### LabelMatchKey
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_\-:]+$`
- **Min Length**: 1
- **Max Length**: 1024

### LabelName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_\-:]+$`
- **Min Length**: 1
- **Max Length**: 1024

### LabelNamespace
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_\-:]+:$`
- **Min Length**: 1
- **Max Length**: 1024

### LockToken
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 36

### LoginPathString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### MetricName
- **Type**: string
- **Pattern**: `^[\w#:\.\-/]+$`
- **Min Length**: 1
- **Max Length**: 255

### NextMarker
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### PolicyString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 395000

### ProductDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1

### ProductId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### ProductLink
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### ProductTitle
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1

### RegexPatternString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 512

### RegistrationPagePathString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### ResourceArn
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 20
- **Max Length**: 2048

### ResponseContent
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 10240

### ResponseInspectionHeaderName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 200

### SingleCookieName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 60

### SuccessValue
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 100

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### TokenDomain
- **Type**: string
- **Pattern**: `^[\w\.\-/]+$`
- **Min Length**: 1
- **Max Length**: 253

### VendorName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### VersionKeyString
- **Type**: string
- **Pattern**: `^[\w#:\.\-/]+$`
- **Min Length**: 1
- **Max Length**: 64

