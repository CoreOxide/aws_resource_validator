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


class AddCacheInput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]


class AddUploadBufferInput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]


class AddWorkingStorageInput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]


class AssignTapePoolInput(BaseValidatorModel):
    TapeARN: str
    PoolId: str
    BypassGovernanceRetention: Optional[bool] = None


class CacheAttributes(BaseValidatorModel):
    CacheStaleTimeoutInSeconds: Optional[int] = None


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


class CancelArchivalInput(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str


class CancelCacheReportInput(BaseValidatorModel):
    CacheReportARN: str


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


class DeleteAutomaticTapeCreationPolicyInput(BaseValidatorModel):
    GatewayARN: str


class DeleteBandwidthRateLimitInput(BaseValidatorModel):
    GatewayARN: str
    BandwidthType: str


class DeleteCacheReportInput(BaseValidatorModel):
    CacheReportARN: str


class DeleteChapCredentialsInput(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str


class DeleteFileShareInput(BaseValidatorModel):
    FileShareARN: str
    ForceDelete: Optional[bool] = None


class DeleteGatewayInput(BaseValidatorModel):
    GatewayARN: str


class DeleteSnapshotScheduleInput(BaseValidatorModel):
    VolumeARN: str


class DeleteTapeArchiveInput(BaseValidatorModel):
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None


class DeleteTapeInput(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None


class DeleteTapePoolInput(BaseValidatorModel):
    PoolARN: str


class DeleteVolumeInput(BaseValidatorModel):
    VolumeARN: str


class DescribeAvailabilityMonitorTestInput(BaseValidatorModel):
    GatewayARN: str


class DescribeBandwidthRateLimitInput(BaseValidatorModel):
    GatewayARN: str


class DescribeBandwidthRateLimitScheduleInput(BaseValidatorModel):
    GatewayARN: str


class DescribeCacheInput(BaseValidatorModel):
    GatewayARN: str


class DescribeCacheReportInput(BaseValidatorModel):
    CacheReportARN: str


class DescribeCachediSCSIVolumesInput(BaseValidatorModel):
    VolumeARNs: List[str]


class DescribeChapCredentialsInput(BaseValidatorModel):
    TargetARN: str


class DescribeFileSystemAssociationsInput(BaseValidatorModel):
    FileSystemAssociationARNList: List[str]


class DescribeGatewayInformationInput(BaseValidatorModel):
    GatewayARN: str


class NetworkInterface(BaseValidatorModel):
    Ipv4Address: Optional[str] = None
    MacAddress: Optional[str] = None
    Ipv6Address: Optional[str] = None


class DescribeMaintenanceStartTimeInput(BaseValidatorModel):
    GatewayARN: str


class SoftwareUpdatePreferences(BaseValidatorModel):
    AutomaticUpdatePolicy: Optional[AutomaticUpdatePolicyType] = None


class DescribeNFSFileSharesInput(BaseValidatorModel):
    FileShareARNList: List[str]


class DescribeSMBFileSharesInput(BaseValidatorModel):
    FileShareARNList: List[str]


class DescribeSMBSettingsInput(BaseValidatorModel):
    GatewayARN: str


class SMBLocalGroupsOutput(BaseValidatorModel):
    GatewayAdmins: Optional[List[str]] = None


class DescribeSnapshotScheduleInput(BaseValidatorModel):
    VolumeARN: str


class DescribeStorediSCSIVolumesInput(BaseValidatorModel):
    VolumeARNs: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


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


class DescribeTapeRecoveryPointsInput(BaseValidatorModel):
    GatewayARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeRecoveryPointInfo(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeRecoveryPointTime: Optional[datetime] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None


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


class DescribeUploadBufferInput(BaseValidatorModel):
    GatewayARN: str


class DescribeVTLDevicesInput(BaseValidatorModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[List[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class DescribeWorkingStorageInput(BaseValidatorModel):
    GatewayARN: str


class DetachVolumeInput(BaseValidatorModel):
    VolumeARN: str
    ForceDetach: Optional[bool] = None


class DeviceiSCSIAttributes(BaseValidatorModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    ChapEnabled: Optional[bool] = None


class DisableGatewayInput(BaseValidatorModel):
    GatewayARN: str


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


class JoinDomainInput(BaseValidatorModel):
    GatewayARN: str
    DomainName: str
    UserName: str
    Password: str
    OrganizationalUnit: Optional[str] = None
    DomainControllers: Optional[List[str]] = None
    TimeoutInSeconds: Optional[int] = None


class ListAutomaticTapeCreationPoliciesInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None


class ListCacheReportsInput(BaseValidatorModel):
    Marker: Optional[str] = None


class ListFileSharesInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListFileSystemAssociationsInput(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListGatewaysInput(BaseValidatorModel):
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class ListLocalDisksInput(BaseValidatorModel):
    GatewayARN: str


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


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


class ListVolumeInitiatorsInput(BaseValidatorModel):
    VolumeARN: str


class ListVolumeRecoveryPointsInput(BaseValidatorModel):
    GatewayARN: str


class VolumeRecoveryPointInfo(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeUsageInBytes: Optional[int] = None
    VolumeRecoveryPointTime: Optional[str] = None


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


class NotifyWhenUploadedInput(BaseValidatorModel):
    FileShareARN: str


class RefreshCacheInput(BaseValidatorModel):
    FileShareARN: str
    FolderList: Optional[List[str]] = None
    Recursive: Optional[bool] = None


class RemoveTagsFromResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class ResetCacheInput(BaseValidatorModel):
    GatewayARN: str


class RetrieveTapeArchiveInput(BaseValidatorModel):
    TapeARN: str
    GatewayARN: str


class RetrieveTapeRecoveryPointInput(BaseValidatorModel):
    TapeARN: str
    GatewayARN: str


class SMBLocalGroups(BaseValidatorModel):
    GatewayAdmins: Optional[List[str]] = None


class SetLocalConsolePasswordInput(BaseValidatorModel):
    GatewayARN: str
    LocalConsolePassword: str


class SetSMBGuestPasswordInput(BaseValidatorModel):
    GatewayARN: str
    Password: str


class ShutdownGatewayInput(BaseValidatorModel):
    GatewayARN: str


class StartAvailabilityMonitorTestInput(BaseValidatorModel):
    GatewayARN: str


class StartGatewayInput(BaseValidatorModel):
    GatewayARN: str


class UpdateBandwidthRateLimitInput(BaseValidatorModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


class UpdateChapCredentialsInput(BaseValidatorModel):
    TargetARN: str
    SecretToAuthenticateInitiator: str
    InitiatorName: str
    SecretToAuthenticateTarget: Optional[str] = None


class UpdateGatewayInformationInput(BaseValidatorModel):
    GatewayARN: str
    GatewayName: Optional[str] = None
    GatewayTimezone: Optional[str] = None
    CloudWatchLogGroupARN: Optional[str] = None
    GatewayCapacity: Optional[GatewayCapacityType] = None


class UpdateGatewaySoftwareNowInput(BaseValidatorModel):
    GatewayARN: str


class UpdateSMBFileShareVisibilityInput(BaseValidatorModel):
    GatewayARN: str
    FileSharesVisible: bool


class UpdateSMBSecurityStrategyInput(BaseValidatorModel):
    GatewayARN: str
    SMBSecurityStrategy: SMBSecurityStrategyType


class UpdateVTLDeviceTypeInput(BaseValidatorModel):
    VTLDeviceARN: str
    DeviceType: str


class ActivateGatewayInput(BaseValidatorModel):
    ActivationKey: str
    GatewayName: str
    GatewayTimezone: str
    GatewayRegion: str
    GatewayType: Optional[str] = None
    TapeDriveType: Optional[str] = None
    MediumChangerType: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class AddTagsToResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


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


class CreateSnapshotFromVolumeRecoveryPointInput(BaseValidatorModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[List[Tag]] = None


class CreateSnapshotInput(BaseValidatorModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[List[Tag]] = None


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


class CreateTapePoolInput(BaseValidatorModel):
    PoolName: str
    StorageClass: TapeStorageClassType
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class CreateTapeWithBarcodeInput(BaseValidatorModel):
    GatewayARN: str
    TapeSizeInBytes: int
    TapeBarcode: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


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


class UpdateSnapshotScheduleInput(BaseValidatorModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ActivateGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class AddCacheOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class AddTagsToResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


class AddUploadBufferOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class AddWorkingStorageOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class AssignTapePoolOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class AssociateFileSystemOutput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadata


class AttachVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadata


class CancelArchivalOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class CancelCacheReportOutput(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadata


class CancelRetrievalOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class CreateCachediSCSIVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadata


class CreateNFSFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


class CreateSMBFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


class CreateSnapshotFromVolumeRecoveryPointOutput(BaseValidatorModel):
    SnapshotId: str
    VolumeARN: str
    VolumeRecoveryPointTime: str
    ResponseMetadata: ResponseMetadata


class CreateSnapshotOutput(BaseValidatorModel):
    VolumeARN: str
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


class CreateStorediSCSIVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    VolumeSizeInBytes: int
    TargetARN: str
    ResponseMetadata: ResponseMetadata


class CreateTapePoolOutput(BaseValidatorModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadata


class CreateTapeWithBarcodeOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class CreateTapesOutput(BaseValidatorModel):
    TapeARNs: List[str]
    ResponseMetadata: ResponseMetadata


class DeleteAutomaticTapeCreationPolicyOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class DeleteBandwidthRateLimitOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class DeleteCacheReportOutput(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadata


class DeleteChapCredentialsOutput(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadata


class DeleteFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


class DeleteGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotScheduleOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


class DeleteTapeArchiveOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class DeleteTapeOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class DeleteTapePoolOutput(BaseValidatorModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadata


class DeleteVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


class DescribeAvailabilityMonitorTestOutput(BaseValidatorModel):
    GatewayARN: str
    Status: AvailabilityMonitorTestStatusType
    StartTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeBandwidthRateLimitOutput(BaseValidatorModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int
    ResponseMetadata: ResponseMetadata


class DescribeCacheOutput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    CacheAllocatedInBytes: int
    CacheUsedPercentage: float
    CacheDirtyPercentage: float
    CacheHitPercentage: float
    CacheMissPercentage: float
    ResponseMetadata: ResponseMetadata


class DescribeSnapshotScheduleOutput(BaseValidatorModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: str
    Timezone: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class DescribeUploadBufferOutput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    UploadBufferUsedInBytes: int
    UploadBufferAllocatedInBytes: int
    ResponseMetadata: ResponseMetadata


class DescribeWorkingStorageOutput(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    WorkingStorageUsedInBytes: int
    WorkingStorageAllocatedInBytes: int
    ResponseMetadata: ResponseMetadata


class DetachVolumeOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


class DisableGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class DisassociateFileSystemOutput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadata


class EvictFilesFailingUploadOutput(BaseValidatorModel):
    NotificationId: str
    ResponseMetadata: ResponseMetadata


class JoinDomainOutput(BaseValidatorModel):
    GatewayARN: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    ResourceARN: str
    Marker: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ListVolumeInitiatorsOutput(BaseValidatorModel):
    Initiators: List[str]
    ResponseMetadata: ResponseMetadata


class NotifyWhenUploadedOutput(BaseValidatorModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadata


class RefreshCacheOutput(BaseValidatorModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadata


class RemoveTagsFromResourceOutput(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadata


class ResetCacheOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class RetrieveTapeArchiveOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class RetrieveTapeRecoveryPointOutput(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadata


class SetLocalConsolePasswordOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class SetSMBGuestPasswordOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class ShutdownGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class StartAvailabilityMonitorTestOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class StartCacheReportOutput(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadata


class StartGatewayOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateAutomaticTapeCreationPolicyOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateBandwidthRateLimitOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateBandwidthRateLimitScheduleOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateChapCredentialsOutput(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadata


class UpdateFileSystemAssociationOutput(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadata


class UpdateGatewayInformationOutput(BaseValidatorModel):
    GatewayARN: str
    GatewayName: str
    ResponseMetadata: ResponseMetadata


class UpdateGatewaySoftwareNowOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateMaintenanceStartTimeOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateNFSFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


class UpdateSMBFileShareOutput(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadata


class UpdateSMBFileShareVisibilityOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateSMBLocalGroupsOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateSMBSecurityStrategyOutput(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadata


class UpdateSnapshotScheduleOutput(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadata


class UpdateVTLDeviceTypeOutput(BaseValidatorModel):
    VTLDeviceARN: str
    ResponseMetadata: ResponseMetadata


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


class UpdateFileSystemAssociationInput(BaseValidatorModel):
    FileSystemAssociationARN: str
    UserName: Optional[str] = None
    Password: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributes] = None


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


class UpdateAutomaticTapeCreationPolicyInput(BaseValidatorModel):
    AutomaticTapeCreationRules: List[AutomaticTapeCreationRule]
    GatewayARN: str


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


class DescribeChapCredentialsOutput(BaseValidatorModel):
    ChapCredentials: List[ChapInfo]
    ResponseMetadata: ResponseMetadata


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


class DescribeMaintenanceStartTimeOutput(BaseValidatorModel):
    GatewayARN: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfWeek: int
    DayOfMonth: int
    Timezone: str
    SoftwareUpdatePreferences: SoftwareUpdatePreferences
    ResponseMetadata: ResponseMetadata


class UpdateMaintenanceStartTimeInput(BaseValidatorModel):
    GatewayARN: str
    HourOfDay: Optional[int] = None
    MinuteOfHour: Optional[int] = None
    DayOfWeek: Optional[int] = None
    DayOfMonth: Optional[int] = None
    SoftwareUpdatePreferences: Optional[SoftwareUpdatePreferences] = None


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


class DescribeTapeArchivesOutput(BaseValidatorModel):
    TapeArchives: List[TapeArchive]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeTapeRecoveryPointsOutput(BaseValidatorModel):
    GatewayARN: str
    TapeRecoveryPointInfos: List[TapeRecoveryPointInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


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


class ListLocalDisksOutput(BaseValidatorModel):
    GatewayARN: str
    Disks: List[Disk]
    ResponseMetadata: ResponseMetadata

EndpointNetworkConfigurationUnion = Union[EndpointNetworkConfiguration, EndpointNetworkConfigurationOutput]


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


class ListFileSystemAssociationsOutput(BaseValidatorModel):
    Marker: str
    NextMarker: str
    FileSystemAssociationSummaryList: List[FileSystemAssociationSummary]
    ResponseMetadata: ResponseMetadata


class ListGatewaysOutput(BaseValidatorModel):
    Gateways: List[GatewayInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListTapePoolsOutput(BaseValidatorModel):
    PoolInfos: List[PoolInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListTapesOutput(BaseValidatorModel):
    TapeInfos: List[TapeInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListVolumeRecoveryPointsOutput(BaseValidatorModel):
    GatewayARN: str
    VolumeRecoveryPointInfos: List[VolumeRecoveryPointInfo]
    ResponseMetadata: ResponseMetadata


class ListVolumesOutput(BaseValidatorModel):
    GatewayARN: str
    Marker: str
    VolumeInfos: List[VolumeInfo]
    ResponseMetadata: ResponseMetadata

SMBLocalGroupsUnion = Union[SMBLocalGroups, SMBLocalGroupsOutput]


class DescribeSMBFileSharesOutput(BaseValidatorModel):
    SMBFileShareInfoList: List[SMBFileShareInfo]
    ResponseMetadata: ResponseMetadata


class ListAutomaticTapeCreationPoliciesOutput(BaseValidatorModel):
    AutomaticTapeCreationPolicyInfos: List[AutomaticTapeCreationPolicyInfo]
    ResponseMetadata: ResponseMetadata


class UpdateBandwidthRateLimitScheduleInput(BaseValidatorModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalUnion]


class DescribeCacheReportOutput(BaseValidatorModel):
    CacheReportInfo: CacheReportInfo
    ResponseMetadata: ResponseMetadata


class ListCacheReportsOutput(BaseValidatorModel):
    CacheReportList: List[CacheReportInfo]
    Marker: str
    ResponseMetadata: ResponseMetadata


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


class DescribeCachediSCSIVolumesOutput(BaseValidatorModel):
    CachediSCSIVolumes: List[CachediSCSIVolume]
    ResponseMetadata: ResponseMetadata


class DescribeStorediSCSIVolumesOutput(BaseValidatorModel):
    StorediSCSIVolumes: List[StorediSCSIVolume]
    ResponseMetadata: ResponseMetadata


class DescribeNFSFileSharesOutput(BaseValidatorModel):
    NFSFileShareInfoList: List[NFSFileShareInfo]
    ResponseMetadata: ResponseMetadata


class DescribeVTLDevicesOutput(BaseValidatorModel):
    GatewayARN: str
    VTLDevices: List[VTLDevice]
    Marker: str
    ResponseMetadata: ResponseMetadata


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


class DescribeFileSystemAssociationsOutput(BaseValidatorModel):
    FileSystemAssociationInfoList: List[FileSystemAssociationInfo]
    ResponseMetadata: ResponseMetadata


class UpdateSMBLocalGroupsInput(BaseValidatorModel):
    GatewayARN: str
    SMBLocalGroups: SMBLocalGroupsUnion