from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplyPendingMaintenanceActionInput(BaseValidatorModel):
    applyAction: str
    optInType: OptInTypeType
    resourceArn: str
    applyOn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ClusterInList(BaseValidatorModel):
    clusterArn: str
    clusterName: str
    status: StatusType


class ClusterSnapshotInList(BaseValidatorModel):
    clusterArn: str
    snapshotArn: str
    snapshotCreationTime: str
    snapshotName: str
    status: StatusType


class ClusterSnapshot(BaseValidatorModel):
    adminUserName: str
    clusterArn: str
    clusterCreationTime: str
    kmsKeyId: str
    snapshotArn: str
    snapshotCreationTime: str
    snapshotName: str
    status: StatusType
    subnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    snapshotType: Optional[SnapshotTypeType] = None


class Shard(BaseValidatorModel):
    createTime: str
    shardId: str
    status: StatusType


class CopyClusterSnapshotInput(BaseValidatorModel):
    snapshotArn: str
    targetSnapshotName: str
    copyTags: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateClusterInput(BaseValidatorModel):
    adminUserName: str
    adminUserPassword: str
    authType: AuthType
    clusterName: str
    shardCapacity: int
    shardCount: int
    backupRetentionPeriod: Optional[int] = None
    clientToken: Optional[str] = None
    kmsKeyId: Optional[str] = None
    preferredBackupWindow: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    shardInstanceCount: Optional[int] = None
    subnetIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    vpcSecurityGroupIds: Optional[List[str]] = None


class CreateClusterSnapshotInput(BaseValidatorModel):
    clusterArn: str
    snapshotName: str
    tags: Optional[Dict[str, str]] = None


class DeleteClusterInput(BaseValidatorModel):
    clusterArn: str


class DeleteClusterSnapshotInput(BaseValidatorModel):
    snapshotArn: str


class GetClusterInput(BaseValidatorModel):
    clusterArn: str


class GetClusterSnapshotInput(BaseValidatorModel):
    snapshotArn: str


class GetPendingMaintenanceActionInput(BaseValidatorModel):
    resourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClusterSnapshotsInput(BaseValidatorModel):
    clusterArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    snapshotType: Optional[str] = None


class ListClustersInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPendingMaintenanceActionsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PendingMaintenanceActionDetails(BaseValidatorModel):
    action: str
    autoAppliedAfterDate: Optional[str] = None
    currentApplyDate: Optional[str] = None
    description: Optional[str] = None
    forcedApplyDate: Optional[str] = None
    optInStatus: Optional[str] = None


class RestoreClusterFromSnapshotInput(BaseValidatorModel):
    clusterName: str
    snapshotArn: str
    kmsKeyId: Optional[str] = None
    shardCapacity: Optional[int] = None
    shardInstanceCount: Optional[int] = None
    subnetIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    vpcSecurityGroupIds: Optional[List[str]] = None


class StartClusterInput(BaseValidatorModel):
    clusterArn: str


class StopClusterInput(BaseValidatorModel):
    clusterArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateClusterInput(BaseValidatorModel):
    clusterArn: str
    adminUserPassword: Optional[str] = None
    authType: Optional[AuthType] = None
    backupRetentionPeriod: Optional[int] = None
    clientToken: Optional[str] = None
    preferredBackupWindow: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    shardCapacity: Optional[int] = None
    shardCount: Optional[int] = None
    shardInstanceCount: Optional[int] = None
    subnetIds: Optional[List[str]] = None
    vpcSecurityGroupIds: Optional[List[str]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListClustersOutput(BaseValidatorModel):
    clusters: List[ClusterInList]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListClusterSnapshotsOutput(BaseValidatorModel):
    snapshots: List[ClusterSnapshotInList]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CopyClusterSnapshotOutput(BaseValidatorModel):
    snapshot: ClusterSnapshot
    ResponseMetadata: ResponseMetadata


class CreateClusterSnapshotOutput(BaseValidatorModel):
    snapshot: ClusterSnapshot
    ResponseMetadata: ResponseMetadata


class DeleteClusterSnapshotOutput(BaseValidatorModel):
    snapshot: ClusterSnapshot
    ResponseMetadata: ResponseMetadata


class GetClusterSnapshotOutput(BaseValidatorModel):
    snapshot: ClusterSnapshot
    ResponseMetadata: ResponseMetadata


class Cluster(BaseValidatorModel):
    adminUserName: str
    authType: AuthType
    clusterArn: str
    clusterEndpoint: str
    clusterName: str
    createTime: str
    kmsKeyId: str
    preferredMaintenanceWindow: str
    shardCapacity: int
    shardCount: int
    status: StatusType
    subnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    backupRetentionPeriod: Optional[int] = None
    preferredBackupWindow: Optional[str] = None
    shardInstanceCount: Optional[int] = None
    shards: Optional[List[Shard]] = None


class ListClusterSnapshotsInputPaginate(BaseValidatorModel):
    clusterArn: Optional[str] = None
    snapshotType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPendingMaintenanceActionsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ResourcePendingMaintenanceAction(BaseValidatorModel):
    pendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionDetails]] = None
    resourceArn: Optional[str] = None


class CreateClusterOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeleteClusterOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class GetClusterOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class RestoreClusterFromSnapshotOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class StartClusterOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class StopClusterOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class UpdateClusterOutput(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ApplyPendingMaintenanceActionOutput(BaseValidatorModel):
    resourcePendingMaintenanceAction: ResourcePendingMaintenanceAction
    ResponseMetadata: ResponseMetadata


class GetPendingMaintenanceActionOutput(BaseValidatorModel):
    resourcePendingMaintenanceAction: ResourcePendingMaintenanceAction
    ResponseMetadata: ResponseMetadata


class ListPendingMaintenanceActionsOutput(BaseValidatorModel):
    resourcePendingMaintenanceActions: List[ResourcePendingMaintenanceAction]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None