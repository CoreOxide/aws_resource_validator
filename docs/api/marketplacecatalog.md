# Marketplacecatalog Service

### ARN
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:*/-]+$`
- **Min Length**: 1
- **Max Length**: 2048

### AmiProductEntityIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### AmiProductTitleString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### BatchDescribeErrorCodeString
- **Type**: string
- **Pattern**: `^[a-zA-Z_]+$`
- **Min Length**: 1
- **Max Length**: 72

### BatchDescribeErrorMessageContent
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 2048

### Catalog
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 64

### ChangeName
- **Type**: string
- **Pattern**: `^[a-zA-Z]$`
- **Min Length**: 1
- **Max Length**: 72

### ChangeSetName
- **Type**: string
- **Pattern**: `^[\w\s+=.:@-]+$`
- **Min Length**: 1
- **Max Length**: 100

### ChangeType
- **Type**: string
- **Pattern**: `^[A-Z][\w]*$`
- **Min Length**: 1
- **Max Length**: 255

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[!-~]+$`
- **Min Length**: 1
- **Max Length**: 64

### ContainerProductEntityIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### ContainerProductTitleString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### DataProductEntityIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### DataProductTitleString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### DateTimeISO8601
- **Type**: string
- **Pattern**: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
- **Min Length**: 20
- **Max Length**: 20

### EntityId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### EntityNameString
- **Type**: string
- **Pattern**: `^\\S+[\\S\\s]*`
- **Min Length**: 1
- **Max Length**: 255

### EntityType
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 255

### ErrorCodeString
- **Type**: string
- **Pattern**: `^[a-zA-Z_]+$`
- **Min Length**: 1
- **Max Length**: 72

### ExceptionMessageContent
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 2048

### FilterName
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 255

### FilterValueContent
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### Identifier
- **Type**: string
- **Pattern**: `^[\w\-@]+$`
- **Min Length**: 1
- **Max Length**: 255

### Json
- **Type**: string
- **Pattern**: `^[\s]*\{[\s\S]*\}[\s]*$`
- **Min Length**: 2
- **Max Length**: 16384

### NextToken
- **Type**: string
- **Pattern**: `^[\w+=.:@\-\/]$`
- **Min Length**: 1
- **Max Length**: 2048

### OfferBuyerAccountsFilterWildcard
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### OfferBuyerAccountsString
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### OfferEntityIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### OfferNameString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 150

### OfferProductIdString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### OfferResaleAuthorizationIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationEntityIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationManufacturerAccountIdFilterWildcard
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ResaleAuthorizationManufacturerAccountIdString
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ResaleAuthorizationManufacturerLegalNameFilterWildcard
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationManufacturerLegalNameString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationNameFilterWildcard
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationNameString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationOfferExtendedStatusString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationProductIdFilterWildcard
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationProductIdString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationProductNameFilterWildcard
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationProductNameString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationResellerAccountIDFilterWildcard
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ResaleAuthorizationResellerAccountIDString
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ResaleAuthorizationResellerLegalNameFilterWildcard
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResaleAuthorizationResellerLegalNameString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### ResourceARN
- **Type**: string
- **Pattern**: `^arn:[\w+=/,.@-]+:aws-marketplace:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*$`
- **Min Length**: 1
- **Max Length**: 255

### ResourceId
- **Type**: string
- **Pattern**: `^[\w\-]+$`
- **Min Length**: 1
- **Max Length**: 255

### ResourcePolicyJson
- **Type**: string
- **Pattern**: `^[\u0009\u000A\u000D\u0020-\u00FF]+$`
- **Min Length**: 1
- **Max Length**: 10240

### SaaSProductEntityIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### SaaSProductTitleString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 255

### SortBy
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 255

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

### VisibilityValue
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 64

