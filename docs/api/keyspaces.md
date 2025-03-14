# Keyspaces Service

### ARN
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`
- **Min Length**: 20
- **Max Length**: 1000

### KeyspaceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
- **Min Length**: 1
- **Max Length**: 48

### TableName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
- **Min Length**: 1
- **Max Length**: 48

### TablesReplicationProgress
- **Type**: string
- **Pattern**: `[0-9]{1,3}(?:[.][0-9]{1,2})?%`
- **Min Length**: 2
- **Max Length**: 7

