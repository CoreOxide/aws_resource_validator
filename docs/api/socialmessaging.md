# Socialmessaging Service

### Arn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 0
- **Max Length**: 2048

### EventDestinationArn
- **Type**: string
- **Pattern**: `arn:.*:[a-z-]+([/:](.*))?`
- **Min Length**: 0
- **Max Length**: 2048

### IsoCountryCode
- **Type**: string
- **Pattern**: `[A-Z]{2}`

### LinkedWhatsAppBusinessAccountArn
- **Type**: string
- **Pattern**: `arn:.*:waba/[0-9a-zA-Z]+`
- **Min Length**: 0
- **Max Length**: 2048

### LinkedWhatsAppBusinessAccountId
- **Type**: string
- **Pattern**: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
- **Min Length**: 1
- **Max Length**: 100

### LinkedWhatsAppPhoneNumberArn
- **Type**: string
- **Pattern**: `arn:.*:phone-number-id/[0-9a-zA-Z]+`
- **Min Length**: 0
- **Max Length**: 2048

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::\d{12}:role\/[a-zA-Z0-9+=,.@\-_]+`

### S3FileBucketNameString
- **Type**: string
- **Pattern**: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### S3PresignedUrlUrlString
- **Type**: string
- **Pattern**: `https://(.*)s3(.*).amazonaws.com/(.*)`
- **Min Length**: 1
- **Max Length**: 2000

### WhatsAppMediaId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 100

### WhatsAppPhoneNumberId
- **Type**: string
- **Pattern**: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
- **Min Length**: 1
- **Max Length**: 100

