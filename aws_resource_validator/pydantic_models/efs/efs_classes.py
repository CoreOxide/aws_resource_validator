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


# This class is the input for the 'create_mount_target' function.
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


# This class is the input for the 'delete_access_point' function.
class DeleteAccessPointRequest(BaseValidatorModel):
    AccessPointId: str


# This class is the input for the 'delete_file_system_policy' function.
class DeleteFileSystemPolicyRequest(BaseValidatorModel):
    FileSystemId: str


# This class is the input for the 'delete_file_system' function.
class DeleteFileSystemRequest(BaseValidatorModel):
    FileSystemId: str


# This class is the input for the 'delete_mount_target' function.
class DeleteMountTargetRequest(BaseValidatorModel):
    MountTargetId: str


# This class is the input for the 'delete_replication_configuration' function.
class DeleteReplicationConfigurationRequest(BaseValidatorModel):
    SourceFileSystemId: str
    DeletionMode: Optional[DeletionModeType] = None


# This class is the input for the 'delete_tags' function.
class DeleteTagsRequest(BaseValidatorModel):
    FileSystemId: str
    TagKeys: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_access_points' function.
class DescribeAccessPointsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccessPointId: Optional[str] = None
    FileSystemId: Optional[str] = None


# This class is the input for the 'describe_account_preferences' function.
class DescribeAccountPreferencesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceIdPreference(BaseValidatorModel):
    ResourceIdType: Optional[ResourceIdTypeType] = None
    Resources: Optional[List[ResourceType]] = None


# This class is the input for the 'describe_backup_policy' function.
class DescribeBackupPolicyRequest(BaseValidatorModel):
    FileSystemId: str


# This class is the input for the 'describe_file_system_policy' function.
class DescribeFileSystemPolicyRequest(BaseValidatorModel):
    FileSystemId: str


# This class is the input for the 'describe_file_systems' function.
class DescribeFileSystemsRequest(BaseValidatorModel):
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    CreationToken: Optional[str] = None
    FileSystemId: Optional[str] = None


# This class is the input for the 'describe_lifecycle_configuration' function.
class DescribeLifecycleConfigurationRequest(BaseValidatorModel):
    FileSystemId: str


# This class is the input for the 'describe_mount_target_security_groups' function.
class DescribeMountTargetSecurityGroupsRequest(BaseValidatorModel):
    MountTargetId: str


# This class is the input for the 'describe_mount_targets' function.
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


# This class is the input for the 'describe_replication_configurations' function.
class DescribeReplicationConfigurationsRequest(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_tags' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'modify_mount_target_security_groups' function.
class ModifyMountTargetSecurityGroupsRequest(BaseValidatorModel):
    MountTargetId: str
    SecurityGroups: Optional[List[str]] = None


class PosixUser(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None


# This class is the input for the 'put_account_preferences' function.
class PutAccountPreferencesRequest(BaseValidatorModel):
    ResourceIdType: ResourceIdTypeType


# This class is the input for the 'put_file_system_policy' function.
class PutFileSystemPolicyRequest(BaseValidatorModel):
    FileSystemId: str
    Policy: str
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: List[str]


# This class is the input for the 'update_file_system_protection' function.
class UpdateFileSystemProtectionRequest(BaseValidatorModel):
    FileSystemId: str
    ReplicationOverwriteProtection: Optional[ReplicationOverwriteProtectionType] = None


# This class is the input for the 'update_file_system' function.
class UpdateFileSystemRequest(BaseValidatorModel):
    FileSystemId: str
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedThroughputInMibps: Optional[float] = None


# This class is the output for the 'describe_mount_target_security_groups' function.
class DescribeMountTargetSecurityGroupsResponse(BaseValidatorModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_file_system_policy' function.
class FileSystemPolicyDescription(BaseValidatorModel):
    FileSystemId: str
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_file_system_protection' function.
class FileSystemProtectionDescriptionResponse(BaseValidatorModel):
    ReplicationOverwriteProtection: ReplicationOverwriteProtectionType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_mount_target' function.
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


# This class is the input for the 'create_file_system' function.
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


# This class is the input for the 'create_tags' function.
class CreateTagsRequest(BaseValidatorModel):
    FileSystemId: str
    Tags: List[Tag]


# This class is the output for the 'describe_tags' function.
class DescribeTagsResponse(BaseValidatorModel):
    Marker: str
    Tags: List[Tag]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceId: str
    Tags: List[Tag]


# This class is the output for the 'put_backup_policy' function.
class BackupPolicyDescription(BaseValidatorModel):
    BackupPolicy: BackupPolicy
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_backup_policy' function.
class PutBackupPolicyRequest(BaseValidatorModel):
    FileSystemId: str
    BackupPolicy: BackupPolicy


# This class is the input for the 'create_replication_configuration' function.
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


# This class is the output for the 'describe_account_preferences' function.
class DescribeAccountPreferencesResponse(BaseValidatorModel):
    ResourceIdPreference: ResourceIdPreference
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_account_preferences' function.
class PutAccountPreferencesResponse(BaseValidatorModel):
    ResourceIdPreference: ResourceIdPreference
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_mount_targets' function.
class DescribeMountTargetsResponse(BaseValidatorModel):
    Marker: str
    MountTargets: List[MountTargetDescription]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_replication_configuration' function.
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


# This class is the output for the 'update_file_system' function.
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


# This class is the output for the 'put_lifecycle_configuration' function.
class LifecycleConfigurationDescription(BaseValidatorModel):
    LifecyclePolicies: List[LifecyclePolicy]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_lifecycle_configuration' function.
class PutLifecycleConfigurationRequest(BaseValidatorModel):
    FileSystemId: str
    LifecyclePolicies: List[LifecyclePolicy]

PosixUserUnion = Union[PosixUser, PosixUserOutput]


# This class is the output for the 'create_access_point' function.
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


# This class is the output for the 'describe_replication_configurations' function.
class DescribeReplicationConfigurationsResponse(BaseValidatorModel):
    Replications: List[ReplicationConfigurationDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_file_systems' function.
class DescribeFileSystemsResponse(BaseValidatorModel):
    Marker: str
    FileSystems: List[FileSystemDescription]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_access_point' function.
class CreateAccessPointRequest(BaseValidatorModel):
    ClientToken: str
    FileSystemId: str
    Tags: Optional[List[Tag]] = None
    PosixUser: Optional[PosixUserUnion] = None
    RootDirectory: Optional[RootDirectory] = None


# This class is the output for the 'describe_access_points' function.
class DescribeAccessPointsResponse(BaseValidatorModel):
    AccessPoints: List[AccessPointDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None