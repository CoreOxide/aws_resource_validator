# Workdocs Classes

# AbortDocumentVersionUploadRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# ActivateUserRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# ActivateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddResourcePermissionsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Principals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workdocs_classes.SharePrincipalTypeDef]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### NotificationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.NotificationOptionsTypeDef]


# AddResourcePermissionsResponseTypeDef

### ShareResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.ShareResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommentMetadataTypeDef

### CommentId
- **Type**: typing.Optional[str]

### Contributor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CommentStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']]

### RecipientId
- **Type**: typing.Optional[str]

### ContributorId
- **Type**: typing.Optional[str]


# CommentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCommentResponseTypeDef

### Comment
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomMetadataRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# CreateFolderRequestTypeDef

### ParentFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CreateFolderResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.FolderMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLabelsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Labels
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# CreateNotificationSubscriptionResponseTypeDef

### Subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.SubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GivenName
- **Type**: <class 'str'>
- **Required**: Yes

### Surname
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### TimeZoneId
- **Type**: typing.Optional[str]

### StorageRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.StorageRuleTypeTypeDef]

### AuthenticationToken
- **Type**: typing.Optional[str]


# CreateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DateRangeTypeTypeDef

### StartValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### EndValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]


# DeactivateUserRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteCommentRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### CommentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteCustomMetadataRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### Keys
- **Type**: typing.Optional[typing.Sequence[str]]

### DeleteAll
- **Type**: typing.Optional[bool]


# DeleteDocumentRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteDocumentVersionRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletePriorVersions
- **Type**: <class 'bool'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteFolderContentsRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteFolderRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteLabelsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### DeleteAll
- **Type**: typing.Optional[bool]


# DeleteNotificationSubscriptionRequestTypeDef

### SubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DescribeActivitiesRequestPaginateTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### OrganizationId
- **Type**: typing.Optional[str]

### ActivityTypes
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### IncludeIndirectActivities
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeActivitiesRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### OrganizationId
- **Type**: typing.Optional[str]

### ActivityTypes
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### IncludeIndirectActivities
- **Type**: typing.Optional[bool]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeActivitiesResponseTypeDef

### UserActivities
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.ActivityTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCommentsRequestPaginateTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeCommentsRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCommentsResponseTypeDef

### Comments
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.CommentTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDocumentVersionsRequestPaginateTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Include
- **Type**: typing.Optional[str]

### Fields
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeDocumentVersionsRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Include
- **Type**: typing.Optional[str]

### Fields
- **Type**: typing.Optional[str]


# DescribeDocumentVersionsResponseTypeDef

### DocumentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.DocumentVersionMetadataTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFolderContentsResponseTypeDef

### Folders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.FolderMetadataTypeDef]
- **Required**: Yes

### Documents
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.DocumentMetadataTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGroupsRequestPaginateTypeDef

### SearchQuery
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeGroupsRequestTypeDef

### SearchQuery
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.GroupMetadataTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNotificationSubscriptionsRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeNotificationSubscriptionsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeNotificationSubscriptionsResponseTypeDef

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.SubscriptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePermissionsRequestPaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeResourcePermissionsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeResourcePermissionsResponseTypeDef

### Principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.PrincipalTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRootFoldersRequestPaginateTypeDef

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeRootFoldersRequestTypeDef

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeRootFoldersResponseTypeDef

### Folders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.FolderMetadataTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUsersRequestPaginateTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### UserIds
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### Include
- **Type**: typing.Optional[typing.Literal['ACTIVE_PENDING', 'ALL']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Sort
- **Type**: typing.Optional[typing.Literal['FULL_NAME', 'STORAGE_LIMIT', 'STORAGE_USED', 'USER_NAME', 'USER_STATUS']]

### Fields
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeUsersRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### UserIds
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### Include
- **Type**: typing.Optional[typing.Literal['ACTIVE_PENDING', 'ALL']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Sort
- **Type**: typing.Optional[typing.Literal['FULL_NAME', 'STORAGE_LIMIT', 'STORAGE_USED', 'USER_NAME', 'USER_STATUS']]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Fields
- **Type**: typing.Optional[str]


# DescribeUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef]
- **Required**: Yes

### TotalNumberOfUsers
- **Type**: <class 'int'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### CreatorId
- **Type**: typing.Optional[str]

### ParentFolderId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LatestVersionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.DocumentVersionMetadataTypeDef]

### ResourceState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RECYCLED', 'RECYCLING', 'RESTORING']]

### Labels
- **Type**: typing.Optional[typing.List[str]]


# DocumentVersionMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[int]

### Signature
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INITIALIZED']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ContentCreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ContentModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatorId
- **Type**: typing.Optional[str]

### Thumbnail
- **Type**: typing.Optional[typing.Dict[typing.Literal['LARGE', 'SMALL', 'SMALL_HQ'], str]]

### Source
- **Type**: typing.Optional[typing.Dict[typing.Literal['ORIGINAL', 'WITH_COMMENTS'], str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FiltersTypeDef

### TextLocales
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AR', 'BG', 'BN', 'CS', 'DA', 'DE', 'DEFAULT', 'EL', 'EN', 'ES', 'FA', 'FI', 'FR', 'HI', 'HU', 'ID', 'IT', 'JA', 'KO', 'LT', 'LV', 'NL', 'NO', 'PT', 'RO', 'RU', 'SV', 'SW', 'TH', 'TR', 'ZH']]]

### ContentCategories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AUDIO', 'DOCUMENT', 'IMAGE', 'OTHER', 'PDF', 'PRESENTATION', 'SOURCE_CODE', 'SPREADSHEET', 'VIDEO']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMMENT', 'DOCUMENT', 'DOCUMENT_VERSION', 'FOLDER']]]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### Principals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workdocs_classes.SearchPrincipalTypeTypeDef]]

### AncestorIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SearchCollectionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['OWNED', 'SHARED_WITH_ME']]]

### SizeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.LongRangeTypeTypeDef]

### CreatedRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.DateRangeTypeTypeDef]

### ModifiedRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.DateRangeTypeTypeDef]


# FolderMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatorId
- **Type**: typing.Optional[str]

### ParentFolderId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ResourceState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RECYCLED', 'RECYCLING', 'RESTORING']]

### Signature
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.List[str]]

### Size
- **Type**: typing.Optional[int]

### LatestVersionSize
- **Type**: typing.Optional[int]


# GetCurrentUserRequestTypeDef

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetCurrentUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDocumentPathRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Fields
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# GetDocumentPathResponseTypeDef

### Path
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResourcePathTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDocumentRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### IncludeCustomMetadata
- **Type**: typing.Optional[bool]


# GetDocumentResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDocumentVersionRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Fields
- **Type**: typing.Optional[str]

### IncludeCustomMetadata
- **Type**: typing.Optional[bool]


# GetDocumentVersionResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.DocumentVersionMetadataTypeDef'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFolderPathRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Fields
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# GetFolderPathResponseTypeDef

### Path
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResourcePathTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFolderRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### IncludeCustomMetadata
- **Type**: typing.Optional[bool]


# GetFolderResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.FolderMetadataTypeDef'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcesRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### CollectionType
- **Type**: typing.Optional[typing.Literal['SHARED_WITH_ME']]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetResourcesResponseTypeDef

### Folders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.FolderMetadataTypeDef]
- **Required**: Yes

### Documents
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.DocumentMetadataTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# InitiateDocumentVersionUploadRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ContentCreatedTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### ContentModifiedTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.TimestampTypeDef]

### ContentType
- **Type**: typing.Optional[str]

### DocumentSizeInBytes
- **Type**: typing.Optional[int]

### ParentFolderId
- **Type**: typing.Optional[str]


# InitiateDocumentVersionUploadResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### UploadMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.UploadMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LongRangeTypeTypeDef

### StartValue
- **Type**: typing.Optional[int]

### EndValue
- **Type**: typing.Optional[int]


# NotificationOptionsTypeDef

### SendEmail
- **Type**: typing.Optional[bool]

### EmailMessage
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipantsTypeDef

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs_classes.UserMetadataTypeDef]]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs_classes.GroupMetadataTypeDef]]


# PrincipalTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemoveAllResourcePermissionsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# RemoveResourcePermissionRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['ANONYMOUS', 'GROUP', 'INVITE', 'ORGANIZATION', 'USER']]


# ResourcePathComponentTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ResourcePathTypeDef

### Components
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs_classes.ResourcePathComponentTypeDef]]


# ResponseItemTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['COMMENT', 'DOCUMENT', 'DOCUMENT_VERSION', 'FOLDER']]

### WebUrl
- **Type**: typing.Optional[str]

### DocumentMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.DocumentMetadataTypeDef]

### FolderMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.FolderMetadataTypeDef]

### CommentMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.CommentMetadataTypeDef]

### DocumentVersionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.DocumentVersionMetadataTypeDef]


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


# RestoreDocumentVersionsRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# SearchPrincipalTypeTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']]]


# SearchResourcesRequestPaginateTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### QueryText
- **Type**: typing.Optional[str]

### QueryScopes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTENT', 'NAME']]]

### OrganizationId
- **Type**: typing.Optional[str]

### AdditionalResponseFields
- **Type**: typing.Optional[typing.Sequence[typing.Literal['WEBURL']]]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.FiltersTypeDef]

### OrderBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workdocs_classes.SearchSortResultTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# SearchResourcesRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### QueryText
- **Type**: typing.Optional[str]

### QueryScopes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTENT', 'NAME']]]

### OrganizationId
- **Type**: typing.Optional[str]

### AdditionalResponseFields
- **Type**: typing.Optional[typing.Sequence[typing.Literal['WEBURL']]]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.FiltersTypeDef]

### OrderBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workdocs_classes.SearchSortResultTypeDef]]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# SearchResourcesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs_classes.ResponseItemTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchSortResultTypeDef

### Field
- **Type**: typing.Optional[typing.Literal['CREATED_TIMESTAMP', 'MODIFIED_TIMESTAMP', 'NAME', 'RELEVANCE', 'SIZE']]

### Order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SharePrincipalTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ShareResultTypeDef

### PrincipalId
- **Type**: typing.Optional[str]

### InviteePrincipalId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILURE', 'SUCCESS']]

### ShareId
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# StorageRuleTypeTypeDef

### StorageAllocatedInBytes
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[typing.Literal['QUOTA', 'UNLIMITED']]


# SubscriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateDocumentRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ParentFolderId
- **Type**: typing.Optional[str]

### ResourceState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RECYCLED', 'RECYCLING', 'RESTORING']]


# UpdateDocumentVersionRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### VersionStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE']]


# UpdateFolderRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ParentFolderId
- **Type**: typing.Optional[str]

### ResourceState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RECYCLED', 'RECYCLING', 'RESTORING']]


# UpdateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadMetadataTypeDef

### UploadUrl
- **Type**: typing.Optional[str]

### SignedHeaders
- **Type**: typing.Optional[typing.Dict[str, str]]


# UserMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]


# UserStorageMetadataTypeDef

### StorageUtilizedInBytes
- **Type**: typing.Optional[int]

### StorageRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.StorageRuleTypeTypeDef]


# UserTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

