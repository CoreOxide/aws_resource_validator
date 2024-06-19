# Organizations Service

### AccountArn
- **Type**: string
- **Pattern**: `^arn:aws:organizations::\d{12}:account\/o-[a-z0-9]{10,32}\/\d{12}`

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Max Length**: 12

### AccountName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 128

### ChildId
- **Type**: string
- **Pattern**: `^(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
- **Max Length**: 100

### CreateAccountName
- **Type**: string
- **Pattern**: `[\u0020-\u007E]+`
- **Min Length**: 1
- **Max Length**: 50

### CreateAccountRequestId
- **Type**: string
- **Pattern**: `^car-[a-z0-9]{8,32}$`
- **Max Length**: 36

### Email
- **Type**: string
- **Pattern**: `[^\s@]+@[^\s@]+\.[^\s@]+`
- **Min Length**: 6
- **Max Length**: 64

### GenericArn
- **Type**: string
- **Pattern**: `^arn:aws:organizations::.+:.+`

### HandshakeArn
- **Type**: string
- **Pattern**: `^arn:aws:organizations::\d{12}:handshake\/o-[a-z0-9]{10,32}\/[a-z_]{1,32}\/h-[0-9a-z]{8,32}`

### HandshakeId
- **Type**: string
- **Pattern**: `^h-[0-9a-z]{8,32}$`
- **Max Length**: 34

### HandshakeNotes
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 1024

### HandshakePartyId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 64

### NextToken
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 100000

### OrganizationArn
- **Type**: string
- **Pattern**: `^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32}`

### OrganizationId
- **Type**: string
- **Pattern**: `^o-[a-z0-9]{10,32}$`

### OrganizationalUnitArn
- **Type**: string
- **Pattern**: `^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}`

### OrganizationalUnitId
- **Type**: string
- **Pattern**: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
- **Max Length**: 68

### OrganizationalUnitName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 128

### ParentId
- **Type**: string
- **Pattern**: `^(r-[0-9a-z]{4,32})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
- **Max Length**: 100

### PolicyArn
- **Type**: string
- **Pattern**: `^(arn:aws:organizations::\d{12}:policy\/o-[a-z0-9]{10,32}\/[0-9a-z_]+\/p-[0-9a-z]{10,32})|(arn:aws:organizations::aws:policy\/[0-9a-z_]+\/p-[0-9a-zA-Z_]{10,128})`

### PolicyContent
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1

### PolicyDescription
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 512

### PolicyId
- **Type**: string
- **Pattern**: `^p-[0-9a-zA-Z_]{8,128}$`
- **Max Length**: 130

### PolicyName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 128

### PolicyTargetId
- **Type**: string
- **Pattern**: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
- **Max Length**: 100

### ResourcePolicyArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:resourcepolicy\/o-[a-z0-9]{10,32}\/rp-[0-9a-zA-Z_]{4,128}`

### ResourcePolicyContent
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 40000

### ResourcePolicyId
- **Type**: string
- **Pattern**: `^rp-[0-9a-zA-Z_]{4,128}$`
- **Max Length**: 131

### RoleName
- **Type**: string
- **Pattern**: `[\w+=,.@-]{1,64}`
- **Max Length**: 64

### RootArn
- **Type**: string
- **Pattern**: `^arn:aws:organizations::\d{12}:root\/o-[a-z0-9]{10,32}\/r-[0-9a-z]{4,32}`

### RootId
- **Type**: string
- **Pattern**: `^r-[0-9a-z]{4,32}$`
- **Max Length**: 34

### ServicePrincipal
- **Type**: string
- **Pattern**: `[\w+=,.@-]*`
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

### TaggableResourceId
- **Type**: string
- **Pattern**: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})|(^p-[0-9a-zA-Z_]{8,128})|(^rp-[0-9a-zA-Z_]{4,128})$`
- **Max Length**: 130

