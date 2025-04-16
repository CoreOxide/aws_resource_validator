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
from aws_resource_validator.pydantic_models.neptunedata_constants import *

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


class CancelOpenCypherQueryInput(BaseValidatorModel):
    queryId: str
    silent: Optional[bool] = None


class CustomModelTrainingParameters(BaseValidatorModel):
    sourceS3DirectoryPath: str
    trainingEntryPointScript: Optional[str] = None
    transformEntryPointScript: Optional[str] = None


class CustomModelTransformParameters(BaseValidatorModel):
    sourceS3DirectoryPath: str
    transformEntryPointScript: Optional[str] = None


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


class MlResourceDefinition(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[str] = None
    outputLocation: Optional[str] = None
    failureReason: Optional[str] = None
    cloudwatchLogUrl: Optional[str] = None


class MlConfigDefinition(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class GetOpenCypherQueryStatusInput(BaseValidatorModel):
    queryId: str


class GetPropertygraphStreamInput(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None


class GetPropertygraphSummaryInput(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


class GetRDFGraphSummaryInput(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


class GetSparqlStreamInput(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None


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


class SubjectStructure(BaseValidatorModel):
    count: Optional[int] = None
    predicates: Optional[List[str]] = None


class SparqlData(BaseValidatorModel):
    stmt: str


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


class PropertygraphData(BaseValidatorModel):
    pass


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


class RDFGraphSummaryValueMap(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[RDFGraphSummary] = None


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


