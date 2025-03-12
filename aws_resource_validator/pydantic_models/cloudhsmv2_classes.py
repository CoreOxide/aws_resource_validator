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

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CertificatesTypeDef(BaseValidatorModel):
    ClusterCsr: Optional[str] = None
    HsmCertificate: Optional[str] = None
    AwsHardwareCertificate: Optional[str] = None
    ManufacturerHardwareCertificate: Optional[str] = None
    ClusterCertificate: Optional[str] = None


class HsmTypeDef(BaseValidatorModel):
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


class DestinationBackupTypeDef(BaseValidatorModel):
    CreateTimestamp: Optional[datetime] = None
    SourceRegion: Optional[str] = None
    SourceBackup: Optional[str] = None
    SourceCluster: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateHsmRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    AvailabilityZone: str
    IpAddress: Optional[str] = None


class DeleteBackupRequestTypeDef(BaseValidatorModel):
    BackupId: str


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    ClusterId: str


class DeleteHsmRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    HsmId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBackupsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None


class DescribeClustersRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class InitializeClusterRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    SignedCert: str
    TrustAnchor: str


class ListTagsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ModifyBackupAttributesRequestTypeDef(BaseValidatorModel):
    BackupId: str
    NeverExpires: bool


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None


class RestoreBackupRequestTypeDef(BaseValidatorModel):
    BackupId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeyList: Sequence[str]


class BackupRetentionPolicyTypeDef(BaseValidatorModel):
    pass


class ModifyClusterRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    HsmType: Optional[str] = None
    BackupRetentionPolicy: Optional[BackupRetentionPolicyTypeDef] = None


class BackupTypeDef(BaseValidatorModel):
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


class CopyBackupToRegionRequestTypeDef(BaseValidatorModel):
    DestinationRegion: str
    BackupId: str
    TagList: Optional[Sequence[TagTypeDef]] = None


class CreateClusterRequestTypeDef(BaseValidatorModel):
    HsmType: str
    SubnetIds: Sequence[str]
    BackupRetentionPolicy: Optional[BackupRetentionPolicyTypeDef] = None
    SourceBackupId: Optional[str] = None
    NetworkType: Optional[NetworkTypeType] = None
    TagList: Optional[Sequence[TagTypeDef]] = None
    Mode: Optional[ClusterModeType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagList: Sequence[TagTypeDef]


class ClusterTypeDef(BaseValidatorModel):
    BackupPolicy: Optional[Literal["DEFAULT"]] = None
    BackupRetentionPolicy: Optional[BackupRetentionPolicyTypeDef] = None
    ClusterId: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    Hsms: Optional[List[HsmTypeDef]] = None
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
    Certificates: Optional[CertificatesTypeDef] = None
    TagList: Optional[List[TagTypeDef]] = None
    Mode: Optional[ClusterModeType] = None


class CopyBackupToRegionResponseTypeDef(BaseValidatorModel):
    DestinationBackup: DestinationBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHsmResponseTypeDef(BaseValidatorModel):
    Hsm: HsmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteHsmResponseTypeDef(BaseValidatorModel):
    HsmId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class InitializeClusterResponseTypeDef(BaseValidatorModel):
    State: ClusterStateType
    StateMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBackupsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeClustersRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsRequestPaginateTypeDef(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DeleteBackupResponseTypeDef(BaseValidatorModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBackupsResponseTypeDef(BaseValidatorModel):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ModifyBackupAttributesResponseTypeDef(BaseValidatorModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreBackupResponseTypeDef(BaseValidatorModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClustersResponseTypeDef(BaseValidatorModel):
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ModifyClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


