from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.databrew.databrew_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AllowedStatisticsOutput(BaseValidatorModel):
    Statistics: List[str]


class AllowedStatistics(BaseValidatorModel):
    Statistics: List[str]


# This class is the input for the 'batch_delete_recipe_version' function.
class BatchDeleteRecipeVersionRequest(BaseValidatorModel):
    Name: str
    RecipeVersions: List[str]


class RecipeVersionErrorDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    RecipeVersion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ColumnSelector(BaseValidatorModel):
    Regex: Optional[str] = None
    Name: Optional[str] = None


class ConditionExpression(BaseValidatorModel):
    Condition: str
    TargetColumn: str
    Value: Optional[str] = None


class JobSample(BaseValidatorModel):
    Mode: Optional[SampleModeType] = None
    Size: Optional[int] = None


class S3Location(BaseValidatorModel):
    Bucket: str
    Key: Optional[str] = None
    BucketOwner: Optional[str] = None


class ValidationConfiguration(BaseValidatorModel):
    RulesetArn: str
    ValidationMode: Optional[Literal['CHECK_ALL']] = None


class Sample(BaseValidatorModel):
    Type: SampleTypeType
    Size: Optional[int] = None


class RecipeReference(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None


# This class is the input for the 'create_schedule' function.
class CreateScheduleRequest(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


class CsvOptions(BaseValidatorModel):
    Delimiter: Optional[str] = None
    HeaderRow: Optional[bool] = None


class CsvOutputOptions(BaseValidatorModel):
    Delimiter: Optional[str] = None


class DatetimeOptions(BaseValidatorModel):
    Format: str
    TimezoneOffset: Optional[str] = None
    LocaleCode: Optional[str] = None


class FilterExpressionOutput(BaseValidatorModel):
    Expression: str
    ValuesMap: Dict[str, str]


class FilterExpression(BaseValidatorModel):
    Expression: str
    ValuesMap: Dict[str, str]


# This class is the input for the 'delete_dataset' function.
class DeleteDatasetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_job' function.
class DeleteJobRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_project' function.
class DeleteProjectRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_recipe_version' function.
class DeleteRecipeVersionRequest(BaseValidatorModel):
    Name: str
    RecipeVersion: str


# This class is the input for the 'delete_ruleset' function.
class DeleteRulesetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_schedule' function.
class DeleteScheduleRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_dataset' function.
class DescribeDatasetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_job' function.
class DescribeJobRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_job_run' function.
class DescribeJobRunRequest(BaseValidatorModel):
    Name: str
    RunId: str


# This class is the input for the 'describe_project' function.
class DescribeProjectRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_recipe' function.
class DescribeRecipeRequest(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None


# This class is the input for the 'describe_ruleset' function.
class DescribeRulesetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_schedule' function.
class DescribeScheduleRequest(BaseValidatorModel):
    Name: str


class ExcelOptionsOutput(BaseValidatorModel):
    SheetNames: Optional[List[str]] = None
    SheetIndexes: Optional[List[int]] = None
    HeaderRow: Optional[bool] = None


class ExcelOptions(BaseValidatorModel):
    SheetNames: Optional[List[str]] = None
    SheetIndexes: Optional[List[int]] = None
    HeaderRow: Optional[bool] = None


class FilesLimit(BaseValidatorModel):
    MaxFiles: int
    OrderedBy: Optional[Literal['LAST_MODIFIED_DATE']] = None
    Order: Optional[OrderType] = None


class JsonOptions(BaseValidatorModel):
    MultiLine: Optional[bool] = None


class Metadata(BaseValidatorModel):
    SourceArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_datasets' function.
class ListDatasetsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_job_runs' function.
class ListJobRunsRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_jobs' function.
class ListJobsRequest(BaseValidatorModel):
    DatasetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProjectName: Optional[str] = None


# This class is the input for the 'list_projects' function.
class ListProjectsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_recipe_versions' function.
class ListRecipeVersionsRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_recipes' function.
class ListRecipesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RecipeVersion: Optional[str] = None


# This class is the input for the 'list_rulesets' function.
class ListRulesetsRequest(BaseValidatorModel):
    TargetArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RulesetItem(BaseValidatorModel):
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


# This class is the input for the 'list_schedules' function.
class ListSchedulesRequest(BaseValidatorModel):
    JobName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Schedule(BaseValidatorModel):
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'publish_recipe' function.
class PublishRecipeRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class RecipeActionOutput(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None


class RecipeAction(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None


class Threshold(BaseValidatorModel):
    Value: float
    Type: Optional[ThresholdTypeType] = None
    Unit: Optional[ThresholdUnitType] = None


class ViewFrame(BaseValidatorModel):
    StartColumnIndex: int
    ColumnRange: Optional[int] = None
    HiddenColumns: Optional[List[str]] = None
    StartRowIndex: Optional[int] = None
    RowRange: Optional[int] = None
    Analytics: Optional[AnalyticsModeType] = None


# This class is the input for the 'start_job_run' function.
class StartJobRunRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'start_project_session' function.
class StartProjectSessionRequest(BaseValidatorModel):
    Name: str
    AssumeControl: Optional[bool] = None


class StatisticOverrideOutput(BaseValidatorModel):
    Statistic: str
    Parameters: Dict[str, str]


class StatisticOverride(BaseValidatorModel):
    Statistic: str
    Parameters: Dict[str, str]


# This class is the input for the 'stop_job_run' function.
class StopJobRunRequest(BaseValidatorModel):
    Name: str
    RunId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_schedule' function.
class UpdateScheduleRequest(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[List[str]] = None


class EntityDetectorConfigurationOutput(BaseValidatorModel):
    EntityTypes: List[str]
    AllowedStatistics: Optional[List[AllowedStatisticsOutput]] = None


class EntityDetectorConfiguration(BaseValidatorModel):
    EntityTypes: List[str]
    AllowedStatistics: Optional[List[AllowedStatistics]] = None


# This class is the output for the 'batch_delete_recipe_version' function.
class BatchDeleteRecipeVersionResponse(BaseValidatorModel):
    Name: str
    Errors: List[RecipeVersionErrorDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_dataset' function.
class CreateDatasetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_profile_job' function.
class CreateProfileJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_project' function.
class CreateProjectResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_recipe_job' function.
class CreateRecipeJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_recipe' function.
class CreateRecipeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ruleset' function.
class CreateRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_schedule' function.
class CreateScheduleResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_dataset' function.
class DeleteDatasetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_job' function.
class DeleteJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_project' function.
class DeleteProjectResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_recipe_version' function.
class DeleteRecipeVersionResponse(BaseValidatorModel):
    Name: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ruleset' function.
class DeleteRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_schedule' function.
class DeleteScheduleResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_schedule' function.
class DescribeScheduleResponse(BaseValidatorModel):
    CreateDate: datetime
    CreatedBy: str
    JobNames: List[str]
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    CronExpression: str
    Tags: Dict[str, str]
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'publish_recipe' function.
class PublishRecipeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_project_session_action' function.
class SendProjectSessionActionResponse(BaseValidatorModel):
    Result: str
    Name: str
    ActionId: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_job_run' function.
class StartJobRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_project_session' function.
class StartProjectSessionResponse(BaseValidatorModel):
    Name: str
    ClientSessionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_job_run' function.
class StopJobRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_dataset' function.
class UpdateDatasetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_profile_job' function.
class UpdateProfileJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project' function.
class UpdateProjectResponse(BaseValidatorModel):
    LastModifiedDate: datetime
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_recipe_job' function.
class UpdateRecipeJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_recipe' function.
class UpdateRecipeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ruleset' function.
class UpdateRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_schedule' function.
class UpdateScheduleResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DataCatalogInputDefinition(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    TempDirectory: Optional[S3Location] = None


class DatabaseInputDefinition(BaseValidatorModel):
    GlueConnectionName: str
    DatabaseTableName: Optional[str] = None
    TempDirectory: Optional[S3Location] = None
    QueryString: Optional[str] = None


class DatabaseTableOutputOptions(BaseValidatorModel):
    TableName: str
    TempDirectory: Optional[S3Location] = None


class S3TableOutputOptions(BaseValidatorModel):
    Location: S3Location


# This class is the input for the 'create_project' function.
class CreateProjectRequest(BaseValidatorModel):
    DatasetName: str
    Name: str
    RecipeName: str
    RoleArn: str
    Sample: Optional[Sample] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_project' function.
class DescribeProjectResponse(BaseValidatorModel):
    CreateDate: datetime
    CreatedBy: str
    DatasetName: str
    LastModifiedDate: datetime
    LastModifiedBy: str
    Name: str
    RecipeName: str
    ResourceArn: str
    Sample: Sample
    RoleArn: str
    Tags: Dict[str, str]
    SessionStatus: SessionStatusType
    OpenedBy: str
    OpenDate: datetime
    ResponseMetadata: ResponseMetadata


class Project(BaseValidatorModel):
    Name: str
    RecipeName: str
    AccountId: Optional[str] = None
    CreateDate: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DatasetName: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    ResourceArn: Optional[str] = None
    Sample: Optional[Sample] = None
    Tags: Optional[Dict[str, str]] = None
    RoleArn: Optional[str] = None
    OpenedBy: Optional[str] = None
    OpenDate: Optional[datetime] = None


# This class is the input for the 'update_project' function.
class UpdateProjectRequest(BaseValidatorModel):
    RoleArn: str
    Name: str
    Sample: Optional[Sample] = None


class OutputFormatOptions(BaseValidatorModel):
    Csv: Optional[CsvOutputOptions] = None


class DatasetParameterOutput(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    DatetimeOptions: Optional[DatetimeOptions] = None
    CreateColumn: Optional[bool] = None
    Filter: Optional[FilterExpressionOutput] = None


class DatasetParameter(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    DatetimeOptions: Optional[DatetimeOptions] = None
    CreateColumn: Optional[bool] = None
    Filter: Optional[FilterExpression] = None


class FormatOptionsOutput(BaseValidatorModel):
    Json: Optional[JsonOptions] = None
    Excel: Optional[ExcelOptionsOutput] = None
    Csv: Optional[CsvOptions] = None


class FormatOptions(BaseValidatorModel):
    Json: Optional[JsonOptions] = None
    Excel: Optional[ExcelOptions] = None
    Csv: Optional[CsvOptions] = None


class ListDatasetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunsRequestPaginate(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    DatasetName: Optional[str] = None
    ProjectName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecipeVersionsRequestPaginate(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecipesRequestPaginate(BaseValidatorModel):
    RecipeVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesetsRequestPaginate(BaseValidatorModel):
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchedulesRequestPaginate(BaseValidatorModel):
    JobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_rulesets' function.
class ListRulesetsResponse(BaseValidatorModel):
    Rulesets: List[RulesetItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_schedules' function.
class ListSchedulesResponse(BaseValidatorModel):
    Schedules: List[Schedule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RecipeStepOutput(BaseValidatorModel):
    Action: RecipeActionOutput
    ConditionExpressions: Optional[List[ConditionExpression]] = None

RecipeActionUnion = Union[RecipeAction, RecipeActionOutput]


class RuleOutput(BaseValidatorModel):
    Name: str
    CheckExpression: str
    Disabled: Optional[bool] = None
    SubstitutionMap: Optional[Dict[str, str]] = None
    Threshold: Optional[Threshold] = None
    ColumnSelectors: Optional[List[ColumnSelector]] = None


class Rule(BaseValidatorModel):
    Name: str
    CheckExpression: str
    Disabled: Optional[bool] = None
    SubstitutionMap: Optional[Dict[str, str]] = None
    Threshold: Optional[Threshold] = None
    ColumnSelectors: Optional[List[ColumnSelector]] = None


class StatisticsConfigurationOutput(BaseValidatorModel):
    IncludedStatistics: Optional[List[str]] = None
    Overrides: Optional[List[StatisticOverrideOutput]] = None


class StatisticsConfiguration(BaseValidatorModel):
    IncludedStatistics: Optional[List[str]] = None
    Overrides: Optional[List[StatisticOverride]] = None


class Input(BaseValidatorModel):
    S3InputDefinition: Optional[S3Location] = None
    DataCatalogInputDefinition: Optional[DataCatalogInputDefinition] = None
    DatabaseInputDefinition: Optional[DatabaseInputDefinition] = None
    Metadata: Optional[Metadata] = None


class DatabaseOutput(BaseValidatorModel):
    GlueConnectionName: str
    DatabaseOptions: DatabaseTableOutputOptions
    DatabaseOutputMode: Optional[Literal['NEW_TABLE']] = None


class DataCatalogOutput(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    S3Options: Optional[S3TableOutputOptions] = None
    DatabaseOptions: Optional[DatabaseTableOutputOptions] = None
    Overwrite: Optional[bool] = None


# This class is the output for the 'list_projects' function.
class ListProjectsResponse(BaseValidatorModel):
    Projects: List[Project]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Extra(BaseValidatorModel):
    Location: S3Location
    CompressionFormat: Optional[CompressionFormatType] = None
    Format: Optional[OutputFormatType] = None
    PartitionColumns: Optional[List[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptions] = None
    MaxOutputFiles: Optional[int] = None


class Output(BaseValidatorModel):
    Location: S3Location
    CompressionFormat: Optional[CompressionFormatType] = None
    Format: Optional[OutputFormatType] = None
    PartitionColumns: Optional[List[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptions] = None
    MaxOutputFiles: Optional[int] = None


class PathOptionsOutput(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpressionOutput] = None
    FilesLimit: Optional[FilesLimit] = None
    Parameters: Optional[Dict[str, DatasetParameterOutput]] = None


class PathOptions(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpression] = None
    FilesLimit: Optional[FilesLimit] = None
    Parameters: Optional[Dict[str, DatasetParameter]] = None

FormatOptionsUnion = Union[FormatOptions, FormatOptionsOutput]


# This class is the output for the 'describe_recipe' function.
class DescribeRecipeResponse(BaseValidatorModel):
    CreatedBy: str
    CreateDate: datetime
    LastModifiedBy: str
    LastModifiedDate: datetime
    ProjectName: str
    PublishedBy: str
    PublishedDate: datetime
    Description: str
    Name: str
    Steps: List[RecipeStepOutput]
    Tags: Dict[str, str]
    ResourceArn: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadata


class Recipe(BaseValidatorModel):
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
    Steps: Optional[List[RecipeStepOutput]] = None
    Tags: Optional[Dict[str, str]] = None
    RecipeVersion: Optional[str] = None


class RecipeStep(BaseValidatorModel):
    Action: RecipeActionUnion
    ConditionExpressions: Optional[List[ConditionExpression]] = None


# This class is the output for the 'describe_ruleset' function.
class DescribeRulesetResponse(BaseValidatorModel):
    Name: str
    Description: str
    TargetArn: str
    Rules: List[RuleOutput]
    CreateDate: datetime
    CreatedBy: str
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

RuleUnion = Union[Rule, RuleOutput]


class ColumnStatisticsConfigurationOutput(BaseValidatorModel):
    Statistics: StatisticsConfigurationOutput
    Selectors: Optional[List[ColumnSelector]] = None


class ColumnStatisticsConfiguration(BaseValidatorModel):
    Statistics: StatisticsConfiguration
    Selectors: Optional[List[ColumnSelector]] = None


class JobRun(BaseValidatorModel):
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
    Outputs: Optional[List[Extra]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutput]] = None
    DatabaseOutputs: Optional[List[DatabaseOutput]] = None
    RecipeReference: Optional[RecipeReference] = None
    StartedBy: Optional[str] = None
    StartedOn: Optional[datetime] = None
    JobSample: Optional[JobSample] = None
    ValidationConfigurations: Optional[List[ValidationConfiguration]] = None


class Job(BaseValidatorModel):
    Name: str
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DatasetName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    Type: Optional[JobTypeType] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[List[Extra]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutput]] = None
    DatabaseOutputs: Optional[List[DatabaseOutput]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReference] = None
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    Timeout: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    JobSample: Optional[JobSample] = None
    ValidationConfigurations: Optional[List[ValidationConfiguration]] = None

UnionType = Union[Output, Extra]


class Dataset(BaseValidatorModel):
    Name: str
    Input: Input
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsOutput] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    Source: Optional[SourceType] = None
    PathOptions: Optional[PathOptionsOutput] = None
    Tags: Optional[Dict[str, str]] = None
    ResourceArn: Optional[str] = None


# This class is the output for the 'describe_dataset' function.
class DescribeDatasetResponse(BaseValidatorModel):
    CreatedBy: str
    CreateDate: datetime
    Name: str
    Format: InputFormatType
    FormatOptions: FormatOptionsOutput
    Input: Input
    LastModifiedDate: datetime
    LastModifiedBy: str
    Source: SourceType
    PathOptions: PathOptionsOutput
    Tags: Dict[str, str]
    ResourceArn: str
    ResponseMetadata: ResponseMetadata

PathOptionsUnion = Union[PathOptions, PathOptionsOutput]


# This class is the output for the 'list_recipe_versions' function.
class ListRecipeVersionsResponse(BaseValidatorModel):
    Recipes: List[Recipe]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_recipes' function.
class ListRecipesResponse(BaseValidatorModel):
    Recipes: List[Recipe]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

RecipeStepUnion = Union[RecipeStep, RecipeStepOutput]


# This class is the input for the 'create_ruleset' function.
class CreateRulesetRequest(BaseValidatorModel):
    Name: str
    TargetArn: str
    Rules: List[RuleUnion]
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_ruleset' function.
class UpdateRulesetRequest(BaseValidatorModel):
    Name: str
    Rules: List[RuleUnion]
    Description: Optional[str] = None


class ProfileConfigurationOutput(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfigurationOutput] = None
    ProfileColumns: Optional[List[ColumnSelector]] = None
    ColumnStatisticsConfigurations: Optional[List[ColumnStatisticsConfigurationOutput]] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfigurationOutput] = None


class ProfileConfiguration(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfiguration] = None
    ProfileColumns: Optional[List[ColumnSelector]] = None
    ColumnStatisticsConfigurations: Optional[List[ColumnStatisticsConfiguration]] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfiguration] = None


# This class is the output for the 'list_job_runs' function.
class ListJobRunsResponse(BaseValidatorModel):
    JobRuns: List[JobRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_jobs' function.
class ListJobsResponse(BaseValidatorModel):
    Jobs: List[Job]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_recipe_job' function.
class CreateRecipeJobRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    DatasetName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[List[UnionType]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutput]] = None
    DatabaseOutputs: Optional[List[DatabaseOutput]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReference] = None
    Tags: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None


# This class is the input for the 'update_recipe_job' function.
class UpdateRecipeJobRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[List[UnionType]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutput]] = None
    DatabaseOutputs: Optional[List[DatabaseOutput]] = None
    Timeout: Optional[int] = None


# This class is the output for the 'list_datasets' function.
class ListDatasetsResponse(BaseValidatorModel):
    Datasets: List[Dataset]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_dataset' function.
class CreateDatasetRequest(BaseValidatorModel):
    Name: str
    Input: Input
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsUnion] = None
    PathOptions: Optional[PathOptionsUnion] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_dataset' function.
class UpdateDatasetRequest(BaseValidatorModel):
    Name: str
    Input: Input
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsUnion] = None
    PathOptions: Optional[PathOptionsUnion] = None


# This class is the input for the 'create_recipe' function.
class CreateRecipeRequest(BaseValidatorModel):
    Name: str
    Steps: List[RecipeStepUnion]
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'send_project_session_action' function.
class SendProjectSessionActionRequest(BaseValidatorModel):
    Name: str
    Preview: Optional[bool] = None
    RecipeStep: Optional[RecipeStepUnion] = None
    StepIndex: Optional[int] = None
    ClientSessionId: Optional[str] = None
    ViewFrame: Optional[ViewFrame] = None


# This class is the input for the 'update_recipe' function.
class UpdateRecipeRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Steps: Optional[List[RecipeStepUnion]] = None


# This class is the output for the 'describe_job' function.
class DescribeJobResponse(BaseValidatorModel):
    CreateDate: datetime
    CreatedBy: str
    DatasetName: str
    EncryptionKeyArn: str
    EncryptionMode: EncryptionModeType
    Name: str
    Type: JobTypeType
    LastModifiedBy: str
    LastModifiedDate: datetime
    LogSubscription: LogSubscriptionType
    MaxCapacity: int
    MaxRetries: int
    Outputs: List[Extra]
    DataCatalogOutputs: List[DataCatalogOutput]
    DatabaseOutputs: List[DatabaseOutput]
    ProjectName: str
    ProfileConfiguration: ProfileConfigurationOutput
    ValidationConfigurations: List[ValidationConfiguration]
    RecipeReference: RecipeReference
    ResourceArn: str
    RoleArn: str
    Tags: Dict[str, str]
    Timeout: int
    JobSample: JobSample
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_job_run' function.
class DescribeJobRunResponse(BaseValidatorModel):
    Attempt: int
    CompletedOn: datetime
    DatasetName: str
    ErrorMessage: str
    ExecutionTime: int
    JobName: str
    ProfileConfiguration: ProfileConfigurationOutput
    ValidationConfigurations: List[ValidationConfiguration]
    RunId: str
    State: JobRunStateType
    LogSubscription: LogSubscriptionType
    LogGroupName: str
    Outputs: List[Extra]
    DataCatalogOutputs: List[DataCatalogOutput]
    DatabaseOutputs: List[DatabaseOutput]
    RecipeReference: RecipeReference
    StartedBy: str
    StartedOn: datetime
    JobSample: JobSample
    ResponseMetadata: ResponseMetadata

ProfileConfigurationUnion = Union[ProfileConfiguration, ProfileConfigurationOutput]


# This class is the input for the 'create_profile_job' function.
class CreateProfileJobRequest(BaseValidatorModel):
    DatasetName: str
    Name: str
    OutputLocation: S3Location
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Configuration: Optional[ProfileConfigurationUnion] = None
    ValidationConfigurations: Optional[List[ValidationConfiguration]] = None
    Tags: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSample] = None


# This class is the input for the 'update_profile_job' function.
class UpdateProfileJobRequest(BaseValidatorModel):
    Name: str
    OutputLocation: S3Location
    RoleArn: str
    Configuration: Optional[ProfileConfigurationUnion] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    ValidationConfigurations: Optional[List[ValidationConfiguration]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSample] = None