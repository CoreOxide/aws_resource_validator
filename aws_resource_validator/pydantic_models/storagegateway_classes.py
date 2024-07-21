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
from aws_resource_validator.pydantic_models.storagegateway_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddCacheInputRequestTypeDef(BaseModel):
    GatewayARN: str
    DiskIds: Sequence[str]

class AddUploadBufferInputRequestTypeDef(BaseModel):
    GatewayARN: str
    DiskIds: Sequence[str]

class AddWorkingStorageInputRequestTypeDef(BaseModel):
    GatewayARN: str
    DiskIds: Sequence[str]

class AssignTapePoolInputRequestTypeDef(BaseModel):
    TapeARN: str
    PoolId: str
    BypassGovernanceRetention: Optional[bool] = None

class CacheAttributesTypeDef(BaseModel):
    CacheStaleTimeoutInSeconds: Optional[int] = None

class EndpointNetworkConfigurationTypeDef(BaseModel):
    IpAddresses: Optional[Sequence[str]] = None

class AttachVolumeInputRequestTypeDef(BaseModel):
    GatewayARN: str
    VolumeARN: str
    NetworkInterfaceId: str
    TargetName: Optional[str] = None
    DiskId: Optional[str] = None

class AutomaticTapeCreationRuleTypeDef(BaseModel):
    TapeBarcodePrefix: str
    PoolId: str
    TapeSizeInBytes: int
    MinimumNumTapes: int
    Worm: Optional[bool] = None

class BandwidthRateLimitIntervalOutputTypeDef(BaseModel):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: List[int]
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None

class BandwidthRateLimitIntervalTypeDef(BaseModel):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: Sequence[int]
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None

