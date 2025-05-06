# Workdocs Classes

# AbortDocumentVersionUploadRequest

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# ActivateUserRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# ActivateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# Activity

### Type
- **Type**: typing.Optional[typing.Literal['DOCUMENT_ANNOTATION_ADDED', 'DOCUMENT_ANNOTATION_DELETED', 'DOCUMENT_CHECKED_IN', 'DOCUMENT_CHECKED_OUT', 'DOCUMENT_COMMENT_ADDED', 'DOCUMENT_COMMENT_DELETED', 'DOCUMENT_MOVED', 'DOCUMENT_RECYCLED', 'DOCUMENT_RENAMED', 'DOCUMENT_RESTORED', 'DOCUMENT_REVERTED', 'DOCUMENT_SHAREABLE_LINK_CREATED', 'DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED', 'DOCUMENT_SHAREABLE_LINK_REMOVED', 'DOCUMENT_SHARED', 'DOCUMENT_SHARE_PERMISSION_CHANGED', 'DOCUMENT_UNSHARED', 'DOCUMENT_VERSION_DELETED', 'DOCUMENT_VERSION_DOWNLOADED', 'DOCUMENT_VERSION_UPLOADED', 'DOCUMENT_VERSION_VIEWED', 'FOLDER_CREATED', 'FOLDER_DELETED', 'FOLDER_MOVED', 'FOLDER_RECYCLED', 'FOLDER_RENAMED', 'FOLDER_RESTORED', 'FOLDER_SHAREABLE_LINK_CREATED', 'FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED', 'FOLDER_SHAREABLE_LINK_REMOVED', 'FOLDER_SHARED', 'FOLDER_SHARE_PERMISSION_CHANGED', 'FOLDER_UNSHARED']]

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]

### IsIndirectActivity
- **Type**: typing.Optional[bool]

### OrganizationId
- **Type**: typing.Optional[str]

### Initiator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.UserMetadata]

### Participants
- **Type**: <class 'NoneType'>

### ResourceMetadata
- **Type**: <class 'NoneType'>

### OriginalParent
- **Type**: <class 'NoneType'>

### CommentMetadata
- **Type**: <class 'NoneType'>


# AddResourcePermissionsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.SharePrincipal]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### NotificationOptions
- **Type**: <class 'NoneType'>


# AddResourcePermissionsResponse

### ShareResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ShareResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Comment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### RecipientId
- **Type**: typing.Optional[str]


# CommentMetadata

### CommentId
- **Type**: typing.Optional[str]

### Contributor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CommentStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']]

### RecipientId
- **Type**: typing.Optional[str]

### ContributorId
- **Type**: typing.Optional[str]


# CreateCommentRequest

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


# CreateCommentResponse

### Comment
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomMetadataRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# CreateFolderRequest

### ParentFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CreateFolderResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.FolderMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLabelsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# CreateNotificationSubscriptionRequest

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


# CreateNotificationSubscriptionResponse

### Subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.Subscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.StorageRuleType]

### AuthenticationToken
- **Type**: typing.Optional[str]


# CreateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DateRangeType

### StartValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DeactivateUserRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteCommentRequest

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


# DeleteCustomMetadataRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### Keys
- **Type**: typing.Optional[typing.List[str]]

### DeleteAll
- **Type**: typing.Optional[bool]


# DeleteDocumentRequest

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteDocumentVersionRequest

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


# DeleteFolderContentsRequest

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteFolderRequest

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DeleteLabelsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.List[str]]

### DeleteAll
- **Type**: typing.Optional[bool]


# DeleteNotificationSubscriptionRequest

### SubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# DescribeActivitiesRequest

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


# DescribeActivitiesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeActivitiesResponse

### UserActivities
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.Activity]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCommentsRequest

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


# DescribeCommentsRequestPaginate

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeCommentsResponse

### Comments
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.Comment]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDocumentVersionsRequest

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


# DescribeDocumentVersionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeDocumentVersionsResponse

### DocumentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentVersionMetadata]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFolderContentsRequest

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


# DescribeFolderContentsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeFolderContentsResponse

### Folders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.FolderMetadata]
- **Required**: Yes

### Documents
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentMetadata]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGroupsRequest

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


# DescribeGroupsRequestPaginate

### SearchQuery
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### OrganizationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.GroupMetadata]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNotificationSubscriptionsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeNotificationSubscriptionsRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeNotificationSubscriptionsResponse

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.Subscription]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourcePermissionsRequest

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


# DescribeResourcePermissionsRequestPaginate

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeResourcePermissionsResponse

### Principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.Principal]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRootFoldersRequest

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeRootFoldersRequestPaginate

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeRootFoldersResponse

### Folders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.FolderMetadata]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUsersRequest

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


# DescribeUsersRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# DescribeUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User]
- **Required**: Yes

### TotalNumberOfUsers
- **Type**: <class 'int'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentMetadata

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentVersionMetadata]

### ResourceState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RECYCLED', 'RECYCLING', 'RESTORING']]

### Labels
- **Type**: typing.Optional[typing.List[str]]


# DocumentVersionMetadata

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# Filters

### TextLocales
- **Type**: typing.Optional[typing.List[typing.Literal['AR', 'BG', 'BN', 'CS', 'DA', 'DE', 'DEFAULT', 'EL', 'EN', 'ES', 'FA', 'FI', 'FR', 'HI', 'HU', 'ID', 'IT', 'JA', 'KO', 'LT', 'LV', 'NL', 'NO', 'PT', 'RO', 'RU', 'SV', 'SW', 'TH', 'TR', 'ZH']]]

### ContentCategories
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO', 'DOCUMENT', 'IMAGE', 'OTHER', 'PDF', 'PRESENTATION', 'SOURCE_CODE', 'SPREADSHEET', 'VIDEO']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMMENT', 'DOCUMENT', 'DOCUMENT_VERSION', 'FOLDER']]]

### Labels
- **Type**: typing.Optional[typing.List[str]]

### Principals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.SearchPrincipalType]]

### AncestorIds
- **Type**: typing.Optional[typing.List[str]]

### SearchCollectionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['OWNED', 'SHARED_WITH_ME']]]

### SizeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.LongRangeType]

### CreatedRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DateRangeType]

### ModifiedRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DateRangeType]


# FolderMetadata

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


# GetCurrentUserRequest

### AuthenticationToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetCurrentUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDocumentPathRequest

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


# GetDocumentPathResponse

### Path
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResourcePath'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDocumentRequest

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### IncludeCustomMetadata
- **Type**: typing.Optional[bool]


# GetDocumentResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentMetadata'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDocumentVersionRequest

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


# GetDocumentVersionResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentVersionMetadata'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GetFolderPathRequest

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


# GetFolderPathResponse

### Path
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResourcePath'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GetFolderRequest

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]

### IncludeCustomMetadata
- **Type**: typing.Optional[bool]


# GetFolderResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.FolderMetadata'>
- **Required**: Yes

### CustomMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcesRequest

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


# GetResourcesResponse

### Folders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.FolderMetadata]
- **Required**: Yes

### Documents
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentMetadata]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# GroupMetadata

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# InitiateDocumentVersionUploadRequest

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


# InitiateDocumentVersionUploadResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.DocumentMetadata'>
- **Required**: Yes

### UploadMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.UploadMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# LongRangeType

### StartValue
- **Type**: typing.Optional[int]

### EndValue
- **Type**: typing.Optional[int]


# NotificationOptions

### SendEmail
- **Type**: typing.Optional[bool]

### EmailMessage
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Participants

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.UserMetadata]]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.GroupMetadata]]


# PermissionInfo

