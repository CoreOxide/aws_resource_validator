# Robomaker Service

### Arn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 1224

### ClientRequestToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-=]*`
- **Min Length**: 1
- **Max Length**: 64

### Command
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]*`
- **Min Length**: 1
- **Max Length**: 1024

### DeploymentVersion
- **Type**: string
- **Pattern**: `[0-9]*`
- **Min Length**: 1
- **Max Length**: 255

### EnvironmentVariableKey
- **Type**: string
- **Pattern**: `[A-Z_][A-Z0-9_]*`
- **Min Length**: 1
- **Max Length**: 1024

### EnvironmentVariableValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### GenericString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### IamRole
- **Type**: string
- **Pattern**: `arn:aws:iam::\w+:role/.*`
- **Min Length**: 1
- **Max Length**: 255

### Id
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1224

### ImageDigest
- **Type**: string
- **Pattern**: `[Ss][Hh][Aa]256:[0-9a-fA-F]{64}`
- **Min Length**: 0
- **Max Length**: 72

### Json
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Min Length**: 1
- **Max Length**: 262144

### Name
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-]*`
- **Min Length**: 1
- **Max Length**: 255

### NonEmptyString
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 255

### PaginationToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-\/+=]*`
- **Min Length**: 1
- **Max Length**: 2048

### Path
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### RenderingEngineVersionType
- **Type**: string
- **Pattern**: `1.x`
- **Min Length**: 1
- **Max Length**: 4

### RepositoryUrl
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024

### RevisionId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]*`
- **Min Length**: 1
- **Max Length**: 40

### S3Bucket
- **Type**: string
- **Pattern**: `[a-z0-9][a-z0-9.\-]*[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### S3KeyOrPrefix
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### SimulationSoftwareSuiteVersionType
- **Type**: string
- **Pattern**: `7|9|11|Kinetic|Melodic|Dashing|Foxy`
- **Min Length**: 0
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.\-\/+=:]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.\-\/+=:]*`
- **Min Length**: 0
- **Max Length**: 256

### TemplateName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 255

### UnrestrictedCommand
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### Version
- **Type**: string
- **Pattern**: `(\$LATEST)|[0-9]*`
- **Min Length**: 1
- **Max Length**: 255

### VersionQualifier
- **Type**: string
- **Pattern**: `ALL`
- **Min Length**: 1
- **Max Length**: 255

