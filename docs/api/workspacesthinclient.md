# Workspacesthinclient Service

### ActivationCode
- **Type**: string
- **Pattern**: `[a-z]{2}[a-z0-9]{6}`

### Arn
- **Type**: string
- **Pattern**: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+`
- **Min Length**: 20
- **Max Length**: 2048

### DesktopEndpoint
- **Type**: string
- **Pattern**: `(https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,32}(:[0-9]{1,5})?(\/.*)?`
- **Min Length**: 1
- **Max Length**: 1024

### DeviceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{24}`

### DeviceName
- **Type**: string
- **Pattern**: `[0-9\p{IsAlphabetic}+:,.@\'" -]{1,64}`

### EnvironmentId
- **Type**: string
- **Pattern**: `[a-z0-9]{9}`

### EnvironmentName
- **Type**: string
- **Pattern**: `[0-9\p{IsAlphabetic}+:,.@\'" -][0-9\p{IsAlphabetic}+=:,.@\'" -]{0,63}`

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[0-9]{0,12}:key\/[a-zA-Z0-9-]+`
- **Min Length**: 20
- **Max Length**: 2048

### PaginationToken
- **Type**: string
- **Pattern**: `\S*`
- **Min Length**: 0
- **Max Length**: 2048

### SoftwareSetId
- **Type**: string
- **Pattern**: `[0-9]{1,9}`

### SoftwareSetIdOrEmptyString
- **Type**: string
- **Pattern**: `[0-9]{0,9}`

