# Cloudhsmv2 Service

### BackupId
- **Type**: string
- **Pattern**: `backup-[2-7a-zA-Z]{11,16}`

### BackupRetentionValue
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 3

### Cert
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+-/=\s]*`
- **Max Length**: 5000

### ClusterId
- **Type**: string
- **Pattern**: `cluster-[2-7a-zA-Z]{11,16}`

### EniId
- **Type**: string
- **Pattern**: `eni-[0-9a-fA-F]{8,17}`

### ExternalAz
- **Type**: string
- **Pattern**: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d[a-z]`

### Field
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`

### HsmId
- **Type**: string
- **Pattern**: `hsm-[2-7a-zA-Z]{11,16}`

### HsmType
- **Type**: string
- **Pattern**: `(hsm1\.medium)`

### IpAddress
- **Type**: string
- **Pattern**: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### Region
- **Type**: string
- **Pattern**: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d`

### ResourceId
- **Type**: string
- **Pattern**: `(?:cluster|backup)-[2-7a-zA-Z]{11,16}`

### SecurityGroup
- **Type**: string
- **Pattern**: `sg-[0-9a-fA-F]{8,17}`

### StateMessage
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 300

### SubnetId
- **Type**: string
- **Pattern**: `subnet-[0-9a-fA-F]{8,17}`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### VpcId
- **Type**: string
- **Pattern**: `vpc-[0-9a-fA-F]`

