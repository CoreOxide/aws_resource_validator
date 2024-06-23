# Rbin Service

### Description
- **Type**: string
- **Pattern**: `^[\S ]{0,255}$`

### NextToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/=]{1,2048}$`

### ResourceTagKey
- **Type**: string
- **Pattern**: `^[\S\s]{1,128}$`

### ResourceTagValue
- **Type**: string
- **Pattern**: `^[\S\s]{0,256}$`

### RuleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]{1,3}){0,2}:rbin:[a-z\-0-9]{0,63}:[0-9]{12}:rule/[0-9a-zA-Z]{11}{0,1011}$`
- **Min Length**: 0
- **Max Length**: 1011

### RuleIdentifier
- **Type**: string
- **Pattern**: `[0-9a-zA-Z]{11}`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

