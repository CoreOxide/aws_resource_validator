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
from aws_resource_validator.pydantic_models.efs_constants import *

class PosixUserOutputTypeDef(BaseModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class BackupPolicyTypeDef(BaseModel):
    Status: StatusType

class PosixUserTypeDef(BaseModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[Sequence[int]] = None

class CreateMountTargetRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    SubnetId: str
    IpAddress: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None

class DestinationToCreateTypeDef(BaseModel):
    Region: Optional[str] = None
    AvailabilityZoneName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    FileSystemId: Optional[str] = None

class CreationInfoTypeDef(BaseModel):
    OwnerUid: int
    OwnerGid: int
    Permissions: str

class DeleteAccessPointRequestRequestTypeDef(BaseModel):
    AccessPointId: str

class DeleteFileSystemPolicyRequestRequestTypeDef(BaseModel):
    FileSystemId: str

class DeleteFileSystemRequestRequestTypeDef(BaseModel):
    FileSystemId: str

class DeleteMountTargetRequestRequestTypeDef(BaseModel):
    MountTargetId: str

class DeleteReplicationConfigurationRequestRequestTypeDef(BaseModel):
    SourceFileSystemId: str

class DeleteTagsRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    TagKeys: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccessPointsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None

class DescribeAccountPreferencesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResourceIdPreferenceTypeDef(BaseModel):
    ResourceIdType: Optional[ResourceIdTypeType] = None
    Resources: Optional[List[ResourceType]] = None

class DescribeBackupPolicyRequestRequestTypeDef(BaseModel):
    FileSystemId: str

class DescribeFileSystemPolicyRequestRequestTypeDef(BaseModel):
    FileSystemId: str

class DescribeFileSystemsRequestRequestTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None

class DescribeLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    FileSystemId: str

class DescribeMountTargetSecurityGroupsRequestRequestTypeDef(BaseModel):
    MountTargetId: str

class DescribeMountTargetsRequestRequestTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    FileSystemId: Optional[str] = None
    MountTargetId: Optional[str] = None
    AccessPointId: Optional[str] = None

class MountTargetDescriptionTypeDef(BaseModel):
    MountTargetId: str
    FileSystemId: str
    SubnetId: str
    LifeCycleState: LifeCycleStateType
    OwnerId: Optional[str] = None
    IpAddress: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    AvailabilityZoneName: Optional[str] = None
    VpcId: Optional[str] = None

class DescribeReplicationConfigurationsRequestRequestTypeDef(BaseModel):
    FileSystemId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTagsRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class DestinationTypeDef(BaseModel):
    Status: ReplicationStatusType
    FileSystemId: str
    Region: str
    LastReplicatedTimestamp: Optional[datetime] = None

class FileSystemProtectionDescriptionTypeDef(BaseModel):
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None

class FileSystemSizeTypeDef(BaseModel):
    Value: int
    Timestamp: Optional[datetime] = None
    ValueInIA: Optional[int] = None
    ValueInStandard: Optional[int] = None
    ValueInArchive: Optional[int] = None

class LifecyclePolicyTypeDef(BaseModel):
    TransitionToIA: Optional[TransitionToIARulesType] = None
    TransitionToPrimaryStorageClass: Optional[Literal["AFTER_1_ACCESS"]] = None
    TransitionToArchive: Optional[TransitionToArchiveRulesType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ModifyMountTargetSecurityGroupsRequestRequestTypeDef(BaseModel):
    MountTargetId: str
    SecurityGroups: Optional[Sequence[str]] = None

class PosixUserExtraOutputTypeDef(BaseModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None

class PutAccountPreferencesRequestRequestTypeDef(BaseModel):
    ResourceIdType: ResourceIdTypeType

class PutFileSystemPolicyRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    Policy: str
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagKeys: Sequence[str]

class UpdateFileSystemProtectionRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None

class UpdateFileSystemRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None

class DescribeMountTargetSecurityGroupsResponseTypeDef(BaseModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemPolicyDescriptionTypeDef(BaseModel):
    FileSystemId: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemProtectionDescriptionResponseTypeDef(BaseModel):
    ReplicationOverwriteProtection: ReplicationOverwriteProtectionType
    ResponseMetadata: ResponseMetadataTypeDef

class MountTargetDescriptionResponseTypeDef(BaseModel):
    OwnerId: str
    MountTargetId: str
    FileSystemId: str
    SubnetId: str
    LifeCycleState: LifeCycleStateType
    IpAddress: str
    NetworkInterfaceId: str
    AvailabilityZoneId: str
    AvailabilityZoneName: str
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemRequestRequestTypeDef(BaseModel):
    CreationToken: str
    PerformanceMode: Optional[PerformanceModeType] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None
    AvailabilityZoneName: Optional[str] = None
    Backup: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTagsRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    Tags: Sequence[TagTypeDef]

class DescribeTagsResponseTypeDef(BaseModel):
    Marker: str
    Tags: List[TagTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class BackupPolicyDescriptionTypeDef(BaseModel):
    BackupPolicy: BackupPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBackupPolicyRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    BackupPolicy: BackupPolicyTypeDef

class CreateReplicationConfigurationRequestRequestTypeDef(BaseModel):
    SourceFileSystemId: str
    Destinations: Sequence[DestinationToCreateTypeDef]

class RootDirectoryTypeDef(BaseModel):
    Path: Optional[str] = None
    CreationInfo: Optional[CreationInfoTypeDef] = None

class DescribeAccessPointsRequestDescribeAccessPointsPaginateTypeDef(BaseModel):
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef(BaseModel):
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef(BaseModel):
    FileSystemId: Optional[str] = None
    MountTargetId: Optional[str] = None
    AccessPointId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsRequestDescribeTagsPaginateTypeDef(BaseModel):
    FileSystemId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountPreferencesResponseTypeDef(BaseModel):
    ResourceIdPreference: ResourceIdPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAccountPreferencesResponseTypeDef(BaseModel):
    ResourceIdPreference: ResourceIdPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMountTargetsResponseTypeDef(BaseModel):
    Marker: str
    MountTargets: List[MountTargetDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationDescriptionResponseTypeDef(BaseModel):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationDescriptionTypeDef(BaseModel):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[DestinationTypeDef]

class FileSystemDescriptionResponseTypeDef(BaseModel):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    FileSystemArn: str
    CreationTime: datetime
    LifeCycleState: LifeCycleStateType
    Name: str
    NumberOfMountTargets: int
    SizeInBytes: FileSystemSizeTypeDef
    PerformanceMode: PerformanceModeType
    Encrypted: bool
    KmsKeyId: str
    ThroughputMode: ThroughputModeType
    ProvisionedThroughputInMibps: float
    AvailabilityZoneName: str
    AvailabilityZoneId: str
    Tags: List[TagTypeDef]
    FileSystemProtection: FileSystemProtectionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemDescriptionTypeDef(BaseModel):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    CreationTime: datetime
    LifeCycleState: LifeCycleStateType
    NumberOfMountTargets: int
    SizeInBytes: FileSystemSizeTypeDef
    PerformanceMode: PerformanceModeType
    Tags: List[TagTypeDef]
    FileSystemArn: Optional[str] = None
    Name: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None
    AvailabilityZoneName: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    FileSystemProtection: Optional[FileSystemProtectionDescriptionTypeDef] = None

class LifecycleConfigurationDescriptionTypeDef(BaseModel):
    LifecyclePolicies: List[LifecyclePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    LifecyclePolicies: Sequence[LifecyclePolicyTypeDef]

class AccessPointDescriptionResponseTypeDef(BaseModel):
    ClientToken: str
    Name: str
    Tags: List[TagTypeDef]
    AccessPointId: str
    AccessPointArn: str
    FileSystemId: str
    PosixUser: PosixUserOutputTypeDef
    RootDirectory: RootDirectoryTypeDef
    OwnerId: str
    LifeCycleState: LifeCycleStateType
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPointDescriptionTypeDef(BaseModel):
    ClientToken: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    AccessPointId: Optional[str] = None
    AccessPointArn: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[PosixUserOutputTypeDef] = None
    RootDirectory: Optional[RootDirectoryTypeDef] = None
    OwnerId: Optional[str] = None
    LifeCycleState: Optional[LifeCycleStateType] = None

class CreateAccessPointRequestRequestTypeDef(BaseModel):
    ClientToken: str
    FileSystemId: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    PosixUser: Optional[PosixUserTypeDef] = None
    RootDirectory: Optional[RootDirectoryTypeDef] = None

class DescribeReplicationConfigurationsResponseTypeDef(BaseModel):
    Replications: List[ReplicationConfigurationDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFileSystemsResponseTypeDef(BaseModel):
    Marker: str
    FileSystems: List[FileSystemDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessPointsResponseTypeDef(BaseModel):
    AccessPoints: List[AccessPointDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

