from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.storagegateway.storagegateway_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'add_cache' function.
class AddCacheInput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]


# This class is the input for the 'add_upload_buffer' function.
class AddUploadBufferInput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]


# This class is the input for the 'add_working_storage' function.
class AddWorkingStorageInput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]


# This class is the input for the 'assign_tape_pool' function.
class AssignTapePoolInput(BaseValidatorModel):
    TapeARN: str
    PoolId: str
    BypassGovernanceRetention: Optional[bool] = None


class CacheAttributes(BaseValidatorModel):
    CacheStaleTimeoutInSeconds: Optional[int] = None


# This class is the input for the 'attach_volume' function.
class AttachVolumeInput(BaseValidatorModel):
    GatewayARN: str
    VolumeARN: str
    NetworkInterfaceId: str
    TargetName: Optional[str] = None
    DiskId: Optional[str] = None


class AutomaticTapeCreationRule(BaseValidatorModel):
    TapeBarcodePrefix: str
    PoolId: str
    TapeSizeInBytes: int
    MinimumNumTapes: int
    Worm: Optional[bool] = None


class BandwidthRateLimitIntervalOutput(BaseValidatorModel):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: List[int]
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


class BandwidthRateLimitInterval(BaseValidatorModel):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: List[int]
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


class CacheReportFilterOutput(BaseValidatorModel):
    Name: CacheReportFilterNameType
    Values: List[str]


class CacheReportFilter(BaseValidatorModel):
    Name: CacheReportFilterNameType
    Values: List[str]


