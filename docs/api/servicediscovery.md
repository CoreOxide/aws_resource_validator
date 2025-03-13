# Servicediscovery Service

### AttrKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9!-~]+$`
- **Max Length**: 255

### AttrValue
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
- **Max Length**: 1024

### InstanceId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_/:.@-]+$`
- **Max Length**: 64

### NamespaceName
- **Type**: string
- **Pattern**: `^[!-~]{1,1024}$`
- **Max Length**: 1024

### NamespaceNameHttp
- **Type**: string
- **Pattern**: `^[!-~]{1,1024}$`
- **Max Length**: 1024

### NamespaceNamePrivate
- **Type**: string
- **Pattern**: `^[!-~]{1,253}$`
- **Max Length**: 253

### NamespaceNamePublic
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$`
- **Max Length**: 253

### ServiceName
- **Type**: string
- **Pattern**: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`

