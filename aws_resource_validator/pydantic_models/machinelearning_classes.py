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

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchPredictionTypeDef(BaseValidatorModel):
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


class CreateBatchPredictionInputTypeDef(BaseValidatorModel):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    OutputUri: str
    BatchPredictionName: Optional[str] = None


class S3DataSpecTypeDef(BaseValidatorModel):
    DataLocationS3: str
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaLocationS3: Optional[str] = None


class CreateEvaluationInputTypeDef(BaseValidatorModel):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    EvaluationName: Optional[str] = None


class CreateMLModelInputTypeDef(BaseValidatorModel):
    MLModelId: str
    MLModelType: MLModelTypeType
    TrainingDataSourceId: str
    MLModelName: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    Recipe: Optional[str] = None
    RecipeUri: Optional[str] = None


class CreateRealtimeEndpointInputTypeDef(BaseValidatorModel):
    MLModelId: str


class RealtimeEndpointInfoTypeDef(BaseValidatorModel):
    PeakRequestsPerSecond: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    EndpointUrl: Optional[str] = None
    EndpointStatus: Optional[RealtimeEndpointStatusType] = None


class DeleteBatchPredictionInputTypeDef(BaseValidatorModel):
    BatchPredictionId: str


class DeleteDataSourceInputTypeDef(BaseValidatorModel):
    DataSourceId: str


class DeleteEvaluationInputTypeDef(BaseValidatorModel):
    EvaluationId: str


class DeleteMLModelInputTypeDef(BaseValidatorModel):
    MLModelId: str


class DeleteRealtimeEndpointInputTypeDef(BaseValidatorModel):
    MLModelId: str


class DeleteTagsInputTypeDef(BaseValidatorModel):
    TagKeys: Sequence[str]
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBatchPredictionsInputTypeDef(BaseValidatorModel):
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


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeDataSourcesInputTypeDef(BaseValidatorModel):
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


class DescribeEvaluationsInputTypeDef(BaseValidatorModel):
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


class DescribeMLModelsInputTypeDef(BaseValidatorModel):
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


class DescribeTagsInputTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class PerformanceMetricsTypeDef(BaseValidatorModel):
    Properties: Optional[Dict[str, str]] = None


class GetBatchPredictionInputTypeDef(BaseValidatorModel):
    BatchPredictionId: str


class GetDataSourceInputTypeDef(BaseValidatorModel):
    DataSourceId: str
    Verbose: Optional[bool] = None


class GetEvaluationInputTypeDef(BaseValidatorModel):
    EvaluationId: str


class GetMLModelInputTypeDef(BaseValidatorModel):
    MLModelId: str
    Verbose: Optional[bool] = None


class PredictInputTypeDef(BaseValidatorModel):
    MLModelId: str
    Record: Mapping[str, str]
    PredictEndpoint: str


class PredictionTypeDef(BaseValidatorModel):
    predictedLabel: Optional[str] = None
    predictedValue: Optional[float] = None
    predictedScores: Optional[Dict[str, float]] = None
    details: Optional[Dict[DetailsAttributesType, str]] = None


class RDSDatabaseCredentialsTypeDef(BaseValidatorModel):
    Username: str
    Password: str


class RDSDatabaseTypeDef(BaseValidatorModel):
    InstanceIdentifier: str
    DatabaseName: str


class RedshiftDatabaseCredentialsTypeDef(BaseValidatorModel):
    Username: str
    Password: str


class RedshiftDatabaseTypeDef(BaseValidatorModel):
    DatabaseName: str
    ClusterIdentifier: str


class UpdateBatchPredictionInputTypeDef(BaseValidatorModel):
    BatchPredictionId: str
    BatchPredictionName: str


class UpdateDataSourceInputTypeDef(BaseValidatorModel):
    DataSourceId: str
    DataSourceName: str


class UpdateEvaluationInputTypeDef(BaseValidatorModel):
    EvaluationId: str
    EvaluationName: str


class UpdateMLModelInputTypeDef(BaseValidatorModel):
    MLModelId: str
    MLModelName: Optional[str] = None
    ScoreThreshold: Optional[float] = None


class AddTagsInputTypeDef(BaseValidatorModel):
    Tags: Sequence[TagTypeDef]
    ResourceId: str
    ResourceType: TaggableResourceTypeType


class AddTagsOutputTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBatchPredictionOutputTypeDef(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataSourceFromRDSOutputTypeDef(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataSourceFromRedshiftOutputTypeDef(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataSourceFromS3OutputTypeDef(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEvaluationOutputTypeDef(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMLModelOutputTypeDef(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBatchPredictionOutputTypeDef(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataSourceOutputTypeDef(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEvaluationOutputTypeDef(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMLModelOutputTypeDef(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTagsOutputTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTagsOutputTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBatchPredictionOutputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBatchPredictionOutputTypeDef(BaseValidatorModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataSourceOutputTypeDef(BaseValidatorModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEvaluationOutputTypeDef(BaseValidatorModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMLModelOutputTypeDef(BaseValidatorModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBatchPredictionsOutputTypeDef(BaseValidatorModel):
    Results: List[BatchPredictionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateDataSourceFromS3InputTypeDef(BaseValidatorModel):
    DataSourceId: str
    DataSpec: S3DataSpecTypeDef
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


class CreateRealtimeEndpointOutputTypeDef(BaseValidatorModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRealtimeEndpointOutputTypeDef(BaseValidatorModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMLModelOutputTypeDef(BaseValidatorModel):
    MLModelId: str
    TrainingDataSourceId: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    SizeInBytes: int
    EndpointInfo: RealtimeEndpointInfoTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef


class MLModelTypeDef(BaseValidatorModel):
    MLModelId: Optional[str] = None
    TrainingDataSourceId: Optional[str] = None
    CreatedByIamUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[EntityStatusType] = None
    SizeInBytes: Optional[int] = None
    EndpointInfo: Optional[RealtimeEndpointInfoTypeDef] = None
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


class DescribeBatchPredictionsInputPaginateTypeDef(BaseValidatorModel):
    FilterVariable: Optional[BatchPredictionFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDataSourcesInputPaginateTypeDef(BaseValidatorModel):
    FilterVariable: Optional[DataSourceFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEvaluationsInputPaginateTypeDef(BaseValidatorModel):
    FilterVariable: Optional[EvaluationFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMLModelsInputPaginateTypeDef(BaseValidatorModel):
    FilterVariable: Optional[MLModelFilterVariableType] = None
    EQ: Optional[str] = None
    GT: Optional[str] = None
    LT: Optional[str] = None
    GE: Optional[str] = None
    LE: Optional[str] = None
    NE: Optional[str] = None
    Prefix: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBatchPredictionsInputWaitTypeDef(BaseValidatorModel):
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
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeDataSourcesInputWaitTypeDef(BaseValidatorModel):
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
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeEvaluationsInputWaitTypeDef(BaseValidatorModel):
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
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeMLModelsInputWaitTypeDef(BaseValidatorModel):
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
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class EvaluationTypeDef(BaseValidatorModel):
    EvaluationId: Optional[str] = None
    MLModelId: Optional[str] = None
    EvaluationDataSourceId: Optional[str] = None
    InputDataLocationS3: Optional[str] = None
    CreatedByIamUser: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[EntityStatusType] = None
    PerformanceMetrics: Optional[PerformanceMetricsTypeDef] = None
    Message: Optional[str] = None
    ComputeTime: Optional[int] = None
    FinishedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None


class GetEvaluationOutputTypeDef(BaseValidatorModel):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    PerformanceMetrics: PerformanceMetricsTypeDef
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PredictOutputTypeDef(BaseValidatorModel):
    Prediction: PredictionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RDSDataSpecTypeDef(BaseValidatorModel):
    DatabaseInformation: RDSDatabaseTypeDef
    SelectSqlQuery: str
    DatabaseCredentials: RDSDatabaseCredentialsTypeDef
    S3StagingLocation: str
    ResourceRole: str
    ServiceRole: str
    SubnetId: str
    SecurityGroupIds: Sequence[str]
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaUri: Optional[str] = None


class RDSMetadataTypeDef(BaseValidatorModel):
    Database: Optional[RDSDatabaseTypeDef] = None
    DatabaseUserName: Optional[str] = None
    SelectSqlQuery: Optional[str] = None
    ResourceRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    DataPipelineId: Optional[str] = None


class RedshiftDataSpecTypeDef(BaseValidatorModel):
    DatabaseInformation: RedshiftDatabaseTypeDef
    SelectSqlQuery: str
    DatabaseCredentials: RedshiftDatabaseCredentialsTypeDef
    S3StagingLocation: str
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaUri: Optional[str] = None


class RedshiftMetadataTypeDef(BaseValidatorModel):
    RedshiftDatabase: Optional[RedshiftDatabaseTypeDef] = None
    DatabaseUserName: Optional[str] = None
    SelectSqlQuery: Optional[str] = None


class DescribeMLModelsOutputTypeDef(BaseValidatorModel):
    Results: List[MLModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeEvaluationsOutputTypeDef(BaseValidatorModel):
    Results: List[EvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateDataSourceFromRDSInputTypeDef(BaseValidatorModel):
    DataSourceId: str
    RDSData: RDSDataSpecTypeDef
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


class CreateDataSourceFromRedshiftInputTypeDef(BaseValidatorModel):
    DataSourceId: str
    DataSpec: RedshiftDataSpecTypeDef
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None


class DataSourceTypeDef(BaseValidatorModel):
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
    RedshiftMetadata: Optional[RedshiftMetadataTypeDef] = None
    RDSMetadata: Optional[RDSMetadataTypeDef] = None
    RoleARN: Optional[str] = None
    ComputeStatistics: Optional[bool] = None
    ComputeTime: Optional[int] = None
    FinishedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None


class GetDataSourceOutputTypeDef(BaseValidatorModel):
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
    RedshiftMetadata: RedshiftMetadataTypeDef
    RDSMetadata: RDSMetadataTypeDef
    RoleARN: str
    ComputeStatistics: bool
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    DataSourceSchema: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDataSourcesOutputTypeDef(BaseValidatorModel):
    Results: List[DataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


