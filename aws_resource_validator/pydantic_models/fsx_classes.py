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
from aws_resource_validator.pydantic_models.fsx_constants import *

class ActiveDirectoryBackupAttributesTypeDef(BaseModel):
    DomainName: Optional[str] = None
    ActiveDirectoryId: Optional[str] = None
    ResourceARN: Optional[str] = None

class AdministrativeActionFailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class AggregateConfigurationTypeDef(BaseModel):
    Aggregates: Optional[List[str]] = None
    TotalConstituents: Optional[int] = None

class AliasTypeDef(BaseModel):
    Name: Optional[str] = None
    Lifecycle: Optional[AliasLifecycleType] = None

class AssociateFileSystemAliasesRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AutoExportPolicyOutputTypeDef(BaseModel):
    Events: Optional[List[EventTypeType]] = None

class AutoExportPolicyTypeDef(BaseModel):
    Events: Optional[Sequence[EventTypeType]] = None

class AutoImportPolicyOutputTypeDef(BaseModel):
    Events: Optional[List[EventTypeType]] = None

class AutoImportPolicyTypeDef(BaseModel):
    Events: Optional[Sequence[EventTypeType]] = None

class AutocommitPeriodTypeDef(BaseModel):
    Type: AutocommitPeriodTypeType
    Value: Optional[int] = None

class BackupFailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CancelDataRepositoryTaskRequestRequestTypeDef(BaseModel):
    TaskId: str

class CompletionReportTypeDef(BaseModel):
    Enabled: bool
    Path: Optional[str] = None
    Format: Optional[Literal["REPORT_CSV_20191124"]] = None
    Scope: Optional[Literal["FAILED_FILES_ONLY"]] = None

class CopySnapshotAndUpdateVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    SourceSnapshotARN: str
    ClientRequestToken: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None
    Options: Optional[Sequence[UpdateOpenZFSVolumeOptionType]] = None

class CreateAggregateConfigurationTypeDef(BaseModel):
    Aggregates: Optional[Sequence[str]] = None
    ConstituentsPerAggregate: Optional[int] = None

class FileCacheLustreMetadataConfigurationTypeDef(BaseModel):
    StorageCapacity: int

class CreateFileSystemLustreMetadataConfigurationTypeDef(BaseModel):
    Mode: MetadataConfigurationModeType
    Iops: Optional[int] = None

class LustreLogCreateConfigurationTypeDef(BaseModel):
    Level: LustreAccessAuditLogLevelType
    Destination: Optional[str] = None

