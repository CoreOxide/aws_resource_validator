# Notifications Service

### AccountId
- **Type**: string
- **Pattern**: `\d{12}`

### Arn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:.*`

### ChannelArn
- **Type**: string
- **Pattern**: `arn:aws:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+`

### ChannelIdentifier
- **Type**: string
- **Pattern**: `ACCOUNT_PRIMARY|ACCOUNT_ALTERNATE_BILLING|ACCOUNT_ALTERNATE_OPERATIONS|ACCOUNT_ALTERNATE_SECURITY|arn:aws:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+`

### EventRuleArn
- **Type**: string
- **Pattern**: `arn:aws:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`

### EventType
- **Type**: string
- **Pattern**: `([a-zA-Z0-9 \-\(\)])+`
- **Min Length**: 1
- **Max Length**: 128

### ManagedNotificationChildEventArn
- **Type**: string
- **Pattern**: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}/child-event/[a-z0-9]{27}`

### ManagedNotificationConfigurationDescription
- **Type**: string
- **Pattern**: `[^\u0001-\u001F\u007F-\u009F]*`
- **Min Length**: 0
- **Max Length**: 256

### ManagedNotificationConfigurationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 64

### ManagedNotificationConfigurationOsArn
- **Type**: string
- **Pattern**: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`

### ManagedNotificationEventArn
- **Type**: string
- **Pattern**: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`

### ManagedRuleArn
- **Type**: string
- **Pattern**: `arn:aws:events:[a-z-\d]{2,25}:\d{12}:rule\/[a-zA-Z-\d]{1,1024}`

### ManagedSourceEventMetadataSummaryEventOriginRegionString
- **Type**: string
- **Pattern**: `([a-z]{1,2})-([a-z]{1,15}-)+([0-9])`
- **Min Length**: 0
- **Max Length**: 32

### ManagedSourceEventMetadataSummaryEventTypeString
- **Type**: string
- **Pattern**: `([a-zA-Z0-9 \-\(\)])+`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `[\w+-/=]+`
- **Min Length**: 1
- **Max Length**: 4096

### NotificationConfigurationArn
- **Type**: string
- **Pattern**: `arn:aws:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

### NotificationConfigurationDescription
- **Type**: string
- **Pattern**: `[^\u0001-\u001F\u007F-\u009F]*`
- **Min Length**: 0
- **Max Length**: 256

### NotificationConfigurationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_\-]+`
- **Min Length**: 1
- **Max Length**: 64

### NotificationEventArn
- **Type**: string
- **Pattern**: `arn:[-.a-z0-9]{1,63}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`

### NotificationEventId
- **Type**: string
- **Pattern**: `[a-z0-9]{27}`

### OrganizationalUnitId
- **Type**: string
- **Pattern**: `Root|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`

### Region
- **Type**: string
- **Pattern**: `([a-z]{1,2})-([a-z]{1,15}-)+([0-9])`
- **Min Length**: 2
- **Max Length**: 25

### Source
- **Type**: string
- **Pattern**: `aws.([a-z0-9\-])+`
- **Min Length**: 1
- **Max Length**: 36

### SourceEventMetadataEventOriginRegionString
- **Type**: string
- **Pattern**: `([a-z]{1,2})-([a-z]{1,15}-)+([0-9])`
- **Min Length**: 0
- **Max Length**: 32

### SourceEventMetadataEventTypeVersionString
- **Type**: string
- **Pattern**: `[0-9.]+`
- **Min Length**: 1
- **Max Length**: 3

### SourceEventMetadataRelatedAccountString
- **Type**: string
- **Pattern**: `[0-9]{12}`

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:).{1,128}`

### TextPartId
- **Type**: string
- **Pattern**: `[A-Za-z0-9_]+`
- **Min Length**: 1
- **Max Length**: 256

### Url
- **Type**: string
- **Pattern**: `(https?)://.*`
- **Min Length**: 0
- **Max Length**: 2000

