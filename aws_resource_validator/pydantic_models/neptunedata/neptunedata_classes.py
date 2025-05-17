from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.neptunedata.neptunedata_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'cancel_gremlin_query' function.
class CancelGremlinQueryInput(BaseValidatorModel):
    queryId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'cancel_loader_job' function.
class CancelLoaderJobInput(BaseValidatorModel):
    loadId: str


# This class is the input for the 'cancel_ml_data_processing_job' function.
class CancelMLDataProcessingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


# This class is the input for the 'cancel_ml_model_training_job' function.
class CancelMLModelTrainingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


# This class is the input for the 'cancel_ml_model_transform_job' function.
class CancelMLModelTransformJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None
    clean: Optional[bool] = None


# This class is the input for the 'cancel_open_cypher_query' function.
class CancelOpenCypherQueryInput(BaseValidatorModel):
    queryId: str
    silent: Optional[bool] = None


# This class is the input for the 'create_ml_endpoint' function.
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


# This class is the input for the 'delete_ml_endpoint' function.
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


# This class is the input for the 'execute_fast_reset' function.
class ExecuteFastResetInput(BaseValidatorModel):
    action: ActionType
    token: Optional[str] = None


class FastResetToken(BaseValidatorModel):
    token: Optional[str] = None


# This class is the input for the 'execute_gremlin_explain_query' function.
class ExecuteGremlinExplainQueryInput(BaseValidatorModel):
    gremlinQuery: str


# This class is the input for the 'execute_gremlin_profile_query' function.
class ExecuteGremlinProfileQueryInput(BaseValidatorModel):
    gremlinQuery: str
    results: Optional[bool] = None
    chop: Optional[int] = None
    serializer: Optional[str] = None
    indexOps: Optional[bool] = None


# This class is the input for the 'execute_gremlin_query' function.
class ExecuteGremlinQueryInput(BaseValidatorModel):
    gremlinQuery: str
    serializer: Optional[str] = None


class GremlinQueryStatusAttributes(BaseValidatorModel):
    message: Optional[str] = None
    code: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None


# This class is the input for the 'execute_open_cypher_explain_query' function.
class ExecuteOpenCypherExplainQueryInput(BaseValidatorModel):
    openCypherQuery: str
    explainMode: OpenCypherExplainModeType
    parameters: Optional[str] = None


# This class is the input for the 'execute_open_cypher_query' function.
class ExecuteOpenCypherQueryInput(BaseValidatorModel):
    openCypherQuery: str
    parameters: Optional[str] = None


class QueryLanguageVersion(BaseValidatorModel):
    version: str


# This class is the input for the 'get_gremlin_query_status' function.
class GetGremlinQueryStatusInput(BaseValidatorModel):
    queryId: str


class QueryEvalStats(BaseValidatorModel):
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    cancelled: Optional[bool] = None
    subqueries: Optional[Dict[str, Any]] = None


# This class is the input for the 'get_loader_job_status' function.
class GetLoaderJobStatusInput(BaseValidatorModel):
    loadId: str
    details: Optional[bool] = None
    errors: Optional[bool] = None
    page: Optional[int] = None
    errorsPerPage: Optional[int] = None


# This class is the input for the 'get_ml_data_processing_job' function.
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


# This class is the input for the 'get_ml_endpoint' function.
class GetMLEndpointInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


