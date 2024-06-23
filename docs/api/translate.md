# Translate Service

### BoundedLengthString
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,10000}`
- **Min Length**: 1
- **Max Length**: 10000

### ClientTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ContentType
- **Type**: string
- **Pattern**: `^[-\w.]+\/[-\w.+]+$`
- **Max Length**: 256

### Description
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{0,256}`
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
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `\p{ASCII}{0,8192}`
- **Max Length**: 8192

### ResourceName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9-]_?)+$`
- **Min Length**: 1
- **Max Length**: 256

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Max Length**: 1024

### String
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{0,10000}`
- **Max Length**: 10000

### TranslatedTextString
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{0,20000}`
- **Max Length**: 20000

