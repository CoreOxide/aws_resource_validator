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
from aws_resource_validator.pydantic_models.kendra_constants import *

class AccessControlConfigurationSummaryTypeDef(BaseModel):
    Id: str

class AccessControlListConfigurationTypeDef(BaseModel):
    KeyPath: Optional[str] = None

class AclConfigurationTypeDef(BaseModel):
    AllowedGroupsColumnName: str

class DataSourceToIndexFieldMappingTypeDef(BaseModel):
    DataSourceFieldName: str
    IndexFieldName: str
    DateFieldFormat: Optional[str] = None

class DataSourceVpcConfigurationTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class S3PathTypeDef(BaseModel):
    Bucket: str
    Key: str

class EntityConfigurationTypeDef(BaseModel):
    EntityId: str
    EntityType: EntityTypeType

class FailedEntityTypeDef(BaseModel):
    EntityId: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class EntityPersonaConfigurationTypeDef(BaseModel):
    EntityId: str
    Persona: PersonaType

class SuggestableConfigTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    Suggestable: Optional[bool] = None

class BasicAuthenticationConfigurationTypeDef(BaseModel):
    Host: str
    Port: int
    Credentials: str

class DataSourceSyncJobMetricTargetTypeDef(BaseModel):
    DataSourceId: str
    DataSourceSyncJobId: Optional[str] = None

class BatchDeleteDocumentResponseFailedDocumentTypeDef(BaseModel):
    Id: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchDeleteFeaturedResultsSetErrorTypeDef(BaseModel):
    Id: str
    ErrorCode: ErrorCodeType
    ErrorMessage: str

class BatchDeleteFeaturedResultsSetRequestRequestTypeDef(BaseModel):
    IndexId: str
    FeaturedResultsSetIds: Sequence[str]

class BatchGetDocumentStatusResponseErrorTypeDef(BaseModel):
    DocumentId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class StatusTypeDef(BaseModel):
    DocumentId: Optional[str] = None
    DocumentStatus: Optional[DocumentStatusType] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None

class BatchPutDocumentResponseFailedDocumentTypeDef(BaseModel):
    Id: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class CapacityUnitsConfigurationTypeDef(BaseModel):
    StorageCapacityUnits: int
    QueryCapacityUnits: int

class ClearQuerySuggestionsRequestRequestTypeDef(BaseModel):
    IndexId: str

class ExpandConfigurationTypeDef(BaseModel):
    MaxResultItemsToExpand: Optional[int] = None
    MaxExpandedResultsPerItem: Optional[int] = None

class SortingConfigurationTypeDef(BaseModel):
    DocumentAttributeKey: str
    SortOrder: SortOrderType

