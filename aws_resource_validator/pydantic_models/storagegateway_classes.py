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
from aws_resource_validator.pydantic_models.storagegateway_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddCacheInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskIds: Sequence[str]


class AddUploadBufferInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskIds: Sequence[str]


class AddWorkingStorageInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskIds: Sequence[str]


class AssignTapePoolInputTypeDef(BaseValidatorModel):
    TapeARN: str
    PoolId: str
    BypassGovernanceRetention: Optional[bool] = None


class CacheAttributesTypeDef(BaseValidatorModel):
    CacheStaleTimeoutInSeconds: Optional[int] = None


class AttachVolumeInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    VolumeARN: str
    NetworkInterfaceId: str
    TargetName: Optional[str] = None
    DiskId: Optional[str] = None


class AutomaticTapeCreationRuleTypeDef(BaseValidatorModel):
    TapeBarcodePrefix: str
    PoolId: str
    TapeSizeInBytes: int
    MinimumNumTapes: int
    Worm: Optional[bool] = None


class BandwidthRateLimitIntervalOutputTypeDef(BaseValidatorModel):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: List[int]
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


class BandwidthRateLimitIntervalTypeDef(BaseValidatorModel):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: Sequence[int]
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


class CacheReportFilterOutputTypeDef(BaseValidatorModel):
    Name: CacheReportFilterNameType
    Values: List[str]


class CacheReportFilterTypeDef(BaseValidatorModel):
    Name: CacheReportFilterNameType
    Values: Sequence[str]


