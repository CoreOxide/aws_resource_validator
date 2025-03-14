# Cloudhsmv2 Service

### BackupArn
- **Type**: string
- **Pattern**: `^(arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:backup/)?backup-[2-7a-zA-Z]{11,16}`

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
- **Max Length**: 20000

### CloudHsmArn
- **Type**: string
- **Pattern**: `arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:(backup/backup|cluster/cluster|hsm/hsm)-[2-7a-zA-Z]{11,16}`

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
- **Pattern**: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`
- **Max Length**: 32

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

