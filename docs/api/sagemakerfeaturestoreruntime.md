# Sagemakerfeaturestoreruntime Service

### FeatureGroupNameOrArn
- **Type**: string
- **Pattern**: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
- **Min Length**: 1
- **Max Length**: 150

### FeatureName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
- **Min Length**: 1
- **Max Length**: 64

### ValueAsString
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 358400

