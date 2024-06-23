# Verifiedpermissions Service

### ActionId
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 200

### ActionType
- **Type**: string
- **Pattern**: `Action$|^.+::Action`
- **Min Length**: 1
- **Max Length**: 200

### ClientId
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### DiscoveryUrl
- **Type**: string
- **Pattern**: `https://.*`
- **Min Length**: 1
- **Max Length**: 2048

### EntityId
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 200

### EntityType
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 200

### GroupEntityType
- **Type**: string
- **Pattern**: `([_a-zA-Z][_a-zA-Z0-9]*::)*[_a-zA-Z][_a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 200

### IdempotencyToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 1
- **Max Length**: 64

### IdentitySourceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 1
- **Max Length**: 200

### Issuer
- **Type**: string
- **Pattern**: `https://.*`
- **Min Length**: 1
- **Max Length**: 2048

### Namespace
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 100

### NextToken
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_=+/\.]*`
- **Min Length**: 1
- **Max Length**: 8000

### PolicyId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 1
- **Max Length**: 200

### PolicyStoreId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 1
- **Max Length**: 200

### PolicyTemplateId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 1
- **Max Length**: 200

### PrincipalEntityType
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 200

### ResourceArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
- **Min Length**: 1
- **Max Length**: 2500

### Token
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`
- **Min Length**: 1
- **Max Length**: 131072

### UserPoolArn
- **Type**: string
- **Pattern**: `arn:[a-zA-Z0-9-]+:cognito-idp:(([a-zA-Z0-9-]+:\d{12}:userpool/[\w-]+_[0-9a-zA-Z]+))`
- **Min Length**: 1
- **Max Length**: 255

