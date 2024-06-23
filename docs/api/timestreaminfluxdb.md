# Timestreaminfluxdb Service

### Arn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`
- **Min Length**: 1
- **Max Length**: 1011

### Bucket
- **Type**: string
- **Pattern**: `[^_][^"]*`
- **Min Length**: 2
- **Max Length**: 64

### DbInstanceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 3
- **Max Length**: 64

### DbInstanceIdentifier
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 3
- **Max Length**: 64

### DbInstanceName
- **Type**: string
- **Pattern**: `[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
- **Min Length**: 3
- **Max Length**: 40

### DbParameterGroupId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 3
- **Max Length**: 64

### DbParameterGroupIdentifier
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 3
- **Max Length**: 64

### DbParameterGroupName
- **Type**: string
- **Pattern**: `[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
- **Min Length**: 3
- **Max Length**: 64

### Password
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 8
- **Max Length**: 64

### S3ConfigurationBucketNameString
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 3
- **Max Length**: 63

### VpcSecurityGroupId
- **Type**: string
- **Pattern**: `sg-[a-z0-9]+`
- **Min Length**: 0
- **Max Length**: 64

### VpcSubnetId
- **Type**: string
- **Pattern**: `subnet-[a-z0-9]+`
- **Min Length**: 0
- **Max Length**: 64

