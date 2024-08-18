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
from aws_resource_validator.pydantic_models.kendra_constants import *

class AccessControlConfigurationSummaryTypeDef(BaseValidatorModel):
    Id: str

class AccessControlListConfigurationTypeDef(BaseValidatorModel):
    KeyPath: Optional[str] = None

class AclConfigurationTypeDef(BaseValidatorModel):
    AllowedGroupsColumnName: str

class DataSourceToIndexFieldMappingTypeDef(BaseValidatorModel):
    DataSourceFieldName: str
    IndexFieldName: str
    DateFieldFormat: Optional[str] = None

class DataSourceVpcConfigurationTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class S3PathTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str

class EntityConfigurationTypeDef(BaseValidatorModel):
    EntityId: str
    EntityType: EntityTypeType

class FailedEntityTypeDef(BaseValidatorModel):
    EntityId: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class EntityPersonaConfigurationTypeDef(BaseValidatorModel):
    EntityId: str
    Persona: PersonaType

class SuggestableConfigTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    Suggestable: Optional[bool] = None

class BasicAuthenticationConfigurationTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Credentials: str

class DataSourceSyncJobMetricTargetTypeDef(BaseValidatorModel):
    DataSourceId: str
    DataSourceSyncJobId: Optional[str] = None

class BatchDeleteDocumentResponseFailedDocumentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchDeleteFeaturedResultsSetErrorTypeDef(BaseValidatorModel):
    Id: str
    ErrorCode: ErrorCodeType
    ErrorMessage: str

class BatchDeleteFeaturedResultsSetRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetIds: Sequence[str]

class BatchGetDocumentStatusResponseErrorTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class StatusTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    DocumentStatus: Optional[DocumentStatusType] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None

class BatchPutDocumentResponseFailedDocumentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class CapacityUnitsConfigurationTypeDef(BaseValidatorModel):
    StorageCapacityUnits: int
    QueryCapacityUnits: int

class ClearQuerySuggestionsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str

class ExpandConfigurationTypeDef(BaseValidatorModel):
    MaxResultItemsToExpand: Optional[int] = None
    MaxExpandedResultsPerItem: Optional[int] = None

class SortingConfigurationTypeDef(BaseValidatorModel):
    DocumentAttributeKey: str
    SortOrder: SortOrderType

