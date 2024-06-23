# Autoscalingplans Service

### PolicyName
- **Type**: string
- **Pattern**: `\p{Print}+`
- **Min Length**: 1
- **Max Length**: 256

### ResourceIdMaxLen1600
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 1600

### ScalingPlanName
- **Type**: string
- **Pattern**: `[\p{Print}&&[^|:/]]+`
- **Min Length**: 1
- **Max Length**: 128

### XmlString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

### XmlStringMaxLen128
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 128

### XmlStringMaxLen256
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 256

