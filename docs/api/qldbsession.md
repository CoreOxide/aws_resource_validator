# Qldbsession Service

### LedgerName
- **Type**: string
- **Pattern**: `(?!^.*--)(?!^[0-9]+$)(?!^-)(?!.*-$)^[A-Za-z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 32

### PageToken
- **Type**: string
- **Pattern**: `^[A-Za-z-0-9+/=]+$`
- **Min Length**: 4
- **Max Length**: 1024

### SessionToken
- **Type**: string
- **Pattern**: `^[A-Za-z-0-9+/=]+$`
- **Min Length**: 4
- **Max Length**: 1024

### TransactionId
- **Type**: string
- **Pattern**: `^[A-Za-z-0-9]+$`
- **Min Length**: 22
- **Max Length**: 22

