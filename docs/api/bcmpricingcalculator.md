# Bcmpricingcalculator Service

### AccountId
- **Type**: string
- **Pattern**: `\d{12}`
- **Min Length**: 12
- **Max Length**: 12

### Arn
- **Type**: string
- **Pattern**: `arn:aws[-a-z0-9]*:bcm-pricing-calculator:[-a-z0-9]*:[0-9]{12}:[-a-z0-9/:_]+`
- **Min Length**: 20
- **Max Length**: 2048

### AvailabilityZone
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9\.\-_:, \/()]*`
- **Min Length**: 0
- **Max Length**: 32

### BillEstimateName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 0
- **Max Length**: 64

### BillScenarioName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 0
- **Max Length**: 64

### ClientToken
- **Type**: string
- **Pattern**: `[\u0021-\u007E]+`
- **Min Length**: 1
- **Max Length**: 64

### Key
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 0
- **Max Length**: 10

### NextPageToken
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 2048

### Operation
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9\.\-_:, \/()]*`
- **Min Length**: 0
- **Max Length**: 32

### ResourceId
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ResourceTagKey
- **Type**: string
- **Pattern**: `[\w\s:+=@/-]+`
- **Min Length**: 1
- **Max Length**: 128

### ResourceTagValue
- **Type**: string
- **Pattern**: `[\w\s:+=@/-]*`
- **Min Length**: 0
- **Max Length**: 256

### ServiceCode
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9\.\-_:, \/()]*`
- **Min Length**: 0
- **Max Length**: 32

### UsageGroup
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 0
- **Max Length**: 30

### UsageType
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9\.\-_:, \/()]*`
- **Min Length**: 0
- **Max Length**: 128

### Uuid
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### WorkloadEstimateName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 0
- **Max Length**: 64