class VolumeiSCSIAttributesTypeDef(BaseModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    LunNumber: Optional[int] = None
    ChapEnabled: Optional[bool] = None

class CancelArchivalInputRequestTypeDef(BaseModel):
    GatewayARN: str
    TapeARN: str

class CancelRetrievalInputRequestTypeDef(BaseModel):
    GatewayARN: str
    TapeARN: str

class ChapInfoTypeDef(BaseModel):
    TargetARN: Optional[str] = None
    SecretToAuthenticateInitiator: Optional[str] = None
    InitiatorName: Optional[str] = None
    SecretToAuthenticateTarget: Optional[str] = None

class NFSFileShareDefaultsTypeDef(BaseModel):
    FileMode: Optional[str] = None
    DirectoryMode: Optional[str] = None
    GroupId: Optional[int] = None
    OwnerId: Optional[int] = None

class DeleteAutomaticTapeCreationPolicyInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DeleteBandwidthRateLimitInputRequestTypeDef(BaseModel):
    GatewayARN: str
    BandwidthType: str

class DeleteChapCredentialsInputRequestTypeDef(BaseModel):
    TargetARN: str
    InitiatorName: str

class DeleteFileShareInputRequestTypeDef(BaseModel):
    FileShareARN: str
    ForceDelete: Optional[bool] = None

class DeleteGatewayInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DeleteSnapshotScheduleInputRequestTypeDef(BaseModel):
    VolumeARN: str

class DeleteTapeArchiveInputRequestTypeDef(BaseModel):
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None

class DeleteTapeInputRequestTypeDef(BaseModel):
    GatewayARN: str
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None

class DeleteTapePoolInputRequestTypeDef(BaseModel):
    PoolARN: str

class DeleteVolumeInputRequestTypeDef(BaseModel):
    VolumeARN: str

class DescribeAvailabilityMonitorTestInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DescribeBandwidthRateLimitInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DescribeBandwidthRateLimitScheduleInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DescribeCacheInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DescribeCachediSCSIVolumesInputRequestTypeDef(BaseModel):
    VolumeARNs: Sequence[str]

class DescribeChapCredentialsInputRequestTypeDef(BaseModel):
    TargetARN: str

class DescribeFileSystemAssociationsInputRequestTypeDef(BaseModel):
    FileSystemAssociationARNList: Sequence[str]

class DescribeGatewayInformationInputRequestTypeDef(BaseModel):
    GatewayARN: str

class NetworkInterfaceTypeDef(BaseModel):
    Ipv4Address: Optional[str] = None
    MacAddress: Optional[str] = None
    Ipv6Address: Optional[str] = None

class DescribeMaintenanceStartTimeInputRequestTypeDef(BaseModel):
    GatewayARN: str

class SoftwareUpdatePreferencesTypeDef(BaseModel):
    AutomaticUpdatePolicy: Optional[AutomaticUpdatePolicyType] = None

class DescribeNFSFileSharesInputRequestTypeDef(BaseModel):
    FileShareARNList: Sequence[str]

class DescribeSMBFileSharesInputRequestTypeDef(BaseModel):
    FileShareARNList: Sequence[str]

class DescribeSMBSettingsInputRequestTypeDef(BaseModel):
    GatewayARN: str

class SMBLocalGroupsOutputTypeDef(BaseModel):
    GatewayAdmins: Optional[List[str]] = None

class DescribeSnapshotScheduleInputRequestTypeDef(BaseModel):
    VolumeARN: str

class DescribeStorediSCSIVolumesInputRequestTypeDef(BaseModel):
    VolumeARNs: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeTapeArchivesInputRequestTypeDef(BaseModel):
    TapeARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class TapeArchiveTypeDef(BaseModel):
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

class DescribeTapeRecoveryPointsInputRequestTypeDef(BaseModel):
    GatewayARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class TapeRecoveryPointInfoTypeDef(BaseModel):
    TapeARN: Optional[str] = None
    TapeRecoveryPointTime: Optional[datetime] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None

class DescribeTapesInputRequestTypeDef(BaseModel):
    GatewayARN: str
    TapeARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class TapeTypeDef(BaseModel):
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

class DescribeUploadBufferInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DescribeVTLDevicesInputRequestTypeDef(BaseModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class DescribeWorkingStorageInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DetachVolumeInputRequestTypeDef(BaseModel):
    VolumeARN: str
    ForceDetach: Optional[bool] = None

class DeviceiSCSIAttributesTypeDef(BaseModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    ChapEnabled: Optional[bool] = None

class DisableGatewayInputRequestTypeDef(BaseModel):
    GatewayARN: str

class DisassociateFileSystemInputRequestTypeDef(BaseModel):
    FileSystemAssociationARN: str
    ForceDelete: Optional[bool] = None

class DiskTypeDef(BaseModel):
    DiskId: Optional[str] = None
    DiskPath: Optional[str] = None
    DiskNode: Optional[str] = None
    DiskStatus: Optional[str] = None
    DiskSizeInBytes: Optional[int] = None
    DiskAllocationType: Optional[str] = None
    DiskAllocationResource: Optional[str] = None
    DiskAttributeList: Optional[List[str]] = None

class EndpointNetworkConfigurationOutputTypeDef(BaseModel):
    IpAddresses: Optional[List[str]] = None

class FileShareInfoTypeDef(BaseModel):
    FileShareType: Optional[FileShareTypeType] = None
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None

class FileSystemAssociationStatusDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None

class FileSystemAssociationSummaryTypeDef(BaseModel):
    FileSystemAssociationId: Optional[str] = None
    FileSystemAssociationARN: Optional[str] = None
    FileSystemAssociationStatus: Optional[str] = None
    GatewayARN: Optional[str] = None

class GatewayInfoTypeDef(BaseModel):
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

class JoinDomainInputRequestTypeDef(BaseModel):
    GatewayARN: str
    DomainName: str
    UserName: str
    Password: str
    OrganizationalUnit: Optional[str] = None
    DomainControllers: Optional[Sequence[str]] = None
    TimeoutInSeconds: Optional[int] = None

class ListAutomaticTapeCreationPoliciesInputRequestTypeDef(BaseModel):
    GatewayARN: Optional[str] = None

class ListFileSharesInputRequestTypeDef(BaseModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListFileSystemAssociationsInputRequestTypeDef(BaseModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListGatewaysInputRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class ListLocalDisksInputRequestTypeDef(BaseModel):
    GatewayARN: str

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class ListTapePoolsInputRequestTypeDef(BaseModel):
    PoolARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class PoolInfoTypeDef(BaseModel):
    PoolARN: Optional[str] = None
    PoolName: Optional[str] = None
    StorageClass: Optional[TapeStorageClassType] = None
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    PoolStatus: Optional[PoolStatusType] = None

class ListTapesInputRequestTypeDef(BaseModel):
    TapeARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class TapeInfoTypeDef(BaseModel):
    TapeARN: Optional[str] = None
    TapeBarcode: Optional[str] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
    PoolId: Optional[str] = None
    RetentionStartDate: Optional[datetime] = None
    PoolEntryDate: Optional[datetime] = None

class ListVolumeInitiatorsInputRequestTypeDef(BaseModel):
    VolumeARN: str

class ListVolumeRecoveryPointsInputRequestTypeDef(BaseModel):
    GatewayARN: str

class VolumeRecoveryPointInfoTypeDef(BaseModel):
    VolumeARN: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeUsageInBytes: Optional[int] = None
    VolumeRecoveryPointTime: Optional[str] = None

class ListVolumesInputRequestTypeDef(BaseModel):
    GatewayARN: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None

class VolumeInfoTypeDef(BaseModel):
    VolumeARN: Optional[str] = None
    VolumeId: Optional[str] = None
    GatewayARN: Optional[str] = None
    GatewayId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeAttachmentStatus: Optional[str] = None

class NotifyWhenUploadedInputRequestTypeDef(BaseModel):
    FileShareARN: str

class RefreshCacheInputRequestTypeDef(BaseModel):
    FileShareARN: str
    FolderList: Optional[Sequence[str]] = None
    Recursive: Optional[bool] = None

class RemoveTagsFromResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ResetCacheInputRequestTypeDef(BaseModel):
    GatewayARN: str

class RetrieveTapeArchiveInputRequestTypeDef(BaseModel):
    TapeARN: str
    GatewayARN: str

class RetrieveTapeRecoveryPointInputRequestTypeDef(BaseModel):
    TapeARN: str
    GatewayARN: str

class SMBLocalGroupsTypeDef(BaseModel):
    GatewayAdmins: Optional[Sequence[str]] = None

class SetLocalConsolePasswordInputRequestTypeDef(BaseModel):
    GatewayARN: str
    LocalConsolePassword: str

class SetSMBGuestPasswordInputRequestTypeDef(BaseModel):
    GatewayARN: str
    Password: str

class ShutdownGatewayInputRequestTypeDef(BaseModel):
    GatewayARN: str

class StartAvailabilityMonitorTestInputRequestTypeDef(BaseModel):
    GatewayARN: str

class StartGatewayInputRequestTypeDef(BaseModel):
    GatewayARN: str

class UpdateBandwidthRateLimitInputRequestTypeDef(BaseModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None

class UpdateChapCredentialsInputRequestTypeDef(BaseModel):
    TargetARN: str
    SecretToAuthenticateInitiator: str
    InitiatorName: str
    SecretToAuthenticateTarget: Optional[str] = None

class UpdateGatewayInformationInputRequestTypeDef(BaseModel):
    GatewayARN: str
    GatewayName: Optional[str] = None
    GatewayTimezone: Optional[str] = None
    CloudWatchLogGroupARN: Optional[str] = None
    GatewayCapacity: Optional[GatewayCapacityType] = None

class UpdateGatewaySoftwareNowInputRequestTypeDef(BaseModel):
    GatewayARN: str

class UpdateSMBFileShareVisibilityInputRequestTypeDef(BaseModel):
    GatewayARN: str
    FileSharesVisible: bool

class UpdateSMBSecurityStrategyInputRequestTypeDef(BaseModel):
    GatewayARN: str
    SMBSecurityStrategy: SMBSecurityStrategyType

class UpdateVTLDeviceTypeInputRequestTypeDef(BaseModel):
    VTLDeviceARN: str
    DeviceType: str

class ActivateGatewayInputRequestTypeDef(BaseModel):
    ActivationKey: str
    GatewayName: str
    GatewayTimezone: str
    GatewayRegion: str
    GatewayType: Optional[str] = None
    TapeDriveType: Optional[str] = None
    MediumChangerType: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class AddTagsToResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateCachediSCSIVolumeInputRequestTypeDef(BaseModel):
    GatewayARN: str
    VolumeSizeInBytes: int
    TargetName: str
    NetworkInterfaceId: str
    ClientToken: str
    SnapshotId: Optional[str] = None
    SourceVolumeARN: Optional[str] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef(BaseModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotInputRequestTypeDef(BaseModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateStorediSCSIVolumeInputRequestTypeDef(BaseModel):
    GatewayARN: str
    DiskId: str
    PreserveExistingData: bool
    TargetName: str
    NetworkInterfaceId: str
    SnapshotId: Optional[str] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTapePoolInputRequestTypeDef(BaseModel):
    PoolName: str
    StorageClass: TapeStorageClassType
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTapeWithBarcodeInputRequestTypeDef(BaseModel):
    GatewayARN: str
    TapeSizeInBytes: int
    TapeBarcode: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTapesInputRequestTypeDef(BaseModel):
    GatewayARN: str
    TapeSizeInBytes: int
    ClientToken: str
    NumTapesToCreate: int
    TapeBarcodePrefix: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateSnapshotScheduleInputRequestTypeDef(BaseModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ActivateGatewayOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddCacheOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceOutputTypeDef(BaseModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddUploadBufferOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddWorkingStorageOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssignTapePoolOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateFileSystemOutputTypeDef(BaseModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachVolumeOutputTypeDef(BaseModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelArchivalOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelRetrievalOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCachediSCSIVolumeOutputTypeDef(BaseModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNFSFileShareOutputTypeDef(BaseModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSMBFileShareOutputTypeDef(BaseModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotFromVolumeRecoveryPointOutputTypeDef(BaseModel):
    SnapshotId: str
    VolumeARN: str
    VolumeRecoveryPointTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotOutputTypeDef(BaseModel):
    VolumeARN: str
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorediSCSIVolumeOutputTypeDef(BaseModel):
    VolumeARN: str
    VolumeSizeInBytes: int
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTapePoolOutputTypeDef(BaseModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTapeWithBarcodeOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTapesOutputTypeDef(BaseModel):
    TapeARNs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAutomaticTapeCreationPolicyOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBandwidthRateLimitOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteChapCredentialsOutputTypeDef(BaseModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFileShareOutputTypeDef(BaseModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotScheduleOutputTypeDef(BaseModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTapeArchiveOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTapeOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTapePoolOutputTypeDef(BaseModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVolumeOutputTypeDef(BaseModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAvailabilityMonitorTestOutputTypeDef(BaseModel):
    GatewayARN: str
    Status: AvailabilityMonitorTestStatusType
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBandwidthRateLimitOutputTypeDef(BaseModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCacheOutputTypeDef(BaseModel):
    GatewayARN: str
    DiskIds: List[str]
    CacheAllocatedInBytes: int
    CacheUsedPercentage: float
    CacheDirtyPercentage: float
    CacheHitPercentage: float
    CacheMissPercentage: float
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotScheduleOutputTypeDef(BaseModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: str
    Timezone: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUploadBufferOutputTypeDef(BaseModel):
    GatewayARN: str
    DiskIds: List[str]
    UploadBufferUsedInBytes: int
    UploadBufferAllocatedInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkingStorageOutputTypeDef(BaseModel):
    GatewayARN: str
    DiskIds: List[str]
    WorkingStorageUsedInBytes: int
    WorkingStorageAllocatedInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class DetachVolumeOutputTypeDef(BaseModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableGatewayOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFileSystemOutputTypeDef(BaseModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class JoinDomainOutputTypeDef(BaseModel):
    GatewayARN: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    ResourceARN: str
    Marker: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVolumeInitiatorsOutputTypeDef(BaseModel):
    Initiators: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyWhenUploadedOutputTypeDef(BaseModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshCacheOutputTypeDef(BaseModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveTagsFromResourceOutputTypeDef(BaseModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetCacheOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveTapeArchiveOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveTapeRecoveryPointOutputTypeDef(BaseModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetLocalConsolePasswordOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetSMBGuestPasswordOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ShutdownGatewayOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAvailabilityMonitorTestOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartGatewayOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAutomaticTapeCreationPolicyOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBandwidthRateLimitOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBandwidthRateLimitScheduleOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChapCredentialsOutputTypeDef(BaseModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFileSystemAssociationOutputTypeDef(BaseModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInformationOutputTypeDef(BaseModel):
    GatewayARN: str
    GatewayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewaySoftwareNowOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMaintenanceStartTimeOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNFSFileShareOutputTypeDef(BaseModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBFileShareOutputTypeDef(BaseModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBFileShareVisibilityOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBLocalGroupsOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBSecurityStrategyOutputTypeDef(BaseModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSnapshotScheduleOutputTypeDef(BaseModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVTLDeviceTypeOutputTypeDef(BaseModel):
    VTLDeviceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSMBFileShareInputRequestTypeDef(BaseModel):
    ClientToken: str
    GatewayARN: str
    Role: str
    LocationARN: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    SMBACLEnabled: Optional[bool] = None
    AccessBasedEnumeration: Optional[bool] = None
    AdminUserList: Optional[Sequence[str]] = None
    ValidUserList: Optional[Sequence[str]] = None
    InvalidUserList: Optional[Sequence[str]] = None
    AuditDestinationARN: Optional[str] = None
    Authentication: Optional[str] = None
    CaseSensitivity: Optional[CaseSensitivityType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    OplocksEnabled: Optional[bool] = None

class SMBFileShareInfoTypeDef(BaseModel):
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
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
    Tags: Optional[List[TagTypeDef]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    OplocksEnabled: Optional[bool] = None

class UpdateFileSystemAssociationInputRequestTypeDef(BaseModel):
    FileSystemAssociationARN: str
    UserName: Optional[str] = None
    Password: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None

class UpdateSMBFileShareInputRequestTypeDef(BaseModel):
    FileShareARN: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    SMBACLEnabled: Optional[bool] = None
    AccessBasedEnumeration: Optional[bool] = None
    AdminUserList: Optional[Sequence[str]] = None
    ValidUserList: Optional[Sequence[str]] = None
    InvalidUserList: Optional[Sequence[str]] = None
    AuditDestinationARN: Optional[str] = None
    CaseSensitivity: Optional[CaseSensitivityType] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    NotificationPolicy: Optional[str] = None
    OplocksEnabled: Optional[bool] = None

class AssociateFileSystemInputRequestTypeDef(BaseModel):
    UserName: str
    Password: str
    ClientToken: str
    GatewayARN: str
    LocationARN: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    EndpointNetworkConfiguration: Optional[EndpointNetworkConfigurationTypeDef] = None

class AutomaticTapeCreationPolicyInfoTypeDef(BaseModel):
    AutomaticTapeCreationRules: Optional[List[AutomaticTapeCreationRuleTypeDef]] = None
    GatewayARN: Optional[str] = None

class UpdateAutomaticTapeCreationPolicyInputRequestTypeDef(BaseModel):
    AutomaticTapeCreationRules: Sequence[AutomaticTapeCreationRuleTypeDef]
    GatewayARN: str

class DescribeBandwidthRateLimitScheduleOutputTypeDef(BaseModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CachediSCSIVolumeTypeDef(BaseModel):
    VolumeARN: Optional[str] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeStatus: Optional[str] = None
    VolumeAttachmentStatus: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeProgress: Optional[float] = None
    SourceSnapshotId: Optional[str] = None
    VolumeiSCSIAttributes: Optional[VolumeiSCSIAttributesTypeDef] = None
    CreatedDate: Optional[datetime] = None
    VolumeUsedInBytes: Optional[int] = None
    KMSKey: Optional[str] = None
    TargetName: Optional[str] = None

class StorediSCSIVolumeTypeDef(BaseModel):
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
    VolumeiSCSIAttributes: Optional[VolumeiSCSIAttributesTypeDef] = None
    CreatedDate: Optional[datetime] = None
    VolumeUsedInBytes: Optional[int] = None
    KMSKey: Optional[str] = None
    TargetName: Optional[str] = None

class DescribeChapCredentialsOutputTypeDef(BaseModel):
    ChapCredentials: List[ChapInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNFSFileShareInputRequestTypeDef(BaseModel):
    ClientToken: str
    GatewayARN: str
    Role: str
    LocationARN: str
    NFSFileShareDefaults: Optional[NFSFileShareDefaultsTypeDef] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ClientList: Optional[Sequence[str]] = None
    Squash: Optional[str] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    AuditDestinationARN: Optional[str] = None

class NFSFileShareInfoTypeDef(BaseModel):
    NFSFileShareDefaults: Optional[NFSFileShareDefaultsTypeDef] = None
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
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
    Tags: Optional[List[TagTypeDef]] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    NotificationPolicy: Optional[str] = None
    VPCEndpointDNSName: Optional[str] = None
    BucketRegion: Optional[str] = None
    AuditDestinationARN: Optional[str] = None

class UpdateNFSFileShareInputRequestTypeDef(BaseModel):
    FileShareARN: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    NFSFileShareDefaults: Optional[NFSFileShareDefaultsTypeDef] = None
    DefaultStorageClass: Optional[str] = None
    ObjectACL: Optional[ObjectACLType] = None
    ClientList: Optional[Sequence[str]] = None
    Squash: Optional[str] = None
    ReadOnly: Optional[bool] = None
    GuessMIMETypeEnabled: Optional[bool] = None
    RequesterPays: Optional[bool] = None
    FileShareName: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    NotificationPolicy: Optional[str] = None
    AuditDestinationARN: Optional[str] = None

class DescribeGatewayInformationOutputTypeDef(BaseModel):
    GatewayARN: str
    GatewayId: str
    GatewayName: str
    GatewayTimezone: str
    GatewayState: str
    GatewayNetworkInterfaces: List[NetworkInterfaceTypeDef]
    GatewayType: str
    NextUpdateAvailabilityDate: str
    LastSoftwareUpdate: str
    Ec2InstanceId: str
    Ec2InstanceRegion: str
    Tags: List[TagTypeDef]
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
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMaintenanceStartTimeOutputTypeDef(BaseModel):
    GatewayARN: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfWeek: int
    DayOfMonth: int
    Timezone: str
    SoftwareUpdatePreferences: SoftwareUpdatePreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMaintenanceStartTimeInputRequestTypeDef(BaseModel):
    GatewayARN: str
    HourOfDay: Optional[int] = None
    MinuteOfHour: Optional[int] = None
    DayOfWeek: Optional[int] = None
    DayOfMonth: Optional[int] = None
    SoftwareUpdatePreferences: Optional[SoftwareUpdatePreferencesTypeDef] = None

class DescribeSMBSettingsOutputTypeDef(BaseModel):
    GatewayARN: str
    DomainName: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    SMBGuestPasswordSet: bool
    SMBSecurityStrategy: SMBSecurityStrategyType
    FileSharesVisible: bool
    SMBLocalGroups: SMBLocalGroupsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTapeArchivesInputDescribeTapeArchivesPaginateTypeDef(BaseModel):
    TapeARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTapeRecoveryPointsInputDescribeTapeRecoveryPointsPaginateTypeDef(BaseModel):
    GatewayARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTapesInputDescribeTapesPaginateTypeDef(BaseModel):
    GatewayARN: str
    TapeARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVTLDevicesInputDescribeVTLDevicesPaginateTypeDef(BaseModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFileSharesInputListFileSharesPaginateTypeDef(BaseModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFileSystemAssociationsInputListFileSystemAssociationsPaginateTypeDef(BaseModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewaysInputListGatewaysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTapePoolsInputListTapePoolsPaginateTypeDef(BaseModel):
    PoolARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTapesInputListTapesPaginateTypeDef(BaseModel):
    TapeARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVolumesInputListVolumesPaginateTypeDef(BaseModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTapeArchivesOutputTypeDef(BaseModel):
    TapeArchives: List[TapeArchiveTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTapeRecoveryPointsOutputTypeDef(BaseModel):
    GatewayARN: str
    TapeRecoveryPointInfos: List[TapeRecoveryPointInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTapesOutputTypeDef(BaseModel):
    Tapes: List[TapeTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class VTLDeviceTypeDef(BaseModel):
    VTLDeviceARN: Optional[str] = None
    VTLDeviceType: Optional[str] = None
    VTLDeviceVendor: Optional[str] = None
    VTLDeviceProductIdentifier: Optional[str] = None
    DeviceiSCSIAttributes: Optional[DeviceiSCSIAttributesTypeDef] = None

class ListLocalDisksOutputTypeDef(BaseModel):
    GatewayARN: str
    Disks: List[DiskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFileSharesOutputTypeDef(BaseModel):
    Marker: str
    NextMarker: str
    FileShareInfoList: List[FileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemAssociationInfoTypeDef(BaseModel):
    FileSystemAssociationARN: Optional[str] = None
    LocationARN: Optional[str] = None
    FileSystemAssociationStatus: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    GatewayARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    EndpointNetworkConfiguration: Optional[EndpointNetworkConfigurationOutputTypeDef] = None
    FileSystemAssociationStatusDetails: Optional[       List[FileSystemAssociationStatusDetailTypeDef]     ] = None

class ListFileSystemAssociationsOutputTypeDef(BaseModel):
    Marker: str
    NextMarker: str
    FileSystemAssociationSummaryList: List[FileSystemAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGatewaysOutputTypeDef(BaseModel):
    Gateways: List[GatewayInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTapePoolsOutputTypeDef(BaseModel):
    PoolInfos: List[PoolInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTapesOutputTypeDef(BaseModel):
    TapeInfos: List[TapeInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVolumeRecoveryPointsOutputTypeDef(BaseModel):
    GatewayARN: str
    VolumeRecoveryPointInfos: List[VolumeRecoveryPointInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVolumesOutputTypeDef(BaseModel):
    GatewayARN: str
    Marker: str
    VolumeInfos: List[VolumeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBLocalGroupsInputRequestTypeDef(BaseModel):
    GatewayARN: str
    SMBLocalGroups: SMBLocalGroupsTypeDef

class DescribeSMBFileSharesOutputTypeDef(BaseModel):
    SMBFileShareInfoList: List[SMBFileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomaticTapeCreationPoliciesOutputTypeDef(BaseModel):
    AutomaticTapeCreationPolicyInfos: List[AutomaticTapeCreationPolicyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBandwidthRateLimitScheduleInputRequestTypeDef(BaseModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalUnionTypeDef]

class DescribeCachediSCSIVolumesOutputTypeDef(BaseModel):
    CachediSCSIVolumes: List[CachediSCSIVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorediSCSIVolumesOutputTypeDef(BaseModel):
    StorediSCSIVolumes: List[StorediSCSIVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNFSFileSharesOutputTypeDef(BaseModel):
    NFSFileShareInfoList: List[NFSFileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVTLDevicesOutputTypeDef(BaseModel):
    GatewayARN: str
    VTLDevices: List[VTLDeviceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFileSystemAssociationsOutputTypeDef(BaseModel):
    FileSystemAssociationInfoList: List[FileSystemAssociationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

