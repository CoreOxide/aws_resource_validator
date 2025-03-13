# B2bi Service

### CapabilityId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### Email
- **Type**: string
- **Pattern**: `[\w\.\-]+@[\w\.\-]+`
- **Min Length**: 5
- **Max Length**: 254

### PartnershipId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### Phone
- **Type**: string
- **Pattern**: `\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?`
- **Min Length**: 7
- **Max Length**: 22

### ProfileId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### TradingPartnerId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### TransformerId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### TransformerJobId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 25
- **Max Length**: 25

### TransformerName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]{1,512}`
- **Min Length**: 1
- **Max Length**: 254

### X12AcknowledgmentRequestedCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 1

### X12ApplicationReceiverCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 ]*`
- **Min Length**: 2
- **Max Length**: 15

### X12ApplicationSenderCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 ]*`
- **Min Length**: 2
- **Max Length**: 15

### X12ComponentSeparator
- **Type**: string
- **Pattern**: `[!&\'()*+,\-./:;?=%@\[\]_{}|<>~^`"]`
- **Min Length**: 1
- **Max Length**: 1

### X12DataElementSeparator
- **Type**: string
- **Pattern**: `[!&\'()*+,\-./:;?=%@\[\]_{}|<>~^`"]`
- **Min Length**: 1
- **Max Length**: 1

### X12IdQualifier
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 2
- **Max Length**: 2

### X12ReceiverId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 ]*`
- **Min Length**: 15
- **Max Length**: 15

### X12ResponsibleAgencyCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 2

### X12SegmentTerminator
- **Type**: string
- **Pattern**: `[!&\'()*+,\-./:;?=%@\[\]_{}|<>~^`"]`
- **Min Length**: 1
- **Max Length**: 1

### X12SenderId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 ]*`
- **Min Length**: 15
- **Max Length**: 15

### X12UsageIndicatorCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 1

