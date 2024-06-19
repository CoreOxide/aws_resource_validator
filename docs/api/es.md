# Es Service

### AWSAccount
- **Type**: string
- **Pattern**: `^[0-9]+$`

### DescribePackagesFilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?-]*$`

### DomainArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 512

### DomainName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 3
- **Max Length**: 28

### DomainNameFqdn
- **Type**: string
- **Pattern**: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 255

### ElasticsearchVersionString
- **Type**: string
- **Pattern**: `^[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$|^OS_[0-9]{1,2}\.[0-9]{1,2}$`

### Endpoint
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\-\.]+$`

### GUID
- **Type**: string
- **Pattern**: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

### IdentityPoolId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### PackageName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 3
- **Max Length**: 28

### UserPoolId
- **Type**: string
- **Pattern**: `[\w-]+_[0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 55

### VpcEndpointId
- **Type**: string
- **Pattern**: `^aos-[a-zA-Z0-9]*$`
- **Min Length**: 5
- **Max Length**: 256

