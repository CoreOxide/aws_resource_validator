# Sagemakera2iruntime Service

### FlowDefinitionArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:flow-definition/.*`
- **Max Length**: 1024

### HumanLoopArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:human-loop/.*`
- **Max Length**: 1024

### HumanLoopName
- **Type**: string
- **Pattern**: `^[a-z0-9](-*[a-z0-9])*$`
- **Min Length**: 1
- **Max Length**: 63

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 8192

