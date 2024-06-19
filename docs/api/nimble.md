# Nimble Service

### EC2ImageId
- **Type**: string
- **Pattern**: `^ami-[0-9A-z]+$`

### EulaAcceptanceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 22

### EulaId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 22

### LaunchProfileId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 22

### LaunchProfileProtocolVersion
- **Type**: string
- **Pattern**: `^2021\-03\-31$`
- **Min Length**: 0
- **Max Length**: 10

### LaunchPurpose
- **Type**: string
- **Pattern**: `^[A-Z0-9_]+$`
- **Min Length**: 0
- **Max Length**: 64

### LinuxMountPoint
- **Type**: string
- **Pattern**: `^(/?|(\$HOME)?(/[^/\n\s\\]+)*)$`
- **Min Length**: 0
- **Max Length**: 128

### Region
- **Type**: string
- **Pattern**: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
- **Min Length**: 0
- **Max Length**: 50

### ScriptParameterKey
- **Type**: string
- **Pattern**: `^[a-zA-Z_][a-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 64

### StreamingImageEncryptionConfigurationKeyArn
- **Type**: string
- **Pattern**: `^arn:.*`
- **Min Length**: 4

### StreamingImageId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 22

### StreamingImagePlatform
- **Type**: string
- **Pattern**: `^[a-zA-Z]*$`

### StreamingSessionStorageRootPathLinux
- **Type**: string
- **Pattern**: `^(\$HOME|/)[/]?([A-Za-z0-9-_]+/)*([A-Za-z0-9_-]+)$`
- **Min Length**: 1
- **Max Length**: 128

### StreamingSessionStorageRootPathWindows
- **Type**: string
- **Pattern**: `^((\%HOMEPATH\%)|[a-zA-Z]:)[\\/](?:[a-zA-Z0-9_-]+[\\/])*[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 128

### StudioComponentId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 22

### StudioEncryptionConfigurationKeyArn
- **Type**: string
- **Pattern**: `^arn:.*`
- **Min Length**: 4

### StudioName
- **Type**: string
- **Pattern**: `^[a-z0-9]*$`
- **Min Length**: 3
- **Max Length**: 64

### WindowsMountDrive
- **Type**: string
- **Pattern**: `^[A-Z]$`

