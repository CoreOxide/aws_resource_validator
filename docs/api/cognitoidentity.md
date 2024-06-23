# Cognitoidentity Service

### AccountId
- **Type**: string
- **Pattern**: `\d+`
- **Min Length**: 1
- **Max Length**: 15

### ClaimName
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 64

### CognitoIdentityProviderClientId
- **Type**: string
- **Pattern**: `[\w_]+`
- **Min Length**: 1
- **Max Length**: 128

### CognitoIdentityProviderName
- **Type**: string
- **Pattern**: `[\w._:/-]+`
- **Min Length**: 1
- **Max Length**: 128

### DeveloperProviderName
- **Type**: string
- **Pattern**: `[\w._-]+`
- **Min Length**: 1
- **Max Length**: 128

### IdentityId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### IdentityPoolId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### IdentityPoolName
- **Type**: string
- **Pattern**: `[\w\s+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### IdentityProviderId
- **Type**: string
- **Pattern**: `[\w.;_/-]+`
- **Min Length**: 1
- **Max Length**: 128

### PaginationKey
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 65535

### RoleType
- **Type**: string
- **Pattern**: `(un)?authenticated`
- **Min Length**: 1
- **Max Length**: 128

