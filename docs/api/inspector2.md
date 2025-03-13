# Inspector2 Service

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### AmiId
- **Type**: string
- **Pattern**: `^ami-([a-z0-9]{8}|[a-z0-9]{17}|\*)$`

### CisFindingArn
- **Type**: string
- **Pattern**: `^arn:aws(-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/\d{12}/cis-finding/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### CisOwnerId
- **Type**: string
- **Pattern**: `^\d{12}|o-[a-z0-9]{10,32}$`

### CisScanArn
- **Type**: string
- **Pattern**: `^arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### CisScanConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws(-us-gov|-cn)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-[0-9]{1}:[0-9]{12}:owner/(o-[a-z0-9]+|[0-9]{12})/cis-configuration/[0-9a-fA-F-]+$`

### ExecutionRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

### FindingArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}$`
- **Min Length**: 1
- **Max Length**: 100

### FunctionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`

### ImageHash
- **Type**: string
- **Pattern**: `^sha256:[a-z0-9]{64}$`
- **Min Length**: 71
- **Max Length**: 71

### IpV4Address
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`
- **Min Length**: 7
- **Max Length**: 15

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(-(us-gov|cn))?:kms:([a-z0-9][-.a-z0-9]{0,62})?:[0-9]{12}?:key/(([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(mrk-[0-9a-zA-Z]{32}))$`

### LambdaLayerArn
- **Type**: string
- **Pattern**: `^arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+$`

### MeteringAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### OwnerId
- **Type**: string
- **Pattern**: `(^\d{12}$)|(^o-[a-z0-9]{10,32}$)`
- **Min Length**: 12
- **Max Length**: 34

### Path
- **Type**: string
- **Pattern**: `^(?:/(?:\.[-\w]+|[-\w]+(?:\.[-\w]+)?))+/?$`
- **Min Length**: 1
- **Max Length**: 512

### ReportId
- **Type**: string
- **Pattern**: `\b[a-f0-9]{8}\b-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-\b[a-f0-9]{12}\b`

### ResourceId
- **Type**: string
- **Pattern**: `(^arn:.*:ecr:.*:\d{12}:repository\/(?:[a-z0-9]+(?:[._-][a-z0-9]+)*\/)*[a-z0-9]+(?:[._-][a-z0-9]+)*(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$))`
- **Min Length**: 10
- **Max Length**: 341

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-([a-z0-9]{8}|[a-z0-9]{17}|\*)$`

### SourceLayerHash
- **Type**: string
- **Pattern**: `^sha256:[a-z0-9]{64}$`
- **Min Length**: 71
- **Max Length**: 71

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-([a-z0-9]{8}|[a-z0-9]{17}|\*)$`

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TargetAccount
- **Type**: string
- **Pattern**: `^\d{12}|ALL_ACCOUNTS|SELF$`

### TargetResourceTagsKey
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:/=\-@]*$`
- **Min Length**: 1
- **Max Length**: 128

### TimeOfDay
- **Type**: string
- **Pattern**: `^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$`

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### UsageAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### Version
- **Type**: string
- **Pattern**: `^\$LATEST|[0-9]+$`

### VpcId
- **Type**: string
- **Pattern**: `^vpc-([a-z0-9]{8}|[a-z0-9]{17}|\*)$`

### VulnId
- **Type**: string
- **Pattern**: `^CVE-[12][0-9]{3}-[0-9]{1,10}$`

