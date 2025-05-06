from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.efs.efs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class PosixUserOutput(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class BackupPolicy(BaseValidatorModel):
    Status: StatusType


class CreateMountTargetRequest(BaseValidatorModel):
    FileSystemId: str
    SubnetId: str
    IpAddress: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None


class DestinationToCreate(BaseValidatorModel):
    Region: Optional[str] = None
    AvailabilityZoneName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    FileSystemId: Optional[str] = None
    RoleArn: Optional[str] = None


class CreationInfo(BaseValidatorModel):
    OwnerUid: int
    OwnerGid: int
    Permissions: str


class DeleteAccessPointRequest(BaseValidatorModel):
    AccessPointId: str


class DeleteFileSystemPolicyRequest(BaseValidatorModel):
    FileSystemId: str


class DeleteFileSystemRequest(BaseValidatorModel):
    FileSystemId: str


class DeleteMountTargetRequest(BaseValidatorModel):
    MountTargetId: str


class DeleteReplicationConfigurationRequest(BaseValidatorModel):
    SourceFileSystemId: str
    DeletionMode: Optional[DeletionModeType] = None


class DeleteTagsRequest(BaseValidatorModel):
    FileSystemId: str
    TagKeys: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAccessPointsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None


class DescribeAccountPreferencesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceIdPreference(BaseValidatorModel):
    ResourceIdType: Optional[ResourceIdTypeType] = None
    Resources: Optional[List[ResourceType]] = None


class DescribeBackupPolicyRequest(BaseValidatorModel):
    FileSystemId: str


class DescribeFileSystemPolicyRequest(BaseValidatorModel):
    FileSystemId: str


class DescribeFileSystemsRequest(BaseValidatorModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None


class DescribeLifecycleConfigurationRequest(BaseValidatorModel):
    FileSystemId: str


class DescribeMountTargetSecurityGroupsRequest(BaseValidatorModel):
    MountTargetId: str


class DescribeMountTargetsRequest(BaseValidatorModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    FileSystemId: Optional[str] = None
    MountTargetId: Optional[str] = None
    AccessPointId: Optional[str] = None


class MountTargetDescription(BaseValidatorModel):
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


class DescribeReplicationConfigurationsRequest(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeTagsRequest(BaseValidatorModel):
    FileSystemId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class Destination(BaseValidatorModel):
    Status: ReplicationStatusType
    FileSystemId: str
    Region: str
    LastReplicatedTimestamp: Optional[datetime] = None
    OwnerId: Optional[str] = None
    StatusMessage: Optional[str] = None
    RoleArn: Optional[str] = None


class FileSystemProtectionDescription(BaseValidatorModel):
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None


class FileSystemSize(BaseValidatorModel):
    Value: int
    Timestamp: Optional[datetime] = None
    ValueInIA: Optional[int] = None
    ValueInStandard: Optional[int] = None
    ValueInArchive: Optional[int] = None


class LifecyclePolicy(BaseValidatorModel):
    TransitionToIA: Optional[TransitionToIARulesType] = None
    TransitionToPrimaryStorageClass: Optional[Literal['AFTER_1_ACCESS']] = None
    TransitionToArchive: Optional[TransitionToArchiveRulesType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ModifyMountTargetSecurityGroupsRequest(BaseValidatorModel):
    MountTargetId: str
    SecurityGroups: Optional[List[str]] = None


class PosixUser(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None


class PutAccountPreferencesRequest(BaseValidatorModel):
    ResourceIdType: ResourceIdTypeType


class PutFileSystemPolicyRequest(BaseValidatorModel):
    FileSystemId: str
    Policy: str
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: List[str]


class UpdateFileSystemProtectionRequest(BaseValidatorModel):
    FileSystemId: str
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None


class UpdateFileSystemRequest(BaseValidatorModel):
    FileSystemId: str
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None


class DescribeMountTargetSecurityGroupsResponse(BaseValidatorModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class FileSystemPolicyDescription(BaseValidatorModel):
    FileSystemId: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class FileSystemProtectionDescriptionResponse(BaseValidatorModel):
    ReplicationOverwriteProtection: ReplicationOverwriteProtectionType
    ResponseMetadata: ResponseMetadata


class MountTargetDescriptionResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class CreateFileSystemRequest(BaseValidatorModel):
    CreationToken: str
    PerformanceMode: Optional[PerformanceModeType] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None
    AvailabilityZoneName: Optional[str] = None
    Backup: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class CreateTagsRequest(BaseValidatorModel):
    FileSystemId: str
    Tags: List[Tag]


class DescribeTagsResponse(BaseValidatorModel):
    Marker: str
    Tags: List[Tag]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceId: str
    Tags: List[Tag]


class BackupPolicyDescription(BaseValidatorModel):
    BackupPolicy: BackupPolicy
    ResponseMetadata: ResponseMetadata


class PutBackupPolicyRequest(BaseValidatorModel):
    FileSystemId: str
    BackupPolicy: BackupPolicy


class CreateReplicationConfigurationRequest(BaseValidatorModel):
    SourceFileSystemId: str
    Destinations: List[DestinationToCreate]


class RootDirectory(BaseValidatorModel):
    Path: Optional[str] = None
    CreationInfo: Optional[CreationInfo] = None


class DescribeAccessPointsRequestPaginate(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFileSystemsRequestPaginate(BaseValidatorModel):
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMountTargetsRequestPaginate(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    MountTargetId: Optional[str] = None
    AccessPointId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationConfigurationsRequestPaginate(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTagsRequestPaginate(BaseValidatorModel):
    FileSystemId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAccountPreferencesResponse(BaseValidatorModel):
    ResourceIdPreference: ResourceIdPreference
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutAccountPreferencesResponse(BaseValidatorModel):
    ResourceIdPreference: ResourceIdPreference
    ResponseMetadata: ResponseMetadata


class DescribeMountTargetsResponse(BaseValidatorModel):
    Marker: str
    MountTargets: List[MountTargetDescription]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ReplicationConfigurationDescriptionResponse(BaseValidatorModel):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[Destination]
    SourceFileSystemOwnerId: str
    ResponseMetadata: ResponseMetadata


class ReplicationConfigurationDescription(BaseValidatorModel):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[Destination]
    SourceFileSystemOwnerId: Optional[str] = None


class FileSystemDescriptionResponse(BaseValidatorModel):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    FileSystemArn: str
    CreationTime: datetime
    LifeCycleState: LifeCycleStateType
    Name: str
    NumberOfMountTargets: int
    SizeInBytes: FileSystemSize
    PerformanceMode: PerformanceModeType
    Encrypted: bool
    KmsKeyId: str
    ThroughputMode: ThroughputModeType
    ProvisionedThroughputInMibps: float
    AvailabilityZoneName: str
    AvailabilityZoneId: str
    Tags: List[Tag]
    FileSystemProtection: FileSystemProtectionDescription
    ResponseMetadata: ResponseMetadata


class FileSystemDescription(BaseValidatorModel):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    CreationTime: datetime
    LifeCycleState: LifeCycleStateType
    NumberOfMountTargets: int
    SizeInBytes: FileSystemSize
    PerformanceMode: PerformanceModeType
    Tags: List[Tag]
    FileSystemArn: Optional[str] = None
    Name: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None
    AvailabilityZoneName: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    FileSystemProtection: Optional[FileSystemProtectionDescription] = None


class LifecycleConfigurationDescription(BaseValidatorModel):
    LifecyclePolicies: List[LifecyclePolicy]
    ResponseMetadata: ResponseMetadata


class PutLifecycleConfigurationRequest(BaseValidatorModel):
    FileSystemId: str
    LifecyclePolicies: List[LifecyclePolicy]

PosixUserUnion = Union[PosixUser, PosixUserOutput]


class AccessPointDescriptionResponse(BaseValidatorModel):
    ClientToken: str
    Name: str
    Tags: List[Tag]
    AccessPointId: str
    AccessPointArn: str
    FileSystemId: str
    PosixUser: PosixUserOutput
    RootDirectory: RootDirectory
    OwnerId: str
    LifeCycleState: LifeCycleStateType
    ResponseMetadata: ResponseMetadata


class AccessPointDescription(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    AccessPointId: Optional[str] = None
    AccessPointArn: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[PosixUserOutput] = None
    RootDirectory: Optional[RootDirectory] = None
    OwnerId: Optional[str] = None
    LifeCycleState: Optional[LifeCycleStateType] = None


class DescribeReplicationConfigurationsResponse(BaseValidatorModel):
    Replications: List[ReplicationConfigurationDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFileSystemsResponse(BaseValidatorModel):
    Marker: str
    FileSystems: List[FileSystemDescription]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class CreateAccessPointRequest(BaseValidatorModel):
    ClientToken: str
    FileSystemId: str
    Tags: Optional[List[Tag]] = None
    PosixUser: Optional[PosixUserUnion] = None
    RootDirectory: Optional[RootDirectory] = None


class DescribeAccessPointsResponse(BaseValidatorModel):
    AccessPoints: List[AccessPointDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None