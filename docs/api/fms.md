# Fms Service

### AWSAccountId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 1024

### AWSRegion
- **Type**: string
- **Pattern**: `^(af|ap|ca|eu|il|me|mx|sa|us|cn|us-gov)-\w+-\d+$`
- **Min Length**: 6
- **Max Length**: 32

### Base62Id
- **Type**: string
- **Pattern**: `^[a-z0-9A-Z]{22}$`
- **Min Length**: 22
- **Max Length**: 22

### CIDR
- **Type**: string
- **Pattern**: `[a-f0-9:./]+`
- **Min Length**: 0
- **Max Length**: 256

### CustomerPolicyScopeId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### Description
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### DetailedInfo
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=,+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 4096

### FirewallPolicyId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### FirewallPolicyName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### Identifier
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 2048

### ListId
- **Type**: string
- **Pattern**: `^[a-z0-9A-Z-]{36}$`
- **Min Length**: 36
- **Max Length**: 36

### ManagedServiceData
- **Type**: string
- **Pattern**: `^((?!\\[nr]).)+`
- **Min Length**: 1
- **Max Length**: 10000

### Name
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### NetworkFirewallAction
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### NetworkFirewallResourceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### OrganizationalUnitId
- **Type**: string
- **Pattern**: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
- **Min Length**: 16
- **Max Length**: 68

### PaginationToken
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 4096

### PolicyId
- **Type**: string
- **Pattern**: `^[a-z0-9A-Z-]{36}$`
- **Min Length**: 36
- **Max Length**: 36

### PolicyUpdateToken
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### PreviousListVersion
- **Type**: string
- **Pattern**: `^\d{1,2}$`
- **Min Length**: 1
- **Max Length**: 2

### Protocol
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 20

### RemediationActionDescription
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### ResourceArn
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### ResourceDescription
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### ResourceId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### ResourceName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceTagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceTagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### ResourceType
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

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

### TargetViolationReason
- **Type**: string
- **Pattern**: `\w+`
- **Min Length**: 0
- **Max Length**: 256

### UpdateToken
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### ViolationTarget
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

