# Macie2 Service

### ClassificationScopeId
- **Type**: string
- **Pattern**: `^[0-9a-z]*$`

### ClassificationScopeName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_\\-]*$`

### NextToken
- **Type**: string
- **Pattern**: `^.*$`

### S3BucketName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9.\-_]{3,255}$`

### __stringMin1Max1024PatternSS
- **Type**: string
- **Pattern**: `^[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 1024

### __stringMin1Max128Pattern
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 128

### __stringMin1Max512PatternSS
- **Type**: string
- **Pattern**: `^[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 512

### __stringMin1Max64PatternW
- **Type**: string
- **Pattern**: `^[\w+=,.@-]*$`
- **Min Length**: 1
- **Max Length**: 64

### __stringMin22Max22PatternAZ0922
- **Type**: string
- **Pattern**: `^[a-z0-9]{22}$`
- **Min Length**: 22
- **Max Length**: 22

### __stringMin3Max255PatternAZaZ093255
- **Type**: string
- **Pattern**: `^[A-Za-z0-9.\-_]{3,255}$`
- **Min Length**: 3
- **Max Length**: 255

### __stringMin71Max89PatternArnAwsAwsCnAwsUsGovMacie2AZ19920D12AllowListAZ0922
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):macie2:[a-z1-9-]{9,20}:\d{12}:allow-list\/[a-z0-9]{22}$`
- **Min Length**: 71
- **Max Length**: 89

