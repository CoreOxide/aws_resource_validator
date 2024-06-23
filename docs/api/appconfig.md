# Appconfig Service

### Arn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:[a-z]+:([a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
- **Min Length**: 20
- **Max Length**: 2048

### ConfigurationProfileType
- **Type**: string
- **Pattern**: `^[a-zA-Z\.]+`

### DeploymentStrategyId
- **Type**: string
- **Pattern**: `(^[a-z0-9]{4,7}$|^AppConfig\.[A-Za-z0-9]{9,40}$)`

### DynamicParameterKey
- **Type**: string
- **Pattern**: `^([^#\n]{1,96})#([^\/#\n]{1,64})$`

### ExtensionOrParameterName
- **Type**: string
- **Pattern**: `^[^\/#:\n]{1,64}$`

### Id
- **Type**: string
- **Pattern**: `[a-z0-9]{4,7}`

### RoleArn
- **Type**: string
- **Pattern**: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):(iam)::\d{12}:role[/].*)$`
- **Min Length**: 20
- **Max Length**: 2048

### VersionLabel
- **Type**: string
- **Pattern**: `.*[^0-9].*`
- **Min Length**: 1
- **Max Length**: 64

