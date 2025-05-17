from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BackupRetentionPolicy(BaseValidatorModel):
    Type: Optional[Literal['DAYS']] = None
    Value: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class Certificates(BaseValidatorModel):
    ClusterCsr: Optional[str] = None
    HsmCertificate: Optional[str] = None
    AwsHardwareCertificate: Optional[str] = None
    ManufacturerHardwareCertificate: Optional[str] = None
    ClusterCertificate: Optional[str] = None


class Hsm(BaseValidatorModel):
    HsmId: str
    AvailabilityZone: Optional[str] = None
    ClusterId: Optional[str] = None
    SubnetId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None
    EniIpV6: Optional[str] = None
    HsmType: Optional[str] = None
    State: Optional[HsmStateType] = None
    StateMessage: Optional[str] = None


class DestinationBackup(BaseValidatorModel):
    CreateTimestamp: Optional[datetime] = None
    SourceRegion: Optional[str] = None
    SourceBackup: Optional[str] = None
    SourceCluster: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_hsm' function.
class CreateHsmRequest(BaseValidatorModel):
    ClusterId: str
    AvailabilityZone: str
    IpAddress: Optional[str] = None


# This class is the input for the 'delete_backup' function.
class DeleteBackupRequest(BaseValidatorModel):
    BackupId: str


# This class is the input for the 'delete_cluster' function.
class DeleteClusterRequest(BaseValidatorModel):
    ClusterId: str


# This class is the input for the 'delete_hsm' function.
class DeleteHsmRequest(BaseValidatorModel):
    ClusterId: str
    HsmId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_backups' function.
class DescribeBackupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Dict[str, List[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None


# This class is the input for the 'describe_clusters' function.
class DescribeClustersRequest(BaseValidatorModel):
    Filters: Optional[Dict[str, List[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None


# This class is the input for the 'initialize_cluster' function.
class InitializeClusterRequest(BaseValidatorModel):
    ClusterId: str
    SignedCert: str
    TrustAnchor: str


# This class is the input for the 'list_tags' function.
class ListTagsRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'modify_backup_attributes' function.
class ModifyBackupAttributesRequest(BaseValidatorModel):
    BackupId: str
    NeverExpires: bool


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None


# This class is the input for the 'restore_backup' function.
class RestoreBackupRequest(BaseValidatorModel):
    BackupId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeyList: List[str]


# This class is the input for the 'modify_cluster' function.
class ModifyClusterRequest(BaseValidatorModel):
    ClusterId: str
    HsmType: Optional[str] = None
    BackupRetentionPolicy: Optional[BackupRetentionPolicy] = None


class Backup(BaseValidatorModel):
    BackupId: str
    BackupArn: Optional[str] = None
    BackupState: Optional[BackupStateType] = None
    ClusterId: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    CopyTimestamp: Optional[datetime] = None
    NeverExpires: Optional[bool] = None
    SourceRegion: Optional[str] = None
    SourceBackup: Optional[str] = None
    SourceCluster: Optional[str] = None
    DeleteTimestamp: Optional[datetime] = None
    TagList: Optional[List[Tag]] = None
    HsmType: Optional[str] = None
    Mode: Optional[ClusterModeType] = None


# This class is the input for the 'copy_backup_to_region' function.
class CopyBackupToRegionRequest(BaseValidatorModel):
    DestinationRegion: str
    BackupId: str
    TagList: Optional[List[Tag]] = None


# This class is the input for the 'create_cluster' function.
class CreateClusterRequest(BaseValidatorModel):
    HsmType: str
    SubnetIds: List[str]
    BackupRetentionPolicy: Optional[BackupRetentionPolicy] = None
    SourceBackupId: Optional[str] = None
    NetworkType: Optional[NetworkTypeType] = None
    TagList: Optional[List[Tag]] = None
    Mode: Optional[ClusterModeType] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagList: List[Tag]


class Cluster(BaseValidatorModel):
    BackupPolicy: Optional[Literal['DEFAULT']] = None
    BackupRetentionPolicy: Optional[BackupRetentionPolicy] = None
    ClusterId: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    Hsms: Optional[List[Hsm]] = None
    HsmType: Optional[str] = None
    HsmTypeRollbackExpiration: Optional[datetime] = None
    PreCoPassword: Optional[str] = None
    SecurityGroup: Optional[str] = None
    SourceBackupId: Optional[str] = None
    State: Optional[ClusterStateType] = None
    StateMessage: Optional[str] = None
    SubnetMapping: Optional[Dict[str, str]] = None
    VpcId: Optional[str] = None
    NetworkType: Optional[NetworkTypeType] = None
    Certificates: Optional[Certificates] = None
    TagList: Optional[List[Tag]] = None
    Mode: Optional[ClusterModeType] = None


# This class is the output for the 'copy_backup_to_region' function.
class CopyBackupToRegionResponse(BaseValidatorModel):
    DestinationBackup: DestinationBackup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hsm' function.
class CreateHsmResponse(BaseValidatorModel):
    Hsm: Hsm
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_hsm' function.
class DeleteHsmResponse(BaseValidatorModel):
    HsmId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_policy' function.
class DeleteResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'initialize_cluster' function.
class InitializeClusterResponse(BaseValidatorModel):
    State: ClusterStateType
    StateMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags' function.
class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class DescribeBackupsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Dict[str, List[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClustersRequestPaginate(BaseValidatorModel):
    Filters: Optional[Dict[str, List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsRequestPaginate(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'delete_backup' function.
class DeleteBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_backups' function.
class DescribeBackupsResponse(BaseValidatorModel):
    Backups: List[Backup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_backup_attributes' function.
class ModifyBackupAttributesResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_backup' function.
class RestoreBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster' function.
class CreateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_clusters' function.
class DescribeClustersResponse(BaseValidatorModel):
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_cluster' function.
class ModifyClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata