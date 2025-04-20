# Mailmanager Service

### AddonInstanceId
- **Type**: string
- **Pattern**: `^ai-[a-zA-Z0-9]{1,64}$`
- **Min Length**: 4
- **Max Length**: 67

### AddonSubscriptionId
- **Type**: string
- **Pattern**: `^as-[a-zA-Z0-9]{1,64}$`
- **Min Length**: 4
- **Max Length**: 67

### AddressListId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 255

### AddressListName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 255

### AnalyzerArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:_/+=,@.#-]+$`

### ArchiveId
- **Type**: string
- **Pattern**: `^a-[\w]{1,64}$`
- **Min Length**: 3
- **Max Length**: 66

### ArchiveNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 64

### EmailAddress
- **Type**: string
- **Pattern**: `^[0-9A-Za-z@+.-]+$`
- **Min Length**: 0
- **Max Length**: 254

### HeaderName
- **Type**: string
- **Pattern**: `^[xX]\-[a-zA-Z0-9\-]+$`
- **Min Length**: 1
- **Max Length**: 64

### IamRoleArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:_/+=,@.#-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### IdOrArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:_/+=,@.#-]+$`
- **Min Length**: 1
- **Max Length**: 2048

### IngressPointName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_\-]+$`
- **Min Length**: 3
- **Max Length**: 63

### Ipv4Cidr
- **Type**: string
- **Pattern**: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([0-9]|[12][0-9]|3[0-2])$`

### JobId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 255

### JobName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 255

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):kms:[a-z0-9-]{1,20}:[0-9]{12}:(key|alias)/.+$`

### KmsKeyId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-:/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### MimeHeaderAttribute
- **Type**: string
- **Pattern**: `^X-[a-zA-Z0-9-]{1,256}$`

### NameOrArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:_/+=,@.#-]+$`
- **Min Length**: 1
- **Max Length**: 2048

### QBusinessApplicationId
- **Type**: string
- **Pattern**: `^[a-z0-9-]+$`
- **Min Length**: 36
- **Max Length**: 36

### QBusinessIndexId
- **Type**: string
- **Pattern**: `^[a-z0-9-]+$`
- **Min Length**: 36
- **Max Length**: 36

### RelayId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 100

### RelayName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 100

### RelayServerName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-\.]+$`
- **Min Length**: 1
- **Max Length**: 100

### ResultField
- **Type**: string
- **Pattern**: `^[\sa-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 256

### RuleIpStringValue
- **Type**: string
- **Pattern**: `^(([0-9]|.|/)*)$`
- **Min Length**: 1
- **Max Length**: 18

### RuleName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 32

### RuleSetName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 100

### S3Bucket
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9.-]+$`
- **Min Length**: 1
- **Max Length**: 62

### S3Location
- **Type**: string
- **Pattern**: `^s3://[a-zA-Z0-9.-]{3,63}(/[a-zA-Z0-9!_.*\'()/-]*)*$`

### S3Prefix
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9!_.*\'()/-]+$`
- **Min Length**: 1
- **Max Length**: 62

### SecretArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+$`

### SmtpPassword
- **Type**: string
- **Pattern**: `^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{}|.,?]+$`
- **Min Length**: 8
- **Max Length**: 64

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_\+=\.:@\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_\+=\.:@\-]*$`
- **Min Length**: 0
- **Max Length**: 256

### TaggableResourceArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):ses:[a-z0-9-]{1,20}:[0-9]{12}:(mailmanager-|addon-).+$`
- **Min Length**: 20
- **Max Length**: 1011

### TrafficPolicyName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_\-]+$`
- **Min Length**: 3
- **Max Length**: 63

