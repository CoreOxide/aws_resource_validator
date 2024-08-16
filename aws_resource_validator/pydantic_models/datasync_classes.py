from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class CredentialsTypeDef(BaseValidatorModel):
    Username: str
    Password: str

class DiscoveryServerConfigurationTypeDef(BaseValidatorModel):
    ServerHostname: str
    ServerPort: Optional[int] = None

class TagListEntryTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class PlatformTypeDef(BaseValidatorModel):
    Version: Optional[str] = None

class AzureBlobSasConfigurationTypeDef(BaseValidatorModel):
    Token: str

class CancelTaskExecutionRequestRequestTypeDef(BaseValidatorModel):
    TaskExecutionArn: str

class CapacityTypeDef(BaseValidatorModel):
    Used: Optional[int] = None
    Provisioned: Optional[int] = None
    LogicalUsed: Optional[int] = None
    ClusterCloudStorageUsed: Optional[int] = None

class Ec2ConfigTypeDef(BaseValidatorModel):
    SubnetArn: str
    SecurityGroupArns: Sequence[str]

class HdfsNameNodeTypeDef(BaseValidatorModel):
    Hostname: str
    Port: int

class QopConfigurationTypeDef(BaseValidatorModel):
    RpcProtection: Optional[HdfsRpcProtectionType] = None
    DataTransferProtection: Optional[HdfsDataTransferProtectionType] = None

class NfsMountOptionsTypeDef(BaseValidatorModel):
    Version: Optional[NfsVersionType] = None

class OnPremConfigTypeDef(BaseValidatorModel):
    AgentArns: Sequence[str]

class S3ConfigTypeDef(BaseValidatorModel):
    BucketAccessRoleArn: str

class SmbMountOptionsTypeDef(BaseValidatorModel):
    Version: Optional[SmbVersionType] = None

class FilterRuleTypeDef(BaseValidatorModel):
    FilterType: Optional[Literal["SIMPLE_PATTERN"]] = None
    Value: Optional[str] = None

class OptionsTypeDef(BaseValidatorModel):
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

class TaskScheduleTypeDef(BaseValidatorModel):
    ScheduleExpression: str
    Status: Optional[ScheduleStatusType] = None

class DeleteAgentRequestRequestTypeDef(BaseValidatorModel):
    AgentArn: str

class DeleteLocationRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DeleteTaskRequestRequestTypeDef(BaseValidatorModel):
    TaskArn: str

class DescribeAgentRequestRequestTypeDef(BaseValidatorModel):
    AgentArn: str

class PrivateLinkConfigTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    PrivateLinkEndpoint: Optional[str] = None
    SubnetArns: Optional[List[str]] = None
    SecurityGroupArns: Optional[List[str]] = None

class DescribeDiscoveryJobRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str

class DescribeLocationAzureBlobRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationEfsRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class Ec2ConfigOutputTypeDef(BaseValidatorModel):
    SubnetArn: str
    SecurityGroupArns: List[str]

class DescribeLocationFsxLustreRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationFsxOntapRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationFsxOpenZfsRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationFsxWindowsRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationHdfsRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationNfsRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class OnPremConfigOutputTypeDef(BaseValidatorModel):
    AgentArns: List[str]

class DescribeLocationObjectStorageRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationS3RequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeLocationSmbRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str

