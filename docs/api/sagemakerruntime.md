# Sagemakerruntime Service

### CustomAttributesHeader
- **Type**: string
- **Pattern**: `\p{ASCII}*`
- **Max Length**: 1024

### EnableExplanationsHeader
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 64

### EndpointName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 63

### Header
- **Type**: string
- **Pattern**: `\p{ASCII}*`
- **Max Length**: 1024

### InferenceComponentHeader
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?$`
- **Max Length**: 63

### InferenceId
- **Type**: string
- **Pattern**: `\A\S[\p{Print}]*\z`
- **Min Length**: 1
- **Max Length**: 64

### InputLocationHeader
- **Type**: string
- **Pattern**: `^(https|s3)://([^/]+)/?(.*)$`
- **Min Length**: 1
- **Max Length**: 1024

### NewSessionResponseHeader
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*;\sExpires=[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`
- **Max Length**: 256

### SessionIdHeader
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Max Length**: 256

### SessionIdOrNewSessionConstantHeader
- **Type**: string
- **Pattern**: `^(NEW_SESSION)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Max Length**: 256

### TargetContainerHostnameHeader
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 63

### TargetModelHeader
- **Type**: string
- **Pattern**: `\A\S[\p{Print}]*\z`
- **Min Length**: 1
- **Max Length**: 1024

### TargetVariantHeader
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 63

