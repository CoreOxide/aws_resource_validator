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


class DataSourceVpcConfigurationOutputTypeDef(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class S3PathTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str


class DataSourceVpcConfigurationTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]


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
    DataSourceId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class BatchDeleteFeaturedResultsSetErrorTypeDef(BaseValidatorModel):
    Id: str
    ErrorCode: ErrorCodeType
    ErrorMessage: str


class BatchDeleteFeaturedResultsSetRequestTypeDef(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetIds: Sequence[str]


class BatchGetDocumentStatusResponseErrorTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    DataSourceId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class StatusTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    DocumentStatus: Optional[DocumentStatusType] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None


class BatchPutDocumentResponseFailedDocumentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    DataSourceId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class CapacityUnitsConfigurationTypeDef(BaseValidatorModel):
    StorageCapacityUnits: int
    QueryCapacityUnits: int


class ClearQuerySuggestionsRequestTypeDef(BaseValidatorModel):
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


class ContentSourceConfigurationOutputTypeDef(BaseValidatorModel):
    DataSourceIds: Optional[List[str]] = None
    FaqIds: Optional[List[str]] = None
    DirectPutContent: Optional[bool] = None


class ContentSourceConfigurationTypeDef(BaseValidatorModel):
    DataSourceIds: Optional[Sequence[str]] = None
    FaqIds: Optional[Sequence[str]] = None
    DirectPutContent: Optional[bool] = None


class CorrectionTypeDef(BaseValidatorModel):
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Term: Optional[str] = None
    CorrectedTerm: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class FeaturedDocumentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None


class UserGroupResolutionConfigurationTypeDef(BaseValidatorModel):
    UserGroupResolutionMode: UserGroupResolutionModeType


class TemplateConfigurationOutputTypeDef(BaseValidatorModel):
    Template: Optional[Dict[str, Any]] = None


class TemplateConfigurationTypeDef(BaseValidatorModel):
    Template: Optional[Mapping[str, Any]] = None


class DataSourceGroupTypeDef(BaseValidatorModel):
    GroupId: str
    DataSourceId: str


class DataSourceSyncJobMetricsTypeDef(BaseValidatorModel):
    DocumentsAdded: Optional[str] = None
    DocumentsModified: Optional[str] = None
    DocumentsDeleted: Optional[str] = None
    DocumentsFailed: Optional[str] = None
    DocumentsScanned: Optional[str] = None


class SqlConfigurationTypeDef(BaseValidatorModel):
    QueryIdentifiersEnclosingOption: Optional[QueryIdentifiersEnclosingOptionType] = None


class DeleteAccessControlConfigurationRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str


class DeleteDataSourceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteExperienceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteFaqRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DeleteIndexRequestTypeDef(BaseValidatorModel):
    Id: str


class DeletePrincipalMappingRequestTypeDef(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None


class DeleteQuerySuggestionsBlockListRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str


class DeleteThesaurusRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DescribeAccessControlConfigurationRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str


class DescribeDataSourceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DescribeExperienceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class ExperienceEndpointTypeDef(BaseValidatorModel):
    EndpointType: Optional[Literal["HOME"]] = None
    Endpoint: Optional[str] = None


class DescribeFaqRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DescribeFeaturedResultsSetRequestTypeDef(BaseValidatorModel):
    IndexId: str
    FeaturedResultsSetId: str


class FeaturedDocumentMissingTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class FeaturedDocumentWithMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    URI: Optional[str] = None


class DescribeIndexRequestTypeDef(BaseValidatorModel):
    Id: str


class DescribePrincipalMappingRequestTypeDef(BaseValidatorModel):
    IndexId: str
    GroupId: str
    DataSourceId: Optional[str] = None


class GroupOrderingIdSummaryTypeDef(BaseValidatorModel):
    Status: Optional[PrincipalMappingStatusType] = None
    LastUpdatedAt: Optional[datetime] = None
    ReceivedAt: Optional[datetime] = None
    OrderingId: Optional[int] = None
    FailureReason: Optional[str] = None


class DescribeQuerySuggestionsBlockListRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str


class DescribeQuerySuggestionsConfigRequestTypeDef(BaseValidatorModel):
    IndexId: str


class DescribeThesaurusRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class DisassociatePersonasFromEntitiesRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityIds: Sequence[str]


class DocumentAttributeValueOutputTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[List[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[datetime] = None


class RelevanceOutputTypeDef(BaseValidatorModel):
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


class FacetTypeDef(BaseValidatorModel):
    DocumentAttributeKey: Optional[str] = None
    Facets: Optional[Sequence[Mapping[str, Any]]] = None
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


class GetSnapshotsRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Interval: IntervalType
    MetricType: MetricTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TimeRangeOutputTypeDef(BaseValidatorModel):
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


class ListAccessControlConfigurationsRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataSourcesRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntityPersonasRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PersonasSummaryTypeDef(BaseValidatorModel):
    EntityId: Optional[str] = None
    Persona: Optional[PersonaType] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ListExperienceEntitiesRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None


class ListExperiencesRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFaqsRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFeaturedResultsSetsRequestTypeDef(BaseValidatorModel):
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupsOlderThanOrderingIdRequestTypeDef(BaseValidatorModel):
    IndexId: str
    OrderingId: int
    DataSourceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIndicesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListQuerySuggestionsBlockListsRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class ListThesauriRequestTypeDef(BaseValidatorModel):
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


class RelevanceTypeDef(BaseValidatorModel):
    Freshness: Optional[bool] = None
    Importance: Optional[int] = None
    Duration: Optional[str] = None
    RankOrder: Optional[OrderType] = None
    ValueImportanceMap: Optional[Mapping[str, int]] = None


class SeedUrlConfigurationOutputTypeDef(BaseValidatorModel):
    SeedUrls: List[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None


class SeedUrlConfigurationTypeDef(BaseValidatorModel):
    SeedUrls: Sequence[str]
    WebCrawlerMode: Optional[WebCrawlerModeType] = None


class SiteMapsConfigurationOutputTypeDef(BaseValidatorModel):
    SiteMaps: List[str]


class SiteMapsConfigurationTypeDef(BaseValidatorModel):
    SiteMaps: Sequence[str]


class StartDataSourceSyncJobRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str


class StopDataSourceSyncJobRequestTypeDef(BaseValidatorModel):
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


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class ColumnConfigurationOutputTypeDef(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: List[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class ColumnConfigurationTypeDef(BaseValidatorModel):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: Sequence[str]
    DocumentTitleColumnName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class GoogleDriveConfigurationOutputTypeDef(BaseValidatorModel):
    SecretArn: str
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    ExcludeMimeTypes: Optional[List[str]] = None
    ExcludeUserAccounts: Optional[List[str]] = None
    ExcludeSharedDrives: Optional[List[str]] = None


class GoogleDriveConfigurationTypeDef(BaseValidatorModel):
    SecretArn: str
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    ExcludeMimeTypes: Optional[Sequence[str]] = None
    ExcludeUserAccounts: Optional[Sequence[str]] = None
    ExcludeSharedDrives: Optional[Sequence[str]] = None


class SalesforceChatterFeedConfigurationOutputTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    IncludeFilterTypes: Optional[List[SalesforceChatterFeedIncludeFilterTypeType]] = None


class SalesforceChatterFeedConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    IncludeFilterTypes: Optional[Sequence[SalesforceChatterFeedIncludeFilterTypeType]] = None


class SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(BaseValidatorModel):
    Name: str
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceStandardObjectAttachmentConfigurationOutputTypeDef(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceStandardObjectAttachmentConfigurationTypeDef(BaseValidatorModel):
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceStandardObjectConfigurationOutputTypeDef(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class SalesforceStandardObjectConfigurationTypeDef(BaseValidatorModel):
    Name: SalesforceStandardObjectNameType
    DocumentDataFieldName: str
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class ServiceNowKnowledgeArticleConfigurationOutputTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    FilterQuery: Optional[str] = None


class ServiceNowKnowledgeArticleConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None
    FilterQuery: Optional[str] = None


class ServiceNowServiceCatalogConfigurationOutputTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class ServiceNowServiceCatalogConfigurationTypeDef(BaseValidatorModel):
    DocumentDataFieldName: str
    CrawlAttachments: Optional[bool] = None
    IncludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]] = None
    DocumentTitleFieldName: Optional[str] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class WorkDocsConfigurationOutputTypeDef(BaseValidatorModel):
    OrganizationId: str
    CrawlComments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class WorkDocsConfigurationTypeDef(BaseValidatorModel):
    OrganizationId: str
    CrawlComments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[Sequence[str]] = None
    ExclusionPatterns: Optional[Sequence[str]] = None
    FieldMappings: Optional[Sequence[DataSourceToIndexFieldMappingTypeDef]] = None


class BoxConfigurationOutputTypeDef(BaseValidatorModel):
    EnterpriseId: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    CrawlTasks: Optional[bool] = None
    CrawlWebLinks: Optional[bool] = None
    FileFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    TaskFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    CommentFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    WebLinkFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None


class FsxConfigurationOutputTypeDef(BaseValidatorModel):
    FileSystemId: str
    FileSystemType: Literal["WINDOWS"]
    VpcConfiguration: DataSourceVpcConfigurationOutputTypeDef
    SecretArn: Optional[str] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class JiraConfigurationOutputTypeDef(BaseValidatorModel):
    JiraAccountUrl: str
    SecretArn: str
    UseChangeLog: Optional[bool] = None
    Project: Optional[List[str]] = None
    IssueType: Optional[List[str]] = None
    Status: Optional[List[str]] = None
    IssueSubEntityFilter: Optional[List[IssueSubEntityType]] = None
    AttachmentFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    CommentFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    IssueFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    ProjectFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    WorkLogFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None


class QuipConfigurationOutputTypeDef(BaseValidatorModel):
    Domain: str
    SecretArn: str
    CrawlFileComments: Optional[bool] = None
    CrawlChatRooms: Optional[bool] = None
    CrawlAttachments: Optional[bool] = None
    FolderIds: Optional[List[str]] = None
    ThreadFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    MessageFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    AttachmentFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None


class SlackConfigurationOutputTypeDef(BaseValidatorModel):
    TeamId: str
    SecretArn: str
    SlackEntityList: List[SlackEntityType]
    SinceCrawlDate: str
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None
    UseChangeLog: Optional[bool] = None
    CrawlBotMessage: Optional[bool] = None
    ExcludeArchived: Optional[bool] = None
    LookBackPeriod: Optional[int] = None
    PrivateChannelFilter: Optional[List[str]] = None
    PublicChannelFilter: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None


class AlfrescoConfigurationOutputTypeDef(BaseValidatorModel):
    SiteUrl: str
    SiteId: str
    SecretArn: str
    SslCertificateS3Path: S3PathTypeDef
    CrawlSystemFolders: Optional[bool] = None
    CrawlComments: Optional[bool] = None
    EntityFilter: Optional[List[AlfrescoEntityType]] = None
    DocumentLibraryFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    BlogFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    WikiFieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None


class OnPremiseConfigurationTypeDef(BaseValidatorModel):
    HostUrl: str
    OrganizationName: str
    SslCertificateS3Path: S3PathTypeDef


class OneDriveUsersOutputTypeDef(BaseValidatorModel):
    OneDriveUserList: Optional[List[str]] = None
    OneDriveUserS3Path: Optional[S3PathTypeDef] = None


class OneDriveUsersTypeDef(BaseValidatorModel):
    OneDriveUserList: Optional[Sequence[str]] = None
    OneDriveUserS3Path: Optional[S3PathTypeDef] = None


class UpdateQuerySuggestionsBlockListRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SourceS3Path: Optional[S3PathTypeDef] = None
    RoleArn: Optional[str] = None


class UpdateThesaurusRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    SourceS3Path: Optional[S3PathTypeDef] = None


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


class AssociateEntitiesToExperienceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    EntityList: Sequence[EntityConfigurationTypeDef]


class DisassociateEntitiesFromExperienceRequestTypeDef(BaseValidatorModel):
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
    AccessControlConfigurations: List[AccessControlConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartDataSourceSyncJobResponseTypeDef(BaseValidatorModel):
    ExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatePersonasToEntitiesRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Personas: Sequence[EntityPersonaConfigurationTypeDef]


class AttributeSuggestionsDescribeConfigTypeDef(BaseValidatorModel):
    SuggestableConfigList: Optional[List[SuggestableConfigTypeDef]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None


class AttributeSuggestionsUpdateConfigTypeDef(BaseValidatorModel):
    SuggestableConfigList: Optional[Sequence[SuggestableConfigTypeDef]] = None
    AttributeSuggestionsMode: Optional[AttributeSuggestionsModeType] = None


class AuthenticationConfigurationOutputTypeDef(BaseValidatorModel):
    BasicAuthentication: Optional[List[BasicAuthenticationConfigurationTypeDef]] = None


class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    BasicAuthentication: Optional[Sequence[BasicAuthenticationConfigurationTypeDef]] = None


class BatchDeleteDocumentRequestTypeDef(BaseValidatorModel):
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


class TimestampTypeDef(BaseValidatorModel):
    pass


class ClickFeedbackTypeDef(BaseValidatorModel):
    ResultId: str
    ClickTime: TimestampTypeDef


class DocumentAttributeValueTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    StringListValue: Optional[Sequence[str]] = None
    LongValue: Optional[int] = None
    DateValue: Optional[TimestampTypeDef] = None


class TimeRangeTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None


class CollapseConfigurationTypeDef(BaseValidatorModel):
    DocumentAttributeKey: str
    SortingConfigurations: Optional[Sequence[SortingConfigurationTypeDef]] = None
    MissingAttributeKeyStrategy: Optional[MissingAttributeKeyStrategyType] = None
    Expand: Optional[bool] = None
    ExpandConfiguration: Optional[ExpandConfigurationTypeDef] = None


class ConfluenceAttachmentConfigurationOutputTypeDef(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[List[ConfluenceAttachmentToIndexFieldMappingTypeDef]] = None


class ConfluenceAttachmentConfigurationTypeDef(BaseValidatorModel):
    CrawlAttachments: Optional[bool] = None
    AttachmentFieldMappings: Optional[Sequence[ConfluenceAttachmentToIndexFieldMappingTypeDef]] = None


class ConfluenceBlogConfigurationOutputTypeDef(BaseValidatorModel):
    BlogFieldMappings: Optional[List[ConfluenceBlogToIndexFieldMappingTypeDef]] = None


class ConfluenceBlogConfigurationTypeDef(BaseValidatorModel):
    BlogFieldMappings: Optional[Sequence[ConfluenceBlogToIndexFieldMappingTypeDef]] = None


class SharePointConfigurationOutputTypeDef(BaseValidatorModel):
    SharePointVersion: SharePointVersionType
    Urls: List[str]
    SecretArn: str
    CrawlAttachments: Optional[bool] = None
    UseChangeLog: Optional[bool] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    DocumentTitleFieldName: Optional[str] = None
    DisableLocalGroups: Optional[bool] = None
    SslCertificateS3Path: Optional[S3PathTypeDef] = None
    AuthenticationType: Optional[SharePointOnlineAuthenticationTypeType] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None


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


class ConfluencePageConfigurationOutputTypeDef(BaseValidatorModel):
    PageFieldMappings: Optional[List[ConfluencePageToIndexFieldMappingTypeDef]] = None


class ConfluencePageConfigurationTypeDef(BaseValidatorModel):
    PageFieldMappings: Optional[Sequence[ConfluencePageToIndexFieldMappingTypeDef]] = None


class ConfluenceSpaceConfigurationOutputTypeDef(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[List[str]] = None
    ExcludeSpaces: Optional[List[str]] = None
    SpaceFieldMappings: Optional[List[ConfluenceSpaceToIndexFieldMappingTypeDef]] = None


class ConfluenceSpaceConfigurationTypeDef(BaseValidatorModel):
    CrawlPersonalSpaces: Optional[bool] = None
    CrawlArchivedSpaces: Optional[bool] = None
    IncludeSpaces: Optional[Sequence[str]] = None
    ExcludeSpaces: Optional[Sequence[str]] = None
    SpaceFieldMappings: Optional[Sequence[ConfluenceSpaceToIndexFieldMappingTypeDef]] = None


class SpellCorrectedQueryTypeDef(BaseValidatorModel):
    SuggestedQueryText: Optional[str] = None
    Corrections: Optional[List[CorrectionTypeDef]] = None


class PrincipalTypeDef(BaseValidatorModel):
    pass


class HierarchicalPrincipalOutputTypeDef(BaseValidatorModel):
    PrincipalList: List[PrincipalTypeDef]


class HierarchicalPrincipalTypeDef(BaseValidatorModel):
    PrincipalList: Sequence[PrincipalTypeDef]


class CreateFaqRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    S3Path: S3PathTypeDef
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FileFormat: Optional[FaqFileFormatType] = None
    ClientToken: Optional[str] = None
    LanguageCode: Optional[str] = None


class CreateQuerySuggestionsBlockListRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    SourceS3Path: S3PathTypeDef
    RoleArn: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateThesaurusRequestTypeDef(BaseValidatorModel):
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


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateFeaturedResultsSetRequestTypeDef(BaseValidatorModel):
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


class UpdateFeaturedResultsSetRequestTypeDef(BaseValidatorModel):
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


class DataSourceSummaryTypeDef(BaseValidatorModel):
    pass


class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[DataSourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class DocumentAttributeConditionOutputTypeDef(BaseValidatorModel):
    ConditionDocumentAttributeKey: str
    Operator: ConditionOperatorType
    ConditionOnValue: Optional[DocumentAttributeValueOutputTypeDef] = None


class DocumentAttributeOutputTypeDef(BaseValidatorModel):
    Key: str
    Value: DocumentAttributeValueOutputTypeDef


class DocumentAttributeTargetOutputTypeDef(BaseValidatorModel):
    TargetDocumentAttributeKey: Optional[str] = None
    TargetDocumentAttributeValueDeletion: Optional[bool] = None
    TargetDocumentAttributeValue: Optional[DocumentAttributeValueOutputTypeDef] = None


class DocumentAttributeValueCountPairTypeDef(BaseValidatorModel):
    DocumentAttributeValue: Optional[DocumentAttributeValueOutputTypeDef] = None
    Count: Optional[int] = None
    FacetResults: Optional[List[Dict[str, Any]]] = None


class S3DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    BucketName: str
    InclusionPrefixes: Optional[List[str]] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    DocumentsMetadataConfiguration: Optional[DocumentsMetadataConfigurationTypeDef] = None
    AccessControlListConfiguration: Optional[AccessControlListConfigurationTypeDef] = None


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


class ExperienceConfigurationOutputTypeDef(BaseValidatorModel):
    ContentSourceConfiguration: Optional[ContentSourceConfigurationOutputTypeDef] = None
    UserIdentityConfiguration: Optional[UserIdentityConfigurationTypeDef] = None


class ExperienceConfigurationTypeDef(BaseValidatorModel):
    ContentSourceConfiguration: Optional[ContentSourceConfigurationTypeDef] = None
    UserIdentityConfiguration: Optional[UserIdentityConfigurationTypeDef] = None


class ListFaqsResponseTypeDef(BaseValidatorModel):
    FaqSummaryItems: List[FaqSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFeaturedResultsSetsResponseTypeDef(BaseValidatorModel):
    FeaturedResultsSetSummaryItems: List[FeaturedResultsSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetSnapshotsResponseTypeDef(BaseValidatorModel):
    SnapShotTimeFilter: TimeRangeOutputTypeDef
    SnapshotsDataHeader: List[str]
    SnapshotsData: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GroupMembersTypeDef(BaseValidatorModel):
    MemberGroups: Optional[Sequence[MemberGroupTypeDef]] = None
    MemberUsers: Optional[Sequence[MemberUserTypeDef]] = None
    S3PathforGroupMembers: Optional[S3PathTypeDef] = None


class ListGroupsOlderThanOrderingIdResponseTypeDef(BaseValidatorModel):
    GroupsSummaries: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIndicesResponseTypeDef(BaseValidatorModel):
    IndexConfigurationSummaryItems: List[IndexConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IndexStatisticsTypeDef(BaseValidatorModel):
    FaqStatistics: FaqStatisticsTypeDef
    TextDocumentStatistics: TextDocumentStatisticsTypeDef


class UserTokenConfigurationTypeDef(BaseValidatorModel):
    JwtTokenTypeConfiguration: Optional[JwtTokenTypeConfigurationTypeDef] = None
    JsonTokenTypeConfiguration: Optional[JsonTokenTypeConfigurationTypeDef] = None


class ListEntityPersonasResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[PersonasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListQuerySuggestionsBlockListsResponseTypeDef(BaseValidatorModel):
    BlockListSummaryItems: List[QuerySuggestionsBlockListSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListThesauriResponseTypeDef(BaseValidatorModel):
    ThesaurusSummaryItems: List[ThesaurusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UrlsOutputTypeDef(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfigurationOutputTypeDef] = None
    SiteMapsConfiguration: Optional[SiteMapsConfigurationOutputTypeDef] = None


class UrlsTypeDef(BaseValidatorModel):
    SeedUrlConfiguration: Optional[SeedUrlConfigurationTypeDef] = None
    SiteMapsConfiguration: Optional[SiteMapsConfigurationTypeDef] = None


class TableRowTypeDef(BaseValidatorModel):
    Cells: Optional[List[TableCellTypeDef]] = None


class DatabaseConfigurationOutputTypeDef(BaseValidatorModel):
    DatabaseEngineType: DatabaseEngineTypeType
    ConnectionConfiguration: ConnectionConfigurationTypeDef
    ColumnConfiguration: ColumnConfigurationOutputTypeDef
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None
    SqlConfiguration: Optional[SqlConfigurationTypeDef] = None


class DatabaseConfigurationTypeDef(BaseValidatorModel):
    DatabaseEngineType: DatabaseEngineTypeType
    ConnectionConfiguration: ConnectionConfigurationTypeDef
    ColumnConfiguration: ColumnConfigurationTypeDef
    VpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None
    SqlConfiguration: Optional[SqlConfigurationTypeDef] = None


class SalesforceKnowledgeArticleConfigurationOutputTypeDef(BaseValidatorModel):
    IncludedStates: List[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[ SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef ] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[ List[SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef] ] = None


class SalesforceKnowledgeArticleConfigurationTypeDef(BaseValidatorModel):
    IncludedStates: Sequence[SalesforceKnowledgeArticleStateType]
    StandardKnowledgeArticleTypeConfiguration: Optional[ SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef ] = None
    CustomKnowledgeArticleTypeConfigurations: Optional[ Sequence[SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef] ] = None


class ServiceNowConfigurationOutputTypeDef(BaseValidatorModel):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionTypeType
    KnowledgeArticleConfiguration: Optional[ServiceNowKnowledgeArticleConfigurationOutputTypeDef] = None
    ServiceCatalogConfiguration: Optional[ServiceNowServiceCatalogConfigurationOutputTypeDef] = None
    AuthenticationType: Optional[ServiceNowAuthenticationTypeType] = None


class ServiceNowConfigurationTypeDef(BaseValidatorModel):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionTypeType
    KnowledgeArticleConfiguration: Optional[ServiceNowKnowledgeArticleConfigurationTypeDef] = None
    ServiceCatalogConfiguration: Optional[ServiceNowServiceCatalogConfigurationTypeDef] = None
    AuthenticationType: Optional[ServiceNowAuthenticationTypeType] = None


class OneDriveConfigurationOutputTypeDef(BaseValidatorModel):
    TenantDomain: str
    SecretArn: str
    OneDriveUsers: OneDriveUsersOutputTypeDef
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    FieldMappings: Optional[List[DataSourceToIndexFieldMappingTypeDef]] = None
    DisableLocalGroups: Optional[bool] = None


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


class UpdateQuerySuggestionsConfigRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Mode: Optional[ModeType] = None
    QueryLogLookBackWindowInDays: Optional[int] = None
    IncludeQueriesWithoutUserInformation: Optional[bool] = None
    MinimumNumberOfQueryingUsers: Optional[int] = None
    MinimumQueryCount: Optional[int] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsUpdateConfigTypeDef] = None


class SubmitFeedbackRequestTypeDef(BaseValidatorModel):
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


class ConfluenceConfigurationOutputTypeDef(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    Version: ConfluenceVersionType
    SpaceConfiguration: Optional[ConfluenceSpaceConfigurationOutputTypeDef] = None
    PageConfiguration: Optional[ConfluencePageConfigurationOutputTypeDef] = None
    BlogConfiguration: Optional[ConfluenceBlogConfigurationOutputTypeDef] = None
    AttachmentConfiguration: Optional[ConfluenceAttachmentConfigurationOutputTypeDef] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationOutputTypeDef] = None
    InclusionPatterns: Optional[List[str]] = None
    ExclusionPatterns: Optional[List[str]] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None
    AuthenticationType: Optional[ConfluenceAuthenticationTypeType] = None


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


class DescribeAccessControlConfigurationResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    ErrorMessage: str
    AccessControlList: List[PrincipalTypeDef]
    HierarchicalAccessControlList: List[HierarchicalPrincipalOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFeaturedResultsSetResponseTypeDef(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFeaturedResultsSetResponseTypeDef(BaseValidatorModel):
    FeaturedResultsSet: FeaturedResultsSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataSourceSyncJobsResponseTypeDef(BaseValidatorModel):
    History: List[DataSourceSyncJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListExperiencesResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[ExperiencesSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class HookConfigurationOutputTypeDef(BaseValidatorModel):
    LambdaArn: str
    S3Bucket: str
    InvocationCondition: Optional[DocumentAttributeConditionOutputTypeDef] = None


class RetrieveResultItemTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[str] = None
    Content: Optional[str] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutputTypeDef]] = None
    ScoreAttributes: Optional[ScoreAttributesTypeDef] = None


class SourceDocumentTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    SuggestionAttributes: Optional[List[str]] = None
    AdditionalAttributes: Optional[List[DocumentAttributeOutputTypeDef]] = None


class InlineCustomDocumentEnrichmentConfigurationOutputTypeDef(BaseValidatorModel):
    Condition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    Target: Optional[DocumentAttributeTargetOutputTypeDef] = None
    DocumentContentDeletion: Optional[bool] = None


class FacetResultTypeDef(BaseValidatorModel):
    DocumentAttributeKey: Optional[str] = None
    DocumentAttributeValueType: Optional[DocumentAttributeValueTypeType] = None
    DocumentAttributeValueCountPairs: Optional[List[DocumentAttributeValueCountPairTypeDef]] = None


class ListExperienceEntitiesResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[ExperienceEntitiesSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeExperienceResponseTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: str
    Endpoints: List[ExperienceEndpointTypeDef]
    Configuration: ExperienceConfigurationOutputTypeDef
    CreatedAt: datetime
    UpdatedAt: datetime
    Description: str
    Status: ExperienceStatusType
    RoleArn: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutPrincipalMappingRequestTypeDef(BaseValidatorModel):
    IndexId: str
    GroupId: str
    GroupMembers: GroupMembersTypeDef
    DataSourceId: Optional[str] = None
    OrderingId: Optional[int] = None
    RoleArn: Optional[str] = None


class TextWithHighlightsTypeDef(BaseValidatorModel):
    pass


class AdditionalResultAttributeValueTypeDef(BaseValidatorModel):
    TextWithHighlightsValue: Optional[TextWithHighlightsTypeDef] = None


class ExpandedResultItemTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    DocumentId: Optional[str] = None
    DocumentTitle: Optional[TextWithHighlightsTypeDef] = None
    DocumentExcerpt: Optional[TextWithHighlightsTypeDef] = None
    DocumentURI: Optional[str] = None
    DocumentAttributes: Optional[List[DocumentAttributeOutputTypeDef]] = None


class CreateIndexRequestTypeDef(BaseValidatorModel):
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


class DocumentMetadataConfigurationOutputTypeDef(BaseValidatorModel):
    pass


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
    DocumentMetadataConfigurations: List[DocumentMetadataConfigurationOutputTypeDef]
    IndexStatistics: IndexStatisticsTypeDef
    ErrorMessage: str
    CapacityUnits: CapacityUnitsConfigurationTypeDef
    UserTokenConfigurations: List[UserTokenConfigurationTypeDef]
    UserContextPolicy: UserContextPolicyType
    UserGroupResolutionConfiguration: UserGroupResolutionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RelevanceUnionTypeDef(BaseValidatorModel):
    pass


class DocumentRelevanceConfigurationTypeDef(BaseValidatorModel):
    Name: str
    Relevance: RelevanceUnionTypeDef


class WebCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    Urls: UrlsOutputTypeDef
    CrawlDepth: Optional[int] = None
    MaxLinksPerPage: Optional[int] = None
    MaxContentSizePerPageInMegaBytes: Optional[float] = None
    MaxUrlsPerMinuteCrawlRate: Optional[int] = None
    UrlInclusionPatterns: Optional[List[str]] = None
    UrlExclusionPatterns: Optional[List[str]] = None
    ProxyConfiguration: Optional[ProxyConfigurationTypeDef] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationOutputTypeDef] = None


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


class TableExcerptTypeDef(BaseValidatorModel):
    Rows: Optional[List[TableRowTypeDef]] = None
    TotalNumberOfRows: Optional[int] = None


class SalesforceConfigurationOutputTypeDef(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[ List[SalesforceStandardObjectConfigurationOutputTypeDef] ] = None
    KnowledgeArticleConfiguration: Optional[SalesforceKnowledgeArticleConfigurationOutputTypeDef] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfigurationOutputTypeDef] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[ SalesforceStandardObjectAttachmentConfigurationOutputTypeDef ] = None
    IncludeAttachmentFilePatterns: Optional[List[str]] = None
    ExcludeAttachmentFilePatterns: Optional[List[str]] = None


class SalesforceConfigurationTypeDef(BaseValidatorModel):
    ServerUrl: str
    SecretArn: str
    StandardObjectConfigurations: Optional[ Sequence[SalesforceStandardObjectConfigurationTypeDef] ] = None
    KnowledgeArticleConfiguration: Optional[SalesforceKnowledgeArticleConfigurationTypeDef] = None
    ChatterFeedConfiguration: Optional[SalesforceChatterFeedConfigurationTypeDef] = None
    CrawlAttachments: Optional[bool] = None
    StandardObjectAttachmentConfiguration: Optional[ SalesforceStandardObjectAttachmentConfigurationTypeDef ] = None
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


class DocumentAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class DocumentAttributeTypeDef(BaseValidatorModel):
    Key: str
    Value: DocumentAttributeValueUnionTypeDef


class TimeRangeUnionTypeDef(BaseValidatorModel):
    pass


class ListDataSourceSyncJobsRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeFilter: Optional[TimeRangeUnionTypeDef] = None
    StatusFilter: Optional[DataSourceSyncJobStatusType] = None


class HierarchicalPrincipalUnionTypeDef(BaseValidatorModel):
    pass


class CreateAccessControlConfigurationRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Name: str
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalUnionTypeDef]] = None
    ClientToken: Optional[str] = None


class UpdateAccessControlConfigurationRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalUnionTypeDef]] = None


class RetrieveResultTypeDef(BaseValidatorModel):
    QueryId: str
    ResultItems: List[RetrieveResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CustomDocumentEnrichmentConfigurationOutputTypeDef(BaseValidatorModel):
    InlineConfigurations: Optional[ List[InlineCustomDocumentEnrichmentConfigurationOutputTypeDef] ] = None
    PreExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None
    PostExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None
    RoleArn: Optional[str] = None


class ExperienceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateExperienceRequestTypeDef(BaseValidatorModel):
    Name: str
    IndexId: str
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationUnionTypeDef] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdateExperienceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Configuration: Optional[ExperienceConfigurationUnionTypeDef] = None
    Description: Optional[str] = None


class AdditionalResultAttributeTypeDef(BaseValidatorModel):
    Key: str
    ValueType: Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
    Value: AdditionalResultAttributeValueTypeDef


class CollapsedResultDetailTypeDef(BaseValidatorModel):
    DocumentAttribute: DocumentAttributeOutputTypeDef
    ExpandedResults: Optional[List[ExpandedResultItemTypeDef]] = None


class SuggestionValueTypeDef(BaseValidatorModel):
    pass


class SuggestionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Value: Optional[SuggestionValueTypeDef] = None
    SourceDocuments: Optional[List[SourceDocumentTypeDef]] = None


class GitHubConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    S3Configuration: Optional[S3DataSourceConfigurationOutputTypeDef] = None
    SharePointConfiguration: Optional[SharePointConfigurationOutputTypeDef] = None
    DatabaseConfiguration: Optional[DatabaseConfigurationOutputTypeDef] = None
    SalesforceConfiguration: Optional[SalesforceConfigurationOutputTypeDef] = None
    OneDriveConfiguration: Optional[OneDriveConfigurationOutputTypeDef] = None
    ServiceNowConfiguration: Optional[ServiceNowConfigurationOutputTypeDef] = None
    ConfluenceConfiguration: Optional[ConfluenceConfigurationOutputTypeDef] = None
    GoogleDriveConfiguration: Optional[GoogleDriveConfigurationOutputTypeDef] = None
    WebCrawlerConfiguration: Optional[WebCrawlerConfigurationOutputTypeDef] = None
    WorkDocsConfiguration: Optional[WorkDocsConfigurationOutputTypeDef] = None
    FsxConfiguration: Optional[FsxConfigurationOutputTypeDef] = None
    SlackConfiguration: Optional[SlackConfigurationOutputTypeDef] = None
    BoxConfiguration: Optional[BoxConfigurationOutputTypeDef] = None
    QuipConfiguration: Optional[QuipConfigurationOutputTypeDef] = None
    JiraConfiguration: Optional[JiraConfigurationOutputTypeDef] = None
    GitHubConfiguration: Optional[GitHubConfigurationOutputTypeDef] = None
    AlfrescoConfiguration: Optional[AlfrescoConfigurationOutputTypeDef] = None
    TemplateConfiguration: Optional[TemplateConfigurationOutputTypeDef] = None


class GitHubConfigurationTypeDef(BaseValidatorModel):
    pass


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
    InlineConfigurations: Optional[Sequence[InlineCustomDocumentEnrichmentConfigurationTypeDef]] = None
    PreExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    PostExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    RoleArn: Optional[str] = None


class DocumentMetadataConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateIndexRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    DocumentMetadataConfigurationUpdates: Optional[ Sequence[DocumentMetadataConfigurationUnionTypeDef] ] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None
    UserTokenConfigurations: Optional[Sequence[UserTokenConfigurationTypeDef]] = None
    UserContextPolicy: Optional[UserContextPolicyType] = None
    UserGroupResolutionConfiguration: Optional[UserGroupResolutionConfigurationTypeDef] = None


class GetQuerySuggestionsResponseTypeDef(BaseValidatorModel):
    QuerySuggestionsId: str
    Suggestions: List[SuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DocumentAttributeUnionTypeDef(BaseValidatorModel):
    pass


class AttributeFilterTypeDef(BaseValidatorModel):
    AndAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    OrAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    NotFilter: Optional[Mapping[str, Any]] = None
    EqualsTo: Optional[DocumentAttributeUnionTypeDef] = None
    ContainsAll: Optional[DocumentAttributeUnionTypeDef] = None
    ContainsAny: Optional[DocumentAttributeUnionTypeDef] = None
    GreaterThan: Optional[DocumentAttributeUnionTypeDef] = None
    GreaterThanOrEquals: Optional[DocumentAttributeUnionTypeDef] = None
    LessThan: Optional[DocumentAttributeUnionTypeDef] = None
    LessThanOrEquals: Optional[DocumentAttributeUnionTypeDef] = None


class DocumentInfoTypeDef(BaseValidatorModel):
    DocumentId: str
    Attributes: Optional[Sequence[DocumentAttributeUnionTypeDef]] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class DocumentTypeDef(BaseValidatorModel):
    Id: str
    Title: Optional[str] = None
    Blob: Optional[BlobTypeDef] = None
    S3Path: Optional[S3PathTypeDef] = None
    Attributes: Optional[Sequence[DocumentAttributeUnionTypeDef]] = None
    AccessControlList: Optional[Sequence[PrincipalTypeDef]] = None
    HierarchicalAccessControlList: Optional[Sequence[HierarchicalPrincipalUnionTypeDef]] = None
    ContentType: Optional[ContentTypeType] = None
    AccessControlConfigurationId: Optional[str] = None


class QueryResultItemTypeDef(BaseValidatorModel):
    pass


class FeaturedResultsItemTypeDef(BaseValidatorModel):
    pass


class QueryResultTypeDef(BaseValidatorModel):
    QueryId: str
    ResultItems: List[QueryResultItemTypeDef]
    FacetResults: List[FacetResultTypeDef]
    TotalNumberOfResults: int
    Warnings: List[WarningTypeDef]
    SpellCorrectedQueries: List[SpellCorrectedQueryTypeDef]
    FeaturedResultsItems: List[FeaturedResultsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DataSourceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DataSourceVpcConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CustomDocumentEnrichmentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateDataSourceRequestTypeDef(BaseValidatorModel):
    Id: str
    IndexId: str
    Name: Optional[str] = None
    Configuration: Optional[DataSourceConfigurationUnionTypeDef] = None
    VpcConfiguration: Optional[DataSourceVpcConfigurationUnionTypeDef] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    RoleArn: Optional[str] = None
    LanguageCode: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[ CustomDocumentEnrichmentConfigurationUnionTypeDef ] = None


class AttributeSuggestionsGetConfigTypeDef(BaseValidatorModel):
    SuggestionAttributes: Optional[Sequence[str]] = None
    AdditionalResponseAttributes: Optional[Sequence[str]] = None
    AttributeFilter: Optional[AttributeFilterTypeDef] = None
    UserContext: Optional[UserContextTypeDef] = None


class QueryRequestTypeDef(BaseValidatorModel):
    IndexId: str
    QueryText: Optional[str] = None
    AttributeFilter: Optional[AttributeFilterTypeDef] = None
    Facets: Optional[Sequence[FacetTypeDef]] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    QueryResultTypeFilter: Optional[QueryResultTypeType] = None
    DocumentRelevanceOverrideConfigurations: Optional[ Sequence[DocumentRelevanceConfigurationTypeDef] ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    SortingConfiguration: Optional[SortingConfigurationTypeDef] = None
    SortingConfigurations: Optional[Sequence[SortingConfigurationTypeDef]] = None
    UserContext: Optional[UserContextTypeDef] = None
    VisitorId: Optional[str] = None
    SpellCorrectionConfiguration: Optional[SpellCorrectionConfigurationTypeDef] = None
    CollapseConfiguration: Optional[CollapseConfigurationTypeDef] = None


class RetrieveRequestTypeDef(BaseValidatorModel):
    IndexId: str
    QueryText: str
    AttributeFilter: Optional[AttributeFilterTypeDef] = None
    RequestedDocumentAttributes: Optional[Sequence[str]] = None
    DocumentRelevanceOverrideConfigurations: Optional[ Sequence[DocumentRelevanceConfigurationTypeDef] ] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    UserContext: Optional[UserContextTypeDef] = None


class BatchGetDocumentStatusRequestTypeDef(BaseValidatorModel):
    IndexId: str
    DocumentInfoList: Sequence[DocumentInfoTypeDef]


class BatchPutDocumentRequestTypeDef(BaseValidatorModel):
    IndexId: str
    Documents: Sequence[DocumentTypeDef]
    RoleArn: Optional[str] = None
    CustomDocumentEnrichmentConfiguration: Optional[ CustomDocumentEnrichmentConfigurationUnionTypeDef ] = None


class GetQuerySuggestionsRequestTypeDef(BaseValidatorModel):
    IndexId: str
    QueryText: str
    MaxSuggestionsCount: Optional[int] = None
    SuggestionTypes: Optional[Sequence[SuggestionTypeType]] = None
    AttributeSuggestionsConfig: Optional[AttributeSuggestionsGetConfigTypeDef] = None


