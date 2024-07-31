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
from aws_resource_validator.pydantic_models.databrew_constants import *

class AllowedStatisticsTypeDef(BaseModel):
    Statistics: Sequence[str]

class BatchDeleteRecipeVersionRequestRequestTypeDef(BaseModel):
    Name: str
    RecipeVersions: Sequence[str]

class RecipeVersionErrorDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    RecipeVersion: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ColumnSelectorTypeDef(BaseModel):
    Regex: Optional[str] = None
    Name: Optional[str] = None

class ConditionExpressionTypeDef(BaseModel):
    Condition: str
    TargetColumn: str
    Value: Optional[str] = None

class JobSampleTypeDef(BaseModel):
    Mode: Optional[SampleModeType] = None
    Size: Optional[int] = None

class S3LocationTypeDef(BaseModel):
    Bucket: str
    Key: Optional[str] = None
    BucketOwner: Optional[str] = None

class ValidationConfigurationTypeDef(BaseModel):
    RulesetArn: str
    ValidationMode: Optional[Literal["CHECK_ALL"]] = None

class SampleTypeDef(BaseModel):
    Type: SampleTypeType
    Size: Optional[int] = None

class RecipeReferenceTypeDef(BaseModel):
    Name: str
    RecipeVersion: Optional[str] = None

