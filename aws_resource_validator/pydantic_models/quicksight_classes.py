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
from aws_resource_validator.pydantic_models.quicksight_constants import *

class AccountCustomizationTypeDef(BaseModel):
    DefaultTheme: Optional[str] = None
    DefaultEmailCustomizationTemplate: Optional[str] = None

class AccountInfoTypeDef(BaseModel):
    AccountName: Optional[str] = None
    Edition: Optional[EditionType] = None
    NotificationEmail: Optional[str] = None
    AuthenticationType: Optional[str] = None
    AccountSubscriptionStatus: Optional[str] = None
    IAMIdentityCenterInstanceArn: Optional[str] = None

class AccountSettingsTypeDef(BaseModel):
    AccountName: Optional[str] = None
    Edition: Optional[EditionType] = None
    DefaultNamespace: Optional[str] = None
    NotificationEmail: Optional[str] = None
    PublicSharingEnabled: Optional[bool] = None
    TerminationProtectionEnabled: Optional[bool] = None

class ActiveIAMPolicyAssignmentTypeDef(BaseModel):
    AssignmentName: Optional[str] = None
    PolicyArn: Optional[str] = None

class AdHocFilteringOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class AttributeAggregationFunctionTypeDef(BaseModel):
    SimpleAttributeAggregation: Optional[Literal["UNIQUE_VALUE"]] = None
    ValueForMultipleValues: Optional[str] = None

class ColumnIdentifierTypeDef(BaseModel):
    DataSetIdentifier: str
    ColumnName: str

class AmazonElasticsearchParametersTypeDef(BaseModel):
    Domain: str

class AmazonOpenSearchParametersTypeDef(BaseModel):
    Domain: str

class AssetOptionsTypeDef(BaseModel):
    Timezone: Optional[str] = None
    WeekStart: Optional[DayOfTheWeekType] = None

class CalculatedFieldTypeDef(BaseModel):
    DataSetIdentifier: str
    Name: str
    Expression: str

class DataSetIdentifierDeclarationTypeDef(BaseModel):
    Identifier: str
    DataSetArn: str

class EntityTypeDef(BaseModel):
    Path: Optional[str] = None

class AnalysisSearchFilterTypeDef(BaseModel):
    Operator: Optional[FilterOperatorType] = None
    Name: Optional[AnalysisFilterAttributeType] = None
    Value: Optional[str] = None

class DataSetReferenceTypeDef(BaseModel):
    DataSetPlaceholder: str
    DataSetArn: str

class AnalysisSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    AnalysisId: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ResourceStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class SheetTypeDef(BaseModel):
    SheetId: Optional[str] = None
    Name: Optional[str] = None

class AnchorDateConfigurationTypeDef(BaseModel):
    AnchorOption: Optional[Literal["NOW"]] = None
    ParameterName: Optional[str] = None

class AnonymousUserDashboardEmbeddingConfigurationTypeDef(BaseModel):
    InitialDashboardId: str

class DashboardVisualIdTypeDef(BaseModel):
    DashboardId: str
    SheetId: str
    VisualId: str

class AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef(BaseModel):
    InitialTopicId: str

class AnonymousUserQSearchBarEmbeddingConfigurationTypeDef(BaseModel):
    InitialTopicId: str

class ArcAxisDisplayRangeTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class ArcConfigurationTypeDef(BaseModel):
    ArcAngle: Optional[float] = None
    ArcThickness: Optional[ArcThicknessOptionsType] = None

class ArcOptionsTypeDef(BaseModel):
    ArcThickness: Optional[ArcThicknessType] = None

class AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[AssetBundleExportJobDataSourcePropertyToOverrideType]

class AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[Literal["StartAfterDateTime"]]

class AssetBundleExportJobResourceIdOverrideConfigurationTypeDef(BaseModel):
    PrefixForAllResources: Optional[bool] = None

class AssetBundleExportJobThemeOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef(BaseModel):
    Arn: str
    Properties: List[AssetBundleExportJobVPCConnectionPropertyToOverrideType]

class AssetBundleExportJobAnalysisOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobDashboardOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobDataSetOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobDataSourceOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[AssetBundleExportJobDataSourcePropertyToOverrideType]

class AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[Literal["StartAfterDateTime"]]

class AssetBundleExportJobThemeOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef(BaseModel):
    Arn: str
    Properties: Sequence[AssetBundleExportJobVPCConnectionPropertyToOverrideType]

class AssetBundleExportJobErrorTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleExportJobSummaryTypeDef(BaseModel):
    JobStatus: Optional[AssetBundleExportJobStatusType] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AssetBundleExportJobId: Optional[str] = None
    IncludeAllDependencies: Optional[bool] = None
    ExportFormat: Optional[AssetBundleExportFormatType] = None
    IncludePermissions: Optional[bool] = None
    IncludeTags: Optional[bool] = None

class AssetBundleExportJobValidationStrategyTypeDef(BaseModel):
    StrictModeForAllResources: Optional[bool] = None

