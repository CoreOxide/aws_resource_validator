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
from aws_resource_validator.pydantic_models.neptunedata_constants import *

class CancelGremlinQueryInputRequestTypeDef(BaseModel):
    queryId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelLoaderJobInputRequestTypeDef(BaseModel):
    loadId: str

class CancelMLDataProcessingJobInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class CancelMLModelTrainingJobInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class CancelMLModelTransformJobInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class CancelOpenCypherQueryInputRequestTypeDef(BaseModel):
    queryId: str
    silent: Optional[bool] = None

class CreateMLEndpointInputRequestTypeDef(BaseModel):
    id: Optional[str] = None
    mlModelTrainingJobId: Optional[str] = None
    mlModelTransformJobId: Optional[str] = None
    update: Optional[bool] = None
    neptuneIamRoleArn: Optional[str] = None
    modelName: Optional[str] = None
    instanceType: Optional[str] = None
    instanceCount: Optional[int] = None
    volumeEncryptionKMSKey: Optional[str] = None

class CustomModelTrainingParametersTypeDef(BaseModel):
    sourceS3DirectoryPath: str
    trainingEntryPointScript: Optional[str] = None
    transformEntryPointScript: Optional[str] = None

class CustomModelTransformParametersTypeDef(BaseModel):
    sourceS3DirectoryPath: str
    transformEntryPointScript: Optional[str] = None

class DeleteMLEndpointInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class DeleteStatisticsValueMapTypeDef(BaseModel):
    active: Optional[bool] = None
    statisticsId: Optional[str] = None

