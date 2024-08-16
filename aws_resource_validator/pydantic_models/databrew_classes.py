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
from aws_resource_validator.pydantic_models.databrew_constants import *

class AllowedStatisticsTypeDef(BaseValidatorModel):
    Statistics: Sequence[str]

class BatchDeleteRecipeVersionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersions: Sequence[str]

class RecipeVersionErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    RecipeVersion: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class SampleTypeDef(BaseValidatorModel):
    Type: SampleTypeType
    Size: Optional[int] = None

class RecipeReferenceTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None

class CreateScheduleRequestRequestTypeDef(BaseValidatorModel):
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

class FilterExpressionPaginatorTypeDef(BaseValidatorModel):
    Expression: str
    ValuesMap: Dict[str, str]

class FilterExpressionTypeDef(BaseValidatorModel):
    Expression: str
    ValuesMap: Mapping[str, str]

class DeleteDatasetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteJobRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteRecipeVersionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: str

class DeleteRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteScheduleRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeDatasetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeJobRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeJobRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str

class DescribeProjectRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeRecipeRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RecipeVersion: Optional[str] = None

class DescribeRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeScheduleRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class ExcelOptionsPaginatorTypeDef(BaseValidatorModel):
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

class ListDatasetsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobRunsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseValidatorModel):
    DatasetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProjectName: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRecipeVersionsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRecipesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RecipeVersion: Optional[str] = None

class ListRulesetsRequestRequestTypeDef(BaseValidatorModel):
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

class ListSchedulesRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PublishRecipeRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None

class RecipeActionPaginatorTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None

class RecipeActionTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None

class ThresholdTypeDef(BaseValidatorModel):
    Value: float
    Type: Optional[ThresholdTypeType] = None
    Unit: Optional[ThresholdUnitType] = None

class ViewFrameTypeDef(BaseValidatorModel):
    StartColumnIndex: int
    ColumnRange: Optional[int] = None
    HiddenColumns: Optional[Sequence[str]] = None
    StartRowIndex: Optional[int] = None
    RowRange: Optional[int] = None
    Analytics: Optional[AnalyticsModeType] = None

class StartJobRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartProjectSessionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    AssumeControl: Optional[bool] = None

class StatisticOverrideTypeDef(BaseValidatorModel):
    Statistic: str
    Parameters: Mapping[str, str]

class StopJobRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateScheduleRequestRequestTypeDef(BaseValidatorModel):
    CronExpression: str
    Name: str
    JobNames: Optional[Sequence[str]] = None

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

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    Name: str
    Sample: Optional[SampleTypeDef] = None

class OutputFormatOptionsTypeDef(BaseValidatorModel):
    Csv: Optional[CsvOutputOptionsTypeDef] = None

