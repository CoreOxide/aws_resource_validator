from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CancelExportTaskInput(BaseValidatorModel):
    taskIdentifier: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelImportTaskInput(BaseValidatorModel):
    taskIdentifier: str


class CancelQueryInput(BaseValidatorModel):
    graphIdentifier: str
    queryId: str


class VectorSearchConfiguration(BaseValidatorModel):
    dimension: int


class CreateGraphSnapshotInput(BaseValidatorModel):
    graphIdentifier: str
    snapshotName: str
    tags: Optional[Dict[str, str]] = None


class CreatePrivateGraphEndpointInput(BaseValidatorModel):
    graphIdentifier: str
    vpcId: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    vpcSecurityGroupIds: Optional[List[str]] = None


class DeleteGraphInput(BaseValidatorModel):
    graphIdentifier: str
    skipSnapshot: bool


class DeleteGraphSnapshotInput(BaseValidatorModel):
    snapshotIdentifier: str


class DeletePrivateGraphEndpointInput(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str


class EdgeStructure(BaseValidatorModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None


class ExecuteQueryInput(BaseValidatorModel):
    graphIdentifier: str
    queryString: str
    language: Literal['OPEN_CYPHER']
    parameters: Optional[Dict[str, Dict[str, Any]]] = None
    planCache: Optional[PlanCacheTypeType] = None
    explainMode: Optional[ExplainModeType] = None
    queryTimeoutMilliseconds: Optional[int] = None


class ExportFilterPropertyAttributes(BaseValidatorModel):
    outputType: Optional[str] = None
    sourcePropertyName: Optional[str] = None
    multiValueHandling: Optional[MultiValueHandlingTypeType] = None


class ExportTaskDetails(BaseValidatorModel):
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    numVerticesWritten: Optional[int] = None
    numEdgesWritten: Optional[int] = None


class ExportTaskSummary(BaseValidatorModel):
    graphId: str
    roleArn: str
    taskId: str
    status: ExportTaskStatusType
    format: ExportFormatType
    destination: str
    kmsKeyIdentifier: str
    parquetType: Optional[Literal['COLUMNAR']] = None
    statusReason: Optional[str] = None


class GetExportTaskInput(BaseValidatorModel):
    taskIdentifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetGraphInput(BaseValidatorModel):
    graphIdentifier: str


class GetGraphSnapshotInput(BaseValidatorModel):
    snapshotIdentifier: str


class GetGraphSummaryInput(BaseValidatorModel):
    graphIdentifier: str
    mode: Optional[GraphSummaryModeType] = None


class GetImportTaskInput(BaseValidatorModel):
    taskIdentifier: str


class ImportTaskDetails(BaseValidatorModel):
    status: str
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    errorCount: int
    statementCount: int
    dictionaryEntryCount: int
    errorDetails: Optional[str] = None


class GetPrivateGraphEndpointInput(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str


class GetQueryInput(BaseValidatorModel):
    graphIdentifier: str
    queryId: str


class NodeStructure(BaseValidatorModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None


class GraphSnapshotSummary(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: Optional[str] = None
    snapshotCreateTime: Optional[datetime] = None
    status: Optional[SnapshotStatusType] = None
    kmsKeyIdentifier: Optional[str] = None


class GraphSummary(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: Optional[GraphStatusType] = None
    provisionedMemory: Optional[int] = None
    publicConnectivity: Optional[bool] = None
    endpoint: Optional[str] = None
    replicaCount: Optional[int] = None
    kmsKeyIdentifier: Optional[str] = None
    deletionProtection: Optional[bool] = None


class NeptuneImportOptions(BaseValidatorModel):
    s3ExportPath: str
    s3ExportKmsKeyId: str
    preserveDefaultVertexLabels: Optional[bool] = None
    preserveEdgeIds: Optional[bool] = None


class ImportTaskSummary(BaseValidatorModel):
    taskId: str
    source: str
    roleArn: str
    status: ImportTaskStatusType
    graphId: Optional[str] = None
    format: Optional[FormatType] = None
    parquetType: Optional[Literal['COLUMNAR']] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListExportTasksInput(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGraphSnapshotsInput(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGraphsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListImportTasksInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPrivateGraphEndpointsInput(BaseValidatorModel):
    graphIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PrivateGraphEndpointSummary(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: Optional[str] = None


class ListQueriesInput(BaseValidatorModel):
    graphIdentifier: str
    maxResults: int
    state: Optional[QueryStateInputType] = None


class QuerySummary(BaseValidatorModel):
    id: Optional[str] = None
    queryString: Optional[str] = None
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    state: Optional[QueryStateType] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class ResetGraphInput(BaseValidatorModel):
    graphIdentifier: str
    skipSnapshot: bool


class RestoreGraphFromSnapshotInput(BaseValidatorModel):
    snapshotIdentifier: str
    graphName: str
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    replicaCount: Optional[int] = None
    publicConnectivity: Optional[bool] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateGraphInput(BaseValidatorModel):
    graphIdentifier: str
    publicConnectivity: Optional[bool] = None
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None


class CancelExportTaskOutput(BaseValidatorModel):
    graphId: str
    roleArn: str
    taskId: str
    status: ExportTaskStatusType
    format: ExportFormatType
    destination: str
    kmsKeyIdentifier: str
    parquetType: Literal['COLUMNAR']
    statusReason: str
    ResponseMetadata: ResponseMetadata


class CancelImportTaskOutput(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    parquetType: Literal['COLUMNAR']
    roleArn: str
    status: ImportTaskStatusType
    ResponseMetadata: ResponseMetadata


class CreateGraphSnapshotOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadata


class CreatePrivateGraphEndpointOutput(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadata


class DeleteGraphSnapshotOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadata


class DeletePrivateGraphEndpointOutput(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExecuteQueryOutput(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetGraphSnapshotOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadata


class GetPrivateGraphEndpointOutput(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadata


class GetQueryOutput(BaseValidatorModel):
    id: str
    queryString: str
    waited: int
    elapsed: int
    state: QueryStateType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateGraphInput(BaseValidatorModel):
    graphName: str
    provisionedMemory: int
    tags: Optional[Dict[str, str]] = None
    publicConnectivity: Optional[bool] = None
    kmsKeyIdentifier: Optional[str] = None
    vectorSearchConfiguration: Optional[VectorSearchConfiguration] = None
    replicaCount: Optional[int] = None
    deletionProtection: Optional[bool] = None


class CreateGraphOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfiguration
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadata


class DeleteGraphOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfiguration
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadata


class GetGraphOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfiguration
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadata


class ResetGraphOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfiguration
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadata


class RestoreGraphFromSnapshotOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfiguration
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadata


class UpdateGraphOutput(BaseValidatorModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfiguration
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadata


class ExportFilterElementOutput(BaseValidatorModel):
    properties: Optional[Dict[str, ExportFilterPropertyAttributes]] = None


class ExportFilterElement(BaseValidatorModel):
    properties: Optional[Dict[str, ExportFilterPropertyAttributes]] = None


class ListExportTasksOutput(BaseValidatorModel):
    tasks: List[ExportTaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetExportTaskInputWaitExtra(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetExportTaskInputWait(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetGraphInputWaitExtra(BaseValidatorModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetGraphInputWait(BaseValidatorModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetGraphSnapshotInputWaitExtra(BaseValidatorModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetGraphSnapshotInputWait(BaseValidatorModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetImportTaskInputWaitExtra(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetImportTaskInputWait(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetPrivateGraphEndpointInputWaitExtra(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetPrivateGraphEndpointInputWait(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GraphDataSummary(BaseValidatorModel):
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


class ListGraphSnapshotsOutput(BaseValidatorModel):
    graphSnapshots: List[GraphSnapshotSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListGraphsOutput(BaseValidatorModel):
    graphs: List[GraphSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImportOptions(BaseValidatorModel):
    neptune: Optional[NeptuneImportOptions] = None


class ListImportTasksOutput(BaseValidatorModel):
    tasks: List[ImportTaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListExportTasksInputPaginate(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGraphSnapshotsInputPaginate(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGraphsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportTasksInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrivateGraphEndpointsInputPaginate(BaseValidatorModel):
    graphIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrivateGraphEndpointsOutput(BaseValidatorModel):
    privateGraphEndpoints: List[PrivateGraphEndpointSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQueriesOutput(BaseValidatorModel):
    queries: List[QuerySummary]
    ResponseMetadata: ResponseMetadata


class ExportFilterOutput(BaseValidatorModel):
    vertexFilter: Optional[Dict[str, ExportFilterElementOutput]] = None
    edgeFilter: Optional[Dict[str, ExportFilterElementOutput]] = None


class ExportFilter(BaseValidatorModel):
    vertexFilter: Optional[Dict[str, ExportFilterElement]] = None
    edgeFilter: Optional[Dict[str, ExportFilterElement]] = None


class GetGraphSummaryOutput(BaseValidatorModel):
    version: str
    lastStatisticsComputationTime: datetime
    graphSummary: GraphDataSummary
    ResponseMetadata: ResponseMetadata


class CreateGraphUsingImportTaskInput(BaseValidatorModel):
    graphName: str
    source: str
    roleArn: str
    tags: Optional[Dict[str, str]] = None
    publicConnectivity: Optional[bool] = None
    kmsKeyIdentifier: Optional[str] = None
    vectorSearchConfiguration: Optional[VectorSearchConfiguration] = None
    replicaCount: Optional[int] = None
    deletionProtection: Optional[bool] = None
    importOptions: Optional[ImportOptions] = None
    maxProvisionedMemory: Optional[int] = None
    minProvisionedMemory: Optional[int] = None
    failOnError: Optional[bool] = None
    format: Optional[FormatType] = None
    parquetType: Optional[Literal['COLUMNAR']] = None
    blankNodeHandling: Optional[Literal['convertToIri']] = None


class CreateGraphUsingImportTaskOutput(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    parquetType: Literal['COLUMNAR']
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptions
    ResponseMetadata: ResponseMetadata


class GetImportTaskOutput(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    parquetType: Literal['COLUMNAR']
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptions
    importTaskDetails: ImportTaskDetails
    attemptNumber: int
    statusReason: str
    ResponseMetadata: ResponseMetadata


class StartImportTaskInput(BaseValidatorModel):
    source: str
    graphIdentifier: str
    roleArn: str
    importOptions: Optional[ImportOptions] = None
    failOnError: Optional[bool] = None
    format: Optional[FormatType] = None
    parquetType: Optional[Literal['COLUMNAR']] = None
    blankNodeHandling: Optional[Literal['convertToIri']] = None


class StartImportTaskOutput(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    parquetType: Literal['COLUMNAR']
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptions
    ResponseMetadata: ResponseMetadata


class GetExportTaskOutput(BaseValidatorModel):
    graphId: str
    roleArn: str
    taskId: str
    status: ExportTaskStatusType
    format: ExportFormatType
    destination: str
    kmsKeyIdentifier: str
    parquetType: Literal['COLUMNAR']
    statusReason: str
    exportTaskDetails: ExportTaskDetails
    exportFilter: ExportFilterOutput
    ResponseMetadata: ResponseMetadata


class StartExportTaskOutput(BaseValidatorModel):
    graphId: str
    roleArn: str
    taskId: str
    status: ExportTaskStatusType
    format: ExportFormatType
    destination: str
    kmsKeyIdentifier: str
    parquetType: Literal['COLUMNAR']
    statusReason: str
    exportFilter: ExportFilterOutput
    ResponseMetadata: ResponseMetadata

ExportFilterUnion = Union[ExportFilter, ExportFilterOutput]


class StartExportTaskInput(BaseValidatorModel):
    graphIdentifier: str
    roleArn: str
    format: ExportFormatType
    destination: str
    kmsKeyIdentifier: str
    parquetType: Optional[Literal['COLUMNAR']] = None
    exportFilter: Optional[ExportFilterUnion] = None
    tags: Optional[Dict[str, str]] = None