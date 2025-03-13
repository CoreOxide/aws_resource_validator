# Controlcatalog Service

### CommonControlArn
- **Type**: string
- **Pattern**: `arn:(aws(?:[-a-z]*)?):controlcatalog:::common-control/[0-9a-z]+`
- **Min Length**: 41
- **Max Length**: 2048

### ControlArn
- **Type**: string
- **Pattern**: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`
- **Min Length**: 34
- **Max Length**: 2048

### DomainArn
- **Type**: string
- **Pattern**: `arn:(aws(?:[-a-z]*)?):controlcatalog:::domain/[0-9a-z]+`
- **Min Length**: 33
- **Max Length**: 2048

### ImplementationType
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+(::[A-Za-z0-9_]+){2,3}`
- **Min Length**: 7
- **Max Length**: 2048

### ObjectiveArn
- **Type**: string
- **Pattern**: `arn:(aws(?:[-a-z]*)?):controlcatalog:::objective/[0-9a-z]+`
- **Min Length**: 36
- **Max Length**: 2048

### RegionCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]{1,128}`

