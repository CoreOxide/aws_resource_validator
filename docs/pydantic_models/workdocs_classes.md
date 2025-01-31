# workdocs_classes

# AbortDocumentVersionUploadRequestRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# ActivateUserRequestRequestTypeDef

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

### Type
- **Type**: typing.Optional[typing.Literal['DOCUMENT_ANNOTATION_ADDED', 'DOCUMENT_ANNOTATION_DELETED', 'DOCUMENT_CHECKED_IN', 'DOCUMENT_CHECKED_OUT', 'DOCUMENT_COMMENT_ADDED', 'DOCUMENT_COMMENT_DELETED', 'DOCUMENT_MOVED', 'DOCUMENT_RECYCLED', 'DOCUMENT_RENAMED', 'DOCUMENT_RESTORED', 'DOCUMENT_REVERTED', 'DOCUMENT_SHAREABLE_LINK_CREATED', 'DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED', 'DOCUMENT_SHAREABLE_LINK_REMOVED', 'DOCUMENT_SHARED', 'DOCUMENT_SHARE_PERMISSION_CHANGED', 'DOCUMENT_UNSHARED', 'DOCUMENT_VERSION_DELETED', 'DOCUMENT_VERSION_DOWNLOADED', 'DOCUMENT_VERSION_UPLOADED', 'DOCUMENT_VERSION_VIEWED', 'FOLDER_CREATED', 'FOLDER_DELETED', 'FOLDER_MOVED', 'FOLDER_RECYCLED', 'FOLDER_RENAMED', 'FOLDER_RESTORED', 'FOLDER_SHAREABLE_LINK_CREATED', 'FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED', 'FOLDER_SHAREABLE_LINK_REMOVED', 'FOLDER_SHARED', 'FOLDER_SHARE_PERMISSION_CHANGED', 'FOLDER_UNSHARED']]

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]

### IsIndirectActivity
- **Type**: typing.Optional[bool]

### OrganizationId
- **Type**: typing.Optional[str]

### Initiator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.UserMetadataTypeDef]

### Participants
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.ParticipantsTypeDef]

### ResourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.ResourceMetadataTypeDef]

### OriginalParent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.ResourceMetadataTypeDef]

### CommentMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.CommentMetadataTypeDef]


# AddResourcePermissionsRequestRequestTypeDef

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

### CommentId
- **Type**: <class 'str'>
- **Required**: Yes

### ParentId
- **Type**: typing.Optional[str]

### ThreadId
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### Contributor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.UserTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### RecipientId
- **Type**: typing.Optional[str]


# CreateCommentRequestRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### ParentId
- **Type**: typing.Optional[str]

### ThreadId
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### NotifyCollaborators
- **Type**: typing.Optional[bool]


# CreateCommentResponseTypeDef

### Comment
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomMetadataRequestRequestTypeDef

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


# CreateFolderRequestRequestTypeDef

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


# CreateLabelsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Labels
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# CreateNotificationSubscriptionRequestRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['HTTPS', 'SQS']
- **Required**: Yes

### SubscriptionType
- **Type**: typing.Literal['ALL']
- **Required**: Yes


# CreateNotificationSubscriptionResponseTypeDef

### Subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.SubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DeactivateUserRequestRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteCommentRequestRequestTypeDef

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


# DeleteCustomMetadataRequestRequestTypeDef

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


# DeleteDocumentRequestRequestTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteDocumentVersionRequestRequestTypeDef

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


# DeleteFolderContentsRequestRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteFolderRequestRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteLabelsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### DeleteAll
- **Type**: typing.Optional[bool]


# DeleteNotificationSubscriptionRequestRequestTypeDef

### SubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DescribeActivitiesRequestDescribeActivitiesPaginateTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# DescribeActivitiesRequestRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# DescribeCommentsRequestDescribeCommentsPaginateTypeDef

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


# DescribeCommentsRequestRequestTypeDef

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


# DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateTypeDef

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


# DescribeDocumentVersionsRequestRequestTypeDef

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


