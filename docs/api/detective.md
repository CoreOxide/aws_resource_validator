# Detective Service

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### EmailAddress
- **Type**: string
- **Pattern**: `^.+@(?:(?:(?!-)[A-Za-z0-9-]{1,62})?[A-Za-z0-9]{1}\.)+[A-Za-z]{2,63}$`
- **Min Length**: 1
- **Max Length**: 64

### EntityArn
- **Type**: string
- **Pattern**: `^arn:.*`

### GraphArn
- **Type**: string
- **Pattern**: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`

### InvestigationId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 21
- **Max Length**: 21

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

