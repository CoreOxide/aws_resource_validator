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

class ActiveDirectoryBackupAttributesTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    ActiveDirectoryId: Optional[str] = None
    ResourceARN: Optional[str] = None


class AdministrativeActionFailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class AggregateConfigurationTypeDef(BaseValidatorModel):
    Aggregates: Optional[List[str]] = None
    TotalConstituents: Optional[int] = None


class AliasTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Lifecycle: Optional[AliasLifecycleType] = None


class AssociateFileSystemAliasesRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AutoExportPolicyOutputTypeDef(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutoExportPolicyTypeDef(BaseValidatorModel):
    Events: Optional[Sequence[EventTypeType]] = None


class AutoImportPolicyOutputTypeDef(BaseValidatorModel):
    Events: Optional[List[EventTypeType]] = None


class AutoImportPolicyTypeDef(BaseValidatorModel):
    Events: Optional[Sequence[EventTypeType]] = None


class BackupFailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CancelDataRepositoryTaskRequestTypeDef(BaseValidatorModel):
    TaskId: str


class CompletionReportTypeDef(BaseValidatorModel):
    Enabled: bool
    Path: Optional[str] = None
    Format: Optional[Literal["REPORT_CSV_20191124"]] = None
    Scope: Optional[Literal["FAILED_FILES_ONLY"]] = None


class CopySnapshotAndUpdateVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    SourceSnapshotARN: str
    ClientRequestToken: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None
    Options: Optional[Sequence[UpdateOpenZFSVolumeOptionType]] = None


class CreateAggregateConfigurationTypeDef(BaseValidatorModel):
    Aggregates: Optional[Sequence[str]] = None
    ConstituentsPerAggregate: Optional[int] = None


class FileCacheLustreMetadataConfigurationTypeDef(BaseValidatorModel):
    StorageCapacity: int


class CreateFileSystemLustreMetadataConfigurationTypeDef(BaseValidatorModel):
    Mode: MetadataConfigurationModeType
    Iops: Optional[int] = None


class LustreLogCreateConfigurationTypeDef(BaseValidatorModel):
    Level: LustreAccessAuditLogLevelType
    Destination: Optional[str] = None


class DiskIopsConfigurationTypeDef(BaseValidatorModel):
    Mode: Optional[DiskIopsConfigurationModeType] = None
    Iops: Optional[int] = None


class OpenZFSReadCacheConfigurationTypeDef(BaseValidatorModel):
    SizingMode: Optional[OpenZFSReadCacheSizingModeType] = None
    SizeGiB: Optional[int] = None


class SelfManagedActiveDirectoryConfigurationTypeDef(BaseValidatorModel):
    DomainName: str
    UserName: str
    Password: str
    DnsIps: Sequence[str]
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None


class WindowsAuditLogCreateConfigurationTypeDef(BaseValidatorModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None


class TieringPolicyTypeDef(BaseValidatorModel):
    CoolingPeriod: Optional[int] = None
    Name: Optional[TieringPolicyNameType] = None


class CreateOpenZFSOriginSnapshotConfigurationTypeDef(BaseValidatorModel):
    SnapshotARN: str
    CopyStrategy: OpenZFSCopyStrategyType


class DataRepositoryFailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class DataRepositoryTaskFailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class DataRepositoryTaskFilterTypeDef(BaseValidatorModel):
    Name: Optional[DataRepositoryTaskFilterNameType] = None
    Values: Optional[Sequence[str]] = None


class DataRepositoryTaskStatusTypeDef(BaseValidatorModel):
    TotalCount: Optional[int] = None
    SucceededCount: Optional[int] = None
    FailedCount: Optional[int] = None
    LastUpdatedTime: Optional[datetime] = None
    ReleasedCapacity: Optional[int] = None


class DeleteBackupRequestTypeDef(BaseValidatorModel):
    BackupId: str
    ClientRequestToken: Optional[str] = None


class DeleteDataRepositoryAssociationRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    DeleteDataInFileSystem: Optional[bool] = None


class DeleteFileCacheRequestTypeDef(BaseValidatorModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None


class DeleteSnapshotRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    ClientRequestToken: Optional[str] = None


class DeleteStorageVirtualMachineRequestTypeDef(BaseValidatorModel):
    StorageVirtualMachineId: str
    ClientRequestToken: Optional[str] = None


class DeleteVolumeOpenZFSConfigurationTypeDef(BaseValidatorModel):
    Options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = None


class FilterTypeDef(BaseValidatorModel):
    Name: Optional[FilterNameType] = None
    Values: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeFileCachesRequestTypeDef(BaseValidatorModel):
    FileCacheIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFileSystemAliasesRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFileSystemsRequestTypeDef(BaseValidatorModel):
    FileSystemIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SnapshotFilterTypeDef(BaseValidatorModel):
    Name: Optional[SnapshotFilterNameType] = None
    Values: Optional[Sequence[str]] = None


class StorageVirtualMachineFilterTypeDef(BaseValidatorModel):
    Name: Optional[Literal["file-system-id"]] = None
    Values: Optional[Sequence[str]] = None


class VolumeFilterTypeDef(BaseValidatorModel):
    Name: Optional[VolumeFilterNameType] = None
    Values: Optional[Sequence[str]] = None


class DisassociateFileSystemAliasesRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: Optional[str] = None


class DurationSinceLastAccessTypeDef(BaseValidatorModel):
    Unit: Optional[Literal["DAYS"]] = None
    Value: Optional[int] = None


class FileCacheFailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class FileCacheNFSConfigurationTypeDef(BaseValidatorModel):
    Version: Literal["NFS3"]
    DnsIps: Optional[Sequence[str]] = None


class LustreLogConfigurationTypeDef(BaseValidatorModel):
    Level: LustreAccessAuditLogLevelType
    Destination: Optional[str] = None


class FileSystemEndpointTypeDef(BaseValidatorModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None


class FileSystemFailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class FileSystemLustreMetadataConfigurationTypeDef(BaseValidatorModel):
    Mode: MetadataConfigurationModeType
    Iops: Optional[int] = None


class LifecycleTransitionReasonTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LustreRootSquashConfigurationOutputTypeDef(BaseValidatorModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[List[str]] = None


class LustreRootSquashConfigurationTypeDef(BaseValidatorModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[Sequence[str]] = None


class OpenZFSClientConfigurationOutputTypeDef(BaseValidatorModel):
    Clients: str
    Options: List[str]


class OpenZFSClientConfigurationTypeDef(BaseValidatorModel):
    Clients: str
    Options: Sequence[str]


class OpenZFSOriginSnapshotConfigurationTypeDef(BaseValidatorModel):
    SnapshotARN: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None


class ReleaseFileSystemNfsV3LocksRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None


class RestoreVolumeFromSnapshotRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None
    Options: Optional[Sequence[RestoreOpenZFSVolumeOptionType]] = None


class SelfManagedActiveDirectoryAttributesTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None
    UserName: Optional[str] = None
    DnsIps: Optional[List[str]] = None


class SelfManagedActiveDirectoryConfigurationUpdatesTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Password: Optional[str] = None
    DnsIps: Optional[Sequence[str]] = None
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None


class StartMisconfiguredStateRecoveryRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None


class SvmEndpointTypeDef(BaseValidatorModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateFileCacheLustreConfigurationTypeDef(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None


class UpdateFileSystemLustreMetadataConfigurationTypeDef(BaseValidatorModel):
    Iops: Optional[int] = None
    Mode: Optional[MetadataConfigurationModeType] = None


class UpdateSharedVpcConfigurationRequestTypeDef(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: Optional[str] = None
    ClientRequestToken: Optional[str] = None


class UpdateSnapshotRequestTypeDef(BaseValidatorModel):
    Name: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None


class WindowsAuditLogConfigurationTypeDef(BaseValidatorModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None


class AssociateFileSystemAliasesResponseTypeDef(BaseValidatorModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CancelDataRepositoryTaskResponseTypeDef(BaseValidatorModel):
    Lifecycle: DataRepositoryTaskLifecycleType
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBackupResponseTypeDef(BaseValidatorModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataRepositoryAssociationResponseTypeDef(BaseValidatorModel):
    AssociationId: str
    Lifecycle: DataRepositoryLifecycleType
    DeleteDataInFileSystem: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFileCacheResponseTypeDef(BaseValidatorModel):
    FileCacheId: str
    Lifecycle: FileCacheLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSnapshotResponseTypeDef(BaseValidatorModel):
    SnapshotId: str
    Lifecycle: SnapshotLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteStorageVirtualMachineResponseTypeDef(BaseValidatorModel):
    StorageVirtualMachineId: str
    Lifecycle: StorageVirtualMachineLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFileSystemAliasesResponseTypeDef(BaseValidatorModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeSharedVpcConfigurationResponseTypeDef(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateFileSystemAliasesResponseTypeDef(BaseValidatorModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSharedVpcConfigurationResponseTypeDef(BaseValidatorModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadataTypeDef


class NFSDataRepositoryConfigurationTypeDef(BaseValidatorModel):
    Version: Literal["NFS3"]
    DnsIps: Optional[List[str]] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutputTypeDef] = None


class S3DataRepositoryConfigurationOutputTypeDef(BaseValidatorModel):
    AutoImportPolicy: Optional[AutoImportPolicyOutputTypeDef] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutputTypeDef] = None


class S3DataRepositoryConfigurationTypeDef(BaseValidatorModel):
    AutoImportPolicy: Optional[AutoImportPolicyTypeDef] = None
    AutoExportPolicy: Optional[AutoExportPolicyTypeDef] = None


class CopyBackupRequestTypeDef(BaseValidatorModel):
    SourceBackupId: str
    ClientRequestToken: Optional[str] = None
    SourceRegion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateBackupRequestTypeDef(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VolumeId: Optional[str] = None


class CreateSnapshotRequestTypeDef(BaseValidatorModel):
    Name: str
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DeleteFileSystemLustreConfigurationTypeDef(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None


class DeleteFileSystemLustreResponseTypeDef(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None


class DeleteFileSystemOpenZFSConfigurationTypeDef(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None
    Options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = None


class DeleteFileSystemOpenZFSResponseTypeDef(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None


class DeleteFileSystemWindowsConfigurationTypeDef(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None


class DeleteFileSystemWindowsResponseTypeDef(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None


class DeleteVolumeOntapConfigurationTypeDef(BaseValidatorModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None
    BypassSnaplockEnterpriseRetention: Optional[bool] = None


class DeleteVolumeOntapResponseTypeDef(BaseValidatorModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateFileCacheLustreConfigurationTypeDef(BaseValidatorModel):
    PerUnitStorageThroughput: int
    DeploymentType: Literal["CACHE_1"]
    MetadataConfiguration: FileCacheLustreMetadataConfigurationTypeDef
    WeeklyMaintenanceStartTime: Optional[str] = None


class CreateFileSystemOntapConfigurationTypeDef(BaseValidatorModel):
    DeploymentType: OntapDeploymentTypeType
    AutomaticBackupRetentionDays: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    EndpointIpAddressRange: Optional[str] = None
    FsxAdminPassword: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    PreferredSubnetId: Optional[str] = None
    RouteTableIds: Optional[Sequence[str]] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    HAPairs: Optional[int] = None
    ThroughputCapacityPerHAPair: Optional[int] = None


class UpdateFileSystemOntapConfigurationTypeDef(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    FsxAdminPassword: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    ThroughputCapacity: Optional[int] = None
    AddRouteTableIds: Optional[Sequence[str]] = None
    RemoveRouteTableIds: Optional[Sequence[str]] = None
    ThroughputCapacityPerHAPair: Optional[int] = None
    HAPairs: Optional[int] = None


class OpenZFSFileSystemConfigurationTypeDef(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    DeploymentType: Optional[OpenZFSDeploymentTypeType] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    RootVolumeId: Optional[str] = None
    PreferredSubnetId: Optional[str] = None
    EndpointIpAddressRange: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    EndpointIpAddress: Optional[str] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfigurationTypeDef] = None


class UpdateFileSystemOpenZFSConfigurationTypeDef(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    AddRouteTableIds: Optional[Sequence[str]] = None
    RemoveRouteTableIds: Optional[Sequence[str]] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfigurationTypeDef] = None


class CreateSvmActiveDirectoryConfigurationTypeDef(BaseValidatorModel):
    NetBiosName: str
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfigurationTypeDef ] = None


class CreateFileSystemWindowsConfigurationTypeDef(BaseValidatorModel):
    ThroughputCapacity: int
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfigurationTypeDef ] = None
    DeploymentType: Optional[WindowsDeploymentTypeType] = None
    PreferredSubnetId: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    Aliases: Optional[Sequence[str]] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfigurationTypeDef] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None


class DataRepositoryConfigurationTypeDef(BaseValidatorModel):
    Lifecycle: Optional[DataRepositoryLifecycleType] = None
    ImportPath: Optional[str] = None
    ExportPath: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    FailureDetails: Optional[DataRepositoryFailureDetailsTypeDef] = None


class DescribeDataRepositoryTasksRequestTypeDef(BaseValidatorModel):
    TaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[DataRepositoryTaskFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBackupsRequestTypeDef(BaseValidatorModel):
    BackupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDataRepositoryAssociationsRequestTypeDef(BaseValidatorModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBackupsRequestPaginateTypeDef(BaseValidatorModel):
    BackupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeFileSystemsRequestPaginateTypeDef(BaseValidatorModel):
    FileSystemIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSnapshotsRequestTypeDef(BaseValidatorModel):
    SnapshotIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[SnapshotFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeShared: Optional[bool] = None


class DescribeStorageVirtualMachinesRequestPaginateTypeDef(BaseValidatorModel):
    StorageVirtualMachineIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[StorageVirtualMachineFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeStorageVirtualMachinesRequestTypeDef(BaseValidatorModel):
    StorageVirtualMachineIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[StorageVirtualMachineFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVolumesRequestPaginateTypeDef(BaseValidatorModel):
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VolumeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeVolumesRequestTypeDef(BaseValidatorModel):
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VolumeFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReleaseConfigurationTypeDef(BaseValidatorModel):
    DurationSinceLastAccess: Optional[DurationSinceLastAccessTypeDef] = None


class FileCacheDataRepositoryAssociationTypeDef(BaseValidatorModel):
    FileCachePath: str
    DataRepositoryPath: str
    DataRepositorySubdirectories: Optional[Sequence[str]] = None
    NFS: Optional[FileCacheNFSConfigurationTypeDef] = None


class FileCacheLustreConfigurationTypeDef(BaseValidatorModel):
    PerUnitStorageThroughput: Optional[int] = None
    DeploymentType: Optional[Literal["CACHE_1"]] = None
    MountName: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    MetadataConfiguration: Optional[FileCacheLustreMetadataConfigurationTypeDef] = None
    LogConfiguration: Optional[LustreLogConfigurationTypeDef] = None


class FileSystemEndpointsTypeDef(BaseValidatorModel):
    Intercluster: Optional[FileSystemEndpointTypeDef] = None
    Management: Optional[FileSystemEndpointTypeDef] = None


class SnapshotPaginatorTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    SnapshotId: Optional[str] = None
    Name: Optional[str] = None
    VolumeId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Lifecycle: Optional[SnapshotLifecycleType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None


class SnapshotTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    SnapshotId: Optional[str] = None
    Name: Optional[str] = None
    VolumeId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Lifecycle: Optional[SnapshotLifecycleType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None


class OpenZFSNfsExportOutputTypeDef(BaseValidatorModel):
    ClientConfigurations: List[OpenZFSClientConfigurationOutputTypeDef]


class RetentionPeriodTypeDef(BaseValidatorModel):
    pass


class SnaplockRetentionPeriodTypeDef(BaseValidatorModel):
    DefaultRetention: RetentionPeriodTypeDef
    MinimumRetention: RetentionPeriodTypeDef
    MaximumRetention: RetentionPeriodTypeDef


class SvmActiveDirectoryConfigurationTypeDef(BaseValidatorModel):
    NetBiosName: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryAttributesTypeDef ] = None


class UpdateFileSystemWindowsConfigurationTypeDef(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    ThroughputCapacity: Optional[int] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfigurationUpdatesTypeDef ] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfigurationTypeDef] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None


class UpdateSvmActiveDirectoryConfigurationTypeDef(BaseValidatorModel):
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryConfigurationUpdatesTypeDef ] = None
    NetBiosName: Optional[str] = None


class SvmEndpointsTypeDef(BaseValidatorModel):
    Iscsi: Optional[SvmEndpointTypeDef] = None
    Management: Optional[SvmEndpointTypeDef] = None
    Nfs: Optional[SvmEndpointTypeDef] = None
    Smb: Optional[SvmEndpointTypeDef] = None


class UpdateFileCacheRequestTypeDef(BaseValidatorModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None
    LustreConfiguration: Optional[UpdateFileCacheLustreConfigurationTypeDef] = None


class WindowsFileSystemConfigurationTypeDef(BaseValidatorModel):
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[ SelfManagedActiveDirectoryAttributesTypeDef ] = None
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
    Aliases: Optional[List[AliasTypeDef]] = None
    AuditLogConfiguration: Optional[WindowsAuditLogConfigurationTypeDef] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None


class DataRepositoryAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    ResourceARN: Optional[str] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[DataRepositoryLifecycleType] = None
    FailureDetails: Optional[DataRepositoryFailureDetailsTypeDef] = None
    FileSystemPath: Optional[str] = None
    DataRepositoryPath: Optional[str] = None
    BatchImportMetaDataOnCreate: Optional[bool] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationOutputTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCachePath: Optional[str] = None
    DataRepositorySubdirectories: Optional[List[str]] = None
    NFS: Optional[NFSDataRepositoryConfigurationTypeDef] = None


class DeleteFileSystemRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    WindowsConfiguration: Optional[DeleteFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[DeleteFileSystemLustreConfigurationTypeDef] = None
    OpenZFSConfiguration: Optional[DeleteFileSystemOpenZFSConfigurationTypeDef] = None


class DeleteFileSystemResponseTypeDef(BaseValidatorModel):
    FileSystemId: str
    Lifecycle: FileSystemLifecycleType
    WindowsResponse: DeleteFileSystemWindowsResponseTypeDef
    LustreResponse: DeleteFileSystemLustreResponseTypeDef
    OpenZFSResponse: DeleteFileSystemOpenZFSResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[DeleteVolumeOntapConfigurationTypeDef] = None
    OpenZFSConfiguration: Optional[DeleteVolumeOpenZFSConfigurationTypeDef] = None


class DeleteVolumeResponseTypeDef(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    OntapResponse: DeleteVolumeOntapResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStorageVirtualMachineRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    Name: str
    ActiveDirectoryConfiguration: Optional[CreateSvmActiveDirectoryConfigurationTypeDef] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    RootVolumeSecurityStyle: Optional[StorageVirtualMachineRootVolumeSecurityStyleType] = None


class LustreFileSystemConfigurationTypeDef(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DataRepositoryConfiguration: Optional[DataRepositoryConfigurationTypeDef] = None
    DeploymentType: Optional[LustreDeploymentTypeType] = None
    PerUnitStorageThroughput: Optional[int] = None
    MountName: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    DriveCacheType: Optional[DriveCacheTypeType] = None
    DataCompressionType: Optional[DataCompressionTypeType] = None
    LogConfiguration: Optional[LustreLogConfigurationTypeDef] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationOutputTypeDef] = None
    MetadataConfiguration: Optional[FileSystemLustreMetadataConfigurationTypeDef] = None
    EfaEnabled: Optional[bool] = None


class CreateFileCacheRequestTypeDef(BaseValidatorModel):
    FileCacheType: Literal["LUSTRE"]
    FileCacheTypeVersion: str
    StorageCapacity: int
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CopyTagsToDataRepositoryAssociations: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    LustreConfiguration: Optional[CreateFileCacheLustreConfigurationTypeDef] = None
    DataRepositoryAssociations: Optional[Sequence[FileCacheDataRepositoryAssociationTypeDef]] = None


class FileCacheCreatingTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCacheType: Optional[Literal["LUSTRE"]] = None
    FileCacheTypeVersion: Optional[str] = None
    Lifecycle: Optional[FileCacheLifecycleType] = None
    FailureDetails: Optional[FileCacheFailureDetailsTypeDef] = None
    StorageCapacity: Optional[int] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    CopyTagsToDataRepositoryAssociations: Optional[bool] = None
    LustreConfiguration: Optional[FileCacheLustreConfigurationTypeDef] = None
    DataRepositoryAssociationIds: Optional[List[str]] = None


class FileCacheTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileCacheId: Optional[str] = None
    FileCacheType: Optional[Literal["LUSTRE"]] = None
    FileCacheTypeVersion: Optional[str] = None
    Lifecycle: Optional[FileCacheLifecycleType] = None
    FailureDetails: Optional[FileCacheFailureDetailsTypeDef] = None
    StorageCapacity: Optional[int] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    LustreConfiguration: Optional[FileCacheLustreConfigurationTypeDef] = None
    DataRepositoryAssociationIds: Optional[List[str]] = None


class OntapFileSystemConfigurationTypeDef(BaseValidatorModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    DeploymentType: Optional[OntapDeploymentTypeType] = None
    EndpointIpAddressRange: Optional[str] = None
    Endpoints: Optional[FileSystemEndpointsTypeDef] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    PreferredSubnetId: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    FsxAdminPassword: Optional[str] = None
    HAPairs: Optional[int] = None
    ThroughputCapacityPerHAPair: Optional[int] = None


class CreateSnapshotResponseTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSnapshotsResponseTypeDef(BaseValidatorModel):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateSnapshotResponseTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LustreRootSquashConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateFileSystemLustreConfigurationTypeDef(BaseValidatorModel):
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
    LogConfiguration: Optional[LustreLogCreateConfigurationTypeDef] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationUnionTypeDef] = None
    MetadataConfiguration: Optional[CreateFileSystemLustreMetadataConfigurationTypeDef] = None


class UpdateFileSystemLustreConfigurationTypeDef(BaseValidatorModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    DataCompressionType: Optional[DataCompressionTypeType] = None
    LogConfiguration: Optional[LustreLogCreateConfigurationTypeDef] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationUnionTypeDef] = None
    PerUnitStorageThroughput: Optional[int] = None
    MetadataConfiguration: Optional[UpdateFileSystemLustreMetadataConfigurationTypeDef] = None


class OpenZFSClientConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class OpenZFSNfsExportTypeDef(BaseValidatorModel):
    ClientConfigurations: Sequence[OpenZFSClientConfigurationUnionTypeDef]


class AutocommitPeriodTypeDef(BaseValidatorModel):
    pass


class CreateSnaplockConfigurationTypeDef(BaseValidatorModel):
    SnaplockType: SnaplockTypeType
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriodTypeDef] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriodTypeDef] = None
    VolumeAppendModeEnabled: Optional[bool] = None


class SnaplockConfigurationTypeDef(BaseValidatorModel):
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriodTypeDef] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriodTypeDef] = None
    SnaplockType: Optional[SnaplockTypeType] = None
    VolumeAppendModeEnabled: Optional[bool] = None


class UpdateSnaplockConfigurationTypeDef(BaseValidatorModel):
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriodTypeDef] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriodTypeDef] = None
    VolumeAppendModeEnabled: Optional[bool] = None


class UpdateStorageVirtualMachineRequestTypeDef(BaseValidatorModel):
    StorageVirtualMachineId: str
    ActiveDirectoryConfiguration: Optional[UpdateSvmActiveDirectoryConfigurationTypeDef] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None


class StorageVirtualMachineTypeDef(BaseValidatorModel):
    ActiveDirectoryConfiguration: Optional[SvmActiveDirectoryConfigurationTypeDef] = None
    CreationTime: Optional[datetime] = None
    Endpoints: Optional[SvmEndpointsTypeDef] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[StorageVirtualMachineLifecycleType] = None
    Name: Optional[str] = None
    ResourceARN: Optional[str] = None
    StorageVirtualMachineId: Optional[str] = None
    Subtype: Optional[StorageVirtualMachineSubtypeType] = None
    UUID: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReasonTypeDef] = None
    RootVolumeSecurityStyle: Optional[StorageVirtualMachineRootVolumeSecurityStyleType] = None


class CreateDataRepositoryAssociationResponseTypeDef(BaseValidatorModel):
    Association: DataRepositoryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDataRepositoryAssociationsResponseTypeDef(BaseValidatorModel):
    Associations: List[DataRepositoryAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateDataRepositoryAssociationResponseTypeDef(BaseValidatorModel):
    Association: DataRepositoryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class S3DataRepositoryConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataRepositoryAssociationRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    DataRepositoryPath: str
    FileSystemPath: Optional[str] = None
    BatchImportMetaDataOnCreate: Optional[bool] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationUnionTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDataRepositoryAssociationRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationUnionTypeDef] = None


class DataRepositoryTaskTypeDef(BaseValidatorModel):
    pass


class CreateDataRepositoryTaskResponseTypeDef(BaseValidatorModel):
    DataRepositoryTask: DataRepositoryTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDataRepositoryTasksResponseTypeDef(BaseValidatorModel):
    DataRepositoryTasks: List[DataRepositoryTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateFileCacheResponseTypeDef(BaseValidatorModel):
    FileCache: FileCacheCreatingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFileCachesResponseTypeDef(BaseValidatorModel):
    FileCaches: List[FileCacheTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateFileCacheResponseTypeDef(BaseValidatorModel):
    FileCache: FileCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFileSystemRequestTypeDef(BaseValidatorModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    StorageCapacity: Optional[int] = None
    WindowsConfiguration: Optional[UpdateFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[UpdateFileSystemLustreConfigurationTypeDef] = None
    OntapConfiguration: Optional[UpdateFileSystemOntapConfigurationTypeDef] = None
    OpenZFSConfiguration: Optional[UpdateFileSystemOpenZFSConfigurationTypeDef] = None
    StorageType: Optional[StorageTypeType] = None
    FileSystemTypeVersion: Optional[str] = None


class CreateOntapVolumeConfigurationTypeDef(BaseValidatorModel):
    StorageVirtualMachineId: str
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicyTypeDef] = None
    OntapVolumeType: Optional[InputOntapVolumeTypeType] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[CreateSnaplockConfigurationTypeDef] = None
    VolumeStyle: Optional[VolumeStyleType] = None
    AggregateConfiguration: Optional[CreateAggregateConfigurationTypeDef] = None
    SizeInBytes: Optional[int] = None


class OntapVolumeConfigurationTypeDef(BaseValidatorModel):
    FlexCacheEndpointType: Optional[FlexCacheEndpointTypeType] = None
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    StorageVirtualMachineId: Optional[str] = None
    StorageVirtualMachineRoot: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicyTypeDef] = None
    UUID: Optional[str] = None
    OntapVolumeType: Optional[OntapVolumeTypeType] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[SnaplockConfigurationTypeDef] = None
    VolumeStyle: Optional[VolumeStyleType] = None
    AggregateConfiguration: Optional[AggregateConfigurationTypeDef] = None
    SizeInBytes: Optional[int] = None


class UpdateOntapVolumeConfigurationTypeDef(BaseValidatorModel):
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicyTypeDef] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[UpdateSnaplockConfigurationTypeDef] = None
    SizeInBytes: Optional[int] = None


class CreateStorageVirtualMachineResponseTypeDef(BaseValidatorModel):
    StorageVirtualMachine: StorageVirtualMachineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeStorageVirtualMachinesResponseTypeDef(BaseValidatorModel):
    StorageVirtualMachines: List[StorageVirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateStorageVirtualMachineResponseTypeDef(BaseValidatorModel):
    StorageVirtualMachine: StorageVirtualMachineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVolumeFromBackupRequestTypeDef(BaseValidatorModel):
    BackupId: str
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class OpenZFSVolumeConfigurationTypeDef(BaseValidatorModel):
    pass


class VolumePaginatorTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[VolumeLifecycleType] = None
    Name: Optional[str] = None
    OntapConfiguration: Optional[OntapVolumeConfigurationTypeDef] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReasonTypeDef] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None
    OpenZFSConfiguration: Optional[OpenZFSVolumeConfigurationTypeDef] = None


class VolumeTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    Lifecycle: Optional[VolumeLifecycleType] = None
    Name: Optional[str] = None
    OntapConfiguration: Optional[OntapVolumeConfigurationTypeDef] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReasonTypeDef] = None
    AdministrativeActions: Optional[List[Dict[str, Any]]] = None
    OpenZFSConfiguration: Optional[OpenZFSVolumeConfigurationTypeDef] = None


class CreateOpenZFSVolumeConfigurationTypeDef(BaseValidatorModel):
    pass


class CreateVolumeRequestTypeDef(BaseValidatorModel):
    VolumeType: VolumeTypeType
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OpenZFSConfiguration: Optional[CreateOpenZFSVolumeConfigurationTypeDef] = None


class OpenZFSCreateRootVolumeConfigurationTypeDef(BaseValidatorModel):
    pass


class CreateFileSystemOpenZFSConfigurationTypeDef(BaseValidatorModel):
    DeploymentType: OpenZFSDeploymentTypeType
    ThroughputCapacity: int
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    RootVolumeConfiguration: Optional[OpenZFSCreateRootVolumeConfigurationTypeDef] = None
    PreferredSubnetId: Optional[str] = None
    EndpointIpAddressRange: Optional[str] = None
    RouteTableIds: Optional[Sequence[str]] = None
    ReadCacheConfiguration: Optional[OpenZFSReadCacheConfigurationTypeDef] = None


class UpdateOpenZFSVolumeConfigurationTypeDef(BaseValidatorModel):
    pass


class UpdateVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[UpdateOntapVolumeConfigurationTypeDef] = None
    Name: Optional[str] = None
    OpenZFSConfiguration: Optional[UpdateOpenZFSVolumeConfigurationTypeDef] = None


class AdministrativeActionPaginatorTypeDef(BaseValidatorModel):
    AdministrativeActionType: Optional[AdministrativeActionTypeType] = None
    ProgressPercent: Optional[int] = None
    RequestTime: Optional[datetime] = None
    Status: Optional[StatusType] = None
    TargetFileSystemValues: Optional[Dict[str, Any]] = None
    FailureDetails: Optional[AdministrativeActionFailureDetailsTypeDef] = None
    TargetVolumeValues: Optional[VolumePaginatorTypeDef] = None
    TargetSnapshotValues: Optional[SnapshotPaginatorTypeDef] = None
    TotalTransferBytes: Optional[int] = None
    RemainingTransferBytes: Optional[int] = None


class DescribeVolumesResponsePaginatorTypeDef(BaseValidatorModel):
    Volumes: List[VolumePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AdministrativeActionTypeDef(BaseValidatorModel):
    AdministrativeActionType: Optional[AdministrativeActionTypeType] = None
    ProgressPercent: Optional[int] = None
    RequestTime: Optional[datetime] = None
    Status: Optional[StatusType] = None
    TargetFileSystemValues: Optional[Dict[str, Any]] = None
    FailureDetails: Optional[AdministrativeActionFailureDetailsTypeDef] = None
    TargetVolumeValues: Optional[VolumeTypeDef] = None
    TargetSnapshotValues: Optional[SnapshotTypeDef] = None
    TotalTransferBytes: Optional[int] = None
    RemainingTransferBytes: Optional[int] = None


class CreateVolumeFromBackupResponseTypeDef(BaseValidatorModel):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVolumeResponseTypeDef(BaseValidatorModel):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVolumesResponseTypeDef(BaseValidatorModel):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateVolumeResponseTypeDef(BaseValidatorModel):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFileSystemFromBackupRequestTypeDef(BaseValidatorModel):
    BackupId: str
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WindowsConfiguration: Optional[CreateFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[CreateFileSystemLustreConfigurationTypeDef] = None
    StorageType: Optional[StorageTypeType] = None
    KmsKeyId: Optional[str] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[CreateFileSystemOpenZFSConfigurationTypeDef] = None
    StorageCapacity: Optional[int] = None


class CreateFileSystemRequestTypeDef(BaseValidatorModel):
    FileSystemType: FileSystemTypeType
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    WindowsConfiguration: Optional[CreateFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[CreateFileSystemLustreConfigurationTypeDef] = None
    OntapConfiguration: Optional[CreateFileSystemOntapConfigurationTypeDef] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[CreateFileSystemOpenZFSConfigurationTypeDef] = None


class FileSystemPaginatorTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    FileSystemType: Optional[FileSystemTypeType] = None
    Lifecycle: Optional[FileSystemLifecycleType] = None
    FailureDetails: Optional[FileSystemFailureDetailsTypeDef] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    WindowsConfiguration: Optional[WindowsFileSystemConfigurationTypeDef] = None
    LustreConfiguration: Optional[LustreFileSystemConfigurationTypeDef] = None
    AdministrativeActions: Optional[List[AdministrativeActionPaginatorTypeDef]] = None
    OntapConfiguration: Optional[OntapFileSystemConfigurationTypeDef] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[OpenZFSFileSystemConfigurationTypeDef] = None


class CopySnapshotAndUpdateVolumeResponseTypeDef(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FileSystemTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FileSystemId: Optional[str] = None
    FileSystemType: Optional[FileSystemTypeType] = None
    Lifecycle: Optional[FileSystemLifecycleType] = None
    FailureDetails: Optional[FileSystemFailureDetailsTypeDef] = None
    StorageCapacity: Optional[int] = None
    StorageType: Optional[StorageTypeType] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DNSName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    WindowsConfiguration: Optional[WindowsFileSystemConfigurationTypeDef] = None
    LustreConfiguration: Optional[LustreFileSystemConfigurationTypeDef] = None
    AdministrativeActions: Optional[List[AdministrativeActionTypeDef]] = None
    OntapConfiguration: Optional[OntapFileSystemConfigurationTypeDef] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[OpenZFSFileSystemConfigurationTypeDef] = None


class RestoreVolumeFromSnapshotResponseTypeDef(BaseValidatorModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFileSystemsResponsePaginatorTypeDef(BaseValidatorModel):
    FileSystems: List[FileSystemPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateFileSystemFromBackupResponseTypeDef(BaseValidatorModel):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFileSystemResponseTypeDef(BaseValidatorModel):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFileSystemsResponseTypeDef(BaseValidatorModel):
    FileSystems: List[FileSystemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ReleaseFileSystemNfsV3LocksResponseTypeDef(BaseValidatorModel):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartMisconfiguredStateRecoveryResponseTypeDef(BaseValidatorModel):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFileSystemResponseTypeDef(BaseValidatorModel):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BackupPaginatorTypeDef(BaseValidatorModel):
    pass


class DescribeBackupsResponsePaginatorTypeDef(BaseValidatorModel):
    Backups: List[BackupPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BackupTypeDef(BaseValidatorModel):
    pass


class CopyBackupResponseTypeDef(BaseValidatorModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackupResponseTypeDef(BaseValidatorModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBackupsResponseTypeDef(BaseValidatorModel):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