### Role
- **Type**: typing.Optional[typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']]

### Type
- **Type**: typing.Optional[typing.Literal['DIRECT', 'INHERITED']]


# Principal

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ANONYMOUS', 'GROUP', 'INVITE', 'ORGANIZATION', 'USER']]

### Roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PermissionInfo]]


# RemoveAllResourcePermissionsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# RemoveResourcePermissionRequest

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


# ResourceMetadata

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.UserMetadata]

### ParentId
- **Type**: typing.Optional[str]


# ResourcePath

### Components
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResourcePathComponent]]


# ResourcePathComponent

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ResponseItem

### ResourceType
- **Type**: typing.Optional[typing.Literal['COMMENT', 'DOCUMENT', 'DOCUMENT_VERSION', 'FOLDER']]

### WebUrl
- **Type**: typing.Optional[str]

### DocumentMetadata
- **Type**: <class 'NoneType'>

### FolderMetadata
- **Type**: <class 'NoneType'>

### CommentMetadata
- **Type**: <class 'NoneType'>

### DocumentVersionMetadata
- **Type**: <class 'NoneType'>


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


# RestoreDocumentVersionsRequest

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationToken
- **Type**: typing.Optional[str]


# SearchPrincipalType

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.List[typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']]]


# SearchResourcesRequest

### AuthenticationToken
- **Type**: typing.Optional[str]

### QueryText
- **Type**: typing.Optional[str]

### QueryScopes
- **Type**: typing.Optional[typing.List[typing.Literal['CONTENT', 'NAME']]]

### OrganizationId
- **Type**: typing.Optional[str]

### AdditionalResponseFields
- **Type**: typing.Optional[typing.List[typing.Literal['WEBURL']]]

### Filters
- **Type**: <class 'NoneType'>

### OrderBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.SearchSortResult]]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# SearchResourcesRequestPaginate

### AuthenticationToken
- **Type**: typing.Optional[str]

### QueryText
- **Type**: typing.Optional[str]

### QueryScopes
- **Type**: typing.Optional[typing.List[typing.Literal['CONTENT', 'NAME']]]

### OrganizationId
- **Type**: typing.Optional[str]

### AdditionalResponseFields
- **Type**: typing.Optional[typing.List[typing.Literal['WEBURL']]]

### Filters
- **Type**: <class 'NoneType'>

### OrderBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.SearchSortResult]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.PaginatorConfig]


# SearchResourcesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseItem]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# SearchSortResult

### Field
- **Type**: typing.Optional[typing.Literal['CREATED_TIMESTAMP', 'MODIFIED_TIMESTAMP', 'NAME', 'RELEVANCE', 'SIZE']]

### Order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SharePrincipal

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ANONYMOUS', 'GROUP', 'INVITE', 'ORGANIZATION', 'USER']
- **Required**: Yes

### Role
- **Type**: typing.Literal['CONTRIBUTOR', 'COOWNER', 'OWNER', 'VIEWER']
- **Required**: Yes


# ShareResult

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


# StorageRuleType

### StorageAllocatedInBytes
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[typing.Literal['QUOTA', 'UNLIMITED']]


# Subscription

### SubscriptionId
- **Type**: typing.Optional[str]

### EndPoint
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['HTTPS', 'SQS']]


# UpdateDocumentRequest

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


# UpdateDocumentVersionRequest

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


# UpdateFolderRequest

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


# UpdateUserRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.StorageRuleType]

### TimeZoneId
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[typing.Literal['de', 'default', 'en', 'es', 'fr', 'ja', 'ko', 'pt_BR', 'ru', 'zh_CN', 'zh_TW']]

### GrantPoweruserPrivileges
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


# UpdateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workdocs.workdocs_classes.ResponseMetadata'>
- **Required**: Yes


# UploadMetadata

### UploadUrl
- **Type**: typing.Optional[str]

### SignedHeaders
- **Type**: typing.Optional[typing.Dict[str, str]]


# User

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.UserStorageMetadata]


# UserMetadata

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


# UserStorageMetadata

### StorageUtilizedInBytes
- **Type**: typing.Optional[int]

### StorageRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workdocs.workdocs_classes.StorageRuleType]


