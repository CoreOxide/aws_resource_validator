# Savingsplans Service

### JsonSafeFilterValueString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_ \/.\:\-\(\)]+$`

### PaginationToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9/=\+]+$`
- **Max Length**: 1024

### SavingsPlanArn
- **Type**: string
- **Pattern**: `arn:aws:[a-z]+:([a-z]{2}-[a-z]+-\d{1}|):(\d{12}):savingsplan\/([0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})$`

### SavingsPlanDescription
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\- ]+$`

### SavingsPlanOperation
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_ \/.:-]*$`
- **Max Length**: 255

### SavingsPlanRateOperation
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_ \/.:-]*$`
- **Max Length**: 255

### SavingsPlanRateUsageType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_ \/.:-]+$`
- **Max Length**: 255

### SavingsPlanServiceCode
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Max Length**: 255

### SavingsPlanUsageType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_ \/.:-]+$`
- **Max Length**: 255

### UUID
- **Type**: string
- **Pattern**: `[a-f0-9]+(-[a-f0-9]+)*`

