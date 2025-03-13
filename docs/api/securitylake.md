# Securitylake Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}$`
- **Min Length**: 1
- **Max Length**: 1011

### AwsAccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### AwsLogSourceVersion
- **Type**: string
- **Pattern**: `^(latest|[0-9]\.[0-9])$`

### AwsPrincipal
- **Type**: string
- **Pattern**: `^([0-9]{12}|[a-z0-9\.\-]*\.(amazonaws|amazon)\.com)$`

### CustomLogSourceName
- **Type**: string
- **Pattern**: `^[\w\-\_\:\.]*$`
- **Min Length**: 1
- **Max Length**: 64

### CustomLogSourceVersion
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\-\.\_]*$`
- **Min Length**: 1
- **Max Length**: 32

### DescriptionString
- **Type**: string
- **Pattern**: `^[\\\w\s\-_:/,.@=+]*$`

### ExternalId
- **Type**: string
- **Pattern**: `^[\w+=,.@:\/-]*$`
- **Min Length**: 2
- **Max Length**: 1224

### HttpsNotificationConfigurationEndpointString
- **Type**: string
- **Pattern**: `^https?://.+$`

### OcsfEventClass
- **Type**: string
- **Pattern**: `^[A-Z\_0-9]*$`

### Region
- **Type**: string
- **Pattern**: `^(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+$`

### ResourceShareName
- **Type**: string
- **Pattern**: `^LakeFormation(?:-V[0-9]+)-([a-zA-Z0-9]+)-([\\\w\-_:/.@=+]*)$`

### RoleArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

### S3URI
- **Type**: string
- **Pattern**: `^s3[an]?://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/[^/].*)+$`
- **Min Length**: 0
- **Max Length**: 1024

### SafeString
- **Type**: string
- **Pattern**: `^[\\\w\-_:/.@=+]*$`

### SubscriptionProtocol
- **Type**: string
- **Pattern**: `^[a-z\-]*$`

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### UpdateSubscriberRequestSubscriberNameString
- **Type**: string
- **Pattern**: `^[\\\w\-_:/.@=+]*$`
- **Min Length**: 0
- **Max Length**: 64

