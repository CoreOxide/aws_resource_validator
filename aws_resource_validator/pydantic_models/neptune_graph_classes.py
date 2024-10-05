from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.neptune_graph_constants import *

class CancelImportTaskInputRequestTypeDef(BaseValidatorModel):
    taskIdentifier: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelQueryInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    queryId: str

class VectorSearchConfigurationTypeDef(BaseValidatorModel):
    dimension: int

class CreateGraphSnapshotInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    snapshotName: str
    tags: Optional[Mapping[str, str]] = None

class CreatePrivateGraphEndpointInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: Optional[str] = None
    subnetIds: Optional[Sequence[str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None

class DeleteGraphInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    skipSnapshot: bool

class DeleteGraphSnapshotInputRequestTypeDef(BaseValidatorModel):
    snapshotIdentifier: str

class DeletePrivateGraphEndpointInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str

class EdgeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    edgeProperties: Optional[List[str]] = None

class ExecuteQueryInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    queryString: str
    language: Literal["OPEN_CYPHER"]
    parameters: Optional[Mapping[str, Mapping[str, Any]]] = None
    planCache: Optional[PlanCacheTypeType] = None
    explainMode: Optional[ExplainModeType] = None
    queryTimeoutMilliseconds: Optional[int] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetGraphInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str

class GetGraphSnapshotInputRequestTypeDef(BaseValidatorModel):
    snapshotIdentifier: str

class GetGraphSummaryInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    mode: Optional[GraphSummaryModeType] = None

class GetImportTaskInputRequestTypeDef(BaseValidatorModel):
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

class GetPrivateGraphEndpointInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str

class GetQueryInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    queryId: str

class NodeStructureTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    nodeProperties: Optional[List[str]] = None
    distinctOutgoingEdgeLabels: Optional[List[str]] = None

class GraphSnapshotSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: Optional[str] = None
    snapshotCreateTime: Optional[datetime] = None
    status: Optional[SnapshotStatusType] = None
    kmsKeyIdentifier: Optional[str] = None

class GraphSummaryTypeDef(BaseValidatorModel):
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

class NeptuneImportOptionsTypeDef(BaseValidatorModel):
    s3ExportPath: str
    s3ExportKmsKeyId: str
    preserveDefaultVertexLabels: Optional[bool] = None
    preserveEdgeIds: Optional[bool] = None

class ImportTaskSummaryTypeDef(BaseValidatorModel):
    taskId: str
    source: str
    roleArn: str
    status: ImportTaskStatusType
    graphId: Optional[str] = None
    format: Optional[FormatType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListGraphSnapshotsInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListGraphsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListImportTasksInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPrivateGraphEndpointsInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PrivateGraphEndpointSummaryTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: Optional[str] = None

class ListQueriesInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    maxResults: int
    state: Optional[QueryStateInputType] = None

class QuerySummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    queryString: Optional[str] = None
    waited: Optional[int] = None
    elapsed: Optional[int] = None
    state: Optional[QueryStateType] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResetGraphInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    skipSnapshot: bool

class RestoreGraphFromSnapshotInputRequestTypeDef(BaseValidatorModel):
    snapshotIdentifier: str
    graphName: str
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    replicaCount: Optional[int] = None
    publicConnectivity: Optional[bool] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateGraphInputRequestTypeDef(BaseValidatorModel):
    graphIdentifier: str
    publicConnectivity: Optional[bool] = None
    provisionedMemory: Optional[int] = None
    deletionProtection: Optional[bool] = None

class CancelImportTaskOutputTypeDef(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphSnapshotOutputTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivateGraphEndpointOutputTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGraphSnapshotOutputTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
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

class GetGraphSnapshotOutputTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    sourceGraphId: str
    snapshotCreateTime: datetime
    status: SnapshotStatusType
    kmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrivateGraphEndpointOutputTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryOutputTypeDef(BaseValidatorModel):
    id: str
    queryString: str
    waited: int
    elapsed: int
    state: QueryStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphInputRequestTypeDef(BaseValidatorModel):
    graphName: str
    provisionedMemory: int
    tags: Optional[Mapping[str, str]] = None
    publicConnectivity: Optional[bool] = None
    kmsKeyIdentifier: Optional[str] = None
    vectorSearchConfiguration: Optional[VectorSearchConfigurationTypeDef] = None
    replicaCount: Optional[int] = None
    deletionProtection: Optional[bool] = None

class CreateGraphOutputTypeDef(BaseValidatorModel):
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

class DeleteGraphOutputTypeDef(BaseValidatorModel):
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

class GetGraphOutputTypeDef(BaseValidatorModel):
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

class ResetGraphOutputTypeDef(BaseValidatorModel):
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

class RestoreGraphFromSnapshotOutputTypeDef(BaseValidatorModel):
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

class UpdateGraphOutputTypeDef(BaseValidatorModel):
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

class GetGraphInputGraphAvailableWaitTypeDef(BaseValidatorModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetGraphInputGraphDeletedWaitTypeDef(BaseValidatorModel):
    graphIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetGraphSnapshotInputGraphSnapshotAvailableWaitTypeDef(BaseValidatorModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetGraphSnapshotInputGraphSnapshotDeletedWaitTypeDef(BaseValidatorModel):
    snapshotIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetImportTaskInputImportTaskCancelledWaitTypeDef(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetImportTaskInputImportTaskSuccessfulWaitTypeDef(BaseValidatorModel):
    taskIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPrivateGraphEndpointInputPrivateGraphEndpointAvailableWaitTypeDef(BaseValidatorModel):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPrivateGraphEndpointInputPrivateGraphEndpointDeletedWaitTypeDef(BaseValidatorModel):
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

class ListGraphSnapshotsOutputTypeDef(BaseValidatorModel):
    graphSnapshots: List[GraphSnapshotSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphsOutputTypeDef(BaseValidatorModel):
    graphs: List[GraphSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportOptionsTypeDef(BaseValidatorModel):
    neptune: Optional[NeptuneImportOptionsTypeDef] = None

class ListImportTasksOutputTypeDef(BaseValidatorModel):
    tasks: List[ImportTaskSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphSnapshotsInputListGraphSnapshotsPaginateTypeDef(BaseValidatorModel):
    graphIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGraphsInputListGraphsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportTasksInputListImportTasksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivateGraphEndpointsInputListPrivateGraphEndpointsPaginateTypeDef(BaseValidatorModel):
    graphIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivateGraphEndpointsOutputTypeDef(BaseValidatorModel):
    privateGraphEndpoints: List[PrivateGraphEndpointSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueriesOutputTypeDef(BaseValidatorModel):
    queries: List[QuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphSummaryOutputTypeDef(BaseValidatorModel):
    version: str
    lastStatisticsComputationTime: datetime
    graphSummary: GraphDataSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphUsingImportTaskInputRequestTypeDef(BaseValidatorModel):
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

class CreateGraphUsingImportTaskOutputTypeDef(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportTaskOutputTypeDef(BaseValidatorModel):
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

class StartImportTaskInputRequestTypeDef(BaseValidatorModel):
    source: str
    graphIdentifier: str
    roleArn: str
    importOptions: Optional[ImportOptionsTypeDef] = None
    failOnError: Optional[bool] = None
    format: Optional[FormatType] = None

class StartImportTaskOutputTypeDef(BaseValidatorModel):
    graphId: str
    taskId: str
    source: str
    format: FormatType
    roleArn: str
    status: ImportTaskStatusType
    importOptions: ImportOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

