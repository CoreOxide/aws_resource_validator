# Ssmsap Service

### AppRegistryArn
- **Type**: string
- **Pattern**: `arn:aws:servicecatalog:[a-z0-9:\/-]+`

### ApplicationId
- **Type**: string
- **Pattern**: `[\w\d]{1,50}`

### Arn
- **Type**: string
- **Pattern**: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`

### ComponentId
- **Type**: string
- **Pattern**: `[\w\d-]+`

### DatabaseId
- **Type**: string
- **Pattern**: `.*[\w\d]+`

### InstanceId
- **Type**: string
- **Pattern**: `i-[\w\d]{8}$|^i-[\w\d]{17}`

### NextToken
- **Type**: string
- **Pattern**: `.{16,1024}`

### OperationEventResourceType
- **Type**: string
- **Pattern**: `[\w]+::[\w]+::[\w]+`

### OperationId
- **Type**: string
- **Pattern**: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`

### SAPInstanceNumber
- **Type**: string
- **Pattern**: `[0-9]{2}`

### SID
- **Type**: string
- **Pattern**: `[A-Z][A-Z0-9]{2}`

### SsmSapArn
- **Type**: string
- **Pattern**: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[a-zA-Z+-=._:/]+`

