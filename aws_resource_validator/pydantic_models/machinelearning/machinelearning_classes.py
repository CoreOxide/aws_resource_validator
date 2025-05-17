from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.machinelearning.machinelearning_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchPrediction(BaseValidatorModel):
    BatchPredictionId: Optional[str] = None
    MLModelId: Optional[str] = None
    BatchPredictionDataSourceId: Optional[str] = None
    InputDataLocationS3: Optional[str] = None
    CreatedByIamUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[EntityStatusType] = None
    OutputUri: Optional[str] = None
    Message: Optional[str] = None
    ComputeTime: Optional[int] = None
    FinishedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None
    TotalRecordCount: Optional[int] = None
    InvalidRecordCount: Optional[int] = None


# This class is the input for the 'create_batch_prediction' function.
class CreateBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    OutputUri: str
    BatchPredictionName: Optional[str] = None


class S3DataSpec(BaseValidatorModel):
    DataLocationS3: str
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaLocationS3: Optional[str] = None


# This class is the input for the 'create_evaluation' function.
class CreateEvaluationInput(BaseValidatorModel):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    EvaluationName: Optional[str] = None


# This class is the input for the 'create_ml_model' function.
class CreateMLModelInput(BaseValidatorModel):
    MLModelId: str
    MLModelType: MLModelTypeType
    TrainingDataSourceId: str
    MLModelName: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    Recipe: Optional[str] = None
    RecipeUri: Optional[str] = None


# This class is the input for the 'create_realtime_endpoint' function.
class CreateRealtimeEndpointInput(BaseValidatorModel):
    MLModelId: str


class RealtimeEndpointInfo(BaseValidatorModel):
    PeakRequestsPerSecond: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    EndpointUrl: Optional[str] = None
    EndpointStatus: Optional[RealtimeEndpointStatusType] = None


# This class is the input for the 'delete_batch_prediction' function.
class DeleteBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str


# This class is the input for the 'delete_data_source' function.
class DeleteDataSourceInput(BaseValidatorModel):
    DataSourceId: str


# This class is the input for the 'delete_evaluation' function.
class DeleteEvaluationInput(BaseValidatorModel):
    EvaluationId: str


# This class is the input for the 'delete_ml_model' function.
class DeleteMLModelInput(BaseValidatorModel):
    MLModelId: str


# This class is the input for the 'delete_realtime_endpoint' function.
class DeleteRealtimeEndpointInput(BaseValidatorModel):
    MLModelId: str


