# Georoutes Service

### CountryCode
- **Type**: string
- **Pattern**: `([A-Z]{2}|[A-Z]{3})`
- **Min Length**: 2
- **Max Length**: 3

### CountryCode3
- **Type**: string
- **Pattern**: `[A-Z]{3}`
- **Min Length**: 3
- **Max Length**: 3

### CurrencyCode
- **Type**: string
- **Pattern**: `[A-Z]{3}`
- **Min Length**: 3
- **Max Length**: 3

### TimeOfDay
- **Type**: string
- **Pattern**: `([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](Z|[+-]([0-1]?[0-9]|2[0-3]):[0-5][0-9])`

### TimestampWithTimezoneOffset
- **Type**: string
- **Pattern**: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`

