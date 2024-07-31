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
from aws_resource_validator.pydantic_models.datasync_constants import *

class CredentialsTypeDef(BaseModel):
    Username: str
    Password: str

class DiscoveryServerConfigurationTypeDef(BaseModel):
    ServerHostname: str
    ServerPort: Optional[int] = None

class TagListEntryTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class PlatformTypeDef(BaseModel):
    Version: Optional[str] = None

class AzureBlobSasConfigurationTypeDef(BaseModel):
    Token: str

class CancelTaskExecutionRequestRequestTypeDef(BaseModel):
    TaskExecutionArn: str

class CapacityTypeDef(BaseModel):
    Used: Optional[int] = None
    Provisioned: Optional[int] = None
    LogicalUsed: Optional[int] = None
    ClusterCloudStorageUsed: Optional[int] = None

class Ec2ConfigTypeDef(BaseModel):
    SubnetArn: str
    SecurityGroupArns: Sequence[str]

class HdfsNameNodeTypeDef(BaseModel):
    Hostname: str
    Port: int

class QopConfigurationTypeDef(BaseModel):
    RpcProtection: Optional[HdfsRpcProtectionType] = None
    DataTransferProtection: Optional[HdfsDataTransferProtectionType] = None

class NfsMountOptionsTypeDef(BaseModel):
    Version: Optional[NfsVersionType] = None

class OnPremConfigTypeDef(BaseModel):
    AgentArns: Sequence[str]

class S3ConfigTypeDef(BaseModel):
    BucketAccessRoleArn: str

class SmbMountOptionsTypeDef(BaseModel):
    Version: Optional[SmbVersionType] = None

class FilterRuleTypeDef(BaseModel):
    FilterType: Optional[Literal["SIMPLE_PATTERN"]] = None
    Value: Optional[str] = None

class OptionsTypeDef(BaseModel):
    VerifyMode: Optional[VerifyModeType] = None
    OverwriteMode: Optional[OverwriteModeType] = None
    Atime: Optional[AtimeType] = None
    Mtime: Optional[MtimeType] = None
    Uid: Optional[UidType] = None
    Gid: Optional[GidType] = None
    PreserveDeletedFiles: Optional[PreserveDeletedFilesType] = None
    PreserveDevices: Optional[PreserveDevicesType] = None
    PosixPermissions: Optional[PosixPermissionsType] = None
    BytesPerSecond: Optional[int] = None
    TaskQueueing: Optional[TaskQueueingType] = None
    LogLevel: Optional[LogLevelType] = None
    TransferMode: Optional[TransferModeType] = None
    SecurityDescriptorCopyFlags: Optional[SmbSecurityDescriptorCopyFlagsType] = None
    ObjectTags: Optional[ObjectTagsType] = None

class TaskScheduleTypeDef(BaseModel):
    ScheduleExpression: str
    Status: Optional[ScheduleStatusType] = None

class DeleteAgentRequestRequestTypeDef(BaseModel):
    AgentArn: str

class DeleteLocationRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DeleteTaskRequestRequestTypeDef(BaseModel):
    TaskArn: str

class DescribeAgentRequestRequestTypeDef(BaseModel):
    AgentArn: str

class PrivateLinkConfigTypeDef(BaseModel):
    VpcEndpointId: Optional[str] = None
    PrivateLinkEndpoint: Optional[str] = None
    SubnetArns: Optional[List[str]] = None
    SecurityGroupArns: Optional[List[str]] = None

class DescribeDiscoveryJobRequestRequestTypeDef(BaseModel):
    DiscoveryJobArn: str

class DescribeLocationAzureBlobRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationEfsRequestRequestTypeDef(BaseModel):
    LocationArn: str

class Ec2ConfigOutputTypeDef(BaseModel):
    SubnetArn: str
    SecurityGroupArns: List[str]

class DescribeLocationFsxLustreRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationFsxOntapRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationFsxOpenZfsRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationFsxWindowsRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationHdfsRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationNfsRequestRequestTypeDef(BaseModel):
    LocationArn: str

