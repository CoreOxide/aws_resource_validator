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
from aws_resource_validator.pydantic_models.neptunedata_constants import *

class CancelGremlinQueryInputRequestTypeDef(BaseValidatorModel):
    queryId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelLoaderJobInputRequestTypeDef(BaseValidatorModel):
    loadId: str

class CancelMLDataProcessingJobInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class CancelMLModelTrainingJobInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class CancelMLModelTransformJobInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class CancelOpenCypherQueryInputRequestTypeDef(BaseValidatorModel):
    queryId: str
    silent: Optional[bool] = None

class CreateMLEndpointInputRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    mlModelTrainingJobId: Optional[str] = None
    mlModelTransformJobId: Optional[str] = None
    update: Optional[bool] = None
    neptuneIamRoleArn: Optional[str] = None
    modelName: Optional[str] = None
    instanceType: Optional[str] = None
    instanceCount: Optional[int] = None
    volumeEncryptionKMSKey: Optional[str] = None

class CustomModelTrainingParametersTypeDef(BaseValidatorModel):
    sourceS3DirectoryPath: str
    trainingEntryPointScript: Optional[str] = None
    transformEntryPointScript: Optional[str] = None

class CustomModelTransformParametersTypeDef(BaseValidatorModel):
    sourceS3DirectoryPath: str
    transformEntryPointScript: Optional[str] = None

class DeleteMLEndpointInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None

class DeleteStatisticsValueMapTypeDef(BaseValidatorModel):
    active: Optional[bool] = None
    statisticsId: Optional[str] = None

class EdgeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None

class ExecuteFastResetInputRequestTypeDef(BaseValidatorModel):
    action: ActionType
    token: Optional[str] = None

class FastResetTokenTypeDef(BaseValidatorModel):
    token: Optional[str] = None

class ExecuteGremlinExplainQueryInputRequestTypeDef(BaseValidatorModel):
    gremlinQuery: str

class ExecuteGremlinProfileQueryInputRequestTypeDef(BaseValidatorModel):
    gremlinQuery: str
    results: Optional[bool] = None
    chop: Optional[int] = None
    serializer: Optional[str] = None
    indexOps: Optional[bool] = None

class ExecuteGremlinQueryInputRequestTypeDef(BaseValidatorModel):
    gremlinQuery: str
    serializer: Optional[str] = None

class GremlinQueryStatusAttributesTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    code: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None

class ExecuteOpenCypherExplainQueryInputRequestTypeDef(BaseValidatorModel):
    openCypherQuery: str
    explainMode: OpenCypherExplainModeType
    parameters: Optional[str] = None

class ExecuteOpenCypherQueryInputRequestTypeDef(BaseValidatorModel):
    openCypherQuery: str
    parameters: Optional[str] = None

class QueryLanguageVersionTypeDef(BaseValidatorModel):
    version: str

class GetGremlinQueryStatusInputRequestTypeDef(BaseValidatorModel):
    queryId: str

class QueryEvalStatsTypeDef(BaseValidatorModel):
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    cancelled: Optional[bool] = None
    subqueries: Optional[Dict[str, Any]] = None

class GetLoaderJobStatusInputRequestTypeDef(BaseValidatorModel):
    loadId: str
    details: Optional[bool] = None
    errors: Optional[bool] = None
    page: Optional[int] = None
    errorsPerPage: Optional[int] = None

class GetMLDataProcessingJobInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class MlResourceDefinitionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[str] = None
    outputLocation: Optional[str] = None
    failureReason: Optional[str] = None
    cloudwatchLogUrl: Optional[str] = None

class GetMLEndpointInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class MlConfigDefinitionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None

class GetMLModelTrainingJobInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class GetMLModelTransformJobInputRequestTypeDef(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None

class GetOpenCypherQueryStatusInputRequestTypeDef(BaseValidatorModel):
    queryId: str

class GetPropertygraphStreamInputRequestTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None

class GetPropertygraphSummaryInputRequestTypeDef(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None

class GetRDFGraphSummaryInputRequestTypeDef(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None

class GetSparqlStreamInputRequestTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None

class ListGremlinQueriesInputRequestTypeDef(BaseValidatorModel):
    includeWaiting: Optional[bool] = None

class ListLoaderJobsInputRequestTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    includeQueuedLoads: Optional[bool] = None

class LoaderIdResultTypeDef(BaseValidatorModel):
    loadIds: Optional[List[str]] = None

class ListMLDataProcessingJobsInputRequestTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListMLEndpointsInputRequestTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListMLModelTrainingJobsInputRequestTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListMLModelTransformJobsInputRequestTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None

class ListOpenCypherQueriesInputRequestTypeDef(BaseValidatorModel):
    includeWaiting: Optional[bool] = None

class ManagePropertygraphStatisticsInputRequestTypeDef(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None

class RefreshStatisticsIdMapTypeDef(BaseValidatorModel):
    statisticsId: Optional[str] = None

class ManageSparqlStatisticsInputRequestTypeDef(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None

class NodeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None

class PropertygraphDataTypeDef(BaseValidatorModel):
    id: str
    type: str
    key: str
    value: Dict[str, Any]
    from: Optional[str] = None
    to: Optional[str] = None

class SubjectStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    predicates: Optional[List[str]] = None

class SparqlDataTypeDef(BaseValidatorModel):
    stmt: str

class StartLoaderJobInputRequestTypeDef(BaseValidatorModel):
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

class StartMLDataProcessingJobInputRequestTypeDef(BaseValidatorModel):
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

class StatisticsSummaryTypeDef(BaseValidatorModel):
    signatureCount: Optional[int] = None
    instanceCount: Optional[int] = None
    predicateCount: Optional[int] = None

class CancelGremlinQueryOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelLoaderJobOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLDataProcessingJobOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLModelTrainingJobOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLModelTransformJobOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelOpenCypherQueryOutputTypeDef(BaseValidatorModel):
    status: str
    payload: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLEndpointOutputTypeDef(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMLEndpointOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinExplainQueryOutputTypeDef(BaseValidatorModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinProfileQueryOutputTypeDef(BaseValidatorModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteOpenCypherExplainQueryOutputTypeDef(BaseValidatorModel):
    results: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteOpenCypherQueryOutputTypeDef(BaseValidatorModel):
    results: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoaderJobStatusOutputTypeDef(BaseValidatorModel):
    status: str
    payload: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLDataProcessingJobsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLEndpointsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLModelTrainingJobsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLModelTransformJobsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartLoaderJobOutputTypeDef(BaseValidatorModel):
    status: str
    payload: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLDataProcessingJobOutputTypeDef(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLModelTrainingJobOutputTypeDef(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLModelTransformJobOutputTypeDef(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLModelTrainingJobInputRequestTypeDef(BaseValidatorModel):
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

class StartMLModelTransformJobInputRequestTypeDef(BaseValidatorModel):
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

class DeletePropertygraphStatisticsOutputTypeDef(BaseValidatorModel):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSparqlStatisticsOutputTypeDef(BaseValidatorModel):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteFastResetOutputTypeDef(BaseValidatorModel):
    status: str
    payload: FastResetTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinQueryOutputTypeDef(BaseValidatorModel):
    requestId: str
    status: GremlinQueryStatusAttributesTypeDef
    result: Dict[str, Any]
    meta: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEngineStatusOutputTypeDef(BaseValidatorModel):
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

class GetGremlinQueryStatusOutputTypeDef(BaseValidatorModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOpenCypherQueryStatusOutputTypeDef(BaseValidatorModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GremlinQueryStatusTypeDef(BaseValidatorModel):
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    queryEvalStats: Optional[QueryEvalStatsTypeDef] = None

class GetMLDataProcessingJobOutputTypeDef(BaseValidatorModel):
    status: str
    id: str
    processingJob: MlResourceDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLEndpointOutputTypeDef(BaseValidatorModel):
    status: str
    id: str
    endpoint: MlResourceDefinitionTypeDef
    endpointConfig: MlConfigDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLModelTrainingJobOutputTypeDef(BaseValidatorModel):
    status: str
    id: str
    processingJob: MlResourceDefinitionTypeDef
    hpoJob: MlResourceDefinitionTypeDef
    modelTransformJob: MlResourceDefinitionTypeDef
    mlModels: List[MlConfigDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLModelTransformJobOutputTypeDef(BaseValidatorModel):
    status: str
    id: str
    baseProcessingJob: MlResourceDefinitionTypeDef
    remoteModelTransformJob: MlResourceDefinitionTypeDef
    models: List[MlConfigDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoaderJobsOutputTypeDef(BaseValidatorModel):
    status: str
    payload: LoaderIdResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ManagePropertygraphStatisticsOutputTypeDef(BaseValidatorModel):
    status: str
    payload: RefreshStatisticsIdMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ManageSparqlStatisticsOutputTypeDef(BaseValidatorModel):
    status: str
    payload: RefreshStatisticsIdMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PropertygraphSummaryTypeDef(BaseValidatorModel):
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

class PropertygraphRecordTypeDef(BaseValidatorModel):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: PropertygraphDataTypeDef
    op: str
    isLastOp: Optional[bool] = None

class RDFGraphSummaryTypeDef(BaseValidatorModel):
    numDistinctSubjects: Optional[int] = None
    numDistinctPredicates: Optional[int] = None
    numQuads: Optional[int] = None
    numClasses: Optional[int] = None
    classes: Optional[List[str]] = None
    predicates: Optional[List[Dict[str, int]]] = None
    subjectStructures: Optional[List[SubjectStructureTypeDef]] = None

class SparqlRecordTypeDef(BaseValidatorModel):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: SparqlDataTypeDef
    op: str
    isLastOp: Optional[bool] = None

class StatisticsTypeDef(BaseValidatorModel):
    autoCompute: Optional[bool] = None
    active: Optional[bool] = None
    statisticsId: Optional[str] = None
    date: Optional[datetime] = None
    note: Optional[str] = None
    signatureInfo: Optional[StatisticsSummaryTypeDef] = None

class ListGremlinQueriesOutputTypeDef(BaseValidatorModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenCypherQueriesOutputTypeDef(BaseValidatorModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PropertygraphSummaryValueMapTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[PropertygraphSummaryTypeDef] = None

class GetPropertygraphStreamOutputTypeDef(BaseValidatorModel):
    lastEventId: Dict[str, str]
    lastTrxTimestampInMillis: int
    format: str
    records: List[PropertygraphRecordTypeDef]
    totalRecords: int
    ResponseMetadata: ResponseMetadataTypeDef

class RDFGraphSummaryValueMapTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[RDFGraphSummaryTypeDef] = None

class GetSparqlStreamOutputTypeDef(BaseValidatorModel):
    lastEventId: Dict[str, str]
    lastTrxTimestampInMillis: int
    format: str
    records: List[SparqlRecordTypeDef]
    totalRecords: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetPropertygraphStatisticsOutputTypeDef(BaseValidatorModel):
    status: str
    payload: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSparqlStatisticsOutputTypeDef(BaseValidatorModel):
    status: str
    payload: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPropertygraphSummaryOutputTypeDef(BaseValidatorModel):
    statusCode: int
    payload: PropertygraphSummaryValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRDFGraphSummaryOutputTypeDef(BaseValidatorModel):
    statusCode: int
    payload: RDFGraphSummaryValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

