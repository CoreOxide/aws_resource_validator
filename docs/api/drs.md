# Drs Service

### ARN
- **Type**: string
- **Pattern**: `^arn:.{16,2044}$`
- **Min Length**: 20
- **Max Length**: 2048

### AccountID
- **Type**: string
- **Pattern**: `[0-9]{12,}`
- **Min Length**: 12
- **Max Length**: 12

### AgentVersion
- **Type**: string
- **Pattern**: `^[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}(.[0-9]{4}.[0-9]{3}.[0-9]{4})?$`

### AwsAvailabilityZone
- **Type**: string
- **Pattern**: `^(us(-gov)?|ap|ca|cn|eu|sa|af|me|il)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9][a-z]$`
- **Min Length**: 0
- **Max Length**: 255

### AwsRegion
- **Type**: string
- **Pattern**: `^(us(-gov)?|ap|ca|cn|eu|sa|af|me|il)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9]$`
- **Min Length**: 0
- **Max Length**: 255

### CfnStackName
- **Type**: string
- **Pattern**: `^[a-zA-Z][-a-zA-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 128

### EC2InstanceID
- **Type**: string
- **Pattern**: `^i-[0-9a-fA-F]{8,}$`
- **Min Length**: 0
- **Max Length**: 255

### EbsSnapshot
- **Type**: string
- **Pattern**: `^snap-[0-9a-zA-Z]{17}$`

### EbsVolumeID
- **Type**: string
- **Pattern**: `^vol-([0-9a-fA-F]{8}|[0-9a-fA-F]{17})$`
- **Min Length**: 10
- **Max Length**: 19

### FailureReason
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z ():/.,\'-_#*;]*$`
- **Min Length**: 0
- **Max Length**: 256

### ISO8601DatetimeString
- **Type**: string
- **Pattern**: `^[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z$`
- **Min Length**: 19
- **Max Length**: 32

### JobID
- **Type**: string
- **Pattern**: `^drsjob-[0-9a-zA-Z]{17}$`
- **Min Length**: 24
- **Max Length**: 24

### LaunchActionDescription
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z ():/.,\'-_#*; ]*$`
- **Min Length**: 0
- **Max Length**: 1024

### LaunchActionId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
- **Min Length**: 1
- **Max Length**: 64

### LaunchActionName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9 /_-]*$`
- **Min Length**: 1
- **Max Length**: 256

### LaunchActionParameterName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9])+$`
- **Min Length**: 1
- **Max Length**: 1011

### LaunchActionParameterValue
- **Type**: string
- **Pattern**: `^[A-Za-z0-9.-]+$`
- **Min Length**: 1
- **Max Length**: 1011

### LaunchActionResourceId
- **Type**: string
- **Pattern**: `^(s-[0-9a-zA-Z]{17}$|lct-[0-9a-zA-Z]{17})$`

### LaunchActionRunId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
- **Min Length**: 1
- **Max Length**: 64

### LaunchActionVersion
- **Type**: string
- **Pattern**: `^(\$DEFAULT|\$LATEST|[0-9]+)$`
- **Min Length**: 1
- **Max Length**: 10

### LaunchConfigurationTemplateID
- **Type**: string
- **Pattern**: `^lct-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### OutpostARN
- **Type**: string
- **Pattern**: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
- **Min Length**: 20
- **Max Length**: 255

### ProductCodeId
- **Type**: string
- **Pattern**: `^([A-Za-z0-9])+$`
- **Min Length**: 25
- **Max Length**: 25

### RecoveryInstanceID
- **Type**: string
- **Pattern**: `^i-[0-9a-fA-F]{8,}$`
- **Min Length**: 10
- **Max Length**: 19

### RecoverySnapshotID
- **Type**: string
- **Pattern**: `^pit-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### ReplicationConfigurationTemplateID
- **Type**: string
- **Pattern**: `^rct-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### SecurityGroupID
- **Type**: string
- **Pattern**: `^sg-[0-9a-fA-F]{8,}$`
- **Min Length**: 0
- **Max Length**: 255

### SourceNetworkID
- **Type**: string
- **Pattern**: `^sn-[0-9a-zA-Z]{17}$`
- **Min Length**: 20
- **Max Length**: 20

### SourceServerARN
- **Type**: string
- **Pattern**: `^arn:(?:[0-9a-zA-Z_-]+:){3}([0-9]{12,}):source-server/(s-[0-9a-zA-Z]{17})$`
- **Min Length**: 20
- **Max Length**: 2048

### SourceServerID
- **Type**: string
- **Pattern**: `^s-[0-9a-zA-Z]{17}$`
- **Min Length**: 19
- **Max Length**: 19

### SsmDocumentName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9-/:])+$`
- **Min Length**: 1
- **Max Length**: 1011

### SubnetID
- **Type**: string
- **Pattern**: `^subnet-[0-9a-fA-F]{8,}$`
- **Min Length**: 0
- **Max Length**: 255

### VpcID
- **Type**: string
- **Pattern**: `^vpc-[0-9a-fA-F]{8,}$`
- **Min Length**: 12
- **Max Length**: 21

