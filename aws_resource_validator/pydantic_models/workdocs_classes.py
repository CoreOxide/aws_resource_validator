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

class AbortDocumentVersionUploadRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None


class ActivateUserRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UserMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Username: Optional[str] = None
    GivenName: Optional[str] = None
    Surname: Optional[str] = None
    EmailAddress: Optional[str] = None


class NotificationOptionsTypeDef(BaseValidatorModel):
    SendEmail: Optional[bool] = None
    EmailMessage: Optional[str] = None


class ShareResultTypeDef(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    InviteePrincipalId: Optional[str] = None
    Role: Optional[RoleTypeType] = None
    Status: Optional[ShareStatusTypeType] = None
    ShareId: Optional[str] = None
    StatusMessage: Optional[str] = None


class CreateCustomMetadataRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    CustomMetadata: Mapping[str, str]
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None


class CreateFolderRequestTypeDef(BaseValidatorModel):
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


class CreateLabelsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Labels: Sequence[str]
    AuthenticationToken: Optional[str] = None


class StorageRuleTypeTypeDef(BaseValidatorModel):
    StorageAllocatedInBytes: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None


class DeactivateUserRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class DeleteCommentRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    CommentId: str
    AuthenticationToken: Optional[str] = None


class DeleteCustomMetadataRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    VersionId: Optional[str] = None
    Keys: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None


class DeleteDocumentRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None


class DeleteDocumentVersionRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    DeletePriorVersions: bool
    AuthenticationToken: Optional[str] = None


class DeleteFolderContentsRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None


class DeleteFolderRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None


class DeleteLabelsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    DeleteAll: Optional[bool] = None


class DeleteNotificationSubscriptionRequestTypeDef(BaseValidatorModel):
    SubscriptionId: str
    OrganizationId: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    UserId: str
    AuthenticationToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCommentsRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDocumentVersionsRequestTypeDef(BaseValidatorModel):
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


class DescribeGroupsRequestTypeDef(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class GroupMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


class DescribeNotificationSubscriptionsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class DescribeResourcePermissionsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class DescribeRootFoldersRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class DescribeUsersRequestTypeDef(BaseValidatorModel):
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


class GetCurrentUserRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: str


class GetDocumentPathRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None


class GetDocumentRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


class GetDocumentVersionRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    Fields: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


class GetFolderPathRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Limit: Optional[int] = None
    Fields: Optional[str] = None
    Marker: Optional[str] = None


class GetFolderRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    IncludeCustomMetadata: Optional[bool] = None


class GetResourcesRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    UserId: Optional[str] = None
    CollectionType: Optional[Literal["SHARED_WITH_ME"]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class UploadMetadataTypeDef(BaseValidatorModel):
    UploadUrl: Optional[str] = None
    SignedHeaders: Optional[Dict[str, str]] = None


class RemoveAllResourcePermissionsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None


class RemoveResourcePermissionRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    PrincipalId: str
    AuthenticationToken: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ResourcePathComponentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


class RestoreDocumentVersionsRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None


class SearchSortResultTypeDef(BaseValidatorModel):
    Field: Optional[OrderByFieldTypeType] = None
    Order: Optional[SortOrderType] = None


class UpdateDocumentRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None


class UpdateDocumentVersionRequestTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    VersionStatus: Optional[Literal["ACTIVE"]] = None


class UpdateFolderRequestTypeDef(BaseValidatorModel):
    FolderId: str
    AuthenticationToken: Optional[str] = None
    Name: Optional[str] = None
    ParentFolderId: Optional[str] = None
    ResourceState: Optional[ResourceStateTypeType] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class SharePrincipalTypeDef(BaseValidatorModel):
    pass


class AddResourcePermissionsRequestTypeDef(BaseValidatorModel):
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


class SubscriptionTypeDef(BaseValidatorModel):
    pass


class CreateNotificationSubscriptionResponseTypeDef(BaseValidatorModel):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeNotificationSubscriptionsResponseTypeDef(BaseValidatorModel):
    Subscriptions: List[SubscriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserRequestTypeDef(BaseValidatorModel):
    Username: str
    GivenName: str
    Surname: str
    Password: str
    OrganizationId: Optional[str] = None
    EmailAddress: Optional[str] = None
    TimeZoneId: Optional[str] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None
    AuthenticationToken: Optional[str] = None


class UserStorageMetadataTypeDef(BaseValidatorModel):
    StorageUtilizedInBytes: Optional[int] = None
    StorageRule: Optional[StorageRuleTypeTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DateRangeTypeTypeDef(BaseValidatorModel):
    StartValue: Optional[TimestampTypeDef] = None
    EndValue: Optional[TimestampTypeDef] = None


class DescribeActivitiesRequestTypeDef(BaseValidatorModel):
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


class InitiateDocumentVersionUploadRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ContentCreatedTimestamp: Optional[TimestampTypeDef] = None
    ContentModifiedTimestamp: Optional[TimestampTypeDef] = None
    ContentType: Optional[str] = None
    DocumentSizeInBytes: Optional[int] = None
    ParentFolderId: Optional[str] = None


class DescribeActivitiesRequestPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    OrganizationId: Optional[str] = None
    ActivityTypes: Optional[str] = None
    ResourceId: Optional[str] = None
    UserId: Optional[str] = None
    IncludeIndirectActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCommentsRequestPaginateTypeDef(BaseValidatorModel):
    DocumentId: str
    VersionId: str
    AuthenticationToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDocumentVersionsRequestPaginateTypeDef(BaseValidatorModel):
    DocumentId: str
    AuthenticationToken: Optional[str] = None
    Include: Optional[str] = None
    Fields: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGroupsRequestPaginateTypeDef(BaseValidatorModel):
    SearchQuery: str
    AuthenticationToken: Optional[str] = None
    OrganizationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeNotificationSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeResourcePermissionsRequestPaginateTypeDef(BaseValidatorModel):
    ResourceId: str
    AuthenticationToken: Optional[str] = None
    PrincipalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRootFoldersRequestPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeUsersRequestPaginateTypeDef(BaseValidatorModel):
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


class ResourcePathTypeDef(BaseValidatorModel):
    Components: Optional[List[ResourcePathComponentTypeDef]] = None


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


class PrincipalTypeDef(BaseValidatorModel):
    pass


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


class UserTypeDef(BaseValidatorModel):
    pass


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


class SearchResourcesRequestPaginateTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[FiltersTypeDef] = None
    OrderBy: Optional[Sequence[SearchSortResultTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchResourcesRequestTypeDef(BaseValidatorModel):
    AuthenticationToken: Optional[str] = None
    QueryText: Optional[str] = None
    QueryScopes: Optional[Sequence[SearchQueryScopeTypeType]] = None
    OrganizationId: Optional[str] = None
    AdditionalResponseFields: Optional[Sequence[Literal["WEBURL"]]] = None
    Filters: Optional[FiltersTypeDef] = None
    OrderBy: Optional[Sequence[SearchSortResultTypeDef]] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ResponseItemTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResponseItemTypeType] = None
    WebUrl: Optional[str] = None
    DocumentMetadata: Optional[DocumentMetadataTypeDef] = None
    FolderMetadata: Optional[FolderMetadataTypeDef] = None
    CommentMetadata: Optional[CommentMetadataTypeDef] = None
    DocumentVersionMetadata: Optional[DocumentVersionMetadataTypeDef] = None


class CommentTypeDef(BaseValidatorModel):
    pass


class CreateCommentResponseTypeDef(BaseValidatorModel):
    Comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCommentsResponseTypeDef(BaseValidatorModel):
    Comments: List[CommentTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ActivityTypeDef(BaseValidatorModel):
    pass


class DescribeActivitiesResponseTypeDef(BaseValidatorModel):
    UserActivities: List[ActivityTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchResourcesResponseTypeDef(BaseValidatorModel):
    Items: List[ResponseItemTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


