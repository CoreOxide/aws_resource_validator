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
from aws_resource_validator.pydantic_models.fsx_constants import *

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


class AssociateFileSystemAliasesRequest(BaseValidatorModel):
    FileSystemId: str
    Aliases: Sequence[str]
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
    Events: Optional[Sequence[EventTypeType]] = None


class AutoImportPolicyOutput(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutoImportPolicy(BaseValidatorModel):
    Events: Optional[Sequence[EventTypeType]] = None


class BackupFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CancelDataRepositoryTaskRequest(BaseValidatorModel):
    TaskId: str


class CompletionReport(BaseValidatorModel):
    Enabled: bool
    Path: Optional[str] = None
    Format: Optional[Literal["REPORT_CSV_20191124"]] = None
    Scope: Optional[Literal["FAILED_FILES_ONLY"]] = None


class CopySnapshotAndUpdateVolumeRequest(BaseValidatorModel):
    VolumeId: str
    SourceSnapshotARN: str
    ClientRequestToken: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None
    Options: Optional[Sequence[UpdateOpenZFSVolumeOptionType]] = None


class CreateAggregateConfiguration(BaseValidatorModel):
    Aggregates: Optional[Sequence[str]] = None
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
    DnsIps: Sequence[str]
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


class DataRepositoryFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class DataRepositoryTaskFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class DataRepositoryTaskFilter(BaseValidatorModel):
    Name: Optional[DataRepositoryTaskFilterNameType] = None
    Values: Optional[Sequence[str]] = None


class DataRepositoryTaskStatus(BaseValidatorModel):
    TotalCount: Optional[int] = None
    SucceededCount: Optional[int] = None
    FailedCount: Optional[int] = None
    LastUpdatedTime: Optional[datetime] = None
    ReleasedCapacity: Optional[int] = None


class DeleteBackupRequest(BaseValidatorModel):
    BackupId: str
    ClientRequestToken: Optional[str] = None


class DeleteDataRepositoryAssociationRequest(BaseValidatorModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    DeleteDataInFileSystem: Optional[bool] = None


class DeleteFileCacheRequest(BaseValidatorModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None


class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    ClientRequestToken: Optional[str] = None


class DeleteStorageVirtualMachineRequest(BaseValidatorModel):
    StorageVirtualMachineId: str
    ClientRequestToken: Optional[str] = None


class DeleteVolumeOpenZFSConfiguration(BaseValidatorModel):
    Options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = None


class Filter(BaseValidatorModel):
    Name: Optional[FilterNameType] = None
    Values: Optional[Sequence[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeFileCachesRequest(BaseValidatorModel):
    FileCacheIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFileSystemAliasesRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFileSystemsRequest(BaseValidatorModel):
    FileSystemIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SnapshotFilter(BaseValidatorModel):
    Name: Optional[SnapshotFilterNameType] = None
    Values: Optional[Sequence[str]] = None


class StorageVirtualMachineFilter(BaseValidatorModel):
    Name: Optional[Literal["file-system-id"]] = None
    Values: Optional[Sequence[str]] = None


class VolumeFilter(BaseValidatorModel):
    Name: Optional[VolumeFilterNameType] = None
    Values: Optional[Sequence[str]] = None


class DisassociateFileSystemAliasesRequest(BaseValidatorModel):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: Optional[str] = None


class DurationSinceLastAccess(BaseValidatorModel):
    Unit: Optional[Literal["DAYS"]] = None
    Value: Optional[int] = None


class FileCacheFailureDetails(BaseValidatorModel):
    Message: Optional[str] = None


class FileCacheNFSConfiguration(BaseValidatorModel):
    Version: Literal["NFS3"]
    DnsIps: Optional[Sequence[str]] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LustreRootSquashConfigurationOutput(BaseValidatorModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[List[str]] = None


class LustreRootSquashConfiguration(BaseValidatorModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[Sequence[str]] = None


class OpenZFSClientConfigurationOutput(BaseValidatorModel):
    Clients: str
    Options: List[str]


class OpenZFSClientConfiguration(BaseValidatorModel):
    Clients: str
    Options: Sequence[str]


class OpenZFSOriginSnapshotConfiguration(BaseValidatorModel):
    SnapshotARN: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None


class ReleaseFileSystemNfsV3LocksRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None


class RestoreVolumeFromSnapshotRequest(BaseValidatorModel):
    VolumeId: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None
    Options: Optional[Sequence[RestoreOpenZFSVolumeOptionType]] = None


class SelfManagedActiveDirectoryAttributes(BaseValidatorModel):
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None
    UserName: Optional[str] = None
    DnsIps: Optional[List[str]] = None


class SelfManagedActiveDirectoryConfigurationUpdates(BaseValidatorModel):
    UserName: Optional[str] = None
    Password: Optional[str] = None
    DnsIps: Optional[Sequence[str]] = None
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None


class StartMisconfiguredStateRecoveryRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None


class SvmEndpoint(BaseValidatorModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateFileCacheLustreConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None


class UpdateFileSystemLustreMetadataConfiguration(BaseValidatorModel):
    Iops: Optional[int] = None
    Mode: Optional[MetadataConfigurationModeType] = None


class UpdateSharedVpcConfigurationRequest(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: Optional[str] = None
    ClientRequestToken: Optional[str] = None


class UpdateSnapshotRequest(BaseValidatorModel):
    Name: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None


class WindowsAuditLogConfiguration(BaseValidatorModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None


class AssociateFileSystemAliasesResponse(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata


class CancelDataRepositoryTaskResponse(BaseValidatorModel):
    Lifecycle: DataRepositoryTaskLifecycleType
    TaskId: str
    ResponseMetadata: ResponseMetadata


class DeleteBackupResponse(BaseValidatorModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    ResponseMetadata: ResponseMetadata


class DeleteDataRepositoryAssociationResponse(BaseValidatorModel):
    AssociationId: str
    Lifecycle: DataRepositoryLifecycleType
    DeleteDataInFileSystem: bool
    ResponseMetadata: ResponseMetadata


class DeleteFileCacheResponse(BaseValidatorModel):
    FileCacheId: str
    Lifecycle: FileCacheLifecycleType
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotResponse(BaseValidatorModel):
    SnapshotId: str
    Lifecycle: SnapshotLifecycleType
    ResponseMetadata: ResponseMetadata


class DeleteStorageVirtualMachineResponse(BaseValidatorModel):
    StorageVirtualMachineId: str
    Lifecycle: StorageVirtualMachineLifecycleType
    ResponseMetadata: ResponseMetadata


class DescribeFileSystemAliasesResponse(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSharedVpcConfigurationResponse(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadata


class DisassociateFileSystemAliasesResponse(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata


class UpdateSharedVpcConfigurationResponse(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadata


class NFSDataRepositoryConfiguration(BaseValidatorModel):
    Version: Literal["NFS3"]
    DnsIps: Optional[List[str]] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutput] = None


class S3DataRepositoryConfigurationOutput(BaseValidatorModel):
    AutoImportPolicy: Optional[AutoImportPolicyOutput] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutput] = None


class S3DataRepositoryConfiguration(BaseValidatorModel):
    AutoImportPolicy: Optional[AutoImportPolicy] = None
    AutoExportPolicy: Optional[AutoExportPolicy] = None


class CopyBackupRequest(BaseValidatorModel):
    SourceBackupId: str
    ClientRequestToken: Optional[str] = None
    SourceRegion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateBackupRequest(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    VolumeId: Optional[str] = None


class CreateSnapshotRequest(BaseValidatorModel):
    Name: str
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class DeleteFileSystemLustreConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[Tag]] = None


class DeleteFileSystemLustreResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteFileSystemOpenZFSConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[Tag]] = None
    Options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = None


class DeleteFileSystemOpenZFSResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteFileSystemWindowsConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[Tag]] = None


class DeleteFileSystemWindowsResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class DeleteVolumeOntapConfiguration(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[Tag]] = None
    BypassSnaplockEnterpriseRetention: Optional[bool] = None


class DeleteVolumeOntapResponse(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateFileCacheLustreConfiguration(BaseValidatorModel):
    PerUnitStorageThroughput: int
    DeploymentType: Literal["CACHE_1"]
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
    RouteTableIds: Optional[Sequence[str]] = None
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
    AddRouteTableIds: Optional[Sequence[str]] = None
    RemoveRouteTableIds: Optional[Sequence[str]] = None
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
    AddRouteTableIds: Optional[Sequence[str]] = None
    RemoveRouteTableIds: Optional[Sequence[str]] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfiguration] = None


class CreateSvmActiveDirectoryConfiguration(BaseValidatorModel):
    NetBiosName: str
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfiguration ] = None


class CreateFileSystemWindowsConfiguration(BaseValidatorModel):
    ThroughputCapacity: int
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfiguration ] = None
    DeploymentType: Optional[WindowsDeploymentTypeType] = None
    PreferredSubnetId: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    Aliases: Optional[Sequence[str]] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfiguration] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None


class DataRepositoryConfiguration(BaseValidatorModel):
    Lifecycle: Optional[DataRepositoryLifecycleType] = None
    ImportPath: Optional[str] = None
    ExportPath: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    FailureDetails: Optional[DataRepositoryFailureDetails] = None


class DescribeDataRepositoryTasksRequest(BaseValidatorModel):
    TaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[DataRepositoryTaskFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBackupsRequest(BaseValidatorModel):
    BackupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDataRepositoryAssociationsRequest(BaseValidatorModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBackupsRequestPaginate(BaseValidatorModel):
    BackupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFileSystemsRequestPaginate(BaseValidatorModel):
    FileSystemIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotsRequest(BaseValidatorModel):
    SnapshotIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[SnapshotFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeShared: Optional[bool] = None


class DescribeStorageVirtualMachinesRequestPaginate(BaseValidatorModel):
    StorageVirtualMachineIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[StorageVirtualMachineFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStorageVirtualMachinesRequest(BaseValidatorModel):
    StorageVirtualMachineIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[StorageVirtualMachineFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVolumesRequestPaginate(BaseValidatorModel):
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VolumeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeVolumesRequest(BaseValidatorModel):
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VolumeFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReleaseConfiguration(BaseValidatorModel):
    DurationSinceLastAccess: Optional[DurationSinceLastAccess] = None


class FileCacheDataRepositoryAssociation(BaseValidatorModel):
    FileCachePath: str
    DataRepositoryPath: str
    DataRepositorySubdirectories: Optional[Sequence[str]] = None
    NFS: Optional[FileCacheNFSConfiguration] = None


class FileCacheLustreConfiguration(BaseValidatorModel):
    PerUnitStorageThroughput: Optional[int] = None
    DeploymentType: Optional[Literal["CACHE_1"]] = None
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


class OpenZFSNfsExportOutput(BaseValidatorModel):
    ClientConfigurations: List[OpenZFSClientConfigurationOutput]


class RetentionPeriod(BaseValidatorModel):
    pass


class SnaplockRetentionPeriod(BaseValidatorModel):
    DefaultRetention: RetentionPeriod
    MinimumRetention: RetentionPeriod
    MaximumRetention: RetentionPeriod


class SvmActiveDirectoryConfiguration(BaseValidatorModel):
    NetBiosName: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryAttributes ] = None


class UpdateFileSystemWindowsConfiguration(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    ThroughputCapacity: Optional[int] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfigurationUpdates ] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfiguration] = None
    DiskIopsConfiguration: Optional[DiskIopsConfiguration] = None


class UpdateSvmActiveDirectoryConfiguration(BaseValidatorModel):
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfigurationUpdates ] = None
    NetBiosName: Optional[str] = None


class SvmEndpoints(BaseValidatorModel):
    Iscsi: Optional[SvmEndpoint] = None
    Management: Optional[SvmEndpoint] = None
    Nfs: Optional[SvmEndpoint] = None
    Smb: Optional[SvmEndpoint] = None


class UpdateFileCacheRequest(BaseValidatorModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None
    LustreConfiguration: Optional[UpdateFileCacheLustreConfiguration] = None


class WindowsFileSystemConfiguration(BaseValidatorModel):
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryAttributes ] = None
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


class DeleteFileSystemRequest(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    WindowsConfiguration: Optional[DeleteFileSystemWindowsConfiguration] = None
    LustreConfiguration: Optional[DeleteFileSystemLustreConfiguration] = None
    OpenZFSConfiguration: Optional[DeleteFileSystemOpenZFSConfiguration] = None


class DeleteFileSystemResponse(BaseValidatorModel):
    FileSystemId: str
    Lifecycle: FileSystemLifecycleType
    WindowsResponse: DeleteFileSystemWindowsResponse
    LustreResponse: DeleteFileSystemLustreResponse
    OpenZFSResponse: DeleteFileSystemOpenZFSResponse
    ResponseMetadata: ResponseMetadata


class DeleteVolumeRequest(BaseValidatorModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[DeleteVolumeOntapConfiguration] = None
    OpenZFSConfiguration: Optional[DeleteVolumeOpenZFSConfiguration] = None


class DeleteVolumeResponse(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    OntapResponse: DeleteVolumeOntapResponse
    ResponseMetadata: ResponseMetadata


class CreateStorageVirtualMachineRequest(BaseValidatorModel):
    FileSystemId: str
    Name: str
    ActiveDirectoryConfiguration: Optional[CreateSvmActiveDirectoryConfiguration] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
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


class CreateFileCacheRequest(BaseValidatorModel):
    FileCacheType: Literal["LUSTRE"]
    FileCacheTypeVersion: str
    StorageCapacity: int
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    CopyTagsToDataRepositoryAssociations: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    LustreConfiguration: Optional[CreateFileCacheLustreConfiguration] = None
    DataRepositoryAssociations: Optional[Sequence[FileCacheDataRepositoryAssociation]] = None


class FileCacheCreating(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCacheType: Optional[Literal["LUSTRE"]] = None
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
    FileCacheType: Optional[Literal["LUSTRE"]] = None
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


class CreateSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DescribeSnapshotsResponse(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class LustreRootSquashConfigurationUnion(BaseValidatorModel):
    pass


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


class OpenZFSClientConfigurationUnion(BaseValidatorModel):
    pass


class OpenZFSNfsExport(BaseValidatorModel):
    ClientConfigurations: Sequence[OpenZFSClientConfigurationUnion]


class AutocommitPeriod(BaseValidatorModel):
    pass


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


class CreateDataRepositoryAssociationResponse(BaseValidatorModel):
    Association: DataRepositoryAssociation
    ResponseMetadata: ResponseMetadata


class DescribeDataRepositoryAssociationsResponse(BaseValidatorModel):
    Associations: List[DataRepositoryAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateDataRepositoryAssociationResponse(BaseValidatorModel):
    Association: DataRepositoryAssociation
    ResponseMetadata: ResponseMetadata


class S3DataRepositoryConfigurationUnion(BaseValidatorModel):
    pass


class CreateDataRepositoryAssociationRequest(BaseValidatorModel):
    FileSystemId: str
    DataRepositoryPath: str
    FileSystemPath: Optional[str] = None
    BatchImportMetaDataOnCreate: Optional[bool] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationUnion] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class UpdateDataRepositoryAssociationRequest(BaseValidatorModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationUnion] = None


class DataRepositoryTask(BaseValidatorModel):
    pass


class CreateDataRepositoryTaskResponse(BaseValidatorModel):
    DataRepositoryTask: DataRepositoryTask
    ResponseMetadata: ResponseMetadata


class DescribeDataRepositoryTasksResponse(BaseValidatorModel):
    DataRepositoryTasks: List[DataRepositoryTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateFileCacheResponse(BaseValidatorModel):
    FileCache: FileCacheCreating
    ResponseMetadata: ResponseMetadata


class DescribeFileCachesResponse(BaseValidatorModel):
    FileCaches: List[FileCache]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateFileCacheResponse(BaseValidatorModel):
    FileCache: FileCache
    ResponseMetadata: ResponseMetadata


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


class CreateStorageVirtualMachineResponse(BaseValidatorModel):
    StorageVirtualMachine: StorageVirtualMachine
    ResponseMetadata: ResponseMetadata


class DescribeStorageVirtualMachinesResponse(BaseValidatorModel):
    StorageVirtualMachines: List[StorageVirtualMachine]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateStorageVirtualMachineResponse(BaseValidatorModel):
    StorageVirtualMachine: StorageVirtualMachine
    ResponseMetadata: ResponseMetadata


class CreateVolumeFromBackupRequest(BaseValidatorModel):
    BackupId: str
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None


class OpenZFSVolumeConfiguration(BaseValidatorModel):
    pass


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


class CreateOpenZFSVolumeConfiguration(BaseValidatorModel):
    pass


class CreateVolumeRequest(BaseValidatorModel):
    VolumeType: VolumeTypeType
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None
    OpenZFSConfiguration: Optional[CreateOpenZFSVolumeConfiguration] = None


class OpenZFSCreateRootVolumeConfiguration(BaseValidatorModel):
    pass


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
    RouteTableIds: Optional[Sequence[str]] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfiguration] = None


class UpdateOpenZFSVolumeConfiguration(BaseValidatorModel):
    pass


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


class CreateVolumeFromBackupResponse(BaseValidatorModel):
    Volume: Volume
    ResponseMetadata: ResponseMetadata


class CreateVolumeResponse(BaseValidatorModel):
    Volume: Volume
    ResponseMetadata: ResponseMetadata


class DescribeVolumesResponse(BaseValidatorModel):
    Volumes: List[Volume]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateVolumeResponse(BaseValidatorModel):
    Volume: Volume
    ResponseMetadata: ResponseMetadata


class CreateFileSystemFromBackupRequest(BaseValidatorModel):
    BackupId: str
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    WindowsConfiguration: Optional[CreateFileSystemWindowsConfiguration] = None
    LustreConfiguration: Optional[CreateFileSystemLustreConfiguration] = None
    StorageType: Optional[StorageTypeType] = None
    KmsKeyId: Optional[str] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[CreateFileSystemOpenZFSConfiguration] = None
    StorageCapacity: Optional[int] = None


class CreateFileSystemRequest(BaseValidatorModel):
    FileSystemType: FileSystemTypeType
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
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


class RestoreVolumeFromSnapshotResponse(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeAction]
    ResponseMetadata: ResponseMetadata


class DescribeFileSystemsResponsePaginator(BaseValidatorModel):
    FileSystems: List[FileSystemPaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateFileSystemFromBackupResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


class CreateFileSystemResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


class DescribeFileSystemsResponse(BaseValidatorModel):
    FileSystems: List[FileSystem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ReleaseFileSystemNfsV3LocksResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


class StartMisconfiguredStateRecoveryResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


class UpdateFileSystemResponse(BaseValidatorModel):
    FileSystem: FileSystem
    ResponseMetadata: ResponseMetadata


class BackupPaginator(BaseValidatorModel):
    pass


class DescribeBackupsResponsePaginator(BaseValidatorModel):
    Backups: List[BackupPaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Backup(BaseValidatorModel):
    pass


class CopyBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


class CreateBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


class DescribeBackupsResponse(BaseValidatorModel):
    Backups: List[Backup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


