# Accessanalyzer Service

### AccessPointArn
- **Type**: string
- **Pattern**: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`

### AccessPreviewId
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### AnalyzerArn
- **Type**: string
- **Pattern**: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

### CloudTrailArn
- **Type**: string
- **Pattern**: `arn:[^:]*:cloudtrail:[^:]*:[^:]*:trail/.{1,576}`

### Name
- **Type**: string
- **Pattern**: `[A-Za-z][A-Za-z0-9_.-]*`
- **Min Length**: 1
- **Max Length**: 255

### PrincipalArn
- **Type**: string
- **Pattern**: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`

### ResourceArn
- **Type**: string
- **Pattern**: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

### RoleArn
- **Type**: string
- **Pattern**: `arn:[^:]*:iam::[^:]*:role/.{1,576}`

### VpcId
- **Type**: string
- **Pattern**: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`

