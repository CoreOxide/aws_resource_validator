# Marketplace Catalog Marketplace Catalog Classes

# AmiProductEntityIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# AmiProductFilters

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.AmiProductEntityIdFilter]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.AmiProductLastModifiedDateFilter]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.AmiProductTitleFilter]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.AmiProductVisibilityFilter]


# AmiProductLastModifiedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.AmiProductLastModifiedDateFilterDateRange]


# AmiProductLastModifiedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# AmiProductSort

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# AmiProductSummary

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]


# AmiProductTitleFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# AmiProductVisibilityFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDescribeEntitiesRequest

### EntityRequestList
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.EntityRequest]
- **Required**: Yes


# BatchDescribeEntitiesResponse

### EntityDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.EntityDetail]
- **Required**: Yes

### Errors
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.BatchDescribeErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDescribeErrorDetail

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# CancelChangeSetRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelChangeSetResponse

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# Change

### ChangeType
- **Type**: <class 'str'>
- **Required**: Yes

### Entity
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Entity'>
- **Required**: Yes

### EntityTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Tag]]

### Details
- **Type**: typing.Optional[str]

### DetailsDocument
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ChangeName
- **Type**: typing.Optional[str]


# ChangeSetSummaryListItem

### ChangeSetId
- **Type**: typing.Optional[str]

### ChangeSetArn
- **Type**: typing.Optional[str]

### ChangeSetName
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPLYING', 'CANCELLED', 'FAILED', 'PREPARING', 'SUCCEEDED']]

### EntityIdList
- **Type**: typing.Optional[typing.List[str]]

### FailureCode
- **Type**: typing.Optional[typing.Literal['CLIENT_ERROR', 'SERVER_FAULT']]


# ChangeSummary

### ChangeType
- **Type**: typing.Optional[str]

### Entity
- **Type**: <class 'NoneType'>

### Details
- **Type**: typing.Optional[str]

### DetailsDocument
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ErrorDetailList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ErrorDetail]]

### ChangeName
- **Type**: typing.Optional[str]


# ContainerProductEntityIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# ContainerProductFilters

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ContainerProductEntityIdFilter]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ContainerProductLastModifiedDateFilter]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ContainerProductTitleFilter]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ContainerProductVisibilityFilter]


# ContainerProductLastModifiedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ContainerProductLastModifiedDateFilterDateRange]


# ContainerProductLastModifiedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ContainerProductSort

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ContainerProductSummary

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]


# ContainerProductTitleFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ContainerProductVisibilityFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]]


# DataProductEntityIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# DataProductFilters

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.DataProductEntityIdFilter]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.DataProductTitleFilter]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.DataProductVisibilityFilter]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.DataProductLastModifiedDateFilter]


# DataProductLastModifiedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.DataProductLastModifiedDateFilterDateRange]


# DataProductLastModifiedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# DataProductSort

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# DataProductSummary

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted', 'Unavailable']]


# DataProductTitleFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# DataProductVisibilityFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['Draft', 'Limited', 'Public', 'Restricted', 'Unavailable']]]


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChangeSetRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChangeSetResponse

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Intent
- **Type**: typing.Literal['APPLY', 'VALIDATE']
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['APPLYING', 'CANCELLED', 'FAILED', 'PREPARING', 'SUCCEEDED']
- **Required**: Yes

### FailureCode
- **Type**: typing.Literal['CLIENT_ERROR', 'SERVER_FAULT']
- **Required**: Yes

### FailureDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ChangeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEntityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntityResponse

### EntityType
- **Type**: <class 'str'>
- **Required**: Yes

### EntityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EntityArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'str'>
- **Required**: Yes

### DetailsDocument
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# Entity

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: typing.Optional[str]


# EntityDetail

### EntityType
- **Type**: typing.Optional[str]

### EntityArn
- **Type**: typing.Optional[str]

### EntityIdentifier
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### DetailsDocument
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# EntityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# EntitySummary

### Name
- **Type**: typing.Optional[str]

### EntityType
- **Type**: typing.Optional[str]

### EntityId
- **Type**: typing.Optional[str]

### EntityArn
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[str]

### AmiProductSummary
- **Type**: <class 'NoneType'>

### ContainerProductSummary
- **Type**: <class 'NoneType'>

### DataProductSummary
- **Type**: <class 'NoneType'>

### SaaSProductSummary
- **Type**: <class 'NoneType'>

### OfferSummary
- **Type**: <class 'NoneType'>

### ResaleAuthorizationSummary
- **Type**: <class 'NoneType'>


# EntityTypeFilters

### DataProductFilters
- **Type**: <class 'NoneType'>

### SaaSProductFilters
- **Type**: <class 'NoneType'>

### AmiProductFilters
- **Type**: <class 'NoneType'>

### OfferFilters
- **Type**: <class 'NoneType'>

### ContainerProductFilters
- **Type**: <class 'NoneType'>

### ResaleAuthorizationFilters
- **Type**: <class 'NoneType'>


# EntityTypeSort

### DataProductSort
- **Type**: <class 'NoneType'>

### SaaSProductSort
- **Type**: <class 'NoneType'>

### AmiProductSort
- **Type**: <class 'NoneType'>

### OfferSort
- **Type**: <class 'NoneType'>

### ContainerProductSort
- **Type**: <class 'NoneType'>

### ResaleAuthorizationSort
- **Type**: <class 'NoneType'>


# ErrorDetail

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Filter

### Name
- **Type**: typing.Optional[str]

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# GetResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListChangeSetsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Filter]]

### Sort
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChangeSetsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Filter]]

### Sort
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.PaginatorConfig]


# ListChangeSetsResponse

### ChangeSetSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ChangeSetSummaryListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitiesRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Filter]]

