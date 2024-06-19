# Iotthingsgraph Service

### FlowTemplateFilterValue
- **Type**: string
- **Pattern**: `^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$`

### SystemTemplateFilterValue
- **Type**: string
- **Pattern**: `^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### ThingName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### Urn
- **Type**: string
- **Pattern**: `^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$`
- **Max Length**: 160

