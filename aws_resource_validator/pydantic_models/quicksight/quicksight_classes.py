from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.quicksight.quicksight_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountCustomization(BaseValidatorModel):
    DefaultTheme: Optional[str] = None
    DefaultEmailCustomizationTemplate: Optional[str] = None


class AccountInfo(BaseValidatorModel):
    AccountName: Optional[str] = None
    Edition: Optional[EditionType] = None
    NotificationEmail: Optional[str] = None
    AuthenticationType: Optional[str] = None
    AccountSubscriptionStatus: Optional[str] = None
    IAMIdentityCenterInstanceArn: Optional[str] = None


class AccountSettings(BaseValidatorModel):
    AccountName: Optional[str] = None
    Edition: Optional[EditionType] = None
    DefaultNamespace: Optional[str] = None
    NotificationEmail: Optional[str] = None
    PublicSharingEnabled: Optional[bool] = None
    TerminationProtectionEnabled: Optional[bool] = None


class ActiveIAMPolicyAssignment(BaseValidatorModel):
    AssignmentName: Optional[str] = None
    PolicyArn: Optional[str] = None


class AdHocFilteringOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class AggFunctionOutput(BaseValidatorModel):
    Aggregation: Optional[AggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None
    Period: Optional[TopicTimeGranularityType] = None
    PeriodField: Optional[str] = None


class AggFunction(BaseValidatorModel):
    Aggregation: Optional[AggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None
    Period: Optional[TopicTimeGranularityType] = None
    PeriodField: Optional[str] = None


class AttributeAggregationFunction(BaseValidatorModel):
    SimpleAttributeAggregation: Optional[Literal['UNIQUE_VALUE']] = None
    ValueForMultipleValues: Optional[str] = None


class AggregationPartitionBy(BaseValidatorModel):
    FieldName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None


class ColumnIdentifier(BaseValidatorModel):
    DataSetIdentifier: str
    ColumnName: str


class AmazonElasticsearchParameters(BaseValidatorModel):
    Domain: str


class AmazonOpenSearchParameters(BaseValidatorModel):
    Domain: str


class AssetOptions(BaseValidatorModel):
    Timezone: Optional[str] = None
    WeekStart: Optional[DayOfTheWeekType] = None


class CalculatedField(BaseValidatorModel):
    DataSetIdentifier: str
    Name: str
    Expression: str


class DataSetIdentifierDeclaration(BaseValidatorModel):
    Identifier: str
    DataSetArn: str


class QueryExecutionOptions(BaseValidatorModel):
    QueryExecutionMode: Optional[QueryExecutionModeType] = None


class Entity(BaseValidatorModel):
    Path: Optional[str] = None


class AnalysisSearchFilter(BaseValidatorModel):
    Operator: Optional[FilterOperatorType] = None
    Name: Optional[AnalysisFilterAttributeType] = None
    Value: Optional[str] = None


class DataSetReference(BaseValidatorModel):
    DataSetPlaceholder: str
    DataSetArn: str


class AnalysisSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    AnalysisId: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ResourceStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class AnchorDateConfiguration(BaseValidatorModel):
    AnchorOption: Optional[Literal['NOW']] = None
    ParameterName: Optional[str] = None


class Anchor(BaseValidatorModel):
    AnchorType: Optional[Literal['TODAY']] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    Offset: Optional[int] = None


class SharedViewConfigurations(BaseValidatorModel):
    Enabled: bool


class DashboardVisualId(BaseValidatorModel):
    DashboardId: str
    SheetId: str
    VisualId: str


class AnonymousUserGenerativeQnAEmbeddingConfiguration(BaseValidatorModel):
    InitialTopicId: str


class AnonymousUserQSearchBarEmbeddingConfiguration(BaseValidatorModel):
    InitialTopicId: str


class ArcAxisDisplayRange(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class ArcConfiguration(BaseValidatorModel):
    ArcAngle: Optional[float] = None
    ArcThickness: Optional[ArcThicknessOptionsType] = None


class ArcOptions(BaseValidatorModel):
    ArcThickness: Optional[ArcThicknessType] = None


class AssetBundleExportJobAnalysisOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobDashboardOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobDataSetOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobDataSourceOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobDataSourcePropertyToOverrideType]


class AssetBundleExportJobFolderOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobFolderPropertyToOverrideType]


class AssetBundleExportJobRefreshScheduleOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['StartAfterDateTime']]


class AssetBundleExportJobResourceIdOverrideConfiguration(BaseValidatorModel):
    PrefixForAllResources: Optional[bool] = None


class AssetBundleExportJobThemeOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobVPCConnectionOverridePropertiesOutput(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobVPCConnectionPropertyToOverrideType]


class AssetBundleExportJobAnalysisOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobDashboardOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobDataSetOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobDataSourceOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobDataSourcePropertyToOverrideType]


class AssetBundleExportJobFolderOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobFolderPropertyToOverrideType]


class AssetBundleExportJobRefreshScheduleOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['StartAfterDateTime']]


class AssetBundleExportJobThemeOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[Literal['Name']]


class AssetBundleExportJobVPCConnectionOverrideProperties(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobVPCConnectionPropertyToOverrideType]


