# Codegurureviewer Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]*:codeguru-reviewer:[^:\s]+:[\d]{12}:[a-z-]+:[\w-]+$`
- **Min Length**: 1
- **Max Length**: 1600

### AssociationArn
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]*:codeguru-reviewer:[^:\s]+:[\d]{12}:association:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 1600

### BuildArtifactsObjectKey
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 1024

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[\w-]+$`
- **Min Length**: 1
- **Max Length**: 64

### CodeReviewName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 1
- **Max Length**: 100

### ConnectionArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
- **Min Length**: 0
- **Max Length**: 256

### EventName
- **Type**: string
- **Pattern**: `^[ \-A-Z_a-z]+$`
- **Min Length**: 1
- **Max Length**: 32

### EventState
- **Type**: string
- **Pattern**: `^[ \-A-Z_a-z]+$`
- **Min Length**: 1
- **Max Length**: 32

### KMSKeyId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 2048

### LongDescription
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 1000

### Name
- **Type**: string
- **Pattern**: `^\S[\w.-]*$`
- **Min Length**: 1
- **Max Length**: 100

### Owner
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 100

### Requester
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 100

### RuleId
- **Type**: string
- **Pattern**: `^\S+\/[a-zA-Z0-9-]+@v\d+\.\d+$`
- **Min Length**: 1
- **Max Length**: 64

### RuleName
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 100

### RuleTag
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 50

### S3BucketName
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 3
- **Max Length**: 63

### ShortDescription
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 200

### SourceCodeArtifactsObjectKey
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 1024

