from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.neptunedata.neptunedata_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CancelGremlinQueryInput(BaseValidatorModel):
    queryId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelLoaderJobInput(BaseValidatorModel):
    loadId: str


class CancelMLDataProcessingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


class CancelMLModelTrainingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


class CancelMLModelTransformJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


class CancelOpenCypherQueryInput(BaseValidatorModel):
    queryId: str
    silent: Optional[bool] = None


class CreateMLEndpointInput(BaseValidatorModel):
    id: Optional[str] = None
    mlModelTrainingJobId: Optional[str] = None
    mlModelTransformJobId: Optional[str] = None
    update: Optional[bool] = None
    neptuneIamRoleArn: Optional[str] = None
    modelName: Optional[str] = None
    instanceType: Optional[str] = None
    instanceCount: Optional[int] = None
    volumeEncryptionKMSKey: Optional[str] = None


class CustomModelTrainingParameters(BaseValidatorModel):
    sourceS3DirectoryPath: str
    trainingEntryPointScript: Optional[str] = None
    transformEntryPointScript: Optional[str] = None


class CustomModelTransformParameters(BaseValidatorModel):
    sourceS3DirectoryPath: str
    transformEntryPointScript: Optional[str] = None


class DeleteMLEndpointInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


class DeleteStatisticsValueMap(BaseValidatorModel):
    active: Optional[bool] = None
    statisticsId: Optional[str] = None


