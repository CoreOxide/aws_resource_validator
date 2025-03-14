# Datasync Service

### ActivationKey
- **Type**: string
- **Pattern**: `[A-Z0-9]{5}(-[A-Z0-9]{5}){4}`
- **Max Length**: 29

### AgentArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`
- **Max Length**: 128

### AgentVersion
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s+=._:@/-]+$`
- **Min Length**: 1
- **Max Length**: 256

### AzureBlobContainerUrl
- **Type**: string
- **Pattern**: `^https:\/\/[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}\/[a-z0-9](-?[a-z0-9]){2,62}$`
- **Max Length**: 325

### AzureBlobSasToken
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### AzureBlobSubdirectory
- **Type**: string
- **Pattern**: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`
- **Max Length**: 1024

### DiscoveryJobArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:system/storage-system-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/job/discovery-job-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Max Length**: 256

### DiscoveryNextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_-]+`
- **Max Length**: 65535

### DiscoveryServerHostname
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
- **Max Length**: 255

### Ec2SecurityGroupArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`
- **Max Length**: 128

### Ec2SubnetArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/.*$`
- **Max Length**: 128

### EfsAccessPointArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$`
- **Max Length**: 128

### EfsFilesystemArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]*:[0-9]{12}:file-system/fs-.*$`
- **Max Length**: 128

### EfsSubdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
- **Max Length**: 4096

### Endpoint
- **Type**: string
- **Pattern**: `\A(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\z`
- **Min Length**: 7
- **Max Length**: 15

### ErrorMessage
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 128

### FilterAttributeValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_\ \-\:\*\.\\/\?-]*$`
- **Min Length**: 1
- **Max Length**: 255

### FilterType
- **Type**: string
- **Pattern**: `^[A-Z0-9_]+$`
- **Max Length**: 128

### FilterValue
- **Type**: string
- **Pattern**: `^[^\x00]+$`
- **Max Length**: 102400

### FsxFilesystemArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):fsx:[a-z\-0-9]*:[0-9]{12}:file-system/fs-.*$`
- **Max Length**: 128

### FsxLustreSubdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
- **Max Length**: 4096

### FsxOntapSubdirectory
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
- **Max Length**: 255

### FsxOpenZfsSubdirectory
- **Type**: string
- **Pattern**: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`
- **Max Length**: 4096

### FsxWindowsSubdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
- **Max Length**: 4096

### HdfsServerHostname
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 255

### HdfsSubdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
- **Max Length**: 4096

### HdfsUser
- **Type**: string
- **Pattern**: `^[_.A-Za-z0-9][-_.A-Za-z0-9]*$`
- **Min Length**: 1
- **Max Length**: 256

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
- **Max Length**: 2048

### KerberosPrincipal
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 256

### KmsKeyProviderUri
- **Type**: string
- **Pattern**: `^kms:\/\/http[s]?@(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(;(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9]))*:[0-9]{1,5}\/kms$`
- **Min Length**: 1
- **Max Length**: 255

### LocationArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
- **Max Length**: 128

### LocationUri
- **Type**: string
- **Pattern**: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`
- **Max Length**: 4360

### LogGroupArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):logs:[a-z\-0-9]+:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`
- **Max Length**: 562

### Name
- **Type**: string
- **Pattern**: `^[\p{L}\p{M}\p{N}\s+=._:@\/-]+$`
- **Min Length**: 1
- **Max Length**: 256

### NetworkInterfaceArn
- **Type**: string
- **Pattern**: `^arn:aws[\-a-z]{0,}:ec2:[a-z\-0-9]*:[0-9]{12}:network-interface/eni-[0-9a-f]+$`
- **Max Length**: 128

### NextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_-]+`
- **Max Length**: 65535

### NfsSubdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]+$`
- **Max Length**: 4096

### ObjectStorageAccessKey
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 200

### ObjectStorageBucketName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\.\(\)\$\p{Zs}]+$`
- **Min Length**: 3
- **Max Length**: 63

### ObjectStorageSecretKey
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 200

### PtolemyPassword
- **Type**: string
- **Pattern**: `^(?!.*[:\"][^:"]*$).+$`
- **Max Length**: 1024

### PtolemyString
- **Type**: string
- **Pattern**: `^.{0,1024}$`
- **Max Length**: 1024

### PtolemyUUID
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### PtolemyUsername
- **Type**: string
- **Pattern**: `^(?!.*[:\"][^:"]*$).+$`
- **Max Length**: 1024

### ResourceId
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### S3BucketArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3:[a-z\-0-9]*:[0-9]{12}:accesspoint[/:][a-zA-Z0-9\-.]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]+:[0-9]{12}:outpost[/:][a-zA-Z0-9\-]{1,63}[/:]accesspoint[/:][a-zA-Z0-9\-]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3:::[a-zA-Z0-9.\-_]{1,255}$`
- **Max Length**: 268

### S3ObjectVersionId
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 100

### S3Subdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
- **Max Length**: 4096

### ScheduleDisabledReason
- **Type**: string
- **Pattern**: `^[\w\s.,\'?!:;\/=|<>()-]*$`
- **Max Length**: 8192

### ScheduleExpressionCron
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\ \_\*\?\,\|\^\-\/\#\s\(\)\+]*$`
- **Max Length**: 256

### SecretsManagerArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z\-0-9]+:[0-9]{12}:secret:.*`
- **Max Length**: 2048

### ServerHostname
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
- **Max Length**: 255

### ServerIpAddress
- **Type**: string
- **Pattern**: `\A(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\z`
- **Min Length**: 7
- **Max Length**: 15

### SmbDomain
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`
- **Max Length**: 253

### SmbPassword
- **Type**: string
- **Pattern**: `^.{0,104}$`
- **Max Length**: 104

### SmbSubdirectory
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
- **Max Length**: 4096

### SmbUser
- **Type**: string
- **Pattern**: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`
- **Max Length**: 104

### StorageSystemArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:system/storage-system-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Max Length**: 128

### StorageVirtualMachineArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:storage-virtual-machine/fs-[0-9a-f]+/svm-[0-9a-f]{17,}$`
- **Max Length**: 162

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s+=._:/-]+$`
- **Min Length**: 1
- **Max Length**: 256

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s+=._:@/-]+$`
- **Min Length**: 0
- **Max Length**: 256

### TaggableResourceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:(agent|task|location|system)/((agent|task|loc)-[a-f0-9]{17}|storage-system-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})(/execution/exec-[a-f0-9]{17})?$`
- **Max Length**: 128

### TaskArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}$`
- **Max Length**: 128

### TaskExecutionArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`
- **Max Length**: 128

### UpdateSmbDomain
- **Type**: string
- **Pattern**: `^([A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252})?$`
- **Max Length**: 253

### UpdatedEfsAccessPointArn
- **Type**: string
- **Pattern**: `(^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$)|(^$)`
- **Max Length**: 128

### UpdatedEfsIamRoleArn
- **Type**: string
- **Pattern**: `(^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$)|(^$)`
- **Max Length**: 2048

### VpcEndpointId
- **Type**: string
- **Pattern**: `^vpce-[0-9a-f]{17}$`

