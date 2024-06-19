# Ssoadmin Service

### AccessControlAttributeKey
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@]+$`
- **Min Length**: 1
- **Max Length**: 128

### AccessControlAttributeValueSource
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@\[\]\{\}\$\\"]*$`
- **Min Length**: 0
- **Max Length**: 256

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ApplicationArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
- **Min Length**: 10
- **Max Length**: 1224

### ApplicationProviderArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::aws:applicationProvider/[a-zA-Z0-9-/]+$`
- **Min Length**: 10
- **Max Length**: 1224

### ApplicationUrl
- **Type**: string
- **Pattern**: `^http(s)?:\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&bb@#\/%?=~_|]$`
- **Min Length**: 1
- **Max Length**: 512

### ClaimAttributePath
- **Type**: string
- **Pattern**: `^\p{L}+(?:(\.|\_)\p{L}+){0,2}$`
- **Min Length**: 1
- **Max Length**: 255

### ClientToken
- **Type**: string
- **Pattern**: `^[!-~]+$`
- **Min Length**: 1
- **Max Length**: 64

### Duration
- **Type**: string
- **Pattern**: `^(-?)P(?=\d|T\d)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)([DW]))?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?$`
- **Min Length**: 1
- **Max Length**: 100

### IconUrl
- **Type**: string
- **Pattern**: `^(http|https):\/\/.*$`
- **Min Length**: 1
- **Max Length**: 768

### Id
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]*$`
- **Min Length**: 1
- **Max Length**: 64

### InstanceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
- **Min Length**: 10
- **Max Length**: 1224

### JMESPath
- **Type**: string
- **Pattern**: `^\p{L}+(?:\.\p{L}+){0,2}$`
- **Min Length**: 1
- **Max Length**: 255

### ManagedPolicyArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::aws:policy/[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]+$`
- **Min Length**: 20
- **Max Length**: 2048

### ManagedPolicyName
- **Type**: string
- **Pattern**: `^[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ManagedPolicyPath
- **Type**: string
- **Pattern**: `^((/[A-Za-z0-9\.,\+@=_-]+)*)/$`
- **Min Length**: 1
- **Max Length**: 512

### NameType
- **Type**: string
- **Pattern**: `^[\w+=,.@-]+$`
- **Min Length**: 0
- **Max Length**: 255

### PermissionSetArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}$`
- **Min Length**: 10
- **Max Length**: 1224

### PermissionSetDescription
- **Type**: string
- **Pattern**: `^[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*$`
- **Min Length**: 1
- **Max Length**: 700

### PermissionSetName
- **Type**: string
- **Pattern**: `^[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 32

### PermissionSetPolicyDocument
- **Type**: string
- **Pattern**: `^[\u0009\u000A\u000D\u0020-\u00FF]+$`
- **Min Length**: 1
- **Max Length**: 32768

### PrincipalId
- **Type**: string
- **Pattern**: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 47

### Reason
- **Type**: string
- **Pattern**: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*$`

### RelayState
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9&$@#\\\/%?=~\-_\'"|!:,.;*+\[\]\ \(\)\{\}]+$`
- **Min Length**: 1
- **Max Length**: 240

### ResourceServerScope
- **Type**: string
- **Pattern**: `^[^:=\-\.\s][0-9a-zA-Z_:\-\.]+$`
- **Min Length**: 1
- **Max Length**: 80

### Scope
- **Type**: string
- **Pattern**: `^([A-Za-z0-9_]{1,50})(:[A-Za-z0-9_]{1,50}){0,1}(:[A-Za-z0-9_]{1,50}){0,1}$`

### ScopeTarget
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::(\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}|:instance/(sso)?ins-[a-zA-Z0-9-.]{16})$`
- **Min Length**: 1
- **Max Length**: 100

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

### TaggableResourceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::((:instance/(sso)?ins-[a-zA-Z0-9-.]{16})|(:permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16})|(\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16})|(\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}))$`
- **Min Length**: 10
- **Max Length**: 2048

### TargetId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### Token
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9+=/_]*$`
- **Min Length**: 0
- **Max Length**: 2048

### TrustedTokenIssuerArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 10
- **Max Length**: 1224

### TrustedTokenIssuerName
- **Type**: string
- **Pattern**: `^[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 255

### TrustedTokenIssuerUrl
- **Type**: string
- **Pattern**: `^https?:\/\/[-a-zA-Z0-9+&@\/%=~_|!:,.;]*[-a-zA-Z0-9+&@\/%=~_|]$`
- **Min Length**: 1
- **Max Length**: 512

### UUId
- **Type**: string
- **Pattern**: `^\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b$`
- **Min Length**: 36
- **Max Length**: 36

