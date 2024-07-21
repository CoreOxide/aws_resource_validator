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
from aws_resource_validator.pydantic_models.docdb_elastic_constants import *

class ClusterInListTypeDef(BaseModel):
    clusterArn: str
    clusterName: str
    status: StatusType

class ClusterSnapshotInListTypeDef(BaseModel):
    clusterArn: str
    snapshotArn: str
    snapshotCreationTime: str
    snapshotName: str
    status: StatusType

class ClusterSnapshotTypeDef(BaseModel):
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

class ShardTypeDef(BaseModel):
    createTime: str
    shardId: str
    status: StatusType

class CopyClusterSnapshotInputRequestTypeDef(BaseModel):
    snapshotArn: str
    targetSnapshotName: str
    copyTags: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateClusterInputRequestTypeDef(BaseModel):
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

class CreateClusterSnapshotInputRequestTypeDef(BaseModel):
    clusterArn: str
    snapshotName: str
    tags: Optional[Mapping[str, str]] = None

class DeleteClusterInputRequestTypeDef(BaseModel):
    clusterArn: str

class DeleteClusterSnapshotInputRequestTypeDef(BaseModel):
    snapshotArn: str

class GetClusterInputRequestTypeDef(BaseModel):
    clusterArn: str

class GetClusterSnapshotInputRequestTypeDef(BaseModel):
    snapshotArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListClusterSnapshotsInputRequestTypeDef(BaseModel):
    clusterArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    snapshotType: Optional[str] = None

class ListClustersInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RestoreClusterFromSnapshotInputRequestTypeDef(BaseModel):
    clusterName: str
    snapshotArn: str
    kmsKeyId: Optional[str] = None
    shardCapacity: Optional[int] = None
    shardInstanceCount: Optional[int] = None
    subnetIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None

class StartClusterInputRequestTypeDef(BaseModel):
    clusterArn: str

class StopClusterInputRequestTypeDef(BaseModel):
    clusterArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateClusterInputRequestTypeDef(BaseModel):
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

class ClusterTypeDef(BaseModel):
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

class CopyClusterSnapshotOutputTypeDef(BaseModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSnapshotOutputTypeDef(BaseModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterSnapshotOutputTypeDef(BaseModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterSnapshotOutputTypeDef(BaseModel):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClusterSnapshotsOutputTypeDef(BaseModel):
    nextToken: str
    snapshots: List[ClusterSnapshotInListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersOutputTypeDef(BaseModel):
    clusters: List[ClusterInListTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef(BaseModel):
    clusterArn: Optional[str] = None
    snapshotType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersInputListClustersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateClusterOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreClusterFromSnapshotOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartClusterOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopClusterOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterOutputTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

