# Marketplace Catalog Classes

# AmiProductEntityIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# AmiProductFiltersTypeDef

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductEntityIdFilterTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductLastModifiedDateFilterTypeDef]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductTitleFilterTypeDef]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductVisibilityFilterTypeDef]


# AmiProductLastModifiedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# AmiProductLastModifiedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductLastModifiedDateFilterDateRangeTypeDef]


# AmiProductSortTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# AmiProductSummaryTypeDef

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]


# AmiProductTitleFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# AmiProductVisibilityFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDescribeEntitiesRequestTypeDef

### EntityRequestList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityRequestTypeDef]
- **Required**: Yes


# BatchDescribeEntitiesResponseTypeDef

### EntityDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityDetailTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.marketplace_catalog_classes.BatchDescribeErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDescribeErrorDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# CancelChangeSetRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelChangeSetResponseTypeDef

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChangeSetSummaryListItemTypeDef

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


# ChangeSummaryTypeDef

### ChangeType
- **Type**: typing.Optional[str]

### Entity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityTypeDef]

### Details
- **Type**: typing.Optional[str]

### DetailsDocument
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ErrorDetailList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ErrorDetailTypeDef]]

### ChangeName
- **Type**: typing.Optional[str]


# ChangeTypeDef

### ChangeType
- **Type**: <class 'str'>
- **Required**: Yes

### Entity
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityTypeDef'>
- **Required**: Yes

### EntityTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.TagTypeDef]]

### Details
- **Type**: typing.Optional[str]

### DetailsDocument
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ChangeName
- **Type**: typing.Optional[str]


# ContainerProductEntityIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# ContainerProductFiltersTypeDef

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductEntityIdFilterTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductLastModifiedDateFilterTypeDef]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductTitleFilterTypeDef]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductVisibilityFilterTypeDef]


# ContainerProductLastModifiedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ContainerProductLastModifiedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductLastModifiedDateFilterDateRangeTypeDef]


# ContainerProductSortTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ContainerProductSummaryTypeDef

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]


# ContainerProductTitleFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ContainerProductVisibilityFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]]


# DataProductEntityIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# DataProductFiltersTypeDef

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductEntityIdFilterTypeDef]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductTitleFilterTypeDef]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductVisibilityFilterTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductLastModifiedDateFilterTypeDef]


# DataProductLastModifiedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# DataProductLastModifiedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductLastModifiedDateFilterDateRangeTypeDef]


# DataProductSortTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# DataProductSummaryTypeDef

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted', 'Unavailable']]


# DataProductTitleFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# DataProductVisibilityFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Draft', 'Limited', 'Public', 'Restricted', 'Unavailable']]]


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChangeSetRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChangeSetResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ChangeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntityRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntityResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityDetailTypeDef

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


# EntityRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# EntitySummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductSummaryTypeDef]

### ContainerProductSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductSummaryTypeDef]

### DataProductSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductSummaryTypeDef]

### SaaSProductSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductSummaryTypeDef]

### OfferSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferSummaryTypeDef]

### ResaleAuthorizationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationSummaryTypeDef]


# EntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityTypeFiltersTypeDef

### DataProductFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductFiltersTypeDef]

### SaaSProductFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductFiltersTypeDef]

### AmiProductFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductFiltersTypeDef]

### OfferFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferFiltersTypeDef]

### ContainerProductFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductFiltersTypeDef]

### ResaleAuthorizationFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationFiltersTypeDef]


# EntityTypeSortTypeDef

### DataProductSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.DataProductSortTypeDef]

### SaaSProductSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductSortTypeDef]

### AmiProductSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.AmiProductSortTypeDef]

### OfferSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferSortTypeDef]

### ContainerProductSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ContainerProductSortTypeDef]

### ResaleAuthorizationSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationSortTypeDef]


# ErrorDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FilterTypeDef

### Name
- **Type**: typing.Optional[str]

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# GetResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChangeSetsRequestPaginateTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.FilterTypeDef]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.PaginatorConfigTypeDef]


# ListChangeSetsRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.FilterTypeDef]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SortTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChangeSetsResponseTypeDef

### ChangeSetSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ChangeSetSummaryListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitiesRequestPaginateTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.FilterTypeDef]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SortTypeDef]

### OwnershipType
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### EntityTypeFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityTypeFiltersTypeDef]

### EntityTypeSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityTypeSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.PaginatorConfigTypeDef]


# ListEntitiesRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: <class 'str'>
- **Required**: Yes

### FilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.FilterTypeDef]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SortTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### OwnershipType
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### EntityTypeFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityTypeFiltersTypeDef]

### EntityTypeSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntityTypeSortTypeDef]


# ListEntitiesResponseTypeDef

### EntitySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog_classes.EntitySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_catalog_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OfferAvailabilityEndDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# OfferAvailabilityEndDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferAvailabilityEndDateFilterDateRangeTypeDef]


# OfferBuyerAccountsFilterTypeDef

### WildCardValue
- **Type**: typing.Optional[str]


# OfferEntityIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# OfferFiltersTypeDef

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferEntityIdFilterTypeDef]

### Name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferNameFilterTypeDef]

### ProductId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferProductIdFilterTypeDef]

### ResaleAuthorizationId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferResaleAuthorizationIdFilterTypeDef]

### ReleaseDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferReleaseDateFilterTypeDef]

### AvailabilityEndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferAvailabilityEndDateFilterTypeDef]

### BuyerAccounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferBuyerAccountsFilterTypeDef]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferStateFilterTypeDef]

### Targeting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferTargetingFilterTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferLastModifiedDateFilterTypeDef]


# OfferLastModifiedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# OfferLastModifiedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferLastModifiedDateFilterDateRangeTypeDef]


# OfferNameFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# OfferProductIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# OfferReleaseDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# OfferReleaseDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.OfferReleaseDateFilterDateRangeTypeDef]


# OfferResaleAuthorizationIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# OfferSortTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['AvailabilityEndDate', 'BuyerAccounts', 'EntityId', 'LastModifiedDate', 'Name', 'ProductId', 'ReleaseDate', 'ResaleAuthorizationId', 'State', 'Targeting']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# OfferStateFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Draft', 'Released']]]


# OfferSummaryTypeDef

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


# OfferTargetingFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BuyerAccounts', 'CountryCodes', 'None', 'ParticipatingPrograms']]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationAvailabilityEndDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef]

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# ResaleAuthorizationCreatedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationCreatedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationCreatedDateFilterDateRangeTypeDef]

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# ResaleAuthorizationEntityIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# ResaleAuthorizationFiltersTypeDef

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationEntityIdFilterTypeDef]

### Name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationNameFilterTypeDef]

### ProductId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationProductIdFilterTypeDef]

### CreatedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationCreatedDateFilterTypeDef]

### AvailabilityEndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationAvailabilityEndDateFilterTypeDef]

### ManufacturerAccountId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationManufacturerAccountIdFilterTypeDef]

### ProductName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationProductNameFilterTypeDef]

### ManufacturerLegalName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationManufacturerLegalNameFilterTypeDef]

### ResellerAccountID
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationResellerAccountIDFilterTypeDef]

### ResellerLegalName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationResellerLegalNameFilterTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationStatusFilterTypeDef]

### OfferExtendedStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationOfferExtendedStatusFilterTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationLastModifiedDateFilterTypeDef]


# ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationLastModifiedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef]


# ResaleAuthorizationManufacturerAccountIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationManufacturerLegalNameFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationNameFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationOfferExtendedStatusFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# ResaleAuthorizationProductIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationProductNameFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationResellerAccountIDFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationResellerLegalNameFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# ResaleAuthorizationSortTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['AvailabilityEndDate', 'CreatedDate', 'EntityId', 'LastModifiedDate', 'ManufacturerAccountId', 'ManufacturerLegalName', 'Name', 'OfferExtendedStatus', 'ProductId', 'ProductName', 'ResellerAccountID', 'ResellerLegalName', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ResaleAuthorizationStatusFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Draft', 'Restricted']]]


# ResaleAuthorizationSummaryTypeDef

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


# ResponseMetadataTypeDef

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


# SaaSProductEntityIdFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# SaaSProductFiltersTypeDef

### EntityId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductEntityIdFilterTypeDef]

### ProductTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductTitleFilterTypeDef]

### Visibility
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductVisibilityFilterTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductLastModifiedDateFilterTypeDef]


# SaaSProductLastModifiedDateFilterDateRangeTypeDef

### AfterValue
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]


# SaaSProductLastModifiedDateFilterTypeDef

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_catalog_classes.SaaSProductLastModifiedDateFilterDateRangeTypeDef]


# SaaSProductSortTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['EntityId', 'LastModifiedDate', 'ProductTitle', 'Visibility']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SaaSProductSummaryTypeDef

### ProductTitle
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]


# SaaSProductTitleFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]

### WildCardValue
- **Type**: typing.Optional[str]


# SaaSProductVisibilityFilterTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Draft', 'Limited', 'Public', 'Restricted']]]


# SortTypeDef

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# StartChangeSetRequestTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSet
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.ChangeTypeDef]
- **Required**: Yes

### ChangeSetName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### ChangeSetTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.TagTypeDef]]

### Intent
- **Type**: typing.Optional[typing.Literal['APPLY', 'VALIDATE']]


# StartChangeSetResponseTypeDef

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_catalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.marketplace_catalog_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


