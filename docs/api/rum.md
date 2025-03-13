# Rum Service

### AppMonitorDomain
- **Type**: string
- **Pattern**: `^(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-]$`
- **Min Length**: 1
- **Max Length**: 253

### AppMonitorId
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### AppMonitorName
- **Type**: string
- **Pattern**: `^(?!\.)[\.\-_#A-Za-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 255

### Arn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

### DestinationArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
- **Min Length**: 0
- **Max Length**: 2048

### DimensionName
- **Type**: string
- **Pattern**: `^(?!:).*[^\s].*`
- **Min Length**: 1
- **Max Length**: 255

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

### IdentityPoolId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### Namespace
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-._/#:]+$`
- **Min Length**: 1
- **Max Length**: 237

### PutRumEventsRequestBatchIdString
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### PutRumEventsRequestIdString
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### RumEventIdString
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### Url
- **Type**: string
- **Pattern**: `https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&*//=]*)`
- **Min Length**: 1
- **Max Length**: 1260

### UserDetailsSessionIdString
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### UserDetailsUserIdString
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

