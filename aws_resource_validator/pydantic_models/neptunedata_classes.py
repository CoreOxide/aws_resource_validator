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

class CancelGremlinQueryInputTypeDef(BaseValidatorModel):
    queryId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelLoaderJobInputTypeDef(BaseValidatorModel):
    loadId: str


class CancelOpenCypherQueryInputTypeDef(BaseValidatorModel):
    queryId: str
    silent: Optional[bool] = None


class CustomModelTrainingParametersTypeDef(BaseValidatorModel):
    sourceS3DirectoryPath: str
    trainingEntryPointScript: Optional[str] = None
    transformEntryPointScript: Optional[str] = None


class CustomModelTransformParametersTypeDef(BaseValidatorModel):
    sourceS3DirectoryPath: str
    transformEntryPointScript: Optional[str] = None


class DeleteStatisticsValueMapTypeDef(BaseValidatorModel):
    active: Optional[bool] = None
    statisticsId: Optional[str] = None


class EdgeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None


class ExecuteFastResetInputTypeDef(BaseValidatorModel):
    action: ActionType
    token: Optional[str] = None


class FastResetTokenTypeDef(BaseValidatorModel):
    token: Optional[str] = None


class ExecuteGremlinExplainQueryInputTypeDef(BaseValidatorModel):
    gremlinQuery: str


class ExecuteGremlinProfileQueryInputTypeDef(BaseValidatorModel):
    gremlinQuery: str
    results: Optional[bool] = None
    chop: Optional[int] = None
    serializer: Optional[str] = None
    indexOps: Optional[bool] = None


class ExecuteGremlinQueryInputTypeDef(BaseValidatorModel):
    gremlinQuery: str
    serializer: Optional[str] = None


class GremlinQueryStatusAttributesTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    code: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None


class ExecuteOpenCypherExplainQueryInputTypeDef(BaseValidatorModel):
    openCypherQuery: str
    explainMode: OpenCypherExplainModeType
    parameters: Optional[str] = None


class ExecuteOpenCypherQueryInputTypeDef(BaseValidatorModel):
    openCypherQuery: str
    parameters: Optional[str] = None


class QueryLanguageVersionTypeDef(BaseValidatorModel):
    version: str


class GetGremlinQueryStatusInputTypeDef(BaseValidatorModel):
    queryId: str


class QueryEvalStatsTypeDef(BaseValidatorModel):
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    cancelled: Optional[bool] = None
    subqueries: Optional[Dict[str, Any]] = None


class GetLoaderJobStatusInputTypeDef(BaseValidatorModel):
    loadId: str
    details: Optional[bool] = None
    errors: Optional[bool] = None
    page: Optional[int] = None
    errorsPerPage: Optional[int] = None


class MlResourceDefinitionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[str] = None
    outputLocation: Optional[str] = None
    failureReason: Optional[str] = None
    cloudwatchLogUrl: Optional[str] = None


class MlConfigDefinitionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class GetOpenCypherQueryStatusInputTypeDef(BaseValidatorModel):
    queryId: str


class GetPropertygraphStreamInputTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None


class GetPropertygraphSummaryInputTypeDef(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


class GetRDFGraphSummaryInputTypeDef(BaseValidatorModel):
    mode: Optional[GraphSummaryTypeType] = None


class GetSparqlStreamInputTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    iteratorType: Optional[IteratorTypeType] = None
    commitNum: Optional[int] = None
    opNum: Optional[int] = None
    encoding: Optional[Literal["gzip"]] = None


class ListGremlinQueriesInputTypeDef(BaseValidatorModel):
    includeWaiting: Optional[bool] = None


class ListLoaderJobsInputTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    includeQueuedLoads: Optional[bool] = None


class LoaderIdResultTypeDef(BaseValidatorModel):
    loadIds: Optional[List[str]] = None


class ListMLDataProcessingJobsInputTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListMLEndpointsInputTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListMLModelTrainingJobsInputTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListMLModelTransformJobsInputTypeDef(BaseValidatorModel):
    maxItems: Optional[int] = None
    neptuneIamRoleArn: Optional[str] = None


class ListOpenCypherQueriesInputTypeDef(BaseValidatorModel):
    includeWaiting: Optional[bool] = None


class ManagePropertygraphStatisticsInputTypeDef(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None


class RefreshStatisticsIdMapTypeDef(BaseValidatorModel):
    statisticsId: Optional[str] = None


class ManageSparqlStatisticsInputTypeDef(BaseValidatorModel):
    mode: Optional[StatisticsAutoGenerationModeType] = None


class NodeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None


class SubjectStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    predicates: Optional[List[str]] = None


class SparqlDataTypeDef(BaseValidatorModel):
    stmt: str


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


class PropertygraphDataTypeDef(BaseValidatorModel):
    pass


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


class RDFGraphSummaryValueMapTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    lastStatisticsComputationTime: Optional[datetime] = None
    graphSummary: Optional[RDFGraphSummaryTypeDef] = None


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


