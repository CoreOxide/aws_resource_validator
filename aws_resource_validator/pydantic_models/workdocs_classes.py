from datetime import datetime
from pydantic import BaseModel
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

class AbortDocumentVersionUploadRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None

class ActivateUserRequestRequestTypeDef(BaseModel):
    UserId: str
    AuthenticationToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class UserMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    Username: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    EmailAddress: Optional[str] = None

class NotificationOptionsTypeDef(BaseModel):
    SendEmail: Optional[bool] = None
    EmailMessage: Optional[str] = None

class SharePrincipalTypeDef(BaseModel):
    Id: str
    Type: PrincipalTypeType
    Role: RoleTypeType

class ShareResultTypeDef(BaseModel):
    PrincipalId: Optional[str] = None
    InviteePrincipalId: Optional[str] = None
    Role: Optional[RoleTypeType] = None
    Status: Optional[ShareStatusTypeType] = None
    ShareId: Optional[str] = None
    StatusMessage: Optional[str] = None

class CreateCommentRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    Text: str
    AuthenticationToken: Optional[str] = None
    ParentId: Optional[str] = None
    ThreadId: Optional[str] = None
    Visibility: Optional[CommentVisibilityTypeType] = None
    NotifyCollaborators: Optional[bool] = None

class CreateCustomMetadataRequestRequestTypeDef(BaseModel):
    ResourceId: str
    CustomMetadata: Mapping[str, str]
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None

class CreateFolderRequestRequestTypeDef(BaseModel):
    ParentFolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None

class FolderMetadataTypeDef(BaseModel):
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

class CreateLabelsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Labels: Sequence[str]
    AuthenticationToken: Optional[str] = None

class CreateNotificationSubscriptionRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Endpoint: str
    Protocol: SubscriptionProtocolTypeType
    SubscriptionType: Literal["ALL"]

class SubscriptionTypeDef(BaseModel):
    SubscriptionId: Optional[str] = None
    EndPoint: Optional[str] = None
    Protocol: Optional[SubscriptionProtocolTypeType] = None

class StorageRuleTypeTypeDef(BaseModel):
    StorageAllocatedInBytes: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None

class DeactivateUserRequestRequestTypeDef(BaseModel):
    UserId: str
    AuthenticationToken: Optional[str] = None

class DeleteCommentRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    CommentId: str
    AuthenticationToken: Optional[str] = None

class DeleteCustomMetadataRequestRequestTypeDef(BaseModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None
    Keys: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None

class DeleteDocumentRequestRequestTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None

class DeleteDocumentVersionRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    DeletePriorVersions: bool
    AuthenticationToken: Optional[str] = None

class DeleteFolderContentsRequestRequestTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None

class DeleteFolderRequestRequestTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None

class DeleteLabelsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None

class DeleteNotificationSubscriptionRequestRequestTypeDef(BaseModel):
    SubscriptionId: str
    OrganizationId: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    UserId: str
    AuthenticationToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCommentsRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDocumentVersionsRequestRequestTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None

class DocumentVersionMetadataTypeDef(BaseModel):
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

class DescribeFolderContentsRequestRequestTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Sort: Optional[ResourceSortTypeType] = None
    Order: Optional[OrderTypeType] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None
    Type: Optional[FolderContentTypeType] = None
    Include: Optional[str] = None

class DescribeGroupsRequestRequestTypeDef(BaseModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class GroupMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class DescribeNotificationSubscriptionsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class DescribeResourcePermissionsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeRootFoldersRequestRequestTypeDef(BaseModel):
    AuthenticationToken: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeUsersRequestRequestTypeDef(BaseModel):
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

class LongRangeTypeTypeDef(BaseModel):
    StartValue: Optional[int] = None
    EndValue: Optional[int] = None

class SearchPrincipalTypeTypeDef(BaseModel):
    Id: str
    Roles: Optional[Sequence[PrincipalRoleTypeType]] = None

class GetCurrentUserRequestRequestTypeDef(BaseModel):
    AuthenticationToken: str

class GetDocumentPathRequestRequestTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None

class GetDocumentRequestRequestTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None

class GetDocumentVersionRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Fields: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None

class GetFolderPathRequestRequestTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None

class GetFolderRequestRequestTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None

class GetResourcesRequestRequestTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    UserId: Optional[str] = None
    CollectionType: Optional[Literal["SHARED_WITH_ME"]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class UploadMetadataTypeDef(BaseModel):
    UploadUrl: Optional[str] = None
    SignedHeaders: Optional[Dict[str, str]] = None

class PermissionInfoTypeDef(BaseModel):
    Role: Optional[RoleTypeType] = None
    Type: Optional[RolePermissionTypeType] = None

class RemoveAllResourcePermissionsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None

class RemoveResourcePermissionRequestRequestTypeDef(BaseModel):
    ResourceId: str
    PrincipalId: str
    AuthenticationToken: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class ResourcePathComponentTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class RestoreDocumentVersionsRequestRequestTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None

class SearchSortResultTypeDef(BaseModel):
    Field: Optional[OrderByFieldTypeType] = None
    Order: Optional[SortOrderType] = None

class UpdateDocumentRequestRequestTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None

class UpdateDocumentVersionRequestRequestTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    VersionStatus: Optional[Literal["ACTIVE"]] = None

class UpdateFolderRequestRequestTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceMetadataTypeDef(BaseModel):
    Type: Optional[ResourceTypeType] = None
    Name: Optional[str] = None
    OriginalName: Optional[str] = None
    Id: Optional[str] = None
    VersionId: Optional[str] = None
    Owner: Optional[UserMetadataTypeDef] = None
    ParentId: Optional[str] = None

class AddResourcePermissionsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Principals: Sequence[SharePrincipalTypeDef]
    AuthenticationToken: Optional[str] = None
    NotificationOptions: Optional[NotificationOptionsTypeDef] = None

class AddResourcePermissionsResponseTypeDef(BaseModel):
    ShareResults: List[ShareResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFolderResponseTypeDef(BaseModel):
    Metadata: FolderMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRootFoldersResponseTypeDef(BaseModel):
    Folders: List[FolderMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderResponseTypeDef(BaseModel):
    Metadata: FolderMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotificationSubscriptionResponseTypeDef(BaseModel):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationSubscriptionsResponseTypeDef(BaseModel):
    Subscriptions: List[SubscriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestRequestTypeDef(BaseModel):
    Username: str
    GivenName: str
    Surname: str
    Password: str
    OrganizationId: Optional[str] = None
    EmailAddress: Optional[str] = None
    TimeZoneId: Optional[str] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None
    AuthenticationToken: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    UserId: str
    AuthenticationToken: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    Type: Optional[UserTypeType] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None
    TimeZoneId: Optional[str] = None
    Locale: Optional[LocaleTypeType] = None
    GrantPoweruserPrivileges: Optional[BooleanEnumTypeType] = None

class UserStorageMetadataTypeDef(BaseModel):
    StorageUtilizedInBytes: Optional[int] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None

class DateRangeTypeTypeDef(BaseModel):
    StartValue: Optional[TimestampTypeDef] = None
    EndValue: Optional[TimestampTypeDef] = None

class DescribeActivitiesRequestRequestTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    OrganizationId: Optional[str] = None
    ActivityTypes: Optional[str] = None
    ResourceId: Optional[str] = None
    UserId: Optional[str] = None
    IncludeIndirectActivities: Optional[bool] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class InitiateDocumentVersionUploadRequestRequestTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ContentCreatedTimestamp: Optional[TimestampTypeDef] = None
    ContentModifiedTimestamp: Optional[TimestampTypeDef] = None
    ContentType: Optional[str] = None
    DocumentSizeInBytes: Optional[int] = None
    ParentFolderId: Optional[str] = None

class DescribeActivitiesRequestDescribeActivitiesPaginateTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    OrganizationId: Optional[str] = None
    ActivityTypes: Optional[str] = None
    ResourceId: Optional[str] = None
    UserId: Optional[str] = None
    IncludeIndirectActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCommentsRequestDescribeCommentsPaginateTypeDef(BaseModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateTypeDef(BaseModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFolderContentsRequestDescribeFolderContentsPaginateTypeDef(BaseModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Sort: Optional[ResourceSortTypeType] = None
    Order: Optional[OrderTypeType] = None
    Type: Optional[FolderContentTypeType] = None
    Include: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGroupsRequestDescribeGroupsPaginateTypeDef(BaseModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateTypeDef(BaseModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRootFoldersRequestDescribeRootFoldersPaginateTypeDef(BaseModel):
    AuthenticationToken: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersRequestDescribeUsersPaginateTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    UserIds: Optional[str] = None
    Query: Optional[str] = None
    Include: Optional[UserFilterTypeType] = None
    Order: Optional[OrderTypeType] = None
    Sort: Optional[UserSortTypeType] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDocumentVersionsResponseTypeDef(BaseModel):
    DocumentVersions: List[DocumentVersionMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    CreatorId: Optional[str] = None
    ParentFolderId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    ModifiedTimestamp: Optional[datetime] = None
    LatestVersionMetadata: Optional[DocumentVersionMetadataTypeDef] = None
    ResourceState: Optional[ResourceStateTypeType] = None
    Labels: Optional[List[str]] = None

class GetDocumentVersionResponseTypeDef(BaseModel):
    Metadata: DocumentVersionMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipantsTypeDef(BaseModel):
    Users: Optional[List[UserMetadataTypeDef]] = None
    Groups: Optional[List[GroupMetadataTypeDef]] = None

class PrincipalTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[PrincipalTypeType] = None
    Roles: Optional[List[PermissionInfoTypeDef]] = None

class ResourcePathTypeDef(BaseModel):
    Components: Optional[List[ResourcePathComponentTypeDef]] = None

class UserTypeDef(BaseModel):
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
    Storage: Optional[UserStorageMetadataTypeDef] = None

class FiltersTypeDef(BaseModel):
    TextLocales: Optional[Sequence[LanguageCodeTypeType]] = None
    ContentCategories: Optional[Sequence[ContentCategoryTypeType]] = None
    ResourceTypes: Optional[Sequence[SearchResourceTypeType]] = None
    Labels: Optional[Sequence[str]] = None
    Principals: Optional[Sequence[SearchPrincipalTypeTypeDef]] = None
    AncestorIds: Optional[Sequence[str]] = None
    SearchCollectionTypes: Optional[Sequence[SearchCollectionTypeType]] = None
    SizeRange: Optional[LongRangeTypeTypeDef] = None
    CreatedRange: Optional[DateRangeTypeTypeDef] = None
    ModifiedRange: Optional[DateRangeTypeTypeDef] = None

class DescribeFolderContentsResponseTypeDef(BaseModel):
    Folders: List[FolderMetadataTypeDef]
    Documents: List[DocumentMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentResponseTypeDef(BaseModel):
    Metadata: DocumentMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesResponseTypeDef(BaseModel):
    Folders: List[FolderMetadataTypeDef]
    Documents: List[DocumentMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateDocumentVersionUploadResponseTypeDef(BaseModel):
    Metadata: DocumentMetadataTypeDef
    UploadMetadata: UploadMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePermissionsResponseTypeDef(BaseModel):
    Principals: List[PrincipalTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentPathResponseTypeDef(BaseModel):
    Path: ResourcePathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderPathResponseTypeDef(BaseModel):
    Path: ResourcePathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CommentMetadataTypeDef(BaseModel):
    CommentId: Optional[str] = None
    Contributor: Optional[UserTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    CommentStatus: Optional[CommentStatusTypeType] = None
    RecipientId: Optional[str] = None
    ContributorId: Optional[str] = None

class CommentTypeDef(BaseModel):
    CommentId: str
    ParentId: Optional[str] = None
    ThreadId: Optional[str] = None
    Text: Optional[str] = None
    Contributor: Optional[UserTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    Status: Optional[CommentStatusTypeType] = None
    Visibility: Optional[CommentVisibilityTypeType] = None
    RecipientId: Optional[str] = None

class CreateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    TotalNumberOfUsers: int
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCurrentUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourcesRequestRequestTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[FiltersTypeDef] = None
    OrderBy: Optional[Sequence[SearchSortResultTypeDef]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class SearchResourcesRequestSearchResourcesPaginateTypeDef(BaseModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[FiltersTypeDef] = None
    OrderBy: Optional[Sequence[SearchSortResultTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ActivityTypeDef(BaseModel):
    Type: Optional[ActivityTypeType] = None
    TimeStamp: Optional[datetime] = None
    IsIndirectActivity: Optional[bool] = None
    OrganizationId: Optional[str] = None
    Initiator: Optional[UserMetadataTypeDef] = None
    Participants: Optional[ParticipantsTypeDef] = None
    ResourceMetadata: Optional[ResourceMetadataTypeDef] = None
    OriginalParent: Optional[ResourceMetadataTypeDef] = None
    CommentMetadata: Optional[CommentMetadataTypeDef] = None

class ResponseItemTypeDef(BaseModel):
    ResourceType: Optional[ResponseItemTypeType] = None
    WebUrl: Optional[str] = None
    DocumentMetadata: Optional[DocumentMetadataTypeDef] = None
    FolderMetadata: Optional[FolderMetadataTypeDef] = None
    CommentMetadata: Optional[CommentMetadataTypeDef] = None
    DocumentVersionMetadata: Optional[DocumentVersionMetadataTypeDef] = None

class CreateCommentResponseTypeDef(BaseModel):
    Comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCommentsResponseTypeDef(BaseModel):
    Comments: List[CommentTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActivitiesResponseTypeDef(BaseModel):
    UserActivities: List[ActivityTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourcesResponseTypeDef(BaseModel):
    Items: List[ResponseItemTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