class AssetBundleExportJobWarningTypeDef(BaseModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleImportJobAnalysisOverrideParametersTypeDef(BaseModel):
    AnalysisId: str
    Name: Optional[str] = None

class AssetBundleResourcePermissionsOutputTypeDef(BaseModel):
    Principals: List[str]
    Actions: List[str]

class AssetBundleResourcePermissionsTypeDef(BaseModel):
    Principals: Sequence[str]
    Actions: Sequence[str]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AssetBundleImportJobDashboardOverrideParametersTypeDef(BaseModel):
    DashboardId: str
    Name: Optional[str] = None

class AssetBundleImportJobDataSetOverrideParametersTypeDef(BaseModel):
    DataSetId: str
    Name: Optional[str] = None

class AssetBundleImportJobDataSourceCredentialPairTypeDef(BaseModel):
    Username: str
    Password: str

class SslPropertiesTypeDef(BaseModel):
    DisableSsl: Optional[bool] = None

class VpcConnectionPropertiesTypeDef(BaseModel):
    VpcConnectionArn: str

class AssetBundleImportJobErrorTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef(BaseModel):
    DataSetId: str
    ScheduleId: str
    StartAfterDateTime: Optional[datetime] = None

class AssetBundleImportJobResourceIdOverrideConfigurationTypeDef(BaseModel):
    PrefixForAllResources: Optional[str] = None

class AssetBundleImportJobThemeOverrideParametersTypeDef(BaseModel):
    ThemeId: str
    Name: Optional[str] = None

class AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef(BaseModel):
    VPCConnectionId: str
    Name: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    RoleArn: Optional[str] = None

class AssetBundleImportJobVPCConnectionOverrideParametersTypeDef(BaseModel):
    VPCConnectionId: str
    Name: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    DnsResolvers: Optional[Sequence[str]] = None
    RoleArn: Optional[str] = None

class AssetBundleImportJobOverrideValidationStrategyTypeDef(BaseModel):
    StrictModeForAllResources: Optional[bool] = None

class AssetBundleImportJobSummaryTypeDef(BaseModel):
    JobStatus: Optional[AssetBundleImportJobStatusType] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AssetBundleImportJobId: Optional[str] = None
    FailureAction: Optional[AssetBundleImportFailureActionType] = None

class AssetBundleImportJobWarningTypeDef(BaseModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleImportSourceDescriptionTypeDef(BaseModel):
    Body: Optional[str] = None
    S3Uri: Optional[str] = None

class AthenaParametersTypeDef(BaseModel):
    WorkGroup: Optional[str] = None
    RoleArn: Optional[str] = None

class AuroraParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class AuroraPostgreSqlParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class AuthorizedTargetsByServiceTypeDef(BaseModel):
    Service: Optional[Literal["REDSHIFT"]] = None
    AuthorizedTargets: Optional[List[str]] = None

class AwsIotAnalyticsParametersTypeDef(BaseModel):
    DataSetName: str

class DateAxisOptionsTypeDef(BaseModel):
    MissingDateVisibility: Optional[VisibilityType] = None

class AxisDisplayMinMaxRangeTypeDef(BaseModel):
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None

class AxisLinearScaleTypeDef(BaseModel):
    StepCount: Optional[int] = None
    StepSize: Optional[float] = None

class AxisLogarithmicScaleTypeDef(BaseModel):
    Base: Optional[float] = None

class ItemsLimitConfigurationTypeDef(BaseModel):
    ItemsLimit: Optional[int] = None
    OtherCategories: Optional[OtherCategoriesType] = None

class BigQueryParametersTypeDef(BaseModel):
    ProjectId: str
    DataSetRegion: Optional[str] = None

class BinCountOptionsTypeDef(BaseModel):
    Value: Optional[int] = None

class BinWidthOptionsTypeDef(BaseModel):
    Value: Optional[float] = None
    BinCountLimit: Optional[int] = None

class SectionAfterPageBreakTypeDef(BaseModel):
    Status: Optional[SectionPageBreakStatusType] = None

class BookmarksConfigurationsTypeDef(BaseModel):
    Enabled: bool

class BorderStyleTypeDef(BaseModel):
    Show: Optional[bool] = None

class BoxPlotStyleOptionsTypeDef(BaseModel):
    FillStyle: Optional[BoxPlotFillStyleType] = None

class PaginationConfigurationTypeDef(BaseModel):
    PageSize: int
    PageNumber: int

class CalculatedColumnTypeDef(BaseModel):
    ColumnName: str
    ColumnId: str
    Expression: str

class CalculatedMeasureFieldTypeDef(BaseModel):
    FieldId: str
    Expression: str

class CancelIngestionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    IngestionId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CastColumnTypeOperationTypeDef(BaseModel):
    ColumnName: str
    NewColumnType: ColumnDataTypeType
    SubType: Optional[ColumnDataSubTypeType] = None
    Format: Optional[str] = None

class CustomFilterConfigurationTypeDef(BaseModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValue: Optional[str] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    ParameterName: Optional[str] = None

class CustomFilterListConfigurationOutputTypeDef(BaseModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None

class FilterListConfigurationOutputTypeDef(BaseModel):
    MatchOperator: CategoryFilterMatchOperatorType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    NullOption: Optional[FilterNullOptionType] = None

class CustomFilterListConfigurationTypeDef(BaseModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValues: Optional[Sequence[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None

class FilterListConfigurationTypeDef(BaseModel):
    MatchOperator: CategoryFilterMatchOperatorType
    CategoryValues: Optional[Sequence[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    NullOption: Optional[FilterNullOptionType] = None

class CellValueSynonymOutputTypeDef(BaseModel):
    CellValue: Optional[str] = None
    Synonyms: Optional[List[str]] = None

class CellValueSynonymTypeDef(BaseModel):
    CellValue: Optional[str] = None
    Synonyms: Optional[Sequence[str]] = None

class SimpleClusterMarkerTypeDef(BaseModel):
    Color: Optional[str] = None

class CollectiveConstantOutputTypeDef(BaseModel):
    ValueList: Optional[List[str]] = None

class CollectiveConstantTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class DataColorTypeDef(BaseModel):
    Color: Optional[str] = None
    DataValue: Optional[float] = None

class CustomColorTypeDef(BaseModel):
    Color: str
    FieldValue: Optional[str] = None
    SpecialValue: Optional[SpecialValueType] = None

class ColumnDescriptionTypeDef(BaseModel):
    Text: Optional[str] = None

class ColumnGroupColumnSchemaTypeDef(BaseModel):
    Name: Optional[str] = None

class GeoSpatialColumnGroupOutputTypeDef(BaseModel):
    Name: str
    Columns: List[str]
    CountryCode: Optional[Literal["US"]] = None

class GeoSpatialColumnGroupTypeDef(BaseModel):
    Name: str
    Columns: Sequence[str]
    CountryCode: Optional[Literal["US"]] = None

class ColumnLevelPermissionRuleOutputTypeDef(BaseModel):
    Principals: Optional[List[str]] = None
    ColumnNames: Optional[List[str]] = None

class ColumnLevelPermissionRuleTypeDef(BaseModel):
    Principals: Optional[Sequence[str]] = None
    ColumnNames: Optional[Sequence[str]] = None

class ColumnSchemaTypeDef(BaseModel):
    Name: Optional[str] = None
    DataType: Optional[str] = None
    GeographicRole: Optional[str] = None

class ComparativeOrderOutputTypeDef(BaseModel):
    UseOrdering: Optional[ColumnOrderingTypeType] = None
    SpecifedOrder: Optional[List[str]] = None
    TreatUndefinedSpecifiedValues: Optional[UndefinedSpecifiedValueTypeType] = None

class ComparativeOrderTypeDef(BaseModel):
    UseOrdering: Optional[ColumnOrderingTypeType] = None
    SpecifedOrder: Optional[Sequence[str]] = None
    TreatUndefinedSpecifiedValues: Optional[UndefinedSpecifiedValueTypeType] = None

class ConditionalFormattingSolidColorTypeDef(BaseModel):
    Expression: str
    Color: Optional[str] = None

class ConditionalFormattingCustomIconOptionsTypeDef(BaseModel):
    Icon: Optional[IconType] = None
    UnicodeIcon: Optional[str] = None

class ConditionalFormattingIconDisplayConfigurationTypeDef(BaseModel):
    IconDisplayOption: Optional[Literal["ICON_ONLY"]] = None

class ConditionalFormattingIconSetTypeDef(BaseModel):
    Expression: str
    IconSetType: Optional[ConditionalFormattingIconSetTypeType] = None

class ContextMenuOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class CreateAccountSubscriptionRequestRequestTypeDef(BaseModel):
    AuthenticationMethod: AuthenticationMethodOptionType
    AwsAccountId: str
    AccountName: str
    NotificationEmail: str
    Edition: Optional[EditionType] = None
    ActiveDirectoryName: Optional[str] = None
    Realm: Optional[str] = None
    DirectoryId: Optional[str] = None
    AdminGroup: Optional[Sequence[str]] = None
    AuthorGroup: Optional[Sequence[str]] = None
    ReaderGroup: Optional[Sequence[str]] = None
    AdminProGroup: Optional[Sequence[str]] = None
    AuthorProGroup: Optional[Sequence[str]] = None
    ReaderProGroup: Optional[Sequence[str]] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    EmailAddress: Optional[str] = None
    ContactNumber: Optional[str] = None
    IAMIdentityCenterInstanceArn: Optional[str] = None

class SignupResponseTypeDef(BaseModel):
    IAMUser: Optional[bool] = None
    userLoginName: Optional[str] = None
    accountName: Optional[str] = None
    directoryType: Optional[str] = None

class ValidationStrategyTypeDef(BaseModel):
    Mode: ValidationStrategyModeType

class DataSetUsageConfigurationTypeDef(BaseModel):
    DisableUseAsDirectQuerySource: Optional[bool] = None
    DisableUseAsImportedSource: Optional[bool] = None

class RowLevelPermissionDataSetTypeDef(BaseModel):
    Arn: str
    PermissionPolicy: RowLevelPermissionPolicyType
    Namespace: Optional[str] = None
    FormatVersion: Optional[RowLevelPermissionFormatVersionType] = None
    Status: Optional[StatusType] = None

class CreateFolderMembershipRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    MemberId: str
    MemberType: MemberTypeType

class FolderMemberTypeDef(BaseModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None

class CreateGroupMembershipRequestRequestTypeDef(BaseModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str

class GroupMemberTypeDef(BaseModel):
    Arn: Optional[str] = None
    MemberName: Optional[str] = None

class CreateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    Description: Optional[str] = None

class GroupTypeDef(BaseModel):
    Arn: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    PrincipalId: Optional[str] = None

class CreateIAMPolicyAssignmentRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssignmentName: str
    AssignmentStatus: AssignmentStatusType
    Namespace: str
    PolicyArn: Optional[str] = None
    Identities: Optional[Mapping[str, Sequence[str]]] = None

class CreateIngestionRequestRequestTypeDef(BaseModel):
    DataSetId: str
    IngestionId: str
    AwsAccountId: str
    IngestionType: Optional[IngestionTypeType] = None

class CreateRoleMembershipRequestRequestTypeDef(BaseModel):
    MemberName: str
    AwsAccountId: str
    Namespace: str
    Role: RoleType

class CreateTemplateAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str
    TemplateVersionNumber: int

class TemplateAliasTypeDef(BaseModel):
    AliasName: Optional[str] = None
    Arn: Optional[str] = None
    TemplateVersionNumber: Optional[int] = None

class CreateThemeAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str
    ThemeVersionNumber: int

class ThemeAliasTypeDef(BaseModel):
    Arn: Optional[str] = None
    AliasName: Optional[str] = None
    ThemeVersionNumber: Optional[int] = None

class DecimalPlacesConfigurationTypeDef(BaseModel):
    DecimalPlaces: int

class NegativeValueConfigurationTypeDef(BaseModel):
    DisplayMode: NegativeValueDisplayModeType

class NullValueFormatConfigurationTypeDef(BaseModel):
    NullString: str

class LocalNavigationConfigurationTypeDef(BaseModel):
    TargetSheetId: str

class CustomActionURLOperationTypeDef(BaseModel):
    URLTemplate: str
    URLTarget: URLTargetConfigurationType

class CustomNarrativeOptionsTypeDef(BaseModel):
    Narrative: str

class CustomParameterValuesOutputTypeDef(BaseModel):
    StringValues: Optional[List[str]] = None
    IntegerValues: Optional[List[int]] = None
    DecimalValues: Optional[List[float]] = None
    DateTimeValues: Optional[List[datetime]] = None

class InputColumnTypeDef(BaseModel):
    Name: str
    Type: InputColumnDataTypeType
    SubType: Optional[ColumnDataSubTypeType] = None

class DataPointDrillUpDownOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DataPointMenuLabelOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DataPointTooltipOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class ExportToCSVOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class ExportWithHiddenFieldsOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class SheetControlsOptionTypeDef(BaseModel):
    VisibilityState: Optional[DashboardUIStateType] = None

class SheetLayoutElementMaximizationOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class VisualAxisSortOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class VisualMenuOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DashboardSearchFilterTypeDef(BaseModel):
    Operator: FilterOperatorType
    Name: Optional[DashboardFilterAttributeType] = None
    Value: Optional[str] = None

class DashboardSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    DashboardId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    PublishedVersionNumber: Optional[int] = None
    LastPublishedTime: Optional[datetime] = None

class DashboardVersionSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    SourceEntityArn: Optional[str] = None
    Description: Optional[str] = None

class ExportHiddenFieldsOptionTypeDef(BaseModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DataAggregationTypeDef(BaseModel):
    DatasetRowDateGranularity: Optional[TopicTimeGranularityType] = None
    DefaultDateColumnName: Optional[str] = None

class DataBarsOptionsTypeDef(BaseModel):
    FieldId: str
    PositiveColor: Optional[str] = None
    NegativeColor: Optional[str] = None

class DataColorPaletteOutputTypeDef(BaseModel):
    Colors: Optional[List[str]] = None
    MinMaxGradient: Optional[List[str]] = None
    EmptyFillColor: Optional[str] = None

class DataColorPaletteTypeDef(BaseModel):
    Colors: Optional[Sequence[str]] = None
    MinMaxGradient: Optional[Sequence[str]] = None
    EmptyFillColor: Optional[str] = None

class DataPathLabelTypeTypeDef(BaseModel):
    FieldId: Optional[str] = None
    FieldValue: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class FieldLabelTypeTypeDef(BaseModel):
    FieldId: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class MaximumLabelTypeTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class MinimumLabelTypeTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class RangeEndsLabelTypeTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class DataPathTypeTypeDef(BaseModel):
    PivotTableDataPathType: Optional[PivotTableDataPathTypeType] = None

class DataSetSearchFilterTypeDef(BaseModel):
    Operator: FilterOperatorType
    Name: DataSetFilterAttributeType
    Value: str

class FieldFolderOutputTypeDef(BaseModel):
    description: Optional[str] = None
    columns: Optional[List[str]] = None

class OutputColumnTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[ColumnDataTypeType] = None
    SubType: Optional[ColumnDataSubTypeType] = None

class DataSourceErrorInfoTypeDef(BaseModel):
    Type: Optional[DataSourceErrorInfoTypeType] = None
    Message: Optional[str] = None

class DatabricksParametersTypeDef(BaseModel):
    Host: str
    Port: int
    SqlEndpointPath: str

class ExasolParametersTypeDef(BaseModel):
    Host: str
    Port: int

class JiraParametersTypeDef(BaseModel):
    SiteBaseUrl: str

class MariaDbParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class MySqlParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class OracleParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class PostgreSqlParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class PrestoParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Catalog: str

class RdsParametersTypeDef(BaseModel):
    InstanceId: str
    Database: str

class ServiceNowParametersTypeDef(BaseModel):
    SiteBaseUrl: str

class SnowflakeParametersTypeDef(BaseModel):
    Host: str
    Database: str
    Warehouse: str

class SparkParametersTypeDef(BaseModel):
    Host: str
    Port: int

class SqlServerParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class StarburstParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Catalog: str
    ProductType: Optional[StarburstProductTypeType] = None

class TeradataParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Database: str

class TrinoParametersTypeDef(BaseModel):
    Host: str
    Port: int
    Catalog: str

class TwitterParametersTypeDef(BaseModel):
    Query: str
    MaxRows: int

class DataSourceSearchFilterTypeDef(BaseModel):
    Operator: FilterOperatorType
    Name: DataSourceFilterAttributeType
    Value: str

class DataSourceSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    DataSourceId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class DateTimeDatasetParameterDefaultValuesOutputTypeDef(BaseModel):
    StaticValues: Optional[List[datetime]] = None

class RollingDateConfigurationTypeDef(BaseModel):
    Expression: str
    DataSetIdentifier: Optional[str] = None

class DateTimeValueWhenUnsetConfigurationOutputTypeDef(BaseModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[datetime] = None

class MappedDataSetParameterTypeDef(BaseModel):
    DataSetIdentifier: str
    DataSetParameterName: str

class DateTimeParameterOutputTypeDef(BaseModel):
    Name: str
    Values: List[datetime]

class SheetControlInfoIconLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    InfoIconText: Optional[str] = None

class DecimalDatasetParameterDefaultValuesOutputTypeDef(BaseModel):
    StaticValues: Optional[List[float]] = None

class DecimalDatasetParameterDefaultValuesTypeDef(BaseModel):
    StaticValues: Optional[Sequence[float]] = None

class DecimalValueWhenUnsetConfigurationTypeDef(BaseModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[float] = None

class DecimalParameterOutputTypeDef(BaseModel):
    Name: str
    Values: List[float]

class DecimalParameterTypeDef(BaseModel):
    Name: str
    Values: Sequence[float]

class FilterSelectableValuesOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class FilterSelectableValuesTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None

class DeleteAccountCustomizationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: Optional[str] = None

class DeleteAccountSubscriptionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str

class DeleteAnalysisRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None

class DeleteDashboardRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None

class DeleteDataSetRefreshPropertiesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str

class DeleteDataSetRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str

class DeleteDataSourceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSourceId: str

class DeleteFolderMembershipRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    MemberId: str
    MemberType: MemberTypeType

class DeleteFolderRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str

class DeleteGroupMembershipRequestRequestTypeDef(BaseModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DeleteIAMPolicyAssignmentRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str

class DeleteIdentityPropagationConfigRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Service: Literal["REDSHIFT"]

class DeleteNamespaceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str

class DeleteRefreshScheduleRequestRequestTypeDef(BaseModel):
    DataSetId: str
    AwsAccountId: str
    ScheduleId: str

class DeleteRoleCustomPermissionRequestRequestTypeDef(BaseModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class DeleteRoleMembershipRequestRequestTypeDef(BaseModel):
    MemberName: str
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class DeleteTemplateAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str

class DeleteTemplateRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None

class DeleteThemeAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str

class DeleteThemeRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    VersionNumber: Optional[int] = None

class DeleteTopicRefreshScheduleRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str

class DeleteTopicRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str

class DeleteUserByPrincipalIdRequestRequestTypeDef(BaseModel):
    PrincipalId: str
    AwsAccountId: str
    Namespace: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AwsAccountId: str
    Namespace: str

class DeleteVPCConnectionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    VPCConnectionId: str

class DescribeAccountCustomizationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: Optional[str] = None
    Resolved: Optional[bool] = None

class DescribeAccountSettingsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str

class DescribeAccountSubscriptionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str

class DescribeAnalysisDefinitionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str

class DescribeAnalysisPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str

class ResourcePermissionOutputTypeDef(BaseModel):
    Principal: str
    Actions: List[str]

class DescribeAnalysisRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str

class DescribeAssetBundleExportJobRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssetBundleExportJobId: str

class DescribeAssetBundleImportJobRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssetBundleImportJobId: str

class DescribeDashboardDefinitionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeDashboardPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str

class DescribeDashboardRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeDashboardSnapshotJobRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str

class DescribeDashboardSnapshotJobResultRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str

class SnapshotJobErrorInfoTypeDef(BaseModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[str] = None

class DescribeDataSetPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str

class DescribeDataSetRefreshPropertiesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str

class DescribeDataSetRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str

class DescribeDataSourcePermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSourceId: str

class DescribeDataSourceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSourceId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeFolderPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResourcePermissionExtraOutputTypeDef(BaseModel):
    Principal: str
    Actions: List[str]

class DescribeFolderRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str

class DescribeFolderResolvedPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class FolderTypeDef(BaseModel):
    FolderId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    FolderPath: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SharingModel: Optional[SharingModelType] = None

class DescribeGroupMembershipRequestRequestTypeDef(BaseModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DescribeGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DescribeIAMPolicyAssignmentRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str

class IAMPolicyAssignmentTypeDef(BaseModel):
    AwsAccountId: Optional[str] = None
    AssignmentId: Optional[str] = None
    AssignmentName: Optional[str] = None
    PolicyArn: Optional[str] = None
    Identities: Optional[Dict[str, List[str]]] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None

class DescribeIngestionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    IngestionId: str

class DescribeIpRestrictionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str

class DescribeKeyRegistrationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DefaultKeyOnly: Optional[bool] = None

class RegisteredCustomerManagedKeyTypeDef(BaseModel):
    KeyArn: Optional[str] = None
    DefaultKey: Optional[bool] = None

class DescribeNamespaceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str

class DescribeRefreshScheduleRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    ScheduleId: str

class DescribeRoleCustomPermissionRequestRequestTypeDef(BaseModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class DescribeTemplateAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str

class DescribeTemplateDefinitionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeTemplatePermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str

class DescribeTemplateRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeThemeAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str

class DescribeThemePermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str

class DescribeThemeRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeTopicPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str

class DescribeTopicRefreshRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    RefreshId: str

class TopicRefreshDetailsTypeDef(BaseModel):
    RefreshArn: Optional[str] = None
    RefreshId: Optional[str] = None
    RefreshStatus: Optional[TopicRefreshStatusType] = None

class DescribeTopicRefreshScheduleRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str

class TopicRefreshScheduleOutputTypeDef(BaseModel):
    IsEnabled: bool
    BasedOnSpiceSchedule: bool
    StartingAt: Optional[datetime] = None
    Timezone: Optional[str] = None
    RepeatAt: Optional[str] = None
    TopicScheduleType: Optional[TopicScheduleTypeType] = None

class DescribeTopicRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str

class DescribeUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AwsAccountId: str
    Namespace: str

class UserTypeDef(BaseModel):
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

class DescribeVPCConnectionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    VPCConnectionId: str

class NegativeFormatTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None

class DonutCenterOptionsTypeDef(BaseModel):
    LabelVisibility: Optional[VisibilityType] = None

class ListControlSelectAllOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class ErrorInfoTypeDef(BaseModel):
    Type: Optional[IngestionErrorTypeType] = None
    Message: Optional[str] = None

class ExcludePeriodConfigurationTypeDef(BaseModel):
    Amount: int
    Granularity: TimeGranularityType
    Status: Optional[WidgetStatusType] = None

class FailedKeyRegistrationEntryTypeDef(BaseModel):
    Message: str
    StatusCode: int
    SenderFault: bool
    KeyArn: Optional[str] = None

class FieldFolderTypeDef(BaseModel):
    description: Optional[str] = None
    columns: Optional[Sequence[str]] = None

class FieldSortTypeDef(BaseModel):
    FieldId: str
    Direction: SortDirectionType

class FieldTooltipItemTypeDef(BaseModel):
    FieldId: str
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    TooltipTarget: Optional[TooltipTargetType] = None

class GeospatialMapStyleOptionsTypeDef(BaseModel):
    BaseMapStyle: Optional[BaseMapStyleTypeType] = None

class SameSheetTargetVisualConfigurationOutputTypeDef(BaseModel):
    TargetVisuals: Optional[List[str]] = None
    TargetVisualOptions: Optional[Literal["ALL_VISUALS"]] = None

class SameSheetTargetVisualConfigurationTypeDef(BaseModel):
    TargetVisuals: Optional[Sequence[str]] = None
    TargetVisualOptions: Optional[Literal["ALL_VISUALS"]] = None

class FilterOperationTypeDef(BaseModel):
    ConditionExpression: str

class FolderSearchFilterTypeDef(BaseModel):
    Operator: Optional[FilterOperatorType] = None
    Name: Optional[FolderFilterAttributeType] = None
    Value: Optional[str] = None

class FolderSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    FolderId: Optional[str] = None
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SharingModel: Optional[SharingModelType] = None

class FontSizeTypeDef(BaseModel):
    Relative: Optional[RelativeFontSizeType] = None

class FontWeightTypeDef(BaseModel):
    Name: Optional[FontWeightNameType] = None

class FontTypeDef(BaseModel):
    FontFamily: Optional[str] = None

class TimeBasedForecastPropertiesTypeDef(BaseModel):
    PeriodsForward: Optional[int] = None
    PeriodsBackward: Optional[int] = None
    UpperBoundary: Optional[float] = None
    LowerBoundary: Optional[float] = None
    PredictionInterval: Optional[int] = None
    Seasonality: Optional[int] = None

class WhatIfPointScenarioOutputTypeDef(BaseModel):
    Date: datetime
    Value: float

class WhatIfRangeScenarioOutputTypeDef(BaseModel):
    StartDate: datetime
    EndDate: datetime
    Value: float

class FreeFormLayoutScreenCanvasSizeOptionsTypeDef(BaseModel):
    OptimizedViewPortWidth: str

class FreeFormLayoutElementBackgroundStyleTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None

class FreeFormLayoutElementBorderStyleTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None

class LoadingAnimationTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class GaugeChartColorConfigurationTypeDef(BaseModel):
    ForegroundColor: Optional[str] = None
    BackgroundColor: Optional[str] = None

class SessionTagTypeDef(BaseModel):
    Key: str
    Value: str

class GeospatialCoordinateBoundsTypeDef(BaseModel):
    North: float
    South: float
    West: float
    East: float

class GeospatialHeatmapDataColorTypeDef(BaseModel):
    Color: str

class GetDashboardEmbedUrlRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    IdentityType: EmbeddingIdentityTypeType
    SessionLifetimeInMinutes: Optional[int] = None
    UndoRedoDisabled: Optional[bool] = None
    ResetDisabled: Optional[bool] = None
    StatePersistenceEnabled: Optional[bool] = None
    UserArn: Optional[str] = None
    Namespace: Optional[str] = None
    AdditionalDashboardIds: Optional[Sequence[str]] = None

class GetSessionEmbedUrlRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    EntryPoint: Optional[str] = None
    SessionLifetimeInMinutes: Optional[int] = None
    UserArn: Optional[str] = None

class TableBorderOptionsTypeDef(BaseModel):
    Color: Optional[str] = None
    Thickness: Optional[int] = None
    Style: Optional[TableBorderStyleType] = None

class GradientStopTypeDef(BaseModel):
    GradientOffset: float
    DataValue: Optional[float] = None
    Color: Optional[str] = None

class GridLayoutScreenCanvasSizeOptionsTypeDef(BaseModel):
    ResizeOption: ResizeOptionType
    OptimizedViewPortWidth: Optional[str] = None

class GridLayoutElementTypeDef(BaseModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    ColumnSpan: int
    RowSpan: int
    ColumnIndex: Optional[int] = None
    RowIndex: Optional[int] = None

class GroupSearchFilterTypeDef(BaseModel):
    Operator: Literal["StartsWith"]
    Name: Literal["GROUP_NAME"]
    Value: str

class GutterStyleTypeDef(BaseModel):
    Show: Optional[bool] = None

class IAMPolicyAssignmentSummaryTypeDef(BaseModel):
    AssignmentName: Optional[str] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None

class IdentityCenterConfigurationTypeDef(BaseModel):
    EnableIdentityPropagation: Optional[bool] = None

class LookbackWindowTypeDef(BaseModel):
    ColumnName: str
    Size: int
    SizeUnit: LookbackWindowSizeUnitType

class QueueInfoTypeDef(BaseModel):
    WaitingOnIngestion: str
    QueuedIngestion: str

class RowInfoTypeDef(BaseModel):
    RowsIngested: Optional[int] = None
    RowsDropped: Optional[int] = None
    TotalRowsInDataset: Optional[int] = None

class IntegerDatasetParameterDefaultValuesOutputTypeDef(BaseModel):
    StaticValues: Optional[List[int]] = None

class IntegerDatasetParameterDefaultValuesTypeDef(BaseModel):
    StaticValues: Optional[Sequence[int]] = None

class IntegerValueWhenUnsetConfigurationTypeDef(BaseModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[int] = None

class IntegerParameterOutputTypeDef(BaseModel):
    Name: str
    Values: List[int]

class IntegerParameterTypeDef(BaseModel):
    Name: str
    Values: Sequence[int]

class JoinKeyPropertiesTypeDef(BaseModel):
    UniqueKey: Optional[bool] = None

class KPISparklineOptionsTypeDef(BaseModel):
    Type: KPISparklineTypeType
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None
    TooltipVisibility: Optional[VisibilityType] = None

class ProgressBarOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class SecondaryValueOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class TrendArrowOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class KPIVisualStandardLayoutTypeDef(BaseModel):
    Type: KPIVisualStandardLayoutTypeType

class LineChartLineStyleSettingsTypeDef(BaseModel):
    LineVisibility: Optional[VisibilityType] = None
    LineInterpolation: Optional[LineInterpolationType] = None
    LineStyle: Optional[LineChartLineStyleType] = None
    LineWidth: Optional[str] = None

class LineChartMarkerStyleSettingsTypeDef(BaseModel):
    MarkerVisibility: Optional[VisibilityType] = None
    MarkerShape: Optional[LineChartMarkerShapeType] = None
    MarkerSize: Optional[str] = None
    MarkerColor: Optional[str] = None

class MissingDataConfigurationTypeDef(BaseModel):
    TreatmentOption: Optional[MissingDataTreatmentOptionType] = None

class ResourcePermissionTypeDef(BaseModel):
    Principal: str
    Actions: Sequence[str]

class ListAnalysesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAssetBundleExportJobsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAssetBundleImportJobsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListControlSearchOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class ListDashboardVersionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDashboardsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataSetsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFolderMembersRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MemberIdArnPairTypeDef(BaseModel):
    MemberId: Optional[str] = None
    MemberArn: Optional[str] = None

class ListFoldersRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupMembershipsRequestRequestTypeDef(BaseModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIAMPolicyAssignmentsForUserRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    UserName: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIAMPolicyAssignmentsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentityPropagationConfigsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListIngestionsRequestRequestTypeDef(BaseModel):
    DataSetId: str
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListNamespacesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRefreshSchedulesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str

class ListRoleMembershipsRequestRequestTypeDef(BaseModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListTemplateAliasesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTemplateVersionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TemplateVersionSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    VersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    Status: Optional[ResourceStatusType] = None
    Description: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TemplateSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    TemplateId: Optional[str] = None
    Name: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class ListThemeAliasesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListThemeVersionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ThemeVersionSummaryTypeDef(BaseModel):
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Status: Optional[ResourceStatusType] = None

class ListThemesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Type: Optional[ThemeTypeType] = None

class ThemeSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ThemeId: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class ListTopicRefreshSchedulesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str

class ListTopicsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TopicSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    TopicId: Optional[str] = None
    Name: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None

class ListUserGroupsRequestRequestTypeDef(BaseModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVPCConnectionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LongFormatTextTypeDef(BaseModel):
    PlainText: Optional[str] = None
    RichText: Optional[str] = None

class ManifestFileLocationTypeDef(BaseModel):
    Bucket: str
    Key: str

class MarginStyleTypeDef(BaseModel):
    Show: Optional[bool] = None

class NamedEntityDefinitionMetricOutputTypeDef(BaseModel):
    Aggregation: Optional[NamedEntityAggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None

class NamedEntityDefinitionMetricTypeDef(BaseModel):
    Aggregation: Optional[NamedEntityAggTypeType] = None
    AggregationFunctionParameters: Optional[Mapping[str, str]] = None

class NamespaceErrorTypeDef(BaseModel):
    Type: Optional[NamespaceErrorTypeType] = None
    Message: Optional[str] = None

class NetworkInterfaceTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    ErrorMessage: Optional[str] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    NetworkInterfaceId: Optional[str] = None

class NewDefaultValuesOutputTypeDef(BaseModel):
    StringStaticValues: Optional[List[str]] = None
    DecimalStaticValues: Optional[List[float]] = None
    DateTimeStaticValues: Optional[List[datetime]] = None
    IntegerStaticValues: Optional[List[int]] = None

class NumericRangeFilterValueTypeDef(BaseModel):
    StaticValue: Optional[float] = None
    Parameter: Optional[str] = None

class ThousandSeparatorOptionsTypeDef(BaseModel):
    Symbol: Optional[NumericSeparatorSymbolType] = None
    Visibility: Optional[VisibilityType] = None

class PercentileAggregationTypeDef(BaseModel):
    PercentileValue: Optional[float] = None

class StringParameterOutputTypeDef(BaseModel):
    Name: str
    Values: List[str]

class StringParameterTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class PercentVisibleRangeTypeDef(BaseModel):
    From: Optional[float] = None
    To: Optional[float] = None

class PivotTableConditionalFormattingScopeTypeDef(BaseModel):
    Role: Optional[PivotTableConditionalFormattingScopeRoleType] = None

class PivotTablePaginatedReportOptionsTypeDef(BaseModel):
    VerticalOverflowVisibility: Optional[VisibilityType] = None
    OverflowColumnHeaderVisibility: Optional[VisibilityType] = None

class PivotTableFieldOptionTypeDef(BaseModel):
    FieldId: str
    CustomLabel: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class PivotTableFieldSubtotalOptionsTypeDef(BaseModel):
    FieldId: Optional[str] = None

class PivotTableRowsLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None

class RowAlternateColorOptionsOutputTypeDef(BaseModel):
    Status: Optional[WidgetStatusType] = None
    RowAlternateColors: Optional[List[str]] = None
    UsePrimaryBackgroundColor: Optional[WidgetStatusType] = None

class RowAlternateColorOptionsTypeDef(BaseModel):
    Status: Optional[WidgetStatusType] = None
    RowAlternateColors: Optional[Sequence[str]] = None
    UsePrimaryBackgroundColor: Optional[WidgetStatusType] = None

class ProjectOperationOutputTypeDef(BaseModel):
    ProjectedColumns: List[str]

class ProjectOperationTypeDef(BaseModel):
    ProjectedColumns: Sequence[str]

class RadarChartAreaStyleSettingsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class RangeConstantTypeDef(BaseModel):
    Minimum: Optional[str] = None
    Maximum: Optional[str] = None

class RedshiftIAMParametersExtraOutputTypeDef(BaseModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[List[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None

class RedshiftIAMParametersOutputTypeDef(BaseModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[List[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None

class RedshiftIAMParametersTypeDef(BaseModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[Sequence[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None

class ReferenceLineCustomLabelConfigurationTypeDef(BaseModel):
    CustomLabel: str

class ReferenceLineStaticDataConfigurationTypeDef(BaseModel):
    Value: float

class ReferenceLineStyleConfigurationTypeDef(BaseModel):
    Pattern: Optional[ReferenceLinePatternTypeType] = None
    Color: Optional[str] = None

class ScheduleRefreshOnEntityTypeDef(BaseModel):
    DayOfWeek: Optional[DayOfWeekType] = None
    DayOfMonth: Optional[str] = None

class StatePersistenceConfigurationsTypeDef(BaseModel):
    Enabled: bool

class RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef(BaseModel):
    InitialTopicId: Optional[str] = None

class RegisteredUserQSearchBarEmbeddingConfigurationTypeDef(BaseModel):
    InitialTopicId: Optional[str] = None

class RenameColumnOperationTypeDef(BaseModel):
    ColumnName: str
    NewColumnName: str

class RestoreAnalysisRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str

class RowLevelPermissionTagRuleTypeDef(BaseModel):
    TagKey: str
    ColumnName: str
    TagMultiValueDelimiter: Optional[str] = None
    MatchAllValue: Optional[str] = None

class S3BucketConfigurationTypeDef(BaseModel):
    BucketName: str
    BucketPrefix: str
    BucketRegion: str

class UploadSettingsTypeDef(BaseModel):
    Format: Optional[FileFormatType] = None
    StartFromRow: Optional[int] = None
    ContainsHeader: Optional[bool] = None
    TextQualifier: Optional[TextQualifierType] = None
    Delimiter: Optional[str] = None

class SpacingTypeDef(BaseModel):
    Top: Optional[str] = None
    Bottom: Optional[str] = None
    Left: Optional[str] = None
    Right: Optional[str] = None

class SheetVisualScopingConfigurationOutputTypeDef(BaseModel):
    SheetId: str
    Scope: FilterVisualScopeType
    VisualIds: Optional[List[str]] = None

class SheetVisualScopingConfigurationTypeDef(BaseModel):
    SheetId: str
    Scope: FilterVisualScopeType
    VisualIds: Optional[Sequence[str]] = None

class SemanticEntityTypeOutputTypeDef(BaseModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None

class SemanticEntityTypeTypeDef(BaseModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Mapping[str, str]] = None

class SemanticTypeOutputTypeDef(BaseModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None
    TruthyCellValue: Optional[str] = None
    TruthyCellValueSynonyms: Optional[List[str]] = None
    FalseyCellValue: Optional[str] = None
    FalseyCellValueSynonyms: Optional[List[str]] = None

class SemanticTypeTypeDef(BaseModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Mapping[str, str]] = None
    TruthyCellValue: Optional[str] = None
    TruthyCellValueSynonyms: Optional[Sequence[str]] = None
    FalseyCellValue: Optional[str] = None
    FalseyCellValueSynonyms: Optional[Sequence[str]] = None

class SheetTextBoxTypeDef(BaseModel):
    SheetTextBoxId: str
    Content: Optional[str] = None

class SheetElementConfigurationOverridesTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class ShortFormatTextTypeDef(BaseModel):
    PlainText: Optional[str] = None
    RichText: Optional[str] = None

class YAxisOptionsTypeDef(BaseModel):
    YAxis: Literal["PRIMARY_Y_AXIS"]

class SmallMultiplesAxisPropertiesTypeDef(BaseModel):
    Scale: Optional[SmallMultiplesAxisScaleType] = None
    Placement: Optional[SmallMultiplesAxisPlacementType] = None

class SnapshotAnonymousUserRedactedTypeDef(BaseModel):
    RowLevelPermissionTagKeys: Optional[List[str]] = None

class SnapshotFileSheetSelectionOutputTypeDef(BaseModel):
    SheetId: str
    SelectionScope: SnapshotFileSheetSelectionScopeType
    VisualIds: Optional[List[str]] = None

class SnapshotFileSheetSelectionTypeDef(BaseModel):
    SheetId: str
    SelectionScope: SnapshotFileSheetSelectionScopeType
    VisualIds: Optional[Sequence[str]] = None

class SnapshotJobResultErrorInfoTypeDef(BaseModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[str] = None

class StringDatasetParameterDefaultValuesOutputTypeDef(BaseModel):
    StaticValues: Optional[List[str]] = None

class StringDatasetParameterDefaultValuesTypeDef(BaseModel):
    StaticValues: Optional[Sequence[str]] = None

class StringValueWhenUnsetConfigurationTypeDef(BaseModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[str] = None

class TableStyleTargetTypeDef(BaseModel):
    CellType: StyledCellTypeType

class SuccessfulKeyRegistrationEntryTypeDef(BaseModel):
    KeyArn: str
    StatusCode: int

class TableCellImageSizingConfigurationTypeDef(BaseModel):
    TableCellImageScalingConfiguration: Optional[TableCellImageScalingConfigurationType] = None

class TablePaginatedReportOptionsTypeDef(BaseModel):
    VerticalOverflowVisibility: Optional[VisibilityType] = None
    OverflowColumnHeaderVisibility: Optional[VisibilityType] = None

class TableFieldCustomIconContentTypeDef(BaseModel):
    Icon: Optional[Literal["LINK"]] = None

class TablePinnedFieldOptionsOutputTypeDef(BaseModel):
    PinnedLeftFields: Optional[List[str]] = None

class TablePinnedFieldOptionsTypeDef(BaseModel):
    PinnedLeftFields: Optional[Sequence[str]] = None

class TemplateSourceTemplateTypeDef(BaseModel):
    Arn: str

class TextControlPlaceholderOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None

class UIColorPaletteTypeDef(BaseModel):
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

class ThemeErrorTypeDef(BaseModel):
    Type: Optional[Literal["INTERNAL_FAILURE"]] = None
    Message: Optional[str] = None

class TopicSingularFilterConstantTypeDef(BaseModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None

class TotalAggregationFunctionTypeDef(BaseModel):
    SimpleTotalAggregationFunction: Optional[SimpleTotalAggregationFunctionType] = None

class UntagColumnOperationOutputTypeDef(BaseModel):
    ColumnName: str
    TagNames: List[ColumnTagNameType]

class UntagColumnOperationTypeDef(BaseModel):
    ColumnName: str
    TagNames: Sequence[ColumnTagNameType]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAccountSettingsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DefaultNamespace: str
    NotificationEmail: Optional[str] = None
    TerminationProtectionEnabled: Optional[bool] = None

class UpdateDashboardLinksRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    LinkEntities: Sequence[str]

class UpdateDashboardPublishedVersionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: int

class UpdateFolderRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    Name: str

class UpdateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    Description: Optional[str] = None

class UpdateIAMPolicyAssignmentRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    PolicyArn: Optional[str] = None
    Identities: Optional[Mapping[str, Sequence[str]]] = None

class UpdateIdentityPropagationConfigRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Service: Literal["REDSHIFT"]
    AuthorizedTargets: Optional[Sequence[str]] = None

class UpdateIpRestrictionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    IpRestrictionRuleMap: Optional[Mapping[str, str]] = None
    VpcIdRestrictionRuleMap: Optional[Mapping[str, str]] = None
    VpcEndpointIdRestrictionRuleMap: Optional[Mapping[str, str]] = None
    Enabled: Optional[bool] = None

class UpdatePublicSharingSettingsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    PublicSharingEnabled: Optional[bool] = None

class UpdateRoleCustomPermissionRequestRequestTypeDef(BaseModel):
    CustomPermissionsName: str
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class UpdateSPICECapacityConfigurationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    PurchaseMode: PurchaseModeType

class UpdateTemplateAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str
    TemplateVersionNumber: int

class UpdateThemeAliasRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str
    ThemeVersionNumber: int

class UpdateUserRequestRequestTypeDef(BaseModel):
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

class UpdateVPCConnectionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    VPCConnectionId: str
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    RoleArn: str
    DnsResolvers: Optional[Sequence[str]] = None

class WaterfallChartGroupColorConfigurationTypeDef(BaseModel):
    PositiveBarColor: Optional[str] = None
    NegativeBarColor: Optional[str] = None
    TotalBarColor: Optional[str] = None

class WaterfallChartOptionsTypeDef(BaseModel):
    TotalBarLabel: Optional[str] = None

class WordCloudOptionsTypeDef(BaseModel):
    WordOrientation: Optional[WordCloudWordOrientationType] = None
    WordScaling: Optional[WordCloudWordScalingType] = None
    CloudLayout: Optional[WordCloudCloudLayoutType] = None
    WordCasing: Optional[WordCloudWordCasingType] = None
    WordPadding: Optional[WordCloudWordPaddingType] = None
    MaximumStringLength: Optional[int] = None

class UpdateAccountCustomizationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AccountCustomization: AccountCustomizationTypeDef
    Namespace: Optional[str] = None

class AxisLabelReferenceOptionsTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef

class CascadingControlSourceTypeDef(BaseModel):
    SourceSheetControlId: Optional[str] = None
    ColumnToMatch: Optional[ColumnIdentifierTypeDef] = None

class CategoryDrillDownFilterOutputTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    CategoryValues: List[str]

class CategoryDrillDownFilterTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    CategoryValues: Sequence[str]

class ContributionAnalysisDefaultOutputTypeDef(BaseModel):
    MeasureFieldId: str
    ContributorDimensions: List[ColumnIdentifierTypeDef]

class ContributionAnalysisDefaultTypeDef(BaseModel):
    MeasureFieldId: str
    ContributorDimensions: Sequence[ColumnIdentifierTypeDef]

class DynamicDefaultValueTypeDef(BaseModel):
    DefaultValueColumn: ColumnIdentifierTypeDef
    UserNameColumn: Optional[ColumnIdentifierTypeDef] = None
    GroupNameColumn: Optional[ColumnIdentifierTypeDef] = None

class FilterOperationSelectedFieldsConfigurationOutputTypeDef(BaseModel):
    SelectedFields: Optional[List[str]] = None
    SelectedFieldOptions: Optional[Literal["ALL_FIELDS"]] = None
    SelectedColumns: Optional[List[ColumnIdentifierTypeDef]] = None

class FilterOperationSelectedFieldsConfigurationTypeDef(BaseModel):
    SelectedFields: Optional[Sequence[str]] = None
    SelectedFieldOptions: Optional[Literal["ALL_FIELDS"]] = None
    SelectedColumns: Optional[Sequence[ColumnIdentifierTypeDef]] = None

class NumericEqualityDrillDownFilterTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Value: float

class ParameterSelectableValuesOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None
    LinkToDataSetColumn: Optional[ColumnIdentifierTypeDef] = None

class ParameterSelectableValuesTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None
    LinkToDataSetColumn: Optional[ColumnIdentifierTypeDef] = None

class TimeRangeDrillDownFilterOutputTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    RangeMinimum: datetime
    RangeMaximum: datetime
    TimeGranularity: TimeGranularityType

class AnalysisErrorTypeDef(BaseModel):
    Type: Optional[AnalysisErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[EntityTypeDef]] = None

class DashboardErrorTypeDef(BaseModel):
    Type: Optional[DashboardErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[EntityTypeDef]] = None

class TemplateErrorTypeDef(BaseModel):
    Type: Optional[TemplateErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[EntityTypeDef]] = None

class SearchAnalysesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[AnalysisSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class AnalysisSourceTemplateTypeDef(BaseModel):
    DataSetReferences: Sequence[DataSetReferenceTypeDef]
    Arn: str

class DashboardSourceTemplateTypeDef(BaseModel):
    DataSetReferences: Sequence[DataSetReferenceTypeDef]
    Arn: str

class TemplateSourceAnalysisTypeDef(BaseModel):
    Arn: str
    DataSetReferences: Sequence[DataSetReferenceTypeDef]

class AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef(BaseModel):
    InitialDashboardVisualId: DashboardVisualIdTypeDef

class RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef(BaseModel):
    InitialDashboardVisualId: DashboardVisualIdTypeDef

class ArcAxisConfigurationTypeDef(BaseModel):
    Range: Optional[ArcAxisDisplayRangeTypeDef] = None
    ReserveRange: Optional[int] = None

class AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef(BaseModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleExportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       List[AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef]     ] = None
    RefreshSchedules: Optional[       List[AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef]     ] = None
    DataSources: Optional[       List[AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef]     ] = None
    DataSets: Optional[List[AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef]] = None
    Themes: Optional[List[AssetBundleExportJobThemeOverridePropertiesOutputTypeDef]] = None
    Analyses: Optional[List[AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef]] = None
    Dashboards: Optional[       List[AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef]     ] = None

class AssetBundleCloudFormationOverridePropertyConfigurationTypeDef(BaseModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleExportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       Sequence[AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef]     ] = None
    RefreshSchedules: Optional[       Sequence[AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef]     ] = None
    DataSources: Optional[       Sequence[AssetBundleExportJobDataSourceOverridePropertiesTypeDef]     ] = None
    DataSets: Optional[Sequence[AssetBundleExportJobDataSetOverridePropertiesTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleExportJobThemeOverridePropertiesTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleExportJobAnalysisOverridePropertiesTypeDef]] = None
    Dashboards: Optional[Sequence[AssetBundleExportJobDashboardOverridePropertiesTypeDef]] = None

class AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef(BaseModel):
    AnalysisIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef(BaseModel):
    DataSetIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef(BaseModel):
    DataSourceIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleImportJobThemeOverridePermissionsOutputTypeDef(BaseModel):
    ThemeIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleResourceLinkSharingConfigurationOutputTypeDef(BaseModel):
    Permissions: Optional[AssetBundleResourcePermissionsOutputTypeDef] = None

class AssetBundleImportJobAnalysisOverridePermissionsTypeDef(BaseModel):
    AnalysisIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleImportJobDataSetOverridePermissionsTypeDef(BaseModel):
    DataSetIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleImportJobDataSourceOverridePermissionsTypeDef(BaseModel):
    DataSourceIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleImportJobThemeOverridePermissionsTypeDef(BaseModel):
    ThemeIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleResourceLinkSharingConfigurationTypeDef(BaseModel):
    Permissions: Optional[AssetBundleResourcePermissionsTypeDef] = None

class AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef(BaseModel):
    AnalysisIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobAnalysisOverrideTagsTypeDef(BaseModel):
    AnalysisIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDashboardOverrideTagsOutputTypeDef(BaseModel):
    DashboardIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobDashboardOverrideTagsTypeDef(BaseModel):
    DashboardIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDataSetOverrideTagsOutputTypeDef(BaseModel):
    DataSetIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobDataSetOverrideTagsTypeDef(BaseModel):
    DataSetIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef(BaseModel):
    DataSourceIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobDataSourceOverrideTagsTypeDef(BaseModel):
    DataSourceIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobThemeOverrideTagsOutputTypeDef(BaseModel):
    ThemeIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobThemeOverrideTagsTypeDef(BaseModel):
    ThemeIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef(BaseModel):
    VPCConnectionIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobVPCConnectionOverrideTagsTypeDef(BaseModel):
    VPCConnectionIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class CreateAccountCustomizationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AccountCustomization: AccountCustomizationTypeDef
    Namespace: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateNamespaceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    IdentityStore: Literal["QUICKSIGHT"]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVPCConnectionRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    VPCConnectionId: str
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    RoleArn: str
    DnsResolvers: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class RegisterUserRequestRequestTypeDef(BaseModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDataSourceCredentialsTypeDef(BaseModel):
    CredentialPair: Optional[AssetBundleImportJobDataSourceCredentialPairTypeDef] = None
    SecretArn: Optional[str] = None

class AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef(BaseModel):
    DataSetId: str
    ScheduleId: str
    StartAfterDateTime: Optional[TimestampTypeDef] = None

class CustomParameterValuesTypeDef(BaseModel):
    StringValues: Optional[Sequence[str]] = None
    IntegerValues: Optional[Sequence[int]] = None
    DecimalValues: Optional[Sequence[float]] = None
    DateTimeValues: Optional[Sequence[TimestampTypeDef]] = None

class DateTimeDatasetParameterDefaultValuesTypeDef(BaseModel):
    StaticValues: Optional[Sequence[TimestampTypeDef]] = None

class DateTimeParameterTypeDef(BaseModel):
    Name: str
    Values: Sequence[TimestampTypeDef]

class DateTimeValueWhenUnsetConfigurationTypeDef(BaseModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[TimestampTypeDef] = None

class NewDefaultValuesTypeDef(BaseModel):
    StringStaticValues: Optional[Sequence[str]] = None
    DecimalStaticValues: Optional[Sequence[float]] = None
    DateTimeStaticValues: Optional[Sequence[TimestampTypeDef]] = None
    IntegerStaticValues: Optional[Sequence[int]] = None

class TimeRangeDrillDownFilterTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    RangeMinimum: TimestampTypeDef
    RangeMaximum: TimestampTypeDef
    TimeGranularity: TimeGranularityType

class TopicRefreshScheduleTypeDef(BaseModel):
    IsEnabled: bool
    BasedOnSpiceSchedule: bool
    StartingAt: Optional[TimestampTypeDef] = None
    Timezone: Optional[str] = None
    RepeatAt: Optional[str] = None
    TopicScheduleType: Optional[TopicScheduleTypeType] = None

class WhatIfPointScenarioTypeDef(BaseModel):
    Date: TimestampTypeDef
    Value: float

class WhatIfRangeScenarioTypeDef(BaseModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Value: float

class AssetBundleImportSourceTypeDef(BaseModel):
    Body: Optional[BlobTypeDef] = None
    S3Uri: Optional[str] = None

class AxisDisplayRangeOutputTypeDef(BaseModel):
    MinMax: Optional[AxisDisplayMinMaxRangeTypeDef] = None
    DataDriven: Optional[Dict[str, Any]] = None

class AxisDisplayRangeTypeDef(BaseModel):
    MinMax: Optional[AxisDisplayMinMaxRangeTypeDef] = None
    DataDriven: Optional[Mapping[str, Any]] = None

class AxisScaleTypeDef(BaseModel):
    Linear: Optional[AxisLinearScaleTypeDef] = None
    Logarithmic: Optional[AxisLogarithmicScaleTypeDef] = None

class ScatterPlotSortConfigurationTypeDef(BaseModel):
    ScatterPlotLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class HistogramBinOptionsTypeDef(BaseModel):
    SelectedBinType: Optional[HistogramBinTypeType] = None
    BinCount: Optional[BinCountOptionsTypeDef] = None
    BinWidth: Optional[BinWidthOptionsTypeDef] = None
    StartValue: Optional[float] = None

class BodySectionRepeatPageBreakConfigurationTypeDef(BaseModel):
    After: Optional[SectionAfterPageBreakTypeDef] = None

class SectionPageBreakConfigurationTypeDef(BaseModel):
    After: Optional[SectionAfterPageBreakTypeDef] = None

class TileStyleTypeDef(BaseModel):
    Border: Optional[BorderStyleTypeDef] = None

class BoxPlotOptionsTypeDef(BaseModel):
    StyleOptions: Optional[BoxPlotStyleOptionsTypeDef] = None
    OutlierVisibility: Optional[VisibilityType] = None
    AllDataPointsVisibility: Optional[VisibilityType] = None

class CreateColumnsOperationOutputTypeDef(BaseModel):
    Columns: List[CalculatedColumnTypeDef]

class CreateColumnsOperationTypeDef(BaseModel):
    Columns: Sequence[CalculatedColumnTypeDef]

class CancelIngestionResponseTypeDef(BaseModel):
    Arn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccountCustomizationResponseTypeDef(BaseModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomizationTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnalysisResponseTypeDef(BaseModel):
    Arn: str
    AnalysisId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDashboardResponseTypeDef(BaseModel):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetResponseTypeDef(BaseModel):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseModel):
    Arn: str
    DataSourceId: str
    CreationStatus: ResourceStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFolderResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIAMPolicyAssignmentResponseTypeDef(BaseModel):
    AssignmentName: str
    AssignmentId: str
    AssignmentStatus: AssignmentStatusType
    PolicyArn: str
    Identities: Dict[str, List[str]]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIngestionResponseTypeDef(BaseModel):
    Arn: str
    IngestionId: str
    IngestionStatus: IngestionStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNamespaceResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    CapacityRegion: str
    CreationStatus: NamespaceStatusType
    IdentityStore: Literal["QUICKSIGHT"]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRefreshScheduleResponseTypeDef(BaseModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoleMembershipResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(BaseModel):
    Arn: str
    VersionArn: str
    TemplateId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThemeResponseTypeDef(BaseModel):
    Arn: str
    VersionArn: str
    ThemeId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRefreshScheduleResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicResponseTypeDef(BaseModel):
    Arn: str
    TopicId: str
    RefreshArn: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVPCConnectionResponseTypeDef(BaseModel):
    Arn: str
    VPCConnectionId: str
    CreationStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountCustomizationResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountSubscriptionResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnalysisResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    AnalysisId: str
    DeletionTime: datetime
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDashboardResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    DashboardId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSetRefreshPropertiesResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSetResponseTypeDef(BaseModel):
    Arn: str
    DataSetId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(BaseModel):
    Arn: str
    DataSourceId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFolderMembershipResponseTypeDef(BaseModel):
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFolderResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGroupMembershipResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGroupResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIAMPolicyAssignmentResponseTypeDef(BaseModel):
    AssignmentName: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdentityPropagationConfigResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRefreshScheduleResponseTypeDef(BaseModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRoleCustomPermissionResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRoleMembershipResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateAliasResponseTypeDef(BaseModel):
    Status: int
    TemplateId: str
    AliasName: str
    Arn: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateResponseTypeDef(BaseModel):
    RequestId: str
    Arn: str
    TemplateId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteThemeAliasResponseTypeDef(BaseModel):
    AliasName: str
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteThemeResponseTypeDef(BaseModel):
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTopicRefreshScheduleResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTopicResponseTypeDef(BaseModel):
    Arn: str
    TopicId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserByPrincipalIdResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVPCConnectionResponseTypeDef(BaseModel):
    Arn: str
    VPCConnectionId: str
    DeletionStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountCustomizationResponseTypeDef(BaseModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomizationTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountSettingsResponseTypeDef(BaseModel):
    AccountSettings: AccountSettingsTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountSubscriptionResponseTypeDef(BaseModel):
    AccountInfo: AccountInfoTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpRestrictionResponseTypeDef(BaseModel):
    AwsAccountId: str
    IpRestrictionRuleMap: Dict[str, str]
    VpcIdRestrictionRuleMap: Dict[str, str]
    VpcEndpointIdRestrictionRuleMap: Dict[str, str]
    Enabled: bool
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRoleCustomPermissionResponseTypeDef(BaseModel):
    CustomPermissionsName: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateEmbedUrlForAnonymousUserResponseTypeDef(BaseModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    AnonymousUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateEmbedUrlForRegisteredUserResponseTypeDef(BaseModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardEmbedUrlResponseTypeDef(BaseModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionEmbedUrlResponseTypeDef(BaseModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalysesResponseTypeDef(BaseModel):
    AnalysisSummaryList: List[AnalysisSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAssetBundleExportJobsResponseTypeDef(BaseModel):
    AssetBundleExportJobSummaryList: List[AssetBundleExportJobSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAssetBundleImportJobsResponseTypeDef(BaseModel):
    AssetBundleImportJobSummaryList: List[AssetBundleImportJobSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIAMPolicyAssignmentsForUserResponseTypeDef(BaseModel):
    ActiveAssignments: List[ActiveIAMPolicyAssignmentTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentityPropagationConfigsResponseTypeDef(BaseModel):
    Services: List[AuthorizedTargetsByServiceTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRoleMembershipsResponseTypeDef(BaseModel):
    MembersList: List[str]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataSetRefreshPropertiesResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreAnalysisResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    AnalysisId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAnalysesResponseTypeDef(BaseModel):
    AnalysisSummaryList: List[AnalysisSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartAssetBundleExportJobResponseTypeDef(BaseModel):
    Arn: str
    AssetBundleExportJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssetBundleImportJobResponseTypeDef(BaseModel):
    Arn: str
    AssetBundleImportJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartDashboardSnapshotJobResponseTypeDef(BaseModel):
    Arn: str
    SnapshotJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountCustomizationResponseTypeDef(BaseModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomizationTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnalysisResponseTypeDef(BaseModel):
    Arn: str
    AnalysisId: str
    UpdateStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardLinksResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    DashboardArn: str
    LinkEntities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardPublishedVersionResponseTypeDef(BaseModel):
    DashboardId: str
    DashboardArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardResponseTypeDef(BaseModel):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetPermissionsResponseTypeDef(BaseModel):
    DataSetArn: str
    DataSetId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetResponseTypeDef(BaseModel):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourcePermissionsResponseTypeDef(BaseModel):
    DataSourceArn: str
    DataSourceId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseModel):
    Arn: str
    DataSourceId: str
    UpdateStatus: ResourceStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFolderResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIAMPolicyAssignmentResponseTypeDef(BaseModel):
    AssignmentName: str
    AssignmentId: str
    PolicyArn: str
    Identities: Dict[str, List[str]]
    AssignmentStatus: AssignmentStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityPropagationConfigResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIpRestrictionResponseTypeDef(BaseModel):
    AwsAccountId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublicSharingSettingsResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRefreshScheduleResponseTypeDef(BaseModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoleCustomPermissionResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSPICECapacityConfigurationResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateResponseTypeDef(BaseModel):
    TemplateId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemeResponseTypeDef(BaseModel):
    ThemeId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTopicRefreshScheduleResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTopicResponseTypeDef(BaseModel):
    TopicId: str
    Arn: str
    RefreshArn: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVPCConnectionResponseTypeDef(BaseModel):
    Arn: str
    VPCConnectionId: str
    UpdateStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CategoryFilterConfigurationOutputTypeDef(BaseModel):
    FilterListConfiguration: Optional[FilterListConfigurationOutputTypeDef] = None
    CustomFilterListConfiguration: Optional[CustomFilterListConfigurationOutputTypeDef] = None
    CustomFilterConfiguration: Optional[CustomFilterConfigurationTypeDef] = None

class CategoryFilterConfigurationTypeDef(BaseModel):
    FilterListConfiguration: Optional[FilterListConfigurationTypeDef] = None
    CustomFilterListConfiguration: Optional[CustomFilterListConfigurationTypeDef] = None
    CustomFilterConfiguration: Optional[CustomFilterConfigurationTypeDef] = None

class ClusterMarkerTypeDef(BaseModel):
    SimpleClusterMarker: Optional[SimpleClusterMarkerTypeDef] = None

class TopicCategoryFilterConstantOutputTypeDef(BaseModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None
    CollectiveConstant: Optional[CollectiveConstantOutputTypeDef] = None

class TopicCategoryFilterConstantTypeDef(BaseModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None
    CollectiveConstant: Optional[CollectiveConstantTypeDef] = None

class ColorScaleOutputTypeDef(BaseModel):
    Colors: List[DataColorTypeDef]
    ColorFillType: ColorFillTypeType
    NullValueColor: Optional[DataColorTypeDef] = None

class ColorScaleTypeDef(BaseModel):
    Colors: Sequence[DataColorTypeDef]
    ColorFillType: ColorFillTypeType
    NullValueColor: Optional[DataColorTypeDef] = None

class ColorsConfigurationOutputTypeDef(BaseModel):
    CustomColors: Optional[List[CustomColorTypeDef]] = None

class ColorsConfigurationTypeDef(BaseModel):
    CustomColors: Optional[Sequence[CustomColorTypeDef]] = None

class ColumnTagTypeDef(BaseModel):
    ColumnGeographicRole: Optional[GeoSpatialDataRoleType] = None
    ColumnDescription: Optional[ColumnDescriptionTypeDef] = None

class ColumnGroupSchemaOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    ColumnGroupColumnSchemaList: Optional[List[ColumnGroupColumnSchemaTypeDef]] = None

class ColumnGroupSchemaTypeDef(BaseModel):
    Name: Optional[str] = None
    ColumnGroupColumnSchemaList: Optional[Sequence[ColumnGroupColumnSchemaTypeDef]] = None

class ColumnGroupOutputTypeDef(BaseModel):
    GeoSpatialColumnGroup: Optional[GeoSpatialColumnGroupOutputTypeDef] = None

class ColumnGroupTypeDef(BaseModel):
    GeoSpatialColumnGroup: Optional[GeoSpatialColumnGroupTypeDef] = None

class DataSetSchemaOutputTypeDef(BaseModel):
    ColumnSchemaList: Optional[List[ColumnSchemaTypeDef]] = None

class DataSetSchemaTypeDef(BaseModel):
    ColumnSchemaList: Optional[Sequence[ColumnSchemaTypeDef]] = None

class ConditionalFormattingCustomIconConditionTypeDef(BaseModel):
    Expression: str
    IconOptions: ConditionalFormattingCustomIconOptionsTypeDef
    Color: Optional[str] = None
    DisplayConfiguration: Optional[ConditionalFormattingIconDisplayConfigurationTypeDef] = None

class CreateAccountSubscriptionResponseTypeDef(BaseModel):
    SignupResponse: SignupResponseTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    DataSetId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ImportMode: Optional[DataSetImportModeType] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSetTypeDef] = None
    RowLevelPermissionTagConfigurationApplied: Optional[bool] = None
    ColumnLevelPermissionRulesApplied: Optional[bool] = None

class CreateFolderMembershipResponseTypeDef(BaseModel):
    Status: int
    FolderMember: FolderMemberTypeDef
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupMembershipResponseTypeDef(BaseModel):
    GroupMember: GroupMemberTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupMembershipResponseTypeDef(BaseModel):
    GroupMember: GroupMemberTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupMembershipsResponseTypeDef(BaseModel):
    GroupMemberList: List[GroupMemberTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseModel):
    GroupList: List[GroupTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUserGroupsResponseTypeDef(BaseModel):
    GroupList: List[GroupTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchGroupsResponseTypeDef(BaseModel):
    GroupList: List[GroupTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateAliasResponseTypeDef(BaseModel):
    TemplateAlias: TemplateAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTemplateAliasResponseTypeDef(BaseModel):
    TemplateAlias: TemplateAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateAliasesResponseTypeDef(BaseModel):
    TemplateAliasList: List[TemplateAliasTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateTemplateAliasResponseTypeDef(BaseModel):
    TemplateAlias: TemplateAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThemeAliasResponseTypeDef(BaseModel):
    ThemeAlias: ThemeAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThemeAliasResponseTypeDef(BaseModel):
    ThemeAlias: ThemeAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThemeAliasesResponseTypeDef(BaseModel):
    ThemeAliasList: List[ThemeAliasTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateThemeAliasResponseTypeDef(BaseModel):
    ThemeAlias: ThemeAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomActionNavigationOperationTypeDef(BaseModel):
    LocalNavigationConfiguration: Optional[LocalNavigationConfigurationTypeDef] = None

class CustomValuesConfigurationOutputTypeDef(BaseModel):
    CustomValues: CustomParameterValuesOutputTypeDef
    IncludeNullValue: Optional[bool] = None

class CustomSqlOutputTypeDef(BaseModel):
    DataSourceArn: str
    Name: str
    SqlQuery: str
    Columns: Optional[List[InputColumnTypeDef]] = None

class CustomSqlTypeDef(BaseModel):
    DataSourceArn: str
    Name: str
    SqlQuery: str
    Columns: Optional[Sequence[InputColumnTypeDef]] = None

class RelationalTableOutputTypeDef(BaseModel):
    DataSourceArn: str
    Name: str
    InputColumns: List[InputColumnTypeDef]
    Catalog: Optional[str] = None
    Schema: Optional[str] = None

class RelationalTableTypeDef(BaseModel):
    DataSourceArn: str
    Name: str
    InputColumns: Sequence[InputColumnTypeDef]
    Catalog: Optional[str] = None
    Schema: Optional[str] = None

class VisualInteractionOptionsTypeDef(BaseModel):
    VisualMenuOption: Optional[VisualMenuOptionTypeDef] = None
    ContextMenuOption: Optional[ContextMenuOptionTypeDef] = None

class SearchDashboardsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[DashboardSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDashboardsResponseTypeDef(BaseModel):
    DashboardSummaryList: List[DashboardSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchDashboardsResponseTypeDef(BaseModel):
    DashboardSummaryList: List[DashboardSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDashboardVersionsResponseTypeDef(BaseModel):
    DashboardVersionSummaryList: List[DashboardVersionSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DashboardVisualPublishOptionsTypeDef(BaseModel):
    ExportHiddenFieldsOption: Optional[ExportHiddenFieldsOptionTypeDef] = None

class TableInlineVisualizationTypeDef(BaseModel):
    DataBars: Optional[DataBarsOptionsTypeDef] = None

class DataLabelTypeTypeDef(BaseModel):
    FieldLabelType: Optional[FieldLabelTypeTypeDef] = None
    DataPathLabelType: Optional[DataPathLabelTypeTypeDef] = None
    RangeEndsLabelType: Optional[RangeEndsLabelTypeTypeDef] = None
    MinimumLabelType: Optional[MinimumLabelTypeTypeDef] = None
    MaximumLabelType: Optional[MaximumLabelTypeTypeDef] = None

class DataPathValueTypeDef(BaseModel):
    FieldId: Optional[str] = None
    FieldValue: Optional[str] = None
    DataPathType: Optional[DataPathTypeTypeDef] = None

class SearchDataSetsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[DataSetSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchDataSourcesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[DataSourceSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchDataSourcesResponseTypeDef(BaseModel):
    DataSourceSummaries: List[DataSourceSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DateTimeDatasetParameterOutputTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultValues: Optional[DateTimeDatasetParameterDefaultValuesOutputTypeDef] = None

class TimeRangeFilterValueOutputTypeDef(BaseModel):
    StaticValue: Optional[datetime] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    Parameter: Optional[str] = None

class TimeRangeFilterValueTypeDef(BaseModel):
    StaticValue: Optional[TimestampTypeDef] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    Parameter: Optional[str] = None

class DecimalDatasetParameterOutputTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[DecimalDatasetParameterDefaultValuesOutputTypeDef] = None

class DecimalDatasetParameterTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[DecimalDatasetParameterDefaultValuesTypeDef] = None

class DescribeAnalysisPermissionsResponseTypeDef(BaseModel):
    AnalysisId: str
    AnalysisArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSetPermissionsResponseTypeDef(BaseModel):
    DataSetArn: str
    DataSetId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSourcePermissionsResponseTypeDef(BaseModel):
    DataSourceArn: str
    DataSourceId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTemplatePermissionsResponseTypeDef(BaseModel):
    TemplateId: str
    TemplateArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThemePermissionsResponseTypeDef(BaseModel):
    ThemeId: str
    ThemeArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTopicPermissionsResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class LinkSharingConfigurationOutputTypeDef(BaseModel):
    Permissions: Optional[List[ResourcePermissionOutputTypeDef]] = None

class UpdateAnalysisPermissionsResponseTypeDef(BaseModel):
    AnalysisArn: str
    AnalysisId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFolderPermissionsResponseTypeDef(BaseModel):
    Status: int
    Arn: str
    FolderId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplatePermissionsResponseTypeDef(BaseModel):
    TemplateId: str
    TemplateArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemePermissionsResponseTypeDef(BaseModel):
    ThemeId: str
    ThemeArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTopicPermissionsResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFolderPermissionsRequestDescribeFolderPermissionsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalysesRequestListAnalysesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardsRequestListDashboardsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetsRequestListDataSetsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFolderMembersRequestListFolderMembersPaginateTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFoldersRequestListFoldersPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef(BaseModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef(BaseModel):
    AwsAccountId: str
    UserName: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngestionsRequestListIngestionsPaginateTypeDef(BaseModel):
    DataSetId: str
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestListNamespacesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoleMembershipsRequestListRoleMembershipsPaginateTypeDef(BaseModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesRequestListTemplatesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThemeVersionsRequestListThemeVersionsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThemesRequestListThemesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Type: Optional[ThemeTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserGroupsRequestListUserGroupsPaginateTypeDef(BaseModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchAnalysesRequestSearchAnalysesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[AnalysisSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchDashboardsRequestSearchDashboardsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[DashboardSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchDataSetsRequestSearchDataSetsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[DataSetSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[DataSourceSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFolderPermissionsResponseTypeDef(BaseModel):
    Status: int
    FolderId: str
    Arn: str
    Permissions: List[ResourcePermissionExtraOutputTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFolderResolvedPermissionsResponseTypeDef(BaseModel):
    Status: int
    FolderId: str
    Arn: str
    Permissions: List[ResourcePermissionExtraOutputTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFolderResponseTypeDef(BaseModel):
    Status: int
    Folder: FolderTypeDef
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIAMPolicyAssignmentResponseTypeDef(BaseModel):
    IAMPolicyAssignment: IAMPolicyAssignmentTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyRegistrationResponseTypeDef(BaseModel):
    AwsAccountId: str
    KeyRegistration: List[RegisteredCustomerManagedKeyTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKeyRegistrationRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    KeyRegistration: Sequence[RegisteredCustomerManagedKeyTypeDef]

class DescribeTopicRefreshResponseTypeDef(BaseModel):
    RefreshDetails: TopicRefreshDetailsTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTopicRefreshScheduleResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    RefreshSchedule: TopicRefreshScheduleOutputTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TopicRefreshScheduleSummaryTypeDef(BaseModel):
    DatasetId: Optional[str] = None
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    RefreshSchedule: Optional[TopicRefreshScheduleOutputTypeDef] = None

class DescribeUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseModel):
    UserList: List[UserTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    UserInvitationUrl: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DisplayFormatOptionsTypeDef(BaseModel):
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
    NegativeFormat: Optional[NegativeFormatTypeDef] = None
    CurrencySymbol: Optional[str] = None

class DonutOptionsTypeDef(BaseModel):
    ArcOptions: Optional[ArcOptionsTypeDef] = None
    DonutCenterOptions: Optional[DonutCenterOptionsTypeDef] = None

class FilterOperationTargetVisualsConfigurationOutputTypeDef(BaseModel):
    SameSheetTargetVisualConfiguration: Optional[       SameSheetTargetVisualConfigurationOutputTypeDef     ] = None

class FilterOperationTargetVisualsConfigurationTypeDef(BaseModel):
    SameSheetTargetVisualConfiguration: Optional[       SameSheetTargetVisualConfigurationTypeDef     ] = None

class SearchFoldersRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[FolderSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchFoldersRequestSearchFoldersPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Filters: Sequence[FolderSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFoldersResponseTypeDef(BaseModel):
    Status: int
    FolderSummaryList: List[FolderSummaryTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchFoldersResponseTypeDef(BaseModel):
    Status: int
    FolderSummaryList: List[FolderSummaryTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FontConfigurationTypeDef(BaseModel):
    FontSize: Optional[FontSizeTypeDef] = None
    FontDecoration: Optional[FontDecorationType] = None
    FontColor: Optional[str] = None
    FontWeight: Optional[FontWeightTypeDef] = None
    FontStyle: Optional[FontStyleType] = None

class TypographyOutputTypeDef(BaseModel):
    FontFamilies: Optional[List[FontTypeDef]] = None

class TypographyTypeDef(BaseModel):
    FontFamilies: Optional[Sequence[FontTypeDef]] = None

class ForecastScenarioOutputTypeDef(BaseModel):
    WhatIfPointScenario: Optional[WhatIfPointScenarioOutputTypeDef] = None
    WhatIfRangeScenario: Optional[WhatIfRangeScenarioOutputTypeDef] = None

class FreeFormLayoutCanvasSizeOptionsTypeDef(BaseModel):
    ScreenCanvasSizeOptions: Optional[FreeFormLayoutScreenCanvasSizeOptionsTypeDef] = None

class SnapshotAnonymousUserTypeDef(BaseModel):
    RowLevelPermissionTags: Optional[Sequence[SessionTagTypeDef]] = None

class GeospatialWindowOptionsTypeDef(BaseModel):
    Bounds: Optional[GeospatialCoordinateBoundsTypeDef] = None
    MapZoomMode: Optional[MapZoomModeType] = None

class GeospatialHeatmapColorScaleOutputTypeDef(BaseModel):
    Colors: Optional[List[GeospatialHeatmapDataColorTypeDef]] = None

class GeospatialHeatmapColorScaleTypeDef(BaseModel):
    Colors: Optional[Sequence[GeospatialHeatmapDataColorTypeDef]] = None

class TableSideBorderOptionsTypeDef(BaseModel):
    InnerVertical: Optional[TableBorderOptionsTypeDef] = None
    InnerHorizontal: Optional[TableBorderOptionsTypeDef] = None
    Left: Optional[TableBorderOptionsTypeDef] = None
    Right: Optional[TableBorderOptionsTypeDef] = None
    Top: Optional[TableBorderOptionsTypeDef] = None
    Bottom: Optional[TableBorderOptionsTypeDef] = None

class GradientColorOutputTypeDef(BaseModel):
    Stops: Optional[List[GradientStopTypeDef]] = None

class GradientColorTypeDef(BaseModel):
    Stops: Optional[Sequence[GradientStopTypeDef]] = None

class GridLayoutCanvasSizeOptionsTypeDef(BaseModel):
    ScreenCanvasSizeOptions: Optional[GridLayoutScreenCanvasSizeOptionsTypeDef] = None

class SearchGroupsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    Filters: Sequence[GroupSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchGroupsRequestSearchGroupsPaginateTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    Filters: Sequence[GroupSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIAMPolicyAssignmentsResponseTypeDef(BaseModel):
    IAMPolicyAssignments: List[IAMPolicyAssignmentSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IncrementalRefreshTypeDef(BaseModel):
    LookbackWindow: LookbackWindowTypeDef

class IngestionTypeDef(BaseModel):
    Arn: str
    IngestionStatus: IngestionStatusType
    CreatedTime: datetime
    IngestionId: Optional[str] = None
    ErrorInfo: Optional[ErrorInfoTypeDef] = None
    RowInfo: Optional[RowInfoTypeDef] = None
    QueueInfo: Optional[QueueInfoTypeDef] = None
    IngestionTimeInSeconds: Optional[int] = None
    IngestionSizeInBytes: Optional[int] = None
    RequestSource: Optional[IngestionRequestSourceType] = None
    RequestType: Optional[IngestionRequestTypeType] = None

class IntegerDatasetParameterOutputTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[IntegerDatasetParameterDefaultValuesOutputTypeDef] = None

class IntegerDatasetParameterTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[IntegerDatasetParameterDefaultValuesTypeDef] = None

class JoinInstructionTypeDef(BaseModel):
    LeftOperand: str
    RightOperand: str
    Type: JoinTypeType
    OnClause: str
    LeftJoinKeyProperties: Optional[JoinKeyPropertiesTypeDef] = None
    RightJoinKeyProperties: Optional[JoinKeyPropertiesTypeDef] = None

class KPIVisualLayoutOptionsTypeDef(BaseModel):
    StandardLayout: Optional[KPIVisualStandardLayoutTypeDef] = None

class LineChartDefaultSeriesSettingsTypeDef(BaseModel):
    AxisBinding: Optional[AxisBindingType] = None
    LineStyleSettings: Optional[LineChartLineStyleSettingsTypeDef] = None
    MarkerStyleSettings: Optional[LineChartMarkerStyleSettingsTypeDef] = None

class LineChartSeriesSettingsTypeDef(BaseModel):
    LineStyleSettings: Optional[LineChartLineStyleSettingsTypeDef] = None
    MarkerStyleSettings: Optional[LineChartMarkerStyleSettingsTypeDef] = None

class LinkSharingConfigurationTypeDef(BaseModel):
    Permissions: Optional[Sequence[ResourcePermissionTypeDef]] = None

class ListFolderMembersResponseTypeDef(BaseModel):
    Status: int
    FolderMemberList: List[MemberIdArnPairTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTemplateVersionsResponseTypeDef(BaseModel):
    TemplateVersionSummaryList: List[TemplateVersionSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTemplatesResponseTypeDef(BaseModel):
    TemplateSummaryList: List[TemplateSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListThemeVersionsResponseTypeDef(BaseModel):
    ThemeVersionSummaryList: List[ThemeVersionSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListThemesResponseTypeDef(BaseModel):
    ThemeSummaryList: List[ThemeSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTopicsResponseTypeDef(BaseModel):
    TopicsSummaries: List[TopicSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VisualSubtitleLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    FormatText: Optional[LongFormatTextTypeDef] = None

class S3ParametersTypeDef(BaseModel):
    ManifestFileLocation: ManifestFileLocationTypeDef
    RoleArn: Optional[str] = None

class TileLayoutStyleTypeDef(BaseModel):
    Gutter: Optional[GutterStyleTypeDef] = None
    Margin: Optional[MarginStyleTypeDef] = None

class NamedEntityDefinitionOutputTypeDef(BaseModel):
    FieldName: Optional[str] = None
    PropertyName: Optional[str] = None
    PropertyRole: Optional[PropertyRoleType] = None
    PropertyUsage: Optional[PropertyUsageType] = None
    Metric: Optional[NamedEntityDefinitionMetricOutputTypeDef] = None

class NamedEntityDefinitionTypeDef(BaseModel):
    FieldName: Optional[str] = None
    PropertyName: Optional[str] = None
    PropertyRole: Optional[PropertyRoleType] = None
    PropertyUsage: Optional[PropertyUsageType] = None
    Metric: Optional[NamedEntityDefinitionMetricTypeDef] = None

class NamespaceInfoV2TypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    CapacityRegion: Optional[str] = None
    CreationStatus: Optional[NamespaceStatusType] = None
    IdentityStore: Optional[Literal["QUICKSIGHT"]] = None
    NamespaceError: Optional[NamespaceErrorTypeDef] = None

class VPCConnectionSummaryTypeDef(BaseModel):
    VPCConnectionId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    Status: Optional[VPCConnectionResourceStatusType] = None
    AvailabilityStatus: Optional[VPCConnectionAvailabilityStatusType] = None
    NetworkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    RoleArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class VPCConnectionTypeDef(BaseModel):
    VPCConnectionId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    Status: Optional[VPCConnectionResourceStatusType] = None
    AvailabilityStatus: Optional[VPCConnectionAvailabilityStatusType] = None
    NetworkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    RoleArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class OverrideDatasetParameterOperationOutputTypeDef(BaseModel):
    ParameterName: str
    NewParameterName: Optional[str] = None
    NewDefaultValues: Optional[NewDefaultValuesOutputTypeDef] = None

class NumericSeparatorConfigurationTypeDef(BaseModel):
    DecimalSeparator: Optional[NumericSeparatorSymbolType] = None
    ThousandsSeparator: Optional[ThousandSeparatorOptionsTypeDef] = None

class NumericalAggregationFunctionTypeDef(BaseModel):
    SimpleNumericalAggregation: Optional[SimpleNumericalAggregationFunctionType] = None
    PercentileAggregation: Optional[PercentileAggregationTypeDef] = None

class ParametersOutputTypeDef(BaseModel):
    StringParameters: Optional[List[StringParameterOutputTypeDef]] = None
    IntegerParameters: Optional[List[IntegerParameterOutputTypeDef]] = None
    DecimalParameters: Optional[List[DecimalParameterOutputTypeDef]] = None
    DateTimeParameters: Optional[List[DateTimeParameterOutputTypeDef]] = None

class VisibleRangeOptionsTypeDef(BaseModel):
    PercentRange: Optional[PercentVisibleRangeTypeDef] = None

class RadarChartSeriesSettingsTypeDef(BaseModel):
    AreaStyleSettings: Optional[RadarChartAreaStyleSettingsTypeDef] = None

class TopicRangeFilterConstantTypeDef(BaseModel):
    ConstantType: Optional[ConstantTypeType] = None
    RangeConstant: Optional[RangeConstantTypeDef] = None

class RedshiftParametersExtraOutputTypeDef(BaseModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersExtraOutputTypeDef] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None

class RedshiftParametersOutputTypeDef(BaseModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersOutputTypeDef] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None

class RedshiftParametersTypeDef(BaseModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersTypeDef] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None

class RefreshFrequencyTypeDef(BaseModel):
    Interval: RefreshIntervalType
    RefreshOnDay: Optional[ScheduleRefreshOnEntityTypeDef] = None
    Timezone: Optional[str] = None
    TimeOfTheDay: Optional[str] = None

class RegisteredUserConsoleFeatureConfigurationsTypeDef(BaseModel):
    StatePersistence: Optional[StatePersistenceConfigurationsTypeDef] = None

class RegisteredUserDashboardFeatureConfigurationsTypeDef(BaseModel):
    StatePersistence: Optional[StatePersistenceConfigurationsTypeDef] = None
    Bookmarks: Optional[BookmarksConfigurationsTypeDef] = None

class RowLevelPermissionTagConfigurationOutputTypeDef(BaseModel):
    TagRules: List[RowLevelPermissionTagRuleTypeDef]
    Status: Optional[StatusType] = None
    TagRuleConfigurations: Optional[List[List[str]]] = None

class RowLevelPermissionTagConfigurationTypeDef(BaseModel):
    TagRules: Sequence[RowLevelPermissionTagRuleTypeDef]
    Status: Optional[StatusType] = None
    TagRuleConfigurations: Optional[Sequence[Sequence[str]]] = None

class SnapshotS3DestinationConfigurationTypeDef(BaseModel):
    BucketConfiguration: S3BucketConfigurationTypeDef

class S3SourceOutputTypeDef(BaseModel):
    DataSourceArn: str
    InputColumns: List[InputColumnTypeDef]
    UploadSettings: Optional[UploadSettingsTypeDef] = None

class S3SourceTypeDef(BaseModel):
    DataSourceArn: str
    InputColumns: Sequence[InputColumnTypeDef]
    UploadSettings: Optional[UploadSettingsTypeDef] = None

class SectionBasedLayoutPaperCanvasSizeOptionsTypeDef(BaseModel):
    PaperSize: Optional[PaperSizeType] = None
    PaperOrientation: Optional[PaperOrientationType] = None
    PaperMargin: Optional[SpacingTypeDef] = None

class SectionStyleTypeDef(BaseModel):
    Height: Optional[str] = None
    Padding: Optional[SpacingTypeDef] = None

class SelectedSheetsFilterScopeConfigurationOutputTypeDef(BaseModel):
    SheetVisualScopingConfigurations: Optional[       List[SheetVisualScopingConfigurationOutputTypeDef]     ] = None

class SelectedSheetsFilterScopeConfigurationTypeDef(BaseModel):
    SheetVisualScopingConfigurations: Optional[       Sequence[SheetVisualScopingConfigurationTypeDef]     ] = None

class SheetElementRenderingRuleTypeDef(BaseModel):
    Expression: str
    ConfigurationOverrides: SheetElementConfigurationOverridesTypeDef

class VisualTitleLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    FormatText: Optional[ShortFormatTextTypeDef] = None

class SingleAxisOptionsTypeDef(BaseModel):
    YAxisOptions: Optional[YAxisOptionsTypeDef] = None

class SnapshotUserConfigurationRedactedTypeDef(BaseModel):
    AnonymousUsers: Optional[List[SnapshotAnonymousUserRedactedTypeDef]] = None

class SnapshotFileOutputTypeDef(BaseModel):
    SheetSelections: List[SnapshotFileSheetSelectionOutputTypeDef]
    FormatType: SnapshotFileFormatTypeType

class SnapshotFileTypeDef(BaseModel):
    SheetSelections: Sequence[SnapshotFileSheetSelectionTypeDef]
    FormatType: SnapshotFileFormatTypeType

class StringDatasetParameterOutputTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[StringDatasetParameterDefaultValuesOutputTypeDef] = None

class StringDatasetParameterTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[StringDatasetParameterDefaultValuesTypeDef] = None

class UpdateKeyRegistrationResponseTypeDef(BaseModel):
    FailedKeyRegistration: List[FailedKeyRegistrationEntryTypeDef]
    SuccessfulKeyRegistration: List[SuccessfulKeyRegistrationEntryTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TableFieldImageConfigurationTypeDef(BaseModel):
    SizingOptions: Optional[TableCellImageSizingConfigurationTypeDef] = None

class TopicNumericEqualityFilterTypeDef(BaseModel):
    Constant: Optional[TopicSingularFilterConstantTypeDef] = None
    Aggregation: Optional[NamedFilterAggTypeType] = None

class TopicRelativeDateFilterTypeDef(BaseModel):
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    RelativeDateFilterFunction: Optional[TopicRelativeDateFilterFunctionType] = None
    Constant: Optional[TopicSingularFilterConstantTypeDef] = None

class TotalAggregationOptionTypeDef(BaseModel):
    FieldId: str
    TotalAggregationFunction: TotalAggregationFunctionTypeDef

class WaterfallChartColorConfigurationTypeDef(BaseModel):
    GroupColorConfiguration: Optional[WaterfallChartGroupColorConfigurationTypeDef] = None

class CascadingControlConfigurationOutputTypeDef(BaseModel):
    SourceControls: Optional[List[CascadingControlSourceTypeDef]] = None

class CascadingControlConfigurationTypeDef(BaseModel):
    SourceControls: Optional[Sequence[CascadingControlSourceTypeDef]] = None

class DateTimeDefaultValuesOutputTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[datetime]] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None

class DateTimeDefaultValuesTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[TimestampTypeDef]] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None

class DecimalDefaultValuesOutputTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[float]] = None

class DecimalDefaultValuesTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[float]] = None

class IntegerDefaultValuesOutputTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[int]] = None

class IntegerDefaultValuesTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[int]] = None

class StringDefaultValuesOutputTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[str]] = None

class StringDefaultValuesTypeDef(BaseModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[str]] = None

class DrillDownFilterOutputTypeDef(BaseModel):
    NumericEqualityFilter: Optional[NumericEqualityDrillDownFilterTypeDef] = None
    CategoryFilter: Optional[CategoryDrillDownFilterOutputTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeDrillDownFilterOutputTypeDef] = None

class AnalysisTypeDef(BaseModel):
    AnalysisId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ResourceStatusType] = None
    Errors: Optional[List[AnalysisErrorTypeDef]] = None
    DataSetArns: Optional[List[str]] = None
    ThemeArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    Sheets: Optional[List[SheetTypeDef]] = None

class DashboardVersionTypeDef(BaseModel):
    CreatedTime: Optional[datetime] = None
    Errors: Optional[List[DashboardErrorTypeDef]] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    Arn: Optional[str] = None
    SourceEntityArn: Optional[str] = None
    DataSetArns: Optional[List[str]] = None
    Description: Optional[str] = None
    ThemeArn: Optional[str] = None
    Sheets: Optional[List[SheetTypeDef]] = None

class AnalysisSourceEntityTypeDef(BaseModel):
    SourceTemplate: Optional[AnalysisSourceTemplateTypeDef] = None

class DashboardSourceEntityTypeDef(BaseModel):
    SourceTemplate: Optional[DashboardSourceTemplateTypeDef] = None

class TemplateSourceEntityTypeDef(BaseModel):
    SourceAnalysis: Optional[TemplateSourceAnalysisTypeDef] = None
    SourceTemplate: Optional[TemplateSourceTemplateTypeDef] = None

class AnonymousUserEmbeddingExperienceConfigurationTypeDef(BaseModel):
    Dashboard: Optional[AnonymousUserDashboardEmbeddingConfigurationTypeDef] = None
    DashboardVisual: Optional[AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef] = None
    QSearchBar: Optional[AnonymousUserQSearchBarEmbeddingConfigurationTypeDef] = None
    GenerativeQnA: Optional[AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef] = None

class DescribeAssetBundleExportJobResponseTypeDef(BaseModel):
    JobStatus: AssetBundleExportJobStatusType
    DownloadUrl: str
    Errors: List[AssetBundleExportJobErrorTypeDef]
    Arn: str
    CreatedTime: datetime
    AssetBundleExportJobId: str
    AwsAccountId: str
    ResourceArns: List[str]
    IncludeAllDependencies: bool
    ExportFormat: AssetBundleExportFormatType
    CloudFormationOverridePropertyConfiguration: AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef
    RequestId: str
    Status: int
    IncludePermissions: bool
    IncludeTags: bool
    ValidationStrategy: AssetBundleExportJobValidationStrategyTypeDef
    Warnings: List[AssetBundleExportJobWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssetBundleExportJobRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssetBundleExportJobId: str
    ResourceArns: Sequence[str]
    ExportFormat: AssetBundleExportFormatType
    IncludeAllDependencies: Optional[bool] = None
    CloudFormationOverridePropertyConfiguration: Optional[       AssetBundleCloudFormationOverridePropertyConfigurationTypeDef     ] = None
    IncludePermissions: Optional[bool] = None
    IncludeTags: Optional[bool] = None
    ValidationStrategy: Optional[AssetBundleExportJobValidationStrategyTypeDef] = None

class AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef(BaseModel):
    DashboardIds: List[str]
    Permissions: Optional[AssetBundleResourcePermissionsOutputTypeDef] = None
    LinkSharingConfiguration: Optional[       AssetBundleResourceLinkSharingConfigurationOutputTypeDef     ] = None

class AssetBundleImportJobDashboardOverridePermissionsTypeDef(BaseModel):
    DashboardIds: Sequence[str]
    Permissions: Optional[AssetBundleResourcePermissionsTypeDef] = None
    LinkSharingConfiguration: Optional[AssetBundleResourceLinkSharingConfigurationTypeDef] = None

class AssetBundleImportJobOverrideTagsOutputTypeDef(BaseModel):
    VPCConnections: Optional[       List[AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef]     ] = None
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideTagsOutputTypeDef]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideTagsOutputTypeDef]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideTagsOutputTypeDef]] = None

class AssetBundleImportJobOverrideTagsTypeDef(BaseModel):
    VPCConnections: Optional[       Sequence[AssetBundleImportJobVPCConnectionOverrideTagsTypeDef]     ] = None
    DataSources: Optional[Sequence[AssetBundleImportJobDataSourceOverrideTagsTypeDef]] = None
    DataSets: Optional[Sequence[AssetBundleImportJobDataSetOverrideTagsTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleImportJobThemeOverrideTagsTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleImportJobAnalysisOverrideTagsTypeDef]] = None
    Dashboards: Optional[Sequence[AssetBundleImportJobDashboardOverrideTagsTypeDef]] = None

class CustomValuesConfigurationTypeDef(BaseModel):
    CustomValues: CustomParameterValuesTypeDef
    IncludeNullValue: Optional[bool] = None

class DateTimeDatasetParameterTypeDef(BaseModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultValues: Optional[DateTimeDatasetParameterDefaultValuesTypeDef] = None

class ParametersTypeDef(BaseModel):
    StringParameters: Optional[Sequence[StringParameterTypeDef]] = None
    IntegerParameters: Optional[Sequence[IntegerParameterTypeDef]] = None
    DecimalParameters: Optional[Sequence[DecimalParameterTypeDef]] = None
    DateTimeParameters: Optional[Sequence[DateTimeParameterTypeDef]] = None

class OverrideDatasetParameterOperationTypeDef(BaseModel):
    ParameterName: str
    NewParameterName: Optional[str] = None
    NewDefaultValues: Optional[NewDefaultValuesTypeDef] = None

class DrillDownFilterTypeDef(BaseModel):
    NumericEqualityFilter: Optional[NumericEqualityDrillDownFilterTypeDef] = None
    CategoryFilter: Optional[CategoryDrillDownFilterTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeDrillDownFilterTypeDef] = None

class CreateTopicRefreshScheduleRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    DatasetArn: str
    RefreshSchedule: TopicRefreshScheduleTypeDef
    DatasetName: Optional[str] = None

class UpdateTopicRefreshScheduleRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str
    RefreshSchedule: TopicRefreshScheduleTypeDef

class ForecastScenarioTypeDef(BaseModel):
    WhatIfPointScenario: Optional[WhatIfPointScenarioTypeDef] = None
    WhatIfRangeScenario: Optional[WhatIfRangeScenarioTypeDef] = None

class NumericAxisOptionsOutputTypeDef(BaseModel):
    Scale: Optional[AxisScaleTypeDef] = None
    Range: Optional[AxisDisplayRangeOutputTypeDef] = None

class NumericAxisOptionsTypeDef(BaseModel):
    Scale: Optional[AxisScaleTypeDef] = None
    Range: Optional[AxisDisplayRangeTypeDef] = None

class ClusterMarkerConfigurationTypeDef(BaseModel):
    ClusterMarker: Optional[ClusterMarkerTypeDef] = None

class TopicCategoryFilterOutputTypeDef(BaseModel):
    CategoryFilterFunction: Optional[CategoryFilterFunctionType] = None
    CategoryFilterType: Optional[CategoryFilterTypeType] = None
    Constant: Optional[TopicCategoryFilterConstantOutputTypeDef] = None
    Inverse: Optional[bool] = None

class TopicCategoryFilterTypeDef(BaseModel):
    CategoryFilterFunction: Optional[CategoryFilterFunctionType] = None
    CategoryFilterType: Optional[CategoryFilterTypeType] = None
    Constant: Optional[TopicCategoryFilterConstantTypeDef] = None
    Inverse: Optional[bool] = None

class TagColumnOperationOutputTypeDef(BaseModel):
    ColumnName: str
    Tags: List[ColumnTagTypeDef]

class TagColumnOperationTypeDef(BaseModel):
    ColumnName: str
    Tags: Sequence[ColumnTagTypeDef]

class DataSetConfigurationOutputTypeDef(BaseModel):
    Placeholder: Optional[str] = None
    DataSetSchema: Optional[DataSetSchemaOutputTypeDef] = None
    ColumnGroupSchemaList: Optional[List[ColumnGroupSchemaOutputTypeDef]] = None

class DataSetConfigurationTypeDef(BaseModel):
    Placeholder: Optional[str] = None
    DataSetSchema: Optional[DataSetSchemaTypeDef] = None
    ColumnGroupSchemaList: Optional[Sequence[ColumnGroupSchemaTypeDef]] = None

class ConditionalFormattingIconTypeDef(BaseModel):
    IconSet: Optional[ConditionalFormattingIconSetTypeDef] = None
    CustomCondition: Optional[ConditionalFormattingCustomIconConditionTypeDef] = None

class ListDataSetsResponseTypeDef(BaseModel):
    DataSetSummaries: List[DataSetSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchDataSetsResponseTypeDef(BaseModel):
    DataSetSummaries: List[DataSetSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DestinationParameterValueConfigurationOutputTypeDef(BaseModel):
    CustomValuesConfiguration: Optional[CustomValuesConfigurationOutputTypeDef] = None
    SelectAllValueOptions: Optional[Literal["ALL_VALUES"]] = None
    SourceParameterName: Optional[str] = None
    SourceField: Optional[str] = None
    SourceColumn: Optional[ColumnIdentifierTypeDef] = None

class CustomContentConfigurationTypeDef(BaseModel):
    ContentUrl: Optional[str] = None
    ContentType: Optional[CustomContentTypeType] = None
    ImageScaling: Optional[CustomContentImageScalingConfigurationType] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class DashboardPublishOptionsTypeDef(BaseModel):
    AdHocFilteringOption: Optional[AdHocFilteringOptionTypeDef] = None
    ExportToCSVOption: Optional[ExportToCSVOptionTypeDef] = None
    SheetControlsOption: Optional[SheetControlsOptionTypeDef] = None
    VisualPublishOptions: Optional[DashboardVisualPublishOptionsTypeDef] = None
    SheetLayoutElementMaximizationOption: Optional[       SheetLayoutElementMaximizationOptionTypeDef     ] = None
    VisualMenuOption: Optional[VisualMenuOptionTypeDef] = None
    VisualAxisSortOption: Optional[VisualAxisSortOptionTypeDef] = None
    ExportWithHiddenFieldsOption: Optional[ExportWithHiddenFieldsOptionTypeDef] = None
    DataPointDrillUpDownOption: Optional[DataPointDrillUpDownOptionTypeDef] = None
    DataPointMenuLabelOption: Optional[DataPointMenuLabelOptionTypeDef] = None
    DataPointTooltipOption: Optional[DataPointTooltipOptionTypeDef] = None

class DataPathColorTypeDef(BaseModel):
    Element: DataPathValueTypeDef
    Color: str
    TimeGranularity: Optional[TimeGranularityType] = None

class DataPathSortOutputTypeDef(BaseModel):
    Direction: SortDirectionType
    SortPaths: List[DataPathValueTypeDef]

class DataPathSortTypeDef(BaseModel):
    Direction: SortDirectionType
    SortPaths: Sequence[DataPathValueTypeDef]

class PivotTableDataPathOptionOutputTypeDef(BaseModel):
    DataPathList: List[DataPathValueTypeDef]
    Width: Optional[str] = None

class PivotTableDataPathOptionTypeDef(BaseModel):
    DataPathList: Sequence[DataPathValueTypeDef]
    Width: Optional[str] = None

class PivotTableFieldCollapseStateTargetOutputTypeDef(BaseModel):
    FieldId: Optional[str] = None
    FieldDataPathValues: Optional[List[DataPathValueTypeDef]] = None

class PivotTableFieldCollapseStateTargetTypeDef(BaseModel):
    FieldId: Optional[str] = None
    FieldDataPathValues: Optional[Sequence[DataPathValueTypeDef]] = None

class DescribeDashboardPermissionsResponseTypeDef(BaseModel):
    DashboardId: str
    DashboardArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    LinkSharingConfiguration: LinkSharingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardPermissionsResponseTypeDef(BaseModel):
    DashboardArn: str
    DashboardId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    LinkSharingConfiguration: LinkSharingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicRefreshSchedulesResponseTypeDef(BaseModel):
    TopicId: str
    TopicArn: str
    RefreshSchedules: List[TopicRefreshScheduleSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DefaultFormattingTypeDef(BaseModel):
    DisplayFormat: Optional[DisplayFormatType] = None
    DisplayFormatOptions: Optional[DisplayFormatOptionsTypeDef] = None

class CustomActionFilterOperationOutputTypeDef(BaseModel):
    SelectedFieldsConfiguration: FilterOperationSelectedFieldsConfigurationOutputTypeDef
    TargetVisualsConfiguration: FilterOperationTargetVisualsConfigurationOutputTypeDef

class CustomActionFilterOperationTypeDef(BaseModel):
    SelectedFieldsConfiguration: FilterOperationSelectedFieldsConfigurationTypeDef
    TargetVisualsConfiguration: FilterOperationTargetVisualsConfigurationTypeDef

class AxisLabelOptionsTypeDef(BaseModel):
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    CustomLabel: Optional[str] = None
    ApplyTo: Optional[AxisLabelReferenceOptionsTypeDef] = None

class DataLabelOptionsOutputTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    DataLabelTypes: Optional[List[DataLabelTypeTypeDef]] = None
    Position: Optional[DataLabelPositionType] = None
    LabelContent: Optional[DataLabelContentType] = None
    LabelFontConfiguration: Optional[FontConfigurationTypeDef] = None
    LabelColor: Optional[str] = None
    Overlap: Optional[DataLabelOverlapType] = None
    TotalsVisibility: Optional[VisibilityType] = None

class DataLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    DataLabelTypes: Optional[Sequence[DataLabelTypeTypeDef]] = None
    Position: Optional[DataLabelPositionType] = None
    LabelContent: Optional[DataLabelContentType] = None
    LabelFontConfiguration: Optional[FontConfigurationTypeDef] = None
    LabelColor: Optional[str] = None
    Overlap: Optional[DataLabelOverlapType] = None
    TotalsVisibility: Optional[VisibilityType] = None

class FunnelChartDataLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    Position: Optional[DataLabelPositionType] = None
    LabelFontConfiguration: Optional[FontConfigurationTypeDef] = None
    LabelColor: Optional[str] = None
    MeasureDataLabelStyle: Optional[FunnelChartMeasureDataLabelStyleType] = None

class LabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    CustomLabel: Optional[str] = None

class PanelTitleOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    HorizontalTextAlignment: Optional[HorizontalTextAlignmentType] = None

class TableFieldCustomTextContentTypeDef(BaseModel):
    FontConfiguration: FontConfigurationTypeDef
    Value: Optional[str] = None

class ForecastConfigurationOutputTypeDef(BaseModel):
    ForecastProperties: Optional[TimeBasedForecastPropertiesTypeDef] = None
    Scenario: Optional[ForecastScenarioOutputTypeDef] = None

class DefaultFreeFormLayoutConfigurationTypeDef(BaseModel):
    CanvasSizeOptions: FreeFormLayoutCanvasSizeOptionsTypeDef

class SnapshotUserConfigurationTypeDef(BaseModel):
    AnonymousUsers: Optional[Sequence[SnapshotAnonymousUserTypeDef]] = None

class GeospatialHeatmapConfigurationOutputTypeDef(BaseModel):
    HeatmapColor: Optional[GeospatialHeatmapColorScaleOutputTypeDef] = None

class GeospatialHeatmapConfigurationTypeDef(BaseModel):
    HeatmapColor: Optional[GeospatialHeatmapColorScaleTypeDef] = None

class GlobalTableBorderOptionsTypeDef(BaseModel):
    UniformBorder: Optional[TableBorderOptionsTypeDef] = None
    SideSpecificBorder: Optional[TableSideBorderOptionsTypeDef] = None

class ConditionalFormattingGradientColorOutputTypeDef(BaseModel):
    Expression: str
    Color: GradientColorOutputTypeDef

class ConditionalFormattingGradientColorTypeDef(BaseModel):
    Expression: str
    Color: GradientColorTypeDef

class DefaultGridLayoutConfigurationTypeDef(BaseModel):
    CanvasSizeOptions: GridLayoutCanvasSizeOptionsTypeDef

class GridLayoutConfigurationOutputTypeDef(BaseModel):
    Elements: List[GridLayoutElementTypeDef]
    CanvasSizeOptions: Optional[GridLayoutCanvasSizeOptionsTypeDef] = None

class GridLayoutConfigurationTypeDef(BaseModel):
    Elements: Sequence[GridLayoutElementTypeDef]
    CanvasSizeOptions: Optional[GridLayoutCanvasSizeOptionsTypeDef] = None

class RefreshConfigurationTypeDef(BaseModel):
    IncrementalRefresh: IncrementalRefreshTypeDef

class DescribeIngestionResponseTypeDef(BaseModel):
    Ingestion: IngestionTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListIngestionsResponseTypeDef(BaseModel):
    Ingestions: List[IngestionTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LogicalTableSourceTypeDef(BaseModel):
    JoinInstruction: Optional[JoinInstructionTypeDef] = None
    PhysicalTableId: Optional[str] = None
    DataSetArn: Optional[str] = None

class DataFieldSeriesItemTypeDef(BaseModel):
    FieldId: str
    AxisBinding: AxisBindingType
    FieldValue: Optional[str] = None
    Settings: Optional[LineChartSeriesSettingsTypeDef] = None

class FieldSeriesItemTypeDef(BaseModel):
    FieldId: str
    AxisBinding: AxisBindingType
    Settings: Optional[LineChartSeriesSettingsTypeDef] = None

class CreateFolderRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    ParentFolderArn: Optional[str] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SharingModel: Optional[SharingModelType] = None

class UpdateAnalysisPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateDashboardPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    GrantLinkPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokeLinkPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateDataSetPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateDataSourcePermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSourceId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateFolderPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    FolderId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateTemplatePermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateThemePermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateTopicPermissionsRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class SheetStyleTypeDef(BaseModel):
    Tile: Optional[TileStyleTypeDef] = None
    TileLayout: Optional[TileLayoutStyleTypeDef] = None

class TopicNamedEntityOutputTypeDef(BaseModel):
    EntityName: str
    EntityDescription: Optional[str] = None
    EntitySynonyms: Optional[List[str]] = None
    SemanticEntityType: Optional[SemanticEntityTypeOutputTypeDef] = None
    Definition: Optional[List[NamedEntityDefinitionOutputTypeDef]] = None

class TopicNamedEntityTypeDef(BaseModel):
    EntityName: str
    EntityDescription: Optional[str] = None
    EntitySynonyms: Optional[Sequence[str]] = None
    SemanticEntityType: Optional[SemanticEntityTypeTypeDef] = None
    Definition: Optional[Sequence[NamedEntityDefinitionTypeDef]] = None

class DescribeNamespaceResponseTypeDef(BaseModel):
    Namespace: NamespaceInfoV2TypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListNamespacesResponseTypeDef(BaseModel):
    Namespaces: List[NamespaceInfoV2TypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVPCConnectionsResponseTypeDef(BaseModel):
    VPCConnectionSummaries: List[VPCConnectionSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVPCConnectionResponseTypeDef(BaseModel):
    VPCConnection: VPCConnectionTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CurrencyDisplayFormatConfigurationTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfigurationTypeDef] = None
    Symbol: Optional[str] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfigurationTypeDef] = None
    NumberScale: Optional[NumberScaleType] = None
    NegativeValueConfiguration: Optional[NegativeValueConfigurationTypeDef] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None

class NumberDisplayFormatConfigurationTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfigurationTypeDef] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfigurationTypeDef] = None
    NumberScale: Optional[NumberScaleType] = None
    NegativeValueConfiguration: Optional[NegativeValueConfigurationTypeDef] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None

class PercentageDisplayFormatConfigurationTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfigurationTypeDef] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfigurationTypeDef] = None
    NegativeValueConfiguration: Optional[NegativeValueConfigurationTypeDef] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None

class AggregationFunctionTypeDef(BaseModel):
    NumericalAggregationFunction: Optional[NumericalAggregationFunctionTypeDef] = None
    CategoricalAggregationFunction: Optional[CategoricalAggregationFunctionType] = None
    DateAggregationFunction: Optional[DateAggregationFunctionType] = None
    AttributeAggregationFunction: Optional[AttributeAggregationFunctionTypeDef] = None

class ScrollBarOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    VisibleRange: Optional[VisibleRangeOptionsTypeDef] = None

class TopicDateRangeFilterTypeDef(BaseModel):
    Inclusive: Optional[bool] = None
    Constant: Optional[TopicRangeFilterConstantTypeDef] = None

class TopicNumericRangeFilterTypeDef(BaseModel):
    Inclusive: Optional[bool] = None
    Constant: Optional[TopicRangeFilterConstantTypeDef] = None
    Aggregation: Optional[NamedFilterAggTypeType] = None

class DataSourceParametersExtraOutputTypeDef(BaseModel):
    AmazonElasticsearchParameters: Optional[AmazonElasticsearchParametersTypeDef] = None
    AthenaParameters: Optional[AthenaParametersTypeDef] = None
    AuroraParameters: Optional[AuroraParametersTypeDef] = None
    AuroraPostgreSqlParameters: Optional[AuroraPostgreSqlParametersTypeDef] = None
    AwsIotAnalyticsParameters: Optional[AwsIotAnalyticsParametersTypeDef] = None
    JiraParameters: Optional[JiraParametersTypeDef] = None
    MariaDbParameters: Optional[MariaDbParametersTypeDef] = None
    MySqlParameters: Optional[MySqlParametersTypeDef] = None
    OracleParameters: Optional[OracleParametersTypeDef] = None
    PostgreSqlParameters: Optional[PostgreSqlParametersTypeDef] = None
    PrestoParameters: Optional[PrestoParametersTypeDef] = None
    RdsParameters: Optional[RdsParametersTypeDef] = None
    RedshiftParameters: Optional[RedshiftParametersExtraOutputTypeDef] = None
    S3Parameters: Optional[S3ParametersTypeDef] = None
    ServiceNowParameters: Optional[ServiceNowParametersTypeDef] = None
    SnowflakeParameters: Optional[SnowflakeParametersTypeDef] = None
    SparkParameters: Optional[SparkParametersTypeDef] = None
    SqlServerParameters: Optional[SqlServerParametersTypeDef] = None
    TeradataParameters: Optional[TeradataParametersTypeDef] = None
    TwitterParameters: Optional[TwitterParametersTypeDef] = None
    AmazonOpenSearchParameters: Optional[AmazonOpenSearchParametersTypeDef] = None
    ExasolParameters: Optional[ExasolParametersTypeDef] = None
    DatabricksParameters: Optional[DatabricksParametersTypeDef] = None
    StarburstParameters: Optional[StarburstParametersTypeDef] = None
    TrinoParameters: Optional[TrinoParametersTypeDef] = None
    BigQueryParameters: Optional[BigQueryParametersTypeDef] = None

class DataSourceParametersOutputTypeDef(BaseModel):
    AmazonElasticsearchParameters: Optional[AmazonElasticsearchParametersTypeDef] = None
    AthenaParameters: Optional[AthenaParametersTypeDef] = None
    AuroraParameters: Optional[AuroraParametersTypeDef] = None
    AuroraPostgreSqlParameters: Optional[AuroraPostgreSqlParametersTypeDef] = None
    AwsIotAnalyticsParameters: Optional[AwsIotAnalyticsParametersTypeDef] = None
    JiraParameters: Optional[JiraParametersTypeDef] = None
    MariaDbParameters: Optional[MariaDbParametersTypeDef] = None
    MySqlParameters: Optional[MySqlParametersTypeDef] = None
    OracleParameters: Optional[OracleParametersTypeDef] = None
    PostgreSqlParameters: Optional[PostgreSqlParametersTypeDef] = None
    PrestoParameters: Optional[PrestoParametersTypeDef] = None
    RdsParameters: Optional[RdsParametersTypeDef] = None
    RedshiftParameters: Optional[RedshiftParametersOutputTypeDef] = None
    S3Parameters: Optional[S3ParametersTypeDef] = None
    ServiceNowParameters: Optional[ServiceNowParametersTypeDef] = None
    SnowflakeParameters: Optional[SnowflakeParametersTypeDef] = None
    SparkParameters: Optional[SparkParametersTypeDef] = None
    SqlServerParameters: Optional[SqlServerParametersTypeDef] = None
    TeradataParameters: Optional[TeradataParametersTypeDef] = None
    TwitterParameters: Optional[TwitterParametersTypeDef] = None
    AmazonOpenSearchParameters: Optional[AmazonOpenSearchParametersTypeDef] = None
    ExasolParameters: Optional[ExasolParametersTypeDef] = None
    DatabricksParameters: Optional[DatabricksParametersTypeDef] = None
    StarburstParameters: Optional[StarburstParametersTypeDef] = None
    TrinoParameters: Optional[TrinoParametersTypeDef] = None
    BigQueryParameters: Optional[BigQueryParametersTypeDef] = None

class DataSourceParametersTypeDef(BaseModel):
    AmazonElasticsearchParameters: Optional[AmazonElasticsearchParametersTypeDef] = None
    AthenaParameters: Optional[AthenaParametersTypeDef] = None
    AuroraParameters: Optional[AuroraParametersTypeDef] = None
    AuroraPostgreSqlParameters: Optional[AuroraPostgreSqlParametersTypeDef] = None
    AwsIotAnalyticsParameters: Optional[AwsIotAnalyticsParametersTypeDef] = None
    JiraParameters: Optional[JiraParametersTypeDef] = None
    MariaDbParameters: Optional[MariaDbParametersTypeDef] = None
    MySqlParameters: Optional[MySqlParametersTypeDef] = None
    OracleParameters: Optional[OracleParametersTypeDef] = None
    PostgreSqlParameters: Optional[PostgreSqlParametersTypeDef] = None
    PrestoParameters: Optional[PrestoParametersTypeDef] = None
    RdsParameters: Optional[RdsParametersTypeDef] = None
    RedshiftParameters: Optional[RedshiftParametersTypeDef] = None
    S3Parameters: Optional[S3ParametersTypeDef] = None
    ServiceNowParameters: Optional[ServiceNowParametersTypeDef] = None
    SnowflakeParameters: Optional[SnowflakeParametersTypeDef] = None
    SparkParameters: Optional[SparkParametersTypeDef] = None
    SqlServerParameters: Optional[SqlServerParametersTypeDef] = None
    TeradataParameters: Optional[TeradataParametersTypeDef] = None
    TwitterParameters: Optional[TwitterParametersTypeDef] = None
    AmazonOpenSearchParameters: Optional[AmazonOpenSearchParametersTypeDef] = None
    ExasolParameters: Optional[ExasolParametersTypeDef] = None
    DatabricksParameters: Optional[DatabricksParametersTypeDef] = None
    StarburstParameters: Optional[StarburstParametersTypeDef] = None
    TrinoParameters: Optional[TrinoParametersTypeDef] = None
    BigQueryParameters: Optional[BigQueryParametersTypeDef] = None

class RefreshScheduleOutputTypeDef(BaseModel):
    ScheduleId: str
    ScheduleFrequency: RefreshFrequencyTypeDef
    RefreshType: IngestionTypeType
    StartAfterDateTime: Optional[datetime] = None
    Arn: Optional[str] = None

class RefreshScheduleTypeDef(BaseModel):
    ScheduleId: str
    ScheduleFrequency: RefreshFrequencyTypeDef
    RefreshType: IngestionTypeType
    StartAfterDateTime: Optional[TimestampTypeDef] = None
    Arn: Optional[str] = None

class RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef(BaseModel):
    InitialPath: Optional[str] = None
    FeatureConfigurations: Optional[RegisteredUserConsoleFeatureConfigurationsTypeDef] = None

class RegisteredUserDashboardEmbeddingConfigurationTypeDef(BaseModel):
    InitialDashboardId: str
    FeatureConfigurations: Optional[RegisteredUserDashboardFeatureConfigurationsTypeDef] = None

class SnapshotDestinationConfigurationOutputTypeDef(BaseModel):
    S3Destinations: Optional[List[SnapshotS3DestinationConfigurationTypeDef]] = None

class SnapshotDestinationConfigurationTypeDef(BaseModel):
    S3Destinations: Optional[Sequence[SnapshotS3DestinationConfigurationTypeDef]] = None

class SnapshotJobS3ResultTypeDef(BaseModel):
    S3DestinationConfiguration: Optional[SnapshotS3DestinationConfigurationTypeDef] = None
    S3Uri: Optional[str] = None
    ErrorInfo: Optional[List[SnapshotJobResultErrorInfoTypeDef]] = None

class PhysicalTableOutputTypeDef(BaseModel):
    RelationalTable: Optional[RelationalTableOutputTypeDef] = None
    CustomSql: Optional[CustomSqlOutputTypeDef] = None
    S3Source: Optional[S3SourceOutputTypeDef] = None

class PhysicalTableTypeDef(BaseModel):
    RelationalTable: Optional[RelationalTableTypeDef] = None
    CustomSql: Optional[CustomSqlTypeDef] = None
    S3Source: Optional[S3SourceTypeDef] = None

class SectionBasedLayoutCanvasSizeOptionsTypeDef(BaseModel):
    PaperCanvasSizeOptions: Optional[SectionBasedLayoutPaperCanvasSizeOptionsTypeDef] = None

class FilterScopeConfigurationOutputTypeDef(BaseModel):
    SelectedSheets: Optional[SelectedSheetsFilterScopeConfigurationOutputTypeDef] = None
    AllSheets: Optional[Dict[str, Any]] = None

class FilterScopeConfigurationTypeDef(BaseModel):
    SelectedSheets: Optional[SelectedSheetsFilterScopeConfigurationTypeDef] = None
    AllSheets: Optional[Mapping[str, Any]] = None

class FreeFormLayoutElementOutputTypeDef(BaseModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    XAxisLocation: str
    YAxisLocation: str
    Width: str
    Height: str
    Visibility: Optional[VisibilityType] = None
    RenderingRules: Optional[List[SheetElementRenderingRuleTypeDef]] = None
    BorderStyle: Optional[FreeFormLayoutElementBorderStyleTypeDef] = None
    SelectedBorderStyle: Optional[FreeFormLayoutElementBorderStyleTypeDef] = None
    BackgroundStyle: Optional[FreeFormLayoutElementBackgroundStyleTypeDef] = None
    LoadingAnimation: Optional[LoadingAnimationTypeDef] = None

class FreeFormLayoutElementTypeDef(BaseModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    XAxisLocation: str
    YAxisLocation: str
    Width: str
    Height: str
    Visibility: Optional[VisibilityType] = None
    RenderingRules: Optional[Sequence[SheetElementRenderingRuleTypeDef]] = None
    BorderStyle: Optional[FreeFormLayoutElementBorderStyleTypeDef] = None
    SelectedBorderStyle: Optional[FreeFormLayoutElementBorderStyleTypeDef] = None
    BackgroundStyle: Optional[FreeFormLayoutElementBackgroundStyleTypeDef] = None
    LoadingAnimation: Optional[LoadingAnimationTypeDef] = None

class SnapshotFileGroupOutputTypeDef(BaseModel):
    Files: Optional[List[SnapshotFileOutputTypeDef]] = None

class SnapshotFileGroupTypeDef(BaseModel):
    Files: Optional[Sequence[SnapshotFileTypeDef]] = None

class DatasetParameterOutputTypeDef(BaseModel):
    StringDatasetParameter: Optional[StringDatasetParameterOutputTypeDef] = None
    DecimalDatasetParameter: Optional[DecimalDatasetParameterOutputTypeDef] = None
    IntegerDatasetParameter: Optional[IntegerDatasetParameterOutputTypeDef] = None
    DateTimeDatasetParameter: Optional[DateTimeDatasetParameterOutputTypeDef] = None

class FilterCrossSheetControlOutputTypeDef(BaseModel):
    FilterControlId: str
    SourceFilterId: str
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class FilterCrossSheetControlTypeDef(BaseModel):
    FilterControlId: str
    SourceFilterId: str
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class DateTimeParameterDeclarationOutputTypeDef(BaseModel):
    Name: str
    DefaultValues: Optional[DateTimeDefaultValuesOutputTypeDef] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ValueWhenUnset: Optional[DateTimeValueWhenUnsetConfigurationOutputTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class DateTimeParameterDeclarationTypeDef(BaseModel):
    Name: str
    DefaultValues: Optional[DateTimeDefaultValuesTypeDef] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ValueWhenUnset: Optional[DateTimeValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class DecimalParameterDeclarationOutputTypeDef(BaseModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[DecimalDefaultValuesOutputTypeDef] = None
    ValueWhenUnset: Optional[DecimalValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class DecimalParameterDeclarationTypeDef(BaseModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[DecimalDefaultValuesTypeDef] = None
    ValueWhenUnset: Optional[DecimalValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class IntegerParameterDeclarationOutputTypeDef(BaseModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[IntegerDefaultValuesOutputTypeDef] = None
    ValueWhenUnset: Optional[IntegerValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class IntegerParameterDeclarationTypeDef(BaseModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[IntegerDefaultValuesTypeDef] = None
    ValueWhenUnset: Optional[IntegerValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class StringParameterDeclarationOutputTypeDef(BaseModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[StringDefaultValuesOutputTypeDef] = None
    ValueWhenUnset: Optional[StringValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class StringParameterDeclarationTypeDef(BaseModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[StringDefaultValuesTypeDef] = None
    ValueWhenUnset: Optional[StringValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class DateTimeHierarchyOutputTypeDef(BaseModel):
    HierarchyId: str
    DrillDownFilters: Optional[List[DrillDownFilterOutputTypeDef]] = None

class ExplicitHierarchyOutputTypeDef(BaseModel):
    HierarchyId: str
    Columns: List[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[List[DrillDownFilterOutputTypeDef]] = None

class PredefinedHierarchyOutputTypeDef(BaseModel):
    HierarchyId: str
    Columns: List[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[List[DrillDownFilterOutputTypeDef]] = None

class DescribeAnalysisResponseTypeDef(BaseModel):
    Analysis: AnalysisTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DashboardTypeDef(BaseModel):
    DashboardId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[DashboardVersionTypeDef] = None
    CreatedTime: Optional[datetime] = None
    LastPublishedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    LinkEntities: Optional[List[str]] = None

class GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    Namespace: str
    AuthorizedResourceArns: Sequence[str]
    ExperienceConfiguration: AnonymousUserEmbeddingExperienceConfigurationTypeDef
    SessionLifetimeInMinutes: Optional[int] = None
    SessionTags: Optional[Sequence[SessionTagTypeDef]] = None
    AllowedDomains: Optional[Sequence[str]] = None

class AssetBundleImportJobOverridePermissionsOutputTypeDef(BaseModel):
    DataSources: Optional[       List[AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef]     ] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverridePermissionsOutputTypeDef]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef]] = None
    Dashboards: Optional[       List[AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef]     ] = None

class AssetBundleImportJobOverridePermissionsTypeDef(BaseModel):
    DataSources: Optional[       Sequence[AssetBundleImportJobDataSourceOverridePermissionsTypeDef]     ] = None
    DataSets: Optional[Sequence[AssetBundleImportJobDataSetOverridePermissionsTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleImportJobThemeOverridePermissionsTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleImportJobAnalysisOverridePermissionsTypeDef]] = None
    Dashboards: Optional[       Sequence[AssetBundleImportJobDashboardOverridePermissionsTypeDef]     ] = None

class DestinationParameterValueConfigurationTypeDef(BaseModel):
    CustomValuesConfiguration: Optional[CustomValuesConfigurationTypeDef] = None
    SelectAllValueOptions: Optional[Literal["ALL_VALUES"]] = None
    SourceParameterName: Optional[str] = None
    SourceField: Optional[str] = None
    SourceColumn: Optional[ColumnIdentifierTypeDef] = None

class DatasetParameterTypeDef(BaseModel):
    StringDatasetParameter: Optional[StringDatasetParameterTypeDef] = None
    DecimalDatasetParameter: Optional[DecimalDatasetParameterTypeDef] = None
    IntegerDatasetParameter: Optional[IntegerDatasetParameterTypeDef] = None
    DateTimeDatasetParameter: Optional[DateTimeDatasetParameterTypeDef] = None

class DateTimeHierarchyTypeDef(BaseModel):
    HierarchyId: str
    DrillDownFilters: Optional[Sequence[DrillDownFilterTypeDef]] = None

class ExplicitHierarchyTypeDef(BaseModel):
    HierarchyId: str
    Columns: Sequence[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[Sequence[DrillDownFilterTypeDef]] = None

class PredefinedHierarchyTypeDef(BaseModel):
    HierarchyId: str
    Columns: Sequence[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[Sequence[DrillDownFilterTypeDef]] = None

class ForecastConfigurationTypeDef(BaseModel):
    ForecastProperties: Optional[TimeBasedForecastPropertiesTypeDef] = None
    Scenario: Optional[ForecastScenarioTypeDef] = None

class AxisDataOptionsOutputTypeDef(BaseModel):
    NumericAxisOptions: Optional[NumericAxisOptionsOutputTypeDef] = None
    DateAxisOptions: Optional[DateAxisOptionsTypeDef] = None

class AxisDataOptionsTypeDef(BaseModel):
    NumericAxisOptions: Optional[NumericAxisOptionsTypeDef] = None
    DateAxisOptions: Optional[DateAxisOptionsTypeDef] = None

class TransformOperationOutputTypeDef(BaseModel):
    ProjectOperation: Optional[ProjectOperationOutputTypeDef] = None
    FilterOperation: Optional[FilterOperationTypeDef] = None
    CreateColumnsOperation: Optional[CreateColumnsOperationOutputTypeDef] = None
    RenameColumnOperation: Optional[RenameColumnOperationTypeDef] = None
    CastColumnTypeOperation: Optional[CastColumnTypeOperationTypeDef] = None
    TagColumnOperation: Optional[TagColumnOperationOutputTypeDef] = None
    UntagColumnOperation: Optional[UntagColumnOperationOutputTypeDef] = None
    OverrideDatasetParameterOperation: Optional[       OverrideDatasetParameterOperationOutputTypeDef     ] = None

class TransformOperationTypeDef(BaseModel):
    ProjectOperation: Optional[ProjectOperationTypeDef] = None
    FilterOperation: Optional[FilterOperationTypeDef] = None
    CreateColumnsOperation: Optional[CreateColumnsOperationTypeDef] = None
    RenameColumnOperation: Optional[RenameColumnOperationTypeDef] = None
    CastColumnTypeOperation: Optional[CastColumnTypeOperationTypeDef] = None
    TagColumnOperation: Optional[TagColumnOperationTypeDef] = None
    UntagColumnOperation: Optional[UntagColumnOperationTypeDef] = None
    OverrideDatasetParameterOperation: Optional[OverrideDatasetParameterOperationTypeDef] = None

class TemplateVersionTypeDef(BaseModel):
    CreatedTime: Optional[datetime] = None
    Errors: Optional[List[TemplateErrorTypeDef]] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    DataSetConfigurations: Optional[List[DataSetConfigurationOutputTypeDef]] = None
    Description: Optional[str] = None
    SourceEntityArn: Optional[str] = None
    ThemeArn: Optional[str] = None
    Sheets: Optional[List[SheetTypeDef]] = None

class SetParameterValueConfigurationOutputTypeDef(BaseModel):
    DestinationParameterName: str
    Value: DestinationParameterValueConfigurationOutputTypeDef

class VisualPaletteOutputTypeDef(BaseModel):
    ChartColor: Optional[str] = None
    ColorMap: Optional[List[DataPathColorTypeDef]] = None

class VisualPaletteTypeDef(BaseModel):
    ChartColor: Optional[str] = None
    ColorMap: Optional[Sequence[DataPathColorTypeDef]] = None

class PivotTableFieldCollapseStateOptionOutputTypeDef(BaseModel):
    Target: PivotTableFieldCollapseStateTargetOutputTypeDef
    State: Optional[PivotTableFieldCollapseStateType] = None

class PivotTableFieldCollapseStateOptionTypeDef(BaseModel):
    Target: PivotTableFieldCollapseStateTargetTypeDef
    State: Optional[PivotTableFieldCollapseStateType] = None

class TopicCalculatedFieldOutputTypeDef(BaseModel):
    CalculatedFieldName: str
    Expression: str
    CalculatedFieldDescription: Optional[str] = None
    CalculatedFieldSynonyms: Optional[List[str]] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    DefaultFormatting: Optional[DefaultFormattingTypeDef] = None
    Aggregation: Optional[DefaultAggregationType] = None
    ComparativeOrder: Optional[ComparativeOrderOutputTypeDef] = None
    SemanticType: Optional[SemanticTypeOutputTypeDef] = None
    AllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[List[CellValueSynonymOutputTypeDef]] = None
    NonAdditive: Optional[bool] = None

class TopicCalculatedFieldTypeDef(BaseModel):
    CalculatedFieldName: str
    Expression: str
    CalculatedFieldDescription: Optional[str] = None
    CalculatedFieldSynonyms: Optional[Sequence[str]] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    DefaultFormatting: Optional[DefaultFormattingTypeDef] = None
    Aggregation: Optional[DefaultAggregationType] = None
    ComparativeOrder: Optional[ComparativeOrderTypeDef] = None
    SemanticType: Optional[SemanticTypeTypeDef] = None
    AllowedAggregations: Optional[Sequence[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[Sequence[AuthorSpecifiedAggregationType]] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[Sequence[CellValueSynonymTypeDef]] = None
    NonAdditive: Optional[bool] = None

class TopicColumnOutputTypeDef(BaseModel):
    ColumnName: str
    ColumnFriendlyName: Optional[str] = None
    ColumnDescription: Optional[str] = None
    ColumnSynonyms: Optional[List[str]] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    Aggregation: Optional[DefaultAggregationType] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ComparativeOrder: Optional[ComparativeOrderOutputTypeDef] = None
    SemanticType: Optional[SemanticTypeOutputTypeDef] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    AllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[List[AuthorSpecifiedAggregationType]] = None
    DefaultFormatting: Optional[DefaultFormattingTypeDef] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[List[CellValueSynonymOutputTypeDef]] = None
    NonAdditive: Optional[bool] = None

class TopicColumnTypeDef(BaseModel):
    ColumnName: str
    ColumnFriendlyName: Optional[str] = None
    ColumnDescription: Optional[str] = None
    ColumnSynonyms: Optional[Sequence[str]] = None
    ColumnDataRole: Optional[ColumnDataRoleType] = None
    Aggregation: Optional[DefaultAggregationType] = None
    IsIncludedInTopic: Optional[bool] = None
    DisableIndexing: Optional[bool] = None
    ComparativeOrder: Optional[ComparativeOrderTypeDef] = None
    SemanticType: Optional[SemanticTypeTypeDef] = None
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    AllowedAggregations: Optional[Sequence[AuthorSpecifiedAggregationType]] = None
    NotAllowedAggregations: Optional[Sequence[AuthorSpecifiedAggregationType]] = None
    DefaultFormatting: Optional[DefaultFormattingTypeDef] = None
    NeverAggregateInFilter: Optional[bool] = None
    CellValueSynonyms: Optional[Sequence[CellValueSynonymTypeDef]] = None
    NonAdditive: Optional[bool] = None

class ChartAxisLabelOptionsOutputTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    SortIconVisibility: Optional[VisibilityType] = None
    AxisLabelOptions: Optional[List[AxisLabelOptionsTypeDef]] = None

class ChartAxisLabelOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    SortIconVisibility: Optional[VisibilityType] = None
    AxisLabelOptions: Optional[Sequence[AxisLabelOptionsTypeDef]] = None

class AxisTickLabelOptionsTypeDef(BaseModel):
    LabelOptions: Optional[LabelOptionsTypeDef] = None
    RotationAngle: Optional[float] = None

class DateTimePickerControlDisplayOptionsTypeDef(BaseModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    DateTimeFormat: Optional[str] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class DropDownControlDisplayOptionsTypeDef(BaseModel):
    SelectAllOptions: Optional[ListControlSelectAllOptionsTypeDef] = None
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class LegendOptionsTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    Title: Optional[LabelOptionsTypeDef] = None
    Position: Optional[LegendPositionType] = None
    Width: Optional[str] = None
    Height: Optional[str] = None

class ListControlDisplayOptionsTypeDef(BaseModel):
    SearchOptions: Optional[ListControlSearchOptionsTypeDef] = None
    SelectAllOptions: Optional[ListControlSelectAllOptionsTypeDef] = None
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class RelativeDateTimeControlDisplayOptionsTypeDef(BaseModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    DateTimeFormat: Optional[str] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class SliderControlDisplayOptionsTypeDef(BaseModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class TextAreaControlDisplayOptionsTypeDef(BaseModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    PlaceholderOptions: Optional[TextControlPlaceholderOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class TextFieldControlDisplayOptionsTypeDef(BaseModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    PlaceholderOptions: Optional[TextControlPlaceholderOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class PanelConfigurationTypeDef(BaseModel):
    Title: Optional[PanelTitleOptionsTypeDef] = None
    BorderVisibility: Optional[VisibilityType] = None
    BorderThickness: Optional[str] = None
    BorderStyle: Optional[PanelBorderStyleType] = None
    BorderColor: Optional[str] = None
    GutterVisibility: Optional[VisibilityType] = None
    GutterSpacing: Optional[str] = None
    BackgroundVisibility: Optional[VisibilityType] = None
    BackgroundColor: Optional[str] = None

class TableFieldLinkContentConfigurationTypeDef(BaseModel):
    CustomTextContent: Optional[TableFieldCustomTextContentTypeDef] = None
    CustomIconContent: Optional[TableFieldCustomIconContentTypeDef] = None

class GeospatialPointStyleOptionsOutputTypeDef(BaseModel):
    SelectedPointStyle: Optional[GeospatialSelectedPointStyleType] = None
    ClusterMarkerConfiguration: Optional[ClusterMarkerConfigurationTypeDef] = None
    HeatmapConfiguration: Optional[GeospatialHeatmapConfigurationOutputTypeDef] = None

class GeospatialPointStyleOptionsTypeDef(BaseModel):
    SelectedPointStyle: Optional[GeospatialSelectedPointStyleType] = None
    ClusterMarkerConfiguration: Optional[ClusterMarkerConfigurationTypeDef] = None
    HeatmapConfiguration: Optional[GeospatialHeatmapConfigurationTypeDef] = None

class TableCellStyleTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    TextWrap: Optional[TextWrapType] = None
    HorizontalTextAlignment: Optional[HorizontalTextAlignmentType] = None
    VerticalTextAlignment: Optional[VerticalTextAlignmentType] = None
    BackgroundColor: Optional[str] = None
    Height: Optional[int] = None
    Border: Optional[GlobalTableBorderOptionsTypeDef] = None

class ConditionalFormattingColorOutputTypeDef(BaseModel):
    Solid: Optional[ConditionalFormattingSolidColorTypeDef] = None
    Gradient: Optional[ConditionalFormattingGradientColorOutputTypeDef] = None

class ConditionalFormattingColorTypeDef(BaseModel):
    Solid: Optional[ConditionalFormattingSolidColorTypeDef] = None
    Gradient: Optional[ConditionalFormattingGradientColorTypeDef] = None

class DefaultInteractiveLayoutConfigurationTypeDef(BaseModel):
    Grid: Optional[DefaultGridLayoutConfigurationTypeDef] = None
    FreeForm: Optional[DefaultFreeFormLayoutConfigurationTypeDef] = None

class SheetControlLayoutConfigurationOutputTypeDef(BaseModel):
    GridLayout: Optional[GridLayoutConfigurationOutputTypeDef] = None

class SheetControlLayoutConfigurationTypeDef(BaseModel):
    GridLayout: Optional[GridLayoutConfigurationTypeDef] = None

class DataSetRefreshPropertiesTypeDef(BaseModel):
    RefreshConfiguration: RefreshConfigurationTypeDef

class SeriesItemTypeDef(BaseModel):
    FieldSeriesItem: Optional[FieldSeriesItemTypeDef] = None
    DataFieldSeriesItem: Optional[DataFieldSeriesItemTypeDef] = None

class ThemeConfigurationOutputTypeDef(BaseModel):
    DataColorPalette: Optional[DataColorPaletteOutputTypeDef] = None
    UIColorPalette: Optional[UIColorPaletteTypeDef] = None
    Sheet: Optional[SheetStyleTypeDef] = None
    Typography: Optional[TypographyOutputTypeDef] = None

class ThemeConfigurationTypeDef(BaseModel):
    DataColorPalette: Optional[DataColorPaletteTypeDef] = None
    UIColorPalette: Optional[UIColorPaletteTypeDef] = None
    Sheet: Optional[SheetStyleTypeDef] = None
    Typography: Optional[TypographyTypeDef] = None

class ComparisonFormatConfigurationTypeDef(BaseModel):
    NumberDisplayFormatConfiguration: Optional[NumberDisplayFormatConfigurationTypeDef] = None
    PercentageDisplayFormatConfiguration: Optional[       PercentageDisplayFormatConfigurationTypeDef     ] = None

class NumericFormatConfigurationTypeDef(BaseModel):
    NumberDisplayFormatConfiguration: Optional[NumberDisplayFormatConfigurationTypeDef] = None
    CurrencyDisplayFormatConfiguration: Optional[       CurrencyDisplayFormatConfigurationTypeDef     ] = None
    PercentageDisplayFormatConfiguration: Optional[       PercentageDisplayFormatConfigurationTypeDef     ] = None

class AggregationSortConfigurationTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    SortDirection: SortDirectionType
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None

class ColumnSortTypeDef(BaseModel):
    SortBy: ColumnIdentifierTypeDef
    Direction: SortDirectionType
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None

class ColumnTooltipItemTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    Aggregation: Optional[AggregationFunctionTypeDef] = None
    TooltipTarget: Optional[TooltipTargetType] = None

class ReferenceLineDynamicDataConfigurationTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Calculation: NumericalAggregationFunctionTypeDef
    MeasureAggregationFunction: Optional[AggregationFunctionTypeDef] = None

class TopicFilterOutputTypeDef(BaseModel):
    FilterName: str
    OperandFieldName: str
    FilterDescription: Optional[str] = None
    FilterClass: Optional[FilterClassType] = None
    FilterSynonyms: Optional[List[str]] = None
    FilterType: Optional[NamedFilterTypeType] = None
    CategoryFilter: Optional[TopicCategoryFilterOutputTypeDef] = None
    NumericEqualityFilter: Optional[TopicNumericEqualityFilterTypeDef] = None
    NumericRangeFilter: Optional[TopicNumericRangeFilterTypeDef] = None
    DateRangeFilter: Optional[TopicDateRangeFilterTypeDef] = None
    RelativeDateFilter: Optional[TopicRelativeDateFilterTypeDef] = None

class TopicFilterTypeDef(BaseModel):
    FilterName: str
    OperandFieldName: str
    FilterDescription: Optional[str] = None
    FilterClass: Optional[FilterClassType] = None
    FilterSynonyms: Optional[Sequence[str]] = None
    FilterType: Optional[NamedFilterTypeType] = None
    CategoryFilter: Optional[TopicCategoryFilterTypeDef] = None
    NumericEqualityFilter: Optional[TopicNumericEqualityFilterTypeDef] = None
    NumericRangeFilter: Optional[TopicNumericRangeFilterTypeDef] = None
    DateRangeFilter: Optional[TopicDateRangeFilterTypeDef] = None
    RelativeDateFilter: Optional[TopicRelativeDateFilterTypeDef] = None

class AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef(BaseModel):
    DataSourceId: str
    Name: Optional[str] = None
    DataSourceParameters: Optional[DataSourceParametersOutputTypeDef] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None
    Credentials: Optional[AssetBundleImportJobDataSourceCredentialsTypeDef] = None

class DataSourceTypeDef(BaseModel):
    Arn: Optional[str] = None
    DataSourceId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    Status: Optional[ResourceStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    DataSourceParameters: Optional[DataSourceParametersOutputTypeDef] = None
    AlternateDataSourceParameters: Optional[List[DataSourceParametersOutputTypeDef]] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None
    ErrorInfo: Optional[DataSourceErrorInfoTypeDef] = None
    SecretArn: Optional[str] = None

class AssetBundleImportJobDataSourceOverrideParametersTypeDef(BaseModel):
    DataSourceId: str
    Name: Optional[str] = None
    DataSourceParameters: Optional[DataSourceParametersTypeDef] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None
    Credentials: Optional[AssetBundleImportJobDataSourceCredentialsTypeDef] = None

class CredentialPairTypeDef(BaseModel):
    Username: str
    Password: str
    AlternateDataSourceParameters: Optional[Sequence[DataSourceParametersTypeDef]] = None

class DescribeRefreshScheduleResponseTypeDef(BaseModel):
    RefreshSchedule: RefreshScheduleOutputTypeDef
    Status: int
    RequestId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRefreshSchedulesResponseTypeDef(BaseModel):
    RefreshSchedules: List[RefreshScheduleOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRefreshScheduleRequestRequestTypeDef(BaseModel):
    DataSetId: str
    AwsAccountId: str
    Schedule: RefreshScheduleTypeDef

class UpdateRefreshScheduleRequestRequestTypeDef(BaseModel):
    DataSetId: str
    AwsAccountId: str
    Schedule: RefreshScheduleTypeDef

class RegisteredUserEmbeddingExperienceConfigurationTypeDef(BaseModel):
    Dashboard: Optional[RegisteredUserDashboardEmbeddingConfigurationTypeDef] = None
    QuickSightConsole: Optional[       RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef     ] = None
    QSearchBar: Optional[RegisteredUserQSearchBarEmbeddingConfigurationTypeDef] = None
    DashboardVisual: Optional[RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef] = None
    GenerativeQnA: Optional[RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef] = None

class SnapshotJobResultFileGroupTypeDef(BaseModel):
    Files: Optional[List[SnapshotFileOutputTypeDef]] = None
    S3Results: Optional[List[SnapshotJobS3ResultTypeDef]] = None

class DefaultSectionBasedLayoutConfigurationTypeDef(BaseModel):
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptionsTypeDef

class FreeFormLayoutConfigurationOutputTypeDef(BaseModel):
    Elements: List[FreeFormLayoutElementOutputTypeDef]
    CanvasSizeOptions: Optional[FreeFormLayoutCanvasSizeOptionsTypeDef] = None

class FreeFormSectionLayoutConfigurationOutputTypeDef(BaseModel):
    Elements: List[FreeFormLayoutElementOutputTypeDef]

class FreeFormLayoutConfigurationTypeDef(BaseModel):
    Elements: Sequence[FreeFormLayoutElementTypeDef]
    CanvasSizeOptions: Optional[FreeFormLayoutCanvasSizeOptionsTypeDef] = None

class FreeFormSectionLayoutConfigurationTypeDef(BaseModel):
    Elements: Sequence[FreeFormLayoutElementTypeDef]

class SnapshotConfigurationOutputTypeDef(BaseModel):
    FileGroups: List[SnapshotFileGroupOutputTypeDef]
    DestinationConfiguration: Optional[SnapshotDestinationConfigurationOutputTypeDef] = None
    Parameters: Optional[ParametersOutputTypeDef] = None

class SnapshotConfigurationTypeDef(BaseModel):
    FileGroups: Sequence[SnapshotFileGroupTypeDef]
    DestinationConfiguration: Optional[SnapshotDestinationConfigurationTypeDef] = None
    Parameters: Optional[ParametersTypeDef] = None

class ParameterDeclarationOutputTypeDef(BaseModel):
    StringParameterDeclaration: Optional[StringParameterDeclarationOutputTypeDef] = None
    DecimalParameterDeclaration: Optional[DecimalParameterDeclarationOutputTypeDef] = None
    IntegerParameterDeclaration: Optional[IntegerParameterDeclarationOutputTypeDef] = None
    DateTimeParameterDeclaration: Optional[DateTimeParameterDeclarationOutputTypeDef] = None

class ParameterDeclarationTypeDef(BaseModel):
    StringParameterDeclaration: Optional[StringParameterDeclarationTypeDef] = None
    DecimalParameterDeclaration: Optional[DecimalParameterDeclarationTypeDef] = None
    IntegerParameterDeclaration: Optional[IntegerParameterDeclarationTypeDef] = None
    DateTimeParameterDeclaration: Optional[DateTimeParameterDeclarationTypeDef] = None

class ColumnHierarchyOutputTypeDef(BaseModel):
    ExplicitHierarchy: Optional[ExplicitHierarchyOutputTypeDef] = None
    DateTimeHierarchy: Optional[DateTimeHierarchyOutputTypeDef] = None
    PredefinedHierarchy: Optional[PredefinedHierarchyOutputTypeDef] = None

class DescribeDashboardResponseTypeDef(BaseModel):
    Dashboard: DashboardTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetParameterValueConfigurationTypeDef(BaseModel):
    DestinationParameterName: str
    Value: DestinationParameterValueConfigurationTypeDef

class ColumnHierarchyTypeDef(BaseModel):
    ExplicitHierarchy: Optional[ExplicitHierarchyTypeDef] = None
    DateTimeHierarchy: Optional[DateTimeHierarchyTypeDef] = None
    PredefinedHierarchy: Optional[PredefinedHierarchyTypeDef] = None

class LogicalTableOutputTypeDef(BaseModel):
    Alias: str
    Source: LogicalTableSourceTypeDef
    DataTransforms: Optional[List[TransformOperationOutputTypeDef]] = None

class LogicalTableTypeDef(BaseModel):
    Alias: str
    Source: LogicalTableSourceTypeDef
    DataTransforms: Optional[Sequence[TransformOperationTypeDef]] = None

class TemplateTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[TemplateVersionTypeDef] = None
    TemplateId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None

class CustomActionSetParametersOperationOutputTypeDef(BaseModel):
    ParameterValueConfigurations: List[SetParameterValueConfigurationOutputTypeDef]

class PivotTableFieldOptionsOutputTypeDef(BaseModel):
    SelectedFieldOptions: Optional[List[PivotTableFieldOptionTypeDef]] = None
    DataPathOptions: Optional[List[PivotTableDataPathOptionOutputTypeDef]] = None
    CollapseStateOptions: Optional[List[PivotTableFieldCollapseStateOptionOutputTypeDef]] = None

class PivotTableFieldOptionsTypeDef(BaseModel):
    SelectedFieldOptions: Optional[Sequence[PivotTableFieldOptionTypeDef]] = None
    DataPathOptions: Optional[Sequence[PivotTableDataPathOptionTypeDef]] = None
    CollapseStateOptions: Optional[Sequence[PivotTableFieldCollapseStateOptionTypeDef]] = None

class AxisDisplayOptionsOutputTypeDef(BaseModel):
    TickLabelOptions: Optional[AxisTickLabelOptionsTypeDef] = None
    AxisLineVisibility: Optional[VisibilityType] = None
    GridLineVisibility: Optional[VisibilityType] = None
    DataOptions: Optional[AxisDataOptionsOutputTypeDef] = None
    ScrollbarOptions: Optional[ScrollBarOptionsTypeDef] = None
    AxisOffset: Optional[str] = None

class AxisDisplayOptionsTypeDef(BaseModel):
    TickLabelOptions: Optional[AxisTickLabelOptionsTypeDef] = None
    AxisLineVisibility: Optional[VisibilityType] = None
    GridLineVisibility: Optional[VisibilityType] = None
    DataOptions: Optional[AxisDataOptionsTypeDef] = None
    ScrollbarOptions: Optional[ScrollBarOptionsTypeDef] = None
    AxisOffset: Optional[str] = None

class DefaultDateTimePickerControlOptionsTypeDef(BaseModel):
    Type: Optional[SheetControlDateTimePickerTypeType] = None
    DisplayOptions: Optional[DateTimePickerControlDisplayOptionsTypeDef] = None

class FilterDateTimePickerControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DateTimePickerControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlDateTimePickerTypeType] = None

class ParameterDateTimePickerControlTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DateTimePickerControlDisplayOptionsTypeDef] = None

class DefaultFilterDropDownControlOptionsOutputTypeDef(BaseModel):
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None

class DefaultFilterDropDownControlOptionsTypeDef(BaseModel):
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None

class FilterDropDownControlOutputTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class FilterDropDownControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class ParameterDropDownControlOutputTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class ParameterDropDownControlTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class DefaultFilterListControlOptionsOutputTypeDef(BaseModel):
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None

class DefaultFilterListControlOptionsTypeDef(BaseModel):
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None

class FilterListControlOutputTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class FilterListControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class ParameterListControlOutputTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class ParameterListControlTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class DefaultRelativeDateTimeControlOptionsTypeDef(BaseModel):
    DisplayOptions: Optional[RelativeDateTimeControlDisplayOptionsTypeDef] = None

class FilterRelativeDateTimeControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[RelativeDateTimeControlDisplayOptionsTypeDef] = None

class DefaultSliderControlOptionsTypeDef(BaseModel):
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlSliderTypeType] = None

class FilterSliderControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlSliderTypeType] = None

class ParameterSliderControlTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptionsTypeDef] = None

class DefaultTextAreaControlOptionsTypeDef(BaseModel):
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptionsTypeDef] = None

class FilterTextAreaControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptionsTypeDef] = None

class ParameterTextAreaControlTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptionsTypeDef] = None

class DefaultTextFieldControlOptionsTypeDef(BaseModel):
    DisplayOptions: Optional[TextFieldControlDisplayOptionsTypeDef] = None

class FilterTextFieldControlTypeDef(BaseModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[TextFieldControlDisplayOptionsTypeDef] = None

class ParameterTextFieldControlTypeDef(BaseModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[TextFieldControlDisplayOptionsTypeDef] = None

class SmallMultiplesOptionsTypeDef(BaseModel):
    MaxVisibleRows: Optional[int] = None
    MaxVisibleColumns: Optional[int] = None
    PanelConfiguration: Optional[PanelConfigurationTypeDef] = None
    XAxis: Optional[SmallMultiplesAxisPropertiesTypeDef] = None
    YAxis: Optional[SmallMultiplesAxisPropertiesTypeDef] = None

class TableFieldLinkConfigurationTypeDef(BaseModel):
    Target: URLTargetConfigurationType
    Content: TableFieldLinkContentConfigurationTypeDef

class PivotTableOptionsOutputTypeDef(BaseModel):
    MetricPlacement: Optional[PivotTableMetricPlacementType] = None
    SingleMetricVisibility: Optional[VisibilityType] = None
    ColumnNamesVisibility: Optional[VisibilityType] = None
    ToggleButtonsVisibility: Optional[VisibilityType] = None
    ColumnHeaderStyle: Optional[TableCellStyleTypeDef] = None
    RowHeaderStyle: Optional[TableCellStyleTypeDef] = None
    CellStyle: Optional[TableCellStyleTypeDef] = None
    RowFieldNamesStyle: Optional[TableCellStyleTypeDef] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsOutputTypeDef] = None
    CollapsedRowDimensionsVisibility: Optional[VisibilityType] = None
    RowsLayout: Optional[PivotTableRowsLayoutType] = None
    RowsLabelOptions: Optional[PivotTableRowsLabelOptionsTypeDef] = None
    DefaultCellWidth: Optional[str] = None

class PivotTableOptionsTypeDef(BaseModel):
    MetricPlacement: Optional[PivotTableMetricPlacementType] = None
    SingleMetricVisibility: Optional[VisibilityType] = None
    ColumnNamesVisibility: Optional[VisibilityType] = None
    ToggleButtonsVisibility: Optional[VisibilityType] = None
    ColumnHeaderStyle: Optional[TableCellStyleTypeDef] = None
    RowHeaderStyle: Optional[TableCellStyleTypeDef] = None
    CellStyle: Optional[TableCellStyleTypeDef] = None
    RowFieldNamesStyle: Optional[TableCellStyleTypeDef] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsTypeDef] = None
    CollapsedRowDimensionsVisibility: Optional[VisibilityType] = None
    RowsLayout: Optional[PivotTableRowsLayoutType] = None
    RowsLabelOptions: Optional[PivotTableRowsLabelOptionsTypeDef] = None
    DefaultCellWidth: Optional[str] = None

class PivotTotalOptionsOutputTypeDef(BaseModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOptionTypeDef]] = None

class PivotTotalOptionsTypeDef(BaseModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[Sequence[TotalAggregationOptionTypeDef]] = None

class SubtotalOptionsOutputTypeDef(BaseModel):
    TotalsVisibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None
    FieldLevel: Optional[PivotTableSubtotalLevelType] = None
    FieldLevelOptions: Optional[List[PivotTableFieldSubtotalOptionsTypeDef]] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    StyleTargets: Optional[List[TableStyleTargetTypeDef]] = None

class SubtotalOptionsTypeDef(BaseModel):
    TotalsVisibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None
    FieldLevel: Optional[PivotTableSubtotalLevelType] = None
    FieldLevelOptions: Optional[Sequence[PivotTableFieldSubtotalOptionsTypeDef]] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    StyleTargets: Optional[Sequence[TableStyleTargetTypeDef]] = None

class TableOptionsOutputTypeDef(BaseModel):
    Orientation: Optional[TableOrientationType] = None
    HeaderStyle: Optional[TableCellStyleTypeDef] = None
    CellStyle: Optional[TableCellStyleTypeDef] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsOutputTypeDef] = None

class TableOptionsTypeDef(BaseModel):
    Orientation: Optional[TableOrientationType] = None
    HeaderStyle: Optional[TableCellStyleTypeDef] = None
    CellStyle: Optional[TableCellStyleTypeDef] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsTypeDef] = None

class TotalOptionsOutputTypeDef(BaseModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOptionTypeDef]] = None

class TotalOptionsTypeDef(BaseModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[Sequence[TotalAggregationOptionTypeDef]] = None

class GaugeChartArcConditionalFormattingOutputTypeDef(BaseModel):
    ForegroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None

class GaugeChartPrimaryValueConditionalFormattingOutputTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIActualValueConditionalFormattingOutputTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIComparisonValueConditionalFormattingOutputTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIPrimaryValueConditionalFormattingOutputTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIProgressBarConditionalFormattingOutputTypeDef(BaseModel):
    ForegroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None

class ShapeConditionalFormatOutputTypeDef(BaseModel):
    BackgroundColor: ConditionalFormattingColorOutputTypeDef

class TableRowConditionalFormattingOutputTypeDef(BaseModel):
    BackgroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None

class TextConditionalFormatOutputTypeDef(BaseModel):
    BackgroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class GaugeChartArcConditionalFormattingTypeDef(BaseModel):
    ForegroundColor: Optional[ConditionalFormattingColorTypeDef] = None

class GaugeChartPrimaryValueConditionalFormattingTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIActualValueConditionalFormattingTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIComparisonValueConditionalFormattingTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIPrimaryValueConditionalFormattingTypeDef(BaseModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIProgressBarConditionalFormattingTypeDef(BaseModel):
    ForegroundColor: Optional[ConditionalFormattingColorTypeDef] = None

class ShapeConditionalFormatTypeDef(BaseModel):
    BackgroundColor: ConditionalFormattingColorTypeDef

class TableRowConditionalFormattingTypeDef(BaseModel):
    BackgroundColor: Optional[ConditionalFormattingColorTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None

class TextConditionalFormatTypeDef(BaseModel):
    BackgroundColor: Optional[ConditionalFormattingColorTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class SheetControlLayoutOutputTypeDef(BaseModel):
    Configuration: SheetControlLayoutConfigurationOutputTypeDef

class SheetControlLayoutTypeDef(BaseModel):
    Configuration: SheetControlLayoutConfigurationTypeDef

class DescribeDataSetRefreshPropertiesResponseTypeDef(BaseModel):
    RequestId: str
    Status: int
    DataSetRefreshProperties: DataSetRefreshPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataSetRefreshPropertiesRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    DataSetRefreshProperties: DataSetRefreshPropertiesTypeDef

class ThemeVersionTypeDef(BaseModel):
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    BaseThemeId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Configuration: Optional[ThemeConfigurationOutputTypeDef] = None
    Errors: Optional[List[ThemeErrorTypeDef]] = None
    Status: Optional[ResourceStatusType] = None

class CreateThemeRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    Name: str
    BaseThemeId: str
    Configuration: ThemeConfigurationTypeDef
    VersionDescription: Optional[str] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateThemeRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    ThemeId: str
    BaseThemeId: str
    Name: Optional[str] = None
    VersionDescription: Optional[str] = None
    Configuration: Optional[ThemeConfigurationTypeDef] = None

class ComparisonConfigurationTypeDef(BaseModel):
    ComparisonMethod: Optional[ComparisonMethodType] = None
    ComparisonFormat: Optional[ComparisonFormatConfigurationTypeDef] = None

class DateTimeFormatConfigurationTypeDef(BaseModel):
    DateTimeFormat: Optional[str] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None
    NumericFormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class NumberFormatConfigurationTypeDef(BaseModel):
    FormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class ReferenceLineValueLabelConfigurationTypeDef(BaseModel):
    RelativePosition: Optional[ReferenceLineValueLabelRelativePositionType] = None
    FormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class StringFormatConfigurationTypeDef(BaseModel):
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None
    NumericFormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSortTypeDef]] = None

class BodySectionDynamicCategoryDimensionConfigurationTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[Sequence[ColumnSortTypeDef]] = None

class BodySectionDynamicNumericDimensionConfigurationOutputTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSortTypeDef]] = None

class BodySectionDynamicNumericDimensionConfigurationTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[Sequence[ColumnSortTypeDef]] = None

class FieldSortOptionsTypeDef(BaseModel):
    FieldSort: Optional[FieldSortTypeDef] = None
    ColumnSort: Optional[ColumnSortTypeDef] = None

class PivotTableSortByOutputTypeDef(BaseModel):
    Field: Optional[FieldSortTypeDef] = None
    Column: Optional[ColumnSortTypeDef] = None
    DataPath: Optional[DataPathSortOutputTypeDef] = None

class PivotTableSortByTypeDef(BaseModel):
    Field: Optional[FieldSortTypeDef] = None
    Column: Optional[ColumnSortTypeDef] = None
    DataPath: Optional[DataPathSortTypeDef] = None

class TooltipItemTypeDef(BaseModel):
    FieldTooltipItem: Optional[FieldTooltipItemTypeDef] = None
    ColumnTooltipItem: Optional[ColumnTooltipItemTypeDef] = None

class ReferenceLineDataConfigurationTypeDef(BaseModel):
    StaticConfiguration: Optional[ReferenceLineStaticDataConfigurationTypeDef] = None
    DynamicConfiguration: Optional[ReferenceLineDynamicDataConfigurationTypeDef] = None
    AxisBinding: Optional[AxisBindingType] = None
    SeriesType: Optional[ReferenceLineSeriesTypeType] = None

class DatasetMetadataOutputTypeDef(BaseModel):
    DatasetArn: str
    DatasetName: Optional[str] = None
    DatasetDescription: Optional[str] = None
    DataAggregation: Optional[DataAggregationTypeDef] = None
    Filters: Optional[List[TopicFilterOutputTypeDef]] = None
    Columns: Optional[List[TopicColumnOutputTypeDef]] = None
    CalculatedFields: Optional[List[TopicCalculatedFieldOutputTypeDef]] = None
    NamedEntities: Optional[List[TopicNamedEntityOutputTypeDef]] = None

class DatasetMetadataTypeDef(BaseModel):
    DatasetArn: str
    DatasetName: Optional[str] = None
    DatasetDescription: Optional[str] = None
    DataAggregation: Optional[DataAggregationTypeDef] = None
    Filters: Optional[Sequence[TopicFilterTypeDef]] = None
    Columns: Optional[Sequence[TopicColumnTypeDef]] = None
    CalculatedFields: Optional[Sequence[TopicCalculatedFieldTypeDef]] = None
    NamedEntities: Optional[Sequence[TopicNamedEntityTypeDef]] = None

class AssetBundleImportJobOverrideParametersOutputTypeDef(BaseModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleImportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       List[AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef]     ] = None
    RefreshSchedules: Optional[       List[AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef]     ] = None
    DataSources: Optional[       List[AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef]     ] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideParametersTypeDef]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideParametersTypeDef]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideParametersTypeDef]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideParametersTypeDef]] = None

class DescribeDataSourceResponseTypeDef(BaseModel):
    DataSource: DataSourceTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(BaseModel):
    DataSources: List[DataSourceTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssetBundleImportJobOverrideParametersTypeDef(BaseModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleImportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       Sequence[AssetBundleImportJobVPCConnectionOverrideParametersTypeDef]     ] = None
    RefreshSchedules: Optional[       Sequence[AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef]     ] = None
    DataSources: Optional[       Sequence[AssetBundleImportJobDataSourceOverrideParametersTypeDef]     ] = None
    DataSets: Optional[Sequence[AssetBundleImportJobDataSetOverrideParametersTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleImportJobThemeOverrideParametersTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleImportJobAnalysisOverrideParametersTypeDef]] = None
    Dashboards: Optional[Sequence[AssetBundleImportJobDashboardOverrideParametersTypeDef]] = None

class DataSourceCredentialsTypeDef(BaseModel):
    CredentialPair: Optional[CredentialPairTypeDef] = None
    CopySourceArn: Optional[str] = None
    SecretArn: Optional[str] = None

class GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    UserArn: str
    ExperienceConfiguration: RegisteredUserEmbeddingExperienceConfigurationTypeDef
    SessionLifetimeInMinutes: Optional[int] = None
    AllowedDomains: Optional[Sequence[str]] = None

class AnonymousUserSnapshotJobResultTypeDef(BaseModel):
    FileGroups: Optional[List[SnapshotJobResultFileGroupTypeDef]] = None

class DefaultPaginatedLayoutConfigurationTypeDef(BaseModel):
    SectionBased: Optional[DefaultSectionBasedLayoutConfigurationTypeDef] = None

class SectionLayoutConfigurationOutputTypeDef(BaseModel):
    FreeFormLayout: FreeFormSectionLayoutConfigurationOutputTypeDef

class SectionLayoutConfigurationTypeDef(BaseModel):
    FreeFormLayout: FreeFormSectionLayoutConfigurationTypeDef

class DescribeDashboardSnapshotJobResponseTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str
    UserConfiguration: SnapshotUserConfigurationRedactedTypeDef
    SnapshotConfiguration: SnapshotConfigurationOutputTypeDef
    Arn: str
    JobStatus: SnapshotJobStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartDashboardSnapshotJobRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str
    UserConfiguration: SnapshotUserConfigurationTypeDef
    SnapshotConfiguration: SnapshotConfigurationTypeDef

class CustomActionSetParametersOperationTypeDef(BaseModel):
    ParameterValueConfigurations: Sequence[SetParameterValueConfigurationTypeDef]

class DataSetTypeDef(BaseModel):
    Arn: Optional[str] = None
    DataSetId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    PhysicalTableMap: Optional[Dict[str, PhysicalTableOutputTypeDef]] = None
    LogicalTableMap: Optional[Dict[str, LogicalTableOutputTypeDef]] = None
    OutputColumns: Optional[List[OutputColumnTypeDef]] = None
    ImportMode: Optional[DataSetImportModeType] = None
    ConsumedSpiceCapacityInBytes: Optional[int] = None
    ColumnGroups: Optional[List[ColumnGroupOutputTypeDef]] = None
    FieldFolders: Optional[Dict[str, FieldFolderOutputTypeDef]] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSetTypeDef] = None
    RowLevelPermissionTagConfiguration: Optional[       RowLevelPermissionTagConfigurationOutputTypeDef     ] = None
    ColumnLevelPermissionRules: Optional[List[ColumnLevelPermissionRuleOutputTypeDef]] = None
    DataSetUsageConfiguration: Optional[DataSetUsageConfigurationTypeDef] = None
    DatasetParameters: Optional[List[DatasetParameterOutputTypeDef]] = None

class DescribeTemplateResponseTypeDef(BaseModel):
    Template: TemplateTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VisualCustomActionOperationOutputTypeDef(BaseModel):
    FilterOperation: Optional[CustomActionFilterOperationOutputTypeDef] = None
    NavigationOperation: Optional[CustomActionNavigationOperationTypeDef] = None
    URLOperation: Optional[CustomActionURLOperationTypeDef] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationOutputTypeDef] = None

class LineSeriesAxisDisplayOptionsOutputTypeDef(BaseModel):
    AxisOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    MissingDataConfigurations: Optional[List[MissingDataConfigurationTypeDef]] = None

class LineSeriesAxisDisplayOptionsTypeDef(BaseModel):
    AxisOptions: Optional[AxisDisplayOptionsTypeDef] = None
    MissingDataConfigurations: Optional[Sequence[MissingDataConfigurationTypeDef]] = None

class DefaultFilterControlOptionsOutputTypeDef(BaseModel):
    DefaultDateTimePickerOptions: Optional[DefaultDateTimePickerControlOptionsTypeDef] = None
    DefaultListOptions: Optional[DefaultFilterListControlOptionsOutputTypeDef] = None
    DefaultDropdownOptions: Optional[DefaultFilterDropDownControlOptionsOutputTypeDef] = None
    DefaultTextFieldOptions: Optional[DefaultTextFieldControlOptionsTypeDef] = None
    DefaultTextAreaOptions: Optional[DefaultTextAreaControlOptionsTypeDef] = None
    DefaultSliderOptions: Optional[DefaultSliderControlOptionsTypeDef] = None
    DefaultRelativeDateTimeOptions: Optional[DefaultRelativeDateTimeControlOptionsTypeDef] = None

class DefaultFilterControlOptionsTypeDef(BaseModel):
    DefaultDateTimePickerOptions: Optional[DefaultDateTimePickerControlOptionsTypeDef] = None
    DefaultListOptions: Optional[DefaultFilterListControlOptionsTypeDef] = None
    DefaultDropdownOptions: Optional[DefaultFilterDropDownControlOptionsTypeDef] = None
    DefaultTextFieldOptions: Optional[DefaultTextFieldControlOptionsTypeDef] = None
    DefaultTextAreaOptions: Optional[DefaultTextAreaControlOptionsTypeDef] = None
    DefaultSliderOptions: Optional[DefaultSliderControlOptionsTypeDef] = None
    DefaultRelativeDateTimeOptions: Optional[DefaultRelativeDateTimeControlOptionsTypeDef] = None

class FilterControlOutputTypeDef(BaseModel):
    DateTimePicker: Optional[FilterDateTimePickerControlTypeDef] = None
    List: Optional[FilterListControlOutputTypeDef] = None
    Dropdown: Optional[FilterDropDownControlOutputTypeDef] = None
    TextField: Optional[FilterTextFieldControlTypeDef] = None
    TextArea: Optional[FilterTextAreaControlTypeDef] = None
    Slider: Optional[FilterSliderControlTypeDef] = None
    RelativeDateTime: Optional[FilterRelativeDateTimeControlTypeDef] = None
    CrossSheet: Optional[FilterCrossSheetControlOutputTypeDef] = None

class FilterControlTypeDef(BaseModel):
    DateTimePicker: Optional[FilterDateTimePickerControlTypeDef] = None
    List: Optional[FilterListControlTypeDef] = None
    Dropdown: Optional[FilterDropDownControlTypeDef] = None
    TextField: Optional[FilterTextFieldControlTypeDef] = None
    TextArea: Optional[FilterTextAreaControlTypeDef] = None
    Slider: Optional[FilterSliderControlTypeDef] = None
    RelativeDateTime: Optional[FilterRelativeDateTimeControlTypeDef] = None
    CrossSheet: Optional[FilterCrossSheetControlTypeDef] = None

class ParameterControlOutputTypeDef(BaseModel):
    DateTimePicker: Optional[ParameterDateTimePickerControlTypeDef] = None
    List: Optional[ParameterListControlOutputTypeDef] = None
    Dropdown: Optional[ParameterDropDownControlOutputTypeDef] = None
    TextField: Optional[ParameterTextFieldControlTypeDef] = None
    TextArea: Optional[ParameterTextAreaControlTypeDef] = None
    Slider: Optional[ParameterSliderControlTypeDef] = None

class ParameterControlTypeDef(BaseModel):
    DateTimePicker: Optional[ParameterDateTimePickerControlTypeDef] = None
    List: Optional[ParameterListControlTypeDef] = None
    Dropdown: Optional[ParameterDropDownControlTypeDef] = None
    TextField: Optional[ParameterTextFieldControlTypeDef] = None
    TextArea: Optional[ParameterTextAreaControlTypeDef] = None
    Slider: Optional[ParameterSliderControlTypeDef] = None

class TableFieldURLConfigurationTypeDef(BaseModel):
    LinkConfiguration: Optional[TableFieldLinkConfigurationTypeDef] = None
    ImageConfiguration: Optional[TableFieldImageConfigurationTypeDef] = None

class PivotTableTotalOptionsOutputTypeDef(BaseModel):
    RowSubtotalOptions: Optional[SubtotalOptionsOutputTypeDef] = None
    ColumnSubtotalOptions: Optional[SubtotalOptionsOutputTypeDef] = None
    RowTotalOptions: Optional[PivotTotalOptionsOutputTypeDef] = None
    ColumnTotalOptions: Optional[PivotTotalOptionsOutputTypeDef] = None

class PivotTableTotalOptionsTypeDef(BaseModel):
    RowSubtotalOptions: Optional[SubtotalOptionsTypeDef] = None
    ColumnSubtotalOptions: Optional[SubtotalOptionsTypeDef] = None
    RowTotalOptions: Optional[PivotTotalOptionsTypeDef] = None
    ColumnTotalOptions: Optional[PivotTotalOptionsTypeDef] = None

class GaugeChartConditionalFormattingOptionOutputTypeDef(BaseModel):
    PrimaryValue: Optional[GaugeChartPrimaryValueConditionalFormattingOutputTypeDef] = None
    Arc: Optional[GaugeChartArcConditionalFormattingOutputTypeDef] = None

class KPIConditionalFormattingOptionOutputTypeDef(BaseModel):
    PrimaryValue: Optional[KPIPrimaryValueConditionalFormattingOutputTypeDef] = None
    ProgressBar: Optional[KPIProgressBarConditionalFormattingOutputTypeDef] = None
    ActualValue: Optional[KPIActualValueConditionalFormattingOutputTypeDef] = None
    ComparisonValue: Optional[KPIComparisonValueConditionalFormattingOutputTypeDef] = None

class FilledMapShapeConditionalFormattingOutputTypeDef(BaseModel):
    FieldId: str
    Format: Optional[ShapeConditionalFormatOutputTypeDef] = None

class PivotTableCellConditionalFormattingOutputTypeDef(BaseModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatOutputTypeDef] = None
    Scope: Optional[PivotTableConditionalFormattingScopeTypeDef] = None
    Scopes: Optional[List[PivotTableConditionalFormattingScopeTypeDef]] = None

class TableCellConditionalFormattingOutputTypeDef(BaseModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatOutputTypeDef] = None

class GaugeChartConditionalFormattingOptionTypeDef(BaseModel):
    PrimaryValue: Optional[GaugeChartPrimaryValueConditionalFormattingTypeDef] = None
    Arc: Optional[GaugeChartArcConditionalFormattingTypeDef] = None

class KPIConditionalFormattingOptionTypeDef(BaseModel):
    PrimaryValue: Optional[KPIPrimaryValueConditionalFormattingTypeDef] = None
    ProgressBar: Optional[KPIProgressBarConditionalFormattingTypeDef] = None
    ActualValue: Optional[KPIActualValueConditionalFormattingTypeDef] = None
    ComparisonValue: Optional[KPIComparisonValueConditionalFormattingTypeDef] = None

class FilledMapShapeConditionalFormattingTypeDef(BaseModel):
    FieldId: str
    Format: Optional[ShapeConditionalFormatTypeDef] = None

class PivotTableCellConditionalFormattingTypeDef(BaseModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatTypeDef] = None
    Scope: Optional[PivotTableConditionalFormattingScopeTypeDef] = None
    Scopes: Optional[Sequence[PivotTableConditionalFormattingScopeTypeDef]] = None

class TableCellConditionalFormattingTypeDef(BaseModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatTypeDef] = None

class ThemeTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ThemeId: Optional[str] = None
    Version: Optional[ThemeVersionTypeDef] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    Type: Optional[ThemeTypeType] = None

class GaugeChartOptionsTypeDef(BaseModel):
    PrimaryValueDisplayType: Optional[PrimaryValueDisplayTypeType] = None
    Comparison: Optional[ComparisonConfigurationTypeDef] = None
    ArcAxis: Optional[ArcAxisConfigurationTypeDef] = None
    Arc: Optional[ArcConfigurationTypeDef] = None
    PrimaryValueFontConfiguration: Optional[FontConfigurationTypeDef] = None

class KPIOptionsTypeDef(BaseModel):
    ProgressBar: Optional[ProgressBarOptionsTypeDef] = None
    TrendArrows: Optional[TrendArrowOptionsTypeDef] = None
    SecondaryValue: Optional[SecondaryValueOptionsTypeDef] = None
    Comparison: Optional[ComparisonConfigurationTypeDef] = None
    PrimaryValueDisplayType: Optional[PrimaryValueDisplayTypeType] = None
    PrimaryValueFontConfiguration: Optional[FontConfigurationTypeDef] = None
    SecondaryValueFontConfiguration: Optional[FontConfigurationTypeDef] = None
    Sparkline: Optional[KPISparklineOptionsTypeDef] = None
    VisualLayoutOptions: Optional[KPIVisualLayoutOptionsTypeDef] = None

class DateDimensionFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    DateGranularity: Optional[TimeGranularityType] = None
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[DateTimeFormatConfigurationTypeDef] = None

class DateMeasureFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    AggregationFunction: Optional[DateAggregationFunctionType] = None
    FormatConfiguration: Optional[DateTimeFormatConfigurationTypeDef] = None

class NumericalDimensionFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[NumberFormatConfigurationTypeDef] = None

class NumericalMeasureFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    AggregationFunction: Optional[NumericalAggregationFunctionTypeDef] = None
    FormatConfiguration: Optional[NumberFormatConfigurationTypeDef] = None

class ReferenceLineLabelConfigurationTypeDef(BaseModel):
    ValueLabelConfiguration: Optional[ReferenceLineValueLabelConfigurationTypeDef] = None
    CustomLabelConfiguration: Optional[ReferenceLineCustomLabelConfigurationTypeDef] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    FontColor: Optional[str] = None
    HorizontalPosition: Optional[ReferenceLineLabelHorizontalPositionType] = None
    VerticalPosition: Optional[ReferenceLineLabelVerticalPositionType] = None

class CategoricalDimensionFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[StringFormatConfigurationTypeDef] = None

class CategoricalMeasureFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    AggregationFunction: Optional[CategoricalAggregationFunctionType] = None
    FormatConfiguration: Optional[StringFormatConfigurationTypeDef] = None

class FormatConfigurationTypeDef(BaseModel):
    StringFormatConfiguration: Optional[StringFormatConfigurationTypeDef] = None
    NumberFormatConfiguration: Optional[NumberFormatConfigurationTypeDef] = None
    DateTimeFormatConfiguration: Optional[DateTimeFormatConfigurationTypeDef] = None

class BodySectionRepeatDimensionConfigurationOutputTypeDef(BaseModel):
    DynamicCategoryDimensionConfiguration: Optional[       BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef     ] = None
    DynamicNumericDimensionConfiguration: Optional[       BodySectionDynamicNumericDimensionConfigurationOutputTypeDef     ] = None

class BodySectionRepeatDimensionConfigurationTypeDef(BaseModel):
    DynamicCategoryDimensionConfiguration: Optional[       BodySectionDynamicCategoryDimensionConfigurationTypeDef     ] = None
    DynamicNumericDimensionConfiguration: Optional[       BodySectionDynamicNumericDimensionConfigurationTypeDef     ] = None

class BarChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[List[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class BarChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class BoxPlotSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class BoxPlotSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class ComboChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[List[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class ComboChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class FilledMapSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None

class FilledMapSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None

class FunnelChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class FunnelChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class HeatMapSortConfigurationOutputTypeDef(BaseModel):
    HeatMapRowSort: Optional[List[FieldSortOptionsTypeDef]] = None
    HeatMapColumnSort: Optional[List[FieldSortOptionsTypeDef]] = None
    HeatMapRowItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    HeatMapColumnItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class HeatMapSortConfigurationTypeDef(BaseModel):
    HeatMapRowSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    HeatMapColumnSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    HeatMapRowItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    HeatMapColumnItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class KPISortConfigurationOutputTypeDef(BaseModel):
    TrendGroupSort: Optional[List[FieldSortOptionsTypeDef]] = None

class KPISortConfigurationTypeDef(BaseModel):
    TrendGroupSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None

class LineChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class LineChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class PieChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class PieChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class RadarChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[List[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class RadarChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class SankeyDiagramSortConfigurationOutputTypeDef(BaseModel):
    WeightSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SourceItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    DestinationItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class SankeyDiagramSortConfigurationTypeDef(BaseModel):
    WeightSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SourceItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    DestinationItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class TableSortConfigurationOutputTypeDef(BaseModel):
    RowSort: Optional[List[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class TableSortConfigurationTypeDef(BaseModel):
    RowSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class TreeMapSortConfigurationOutputTypeDef(BaseModel):
    TreeMapSort: Optional[List[FieldSortOptionsTypeDef]] = None
    TreeMapGroupItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class TreeMapSortConfigurationTypeDef(BaseModel):
    TreeMapSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    TreeMapGroupItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class WaterfallChartSortConfigurationOutputTypeDef(BaseModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    BreakdownItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class WaterfallChartSortConfigurationTypeDef(BaseModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    BreakdownItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class WordCloudSortConfigurationOutputTypeDef(BaseModel):
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None

class WordCloudSortConfigurationTypeDef(BaseModel):
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None

class PivotFieldSortOptionsOutputTypeDef(BaseModel):
    FieldId: str
    SortBy: PivotTableSortByOutputTypeDef

class PivotFieldSortOptionsTypeDef(BaseModel):
    FieldId: str
    SortBy: PivotTableSortByTypeDef

class FieldBasedTooltipOutputTypeDef(BaseModel):
    AggregationVisibility: Optional[VisibilityType] = None
    TooltipTitleType: Optional[TooltipTitleTypeType] = None
    TooltipFields: Optional[List[TooltipItemTypeDef]] = None

class FieldBasedTooltipTypeDef(BaseModel):
    AggregationVisibility: Optional[VisibilityType] = None
    TooltipTitleType: Optional[TooltipTitleTypeType] = None
    TooltipFields: Optional[Sequence[TooltipItemTypeDef]] = None

class TopicDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None
    DataSets: Optional[List[DatasetMetadataOutputTypeDef]] = None

class TopicDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None
    DataSets: Optional[Sequence[DatasetMetadataTypeDef]] = None

class DescribeAssetBundleImportJobResponseTypeDef(BaseModel):
    JobStatus: AssetBundleImportJobStatusType
    Errors: List[AssetBundleImportJobErrorTypeDef]
    RollbackErrors: List[AssetBundleImportJobErrorTypeDef]
    Arn: str
    CreatedTime: datetime
    AssetBundleImportJobId: str
    AwsAccountId: str
    AssetBundleImportSource: AssetBundleImportSourceDescriptionTypeDef
    OverrideParameters: AssetBundleImportJobOverrideParametersOutputTypeDef
    FailureAction: AssetBundleImportFailureActionType
    RequestId: str
    Status: int
    OverridePermissions: AssetBundleImportJobOverridePermissionsOutputTypeDef
    OverrideTags: AssetBundleImportJobOverrideTagsOutputTypeDef
    OverrideValidationStrategy: AssetBundleImportJobOverrideValidationStrategyTypeDef
    Warnings: List[AssetBundleImportJobWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssetBundleImportJobRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AssetBundleImportJobId: str
    AssetBundleImportSource: AssetBundleImportSourceTypeDef
    OverrideParameters: Optional[AssetBundleImportJobOverrideParametersTypeDef] = None
    FailureAction: Optional[AssetBundleImportFailureActionType] = None
    OverridePermissions: Optional[AssetBundleImportJobOverridePermissionsTypeDef] = None
    OverrideTags: Optional[AssetBundleImportJobOverrideTagsTypeDef] = None
    OverrideValidationStrategy: Optional[       AssetBundleImportJobOverrideValidationStrategyTypeDef     ] = None

class CreateDataSourceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSourceId: str
    Name: str
    Type: DataSourceTypeType
    DataSourceParameters: Optional[DataSourceParametersTypeDef] = None
    Credentials: Optional[DataSourceCredentialsTypeDef] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FolderArns: Optional[Sequence[str]] = None

class UpdateDataSourceRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSourceId: str
    Name: str
    DataSourceParameters: Optional[DataSourceParametersTypeDef] = None
    Credentials: Optional[DataSourceCredentialsTypeDef] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None

class SnapshotJobResultTypeDef(BaseModel):
    AnonymousUsers: Optional[List[AnonymousUserSnapshotJobResultTypeDef]] = None

class DefaultNewSheetConfigurationTypeDef(BaseModel):
    InteractiveLayoutConfiguration: Optional[DefaultInteractiveLayoutConfigurationTypeDef] = None
    PaginatedLayoutConfiguration: Optional[DefaultPaginatedLayoutConfigurationTypeDef] = None
    SheetContentType: Optional[SheetContentTypeType] = None

class BodySectionContentOutputTypeDef(BaseModel):
    Layout: Optional[SectionLayoutConfigurationOutputTypeDef] = None

class HeaderFooterSectionConfigurationOutputTypeDef(BaseModel):
    SectionId: str
    Layout: SectionLayoutConfigurationOutputTypeDef
    Style: Optional[SectionStyleTypeDef] = None

class BodySectionContentTypeDef(BaseModel):
    Layout: Optional[SectionLayoutConfigurationTypeDef] = None

class HeaderFooterSectionConfigurationTypeDef(BaseModel):
    SectionId: str
    Layout: SectionLayoutConfigurationTypeDef
    Style: Optional[SectionStyleTypeDef] = None

class VisualCustomActionOperationTypeDef(BaseModel):
    FilterOperation: Optional[CustomActionFilterOperationTypeDef] = None
    NavigationOperation: Optional[CustomActionNavigationOperationTypeDef] = None
    URLOperation: Optional[CustomActionURLOperationTypeDef] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationTypeDef] = None

class DescribeDataSetResponseTypeDef(BaseModel):
    DataSet: DataSetTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    Name: str
    PhysicalTableMap: Mapping[str, PhysicalTableUnionTypeDef]
    ImportMode: DataSetImportModeType
    LogicalTableMap: Optional[Mapping[str, LogicalTableUnionTypeDef]] = None
    ColumnGroups: Optional[Sequence[ColumnGroupUnionTypeDef]] = None
    FieldFolders: Optional[Mapping[str, FieldFolderUnionTypeDef]] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSetTypeDef] = None
    RowLevelPermissionTagConfiguration: Optional[       RowLevelPermissionTagConfigurationTypeDef     ] = None
    ColumnLevelPermissionRules: Optional[Sequence[ColumnLevelPermissionRuleUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataSetUsageConfiguration: Optional[DataSetUsageConfigurationTypeDef] = None
    DatasetParameters: Optional[Sequence[DatasetParameterUnionTypeDef]] = None
    FolderArns: Optional[Sequence[str]] = None

class UpdateDataSetRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DataSetId: str
    Name: str
    PhysicalTableMap: Mapping[str, PhysicalTableUnionTypeDef]
    ImportMode: DataSetImportModeType
    LogicalTableMap: Optional[Mapping[str, LogicalTableUnionTypeDef]] = None
    ColumnGroups: Optional[Sequence[ColumnGroupUnionTypeDef]] = None
    FieldFolders: Optional[Mapping[str, FieldFolderUnionTypeDef]] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSetTypeDef] = None
    RowLevelPermissionTagConfiguration: Optional[       RowLevelPermissionTagConfigurationTypeDef     ] = None
    ColumnLevelPermissionRules: Optional[Sequence[ColumnLevelPermissionRuleUnionTypeDef]] = None
    DataSetUsageConfiguration: Optional[DataSetUsageConfigurationTypeDef] = None
    DatasetParameters: Optional[Sequence[DatasetParameterUnionTypeDef]] = None

class VisualCustomActionOutputTypeDef(BaseModel):
    CustomActionId: str
    Name: str
    Trigger: VisualCustomActionTriggerType
    ActionOperations: List[VisualCustomActionOperationOutputTypeDef]
    Status: Optional[WidgetStatusType] = None

class DefaultFilterControlConfigurationOutputTypeDef(BaseModel):
    Title: str
    ControlOptions: DefaultFilterControlOptionsOutputTypeDef

class DefaultFilterControlConfigurationTypeDef(BaseModel):
    Title: str
    ControlOptions: DefaultFilterControlOptionsTypeDef

class TableFieldOptionTypeDef(BaseModel):
    FieldId: str
    Width: Optional[str] = None
    CustomLabel: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    URLStyling: Optional[TableFieldURLConfigurationTypeDef] = None

class GaugeChartConditionalFormattingOutputTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       List[GaugeChartConditionalFormattingOptionOutputTypeDef]     ] = None

class KPIConditionalFormattingOutputTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       List[KPIConditionalFormattingOptionOutputTypeDef]     ] = None

class FilledMapConditionalFormattingOptionOutputTypeDef(BaseModel):
    Shape: FilledMapShapeConditionalFormattingOutputTypeDef

class PivotTableConditionalFormattingOptionOutputTypeDef(BaseModel):
    Cell: Optional[PivotTableCellConditionalFormattingOutputTypeDef] = None

class TableConditionalFormattingOptionOutputTypeDef(BaseModel):
    Cell: Optional[TableCellConditionalFormattingOutputTypeDef] = None
    Row: Optional[TableRowConditionalFormattingOutputTypeDef] = None

class GaugeChartConditionalFormattingTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       Sequence[GaugeChartConditionalFormattingOptionTypeDef]     ] = None

class KPIConditionalFormattingTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       Sequence[KPIConditionalFormattingOptionTypeDef]     ] = None

class FilledMapConditionalFormattingOptionTypeDef(BaseModel):
    Shape: FilledMapShapeConditionalFormattingTypeDef

class PivotTableConditionalFormattingOptionTypeDef(BaseModel):
    Cell: Optional[PivotTableCellConditionalFormattingTypeDef] = None

class TableConditionalFormattingOptionTypeDef(BaseModel):
    Cell: Optional[TableCellConditionalFormattingTypeDef] = None
    Row: Optional[TableRowConditionalFormattingTypeDef] = None

class DescribeThemeResponseTypeDef(BaseModel):
    Theme: ThemeTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReferenceLineTypeDef(BaseModel):
    DataConfiguration: ReferenceLineDataConfigurationTypeDef
    Status: Optional[WidgetStatusType] = None
    StyleConfiguration: Optional[ReferenceLineStyleConfigurationTypeDef] = None
    LabelConfiguration: Optional[ReferenceLineLabelConfigurationTypeDef] = None

class DimensionFieldTypeDef(BaseModel):
    NumericalDimensionField: Optional[NumericalDimensionFieldTypeDef] = None
    CategoricalDimensionField: Optional[CategoricalDimensionFieldTypeDef] = None
    DateDimensionField: Optional[DateDimensionFieldTypeDef] = None

class MeasureFieldTypeDef(BaseModel):
    NumericalMeasureField: Optional[NumericalMeasureFieldTypeDef] = None
    CategoricalMeasureField: Optional[CategoricalMeasureFieldTypeDef] = None
    DateMeasureField: Optional[DateMeasureFieldTypeDef] = None
    CalculatedMeasureField: Optional[CalculatedMeasureFieldTypeDef] = None

class ColumnConfigurationOutputTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    FormatConfiguration: Optional[FormatConfigurationTypeDef] = None
    Role: Optional[ColumnRoleType] = None
    ColorsConfiguration: Optional[ColorsConfigurationOutputTypeDef] = None

class ColumnConfigurationTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    FormatConfiguration: Optional[FormatConfigurationTypeDef] = None
    Role: Optional[ColumnRoleType] = None
    ColorsConfiguration: Optional[ColorsConfigurationTypeDef] = None

class UnaggregatedFieldTypeDef(BaseModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    FormatConfiguration: Optional[FormatConfigurationTypeDef] = None

class BodySectionRepeatConfigurationOutputTypeDef(BaseModel):
    DimensionConfigurations: Optional[       List[BodySectionRepeatDimensionConfigurationOutputTypeDef]     ] = None
    PageBreakConfiguration: Optional[BodySectionRepeatPageBreakConfigurationTypeDef] = None
    NonRepeatingVisuals: Optional[List[str]] = None

class BodySectionRepeatConfigurationTypeDef(BaseModel):
    DimensionConfigurations: Optional[       Sequence[BodySectionRepeatDimensionConfigurationTypeDef]     ] = None
    PageBreakConfiguration: Optional[BodySectionRepeatPageBreakConfigurationTypeDef] = None
    NonRepeatingVisuals: Optional[Sequence[str]] = None

class PivotTableSortConfigurationOutputTypeDef(BaseModel):
    FieldSortOptions: Optional[List[PivotFieldSortOptionsOutputTypeDef]] = None

class PivotTableSortConfigurationTypeDef(BaseModel):
    FieldSortOptions: Optional[Sequence[PivotFieldSortOptionsTypeDef]] = None

class TooltipOptionsOutputTypeDef(BaseModel):
    TooltipVisibility: Optional[VisibilityType] = None
    SelectedTooltipType: Optional[SelectedTooltipTypeType] = None
    FieldBasedTooltip: Optional[FieldBasedTooltipOutputTypeDef] = None

class TooltipOptionsTypeDef(BaseModel):
    TooltipVisibility: Optional[VisibilityType] = None
    SelectedTooltipType: Optional[SelectedTooltipTypeType] = None
    FieldBasedTooltip: Optional[FieldBasedTooltipTypeDef] = None

class DescribeTopicResponseTypeDef(BaseModel):
    Arn: str
    TopicId: str
    Topic: TopicDetailsOutputTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    Topic: TopicDetailsTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateTopicRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TopicId: str
    Topic: TopicDetailsTypeDef

class DescribeDashboardSnapshotJobResultResponseTypeDef(BaseModel):
    Arn: str
    JobStatus: SnapshotJobStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Result: SnapshotJobResultTypeDef
    ErrorInfo: SnapshotJobErrorInfoTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisDefaultsTypeDef(BaseModel):
    DefaultNewSheetConfiguration: DefaultNewSheetConfigurationTypeDef

class VisualCustomActionTypeDef(BaseModel):
    CustomActionId: str
    Name: str
    Trigger: VisualCustomActionTriggerType
    ActionOperations: Sequence[VisualCustomActionOperationTypeDef]
    Status: Optional[WidgetStatusType] = None

class CustomContentVisualOutputTypeDef(BaseModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[CustomContentConfigurationTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class EmptyVisualOutputTypeDef(BaseModel):
    VisualId: str
    DataSetIdentifier: str
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class CategoryFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationOutputTypeDef
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class CategoryInnerFilterOutputTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationOutputTypeDef
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class NumericEqualityFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    MatchOperator: NumericEqualityMatchOperatorType
    NullOption: FilterNullOptionType
    Value: Optional[float] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class NumericRangeFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimum: Optional[NumericRangeFilterValueTypeDef] = None
    RangeMaximum: Optional[NumericRangeFilterValueTypeDef] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class RelativeDatesFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    AnchorDateConfiguration: AnchorDateConfigurationTypeDef
    TimeGranularity: TimeGranularityType
    RelativeDateType: RelativeDateTypeType
    NullOption: FilterNullOptionType
    MinimumGranularity: Optional[TimeGranularityType] = None
    RelativeDateValue: Optional[int] = None
    ParameterName: Optional[str] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfigurationTypeDef] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class TimeEqualityFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Value: Optional[datetime] = None
    ParameterName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class TimeRangeFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimumValue: Optional[TimeRangeFilterValueOutputTypeDef] = None
    RangeMaximumValue: Optional[TimeRangeFilterValueOutputTypeDef] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfigurationTypeDef] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class TopBottomFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    AggregationSortConfigurations: List[AggregationSortConfigurationTypeDef]
    Limit: Optional[int] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class CategoryFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationTypeDef
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class CategoryInnerFilterTypeDef(BaseModel):
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationTypeDef
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class NumericEqualityFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    MatchOperator: NumericEqualityMatchOperatorType
    NullOption: FilterNullOptionType
    Value: Optional[float] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class NumericRangeFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimum: Optional[NumericRangeFilterValueTypeDef] = None
    RangeMaximum: Optional[NumericRangeFilterValueTypeDef] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class RelativeDatesFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    AnchorDateConfiguration: AnchorDateConfigurationTypeDef
    TimeGranularity: TimeGranularityType
    RelativeDateType: RelativeDateTypeType
    NullOption: FilterNullOptionType
    MinimumGranularity: Optional[TimeGranularityType] = None
    RelativeDateValue: Optional[int] = None
    ParameterName: Optional[str] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfigurationTypeDef] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class TimeEqualityFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Value: Optional[TimestampTypeDef] = None
    ParameterName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class TimeRangeFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    NullOption: FilterNullOptionType
    IncludeMinimum: Optional[bool] = None
    IncludeMaximum: Optional[bool] = None
    RangeMinimumValue: Optional[TimeRangeFilterValueTypeDef] = None
    RangeMaximumValue: Optional[TimeRangeFilterValueTypeDef] = None
    ExcludePeriodConfiguration: Optional[ExcludePeriodConfigurationTypeDef] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class TopBottomFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    AggregationSortConfigurations: Sequence[AggregationSortConfigurationTypeDef]
    Limit: Optional[int] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class TableFieldOptionsOutputTypeDef(BaseModel):
    SelectedFieldOptions: Optional[List[TableFieldOptionTypeDef]] = None
    Order: Optional[List[str]] = None
    PinnedFieldOptions: Optional[TablePinnedFieldOptionsOutputTypeDef] = None

class TableFieldOptionsTypeDef(BaseModel):
    SelectedFieldOptions: Optional[Sequence[TableFieldOptionTypeDef]] = None
    Order: Optional[Sequence[str]] = None
    PinnedFieldOptions: Optional[TablePinnedFieldOptionsTypeDef] = None

class FilledMapConditionalFormattingOutputTypeDef(BaseModel):
    ConditionalFormattingOptions: List[FilledMapConditionalFormattingOptionOutputTypeDef]

class PivotTableConditionalFormattingOutputTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       List[PivotTableConditionalFormattingOptionOutputTypeDef]     ] = None

class TableConditionalFormattingOutputTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       List[TableConditionalFormattingOptionOutputTypeDef]     ] = None

class FilledMapConditionalFormattingTypeDef(BaseModel):
    ConditionalFormattingOptions: Sequence[FilledMapConditionalFormattingOptionTypeDef]

class PivotTableConditionalFormattingTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       Sequence[PivotTableConditionalFormattingOptionTypeDef]     ] = None

class TableConditionalFormattingTypeDef(BaseModel):
    ConditionalFormattingOptions: Optional[       Sequence[TableConditionalFormattingOptionTypeDef]     ] = None

class UniqueValuesComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Category: Optional[DimensionFieldTypeDef] = None

class BarChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[List[DimensionFieldTypeDef]] = None

class BarChartAggregatedFieldWellsTypeDef(BaseModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[Sequence[DimensionFieldTypeDef]] = None

class BoxPlotAggregatedFieldWellsOutputTypeDef(BaseModel):
    GroupBy: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class BoxPlotAggregatedFieldWellsTypeDef(BaseModel):
    GroupBy: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class ComboChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    BarValues: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None
    LineValues: Optional[List[MeasureFieldTypeDef]] = None

class ComboChartAggregatedFieldWellsTypeDef(BaseModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    BarValues: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None
    LineValues: Optional[Sequence[MeasureFieldTypeDef]] = None

class FilledMapAggregatedFieldWellsOutputTypeDef(BaseModel):
    Geospatial: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class FilledMapAggregatedFieldWellsTypeDef(BaseModel):
    Geospatial: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class ForecastComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    PeriodsForward: Optional[int] = None
    PeriodsBackward: Optional[int] = None
    UpperBoundary: Optional[float] = None
    LowerBoundary: Optional[float] = None
    PredictionInterval: Optional[int] = None
    Seasonality: Optional[ForecastComputationSeasonalityType] = None
    CustomSeasonalityValue: Optional[int] = None

class FunnelChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class FunnelChartAggregatedFieldWellsTypeDef(BaseModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class GaugeChartFieldWellsOutputTypeDef(BaseModel):
    Values: Optional[List[MeasureFieldTypeDef]] = None
    TargetValues: Optional[List[MeasureFieldTypeDef]] = None

class GaugeChartFieldWellsTypeDef(BaseModel):
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    TargetValues: Optional[Sequence[MeasureFieldTypeDef]] = None

class GeospatialMapAggregatedFieldWellsOutputTypeDef(BaseModel):
    Geospatial: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None

class GeospatialMapAggregatedFieldWellsTypeDef(BaseModel):
    Geospatial: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None

class GrowthRateComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    PeriodSize: Optional[int] = None

class HeatMapAggregatedFieldWellsOutputTypeDef(BaseModel):
    Rows: Optional[List[DimensionFieldTypeDef]] = None
    Columns: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class HeatMapAggregatedFieldWellsTypeDef(BaseModel):
    Rows: Optional[Sequence[DimensionFieldTypeDef]] = None
    Columns: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class HistogramAggregatedFieldWellsOutputTypeDef(BaseModel):
    Values: Optional[List[MeasureFieldTypeDef]] = None

class HistogramAggregatedFieldWellsTypeDef(BaseModel):
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class KPIFieldWellsOutputTypeDef(BaseModel):
    Values: Optional[List[MeasureFieldTypeDef]] = None
    TargetValues: Optional[List[MeasureFieldTypeDef]] = None
    TrendGroups: Optional[List[DimensionFieldTypeDef]] = None

class KPIFieldWellsTypeDef(BaseModel):
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    TargetValues: Optional[Sequence[MeasureFieldTypeDef]] = None
    TrendGroups: Optional[Sequence[DimensionFieldTypeDef]] = None

class LineChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[List[DimensionFieldTypeDef]] = None

class LineChartAggregatedFieldWellsTypeDef(BaseModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[Sequence[DimensionFieldTypeDef]] = None

class MaximumMinimumComputationTypeDef(BaseModel):
    ComputationId: str
    Type: MaximumMinimumComputationTypeType
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None

class MetricComparisonComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    FromValue: Optional[MeasureFieldTypeDef] = None
    TargetValue: Optional[MeasureFieldTypeDef] = None

class PeriodOverPeriodComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None

class PeriodToDateComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    PeriodTimeGranularity: Optional[TimeGranularityType] = None

class PieChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    SmallMultiples: Optional[List[DimensionFieldTypeDef]] = None

class PieChartAggregatedFieldWellsTypeDef(BaseModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    SmallMultiples: Optional[Sequence[DimensionFieldTypeDef]] = None

class PivotTableAggregatedFieldWellsOutputTypeDef(BaseModel):
    Rows: Optional[List[DimensionFieldTypeDef]] = None
    Columns: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class PivotTableAggregatedFieldWellsTypeDef(BaseModel):
    Rows: Optional[Sequence[DimensionFieldTypeDef]] = None
    Columns: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class RadarChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Color: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class RadarChartAggregatedFieldWellsTypeDef(BaseModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Color: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class SankeyDiagramAggregatedFieldWellsOutputTypeDef(BaseModel):
    Source: Optional[List[DimensionFieldTypeDef]] = None
    Destination: Optional[List[DimensionFieldTypeDef]] = None
    Weight: Optional[List[MeasureFieldTypeDef]] = None

class SankeyDiagramAggregatedFieldWellsTypeDef(BaseModel):
    Source: Optional[Sequence[DimensionFieldTypeDef]] = None
    Destination: Optional[Sequence[DimensionFieldTypeDef]] = None
    Weight: Optional[Sequence[MeasureFieldTypeDef]] = None

class ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef(BaseModel):
    XAxis: Optional[List[MeasureFieldTypeDef]] = None
    YAxis: Optional[List[MeasureFieldTypeDef]] = None
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Size: Optional[List[MeasureFieldTypeDef]] = None
    Label: Optional[List[DimensionFieldTypeDef]] = None

class ScatterPlotCategoricallyAggregatedFieldWellsTypeDef(BaseModel):
    XAxis: Optional[Sequence[MeasureFieldTypeDef]] = None
    YAxis: Optional[Sequence[MeasureFieldTypeDef]] = None
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Size: Optional[Sequence[MeasureFieldTypeDef]] = None
    Label: Optional[Sequence[DimensionFieldTypeDef]] = None

class ScatterPlotUnaggregatedFieldWellsOutputTypeDef(BaseModel):
    XAxis: Optional[List[DimensionFieldTypeDef]] = None
    YAxis: Optional[List[DimensionFieldTypeDef]] = None
    Size: Optional[List[MeasureFieldTypeDef]] = None
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Label: Optional[List[DimensionFieldTypeDef]] = None

class ScatterPlotUnaggregatedFieldWellsTypeDef(BaseModel):
    XAxis: Optional[Sequence[DimensionFieldTypeDef]] = None
    YAxis: Optional[Sequence[DimensionFieldTypeDef]] = None
    Size: Optional[Sequence[MeasureFieldTypeDef]] = None
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Label: Optional[Sequence[DimensionFieldTypeDef]] = None

class TableAggregatedFieldWellsOutputTypeDef(BaseModel):
    GroupBy: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class TableAggregatedFieldWellsTypeDef(BaseModel):
    GroupBy: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class TopBottomMoversComputationTypeDef(BaseModel):
    ComputationId: str
    Type: TopBottomComputationTypeType
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Category: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    MoverSize: Optional[int] = None
    SortOrder: Optional[TopBottomSortOrderType] = None

class TopBottomRankedComputationTypeDef(BaseModel):
    ComputationId: str
    Type: TopBottomComputationTypeType
    Name: Optional[str] = None
    Category: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    ResultSize: Optional[int] = None

class TotalAggregationComputationTypeDef(BaseModel):
    ComputationId: str
    Name: Optional[str] = None
    Value: Optional[MeasureFieldTypeDef] = None

class TreeMapAggregatedFieldWellsOutputTypeDef(BaseModel):
    Groups: Optional[List[DimensionFieldTypeDef]] = None
    Sizes: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[MeasureFieldTypeDef]] = None

class TreeMapAggregatedFieldWellsTypeDef(BaseModel):
    Groups: Optional[Sequence[DimensionFieldTypeDef]] = None
    Sizes: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[MeasureFieldTypeDef]] = None

class WaterfallChartAggregatedFieldWellsOutputTypeDef(BaseModel):
    Categories: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Breakdowns: Optional[List[DimensionFieldTypeDef]] = None

class WaterfallChartAggregatedFieldWellsTypeDef(BaseModel):
    Categories: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Breakdowns: Optional[Sequence[DimensionFieldTypeDef]] = None

class WordCloudAggregatedFieldWellsOutputTypeDef(BaseModel):
    GroupBy: Optional[List[DimensionFieldTypeDef]] = None
    Size: Optional[List[MeasureFieldTypeDef]] = None

class WordCloudAggregatedFieldWellsTypeDef(BaseModel):
    GroupBy: Optional[Sequence[DimensionFieldTypeDef]] = None
    Size: Optional[Sequence[MeasureFieldTypeDef]] = None

class TableUnaggregatedFieldWellsOutputTypeDef(BaseModel):
    Values: Optional[List[UnaggregatedFieldTypeDef]] = None

class TableUnaggregatedFieldWellsTypeDef(BaseModel):
    Values: Optional[Sequence[UnaggregatedFieldTypeDef]] = None

class BodySectionConfigurationOutputTypeDef(BaseModel):
    SectionId: str
    Content: BodySectionContentOutputTypeDef
    Style: Optional[SectionStyleTypeDef] = None
    PageBreakConfiguration: Optional[SectionPageBreakConfigurationTypeDef] = None
    RepeatConfiguration: Optional[BodySectionRepeatConfigurationOutputTypeDef] = None

class BodySectionConfigurationTypeDef(BaseModel):
    SectionId: str
    Content: BodySectionContentTypeDef
    Style: Optional[SectionStyleTypeDef] = None
    PageBreakConfiguration: Optional[SectionPageBreakConfigurationTypeDef] = None
    RepeatConfiguration: Optional[BodySectionRepeatConfigurationTypeDef] = None

class CustomContentVisualTypeDef(BaseModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[CustomContentConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class EmptyVisualTypeDef(BaseModel):
    VisualId: str
    DataSetIdentifier: str
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class InnerFilterOutputTypeDef(BaseModel):
    CategoryInnerFilter: Optional[CategoryInnerFilterOutputTypeDef] = None

class InnerFilterTypeDef(BaseModel):
    CategoryInnerFilter: Optional[CategoryInnerFilterTypeDef] = None

class BarChartFieldWellsOutputTypeDef(BaseModel):
    BarChartAggregatedFieldWells: Optional[BarChartAggregatedFieldWellsOutputTypeDef] = None

class BarChartFieldWellsTypeDef(BaseModel):
    BarChartAggregatedFieldWells: Optional[BarChartAggregatedFieldWellsTypeDef] = None

class BoxPlotFieldWellsOutputTypeDef(BaseModel):
    BoxPlotAggregatedFieldWells: Optional[BoxPlotAggregatedFieldWellsOutputTypeDef] = None

class BoxPlotFieldWellsTypeDef(BaseModel):
    BoxPlotAggregatedFieldWells: Optional[BoxPlotAggregatedFieldWellsTypeDef] = None

class ComboChartFieldWellsOutputTypeDef(BaseModel):
    ComboChartAggregatedFieldWells: Optional[ComboChartAggregatedFieldWellsOutputTypeDef] = None

class ComboChartFieldWellsTypeDef(BaseModel):
    ComboChartAggregatedFieldWells: Optional[ComboChartAggregatedFieldWellsTypeDef] = None

class FilledMapFieldWellsOutputTypeDef(BaseModel):
    FilledMapAggregatedFieldWells: Optional[FilledMapAggregatedFieldWellsOutputTypeDef] = None

class FilledMapFieldWellsTypeDef(BaseModel):
    FilledMapAggregatedFieldWells: Optional[FilledMapAggregatedFieldWellsTypeDef] = None

class FunnelChartFieldWellsOutputTypeDef(BaseModel):
    FunnelChartAggregatedFieldWells: Optional[       FunnelChartAggregatedFieldWellsOutputTypeDef     ] = None

class FunnelChartFieldWellsTypeDef(BaseModel):
    FunnelChartAggregatedFieldWells: Optional[FunnelChartAggregatedFieldWellsTypeDef] = None

class GaugeChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[GaugeChartFieldWellsOutputTypeDef] = None
    GaugeChartOptions: Optional[GaugeChartOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    TooltipOptions: Optional[TooltipOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    ColorConfiguration: Optional[GaugeChartColorConfigurationTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GaugeChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[GaugeChartFieldWellsTypeDef] = None
    GaugeChartOptions: Optional[GaugeChartOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    TooltipOptions: Optional[TooltipOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    ColorConfiguration: Optional[GaugeChartColorConfigurationTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GeospatialMapFieldWellsOutputTypeDef(BaseModel):
    GeospatialMapAggregatedFieldWells: Optional[       GeospatialMapAggregatedFieldWellsOutputTypeDef     ] = None

class GeospatialMapFieldWellsTypeDef(BaseModel):
    GeospatialMapAggregatedFieldWells: Optional[GeospatialMapAggregatedFieldWellsTypeDef] = None

class HeatMapFieldWellsOutputTypeDef(BaseModel):
    HeatMapAggregatedFieldWells: Optional[HeatMapAggregatedFieldWellsOutputTypeDef] = None

class HeatMapFieldWellsTypeDef(BaseModel):
    HeatMapAggregatedFieldWells: Optional[HeatMapAggregatedFieldWellsTypeDef] = None

class HistogramFieldWellsOutputTypeDef(BaseModel):
    HistogramAggregatedFieldWells: Optional[HistogramAggregatedFieldWellsOutputTypeDef] = None

class HistogramFieldWellsTypeDef(BaseModel):
    HistogramAggregatedFieldWells: Optional[HistogramAggregatedFieldWellsTypeDef] = None

class KPIConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[KPIFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[KPISortConfigurationOutputTypeDef] = None
    KPIOptions: Optional[KPIOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class KPIConfigurationTypeDef(BaseModel):
    FieldWells: Optional[KPIFieldWellsTypeDef] = None
    SortConfiguration: Optional[KPISortConfigurationTypeDef] = None
    KPIOptions: Optional[KPIOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class LineChartFieldWellsOutputTypeDef(BaseModel):
    LineChartAggregatedFieldWells: Optional[LineChartAggregatedFieldWellsOutputTypeDef] = None

class LineChartFieldWellsTypeDef(BaseModel):
    LineChartAggregatedFieldWells: Optional[LineChartAggregatedFieldWellsTypeDef] = None

class PieChartFieldWellsOutputTypeDef(BaseModel):
    PieChartAggregatedFieldWells: Optional[PieChartAggregatedFieldWellsOutputTypeDef] = None

class PieChartFieldWellsTypeDef(BaseModel):
    PieChartAggregatedFieldWells: Optional[PieChartAggregatedFieldWellsTypeDef] = None

class PivotTableFieldWellsOutputTypeDef(BaseModel):
    PivotTableAggregatedFieldWells: Optional[PivotTableAggregatedFieldWellsOutputTypeDef] = None

class PivotTableFieldWellsTypeDef(BaseModel):
    PivotTableAggregatedFieldWells: Optional[PivotTableAggregatedFieldWellsTypeDef] = None

class RadarChartFieldWellsOutputTypeDef(BaseModel):
    RadarChartAggregatedFieldWells: Optional[RadarChartAggregatedFieldWellsOutputTypeDef] = None

class RadarChartFieldWellsTypeDef(BaseModel):
    RadarChartAggregatedFieldWells: Optional[RadarChartAggregatedFieldWellsTypeDef] = None

class SankeyDiagramFieldWellsOutputTypeDef(BaseModel):
    SankeyDiagramAggregatedFieldWells: Optional[       SankeyDiagramAggregatedFieldWellsOutputTypeDef     ] = None

class SankeyDiagramFieldWellsTypeDef(BaseModel):
    SankeyDiagramAggregatedFieldWells: Optional[SankeyDiagramAggregatedFieldWellsTypeDef] = None

class ScatterPlotFieldWellsOutputTypeDef(BaseModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional[       ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef     ] = None
    ScatterPlotUnaggregatedFieldWells: Optional[       ScatterPlotUnaggregatedFieldWellsOutputTypeDef     ] = None

class ScatterPlotFieldWellsTypeDef(BaseModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional[       ScatterPlotCategoricallyAggregatedFieldWellsTypeDef     ] = None
    ScatterPlotUnaggregatedFieldWells: Optional[ScatterPlotUnaggregatedFieldWellsTypeDef] = None

class ComputationTypeDef(BaseModel):
    TopBottomRanked: Optional[TopBottomRankedComputationTypeDef] = None
    TopBottomMovers: Optional[TopBottomMoversComputationTypeDef] = None
    TotalAggregation: Optional[TotalAggregationComputationTypeDef] = None
    MaximumMinimum: Optional[MaximumMinimumComputationTypeDef] = None
    MetricComparison: Optional[MetricComparisonComputationTypeDef] = None
    PeriodOverPeriod: Optional[PeriodOverPeriodComputationTypeDef] = None
    PeriodToDate: Optional[PeriodToDateComputationTypeDef] = None
    GrowthRate: Optional[GrowthRateComputationTypeDef] = None
    UniqueValues: Optional[UniqueValuesComputationTypeDef] = None
    Forecast: Optional[ForecastComputationTypeDef] = None

class TreeMapFieldWellsOutputTypeDef(BaseModel):
    TreeMapAggregatedFieldWells: Optional[TreeMapAggregatedFieldWellsOutputTypeDef] = None

class TreeMapFieldWellsTypeDef(BaseModel):
    TreeMapAggregatedFieldWells: Optional[TreeMapAggregatedFieldWellsTypeDef] = None

class WaterfallChartFieldWellsOutputTypeDef(BaseModel):
    WaterfallChartAggregatedFieldWells: Optional[       WaterfallChartAggregatedFieldWellsOutputTypeDef     ] = None

class WaterfallChartFieldWellsTypeDef(BaseModel):
    WaterfallChartAggregatedFieldWells: Optional[       WaterfallChartAggregatedFieldWellsTypeDef     ] = None

class WordCloudFieldWellsOutputTypeDef(BaseModel):
    WordCloudAggregatedFieldWells: Optional[WordCloudAggregatedFieldWellsOutputTypeDef] = None

class WordCloudFieldWellsTypeDef(BaseModel):
    WordCloudAggregatedFieldWells: Optional[WordCloudAggregatedFieldWellsTypeDef] = None

class TableFieldWellsOutputTypeDef(BaseModel):
    TableAggregatedFieldWells: Optional[TableAggregatedFieldWellsOutputTypeDef] = None
    TableUnaggregatedFieldWells: Optional[TableUnaggregatedFieldWellsOutputTypeDef] = None

class TableFieldWellsTypeDef(BaseModel):
    TableAggregatedFieldWells: Optional[TableAggregatedFieldWellsTypeDef] = None
    TableUnaggregatedFieldWells: Optional[TableUnaggregatedFieldWellsTypeDef] = None

class SectionBasedLayoutConfigurationOutputTypeDef(BaseModel):
    HeaderSections: List[HeaderFooterSectionConfigurationOutputTypeDef]
    BodySections: List[BodySectionConfigurationOutputTypeDef]
    FooterSections: List[HeaderFooterSectionConfigurationOutputTypeDef]
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptionsTypeDef

class SectionBasedLayoutConfigurationTypeDef(BaseModel):
    HeaderSections: Sequence[HeaderFooterSectionConfigurationTypeDef]
    BodySections: Sequence[BodySectionConfigurationTypeDef]
    FooterSections: Sequence[HeaderFooterSectionConfigurationTypeDef]
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptionsTypeDef

class NestedFilterOutputTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    IncludeInnerSet: bool
    InnerFilter: InnerFilterOutputTypeDef

class NestedFilterTypeDef(BaseModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    IncludeInnerSet: bool
    InnerFilter: InnerFilterTypeDef

class BarChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[BarChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[BarChartSortConfigurationOutputTypeDef] = None
    Orientation: Optional[BarChartOrientationType] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptionsTypeDef] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ValueAxis: Optional[AxisDisplayOptionsOutputTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    ReferenceLines: Optional[List[ReferenceLineTypeDef]] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefaultOutputTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class BarChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[BarChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[BarChartSortConfigurationTypeDef] = None
    Orientation: Optional[BarChartOrientationType] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptionsTypeDef] = None
    CategoryAxis: Optional[AxisDisplayOptionsTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ValueAxis: Optional[AxisDisplayOptionsTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    ReferenceLines: Optional[Sequence[ReferenceLineTypeDef]] = None
    ContributionAnalysisDefaults: Optional[Sequence[ContributionAnalysisDefaultTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class BoxPlotChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[BoxPlotFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[BoxPlotSortConfigurationOutputTypeDef] = None
    BoxPlotOptions: Optional[BoxPlotOptionsTypeDef] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    ReferenceLines: Optional[List[ReferenceLineTypeDef]] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class BoxPlotChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[BoxPlotFieldWellsTypeDef] = None
    SortConfiguration: Optional[BoxPlotSortConfigurationTypeDef] = None
    BoxPlotOptions: Optional[BoxPlotOptionsTypeDef] = None
    CategoryAxis: Optional[AxisDisplayOptionsTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    ReferenceLines: Optional[Sequence[ReferenceLineTypeDef]] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class ComboChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[ComboChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[ComboChartSortConfigurationOutputTypeDef] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    SecondaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    SingleAxisOptions: Optional[SingleAxisOptionsTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    BarDataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    LineDataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    ReferenceLines: Optional[List[ReferenceLineTypeDef]] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class ComboChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[ComboChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[ComboChartSortConfigurationTypeDef] = None
    BarsArrangement: Optional[BarsArrangementType] = None
    CategoryAxis: Optional[AxisDisplayOptionsTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    SecondaryYAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    SingleAxisOptions: Optional[SingleAxisOptionsTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    BarDataLabels: Optional[DataLabelOptionsTypeDef] = None
    LineDataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    ReferenceLines: Optional[Sequence[ReferenceLineTypeDef]] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FilledMapConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[FilledMapFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[FilledMapSortConfigurationOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FilledMapConfigurationTypeDef(BaseModel):
    FieldWells: Optional[FilledMapFieldWellsTypeDef] = None
    SortConfiguration: Optional[FilledMapSortConfigurationTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FunnelChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[FunnelChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[FunnelChartSortConfigurationOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    DataLabelOptions: Optional[FunnelChartDataLabelOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FunnelChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[FunnelChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[FunnelChartSortConfigurationTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    DataLabelOptions: Optional[FunnelChartDataLabelOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GaugeChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GaugeChartConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[GaugeChartConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class GaugeChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GaugeChartConfigurationTypeDef] = None
    ConditionalFormatting: Optional[GaugeChartConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class GeospatialMapConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[GeospatialMapFieldWellsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    PointStyleOptions: Optional[GeospatialPointStyleOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GeospatialMapConfigurationTypeDef(BaseModel):
    FieldWells: Optional[GeospatialMapFieldWellsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    PointStyleOptions: Optional[GeospatialPointStyleOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HeatMapConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[HeatMapFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[HeatMapSortConfigurationOutputTypeDef] = None
    RowLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColumnLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColorScale: Optional[ColorScaleOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HeatMapConfigurationTypeDef(BaseModel):
    FieldWells: Optional[HeatMapFieldWellsTypeDef] = None
    SortConfiguration: Optional[HeatMapSortConfigurationTypeDef] = None
    RowLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColumnLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColorScale: Optional[ColorScaleTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HistogramConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[HistogramFieldWellsOutputTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    BinOptions: Optional[HistogramBinOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HistogramConfigurationTypeDef(BaseModel):
    FieldWells: Optional[HistogramFieldWellsTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    BinOptions: Optional[HistogramBinOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class KPIVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[KPIConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[KPIConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class KPIVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[KPIConfigurationTypeDef] = None
    ConditionalFormatting: Optional[KPIConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class LineChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[LineChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[LineChartSortConfigurationOutputTypeDef] = None
    ForecastConfigurations: Optional[List[ForecastConfigurationOutputTypeDef]] = None
    Type: Optional[LineChartTypeType] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptionsTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptionsOutputTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    SecondaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptionsOutputTypeDef] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    SingleAxisOptions: Optional[SingleAxisOptionsTypeDef] = None
    DefaultSeriesSettings: Optional[LineChartDefaultSeriesSettingsTypeDef] = None
    Series: Optional[List[SeriesItemTypeDef]] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    ReferenceLines: Optional[List[ReferenceLineTypeDef]] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefaultOutputTypeDef]] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class LineChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[LineChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[LineChartSortConfigurationTypeDef] = None
    ForecastConfigurations: Optional[Sequence[ForecastConfigurationTypeDef]] = None
    Type: Optional[LineChartTypeType] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptionsTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptionsTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    SecondaryYAxisDisplayOptions: Optional[LineSeriesAxisDisplayOptionsTypeDef] = None
    SecondaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    SingleAxisOptions: Optional[SingleAxisOptionsTypeDef] = None
    DefaultSeriesSettings: Optional[LineChartDefaultSeriesSettingsTypeDef] = None
    Series: Optional[Sequence[SeriesItemTypeDef]] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    ReferenceLines: Optional[Sequence[ReferenceLineTypeDef]] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    ContributionAnalysisDefaults: Optional[Sequence[ContributionAnalysisDefaultTypeDef]] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class PieChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[PieChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[PieChartSortConfigurationOutputTypeDef] = None
    DonutOptions: Optional[DonutOptionsTypeDef] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptionsTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    ContributionAnalysisDefaults: Optional[List[ContributionAnalysisDefaultOutputTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class PieChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[PieChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[PieChartSortConfigurationTypeDef] = None
    DonutOptions: Optional[DonutOptionsTypeDef] = None
    SmallMultiplesOptions: Optional[SmallMultiplesOptionsTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    ContributionAnalysisDefaults: Optional[Sequence[ContributionAnalysisDefaultTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class PivotTableConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[PivotTableFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[PivotTableSortConfigurationOutputTypeDef] = None
    TableOptions: Optional[PivotTableOptionsOutputTypeDef] = None
    TotalOptions: Optional[PivotTableTotalOptionsOutputTypeDef] = None
    FieldOptions: Optional[PivotTableFieldOptionsOutputTypeDef] = None
    PaginatedReportOptions: Optional[PivotTablePaginatedReportOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class PivotTableConfigurationTypeDef(BaseModel):
    FieldWells: Optional[PivotTableFieldWellsTypeDef] = None
    SortConfiguration: Optional[PivotTableSortConfigurationTypeDef] = None
    TableOptions: Optional[PivotTableOptionsTypeDef] = None
    TotalOptions: Optional[PivotTableTotalOptionsTypeDef] = None
    FieldOptions: Optional[PivotTableFieldOptionsTypeDef] = None
    PaginatedReportOptions: Optional[PivotTablePaginatedReportOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class RadarChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[RadarChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[RadarChartSortConfigurationOutputTypeDef] = None
    Shape: Optional[RadarChartShapeType] = None
    BaseSeriesSettings: Optional[RadarChartSeriesSettingsTypeDef] = None
    StartAngle: Optional[float] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    AlternateBandColorsVisibility: Optional[VisibilityType] = None
    AlternateBandEvenColor: Optional[str] = None
    AlternateBandOddColor: Optional[str] = None
    CategoryAxis: Optional[AxisDisplayOptionsOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColorAxis: Optional[AxisDisplayOptionsOutputTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    AxesRangeScale: Optional[RadarChartAxesRangeScaleType] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class RadarChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[RadarChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[RadarChartSortConfigurationTypeDef] = None
    Shape: Optional[RadarChartShapeType] = None
    BaseSeriesSettings: Optional[RadarChartSeriesSettingsTypeDef] = None
    StartAngle: Optional[float] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    AlternateBandColorsVisibility: Optional[VisibilityType] = None
    AlternateBandEvenColor: Optional[str] = None
    AlternateBandOddColor: Optional[str] = None
    CategoryAxis: Optional[AxisDisplayOptionsTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColorAxis: Optional[AxisDisplayOptionsTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    AxesRangeScale: Optional[RadarChartAxesRangeScaleType] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class SankeyDiagramChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[SankeyDiagramFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[SankeyDiagramSortConfigurationOutputTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class SankeyDiagramChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[SankeyDiagramFieldWellsTypeDef] = None
    SortConfiguration: Optional[SankeyDiagramSortConfigurationTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class ScatterPlotConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[ScatterPlotFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[ScatterPlotSortConfigurationTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    YAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class ScatterPlotConfigurationTypeDef(BaseModel):
    FieldWells: Optional[ScatterPlotFieldWellsTypeDef] = None
    SortConfiguration: Optional[ScatterPlotSortConfigurationTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    YAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class InsightConfigurationOutputTypeDef(BaseModel):
    Computations: Optional[List[ComputationTypeDef]] = None
    CustomNarrative: Optional[CustomNarrativeOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class InsightConfigurationTypeDef(BaseModel):
    Computations: Optional[Sequence[ComputationTypeDef]] = None
    CustomNarrative: Optional[CustomNarrativeOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TreeMapConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[TreeMapFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[TreeMapSortConfigurationOutputTypeDef] = None
    GroupLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    SizeLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColorScale: Optional[ColorScaleOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TreeMapConfigurationTypeDef(BaseModel):
    FieldWells: Optional[TreeMapFieldWellsTypeDef] = None
    SortConfiguration: Optional[TreeMapSortConfigurationTypeDef] = None
    GroupLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    SizeLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColorLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColorScale: Optional[ColorScaleTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class WaterfallChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[WaterfallChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[WaterfallChartSortConfigurationOutputTypeDef] = None
    WaterfallChartOptions: Optional[WaterfallChartOptionsTypeDef] = None
    CategoryAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    CategoryAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    ColorConfiguration: Optional[WaterfallChartColorConfigurationTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class WaterfallChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[WaterfallChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[WaterfallChartSortConfigurationTypeDef] = None
    WaterfallChartOptions: Optional[WaterfallChartOptionsTypeDef] = None
    CategoryAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    CategoryAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    PrimaryYAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    PrimaryYAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    ColorConfiguration: Optional[WaterfallChartColorConfigurationTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class WordCloudChartConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[WordCloudFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[WordCloudSortConfigurationOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    WordCloudOptions: Optional[WordCloudOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class WordCloudChartConfigurationTypeDef(BaseModel):
    FieldWells: Optional[WordCloudFieldWellsTypeDef] = None
    SortConfiguration: Optional[WordCloudSortConfigurationTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    WordCloudOptions: Optional[WordCloudOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TableConfigurationOutputTypeDef(BaseModel):
    FieldWells: Optional[TableFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[TableSortConfigurationOutputTypeDef] = None
    TableOptions: Optional[TableOptionsOutputTypeDef] = None
    TotalOptions: Optional[TotalOptionsOutputTypeDef] = None
    FieldOptions: Optional[TableFieldOptionsOutputTypeDef] = None
    PaginatedReportOptions: Optional[TablePaginatedReportOptionsTypeDef] = None
    TableInlineVisualizations: Optional[List[TableInlineVisualizationTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TableConfigurationTypeDef(BaseModel):
    FieldWells: Optional[TableFieldWellsTypeDef] = None
    SortConfiguration: Optional[TableSortConfigurationTypeDef] = None
    TableOptions: Optional[TableOptionsTypeDef] = None
    TotalOptions: Optional[TotalOptionsTypeDef] = None
    FieldOptions: Optional[TableFieldOptionsTypeDef] = None
    PaginatedReportOptions: Optional[TablePaginatedReportOptionsTypeDef] = None
    TableInlineVisualizations: Optional[Sequence[TableInlineVisualizationTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class LayoutConfigurationOutputTypeDef(BaseModel):
    GridLayout: Optional[GridLayoutConfigurationOutputTypeDef] = None
    FreeFormLayout: Optional[FreeFormLayoutConfigurationOutputTypeDef] = None
    SectionBasedLayout: Optional[SectionBasedLayoutConfigurationOutputTypeDef] = None

class LayoutConfigurationTypeDef(BaseModel):
    GridLayout: Optional[GridLayoutConfigurationTypeDef] = None
    FreeFormLayout: Optional[FreeFormLayoutConfigurationTypeDef] = None
    SectionBasedLayout: Optional[SectionBasedLayoutConfigurationTypeDef] = None

class FilterOutputTypeDef(BaseModel):
    CategoryFilter: Optional[CategoryFilterOutputTypeDef] = None
    NumericRangeFilter: Optional[NumericRangeFilterOutputTypeDef] = None
    NumericEqualityFilter: Optional[NumericEqualityFilterOutputTypeDef] = None
    TimeEqualityFilter: Optional[TimeEqualityFilterOutputTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeFilterOutputTypeDef] = None
    RelativeDatesFilter: Optional[RelativeDatesFilterOutputTypeDef] = None
    TopBottomFilter: Optional[TopBottomFilterOutputTypeDef] = None
    NestedFilter: Optional[NestedFilterOutputTypeDef] = None

class FilterTypeDef(BaseModel):
    CategoryFilter: Optional[CategoryFilterTypeDef] = None
    NumericRangeFilter: Optional[NumericRangeFilterTypeDef] = None
    NumericEqualityFilter: Optional[NumericEqualityFilterTypeDef] = None
    TimeEqualityFilter: Optional[TimeEqualityFilterTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeFilterTypeDef] = None
    RelativeDatesFilter: Optional[RelativeDatesFilterTypeDef] = None
    TopBottomFilter: Optional[TopBottomFilterTypeDef] = None
    NestedFilter: Optional[NestedFilterTypeDef] = None

class BarChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BarChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class BarChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BarChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class BoxPlotVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BoxPlotChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class BoxPlotVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BoxPlotChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class ComboChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ComboChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class ComboChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ComboChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class FilledMapVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FilledMapConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[FilledMapConditionalFormattingOutputTypeDef] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class FilledMapVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FilledMapConfigurationTypeDef] = None
    ConditionalFormatting: Optional[FilledMapConditionalFormattingTypeDef] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class FunnelChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FunnelChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class FunnelChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FunnelChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class GeospatialMapVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GeospatialMapConfigurationOutputTypeDef] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class GeospatialMapVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GeospatialMapConfigurationTypeDef] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class HeatMapVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HeatMapConfigurationOutputTypeDef] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class HeatMapVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HeatMapConfigurationTypeDef] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class HistogramVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HistogramConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class HistogramVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HistogramConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class LineChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[LineChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class LineChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[LineChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class PieChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PieChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class PieChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PieChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class PivotTableVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PivotTableConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[PivotTableConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class PivotTableVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PivotTableConfigurationTypeDef] = None
    ConditionalFormatting: Optional[PivotTableConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class RadarChartVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[RadarChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class RadarChartVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[RadarChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class SankeyDiagramVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[SankeyDiagramChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class SankeyDiagramVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[SankeyDiagramChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class ScatterPlotVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ScatterPlotConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class ScatterPlotVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ScatterPlotConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class InsightVisualOutputTypeDef(BaseModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    InsightConfiguration: Optional[InsightConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class InsightVisualTypeDef(BaseModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    InsightConfiguration: Optional[InsightConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class TreeMapVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TreeMapConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class TreeMapVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TreeMapConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class WaterfallVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WaterfallChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class WaterfallVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WaterfallChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class WordCloudVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WordCloudChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class WordCloudVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WordCloudChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class TableVisualOutputTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TableConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[TableConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class TableVisualTypeDef(BaseModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TableConfigurationTypeDef] = None
    ConditionalFormatting: Optional[TableConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class LayoutOutputTypeDef(BaseModel):
    Configuration: LayoutConfigurationOutputTypeDef

class LayoutTypeDef(BaseModel):
    Configuration: LayoutConfigurationTypeDef

class FilterGroupOutputTypeDef(BaseModel):
    FilterGroupId: str
    Filters: List[FilterOutputTypeDef]
    ScopeConfiguration: FilterScopeConfigurationOutputTypeDef
    CrossDataset: CrossDatasetTypesType
    Status: Optional[WidgetStatusType] = None

class FilterGroupTypeDef(BaseModel):
    FilterGroupId: str
    Filters: Sequence[FilterTypeDef]
    ScopeConfiguration: FilterScopeConfigurationTypeDef
    CrossDataset: CrossDatasetTypesType
    Status: Optional[WidgetStatusType] = None

class VisualOutputTypeDef(BaseModel):
    TableVisual: Optional[TableVisualOutputTypeDef] = None
    PivotTableVisual: Optional[PivotTableVisualOutputTypeDef] = None
    BarChartVisual: Optional[BarChartVisualOutputTypeDef] = None
    KPIVisual: Optional[KPIVisualOutputTypeDef] = None
    PieChartVisual: Optional[PieChartVisualOutputTypeDef] = None
    GaugeChartVisual: Optional[GaugeChartVisualOutputTypeDef] = None
    LineChartVisual: Optional[LineChartVisualOutputTypeDef] = None
    HeatMapVisual: Optional[HeatMapVisualOutputTypeDef] = None
    TreeMapVisual: Optional[TreeMapVisualOutputTypeDef] = None
    GeospatialMapVisual: Optional[GeospatialMapVisualOutputTypeDef] = None
    FilledMapVisual: Optional[FilledMapVisualOutputTypeDef] = None
    FunnelChartVisual: Optional[FunnelChartVisualOutputTypeDef] = None
    ScatterPlotVisual: Optional[ScatterPlotVisualOutputTypeDef] = None
    ComboChartVisual: Optional[ComboChartVisualOutputTypeDef] = None
    BoxPlotVisual: Optional[BoxPlotVisualOutputTypeDef] = None
    WaterfallVisual: Optional[WaterfallVisualOutputTypeDef] = None
    HistogramVisual: Optional[HistogramVisualOutputTypeDef] = None
    WordCloudVisual: Optional[WordCloudVisualOutputTypeDef] = None
    InsightVisual: Optional[InsightVisualOutputTypeDef] = None
    SankeyDiagramVisual: Optional[SankeyDiagramVisualOutputTypeDef] = None
    CustomContentVisual: Optional[CustomContentVisualOutputTypeDef] = None
    EmptyVisual: Optional[EmptyVisualOutputTypeDef] = None
    RadarChartVisual: Optional[RadarChartVisualOutputTypeDef] = None

class VisualTypeDef(BaseModel):
    TableVisual: Optional[TableVisualTypeDef] = None
    PivotTableVisual: Optional[PivotTableVisualTypeDef] = None
    BarChartVisual: Optional[BarChartVisualTypeDef] = None
    KPIVisual: Optional[KPIVisualTypeDef] = None
    PieChartVisual: Optional[PieChartVisualTypeDef] = None
    GaugeChartVisual: Optional[GaugeChartVisualTypeDef] = None
    LineChartVisual: Optional[LineChartVisualTypeDef] = None
    HeatMapVisual: Optional[HeatMapVisualTypeDef] = None
    TreeMapVisual: Optional[TreeMapVisualTypeDef] = None
    GeospatialMapVisual: Optional[GeospatialMapVisualTypeDef] = None
    FilledMapVisual: Optional[FilledMapVisualTypeDef] = None
    FunnelChartVisual: Optional[FunnelChartVisualTypeDef] = None
    ScatterPlotVisual: Optional[ScatterPlotVisualTypeDef] = None
    ComboChartVisual: Optional[ComboChartVisualTypeDef] = None
    BoxPlotVisual: Optional[BoxPlotVisualTypeDef] = None
    WaterfallVisual: Optional[WaterfallVisualTypeDef] = None
    HistogramVisual: Optional[HistogramVisualTypeDef] = None
    WordCloudVisual: Optional[WordCloudVisualTypeDef] = None
    InsightVisual: Optional[InsightVisualTypeDef] = None
    SankeyDiagramVisual: Optional[SankeyDiagramVisualTypeDef] = None
    CustomContentVisual: Optional[CustomContentVisualTypeDef] = None
    EmptyVisual: Optional[EmptyVisualTypeDef] = None
    RadarChartVisual: Optional[RadarChartVisualTypeDef] = None

class SheetDefinitionOutputTypeDef(BaseModel):
    SheetId: str
    Title: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ParameterControls: Optional[List[ParameterControlOutputTypeDef]] = None
    FilterControls: Optional[List[FilterControlOutputTypeDef]] = None
    Visuals: Optional[List[VisualOutputTypeDef]] = None
    TextBoxes: Optional[List[SheetTextBoxTypeDef]] = None
    Layouts: Optional[List[LayoutOutputTypeDef]] = None
    SheetControlLayouts: Optional[List[SheetControlLayoutOutputTypeDef]] = None
    ContentType: Optional[SheetContentTypeType] = None

class SheetDefinitionTypeDef(BaseModel):
    SheetId: str
    Title: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ParameterControls: Optional[Sequence[ParameterControlTypeDef]] = None
    FilterControls: Optional[Sequence[FilterControlTypeDef]] = None
    Visuals: Optional[Sequence[VisualTypeDef]] = None
    TextBoxes: Optional[Sequence[SheetTextBoxTypeDef]] = None
    Layouts: Optional[Sequence[LayoutTypeDef]] = None
    SheetControlLayouts: Optional[Sequence[SheetControlLayoutTypeDef]] = None
    ContentType: Optional[SheetContentTypeType] = None

class AnalysisDefinitionOutputTypeDef(BaseModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[List[SheetDefinitionOutputTypeDef]] = None
    CalculatedFields: Optional[List[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutputTypeDef]] = None
    FilterGroups: Optional[List[FilterGroupOutputTypeDef]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutputTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class DashboardVersionDefinitionOutputTypeDef(BaseModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[List[SheetDefinitionOutputTypeDef]] = None
    CalculatedFields: Optional[List[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutputTypeDef]] = None
    FilterGroups: Optional[List[FilterGroupOutputTypeDef]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutputTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class TemplateVersionDefinitionOutputTypeDef(BaseModel):
    DataSetConfigurations: List[DataSetConfigurationOutputTypeDef]
    Sheets: Optional[List[SheetDefinitionOutputTypeDef]] = None
    CalculatedFields: Optional[List[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutputTypeDef]] = None
    FilterGroups: Optional[List[FilterGroupOutputTypeDef]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutputTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class AnalysisDefinitionTypeDef(BaseModel):
    DataSetIdentifierDeclarations: Sequence[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[Sequence[SheetDefinitionTypeDef]] = None
    CalculatedFields: Optional[Sequence[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[Sequence[ParameterDeclarationTypeDef]] = None
    FilterGroups: Optional[Sequence[FilterGroupTypeDef]] = None
    ColumnConfigurations: Optional[Sequence[ColumnConfigurationTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class DashboardVersionDefinitionTypeDef(BaseModel):
    DataSetIdentifierDeclarations: Sequence[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[Sequence[SheetDefinitionTypeDef]] = None
    CalculatedFields: Optional[Sequence[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[Sequence[ParameterDeclarationTypeDef]] = None
    FilterGroups: Optional[Sequence[FilterGroupTypeDef]] = None
    ColumnConfigurations: Optional[Sequence[ColumnConfigurationTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class TemplateVersionDefinitionTypeDef(BaseModel):
    DataSetConfigurations: Sequence[DataSetConfigurationTypeDef]
    Sheets: Optional[Sequence[SheetDefinitionTypeDef]] = None
    CalculatedFields: Optional[Sequence[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[Sequence[ParameterDeclarationTypeDef]] = None
    FilterGroups: Optional[Sequence[FilterGroupTypeDef]] = None
    ColumnConfigurations: Optional[Sequence[ColumnConfigurationTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class DescribeAnalysisDefinitionResponseTypeDef(BaseModel):
    AnalysisId: str
    Name: str
    Errors: List[AnalysisErrorTypeDef]
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: AnalysisDefinitionOutputTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDashboardDefinitionResponseTypeDef(BaseModel):
    DashboardId: str
    Errors: List[DashboardErrorTypeDef]
    Name: str
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: DashboardVersionDefinitionOutputTypeDef
    Status: int
    RequestId: str
    DashboardPublishOptions: DashboardPublishOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTemplateDefinitionResponseTypeDef(BaseModel):
    Name: str
    TemplateId: str
    Errors: List[TemplateErrorTypeDef]
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: TemplateVersionDefinitionOutputTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnalysisRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str
    Name: str
    Parameters: Optional[ParametersTypeDef] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    SourceEntity: Optional[AnalysisSourceEntityTypeDef] = None
    ThemeArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Definition: Optional[AnalysisDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None
    FolderArns: Optional[Sequence[str]] = None

class UpdateAnalysisRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    AnalysisId: str
    Name: str
    Parameters: Optional[ParametersTypeDef] = None
    SourceEntity: Optional[AnalysisSourceEntityTypeDef] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[AnalysisDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

class CreateDashboardRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    Name: str
    Parameters: Optional[ParametersTypeDef] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    SourceEntity: Optional[DashboardSourceEntityTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VersionDescription: Optional[str] = None
    DashboardPublishOptions: Optional[DashboardPublishOptionsTypeDef] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[DashboardVersionDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None
    FolderArns: Optional[Sequence[str]] = None
    LinkSharingConfiguration: Optional[LinkSharingConfigurationTypeDef] = None
    LinkEntities: Optional[Sequence[str]] = None

class UpdateDashboardRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    DashboardId: str
    Name: str
    SourceEntity: Optional[DashboardSourceEntityTypeDef] = None
    Parameters: Optional[ParametersTypeDef] = None
    VersionDescription: Optional[str] = None
    DashboardPublishOptions: Optional[DashboardPublishOptionsTypeDef] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[DashboardVersionDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

class CreateTemplateRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    Name: Optional[str] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    SourceEntity: Optional[TemplateSourceEntityTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VersionDescription: Optional[str] = None
    Definition: Optional[TemplateVersionDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

class UpdateTemplateRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    TemplateId: str
    SourceEntity: Optional[TemplateSourceEntityTypeDef] = None
    VersionDescription: Optional[str] = None
    Name: Optional[str] = None
    Definition: Optional[TemplateVersionDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