class DatasetParameterPaginatorTypeDef(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    DatetimeOptions: Optional[DatetimeOptionsTypeDef] = None
    CreateColumn: Optional[bool] = None
    Filter: Optional[FilterExpressionPaginatorTypeDef] = None

class DatasetParameterTypeDef(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    DatetimeOptions: Optional[DatetimeOptionsTypeDef] = None
    CreateColumn: Optional[bool] = None
    Filter: Optional[FilterExpressionTypeDef] = None

class FormatOptionsPaginatorTypeDef(BaseValidatorModel):
    Json: Optional[JsonOptionsTypeDef] = None
    Excel: Optional[ExcelOptionsPaginatorTypeDef] = None
    Csv: Optional[CsvOptionsTypeDef] = None

class FormatOptionsTypeDef(BaseValidatorModel):
    Json: Optional[JsonOptionsTypeDef] = None
    Excel: Optional[ExcelOptionsTypeDef] = None
    Csv: Optional[CsvOptionsTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestListJobRunsPaginateTypeDef(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseValidatorModel):
    DatasetName: Optional[str] = None
    ProjectName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecipesRequestListRecipesPaginateTypeDef(BaseValidatorModel):
    RecipeVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesetsRequestListRulesetsPaginateTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchedulesRequestListSchedulesPaginateTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesetsResponseTypeDef(BaseValidatorModel):
    Rulesets: List[RulesetItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchedulesResponseTypeDef(BaseValidatorModel):
    Schedules: List[ScheduleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecipeStepPaginatorTypeDef(BaseValidatorModel):
    Action: RecipeActionPaginatorTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None

class RecipeStepTypeDef(BaseValidatorModel):
    Action: RecipeActionTypeDef
    ConditionExpressions: Optional[Sequence[ConditionExpressionTypeDef]] = None

class RuleTypeDef(BaseValidatorModel):
    Name: str
    CheckExpression: str
    Disabled: Optional[bool] = None
    SubstitutionMap: Optional[Mapping[str, str]] = None
    Threshold: Optional[ThresholdTypeDef] = None
    ColumnSelectors: Optional[Sequence[ColumnSelectorTypeDef]] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OutputPaginatorTypeDef(BaseValidatorModel):
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

class PathOptionsPaginatorTypeDef(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpressionPaginatorTypeDef] = None
    FilesLimit: Optional[FilesLimitTypeDef] = None
    Parameters: Optional[Dict[str, DatasetParameterPaginatorTypeDef]] = None

class PathOptionsTypeDef(BaseValidatorModel):
    LastModifiedDateCondition: Optional[FilterExpressionTypeDef] = None
    FilesLimit: Optional[FilesLimitTypeDef] = None
    Parameters: Optional[Mapping[str, DatasetParameterTypeDef]] = None

class RecipePaginatorTypeDef(BaseValidatorModel):
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

class CreateRecipeRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Steps: Sequence[RecipeStepTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

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
    Steps: List[RecipeStepTypeDef]
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
    Steps: Optional[List[RecipeStepTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None
    RecipeVersion: Optional[str] = None

class SendProjectSessionActionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Preview: Optional[bool] = None
    RecipeStep: Optional[RecipeStepTypeDef] = None
    StepIndex: Optional[int] = None
    ClientSessionId: Optional[str] = None
    ViewFrame: Optional[ViewFrameTypeDef] = None

class UpdateRecipeRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Steps: Optional[Sequence[RecipeStepTypeDef]] = None

class CreateRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    TargetArn: str
    Rules: Sequence[RuleTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class DescribeRulesetResponseTypeDef(BaseValidatorModel):
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

class UpdateRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Rules: Sequence[RuleTypeDef]
    Description: Optional[str] = None

class ColumnStatisticsConfigurationTypeDef(BaseValidatorModel):
    Statistics: StatisticsConfigurationTypeDef
    Selectors: Optional[Sequence[ColumnSelectorTypeDef]] = None

class JobPaginatorTypeDef(BaseValidatorModel):
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

class JobRunPaginatorTypeDef(BaseValidatorModel):
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

class CreateRecipeJobRequestRequestTypeDef(BaseValidatorModel):
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
    Outputs: Optional[List[OutputTypeDef]] = None
    DataCatalogOutputs: Optional[List[DataCatalogOutputTypeDef]] = None
    DatabaseOutputs: Optional[List[DatabaseOutputTypeDef]] = None
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    StartedBy: Optional[str] = None
    StartedOn: Optional[datetime] = None
    JobSample: Optional[JobSampleTypeDef] = None
    ValidationConfigurations: Optional[List[ValidationConfigurationTypeDef]] = None

class JobTypeDef(BaseValidatorModel):
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

class UpdateRecipeJobRequestRequestTypeDef(BaseValidatorModel):
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

class DatasetPaginatorTypeDef(BaseValidatorModel):
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

class CreateDatasetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Input: InputTypeDef
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsTypeDef] = None
    PathOptions: Optional[PathOptionsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class DatasetTypeDef(BaseValidatorModel):
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

class DescribeDatasetResponseTypeDef(BaseValidatorModel):
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

class UpdateDatasetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Input: InputTypeDef
    Format: Optional[InputFormatType] = None
    FormatOptions: Optional[FormatOptionsTypeDef] = None
    PathOptions: Optional[PathOptionsTypeDef] = None

class ListRecipeVersionsResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    Recipes: List[RecipePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipesResponsePaginatorTypeDef(BaseValidatorModel):
    Recipes: List[RecipePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipeVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Recipes: List[RecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipesResponseTypeDef(BaseValidatorModel):
    Recipes: List[RecipeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProfileConfigurationTypeDef(BaseValidatorModel):
    DatasetStatisticsConfiguration: Optional[StatisticsConfigurationTypeDef] = None
    ProfileColumns: Optional[Sequence[ColumnSelectorTypeDef]] = None
    ColumnStatisticsConfigurations: Optional[       Sequence[ColumnStatisticsConfigurationTypeDef]     ] = None
    EntityDetectorConfiguration: Optional[EntityDetectorConfigurationTypeDef] = None

class ListJobsResponsePaginatorTypeDef(BaseValidatorModel):
    Jobs: List[JobPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponsePaginatorTypeDef(BaseValidatorModel):
    JobRuns: List[JobRunPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(BaseValidatorModel):
    JobRuns: List[JobRunTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponsePaginatorTypeDef(BaseValidatorModel):
    Datasets: List[DatasetPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseValidatorModel):
    Datasets: List[DatasetTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileJobRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeJobResponseTypeDef(BaseValidatorModel):
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

class DescribeJobRunResponseTypeDef(BaseValidatorModel):
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

class UpdateProfileJobRequestRequestTypeDef(BaseValidatorModel):
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