# This class is the input for the 'delete_tags' function.
class DeleteTagsInput(BaseValidatorModel):
    TagKeys: List[str]
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_batch_predictions' function.
class DescribeBatchPredictionsInput(BaseValidatorModel):
    FilterVariable: Optional[BatchPredictionFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_data_sources' function.
class DescribeDataSourcesInput(BaseValidatorModel):
    FilterVariable: Optional[DataSourceFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_evaluations' function.
class DescribeEvaluationsInput(BaseValidatorModel):
    FilterVariable: Optional[EvaluationFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_ml_models' function.
class DescribeMLModelsInput(BaseValidatorModel):
    FilterVariable: Optional[MLModelFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsInput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class PerformanceMetrics(BaseValidatorModel):
    Properties: Optional[Dict[str, str]] = None


# This class is the input for the 'get_batch_prediction' function.
class GetBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str


# This class is the input for the 'get_data_source' function.
class GetDataSourceInput(BaseValidatorModel):
    DataSourceId: str
    Verbose: Optional[bool] = None


# This class is the input for the 'get_evaluation' function.
class GetEvaluationInput(BaseValidatorModel):
    EvaluationId: str


# This class is the input for the 'get_ml_model' function.
class GetMLModelInput(BaseValidatorModel):
    MLModelId: str
    Verbose: Optional[bool] = None


# This class is the input for the 'predict' function.
class PredictInput(BaseValidatorModel):
    MLModelId: str
    Record: Dict[str, str]
    PredictEndpoint: str


class Prediction(BaseValidatorModel):
    predictedLabel: Optional[str] = None
    predictedValue: Optional[float] = None
    predictedScores: Optional[Dict[str, float]] = None
    details: Optional[Dict[DetailsAttributesType, str]] = None


class RDSDatabaseCredentials(BaseValidatorModel):
    Username: str
    Password: str


class RDSDatabase(BaseValidatorModel):
    InstanceIdentifier: str
    DatabaseName: str


class RedshiftDatabaseCredentials(BaseValidatorModel):
    Username: str
    Password: str


class RedshiftDatabase(BaseValidatorModel):
    DatabaseName: str
    ClusterIdentifier: str


# This class is the input for the 'update_batch_prediction' function.
class UpdateBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str
    BatchPredictionName: str


# This class is the input for the 'update_data_source' function.
class UpdateDataSourceInput(BaseValidatorModel):
    DataSourceId: str
    DataSourceName: str


# This class is the input for the 'update_evaluation' function.
class UpdateEvaluationInput(BaseValidatorModel):
    EvaluationId: str
    EvaluationName: str


# This class is the input for the 'update_ml_model' function.
class UpdateMLModelInput(BaseValidatorModel):
    MLModelId: str
    MLModelName: Optional[str] = None
    ScoreThreshold: Optional[float] = None


# This class is the input for the 'add_tags' function.
class AddTagsInput(BaseValidatorModel):
    Tags: List[Tag]
    ResourceId: str
    ResourceType: TaggableResourceTypeType


# This class is the output for the 'add_tags' function.
class AddTagsOutput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_batch_prediction' function.
class CreateBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_source_from_rds' function.
class CreateDataSourceFromRDSOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_source_from_redshift' function.
class CreateDataSourceFromRedshiftOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_source_from_s3' function.
class CreateDataSourceFromS3Output(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_evaluation' function.
class CreateEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ml_model' function.
class CreateMLModelOutput(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_batch_prediction' function.
class DeleteBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_source' function.
class DeleteDataSourceOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_evaluation' function.
class DeleteEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ml_model' function.
class DeleteMLModelOutput(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_tags' function.
class DeleteTagsOutput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tags' function.
class DescribeTagsOutput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_batch_prediction' function.
class GetBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    OutputUri: str
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    TotalRecordCount: int
    InvalidRecordCount: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_batch_prediction' function.
class UpdateBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_data_source' function.
class UpdateDataSourceOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_evaluation' function.
class UpdateEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ml_model' function.
class UpdateMLModelOutput(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_batch_predictions' function.
class DescribeBatchPredictionsOutput(BaseValidatorModel):
    Results: List[BatchPrediction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_data_source_from_s3' function.
class CreateDataSourceFromS3Input(BaseValidatorModel):
    DataSourceId: str
    DataSpec: S3DataSpec
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


# This class is the output for the 'create_realtime_endpoint' function.
class CreateRealtimeEndpointOutput(BaseValidatorModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_realtime_endpoint' function.
class DeleteRealtimeEndpointOutput(BaseValidatorModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ml_model' function.
class GetMLModelOutput(BaseValidatorModel):
    MLModelId: str
    TrainingDataSourceId: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    SizeInBytes: int
    EndpointInfo: RealtimeEndpointInfo
    TrainingParameters: Dict[str, str]
    InputDataLocationS3: str
    MLModelType: MLModelTypeType
    ScoreThreshold: float
    ScoreThresholdLastUpdatedAt: datetime
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    Recipe: str
    Schema: str
    ResponseMetadata: ResponseMetadata


class MLModel(BaseValidatorModel):
    MLModelId: Optional[str] = None
    TrainingDataSourceId: Optional[str] = None
    CreatedByIamUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[EntityStatusType] = None
    SizeInBytes: Optional[int] = None
    EndpointInfo: Optional[RealtimeEndpointInfo] = None
    TrainingParameters: Optional[Dict[str, str]] = None
    InputDataLocationS3: Optional[str] = None
    Algorithm: Optional[Literal['sgd']] = None
    MLModelType: Optional[MLModelTypeType] = None
    ScoreThreshold: Optional[float] = None
    ScoreThresholdLastUpdatedAt: Optional[datetime] = None
    Message: Optional[str] = None
    ComputeTime: Optional[int] = None
    FinishedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None


class DescribeBatchPredictionsInputPaginate(BaseValidatorModel):
    FilterVariable: Optional[BatchPredictionFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSourcesInputPaginate(BaseValidatorModel):
    FilterVariable: Optional[DataSourceFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEvaluationsInputPaginate(BaseValidatorModel):
    FilterVariable: Optional[EvaluationFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMLModelsInputPaginate(BaseValidatorModel):
    FilterVariable: Optional[MLModelFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBatchPredictionsInputWait(BaseValidatorModel):
    FilterVariable: Optional[BatchPredictionFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDataSourcesInputWait(BaseValidatorModel):
    FilterVariable: Optional[DataSourceFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEvaluationsInputWait(BaseValidatorModel):
    FilterVariable: Optional[EvaluationFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeMLModelsInputWait(BaseValidatorModel):
    FilterVariable: Optional[MLModelFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class Evaluation(BaseValidatorModel):
    EvaluationId: Optional[str] = None
    MLModelId: Optional[str] = None
    EvaluationDataSourceId: Optional[str] = None
    InputDataLocationS3: Optional[str] = None
    CreatedByIamUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[EntityStatusType] = None
    PerformanceMetrics: Optional[PerformanceMetrics] = None
    Message: Optional[str] = None
    ComputeTime: Optional[int] = None
    FinishedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None


# This class is the output for the 'get_evaluation' function.
class GetEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    PerformanceMetrics: PerformanceMetrics
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'predict' function.
class PredictOutput(BaseValidatorModel):
    Prediction: Prediction
    ResponseMetadata: ResponseMetadata


class RDSDataSpec(BaseValidatorModel):
    DatabaseInformation: RDSDatabase
    SelectSqlQuery: str
    DatabaseCredentials: RDSDatabaseCredentials
    S3StagingLocation: str
    ResourceRole: str
    ServiceRole: str
    SubnetId: str
    SecurityGroupIds: List[str]
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaUri: Optional[str] = None


class RDSMetadata(BaseValidatorModel):
    Database: Optional[RDSDatabase] = None
    DatabaseUserName: Optional[str] = None
    SelectSqlQuery: Optional[str] = None
    ResourceRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    DataPipelineId: Optional[str] = None


class RedshiftDataSpec(BaseValidatorModel):
    DatabaseInformation: RedshiftDatabase
    SelectSqlQuery: str
    DatabaseCredentials: RedshiftDatabaseCredentials
    S3StagingLocation: str
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaUri: Optional[str] = None


class RedshiftMetadata(BaseValidatorModel):
    RedshiftDatabase: Optional[RedshiftDatabase] = None
    DatabaseUserName: Optional[str] = None
    SelectSqlQuery: Optional[str] = None


# This class is the output for the 'describe_ml_models' function.
class DescribeMLModelsOutput(BaseValidatorModel):
    Results: List[MLModel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_evaluations' function.
class DescribeEvaluationsOutput(BaseValidatorModel):
    Results: List[Evaluation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_data_source_from_rds' function.
class CreateDataSourceFromRDSInput(BaseValidatorModel):
    DataSourceId: str
    RDSData: RDSDataSpec
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


# This class is the input for the 'create_data_source_from_redshift' function.
class CreateDataSourceFromRedshiftInput(BaseValidatorModel):
    DataSourceId: str
    DataSpec: RedshiftDataSpec
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


class DataSource(BaseValidatorModel):
    DataSourceId: Optional[str] = None
    DataLocationS3: Optional[str] = None
    DataRearrangement: Optional[str] = None
    CreatedByIamUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    DataSizeInBytes: Optional[int] = None
    NumberOfFiles: Optional[int] = None
    Name: Optional[str] = None
    Status: Optional[EntityStatusType] = None
    Message: Optional[str] = None
    RedshiftMetadata: Optional[RedshiftMetadata] = None
    RDSMetadata: Optional[RDSMetadata] = None
    RoleARN: Optional[str] = None
    ComputeStatistics: Optional[bool] = None
    ComputeTime: Optional[int] = None
    FinishedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None


# This class is the output for the 'get_data_source' function.
class GetDataSourceOutput(BaseValidatorModel):
    DataSourceId: str
    DataLocationS3: str
    DataRearrangement: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    DataSizeInBytes: int
    NumberOfFiles: int
    Name: str
    Status: EntityStatusType
    LogUri: str
    Message: str
    RedshiftMetadata: RedshiftMetadata
    RDSMetadata: RDSMetadata
    RoleARN: str
    ComputeStatistics: bool
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    DataSourceSchema: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_sources' function.
class DescribeDataSourcesOutput(BaseValidatorModel):
    Results: List[DataSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None