class DescribeStorageSystemRequestRequestTypeDef(BaseValidatorModel):
    StorageSystemArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeStorageSystemResourcesRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceIds: Optional[Sequence[str]] = None
    Filter: Optional[Mapping[Literal["SVM"], Sequence[str]]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTaskExecutionRequestRequestTypeDef(BaseValidatorModel):
    TaskExecutionArn: str

class ReportResultTypeDef(BaseValidatorModel):
    Status: Optional[PhaseStatusType] = None
    ErrorCode: Optional[str] = None
    ErrorDetail: Optional[str] = None

class TaskExecutionResultDetailTypeDef(BaseValidatorModel):
    PrepareDuration: Optional[int] = None
    PrepareStatus: Optional[PhaseStatusType] = None
    TotalDuration: Optional[int] = None
    TransferDuration: Optional[int] = None
    TransferStatus: Optional[PhaseStatusType] = None
    VerifyDuration: Optional[int] = None
    VerifyStatus: Optional[PhaseStatusType] = None
    ErrorCode: Optional[str] = None
    ErrorDetail: Optional[str] = None

class DescribeTaskRequestRequestTypeDef(BaseValidatorModel):
    TaskArn: str

class TaskScheduleDetailsTypeDef(BaseValidatorModel):
    StatusUpdateTime: Optional[datetime] = None
    DisabledReason: Optional[str] = None
    DisabledBy: Optional[ScheduleDisabledByType] = None

class DiscoveryJobListEntryTypeDef(BaseValidatorModel):
    DiscoveryJobArn: Optional[str] = None
    Status: Optional[DiscoveryJobStatusType] = None

class GenerateRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceIds: Sequence[str]
    ResourceType: DiscoveryResourceTypeType

class IOPSTypeDef(BaseValidatorModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None
    Total: Optional[float] = None

class LatencyTypeDef(BaseValidatorModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None

class ListAgentsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDiscoveryJobsRequestRequestTypeDef(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LocationFilterTypeDef(BaseValidatorModel):
    Name: LocationFilterNameType
    Values: Sequence[str]
    Operator: OperatorType

class LocationListEntryTypeDef(BaseValidatorModel):
    LocationArn: Optional[str] = None
    LocationUri: Optional[str] = None

class ListStorageSystemsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StorageSystemListEntryTypeDef(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    Name: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTaskExecutionsRequestRequestTypeDef(BaseValidatorModel):
    TaskArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TaskExecutionListEntryTypeDef(BaseValidatorModel):
    TaskExecutionArn: Optional[str] = None
    Status: Optional[TaskExecutionStatusType] = None

class TaskFilterTypeDef(BaseValidatorModel):
    Name: TaskFilterNameType
    Values: Sequence[str]
    Operator: OperatorType

class TaskListEntryTypeDef(BaseValidatorModel):
    TaskArn: Optional[str] = None
    Status: Optional[TaskStatusType] = None
    Name: Optional[str] = None

class MaxP95PerformanceTypeDef(BaseValidatorModel):
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

class RecommendationTypeDef(BaseValidatorModel):
    StorageType: Optional[str] = None
    StorageConfiguration: Optional[Dict[str, str]] = None
    EstimatedMonthlyStorageCost: Optional[str] = None

class ThroughputTypeDef(BaseValidatorModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None
    Total: Optional[float] = None

class RemoveStorageSystemRequestRequestTypeDef(BaseValidatorModel):
    StorageSystemArn: str

class ReportDestinationS3TypeDef(BaseValidatorModel):
    S3BucketArn: str
    BucketAccessRoleArn: str
    Subdirectory: Optional[str] = None

class ReportOverrideTypeDef(BaseValidatorModel):
    ReportLevel: Optional[ReportLevelType] = None

class S3ManifestConfigTypeDef(BaseValidatorModel):
    ManifestObjectPath: str
    BucketAccessRoleArn: str
    S3BucketArn: str
    ManifestObjectVersionId: Optional[str] = None

class StopDiscoveryJobRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Keys: Sequence[str]

class UpdateAgentRequestRequestTypeDef(BaseValidatorModel):
    AgentArn: str
    Name: Optional[str] = None

class UpdateDiscoveryJobRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str
    CollectionDurationMinutes: int

class UpdateStorageSystemRequestRequestTypeDef(BaseValidatorModel):
    StorageSystemArn: str
    ServerConfiguration: Optional[DiscoveryServerConfigurationTypeDef] = None
    AgentArns: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Credentials: Optional[CredentialsTypeDef] = None

class AddStorageSystemRequestRequestTypeDef(BaseValidatorModel):
    ServerConfiguration: DiscoveryServerConfigurationTypeDef
    SystemType: Literal["NetAppONTAP"]
    AgentArns: Sequence[str]
    ClientToken: str
    Credentials: CredentialsTypeDef
    CloudWatchLogGroupArn: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    Name: Optional[str] = None

class CreateAgentRequestRequestTypeDef(BaseValidatorModel):
    ActivationKey: str
    AgentName: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    VpcEndpointId: Optional[str] = None
    SubnetArns: Optional[Sequence[str]] = None
    SecurityGroupArns: Optional[Sequence[str]] = None

class CreateLocationFsxLustreRequestRequestTypeDef(BaseValidatorModel):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class CreateLocationFsxWindowsRequestRequestTypeDef(BaseValidatorModel):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    User: str
    Password: str
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    Domain: Optional[str] = None

class StartDiscoveryJobRequestRequestTypeDef(BaseValidatorModel):
    StorageSystemArn: str
    CollectionDurationMinutes: int
    ClientToken: str
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagListEntryTypeDef]

class AddStorageSystemResponseTypeDef(BaseValidatorModel):
    StorageSystemArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentResponseTypeDef(BaseValidatorModel):
    AgentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationAzureBlobResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationEfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxLustreResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxOntapResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxOpenZfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxWindowsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationHdfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationNfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationObjectStorageResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationS3ResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationSmbResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskResponseTypeDef(BaseValidatorModel):
    TaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDiscoveryJobResponseTypeDef(BaseValidatorModel):
    StorageSystemArn: str
    DiscoveryJobArn: str
    CollectionDurationMinutes: int
    Status: DiscoveryJobStatusType
    JobStartTime: datetime
    JobEndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationAzureBlobResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AuthenticationType: Literal["SAS"]
    BlobType: Literal["BLOCK"]
    AccessTier: AzureAccessTierType
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxLustreResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxWindowsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    User: str
    Domain: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationObjectStorageResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AccessKey: str
    ServerPort: int
    ServerProtocol: ObjectStorageServerProtocolType
    AgentArns: List[str]
    CreationTime: datetime
    ServerCertificate: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorageSystemResponseTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartDiscoveryJobResponseTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskExecutionResponseTypeDef(BaseValidatorModel):
    TaskExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AgentListEntryTypeDef(BaseValidatorModel):
    AgentArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AgentStatusType] = None
    Platform: Optional[PlatformTypeDef] = None

class CreateLocationAzureBlobRequestRequestTypeDef(BaseValidatorModel):
    ContainerUrl: str
    AuthenticationType: Literal["SAS"]
    AgentArns: Sequence[str]
    SasConfiguration: Optional[AzureBlobSasConfigurationTypeDef] = None
    BlobType: Optional[Literal["BLOCK"]] = None
    AccessTier: Optional[AzureAccessTierType] = None
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class UpdateLocationAzureBlobRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    AuthenticationType: Optional[Literal["SAS"]] = None
    SasConfiguration: Optional[AzureBlobSasConfigurationTypeDef] = None
    BlobType: Optional[Literal["BLOCK"]] = None
    AccessTier: Optional[AzureAccessTierType] = None
    AgentArns: Optional[Sequence[str]] = None

class CreateLocationObjectStorageRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateLocationObjectStorageRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    AgentArns: Optional[Sequence[str]] = None
    ServerCertificate: Optional[BlobTypeDef] = None

class CreateLocationEfsRequestRequestTypeDef(BaseValidatorModel):
    EfsFilesystemArn: str
    Ec2Config: Ec2ConfigTypeDef
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None
    AccessPointArn: Optional[str] = None
    FileSystemAccessRoleArn: Optional[str] = None
    InTransitEncryption: Optional[EfsInTransitEncryptionType] = None

class CreateLocationHdfsRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeLocationHdfsResponseTypeDef(BaseValidatorModel):
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

class UpdateLocationHdfsRequestRequestTypeDef(BaseValidatorModel):
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

class FsxProtocolNfsTypeDef(BaseValidatorModel):
    MountOptions: Optional[NfsMountOptionsTypeDef] = None

class CreateLocationNfsRequestRequestTypeDef(BaseValidatorModel):
    Subdirectory: str
    ServerHostname: str
    OnPremConfig: OnPremConfigTypeDef
    MountOptions: Optional[NfsMountOptionsTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class UpdateLocationNfsRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    OnPremConfig: Optional[OnPremConfigTypeDef] = None
    MountOptions: Optional[NfsMountOptionsTypeDef] = None

class CreateLocationS3RequestRequestTypeDef(BaseValidatorModel):
    S3BucketArn: str
    S3Config: S3ConfigTypeDef
    Subdirectory: Optional[str] = None
    S3StorageClass: Optional[S3StorageClassType] = None
    AgentArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationS3ResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    S3StorageClass: S3StorageClassType
    S3Config: S3ConfigTypeDef
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationSmbRequestRequestTypeDef(BaseValidatorModel):
    Subdirectory: str
    ServerHostname: str
    User: str
    Password: str
    AgentArns: Sequence[str]
    Domain: Optional[str] = None
    MountOptions: Optional[SmbMountOptionsTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationSmbResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AgentArns: List[str]
    User: str
    Domain: str
    MountOptions: SmbMountOptionsTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class FsxProtocolSmbTypeDef(BaseValidatorModel):
    Password: str
    User: str
    Domain: Optional[str] = None
    MountOptions: Optional[SmbMountOptionsTypeDef] = None

class UpdateLocationSmbRequestRequestTypeDef(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    User: Optional[str] = None
    Domain: Optional[str] = None
    Password: Optional[str] = None
    AgentArns: Optional[Sequence[str]] = None
    MountOptions: Optional[SmbMountOptionsTypeDef] = None

class UpdateTaskExecutionRequestRequestTypeDef(BaseValidatorModel):
    TaskExecutionArn: str
    Options: OptionsTypeDef

class DescribeAgentResponseTypeDef(BaseValidatorModel):
    AgentArn: str
    Name: str
    Status: AgentStatusType
    LastConnectionTime: datetime
    CreationTime: datetime
    EndpointType: EndpointTypeType
    PrivateLinkConfig: PrivateLinkConfigTypeDef
    Platform: PlatformTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationEfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    Ec2Config: Ec2ConfigOutputTypeDef
    CreationTime: datetime
    AccessPointArn: str
    FileSystemAccessRoleArn: str
    InTransitEncryption: EfsInTransitEncryptionType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationNfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    OnPremConfig: OnPremConfigOutputTypeDef
    MountOptions: NfsMountOptionsTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentsRequestListAgentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDiscoveryJobsRequestListDiscoveryJobsPaginateTypeDef(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStorageSystemsRequestListStorageSystemsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTaskExecutionsRequestListTaskExecutionsPaginateTypeDef(BaseValidatorModel):
    TaskArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStorageSystemResourceMetricsRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDiscoveryJobsResponseTypeDef(BaseValidatorModel):
    DiscoveryJobs: List[DiscoveryJobListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLocationsRequestListLocationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLocationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[LocationFilterTypeDef]] = None

class ListLocationsResponseTypeDef(BaseValidatorModel):
    Locations: List[LocationListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStorageSystemsResponseTypeDef(BaseValidatorModel):
    StorageSystems: List[StorageSystemListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTaskExecutionsResponseTypeDef(BaseValidatorModel):
    TaskExecutions: List[TaskExecutionListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTasksRequestListTasksPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[TaskFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[TaskFilterTypeDef]] = None

class ListTasksResponseTypeDef(BaseValidatorModel):
    Tasks: List[TaskListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetAppONTAPClusterTypeDef(BaseValidatorModel):
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

class NetAppONTAPSVMTypeDef(BaseValidatorModel):
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

class NetAppONTAPVolumeTypeDef(BaseValidatorModel):
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

class P95MetricsTypeDef(BaseValidatorModel):
    IOPS: Optional[IOPSTypeDef] = None
    Throughput: Optional[ThroughputTypeDef] = None
    Latency: Optional[LatencyTypeDef] = None

class ReportDestinationTypeDef(BaseValidatorModel):
    S3: Optional[ReportDestinationS3TypeDef] = None

class ReportOverridesTypeDef(BaseValidatorModel):
    Transferred: Optional[ReportOverrideTypeDef] = None
    Verified: Optional[ReportOverrideTypeDef] = None
    Deleted: Optional[ReportOverrideTypeDef] = None
    Skipped: Optional[ReportOverrideTypeDef] = None

class SourceManifestConfigTypeDef(BaseValidatorModel):
    S3: S3ManifestConfigTypeDef

class ListAgentsResponseTypeDef(BaseValidatorModel):
    Agents: List[AgentListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FsxProtocolTypeDef(BaseValidatorModel):
    NFS: Optional[FsxProtocolNfsTypeDef] = None
    SMB: Optional[FsxProtocolSmbTypeDef] = None

class ResourceDetailsTypeDef(BaseValidatorModel):
    NetAppONTAPSVMs: Optional[List[NetAppONTAPSVMTypeDef]] = None
    NetAppONTAPVolumes: Optional[List[NetAppONTAPVolumeTypeDef]] = None
    NetAppONTAPClusters: Optional[List[NetAppONTAPClusterTypeDef]] = None

class ResourceMetricsTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    P95Metrics: Optional[P95MetricsTypeDef] = None
    Capacity: Optional[CapacityTypeDef] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[DiscoveryResourceTypeType] = None

class TaskReportConfigTypeDef(BaseValidatorModel):
    Destination: Optional[ReportDestinationTypeDef] = None
    OutputType: Optional[ReportOutputTypeType] = None
    ReportLevel: Optional[ReportLevelType] = None
    ObjectVersionIds: Optional[ObjectVersionIdsType] = None
    Overrides: Optional[ReportOverridesTypeDef] = None

class ManifestConfigTypeDef(BaseValidatorModel):
    Action: Optional[Literal["TRANSFER"]] = None
    Format: Optional[Literal["CSV"]] = None
    Source: Optional[SourceManifestConfigTypeDef] = None

class CreateLocationFsxOntapRequestRequestTypeDef(BaseValidatorModel):
    Protocol: FsxProtocolTypeDef
    SecurityGroupArns: Sequence[str]
    StorageVirtualMachineArn: str
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class CreateLocationFsxOpenZfsRequestRequestTypeDef(BaseValidatorModel):
    FsxFilesystemArn: str
    Protocol: FsxProtocolTypeDef
    SecurityGroupArns: Sequence[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class DescribeLocationFsxOntapResponseTypeDef(BaseValidatorModel):
    CreationTime: datetime
    LocationArn: str
    LocationUri: str
    Protocol: FsxProtocolTypeDef
    SecurityGroupArns: List[str]
    StorageVirtualMachineArn: str
    FsxFilesystemArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxOpenZfsResponseTypeDef(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    Protocol: FsxProtocolTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorageSystemResourcesResponseTypeDef(BaseValidatorModel):
    ResourceDetails: ResourceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStorageSystemResourceMetricsResponseTypeDef(BaseValidatorModel):
    Metrics: List[ResourceMetricsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTaskRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeTaskExecutionResponseTypeDef(BaseValidatorModel):
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

class DescribeTaskResponseTypeDef(BaseValidatorModel):
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

class StartTaskExecutionRequestRequestTypeDef(BaseValidatorModel):
    TaskArn: str
    OverrideOptions: Optional[OptionsTypeDef] = None
    Includes: Optional[Sequence[FilterRuleTypeDef]] = None
    Excludes: Optional[Sequence[FilterRuleTypeDef]] = None
    ManifestConfig: Optional[ManifestConfigTypeDef] = None
    TaskReportConfig: Optional[TaskReportConfigTypeDef] = None
    Tags: Optional[Sequence[TagListEntryTypeDef]] = None

class UpdateTaskRequestRequestTypeDef(BaseValidatorModel):
    TaskArn: str
    Options: Optional[OptionsTypeDef] = None
    Excludes: Optional[Sequence[FilterRuleTypeDef]] = None
    Schedule: Optional[TaskScheduleTypeDef] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Includes: Optional[Sequence[FilterRuleTypeDef]] = None
    ManifestConfig: Optional[ManifestConfigTypeDef] = None
    TaskReportConfig: Optional[TaskReportConfigTypeDef] = None

