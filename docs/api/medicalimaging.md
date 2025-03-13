# Medicalimaging Service

### Arn
- **Type**: string
- **Pattern**: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:medical-imaging:[a-z0-9-]+:[0-9]{12}:datastore/[0-9a-z]{32}(/imageset/[0-9a-z]{32})?`

### AwsAccountId
- **Type**: string
- **Pattern**: `\d+`
- **Min Length**: 12
- **Max Length**: 12

### ClientToken
- **Type**: string
- **Pattern**: `[A-Za-z0-9._-]+`
- **Min Length**: 1
- **Max Length**: 64

### DICOMSeriesInstanceUID
- **Type**: string
- **Pattern**: `(?:[0-9][0-9]*|0)(\.(?:[1-9][0-9]*|0))*`
- **Min Length**: 0
- **Max Length**: 256

### DICOMStudyInstanceUID
- **Type**: string
- **Pattern**: `(?:[0-9][0-9]*|0)(\.(?:[1-9][0-9]*|0))*`
- **Min Length**: 0
- **Max Length**: 256

### DatastoreId
- **Type**: string
- **Pattern**: `[0-9a-z]{32}`

### DatastoreName
- **Type**: string
- **Pattern**: `[A-Za-z0-9._/#-]+`
- **Min Length**: 1
- **Max Length**: 256

### ImageFrameId
- **Type**: string
- **Pattern**: `[0-9a-z]{32}`

### ImageSetExternalVersionId
- **Type**: string
- **Pattern**: `\d+`

### ImageSetId
- **Type**: string
- **Pattern**: `[0-9a-z]{32}`

### JobId
- **Type**: string
- **Pattern**: `[0-9a-z]+`
- **Min Length**: 1
- **Max Length**: 32

### JobName
- **Type**: string
- **Pattern**: `[A-Za-z0-9._/#-]+`
- **Min Length**: 1
- **Max Length**: 64

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws[a-zA-Z-]{0,16}:kms:[a-z]{2}(-[a-z]{1,16}){1,3}-\d{1}:\d{12}:((key/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})|(alias/[a-zA-Z0-9:/_-]{1,256}))`
- **Min Length**: 1
- **Max Length**: 512

### Message
- **Type**: string
- **Pattern**: `[\w -:]+`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `\p{ASCII}{0,8192}`
- **Min Length**: 1
- **Max Length**: 8192

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Min Length**: 1
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[a-zA-Z+-=._:/]+`
- **Min Length**: 1
- **Max Length**: 128

