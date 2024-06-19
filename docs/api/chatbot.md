# Chatbot Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
- **Min Length**: 12
- **Max Length**: 1224

### AwsUserIdentity
- **Type**: string
- **Pattern**: `^arn:aws:(iam|sts)::[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
- **Min Length**: 15
- **Max Length**: 1101

### ChatConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
- **Min Length**: 19
- **Max Length**: 1169

### ChimeWebhookUrl
- **Type**: string
- **Pattern**: `^https://hooks\.chime\.aws/incomingwebhooks/[A-Za-z0-9\-]+?\?token=[A-Za-z0-9\-]+$`
- **Min Length**: 1
- **Max Length**: 255

### ConfigurationName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 128

### CustomerCwLogLevel
- **Type**: string
- **Pattern**: `^(ERROR|INFO|NONE)$`
- **Min Length**: 4
- **Max Length**: 5

### GuardrailPolicyArn
- **Type**: string
- **Pattern**: `^(^$|(?!.*\/aws-service-role\/.*)arn:aws:iam:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\/+=,@.-]{0,1023})$`
- **Min Length**: 11
- **Max Length**: 1163

### PaginationToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}$`
- **Min Length**: 1
- **Max Length**: 1276

### SlackChannelId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 255

### SlackTeamId
- **Type**: string
- **Pattern**: `^[0-9A-Z]{1,255}$`
- **Min Length**: 1
- **Max Length**: 255

### SlackUserId
- **Type**: string
- **Pattern**: `^(.*)$`
- **Min Length**: 1
- **Max Length**: 255

### TeamName
- **Type**: string
- **Pattern**: `^(.*)$`
- **Min Length**: 1
- **Max Length**: 255

### TeamsChannelId
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9-_=+\/.,])*%3[aA]([a-zA-Z0-9-_=+\/.,])*%40([a-zA-Z0-9-_=+\/.,])*$`
- **Min Length**: 1
- **Max Length**: 255

### TeamsChannelName
- **Type**: string
- **Pattern**: `^(.*)$`
- **Min Length**: 1
- **Max Length**: 1000

### UUID
- **Type**: string
- **Pattern**: `^[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}$`
- **Min Length**: 36
- **Max Length**: 36

