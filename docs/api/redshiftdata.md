# Redshiftdata Service

### ParameterName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_]+$`

### StatementId
- **Type**: string
- **Pattern**: `^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d+)?$`

### WorkgroupNameString
- **Type**: string
- **Pattern**: `^(([a-z0-9-]+)|(arn:(aws(-[a-z]+)*):redshift-serverless:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}))$`
- **Min Length**: 3
- **Max Length**: 128

