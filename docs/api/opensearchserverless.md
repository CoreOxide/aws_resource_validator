# Opensearchserverless Service

### CollectionId
- **Type**: string
- **Pattern**: `[a-z0-9]{3,40}`
- **Min Length**: 3
- **Max Length**: 40

### CollectionName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9-]+`
- **Min Length**: 3
- **Max Length**: 32

### ConfigName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9-]+`
- **Min Length**: 3
- **Max Length**: 32

### IamIdentityCenterApplicationArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
- **Min Length**: 10
- **Max Length**: 1224

### IamIdentityCenterInstanceArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
- **Min Length**: 10
- **Max Length**: 1224

### PolicyDocument
- **Type**: string
- **Pattern**: `.*[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+.*`
- **Min Length**: 1
- **Max Length**: 20480

### PolicyName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9-]+`
- **Min Length**: 3
- **Max Length**: 32

### PolicyVersion
- **Type**: string
- **Pattern**: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
- **Min Length**: 20
- **Max Length**: 36

### ResourceName
- **Type**: string
- **Pattern**: `index/[a-z][a-z0-9-]{3,32}/([a-z;0-9&$%][+.~=\-_a-z;0-9&$%]*)`

### SecurityGroupId
- **Type**: string
- **Pattern**: `[\w+\-]+`
- **Min Length**: 1
- **Max Length**: 128

### SubnetId
- **Type**: string
- **Pattern**: `subnet-([0-9a-f]{8}|[0-9a-f]{17})`
- **Min Length**: 1
- **Max Length**: 32

### VpcEndpointId
- **Type**: string
- **Pattern**: `vpce-[0-9a-z]*`
- **Min Length**: 1
- **Max Length**: 255

### VpcEndpointName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9-]+`
- **Min Length**: 3
- **Max Length**: 32

### VpcId
- **Type**: string
- **Pattern**: `vpc-[0-9a-z]*`
- **Min Length**: 1
- **Max Length**: 255

### openSearchServerlessEntityId
- **Type**: string
- **Pattern**: `aws:opensearch:[0-9]{12}:*.*`
- **Min Length**: 1
- **Max Length**: 1024

### samlGroupAttribute
- **Type**: string
- **Pattern**: `.*[\w+=,.@-]+.*`
- **Min Length**: 1
- **Max Length**: 2048

### samlMetadata
- **Type**: string
- **Pattern**: `.*[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+.*`
- **Min Length**: 1
- **Max Length**: 51200

### samlUserAttribute
- **Type**: string
- **Pattern**: `.*[\w+=,.@-]+.*`
- **Min Length**: 1
- **Max Length**: 2048

