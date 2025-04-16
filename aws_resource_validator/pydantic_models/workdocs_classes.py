from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.workdocs_constants import *

class AbortDocumentVersionUploadRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None


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


class ShareResult(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    InviteePrincipalId: Optional[str] = None
    Role: Optional[RoleTypeType] = None
    Status: Optional[ShareStatusTypeType] = None
    ShareId: Optional[str] = None
    StatusMessage: Optional[str] = None


class CreateCustomMetadataRequest(BaseValidatorModel):
    ResourceId: str
    CustomMetadata: Mapping[str, str]
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None


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
    Labels: Sequence[str]
    AuthenticationToken: Optional[str] = None


class StorageRuleType(BaseValidatorModel):
    StorageAllocatedInBytes: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None


class DeactivateUserRequest(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class DeleteCommentRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    CommentId: str
    AuthenticationToken: Optional[str] = None


class DeleteCustomMetadataRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None
    Keys: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None


class DeleteDocumentRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None


class DeleteDocumentVersionRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    DeletePriorVersions: bool
    AuthenticationToken: Optional[str] = None


class DeleteFolderContentsRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None


class DeleteFolderRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None


class DeleteLabelsRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None


class DeleteNotificationSubscriptionRequest(BaseValidatorModel):
    SubscriptionId: str
    OrganizationId: str


class DeleteUserRequest(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCommentsRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


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


class DescribeGroupsRequest(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class GroupMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


class DescribeNotificationSubscriptionsRequest(BaseValidatorModel):
    OrganizationId: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class DescribeResourcePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class DescribeRootFoldersRequest(BaseValidatorModel):
    AuthenticationToken: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


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
    Roles: Optional[Sequence[PrincipalRoleTypeType]] = None


class GetCurrentUserRequest(BaseValidatorModel):
    AuthenticationToken: str


class GetDocumentPathRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None


class GetDocumentRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


class GetDocumentVersionRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Fields: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


class GetFolderPathRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None


class GetFolderRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


class GetResourcesRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    UserId: Optional[str] = None
    CollectionType: Optional[Literal["SHARED_WITH_ME"]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class UploadMetadata(BaseValidatorModel):
    UploadUrl: Optional[str] = None
    SignedHeaders: Optional[Dict[str, str]] = None


class RemoveAllResourcePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None


class RemoveResourcePermissionRequest(BaseValidatorModel):
    ResourceId: str
    PrincipalId: str
    AuthenticationToken: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ResourcePathComponent(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


class RestoreDocumentVersionsRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None


class SearchSortResult(BaseValidatorModel):
    Field: Optional[OrderByFieldTypeType] = None
    Order: Optional[SortOrderType] = None


class UpdateDocumentRequest(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None


class UpdateDocumentVersionRequest(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    VersionStatus: Optional[Literal["ACTIVE"]] = None


class UpdateFolderRequest(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class SharePrincipal(BaseValidatorModel):
    pass


class AddResourcePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    Principals: Sequence[SharePrincipal]
    AuthenticationToken: Optional[str] = None
    NotificationOptions: Optional[NotificationOptions] = None


class AddResourcePermissionsResponse(BaseValidatorModel):
    ShareResults: List[ShareResult]
    ResponseMetadata: ResponseMetadata


class CreateFolderResponse(BaseValidatorModel):
    Metadata: FolderMetadata
    ResponseMetadata: ResponseMetadata


class DescribeRootFoldersResponse(BaseValidatorModel):
    Folders: List[FolderMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetFolderResponse(BaseValidatorModel):
    Metadata: FolderMetadata
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Subscription(BaseValidatorModel):
    pass


class CreateNotificationSubscriptionResponse(BaseValidatorModel):
    Subscription: Subscription
    ResponseMetadata: ResponseMetadata


class DescribeNotificationSubscriptionsResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    Marker: str
    ResponseMetadata: ResponseMetadata


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


class UserStorageMetadata(BaseValidatorModel):
    StorageUtilizedInBytes: Optional[int] = None
    StorageRule: Optional[StorageRuleType] = None


class Timestamp(BaseValidatorModel):
    pass


class DateRangeType(BaseValidatorModel):
    StartValue: Optional[Timestamp] = None
    EndValue: Optional[Timestamp] = None


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


class GetDocumentVersionResponse(BaseValidatorModel):
    Metadata: DocumentVersionMetadata
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeGroupsResponse(BaseValidatorModel):
    Groups: List[GroupMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


class Participants(BaseValidatorModel):
    Users: Optional[List[UserMetadata]] = None
    Groups: Optional[List[GroupMetadata]] = None


class ResourcePath(BaseValidatorModel):
    Components: Optional[List[ResourcePathComponent]] = None


class Filters(BaseValidatorModel):
    TextLocales: Optional[Sequence[LanguageCodeTypeType]] = None
    ContentCategories: Optional[Sequence[ContentCategoryTypeType]] = None
    ResourceTypes: Optional[Sequence[SearchResourceTypeType]] = None
    Labels: Optional[Sequence[str]] = None
    Principals: Optional[Sequence[SearchPrincipalType]] = None
    AncestorIds: Optional[Sequence[str]] = None
    SearchCollectionTypes: Optional[Sequence[SearchCollectionTypeType]] = None
    SizeRange: Optional[LongRangeType] = None
    CreatedRange: Optional[DateRangeType] = None
    ModifiedRange: Optional[DateRangeType] = None


class DescribeFolderContentsResponse(BaseValidatorModel):
    Folders: List[FolderMetadata]
    Documents: List[DocumentMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetDocumentResponse(BaseValidatorModel):
    Metadata: DocumentMetadata
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetResourcesResponse(BaseValidatorModel):
    Folders: List[FolderMetadata]
    Documents: List[DocumentMetadata]
    Marker: str
    ResponseMetadata: ResponseMetadata


class InitiateDocumentVersionUploadResponse(BaseValidatorModel):
    Metadata: DocumentMetadata
    UploadMetadata: UploadMetadata
    ResponseMetadata: ResponseMetadata


class Principal(BaseValidatorModel):
    pass


class DescribeResourcePermissionsResponse(BaseValidatorModel):
    Principals: List[Principal]
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetDocumentPathResponse(BaseValidatorModel):
    Path: ResourcePath
    ResponseMetadata: ResponseMetadata


class GetFolderPathResponse(BaseValidatorModel):
    Path: ResourcePath
    ResponseMetadata: ResponseMetadata


class User(BaseValidatorModel):
    pass


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


class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class DescribeUsersResponse(BaseValidatorModel):
    Users: List[User]
    TotalNumberOfUsers: int
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetCurrentUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class UpdateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class SearchResourcesRequestPaginate(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[Filters] = None
    OrderBy: Optional[Sequence[SearchSortResult]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchResourcesRequest(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[Filters] = None
    OrderBy: Optional[Sequence[SearchSortResult]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ResponseItem(BaseValidatorModel):
    ResourceType: Optional[ResponseItemTypeType] = None
    WebUrl: Optional[str] = None
    DocumentMetadata: Optional[DocumentMetadata] = None
    FolderMetadata: Optional[FolderMetadata] = None
    CommentMetadata: Optional[CommentMetadata] = None
    DocumentVersionMetadata: Optional[DocumentVersionMetadata] = None


class Comment(BaseValidatorModel):
    pass


class CreateCommentResponse(BaseValidatorModel):
    Comment: Comment
    ResponseMetadata: ResponseMetadata


class DescribeCommentsResponse(BaseValidatorModel):
    Comments: List[Comment]
    Marker: str
    ResponseMetadata: ResponseMetadata


class Activity(BaseValidatorModel):
    pass


class DescribeActivitiesResponse(BaseValidatorModel):
    UserActivities: List[Activity]
    Marker: str
    ResponseMetadata: ResponseMetadata


class SearchResourcesResponse(BaseValidatorModel):
    Items: List[ResponseItem]
    Marker: str
    ResponseMetadata: ResponseMetadata