class EdgeStructureTypeDef(BaseModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None

class ExecuteFastResetInputRequestTypeDef(BaseModel):
    action: ActionType
    token: Optional[str] = None

class FastResetTokenTypeDef(BaseModel):
    token: Optional[str] = None

class ExecuteGremlinExplainQueryInputRequestTypeDef(BaseModel):
    gremlinQuery: str

class ExecuteGremlinProfileQueryInputRequestTypeDef(BaseModel):
    gremlinQuery: str
    results: Optional[bool] = None
    chop: Optional[int] = None
    serializer: Optional[str] = None
    indexOps: Optional[bool] = None

class ExecuteGremlinQueryInputRequestTypeDef(BaseModel):
    gremlinQuery: str
    serializer: Optional[str] = None

class GremlinQueryStatusAttributesTypeDef(BaseModel):
    message: Optional[str] = None
    code: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None

class ExecuteOpenCypherExplainQueryInputRequestTypeDef(BaseModel):
    openCypherQuery: str
    explainMode: OpenCypherExplainModeType
    parameters: Optional[str] = None

class ExecuteOpenCypherQueryInputRequestTypeDef(BaseModel):
    openCypherQuery: str
    parameters: Optional[str] = None

class QueryLanguageVersionTypeDef(BaseModel):
    version: str

class GetGremlinQueryStatusInputRequestTypeDef(BaseModel):
    queryId: str

class QueryEvalStatsTypeDef(BaseModel):
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    cancelled: Optional[bool] = None
    subqueries: Optional[Dict[str, Any]] = None

class GetLoaderJobStatusInputRequestTypeDef(BaseModel):
    loadId: str
    details: Optional[bool] = None
    errors: Optional[bool] = None
    page: Optional[int] = None
    errorsPerPage: Optional[int] = None

class GetMLDataProcessingJobInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class MlResourceDefinitionTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[str] = None
    outputLocation: Optional[str] = None
    failureReason: Optional[str] = None
    cloudwatchLogUrl: Optional[str] = None

class GetMLEndpointInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class MlConfigDefinitionTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None

class GetMLModelTrainingJobInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class GetMLModelTransformJobInputRequestTypeDef(BaseModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class GetOpenCypherQueryStatusInputRequestTypeDef(BaseModel):
    queryId: str

class GetPropertygraphStreamInputRequestTypeDef(BaseModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None

class GetPropertygraphSummaryInputRequestTypeDef(BaseModel):
    mode: Optional[GraphSummaryTypeType] = None

class GetRDFGraphSummaryInputRequestTypeDef(BaseModel):
    mode: Optional[GraphSummaryTypeType] = None

class GetSparqlStreamInputRequestTypeDef(BaseModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None

class ListGremlinQueriesInputRequestTypeDef(BaseModel):
    includeWaiting: Optional[bool] = None

class ListLoaderJobsInputRequestTypeDef(BaseModel):
    limit: Optional[int] = None
    includeQueuedLoads: Optional[bool] = None

class LoaderIdResultTypeDef(BaseModel):
    loadIds: Optional[List[str]] = None

class ListMLDataProcessingJobsInputRequestTypeDef(BaseModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListMLEndpointsInputRequestTypeDef(BaseModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListMLModelTrainingJobsInputRequestTypeDef(BaseModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListMLModelTransformJobsInputRequestTypeDef(BaseModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListOpenCypherQueriesInputRequestTypeDef(BaseModel):
    includeWaiting: Optional[bool] = None

class ManagePropertygraphStatisticsInputRequestTypeDef(BaseModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None

class RefreshStatisticsIdMapTypeDef(BaseModel):
    statisticsId: Optional[str] = None

class ManageSparqlStatisticsInputRequestTypeDef(BaseModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None

class NodeStructureTypeDef(BaseModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None

class PropertygraphDataTypeDef(BaseModel):
    id: str
    type: str
    key: str
    value: Dict[str, Any]
    from: Optional[str] = None
    to: Optional[str] = None

class SubjectStructureTypeDef(BaseModel):
    count: Optional[int] = None
    predicates: Optional[List[str]] = None

class SparqlDataTypeDef(BaseModel):
    stmt: str

class StartLoaderJobInputRequestTypeDef(BaseModel):
    source: str
    format: FormatType
    s3BucketRegion: S3BucketRegionType
    iamRoleArn: str
    mode: Optional[ModeType] = None
    failOnError: Optional[bool] = None
    parallelism: Optional[ParallelismType] = None
    parserConfiguration: Optional[Mapping[str, str]] = None
    updateSingleCardinalityProperties: Optional[bool] = None
    queueRequest: Optional[bool] = None
    dependencies: Optional[Sequence[str]] = None
    userProvidedEdgeIds: Optional[bool] = None

class StartMLDataProcessingJobInputRequestTypeDef(BaseModel):
    inputDataS3Location: str
    processedDataS3Location: str
    id: Optional[str] = None
    previousDataProcessingJobId: Optional[str] = None
    sagemakerIamRoleArn: Optional[str] = None
    neptuneIamRoleArn: Optional[str] = None
    processingInstanceType: Optional[str] = None
    processingInstanceVolumeSizeInGB: Optional[int] = None
    processingTimeOutInSeconds: Optional[int] = None
    modelType: Optional[str] = None
    configFileName: Optional[str] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    volumeEncryptionKMSKey: Optional[str] = None
    s3OutputEncryptionKMSKey: Optional[str] = None

class StatisticsSummaryTypeDef(BaseModel):
    signatureCount: Optional[int] = None
    instanceCount: Optional[int] = None
    predicateCount: Optional[int] = None

class CancelGremlinQueryOutputTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelLoaderJobOutputTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLDataProcessingJobOutputTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLModelTrainingJobOutputTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLModelTransformJobOutputTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelOpenCypherQueryOutputTypeDef(BaseModel):
    status: str
    payload: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLEndpointOutputTypeDef(BaseModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMLEndpointOutputTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinExplainQueryOutputTypeDef(BaseModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinProfileQueryOutputTypeDef(BaseModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteOpenCypherExplainQueryOutputTypeDef(BaseModel):
    results: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteOpenCypherQueryOutputTypeDef(BaseModel):
    results: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoaderJobStatusOutputTypeDef(BaseModel):
    status: str
    payload: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLDataProcessingJobsOutputTypeDef(BaseModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLEndpointsOutputTypeDef(BaseModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLModelTrainingJobsOutputTypeDef(BaseModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLModelTransformJobsOutputTypeDef(BaseModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartLoaderJobOutputTypeDef(BaseModel):
    status: str
    payload: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLDataProcessingJobOutputTypeDef(BaseModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLModelTrainingJobOutputTypeDef(BaseModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLModelTransformJobOutputTypeDef(BaseModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLModelTrainingJobInputRequestTypeDef(BaseModel):
    dataProcessingJobId: str
    trainModelS3Location: str
    id: Optional[str] = None
    previousModelTrainingJobId: Optional[str] = None
    sagemakerIamRoleArn: Optional[str] = None
    neptuneIamRoleArn: Optional[str] = None
    baseProcessingInstanceType: Optional[str] = None
    trainingInstanceType: Optional[str] = None
    trainingInstanceVolumeSizeInGB: Optional[int] = None
    trainingTimeOutInSeconds: Optional[int] = None
    maxHPONumberOfTrainingJobs: Optional[int] = None
    maxHPOParallelTrainingJobs: Optional[int] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    volumeEncryptionKMSKey: Optional[str] = None
    s3OutputEncryptionKMSKey: Optional[str] = None
    enableManagedSpotTraining: Optional[bool] = None
    customModelTrainingParameters: Optional[CustomModelTrainingParametersTypeDef] = None

class StartMLModelTransformJobInputRequestTypeDef(BaseModel):
    modelTransformOutputS3Location: str
    id: Optional[str] = None
    dataProcessingJobId: Optional[str] = None
    mlModelTrainingJobId: Optional[str] = None
    trainingJobName: Optional[str] = None
    sagemakerIamRoleArn: Optional[str] = None
    neptuneIamRoleArn: Optional[str] = None
    customModelTransformParameters: Optional[CustomModelTransformParametersTypeDef] = None
    baseProcessingInstanceType: Optional[str] = None
    baseProcessingInstanceVolumeSizeInGB: Optional[int] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    volumeEncryptionKMSKey: Optional[str] = None
    s3OutputEncryptionKMSKey: Optional[str] = None

class DeletePropertygraphStatisticsOutputTypeDef(BaseModel):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSparqlStatisticsOutputTypeDef(BaseModel):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteFastResetOutputTypeDef(BaseModel):
    status: str
    payload: FastResetTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinQueryOutputTypeDef(BaseModel):
    requestId: str
    status: GremlinQueryStatusAttributesTypeDef
    result: Dict[str, Any]
    meta: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEngineStatusOutputTypeDef(BaseModel):
    status: str
    startTime: str
    dbEngineVersion: str
    role: str
    dfeQueryEngine: str
    gremlin: QueryLanguageVersionTypeDef
    sparql: QueryLanguageVersionTypeDef
    opencypher: QueryLanguageVersionTypeDef
    labMode: Dict[str, str]
    rollingBackTrxCount: int
    rollingBackTrxEarliestStartTime: str
    features: Dict[str, Dict[str, Any]]
    settings: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGremlinQueryStatusOutputTypeDef(BaseModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOpenCypherQueryStatusOutputTypeDef(BaseModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GremlinQueryStatusTypeDef(BaseModel):
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    queryEvalStats: Optional[QueryEvalStatsTypeDef] = None

class GetMLDataProcessingJobOutputTypeDef(BaseModel):
    status: str
    id: str
    processingJob: MlResourceDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLEndpointOutputTypeDef(BaseModel):
    status: str
    id: str
    endpoint: MlResourceDefinitionTypeDef
    endpointConfig: MlConfigDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLModelTrainingJobOutputTypeDef(BaseModel):
    status: str
    id: str
    processingJob: MlResourceDefinitionTypeDef
    hpoJob: MlResourceDefinitionTypeDef
    modelTransformJob: MlResourceDefinitionTypeDef
    mlModels: List[MlConfigDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLModelTransformJobOutputTypeDef(BaseModel):
    status: str
    id: str
    baseProcessingJob: MlResourceDefinitionTypeDef
    remoteModelTransformJob: MlResourceDefinitionTypeDef
    models: List[MlConfigDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoaderJobsOutputTypeDef(BaseModel):
    status: str
    payload: LoaderIdResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ManagePropertygraphStatisticsOutputTypeDef(BaseModel):
    status: str
    payload: RefreshStatisticsIdMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ManageSparqlStatisticsOutputTypeDef(BaseModel):
    status: str
    payload: RefreshStatisticsIdMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PropertygraphSummaryTypeDef(BaseModel):
    numNodes: Optional[int] = None
    numEdges: Optional[int] = None
    numNodeLabels: Optional[int] = None
    numEdgeLabels: Optional[int] = None
    nodeLabels: Optional[List[str]] = None
    edgeLabels: Optional[List[str]] = None
    numNodeProperties: Optional[int] = None
    numEdgeProperties: Optional[int] = None
    nodeProperties: Optional[List[Dict[str, int]]] = None
    edgeProperties: Optional[List[Dict[str, int]]] = None
    totalNodePropertyValues: Optional[int] = None
    totalEdgePropertyValues: Optional[int] = None
    nodeStructures: Optional[List[NodeStructureTypeDef]] = None
    edgeStructures: Optional[List[EdgeStructureTypeDef]] = None

class PropertygraphRecordTypeDef(BaseModel):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: PropertygraphDataTypeDef
    op: str
    isLastOp: Optional[bool] = None

class RDFGraphSummaryTypeDef(BaseModel):
    numDistinctSubjects: Optional[int] = None
    numDistinctPredicates: Optional[int] = None
    numQuads: Optional[int] = None
    numClasses: Optional[int] = None
    classes: Optional[List[str]] = None
    predicates: Optional[List[Dict[str, int]]] = None
    subjectStructures: Optional[List[SubjectStructureTypeDef]] = None

class SparqlRecordTypeDef(BaseModel):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: SparqlDataTypeDef
    op: str
    isLastOp: Optional[bool] = None

class StatisticsTypeDef(BaseModel):
    autoCompute: Optional[bool] = None
    active: Optional[bool] = None
    statisticsId: Optional[str] = None
    date: Optional[datetime] = None
    note: Optional[str] = None
    signatureInfo: Optional[StatisticsSummaryTypeDef] = None

class ListGremlinQueriesOutputTypeDef(BaseModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenCypherQueriesOutputTypeDef(BaseModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PropertygraphSummaryValueMapTypeDef(BaseModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[PropertygraphSummaryTypeDef] = None

class GetPropertygraphStreamOutputTypeDef(BaseModel):
    lastEventId: Dict[str, str]
    lastTrxTimestampInMillis: int
    format: str
    records: List[PropertygraphRecordTypeDef]
    totalRecords: int
    ResponseMetadata: ResponseMetadataTypeDef

class RDFGraphSummaryValueMapTypeDef(BaseModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[RDFGraphSummaryTypeDef] = None

class GetSparqlStreamOutputTypeDef(BaseModel):
    lastEventId: Dict[str, str]
    lastTrxTimestampInMillis: int
    format: str
    records: List[SparqlRecordTypeDef]
    totalRecords: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetPropertygraphStatisticsOutputTypeDef(BaseModel):
    status: str
    payload: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSparqlStatisticsOutputTypeDef(BaseModel):
    status: str
    payload: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPropertygraphSummaryOutputTypeDef(BaseModel):
    statusCode: int
    payload: PropertygraphSummaryValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRDFGraphSummaryOutputTypeDef(BaseModel):
    statusCode: int
    payload: RDFGraphSummaryValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