### Sort
- **Type**: <class 'NoneType'>

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### OwnershipType
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### EntityTypeFilters
- **Type**: <class 'NoneType'>

### EntityTypeSort
- **Type**: <class 'NoneType'>


# ListEntitiesRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Filter]]

### Sort
- **Type**: <class 'NoneType'>

### OwnershipType
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### EntityTypeFilters
- **Type**: <class 'NoneType'>

### EntityTypeSort
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.PaginatorConfig]


# ListEntitiesResponse

### EntitySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.EntitySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# OfferAvailabilityEndDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferAvailabilityEndDateFilterDateRange]


# OfferAvailabilityEndDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# OfferBuyerAccountsFilter

### WildCardValue
- **Type**: typing.Optional[str]


# OfferEntityIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# OfferFilters

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferEntityIdFilter]

### Name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferNameFilter]

### ProductId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferProductIdFilter]

### ResaleAuthorizationId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferResaleAuthorizationIdFilter]

### ReleaseDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferReleaseDateFilter]

### AvailabilityEndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferAvailabilityEndDateFilter]

### BuyerAccounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferBuyerAccountsFilter]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferStateFilter]

### Targeting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferTargetingFilter]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferLastModifiedDateFilter]


# OfferLastModifiedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferLastModifiedDateFilterDateRange]


# OfferLastModifiedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# OfferNameFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# OfferProductIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# OfferReleaseDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.OfferReleaseDateFilterDateRange]


# OfferReleaseDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# OfferResaleAuthorizationIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# OfferSort

### SortBy
- **Type**: typing.Optional[typing.Literal['AvailabilityEndDate', 'BuyerAccounts', 'EntityId', 'LastModifiedDate', 'Name', 'ProductId', 'ReleaseDate', 'ResaleAuthorizationId', 'State', 'Targeting']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# OfferStateFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['Draft', 'Released']]]


# OfferSummary

### Name
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ResaleAuthorizationId
- **Type**: typing.Optional[str]

### ReleaseDate
- **Type**: typing.Optional[str]

### AvailabilityEndDate
- **Type**: typing.Optional[str]

### BuyerAccounts
- **Type**: typing.Optional[typing.List[str]]

### State
- **Type**: typing.Optional[typing.Literal['Draft', 'Released']]

### Targeting
- **Type**: typing.Optional[typing.List[typing.Literal['BuyerAccounts', 'CountryCodes', 'None', 'ParticipatingPrograms']]]


# OfferTargetingFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['BuyerAccounts', 'CountryCodes', 'None', 'ParticipatingPrograms']]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# ResaleAuthorizationAvailabilityEndDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationAvailabilityEndDateFilterDateRange]

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# ResaleAuthorizationAvailabilityEndDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationCreatedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationCreatedDateFilterDateRange]

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# ResaleAuthorizationCreatedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationEntityIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# ResaleAuthorizationFilters

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationEntityIdFilter]

### Name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationNameFilter]

### ProductId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationProductIdFilter]

### CreatedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationCreatedDateFilter]

### AvailabilityEndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationAvailabilityEndDateFilter]

### ManufacturerAccountId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationManufacturerAccountIdFilter]

### ProductName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationProductNameFilter]

### ManufacturerLegalName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationManufacturerLegalNameFilter]

### ResellerAccountID
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationResellerAccountIDFilter]

### ResellerLegalName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationResellerLegalNameFilter]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationStatusFilter]

### OfferExtendedStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationOfferExtendedStatusFilter]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationLastModifiedDateFilter]


# ResaleAuthorizationLastModifiedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResaleAuthorizationLastModifiedDateFilterDateRange]


# ResaleAuthorizationLastModifiedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationManufacturerAccountIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationManufacturerLegalNameFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationNameFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationOfferExtendedStatusFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# ResaleAuthorizationProductIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationProductNameFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationResellerAccountIDFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationResellerLegalNameFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationSort

### SortBy
- **Type**: typing.Optional[typing.Literal['AvailabilityEndDate', 'CreatedDate', 'EntityId', 'LastModifiedDate', 'ManufacturerAccountId', 'ManufacturerLegalName', 'Name', 'OfferExtendedStatus', 'ProductId', 'ProductName', 'ResellerAccountID', 'ResellerLegalName', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ResaleAuthorizationStatusFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'Draft', 'Restricted']]]


# ResaleAuthorizationSummary

### Name
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ManufacturerAccountId
- **Type**: typing.Optional[str]

### ManufacturerLegalName
- **Type**: typing.Optional[str]

### ResellerAccountID
- **Type**: typing.Optional[str]

### ResellerLegalName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Draft', 'Restricted']]

### OfferExtendedStatus
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### AvailabilityEndDate
- **Type**: typing.Optional[str]


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# SaaSProductEntityIdFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# SaaSProductFilters

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.SaaSProductEntityIdFilter]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.SaaSProductTitleFilter]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.SaaSProductVisibilityFilter]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.SaaSProductLastModifiedDateFilter]


# SaaSProductLastModifiedDateFilter

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.SaaSProductLastModifiedDateFilterDateRange]


# SaaSProductLastModifiedDateFilterDateRange

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# SaaSProductSort

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SaaSProductSummary

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]


# SaaSProductTitleFilter

### ValueList
- **Type**: typing.Optional[typing.List[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# SaaSProductVisibilityFilter

### ValueList
- **Type**: typing.Optional[typing.List[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]]


# Sort

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# StartChangeSetRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Change]
- **Required**: Yes

### ChangeSetName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### ChangeSetTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Tag]]

### Intent
- **Type**: typing.Optional[typing.Literal['APPLY', 'VALIDATE']]


# StartChangeSetResponse

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


