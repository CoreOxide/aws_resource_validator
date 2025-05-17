from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kendra.kendra_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessControlConfigurationSummary(BaseValidatorModel):
    Id: str


class AccessControlListConfiguration(BaseValidatorModel):
    KeyPath: Optional[str] = None


class AclConfiguration(BaseValidatorModel):
    AllowedGroupsColumnName: str


class DataSourceToIndexFieldMapping(BaseValidatorModel):
    DataSourceFieldName: str
    IndexFieldName: str
    DateFieldFormat: Optional[str] = None


class DataSourceVpcConfigurationOutput(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class S3Path(BaseValidatorModel):
    Bucket: str
    Key: str


class DataSourceVpcConfiguration(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class EntityConfiguration(BaseValidatorModel):
    EntityId: str
    EntityType: EntityTypeType


class FailedEntity(BaseValidatorModel):
    EntityId: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EntityPersonaConfiguration(BaseValidatorModel):
    EntityId: str
    Persona: PersonaType


class SuggestableConfig(BaseValidatorModel):
    AttributeName: Optional[str] = None
    Suggestable: Optional[bool] = None


class BasicAuthenticationConfiguration(BaseValidatorModel):
    Host: str
    Port: int
    Credentials: str


class DataSourceSyncJobMetricTarget(BaseValidatorModel):
    DataSourceId: str
    DataSourceSyncJobId: Optional[str] = None


class BatchDeleteDocumentResponseFailedDocument(BaseValidatorModel):
    Id: Optional[str] = None
    DataSourceId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class BatchDeleteFeaturedResultsSetError(BaseValidatorModel):
    Id: str
    ErrorCode: ErrorCodeType
    ErrorMessage: str


# This class is the input for the 'batch_delete_featured_results_set' function.
class BatchDeleteFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetIds: List[str]


class BatchGetDocumentStatusResponseError(BaseValidatorModel):
    DocumentId: Optional[str] = None
    DataSourceId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class Status(BaseValidatorModel):
    DocumentId: Optional[str] = None
    DocumentStatus: Optional[DocumentStatusType] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None


class BatchPutDocumentResponseFailedDocument(BaseValidatorModel):
    Id: Optional[str] = None
    DataSourceId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CapacityUnitsConfiguration(BaseValidatorModel):
    StorageCapacityUnits: int
    QueryCapacityUnits: int


# This class is the input for the 'clear_query_suggestions' function.
class ClearQuerySuggestionsRequest(BaseValidatorModel):
    IndexId: str

Timestamp = Union[datetime, str]


class ExpandConfiguration(BaseValidatorModel):
    MaxResultItemsToExpand: Optional[int] = None
    MaxExpandedResultsPerItem: Optional[int] = None


class SortingConfiguration(BaseValidatorModel):
    DocumentAttributeKey: str
    SortOrder: SortOrderType


class ConfluenceAttachmentToIndexFieldMapping(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluenceAttachmentFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None


class ConfluenceBlogToIndexFieldMapping(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluenceBlogFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None


class ProxyConfiguration(BaseValidatorModel):
    Host: str
    Port: int
    Credentials: Optional[str] = None


class ConfluencePageToIndexFieldMapping(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluencePageFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None


class ConfluenceSpaceToIndexFieldMapping(BaseValidatorModel):
    DataSourceFieldName: Optional[ConfluenceSpaceFieldNameType] = None
    DateFieldFormat: Optional[str] = None
    IndexFieldName: Optional[str] = None


class ConnectionConfiguration(BaseValidatorModel):
    DatabaseHost: str
    DatabasePort: int
    DatabaseName: str
    TableName: str
    SecretArn: str


class ContentSourceConfigurationOutput(BaseValidatorModel):
    DataSourceIds: Optional[List[str]] = None
    FaqIds: Optional[List[str]] = None
    DirectPutContent: Optional[bool] = None


class ContentSourceConfiguration(BaseValidatorModel):
    DataSourceIds: Optional[List[str]] = None
    FaqIds: Optional[List[str]] = None
    DirectPutContent: Optional[bool] = None


class Correction(BaseValidatorModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Term: Optional[str] = None
    CorrectedTerm: Optional[str] = None


class Principal(BaseValidatorModel):
    Name: str
    Type: PrincipalTypeType
    Access: ReadAccessTypeType
    DataSourceId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class FeaturedDocument(BaseValidatorModel):
    Id: Optional[str] = None


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    KmsKeyId: Optional[str] = None


class UserGroupResolutionConfiguration(BaseValidatorModel):
    UserGroupResolutionMode: UserGroupResolutionModeType


class TemplateConfigurationOutput(BaseValidatorModel):
    Template: Optional[Dict[str, Any]] = None


class TemplateConfiguration(BaseValidatorModel):
    Template: Optional[Dict[str, Any]] = None


class DataSourceGroup(BaseValidatorModel):
    GroupId: str
    DataSourceId: str


class DataSourceSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[DataSourceStatusType] = None
    LanguageCode: Optional[str] = None


class DataSourceSyncJobMetrics(BaseValidatorModel):
    DocumentsAdded: Optional[str] = None
    DocumentsModified: Optional[str] = None
    DocumentsDeleted: Optional[str] = None
    DocumentsFailed: Optional[str] = None
    DocumentsScanned: Optional[str] = None


class SqlConfiguration(BaseValidatorModel):
    QueryIdentifiersEnclosingOption: Optional[QueryIdentifiersEnclosingOptionType] = None


class DeleteAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Id: str


# This class is the input for the 'delete_data_source' function.
class DeleteDataSourceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'delete_faq' function.
class DeleteFaqRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'delete_index' function.
class DeleteIndexRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'delete_principal_mapping' function.
class DeletePrincipalMappingRequest(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None


# This class is the input for the 'delete_query_suggestions_block_list' function.
class DeleteQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Id: str


# This class is the input for the 'delete_thesaurus' function.
class DeleteThesaurusRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'describe_access_control_configuration' function.
class DescribeAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Id: str


# This class is the input for the 'describe_data_source' function.
class DescribeDataSourceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'describe_experience' function.
class DescribeExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class ExperienceEndpoint(BaseValidatorModel):
    EndpointType: Optional[Literal['HOME']] = None
    Endpoint: Optional[str] = None


# This class is the input for the 'describe_faq' function.
class DescribeFaqRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'describe_featured_results_set' function.
class DescribeFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str


class FeaturedDocumentMissing(BaseValidatorModel):
    Id: Optional[str] = None


class FeaturedDocumentWithMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    URI: Optional[str] = None


# This class is the input for the 'describe_index' function.
class DescribeIndexRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'describe_principal_mapping' function.
class DescribePrincipalMappingRequest(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None


class GroupOrderingIdSummary(BaseValidatorModel):
    Status: Optional[PrincipalMappingStatusType] = None
    LastUpdatedAt: Optional[datetime] = None
    ReceivedAt: Optional[datetime] = None
    OrderingId: Optional[int] = None
    FailureReason: Optional[str] = None


# This class is the input for the 'describe_query_suggestions_block_list' function.
class DescribeQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Id: str


# This class is the input for the 'describe_query_suggestions_config' function.
class DescribeQuerySuggestionsConfigRequest(BaseValidatorModel):
    IndexId: str


# This class is the input for the 'describe_thesaurus' function.
class DescribeThesaurusRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'disassociate_personas_from_entities' function.
class DisassociatePersonasFromEntitiesRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityIds: List[str]


class DocumentAttributeValueOutput(BaseValidatorModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[List[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[datetime] = None


class RelevanceOutput(BaseValidatorModel):
    Freshness: Optional[bool] = None
    Importance: Optional[int] = None
    Duration: Optional[str] = None
    RankOrder: Optional[OrderType] = None
    ValueImportanceMap: Optional[Dict[str, int]] = None


class Search(BaseValidatorModel):
    Facetable: Optional[bool] = None
    Searchable: Optional[bool] = None
    Displayable: Optional[bool] = None
    Sortable: Optional[bool] = None


class DocumentsMetadataConfiguration(BaseValidatorModel):
    S3Prefix: Optional[str] = None


class EntityDisplayData(BaseValidatorModel):
    UserName: Optional[str] = None
    GroupName: Optional[str] = None
    IdentifiedUserName: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None


class UserIdentityConfiguration(BaseValidatorModel):
    IdentityAttributeName: Optional[str] = None


class Facet(BaseValidatorModel):
    DocumentAttributeKey: Optional[str] = None
    Facets: Optional[List[Dict[str, Any]]] = None
    MaxResults: Optional[int] = None


class FaqStatistics(BaseValidatorModel):
    IndexedQuestionAnswersCount: int


class FaqSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[FaqStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    FileFormat: Optional[FaqFileFormatType] = None
    LanguageCode: Optional[str] = None


class FeaturedResultsSetSummary(BaseValidatorModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None


# This class is the input for the 'get_snapshots' function.
class GetSnapshotsRequest(BaseValidatorModel):
    IndexId: str
    Interval: IntervalType
    MetricType: MetricTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TimeRangeOutput(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class GitHubDocumentCrawlProperties(BaseValidatorModel):
    CrawlRepositoryDocuments: Optional[bool] = None
    CrawlIssue: Optional[bool] = None
    CrawlIssueComment: Optional[bool] = None
    CrawlIssueCommentAttachment: Optional[bool] = None
    CrawlPullRequest: Optional[bool] = None
    CrawlPullRequestComment: Optional[bool] = None
    CrawlPullRequestCommentAttachment: Optional[bool] = None


class SaaSConfiguration(BaseValidatorModel):
    OrganizationName: str
    HostUrl: str


class MemberGroup(BaseValidatorModel):
    GroupId: str
    DataSourceId: Optional[str] = None


class MemberUser(BaseValidatorModel):
    UserId: str


class GroupSummary(BaseValidatorModel):
    GroupId: Optional[str] = None
    OrderingId: Optional[int] = None


class Highlight(BaseValidatorModel):
    BeginOffset: int
    EndOffset: int
    TopAnswer: Optional[bool] = None
    Type: Optional[HighlightTypeType] = None


class IndexConfigurationSummary(BaseValidatorModel):
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: IndexStatusType
    Name: Optional[str] = None
    Id: Optional[str] = None
    Edition: Optional[IndexEditionType] = None


class TextDocumentStatistics(BaseValidatorModel):
    IndexedTextDocumentsCount: int
    IndexedTextBytes: int


class JsonTokenTypeConfiguration(BaseValidatorModel):
    UserNameAttributeField: str
    GroupAttributeField: str


class JwtTokenTypeConfiguration(BaseValidatorModel):
    KeyLocation: KeyLocationType
    URL: Optional[str] = None
    SecretManagerArn: Optional[str] = None
    UserNameAttributeField: Optional[str] = None
    GroupAttributeField: Optional[str] = None
    Issuer: Optional[str] = None
    ClaimRegex: Optional[str] = None


# This class is the input for the 'list_access_control_configurations' function.
class ListAccessControlConfigurationsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_data_sources' function.
class ListDataSourcesRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_entity_personas' function.
class ListEntityPersonasRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PersonasSummary(BaseValidatorModel):
    EntityId: Optional[str] = None
    Persona: Optional[PersonaType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'list_experience_entities' function.
class ListExperienceEntitiesRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_experiences' function.
class ListExperiencesRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_faqs' function.
class ListFaqsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_featured_results_sets' function.
class ListFeaturedResultsSetsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_groups_older_than_ordering_id' function.
class ListGroupsOlderThanOrderingIdRequest(BaseValidatorModel):
    IndexId: str
    OrderingId: int
    DataSourceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_indices' function.
class ListIndicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_query_suggestions_block_lists' function.
class ListQuerySuggestionsBlockListsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QuerySuggestionsBlockListSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[QuerySuggestionsBlockListStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ItemCount: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'list_thesauri' function.
class ListThesauriRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ThesaurusSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ThesaurusStatusType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class SpellCorrectionConfiguration(BaseValidatorModel):
    IncludeQuerySpellCheckSuggestions: bool


class ScoreAttributes(BaseValidatorModel):
    ScoreConfidence: Optional[ScoreConfidenceType] = None


class Warning(BaseValidatorModel):
    Message: Optional[str] = None
    Code: Optional[Literal['QUERY_LANGUAGE_INVALID_SYNTAX']] = None


class RelevanceFeedback(BaseValidatorModel):
    ResultId: str
    RelevanceValue: RelevanceTypeType


class Relevance(BaseValidatorModel):
    Freshness: Optional[bool] = None
    Importance: Optional[int] = None
    Duration: Optional[str] = None
    RankOrder: Optional[OrderType] = None
    ValueImportanceMap: Optional[Dict[str, int]] = None


class SeedUrlConfigurationOutput(BaseValidatorModel):
    SeedUrls: List[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None


class SeedUrlConfiguration(BaseValidatorModel):
    SeedUrls: List[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None


class SiteMapsConfigurationOutput(BaseValidatorModel):
    SiteMaps: List[str]


class SiteMapsConfiguration(BaseValidatorModel):
    SiteMaps: List[str]


# This class is the input for the 'start_data_source_sync_job' function.
class StartDataSourceSyncJobRequest(BaseValidatorModel):
    Id: str
    IndexId: str


# This class is the input for the 'stop_data_source_sync_job' function.
class StopDataSourceSyncJobRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class SuggestionHighlight(BaseValidatorModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


class TableCell(BaseValidatorModel):
    Value: Optional[str] = None
    TopAnswer: Optional[bool] = None
    Highlighted: Optional[bool] = None
    Header: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class ColumnConfigurationOutput(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: List[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class ColumnConfiguration(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: List[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class GoogleDriveConfigurationOutput(BaseValidatorModel):
    SecretArn: str
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    ExcludeMimeTypes: Optional[List[str]] = None
    ExcludeUserAccounts: Optional[List[str]] = None
    ExcludeSharedDrives: Optional[List[str]] = None


class GoogleDriveConfiguration(BaseValidatorModel):
    SecretArn: str
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    ExcludeMimeTypes: Optional[List[str]] = None
    ExcludeUserAccounts: Optional[List[str]] = None
    ExcludeSharedDrives: Optional[List[str]] = None


class SalesforceChatterFeedConfigurationOutput(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    IncludeFilterTypes: Optional[List[SalesforceChatterFeedIncludeFilterTypeType]] = None


class SalesforceChatterFeedConfiguration(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    IncludeFilterTypes: Optional[List[SalesforceChatterFeedIncludeFilterTypeType]] = None


class SalesforceCustomKnowledgeArticleTypeConfigurationOutput(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceCustomKnowledgeArticleTypeConfiguration(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardKnowledgeArticleTypeConfigurationOutput(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardKnowledgeArticleTypeConfiguration(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectAttachmentConfigurationOutput(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectAttachmentConfiguration(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectConfigurationOutput(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectConfiguration(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class ServiceNowKnowledgeArticleConfigurationOutput(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    FilterQuery: Optional[str] = None


class ServiceNowKnowledgeArticleConfiguration(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    FilterQuery: Optional[str] = None


class ServiceNowServiceCatalogConfigurationOutput(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class ServiceNowServiceCatalogConfiguration(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class WorkDocsConfigurationOutput(BaseValidatorModel):
    OrganizationId: str
    CrawlComments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class WorkDocsConfiguration(BaseValidatorModel):
    OrganizationId: str
    CrawlComments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class BoxConfigurationOutput(BaseValidatorModel):
    EnterpriseId: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    CrawlTasks: Optional[bool] = None
    CrawlWebLinks: Optional[bool] = None
    FileFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    TaskFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    CommentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    WebLinkFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None


class FsxConfigurationOutput(BaseValidatorModel):
    FileSystemId: str
    FileSystemType: Literal['WINDOWS']
    VpcConfiguration: DataSourceVpcConfigurationOutput
    SecretArn: Optional[str] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class JiraConfigurationOutput(BaseValidatorModel):
    JiraAccountUrl: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    Project: Optional[List[str]] = None
    IssueType: Optional[List[str]] = None
    Status: Optional[List[str]] = None
    IssueSubEntityFilter: Optional[List[IssueSubEntityType]] = None
    AttachmentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    CommentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    IssueFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    ProjectFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    WorkLogFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None


class QuipConfigurationOutput(BaseValidatorModel):
    Domain: str
    SecretArn: str
    CrawlFileComments: Optional[bool] = None
    CrawlChatRooms: Optional[bool] = None
    CrawlAttachments: Optional[bool] = None
    FolderIds: Optional[List[str]] = None
    ThreadFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    MessageFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    AttachmentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None


class SlackConfigurationOutput(BaseValidatorModel):
    TeamId: str
    SecretArn: str
    SlackEntityList: List[SlackEntityType]
    SinceCrawlDate: str
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None
    UseChangeLog: Optional[bool] = None
    CrawlBotMessage: Optional[bool] = None
    ExcludeArchived: Optional[bool] = None
    LookBackPeriod: Optional[int] = None
    PrivateChannelFilter: Optional[List[str]] = None
    PublicChannelFilter: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class AlfrescoConfigurationOutput(BaseValidatorModel):
    SiteUrl: str
    SiteId: str
    SecretArn: str
    SslCertificateS3Path: S3Path
    CrawlSystemFolders: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    EntityFilter: Optional[List[AlfrescoEntityType]] = None
    DocumentLibraryFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    BlogFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    WikiFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None


class OnPremiseConfiguration(BaseValidatorModel):
    HostUrl: str
    OrganizationName: str
    SslCertificateS3Path: S3Path


class OneDriveUsersOutput(BaseValidatorModel):
    OneDriveUserList: Optional[List[str]] = None
    OneDriveUserS3Path: Optional[S3Path] = None


class OneDriveUsers(BaseValidatorModel):
    OneDriveUserList: Optional[List[str]] = None
    OneDriveUserS3Path: Optional[S3Path] = None


# This class is the input for the 'update_query_suggestions_block_list' function.
class UpdateQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SourceS3Path: Optional[S3Path] = None
    RoleArn: Optional[str] = None


# This class is the input for the 'update_thesaurus' function.
class UpdateThesaurusRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    SourceS3Path: Optional[S3Path] = None


class AlfrescoConfiguration(BaseValidatorModel):
    SiteUrl: str
    SiteId: str
    SecretArn: str
    SslCertificateS3Path: S3Path
    CrawlSystemFolders: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    EntityFilter: Optional[List[AlfrescoEntityType]] = None
    DocumentLibraryFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    BlogFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    WikiFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class BoxConfiguration(BaseValidatorModel):
    EnterpriseId: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    CrawlTasks: Optional[bool] = None
    CrawlWebLinks: Optional[bool] = None
    FileFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    TaskFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    CommentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    WebLinkFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None

DataSourceVpcConfigurationUnion = Union[DataSourceVpcConfiguration, DataSourceVpcConfigurationOutput]


class FsxConfiguration(BaseValidatorModel):
    FileSystemId: str
    FileSystemType: Literal['WINDOWS']
    VpcConfiguration: DataSourceVpcConfiguration
    SecretArn: Optional[str] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class JiraConfiguration(BaseValidatorModel):
    JiraAccountUrl: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    Project: Optional[List[str]] = None
    IssueType: Optional[List[str]] = None
    Status: Optional[List[str]] = None
    IssueSubEntityFilter: Optional[List[IssueSubEntityType]] = None
    AttachmentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    CommentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    IssueFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    ProjectFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    WorkLogFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class QuipConfiguration(BaseValidatorModel):
    Domain: str
    SecretArn: str
    CrawlFileComments: Optional[bool] = None
    CrawlChatRooms: Optional[bool] = None
    CrawlAttachments: Optional[bool] = None
    FolderIds: Optional[List[str]] = None
    ThreadFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    MessageFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    AttachmentFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class SlackConfiguration(BaseValidatorModel):
    TeamId: str
    SecretArn: str
    SlackEntityList: List[SlackEntityType]
    SinceCrawlDate: str
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    UseChangeLog: Optional[bool] = None
    CrawlBotMessage: Optional[bool] = None
    ExcludeArchived: Optional[bool] = None
    LookBackPeriod: Optional[int] = None
    PrivateChannelFilter: Optional[List[str]] = None
    PublicChannelFilter: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


# This class is the input for the 'associate_entities_to_experience' function.
class AssociateEntitiesToExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: List[EntityConfiguration]


# This class is the input for the 'disassociate_entities_from_experience' function.
class DisassociateEntitiesFromExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: List[EntityConfiguration]


# This class is the output for the 'associate_entities_to_experience' function.
class AssociateEntitiesToExperienceResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_personas_to_entities' function.
class AssociatePersonasToEntitiesResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_access_control_configuration' function.
class CreateAccessControlConfigurationResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_source' function.
class CreateDataSourceResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_experience' function.
class CreateExperienceResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_faq' function.
class CreateFaqResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_index' function.
class CreateIndexResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_query_suggestions_block_list' function.
class CreateQuerySuggestionsBlockListResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_thesaurus' function.
class CreateThesaurusResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_faq' function.
class DescribeFaqResponse(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: str
    Description: str
    CreatedAt: datetime
    UpdatedAt: datetime
    S3Path: S3Path
    Status: FaqStatusType
    RoleArn: str
    ErrorMessage: str
    FileFormat: FaqFileFormatType
    LanguageCode: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_query_suggestions_block_list' function.
class DescribeQuerySuggestionsBlockListResponse(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: str
    Description: str
    Status: QuerySuggestionsBlockListStatusType
    ErrorMessage: str
    CreatedAt: datetime
    UpdatedAt: datetime
    SourceS3Path: S3Path
    ItemCount: int
    FileSizeBytes: int
    RoleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_thesaurus' function.
class DescribeThesaurusResponse(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: str
    Description: str
    Status: ThesaurusStatusType
    ErrorMessage: str
    CreatedAt: datetime
    UpdatedAt: datetime
    RoleArn: str
    SourceS3Path: S3Path
    FileSizeBytes: int
    TermCount: int
    SynonymRuleCount: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_entities_from_experience' function.
class DisassociateEntitiesFromExperienceResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_personas_from_entities' function.
class DisassociatePersonasFromEntitiesResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_thesaurus' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_access_control_configurations' function.
class ListAccessControlConfigurationsResponse(BaseValidatorModel):
    AccessControlConfigurations: List[AccessControlConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_data_source_sync_job' function.
class StartDataSourceSyncJobResponse(BaseValidatorModel):
    ExecutionId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_personas_to_entities' function.
class AssociatePersonasToEntitiesRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    Personas: List[EntityPersonaConfiguration]


class AttributeSuggestionsDescribeConfig(BaseValidatorModel):
    SuggestableConfigList: Optional[List[SuggestableConfig]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None


class AttributeSuggestionsUpdateConfig(BaseValidatorModel):
    SuggestableConfigList: Optional[List[SuggestableConfig]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None


class AuthenticationConfigurationOutput(BaseValidatorModel):
    BasicAuthentication: Optional[List[BasicAuthenticationConfiguration]] = None


class AuthenticationConfiguration(BaseValidatorModel):
    BasicAuthentication: Optional[List[BasicAuthenticationConfiguration]] = None


# This class is the input for the 'batch_delete_document' function.
class BatchDeleteDocumentRequest(BaseValidatorModel):
    IndexId: str
    DocumentIdList: List[str]
    DataSourceSyncJobMetricTarget: Optional[DataSourceSyncJobMetricTarget] = None


# This class is the output for the 'batch_delete_document' function.
class BatchDeleteDocumentResponse(BaseValidatorModel):
    FailedDocuments: List[BatchDeleteDocumentResponseFailedDocument]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_featured_results_set' function.
class BatchDeleteFeaturedResultsSetResponse(BaseValidatorModel):
    Errors: List[BatchDeleteFeaturedResultsSetError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_document_status' function.
class BatchGetDocumentStatusResponse(BaseValidatorModel):
    Errors: List[BatchGetDocumentStatusResponseError]
    DocumentStatusList: List[Status]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_put_document' function.
class BatchPutDocumentResponse(BaseValidatorModel):
    FailedDocuments: List[BatchPutDocumentResponseFailedDocument]
    ResponseMetadata: ResponseMetadata


class ClickFeedback(BaseValidatorModel):
    ResultId: str
    ClickTime: Timestamp


class DocumentAttributeValue(BaseValidatorModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[List[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[Timestamp] = None


class TimeRange(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class CollapseConfiguration(BaseValidatorModel):
    DocumentAttributeKey: str
    SortingConfigurations: Optional[List[SortingConfiguration]] = None
    MissingAttributeKeyStrategy: Optional[MissingAttributeKeyStrategyType] = None
    Expand: Optional[bool] = None
    ExpandConfiguration: Optional[ExpandConfiguration] = None


class ConfluenceAttachmentConfigurationOutput(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[List[ConfluenceAttachmentToIndexFieldMapping]] = None


class ConfluenceAttachmentConfiguration(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[List[ConfluenceAttachmentToIndexFieldMapping]] = None


class ConfluenceBlogConfigurationOutput(BaseValidatorModel):
    BlogFieldMappings: Optional[List[ConfluenceBlogToIndexFieldMapping]] = None


class ConfluenceBlogConfiguration(BaseValidatorModel):
    BlogFieldMappings: Optional[List[ConfluenceBlogToIndexFieldMapping]] = None


class SharePointConfigurationOutput(BaseValidatorModel):
    SharePointVersion: SharePointVersionType
    Urls: List[str]
    SecretArn: str
    CrawlAttachments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    DocumentTitleFieldName: Optional[str] = None
    DisableLocalGroups: Optional[bool] = None
    SslCertificateS3Path: Optional[S3Path] = None
    AuthenticationType: Optional[SharePointOnlineAuthenticationTypeType] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None


class SharePointConfiguration(BaseValidatorModel):
    SharePointVersion: SharePointVersionType
    Urls: List[str]
    SecretArn: str
    CrawlAttachments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    DocumentTitleFieldName: Optional[str] = None
    DisableLocalGroups: Optional[bool] = None
    SslCertificateS3Path: Optional[S3Path] = None
    AuthenticationType: Optional[SharePointOnlineAuthenticationTypeType] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None


class ConfluencePageConfigurationOutput(BaseValidatorModel):
    PageFieldMappings: Optional[List[ConfluencePageToIndexFieldMapping]] = None


class ConfluencePageConfiguration(BaseValidatorModel):
    PageFieldMappings: Optional[List[ConfluencePageToIndexFieldMapping]] = None


class ConfluenceSpaceConfigurationOutput(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[List[str]] = None
    ExcludeSpaces: Optional[List[str]] = None
    SpaceFieldMappings: Optional[List[ConfluenceSpaceToIndexFieldMapping]] = None


class ConfluenceSpaceConfiguration(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[List[str]] = None
    ExcludeSpaces: Optional[List[str]] = None
    SpaceFieldMappings: Optional[List[ConfluenceSpaceToIndexFieldMapping]] = None


class SpellCorrectedQuery(BaseValidatorModel):
    SuggestedQueryText: Optional[str] = None
    Corrections: Optional[List[Correction]] = None


class HierarchicalPrincipalOutput(BaseValidatorModel):
    PrincipalList: List[Principal]


class HierarchicalPrincipal(BaseValidatorModel):
    PrincipalList: List[Principal]


# This class is the input for the 'create_faq' function.
class CreateFaqRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    S3Path: S3Path
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    FileFormat: Optional[FaqFileFormatType] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None


# This class is the input for the 'create_query_suggestions_block_list' function.
class CreateQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    SourceS3Path: S3Path
    RoleArn: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_thesaurus' function.
class CreateThesaurusRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    RoleArn: str
    SourceS3Path: S3Path
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the input for the 'create_featured_results_set' function.
class CreateFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetName: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[List[str]] = None
    FeaturedDocuments: Optional[List[FeaturedDocument]] = None
    Tags: Optional[List[Tag]] = None


class FeaturedResultsSet(BaseValidatorModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[List[str]] = None
    FeaturedDocuments: Optional[List[FeaturedDocument]] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None


# This class is the input for the 'update_featured_results_set' function.
class UpdateFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[List[str]] = None
    FeaturedDocuments: Optional[List[FeaturedDocument]] = None


class UserContext(BaseValidatorModel):
    Token: Optional[str] = None
    UserId: Optional[str] = None
    Groups: Optional[List[str]] = None
    DataSourceGroups: Optional[List[DataSourceGroup]] = None


# This class is the output for the 'list_data_sources' function.
class ListDataSourcesResponse(BaseValidatorModel):
    SummaryItems: List[DataSourceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DataSourceSyncJob(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[DataSourceSyncJobStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    DataSourceErrorCode: Optional[str] = None
    Metrics: Optional[DataSourceSyncJobMetrics] = None


class ExperiencesSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Status: Optional[ExperienceStatusType] = None
    Endpoints: Optional[List[ExperienceEndpoint]] = None


# This class is the output for the 'describe_featured_results_set' function.
class DescribeFeaturedResultsSetResponse(BaseValidatorModel):
    FeaturedResultsSetId: str
    FeaturedResultsSetName: str
    Description: str
    Status: FeaturedResultsSetStatusType
    QueryTexts: List[str]
    FeaturedDocumentsWithMetadata: List[FeaturedDocumentWithMetadata]
    FeaturedDocumentsMissing: List[FeaturedDocumentMissing]
    LastUpdatedTimestamp: int
    CreationTimestamp: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_principal_mapping' function.
class DescribePrincipalMappingResponse(BaseValidatorModel):
    IndexId: str
    DataSourceId: str
    GroupId: str
    GroupOrderingIdSummaries: List[GroupOrderingIdSummary]
    ResponseMetadata: ResponseMetadata


class DocumentAttributeConditionOutput(BaseValidatorModel):
    ConditionDocumentAttributeKey: str
    Operator: ConditionOperatorType
    ConditionOnValue: Optional[DocumentAttributeValueOutput] = None


class DocumentAttributeOutput(BaseValidatorModel):
    Key: str
    Value: DocumentAttributeValueOutput


class DocumentAttributeTargetOutput(BaseValidatorModel):
    TargetDocumentAttributeKey: Optional[str] = None
    TargetDocumentAttributeValueDeletion: Optional[bool] = None
    TargetDocumentAttributeValue: Optional[DocumentAttributeValueOutput] = None


class DocumentAttributeValueCountPair(BaseValidatorModel):
    DocumentAttributeValue: Optional[DocumentAttributeValueOutput] = None
    Count: Optional[int] = None
    FacetResults: Optional[List[Dict[str, Any]]] = None


class DocumentMetadataConfigurationOutput(BaseValidatorModel):
    Name: str
    Type: DocumentAttributeValueTypeType
    Relevance: Optional[RelevanceOutput] = None
    Search: Optional[Search] = None


class S3DataSourceConfigurationOutput(BaseValidatorModel):
    BucketName: str
    InclusionPrefixes: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    DocumentsMetadataConfiguration: Optional[DocumentsMetadataConfiguration] = None
    AccessControlListConfiguration: Optional[AccessControlListConfiguration] = None


class S3DataSourceConfiguration(BaseValidatorModel):
    BucketName: str
    InclusionPrefixes: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    DocumentsMetadataConfiguration: Optional[DocumentsMetadataConfiguration] = None
    AccessControlListConfiguration: Optional[AccessControlListConfiguration] = None


class ExperienceEntitiesSummary(BaseValidatorModel):
    EntityId: Optional[str] = None
    EntityType: Optional[EntityTypeType] = None
    DisplayData: Optional[EntityDisplayData] = None


class ExperienceConfigurationOutput(BaseValidatorModel):
    ContentSourceConfiguration: Optional[ContentSourceConfigurationOutput] = None
    UserIdentityConfiguration: Optional[UserIdentityConfiguration] = None


class ExperienceConfiguration(BaseValidatorModel):
    ContentSourceConfiguration: Optional[ContentSourceConfiguration] = None
    UserIdentityConfiguration: Optional[UserIdentityConfiguration] = None


# This class is the output for the 'list_faqs' function.
class ListFaqsResponse(BaseValidatorModel):
    FaqSummaryItems: List[FaqSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_featured_results_sets' function.
class ListFeaturedResultsSetsResponse(BaseValidatorModel):
    FeaturedResultsSetSummaryItems: List[FeaturedResultsSetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_snapshots' function.
class GetSnapshotsResponse(BaseValidatorModel):
    SnapShotTimeFilter: TimeRangeOutput
    SnapshotsDataHeader: List[str]
    SnapshotsData: List[List[str]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GroupMembers(BaseValidatorModel):
    MemberGroups: Optional[List[MemberGroup]] = None
    MemberUsers: Optional[List[MemberUser]] = None
    S3PathforGroupMembers: Optional[S3Path] = None


# This class is the output for the 'list_groups_older_than_ordering_id' function.
class ListGroupsOlderThanOrderingIdResponse(BaseValidatorModel):
    GroupsSummaries: List[GroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TextWithHighlights(BaseValidatorModel):
    Text: Optional[str] = None
    Highlights: Optional[List[Highlight]] = None


# This class is the output for the 'list_indices' function.
class ListIndicesResponse(BaseValidatorModel):
    IndexConfigurationSummaryItems: List[IndexConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IndexStatistics(BaseValidatorModel):
    FaqStatistics: FaqStatistics
    TextDocumentStatistics: TextDocumentStatistics


class UserTokenConfiguration(BaseValidatorModel):
    JwtTokenTypeConfiguration: Optional[JwtTokenTypeConfiguration] = None
    JsonTokenTypeConfiguration: Optional[JsonTokenTypeConfiguration] = None


# This class is the output for the 'list_entity_personas' function.
class ListEntityPersonasResponse(BaseValidatorModel):
    SummaryItems: List[PersonasSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_query_suggestions_block_lists' function.
class ListQuerySuggestionsBlockListsResponse(BaseValidatorModel):
    BlockListSummaryItems: List[QuerySuggestionsBlockListSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_thesauri' function.
class ListThesauriResponse(BaseValidatorModel):
    ThesaurusSummaryItems: List[ThesaurusSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

RelevanceUnion = Union[Relevance, RelevanceOutput]


class UrlsOutput(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfigurationOutput] = None
    SiteMapsConfiguration: Optional[SiteMapsConfigurationOutput] = None


class Urls(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfiguration] = None
    SiteMapsConfiguration: Optional[SiteMapsConfiguration] = None


class SuggestionTextWithHighlights(BaseValidatorModel):
    Text: Optional[str] = None
    Highlights: Optional[List[SuggestionHighlight]] = None


class TableRow(BaseValidatorModel):
    Cells: Optional[List[TableCell]] = None


class DatabaseConfigurationOutput(BaseValidatorModel):
    DatabaseEngineType: DatabaseEngineTypeType
    ConnectionConfiguration: ConnectionConfiguration
    ColumnConfiguration: ColumnConfigurationOutput
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None
    AclConfiguration: Optional[AclConfiguration] = None
    SqlConfiguration: Optional[SqlConfiguration] = None


class DatabaseConfiguration(BaseValidatorModel):
    DatabaseEngineType: DatabaseEngineTypeType
    ConnectionConfiguration: ConnectionConfiguration
    ColumnConfiguration: ColumnConfiguration
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    AclConfiguration: Optional[AclConfiguration] = None
    SqlConfiguration: Optional[SqlConfiguration] = None


class SalesforceKnowledgeArticleConfigurationOutput(BaseValidatorModel):
    IncludedStates: List[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[SalesforceStandardKnowledgeArticleTypeConfigurationOutput] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[List[SalesforceCustomKnowledgeArticleTypeConfigurationOutput]] = None


class SalesforceKnowledgeArticleConfiguration(BaseValidatorModel):
    IncludedStates: List[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[SalesforceStandardKnowledgeArticleTypeConfiguration] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[List[SalesforceCustomKnowledgeArticleTypeConfiguration]] = None


class ServiceNowConfigurationOutput(BaseValidatorModel):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionTypeType
    KnowledgeArticleConfiguration: Optional[ServiceNowKnowledgeArticleConfigurationOutput] = None
    ServiceCatalogConfiguration: Optional[ServiceNowServiceCatalogConfigurationOutput] = None
    AuthenticationType: Optional[ServiceNowAuthenticationTypeType] = None


class ServiceNowConfiguration(BaseValidatorModel):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionTypeType
    KnowledgeArticleConfiguration: Optional[ServiceNowKnowledgeArticleConfiguration] = None
    ServiceCatalogConfiguration: Optional[ServiceNowServiceCatalogConfiguration] = None
    AuthenticationType: Optional[ServiceNowAuthenticationTypeType] = None


class GitHubConfigurationOutput(BaseValidatorModel):
    SecretArn: str
    SaaSConfiguration: Optional[SaaSConfiguration] = None
    OnPremiseConfiguration: Optional[OnPremiseConfiguration] = None
    Type: Optional[TypeType] = None
    UseChangeLog: Optional[bool] = None
    GitHubDocumentCrawlProperties: Optional[GitHubDocumentCrawlProperties] = None
    RepositoryFilter: Optional[List[str]] = None
    InclusionFolderNamePatterns: Optional[List[str]] = None
    InclusionFileTypePatterns: Optional[List[str]] = None
    InclusionFileNamePatterns: Optional[List[str]] = None
    ExclusionFolderNamePatterns: Optional[List[str]] = None
    ExclusionFileTypePatterns: Optional[List[str]] = None
    ExclusionFileNamePatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None
    GitHubRepositoryConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubCommitConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubIssueDocumentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubIssueCommentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubIssueAttachmentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubPullRequestCommentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubPullRequestDocumentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubPullRequestDocumentAttachmentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class GitHubConfiguration(BaseValidatorModel):
    SecretArn: str
    SaaSConfiguration: Optional[SaaSConfiguration] = None
    OnPremiseConfiguration: Optional[OnPremiseConfiguration] = None
    Type: Optional[TypeType] = None
    UseChangeLog: Optional[bool] = None
    GitHubDocumentCrawlProperties: Optional[GitHubDocumentCrawlProperties] = None
    RepositoryFilter: Optional[List[str]] = None
    InclusionFolderNamePatterns: Optional[List[str]] = None
    InclusionFileTypePatterns: Optional[List[str]] = None
    InclusionFileNamePatterns: Optional[List[str]] = None
    ExclusionFolderNamePatterns: Optional[List[str]] = None
    ExclusionFileTypePatterns: Optional[List[str]] = None
    ExclusionFileNamePatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    GitHubRepositoryConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubCommitConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubIssueDocumentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubIssueCommentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubIssueAttachmentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubPullRequestCommentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubPullRequestDocumentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    GitHubPullRequestDocumentAttachmentConfigurationFieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class OneDriveConfigurationOutput(BaseValidatorModel):
    TenantDomain: str
    SecretArn: str
    OneDriveUsers: OneDriveUsersOutput
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    DisableLocalGroups: Optional[bool] = None


class OneDriveConfiguration(BaseValidatorModel):
    TenantDomain: str
    SecretArn: str
    OneDriveUsers: OneDriveUsers
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    DisableLocalGroups: Optional[bool] = None


# This class is the output for the 'describe_query_suggestions_config' function.
class DescribeQuerySuggestionsConfigResponse(BaseValidatorModel):
    Mode: ModeType
    Status: QuerySuggestionsStatusType
    QueryLogLookBackWindowInDays: int
    IncludeQueriesWithoutUserInformation: bool
    MinimumNumberOfQueryingUsers: int
    MinimumQueryCount: int
    LastSuggestionsBuildTime: datetime
    LastClearTime: datetime
    TotalSuggestionsCount: int
    AttributeSuggestionsConfig: AttributeSuggestionsDescribeConfig
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_query_suggestions_config' function.
class UpdateQuerySuggestionsConfigRequest(BaseValidatorModel):
    IndexId: str
    Mode: Optional[ModeType] = None
    QueryLogLookBackWindowInDays: Optional[int] = None
    IncludeQueriesWithoutUserInformation: Optional[bool] = None
    MinimumNumberOfQueryingUsers: Optional[int] = None
    MinimumQueryCount: Optional[int] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsUpdateConfig] = None


# This class is the input for the 'submit_feedback' function.
class SubmitFeedbackRequest(BaseValidatorModel):
    IndexId: str
    QueryId: str
    ClickFeedbackItems: Optional[List[ClickFeedback]] = None
    RelevanceFeedbackItems: Optional[List[RelevanceFeedback]] = None


class DocumentAttributeCondition(BaseValidatorModel):
    ConditionDocumentAttributeKey: str
    Operator: ConditionOperatorType
    ConditionOnValue: Optional[DocumentAttributeValue] = None


class DocumentAttributeTarget(BaseValidatorModel):
    TargetDocumentAttributeKey: Optional[str] = None
    TargetDocumentAttributeValueDeletion: Optional[bool] = None
    TargetDocumentAttributeValue: Optional[DocumentAttributeValue] = None

DocumentAttributeValueUnion = Union[DocumentAttributeValue, DocumentAttributeValueOutput]

TimeRangeUnion = Union[TimeRange, TimeRangeOutput]


class ConfluenceConfigurationOutput(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    Version: ConfluenceVersionType
    SpaceConfiguration: Optional[ConfluenceSpaceConfigurationOutput] = None
    PageConfiguration: Optional[ConfluencePageConfigurationOutput] = None
    BlogConfiguration: Optional[ConfluenceBlogConfigurationOutput] = None
    AttachmentConfiguration: Optional[ConfluenceAttachmentConfigurationOutput] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutput] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None
    AuthenticationType: Optional[ConfluenceAuthenticationTypeType] = None


class ConfluenceConfiguration(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    Version: ConfluenceVersionType
    SpaceConfiguration: Optional[ConfluenceSpaceConfiguration] = None
    PageConfiguration: Optional[ConfluencePageConfiguration] = None
    BlogConfiguration: Optional[ConfluenceBlogConfiguration] = None
    AttachmentConfiguration: Optional[ConfluenceAttachmentConfiguration] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None
    AuthenticationType: Optional[ConfluenceAuthenticationTypeType] = None


# This class is the output for the 'describe_access_control_configuration' function.
class DescribeAccessControlConfigurationResponse(BaseValidatorModel):
    Name: str
    Description: str
    ErrorMessage: str
    AccessControlList: List[Principal]
    HierarchicalAccessControlList: List[HierarchicalPrincipalOutput]
    ResponseMetadata: ResponseMetadata

HierarchicalPrincipalUnion = Union[HierarchicalPrincipal, HierarchicalPrincipalOutput]


# This class is the output for the 'create_featured_results_set' function.
class CreateFeaturedResultsSetResponse(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_featured_results_set' function.
class UpdateFeaturedResultsSetResponse(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_source_sync_jobs' function.
class ListDataSourceSyncJobsResponse(BaseValidatorModel):
    History: List[DataSourceSyncJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_experiences' function.
class ListExperiencesResponse(BaseValidatorModel):
    SummaryItems: List[ExperiencesSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HookConfigurationOutput(BaseValidatorModel):
    LambdaArn: str
    S3Bucket: str
    InvocationCondition: Optional[DocumentAttributeConditionOutput] = None


class RetrieveResultItem(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[str] = None
    Content: Optional[str] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutput]] = None
    ScoreAttributes: Optional[ScoreAttributes] = None


class SourceDocument(BaseValidatorModel):
    DocumentId: Optional[str] = None
    SuggestionAttributes: Optional[List[str]] = None
    AdditionalAttributes: Optional[List[DocumentAttributeOutput]] = None


class InlineCustomDocumentEnrichmentConfigurationOutput(BaseValidatorModel):
    Condition: Optional[DocumentAttributeConditionOutput] = None
    Target: Optional[DocumentAttributeTargetOutput] = None
    DocumentContentDeletion: Optional[bool] = None


class FacetResult(BaseValidatorModel):
    DocumentAttributeKey: Optional[str] = None
    DocumentAttributeValueType: Optional[DocumentAttributeValueTypeType] = None
    DocumentAttributeValueCountPairs: Optional[List[DocumentAttributeValueCountPair]] = None


# This class is the output for the 'list_experience_entities' function.
class ListExperienceEntitiesResponse(BaseValidatorModel):
    SummaryItems: List[ExperienceEntitiesSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_experience' function.
class DescribeExperienceResponse(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: str
    Endpoints: List[ExperienceEndpoint]
    Configuration: ExperienceConfigurationOutput
    CreatedAt: datetime
    UpdatedAt: datetime
    Description: str
    Status: ExperienceStatusType
    RoleArn: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadata

ExperienceConfigurationUnion = Union[ExperienceConfiguration, ExperienceConfigurationOutput]


# This class is the input for the 'put_principal_mapping' function.
class PutPrincipalMappingRequest(BaseValidatorModel):
    IndexId: str
    GroupId: str
    GroupMembers: GroupMembers
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None
    RoleArn: Optional[str] = None


class AdditionalResultAttributeValue(BaseValidatorModel):
    TextWithHighlightsValue: Optional[TextWithHighlights] = None


class ExpandedResultItem(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlights] = None
    DocumentExcerpt: Optional[TextWithHighlights] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutput]] = None


# This class is the input for the 'create_index' function.
class CreateIndexRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    Edition: Optional[IndexEditionType] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    UserTokenConfigurations: Optional[List[UserTokenConfiguration]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfiguration] = None


# This class is the output for the 'describe_index' function.
class DescribeIndexResponse(BaseValidatorModel):
    Name: str
    Id: str
    Edition: IndexEditionType
    RoleArn: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfiguration
    Status: IndexStatusType
    Description: str
    CreatedAt: datetime
    UpdatedAt: datetime
    DocumentMetadataConfigurations: List[DocumentMetadataConfigurationOutput]
    IndexStatistics: IndexStatistics
    ErrorMessage: str
    CapacityUnits: CapacityUnitsConfiguration
    UserTokenConfigurations: List[UserTokenConfiguration]
    UserContextPolicy: UserContextPolicyType
    UserGroupResolutionConfiguration: UserGroupResolutionConfiguration
    ResponseMetadata: ResponseMetadata


class DocumentMetadataConfiguration(BaseValidatorModel):
    Name: str
    Type: DocumentAttributeValueTypeType
    Relevance: Optional[RelevanceUnion] = None
    Search: Optional[Search] = None


class DocumentRelevanceConfiguration(BaseValidatorModel):
    Name: str
    Relevance: RelevanceUnion


class WebCrawlerConfigurationOutput(BaseValidatorModel):
    Urls: UrlsOutput
    CrawlDepth: Optional[int] = None
    MaxLinksPerPage: Optional[int] = None
    MaxContentSizePerPageInMegaBytes: Optional[float] = None
    MaxUrlsPerMinuteCrawlRate: Optional[int] = None
    UrlInclusionPatterns: Optional[List[str]] = None
    UrlExclusionPatterns: Optional[List[str]] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationOutput] = None


class WebCrawlerConfiguration(BaseValidatorModel):
    Urls: Urls
    CrawlDepth: Optional[int] = None
    MaxLinksPerPage: Optional[int] = None
    MaxContentSizePerPageInMegaBytes: Optional[float] = None
    MaxUrlsPerMinuteCrawlRate: Optional[int] = None
    UrlInclusionPatterns: Optional[List[str]] = None
    UrlExclusionPatterns: Optional[List[str]] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None
    AuthenticationConfiguration: Optional[AuthenticationConfiguration] = None


class SuggestionValue(BaseValidatorModel):
    Text: Optional[SuggestionTextWithHighlights] = None


class TableExcerpt(BaseValidatorModel):
    Rows: Optional[List[TableRow]] = None
    TotalNumberOfRows: Optional[int] = None


class SalesforceConfigurationOutput(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[List[SalesforceStandardObjectConfigurationOutput]] = None
    KnowledgeArticleConfiguration: Optional[SalesforceKnowledgeArticleConfigurationOutput] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfigurationOutput] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[SalesforceStandardObjectAttachmentConfigurationOutput] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None


class SalesforceConfiguration(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[List[SalesforceStandardObjectConfiguration]] = None
    KnowledgeArticleConfiguration: Optional[SalesforceKnowledgeArticleConfiguration] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfiguration] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[SalesforceStandardObjectAttachmentConfiguration] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None


class HookConfiguration(BaseValidatorModel):
    LambdaArn: str
    S3Bucket: str
    InvocationCondition: Optional[DocumentAttributeCondition] = None


class InlineCustomDocumentEnrichmentConfiguration(BaseValidatorModel):
    Condition: Optional[DocumentAttributeCondition] = None
    Target: Optional[DocumentAttributeTarget] = None
    DocumentContentDeletion: Optional[bool] = None


class DocumentAttribute(BaseValidatorModel):
    Key: str
    Value: DocumentAttributeValueUnion


# This class is the input for the 'list_data_source_sync_jobs' function.
class ListDataSourceSyncJobsRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeFilter: Optional[TimeRangeUnion] = None
    StatusFilter: Optional[DataSourceSyncJobStatusType] = None


# This class is the input for the 'create_access_control_configuration' function.
class CreateAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    Description: Optional[str] = None
    AccessControlList: Optional[List[Principal]] = None
    HierarchicalAccessControlList: Optional[List[HierarchicalPrincipalUnion]] = None
    ClientToken: Optional[str] = None


class UpdateAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AccessControlList: Optional[List[Principal]] = None
    HierarchicalAccessControlList: Optional[List[HierarchicalPrincipalUnion]] = None


# This class is the output for the 'retrieve' function.
class RetrieveResult(BaseValidatorModel):
    QueryId: str
    ResultItems: List[RetrieveResultItem]
    ResponseMetadata: ResponseMetadata


class CustomDocumentEnrichmentConfigurationOutput(BaseValidatorModel):
    InlineConfigurations: Optional[List[InlineCustomDocumentEnrichmentConfigurationOutput]] = None
    PreExtractionHookConfiguration: Optional[HookConfigurationOutput] = None
    PostExtractionHookConfiguration: Optional[HookConfigurationOutput] = None
    RoleArn: Optional[str] = None


# This class is the input for the 'create_experience' function.
class CreateExperienceRequest(BaseValidatorModel):
    Name: str
    IndexId: str
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationUnion] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_experience' function.
class UpdateExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationUnion] = None
    Description: Optional[str] = None


class AdditionalResultAttribute(BaseValidatorModel):
    Key: str
    ValueType: Literal['TEXT_WITH_HIGHLIGHTS_VALUE']
    Value: AdditionalResultAttributeValue


class CollapsedResultDetail(BaseValidatorModel):
    DocumentAttribute: DocumentAttributeOutput
    ExpandedResults: Optional[List[ExpandedResultItem]] = None

DocumentMetadataConfigurationUnion = Union[DocumentMetadataConfiguration, DocumentMetadataConfigurationOutput]


class Suggestion(BaseValidatorModel):
    Id: Optional[str] = None
    Value: Optional[SuggestionValue] = None
    SourceDocuments: Optional[List[SourceDocument]] = None


class DataSourceConfigurationOutput(BaseValidatorModel):
    S3Configuration: Optional[S3DataSourceConfigurationOutput] = None
    SharePointConfiguration: Optional[SharePointConfigurationOutput] = None
    DatabaseConfiguration: Optional[DatabaseConfigurationOutput] = None
    SalesforceConfiguration: Optional[SalesforceConfigurationOutput] = None
    OneDriveConfiguration: Optional[OneDriveConfigurationOutput] = None
    ServiceNowConfiguration: Optional[ServiceNowConfigurationOutput] = None
    ConfluenceConfiguration: Optional[ConfluenceConfigurationOutput] = None
    GoogleDriveConfiguration: Optional[GoogleDriveConfigurationOutput] = None
    WebCrawlerConfiguration: Optional[WebCrawlerConfigurationOutput] = None
    WorkDocsConfiguration: Optional[WorkDocsConfigurationOutput] = None
    FsxConfiguration: Optional[FsxConfigurationOutput] = None
    SlackConfiguration: Optional[SlackConfigurationOutput] = None
    BoxConfiguration: Optional[BoxConfigurationOutput] = None
    QuipConfiguration: Optional[QuipConfigurationOutput] = None
    JiraConfiguration: Optional[JiraConfigurationOutput] = None
    GitHubConfiguration: Optional[GitHubConfigurationOutput] = None
    AlfrescoConfiguration: Optional[AlfrescoConfigurationOutput] = None
    TemplateConfiguration: Optional[TemplateConfigurationOutput] = None


class DataSourceConfiguration(BaseValidatorModel):
    S3Configuration: Optional[S3DataSourceConfiguration] = None
    SharePointConfiguration: Optional[SharePointConfiguration] = None
    DatabaseConfiguration: Optional[DatabaseConfiguration] = None
    SalesforceConfiguration: Optional[SalesforceConfiguration] = None
    OneDriveConfiguration: Optional[OneDriveConfiguration] = None
    ServiceNowConfiguration: Optional[ServiceNowConfiguration] = None
    ConfluenceConfiguration: Optional[ConfluenceConfiguration] = None
    GoogleDriveConfiguration: Optional[GoogleDriveConfiguration] = None
    WebCrawlerConfiguration: Optional[WebCrawlerConfiguration] = None
    WorkDocsConfiguration: Optional[WorkDocsConfiguration] = None
    FsxConfiguration: Optional[FsxConfiguration] = None
    SlackConfiguration: Optional[SlackConfiguration] = None
    BoxConfiguration: Optional[BoxConfiguration] = None
    QuipConfiguration: Optional[QuipConfiguration] = None
    JiraConfiguration: Optional[JiraConfiguration] = None
    GitHubConfiguration: Optional[GitHubConfiguration] = None
    AlfrescoConfiguration: Optional[AlfrescoConfiguration] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None


class CustomDocumentEnrichmentConfiguration(BaseValidatorModel):
    InlineConfigurations: Optional[List[InlineCustomDocumentEnrichmentConfiguration]] = None
    PreExtractionHookConfiguration: Optional[HookConfiguration] = None
    PostExtractionHookConfiguration: Optional[HookConfiguration] = None
    RoleArn: Optional[str] = None

DocumentAttributeUnion = Union[DocumentAttribute, DocumentAttributeOutput]


class FeaturedResultsItem(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[QueryResultTypeType] = None
    AdditionalAttributes: Optional[List[AdditionalResultAttribute]] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlights] = None
    DocumentExcerpt: Optional[TextWithHighlights] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutput]] = None
    FeedbackToken: Optional[str] = None


class QueryResultItem(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[QueryResultTypeType] = None
    Format: Optional[QueryResultFormatType] = None
    AdditionalAttributes: Optional[List[AdditionalResultAttribute]] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlights] = None
    DocumentExcerpt: Optional[TextWithHighlights] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutput]] = None
    ScoreAttributes: Optional[ScoreAttributes] = None
    FeedbackToken: Optional[str] = None
    TableExcerpt: Optional[TableExcerpt] = None
    CollapsedResultDetail: Optional[CollapsedResultDetail] = None


# This class is the input for the 'update_index' function.
class UpdateIndexRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    DocumentMetadataConfigurationUpdates: Optional[List[DocumentMetadataConfigurationUnion]] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None
    UserTokenConfigurations: Optional[List[UserTokenConfiguration]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfiguration] = None


# This class is the output for the 'get_query_suggestions' function.
class GetQuerySuggestionsResponse(BaseValidatorModel):
    QuerySuggestionsId: str
    Suggestions: List[Suggestion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_source' function.
class DescribeDataSourceResponse(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: str
    Type: DataSourceTypeType
    Configuration: DataSourceConfigurationOutput
    VpcConfiguration: DataSourceVpcConfigurationOutput
    CreatedAt: datetime
    UpdatedAt: datetime
    Description: str
    Status: DataSourceStatusType
    Schedule: str
    RoleArn: str
    ErrorMessage: str
    LanguageCode: str
    CustomDocumentEnrichmentConfiguration: CustomDocumentEnrichmentConfigurationOutput
    ResponseMetadata: ResponseMetadata

DataSourceConfigurationUnion = Union[DataSourceConfiguration, DataSourceConfigurationOutput]

CustomDocumentEnrichmentConfigurationUnion = Union[CustomDocumentEnrichmentConfiguration, CustomDocumentEnrichmentConfigurationOutput]


class AttributeFilter(BaseValidatorModel):
    AndAllFilters: Optional[List[Dict[str, Any]]] = None
    OrAllFilters: Optional[List[Dict[str, Any]]] = None
    NotFilter: Optional[Dict[str, Any]] = None
    EqualsTo: Optional[DocumentAttributeUnion] = None
    ContainsAll: Optional[DocumentAttributeUnion] = None
    ContainsAny: Optional[DocumentAttributeUnion] = None
    GreaterThan: Optional[DocumentAttributeUnion] = None
    GreaterThanOrEquals: Optional[DocumentAttributeUnion] = None
    LessThan: Optional[DocumentAttributeUnion] = None
    LessThanOrEquals: Optional[DocumentAttributeUnion] = None


class DocumentInfo(BaseValidatorModel):
    DocumentId: str
    Attributes: Optional[List[DocumentAttributeUnion]] = None


class Document(BaseValidatorModel):
    Id: str
    Title: Optional[str] = None
    Blob: Optional[Blob] = None
    S3Path: Optional[S3Path] = None
    Attributes: Optional[List[DocumentAttributeUnion]] = None
    AccessControlList: Optional[List[Principal]] = None
    HierarchicalAccessControlList: Optional[List[HierarchicalPrincipalUnion]] = None
    ContentType: Optional[ContentTypeType] = None
    AccessControlConfigurationId: Optional[str] = None


# This class is the output for the 'query' function.
class QueryResult(BaseValidatorModel):
    QueryId: str
    ResultItems: List[QueryResultItem]
    FacetResults: List[FacetResult]
    TotalNumberOfResults: int
    Warnings: List[Warning]
    SpellCorrectedQueries: List[SpellCorrectedQuery]
    FeaturedResultsItems: List[FeaturedResultsItem]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_data_source' function.
class CreateDataSourceRequest(BaseValidatorModel):
    Name: str
    IndexId: str
    Type: DataSourceTypeType
    Configuration: Optional[DataSourceConfigurationUnion] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationUnion] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[CustomDocumentEnrichmentConfigurationUnion] = None


# This class is the input for the 'update_data_source' function.
class UpdateDataSourceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Configuration: Optional[DataSourceConfigurationUnion] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationUnion] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    RoleArn: Optional[str] = None
    LanguageCode: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[CustomDocumentEnrichmentConfigurationUnion] = None


class AttributeSuggestionsGetConfig(BaseValidatorModel):
    SuggestionAttributes: Optional[List[str]] = None
    AdditionalResponseAttributes: Optional[List[str]] = None
    AttributeFilter: Optional[AttributeFilter] = None
    UserContext: Optional[UserContext] = None


# This class is the input for the 'query' function.
class QueryRequest(BaseValidatorModel):
    IndexId: str
    QueryText: Optional[str] = None
    AttributeFilter: Optional[AttributeFilter] = None
    Facets: Optional[List[Facet]] = None
    RequestedDocumentAttributes: Optional[List[str]] = None
    QueryResultTypeFilter: Optional[QueryResultTypeType] = None
    DocumentRelevanceOverrideConfigurations: Optional[List[DocumentRelevanceConfiguration]] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    SortingConfiguration: Optional[SortingConfiguration] = None
    SortingConfigurations: Optional[List[SortingConfiguration]] = None
    UserContext: Optional[UserContext] = None
    VisitorId: Optional[str] = None
    SpellCorrectionConfiguration: Optional[SpellCorrectionConfiguration] = None
    CollapseConfiguration: Optional[CollapseConfiguration] = None


# This class is the input for the 'retrieve' function.
class RetrieveRequest(BaseValidatorModel):
    IndexId: str
    QueryText: str
    AttributeFilter: Optional[AttributeFilter] = None
    RequestedDocumentAttributes: Optional[List[str]] = None
    DocumentRelevanceOverrideConfigurations: Optional[List[DocumentRelevanceConfiguration]] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    UserContext: Optional[UserContext] = None


# This class is the input for the 'batch_get_document_status' function.
class BatchGetDocumentStatusRequest(BaseValidatorModel):
    IndexId: str
    DocumentInfoList: List[DocumentInfo]


# This class is the input for the 'batch_put_document' function.
class BatchPutDocumentRequest(BaseValidatorModel):
    IndexId: str
    Documents: List[Document]
    RoleArn: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[CustomDocumentEnrichmentConfigurationUnion] = None


# This class is the input for the 'get_query_suggestions' function.
class GetQuerySuggestionsRequest(BaseValidatorModel):
    IndexId: str
    QueryText: str
    MaxSuggestionsCount: Optional[int] = None
    SuggestionTypes: Optional[List[SuggestionTypeType]] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsGetConfig] = None