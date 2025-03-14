# Autoscaling Service

### AllowedInstanceType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\*\-]+`
- **Min Length**: 1
- **Max Length**: 30

### AnyPrintableAsciiStringMaxLen4000
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007e]+`
- **Min Length**: 1
- **Max Length**: 4000

### AsciiStringMaxLen255
- **Type**: string
- **Pattern**: `[A-Za-z0-9\-_\/]+`
- **Min Length**: 1
- **Max Length**: 255

### ExcludedInstance
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\*\-]+`
- **Min Length**: 1
- **Max Length**: 30

### LaunchTemplateName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\(\)\.\-/_]+`
- **Min Length**: 3
- **Max Length**: 128

### NotificationTargetResourceName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 255

### ResourceName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 1600

### TagKey
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 256

### UpdatePlacementGroupParam
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 255

### XmlString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

### XmlStringMaxLen1023
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 1023

### XmlStringMaxLen1600
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 1600

### XmlStringMaxLen19
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 19

### XmlStringMaxLen2047
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 2047

### XmlStringMaxLen255
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 255

### XmlStringMaxLen32
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 32

### XmlStringMaxLen5000
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 5000

### XmlStringMaxLen511
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 511

### XmlStringMaxLen64
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 64

### XmlStringMetricLabel
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Max Length**: 2047

### XmlStringMetricStat
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 100

### XmlStringUserData
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Max Length**: 21847