class OnPremConfigOutputTypeDef(BaseModel):
    AgentArns: List[str]

class DescribeLocationObjectStorageRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationS3RequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeLocationSmbRequestRequestTypeDef(BaseModel):
    LocationArn: str

class DescribeStorageSystemRequestRequestTypeDef(BaseModel):
    StorageSystemArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeStorageSystemResourcesRequestRequestTypeDef(BaseModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceIds: Optional[Sequence[str]] = None
    Filter: Optional[Mapping[Literal["SVM"], Sequence[str]]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTaskExecutionRequestRequestTypeDef(BaseModel):
    TaskExecutionArn: str

class ReportResultTypeDef(BaseModel):
    Status: Optional[PhaseStatusType] = None
    ErrorCode: Optional[str] = None
    ErrorDetail: Optional[str] = None

class TaskExecutionResultDetailTypeDef(BaseModel):
    PrepareDuration: Optional[int] = None
    PrepareStatus: Optional[PhaseStatusType] = None
    TotalDuration: Optional[int] = None
    TransferDuration: Optional[int] = None
    TransferStatus: Optional[PhaseStatusType] = None
    VerifyDuration: Optional[int] = None
    VerifyStatus: Optional[PhaseStatusType] = None
    ErrorCode: Optional[str] = None
    ErrorDetail: Optional[str] = None

class DescribeTaskRequestRequestTypeDef(BaseModel):
    TaskArn: str

class TaskScheduleDetailsTypeDef(BaseModel):
    StatusUpdateTime: Optional[datetime] = None
    DisabledReason: Optional[str] = None
    DisabledBy: Optional[ScheduleDisabledByType] = None

class DiscoveryJobListEntryTypeDef(BaseModel):
    DiscoveryJobArn: Optional[str] = None
    Status: Optional[DiscoveryJobStatusType] = None

class GenerateRecommendationsRequestRequestTypeDef(BaseModel):
    DiscoveryJobArn: str
    ResourceIds: Sequence[str]
    ResourceType: DiscoveryResourceTypeType

class IOPSTypeDef(BaseModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None
    Total: Optional[float] = None

class LatencyTypeDef(BaseModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None

class ListAgentsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDiscoveryJobsRequestRequestTypeDef(BaseModel):
    StorageSystemArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LocationFilterTypeDef(BaseModel):
    Name: LocationFilterNameType
    Values: Sequence[str]
    Operator: OperatorType

class LocationListEntryTypeDef(BaseModel):
    LocationArn: Optional[str] = None
    LocationUri: Optional[str] = None

class ListStorageSystemsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StorageSystemListEntryTypeDef(BaseModel):
    StorageSystemArn: Optional[str] = None
    Name: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTaskExecutionsRequestRequestTypeDef(BaseModel):
    TaskArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TaskExecutionListEntryTypeDef(BaseModel):
    TaskExecutionArn: Optional[str] = None
    Status: Optional[TaskExecutionStatusType] = None

class TaskFilterTypeDef(BaseModel):
    Name: TaskFilterNameType
    Values: Sequence[str]
    Operator: OperatorType

class TaskListEntryTypeDef(BaseModel):
    TaskArn: Optional[str] = None
    Status: Optional[TaskStatusType] = None
    Name: Optional[str] = None

class MaxP95PerformanceTypeDef(BaseModel):
    IopsRead: Optional[float] = None
    IopsWrite: Optional[float] = None
    IopsOther: Optional[float] = None
    IopsTotal: Optional[float] = None
    ThroughputRead: Optional[float] = None
    ThroughputWrite: Optional[float] = None
    ThroughputOther: Optional[float] = None
    ThroughputTotal: Optional[float] = None
    LatencyRead: Optional[float] = None
    LatencyWrite: Optional[float] = None
    LatencyOther: Optional[float] = None

class RecommendationTypeDef(BaseModel):
    StorageType: Optional[str] = None
    StorageConfiguration: Optional[Dict[str, str]] = None
    EstimatedMonthlyStorageCost: Optional[str] = None

class ThroughputTypeDef(BaseModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None
    Total: Optional[float] = None

class RemoveStorageSystemRequestRequestTypeDef(BaseModel):
    StorageSystemArn: str

class ReportDestinationS3TypeDef(BaseModel):
    S3BucketArn: str
    BucketAccessRoleArn: str
    Subdirectory: Optional[str] = None

class ReportOverrideTypeDef(BaseModel):
    ReportLevel: Optional[ReportLevelType] = None

class S3ManifestConfigTypeDef(BaseModel):
    ManifestObjectPath: str
    BucketAccessRoleArn: str
    S3BucketArn: str
    ManifestObjectVersionId: Optional[str] = None

class StopDiscoveryJobRequestRequestTypeDef(BaseModel):
    DiscoveryJobArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Keys: Sequence[str]

class UpdateAgentRequestRequestTypeDef(BaseModel):
    AgentArn: str
    Name: Optional[str] = None

class UpdateDiscoveryJobRequestRequestTypeDef(BaseModel):
    DiscoveryJobArn: str
    CollectionDurationMinutes: int

class UpdateStorageSystemRequestRequestTypeDef(BaseModel):
    StorageSystemArn: str
    ServerConfiguration: Optional[DiscoveryServerConfigurationTypeDef] = None
    AgentArns: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Credentials: Optional[CredentialsTypeDef] = None

class AddStorageSystemRequestRequestTypeDef(BaseModel):
    ServerConfiguration: DiscoveryServerConfigurationTypeDef
    SystemType: Literal["NetAppONTAP"]
    AgentArns: Sequence[str]
    ClientToken: str
    Credentials: CredentialsTypeDef
    CloudWatchLogGroupArn: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    Name: Optional[str] = None

class CreateAgentRequestRequestTypeDef(BaseModel):
    ActivationKey: str
    AgentName: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    VpcEndpointId: Optional[str] = None
    SubnetArns: Optional[Sequence[str]] = None
    SecurityGroupArns: Optional[Sequence[str]] = None

class CreateLocationFsxLustreRequestRequestTypeDef(BaseModel):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class CreateLocationFsxWindowsRequestRequestTypeDef(BaseModel):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    User: str
    Password: str
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    Domain: Optional[str] = None

class StartDiscoveryJobRequestRequestTypeDef(BaseModel):
    StorageSystemArn: str
    CollectionDurationMinutes: int
    ClientToken: str
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagListEntryTypeDef]

class AddStorageSystemResponseTypeDef(BaseModel):
    StorageSystemArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentResponseTypeDef(BaseModel):
    AgentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationAzureBlobResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationEfsResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxLustreResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxOntapResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxOpenZfsResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxWindowsResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationHdfsResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationNfsResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationObjectStorageResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationS3ResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationSmbResponseTypeDef(BaseModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskResponseTypeDef(BaseModel):
    TaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDiscoveryJobResponseTypeDef(BaseModel):
    StorageSystemArn: str
    DiscoveryJobArn: str
    CollectionDurationMinutes: int
    Status: DiscoveryJobStatusType
    JobStartTime: datetime
    JobEndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationAzureBlobResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    AuthenticationType: Literal["SAS"]
    BlobType: Literal["BLOCK"]
    AccessTier: AzureAccessTierType
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxLustreResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxWindowsResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    User: str
    Domain: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationObjectStorageResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    AccessKey: str
    ServerPort: int
    ServerProtocol: ObjectStorageServerProtocolType
    AgentArns: List[str]
    CreationTime: datetime
    ServerCertificate: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorageSystemResponseTypeDef(BaseModel):
    StorageSystemArn: str
    ServerConfiguration: DiscoveryServerConfigurationTypeDef
    SystemType: Literal["NetAppONTAP"]
    AgentArns: List[str]
    Name: str
    ErrorMessage: str
    ConnectivityStatus: StorageSystemConnectivityStatusType
    CloudWatchLogGroupArn: str
    CreationTime: datetime
    SecretsManagerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartDiscoveryJobResponseTypeDef(BaseModel):
    DiscoveryJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskExecutionResponseTypeDef(BaseModel):
    TaskExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AgentListEntryTypeDef(BaseModel):
    AgentArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AgentStatusType] = None
    Platform: Optional[PlatformTypeDef] = None

class CreateLocationAzureBlobRequestRequestTypeDef(BaseModel):
    ContainerUrl: str
    AuthenticationType: Literal["SAS"]
    AgentArns: Sequence[str]
    SasConfiguration: Optional[AzureBlobSasConfigurationTypeDef] = None
    BlobType: Optional[Literal["BLOCK"]] = None
    AccessTier: Optional[AzureAccessTierType] = None
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class UpdateLocationAzureBlobRequestRequestTypeDef(BaseModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    AuthenticationType: Optional[Literal["SAS"]] = None
    SasConfiguration: Optional[AzureBlobSasConfigurationTypeDef] = None
    BlobType: Optional[Literal["BLOCK"]] = None
    AccessTier: Optional[AzureAccessTierType] = None
    AgentArns: Optional[Sequence[str]] = None

class CreateLocationObjectStorageRequestRequestTypeDef(BaseModel):
    ServerHostname: str
    BucketName: str
    AgentArns: Sequence[str]
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    ServerCertificate: Optional[BlobTypeDef] = None

class UpdateLocationObjectStorageRequestRequestTypeDef(BaseModel):
    LocationArn: str
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    AgentArns: Optional[Sequence[str]] = None
    ServerCertificate: Optional[BlobTypeDef] = None

class CreateLocationEfsRequestRequestTypeDef(BaseModel):
    EfsFilesystemArn: str
    Ec2Config: Ec2ConfigTypeDef
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    AccessPointArn: Optional[str] = None
    FileSystemAccessRoleArn: Optional[str] = None
    InTransitEncryption: Optional[EfsInTransitEncryptionType] = None

class CreateLocationHdfsRequestRequestTypeDef(BaseModel):
    NameNodes: Sequence[HdfsNameNodeTypeDef]
    AuthenticationType: HdfsAuthenticationTypeType
    AgentArns: Sequence[str]
    Subdirectory: Optional[str] = None
    BlockSize: Optional[int] = None
    ReplicationFactor: Optional[int] = None
    KmsKeyProviderUri: Optional[str] = None
    QopConfiguration: Optional[QopConfigurationTypeDef] = None
    SimpleUser: Optional[str] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[BlobTypeDef] = None
    KerberosKrb5Conf: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationHdfsResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    NameNodes: List[HdfsNameNodeTypeDef]
    BlockSize: int
    ReplicationFactor: int
    KmsKeyProviderUri: str
    QopConfiguration: QopConfigurationTypeDef
    AuthenticationType: HdfsAuthenticationTypeType
    SimpleUser: str
    KerberosPrincipal: str
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLocationHdfsRequestRequestTypeDef(BaseModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    NameNodes: Optional[Sequence[HdfsNameNodeTypeDef]] = None
    BlockSize: Optional[int] = None
    ReplicationFactor: Optional[int] = None
    KmsKeyProviderUri: Optional[str] = None
    QopConfiguration: Optional[QopConfigurationTypeDef] = None
    AuthenticationType: Optional[HdfsAuthenticationTypeType] = None
    SimpleUser: Optional[str] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[BlobTypeDef] = None
    KerberosKrb5Conf: Optional[BlobTypeDef] = None
    AgentArns: Optional[Sequence[str]] = None

class FsxProtocolNfsTypeDef(BaseModel):
    MountOptions: Optional[NfsMountOptionsTypeDef] = None

class CreateLocationNfsRequestRequestTypeDef(BaseModel):
    Subdirectory: str
    ServerHostname: str
    OnPremConfig: OnPremConfigTypeDef
    MountOptions: Optional[NfsMountOptionsTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class UpdateLocationNfsRequestRequestTypeDef(BaseModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    OnPremConfig: Optional[OnPremConfigTypeDef] = None
    MountOptions: Optional[NfsMountOptionsTypeDef] = None

class CreateLocationS3RequestRequestTypeDef(BaseModel):
    S3BucketArn: str
    S3Config: S3ConfigTypeDef
    Subdirectory: Optional[str] = None
    S3StorageClass: Optional[S3StorageClassType] = None
    AgentArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationS3ResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    S3StorageClass: S3StorageClassType
    S3Config: S3ConfigTypeDef
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationSmbRequestRequestTypeDef(BaseModel):
    Subdirectory: str
    ServerHostname: str
    User: str
    Password: str
    AgentArns: Sequence[str]
    Domain: Optional[str] = None
    MountOptions: Optional[SmbMountOptionsTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationSmbResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    AgentArns: List[str]
    User: str
    Domain: str
    MountOptions: SmbMountOptionsTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class FsxProtocolSmbTypeDef(BaseModel):
    Password: str
    User: str
    Domain: Optional[str] = None
    MountOptions: Optional[SmbMountOptionsTypeDef] = None

class UpdateLocationSmbRequestRequestTypeDef(BaseModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    User: Optional[str] = None
    Domain: Optional[str] = None
    Password: Optional[str] = None
    AgentArns: Optional[Sequence[str]] = None
    MountOptions: Optional[SmbMountOptionsTypeDef] = None

class UpdateTaskExecutionRequestRequestTypeDef(BaseModel):
    TaskExecutionArn: str
    Options: OptionsTypeDef

class DescribeAgentResponseTypeDef(BaseModel):
    AgentArn: str
    Name: str
    Status: AgentStatusType
    LastConnectionTime: datetime
    CreationTime: datetime
    EndpointType: EndpointTypeType
    PrivateLinkConfig: PrivateLinkConfigTypeDef
    Platform: PlatformTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationEfsResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    Ec2Config: Ec2ConfigOutputTypeDef
    CreationTime: datetime
    AccessPointArn: str
    FileSystemAccessRoleArn: str
    InTransitEncryption: EfsInTransitEncryptionType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationNfsResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    OnPremConfig: OnPremConfigOutputTypeDef
    MountOptions: NfsMountOptionsTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentsRequestListAgentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDiscoveryJobsRequestListDiscoveryJobsPaginateTypeDef(BaseModel):
    StorageSystemArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStorageSystemsRequestListStorageSystemsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTaskExecutionsRequestListTaskExecutionsPaginateTypeDef(BaseModel):
    TaskArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef(BaseModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStorageSystemResourceMetricsRequestRequestTypeDef(BaseModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDiscoveryJobsResponseTypeDef(BaseModel):
    DiscoveryJobs: List[DiscoveryJobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLocationsRequestListLocationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[LocationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLocationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[LocationFilterTypeDef]] = None

class ListLocationsResponseTypeDef(BaseModel):
    Locations: List[LocationListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStorageSystemsResponseTypeDef(BaseModel):
    StorageSystems: List[StorageSystemListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTaskExecutionsResponseTypeDef(BaseModel):
    TaskExecutions: List[TaskExecutionListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTasksRequestListTasksPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[TaskFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[TaskFilterTypeDef]] = None

class ListTasksResponseTypeDef(BaseModel):
    Tasks: List[TaskListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetAppONTAPClusterTypeDef(BaseModel):
    CifsShareCount: Optional[int] = None
    NfsExportedVolumes: Optional[int] = None
    ResourceId: Optional[str] = None
    ClusterName: Optional[str] = None
    MaxP95Performance: Optional[MaxP95PerformanceTypeDef] = None
    ClusterBlockStorageSize: Optional[int] = None
    ClusterBlockStorageUsed: Optional[int] = None
    ClusterBlockStorageLogicalUsed: Optional[int] = None
    Recommendations: Optional[List[RecommendationTypeDef]] = None
    RecommendationStatus: Optional[RecommendationStatusType] = None
    LunCount: Optional[int] = None
    ClusterCloudStorageUsed: Optional[int] = None

class NetAppONTAPSVMTypeDef(BaseModel):
    ClusterUuid: Optional[str] = None
    ResourceId: Optional[str] = None
    SvmName: Optional[str] = None
    CifsShareCount: Optional[int] = None
    EnabledProtocols: Optional[List[str]] = None
    TotalCapacityUsed: Optional[int] = None
    TotalCapacityProvisioned: Optional[int] = None
    TotalLogicalCapacityUsed: Optional[int] = None
    MaxP95Performance: Optional[MaxP95PerformanceTypeDef] = None
    Recommendations: Optional[List[RecommendationTypeDef]] = None
    NfsExportedVolumes: Optional[int] = None
    RecommendationStatus: Optional[RecommendationStatusType] = None
    TotalSnapshotCapacityUsed: Optional[int] = None
    LunCount: Optional[int] = None

class NetAppONTAPVolumeTypeDef(BaseModel):
    VolumeName: Optional[str] = None
    ResourceId: Optional[str] = None
    CifsShareCount: Optional[int] = None
    SecurityStyle: Optional[str] = None
    SvmUuid: Optional[str] = None
    SvmName: Optional[str] = None
    CapacityUsed: Optional[int] = None
    CapacityProvisioned: Optional[int] = None
    LogicalCapacityUsed: Optional[int] = None
    NfsExported: Optional[bool] = None
    SnapshotCapacityUsed: Optional[int] = None
    MaxP95Performance: Optional[MaxP95PerformanceTypeDef] = None
    Recommendations: Optional[List[RecommendationTypeDef]] = None
    RecommendationStatus: Optional[RecommendationStatusType] = None
    LunCount: Optional[int] = None

class P95MetricsTypeDef(BaseModel):
    IOPS: Optional[IOPSTypeDef] = None
    Throughput: Optional[ThroughputTypeDef] = None
    Latency: Optional[LatencyTypeDef] = None

class ReportDestinationTypeDef(BaseModel):
    S3: Optional[ReportDestinationS3TypeDef] = None

class ReportOverridesTypeDef(BaseModel):
    Transferred: Optional[ReportOverrideTypeDef] = None
    Verified: Optional[ReportOverrideTypeDef] = None
    Deleted: Optional[ReportOverrideTypeDef] = None
    Skipped: Optional[ReportOverrideTypeDef] = None

class SourceManifestConfigTypeDef(BaseModel):
    S3: S3ManifestConfigTypeDef

class ListAgentsResponseTypeDef(BaseModel):
    Agents: List[AgentListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FsxProtocolTypeDef(BaseModel):
    NFS: Optional[FsxProtocolNfsTypeDef] = None
    SMB: Optional[FsxProtocolSmbTypeDef] = None

class ResourceDetailsTypeDef(BaseModel):
    NetAppONTAPSVMs: Optional[List[NetAppONTAPSVMTypeDef]] = None
    NetAppONTAPVolumes: Optional[List[NetAppONTAPVolumeTypeDef]] = None
    NetAppONTAPClusters: Optional[List[NetAppONTAPClusterTypeDef]] = None

class ResourceMetricsTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    P95Metrics: Optional[P95MetricsTypeDef] = None
    Capacity: Optional[CapacityTypeDef] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[DiscoveryResourceTypeType] = None

class TaskReportConfigTypeDef(BaseModel):
    Destination: Optional[ReportDestinationTypeDef] = None
    OutputType: Optional[ReportOutputTypeType] = None
    ReportLevel: Optional[ReportLevelType] = None
    ObjectVersionIds: Optional[ObjectVersionIdsType] = None
    Overrides: Optional[ReportOverridesTypeDef] = None

class ManifestConfigTypeDef(BaseModel):
    Action: Optional[Literal["TRANSFER"]] = None
    Format: Optional[Literal["CSV"]] = None
    Source: Optional[SourceManifestConfigTypeDef] = None

class CreateLocationFsxOntapRequestRequestTypeDef(BaseModel):
    Protocol: FsxProtocolTypeDef
    SecurityGroupArns: Sequence[str]
    StorageVirtualMachineArn: str
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class CreateLocationFsxOpenZfsRequestRequestTypeDef(BaseModel):
    FsxFilesystemArn: str
    Protocol: FsxProtocolTypeDef
    SecurityGroupArns: Sequence[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationFsxOntapResponseTypeDef(BaseModel):
    CreationTime: datetime
    LocationArn: str
    LocationUri: str
    Protocol: FsxProtocolTypeDef
    SecurityGroupArns: List[str]
    StorageVirtualMachineArn: str
    FsxFilesystemArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxOpenZfsResponseTypeDef(BaseModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    Protocol: FsxProtocolTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorageSystemResourcesResponseTypeDef(BaseModel):
    ResourceDetails: ResourceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStorageSystemResourceMetricsResponseTypeDef(BaseModel):
    Metrics: List[ResourceMetricsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTaskRequestRequestTypeDef(BaseModel):
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    Options: Optional[OptionsTypeDef] = None
    Excludes: Optional[Sequence[FilterRuleTypeDef]] = None
    Schedule: Optional[TaskScheduleTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    Includes: Optional[Sequence[FilterRuleTypeDef]] = None
    ManifestConfig: Optional[ManifestConfigTypeDef] = None
    TaskReportConfig: Optional[TaskReportConfigTypeDef] = None

class DescribeTaskExecutionResponseTypeDef(BaseModel):
    TaskExecutionArn: str
    Status: TaskExecutionStatusType
    Options: OptionsTypeDef
    Excludes: List[FilterRuleTypeDef]
    Includes: List[FilterRuleTypeDef]
    ManifestConfig: ManifestConfigTypeDef
    StartTime: datetime
    EstimatedFilesToTransfer: int
    EstimatedBytesToTransfer: int
    FilesTransferred: int
    BytesWritten: int
    BytesTransferred: int
    BytesCompressed: int
    Result: TaskExecutionResultDetailTypeDef
    TaskReportConfig: TaskReportConfigTypeDef
    FilesDeleted: int
    FilesSkipped: int
    FilesVerified: int
    ReportResult: ReportResultTypeDef
    EstimatedFilesToDelete: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskResponseTypeDef(BaseModel):
    TaskArn: str
    Status: TaskStatusType
    Name: str
    CurrentTaskExecutionArn: str
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: str
    SourceNetworkInterfaceArns: List[str]
    DestinationNetworkInterfaceArns: List[str]
    Options: OptionsTypeDef
    Excludes: List[FilterRuleTypeDef]
    Schedule: TaskScheduleTypeDef
    ErrorCode: str
    ErrorDetail: str
    CreationTime: datetime
    Includes: List[FilterRuleTypeDef]
    ManifestConfig: ManifestConfigTypeDef
    TaskReportConfig: TaskReportConfigTypeDef
    ScheduleDetails: TaskScheduleDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskExecutionRequestRequestTypeDef(BaseModel):
    TaskArn: str
    OverrideOptions: Optional[OptionsTypeDef] = None
    Includes: Optional[Sequence[FilterRuleTypeDef]] = None
    Excludes: Optional[Sequence[FilterRuleTypeDef]] = None
    ManifestConfig: Optional[ManifestConfigTypeDef] = None
    TaskReportConfig: Optional[TaskReportConfigTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class UpdateTaskRequestRequestTypeDef(BaseModel):
    TaskArn: str
    Options: Optional[OptionsTypeDef] = None
    Excludes: Optional[Sequence[FilterRuleTypeDef]] = None
    Schedule: Optional[TaskScheduleTypeDef] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Includes: Optional[Sequence[FilterRuleTypeDef]] = None
    ManifestConfig: Optional[ManifestConfigTypeDef] = None
    TaskReportConfig: Optional[TaskReportConfigTypeDef] = None

