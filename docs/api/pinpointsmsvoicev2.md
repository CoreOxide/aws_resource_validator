# Pinpointsmsvoicev2 Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `arn:[A-Za-z0-9_:/-]+`
- **Min Length**: 20
- **Max Length**: 256

### AttachmentUrl
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 2048

### ClientToken
- **Type**: string
- **Pattern**: `[!-~]+`
- **Min Length**: 1
- **Max Length**: 64

### ConfigurationSetName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ConfigurationSetNameOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### ContextKey
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 100

### ContextValue
- **Type**: string
- **Pattern**: `(?!\s)^[\s\S]+(?<!\s)`
- **Min Length**: 1
- **Max Length**: 800

### DeliveryStreamArn
- **Type**: string
- **Pattern**: `arn:\S+`
- **Min Length**: 20
- **Max Length**: 2048

### DestinationCountryParameterValue
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 64

### EventDestinationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### FieldPath
- **Type**: string
- **Pattern**: `[A-Za-z0-9_\.]+`
- **Min Length**: 1
- **Max Length**: 100

### FilterValue
- **Type**: string
- **Pattern**: `[/\.:A-Za-z0-9+_-]+`
- **Min Length**: 1
- **Max Length**: 128

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:\S+`
- **Min Length**: 20
- **Max Length**: 2048

### IsoCountryCode
- **Type**: string
- **Pattern**: `[A-Z]{2}`
- **Min Length**: 2
- **Max Length**: 2

### Keyword
- **Type**: string
- **Pattern**: `[ \S]+`
- **Min Length**: 1
- **Max Length**: 30

### KeywordMessage
- **Type**: string
- **Pattern**: `(?!\s*$)[\s\S]+`
- **Min Length**: 1
- **Max Length**: 1600

### LogGroupArn
- **Type**: string
- **Pattern**: `arn:\S+`
- **Min Length**: 20
- **Max Length**: 2048

### MaxPrice
- **Type**: string
- **Pattern**: `[0-9]{0,2}\.[0-9]{1,5}`
- **Min Length**: 2
- **Max Length**: 8

### MediaMessageOriginationIdentity
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/\+-]+`
- **Min Length**: 1
- **Max Length**: 256

### MediaUrlValue
- **Type**: string
- **Pattern**: `s3://([a-z0-9\.-]{3,63})/(.+)`
- **Min Length**: 1
- **Max Length**: 2048

### MessageId
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 64

### NextToken
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024

### OptOutListName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### OptOutListNameOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### PhoneNumber
- **Type**: string
- **Pattern**: `\+?[1-9][0-9]{1,18}`
- **Min Length**: 1
- **Max Length**: 20

### PhoneNumberIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### PhoneOrPoolIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### PhoneOrSenderIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### PoolIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### ProtectConfigurationArn
- **Type**: string
- **Pattern**: `arn:\S+`
- **Min Length**: 1
- **Max Length**: 256

### ProtectConfigurationId
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ProtectConfigurationIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### RegistrationAttachmentIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### RegistrationIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### RegistrationType
- **Type**: string
- **Pattern**: `[A-Za-z0-9_]+`
- **Min Length**: 1
- **Max Length**: 64

### ResourceIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### SectionPath
- **Type**: string
- **Pattern**: `[A-Za-z0-9_]+`
- **Min Length**: 1
- **Max Length**: 100

### SenderId
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 11

### SenderIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### SnsTopicArn
- **Type**: string
- **Pattern**: `arn:\S+`
- **Min Length**: 20
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256

### TextMessageBody
- **Type**: string
- **Pattern**: `(?!\s*$)[\s\S]+`
- **Min Length**: 1
- **Max Length**: 1600

### TextMessageOriginationIdentity
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/\+-]+`
- **Min Length**: 1
- **Max Length**: 256

### TwoWayChannelArn
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 20
- **Max Length**: 2048

### VerificationCode
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 20

### VerificationMessageOriginationIdentity
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/\+-]+`
- **Min Length**: 1
- **Max Length**: 256

### VerifiedDestinationNumberIdOrArn
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### VoiceMessageBody
- **Type**: string
- **Pattern**: `(?!\s*$)[\s\S]+`
- **Min Length**: 1
- **Max Length**: 6000

### VoiceMessageOriginationIdentity
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:/\+-]+`
- **Min Length**: 1
- **Max Length**: 256