class AssetBundleExportJobError(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None


class AssetBundleExportJobSummary(BaseValidatorModel):
    JobStatus: Optional[AssetBundleExportJobStatusType] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AssetBundleExportJobId: Optional[str] = None
    IncludeAllDependencies: Optional[bool] = None
    ExportFormat: Optional[AssetBundleExportFormatType] = None
    IncludePermissions: Optional[bool] = None
    IncludeTags: Optional[bool] = None


class AssetBundleExportJobValidationStrategy(BaseValidatorModel):
    StrictModeForAllResources: Optional[bool] = None


class AssetBundleExportJobWarning(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None


class AssetBundleImportJobAnalysisOverrideParameters(BaseValidatorModel):
    AnalysisId: str
    Name: Optional[str] = None


class AssetBundleResourcePermissionsOutput(BaseValidatorModel):
    Principals: List[str]
    Actions: List[str]


class AssetBundleResourcePermissions(BaseValidatorModel):
    Principals: List[str]
    Actions: List[str]


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AssetBundleImportJobDashboardOverrideParameters(BaseValidatorModel):
    DashboardId: str
    Name: Optional[str] = None


class AssetBundleImportJobDataSetOverrideParameters(BaseValidatorModel):
    DataSetId: str
    Name: Optional[str] = None


class AssetBundleImportJobDataSourceCredentialPair(BaseValidatorModel):
    Username: str
    Password: str


class SslProperties(BaseValidatorModel):
    DisableSsl: Optional[bool] = None


class VpcConnectionProperties(BaseValidatorModel):
    VpcConnectionArn: str


class AssetBundleImportJobError(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None


class AssetBundleImportJobFolderOverrideParameters(BaseValidatorModel):
    FolderId: str
    Name: Optional[str] = None
    ParentFolderArn: Optional[str] = None


class AssetBundleImportJobRefreshScheduleOverrideParametersOutput(BaseValidatorModel):
    DataSetId: str
    ScheduleId: str
    StartAfterDateTime: Optional[datetime] = None


class AssetBundleImportJobResourceIdOverrideConfiguration(BaseValidatorModel):
    PrefixForAllResources: Optional[str] = None


class AssetBundleImportJobThemeOverrideParameters(BaseValidatorModel):
    ThemeId: str
    Name: Optional[str] = None


class AssetBundleImportJobVPCConnectionOverrideParametersOutput(BaseValidatorModel):
    VPCConnectionId: str
    Name: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    RoleArn: Optional[str] = None


class AssetBundleImportJobVPCConnectionOverrideParameters(BaseValidatorModel):
    VPCConnectionId: str
    Name: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    RoleArn: Optional[str] = None


class AssetBundleImportJobOverrideValidationStrategy(BaseValidatorModel):
    StrictModeForAllResources: Optional[bool] = None

Timestamp = Union[datetime, str]


class AssetBundleImportJobSummary(BaseValidatorModel):
    JobStatus: Optional[AssetBundleImportJobStatusType] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AssetBundleImportJobId: Optional[str] = None
    FailureAction: Optional[AssetBundleImportFailureActionType] = None


class AssetBundleImportJobWarning(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None


class AssetBundleImportSourceDescription(BaseValidatorModel):
    Body: Optional[str] = None
    S3Uri: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class AthenaParameters(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    RoleArn: Optional[str] = None


class AuroraParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class AuroraPostgreSqlParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class AuthorizedTargetsByService(BaseValidatorModel):
    Service: Optional[ServiceTypeType] = None
    AuthorizedTargets: Optional[List[str]] = None


class AwsIotAnalyticsParameters(BaseValidatorModel):
    DataSetName: str


class DateAxisOptions(BaseValidatorModel):
    MissingDateVisibility: Optional[VisibilityType] = None


class AxisDisplayMinMaxRange(BaseValidatorModel):
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None


class AxisLinearScale(BaseValidatorModel):
    StepCount: Optional[int] = None
    StepSize: Optional[float] = None


class AxisLogarithmicScale(BaseValidatorModel):
    Base: Optional[float] = None


class ItemsLimitConfiguration(BaseValidatorModel):
    ItemsLimit: Optional[int] = None
    OtherCategories: Optional[OtherCategoriesType] = None


class InvalidTopicReviewedAnswer(BaseValidatorModel):
    AnswerId: Optional[str] = None
    Error: Optional[ReviewedAnswerErrorCodeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SucceededTopicReviewedAnswer(BaseValidatorModel):
    AnswerId: Optional[str] = None


class BatchDeleteTopicReviewedAnswerRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    AnswerIds: Optional[List[str]] = None


class BigQueryParameters(BaseValidatorModel):
    ProjectId: str
    DataSetRegion: Optional[str] = None


class BinCountOptions(BaseValidatorModel):
    Value: Optional[int] = None


class BinWidthOptions(BaseValidatorModel):
    Value: Optional[float] = None
    BinCountLimit: Optional[int] = None


class SectionAfterPageBreak(BaseValidatorModel):
    Status: Optional[SectionPageBreakStatusType] = None


class BookmarksConfigurations(BaseValidatorModel):
    Enabled: bool


class BorderStyle(BaseValidatorModel):
    Show: Optional[bool] = None


class BoxPlotStyleOptions(BaseValidatorModel):
    FillStyle: Optional[BoxPlotFillStyleType] = None


class PaginationConfiguration(BaseValidatorModel):
    PageSize: int
    PageNumber: int


class Palette(BaseValidatorModel):
    Foreground: Optional[str] = None
    Background: Optional[str] = None


class BrandSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    BrandId: Optional[str] = None
    BrandName: Optional[str] = None
    Description: Optional[str] = None
    BrandStatus: Optional[BrandStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class CalculatedColumn(BaseValidatorModel):
    ColumnName: str
    ColumnId: str
    Expression: str


class CalculatedMeasureField(BaseValidatorModel):
    FieldId: str
    Expression: str


class CancelIngestionRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    IngestionId: str


class Capabilities(BaseValidatorModel):
    ExportToCsv: Optional[Literal['DENY']] = None
    ExportToExcel: Optional[Literal['DENY']] = None
    CreateAndUpdateThemes: Optional[Literal['DENY']] = None
    AddOrRunAnomalyDetectionForAnalyses: Optional[Literal['DENY']] = None
    ShareAnalyses: Optional[Literal['DENY']] = None
    CreateAndUpdateDatasets: Optional[Literal['DENY']] = None
    ShareDatasets: Optional[Literal['DENY']] = None
    SubscribeDashboardEmailReports: Optional[Literal['DENY']] = None
    CreateAndUpdateDashboardEmailReports: Optional[Literal['DENY']] = None
    ShareDashboards: Optional[Literal['DENY']] = None
    CreateAndUpdateThresholdAlerts: Optional[Literal['DENY']] = None
    RenameSharedFolders: Optional[Literal['DENY']] = None
    CreateSharedFolders: Optional[Literal['DENY']] = None
    CreateAndUpdateDataSources: Optional[Literal['DENY']] = None
    ShareDataSources: Optional[Literal['DENY']] = None
    ViewAccountSPICECapacity: Optional[Literal['DENY']] = None
    CreateSPICEDataset: Optional[Literal['DENY']] = None


class CastColumnTypeOperation(BaseValidatorModel):
    ColumnName: str
    NewColumnType: ColumnDataTypeType
    SubType: Optional[ColumnDataSubTypeType] = None
    Format: Optional[str] = None


class CustomFilterConfiguration(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValue: Optional[str] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    ParameterName: Optional[str] = None


class CustomFilterListConfigurationOutput(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None


class FilterListConfigurationOutput(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    NullOption: Optional[FilterNullOptionType] = None


class CustomFilterListConfiguration(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None


class FilterListConfiguration(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    NullOption: Optional[FilterNullOptionType] = None


class CellValueSynonymOutput(BaseValidatorModel):
    CellValue: Optional[str] = None
    Synonyms: Optional[List[str]] = None


class CellValueSynonym(BaseValidatorModel):
    CellValue: Optional[str] = None
    Synonyms: Optional[List[str]] = None


class SimpleClusterMarker(BaseValidatorModel):
    Color: Optional[str] = None


class CollectiveConstantEntry(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    Value: Optional[str] = None


class CollectiveConstantOutput(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class CollectiveConstant(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class DataColor(BaseValidatorModel):
    Color: Optional[str] = None
    DataValue: Optional[float] = None


class CustomColor(BaseValidatorModel):
    Color: str
    FieldValue: Optional[str] = None
    SpecialValue: Optional[SpecialValueType] = None


class ColumnDescription(BaseValidatorModel):
    Text: Optional[str] = None


class ColumnGroupColumnSchema(BaseValidatorModel):
    Name: Optional[str] = None


class GeoSpatialColumnGroupOutput(BaseValidatorModel):
    Name: str
    Columns: List[str]
    CountryCode: Optional[Literal['US']] = None


class ColumnLevelPermissionRuleOutput(BaseValidatorModel):
    Principals: Optional[List[str]] = None
    ColumnNames: Optional[List[str]] = None


class ColumnLevelPermissionRule(BaseValidatorModel):
    Principals: Optional[List[str]] = None
    ColumnNames: Optional[List[str]] = None


class ColumnSchema(BaseValidatorModel):
    Name: Optional[str] = None
    DataType: Optional[str] = None
    GeographicRole: Optional[str] = None


class ComparativeOrderOutput(BaseValidatorModel):
    UseOrdering: Optional[ColumnOrderingTypeType] = None
    SpecifedOrder: Optional[List[str]] = None
    TreatUndefinedSpecifiedValues: Optional[UndefinedSpecifiedValueTypeType] = None


class ComparativeOrder(BaseValidatorModel):
    UseOrdering: Optional[ColumnOrderingTypeType] = None
    SpecifedOrder: Optional[List[str]] = None
    TreatUndefinedSpecifiedValues: Optional[UndefinedSpecifiedValueTypeType] = None


class ConditionalFormattingSolidColor(BaseValidatorModel):
    Expression: str
    Color: Optional[str] = None


class ConditionalFormattingCustomIconOptions(BaseValidatorModel):
    Icon: Optional[IconType] = None
    UnicodeIcon: Optional[str] = None


class ConditionalFormattingIconDisplayConfiguration(BaseValidatorModel):
    IconDisplayOption: Optional[Literal['ICON_ONLY']] = None


class ConditionalFormattingIconSet(BaseValidatorModel):
    Expression: str
    IconSetType: Optional[ConditionalFormattingIconSetTypeType] = None


class ContextMenuOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class ContributionAnalysisFactor(BaseValidatorModel):
    FieldName: Optional[str] = None


class CreateAccountSubscriptionRequest(BaseValidatorModel):
    AuthenticationMethod: AuthenticationMethodOptionType
    AwsAccountId: str
    AccountName: str
    NotificationEmail: str
    Edition: Optional[EditionType] = None
    ActiveDirectoryName: Optional[str] = None
    Realm: Optional[str] = None
    DirectoryId: Optional[str] = None
    AdminGroup: Optional[List[str]] = None
    AuthorGroup: Optional[List[str]] = None
    ReaderGroup: Optional[List[str]] = None
    AdminProGroup: Optional[List[str]] = None
    AuthorProGroup: Optional[List[str]] = None
    ReaderProGroup: Optional[List[str]] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    EmailAddress: Optional[str] = None
    ContactNumber: Optional[str] = None
    IAMIdentityCenterInstanceArn: Optional[str] = None


class SignupResponse(BaseValidatorModel):
    IAMUser: Optional[bool] = None
    userLoginName: Optional[str] = None
    accountName: Optional[str] = None
    directoryType: Optional[str] = None


class ValidationStrategy(BaseValidatorModel):
    Mode: ValidationStrategyModeType


class DataSetUsageConfiguration(BaseValidatorModel):
    DisableUseAsDirectQuerySource: Optional[bool] = None
    DisableUseAsImportedSource: Optional[bool] = None


class RowLevelPermissionDataSet(BaseValidatorModel):
    Arn: str
    PermissionPolicy: RowLevelPermissionPolicyType
    Namespace: Optional[str] = None
    FormatVersion: Optional[RowLevelPermissionFormatVersionType] = None
    Status: Optional[StatusType] = None


class CreateFolderMembershipRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    MemberId: str
    MemberType: MemberTypeType


class FolderMember(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None


class CreateGroupMembershipRequest(BaseValidatorModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str


class GroupMember(BaseValidatorModel):
    Arn: Optional[str] = None
    MemberName: Optional[str] = None


class CreateGroupRequest(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    Description: Optional[str] = None


class Group(BaseValidatorModel):
    Arn: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    PrincipalId: Optional[str] = None


class CreateIAMPolicyAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    AssignmentStatus: AssignmentStatusType
    Namespace: str
    PolicyArn: Optional[str] = None
    Identities: Optional[Dict[str, List[str]]] = None


class CreateIngestionRequest(BaseValidatorModel):
    DataSetId: str
    IngestionId: str
    AwsAccountId: str
    IngestionType: Optional[IngestionTypeType] = None


class CreateRoleMembershipRequest(BaseValidatorModel):
    MemberName: str
    AwsAccountId: str
    Namespace: str
    Role: RoleType


class CreateTemplateAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str
    TemplateVersionNumber: int


class TemplateAlias(BaseValidatorModel):
    AliasName: Optional[str] = None
    Arn: Optional[str] = None
    TemplateVersionNumber: Optional[int] = None


class CreateThemeAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str
    ThemeVersionNumber: int


class ThemeAlias(BaseValidatorModel):
    Arn: Optional[str] = None
    AliasName: Optional[str] = None
    ThemeVersionNumber: Optional[int] = None


class DecimalPlacesConfiguration(BaseValidatorModel):
    DecimalPlaces: int


class NegativeValueConfiguration(BaseValidatorModel):
    DisplayMode: NegativeValueDisplayModeType


class NullValueFormatConfiguration(BaseValidatorModel):
    NullString: str


class LocalNavigationConfiguration(BaseValidatorModel):
    TargetSheetId: str


class CustomActionURLOperation(BaseValidatorModel):
    URLTemplate: str
    URLTarget: URLTargetConfigurationType


class CustomNarrativeOptions(BaseValidatorModel):
    Narrative: str


class CustomParameterValuesOutput(BaseValidatorModel):
    StringValues: Optional[List[str]] = None
    IntegerValues: Optional[List[int]] = None
    DecimalValues: Optional[List[float]] = None
    DateTimeValues: Optional[List[datetime]] = None


class InputColumn(BaseValidatorModel):
    Name: str
    Type: InputColumnDataTypeType
    SubType: Optional[ColumnDataSubTypeType] = None


class DataPointDrillUpDownOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class DataPointMenuLabelOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class DataPointTooltipOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class ExportToCSVOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class ExportWithHiddenFieldsOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class SheetControlsOption(BaseValidatorModel):
    VisibilityState: Optional[DashboardUIStateType] = None


class SheetLayoutElementMaximizationOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class VisualAxisSortOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class VisualMenuOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class DashboardSearchFilter(BaseValidatorModel):
    Operator: FilterOperatorType
    Name: Optional[DashboardFilterAttributeType] = None
    Value: Optional[str] = None


class DashboardSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    DashboardId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    PublishedVersionNumber: Optional[int] = None
    LastPublishedTime: Optional[datetime] = None


class DashboardVersionSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    SourceEntityArn: Optional[str] = None
    Description: Optional[str] = None


class ExportHiddenFieldsOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class DashboardVisualResult(BaseValidatorModel):
    DashboardId: Optional[str] = None
    DashboardName: Optional[str] = None
    SheetId: Optional[str] = None
    SheetName: Optional[str] = None
    VisualId: Optional[str] = None
    VisualTitle: Optional[str] = None
    VisualSubtitle: Optional[str] = None
    DashboardUrl: Optional[str] = None


class DataAggregation(BaseValidatorModel):
    DatasetRowDateGranularity: Optional[TopicTimeGranularityType] = None
    DefaultDateColumnName: Optional[str] = None


class DataBarsOptions(BaseValidatorModel):
    FieldId: str
    PositiveColor: Optional[str] = None
    NegativeColor: Optional[str] = None


class DataColorPaletteOutput(BaseValidatorModel):
    Colors: Optional[List[str]] = None
    MinMaxGradient: Optional[List[str]] = None
    EmptyFillColor: Optional[str] = None


class DataColorPalette(BaseValidatorModel):
    Colors: Optional[List[str]] = None
    MinMaxGradient: Optional[List[str]] = None
    EmptyFillColor: Optional[str] = None


class DataPathLabelType(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldValue: Optional[str] = None
    Visibility: Optional[VisibilityType] = None


class FieldLabelType(BaseValidatorModel):
    FieldId: Optional[str] = None
    Visibility: Optional[VisibilityType] = None


class MaximumLabelType(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class MinimumLabelType(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class RangeEndsLabelType(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class DataPathType(BaseValidatorModel):
    PivotTableDataPathType: Optional[PivotTableDataPathTypeType] = None


class DataSetSearchFilter(BaseValidatorModel):
    Operator: FilterOperatorType
    Name: DataSetFilterAttributeType
    Value: str


class FieldFolderOutput(BaseValidatorModel):
    description: Optional[str] = None
    columns: Optional[List[str]] = None


class OutputColumn(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[ColumnDataTypeType] = None
    SubType: Optional[ColumnDataSubTypeType] = None


class DataSourceErrorInfo(BaseValidatorModel):
    Type: Optional[DataSourceErrorInfoTypeType] = None
    Message: Optional[str] = None


class DatabricksParameters(BaseValidatorModel):
    Host: str
    Port: int
    SqlEndpointPath: str


class ExasolParameters(BaseValidatorModel):
    Host: str
    Port: int


class JiraParameters(BaseValidatorModel):
    SiteBaseUrl: str


class MariaDbParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class MySqlParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class OracleParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class PostgreSqlParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class PrestoParameters(BaseValidatorModel):
    Host: str
    Port: int
    Catalog: str


class RdsParameters(BaseValidatorModel):
    InstanceId: str
    Database: str


class ServiceNowParameters(BaseValidatorModel):
    SiteBaseUrl: str


class SparkParameters(BaseValidatorModel):
    Host: str
    Port: int


class SqlServerParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class TeradataParameters(BaseValidatorModel):
    Host: str
    Port: int
    Database: str


class TrinoParameters(BaseValidatorModel):
    Host: str
    Port: int
    Catalog: str


class TwitterParameters(BaseValidatorModel):
    Query: str
    MaxRows: int


class DataSourceSearchFilter(BaseValidatorModel):
    Operator: FilterOperatorType
    Name: DataSourceFilterAttributeType
    Value: str


class DataSourceSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    DataSourceId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class DateTimeDatasetParameterDefaultValuesOutput(BaseValidatorModel):
    StaticValues: Optional[List[datetime]] = None


class RollingDateConfiguration(BaseValidatorModel):
    Expression: str
    DataSetIdentifier: Optional[str] = None


class DateTimeValueWhenUnsetConfigurationOutput(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[datetime] = None


class MappedDataSetParameter(BaseValidatorModel):
    DataSetIdentifier: str
    DataSetParameterName: str


class DateTimeParameterOutput(BaseValidatorModel):
    Name: str
    Values: List[datetime]


class SheetControlInfoIconLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    InfoIconText: Optional[str] = None


class DecimalDatasetParameterDefaultValuesOutput(BaseValidatorModel):
    StaticValues: Optional[List[float]] = None


class DecimalDatasetParameterDefaultValues(BaseValidatorModel):
    StaticValues: Optional[List[float]] = None


class DecimalValueWhenUnsetConfiguration(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[float] = None


class DecimalParameterOutput(BaseValidatorModel):
    Name: str
    Values: List[float]


class DecimalParameter(BaseValidatorModel):
    Name: str
    Values: List[float]


class FilterSelectableValuesOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class FilterSelectableValues(BaseValidatorModel):
    Values: Optional[List[str]] = None


class DeleteAccountCustomizationRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: Optional[str] = None


class DeleteAccountSubscriptionRequest(BaseValidatorModel):
    AwsAccountId: str


class DeleteAnalysisRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None


class DeleteBrandAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str


class DeleteBrandRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandId: str


class DeleteCustomPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    CustomPermissionsName: str


class DeleteDashboardRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None


class DeleteDataSetRefreshPropertiesRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str


class DeleteDataSetRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str


class DeleteDataSourceRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str


class DeleteDefaultQBusinessApplicationRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: Optional[str] = None


class DeleteFolderMembershipRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    MemberId: str
    MemberType: MemberTypeType


class DeleteFolderRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str


class DeleteGroupMembershipRequest(BaseValidatorModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str


class DeleteGroupRequest(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str


class DeleteIAMPolicyAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str


class DeleteIdentityPropagationConfigRequest(BaseValidatorModel):
    AwsAccountId: str
    Service: ServiceTypeType


class DeleteNamespaceRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str


class DeleteRefreshScheduleRequest(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    ScheduleId: str


class DeleteRoleCustomPermissionRequest(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str


class DeleteRoleMembershipRequest(BaseValidatorModel):
    MemberName: str
    Role: RoleType
    AwsAccountId: str
    Namespace: str


class DeleteTemplateAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str


class DeleteTemplateRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None


class DeleteThemeAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str


class DeleteThemeRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    VersionNumber: Optional[int] = None


class DeleteTopicRefreshScheduleRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str


class DeleteTopicRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str


class DeleteUserByPrincipalIdRequest(BaseValidatorModel):
    PrincipalId: str
    AwsAccountId: str
    Namespace: str


class DeleteUserCustomPermissionRequest(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str


class DeleteUserRequest(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str


class DeleteVPCConnectionRequest(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str


class DescribeAccountCustomizationRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: Optional[str] = None
    Resolved: Optional[bool] = None


class DescribeAccountSettingsRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeAccountSubscriptionRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeAnalysisDefinitionRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str


class DescribeAnalysisPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str


class ResourcePermissionOutput(BaseValidatorModel):
    Principal: str
    Actions: List[str]


class DescribeAnalysisRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str


class DescribeAssetBundleExportJobRequest(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleExportJobId: str


class DescribeAssetBundleImportJobRequest(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleImportJobId: str


class DescribeBrandAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeBrandPublishedVersionRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandId: str


class DescribeBrandRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandId: str
    VersionId: Optional[str] = None


class DescribeCustomPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    CustomPermissionsName: str


class DescribeDashboardDefinitionRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None


class DescribeDashboardPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str


class DescribeDashboardRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None


class DescribeDashboardSnapshotJobRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str


class DescribeDashboardSnapshotJobResultRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str


class SnapshotJobErrorInfo(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[str] = None


class DescribeDashboardsQAConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeDataSetPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str


class DescribeDataSetRefreshPropertiesRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str


class DescribeDataSetRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str


class DescribeDataSourcePermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str


class DescribeDataSourceRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str


class DescribeDefaultQBusinessApplicationRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeFolderPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFolderRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str


class DescribeFolderResolvedPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Folder(BaseValidatorModel):
    FolderId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    FolderPath: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SharingModel: Optional[SharingModelType] = None


class DescribeGroupMembershipRequest(BaseValidatorModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str


class DescribeGroupRequest(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str


class DescribeIAMPolicyAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str


class IAMPolicyAssignment(BaseValidatorModel):
    AwsAccountId: Optional[str] = None
    AssignmentId: Optional[str] = None
    AssignmentName: Optional[str] = None
    PolicyArn: Optional[str] = None
    Identities: Optional[Dict[str, List[str]]] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None


class DescribeIngestionRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    IngestionId: str


class DescribeIpRestrictionRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeKeyRegistrationRequest(BaseValidatorModel):
    AwsAccountId: str
    DefaultKeyOnly: Optional[bool] = None


class RegisteredCustomerManagedKey(BaseValidatorModel):
    KeyArn: Optional[str] = None
    DefaultKey: Optional[bool] = None


class DescribeNamespaceRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str


class DescribeQPersonalizationConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeQuickSightQSearchConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str


class DescribeRefreshScheduleRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    ScheduleId: str


class DescribeRoleCustomPermissionRequest(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str


class DescribeTemplateAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str


class DescribeTemplateDefinitionRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None


class DescribeTemplatePermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str


class DescribeTemplateRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None


class DescribeThemeAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str


class DescribeThemePermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str


class DescribeThemeRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None


class DescribeTopicPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str


class DescribeTopicRefreshRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    RefreshId: str


class TopicRefreshDetails(BaseValidatorModel):
    RefreshArn: Optional[str] = None
    RefreshId: Optional[str] = None
    RefreshStatus: Optional[TopicRefreshStatusType] = None


class DescribeTopicRefreshScheduleRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str


class TopicRefreshScheduleOutput(BaseValidatorModel):
    IsEnabled: bool
    BasedOnSpiceSchedule: bool
    StartingAt: Optional[datetime] = None
    Timezone: Optional[str] = None
    RepeatAt: Optional[str] = None
    TopicScheduleType: Optional[TopicScheduleTypeType] = None


class DescribeTopicRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str


class DescribeUserRequest(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str


class User(BaseValidatorModel):
    Arn: Optional[str] = None
    UserName: Optional[str] = None
    Email: Optional[str] = None
    Role: Optional[UserRoleType] = None
    IdentityType: Optional[IdentityTypeType] = None
    Active: Optional[bool] = None
    PrincipalId: Optional[str] = None
    CustomPermissionsName: Optional[str] = None
    ExternalLoginFederationProviderType: Optional[str] = None
    ExternalLoginFederationProviderUrl: Optional[str] = None
    ExternalLoginId: Optional[str] = None


class DescribeVPCConnectionRequest(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str


class NegativeFormat(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None


class DonutCenterOptions(BaseValidatorModel):
    LabelVisibility: Optional[VisibilityType] = None


class ListControlSelectAllOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class ErrorInfo(BaseValidatorModel):
    Type: Optional[IngestionErrorTypeType] = None
    Message: Optional[str] = None


class ExcludePeriodConfiguration(BaseValidatorModel):
    Amount: int
    Granularity: TimeGranularityType
    Status: Optional[WidgetStatusType] = None


class FailedKeyRegistrationEntry(BaseValidatorModel):
    Message: str
    StatusCode: int
    SenderFault: bool
    KeyArn: Optional[str] = None


class FieldFolder(BaseValidatorModel):
    description: Optional[str] = None
    columns: Optional[List[str]] = None


class FieldSort(BaseValidatorModel):
    FieldId: str
    Direction: SortDirectionType


class FieldTooltipItem(BaseValidatorModel):
    FieldId: str
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    TooltipTarget: Optional[TooltipTargetType] = None


class GeospatialMapStyleOptions(BaseValidatorModel):
    BaseMapStyle: Optional[BaseMapStyleTypeType] = None


class Identifier(BaseValidatorModel):
    Identity: str


class SameSheetTargetVisualConfigurationOutput(BaseValidatorModel):
    TargetVisuals: Optional[List[str]] = None
    TargetVisualOptions: Optional[Literal['ALL_VISUALS']] = None


class SameSheetTargetVisualConfiguration(BaseValidatorModel):
    TargetVisuals: Optional[List[str]] = None
    TargetVisualOptions: Optional[Literal['ALL_VISUALS']] = None


class FilterOperation(BaseValidatorModel):
    ConditionExpression: str


class FolderSearchFilter(BaseValidatorModel):
    Operator: Optional[FilterOperatorType] = None
    Name: Optional[FolderFilterAttributeType] = None
    Value: Optional[str] = None


class FolderSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    FolderId: Optional[str] = None
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SharingModel: Optional[SharingModelType] = None


class FontSize(BaseValidatorModel):
    Relative: Optional[RelativeFontSizeType] = None
    Absolute: Optional[str] = None


class FontWeight(BaseValidatorModel):
    Name: Optional[FontWeightNameType] = None


class Font(BaseValidatorModel):
    FontFamily: Optional[str] = None


class TimeBasedForecastProperties(BaseValidatorModel):
    PeriodsForward: Optional[int] = None
    PeriodsBackward: Optional[int] = None
    UpperBoundary: Optional[float] = None
    LowerBoundary: Optional[float] = None
    PredictionInterval: Optional[int] = None
    Seasonality: Optional[int] = None


class WhatIfPointScenarioOutput(BaseValidatorModel):
    Date: datetime
    Value: float


class WhatIfRangeScenarioOutput(BaseValidatorModel):
    StartDate: datetime
    EndDate: datetime
    Value: float


class FreeFormLayoutScreenCanvasSizeOptions(BaseValidatorModel):
    OptimizedViewPortWidth: str


class FreeFormLayoutElementBackgroundStyle(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None


class FreeFormLayoutElementBorderStyle(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None


class LoadingAnimation(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class GaugeChartColorConfiguration(BaseValidatorModel):
    ForegroundColor: Optional[str] = None
    BackgroundColor: Optional[str] = None


class SessionTag(BaseValidatorModel):
    Key: str
    Value: str


class GeneratedAnswerResult(BaseValidatorModel):
    QuestionText: Optional[str] = None
    AnswerStatus: Optional[GeneratedAnswerStatusType] = None
    TopicId: Optional[str] = None
    TopicName: Optional[str] = None
    Restatement: Optional[str] = None
    QuestionId: Optional[str] = None
    AnswerId: Optional[str] = None
    QuestionUrl: Optional[str] = None


class GeoSpatialColumnGroup(BaseValidatorModel):
    Name: str
    Columns: List[str]
    CountryCode: Optional[Literal['US']] = None


class GeospatialCategoricalDataColor(BaseValidatorModel):
    Color: str
    DataValue: str


class GeospatialCircleRadius(BaseValidatorModel):
    Radius: Optional[float] = None


class GeospatialLineWidth(BaseValidatorModel):
    LineWidth: Optional[float] = None


class GeospatialSolidColor(BaseValidatorModel):
    Color: str
    State: Optional[GeospatialColorStateType] = None


class GeospatialCoordinateBounds(BaseValidatorModel):
    North: float
    South: float
    West: float
    East: float


class GeospatialStaticFileSource(BaseValidatorModel):
    StaticFileId: str


class GeospatialGradientStepColor(BaseValidatorModel):
    Color: str
    DataValue: float


class GeospatialHeatmapDataColor(BaseValidatorModel):
    Color: str


class GeospatialMapStyle(BaseValidatorModel):
    BaseMapStyle: Optional[BaseMapStyleTypeType] = None
    BackgroundColor: Optional[str] = None
    BaseMapVisibility: Optional[VisibilityType] = None


class GeospatialNullSymbolStyle(BaseValidatorModel):
    FillColor: Optional[str] = None
    StrokeColor: Optional[str] = None
    StrokeWidth: Optional[float] = None


class GetDashboardEmbedUrlRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    IdentityType: EmbeddingIdentityTypeType
    SessionLifetimeInMinutes: Optional[int] = None
    UndoRedoDisabled: Optional[bool] = None
    ResetDisabled: Optional[bool] = None
    StatePersistenceEnabled: Optional[bool] = None
    UserArn: Optional[str] = None
    Namespace: Optional[str] = None
    AdditionalDashboardIds: Optional[List[str]] = None


class GetSessionEmbedUrlRequest(BaseValidatorModel):
    AwsAccountId: str
    EntryPoint: Optional[str] = None
    SessionLifetimeInMinutes: Optional[int] = None
    UserArn: Optional[str] = None


class TableBorderOptions(BaseValidatorModel):
    Color: Optional[str] = None
    Thickness: Optional[int] = None
    Style: Optional[TableBorderStyleType] = None


class GradientStop(BaseValidatorModel):
    GradientOffset: float
    DataValue: Optional[float] = None
    Color: Optional[str] = None


class GridLayoutScreenCanvasSizeOptions(BaseValidatorModel):
    ResizeOption: ResizeOptionType
    OptimizedViewPortWidth: Optional[str] = None


class GridLayoutElement(BaseValidatorModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    ColumnSpan: int
    RowSpan: int
    ColumnIndex: Optional[int] = None
    RowIndex: Optional[int] = None


class GroupSearchFilter(BaseValidatorModel):
    Operator: Literal['StartsWith']
    Name: Literal['GROUP_NAME']
    Value: str


class GutterStyle(BaseValidatorModel):
    Show: Optional[bool] = None


class IAMPolicyAssignmentSummary(BaseValidatorModel):
    AssignmentName: Optional[str] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None


class IdentityCenterConfiguration(BaseValidatorModel):
    EnableIdentityPropagation: Optional[bool] = None


class ImageSource(BaseValidatorModel):
    PublicUrl: Optional[str] = None
    S3Uri: Optional[str] = None


class ImageMenuOption(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None


class LookbackWindow(BaseValidatorModel):
    ColumnName: str
    Size: int
    SizeUnit: LookbackWindowSizeUnitType


class QueueInfo(BaseValidatorModel):
    WaitingOnIngestion: str
    QueuedIngestion: str


class RowInfo(BaseValidatorModel):
    RowsIngested: Optional[int] = None
    RowsDropped: Optional[int] = None
    TotalRowsInDataset: Optional[int] = None


class IntegerDatasetParameterDefaultValuesOutput(BaseValidatorModel):
    StaticValues: Optional[List[int]] = None


class IntegerDatasetParameterDefaultValues(BaseValidatorModel):
    StaticValues: Optional[List[int]] = None


class IntegerValueWhenUnsetConfiguration(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[int] = None


class IntegerParameterOutput(BaseValidatorModel):
    Name: str
    Values: List[int]


class IntegerParameter(BaseValidatorModel):
    Name: str
    Values: List[int]


class JoinKeyProperties(BaseValidatorModel):
    UniqueKey: Optional[bool] = None


class KPISparklineOptions(BaseValidatorModel):
    Type: KPISparklineTypeType
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None
    TooltipVisibility: Optional[VisibilityType] = None


class ProgressBarOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class SecondaryValueOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class TrendArrowOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class KPIVisualStandardLayout(BaseValidatorModel):
    Type: KPIVisualStandardLayoutTypeType


class LineChartLineStyleSettings(BaseValidatorModel):
    LineVisibility: Optional[VisibilityType] = None
    LineInterpolation: Optional[LineInterpolationType] = None
    LineStyle: Optional[LineChartLineStyleType] = None
    LineWidth: Optional[str] = None


class LineChartMarkerStyleSettings(BaseValidatorModel):
    MarkerVisibility: Optional[VisibilityType] = None
    MarkerShape: Optional[LineChartMarkerShapeType] = None
    MarkerSize: Optional[str] = None
    MarkerColor: Optional[str] = None


class MissingDataConfiguration(BaseValidatorModel):
    TreatmentOption: Optional[MissingDataTreatmentOptionType] = None


class ResourcePermission(BaseValidatorModel):
    Principal: str
    Actions: List[str]


class ListAnalysesRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAssetBundleExportJobsRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAssetBundleImportJobsRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBrandsRequest(BaseValidatorModel):
    AwsAccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListControlSearchOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class ListCustomPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDashboardVersionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDashboardsRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataSetsRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataSourcesRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFolderMembersRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MemberIdArnPair(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberArn: Optional[str] = None


class ListFoldersForResourceRequest(BaseValidatorModel):
    AwsAccountId: str
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFoldersRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupMembershipsRequest(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupsRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIAMPolicyAssignmentsForUserRequest(BaseValidatorModel):
    AwsAccountId: str
    UserName: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIAMPolicyAssignmentsRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIdentityPropagationConfigsRequest(BaseValidatorModel):
    AwsAccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListIngestionsRequest(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListNamespacesRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRefreshSchedulesRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str


class ListRoleMembershipsRequest(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListTemplateAliasesRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTemplateVersionsRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TemplateVersionSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    VersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    Status: Optional[ResourceStatusType] = None
    Description: Optional[str] = None


class ListTemplatesRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TemplateSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    TemplateId: Optional[str] = None
    Name: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class ListThemeAliasesRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListThemeVersionsRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ThemeVersionSummary(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Status: Optional[ResourceStatusType] = None


class ListThemesRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Type: Optional[ThemeTypeType] = None


class ThemeSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ThemeId: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class ListTopicRefreshSchedulesRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str


class ListTopicReviewedAnswersRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str


class ListTopicsRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TopicSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    TopicId: Optional[str] = None
    Name: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None


class ListUserGroupsRequest(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListUsersRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListVPCConnectionsRequest(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class LongFormatText(BaseValidatorModel):
    PlainText: Optional[str] = None
    RichText: Optional[str] = None


class ManifestFileLocation(BaseValidatorModel):
    Bucket: str
    Key: str


class MarginStyle(BaseValidatorModel):
    Show: Optional[bool] = None


class NamedEntityDefinitionMetricOutput(BaseValidatorModel):
    Aggregation: Optional[NamedEntityAggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None


class NamedEntityDefinitionMetric(BaseValidatorModel):
    Aggregation: Optional[NamedEntityAggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None


class NamedEntityRef(BaseValidatorModel):
    NamedEntityName: Optional[str] = None


class NamespaceError(BaseValidatorModel):
    Type: Optional[NamespaceErrorTypeType] = None
    Message: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    ErrorMessage: Optional[str] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    NetworkInterfaceId: Optional[str] = None


class NewDefaultValuesOutput(BaseValidatorModel):
    StringStaticValues: Optional[List[str]] = None
    DecimalStaticValues: Optional[List[float]] = None
    DateTimeStaticValues: Optional[List[datetime]] = None
    IntegerStaticValues: Optional[List[int]] = None


class NumericRangeFilterValue(BaseValidatorModel):
    StaticValue: Optional[float] = None
    Parameter: Optional[str] = None


class ThousandSeparatorOptions(BaseValidatorModel):
    Symbol: Optional[NumericSeparatorSymbolType] = None
    Visibility: Optional[VisibilityType] = None
    GroupingStyle: Optional[DigitGroupingStyleType] = None


class PercentileAggregation(BaseValidatorModel):
    PercentileValue: Optional[float] = None


class StringParameterOutput(BaseValidatorModel):
    Name: str
    Values: List[str]


class StringParameter(BaseValidatorModel):
    Name: str
    Values: List[str]


class PercentVisibleRange(BaseValidatorModel):
    From: Optional[float] = None
    To: Optional[float] = None


class UniqueKeyOutput(BaseValidatorModel):
    ColumnNames: List[str]


class UniqueKey(BaseValidatorModel):
    ColumnNames: List[str]


class PivotTableConditionalFormattingScope(BaseValidatorModel):
    Role: Optional[PivotTableConditionalFormattingScopeRoleType] = None


class PivotTablePaginatedReportOptions(BaseValidatorModel):
    VerticalOverflowVisibility: Optional[VisibilityType] = None
    OverflowColumnHeaderVisibility: Optional[VisibilityType] = None


class PivotTableFieldOption(BaseValidatorModel):
    FieldId: str
    CustomLabel: Optional[str] = None
    Visibility: Optional[VisibilityType] = None


class PivotTableFieldSubtotalOptions(BaseValidatorModel):
    FieldId: Optional[str] = None


class PivotTableRowsLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None


class RowAlternateColorOptionsOutput(BaseValidatorModel):
    Status: Optional[WidgetStatusType] = None
    RowAlternateColors: Optional[List[str]] = None
    UsePrimaryBackgroundColor: Optional[WidgetStatusType] = None


class RowAlternateColorOptions(BaseValidatorModel):
    Status: Optional[WidgetStatusType] = None
    RowAlternateColors: Optional[List[str]] = None
    UsePrimaryBackgroundColor: Optional[WidgetStatusType] = None


class PluginVisualItemsLimitConfiguration(BaseValidatorModel):
    ItemsLimit: Optional[int] = None


class PluginVisualProperty(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class PredictQAResultsRequest(BaseValidatorModel):
    AwsAccountId: str
    QueryText: str
    IncludeQuickSightQIndex: Optional[IncludeQuickSightQIndexType] = None
    IncludeGeneratedAnswer: Optional[IncludeGeneratedAnswerType] = None
    MaxTopicsToConsider: Optional[int] = None


class ProjectOperationOutput(BaseValidatorModel):
    ProjectedColumns: List[str]


class ProjectOperation(BaseValidatorModel):
    ProjectedColumns: List[str]


class RadarChartAreaStyleSettings(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class RangeConstant(BaseValidatorModel):
    Minimum: Optional[str] = None
    Maximum: Optional[str] = None


class RedshiftIAMParametersOutput(BaseValidatorModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[List[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None


class RedshiftIAMParameters(BaseValidatorModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[List[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None


class ReferenceLineCustomLabelConfiguration(BaseValidatorModel):
    CustomLabel: str


class ReferenceLineStaticDataConfiguration(BaseValidatorModel):
    Value: float


class ReferenceLineStyleConfiguration(BaseValidatorModel):
    Pattern: Optional[ReferenceLinePatternTypeType] = None
    Color: Optional[str] = None


class ScheduleRefreshOnEntity(BaseValidatorModel):
    DayOfWeek: Optional[DayOfWeekType] = None
    DayOfMonth: Optional[str] = None


class StatePersistenceConfigurations(BaseValidatorModel):
    Enabled: bool


class RegisteredUserGenerativeQnAEmbeddingConfiguration(BaseValidatorModel):
    InitialTopicId: Optional[str] = None


class RegisteredUserQSearchBarEmbeddingConfiguration(BaseValidatorModel):
    InitialTopicId: Optional[str] = None


class RenameColumnOperation(BaseValidatorModel):
    ColumnName: str
    NewColumnName: str


class RestoreAnalysisRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    RestoreToFolders: Optional[bool] = None


class RowLevelPermissionTagRule(BaseValidatorModel):
    TagKey: str
    ColumnName: str
    TagMultiValueDelimiter: Optional[str] = None
    MatchAllValue: Optional[str] = None


class S3BucketConfiguration(BaseValidatorModel):
    BucketName: str
    BucketPrefix: str
    BucketRegion: str


class UploadSettings(BaseValidatorModel):
    Format: Optional[FileFormatType] = None
    StartFromRow: Optional[int] = None
    ContainsHeader: Optional[bool] = None
    TextQualifier: Optional[TextQualifierType] = None
    Delimiter: Optional[str] = None


class TopicSearchFilter(BaseValidatorModel):
    Operator: TopicFilterOperatorType
    Name: TopicFilterAttributeType
    Value: str


class Spacing(BaseValidatorModel):
    Top: Optional[str] = None
    Bottom: Optional[str] = None
    Left: Optional[str] = None
    Right: Optional[str] = None


class SheetVisualScopingConfigurationOutput(BaseValidatorModel):
    SheetId: str
    Scope: FilterVisualScopeType
    VisualIds: Optional[List[str]] = None


class SheetVisualScopingConfiguration(BaseValidatorModel):
    SheetId: str
    Scope: FilterVisualScopeType
    VisualIds: Optional[List[str]] = None


class SemanticEntityTypeOutput(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None


class SemanticEntityType(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None


class SemanticTypeOutput(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None
    TruthyCellValue: Optional[str] = None
    TruthyCellValueSynonyms: Optional[List[str]] = None
    FalseyCellValue: Optional[str] = None
    FalseyCellValueSynonyms: Optional[List[str]] = None


class SemanticType(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None
    TruthyCellValue: Optional[str] = None
    TruthyCellValueSynonyms: Optional[List[str]] = None
    FalseyCellValue: Optional[str] = None
    FalseyCellValueSynonyms: Optional[List[str]] = None


class SheetTextBox(BaseValidatorModel):
    SheetTextBoxId: str
    Content: Optional[str] = None


class SheetElementConfigurationOverrides(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class SheetImageScalingConfiguration(BaseValidatorModel):
    ScalingType: Optional[SheetImageScalingTypeType] = None


class SheetImageStaticFileSource(BaseValidatorModel):
    StaticFileId: str


class SheetImageTooltipText(BaseValidatorModel):
    PlainText: Optional[str] = None


class ShortFormatText(BaseValidatorModel):
    PlainText: Optional[str] = None
    RichText: Optional[str] = None


class YAxisOptions(BaseValidatorModel):
    YAxis: Literal['PRIMARY_Y_AXIS']


class Slot(BaseValidatorModel):
    SlotId: Optional[str] = None
    VisualId: Optional[str] = None


class SmallMultiplesAxisProperties(BaseValidatorModel):
    Scale: Optional[SmallMultiplesAxisScaleType] = None
    Placement: Optional[SmallMultiplesAxisPlacementType] = None


class SnapshotAnonymousUserRedacted(BaseValidatorModel):
    RowLevelPermissionTagKeys: Optional[List[str]] = None


class SnapshotFileSheetSelectionOutput(BaseValidatorModel):
    SheetId: str
    SelectionScope: SnapshotFileSheetSelectionScopeType
    VisualIds: Optional[List[str]] = None


class SnapshotFileSheetSelection(BaseValidatorModel):
    SheetId: str
    SelectionScope: SnapshotFileSheetSelectionScopeType
    VisualIds: Optional[List[str]] = None


class SnapshotJobResultErrorInfo(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[str] = None


class StartDashboardSnapshotJobScheduleRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    ScheduleId: str


class StaticFileS3SourceOptions(BaseValidatorModel):
    BucketName: str
    ObjectKey: str
    Region: str


class StaticFileUrlSourceOptions(BaseValidatorModel):
    Url: str


class StringDatasetParameterDefaultValuesOutput(BaseValidatorModel):
    StaticValues: Optional[List[str]] = None


class StringDatasetParameterDefaultValues(BaseValidatorModel):
    StaticValues: Optional[List[str]] = None


class StringValueWhenUnsetConfiguration(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[str] = None


class TableStyleTarget(BaseValidatorModel):
    CellType: StyledCellTypeType


class SuccessfulKeyRegistrationEntry(BaseValidatorModel):
    KeyArn: str
    StatusCode: int


class TableCellImageSizingConfiguration(BaseValidatorModel):
    TableCellImageScalingConfiguration: Optional[TableCellImageScalingConfigurationType] = None


class TablePaginatedReportOptions(BaseValidatorModel):
    VerticalOverflowVisibility: Optional[VisibilityType] = None
    OverflowColumnHeaderVisibility: Optional[VisibilityType] = None


class TableFieldCustomIconContent(BaseValidatorModel):
    Icon: Optional[Literal['LINK']] = None


class TablePinnedFieldOptionsOutput(BaseValidatorModel):
    PinnedLeftFields: Optional[List[str]] = None


class TablePinnedFieldOptions(BaseValidatorModel):
    PinnedLeftFields: Optional[List[str]] = None


class TemplateSourceTemplate(BaseValidatorModel):
    Arn: str


class TextControlPlaceholderOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None


class UIColorPalette(BaseValidatorModel):
    PrimaryForeground: Optional[str] = None
    PrimaryBackground: Optional[str] = None
    SecondaryForeground: Optional[str] = None
    SecondaryBackground: Optional[str] = None
    Accent: Optional[str] = None
    AccentForeground: Optional[str] = None
    Danger: Optional[str] = None
    DangerForeground: Optional[str] = None
    Warning: Optional[str] = None
    WarningForeground: Optional[str] = None
    Success: Optional[str] = None
    SuccessForeground: Optional[str] = None
    Dimension: Optional[str] = None
    DimensionForeground: Optional[str] = None
    Measure: Optional[str] = None
    MeasureForeground: Optional[str] = None


class ThemeError(BaseValidatorModel):
    Type: Optional[Literal['INTERNAL_FAILURE']] = None
    Message: Optional[str] = None


class TopicConfigOptions(BaseValidatorModel):
    QBusinessInsightsEnabled: Optional[bool] = None


class TopicIRComparisonMethod(BaseValidatorModel):
    Type: Optional[ComparisonMethodTypeType] = None
    Period: Optional[TopicTimeGranularityType] = None
    WindowSize: Optional[int] = None


class VisualOptions(BaseValidatorModel):
    type: Optional[str] = None


class TopicSingularFilterConstant(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None


class TotalAggregationFunction(BaseValidatorModel):
    SimpleTotalAggregationFunction: Optional[SimpleTotalAggregationFunctionType] = None


class UntagColumnOperationOutput(BaseValidatorModel):
    ColumnName: str
    TagNames: List[ColumnTagNameType]


class UntagColumnOperation(BaseValidatorModel):
    ColumnName: str
    TagNames: List[ColumnTagNameType]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateAccountSettingsRequest(BaseValidatorModel):
    AwsAccountId: str
    DefaultNamespace: str
    NotificationEmail: Optional[str] = None
    TerminationProtectionEnabled: Optional[bool] = None


class UpdateApplicationWithTokenExchangeGrantRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str


class UpdateBrandAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandArn: str


class UpdateBrandPublishedVersionRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandId: str
    VersionId: str


class UpdateDashboardLinksRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    LinkEntities: List[str]


class UpdateDashboardPublishedVersionRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: int


class UpdateDashboardsQAConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardsQAStatus: DashboardsQAStatusType


class UpdateDefaultQBusinessApplicationRequest(BaseValidatorModel):
    AwsAccountId: str
    ApplicationId: str
    Namespace: Optional[str] = None


class UpdateFolderRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Name: str


class UpdateGroupRequest(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    Description: Optional[str] = None


class UpdateIAMPolicyAssignmentRequest(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    PolicyArn: Optional[str] = None
    Identities: Optional[Dict[str, List[str]]] = None


class UpdateIdentityPropagationConfigRequest(BaseValidatorModel):
    AwsAccountId: str
    Service: ServiceTypeType
    AuthorizedTargets: Optional[List[str]] = None


class UpdateIpRestrictionRequest(BaseValidatorModel):
    AwsAccountId: str
    IpRestrictionRuleMap: Optional[Dict[str, str]] = None
    VpcIdRestrictionRuleMap: Optional[Dict[str, str]] = None
    VpcEndpointIdRestrictionRuleMap: Optional[Dict[str, str]] = None
    Enabled: Optional[bool] = None


class UpdatePublicSharingSettingsRequest(BaseValidatorModel):
    AwsAccountId: str
    PublicSharingEnabled: Optional[bool] = None


class UpdateQPersonalizationConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str
    PersonalizationMode: PersonalizationModeType


class UpdateQuickSightQSearchConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str
    QSearchStatus: QSearchStatusType


class UpdateRoleCustomPermissionRequest(BaseValidatorModel):
    CustomPermissionsName: str
    Role: RoleType
    AwsAccountId: str
    Namespace: str


class UpdateSPICECapacityConfigurationRequest(BaseValidatorModel):
    AwsAccountId: str
    PurchaseMode: PurchaseModeType


class UpdateTemplateAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str
    TemplateVersionNumber: int


class UpdateThemeAliasRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str
    ThemeVersionNumber: int


class UpdateUserCustomPermissionRequest(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    CustomPermissionsName: str


class UpdateUserRequest(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    Email: str
    Role: UserRoleType
    CustomPermissionsName: Optional[str] = None
    UnapplyCustomPermissions: Optional[bool] = None
    ExternalLoginFederationProviderType: Optional[str] = None
    CustomFederationProviderUrl: Optional[str] = None
    ExternalLoginId: Optional[str] = None


class UpdateVPCConnectionRequest(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str
    Name: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    RoleArn: str
    DnsResolvers: Optional[List[str]] = None


class WaterfallChartGroupColorConfiguration(BaseValidatorModel):
    PositiveBarColor: Optional[str] = None
    NegativeBarColor: Optional[str] = None
    TotalBarColor: Optional[str] = None


class WaterfallChartOptions(BaseValidatorModel):
    TotalBarLabel: Optional[str] = None


class WordCloudOptions(BaseValidatorModel):
    WordOrientation: Optional[WordCloudWordOrientationType] = None
    WordScaling: Optional[WordCloudWordScalingType] = None
    CloudLayout: Optional[WordCloudCloudLayoutType] = None
    WordCasing: Optional[WordCloudWordCasingType] = None
    WordPadding: Optional[WordCloudWordPaddingType] = None
    MaximumStringLength: Optional[int] = None


class UpdateAccountCustomizationRequest(BaseValidatorModel):
    AwsAccountId: str
    AccountCustomization: AccountCustomization
    Namespace: Optional[str] = None

AggFunctionUnion = Union[AggFunction, AggFunctionOutput]


class AxisLabelReferenceOptions(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier


class CascadingControlSource(BaseValidatorModel):
    SourceSheetControlId: Optional[str] = None
    ColumnToMatch: Optional[ColumnIdentifier] = None


class CategoryDrillDownFilterOutput(BaseValidatorModel):
    Column: ColumnIdentifier
    CategoryValues: List[str]


class CategoryDrillDownFilter(BaseValidatorModel):
    Column: ColumnIdentifier
    CategoryValues: List[str]


class ContributionAnalysisDefaultOutput(BaseValidatorModel):
    MeasureFieldId: str
    ContributorDimensions: List[ColumnIdentifier]


class ContributionAnalysisDefault(BaseValidatorModel):
    MeasureFieldId: str
    ContributorDimensions: List[ColumnIdentifier]


class DynamicDefaultValue(BaseValidatorModel):
    DefaultValueColumn: ColumnIdentifier
    UserNameColumn: Optional[ColumnIdentifier] = None
    GroupNameColumn: Optional[ColumnIdentifier] = None


class FilterOperationSelectedFieldsConfigurationOutput(BaseValidatorModel):
    SelectedFields: Optional[List[str]] = None
    SelectedFieldOptions: Optional[Literal['ALL_FIELDS']] = None
    SelectedColumns: Optional[List[ColumnIdentifier]] = None


class FilterOperationSelectedFieldsConfiguration(BaseValidatorModel):
    SelectedFields: Optional[List[str]] = None
    SelectedFieldOptions: Optional[Literal['ALL_FIELDS']] = None
    SelectedColumns: Optional[List[ColumnIdentifier]] = None


class NumericEqualityDrillDownFilter(BaseValidatorModel):
    Column: ColumnIdentifier
    Value: float


class ParameterSelectableValuesOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None
    LinkToDataSetColumn: Optional[ColumnIdentifier] = None


class ParameterSelectableValues(BaseValidatorModel):
    Values: Optional[List[str]] = None
    LinkToDataSetColumn: Optional[ColumnIdentifier] = None


class TimeRangeDrillDownFilterOutput(BaseValidatorModel):
    Column: ColumnIdentifier
    RangeMinimum: datetime
    RangeMaximum: datetime
    TimeGranularity: TimeGranularityType


class AnalysisError(BaseValidatorModel):
    Type: Optional[AnalysisErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[Entity]] = None


class DashboardError(BaseValidatorModel):
    Type: Optional[DashboardErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[Entity]] = None


class TemplateError(BaseValidatorModel):
    Type: Optional[TemplateErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[Entity]] = None


class SearchAnalysesRequest(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[AnalysisSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class AnalysisSourceTemplate(BaseValidatorModel):
    DataSetReferences: List[DataSetReference]
    Arn: str


class DashboardSourceTemplate(BaseValidatorModel):
    DataSetReferences: List[DataSetReference]
    Arn: str


class TemplateSourceAnalysis(BaseValidatorModel):
    Arn: str
    DataSetReferences: List[DataSetReference]


class AnonymousUserDashboardFeatureConfigurations(BaseValidatorModel):
    SharedView: Optional[SharedViewConfigurations] = None


class AnonymousUserDashboardVisualEmbeddingConfiguration(BaseValidatorModel):
    InitialDashboardVisualId: DashboardVisualId


class RegisteredUserDashboardVisualEmbeddingConfiguration(BaseValidatorModel):
    InitialDashboardVisualId: DashboardVisualId


class ArcAxisConfiguration(BaseValidatorModel):
    Range: Optional[ArcAxisDisplayRange] = None
    ReserveRange: Optional[int] = None


class AssetBundleCloudFormationOverridePropertyConfigurationOutput(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[AssetBundleExportJobResourceIdOverrideConfiguration] = None
    VPCConnections: Optional[List[AssetBundleExportJobVPCConnectionOverridePropertiesOutput]] = None
    RefreshSchedules: Optional[List[AssetBundleExportJobRefreshScheduleOverridePropertiesOutput]] = None
    DataSources: Optional[List[AssetBundleExportJobDataSourceOverridePropertiesOutput]] = None
    DataSets: Optional[List[AssetBundleExportJobDataSetOverridePropertiesOutput]] = None
    Themes: Optional[List[AssetBundleExportJobThemeOverridePropertiesOutput]] = None
    Analyses: Optional[List[AssetBundleExportJobAnalysisOverridePropertiesOutput]] = None
    Dashboards: Optional[List[AssetBundleExportJobDashboardOverridePropertiesOutput]] = None
    Folders: Optional[List[AssetBundleExportJobFolderOverridePropertiesOutput]] = None


class AssetBundleCloudFormationOverridePropertyConfiguration(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[AssetBundleExportJobResourceIdOverrideConfiguration] = None
    VPCConnections: Optional[List[AssetBundleExportJobVPCConnectionOverrideProperties]] = None
    RefreshSchedules: Optional[List[AssetBundleExportJobRefreshScheduleOverrideProperties]] = None
    DataSources: Optional[List[AssetBundleExportJobDataSourceOverrideProperties]] = None
    DataSets: Optional[List[AssetBundleExportJobDataSetOverrideProperties]] = None
    Themes: Optional[List[AssetBundleExportJobThemeOverrideProperties]] = None
    Analyses: Optional[List[AssetBundleExportJobAnalysisOverrideProperties]] = None
    Dashboards: Optional[List[AssetBundleExportJobDashboardOverrideProperties]] = None
    Folders: Optional[List[AssetBundleExportJobFolderOverrideProperties]] = None


class AssetBundleImportJobAnalysisOverridePermissionsOutput(BaseValidatorModel):
    AnalysisIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutput


class AssetBundleImportJobDataSetOverridePermissionsOutput(BaseValidatorModel):
    DataSetIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutput


class AssetBundleImportJobDataSourceOverridePermissionsOutput(BaseValidatorModel):
    DataSourceIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutput


class AssetBundleImportJobFolderOverridePermissionsOutput(BaseValidatorModel):
    FolderIds: List[str]
    Permissions: Optional[AssetBundleResourcePermissionsOutput] = None


class AssetBundleImportJobThemeOverridePermissionsOutput(BaseValidatorModel):
    ThemeIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutput


class AssetBundleResourceLinkSharingConfigurationOutput(BaseValidatorModel):
    Permissions: Optional[AssetBundleResourcePermissionsOutput] = None


class AssetBundleImportJobAnalysisOverridePermissions(BaseValidatorModel):
    AnalysisIds: List[str]
    Permissions: AssetBundleResourcePermissions


class AssetBundleImportJobDataSetOverridePermissions(BaseValidatorModel):
    DataSetIds: List[str]
    Permissions: AssetBundleResourcePermissions


class AssetBundleImportJobDataSourceOverridePermissions(BaseValidatorModel):
    DataSourceIds: List[str]
    Permissions: AssetBundleResourcePermissions


class AssetBundleImportJobFolderOverridePermissions(BaseValidatorModel):
    FolderIds: List[str]
    Permissions: Optional[AssetBundleResourcePermissions] = None


class AssetBundleImportJobThemeOverridePermissions(BaseValidatorModel):
    ThemeIds: List[str]
    Permissions: AssetBundleResourcePermissions


class AssetBundleResourceLinkSharingConfiguration(BaseValidatorModel):
    Permissions: Optional[AssetBundleResourcePermissions] = None


class AssetBundleImportJobAnalysisOverrideTagsOutput(BaseValidatorModel):
    AnalysisIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobAnalysisOverrideTags(BaseValidatorModel):
    AnalysisIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobDashboardOverrideTagsOutput(BaseValidatorModel):
    DashboardIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobDashboardOverrideTags(BaseValidatorModel):
    DashboardIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobDataSetOverrideTagsOutput(BaseValidatorModel):
    DataSetIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobDataSetOverrideTags(BaseValidatorModel):
    DataSetIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobDataSourceOverrideTagsOutput(BaseValidatorModel):
    DataSourceIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobDataSourceOverrideTags(BaseValidatorModel):
    DataSourceIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobFolderOverrideTagsOutput(BaseValidatorModel):
    FolderIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobFolderOverrideTags(BaseValidatorModel):
    FolderIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobThemeOverrideTagsOutput(BaseValidatorModel):
    ThemeIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobThemeOverrideTags(BaseValidatorModel):
    ThemeIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobVPCConnectionOverrideTagsOutput(BaseValidatorModel):
    VPCConnectionIds: List[str]
    Tags: List[Tag]


class AssetBundleImportJobVPCConnectionOverrideTags(BaseValidatorModel):
    VPCConnectionIds: List[str]
    Tags: List[Tag]


class CreateAccountCustomizationRequest(BaseValidatorModel):
    AwsAccountId: str
    AccountCustomization: AccountCustomization
    Namespace: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateNamespaceRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    IdentityStore: Literal['QUICKSIGHT']
    Tags: Optional[List[Tag]] = None


class CreateVPCConnectionRequest(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str
    Name: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    RoleArn: str
    DnsResolvers: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class RegisterUserRequest(BaseValidatorModel):
    IdentityType: IdentityTypeType
    Email: str
    UserRole: UserRoleType
    AwsAccountId: str
    Namespace: str
    IamArn: Optional[str] = None
    SessionName: Optional[str] = None
    UserName: Optional[str] = None
    CustomPermissionsName: Optional[str] = None
    ExternalLoginFederationProviderType: Optional[str] = None
    CustomFederationProviderUrl: Optional[str] = None
    ExternalLoginId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class AssetBundleImportJobDataSourceCredentials(BaseValidatorModel):
    CredentialPair: Optional[AssetBundleImportJobDataSourceCredentialPair] = None
    SecretArn: Optional[str] = None


class OAuthParameters(BaseValidatorModel):
    TokenProviderUrl: str
    OAuthScope: Optional[str] = None
    IdentityProviderVpcConnectionProperties: Optional[VpcConnectionProperties] = None
    IdentityProviderResourceUri: Optional[str] = None


class AssetBundleImportJobRefreshScheduleOverrideParameters(BaseValidatorModel):
    DataSetId: str
    ScheduleId: str
    StartAfterDateTime: Optional[Timestamp] = None


class CustomParameterValues(BaseValidatorModel):
    StringValues: Optional[List[str]] = None
    IntegerValues: Optional[List[int]] = None
    DecimalValues: Optional[List[float]] = None
    DateTimeValues: Optional[List[Timestamp]] = None


class DateTimeDatasetParameterDefaultValues(BaseValidatorModel):
    StaticValues: Optional[List[Timestamp]] = None


class DateTimeParameter(BaseValidatorModel):
    Name: str
    Values: List[Timestamp]


class DateTimeValueWhenUnsetConfiguration(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[Timestamp] = None


class NewDefaultValues(BaseValidatorModel):
    StringStaticValues: Optional[List[str]] = None
    DecimalStaticValues: Optional[List[float]] = None
    DateTimeStaticValues: Optional[List[Timestamp]] = None
    IntegerStaticValues: Optional[List[int]] = None


class TimeRangeDrillDownFilter(BaseValidatorModel):
    Column: ColumnIdentifier
    RangeMinimum: Timestamp
    RangeMaximum: Timestamp
    TimeGranularity: TimeGranularityType


class TopicRefreshSchedule(BaseValidatorModel):
    IsEnabled: bool
    BasedOnSpiceSchedule: bool
    StartingAt: Optional[Timestamp] = None
    Timezone: Optional[str] = None
    RepeatAt: Optional[str] = None
    TopicScheduleType: Optional[TopicScheduleTypeType] = None


class WhatIfPointScenario(BaseValidatorModel):
    Date: Timestamp
    Value: float


class WhatIfRangeScenario(BaseValidatorModel):
    StartDate: Timestamp
    EndDate: Timestamp
    Value: float


class AssetBundleImportSource(BaseValidatorModel):
    Body: Optional[Blob] = None
    S3Uri: Optional[str] = None


class AxisDisplayRangeOutput(BaseValidatorModel):
    MinMax: Optional[AxisDisplayMinMaxRange] = None
    DataDriven: Optional[Dict[str, Any]] = None


class AxisDisplayRange(BaseValidatorModel):
    MinMax: Optional[AxisDisplayMinMaxRange] = None
    DataDriven: Optional[Dict[str, Any]] = None


class AxisScale(BaseValidatorModel):
    Linear: Optional[AxisLinearScale] = None
    Logarithmic: Optional[AxisLogarithmicScale] = None


class ScatterPlotSortConfiguration(BaseValidatorModel):
    ScatterPlotLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class CancelIngestionResponse(BaseValidatorModel):
    Arn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateAccountCustomizationResponse(BaseValidatorModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomization
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateAnalysisResponse(BaseValidatorModel):
    Arn: str
    AnalysisId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateCustomPermissionsResponse(BaseValidatorModel):
    Status: int
    Arn: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateDashboardResponse(BaseValidatorModel):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateDataSetResponse(BaseValidatorModel):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateDataSourceResponse(BaseValidatorModel):
    Arn: str
    DataSourceId: str
    CreationStatus: ResourceStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateFolderResponse(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateIAMPolicyAssignmentResponse(BaseValidatorModel):
    AssignmentName: str
    AssignmentId: str
    AssignmentStatus: AssignmentStatusType
    PolicyArn: str
    Identities: Dict[str, List[str]]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateIngestionResponse(BaseValidatorModel):
    Arn: str
    IngestionId: str
    IngestionStatus: IngestionStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateNamespaceResponse(BaseValidatorModel):
    Arn: str
    Name: str
    CapacityRegion: str
    CreationStatus: NamespaceStatusType
    IdentityStore: Literal['QUICKSIGHT']
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateRefreshScheduleResponse(BaseValidatorModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateRoleMembershipResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateTemplateResponse(BaseValidatorModel):
    Arn: str
    VersionArn: str
    TemplateId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateThemeResponse(BaseValidatorModel):
    Arn: str
    VersionArn: str
    ThemeId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateTopicRefreshScheduleResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateTopicResponse(BaseValidatorModel):
    Arn: str
    TopicId: str
    RefreshArn: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateVPCConnectionResponse(BaseValidatorModel):
    Arn: str
    VPCConnectionId: str
    CreationStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteAccountCustomizationResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteAccountSubscriptionResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteAnalysisResponse(BaseValidatorModel):
    Status: int
    Arn: str
    AnalysisId: str
    DeletionTime: datetime
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteBrandAssignmentResponse(BaseValidatorModel):
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteBrandResponse(BaseValidatorModel):
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteCustomPermissionsResponse(BaseValidatorModel):
    Status: int
    Arn: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteDashboardResponse(BaseValidatorModel):
    Status: int
    Arn: str
    DashboardId: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteDataSetRefreshPropertiesResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteDataSetResponse(BaseValidatorModel):
    Arn: str
    DataSetId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteDataSourceResponse(BaseValidatorModel):
    Arn: str
    DataSourceId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteDefaultQBusinessApplicationResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteFolderMembershipResponse(BaseValidatorModel):
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteFolderResponse(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteGroupMembershipResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteGroupResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteIAMPolicyAssignmentResponse(BaseValidatorModel):
    AssignmentName: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteIdentityPropagationConfigResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteNamespaceResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteRefreshScheduleResponse(BaseValidatorModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeleteRoleCustomPermissionResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteRoleMembershipResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteTemplateAliasResponse(BaseValidatorModel):
    Status: int
    TemplateId: str
    AliasName: str
    Arn: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteTemplateResponse(BaseValidatorModel):
    RequestId: str
    Arn: str
    TemplateId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteThemeAliasResponse(BaseValidatorModel):
    AliasName: str
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str
    ResponseMetadata: ResponseMetadata


class DeleteThemeResponse(BaseValidatorModel):
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str
    ResponseMetadata: ResponseMetadata


class DeleteTopicRefreshScheduleResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DeleteTopicResponse(BaseValidatorModel):
    Arn: str
    TopicId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteUserByPrincipalIdResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteUserCustomPermissionResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteUserResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DeleteVPCConnectionResponse(BaseValidatorModel):
    Arn: str
    VPCConnectionId: str
    DeletionStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeAccountCustomizationResponse(BaseValidatorModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomization
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeAccountSettingsResponse(BaseValidatorModel):
    AccountSettings: AccountSettings
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeAccountSubscriptionResponse(BaseValidatorModel):
    AccountInfo: AccountInfo
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeBrandAssignmentResponse(BaseValidatorModel):
    RequestId: str
    BrandArn: str
    ResponseMetadata: ResponseMetadata


class DescribeDashboardsQAConfigurationResponse(BaseValidatorModel):
    DashboardsQAStatus: DashboardsQAStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeDefaultQBusinessApplicationResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ApplicationId: str
    ResponseMetadata: ResponseMetadata


class DescribeIpRestrictionResponse(BaseValidatorModel):
    AwsAccountId: str
    IpRestrictionRuleMap: Dict[str, str]
    VpcIdRestrictionRuleMap: Dict[str, str]
    VpcEndpointIdRestrictionRuleMap: Dict[str, str]
    Enabled: bool
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeQPersonalizationConfigurationResponse(BaseValidatorModel):
    PersonalizationMode: PersonalizationModeType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeQuickSightQSearchConfigurationResponse(BaseValidatorModel):
    QSearchStatus: QSearchStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeRoleCustomPermissionResponse(BaseValidatorModel):
    CustomPermissionsName: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class GenerateEmbedUrlForAnonymousUserResponse(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    AnonymousUserArn: str
    ResponseMetadata: ResponseMetadata


class GenerateEmbedUrlForRegisteredUserResponse(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class GenerateEmbedUrlForRegisteredUserWithIdentityResponse(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class GetDashboardEmbedUrlResponse(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class GetSessionEmbedUrlResponse(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class ListAnalysesResponse(BaseValidatorModel):
    AnalysisSummaryList: List[AnalysisSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAssetBundleExportJobsResponse(BaseValidatorModel):
    AssetBundleExportJobSummaryList: List[AssetBundleExportJobSummary]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAssetBundleImportJobsResponse(BaseValidatorModel):
    AssetBundleImportJobSummaryList: List[AssetBundleImportJobSummary]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFoldersForResourceResponse(BaseValidatorModel):
    Status: int
    Folders: List[str]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIAMPolicyAssignmentsForUserResponse(BaseValidatorModel):
    ActiveAssignments: List[ActiveIAMPolicyAssignment]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIdentityPropagationConfigsResponse(BaseValidatorModel):
    Services: List[AuthorizedTargetsByService]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRoleMembershipsResponse(BaseValidatorModel):
    MembersList: List[str]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class PutDataSetRefreshPropertiesResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class RestoreAnalysisResponse(BaseValidatorModel):
    Status: int
    Arn: str
    AnalysisId: str
    RequestId: str
    RestorationFailedFolderArns: List[str]
    ResponseMetadata: ResponseMetadata


class SearchAnalysesResponse(BaseValidatorModel):
    AnalysisSummaryList: List[AnalysisSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartAssetBundleExportJobResponse(BaseValidatorModel):
    Arn: str
    AssetBundleExportJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class StartAssetBundleImportJobResponse(BaseValidatorModel):
    Arn: str
    AssetBundleImportJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class StartDashboardSnapshotJobResponse(BaseValidatorModel):
    Arn: str
    SnapshotJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class StartDashboardSnapshotJobScheduleResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class TagResourceResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UntagResourceResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateAccountCustomizationResponse(BaseValidatorModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomization
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateAccountSettingsResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateAnalysisResponse(BaseValidatorModel):
    Arn: str
    AnalysisId: str
    UpdateStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateApplicationWithTokenExchangeGrantResponse(BaseValidatorModel):
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateBrandAssignmentResponse(BaseValidatorModel):
    RequestId: str
    BrandArn: str
    ResponseMetadata: ResponseMetadata


class UpdateBrandPublishedVersionResponse(BaseValidatorModel):
    RequestId: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


class UpdateCustomPermissionsResponse(BaseValidatorModel):
    Status: int
    Arn: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateDashboardLinksResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    DashboardArn: str
    LinkEntities: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateDashboardPublishedVersionResponse(BaseValidatorModel):
    DashboardId: str
    DashboardArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateDashboardResponse(BaseValidatorModel):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateDashboardsQAConfigurationResponse(BaseValidatorModel):
    DashboardsQAStatus: DashboardsQAStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateDataSetPermissionsResponse(BaseValidatorModel):
    DataSetArn: str
    DataSetId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateDataSetResponse(BaseValidatorModel):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateDataSourcePermissionsResponse(BaseValidatorModel):
    DataSourceArn: str
    DataSourceId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateDataSourceResponse(BaseValidatorModel):
    Arn: str
    DataSourceId: str
    UpdateStatus: ResourceStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateDefaultQBusinessApplicationResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateFolderResponse(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateIAMPolicyAssignmentResponse(BaseValidatorModel):
    AssignmentName: str
    AssignmentId: str
    PolicyArn: str
    Identities: Dict[str, List[str]]
    AssignmentStatus: AssignmentStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateIdentityPropagationConfigResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateIpRestrictionResponse(BaseValidatorModel):
    AwsAccountId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdatePublicSharingSettingsResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateQPersonalizationConfigurationResponse(BaseValidatorModel):
    PersonalizationMode: PersonalizationModeType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateQuickSightQSearchConfigurationResponse(BaseValidatorModel):
    QSearchStatus: QSearchStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateRefreshScheduleResponse(BaseValidatorModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class UpdateRoleCustomPermissionResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateSPICECapacityConfigurationResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateTemplateResponse(BaseValidatorModel):
    TemplateId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateThemeResponse(BaseValidatorModel):
    ThemeId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateTopicRefreshScheduleResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateTopicResponse(BaseValidatorModel):
    TopicId: str
    Arn: str
    RefreshArn: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateUserCustomPermissionResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateVPCConnectionResponse(BaseValidatorModel):
    Arn: str
    VPCConnectionId: str
    UpdateStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class BatchCreateTopicReviewedAnswerResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    SucceededAnswers: List[SucceededTopicReviewedAnswer]
    InvalidAnswers: List[InvalidTopicReviewedAnswer]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class BatchDeleteTopicReviewedAnswerResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    SucceededAnswers: List[SucceededTopicReviewedAnswer]
    InvalidAnswers: List[InvalidTopicReviewedAnswer]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class HistogramBinOptions(BaseValidatorModel):
    SelectedBinType: Optional[HistogramBinTypeType] = None
    BinCount: Optional[BinCountOptions] = None
    BinWidth: Optional[BinWidthOptions] = None
    StartValue: Optional[float] = None


class BodySectionRepeatPageBreakConfiguration(BaseValidatorModel):
    After: Optional[SectionAfterPageBreak] = None


class SectionPageBreakConfiguration(BaseValidatorModel):
    After: Optional[SectionAfterPageBreak] = None


class TileStyle(BaseValidatorModel):
    Border: Optional[BorderStyle] = None


class BoxPlotOptions(BaseValidatorModel):
    StyleOptions: Optional[BoxPlotStyleOptions] = None
    OutlierVisibility: Optional[VisibilityType] = None
    AllDataPointsVisibility: Optional[VisibilityType] = None


class BrandColorPalette(BaseValidatorModel):
    Primary: Optional[Palette] = None
    Secondary: Optional[Palette] = None
    Accent: Optional[Palette] = None
    Measure: Optional[Palette] = None
    Dimension: Optional[Palette] = None
    Success: Optional[Palette] = None
    Info: Optional[Palette] = None
    Warning: Optional[Palette] = None
    Danger: Optional[Palette] = None


class NavbarStyle(BaseValidatorModel):
    GlobalNavbar: Optional[Palette] = None
    ContextualNavbar: Optional[Palette] = None


class ListBrandsResponse(BaseValidatorModel):
    Brands: List[BrandSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateColumnsOperationOutput(BaseValidatorModel):
    Columns: List[CalculatedColumn]


class CreateColumnsOperation(BaseValidatorModel):
    Columns: List[CalculatedColumn]


class CreateCustomPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    CustomPermissionsName: str
    Capabilities: Optional[Capabilities] = None
    Tags: Optional[List[Tag]] = None


class CustomPermissions(BaseValidatorModel):
    Arn: Optional[str] = None
    CustomPermissionsName: Optional[str] = None
    Capabilities: Optional[Capabilities] = None


class UpdateCustomPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    CustomPermissionsName: str
    Capabilities: Optional[Capabilities] = None


class CategoryFilterConfigurationOutput(BaseValidatorModel):
    FilterListConfiguration: Optional[FilterListConfigurationOutput] = None
    CustomFilterListConfiguration: Optional[CustomFilterListConfigurationOutput] = None
    CustomFilterConfiguration: Optional[CustomFilterConfiguration] = None


class CategoryFilterConfiguration(BaseValidatorModel):
    FilterListConfiguration: Optional[FilterListConfiguration] = None
    CustomFilterListConfiguration: Optional[CustomFilterListConfiguration] = None
    CustomFilterConfiguration: Optional[CustomFilterConfiguration] = None


class ClusterMarker(BaseValidatorModel):
    SimpleClusterMarker: Optional[SimpleClusterMarker] = None


class TopicConstantValueOutput(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    Value: Optional[str] = None
    Minimum: Optional[str] = None
    Maximum: Optional[str] = None
    ValueList: Optional[List[CollectiveConstantEntry]] = None


class TopicConstantValue(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    Value: Optional[str] = None
    Minimum: Optional[str] = None
    Maximum: Optional[str] = None
    ValueList: Optional[List[CollectiveConstantEntry]] = None


class TopicCategoryFilterConstantOutput(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None
    CollectiveConstant: Optional[CollectiveConstantOutput] = None


class TopicCategoryFilterConstant(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None
    CollectiveConstant: Optional[CollectiveConstant] = None


class ColorScaleOutput(BaseValidatorModel):
    Colors: List[DataColor]
    ColorFillType: ColorFillTypeType
    NullValueColor: Optional[DataColor] = None


class ColorScale(BaseValidatorModel):
    Colors: List[DataColor]
    ColorFillType: ColorFillTypeType
    NullValueColor: Optional[DataColor] = None


class ColorsConfigurationOutput(BaseValidatorModel):
    CustomColors: Optional[List[CustomColor]] = None


class ColorsConfiguration(BaseValidatorModel):
    CustomColors: Optional[List[CustomColor]] = None


class ColumnTag(BaseValidatorModel):
    ColumnGeographicRole: Optional[GeoSpatialDataRoleType] = None
    ColumnDescription: Optional[ColumnDescription] = None


class ColumnGroupSchemaOutput(BaseValidatorModel):
    Name: Optional[str] = None
    ColumnGroupColumnSchemaList: Optional[List[ColumnGroupColumnSchema]] = None


class ColumnGroupSchema(BaseValidatorModel):
    Name: Optional[str] = None
    ColumnGroupColumnSchemaList: Optional[List[ColumnGroupColumnSchema]] = None


class ColumnGroupOutput(BaseValidatorModel):
    GeoSpatialColumnGroup: Optional[GeoSpatialColumnGroupOutput] = None

ColumnLevelPermissionRuleUnion = Union[ColumnLevelPermissionRule, ColumnLevelPermissionRuleOutput]


class DataSetSchemaOutput(BaseValidatorModel):
    ColumnSchemaList: Optional[List[ColumnSchema]] = None


class DataSetSchema(BaseValidatorModel):
    ColumnSchemaList: Optional[List[ColumnSchema]] = None


class ConditionalFormattingCustomIconCondition(BaseValidatorModel):
    Expression: str
    IconOptions: ConditionalFormattingCustomIconOptions
    Color: Optional[str] = None
    DisplayConfiguration: Optional[ConditionalFormattingIconDisplayConfiguration] = None


class CreateAccountSubscriptionResponse(BaseValidatorModel):
    SignupResponse: SignupResponse
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DataSetSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    DataSetId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ImportMode: Optional[DataSetImportModeType] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSet] = None
    RowLevelPermissionTagConfigurationApplied: Optional[bool] = None
    ColumnLevelPermissionRulesApplied: Optional[bool] = None


class CreateFolderMembershipResponse(BaseValidatorModel):
    Status: int
    FolderMember: FolderMember
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateGroupMembershipResponse(BaseValidatorModel):
    GroupMember: GroupMember
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeGroupMembershipResponse(BaseValidatorModel):
    GroupMember: GroupMember
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ListGroupMembershipsResponse(BaseValidatorModel):
    GroupMemberList: List[GroupMember]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateGroupResponse(BaseValidatorModel):
    Group: Group
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeGroupResponse(BaseValidatorModel):
    Group: Group
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ListGroupsResponse(BaseValidatorModel):
    GroupList: List[Group]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUserGroupsResponse(BaseValidatorModel):
    GroupList: List[Group]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchGroupsResponse(BaseValidatorModel):
    GroupList: List[Group]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateGroupResponse(BaseValidatorModel):
    Group: Group
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CreateTemplateAliasResponse(BaseValidatorModel):
    TemplateAlias: TemplateAlias
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeTemplateAliasResponse(BaseValidatorModel):
    TemplateAlias: TemplateAlias
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class ListTemplateAliasesResponse(BaseValidatorModel):
    TemplateAliasList: List[TemplateAlias]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateTemplateAliasResponse(BaseValidatorModel):
    TemplateAlias: TemplateAlias
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CreateThemeAliasResponse(BaseValidatorModel):
    ThemeAlias: ThemeAlias
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeThemeAliasResponse(BaseValidatorModel):
    ThemeAlias: ThemeAlias
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class ListThemeAliasesResponse(BaseValidatorModel):
    ThemeAliasList: List[ThemeAlias]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateThemeAliasResponse(BaseValidatorModel):
    ThemeAlias: ThemeAlias
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class CustomActionNavigationOperation(BaseValidatorModel):
    LocalNavigationConfiguration: Optional[LocalNavigationConfiguration] = None


class CustomValuesConfigurationOutput(BaseValidatorModel):
    CustomValues: CustomParameterValuesOutput
    IncludeNullValue: Optional[bool] = None


class CustomSqlOutput(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    SqlQuery: str
    Columns: Optional[List[InputColumn]] = None


class CustomSql(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    SqlQuery: str
    Columns: Optional[List[InputColumn]] = None


class RelationalTableOutput(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    InputColumns: List[InputColumn]
    Catalog: Optional[str] = None
    Schema: Optional[str] = None


class RelationalTable(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    InputColumns: List[InputColumn]
    Catalog: Optional[str] = None
    Schema: Optional[str] = None


class VisualInteractionOptions(BaseValidatorModel):
    VisualMenuOption: Optional[VisualMenuOption] = None
    ContextMenuOption: Optional[ContextMenuOption] = None


class SearchDashboardsRequest(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[DashboardSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDashboardsResponse(BaseValidatorModel):
    DashboardSummaryList: List[DashboardSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchDashboardsResponse(BaseValidatorModel):
    DashboardSummaryList: List[DashboardSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDashboardVersionsResponse(BaseValidatorModel):
    DashboardVersionSummaryList: List[DashboardVersionSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DashboardVisualPublishOptions(BaseValidatorModel):
    ExportHiddenFieldsOption: Optional[ExportHiddenFieldsOption] = None


class TableInlineVisualization(BaseValidatorModel):
    DataBars: Optional[DataBarsOptions] = None


class DataLabelType(BaseValidatorModel):
    FieldLabelType: Optional[FieldLabelType] = None
    DataPathLabelType: Optional[DataPathLabelType] = None
    RangeEndsLabelType: Optional[RangeEndsLabelType] = None
    MinimumLabelType: Optional[MinimumLabelType] = None
    MaximumLabelType: Optional[MaximumLabelType] = None


class DataPathValue(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldValue: Optional[str] = None
    DataPathType: Optional[DataPathType] = None


class SearchDataSetsRequest(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[DataSetSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SearchDataSourcesRequest(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[DataSourceSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SearchDataSourcesResponse(BaseValidatorModel):
    DataSourceSummaries: List[DataSourceSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DateTimeDatasetParameterOutput(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultValues: Optional[DateTimeDatasetParameterDefaultValuesOutput] = None


class TimeRangeFilterValueOutput(BaseValidatorModel):
    StaticValue: Optional[datetime] = None
    RollingDate: Optional[RollingDateConfiguration] = None
    Parameter: Optional[str] = None


class TimeRangeFilterValue(BaseValidatorModel):
    StaticValue: Optional[Timestamp] = None
    RollingDate: Optional[RollingDateConfiguration] = None
    Parameter: Optional[str] = None


class DecimalDatasetParameterOutput(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[DecimalDatasetParameterDefaultValuesOutput] = None

DecimalDatasetParameterDefaultValuesUnion = Union[DecimalDatasetParameterDefaultValues, DecimalDatasetParameterDefaultValuesOutput]


class DescribeAnalysisPermissionsResponse(BaseValidatorModel):
    AnalysisId: str
    AnalysisArn: str
    Permissions: List[ResourcePermissionOutput]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeDataSetPermissionsResponse(BaseValidatorModel):
    DataSetArn: str
    DataSetId: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeDataSourcePermissionsResponse(BaseValidatorModel):
    DataSourceArn: str
    DataSourceId: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeFolderPermissionsResponse(BaseValidatorModel):
    Status: int
    FolderId: str
    Arn: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFolderResolvedPermissionsResponse(BaseValidatorModel):
    Status: int
    FolderId: str
    Arn: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeTemplatePermissionsResponse(BaseValidatorModel):
    TemplateId: str
    TemplateArn: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeThemePermissionsResponse(BaseValidatorModel):
    ThemeId: str
    ThemeArn: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeTopicPermissionsResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    Permissions: List[ResourcePermissionOutput]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class LinkSharingConfigurationOutput(BaseValidatorModel):
    Permissions: Optional[List[ResourcePermissionOutput]] = None


class UpdateAnalysisPermissionsResponse(BaseValidatorModel):
    AnalysisArn: str
    AnalysisId: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateFolderPermissionsResponse(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    ResponseMetadata: ResponseMetadata


class UpdateTemplatePermissionsResponse(BaseValidatorModel):
    TemplateId: str
    TemplateArn: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateThemePermissionsResponse(BaseValidatorModel):
    ThemeId: str
    ThemeArn: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateTopicPermissionsResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    Permissions: List[ResourcePermissionOutput]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeFolderPermissionsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFolderResolvedPermissionsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnalysesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetBundleExportJobsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetBundleImportJobsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBrandsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomPermissionsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDashboardVersionsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDashboardsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSetsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourcesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFolderMembersRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFoldersForResourceRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFoldersRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupMembershipsRequestPaginate(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIAMPolicyAssignmentsForUserRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    UserName: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIAMPolicyAssignmentsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIngestionsRequestPaginate(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoleMembershipsRequestPaginate(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplateAliasesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplateVersionsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplatesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThemeVersionsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThemesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Type: Optional[ThemeTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserGroupsRequestPaginate(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchAnalysesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[AnalysisSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchDashboardsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[DashboardSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchDataSetsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[DataSetSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchDataSourcesRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[DataSourceSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFolderResponse(BaseValidatorModel):
    Status: int
    Folder: Folder
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeIAMPolicyAssignmentResponse(BaseValidatorModel):
    IAMPolicyAssignment: IAMPolicyAssignment
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeKeyRegistrationResponse(BaseValidatorModel):
    AwsAccountId: str
    KeyRegistration: List[RegisteredCustomerManagedKey]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateKeyRegistrationRequest(BaseValidatorModel):
    AwsAccountId: str
    KeyRegistration: List[RegisteredCustomerManagedKey]


class DescribeTopicRefreshResponse(BaseValidatorModel):
    RefreshDetails: TopicRefreshDetails
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DescribeTopicRefreshScheduleResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    RefreshSchedule: TopicRefreshScheduleOutput
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class TopicRefreshScheduleSummary(BaseValidatorModel):
    DatasetId: Optional[str] = None
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    RefreshSchedule: Optional[TopicRefreshScheduleOutput] = None


class DescribeUserResponse(BaseValidatorModel):
    User: User
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ListUsersResponse(BaseValidatorModel):
    UserList: List[User]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RegisterUserResponse(BaseValidatorModel):
    User: User
    UserInvitationUrl: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class UpdateUserResponse(BaseValidatorModel):
    User: User
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class DisplayFormatOptions(BaseValidatorModel):
    UseBlankCellFormat: Optional[bool] = None
    BlankCellFormat: Optional[str] = None
    DateFormat: Optional[str] = None
    DecimalSeparator: Optional[TopicNumericSeparatorSymbolType] = None
    GroupingSeparator: Optional[str] = None
    UseGrouping: Optional[bool] = None
    FractionDigits: Optional[int] = None
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    UnitScaler: Optional[NumberScaleType] = None
    NegativeFormat: Optional[NegativeFormat] = None
    CurrencySymbol: Optional[str] = None


class DonutOptions(BaseValidatorModel):
    ArcOptions: Optional[ArcOptions] = None
    DonutCenterOptions: Optional[DonutCenterOptions] = None

FieldFolderUnion = Union[FieldFolder, FieldFolderOutput]


class FilterAggMetrics(BaseValidatorModel):
    MetricOperand: Optional[Identifier] = None
    Function: Optional[AggTypeType] = None
    SortDirection: Optional[TopicSortDirectionType] = None


class TopicSortClause(BaseValidatorModel):
    Operand: Optional[Identifier] = None
    SortDirection: Optional[TopicSortDirectionType] = None


class FilterOperationTargetVisualsConfigurationOutput(BaseValidatorModel):
    SameSheetTargetVisualConfiguration: Optional[SameSheetTargetVisualConfigurationOutput] = None


class FilterOperationTargetVisualsConfiguration(BaseValidatorModel):
    SameSheetTargetVisualConfiguration: Optional[SameSheetTargetVisualConfiguration] = None


class SearchFoldersRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[FolderSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchFoldersRequest(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[FolderSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFoldersResponse(BaseValidatorModel):
    Status: int
    FolderSummaryList: List[FolderSummary]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchFoldersResponse(BaseValidatorModel):
    Status: int
    FolderSummaryList: List[FolderSummary]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FontConfiguration(BaseValidatorModel):
    FontSize: Optional[FontSize] = None
    FontDecoration: Optional[FontDecorationType] = None
    FontColor: Optional[str] = None
    FontWeight: Optional[FontWeight] = None
    FontStyle: Optional[FontStyleType] = None
    FontFamily: Optional[str] = None


class TypographyOutput(BaseValidatorModel):
    FontFamilies: Optional[List[Font]] = None


class Typography(BaseValidatorModel):
    FontFamilies: Optional[List[Font]] = None


class ForecastScenarioOutput(BaseValidatorModel):
    WhatIfPointScenario: Optional[WhatIfPointScenarioOutput] = None
    WhatIfRangeScenario: Optional[WhatIfRangeScenarioOutput] = None


class FreeFormLayoutCanvasSizeOptions(BaseValidatorModel):
    ScreenCanvasSizeOptions: Optional[FreeFormLayoutScreenCanvasSizeOptions] = None


class SnapshotAnonymousUser(BaseValidatorModel):
    RowLevelPermissionTags: Optional[List[SessionTag]] = None


class QAResult(BaseValidatorModel):
    ResultType: Optional[QAResultTypeType] = None
    DashboardVisual: Optional[DashboardVisualResult] = None
    GeneratedAnswer: Optional[GeneratedAnswerResult] = None

GeoSpatialColumnGroupUnion = Union[GeoSpatialColumnGroup, GeoSpatialColumnGroupOutput]


class GeospatialMapState(BaseValidatorModel):
    Bounds: Optional[GeospatialCoordinateBounds] = None
    MapNavigation: Optional[GeospatialMapNavigationType] = None


class GeospatialWindowOptions(BaseValidatorModel):
    Bounds: Optional[GeospatialCoordinateBounds] = None
    MapZoomMode: Optional[MapZoomModeType] = None


class GeospatialDataSourceItem(BaseValidatorModel):
    StaticFileDataSource: Optional[GeospatialStaticFileSource] = None


class GeospatialHeatmapColorScaleOutput(BaseValidatorModel):
    Colors: Optional[List[GeospatialHeatmapDataColor]] = None


class GeospatialHeatmapColorScale(BaseValidatorModel):
    Colors: Optional[List[GeospatialHeatmapDataColor]] = None


class GeospatialNullDataSettings(BaseValidatorModel):
    SymbolStyle: GeospatialNullSymbolStyle


class TableSideBorderOptions(BaseValidatorModel):
    InnerVertical: Optional[TableBorderOptions] = None
    InnerHorizontal: Optional[TableBorderOptions] = None
    Left: Optional[TableBorderOptions] = None
    Right: Optional[TableBorderOptions] = None
    Top: Optional[TableBorderOptions] = None
    Bottom: Optional[TableBorderOptions] = None


class GradientColorOutput(BaseValidatorModel):
    Stops: Optional[List[GradientStop]] = None


class GradientColor(BaseValidatorModel):
    Stops: Optional[List[GradientStop]] = None


class GridLayoutCanvasSizeOptions(BaseValidatorModel):
    ScreenCanvasSizeOptions: Optional[GridLayoutScreenCanvasSizeOptions] = None


class SearchGroupsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    Filters: List[GroupSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchGroupsRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    Filters: List[GroupSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIAMPolicyAssignmentsResponse(BaseValidatorModel):
    IAMPolicyAssignments: List[IAMPolicyAssignmentSummary]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ImageConfiguration(BaseValidatorModel):
    Source: Optional[ImageSource] = None


class Image(BaseValidatorModel):
    Source: Optional[ImageSource] = None
    GeneratedImageUrl: Optional[str] = None


class ImageInteractionOptions(BaseValidatorModel):
    ImageMenuOption: Optional[ImageMenuOption] = None


class IncrementalRefresh(BaseValidatorModel):
    LookbackWindow: LookbackWindow


class Ingestion(BaseValidatorModel):
    Arn: str
    IngestionStatus: IngestionStatusType
    CreatedTime: datetime
    IngestionId: Optional[str] = None
    ErrorInfo: Optional[ErrorInfo] = None
    RowInfo: Optional[RowInfo] = None
    QueueInfo: Optional[QueueInfo] = None
    IngestionTimeInSeconds: Optional[int] = None
    IngestionSizeInBytes: Optional[int] = None
    RequestSource: Optional[IngestionRequestSourceType] = None
    RequestType: Optional[IngestionRequestTypeType] = None


class IntegerDatasetParameterOutput(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[IntegerDatasetParameterDefaultValuesOutput] = None

IntegerDatasetParameterDefaultValuesUnion = Union[IntegerDatasetParameterDefaultValues, IntegerDatasetParameterDefaultValuesOutput]


class JoinInstruction(BaseValidatorModel):
    LeftOperand: str
    RightOperand: str
    Type: JoinTypeType
    OnClause: str
    LeftJoinKeyProperties: Optional[JoinKeyProperties] = None
    RightJoinKeyProperties: Optional[JoinKeyProperties] = None


class KPIVisualLayoutOptions(BaseValidatorModel):
    StandardLayout: Optional[KPIVisualStandardLayout] = None


class LineChartDefaultSeriesSettings(BaseValidatorModel):
    AxisBinding: Optional[AxisBindingType] = None
    LineStyleSettings: Optional[LineChartLineStyleSettings] = None
    MarkerStyleSettings: Optional[LineChartMarkerStyleSettings] = None


class LineChartSeriesSettings(BaseValidatorModel):
    LineStyleSettings: Optional[LineChartLineStyleSettings] = None
    MarkerStyleSettings: Optional[LineChartMarkerStyleSettings] = None


class LinkSharingConfiguration(BaseValidatorModel):
    Permissions: Optional[List[ResourcePermission]] = None

ResourcePermissionUnion = Union[ResourcePermission, ResourcePermissionOutput]


class ListFolderMembersResponse(BaseValidatorModel):
    Status: int
    FolderMemberList: List[MemberIdArnPair]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTemplateVersionsResponse(BaseValidatorModel):
    TemplateVersionSummaryList: List[TemplateVersionSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTemplatesResponse(BaseValidatorModel):
    TemplateSummaryList: List[TemplateSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListThemeVersionsResponse(BaseValidatorModel):
    ThemeVersionSummaryList: List[ThemeVersionSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListThemesResponse(BaseValidatorModel):
    ThemeSummaryList: List[ThemeSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTopicsResponse(BaseValidatorModel):
    TopicsSummaries: List[TopicSummary]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchTopicsResponse(BaseValidatorModel):
    TopicSummaryList: List[TopicSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class VisualSubtitleLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FormatText: Optional[LongFormatText] = None


class S3Parameters(BaseValidatorModel):
    ManifestFileLocation: ManifestFileLocation
    RoleArn: Optional[str] = None


class TileLayoutStyle(BaseValidatorModel):
    Gutter: Optional[GutterStyle] = None
    Margin: Optional[MarginStyle] = None


class NamedEntityDefinitionOutput(BaseValidatorModel):
    FieldName: Optional[str] = None
    PropertyName: Optional[str] = None
    PropertyRole: Optional[PropertyRoleType] = None
    PropertyUsage: Optional[PropertyUsageType] = None
    Metric: Optional[NamedEntityDefinitionMetricOutput] = None


class NamedEntityDefinition(BaseValidatorModel):
    FieldName: Optional[str] = None
    PropertyName: Optional[str] = None
    PropertyRole: Optional[PropertyRoleType] = None
    PropertyUsage: Optional[PropertyUsageType] = None
    Metric: Optional[NamedEntityDefinitionMetric] = None


class NamespaceInfoV2(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    CapacityRegion: Optional[str] = None
    CreationStatus: Optional[NamespaceStatusType] = None
    IdentityStore: Optional[Literal['QUICKSIGHT']] = None
    NamespaceError: Optional[NamespaceError] = None
    IamIdentityCenterApplicationArn: Optional[str] = None
    IamIdentityCenterInstanceArn: Optional[str] = None


class VPCConnectionSummary(BaseValidatorModel):
    VPCConnectionId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    Status: Optional[VPCConnectionResourceStatusType] = None
    AvailabilityStatus: Optional[VPCConnectionAvailabilityStatusType] = None
    NetworkInterfaces: Optional[List[NetworkInterface]] = None
    RoleArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class VPCConnection(BaseValidatorModel):
    VPCConnectionId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    Status: Optional[VPCConnectionResourceStatusType] = None
    AvailabilityStatus: Optional[VPCConnectionAvailabilityStatusType] = None
    NetworkInterfaces: Optional[List[NetworkInterface]] = None
    RoleArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class OverrideDatasetParameterOperationOutput(BaseValidatorModel):
    ParameterName: str
    NewParameterName: Optional[str] = None
    NewDefaultValues: Optional[NewDefaultValuesOutput] = None


class NumericSeparatorConfiguration(BaseValidatorModel):
    DecimalSeparator: Optional[NumericSeparatorSymbolType] = None
    ThousandsSeparator: Optional[ThousandSeparatorOptions] = None


class NumericalAggregationFunction(BaseValidatorModel):
    SimpleNumericalAggregation: Optional[SimpleNumericalAggregationFunctionType] = None
    PercentileAggregation: Optional[PercentileAggregation] = None


class ParametersOutput(BaseValidatorModel):
    StringParameters: Optional[List[StringParameterOutput]] = None
    IntegerParameters: Optional[List[IntegerParameterOutput]] = None
    DecimalParameters: Optional[List[DecimalParameterOutput]] = None
    DateTimeParameters: Optional[List[DateTimeParameterOutput]] = None


class VisibleRangeOptions(BaseValidatorModel):
    PercentRange: Optional[PercentVisibleRange] = None


class PerformanceConfigurationOutput(BaseValidatorModel):
    UniqueKeys: Optional[List[UniqueKeyOutput]] = None


class PerformanceConfiguration(BaseValidatorModel):
    UniqueKeys: Optional[List[UniqueKey]] = None


class PluginVisualOptionsOutput(BaseValidatorModel):
    VisualProperties: Optional[List[PluginVisualProperty]] = None


class PluginVisualOptions(BaseValidatorModel):
    VisualProperties: Optional[List[PluginVisualProperty]] = None

ProjectOperationUnion = Union[ProjectOperation, ProjectOperationOutput]


class RadarChartSeriesSettings(BaseValidatorModel):
    AreaStyleSettings: Optional[RadarChartAreaStyleSettings] = None


class TopicRangeFilterConstant(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    RangeConstant: Optional[RangeConstant] = None


class RedshiftParametersOutput(BaseValidatorModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersOutput] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfiguration] = None

RedshiftIAMParametersUnion = Union[RedshiftIAMParameters, RedshiftIAMParametersOutput]


class RefreshFrequency(BaseValidatorModel):
    Interval: RefreshIntervalType
    RefreshOnDay: Optional[ScheduleRefreshOnEntity] = None
    Timezone: Optional[str] = None
    TimeOfTheDay: Optional[str] = None


class RegisteredUserConsoleFeatureConfigurations(BaseValidatorModel):
    StatePersistence: Optional[StatePersistenceConfigurations] = None
    SharedView: Optional[SharedViewConfigurations] = None


class RegisteredUserDashboardFeatureConfigurations(BaseValidatorModel):
    StatePersistence: Optional[StatePersistenceConfigurations] = None
    SharedView: Optional[SharedViewConfigurations] = None
    Bookmarks: Optional[BookmarksConfigurations] = None


class RowLevelPermissionTagConfigurationOutput(BaseValidatorModel):
    TagRules: List[RowLevelPermissionTagRule]
    Status: Optional[StatusType] = None
    TagRuleConfigurations: Optional[List[List[str]]] = None


class RowLevelPermissionTagConfiguration(BaseValidatorModel):
    TagRules: List[RowLevelPermissionTagRule]
    Status: Optional[StatusType] = None
    TagRuleConfigurations: Optional[List[List[str]]] = None


class SnapshotS3DestinationConfiguration(BaseValidatorModel):
    BucketConfiguration: S3BucketConfiguration


class S3SourceOutput(BaseValidatorModel):
    DataSourceArn: str
    InputColumns: List[InputColumn]
    UploadSettings: Optional[UploadSettings] = None


class S3Source(BaseValidatorModel):
    DataSourceArn: str
    InputColumns: List[InputColumn]
    UploadSettings: Optional[UploadSettings] = None


class SearchTopicsRequestPaginate(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[TopicSearchFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchTopicsRequest(BaseValidatorModel):
    AwsAccountId: str
    Filters: List[TopicSearchFilter]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SectionBasedLayoutPaperCanvasSizeOptions(BaseValidatorModel):
    PaperSize: Optional[PaperSizeType] = None
    PaperOrientation: Optional[PaperOrientationType] = None
    PaperMargin: Optional[Spacing] = None


class SectionStyle(BaseValidatorModel):
    Height: Optional[str] = None
    Padding: Optional[Spacing] = None


class SelectedSheetsFilterScopeConfigurationOutput(BaseValidatorModel):
    SheetVisualScopingConfigurations: Optional[List[SheetVisualScopingConfigurationOutput]] = None


class SelectedSheetsFilterScopeConfiguration(BaseValidatorModel):
    SheetVisualScopingConfigurations: Optional[List[SheetVisualScopingConfiguration]] = None


class SheetElementRenderingRule(BaseValidatorModel):
    Expression: str
    ConfigurationOverrides: SheetElementConfigurationOverrides


class SheetImageSource(BaseValidatorModel):
    SheetImageStaticFileSource: Optional[SheetImageStaticFileSource] = None


class SheetImageTooltipConfiguration(BaseValidatorModel):
    TooltipText: Optional[SheetImageTooltipText] = None
    Visibility: Optional[VisibilityType] = None


class VisualTitleLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FormatText: Optional[ShortFormatText] = None


class SingleAxisOptions(BaseValidatorModel):
    YAxisOptions: Optional[YAxisOptions] = None


class TopicTemplateOutput(BaseValidatorModel):
    TemplateType: Optional[str] = None
    Slots: Optional[List[Slot]] = None


class TopicTemplate(BaseValidatorModel):
    TemplateType: Optional[str] = None
    Slots: Optional[List[Slot]] = None


class SnapshotUserConfigurationRedacted(BaseValidatorModel):
    AnonymousUsers: Optional[List[SnapshotAnonymousUserRedacted]] = None


class SnapshotFileOutput(BaseValidatorModel):
    SheetSelections: List[SnapshotFileSheetSelectionOutput]
    FormatType: SnapshotFileFormatTypeType


class SnapshotFile(BaseValidatorModel):
    SheetSelections: List[SnapshotFileSheetSelection]
    FormatType: SnapshotFileFormatTypeType


class StaticFileSource(BaseValidatorModel):
    UrlOptions: Optional[StaticFileUrlSourceOptions] = None
    S3Options: Optional[StaticFileS3SourceOptions] = None


class StringDatasetParameterOutput(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[StringDatasetParameterDefaultValuesOutput] = None

StringDatasetParameterDefaultValuesUnion = Union[StringDatasetParameterDefaultValues, StringDatasetParameterDefaultValuesOutput]


class UpdateKeyRegistrationResponse(BaseValidatorModel):
    FailedKeyRegistration: List[FailedKeyRegistrationEntry]
    SuccessfulKeyRegistration: List[SuccessfulKeyRegistrationEntry]
    RequestId: str
    ResponseMetadata: ResponseMetadata


class TableFieldImageConfiguration(BaseValidatorModel):
    SizingOptions: Optional[TableCellImageSizingConfiguration] = None


class TopicNumericEqualityFilter(BaseValidatorModel):
    Constant: Optional[TopicSingularFilterConstant] = None
    Aggregation: Optional[NamedFilterAggTypeType] = None


class TopicRelativeDateFilter(BaseValidatorModel):
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    RelativeDateFilterFunction: Optional[TopicRelativeDateFilterFunctionType] = None
    Constant: Optional[TopicSingularFilterConstant] = None


class TotalAggregationOption(BaseValidatorModel):
    FieldId: str
    TotalAggregationFunction: TotalAggregationFunction

UntagColumnOperationUnion = Union[UntagColumnOperation, UntagColumnOperationOutput]


class WaterfallChartColorConfiguration(BaseValidatorModel):
    GroupColorConfiguration: Optional[WaterfallChartGroupColorConfiguration] = None


class CascadingControlConfigurationOutput(BaseValidatorModel):
    SourceControls: Optional[List[CascadingControlSource]] = None


class CascadingControlConfiguration(BaseValidatorModel):
    SourceControls: Optional[List[CascadingControlSource]] = None


class DateTimeDefaultValuesOutput(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[datetime]] = None
    RollingDate: Optional[RollingDateConfiguration] = None


class DateTimeDefaultValues(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[Timestamp]] = None
    RollingDate: Optional[RollingDateConfiguration] = None


class DecimalDefaultValuesOutput(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[float]] = None


class DecimalDefaultValues(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[float]] = None


class IntegerDefaultValuesOutput(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[int]] = None


class IntegerDefaultValues(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[int]] = None


class StringDefaultValuesOutput(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[str]] = None


class StringDefaultValues(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValue] = None
    StaticValues: Optional[List[str]] = None


class DrillDownFilterOutput(BaseValidatorModel):
    NumericEqualityFilter: Optional[NumericEqualityDrillDownFilter] = None
    CategoryFilter: Optional[CategoryDrillDownFilterOutput] = None
    TimeRangeFilter: Optional[TimeRangeDrillDownFilterOutput] = None


class AnalysisSourceEntity(BaseValidatorModel):
    SourceTemplate: Optional[AnalysisSourceTemplate] = None


class DashboardSourceEntity(BaseValidatorModel):
    SourceTemplate: Optional[DashboardSourceTemplate] = None


class TemplateSourceEntity(BaseValidatorModel):
    SourceAnalysis: Optional[TemplateSourceAnalysis] = None
    SourceTemplate: Optional[TemplateSourceTemplate] = None


class AnonymousUserDashboardEmbeddingConfiguration(BaseValidatorModel):
    InitialDashboardId: str
    EnabledFeatures: Optional[List[Literal['SHARED_VIEW']]] = None
    DisabledFeatures: Optional[List[Literal['SHARED_VIEW']]] = None
    FeatureConfigurations: Optional[AnonymousUserDashboardFeatureConfigurations] = None


class DescribeAssetBundleExportJobResponse(BaseValidatorModel):
    JobStatus: AssetBundleExportJobStatusType
    DownloadUrl: str
    Errors: List[AssetBundleExportJobError]
    Arn: str
    CreatedTime: datetime
    AssetBundleExportJobId: str
    AwsAccountId: str
    ResourceArns: List[str]
    IncludeAllDependencies: bool
    ExportFormat: AssetBundleExportFormatType
    CloudFormationOverridePropertyConfiguration: AssetBundleCloudFormationOverridePropertyConfigurationOutput
    RequestId: str
    Status: int
    IncludePermissions: bool
    IncludeTags: bool
    ValidationStrategy: AssetBundleExportJobValidationStrategy
    Warnings: List[AssetBundleExportJobWarning]
    IncludeFolderMemberships: bool
    IncludeFolderMembers: IncludeFolderMembersType
    ResponseMetadata: ResponseMetadata

AssetBundleCloudFormationOverridePropertyConfigurationUnion = Union[AssetBundleCloudFormationOverridePropertyConfiguration, AssetBundleCloudFormationOverridePropertyConfigurationOutput]


class AssetBundleImportJobDashboardOverridePermissionsOutput(BaseValidatorModel):
    DashboardIds: List[str]
    Permissions: Optional[AssetBundleResourcePermissionsOutput] = None
    LinkSharingConfiguration: Optional[AssetBundleResourceLinkSharingConfigurationOutput] = None


class AssetBundleImportJobDashboardOverridePermissions(BaseValidatorModel):
    DashboardIds: List[str]
    Permissions: Optional[AssetBundleResourcePermissions] = None
    LinkSharingConfiguration: Optional[AssetBundleResourceLinkSharingConfiguration] = None


class AssetBundleImportJobOverrideTagsOutput(BaseValidatorModel):
    VPCConnections: Optional[List[AssetBundleImportJobVPCConnectionOverrideTagsOutput]] = None
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverrideTagsOutput]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideTagsOutput]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideTagsOutput]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideTagsOutput]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideTagsOutput]] = None
    Folders: Optional[List[AssetBundleImportJobFolderOverrideTagsOutput]] = None


class AssetBundleImportJobOverrideTags(BaseValidatorModel):
    VPCConnections: Optional[List[AssetBundleImportJobVPCConnectionOverrideTags]] = None
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverrideTags]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideTags]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideTags]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideTags]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideTags]] = None
    Folders: Optional[List[AssetBundleImportJobFolderOverrideTags]] = None


class SnowflakeParameters(BaseValidatorModel):
    Host: str
    Database: str
    Warehouse: str
    AuthenticationType: Optional[AuthenticationTypeType] = None
    DatabaseAccessControlRole: Optional[str] = None
    OAuthParameters: Optional[OAuthParameters] = None


class StarburstParameters(BaseValidatorModel):
    Host: str
    Port: int
    Catalog: str
    ProductType: Optional[StarburstProductTypeType] = None
    DatabaseAccessControlRole: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    OAuthParameters: Optional[OAuthParameters] = None


class CustomValuesConfiguration(BaseValidatorModel):
    CustomValues: CustomParameterValues
    IncludeNullValue: Optional[bool] = None

DateTimeDatasetParameterDefaultValuesUnion = Union[DateTimeDatasetParameterDefaultValues, DateTimeDatasetParameterDefaultValuesOutput]


class Parameters(BaseValidatorModel):
    StringParameters: Optional[List[StringParameter]] = None
    IntegerParameters: Optional[List[IntegerParameter]] = None
    DecimalParameters: Optional[List[DecimalParameter]] = None
    DateTimeParameters: Optional[List[DateTimeParameter]] = None

NewDefaultValuesUnion = Union[NewDefaultValues, NewDefaultValuesOutput]


class DrillDownFilter(BaseValidatorModel):
    NumericEqualityFilter: Optional[NumericEqualityDrillDownFilter] = None
    CategoryFilter: Optional[CategoryDrillDownFilter] = None
    TimeRangeFilter: Optional[TimeRangeDrillDownFilter] = None

TopicRefreshScheduleUnion = Union[TopicRefreshSchedule, TopicRefreshScheduleOutput]


class ForecastScenario(BaseValidatorModel):
    WhatIfPointScenario: Optional[WhatIfPointScenario] = None
    WhatIfRangeScenario: Optional[WhatIfRangeScenario] = None


class NumericAxisOptionsOutput(BaseValidatorModel):
    Scale: Optional[AxisScale] = None
    Range: Optional[AxisDisplayRangeOutput] = None


class NumericAxisOptions(BaseValidatorModel):
    Scale: Optional[AxisScale] = None
    Range: Optional[AxisDisplayRange] = None


class BrandElementStyle(BaseValidatorModel):
    NavbarStyle: Optional[NavbarStyle] = None

CreateColumnsOperationUnion = Union[CreateColumnsOperation, CreateColumnsOperationOutput]


class DescribeCustomPermissionsResponse(BaseValidatorModel):
    Status: int
    CustomPermissions: CustomPermissions
    RequestId: str
    ResponseMetadata: ResponseMetadata


class ListCustomPermissionsResponse(BaseValidatorModel):
    Status: int
    CustomPermissionsList: List[CustomPermissions]
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClusterMarkerConfiguration(BaseValidatorModel):
    ClusterMarker: Optional[ClusterMarker] = None

TopicConstantValueUnion = Union[TopicConstantValue, TopicConstantValueOutput]


class TopicCategoryFilterOutput(BaseValidatorModel):
    CategoryFilterFunction: Optional[CategoryFilterFunctionType] = None
    CategoryFilterType: Optional[CategoryFilterTypeType] = None
    Constant: Optional[TopicCategoryFilterConstantOutput] = None
    Inverse: Optional[bool] = None


class TopicCategoryFilter(BaseValidatorModel):
    CategoryFilterFunction: Optional[CategoryFilterFunctionType] = None
    CategoryFilterType: Optional[CategoryFilterTypeType] = None
    Constant: Optional[TopicCategoryFilterConstant] = None
    Inverse: Optional[bool] = None


class TagColumnOperationOutput(BaseValidatorModel):
    ColumnName: str
    Tags: List[ColumnTag]


class TagColumnOperation(BaseValidatorModel):
    ColumnName: str
    Tags: List[ColumnTag]


class DataSetConfigurationOutput(BaseValidatorModel):
    Placeholder: Optional[str] = None
    DataSetSchema: Optional[DataSetSchemaOutput] = None
    ColumnGroupSchemaList: Optional[List[ColumnGroupSchemaOutput]] = None


class DataSetConfiguration(BaseValidatorModel):
    Placeholder: Optional[str] = None
    DataSetSchema: Optional[DataSetSchema] = None
    ColumnGroupSchemaList: Optional[List[ColumnGroupSchema]] = None


class ConditionalFormattingIcon(BaseValidatorModel):
    IconSet: Optional[ConditionalFormattingIconSet] = None
    CustomCondition: Optional[ConditionalFormattingCustomIconCondition] = None


class ListDataSetsResponse(BaseValidatorModel):
    DataSetSummaries: List[DataSetSummary]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchDataSetsResponse(BaseValidatorModel):
    DataSetSummaries: List[DataSetSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DestinationParameterValueConfigurationOutput(BaseValidatorModel):
    CustomValuesConfiguration: Optional[CustomValuesConfigurationOutput] = None
    SelectAllValueOptions: Optional[Literal['ALL_VALUES']] = None
    SourceParameterName: Optional[str] = None
    SourceField: Optional[str] = None
    SourceColumn: Optional[ColumnIdentifier] = None

CustomSqlUnion = Union[CustomSql, CustomSqlOutput]

RelationalTableUnion = Union[RelationalTable, RelationalTableOutput]


class CustomContentConfiguration(BaseValidatorModel):
    ContentUrl: Optional[str] = None
    ContentType: Optional[CustomContentTypeType] = None
    ImageScaling: Optional[CustomContentImageScalingConfigurationType] = None
    Interactions: Optional[VisualInteractionOptions] = None


class DashboardPublishOptions(BaseValidatorModel):
    AdHocFilteringOption: Optional[AdHocFilteringOption] = None
    ExportToCSVOption: Optional[ExportToCSVOption] = None
    SheetControlsOption: Optional[SheetControlsOption] = None
    VisualPublishOptions: Optional[DashboardVisualPublishOptions] = None
    SheetLayoutElementMaximizationOption: Optional[SheetLayoutElementMaximizationOption] = None
    VisualMenuOption: Optional[VisualMenuOption] = None
    VisualAxisSortOption: Optional[VisualAxisSortOption] = None
    ExportWithHiddenFieldsOption: Optional[ExportWithHiddenFieldsOption] = None
    DataPointDrillUpDownOption: Optional[DataPointDrillUpDownOption] = None
    DataPointMenuLabelOption: Optional[DataPointMenuLabelOption] = None
    DataPointTooltipOption: Optional[DataPointTooltipOption] = None


class DataPathColor(BaseValidatorModel):
    Element: DataPathValue
    Color: str
    TimeGranularity: Optional[TimeGranularityType] = None


class DataPathSortOutput(BaseValidatorModel):
    Direction: SortDirectionType
    SortPaths: List[DataPathValue]


class DataPathSort(BaseValidatorModel):
    Direction: SortDirectionType
    SortPaths: List[DataPathValue]


class PivotTableDataPathOptionOutput(BaseValidatorModel):
    DataPathList: List[DataPathValue]
    Width: Optional[str] = None


class PivotTableDataPathOption(BaseValidatorModel):
    DataPathList: List[DataPathValue]
    Width: Optional[str] = None


class PivotTableFieldCollapseStateTargetOutput(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldDataPathValues: Optional[List[DataPathValue]] = None


class PivotTableFieldCollapseStateTarget(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldDataPathValues: Optional[List[DataPathValue]] = None


class DecimalDatasetParameter(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[DecimalDatasetParameterDefaultValuesUnion] = None


class DescribeDashboardPermissionsResponse(BaseValidatorModel):
    DashboardId: str
    DashboardArn: str
    Permissions: List[ResourcePermissionOutput]
    Status: int
    RequestId: str
    LinkSharingConfiguration: LinkSharingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class UpdateDashboardPermissionsResponse(BaseValidatorModel):
    DashboardArn: str
    DashboardId: str
    Permissions: List[ResourcePermissionOutput]
    RequestId: str
    Status: int
    LinkSharingConfiguration: LinkSharingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class ListTopicRefreshSchedulesResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    RefreshSchedules: List[TopicRefreshScheduleSummary]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DefaultFormatting(BaseValidatorModel):
    DisplayFormat: Optional[DisplayFormatType] = None
    DisplayFormatOptions: Optional[DisplayFormatOptions] = None


class TopicIRMetricOutput(BaseValidatorModel):
    MetricId: Optional[Identifier] = None
    Function: Optional[AggFunctionOutput] = None
    Operands: Optional[List[Identifier]] = None
    ComparisonMethod: Optional[TopicIRComparisonMethod] = None
    Expression: Optional[str] = None
    CalculatedFieldReferences: Optional[List[Identifier]] = None
    DisplayFormat: Optional[DisplayFormatType] = None
    DisplayFormatOptions: Optional[DisplayFormatOptions] = None
    NamedEntity: Optional[NamedEntityRef] = None


class TopicIRMetric(BaseValidatorModel):
    MetricId: Optional[Identifier] = None
    Function: Optional[AggFunctionUnion] = None
    Operands: Optional[List[Identifier]] = None
    ComparisonMethod: Optional[TopicIRComparisonMethod] = None
    Expression: Optional[str] = None
    CalculatedFieldReferences: Optional[List[Identifier]] = None
    DisplayFormat: Optional[DisplayFormatType] = None
    DisplayFormatOptions: Optional[DisplayFormatOptions] = None
    NamedEntity: Optional[NamedEntityRef] = None


class TopicIRFilterOptionOutput(BaseValidatorModel):
    FilterType: Optional[TopicIRFilterTypeType] = None
    FilterClass: Optional[FilterClassType] = None
    OperandField: Optional[Identifier] = None
    Function: Optional[TopicIRFilterFunctionType] = None
    Constant: Optional[TopicConstantValueOutput] = None
    Inverse: Optional[bool] = None
    NullFilter: Optional[NullFilterOptionType] = None
    Aggregation: Optional[AggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None
    AggregationPartitionBy: Optional[List[AggregationPartitionBy]] = None
    Range: Optional[TopicConstantValueOutput] = None
    Inclusive: Optional[bool] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    LastNextOffset: Optional[TopicConstantValueOutput] = None
    AggMetrics: Optional[List[FilterAggMetrics]] = None
    TopBottomLimit: Optional[TopicConstantValueOutput] = None
    SortDirection: Optional[TopicSortDirectionType] = None
    Anchor: Optional[Anchor] = None


class TopicIRGroupBy(BaseValidatorModel):
    FieldName: Optional[Identifier] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    Sort: Optional[TopicSortClause] = None
    DisplayFormat: Optional[DisplayFormatType] = None
    DisplayFormatOptions: Optional[DisplayFormatOptions] = None
    NamedEntity: Optional[NamedEntityRef] = None


class CustomActionFilterOperationOutput(BaseValidatorModel):
    SelectedFieldsConfiguration: FilterOperationSelectedFieldsConfigurationOutput
    TargetVisualsConfiguration: FilterOperationTargetVisualsConfigurationOutput


class CustomActionFilterOperation(BaseValidatorModel):
    SelectedFieldsConfiguration: FilterOperationSelectedFieldsConfiguration
    TargetVisualsConfiguration: FilterOperationTargetVisualsConfiguration


class AxisLabelOptions(BaseValidatorModel):
    FontConfiguration: Optional[FontConfiguration] = None
    CustomLabel: Optional[str] = None
    ApplyTo: Optional[AxisLabelReferenceOptions] = None


class DataLabelOptionsOutput(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    DataLabelTypes: Optional[List[DataLabelType]] = None
    Position: Optional[DataLabelPositionType] = None
    LabelContent: Optional[DataLabelContentType] = None
    LabelFontConfiguration: Optional[FontConfiguration] = None
    LabelColor: Optional[str] = None
    Overlap: Optional[DataLabelOverlapType] = None
    TotalsVisibility: Optional[VisibilityType] = None


class DataLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    DataLabelTypes: Optional[List[DataLabelType]] = None
    Position: Optional[DataLabelPositionType] = None
    LabelContent: Optional[DataLabelContentType] = None
    LabelFontConfiguration: Optional[FontConfiguration] = None
    LabelColor: Optional[str] = None
    Overlap: Optional[DataLabelOverlapType] = None
    TotalsVisibility: Optional[VisibilityType] = None


class FunnelChartDataLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    Position: Optional[DataLabelPositionType] = None
    LabelFontConfiguration: Optional[FontConfiguration] = None
    LabelColor: Optional[str] = None
    MeasureDataLabelStyle: Optional[FunnelChartMeasureDataLabelStyleType] = None


class LabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfiguration] = None
    CustomLabel: Optional[str] = None


class PanelTitleOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfiguration] = None
    HorizontalTextAlignment: Optional[HorizontalTextAlignmentType] = None


class TableFieldCustomTextContent(BaseValidatorModel):
    FontConfiguration: FontConfiguration
    Value: Optional[str] = None


class ForecastConfigurationOutput(BaseValidatorModel):
    ForecastProperties: Optional[TimeBasedForecastProperties] = None
    Scenario: Optional[ForecastScenarioOutput] = None


class DefaultFreeFormLayoutConfiguration(BaseValidatorModel):
    CanvasSizeOptions: FreeFormLayoutCanvasSizeOptions


class SnapshotUserConfiguration(BaseValidatorModel):
    AnonymousUsers: Optional[List[SnapshotAnonymousUser]] = None


class PredictQAResultsResponse(BaseValidatorModel):
    PrimaryResult: QAResult
    AdditionalResults: List[QAResult]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ColumnGroup(BaseValidatorModel):
    GeoSpatialColumnGroup: Optional[GeoSpatialColumnGroupUnion] = None


class GeospatialHeatmapConfigurationOutput(BaseValidatorModel):
    HeatmapColor: Optional[GeospatialHeatmapColorScaleOutput] = None


class GeospatialHeatmapConfiguration(BaseValidatorModel):
    HeatmapColor: Optional[GeospatialHeatmapColorScale] = None


class GeospatialCategoricalColorOutput(BaseValidatorModel):
    CategoryDataColors: List[GeospatialCategoricalDataColor]
    NullDataVisibility: Optional[VisibilityType] = None
    NullDataSettings: Optional[GeospatialNullDataSettings] = None
    DefaultOpacity: Optional[float] = None


class GeospatialCategoricalColor(BaseValidatorModel):
    CategoryDataColors: List[GeospatialCategoricalDataColor]
    NullDataVisibility: Optional[VisibilityType] = None
    NullDataSettings: Optional[GeospatialNullDataSettings] = None
    DefaultOpacity: Optional[float] = None


class GeospatialGradientColorOutput(BaseValidatorModel):
    StepColors: List[GeospatialGradientStepColor]
    NullDataVisibility: Optional[VisibilityType] = None
    NullDataSettings: Optional[GeospatialNullDataSettings] = None
    DefaultOpacity: Optional[float] = None


class GeospatialGradientColor(BaseValidatorModel):
    StepColors: List[GeospatialGradientStepColor]
    NullDataVisibility: Optional[VisibilityType] = None
    NullDataSettings: Optional[GeospatialNullDataSettings] = None
    DefaultOpacity: Optional[float] = None


class GlobalTableBorderOptions(BaseValidatorModel):
    UniformBorder: Optional[TableBorderOptions] = None
    SideSpecificBorder: Optional[TableSideBorderOptions] = None


class ConditionalFormattingGradientColorOutput(BaseValidatorModel):
    Expression: str
    Color: GradientColorOutput


class ConditionalFormattingGradientColor(BaseValidatorModel):
    Expression: str
    Color: GradientColor


class DefaultGridLayoutConfiguration(BaseValidatorModel):
    CanvasSizeOptions: GridLayoutCanvasSizeOptions


class GridLayoutConfigurationOutput(BaseValidatorModel):
    Elements: List[GridLayoutElement]
    CanvasSizeOptions: Optional[GridLayoutCanvasSizeOptions] = None


class GridLayoutConfiguration(BaseValidatorModel):
    Elements: List[GridLayoutElement]
    CanvasSizeOptions: Optional[GridLayoutCanvasSizeOptions] = None


class ImageSetConfiguration(BaseValidatorModel):
    Original: ImageConfiguration


class ImageSet(BaseValidatorModel):
    Original: Image
    Height64: Optional[Image] = None
    Height32: Optional[Image] = None


class RefreshConfiguration(BaseValidatorModel):
    IncrementalRefresh: IncrementalRefresh


class DescribeIngestionResponse(BaseValidatorModel):
    Ingestion: Ingestion
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ListIngestionsResponse(BaseValidatorModel):
    Ingestions: List[Ingestion]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IntegerDatasetParameter(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[IntegerDatasetParameterDefaultValuesUnion] = None


class LogicalTableSource(BaseValidatorModel):
    JoinInstruction: Optional[JoinInstruction] = None
    PhysicalTableId: Optional[str] = None
    DataSetArn: Optional[str] = None


class DataFieldSeriesItem(BaseValidatorModel):
    FieldId: str
    AxisBinding: AxisBindingType
    FieldValue: Optional[str] = None
    Settings: Optional[LineChartSeriesSettings] = None


class FieldSeriesItem(BaseValidatorModel):
    FieldId: str
    AxisBinding: AxisBindingType
    Settings: Optional[LineChartSeriesSettings] = None

LinkSharingConfigurationUnion = Union[LinkSharingConfiguration, LinkSharingConfigurationOutput]


class CreateFolderRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    ParentFolderArn: Optional[str] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    Tags: Optional[List[Tag]] = None
    SharingModel: Optional[SharingModelType] = None


class UpdateAnalysisPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateDashboardPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None
    GrantLinkPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokeLinkPermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateDataSetPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateDataSourcePermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateFolderPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateTemplatePermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateThemePermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class UpdateTopicPermissionsRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    GrantPermissions: Optional[List[ResourcePermissionUnion]] = None
    RevokePermissions: Optional[List[ResourcePermissionUnion]] = None


class SheetStyle(BaseValidatorModel):
    Tile: Optional[TileStyle] = None
    TileLayout: Optional[TileLayoutStyle] = None


class TopicNamedEntityOutput(BaseValidatorModel):
    EntityName: str
    EntityDescription: Optional[str] = None
    EntitySynonyms: Optional[List[str]] = None
    SemanticEntityType: Optional[SemanticEntityTypeOutput] = None
    Definition: Optional[List[NamedEntityDefinitionOutput]] = None


class TopicNamedEntity(BaseValidatorModel):
    EntityName: str
    EntityDescription: Optional[str] = None
    EntitySynonyms: Optional[List[str]] = None
    SemanticEntityType: Optional[SemanticEntityType] = None
    Definition: Optional[List[NamedEntityDefinition]] = None


class DescribeNamespaceResponse(BaseValidatorModel):
    Namespace: NamespaceInfoV2
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ListNamespacesResponse(BaseValidatorModel):
    Namespaces: List[NamespaceInfoV2]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVPCConnectionsResponse(BaseValidatorModel):
    VPCConnectionSummaries: List[VPCConnectionSummary]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeVPCConnectionResponse(BaseValidatorModel):
    VPCConnection: VPCConnection
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class CurrencyDisplayFormatConfiguration(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfiguration] = None
    Symbol: Optional[str] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfiguration] = None
    NumberScale: Optional[NumberScaleType] = None
    NegativeValueConfiguration: Optional[NegativeValueConfiguration] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfiguration] = None


class NumberDisplayFormatConfiguration(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfiguration] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfiguration] = None
    NumberScale: Optional[NumberScaleType] = None
    NegativeValueConfiguration: Optional[NegativeValueConfiguration] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfiguration] = None


class PercentageDisplayFormatConfiguration(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfiguration] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfiguration] = None
    NegativeValueConfiguration: Optional[NegativeValueConfiguration] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfiguration] = None


class AggregationFunction(BaseValidatorModel):
    NumericalAggregationFunction: Optional[NumericalAggregationFunction] = None
    CategoricalAggregationFunction: Optional[CategoricalAggregationFunctionType] = None
    DateAggregationFunction: Optional[DateAggregationFunctionType] = None
    AttributeAggregationFunction: Optional[AttributeAggregationFunction] = None


class ScrollBarOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    VisibleRange: Optional[VisibleRangeOptions] = None

PerformanceConfigurationUnion = Union[PerformanceConfiguration, PerformanceConfigurationOutput]


class TopicDateRangeFilter(BaseValidatorModel):
    Inclusive: Optional[bool] = None
    Constant: Optional[TopicRangeFilterConstant] = None


class TopicNumericRangeFilter(BaseValidatorModel):
    Inclusive: Optional[bool] = None
    Constant: Optional[TopicRangeFilterConstant] = None
    Aggregation: Optional[NamedFilterAggTypeType] = None


class RedshiftParameters(BaseValidatorModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersUnion] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfiguration] = None


class RefreshScheduleOutput(BaseValidatorModel):
    ScheduleId: str
    ScheduleFrequency: RefreshFrequency
    RefreshType: IngestionTypeType
    StartAfterDateTime: Optional[datetime] = None
    Arn: Optional[str] = None


class RefreshSchedule(BaseValidatorModel):
    ScheduleId: str
    ScheduleFrequency: RefreshFrequency
    RefreshType: IngestionTypeType
    StartAfterDateTime: Optional[Timestamp] = None
    Arn: Optional[str] = None


class RegisteredUserQuickSightConsoleEmbeddingConfiguration(BaseValidatorModel):
    InitialPath: Optional[str] = None
    FeatureConfigurations: Optional[RegisteredUserConsoleFeatureConfigurations] = None


class RegisteredUserDashboardEmbeddingConfiguration(BaseValidatorModel):
    InitialDashboardId: str
    FeatureConfigurations: Optional[RegisteredUserDashboardFeatureConfigurations] = None

RowLevelPermissionTagConfigurationUnion = Union[RowLevelPermissionTagConfiguration, RowLevelPermissionTagConfigurationOutput]


class SnapshotDestinationConfigurationOutput(BaseValidatorModel):
    S3Destinations: Optional[List[SnapshotS3DestinationConfiguration]] = None


class SnapshotDestinationConfiguration(BaseValidatorModel):
    S3Destinations: Optional[List[SnapshotS3DestinationConfiguration]] = None


class SnapshotJobS3Result(BaseValidatorModel):
    S3DestinationConfiguration: Optional[SnapshotS3DestinationConfiguration] = None
    S3Uri: Optional[str] = None
    ErrorInfo: Optional[List[SnapshotJobResultErrorInfo]] = None


class PhysicalTableOutput(BaseValidatorModel):
    RelationalTable: Optional[RelationalTableOutput] = None
    CustomSql: Optional[CustomSqlOutput] = None
    S3Source: Optional[S3SourceOutput] = None

S3SourceUnion = Union[S3Source, S3SourceOutput]


class SectionBasedLayoutCanvasSizeOptions(BaseValidatorModel):
    PaperCanvasSizeOptions: Optional[SectionBasedLayoutPaperCanvasSizeOptions] = None


class FilterScopeConfigurationOutput(BaseValidatorModel):
    SelectedSheets: Optional[SelectedSheetsFilterScopeConfigurationOutput] = None
    AllSheets: Optional[Dict[str, Any]] = None


class FilterScopeConfiguration(BaseValidatorModel):
    SelectedSheets: Optional[SelectedSheetsFilterScopeConfiguration] = None
    AllSheets: Optional[Dict[str, Any]] = None


class FreeFormLayoutElementOutput(BaseValidatorModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    XAxisLocation: str
    YAxisLocation: str
    Width: str
    Height: str
    Visibility: Optional[VisibilityType] = None
    RenderingRules: Optional[List[SheetElementRenderingRule]] = None
    BorderStyle: Optional[FreeFormLayoutElementBorderStyle] = None
    SelectedBorderStyle: Optional[FreeFormLayoutElementBorderStyle] = None
    BackgroundStyle: Optional[FreeFormLayoutElementBackgroundStyle] = None
    LoadingAnimation: Optional[LoadingAnimation] = None


class FreeFormLayoutElement(BaseValidatorModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    XAxisLocation: str
    YAxisLocation: str
    Width: str
    Height: str
    Visibility: Optional[VisibilityType] = None
    RenderingRules: Optional[List[SheetElementRenderingRule]] = None
    BorderStyle: Optional[FreeFormLayoutElementBorderStyle] = None
    SelectedBorderStyle: Optional[FreeFormLayoutElementBorderStyle] = None
    BackgroundStyle: Optional[FreeFormLayoutElementBackgroundStyle] = None
    LoadingAnimation: Optional[LoadingAnimation] = None

TopicTemplateUnion = Union[TopicTemplate, TopicTemplateOutput]


class SnapshotFileGroupOutput(BaseValidatorModel):
    Files: Optional[List[SnapshotFileOutput]] = None


class SnapshotFileGroup(BaseValidatorModel):
    Files: Optional[List[SnapshotFile]] = None


class ImageStaticFile(BaseValidatorModel):
    StaticFileId: str
    Source: Optional[StaticFileSource] = None


class SpatialStaticFile(BaseValidatorModel):
    StaticFileId: str
    Source: Optional[StaticFileSource] = None


class DatasetParameterOutput(BaseValidatorModel):
    StringDatasetParameter: Optional[StringDatasetParameterOutput] = None
    DecimalDatasetParameter: Optional[DecimalDatasetParameterOutput] = None
    IntegerDatasetParameter: Optional[IntegerDatasetParameterOutput] = None
    DateTimeDatasetParameter: Optional[DateTimeDatasetParameterOutput] = None


class StringDatasetParameter(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[StringDatasetParameterDefaultValuesUnion] = None


class FilterCrossSheetControlOutput(BaseValidatorModel):
    FilterControlId: str
    SourceFilterId: str
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutput] = None


class FilterCrossSheetControl(BaseValidatorModel):
    FilterControlId: str
    SourceFilterId: str
    CascadingControlConfiguration: Optional[CascadingControlConfiguration] = None


class DateTimeParameterDeclarationOutput(BaseValidatorModel):
    Name: str
    DefaultValues: Optional[DateTimeDefaultValuesOutput] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ValueWhenUnset: Optional[DateTimeValueWhenUnsetConfigurationOutput] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class DateTimeParameterDeclaration(BaseValidatorModel):
    Name: str
    DefaultValues: Optional[DateTimeDefaultValues] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ValueWhenUnset: Optional[DateTimeValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class DecimalParameterDeclarationOutput(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[DecimalDefaultValuesOutput] = None
    ValueWhenUnset: Optional[DecimalValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class DecimalParameterDeclaration(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[DecimalDefaultValues] = None
    ValueWhenUnset: Optional[DecimalValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class IntegerParameterDeclarationOutput(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[IntegerDefaultValuesOutput] = None
    ValueWhenUnset: Optional[IntegerValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class IntegerParameterDeclaration(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[IntegerDefaultValues] = None
    ValueWhenUnset: Optional[IntegerValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class StringParameterDeclarationOutput(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[StringDefaultValuesOutput] = None
    ValueWhenUnset: Optional[StringValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class StringParameterDeclaration(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[StringDefaultValues] = None
    ValueWhenUnset: Optional[StringValueWhenUnsetConfiguration] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameter]] = None


class DateTimeHierarchyOutput(BaseValidatorModel):
    HierarchyId: str
    DrillDownFilters: Optional[List[DrillDownFilterOutput]] = None


class ExplicitHierarchyOutput(BaseValidatorModel):
    HierarchyId: str
    Columns: List[ColumnIdentifier]
    DrillDownFilters: Optional[List[DrillDownFilterOutput]] = None


class PredefinedHierarchyOutput(BaseValidatorModel):
    HierarchyId: str
    Columns: List[ColumnIdentifier]
    DrillDownFilters: Optional[List[DrillDownFilterOutput]] = None


class AnonymousUserEmbeddingExperienceConfiguration(BaseValidatorModel):
    Dashboard: Optional[AnonymousUserDashboardEmbeddingConfiguration] = None
    DashboardVisual: Optional[AnonymousUserDashboardVisualEmbeddingConfiguration] = None
    QSearchBar: Optional[AnonymousUserQSearchBarEmbeddingConfiguration] = None
    GenerativeQnA: Optional[AnonymousUserGenerativeQnAEmbeddingConfiguration] = None


class StartAssetBundleExportJobRequest(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleExportJobId: str
    ResourceArns: List[str]
    ExportFormat: AssetBundleExportFormatType
    IncludeAllDependencies: Optional[bool] = None
    CloudFormationOverridePropertyConfiguration: Optional[AssetBundleCloudFormationOverridePropertyConfigurationUnion] = None
    IncludePermissions: Optional[bool] = None
    IncludeTags: Optional[bool] = None
    ValidationStrategy: Optional[AssetBundleExportJobValidationStrategy] = None
    IncludeFolderMemberships: Optional[bool] = None
    IncludeFolderMembers: Optional[IncludeFolderMembersType] = None


class AssetBundleImportJobOverridePermissionsOutput(BaseValidatorModel):
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverridePermissionsOutput]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverridePermissionsOutput]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverridePermissionsOutput]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverridePermissionsOutput]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverridePermissionsOutput]] = None
    Folders: Optional[List[AssetBundleImportJobFolderOverridePermissionsOutput]] = None


class AssetBundleImportJobOverridePermissions(BaseValidatorModel):
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverridePermissions]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverridePermissions]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverridePermissions]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverridePermissions]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverridePermissions]] = None
    Folders: Optional[List[AssetBundleImportJobFolderOverridePermissions]] = None

AssetBundleImportJobOverrideTagsUnion = Union[AssetBundleImportJobOverrideTags, AssetBundleImportJobOverrideTagsOutput]


class DataSourceParametersOutput(BaseValidatorModel):
    AmazonElasticsearchParameters: Optional[AmazonElasticsearchParameters] = None
    AthenaParameters: Optional[AthenaParameters] = None
    AuroraParameters: Optional[AuroraParameters] = None
    AuroraPostgreSqlParameters: Optional[AuroraPostgreSqlParameters] = None
    AwsIotAnalyticsParameters: Optional[AwsIotAnalyticsParameters] = None
    JiraParameters: Optional[JiraParameters] = None
    MariaDbParameters: Optional[MariaDbParameters] = None
    MySqlParameters: Optional[MySqlParameters] = None
    OracleParameters: Optional[OracleParameters] = None
    PostgreSqlParameters: Optional[PostgreSqlParameters] = None
    PrestoParameters: Optional[PrestoParameters] = None
    RdsParameters: Optional[RdsParameters] = None
    RedshiftParameters: Optional[RedshiftParametersOutput] = None
    S3Parameters: Optional[S3Parameters] = None
    ServiceNowParameters: Optional[ServiceNowParameters] = None
    SnowflakeParameters: Optional[SnowflakeParameters] = None
    SparkParameters: Optional[SparkParameters] = None
    SqlServerParameters: Optional[SqlServerParameters] = None
    TeradataParameters: Optional[TeradataParameters] = None
    TwitterParameters: Optional[TwitterParameters] = None
    AmazonOpenSearchParameters: Optional[AmazonOpenSearchParameters] = None
    ExasolParameters: Optional[ExasolParameters] = None
    DatabricksParameters: Optional[DatabricksParameters] = None
    StarburstParameters: Optional[StarburstParameters] = None
    TrinoParameters: Optional[TrinoParameters] = None
    BigQueryParameters: Optional[BigQueryParameters] = None


class DestinationParameterValueConfiguration(BaseValidatorModel):
    CustomValuesConfiguration: Optional[CustomValuesConfiguration] = None
    SelectAllValueOptions: Optional[Literal['ALL_VALUES']] = None
    SourceParameterName: Optional[str] = None
    SourceField: Optional[str] = None
    SourceColumn: Optional[ColumnIdentifier] = None


class DateTimeDatasetParameter(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultValues: Optional[DateTimeDatasetParameterDefaultValuesUnion] = None

ParametersUnion = Union[Parameters, ParametersOutput]


class OverrideDatasetParameterOperation(BaseValidatorModel):
    ParameterName: str
    NewParameterName: Optional[str] = None
    NewDefaultValues: Optional[NewDefaultValuesUnion] = None


class DateTimeHierarchy(BaseValidatorModel):
    HierarchyId: str
    DrillDownFilters: Optional[List[DrillDownFilter]] = None


class ExplicitHierarchy(BaseValidatorModel):
    HierarchyId: str
    Columns: List[ColumnIdentifier]
    DrillDownFilters: Optional[List[DrillDownFilter]] = None


class PredefinedHierarchy(BaseValidatorModel):
    HierarchyId: str
    Columns: List[ColumnIdentifier]
    DrillDownFilters: Optional[List[DrillDownFilter]] = None


class CreateTopicRefreshScheduleRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetArn: str
    RefreshSchedule: TopicRefreshScheduleUnion
    DatasetName: Optional[str] = None


class UpdateTopicRefreshScheduleRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str
    RefreshSchedule: TopicRefreshScheduleUnion


class ForecastConfiguration(BaseValidatorModel):
    ForecastProperties: Optional[TimeBasedForecastProperties] = None
    Scenario: Optional[ForecastScenario] = None


class AxisDataOptionsOutput(BaseValidatorModel):
    NumericAxisOptions: Optional[NumericAxisOptionsOutput] = None
    DateAxisOptions: Optional[DateAxisOptions] = None


class AxisDataOptions(BaseValidatorModel):
    NumericAxisOptions: Optional[NumericAxisOptions] = None
    DateAxisOptions: Optional[DateAxisOptions] = None


class ApplicationTheme(BaseValidatorModel):
    BrandColorPalette: Optional[BrandColorPalette] = None
    BrandElementStyle: Optional[BrandElementStyle] = None


class TopicIRFilterOption(BaseValidatorModel):
    FilterType: Optional[TopicIRFilterTypeType] = None
    FilterClass: Optional[FilterClassType] = None
    OperandField: Optional[Identifier] = None
    Function: Optional[TopicIRFilterFunctionType] = None
    Constant: Optional[TopicConstantValueUnion] = None
    Inverse: Optional[bool] = None
    NullFilter: Optional[NullFilterOptionType] = None
    Aggregation: Optional[AggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None
    AggregationPartitionBy: Optional[List[AggregationPartitionBy]] = None
    Range: Optional[TopicConstantValueUnion] = None
    Inclusive: Optional[bool] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    LastNextOffset: Optional[TopicConstantValueUnion] = None
    AggMetrics: Optional[List[FilterAggMetrics]] = None
    TopBottomLimit: Optional[TopicConstantValueUnion] = None
    SortDirection: Optional[TopicSortDirectionType] = None
    Anchor: Optional[Anchor] = None


class TransformOperationOutput(BaseValidatorModel):
    ProjectOperation: Optional[ProjectOperationOutput] = None
    FilterOperation: Optional[FilterOperation] = None
    CreateColumnsOperation: Optional[CreateColumnsOperationOutput] = None
    RenameColumnOperation: Optional[RenameColumnOperation] = None
    CastColumnTypeOperation: Optional[CastColumnTypeOperation] = None
    TagColumnOperation: Optional[TagColumnOperationOutput] = None
    UntagColumnOperation: Optional[UntagColumnOperationOutput] = None
    OverrideDatasetParameterOperation: Optional[OverrideDatasetParameterOperationOutput] = None

TagColumnOperationUnion = Union[TagColumnOperation, TagColumnOperationOutput]


class SetParameterValueConfigurationOutput(BaseValidatorModel):
    DestinationParameterName: str
    Value: DestinationParameterValueConfigurationOutput


class VisualPaletteOutput(BaseValidatorModel):
    ChartColor: Optional[str] = None
    ColorMap: Optional[List[DataPathColor]] = None


class VisualPalette(BaseValidatorModel):
    ChartColor: Optional[str] = None
    ColorMap: Optional[List[DataPathColor]] = None


class PivotTableFieldCollapseStateOptionOutput(BaseValidatorModel):
    Target: PivotTableFieldCollapseStateTargetOutput
    State: Optional[PivotTableFieldCollapseStateType] = None


class PivotTableFieldCollapseStateOption(BaseValidatorModel):
    Target: PivotTableFieldCollapseStateTarget
    State: Optional[PivotTableFieldCollapseStateType] = None

DecimalDatasetParameterUnion = Union[DecimalDatasetParameter, DecimalDatasetParameterOutput]


class TopicCalculatedFieldOutput(BaseValidatorModel):
    CalculatedFieldName: str
    Expression: str
    CalculatedFieldDescription: Optional[str] = None
    CalculatedFieldSynonyms: Optional[List[str]] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    DefaultFormatting: Optional[DefaultFormatting] = None
    Aggregation: Optional[DefaultAggregationType] = None
    ComparativeOrder: Optional[ComparativeOrderOutput] = None
    SemanticType: Optional[SemanticTypeOutput] = None
    AllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[List[CellValueSynonymOutput]] = None
    NonAdditive: Optional[bool] = None


class TopicCalculatedField(BaseValidatorModel):
    CalculatedFieldName: str
    Expression: str
    CalculatedFieldDescription: Optional[str] = None
    CalculatedFieldSynonyms: Optional[List[str]] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    DefaultFormatting: Optional[DefaultFormatting] = None
    Aggregation: Optional[DefaultAggregationType] = None
    ComparativeOrder: Optional[ComparativeOrder] = None
    SemanticType: Optional[SemanticType] = None
    AllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[List[CellValueSynonym]] = None
    NonAdditive: Optional[bool] = None


class TopicColumnOutput(BaseValidatorModel):
    ColumnName: str
    ColumnFriendlyName: Optional[str] = None
    ColumnDescription: Optional[str] = None
    ColumnSynonyms: Optional[List[str]] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    Aggregation: Optional[DefaultAggregationType] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ComparativeOrder: Optional[ComparativeOrderOutput] = None
    SemanticType: Optional[SemanticTypeOutput] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    AllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    DefaultFormatting: Optional[DefaultFormatting] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[List[CellValueSynonymOutput]] = None
    NonAdditive: Optional[bool] = None


class TopicColumn(BaseValidatorModel):
    ColumnName: str
    ColumnFriendlyName: Optional[str] = None
    ColumnDescription: Optional[str] = None
    ColumnSynonyms: Optional[List[str]] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    Aggregation: Optional[DefaultAggregationType] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ComparativeOrder: Optional[ComparativeOrder] = None
    SemanticType: Optional[SemanticType] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    AllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    DefaultFormatting: Optional[DefaultFormatting] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[List[CellValueSynonym]] = None
    NonAdditive: Optional[bool] = None

TopicIRMetricUnion = Union[TopicIRMetric, TopicIRMetricOutput]


class ContributionAnalysisTimeRangesOutput(BaseValidatorModel):
    StartRange: Optional[TopicIRFilterOptionOutput] = None
    EndRange: Optional[TopicIRFilterOptionOutput] = None


class ChartAxisLabelOptionsOutput(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    SortIconVisibility: Optional[VisibilityType] = None
    AxisLabelOptions: Optional[List[AxisLabelOptions]] = None


class ChartAxisLabelOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    SortIconVisibility: Optional[VisibilityType] = None
    AxisLabelOptions: Optional[List[AxisLabelOptions]] = None


class AxisTickLabelOptions(BaseValidatorModel):
    LabelOptions: Optional[LabelOptions] = None
    RotationAngle: Optional[float] = None


class DateTimePickerControlDisplayOptions(BaseValidatorModel):
    TitleOptions: Optional[LabelOptions] = None
    DateTimeFormat: Optional[str] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None
    HelperTextVisibility: Optional[VisibilityType] = None
    DateIconVisibility: Optional[VisibilityType] = None


class DropDownControlDisplayOptions(BaseValidatorModel):
    SelectAllOptions: Optional[ListControlSelectAllOptions] = None
    TitleOptions: Optional[LabelOptions] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None


class LegendOptions(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    Title: Optional[LabelOptions] = None
    Position: Optional[LegendPositionType] = None
    Width: Optional[str] = None
    Height: Optional[str] = None
    ValueFontConfiguration: Optional[FontConfiguration] = None


class ListControlDisplayOptions(BaseValidatorModel):
    SearchOptions: Optional[ListControlSearchOptions] = None
    SelectAllOptions: Optional[ListControlSelectAllOptions] = None
    TitleOptions: Optional[LabelOptions] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None


class RelativeDateTimeControlDisplayOptions(BaseValidatorModel):
    TitleOptions: Optional[LabelOptions] = None
    DateTimeFormat: Optional[str] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None


class SliderControlDisplayOptions(BaseValidatorModel):
    TitleOptions: Optional[LabelOptions] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None


class TextAreaControlDisplayOptions(BaseValidatorModel):
    TitleOptions: Optional[LabelOptions] = None
    PlaceholderOptions: Optional[TextControlPlaceholderOptions] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None


class TextFieldControlDisplayOptions(BaseValidatorModel):
    TitleOptions: Optional[LabelOptions] = None
    PlaceholderOptions: Optional[TextControlPlaceholderOptions] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptions] = None


class PanelConfiguration(BaseValidatorModel):
    Title: Optional[PanelTitleOptions] = None
    BorderVisibility: Optional[VisibilityType] = None
    BorderThickness: Optional[str] = None
    BorderStyle: Optional[PanelBorderStyleType] = None
    BorderColor: Optional[str] = None
    GutterVisibility: Optional[VisibilityType] = None
    GutterSpacing: Optional[str] = None
    BackgroundVisibility: Optional[VisibilityType] = None
    BackgroundColor: Optional[str] = None


class TableFieldLinkContentConfiguration(BaseValidatorModel):
    CustomTextContent: Optional[TableFieldCustomTextContent] = None
    CustomIconContent: Optional[TableFieldCustomIconContent] = None

ColumnGroupUnion = Union[ColumnGroup, ColumnGroupOutput]


class GeospatialPointStyleOptionsOutput(BaseValidatorModel):
    SelectedPointStyle: Optional[GeospatialSelectedPointStyleType] = None
    ClusterMarkerConfiguration: Optional[ClusterMarkerConfiguration] = None
    HeatmapConfiguration: Optional[GeospatialHeatmapConfigurationOutput] = None


class GeospatialPointStyleOptions(BaseValidatorModel):
    SelectedPointStyle: Optional[GeospatialSelectedPointStyleType] = None
    ClusterMarkerConfiguration: Optional[ClusterMarkerConfiguration] = None
    HeatmapConfiguration: Optional[GeospatialHeatmapConfiguration] = None


class GeospatialColorOutput(BaseValidatorModel):
    Solid: Optional[GeospatialSolidColor] = None
    Gradient: Optional[GeospatialGradientColorOutput] = None
    Categorical: Optional[GeospatialCategoricalColorOutput] = None


class GeospatialColor(BaseValidatorModel):
    Solid: Optional[GeospatialSolidColor] = None
    Gradient: Optional[GeospatialGradientColor] = None
    Categorical: Optional[GeospatialCategoricalColor] = None


class TableCellStyle(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfiguration] = None
    TextWrap: Optional[TextWrapType] = None
    HorizontalTextAlignment: Optional[HorizontalTextAlignmentType] = None
    VerticalTextAlignment: Optional[VerticalTextAlignmentType] = None
    BackgroundColor: Optional[str] = None
    Height: Optional[int] = None
    Border: Optional[GlobalTableBorderOptions] = None


class ConditionalFormattingColorOutput(BaseValidatorModel):
    Solid: Optional[ConditionalFormattingSolidColor] = None
    Gradient: Optional[ConditionalFormattingGradientColorOutput] = None


class ConditionalFormattingColor(BaseValidatorModel):
    Solid: Optional[ConditionalFormattingSolidColor] = None
    Gradient: Optional[ConditionalFormattingGradientColor] = None


class DefaultInteractiveLayoutConfiguration(BaseValidatorModel):
    Grid: Optional[DefaultGridLayoutConfiguration] = None
    FreeForm: Optional[DefaultFreeFormLayoutConfiguration] = None


class SheetControlLayoutConfigurationOutput(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfigurationOutput] = None


class SheetControlLayoutConfiguration(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfiguration] = None


class LogoSetConfiguration(BaseValidatorModel):
    Primary: ImageSetConfiguration
    Favicon: Optional[ImageSetConfiguration] = None


class LogoSet(BaseValidatorModel):
    Primary: ImageSet
    Favicon: Optional[ImageSet] = None


class DataSetRefreshProperties(BaseValidatorModel):
    RefreshConfiguration: RefreshConfiguration

IntegerDatasetParameterUnion = Union[IntegerDatasetParameter, IntegerDatasetParameterOutput]


class SeriesItem(BaseValidatorModel):
    FieldSeriesItem: Optional[FieldSeriesItem] = None
    DataFieldSeriesItem: Optional[DataFieldSeriesItem] = None


class ThemeConfigurationOutput(BaseValidatorModel):
    DataColorPalette: Optional[DataColorPaletteOutput] = None
    UIColorPalette: Optional[UIColorPalette] = None
    Sheet: Optional[SheetStyle] = None
    Typography: Optional[TypographyOutput] = None


class ThemeConfiguration(BaseValidatorModel):
    DataColorPalette: Optional[DataColorPalette] = None
    UIColorPalette: Optional[UIColorPalette] = None
    Sheet: Optional[SheetStyle] = None
    Typography: Optional[Typography] = None


class ComparisonFormatConfiguration(BaseValidatorModel):
    NumberDisplayFormatConfiguration: Optional[NumberDisplayFormatConfiguration] = None
    PercentageDisplayFormatConfiguration: Optional[PercentageDisplayFormatConfiguration] = None


class NumericFormatConfiguration(BaseValidatorModel):
    NumberDisplayFormatConfiguration: Optional[NumberDisplayFormatConfiguration] = None
    CurrencyDisplayFormatConfiguration: Optional[CurrencyDisplayFormatConfiguration] = None
    PercentageDisplayFormatConfiguration: Optional[PercentageDisplayFormatConfiguration] = None


class AggregationSortConfiguration(BaseValidatorModel):
    Column: ColumnIdentifier
    SortDirection: SortDirectionType
    AggregationFunction: Optional[AggregationFunction] = None


class ColumnSort(BaseValidatorModel):
    SortBy: ColumnIdentifier
    Direction: SortDirectionType
    AggregationFunction: Optional[AggregationFunction] = None


class ColumnTooltipItem(BaseValidatorModel):
    Column: ColumnIdentifier
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    Aggregation: Optional[AggregationFunction] = None
    TooltipTarget: Optional[TooltipTargetType] = None


class ReferenceLineDynamicDataConfiguration(BaseValidatorModel):
    Column: ColumnIdentifier
    Calculation: NumericalAggregationFunction
    MeasureAggregationFunction: Optional[AggregationFunction] = None


class TopicFilterOutput(BaseValidatorModel):
    FilterName: str
    OperandFieldName: str
    FilterDescription: Optional[str] = None
    FilterClass: Optional[FilterClassType] = None
    FilterSynonyms: Optional[List[str]] = None
    FilterType: Optional[NamedFilterTypeType] = None
    CategoryFilter: Optional[TopicCategoryFilterOutput] = None
    NumericEqualityFilter: Optional[TopicNumericEqualityFilter] = None
    NumericRangeFilter: Optional[TopicNumericRangeFilter] = None
    DateRangeFilter: Optional[TopicDateRangeFilter] = None
    RelativeDateFilter: Optional[TopicRelativeDateFilter] = None


class TopicFilter(BaseValidatorModel):
    FilterName: str
    OperandFieldName: str
    FilterDescription: Optional[str] = None
    FilterClass: Optional[FilterClassType] = None
    FilterSynonyms: Optional[List[str]] = None
    FilterType: Optional[NamedFilterTypeType] = None
    CategoryFilter: Optional[TopicCategoryFilter] = None
    NumericEqualityFilter: Optional[TopicNumericEqualityFilter] = None
    NumericRangeFilter: Optional[TopicNumericRangeFilter] = None
    DateRangeFilter: Optional[TopicDateRangeFilter] = None
    RelativeDateFilter: Optional[TopicRelativeDateFilter] = None

RedshiftParametersUnion = Union[RedshiftParameters, RedshiftParametersOutput]


class DescribeRefreshScheduleResponse(BaseValidatorModel):
    RefreshSchedule: RefreshScheduleOutput
    Status: int
    RequestId: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class ListRefreshSchedulesResponse(BaseValidatorModel):
    RefreshSchedules: List[RefreshScheduleOutput]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata

RefreshScheduleUnion = Union[RefreshSchedule, RefreshScheduleOutput]


class RegisteredUserEmbeddingExperienceConfiguration(BaseValidatorModel):
    Dashboard: Optional[RegisteredUserDashboardEmbeddingConfiguration] = None
    QuickSightConsole: Optional[RegisteredUserQuickSightConsoleEmbeddingConfiguration] = None
    QSearchBar: Optional[RegisteredUserQSearchBarEmbeddingConfiguration] = None
    DashboardVisual: Optional[RegisteredUserDashboardVisualEmbeddingConfiguration] = None
    GenerativeQnA: Optional[RegisteredUserGenerativeQnAEmbeddingConfiguration] = None


class SnapshotJobResultFileGroup(BaseValidatorModel):
    Files: Optional[List[SnapshotFileOutput]] = None
    S3Results: Optional[List[SnapshotJobS3Result]] = None


class PhysicalTable(BaseValidatorModel):
    RelationalTable: Optional[RelationalTableUnion] = None
    CustomSql: Optional[CustomSqlUnion] = None
    S3Source: Optional[S3SourceUnion] = None


class DefaultSectionBasedLayoutConfiguration(BaseValidatorModel):
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptions


class FreeFormLayoutConfigurationOutput(BaseValidatorModel):
    Elements: List[FreeFormLayoutElementOutput]
    CanvasSizeOptions: Optional[FreeFormLayoutCanvasSizeOptions] = None


class FreeFormSectionLayoutConfigurationOutput(BaseValidatorModel):
    Elements: List[FreeFormLayoutElementOutput]


class FreeFormLayoutConfiguration(BaseValidatorModel):
    Elements: List[FreeFormLayoutElement]
    CanvasSizeOptions: Optional[FreeFormLayoutCanvasSizeOptions] = None


class FreeFormSectionLayoutConfiguration(BaseValidatorModel):
    Elements: List[FreeFormLayoutElement]


class SnapshotConfigurationOutput(BaseValidatorModel):
    FileGroups: List[SnapshotFileGroupOutput]
    DestinationConfiguration: Optional[SnapshotDestinationConfigurationOutput] = None
    Parameters: Optional[ParametersOutput] = None


class SnapshotConfiguration(BaseValidatorModel):
    FileGroups: List[SnapshotFileGroup]
    DestinationConfiguration: Optional[SnapshotDestinationConfiguration] = None
    Parameters: Optional[Parameters] = None


class StaticFile(BaseValidatorModel):
    ImageStaticFile: Optional[ImageStaticFile] = None
    SpatialStaticFile: Optional[SpatialStaticFile] = None

StringDatasetParameterUnion = Union[StringDatasetParameter, StringDatasetParameterOutput]


class ParameterDeclarationOutput(BaseValidatorModel):
    StringParameterDeclaration: Optional[StringParameterDeclarationOutput] = None
    DecimalParameterDeclaration: Optional[DecimalParameterDeclarationOutput] = None
    IntegerParameterDeclaration: Optional[IntegerParameterDeclarationOutput] = None
    DateTimeParameterDeclaration: Optional[DateTimeParameterDeclarationOutput] = None


class ParameterDeclaration(BaseValidatorModel):
    StringParameterDeclaration: Optional[StringParameterDeclaration] = None
    DecimalParameterDeclaration: Optional[DecimalParameterDeclaration] = None
    IntegerParameterDeclaration: Optional[IntegerParameterDeclaration] = None
    DateTimeParameterDeclaration: Optional[DateTimeParameterDeclaration] = None


class ColumnHierarchyOutput(BaseValidatorModel):
    ExplicitHierarchy: Optional[ExplicitHierarchyOutput] = None
    DateTimeHierarchy: Optional[DateTimeHierarchyOutput] = None
    PredefinedHierarchy: Optional[PredefinedHierarchyOutput] = None


class GenerateEmbedUrlForAnonymousUserRequest(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    AuthorizedResourceArns: List[str]
    ExperienceConfiguration: AnonymousUserEmbeddingExperienceConfiguration
    SessionLifetimeInMinutes: Optional[int] = None
    SessionTags: Optional[List[SessionTag]] = None
    AllowedDomains: Optional[List[str]] = None

AssetBundleImportJobOverridePermissionsUnion = Union[AssetBundleImportJobOverridePermissions, AssetBundleImportJobOverridePermissionsOutput]


class AssetBundleImportJobDataSourceOverrideParametersOutput(BaseValidatorModel):
    DataSourceId: str
    Name: Optional[str] = None
    DataSourceParameters: Optional[DataSourceParametersOutput] = None
    VpcConnectionProperties: Optional[VpcConnectionProperties] = None
    SslProperties: Optional[SslProperties] = None
    Credentials: Optional[AssetBundleImportJobDataSourceCredentials] = None


class DataSource(BaseValidatorModel):
    Arn: Optional[str] = None
    DataSourceId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    Status: Optional[ResourceStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    DataSourceParameters: Optional[DataSourceParametersOutput] = None
    AlternateDataSourceParameters: Optional[List[DataSourceParametersOutput]] = None
    VpcConnectionProperties: Optional[VpcConnectionProperties] = None
    SslProperties: Optional[SslProperties] = None
    ErrorInfo: Optional[DataSourceErrorInfo] = None
    SecretArn: Optional[str] = None


class SetParameterValueConfiguration(BaseValidatorModel):
    DestinationParameterName: str
    Value: DestinationParameterValueConfiguration

DateTimeDatasetParameterUnion = Union[DateTimeDatasetParameter, DateTimeDatasetParameterOutput]

OverrideDatasetParameterOperationUnion = Union[OverrideDatasetParameterOperation, OverrideDatasetParameterOperationOutput]


class ColumnHierarchy(BaseValidatorModel):
    ExplicitHierarchy: Optional[ExplicitHierarchy] = None
    DateTimeHierarchy: Optional[DateTimeHierarchy] = None
    PredefinedHierarchy: Optional[PredefinedHierarchy] = None

TopicIRFilterOptionUnion = Union[TopicIRFilterOption, TopicIRFilterOptionOutput]


class LogicalTableOutput(BaseValidatorModel):
    Alias: str
    Source: LogicalTableSource
    DataTransforms: Optional[List[TransformOperationOutput]] = None


class CustomActionSetParametersOperationOutput(BaseValidatorModel):
    ParameterValueConfigurations: List[SetParameterValueConfigurationOutput]


class PivotTableFieldOptionsOutput(BaseValidatorModel):
    SelectedFieldOptions: Optional[List[PivotTableFieldOption]] = None
    DataPathOptions: Optional[List[PivotTableDataPathOptionOutput]] = None
    CollapseStateOptions: Optional[List[PivotTableFieldCollapseStateOptionOutput]] = None


class PivotTableFieldOptions(BaseValidatorModel):
    SelectedFieldOptions: Optional[List[PivotTableFieldOption]] = None
    DataPathOptions: Optional[List[PivotTableDataPathOption]] = None
    CollapseStateOptions: Optional[List[PivotTableFieldCollapseStateOption]] = None


class TopicIRContributionAnalysisOutput(BaseValidatorModel):
    Factors: Optional[List[ContributionAnalysisFactor]] = None
    TimeRanges: Optional[ContributionAnalysisTimeRangesOutput] = None
    Direction: Optional[ContributionAnalysisDirectionType] = None
    SortType: Optional[ContributionAnalysisSortTypeType] = None


class AxisDisplayOptionsOutput(BaseValidatorModel):
    TickLabelOptions: Optional[AxisTickLabelOptions] = None
    AxisLineVisibility: Optional[VisibilityType] = None
    GridLineVisibility: Optional[VisibilityType] = None
    DataOptions: Optional[AxisDataOptionsOutput] = None
    ScrollbarOptions: Optional[ScrollBarOptions] = None
    AxisOffset: Optional[str] = None


class AxisDisplayOptions(BaseValidatorModel):
    TickLabelOptions: Optional[AxisTickLabelOptions] = None
    AxisLineVisibility: Optional[VisibilityType] = None
    GridLineVisibility: Optional[VisibilityType] = None
    DataOptions: Optional[AxisDataOptions] = None
    ScrollbarOptions: Optional[ScrollBarOptions] = None
    AxisOffset: Optional[str] = None


class DefaultDateTimePickerControlOptions(BaseValidatorModel):
    Type: Optional[SheetControlDateTimePickerTypeType] = None
    DisplayOptions: Optional[DateTimePickerControlDisplayOptions] = None
    CommitMode: Optional[CommitModeType] = None


class FilterDateTimePickerControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DateTimePickerControlDisplayOptions] = None
    Type: Optional[SheetControlDateTimePickerTypeType] = None
    CommitMode: Optional[CommitModeType] = None


class ParameterDateTimePickerControl(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DateTimePickerControlDisplayOptions] = None


class DefaultFilterDropDownControlOptionsOutput(BaseValidatorModel):
    DisplayOptions: Optional[DropDownControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutput] = None
    CommitMode: Optional[CommitModeType] = None


class DefaultFilterDropDownControlOptions(BaseValidatorModel):
    DisplayOptions: Optional[DropDownControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValues] = None
    CommitMode: Optional[CommitModeType] = None


class FilterDropDownControlOutput(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DropDownControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutput] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutput] = None
    CommitMode: Optional[CommitModeType] = None


class FilterDropDownControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DropDownControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValues] = None
    CascadingControlConfiguration: Optional[CascadingControlConfiguration] = None
    CommitMode: Optional[CommitModeType] = None


class ParameterDropDownControlOutput(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DropDownControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesOutput] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutput] = None
    CommitMode: Optional[CommitModeType] = None


class ParameterDropDownControl(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DropDownControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValues] = None
    CascadingControlConfiguration: Optional[CascadingControlConfiguration] = None
    CommitMode: Optional[CommitModeType] = None


class DefaultFilterListControlOptionsOutput(BaseValidatorModel):
    DisplayOptions: Optional[ListControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutput] = None


class DefaultFilterListControlOptions(BaseValidatorModel):
    DisplayOptions: Optional[ListControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValues] = None


class FilterListControlOutput(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[ListControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutput] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutput] = None


class FilterListControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[ListControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValues] = None
    CascadingControlConfiguration: Optional[CascadingControlConfiguration] = None


class ParameterListControlOutput(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[ListControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesOutput] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutput] = None


class ParameterListControl(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[ListControlDisplayOptions] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValues] = None
    CascadingControlConfiguration: Optional[CascadingControlConfiguration] = None


class DefaultRelativeDateTimeControlOptions(BaseValidatorModel):
    DisplayOptions: Optional[RelativeDateTimeControlDisplayOptions] = None
    CommitMode: Optional[CommitModeType] = None


class FilterRelativeDateTimeControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[RelativeDateTimeControlDisplayOptions] = None
    CommitMode: Optional[CommitModeType] = None


class DefaultSliderControlOptions(BaseValidatorModel):
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptions] = None
    Type: Optional[SheetControlSliderTypeType] = None


class FilterSliderControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptions] = None
    Type: Optional[SheetControlSliderTypeType] = None


class ParameterSliderControl(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptions] = None


class DefaultTextAreaControlOptions(BaseValidatorModel):
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptions] = None


class FilterTextAreaControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptions] = None


class ParameterTextAreaControl(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptions] = None


class DefaultTextFieldControlOptions(BaseValidatorModel):
    DisplayOptions: Optional[TextFieldControlDisplayOptions] = None


class FilterTextFieldControl(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[TextFieldControlDisplayOptions] = None


class ParameterTextFieldControl(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[TextFieldControlDisplayOptions] = None


class SmallMultiplesOptions(BaseValidatorModel):
    MaxVisibleRows: Optional[int] = None
    MaxVisibleColumns: Optional[int] = None
    PanelConfiguration: Optional[PanelConfiguration] = None
    XAxis: Optional[SmallMultiplesAxisProperties] = None
    YAxis: Optional[SmallMultiplesAxisProperties] = None


class TableFieldLinkConfiguration(BaseValidatorModel):
    Target: URLTargetConfigurationType
    Content: TableFieldLinkContentConfiguration


class GeospatialCircleSymbolStyleOutput(BaseValidatorModel):
    FillColor: Optional[GeospatialColorOutput] = None
    StrokeColor: Optional[GeospatialColorOutput] = None
    StrokeWidth: Optional[GeospatialLineWidth] = None
    CircleRadius: Optional[GeospatialCircleRadius] = None


class GeospatialLineSymbolStyleOutput(BaseValidatorModel):
    FillColor: Optional[GeospatialColorOutput] = None
    LineWidth: Optional[GeospatialLineWidth] = None


class GeospatialPolygonSymbolStyleOutput(BaseValidatorModel):
    FillColor: Optional[GeospatialColorOutput] = None
    StrokeColor: Optional[GeospatialColorOutput] = None
    StrokeWidth: Optional[GeospatialLineWidth] = None


class GeospatialCircleSymbolStyle(BaseValidatorModel):
    FillColor: Optional[GeospatialColor] = None
    StrokeColor: Optional[GeospatialColor] = None
    StrokeWidth: Optional[GeospatialLineWidth] = None
    CircleRadius: Optional[GeospatialCircleRadius] = None


class GeospatialLineSymbolStyle(BaseValidatorModel):
    FillColor: Optional[GeospatialColor] = None
    LineWidth: Optional[GeospatialLineWidth] = None


class GeospatialPolygonSymbolStyle(BaseValidatorModel):
    FillColor: Optional[GeospatialColor] = None
    StrokeColor: Optional[GeospatialColor] = None
    StrokeWidth: Optional[GeospatialLineWidth] = None


class PivotTableOptionsOutput(BaseValidatorModel):
    MetricPlacement: Optional[PivotTableMetricPlacementType] = None
    SingleMetricVisibility: Optional[VisibilityType] = None
    ColumnNamesVisibility: Optional[VisibilityType] = None
    ToggleButtonsVisibility: Optional[VisibilityType] = None
    ColumnHeaderStyle: Optional[TableCellStyle] = None
    RowHeaderStyle: Optional[TableCellStyle] = None
    CellStyle: Optional[TableCellStyle] = None
    RowFieldNamesStyle: Optional[TableCellStyle] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsOutput] = None
    CollapsedRowDimensionsVisibility: Optional[VisibilityType] = None
    RowsLayout: Optional[PivotTableRowsLayoutType] = None
    RowsLabelOptions: Optional[PivotTableRowsLabelOptions] = None
    DefaultCellWidth: Optional[str] = None


class PivotTableOptions(BaseValidatorModel):
    MetricPlacement: Optional[PivotTableMetricPlacementType] = None
    SingleMetricVisibility: Optional[VisibilityType] = None
    ColumnNamesVisibility: Optional[VisibilityType] = None
    ToggleButtonsVisibility: Optional[VisibilityType] = None
    ColumnHeaderStyle: Optional[TableCellStyle] = None
    RowHeaderStyle: Optional[TableCellStyle] = None
    CellStyle: Optional[TableCellStyle] = None
    RowFieldNamesStyle: Optional[TableCellStyle] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptions] = None
    CollapsedRowDimensionsVisibility: Optional[VisibilityType] = None
    RowsLayout: Optional[PivotTableRowsLayoutType] = None
    RowsLabelOptions: Optional[PivotTableRowsLabelOptions] = None
    DefaultCellWidth: Optional[str] = None


class PivotTotalOptionsOutput(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyle] = None
    ValueCellStyle: Optional[TableCellStyle] = None
    MetricHeaderCellStyle: Optional[TableCellStyle] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOption]] = None


class PivotTotalOptions(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyle] = None
    ValueCellStyle: Optional[TableCellStyle] = None
    MetricHeaderCellStyle: Optional[TableCellStyle] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOption]] = None


class SubtotalOptionsOutput(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None
    FieldLevel: Optional[PivotTableSubtotalLevelType] = None
    FieldLevelOptions: Optional[List[PivotTableFieldSubtotalOptions]] = None
    TotalCellStyle: Optional[TableCellStyle] = None
    ValueCellStyle: Optional[TableCellStyle] = None
    MetricHeaderCellStyle: Optional[TableCellStyle] = None
    StyleTargets: Optional[List[TableStyleTarget]] = None


class SubtotalOptions(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None
    FieldLevel: Optional[PivotTableSubtotalLevelType] = None
    FieldLevelOptions: Optional[List[PivotTableFieldSubtotalOptions]] = None
    TotalCellStyle: Optional[TableCellStyle] = None
    ValueCellStyle: Optional[TableCellStyle] = None
    MetricHeaderCellStyle: Optional[TableCellStyle] = None
    StyleTargets: Optional[List[TableStyleTarget]] = None


class TableOptionsOutput(BaseValidatorModel):
    Orientation: Optional[TableOrientationType] = None
    HeaderStyle: Optional[TableCellStyle] = None
    CellStyle: Optional[TableCellStyle] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsOutput] = None


class TableOptions(BaseValidatorModel):
    Orientation: Optional[TableOrientationType] = None
    HeaderStyle: Optional[TableCellStyle] = None
    CellStyle: Optional[TableCellStyle] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptions] = None


class TotalOptionsOutput(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyle] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOption]] = None


class TotalOptions(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyle] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOption]] = None


class GaugeChartArcConditionalFormattingOutput(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColorOutput] = None


class GaugeChartPrimaryValueConditionalFormattingOutput(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutput] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIActualValueConditionalFormattingOutput(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutput] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIComparisonValueConditionalFormattingOutput(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutput] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIPrimaryValueConditionalFormattingOutput(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutput] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIProgressBarConditionalFormattingOutput(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColorOutput] = None


class ShapeConditionalFormatOutput(BaseValidatorModel):
    BackgroundColor: ConditionalFormattingColorOutput


class TableRowConditionalFormattingOutput(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColorOutput] = None
    TextColor: Optional[ConditionalFormattingColorOutput] = None


class TextConditionalFormatOutput(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColorOutput] = None
    TextColor: Optional[ConditionalFormattingColorOutput] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class GaugeChartArcConditionalFormatting(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColor] = None


class GaugeChartPrimaryValueConditionalFormatting(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColor] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIActualValueConditionalFormatting(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColor] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIComparisonValueConditionalFormatting(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColor] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIPrimaryValueConditionalFormatting(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColor] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class KPIProgressBarConditionalFormatting(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColor] = None


class ShapeConditionalFormat(BaseValidatorModel):
    BackgroundColor: ConditionalFormattingColor


class TableRowConditionalFormatting(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColor] = None
    TextColor: Optional[ConditionalFormattingColor] = None


class TextConditionalFormat(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColor] = None
    TextColor: Optional[ConditionalFormattingColor] = None
    Icon: Optional[ConditionalFormattingIcon] = None


class SheetControlLayoutOutput(BaseValidatorModel):
    Configuration: SheetControlLayoutConfigurationOutput


class SheetControlLayout(BaseValidatorModel):
    Configuration: SheetControlLayoutConfiguration


class LogoConfiguration(BaseValidatorModel):
    AltText: str
    LogoSet: LogoSetConfiguration


class Logo(BaseValidatorModel):
    AltText: str
    LogoSet: LogoSet


class DescribeDataSetRefreshPropertiesResponse(BaseValidatorModel):
    RequestId: str
    Status: int
    DataSetRefreshProperties: DataSetRefreshProperties
    ResponseMetadata: ResponseMetadata


class PutDataSetRefreshPropertiesRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    DataSetRefreshProperties: DataSetRefreshProperties


class ThemeVersion(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    BaseThemeId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Configuration: Optional[ThemeConfigurationOutput] = None
    Errors: Optional[List[ThemeError]] = None
    Status: Optional[ResourceStatusType] = None

ThemeConfigurationUnion = Union[ThemeConfiguration, ThemeConfigurationOutput]


class ComparisonConfiguration(BaseValidatorModel):
    ComparisonMethod: Optional[ComparisonMethodType] = None
    ComparisonFormat: Optional[ComparisonFormatConfiguration] = None


class DateTimeFormatConfiguration(BaseValidatorModel):
    DateTimeFormat: Optional[str] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfiguration] = None
    NumericFormatConfiguration: Optional[NumericFormatConfiguration] = None


class NumberFormatConfiguration(BaseValidatorModel):
    FormatConfiguration: Optional[NumericFormatConfiguration] = None


class ReferenceLineValueLabelConfiguration(BaseValidatorModel):
    RelativePosition: Optional[ReferenceLineValueLabelRelativePositionType] = None
    FormatConfiguration: Optional[NumericFormatConfiguration] = None


class StringFormatConfiguration(BaseValidatorModel):
    NullValueFormatConfiguration: Optional[NullValueFormatConfiguration] = None
    NumericFormatConfiguration: Optional[NumericFormatConfiguration] = None


class BodySectionDynamicCategoryDimensionConfigurationOutput(BaseValidatorModel):
    Column: ColumnIdentifier
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSort]] = None


class BodySectionDynamicCategoryDimensionConfiguration(BaseValidatorModel):
    Column: ColumnIdentifier
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSort]] = None


class BodySectionDynamicNumericDimensionConfigurationOutput(BaseValidatorModel):
    Column: ColumnIdentifier
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSort]] = None


class BodySectionDynamicNumericDimensionConfiguration(BaseValidatorModel):
    Column: ColumnIdentifier
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSort]] = None


class FieldSortOptions(BaseValidatorModel):
    FieldSort: Optional[FieldSort] = None
    ColumnSort: Optional[ColumnSort] = None


class PivotTableSortByOutput(BaseValidatorModel):
    Field: Optional[FieldSort] = None
    Column: Optional[ColumnSort] = None
    DataPath: Optional[DataPathSortOutput] = None


class PivotTableSortBy(BaseValidatorModel):
    Field: Optional[FieldSort] = None
    Column: Optional[ColumnSort] = None
    DataPath: Optional[DataPathSort] = None


class TooltipItem(BaseValidatorModel):
    FieldTooltipItem: Optional[FieldTooltipItem] = None
    ColumnTooltipItem: Optional[ColumnTooltipItem] = None


class ReferenceLineDataConfiguration(BaseValidatorModel):
    StaticConfiguration: Optional[ReferenceLineStaticDataConfiguration] = None
    DynamicConfiguration: Optional[ReferenceLineDynamicDataConfiguration] = None
    AxisBinding: Optional[AxisBindingType] = None
    SeriesType: Optional[ReferenceLineSeriesTypeType] = None


class DatasetMetadataOutput(BaseValidatorModel):
    DatasetArn: str
    DatasetName: Optional[str] = None
    DatasetDescription: Optional[str] = None
    DataAggregation: Optional[DataAggregation] = None
    Filters: Optional[List[TopicFilterOutput]] = None
    Columns: Optional[List[TopicColumnOutput]] = None
    CalculatedFields: Optional[List[TopicCalculatedFieldOutput]] = None
    NamedEntities: Optional[List[TopicNamedEntityOutput]] = None


class DatasetMetadata(BaseValidatorModel):
    DatasetArn: str
    DatasetName: Optional[str] = None
    DatasetDescription: Optional[str] = None
    DataAggregation: Optional[DataAggregation] = None
    Filters: Optional[List[TopicFilter]] = None
    Columns: Optional[List[TopicColumn]] = None
    CalculatedFields: Optional[List[TopicCalculatedField]] = None
    NamedEntities: Optional[List[TopicNamedEntity]] = None


class DataSourceParameters(BaseValidatorModel):
    AmazonElasticsearchParameters: Optional[AmazonElasticsearchParameters] = None
    AthenaParameters: Optional[AthenaParameters] = None
    AuroraParameters: Optional[AuroraParameters] = None
    AuroraPostgreSqlParameters: Optional[AuroraPostgreSqlParameters] = None
    AwsIotAnalyticsParameters: Optional[AwsIotAnalyticsParameters] = None
    JiraParameters: Optional[JiraParameters] = None
    MariaDbParameters: Optional[MariaDbParameters] = None
    MySqlParameters: Optional[MySqlParameters] = None
    OracleParameters: Optional[OracleParameters] = None
    PostgreSqlParameters: Optional[PostgreSqlParameters] = None
    PrestoParameters: Optional[PrestoParameters] = None
    RdsParameters: Optional[RdsParameters] = None
    RedshiftParameters: Optional[RedshiftParametersUnion] = None
    S3Parameters: Optional[S3Parameters] = None
    ServiceNowParameters: Optional[ServiceNowParameters] = None
    SnowflakeParameters: Optional[SnowflakeParameters] = None
    SparkParameters: Optional[SparkParameters] = None
    SqlServerParameters: Optional[SqlServerParameters] = None
    TeradataParameters: Optional[TeradataParameters] = None
    TwitterParameters: Optional[TwitterParameters] = None
    AmazonOpenSearchParameters: Optional[AmazonOpenSearchParameters] = None
    ExasolParameters: Optional[ExasolParameters] = None
    DatabricksParameters: Optional[DatabricksParameters] = None
    StarburstParameters: Optional[StarburstParameters] = None
    TrinoParameters: Optional[TrinoParameters] = None
    BigQueryParameters: Optional[BigQueryParameters] = None


class CreateRefreshScheduleRequest(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    Schedule: RefreshScheduleUnion


class UpdateRefreshScheduleRequest(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    Schedule: RefreshScheduleUnion


class GenerateEmbedUrlForRegisteredUserRequest(BaseValidatorModel):
    AwsAccountId: str
    UserArn: str
    ExperienceConfiguration: RegisteredUserEmbeddingExperienceConfiguration
    SessionLifetimeInMinutes: Optional[int] = None
    AllowedDomains: Optional[List[str]] = None


class GenerateEmbedUrlForRegisteredUserWithIdentityRequest(BaseValidatorModel):
    AwsAccountId: str
    ExperienceConfiguration: RegisteredUserEmbeddingExperienceConfiguration
    SessionLifetimeInMinutes: Optional[int] = None
    AllowedDomains: Optional[List[str]] = None


class AnonymousUserSnapshotJobResult(BaseValidatorModel):
    FileGroups: Optional[List[SnapshotJobResultFileGroup]] = None

PhysicalTableUnion = Union[PhysicalTable, PhysicalTableOutput]


class DefaultPaginatedLayoutConfiguration(BaseValidatorModel):
    SectionBased: Optional[DefaultSectionBasedLayoutConfiguration] = None


class SectionLayoutConfigurationOutput(BaseValidatorModel):
    FreeFormLayout: FreeFormSectionLayoutConfigurationOutput


class SectionLayoutConfiguration(BaseValidatorModel):
    FreeFormLayout: FreeFormSectionLayoutConfiguration


class DescribeDashboardSnapshotJobResponse(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str
    UserConfiguration: SnapshotUserConfigurationRedacted
    SnapshotConfiguration: SnapshotConfigurationOutput
    Arn: str
    JobStatus: SnapshotJobStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata

SnapshotConfigurationUnion = Union[SnapshotConfiguration, SnapshotConfigurationOutput]


class AssetBundleImportJobOverrideParametersOutput(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[AssetBundleImportJobResourceIdOverrideConfiguration] = None
    VPCConnections: Optional[List[AssetBundleImportJobVPCConnectionOverrideParametersOutput]] = None
    RefreshSchedules: Optional[List[AssetBundleImportJobRefreshScheduleOverrideParametersOutput]] = None
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverrideParametersOutput]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideParameters]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideParameters]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideParameters]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideParameters]] = None
    Folders: Optional[List[AssetBundleImportJobFolderOverrideParameters]] = None


class DescribeDataSourceResponse(BaseValidatorModel):
    DataSource: DataSource
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ListDataSourcesResponse(BaseValidatorModel):
    DataSources: List[DataSource]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CustomActionSetParametersOperation(BaseValidatorModel):
    ParameterValueConfigurations: List[SetParameterValueConfiguration]


class DatasetParameter(BaseValidatorModel):
    StringDatasetParameter: Optional[StringDatasetParameterUnion] = None
    DecimalDatasetParameter: Optional[DecimalDatasetParameterUnion] = None
    IntegerDatasetParameter: Optional[IntegerDatasetParameterUnion] = None
    DateTimeDatasetParameter: Optional[DateTimeDatasetParameterUnion] = None


class TransformOperation(BaseValidatorModel):
    ProjectOperation: Optional[ProjectOperationUnion] = None
    FilterOperation: Optional[FilterOperation] = None
    CreateColumnsOperation: Optional[CreateColumnsOperationUnion] = None
    RenameColumnOperation: Optional[RenameColumnOperation] = None
    CastColumnTypeOperation: Optional[CastColumnTypeOperation] = None
    TagColumnOperation: Optional[TagColumnOperationUnion] = None
    UntagColumnOperation: Optional[UntagColumnOperationUnion] = None
    OverrideDatasetParameterOperation: Optional[OverrideDatasetParameterOperationUnion] = None


class ContributionAnalysisTimeRanges(BaseValidatorModel):
    StartRange: Optional[TopicIRFilterOptionUnion] = None
    EndRange: Optional[TopicIRFilterOptionUnion] = None


class DataSet(BaseValidatorModel):
    Arn: Optional[str] = None
    DataSetId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    PhysicalTableMap: Optional[Dict[str, PhysicalTableOutput]] = None
    LogicalTableMap: Optional[Dict[str, LogicalTableOutput]] = None
    OutputColumns: Optional[List[OutputColumn]] = None
    ImportMode: Optional[DataSetImportModeType] = None
    ConsumedSpiceCapacityInBytes: Optional[int] = None
    ColumnGroups: Optional[List[ColumnGroupOutput]] = None
    FieldFolders: Optional[Dict[str, FieldFolderOutput]] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSet] = None
    RowLevelPermissionTagConfiguration: Optional[RowLevelPermissionTagConfigurationOutput] = None
    ColumnLevelPermissionRules: Optional[List[ColumnLevelPermissionRuleOutput]] = None
    DataSetUsageConfiguration: Optional[DataSetUsageConfiguration] = None
    DatasetParameters: Optional[List[DatasetParameterOutput]] = None
    PerformanceConfiguration: Optional[PerformanceConfigurationOutput] = None


class ImageCustomActionOperationOutput(BaseValidatorModel):
    NavigationOperation: Optional[CustomActionNavigationOperation] = None
    URLOperation: Optional[CustomActionURLOperation] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationOutput] = None


class LayerCustomActionOperationOutput(BaseValidatorModel):
    FilterOperation: Optional[CustomActionFilterOperationOutput] = None
    NavigationOperation: Optional[CustomActionNavigationOperation] = None
    URLOperation: Optional[CustomActionURLOperation] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationOutput] = None


class VisualCustomActionOperationOutput(BaseValidatorModel):
    FilterOperation: Optional[CustomActionFilterOperationOutput] = None
    NavigationOperation: Optional[CustomActionNavigationOperation] = None
    URLOperation: Optional[CustomActionURLOperation] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationOutput] = None


class TopicIROutput(BaseValidatorModel):
    Metrics: Optional[List[TopicIRMetricOutput]] = None
    GroupByList: Optional[List[TopicIRGroupBy]] = None
    Filters: Optional[List[List[TopicIRFilterOptionOutput]]] = None
    Sort: Optional[TopicSortClause] = None
    ContributionAnalysis: Optional[TopicIRContributionAnalysisOutput] = None
    Visual: Optional[VisualOptions] = None


class LineSeriesAxisDisplayOptionsOutput(BaseValidatorModel):
    AxisOptions: Optional[AxisDisplayOptionsOutput] = None
    MissingDataConfigurations: Optional[List[MissingDataConfiguration]] = None


class LineSeriesAxisDisplayOptions(BaseValidatorModel):
    AxisOptions: Optional[AxisDisplayOptions] = None
    MissingDataConfigurations: Optional[List[MissingDataConfiguration]] = None


class DefaultFilterControlOptionsOutput(BaseValidatorModel):
    DefaultDateTimePickerOptions: Optional[DefaultDateTimePickerControlOptions] = None
    DefaultListOptions: Optional[DefaultFilterListControlOptionsOutput] = None
    DefaultDropdownOptions: Optional[DefaultFilterDropDownControlOptionsOutput] = None
    DefaultTextFieldOptions: Optional[DefaultTextFieldControlOptions] = None
    DefaultTextAreaOptions: Optional[DefaultTextAreaControlOptions] = None
    DefaultSliderOptions: Optional[DefaultSliderControlOptions] = None
    DefaultRelativeDateTimeOptions: Optional[DefaultRelativeDateTimeControlOptions] = None


class DefaultFilterControlOptions(BaseValidatorModel):
    DefaultDateTimePickerOptions: Optional[DefaultDateTimePickerControlOptions] = None
    DefaultListOptions: Optional[DefaultFilterListControlOptions] = None
    DefaultDropdownOptions: Optional[DefaultFilterDropDownControlOptions] = None
    DefaultTextFieldOptions: Optional[DefaultTextFieldControlOptions] = None
    DefaultTextAreaOptions: Optional[DefaultTextAreaControlOptions] = None
    DefaultSliderOptions: Optional[DefaultSliderControlOptions] = None
    DefaultRelativeDateTimeOptions: Optional[DefaultRelativeDateTimeControlOptions] = None


class FilterControlOutput(BaseValidatorModel):
    DateTimePicker: Optional[FilterDateTimePickerControl] = None
    List: Optional[FilterListControlOutput] = None
    Dropdown: Optional[FilterDropDownControlOutput] = None
    TextField: Optional[FilterTextFieldControl] = None
    TextArea: Optional[FilterTextAreaControl] = None
    Slider: Optional[FilterSliderControl] = None
    RelativeDateTime: Optional[FilterRelativeDateTimeControl] = None
    CrossSheet: Optional[FilterCrossSheetControlOutput] = None


class FilterControl(BaseValidatorModel):
    DateTimePicker: Optional[FilterDateTimePickerControl] = None
    List: Optional[FilterListControl] = None
    Dropdown: Optional[FilterDropDownControl] = None
    TextField: Optional[FilterTextFieldControl] = None
    TextArea: Optional[FilterTextAreaControl] = None
    Slider: Optional[FilterSliderControl] = None
    RelativeDateTime: Optional[FilterRelativeDateTimeControl] = None
    CrossSheet: Optional[FilterCrossSheetControl] = None


class ParameterControlOutput(BaseValidatorModel):
    DateTimePicker: Optional[ParameterDateTimePickerControl] = None
    List: Optional[ParameterListControlOutput] = None
    Dropdown: Optional[ParameterDropDownControlOutput] = None
    TextField: Optional[ParameterTextFieldControl] = None
    TextArea: Optional[ParameterTextAreaControl] = None
    Slider: Optional[ParameterSliderControl] = None


class ParameterControl(BaseValidatorModel):
    DateTimePicker: Optional[ParameterDateTimePickerControl] = None
    List: Optional[ParameterListControl] = None
    Dropdown: Optional[ParameterDropDownControl] = None
    TextField: Optional[ParameterTextFieldControl] = None
    TextArea: Optional[ParameterTextAreaControl] = None
    Slider: Optional[ParameterSliderControl] = None


class TableFieldURLConfiguration(BaseValidatorModel):
    LinkConfiguration: Optional[TableFieldLinkConfiguration] = None
    ImageConfiguration: Optional[TableFieldImageConfiguration] = None


class GeospatialPointStyleOutput(BaseValidatorModel):
    CircleSymbolStyle: Optional[GeospatialCircleSymbolStyleOutput] = None


class GeospatialLineStyleOutput(BaseValidatorModel):
    LineSymbolStyle: Optional[GeospatialLineSymbolStyleOutput] = None


class GeospatialPolygonStyleOutput(BaseValidatorModel):
    PolygonSymbolStyle: Optional[GeospatialPolygonSymbolStyleOutput] = None


class GeospatialPointStyle(BaseValidatorModel):
    CircleSymbolStyle: Optional[GeospatialCircleSymbolStyle] = None


class GeospatialLineStyle(BaseValidatorModel):
    LineSymbolStyle: Optional[GeospatialLineSymbolStyle] = None


class GeospatialPolygonStyle(BaseValidatorModel):
    PolygonSymbolStyle: Optional[GeospatialPolygonSymbolStyle] = None


class PivotTableTotalOptionsOutput(BaseValidatorModel):
    RowSubtotalOptions: Optional[SubtotalOptionsOutput] = None
    ColumnSubtotalOptions: Optional[SubtotalOptionsOutput] = None
    RowTotalOptions: Optional[PivotTotalOptionsOutput] = None
    ColumnTotalOptions: Optional[PivotTotalOptionsOutput] = None


class PivotTableTotalOptions(BaseValidatorModel):
    RowSubtotalOptions: Optional[SubtotalOptions] = None
    ColumnSubtotalOptions: Optional[SubtotalOptions] = None
    RowTotalOptions: Optional[PivotTotalOptions] = None
    ColumnTotalOptions: Optional[PivotTotalOptions] = None


class GaugeChartConditionalFormattingOptionOutput(BaseValidatorModel):
    PrimaryValue: Optional[GaugeChartPrimaryValueConditionalFormattingOutput] = None
    Arc: Optional[GaugeChartArcConditionalFormattingOutput] = None


class KPIConditionalFormattingOptionOutput(BaseValidatorModel):
    PrimaryValue: Optional[KPIPrimaryValueConditionalFormattingOutput] = None
    ProgressBar: Optional[KPIProgressBarConditionalFormattingOutput] = None
    ActualValue: Optional[KPIActualValueConditionalFormattingOutput] = None
    ComparisonValue: Optional[KPIComparisonValueConditionalFormattingOutput] = None


class FilledMapShapeConditionalFormattingOutput(BaseValidatorModel):
    FieldId: str
    Format: Optional[ShapeConditionalFormatOutput] = None


class PivotTableCellConditionalFormattingOutput(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatOutput] = None
    Scope: Optional[PivotTableConditionalFormattingScope] = None
    Scopes: Optional[List[PivotTableConditionalFormattingScope]] = None


class TableCellConditionalFormattingOutput(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatOutput] = None


class GaugeChartConditionalFormattingOption(BaseValidatorModel):
    PrimaryValue: Optional[GaugeChartPrimaryValueConditionalFormatting] = None
    Arc: Optional[GaugeChartArcConditionalFormatting] = None


class KPIConditionalFormattingOption(BaseValidatorModel):
    PrimaryValue: Optional[KPIPrimaryValueConditionalFormatting] = None
    ProgressBar: Optional[KPIProgressBarConditionalFormatting] = None
    ActualValue: Optional[KPIActualValueConditionalFormatting] = None
    ComparisonValue: Optional[KPIComparisonValueConditionalFormatting] = None


class FilledMapShapeConditionalFormatting(BaseValidatorModel):
    FieldId: str
    Format: Optional[ShapeConditionalFormat] = None


class PivotTableCellConditionalFormatting(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormat] = None
    Scope: Optional[PivotTableConditionalFormattingScope] = None
    Scopes: Optional[List[PivotTableConditionalFormattingScope]] = None


class TableCellConditionalFormatting(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormat] = None


class BrandDefinition(BaseValidatorModel):
    BrandName: str
    Description: Optional[str] = None
    ApplicationTheme: Optional[ApplicationTheme] = None
    LogoConfiguration: Optional[LogoConfiguration] = None


class BrandDetail(BaseValidatorModel):
    BrandId: str
    Arn: Optional[str] = None
    BrandStatus: Optional[BrandStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    VersionId: Optional[str] = None
    VersionStatus: Optional[BrandVersionStatusType] = None
    Errors: Optional[List[str]] = None
    Logo: Optional[Logo] = None


class Theme(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ThemeId: Optional[str] = None
    Version: Optional[ThemeVersion] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    Type: Optional[ThemeTypeType] = None


class CreateThemeRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    Name: str
    BaseThemeId: str
    Configuration: ThemeConfigurationUnion
    VersionDescription: Optional[str] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    Tags: Optional[List[Tag]] = None


class UpdateThemeRequest(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    BaseThemeId: str
    Name: Optional[str] = None
    VersionDescription: Optional[str] = None
    Configuration: Optional[ThemeConfigurationUnion] = None


class GaugeChartOptions(BaseValidatorModel):
    PrimaryValueDisplayType: Optional[PrimaryValueDisplayTypeType] = None
    Comparison: Optional[ComparisonConfiguration] = None
    ArcAxis: Optional[ArcAxisConfiguration] = None
    Arc: Optional[ArcConfiguration] = None
    PrimaryValueFontConfiguration: Optional[FontConfiguration] = None


class KPIOptions(BaseValidatorModel):
    ProgressBar: Optional[ProgressBarOptions] = None
    TrendArrows: Optional[TrendArrowOptions] = None
    SecondaryValue: Optional[SecondaryValueOptions] = None
    Comparison: Optional[ComparisonConfiguration] = None
    PrimaryValueDisplayType: Optional[PrimaryValueDisplayTypeType] = None
    PrimaryValueFontConfiguration: Optional[FontConfiguration] = None
    SecondaryValueFontConfiguration: Optional[FontConfiguration] = None
    Sparkline: Optional[KPISparklineOptions] = None
    VisualLayoutOptions: Optional[KPIVisualLayoutOptions] = None


class DateDimensionField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    DateGranularity: Optional[TimeGranularityType] = None
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[DateTimeFormatConfiguration] = None


class DateMeasureField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    AggregationFunction: Optional[DateAggregationFunctionType] = None
    FormatConfiguration: Optional[DateTimeFormatConfiguration] = None


class NumericalDimensionField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[NumberFormatConfiguration] = None


class NumericalMeasureField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    AggregationFunction: Optional[NumericalAggregationFunction] = None
    FormatConfiguration: Optional[NumberFormatConfiguration] = None


class ReferenceLineLabelConfiguration(BaseValidatorModel):
    ValueLabelConfiguration: Optional[ReferenceLineValueLabelConfiguration] = None
    CustomLabelConfiguration: Optional[ReferenceLineCustomLabelConfiguration] = None
    FontConfiguration: Optional[FontConfiguration] = None
    FontColor: Optional[str] = None
    HorizontalPosition: Optional[ReferenceLineLabelHorizontalPositionType] = None
    VerticalPosition: Optional[ReferenceLineLabelVerticalPositionType] = None


class CategoricalDimensionField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[StringFormatConfiguration] = None


class CategoricalMeasureField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    AggregationFunction: Optional[CategoricalAggregationFunctionType] = None
    FormatConfiguration: Optional[StringFormatConfiguration] = None


class FormatConfiguration(BaseValidatorModel):
    StringFormatConfiguration: Optional[StringFormatConfiguration] = None
    NumberFormatConfiguration: Optional[NumberFormatConfiguration] = None
    DateTimeFormatConfiguration: Optional[DateTimeFormatConfiguration] = None


class BodySectionRepeatDimensionConfigurationOutput(BaseValidatorModel):
    DynamicCategoryDimensionConfiguration: Optional[BodySectionDynamicCategoryDimensionConfigurationOutput] = None
    DynamicNumericDimensionConfiguration: Optional[BodySectionDynamicNumericDimensionConfigurationOutput] = None


class BodySectionRepeatDimensionConfiguration(BaseValidatorModel):
    DynamicCategoryDimensionConfiguration: Optional[BodySectionDynamicCategoryDimensionConfiguration] = None
    DynamicNumericDimensionConfiguration: Optional[BodySectionDynamicNumericDimensionConfiguration] = None


class BarChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    ColorSort: Optional[List[FieldSortOptions]] = None
    ColorItemsLimit: Optional[ItemsLimitConfiguration] = None
    SmallMultiplesSort: Optional[List[FieldSortOptions]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class BarChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    ColorSort: Optional[List[FieldSortOptions]] = None
    ColorItemsLimit: Optional[ItemsLimitConfiguration] = None
    SmallMultiplesSort: Optional[List[FieldSortOptions]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class BoxPlotSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    PaginationConfiguration: Optional[PaginationConfiguration] = None


class BoxPlotSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    PaginationConfiguration: Optional[PaginationConfiguration] = None


class ComboChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    ColorSort: Optional[List[FieldSortOptions]] = None
    ColorItemsLimit: Optional[ItemsLimitConfiguration] = None


class ComboChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    ColorSort: Optional[List[FieldSortOptions]] = None
    ColorItemsLimit: Optional[ItemsLimitConfiguration] = None


class FilledMapSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None


class FilledMapSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None


class FunnelChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None


class FunnelChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None


class HeatMapSortConfigurationOutput(BaseValidatorModel):
    HeatMapRowSort: Optional[List[FieldSortOptions]] = None
    HeatMapColumnSort: Optional[List[FieldSortOptions]] = None
    HeatMapRowItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None
    HeatMapColumnItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class HeatMapSortConfiguration(BaseValidatorModel):
    HeatMapRowSort: Optional[List[FieldSortOptions]] = None
    HeatMapColumnSort: Optional[List[FieldSortOptions]] = None
    HeatMapRowItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None
    HeatMapColumnItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class KPISortConfigurationOutput(BaseValidatorModel):
    TrendGroupSort: Optional[List[FieldSortOptions]] = None


class KPISortConfiguration(BaseValidatorModel):
    TrendGroupSort: Optional[List[FieldSortOptions]] = None


class LineChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None
    ColorItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None
    SmallMultiplesSort: Optional[List[FieldSortOptions]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class LineChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None
    ColorItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None
    SmallMultiplesSort: Optional[List[FieldSortOptions]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class PieChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    SmallMultiplesSort: Optional[List[FieldSortOptions]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class PieChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    SmallMultiplesSort: Optional[List[FieldSortOptions]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class PluginVisualTableQuerySortOutput(BaseValidatorModel):
    RowSort: Optional[List[FieldSortOptions]] = None
    ItemsLimitConfiguration: Optional[PluginVisualItemsLimitConfiguration] = None


class PluginVisualTableQuerySort(BaseValidatorModel):
    RowSort: Optional[List[FieldSortOptions]] = None
    ItemsLimitConfiguration: Optional[PluginVisualItemsLimitConfiguration] = None


class RadarChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    ColorSort: Optional[List[FieldSortOptions]] = None
    ColorItemsLimit: Optional[ItemsLimitConfiguration] = None


class RadarChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    ColorSort: Optional[List[FieldSortOptions]] = None
    ColorItemsLimit: Optional[ItemsLimitConfiguration] = None


class SankeyDiagramSortConfigurationOutput(BaseValidatorModel):
    WeightSort: Optional[List[FieldSortOptions]] = None
    SourceItemsLimit: Optional[ItemsLimitConfiguration] = None
    DestinationItemsLimit: Optional[ItemsLimitConfiguration] = None


class SankeyDiagramSortConfiguration(BaseValidatorModel):
    WeightSort: Optional[List[FieldSortOptions]] = None
    SourceItemsLimit: Optional[ItemsLimitConfiguration] = None
    DestinationItemsLimit: Optional[ItemsLimitConfiguration] = None


class TableSortConfigurationOutput(BaseValidatorModel):
    RowSort: Optional[List[FieldSortOptions]] = None
    PaginationConfiguration: Optional[PaginationConfiguration] = None


class TableSortConfiguration(BaseValidatorModel):
    RowSort: Optional[List[FieldSortOptions]] = None
    PaginationConfiguration: Optional[PaginationConfiguration] = None


class TreeMapSortConfigurationOutput(BaseValidatorModel):
    TreeMapSort: Optional[List[FieldSortOptions]] = None
    TreeMapGroupItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class TreeMapSortConfiguration(BaseValidatorModel):
    TreeMapSort: Optional[List[FieldSortOptions]] = None
    TreeMapGroupItemsLimitConfiguration: Optional[ItemsLimitConfiguration] = None


class WaterfallChartSortConfigurationOutput(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    BreakdownItemsLimit: Optional[ItemsLimitConfiguration] = None


class WaterfallChartSortConfiguration(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptions]] = None
    BreakdownItemsLimit: Optional[ItemsLimitConfiguration] = None


class WordCloudSortConfigurationOutput(BaseValidatorModel):
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    CategorySort: Optional[List[FieldSortOptions]] = None


class WordCloudSortConfiguration(BaseValidatorModel):
    CategoryItemsLimit: Optional[ItemsLimitConfiguration] = None
    CategorySort: Optional[List[FieldSortOptions]] = None


class PivotFieldSortOptionsOutput(BaseValidatorModel):
    FieldId: str
    SortBy: PivotTableSortByOutput


class PivotFieldSortOptions(BaseValidatorModel):
    FieldId: str
    SortBy: PivotTableSortBy


class FieldBasedTooltipOutput(BaseValidatorModel):
    AggregationVisibility: Optional[VisibilityType] = None
    TooltipTitleType: Optional[TooltipTitleTypeType] = None
    TooltipFields: Optional[List[TooltipItem]] = None


class FieldBasedTooltip(BaseValidatorModel):
    AggregationVisibility: Optional[VisibilityType] = None
    TooltipTitleType: Optional[TooltipTitleTypeType] = None
    TooltipFields: Optional[List[TooltipItem]] = None


class TopicDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None
    DataSets: Optional[List[DatasetMetadataOutput]] = None
    ConfigOptions: Optional[TopicConfigOptions] = None


class TopicDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None
    DataSets: Optional[List[DatasetMetadata]] = None
    ConfigOptions: Optional[TopicConfigOptions] = None


class AssetBundleImportJobDataSourceOverrideParameters(BaseValidatorModel):
    DataSourceId: str
    Name: Optional[str] = None
    DataSourceParameters: Optional[DataSourceParameters] = None
    VpcConnectionProperties: Optional[VpcConnectionProperties] = None
    SslProperties: Optional[SslProperties] = None
    Credentials: Optional[AssetBundleImportJobDataSourceCredentials] = None

DataSourceParametersUnion = Union[DataSourceParameters, DataSourceParametersOutput]


class SnapshotJobResult(BaseValidatorModel):
    AnonymousUsers: Optional[List[AnonymousUserSnapshotJobResult]] = None


class DefaultNewSheetConfiguration(BaseValidatorModel):
    InteractiveLayoutConfiguration: Optional[DefaultInteractiveLayoutConfiguration] = None
    PaginatedLayoutConfiguration: Optional[DefaultPaginatedLayoutConfiguration] = None
    SheetContentType: Optional[SheetContentTypeType] = None


class BodySectionContentOutput(BaseValidatorModel):
    Layout: Optional[SectionLayoutConfigurationOutput] = None


class HeaderFooterSectionConfigurationOutput(BaseValidatorModel):
    SectionId: str
    Layout: SectionLayoutConfigurationOutput
    Style: Optional[SectionStyle] = None


class BodySectionContent(BaseValidatorModel):
    Layout: Optional[SectionLayoutConfiguration] = None


class HeaderFooterSectionConfiguration(BaseValidatorModel):
    SectionId: str
    Layout: SectionLayoutConfiguration
    Style: Optional[SectionStyle] = None


class StartDashboardSnapshotJobRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str
    UserConfiguration: SnapshotUserConfiguration
    SnapshotConfiguration: SnapshotConfigurationUnion


class DescribeAssetBundleImportJobResponse(BaseValidatorModel):
    JobStatus: AssetBundleImportJobStatusType
    Errors: List[AssetBundleImportJobError]
    RollbackErrors: List[AssetBundleImportJobError]
    Arn: str
    CreatedTime: datetime
    AssetBundleImportJobId: str
    AwsAccountId: str
    AssetBundleImportSource: AssetBundleImportSourceDescription
    OverrideParameters: AssetBundleImportJobOverrideParametersOutput
    FailureAction: AssetBundleImportFailureActionType
    RequestId: str
    Status: int
    OverridePermissions: AssetBundleImportJobOverridePermissionsOutput
    OverrideTags: AssetBundleImportJobOverrideTagsOutput
    OverrideValidationStrategy: AssetBundleImportJobOverrideValidationStrategy
    Warnings: List[AssetBundleImportJobWarning]
    ResponseMetadata: ResponseMetadata


class ImageCustomActionOperation(BaseValidatorModel):
    NavigationOperation: Optional[CustomActionNavigationOperation] = None
    URLOperation: Optional[CustomActionURLOperation] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperation] = None


class LayerCustomActionOperation(BaseValidatorModel):
    FilterOperation: Optional[CustomActionFilterOperation] = None
    NavigationOperation: Optional[CustomActionNavigationOperation] = None
    URLOperation: Optional[CustomActionURLOperation] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperation] = None


class VisualCustomActionOperation(BaseValidatorModel):
    FilterOperation: Optional[CustomActionFilterOperation] = None
    NavigationOperation: Optional[CustomActionNavigationOperation] = None
    URLOperation: Optional[CustomActionURLOperation] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperation] = None

DatasetParameterUnion = Union[DatasetParameter, DatasetParameterOutput]

TransformOperationUnion = Union[TransformOperation, TransformOperationOutput]

ContributionAnalysisTimeRangesUnion = Union[ContributionAnalysisTimeRanges, ContributionAnalysisTimeRangesOutput]


class DescribeDataSetResponse(BaseValidatorModel):
    DataSet: DataSet
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class ImageCustomActionOutput(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: ImageCustomActionTriggerType
    ActionOperations: List[ImageCustomActionOperationOutput]
    Status: Optional[WidgetStatusType] = None


class LayerCustomActionOutput(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: LayerCustomActionTriggerType
    ActionOperations: List[LayerCustomActionOperationOutput]
    Status: Optional[WidgetStatusType] = None


class VisualCustomActionOutput(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: VisualCustomActionTriggerType
    ActionOperations: List[VisualCustomActionOperationOutput]
    Status: Optional[WidgetStatusType] = None


class TopicVisualOutput(BaseValidatorModel):
    VisualId: Optional[str] = None
    Role: Optional[VisualRoleType] = None
    Ir: Optional[TopicIROutput] = None
    SupportingVisuals: Optional[List[Dict[str, Any]]] = None


class DefaultFilterControlConfigurationOutput(BaseValidatorModel):
    Title: str
    ControlOptions: DefaultFilterControlOptionsOutput


class DefaultFilterControlConfiguration(BaseValidatorModel):
    Title: str
    ControlOptions: DefaultFilterControlOptions


class TableFieldOption(BaseValidatorModel):
    FieldId: str
    Width: Optional[str] = None
    CustomLabel: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    URLStyling: Optional[TableFieldURLConfiguration] = None


class GeospatialPointLayerOutput(BaseValidatorModel):
    Style: GeospatialPointStyleOutput


class GeospatialLineLayerOutput(BaseValidatorModel):
    Style: GeospatialLineStyleOutput


class GeospatialPolygonLayerOutput(BaseValidatorModel):
    Style: GeospatialPolygonStyleOutput


class GeospatialPointLayer(BaseValidatorModel):
    Style: GeospatialPointStyle


class GeospatialLineLayer(BaseValidatorModel):
    Style: GeospatialLineStyle


class GeospatialPolygonLayer(BaseValidatorModel):
    Style: GeospatialPolygonStyle


class GaugeChartConditionalFormattingOutput(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[GaugeChartConditionalFormattingOptionOutput]] = None


class KPIConditionalFormattingOutput(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[KPIConditionalFormattingOptionOutput]] = None


class FilledMapConditionalFormattingOptionOutput(BaseValidatorModel):
    Shape: FilledMapShapeConditionalFormattingOutput


class PivotTableConditionalFormattingOptionOutput(BaseValidatorModel):
    Cell: Optional[PivotTableCellConditionalFormattingOutput] = None


class TableConditionalFormattingOptionOutput(BaseValidatorModel):
    Cell: Optional[TableCellConditionalFormattingOutput] = None
    Row: Optional[TableRowConditionalFormattingOutput] = None


class GaugeChartConditionalFormatting(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[GaugeChartConditionalFormattingOption]] = None


class KPIConditionalFormatting(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[KPIConditionalFormattingOption]] = None


class FilledMapConditionalFormattingOption(BaseValidatorModel):
    Shape: FilledMapShapeConditionalFormatting


class PivotTableConditionalFormattingOption(BaseValidatorModel):
    Cell: Optional[PivotTableCellConditionalFormatting] = None


class TableConditionalFormattingOption(BaseValidatorModel):
    Cell: Optional[TableCellConditionalFormatting] = None
    Row: Optional[TableRowConditionalFormatting] = None


class CreateBrandRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandId: str
    BrandDefinition: Optional[BrandDefinition] = None
    Tags: Optional[List[Tag]] = None


class UpdateBrandRequest(BaseValidatorModel):
    AwsAccountId: str
    BrandId: str
    BrandDefinition: Optional[BrandDefinition] = None


class CreateBrandResponse(BaseValidatorModel):
    RequestId: str
    BrandDetail: BrandDetail
    BrandDefinition: BrandDefinition
    ResponseMetadata: ResponseMetadata


class DescribeBrandPublishedVersionResponse(BaseValidatorModel):
    RequestId: str
    BrandDetail: BrandDetail
    BrandDefinition: BrandDefinition
    ResponseMetadata: ResponseMetadata


class DescribeBrandResponse(BaseValidatorModel):
    RequestId: str
    BrandDetail: BrandDetail
    BrandDefinition: BrandDefinition
    ResponseMetadata: ResponseMetadata


class UpdateBrandResponse(BaseValidatorModel):
    RequestId: str
    BrandDetail: BrandDetail
    BrandDefinition: BrandDefinition
    ResponseMetadata: ResponseMetadata


class DescribeThemeResponse(BaseValidatorModel):
    Theme: Theme
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class ReferenceLine(BaseValidatorModel):
    DataConfiguration: ReferenceLineDataConfiguration
    Status: Optional[WidgetStatusType] = None
    StyleConfiguration: Optional[ReferenceLineStyleConfiguration] = None
    LabelConfiguration: Optional[ReferenceLineLabelConfiguration] = None


class DimensionField(BaseValidatorModel):
    NumericalDimensionField: Optional[NumericalDimensionField] = None
    CategoricalDimensionField: Optional[CategoricalDimensionField] = None
    DateDimensionField: Optional[DateDimensionField] = None


class MeasureField(BaseValidatorModel):
    NumericalMeasureField: Optional[NumericalMeasureField] = None
    CategoricalMeasureField: Optional[CategoricalMeasureField] = None
    DateMeasureField: Optional[DateMeasureField] = None
    CalculatedMeasureField: Optional[CalculatedMeasureField] = None


class ColumnConfigurationOutput(BaseValidatorModel):
    Column: ColumnIdentifier
    FormatConfiguration: Optional[FormatConfiguration] = None
    Role: Optional[ColumnRoleType] = None
    ColorsConfiguration: Optional[ColorsConfigurationOutput] = None


class ColumnConfiguration(BaseValidatorModel):
    Column: ColumnIdentifier
    FormatConfiguration: Optional[FormatConfiguration] = None
    Role: Optional[ColumnRoleType] = None
    ColorsConfiguration: Optional[ColorsConfiguration] = None


class UnaggregatedField(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifier
    FormatConfiguration: Optional[FormatConfiguration] = None


class BodySectionRepeatConfigurationOutput(BaseValidatorModel):
    DimensionConfigurations: Optional[List[BodySectionRepeatDimensionConfigurationOutput]] = None
    PageBreakConfiguration: Optional[BodySectionRepeatPageBreakConfiguration] = None
    NonRepeatingVisuals: Optional[List[str]] = None


class BodySectionRepeatConfiguration(BaseValidatorModel):
    DimensionConfigurations: Optional[List[BodySectionRepeatDimensionConfiguration]] = None
    PageBreakConfiguration: Optional[BodySectionRepeatPageBreakConfiguration] = None
    NonRepeatingVisuals: Optional[List[str]] = None


class PluginVisualSortConfigurationOutput(BaseValidatorModel):
    PluginVisualTableQuerySort: Optional[PluginVisualTableQuerySortOutput] = None


class PluginVisualSortConfiguration(BaseValidatorModel):
    PluginVisualTableQuerySort: Optional[PluginVisualTableQuerySort] = None


class PivotTableSortConfigurationOutput(BaseValidatorModel):
    FieldSortOptions: Optional[List[PivotFieldSortOptionsOutput]] = None


class PivotTableSortConfiguration(BaseValidatorModel):
    FieldSortOptions: Optional[List[PivotFieldSortOptions]] = None


class TooltipOptionsOutput(BaseValidatorModel):
    TooltipVisibility: Optional[VisibilityType] = None
    SelectedTooltipType: Optional[SelectedTooltipTypeType] = None
    FieldBasedTooltip: Optional[FieldBasedTooltipOutput] = None


class TooltipOptions(BaseValidatorModel):
    TooltipVisibility: Optional[VisibilityType] = None
    SelectedTooltipType: Optional[SelectedTooltipTypeType] = None
    FieldBasedTooltip: Optional[FieldBasedTooltip] = None


class DescribeTopicResponse(BaseValidatorModel):
    Arn: str
    TopicId: str
    Topic: TopicDetailsOutput
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata

TopicDetailsUnion = Union[TopicDetails, TopicDetailsOutput]


class AssetBundleImportJobOverrideParameters(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[AssetBundleImportJobResourceIdOverrideConfiguration] = None
    VPCConnections: Optional[List[AssetBundleImportJobVPCConnectionOverrideParameters]] = None
    RefreshSchedules: Optional[List[AssetBundleImportJobRefreshScheduleOverrideParameters]] = None
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverrideParameters]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideParameters]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideParameters]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideParameters]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideParameters]] = None
    Folders: Optional[List[AssetBundleImportJobFolderOverrideParameters]] = None


class CredentialPair(BaseValidatorModel):
    Username: str
    Password: str
    AlternateDataSourceParameters: Optional[List[DataSourceParametersUnion]] = None


class DescribeDashboardSnapshotJobResultResponse(BaseValidatorModel):
    Arn: str
    JobStatus: SnapshotJobStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Result: SnapshotJobResult
    ErrorInfo: SnapshotJobErrorInfo
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadata


class AnalysisDefaults(BaseValidatorModel):
    DefaultNewSheetConfiguration: DefaultNewSheetConfiguration


class ImageCustomAction(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: ImageCustomActionTriggerType
    ActionOperations: List[ImageCustomActionOperation]
    Status: Optional[WidgetStatusType] = None


class LayerCustomAction(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: LayerCustomActionTriggerType
    ActionOperations: List[LayerCustomActionOperation]
    Status: Optional[WidgetStatusType] = None


class VisualCustomAction(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: VisualCustomActionTriggerType
    ActionOperations: List[VisualCustomActionOperation]
    Status: Optional[WidgetStatusType] = None


class LogicalTable(BaseValidatorModel):
    Alias: str
    Source: LogicalTableSource
    DataTransforms: Optional[List[TransformOperationUnion]] = None


class TopicIRContributionAnalysis(BaseValidatorModel):
    Factors: Optional[List[ContributionAnalysisFactor]] = None
    TimeRanges: Optional[ContributionAnalysisTimeRangesUnion] = None
    Direction: Optional[ContributionAnalysisDirectionType] = None
    SortType: Optional[ContributionAnalysisSortTypeType] = None


class SheetImageOutput(BaseValidatorModel):
    SheetImageId: str
    Source: SheetImageSource
    Scaling: Optional[SheetImageScalingConfiguration] = None
    Tooltip: Optional[SheetImageTooltipConfiguration] = None
    ImageContentAltText: Optional[str] = None
    Interactions: Optional[ImageInteractionOptions] = None
    Actions: Optional[List[ImageCustomActionOutput]] = None


class CustomContentVisualOutput(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[CustomContentConfiguration] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class EmptyVisualOutput(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Actions: Optional[List[VisualCustomActionOutput]] = None


class TopicReviewedAnswer(BaseValidatorModel):
    AnswerId: str
    DatasetArn: str
    Question: str
    Arn: Optional[str] = None
    Mir: Optional[TopicIROutput] = None
    PrimaryVisual: Optional[TopicVisualOutput] = None
    Template: Optional[TopicTemplateOutput] = None


class CategoryFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    Configuration: CategoryFilterConfigurationOutput
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class CategoryInnerFilterOutput(BaseValidatorModel):
    Column: ColumnIdentifier
    Configuration: CategoryFilterConfigurationOutput
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class NumericEqualityFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    MatchOperator: NumericEqualityMatchOperatorType
    NullOption: FilterNullOptionType
    Value: Optional[float] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    AggregationFunction: Optional[AggregationFunction] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class NumericRangeFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimum: Optional[NumericRangeFilterValue] = None
    RangeMaximum: Optional[NumericRangeFilterValue] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    AggregationFunction: Optional[AggregationFunction] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class RelativeDatesFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    AnchorDateConfiguration: AnchorDateConfiguration
    TimeGranularity: TimeGranularityType
    RelativeDateType: RelativeDateTypeType
    NullOption: FilterNullOptionType
    MinimumGranularity: Optional[TimeGranularityType] = None
    RelativeDateValue: Optional[int] = None
    ParameterName: Optional[str] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfiguration] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class TimeEqualityFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    Value: Optional[datetime] = None
    ParameterName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    RollingDate: Optional[RollingDateConfiguration] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class TimeRangeFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimumValue: Optional[TimeRangeFilterValueOutput] = None
    RangeMaximumValue: Optional[TimeRangeFilterValueOutput] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfiguration] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class TopBottomFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    AggregationSortConfigurations: List[AggregationSortConfiguration]
    Limit: Optional[int] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationOutput] = None


class CategoryFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    Configuration: CategoryFilterConfiguration
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class CategoryInnerFilter(BaseValidatorModel):
    Column: ColumnIdentifier
    Configuration: CategoryFilterConfiguration
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class NumericEqualityFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    MatchOperator: NumericEqualityMatchOperatorType
    NullOption: FilterNullOptionType
    Value: Optional[float] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    AggregationFunction: Optional[AggregationFunction] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class NumericRangeFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimum: Optional[NumericRangeFilterValue] = None
    RangeMaximum: Optional[NumericRangeFilterValue] = None
    SelectAllOptions: Optional[Literal['FILTER_ALL_VALUES']] = None
    AggregationFunction: Optional[AggregationFunction] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class RelativeDatesFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    AnchorDateConfiguration: AnchorDateConfiguration
    TimeGranularity: TimeGranularityType
    RelativeDateType: RelativeDateTypeType
    NullOption: FilterNullOptionType
    MinimumGranularity: Optional[TimeGranularityType] = None
    RelativeDateValue: Optional[int] = None
    ParameterName: Optional[str] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfiguration] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class TimeEqualityFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    Value: Optional[Timestamp] = None
    ParameterName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    RollingDate: Optional[RollingDateConfiguration] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class TimeRangeFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimumValue: Optional[TimeRangeFilterValue] = None
    RangeMaximumValue: Optional[TimeRangeFilterValue] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfiguration] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class TopBottomFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    AggregationSortConfigurations: List[AggregationSortConfiguration]
    Limit: Optional[int] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfiguration] = None


class TableFieldOptionsOutput(BaseValidatorModel):
    SelectedFieldOptions: Optional[List[TableFieldOption]] = None
    Order: Optional[List[str]] = None
    PinnedFieldOptions: Optional[TablePinnedFieldOptionsOutput] = None


class TableFieldOptions(BaseValidatorModel):
    SelectedFieldOptions: Optional[List[TableFieldOption]] = None
    Order: Optional[List[str]] = None
    PinnedFieldOptions: Optional[TablePinnedFieldOptions] = None


class GeospatialLayerDefinitionOutput(BaseValidatorModel):
    PointLayer: Optional[GeospatialPointLayerOutput] = None
    LineLayer: Optional[GeospatialLineLayerOutput] = None
    PolygonLayer: Optional[GeospatialPolygonLayerOutput] = None


class GeospatialLayerDefinition(BaseValidatorModel):
    PointLayer: Optional[GeospatialPointLayer] = None
    LineLayer: Optional[GeospatialLineLayer] = None
    PolygonLayer: Optional[GeospatialPolygonLayer] = None


class FilledMapConditionalFormattingOutput(BaseValidatorModel):
    ConditionalFormattingOptions: List[FilledMapConditionalFormattingOptionOutput]


class PivotTableConditionalFormattingOutput(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[PivotTableConditionalFormattingOptionOutput]] = None


class TableConditionalFormattingOutput(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[TableConditionalFormattingOptionOutput]] = None


class FilledMapConditionalFormatting(BaseValidatorModel):
    ConditionalFormattingOptions: List[FilledMapConditionalFormattingOption]


class PivotTableConditionalFormatting(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[PivotTableConditionalFormattingOption]] = None


class TableConditionalFormatting(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[List[TableConditionalFormattingOption]] = None


class UniqueValuesComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Category: Optional[DimensionField] = None


class BarChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None
    SmallMultiples: Optional[List[DimensionField]] = None


class BarChartAggregatedFieldWells(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None
    SmallMultiples: Optional[List[DimensionField]] = None


class BoxPlotAggregatedFieldWellsOutput(BaseValidatorModel):
    GroupBy: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class BoxPlotAggregatedFieldWells(BaseValidatorModel):
    GroupBy: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class ComboChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    BarValues: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None
    LineValues: Optional[List[MeasureField]] = None


class ComboChartAggregatedFieldWells(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    BarValues: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None
    LineValues: Optional[List[MeasureField]] = None


class FilledMapAggregatedFieldWellsOutput(BaseValidatorModel):
    Geospatial: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class FilledMapAggregatedFieldWells(BaseValidatorModel):
    Geospatial: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class ForecastComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None
    PeriodsForward: Optional[int] = None
    PeriodsBackward: Optional[int] = None
    UpperBoundary: Optional[float] = None
    LowerBoundary: Optional[float] = None
    PredictionInterval: Optional[int] = None
    Seasonality: Optional[ForecastComputationSeasonalityType] = None
    CustomSeasonalityValue: Optional[int] = None


class FunnelChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class FunnelChartAggregatedFieldWells(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class GaugeChartFieldWellsOutput(BaseValidatorModel):
    Values: Optional[List[MeasureField]] = None
    TargetValues: Optional[List[MeasureField]] = None


class GaugeChartFieldWells(BaseValidatorModel):
    Values: Optional[List[MeasureField]] = None
    TargetValues: Optional[List[MeasureField]] = None


class GeospatialLayerColorFieldOutput(BaseValidatorModel):
    ColorDimensionsFields: Optional[List[DimensionField]] = None
    ColorValuesFields: Optional[List[MeasureField]] = None


class GeospatialLayerColorField(BaseValidatorModel):
    ColorDimensionsFields: Optional[List[DimensionField]] = None
    ColorValuesFields: Optional[List[MeasureField]] = None


class GeospatialMapAggregatedFieldWellsOutput(BaseValidatorModel):
    Geospatial: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None


class GeospatialMapAggregatedFieldWells(BaseValidatorModel):
    Geospatial: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None


class GrowthRateComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None
    PeriodSize: Optional[int] = None


class HeatMapAggregatedFieldWellsOutput(BaseValidatorModel):
    Rows: Optional[List[DimensionField]] = None
    Columns: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class HeatMapAggregatedFieldWells(BaseValidatorModel):
    Rows: Optional[List[DimensionField]] = None
    Columns: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class HistogramAggregatedFieldWellsOutput(BaseValidatorModel):
    Values: Optional[List[MeasureField]] = None


class HistogramAggregatedFieldWells(BaseValidatorModel):
    Values: Optional[List[MeasureField]] = None


class KPIFieldWellsOutput(BaseValidatorModel):
    Values: Optional[List[MeasureField]] = None
    TargetValues: Optional[List[MeasureField]] = None
    TrendGroups: Optional[List[DimensionField]] = None


class KPIFieldWells(BaseValidatorModel):
    Values: Optional[List[MeasureField]] = None
    TargetValues: Optional[List[MeasureField]] = None
    TrendGroups: Optional[List[DimensionField]] = None


class LineChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None
    SmallMultiples: Optional[List[DimensionField]] = None


class LineChartAggregatedFieldWells(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Colors: Optional[List[DimensionField]] = None
    SmallMultiples: Optional[List[DimensionField]] = None


class MaximumMinimumComputation(BaseValidatorModel):
    ComputationId: str
    Type: MaximumMinimumComputationTypeType
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None


class MetricComparisonComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    FromValue: Optional[MeasureField] = None
    TargetValue: Optional[MeasureField] = None


class PeriodOverPeriodComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None


class PeriodToDateComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None
    PeriodTimeGranularity: Optional[TimeGranularityType] = None


class PieChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    SmallMultiples: Optional[List[DimensionField]] = None


class PieChartAggregatedFieldWells(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    SmallMultiples: Optional[List[DimensionField]] = None


class PivotTableAggregatedFieldWellsOutput(BaseValidatorModel):
    Rows: Optional[List[DimensionField]] = None
    Columns: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class PivotTableAggregatedFieldWells(BaseValidatorModel):
    Rows: Optional[List[DimensionField]] = None
    Columns: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class RadarChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Color: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class RadarChartAggregatedFieldWells(BaseValidatorModel):
    Category: Optional[List[DimensionField]] = None
    Color: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class SankeyDiagramAggregatedFieldWellsOutput(BaseValidatorModel):
    Source: Optional[List[DimensionField]] = None
    Destination: Optional[List[DimensionField]] = None
    Weight: Optional[List[MeasureField]] = None


class SankeyDiagramAggregatedFieldWells(BaseValidatorModel):
    Source: Optional[List[DimensionField]] = None
    Destination: Optional[List[DimensionField]] = None
    Weight: Optional[List[MeasureField]] = None


class ScatterPlotCategoricallyAggregatedFieldWellsOutput(BaseValidatorModel):
    XAxis: Optional[List[MeasureField]] = None
    YAxis: Optional[List[MeasureField]] = None
    Category: Optional[List[DimensionField]] = None
    Size: Optional[List[MeasureField]] = None
    Label: Optional[List[DimensionField]] = None


class ScatterPlotCategoricallyAggregatedFieldWells(BaseValidatorModel):
    XAxis: Optional[List[MeasureField]] = None
    YAxis: Optional[List[MeasureField]] = None
    Category: Optional[List[DimensionField]] = None
    Size: Optional[List[MeasureField]] = None
    Label: Optional[List[DimensionField]] = None


class ScatterPlotUnaggregatedFieldWellsOutput(BaseValidatorModel):
    XAxis: Optional[List[DimensionField]] = None
    YAxis: Optional[List[DimensionField]] = None
    Size: Optional[List[MeasureField]] = None
    Category: Optional[List[DimensionField]] = None
    Label: Optional[List[DimensionField]] = None


class ScatterPlotUnaggregatedFieldWells(BaseValidatorModel):
    XAxis: Optional[List[DimensionField]] = None
    YAxis: Optional[List[DimensionField]] = None
    Size: Optional[List[MeasureField]] = None
    Category: Optional[List[DimensionField]] = None
    Label: Optional[List[DimensionField]] = None


class TableAggregatedFieldWellsOutput(BaseValidatorModel):
    GroupBy: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class TableAggregatedFieldWells(BaseValidatorModel):
    GroupBy: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None


class TopBottomMoversComputation(BaseValidatorModel):
    ComputationId: str
    Type: TopBottomComputationTypeType
    Name: Optional[str] = None
    Time: Optional[DimensionField] = None
    Category: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None
    MoverSize: Optional[int] = None
    SortOrder: Optional[TopBottomSortOrderType] = None


class TopBottomRankedComputation(BaseValidatorModel):
    ComputationId: str
    Type: TopBottomComputationTypeType
    Name: Optional[str] = None
    Category: Optional[DimensionField] = None
    Value: Optional[MeasureField] = None
    ResultSize: Optional[int] = None


class TotalAggregationComputation(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Value: Optional[MeasureField] = None


class TreeMapAggregatedFieldWellsOutput(BaseValidatorModel):
    Groups: Optional[List[DimensionField]] = None
    Sizes: Optional[List[MeasureField]] = None
    Colors: Optional[List[MeasureField]] = None


class TreeMapAggregatedFieldWells(BaseValidatorModel):
    Groups: Optional[List[DimensionField]] = None
    Sizes: Optional[List[MeasureField]] = None
    Colors: Optional[List[MeasureField]] = None


class WaterfallChartAggregatedFieldWellsOutput(BaseValidatorModel):
    Categories: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Breakdowns: Optional[List[DimensionField]] = None


class WaterfallChartAggregatedFieldWells(BaseValidatorModel):
    Categories: Optional[List[DimensionField]] = None
    Values: Optional[List[MeasureField]] = None
    Breakdowns: Optional[List[DimensionField]] = None


class WordCloudAggregatedFieldWellsOutput(BaseValidatorModel):
    GroupBy: Optional[List[DimensionField]] = None
    Size: Optional[List[MeasureField]] = None


class WordCloudAggregatedFieldWells(BaseValidatorModel):
    GroupBy: Optional[List[DimensionField]] = None
    Size: Optional[List[MeasureField]] = None


class PluginVisualFieldWellOutput(BaseValidatorModel):
    AxisName: Optional[PluginVisualAxisNameType] = None
    Dimensions: Optional[List[DimensionField]] = None
    Measures: Optional[List[MeasureField]] = None
    Unaggregated: Optional[List[UnaggregatedField]] = None


class PluginVisualFieldWell(BaseValidatorModel):
    AxisName: Optional[PluginVisualAxisNameType] = None
    Dimensions: Optional[List[DimensionField]] = None
    Measures: Optional[List[MeasureField]] = None
    Unaggregated: Optional[List[UnaggregatedField]] = None


class TableUnaggregatedFieldWellsOutput(BaseValidatorModel):
    Values: Optional[List[UnaggregatedField]] = None


class TableUnaggregatedFieldWells(BaseValidatorModel):
    Values: Optional[List[UnaggregatedField]] = None


class BodySectionConfigurationOutput(BaseValidatorModel):
    SectionId: str
    Content: BodySectionContentOutput
    Style: Optional[SectionStyle] = None
    PageBreakConfiguration: Optional[SectionPageBreakConfiguration] = None
    RepeatConfiguration: Optional[BodySectionRepeatConfigurationOutput] = None


class BodySectionConfiguration(BaseValidatorModel):
    SectionId: str
    Content: BodySectionContent
    Style: Optional[SectionStyle] = None
    PageBreakConfiguration: Optional[SectionPageBreakConfiguration] = None
    RepeatConfiguration: Optional[BodySectionRepeatConfiguration] = None


class CreateTopicRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    Topic: TopicDetailsUnion
    Tags: Optional[List[Tag]] = None
    FolderArns: Optional[List[str]] = None


class UpdateTopicRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    Topic: TopicDetailsUnion

AssetBundleImportJobOverrideParametersUnion = Union[AssetBundleImportJobOverrideParameters, AssetBundleImportJobOverrideParametersOutput]


class DataSourceCredentials(BaseValidatorModel):
    CredentialPair: Optional[CredentialPair] = None
    CopySourceArn: Optional[str] = None
    SecretArn: Optional[str] = None


class SheetImage(BaseValidatorModel):
    SheetImageId: str
    Source: SheetImageSource
    Scaling: Optional[SheetImageScalingConfiguration] = None
    Tooltip: Optional[SheetImageTooltipConfiguration] = None
    ImageContentAltText: Optional[str] = None
    Interactions: Optional[ImageInteractionOptions] = None
    Actions: Optional[List[ImageCustomAction]] = None


class CustomContentVisual(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[CustomContentConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class EmptyVisual(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Actions: Optional[List[VisualCustomAction]] = None

LogicalTableUnion = Union[LogicalTable, LogicalTableOutput]

TopicIRContributionAnalysisUnion = Union[TopicIRContributionAnalysis, TopicIRContributionAnalysisOutput]


class Sheet(BaseValidatorModel):
    SheetId: Optional[str] = None
    Name: Optional[str] = None
    Images: Optional[List[SheetImageOutput]] = None


class ListTopicReviewedAnswersResponse(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    Answers: List[TopicReviewedAnswer]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class InnerFilterOutput(BaseValidatorModel):
    CategoryInnerFilter: Optional[CategoryInnerFilterOutput] = None


class InnerFilter(BaseValidatorModel):
    CategoryInnerFilter: Optional[CategoryInnerFilter] = None


class BarChartFieldWellsOutput(BaseValidatorModel):
    BarChartAggregatedFieldWells: Optional[BarChartAggregatedFieldWellsOutput] = None


class BarChartFieldWells(BaseValidatorModel):
    BarChartAggregatedFieldWells: Optional[BarChartAggregatedFieldWells] = None


class BoxPlotFieldWellsOutput(BaseValidatorModel):
    BoxPlotAggregatedFieldWells: Optional[BoxPlotAggregatedFieldWellsOutput] = None


class BoxPlotFieldWells(BaseValidatorModel):
    BoxPlotAggregatedFieldWells: Optional[BoxPlotAggregatedFieldWells] = None


class ComboChartFieldWellsOutput(BaseValidatorModel):
    ComboChartAggregatedFieldWells: Optional[ComboChartAggregatedFieldWellsOutput] = None


class ComboChartFieldWells(BaseValidatorModel):
    ComboChartAggregatedFieldWells: Optional[ComboChartAggregatedFieldWells] = None


class FilledMapFieldWellsOutput(BaseValidatorModel):
    FilledMapAggregatedFieldWells: Optional[FilledMapAggregatedFieldWellsOutput] = None


class FilledMapFieldWells(BaseValidatorModel):
    FilledMapAggregatedFieldWells: Optional[FilledMapAggregatedFieldWells] = None


class FunnelChartFieldWellsOutput(BaseValidatorModel):
    FunnelChartAggregatedFieldWells: Optional[FunnelChartAggregatedFieldWellsOutput] = None


class FunnelChartFieldWells(BaseValidatorModel):
    FunnelChartAggregatedFieldWells: Optional[FunnelChartAggregatedFieldWells] = None


class GaugeChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[GaugeChartFieldWellsOutput] = None
    GaugeChartOptions: Optional[GaugeChartOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    TooltipOptions: Optional[TooltipOptionsOutput] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    ColorConfiguration: Optional[GaugeChartColorConfiguration] = None
    Interactions: Optional[VisualInteractionOptions] = None


class GaugeChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[GaugeChartFieldWells] = None
    GaugeChartOptions: Optional[GaugeChartOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    TooltipOptions: Optional[TooltipOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    ColorConfiguration: Optional[GaugeChartColorConfiguration] = None
    Interactions: Optional[VisualInteractionOptions] = None


class GeospatialLayerJoinDefinitionOutput(BaseValidatorModel):
    ShapeKeyField: Optional[str] = None
    DatasetKeyField: Optional[UnaggregatedField] = None
    ColorField: Optional[GeospatialLayerColorFieldOutput] = None


class GeospatialLayerJoinDefinition(BaseValidatorModel):
    ShapeKeyField: Optional[str] = None
    DatasetKeyField: Optional[UnaggregatedField] = None
    ColorField: Optional[GeospatialLayerColorField] = None


class GeospatialMapFieldWellsOutput(BaseValidatorModel):
    GeospatialMapAggregatedFieldWells: Optional[GeospatialMapAggregatedFieldWellsOutput] = None


class GeospatialMapFieldWells(BaseValidatorModel):
    GeospatialMapAggregatedFieldWells: Optional[GeospatialMapAggregatedFieldWells] = None


class HeatMapFieldWellsOutput(BaseValidatorModel):
    HeatMapAggregatedFieldWells: Optional[HeatMapAggregatedFieldWellsOutput] = None


class HeatMapFieldWells(BaseValidatorModel):
    HeatMapAggregatedFieldWells: Optional[HeatMapAggregatedFieldWells] = None


class HistogramFieldWellsOutput(BaseValidatorModel):
    HistogramAggregatedFieldWells: Optional[HistogramAggregatedFieldWellsOutput] = None


class HistogramFieldWells(BaseValidatorModel):
    HistogramAggregatedFieldWells: Optional[HistogramAggregatedFieldWells] = None


class KPIConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[KPIFieldWellsOutput] = None
    SortConfiguration: Optional[KPISortConfigurationOutput] = None
    KPIOptions: Optional[KPIOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class KPIConfiguration(BaseValidatorModel):
    FieldWells: Optional[KPIFieldWells] = None
    SortConfiguration: Optional[KPISortConfiguration] = None
    KPIOptions: Optional[KPIOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class LineChartFieldWellsOutput(BaseValidatorModel):
    LineChartAggregatedFieldWells: Optional[LineChartAggregatedFieldWellsOutput] = None


class LineChartFieldWells(BaseValidatorModel):
    LineChartAggregatedFieldWells: Optional[LineChartAggregatedFieldWells] = None


class PieChartFieldWellsOutput(BaseValidatorModel):
    PieChartAggregatedFieldWells: Optional[PieChartAggregatedFieldWellsOutput] = None


class PieChartFieldWells(BaseValidatorModel):
    PieChartAggregatedFieldWells: Optional[PieChartAggregatedFieldWells] = None


class PivotTableFieldWellsOutput(BaseValidatorModel):
    PivotTableAggregatedFieldWells: Optional[PivotTableAggregatedFieldWellsOutput] = None


class PivotTableFieldWells(BaseValidatorModel):
    PivotTableAggregatedFieldWells: Optional[PivotTableAggregatedFieldWells] = None


class RadarChartFieldWellsOutput(BaseValidatorModel):
    RadarChartAggregatedFieldWells: Optional[RadarChartAggregatedFieldWellsOutput] = None


class RadarChartFieldWells(BaseValidatorModel):
    RadarChartAggregatedFieldWells: Optional[RadarChartAggregatedFieldWells] = None


class SankeyDiagramFieldWellsOutput(BaseValidatorModel):
    SankeyDiagramAggregatedFieldWells: Optional[SankeyDiagramAggregatedFieldWellsOutput] = None


class SankeyDiagramFieldWells(BaseValidatorModel):
    SankeyDiagramAggregatedFieldWells: Optional[SankeyDiagramAggregatedFieldWells] = None


class ScatterPlotFieldWellsOutput(BaseValidatorModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional[ScatterPlotCategoricallyAggregatedFieldWellsOutput] = None
    ScatterPlotUnaggregatedFieldWells: Optional[ScatterPlotUnaggregatedFieldWellsOutput] = None


class ScatterPlotFieldWells(BaseValidatorModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional[ScatterPlotCategoricallyAggregatedFieldWells] = None
    ScatterPlotUnaggregatedFieldWells: Optional[ScatterPlotUnaggregatedFieldWells] = None


class Computation(BaseValidatorModel):
    TopBottomRanked: Optional[TopBottomRankedComputation] = None
    TopBottomMovers: Optional[TopBottomMoversComputation] = None
    TotalAggregation: Optional[TotalAggregationComputation] = None
    MaximumMinimum: Optional[MaximumMinimumComputation] = None
    MetricComparison: Optional[MetricComparisonComputation] = None
    PeriodOverPeriod: Optional[PeriodOverPeriodComputation] = None
    PeriodToDate: Optional[PeriodToDateComputation] = None
    GrowthRate: Optional[GrowthRateComputation] = None
    UniqueValues: Optional[UniqueValuesComputation] = None
    Forecast: Optional[ForecastComputation] = None


class TreeMapFieldWellsOutput(BaseValidatorModel):
    TreeMapAggregatedFieldWells: Optional[TreeMapAggregatedFieldWellsOutput] = None


class TreeMapFieldWells(BaseValidatorModel):
    TreeMapAggregatedFieldWells: Optional[TreeMapAggregatedFieldWells] = None


class WaterfallChartFieldWellsOutput(BaseValidatorModel):
    WaterfallChartAggregatedFieldWells: Optional[WaterfallChartAggregatedFieldWellsOutput] = None


class WaterfallChartFieldWells(BaseValidatorModel):
    WaterfallChartAggregatedFieldWells: Optional[WaterfallChartAggregatedFieldWells] = None


class WordCloudFieldWellsOutput(BaseValidatorModel):
    WordCloudAggregatedFieldWells: Optional[WordCloudAggregatedFieldWellsOutput] = None


class WordCloudFieldWells(BaseValidatorModel):
    WordCloudAggregatedFieldWells: Optional[WordCloudAggregatedFieldWells] = None


class PluginVisualConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[List[PluginVisualFieldWellOutput]] = None
    VisualOptions: Optional[PluginVisualOptionsOutput] = None
    SortConfiguration: Optional[PluginVisualSortConfigurationOutput] = None


class PluginVisualConfiguration(BaseValidatorModel):
    FieldWells: Optional[List[PluginVisualFieldWell]] = None
    VisualOptions: Optional[PluginVisualOptions] = None
    SortConfiguration: Optional[PluginVisualSortConfiguration] = None


class TableFieldWellsOutput(BaseValidatorModel):
    TableAggregatedFieldWells: Optional[TableAggregatedFieldWellsOutput] = None
    TableUnaggregatedFieldWells: Optional[TableUnaggregatedFieldWellsOutput] = None


class TableFieldWells(BaseValidatorModel):
    TableAggregatedFieldWells: Optional[TableAggregatedFieldWells] = None
    TableUnaggregatedFieldWells: Optional[TableUnaggregatedFieldWells] = None


class SectionBasedLayoutConfigurationOutput(BaseValidatorModel):
    HeaderSections: List[HeaderFooterSectionConfigurationOutput]
    BodySections: List[BodySectionConfigurationOutput]
    FooterSections: List[HeaderFooterSectionConfigurationOutput]
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptions


class SectionBasedLayoutConfiguration(BaseValidatorModel):
    HeaderSections: List[HeaderFooterSectionConfiguration]
    BodySections: List[BodySectionConfiguration]
    FooterSections: List[HeaderFooterSectionConfiguration]
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptions


class StartAssetBundleImportJobRequest(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleImportJobId: str
    AssetBundleImportSource: AssetBundleImportSource
    OverrideParameters: Optional[AssetBundleImportJobOverrideParametersUnion] = None
    FailureAction: Optional[AssetBundleImportFailureActionType] = None
    OverridePermissions: Optional[AssetBundleImportJobOverridePermissionsUnion] = None
    OverrideTags: Optional[AssetBundleImportJobOverrideTagsUnion] = None
    OverrideValidationStrategy: Optional[AssetBundleImportJobOverrideValidationStrategy] = None


class CreateDataSourceRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str
    Name: str
    Type: DataSourceTypeType
    DataSourceParameters: Optional[DataSourceParametersUnion] = None
    Credentials: Optional[DataSourceCredentials] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    VpcConnectionProperties: Optional[VpcConnectionProperties] = None
    SslProperties: Optional[SslProperties] = None
    Tags: Optional[List[Tag]] = None
    FolderArns: Optional[List[str]] = None


class UpdateDataSourceRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str
    Name: str
    DataSourceParameters: Optional[DataSourceParametersUnion] = None
    Credentials: Optional[DataSourceCredentials] = None
    VpcConnectionProperties: Optional[VpcConnectionProperties] = None
    SslProperties: Optional[SslProperties] = None


class CreateDataSetRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    Name: str
    PhysicalTableMap: Dict[str, PhysicalTableUnion]
    ImportMode: DataSetImportModeType
    LogicalTableMap: Optional[Dict[str, LogicalTableUnion]] = None
    ColumnGroups: Optional[List[ColumnGroupUnion]] = None
    FieldFolders: Optional[Dict[str, FieldFolderUnion]] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSet] = None
    RowLevelPermissionTagConfiguration: Optional[RowLevelPermissionTagConfigurationUnion] = None
    ColumnLevelPermissionRules: Optional[List[ColumnLevelPermissionRuleUnion]] = None
    Tags: Optional[List[Tag]] = None
    DataSetUsageConfiguration: Optional[DataSetUsageConfiguration] = None
    DatasetParameters: Optional[List[DatasetParameterUnion]] = None
    FolderArns: Optional[List[str]] = None
    PerformanceConfiguration: Optional[PerformanceConfigurationUnion] = None


class UpdateDataSetRequest(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    Name: str
    PhysicalTableMap: Dict[str, PhysicalTableUnion]
    ImportMode: DataSetImportModeType
    LogicalTableMap: Optional[Dict[str, LogicalTableUnion]] = None
    ColumnGroups: Optional[List[ColumnGroupUnion]] = None
    FieldFolders: Optional[Dict[str, FieldFolderUnion]] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSet] = None
    RowLevelPermissionTagConfiguration: Optional[RowLevelPermissionTagConfigurationUnion] = None
    ColumnLevelPermissionRules: Optional[List[ColumnLevelPermissionRuleUnion]] = None
    DataSetUsageConfiguration: Optional[DataSetUsageConfiguration] = None
    DatasetParameters: Optional[List[DatasetParameterUnion]] = None
    PerformanceConfiguration: Optional[PerformanceConfigurationUnion] = None


class TopicIR(BaseValidatorModel):
    Metrics: Optional[List[TopicIRMetricUnion]] = None
    GroupByList: Optional[List[TopicIRGroupBy]] = None
    Filters: Optional[List[List[TopicIRFilterOptionUnion]]] = None
    Sort: Optional[TopicSortClause] = None
    ContributionAnalysis: Optional[TopicIRContributionAnalysisUnion] = None
    Visual: Optional[VisualOptions] = None


class Analysis(BaseValidatorModel):
    AnalysisId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ResourceStatusType] = None
    Errors: Optional[List[AnalysisError]] = None
    DataSetArns: Optional[List[str]] = None
    ThemeArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    Sheets: Optional[List[Sheet]] = None


class DashboardVersion(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    Errors: Optional[List[DashboardError]] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    Arn: Optional[str] = None
    SourceEntityArn: Optional[str] = None
    DataSetArns: Optional[List[str]] = None
    Description: Optional[str] = None
    ThemeArn: Optional[str] = None
    Sheets: Optional[List[Sheet]] = None


class TemplateVersion(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    Errors: Optional[List[TemplateError]] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    DataSetConfigurations: Optional[List[DataSetConfigurationOutput]] = None
    Description: Optional[str] = None
    SourceEntityArn: Optional[str] = None
    ThemeArn: Optional[str] = None
    Sheets: Optional[List[Sheet]] = None


class NestedFilterOutput(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    IncludeInnerSet: bool
    InnerFilter: InnerFilterOutput


class NestedFilter(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifier
    IncludeInnerSet: bool
    InnerFilter: InnerFilter


class BarChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[BarChartFieldWellsOutput] = None
    SortConfiguration: Optional[BarChartSortConfigurationOutput] = None
    Orientation: Optional[BarChartOrientationType] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptions] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutput] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ValueAxis: Optional[AxisDisplayOptionsOutput] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefaultOutput]] = None
    Interactions: Optional[VisualInteractionOptions] = None


class BarChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[BarChartFieldWells] = None
    SortConfiguration: Optional[BarChartSortConfiguration] = None
    Orientation: Optional[BarChartOrientationType] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    VisualPalette: Optional[VisualPalette] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptions] = None
    CategoryAxis: Optional[AxisDisplayOptions] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    ValueAxis: Optional[AxisDisplayOptions] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptions] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptions] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefault]] = None
    Interactions: Optional[VisualInteractionOptions] = None


class BoxPlotChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[BoxPlotFieldWellsOutput] = None
    SortConfiguration: Optional[BoxPlotSortConfigurationOutput] = None
    BoxPlotOptions: Optional[BoxPlotOptions] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutput] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class BoxPlotChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[BoxPlotFieldWells] = None
    SortConfiguration: Optional[BoxPlotSortConfiguration] = None
    BoxPlotOptions: Optional[BoxPlotOptions] = None
    CategoryAxis: Optional[AxisDisplayOptions] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    Legend: Optional[LegendOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class ComboChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[ComboChartFieldWellsOutput] = None
    SortConfiguration: Optional[ComboChartSortConfigurationOutput] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutput] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    SecondaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    SingleAxisOptions: Optional[SingleAxisOptions] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    BarDataLabels: Optional[DataLabelOptionsOutput] = None
    LineDataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class ComboChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[ComboChartFieldWells] = None
    SortConfiguration: Optional[ComboChartSortConfiguration] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    CategoryAxis: Optional[AxisDisplayOptions] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    SecondaryYAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    SingleAxisOptions: Optional[SingleAxisOptions] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptions] = None
    Legend: Optional[LegendOptions] = None
    BarDataLabels: Optional[DataLabelOptions] = None
    LineDataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class FilledMapConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[FilledMapFieldWellsOutput] = None
    SortConfiguration: Optional[FilledMapSortConfigurationOutput] = None
    Legend: Optional[LegendOptions] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    WindowOptions: Optional[GeospatialWindowOptions] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class FilledMapConfiguration(BaseValidatorModel):
    FieldWells: Optional[FilledMapFieldWells] = None
    SortConfiguration: Optional[FilledMapSortConfiguration] = None
    Legend: Optional[LegendOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    WindowOptions: Optional[GeospatialWindowOptions] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class FunnelChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[FunnelChartFieldWellsOutput] = None
    SortConfiguration: Optional[FunnelChartSortConfigurationOutput] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    DataLabelOptions: Optional[FunnelChartDataLabelOptions] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class FunnelChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[FunnelChartFieldWells] = None
    SortConfiguration: Optional[FunnelChartSortConfiguration] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    DataLabelOptions: Optional[FunnelChartDataLabelOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class GaugeChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[GaugeChartConfigurationOutput] = None
    ConditionalFormatting: Optional[GaugeChartConditionalFormattingOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class GaugeChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[GaugeChartConfiguration] = None
    ConditionalFormatting: Optional[GaugeChartConditionalFormatting] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class GeospatialLayerItemOutput(BaseValidatorModel):
    LayerId: str
    LayerType: Optional[GeospatialLayerTypeType] = None
    DataSource: Optional[GeospatialDataSourceItem] = None
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    LayerDefinition: Optional[GeospatialLayerDefinitionOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    JoinDefinition: Optional[GeospatialLayerJoinDefinitionOutput] = None
    Actions: Optional[List[LayerCustomActionOutput]] = None


class GeospatialLayerItem(BaseValidatorModel):
    LayerId: str
    LayerType: Optional[GeospatialLayerTypeType] = None
    DataSource: Optional[GeospatialDataSourceItem] = None
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    LayerDefinition: Optional[GeospatialLayerDefinition] = None
    Tooltip: Optional[TooltipOptions] = None
    JoinDefinition: Optional[GeospatialLayerJoinDefinition] = None
    Actions: Optional[List[LayerCustomAction]] = None


class GeospatialMapConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[GeospatialMapFieldWellsOutput] = None
    Legend: Optional[LegendOptions] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    WindowOptions: Optional[GeospatialWindowOptions] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptions] = None
    PointStyleOptions: Optional[GeospatialPointStyleOptionsOutput] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class GeospatialMapConfiguration(BaseValidatorModel):
    FieldWells: Optional[GeospatialMapFieldWells] = None
    Legend: Optional[LegendOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    WindowOptions: Optional[GeospatialWindowOptions] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptions] = None
    PointStyleOptions: Optional[GeospatialPointStyleOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class HeatMapConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[HeatMapFieldWellsOutput] = None
    SortConfiguration: Optional[HeatMapSortConfigurationOutput] = None
    RowLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ColumnLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ColorScale: Optional[ColorScaleOutput] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class HeatMapConfiguration(BaseValidatorModel):
    FieldWells: Optional[HeatMapFieldWells] = None
    SortConfiguration: Optional[HeatMapSortConfiguration] = None
    RowLabelOptions: Optional[ChartAxisLabelOptions] = None
    ColumnLabelOptions: Optional[ChartAxisLabelOptions] = None
    ColorScale: Optional[ColorScale] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class HistogramConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[HistogramFieldWellsOutput] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    BinOptions: Optional[HistogramBinOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class HistogramConfiguration(BaseValidatorModel):
    FieldWells: Optional[HistogramFieldWells] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    BinOptions: Optional[HistogramBinOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class KPIVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[KPIConfigurationOutput] = None
    ConditionalFormatting: Optional[KPIConditionalFormattingOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class KPIVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[KPIConfiguration] = None
    ConditionalFormatting: Optional[KPIConditionalFormatting] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class LineChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[LineChartFieldWellsOutput] = None
    SortConfiguration: Optional[LineChartSortConfigurationOutput] = None
    ForecastConfigurations: Optional[List[ForecastConfigurationOutput]] = None
    Type: Optional[LineChartTypeType] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptions] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    PrimaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptionsOutput] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    SecondaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptionsOutput] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    SingleAxisOptions: Optional[SingleAxisOptions] = None
    DefaultSeriesSettings: Optional[LineChartDefaultSeriesSettings] = None
    Series: Optional[List[SeriesItem]] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefaultOutput]] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class LineChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[LineChartFieldWells] = None
    SortConfiguration: Optional[LineChartSortConfiguration] = None
    ForecastConfigurations: Optional[List[ForecastConfiguration]] = None
    Type: Optional[LineChartTypeType] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptions] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    PrimaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptions] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    SecondaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptions] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    SingleAxisOptions: Optional[SingleAxisOptions] = None
    DefaultSeriesSettings: Optional[LineChartDefaultSeriesSettings] = None
    Series: Optional[List[SeriesItem]] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    ReferenceLines: Optional[List[ReferenceLine]] = None
    Tooltip: Optional[TooltipOptions] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefault]] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class PieChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[PieChartFieldWellsOutput] = None
    SortConfiguration: Optional[PieChartSortConfigurationOutput] = None
    DonutOptions: Optional[DonutOptions] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptions] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefaultOutput]] = None
    Interactions: Optional[VisualInteractionOptions] = None


class PieChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[PieChartFieldWells] = None
    SortConfiguration: Optional[PieChartSortConfiguration] = None
    DonutOptions: Optional[DonutOptions] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptions] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptions] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefault]] = None
    Interactions: Optional[VisualInteractionOptions] = None


class PivotTableConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[PivotTableFieldWellsOutput] = None
    SortConfiguration: Optional[PivotTableSortConfigurationOutput] = None
    TableOptions: Optional[PivotTableOptionsOutput] = None
    TotalOptions: Optional[PivotTableTotalOptionsOutput] = None
    FieldOptions: Optional[PivotTableFieldOptionsOutput] = None
    PaginatedReportOptions: Optional[PivotTablePaginatedReportOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class PivotTableConfiguration(BaseValidatorModel):
    FieldWells: Optional[PivotTableFieldWells] = None
    SortConfiguration: Optional[PivotTableSortConfiguration] = None
    TableOptions: Optional[PivotTableOptions] = None
    TotalOptions: Optional[PivotTableTotalOptions] = None
    FieldOptions: Optional[PivotTableFieldOptions] = None
    PaginatedReportOptions: Optional[PivotTablePaginatedReportOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class RadarChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[RadarChartFieldWellsOutput] = None
    SortConfiguration: Optional[RadarChartSortConfigurationOutput] = None
    Shape: Optional[RadarChartShapeType] = None
    BaseSeriesSettings: Optional[RadarChartSeriesSettings] = None
    StartAngle: Optional[float] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    AlternateBandColorsVisibility: Optional[VisibilityType] = None
    AlternateBandEvenColor: Optional[str] = None
    AlternateBandOddColor: Optional[str] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutput] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ColorAxis: Optional[AxisDisplayOptionsOutput] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    AxesRangeScale: Optional[RadarChartAxesRangeScaleType] = None
    Interactions: Optional[VisualInteractionOptions] = None


class RadarChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[RadarChartFieldWells] = None
    SortConfiguration: Optional[RadarChartSortConfiguration] = None
    Shape: Optional[RadarChartShapeType] = None
    BaseSeriesSettings: Optional[RadarChartSeriesSettings] = None
    StartAngle: Optional[float] = None
    VisualPalette: Optional[VisualPalette] = None
    AlternateBandColorsVisibility: Optional[VisibilityType] = None
    AlternateBandEvenColor: Optional[str] = None
    AlternateBandOddColor: Optional[str] = None
    CategoryAxis: Optional[AxisDisplayOptions] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    ColorAxis: Optional[AxisDisplayOptions] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptions] = None
    Legend: Optional[LegendOptions] = None
    AxesRangeScale: Optional[RadarChartAxesRangeScaleType] = None
    Interactions: Optional[VisualInteractionOptions] = None


class SankeyDiagramChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[SankeyDiagramFieldWellsOutput] = None
    SortConfiguration: Optional[SankeyDiagramSortConfigurationOutput] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class SankeyDiagramChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[SankeyDiagramFieldWells] = None
    SortConfiguration: Optional[SankeyDiagramSortConfiguration] = None
    DataLabels: Optional[DataLabelOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class ScatterPlotConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[ScatterPlotFieldWellsOutput] = None
    SortConfiguration: Optional[ScatterPlotSortConfiguration] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    YAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class ScatterPlotConfiguration(BaseValidatorModel):
    FieldWells: Optional[ScatterPlotFieldWells] = None
    SortConfiguration: Optional[ScatterPlotSortConfiguration] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    YAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    Interactions: Optional[VisualInteractionOptions] = None


class InsightConfigurationOutput(BaseValidatorModel):
    Computations: Optional[List[Computation]] = None
    CustomNarrative: Optional[CustomNarrativeOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class InsightConfiguration(BaseValidatorModel):
    Computations: Optional[List[Computation]] = None
    CustomNarrative: Optional[CustomNarrativeOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class TreeMapConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[TreeMapFieldWellsOutput] = None
    SortConfiguration: Optional[TreeMapSortConfigurationOutput] = None
    GroupLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    SizeLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    ColorScale: Optional[ColorScaleOutput] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    Tooltip: Optional[TooltipOptionsOutput] = None
    Interactions: Optional[VisualInteractionOptions] = None


class TreeMapConfiguration(BaseValidatorModel):
    FieldWells: Optional[TreeMapFieldWells] = None
    SortConfiguration: Optional[TreeMapSortConfiguration] = None
    GroupLabelOptions: Optional[ChartAxisLabelOptions] = None
    SizeLabelOptions: Optional[ChartAxisLabelOptions] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptions] = None
    ColorScale: Optional[ColorScale] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    Tooltip: Optional[TooltipOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class WaterfallChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[WaterfallChartFieldWellsOutput] = None
    SortConfiguration: Optional[WaterfallChartSortConfigurationOutput] = None
    WaterfallChartOptions: Optional[WaterfallChartOptions] = None
    CategoryAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    CategoryAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutput] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptionsOutput] = None
    VisualPalette: Optional[VisualPaletteOutput] = None
    ColorConfiguration: Optional[WaterfallChartColorConfiguration] = None
    Interactions: Optional[VisualInteractionOptions] = None


class WaterfallChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[WaterfallChartFieldWells] = None
    SortConfiguration: Optional[WaterfallChartSortConfiguration] = None
    WaterfallChartOptions: Optional[WaterfallChartOptions] = None
    CategoryAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    CategoryAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptions] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptions] = None
    Legend: Optional[LegendOptions] = None
    DataLabels: Optional[DataLabelOptions] = None
    VisualPalette: Optional[VisualPalette] = None
    ColorConfiguration: Optional[WaterfallChartColorConfiguration] = None
    Interactions: Optional[VisualInteractionOptions] = None


class WordCloudChartConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[WordCloudFieldWellsOutput] = None
    SortConfiguration: Optional[WordCloudSortConfigurationOutput] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutput] = None
    WordCloudOptions: Optional[WordCloudOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class WordCloudChartConfiguration(BaseValidatorModel):
    FieldWells: Optional[WordCloudFieldWells] = None
    SortConfiguration: Optional[WordCloudSortConfiguration] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptions] = None
    WordCloudOptions: Optional[WordCloudOptions] = None
    Interactions: Optional[VisualInteractionOptions] = None


class PluginVisualOutput(BaseValidatorModel):
    VisualId: str
    PluginArn: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[PluginVisualConfigurationOutput] = None
    VisualContentAltText: Optional[str] = None


class PluginVisual(BaseValidatorModel):
    VisualId: str
    PluginArn: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[PluginVisualConfiguration] = None
    VisualContentAltText: Optional[str] = None


class TableConfigurationOutput(BaseValidatorModel):
    FieldWells: Optional[TableFieldWellsOutput] = None
    SortConfiguration: Optional[TableSortConfigurationOutput] = None
    TableOptions: Optional[TableOptionsOutput] = None
    TotalOptions: Optional[TotalOptionsOutput] = None
    FieldOptions: Optional[TableFieldOptionsOutput] = None
    PaginatedReportOptions: Optional[TablePaginatedReportOptions] = None
    TableInlineVisualizations: Optional[List[TableInlineVisualization]] = None
    Interactions: Optional[VisualInteractionOptions] = None


class TableConfiguration(BaseValidatorModel):
    FieldWells: Optional[TableFieldWells] = None
    SortConfiguration: Optional[TableSortConfiguration] = None
    TableOptions: Optional[TableOptions] = None
    TotalOptions: Optional[TotalOptions] = None
    FieldOptions: Optional[TableFieldOptions] = None
    PaginatedReportOptions: Optional[TablePaginatedReportOptions] = None
    TableInlineVisualizations: Optional[List[TableInlineVisualization]] = None
    Interactions: Optional[VisualInteractionOptions] = None


class LayoutConfigurationOutput(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfigurationOutput] = None
    FreeFormLayout: Optional[FreeFormLayoutConfigurationOutput] = None
    SectionBasedLayout: Optional[SectionBasedLayoutConfigurationOutput] = None


class LayoutConfiguration(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfiguration] = None
    FreeFormLayout: Optional[FreeFormLayoutConfiguration] = None
    SectionBasedLayout: Optional[SectionBasedLayoutConfiguration] = None

TopicIRUnion = Union[TopicIR, TopicIROutput]


class DescribeAnalysisResponse(BaseValidatorModel):
    Analysis: Analysis
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class Dashboard(BaseValidatorModel):
    DashboardId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[DashboardVersion] = None
    CreatedTime: Optional[datetime] = None
    LastPublishedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    LinkEntities: Optional[List[str]] = None


class Template(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[TemplateVersion] = None
    TemplateId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None


class FilterOutput(BaseValidatorModel):
    CategoryFilter: Optional[CategoryFilterOutput] = None
    NumericRangeFilter: Optional[NumericRangeFilterOutput] = None
    NumericEqualityFilter: Optional[NumericEqualityFilterOutput] = None
    TimeEqualityFilter: Optional[TimeEqualityFilterOutput] = None
    TimeRangeFilter: Optional[TimeRangeFilterOutput] = None
    RelativeDatesFilter: Optional[RelativeDatesFilterOutput] = None
    TopBottomFilter: Optional[TopBottomFilterOutput] = None
    NestedFilter: Optional[NestedFilterOutput] = None


class Filter(BaseValidatorModel):
    CategoryFilter: Optional[CategoryFilter] = None
    NumericRangeFilter: Optional[NumericRangeFilter] = None
    NumericEqualityFilter: Optional[NumericEqualityFilter] = None
    TimeEqualityFilter: Optional[TimeEqualityFilter] = None
    TimeRangeFilter: Optional[TimeRangeFilter] = None
    RelativeDatesFilter: Optional[RelativeDatesFilter] = None
    TopBottomFilter: Optional[TopBottomFilter] = None
    NestedFilter: Optional[NestedFilter] = None


class BarChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[BarChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class BarChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[BarChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class BoxPlotVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[BoxPlotChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class BoxPlotVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[BoxPlotChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class ComboChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[ComboChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class ComboChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[ComboChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class FilledMapVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[FilledMapConfigurationOutput] = None
    ConditionalFormatting: Optional[FilledMapConditionalFormattingOutput] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class FilledMapVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[FilledMapConfiguration] = None
    ConditionalFormatting: Optional[FilledMapConditionalFormatting] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class FunnelChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[FunnelChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class FunnelChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[FunnelChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class GeospatialLayerMapConfigurationOutput(BaseValidatorModel):
    Legend: Optional[LegendOptions] = None
    MapLayers: Optional[List[GeospatialLayerItemOutput]] = None
    MapState: Optional[GeospatialMapState] = None
    MapStyle: Optional[GeospatialMapStyle] = None
    Interactions: Optional[VisualInteractionOptions] = None


class GeospatialLayerMapConfiguration(BaseValidatorModel):
    Legend: Optional[LegendOptions] = None
    MapLayers: Optional[List[GeospatialLayerItem]] = None
    MapState: Optional[GeospatialMapState] = None
    MapStyle: Optional[GeospatialMapStyle] = None
    Interactions: Optional[VisualInteractionOptions] = None


class GeospatialMapVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[GeospatialMapConfigurationOutput] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class GeospatialMapVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[GeospatialMapConfiguration] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class HeatMapVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[HeatMapConfigurationOutput] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class HeatMapVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[HeatMapConfiguration] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class HistogramVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[HistogramConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class HistogramVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[HistogramConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class LineChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[LineChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class LineChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[LineChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class PieChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[PieChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class PieChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[PieChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class PivotTableVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[PivotTableConfigurationOutput] = None
    ConditionalFormatting: Optional[PivotTableConditionalFormattingOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class PivotTableVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[PivotTableConfiguration] = None
    ConditionalFormatting: Optional[PivotTableConditionalFormatting] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class RadarChartVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[RadarChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class RadarChartVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[RadarChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class SankeyDiagramVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[SankeyDiagramChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class SankeyDiagramVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[SankeyDiagramChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class ScatterPlotVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[ScatterPlotConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class ScatterPlotVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[ScatterPlotConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class InsightVisualOutput(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    InsightConfiguration: Optional[InsightConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class InsightVisual(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    InsightConfiguration: Optional[InsightConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class TreeMapVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[TreeMapConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class TreeMapVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[TreeMapConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class WaterfallVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[WaterfallChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class WaterfallVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[WaterfallChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class WordCloudVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[WordCloudChartConfigurationOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutput]] = None
    VisualContentAltText: Optional[str] = None


class WordCloudVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[WordCloudChartConfiguration] = None
    Actions: Optional[List[VisualCustomAction]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchy]] = None
    VisualContentAltText: Optional[str] = None


class TableVisualOutput(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[TableConfigurationOutput] = None
    ConditionalFormatting: Optional[TableConditionalFormattingOutput] = None
    Actions: Optional[List[VisualCustomActionOutput]] = None
    VisualContentAltText: Optional[str] = None


class TableVisual(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[TableConfiguration] = None
    ConditionalFormatting: Optional[TableConditionalFormatting] = None
    Actions: Optional[List[VisualCustomAction]] = None
    VisualContentAltText: Optional[str] = None


class LayoutOutput(BaseValidatorModel):
    Configuration: LayoutConfigurationOutput


class Layout(BaseValidatorModel):
    Configuration: LayoutConfiguration


class TopicVisual(BaseValidatorModel):
    VisualId: Optional[str] = None
    Role: Optional[VisualRoleType] = None
    Ir: Optional[TopicIRUnion] = None
    SupportingVisuals: Optional[List[Dict[str, Any]]] = None


class DescribeDashboardResponse(BaseValidatorModel):
    Dashboard: Dashboard
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeTemplateResponse(BaseValidatorModel):
    Template: Template
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class FilterGroupOutput(BaseValidatorModel):
    FilterGroupId: str
    Filters: List[FilterOutput]
    ScopeConfiguration: FilterScopeConfigurationOutput
    CrossDataset: CrossDatasetTypesType
    Status: Optional[WidgetStatusType] = None


class FilterGroup(BaseValidatorModel):
    FilterGroupId: str
    Filters: List[Filter]
    ScopeConfiguration: FilterScopeConfiguration
    CrossDataset: CrossDatasetTypesType
    Status: Optional[WidgetStatusType] = None


class LayerMapVisualOutput(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[GeospatialLayerMapConfigurationOutput] = None
    VisualContentAltText: Optional[str] = None


class LayerMapVisual(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptions] = None
    Subtitle: Optional[VisualSubtitleLabelOptions] = None
    ChartConfiguration: Optional[GeospatialLayerMapConfiguration] = None
    VisualContentAltText: Optional[str] = None

TopicVisualUnion = Union[TopicVisual, TopicVisualOutput]


class VisualOutput(BaseValidatorModel):
    TableVisual: Optional[TableVisualOutput] = None
    PivotTableVisual: Optional[PivotTableVisualOutput] = None
    BarChartVisual: Optional[BarChartVisualOutput] = None
    KPIVisual: Optional[KPIVisualOutput] = None
    PieChartVisual: Optional[PieChartVisualOutput] = None
    GaugeChartVisual: Optional[GaugeChartVisualOutput] = None
    LineChartVisual: Optional[LineChartVisualOutput] = None
    HeatMapVisual: Optional[HeatMapVisualOutput] = None
    TreeMapVisual: Optional[TreeMapVisualOutput] = None
    GeospatialMapVisual: Optional[GeospatialMapVisualOutput] = None
    FilledMapVisual: Optional[FilledMapVisualOutput] = None
    LayerMapVisual: Optional[LayerMapVisualOutput] = None
    FunnelChartVisual: Optional[FunnelChartVisualOutput] = None
    ScatterPlotVisual: Optional[ScatterPlotVisualOutput] = None
    ComboChartVisual: Optional[ComboChartVisualOutput] = None
    BoxPlotVisual: Optional[BoxPlotVisualOutput] = None
    WaterfallVisual: Optional[WaterfallVisualOutput] = None
    HistogramVisual: Optional[HistogramVisualOutput] = None
    WordCloudVisual: Optional[WordCloudVisualOutput] = None
    InsightVisual: Optional[InsightVisualOutput] = None
    SankeyDiagramVisual: Optional[SankeyDiagramVisualOutput] = None
    CustomContentVisual: Optional[CustomContentVisualOutput] = None
    EmptyVisual: Optional[EmptyVisualOutput] = None
    RadarChartVisual: Optional[RadarChartVisualOutput] = None
    PluginVisual: Optional[PluginVisualOutput] = None


class Visual(BaseValidatorModel):
    TableVisual: Optional[TableVisual] = None
    PivotTableVisual: Optional[PivotTableVisual] = None
    BarChartVisual: Optional[BarChartVisual] = None
    KPIVisual: Optional[KPIVisual] = None
    PieChartVisual: Optional[PieChartVisual] = None
    GaugeChartVisual: Optional[GaugeChartVisual] = None
    LineChartVisual: Optional[LineChartVisual] = None
    HeatMapVisual: Optional[HeatMapVisual] = None
    TreeMapVisual: Optional[TreeMapVisual] = None
    GeospatialMapVisual: Optional[GeospatialMapVisual] = None
    FilledMapVisual: Optional[FilledMapVisual] = None
    LayerMapVisual: Optional[LayerMapVisual] = None
    FunnelChartVisual: Optional[FunnelChartVisual] = None
    ScatterPlotVisual: Optional[ScatterPlotVisual] = None
    ComboChartVisual: Optional[ComboChartVisual] = None
    BoxPlotVisual: Optional[BoxPlotVisual] = None
    WaterfallVisual: Optional[WaterfallVisual] = None
    HistogramVisual: Optional[HistogramVisual] = None
    WordCloudVisual: Optional[WordCloudVisual] = None
    InsightVisual: Optional[InsightVisual] = None
    SankeyDiagramVisual: Optional[SankeyDiagramVisual] = None
    CustomContentVisual: Optional[CustomContentVisual] = None
    EmptyVisual: Optional[EmptyVisual] = None
    RadarChartVisual: Optional[RadarChartVisual] = None
    PluginVisual: Optional[PluginVisual] = None


class CreateTopicReviewedAnswer(BaseValidatorModel):
    AnswerId: str
    DatasetArn: str
    Question: str
    Mir: Optional[TopicIRUnion] = None
    PrimaryVisual: Optional[TopicVisualUnion] = None
    Template: Optional[TopicTemplateUnion] = None


class SheetDefinitionOutput(BaseValidatorModel):
    SheetId: str
    Title: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ParameterControls: Optional[List[ParameterControlOutput]] = None
    FilterControls: Optional[List[FilterControlOutput]] = None
    Visuals: Optional[List[VisualOutput]] = None
    TextBoxes: Optional[List[SheetTextBox]] = None
    Images: Optional[List[SheetImageOutput]] = None
    Layouts: Optional[List[LayoutOutput]] = None
    SheetControlLayouts: Optional[List[SheetControlLayoutOutput]] = None
    ContentType: Optional[SheetContentTypeType] = None


class SheetDefinition(BaseValidatorModel):
    SheetId: str
    Title: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ParameterControls: Optional[List[ParameterControl]] = None
    FilterControls: Optional[List[FilterControl]] = None
    Visuals: Optional[List[Visual]] = None
    TextBoxes: Optional[List[SheetTextBox]] = None
    Images: Optional[List[SheetImage]] = None
    Layouts: Optional[List[Layout]] = None
    SheetControlLayouts: Optional[List[SheetControlLayout]] = None
    ContentType: Optional[SheetContentTypeType] = None


class BatchCreateTopicReviewedAnswerRequest(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    Answers: List[CreateTopicReviewedAnswer]


class AnalysisDefinitionOutput(BaseValidatorModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclaration]
    Sheets: Optional[List[SheetDefinitionOutput]] = None
    CalculatedFields: Optional[List[CalculatedField]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutput]] = None
    FilterGroups: Optional[List[FilterGroupOutput]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutput]] = None
    AnalysisDefaults: Optional[AnalysisDefaults] = None
    Options: Optional[AssetOptions] = None
    QueryExecutionOptions: Optional[QueryExecutionOptions] = None
    StaticFiles: Optional[List[StaticFile]] = None


class DashboardVersionDefinitionOutput(BaseValidatorModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclaration]
    Sheets: Optional[List[SheetDefinitionOutput]] = None
    CalculatedFields: Optional[List[CalculatedField]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutput]] = None
    FilterGroups: Optional[List[FilterGroupOutput]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutput]] = None
    AnalysisDefaults: Optional[AnalysisDefaults] = None
    Options: Optional[AssetOptions] = None
    StaticFiles: Optional[List[StaticFile]] = None


class TemplateVersionDefinitionOutput(BaseValidatorModel):
    DataSetConfigurations: List[DataSetConfigurationOutput]
    Sheets: Optional[List[SheetDefinitionOutput]] = None
    CalculatedFields: Optional[List[CalculatedField]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutput]] = None
    FilterGroups: Optional[List[FilterGroupOutput]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutput]] = None
    AnalysisDefaults: Optional[AnalysisDefaults] = None
    Options: Optional[AssetOptions] = None
    QueryExecutionOptions: Optional[QueryExecutionOptions] = None
    StaticFiles: Optional[List[StaticFile]] = None


class AnalysisDefinition(BaseValidatorModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclaration]
    Sheets: Optional[List[SheetDefinition]] = None
    CalculatedFields: Optional[List[CalculatedField]] = None
    ParameterDeclarations: Optional[List[ParameterDeclaration]] = None
    FilterGroups: Optional[List[FilterGroup]] = None
    ColumnConfigurations: Optional[List[ColumnConfiguration]] = None
    AnalysisDefaults: Optional[AnalysisDefaults] = None
    Options: Optional[AssetOptions] = None
    QueryExecutionOptions: Optional[QueryExecutionOptions] = None
    StaticFiles: Optional[List[StaticFile]] = None


class DashboardVersionDefinition(BaseValidatorModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclaration]
    Sheets: Optional[List[SheetDefinition]] = None
    CalculatedFields: Optional[List[CalculatedField]] = None
    ParameterDeclarations: Optional[List[ParameterDeclaration]] = None
    FilterGroups: Optional[List[FilterGroup]] = None
    ColumnConfigurations: Optional[List[ColumnConfiguration]] = None
    AnalysisDefaults: Optional[AnalysisDefaults] = None
    Options: Optional[AssetOptions] = None
    StaticFiles: Optional[List[StaticFile]] = None


class TemplateVersionDefinition(BaseValidatorModel):
    DataSetConfigurations: List[DataSetConfiguration]
    Sheets: Optional[List[SheetDefinition]] = None
    CalculatedFields: Optional[List[CalculatedField]] = None
    ParameterDeclarations: Optional[List[ParameterDeclaration]] = None
    FilterGroups: Optional[List[FilterGroup]] = None
    ColumnConfigurations: Optional[List[ColumnConfiguration]] = None
    AnalysisDefaults: Optional[AnalysisDefaults] = None
    Options: Optional[AssetOptions] = None
    QueryExecutionOptions: Optional[QueryExecutionOptions] = None
    StaticFiles: Optional[List[StaticFile]] = None


class DescribeAnalysisDefinitionResponse(BaseValidatorModel):
    AnalysisId: str
    Name: str
    Errors: List[AnalysisError]
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: AnalysisDefinitionOutput
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata


class DescribeDashboardDefinitionResponse(BaseValidatorModel):
    DashboardId: str
    Errors: List[DashboardError]
    Name: str
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: DashboardVersionDefinitionOutput
    Status: int
    RequestId: str
    DashboardPublishOptions: DashboardPublishOptions
    ResponseMetadata: ResponseMetadata


class DescribeTemplateDefinitionResponse(BaseValidatorModel):
    Name: str
    TemplateId: str
    Errors: List[TemplateError]
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: TemplateVersionDefinitionOutput
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadata

AnalysisDefinitionUnion = Union[AnalysisDefinition, AnalysisDefinitionOutput]

DashboardVersionDefinitionUnion = Union[DashboardVersionDefinition, DashboardVersionDefinitionOutput]

TemplateVersionDefinitionUnion = Union[TemplateVersionDefinition, TemplateVersionDefinitionOutput]


class CreateAnalysisRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    Name: str
    Parameters: Optional[ParametersUnion] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    SourceEntity: Optional[AnalysisSourceEntity] = None
    ThemeArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Definition: Optional[AnalysisDefinitionUnion] = None
    ValidationStrategy: Optional[ValidationStrategy] = None
    FolderArns: Optional[List[str]] = None


class UpdateAnalysisRequest(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    Name: str
    Parameters: Optional[ParametersUnion] = None
    SourceEntity: Optional[AnalysisSourceEntity] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[AnalysisDefinitionUnion] = None
    ValidationStrategy: Optional[ValidationStrategy] = None


class CreateDashboardRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    Name: str
    Parameters: Optional[ParametersUnion] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    SourceEntity: Optional[DashboardSourceEntity] = None
    Tags: Optional[List[Tag]] = None
    VersionDescription: Optional[str] = None
    DashboardPublishOptions: Optional[DashboardPublishOptions] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[DashboardVersionDefinitionUnion] = None
    ValidationStrategy: Optional[ValidationStrategy] = None
    FolderArns: Optional[List[str]] = None
    LinkSharingConfiguration: Optional[LinkSharingConfigurationUnion] = None
    LinkEntities: Optional[List[str]] = None


class UpdateDashboardRequest(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    Name: str
    SourceEntity: Optional[DashboardSourceEntity] = None
    Parameters: Optional[ParametersUnion] = None
    VersionDescription: Optional[str] = None
    DashboardPublishOptions: Optional[DashboardPublishOptions] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[DashboardVersionDefinitionUnion] = None
    ValidationStrategy: Optional[ValidationStrategy] = None


class CreateTemplateRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    Name: Optional[str] = None
    Permissions: Optional[List[ResourcePermissionUnion]] = None
    SourceEntity: Optional[TemplateSourceEntity] = None
    Tags: Optional[List[Tag]] = None
    VersionDescription: Optional[str] = None
    Definition: Optional[TemplateVersionDefinitionUnion] = None
    ValidationStrategy: Optional[ValidationStrategy] = None


class UpdateTemplateRequest(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    SourceEntity: Optional[TemplateSourceEntity] = None
    VersionDescription: Optional[str] = None
    Name: Optional[str] = None
    Definition: Optional[TemplateVersionDefinitionUnion] = None
    ValidationStrategy: Optional[ValidationStrategy] = None