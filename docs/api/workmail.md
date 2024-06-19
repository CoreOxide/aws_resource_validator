# Workmail Service

### AccessControlRuleAction
- **Type**: string
- **Pattern**: `[a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 64

### AccessControlRuleDescription
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 0
- **Max Length**: 255

### AccessControlRuleName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### AmazonResourceName
- **Type**: string
- **Pattern**: `arn:aws:workmail:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
- **Min Length**: 1
- **Max Length**: 1011

### Description
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1023

### DeviceId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 32

### DeviceModel
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 256

### DeviceOperatingSystem
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 256

### DeviceType
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 256

### DeviceUserAgent
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 256

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$`
- **Min Length**: 12
- **Max Length**: 12

### DomainName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9.-]+`
- **Min Length**: 3
- **Max Length**: 255

### EmailAddress
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`
- **Min Length**: 1
- **Max Length**: 254

### EntityIdentifier
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._%+@-]+`
- **Min Length**: 1
- **Max Length**: 256

### ExternalUserName
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Max Length**: 256

### GroupName
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 256

### HostedZoneId
- **Type**: string
- **Pattern**: `[^/\\]*`
- **Min Length**: 1
- **Max Length**: 32

### IdempotencyClientToken
- **Type**: string
- **Pattern**: `[\x21-\x7e]+`
- **Min Length**: 1
- **Max Length**: 128

### ImpersonationRoleDescription
- **Type**: string
- **Pattern**: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F\x3C\x3E\x5C]+`
- **Min Length**: 1
- **Max Length**: 256

### ImpersonationRoleId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ImpersonationRoleName
- **Type**: string
- **Pattern**: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`
- **Min Length**: 1
- **Max Length**: 64

### ImpersonationRuleDescription
- **Type**: string
- **Pattern**: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F\x3C\x3E\x5C]+`
- **Min Length**: 1
- **Max Length**: 256

### ImpersonationRuleId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ImpersonationRuleName
- **Type**: string
- **Pattern**: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`
- **Min Length**: 1
- **Max Length**: 64

### ImpersonationToken
- **Type**: string
- **Pattern**: `[\x21-\x7e]+`
- **Min Length**: 1
- **Max Length**: 256

### IpAddress
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`
- **Min Length**: 1
- **Max Length**: 15

### IpRange
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[12][0-9]|3[0-2])$`
- **Min Length**: 1
- **Max Length**: 18

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws:kms:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
- **Min Length**: 20
- **Max Length**: 2048

### LambdaArn
- **Type**: string
- **Pattern**: `arn:aws:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9\-_\.]+(:(\$LATEST|[a-zA-Z0-9\-_]+))?`
- **Min Length**: 49
- **Max Length**: 256

### LogGroupArn
- **Type**: string
- **Pattern**: `arn:aws:logs:[a-z\-0-9]*:[0-9]{12}:log-group:([\.\-_/#A-Za-z0-9]+):\*$`
- **Min Length**: 47
- **Max Length**: 562

### MailboxExportErrorInfo
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 1
- **Max Length**: 1024

### MailboxExportJobId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 63

### MobileDeviceAccessRuleDescription
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Min Length**: 1
- **Max Length**: 256

### MobileDeviceAccessRuleId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### MobileDeviceAccessRuleName
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Min Length**: 1
- **Max Length**: 64

### NextToken
- **Type**: string
- **Pattern**: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`
- **Min Length**: 1
- **Max Length**: 1024

### OrganizationId
- **Type**: string
- **Pattern**: `^m-[0-9a-f]{32}$`
- **Min Length**: 34
- **Max Length**: 34

### OrganizationName
- **Type**: string
- **Pattern**: `^(?!d-)([\da-zA-Z]+)([-][\da-zA-Z]+)*`
- **Min Length**: 1
- **Max Length**: 62

### Password
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Max Length**: 256

### PolicyDescription
- **Type**: string
- **Pattern**: `[\w\d\s\S\-!?=,.;:\'_]+`
- **Max Length**: 256

### ResourceId
- **Type**: string
- **Pattern**: `^r-[0-9a-f]{32}$`
- **Min Length**: 34
- **Max Length**: 34

### ResourceName
- **Type**: string
- **Pattern**: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`
- **Min Length**: 1
- **Max Length**: 20

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
- **Min Length**: 20
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `[A-Za-z0-9.-]+`
- **Min Length**: 1
- **Max Length**: 63

### S3ObjectKey
- **Type**: string
- **Pattern**: `[A-Za-z0-9!_.*\'()/-]+`
- **Min Length**: 1
- **Max Length**: 1023

### ShortString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### Url
- **Type**: string
- **Pattern**: `https?://[A-Za-z0-9.-]+(:[0-9]+)?/.*`
- **Max Length**: 256

### UserName
- **Type**: string
- **Pattern**: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`
- **Min Length**: 1
- **Max Length**: 64

### WorkMailDomainName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9.-]+`
- **Min Length**: 3
- **Max Length**: 209

