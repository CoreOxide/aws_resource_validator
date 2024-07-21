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
from aws_resource_validator.pydantic_models.machinelearning_constants import *

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchPredictionTypeDef(BaseModel):
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

class CreateBatchPredictionInputRequestTypeDef(BaseModel):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    OutputUri: str
    BatchPredictionName: Optional[str] = None

class S3DataSpecTypeDef(BaseModel):
    DataLocationS3: str
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaLocationS3: Optional[str] = None

class CreateEvaluationInputRequestTypeDef(BaseModel):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    EvaluationName: Optional[str] = None

class CreateMLModelInputRequestTypeDef(BaseModel):
    MLModelId: str
    MLModelType: MLModelTypeType
    TrainingDataSourceId: str
    MLModelName: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    Recipe: Optional[str] = None
    RecipeUri: Optional[str] = None

class CreateRealtimeEndpointInputRequestTypeDef(BaseModel):
    MLModelId: str

class RealtimeEndpointInfoTypeDef(BaseModel):
    PeakRequestsPerSecond: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    EndpointUrl: Optional[str] = None
    EndpointStatus: Optional[RealtimeEndpointStatusType] = None

class DeleteBatchPredictionInputRequestTypeDef(BaseModel):
    BatchPredictionId: str

class DeleteDataSourceInputRequestTypeDef(BaseModel):
    DataSourceId: str

class DeleteEvaluationInputRequestTypeDef(BaseModel):
    EvaluationId: str

class DeleteMLModelInputRequestTypeDef(BaseModel):
    MLModelId: str

class DeleteRealtimeEndpointInputRequestTypeDef(BaseModel):
    MLModelId: str

class DeleteTagsInputRequestTypeDef(BaseModel):
    TagKeys: Sequence[str]
    ResourceId: str
    ResourceType: TaggableResourceTypeType

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBatchPredictionsInputRequestTypeDef(BaseModel):
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

class DescribeDataSourcesInputRequestTypeDef(BaseModel):
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

class DescribeEvaluationsInputRequestTypeDef(BaseModel):
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

class DescribeMLModelsInputRequestTypeDef(BaseModel):
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

