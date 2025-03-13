# Transfer Service

### AgreementId
- **Type**: string
- **Pattern**: `a-([0-9a-f]{17})`
- **Min Length**: 19
- **Max Length**: 19

### Arn
- **Type**: string
- **Pattern**: `arn:\S+`
- **Min Length**: 20
- **Max Length**: 1600

### As2Id
- **Type**: string
- **Pattern**: `[\p{Print}\s]*`
- **Min Length**: 1
- **Max Length**: 128

### CallbackToken
- **Type**: string
- **Pattern**: `\w+`
- **Min Length**: 1
- **Max Length**: 64

### CertSerial
- **Type**: string
- **Pattern**: `[\p{XDigit}{2}:?]*`
- **Min Length**: 0
- **Max Length**: 48

### CertificateBodyType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]*`
- **Min Length**: 1
- **Max Length**: 16384

### CertificateChainType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]*`
- **Min Length**: 1
- **Max Length**: 2097152

### CertificateId
- **Type**: string
- **Pattern**: `cert-([0-9a-f]{17})`
- **Min Length**: 22
- **Max Length**: 22

### ConnectorId
- **Type**: string
- **Pattern**: `c-([0-9a-f]{17})`
- **Min Length**: 19
- **Max Length**: 19

### ConnectorSecurityPolicyName
- **Type**: string
- **Pattern**: `TransferSFTPConnectorSecurityPolicy-[A-Za-z0-9-]+`
- **Min Length**: 0
- **Max Length**: 100

### CustomStepTarget
- **Type**: string
- **Pattern**: `arn:[a-z-]+:lambda:.*`
- **Min Length**: 0
- **Max Length**: 170

### Description
- **Type**: string
- **Pattern**: `[\p{Graph}]+`
- **Min Length**: 1
- **Max Length**: 200

### DirectoryId
- **Type**: string
- **Pattern**: `d-[0-9a-f]{10}`
- **Min Length**: 12
- **Max Length**: 12

### EfsFileSystemId
- **Type**: string
- **Pattern**: `(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})`
- **Min Length**: 0
- **Max Length**: 128

### EfsPath
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 65536

### ExecutionId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ExternalId
- **Type**: string
- **Pattern**: `S-1-[\d-]+`
- **Min Length**: 1
- **Max Length**: 256

### FilePath
- **Type**: string
- **Pattern**: `(.)+`
- **Min Length**: 1
- **Max Length**: 1024

### Function
- **Type**: string
- **Pattern**: `arn:[a-z-]+:lambda:.*`
- **Min Length**: 1
- **Max Length**: 170

### HomeDirectory
- **Type**: string
- **Pattern**: `(|/.*)`
- **Min Length**: 0
- **Max Length**: 1024

### HostKeyDescription
- **Type**: string
- **Pattern**: `[\p{Print}]*`
- **Min Length**: 0
- **Max Length**: 200

### HostKeyId
- **Type**: string
- **Pattern**: `hostkey-[0-9a-f]{17}`
- **Min Length**: 25
- **Max Length**: 25

### IdentityCenterApplicationArn
- **Type**: string
- **Pattern**: `arn:[\w-]+:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
- **Min Length**: 10
- **Max Length**: 1224

### IdentityCenterInstanceArn
- **Type**: string
- **Pattern**: `arn:[\w-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
- **Min Length**: 10
- **Max Length**: 1224

### ListingId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z./-]+`
- **Min Length**: 1
- **Max Length**: 512

### LogGroupName
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]*`
- **Min Length**: 1
- **Max Length**: 512

### MapEntry
- **Type**: string
- **Pattern**: `/.*`
- **Min Length**: 0
- **Max Length**: 1024

### MapTarget
- **Type**: string
- **Pattern**: `/.*`
- **Min Length**: 0
- **Max Length**: 1024

### MessageSubject
- **Type**: string
- **Pattern**: `[\p{Print}\p{Blank}]+`
- **Min Length**: 1
- **Max Length**: 1024

### NullableRole
- **Type**: string
- **Pattern**: `(|arn:.*role/\S+)`
- **Min Length**: 0
- **Max Length**: 2048

### OutputFileName
- **Type**: string
- **Pattern**: `c-([0-9a-f]{17})-[0-9a-zA-Z./-]+.json`
- **Min Length**: 26
- **Max Length**: 537

### PostAuthenticationLoginBanner
- **Type**: string
- **Pattern**: `[\x09-\x0D\x20-\x7E]*`
- **Min Length**: 0
- **Max Length**: 4096

### PreAuthenticationLoginBanner
- **Type**: string
- **Pattern**: `[\x09-\x0D\x20-\x7E]*`
- **Min Length**: 0
- **Max Length**: 4096

### PrivateKeyType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]*`
- **Min Length**: 1
- **Max Length**: 16384

