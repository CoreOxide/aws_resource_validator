# Emr Service

### IAMRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
- **Min Length**: 20
- **Max Length**: 2048

### InstanceType
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 256

### UriString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 10280

### XmlString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 10280

### XmlStringMaxLen256
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 256

