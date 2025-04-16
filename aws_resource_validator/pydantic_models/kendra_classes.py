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
from aws_resource_validator.pydantic_models.kendra_constants import *

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
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]


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


class BatchDeleteFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetIds: Sequence[str]


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


class CapacityUnitsConfiguration(BaseValidatorModel):
    StorageCapacityUnits: int
    QueryCapacityUnits: int


class ClearQuerySuggestionsRequest(BaseValidatorModel):
    IndexId: str


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
    DataSourceIds: Optional[Sequence[str]] = None
    FaqIds: Optional[Sequence[str]] = None
    DirectPutContent: Optional[bool] = None


class Correction(BaseValidatorModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Term: Optional[str] = None
    CorrectedTerm: Optional[str] = None


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
    Template: Optional[Mapping[str, Any]] = None


class DataSourceGroup(BaseValidatorModel):
    GroupId: str
    DataSourceId: str


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


class DeleteDataSourceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteFaqRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteIndexRequest(BaseValidatorModel):
    Id: str


class DeletePrincipalMappingRequest(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None


class DeleteQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Id: str


class DeleteThesaurusRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DescribeAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Id: str


class DescribeDataSourceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DescribeExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class ExperienceEndpoint(BaseValidatorModel):
    EndpointType: Optional[Literal["HOME"]] = None
    Endpoint: Optional[str] = None


class DescribeFaqRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DescribeFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str


class FeaturedDocumentMissing(BaseValidatorModel):
    Id: Optional[str] = None


class FeaturedDocumentWithMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    URI: Optional[str] = None


class DescribeIndexRequest(BaseValidatorModel):
    Id: str


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


class DescribeQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Id: str


class DescribeQuerySuggestionsConfigRequest(BaseValidatorModel):
    IndexId: str


class DescribeThesaurusRequest(BaseValidatorModel):
    Id: str
    IndexId: str


class DisassociatePersonasFromEntitiesRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityIds: Sequence[str]


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
    Facets: Optional[Sequence[Mapping[str, Any]]] = None
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


class ListAccessControlConfigurationsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataSourcesRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class ListExperienceEntitiesRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None


class ListExperiencesRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFaqsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFeaturedResultsSetsRequest(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupsOlderThanOrderingIdRequest(BaseValidatorModel):
    IndexId: str
    OrderingId: int
    DataSourceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIndicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


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
    Code: Optional[Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]] = None


class RelevanceFeedback(BaseValidatorModel):
    ResultId: str
    RelevanceValue: RelevanceTypeType


class Relevance(BaseValidatorModel):
    Freshness: Optional[bool] = None
    Importance: Optional[int] = None
    Duration: Optional[str] = None
    RankOrder: Optional[OrderType] = None
    ValueImportanceMap: Optional[Mapping[str, int]] = None


class SeedUrlConfigurationOutput(BaseValidatorModel):
    SeedUrls: List[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None


class SeedUrlConfiguration(BaseValidatorModel):
    SeedUrls: Sequence[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None


class SiteMapsConfigurationOutput(BaseValidatorModel):
    SiteMaps: List[str]


class SiteMapsConfiguration(BaseValidatorModel):
    SiteMaps: Sequence[str]


class StartDataSourceSyncJobRequest(BaseValidatorModel):
    Id: str
    IndexId: str


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
    TagKeys: Sequence[str]


class ColumnConfigurationOutput(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: List[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class ColumnConfiguration(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: Sequence[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


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
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    ExcludeMimeTypes: Optional[Sequence[str]] = None
    ExcludeUserAccounts: Optional[Sequence[str]] = None
    ExcludeSharedDrives: Optional[Sequence[str]] = None


class SalesforceChatterFeedConfigurationOutput(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None
    IncludeFilterTypes: Optional[List[SalesforceChatterFeedIncludeFilterTypeType]] = None


class SalesforceChatterFeedConfiguration(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    IncludeFilterTypes: Optional[Sequence[SalesforceChatterFeedIncludeFilterTypeType]] = None


class SalesforceCustomKnowledgeArticleTypeConfigurationOutput(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceCustomKnowledgeArticleTypeConfiguration(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardKnowledgeArticleTypeConfigurationOutput(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardKnowledgeArticleTypeConfiguration(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectAttachmentConfigurationOutput(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectAttachmentConfiguration(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectConfigurationOutput(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMapping]] = None


class SalesforceStandardObjectConfiguration(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


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
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
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
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


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
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


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
    FileSystemType: Literal["WINDOWS"]
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
    OneDriveUserList: Optional[Sequence[str]] = None
    OneDriveUserS3Path: Optional[S3Path] = None


class UpdateQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SourceS3Path: Optional[S3Path] = None
    RoleArn: Optional[str] = None


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
    EntityFilter: Optional[Sequence[AlfrescoEntityType]] = None
    DocumentLibraryFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    BlogFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    WikiFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class BoxConfiguration(BaseValidatorModel):
    EnterpriseId: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    CrawlTasks: Optional[bool] = None
    CrawlWebLinks: Optional[bool] = None
    FileFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    TaskFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    CommentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    WebLinkFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class FsxConfiguration(BaseValidatorModel):
    FileSystemId: str
    FileSystemType: Literal["WINDOWS"]
    VpcConfiguration: DataSourceVpcConfiguration
    SecretArn: Optional[str] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


class JiraConfiguration(BaseValidatorModel):
    JiraAccountUrl: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    Project: Optional[Sequence[str]] = None
    IssueType: Optional[Sequence[str]] = None
    Status: Optional[Sequence[str]] = None
    IssueSubEntityFilter: Optional[Sequence[IssueSubEntityType]] = None
    AttachmentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    CommentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    IssueFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    ProjectFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    WorkLogFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class QuipConfiguration(BaseValidatorModel):
    Domain: str
    SecretArn: str
    CrawlFileComments: Optional[bool] = None
    CrawlChatRooms: Optional[bool] = None
    CrawlAttachments: Optional[bool] = None
    FolderIds: Optional[Sequence[str]] = None
    ThreadFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    MessageFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    AttachmentFieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None


class SlackConfiguration(BaseValidatorModel):
    TeamId: str
    SecretArn: str
    SlackEntityList: Sequence[SlackEntityType]
    SinceCrawlDate: str
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    UseChangeLog: Optional[bool] = None
    CrawlBotMessage: Optional[bool] = None
    ExcludeArchived: Optional[bool] = None
    LookBackPeriod: Optional[int] = None
    PrivateChannelFilter: Optional[Sequence[str]] = None
    PublicChannelFilter: Optional[Sequence[str]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None


class AssociateEntitiesToExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfiguration]


class DisassociateEntitiesFromExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfiguration]


class AssociateEntitiesToExperienceResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


class AssociatePersonasToEntitiesResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


class CreateAccessControlConfigurationResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateDataSourceResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateExperienceResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateFaqResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateIndexResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateQuerySuggestionsBlockListResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateThesaurusResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


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


class DisassociateEntitiesFromExperienceResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


class DisassociatePersonasFromEntitiesResponse(BaseValidatorModel):
    FailedEntityList: List[FailedEntity]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListAccessControlConfigurationsResponse(BaseValidatorModel):
    AccessControlConfigurations: List[AccessControlConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartDataSourceSyncJobResponse(BaseValidatorModel):
    ExecutionId: str
    ResponseMetadata: ResponseMetadata


class AssociatePersonasToEntitiesRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    Personas: Sequence[EntityPersonaConfiguration]


class AttributeSuggestionsDescribeConfig(BaseValidatorModel):
    SuggestableConfigList: Optional[List[SuggestableConfig]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None


class AttributeSuggestionsUpdateConfig(BaseValidatorModel):
    SuggestableConfigList: Optional[Sequence[SuggestableConfig]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None


class AuthenticationConfigurationOutput(BaseValidatorModel):
    BasicAuthentication: Optional[List[BasicAuthenticationConfiguration]] = None


class AuthenticationConfiguration(BaseValidatorModel):
    BasicAuthentication: Optional[Sequence[BasicAuthenticationConfiguration]] = None


class BatchDeleteDocumentRequest(BaseValidatorModel):
    IndexId: str
    DocumentIdList: Sequence[str]
    DataSourceSyncJobMetricTarget: Optional[DataSourceSyncJobMetricTarget] = None


class BatchDeleteDocumentResponse(BaseValidatorModel):
    FailedDocuments: List[BatchDeleteDocumentResponseFailedDocument]
    ResponseMetadata: ResponseMetadata


class BatchDeleteFeaturedResultsSetResponse(BaseValidatorModel):
    Errors: List[BatchDeleteFeaturedResultsSetError]
    ResponseMetadata: ResponseMetadata


class BatchGetDocumentStatusResponse(BaseValidatorModel):
    Errors: List[BatchGetDocumentStatusResponseError]
    DocumentStatusList: List[Status]
    ResponseMetadata: ResponseMetadata


class BatchPutDocumentResponse(BaseValidatorModel):
    FailedDocuments: List[BatchPutDocumentResponseFailedDocument]
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class ClickFeedback(BaseValidatorModel):
    ResultId: str
    ClickTime: Timestamp


class DocumentAttributeValue(BaseValidatorModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[Sequence[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[Timestamp] = None


class TimeRange(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class CollapseConfiguration(BaseValidatorModel):
    DocumentAttributeKey: str
    SortingConfigurations: Optional[Sequence[SortingConfiguration]] = None
    MissingAttributeKeyStrategy: Optional[MissingAttributeKeyStrategyType] = None
    Expand: Optional[bool] = None
    ExpandConfiguration: Optional[ExpandConfiguration] = None


class ConfluenceAttachmentConfigurationOutput(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[List[ConfluenceAttachmentToIndexFieldMapping]] = None


class ConfluenceAttachmentConfiguration(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[Sequence[ConfluenceAttachmentToIndexFieldMapping]] = None


class ConfluenceBlogConfigurationOutput(BaseValidatorModel):
    BlogFieldMappings: Optional[List[ConfluenceBlogToIndexFieldMapping]] = None


class ConfluenceBlogConfiguration(BaseValidatorModel):
    BlogFieldMappings: Optional[Sequence[ConfluenceBlogToIndexFieldMapping]] = None


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
    Urls: Sequence[str]
    SecretArn: str
    CrawlAttachments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfiguration] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    DocumentTitleFieldName: Optional[str] = None
    DisableLocalGroups: Optional[bool] = None
    SslCertificateS3Path: Optional[S3Path] = None
    AuthenticationType: Optional[SharePointOnlineAuthenticationTypeType] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None


class ConfluencePageConfigurationOutput(BaseValidatorModel):
    PageFieldMappings: Optional[List[ConfluencePageToIndexFieldMapping]] = None


class ConfluencePageConfiguration(BaseValidatorModel):
    PageFieldMappings: Optional[Sequence[ConfluencePageToIndexFieldMapping]] = None


class ConfluenceSpaceConfigurationOutput(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[List[str]] = None
    ExcludeSpaces: Optional[List[str]] = None
    SpaceFieldMappings: Optional[List[ConfluenceSpaceToIndexFieldMapping]] = None


class ConfluenceSpaceConfiguration(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[Sequence[str]] = None
    ExcludeSpaces: Optional[Sequence[str]] = None
    SpaceFieldMappings: Optional[Sequence[ConfluenceSpaceToIndexFieldMapping]] = None


class SpellCorrectedQuery(BaseValidatorModel):
    SuggestedQueryText: Optional[str] = None
    Corrections: Optional[List[Correction]] = None


class Principal(BaseValidatorModel):
    pass


class HierarchicalPrincipalOutput(BaseValidatorModel):
    PrincipalList: List[Principal]


class HierarchicalPrincipal(BaseValidatorModel):
    PrincipalList: Sequence[Principal]


class CreateFaqRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    S3Path: S3Path
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    FileFormat: Optional[FaqFileFormatType] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None


class CreateQuerySuggestionsBlockListRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    SourceS3Path: S3Path
    RoleArn: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateThesaurusRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    RoleArn: str
    SourceS3Path: S3Path
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    ClientToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetName: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[Sequence[str]] = None
    FeaturedDocuments: Optional[Sequence[FeaturedDocument]] = None
    Tags: Optional[Sequence[Tag]] = None


class FeaturedResultsSet(BaseValidatorModel):
    FeaturedResultsSetId: Optional[str] = None
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[List[str]] = None
    FeaturedDocuments: Optional[List[FeaturedDocument]] = None
    LastUpdatedTimestamp: Optional[int] = None
    CreationTimestamp: Optional[int] = None


class UpdateFeaturedResultsSetRequest(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str
    FeaturedResultsSetName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[FeaturedResultsSetStatusType] = None
    QueryTexts: Optional[Sequence[str]] = None
    FeaturedDocuments: Optional[Sequence[FeaturedDocument]] = None


class UserContext(BaseValidatorModel):
    Token: Optional[str] = None
    UserId: Optional[str] = None
    Groups: Optional[Sequence[str]] = None
    DataSourceGroups: Optional[Sequence[DataSourceGroup]] = None


class DataSourceSummary(BaseValidatorModel):
    pass


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


class S3DataSourceConfigurationOutput(BaseValidatorModel):
    BucketName: str
    InclusionPrefixes: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    DocumentsMetadataConfiguration: Optional[DocumentsMetadataConfiguration] = None
    AccessControlListConfiguration: Optional[AccessControlListConfiguration] = None


class S3DataSourceConfiguration(BaseValidatorModel):
    BucketName: str
    InclusionPrefixes: Optional[Sequence[str]] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
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


class ListFaqsResponse(BaseValidatorModel):
    FaqSummaryItems: List[FaqSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFeaturedResultsSetsResponse(BaseValidatorModel):
    FeaturedResultsSetSummaryItems: List[FeaturedResultsSetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetSnapshotsResponse(BaseValidatorModel):
    SnapShotTimeFilter: TimeRangeOutput
    SnapshotsDataHeader: List[str]
    SnapshotsData: List[List[str]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GroupMembers(BaseValidatorModel):
    MemberGroups: Optional[Sequence[MemberGroup]] = None
    MemberUsers: Optional[Sequence[MemberUser]] = None
    S3PathforGroupMembers: Optional[S3Path] = None


class ListGroupsOlderThanOrderingIdResponse(BaseValidatorModel):
    GroupsSummaries: List[GroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListEntityPersonasResponse(BaseValidatorModel):
    SummaryItems: List[PersonasSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQuerySuggestionsBlockListsResponse(BaseValidatorModel):
    BlockListSummaryItems: List[QuerySuggestionsBlockListSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListThesauriResponse(BaseValidatorModel):
    ThesaurusSummaryItems: List[ThesaurusSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UrlsOutput(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfigurationOutput] = None
    SiteMapsConfiguration: Optional[SiteMapsConfigurationOutput] = None


class Urls(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfiguration] = None
    SiteMapsConfiguration: Optional[SiteMapsConfiguration] = None


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
    StandardKnowledgeArticleTypeConfiguration: Optional[ SalesforceStandardKnowledgeArticleTypeConfigurationOutput ] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[ List[SalesforceCustomKnowledgeArticleTypeConfigurationOutput] ] = None


class SalesforceKnowledgeArticleConfiguration(BaseValidatorModel):
    IncludedStates: Sequence[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[ SalesforceStandardKnowledgeArticleTypeConfiguration ] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[ Sequence[SalesforceCustomKnowledgeArticleTypeConfiguration] ] = None


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
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMapping]] = None
    DisableLocalGroups: Optional[bool] = None


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


class UpdateQuerySuggestionsConfigRequest(BaseValidatorModel):
    IndexId: str
    Mode: Optional[ModeType] = None
    QueryLogLookBackWindowInDays: Optional[int] = None
    IncludeQueriesWithoutUserInformation: Optional[bool] = None
    MinimumNumberOfQueryingUsers: Optional[int] = None
    MinimumQueryCount: Optional[int] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsUpdateConfig] = None


class SubmitFeedbackRequest(BaseValidatorModel):
    IndexId: str
    QueryId: str
    ClickFeedbackItems: Optional[Sequence[ClickFeedback]] = None
    RelevanceFeedbackItems: Optional[Sequence[RelevanceFeedback]] = None


class DocumentAttributeCondition(BaseValidatorModel):
    ConditionDocumentAttributeKey: str
    Operator: ConditionOperatorType
    ConditionOnValue: Optional[DocumentAttributeValue] = None


class DocumentAttributeTarget(BaseValidatorModel):
    TargetDocumentAttributeKey: Optional[str] = None
    TargetDocumentAttributeValueDeletion: Optional[bool] = None
    TargetDocumentAttributeValue: Optional[DocumentAttributeValue] = None


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
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None
    AuthenticationType: Optional[ConfluenceAuthenticationTypeType] = None


class DescribeAccessControlConfigurationResponse(BaseValidatorModel):
    Name: str
    Description: str
    ErrorMessage: str
    AccessControlList: List[Principal]
    HierarchicalAccessControlList: List[HierarchicalPrincipalOutput]
    ResponseMetadata: ResponseMetadata


class CreateFeaturedResultsSetResponse(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSet
    ResponseMetadata: ResponseMetadata


class UpdateFeaturedResultsSetResponse(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSet
    ResponseMetadata: ResponseMetadata


class ListDataSourceSyncJobsResponse(BaseValidatorModel):
    History: List[DataSourceSyncJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListExperienceEntitiesResponse(BaseValidatorModel):
    SummaryItems: List[ExperienceEntitiesSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class PutPrincipalMappingRequest(BaseValidatorModel):
    IndexId: str
    GroupId: str
    GroupMembers: GroupMembers
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None
    RoleArn: Optional[str] = None


class TextWithHighlights(BaseValidatorModel):
    pass


class AdditionalResultAttributeValue(BaseValidatorModel):
    TextWithHighlightsValue: Optional[TextWithHighlights] = None


class ExpandedResultItem(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlights] = None
    DocumentExcerpt: Optional[TextWithHighlights] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutput]] = None


class CreateIndexRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    Edition: Optional[IndexEditionType] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    UserTokenConfigurations: Optional[Sequence[UserTokenConfiguration]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfiguration] = None


class DocumentMetadataConfigurationOutput(BaseValidatorModel):
    pass


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


class RelevanceUnion(BaseValidatorModel):
    pass


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
    UrlInclusionPatterns: Optional[Sequence[str]] = None
    UrlExclusionPatterns: Optional[Sequence[str]] = None
    ProxyConfiguration: Optional[ProxyConfiguration] = None
    AuthenticationConfiguration: Optional[AuthenticationConfiguration] = None


class TableExcerpt(BaseValidatorModel):
    Rows: Optional[List[TableRow]] = None
    TotalNumberOfRows: Optional[int] = None


class SalesforceConfigurationOutput(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[ List[SalesforceStandardObjectConfigurationOutput] ] = None
    KnowledgeArticleConfiguration: Optional[SalesforceKnowledgeArticleConfigurationOutput] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfigurationOutput] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[ SalesforceStandardObjectAttachmentConfigurationOutput ] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None


class SalesforceConfiguration(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[ Sequence[SalesforceStandardObjectConfiguration] ] = None
    KnowledgeArticleConfiguration: Optional[SalesforceKnowledgeArticleConfiguration] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfiguration] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[ SalesforceStandardObjectAttachmentConfiguration ] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None


class HookConfiguration(BaseValidatorModel):
    LambdaArn: str
    S3Bucket: str
    InvocationCondition: Optional[DocumentAttributeCondition] = None


class InlineCustomDocumentEnrichmentConfiguration(BaseValidatorModel):
    Condition: Optional[DocumentAttributeCondition] = None
    Target: Optional[DocumentAttributeTarget] = None
    DocumentContentDeletion: Optional[bool] = None


class DocumentAttributeValueUnion(BaseValidatorModel):
    pass


class DocumentAttribute(BaseValidatorModel):
    Key: str
    Value: DocumentAttributeValueUnion


class TimeRangeUnion(BaseValidatorModel):
    pass


class ListDataSourceSyncJobsRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeFilter: Optional[TimeRangeUnion] = None
    StatusFilter: Optional[DataSourceSyncJobStatusType] = None


class HierarchicalPrincipalUnion(BaseValidatorModel):
    pass


class CreateAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Name: str
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[Principal]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalUnion]] = None
    ClientToken: Optional[str] = None


class UpdateAccessControlConfigurationRequest(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[Principal]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalUnion]] = None


class RetrieveResult(BaseValidatorModel):
    QueryId: str
    ResultItems: List[RetrieveResultItem]
    ResponseMetadata: ResponseMetadata


class CustomDocumentEnrichmentConfigurationOutput(BaseValidatorModel):
    InlineConfigurations: Optional[ List[InlineCustomDocumentEnrichmentConfigurationOutput] ] = None
    PreExtractionHookConfiguration: Optional[HookConfigurationOutput] = None
    PostExtractionHookConfiguration: Optional[HookConfigurationOutput] = None
    RoleArn: Optional[str] = None


class ExperienceConfigurationUnion(BaseValidatorModel):
    pass


class CreateExperienceRequest(BaseValidatorModel):
    Name: str
    IndexId: str
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationUnion] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdateExperienceRequest(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationUnion] = None
    Description: Optional[str] = None


class AdditionalResultAttribute(BaseValidatorModel):
    Key: str
    ValueType: Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
    Value: AdditionalResultAttributeValue


class CollapsedResultDetail(BaseValidatorModel):
    DocumentAttribute: DocumentAttributeOutput
    ExpandedResults: Optional[List[ExpandedResultItem]] = None


class SuggestionValue(BaseValidatorModel):
    pass


class Suggestion(BaseValidatorModel):
    Id: Optional[str] = None
    Value: Optional[SuggestionValue] = None
    SourceDocuments: Optional[List[SourceDocument]] = None


class GitHubConfigurationOutput(BaseValidatorModel):
    pass


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


class GitHubConfiguration(BaseValidatorModel):
    pass


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
    InlineConfigurations: Optional[Sequence[InlineCustomDocumentEnrichmentConfiguration]] = None
    PreExtractionHookConfiguration: Optional[HookConfiguration] = None
    PostExtractionHookConfiguration: Optional[HookConfiguration] = None
    RoleArn: Optional[str] = None


class DocumentMetadataConfigurationUnion(BaseValidatorModel):
    pass


class UpdateIndexRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    DocumentMetadataConfigurationUpdates: Optional[ Sequence[DocumentMetadataConfigurationUnion] ] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None
    UserTokenConfigurations: Optional[Sequence[UserTokenConfiguration]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfiguration] = None


class GetQuerySuggestionsResponse(BaseValidatorModel):
    QuerySuggestionsId: str
    Suggestions: List[Suggestion]
    ResponseMetadata: ResponseMetadata


class DocumentAttributeUnion(BaseValidatorModel):
    pass


class AttributeFilter(BaseValidatorModel):
    AndAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    OrAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    NotFilter: Optional[Mapping[str, Any]] = None
    EqualsTo: Optional[DocumentAttributeUnion] = None
    ContainsAll: Optional[DocumentAttributeUnion] = None
    ContainsAny: Optional[DocumentAttributeUnion] = None
    GreaterThan: Optional[DocumentAttributeUnion] = None
    GreaterThanOrEquals: Optional[DocumentAttributeUnion] = None
    LessThan: Optional[DocumentAttributeUnion] = None
    LessThanOrEquals: Optional[DocumentAttributeUnion] = None


class DocumentInfo(BaseValidatorModel):
    DocumentId: str
    Attributes: Optional[Sequence[DocumentAttributeUnion]] = None


class Blob(BaseValidatorModel):
    pass


class Document(BaseValidatorModel):
    Id: str
    Title: Optional[str] = None
    Blob: Optional[Blob] = None
    S3Path: Optional[S3Path] = None
    Attributes: Optional[Sequence[DocumentAttributeUnion]] = None
    AccessControlList: Optional[Sequence[Principal]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalUnion]] = None
    ContentType: Optional[ContentTypeType] = None
    AccessControlConfigurationId: Optional[str] = None


class QueryResultItem(BaseValidatorModel):
    pass


class FeaturedResultsItem(BaseValidatorModel):
    pass


class QueryResult(BaseValidatorModel):
    QueryId: str
    ResultItems: List[QueryResultItem]
    FacetResults: List[FacetResult]
    TotalNumberOfResults: int
    Warnings: List[Warning]
    SpellCorrectedQueries: List[SpellCorrectedQuery]
    FeaturedResultsItems: List[FeaturedResultsItem]
    ResponseMetadata: ResponseMetadata


class DataSourceConfigurationUnion(BaseValidatorModel):
    pass


class DataSourceVpcConfigurationUnion(BaseValidatorModel):
    pass


class CustomDocumentEnrichmentConfigurationUnion(BaseValidatorModel):
    pass


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
    CustomDocumentEnrichmentConfiguration: Optional[ CustomDocumentEnrichmentConfigurationUnion ] = None


class AttributeSuggestionsGetConfig(BaseValidatorModel):
    SuggestionAttributes: Optional[Sequence[str]] = None
    AdditionalResponseAttributes: Optional[Sequence[str]] = None
    AttributeFilter: Optional[AttributeFilter] = None
    UserContext: Optional[UserContext] = None


class QueryRequest(BaseValidatorModel):
    IndexId: str
    QueryText: Optional[str] = None
    AttributeFilter: Optional[AttributeFilter] = None
    Facets: Optional[Sequence[Facet]] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    QueryResultTypeFilter: Optional[QueryResultTypeType] = None
    DocumentRelevanceOverrideConfigurations: Optional[ Sequence[DocumentRelevanceConfiguration] ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    SortingConfiguration: Optional[SortingConfiguration] = None
    SortingConfigurations: Optional[Sequence[SortingConfiguration]] = None
    UserContext: Optional[UserContext] = None
    VisitorId: Optional[str] = None
    SpellCorrectionConfiguration: Optional[SpellCorrectionConfiguration] = None
    CollapseConfiguration: Optional[CollapseConfiguration] = None


class RetrieveRequest(BaseValidatorModel):
    IndexId: str
    QueryText: str
    AttributeFilter: Optional[AttributeFilter] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    DocumentRelevanceOverrideConfigurations: Optional[ Sequence[DocumentRelevanceConfiguration] ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    UserContext: Optional[UserContext] = None


class BatchGetDocumentStatusRequest(BaseValidatorModel):
    IndexId: str
    DocumentInfoList: Sequence[DocumentInfo]


class BatchPutDocumentRequest(BaseValidatorModel):
    IndexId: str
    Documents: Sequence[Document]
    RoleArn: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[ CustomDocumentEnrichmentConfigurationUnion ] = None


class GetQuerySuggestionsRequest(BaseValidatorModel):
    IndexId: str
    QueryText: str
    MaxSuggestionsCount: Optional[int] = None
    SuggestionTypes: Optional[Sequence[SuggestionTypeType]] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsGetConfig] = None


