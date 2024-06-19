# Arczonalshift Service

### BlockedDate
- **Type**: string
- **Pattern**: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`
- **Min Length**: 10
- **Max Length**: 10

### BlockedWindow
- **Type**: string
- **Pattern**: `^(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}$`
- **Min Length**: 19
- **Max Length**: 19

### ExpiresIn
- **Type**: string
- **Pattern**: `^([1-9][0-9]*)(m|h)$`
- **Min Length**: 2
- **Max Length**: 5

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:.*$`
- **Min Length**: 8
- **Max Length**: 1024

### ZonalShiftId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-]+$`
- **Min Length**: 6
- **Max Length**: 36

