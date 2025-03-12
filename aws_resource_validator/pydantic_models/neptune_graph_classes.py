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
from aws_resource_validator.pydantic_models.neptune_graph_constants import *

class CancelExportTaskInputTypeDef(BaseValidatorModel):
    taskIdentifier: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelImportTaskInputTypeDef(BaseValidatorModel):
    taskIdentifier: str


class CancelQueryInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    queryId: str


class VectorSearchConfigurationTypeDef(BaseValidatorModel):
    dimension: int


class CreateGraphSnapshotInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    snapshotName: str
    tags: Optional[Mapping[str, str]] = None


class CreatePrivateGraphEndpointInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: Optional[str] = None
    subnetIds: Optional[Sequence[str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None


class DeleteGraphInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    skipSnapshot: bool


class DeleteGraphSnapshotInputTypeDef(BaseValidatorModel):
    snapshotIdentifier: str


class DeletePrivateGraphEndpointInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str


class EdgeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None


class ExecuteQueryInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    queryString: str
    language: Literal["OPEN_CYPHER"]
    parameters: Optional[Mapping[str, Mapping[str, Any]]] = None
    planCache: Optional[PlanCacheTypeType] = None
    explainMode: Optional[ExplainModeType] = None
    queryTimeoutMilliseconds: Optional[int] = None


class ExportFilterPropertyAttributesTypeDef(BaseValidatorModel):
    outputType: Optional[str] = None
    sourcePropertyName: Optional[str] = None
    multiValueHandling: Optional[MultiValueHandlingTypeType] = None


class ExportTaskDetailsTypeDef(BaseValidatorModel):
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    numVerticesWritten: Optional[int] = None
    numEdgesWritten: Optional[int] = None


class GetExportTaskInputTypeDef(BaseValidatorModel):
    taskIdentifier: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetGraphInputTypeDef(BaseValidatorModel):
    graphIdentifier: str


class GetGraphSnapshotInputTypeDef(BaseValidatorModel):
    snapshotIdentifier: str


class GetGraphSummaryInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    mode: Optional[GraphSummaryModeType] = None


class GetImportTaskInputTypeDef(BaseValidatorModel):
    taskIdentifier: str


class ImportTaskDetailsTypeDef(BaseValidatorModel):
    status: str
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    errorCount: int
    statementCount: int
    dictionaryEntryCount: int
    errorDetails: Optional[str] = None


class GetPrivateGraphEndpointInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str


class GetQueryInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    queryId: str


class NodeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None


class NeptuneImportOptionsTypeDef(BaseValidatorModel):
    s3ExportPath: str
    s3ExportKmsKeyId: str
    preserveDefaultVertexLabels: Optional[bool] = None
    preserveEdgeIds: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListExportTasksInputTypeDef(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGraphSnapshotsInputTypeDef(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGraphsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListImportTasksInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPrivateGraphEndpointsInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PrivateGraphEndpointSummaryTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: Optional[str] = None


class ListQueriesInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    maxResults: int
    state: Optional[QueryStateInputType] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class ResetGraphInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    skipSnapshot: bool


class RestoreGraphFromSnapshotInputTypeDef(BaseValidatorModel):
    snapshotIdentifier: str
    graphName: str
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    replicaCount: Optional[int] = None
    publicConnectivity: Optional[bool] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateGraphInputTypeDef(BaseValidatorModel):
    graphIdentifier: str
    publicConnectivity: Optional[bool] = None
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None


class CreatePrivateGraphEndpointOutputTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePrivateGraphEndpointOutputTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExecuteQueryOutputTypeDef(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetPrivateGraphEndpointOutputTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGraphInputTypeDef(BaseValidatorModel):
    graphName: str
    provisionedMemory: int
    tags: Optional[Mapping[str, str]] = None
    publicConnectivity: Optional[bool] = None
    kmsKeyIdentifier: Optional[str] = None
    vectorSearchConfiguration: Optional[VectorSearchConfigurationTypeDef] = None
    replicaCount: Optional[int] = None
    deletionProtection: Optional[bool] = None


class ExportFilterElementOutputTypeDef(BaseValidatorModel):
    properties: Optional[Dict[str, ExportFilterPropertyAttributesTypeDef]] = None


class ExportFilterElementTypeDef(BaseValidatorModel):
    properties: Optional[Mapping[str, ExportFilterPropertyAttributesTypeDef]] = None


class ExportTaskSummaryTypeDef(BaseValidatorModel):
    pass


class ListExportTasksOutputTypeDef(BaseValidatorModel):
    tasks: List[ExportTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetExportTaskInputWaitExtraTypeDef(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetExportTaskInputWaitTypeDef(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetGraphInputWaitExtraTypeDef(BaseValidatorModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetGraphInputWaitTypeDef(BaseValidatorModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetGraphSnapshotInputWaitExtraTypeDef(BaseValidatorModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetGraphSnapshotInputWaitTypeDef(BaseValidatorModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetImportTaskInputWaitExtraTypeDef(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetImportTaskInputWaitTypeDef(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetPrivateGraphEndpointInputWaitExtraTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetPrivateGraphEndpointInputWaitTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GraphDataSummaryTypeDef(BaseValidatorModel):
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


class GraphSnapshotSummaryTypeDef(BaseValidatorModel):
    pass


class ListGraphSnapshotsOutputTypeDef(BaseValidatorModel):
    graphSnapshots: List[GraphSnapshotSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GraphSummaryTypeDef(BaseValidatorModel):
    pass


class ListGraphsOutputTypeDef(BaseValidatorModel):
    graphs: List[GraphSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImportOptionsTypeDef(BaseValidatorModel):
    neptune: Optional[NeptuneImportOptionsTypeDef] = None


class ImportTaskSummaryTypeDef(BaseValidatorModel):
    pass


class ListImportTasksOutputTypeDef(BaseValidatorModel):
    tasks: List[ImportTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListExportTasksInputPaginateTypeDef(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGraphSnapshotsInputPaginateTypeDef(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGraphsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportTasksInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrivateGraphEndpointsInputPaginateTypeDef(BaseValidatorModel):
    graphIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrivateGraphEndpointsOutputTypeDef(BaseValidatorModel):
    privateGraphEndpoints: List[PrivateGraphEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class QuerySummaryTypeDef(BaseValidatorModel):
    pass


class ListQueriesOutputTypeDef(BaseValidatorModel):
    queries: List[QuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExportFilterOutputTypeDef(BaseValidatorModel):
    vertexFilter: Optional[Dict[str, ExportFilterElementOutputTypeDef]] = None
    edgeFilter: Optional[Dict[str, ExportFilterElementOutputTypeDef]] = None


class ExportFilterTypeDef(BaseValidatorModel):
    vertexFilter: Optional[Mapping[str, ExportFilterElementTypeDef]] = None
    edgeFilter: Optional[Mapping[str, ExportFilterElementTypeDef]] = None


class GetGraphSummaryOutputTypeDef(BaseValidatorModel):
    version: str
    lastStatisticsComputationTime: datetime
    graphSummary: GraphDataSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