class CreateScheduleRequestRequestTypeDef(BaseModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class CsvOptionsTypeDef(BaseModel):
    Delimiter: Optional[str] = None
    HeaderRow: Optional[bool] = None

class CsvOutputOptionsTypeDef(BaseModel):
    Delimiter: Optional[str] = None

class DatetimeOptionsTypeDef(BaseModel):
    Format: str
    TimezoneOffset: Optional[str] = None
    LocaleCode: Optional[str] = None

class FilterExpressionPaginatorTypeDef(BaseModel):
    Expression: str
    ValuesMap: Dict[str, str]

class FilterExpressionTypeDef(BaseModel):
    Expression: str
    ValuesMap: Mapping[str, str]

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteJobRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteProjectRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteRecipeVersionRequestRequestTypeDef(BaseModel):
    Name: str
    RecipeVersion: str

class DeleteRulesetRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteScheduleRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeJobRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeJobRunRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str

class DescribeProjectRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeRecipeRequestRequestTypeDef(BaseModel):
    Name: str
    RecipeVersion: Optional[str] = None

class DescribeRulesetRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeScheduleRequestRequestTypeDef(BaseModel):
    Name: str

class ExcelOptionsPaginatorTypeDef(BaseModel):
    SheetNames: Optional[List[str]] = None
    SheetIndexes: Optional[List[int]] = None
    HeaderRow: Optional[bool] = None

class ExcelOptionsTypeDef(BaseModel):
    SheetNames: Optional[Sequence[str]] = None
    SheetIndexes: Optional[Sequence[int]] = None
    HeaderRow: Optional[bool] = None

class FilesLimitTypeDef(BaseModel):
    MaxFiles: int
    OrderedBy: Optional[Literal["LAST_MODIFIED_DATE"]] = None
    Order: Optional[OrderType] = None

class JsonOptionsTypeDef(BaseModel):
    MultiLine: Optional[bool] = None

class MetadataTypeDef(BaseModel):
    SourceArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobRunsRequestRequestTypeDef(BaseModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    DatasetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProjectName: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRecipeVersionsRequestRequestTypeDef(BaseModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRecipesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RecipeVersion: Optional[str] = None

class ListRulesetsRequestRequestTypeDef(BaseModel):
    TargetArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RulesetItemTypeDef(BaseModel):
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

class ListSchedulesRequestRequestTypeDef(BaseModel):
    JobName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ScheduleTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PublishRecipeRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None

class RecipeActionPaginatorTypeDef(BaseModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None

class RecipeActionTypeDef(BaseModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None

class ThresholdTypeDef(BaseModel):
    Value: float
    Type: Optional[ThresholdTypeType] = None
    Unit: Optional[ThresholdUnitType] = None

class ViewFrameTypeDef(BaseModel):
    StartColumnIndex: int
    ColumnRange: Optional[int] = None
    HiddenColumns: Optional[Sequence[str]] = None
    StartRowIndex: Optional[int] = None
    RowRange: Optional[int] = None
    Analytics: Optional[AnalyticsModeType] = None

class StartJobRunRequestRequestTypeDef(BaseModel):
    Name: str

class StartProjectSessionRequestRequestTypeDef(BaseModel):
    Name: str
    AssumeControl: Optional[bool] = None

class StatisticOverrideTypeDef(BaseModel):
    Statistic: str
    Parameters: Mapping[str, str]

class StopJobRunRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateScheduleRequestRequestTypeDef(BaseModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None

class EntityDetectorConfigurationTypeDef(BaseModel):
    EntityTypes: Sequence[str]
    AllowedStatistics: Optional[Sequence[AllowedStatisticsTypeDef]] = None

class BatchDeleteRecipeVersionResponseTypeDef(BaseModel):
    Name: str
    Errors: List[RecipeVersionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileJobResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecipeJobResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecipeResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRulesetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduleResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatasetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRecipeVersionResponseTypeDef(BaseModel):
    Name: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRulesetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScheduleResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScheduleResponseTypeDef(BaseModel):
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishRecipeResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendProjectSessionActionResponseTypeDef(BaseModel):
    Result: str
    Name: str
    ActionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(BaseModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartProjectSessionResponseTypeDef(BaseModel):
    Name: str
    ClientSessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopJobRunResponseTypeDef(BaseModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileJobResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResponseTypeDef(BaseModel):
    LastModifiedDate: datetime
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecipeJobResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecipeResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRulesetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduleResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataCatalogInputDefinitionTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    TempDirectory: Optional[S3LocationTypeDef] = None

class DatabaseInputDefinitionTypeDef(BaseModel):
    GlueConnectionName: str
    DatabaseTableName: Optional[str] = None
    TempDirectory: Optional[S3LocationTypeDef] = None
    QueryString: Optional[str] = None

class DatabaseTableOutputOptionsTypeDef(BaseModel):
    TableName: str
    TempDirectory: Optional[S3LocationTypeDef] = None

class S3TableOutputOptionsTypeDef(BaseModel):
    Location: S3LocationTypeDef

class CreateProjectRequestRequestTypeDef(BaseModel):
    DatasetName: str
    Name: str
    RecipeName: str
    RoleArn: str
    Sample: Optional[SampleTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class DescribeProjectResponseTypeDef(BaseModel):
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

class ProjectTypeDef(BaseModel):
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

class UpdateProjectRequestRequestTypeDef(BaseModel):
    RoleArn: str
    Name: str
    Sample: Optional[SampleTypeDef] = None

class OutputFormatOptionsTypeDef(BaseModel):
    Csv: Optional[CsvOutputOptionsTypeDef] = None

class DatasetParameterPaginatorTypeDef(BaseModel):
    Name: str
    Type: ParameterTypeType
    DatetimeOptions: Optional[DatetimeOptionsTypeDef] = None
    CreateColumn: Optional[bool] = None
    Filter: Optional[FilterExpressionPaginatorTypeDef] = None

class DatasetParameterTypeDef(BaseModel):
    Name: str
    Type: ParameterTypeType
    DatetimeOptions: Optional[DatetimeOptionsTypeDef] = None
    CreateColumn: Optional[bool] = None
    Filter: Optional[FilterExpressionTypeDef] = None

class FormatOptionsPaginatorTypeDef(BaseModel):
    Json: Optional[JsonOptionsTypeDef] = None
    Excel: Optional[ExcelOptionsPaginatorTypeDef] = None
    Csv: Optional[CsvOptionsTypeDef] = None

class FormatOptionsTypeDef(BaseModel):
    Json: Optional[JsonOptionsTypeDef] = None
    Excel: Optional[ExcelOptionsTypeDef] = None
    Csv: Optional[CsvOptionsTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestListJobRunsPaginateTypeDef(BaseModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    DatasetName: Optional[str] = None
    ProjectName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef(BaseModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecipesRequestListRecipesPaginateTypeDef(BaseModel):
    RecipeVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesetsRequestListRulesetsPaginateTypeDef(BaseModel):
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchedulesRequestListSchedulesPaginateTypeDef(BaseModel):
    JobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesetsResponseTypeDef(BaseModel):
    Rulesets: List[RulesetItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchedulesResponseTypeDef(BaseModel):
    Schedules: List[ScheduleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecipeStepPaginatorTypeDef(BaseModel):
    Action: RecipeActionPaginatorTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None

class RecipeStepTypeDef(BaseModel):
    Action: RecipeActionTypeDef
    ConditionExpressions: Optional[Sequence[ConditionExpressionTypeDef]] = None

class RuleTypeDef(BaseModel):
    Name: str
    CheckExpression: str
    Disabled: Optional[bool] = None
    SubstitutionMap: Optional[Mapping[str, str]] = None
    Threshold: Optional[ThresholdTypeDef] = None
    ColumnSelectors: Optional[Sequence[ColumnSelectorTypeDef]] = None

class StatisticsConfigurationTypeDef(BaseModel):
    IncludedStatistics: Optional[Sequence[str]] = None
    Overrides: Optional[Sequence[StatisticOverrideTypeDef]] = None

class InputTypeDef(BaseModel):
    S3InputDefinition: Optional[S3LocationTypeDef] = None
    DataCatalogInputDefinition: Optional[DataCatalogInputDefinitionTypeDef] = None
    DatabaseInputDefinition: Optional[DatabaseInputDefinitionTypeDef] = None
    Metadata: Optional[MetadataTypeDef] = None

class DatabaseOutputTypeDef(BaseModel):
    GlueConnectionName: str
    DatabaseOptions: DatabaseTableOutputOptionsTypeDef
    DatabaseOutputMode: Optional[Literal["NEW_TABLE"]] = None

class DataCatalogOutputTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    S3Options: Optional[S3TableOutputOptionsTypeDef] = None
    DatabaseOptions: Optional[DatabaseTableOutputOptionsTypeDef] = None
    Overwrite: Optional[bool] = None

class ListProjectsResponseTypeDef(BaseModel):
    Projects: List[ProjectTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OutputPaginatorTypeDef(BaseModel):
    Location: S3LocationTypeDef
    CompressionFormat: Optional[CompressionFormatType] = None
    Format: Optional[OutputFormatType] = None
    PartitionColumns: Optional[List[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptionsTypeDef] = None
    MaxOutputFiles: Optional[int] = None

class OutputTypeDef(BaseModel):
    Location: S3LocationTypeDef
    CompressionFormat: Optional[CompressionFormatType] = None
    Format: Optional[OutputFormatType] = None
    PartitionColumns: Optional[Sequence[str]] = None
    Overwrite: Optional[bool] = None
    FormatOptions: Optional[OutputFormatOptionsTypeDef] = None
    MaxOutputFiles: Optional[int] = None

class PathOptionsPaginatorTypeDef(BaseModel):
    LastModifiedDateCondition: Optional[FilterExpressionPaginatorTypeDef] = None
    FilesLimit: Optional[FilesLimitTypeDef] = None
    Parameters: Optional[Dict[str, DatasetParameterPaginatorTypeDef]] = None

class PathOptionsTypeDef(BaseModel):
    LastModifiedDateCondition: Optional[FilterExpressionTypeDef] = None
    FilesLimit: Optional[FilesLimitTypeDef] = None
    Parameters: Optional[Mapping[str, DatasetParameterTypeDef]] = None

class RecipePaginatorTypeDef(BaseModel):
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
    Steps: Optional[List[RecipeStepPaginatorTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None
    RecipeVersion: Optional[str] = None

class CreateRecipeRequestRequestTypeDef(BaseModel):
    Name: str
    Steps: Sequence[RecipeStepTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class DescribeRecipeResponseTypeDef(BaseModel):
    CreatedBy: str
    CreateDate: datetime
    LastModifiedBy: str
    LastModifiedDate: datetime
    ProjectName: str
    PublishedBy: str
    PublishedDate: datetime
    Description: str
    Name: str
    Steps: List[RecipeStepTypeDef]
    Tags: Dict[str, str]
    ResourceArn: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecipeTypeDef(BaseModel):
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
    Steps: Optional[List[RecipeStepTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None
    RecipeVersion: Optional[str] = None

class SendProjectSessionActionRequestRequestTypeDef(BaseModel):
    Name: str
    Preview: Optional[bool] = None
    RecipeStep: Optional[RecipeStepTypeDef] = None
    StepIndex: Optional[int] = None
    ClientSessionId: Optional[str] = None
    ViewFrame: Optional[ViewFrameTypeDef] = None

class UpdateRecipeRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    Steps: Optional[Sequence[RecipeStepTypeDef]] = None

class CreateRulesetRequestRequestTypeDef(BaseModel):
    Name: str
    TargetArn: str
    Rules: Sequence[RuleTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class DescribeRulesetResponseTypeDef(BaseModel):
    Name: str
    Description: str
    TargetArn: str
    Rules: List[RuleTypeDef]
    CreateDate: datetime
    CreatedBy: str
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRulesetRequestRequestTypeDef(BaseModel):
    Name: str
    Rules: Sequence[RuleTypeDef]
    Description: Optional[str] = None

class ColumnStatisticsConfigurationTypeDef(BaseModel):
    Statistics: StatisticsConfigurationTypeDef
    Selectors: Optional[Sequence[ColumnSelectorTypeDef]] = None

class JobPaginatorTypeDef(BaseModel):
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
    Outputs: Optional[List[OutputPaginatorTypeDef]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[List[DatabaseOutputTypeDef]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    Timeout: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    JobSample: Optional[JobSampleTypeDef] = None
    ValidationConfigurations: Optional[List[ValidationConfigurationTypeDef]] = None

class JobRunPaginatorTypeDef(BaseModel):
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
    Outputs: Optional[List[OutputPaginatorTypeDef]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[List[DatabaseOutputTypeDef]] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    StartedBy: Optional[str] = None
    StartedOn: Optional[datetime] = None
    JobSample: Optional[JobSampleTypeDef] = None
    ValidationConfigurations: Optional[List[ValidationConfigurationTypeDef]] = None

class CreateRecipeJobRequestRequestTypeDef(BaseModel):
    Name: str
    RoleArn: str
    DatasetName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None
    DataCatalogOutputs: Optional[Sequence[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[Sequence[DatabaseOutputTypeDef]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None

class JobRunTypeDef(BaseModel):
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
    Outputs: Optional[List[OutputTypeDef]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[List[DatabaseOutputTypeDef]] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    StartedBy: Optional[str] = None
    StartedOn: Optional[datetime] = None
    JobSample: Optional[JobSampleTypeDef] = None
    ValidationConfigurations: Optional[List[ValidationConfigurationTypeDef]] = None

class JobTypeDef(BaseModel):
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
    Outputs: Optional[List[OutputTypeDef]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[List[DatabaseOutputTypeDef]] = None
    ProjectName: Optional[str] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    Timeout: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    JobSample: Optional[JobSampleTypeDef] = None
    ValidationConfigurations: Optional[List[ValidationConfigurationTypeDef]] = None

class UpdateRecipeJobRequestRequestTypeDef(BaseModel):
    Name: str
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None
    DataCatalogOutputs: Optional[Sequence[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[Sequence[DatabaseOutputTypeDef]] = None
    Timeout: Optional[int] = None

class DatasetPaginatorTypeDef(BaseModel):
    Name: str
    Input: InputTypeDef
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsPaginatorTypeDef] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    Source: Optional[SourceType] = None
    PathOptions: Optional[PathOptionsPaginatorTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    ResourceArn: Optional[str] = None

class CreateDatasetRequestRequestTypeDef(BaseModel):
    Name: str
    Input: InputTypeDef
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsTypeDef] = None
    PathOptions: Optional[PathOptionsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class DatasetTypeDef(BaseModel):
    Name: str
    Input: InputTypeDef
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreateDate: Optional[datetime] = None
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsTypeDef] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    Source: Optional[SourceType] = None
    PathOptions: Optional[PathOptionsTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    ResourceArn: Optional[str] = None

class DescribeDatasetResponseTypeDef(BaseModel):
    CreatedBy: str
    CreateDate: datetime
    Name: str
    Format: InputFormatType
    FormatOptions: FormatOptionsTypeDef
    Input: InputTypeDef
    LastModifiedDate: datetime
    LastModifiedBy: str
    Source: SourceType
    PathOptions: PathOptionsTypeDef
    Tags: Dict[str, str]
    ResourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetRequestRequestTypeDef(BaseModel):
    Name: str
    Input: InputTypeDef
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsTypeDef] = None
    PathOptions: Optional[PathOptionsTypeDef] = None

class ListRecipeVersionsResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    Recipes: List[RecipePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipesResponsePaginatorTypeDef(BaseModel):
    Recipes: List[RecipePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipeVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Recipes: List[RecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipesResponseTypeDef(BaseModel):
    Recipes: List[RecipeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProfileConfigurationTypeDef(BaseModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfigurationTypeDef] = None
    ProfileColumns: Optional[Sequence[ColumnSelectorTypeDef]] = None
    ColumnStatisticsConfigurations: Optional[       Sequence[ColumnStatisticsConfigurationTypeDef]     ] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfigurationTypeDef] = None

class ListJobsResponsePaginatorTypeDef(BaseModel):
    Jobs: List[JobPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponsePaginatorTypeDef(BaseModel):
    JobRuns: List[JobRunPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(BaseModel):
    JobRuns: List[JobRunTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponsePaginatorTypeDef(BaseModel):
    Datasets: List[DatasetPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseModel):
    Datasets: List[DatasetTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileJobRequestRequestTypeDef(BaseModel):
    DatasetName: str
    Name: str
    OutputLocation: S3LocationTypeDef
    RoleArn: str
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    Configuration: Optional[ProfileConfigurationTypeDef] = None
    ValidationConfigurations: Optional[Sequence[ValidationConfigurationTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSampleTypeDef] = None

class DescribeJobResponseTypeDef(BaseModel):
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
    Outputs: List[OutputTypeDef]
    DataCatalogOutputs: List[DataCatalogOutputTypeDef]
    DatabaseOutputs: List[DatabaseOutputTypeDef]
    ProjectName: str
    ProfileConfiguration: ProfileConfigurationTypeDef
    ValidationConfigurations: List[ValidationConfigurationTypeDef]
    RecipeReference: RecipeReferenceTypeDef
    ResourceArn: str
    RoleArn: str
    Tags: Dict[str, str]
    Timeout: int
    JobSample: JobSampleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobRunResponseTypeDef(BaseModel):
    Attempt: int
    CompletedOn: datetime
    DatasetName: str
    ErrorMessage: str
    ExecutionTime: int
    JobName: str
    ProfileConfiguration: ProfileConfigurationTypeDef
    ValidationConfigurations: List[ValidationConfigurationTypeDef]
    RunId: str
    State: JobRunStateType
    LogSubscription: LogSubscriptionType
    LogGroupName: str
    Outputs: List[OutputTypeDef]
    DataCatalogOutputs: List[DataCatalogOutputTypeDef]
    DatabaseOutputs: List[DatabaseOutputTypeDef]
    RecipeReference: RecipeReferenceTypeDef
    StartedBy: str
    StartedOn: datetime
    JobSample: JobSampleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileJobRequestRequestTypeDef(BaseModel):
    Name: str
    OutputLocation: S3LocationTypeDef
    RoleArn: str
    Configuration: Optional[ProfileConfigurationTypeDef] = None
    EncryptionKeyArn: Optional[str] = None
    EncryptionMode: Optional[EncryptionModeType] = None
    LogSubscription: Optional[LogSubscriptionType] = None
    MaxCapacity: Optional[int] = None
    MaxRetries: Optional[int] = None
    ValidationConfigurations: Optional[Sequence[ValidationConfigurationTypeDef]] = None
    Timeout: Optional[int] = None
    JobSample: Optional[JobSampleTypeDef] = None

