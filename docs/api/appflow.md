# Appflow Service

### ARN
- **Type**: string
- **Pattern**: `arn:aws:.*:.*:[0-9]+:.*`
- **Max Length**: 512

### AccessKeyId
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### AccessToken
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 4096

### AccountName
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ApiKey
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ApiSecretKey
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ApiToken
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ApiVersion
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ApplicationHostUrl
- **Type**: string
- **Pattern**: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
- **Max Length**: 256

### ApplicationKey
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ApplicationServicePath
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ApplicationType
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### AuthCode
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 4096

### AuthCodeUrl
- **Type**: string
- **Pattern**: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
- **Max Length**: 256

### BucketName
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 3
- **Max Length**: 63

### BucketPrefix
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 512

### BusinessUnitId
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 18

### ClientCredentialsArn
- **Type**: string
- **Pattern**: `arn:aws:secretsmanager:.*:[0-9]+:.*`
- **Min Length**: 20
- **Max Length**: 2048

### ClientId
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ClientNumber
- **Type**: string
- **Pattern**: `^\d{3}$`
- **Min Length**: 3
- **Max Length**: 3

### ClientSecret
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ClientToken
- **Type**: string
- **Pattern**: `[ -~]+`
- **Min Length**: 1
- **Max Length**: 256

### ClusterIdentifier
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ConnectorDescription
- **Type**: string
- **Pattern**: `[\w!@#\-.?,\s]*`
- **Max Length**: 2048

### ConnectorLabel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][\w!@#.-]+`
- **Max Length**: 256

### ConnectorMode
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ConnectorName
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### ConnectorOwner
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### ConnectorProfileArn
- **Type**: string
- **Pattern**: `arn:aws:appflow:.*:[0-9]+:.*`
- **Max Length**: 512

### ConnectorProfileName
- **Type**: string
- **Pattern**: `[\w/!@#+=.-]+`
- **Max Length**: 256

### ConnectorRuntimeSettingDataType
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ConnectorRuntimeSettingScope
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ConnectorSuppliedValue
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ConnectorVersion
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### CreatedBy
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### CredentialsMapKey
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 1
- **Max Length**: 128

### CredentialsMapValue
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 2048

### CustomAuthenticationType
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### CustomPropertyKey
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 1
- **Max Length**: 128

### CustomPropertyValue
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 2048

### DataApiRoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam:.*:[0-9]+:.*`
- **Max Length**: 512

### DataTransferApiTypeName
- **Type**: string
- **Pattern**: `[\w/-]+`
- **Max Length**: 64

### DatabaseName
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### DatabaseUrl
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### DatetimeTypeFieldName
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### Description
- **Type**: string
- **Pattern**: `[\s\w/!@#+=.-]*`
- **Max Length**: 1024

### DestinationField
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### DocumentType
- **Type**: string
- **Pattern**: `[\s\w_-]+`
- **Max Length**: 512

### DomainName
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 64

### EntitiesPath
- **Type**: string
- **Pattern**: `[\s\w/!@#+=,.-]*`
- **Max Length**: 256

### EntityName
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 1024

### ErrorMessage
- **Type**: string
- **Pattern**: `[\s\w/!@#+=.-]*`
- **Max Length**: 2048

### ExecutionId
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### ExecutionMessage
- **Type**: string
- **Pattern**: `[\s\w/!@#+=.-]*`
- **Max Length**: 2048

### FlowArn
- **Type**: string
- **Pattern**: `arn:aws:appflow:.*:[0-9]+:.*`
- **Max Length**: 512

### FlowDescription
- **Type**: string
- **Pattern**: `[\w!@#\-.?,\s]*`
- **Max Length**: 2048

### FlowName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][\w!@#.-]+`
- **Max Length**: 256

### FlowStatusMessage
- **Type**: string
- **Pattern**: `[\s\w/!@#+=.-]*`
- **Max Length**: 2048

### GlueDataCatalogDatabaseName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Max Length**: 255

### GlueDataCatalogIAMRole
- **Type**: string
- **Pattern**: `arn:aws:iam:.*:[0-9]+:.*`
- **Max Length**: 512

### GlueDataCatalogTablePrefix
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Max Length**: 128

### Group
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 128

### Identifier
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 128

### InstanceUrl
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### JwtToken
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)`
- **Max Length**: 8000

### KMSArn
- **Type**: string
- **Pattern**: `arn:aws:kms:.*:[0-9]+:.*`
- **Min Length**: 20
- **Max Length**: 2048

### Key
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### Label
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 128

### LogoURL
- **Type**: string
- **Pattern**: `^(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
- **Max Length**: 256

### LogonLanguage
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]*$`
- **Max Length**: 2

### MostRecentExecutionMessage
- **Type**: string
- **Pattern**: `[\w!@#\-.?,\s]*`
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 128

### NextToken
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 2048

### OAuthScope
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 128

### Object
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### ObjectTypeName
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 255

### Password
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 512

### PrivateConnectionProvisioningFailureMessage
- **Type**: string
- **Pattern**: `[\s\w/!@#+=.-]*`
- **Max Length**: 2048

### PrivateLinkServiceName
- **Type**: string
- **Pattern**: `^$|com.amazonaws.vpce.[\w/!:@#.\-]+`
- **Max Length**: 512

### ProfilePropertyKey
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 1
- **Max Length**: 128

### ProfilePropertyValue
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 2048

### Property
- **Type**: string
- **Pattern**: `.+`
- **Max Length**: 2048

### RedirectUri
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### RefreshToken
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 4096

### Region
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 64

### RegisteredBy
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam:.*:[0-9]+:.*`
- **Max Length**: 512

### ScheduleExpression
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### SecretKey
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### Stage
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### String
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 2048

### SupportedApiVersion
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\s\w+-=\.:/@]*`
- **Max Length**: 256

### Timezone
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### TokenUrl
- **Type**: string
- **Pattern**: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
- **Max Length**: 256

### UpdatedBy
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 256

### UpsolverBucketName
- **Type**: string
- **Pattern**: `^(upsolver-appflow)\S*`
- **Min Length**: 16
- **Max Length**: 63

### Username
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### Value
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 128

### Warehouse
- **Type**: string
- **Pattern**: `[\s\w/!@#+=.-]*`
- **Max Length**: 512

### WorkgroupName
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

