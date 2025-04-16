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
from aws_resource_validator.pydantic_models.machinelearning_constants import *

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


class CreateEvaluationInput(BaseValidatorModel):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    EvaluationName: Optional[str] = None


class CreateMLModelInput(BaseValidatorModel):
    MLModelId: str
    MLModelType: MLModelTypeType
    TrainingDataSourceId: str
    MLModelName: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    Recipe: Optional[str] = None
    RecipeUri: Optional[str] = None


class CreateRealtimeEndpointInput(BaseValidatorModel):
    MLModelId: str


class RealtimeEndpointInfo(BaseValidatorModel):
    PeakRequestsPerSecond: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    EndpointUrl: Optional[str] = None
    EndpointStatus: Optional[RealtimeEndpointStatusType] = None


class DeleteBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str


class DeleteDataSourceInput(BaseValidatorModel):
    DataSourceId: str


class DeleteEvaluationInput(BaseValidatorModel):
    EvaluationId: str


class DeleteMLModelInput(BaseValidatorModel):
    MLModelId: str


class DeleteRealtimeEndpointInput(BaseValidatorModel):
    MLModelId: str


class DeleteTagsInput(BaseValidatorModel):
    TagKeys: Sequence[str]
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


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


class DescribeTagsInput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class PerformanceMetrics(BaseValidatorModel):
    Properties: Optional[Dict[str, str]] = None


class GetBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str


class GetDataSourceInput(BaseValidatorModel):
    DataSourceId: str
    Verbose: Optional[bool] = None


class GetEvaluationInput(BaseValidatorModel):
    EvaluationId: str


class GetMLModelInput(BaseValidatorModel):
    MLModelId: str
    Verbose: Optional[bool] = None


class PredictInput(BaseValidatorModel):
    MLModelId: str
    Record: Mapping[str, str]
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


class UpdateBatchPredictionInput(BaseValidatorModel):
    BatchPredictionId: str
    BatchPredictionName: str


class UpdateDataSourceInput(BaseValidatorModel):
    DataSourceId: str
    DataSourceName: str


class UpdateEvaluationInput(BaseValidatorModel):
    EvaluationId: str
    EvaluationName: str


class UpdateMLModelInput(BaseValidatorModel):
    MLModelId: str
    MLModelName: Optional[str] = None
    ScoreThreshold: Optional[float] = None


class AddTagsInput(BaseValidatorModel):
    Tags: Sequence[Tag]
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class AddTagsOutput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadata


class CreateBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadata


class CreateDataSourceFromRDSOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


class CreateDataSourceFromRedshiftOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


class CreateDataSourceFromS3Output(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


class CreateEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadata


class CreateMLModelOutput(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadata


class DeleteBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadata


class DeleteDataSourceOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


class DeleteEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadata


class DeleteMLModelOutput(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadata


class DeleteTagsOutput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadata


class DescribeTagsOutput(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


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


class UpdateBatchPredictionOutput(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadata


class UpdateDataSourceOutput(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadata


class UpdateEvaluationOutput(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadata


class UpdateMLModelOutput(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadata


class DescribeBatchPredictionsOutput(BaseValidatorModel):
    Results: List[BatchPrediction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateDataSourceFromS3Input(BaseValidatorModel):
    DataSourceId: str
    DataSpec: S3DataSpec
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


class CreateRealtimeEndpointOutput(BaseValidatorModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfo
    ResponseMetadata: ResponseMetadata


class DeleteRealtimeEndpointOutput(BaseValidatorModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfo
    ResponseMetadata: ResponseMetadata


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
    Algorithm: Optional[Literal["sgd"]] = None
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
    SecurityGroupIds: Sequence[str]
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


class DescribeMLModelsOutput(BaseValidatorModel):
    Results: List[MLModel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEvaluationsOutput(BaseValidatorModel):
    Results: List[Evaluation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateDataSourceFromRDSInput(BaseValidatorModel):
    DataSourceId: str
    RDSData: RDSDataSpec
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


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


class DescribeDataSourcesOutput(BaseValidatorModel):
    Results: List[DataSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


