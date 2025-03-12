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
from aws_resource_validator.pydantic_models.databrew_constants import *

class AllowedStatisticsOutputTypeDef(BaseValidatorModel):
    Statistics: List[str]


class AllowedStatisticsTypeDef(BaseValidatorModel):
    Statistics: Sequence[str]


class BatchDeleteRecipeVersionRequestTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersions: Sequence[str]


class RecipeVersionErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    RecipeVersion: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ColumnSelectorTypeDef(BaseValidatorModel):
    Regex: Optional[str] = None
    Name: Optional[str] = None


class ConditionExpressionTypeDef(BaseValidatorModel):
    Condition: str
    TargetColumn: str
    Value: Optional[str] = None


class JobSampleTypeDef(BaseValidatorModel):
    Mode: Optional[SampleModeType] = None
    Size: Optional[int] = None


class S3LocationTypeDef(BaseValidatorModel):
    Bucket: str
    Key: Optional[str] = None
    BucketOwner: Optional[str] = None


class ValidationConfigurationTypeDef(BaseValidatorModel):
    RulesetArn: str
    ValidationMode: Optional[Literal["CHECK_ALL"]] = None


class RecipeReferenceTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None


class CreateScheduleRequestTypeDef(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class CsvOptionsTypeDef(BaseValidatorModel):
    Delimiter: Optional[str] = None
    HeaderRow: Optional[bool] = None


class CsvOutputOptionsTypeDef(BaseValidatorModel):
    Delimiter: Optional[str] = None


class DatetimeOptionsTypeDef(BaseValidatorModel):
    Format: str
    TimezoneOffset: Optional[str] = None
    LocaleCode: Optional[str] = None


class FilterExpressionOutputTypeDef(BaseValidatorModel):
    Expression: str
    ValuesMap: Dict[str, str]


class FilterExpressionTypeDef(BaseValidatorModel):
    Expression: str
    ValuesMap: Mapping[str, str]


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteJobRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteRecipeVersionRequestTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: str


class DeleteRulesetRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteScheduleRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeJobRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeJobRunRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str


class DescribeProjectRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeRecipeRequestTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None


class DescribeRulesetRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeScheduleRequestTypeDef(BaseValidatorModel):
    Name: str


class ExcelOptionsOutputTypeDef(BaseValidatorModel):
    SheetNames: Optional[List[str]] = None
    SheetIndexes: Optional[List[int]] = None
    HeaderRow: Optional[bool] = None


class ExcelOptionsTypeDef(BaseValidatorModel):
    SheetNames: Optional[Sequence[str]] = None
    SheetIndexes: Optional[Sequence[int]] = None
    HeaderRow: Optional[bool] = None


class FilesLimitTypeDef(BaseValidatorModel):
    MaxFiles: int
    OrderedBy: Optional[Literal["LAST_MODIFIED_DATE"]] = None
    Order: Optional[OrderType] = None


class JsonOptionsTypeDef(BaseValidatorModel):
    MultiLine: Optional[bool] = None


class MetadataTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobRunsRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    DatasetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProjectName: Optional[str] = None


class ListProjectsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRecipeVersionsRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRecipesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RecipeVersion: Optional[str] = None


class ListRulesetsRequestTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RulesetItemTypeDef(BaseValidatorModel):
    Name: str
    TargetArn: str
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    Description: Optional[str] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    ResourceArn: Optional[str] = None
    RuleCount: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None


class ListSchedulesRequestTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ScheduleTypeDef(BaseValidatorModel):
    Name: str
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    JobNames: Optional[List[str]] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    ResourceArn: Optional[str] = None
    CronExpression: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PublishRecipeRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class RecipeActionOutputTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None


class RecipeActionTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None


class ViewFrameTypeDef(BaseValidatorModel):
    StartColumnIndex: int
    ColumnRange: Optional[int] = None
    HiddenColumns: Optional[Sequence[str]] = None
    StartRowIndex: Optional[int] = None
    RowRange: Optional[int] = None
    Analytics: Optional[AnalyticsModeType] = None


class StartJobRunRequestTypeDef(BaseValidatorModel):
    Name: str


class StartProjectSessionRequestTypeDef(BaseValidatorModel):
    Name: str
    AssumeControl: Optional[bool] = None


class StatisticOverrideOutputTypeDef(BaseValidatorModel):
    Statistic: str
    Parameters: Dict[str, str]


class StatisticOverrideTypeDef(BaseValidatorModel):
    Statistic: str
    Parameters: Mapping[str, str]


class StopJobRunRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateScheduleRequestTypeDef(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None


class EntityDetectorConfigurationOutputTypeDef(BaseValidatorModel):
    EntityTypes: List[str]
    AllowedStatistics: Optional[List[AllowedStatisticsOutputTypeDef]] = None


class EntityDetectorConfigurationTypeDef(BaseValidatorModel):
    EntityTypes: Sequence[str]
    AllowedStatistics: Optional[Sequence[AllowedStatisticsTypeDef]] = None


class BatchDeleteRecipeVersionResponseTypeDef(BaseValidatorModel):
    Name: str
    Errors: List[RecipeVersionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProfileJobResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProjectResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRecipeJobResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRecipeResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateScheduleResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDatasetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteJobResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProjectResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRecipeVersionResponseTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteScheduleResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeScheduleResponseTypeDef(BaseValidatorModel):
    CreateDate: datetime
    CreatedBy: str
    JobNames: List[str]
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    CronExpression: str
    Tags: Dict[str, str]
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PublishRecipeResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendProjectSessionActionResponseTypeDef(BaseValidatorModel):
    Result: str
    Name: str
    ActionId: int
    ResponseMetadata: ResponseMetadataTypeDef


class StartJobRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartProjectSessionResponseTypeDef(BaseValidatorModel):
    Name: str
    ClientSessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopJobRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDatasetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProfileJobResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProjectResponseTypeDef(BaseValidatorModel):
    LastModifiedDate: datetime
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRecipeJobResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRecipeResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateScheduleResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DataCatalogInputDefinitionTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    TempDirectory: Optional[S3LocationTypeDef] = None


class DatabaseInputDefinitionTypeDef(BaseValidatorModel):
    GlueConnectionName: str
    DatabaseTableName: Optional[str] = None
    TempDirectory: Optional[S3LocationTypeDef] = None
    QueryString: Optional[str] = None


class DatabaseTableOutputOptionsTypeDef(BaseValidatorModel):
    TableName: str
    TempDirectory: Optional[S3LocationTypeDef] = None


class S3TableOutputOptionsTypeDef(BaseValidatorModel):
    Location: S3LocationTypeDef


class SampleTypeDef(BaseValidatorModel):
    pass


class CreateProjectRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    Name: str
    RecipeName: str
    RoleArn: str
    Sample: Optional[SampleTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class DescribeProjectResponseTypeDef(BaseValidatorModel):
    CreateDate: datetime
    CreatedBy: str
    DatasetName: str
    LastModifiedDate: datetime
    LastModifiedBy: str
    Name: str
    RecipeName: str
    ResourceArn: str
    Sample: SampleTypeDef
    RoleArn: str
    Tags: Dict[str, str]
    SessionStatus: SessionStatusType
    OpenedBy: str
    OpenDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ProjectTypeDef(BaseValidatorModel):
    Name: str
    RecipeName: str
    AccountId: Optional[str] = None
    CreateDate: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DatasetName: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    ResourceArn: Optional[str] = None
    Sample: Optional[SampleTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    RoleArn: Optional[str] = None
    OpenedBy: Optional[str] = None
    OpenDate: Optional[datetime] = None


class UpdateProjectRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    Name: str
    Sample: Optional[SampleTypeDef] = None


class OutputFormatOptionsTypeDef(BaseValidatorModel):
    Csv: Optional[CsvOutputOptionsTypeDef] = None


class FormatOptionsOutputTypeDef(BaseValidatorModel):
    Json: Optional[JsonOptionsTypeDef] = None
    Excel: Optional[ExcelOptionsOutputTypeDef] = None
    Csv: Optional[CsvOptionsTypeDef] = None


class FormatOptionsTypeDef(BaseValidatorModel):
    Json: Optional[JsonOptionsTypeDef] = None
    Excel: Optional[ExcelOptionsTypeDef] = None
    Csv: Optional[CsvOptionsTypeDef] = None


class ListDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobRunsRequestPaginateTypeDef(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    DatasetName: Optional[str] = None
    ProjectName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecipeVersionsRequestPaginateTypeDef(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecipesRequestPaginateTypeDef(BaseValidatorModel):
    RecipeVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesetsRequestPaginateTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchedulesRequestPaginateTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesetsResponseTypeDef(BaseValidatorModel):
    Rulesets: List[RulesetItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSchedulesResponseTypeDef(BaseValidatorModel):
    Schedules: List[ScheduleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RecipeStepOutputTypeDef(BaseValidatorModel):
    Action: RecipeActionOutputTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None


class ThresholdTypeDef(BaseValidatorModel):
    pass


class RuleOutputTypeDef(BaseValidatorModel):
    Name: str
    CheckExpression: str
    Disabled: Optional[bool] = None
    SubstitutionMap: Optional[Dict[str, str]] = None
    Threshold: Optional[ThresholdTypeDef] = None
    ColumnSelectors: Optional[List[ColumnSelectorTypeDef]] = None


class RuleTypeDef(BaseValidatorModel):
    Name: str
    CheckExpression: str
    Disabled: Optional[bool] = None
    SubstitutionMap: Optional[Mapping[str, str]] = None
    Threshold: Optional[ThresholdTypeDef] = None
    ColumnSelectors: Optional[Sequence[ColumnSelectorTypeDef]] = None


class StatisticsConfigurationOutputTypeDef(BaseValidatorModel):
    IncludedStatistics: Optional[List[str]] = None
    Overrides: Optional[List[StatisticOverrideOutputTypeDef]] = None


class StatisticsConfigurationTypeDef(BaseValidatorModel):
    IncludedStatistics: Optional[Sequence[str]] = None
    Overrides: Optional[Sequence[StatisticOverrideTypeDef]] = None


class InputTypeDef(BaseValidatorModel):
    S3InputDefinition: Optional[S3LocationTypeDef] = None
    DataCatalogInputDefinition: Optional[DataCatalogInputDefinitionTypeDef] = None
    DatabaseInputDefinition: Optional[DatabaseInputDefinitionTypeDef] = None
    Metadata: Optional[MetadataTypeDef] = None


class DatabaseOutputTypeDef(BaseValidatorModel):
    GlueConnectionName: str
    DatabaseOptions: DatabaseTableOutputOptionsTypeDef
    DatabaseOutputMode: Optional[Literal["NEW_TABLE"]] = None


class DataCatalogOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    S3Options: Optional[S3TableOutputOptionsTypeDef] = None
    DatabaseOptions: Optional[DatabaseTableOutputOptionsTypeDef] = None
    Overwrite: Optional[bool] = None


class ListProjectsResponseTypeDef(BaseValidatorModel):
    Projects: List[ProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExtraTypeDef(BaseValidatorModel):
    Location: S3LocationTypeDef
    CompressionFormat: Optional[CompressionFormatType] = None
    Format: Optional[OutputFormatType] = None
    PartitionColumns: Optional[List[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptionsTypeDef] = None
    MaxOutputFiles: Optional[int] = None


class OutputTypeDef(BaseValidatorModel):
    Location: S3LocationTypeDef
    CompressionFormat: Optional[CompressionFormatType] = None
    Format: Optional[OutputFormatType] = None
    PartitionColumns: Optional[Sequence[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptionsTypeDef] = None
    MaxOutputFiles: Optional[int] = None


class DatasetParameterOutputTypeDef(BaseValidatorModel):
    pass


class PathOptionsOutputTypeDef(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpressionOutputTypeDef] = None
    FilesLimit: Optional[FilesLimitTypeDef] = None
    Parameters: Optional[Dict[str, DatasetParameterOutputTypeDef]] = None


class DatasetParameterTypeDef(BaseValidatorModel):
    pass


class PathOptionsTypeDef(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpressionTypeDef] = None
    FilesLimit: Optional[FilesLimitTypeDef] = None
    Parameters: Optional[Mapping[str, DatasetParameterTypeDef]] = None


class DescribeRecipeResponseTypeDef(BaseValidatorModel):
    CreatedBy: str
    CreateDate: datetime
    LastModifiedBy: str
    LastModifiedDate: datetime
    ProjectName: str
    PublishedBy: str
    PublishedDate: datetime
    Description: str
    Name: str
    Steps: List[RecipeStepOutputTypeDef]
    Tags: Dict[str, str]
    ResourceArn: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class RecipeTypeDef(BaseValidatorModel):
    Name: str
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    ProjectName: Optional[str] = None
    PublishedBy: Optional[str] = None
    PublishedDate: Optional[datetime] = None
    Description: Optional[str] = None
    ResourceArn: Optional[str] = None
    Steps: Optional[List[RecipeStepOutputTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None
    RecipeVersion: Optional[str] = None


class RecipeActionUnionTypeDef(BaseValidatorModel):
    pass


class RecipeStepTypeDef(BaseValidatorModel):
    Action: RecipeActionUnionTypeDef
    ConditionExpressions: Optional[Sequence[ConditionExpressionTypeDef]] = None


class DescribeRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    TargetArn: str
    Rules: List[RuleOutputTypeDef]
    CreateDate: datetime
    CreatedBy: str
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnStatisticsConfigurationOutputTypeDef(BaseValidatorModel):
    Statistics: StatisticsConfigurationOutputTypeDef
    Selectors: Optional[List[ColumnSelectorTypeDef]] = None


class ColumnStatisticsConfigurationTypeDef(BaseValidatorModel):
    Statistics: StatisticsConfigurationTypeDef
    Selectors: Optional[Sequence[ColumnSelectorTypeDef]] = None


class JobRunTypeDef(BaseValidatorModel):
    Attempt: Optional[int] = None
    CompletedOn: Optional[datetime] = None
    DatasetName: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ExecutionTime: Optional[int] = None
    JobName: Optional[str] = None
    RunId: Optional[str] = None
    State: Optional[JobRunStateType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    LogGroupName: Optional[str] = None
    Outputs: Optional[List[ExtraTypeDef]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[List[DatabaseOutputTypeDef]] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    StartedBy: Optional[str] = None
    StartedOn: Optional[datetime] = None
    JobSample: Optional[JobSampleTypeDef] = None
    ValidationConfigurations: Optional[List[ValidationConfigurationTypeDef]] = None


class DatasetTypeDef(BaseValidatorModel):
    Name: str
    Input: InputTypeDef
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsOutputTypeDef] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    Source: Optional[SourceType] = None
    PathOptions: Optional[PathOptionsOutputTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    ResourceArn: Optional[str] = None


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    CreatedBy: str
    CreateDate: datetime
    Name: str
    Format: InputFormatType
    FormatOptions: FormatOptionsOutputTypeDef
    Input: InputTypeDef
    LastModifiedDate: datetime
    LastModifiedBy: str
    Source: SourceType
    PathOptions: PathOptionsOutputTypeDef
    Tags: Dict[str, str]
    ResourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecipeVersionsResponseTypeDef(BaseValidatorModel):
    Recipes: List[RecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRecipesResponseTypeDef(BaseValidatorModel):
    Recipes: List[RecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class CreateRulesetRequestTypeDef(BaseValidatorModel):
    Name: str
    TargetArn: str
    Rules: Sequence[RuleUnionTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateRulesetRequestTypeDef(BaseValidatorModel):
    Name: str
    Rules: Sequence[RuleUnionTypeDef]
    Description: Optional[str] = None


class ProfileConfigurationOutputTypeDef(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfigurationOutputTypeDef] = None
    ProfileColumns: Optional[List[ColumnSelectorTypeDef]] = None
    ColumnStatisticsConfigurations: Optional[List[ColumnStatisticsConfigurationOutputTypeDef]] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfigurationOutputTypeDef] = None


class ProfileConfigurationTypeDef(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfigurationTypeDef] = None
    ProfileColumns: Optional[Sequence[ColumnSelectorTypeDef]] = None
    ColumnStatisticsConfigurations: Optional[Sequence[ColumnStatisticsConfigurationTypeDef]] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfigurationTypeDef] = None


class ListJobRunsResponseTypeDef(BaseValidatorModel):
    JobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class JobTypeDef(BaseValidatorModel):
    pass


class ListJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UnionTypeDef(BaseValidatorModel):
    pass


class CreateRecipeJobRequestTypeDef(BaseValidatorModel):
    Name: str
    RoleArn: str
    DatasetName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[Sequence[UnionTypeDef]] = None
    DataCatalogOutputs: Optional[Sequence[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[Sequence[DatabaseOutputTypeDef]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None


class UpdateRecipeJobRequestTypeDef(BaseValidatorModel):
    Name: str
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[Sequence[UnionTypeDef]] = None
    DataCatalogOutputs: Optional[Sequence[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[Sequence[DatabaseOutputTypeDef]] = None
    Timeout: Optional[int] = None


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    Datasets: List[DatasetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FormatOptionsUnionTypeDef(BaseValidatorModel):
    pass


class PathOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    Name: str
    Input: InputTypeDef
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsUnionTypeDef] = None
    PathOptions: Optional[PathOptionsUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDatasetRequestTypeDef(BaseValidatorModel):
    Name: str
    Input: InputTypeDef
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsUnionTypeDef] = None
    PathOptions: Optional[PathOptionsUnionTypeDef] = None


class RecipeStepUnionTypeDef(BaseValidatorModel):
    pass


class CreateRecipeRequestTypeDef(BaseValidatorModel):
    Name: str
    Steps: Sequence[RecipeStepUnionTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class SendProjectSessionActionRequestTypeDef(BaseValidatorModel):
    Name: str
    Preview: Optional[bool] = None
    RecipeStep: Optional[RecipeStepUnionTypeDef] = None
    StepIndex: Optional[int] = None
    ClientSessionId: Optional[str] = None
    ViewFrame: Optional[ViewFrameTypeDef] = None


class UpdateRecipeRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Steps: Optional[Sequence[RecipeStepUnionTypeDef]] = None


class DescribeJobRunResponseTypeDef(BaseValidatorModel):
    Attempt: int
    CompletedOn: datetime
    DatasetName: str
    ErrorMessage: str
    ExecutionTime: int
    JobName: str
    ProfileConfiguration: ProfileConfigurationOutputTypeDef
    ValidationConfigurations: List[ValidationConfigurationTypeDef]
    RunId: str
    State: JobRunStateType
    LogSubscription: LogSubscriptionType
    LogGroupName: str
    Outputs: List[ExtraTypeDef]
    DataCatalogOutputs: List[DataCatalogOutputTypeDef]
    DatabaseOutputs: List[DatabaseOutputTypeDef]
    RecipeReference: RecipeReferenceTypeDef
    StartedBy: str
    StartedOn: datetime
    JobSample: JobSampleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ProfileConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateProfileJobRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    Name: str
    OutputLocation: S3LocationTypeDef
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Configuration: Optional[ProfileConfigurationUnionTypeDef] = None
    ValidationConfigurations: Optional[Sequence[ValidationConfigurationTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSampleTypeDef] = None


class UpdateProfileJobRequestTypeDef(BaseValidatorModel):
    Name: str
    OutputLocation: S3LocationTypeDef
    RoleArn: str
    Configuration: Optional[ProfileConfigurationUnionTypeDef] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    ValidationConfigurations: Optional[Sequence[ValidationConfigurationTypeDef]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSampleTypeDef] = None


