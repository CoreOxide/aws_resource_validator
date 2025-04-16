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

class AllowedStatisticsOutput(BaseValidatorModel):
    Statistics: List[str]


class AllowedStatistics(BaseValidatorModel):
    Statistics: Sequence[str]


class BatchDeleteRecipeVersionRequest(BaseValidatorModel):
    Name: str
    RecipeVersions: Sequence[str]


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
    ValidationMode: Optional[Literal["CHECK_ALL"]] = None


class RecipeReference(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None


class CreateScheduleRequest(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


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
    ValuesMap: Mapping[str, str]


class DeleteDatasetRequest(BaseValidatorModel):
    Name: str


class DeleteJobRequest(BaseValidatorModel):
    Name: str


class DeleteProjectRequest(BaseValidatorModel):
    Name: str


class DeleteRecipeVersionRequest(BaseValidatorModel):
    Name: str
    RecipeVersion: str


class DeleteRulesetRequest(BaseValidatorModel):
    Name: str


class DeleteScheduleRequest(BaseValidatorModel):
    Name: str


class DescribeDatasetRequest(BaseValidatorModel):
    Name: str


class DescribeJobRequest(BaseValidatorModel):
    Name: str


class DescribeJobRunRequest(BaseValidatorModel):
    Name: str
    RunId: str


class DescribeProjectRequest(BaseValidatorModel):
    Name: str


class DescribeRecipeRequest(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None


class DescribeRulesetRequest(BaseValidatorModel):
    Name: str


class DescribeScheduleRequest(BaseValidatorModel):
    Name: str


class ExcelOptionsOutput(BaseValidatorModel):
    SheetNames: Optional[List[str]] = None
    SheetIndexes: Optional[List[int]] = None
    HeaderRow: Optional[bool] = None


class ExcelOptions(BaseValidatorModel):
    SheetNames: Optional[Sequence[str]] = None
    SheetIndexes: Optional[Sequence[int]] = None
    HeaderRow: Optional[bool] = None


class FilesLimit(BaseValidatorModel):
    MaxFiles: int
    OrderedBy: Optional[Literal["LAST_MODIFIED_DATE"]] = None
    Order: Optional[OrderType] = None


class JsonOptions(BaseValidatorModel):
    MultiLine: Optional[bool] = None


class Metadata(BaseValidatorModel):
    SourceArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDatasetsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobRunsRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobsRequest(BaseValidatorModel):
    DatasetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProjectName: Optional[str] = None


class ListProjectsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRecipeVersionsRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRecipesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RecipeVersion: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PublishRecipeRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class RecipeActionOutput(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None


class RecipeAction(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None


class ViewFrame(BaseValidatorModel):
    StartColumnIndex: int
    ColumnRange: Optional[int] = None
    HiddenColumns: Optional[Sequence[str]] = None
    StartRowIndex: Optional[int] = None
    RowRange: Optional[int] = None
    Analytics: Optional[AnalyticsModeType] = None


class StartJobRunRequest(BaseValidatorModel):
    Name: str


class StartProjectSessionRequest(BaseValidatorModel):
    Name: str
    AssumeControl: Optional[bool] = None


class StatisticOverrideOutput(BaseValidatorModel):
    Statistic: str
    Parameters: Dict[str, str]


class StatisticOverride(BaseValidatorModel):
    Statistic: str
    Parameters: Mapping[str, str]


class StopJobRunRequest(BaseValidatorModel):
    Name: str
    RunId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateScheduleRequest(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None


class EntityDetectorConfigurationOutput(BaseValidatorModel):
    EntityTypes: List[str]
    AllowedStatistics: Optional[List[AllowedStatisticsOutput]] = None


class EntityDetectorConfiguration(BaseValidatorModel):
    EntityTypes: Sequence[str]
    AllowedStatistics: Optional[Sequence[AllowedStatistics]] = None


class BatchDeleteRecipeVersionResponse(BaseValidatorModel):
    Name: str
    Errors: List[RecipeVersionErrorDetail]
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateProfileJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateProjectResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateRecipeJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateRecipeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateScheduleResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteDatasetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteProjectResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteRecipeVersionResponse(BaseValidatorModel):
    Name: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadata


class DeleteRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteScheduleResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


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


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PublishRecipeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class SendProjectSessionActionResponse(BaseValidatorModel):
    Result: str
    Name: str
    ActionId: int
    ResponseMetadata: ResponseMetadata


class StartJobRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


class StartProjectSessionResponse(BaseValidatorModel):
    Name: str
    ClientSessionId: str
    ResponseMetadata: ResponseMetadata


class StopJobRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


class UpdateDatasetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateProfileJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateProjectResponse(BaseValidatorModel):
    LastModifiedDate: datetime
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateRecipeJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateRecipeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


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


class Sample(BaseValidatorModel):
    pass


class CreateProjectRequest(BaseValidatorModel):
    DatasetName: str
    Name: str
    RecipeName: str
    RoleArn: str
    Sample: Optional[Sample] = None
    Tags: Optional[Mapping[str, str]] = None


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


class UpdateProjectRequest(BaseValidatorModel):
    RoleArn: str
    Name: str
    Sample: Optional[Sample] = None


class OutputFormatOptions(BaseValidatorModel):
    Csv: Optional[CsvOutputOptions] = None


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


class ListRulesetsResponse(BaseValidatorModel):
    Rulesets: List[RulesetItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchedulesResponse(BaseValidatorModel):
    Schedules: List[Schedule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RecipeStepOutput(BaseValidatorModel):
    Action: RecipeActionOutput
    ConditionExpressions: Optional[List[ConditionExpression]] = None


class Threshold(BaseValidatorModel):
    pass


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
    SubstitutionMap: Optional[Mapping[str, str]] = None
    Threshold: Optional[Threshold] = None
    ColumnSelectors: Optional[Sequence[ColumnSelector]] = None


class StatisticsConfigurationOutput(BaseValidatorModel):
    IncludedStatistics: Optional[List[str]] = None
    Overrides: Optional[List[StatisticOverrideOutput]] = None


class StatisticsConfiguration(BaseValidatorModel):
    IncludedStatistics: Optional[Sequence[str]] = None
    Overrides: Optional[Sequence[StatisticOverride]] = None


class Input(BaseValidatorModel):
    S3InputDefinition: Optional[S3Location] = None
    DataCatalogInputDefinition: Optional[DataCatalogInputDefinition] = None
    DatabaseInputDefinition: Optional[DatabaseInputDefinition] = None
    Metadata: Optional[Metadata] = None


class DatabaseOutput(BaseValidatorModel):
    GlueConnectionName: str
    DatabaseOptions: DatabaseTableOutputOptions
    DatabaseOutputMode: Optional[Literal["NEW_TABLE"]] = None


class DataCatalogOutput(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    S3Options: Optional[S3TableOutputOptions] = None
    DatabaseOptions: Optional[DatabaseTableOutputOptions] = None
    Overwrite: Optional[bool] = None


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
    PartitionColumns: Optional[Sequence[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptions] = None
    MaxOutputFiles: Optional[int] = None


class DatasetParameterOutput(BaseValidatorModel):
    pass


class PathOptionsOutput(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpressionOutput] = None
    FilesLimit: Optional[FilesLimit] = None
    Parameters: Optional[Dict[str, DatasetParameterOutput]] = None


class DatasetParameter(BaseValidatorModel):
    pass


class PathOptions(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpression] = None
    FilesLimit: Optional[FilesLimit] = None
    Parameters: Optional[Mapping[str, DatasetParameter]] = None


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


class RecipeActionUnion(BaseValidatorModel):
    pass


class RecipeStep(BaseValidatorModel):
    Action: RecipeActionUnion
    ConditionExpressions: Optional[Sequence[ConditionExpression]] = None


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


class ColumnStatisticsConfigurationOutput(BaseValidatorModel):
    Statistics: StatisticsConfigurationOutput
    Selectors: Optional[List[ColumnSelector]] = None


class ColumnStatisticsConfiguration(BaseValidatorModel):
    Statistics: StatisticsConfiguration
    Selectors: Optional[Sequence[ColumnSelector]] = None


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


class ListRecipeVersionsResponse(BaseValidatorModel):
    Recipes: List[Recipe]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRecipesResponse(BaseValidatorModel):
    Recipes: List[Recipe]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RuleUnion(BaseValidatorModel):
    pass


class CreateRulesetRequest(BaseValidatorModel):
    Name: str
    TargetArn: str
    Rules: Sequence[RuleUnion]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateRulesetRequest(BaseValidatorModel):
    Name: str
    Rules: Sequence[RuleUnion]
    Description: Optional[str] = None


class ProfileConfigurationOutput(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfigurationOutput] = None
    ProfileColumns: Optional[List[ColumnSelector]] = None
    ColumnStatisticsConfigurations: Optional[List[ColumnStatisticsConfigurationOutput]] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfigurationOutput] = None


class ProfileConfiguration(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfiguration] = None
    ProfileColumns: Optional[Sequence[ColumnSelector]] = None
    ColumnStatisticsConfigurations: Optional[Sequence[ColumnStatisticsConfiguration]] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfiguration] = None


class ListJobRunsResponse(BaseValidatorModel):
    JobRuns: List[JobRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Job(BaseValidatorModel):
    pass


class ListJobsResponse(BaseValidatorModel):
    Jobs: List[Job]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Union(BaseValidatorModel):
    pass


class CreateRecipeJobRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    DatasetName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[Sequence[Union]] = None
    DataCatalogOutputs: Optional[Sequence[DataCatalogOutput]] = None
    DatabaseOutputs: Optional[Sequence[DatabaseOutput]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReference] = None
    Tags: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None


class UpdateRecipeJobRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[Sequence[Union]] = None
    DataCatalogOutputs: Optional[Sequence[DataCatalogOutput]] = None
    DatabaseOutputs: Optional[Sequence[DatabaseOutput]] = None
    Timeout: Optional[int] = None


class ListDatasetsResponse(BaseValidatorModel):
    Datasets: List[Dataset]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FormatOptionsUnion(BaseValidatorModel):
    pass


class PathOptionsUnion(BaseValidatorModel):
    pass


class CreateDatasetRequest(BaseValidatorModel):
    Name: str
    Input: Input
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsUnion] = None
    PathOptions: Optional[PathOptionsUnion] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDatasetRequest(BaseValidatorModel):
    Name: str
    Input: Input
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsUnion] = None
    PathOptions: Optional[PathOptionsUnion] = None


class RecipeStepUnion(BaseValidatorModel):
    pass


class CreateRecipeRequest(BaseValidatorModel):
    Name: str
    Steps: Sequence[RecipeStepUnion]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class SendProjectSessionActionRequest(BaseValidatorModel):
    Name: str
    Preview: Optional[bool] = None
    RecipeStep: Optional[RecipeStepUnion] = None
    StepIndex: Optional[int] = None
    ClientSessionId: Optional[str] = None
    ViewFrame: Optional[ViewFrame] = None


class UpdateRecipeRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Steps: Optional[Sequence[RecipeStepUnion]] = None


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


class ProfileConfigurationUnion(BaseValidatorModel):
    pass


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
    ValidationConfigurations: Optional[Sequence[ValidationConfiguration]] = None
    Tags: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSample] = None


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
    ValidationConfigurations: Optional[Sequence[ValidationConfiguration]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSample] = None


