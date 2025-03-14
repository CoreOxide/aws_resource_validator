# Licensemanagerusersubscriptions Service

### Arn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}$`

### Directory
- **Type**: string
- **Pattern**: `^(d|sd)-[0-9a-f]{10}$`

### IpV4
- **Type**: string
- **Pattern**: `^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$`

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,510})/([a-z0-9-\.]{1,510})$`

### SecurityGroup
- **Type**: string
- **Pattern**: `^sg-(([0-9a-z]{8})|([0-9a-z]{17}))$`
- **Min Length**: 5
- **Max Length**: 200

### Subnet
- **Type**: string
- **Pattern**: `^subnet-[a-z0-9]{8,17}`

