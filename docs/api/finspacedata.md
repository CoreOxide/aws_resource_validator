# Finspacedata Service

### AccessKeyId
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 255

### AliasString
- **Type**: string
- **Pattern**: `^alias\/\S+`
- **Min Length**: 1
- **Max Length**: 255

### ClientToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### ColumnDescription
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 512

### ColumnName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Max Length**: 126

### DatasetDescription
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 1000

### DatasetTitle
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 255

### Email
- **Type**: string
- **Pattern**: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}`
- **Min Length**: 4
- **Max Length**: 320

### FirstName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 50

### LastName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 50

### OwnerName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 250

### Password
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 8
- **Max Length**: 20

### PermissionGroupDescription
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 4000

### PermissionGroupId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 26

### PermissionGroupName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 255

### PhoneNumber
- **Type**: string
- **Pattern**: `^[\+0-9\#\,\(][\+0-9\-\.\/\(\)\,\#\s]+$`
- **Min Length**: 10
- **Max Length**: 20

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1
- **Max Length**: 1024

### SecretAccessKey
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 1000

### SessionToken
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 1000

### StringMapKey
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Max Length**: 128

### StringMapValue
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Max Length**: 1000

### StringValueLength1to250
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 250

### StringValueLength1to255
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 255

### UserId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 26

### stringValueLength1to1024
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### stringValueLength1to63
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 63

