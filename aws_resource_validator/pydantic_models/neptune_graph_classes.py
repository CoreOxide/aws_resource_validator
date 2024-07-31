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
from aws_resource_validator.pydantic_models.neptune_graph_constants import *

class CancelImportTaskInputRequestTypeDef(BaseModel):
    taskIdentifier: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelQueryInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    queryId: str

class VectorSearchConfigurationTypeDef(BaseModel):
    dimension: int

class CreateGraphSnapshotInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    snapshotName: str
    tags: Optional[Mapping[str, str]] = None

class CreatePrivateGraphEndpointInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    vpcId: Optional[str] = None
    subnetIds: Optional[Sequence[str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None

class DeleteGraphInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    skipSnapshot: bool

class DeleteGraphSnapshotInputRequestTypeDef(BaseModel):
    snapshotIdentifier: str

class DeletePrivateGraphEndpointInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    vpcId: str

class EdgeStructureTypeDef(BaseModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None

class ExecuteQueryInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    queryString: str
    language: Literal["OPEN_CYPHER"]
    parameters: Optional[Mapping[str, Mapping[str, Any]]] = None
    planCache: Optional[PlanCacheTypeType] = None
    explainMode: Optional[ExplainModeType] = None
    queryTimeoutMilliseconds: Optional[int] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetGraphInputRequestTypeDef(BaseModel):
    graphIdentifier: str

class GetGraphSnapshotInputRequestTypeDef(BaseModel):
    snapshotIdentifier: str

class GetGraphSummaryInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    mode: Optional[GraphSummaryModeType] = None

class GetImportTaskInputRequestTypeDef(BaseModel):
    taskIdentifier: str

class ImportTaskDetailsTypeDef(BaseModel):
    status: str
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    errorCount: int
    statementCount: int
    dictionaryEntryCount: int
    errorDetails: Optional[str] = None

class GetPrivateGraphEndpointInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    vpcId: str

class GetQueryInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    queryId: str

class NodeStructureTypeDef(BaseModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None

class GraphSnapshotSummaryTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    sourceGraphId: Optional[str] = None
    snapshotCreateTime: Optional[datetime] = None
    status: Optional[SnapshotStatusType] = None
    kmsKeyIdentifier: Optional[str] = None

class GraphSummaryTypeDef(BaseModel):
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

class NeptuneImportOptionsTypeDef(BaseModel):
    s3ExportPath: str
    s3ExportKmsKeyId: str
    preserveDefaultVertexLabels: Optional[bool] = None
    preserveEdgeIds: Optional[bool] = None

class ImportTaskSummaryTypeDef(BaseModel):
    taskId: str
    source: str
    roleArn: str
    status: ImportTaskStatusType
    graphId: Optional[str] = None
    format: Optional[FormatType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListGraphSnapshotsInputRequestTypeDef(BaseModel):
    graphIdentifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListGraphsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListImportTasksInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPrivateGraphEndpointsInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PrivateGraphEndpointSummaryTypeDef(BaseModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: Optional[str] = None

class ListQueriesInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    maxResults: int
    state: Optional[QueryStateInputType] = None

class QuerySummaryTypeDef(BaseModel):
    id: Optional[str] = None
    queryString: Optional[str] = None
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    state: Optional[QueryStateType] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class ResetGraphInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    skipSnapshot: bool

class RestoreGraphFromSnapshotInputRequestTypeDef(BaseModel):
    snapshotIdentifier: str
    graphName: str
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    replicaCount: Optional[int] = None
    publicConnectivity: Optional[bool] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateGraphInputRequestTypeDef(BaseModel):
    graphIdentifier: str
    publicConnectivity: Optional[bool] = None
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None

class CancelImportTaskOutputTypeDef(BaseModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphSnapshotOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivateGraphEndpointOutputTypeDef(BaseModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGraphSnapshotOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePrivateGraphEndpointOutputTypeDef(BaseModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteQueryOutputTypeDef(BaseModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphSnapshotOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrivateGraphEndpointOutputTypeDef(BaseModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryOutputTypeDef(BaseModel):
    id: str
    queryString: str
    waited: int
    elapsed: int
    state: QueryStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphInputRequestTypeDef(BaseModel):
    graphName: str
    provisionedMemory: int
    tags: Optional[Mapping[str, str]] = None
    publicConnectivity: Optional[bool] = None
    kmsKeyIdentifier: Optional[str] = None
    vectorSearchConfiguration: Optional[VectorSearchConfigurationTypeDef] = None
    replicaCount: Optional[int] = None
    deletionProtection: Optional[bool] = None

class CreateGraphOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfigurationTypeDef
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGraphOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfigurationTypeDef
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfigurationTypeDef
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetGraphOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfigurationTypeDef
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreGraphFromSnapshotOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfigurationTypeDef
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGraphOutputTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    status: GraphStatusType
    statusReason: str
    createTime: datetime
    provisionedMemory: int
    endpoint: str
    publicConnectivity: bool
    vectorSearchConfiguration: VectorSearchConfigurationTypeDef
    replicaCount: int
    kmsKeyIdentifier: str
    sourceSnapshotId: str
    deletionProtection: bool
    buildNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphInputGraphAvailableWaitTypeDef(BaseModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetGraphInputGraphDeletedWaitTypeDef(BaseModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetGraphSnapshotInputGraphSnapshotAvailableWaitTypeDef(BaseModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetGraphSnapshotInputGraphSnapshotDeletedWaitTypeDef(BaseModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetImportTaskInputImportTaskCancelledWaitTypeDef(BaseModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetImportTaskInputImportTaskSuccessfulWaitTypeDef(BaseModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPrivateGraphEndpointInputPrivateGraphEndpointAvailableWaitTypeDef(BaseModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPrivateGraphEndpointInputPrivateGraphEndpointDeletedWaitTypeDef(BaseModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GraphDataSummaryTypeDef(BaseModel):
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

class ListGraphSnapshotsOutputTypeDef(BaseModel):
    graphSnapshots: List[GraphSnapshotSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphsOutputTypeDef(BaseModel):
    graphs: List[GraphSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportOptionsTypeDef(BaseModel):
    neptune: Optional[NeptuneImportOptionsTypeDef] = None

class ListImportTasksOutputTypeDef(BaseModel):
    tasks: List[ImportTaskSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphSnapshotsInputListGraphSnapshotsPaginateTypeDef(BaseModel):
    graphIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGraphsInputListGraphsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportTasksInputListImportTasksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivateGraphEndpointsInputListPrivateGraphEndpointsPaginateTypeDef(BaseModel):
    graphIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivateGraphEndpointsOutputTypeDef(BaseModel):
    privateGraphEndpoints: List[PrivateGraphEndpointSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueriesOutputTypeDef(BaseModel):
    queries: List[QuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphSummaryOutputTypeDef(BaseModel):
    version: str
    lastStatisticsComputationTime: datetime
    graphSummary: GraphDataSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphUsingImportTaskInputRequestTypeDef(BaseModel):
    graphName: str
    source: str
    roleArn: str
    tags: Optional[Mapping[str, str]] = None
    publicConnectivity: Optional[bool] = None
    kmsKeyIdentifier: Optional[str] = None
    vectorSearchConfiguration: Optional[VectorSearchConfigurationTypeDef] = None
    replicaCount: Optional[int] = None
    deletionProtection: Optional[bool] = None
    importOptions: Optional[ImportOptionsTypeDef] = None
    maxProvisionedMemory: Optional[int] = None
    minProvisionedMemory: Optional[int] = None
    failOnError: Optional[bool] = None
    format: Optional[FormatType] = None

class CreateGraphUsingImportTaskOutputTypeDef(BaseModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportTaskOutputTypeDef(BaseModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptionsTypeDef
    importTaskDetails: ImportTaskDetailsTypeDef
    attemptNumber: int
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportTaskInputRequestTypeDef(BaseModel):
    source: str
    graphIdentifier: str
    roleArn: str
    importOptions: Optional[ImportOptionsTypeDef] = None
    failOnError: Optional[bool] = None
    format: Optional[FormatType] = None

class StartImportTaskOutputTypeDef(BaseModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

