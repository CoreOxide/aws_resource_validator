# Alexaforbusiness Service

### AddressBookDescription
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 200

### AddressBookName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### AmazonId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{1,18}`

### Arn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

### AudioLocation
- **Type**: string
- **Pattern**: `https://([A-Za-z0-9_.-]+)?(s3-[A-Za-z0-9-]+|s3\.([A-Za-z0-9-])+|s3|s3.dualstack\.([A-Za-z0-9-])+)+.amazonaws.com/.*`
- **Min Length**: 0
- **Max Length**: 1200

### BusinessReportScheduleName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 64

### ClientId
- **Type**: string
- **Pattern**: `^\S+{1,256}$`

### ClientRequestToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 10
- **Max Length**: 150

### ConferenceProviderName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 50

### ContactName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### CountryCode
- **Type**: string
- **Pattern**: `\d{1,3}`

### CurrentWiFiPassword
- **Type**: string
- **Pattern**: `[\x00-\x7F]*`
- **Min Length**: 5
- **Max Length**: 128

### CustomerS3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9-\.]{3,63}`

### Date
- **Type**: string
- **Pattern**: `^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$`

### DeviceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 2
- **Max Length**: 100

### DeviceRoomName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### DeviceSerialNumber
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{1,200}`

### DeviceSerialNumberForAVS
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{1,50}$`

### DeviceType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{1,200}`

### Email
- **Type**: string
- **Pattern**: `\w[+-.\w]*@\w[\w\.\-]+\.[0-9a-zA-Z]{2,24}`
- **Min Length**: 1
- **Max Length**: 128

### GatewayDescription
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 200

### GatewayGroupName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### GatewayName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 253

### NetworkProfileDescription
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 200

### NetworkProfileName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### NetworkSsid
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 32

### NextWiFiPassword
- **Type**: string
- **Pattern**: `(^$)|([\x00-\x7F]{5,})`
- **Min Length**: 0
- **Max Length**: 128

### OrganizationName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### OutboundPhoneNumber
- **Type**: string
- **Pattern**: `\d{10}`

### ProductId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]{1,256}$`

### ProfileName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### RawPhoneNumber
- **Type**: string
- **Pattern**: `^[\+0-9\#\,\(][\+0-9\-\.\/\(\)\,\#\s]+$`
- **Min Length**: 0
- **Max Length**: 50

### RoomDescription
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 200

### RoomName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### S3KeyPrefix
- **Type**: string
- **Pattern**: `[A-Za-z0-9!_\-\.\*\'()/]*`
- **Min Length**: 0
- **Max Length**: 100

### SipUri
- **Type**: string
- **Pattern**: `^sip[s]?:([^@:]+)\@([^@]+)$`
- **Min Length**: 1
- **Max Length**: 256

### SkillGroupDescription
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 200

### SkillGroupName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### SkillId
- **Type**: string
- **Pattern**: `(^amzn1\.ask\.skill\.[0-9a-f\-]{1,200})|(^amzn1\.echo-sdk-ams\.app\.[0-9a-f\-]{1,200})`

### SkillName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 100

### SkillType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### SsmlValue
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 4096

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

### TextValue
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 4096

### TrustAnchor
- **Type**: string
- **Pattern**: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`

### UserId
- **Type**: string
- **Pattern**: `amzn1\.[A-Za-z0-9+-\/=.]{1,300}`

### userFirstName
- **Type**: string
- **Pattern**: `([A-Za-z\-\' 0-9._]|\p{IsLetter})*`
- **Min Length**: 0
- **Max Length**: 30

### userLastName
- **Type**: string
- **Pattern**: `([A-Za-z\-\' 0-9._]|\p{IsLetter})*`
- **Min Length**: 0
- **Max Length**: 30

### userUserId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9@_+.-]*`
- **Min Length**: 1
- **Max Length**: 128