class VolumeiSCSIAttributes(BaseValidatorModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    LunNumber: Optional[int] = None
    ChapEnabled: Optional[bool] = None


# This class is the input for the 'cancel_archival' function.
class CancelArchivalInput(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str


# This class is the input for the 'cancel_cache_report' function.
class CancelCacheReportInput(BaseValidatorModel):
    CacheReportARN: str


# This class is the input for the 'cancel_retrieval' function.
class CancelRetrievalInput(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str


class ChapInfo(BaseValidatorModel):
    TargetARN: Optional[str] = None
    SecretToAuthenticateInitiator: Optional[str] = None
    InitiatorName: Optional[str] = None
    SecretToAuthenticateTarget: Optional[str] = None


class NFSFileShareDefaults(BaseValidatorModel):
    FileMode: Optional[str] = None
    DirectoryMode: Optional[str] = None
    GroupId: Optional[int] = None
    OwnerId: Optional[int] = None


# This class is the input for the 'delete_automatic_tape_creation_policy' function.
class DeleteAutomaticTapeCreationPolicyInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'delete_bandwidth_rate_limit' function.
class DeleteBandwidthRateLimitInput(BaseValidatorModel):
    GatewayARN: str
    BandwidthType: str


# This class is the input for the 'delete_cache_report' function.
class DeleteCacheReportInput(BaseValidatorModel):
    CacheReportARN: str


# This class is the input for the 'delete_chap_credentials' function.
class DeleteChapCredentialsInput(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str


# This class is the input for the 'delete_file_share' function.
class DeleteFileShareInput(BaseValidatorModel):
    FileShareARN: str
    ForceDelete: Optional[bool] = None


# This class is the input for the 'delete_gateway' function.
class DeleteGatewayInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'delete_snapshot_schedule' function.
class DeleteSnapshotScheduleInput(BaseValidatorModel):
    VolumeARN: str


# This class is the input for the 'delete_tape_archive' function.
class DeleteTapeArchiveInput(BaseValidatorModel):
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None


# This class is the input for the 'delete_tape' function.
class DeleteTapeInput(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None


# This class is the input for the 'delete_tape_pool' function.
class DeleteTapePoolInput(BaseValidatorModel):
    PoolARN: str


# This class is the input for the 'delete_volume' function.
class DeleteVolumeInput(BaseValidatorModel):
    VolumeARN: str


# This class is the input for the 'describe_availability_monitor_test' function.
class DescribeAvailabilityMonitorTestInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'describe_bandwidth_rate_limit' function.
class DescribeBandwidthRateLimitInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'describe_bandwidth_rate_limit_schedule' function.
class DescribeBandwidthRateLimitScheduleInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'describe_cache' function.
class DescribeCacheInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'describe_cache_report' function.
class DescribeCacheReportInput(BaseValidatorModel):
    CacheReportARN: str


# This class is the input for the 'describe_cached_iscsi_volumes' function.
class DescribeCachediSCSIVolumesInput(BaseValidatorModel):
    VolumeARNs: List[str]


# This class is the input for the 'describe_chap_credentials' function.
class DescribeChapCredentialsInput(BaseValidatorModel):
    TargetARN: str


# This class is the input for the 'describe_file_system_associations' function.
class DescribeFileSystemAssociationsInput(BaseValidatorModel):
    FileSystemAssociationARNList: List[str]


# This class is the input for the 'describe_gateway_information' function.
class DescribeGatewayInformationInput(BaseValidatorModel):
    GatewayARN: str


class NetworkInterface(BaseValidatorModel):
    Ipv4Address: Optional[str] = None
    MacAddress: Optional[str] = None
    Ipv6Address: Optional[str] = None


# This class is the input for the 'describe_maintenance_start_time' function.
class DescribeMaintenanceStartTimeInput(BaseValidatorModel):
    GatewayARN: str


class SoftwareUpdatePreferences(BaseValidatorModel):
    AutomaticUpdatePolicy: Optional[AutomaticUpdatePolicyType] = None


# This class is the input for the 'describe_nfs_file_shares' function.
class DescribeNFSFileSharesInput(BaseValidatorModel):
    FileShareARNList: List[str]


# This class is the input for the 'describe_smb_file_shares' function.
class DescribeSMBFileSharesInput(BaseValidatorModel):
    FileShareARNList: List[str]


# This class is the input for the 'describe_smb_settings' function.
class DescribeSMBSettingsInput(BaseValidatorModel):
    GatewayARN: str


class SMBLocalGroupsOutput(BaseValidatorModel):
    GatewayAdmins: Optional[List[str]] = None


# This class is the input for the 'describe_snapshot_schedule' function.
class DescribeSnapshotScheduleInput(BaseValidatorModel):
    VolumeARN: str


# This class is the input for the 'describe_stored_iscsi_volumes' function.
class DescribeStorediSCSIVolumesInput(BaseValidatorModel):
    VolumeARNs: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_tape_archives' function.
class DescribeTapeArchivesInput(BaseValidatorModel):
    TapeARNs: Optional[List[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeArchive(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeBarcode: Optional[str] = None
    TapeCreatedDate: Optional[datetime] = None
    TapeSizeInBytes: Optional[int] = None
    CompletionTime: Optional[datetime] = None
    RetrievedTo: Optional[str] = None
    TapeStatus: Optional[str] = None
    TapeUsedInBytes: Optional[int] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    RetentionStartDate: Optional[datetime] = None
    PoolEntryDate: Optional[datetime] = None


# This class is the input for the 'describe_tape_recovery_points' function.
class DescribeTapeRecoveryPointsInput(BaseValidatorModel):
    GatewayARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeRecoveryPointInfo(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeRecoveryPointTime: Optional[datetime] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None


# This class is the input for the 'describe_tapes' function.
class DescribeTapesInput(BaseValidatorModel):
    GatewayARN: str
    TapeARNs: Optional[List[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class Tape(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeBarcode: Optional[str] = None
    TapeCreatedDate: Optional[datetime] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None
    VTLDevice: Optional[str] = None
    Progress: Optional[float] = None
    TapeUsedInBytes: Optional[int] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    RetentionStartDate: Optional[datetime] = None
    PoolEntryDate: Optional[datetime] = None


# This class is the input for the 'describe_upload_buffer' function.
class DescribeUploadBufferInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'describe_vtl_devices' function.
class DescribeVTLDevicesInput(BaseValidatorModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[List[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_working_storage' function.
class DescribeWorkingStorageInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'detach_volume' function.
class DetachVolumeInput(BaseValidatorModel):
    VolumeARN: str
    ForceDetach: Optional[bool] = None


class DeviceiSCSIAttributes(BaseValidatorModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    ChapEnabled: Optional[bool] = None


# This class is the input for the 'disable_gateway' function.
class DisableGatewayInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'disassociate_file_system' function.
class DisassociateFileSystemInput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ForceDelete: Optional[bool] = None


class Disk(BaseValidatorModel):
    DiskId: Optional[str] = None
    DiskPath: Optional[str] = None
    DiskNode: Optional[str] = None
    DiskStatus: Optional[str] = None
    DiskSizeInBytes: Optional[int] = None
    DiskAllocationType: Optional[str] = None
    DiskAllocationResource: Optional[str] = None
    DiskAttributeList: Optional[List[str]] = None


class EndpointNetworkConfigurationOutput(BaseValidatorModel):
    IpAddresses: Optional[List[str]] = None


class EndpointNetworkConfiguration(BaseValidatorModel):
    IpAddresses: Optional[List[str]] = None


# This class is the input for the 'evict_files_failing_upload' function.
class EvictFilesFailingUploadInput(BaseValidatorModel):
    FileShareARN: str
    ForceRemove: Optional[bool] = None


class FileShareInfo(BaseValidatorModel):
    FileShareType: Optional[FileShareTypeType] = None
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None


class FileSystemAssociationStatusDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None


class FileSystemAssociationSummary(BaseValidatorModel):
    FileSystemAssociationId: Optional[str] = None
    FileSystemAssociationARN: Optional[str] = None
    FileSystemAssociationStatus: Optional[str] = None
    GatewayARN: Optional[str] = None


class GatewayInfo(BaseValidatorModel):
    GatewayId: Optional[str] = None
    GatewayARN: Optional[str] = None
    GatewayType: Optional[str] = None
    GatewayOperationalState: Optional[str] = None
    GatewayName: Optional[str] = None
    Ec2InstanceId: Optional[str] = None
    Ec2InstanceRegion: Optional[str] = None
    HostEnvironment: Optional[HostEnvironmentType] = None
    HostEnvironmentId: Optional[str] = None
    DeprecationDate: Optional[str] = None
    SoftwareVersion: Optional[str] = None


# This class is the input for the 'join_domain' function.
class JoinDomainInput(BaseValidatorModel):
    GatewayARN: str
    DomainName: str
    UserName: str
    Password: str
    OrganizationalUnit: Optional[str] = None
    DomainControllers: Optional[List[str]] = None
    TimeoutInSeconds: Optional[int] = None


# This class is the input for the 'list_automatic_tape_creation_policies' function.
class ListAutomaticTapeCreationPoliciesInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None


# This class is the input for the 'list_cache_reports' function.
class ListCacheReportsInput(BaseValidatorModel):
    Marker: Optional[str] = None


# This class is the input for the 'list_file_shares' function.
class ListFileSharesInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'list_file_system_associations' function.
class ListFileSystemAssociationsInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'list_gateways' function.
class ListGatewaysInput(BaseValidatorModel):
    Marker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_local_disks' function.
class ListLocalDisksInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    ResourceARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_tape_pools' function.
class ListTapePoolsInput(BaseValidatorModel):
    PoolARNs: Optional[List[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class PoolInfo(BaseValidatorModel):
    PoolARN: Optional[str] = None
    PoolName: Optional[str] = None
    StorageClass: Optional[TapeStorageClassType] = None
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    PoolStatus: Optional[PoolStatusType] = None


# This class is the input for the 'list_tapes' function.
class ListTapesInput(BaseValidatorModel):
    TapeARNs: Optional[List[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeInfo(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeBarcode: Optional[str] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
    PoolId: Optional[str] = None
    RetentionStartDate: Optional[datetime] = None
    PoolEntryDate: Optional[datetime] = None


# This class is the input for the 'list_volume_initiators' function.
class ListVolumeInitiatorsInput(BaseValidatorModel):
    VolumeARN: str


# This class is the input for the 'list_volume_recovery_points' function.
class ListVolumeRecoveryPointsInput(BaseValidatorModel):
    GatewayARN: str


class VolumeRecoveryPointInfo(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeUsageInBytes: Optional[int] = None
    VolumeRecoveryPointTime: Optional[str] = None


# This class is the input for the 'list_volumes' function.
class ListVolumesInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class VolumeInfo(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeId: Optional[str] = None
    GatewayARN: Optional[str] = None
    GatewayId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeAttachmentStatus: Optional[str] = None


# This class is the input for the 'notify_when_uploaded' function.
class NotifyWhenUploadedInput(BaseValidatorModel):
    FileShareARN: str


# This class is the input for the 'refresh_cache' function.
class RefreshCacheInput(BaseValidatorModel):
    FileShareARN: str
    FolderList: Optional[List[str]] = None
    Recursive: Optional[bool] = None


# This class is the input for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'reset_cache' function.
class ResetCacheInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'retrieve_tape_archive' function.
class RetrieveTapeArchiveInput(BaseValidatorModel):
    TapeARN: str
    GatewayARN: str


# This class is the input for the 'retrieve_tape_recovery_point' function.
class RetrieveTapeRecoveryPointInput(BaseValidatorModel):
    TapeARN: str
    GatewayARN: str


class SMBLocalGroups(BaseValidatorModel):
    GatewayAdmins: Optional[List[str]] = None


# This class is the input for the 'set_local_console_password' function.
class SetLocalConsolePasswordInput(BaseValidatorModel):
    GatewayARN: str
    LocalConsolePassword: str


# This class is the input for the 'set_smb_guest_password' function.
class SetSMBGuestPasswordInput(BaseValidatorModel):
    GatewayARN: str
    Password: str


# This class is the input for the 'shutdown_gateway' function.
class ShutdownGatewayInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'start_availability_monitor_test' function.
class StartAvailabilityMonitorTestInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'start_gateway' function.
class StartGatewayInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'update_bandwidth_rate_limit' function.
class UpdateBandwidthRateLimitInput(BaseValidatorModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


# This class is the input for the 'update_chap_credentials' function.
class UpdateChapCredentialsInput(BaseValidatorModel):
    TargetARN: str
    SecretToAuthenticateInitiator: str
    InitiatorName: str
    SecretToAuthenticateTarget: Optional[str] = None


# This class is the input for the 'update_gateway_information' function.
class UpdateGatewayInformationInput(BaseValidatorModel):
    GatewayARN: str
    GatewayName: Optional[str] = None
    GatewayTimezone: Optional[str] = None
    CloudWatchLogGroupARN: Optional[str] = None
    GatewayCapacity: Optional[GatewayCapacityType] = None


# This class is the input for the 'update_gateway_software_now' function.
class UpdateGatewaySoftwareNowInput(BaseValidatorModel):
    GatewayARN: str


# This class is the input for the 'update_smb_file_share_visibility' function.
class UpdateSMBFileShareVisibilityInput(BaseValidatorModel):
    GatewayARN: str
    FileSharesVisible: bool


# This class is the input for the 'update_smb_security_strategy' function.
class UpdateSMBSecurityStrategyInput(BaseValidatorModel):
    GatewayARN: str
    SMBSecurityStrategy: SMBSecurityStrategyType


# This class is the input for the 'update_vtl_device_type' function.
class UpdateVTLDeviceTypeInput(BaseValidatorModel):
    VTLDeviceARN: str
    DeviceType: str


# This class is the input for the 'activate_gateway' function.
class ActivateGatewayInput(BaseValidatorModel):
    ActivationKey: str
    GatewayName: str
    GatewayTimezone: str
    GatewayRegion: str
    GatewayType: Optional[str] = None
    TapeDriveType: Optional[str] = None
    MediumChangerType: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'add_tags_to_resource' function.
class AddTagsToResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the input for the 'create_cached_iscsi_volume' function.
class CreateCachediSCSIVolumeInput(BaseValidatorModel):
    GatewayARN: str
    VolumeSizeInBytes: int
    TargetName: str
    NetworkInterfaceId: str
    ClientToken: str
    SnapshotId: Optional[str] = None
    SourceVolumeARN: Optional[str] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_snapshot_from_volume_recovery_point' function.
class CreateSnapshotFromVolumeRecoveryPointInput(BaseValidatorModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotInput(BaseValidatorModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_stored_iscsi_volume' function.
class CreateStorediSCSIVolumeInput(BaseValidatorModel):
    GatewayARN: str
    DiskId: str
    PreserveExistingData: bool
    TargetName: str
    NetworkInterfaceId: str
    SnapshotId: Optional[str] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_tape_pool' function.
class CreateTapePoolInput(BaseValidatorModel):
    PoolName: str
    StorageClass: TapeStorageClassType
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_tape_with_barcode' function.
class CreateTapeWithBarcodeInput(BaseValidatorModel):
    GatewayARN: str
    TapeSizeInBytes: int
    TapeBarcode: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_tapes' function.
class CreateTapesInput(BaseValidatorModel):
    GatewayARN: str
    TapeSizeInBytes: int
    ClientToken: str
    NumTapesToCreate: int
    TapeBarcodePrefix: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_snapshot_schedule' function.
class UpdateSnapshotScheduleInput(BaseValidatorModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'activate_gateway' function.
class ActivateGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_cache' function.
class AddCacheOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_tags_to_resource' function.
class AddTagsToResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_upload_buffer' function.
class AddUploadBufferOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_working_storage' function.
class AddWorkingStorageOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'assign_tape_pool' function.
class AssignTapePoolOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_file_system' function.
class AssociateFileSystemOutput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_volume' function.
class AttachVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_archival' function.
class CancelArchivalOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_cache_report' function.
class CancelCacheReportOutput(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_retrieval' function.
class CancelRetrievalOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cached_iscsi_volume' function.
class CreateCachediSCSIVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_nfs_file_share' function.
class CreateNFSFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_smb_file_share' function.
class CreateSMBFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_snapshot_from_volume_recovery_point' function.
class CreateSnapshotFromVolumeRecoveryPointOutput(BaseValidatorModel):
    SnapshotId: str
    VolumeARN: str
    VolumeRecoveryPointTime: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_snapshot' function.
class CreateSnapshotOutput(BaseValidatorModel):
    VolumeARN: str
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stored_iscsi_volume' function.
class CreateStorediSCSIVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    VolumeSizeInBytes: int
    TargetARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_tape_pool' function.
class CreateTapePoolOutput(BaseValidatorModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_tape_with_barcode' function.
class CreateTapeWithBarcodeOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_tapes' function.
class CreateTapesOutput(BaseValidatorModel):
    TapeARNs: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_automatic_tape_creation_policy' function.
class DeleteAutomaticTapeCreationPolicyOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bandwidth_rate_limit' function.
class DeleteBandwidthRateLimitOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cache_report' function.
class DeleteCacheReportOutput(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_chap_credentials' function.
class DeleteChapCredentialsOutput(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_file_share' function.
class DeleteFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_gateway' function.
class DeleteGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot_schedule' function.
class DeleteSnapshotScheduleOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_tape_archive' function.
class DeleteTapeArchiveOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_tape' function.
class DeleteTapeOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_tape_pool' function.
class DeleteTapePoolOutput(BaseValidatorModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_volume' function.
class DeleteVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_availability_monitor_test' function.
class DescribeAvailabilityMonitorTestOutput(BaseValidatorModel):
    GatewayARN: str
    Status: AvailabilityMonitorTestStatusType
    StartTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bandwidth_rate_limit' function.
class DescribeBandwidthRateLimitOutput(BaseValidatorModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cache' function.
class DescribeCacheOutput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    CacheAllocatedInBytes: int
    CacheUsedPercentage: float
    CacheDirtyPercentage: float
    CacheHitPercentage: float
    CacheMissPercentage: float
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshot_schedule' function.
class DescribeSnapshotScheduleOutput(BaseValidatorModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: str
    Timezone: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_upload_buffer' function.
class DescribeUploadBufferOutput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    UploadBufferUsedInBytes: int
    UploadBufferAllocatedInBytes: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_working_storage' function.
class DescribeWorkingStorageOutput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    WorkingStorageUsedInBytes: int
    WorkingStorageAllocatedInBytes: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_volume' function.
class DetachVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_gateway' function.
class DisableGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_file_system' function.
class DisassociateFileSystemOutput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'evict_files_failing_upload' function.
class EvictFilesFailingUploadOutput(BaseValidatorModel):
    NotificationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'join_domain' function.
class JoinDomainOutput(BaseValidatorModel):
    GatewayARN: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    ResourceARN: str
    Marker: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_volume_initiators' function.
class ListVolumeInitiatorsOutput(BaseValidatorModel):
    Initiators: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'notify_when_uploaded' function.
class NotifyWhenUploadedOutput(BaseValidatorModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'refresh_cache' function.
class RefreshCacheOutput(BaseValidatorModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_cache' function.
class ResetCacheOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'retrieve_tape_archive' function.
class RetrieveTapeArchiveOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'retrieve_tape_recovery_point' function.
class RetrieveTapeRecoveryPointOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_local_console_password' function.
class SetLocalConsolePasswordOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_smb_guest_password' function.
class SetSMBGuestPasswordOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'shutdown_gateway' function.
class ShutdownGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_availability_monitor_test' function.
class StartAvailabilityMonitorTestOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_cache_report' function.
class StartCacheReportOutput(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_gateway' function.
class StartGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_automatic_tape_creation_policy' function.
class UpdateAutomaticTapeCreationPolicyOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bandwidth_rate_limit' function.
class UpdateBandwidthRateLimitOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bandwidth_rate_limit_schedule' function.
class UpdateBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_chap_credentials' function.
class UpdateChapCredentialsOutput(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_file_system_association' function.
class UpdateFileSystemAssociationOutput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_gateway_information' function.
class UpdateGatewayInformationOutput(BaseValidatorModel):
    GatewayARN: str
    GatewayName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_gateway_software_now' function.
class UpdateGatewaySoftwareNowOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_maintenance_start_time' function.
class UpdateMaintenanceStartTimeOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_nfs_file_share' function.
class UpdateNFSFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_smb_file_share' function.
class UpdateSMBFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_smb_file_share_visibility' function.
class UpdateSMBFileShareVisibilityOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_smb_local_groups' function.
class UpdateSMBLocalGroupsOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_smb_security_strategy' function.
class UpdateSMBSecurityStrategyOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_snapshot_schedule' function.
class UpdateSnapshotScheduleOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vtl_device_type' function.
class UpdateVTLDeviceTypeOutput(BaseValidatorModel):
    VTLDeviceARN: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_smb_file_share' function.
class CreateSMBFileShareInput(BaseValidatorModel):
    ClientToken: str
    GatewayARN: str
    Role: str
    LocationARN: str
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    SMBACLEnabled: Optional[bool] = None
    AccessBasedEnumeration: Optional[bool] = None
    AdminUserList: Optional[List[str]] = None
    ValidUserList: Optional[List[str]] = None
    InvalidUserList: Optional[List[str]] = None
    AuditDestinationARN: Optional[str] = None
    Authentication: Optional[str] = None
    CaseSensitivity: Optional[CaseSensitivityType] = None
    Tags: Optional[List[Tag]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    OplocksEnabled: Optional[bool] = None


class SMBFileShareInfo(BaseValidatorModel):
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Path: Optional[str] = None
    Role: Optional[str] = None
    LocationARN: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    SMBACLEnabled: Optional[bool] = None
    AccessBasedEnumeration: Optional[bool] = None
    AdminUserList: Optional[List[str]] = None
    ValidUserList: Optional[List[str]] = None
    InvalidUserList: Optional[List[str]] = None
    AuditDestinationARN: Optional[str] = None
    Authentication: Optional[str] = None
    CaseSensitivity: Optional[CaseSensitivityType] = None
    Tags: Optional[List[Tag]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    OplocksEnabled: Optional[bool] = None


# This class is the input for the 'update_file_system_association' function.
class UpdateFileSystemAssociationInput(BaseValidatorModel):
    FileSystemAssociationARN: str
    UserName: Optional[str] = None
    Password: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None


# This class is the input for the 'update_smb_file_share' function.
class UpdateSMBFileShareInput(BaseValidatorModel):
    FileShareARN: str
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    SMBACLEnabled: Optional[bool] = None
    AccessBasedEnumeration: Optional[bool] = None
    AdminUserList: Optional[List[str]] = None
    ValidUserList: Optional[List[str]] = None
    InvalidUserList: Optional[List[str]] = None
    AuditDestinationARN: Optional[str] = None
    CaseSensitivity: Optional[CaseSensitivityType] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    NotificationPolicy: Optional[str] = None
    OplocksEnabled: Optional[bool] = None


class AutomaticTapeCreationPolicyInfo(BaseValidatorModel):
    AutomaticTapeCreationRules: Optional[List[AutomaticTapeCreationRule]] = None
    GatewayARN: Optional[str] = None


# This class is the input for the 'update_automatic_tape_creation_policy' function.
class UpdateAutomaticTapeCreationPolicyInput(BaseValidatorModel):
    AutomaticTapeCreationRules: List[AutomaticTapeCreationRule]
    GatewayARN: str


# This class is the output for the 'describe_bandwidth_rate_limit_schedule' function.
class DescribeBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutput]
    ResponseMetadata: ResponseMetadata

BandwidthRateLimitIntervalUnion = Union[BandwidthRateLimitInterval, BandwidthRateLimitIntervalOutput]


class CacheReportInfo(BaseValidatorModel):
    CacheReportARN: Optional[str] = None
    CacheReportStatus: Optional[CacheReportStatusType] = None
    ReportCompletionPercent: Optional[int] = None
    EndTime: Optional[datetime] = None
    Role: Optional[str] = None
    FileShareARN: Optional[str] = None
    LocationARN: Optional[str] = None
    StartTime: Optional[datetime] = None
    InclusionFilters: Optional[List[CacheReportFilterOutput]] = None
    ExclusionFilters: Optional[List[CacheReportFilterOutput]] = None
    ReportName: Optional[str] = None
    Tags: Optional[List[Tag]] = None

CacheReportFilterUnion = Union[CacheReportFilter, CacheReportFilterOutput]


class CachediSCSIVolume(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeStatus: Optional[str] = None
    VolumeAttachmentStatus: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeProgress: Optional[float] = None
    SourceSnapshotId: Optional[str] = None
    VolumeiSCSIAttributes: Optional[VolumeiSCSIAttributes] = None
    CreatedDate: Optional[datetime] = None
    VolumeUsedInBytes: Optional[int] = None
    KMSKey: Optional[str] = None
    TargetName: Optional[str] = None


class StorediSCSIVolume(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeStatus: Optional[str] = None
    VolumeAttachmentStatus: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeProgress: Optional[float] = None
    VolumeDiskId: Optional[str] = None
    SourceSnapshotId: Optional[str] = None
    PreservedExistingData: Optional[bool] = None
    VolumeiSCSIAttributes: Optional[VolumeiSCSIAttributes] = None
    CreatedDate: Optional[datetime] = None
    VolumeUsedInBytes: Optional[int] = None
    KMSKey: Optional[str] = None
    TargetName: Optional[str] = None


# This class is the output for the 'describe_chap_credentials' function.
class DescribeChapCredentialsOutput(BaseValidatorModel):
    ChapCredentials: List[ChapInfo]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_nfs_file_share' function.
class CreateNFSFileShareInput(BaseValidatorModel):
    ClientToken: str
    GatewayARN: str
    Role: str
    LocationARN: str
    NFSFileShareDefaults: Optional[NFSFileShareDefaults] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ClientList: Optional[List[str]] = None
    Squash: Optional[str] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    AuditDestinationARN: Optional[str] = None


class NFSFileShareInfo(BaseValidatorModel):
    NFSFileShareDefaults: Optional[NFSFileShareDefaults] = None
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Path: Optional[str] = None
    Role: Optional[str] = None
    LocationARN: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ClientList: Optional[List[str]] = None
    Squash: Optional[str] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    AuditDestinationARN: Optional[str] = None


# This class is the input for the 'update_nfs_file_share' function.
class UpdateNFSFileShareInput(BaseValidatorModel):
    FileShareARN: str
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    NFSFileShareDefaults: Optional[NFSFileShareDefaults] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ClientList: Optional[List[str]] = None
    Squash: Optional[str] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    NotificationPolicy: Optional[str] = None
    AuditDestinationARN: Optional[str] = None


# This class is the output for the 'describe_gateway_information' function.
class DescribeGatewayInformationOutput(BaseValidatorModel):
    GatewayARN: str
    GatewayId: str
    GatewayName: str
    GatewayTimezone: str
    GatewayState: str
    GatewayNetworkInterfaces: List[NetworkInterface]
    GatewayType: str
    NextUpdateAvailabilityDate: str
    LastSoftwareUpdate: str
    Ec2InstanceId: str
    Ec2InstanceRegion: str
    Tags: List[Tag]
    VPCEndpoint: str
    CloudWatchLogGroupARN: str
    HostEnvironment: HostEnvironmentType
    EndpointType: str
    SoftwareUpdatesEndDate: str
    DeprecationDate: str
    GatewayCapacity: GatewayCapacityType
    SupportedGatewayCapacities: List[GatewayCapacityType]
    HostEnvironmentId: str
    SoftwareVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_maintenance_start_time' function.
class DescribeMaintenanceStartTimeOutput(BaseValidatorModel):
    GatewayARN: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfWeek: int
    DayOfMonth: int
    Timezone: str
    SoftwareUpdatePreferences: SoftwareUpdatePreferences
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_maintenance_start_time' function.
class UpdateMaintenanceStartTimeInput(BaseValidatorModel):
    GatewayARN: str
    HourOfDay: Optional[int] = None
    MinuteOfHour: Optional[int] = None
    DayOfWeek: Optional[int] = None
    DayOfMonth: Optional[int] = None
    SoftwareUpdatePreferences: Optional[SoftwareUpdatePreferences] = None


# This class is the output for the 'describe_smb_settings' function.
class DescribeSMBSettingsOutput(BaseValidatorModel):
    GatewayARN: str
    DomainName: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    SMBGuestPasswordSet: bool
    SMBSecurityStrategy: SMBSecurityStrategyType
    FileSharesVisible: bool
    SMBLocalGroups: SMBLocalGroupsOutput
    ResponseMetadata: ResponseMetadata


class DescribeTapeArchivesInputPaginate(BaseValidatorModel):
    TapeARNs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTapeRecoveryPointsInputPaginate(BaseValidatorModel):
    GatewayARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTapesInputPaginate(BaseValidatorModel):
    GatewayARN: str
    TapeARNs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeVTLDevicesInputPaginate(BaseValidatorModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFileSharesInputPaginate(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFileSystemAssociationsInputPaginate(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGatewaysInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceInputPaginate(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTapePoolsInputPaginate(BaseValidatorModel):
    PoolARNs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTapesInputPaginate(BaseValidatorModel):
    TapeARNs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVolumesInputPaginate(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_tape_archives' function.
class DescribeTapeArchivesOutput(BaseValidatorModel):
    TapeArchives: List[TapeArchive]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tape_recovery_points' function.
class DescribeTapeRecoveryPointsOutput(BaseValidatorModel):
    GatewayARN: str
    TapeRecoveryPointInfos: List[TapeRecoveryPointInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tapes' function.
class DescribeTapesOutput(BaseValidatorModel):
    Tapes: List[Tape]
    Marker: str
    ResponseMetadata: ResponseMetadata


class VTLDevice(BaseValidatorModel):
    VTLDeviceARN: Optional[str] = None
    VTLDeviceType: Optional[str] = None
    VTLDeviceVendor: Optional[str] = None
    VTLDeviceProductIdentifier: Optional[str] = None
    DeviceiSCSIAttributes: Optional[DeviceiSCSIAttributes] = None


# This class is the output for the 'list_local_disks' function.
class ListLocalDisksOutput(BaseValidatorModel):
    GatewayARN: str
    Disks: List[Disk]
    ResponseMetadata: ResponseMetadata

EndpointNetworkConfigurationUnion = Union[EndpointNetworkConfiguration, EndpointNetworkConfigurationOutput]


# This class is the output for the 'list_file_shares' function.
class ListFileSharesOutput(BaseValidatorModel):
    Marker: str
    NextMarker: str
    FileShareInfoList: List[FileShareInfo]
    ResponseMetadata: ResponseMetadata


class FileSystemAssociationInfo(BaseValidatorModel):
    FileSystemAssociationARN: Optional[str] = None
    LocationARN: Optional[str] = None
    FileSystemAssociationStatus: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    GatewayARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CacheAttributes: Optional[CacheAttributes] = None
    EndpointNetworkConfiguration: Optional[EndpointNetworkConfigurationOutput] = None
    FileSystemAssociationStatusDetails: Optional[List[FileSystemAssociationStatusDetail]] = None


# This class is the output for the 'list_file_system_associations' function.
class ListFileSystemAssociationsOutput(BaseValidatorModel):
    Marker: str
    NextMarker: str
    FileSystemAssociationSummaryList: List[FileSystemAssociationSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_gateways' function.
class ListGatewaysOutput(BaseValidatorModel):
    Gateways: List[GatewayInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tape_pools' function.
class ListTapePoolsOutput(BaseValidatorModel):
    PoolInfos: List[PoolInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tapes' function.
class ListTapesOutput(BaseValidatorModel):
    TapeInfos: List[TapeInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_volume_recovery_points' function.
class ListVolumeRecoveryPointsOutput(BaseValidatorModel):
    GatewayARN: str
    VolumeRecoveryPointInfos: List[VolumeRecoveryPointInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_volumes' function.
class ListVolumesOutput(BaseValidatorModel):
    GatewayARN: str
    Marker: str
    VolumeInfos: List[VolumeInfo]
    ResponseMetadata: ResponseMetadata

SMBLocalGroupsUnion = Union[SMBLocalGroups, SMBLocalGroupsOutput]


# This class is the output for the 'describe_smb_file_shares' function.
class DescribeSMBFileSharesOutput(BaseValidatorModel):
    SMBFileShareInfoList: List[SMBFileShareInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_automatic_tape_creation_policies' function.
class ListAutomaticTapeCreationPoliciesOutput(BaseValidatorModel):
    AutomaticTapeCreationPolicyInfos: List[AutomaticTapeCreationPolicyInfo]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_bandwidth_rate_limit_schedule' function.
class UpdateBandwidthRateLimitScheduleInput(BaseValidatorModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalUnion]


# This class is the output for the 'describe_cache_report' function.
class DescribeCacheReportOutput(BaseValidatorModel):
    CacheReportInfo: CacheReportInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_cache_reports' function.
class ListCacheReportsOutput(BaseValidatorModel):
    CacheReportList: List[CacheReportInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_cache_report' function.
class StartCacheReportInput(BaseValidatorModel):
    FileShareARN: str
    Role: str
    LocationARN: str
    BucketRegion: str
    ClientToken: str
    VPCEndpointDNSName: Optional[str] = None
    InclusionFilters: Optional[List[CacheReportFilterUnion]] = None
    ExclusionFilters: Optional[List[CacheReportFilterUnion]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_cached_iscsi_volumes' function.
class DescribeCachediSCSIVolumesOutput(BaseValidatorModel):
    CachediSCSIVolumes: List[CachediSCSIVolume]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stored_iscsi_volumes' function.
class DescribeStorediSCSIVolumesOutput(BaseValidatorModel):
    StorediSCSIVolumes: List[StorediSCSIVolume]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_nfs_file_shares' function.
class DescribeNFSFileSharesOutput(BaseValidatorModel):
    NFSFileShareInfoList: List[NFSFileShareInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vtl_devices' function.
class DescribeVTLDevicesOutput(BaseValidatorModel):
    GatewayARN: str
    VTLDevices: List[VTLDevice]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_file_system' function.
class AssociateFileSystemInput(BaseValidatorModel):
    UserName: str
    Password: str
    ClientToken: str
    GatewayARN: str
    LocationARN: str
    Tags: Optional[List[Tag]] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None
    EndpointNetworkConfiguration: Optional[EndpointNetworkConfigurationUnion] = None


# This class is the output for the 'describe_file_system_associations' function.
class DescribeFileSystemAssociationsOutput(BaseValidatorModel):
    FileSystemAssociationInfoList: List[FileSystemAssociationInfo]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_smb_local_groups' function.
class UpdateSMBLocalGroupsInput(BaseValidatorModel):
    GatewayARN: str
    SMBLocalGroups: SMBLocalGroupsUnion