class DescribeTagsInputRequestTypeDef(BaseModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType

class PerformanceMetricsTypeDef(BaseModel):
    Properties: Optional[Dict[str, str]] = None

class GetBatchPredictionInputRequestTypeDef(BaseModel):
    BatchPredictionId: str

class GetDataSourceInputRequestTypeDef(BaseModel):
    DataSourceId: str
    Verbose: Optional[bool] = None

class GetEvaluationInputRequestTypeDef(BaseModel):
    EvaluationId: str

class GetMLModelInputRequestTypeDef(BaseModel):
    MLModelId: str
    Verbose: Optional[bool] = None

class PredictInputRequestTypeDef(BaseModel):
    MLModelId: str
    Record: Mapping[str, str]
    PredictEndpoint: str

class PredictionTypeDef(BaseModel):
    predictedLabel: Optional[str] = None
    predictedValue: Optional[float] = None
    predictedScores: Optional[Dict[str, float]] = None
    details: Optional[Dict[DetailsAttributesType, str]] = None

class RDSDatabaseCredentialsTypeDef(BaseModel):
    Username: str
    Password: str

class RDSDatabaseTypeDef(BaseModel):
    InstanceIdentifier: str
    DatabaseName: str

class RedshiftDatabaseCredentialsTypeDef(BaseModel):
    Username: str
    Password: str

class RedshiftDatabaseTypeDef(BaseModel):
    DatabaseName: str
    ClusterIdentifier: str

class UpdateBatchPredictionInputRequestTypeDef(BaseModel):
    BatchPredictionId: str
    BatchPredictionName: str

class UpdateDataSourceInputRequestTypeDef(BaseModel):
    DataSourceId: str
    DataSourceName: str

class UpdateEvaluationInputRequestTypeDef(BaseModel):
    EvaluationId: str
    EvaluationName: str

class UpdateMLModelInputRequestTypeDef(BaseModel):
    MLModelId: str
    MLModelName: Optional[str] = None
    ScoreThreshold: Optional[float] = None

class AddTagsInputRequestTypeDef(BaseModel):
    Tags: Sequence[TagTypeDef]
    ResourceId: str
    ResourceType: TaggableResourceTypeType

class AddTagsOutputTypeDef(BaseModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBatchPredictionOutputTypeDef(BaseModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromRDSOutputTypeDef(BaseModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromRedshiftOutputTypeDef(BaseModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromS3OutputTypeDef(BaseModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluationOutputTypeDef(BaseModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLModelOutputTypeDef(BaseModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBatchPredictionOutputTypeDef(BaseModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceOutputTypeDef(BaseModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEvaluationOutputTypeDef(BaseModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMLModelOutputTypeDef(BaseModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTagsOutputTypeDef(BaseModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTagsOutputTypeDef(BaseModel):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBatchPredictionOutputTypeDef(BaseModel):
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

class UpdateBatchPredictionOutputTypeDef(BaseModel):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceOutputTypeDef(BaseModel):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEvaluationOutputTypeDef(BaseModel):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMLModelOutputTypeDef(BaseModel):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBatchPredictionsOutputTypeDef(BaseModel):
    Results: List[BatchPredictionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromS3InputRequestTypeDef(BaseModel):
    DataSourceId: str
    DataSpec: S3DataSpecTypeDef
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None

class CreateRealtimeEndpointOutputTypeDef(BaseModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRealtimeEndpointOutputTypeDef(BaseModel):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLModelOutputTypeDef(BaseModel):
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

class MLModelTypeDef(BaseModel):
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

class DescribeBatchPredictionsInputBatchPredictionAvailableWaitTypeDef(BaseModel):
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

class DescribeDataSourcesInputDataSourceAvailableWaitTypeDef(BaseModel):
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

class DescribeEvaluationsInputEvaluationAvailableWaitTypeDef(BaseModel):
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

class DescribeMLModelsInputMLModelAvailableWaitTypeDef(BaseModel):
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

class DescribeBatchPredictionsInputDescribeBatchPredictionsPaginateTypeDef(BaseModel):
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

class DescribeDataSourcesInputDescribeDataSourcesPaginateTypeDef(BaseModel):
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

class DescribeEvaluationsInputDescribeEvaluationsPaginateTypeDef(BaseModel):
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

class DescribeMLModelsInputDescribeMLModelsPaginateTypeDef(BaseModel):
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

class EvaluationTypeDef(BaseModel):
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

class GetEvaluationOutputTypeDef(BaseModel):
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

class PredictOutputTypeDef(BaseModel):
    Prediction: PredictionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RDSDataSpecTypeDef(BaseModel):
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

class RDSMetadataTypeDef(BaseModel):
    Database: Optional[RDSDatabaseTypeDef] = None
    DatabaseUserName: Optional[str] = None
    SelectSqlQuery: Optional[str] = None
    ResourceRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    DataPipelineId: Optional[str] = None

class RedshiftDataSpecTypeDef(BaseModel):
    DatabaseInformation: RedshiftDatabaseTypeDef
    SelectSqlQuery: str
    DatabaseCredentials: RedshiftDatabaseCredentialsTypeDef
    S3StagingLocation: str
    DataRearrangement: Optional[str] = None
    DataSchema: Optional[str] = None
    DataSchemaUri: Optional[str] = None

class RedshiftMetadataTypeDef(BaseModel):
    RedshiftDatabase: Optional[RedshiftDatabaseTypeDef] = None
    DatabaseUserName: Optional[str] = None
    SelectSqlQuery: Optional[str] = None

class DescribeMLModelsOutputTypeDef(BaseModel):
    Results: List[MLModelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEvaluationsOutputTypeDef(BaseModel):
    Results: List[EvaluationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromRDSInputRequestTypeDef(BaseModel):
    DataSourceId: str
    RDSData: RDSDataSpecTypeDef
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None

class CreateDataSourceFromRedshiftInputRequestTypeDef(BaseModel):
    DataSourceId: str
    DataSpec: RedshiftDataSpecTypeDef
    RoleARN: str
    DataSourceName: Optional[str] = None
    ComputeStatistics: Optional[bool] = None

class DataSourceTypeDef(BaseModel):
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

class GetDataSourceOutputTypeDef(BaseModel):
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

class DescribeDataSourcesOutputTypeDef(BaseModel):
    Results: List[DataSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

