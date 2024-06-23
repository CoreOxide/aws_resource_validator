# Healthlake Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-z0-9-]+:\d{12}:datastore\/fhir\/.{32}`
- **Min Length**: 1
- **Max Length**: 1011

### BoundedLengthString
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,5000}`
- **Min Length**: 1
- **Max Length**: 5000

### ClientTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### DatastoreArn
- **Type**: string
- **Pattern**: `^arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-zA-Z0-9-]+:[0-9]{12}:datastore/.+?`

### DatastoreId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 32

### DatastoreName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### EncryptionKeyID
- **Type**: string
- **Pattern**: `(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\d:)?(\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))`
- **Min Length**: 1
- **Max Length**: 400

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### JobId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 32

### JobName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 64

### LambdaArn
- **Type**: string
- **Pattern**: `arn:aws:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9\-_\.]+(:(\$LATEST|[a-zA-Z0-9\-_]+))?`
- **Min Length**: 49
- **Max Length**: 256

### Message
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `\p{ASCII}{0,8192}`
- **Max Length**: 8192

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Max Length**: 1024

### String
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{0,10000}`
- **Max Length**: 10000

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

