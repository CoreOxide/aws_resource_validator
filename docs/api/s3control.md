# S3control Service

### AccessGrantArn
- **Type**: string
- **Pattern**: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/grant/[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 2048

### AccessGrantId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 64

### AccessGrantsInstanceArn
- **Type**: string
- **Pattern**: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 2048

### AccessGrantsInstanceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 64

### AccessGrantsLocationArn
- **Type**: string
- **Pattern**: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/location/[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 2048

### AccessGrantsLocationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 64

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Max Length**: 64

### Alias
- **Type**: string
- **Pattern**: `^[0-9a-z\\-]{63}`
- **Max Length**: 63

### AsyncRequestTokenARN
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 1024

### AwsOrgArn
- **Type**: string
- **Pattern**: `arn:[a-z\-]+:organizations::\d{12}:organization\/o-[a-z0-9]{10,32}`
- **Min Length**: 1
- **Max Length**: 1024

### ConfigId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-\_\.]+`
- **Min Length**: 1
- **Max Length**: 64

### FunctionArnString
- **Type**: string
- **Pattern**: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
- **Min Length**: 1
- **Max Length**: 1024

### IAMRoleArn
- **Type**: string
- **Pattern**: `arn:[^:]+:iam::\d{12}:role/.*`
- **Min Length**: 1
- **Max Length**: 2048

### IdentityCenterApplicationArn
- **Type**: string
- **Pattern**: `arn:[^:]+:sso:.*$`
- **Min Length**: 10
- **Max Length**: 1224

### IdentityCenterArn
- **Type**: string
- **Pattern**: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`
- **Min Length**: 10
- **Max Length**: 1224

### JobArn
- **Type**: string
- **Pattern**: `arn:[^:]+:s3:[a-zA-Z0-9\-]+:\d{12}:job\/.*`
- **Min Length**: 1
- **Max Length**: 1024

### JobId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-\_]+`
- **Min Length**: 5
- **Max Length**: 36

### MultiRegionAccessPointAlias
- **Type**: string
- **Pattern**: `^[a-z][a-z0-9]*[.]mrap$`
- **Max Length**: 63

### MultiRegionAccessPointClientToken
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 64

### MultiRegionAccessPointId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\:.-]{3,200}$`
- **Max Length**: 200

### MultiRegionAccessPointName
- **Type**: string
- **Pattern**: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`
- **Max Length**: 50

### ObjectLambdaAccessPointAliasValue
- **Type**: string
- **Pattern**: `^[0-9a-z\\-]{3,63}`
- **Min Length**: 3
- **Max Length**: 63

### ObjectLambdaAccessPointArn
- **Type**: string
- **Pattern**: `arn:[^:]+:s3-object-lambda:[^:]*:\d{12}:accesspoint/.*`
- **Min Length**: 1
- **Max Length**: 2048

### ObjectLambdaAccessPointName
- **Type**: string
- **Pattern**: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
- **Min Length**: 3
- **Max Length**: 45

### ObjectLambdaSupportingAccessPointArn
- **Type**: string
- **Pattern**: `arn:[^:]+:s3:[^:]*:\d{12}:accesspoint/.*`
- **Min Length**: 1
- **Max Length**: 2048

### Organization
- **Type**: string
- **Pattern**: `^o-[a-z0-9]{10,32}$`
- **Min Length**: 12
- **Max Length**: 34

### S3AWSRegion
- **Type**: string
- **Pattern**: `[a-z0-9\-]+`
- **Min Length**: 5
- **Max Length**: 30

### S3BucketArnString
- **Type**: string
- **Pattern**: `arn:[^:]+:s3:.*`
- **Min Length**: 1
- **Max Length**: 128

### S3KeyArnString
- **Type**: string
- **Pattern**: `arn:[^:]+:s3:.*`
- **Min Length**: 1
- **Max Length**: 2000

### S3Prefix
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 2000

### S3RegionalOrS3ExpressBucketArnString
- **Type**: string
- **Pattern**: `arn:[^:]+:(s3|s3express):.*`
- **Min Length**: 1
- **Max Length**: 128

### S3ResourceArn
- **Type**: string
- **Pattern**: `arn:[^:]+:s3:[^:].*`
- **Max Length**: 1011

### StorageLensArn
- **Type**: string
- **Pattern**: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\/.*`
- **Min Length**: 1
- **Max Length**: 1024

### StorageLensGroupArn
- **Type**: string
- **Pattern**: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\-group\/.*`
- **Min Length**: 4
- **Max Length**: 1024

### StorageLensGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-\_]+`
- **Min Length**: 1
- **Max Length**: 64

### StringForNextToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`
- **Min Length**: 1
- **Max Length**: 1024

### TagKeyString
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValueString
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

