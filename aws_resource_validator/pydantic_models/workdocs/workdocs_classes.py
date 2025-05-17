from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workdocs.workdocs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'abort_document_version_upload' function.
class AbortDocumentVersionUploadRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'activate_user' function.
class ActivateUserRequest(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UserMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Username: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    EmailAddress: Optional[str] = None


class NotificationOptions(BaseValidatorModel):
    SendEmail: Optional[bool] = None
    EmailMessage: Optional[str] = None


class SharePrincipal(BaseValidatorModel):
    Id: str
    Type: PrincipalTypeType
    Role: RoleTypeType


class ShareResult(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    InviteePrincipalId: Optional[str] = None
    Role: Optional[RoleTypeType] = None
    Status: Optional[ShareStatusTypeType] = None
    ShareId: Optional[str] = None
    StatusMessage: Optional[str] = None


# This class is the input for the 'create_comment' function.
class CreateCommentRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    Text: str
    AuthenticationToken: Optional[str] = None
    ParentId: Optional[str] = None
    ThreadId: Optional[str] = None
    Visibility: Optional[CommentVisibilityTypeType] = None
    NotifyCollaborators: Optional[bool] = None


class CreateCustomMetadataRequest(BaseValidatorModel):
    ResourceId: str
    CustomMetadata: Dict[str, str]
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None


# This class is the input for the 'create_folder' function.
class CreateFolderRequest(BaseValidatorModel):
    ParentFolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None


class FolderMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    CreatorId: Optional[str] = None
    ParentFolderId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    ModifiedTimestamp: Optional[datetime] = None
    ResourceState: Optional[ResourceStateTypeType] = None
    Signature: Optional[str] = None
    Labels: Optional[List[str]] = None
    Size: Optional[int] = None
    LatestVersionSize: Optional[int] = None


class CreateLabelsRequest(BaseValidatorModel):
    ResourceId: str
    Labels: List[str]
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'create_notification_subscription' function.
class CreateNotificationSubscriptionRequest(BaseValidatorModel):
    OrganizationId: str
    Endpoint: str
    Protocol: SubscriptionProtocolTypeType
    SubscriptionType: Literal['ALL']


class Subscription(BaseValidatorModel):
    SubscriptionId: Optional[str] = None
    EndPoint: Optional[str] = None
    Protocol: Optional[SubscriptionProtocolTypeType] = None


class StorageRuleType(BaseValidatorModel):
    StorageAllocatedInBytes: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'deactivate_user' function.
class DeactivateUserRequest(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'delete_comment' function.
class DeleteCommentRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    CommentId: str
    AuthenticationToken: Optional[str] = None


class DeleteCustomMetadataRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None
    Keys: Optional[List[str]] = None
    DeleteAll: Optional[bool] = None


# This class is the input for the 'delete_document' function.
class DeleteDocumentRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'delete_document_version' function.
class DeleteDocumentVersionRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    DeletePriorVersions: bool
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'delete_folder_contents' function.
class DeleteFolderContentsRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'delete_folder' function.
class DeleteFolderRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None


class DeleteLabelsRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    Labels: Optional[List[str]] = None
    DeleteAll: Optional[bool] = None


# This class is the input for the 'delete_notification_subscription' function.
class DeleteNotificationSubscriptionRequest(BaseValidatorModel):
    SubscriptionId: str
    OrganizationId: str


# This class is the input for the 'delete_user' function.
class DeleteUserRequest(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_comments' function.
class DescribeCommentsRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_document_versions' function.
class DescribeDocumentVersionsRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None


class DocumentVersionMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    ContentType: Optional[str] = None
    Size: Optional[int] = None
    Signature: Optional[str] = None
    Status: Optional[DocumentStatusTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    ModifiedTimestamp: Optional[datetime] = None
    ContentCreatedTimestamp: Optional[datetime] = None
    ContentModifiedTimestamp: Optional[datetime] = None
    CreatorId: Optional[str] = None
    Thumbnail: Optional[Dict[DocumentThumbnailTypeType, str]] = None
    Source: Optional[Dict[DocumentSourceTypeType, str]] = None


# This class is the input for the 'describe_folder_contents' function.
class DescribeFolderContentsRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Sort: Optional[ResourceSortTypeType] = None
    Order: Optional[OrderTypeType] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None
    Type: Optional[FolderContentTypeType] = None
    Include: Optional[str] = None


# This class is the input for the 'describe_groups' function.
class DescribeGroupsRequest(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class GroupMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'describe_notification_subscriptions' function.
class DescribeNotificationSubscriptionsRequest(BaseValidatorModel):
    OrganizationId: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_resource_permissions' function.
class DescribeResourcePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_root_folders' function.
class DescribeRootFoldersRequest(BaseValidatorModel):
    AuthenticationToken: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_users' function.
class DescribeUsersRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    UserIds: Optional[str] = None
    Query: Optional[str] = None
    Include: Optional[UserFilterTypeType] = None
    Order: Optional[OrderTypeType] = None
    Sort: Optional[UserSortTypeType] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None


class LongRangeType(BaseValidatorModel):
    StartValue: Optional[int] = None
    EndValue: Optional[int] = None


class SearchPrincipalType(BaseValidatorModel):
    Id: str
    Roles: Optional[List[PrincipalRoleTypeType]] = None


# This class is the input for the 'get_current_user' function.
class GetCurrentUserRequest(BaseValidatorModel):
    AuthenticationToken: str


# This class is the input for the 'get_document_path' function.
class GetDocumentPathRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None


# This class is the input for the 'get_document' function.
class GetDocumentRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


# This class is the input for the 'get_document_version' function.
class GetDocumentVersionRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Fields: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


# This class is the input for the 'get_folder_path' function.
class GetFolderPathRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None


# This class is the input for the 'get_folder' function.
class GetFolderRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


# This class is the input for the 'get_resources' function.
class GetResourcesRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    UserId: Optional[str] = None
    CollectionType: Optional[Literal['SHARED_WITH_ME']] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class UploadMetadata(BaseValidatorModel):
    UploadUrl: Optional[str] = None
    SignedHeaders: Optional[Dict[str, str]] = None


class PermissionInfo(BaseValidatorModel):
    Role: Optional[RoleTypeType] = None
    Type: Optional[RolePermissionTypeType] = None


# This class is the input for the 'remove_all_resource_permissions' function.
class RemoveAllResourcePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'remove_resource_permission' function.
class RemoveResourcePermissionRequest(BaseValidatorModel):
    ResourceId: str
    PrincipalId: str
    AuthenticationToken: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ResourcePathComponent(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'restore_document_versions' function.
class RestoreDocumentVersionsRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None


class SearchSortResult(BaseValidatorModel):
    Field: Optional[OrderByFieldTypeType] = None
    Order: Optional[SortOrderType] = None


# This class is the input for the 'update_document' function.
class UpdateDocumentRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None


# This class is the input for the 'update_document_version' function.
class UpdateDocumentVersionRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    VersionStatus: Optional[Literal['ACTIVE']] = None


# This class is the input for the 'update_folder' function.
class UpdateFolderRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None


# This class is the output for the 'update_folder' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ResourceMetadata(BaseValidatorModel):
    Type: Optional[ResourceTypeType] = None
    Name: Optional[str] = None
    OriginalName: Optional[str] = None
    Id: Optional[str] = None
    VersionId: Optional[str] = None
    Owner: Optional[UserMetadata] = None
    ParentId: Optional[str] = None


# This class is the input for the 'add_resource_permissions' function.
class AddResourcePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    Principals: List[SharePrincipal]
    AuthenticationToken: Optional[str] = None
    NotificationOptions: Optional[NotificationOptions] = None


# This class is the output for the 'add_resource_permissions' function.
class AddResourcePermissionsResponse(BaseValidatorModel):
    ShareResults: List[ShareResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_folder' function.
class CreateFolderResponse(BaseValidatorModel):
    Metadata: FolderMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_root_folders' function.
class DescribeRootFoldersResponse(BaseValidatorModel):
    Folders: List[FolderMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_folder' function.
class GetFolderResponse(BaseValidatorModel):
    Metadata: FolderMetadata
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_notification_subscription' function.
class CreateNotificationSubscriptionResponse(BaseValidatorModel):
    Subscription: Subscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_notification_subscriptions' function.
class DescribeNotificationSubscriptionsResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    Username: str
    GivenName: str
    Surname: str
    Password: str
    OrganizationId: Optional[str] = None
    EmailAddress: Optional[str] = None
    TimeZoneId: Optional[str] = None
    StorageRule: Optional[StorageRuleType] = None
    AuthenticationToken: Optional[str] = None


# This class is the input for the 'update_user' function.
class UpdateUserRequest(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    Type: Optional[UserTypeType] = None
    StorageRule: Optional[StorageRuleType] = None
    TimeZoneId: Optional[str] = None
    Locale: Optional[LocaleTypeType] = None
    GrantPoweruserPrivileges: Optional[BooleanEnumTypeType] = None


class UserStorageMetadata(BaseValidatorModel):
    StorageUtilizedInBytes: Optional[int] = None
    StorageRule: Optional[StorageRuleType] = None


class DateRangeType(BaseValidatorModel):
    StartValue: Optional[Timestamp] = None
    EndValue: Optional[Timestamp] = None


# This class is the input for the 'describe_activities' function.
class DescribeActivitiesRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    OrganizationId: Optional[str] = None
    ActivityTypes: Optional[str] = None
    ResourceId: Optional[str] = None
    UserId: Optional[str] = None
    IncludeIndirectActivities: Optional[bool] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'initiate_document_version_upload' function.
class InitiateDocumentVersionUploadRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ContentCreatedTimestamp: Optional[Timestamp] = None
    ContentModifiedTimestamp: Optional[Timestamp] = None
    ContentType: Optional[str] = None
    DocumentSizeInBytes: Optional[int] = None
    ParentFolderId: Optional[str] = None


class DescribeActivitiesRequestPaginate(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    OrganizationId: Optional[str] = None
    ActivityTypes: Optional[str] = None
    ResourceId: Optional[str] = None
    UserId: Optional[str] = None
    IncludeIndirectActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCommentsRequestPaginate(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDocumentVersionsRequestPaginate(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFolderContentsRequestPaginate(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Sort: Optional[ResourceSortTypeType] = None
    Order: Optional[OrderTypeType] = None
    Type: Optional[FolderContentTypeType] = None
    Include: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGroupsRequestPaginate(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeNotificationSubscriptionsRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeResourcePermissionsRequestPaginate(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRootFoldersRequestPaginate(BaseValidatorModel):
    AuthenticationToken: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUsersRequestPaginate(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    UserIds: Optional[str] = None
    Query: Optional[str] = None
    Include: Optional[UserFilterTypeType] = None
    Order: Optional[OrderTypeType] = None
    Sort: Optional[UserSortTypeType] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_document_versions' function.
class DescribeDocumentVersionsResponse(BaseValidatorModel):
    DocumentVersions: List[DocumentVersionMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DocumentMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    CreatorId: Optional[str] = None
    ParentFolderId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    ModifiedTimestamp: Optional[datetime] = None
    LatestVersionMetadata: Optional[DocumentVersionMetadata] = None
    ResourceState: Optional[ResourceStateTypeType] = None
    Labels: Optional[List[str]] = None


# This class is the output for the 'get_document_version' function.
class GetDocumentVersionResponse(BaseValidatorModel):
    Metadata: DocumentVersionMetadata
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_groups' function.
class DescribeGroupsResponse(BaseValidatorModel):
    Groups: List[GroupMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


class Participants(BaseValidatorModel):
    Users: Optional[List[UserMetadata]] = None
    Groups: Optional[List[GroupMetadata]] = None


class Principal(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[PrincipalTypeType] = None
    Roles: Optional[List[PermissionInfo]] = None


class ResourcePath(BaseValidatorModel):
    Components: Optional[List[ResourcePathComponent]] = None


class User(BaseValidatorModel):
    Id: Optional[str] = None
    Username: Optional[str] = None
    EmailAddress: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    OrganizationId: Optional[str] = None
    RootFolderId: Optional[str] = None
    RecycleBinFolderId: Optional[str] = None
    Status: Optional[UserStatusTypeType] = None
    Type: Optional[UserTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    ModifiedTimestamp: Optional[datetime] = None
    TimeZoneId: Optional[str] = None
    Locale: Optional[LocaleTypeType] = None
    Storage: Optional[UserStorageMetadata] = None


class Filters(BaseValidatorModel):
    TextLocales: Optional[List[LanguageCodeTypeType]] = None
    ContentCategories: Optional[List[ContentCategoryTypeType]] = None
    ResourceTypes: Optional[List[SearchResourceTypeType]] = None
    Labels: Optional[List[str]] = None
    Principals: Optional[List[SearchPrincipalType]] = None
    AncestorIds: Optional[List[str]] = None
    SearchCollectionTypes: Optional[List[SearchCollectionTypeType]] = None
    SizeRange: Optional[LongRangeType] = None
    CreatedRange: Optional[DateRangeType] = None
    ModifiedRange: Optional[DateRangeType] = None


# This class is the output for the 'describe_folder_contents' function.
class DescribeFolderContentsResponse(BaseValidatorModel):
    Folders: List[FolderMetadata]
    Documents: List[DocumentMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_document' function.
class GetDocumentResponse(BaseValidatorModel):
    Metadata: DocumentMetadata
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resources' function.
class GetResourcesResponse(BaseValidatorModel):
    Folders: List[FolderMetadata]
    Documents: List[DocumentMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'initiate_document_version_upload' function.
class InitiateDocumentVersionUploadResponse(BaseValidatorModel):
    Metadata: DocumentMetadata
    UploadMetadata: UploadMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource_permissions' function.
class DescribeResourcePermissionsResponse(BaseValidatorModel):
    Principals: List[Principal]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_document_path' function.
class GetDocumentPathResponse(BaseValidatorModel):
    Path: ResourcePath
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_folder_path' function.
class GetFolderPathResponse(BaseValidatorModel):
    Path: ResourcePath
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'activate_user' function.
class ActivateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class CommentMetadata(BaseValidatorModel):
    CommentId: Optional[str] = None
    Contributor: Optional[User] = None
    CreatedTimestamp: Optional[datetime] = None
    CommentStatus: Optional[CommentStatusTypeType] = None
    RecipientId: Optional[str] = None
    ContributorId: Optional[str] = None


class Comment(BaseValidatorModel):
    CommentId: str
    ParentId: Optional[str] = None
    ThreadId: Optional[str] = None
    Text: Optional[str] = None
    Contributor: Optional[User] = None
    CreatedTimestamp: Optional[datetime] = None
    Status: Optional[CommentStatusTypeType] = None
    Visibility: Optional[CommentVisibilityTypeType] = None
    RecipientId: Optional[str] = None


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_users' function.
class DescribeUsersResponse(BaseValidatorModel):
    Users: List[User]
    TotalNumberOfUsers: int
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_current_user' function.
class GetCurrentUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user' function.
class UpdateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class SearchResourcesRequestPaginate(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[List[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[List[Literal['WEBURL']]] = None
    Filters: Optional[Filters] = None
    OrderBy: Optional[List[SearchSortResult]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_resources' function.
class SearchResourcesRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[List[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[List[Literal['WEBURL']]] = None
    Filters: Optional[Filters] = None
    OrderBy: Optional[List[SearchSortResult]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class Activity(BaseValidatorModel):
    Type: Optional[ActivityTypeType] = None
    TimeStamp: Optional[datetime] = None
    IsIndirectActivity: Optional[bool] = None
    OrganizationId: Optional[str] = None
    Initiator: Optional[UserMetadata] = None
    Participants: Optional[Participants] = None
    ResourceMetadata: Optional[ResourceMetadata] = None
    OriginalParent: Optional[ResourceMetadata] = None
    CommentMetadata: Optional[CommentMetadata] = None


class ResponseItem(BaseValidatorModel):
    ResourceType: Optional[ResponseItemTypeType] = None
    WebUrl: Optional[str] = None
    DocumentMetadata: Optional[DocumentMetadata] = None
    FolderMetadata: Optional[FolderMetadata] = None
    CommentMetadata: Optional[CommentMetadata] = None
    DocumentVersionMetadata: Optional[DocumentVersionMetadata] = None


# This class is the output for the 'create_comment' function.
class CreateCommentResponse(BaseValidatorModel):
    Comment: Comment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_comments' function.
class DescribeCommentsResponse(BaseValidatorModel):
    Comments: List[Comment]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_activities' function.
class DescribeActivitiesResponse(BaseValidatorModel):
    UserActivities: List[Activity]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_resources' function.
class SearchResourcesResponse(BaseValidatorModel):
    Items: List[ResponseItem]
    Marker: str
    ResponseMetadata: ResponseMetadata