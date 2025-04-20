# Apptest Service

### Arn
- **Type**: string
- **Pattern**: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`

### IdempotencyTokenString
- **Type**: string
- **Pattern**: `[A-Za-z0-9\-]{1,64}`

### Identifier
- **Type**: string
- **Pattern**: `[A-Za-z0-9:/\-]{1,100}`

### NextToken
- **Type**: string
- **Pattern**: `\S{1,2000}`

### ResourceName
- **Type**: string
- **Pattern**: `[A-Za-z][A-Za-z0-9_\-]{1,59}`

### String100
- **Type**: string
- **Pattern**: `\S{1,100}`

### String50
- **Type**: string
- **Pattern**: `\S{1,50}`

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:).+`
- **Min Length**: 1
- **Max Length**: 128

### Variable
- **Type**: string
- **Pattern**: `\S{1,1000}`

