# Evidently Service

### AppConfigResourceId
- **Type**: string
- **Pattern**: `[a-z0-9]{4,7}`

### Arn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
- **Min Length**: 0
- **Max Length**: 2048

### CwDimensionSafeName
- **Type**: string
- **Pattern**: `^[\S]+$`
- **Min Length**: 1
- **Max Length**: 255

### CwLogGroupSafeName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._/]+$`
- **Min Length**: 1
- **Max Length**: 512

### Description
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 160

### EntityId
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 512

### ErrorMessage
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### ExperimentArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*/experiment/[-a-zA-Z0-9._]*`
- **Min Length**: 0
- **Max Length**: 2048

### ExperimentName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

### FeatureArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*/feature/[-a-zA-Z0-9._]*`
- **Min Length**: 0
- **Max Length**: 2048

### FeatureName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

### GroupName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

### JsonPath
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### LaunchArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*/launch/[-a-zA-Z0-9._]*`
- **Min Length**: 0
- **Max Length**: 2048

### LaunchName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

### MetricUnitLabel
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 8192

### ProjectArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*`
- **Min Length**: 0
- **Max Length**: 2048

### ProjectName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

### ProjectRef
- **Type**: string
- **Pattern**: `(^[a-zA-Z0-9._-]*$)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[a-zA-Z0-9._-]*)`
- **Min Length**: 0
- **Max Length**: 2048

### RandomizationSalt
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 127

### S3BucketSafeName
- **Type**: string
- **Pattern**: `^[a-z0-9][-a-z0-9]*[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### S3PrefixSafeName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9!_.*\'()/]*$`
- **Min Length**: 1
- **Max Length**: 1024

### SegmentArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:segment/[-a-zA-Z0-9._]*`
- **Min Length**: 0
- **Max Length**: 2048

### SegmentName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 64

### SegmentRef
- **Type**: string
- **Pattern**: `(^[-a-zA-Z0-9._]*$)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:segment/[-a-zA-Z0-9._]*)`
- **Min Length**: 0
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TreatmentName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

### Uuid
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### VariationName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9._]*$`
- **Min Length**: 1
- **Max Length**: 127