class EdgeStructure(BaseValidatorModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None


class ExecuteFastResetInput(BaseValidatorModel):
    action: ActionType
    token: Optional[str] = None


class FastResetToken(BaseValidatorModel):
    token: Optional[str] = None


class ExecuteGremlinExplainQueryInput(BaseValidatorModel):
    gremlinQuery: str


class ExecuteGremlinProfileQueryInput(BaseValidatorModel):
    gremlinQuery: str
    results: Optional[bool] = None
    chop: Optional[int] = None
    serializer: Optional[str] = None
    indexOps: Optional[bool] = None


class ExecuteGremlinQueryInput(BaseValidatorModel):
    gremlinQuery: str
    serializer: Optional[str] = None


class GremlinQueryStatusAttributes(BaseValidatorModel):
    message: Optional[str] = None
    code: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None


class ExecuteOpenCypherExplainQueryInput(BaseValidatorModel):
    openCypherQuery: str
    explainMode: OpenCypherExplainModeType
    parameters: Optional[str] = None


class ExecuteOpenCypherQueryInput(BaseValidatorModel):
    openCypherQuery: str
    parameters: Optional[str] = None


class QueryLanguageVersion(BaseValidatorModel):
    version: str


class GetGremlinQueryStatusInput(BaseValidatorModel):
    queryId: str


class QueryEvalStats(BaseValidatorModel):
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    cancelled: Optional[bool] = None
    subqueries: Optional[Dict[str, Any]] = None


class GetLoaderJobStatusInput(BaseValidatorModel):
    loadId: str
    details: Optional[bool] = None
    errors: Optional[bool] = None
    page: Optional[int] = None
    errorsPerPage: Optional[int] = None


class GetMLDataProcessingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


class MlResourceDefinition(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[str] = None
    outputLocation: Optional[str] = None
    failureReason: Optional[str] = None
    cloudwatchLogUrl: Optional[str] = None


class GetMLEndpointInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


class MlConfigDefinition(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class GetMLModelTrainingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


class GetMLModelTransformJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


class GetOpenCypherQueryStatusInput(BaseValidatorModel):
    queryId: str


class GetPropertygraphStreamInput(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal['gzip']] = None


class GetPropertygraphSummaryInput(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


class GetRDFGraphSummaryInput(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


class GetSparqlStreamInput(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal['gzip']] = None


class ListGremlinQueriesInput(BaseValidatorModel):
    includeWaiting: Optional[bool] = None


class ListLoaderJobsInput(BaseValidatorModel):
    limit: Optional[int] = None
    includeQueuedLoads: Optional[bool] = None


class LoaderIdResult(BaseValidatorModel):
    loadIds: Optional[List[str]] = None


class ListMLDataProcessingJobsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListMLEndpointsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListMLModelTrainingJobsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListMLModelTransformJobsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListOpenCypherQueriesInput(BaseValidatorModel):
    includeWaiting: Optional[bool] = None


class ManagePropertygraphStatisticsInput(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None


class RefreshStatisticsIdMap(BaseValidatorModel):
    statisticsId: Optional[str] = None


class ManageSparqlStatisticsInput(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None


class NodeStructure(BaseValidatorModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None


class PropertygraphData(BaseValidatorModel):
    id: str
    type: str
    key: str
    value: Dict[str, Any]
    from_: Optional[str] = None
    to: Optional[str] = None


class SubjectStructure(BaseValidatorModel):
    count: Optional[int] = None
    predicates: Optional[List[str]] = None


class SparqlData(BaseValidatorModel):
    stmt: str


class StartLoaderJobInput(BaseValidatorModel):
    source: str
    format: FormatType
    s3BucketRegion: S3BucketRegionType
    iamRoleArn: str
    mode: Optional[ModeType] = None
    failOnError: Optional[bool] = None
    parallelism: Optional[ParallelismType] = None
    parserConfiguration: Optional[Dict[str, str]] = None
    updateSingleCardinalityProperties: Optional[bool] = None
    queueRequest: Optional[bool] = None
    dependencies: Optional[List[str]] = None
    userProvidedEdgeIds: Optional[bool] = None


class StartMLDataProcessingJobInput(BaseValidatorModel):
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
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    volumeEncryptionKMSKey: Optional[str] = None
    s3OutputEncryptionKMSKey: Optional[str] = None


class StatisticsSummary(BaseValidatorModel):
    signatureCount: Optional[int] = None
    instanceCount: Optional[int] = None
    predicateCount: Optional[int] = None


class CancelGremlinQueryOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class CancelLoaderJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class CancelMLDataProcessingJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class CancelMLModelTrainingJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class CancelMLModelTransformJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class CancelOpenCypherQueryOutput(BaseValidatorModel):
    status: str
    payload: bool
    ResponseMetadata: ResponseMetadata


class CreateMLEndpointOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


class DeleteMLEndpointOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class ExecuteGremlinExplainQueryOutput(BaseValidatorModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadata


class ExecuteGremlinProfileQueryOutput(BaseValidatorModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadata


class ExecuteOpenCypherExplainQueryOutput(BaseValidatorModel):
    results: StreamingBody
    ResponseMetadata: ResponseMetadata


class ExecuteOpenCypherQueryOutput(BaseValidatorModel):
    results: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


class GetLoaderJobStatusOutput(BaseValidatorModel):
    status: str
    payload: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


class ListMLDataProcessingJobsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


class ListMLEndpointsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


class ListMLModelTrainingJobsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


class ListMLModelTransformJobsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


class StartLoaderJobOutput(BaseValidatorModel):
    status: str
    payload: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartMLDataProcessingJobOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


class StartMLModelTrainingJobOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


class StartMLModelTransformJobOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


class StartMLModelTrainingJobInput(BaseValidatorModel):
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
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    volumeEncryptionKMSKey: Optional[str] = None
    s3OutputEncryptionKMSKey: Optional[str] = None
    enableManagedSpotTraining: Optional[bool] = None
    customModelTrainingParameters: Optional[CustomModelTrainingParameters] = None


class StartMLModelTransformJobInput(BaseValidatorModel):
    modelTransformOutputS3Location: str
    id: Optional[str] = None
    dataProcessingJobId: Optional[str] = None
    mlModelTrainingJobId: Optional[str] = None
    trainingJobName: Optional[str] = None
    sagemakerIamRoleArn: Optional[str] = None
    neptuneIamRoleArn: Optional[str] = None
    customModelTransformParameters: Optional[CustomModelTransformParameters] = None
    baseProcessingInstanceType: Optional[str] = None
    baseProcessingInstanceVolumeSizeInGB: Optional[int] = None
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    volumeEncryptionKMSKey: Optional[str] = None
    s3OutputEncryptionKMSKey: Optional[str] = None


class DeletePropertygraphStatisticsOutput(BaseValidatorModel):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMap
    ResponseMetadata: ResponseMetadata


class DeleteSparqlStatisticsOutput(BaseValidatorModel):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMap
    ResponseMetadata: ResponseMetadata


class ExecuteFastResetOutput(BaseValidatorModel):
    status: str
    payload: FastResetToken
    ResponseMetadata: ResponseMetadata


class ExecuteGremlinQueryOutput(BaseValidatorModel):
    requestId: str
    status: GremlinQueryStatusAttributes
    result: Dict[str, Any]
    meta: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


class GetEngineStatusOutput(BaseValidatorModel):
    status: str
    startTime: str
    dbEngineVersion: str
    role: str
    dfeQueryEngine: str
    gremlin: QueryLanguageVersion
    sparql: QueryLanguageVersion
    opencypher: QueryLanguageVersion
    labMode: Dict[str, str]
    rollingBackTrxCount: int
    rollingBackTrxEarliestStartTime: str
    features: Dict[str, Dict[str, Any]]
    settings: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetGremlinQueryStatusOutput(BaseValidatorModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStats
    ResponseMetadata: ResponseMetadata


class GetOpenCypherQueryStatusOutput(BaseValidatorModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStats
    ResponseMetadata: ResponseMetadata


class GremlinQueryStatus(BaseValidatorModel):
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    queryEvalStats: Optional[QueryEvalStats] = None


class GetMLDataProcessingJobOutput(BaseValidatorModel):
    status: str
    id: str
    processingJob: MlResourceDefinition
    ResponseMetadata: ResponseMetadata


class GetMLEndpointOutput(BaseValidatorModel):
    status: str
    id: str
    endpoint: MlResourceDefinition
    endpointConfig: MlConfigDefinition
    ResponseMetadata: ResponseMetadata


class GetMLModelTrainingJobOutput(BaseValidatorModel):
    status: str
    id: str
    processingJob: MlResourceDefinition
    hpoJob: MlResourceDefinition
    modelTransformJob: MlResourceDefinition
    mlModels: List[MlConfigDefinition]
    ResponseMetadata: ResponseMetadata


class GetMLModelTransformJobOutput(BaseValidatorModel):
    status: str
    id: str
    baseProcessingJob: MlResourceDefinition
    remoteModelTransformJob: MlResourceDefinition
    models: List[MlConfigDefinition]
    ResponseMetadata: ResponseMetadata


class ListLoaderJobsOutput(BaseValidatorModel):
    status: str
    payload: LoaderIdResult
    ResponseMetadata: ResponseMetadata


class ManagePropertygraphStatisticsOutput(BaseValidatorModel):
    status: str
    payload: RefreshStatisticsIdMap
    ResponseMetadata: ResponseMetadata


class ManageSparqlStatisticsOutput(BaseValidatorModel):
    status: str
    payload: RefreshStatisticsIdMap
    ResponseMetadata: ResponseMetadata


class PropertygraphSummary(BaseValidatorModel):
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
    nodeStructures: Optional[List[NodeStructure]] = None
    edgeStructures: Optional[List[EdgeStructure]] = None


class PropertygraphRecord(BaseValidatorModel):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: PropertygraphData
    op: str
    isLastOp: Optional[bool] = None


class RDFGraphSummary(BaseValidatorModel):
    numDistinctSubjects: Optional[int] = None
    numDistinctPredicates: Optional[int] = None
    numQuads: Optional[int] = None
    numClasses: Optional[int] = None
    classes: Optional[List[str]] = None
    predicates: Optional[List[Dict[str, int]]] = None
    subjectStructures: Optional[List[SubjectStructure]] = None


class SparqlRecord(BaseValidatorModel):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: SparqlData
    op: str
    isLastOp: Optional[bool] = None


class Statistics(BaseValidatorModel):
    autoCompute: Optional[bool] = None
    active: Optional[bool] = None
    statisticsId: Optional[str] = None
    date: Optional[datetime] = None
    note: Optional[str] = None
    signatureInfo: Optional[StatisticsSummary] = None


class ListGremlinQueriesOutput(BaseValidatorModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatus]
    ResponseMetadata: ResponseMetadata


class ListOpenCypherQueriesOutput(BaseValidatorModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatus]
    ResponseMetadata: ResponseMetadata


class PropertygraphSummaryValueMap(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[PropertygraphSummary] = None


class GetPropertygraphStreamOutput(BaseValidatorModel):
    lastEventId: Dict[str, str]
    lastTrxTimestampInMillis: int
    format: str
    records: List[PropertygraphRecord]
    totalRecords: int
    ResponseMetadata: ResponseMetadata


class RDFGraphSummaryValueMap(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[RDFGraphSummary] = None


class GetSparqlStreamOutput(BaseValidatorModel):
    lastEventId: Dict[str, str]
    lastTrxTimestampInMillis: int
    format: str
    records: List[SparqlRecord]
    totalRecords: int
    ResponseMetadata: ResponseMetadata


class GetPropertygraphStatisticsOutput(BaseValidatorModel):
    status: str
    payload: Statistics
    ResponseMetadata: ResponseMetadata


class GetSparqlStatisticsOutput(BaseValidatorModel):
    status: str
    payload: Statistics
    ResponseMetadata: ResponseMetadata


class GetPropertygraphSummaryOutput(BaseValidatorModel):
    statusCode: int
    payload: PropertygraphSummaryValueMap
    ResponseMetadata: ResponseMetadata


class GetRDFGraphSummaryOutput(BaseValidatorModel):
    statusCode: int
    payload: RDFGraphSummaryValueMap
    ResponseMetadata: ResponseMetadata