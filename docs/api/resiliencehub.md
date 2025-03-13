# Resiliencehub Service

### AppTemplateBody
- **Type**: string
- **Pattern**: `^[\w\s:,-\.\'\/{}\[\]:"\\]+$`
- **Min Length**: 0
- **Max Length**: 409600

### Arn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`

### AwsRegion
- **Type**: string
- **Pattern**: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]$`

### ClientToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_.-]{0,63}$`
- **Min Length**: 1
- **Max Length**: 63

### CustomerId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### EksNamespace
- **Type**: string
- **Pattern**: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`
- **Min Length**: 1
- **Max Length**: 63

### EntityId
- **Type**: string
- **Pattern**: `^\S{1,255}$`

### EntityName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`

### EntityName255
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9_\-]{0,254}$`

### EntityVersion
- **Type**: string
- **Pattern**: `^\S{1,50}$`

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):iam::[0-9]{12}:role/(([^/][!-~]+/){1,511})?[A-Za-z0-9_+=,.@-]{1,64}$`

### IamRoleName
- **Type**: string
- **Pattern**: `^([^/]([!-~]+/){1,511})?[A-Za-z0-9_+=,.@-]{1,64}$`

### NextToken
- **Type**: string
- **Pattern**: `^\S{1,2000}$`

### ResourceId
- **Type**: string
- **Pattern**: `.*`

### ResourceType
- **Type**: string
- **Pattern**: `.*`

### S3Url
- **Type**: string
- **Pattern**: `^((https://([^/]+)\.s3((-|\.)[^/]+)?\.amazonaws\.com(.cn)?)|(s3://([^/]+)))/\S{1,2000}$`
- **Min Length**: 0
- **Max Length**: 2000

### String128WithoutWhitespace
- **Type**: string
- **Pattern**: `^\S{1,128}$`

### TagKey
- **Type**: string
- **Pattern**: `^[^\x00-\x1f\x22]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[^\x00-\x1f\x22]*$`
- **Min Length**: 0
- **Max Length**: 256

### Uuid
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$`