### ProfileId
- **Type**: string
- **Pattern**: `p-([0-9a-f]{17})`
- **Min Length**: 19
- **Max Length**: 19

### Role
- **Type**: string
- **Pattern**: `arn:.*role/\S+`
- **Min Length**: 20
- **Max Length**: 2048

### S3Bucket
- **Type**: string
- **Pattern**: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### S3Etag
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 65536

### S3Key
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]*`
- **Min Length**: 0
- **Max Length**: 1024

### S3TagKey
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 1
- **Max Length**: 128

### S3TagValue
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 0
- **Max Length**: 256

### S3VersionId
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024

### SecurityGroupId
- **Type**: string
- **Pattern**: `sg-[0-9a-f]{8,17}`
- **Min Length**: 11
- **Max Length**: 20

### SecurityPolicyName
- **Type**: string
- **Pattern**: `Transfer[A-Za-z0-9]*SecurityPolicy-[A-Za-z0-9-]+`
- **Min Length**: 0
- **Max Length**: 100

### ServerId
- **Type**: string
- **Pattern**: `s-([0-9a-f]{17})`
- **Min Length**: 19
- **Max Length**: 19

### ServiceManagedEgressIpAddress
- **Type**: string
- **Pattern**: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

### SessionId
- **Type**: string
- **Pattern**: `[\w-]*`
- **Min Length**: 3
- **Max Length**: 32

### SourceFileLocation
- **Type**: string
- **Pattern**: `\$\{(\w+.)+\w+\}`
- **Min Length**: 0
- **Max Length**: 256

### SourceIp
- **Type**: string
- **Pattern**: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
- **Min Length**: 0
- **Max Length**: 32

### SshPublicKeyBody
- **Type**: string
- **Pattern**: `\s*(ssh|ecdsa)-[a-z0-9-]+[ \t]+(([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{1,3})?(={0,3})?)(\s*|[ \t]+[\S \t]*\s*)`
- **Min Length**: 0
- **Max Length**: 2048

### SshPublicKeyId
- **Type**: string
- **Pattern**: `key-[0-9a-f]{17}`
- **Min Length**: 21
- **Max Length**: 21

### TransferId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z./-]+`
- **Min Length**: 1
- **Max Length**: 512

### UserName
- **Type**: string
- **Pattern**: `[\w][\w@.-]{2,99}`
- **Min Length**: 3
- **Max Length**: 100

### VpcEndpointId
- **Type**: string
- **Pattern**: `vpce-[0-9a-f]{17}`
- **Min Length**: 22
- **Max Length**: 22

### WebAppId
- **Type**: string
- **Pattern**: `webapp-[0-9a-f]{17}`
- **Min Length**: 24
- **Max Length**: 24

### WorkflowDescription
- **Type**: string
- **Pattern**: `[\w- ]*`
- **Min Length**: 0
- **Max Length**: 256

### WorkflowId
- **Type**: string
- **Pattern**: `w-([a-z0-9]{17})`
- **Min Length**: 19
- **Max Length**: 19

### WorkflowStepName
- **Type**: string
- **Pattern**: `[\w-]*`
- **Min Length**: 0
- **Max Length**: 30

