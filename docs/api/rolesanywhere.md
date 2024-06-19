# Rolesanywhere Service

### ProfileArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:profile.*)$`
- **Min Length**: 1
- **Max Length**: 1011

### ResourceName
- **Type**: string
- **Pattern**: `^[ a-zA-Z0-9-_]*$`
- **Min Length**: 1
- **Max Length**: 255

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:iam(:.*){2}(:role.*)$`
- **Min Length**: 1
- **Max Length**: 1011

### TagKey
- **Type**: string
- **Pattern**: `^[ a-zA-Z0-9_.:/=+@-]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[ a-zA-Z0-9_.:/=+@-]*$`
- **Min Length**: 0
- **Max Length**: 256

### TrustAnchorArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:trust-anchor.*)$`
- **Min Length**: 1
- **Max Length**: 1011

### Uuid
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

