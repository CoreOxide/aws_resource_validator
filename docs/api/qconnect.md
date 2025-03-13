# Qconnect Service

### Arn
- **Type**: string
- **Pattern**: `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`

### ArnWithQualifier
- **Type**: string
- **Pattern**: `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}$`

### AttachmentFileName
- **Type**: string
- **Pattern**: `^[\p{L}\p{M}\p{N}_\s&@()+,;=\-]+\.[A-Za-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 256

### BedrockModelArnForParsing
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/anthropic.claude-3-haiku-20240307-v1:0$`
- **Min Length**: 1
- **Max Length**: 2048

### ContentType
- **Type**: string
- **Pattern**: `^(text/(plain|html|csv))|(application/(pdf|vnd\.openxmlformats-officedocument\.wordprocessingml\.document))|(application/x\.wisdom-json;source=(salesforce|servicenow|zendesk))$`

### Description
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s_.,-]+`
- **Min Length**: 1
- **Max Length**: 255

### EmailHeaderKey
- **Type**: string
- **Pattern**: `^[!-9;-@A-~]+$`
- **Min Length**: 1
- **Max Length**: 126

### EmailHeaderValue
- **Type**: string
- **Pattern**: `[ -~]*`
- **Min Length**: 1
- **Max Length**: 870

### GenericArn
- **Type**: string
- **Pattern**: `^arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+$`
- **Min Length**: 1
- **Max Length**: 2048

### GuardrailTopicName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z-_ !?.]+$`
- **Min Length**: 1
- **Max Length**: 100

### MessageTemplateContentSha256
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 64

### Name
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s_.,-]+`
- **Min Length**: 1
- **Max Length**: 255

### QuickResponseType
- **Type**: string
- **Pattern**: `^(application/x\.quickresponse;format=(plain|markdown))$`

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### Uuid
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### UuidOrArn
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`

### UuidOrArnOrEitherWithQualifier
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}$`

### UuidWithQualifier
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`

### WebUrl
- **Type**: string
- **Pattern**: `^https?://[A-Za-z0-9][^\s]*$`

