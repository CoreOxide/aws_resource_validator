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
from aws_resource_validator.pydantic_models.cloudhsmv2_constants import *

class BackupRetentionPolicyTypeDef(BaseModel):
    Type: Optional[Literal["DAYS"]] = None
    Value: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CertificatesTypeDef(BaseModel):
    ClusterCsr: Optional[str] = None
    HsmCertificate: Optional[str] = None
    AwsHardwareCertificate: Optional[str] = None
    ManufacturerHardwareCertificate: Optional[str] = None
    ClusterCertificate: Optional[str] = None

class HsmTypeDef(BaseModel):
    HsmId: str
    AvailabilityZone: Optional[str] = None
    ClusterId: Optional[str] = None
    SubnetId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None
    State: Optional[HsmStateType] = None
    StateMessage: Optional[str] = None

class DestinationBackupTypeDef(BaseModel):
    CreateTimestamp: Optional[datetime] = None
    SourceRegion: Optional[str] = None
    SourceBackup: Optional[str] = None
    SourceCluster: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateHsmRequestRequestTypeDef(BaseModel):
    ClusterId: str
    AvailabilityZone: str
    IpAddress: Optional[str] = None

class DeleteBackupRequestRequestTypeDef(BaseModel):
    BackupId: str

class DeleteClusterRequestRequestTypeDef(BaseModel):
    ClusterId: str

class DeleteHsmRequestRequestTypeDef(BaseModel):
    ClusterId: str
    HsmId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBackupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None

class DescribeClustersRequestRequestTypeDef(BaseModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class InitializeClusterRequestRequestTypeDef(BaseModel):
    ClusterId: str
    SignedCert: str
    TrustAnchor: str

class ListTagsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ModifyBackupAttributesRequestRequestTypeDef(BaseModel):
    BackupId: str
    NeverExpires: bool

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None

class RestoreBackupRequestRequestTypeDef(BaseModel):
    BackupId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagKeyList: Sequence[str]

class ModifyClusterRequestRequestTypeDef(BaseModel):
    BackupRetentionPolicy: BackupRetentionPolicyTypeDef
    ClusterId: str

class BackupTypeDef(BaseModel):
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
    TagList: Optional[List[TagTypeDef]] = None
    HsmType: Optional[str] = None
    Mode: Optional[ClusterModeType] = None

class CopyBackupToRegionRequestRequestTypeDef(BaseModel):
    DestinationRegion: str
    BackupId: str
    TagList: Optional[Sequence[TagTypeDef]] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
    HsmType: str
    SubnetIds: Sequence[str]
    BackupRetentionPolicy: Optional[BackupRetentionPolicyTypeDef] = None
    SourceBackupId: Optional[str] = None
    TagList: Optional[Sequence[TagTypeDef]] = None
    Mode: Optional[ClusterModeType] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagList: Sequence[TagTypeDef]

class ClusterTypeDef(BaseModel):
    BackupPolicy: Optional[Literal["DEFAULT"]] = None
    BackupRetentionPolicy: Optional[BackupRetentionPolicyTypeDef] = None
    ClusterId: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    Hsms: Optional[List[HsmTypeDef]] = None
    HsmType: Optional[str] = None
    PreCoPassword: Optional[str] = None
    SecurityGroup: Optional[str] = None
    SourceBackupId: Optional[str] = None
    State: Optional[ClusterStateType] = None
    StateMessage: Optional[str] = None
    SubnetMapping: Optional[Dict[str, str]] = None
    VpcId: Optional[str] = None
    Certificates: Optional[CertificatesTypeDef] = None
    TagList: Optional[List[TagTypeDef]] = None
    Mode: Optional[ClusterModeType] = None

class CopyBackupToRegionResponseTypeDef(BaseModel):
    DestinationBackup: DestinationBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmResponseTypeDef(BaseModel):
    Hsm: HsmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHsmResponseTypeDef(BaseModel):
    HsmId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(BaseModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitializeClusterResponseTypeDef(BaseModel):
    State: ClusterStateType
    StateMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutResourcePolicyResponseTypeDef(BaseModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsRequestDescribeBackupsPaginateTypeDef(BaseModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClustersRequestDescribeClustersPaginateTypeDef(BaseModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DeleteBackupResponseTypeDef(BaseModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(BaseModel):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyBackupAttributesResponseTypeDef(BaseModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreBackupResponseTypeDef(BaseModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(BaseModel):
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

