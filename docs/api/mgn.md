# Mgn Service

### AccountID
- **Type**: string
- **Pattern**: `[0-9]{12,}`
- **Min Length**: 12
- **Max Length**: 12

### ActionDescription
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z ():/.,\'-_#*; ]*$`
- **Min Length**: 0
- **Max Length**: 256

### ActionID
- **Type**: string
- **Pattern**: `[0-9a-zA-Z]$`
- **Min Length**: 1
- **Max Length**: 64

### ActionName
- **Type**: string
- **Pattern**: `^[^\s\x00]( *[^\s\x00])*$`
- **Min Length**: 1
- **Max Length**: 256

### ApplicationDescription
- **Type**: string
- **Pattern**: `^[^\x00]*$`
- **Min Length**: 0
- **Max Length**: 600

### ApplicationID
- **Type**: string
- **Pattern**: `^app-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### ApplicationName
- **Type**: string
- **Pattern**: `^[^\s\x00]( *[^\s\x00])*$`
- **Min Length**: 1
- **Max Length**: 256

### CloudWatchLogGroupName
- **Type**: string
- **Pattern**: `^[\.\-_/#A-Za-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 512

### ConnectorArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:mgn:([a-z]{2}-(gov-)?[a-z]+-\d{1})?:(\d{12})?:connector\/(connector-[0-9a-zA-Z]{17})$`
- **Min Length**: 27
- **Max Length**: 100

### ConnectorID
- **Type**: string
- **Pattern**: `^connector-[0-9a-zA-Z]{17}$`
- **Min Length**: 27
- **Max Length**: 27

### ConnectorName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 256

### DocumentVersion
- **Type**: string
- **Pattern**: `^(\$DEFAULT|\$LATEST|[0-9]+)$`

### EC2InstanceID
- **Type**: string
- **Pattern**: `^i-[0-9a-fA-F]{8,}$`
- **Min Length**: 0
- **Max Length**: 255

### EC2LaunchConfigurationTemplateID
- **Type**: string
- **Pattern**: `^lt-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 20

### ExportID
- **Type**: string
- **Pattern**: `^export-[0-9a-zA-Z]{17}$`
- **Min Length**: 24
- **Max Length**: 24

### ISO8601DatetimeString
- **Type**: string
- **Pattern**: `^[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z$`
- **Min Length**: 19
- **Max Length**: 32

### ImportID
- **Type**: string
- **Pattern**: `^import-[0-9a-zA-Z]{17}$`
- **Min Length**: 24
- **Max Length**: 24

### JmesPathString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+(\.[a-zA-Z0-9_\[\]]+)*$`
- **Min Length**: 1
- **Max Length**: 1011

### JobID
- **Type**: string
- **Pattern**: `^mgnjob-[0-9a-zA-Z]{17}$`
- **Min Length**: 24
- **Max Length**: 24

### LaunchConfigurationTemplateID
- **Type**: string
- **Pattern**: `^lct-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### OperatingSystemString
- **Type**: string
- **Pattern**: `^(linux|windows)$`

### ReplicationConfigurationTemplateID
- **Type**: string
- **Pattern**: `^rct-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### S3BucketName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9.\-_]{1,255}$`

### S3Key
- **Type**: string
- **Pattern**: `^[^\x00]{1,1020}\.csv$`

### SecretArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:secretsmanager:([a-z]{2}-(gov-)?[a-z]+-\d{1})?:(\d{12})?:secret:(.+)$`
- **Min Length**: 20
- **Max Length**: 100

### SecurityGroupID
- **Type**: string
- **Pattern**: `^sg-[0-9a-fA-F]{8,}$`
- **Min Length**: 0
- **Max Length**: 255

### SourceServerID
- **Type**: string
- **Pattern**: `^s-[0-9a-zA-Z]{17}$`
- **Min Length**: 19
- **Max Length**: 19

### SsmDocumentName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9/:_\.-])+$`
- **Min Length**: 3
- **Max Length**: 172

### SsmDocumentParameterName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9])+$`
- **Min Length**: 1
- **Max Length**: 1011

### SsmInstanceID
- **Type**: string
- **Pattern**: `(^i-[0-9a-zA-Z]{17}$)|(^mi-[0-9a-zA-Z]{17}$)`
- **Min Length**: 19
- **Max Length**: 20

### SsmParameterStoreParameterName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9_\.-])+$`
- **Min Length**: 1
- **Max Length**: 1011

### SubnetID
- **Type**: string
- **Pattern**: `^subnet-[0-9a-fA-F]{8,}$`
- **Min Length**: 0
- **Max Length**: 255

### VcenterClientID
- **Type**: string
- **Pattern**: `^vcc-[0-9a-zA-Z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### WaveDescription
- **Type**: string
- **Pattern**: `^[^\x00]*$`
- **Min Length**: 0
- **Max Length**: 600

### WaveID
- **Type**: string
- **Pattern**: `^wave-[0-9a-zA-Z]{17}$`
- **Min Length**: 22
- **Max Length**: 22

### WaveName
- **Type**: string
- **Pattern**: `^[^\s\x00]( *[^\s\x00])*$`
- **Min Length**: 1
- **Max Length**: 256