class ConfluenceAttachmentToIndexFieldMappingTypeDef(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluenceAttachmentFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ConfluenceBlogToIndexFieldMappingTypeDef(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluenceBlogFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ProxyConfigurationTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Credentials: Optional[str] = None

class ConfluencePageToIndexFieldMappingTypeDef(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluencePageFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ConfluenceSpaceToIndexFieldMappingTypeDef(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluenceSpaceFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None

class ConnectionConfigurationTypeDef(BaseValidatorModel):
    DatabaseHost: str
    DatabasePort: int
    DatabaseName: str
    TableName: str
    SecretArn: str

class ContentSourceConfigurationTypeDef(BaseValidatorModel):
    DataSourceIds: Optional[Sequence[str]] = None
    FaqIds: Optional[Sequence[str]] = None
    DirectPutContent: Optional[bool] = None

class CorrectionTypeDef(BaseValidatorModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Term: Optional[str] = None
    CorrectedTerm: Optional[str] = None

class PrincipalTypeDef(BaseValidatorModel):
    Name: str
    Type: PrincipalTypeType
    Access: ReadAccessTypeType
    DataSourceId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class FeaturedDocumentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None

class UserGroupResolutionConfigurationTypeDef(BaseValidatorModel):
    UserGroupResolutionMode: UserGroupResolutionModeType

class TemplateConfigurationTypeDef(BaseValidatorModel):
    Template: Optional[Mapping[str, Any]] = None

class DataSourceGroupTypeDef(BaseValidatorModel):
    GroupId: str
    DataSourceId: str

class DataSourceSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[DataSourceStatusType] = None
    LanguageCode: Optional[str] = None

class DataSourceSyncJobMetricsTypeDef(BaseValidatorModel):
    DocumentsAdded: Optional[str] = None
    DocumentsModified: Optional[str] = None
    DocumentsDeleted: Optional[str] = None
    DocumentsFailed: Optional[str] = None
    DocumentsScanned: Optional[str] = None

class SqlConfigurationTypeDef(BaseValidatorModel):
    QueryIdentifiersEnclosingOption: Optional[QueryIdentifiersEnclosingOptionType] = None

class DeleteAccessControlConfigurationRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str

class DeleteDataSourceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DeleteExperienceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DeleteFaqRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DeleteIndexRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeletePrincipalMappingRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None

class DeleteQuerySuggestionsBlockListRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str

class DeleteThesaurusRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DescribeAccessControlConfigurationRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str

class DescribeDataSourceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DescribeExperienceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class ExperienceEndpointTypeDef(BaseValidatorModel):
    EndpointType: Optional[Literal["HOME"]] = None
    Endpoint: Optional[str] = None

class DescribeFaqRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DescribeFeaturedResultsSetRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str

class FeaturedDocumentMissingTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class FeaturedDocumentWithMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    URI: Optional[str] = None

class DescribeIndexRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribePrincipalMappingRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None

class GroupOrderingIdSummaryTypeDef(BaseValidatorModel):
    Status: Optional[PrincipalMappingStatusType] = None
    LastUpdatedAt: Optional[datetime] = None
    ReceivedAt: Optional[datetime] = None
    OrderingId: Optional[int] = None
    FailureReason: Optional[str] = None

class DescribeQuerySuggestionsBlockListRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str

class DescribeQuerySuggestionsConfigRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str

class DescribeThesaurusRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class DisassociatePersonasFromEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityIds: Sequence[str]

class RelevanceTypeDef(BaseValidatorModel):
    Freshness: Optional[bool] = None
    Importance: Optional[int] = None
    Duration: Optional[str] = None
    RankOrder: Optional[OrderType] = None
    ValueImportanceMap: Optional[Dict[str, int]] = None

class SearchTypeDef(BaseValidatorModel):
    Facetable: Optional[bool] = None
    Searchable: Optional[bool] = None
    Displayable: Optional[bool] = None
    Sortable: Optional[bool] = None

class DocumentsMetadataConfigurationTypeDef(BaseValidatorModel):
    S3Prefix: Optional[str] = None

class EntityDisplayDataTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    GroupName: Optional[str] = None
    IdentifiedUserName: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class UserIdentityConfigurationTypeDef(BaseValidatorModel):
    IdentityAttributeName: Optional[str] = None

class FacetResultTypeDef(BaseValidatorModel):
    DocumentAttributeKey: Optional[str] = None
    DocumentAttributeValueType: Optional[DocumentAttributeValueTypeType] = None
    DocumentAttributeValueCountPairs: Optional[       List["DocumentAttributeValueCountPairTypeDef"]     ] = None

class FacetTypeDef(BaseValidatorModel):
    DocumentAttributeKey: Optional[str] = None
    Facets: Optional[Sequence[Dict[str, Any]]] = None
    MaxResults: Optional[int] = None

class FaqStatisticsTypeDef(BaseValidatorModel):
    IndexedQuestionAnswersCount: int

class FaqSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[FaqStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    FileFormat: Optional[FaqFileFormatType] = None
    LanguageCode: Optional[str] = None

class FeaturedResultsSetSummaryTypeDef(BaseValidatorModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None

class GetSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Interval: IntervalType
    MetricType: MetricTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TimeRangeTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class GitHubDocumentCrawlPropertiesTypeDef(BaseValidatorModel):
    CrawlRepositoryDocuments: Optional[bool] = None
    CrawlIssue: Optional[bool] = None
    CrawlIssueComment: Optional[bool] = None
    CrawlIssueCommentAttachment: Optional[bool] = None
    CrawlPullRequest: Optional[bool] = None
    CrawlPullRequestComment: Optional[bool] = None
    CrawlPullRequestCommentAttachment: Optional[bool] = None

class SaaSConfigurationTypeDef(BaseValidatorModel):
    OrganizationName: str
    HostUrl: str

class MemberGroupTypeDef(BaseValidatorModel):
    GroupId: str
    DataSourceId: Optional[str] = None

class MemberUserTypeDef(BaseValidatorModel):
    UserId: str

class GroupSummaryTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    OrderingId: Optional[int] = None

class HighlightTypeDef(BaseValidatorModel):
    BeginOffset: int
    EndOffset: int
    TopAnswer: Optional[bool] = None
    Type: Optional[HighlightTypeType] = None

class IndexConfigurationSummaryTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: IndexStatusType
    Name: Optional[str] = None
    Id: Optional[str] = None
    Edition: Optional[IndexEditionType] = None

class TextDocumentStatisticsTypeDef(BaseValidatorModel):
    IndexedTextDocumentsCount: int
    IndexedTextBytes: int

class JsonTokenTypeConfigurationTypeDef(BaseValidatorModel):
    UserNameAttributeField: str
    GroupAttributeField: str

class JwtTokenTypeConfigurationTypeDef(BaseValidatorModel):
    KeyLocation: KeyLocationType
    URL: Optional[str] = None
    SecretManagerArn: Optional[str] = None
    UserNameAttributeField: Optional[str] = None
    GroupAttributeField: Optional[str] = None
    Issuer: Optional[str] = None
    ClaimRegex: Optional[str] = None

class ListAccessControlConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntityPersonasRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PersonasSummaryTypeDef(BaseValidatorModel):
    EntityId: Optional[str] = None
    Persona: Optional[PersonaType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ListExperienceEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None

class ListExperiencesRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFaqsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFeaturedResultsSetsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupsOlderThanOrderingIdRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    OrderingId: int
    DataSourceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIndicesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListQuerySuggestionsBlockListsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QuerySuggestionsBlockListSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[QuerySuggestionsBlockListStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ItemCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListThesauriRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ThesaurusSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ThesaurusStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class SpellCorrectionConfigurationTypeDef(BaseValidatorModel):
    IncludeQuerySpellCheckSuggestions: bool

class ScoreAttributesTypeDef(BaseValidatorModel):
    ScoreConfidence: Optional[ScoreConfidenceType] = None

class WarningTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Code: Optional[Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]] = None

class RelevanceFeedbackTypeDef(BaseValidatorModel):
    ResultId: str
    RelevanceValue: RelevanceTypeType

class SeedUrlConfigurationTypeDef(BaseValidatorModel):
    SeedUrls: Sequence[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None

class SiteMapsConfigurationTypeDef(BaseValidatorModel):
    SiteMaps: Sequence[str]

class StartDataSourceSyncJobRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class StopDataSourceSyncJobRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str

class SuggestionHighlightTypeDef(BaseValidatorModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class TableCellTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    TopAnswer: Optional[bool] = None
    Highlighted: Optional[bool] = None
    Header: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ColumnConfigurationTypeDef(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: Sequence[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class GoogleDriveConfigurationTypeDef(BaseValidatorModel):
    SecretArn: str
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    ExcludeMimeTypes: Optional[Sequence[str]] = None
    ExcludeUserAccounts: Optional[Sequence[str]] = None
    ExcludeSharedDrives: Optional[Sequence[str]] = None

class SalesforceChatterFeedConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    IncludeFilterTypes: Optional[Sequence[SalesforceChatterFeedIncludeFilterTypeType]] = None

class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class SalesforceStandardObjectAttachmentConfigurationTypeDef(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class SalesforceStandardObjectConfigurationTypeDef(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class ServiceNowKnowledgeArticleConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    FilterQuery: Optional[str] = None

class ServiceNowServiceCatalogConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class WorkDocsConfigurationTypeDef(BaseValidatorModel):
    OrganizationId: str
    CrawlComments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class BoxConfigurationTypeDef(BaseValidatorModel):
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

class FsxConfigurationTypeDef(BaseValidatorModel):
    FileSystemId: str
    FileSystemType: Literal["WINDOWS"]
    VpcConfiguration: DataSourceVpcConfigurationTypeDef
    SecretArn: Optional[str] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None

class JiraConfigurationTypeDef(BaseValidatorModel):
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

class QuipConfigurationTypeDef(BaseValidatorModel):
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

class SlackConfigurationTypeDef(BaseValidatorModel):
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

class AlfrescoConfigurationTypeDef(BaseValidatorModel):
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

class OnPremiseConfigurationTypeDef(BaseValidatorModel):
    HostUrl: str
    OrganizationName: str
    SslCertificateS3Path: S3PathTypeDef

class OneDriveUsersTypeDef(BaseValidatorModel):
    OneDriveUserList: Optional[Sequence[str]] = None
    OneDriveUserS3Path: Optional[S3PathTypeDef] = None

class UpdateQuerySuggestionsBlockListRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SourceS3Path: Optional[S3PathTypeDef] = None
    RoleArn: Optional[str] = None

class UpdateThesaurusRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    SourceS3Path: Optional[S3PathTypeDef] = None

class AssociateEntitiesToExperienceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfigurationTypeDef]

class DisassociateEntitiesFromExperienceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfigurationTypeDef]

class AssociateEntitiesToExperienceResponseTypeDef(BaseValidatorModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePersonasToEntitiesResponseTypeDef(BaseValidatorModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessControlConfigurationResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperienceResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFaqResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuerySuggestionsBlockListResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThesaurusResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFaqResponseTypeDef(BaseValidatorModel):
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

class DescribeQuerySuggestionsBlockListResponseTypeDef(BaseValidatorModel):
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

class DescribeThesaurusResponseTypeDef(BaseValidatorModel):
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

class DisassociateEntitiesFromExperienceResponseTypeDef(BaseValidatorModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePersonasFromEntitiesResponseTypeDef(BaseValidatorModel):
    FailedEntityList: List[FailedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessControlConfigurationsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    AccessControlConfigurations: List[AccessControlConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceSyncJobResponseTypeDef(BaseValidatorModel):
    ExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePersonasToEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Personas: Sequence[EntityPersonaConfigurationTypeDef]

class AttributeSuggestionsDescribeConfigTypeDef(BaseValidatorModel):
    SuggestableConfigList: Optional[List[SuggestableConfigTypeDef]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None

class AttributeSuggestionsUpdateConfigTypeDef(BaseValidatorModel):
    SuggestableConfigList: Optional[Sequence[SuggestableConfigTypeDef]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None

class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    BasicAuthentication: Optional[Sequence[BasicAuthenticationConfigurationTypeDef]] = None

class BatchDeleteDocumentRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    DocumentIdList: Sequence[str]
    DataSourceSyncJobMetricTarget: Optional[DataSourceSyncJobMetricTargetTypeDef] = None

class BatchDeleteDocumentResponseTypeDef(BaseValidatorModel):
    FailedDocuments: List[BatchDeleteDocumentResponseFailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteFeaturedResultsSetResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchDeleteFeaturedResultsSetErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDocumentStatusResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchGetDocumentStatusResponseErrorTypeDef]
    DocumentStatusList: List[StatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutDocumentResponseTypeDef(BaseValidatorModel):
    FailedDocuments: List[BatchPutDocumentResponseFailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClickFeedbackTypeDef(BaseValidatorModel):
    ResultId: str
    ClickTime: TimestampTypeDef

class DocumentAttributeValueTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[Sequence[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[TimestampTypeDef] = None

class CollapseConfigurationTypeDef(BaseValidatorModel):
    DocumentAttributeKey: str
    SortingConfigurations: Optional[Sequence[SortingConfigurationTypeDef]] = None
    MissingAttributeKeyStrategy: Optional[MissingAttributeKeyStrategyType] = None
    Expand: Optional[bool] = None
    ExpandConfiguration: Optional[ExpandConfigurationTypeDef] = None

class ConfluenceAttachmentConfigurationTypeDef(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[       Sequence[ConfluenceAttachmentToIndexFieldMappingTypeDef]     ] = None

class ConfluenceBlogConfigurationTypeDef(BaseValidatorModel):
    BlogFieldMappings: Optional[Sequence[ConfluenceBlogToIndexFieldMappingTypeDef]] = None

class SharePointConfigurationTypeDef(BaseValidatorModel):
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

class ConfluencePageConfigurationTypeDef(BaseValidatorModel):
    PageFieldMappings: Optional[Sequence[ConfluencePageToIndexFieldMappingTypeDef]] = None

class ConfluenceSpaceConfigurationTypeDef(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[Sequence[str]] = None
    ExcludeSpaces: Optional[Sequence[str]] = None
    SpaceFieldMappings: Optional[Sequence[ConfluenceSpaceToIndexFieldMappingTypeDef]] = None

class SpellCorrectedQueryTypeDef(BaseValidatorModel):
    SuggestedQueryText: Optional[str] = None
    Corrections: Optional[List[CorrectionTypeDef]] = None

class HierarchicalPrincipalTypeDef(BaseValidatorModel):
    PrincipalList: Sequence[PrincipalTypeDef]

class CreateFaqRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    S3Path: S3PathTypeDef
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FileFormat: Optional[FaqFileFormatType] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None

class CreateQuerySuggestionsBlockListRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    SourceS3Path: S3PathTypeDef
    RoleArn: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateThesaurusRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    RoleArn: str
    SourceS3Path: S3PathTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateFeaturedResultsSetRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetName: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[Sequence[str]] = None
    FeaturedDocuments: Optional[Sequence[FeaturedDocumentTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class FeaturedResultsSetTypeDef(BaseValidatorModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[List[str]] = None
    FeaturedDocuments: Optional[List[FeaturedDocumentTypeDef]] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None

class UpdateFeaturedResultsSetRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[Sequence[str]] = None
    FeaturedDocuments: Optional[Sequence[FeaturedDocumentTypeDef]] = None

class UserContextTypeDef(BaseValidatorModel):
    Token: Optional[str] = None
    UserId: Optional[str] = None
    Groups: Optional[Sequence[str]] = None
    DataSourceGroups: Optional[Sequence[DataSourceGroupTypeDef]] = None

class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[DataSourceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceSyncJobTypeDef(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[DataSourceSyncJobStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    DataSourceErrorCode: Optional[str] = None
    Metrics: Optional[DataSourceSyncJobMetricsTypeDef] = None

class ExperiencesSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Status: Optional[ExperienceStatusType] = None
    Endpoints: Optional[List[ExperienceEndpointTypeDef]] = None

class DescribeFeaturedResultsSetResponseTypeDef(BaseValidatorModel):
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

class DescribePrincipalMappingResponseTypeDef(BaseValidatorModel):
    IndexId: str
    DataSourceId: str
    GroupId: str
    GroupOrderingIdSummaries: List[GroupOrderingIdSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentRelevanceConfigurationTypeDef(BaseValidatorModel):
    Name: str
    Relevance: RelevanceTypeDef

class DocumentMetadataConfigurationTypeDef(BaseValidatorModel):
    Name: str
    Type: DocumentAttributeValueTypeType
    Relevance: Optional[RelevanceTypeDef] = None
    Search: Optional[SearchTypeDef] = None

class S3DataSourceConfigurationTypeDef(BaseValidatorModel):
    BucketName: str
    InclusionPrefixes: Optional[Sequence[str]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    DocumentsMetadataConfiguration: Optional[DocumentsMetadataConfigurationTypeDef] = None
    AccessControlListConfiguration: Optional[AccessControlListConfigurationTypeDef] = None

class ExperienceEntitiesSummaryTypeDef(BaseValidatorModel):
    EntityId: Optional[str] = None
    EntityType: Optional[EntityTypeType] = None
    DisplayData: Optional[EntityDisplayDataTypeDef] = None

class ExperienceConfigurationTypeDef(BaseValidatorModel):
    ContentSourceConfiguration: Optional[ContentSourceConfigurationTypeDef] = None
    UserIdentityConfiguration: Optional[UserIdentityConfigurationTypeDef] = None

class ListFaqsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    FaqSummaryItems: List[FaqSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFeaturedResultsSetsResponseTypeDef(BaseValidatorModel):
    FeaturedResultsSetSummaryItems: List[FeaturedResultsSetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotsResponseTypeDef(BaseValidatorModel):
    SnapShotTimeFilter: TimeRangeTypeDef
    SnapshotsDataHeader: List[str]
    SnapshotsData: List[List[str]]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourceSyncJobsRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeFilter: Optional[TimeRangeTypeDef] = None
    StatusFilter: Optional[DataSourceSyncJobStatusType] = None

class GroupMembersTypeDef(BaseValidatorModel):
    MemberGroups: Optional[Sequence[MemberGroupTypeDef]] = None
    MemberUsers: Optional[Sequence[MemberUserTypeDef]] = None
    S3PathforGroupMembers: Optional[S3PathTypeDef] = None

class ListGroupsOlderThanOrderingIdResponseTypeDef(BaseValidatorModel):
    GroupsSummaries: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TextWithHighlightsTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    Highlights: Optional[List[HighlightTypeDef]] = None

class ListIndicesResponseTypeDef(BaseValidatorModel):
    IndexConfigurationSummaryItems: List[IndexConfigurationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IndexStatisticsTypeDef(BaseValidatorModel):
    FaqStatistics: FaqStatisticsTypeDef
    TextDocumentStatistics: TextDocumentStatisticsTypeDef

class UserTokenConfigurationTypeDef(BaseValidatorModel):
    JwtTokenTypeConfiguration: Optional[JwtTokenTypeConfigurationTypeDef] = None
    JsonTokenTypeConfiguration: Optional[JsonTokenTypeConfigurationTypeDef] = None

class ListEntityPersonasResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[PersonasSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQuerySuggestionsBlockListsResponseTypeDef(BaseValidatorModel):
    BlockListSummaryItems: List[QuerySuggestionsBlockListSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThesauriResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ThesaurusSummaryItems: List[ThesaurusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UrlsTypeDef(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfigurationTypeDef] = None
    SiteMapsConfiguration: Optional[SiteMapsConfigurationTypeDef] = None

class SuggestionTextWithHighlightsTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    Highlights: Optional[List[SuggestionHighlightTypeDef]] = None

class TableRowTypeDef(BaseValidatorModel):
    Cells: Optional[List[TableCellTypeDef]] = None

class DatabaseConfigurationTypeDef(BaseValidatorModel):
    DatabaseEngineType: DatabaseEngineTypeType
    ConnectionConfiguration: ConnectionConfigurationTypeDef
    ColumnConfiguration: ColumnConfigurationTypeDef
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None
    SqlConfiguration: Optional[SqlConfigurationTypeDef] = None

class SalesforceKnowledgeArticleConfigurationTypeDef(BaseValidatorModel):
    IncludedStates: Sequence[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[       SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef     ] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[       Sequence[SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef]     ] = None

class ServiceNowConfigurationTypeDef(BaseValidatorModel):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionTypeType
    KnowledgeArticleConfiguration: Optional[       ServiceNowKnowledgeArticleConfigurationTypeDef     ] = None
    ServiceCatalogConfiguration: Optional[ServiceNowServiceCatalogConfigurationTypeDef] = None
    AuthenticationType: Optional[ServiceNowAuthenticationTypeType] = None

class GitHubConfigurationTypeDef(BaseValidatorModel):
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

class OneDriveConfigurationTypeDef(BaseValidatorModel):
    TenantDomain: str
    SecretArn: str
    OneDriveUsers: OneDriveUsersTypeDef
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    DisableLocalGroups: Optional[bool] = None

class DescribeQuerySuggestionsConfigResponseTypeDef(BaseValidatorModel):
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

class UpdateQuerySuggestionsConfigRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Mode: Optional[ModeType] = None
    QueryLogLookBackWindowInDays: Optional[int] = None
    IncludeQueriesWithoutUserInformation: Optional[bool] = None
    MinimumNumberOfQueryingUsers: Optional[int] = None
    MinimumQueryCount: Optional[int] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsUpdateConfigTypeDef] = None

class SubmitFeedbackRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    QueryId: str
    ClickFeedbackItems: Optional[Sequence[ClickFeedbackTypeDef]] = None
    RelevanceFeedbackItems: Optional[Sequence[RelevanceFeedbackTypeDef]] = None

class DocumentAttributeConditionTypeDef(BaseValidatorModel):
    ConditionDocumentAttributeKey: str
    Operator: ConditionOperatorType
    ConditionOnValue: Optional[DocumentAttributeValueTypeDef] = None

class DocumentAttributeTargetTypeDef(BaseValidatorModel):
    TargetDocumentAttributeKey: Optional[str] = None
    TargetDocumentAttributeValueDeletion: Optional[bool] = None
    TargetDocumentAttributeValue: Optional[DocumentAttributeValueTypeDef] = None

class DocumentAttributeTypeDef(BaseValidatorModel):
    Key: str
    Value: DocumentAttributeValueTypeDef

class DocumentAttributeValueCountPairTypeDef(BaseValidatorModel):
    DocumentAttributeValue: Optional[DocumentAttributeValueTypeDef] = None
    Count: Optional[int] = None
    FacetResults: Optional[List[Dict[str, Any]]] = None

class ConfluenceConfigurationTypeDef(BaseValidatorModel):
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

class CreateAccessControlConfigurationRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalTypeDef]] = None
    ClientToken: Optional[str] = None

class DescribeAccessControlConfigurationResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    ErrorMessage: str
    AccessControlList: List[PrincipalTypeDef]
    HierarchicalAccessControlList: List[HierarchicalPrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessControlConfigurationRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalTypeDef]] = None

class CreateFeaturedResultsSetResponseTypeDef(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFeaturedResultsSetResponseTypeDef(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttributeSuggestionsGetConfigTypeDef(BaseValidatorModel):
    SuggestionAttributes: Optional[Sequence[str]] = None
    AdditionalResponseAttributes: Optional[Sequence[str]] = None
    AttributeFilter: Optional["AttributeFilterTypeDef"] = None
    UserContext: Optional[UserContextTypeDef] = None

class ListDataSourceSyncJobsResponseTypeDef(BaseValidatorModel):
    History: List[DataSourceSyncJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperiencesResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[ExperiencesSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class QueryRequestRequestTypeDef(BaseValidatorModel):
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

class RetrieveRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    QueryText: str
    AttributeFilter: Optional["AttributeFilterTypeDef"] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    DocumentRelevanceOverrideConfigurations: Optional[       Sequence[DocumentRelevanceConfigurationTypeDef]     ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    UserContext: Optional[UserContextTypeDef] = None

class ListExperienceEntitiesResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[ExperienceEntitiesSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperienceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    IndexId: str
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationTypeDef] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None

class DescribeExperienceResponseTypeDef(BaseValidatorModel):
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

class UpdateExperienceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationTypeDef] = None
    Description: Optional[str] = None

class PutPrincipalMappingRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    GroupId: str
    GroupMembers: GroupMembersTypeDef
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None
    RoleArn: Optional[str] = None

class AdditionalResultAttributeValueTypeDef(BaseValidatorModel):
    TextWithHighlightsValue: Optional[TextWithHighlightsTypeDef] = None

class CreateIndexRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeIndexResponseTypeDef(BaseValidatorModel):
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

class UpdateIndexRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    DocumentMetadataConfigurationUpdates: Optional[       Sequence[DocumentMetadataConfigurationTypeDef]     ] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None
    UserTokenConfigurations: Optional[Sequence[UserTokenConfigurationTypeDef]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfigurationTypeDef] = None

class WebCrawlerConfigurationTypeDef(BaseValidatorModel):
    Urls: UrlsTypeDef
    CrawlDepth: Optional[int] = None
    MaxLinksPerPage: Optional[int] = None
    MaxContentSizePerPageInMegaBytes: Optional[float] = None
    MaxUrlsPerMinuteCrawlRate: Optional[int] = None
    UrlInclusionPatterns: Optional[Sequence[str]] = None
    UrlExclusionPatterns: Optional[Sequence[str]] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None

class SuggestionValueTypeDef(BaseValidatorModel):
    Text: Optional[SuggestionTextWithHighlightsTypeDef] = None

class TableExcerptTypeDef(BaseValidatorModel):
    Rows: Optional[List[TableRowTypeDef]] = None
    TotalNumberOfRows: Optional[int] = None

class SalesforceConfigurationTypeDef(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[       Sequence[SalesforceStandardObjectConfigurationTypeDef]     ] = None
    KnowledgeArticleConfiguration: Optional[       SalesforceKnowledgeArticleConfigurationTypeDef     ] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfigurationTypeDef] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[       SalesforceStandardObjectAttachmentConfigurationTypeDef     ] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None

class HookConfigurationTypeDef(BaseValidatorModel):
    LambdaArn: str
    S3Bucket: str
    InvocationCondition: Optional[DocumentAttributeConditionTypeDef] = None

class InlineCustomDocumentEnrichmentConfigurationTypeDef(BaseValidatorModel):
    Condition: Optional[DocumentAttributeConditionTypeDef] = None
    Target: Optional[DocumentAttributeTargetTypeDef] = None
    DocumentContentDeletion: Optional[bool] = None

class AttributeFilterTypeDef(BaseValidatorModel):
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

class DocumentInfoTypeDef(BaseValidatorModel):
    DocumentId: str
    Attributes: Optional[Sequence[DocumentAttributeTypeDef]] = None

class DocumentTypeDef(BaseValidatorModel):
    Id: str
    Title: Optional[str] = None
    Blob: Optional[BlobTypeDef] = None
    S3Path: Optional[S3PathTypeDef] = None
    Attributes: Optional[Sequence[DocumentAttributeTypeDef]] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalTypeDef]] = None
    ContentType: Optional[ContentTypeType] = None
    AccessControlConfigurationId: Optional[str] = None

class ExpandedResultItemTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlightsTypeDef] = None
    DocumentExcerpt: Optional[TextWithHighlightsTypeDef] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None

class RetrieveResultItemTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[str] = None
    Content: Optional[str] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None
    ScoreAttributes: Optional[ScoreAttributesTypeDef] = None

class SourceDocumentTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    SuggestionAttributes: Optional[List[str]] = None
    AdditionalAttributes: Optional[List[DocumentAttributeTypeDef]] = None

class GetQuerySuggestionsRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    QueryText: str
    MaxSuggestionsCount: Optional[int] = None
    SuggestionTypes: Optional[Sequence[SuggestionTypeType]] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsGetConfigTypeDef] = None

class AdditionalResultAttributeTypeDef(BaseValidatorModel):
    Key: str
    ValueType: Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
    Value: AdditionalResultAttributeValueTypeDef

class DataSourceConfigurationTypeDef(BaseValidatorModel):
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

class CustomDocumentEnrichmentConfigurationTypeDef(BaseValidatorModel):
    InlineConfigurations: Optional[       Sequence[InlineCustomDocumentEnrichmentConfigurationTypeDef]     ] = None
    PreExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    PostExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    RoleArn: Optional[str] = None

class BatchGetDocumentStatusRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    DocumentInfoList: Sequence[DocumentInfoTypeDef]

class CollapsedResultDetailTypeDef(BaseValidatorModel):
    DocumentAttribute: DocumentAttributeTypeDef
    ExpandedResults: Optional[List[ExpandedResultItemTypeDef]] = None

class RetrieveResultTypeDef(BaseValidatorModel):
    QueryId: str
    ResultItems: List[RetrieveResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SuggestionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Value: Optional[SuggestionValueTypeDef] = None
    SourceDocuments: Optional[List[SourceDocumentTypeDef]] = None

class FeaturedResultsItemTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[QueryResultTypeType] = None
    AdditionalAttributes: Optional[List[AdditionalResultAttributeTypeDef]] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlightsTypeDef] = None
    DocumentExcerpt: Optional[TextWithHighlightsTypeDef] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeTypeDef]] = None
    FeedbackToken: Optional[str] = None

class BatchPutDocumentRequestRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Documents: Sequence[DocumentTypeDef]
    RoleArn: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[       CustomDocumentEnrichmentConfigurationTypeDef     ] = None

class CreateDataSourceRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeDataSourceResponseTypeDef(BaseValidatorModel):
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

class UpdateDataSourceRequestRequestTypeDef(BaseValidatorModel):
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

class QueryResultItemTypeDef(BaseValidatorModel):
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

class GetQuerySuggestionsResponseTypeDef(BaseValidatorModel):
    QuerySuggestionsId: str
    Suggestions: List[SuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryResultTypeDef(BaseValidatorModel):
    QueryId: str
    ResultItems: List[QueryResultItemTypeDef]
    FacetResults: List["FacetResultTypeDef"]
    TotalNumberOfResults: int
    Warnings: List[WarningTypeDef]
    SpellCorrectedQueries: List[SpellCorrectedQueryTypeDef]
    FeaturedResultsItems: List[FeaturedResultsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

