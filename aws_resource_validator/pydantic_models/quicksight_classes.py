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
from aws_resource_validator.pydantic_models.quicksight_constants import *

class AccountCustomizationTypeDef(BaseValidatorModel):
    DefaultTheme: Optional[str] = None
    DefaultEmailCustomizationTemplate: Optional[str] = None

class AccountInfoTypeDef(BaseValidatorModel):
    AccountName: Optional[str] = None
    Edition: Optional[EditionType] = None
    NotificationEmail: Optional[str] = None
    AuthenticationType: Optional[str] = None
    AccountSubscriptionStatus: Optional[str] = None
    IAMIdentityCenterInstanceArn: Optional[str] = None

class AccountSettingsTypeDef(BaseValidatorModel):
    AccountName: Optional[str] = None
    Edition: Optional[EditionType] = None
    DefaultNamespace: Optional[str] = None
    NotificationEmail: Optional[str] = None
    PublicSharingEnabled: Optional[bool] = None
    TerminationProtectionEnabled: Optional[bool] = None

class ActiveIAMPolicyAssignmentTypeDef(BaseValidatorModel):
    AssignmentName: Optional[str] = None
    PolicyArn: Optional[str] = None

class AdHocFilteringOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class AttributeAggregationFunctionTypeDef(BaseValidatorModel):
    SimpleAttributeAggregation: Optional[Literal["UNIQUE_VALUE"]] = None
    ValueForMultipleValues: Optional[str] = None

class ColumnIdentifierTypeDef(BaseValidatorModel):
    DataSetIdentifier: str
    ColumnName: str

class AmazonElasticsearchParametersTypeDef(BaseValidatorModel):
    Domain: str

class AmazonOpenSearchParametersTypeDef(BaseValidatorModel):
    Domain: str

class AssetOptionsTypeDef(BaseValidatorModel):
    Timezone: Optional[str] = None
    WeekStart: Optional[DayOfTheWeekType] = None

class CalculatedFieldTypeDef(BaseValidatorModel):
    DataSetIdentifier: str
    Name: str
    Expression: str

class DataSetIdentifierDeclarationTypeDef(BaseValidatorModel):
    Identifier: str
    DataSetArn: str

class EntityTypeDef(BaseValidatorModel):
    Path: Optional[str] = None

class AnalysisSearchFilterTypeDef(BaseValidatorModel):
    Operator: Optional[FilterOperatorType] = None
    Name: Optional[AnalysisFilterAttributeType] = None
    Value: Optional[str] = None

class DataSetReferenceTypeDef(BaseValidatorModel):
    DataSetPlaceholder: str
    DataSetArn: str

class AnalysisSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AnalysisId: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ResourceStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class SheetTypeDef(BaseValidatorModel):
    SheetId: Optional[str] = None
    Name: Optional[str] = None

class AnchorDateConfigurationTypeDef(BaseValidatorModel):
    AnchorOption: Optional[Literal["NOW"]] = None
    ParameterName: Optional[str] = None

class AnonymousUserDashboardEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialDashboardId: str

class DashboardVisualIdTypeDef(BaseValidatorModel):
    DashboardId: str
    SheetId: str
    VisualId: str

class AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialTopicId: str

class AnonymousUserQSearchBarEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialTopicId: str

class ArcAxisDisplayRangeTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class ArcConfigurationTypeDef(BaseValidatorModel):
    ArcAngle: Optional[float] = None
    ArcThickness: Optional[ArcThicknessOptionsType] = None

class ArcOptionsTypeDef(BaseValidatorModel):
    ArcThickness: Optional[ArcThicknessType] = None

class AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobDataSourcePropertyToOverrideType]

class AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[Literal["StartAfterDateTime"]]

class AssetBundleExportJobResourceIdOverrideConfigurationTypeDef(BaseValidatorModel):
    PrefixForAllResources: Optional[bool] = None

class AssetBundleExportJobThemeOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[Literal["Name"]]

class AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef(BaseValidatorModel):
    Arn: str
    Properties: List[AssetBundleExportJobVPCConnectionPropertyToOverrideType]

class AssetBundleExportJobAnalysisOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobDashboardOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobDataSetOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobDataSourceOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[AssetBundleExportJobDataSourcePropertyToOverrideType]

class AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[Literal["StartAfterDateTime"]]

class AssetBundleExportJobThemeOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[Literal["Name"]]

class AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef(BaseValidatorModel):
    Arn: str
    Properties: Sequence[AssetBundleExportJobVPCConnectionPropertyToOverrideType]

class AssetBundleExportJobErrorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleExportJobSummaryTypeDef(BaseValidatorModel):
    JobStatus: Optional[AssetBundleExportJobStatusType] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AssetBundleExportJobId: Optional[str] = None
    IncludeAllDependencies: Optional[bool] = None
    ExportFormat: Optional[AssetBundleExportFormatType] = None
    IncludePermissions: Optional[bool] = None
    IncludeTags: Optional[bool] = None

class AssetBundleExportJobValidationStrategyTypeDef(BaseValidatorModel):
    StrictModeForAllResources: Optional[bool] = None

class AssetBundleExportJobWarningTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleImportJobAnalysisOverrideParametersTypeDef(BaseValidatorModel):
    AnalysisId: str
    Name: Optional[str] = None

class AssetBundleResourcePermissionsOutputTypeDef(BaseValidatorModel):
    Principals: List[str]
    Actions: List[str]

class AssetBundleResourcePermissionsTypeDef(BaseValidatorModel):
    Principals: Sequence[str]
    Actions: Sequence[str]

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class AssetBundleImportJobDashboardOverrideParametersTypeDef(BaseValidatorModel):
    DashboardId: str
    Name: Optional[str] = None

class AssetBundleImportJobDataSetOverrideParametersTypeDef(BaseValidatorModel):
    DataSetId: str
    Name: Optional[str] = None

class AssetBundleImportJobDataSourceCredentialPairTypeDef(BaseValidatorModel):
    Username: str
    Password: str

class SslPropertiesTypeDef(BaseValidatorModel):
    DisableSsl: Optional[bool] = None

class VpcConnectionPropertiesTypeDef(BaseValidatorModel):
    VpcConnectionArn: str

class AssetBundleImportJobErrorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef(BaseValidatorModel):
    DataSetId: str
    ScheduleId: str
    StartAfterDateTime: Optional[datetime] = None

class AssetBundleImportJobResourceIdOverrideConfigurationTypeDef(BaseValidatorModel):
    PrefixForAllResources: Optional[str] = None

class AssetBundleImportJobThemeOverrideParametersTypeDef(BaseValidatorModel):
    ThemeId: str
    Name: Optional[str] = None

class AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef(BaseValidatorModel):
    VPCConnectionId: str
    Name: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    DnsResolvers: Optional[List[str]] = None
    RoleArn: Optional[str] = None

class AssetBundleImportJobVPCConnectionOverrideParametersTypeDef(BaseValidatorModel):
    VPCConnectionId: str
    Name: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    DnsResolvers: Optional[Sequence[str]] = None
    RoleArn: Optional[str] = None

class AssetBundleImportJobOverrideValidationStrategyTypeDef(BaseValidatorModel):
    StrictModeForAllResources: Optional[bool] = None

class AssetBundleImportJobSummaryTypeDef(BaseValidatorModel):
    JobStatus: Optional[AssetBundleImportJobStatusType] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AssetBundleImportJobId: Optional[str] = None
    FailureAction: Optional[AssetBundleImportFailureActionType] = None

class AssetBundleImportJobWarningTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None

class AssetBundleImportSourceDescriptionTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    S3Uri: Optional[str] = None