class ConfluenceAttachmentToIndexFieldMappingTypeDef(BaseModel):
    DataSourceFieldName: Optional[ConfluenceAttachmentFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ConfluenceBlogToIndexFieldMappingTypeDef(BaseModel):
    DataSourceFieldName: Optional[ConfluenceBlogFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ProxyConfigurationTypeDef(BaseModel):
    Host: str
    Port: int
    Credentials: Optional[str] = None

class ConfluencePageToIndexFieldMappingTypeDef(BaseModel):
    DataSourceFieldName: Optional[ConfluencePageFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ConfluenceSpaceToIndexFieldMappingTypeDef(BaseModel):
    DataSourceFieldName: Optional[ConfluenceSpaceFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ConnectionConfigurationTypeDef(BaseModel):
    DatabaseHost: str
    DatabasePort: int
    DatabaseName: str
    TableName: str
    SecretArn: str

class ContentSourceConfigurationTypeDef(BaseModel):
    DataSourceIds: Optional[Sequence[str]] = None
    FaqIds: Optional[Sequence[str]] = None
    DirectPutContent: Optional[bool] = None

class CorrectionTypeDef(BaseModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Term: Optional[str] = None
    CorrectedTerm: Optional[str] = None

class PrincipalTypeDef(BaseModel):
    Name: str
    Type: PrincipalTypeType
    Access: ReadAccessTypeType
    DataSourceId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class FeaturedDocumentTypeDef(BaseModel):
    Id: Optional[str] = None

class ServerSideEncryptionConfigurationTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None

class UserGroupResolutionConfigurationTypeDef(BaseModel):
    UserGroupResolutionMode: UserGroupResolutionModeType

class TemplateConfigurationTypeDef(BaseModel):
    Template: Optional[Mapping[str, Any]] = None

class DataSourceGroupTypeDef(BaseModel):
    GroupId: str
    DataSourceId: str

class DataSourceSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[DataSourceStatusType] = None
    LanguageCode: Optional[str] = None

class DataSourceSyncJobMetricsTypeDef(BaseModel):
    DocumentsAdded: Optional[str] = None
    DocumentsModified: Optional[str] = None
    DocumentsDeleted: Optional[str] = None
    DocumentsFailed: Optional[str] = None
    DocumentsScanned: Optional[str] = None

class SqlConfigurationTypeDef(BaseModel):
    QueryIdentifiersEnclosingOption: Optional[QueryIdentifiersEnclosingOptionType] = None

class DeleteAccessControlConfigurationRequestRequestTypeDef(BaseModel):
    IndexId: str
    Id: str

class DeleteDataSourceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DeleteExperienceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DeleteFaqRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DeleteIndexRequestRequestTypeDef(BaseModel):
    Id: str

class DeletePrincipalMappingRequestRequestTypeDef(BaseModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None

class DeleteQuerySuggestionsBlockListRequestRequestTypeDef(BaseModel):
    IndexId: str
    Id: str

class DeleteThesaurusRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DescribeAccessControlConfigurationRequestRequestTypeDef(BaseModel):
    IndexId: str
    Id: str

class DescribeDataSourceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DescribeExperienceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class ExperienceEndpointTypeDef(BaseModel):
    EndpointType: Optional[Literal["HOME"]] = None
    Endpoint: Optional[str] = None

class DescribeFaqRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DescribeFeaturedResultsSetRequestRequestTypeDef(BaseModel):
    IndexId: str
    FeaturedResultsSetId: str

class FeaturedDocumentMissingTypeDef(BaseModel):
    Id: Optional[str] = None

class FeaturedDocumentWithMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    URI: Optional[str] = None

class DescribeIndexRequestRequestTypeDef(BaseModel):
    Id: str

class DescribePrincipalMappingRequestRequestTypeDef(BaseModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None

class GroupOrderingIdSummaryTypeDef(BaseModel):
    Status: Optional[PrincipalMappingStatusType] = None
    LastUpdatedAt: Optional[datetime] = None
    ReceivedAt: Optional[datetime] = None
    OrderingId: Optional[int] = None
    FailureReason: Optional[str] = None

class DescribeQuerySuggestionsBlockListRequestRequestTypeDef(BaseModel):
    IndexId: str
    Id: str

class DescribeQuerySuggestionsConfigRequestRequestTypeDef(BaseModel):
    IndexId: str

class DescribeThesaurusRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class DisassociatePersonasFromEntitiesRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    EntityIds: Sequence[str]

class RelevanceTypeDef(BaseModel):
    Freshness: Optional[bool] = None
    Importance: Optional[int] = None
    Duration: Optional[str] = None
    RankOrder: Optional[OrderType] = None
    ValueImportanceMap: Optional[Dict[str, int]] = None

class SearchTypeDef(BaseModel):
    Facetable: Optional[bool] = None
    Searchable: Optional[bool] = None
    Displayable: Optional[bool] = None
    Sortable: Optional[bool] = None

class DocumentsMetadataConfigurationTypeDef(BaseModel):
    S3Prefix: Optional[str] = None

class EntityDisplayDataTypeDef(BaseModel):
    UserName: Optional[str] = None
    GroupName: Optional[str] = None
    IdentifiedUserName: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class UserIdentityConfigurationTypeDef(BaseModel):
    IdentityAttributeName: Optional[str] = None

class FacetResultTypeDef(BaseModel):
    DocumentAttributeKey: Optional[str] = None
    DocumentAttributeValueType: Optional[DocumentAttributeValueTypeType] = None
    DocumentAttributeValueCountPairs: Optional[       List["DocumentAttributeValueCountPairTypeDef"]     ] = None

class FacetTypeDef(BaseModel):
    DocumentAttributeKey: Optional[str] = None
    Facets: Optional[Sequence[Dict[str, Any]]] = None
    MaxResults: Optional[int] = None

class FaqStatisticsTypeDef(BaseModel):
    IndexedQuestionAnswersCount: int

class FaqSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[FaqStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    FileFormat: Optional[FaqFileFormatType] = None
    LanguageCode: Optional[str] = None

class FeaturedResultsSetSummaryTypeDef(BaseModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None

class GetSnapshotsRequestRequestTypeDef(BaseModel):
    IndexId: str
    Interval: IntervalType
    MetricType: MetricTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TimeRangeTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class GitHubDocumentCrawlPropertiesTypeDef(BaseModel):
    CrawlRepositoryDocuments: Optional[bool] = None
    CrawlIssue: Optional[bool] = None
    CrawlIssueComment: Optional[bool] = None
    CrawlIssueCommentAttachment: Optional[bool] = None
    CrawlPullRequest: Optional[bool] = None
    CrawlPullRequestComment: Optional[bool] = None
    CrawlPullRequestCommentAttachment: Optional[bool] = None

class SaaSConfigurationTypeDef(BaseModel):
    OrganizationName: str
    HostUrl: str

class MemberGroupTypeDef(BaseModel):
    GroupId: str
    DataSourceId: Optional[str] = None

class MemberUserTypeDef(BaseModel):
    UserId: str

class GroupSummaryTypeDef(BaseModel):
    GroupId: Optional[str] = None
    OrderingId: Optional[int] = None

class HighlightTypeDef(BaseModel):
    BeginOffset: int
    EndOffset: int
    TopAnswer: Optional[bool] = None
    Type: Optional[HighlightTypeType] = None

class IndexConfigurationSummaryTypeDef(BaseModel):
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: IndexStatusType
    Name: Optional[str] = None
    Id: Optional[str] = None
    Edition: Optional[IndexEditionType] = None

class TextDocumentStatisticsTypeDef(BaseModel):
    IndexedTextDocumentsCount: int
    IndexedTextBytes: int

class JsonTokenTypeConfigurationTypeDef(BaseModel):
    UserNameAttributeField: str
    GroupAttributeField: str

class JwtTokenTypeConfigurationTypeDef(BaseModel):
    KeyLocation: KeyLocationType
    URL: Optional[str] = None
    SecretManagerArn: Optional[str] = None
    UserNameAttributeField: Optional[str] = None
    GroupAttributeField: Optional[str] = None
    Issuer: Optional[str] = None
    ClaimRegex: Optional[str] = None

class ListAccessControlConfigurationsRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntityPersonasRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PersonasSummaryTypeDef(BaseModel):
    EntityId: Optional[str] = None
    Persona: Optional[PersonaType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ListExperienceEntitiesRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None

class ListExperiencesRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFaqsRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFeaturedResultsSetsRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupsOlderThanOrderingIdRequestRequestTypeDef(BaseModel):
    IndexId: str
    OrderingId: int
    DataSourceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIndicesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListQuerySuggestionsBlockListsRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QuerySuggestionsBlockListSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[QuerySuggestionsBlockListStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ItemCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListThesauriRequestRequestTypeDef(BaseModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ThesaurusSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ThesaurusStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class SpellCorrectionConfigurationTypeDef(BaseModel):
    IncludeQuerySpellCheckSuggestions: bool

class ScoreAttributesTypeDef(BaseModel):
    ScoreConfidence: Optional[ScoreConfidenceType] = None

class WarningTypeDef(BaseModel):
    Message: Optional[str] = None
    Code: Optional[Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]] = None

class RelevanceFeedbackTypeDef(BaseModel):
    ResultId: str
    RelevanceValue: RelevanceTypeType

class SeedUrlConfigurationTypeDef(BaseModel):
    SeedUrls: Sequence[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None

class SiteMapsConfigurationTypeDef(BaseModel):
    SiteMaps: Sequence[str]

class StartDataSourceSyncJobRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class StopDataSourceSyncJobRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str

class SuggestionHighlightTypeDef(BaseModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class TableCellTypeDef(BaseModel):
    Value: Optional[str] = None
    TopAnswer: Optional[bool] = None
    Highlighted: Optional[bool] = None
    Header: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ColumnConfigurationTypeDef(BaseModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: Sequence[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class GoogleDriveConfigurationTypeDef(BaseModel):
    SecretArn: str
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    ExcludeMimeTypes: Optional[Sequence[str]] = None
    ExcludeUserAccounts: Optional[Sequence[str]] = None
    ExcludeSharedDrives: Optional[Sequence[str]] = None

class SalesforceChatterFeedConfigurationTypeDef(BaseModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    IncludeFilterTypes: Optional[Sequence[SalesforceChatterFeedIncludeFilterTypeType]] = None

class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(BaseModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(BaseModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class SalesforceStandardObjectAttachmentConfigurationTypeDef(BaseModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class SalesforceStandardObjectConfigurationTypeDef(BaseModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class ServiceNowKnowledgeArticleConfigurationTypeDef(BaseModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    FilterQuery: Optional[str] = None

class ServiceNowServiceCatalogConfigurationTypeDef(BaseModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class WorkDocsConfigurationTypeDef(BaseModel):
    OrganizationId: str
    CrawlComments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class BoxConfigurationTypeDef(BaseModel):
    EnterpriseId: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    CrawlTasks: Optional[bool] = None
    CrawlWebLinks: Optional[bool] = None
    FileFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    TaskFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    CommentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    WebLinkFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None

class FsxConfigurationTypeDef(BaseModel):
    FileSystemId: str
    FileSystemType: Literal["WINDOWS"]
    VpcConfiguration: DataSourceVpcConfigurationTypeDef
    SecretArn: Optional[str] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class JiraConfigurationTypeDef(BaseModel):
    JiraAccountUrl: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    Project: Optional[Sequence[str]] = None
    IssueType: Optional[Sequence[str]] = None
    Status: Optional[Sequence[str]] = None
    IssueSubEntityFilter: Optional[Sequence[IssueSubEntityType]] = None
    AttachmentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    CommentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    IssueFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    ProjectFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    WorkLogFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None

class QuipConfigurationTypeDef(BaseModel):
    Domain: str
    SecretArn: str
    CrawlFileComments: Optional[bool] = None
    CrawlChatRooms: Optional[bool] = None
    CrawlAttachments: Optional[bool] = None
    FolderIds: Optional[Sequence[str]] = None
    ThreadFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    MessageFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    AttachmentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None

class SlackConfigurationTypeDef(BaseModel):
    TeamId: str
    SecretArn: str
    SlackEntityList: Sequence[SlackEntityType]
    SinceCrawlDate: str
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    UseChangeLog: Optional[bool] = None
    CrawlBotMessage: Optional[bool] = None
    ExcludeArchived: Optional[bool] = None
    LookBackPeriod: Optional[int] = None
    PrivateChannelFilter: Optional[Sequence[str]] = None
    PublicChannelFilter: Optional[Sequence[str]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class AlfrescoConfigurationTypeDef(BaseModel):
    SiteUrl: str
    SiteId: str
    SecretArn: str
    SslCertificateS3Path: S3PathTypeDef
    CrawlSystemFolders: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    EntityFilter: Optional[Sequence[AlfrescoEntityType]] = None
    DocumentLibraryFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    BlogFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    WikiFieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None

class OnPremiseConfigurationTypeDef(BaseModel):
    HostUrl: str
    OrganizationName: str
    SslCertificateS3Path: S3PathTypeDef

class OneDriveUsersTypeDef(BaseModel):
    OneDriveUserList: Optional[Sequence[str]] = None
    OneDriveUserS3Path: Optional[S3PathTypeDef] = None

class UpdateQuerySuggestionsBlockListRequestRequestTypeDef(BaseModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SourceS3Path: Optional[S3PathTypeDef] = None
    RoleArn: Optional[str] = None

class UpdateThesaurusRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    SourceS3Path: Optional[S3PathTypeDef] = None

class AssociateEntitiesToExperienceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfigurationTypeDef]

class DisassociateEntitiesFromExperienceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfigurationTypeDef]

class AssociateEntitiesToExperienceResponseTypeDef(BaseModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePersonasToEntitiesResponseTypeDef(BaseModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessControlConfigurationResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperienceResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFaqResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuerySuggestionsBlockListResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThesaurusResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFaqResponseTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: str
    Description: str
    CreatedAt: datetime
    UpdatedAt: datetime
    S3Path: S3PathTypeDef
    Status: FaqStatusType
    RoleArn: str
    ErrorMessage: str
    FileFormat: FaqFileFormatType
    LanguageCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQuerySuggestionsBlockListResponseTypeDef(BaseModel):
    IndexId: str
    Id: str
    Name: str
    Description: str
    Status: QuerySuggestionsBlockListStatusType
    ErrorMessage: str
    CreatedAt: datetime
    UpdatedAt: datetime
    SourceS3Path: S3PathTypeDef
    ItemCount: int
    FileSizeBytes: int
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThesaurusResponseTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: str
    Description: str
    Status: ThesaurusStatusType
    ErrorMessage: str
    CreatedAt: datetime
    UpdatedAt: datetime
    RoleArn: str
    SourceS3Path: S3PathTypeDef
    FileSizeBytes: int
    TermCount: int
    SynonymRuleCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateEntitiesFromExperienceResponseTypeDef(BaseModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePersonasFromEntitiesResponseTypeDef(BaseModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessControlConfigurationsResponseTypeDef(BaseModel):
    NextToken: str
    AccessControlConfigurations: List[AccessControlConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceSyncJobResponseTypeDef(BaseModel):
    ExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePersonasToEntitiesRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    Personas: Sequence[EntityPersonaConfigurationTypeDef]

class AttributeSuggestionsDescribeConfigTypeDef(BaseModel):
    SuggestableConfigList: Optional[List[SuggestableConfigTypeDef]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None

class AttributeSuggestionsUpdateConfigTypeDef(BaseModel):
    SuggestableConfigList: Optional[Sequence[SuggestableConfigTypeDef]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None

class AuthenticationConfigurationTypeDef(BaseModel):
    BasicAuthentication: Optional[Sequence[BasicAuthenticationConfigurationTypeDef]] = None

class BatchDeleteDocumentRequestRequestTypeDef(BaseModel):
    IndexId: str
    DocumentIdList: Sequence[str]
    DataSourceSyncJobMetricTarget: Optional[DataSourceSyncJobMetricTargetTypeDef] = None

class BatchDeleteDocumentResponseTypeDef(BaseModel):
    FailedDocuments: List[BatchDeleteDocumentResponseFailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteFeaturedResultsSetResponseTypeDef(BaseModel):
    Errors: List[BatchDeleteFeaturedResultsSetErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDocumentStatusResponseTypeDef(BaseModel):
    Errors: List[BatchGetDocumentStatusResponseErrorTypeDef]
    DocumentStatusList: List[StatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutDocumentResponseTypeDef(BaseModel):
    FailedDocuments: List[BatchPutDocumentResponseFailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClickFeedbackTypeDef(BaseModel):
    ResultId: str
    ClickTime: TimestampTypeDef

class DocumentAttributeValueTypeDef(BaseModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[Sequence[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[TimestampTypeDef] = None

class CollapseConfigurationTypeDef(BaseModel):
    DocumentAttributeKey: str
    SortingConfigurations: Optional[Sequence[SortingConfigurationTypeDef]] = None
    MissingAttributeKeyStrategy: Optional[MissingAttributeKeyStrategyType] = None
    Expand: Optional[bool] = None
    ExpandConfiguration: Optional[ExpandConfigurationTypeDef] = None

class ConfluenceAttachmentConfigurationTypeDef(BaseModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[       Sequence[ConfluenceAttachmentToIndexFieldMappingTypeDef]     ] = None

class ConfluenceBlogConfigurationTypeDef(BaseModel):
    BlogFieldMappings: Optional[Sequence[ConfluenceBlogToIndexFieldMappingTypeDef]] = None

class SharePointConfigurationTypeDef(BaseModel):
    SharePointVersion: SharePointVersionType
    Urls: Sequence[str]
    SecretArn: str
    CrawlAttachments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    DocumentTitleFieldName: Optional[str] = None
    DisableLocalGroups: Optional[bool] = None
    SslCertificateS3Path: Optional[S3PathTypeDef] = None
    AuthenticationType: Optional[SharePointOnlineAuthenticationTypeType] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None

class ConfluencePageConfigurationTypeDef(BaseModel):
    PageFieldMappings: Optional[Sequence[ConfluencePageToIndexFieldMappingTypeDef]] = None

class ConfluenceSpaceConfigurationTypeDef(BaseModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[Sequence[str]] = None
    ExcludeSpaces: Optional[Sequence[str]] = None
    SpaceFieldMappings: Optional[Sequence[ConfluenceSpaceToIndexFieldMappingTypeDef]] = None

class SpellCorrectedQueryTypeDef(BaseModel):
    SuggestedQueryText: Optional[str] = None
    Corrections: Optional[List[CorrectionTypeDef]] = None

class HierarchicalPrincipalTypeDef(BaseModel):
    PrincipalList: Sequence[PrincipalTypeDef]

class CreateFaqRequestRequestTypeDef(BaseModel):
    IndexId: str
    Name: str
    S3Path: S3PathTypeDef
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FileFormat: Optional[FaqFileFormatType] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None

class CreateQuerySuggestionsBlockListRequestRequestTypeDef(BaseModel):
    IndexId: str
    Name: str
    SourceS3Path: S3PathTypeDef
    RoleArn: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateThesaurusRequestRequestTypeDef(BaseModel):
    IndexId: str
    Name: str
    RoleArn: str
    SourceS3Path: S3PathTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateFeaturedResultsSetRequestRequestTypeDef(BaseModel):
    IndexId: str
    FeaturedResultsSetName: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[Sequence[str]] = None
    FeaturedDocuments: Optional[Sequence[FeaturedDocumentTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class FeaturedResultsSetTypeDef(BaseModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[List[str]] = None
    FeaturedDocuments: Optional[List[FeaturedDocumentTypeDef]] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None

class UpdateFeaturedResultsSetRequestRequestTypeDef(BaseModel):
    IndexId: str
    FeaturedResultsSetId: str
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[Sequence[str]] = None
    FeaturedDocuments: Optional[Sequence[FeaturedDocumentTypeDef]] = None

class UserContextTypeDef(BaseModel):
    Token: Optional[str] = None
    UserId: Optional[str] = None
    Groups: Optional[Sequence[str]] = None
    DataSourceGroups: Optional[Sequence[DataSourceGroupTypeDef]] = None

class ListDataSourcesResponseTypeDef(BaseModel):
    SummaryItems: List[DataSourceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceSyncJobTypeDef(BaseModel):
    ExecutionId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[DataSourceSyncJobStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    DataSourceErrorCode: Optional[str] = None
    Metrics: Optional[DataSourceSyncJobMetricsTypeDef] = None

class ExperiencesSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Status: Optional[ExperienceStatusType] = None
    Endpoints: Optional[List[ExperienceEndpointTypeDef]] = None

class DescribeFeaturedResultsSetResponseTypeDef(BaseModel):
    FeaturedResultsSetId: str
    FeaturedResultsSetName: str
    Description: str
    Status: FeaturedResultsSetStatusType
    QueryTexts: List[str]
    FeaturedDocumentsWithMetadata: List[FeaturedDocumentWithMetadataTypeDef]
    FeaturedDocumentsMissing: List[FeaturedDocumentMissingTypeDef]
    LastUpdatedTimestamp: int
    CreationTimestamp: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePrincipalMappingResponseTypeDef(BaseModel):
    IndexId: str
    DataSourceId: str
    GroupId: str
    GroupOrderingIdSummaries: List[GroupOrderingIdSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentRelevanceConfigurationTypeDef(BaseModel):
    Name: str
    Relevance: RelevanceTypeDef

class DocumentMetadataConfigurationTypeDef(BaseModel):
    Name: str
    Type: DocumentAttributeValueTypeType
    Relevance: Optional[RelevanceTypeDef] = None
    Search: Optional[SearchTypeDef] = None

class S3DataSourceConfigurationTypeDef(BaseModel):
    BucketName: str
    InclusionPrefixes: Optional[Sequence[str]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    DocumentsMetadataConfiguration: Optional[DocumentsMetadataConfigurationTypeDef] = None
    AccessControlListConfiguration: Optional[AccessControlListConfigurationTypeDef] = None

class ExperienceEntitiesSummaryTypeDef(BaseModel):
    EntityId: Optional[str] = None
    EntityType: Optional[EntityTypeType] = None
    DisplayData: Optional[EntityDisplayDataTypeDef] = None

class ExperienceConfigurationTypeDef(BaseModel):
    ContentSourceConfiguration: Optional[ContentSourceConfigurationTypeDef] = None
    UserIdentityConfiguration: Optional[UserIdentityConfigurationTypeDef] = None

class ListFaqsResponseTypeDef(BaseModel):
    NextToken: str
    FaqSummaryItems: List[FaqSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFeaturedResultsSetsResponseTypeDef(BaseModel):
    FeaturedResultsSetSummaryItems: List[FeaturedResultsSetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotsResponseTypeDef(BaseModel):
    SnapShotTimeFilter: TimeRangeTypeDef
    SnapshotsDataHeader: List[str]
    SnapshotsData: List[List[str]]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourceSyncJobsRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeFilter: Optional[TimeRangeTypeDef] = None
    StatusFilter: Optional[DataSourceSyncJobStatusType] = None

class GroupMembersTypeDef(BaseModel):
    MemberGroups: Optional[Sequence[MemberGroupTypeDef]] = None
    MemberUsers: Optional[Sequence[MemberUserTypeDef]] = None
    S3PathforGroupMembers: Optional[S3PathTypeDef] = None

class ListGroupsOlderThanOrderingIdResponseTypeDef(BaseModel):
    GroupsSummaries: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TextWithHighlightsTypeDef(BaseModel):
    Text: Optional[str] = None
    Highlights: Optional[List[HighlightTypeDef]] = None

class ListIndicesResponseTypeDef(BaseModel):
    IndexConfigurationSummaryItems: List[IndexConfigurationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IndexStatisticsTypeDef(BaseModel):
    FaqStatistics: FaqStatisticsTypeDef
    TextDocumentStatistics: TextDocumentStatisticsTypeDef

class UserTokenConfigurationTypeDef(BaseModel):
    JwtTokenTypeConfiguration: Optional[JwtTokenTypeConfigurationTypeDef] = None
    JsonTokenTypeConfiguration: Optional[JsonTokenTypeConfigurationTypeDef] = None

class ListEntityPersonasResponseTypeDef(BaseModel):
    SummaryItems: List[PersonasSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQuerySuggestionsBlockListsResponseTypeDef(BaseModel):
    BlockListSummaryItems: List[QuerySuggestionsBlockListSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThesauriResponseTypeDef(BaseModel):
    NextToken: str
    ThesaurusSummaryItems: List[ThesaurusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UrlsTypeDef(BaseModel):
    SeedUrlConfiguration: Optional[SeedUrlConfigurationTypeDef] = None
    SiteMapsConfiguration: Optional[SiteMapsConfigurationTypeDef] = None

class SuggestionTextWithHighlightsTypeDef(BaseModel):
    Text: Optional[str] = None
    Highlights: Optional[List[SuggestionHighlightTypeDef]] = None

class TableRowTypeDef(BaseModel):
    Cells: Optional[List[TableCellTypeDef]] = None

class DatabaseConfigurationTypeDef(BaseModel):
    DatabaseEngineType: DatabaseEngineTypeType
    ConnectionConfiguration: ConnectionConfigurationTypeDef
    ColumnConfiguration: ColumnConfigurationTypeDef
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None
    SqlConfiguration: Optional[SqlConfigurationTypeDef] = None

class SalesforceKnowledgeArticleConfigurationTypeDef(BaseModel):
    IncludedStates: Sequence[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[       SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef     ] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[       Sequence[SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef]     ] = None

class ServiceNowConfigurationTypeDef(BaseModel):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionTypeType
    KnowledgeArticleConfiguration: Optional[       ServiceNowKnowledgeArticleConfigurationTypeDef     ] = None
    ServiceCatalogConfiguration: Optional[ServiceNowServiceCatalogConfigurationTypeDef] = None
    AuthenticationType: Optional[ServiceNowAuthenticationTypeType] = None

class GitHubConfigurationTypeDef(BaseModel):
    SecretArn: str
    SaaSConfiguration: Optional[SaaSConfigurationTypeDef] = None
    OnPremiseConfiguration: Optional[OnPremiseConfigurationTypeDef] = None
    Type: Optional[TypeType] = None
    UseChangeLog: Optional[bool] = None
    GitHubDocumentCrawlProperties: Optional[GitHubDocumentCrawlPropertiesTypeDef] = None
    RepositoryFilter: Optional[Sequence[str]] = None
    InclusionFolderNamePatterns: Optional[Sequence[str]] = None
    InclusionFileTypePatterns: Optional[Sequence[str]] = None
    InclusionFileNamePatterns: Optional[Sequence[str]] = None
    ExclusionFolderNamePatterns: Optional[Sequence[str]] = None
    ExclusionFileTypePatterns: Optional[Sequence[str]] = None
    ExclusionFileNamePatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    GitHubRepositoryConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubCommitConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubIssueDocumentConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubIssueCommentConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubIssueAttachmentConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubPullRequestCommentConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubPullRequestDocumentConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None
    GitHubPullRequestDocumentAttachmentConfigurationFieldMappings: Optional[       Sequence[DataSourceToIndexFieldMappingTypeDef]     ] = None

class OneDriveConfigurationTypeDef(BaseModel):
    TenantDomain: str
    SecretArn: str
    OneDriveUsers: OneDriveUsersTypeDef
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    DisableLocalGroups: Optional[bool] = None

class DescribeQuerySuggestionsConfigResponseTypeDef(BaseModel):
    Mode: ModeType
    Status: QuerySuggestionsStatusType
    QueryLogLookBackWindowInDays: int
    IncludeQueriesWithoutUserInformation: bool
    MinimumNumberOfQueryingUsers: int
    MinimumQueryCount: int
    LastSuggestionsBuildTime: datetime
    LastClearTime: datetime
    TotalSuggestionsCount: int
    AttributeSuggestionsConfig: AttributeSuggestionsDescribeConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQuerySuggestionsConfigRequestRequestTypeDef(BaseModel):
    IndexId: str
    Mode: Optional[ModeType] = None
    QueryLogLookBackWindowInDays: Optional[int] = None
    IncludeQueriesWithoutUserInformation: Optional[bool] = None
    MinimumNumberOfQueryingUsers: Optional[int] = None
    MinimumQueryCount: Optional[int] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsUpdateConfigTypeDef] = None

class SubmitFeedbackRequestRequestTypeDef(BaseModel):
    IndexId: str
    QueryId: str
    ClickFeedbackItems: Optional[Sequence[ClickFeedbackTypeDef]] = None
    RelevanceFeedbackItems: Optional[Sequence[RelevanceFeedbackTypeDef]] = None

class DocumentAttributeConditionTypeDef(BaseModel):
    ConditionDocumentAttributeKey: str
    Operator: ConditionOperatorType
    ConditionOnValue: Optional[DocumentAttributeValueTypeDef] = None

class DocumentAttributeTargetTypeDef(BaseModel):
    TargetDocumentAttributeKey: Optional[str] = None
    TargetDocumentAttributeValueDeletion: Optional[bool] = None
    TargetDocumentAttributeValue: Optional[DocumentAttributeValueTypeDef] = None

class DocumentAttributeTypeDef(BaseModel):
    Key: str
    Value: DocumentAttributeValueTypeDef

class DocumentAttributeValueCountPairTypeDef(BaseModel):
    DocumentAttributeValue: Optional[DocumentAttributeValueTypeDef] = None
    Count: Optional[int] = None
    FacetResults: Optional[List[Dict[str, Any]]] = None

class ConfluenceConfigurationTypeDef(BaseModel):
    ServerUrl: str
    SecretArn: str
    Version: ConfluenceVersionType
    SpaceConfiguration: Optional[ConfluenceSpaceConfigurationTypeDef] = None
    PageConfiguration: Optional[ConfluencePageConfigurationTypeDef] = None
    BlogConfiguration: Optional[ConfluenceBlogConfigurationTypeDef] = None
    AttachmentConfiguration: Optional[ConfluenceAttachmentConfigurationTypeDef] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None
    AuthenticationType: Optional[ConfluenceAuthenticationTypeType] = None

class CreateAccessControlConfigurationRequestRequestTypeDef(BaseModel):
    IndexId: str
    Name: str
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalTypeDef]] = None
    ClientToken: Optional[str] = None

class DescribeAccessControlConfigurationResponseTypeDef(BaseModel):
    Name: str
    Description: str
    ErrorMessage: str
    AccessControlList: List[PrincipalTypeDef]
    HierarchicalAccessControlList: List[HierarchicalPrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessControlConfigurationRequestRequestTypeDef(BaseModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalTypeDef]] = None

class CreateFeaturedResultsSetResponseTypeDef(BaseModel):
    FeaturedResultsSet: FeaturedResultsSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFeaturedResultsSetResponseTypeDef(BaseModel):
    FeaturedResultsSet: FeaturedResultsSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttributeSuggestionsGetConfigTypeDef(BaseModel):
    SuggestionAttributes: Optional[Sequence[str]] = None
    AdditionalResponseAttributes: Optional[Sequence[str]] = None
    AttributeFilter: Optional["AttributeFilterTypeDef"] = None
    UserContext: Optional[UserContextTypeDef] = None

class ListDataSourceSyncJobsResponseTypeDef(BaseModel):
    History: List[DataSourceSyncJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperiencesResponseTypeDef(BaseModel):
    SummaryItems: List[ExperiencesSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class QueryRequestRequestTypeDef(BaseModel):
    IndexId: str
    QueryText: Optional[str] = None
    AttributeFilter: Optional["AttributeFilterTypeDef"] = None
    Facets: Optional[Sequence["FacetTypeDef"]] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    QueryResultTypeFilter: Optional[QueryResultTypeType] = None
    DocumentRelevanceOverrideConfigurations: Optional[       Sequence[DocumentRelevanceConfigurationTypeDef]     ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    SortingConfiguration: Optional[SortingConfigurationTypeDef] = None
    SortingConfigurations: Optional[Sequence[SortingConfigurationTypeDef]] = None
    UserContext: Optional[UserContextTypeDef] = None
    VisitorId: Optional[str] = None
    SpellCorrectionConfiguration: Optional[SpellCorrectionConfigurationTypeDef] = None
    CollapseConfiguration: Optional[CollapseConfigurationTypeDef] = None

class RetrieveRequestRequestTypeDef(BaseModel):
    IndexId: str
    QueryText: str
    AttributeFilter: Optional["AttributeFilterTypeDef"] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    DocumentRelevanceOverrideConfigurations: Optional[       Sequence[DocumentRelevanceConfigurationTypeDef]     ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    UserContext: Optional[UserContextTypeDef] = None

class ListExperienceEntitiesResponseTypeDef(BaseModel):
    SummaryItems: List[ExperienceEntitiesSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperienceRequestRequestTypeDef(BaseModel):
    Name: str
    IndexId: str
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationTypeDef] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None

class DescribeExperienceResponseTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: str
    Endpoints: List[ExperienceEndpointTypeDef]
    Configuration: ExperienceConfigurationTypeDef
    CreatedAt: datetime
    UpdatedAt: datetime
    Description: str
    Status: ExperienceStatusType
    RoleArn: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperienceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationTypeDef] = None
    Description: Optional[str] = None

class PutPrincipalMappingRequestRequestTypeDef(BaseModel):
    IndexId: str
    GroupId: str
    GroupMembers: GroupMembersTypeDef
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None
    RoleArn: Optional[str] = None

class AdditionalResultAttributeValueTypeDef(BaseModel):
    TextWithHighlightsValue: Optional[TextWithHighlightsTypeDef] = None

class CreateIndexRequestRequestTypeDef(BaseModel):
    Name: str
    RoleArn: str
    Edition: Optional[IndexEditionType] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UserTokenConfigurations: Optional[Sequence[UserTokenConfigurationTypeDef]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfigurationTypeDef] = None

class DescribeIndexResponseTypeDef(BaseModel):
    Name: str
    Id: str
    Edition: IndexEditionType
    RoleArn: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Status: IndexStatusType
    Description: str
    CreatedAt: datetime
    UpdatedAt: datetime
    DocumentMetadataConfigurations: List[DocumentMetadataConfigurationTypeDef]
    IndexStatistics: IndexStatisticsTypeDef
    ErrorMessage: str
    CapacityUnits: CapacityUnitsConfigurationTypeDef
    UserTokenConfigurations: List[UserTokenConfigurationTypeDef]
    UserContextPolicy: UserContextPolicyType
    UserGroupResolutionConfiguration: UserGroupResolutionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIndexRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    DocumentMetadataConfigurationUpdates: Optional[       Sequence[DocumentMetadataConfigurationTypeDef]     ] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None
    UserTokenConfigurations: Optional[Sequence[UserTokenConfigurationTypeDef]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfigurationTypeDef] = None

class WebCrawlerConfigurationTypeDef(BaseModel):
    Urls: UrlsTypeDef
    CrawlDepth: Optional[int] = None
    MaxLinksPerPage: Optional[int] = None
    MaxContentSizePerPageInMegaBytes: Optional[float] = None
    MaxUrlsPerMinuteCrawlRate: Optional[int] = None
    UrlInclusionPatterns: Optional[Sequence[str]] = None
    UrlExclusionPatterns: Optional[Sequence[str]] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None

class SuggestionValueTypeDef(BaseModel):
    Text: Optional[SuggestionTextWithHighlightsTypeDef] = None

class TableExcerptTypeDef(BaseModel):
    Rows: Optional[List[TableRowTypeDef]] = None
    TotalNumberOfRows: Optional[int] = None

class SalesforceConfigurationTypeDef(BaseModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[       Sequence[SalesforceStandardObjectConfigurationTypeDef]     ] = None
    KnowledgeArticleConfiguration: Optional[       SalesforceKnowledgeArticleConfigurationTypeDef     ] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfigurationTypeDef] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[       SalesforceStandardObjectAttachmentConfigurationTypeDef     ] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None

class HookConfigurationTypeDef(BaseModel):
    LambdaArn: str
    S3Bucket: str
    InvocationCondition: Optional[DocumentAttributeConditionTypeDef] = None

class InlineCustomDocumentEnrichmentConfigurationTypeDef(BaseModel):
    Condition: Optional[DocumentAttributeConditionTypeDef] = None
    Target: Optional[DocumentAttributeTargetTypeDef] = None
    DocumentContentDeletion: Optional[bool] = None

class AttributeFilterTypeDef(BaseModel):
    AndAllFilters: Optional[Sequence[Dict[str, Any]]] = None
    OrAllFilters: Optional[Sequence[Dict[str, Any]]] = None
    NotFilter: Optional[Dict[str, Any]] = None
    EqualsTo: Optional[DocumentAttributeTypeDef] = None
    ContainsAll: Optional[DocumentAttributeTypeDef] = None
    ContainsAny: Optional[DocumentAttributeTypeDef] = None
    GreaterThan: Optional[DocumentAttributeTypeDef] = None
    GreaterThanOrEquals: Optional[DocumentAttributeTypeDef] = None
    LessThan: Optional[DocumentAttributeTypeDef] = None
    LessThanOrEquals: Optional[DocumentAttributeTypeDef] = None

class DocumentInfoTypeDef(BaseModel):
    DocumentId: str
    Attributes: Optional[Sequence[DocumentAttributeTypeDef]] = None

class DocumentTypeDef(BaseModel):
    Id: str
    Title: Optional[str] = None
    Blob: Optional[BlobTypeDef] = None
    S3Path: Optional[S3PathTypeDef] = None
    Attributes: Optional[Sequence[DocumentAttributeTypeDef]] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalTypeDef]] = None
    ContentType: Optional[ContentTypeType] = None
    AccessControlConfigurationId: Optional[str] = None

class ExpandedResultItemTypeDef(BaseModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlightsTypeDef] = None
    DocumentExcerpt: Optional[TextWithHighlightsTypeDef] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None

class RetrieveResultItemTypeDef(BaseModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[str] = None
    Content: Optional[str] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None
    ScoreAttributes: Optional[ScoreAttributesTypeDef] = None

class SourceDocumentTypeDef(BaseModel):
    DocumentId: Optional[str] = None
    SuggestionAttributes: Optional[List[str]] = None
    AdditionalAttributes: Optional[List[DocumentAttributeTypeDef]] = None

class GetQuerySuggestionsRequestRequestTypeDef(BaseModel):
    IndexId: str
    QueryText: str
    MaxSuggestionsCount: Optional[int] = None
    SuggestionTypes: Optional[Sequence[SuggestionTypeType]] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsGetConfigTypeDef] = None

class AdditionalResultAttributeTypeDef(BaseModel):
    Key: str
    ValueType: Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
    Value: AdditionalResultAttributeValueTypeDef

class DataSourceConfigurationTypeDef(BaseModel):
    S3Configuration: Optional[S3DataSourceConfigurationTypeDef] = None
    SharePointConfiguration: Optional[SharePointConfigurationTypeDef] = None
    DatabaseConfiguration: Optional[DatabaseConfigurationTypeDef] = None
    SalesforceConfiguration: Optional[SalesforceConfigurationTypeDef] = None
    OneDriveConfiguration: Optional[OneDriveConfigurationTypeDef] = None
    ServiceNowConfiguration: Optional[ServiceNowConfigurationTypeDef] = None
    ConfluenceConfiguration: Optional[ConfluenceConfigurationTypeDef] = None
    GoogleDriveConfiguration: Optional[GoogleDriveConfigurationTypeDef] = None
    WebCrawlerConfiguration: Optional[WebCrawlerConfigurationTypeDef] = None
    WorkDocsConfiguration: Optional[WorkDocsConfigurationTypeDef] = None
    FsxConfiguration: Optional[FsxConfigurationTypeDef] = None
    SlackConfiguration: Optional[SlackConfigurationTypeDef] = None
    BoxConfiguration: Optional[BoxConfigurationTypeDef] = None
    QuipConfiguration: Optional[QuipConfigurationTypeDef] = None
    JiraConfiguration: Optional[JiraConfigurationTypeDef] = None
    GitHubConfiguration: Optional[GitHubConfigurationTypeDef] = None
    AlfrescoConfiguration: Optional[AlfrescoConfigurationTypeDef] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None

class CustomDocumentEnrichmentConfigurationTypeDef(BaseModel):
    InlineConfigurations: Optional[       Sequence[InlineCustomDocumentEnrichmentConfigurationTypeDef]     ] = None
    PreExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    PostExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    RoleArn: Optional[str] = None

class BatchGetDocumentStatusRequestRequestTypeDef(BaseModel):
    IndexId: str
    DocumentInfoList: Sequence[DocumentInfoTypeDef]

class CollapsedResultDetailTypeDef(BaseModel):
    DocumentAttribute: DocumentAttributeTypeDef
    ExpandedResults: Optional[List[ExpandedResultItemTypeDef]] = None

class RetrieveResultTypeDef(BaseModel):
    QueryId: str
    ResultItems: List[RetrieveResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SuggestionTypeDef(BaseModel):
    Id: Optional[str] = None
    Value: Optional[SuggestionValueTypeDef] = None
    SourceDocuments: Optional[List[SourceDocumentTypeDef]] = None

class FeaturedResultsItemTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[QueryResultTypeType] = None
    AdditionalAttributes: Optional[List[AdditionalResultAttributeTypeDef]] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlightsTypeDef] = None
    DocumentExcerpt: Optional[TextWithHighlightsTypeDef] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None
    FeedbackToken: Optional[str] = None

class BatchPutDocumentRequestRequestTypeDef(BaseModel):
    IndexId: str
    Documents: Sequence[DocumentTypeDef]
    RoleArn: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[       CustomDocumentEnrichmentConfigurationTypeDef     ] = None

class CreateDataSourceRequestRequestTypeDef(BaseModel):
    Name: str
    IndexId: str
    Type: DataSourceTypeType
    Configuration: Optional[DataSourceConfigurationTypeDef] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[       CustomDocumentEnrichmentConfigurationTypeDef     ] = None

class DescribeDataSourceResponseTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: str
    Type: DataSourceTypeType
    Configuration: DataSourceConfigurationTypeDef
    VpcConfiguration: DataSourceVpcConfigurationTypeDef
    CreatedAt: datetime
    UpdatedAt: datetime
    Description: str
    Status: DataSourceStatusType
    Schedule: str
    RoleArn: str
    ErrorMessage: str
    LanguageCode: str
    CustomDocumentEnrichmentConfiguration: CustomDocumentEnrichmentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceRequestRequestTypeDef(BaseModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Configuration: Optional[DataSourceConfigurationTypeDef] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    RoleArn: Optional[str] = None
    LanguageCode: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[       CustomDocumentEnrichmentConfigurationTypeDef     ] = None

class QueryResultItemTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[QueryResultTypeType] = None
    Format: Optional[QueryResultFormatType] = None
    AdditionalAttributes: Optional[List[AdditionalResultAttributeTypeDef]] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlightsTypeDef] = None
    DocumentExcerpt: Optional[TextWithHighlightsTypeDef] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None
    ScoreAttributes: Optional[ScoreAttributesTypeDef] = None
    FeedbackToken: Optional[str] = None
    TableExcerpt: Optional[TableExcerptTypeDef] = None
    CollapsedResultDetail: Optional[CollapsedResultDetailTypeDef] = None

class GetQuerySuggestionsResponseTypeDef(BaseModel):
    QuerySuggestionsId: str
    Suggestions: List[SuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryResultTypeDef(BaseModel):
    QueryId: str
    ResultItems: List[QueryResultItemTypeDef]
    FacetResults: List["FacetResultTypeDef"]
    TotalNumberOfResults: int
    Warnings: List[WarningTypeDef]
    SpellCorrectedQueries: List[SpellCorrectedQueryTypeDef]
    FeaturedResultsItems: List[FeaturedResultsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