class VolumeiSCSIAttributesTypeDef(BaseValidatorModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    LunNumber: Optional[int] = None
    ChapEnabled: Optional[bool] = None


class CancelArchivalInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str


class CancelCacheReportInputTypeDef(BaseValidatorModel):
    CacheReportARN: str


class CancelRetrievalInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str


class ChapInfoTypeDef(BaseValidatorModel):
    TargetARN: Optional[str] = None
    SecretToAuthenticateInitiator: Optional[str] = None
    InitiatorName: Optional[str] = None
    SecretToAuthenticateTarget: Optional[str] = None


class NFSFileShareDefaultsTypeDef(BaseValidatorModel):
    FileMode: Optional[str] = None
    DirectoryMode: Optional[str] = None
    GroupId: Optional[int] = None
    OwnerId: Optional[int] = None


class DeleteAutomaticTapeCreationPolicyInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DeleteBandwidthRateLimitInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    BandwidthType: str


class DeleteCacheReportInputTypeDef(BaseValidatorModel):
    CacheReportARN: str


class DeleteChapCredentialsInputTypeDef(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str


class DeleteFileShareInputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ForceDelete: Optional[bool] = None


class DeleteGatewayInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DeleteSnapshotScheduleInputTypeDef(BaseValidatorModel):
    VolumeARN: str


class DeleteTapeArchiveInputTypeDef(BaseValidatorModel):
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None


class DeleteTapeInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeARN: str
    BypassGovernanceRetention: Optional[bool] = None


class DeleteTapePoolInputTypeDef(BaseValidatorModel):
    PoolARN: str


class DeleteVolumeInputTypeDef(BaseValidatorModel):
    VolumeARN: str


class DescribeAvailabilityMonitorTestInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DescribeBandwidthRateLimitInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DescribeBandwidthRateLimitScheduleInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DescribeCacheInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DescribeCacheReportInputTypeDef(BaseValidatorModel):
    CacheReportARN: str


class DescribeCachediSCSIVolumesInputTypeDef(BaseValidatorModel):
    VolumeARNs: Sequence[str]


class DescribeChapCredentialsInputTypeDef(BaseValidatorModel):
    TargetARN: str


class DescribeFileSystemAssociationsInputTypeDef(BaseValidatorModel):
    FileSystemAssociationARNList: Sequence[str]


class DescribeGatewayInformationInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class NetworkInterfaceTypeDef(BaseValidatorModel):
    Ipv4Address: Optional[str] = None
    MacAddress: Optional[str] = None
    Ipv6Address: Optional[str] = None


class DescribeMaintenanceStartTimeInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class SoftwareUpdatePreferencesTypeDef(BaseValidatorModel):
    AutomaticUpdatePolicy: Optional[AutomaticUpdatePolicyType] = None


class DescribeNFSFileSharesInputTypeDef(BaseValidatorModel):
    FileShareARNList: Sequence[str]


class DescribeSMBFileSharesInputTypeDef(BaseValidatorModel):
    FileShareARNList: Sequence[str]


class DescribeSMBSettingsInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class SMBLocalGroupsOutputTypeDef(BaseValidatorModel):
    GatewayAdmins: Optional[List[str]] = None


class DescribeSnapshotScheduleInputTypeDef(BaseValidatorModel):
    VolumeARN: str


class DescribeStorediSCSIVolumesInputTypeDef(BaseValidatorModel):
    VolumeARNs: Sequence[str]


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeTapeArchivesInputTypeDef(BaseValidatorModel):
    TapeARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeArchiveTypeDef(BaseValidatorModel):
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


class DescribeTapeRecoveryPointsInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeRecoveryPointInfoTypeDef(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeRecoveryPointTime: Optional[datetime] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None


class DescribeTapesInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeTypeDef(BaseValidatorModel):
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


class DescribeUploadBufferInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DescribeVTLDevicesInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class DescribeWorkingStorageInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DetachVolumeInputTypeDef(BaseValidatorModel):
    VolumeARN: str
    ForceDetach: Optional[bool] = None


class DeviceiSCSIAttributesTypeDef(BaseValidatorModel):
    TargetARN: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfacePort: Optional[int] = None
    ChapEnabled: Optional[bool] = None


class DisableGatewayInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class DisassociateFileSystemInputTypeDef(BaseValidatorModel):
    FileSystemAssociationARN: str
    ForceDelete: Optional[bool] = None


class DiskTypeDef(BaseValidatorModel):
    DiskId: Optional[str] = None
    DiskPath: Optional[str] = None
    DiskNode: Optional[str] = None
    DiskStatus: Optional[str] = None
    DiskSizeInBytes: Optional[int] = None
    DiskAllocationType: Optional[str] = None
    DiskAllocationResource: Optional[str] = None
    DiskAttributeList: Optional[List[str]] = None


class EndpointNetworkConfigurationOutputTypeDef(BaseValidatorModel):
    IpAddresses: Optional[List[str]] = None


class EndpointNetworkConfigurationTypeDef(BaseValidatorModel):
    IpAddresses: Optional[Sequence[str]] = None


class EvictFilesFailingUploadInputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ForceRemove: Optional[bool] = None


class FileShareInfoTypeDef(BaseValidatorModel):
    FileShareType: Optional[FileShareTypeType] = None
    FileShareARN: Optional[str] = None
    FileShareId: Optional[str] = None
    FileShareStatus: Optional[str] = None
    GatewayARN: Optional[str] = None


class FileSystemAssociationStatusDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None


class FileSystemAssociationSummaryTypeDef(BaseValidatorModel):
    FileSystemAssociationId: Optional[str] = None
    FileSystemAssociationARN: Optional[str] = None
    FileSystemAssociationStatus: Optional[str] = None
    GatewayARN: Optional[str] = None


class GatewayInfoTypeDef(BaseValidatorModel):
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


class JoinDomainInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DomainName: str
    UserName: str
    Password: str
    OrganizationalUnit: Optional[str] = None
    DomainControllers: Optional[Sequence[str]] = None
    TimeoutInSeconds: Optional[int] = None


class ListAutomaticTapeCreationPoliciesInputTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None


class ListCacheReportsInputTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None


class ListFileSharesInputTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListFileSystemAssociationsInputTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListGatewaysInputTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class ListLocalDisksInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class ListTapePoolsInputTypeDef(BaseValidatorModel):
    PoolARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class PoolInfoTypeDef(BaseValidatorModel):
    PoolARN: Optional[str] = None
    PoolName: Optional[str] = None
    StorageClass: Optional[TapeStorageClassType] = None
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    PoolStatus: Optional[PoolStatusType] = None


class ListTapesInputTypeDef(BaseValidatorModel):
    TapeARNs: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class TapeInfoTypeDef(BaseValidatorModel):
    TapeARN: Optional[str] = None
    TapeBarcode: Optional[str] = None
    TapeSizeInBytes: Optional[int] = None
    TapeStatus: Optional[str] = None
    GatewayARN: Optional[str] = None
    PoolId: Optional[str] = None
    RetentionStartDate: Optional[datetime] = None
    PoolEntryDate: Optional[datetime] = None


class ListVolumeInitiatorsInputTypeDef(BaseValidatorModel):
    VolumeARN: str


class ListVolumeRecoveryPointsInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class VolumeRecoveryPointInfoTypeDef(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeUsageInBytes: Optional[int] = None
    VolumeRecoveryPointTime: Optional[str] = None


class ListVolumesInputTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    Marker: Optional[str] = None
    Limit: Optional[int] = None


class VolumeInfoTypeDef(BaseValidatorModel):
    VolumeARN: Optional[str] = None
    VolumeId: Optional[str] = None
    GatewayARN: Optional[str] = None
    GatewayId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeSizeInBytes: Optional[int] = None
    VolumeAttachmentStatus: Optional[str] = None


class NotifyWhenUploadedInputTypeDef(BaseValidatorModel):
    FileShareARN: str


class RefreshCacheInputTypeDef(BaseValidatorModel):
    FileShareARN: str
    FolderList: Optional[Sequence[str]] = None
    Recursive: Optional[bool] = None


class RemoveTagsFromResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class ResetCacheInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class RetrieveTapeArchiveInputTypeDef(BaseValidatorModel):
    TapeARN: str
    GatewayARN: str


class RetrieveTapeRecoveryPointInputTypeDef(BaseValidatorModel):
    TapeARN: str
    GatewayARN: str


class SMBLocalGroupsTypeDef(BaseValidatorModel):
    GatewayAdmins: Optional[Sequence[str]] = None


class SetLocalConsolePasswordInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    LocalConsolePassword: str


class SetSMBGuestPasswordInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    Password: str


class ShutdownGatewayInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class StartAvailabilityMonitorTestInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class StartGatewayInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class UpdateBandwidthRateLimitInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: Optional[int] = None
    AverageDownloadRateLimitInBitsPerSec: Optional[int] = None


class UpdateChapCredentialsInputTypeDef(BaseValidatorModel):
    TargetARN: str
    SecretToAuthenticateInitiator: str
    InitiatorName: str
    SecretToAuthenticateTarget: Optional[str] = None


class UpdateGatewayInformationInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    GatewayName: Optional[str] = None
    GatewayTimezone: Optional[str] = None
    CloudWatchLogGroupARN: Optional[str] = None
    GatewayCapacity: Optional[GatewayCapacityType] = None


class UpdateGatewaySoftwareNowInputTypeDef(BaseValidatorModel):
    GatewayARN: str


class UpdateSMBFileShareVisibilityInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    FileSharesVisible: bool


class UpdateSMBSecurityStrategyInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    SMBSecurityStrategy: SMBSecurityStrategyType


class UpdateVTLDeviceTypeInputTypeDef(BaseValidatorModel):
    VTLDeviceARN: str
    DeviceType: str


class ActivateGatewayInputTypeDef(BaseValidatorModel):
    ActivationKey: str
    GatewayName: str
    GatewayTimezone: str
    GatewayRegion: str
    GatewayType: Optional[str] = None
    TapeDriveType: Optional[str] = None
    MediumChangerType: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class AddTagsToResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateCachediSCSIVolumeInputTypeDef(BaseValidatorModel):
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


class CreateSnapshotFromVolumeRecoveryPointInputTypeDef(BaseValidatorModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateSnapshotInputTypeDef(BaseValidatorModel):
    VolumeARN: str
    SnapshotDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateStorediSCSIVolumeInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskId: str
    PreserveExistingData: bool
    TargetName: str
    NetworkInterfaceId: str
    SnapshotId: Optional[str] = None
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateTapePoolInputTypeDef(BaseValidatorModel):
    PoolName: str
    StorageClass: TapeStorageClassType
    RetentionLockType: Optional[RetentionLockTypeType] = None
    RetentionLockTimeInDays: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateTapeWithBarcodeInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeSizeInBytes: int
    TapeBarcode: str
    KMSEncrypted: Optional[bool] = None
    KMSKey: Optional[str] = None
    PoolId: Optional[str] = None
    Worm: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateTapesInputTypeDef(BaseValidatorModel):
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


class UpdateSnapshotScheduleInputTypeDef(BaseValidatorModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ActivateGatewayOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddCacheOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddTagsToResourceOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddUploadBufferOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddWorkingStorageOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssignTapePoolOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateFileSystemOutputTypeDef(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class AttachVolumeOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelArchivalOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelCacheReportOutputTypeDef(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelRetrievalOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCachediSCSIVolumeOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNFSFileShareOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSMBFileShareOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSnapshotFromVolumeRecoveryPointOutputTypeDef(BaseValidatorModel):
    SnapshotId: str
    VolumeARN: str
    VolumeRecoveryPointTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSnapshotOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStorediSCSIVolumeOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    VolumeSizeInBytes: int
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTapePoolOutputTypeDef(BaseValidatorModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTapeWithBarcodeOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTapesOutputTypeDef(BaseValidatorModel):
    TapeARNs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAutomaticTapeCreationPolicyOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBandwidthRateLimitOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCacheReportOutputTypeDef(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteChapCredentialsOutputTypeDef(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFileShareOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteGatewayOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSnapshotScheduleOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTapeArchiveOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTapeOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTapePoolOutputTypeDef(BaseValidatorModel):
    PoolARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVolumeOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAvailabilityMonitorTestOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    Status: AvailabilityMonitorTestStatusType
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBandwidthRateLimitOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCacheOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    CacheAllocatedInBytes: int
    CacheUsedPercentage: float
    CacheDirtyPercentage: float
    CacheHitPercentage: float
    CacheMissPercentage: float
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSnapshotScheduleOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: str
    Timezone: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUploadBufferOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    UploadBufferUsedInBytes: int
    UploadBufferAllocatedInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkingStorageOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DiskIds: List[str]
    WorkingStorageUsedInBytes: int
    WorkingStorageAllocatedInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef


class DetachVolumeOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisableGatewayOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateFileSystemOutputTypeDef(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class EvictFilesFailingUploadOutputTypeDef(BaseValidatorModel):
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class JoinDomainOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    Marker: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListVolumeInitiatorsOutputTypeDef(BaseValidatorModel):
    Initiators: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class NotifyWhenUploadedOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RefreshCacheOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveTagsFromResourceOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResetCacheOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class RetrieveTapeArchiveOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class RetrieveTapeRecoveryPointOutputTypeDef(BaseValidatorModel):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetLocalConsolePasswordOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetSMBGuestPasswordOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class ShutdownGatewayOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartAvailabilityMonitorTestOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartCacheReportOutputTypeDef(BaseValidatorModel):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartGatewayOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAutomaticTapeCreationPolicyOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBandwidthRateLimitOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBandwidthRateLimitScheduleOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateChapCredentialsOutputTypeDef(BaseValidatorModel):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFileSystemAssociationOutputTypeDef(BaseValidatorModel):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGatewayInformationOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    GatewayName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGatewaySoftwareNowOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMaintenanceStartTimeOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNFSFileShareOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSMBFileShareOutputTypeDef(BaseValidatorModel):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSMBFileShareVisibilityOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSMBLocalGroupsOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSMBSecurityStrategyOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSnapshotScheduleOutputTypeDef(BaseValidatorModel):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVTLDeviceTypeOutputTypeDef(BaseValidatorModel):
    VTLDeviceARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFileSystemAssociationInputTypeDef(BaseValidatorModel):
    FileSystemAssociationARN: str
    UserName: Optional[str] = None
    Password: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None


class AutomaticTapeCreationPolicyInfoTypeDef(BaseValidatorModel):
    AutomaticTapeCreationRules: Optional[List[AutomaticTapeCreationRuleTypeDef]] = None
    GatewayARN: Optional[str] = None


class UpdateAutomaticTapeCreationPolicyInputTypeDef(BaseValidatorModel):
    AutomaticTapeCreationRules: Sequence[AutomaticTapeCreationRuleTypeDef]
    GatewayARN: str


class DescribeBandwidthRateLimitScheduleOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CacheReportInfoTypeDef(BaseValidatorModel):
    CacheReportARN: Optional[str] = None
    CacheReportStatus: Optional[CacheReportStatusType] = None
    ReportCompletionPercent: Optional[int] = None
    EndTime: Optional[datetime] = None
    Role: Optional[str] = None
    FileShareARN: Optional[str] = None
    LocationARN: Optional[str] = None
    StartTime: Optional[datetime] = None
    InclusionFilters: Optional[List[CacheReportFilterOutputTypeDef]] = None
    ExclusionFilters: Optional[List[CacheReportFilterOutputTypeDef]] = None
    ReportName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class CachediSCSIVolumeTypeDef(BaseValidatorModel):
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


class StorediSCSIVolumeTypeDef(BaseValidatorModel):
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


class DescribeChapCredentialsOutputTypeDef(BaseValidatorModel):
    ChapCredentials: List[ChapInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGatewayInformationOutputTypeDef(BaseValidatorModel):
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


class DescribeMaintenanceStartTimeOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfWeek: int
    DayOfMonth: int
    Timezone: str
    SoftwareUpdatePreferences: SoftwareUpdatePreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMaintenanceStartTimeInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    HourOfDay: Optional[int] = None
    MinuteOfHour: Optional[int] = None
    DayOfWeek: Optional[int] = None
    DayOfMonth: Optional[int] = None
    SoftwareUpdatePreferences: Optional[SoftwareUpdatePreferencesTypeDef] = None


class DescribeSMBSettingsOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    DomainName: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    SMBGuestPasswordSet: bool
    SMBSecurityStrategy: SMBSecurityStrategyType
    FileSharesVisible: bool
    SMBLocalGroups: SMBLocalGroupsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTapeArchivesInputPaginateTypeDef(BaseValidatorModel):
    TapeARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTapeRecoveryPointsInputPaginateTypeDef(BaseValidatorModel):
    GatewayARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTapesInputPaginateTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeVTLDevicesInputPaginateTypeDef(BaseValidatorModel):
    GatewayARN: str
    VTLDeviceARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFileSharesInputPaginateTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFileSystemAssociationsInputPaginateTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGatewaysInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceInputPaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTapePoolsInputPaginateTypeDef(BaseValidatorModel):
    PoolARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTapesInputPaginateTypeDef(BaseValidatorModel):
    TapeARNs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVolumesInputPaginateTypeDef(BaseValidatorModel):
    GatewayARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTapeArchivesOutputTypeDef(BaseValidatorModel):
    TapeArchives: List[TapeArchiveTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTapeRecoveryPointsOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    TapeRecoveryPointInfos: List[TapeRecoveryPointInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTapesOutputTypeDef(BaseValidatorModel):
    Tapes: List[TapeTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class VTLDeviceTypeDef(BaseValidatorModel):
    VTLDeviceARN: Optional[str] = None
    VTLDeviceType: Optional[str] = None
    VTLDeviceVendor: Optional[str] = None
    VTLDeviceProductIdentifier: Optional[str] = None
    DeviceiSCSIAttributes: Optional[DeviceiSCSIAttributesTypeDef] = None


class ListLocalDisksOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    Disks: List[DiskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListFileSharesOutputTypeDef(BaseValidatorModel):
    Marker: str
    NextMarker: str
    FileShareInfoList: List[FileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FileSystemAssociationInfoTypeDef(BaseValidatorModel):
    FileSystemAssociationARN: Optional[str] = None
    LocationARN: Optional[str] = None
    FileSystemAssociationStatus: Optional[str] = None
    AuditDestinationARN: Optional[str] = None
    GatewayARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    EndpointNetworkConfiguration: Optional[EndpointNetworkConfigurationOutputTypeDef] = None
    FileSystemAssociationStatusDetails: Optional[List[FileSystemAssociationStatusDetailTypeDef]] = None


class ListFileSystemAssociationsOutputTypeDef(BaseValidatorModel):
    Marker: str
    NextMarker: str
    FileSystemAssociationSummaryList: List[FileSystemAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListGatewaysOutputTypeDef(BaseValidatorModel):
    Gateways: List[GatewayInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTapePoolsOutputTypeDef(BaseValidatorModel):
    PoolInfos: List[PoolInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTapesOutputTypeDef(BaseValidatorModel):
    TapeInfos: List[TapeInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListVolumeRecoveryPointsOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    VolumeRecoveryPointInfos: List[VolumeRecoveryPointInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListVolumesOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    Marker: str
    VolumeInfos: List[VolumeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SMBFileShareInfoTypeDef(BaseValidatorModel):
    pass


class DescribeSMBFileSharesOutputTypeDef(BaseValidatorModel):
    SMBFileShareInfoList: List[SMBFileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAutomaticTapeCreationPoliciesOutputTypeDef(BaseValidatorModel):
    AutomaticTapeCreationPolicyInfos: List[AutomaticTapeCreationPolicyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BandwidthRateLimitIntervalUnionTypeDef(BaseValidatorModel):
    pass


class UpdateBandwidthRateLimitScheduleInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalUnionTypeDef]


class DescribeCacheReportOutputTypeDef(BaseValidatorModel):
    CacheReportInfo: CacheReportInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCacheReportsOutputTypeDef(BaseValidatorModel):
    CacheReportList: List[CacheReportInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CacheReportFilterUnionTypeDef(BaseValidatorModel):
    pass


class StartCacheReportInputTypeDef(BaseValidatorModel):
    FileShareARN: str
    Role: str
    LocationARN: str
    BucketRegion: str
    ClientToken: str
    VPCEndpointDNSName: Optional[str] = None
    InclusionFilters: Optional[Sequence[CacheReportFilterUnionTypeDef]] = None
    ExclusionFilters: Optional[Sequence[CacheReportFilterUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeCachediSCSIVolumesOutputTypeDef(BaseValidatorModel):
    CachediSCSIVolumes: List[CachediSCSIVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeStorediSCSIVolumesOutputTypeDef(BaseValidatorModel):
    StorediSCSIVolumes: List[StorediSCSIVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class NFSFileShareInfoTypeDef(BaseValidatorModel):
    pass


class DescribeNFSFileSharesOutputTypeDef(BaseValidatorModel):
    NFSFileShareInfoList: List[NFSFileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVTLDevicesOutputTypeDef(BaseValidatorModel):
    GatewayARN: str
    VTLDevices: List[VTLDeviceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointNetworkConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class AssociateFileSystemInputTypeDef(BaseValidatorModel):
    UserName: str
    Password: str
    ClientToken: str
    GatewayARN: str
    LocationARN: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    AuditDestinationARN: Optional[str] = None
    CacheAttributes: Optional[CacheAttributesTypeDef] = None
    EndpointNetworkConfiguration: Optional[EndpointNetworkConfigurationUnionTypeDef] = None


class DescribeFileSystemAssociationsOutputTypeDef(BaseValidatorModel):
    FileSystemAssociationInfoList: List[FileSystemAssociationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SMBLocalGroupsUnionTypeDef(BaseValidatorModel):
    pass


class UpdateSMBLocalGroupsInputTypeDef(BaseValidatorModel):
    GatewayARN: str
    SMBLocalGroups: SMBLocalGroupsUnionTypeDef


