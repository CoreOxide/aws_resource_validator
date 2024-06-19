# Workspaces Service

### ARN
- **Type**: string
- **Pattern**: `^arn:aws:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-za-z0-9_/.-]{0,127}$`

### AddInName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 64

### AddInUrl
- **Type**: string
- **Pattern**: `^(http|https)\://\S+`
- **Min Length**: 1
- **Max Length**: 1024

### AmazonUuid
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### AwsAccount
- **Type**: string
- **Pattern**: `^\d{12}$`

### BundleId
- **Type**: string
- **Pattern**: `^wsb-[0-9a-z]{8,63}$`

### CertificateAuthorityArn
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
- **Min Length**: 5
- **Max Length**: 200

### ClientEmail
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$`
- **Min Length**: 6
- **Max Length**: 64

### ClientLocale
- **Type**: string
- **Pattern**: `^[a-z]{2}_[A-Z]{2}$`
- **Min Length**: 5
- **Max Length**: 5

### ClientLoginMessage
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2000

### ClientToken
- **Type**: string
- **Pattern**: `^.{1,64}$`

### ClientUrl
- **Type**: string
- **Pattern**: `^(http|https)\://\S+`
- **Min Length**: 1
- **Max Length**: 200

### ConnectionAliasId
- **Type**: string
- **Pattern**: `^wsca-[0-9a-z]{8,63}$`
- **Min Length**: 13
- **Max Length**: 68

### ConnectionIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 20

### ConnectionString
- **Type**: string
- **Pattern**: `^[.0-9a-zA-Z\-]{1,255}$`
- **Min Length**: 1
- **Max Length**: 255

### DedicatedTenancyManagementCidrRange
- **Type**: string
- **Pattern**: `(^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.0\.0)(\/(16$))$`

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{8,63}$`
- **Min Length**: 10
- **Max Length**: 65

### Ec2ImageId
- **Type**: string
- **Pattern**: `^ami\-([a-f0-9]{8}|[a-f0-9]{17})$`

### IpGroupId
- **Type**: string
- **Pattern**: `wsipg-[0-9a-z]{8,63}$`

### LinkId
- **Type**: string
- **Pattern**: `^link-.{8,24}$`

### ManagementCidrRangeConstraint
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$`

### Region
- **Type**: string
- **Pattern**: `^[-0-9a-z]{1,31}$`
- **Min Length**: 1
- **Max Length**: 31

### SamlUserAccessUrl
- **Type**: string
- **Pattern**: `^(http|https)\://\S+$`
- **Min Length**: 8
- **Max Length**: 200

### SecurityGroupId
- **Type**: string
- **Pattern**: `^(sg-([0-9a-f]{8}|[0-9a-f]{17}))$`
- **Min Length**: 11
- **Max Length**: 20

### SubnetId
- **Type**: string
- **Pattern**: `^(subnet-([0-9a-f]{8}|[0-9a-f]{17}))$`
- **Min Length**: 15
- **Max Length**: 24

### UpdateDescription
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_./() -]+$`
- **Min Length**: 1
- **Max Length**: 255

### WorkSpaceApplicationId
- **Type**: string
- **Pattern**: `^wsa-[0-9a-z]{8,63}$`

### WorkSpaceApplicationOwner
- **Type**: string
- **Pattern**: `^\d{12}|AMAZON$`

### WorkspaceBundleDescription
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_./() -]+$`
- **Min Length**: 1
- **Max Length**: 255

### WorkspaceBundleName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_./()\\-]+$`
- **Min Length**: 1
- **Max Length**: 64

### WorkspaceId
- **Type**: string
- **Pattern**: `^ws-[0-9a-z]{8,63}$`

### WorkspaceImageDescription
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_./() -]+$`
- **Min Length**: 1
- **Max Length**: 256

### WorkspaceImageId
- **Type**: string
- **Pattern**: `wsi-[0-9a-z]{9,63}$`

### WorkspaceImageName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_./()\\-]+$`
- **Min Length**: 1
- **Max Length**: 64

### WorkspaceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_()][a-zA-Z0-9_.()-]{1,63}$`

