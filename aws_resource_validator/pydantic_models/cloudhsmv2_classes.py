from datetime import datetime
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
from aws_resource_validator.pydantic_models.cloudhsmv2_constants import *

class BackupRetentionPolicyTypeDef(BaseValidatorModel):
    Type: Optional[Literal["DAYS"]] = None
    Value: Optional[str] = None

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

class CreateHsmRequestRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    AvailabilityZone: str
    IpAddress: Optional[str] = None

class DeleteBackupRequestRequestTypeDef(BaseValidatorModel):
    BackupId: str

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterId: str

class DeleteHsmRequestRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    HsmId: Optional[str] = None
    EniId: Optional[str] = None
    EniIp: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBackupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None

class DescribeClustersRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None

class InitializeClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    SignedCert: str
    TrustAnchor: str

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ModifyBackupAttributesRequestRequestTypeDef(BaseValidatorModel):
    BackupId: str
    NeverExpires: bool

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None

class RestoreBackupRequestRequestTypeDef(BaseValidatorModel):
    BackupId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeyList: Sequence[str]

class ModifyClusterRequestRequestTypeDef(BaseValidatorModel):
    BackupRetentionPolicy: BackupRetentionPolicyTypeDef
    ClusterId: str

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

class CopyBackupToRegionRequestRequestTypeDef(BaseValidatorModel):
    DestinationRegion: str
    BackupId: str
    TagList: Optional[Sequence[TagTypeDef]] = None

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
    HsmType: str
    SubnetIds: Sequence[str]
    BackupRetentionPolicy: Optional[BackupRetentionPolicyTypeDef] = None
    SourceBackupId: Optional[str] = None
    TagList: Optional[Sequence[TagTypeDef]] = None
    Mode: Optional[ClusterModeType] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagList: Sequence[TagTypeDef]

class ClusterTypeDef(BaseValidatorModel):
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

class DescribeBackupsRequestDescribeBackupsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    Shared: Optional[bool] = None
    SortAscending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClustersRequestDescribeClustersPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseValidatorModel):
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