class AthenaParametersTypeDef(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    RoleArn: Optional[str] = None

class AuroraParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class AuroraPostgreSqlParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class AuthorizedTargetsByServiceTypeDef(BaseValidatorModel):
    Service: Optional[Literal["REDSHIFT"]] = None
    AuthorizedTargets: Optional[List[str]] = None

class AwsIotAnalyticsParametersTypeDef(BaseValidatorModel):
    DataSetName: str

class DateAxisOptionsTypeDef(BaseValidatorModel):
    MissingDateVisibility: Optional[VisibilityType] = None

class AxisDisplayMinMaxRangeTypeDef(BaseValidatorModel):
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None

class AxisLinearScaleTypeDef(BaseValidatorModel):
    StepCount: Optional[int] = None
    StepSize: Optional[float] = None

class AxisLogarithmicScaleTypeDef(BaseValidatorModel):
    Base: Optional[float] = None

class ItemsLimitConfigurationTypeDef(BaseValidatorModel):
    ItemsLimit: Optional[int] = None
    OtherCategories: Optional[OtherCategoriesType] = None

class BigQueryParametersTypeDef(BaseValidatorModel):
    ProjectId: str
    DataSetRegion: Optional[str] = None

class BinCountOptionsTypeDef(BaseValidatorModel):
    Value: Optional[int] = None

class BinWidthOptionsTypeDef(BaseValidatorModel):
    Value: Optional[float] = None
    BinCountLimit: Optional[int] = None

class SectionAfterPageBreakTypeDef(BaseValidatorModel):
    Status: Optional[SectionPageBreakStatusType] = None

class BookmarksConfigurationsTypeDef(BaseValidatorModel):
    Enabled: bool

class BorderStyleTypeDef(BaseValidatorModel):
    Show: Optional[bool] = None

class BoxPlotStyleOptionsTypeDef(BaseValidatorModel):
    FillStyle: Optional[BoxPlotFillStyleType] = None

class PaginationConfigurationTypeDef(BaseValidatorModel):
    PageSize: int
    PageNumber: int

class CalculatedColumnTypeDef(BaseValidatorModel):
    ColumnName: str
    ColumnId: str
    Expression: str

class CalculatedMeasureFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Expression: str

class CancelIngestionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    IngestionId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CastColumnTypeOperationTypeDef(BaseValidatorModel):
    ColumnName: str
    NewColumnType: ColumnDataTypeType
    SubType: Optional[ColumnDataSubTypeType] = None
    Format: Optional[str] = None

class CustomFilterConfigurationTypeDef(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValue: Optional[str] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    ParameterName: Optional[str] = None

class CustomFilterListConfigurationOutputTypeDef(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None

class FilterListConfigurationOutputTypeDef(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    CategoryValues: Optional[List[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    NullOption: Optional[FilterNullOptionType] = None

class CustomFilterListConfigurationTypeDef(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    NullOption: FilterNullOptionType
    CategoryValues: Optional[Sequence[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None

class FilterListConfigurationTypeDef(BaseValidatorModel):
    MatchOperator: CategoryFilterMatchOperatorType
    CategoryValues: Optional[Sequence[str]] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    NullOption: Optional[FilterNullOptionType] = None

class CellValueSynonymOutputTypeDef(BaseValidatorModel):
    CellValue: Optional[str] = None
    Synonyms: Optional[List[str]] = None

class CellValueSynonymTypeDef(BaseValidatorModel):
    CellValue: Optional[str] = None
    Synonyms: Optional[Sequence[str]] = None

class SimpleClusterMarkerTypeDef(BaseValidatorModel):
    Color: Optional[str] = None

class CollectiveConstantOutputTypeDef(BaseValidatorModel):
    ValueList: Optional[List[str]] = None

class CollectiveConstantTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None

class DataColorTypeDef(BaseValidatorModel):
    Color: Optional[str] = None
    DataValue: Optional[float] = None

class CustomColorTypeDef(BaseValidatorModel):
    Color: str
    FieldValue: Optional[str] = None
    SpecialValue: Optional[SpecialValueType] = None

class ColumnDescriptionTypeDef(BaseValidatorModel):
    Text: Optional[str] = None

class ColumnGroupColumnSchemaTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class GeoSpatialColumnGroupOutputTypeDef(BaseValidatorModel):
    Name: str
    Columns: List[str]
    CountryCode: Optional[Literal["US"]] = None

class GeoSpatialColumnGroupTypeDef(BaseValidatorModel):
    Name: str
    Columns: Sequence[str]
    CountryCode: Optional[Literal["US"]] = None

class ColumnLevelPermissionRuleOutputTypeDef(BaseValidatorModel):
    Principals: Optional[List[str]] = None
    ColumnNames: Optional[List[str]] = None

class ColumnLevelPermissionRuleTypeDef(BaseValidatorModel):
    Principals: Optional[Sequence[str]] = None
    ColumnNames: Optional[Sequence[str]] = None

class ColumnSchemaTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DataType: Optional[str] = None
    GeographicRole: Optional[str] = None

class ComparativeOrderOutputTypeDef(BaseValidatorModel):
    UseOrdering: Optional[ColumnOrderingTypeType] = None
    SpecifedOrder: Optional[List[str]] = None
    TreatUndefinedSpecifiedValues: Optional[UndefinedSpecifiedValueTypeType] = None

class ComparativeOrderTypeDef(BaseValidatorModel):
    UseOrdering: Optional[ColumnOrderingTypeType] = None
    SpecifedOrder: Optional[Sequence[str]] = None
    TreatUndefinedSpecifiedValues: Optional[UndefinedSpecifiedValueTypeType] = None

class ConditionalFormattingSolidColorTypeDef(BaseValidatorModel):
    Expression: str
    Color: Optional[str] = None

class ConditionalFormattingCustomIconOptionsTypeDef(BaseValidatorModel):
    Icon: Optional[IconType] = None
    UnicodeIcon: Optional[str] = None

class ConditionalFormattingIconDisplayConfigurationTypeDef(BaseValidatorModel):
    IconDisplayOption: Optional[Literal["ICON_ONLY"]] = None

class ConditionalFormattingIconSetTypeDef(BaseValidatorModel):
    Expression: str
    IconSetType: Optional[ConditionalFormattingIconSetTypeType] = None

class ContextMenuOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class CreateAccountSubscriptionRequestRequestTypeDef(BaseValidatorModel):
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

class SignupResponseTypeDef(BaseValidatorModel):
    IAMUser: Optional[bool] = None
    userLoginName: Optional[str] = None
    accountName: Optional[str] = None
    directoryType: Optional[str] = None

class ValidationStrategyTypeDef(BaseValidatorModel):
    Mode: ValidationStrategyModeType

class DataSetUsageConfigurationTypeDef(BaseValidatorModel):
    DisableUseAsDirectQuerySource: Optional[bool] = None
    DisableUseAsImportedSource: Optional[bool] = None

class RowLevelPermissionDataSetTypeDef(BaseValidatorModel):
    Arn: str
    PermissionPolicy: RowLevelPermissionPolicyType
    Namespace: Optional[str] = None
    FormatVersion: Optional[RowLevelPermissionFormatVersionType] = None
    Status: Optional[StatusType] = None

class CreateFolderMembershipRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    MemberId: str
    MemberType: MemberTypeType

class FolderMemberTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None

class CreateGroupMembershipRequestRequestTypeDef(BaseValidatorModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str

class GroupMemberTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    MemberName: Optional[str] = None

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    Description: Optional[str] = None

class GroupTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    PrincipalId: Optional[str] = None

class CreateIAMPolicyAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    AssignmentStatus: AssignmentStatusType
    Namespace: str
    PolicyArn: Optional[str] = None
    Identities: Optional[Mapping[str, Sequence[str]]] = None

class CreateIngestionRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    IngestionId: str
    AwsAccountId: str
    IngestionType: Optional[IngestionTypeType] = None

class CreateRoleMembershipRequestRequestTypeDef(BaseValidatorModel):
    MemberName: str
    AwsAccountId: str
    Namespace: str
    Role: RoleType

class CreateTemplateAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str
    TemplateVersionNumber: int

class TemplateAliasTypeDef(BaseValidatorModel):
    AliasName: Optional[str] = None
    Arn: Optional[str] = None
    TemplateVersionNumber: Optional[int] = None

class CreateThemeAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str
    ThemeVersionNumber: int

class ThemeAliasTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AliasName: Optional[str] = None
    ThemeVersionNumber: Optional[int] = None

class DecimalPlacesConfigurationTypeDef(BaseValidatorModel):
    DecimalPlaces: int

class NegativeValueConfigurationTypeDef(BaseValidatorModel):
    DisplayMode: NegativeValueDisplayModeType

class NullValueFormatConfigurationTypeDef(BaseValidatorModel):
    NullString: str

class LocalNavigationConfigurationTypeDef(BaseValidatorModel):
    TargetSheetId: str

class CustomActionURLOperationTypeDef(BaseValidatorModel):
    URLTemplate: str
    URLTarget: URLTargetConfigurationType

class CustomNarrativeOptionsTypeDef(BaseValidatorModel):
    Narrative: str

class CustomParameterValuesOutputTypeDef(BaseValidatorModel):
    StringValues: Optional[List[str]] = None
    IntegerValues: Optional[List[int]] = None
    DecimalValues: Optional[List[float]] = None
    DateTimeValues: Optional[List[datetime]] = None

class InputColumnTypeDef(BaseValidatorModel):
    Name: str
    Type: InputColumnDataTypeType
    SubType: Optional[ColumnDataSubTypeType] = None

class DataPointDrillUpDownOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DataPointMenuLabelOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DataPointTooltipOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class ExportToCSVOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class ExportWithHiddenFieldsOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class SheetControlsOptionTypeDef(BaseValidatorModel):
    VisibilityState: Optional[DashboardUIStateType] = None

class SheetLayoutElementMaximizationOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class VisualAxisSortOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class VisualMenuOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DashboardSearchFilterTypeDef(BaseValidatorModel):
    Operator: FilterOperatorType
    Name: Optional[DashboardFilterAttributeType] = None
    Value: Optional[str] = None

class DashboardSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    DashboardId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    PublishedVersionNumber: Optional[int] = None
    LastPublishedTime: Optional[datetime] = None

class DashboardVersionSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    SourceEntityArn: Optional[str] = None
    Description: Optional[str] = None

class ExportHiddenFieldsOptionTypeDef(BaseValidatorModel):
    AvailabilityStatus: Optional[DashboardBehaviorType] = None

class DataAggregationTypeDef(BaseValidatorModel):
    DatasetRowDateGranularity: Optional[TopicTimeGranularityType] = None
    DefaultDateColumnName: Optional[str] = None

class DataBarsOptionsTypeDef(BaseValidatorModel):
    FieldId: str
    PositiveColor: Optional[str] = None
    NegativeColor: Optional[str] = None

class DataColorPaletteOutputTypeDef(BaseValidatorModel):
    Colors: Optional[List[str]] = None
    MinMaxGradient: Optional[List[str]] = None
    EmptyFillColor: Optional[str] = None

class DataColorPaletteTypeDef(BaseValidatorModel):
    Colors: Optional[Sequence[str]] = None
    MinMaxGradient: Optional[Sequence[str]] = None
    EmptyFillColor: Optional[str] = None

class DataPathLabelTypeTypeDef(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldValue: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class FieldLabelTypeTypeDef(BaseValidatorModel):
    FieldId: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class MaximumLabelTypeTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class MinimumLabelTypeTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class RangeEndsLabelTypeTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class DataPathTypeTypeDef(BaseValidatorModel):
    PivotTableDataPathType: Optional[PivotTableDataPathTypeType] = None

class DataSetSearchFilterTypeDef(BaseValidatorModel):
    Operator: FilterOperatorType
    Name: DataSetFilterAttributeType
    Value: str

class FieldFolderOutputTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    columns: Optional[List[str]] = None

class OutputColumnTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[ColumnDataTypeType] = None
    SubType: Optional[ColumnDataSubTypeType] = None

class DataSourceErrorInfoTypeDef(BaseValidatorModel):
    Type: Optional[DataSourceErrorInfoTypeType] = None
    Message: Optional[str] = None

class DatabricksParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    SqlEndpointPath: str

class ExasolParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int

class JiraParametersTypeDef(BaseValidatorModel):
    SiteBaseUrl: str

class MariaDbParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class MySqlParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class OracleParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class PostgreSqlParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class PrestoParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Catalog: str

class RdsParametersTypeDef(BaseValidatorModel):
    InstanceId: str
    Database: str

class ServiceNowParametersTypeDef(BaseValidatorModel):
    SiteBaseUrl: str

class SnowflakeParametersTypeDef(BaseValidatorModel):
    Host: str
    Database: str
    Warehouse: str

class SparkParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int

class SqlServerParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class StarburstParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Catalog: str
    ProductType: Optional[StarburstProductTypeType] = None

class TeradataParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Database: str

class TrinoParametersTypeDef(BaseValidatorModel):
    Host: str
    Port: int
    Catalog: str

class TwitterParametersTypeDef(BaseValidatorModel):
    Query: str
    MaxRows: int

class DataSourceSearchFilterTypeDef(BaseValidatorModel):
    Operator: FilterOperatorType
    Name: DataSourceFilterAttributeType
    Value: str

class DataSourceSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    DataSourceId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[DataSourceTypeType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class DateTimeDatasetParameterDefaultValuesOutputTypeDef(BaseValidatorModel):
    StaticValues: Optional[List[datetime]] = None

class RollingDateConfigurationTypeDef(BaseValidatorModel):
    Expression: str
    DataSetIdentifier: Optional[str] = None

class DateTimeValueWhenUnsetConfigurationOutputTypeDef(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[datetime] = None

class MappedDataSetParameterTypeDef(BaseValidatorModel):
    DataSetIdentifier: str
    DataSetParameterName: str

class DateTimeParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[datetime]

class SheetControlInfoIconLabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    InfoIconText: Optional[str] = None

class DecimalDatasetParameterDefaultValuesOutputTypeDef(BaseValidatorModel):
    StaticValues: Optional[List[float]] = None

class DecimalDatasetParameterDefaultValuesTypeDef(BaseValidatorModel):
    StaticValues: Optional[Sequence[float]] = None

class DecimalValueWhenUnsetConfigurationTypeDef(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[float] = None

class DecimalParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[float]

class DecimalParameterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[float]

class FilterSelectableValuesOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class FilterSelectableValuesTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None

class DeleteAccountCustomizationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: Optional[str] = None

class DeleteAccountSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str

class DeleteAnalysisRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None

class DeleteDashboardRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None

class DeleteDataSetRefreshPropertiesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str

class DeleteDataSetRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str

class DeleteDataSourceRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str

class DeleteFolderMembershipRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    MemberId: str
    MemberType: MemberTypeType

class DeleteFolderRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str

class DeleteGroupMembershipRequestRequestTypeDef(BaseValidatorModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DeleteIAMPolicyAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str

class DeleteIdentityPropagationConfigRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Service: Literal["REDSHIFT"]

class DeleteNamespaceRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str

class DeleteRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    ScheduleId: str

class DeleteRoleCustomPermissionRequestRequestTypeDef(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class DeleteRoleMembershipRequestRequestTypeDef(BaseValidatorModel):
    MemberName: str
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class DeleteTemplateAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str

class DeleteTemplateRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None

class DeleteThemeAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str

class DeleteThemeRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    VersionNumber: Optional[int] = None

class DeleteTopicRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str

class DeleteTopicRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str

class DeleteUserByPrincipalIdRequestRequestTypeDef(BaseValidatorModel):
    PrincipalId: str
    AwsAccountId: str
    Namespace: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str

class DeleteVPCConnectionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str

class DescribeAccountCustomizationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: Optional[str] = None
    Resolved: Optional[bool] = None

class DescribeAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str

class DescribeAccountSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str

class DescribeAnalysisDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str

class DescribeAnalysisPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str

class ResourcePermissionOutputTypeDef(BaseValidatorModel):
    Principal: str
    Actions: List[str]

class DescribeAnalysisRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str

class DescribeAssetBundleExportJobRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleExportJobId: str

class DescribeAssetBundleImportJobRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleImportJobId: str

class DescribeDashboardDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeDashboardPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str

class DescribeDashboardRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeDashboardSnapshotJobRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str

class DescribeDashboardSnapshotJobResultRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str

class SnapshotJobErrorInfoTypeDef(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[str] = None

class DescribeDataSetPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str

class DescribeDataSetRefreshPropertiesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str

class DescribeDataSetRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str

class DescribeDataSourcePermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str

class DescribeDataSourceRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeFolderPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResourcePermissionExtraOutputTypeDef(BaseValidatorModel):
    Principal: str
    Actions: List[str]

class DescribeFolderRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str

class DescribeFolderResolvedPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class FolderTypeDef(BaseValidatorModel):
    FolderId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    FolderPath: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SharingModel: Optional[SharingModelType] = None

class DescribeGroupMembershipRequestRequestTypeDef(BaseValidatorModel):
    MemberName: str
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DescribeGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str

class DescribeIAMPolicyAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str

class IAMPolicyAssignmentTypeDef(BaseValidatorModel):
    AwsAccountId: Optional[str] = None
    AssignmentId: Optional[str] = None
    AssignmentName: Optional[str] = None
    PolicyArn: Optional[str] = None
    Identities: Optional[Dict[str, List[str]]] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None

class DescribeIngestionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    IngestionId: str

class DescribeIpRestrictionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str

class DescribeKeyRegistrationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DefaultKeyOnly: Optional[bool] = None

class RegisteredCustomerManagedKeyTypeDef(BaseValidatorModel):
    KeyArn: Optional[str] = None
    DefaultKey: Optional[bool] = None

class DescribeNamespaceRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str

class DescribeRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    ScheduleId: str

class DescribeRoleCustomPermissionRequestRequestTypeDef(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class DescribeTemplateAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str

class DescribeTemplateDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeTemplatePermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str

class DescribeTemplateRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeThemeAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str

class DescribeThemePermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str

class DescribeThemeRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    VersionNumber: Optional[int] = None
    AliasName: Optional[str] = None

class DescribeTopicPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str

class DescribeTopicRefreshRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    RefreshId: str

class TopicRefreshDetailsTypeDef(BaseValidatorModel):
    RefreshArn: Optional[str] = None
    RefreshId: Optional[str] = None
    RefreshStatus: Optional[TopicRefreshStatusType] = None

class DescribeTopicRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str

class TopicRefreshScheduleOutputTypeDef(BaseValidatorModel):
    IsEnabled: bool
    BasedOnSpiceSchedule: bool
    StartingAt: Optional[datetime] = None
    Timezone: Optional[str] = None
    RepeatAt: Optional[str] = None
    TopicScheduleType: Optional[TopicScheduleTypeType] = None

class DescribeTopicRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str

class DescribeUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str

class UserTypeDef(BaseValidatorModel):
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

class DescribeVPCConnectionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str

class NegativeFormatTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None

class DonutCenterOptionsTypeDef(BaseValidatorModel):
    LabelVisibility: Optional[VisibilityType] = None

class ListControlSelectAllOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class ErrorInfoTypeDef(BaseValidatorModel):
    Type: Optional[IngestionErrorTypeType] = None
    Message: Optional[str] = None

class ExcludePeriodConfigurationTypeDef(BaseValidatorModel):
    Amount: int
    Granularity: TimeGranularityType
    Status: Optional[WidgetStatusType] = None

class FailedKeyRegistrationEntryTypeDef(BaseValidatorModel):
    Message: str
    StatusCode: int
    SenderFault: bool
    KeyArn: Optional[str] = None

class FieldFolderTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    columns: Optional[Sequence[str]] = None

class FieldSortTypeDef(BaseValidatorModel):
    FieldId: str
    Direction: SortDirectionType

class FieldTooltipItemTypeDef(BaseValidatorModel):
    FieldId: str
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    TooltipTarget: Optional[TooltipTargetType] = None

class GeospatialMapStyleOptionsTypeDef(BaseValidatorModel):
    BaseMapStyle: Optional[BaseMapStyleTypeType] = None

class SameSheetTargetVisualConfigurationOutputTypeDef(BaseValidatorModel):
    TargetVisuals: Optional[List[str]] = None
    TargetVisualOptions: Optional[Literal["ALL_VISUALS"]] = None

class SameSheetTargetVisualConfigurationTypeDef(BaseValidatorModel):
    TargetVisuals: Optional[Sequence[str]] = None
    TargetVisualOptions: Optional[Literal["ALL_VISUALS"]] = None

class FilterOperationTypeDef(BaseValidatorModel):
    ConditionExpression: str

class FolderSearchFilterTypeDef(BaseValidatorModel):
    Operator: Optional[FilterOperatorType] = None
    Name: Optional[FolderFilterAttributeType] = None
    Value: Optional[str] = None

class FolderSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    FolderId: Optional[str] = None
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SharingModel: Optional[SharingModelType] = None

class FontSizeTypeDef(BaseValidatorModel):
    Relative: Optional[RelativeFontSizeType] = None

class FontWeightTypeDef(BaseValidatorModel):
    Name: Optional[FontWeightNameType] = None

class FontTypeDef(BaseValidatorModel):
    FontFamily: Optional[str] = None

class TimeBasedForecastPropertiesTypeDef(BaseValidatorModel):
    PeriodsForward: Optional[int] = None
    PeriodsBackward: Optional[int] = None
    UpperBoundary: Optional[float] = None
    LowerBoundary: Optional[float] = None
    PredictionInterval: Optional[int] = None
    Seasonality: Optional[int] = None

class WhatIfPointScenarioOutputTypeDef(BaseValidatorModel):
    Date: datetime
    Value: float

class WhatIfRangeScenarioOutputTypeDef(BaseValidatorModel):
    StartDate: datetime
    EndDate: datetime
    Value: float

class FreeFormLayoutScreenCanvasSizeOptionsTypeDef(BaseValidatorModel):
    OptimizedViewPortWidth: str

class FreeFormLayoutElementBackgroundStyleTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None

class FreeFormLayoutElementBorderStyleTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None

class LoadingAnimationTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class GaugeChartColorConfigurationTypeDef(BaseValidatorModel):
    ForegroundColor: Optional[str] = None
    BackgroundColor: Optional[str] = None

class SessionTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class GeospatialCoordinateBoundsTypeDef(BaseValidatorModel):
    North: float
    South: float
    West: float
    East: float

class GeospatialHeatmapDataColorTypeDef(BaseValidatorModel):
    Color: str

class GetDashboardEmbedUrlRequestRequestTypeDef(BaseValidatorModel):
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

class GetSessionEmbedUrlRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    EntryPoint: Optional[str] = None
    SessionLifetimeInMinutes: Optional[int] = None
    UserArn: Optional[str] = None

class TableBorderOptionsTypeDef(BaseValidatorModel):
    Color: Optional[str] = None
    Thickness: Optional[int] = None
    Style: Optional[TableBorderStyleType] = None

class GradientStopTypeDef(BaseValidatorModel):
    GradientOffset: float
    DataValue: Optional[float] = None
    Color: Optional[str] = None

class GridLayoutScreenCanvasSizeOptionsTypeDef(BaseValidatorModel):
    ResizeOption: ResizeOptionType
    OptimizedViewPortWidth: Optional[str] = None

class GridLayoutElementTypeDef(BaseValidatorModel):
    ElementId: str
    ElementType: LayoutElementTypeType
    ColumnSpan: int
    RowSpan: int
    ColumnIndex: Optional[int] = None
    RowIndex: Optional[int] = None

class GroupSearchFilterTypeDef(BaseValidatorModel):
    Operator: Literal["StartsWith"]
    Name: Literal["GROUP_NAME"]
    Value: str

class GutterStyleTypeDef(BaseValidatorModel):
    Show: Optional[bool] = None

class IAMPolicyAssignmentSummaryTypeDef(BaseValidatorModel):
    AssignmentName: Optional[str] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None

class IdentityCenterConfigurationTypeDef(BaseValidatorModel):
    EnableIdentityPropagation: Optional[bool] = None

class LookbackWindowTypeDef(BaseValidatorModel):
    ColumnName: str
    Size: int
    SizeUnit: LookbackWindowSizeUnitType

class QueueInfoTypeDef(BaseValidatorModel):
    WaitingOnIngestion: str
    QueuedIngestion: str

class RowInfoTypeDef(BaseValidatorModel):
    RowsIngested: Optional[int] = None
    RowsDropped: Optional[int] = None
    TotalRowsInDataset: Optional[int] = None

class IntegerDatasetParameterDefaultValuesOutputTypeDef(BaseValidatorModel):
    StaticValues: Optional[List[int]] = None

class IntegerDatasetParameterDefaultValuesTypeDef(BaseValidatorModel):
    StaticValues: Optional[Sequence[int]] = None

class IntegerValueWhenUnsetConfigurationTypeDef(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[int] = None

class IntegerParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[int]

class IntegerParameterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[int]

class JoinKeyPropertiesTypeDef(BaseValidatorModel):
    UniqueKey: Optional[bool] = None

class KPISparklineOptionsTypeDef(BaseValidatorModel):
    Type: KPISparklineTypeType
    Visibility: Optional[VisibilityType] = None
    Color: Optional[str] = None
    TooltipVisibility: Optional[VisibilityType] = None

class ProgressBarOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class SecondaryValueOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class TrendArrowOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class KPIVisualStandardLayoutTypeDef(BaseValidatorModel):
    Type: KPIVisualStandardLayoutTypeType

class LineChartLineStyleSettingsTypeDef(BaseValidatorModel):
    LineVisibility: Optional[VisibilityType] = None
    LineInterpolation: Optional[LineInterpolationType] = None
    LineStyle: Optional[LineChartLineStyleType] = None
    LineWidth: Optional[str] = None

class LineChartMarkerStyleSettingsTypeDef(BaseValidatorModel):
    MarkerVisibility: Optional[VisibilityType] = None
    MarkerShape: Optional[LineChartMarkerShapeType] = None
    MarkerSize: Optional[str] = None
    MarkerColor: Optional[str] = None

class MissingDataConfigurationTypeDef(BaseValidatorModel):
    TreatmentOption: Optional[MissingDataTreatmentOptionType] = None

class ResourcePermissionTypeDef(BaseValidatorModel):
    Principal: str
    Actions: Sequence[str]

class ListAnalysesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAssetBundleExportJobsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAssetBundleImportJobsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListControlSearchOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class ListDashboardVersionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDashboardsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataSetsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFolderMembersRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MemberIdArnPairTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberArn: Optional[str] = None

class ListFoldersRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupMembershipsRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIAMPolicyAssignmentsForUserRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    UserName: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIAMPolicyAssignmentsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentityPropagationConfigsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListIngestionsRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListNamespacesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRefreshSchedulesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str

class ListRoleMembershipsRequestRequestTypeDef(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListTemplateAliasesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTemplateVersionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TemplateVersionSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    VersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    Status: Optional[ResourceStatusType] = None
    Description: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TemplateSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    TemplateId: Optional[str] = None
    Name: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class ListThemeAliasesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListThemeVersionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ThemeVersionSummaryTypeDef(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Status: Optional[ResourceStatusType] = None

class ListThemesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Type: Optional[ThemeTypeType] = None

class ThemeSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ThemeId: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class ListTopicRefreshSchedulesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str

class ListTopicsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TopicSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    TopicId: Optional[str] = None
    Name: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None

class ListUserGroupsRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVPCConnectionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LongFormatTextTypeDef(BaseValidatorModel):
    PlainText: Optional[str] = None
    RichText: Optional[str] = None

class ManifestFileLocationTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str

class MarginStyleTypeDef(BaseValidatorModel):
    Show: Optional[bool] = None

class NamedEntityDefinitionMetricOutputTypeDef(BaseValidatorModel):
    Aggregation: Optional[NamedEntityAggTypeType] = None
    AggregationFunctionParameters: Optional[Dict[str, str]] = None

class NamedEntityDefinitionMetricTypeDef(BaseValidatorModel):
    Aggregation: Optional[NamedEntityAggTypeType] = None
    AggregationFunctionParameters: Optional[Mapping[str, str]] = None

class NamespaceErrorTypeDef(BaseValidatorModel):
    Type: Optional[NamespaceErrorTypeType] = None
    Message: Optional[str] = None

class NetworkInterfaceTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    ErrorMessage: Optional[str] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    NetworkInterfaceId: Optional[str] = None

class NewDefaultValuesOutputTypeDef(BaseValidatorModel):
    StringStaticValues: Optional[List[str]] = None
    DecimalStaticValues: Optional[List[float]] = None
    DateTimeStaticValues: Optional[List[datetime]] = None
    IntegerStaticValues: Optional[List[int]] = None

class NumericRangeFilterValueTypeDef(BaseValidatorModel):
    StaticValue: Optional[float] = None
    Parameter: Optional[str] = None

class ThousandSeparatorOptionsTypeDef(BaseValidatorModel):
    Symbol: Optional[NumericSeparatorSymbolType] = None
    Visibility: Optional[VisibilityType] = None

class PercentileAggregationTypeDef(BaseValidatorModel):
    PercentileValue: Optional[float] = None

class StringParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[str]

class StringParameterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]

class PercentVisibleRangeTypeDef(BaseValidatorModel):
    From: Optional[float] = None
    To: Optional[float] = None

class PivotTableConditionalFormattingScopeTypeDef(BaseValidatorModel):
    Role: Optional[PivotTableConditionalFormattingScopeRoleType] = None

class PivotTablePaginatedReportOptionsTypeDef(BaseValidatorModel):
    VerticalOverflowVisibility: Optional[VisibilityType] = None
    OverflowColumnHeaderVisibility: Optional[VisibilityType] = None

class PivotTableFieldOptionTypeDef(BaseValidatorModel):
    FieldId: str
    CustomLabel: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class PivotTableFieldSubtotalOptionsTypeDef(BaseValidatorModel):
    FieldId: Optional[str] = None

class PivotTableRowsLabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None

class RowAlternateColorOptionsOutputTypeDef(BaseValidatorModel):
    Status: Optional[WidgetStatusType] = None
    RowAlternateColors: Optional[List[str]] = None
    UsePrimaryBackgroundColor: Optional[WidgetStatusType] = None

class RowAlternateColorOptionsTypeDef(BaseValidatorModel):
    Status: Optional[WidgetStatusType] = None
    RowAlternateColors: Optional[Sequence[str]] = None
    UsePrimaryBackgroundColor: Optional[WidgetStatusType] = None

class ProjectOperationOutputTypeDef(BaseValidatorModel):
    ProjectedColumns: List[str]

class ProjectOperationTypeDef(BaseValidatorModel):
    ProjectedColumns: Sequence[str]

class RadarChartAreaStyleSettingsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class RangeConstantTypeDef(BaseValidatorModel):
    Minimum: Optional[str] = None
    Maximum: Optional[str] = None

class RedshiftIAMParametersExtraOutputTypeDef(BaseValidatorModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[List[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None

class RedshiftIAMParametersOutputTypeDef(BaseValidatorModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[List[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None

class RedshiftIAMParametersTypeDef(BaseValidatorModel):
    RoleArn: str
    DatabaseUser: Optional[str] = None
    DatabaseGroups: Optional[Sequence[str]] = None
    AutoCreateDatabaseUser: Optional[bool] = None

class ReferenceLineCustomLabelConfigurationTypeDef(BaseValidatorModel):
    CustomLabel: str

class ReferenceLineStaticDataConfigurationTypeDef(BaseValidatorModel):
    Value: float

class ReferenceLineStyleConfigurationTypeDef(BaseValidatorModel):
    Pattern: Optional[ReferenceLinePatternTypeType] = None
    Color: Optional[str] = None

class ScheduleRefreshOnEntityTypeDef(BaseValidatorModel):
    DayOfWeek: Optional[DayOfWeekType] = None
    DayOfMonth: Optional[str] = None

class StatePersistenceConfigurationsTypeDef(BaseValidatorModel):
    Enabled: bool

class RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialTopicId: Optional[str] = None

class RegisteredUserQSearchBarEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialTopicId: Optional[str] = None

class RenameColumnOperationTypeDef(BaseValidatorModel):
    ColumnName: str
    NewColumnName: str

class RestoreAnalysisRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str

class RowLevelPermissionTagRuleTypeDef(BaseValidatorModel):
    TagKey: str
    ColumnName: str
    TagMultiValueDelimiter: Optional[str] = None
    MatchAllValue: Optional[str] = None

class S3BucketConfigurationTypeDef(BaseValidatorModel):
    BucketName: str
    BucketPrefix: str
    BucketRegion: str

class UploadSettingsTypeDef(BaseValidatorModel):
    Format: Optional[FileFormatType] = None
    StartFromRow: Optional[int] = None
    ContainsHeader: Optional[bool] = None
    TextQualifier: Optional[TextQualifierType] = None
    Delimiter: Optional[str] = None

class SpacingTypeDef(BaseValidatorModel):
    Top: Optional[str] = None
    Bottom: Optional[str] = None
    Left: Optional[str] = None
    Right: Optional[str] = None

class SheetVisualScopingConfigurationOutputTypeDef(BaseValidatorModel):
    SheetId: str
    Scope: FilterVisualScopeType
    VisualIds: Optional[List[str]] = None

class SheetVisualScopingConfigurationTypeDef(BaseValidatorModel):
    SheetId: str
    Scope: FilterVisualScopeType
    VisualIds: Optional[Sequence[str]] = None

class SemanticEntityTypeOutputTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None

class SemanticEntityTypeTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Mapping[str, str]] = None

class SemanticTypeOutputTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Dict[str, str]] = None
    TruthyCellValue: Optional[str] = None
    TruthyCellValueSynonyms: Optional[List[str]] = None
    FalseyCellValue: Optional[str] = None
    FalseyCellValueSynonyms: Optional[List[str]] = None

class SemanticTypeTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    SubTypeName: Optional[str] = None
    TypeParameters: Optional[Mapping[str, str]] = None
    TruthyCellValue: Optional[str] = None
    TruthyCellValueSynonyms: Optional[Sequence[str]] = None
    FalseyCellValue: Optional[str] = None
    FalseyCellValueSynonyms: Optional[Sequence[str]] = None

class SheetTextBoxTypeDef(BaseValidatorModel):
    SheetTextBoxId: str
    Content: Optional[str] = None

class SheetElementConfigurationOverridesTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class ShortFormatTextTypeDef(BaseValidatorModel):
    PlainText: Optional[str] = None
    RichText: Optional[str] = None

class YAxisOptionsTypeDef(BaseValidatorModel):
    YAxis: Literal["PRIMARY_Y_AXIS"]

class SmallMultiplesAxisPropertiesTypeDef(BaseValidatorModel):
    Scale: Optional[SmallMultiplesAxisScaleType] = None
    Placement: Optional[SmallMultiplesAxisPlacementType] = None

class SnapshotAnonymousUserRedactedTypeDef(BaseValidatorModel):
    RowLevelPermissionTagKeys: Optional[List[str]] = None

class SnapshotFileSheetSelectionOutputTypeDef(BaseValidatorModel):
    SheetId: str
    SelectionScope: SnapshotFileSheetSelectionScopeType
    VisualIds: Optional[List[str]] = None

class SnapshotFileSheetSelectionTypeDef(BaseValidatorModel):
    SheetId: str
    SelectionScope: SnapshotFileSheetSelectionScopeType
    VisualIds: Optional[Sequence[str]] = None

class SnapshotJobResultErrorInfoTypeDef(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[str] = None

class StringDatasetParameterDefaultValuesOutputTypeDef(BaseValidatorModel):
    StaticValues: Optional[List[str]] = None

class StringDatasetParameterDefaultValuesTypeDef(BaseValidatorModel):
    StaticValues: Optional[Sequence[str]] = None

class StringValueWhenUnsetConfigurationTypeDef(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[str] = None

class TableStyleTargetTypeDef(BaseValidatorModel):
    CellType: StyledCellTypeType

class SuccessfulKeyRegistrationEntryTypeDef(BaseValidatorModel):
    KeyArn: str
    StatusCode: int

class TableCellImageSizingConfigurationTypeDef(BaseValidatorModel):
    TableCellImageScalingConfiguration: Optional[TableCellImageScalingConfigurationType] = None

class TablePaginatedReportOptionsTypeDef(BaseValidatorModel):
    VerticalOverflowVisibility: Optional[VisibilityType] = None
    OverflowColumnHeaderVisibility: Optional[VisibilityType] = None

class TableFieldCustomIconContentTypeDef(BaseValidatorModel):
    Icon: Optional[Literal["LINK"]] = None

class TablePinnedFieldOptionsOutputTypeDef(BaseValidatorModel):
    PinnedLeftFields: Optional[List[str]] = None

class TablePinnedFieldOptionsTypeDef(BaseValidatorModel):
    PinnedLeftFields: Optional[Sequence[str]] = None

class TemplateSourceTemplateTypeDef(BaseValidatorModel):
    Arn: str

class TextControlPlaceholderOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None

class UIColorPaletteTypeDef(BaseValidatorModel):
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

class ThemeErrorTypeDef(BaseValidatorModel):
    Type: Optional[Literal["INTERNAL_FAILURE"]] = None
    Message: Optional[str] = None

class TopicSingularFilterConstantTypeDef(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None

class TotalAggregationFunctionTypeDef(BaseValidatorModel):
    SimpleTotalAggregationFunction: Optional[SimpleTotalAggregationFunctionType] = None

class UntagColumnOperationOutputTypeDef(BaseValidatorModel):
    ColumnName: str
    TagNames: List[ColumnTagNameType]

class UntagColumnOperationTypeDef(BaseValidatorModel):
    ColumnName: str
    TagNames: Sequence[ColumnTagNameType]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DefaultNamespace: str
    NotificationEmail: Optional[str] = None
    TerminationProtectionEnabled: Optional[bool] = None

class UpdateDashboardLinksRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    LinkEntities: Sequence[str]

class UpdateDashboardPublishedVersionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    VersionNumber: int

class UpdateFolderRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Name: str

class UpdateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    Description: Optional[str] = None

class UpdateIAMPolicyAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssignmentName: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    PolicyArn: Optional[str] = None
    Identities: Optional[Mapping[str, Sequence[str]]] = None

class UpdateIdentityPropagationConfigRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Service: Literal["REDSHIFT"]
    AuthorizedTargets: Optional[Sequence[str]] = None

class UpdateIpRestrictionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    IpRestrictionRuleMap: Optional[Mapping[str, str]] = None
    VpcIdRestrictionRuleMap: Optional[Mapping[str, str]] = None
    VpcEndpointIdRestrictionRuleMap: Optional[Mapping[str, str]] = None
    Enabled: Optional[bool] = None

class UpdatePublicSharingSettingsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PublicSharingEnabled: Optional[bool] = None

class UpdateRoleCustomPermissionRequestRequestTypeDef(BaseValidatorModel):
    CustomPermissionsName: str
    Role: RoleType
    AwsAccountId: str
    Namespace: str

class UpdateSPICECapacityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PurchaseMode: PurchaseModeType

class UpdateTemplateAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    AliasName: str
    TemplateVersionNumber: int

class UpdateThemeAliasRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    AliasName: str
    ThemeVersionNumber: int

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateVPCConnectionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    RoleArn: str
    DnsResolvers: Optional[Sequence[str]] = None

class WaterfallChartGroupColorConfigurationTypeDef(BaseValidatorModel):
    PositiveBarColor: Optional[str] = None
    NegativeBarColor: Optional[str] = None
    TotalBarColor: Optional[str] = None

class WaterfallChartOptionsTypeDef(BaseValidatorModel):
    TotalBarLabel: Optional[str] = None

class WordCloudOptionsTypeDef(BaseValidatorModel):
    WordOrientation: Optional[WordCloudWordOrientationType] = None
    WordScaling: Optional[WordCloudWordScalingType] = None
    CloudLayout: Optional[WordCloudCloudLayoutType] = None
    WordCasing: Optional[WordCloudWordCasingType] = None
    WordPadding: Optional[WordCloudWordPaddingType] = None
    MaximumStringLength: Optional[int] = None

class UpdateAccountCustomizationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AccountCustomization: AccountCustomizationTypeDef
    Namespace: Optional[str] = None

class AxisLabelReferenceOptionsTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef

class CascadingControlSourceTypeDef(BaseValidatorModel):
    SourceSheetControlId: Optional[str] = None
    ColumnToMatch: Optional[ColumnIdentifierTypeDef] = None

class CategoryDrillDownFilterOutputTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    CategoryValues: List[str]

class CategoryDrillDownFilterTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    CategoryValues: Sequence[str]

class ContributionAnalysisDefaultOutputTypeDef(BaseValidatorModel):
    MeasureFieldId: str
    ContributorDimensions: List[ColumnIdentifierTypeDef]

class ContributionAnalysisDefaultTypeDef(BaseValidatorModel):
    MeasureFieldId: str
    ContributorDimensions: Sequence[ColumnIdentifierTypeDef]

class DynamicDefaultValueTypeDef(BaseValidatorModel):
    DefaultValueColumn: ColumnIdentifierTypeDef
    UserNameColumn: Optional[ColumnIdentifierTypeDef] = None
    GroupNameColumn: Optional[ColumnIdentifierTypeDef] = None

class FilterOperationSelectedFieldsConfigurationOutputTypeDef(BaseValidatorModel):
    SelectedFields: Optional[List[str]] = None
    SelectedFieldOptions: Optional[Literal["ALL_FIELDS"]] = None
    SelectedColumns: Optional[List[ColumnIdentifierTypeDef]] = None

class FilterOperationSelectedFieldsConfigurationTypeDef(BaseValidatorModel):
    SelectedFields: Optional[Sequence[str]] = None
    SelectedFieldOptions: Optional[Literal["ALL_FIELDS"]] = None
    SelectedColumns: Optional[Sequence[ColumnIdentifierTypeDef]] = None

class NumericEqualityDrillDownFilterTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Value: float

class ParameterSelectableValuesOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None
    LinkToDataSetColumn: Optional[ColumnIdentifierTypeDef] = None

class ParameterSelectableValuesTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None
    LinkToDataSetColumn: Optional[ColumnIdentifierTypeDef] = None

class TimeRangeDrillDownFilterOutputTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    RangeMinimum: datetime
    RangeMaximum: datetime
    TimeGranularity: TimeGranularityType

class AnalysisErrorTypeDef(BaseValidatorModel):
    Type: Optional[AnalysisErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[EntityTypeDef]] = None

class DashboardErrorTypeDef(BaseValidatorModel):
    Type: Optional[DashboardErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[EntityTypeDef]] = None

class TemplateErrorTypeDef(BaseValidatorModel):
    Type: Optional[TemplateErrorTypeType] = None
    Message: Optional[str] = None
    ViolatedEntities: Optional[List[EntityTypeDef]] = None

class SearchAnalysesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[AnalysisSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class AnalysisSourceTemplateTypeDef(BaseValidatorModel):
    DataSetReferences: Sequence[DataSetReferenceTypeDef]
    Arn: str

class DashboardSourceTemplateTypeDef(BaseValidatorModel):
    DataSetReferences: Sequence[DataSetReferenceTypeDef]
    Arn: str

class TemplateSourceAnalysisTypeDef(BaseValidatorModel):
    Arn: str
    DataSetReferences: Sequence[DataSetReferenceTypeDef]

class AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialDashboardVisualId: DashboardVisualIdTypeDef

class RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialDashboardVisualId: DashboardVisualIdTypeDef

class ArcAxisConfigurationTypeDef(BaseValidatorModel):
    Range: Optional[ArcAxisDisplayRangeTypeDef] = None
    ReserveRange: Optional[int] = None

class AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleExportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       List[AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef]     ] = None
    RefreshSchedules: Optional[       List[AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef]     ] = None
    DataSources: Optional[       List[AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef]     ] = None
    DataSets: Optional[List[AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef]] = None
    Themes: Optional[List[AssetBundleExportJobThemeOverridePropertiesOutputTypeDef]] = None
    Analyses: Optional[List[AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef]] = None
    Dashboards: Optional[       List[AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef]     ] = None

class AssetBundleCloudFormationOverridePropertyConfigurationTypeDef(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleExportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       Sequence[AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef]     ] = None
    RefreshSchedules: Optional[       Sequence[AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef]     ] = None
    DataSources: Optional[       Sequence[AssetBundleExportJobDataSourceOverridePropertiesTypeDef]     ] = None
    DataSets: Optional[Sequence[AssetBundleExportJobDataSetOverridePropertiesTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleExportJobThemeOverridePropertiesTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleExportJobAnalysisOverridePropertiesTypeDef]] = None
    Dashboards: Optional[Sequence[AssetBundleExportJobDashboardOverridePropertiesTypeDef]] = None

class AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef(BaseValidatorModel):
    AnalysisIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef(BaseValidatorModel):
    DataSetIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef(BaseValidatorModel):
    DataSourceIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleImportJobThemeOverridePermissionsOutputTypeDef(BaseValidatorModel):
    ThemeIds: List[str]
    Permissions: AssetBundleResourcePermissionsOutputTypeDef

class AssetBundleResourceLinkSharingConfigurationOutputTypeDef(BaseValidatorModel):
    Permissions: Optional[AssetBundleResourcePermissionsOutputTypeDef] = None

class AssetBundleImportJobAnalysisOverridePermissionsTypeDef(BaseValidatorModel):
    AnalysisIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleImportJobDataSetOverridePermissionsTypeDef(BaseValidatorModel):
    DataSetIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleImportJobDataSourceOverridePermissionsTypeDef(BaseValidatorModel):
    DataSourceIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleImportJobThemeOverridePermissionsTypeDef(BaseValidatorModel):
    ThemeIds: Sequence[str]
    Permissions: AssetBundleResourcePermissionsTypeDef

class AssetBundleResourceLinkSharingConfigurationTypeDef(BaseValidatorModel):
    Permissions: Optional[AssetBundleResourcePermissionsTypeDef] = None

class AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef(BaseValidatorModel):
    AnalysisIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobAnalysisOverrideTagsTypeDef(BaseValidatorModel):
    AnalysisIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDashboardOverrideTagsOutputTypeDef(BaseValidatorModel):
    DashboardIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobDashboardOverrideTagsTypeDef(BaseValidatorModel):
    DashboardIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDataSetOverrideTagsOutputTypeDef(BaseValidatorModel):
    DataSetIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobDataSetOverrideTagsTypeDef(BaseValidatorModel):
    DataSetIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef(BaseValidatorModel):
    DataSourceIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobDataSourceOverrideTagsTypeDef(BaseValidatorModel):
    DataSourceIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobThemeOverrideTagsOutputTypeDef(BaseValidatorModel):
    ThemeIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobThemeOverrideTagsTypeDef(BaseValidatorModel):
    ThemeIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef(BaseValidatorModel):
    VPCConnectionIds: List[str]
    Tags: List[TagTypeDef]

class AssetBundleImportJobVPCConnectionOverrideTagsTypeDef(BaseValidatorModel):
    VPCConnectionIds: Sequence[str]
    Tags: Sequence[TagTypeDef]

class CreateAccountCustomizationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AccountCustomization: AccountCustomizationTypeDef
    Namespace: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateNamespaceRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    IdentityStore: Literal["QUICKSIGHT"]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVPCConnectionRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    VPCConnectionId: str
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    RoleArn: str
    DnsResolvers: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class RegisterUserRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AssetBundleImportJobDataSourceCredentialsTypeDef(BaseValidatorModel):
    CredentialPair: Optional[AssetBundleImportJobDataSourceCredentialPairTypeDef] = None
    SecretArn: Optional[str] = None

class AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef(BaseValidatorModel):
    DataSetId: str
    ScheduleId: str
    StartAfterDateTime: Optional[TimestampTypeDef] = None

class CustomParameterValuesTypeDef(BaseValidatorModel):
    StringValues: Optional[Sequence[str]] = None
    IntegerValues: Optional[Sequence[int]] = None
    DecimalValues: Optional[Sequence[float]] = None
    DateTimeValues: Optional[Sequence[TimestampTypeDef]] = None

class DateTimeDatasetParameterDefaultValuesTypeDef(BaseValidatorModel):
    StaticValues: Optional[Sequence[TimestampTypeDef]] = None

class DateTimeParameterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[TimestampTypeDef]

class DateTimeValueWhenUnsetConfigurationTypeDef(BaseValidatorModel):
    ValueWhenUnsetOption: Optional[ValueWhenUnsetOptionType] = None
    CustomValue: Optional[TimestampTypeDef] = None

class NewDefaultValuesTypeDef(BaseValidatorModel):
    StringStaticValues: Optional[Sequence[str]] = None
    DecimalStaticValues: Optional[Sequence[float]] = None
    DateTimeStaticValues: Optional[Sequence[TimestampTypeDef]] = None
    IntegerStaticValues: Optional[Sequence[int]] = None

class TimeRangeDrillDownFilterTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    RangeMinimum: TimestampTypeDef
    RangeMaximum: TimestampTypeDef
    TimeGranularity: TimeGranularityType

class TopicRefreshScheduleTypeDef(BaseValidatorModel):
    IsEnabled: bool
    BasedOnSpiceSchedule: bool
    StartingAt: Optional[TimestampTypeDef] = None
    Timezone: Optional[str] = None
    RepeatAt: Optional[str] = None
    TopicScheduleType: Optional[TopicScheduleTypeType] = None

class WhatIfPointScenarioTypeDef(BaseValidatorModel):
    Date: TimestampTypeDef
    Value: float

class WhatIfRangeScenarioTypeDef(BaseValidatorModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Value: float

class AssetBundleImportSourceTypeDef(BaseValidatorModel):
    Body: Optional[BlobTypeDef] = None
    S3Uri: Optional[str] = None

class AxisDisplayRangeOutputTypeDef(BaseValidatorModel):
    MinMax: Optional[AxisDisplayMinMaxRangeTypeDef] = None
    DataDriven: Optional[Dict[str, Any]] = None

class AxisDisplayRangeTypeDef(BaseValidatorModel):
    MinMax: Optional[AxisDisplayMinMaxRangeTypeDef] = None
    DataDriven: Optional[Mapping[str, Any]] = None

class AxisScaleTypeDef(BaseValidatorModel):
    Linear: Optional[AxisLinearScaleTypeDef] = None
    Logarithmic: Optional[AxisLogarithmicScaleTypeDef] = None

class ScatterPlotSortConfigurationTypeDef(BaseValidatorModel):
    ScatterPlotLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class HistogramBinOptionsTypeDef(BaseValidatorModel):
    SelectedBinType: Optional[HistogramBinTypeType] = None
    BinCount: Optional[BinCountOptionsTypeDef] = None
    BinWidth: Optional[BinWidthOptionsTypeDef] = None
    StartValue: Optional[float] = None

class BodySectionRepeatPageBreakConfigurationTypeDef(BaseValidatorModel):
    After: Optional[SectionAfterPageBreakTypeDef] = None

class SectionPageBreakConfigurationTypeDef(BaseValidatorModel):
    After: Optional[SectionAfterPageBreakTypeDef] = None

class TileStyleTypeDef(BaseValidatorModel):
    Border: Optional[BorderStyleTypeDef] = None

class BoxPlotOptionsTypeDef(BaseValidatorModel):
    StyleOptions: Optional[BoxPlotStyleOptionsTypeDef] = None
    OutlierVisibility: Optional[VisibilityType] = None
    AllDataPointsVisibility: Optional[VisibilityType] = None

class CreateColumnsOperationOutputTypeDef(BaseValidatorModel):
    Columns: List[CalculatedColumnTypeDef]

class CreateColumnsOperationTypeDef(BaseValidatorModel):
    Columns: Sequence[CalculatedColumnTypeDef]

class CancelIngestionResponseTypeDef(BaseValidatorModel):
    Arn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccountCustomizationResponseTypeDef(BaseValidatorModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomizationTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnalysisResponseTypeDef(BaseValidatorModel):
    Arn: str
    AnalysisId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDashboardResponseTypeDef(BaseValidatorModel):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetResponseTypeDef(BaseValidatorModel):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    DataSourceId: str
    CreationStatus: ResourceStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFolderResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIAMPolicyAssignmentResponseTypeDef(BaseValidatorModel):
    AssignmentName: str
    AssignmentId: str
    AssignmentStatus: AssignmentStatusType
    PolicyArn: str
    Identities: Dict[str, List[str]]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIngestionResponseTypeDef(BaseValidatorModel):
    Arn: str
    IngestionId: str
    IngestionStatus: IngestionStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNamespaceResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    CapacityRegion: str
    CreationStatus: NamespaceStatusType
    IdentityStore: Literal["QUICKSIGHT"]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRefreshScheduleResponseTypeDef(BaseValidatorModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoleMembershipResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(BaseValidatorModel):
    Arn: str
    VersionArn: str
    TemplateId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThemeResponseTypeDef(BaseValidatorModel):
    Arn: str
    VersionArn: str
    ThemeId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRefreshScheduleResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicResponseTypeDef(BaseValidatorModel):
    Arn: str
    TopicId: str
    RefreshArn: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVPCConnectionResponseTypeDef(BaseValidatorModel):
    Arn: str
    VPCConnectionId: str
    CreationStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountCustomizationResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountSubscriptionResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnalysisResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    AnalysisId: str
    DeletionTime: datetime
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDashboardResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    DashboardId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSetRefreshPropertiesResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSetResponseTypeDef(BaseValidatorModel):
    Arn: str
    DataSetId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    DataSourceId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFolderMembershipResponseTypeDef(BaseValidatorModel):
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFolderResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGroupMembershipResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGroupResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIAMPolicyAssignmentResponseTypeDef(BaseValidatorModel):
    AssignmentName: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdentityPropagationConfigResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRefreshScheduleResponseTypeDef(BaseValidatorModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRoleCustomPermissionResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRoleMembershipResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateAliasResponseTypeDef(BaseValidatorModel):
    Status: int
    TemplateId: str
    AliasName: str
    Arn: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Arn: str
    TemplateId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteThemeAliasResponseTypeDef(BaseValidatorModel):
    AliasName: str
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteThemeResponseTypeDef(BaseValidatorModel):
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTopicRefreshScheduleResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTopicResponseTypeDef(BaseValidatorModel):
    Arn: str
    TopicId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserByPrincipalIdResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVPCConnectionResponseTypeDef(BaseValidatorModel):
    Arn: str
    VPCConnectionId: str
    DeletionStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountCustomizationResponseTypeDef(BaseValidatorModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomizationTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountSettingsResponseTypeDef(BaseValidatorModel):
    AccountSettings: AccountSettingsTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountSubscriptionResponseTypeDef(BaseValidatorModel):
    AccountInfo: AccountInfoTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpRestrictionResponseTypeDef(BaseValidatorModel):
    AwsAccountId: str
    IpRestrictionRuleMap: Dict[str, str]
    VpcIdRestrictionRuleMap: Dict[str, str]
    VpcEndpointIdRestrictionRuleMap: Dict[str, str]
    Enabled: bool
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRoleCustomPermissionResponseTypeDef(BaseValidatorModel):
    CustomPermissionsName: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateEmbedUrlForAnonymousUserResponseTypeDef(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    AnonymousUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateEmbedUrlForRegisteredUserResponseTypeDef(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardEmbedUrlResponseTypeDef(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionEmbedUrlResponseTypeDef(BaseValidatorModel):
    EmbedUrl: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalysesResponseTypeDef(BaseValidatorModel):
    AnalysisSummaryList: List[AnalysisSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAssetBundleExportJobsResponseTypeDef(BaseValidatorModel):
    AssetBundleExportJobSummaryList: List[AssetBundleExportJobSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAssetBundleImportJobsResponseTypeDef(BaseValidatorModel):
    AssetBundleImportJobSummaryList: List[AssetBundleImportJobSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIAMPolicyAssignmentsForUserResponseTypeDef(BaseValidatorModel):
    ActiveAssignments: List[ActiveIAMPolicyAssignmentTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentityPropagationConfigsResponseTypeDef(BaseValidatorModel):
    Services: List[AuthorizedTargetsByServiceTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRoleMembershipsResponseTypeDef(BaseValidatorModel):
    MembersList: List[str]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataSetRefreshPropertiesResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreAnalysisResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    AnalysisId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAnalysesResponseTypeDef(BaseValidatorModel):
    AnalysisSummaryList: List[AnalysisSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartAssetBundleExportJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    AssetBundleExportJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssetBundleImportJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    AssetBundleImportJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartDashboardSnapshotJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    SnapshotJobId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountCustomizationResponseTypeDef(BaseValidatorModel):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: AccountCustomizationTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnalysisResponseTypeDef(BaseValidatorModel):
    Arn: str
    AnalysisId: str
    UpdateStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardLinksResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    DashboardArn: str
    LinkEntities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardPublishedVersionResponseTypeDef(BaseValidatorModel):
    DashboardId: str
    DashboardArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardResponseTypeDef(BaseValidatorModel):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetPermissionsResponseTypeDef(BaseValidatorModel):
    DataSetArn: str
    DataSetId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetResponseTypeDef(BaseValidatorModel):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourcePermissionsResponseTypeDef(BaseValidatorModel):
    DataSourceArn: str
    DataSourceId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    DataSourceId: str
    UpdateStatus: ResourceStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFolderResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIAMPolicyAssignmentResponseTypeDef(BaseValidatorModel):
    AssignmentName: str
    AssignmentId: str
    PolicyArn: str
    Identities: Dict[str, List[str]]
    AssignmentStatus: AssignmentStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityPropagationConfigResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIpRestrictionResponseTypeDef(BaseValidatorModel):
    AwsAccountId: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublicSharingSettingsResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRefreshScheduleResponseTypeDef(BaseValidatorModel):
    Status: int
    RequestId: str
    ScheduleId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoleCustomPermissionResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSPICECapacityConfigurationResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateResponseTypeDef(BaseValidatorModel):
    TemplateId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemeResponseTypeDef(BaseValidatorModel):
    ThemeId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatusType
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTopicRefreshScheduleResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTopicResponseTypeDef(BaseValidatorModel):
    TopicId: str
    Arn: str
    RefreshArn: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVPCConnectionResponseTypeDef(BaseValidatorModel):
    Arn: str
    VPCConnectionId: str
    UpdateStatus: VPCConnectionResourceStatusType
    AvailabilityStatus: VPCConnectionAvailabilityStatusType
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CategoryFilterConfigurationOutputTypeDef(BaseValidatorModel):
    FilterListConfiguration: Optional[FilterListConfigurationOutputTypeDef] = None
    CustomFilterListConfiguration: Optional[CustomFilterListConfigurationOutputTypeDef] = None
    CustomFilterConfiguration: Optional[CustomFilterConfigurationTypeDef] = None

class CategoryFilterConfigurationTypeDef(BaseValidatorModel):
    FilterListConfiguration: Optional[FilterListConfigurationTypeDef] = None
    CustomFilterListConfiguration: Optional[CustomFilterListConfigurationTypeDef] = None
    CustomFilterConfiguration: Optional[CustomFilterConfigurationTypeDef] = None

class ClusterMarkerTypeDef(BaseValidatorModel):
    SimpleClusterMarker: Optional[SimpleClusterMarkerTypeDef] = None

class TopicCategoryFilterConstantOutputTypeDef(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None
    CollectiveConstant: Optional[CollectiveConstantOutputTypeDef] = None

class TopicCategoryFilterConstantTypeDef(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    SingularConstant: Optional[str] = None
    CollectiveConstant: Optional[CollectiveConstantTypeDef] = None

class ColorScaleOutputTypeDef(BaseValidatorModel):
    Colors: List[DataColorTypeDef]
    ColorFillType: ColorFillTypeType
    NullValueColor: Optional[DataColorTypeDef] = None

class ColorScaleTypeDef(BaseValidatorModel):
    Colors: Sequence[DataColorTypeDef]
    ColorFillType: ColorFillTypeType
    NullValueColor: Optional[DataColorTypeDef] = None

class ColorsConfigurationOutputTypeDef(BaseValidatorModel):
    CustomColors: Optional[List[CustomColorTypeDef]] = None

class ColorsConfigurationTypeDef(BaseValidatorModel):
    CustomColors: Optional[Sequence[CustomColorTypeDef]] = None

class ColumnTagTypeDef(BaseValidatorModel):
    ColumnGeographicRole: Optional[GeoSpatialDataRoleType] = None
    ColumnDescription: Optional[ColumnDescriptionTypeDef] = None

class ColumnGroupSchemaOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ColumnGroupColumnSchemaList: Optional[List[ColumnGroupColumnSchemaTypeDef]] = None

class ColumnGroupSchemaTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ColumnGroupColumnSchemaList: Optional[Sequence[ColumnGroupColumnSchemaTypeDef]] = None

class ColumnGroupOutputTypeDef(BaseValidatorModel):
    GeoSpatialColumnGroup: Optional[GeoSpatialColumnGroupOutputTypeDef] = None

class ColumnGroupTypeDef(BaseValidatorModel):
    GeoSpatialColumnGroup: Optional[GeoSpatialColumnGroupTypeDef] = None

class DataSetSchemaOutputTypeDef(BaseValidatorModel):
    ColumnSchemaList: Optional[List[ColumnSchemaTypeDef]] = None

class DataSetSchemaTypeDef(BaseValidatorModel):
    ColumnSchemaList: Optional[Sequence[ColumnSchemaTypeDef]] = None

class ConditionalFormattingCustomIconConditionTypeDef(BaseValidatorModel):
    Expression: str
    IconOptions: ConditionalFormattingCustomIconOptionsTypeDef
    Color: Optional[str] = None
    DisplayConfiguration: Optional[ConditionalFormattingIconDisplayConfigurationTypeDef] = None

class CreateAccountSubscriptionResponseTypeDef(BaseValidatorModel):
    SignupResponse: SignupResponseTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    DataSetId: Optional[str] = None
    Name: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ImportMode: Optional[DataSetImportModeType] = None
    RowLevelPermissionDataSet: Optional[RowLevelPermissionDataSetTypeDef] = None
    RowLevelPermissionTagConfigurationApplied: Optional[bool] = None
    ColumnLevelPermissionRulesApplied: Optional[bool] = None

class CreateFolderMembershipResponseTypeDef(BaseValidatorModel):
    Status: int
    FolderMember: FolderMemberTypeDef
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupMembershipResponseTypeDef(BaseValidatorModel):
    GroupMember: GroupMemberTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupMembershipResponseTypeDef(BaseValidatorModel):
    GroupMember: GroupMemberTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupMembershipsResponseTypeDef(BaseValidatorModel):
    GroupMemberList: List[GroupMemberTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseValidatorModel):
    GroupList: List[GroupTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUserGroupsResponseTypeDef(BaseValidatorModel):
    GroupList: List[GroupTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchGroupsResponseTypeDef(BaseValidatorModel):
    GroupList: List[GroupTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateAliasResponseTypeDef(BaseValidatorModel):
    TemplateAlias: TemplateAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTemplateAliasResponseTypeDef(BaseValidatorModel):
    TemplateAlias: TemplateAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateAliasesResponseTypeDef(BaseValidatorModel):
    TemplateAliasList: List[TemplateAliasTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateTemplateAliasResponseTypeDef(BaseValidatorModel):
    TemplateAlias: TemplateAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThemeAliasResponseTypeDef(BaseValidatorModel):
    ThemeAlias: ThemeAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThemeAliasResponseTypeDef(BaseValidatorModel):
    ThemeAlias: ThemeAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThemeAliasesResponseTypeDef(BaseValidatorModel):
    ThemeAliasList: List[ThemeAliasTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateThemeAliasResponseTypeDef(BaseValidatorModel):
    ThemeAlias: ThemeAliasTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomActionNavigationOperationTypeDef(BaseValidatorModel):
    LocalNavigationConfiguration: Optional[LocalNavigationConfigurationTypeDef] = None

class CustomValuesConfigurationOutputTypeDef(BaseValidatorModel):
    CustomValues: CustomParameterValuesOutputTypeDef
    IncludeNullValue: Optional[bool] = None

class CustomSqlOutputTypeDef(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    SqlQuery: str
    Columns: Optional[List[InputColumnTypeDef]] = None

class CustomSqlTypeDef(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    SqlQuery: str
    Columns: Optional[Sequence[InputColumnTypeDef]] = None

class RelationalTableOutputTypeDef(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    InputColumns: List[InputColumnTypeDef]
    Catalog: Optional[str] = None
    Schema: Optional[str] = None

class RelationalTableTypeDef(BaseValidatorModel):
    DataSourceArn: str
    Name: str
    InputColumns: Sequence[InputColumnTypeDef]
    Catalog: Optional[str] = None
    Schema: Optional[str] = None

class VisualInteractionOptionsTypeDef(BaseValidatorModel):
    VisualMenuOption: Optional[VisualMenuOptionTypeDef] = None
    ContextMenuOption: Optional[ContextMenuOptionTypeDef] = None

class SearchDashboardsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[DashboardSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDashboardsResponseTypeDef(BaseValidatorModel):
    DashboardSummaryList: List[DashboardSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchDashboardsResponseTypeDef(BaseValidatorModel):
    DashboardSummaryList: List[DashboardSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDashboardVersionsResponseTypeDef(BaseValidatorModel):
    DashboardVersionSummaryList: List[DashboardVersionSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DashboardVisualPublishOptionsTypeDef(BaseValidatorModel):
    ExportHiddenFieldsOption: Optional[ExportHiddenFieldsOptionTypeDef] = None

class TableInlineVisualizationTypeDef(BaseValidatorModel):
    DataBars: Optional[DataBarsOptionsTypeDef] = None

class DataLabelTypeTypeDef(BaseValidatorModel):
    FieldLabelType: Optional[FieldLabelTypeTypeDef] = None
    DataPathLabelType: Optional[DataPathLabelTypeTypeDef] = None
    RangeEndsLabelType: Optional[RangeEndsLabelTypeTypeDef] = None
    MinimumLabelType: Optional[MinimumLabelTypeTypeDef] = None
    MaximumLabelType: Optional[MaximumLabelTypeTypeDef] = None

class DataPathValueTypeDef(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldValue: Optional[str] = None
    DataPathType: Optional[DataPathTypeTypeDef] = None

class SearchDataSetsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[DataSetSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[DataSourceSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchDataSourcesResponseTypeDef(BaseValidatorModel):
    DataSourceSummaries: List[DataSourceSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DateTimeDatasetParameterOutputTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultValues: Optional[DateTimeDatasetParameterDefaultValuesOutputTypeDef] = None

class TimeRangeFilterValueOutputTypeDef(BaseValidatorModel):
    StaticValue: Optional[datetime] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    Parameter: Optional[str] = None

class TimeRangeFilterValueTypeDef(BaseValidatorModel):
    StaticValue: Optional[TimestampTypeDef] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    Parameter: Optional[str] = None

class DecimalDatasetParameterOutputTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[DecimalDatasetParameterDefaultValuesOutputTypeDef] = None

class DecimalDatasetParameterTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[DecimalDatasetParameterDefaultValuesTypeDef] = None

class DescribeAnalysisPermissionsResponseTypeDef(BaseValidatorModel):
    AnalysisId: str
    AnalysisArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSetPermissionsResponseTypeDef(BaseValidatorModel):
    DataSetArn: str
    DataSetId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSourcePermissionsResponseTypeDef(BaseValidatorModel):
    DataSourceArn: str
    DataSourceId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTemplatePermissionsResponseTypeDef(BaseValidatorModel):
    TemplateId: str
    TemplateArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThemePermissionsResponseTypeDef(BaseValidatorModel):
    ThemeId: str
    ThemeArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTopicPermissionsResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class LinkSharingConfigurationOutputTypeDef(BaseValidatorModel):
    Permissions: Optional[List[ResourcePermissionOutputTypeDef]] = None

class UpdateAnalysisPermissionsResponseTypeDef(BaseValidatorModel):
    AnalysisArn: str
    AnalysisId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFolderPermissionsResponseTypeDef(BaseValidatorModel):
    Status: int
    Arn: str
    FolderId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplatePermissionsResponseTypeDef(BaseValidatorModel):
    TemplateId: str
    TemplateArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemePermissionsResponseTypeDef(BaseValidatorModel):
    ThemeId: str
    ThemeArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTopicPermissionsResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFolderPermissionsRequestDescribeFolderPermissionsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalysesRequestListAnalysesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardsRequestListDashboardsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetsRequestListDataSetsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFolderMembersRequestListFolderMembersPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFoldersRequestListFoldersPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    UserName: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    AssignmentStatus: Optional[AssignmentStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngestionsRequestListIngestionsPaginateTypeDef(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestListNamespacesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoleMembershipsRequestListRoleMembershipsPaginateTypeDef(BaseValidatorModel):
    Role: RoleType
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesRequestListTemplatesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThemeVersionsRequestListThemeVersionsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThemesRequestListThemesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Type: Optional[ThemeTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserGroupsRequestListUserGroupsPaginateTypeDef(BaseValidatorModel):
    UserName: str
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchAnalysesRequestSearchAnalysesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[AnalysisSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchDashboardsRequestSearchDashboardsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[DashboardSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchDataSetsRequestSearchDataSetsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[DataSetSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[DataSourceSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFolderPermissionsResponseTypeDef(BaseValidatorModel):
    Status: int
    FolderId: str
    Arn: str
    Permissions: List[ResourcePermissionExtraOutputTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFolderResolvedPermissionsResponseTypeDef(BaseValidatorModel):
    Status: int
    FolderId: str
    Arn: str
    Permissions: List[ResourcePermissionExtraOutputTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFolderResponseTypeDef(BaseValidatorModel):
    Status: int
    Folder: FolderTypeDef
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIAMPolicyAssignmentResponseTypeDef(BaseValidatorModel):
    IAMPolicyAssignment: IAMPolicyAssignmentTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyRegistrationResponseTypeDef(BaseValidatorModel):
    AwsAccountId: str
    KeyRegistration: List[RegisteredCustomerManagedKeyTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKeyRegistrationRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    KeyRegistration: Sequence[RegisteredCustomerManagedKeyTypeDef]

class DescribeTopicRefreshResponseTypeDef(BaseValidatorModel):
    RefreshDetails: TopicRefreshDetailsTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTopicRefreshScheduleResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    DatasetArn: str
    RefreshSchedule: TopicRefreshScheduleOutputTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TopicRefreshScheduleSummaryTypeDef(BaseValidatorModel):
    DatasetId: Optional[str] = None
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    RefreshSchedule: Optional[TopicRefreshScheduleOutputTypeDef] = None

class DescribeUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseValidatorModel):
    UserList: List[UserTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    UserInvitationUrl: str
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class DisplayFormatOptionsTypeDef(BaseValidatorModel):
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

class DonutOptionsTypeDef(BaseValidatorModel):
    ArcOptions: Optional[ArcOptionsTypeDef] = None
    DonutCenterOptions: Optional[DonutCenterOptionsTypeDef] = None

class FilterOperationTargetVisualsConfigurationOutputTypeDef(BaseValidatorModel):
    SameSheetTargetVisualConfiguration: Optional[       SameSheetTargetVisualConfigurationOutputTypeDef     ] = None

class FilterOperationTargetVisualsConfigurationTypeDef(BaseValidatorModel):
    SameSheetTargetVisualConfiguration: Optional[       SameSheetTargetVisualConfigurationTypeDef     ] = None

class SearchFoldersRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[FolderSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchFoldersRequestSearchFoldersPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Filters: Sequence[FolderSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFoldersResponseTypeDef(BaseValidatorModel):
    Status: int
    FolderSummaryList: List[FolderSummaryTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchFoldersResponseTypeDef(BaseValidatorModel):
    Status: int
    FolderSummaryList: List[FolderSummaryTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FontConfigurationTypeDef(BaseValidatorModel):
    FontSize: Optional[FontSizeTypeDef] = None
    FontDecoration: Optional[FontDecorationType] = None
    FontColor: Optional[str] = None
    FontWeight: Optional[FontWeightTypeDef] = None
    FontStyle: Optional[FontStyleType] = None

class TypographyOutputTypeDef(BaseValidatorModel):
    FontFamilies: Optional[List[FontTypeDef]] = None

class TypographyTypeDef(BaseValidatorModel):
    FontFamilies: Optional[Sequence[FontTypeDef]] = None

class ForecastScenarioOutputTypeDef(BaseValidatorModel):
    WhatIfPointScenario: Optional[WhatIfPointScenarioOutputTypeDef] = None
    WhatIfRangeScenario: Optional[WhatIfRangeScenarioOutputTypeDef] = None

class FreeFormLayoutCanvasSizeOptionsTypeDef(BaseValidatorModel):
    ScreenCanvasSizeOptions: Optional[FreeFormLayoutScreenCanvasSizeOptionsTypeDef] = None

class SnapshotAnonymousUserTypeDef(BaseValidatorModel):
    RowLevelPermissionTags: Optional[Sequence[SessionTagTypeDef]] = None

class GeospatialWindowOptionsTypeDef(BaseValidatorModel):
    Bounds: Optional[GeospatialCoordinateBoundsTypeDef] = None
    MapZoomMode: Optional[MapZoomModeType] = None

class GeospatialHeatmapColorScaleOutputTypeDef(BaseValidatorModel):
    Colors: Optional[List[GeospatialHeatmapDataColorTypeDef]] = None

class GeospatialHeatmapColorScaleTypeDef(BaseValidatorModel):
    Colors: Optional[Sequence[GeospatialHeatmapDataColorTypeDef]] = None

class TableSideBorderOptionsTypeDef(BaseValidatorModel):
    InnerVertical: Optional[TableBorderOptionsTypeDef] = None
    InnerHorizontal: Optional[TableBorderOptionsTypeDef] = None
    Left: Optional[TableBorderOptionsTypeDef] = None
    Right: Optional[TableBorderOptionsTypeDef] = None
    Top: Optional[TableBorderOptionsTypeDef] = None
    Bottom: Optional[TableBorderOptionsTypeDef] = None

class GradientColorOutputTypeDef(BaseValidatorModel):
    Stops: Optional[List[GradientStopTypeDef]] = None

class GradientColorTypeDef(BaseValidatorModel):
    Stops: Optional[Sequence[GradientStopTypeDef]] = None

class GridLayoutCanvasSizeOptionsTypeDef(BaseValidatorModel):
    ScreenCanvasSizeOptions: Optional[GridLayoutScreenCanvasSizeOptionsTypeDef] = None

class SearchGroupsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    Filters: Sequence[GroupSearchFilterTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchGroupsRequestSearchGroupsPaginateTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    Filters: Sequence[GroupSearchFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIAMPolicyAssignmentsResponseTypeDef(BaseValidatorModel):
    IAMPolicyAssignments: List[IAMPolicyAssignmentSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IncrementalRefreshTypeDef(BaseValidatorModel):
    LookbackWindow: LookbackWindowTypeDef

class IngestionTypeDef(BaseValidatorModel):
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

class IntegerDatasetParameterOutputTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[IntegerDatasetParameterDefaultValuesOutputTypeDef] = None

class IntegerDatasetParameterTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[IntegerDatasetParameterDefaultValuesTypeDef] = None

class JoinInstructionTypeDef(BaseValidatorModel):
    LeftOperand: str
    RightOperand: str
    Type: JoinTypeType
    OnClause: str
    LeftJoinKeyProperties: Optional[JoinKeyPropertiesTypeDef] = None
    RightJoinKeyProperties: Optional[JoinKeyPropertiesTypeDef] = None

class KPIVisualLayoutOptionsTypeDef(BaseValidatorModel):
    StandardLayout: Optional[KPIVisualStandardLayoutTypeDef] = None

class LineChartDefaultSeriesSettingsTypeDef(BaseValidatorModel):
    AxisBinding: Optional[AxisBindingType] = None
    LineStyleSettings: Optional[LineChartLineStyleSettingsTypeDef] = None
    MarkerStyleSettings: Optional[LineChartMarkerStyleSettingsTypeDef] = None

class LineChartSeriesSettingsTypeDef(BaseValidatorModel):
    LineStyleSettings: Optional[LineChartLineStyleSettingsTypeDef] = None
    MarkerStyleSettings: Optional[LineChartMarkerStyleSettingsTypeDef] = None

class LinkSharingConfigurationTypeDef(BaseValidatorModel):
    Permissions: Optional[Sequence[ResourcePermissionTypeDef]] = None

class ListFolderMembersResponseTypeDef(BaseValidatorModel):
    Status: int
    FolderMemberList: List[MemberIdArnPairTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTemplateVersionsResponseTypeDef(BaseValidatorModel):
    TemplateVersionSummaryList: List[TemplateVersionSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTemplatesResponseTypeDef(BaseValidatorModel):
    TemplateSummaryList: List[TemplateSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListThemeVersionsResponseTypeDef(BaseValidatorModel):
    ThemeVersionSummaryList: List[ThemeVersionSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListThemesResponseTypeDef(BaseValidatorModel):
    ThemeSummaryList: List[ThemeSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTopicsResponseTypeDef(BaseValidatorModel):
    TopicsSummaries: List[TopicSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VisualSubtitleLabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FormatText: Optional[LongFormatTextTypeDef] = None

class S3ParametersTypeDef(BaseValidatorModel):
    ManifestFileLocation: ManifestFileLocationTypeDef
    RoleArn: Optional[str] = None

class TileLayoutStyleTypeDef(BaseValidatorModel):
    Gutter: Optional[GutterStyleTypeDef] = None
    Margin: Optional[MarginStyleTypeDef] = None

class NamedEntityDefinitionOutputTypeDef(BaseValidatorModel):
    FieldName: Optional[str] = None
    PropertyName: Optional[str] = None
    PropertyRole: Optional[PropertyRoleType] = None
    PropertyUsage: Optional[PropertyUsageType] = None
    Metric: Optional[NamedEntityDefinitionMetricOutputTypeDef] = None

class NamedEntityDefinitionTypeDef(BaseValidatorModel):
    FieldName: Optional[str] = None
    PropertyName: Optional[str] = None
    PropertyRole: Optional[PropertyRoleType] = None
    PropertyUsage: Optional[PropertyUsageType] = None
    Metric: Optional[NamedEntityDefinitionMetricTypeDef] = None

class NamespaceInfoV2TypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    CapacityRegion: Optional[str] = None
    CreationStatus: Optional[NamespaceStatusType] = None
    IdentityStore: Optional[Literal["QUICKSIGHT"]] = None
    NamespaceError: Optional[NamespaceErrorTypeDef] = None

class VPCConnectionSummaryTypeDef(BaseValidatorModel):
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

class VPCConnectionTypeDef(BaseValidatorModel):
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

class OverrideDatasetParameterOperationOutputTypeDef(BaseValidatorModel):
    ParameterName: str
    NewParameterName: Optional[str] = None
    NewDefaultValues: Optional[NewDefaultValuesOutputTypeDef] = None

class NumericSeparatorConfigurationTypeDef(BaseValidatorModel):
    DecimalSeparator: Optional[NumericSeparatorSymbolType] = None
    ThousandsSeparator: Optional[ThousandSeparatorOptionsTypeDef] = None

class NumericalAggregationFunctionTypeDef(BaseValidatorModel):
    SimpleNumericalAggregation: Optional[SimpleNumericalAggregationFunctionType] = None
    PercentileAggregation: Optional[PercentileAggregationTypeDef] = None

class ParametersOutputTypeDef(BaseValidatorModel):
    StringParameters: Optional[List[StringParameterOutputTypeDef]] = None
    IntegerParameters: Optional[List[IntegerParameterOutputTypeDef]] = None
    DecimalParameters: Optional[List[DecimalParameterOutputTypeDef]] = None
    DateTimeParameters: Optional[List[DateTimeParameterOutputTypeDef]] = None

class VisibleRangeOptionsTypeDef(BaseValidatorModel):
    PercentRange: Optional[PercentVisibleRangeTypeDef] = None

class RadarChartSeriesSettingsTypeDef(BaseValidatorModel):
    AreaStyleSettings: Optional[RadarChartAreaStyleSettingsTypeDef] = None

class TopicRangeFilterConstantTypeDef(BaseValidatorModel):
    ConstantType: Optional[ConstantTypeType] = None
    RangeConstant: Optional[RangeConstantTypeDef] = None

class RedshiftParametersExtraOutputTypeDef(BaseValidatorModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersExtraOutputTypeDef] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None

class RedshiftParametersOutputTypeDef(BaseValidatorModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersOutputTypeDef] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None

class RedshiftParametersTypeDef(BaseValidatorModel):
    Database: str
    Host: Optional[str] = None
    Port: Optional[int] = None
    ClusterId: Optional[str] = None
    IAMParameters: Optional[RedshiftIAMParametersTypeDef] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None

class RefreshFrequencyTypeDef(BaseValidatorModel):
    Interval: RefreshIntervalType
    RefreshOnDay: Optional[ScheduleRefreshOnEntityTypeDef] = None
    Timezone: Optional[str] = None
    TimeOfTheDay: Optional[str] = None

class RegisteredUserConsoleFeatureConfigurationsTypeDef(BaseValidatorModel):
    StatePersistence: Optional[StatePersistenceConfigurationsTypeDef] = None

class RegisteredUserDashboardFeatureConfigurationsTypeDef(BaseValidatorModel):
    StatePersistence: Optional[StatePersistenceConfigurationsTypeDef] = None
    Bookmarks: Optional[BookmarksConfigurationsTypeDef] = None

class RowLevelPermissionTagConfigurationOutputTypeDef(BaseValidatorModel):
    TagRules: List[RowLevelPermissionTagRuleTypeDef]
    Status: Optional[StatusType] = None
    TagRuleConfigurations: Optional[List[List[str]]] = None

class RowLevelPermissionTagConfigurationTypeDef(BaseValidatorModel):
    TagRules: Sequence[RowLevelPermissionTagRuleTypeDef]
    Status: Optional[StatusType] = None
    TagRuleConfigurations: Optional[Sequence[Sequence[str]]] = None

class SnapshotS3DestinationConfigurationTypeDef(BaseValidatorModel):
    BucketConfiguration: S3BucketConfigurationTypeDef

class S3SourceOutputTypeDef(BaseValidatorModel):
    DataSourceArn: str
    InputColumns: List[InputColumnTypeDef]
    UploadSettings: Optional[UploadSettingsTypeDef] = None

class S3SourceTypeDef(BaseValidatorModel):
    DataSourceArn: str
    InputColumns: Sequence[InputColumnTypeDef]
    UploadSettings: Optional[UploadSettingsTypeDef] = None

class SectionBasedLayoutPaperCanvasSizeOptionsTypeDef(BaseValidatorModel):
    PaperSize: Optional[PaperSizeType] = None
    PaperOrientation: Optional[PaperOrientationType] = None
    PaperMargin: Optional[SpacingTypeDef] = None

class SectionStyleTypeDef(BaseValidatorModel):
    Height: Optional[str] = None
    Padding: Optional[SpacingTypeDef] = None

class SelectedSheetsFilterScopeConfigurationOutputTypeDef(BaseValidatorModel):
    SheetVisualScopingConfigurations: Optional[       List[SheetVisualScopingConfigurationOutputTypeDef]     ] = None

class SelectedSheetsFilterScopeConfigurationTypeDef(BaseValidatorModel):
    SheetVisualScopingConfigurations: Optional[       Sequence[SheetVisualScopingConfigurationTypeDef]     ] = None

class SheetElementRenderingRuleTypeDef(BaseValidatorModel):
    Expression: str
    ConfigurationOverrides: SheetElementConfigurationOverridesTypeDef

class VisualTitleLabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FormatText: Optional[ShortFormatTextTypeDef] = None

class SingleAxisOptionsTypeDef(BaseValidatorModel):
    YAxisOptions: Optional[YAxisOptionsTypeDef] = None

class SnapshotUserConfigurationRedactedTypeDef(BaseValidatorModel):
    AnonymousUsers: Optional[List[SnapshotAnonymousUserRedactedTypeDef]] = None

class SnapshotFileOutputTypeDef(BaseValidatorModel):
    SheetSelections: List[SnapshotFileSheetSelectionOutputTypeDef]
    FormatType: SnapshotFileFormatTypeType

class SnapshotFileTypeDef(BaseValidatorModel):
    SheetSelections: Sequence[SnapshotFileSheetSelectionTypeDef]
    FormatType: SnapshotFileFormatTypeType

class StringDatasetParameterOutputTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[StringDatasetParameterDefaultValuesOutputTypeDef] = None

class StringDatasetParameterTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    DefaultValues: Optional[StringDatasetParameterDefaultValuesTypeDef] = None

class UpdateKeyRegistrationResponseTypeDef(BaseValidatorModel):
    FailedKeyRegistration: List[FailedKeyRegistrationEntryTypeDef]
    SuccessfulKeyRegistration: List[SuccessfulKeyRegistrationEntryTypeDef]
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TableFieldImageConfigurationTypeDef(BaseValidatorModel):
    SizingOptions: Optional[TableCellImageSizingConfigurationTypeDef] = None

class TopicNumericEqualityFilterTypeDef(BaseValidatorModel):
    Constant: Optional[TopicSingularFilterConstantTypeDef] = None
    Aggregation: Optional[NamedFilterAggTypeType] = None

class TopicRelativeDateFilterTypeDef(BaseValidatorModel):
    TimeGranularity: Optional[TopicTimeGranularityType] = None
    RelativeDateFilterFunction: Optional[TopicRelativeDateFilterFunctionType] = None
    Constant: Optional[TopicSingularFilterConstantTypeDef] = None

class TotalAggregationOptionTypeDef(BaseValidatorModel):
    FieldId: str
    TotalAggregationFunction: TotalAggregationFunctionTypeDef

class WaterfallChartColorConfigurationTypeDef(BaseValidatorModel):
    GroupColorConfiguration: Optional[WaterfallChartGroupColorConfigurationTypeDef] = None

class CascadingControlConfigurationOutputTypeDef(BaseValidatorModel):
    SourceControls: Optional[List[CascadingControlSourceTypeDef]] = None

class CascadingControlConfigurationTypeDef(BaseValidatorModel):
    SourceControls: Optional[Sequence[CascadingControlSourceTypeDef]] = None

class DateTimeDefaultValuesOutputTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[datetime]] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None

class DateTimeDefaultValuesTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[TimestampTypeDef]] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None

class DecimalDefaultValuesOutputTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[float]] = None

class DecimalDefaultValuesTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[float]] = None

class IntegerDefaultValuesOutputTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[int]] = None

class IntegerDefaultValuesTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[int]] = None

class StringDefaultValuesOutputTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[List[str]] = None

class StringDefaultValuesTypeDef(BaseValidatorModel):
    DynamicValue: Optional[DynamicDefaultValueTypeDef] = None
    StaticValues: Optional[Sequence[str]] = None

class DrillDownFilterOutputTypeDef(BaseValidatorModel):
    NumericEqualityFilter: Optional[NumericEqualityDrillDownFilterTypeDef] = None
    CategoryFilter: Optional[CategoryDrillDownFilterOutputTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeDrillDownFilterOutputTypeDef] = None

class AnalysisTypeDef(BaseValidatorModel):
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

class DashboardVersionTypeDef(BaseValidatorModel):
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

class AnalysisSourceEntityTypeDef(BaseValidatorModel):
    SourceTemplate: Optional[AnalysisSourceTemplateTypeDef] = None

class DashboardSourceEntityTypeDef(BaseValidatorModel):
    SourceTemplate: Optional[DashboardSourceTemplateTypeDef] = None

class TemplateSourceEntityTypeDef(BaseValidatorModel):
    SourceAnalysis: Optional[TemplateSourceAnalysisTypeDef] = None
    SourceTemplate: Optional[TemplateSourceTemplateTypeDef] = None

class AnonymousUserEmbeddingExperienceConfigurationTypeDef(BaseValidatorModel):
    Dashboard: Optional[AnonymousUserDashboardEmbeddingConfigurationTypeDef] = None
    DashboardVisual: Optional[AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef] = None
    QSearchBar: Optional[AnonymousUserQSearchBarEmbeddingConfigurationTypeDef] = None
    GenerativeQnA: Optional[AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef] = None

class DescribeAssetBundleExportJobResponseTypeDef(BaseValidatorModel):
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

class StartAssetBundleExportJobRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleExportJobId: str
    ResourceArns: Sequence[str]
    ExportFormat: AssetBundleExportFormatType
    IncludeAllDependencies: Optional[bool] = None
    CloudFormationOverridePropertyConfiguration: Optional[       AssetBundleCloudFormationOverridePropertyConfigurationTypeDef     ] = None
    IncludePermissions: Optional[bool] = None
    IncludeTags: Optional[bool] = None
    ValidationStrategy: Optional[AssetBundleExportJobValidationStrategyTypeDef] = None

class AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef(BaseValidatorModel):
    DashboardIds: List[str]
    Permissions: Optional[AssetBundleResourcePermissionsOutputTypeDef] = None
    LinkSharingConfiguration: Optional[       AssetBundleResourceLinkSharingConfigurationOutputTypeDef     ] = None

class AssetBundleImportJobDashboardOverridePermissionsTypeDef(BaseValidatorModel):
    DashboardIds: Sequence[str]
    Permissions: Optional[AssetBundleResourcePermissionsTypeDef] = None
    LinkSharingConfiguration: Optional[AssetBundleResourceLinkSharingConfigurationTypeDef] = None

class AssetBundleImportJobOverrideTagsOutputTypeDef(BaseValidatorModel):
    VPCConnections: Optional[       List[AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef]     ] = None
    DataSources: Optional[List[AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef]] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideTagsOutputTypeDef]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideTagsOutputTypeDef]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideTagsOutputTypeDef]] = None

class AssetBundleImportJobOverrideTagsTypeDef(BaseValidatorModel):
    VPCConnections: Optional[       Sequence[AssetBundleImportJobVPCConnectionOverrideTagsTypeDef]     ] = None
    DataSources: Optional[Sequence[AssetBundleImportJobDataSourceOverrideTagsTypeDef]] = None
    DataSets: Optional[Sequence[AssetBundleImportJobDataSetOverrideTagsTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleImportJobThemeOverrideTagsTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleImportJobAnalysisOverrideTagsTypeDef]] = None
    Dashboards: Optional[Sequence[AssetBundleImportJobDashboardOverrideTagsTypeDef]] = None

class CustomValuesConfigurationTypeDef(BaseValidatorModel):
    CustomValues: CustomParameterValuesTypeDef
    IncludeNullValue: Optional[bool] = None

class DateTimeDatasetParameterTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ValueType: DatasetParameterValueTypeType
    TimeGranularity: Optional[TimeGranularityType] = None
    DefaultValues: Optional[DateTimeDatasetParameterDefaultValuesTypeDef] = None

class ParametersTypeDef(BaseValidatorModel):
    StringParameters: Optional[Sequence[StringParameterTypeDef]] = None
    IntegerParameters: Optional[Sequence[IntegerParameterTypeDef]] = None
    DecimalParameters: Optional[Sequence[DecimalParameterTypeDef]] = None
    DateTimeParameters: Optional[Sequence[DateTimeParameterTypeDef]] = None

class OverrideDatasetParameterOperationTypeDef(BaseValidatorModel):
    ParameterName: str
    NewParameterName: Optional[str] = None
    NewDefaultValues: Optional[NewDefaultValuesTypeDef] = None

class DrillDownFilterTypeDef(BaseValidatorModel):
    NumericEqualityFilter: Optional[NumericEqualityDrillDownFilterTypeDef] = None
    CategoryFilter: Optional[CategoryDrillDownFilterTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeDrillDownFilterTypeDef] = None

class CreateTopicRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetArn: str
    RefreshSchedule: TopicRefreshScheduleTypeDef
    DatasetName: Optional[str] = None

class UpdateTopicRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    DatasetId: str
    RefreshSchedule: TopicRefreshScheduleTypeDef

class ForecastScenarioTypeDef(BaseValidatorModel):
    WhatIfPointScenario: Optional[WhatIfPointScenarioTypeDef] = None
    WhatIfRangeScenario: Optional[WhatIfRangeScenarioTypeDef] = None

class NumericAxisOptionsOutputTypeDef(BaseValidatorModel):
    Scale: Optional[AxisScaleTypeDef] = None
    Range: Optional[AxisDisplayRangeOutputTypeDef] = None

class NumericAxisOptionsTypeDef(BaseValidatorModel):
    Scale: Optional[AxisScaleTypeDef] = None
    Range: Optional[AxisDisplayRangeTypeDef] = None

class ClusterMarkerConfigurationTypeDef(BaseValidatorModel):
    ClusterMarker: Optional[ClusterMarkerTypeDef] = None

class TopicCategoryFilterOutputTypeDef(BaseValidatorModel):
    CategoryFilterFunction: Optional[CategoryFilterFunctionType] = None
    CategoryFilterType: Optional[CategoryFilterTypeType] = None
    Constant: Optional[TopicCategoryFilterConstantOutputTypeDef] = None
    Inverse: Optional[bool] = None

class TopicCategoryFilterTypeDef(BaseValidatorModel):
    CategoryFilterFunction: Optional[CategoryFilterFunctionType] = None
    CategoryFilterType: Optional[CategoryFilterTypeType] = None
    Constant: Optional[TopicCategoryFilterConstantTypeDef] = None
    Inverse: Optional[bool] = None

class TagColumnOperationOutputTypeDef(BaseValidatorModel):
    ColumnName: str
    Tags: List[ColumnTagTypeDef]

class TagColumnOperationTypeDef(BaseValidatorModel):
    ColumnName: str
    Tags: Sequence[ColumnTagTypeDef]

class DataSetConfigurationOutputTypeDef(BaseValidatorModel):
    Placeholder: Optional[str] = None
    DataSetSchema: Optional[DataSetSchemaOutputTypeDef] = None
    ColumnGroupSchemaList: Optional[List[ColumnGroupSchemaOutputTypeDef]] = None

class DataSetConfigurationTypeDef(BaseValidatorModel):
    Placeholder: Optional[str] = None
    DataSetSchema: Optional[DataSetSchemaTypeDef] = None
    ColumnGroupSchemaList: Optional[Sequence[ColumnGroupSchemaTypeDef]] = None

class ConditionalFormattingIconTypeDef(BaseValidatorModel):
    IconSet: Optional[ConditionalFormattingIconSetTypeDef] = None
    CustomCondition: Optional[ConditionalFormattingCustomIconConditionTypeDef] = None

class ListDataSetsResponseTypeDef(BaseValidatorModel):
    DataSetSummaries: List[DataSetSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchDataSetsResponseTypeDef(BaseValidatorModel):
    DataSetSummaries: List[DataSetSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DestinationParameterValueConfigurationOutputTypeDef(BaseValidatorModel):
    CustomValuesConfiguration: Optional[CustomValuesConfigurationOutputTypeDef] = None
    SelectAllValueOptions: Optional[Literal["ALL_VALUES"]] = None
    SourceParameterName: Optional[str] = None
    SourceField: Optional[str] = None
    SourceColumn: Optional[ColumnIdentifierTypeDef] = None

class CustomContentConfigurationTypeDef(BaseValidatorModel):
    ContentUrl: Optional[str] = None
    ContentType: Optional[CustomContentTypeType] = None
    ImageScaling: Optional[CustomContentImageScalingConfigurationType] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class DashboardPublishOptionsTypeDef(BaseValidatorModel):
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

class DataPathColorTypeDef(BaseValidatorModel):
    Element: DataPathValueTypeDef
    Color: str
    TimeGranularity: Optional[TimeGranularityType] = None

class DataPathSortOutputTypeDef(BaseValidatorModel):
    Direction: SortDirectionType
    SortPaths: List[DataPathValueTypeDef]

class DataPathSortTypeDef(BaseValidatorModel):
    Direction: SortDirectionType
    SortPaths: Sequence[DataPathValueTypeDef]

class PivotTableDataPathOptionOutputTypeDef(BaseValidatorModel):
    DataPathList: List[DataPathValueTypeDef]
    Width: Optional[str] = None

class PivotTableDataPathOptionTypeDef(BaseValidatorModel):
    DataPathList: Sequence[DataPathValueTypeDef]
    Width: Optional[str] = None

class PivotTableFieldCollapseStateTargetOutputTypeDef(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldDataPathValues: Optional[List[DataPathValueTypeDef]] = None

class PivotTableFieldCollapseStateTargetTypeDef(BaseValidatorModel):
    FieldId: Optional[str] = None
    FieldDataPathValues: Optional[Sequence[DataPathValueTypeDef]] = None

class DescribeDashboardPermissionsResponseTypeDef(BaseValidatorModel):
    DashboardId: str
    DashboardArn: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    Status: int
    RequestId: str
    LinkSharingConfiguration: LinkSharingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardPermissionsResponseTypeDef(BaseValidatorModel):
    DashboardArn: str
    DashboardId: str
    Permissions: List[ResourcePermissionOutputTypeDef]
    RequestId: str
    Status: int
    LinkSharingConfiguration: LinkSharingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicRefreshSchedulesResponseTypeDef(BaseValidatorModel):
    TopicId: str
    TopicArn: str
    RefreshSchedules: List[TopicRefreshScheduleSummaryTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DefaultFormattingTypeDef(BaseValidatorModel):
    DisplayFormat: Optional[DisplayFormatType] = None
    DisplayFormatOptions: Optional[DisplayFormatOptionsTypeDef] = None

class CustomActionFilterOperationOutputTypeDef(BaseValidatorModel):
    SelectedFieldsConfiguration: FilterOperationSelectedFieldsConfigurationOutputTypeDef
    TargetVisualsConfiguration: FilterOperationTargetVisualsConfigurationOutputTypeDef

class CustomActionFilterOperationTypeDef(BaseValidatorModel):
    SelectedFieldsConfiguration: FilterOperationSelectedFieldsConfigurationTypeDef
    TargetVisualsConfiguration: FilterOperationTargetVisualsConfigurationTypeDef

class AxisLabelOptionsTypeDef(BaseValidatorModel):
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    CustomLabel: Optional[str] = None
    ApplyTo: Optional[AxisLabelReferenceOptionsTypeDef] = None

class DataLabelOptionsOutputTypeDef(BaseValidatorModel):
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

class DataLabelOptionsTypeDef(BaseValidatorModel):
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

class FunnelChartDataLabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    CategoryLabelVisibility: Optional[VisibilityType] = None
    MeasureLabelVisibility: Optional[VisibilityType] = None
    Position: Optional[DataLabelPositionType] = None
    LabelFontConfiguration: Optional[FontConfigurationTypeDef] = None
    LabelColor: Optional[str] = None
    MeasureDataLabelStyle: Optional[FunnelChartMeasureDataLabelStyleType] = None

class LabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    CustomLabel: Optional[str] = None

class PanelTitleOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    HorizontalTextAlignment: Optional[HorizontalTextAlignmentType] = None

class TableFieldCustomTextContentTypeDef(BaseValidatorModel):
    FontConfiguration: FontConfigurationTypeDef
    Value: Optional[str] = None

class ForecastConfigurationOutputTypeDef(BaseValidatorModel):
    ForecastProperties: Optional[TimeBasedForecastPropertiesTypeDef] = None
    Scenario: Optional[ForecastScenarioOutputTypeDef] = None

class DefaultFreeFormLayoutConfigurationTypeDef(BaseValidatorModel):
    CanvasSizeOptions: FreeFormLayoutCanvasSizeOptionsTypeDef

class SnapshotUserConfigurationTypeDef(BaseValidatorModel):
    AnonymousUsers: Optional[Sequence[SnapshotAnonymousUserTypeDef]] = None

class GeospatialHeatmapConfigurationOutputTypeDef(BaseValidatorModel):
    HeatmapColor: Optional[GeospatialHeatmapColorScaleOutputTypeDef] = None

class GeospatialHeatmapConfigurationTypeDef(BaseValidatorModel):
    HeatmapColor: Optional[GeospatialHeatmapColorScaleTypeDef] = None

class GlobalTableBorderOptionsTypeDef(BaseValidatorModel):
    UniformBorder: Optional[TableBorderOptionsTypeDef] = None
    SideSpecificBorder: Optional[TableSideBorderOptionsTypeDef] = None

class ConditionalFormattingGradientColorOutputTypeDef(BaseValidatorModel):
    Expression: str
    Color: GradientColorOutputTypeDef

class ConditionalFormattingGradientColorTypeDef(BaseValidatorModel):
    Expression: str
    Color: GradientColorTypeDef

class DefaultGridLayoutConfigurationTypeDef(BaseValidatorModel):
    CanvasSizeOptions: GridLayoutCanvasSizeOptionsTypeDef

class GridLayoutConfigurationOutputTypeDef(BaseValidatorModel):
    Elements: List[GridLayoutElementTypeDef]
    CanvasSizeOptions: Optional[GridLayoutCanvasSizeOptionsTypeDef] = None

class GridLayoutConfigurationTypeDef(BaseValidatorModel):
    Elements: Sequence[GridLayoutElementTypeDef]
    CanvasSizeOptions: Optional[GridLayoutCanvasSizeOptionsTypeDef] = None

class RefreshConfigurationTypeDef(BaseValidatorModel):
    IncrementalRefresh: IncrementalRefreshTypeDef

class DescribeIngestionResponseTypeDef(BaseValidatorModel):
    Ingestion: IngestionTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListIngestionsResponseTypeDef(BaseValidatorModel):
    Ingestions: List[IngestionTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LogicalTableSourceTypeDef(BaseValidatorModel):
    JoinInstruction: Optional[JoinInstructionTypeDef] = None
    PhysicalTableId: Optional[str] = None
    DataSetArn: Optional[str] = None

class DataFieldSeriesItemTypeDef(BaseValidatorModel):
    FieldId: str
    AxisBinding: AxisBindingType
    FieldValue: Optional[str] = None
    Settings: Optional[LineChartSeriesSettingsTypeDef] = None

class FieldSeriesItemTypeDef(BaseValidatorModel):
    FieldId: str
    AxisBinding: AxisBindingType
    Settings: Optional[LineChartSeriesSettingsTypeDef] = None

class CreateFolderRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    Name: Optional[str] = None
    FolderType: Optional[FolderTypeType] = None
    ParentFolderArn: Optional[str] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SharingModel: Optional[SharingModelType] = None

class UpdateAnalysisPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateDashboardPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    GrantLinkPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokeLinkPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateDataSetPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateDataSourcePermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateFolderPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    FolderId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateTemplatePermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateThemePermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class UpdateTopicPermissionsRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    GrantPermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    RevokePermissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None

class SheetStyleTypeDef(BaseValidatorModel):
    Tile: Optional[TileStyleTypeDef] = None
    TileLayout: Optional[TileLayoutStyleTypeDef] = None

class TopicNamedEntityOutputTypeDef(BaseValidatorModel):
    EntityName: str
    EntityDescription: Optional[str] = None
    EntitySynonyms: Optional[List[str]] = None
    SemanticEntityType: Optional[SemanticEntityTypeOutputTypeDef] = None
    Definition: Optional[List[NamedEntityDefinitionOutputTypeDef]] = None

class TopicNamedEntityTypeDef(BaseValidatorModel):
    EntityName: str
    EntityDescription: Optional[str] = None
    EntitySynonyms: Optional[Sequence[str]] = None
    SemanticEntityType: Optional[SemanticEntityTypeTypeDef] = None
    Definition: Optional[Sequence[NamedEntityDefinitionTypeDef]] = None

class DescribeNamespaceResponseTypeDef(BaseValidatorModel):
    Namespace: NamespaceInfoV2TypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListNamespacesResponseTypeDef(BaseValidatorModel):
    Namespaces: List[NamespaceInfoV2TypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVPCConnectionsResponseTypeDef(BaseValidatorModel):
    VPCConnectionSummaries: List[VPCConnectionSummaryTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVPCConnectionResponseTypeDef(BaseValidatorModel):
    VPCConnection: VPCConnectionTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CurrencyDisplayFormatConfigurationTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfigurationTypeDef] = None
    Symbol: Optional[str] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfigurationTypeDef] = None
    NumberScale: Optional[NumberScaleType] = None
    NegativeValueConfiguration: Optional[NegativeValueConfigurationTypeDef] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None

class NumberDisplayFormatConfigurationTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfigurationTypeDef] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfigurationTypeDef] = None
    NumberScale: Optional[NumberScaleType] = None
    NegativeValueConfiguration: Optional[NegativeValueConfigurationTypeDef] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None

class PercentageDisplayFormatConfigurationTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    SeparatorConfiguration: Optional[NumericSeparatorConfigurationTypeDef] = None
    DecimalPlacesConfiguration: Optional[DecimalPlacesConfigurationTypeDef] = None
    NegativeValueConfiguration: Optional[NegativeValueConfigurationTypeDef] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None

class AggregationFunctionTypeDef(BaseValidatorModel):
    NumericalAggregationFunction: Optional[NumericalAggregationFunctionTypeDef] = None
    CategoricalAggregationFunction: Optional[CategoricalAggregationFunctionType] = None
    DateAggregationFunction: Optional[DateAggregationFunctionType] = None
    AttributeAggregationFunction: Optional[AttributeAggregationFunctionTypeDef] = None

class ScrollBarOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    VisibleRange: Optional[VisibleRangeOptionsTypeDef] = None

class TopicDateRangeFilterTypeDef(BaseValidatorModel):
    Inclusive: Optional[bool] = None
    Constant: Optional[TopicRangeFilterConstantTypeDef] = None

class TopicNumericRangeFilterTypeDef(BaseValidatorModel):
    Inclusive: Optional[bool] = None
    Constant: Optional[TopicRangeFilterConstantTypeDef] = None
    Aggregation: Optional[NamedFilterAggTypeType] = None

class DataSourceParametersExtraOutputTypeDef(BaseValidatorModel):
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

class DataSourceParametersOutputTypeDef(BaseValidatorModel):
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

class DataSourceParametersTypeDef(BaseValidatorModel):
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

class RefreshScheduleOutputTypeDef(BaseValidatorModel):
    ScheduleId: str
    ScheduleFrequency: RefreshFrequencyTypeDef
    RefreshType: IngestionTypeType
    StartAfterDateTime: Optional[datetime] = None
    Arn: Optional[str] = None

class RefreshScheduleTypeDef(BaseValidatorModel):
    ScheduleId: str
    ScheduleFrequency: RefreshFrequencyTypeDef
    RefreshType: IngestionTypeType
    StartAfterDateTime: Optional[TimestampTypeDef] = None
    Arn: Optional[str] = None

class RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialPath: Optional[str] = None
    FeatureConfigurations: Optional[RegisteredUserConsoleFeatureConfigurationsTypeDef] = None

class RegisteredUserDashboardEmbeddingConfigurationTypeDef(BaseValidatorModel):
    InitialDashboardId: str
    FeatureConfigurations: Optional[RegisteredUserDashboardFeatureConfigurationsTypeDef] = None

class SnapshotDestinationConfigurationOutputTypeDef(BaseValidatorModel):
    S3Destinations: Optional[List[SnapshotS3DestinationConfigurationTypeDef]] = None

class SnapshotDestinationConfigurationTypeDef(BaseValidatorModel):
    S3Destinations: Optional[Sequence[SnapshotS3DestinationConfigurationTypeDef]] = None

class SnapshotJobS3ResultTypeDef(BaseValidatorModel):
    S3DestinationConfiguration: Optional[SnapshotS3DestinationConfigurationTypeDef] = None
    S3Uri: Optional[str] = None
    ErrorInfo: Optional[List[SnapshotJobResultErrorInfoTypeDef]] = None

class PhysicalTableOutputTypeDef(BaseValidatorModel):
    RelationalTable: Optional[RelationalTableOutputTypeDef] = None
    CustomSql: Optional[CustomSqlOutputTypeDef] = None
    S3Source: Optional[S3SourceOutputTypeDef] = None

class PhysicalTableTypeDef(BaseValidatorModel):
    RelationalTable: Optional[RelationalTableTypeDef] = None
    CustomSql: Optional[CustomSqlTypeDef] = None
    S3Source: Optional[S3SourceTypeDef] = None

class SectionBasedLayoutCanvasSizeOptionsTypeDef(BaseValidatorModel):
    PaperCanvasSizeOptions: Optional[SectionBasedLayoutPaperCanvasSizeOptionsTypeDef] = None

class FilterScopeConfigurationOutputTypeDef(BaseValidatorModel):
    SelectedSheets: Optional[SelectedSheetsFilterScopeConfigurationOutputTypeDef] = None
    AllSheets: Optional[Dict[str, Any]] = None

class FilterScopeConfigurationTypeDef(BaseValidatorModel):
    SelectedSheets: Optional[SelectedSheetsFilterScopeConfigurationTypeDef] = None
    AllSheets: Optional[Mapping[str, Any]] = None

class FreeFormLayoutElementOutputTypeDef(BaseValidatorModel):
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

class FreeFormLayoutElementTypeDef(BaseValidatorModel):
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

class SnapshotFileGroupOutputTypeDef(BaseValidatorModel):
    Files: Optional[List[SnapshotFileOutputTypeDef]] = None

class SnapshotFileGroupTypeDef(BaseValidatorModel):
    Files: Optional[Sequence[SnapshotFileTypeDef]] = None

class DatasetParameterOutputTypeDef(BaseValidatorModel):
    StringDatasetParameter: Optional[StringDatasetParameterOutputTypeDef] = None
    DecimalDatasetParameter: Optional[DecimalDatasetParameterOutputTypeDef] = None
    IntegerDatasetParameter: Optional[IntegerDatasetParameterOutputTypeDef] = None
    DateTimeDatasetParameter: Optional[DateTimeDatasetParameterOutputTypeDef] = None

class FilterCrossSheetControlOutputTypeDef(BaseValidatorModel):
    FilterControlId: str
    SourceFilterId: str
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class FilterCrossSheetControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    SourceFilterId: str
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class DateTimeParameterDeclarationOutputTypeDef(BaseValidatorModel):
    Name: str
    DefaultValues: Optional[DateTimeDefaultValuesOutputTypeDef] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ValueWhenUnset: Optional[DateTimeValueWhenUnsetConfigurationOutputTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class DateTimeParameterDeclarationTypeDef(BaseValidatorModel):
    Name: str
    DefaultValues: Optional[DateTimeDefaultValuesTypeDef] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ValueWhenUnset: Optional[DateTimeValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class DecimalParameterDeclarationOutputTypeDef(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[DecimalDefaultValuesOutputTypeDef] = None
    ValueWhenUnset: Optional[DecimalValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class DecimalParameterDeclarationTypeDef(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[DecimalDefaultValuesTypeDef] = None
    ValueWhenUnset: Optional[DecimalValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class IntegerParameterDeclarationOutputTypeDef(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[IntegerDefaultValuesOutputTypeDef] = None
    ValueWhenUnset: Optional[IntegerValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class IntegerParameterDeclarationTypeDef(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[IntegerDefaultValuesTypeDef] = None
    ValueWhenUnset: Optional[IntegerValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class StringParameterDeclarationOutputTypeDef(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[StringDefaultValuesOutputTypeDef] = None
    ValueWhenUnset: Optional[StringValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[List[MappedDataSetParameterTypeDef]] = None

class StringParameterDeclarationTypeDef(BaseValidatorModel):
    ParameterValueType: ParameterValueTypeType
    Name: str
    DefaultValues: Optional[StringDefaultValuesTypeDef] = None
    ValueWhenUnset: Optional[StringValueWhenUnsetConfigurationTypeDef] = None
    MappedDataSetParameters: Optional[Sequence[MappedDataSetParameterTypeDef]] = None

class DateTimeHierarchyOutputTypeDef(BaseValidatorModel):
    HierarchyId: str
    DrillDownFilters: Optional[List[DrillDownFilterOutputTypeDef]] = None

class ExplicitHierarchyOutputTypeDef(BaseValidatorModel):
    HierarchyId: str
    Columns: List[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[List[DrillDownFilterOutputTypeDef]] = None

class PredefinedHierarchyOutputTypeDef(BaseValidatorModel):
    HierarchyId: str
    Columns: List[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[List[DrillDownFilterOutputTypeDef]] = None

class DescribeAnalysisResponseTypeDef(BaseValidatorModel):
    Analysis: AnalysisTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DashboardTypeDef(BaseValidatorModel):
    DashboardId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[DashboardVersionTypeDef] = None
    CreatedTime: Optional[datetime] = None
    LastPublishedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    LinkEntities: Optional[List[str]] = None

class GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Namespace: str
    AuthorizedResourceArns: Sequence[str]
    ExperienceConfiguration: AnonymousUserEmbeddingExperienceConfigurationTypeDef
    SessionLifetimeInMinutes: Optional[int] = None
    SessionTags: Optional[Sequence[SessionTagTypeDef]] = None
    AllowedDomains: Optional[Sequence[str]] = None

class AssetBundleImportJobOverridePermissionsOutputTypeDef(BaseValidatorModel):
    DataSources: Optional[       List[AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef]     ] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverridePermissionsOutputTypeDef]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef]] = None
    Dashboards: Optional[       List[AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef]     ] = None

class AssetBundleImportJobOverridePermissionsTypeDef(BaseValidatorModel):
    DataSources: Optional[       Sequence[AssetBundleImportJobDataSourceOverridePermissionsTypeDef]     ] = None
    DataSets: Optional[Sequence[AssetBundleImportJobDataSetOverridePermissionsTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleImportJobThemeOverridePermissionsTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleImportJobAnalysisOverridePermissionsTypeDef]] = None
    Dashboards: Optional[       Sequence[AssetBundleImportJobDashboardOverridePermissionsTypeDef]     ] = None

class DestinationParameterValueConfigurationTypeDef(BaseValidatorModel):
    CustomValuesConfiguration: Optional[CustomValuesConfigurationTypeDef] = None
    SelectAllValueOptions: Optional[Literal["ALL_VALUES"]] = None
    SourceParameterName: Optional[str] = None
    SourceField: Optional[str] = None
    SourceColumn: Optional[ColumnIdentifierTypeDef] = None

class DatasetParameterTypeDef(BaseValidatorModel):
    StringDatasetParameter: Optional[StringDatasetParameterTypeDef] = None
    DecimalDatasetParameter: Optional[DecimalDatasetParameterTypeDef] = None
    IntegerDatasetParameter: Optional[IntegerDatasetParameterTypeDef] = None
    DateTimeDatasetParameter: Optional[DateTimeDatasetParameterTypeDef] = None

class DateTimeHierarchyTypeDef(BaseValidatorModel):
    HierarchyId: str
    DrillDownFilters: Optional[Sequence[DrillDownFilterTypeDef]] = None

class ExplicitHierarchyTypeDef(BaseValidatorModel):
    HierarchyId: str
    Columns: Sequence[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[Sequence[DrillDownFilterTypeDef]] = None

class PredefinedHierarchyTypeDef(BaseValidatorModel):
    HierarchyId: str
    Columns: Sequence[ColumnIdentifierTypeDef]
    DrillDownFilters: Optional[Sequence[DrillDownFilterTypeDef]] = None

class ForecastConfigurationTypeDef(BaseValidatorModel):
    ForecastProperties: Optional[TimeBasedForecastPropertiesTypeDef] = None
    Scenario: Optional[ForecastScenarioTypeDef] = None

class AxisDataOptionsOutputTypeDef(BaseValidatorModel):
    NumericAxisOptions: Optional[NumericAxisOptionsOutputTypeDef] = None
    DateAxisOptions: Optional[DateAxisOptionsTypeDef] = None

class AxisDataOptionsTypeDef(BaseValidatorModel):
    NumericAxisOptions: Optional[NumericAxisOptionsTypeDef] = None
    DateAxisOptions: Optional[DateAxisOptionsTypeDef] = None

class TransformOperationOutputTypeDef(BaseValidatorModel):
    ProjectOperation: Optional[ProjectOperationOutputTypeDef] = None
    FilterOperation: Optional[FilterOperationTypeDef] = None
    CreateColumnsOperation: Optional[CreateColumnsOperationOutputTypeDef] = None
    RenameColumnOperation: Optional[RenameColumnOperationTypeDef] = None
    CastColumnTypeOperation: Optional[CastColumnTypeOperationTypeDef] = None
    TagColumnOperation: Optional[TagColumnOperationOutputTypeDef] = None
    UntagColumnOperation: Optional[UntagColumnOperationOutputTypeDef] = None
    OverrideDatasetParameterOperation: Optional[       OverrideDatasetParameterOperationOutputTypeDef     ] = None

class TransformOperationTypeDef(BaseValidatorModel):
    ProjectOperation: Optional[ProjectOperationTypeDef] = None
    FilterOperation: Optional[FilterOperationTypeDef] = None
    CreateColumnsOperation: Optional[CreateColumnsOperationTypeDef] = None
    RenameColumnOperation: Optional[RenameColumnOperationTypeDef] = None
    CastColumnTypeOperation: Optional[CastColumnTypeOperationTypeDef] = None
    TagColumnOperation: Optional[TagColumnOperationTypeDef] = None
    UntagColumnOperation: Optional[UntagColumnOperationTypeDef] = None
    OverrideDatasetParameterOperation: Optional[OverrideDatasetParameterOperationTypeDef] = None

class TemplateVersionTypeDef(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    Errors: Optional[List[TemplateErrorTypeDef]] = None
    VersionNumber: Optional[int] = None
    Status: Optional[ResourceStatusType] = None
    DataSetConfigurations: Optional[List[DataSetConfigurationOutputTypeDef]] = None
    Description: Optional[str] = None
    SourceEntityArn: Optional[str] = None
    ThemeArn: Optional[str] = None
    Sheets: Optional[List[SheetTypeDef]] = None

class SetParameterValueConfigurationOutputTypeDef(BaseValidatorModel):
    DestinationParameterName: str
    Value: DestinationParameterValueConfigurationOutputTypeDef

class VisualPaletteOutputTypeDef(BaseValidatorModel):
    ChartColor: Optional[str] = None
    ColorMap: Optional[List[DataPathColorTypeDef]] = None

class VisualPaletteTypeDef(BaseValidatorModel):
    ChartColor: Optional[str] = None
    ColorMap: Optional[Sequence[DataPathColorTypeDef]] = None

class PivotTableFieldCollapseStateOptionOutputTypeDef(BaseValidatorModel):
    Target: PivotTableFieldCollapseStateTargetOutputTypeDef
    State: Optional[PivotTableFieldCollapseStateType] = None

class PivotTableFieldCollapseStateOptionTypeDef(BaseValidatorModel):
    Target: PivotTableFieldCollapseStateTargetTypeDef
    State: Optional[PivotTableFieldCollapseStateType] = None

class TopicCalculatedFieldOutputTypeDef(BaseValidatorModel):
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

class TopicCalculatedFieldTypeDef(BaseValidatorModel):
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

class TopicColumnOutputTypeDef(BaseValidatorModel):
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

class TopicColumnTypeDef(BaseValidatorModel):
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

class ChartAxisLabelOptionsOutputTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    SortIconVisibility: Optional[VisibilityType] = None
    AxisLabelOptions: Optional[List[AxisLabelOptionsTypeDef]] = None

class ChartAxisLabelOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    SortIconVisibility: Optional[VisibilityType] = None
    AxisLabelOptions: Optional[Sequence[AxisLabelOptionsTypeDef]] = None

class AxisTickLabelOptionsTypeDef(BaseValidatorModel):
    LabelOptions: Optional[LabelOptionsTypeDef] = None
    RotationAngle: Optional[float] = None

class DateTimePickerControlDisplayOptionsTypeDef(BaseValidatorModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    DateTimeFormat: Optional[str] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class DropDownControlDisplayOptionsTypeDef(BaseValidatorModel):
    SelectAllOptions: Optional[ListControlSelectAllOptionsTypeDef] = None
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class LegendOptionsTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    Title: Optional[LabelOptionsTypeDef] = None
    Position: Optional[LegendPositionType] = None
    Width: Optional[str] = None
    Height: Optional[str] = None

class ListControlDisplayOptionsTypeDef(BaseValidatorModel):
    SearchOptions: Optional[ListControlSearchOptionsTypeDef] = None
    SelectAllOptions: Optional[ListControlSelectAllOptionsTypeDef] = None
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class RelativeDateTimeControlDisplayOptionsTypeDef(BaseValidatorModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    DateTimeFormat: Optional[str] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class SliderControlDisplayOptionsTypeDef(BaseValidatorModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class TextAreaControlDisplayOptionsTypeDef(BaseValidatorModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    PlaceholderOptions: Optional[TextControlPlaceholderOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class TextFieldControlDisplayOptionsTypeDef(BaseValidatorModel):
    TitleOptions: Optional[LabelOptionsTypeDef] = None
    PlaceholderOptions: Optional[TextControlPlaceholderOptionsTypeDef] = None
    InfoIconLabelOptions: Optional[SheetControlInfoIconLabelOptionsTypeDef] = None

class PanelConfigurationTypeDef(BaseValidatorModel):
    Title: Optional[PanelTitleOptionsTypeDef] = None
    BorderVisibility: Optional[VisibilityType] = None
    BorderThickness: Optional[str] = None
    BorderStyle: Optional[PanelBorderStyleType] = None
    BorderColor: Optional[str] = None
    GutterVisibility: Optional[VisibilityType] = None
    GutterSpacing: Optional[str] = None
    BackgroundVisibility: Optional[VisibilityType] = None
    BackgroundColor: Optional[str] = None

class TableFieldLinkContentConfigurationTypeDef(BaseValidatorModel):
    CustomTextContent: Optional[TableFieldCustomTextContentTypeDef] = None
    CustomIconContent: Optional[TableFieldCustomIconContentTypeDef] = None

class GeospatialPointStyleOptionsOutputTypeDef(BaseValidatorModel):
    SelectedPointStyle: Optional[GeospatialSelectedPointStyleType] = None
    ClusterMarkerConfiguration: Optional[ClusterMarkerConfigurationTypeDef] = None
    HeatmapConfiguration: Optional[GeospatialHeatmapConfigurationOutputTypeDef] = None

class GeospatialPointStyleOptionsTypeDef(BaseValidatorModel):
    SelectedPointStyle: Optional[GeospatialSelectedPointStyleType] = None
    ClusterMarkerConfiguration: Optional[ClusterMarkerConfigurationTypeDef] = None
    HeatmapConfiguration: Optional[GeospatialHeatmapConfigurationTypeDef] = None

class TableCellStyleTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    TextWrap: Optional[TextWrapType] = None
    HorizontalTextAlignment: Optional[HorizontalTextAlignmentType] = None
    VerticalTextAlignment: Optional[VerticalTextAlignmentType] = None
    BackgroundColor: Optional[str] = None
    Height: Optional[int] = None
    Border: Optional[GlobalTableBorderOptionsTypeDef] = None

class ConditionalFormattingColorOutputTypeDef(BaseValidatorModel):
    Solid: Optional[ConditionalFormattingSolidColorTypeDef] = None
    Gradient: Optional[ConditionalFormattingGradientColorOutputTypeDef] = None

class ConditionalFormattingColorTypeDef(BaseValidatorModel):
    Solid: Optional[ConditionalFormattingSolidColorTypeDef] = None
    Gradient: Optional[ConditionalFormattingGradientColorTypeDef] = None

class DefaultInteractiveLayoutConfigurationTypeDef(BaseValidatorModel):
    Grid: Optional[DefaultGridLayoutConfigurationTypeDef] = None
    FreeForm: Optional[DefaultFreeFormLayoutConfigurationTypeDef] = None

class SheetControlLayoutConfigurationOutputTypeDef(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfigurationOutputTypeDef] = None

class SheetControlLayoutConfigurationTypeDef(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfigurationTypeDef] = None

class DataSetRefreshPropertiesTypeDef(BaseValidatorModel):
    RefreshConfiguration: RefreshConfigurationTypeDef

class SeriesItemTypeDef(BaseValidatorModel):
    FieldSeriesItem: Optional[FieldSeriesItemTypeDef] = None
    DataFieldSeriesItem: Optional[DataFieldSeriesItemTypeDef] = None

class ThemeConfigurationOutputTypeDef(BaseValidatorModel):
    DataColorPalette: Optional[DataColorPaletteOutputTypeDef] = None
    UIColorPalette: Optional[UIColorPaletteTypeDef] = None
    Sheet: Optional[SheetStyleTypeDef] = None
    Typography: Optional[TypographyOutputTypeDef] = None

class ThemeConfigurationTypeDef(BaseValidatorModel):
    DataColorPalette: Optional[DataColorPaletteTypeDef] = None
    UIColorPalette: Optional[UIColorPaletteTypeDef] = None
    Sheet: Optional[SheetStyleTypeDef] = None
    Typography: Optional[TypographyTypeDef] = None

class ComparisonFormatConfigurationTypeDef(BaseValidatorModel):
    NumberDisplayFormatConfiguration: Optional[NumberDisplayFormatConfigurationTypeDef] = None
    PercentageDisplayFormatConfiguration: Optional[       PercentageDisplayFormatConfigurationTypeDef     ] = None

class NumericFormatConfigurationTypeDef(BaseValidatorModel):
    NumberDisplayFormatConfiguration: Optional[NumberDisplayFormatConfigurationTypeDef] = None
    CurrencyDisplayFormatConfiguration: Optional[       CurrencyDisplayFormatConfigurationTypeDef     ] = None
    PercentageDisplayFormatConfiguration: Optional[       PercentageDisplayFormatConfigurationTypeDef     ] = None

class AggregationSortConfigurationTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    SortDirection: SortDirectionType
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None

class ColumnSortTypeDef(BaseValidatorModel):
    SortBy: ColumnIdentifierTypeDef
    Direction: SortDirectionType
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None

class ColumnTooltipItemTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Label: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    Aggregation: Optional[AggregationFunctionTypeDef] = None
    TooltipTarget: Optional[TooltipTargetType] = None

class ReferenceLineDynamicDataConfigurationTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Calculation: NumericalAggregationFunctionTypeDef
    MeasureAggregationFunction: Optional[AggregationFunctionTypeDef] = None

class TopicFilterOutputTypeDef(BaseValidatorModel):
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

class TopicFilterTypeDef(BaseValidatorModel):
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

class AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef(BaseValidatorModel):
    DataSourceId: str
    Name: Optional[str] = None
    DataSourceParameters: Optional[DataSourceParametersOutputTypeDef] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None
    Credentials: Optional[AssetBundleImportJobDataSourceCredentialsTypeDef] = None

class DataSourceTypeDef(BaseValidatorModel):
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

class AssetBundleImportJobDataSourceOverrideParametersTypeDef(BaseValidatorModel):
    DataSourceId: str
    Name: Optional[str] = None
    DataSourceParameters: Optional[DataSourceParametersTypeDef] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None
    Credentials: Optional[AssetBundleImportJobDataSourceCredentialsTypeDef] = None

class CredentialPairTypeDef(BaseValidatorModel):
    Username: str
    Password: str
    AlternateDataSourceParameters: Optional[Sequence[DataSourceParametersTypeDef]] = None

class DescribeRefreshScheduleResponseTypeDef(BaseValidatorModel):
    RefreshSchedule: RefreshScheduleOutputTypeDef
    Status: int
    RequestId: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRefreshSchedulesResponseTypeDef(BaseValidatorModel):
    RefreshSchedules: List[RefreshScheduleOutputTypeDef]
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    Schedule: RefreshScheduleTypeDef

class UpdateRefreshScheduleRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    AwsAccountId: str
    Schedule: RefreshScheduleTypeDef

class RegisteredUserEmbeddingExperienceConfigurationTypeDef(BaseValidatorModel):
    Dashboard: Optional[RegisteredUserDashboardEmbeddingConfigurationTypeDef] = None
    QuickSightConsole: Optional[       RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef     ] = None
    QSearchBar: Optional[RegisteredUserQSearchBarEmbeddingConfigurationTypeDef] = None
    DashboardVisual: Optional[RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef] = None
    GenerativeQnA: Optional[RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef] = None

class SnapshotJobResultFileGroupTypeDef(BaseValidatorModel):
    Files: Optional[List[SnapshotFileOutputTypeDef]] = None
    S3Results: Optional[List[SnapshotJobS3ResultTypeDef]] = None

class DefaultSectionBasedLayoutConfigurationTypeDef(BaseValidatorModel):
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptionsTypeDef

class FreeFormLayoutConfigurationOutputTypeDef(BaseValidatorModel):
    Elements: List[FreeFormLayoutElementOutputTypeDef]
    CanvasSizeOptions: Optional[FreeFormLayoutCanvasSizeOptionsTypeDef] = None

class FreeFormSectionLayoutConfigurationOutputTypeDef(BaseValidatorModel):
    Elements: List[FreeFormLayoutElementOutputTypeDef]

class FreeFormLayoutConfigurationTypeDef(BaseValidatorModel):
    Elements: Sequence[FreeFormLayoutElementTypeDef]
    CanvasSizeOptions: Optional[FreeFormLayoutCanvasSizeOptionsTypeDef] = None

class FreeFormSectionLayoutConfigurationTypeDef(BaseValidatorModel):
    Elements: Sequence[FreeFormLayoutElementTypeDef]

class SnapshotConfigurationOutputTypeDef(BaseValidatorModel):
    FileGroups: List[SnapshotFileGroupOutputTypeDef]
    DestinationConfiguration: Optional[SnapshotDestinationConfigurationOutputTypeDef] = None
    Parameters: Optional[ParametersOutputTypeDef] = None

class SnapshotConfigurationTypeDef(BaseValidatorModel):
    FileGroups: Sequence[SnapshotFileGroupTypeDef]
    DestinationConfiguration: Optional[SnapshotDestinationConfigurationTypeDef] = None
    Parameters: Optional[ParametersTypeDef] = None

class ParameterDeclarationOutputTypeDef(BaseValidatorModel):
    StringParameterDeclaration: Optional[StringParameterDeclarationOutputTypeDef] = None
    DecimalParameterDeclaration: Optional[DecimalParameterDeclarationOutputTypeDef] = None
    IntegerParameterDeclaration: Optional[IntegerParameterDeclarationOutputTypeDef] = None
    DateTimeParameterDeclaration: Optional[DateTimeParameterDeclarationOutputTypeDef] = None

class ParameterDeclarationTypeDef(BaseValidatorModel):
    StringParameterDeclaration: Optional[StringParameterDeclarationTypeDef] = None
    DecimalParameterDeclaration: Optional[DecimalParameterDeclarationTypeDef] = None
    IntegerParameterDeclaration: Optional[IntegerParameterDeclarationTypeDef] = None
    DateTimeParameterDeclaration: Optional[DateTimeParameterDeclarationTypeDef] = None

class ColumnHierarchyOutputTypeDef(BaseValidatorModel):
    ExplicitHierarchy: Optional[ExplicitHierarchyOutputTypeDef] = None
    DateTimeHierarchy: Optional[DateTimeHierarchyOutputTypeDef] = None
    PredefinedHierarchy: Optional[PredefinedHierarchyOutputTypeDef] = None

class DescribeDashboardResponseTypeDef(BaseValidatorModel):
    Dashboard: DashboardTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetParameterValueConfigurationTypeDef(BaseValidatorModel):
    DestinationParameterName: str
    Value: DestinationParameterValueConfigurationTypeDef

class ColumnHierarchyTypeDef(BaseValidatorModel):
    ExplicitHierarchy: Optional[ExplicitHierarchyTypeDef] = None
    DateTimeHierarchy: Optional[DateTimeHierarchyTypeDef] = None
    PredefinedHierarchy: Optional[PredefinedHierarchyTypeDef] = None

class LogicalTableOutputTypeDef(BaseValidatorModel):
    Alias: str
    Source: LogicalTableSourceTypeDef
    DataTransforms: Optional[List[TransformOperationOutputTypeDef]] = None

class LogicalTableTypeDef(BaseValidatorModel):
    Alias: str
    Source: LogicalTableSourceTypeDef
    DataTransforms: Optional[Sequence[TransformOperationTypeDef]] = None

class TemplateTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[TemplateVersionTypeDef] = None
    TemplateId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None

class CustomActionSetParametersOperationOutputTypeDef(BaseValidatorModel):
    ParameterValueConfigurations: List[SetParameterValueConfigurationOutputTypeDef]

class PivotTableFieldOptionsOutputTypeDef(BaseValidatorModel):
    SelectedFieldOptions: Optional[List[PivotTableFieldOptionTypeDef]] = None
    DataPathOptions: Optional[List[PivotTableDataPathOptionOutputTypeDef]] = None
    CollapseStateOptions: Optional[List[PivotTableFieldCollapseStateOptionOutputTypeDef]] = None

class PivotTableFieldOptionsTypeDef(BaseValidatorModel):
    SelectedFieldOptions: Optional[Sequence[PivotTableFieldOptionTypeDef]] = None
    DataPathOptions: Optional[Sequence[PivotTableDataPathOptionTypeDef]] = None
    CollapseStateOptions: Optional[Sequence[PivotTableFieldCollapseStateOptionTypeDef]] = None

class AxisDisplayOptionsOutputTypeDef(BaseValidatorModel):
    TickLabelOptions: Optional[AxisTickLabelOptionsTypeDef] = None
    AxisLineVisibility: Optional[VisibilityType] = None
    GridLineVisibility: Optional[VisibilityType] = None
    DataOptions: Optional[AxisDataOptionsOutputTypeDef] = None
    ScrollbarOptions: Optional[ScrollBarOptionsTypeDef] = None
    AxisOffset: Optional[str] = None

class AxisDisplayOptionsTypeDef(BaseValidatorModel):
    TickLabelOptions: Optional[AxisTickLabelOptionsTypeDef] = None
    AxisLineVisibility: Optional[VisibilityType] = None
    GridLineVisibility: Optional[VisibilityType] = None
    DataOptions: Optional[AxisDataOptionsTypeDef] = None
    ScrollbarOptions: Optional[ScrollBarOptionsTypeDef] = None
    AxisOffset: Optional[str] = None

class DefaultDateTimePickerControlOptionsTypeDef(BaseValidatorModel):
    Type: Optional[SheetControlDateTimePickerTypeType] = None
    DisplayOptions: Optional[DateTimePickerControlDisplayOptionsTypeDef] = None

class FilterDateTimePickerControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DateTimePickerControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlDateTimePickerTypeType] = None

class ParameterDateTimePickerControlTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DateTimePickerControlDisplayOptionsTypeDef] = None

class DefaultFilterDropDownControlOptionsOutputTypeDef(BaseValidatorModel):
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None

class DefaultFilterDropDownControlOptionsTypeDef(BaseValidatorModel):
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None

class FilterDropDownControlOutputTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class FilterDropDownControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class ParameterDropDownControlOutputTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class ParameterDropDownControlTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[DropDownControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class DefaultFilterListControlOptionsOutputTypeDef(BaseValidatorModel):
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None

class DefaultFilterListControlOptionsTypeDef(BaseValidatorModel):
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None

class FilterListControlOutputTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class FilterListControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[FilterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class ParameterListControlOutputTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesOutputTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationOutputTypeDef] = None

class ParameterListControlTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[ListControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlListTypeType] = None
    SelectableValues: Optional[ParameterSelectableValuesTypeDef] = None
    CascadingControlConfiguration: Optional[CascadingControlConfigurationTypeDef] = None

class DefaultRelativeDateTimeControlOptionsTypeDef(BaseValidatorModel):
    DisplayOptions: Optional[RelativeDateTimeControlDisplayOptionsTypeDef] = None

class FilterRelativeDateTimeControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[RelativeDateTimeControlDisplayOptionsTypeDef] = None

class DefaultSliderControlOptionsTypeDef(BaseValidatorModel):
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlSliderTypeType] = None

class FilterSliderControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptionsTypeDef] = None
    Type: Optional[SheetControlSliderTypeType] = None

class ParameterSliderControlTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    MaximumValue: float
    MinimumValue: float
    StepSize: float
    DisplayOptions: Optional[SliderControlDisplayOptionsTypeDef] = None

class DefaultTextAreaControlOptionsTypeDef(BaseValidatorModel):
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptionsTypeDef] = None

class FilterTextAreaControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptionsTypeDef] = None

class ParameterTextAreaControlTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    Delimiter: Optional[str] = None
    DisplayOptions: Optional[TextAreaControlDisplayOptionsTypeDef] = None

class DefaultTextFieldControlOptionsTypeDef(BaseValidatorModel):
    DisplayOptions: Optional[TextFieldControlDisplayOptionsTypeDef] = None

class FilterTextFieldControlTypeDef(BaseValidatorModel):
    FilterControlId: str
    Title: str
    SourceFilterId: str
    DisplayOptions: Optional[TextFieldControlDisplayOptionsTypeDef] = None

class ParameterTextFieldControlTypeDef(BaseValidatorModel):
    ParameterControlId: str
    Title: str
    SourceParameterName: str
    DisplayOptions: Optional[TextFieldControlDisplayOptionsTypeDef] = None

class SmallMultiplesOptionsTypeDef(BaseValidatorModel):
    MaxVisibleRows: Optional[int] = None
    MaxVisibleColumns: Optional[int] = None
    PanelConfiguration: Optional[PanelConfigurationTypeDef] = None
    XAxis: Optional[SmallMultiplesAxisPropertiesTypeDef] = None
    YAxis: Optional[SmallMultiplesAxisPropertiesTypeDef] = None

class TableFieldLinkConfigurationTypeDef(BaseValidatorModel):
    Target: URLTargetConfigurationType
    Content: TableFieldLinkContentConfigurationTypeDef

class PivotTableOptionsOutputTypeDef(BaseValidatorModel):
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

class PivotTableOptionsTypeDef(BaseValidatorModel):
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

class PivotTotalOptionsOutputTypeDef(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOptionTypeDef]] = None

class PivotTotalOptionsTypeDef(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[Sequence[TotalAggregationOptionTypeDef]] = None

class SubtotalOptionsOutputTypeDef(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None
    FieldLevel: Optional[PivotTableSubtotalLevelType] = None
    FieldLevelOptions: Optional[List[PivotTableFieldSubtotalOptionsTypeDef]] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    StyleTargets: Optional[List[TableStyleTargetTypeDef]] = None

class SubtotalOptionsTypeDef(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    CustomLabel: Optional[str] = None
    FieldLevel: Optional[PivotTableSubtotalLevelType] = None
    FieldLevelOptions: Optional[Sequence[PivotTableFieldSubtotalOptionsTypeDef]] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    ValueCellStyle: Optional[TableCellStyleTypeDef] = None
    MetricHeaderCellStyle: Optional[TableCellStyleTypeDef] = None
    StyleTargets: Optional[Sequence[TableStyleTargetTypeDef]] = None

class TableOptionsOutputTypeDef(BaseValidatorModel):
    Orientation: Optional[TableOrientationType] = None
    HeaderStyle: Optional[TableCellStyleTypeDef] = None
    CellStyle: Optional[TableCellStyleTypeDef] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsOutputTypeDef] = None

class TableOptionsTypeDef(BaseValidatorModel):
    Orientation: Optional[TableOrientationType] = None
    HeaderStyle: Optional[TableCellStyleTypeDef] = None
    CellStyle: Optional[TableCellStyleTypeDef] = None
    RowAlternateColorOptions: Optional[RowAlternateColorOptionsTypeDef] = None

class TotalOptionsOutputTypeDef(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[List[TotalAggregationOptionTypeDef]] = None

class TotalOptionsTypeDef(BaseValidatorModel):
    TotalsVisibility: Optional[VisibilityType] = None
    Placement: Optional[TableTotalsPlacementType] = None
    ScrollStatus: Optional[TableTotalsScrollStatusType] = None
    CustomLabel: Optional[str] = None
    TotalCellStyle: Optional[TableCellStyleTypeDef] = None
    TotalAggregationOptions: Optional[Sequence[TotalAggregationOptionTypeDef]] = None

class GaugeChartArcConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None

class GaugeChartPrimaryValueConditionalFormattingOutputTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIActualValueConditionalFormattingOutputTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIComparisonValueConditionalFormattingOutputTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIPrimaryValueConditionalFormattingOutputTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIProgressBarConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None

class ShapeConditionalFormatOutputTypeDef(BaseValidatorModel):
    BackgroundColor: ConditionalFormattingColorOutputTypeDef

class TableRowConditionalFormattingOutputTypeDef(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None

class TextConditionalFormatOutputTypeDef(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorOutputTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class GaugeChartArcConditionalFormattingTypeDef(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColorTypeDef] = None

class GaugeChartPrimaryValueConditionalFormattingTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIActualValueConditionalFormattingTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIComparisonValueConditionalFormattingTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIPrimaryValueConditionalFormattingTypeDef(BaseValidatorModel):
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class KPIProgressBarConditionalFormattingTypeDef(BaseValidatorModel):
    ForegroundColor: Optional[ConditionalFormattingColorTypeDef] = None

class ShapeConditionalFormatTypeDef(BaseValidatorModel):
    BackgroundColor: ConditionalFormattingColorTypeDef

class TableRowConditionalFormattingTypeDef(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColorTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None

class TextConditionalFormatTypeDef(BaseValidatorModel):
    BackgroundColor: Optional[ConditionalFormattingColorTypeDef] = None
    TextColor: Optional[ConditionalFormattingColorTypeDef] = None
    Icon: Optional[ConditionalFormattingIconTypeDef] = None

class SheetControlLayoutOutputTypeDef(BaseValidatorModel):
    Configuration: SheetControlLayoutConfigurationOutputTypeDef

class SheetControlLayoutTypeDef(BaseValidatorModel):
    Configuration: SheetControlLayoutConfigurationTypeDef

class DescribeDataSetRefreshPropertiesResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Status: int
    DataSetRefreshProperties: DataSetRefreshPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataSetRefreshPropertiesRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSetId: str
    DataSetRefreshProperties: DataSetRefreshPropertiesTypeDef

class ThemeVersionTypeDef(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    BaseThemeId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Configuration: Optional[ThemeConfigurationOutputTypeDef] = None
    Errors: Optional[List[ThemeErrorTypeDef]] = None
    Status: Optional[ResourceStatusType] = None

class CreateThemeRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    Name: str
    BaseThemeId: str
    Configuration: ThemeConfigurationTypeDef
    VersionDescription: Optional[str] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateThemeRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    ThemeId: str
    BaseThemeId: str
    Name: Optional[str] = None
    VersionDescription: Optional[str] = None
    Configuration: Optional[ThemeConfigurationTypeDef] = None

class ComparisonConfigurationTypeDef(BaseValidatorModel):
    ComparisonMethod: Optional[ComparisonMethodType] = None
    ComparisonFormat: Optional[ComparisonFormatConfigurationTypeDef] = None

class DateTimeFormatConfigurationTypeDef(BaseValidatorModel):
    DateTimeFormat: Optional[str] = None
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None
    NumericFormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class NumberFormatConfigurationTypeDef(BaseValidatorModel):
    FormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class ReferenceLineValueLabelConfigurationTypeDef(BaseValidatorModel):
    RelativePosition: Optional[ReferenceLineValueLabelRelativePositionType] = None
    FormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class StringFormatConfigurationTypeDef(BaseValidatorModel):
    NullValueFormatConfiguration: Optional[NullValueFormatConfigurationTypeDef] = None
    NumericFormatConfiguration: Optional[NumericFormatConfigurationTypeDef] = None

class BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSortTypeDef]] = None

class BodySectionDynamicCategoryDimensionConfigurationTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[Sequence[ColumnSortTypeDef]] = None

class BodySectionDynamicNumericDimensionConfigurationOutputTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[List[ColumnSortTypeDef]] = None

class BodySectionDynamicNumericDimensionConfigurationTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Limit: Optional[int] = None
    SortByMetrics: Optional[Sequence[ColumnSortTypeDef]] = None

class FieldSortOptionsTypeDef(BaseValidatorModel):
    FieldSort: Optional[FieldSortTypeDef] = None
    ColumnSort: Optional[ColumnSortTypeDef] = None

class PivotTableSortByOutputTypeDef(BaseValidatorModel):
    Field: Optional[FieldSortTypeDef] = None
    Column: Optional[ColumnSortTypeDef] = None
    DataPath: Optional[DataPathSortOutputTypeDef] = None

class PivotTableSortByTypeDef(BaseValidatorModel):
    Field: Optional[FieldSortTypeDef] = None
    Column: Optional[ColumnSortTypeDef] = None
    DataPath: Optional[DataPathSortTypeDef] = None

class TooltipItemTypeDef(BaseValidatorModel):
    FieldTooltipItem: Optional[FieldTooltipItemTypeDef] = None
    ColumnTooltipItem: Optional[ColumnTooltipItemTypeDef] = None

class ReferenceLineDataConfigurationTypeDef(BaseValidatorModel):
    StaticConfiguration: Optional[ReferenceLineStaticDataConfigurationTypeDef] = None
    DynamicConfiguration: Optional[ReferenceLineDynamicDataConfigurationTypeDef] = None
    AxisBinding: Optional[AxisBindingType] = None
    SeriesType: Optional[ReferenceLineSeriesTypeType] = None

class DatasetMetadataOutputTypeDef(BaseValidatorModel):
    DatasetArn: str
    DatasetName: Optional[str] = None
    DatasetDescription: Optional[str] = None
    DataAggregation: Optional[DataAggregationTypeDef] = None
    Filters: Optional[List[TopicFilterOutputTypeDef]] = None
    Columns: Optional[List[TopicColumnOutputTypeDef]] = None
    CalculatedFields: Optional[List[TopicCalculatedFieldOutputTypeDef]] = None
    NamedEntities: Optional[List[TopicNamedEntityOutputTypeDef]] = None

class DatasetMetadataTypeDef(BaseValidatorModel):
    DatasetArn: str
    DatasetName: Optional[str] = None
    DatasetDescription: Optional[str] = None
    DataAggregation: Optional[DataAggregationTypeDef] = None
    Filters: Optional[Sequence[TopicFilterTypeDef]] = None
    Columns: Optional[Sequence[TopicColumnTypeDef]] = None
    CalculatedFields: Optional[Sequence[TopicCalculatedFieldTypeDef]] = None
    NamedEntities: Optional[Sequence[TopicNamedEntityTypeDef]] = None

class AssetBundleImportJobOverrideParametersOutputTypeDef(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleImportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       List[AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef]     ] = None
    RefreshSchedules: Optional[       List[AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef]     ] = None
    DataSources: Optional[       List[AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef]     ] = None
    DataSets: Optional[List[AssetBundleImportJobDataSetOverrideParametersTypeDef]] = None
    Themes: Optional[List[AssetBundleImportJobThemeOverrideParametersTypeDef]] = None
    Analyses: Optional[List[AssetBundleImportJobAnalysisOverrideParametersTypeDef]] = None
    Dashboards: Optional[List[AssetBundleImportJobDashboardOverrideParametersTypeDef]] = None

class DescribeDataSourceResponseTypeDef(BaseValidatorModel):
    DataSource: DataSourceTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    DataSources: List[DataSourceTypeDef]
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssetBundleImportJobOverrideParametersTypeDef(BaseValidatorModel):
    ResourceIdOverrideConfiguration: Optional[       AssetBundleImportJobResourceIdOverrideConfigurationTypeDef     ] = None
    VPCConnections: Optional[       Sequence[AssetBundleImportJobVPCConnectionOverrideParametersTypeDef]     ] = None
    RefreshSchedules: Optional[       Sequence[AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef]     ] = None
    DataSources: Optional[       Sequence[AssetBundleImportJobDataSourceOverrideParametersTypeDef]     ] = None
    DataSets: Optional[Sequence[AssetBundleImportJobDataSetOverrideParametersTypeDef]] = None
    Themes: Optional[Sequence[AssetBundleImportJobThemeOverrideParametersTypeDef]] = None
    Analyses: Optional[Sequence[AssetBundleImportJobAnalysisOverrideParametersTypeDef]] = None
    Dashboards: Optional[Sequence[AssetBundleImportJobDashboardOverrideParametersTypeDef]] = None

class DataSourceCredentialsTypeDef(BaseValidatorModel):
    CredentialPair: Optional[CredentialPairTypeDef] = None
    CopySourceArn: Optional[str] = None
    SecretArn: Optional[str] = None

class GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    UserArn: str
    ExperienceConfiguration: RegisteredUserEmbeddingExperienceConfigurationTypeDef
    SessionLifetimeInMinutes: Optional[int] = None
    AllowedDomains: Optional[Sequence[str]] = None

class AnonymousUserSnapshotJobResultTypeDef(BaseValidatorModel):
    FileGroups: Optional[List[SnapshotJobResultFileGroupTypeDef]] = None

class DefaultPaginatedLayoutConfigurationTypeDef(BaseValidatorModel):
    SectionBased: Optional[DefaultSectionBasedLayoutConfigurationTypeDef] = None

class SectionLayoutConfigurationOutputTypeDef(BaseValidatorModel):
    FreeFormLayout: FreeFormSectionLayoutConfigurationOutputTypeDef

class SectionLayoutConfigurationTypeDef(BaseValidatorModel):
    FreeFormLayout: FreeFormSectionLayoutConfigurationTypeDef

class DescribeDashboardSnapshotJobResponseTypeDef(BaseValidatorModel):
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

class StartDashboardSnapshotJobRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DashboardId: str
    SnapshotJobId: str
    UserConfiguration: SnapshotUserConfigurationTypeDef
    SnapshotConfiguration: SnapshotConfigurationTypeDef

class CustomActionSetParametersOperationTypeDef(BaseValidatorModel):
    ParameterValueConfigurations: Sequence[SetParameterValueConfigurationTypeDef]

class DataSetTypeDef(BaseValidatorModel):
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

class DescribeTemplateResponseTypeDef(BaseValidatorModel):
    Template: TemplateTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VisualCustomActionOperationOutputTypeDef(BaseValidatorModel):
    FilterOperation: Optional[CustomActionFilterOperationOutputTypeDef] = None
    NavigationOperation: Optional[CustomActionNavigationOperationTypeDef] = None
    URLOperation: Optional[CustomActionURLOperationTypeDef] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationOutputTypeDef] = None

class LineSeriesAxisDisplayOptionsOutputTypeDef(BaseValidatorModel):
    AxisOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    MissingDataConfigurations: Optional[List[MissingDataConfigurationTypeDef]] = None

class LineSeriesAxisDisplayOptionsTypeDef(BaseValidatorModel):
    AxisOptions: Optional[AxisDisplayOptionsTypeDef] = None
    MissingDataConfigurations: Optional[Sequence[MissingDataConfigurationTypeDef]] = None

class DefaultFilterControlOptionsOutputTypeDef(BaseValidatorModel):
    DefaultDateTimePickerOptions: Optional[DefaultDateTimePickerControlOptionsTypeDef] = None
    DefaultListOptions: Optional[DefaultFilterListControlOptionsOutputTypeDef] = None
    DefaultDropdownOptions: Optional[DefaultFilterDropDownControlOptionsOutputTypeDef] = None
    DefaultTextFieldOptions: Optional[DefaultTextFieldControlOptionsTypeDef] = None
    DefaultTextAreaOptions: Optional[DefaultTextAreaControlOptionsTypeDef] = None
    DefaultSliderOptions: Optional[DefaultSliderControlOptionsTypeDef] = None
    DefaultRelativeDateTimeOptions: Optional[DefaultRelativeDateTimeControlOptionsTypeDef] = None

class DefaultFilterControlOptionsTypeDef(BaseValidatorModel):
    DefaultDateTimePickerOptions: Optional[DefaultDateTimePickerControlOptionsTypeDef] = None
    DefaultListOptions: Optional[DefaultFilterListControlOptionsTypeDef] = None
    DefaultDropdownOptions: Optional[DefaultFilterDropDownControlOptionsTypeDef] = None
    DefaultTextFieldOptions: Optional[DefaultTextFieldControlOptionsTypeDef] = None
    DefaultTextAreaOptions: Optional[DefaultTextAreaControlOptionsTypeDef] = None
    DefaultSliderOptions: Optional[DefaultSliderControlOptionsTypeDef] = None
    DefaultRelativeDateTimeOptions: Optional[DefaultRelativeDateTimeControlOptionsTypeDef] = None

class FilterControlOutputTypeDef(BaseValidatorModel):
    DateTimePicker: Optional[FilterDateTimePickerControlTypeDef] = None
    List: Optional[FilterListControlOutputTypeDef] = None
    Dropdown: Optional[FilterDropDownControlOutputTypeDef] = None
    TextField: Optional[FilterTextFieldControlTypeDef] = None
    TextArea: Optional[FilterTextAreaControlTypeDef] = None
    Slider: Optional[FilterSliderControlTypeDef] = None
    RelativeDateTime: Optional[FilterRelativeDateTimeControlTypeDef] = None
    CrossSheet: Optional[FilterCrossSheetControlOutputTypeDef] = None

class FilterControlTypeDef(BaseValidatorModel):
    DateTimePicker: Optional[FilterDateTimePickerControlTypeDef] = None
    List: Optional[FilterListControlTypeDef] = None
    Dropdown: Optional[FilterDropDownControlTypeDef] = None
    TextField: Optional[FilterTextFieldControlTypeDef] = None
    TextArea: Optional[FilterTextAreaControlTypeDef] = None
    Slider: Optional[FilterSliderControlTypeDef] = None
    RelativeDateTime: Optional[FilterRelativeDateTimeControlTypeDef] = None
    CrossSheet: Optional[FilterCrossSheetControlTypeDef] = None

class ParameterControlOutputTypeDef(BaseValidatorModel):
    DateTimePicker: Optional[ParameterDateTimePickerControlTypeDef] = None
    List: Optional[ParameterListControlOutputTypeDef] = None
    Dropdown: Optional[ParameterDropDownControlOutputTypeDef] = None
    TextField: Optional[ParameterTextFieldControlTypeDef] = None
    TextArea: Optional[ParameterTextAreaControlTypeDef] = None
    Slider: Optional[ParameterSliderControlTypeDef] = None

class ParameterControlTypeDef(BaseValidatorModel):
    DateTimePicker: Optional[ParameterDateTimePickerControlTypeDef] = None
    List: Optional[ParameterListControlTypeDef] = None
    Dropdown: Optional[ParameterDropDownControlTypeDef] = None
    TextField: Optional[ParameterTextFieldControlTypeDef] = None
    TextArea: Optional[ParameterTextAreaControlTypeDef] = None
    Slider: Optional[ParameterSliderControlTypeDef] = None

class TableFieldURLConfigurationTypeDef(BaseValidatorModel):
    LinkConfiguration: Optional[TableFieldLinkConfigurationTypeDef] = None
    ImageConfiguration: Optional[TableFieldImageConfigurationTypeDef] = None

class PivotTableTotalOptionsOutputTypeDef(BaseValidatorModel):
    RowSubtotalOptions: Optional[SubtotalOptionsOutputTypeDef] = None
    ColumnSubtotalOptions: Optional[SubtotalOptionsOutputTypeDef] = None
    RowTotalOptions: Optional[PivotTotalOptionsOutputTypeDef] = None
    ColumnTotalOptions: Optional[PivotTotalOptionsOutputTypeDef] = None

class PivotTableTotalOptionsTypeDef(BaseValidatorModel):
    RowSubtotalOptions: Optional[SubtotalOptionsTypeDef] = None
    ColumnSubtotalOptions: Optional[SubtotalOptionsTypeDef] = None
    RowTotalOptions: Optional[PivotTotalOptionsTypeDef] = None
    ColumnTotalOptions: Optional[PivotTotalOptionsTypeDef] = None

class GaugeChartConditionalFormattingOptionOutputTypeDef(BaseValidatorModel):
    PrimaryValue: Optional[GaugeChartPrimaryValueConditionalFormattingOutputTypeDef] = None
    Arc: Optional[GaugeChartArcConditionalFormattingOutputTypeDef] = None

class KPIConditionalFormattingOptionOutputTypeDef(BaseValidatorModel):
    PrimaryValue: Optional[KPIPrimaryValueConditionalFormattingOutputTypeDef] = None
    ProgressBar: Optional[KPIProgressBarConditionalFormattingOutputTypeDef] = None
    ActualValue: Optional[KPIActualValueConditionalFormattingOutputTypeDef] = None
    ComparisonValue: Optional[KPIComparisonValueConditionalFormattingOutputTypeDef] = None

class FilledMapShapeConditionalFormattingOutputTypeDef(BaseValidatorModel):
    FieldId: str
    Format: Optional[ShapeConditionalFormatOutputTypeDef] = None

class PivotTableCellConditionalFormattingOutputTypeDef(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatOutputTypeDef] = None
    Scope: Optional[PivotTableConditionalFormattingScopeTypeDef] = None
    Scopes: Optional[List[PivotTableConditionalFormattingScopeTypeDef]] = None

class TableCellConditionalFormattingOutputTypeDef(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatOutputTypeDef] = None

class GaugeChartConditionalFormattingOptionTypeDef(BaseValidatorModel):
    PrimaryValue: Optional[GaugeChartPrimaryValueConditionalFormattingTypeDef] = None
    Arc: Optional[GaugeChartArcConditionalFormattingTypeDef] = None

class KPIConditionalFormattingOptionTypeDef(BaseValidatorModel):
    PrimaryValue: Optional[KPIPrimaryValueConditionalFormattingTypeDef] = None
    ProgressBar: Optional[KPIProgressBarConditionalFormattingTypeDef] = None
    ActualValue: Optional[KPIActualValueConditionalFormattingTypeDef] = None
    ComparisonValue: Optional[KPIComparisonValueConditionalFormattingTypeDef] = None

class FilledMapShapeConditionalFormattingTypeDef(BaseValidatorModel):
    FieldId: str
    Format: Optional[ShapeConditionalFormatTypeDef] = None

class PivotTableCellConditionalFormattingTypeDef(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatTypeDef] = None
    Scope: Optional[PivotTableConditionalFormattingScopeTypeDef] = None
    Scopes: Optional[Sequence[PivotTableConditionalFormattingScopeTypeDef]] = None

class TableCellConditionalFormattingTypeDef(BaseValidatorModel):
    FieldId: str
    TextFormat: Optional[TextConditionalFormatTypeDef] = None

class ThemeTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ThemeId: Optional[str] = None
    Version: Optional[ThemeVersionTypeDef] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    Type: Optional[ThemeTypeType] = None

class GaugeChartOptionsTypeDef(BaseValidatorModel):
    PrimaryValueDisplayType: Optional[PrimaryValueDisplayTypeType] = None
    Comparison: Optional[ComparisonConfigurationTypeDef] = None
    ArcAxis: Optional[ArcAxisConfigurationTypeDef] = None
    Arc: Optional[ArcConfigurationTypeDef] = None
    PrimaryValueFontConfiguration: Optional[FontConfigurationTypeDef] = None

class KPIOptionsTypeDef(BaseValidatorModel):
    ProgressBar: Optional[ProgressBarOptionsTypeDef] = None
    TrendArrows: Optional[TrendArrowOptionsTypeDef] = None
    SecondaryValue: Optional[SecondaryValueOptionsTypeDef] = None
    Comparison: Optional[ComparisonConfigurationTypeDef] = None
    PrimaryValueDisplayType: Optional[PrimaryValueDisplayTypeType] = None
    PrimaryValueFontConfiguration: Optional[FontConfigurationTypeDef] = None
    SecondaryValueFontConfiguration: Optional[FontConfigurationTypeDef] = None
    Sparkline: Optional[KPISparklineOptionsTypeDef] = None
    VisualLayoutOptions: Optional[KPIVisualLayoutOptionsTypeDef] = None

class DateDimensionFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    DateGranularity: Optional[TimeGranularityType] = None
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[DateTimeFormatConfigurationTypeDef] = None

class DateMeasureFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    AggregationFunction: Optional[DateAggregationFunctionType] = None
    FormatConfiguration: Optional[DateTimeFormatConfigurationTypeDef] = None

class NumericalDimensionFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[NumberFormatConfigurationTypeDef] = None

class NumericalMeasureFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    AggregationFunction: Optional[NumericalAggregationFunctionTypeDef] = None
    FormatConfiguration: Optional[NumberFormatConfigurationTypeDef] = None

class ReferenceLineLabelConfigurationTypeDef(BaseValidatorModel):
    ValueLabelConfiguration: Optional[ReferenceLineValueLabelConfigurationTypeDef] = None
    CustomLabelConfiguration: Optional[ReferenceLineCustomLabelConfigurationTypeDef] = None
    FontConfiguration: Optional[FontConfigurationTypeDef] = None
    FontColor: Optional[str] = None
    HorizontalPosition: Optional[ReferenceLineLabelHorizontalPositionType] = None
    VerticalPosition: Optional[ReferenceLineLabelVerticalPositionType] = None

class CategoricalDimensionFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    HierarchyId: Optional[str] = None
    FormatConfiguration: Optional[StringFormatConfigurationTypeDef] = None

class CategoricalMeasureFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    AggregationFunction: Optional[CategoricalAggregationFunctionType] = None
    FormatConfiguration: Optional[StringFormatConfigurationTypeDef] = None

class FormatConfigurationTypeDef(BaseValidatorModel):
    StringFormatConfiguration: Optional[StringFormatConfigurationTypeDef] = None
    NumberFormatConfiguration: Optional[NumberFormatConfigurationTypeDef] = None
    DateTimeFormatConfiguration: Optional[DateTimeFormatConfigurationTypeDef] = None

class BodySectionRepeatDimensionConfigurationOutputTypeDef(BaseValidatorModel):
    DynamicCategoryDimensionConfiguration: Optional[       BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef     ] = None
    DynamicNumericDimensionConfiguration: Optional[       BodySectionDynamicNumericDimensionConfigurationOutputTypeDef     ] = None

class BodySectionRepeatDimensionConfigurationTypeDef(BaseValidatorModel):
    DynamicCategoryDimensionConfiguration: Optional[       BodySectionDynamicCategoryDimensionConfigurationTypeDef     ] = None
    DynamicNumericDimensionConfiguration: Optional[       BodySectionDynamicNumericDimensionConfigurationTypeDef     ] = None

class BarChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[List[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class BarChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class BoxPlotSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class BoxPlotSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class ComboChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[List[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class ComboChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class FilledMapSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None

class FilledMapSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None

class FunnelChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class FunnelChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class HeatMapSortConfigurationOutputTypeDef(BaseValidatorModel):
    HeatMapRowSort: Optional[List[FieldSortOptionsTypeDef]] = None
    HeatMapColumnSort: Optional[List[FieldSortOptionsTypeDef]] = None
    HeatMapRowItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    HeatMapColumnItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class HeatMapSortConfigurationTypeDef(BaseValidatorModel):
    HeatMapRowSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    HeatMapColumnSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    HeatMapRowItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    HeatMapColumnItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class KPISortConfigurationOutputTypeDef(BaseValidatorModel):
    TrendGroupSort: Optional[List[FieldSortOptionsTypeDef]] = None

class KPISortConfigurationTypeDef(BaseValidatorModel):
    TrendGroupSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None

class LineChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class LineChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class PieChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class PieChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    SmallMultiplesSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SmallMultiplesLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class RadarChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[List[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class RadarChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    ColorSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    ColorItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class SankeyDiagramSortConfigurationOutputTypeDef(BaseValidatorModel):
    WeightSort: Optional[List[FieldSortOptionsTypeDef]] = None
    SourceItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    DestinationItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class SankeyDiagramSortConfigurationTypeDef(BaseValidatorModel):
    WeightSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    SourceItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    DestinationItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class TableSortConfigurationOutputTypeDef(BaseValidatorModel):
    RowSort: Optional[List[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class TableSortConfigurationTypeDef(BaseValidatorModel):
    RowSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    PaginationConfiguration: Optional[PaginationConfigurationTypeDef] = None

class TreeMapSortConfigurationOutputTypeDef(BaseValidatorModel):
    TreeMapSort: Optional[List[FieldSortOptionsTypeDef]] = None
    TreeMapGroupItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class TreeMapSortConfigurationTypeDef(BaseValidatorModel):
    TreeMapSort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    TreeMapGroupItemsLimitConfiguration: Optional[ItemsLimitConfigurationTypeDef] = None

class WaterfallChartSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None
    BreakdownItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class WaterfallChartSortConfigurationTypeDef(BaseValidatorModel):
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None
    BreakdownItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None

class WordCloudSortConfigurationOutputTypeDef(BaseValidatorModel):
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    CategorySort: Optional[List[FieldSortOptionsTypeDef]] = None

class WordCloudSortConfigurationTypeDef(BaseValidatorModel):
    CategoryItemsLimit: Optional[ItemsLimitConfigurationTypeDef] = None
    CategorySort: Optional[Sequence[FieldSortOptionsTypeDef]] = None

class PivotFieldSortOptionsOutputTypeDef(BaseValidatorModel):
    FieldId: str
    SortBy: PivotTableSortByOutputTypeDef

class PivotFieldSortOptionsTypeDef(BaseValidatorModel):
    FieldId: str
    SortBy: PivotTableSortByTypeDef

class FieldBasedTooltipOutputTypeDef(BaseValidatorModel):
    AggregationVisibility: Optional[VisibilityType] = None
    TooltipTitleType: Optional[TooltipTitleTypeType] = None
    TooltipFields: Optional[List[TooltipItemTypeDef]] = None

class FieldBasedTooltipTypeDef(BaseValidatorModel):
    AggregationVisibility: Optional[VisibilityType] = None
    TooltipTitleType: Optional[TooltipTitleTypeType] = None
    TooltipFields: Optional[Sequence[TooltipItemTypeDef]] = None

class TopicDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None
    DataSets: Optional[List[DatasetMetadataOutputTypeDef]] = None

class TopicDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    UserExperienceVersion: Optional[TopicUserExperienceVersionType] = None
    DataSets: Optional[Sequence[DatasetMetadataTypeDef]] = None

class DescribeAssetBundleImportJobResponseTypeDef(BaseValidatorModel):
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

class StartAssetBundleImportJobRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AssetBundleImportJobId: str
    AssetBundleImportSource: AssetBundleImportSourceTypeDef
    OverrideParameters: Optional[AssetBundleImportJobOverrideParametersTypeDef] = None
    FailureAction: Optional[AssetBundleImportFailureActionType] = None
    OverridePermissions: Optional[AssetBundleImportJobOverridePermissionsTypeDef] = None
    OverrideTags: Optional[AssetBundleImportJobOverrideTagsTypeDef] = None
    OverrideValidationStrategy: Optional[       AssetBundleImportJobOverrideValidationStrategyTypeDef     ] = None

class CreateDataSourceRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDataSourceRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    DataSourceId: str
    Name: str
    DataSourceParameters: Optional[DataSourceParametersTypeDef] = None
    Credentials: Optional[DataSourceCredentialsTypeDef] = None
    VpcConnectionProperties: Optional[VpcConnectionPropertiesTypeDef] = None
    SslProperties: Optional[SslPropertiesTypeDef] = None

class SnapshotJobResultTypeDef(BaseValidatorModel):
    AnonymousUsers: Optional[List[AnonymousUserSnapshotJobResultTypeDef]] = None

class DefaultNewSheetConfigurationTypeDef(BaseValidatorModel):
    InteractiveLayoutConfiguration: Optional[DefaultInteractiveLayoutConfigurationTypeDef] = None
    PaginatedLayoutConfiguration: Optional[DefaultPaginatedLayoutConfigurationTypeDef] = None
    SheetContentType: Optional[SheetContentTypeType] = None

class BodySectionContentOutputTypeDef(BaseValidatorModel):
    Layout: Optional[SectionLayoutConfigurationOutputTypeDef] = None

class HeaderFooterSectionConfigurationOutputTypeDef(BaseValidatorModel):
    SectionId: str
    Layout: SectionLayoutConfigurationOutputTypeDef
    Style: Optional[SectionStyleTypeDef] = None

class BodySectionContentTypeDef(BaseValidatorModel):
    Layout: Optional[SectionLayoutConfigurationTypeDef] = None

class HeaderFooterSectionConfigurationTypeDef(BaseValidatorModel):
    SectionId: str
    Layout: SectionLayoutConfigurationTypeDef
    Style: Optional[SectionStyleTypeDef] = None

class VisualCustomActionOperationTypeDef(BaseValidatorModel):
    FilterOperation: Optional[CustomActionFilterOperationTypeDef] = None
    NavigationOperation: Optional[CustomActionNavigationOperationTypeDef] = None
    URLOperation: Optional[CustomActionURLOperationTypeDef] = None
    SetParametersOperation: Optional[CustomActionSetParametersOperationTypeDef] = None

class DescribeDataSetResponseTypeDef(BaseValidatorModel):
    DataSet: DataSetTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDataSetRequestRequestTypeDef(BaseValidatorModel):
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

class VisualCustomActionOutputTypeDef(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: VisualCustomActionTriggerType
    ActionOperations: List[VisualCustomActionOperationOutputTypeDef]
    Status: Optional[WidgetStatusType] = None

class DefaultFilterControlConfigurationOutputTypeDef(BaseValidatorModel):
    Title: str
    ControlOptions: DefaultFilterControlOptionsOutputTypeDef

class DefaultFilterControlConfigurationTypeDef(BaseValidatorModel):
    Title: str
    ControlOptions: DefaultFilterControlOptionsTypeDef

class TableFieldOptionTypeDef(BaseValidatorModel):
    FieldId: str
    Width: Optional[str] = None
    CustomLabel: Optional[str] = None
    Visibility: Optional[VisibilityType] = None
    URLStyling: Optional[TableFieldURLConfigurationTypeDef] = None

class GaugeChartConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       List[GaugeChartConditionalFormattingOptionOutputTypeDef]     ] = None

class KPIConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       List[KPIConditionalFormattingOptionOutputTypeDef]     ] = None

class FilledMapConditionalFormattingOptionOutputTypeDef(BaseValidatorModel):
    Shape: FilledMapShapeConditionalFormattingOutputTypeDef

class PivotTableConditionalFormattingOptionOutputTypeDef(BaseValidatorModel):
    Cell: Optional[PivotTableCellConditionalFormattingOutputTypeDef] = None

class TableConditionalFormattingOptionOutputTypeDef(BaseValidatorModel):
    Cell: Optional[TableCellConditionalFormattingOutputTypeDef] = None
    Row: Optional[TableRowConditionalFormattingOutputTypeDef] = None

class GaugeChartConditionalFormattingTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       Sequence[GaugeChartConditionalFormattingOptionTypeDef]     ] = None

class KPIConditionalFormattingTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       Sequence[KPIConditionalFormattingOptionTypeDef]     ] = None

class FilledMapConditionalFormattingOptionTypeDef(BaseValidatorModel):
    Shape: FilledMapShapeConditionalFormattingTypeDef

class PivotTableConditionalFormattingOptionTypeDef(BaseValidatorModel):
    Cell: Optional[PivotTableCellConditionalFormattingTypeDef] = None

class TableConditionalFormattingOptionTypeDef(BaseValidatorModel):
    Cell: Optional[TableCellConditionalFormattingTypeDef] = None
    Row: Optional[TableRowConditionalFormattingTypeDef] = None

class DescribeThemeResponseTypeDef(BaseValidatorModel):
    Theme: ThemeTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReferenceLineTypeDef(BaseValidatorModel):
    DataConfiguration: ReferenceLineDataConfigurationTypeDef
    Status: Optional[WidgetStatusType] = None
    StyleConfiguration: Optional[ReferenceLineStyleConfigurationTypeDef] = None
    LabelConfiguration: Optional[ReferenceLineLabelConfigurationTypeDef] = None

class DimensionFieldTypeDef(BaseValidatorModel):
    NumericalDimensionField: Optional[NumericalDimensionFieldTypeDef] = None
    CategoricalDimensionField: Optional[CategoricalDimensionFieldTypeDef] = None
    DateDimensionField: Optional[DateDimensionFieldTypeDef] = None

class MeasureFieldTypeDef(BaseValidatorModel):
    NumericalMeasureField: Optional[NumericalMeasureFieldTypeDef] = None
    CategoricalMeasureField: Optional[CategoricalMeasureFieldTypeDef] = None
    DateMeasureField: Optional[DateMeasureFieldTypeDef] = None
    CalculatedMeasureField: Optional[CalculatedMeasureFieldTypeDef] = None

class ColumnConfigurationOutputTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    FormatConfiguration: Optional[FormatConfigurationTypeDef] = None
    Role: Optional[ColumnRoleType] = None
    ColorsConfiguration: Optional[ColorsConfigurationOutputTypeDef] = None

class ColumnConfigurationTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    FormatConfiguration: Optional[FormatConfigurationTypeDef] = None
    Role: Optional[ColumnRoleType] = None
    ColorsConfiguration: Optional[ColorsConfigurationTypeDef] = None

class UnaggregatedFieldTypeDef(BaseValidatorModel):
    FieldId: str
    Column: ColumnIdentifierTypeDef
    FormatConfiguration: Optional[FormatConfigurationTypeDef] = None

class BodySectionRepeatConfigurationOutputTypeDef(BaseValidatorModel):
    DimensionConfigurations: Optional[       List[BodySectionRepeatDimensionConfigurationOutputTypeDef]     ] = None
    PageBreakConfiguration: Optional[BodySectionRepeatPageBreakConfigurationTypeDef] = None
    NonRepeatingVisuals: Optional[List[str]] = None

class BodySectionRepeatConfigurationTypeDef(BaseValidatorModel):
    DimensionConfigurations: Optional[       Sequence[BodySectionRepeatDimensionConfigurationTypeDef]     ] = None
    PageBreakConfiguration: Optional[BodySectionRepeatPageBreakConfigurationTypeDef] = None
    NonRepeatingVisuals: Optional[Sequence[str]] = None

class PivotTableSortConfigurationOutputTypeDef(BaseValidatorModel):
    FieldSortOptions: Optional[List[PivotFieldSortOptionsOutputTypeDef]] = None

class PivotTableSortConfigurationTypeDef(BaseValidatorModel):
    FieldSortOptions: Optional[Sequence[PivotFieldSortOptionsTypeDef]] = None

class TooltipOptionsOutputTypeDef(BaseValidatorModel):
    TooltipVisibility: Optional[VisibilityType] = None
    SelectedTooltipType: Optional[SelectedTooltipTypeType] = None
    FieldBasedTooltip: Optional[FieldBasedTooltipOutputTypeDef] = None

class TooltipOptionsTypeDef(BaseValidatorModel):
    TooltipVisibility: Optional[VisibilityType] = None
    SelectedTooltipType: Optional[SelectedTooltipTypeType] = None
    FieldBasedTooltip: Optional[FieldBasedTooltipTypeDef] = None

class DescribeTopicResponseTypeDef(BaseValidatorModel):
    Arn: str
    TopicId: str
    Topic: TopicDetailsOutputTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    Topic: TopicDetailsTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateTopicRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TopicId: str
    Topic: TopicDetailsTypeDef

class DescribeDashboardSnapshotJobResultResponseTypeDef(BaseValidatorModel):
    Arn: str
    JobStatus: SnapshotJobStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Result: SnapshotJobResultTypeDef
    ErrorInfo: SnapshotJobErrorInfoTypeDef
    RequestId: str
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisDefaultsTypeDef(BaseValidatorModel):
    DefaultNewSheetConfiguration: DefaultNewSheetConfigurationTypeDef

class VisualCustomActionTypeDef(BaseValidatorModel):
    CustomActionId: str
    Name: str
    Trigger: VisualCustomActionTriggerType
    ActionOperations: Sequence[VisualCustomActionOperationTypeDef]
    Status: Optional[WidgetStatusType] = None

class CustomContentVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[CustomContentConfigurationTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class EmptyVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class CategoryFilterOutputTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationOutputTypeDef
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class CategoryInnerFilterOutputTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationOutputTypeDef
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class NumericEqualityFilterOutputTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    MatchOperator: NumericEqualityMatchOperatorType
    NullOption: FilterNullOptionType
    Value: Optional[float] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class NumericRangeFilterOutputTypeDef(BaseValidatorModel):
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

class RelativeDatesFilterOutputTypeDef(BaseValidatorModel):
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

class TimeEqualityFilterOutputTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Value: Optional[datetime] = None
    ParameterName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class TimeRangeFilterOutputTypeDef(BaseValidatorModel):
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

class TopBottomFilterOutputTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    AggregationSortConfigurations: List[AggregationSortConfigurationTypeDef]
    Limit: Optional[int] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[       DefaultFilterControlConfigurationOutputTypeDef     ] = None

class CategoryFilterTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationTypeDef
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class CategoryInnerFilterTypeDef(BaseValidatorModel):
    Column: ColumnIdentifierTypeDef
    Configuration: CategoryFilterConfigurationTypeDef
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class NumericEqualityFilterTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    MatchOperator: NumericEqualityMatchOperatorType
    NullOption: FilterNullOptionType
    Value: Optional[float] = None
    SelectAllOptions: Optional[Literal["FILTER_ALL_VALUES"]] = None
    AggregationFunction: Optional[AggregationFunctionTypeDef] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class NumericRangeFilterTypeDef(BaseValidatorModel):
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

class RelativeDatesFilterTypeDef(BaseValidatorModel):
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

class TimeEqualityFilterTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    Value: Optional[TimestampTypeDef] = None
    ParameterName: Optional[str] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    RollingDate: Optional[RollingDateConfigurationTypeDef] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class TimeRangeFilterTypeDef(BaseValidatorModel):
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

class TopBottomFilterTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    AggregationSortConfigurations: Sequence[AggregationSortConfigurationTypeDef]
    Limit: Optional[int] = None
    TimeGranularity: Optional[TimeGranularityType] = None
    ParameterName: Optional[str] = None
    DefaultFilterControlConfiguration: Optional[DefaultFilterControlConfigurationTypeDef] = None

class TableFieldOptionsOutputTypeDef(BaseValidatorModel):
    SelectedFieldOptions: Optional[List[TableFieldOptionTypeDef]] = None
    Order: Optional[List[str]] = None
    PinnedFieldOptions: Optional[TablePinnedFieldOptionsOutputTypeDef] = None

class TableFieldOptionsTypeDef(BaseValidatorModel):
    SelectedFieldOptions: Optional[Sequence[TableFieldOptionTypeDef]] = None
    Order: Optional[Sequence[str]] = None
    PinnedFieldOptions: Optional[TablePinnedFieldOptionsTypeDef] = None

class FilledMapConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: List[FilledMapConditionalFormattingOptionOutputTypeDef]

class PivotTableConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       List[PivotTableConditionalFormattingOptionOutputTypeDef]     ] = None

class TableConditionalFormattingOutputTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       List[TableConditionalFormattingOptionOutputTypeDef]     ] = None

class FilledMapConditionalFormattingTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Sequence[FilledMapConditionalFormattingOptionTypeDef]

class PivotTableConditionalFormattingTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       Sequence[PivotTableConditionalFormattingOptionTypeDef]     ] = None

class TableConditionalFormattingTypeDef(BaseValidatorModel):
    ConditionalFormattingOptions: Optional[       Sequence[TableConditionalFormattingOptionTypeDef]     ] = None

class UniqueValuesComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Category: Optional[DimensionFieldTypeDef] = None

class BarChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[List[DimensionFieldTypeDef]] = None

class BarChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[Sequence[DimensionFieldTypeDef]] = None

class BoxPlotAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    GroupBy: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class BoxPlotAggregatedFieldWellsTypeDef(BaseValidatorModel):
    GroupBy: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class ComboChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    BarValues: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None
    LineValues: Optional[List[MeasureFieldTypeDef]] = None

class ComboChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    BarValues: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None
    LineValues: Optional[Sequence[MeasureFieldTypeDef]] = None

class FilledMapAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Geospatial: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class FilledMapAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Geospatial: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class ForecastComputationTypeDef(BaseValidatorModel):
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

class FunnelChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class FunnelChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class GaugeChartFieldWellsOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[MeasureFieldTypeDef]] = None
    TargetValues: Optional[List[MeasureFieldTypeDef]] = None

class GaugeChartFieldWellsTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    TargetValues: Optional[Sequence[MeasureFieldTypeDef]] = None

class GeospatialMapAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Geospatial: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None

class GeospatialMapAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Geospatial: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None

class GrowthRateComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    PeriodSize: Optional[int] = None

class HeatMapAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Rows: Optional[List[DimensionFieldTypeDef]] = None
    Columns: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class HeatMapAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Rows: Optional[Sequence[DimensionFieldTypeDef]] = None
    Columns: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class HistogramAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[MeasureFieldTypeDef]] = None

class HistogramAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class KPIFieldWellsOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[MeasureFieldTypeDef]] = None
    TargetValues: Optional[List[MeasureFieldTypeDef]] = None
    TrendGroups: Optional[List[DimensionFieldTypeDef]] = None

class KPIFieldWellsTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    TargetValues: Optional[Sequence[MeasureFieldTypeDef]] = None
    TrendGroups: Optional[Sequence[DimensionFieldTypeDef]] = None

class LineChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[List[DimensionFieldTypeDef]] = None

class LineChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[DimensionFieldTypeDef]] = None
    SmallMultiples: Optional[Sequence[DimensionFieldTypeDef]] = None

class MaximumMinimumComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Type: MaximumMinimumComputationTypeType
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None

class MetricComparisonComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    FromValue: Optional[MeasureFieldTypeDef] = None
    TargetValue: Optional[MeasureFieldTypeDef] = None

class PeriodOverPeriodComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None

class PeriodToDateComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    PeriodTimeGranularity: Optional[TimeGranularityType] = None

class PieChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    SmallMultiples: Optional[List[DimensionFieldTypeDef]] = None

class PieChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    SmallMultiples: Optional[Sequence[DimensionFieldTypeDef]] = None

class PivotTableAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Rows: Optional[List[DimensionFieldTypeDef]] = None
    Columns: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class PivotTableAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Rows: Optional[Sequence[DimensionFieldTypeDef]] = None
    Columns: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class RadarChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Color: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class RadarChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Color: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class SankeyDiagramAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Source: Optional[List[DimensionFieldTypeDef]] = None
    Destination: Optional[List[DimensionFieldTypeDef]] = None
    Weight: Optional[List[MeasureFieldTypeDef]] = None

class SankeyDiagramAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Source: Optional[Sequence[DimensionFieldTypeDef]] = None
    Destination: Optional[Sequence[DimensionFieldTypeDef]] = None
    Weight: Optional[Sequence[MeasureFieldTypeDef]] = None

class ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    XAxis: Optional[List[MeasureFieldTypeDef]] = None
    YAxis: Optional[List[MeasureFieldTypeDef]] = None
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Size: Optional[List[MeasureFieldTypeDef]] = None
    Label: Optional[List[DimensionFieldTypeDef]] = None

class ScatterPlotCategoricallyAggregatedFieldWellsTypeDef(BaseValidatorModel):
    XAxis: Optional[Sequence[MeasureFieldTypeDef]] = None
    YAxis: Optional[Sequence[MeasureFieldTypeDef]] = None
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Size: Optional[Sequence[MeasureFieldTypeDef]] = None
    Label: Optional[Sequence[DimensionFieldTypeDef]] = None

class ScatterPlotUnaggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    XAxis: Optional[List[DimensionFieldTypeDef]] = None
    YAxis: Optional[List[DimensionFieldTypeDef]] = None
    Size: Optional[List[MeasureFieldTypeDef]] = None
    Category: Optional[List[DimensionFieldTypeDef]] = None
    Label: Optional[List[DimensionFieldTypeDef]] = None

class ScatterPlotUnaggregatedFieldWellsTypeDef(BaseValidatorModel):
    XAxis: Optional[Sequence[DimensionFieldTypeDef]] = None
    YAxis: Optional[Sequence[DimensionFieldTypeDef]] = None
    Size: Optional[Sequence[MeasureFieldTypeDef]] = None
    Category: Optional[Sequence[DimensionFieldTypeDef]] = None
    Label: Optional[Sequence[DimensionFieldTypeDef]] = None

class TableAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    GroupBy: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None

class TableAggregatedFieldWellsTypeDef(BaseValidatorModel):
    GroupBy: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None

class TopBottomMoversComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Type: TopBottomComputationTypeType
    Name: Optional[str] = None
    Time: Optional[DimensionFieldTypeDef] = None
    Category: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    MoverSize: Optional[int] = None
    SortOrder: Optional[TopBottomSortOrderType] = None

class TopBottomRankedComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Type: TopBottomComputationTypeType
    Name: Optional[str] = None
    Category: Optional[DimensionFieldTypeDef] = None
    Value: Optional[MeasureFieldTypeDef] = None
    ResultSize: Optional[int] = None

class TotalAggregationComputationTypeDef(BaseValidatorModel):
    ComputationId: str
    Name: Optional[str] = None
    Value: Optional[MeasureFieldTypeDef] = None

class TreeMapAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Groups: Optional[List[DimensionFieldTypeDef]] = None
    Sizes: Optional[List[MeasureFieldTypeDef]] = None
    Colors: Optional[List[MeasureFieldTypeDef]] = None

class TreeMapAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Groups: Optional[Sequence[DimensionFieldTypeDef]] = None
    Sizes: Optional[Sequence[MeasureFieldTypeDef]] = None
    Colors: Optional[Sequence[MeasureFieldTypeDef]] = None

class WaterfallChartAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Categories: Optional[List[DimensionFieldTypeDef]] = None
    Values: Optional[List[MeasureFieldTypeDef]] = None
    Breakdowns: Optional[List[DimensionFieldTypeDef]] = None

class WaterfallChartAggregatedFieldWellsTypeDef(BaseValidatorModel):
    Categories: Optional[Sequence[DimensionFieldTypeDef]] = None
    Values: Optional[Sequence[MeasureFieldTypeDef]] = None
    Breakdowns: Optional[Sequence[DimensionFieldTypeDef]] = None

class WordCloudAggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    GroupBy: Optional[List[DimensionFieldTypeDef]] = None
    Size: Optional[List[MeasureFieldTypeDef]] = None

class WordCloudAggregatedFieldWellsTypeDef(BaseValidatorModel):
    GroupBy: Optional[Sequence[DimensionFieldTypeDef]] = None
    Size: Optional[Sequence[MeasureFieldTypeDef]] = None

class TableUnaggregatedFieldWellsOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[UnaggregatedFieldTypeDef]] = None

class TableUnaggregatedFieldWellsTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[UnaggregatedFieldTypeDef]] = None

class BodySectionConfigurationOutputTypeDef(BaseValidatorModel):
    SectionId: str
    Content: BodySectionContentOutputTypeDef
    Style: Optional[SectionStyleTypeDef] = None
    PageBreakConfiguration: Optional[SectionPageBreakConfigurationTypeDef] = None
    RepeatConfiguration: Optional[BodySectionRepeatConfigurationOutputTypeDef] = None

class BodySectionConfigurationTypeDef(BaseValidatorModel):
    SectionId: str
    Content: BodySectionContentTypeDef
    Style: Optional[SectionStyleTypeDef] = None
    PageBreakConfiguration: Optional[SectionPageBreakConfigurationTypeDef] = None
    RepeatConfiguration: Optional[BodySectionRepeatConfigurationTypeDef] = None

class CustomContentVisualTypeDef(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[CustomContentConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class EmptyVisualTypeDef(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class InnerFilterOutputTypeDef(BaseValidatorModel):
    CategoryInnerFilter: Optional[CategoryInnerFilterOutputTypeDef] = None

class InnerFilterTypeDef(BaseValidatorModel):
    CategoryInnerFilter: Optional[CategoryInnerFilterTypeDef] = None

class BarChartFieldWellsOutputTypeDef(BaseValidatorModel):
    BarChartAggregatedFieldWells: Optional[BarChartAggregatedFieldWellsOutputTypeDef] = None

class BarChartFieldWellsTypeDef(BaseValidatorModel):
    BarChartAggregatedFieldWells: Optional[BarChartAggregatedFieldWellsTypeDef] = None

class BoxPlotFieldWellsOutputTypeDef(BaseValidatorModel):
    BoxPlotAggregatedFieldWells: Optional[BoxPlotAggregatedFieldWellsOutputTypeDef] = None

class BoxPlotFieldWellsTypeDef(BaseValidatorModel):
    BoxPlotAggregatedFieldWells: Optional[BoxPlotAggregatedFieldWellsTypeDef] = None

class ComboChartFieldWellsOutputTypeDef(BaseValidatorModel):
    ComboChartAggregatedFieldWells: Optional[ComboChartAggregatedFieldWellsOutputTypeDef] = None

class ComboChartFieldWellsTypeDef(BaseValidatorModel):
    ComboChartAggregatedFieldWells: Optional[ComboChartAggregatedFieldWellsTypeDef] = None

class FilledMapFieldWellsOutputTypeDef(BaseValidatorModel):
    FilledMapAggregatedFieldWells: Optional[FilledMapAggregatedFieldWellsOutputTypeDef] = None

class FilledMapFieldWellsTypeDef(BaseValidatorModel):
    FilledMapAggregatedFieldWells: Optional[FilledMapAggregatedFieldWellsTypeDef] = None

class FunnelChartFieldWellsOutputTypeDef(BaseValidatorModel):
    FunnelChartAggregatedFieldWells: Optional[       FunnelChartAggregatedFieldWellsOutputTypeDef     ] = None

class FunnelChartFieldWellsTypeDef(BaseValidatorModel):
    FunnelChartAggregatedFieldWells: Optional[FunnelChartAggregatedFieldWellsTypeDef] = None

class GaugeChartConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[GaugeChartFieldWellsOutputTypeDef] = None
    GaugeChartOptions: Optional[GaugeChartOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    TooltipOptions: Optional[TooltipOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    ColorConfiguration: Optional[GaugeChartColorConfigurationTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GaugeChartConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[GaugeChartFieldWellsTypeDef] = None
    GaugeChartOptions: Optional[GaugeChartOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    TooltipOptions: Optional[TooltipOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    ColorConfiguration: Optional[GaugeChartColorConfigurationTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GeospatialMapFieldWellsOutputTypeDef(BaseValidatorModel):
    GeospatialMapAggregatedFieldWells: Optional[       GeospatialMapAggregatedFieldWellsOutputTypeDef     ] = None

class GeospatialMapFieldWellsTypeDef(BaseValidatorModel):
    GeospatialMapAggregatedFieldWells: Optional[GeospatialMapAggregatedFieldWellsTypeDef] = None

class HeatMapFieldWellsOutputTypeDef(BaseValidatorModel):
    HeatMapAggregatedFieldWells: Optional[HeatMapAggregatedFieldWellsOutputTypeDef] = None

class HeatMapFieldWellsTypeDef(BaseValidatorModel):
    HeatMapAggregatedFieldWells: Optional[HeatMapAggregatedFieldWellsTypeDef] = None

class HistogramFieldWellsOutputTypeDef(BaseValidatorModel):
    HistogramAggregatedFieldWells: Optional[HistogramAggregatedFieldWellsOutputTypeDef] = None

class HistogramFieldWellsTypeDef(BaseValidatorModel):
    HistogramAggregatedFieldWells: Optional[HistogramAggregatedFieldWellsTypeDef] = None

class KPIConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[KPIFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[KPISortConfigurationOutputTypeDef] = None
    KPIOptions: Optional[KPIOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class KPIConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[KPIFieldWellsTypeDef] = None
    SortConfiguration: Optional[KPISortConfigurationTypeDef] = None
    KPIOptions: Optional[KPIOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class LineChartFieldWellsOutputTypeDef(BaseValidatorModel):
    LineChartAggregatedFieldWells: Optional[LineChartAggregatedFieldWellsOutputTypeDef] = None

class LineChartFieldWellsTypeDef(BaseValidatorModel):
    LineChartAggregatedFieldWells: Optional[LineChartAggregatedFieldWellsTypeDef] = None

class PieChartFieldWellsOutputTypeDef(BaseValidatorModel):
    PieChartAggregatedFieldWells: Optional[PieChartAggregatedFieldWellsOutputTypeDef] = None

class PieChartFieldWellsTypeDef(BaseValidatorModel):
    PieChartAggregatedFieldWells: Optional[PieChartAggregatedFieldWellsTypeDef] = None

class PivotTableFieldWellsOutputTypeDef(BaseValidatorModel):
    PivotTableAggregatedFieldWells: Optional[PivotTableAggregatedFieldWellsOutputTypeDef] = None

class PivotTableFieldWellsTypeDef(BaseValidatorModel):
    PivotTableAggregatedFieldWells: Optional[PivotTableAggregatedFieldWellsTypeDef] = None

class RadarChartFieldWellsOutputTypeDef(BaseValidatorModel):
    RadarChartAggregatedFieldWells: Optional[RadarChartAggregatedFieldWellsOutputTypeDef] = None

class RadarChartFieldWellsTypeDef(BaseValidatorModel):
    RadarChartAggregatedFieldWells: Optional[RadarChartAggregatedFieldWellsTypeDef] = None

class SankeyDiagramFieldWellsOutputTypeDef(BaseValidatorModel):
    SankeyDiagramAggregatedFieldWells: Optional[       SankeyDiagramAggregatedFieldWellsOutputTypeDef     ] = None

class SankeyDiagramFieldWellsTypeDef(BaseValidatorModel):
    SankeyDiagramAggregatedFieldWells: Optional[SankeyDiagramAggregatedFieldWellsTypeDef] = None

class ScatterPlotFieldWellsOutputTypeDef(BaseValidatorModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional[       ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef     ] = None
    ScatterPlotUnaggregatedFieldWells: Optional[       ScatterPlotUnaggregatedFieldWellsOutputTypeDef     ] = None

class ScatterPlotFieldWellsTypeDef(BaseValidatorModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional[       ScatterPlotCategoricallyAggregatedFieldWellsTypeDef     ] = None
    ScatterPlotUnaggregatedFieldWells: Optional[ScatterPlotUnaggregatedFieldWellsTypeDef] = None

class ComputationTypeDef(BaseValidatorModel):
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

class TreeMapFieldWellsOutputTypeDef(BaseValidatorModel):
    TreeMapAggregatedFieldWells: Optional[TreeMapAggregatedFieldWellsOutputTypeDef] = None

class TreeMapFieldWellsTypeDef(BaseValidatorModel):
    TreeMapAggregatedFieldWells: Optional[TreeMapAggregatedFieldWellsTypeDef] = None

class WaterfallChartFieldWellsOutputTypeDef(BaseValidatorModel):
    WaterfallChartAggregatedFieldWells: Optional[       WaterfallChartAggregatedFieldWellsOutputTypeDef     ] = None

class WaterfallChartFieldWellsTypeDef(BaseValidatorModel):
    WaterfallChartAggregatedFieldWells: Optional[       WaterfallChartAggregatedFieldWellsTypeDef     ] = None

class WordCloudFieldWellsOutputTypeDef(BaseValidatorModel):
    WordCloudAggregatedFieldWells: Optional[WordCloudAggregatedFieldWellsOutputTypeDef] = None

class WordCloudFieldWellsTypeDef(BaseValidatorModel):
    WordCloudAggregatedFieldWells: Optional[WordCloudAggregatedFieldWellsTypeDef] = None

class TableFieldWellsOutputTypeDef(BaseValidatorModel):
    TableAggregatedFieldWells: Optional[TableAggregatedFieldWellsOutputTypeDef] = None
    TableUnaggregatedFieldWells: Optional[TableUnaggregatedFieldWellsOutputTypeDef] = None

class TableFieldWellsTypeDef(BaseValidatorModel):
    TableAggregatedFieldWells: Optional[TableAggregatedFieldWellsTypeDef] = None
    TableUnaggregatedFieldWells: Optional[TableUnaggregatedFieldWellsTypeDef] = None

class SectionBasedLayoutConfigurationOutputTypeDef(BaseValidatorModel):
    HeaderSections: List[HeaderFooterSectionConfigurationOutputTypeDef]
    BodySections: List[BodySectionConfigurationOutputTypeDef]
    FooterSections: List[HeaderFooterSectionConfigurationOutputTypeDef]
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptionsTypeDef

class SectionBasedLayoutConfigurationTypeDef(BaseValidatorModel):
    HeaderSections: Sequence[HeaderFooterSectionConfigurationTypeDef]
    BodySections: Sequence[BodySectionConfigurationTypeDef]
    FooterSections: Sequence[HeaderFooterSectionConfigurationTypeDef]
    CanvasSizeOptions: SectionBasedLayoutCanvasSizeOptionsTypeDef

class NestedFilterOutputTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    IncludeInnerSet: bool
    InnerFilter: InnerFilterOutputTypeDef

class NestedFilterTypeDef(BaseValidatorModel):
    FilterId: str
    Column: ColumnIdentifierTypeDef
    IncludeInnerSet: bool
    InnerFilter: InnerFilterTypeDef

class BarChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class BarChartConfigurationTypeDef(BaseValidatorModel):
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

class BoxPlotChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class BoxPlotChartConfigurationTypeDef(BaseValidatorModel):
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

class ComboChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class ComboChartConfigurationTypeDef(BaseValidatorModel):
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

class FilledMapConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[FilledMapFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[FilledMapSortConfigurationOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FilledMapConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[FilledMapFieldWellsTypeDef] = None
    SortConfiguration: Optional[FilledMapSortConfigurationTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FunnelChartConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[FunnelChartFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[FunnelChartSortConfigurationOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    DataLabelOptions: Optional[FunnelChartDataLabelOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class FunnelChartConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[FunnelChartFieldWellsTypeDef] = None
    SortConfiguration: Optional[FunnelChartSortConfigurationTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ValueLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    DataLabelOptions: Optional[FunnelChartDataLabelOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GaugeChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GaugeChartConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[GaugeChartConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class GaugeChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GaugeChartConfigurationTypeDef] = None
    ConditionalFormatting: Optional[GaugeChartConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class GeospatialMapConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[GeospatialMapFieldWellsOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    PointStyleOptions: Optional[GeospatialPointStyleOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class GeospatialMapConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[GeospatialMapFieldWellsTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    WindowOptions: Optional[GeospatialWindowOptionsTypeDef] = None
    MapStyleOptions: Optional[GeospatialMapStyleOptionsTypeDef] = None
    PointStyleOptions: Optional[GeospatialPointStyleOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HeatMapConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[HeatMapFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[HeatMapSortConfigurationOutputTypeDef] = None
    RowLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColumnLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    ColorScale: Optional[ColorScaleOutputTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HeatMapConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[HeatMapFieldWellsTypeDef] = None
    SortConfiguration: Optional[HeatMapSortConfigurationTypeDef] = None
    RowLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColumnLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    ColorScale: Optional[ColorScaleTypeDef] = None
    Legend: Optional[LegendOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HistogramConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[HistogramFieldWellsOutputTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsOutputTypeDef] = None
    BinOptions: Optional[HistogramBinOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Tooltip: Optional[TooltipOptionsOutputTypeDef] = None
    VisualPalette: Optional[VisualPaletteOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class HistogramConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[HistogramFieldWellsTypeDef] = None
    XAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    XAxisLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    YAxisDisplayOptions: Optional[AxisDisplayOptionsTypeDef] = None
    BinOptions: Optional[HistogramBinOptionsTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Tooltip: Optional[TooltipOptionsTypeDef] = None
    VisualPalette: Optional[VisualPaletteTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class KPIVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[KPIConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[KPIConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class KPIVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[KPIConfigurationTypeDef] = None
    ConditionalFormatting: Optional[KPIConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class LineChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class LineChartConfigurationTypeDef(BaseValidatorModel):
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

class PieChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class PieChartConfigurationTypeDef(BaseValidatorModel):
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

class PivotTableConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[PivotTableFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[PivotTableSortConfigurationOutputTypeDef] = None
    TableOptions: Optional[PivotTableOptionsOutputTypeDef] = None
    TotalOptions: Optional[PivotTableTotalOptionsOutputTypeDef] = None
    FieldOptions: Optional[PivotTableFieldOptionsOutputTypeDef] = None
    PaginatedReportOptions: Optional[PivotTablePaginatedReportOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class PivotTableConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[PivotTableFieldWellsTypeDef] = None
    SortConfiguration: Optional[PivotTableSortConfigurationTypeDef] = None
    TableOptions: Optional[PivotTableOptionsTypeDef] = None
    TotalOptions: Optional[PivotTableTotalOptionsTypeDef] = None
    FieldOptions: Optional[PivotTableFieldOptionsTypeDef] = None
    PaginatedReportOptions: Optional[PivotTablePaginatedReportOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class RadarChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class RadarChartConfigurationTypeDef(BaseValidatorModel):
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

class SankeyDiagramChartConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[SankeyDiagramFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[SankeyDiagramSortConfigurationOutputTypeDef] = None
    DataLabels: Optional[DataLabelOptionsOutputTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class SankeyDiagramChartConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[SankeyDiagramFieldWellsTypeDef] = None
    SortConfiguration: Optional[SankeyDiagramSortConfigurationTypeDef] = None
    DataLabels: Optional[DataLabelOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class ScatterPlotConfigurationOutputTypeDef(BaseValidatorModel):
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

class ScatterPlotConfigurationTypeDef(BaseValidatorModel):
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

class InsightConfigurationOutputTypeDef(BaseValidatorModel):
    Computations: Optional[List[ComputationTypeDef]] = None
    CustomNarrative: Optional[CustomNarrativeOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class InsightConfigurationTypeDef(BaseValidatorModel):
    Computations: Optional[Sequence[ComputationTypeDef]] = None
    CustomNarrative: Optional[CustomNarrativeOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TreeMapConfigurationOutputTypeDef(BaseValidatorModel):
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

class TreeMapConfigurationTypeDef(BaseValidatorModel):
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

class WaterfallChartConfigurationOutputTypeDef(BaseValidatorModel):
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

class WaterfallChartConfigurationTypeDef(BaseValidatorModel):
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

class WordCloudChartConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[WordCloudFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[WordCloudSortConfigurationOutputTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsOutputTypeDef] = None
    WordCloudOptions: Optional[WordCloudOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class WordCloudChartConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[WordCloudFieldWellsTypeDef] = None
    SortConfiguration: Optional[WordCloudSortConfigurationTypeDef] = None
    CategoryLabelOptions: Optional[ChartAxisLabelOptionsTypeDef] = None
    WordCloudOptions: Optional[WordCloudOptionsTypeDef] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TableConfigurationOutputTypeDef(BaseValidatorModel):
    FieldWells: Optional[TableFieldWellsOutputTypeDef] = None
    SortConfiguration: Optional[TableSortConfigurationOutputTypeDef] = None
    TableOptions: Optional[TableOptionsOutputTypeDef] = None
    TotalOptions: Optional[TotalOptionsOutputTypeDef] = None
    FieldOptions: Optional[TableFieldOptionsOutputTypeDef] = None
    PaginatedReportOptions: Optional[TablePaginatedReportOptionsTypeDef] = None
    TableInlineVisualizations: Optional[List[TableInlineVisualizationTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class TableConfigurationTypeDef(BaseValidatorModel):
    FieldWells: Optional[TableFieldWellsTypeDef] = None
    SortConfiguration: Optional[TableSortConfigurationTypeDef] = None
    TableOptions: Optional[TableOptionsTypeDef] = None
    TotalOptions: Optional[TotalOptionsTypeDef] = None
    FieldOptions: Optional[TableFieldOptionsTypeDef] = None
    PaginatedReportOptions: Optional[TablePaginatedReportOptionsTypeDef] = None
    TableInlineVisualizations: Optional[Sequence[TableInlineVisualizationTypeDef]] = None
    Interactions: Optional[VisualInteractionOptionsTypeDef] = None

class LayoutConfigurationOutputTypeDef(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfigurationOutputTypeDef] = None
    FreeFormLayout: Optional[FreeFormLayoutConfigurationOutputTypeDef] = None
    SectionBasedLayout: Optional[SectionBasedLayoutConfigurationOutputTypeDef] = None

class LayoutConfigurationTypeDef(BaseValidatorModel):
    GridLayout: Optional[GridLayoutConfigurationTypeDef] = None
    FreeFormLayout: Optional[FreeFormLayoutConfigurationTypeDef] = None
    SectionBasedLayout: Optional[SectionBasedLayoutConfigurationTypeDef] = None

class FilterOutputTypeDef(BaseValidatorModel):
    CategoryFilter: Optional[CategoryFilterOutputTypeDef] = None
    NumericRangeFilter: Optional[NumericRangeFilterOutputTypeDef] = None
    NumericEqualityFilter: Optional[NumericEqualityFilterOutputTypeDef] = None
    TimeEqualityFilter: Optional[TimeEqualityFilterOutputTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeFilterOutputTypeDef] = None
    RelativeDatesFilter: Optional[RelativeDatesFilterOutputTypeDef] = None
    TopBottomFilter: Optional[TopBottomFilterOutputTypeDef] = None
    NestedFilter: Optional[NestedFilterOutputTypeDef] = None

class FilterTypeDef(BaseValidatorModel):
    CategoryFilter: Optional[CategoryFilterTypeDef] = None
    NumericRangeFilter: Optional[NumericRangeFilterTypeDef] = None
    NumericEqualityFilter: Optional[NumericEqualityFilterTypeDef] = None
    TimeEqualityFilter: Optional[TimeEqualityFilterTypeDef] = None
    TimeRangeFilter: Optional[TimeRangeFilterTypeDef] = None
    RelativeDatesFilter: Optional[RelativeDatesFilterTypeDef] = None
    TopBottomFilter: Optional[TopBottomFilterTypeDef] = None
    NestedFilter: Optional[NestedFilterTypeDef] = None

class BarChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BarChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class BarChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BarChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class BoxPlotVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BoxPlotChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class BoxPlotVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[BoxPlotChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class ComboChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ComboChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class ComboChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ComboChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class FilledMapVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FilledMapConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[FilledMapConditionalFormattingOutputTypeDef] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class FilledMapVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FilledMapConfigurationTypeDef] = None
    ConditionalFormatting: Optional[FilledMapConditionalFormattingTypeDef] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class FunnelChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FunnelChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class FunnelChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[FunnelChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class GeospatialMapVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GeospatialMapConfigurationOutputTypeDef] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class GeospatialMapVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[GeospatialMapConfigurationTypeDef] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class HeatMapVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HeatMapConfigurationOutputTypeDef] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class HeatMapVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HeatMapConfigurationTypeDef] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class HistogramVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HistogramConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class HistogramVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[HistogramConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class LineChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[LineChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class LineChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[LineChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class PieChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PieChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class PieChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PieChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class PivotTableVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PivotTableConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[PivotTableConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class PivotTableVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[PivotTableConfigurationTypeDef] = None
    ConditionalFormatting: Optional[PivotTableConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class RadarChartVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[RadarChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class RadarChartVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[RadarChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class SankeyDiagramVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[SankeyDiagramChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class SankeyDiagramVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[SankeyDiagramChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class ScatterPlotVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ScatterPlotConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class ScatterPlotVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[ScatterPlotConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class InsightVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    InsightConfiguration: Optional[InsightConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class InsightVisualTypeDef(BaseValidatorModel):
    VisualId: str
    DataSetIdentifier: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    InsightConfiguration: Optional[InsightConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class TreeMapVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TreeMapConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class TreeMapVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TreeMapConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class WaterfallVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WaterfallChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class WaterfallVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WaterfallChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class WordCloudVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WordCloudChartConfigurationOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None
    ColumnHierarchies: Optional[List[ColumnHierarchyOutputTypeDef]] = None

class WordCloudVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[WordCloudChartConfigurationTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None
    ColumnHierarchies: Optional[Sequence[ColumnHierarchyTypeDef]] = None

class TableVisualOutputTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TableConfigurationOutputTypeDef] = None
    ConditionalFormatting: Optional[TableConditionalFormattingOutputTypeDef] = None
    Actions: Optional[List[VisualCustomActionOutputTypeDef]] = None

class TableVisualTypeDef(BaseValidatorModel):
    VisualId: str
    Title: Optional[VisualTitleLabelOptionsTypeDef] = None
    Subtitle: Optional[VisualSubtitleLabelOptionsTypeDef] = None
    ChartConfiguration: Optional[TableConfigurationTypeDef] = None
    ConditionalFormatting: Optional[TableConditionalFormattingTypeDef] = None
    Actions: Optional[Sequence[VisualCustomActionTypeDef]] = None

class LayoutOutputTypeDef(BaseValidatorModel):
    Configuration: LayoutConfigurationOutputTypeDef

class LayoutTypeDef(BaseValidatorModel):
    Configuration: LayoutConfigurationTypeDef

class FilterGroupOutputTypeDef(BaseValidatorModel):
    FilterGroupId: str
    Filters: List[FilterOutputTypeDef]
    ScopeConfiguration: FilterScopeConfigurationOutputTypeDef
    CrossDataset: CrossDatasetTypesType
    Status: Optional[WidgetStatusType] = None

class FilterGroupTypeDef(BaseValidatorModel):
    FilterGroupId: str
    Filters: Sequence[FilterTypeDef]
    ScopeConfiguration: FilterScopeConfigurationTypeDef
    CrossDataset: CrossDatasetTypesType
    Status: Optional[WidgetStatusType] = None

class VisualOutputTypeDef(BaseValidatorModel):
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

class VisualTypeDef(BaseValidatorModel):
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

class SheetDefinitionOutputTypeDef(BaseValidatorModel):
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

class SheetDefinitionTypeDef(BaseValidatorModel):
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

class AnalysisDefinitionOutputTypeDef(BaseValidatorModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[List[SheetDefinitionOutputTypeDef]] = None
    CalculatedFields: Optional[List[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutputTypeDef]] = None
    FilterGroups: Optional[List[FilterGroupOutputTypeDef]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutputTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class DashboardVersionDefinitionOutputTypeDef(BaseValidatorModel):
    DataSetIdentifierDeclarations: List[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[List[SheetDefinitionOutputTypeDef]] = None
    CalculatedFields: Optional[List[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutputTypeDef]] = None
    FilterGroups: Optional[List[FilterGroupOutputTypeDef]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutputTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class TemplateVersionDefinitionOutputTypeDef(BaseValidatorModel):
    DataSetConfigurations: List[DataSetConfigurationOutputTypeDef]
    Sheets: Optional[List[SheetDefinitionOutputTypeDef]] = None
    CalculatedFields: Optional[List[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[List[ParameterDeclarationOutputTypeDef]] = None
    FilterGroups: Optional[List[FilterGroupOutputTypeDef]] = None
    ColumnConfigurations: Optional[List[ColumnConfigurationOutputTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class AnalysisDefinitionTypeDef(BaseValidatorModel):
    DataSetIdentifierDeclarations: Sequence[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[Sequence[SheetDefinitionTypeDef]] = None
    CalculatedFields: Optional[Sequence[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[Sequence[ParameterDeclarationTypeDef]] = None
    FilterGroups: Optional[Sequence[FilterGroupTypeDef]] = None
    ColumnConfigurations: Optional[Sequence[ColumnConfigurationTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class DashboardVersionDefinitionTypeDef(BaseValidatorModel):
    DataSetIdentifierDeclarations: Sequence[DataSetIdentifierDeclarationTypeDef]
    Sheets: Optional[Sequence[SheetDefinitionTypeDef]] = None
    CalculatedFields: Optional[Sequence[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[Sequence[ParameterDeclarationTypeDef]] = None
    FilterGroups: Optional[Sequence[FilterGroupTypeDef]] = None
    ColumnConfigurations: Optional[Sequence[ColumnConfigurationTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class TemplateVersionDefinitionTypeDef(BaseValidatorModel):
    DataSetConfigurations: Sequence[DataSetConfigurationTypeDef]
    Sheets: Optional[Sequence[SheetDefinitionTypeDef]] = None
    CalculatedFields: Optional[Sequence[CalculatedFieldTypeDef]] = None
    ParameterDeclarations: Optional[Sequence[ParameterDeclarationTypeDef]] = None
    FilterGroups: Optional[Sequence[FilterGroupTypeDef]] = None
    ColumnConfigurations: Optional[Sequence[ColumnConfigurationTypeDef]] = None
    AnalysisDefaults: Optional[AnalysisDefaultsTypeDef] = None
    Options: Optional[AssetOptionsTypeDef] = None

class DescribeAnalysisDefinitionResponseTypeDef(BaseValidatorModel):
    AnalysisId: str
    Name: str
    Errors: List[AnalysisErrorTypeDef]
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: AnalysisDefinitionOutputTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDashboardDefinitionResponseTypeDef(BaseValidatorModel):
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

class DescribeTemplateDefinitionResponseTypeDef(BaseValidatorModel):
    Name: str
    TemplateId: str
    Errors: List[TemplateErrorTypeDef]
    ResourceStatus: ResourceStatusType
    ThemeArn: str
    Definition: TemplateVersionDefinitionOutputTypeDef
    Status: int
    RequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnalysisRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAnalysisRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AnalysisId: str
    Name: str
    Parameters: Optional[ParametersTypeDef] = None
    SourceEntity: Optional[AnalysisSourceEntityTypeDef] = None
    ThemeArn: Optional[str] = None
    Definition: Optional[AnalysisDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

class CreateDashboardRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDashboardRequestRequestTypeDef(BaseValidatorModel):
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

class CreateTemplateRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    Name: Optional[str] = None
    Permissions: Optional[Sequence[ResourcePermissionUnionTypeDef]] = None
    SourceEntity: Optional[TemplateSourceEntityTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VersionDescription: Optional[str] = None
    Definition: Optional[TemplateVersionDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

class UpdateTemplateRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    TemplateId: str
    SourceEntity: Optional[TemplateSourceEntityTypeDef] = None
    VersionDescription: Optional[str] = None
    Name: Optional[str] = None
    Definition: Optional[TemplateVersionDefinitionTypeDef] = None
    ValidationStrategy: Optional[ValidationStrategyTypeDef] = None

