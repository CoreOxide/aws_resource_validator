# Ssmincidents Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+$`
- **Min Length**: 0
- **Max Length**: 1000

### GeneratedId
- **Type**: string
- **Pattern**: `^related-item/(ANALYSIS|INCIDENT|METRIC|PARENT|ATTACHMENT|OTHER|AUTOMATION|INVOLVED_RESOURCE|TASK)/([0-9]|[A-F]){32}$`
- **Min Length**: 0
- **Max Length**: 200

### ResponsePlanName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 1
- **Max Length**: 200

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-cn|-us-gov)?:iam::([0-9]{12})?:role/.+$`
- **Min Length**: 0
- **Max Length**: 1000

### SsmAutomationDocumentNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.:/]{3,128}$`

### SsmContactsArn
- **Type**: string
- **Pattern**: `^arn:aws(-cn|-us-gov)?:ssm-contacts:[a-z0-9-]*:([0-9]{12}):contact/[a-z0-9_-]+$`
- **Min Length**: 0
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[A-Za-z0-9 _=@:.+-/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[A-Za-z0-9 _=@:.+-/]*$`
- **Min Length**: 0
- **Max Length**: 256

