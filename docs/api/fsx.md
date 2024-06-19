# Fsx Service

### AWSAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ActiveDirectoryFullyQualifiedName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
- **Min Length**: 1
- **Max Length**: 255

### AdminPassword
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{8,50}$`
- **Min Length**: 8
- **Max Length**: 50

### Aggregate
- **Type**: string
- **Pattern**: `^(aggr[0-9]{1,2})$`
- **Min Length**: 5
- **Max Length**: 6

### AlternateDNSName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{4,253}$`
- **Min Length**: 4
- **Max Length**: 253

### ArchivePath
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`
- **Min Length**: 3
- **Max Length**: 4357

### BackupId
- **Type**: string
- **Pattern**: `^(backup-[0-9a-f]{8,})$`
- **Min Length**: 12
- **Max Length**: 128

### ClientRequestToken
- **Type**: string
- **Pattern**: `[A-za-z0-9_.-]{0,63}$`
- **Min Length**: 1
- **Max Length**: 63

### DNSName
- **Type**: string
- **Pattern**: `^((fs|fc)i?-[0-9a-f]{8,}\..{4,253})$`
- **Min Length**: 16
- **Max Length**: 275

### DailyTime
- **Type**: string
- **Pattern**: `^([01]\d|2[0-3]):?([0-5]\d)$`
- **Min Length**: 5
- **Max Length**: 5

### DataRepositoryAssociationId
- **Type**: string
- **Pattern**: `^(dra-[0-9a-f]{8,})$`
- **Min Length**: 13
- **Max Length**: 23

### DataRepositoryTaskFilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
- **Min Length**: 1
- **Max Length**: 128

### DataRepositoryTaskPath
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{0,4096}$`
- **Min Length**: 0
- **Max Length**: 4096

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$`
- **Min Length**: 12
- **Max Length**: 12

### DirectoryPassword
- **Type**: string
- **Pattern**: `^.{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### DirectoryUserName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### FileCacheId
- **Type**: string
- **Pattern**: `^(fc-[0-9a-f]{8,})$`
- **Min Length**: 11
- **Max Length**: 21

### FileSystemAdministratorsGroupName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### FileSystemId
- **Type**: string
- **Pattern**: `^(fs-[0-9a-f]{8,})$`
- **Min Length**: 11
- **Max Length**: 21

### FileSystemTypeVersion
- **Type**: string
- **Pattern**: `^[0-9](.[0-9]*)*$`
- **Min Length**: 1
- **Max Length**: 20

### FilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
- **Min Length**: 1
- **Max Length**: 128

### GeneralARN
- **Type**: string
- **Pattern**: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`
- **Min Length**: 8
- **Max Length**: 1024

### IpAddress
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`
- **Min Length**: 7
- **Max Length**: 15

### IpAddressRange
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{9,17}$`
- **Min Length**: 9
- **Max Length**: 17

### JunctionPath
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
- **Min Length**: 1
- **Max Length**: 255

### KmsKeyId
- **Type**: string
- **Pattern**: `^.{1,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### LustreFileSystemMountName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9_-]{1,8})$`
- **Min Length**: 1
- **Max Length**: 8

### LustreNoSquashNid
- **Type**: string
- **Pattern**: `^([0-9\[\]\-]*\.){3}([0-9\[\]\-]*)@tcp$`
- **Min Length**: 11
- **Max Length**: 43

### LustreRootSquash
- **Type**: string
- **Pattern**: `^([0-9]{1,10}):([0-9]{1,10})$`
- **Min Length**: 3
- **Max Length**: 21

### Namespace
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`
- **Min Length**: 1
- **Max Length**: 4096

### NetBiosAlias
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
- **Min Length**: 1
- **Max Length**: 15

### NetworkInterfaceId
- **Type**: string
- **Pattern**: `^(eni-[0-9a-f]{8,})$`
- **Min Length**: 12
- **Max Length**: 21

### NextToken
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
- **Min Length**: 1
- **Max Length**: 255

### OpenZFSClients
- **Type**: string
- **Pattern**: `^[ -~]{1,128}$`
- **Min Length**: 1
- **Max Length**: 128

### OpenZFSNfsExportOption
- **Type**: string
- **Pattern**: `^[ -~]{1,128}$`
- **Min Length**: 1
- **Max Length**: 128

### OrganizationalUnitDistinguishedName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,2000}$`
- **Min Length**: 1
- **Max Length**: 2000

### Region
- **Type**: string
- **Pattern**: `^[a-z0-9-]{1,20}$`
- **Min Length**: 1
- **Max Length**: 20

### ResourceARN
- **Type**: string
- **Pattern**: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`
- **Min Length**: 8
- **Max Length**: 512

### RouteTableId
- **Type**: string
- **Pattern**: `^(rtb-[0-9a-f]{8,})$`
- **Min Length**: 12
- **Max Length**: 21

### SecurityGroupId
- **Type**: string
- **Pattern**: `^(sg-[0-9a-f]{8,})$`
- **Min Length**: 11
- **Max Length**: 20

### SnapshotFilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
- **Min Length**: 1
- **Max Length**: 128

### SnapshotId
- **Type**: string
- **Pattern**: `^((fs)?volsnap-[0-9a-f]{8,})$`
- **Min Length**: 11
- **Max Length**: 28

### SnapshotName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_:.-]{1,203}$`
- **Min Length**: 1
- **Max Length**: 203

### SourceBackupId
- **Type**: string
- **Pattern**: `^(backup-[0-9a-f]{8,})$`
- **Min Length**: 12
- **Max Length**: 128

### StorageVirtualMachineFilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
- **Min Length**: 1
- **Max Length**: 128

### StorageVirtualMachineId
- **Type**: string
- **Pattern**: `^(svm-[0-9a-f]{17,})$`
- **Min Length**: 21
- **Max Length**: 21

### StorageVirtualMachineName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,47}$`
- **Min Length**: 1
- **Max Length**: 47

### SubnetId
- **Type**: string
- **Pattern**: `^(subnet-[0-9a-f]{8,})$`
- **Min Length**: 15
- **Max Length**: 24

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

### TaskId
- **Type**: string
- **Pattern**: `^(task-[0-9a-f]{17,})$`
- **Min Length**: 12
- **Max Length**: 128

### UUID
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
- **Max Length**: 36

### VerboseFlag
- **Type**: string
- **Pattern**: `^(?i)(true|false)$`
- **Min Length**: 4
- **Max Length**: 5

### VolumeFilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
- **Min Length**: 1
- **Max Length**: 128

### VolumeId
- **Type**: string
- **Pattern**: `^(fsvol-[0-9a-f]{17,})$`
- **Min Length**: 23
- **Max Length**: 23

### VolumeName
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,203}$`
- **Min Length**: 1
- **Max Length**: 203

### VolumePath
- **Type**: string
- **Pattern**: `^[A-za-z0-9\_\.\:\-\/]*$`
- **Min Length**: 1
- **Max Length**: 2048

### VpcId
- **Type**: string
- **Pattern**: `^(vpc-[0-9a-f]{8,})$`
- **Min Length**: 12
- **Max Length**: 21

### WeeklyTime
- **Type**: string
- **Pattern**: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`
- **Min Length**: 7
- **Max Length**: 7