class MlConfigDefinition(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


# This class is the input for the 'get_ml_model_training_job' function.
class GetMLModelTrainingJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


# This class is the input for the 'get_ml_model_transform_job' function.
class GetMLModelTransformJobInput(BaseValidatorModel):
    id: str
    neptuneIamRoleArn: Optional[str] = None


# This class is the input for the 'get_open_cypher_query_status' function.
class GetOpenCypherQueryStatusInput(BaseValidatorModel):
    queryId: str


# This class is the input for the 'get_propertygraph_stream' function.
class GetPropertygraphStreamInput(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal['gzip']] = None


# This class is the input for the 'get_propertygraph_summary' function.
class GetPropertygraphSummaryInput(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


# This class is the input for the 'get_rdf_graph_summary' function.
class GetRDFGraphSummaryInput(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


# This class is the input for the 'get_sparql_stream' function.
class GetSparqlStreamInput(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal['gzip']] = None


# This class is the input for the 'list_gremlin_queries' function.
class ListGremlinQueriesInput(BaseValidatorModel):
    includeWaiting: Optional[bool] = None


# This class is the input for the 'list_loader_jobs' function.
class ListLoaderJobsInput(BaseValidatorModel):
    limit: Optional[int] = None
    includeQueuedLoads: Optional[bool] = None


class LoaderIdResult(BaseValidatorModel):
    loadIds: Optional[List[str]] = None


# This class is the input for the 'list_ml_data_processing_jobs' function.
class ListMLDataProcessingJobsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


# This class is the input for the 'list_ml_endpoints' function.
class ListMLEndpointsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


# This class is the input for the 'list_ml_model_training_jobs' function.
class ListMLModelTrainingJobsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


# This class is the input for the 'list_ml_model_transform_jobs' function.
class ListMLModelTransformJobsInput(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


# This class is the input for the 'list_open_cypher_queries' function.
class ListOpenCypherQueriesInput(BaseValidatorModel):
    includeWaiting: Optional[bool] = None


# This class is the input for the 'manage_propertygraph_statistics' function.
class ManagePropertygraphStatisticsInput(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None


class RefreshStatisticsIdMap(BaseValidatorModel):
    statisticsId: Optional[str] = None


# This class is the input for the 'manage_sparql_statistics' function.
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


# This class is the input for the 'start_loader_job' function.
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


# This class is the input for the 'start_ml_data_processing_job' function.
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


# This class is the output for the 'cancel_gremlin_query' function.
class CancelGremlinQueryOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_loader_job' function.
class CancelLoaderJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_ml_data_processing_job' function.
class CancelMLDataProcessingJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_ml_model_training_job' function.
class CancelMLModelTrainingJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_ml_model_transform_job' function.
class CancelMLModelTransformJobOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_open_cypher_query' function.
class CancelOpenCypherQueryOutput(BaseValidatorModel):
    status: str
    payload: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ml_endpoint' function.
class CreateMLEndpointOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ml_endpoint' function.
class DeleteMLEndpointOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_gremlin_explain_query' function.
class ExecuteGremlinExplainQueryOutput(BaseValidatorModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_gremlin_profile_query' function.
class ExecuteGremlinProfileQueryOutput(BaseValidatorModel):
    output: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_open_cypher_explain_query' function.
class ExecuteOpenCypherExplainQueryOutput(BaseValidatorModel):
    results: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_open_cypher_query' function.
class ExecuteOpenCypherQueryOutput(BaseValidatorModel):
    results: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_loader_job_status' function.
class GetLoaderJobStatusOutput(BaseValidatorModel):
    status: str
    payload: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ml_data_processing_jobs' function.
class ListMLDataProcessingJobsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ml_endpoints' function.
class ListMLEndpointsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ml_model_training_jobs' function.
class ListMLModelTrainingJobsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ml_model_transform_jobs' function.
class ListMLModelTransformJobsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_loader_job' function.
class StartLoaderJobOutput(BaseValidatorModel):
    status: str
    payload: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_ml_data_processing_job' function.
class StartMLDataProcessingJobOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_ml_model_training_job' function.
class StartMLModelTrainingJobOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_ml_model_transform_job' function.
class StartMLModelTransformJobOutput(BaseValidatorModel):
    id: str
    arn: str
    creationTimeInMillis: int
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_ml_model_training_job' function.
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


# This class is the input for the 'start_ml_model_transform_job' function.
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


# This class is the output for the 'execute_fast_reset' function.
class ExecuteFastResetOutput(BaseValidatorModel):
    status: str
    payload: FastResetToken
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_gremlin_query' function.
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


# This class is the output for the 'get_gremlin_query_status' function.
class GetGremlinQueryStatusOutput(BaseValidatorModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStats
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_open_cypher_query_status' function.
class GetOpenCypherQueryStatusOutput(BaseValidatorModel):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStats
    ResponseMetadata: ResponseMetadata


class GremlinQueryStatus(BaseValidatorModel):
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    queryEvalStats: Optional[QueryEvalStats] = None


# This class is the output for the 'get_ml_data_processing_job' function.
class GetMLDataProcessingJobOutput(BaseValidatorModel):
    status: str
    id: str
    processingJob: MlResourceDefinition
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ml_endpoint' function.
class GetMLEndpointOutput(BaseValidatorModel):
    status: str
    id: str
    endpoint: MlResourceDefinition
    endpointConfig: MlConfigDefinition
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ml_model_training_job' function.
class GetMLModelTrainingJobOutput(BaseValidatorModel):
    status: str
    id: str
    processingJob: MlResourceDefinition
    hpoJob: MlResourceDefinition
    modelTransformJob: MlResourceDefinition
    mlModels: List[MlConfigDefinition]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ml_model_transform_job' function.
class GetMLModelTransformJobOutput(BaseValidatorModel):
    status: str
    id: str
    baseProcessingJob: MlResourceDefinition
    remoteModelTransformJob: MlResourceDefinition
    models: List[MlConfigDefinition]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_loader_jobs' function.
class ListLoaderJobsOutput(BaseValidatorModel):
    status: str
    payload: LoaderIdResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'manage_propertygraph_statistics' function.
class ManagePropertygraphStatisticsOutput(BaseValidatorModel):
    status: str
    payload: RefreshStatisticsIdMap
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'manage_sparql_statistics' function.
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


# This class is the output for the 'list_gremlin_queries' function.
class ListGremlinQueriesOutput(BaseValidatorModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_open_cypher_queries' function.
class ListOpenCypherQueriesOutput(BaseValidatorModel):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatus]
    ResponseMetadata: ResponseMetadata


class PropertygraphSummaryValueMap(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[PropertygraphSummary] = None


# This class is the output for the 'get_propertygraph_stream' function.
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


# This class is the output for the 'get_sparql_stream' function.
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


# This class is the output for the 'get_propertygraph_summary' function.
class GetPropertygraphSummaryOutput(BaseValidatorModel):
    statusCode: int
    payload: PropertygraphSummaryValueMap
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rdf_graph_summary' function.
class GetRDFGraphSummaryOutput(BaseValidatorModel):
    statusCode: int
    payload: RDFGraphSummaryValueMap
    ResponseMetadata: ResponseMetadata