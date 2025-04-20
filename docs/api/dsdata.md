# Dsdata Service

### ClientToken
- **Type**: string
- **Pattern**: `^[\x00-\x7F]+$`
- **Min Length**: 1
- **Max Length**: 128

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$`

### GroupName
- **Type**: string
- **Pattern**: `^[^:;|=+"*?<>/\\,\[\]@]+$`
- **Min Length**: 1
- **Max Length**: 64

### LdapDisplayName
- **Type**: string
- **Pattern**: `^[A-Za-z*][A-Za-z-*]*$`
- **Min Length**: 1
- **Max Length**: 63

### MemberName
- **Type**: string
- **Pattern**: `^[^:;|=+"*?<>/\\,\[\]@]+$`
- **Min Length**: 1
- **Max Length**: 63

### Realm
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`
- **Min Length**: 1
- **Max Length**: 255

### UserName
- **Type**: string
- **Pattern**: `^[\w\-.]+$`
- **Min Length**: 1
- **Max Length**: 20

