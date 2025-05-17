from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.fsx.fsx_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActiveDirectoryBackupAttributes(BaseValidatorModel):
    DomainName: Optional[str] = None
    ActiveDirectoryId: Optional[str] = None
    ResourceARN: Optional[str] = None


class AdministrativeActionFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class AggregateConfiguration(BaseValidatorModel):
    Aggregates: Optional[List[str]] = None
    TotalConstituents: Optional[int] = None


class Alias(BaseValidatorModel):
    Name: Optional[str] = None
    Lifecycle: Optional[AliasLifecycleType] = None


# This class is the input for the 'associate_file_system_aliases' function.
class AssociateFileSystemAliasesRequest(BaseValidatorModel):
    FileSystemId: str
    Aliases: List[str]
    ClientRequestToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AutoExportPolicyOutput(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutoExportPolicy(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutoImportPolicyOutput(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutoImportPolicy(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutocommitPeriod(BaseValidatorModel):
    Type: AutocommitPeriodTypeType
    Value: Optional[int] = None


class BackupFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'cancel_data_repository_task' function.
class CancelDataRepositoryTaskRequest(BaseValidatorModel):
    TaskId: str


class CompletionReport(BaseValidatorModel):
    Enabled: bool
    Path: Optional[str] = None
    Format: Optional[Literal['REPORT_CSV_20191124']] = None
    Scope: Optional[Literal['FAILED_FILES_ONLY']] = None


# This class is the input for the 'copy_snapshot_and_update_volume' function.
class CopySnapshotAndUpdateVolumeRequest(BaseValidatorModel):
    VolumeId: str
    SourceSnapshotARN: str
    ClientRequestToken: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None
    Options: Optional[List[UpdateOpenZFSVolumeOptionType]] = None


class CreateAggregateConfiguration(BaseValidatorModel):
    Aggregates: Optional[List[str]] = None
    ConstituentsPerAggregate: Optional[int] = None


class FileCacheLustreMetadataConfiguration(BaseValidatorModel):
    StorageCapacity: int


class CreateFileSystemLustreMetadataConfiguration(BaseValidatorModel):
    Mode: MetadataConfigurationModeType
    Iops: Optional[int] = None


class LustreLogCreateConfiguration(BaseValidatorModel):
    Level: LustreAccessAuditLogLevelType
    Destination: Optional[str] = None


class DiskIopsConfiguration(BaseValidatorModel):
    Mode: Optional[DiskIopsConfigurationModeType] = None
    Iops: Optional[int] = None


class OpenZFSReadCacheConfiguration(BaseValidatorModel):
    SizingMode: Optional[OpenZFSReadCacheSizingModeType] = None
    SizeGiB: Optional[int] = None


class SelfManagedActiveDirectoryConfiguration(BaseValidatorModel):
    DomainName: str
    UserName: str
    Password: str
    DnsIps: List[str]
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None


class WindowsAuditLogCreateConfiguration(BaseValidatorModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None


class TieringPolicy(BaseValidatorModel):
    CoolingPeriod: Optional[int] = None
    Name: Optional[TieringPolicyNameType] = None


class CreateOpenZFSOriginSnapshotConfiguration(BaseValidatorModel):
    SnapshotARN: str
    CopyStrategy: OpenZFSCopyStrategyType


class OpenZFSUserOrGroupQuota(BaseValidatorModel):
    Type: OpenZFSQuotaTypeType
    Id: int
    StorageCapacityQuotaGiB: int


class DataRepositoryFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class DataRepositoryTaskFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class DataRepositoryTaskFilter(BaseValidatorModel):
    Name: Optional[DataRepositoryTaskFilterNameType] = None
    Values: Optional[List[str]] = None


class DataRepositoryTaskStatus(BaseValidatorModel):
    TotalCount: Optional[int] = None
    SucceededCount: Optional[int] = None
    FailedCount: Optional[int] = None
    LastUpdatedTime: Optional[datetime] = None
    ReleasedCapacity: Optional[int] = None


# This class is the input for the 'delete_backup' function.
class DeleteBackupRequest(BaseValidatorModel):
    BackupId: str
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'delete_data_repository_association' function.
class DeleteDataRepositoryAssociationRequest(BaseValidatorModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    DeleteDataInFileSystem: Optional[bool] = None


# This class is the input for the 'delete_file_cache' function.
class DeleteFileCacheRequest(BaseValidatorModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'delete_snapshot' function.
class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'delete_storage_virtual_machine' function.
class DeleteStorageVirtualMachineRequest(BaseValidatorModel):
    StorageVirtualMachineId: str
    ClientRequestToken: Optional[str] = None


class DeleteVolumeOpenZFSConfiguration(BaseValidatorModel):
    Options: Optional[List[Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']]] = None


class Filter(BaseValidatorModel):
    Name: Optional[FilterNameType] = None
    Values: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_file_caches' function.
class DescribeFileCachesRequest(BaseValidatorModel):
    FileCacheIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_file_system_aliases' function.
class DescribeFileSystemAliasesRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_file_systems' function.
class DescribeFileSystemsRequest(BaseValidatorModel):
    FileSystemIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SnapshotFilter(BaseValidatorModel):
    Name: Optional[SnapshotFilterNameType] = None
    Values: Optional[List[str]] = None


class StorageVirtualMachineFilter(BaseValidatorModel):
    Name: Optional[Literal['file-system-id']] = None
    Values: Optional[List[str]] = None


class VolumeFilter(BaseValidatorModel):
    Name: Optional[VolumeFilterNameType] = None
    Values: Optional[List[str]] = None


# This class is the input for the 'disassociate_file_system_aliases' function.
class DisassociateFileSystemAliasesRequest(BaseValidatorModel):
    FileSystemId: str
    Aliases: List[str]
    ClientRequestToken: Optional[str] = None


class DurationSinceLastAccess(BaseValidatorModel):
    Unit: Optional[Literal['DAYS']] = None
    Value: Optional[int] = None


class FileCacheFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class FileCacheNFSConfiguration(BaseValidatorModel):
    Version: Literal['NFS3']
    DnsIps: Optional[List[str]] = None


class LustreLogConfiguration(BaseValidatorModel):
    Level: LustreAccessAuditLogLevelType
    Destination: Optional[str] = None


class FileSystemEndpoint(BaseValidatorModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None


class FileSystemFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class FileSystemLustreMetadataConfiguration(BaseValidatorModel):
    Mode: MetadataConfigurationModeType
    Iops: Optional[int] = None


class LifecycleTransitionReason(BaseValidatorModel):
    Message: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LustreRootSquashConfigurationOutput(BaseValidatorModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[List[str]] = None


class LustreRootSquashConfiguration(BaseValidatorModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[List[str]] = None


class OpenZFSClientConfigurationOutput(BaseValidatorModel):
    Clients: str
    Options: List[str]


class OpenZFSClientConfiguration(BaseValidatorModel):
    Clients: str
    Options: List[str]


class OpenZFSOriginSnapshotConfiguration(BaseValidatorModel):
    SnapshotARN: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None


# This class is the input for the 'release_file_system_nfs_v3_locks' function.
class ReleaseFileSystemNfsV3LocksRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'restore_volume_from_snapshot' function.
class RestoreVolumeFromSnapshotRequest(BaseValidatorModel):
    VolumeId: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None
    Options: Optional[List[RestoreOpenZFSVolumeOptionType]] = None


class RetentionPeriod(BaseValidatorModel):
    Type: RetentionPeriodTypeType
    Value: Optional[int] = None


class SelfManagedActiveDirectoryAttributes(BaseValidatorModel):
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None
    UserName: Optional[str] = None
    DnsIps: Optional[List[str]] = None


class SelfManagedActiveDirectoryConfigurationUpdates(BaseValidatorModel):
    UserName: Optional[str] = None
    Password: Optional[str] = None
    DnsIps: Optional[List[str]] = None
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None


# This class is the input for the 'start_misconfigured_state_recovery' function.
class StartMisconfiguredStateRecoveryRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None


class SvmEndpoint(BaseValidatorModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateFileCacheLustreConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None


class UpdateFileSystemLustreMetadataConfiguration(BaseValidatorModel):
    Iops: Optional[int] = None
    Mode: Optional[MetadataConfigurationModeType] = None


# This class is the input for the 'update_shared_vpc_configuration' function.
class UpdateSharedVpcConfigurationRequest(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: Optional[str] = None
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'update_snapshot' function.
class UpdateSnapshotRequest(BaseValidatorModel):
    Name: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None


class WindowsAuditLogConfiguration(BaseValidatorModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None


# This class is the output for the 'associate_file_system_aliases' function.
class AssociateFileSystemAliasesResponse(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_data_repository_task' function.
class CancelDataRepositoryTaskResponse(BaseValidatorModel):
    Lifecycle: DataRepositoryTaskLifecycleType
    TaskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backup' function.
class DeleteBackupResponse(BaseValidatorModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_repository_association' function.
class DeleteDataRepositoryAssociationResponse(BaseValidatorModel):
    AssociationId: str
    Lifecycle: DataRepositoryLifecycleType
    DeleteDataInFileSystem: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_file_cache' function.
class DeleteFileCacheResponse(BaseValidatorModel):
    FileCacheId: str
    Lifecycle: FileCacheLifecycleType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot' function.
class DeleteSnapshotResponse(BaseValidatorModel):
    SnapshotId: str
    Lifecycle: SnapshotLifecycleType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_storage_virtual_machine' function.
class DeleteStorageVirtualMachineResponse(BaseValidatorModel):
    StorageVirtualMachineId: str
    Lifecycle: StorageVirtualMachineLifecycleType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_file_system_aliases' function.
class DescribeFileSystemAliasesResponse(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSharedVpcConfigurationResponse(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_file_system_aliases' function.
class DisassociateFileSystemAliasesResponse(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_shared_vpc_configuration' function.
class UpdateSharedVpcConfigurationResponse(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadata


class NFSDataRepositoryConfiguration(BaseValidatorModel):
    Version: Literal['NFS3']
    DnsIps: Optional[List[str]] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutput] = None


class S3DataRepositoryConfigurationOutput(BaseValidatorModel):
    AutoImportPolicy: Optional[AutoImportPolicyOutput] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutput] = None


class S3DataRepositoryConfiguration(BaseValidatorModel):
    AutoImportPolicy: Optional[AutoImportPolicy] = None
    AutoExportPolicy: Optional[AutoExportPolicy] = None


# This class is the input for the 'copy_backup' function.
class CopyBackupRequest(BaseValidatorModel):
    SourceBackupId: str
    ClientRequestToken: Optional[str] = None
    SourceRegion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_backup' function.
class CreateBackupRequest(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VolumeId: Optional[str] = None


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotRequest(BaseValidatorModel):
    Name: str
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DeleteFileSystemLustreConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteFileSystemLustreResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteFileSystemOpenZFSConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[List[Tag]] = None
    Options: Optional[List[Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']]] = None


class DeleteFileSystemOpenZFSResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteFileSystemWindowsConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteFileSystemWindowsResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteVolumeOntapConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[List[Tag]] = None
    BypassSnaplockEnterpriseRetention: Optional[bool] = None


class DeleteVolumeOntapResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class CreateFileCacheLustreConfiguration(BaseValidatorModel):
    PerUnitStorageThroughput: int
    DeploymentType: Literal['CACHE_1']
    MetadataConfiguration: FileCacheLustreMetadataConfiguration
    WeeklyMaintenanceStartTime: Optional[str] = None


class CreateFileSystemOntapConfiguration(BaseValidatorModel):
    DeploymentType: OntapDeploymentTypeType
    AutomaticBackupRetentionDays: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    EndpointIpAddressRange: Optional[str] = None
    FsxAdminPassword: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None
    PreferredSubnetId: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    HAPairs: Optional[int] = None
    ThroughputCapacityPerHAPair: Optional[int] = None


class UpdateFileSystemOntapConfiguration(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    FsxAdminPassword: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None
    ThroughputCapacity: Optional[int] = None
    AddRouteTableIds: Optional[List[str]] = None
    RemoveRouteTableIds: Optional[List[str]] = None
    ThroughputCapacityPerHAPair: Optional[int] = None
    HAPairs: Optional[int] = None


class OpenZFSFileSystemConfiguration(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    DeploymentType: Optional[OpenZFSDeploymentTypeType] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None
    RootVolumeId: Optional[str] = None
    PreferredSubnetId: Optional[str] = None
    EndpointIpAddressRange: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    EndpointIpAddress: Optional[str] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfiguration] = None


class UpdateFileSystemOpenZFSConfiguration(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None
    AddRouteTableIds: Optional[List[str]] = None
    RemoveRouteTableIds: Optional[List[str]] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfiguration] = None


class CreateSvmActiveDirectoryConfiguration(BaseValidatorModel):
    NetBiosName: str
    SelfManagedActiveDirectoryConfiguration: Optional[SelfManagedActiveDirectoryConfiguration] = None


class CreateFileSystemWindowsConfiguration(BaseValidatorModel):
    ThroughputCapacity: int
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[SelfManagedActiveDirectoryConfiguration] = None
    DeploymentType: Optional[WindowsDeploymentTypeType] = None
    PreferredSubnetId: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    Aliases: Optional[List[str]] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfiguration] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None


class DataRepositoryConfiguration(BaseValidatorModel):
    Lifecycle: Optional[DataRepositoryLifecycleType] = None
    ImportPath: Optional[str] = None
    ExportPath: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    FailureDetails: Optional[DataRepositoryFailureDetails] = None


# This class is the input for the 'describe_data_repository_tasks' function.
class DescribeDataRepositoryTasksRequest(BaseValidatorModel):
    TaskIds: Optional[List[str]] = None
    Filters: Optional[List[DataRepositoryTaskFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_backups' function.
class DescribeBackupsRequest(BaseValidatorModel):
    BackupIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_data_repository_associations' function.
class DescribeDataRepositoryAssociationsRequest(BaseValidatorModel):
    AssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBackupsRequestPaginate(BaseValidatorModel):
    BackupIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFileSystemsRequestPaginate(BaseValidatorModel):
    FileSystemIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_snapshots' function.
class DescribeSnapshotsRequest(BaseValidatorModel):
    SnapshotIds: Optional[List[str]] = None
    Filters: Optional[List[SnapshotFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeShared: Optional[bool] = None


class DescribeStorageVirtualMachinesRequestPaginate(BaseValidatorModel):
    StorageVirtualMachineIds: Optional[List[str]] = None
    Filters: Optional[List[StorageVirtualMachineFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_storage_virtual_machines' function.
class DescribeStorageVirtualMachinesRequest(BaseValidatorModel):
    StorageVirtualMachineIds: Optional[List[str]] = None
    Filters: Optional[List[StorageVirtualMachineFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVolumesRequestPaginate(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    Filters: Optional[List[VolumeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_volumes' function.
class DescribeVolumesRequest(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    Filters: Optional[List[VolumeFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReleaseConfiguration(BaseValidatorModel):
    DurationSinceLastAccess: Optional[DurationSinceLastAccess] = None


class FileCacheDataRepositoryAssociation(BaseValidatorModel):
    FileCachePath: str
    DataRepositoryPath: str
    DataRepositorySubdirectories: Optional[List[str]] = None
    NFS: Optional[FileCacheNFSConfiguration] = None


class FileCacheLustreConfiguration(BaseValidatorModel):
    PerUnitStorageThroughput: Optional[int] = None
    DeploymentType: Optional[Literal['CACHE_1']] = None
    MountName: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    MetadataConfiguration: Optional[FileCacheLustreMetadataConfiguration] = None
    LogConfiguration: Optional[LustreLogConfiguration] = None


class FileSystemEndpoints(BaseValidatorModel):
    Intercluster: Optional[FileSystemEndpoint] = None
    Management: Optional[FileSystemEndpoint] = None


class SnapshotPaginator(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    SnapshotId: Optional[str] = None
    Name: Optional[str] = None
    VolumeId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Lifecycle: Optional[SnapshotLifecycleType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReason] = None
    Tags: Optional[List[Tag]] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None


class Snapshot(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    SnapshotId: Optional[str] = None
    Name: Optional[str] = None
    VolumeId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Lifecycle: Optional[SnapshotLifecycleType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReason] = None
    Tags: Optional[List[Tag]] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None

LustreRootSquashConfigurationUnion = Union[LustreRootSquashConfiguration, LustreRootSquashConfigurationOutput]


class OpenZFSNfsExportOutput(BaseValidatorModel):
    ClientConfigurations: List[OpenZFSClientConfigurationOutput]

OpenZFSClientConfigurationUnion = Union[OpenZFSClientConfiguration, OpenZFSClientConfigurationOutput]


class SnaplockRetentionPeriod(BaseValidatorModel):
    DefaultRetention: RetentionPeriod
    MinimumRetention: RetentionPeriod
    MaximumRetention: RetentionPeriod


class SvmActiveDirectoryConfiguration(BaseValidatorModel):
    NetBiosName: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[SelfManagedActiveDirectoryAttributes] = None


class UpdateFileSystemWindowsConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    ThroughputCapacity: Optional[int] = None
    SelfManagedActiveDirectoryConfiguration: Optional[SelfManagedActiveDirectoryConfigurationUpdates] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfiguration] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None


class UpdateSvmActiveDirectoryConfiguration(BaseValidatorModel):
    SelfManagedActiveDirectoryConfiguration: Optional[SelfManagedActiveDirectoryConfigurationUpdates] = None
    NetBiosName: Optional[str] = None


class SvmEndpoints(BaseValidatorModel):
    Iscsi: Optional[SvmEndpoint] = None
    Management: Optional[SvmEndpoint] = None
    Nfs: Optional[SvmEndpoint] = None
    Smb: Optional[SvmEndpoint] = None


# This class is the input for the 'update_file_cache' function.
class UpdateFileCacheRequest(BaseValidatorModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None
    LustreConfiguration: Optional[UpdateFileCacheLustreConfiguration] = None


class WindowsFileSystemConfiguration(BaseValidatorModel):
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[SelfManagedActiveDirectoryAttributes] = None
    DeploymentType: Optional[WindowsDeploymentTypeType] = None
    RemoteAdministrationEndpoint: Optional[str] = None
    PreferredSubnetId: Optional[str] = None
    PreferredFileServerIp: Optional[str] = None
    ThroughputCapacity: Optional[int] = None
    MaintenanceOperationsInProgress: Optional[List[FileSystemMaintenanceOperationType]] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    Aliases: Optional[List[Alias]] = None
    AuditLogConfiguration: Optional[WindowsAuditLogConfiguration] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None


class DataRepositoryAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    ResourceARN: Optional[str] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[DataRepositoryLifecycleType] = None
    FailureDetails: Optional[DataRepositoryFailureDetails] = None
    FileSystemPath: Optional[str] = None
    DataRepositoryPath: Optional[str] = None
    BatchImportMetaDataOnCreate: Optional[bool] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationOutput] = None
    Tags: Optional[List[Tag]] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCachePath: Optional[str] = None
    DataRepositorySubdirectories: Optional[List[str]] = None
    NFS: Optional[NFSDataRepositoryConfiguration] = None

S3DataRepositoryConfigurationUnion = Union[S3DataRepositoryConfiguration, S3DataRepositoryConfigurationOutput]


# This class is the input for the 'delete_file_system' function.
class DeleteFileSystemRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    WindowsConfiguration: Optional[DeleteFileSystemWindowsConfiguration] = None
    LustreConfiguration: Optional[DeleteFileSystemLustreConfiguration] = None
    OpenZFSConfiguration: Optional[DeleteFileSystemOpenZFSConfiguration] = None


# This class is the output for the 'delete_file_system' function.
class DeleteFileSystemResponse(BaseValidatorModel):
    FileSystemId: str
    Lifecycle: FileSystemLifecycleType
    WindowsResponse: DeleteFileSystemWindowsResponse
    LustreResponse: DeleteFileSystemLustreResponse
    OpenZFSResponse: DeleteFileSystemOpenZFSResponse
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'delete_volume' function.
class DeleteVolumeRequest(BaseValidatorModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[DeleteVolumeOntapConfiguration] = None
    OpenZFSConfiguration: Optional[DeleteVolumeOpenZFSConfiguration] = None


# This class is the output for the 'delete_volume' function.
class DeleteVolumeResponse(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    OntapResponse: DeleteVolumeOntapResponse
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_storage_virtual_machine' function.
class CreateStorageVirtualMachineRequest(BaseValidatorModel):
    FileSystemId: str
    Name: str
    ActiveDirectoryConfiguration: Optional[CreateSvmActiveDirectoryConfiguration] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    RootVolumeSecurityStyle: Optional[StorageVirtualMachineRootVolumeSecurityStyleType] = None


class LustreFileSystemConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DataRepositoryConfiguration: Optional[DataRepositoryConfiguration] = None
    DeploymentType: Optional[LustreDeploymentTypeType] = None
    PerUnitStorageThroughput: Optional[int] = None
    MountName: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    DriveCacheType: Optional[DriveCacheTypeType] = None
    DataCompressionType: Optional[DataCompressionTypeType] = None
    LogConfiguration: Optional[LustreLogConfiguration] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationOutput] = None
    MetadataConfiguration: Optional[FileSystemLustreMetadataConfiguration] = None
    EfaEnabled: Optional[bool] = None


# This class is the input for the 'create_data_repository_task' function.
class CreateDataRepositoryTaskRequest(BaseValidatorModel):
    Type: DataRepositoryTaskTypeType
    FileSystemId: str
    Report: CompletionReport
    Paths: Optional[List[str]] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CapacityToRelease: Optional[int] = None
    ReleaseConfiguration: Optional[ReleaseConfiguration] = None


class DataRepositoryTask(BaseValidatorModel):
    TaskId: str
    Lifecycle: DataRepositoryTaskLifecycleType
    Type: DataRepositoryTaskTypeType
    CreationTime: datetime
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    FileSystemId: Optional[str] = None
    Paths: Optional[List[str]] = None
    FailureDetails: Optional[DataRepositoryTaskFailureDetails] = None
    Status: Optional[DataRepositoryTaskStatus] = None
    Report: Optional[CompletionReport] = None
    CapacityToRelease: Optional[int] = None
    FileCacheId: Optional[str] = None
    ReleaseConfiguration: Optional[ReleaseConfiguration] = None


# This class is the input for the 'create_file_cache' function.
class CreateFileCacheRequest(BaseValidatorModel):
    FileCacheType: Literal['LUSTRE']
    FileCacheTypeVersion: str
    StorageCapacity: int
    SubnetIds: List[str]
    ClientRequestToken: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    CopyTagsToDataRepositoryAssociations: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    LustreConfiguration: Optional[CreateFileCacheLustreConfiguration] = None
    DataRepositoryAssociations: Optional[List[FileCacheDataRepositoryAssociation]] = None


class FileCacheCreating(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCacheType: Optional[Literal['LUSTRE']] = None
    FileCacheTypeVersion: Optional[str] = None
    Lifecycle: Optional[FileCacheLifecycleType] = None
    FailureDetails: Optional[FileCacheFailureDetails] = None
    StorageCapacity: Optional[int] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CopyTagsToDataRepositoryAssociations: Optional[bool] = None
    LustreConfiguration: Optional[FileCacheLustreConfiguration] = None
    DataRepositoryAssociationIds: Optional[List[str]] = None


class FileCache(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCacheType: Optional[Literal['LUSTRE']] = None
    FileCacheTypeVersion: Optional[str] = None
    Lifecycle: Optional[FileCacheLifecycleType] = None
    FailureDetails: Optional[FileCacheFailureDetails] = None
    StorageCapacity: Optional[int] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    LustreConfiguration: Optional[FileCacheLustreConfiguration] = None
    DataRepositoryAssociationIds: Optional[List[str]] = None


class OntapFileSystemConfiguration(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    DeploymentType: Optional[OntapDeploymentTypeType] = None
    EndpointIpAddressRange: Optional[str] = None
    Endpoints: Optional[FileSystemEndpoints] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None
    PreferredSubnetId: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    FsxAdminPassword: Optional[str] = None
    HAPairs: Optional[int] = None
    ThroughputCapacityPerHAPair: Optional[int] = None


# This class is the output for the 'create_snapshot' function.
class CreateSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshots' function.
class DescribeSnapshotsResponse(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_snapshot' function.
class UpdateSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CreateFileSystemLustreConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    ImportPath: Optional[str] = None
    ExportPath: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    DeploymentType: Optional[LustreDeploymentTypeType] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    PerUnitStorageThroughput: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    DriveCacheType: Optional[DriveCacheTypeType] = None
    DataCompressionType: Optional[DataCompressionTypeType] = None
    EfaEnabled: Optional[bool] = None
    LogConfiguration: Optional[LustreLogCreateConfiguration] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationUnion] = None
    MetadataConfiguration: Optional[CreateFileSystemLustreMetadataConfiguration] = None


class UpdateFileSystemLustreConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    DataCompressionType: Optional[DataCompressionTypeType] = None
    LogConfiguration: Optional[LustreLogCreateConfiguration] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationUnion] = None
    PerUnitStorageThroughput: Optional[int] = None
    MetadataConfiguration: Optional[UpdateFileSystemLustreMetadataConfiguration] = None


class OpenZFSVolumeConfiguration(BaseValidatorModel):
    ParentVolumeId: Optional[str] = None
    VolumePath: Optional[str] = None
    StorageCapacityReservationGiB: Optional[int] = None
    StorageCapacityQuotaGiB: Optional[int] = None
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    CopyTagsToSnapshots: Optional[bool] = None
    OriginSnapshot: Optional[OpenZFSOriginSnapshotConfiguration] = None
    ReadOnly: Optional[bool] = None
    NfsExports: Optional[List[OpenZFSNfsExportOutput]] = None
    UserAndGroupQuotas: Optional[List[OpenZFSUserOrGroupQuota]] = None
    RestoreToSnapshot: Optional[str] = None
    DeleteIntermediateSnaphots: Optional[bool] = None
    DeleteClonedVolumes: Optional[bool] = None
    DeleteIntermediateData: Optional[bool] = None
    SourceSnapshotARN: Optional[str] = None
    DestinationSnapshot: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None


class OpenZFSNfsExport(BaseValidatorModel):
    ClientConfigurations: List[OpenZFSClientConfigurationUnion]


class CreateSnaplockConfiguration(BaseValidatorModel):
    SnaplockType: SnaplockTypeType
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriod] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriod] = None
    VolumeAppendModeEnabled: Optional[bool] = None


class SnaplockConfiguration(BaseValidatorModel):
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriod] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriod] = None
    SnaplockType: Optional[SnaplockTypeType] = None
    VolumeAppendModeEnabled: Optional[bool] = None


class UpdateSnaplockConfiguration(BaseValidatorModel):
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriod] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriod] = None
    VolumeAppendModeEnabled: Optional[bool] = None


# This class is the input for the 'update_storage_virtual_machine' function.
class UpdateStorageVirtualMachineRequest(BaseValidatorModel):
    StorageVirtualMachineId: str
    ActiveDirectoryConfiguration: Optional[UpdateSvmActiveDirectoryConfiguration] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None


class StorageVirtualMachine(BaseValidatorModel):
    ActiveDirectoryConfiguration: Optional[SvmActiveDirectoryConfiguration] = None
    CreationTime: Optional[datetime] = None
    Endpoints: Optional[SvmEndpoints] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[StorageVirtualMachineLifecycleType] = None
    Name: Optional[str] = None
    ResourceARN: Optional[str] = None
    StorageVirtualMachineId: Optional[str] = None
    Subtype: Optional[StorageVirtualMachineSubtypeType] = None
    UUID: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReason] = None
    RootVolumeSecurityStyle: Optional[StorageVirtualMachineRootVolumeSecurityStyleType] = None


# This class is the output for the 'create_data_repository_association' function.
class CreateDataRepositoryAssociationResponse(BaseValidatorModel):
    Association: DataRepositoryAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_repository_associations' function.
class DescribeDataRepositoryAssociationsResponse(BaseValidatorModel):
    Associations: List[DataRepositoryAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_data_repository_association' function.
class UpdateDataRepositoryAssociationResponse(BaseValidatorModel):
    Association: DataRepositoryAssociation
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_data_repository_association' function.
class CreateDataRepositoryAssociationRequest(BaseValidatorModel):
    FileSystemId: str
    DataRepositoryPath: str
    FileSystemPath: Optional[str] = None
    BatchImportMetaDataOnCreate: Optional[bool] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationUnion] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_data_repository_association' function.
class UpdateDataRepositoryAssociationRequest(BaseValidatorModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationUnion] = None


# This class is the output for the 'create_data_repository_task' function.
class CreateDataRepositoryTaskResponse(BaseValidatorModel):
    DataRepositoryTask: DataRepositoryTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_repository_tasks' function.
class DescribeDataRepositoryTasksResponse(BaseValidatorModel):
    DataRepositoryTasks: List[DataRepositoryTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_file_cache' function.
class CreateFileCacheResponse(BaseValidatorModel):
    FileCache: FileCacheCreating
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_file_caches' function.
class DescribeFileCachesResponse(BaseValidatorModel):
    FileCaches: List[FileCache]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_file_cache' function.
class UpdateFileCacheResponse(BaseValidatorModel):
    FileCache: FileCache
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_file_system' function.
class UpdateFileSystemRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    StorageCapacity: Optional[int] = None
    WindowsConfiguration: Optional[UpdateFileSystemWindowsConfiguration] = None
    LustreConfiguration: Optional[UpdateFileSystemLustreConfiguration] = None
    OntapConfiguration: Optional[UpdateFileSystemOntapConfiguration] = None
    OpenZFSConfiguration: Optional[UpdateFileSystemOpenZFSConfiguration] = None
    StorageType: Optional[StorageTypeType] = None
    FileSystemTypeVersion: Optional[str] = None

OpenZFSNfsExportUnion = Union[OpenZFSNfsExport, OpenZFSNfsExportOutput]


class CreateOntapVolumeConfiguration(BaseValidatorModel):
    StorageVirtualMachineId: str
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicy] = None
    OntapVolumeType: Optional[InputOntapVolumeTypeType] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[CreateSnaplockConfiguration] = None
    VolumeStyle: Optional[VolumeStyleType] = None
    AggregateConfiguration: Optional[CreateAggregateConfiguration] = None
    SizeInBytes: Optional[int] = None


class OntapVolumeConfiguration(BaseValidatorModel):
    FlexCacheEndpointType: Optional[FlexCacheEndpointTypeType] = None
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    StorageVirtualMachineId: Optional[str] = None
    StorageVirtualMachineRoot: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicy] = None
    UUID: Optional[str] = None
    OntapVolumeType: Optional[OntapVolumeTypeType] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[SnaplockConfiguration] = None
    VolumeStyle: Optional[VolumeStyleType] = None
    AggregateConfiguration: Optional[AggregateConfiguration] = None
    SizeInBytes: Optional[int] = None


class UpdateOntapVolumeConfiguration(BaseValidatorModel):
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicy] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[UpdateSnaplockConfiguration] = None
    SizeInBytes: Optional[int] = None


# This class is the output for the 'create_storage_virtual_machine' function.
class CreateStorageVirtualMachineResponse(BaseValidatorModel):
    StorageVirtualMachine: StorageVirtualMachine
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_storage_virtual_machines' function.
class DescribeStorageVirtualMachinesResponse(BaseValidatorModel):
    StorageVirtualMachines: List[StorageVirtualMachine]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_storage_virtual_machine' function.
class UpdateStorageVirtualMachineResponse(BaseValidatorModel):
    StorageVirtualMachine: StorageVirtualMachine
    ResponseMetadata: ResponseMetadata


class CreateOpenZFSVolumeConfiguration(BaseValidatorModel):
    ParentVolumeId: str
    StorageCapacityReservationGiB: Optional[int] = None
    StorageCapacityQuotaGiB: Optional[int] = None
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    CopyTagsToSnapshots: Optional[bool] = None
    OriginSnapshot: Optional[CreateOpenZFSOriginSnapshotConfiguration] = None
    ReadOnly: Optional[bool] = None
    NfsExports: Optional[List[OpenZFSNfsExportUnion]] = None
    UserAndGroupQuotas: Optional[List[OpenZFSUserOrGroupQuota]] = None


class OpenZFSCreateRootVolumeConfiguration(BaseValidatorModel):
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    NfsExports: Optional[List[OpenZFSNfsExportUnion]] = None
    UserAndGroupQuotas: Optional[List[OpenZFSUserOrGroupQuota]] = None
    CopyTagsToSnapshots: Optional[bool] = None
    ReadOnly: Optional[bool] = None


class UpdateOpenZFSVolumeConfiguration(BaseValidatorModel):
    StorageCapacityReservationGiB: Optional[int] = None
    StorageCapacityQuotaGiB: Optional[int] = None
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    NfsExports: Optional[List[OpenZFSNfsExportUnion]] = None
    UserAndGroupQuotas: Optional[List[OpenZFSUserOrGroupQuota]] = None
    ReadOnly: Optional[bool] = None


# This class is the input for the 'create_volume_from_backup' function.
class CreateVolumeFromBackupRequest(BaseValidatorModel):
    BackupId: str
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfiguration] = None
    Tags: Optional[List[Tag]] = None


class VolumePaginator(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[VolumeLifecycleType] = None
    Name: Optional[str] = None
    OntapConfiguration: Optional[OntapVolumeConfiguration] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReason] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None
    OpenZFSConfiguration: Optional[OpenZFSVolumeConfiguration] = None


class Volume(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[VolumeLifecycleType] = None
    Name: Optional[str] = None
    OntapConfiguration: Optional[OntapVolumeConfiguration] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReason] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None
    OpenZFSConfiguration: Optional[OpenZFSVolumeConfiguration] = None


# This class is the input for the 'create_volume' function.
class CreateVolumeRequest(BaseValidatorModel):
    VolumeType: VolumeTypeType
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfiguration] = None
    Tags: Optional[List[Tag]] = None
    OpenZFSConfiguration: Optional[CreateOpenZFSVolumeConfiguration] = None


class CreateFileSystemOpenZFSConfiguration(BaseValidatorModel):
    DeploymentType: OpenZFSDeploymentTypeType
    ThroughputCapacity: int
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None
    RootVolumeConfiguration: Optional[OpenZFSCreateRootVolumeConfiguration] = None
    PreferredSubnetId: Optional[str] = None
    EndpointIpAddressRange: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfiguration] = None


# This class is the input for the 'update_volume' function.
class UpdateVolumeRequest(BaseValidatorModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[UpdateOntapVolumeConfiguration] = None
    Name: Optional[str] = None
    OpenZFSConfiguration: Optional[UpdateOpenZFSVolumeConfiguration] = None


class AdministrativeActionPaginator(BaseValidatorModel):
    AdministrativeActionType: Optional[AdministrativeActionTypeType] = None
    ProgressPercent: Optional[int] = None
    RequestTime: Optional[datetime] = None
    Status: Optional[StatusType] = None
    TargetFileSystemValues: Optional[Dict[str, Any]] = None
    FailureDetails: Optional[AdministrativeActionFailureDetails] = None
    TargetVolumeValues: Optional[VolumePaginator] = None
    TargetSnapshotValues: Optional[SnapshotPaginator] = None
    TotalTransferBytes: Optional[int] = None
    RemainingTransferBytes: Optional[int] = None


class DescribeVolumesResponsePaginator(BaseValidatorModel):
    Volumes: List[VolumePaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AdministrativeAction(BaseValidatorModel):
    AdministrativeActionType: Optional[AdministrativeActionTypeType] = None
    ProgressPercent: Optional[int] = None
    RequestTime: Optional[datetime] = None
    Status: Optional[StatusType] = None
    TargetFileSystemValues: Optional[Dict[str, Any]] = None
    FailureDetails: Optional[AdministrativeActionFailureDetails] = None
    TargetVolumeValues: Optional[Volume] = None
    TargetSnapshotValues: Optional[Snapshot] = None
    TotalTransferBytes: Optional[int] = None
    RemainingTransferBytes: Optional[int] = None


# This class is the output for the 'create_volume_from_backup' function.
class CreateVolumeFromBackupResponse(BaseValidatorModel):
    Volume: Volume
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_volume' function.
class CreateVolumeResponse(BaseValidatorModel):
    Volume: Volume
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_volumes' function.
class DescribeVolumesResponse(BaseValidatorModel):
    Volumes: List[Volume]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_volume' function.
class UpdateVolumeResponse(BaseValidatorModel):
    Volume: Volume
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_file_system_from_backup' function.
class CreateFileSystemFromBackupRequest(BaseValidatorModel):
    BackupId: str
    SubnetIds: List[str]
    ClientRequestToken: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    WindowsConfiguration: Optional[CreateFileSystemWindowsConfiguration] = None
    LustreConfiguration: Optional[CreateFileSystemLustreConfiguration] = None
    StorageType: Optional[StorageTypeType] = None
    KmsKeyId: Optional[str] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[CreateFileSystemOpenZFSConfiguration] = None
    StorageCapacity: Optional[int] = None


# This class is the input for the 'create_file_system' function.
class CreateFileSystemRequest(BaseValidatorModel):
    FileSystemType: FileSystemTypeType
    SubnetIds: List[str]
    ClientRequestToken: Optional[str] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    WindowsConfiguration: Optional[CreateFileSystemWindowsConfiguration] = None
    LustreConfiguration: Optional[CreateFileSystemLustreConfiguration] = None
    OntapConfiguration: Optional[CreateFileSystemOntapConfiguration] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[CreateFileSystemOpenZFSConfiguration] = None


class FileSystemPaginator(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    FileSystemType: Optional[FileSystemTypeType] = None
    Lifecycle: Optional[FileSystemLifecycleType] = None
    FailureDetails: Optional[FileSystemFailureDetails] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    WindowsConfiguration: Optional[WindowsFileSystemConfiguration] = None
    LustreConfiguration: Optional[LustreFileSystemConfiguration] = None
    AdministrativeActions: Optional[List[AdministrativeActionPaginator]] = None
    OntapConfiguration: Optional[OntapFileSystemConfiguration] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[OpenZFSFileSystemConfiguration] = None


# This class is the output for the 'copy_snapshot_and_update_volume' function.
class CopySnapshotAndUpdateVolumeResponse(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeAction]
    ResponseMetadata: ResponseMetadata


class FileSystem(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    FileSystemType: Optional[FileSystemTypeType] = None
    Lifecycle: Optional[FileSystemLifecycleType] = None
    FailureDetails: Optional[FileSystemFailureDetails] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    WindowsConfiguration: Optional[WindowsFileSystemConfiguration] = None
    LustreConfiguration: Optional[LustreFileSystemConfiguration] = None
    AdministrativeActions: Optional[List[AdministrativeAction]] = None
    OntapConfiguration: Optional[OntapFileSystemConfiguration] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[OpenZFSFileSystemConfiguration] = None


# This class is the output for the 'restore_volume_from_snapshot' function.
class RestoreVolumeFromSnapshotResponse(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeAction]
    ResponseMetadata: ResponseMetadata


class BackupPaginator(BaseValidatorModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    Type: BackupTypeType
    CreationTime: datetime
    FileSystem: FileSystemPaginator
    FailureDetails: Optional[BackupFailureDetails] = None
    ProgressPercent: Optional[int] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DirectoryInformation: Optional[ActiveDirectoryBackupAttributes] = None
    OwnerId: Optional[str] = None
    SourceBackupId: Optional[str] = None
    SourceBackupRegion: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    Volume: Optional[VolumePaginator] = None
    SizeInBytes: Optional[int] = None


class DescribeFileSystemsResponsePaginator(BaseValidatorModel):
    FileSystems: List[FileSystemPaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Backup(BaseValidatorModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    Type: BackupTypeType
    CreationTime: datetime
    FileSystem: FileSystem
    FailureDetails: Optional[BackupFailureDetails] = None
    ProgressPercent: Optional[int] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DirectoryInformation: Optional[ActiveDirectoryBackupAttributes] = None
    OwnerId: Optional[str] = None
    SourceBackupId: Optional[str] = None
    SourceBackupRegion: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    Volume: Optional[Volume] = None
    SizeInBytes: Optional[int] = None


# This class is the output for the 'create_file_system_from_backup' function.
class CreateFileSystemFromBackupResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_file_system' function.
class CreateFileSystemResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_file_systems' function.
class DescribeFileSystemsResponse(BaseValidatorModel):
    FileSystems: List[FileSystem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'release_file_system_nfs_v3_locks' function.
class ReleaseFileSystemNfsV3LocksResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_misconfigured_state_recovery' function.
class StartMisconfiguredStateRecoveryResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_file_system' function.
class UpdateFileSystemResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


class DescribeBackupsResponsePaginator(BaseValidatorModel):
    Backups: List[BackupPaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'copy_backup' function.
class CopyBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backup' function.
class CreateBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_backups' function.
class DescribeBackupsResponse(BaseValidatorModel):
    Backups: List[Backup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None