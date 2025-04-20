# Partnercentralselling Service

### Alias
- **Type**: string
- **Pattern**: `^[\p{L}\p{N}\p{P}\p{Z}]+$`
- **Min Length**: 0
- **Max Length**: 80

### AwsAccount
- **Type**: string
- **Pattern**: `^([0-9]{12}|\w{1,12})$`

### AwsMarketplaceOfferIdentifier
- **Type**: string
- **Pattern**: `^arn:aws:aws-marketplace:[a-z]{1,2}-[a-z]*-\d+:\d{12}:AWSMarketplace/Offer/.*$`

### CatalogIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`

### ClientToken
- **Type**: string
- **Pattern**: `^[!-~]{1,64}$`

### CompanyName
- **Type**: string
- **Pattern**: `^[\p{L}\p{N}\p{P}\p{Z}]+$`
- **Min Length**: 1
- **Max Length**: 120

### CompanyWebsiteUrl
- **Type**: string
- **Pattern**: `^((http|https)://)??(www[.])??([a-zA-Z0-9]|-)+?([.][a-zA-Z0-9(-|/|=|?)??]+?)+?$`
- **Min Length**: 4
- **Max Length**: 255

### CreateEngagementRequestClientTokenString
- **Type**: string
- **Pattern**: `^[!-~]{1,64}$`

### CreateResourceSnapshotJobRequestClientTokenString
- **Type**: string
- **Pattern**: `^[!-~]{1,64}$`

### CreateResourceSnapshotRequestClientTokenString
- **Type**: string
- **Pattern**: `^[!-~]{1,64}$`

### Date
- **Type**: string
- **Pattern**: `^[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$`

### DunsNumber
- **Type**: string
- **Pattern**: `^[0-9]{9}$`

### Email
- **Type**: string
- **Pattern**: `^[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$`
- **Min Length**: 0
- **Max Length**: 80

### EngagementArn
- **Type**: string
- **Pattern**: `^arn:.*`

### EngagementArnOrIdentifier
- **Type**: string
- **Pattern**: `^(arn:.*|eng-[0-9a-z]{14})$`

### EngagementCustomerProjectDetailsTargetCompletionDateString
- **Type**: string
- **Pattern**: `^[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$`

### EngagementIdentifier
- **Type**: string
- **Pattern**: `^eng-[0-9a-z]{14}$`

### EngagementInvitationArn
- **Type**: string
- **Pattern**: `^arn:aws:partnercentral::[0-9]{12}:[a-zA-Z]+/engagement-invitation/engi-[0-9,a-z]{13}$`

### EngagementInvitationArnOrIdentifier
- **Type**: string
- **Pattern**: `^(arn:.*|engi-[0-9a-z]{13})$`
- **Min Length**: 1
- **Max Length**: 255

### EngagementInvitationIdentifier
- **Type**: string
- **Pattern**: `^engi-[0-9,a-z]{13}$`

### ExpectedCustomerSpendCurrencyCodeEnum
- **Type**: string
- **Pattern**: `^USD$`

### MonetaryValueAmountString
- **Type**: string
- **Pattern**: `^(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?$`

### OpportunityArn
- **Type**: string
- **Pattern**: `^arn:.*$`

### OpportunityIdentifier
- **Type**: string
- **Pattern**: `^O[0-9]{1,19}$`

### PhoneNumber
- **Type**: string
- **Pattern**: `^\+[1-9]\d{1,14}$`
- **Min Length**: 0
- **Max Length**: 40

### RejectionReasonString
- **Type**: string
- **Pattern**: `^[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]{1,80}$`

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:.*`

### ResourceIdentifier
- **Type**: string
- **Pattern**: `^O[0-9]{1,19}$`

### ResourceSnapshotArn
- **Type**: string
- **Pattern**: `^arn:.*`

### ResourceSnapshotJobArn
- **Type**: string
- **Pattern**: `^arn:.*`

### ResourceSnapshotJobIdentifier
- **Type**: string
- **Pattern**: `^job-[0-9a-z]{13}$`

### ResourceSnapshotJobRoleArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::\d{12}:role/([-+=,.@_a-zA-Z0-9]+/)*[-+=,.@_a-zA-Z0-9]{1,64}$`
- **Min Length**: 0
- **Max Length**: 2048

### ResourceSnapshotJobRoleIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws:iam::\d{12}:role/([-+=,.@_a-zA-Z0-9]+/)*)?[-+=,.@_a-zA-Z0-9]{1,64}$`
- **Min Length**: 0
- **Max Length**: 2048

### ResourceTemplateName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{3,80}$`

### SenderContactEmail
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9.!#$%&\'*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)*$`
- **Min Length**: 0
- **Max Length**: 80

### SolutionArn
- **Type**: string
- **Pattern**: `^S-[0-9]{1,19}$`

### SolutionIdentifier
- **Type**: string
- **Pattern**: `^S-[0-9]{1,19}$`

### StartEngagementByAcceptingInvitationTaskRequestClientTokenString
- **Type**: string
- **Pattern**: `^[!-~]{1,64}$`
- **Min Length**: 1

### StartEngagementFromOpportunityTaskRequestClientTokenString
- **Type**: string
- **Pattern**: `^[!-~]{1,64}$`
- **Min Length**: 1

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
- **Pattern**: `^arn:[\w+=/,.@-]+:partnercentral:[\w+=/,.@-]*:[0-9]{12}:catalog/([a-zA-Z]+)/[\w+=,.@-]+(/[\w+=,.@-]+)*$`
- **Min Length**: 1
- **Max Length**: 1000

### TaskArn
- **Type**: string
- **Pattern**: `^arn:.*`

### TaskArnOrIdentifier
- **Type**: string
- **Pattern**: `^(arn:.*|task-[0-9a-z]{13})$`

### TaskIdentifier
- **Type**: string
- **Pattern**: `task-[0-9a-z]{13}$`