class LustreRootSquashConfigurationTypeDef(BaseModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[Sequence[str]] = None

class DiskIopsConfigurationTypeDef(BaseModel):
    Mode: Optional[DiskIopsConfigurationModeType] = None
    Iops: Optional[int] = None

class SelfManagedActiveDirectoryConfigurationTypeDef(BaseModel):
    DomainName: str
    UserName: str
    Password: str
    DnsIps: Sequence[str]
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None

class WindowsAuditLogCreateConfigurationTypeDef(BaseModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None

class TieringPolicyTypeDef(BaseModel):
    CoolingPeriod: Optional[int] = None
    Name: Optional[TieringPolicyNameType] = None

class CreateOpenZFSOriginSnapshotConfigurationTypeDef(BaseModel):
    SnapshotARN: str
    CopyStrategy: OpenZFSCopyStrategyType

class OpenZFSUserOrGroupQuotaTypeDef(BaseModel):
    Type: OpenZFSQuotaTypeType
    Id: int
    StorageCapacityQuotaGiB: int

class DataRepositoryFailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class DataRepositoryTaskFailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class DataRepositoryTaskFilterTypeDef(BaseModel):
    Name: Optional[DataRepositoryTaskFilterNameType] = None
    Values: Optional[Sequence[str]] = None

class DataRepositoryTaskStatusTypeDef(BaseModel):
    TotalCount: Optional[int] = None
    SucceededCount: Optional[int] = None
    FailedCount: Optional[int] = None
    LastUpdatedTime: Optional[datetime] = None
    ReleasedCapacity: Optional[int] = None

class DeleteBackupRequestRequestTypeDef(BaseModel):
    BackupId: str
    ClientRequestToken: Optional[str] = None

class DeleteDataRepositoryAssociationRequestRequestTypeDef(BaseModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    DeleteDataInFileSystem: Optional[bool] = None

class DeleteFileCacheRequestRequestTypeDef(BaseModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None

class DeleteSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    ClientRequestToken: Optional[str] = None

class DeleteStorageVirtualMachineRequestRequestTypeDef(BaseModel):
    StorageVirtualMachineId: str
    ClientRequestToken: Optional[str] = None

class DeleteVolumeOpenZFSConfigurationTypeDef(BaseModel):
    Options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = None

class FilterTypeDef(BaseModel):
    Name: Optional[FilterNameType] = None
    Values: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeFileCachesRequestRequestTypeDef(BaseModel):
    FileCacheIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFileSystemAliasesRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFileSystemsRequestRequestTypeDef(BaseModel):
    FileSystemIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SnapshotFilterTypeDef(BaseModel):
    Name: Optional[SnapshotFilterNameType] = None
    Values: Optional[Sequence[str]] = None

class StorageVirtualMachineFilterTypeDef(BaseModel):
    Name: Optional[Literal["file-system-id"]] = None
    Values: Optional[Sequence[str]] = None

class VolumeFilterTypeDef(BaseModel):
    Name: Optional[VolumeFilterNameType] = None
    Values: Optional[Sequence[str]] = None

class DisassociateFileSystemAliasesRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: Optional[str] = None

class DurationSinceLastAccessTypeDef(BaseModel):
    Unit: Optional[Literal["DAYS"]] = None
    Value: Optional[int] = None

class FileCacheFailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class FileCacheNFSConfigurationTypeDef(BaseModel):
    Version: Literal["NFS3"]
    DnsIps: Optional[Sequence[str]] = None

class LustreLogConfigurationTypeDef(BaseModel):
    Level: LustreAccessAuditLogLevelType
    Destination: Optional[str] = None

class FileSystemEndpointTypeDef(BaseModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None

class FileSystemFailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class FileSystemLustreMetadataConfigurationTypeDef(BaseModel):
    Mode: MetadataConfigurationModeType
    Iops: Optional[int] = None

class LifecycleTransitionReasonTypeDef(BaseModel):
    Message: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LustreRootSquashConfigurationOutputTypeDef(BaseModel):
    RootSquash: Optional[str] = None
    NoSquashNids: Optional[List[str]] = None

class OpenZFSClientConfigurationOutputTypeDef(BaseModel):
    Clients: str
    Options: List[str]

class OpenZFSClientConfigurationTypeDef(BaseModel):
    Clients: str
    Options: Sequence[str]

class OpenZFSOriginSnapshotConfigurationTypeDef(BaseModel):
    SnapshotARN: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None

class ReleaseFileSystemNfsV3LocksRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None

class RestoreVolumeFromSnapshotRequestRequestTypeDef(BaseModel):
    VolumeId: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None
    Options: Optional[Sequence[RestoreOpenZFSVolumeOptionType]] = None

class RetentionPeriodTypeDef(BaseModel):
    Type: RetentionPeriodTypeType
    Value: Optional[int] = None

class SelfManagedActiveDirectoryAttributesTypeDef(BaseModel):
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None
    UserName: Optional[str] = None
    DnsIps: Optional[List[str]] = None

class SelfManagedActiveDirectoryConfigurationUpdatesTypeDef(BaseModel):
    UserName: Optional[str] = None
    Password: Optional[str] = None
    DnsIps: Optional[Sequence[str]] = None
    DomainName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None
    FileSystemAdministratorsGroup: Optional[str] = None

class StartMisconfiguredStateRecoveryRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None

class SvmEndpointTypeDef(BaseModel):
    DNSName: Optional[str] = None
    IpAddresses: Optional[List[str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateFileCacheLustreConfigurationTypeDef(BaseModel):
    WeeklyMaintenanceStartTime: Optional[str] = None

class UpdateFileSystemLustreMetadataConfigurationTypeDef(BaseModel):
    Iops: Optional[int] = None
    Mode: Optional[MetadataConfigurationModeType] = None

class UpdateSharedVpcConfigurationRequestRequestTypeDef(BaseModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class UpdateSnapshotRequestRequestTypeDef(BaseModel):
    Name: str
    SnapshotId: str
    ClientRequestToken: Optional[str] = None

class WindowsAuditLogConfigurationTypeDef(BaseModel):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: Optional[str] = None

class AssociateFileSystemAliasesResponseTypeDef(BaseModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDataRepositoryTaskResponseTypeDef(BaseModel):
    Lifecycle: DataRepositoryTaskLifecycleType
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopySnapshotAndUpdateVolumeResponseTypeDef(BaseModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List["AdministrativeActionTypeDef"]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemFromBackupResponseTypeDef(BaseModel):
    FileSystem: "FileSystemTypeDef"
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemResponseTypeDef(BaseModel):
    FileSystem: "FileSystemTypeDef"
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupResponseTypeDef(BaseModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataRepositoryAssociationResponseTypeDef(BaseModel):
    AssociationId: str
    Lifecycle: DataRepositoryLifecycleType
    DeleteDataInFileSystem: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFileCacheResponseTypeDef(BaseModel):
    FileCacheId: str
    Lifecycle: FileCacheLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResponseTypeDef(BaseModel):
    SnapshotId: str
    Lifecycle: SnapshotLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStorageVirtualMachineResponseTypeDef(BaseModel):
    StorageVirtualMachineId: str
    Lifecycle: StorageVirtualMachineLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFileSystemAliasesResponseTypeDef(BaseModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFileSystemsResponseTypeDef(BaseModel):
    FileSystems: List["FileSystemTypeDef"]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSharedVpcConfigurationResponseTypeDef(BaseModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFileSystemAliasesResponseTypeDef(BaseModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseFileSystemNfsV3LocksResponseTypeDef(BaseModel):
    FileSystem: "FileSystemTypeDef"
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreVolumeFromSnapshotResponseTypeDef(BaseModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List["AdministrativeActionTypeDef"]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMisconfiguredStateRecoveryResponseTypeDef(BaseModel):
    FileSystem: "FileSystemTypeDef"
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFileSystemResponseTypeDef(BaseModel):
    FileSystem: "FileSystemTypeDef"
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSharedVpcConfigurationResponseTypeDef(BaseModel):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadataTypeDef

class NFSDataRepositoryConfigurationTypeDef(BaseModel):
    Version: Literal["NFS3"]
    DnsIps: Optional[List[str]] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutputTypeDef] = None

class S3DataRepositoryConfigurationOutputTypeDef(BaseModel):
    AutoImportPolicy: Optional[AutoImportPolicyOutputTypeDef] = None
    AutoExportPolicy: Optional[AutoExportPolicyOutputTypeDef] = None

class S3DataRepositoryConfigurationTypeDef(BaseModel):
    AutoImportPolicy: Optional[AutoImportPolicyTypeDef] = None
    AutoExportPolicy: Optional[AutoExportPolicyTypeDef] = None

class CopyBackupRequestRequestTypeDef(BaseModel):
    SourceBackupId: str
    ClientRequestToken: Optional[str] = None
    SourceRegion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateBackupRequestRequestTypeDef(BaseModel):
    FileSystemId: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VolumeId: Optional[str] = None

class CreateSnapshotRequestRequestTypeDef(BaseModel):
    Name: str
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DeleteFileSystemLustreConfigurationTypeDef(BaseModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None

class DeleteFileSystemLustreResponseTypeDef(BaseModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None

class DeleteFileSystemOpenZFSConfigurationTypeDef(BaseModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None
    Options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = None

class DeleteFileSystemOpenZFSResponseTypeDef(BaseModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None

class DeleteFileSystemWindowsConfigurationTypeDef(BaseModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None

class DeleteFileSystemWindowsResponseTypeDef(BaseModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None

class DeleteVolumeOntapConfigurationTypeDef(BaseModel):
    SkipFinalBackup: Optional[bool] = None
    FinalBackupTags: Optional[Sequence[TagTypeDef]] = None
    BypassSnaplockEnterpriseRetention: Optional[bool] = None

class DeleteVolumeOntapResponseTypeDef(BaseModel):
    FinalBackupId: Optional[str] = None
    FinalBackupTags: Optional[List[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateFileCacheLustreConfigurationTypeDef(BaseModel):
    PerUnitStorageThroughput: int
    DeploymentType: Literal["CACHE_1"]
    MetadataConfiguration: FileCacheLustreMetadataConfigurationTypeDef
    WeeklyMaintenanceStartTime: Optional[str] = None

class CreateFileSystemLustreConfigurationTypeDef(BaseModel):
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
    LogConfiguration: Optional[LustreLogCreateConfigurationTypeDef] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationTypeDef] = None
    MetadataConfiguration: Optional[CreateFileSystemLustreMetadataConfigurationTypeDef] = None

class CreateFileSystemOntapConfigurationTypeDef(BaseModel):
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

class OpenZFSFileSystemConfigurationTypeDef(BaseModel):
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

class UpdateFileSystemOntapConfigurationTypeDef(BaseModel):
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

class UpdateFileSystemOpenZFSConfigurationTypeDef(BaseModel):
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    CopyTagsToVolumes: Optional[bool] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    ThroughputCapacity: Optional[int] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None
    AddRouteTableIds: Optional[Sequence[str]] = None
    RemoveRouteTableIds: Optional[Sequence[str]] = None

class CreateSvmActiveDirectoryConfigurationTypeDef(BaseModel):
    NetBiosName: str
    SelfManagedActiveDirectoryConfiguration: Optional[       SelfManagedActiveDirectoryConfigurationTypeDef     ] = None

class CreateFileSystemWindowsConfigurationTypeDef(BaseModel):
    ThroughputCapacity: int
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[       SelfManagedActiveDirectoryConfigurationTypeDef     ] = None
    DeploymentType: Optional[WindowsDeploymentTypeType] = None
    PreferredSubnetId: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    CopyTagsToBackups: Optional[bool] = None
    Aliases: Optional[Sequence[str]] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfigurationTypeDef] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None

class DataRepositoryConfigurationTypeDef(BaseModel):
    Lifecycle: Optional[DataRepositoryLifecycleType] = None
    ImportPath: Optional[str] = None
    ExportPath: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    FailureDetails: Optional[DataRepositoryFailureDetailsTypeDef] = None

class DescribeDataRepositoryTasksRequestRequestTypeDef(BaseModel):
    TaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[DataRepositoryTaskFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBackupsRequestRequestTypeDef(BaseModel):
    BackupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDataRepositoryAssociationsRequestRequestTypeDef(BaseModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBackupsRequestDescribeBackupsPaginateTypeDef(BaseModel):
    BackupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef(BaseModel):
    FileSystemIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseModel):
    SnapshotIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[SnapshotFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeShared: Optional[bool] = None

class DescribeStorageVirtualMachinesRequestDescribeStorageVirtualMachinesPaginateTypeDef(BaseModel):
    StorageVirtualMachineIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[StorageVirtualMachineFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStorageVirtualMachinesRequestRequestTypeDef(BaseModel):
    StorageVirtualMachineIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[StorageVirtualMachineFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVolumesRequestDescribeVolumesPaginateTypeDef(BaseModel):
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VolumeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumesRequestRequestTypeDef(BaseModel):
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VolumeFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ReleaseConfigurationTypeDef(BaseModel):
    DurationSinceLastAccess: Optional[DurationSinceLastAccessTypeDef] = None

class FileCacheDataRepositoryAssociationTypeDef(BaseModel):
    FileCachePath: str
    DataRepositoryPath: str
    DataRepositorySubdirectories: Optional[Sequence[str]] = None
    NFS: Optional[FileCacheNFSConfigurationTypeDef] = None

class FileCacheLustreConfigurationTypeDef(BaseModel):
    PerUnitStorageThroughput: Optional[int] = None
    DeploymentType: Optional[Literal["CACHE_1"]] = None
    MountName: Optional[str] = None
    WeeklyMaintenanceStartTime: Optional[str] = None
    MetadataConfiguration: Optional[FileCacheLustreMetadataConfigurationTypeDef] = None
    LogConfiguration: Optional[LustreLogConfigurationTypeDef] = None

class FileSystemEndpointsTypeDef(BaseModel):
    Intercluster: Optional[FileSystemEndpointTypeDef] = None
    Management: Optional[FileSystemEndpointTypeDef] = None

class SnapshotTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    SnapshotId: Optional[str] = None
    Name: Optional[str] = None
    VolumeId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Lifecycle: Optional[SnapshotLifecycleType] = None
    LifecycleTransitionReason: Optional[LifecycleTransitionReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    AdministrativeActions: Optional[List["AdministrativeActionTypeDef"]] = None

class OpenZFSNfsExportOutputTypeDef(BaseModel):
    ClientConfigurations: List[OpenZFSClientConfigurationOutputTypeDef]

class OpenZFSNfsExportTypeDef(BaseModel):
    ClientConfigurations: Sequence[OpenZFSClientConfigurationTypeDef]

class SnaplockRetentionPeriodTypeDef(BaseModel):
    DefaultRetention: RetentionPeriodTypeDef
    MinimumRetention: RetentionPeriodTypeDef
    MaximumRetention: RetentionPeriodTypeDef

class SvmActiveDirectoryConfigurationTypeDef(BaseModel):
    NetBiosName: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[       SelfManagedActiveDirectoryAttributesTypeDef     ] = None

class UpdateFileSystemWindowsConfigurationTypeDef(BaseModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    ThroughputCapacity: Optional[int] = None
    SelfManagedActiveDirectoryConfiguration: Optional[       SelfManagedActiveDirectoryConfigurationUpdatesTypeDef     ] = None
    AuditLogConfiguration: Optional[WindowsAuditLogCreateConfigurationTypeDef] = None
    DiskIopsConfiguration: Optional[DiskIopsConfigurationTypeDef] = None

class UpdateSvmActiveDirectoryConfigurationTypeDef(BaseModel):
    SelfManagedActiveDirectoryConfiguration: Optional[       SelfManagedActiveDirectoryConfigurationUpdatesTypeDef     ] = None
    NetBiosName: Optional[str] = None

class SvmEndpointsTypeDef(BaseModel):
    Iscsi: Optional[SvmEndpointTypeDef] = None
    Management: Optional[SvmEndpointTypeDef] = None
    Nfs: Optional[SvmEndpointTypeDef] = None
    Smb: Optional[SvmEndpointTypeDef] = None

class UpdateFileCacheRequestRequestTypeDef(BaseModel):
    FileCacheId: str
    ClientRequestToken: Optional[str] = None
    LustreConfiguration: Optional[UpdateFileCacheLustreConfigurationTypeDef] = None

class UpdateFileSystemLustreConfigurationTypeDef(BaseModel):
    WeeklyMaintenanceStartTime: Optional[str] = None
    DailyAutomaticBackupStartTime: Optional[str] = None
    AutomaticBackupRetentionDays: Optional[int] = None
    AutoImportPolicy: Optional[AutoImportPolicyTypeType] = None
    DataCompressionType: Optional[DataCompressionTypeType] = None
    LogConfiguration: Optional[LustreLogCreateConfigurationTypeDef] = None
    RootSquashConfiguration: Optional[LustreRootSquashConfigurationTypeDef] = None
    PerUnitStorageThroughput: Optional[int] = None
    MetadataConfiguration: Optional[UpdateFileSystemLustreMetadataConfigurationTypeDef] = None

class WindowsFileSystemConfigurationTypeDef(BaseModel):
    ActiveDirectoryId: Optional[str] = None
    SelfManagedActiveDirectoryConfiguration: Optional[       SelfManagedActiveDirectoryAttributesTypeDef     ] = None
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

class DataRepositoryAssociationTypeDef(BaseModel):
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

class CreateDataRepositoryAssociationRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    DataRepositoryPath: str
    FileSystemPath: Optional[str] = None
    BatchImportMetaDataOnCreate: Optional[bool] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDataRepositoryAssociationRequestRequestTypeDef(BaseModel):
    AssociationId: str
    ClientRequestToken: Optional[str] = None
    ImportedFileChunkSize: Optional[int] = None
    S3: Optional[S3DataRepositoryConfigurationTypeDef] = None

class DeleteFileSystemRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    WindowsConfiguration: Optional[DeleteFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[DeleteFileSystemLustreConfigurationTypeDef] = None
    OpenZFSConfiguration: Optional[DeleteFileSystemOpenZFSConfigurationTypeDef] = None

class DeleteFileSystemResponseTypeDef(BaseModel):
    FileSystemId: str
    Lifecycle: FileSystemLifecycleType
    WindowsResponse: DeleteFileSystemWindowsResponseTypeDef
    LustreResponse: DeleteFileSystemLustreResponseTypeDef
    OpenZFSResponse: DeleteFileSystemOpenZFSResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[DeleteVolumeOntapConfigurationTypeDef] = None
    OpenZFSConfiguration: Optional[DeleteVolumeOpenZFSConfigurationTypeDef] = None

class DeleteVolumeResponseTypeDef(BaseModel):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    OntapResponse: DeleteVolumeOntapResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageVirtualMachineRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    Name: str
    ActiveDirectoryConfiguration: Optional[CreateSvmActiveDirectoryConfigurationTypeDef] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    RootVolumeSecurityStyle: Optional[StorageVirtualMachineRootVolumeSecurityStyleType] = None

class LustreFileSystemConfigurationTypeDef(BaseModel):
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

class CreateDataRepositoryTaskRequestRequestTypeDef(BaseModel):
    Type: DataRepositoryTaskTypeType
    FileSystemId: str
    Report: CompletionReportTypeDef
    Paths: Optional[Sequence[str]] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CapacityToRelease: Optional[int] = None
    ReleaseConfiguration: Optional[ReleaseConfigurationTypeDef] = None

class DataRepositoryTaskTypeDef(BaseModel):
    TaskId: str
    Lifecycle: DataRepositoryTaskLifecycleType
    Type: DataRepositoryTaskTypeType
    CreationTime: datetime
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    FileSystemId: Optional[str] = None
    Paths: Optional[List[str]] = None
    FailureDetails: Optional[DataRepositoryTaskFailureDetailsTypeDef] = None
    Status: Optional[DataRepositoryTaskStatusTypeDef] = None
    Report: Optional[CompletionReportTypeDef] = None
    CapacityToRelease: Optional[int] = None
    FileCacheId: Optional[str] = None
    ReleaseConfiguration: Optional[ReleaseConfigurationTypeDef] = None

class CreateFileCacheRequestRequestTypeDef(BaseModel):
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
    DataRepositoryAssociations: Optional[       Sequence[FileCacheDataRepositoryAssociationTypeDef]     ] = None

class FileCacheCreatingTypeDef(BaseModel):
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

class FileCacheTypeDef(BaseModel):
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

class OntapFileSystemConfigurationTypeDef(BaseModel):
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

class CreateSnapshotResponseTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotsResponseTypeDef(BaseModel):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSnapshotResponseTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OpenZFSVolumeConfigurationTypeDef(BaseModel):
    ParentVolumeId: Optional[str] = None
    VolumePath: Optional[str] = None
    StorageCapacityReservationGiB: Optional[int] = None
    StorageCapacityQuotaGiB: Optional[int] = None
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    CopyTagsToSnapshots: Optional[bool] = None
    OriginSnapshot: Optional[OpenZFSOriginSnapshotConfigurationTypeDef] = None
    ReadOnly: Optional[bool] = None
    NfsExports: Optional[List[OpenZFSNfsExportOutputTypeDef]] = None
    UserAndGroupQuotas: Optional[List[OpenZFSUserOrGroupQuotaTypeDef]] = None
    RestoreToSnapshot: Optional[str] = None
    DeleteIntermediateSnaphots: Optional[bool] = None
    DeleteClonedVolumes: Optional[bool] = None
    DeleteIntermediateData: Optional[bool] = None
    SourceSnapshotARN: Optional[str] = None
    DestinationSnapshot: Optional[str] = None
    CopyStrategy: Optional[OpenZFSCopyStrategyType] = None

class CreateOpenZFSVolumeConfigurationTypeDef(BaseModel):
    ParentVolumeId: str
    StorageCapacityReservationGiB: Optional[int] = None
    StorageCapacityQuotaGiB: Optional[int] = None
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    CopyTagsToSnapshots: Optional[bool] = None
    OriginSnapshot: Optional[CreateOpenZFSOriginSnapshotConfigurationTypeDef] = None
    ReadOnly: Optional[bool] = None
    NfsExports: Optional[Sequence[OpenZFSNfsExportTypeDef]] = None
    UserAndGroupQuotas: Optional[Sequence[OpenZFSUserOrGroupQuotaTypeDef]] = None

class OpenZFSCreateRootVolumeConfigurationTypeDef(BaseModel):
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    NfsExports: Optional[Sequence[OpenZFSNfsExportTypeDef]] = None
    UserAndGroupQuotas: Optional[Sequence[OpenZFSUserOrGroupQuotaTypeDef]] = None
    CopyTagsToSnapshots: Optional[bool] = None
    ReadOnly: Optional[bool] = None

class UpdateOpenZFSVolumeConfigurationTypeDef(BaseModel):
    StorageCapacityReservationGiB: Optional[int] = None
    StorageCapacityQuotaGiB: Optional[int] = None
    RecordSizeKiB: Optional[int] = None
    DataCompressionType: Optional[OpenZFSDataCompressionTypeType] = None
    NfsExports: Optional[Sequence[OpenZFSNfsExportTypeDef]] = None
    UserAndGroupQuotas: Optional[Sequence[OpenZFSUserOrGroupQuotaTypeDef]] = None
    ReadOnly: Optional[bool] = None

class CreateSnaplockConfigurationTypeDef(BaseModel):
    SnaplockType: SnaplockTypeType
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriodTypeDef] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriodTypeDef] = None
    VolumeAppendModeEnabled: Optional[bool] = None

class SnaplockConfigurationTypeDef(BaseModel):
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriodTypeDef] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriodTypeDef] = None
    SnaplockType: Optional[SnaplockTypeType] = None
    VolumeAppendModeEnabled: Optional[bool] = None

class UpdateSnaplockConfigurationTypeDef(BaseModel):
    AuditLogVolume: Optional[bool] = None
    AutocommitPeriod: Optional[AutocommitPeriodTypeDef] = None
    PrivilegedDelete: Optional[PrivilegedDeleteType] = None
    RetentionPeriod: Optional[SnaplockRetentionPeriodTypeDef] = None
    VolumeAppendModeEnabled: Optional[bool] = None

class UpdateStorageVirtualMachineRequestRequestTypeDef(BaseModel):
    StorageVirtualMachineId: str
    ActiveDirectoryConfiguration: Optional[UpdateSvmActiveDirectoryConfigurationTypeDef] = None
    ClientRequestToken: Optional[str] = None
    SvmAdminPassword: Optional[str] = None

class StorageVirtualMachineTypeDef(BaseModel):
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

class UpdateFileSystemRequestRequestTypeDef(BaseModel):
    FileSystemId: str
    ClientRequestToken: Optional[str] = None
    StorageCapacity: Optional[int] = None
    WindowsConfiguration: Optional[UpdateFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[UpdateFileSystemLustreConfigurationTypeDef] = None
    OntapConfiguration: Optional[UpdateFileSystemOntapConfigurationTypeDef] = None
    OpenZFSConfiguration: Optional[UpdateFileSystemOpenZFSConfigurationTypeDef] = None
    StorageType: Optional[StorageTypeType] = None

class CreateDataRepositoryAssociationResponseTypeDef(BaseModel):
    Association: DataRepositoryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataRepositoryAssociationsResponseTypeDef(BaseModel):
    Associations: List[DataRepositoryAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateDataRepositoryAssociationResponseTypeDef(BaseModel):
    Association: DataRepositoryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataRepositoryTaskResponseTypeDef(BaseModel):
    DataRepositoryTask: DataRepositoryTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataRepositoryTasksResponseTypeDef(BaseModel):
    DataRepositoryTasks: List[DataRepositoryTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateFileCacheResponseTypeDef(BaseModel):
    FileCache: FileCacheCreatingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFileCachesResponseTypeDef(BaseModel):
    FileCaches: List[FileCacheTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateFileCacheResponseTypeDef(BaseModel):
    FileCache: FileCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemTypeDef(BaseModel):
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
    AdministrativeActions: Optional[List["AdministrativeActionTypeDef"]] = None
    OntapConfiguration: Optional[OntapFileSystemConfigurationTypeDef] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[OpenZFSFileSystemConfigurationTypeDef] = None

class CreateFileSystemOpenZFSConfigurationTypeDef(BaseModel):
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

class CreateOntapVolumeConfigurationTypeDef(BaseModel):
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

class OntapVolumeConfigurationTypeDef(BaseModel):
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

class UpdateOntapVolumeConfigurationTypeDef(BaseModel):
    JunctionPath: Optional[str] = None
    SecurityStyle: Optional[SecurityStyleType] = None
    SizeInMegabytes: Optional[int] = None
    StorageEfficiencyEnabled: Optional[bool] = None
    TieringPolicy: Optional[TieringPolicyTypeDef] = None
    SnapshotPolicy: Optional[str] = None
    CopyTagsToBackups: Optional[bool] = None
    SnaplockConfiguration: Optional[UpdateSnaplockConfigurationTypeDef] = None
    SizeInBytes: Optional[int] = None

class CreateStorageVirtualMachineResponseTypeDef(BaseModel):
    StorageVirtualMachine: StorageVirtualMachineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorageVirtualMachinesResponseTypeDef(BaseModel):
    StorageVirtualMachines: List[StorageVirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateStorageVirtualMachineResponseTypeDef(BaseModel):
    StorageVirtualMachine: StorageVirtualMachineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemFromBackupRequestRequestTypeDef(BaseModel):
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

class CreateFileSystemRequestRequestTypeDef(BaseModel):
    FileSystemType: FileSystemTypeType
    StorageCapacity: int
    SubnetIds: Sequence[str]
    ClientRequestToken: Optional[str] = None
    StorageType: Optional[StorageTypeType] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    WindowsConfiguration: Optional[CreateFileSystemWindowsConfigurationTypeDef] = None
    LustreConfiguration: Optional[CreateFileSystemLustreConfigurationTypeDef] = None
    OntapConfiguration: Optional[CreateFileSystemOntapConfigurationTypeDef] = None
    FileSystemTypeVersion: Optional[str] = None
    OpenZFSConfiguration: Optional[CreateFileSystemOpenZFSConfigurationTypeDef] = None

class CreateVolumeFromBackupRequestRequestTypeDef(BaseModel):
    BackupId: str
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVolumeRequestRequestTypeDef(BaseModel):
    VolumeType: VolumeTypeType
    Name: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[CreateOntapVolumeConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OpenZFSConfiguration: Optional[CreateOpenZFSVolumeConfigurationTypeDef] = None

class VolumeTypeDef(BaseModel):
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
    AdministrativeActions: Optional[List["AdministrativeActionTypeDef"]] = None
    OpenZFSConfiguration: Optional[OpenZFSVolumeConfigurationTypeDef] = None

class UpdateVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    ClientRequestToken: Optional[str] = None
    OntapConfiguration: Optional[UpdateOntapVolumeConfigurationTypeDef] = None
    Name: Optional[str] = None
    OpenZFSConfiguration: Optional[UpdateOpenZFSVolumeConfigurationTypeDef] = None

class AdministrativeActionTypeDef(BaseModel):
    AdministrativeActionType: Optional[AdministrativeActionTypeType] = None
    ProgressPercent: Optional[int] = None
    RequestTime: Optional[datetime] = None
    Status: Optional[StatusType] = None
    TargetFileSystemValues: Optional[Dict[str, Any]] = None
    FailureDetails: Optional[AdministrativeActionFailureDetailsTypeDef] = None
    TargetVolumeValues: Optional[Dict[str, Any]] = None
    TargetSnapshotValues: Optional[Dict[str, Any]] = None
    TotalTransferBytes: Optional[int] = None
    RemainingTransferBytes: Optional[int] = None

class BackupTypeDef(BaseModel):
    BackupId: str
    Lifecycle: BackupLifecycleType
    Type: BackupTypeType
    CreationTime: datetime
    FileSystem: "FileSystemTypeDef"
    FailureDetails: Optional[BackupFailureDetailsTypeDef] = None
    ProgressPercent: Optional[int] = None
    KmsKeyId: Optional[str] = None
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    DirectoryInformation: Optional[ActiveDirectoryBackupAttributesTypeDef] = None
    OwnerId: Optional[str] = None
    SourceBackupId: Optional[str] = None
    SourceBackupRegion: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    Volume: Optional[VolumeTypeDef] = None

class CreateVolumeFromBackupResponseTypeDef(BaseModel):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVolumeResponseTypeDef(BaseModel):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVolumesResponseTypeDef(BaseModel):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateVolumeResponseTypeDef(BaseModel):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyBackupResponseTypeDef(BaseModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupResponseTypeDef(BaseModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(BaseModel):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

