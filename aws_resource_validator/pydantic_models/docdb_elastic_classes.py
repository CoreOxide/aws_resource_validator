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
from aws_resource_validator.pydantic_models.docdb_elastic_constants import *

class ApplyPendingMaintenanceActionInputTypeDef(BaseValidatorModel):
    applyAction: str
    optInType: OptInTypeType
    resourceArn: str
    applyOn: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ClusterInListTypeDef(BaseValidatorModel):
    clusterArn: str
    clusterName: str
    status: StatusType


class ClusterSnapshotInListTypeDef(BaseValidatorModel):
    clusterArn: str
    snapshotArn: str
    snapshotCreationTime: str
    snapshotName: str
    status: StatusType


class ClusterSnapshotTypeDef(BaseValidatorModel):
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


class ShardTypeDef(BaseValidatorModel):
    createTime: str
    shardId: str
    status: StatusType


class CopyClusterSnapshotInputTypeDef(BaseValidatorModel):
    snapshotArn: str
    targetSnapshotName: str
    copyTags: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateClusterInputTypeDef(BaseValidatorModel):
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
    subnetIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None


class CreateClusterSnapshotInputTypeDef(BaseValidatorModel):
    clusterArn: str
    snapshotName: str
    tags: Optional[Mapping[str, str]] = None


class DeleteClusterInputTypeDef(BaseValidatorModel):
    clusterArn: str


class DeleteClusterSnapshotInputTypeDef(BaseValidatorModel):
    snapshotArn: str


class GetClusterInputTypeDef(BaseValidatorModel):
    clusterArn: str


class GetClusterSnapshotInputTypeDef(BaseValidatorModel):
    snapshotArn: str


class GetPendingMaintenanceActionInputTypeDef(BaseValidatorModel):
    resourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClusterSnapshotsInputTypeDef(BaseValidatorModel):
    clusterArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    snapshotType: Optional[str] = None


class ListClustersInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPendingMaintenanceActionsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PendingMaintenanceActionDetailsTypeDef(BaseValidatorModel):
    action: str
    autoAppliedAfterDate: Optional[str] = None
    currentApplyDate: Optional[str] = None
    description: Optional[str] = None
    forcedApplyDate: Optional[str] = None
    optInStatus: Optional[str] = None


class RestoreClusterFromSnapshotInputTypeDef(BaseValidatorModel):
    clusterName: str
    snapshotArn: str
    kmsKeyId: Optional[str] = None
    shardCapacity: Optional[int] = None
    shardInstanceCount: Optional[int] = None
    subnetIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None


class StartClusterInputTypeDef(BaseValidatorModel):
    clusterArn: str


class StopClusterInputTypeDef(BaseValidatorModel):
    clusterArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateClusterInputTypeDef(BaseValidatorModel):
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
    subnetIds: Optional[Sequence[str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListClustersOutputTypeDef(BaseValidatorModel):
    clusters: List[ClusterInListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListClusterSnapshotsOutputTypeDef(BaseValidatorModel):
    snapshots: List[ClusterSnapshotInListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CopyClusterSnapshotOutputTypeDef(BaseValidatorModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateClusterSnapshotOutputTypeDef(BaseValidatorModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterSnapshotOutputTypeDef(BaseValidatorModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetClusterSnapshotOutputTypeDef(BaseValidatorModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ClusterTypeDef(BaseValidatorModel):
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
    shards: Optional[List[ShardTypeDef]] = None


class ListClusterSnapshotsInputPaginateTypeDef(BaseValidatorModel):
    clusterArn: Optional[str] = None
    snapshotType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClustersInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPendingMaintenanceActionsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ResourcePendingMaintenanceActionTypeDef(BaseValidatorModel):
    pendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionDetailsTypeDef]] = None
    resourceArn: Optional[str] = None


class CreateClusterOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetClusterOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreClusterFromSnapshotOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartClusterOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopClusterOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterOutputTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApplyPendingMaintenanceActionOutputTypeDef(BaseValidatorModel):
    resourcePendingMaintenanceAction: ResourcePendingMaintenanceActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPendingMaintenanceActionOutputTypeDef(BaseValidatorModel):
    resourcePendingMaintenanceAction: ResourcePendingMaintenanceActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPendingMaintenanceActionsOutputTypeDef(BaseValidatorModel):
    resourcePendingMaintenanceActions: List[ResourcePendingMaintenanceActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


