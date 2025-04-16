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
from aws_resource_validator.pydantic_models.cloudhsmv2_constants import *

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


class CreateHsmRequest(BaseValidatorModel):
    ClusterId: str
    AvailabilityZone: str
    IpAddress: Optional[str] = None


class DeleteBackupRequest(BaseValidatorModel):
    BackupId: str


class DeleteClusterRequest(BaseValidatorModel):
    ClusterId: str


class DeleteHsmRequest(BaseValidatorModel):
    ClusterId: str
    HsmId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBackupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None


class DescribeClustersRequest(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class InitializeClusterRequest(BaseValidatorModel):
    ClusterId: str
    SignedCert: str
    TrustAnchor: str


class ListTagsRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ModifyBackupAttributesRequest(BaseValidatorModel):
    BackupId: str
    NeverExpires: bool


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None


class RestoreBackupRequest(BaseValidatorModel):
    BackupId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeyList: Sequence[str]


class BackupRetentionPolicy(BaseValidatorModel):
    pass


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


class CopyBackupToRegionRequest(BaseValidatorModel):
    DestinationRegion: str
    BackupId: str
    TagList: Optional[Sequence[Tag]] = None


class CreateClusterRequest(BaseValidatorModel):
    HsmType: str
    SubnetIds: Sequence[str]
    BackupRetentionPolicy: Optional[BackupRetentionPolicy] = None
    SourceBackupId: Optional[str] = None
    NetworkType: Optional[NetworkTypeType] = None
    TagList: Optional[Sequence[Tag]] = None
    Mode: Optional[ClusterModeType] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagList: Sequence[Tag]


class Cluster(BaseValidatorModel):
    BackupPolicy: Optional[Literal["DEFAULT"]] = None
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


class CopyBackupToRegionResponse(BaseValidatorModel):
    DestinationBackup: DestinationBackup
    ResponseMetadata: ResponseMetadata


class CreateHsmResponse(BaseValidatorModel):
    Hsm: Hsm
    ResponseMetadata: ResponseMetadata


class DeleteHsmResponse(BaseValidatorModel):
    HsmId: str
    ResponseMetadata: ResponseMetadata


class DeleteResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class InitializeClusterResponse(BaseValidatorModel):
    State: ClusterStateType
    StateMessage: str
    ResponseMetadata: ResponseMetadata


class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class DescribeBackupsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClustersRequestPaginate(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsRequestPaginate(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DeleteBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


class DescribeBackupsResponse(BaseValidatorModel):
    Backups: List[Backup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyBackupAttributesResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


class RestoreBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


class CreateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DescribeClustersResponse(BaseValidatorModel):
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


