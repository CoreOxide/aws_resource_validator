from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AbortDocumentVersionUploadRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None

class ActivateUserRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class UserMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Username: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    EmailAddress: Optional[str] = None

class NotificationOptionsTypeDef(BaseValidatorModel):
    SendEmail: Optional[bool] = None
    EmailMessage: Optional[str] = None

class SharePrincipalTypeDef(BaseValidatorModel):
    Id: str
    Type: PrincipalTypeType
    Role: RoleTypeType

class ShareResultTypeDef(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    InviteePrincipalId: Optional[str] = None
    Role: Optional[RoleTypeType] = None
    Status: Optional[ShareStatusTypeType] = None
    ShareId: Optional[str] = None
    StatusMessage: Optional[str] = None

class CreateCommentRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    Text: str
    AuthenticationToken: Optional[str] = None
    ParentId: Optional[str] = None
    ThreadId: Optional[str] = None
    Visibility: Optional[CommentVisibilityTypeType] = None
    NotifyCollaborators: Optional[bool] = None

class CreateCustomMetadataRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    CustomMetadata: Mapping[str, str]
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None

class CreateFolderRequestRequestTypeDef(BaseValidatorModel):
    ParentFolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None

class FolderMetadataTypeDef(BaseValidatorModel):
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

class CreateLabelsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Labels: Sequence[str]
    AuthenticationToken: Optional[str] = None

class CreateNotificationSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Endpoint: str
    Protocol: SubscriptionProtocolTypeType
    SubscriptionType: Literal["ALL"]

class SubscriptionTypeDef(BaseValidatorModel):
    SubscriptionId: Optional[str] = None
    EndPoint: Optional[str] = None
    Protocol: Optional[SubscriptionProtocolTypeType] = None

class StorageRuleTypeTypeDef(BaseValidatorModel):
    StorageAllocatedInBytes: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None

class DeactivateUserRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None

class DeleteCommentRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    CommentId: str
    AuthenticationToken: Optional[str] = None

class DeleteCustomMetadataRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None
    Keys: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None

class DeleteDocumentRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None

class DeleteDocumentVersionRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    DeletePriorVersions: bool
    AuthenticationToken: Optional[str] = None

class DeleteFolderContentsRequestRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None

class DeleteFolderRequestRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None

class DeleteLabelsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None

class DeleteNotificationSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionId: str
    OrganizationId: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCommentsRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDocumentVersionsRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None

class DocumentVersionMetadataTypeDef(BaseValidatorModel):
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

class DescribeFolderContentsRequestRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Sort: Optional[ResourceSortTypeType] = None
    Order: Optional[OrderTypeType] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None
    Type: Optional[FolderContentTypeType] = None
    Include: Optional[str] = None

class DescribeGroupsRequestRequestTypeDef(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class GroupMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class DescribeNotificationSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class DescribeResourcePermissionsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeRootFoldersRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeUsersRequestRequestTypeDef(BaseValidatorModel):
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

class LongRangeTypeTypeDef(BaseValidatorModel):
    StartValue: Optional[int] = None
    EndValue: Optional[int] = None

class SearchPrincipalTypeTypeDef(BaseValidatorModel):
    Id: str
    Roles: Optional[Sequence[PrincipalRoleTypeType]] = None

class GetCurrentUserRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: str

class GetDocumentPathRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None

class GetDocumentRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None

class GetDocumentVersionRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Fields: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None

class GetFolderPathRequestRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None

class GetFolderRequestRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None

class GetResourcesRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    UserId: Optional[str] = None
    CollectionType: Optional[Literal["SHARED_WITH_ME"]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class UploadMetadataTypeDef(BaseValidatorModel):
    UploadUrl: Optional[str] = None
    SignedHeaders: Optional[Dict[str, str]] = None

class PermissionInfoTypeDef(BaseValidatorModel):
    Role: Optional[RoleTypeType] = None
    Type: Optional[RolePermissionTypeType] = None

class RemoveAllResourcePermissionsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None

class RemoveResourcePermissionRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    PrincipalId: str
    AuthenticationToken: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class ResourcePathComponentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class RestoreDocumentVersionsRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None

class SearchSortResultTypeDef(BaseValidatorModel):
    Field: Optional[OrderByFieldTypeType] = None
    Order: Optional[SortOrderType] = None

class UpdateDocumentRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None

class UpdateDocumentVersionRequestRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    VersionStatus: Optional[Literal["ACTIVE"]] = None

class UpdateFolderRequestRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceMetadataTypeDef(BaseValidatorModel):
    Type: Optional[ResourceTypeType] = None
    Name: Optional[str] = None
    OriginalName: Optional[str] = None
    Id: Optional[str] = None
    VersionId: Optional[str] = None
    Owner: Optional[UserMetadataTypeDef] = None
    ParentId: Optional[str] = None

class AddResourcePermissionsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Principals: Sequence[SharePrincipalTypeDef]
    AuthenticationToken: Optional[str] = None
    NotificationOptions: Optional[NotificationOptionsTypeDef] = None

class AddResourcePermissionsResponseTypeDef(BaseValidatorModel):
    ShareResults: List[ShareResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFolderResponseTypeDef(BaseValidatorModel):
    Metadata: FolderMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRootFoldersResponseTypeDef(BaseValidatorModel):
    Folders: List[FolderMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderResponseTypeDef(BaseValidatorModel):
    Metadata: FolderMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotificationSubscriptionResponseTypeDef(BaseValidatorModel):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationSubscriptionsResponseTypeDef(BaseValidatorModel):
    Subscriptions: List[SubscriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    Username: str
    GivenName: str
    Surname: str
    Password: str
    OrganizationId: Optional[str] = None
    EmailAddress: Optional[str] = None
    TimeZoneId: Optional[str] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None
    AuthenticationToken: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    Type: Optional[UserTypeType] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None
    TimeZoneId: Optional[str] = None
    Locale: Optional[LocaleTypeType] = None
    GrantPoweruserPrivileges: Optional[BooleanEnumTypeType] = None

class UserStorageMetadataTypeDef(BaseValidatorModel):
    StorageUtilizedInBytes: Optional[int] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None

class DateRangeTypeTypeDef(BaseValidatorModel):
    StartValue: Optional[TimestampTypeDef] = None
    EndValue: Optional[TimestampTypeDef] = None

class DescribeActivitiesRequestRequestTypeDef(BaseValidatorModel):
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

class InitiateDocumentVersionUploadRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ContentCreatedTimestamp: Optional[TimestampTypeDef] = None
    ContentModifiedTimestamp: Optional[TimestampTypeDef] = None
    ContentType: Optional[str] = None
    DocumentSizeInBytes: Optional[int] = None
    ParentFolderId: Optional[str] = None

class DescribeActivitiesRequestDescribeActivitiesPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    OrganizationId: Optional[str] = None
    ActivityTypes: Optional[str] = None
    ResourceId: Optional[str] = None
    UserId: Optional[str] = None
    IncludeIndirectActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCommentsRequestDescribeCommentsPaginateTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFolderContentsRequestDescribeFolderContentsPaginateTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Sort: Optional[ResourceSortTypeType] = None
    Order: Optional[OrderTypeType] = None
    Type: Optional[FolderContentTypeType] = None
    Include: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGroupsRequestDescribeGroupsPaginateTypeDef(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRootFoldersRequestDescribeRootFoldersPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersRequestDescribeUsersPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    UserIds: Optional[str] = None
    Query: Optional[str] = None
    Include: Optional[UserFilterTypeType] = None
    Order: Optional[OrderTypeType] = None
    Sort: Optional[UserSortTypeType] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDocumentVersionsResponseTypeDef(BaseValidatorModel):
    DocumentVersions: List[DocumentVersionMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    CreatorId: Optional[str] = None
    ParentFolderId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    ModifiedTimestamp: Optional[datetime] = None
    LatestVersionMetadata: Optional[DocumentVersionMetadataTypeDef] = None
    ResourceState: Optional[ResourceStateTypeType] = None
    Labels: Optional[List[str]] = None

class GetDocumentVersionResponseTypeDef(BaseValidatorModel):
    Metadata: DocumentVersionMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipantsTypeDef(BaseValidatorModel):
    Users: Optional[List[UserMetadataTypeDef]] = None
    Groups: Optional[List[GroupMetadataTypeDef]] = None

class PrincipalTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[PrincipalTypeType] = None
    Roles: Optional[List[PermissionInfoTypeDef]] = None

class ResourcePathTypeDef(BaseValidatorModel):
    Components: Optional[List[ResourcePathComponentTypeDef]] = None

class UserTypeDef(BaseValidatorModel):
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

class FiltersTypeDef(BaseValidatorModel):
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

class DescribeFolderContentsResponseTypeDef(BaseValidatorModel):
    Folders: List[FolderMetadataTypeDef]
    Documents: List[DocumentMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentResponseTypeDef(BaseValidatorModel):
    Metadata: DocumentMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesResponseTypeDef(BaseValidatorModel):
    Folders: List[FolderMetadataTypeDef]
    Documents: List[DocumentMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateDocumentVersionUploadResponseTypeDef(BaseValidatorModel):
    Metadata: DocumentMetadataTypeDef
    UploadMetadata: UploadMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePermissionsResponseTypeDef(BaseValidatorModel):
    Principals: List[PrincipalTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentPathResponseTypeDef(BaseValidatorModel):
    Path: ResourcePathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderPathResponseTypeDef(BaseValidatorModel):
    Path: ResourcePathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CommentMetadataTypeDef(BaseValidatorModel):
    CommentId: Optional[str] = None
    Contributor: Optional[UserTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    CommentStatus: Optional[CommentStatusTypeType] = None
    RecipientId: Optional[str] = None
    ContributorId: Optional[str] = None

class CommentTypeDef(BaseValidatorModel):
    CommentId: str
    ParentId: Optional[str] = None
    ThreadId: Optional[str] = None
    Text: Optional[str] = None
    Contributor: Optional[UserTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    Status: Optional[CommentStatusTypeType] = None
    Visibility: Optional[CommentVisibilityTypeType] = None
    RecipientId: Optional[str] = None

class CreateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    TotalNumberOfUsers: int
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCurrentUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourcesRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[FiltersTypeDef] = None
    OrderBy: Optional[Sequence[SearchSortResultTypeDef]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class SearchResourcesRequestSearchResourcesPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[FiltersTypeDef] = None
    OrderBy: Optional[Sequence[SearchSortResultTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ActivityTypeDef(BaseValidatorModel):
    Type: Optional[ActivityTypeType] = None
    TimeStamp: Optional[datetime] = None
    IsIndirectActivity: Optional[bool] = None
    OrganizationId: Optional[str] = None
    Initiator: Optional[UserMetadataTypeDef] = None
    Participants: Optional[ParticipantsTypeDef] = None
    ResourceMetadata: Optional[ResourceMetadataTypeDef] = None
    OriginalParent: Optional[ResourceMetadataTypeDef] = None
    CommentMetadata: Optional[CommentMetadataTypeDef] = None

class ResponseItemTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResponseItemTypeType] = None
    WebUrl: Optional[str] = None
    DocumentMetadata: Optional[DocumentMetadataTypeDef] = None
    FolderMetadata: Optional[FolderMetadataTypeDef] = None
    CommentMetadata: Optional[CommentMetadataTypeDef] = None
    DocumentVersionMetadata: Optional[DocumentVersionMetadataTypeDef] = None

class CreateCommentResponseTypeDef(BaseValidatorModel):
    Comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCommentsResponseTypeDef(BaseValidatorModel):
    Comments: List[CommentTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActivitiesResponseTypeDef(BaseValidatorModel):
    UserActivities: List[ActivityTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourcesResponseTypeDef(BaseValidatorModel):
    Items: List[ResponseItemTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

