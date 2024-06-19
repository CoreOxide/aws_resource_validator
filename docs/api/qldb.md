# Qldb Service

### LedgerName
- **Type**: string
- **Pattern**: `(?!^.*--)(?!^[0-9]+$)(?!^-)(?!.*-$)^[A-Za-z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 32

### NextToken
- **Type**: string
- **Pattern**: `^[A-Za-z-0-9+/=]+$`
- **Min Length**: 4
- **Max Length**: 1024

### S3Bucket
- **Type**: string
- **Pattern**: `^[A-Za-z-0-9-_.]+$`
- **Min Length**: 3
- **Max Length**: 255

### StreamName
- **Type**: string
- **Pattern**: `(?!^.*--)(?!^[0-9]+$)(?!^-)(?!.*-$)^[A-Za-z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 32

### UniqueId
- **Type**: string
- **Pattern**: `^[A-Za-z-0-9]+$`
- **Min Length**: 22
- **Max Length**: 22

