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
from aws_resource_validator.pydantic_models.efs_constants import *

class PosixUserOutputTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class BackupPolicyTypeDef(BaseValidatorModel):
    Status: StatusType

class PosixUserTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[Sequence[int]] = None

class CreateMountTargetRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    SubnetId: str
    IpAddress: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None

class DestinationToCreateTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    AvailabilityZoneName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    FileSystemId: Optional[str] = None

class CreationInfoTypeDef(BaseValidatorModel):
    OwnerUid: int
    OwnerGid: int
    Permissions: str

class DeleteAccessPointRequestRequestTypeDef(BaseValidatorModel):
    AccessPointId: str

class DeleteFileSystemPolicyRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str

class DeleteFileSystemRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str

class DeleteMountTargetRequestRequestTypeDef(BaseValidatorModel):
    MountTargetId: str

class DeleteReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SourceFileSystemId: str

class DeleteTagsRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    TagKeys: Sequence[str]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccessPointsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None

class DescribeAccountPreferencesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResourceIdPreferenceTypeDef(BaseValidatorModel):
    ResourceIdType: Optional[ResourceIdTypeType] = None
    Resources: Optional[List[ResourceType]] = None

class DescribeBackupPolicyRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str

class DescribeFileSystemPolicyRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str

class DescribeFileSystemsRequestRequestTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None

class DescribeLifecycleConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str

class DescribeMountTargetSecurityGroupsRequestRequestTypeDef(BaseValidatorModel):
    MountTargetId: str

class DescribeMountTargetsRequestRequestTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    FileSystemId: Optional[str] = None
    MountTargetId: Optional[str] = None
    AccessPointId: Optional[str] = None

class MountTargetDescriptionTypeDef(BaseValidatorModel):
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

class DescribeReplicationConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTagsRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class DestinationTypeDef(BaseValidatorModel):
    Status: ReplicationStatusType
    FileSystemId: str
    Region: str
    LastReplicatedTimestamp: Optional[datetime] = None

class FileSystemProtectionDescriptionTypeDef(BaseValidatorModel):
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None

class FileSystemSizeTypeDef(BaseValidatorModel):
    Value: int
    Timestamp: Optional[datetime] = None
    ValueInIA: Optional[int] = None
    ValueInStandard: Optional[int] = None
    ValueInArchive: Optional[int] = None

class LifecyclePolicyTypeDef(BaseValidatorModel):
    TransitionToIA: Optional[TransitionToIARulesType] = None
    TransitionToPrimaryStorageClass: Optional[Literal["AFTER_1_ACCESS"]] = None
    TransitionToArchive: Optional[TransitionToArchiveRulesType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ModifyMountTargetSecurityGroupsRequestRequestTypeDef(BaseValidatorModel):
    MountTargetId: str
    SecurityGroups: Optional[Sequence[str]] = None

class PosixUserExtraOutputTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None

class PutAccountPreferencesRequestRequestTypeDef(BaseValidatorModel):
    ResourceIdType: ResourceIdTypeType

class PutFileSystemPolicyRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    Policy: str
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]

class UpdateFileSystemProtectionRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None

class UpdateFileSystemRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None

class DescribeMountTargetSecurityGroupsResponseTypeDef(BaseValidatorModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemPolicyDescriptionTypeDef(BaseValidatorModel):
    FileSystemId: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemProtectionDescriptionResponseTypeDef(BaseValidatorModel):
    ReplicationOverwriteProtection: ReplicationOverwriteProtectionType
    ResponseMetadata: ResponseMetadataTypeDef

class MountTargetDescriptionResponseTypeDef(BaseValidatorModel):
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

class CreateFileSystemRequestRequestTypeDef(BaseValidatorModel):
    CreationToken: str
    PerformanceMode: Optional[PerformanceModeType] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None
    AvailabilityZoneName: Optional[str] = None
    Backup: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTagsRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    Tags: Sequence[TagTypeDef]

class DescribeTagsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Tags: List[TagTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class BackupPolicyDescriptionTypeDef(BaseValidatorModel):
    BackupPolicy: BackupPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBackupPolicyRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    BackupPolicy: BackupPolicyTypeDef

class CreateReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SourceFileSystemId: str
    Destinations: Sequence[DestinationToCreateTypeDef]

class RootDirectoryTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    CreationInfo: Optional[CreationInfoTypeDef] = None

class DescribeAccessPointsRequestDescribeAccessPointsPaginateTypeDef(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef(BaseValidatorModel):
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    MountTargetId: Optional[str] = None
    AccessPointId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsRequestDescribeTagsPaginateTypeDef(BaseValidatorModel):
    FileSystemId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountPreferencesResponseTypeDef(BaseValidatorModel):
    ResourceIdPreference: ResourceIdPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAccountPreferencesResponseTypeDef(BaseValidatorModel):
    ResourceIdPreference: ResourceIdPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMountTargetsResponseTypeDef(BaseValidatorModel):
    Marker: str
    MountTargets: List[MountTargetDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationDescriptionResponseTypeDef(BaseValidatorModel):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationDescriptionTypeDef(BaseValidatorModel):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[DestinationTypeDef]

class FileSystemDescriptionResponseTypeDef(BaseValidatorModel):
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

class FileSystemDescriptionTypeDef(BaseValidatorModel):
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

class LifecycleConfigurationDescriptionTypeDef(BaseValidatorModel):
    LifecyclePolicies: List[LifecyclePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutLifecycleConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    LifecyclePolicies: Sequence[LifecyclePolicyTypeDef]

class AccessPointDescriptionResponseTypeDef(BaseValidatorModel):
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

class AccessPointDescriptionTypeDef(BaseValidatorModel):
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

class CreateAccessPointRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    FileSystemId: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    PosixUser: Optional[PosixUserTypeDef] = None
    RootDirectory: Optional[RootDirectoryTypeDef] = None

class DescribeReplicationConfigurationsResponseTypeDef(BaseValidatorModel):
    Replications: List[ReplicationConfigurationDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFileSystemsResponseTypeDef(BaseValidatorModel):
    Marker: str
    FileSystems: List[FileSystemDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessPointsResponseTypeDef(BaseValidatorModel):
    AccessPoints: List[AccessPointDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