# DescribeFolderContentsRequestDescribeFolderContentsPaginateTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[typing.Literal['DATE', 'NAME']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'DOCUMENT', 'FOLDER']]

### Include
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeFolderContentsRequestRequestTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[typing.Literal['DATE', 'NAME']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'DOCUMENT', 'FOLDER']]

### Include
- **Type**: typing.Optional[str]


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


# DescribeGroupsRequestDescribeGroupsPaginateTypeDef

### SearchQuery
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeGroupsRequestRequestTypeDef

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


# DescribeNotificationSubscriptionsRequestRequestTypeDef

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


# DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeResourcePermissionsRequestRequestTypeDef

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


# DescribeRootFoldersRequestDescribeRootFoldersPaginateTypeDef

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.PaginatorConfigTypeDef]


# DescribeRootFoldersRequestRequestTypeDef

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


# DescribeUsersRequestDescribeUsersPaginateTypeDef

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


# DescribeUsersRequestRequestTypeDef

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


# GetCurrentUserRequestRequestTypeDef

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


# GetDocumentPathRequestRequestTypeDef

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


# GetDocumentRequestRequestTypeDef

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


# GetDocumentVersionRequestRequestTypeDef

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


# GetFolderPathRequestRequestTypeDef

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


# GetFolderRequestRequestTypeDef

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


# GetResourcesRequestRequestTypeDef

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


# InitiateDocumentVersionUploadRequestRequestTypeDef

### AuthenticationToken
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ContentCreatedTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ContentModifiedTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# PermissionInfoTypeDef

### Role
- **Type**: typing.Optional[typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']]

### Type
- **Type**: typing.Optional[typing.Literal['DIRECT', 'INHERITED']]


# PrincipalTypeDef

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ANONYMOUS', 'GROUP', 'INVITE', 'ORGANIZATION', 'USER']]

### Roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs_classes.PermissionInfoTypeDef]]


# RemoveAllResourcePermissionsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# RemoveResourcePermissionRequestRequestTypeDef

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


# ResourceMetadataTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['DOCUMENT', 'FOLDER']]

### Name
- **Type**: typing.Optional[str]

### OriginalName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.UserMetadataTypeDef]

### ParentId
- **Type**: typing.Optional[str]


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

### HostId
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


# RestoreDocumentVersionsRequestRequestTypeDef

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


# SearchResourcesRequestRequestTypeDef

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


# SearchResourcesRequestSearchResourcesPaginateTypeDef

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

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ANONYMOUS', 'GROUP', 'INVITE', 'ORGANIZATION', 'USER']
- **Required**: Yes

### Role
- **Type**: typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']
- **Required**: Yes


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

### SubscriptionId
- **Type**: typing.Optional[str]

### EndPoint
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['HTTPS', 'SQS']]


# UpdateDocumentRequestRequestTypeDef

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


# UpdateDocumentVersionRequestRequestTypeDef

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


# UpdateFolderRequestRequestTypeDef

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


# UpdateUserRequestRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ADMIN', 'MINIMALUSER', 'POWERUSER', 'USER', 'WORKSPACESUSER']]

### StorageRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.StorageRuleTypeTypeDef]

### TimeZoneId
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[typing.Literal['de', 'default', 'en', 'es', 'fr', 'ja', 'ko', 'pt_BR', 'ru', 'zh_CN', 'zh_TW']]

### GrantPoweruserPrivileges
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


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

### Id
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### RootFolderId
- **Type**: typing.Optional[str]

### RecycleBinFolderId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING']]

### Type
- **Type**: typing.Optional[typing.Literal['ADMIN', 'MINIMALUSER', 'POWERUSER', 'USER', 'WORKSPACESUSER']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### TimeZoneId
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[typing.Literal['de', 'default', 'en', 'es', 'fr', 'ja', 'ko', 'pt_BR', 'ru', 'zh_CN', 'zh_TW']]

### Storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs_classes.UserStorageMetadataTypeDef]


