# Opensearch Service

### ARN
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 20
- **Max Length**: 2048

### AWSAccount
- **Type**: string
- **Pattern**: `^[0-9]+$`

### ApplicationName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 3
- **Max Length**: 30

### CloudWatchLogsLogGroupArn
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 20
- **Max Length**: 2048

### ConnectionAlias
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9\-\_]+`
- **Min Length**: 2
- **Max Length**: 100

### ConnectionId
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 10
- **Max Length**: 256

### DataSourceDescription
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
- **Max Length**: 1000

### DataSourceName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9_]+`
- **Min Length**: 3
- **Max Length**: 80

### DescribePackagesFilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\_\\\/\?-]+$`

### DirectQueryDataSourceDescription
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
- **Max Length**: 1000

### DirectQueryDataSourceName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9_]+`
- **Min Length**: 3
- **Max Length**: 80

### DirectQueryDataSourceRoleArn
- **Type**: string
- **Pattern**: `^arn:aws[a-zA-Z-]*:iam::\d{12}:role(\/service-role)?\/[A-Za-z0-9+=,.@\-_]{1,64}$`
- **Min Length**: 32
- **Max Length**: 200

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

### Endpoint
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\-\.]+$`

### EngineVersion
- **Type**: string
- **Pattern**: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`

### GUID
- **Type**: string
- **Pattern**: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
- **Min Length**: 36
- **Max Length**: 36

### Id
- **Type**: string
- **Pattern**: `[a-z0-9]{3,30}`

### IdentityCenterApplicationARN
- **Type**: string
- **Pattern**: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+\/[a-z0-9\\-]+`
- **Min Length**: 20
- **Max Length**: 2048

### IdentityCenterInstanceARN
- **Type**: string
- **Pattern**: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+`
- **Min Length**: 20
- **Max Length**: 2048

### IdentityPoolId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### IdentityStoreId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}\\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\\b[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 64

### InstanceTypeString
- **Type**: string
- **Pattern**: `^.*\..*\.search$`
- **Min Length**: 10
- **Max Length**: 40

### KmsKeyId
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 500

### LicenseFilepath
- **Type**: string
- **Pattern**: `^(?!.*\/\.{2,})(?!.*\.\.)[a-zA-Z0-9_.-]+(?:\/[a-zA-Z0-9_.-]+)*$`
- **Max Length**: 256

### MaintenanceStatusMessage
- **Type**: string
- **Pattern**: `^([\s\S]*)$`
- **Min Length**: 0
- **Max Length**: 1000

### NonEmptyString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-\_\.]+`
- **Min Length**: 1
- **Max Length**: 100

### NumberOfAZs
- **Type**: string
- **Pattern**: `^((\d+)|(NotAvailable))$`

### NumberOfNodes
- **Type**: string
- **Pattern**: `^((\d+)|(NotAvailable))$`

### NumberOfShards
- **Type**: string
- **Pattern**: `^((\d+)|(NotAvailable))$`

### OwnerId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 12
- **Max Length**: 12

### PackageID
- **Type**: string
- **Pattern**: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`

### PackageName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 3
- **Max Length**: 256

### PackageUser
- **Type**: string
- **Pattern**: `^[0-9]{12}$|^GLOBAL$`
- **Min Length**: 6
- **Max Length**: 12

### Password
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 8
- **Max Length**: 128

### PolicyDocument
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 102400

### Region
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 5
- **Max Length**: 30

### RequestId
- **Type**: string
- **Pattern**: `^([\s\S]*)$`
- **Min Length**: 1
- **Max Length**: 100

### ReservationToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 5
- **Max Length**: 64

### RoleArn
- **Type**: string
- **Pattern**: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
- **Min Length**: 20
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256

### UserPoolId
- **Type**: string
- **Pattern**: `[\w-]+_[0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 55

### Username
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 64

### VersionString
- **Type**: string
- **Pattern**: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
- **Min Length**: 14
- **Max Length**: 18

### VpcEndpointId
- **Type**: string
- **Pattern**: `^aos-[a-zA-Z0-9]*$`
- **Min Length**: 5
- **Max Length**: 256

