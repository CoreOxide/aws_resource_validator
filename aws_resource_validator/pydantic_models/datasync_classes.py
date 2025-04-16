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
from aws_resource_validator.pydantic_models.datasync_constants import *

class Credentials(BaseValidatorModel):
    Username: str
    Password: str


class DiscoveryServerConfiguration(BaseValidatorModel):
    ServerHostname: str
    ServerPort: Optional[int] = None


class TagListEntry(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Platform(BaseValidatorModel):
    Version: Optional[str] = None


class AzureBlobSasConfiguration(BaseValidatorModel):
    Token: str


class CancelTaskExecutionRequest(BaseValidatorModel):
    TaskExecutionArn: str


class Capacity(BaseValidatorModel):
    Used: Optional[int] = None
    Provisioned: Optional[int] = None
    LogicalUsed: Optional[int] = None
    ClusterCloudStorageUsed: Optional[int] = None


class HdfsNameNode(BaseValidatorModel):
    Hostname: str
    Port: int


class QopConfiguration(BaseValidatorModel):
    RpcProtection: Optional[HdfsRpcProtectionType] = None
    DataTransferProtection: Optional[HdfsDataTransferProtectionType] = None


class NfsMountOptions(BaseValidatorModel):
    Version: Optional[NfsVersionType] = None


class S3Config(BaseValidatorModel):
    BucketAccessRoleArn: str


class SmbMountOptions(BaseValidatorModel):
    Version: Optional[SmbVersionType] = None


class FilterRule(BaseValidatorModel):
    FilterType: Optional[Literal["SIMPLE_PATTERN"]] = None
    Value: Optional[str] = None


class Options(BaseValidatorModel):
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


class TaskSchedule(BaseValidatorModel):
    ScheduleExpression: str
    Status: Optional[ScheduleStatusType] = None


class DeleteAgentRequest(BaseValidatorModel):
    AgentArn: str


class DeleteLocationRequest(BaseValidatorModel):
    LocationArn: str


class DeleteTaskRequest(BaseValidatorModel):
    TaskArn: str


class DescribeAgentRequest(BaseValidatorModel):
    AgentArn: str


class PrivateLinkConfig(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    PrivateLinkEndpoint: Optional[str] = None
    SubnetArns: Optional[List[str]] = None
    SecurityGroupArns: Optional[List[str]] = None


class DescribeDiscoveryJobRequest(BaseValidatorModel):
    DiscoveryJobArn: str


class DescribeLocationAzureBlobRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationEfsRequest(BaseValidatorModel):
    LocationArn: str


class Ec2ConfigOutput(BaseValidatorModel):
    SubnetArn: str
    SecurityGroupArns: List[str]


class DescribeLocationFsxLustreRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationFsxOntapRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationFsxOpenZfsRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationFsxWindowsRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationHdfsRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationNfsRequest(BaseValidatorModel):
    LocationArn: str


class OnPremConfigOutput(BaseValidatorModel):
    AgentArns: List[str]


class DescribeLocationObjectStorageRequest(BaseValidatorModel):
    LocationArn: str


class DescribeLocationS3Request(BaseValidatorModel):
    LocationArn: str


class DescribeLocationSmbRequest(BaseValidatorModel):
    LocationArn: str


class DescribeStorageSystemRequest(BaseValidatorModel):
    StorageSystemArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeStorageSystemResourcesRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceIds: Optional[Sequence[str]] = None
    Filter: Optional[Mapping[Literal["SVM"], Sequence[str]]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeTaskExecutionRequest(BaseValidatorModel):
    TaskExecutionArn: str


class ReportResult(BaseValidatorModel):
    Status: Optional[PhaseStatusType] = None
    ErrorCode: Optional[str] = None
    ErrorDetail: Optional[str] = None


class TaskExecutionFilesFailedDetail(BaseValidatorModel):
    Prepare: Optional[int] = None
    Transfer: Optional[int] = None
    Verify: Optional[int] = None
    Delete: Optional[int] = None


class TaskExecutionFilesListedDetail(BaseValidatorModel):
    AtSource: Optional[int] = None
    AtDestinationForDelete: Optional[int] = None


class TaskExecutionResultDetail(BaseValidatorModel):
    PrepareDuration: Optional[int] = None
    PrepareStatus: Optional[PhaseStatusType] = None
    TotalDuration: Optional[int] = None
    TransferDuration: Optional[int] = None
    TransferStatus: Optional[PhaseStatusType] = None
    VerifyDuration: Optional[int] = None
    VerifyStatus: Optional[PhaseStatusType] = None
    ErrorCode: Optional[str] = None
    ErrorDetail: Optional[str] = None


class DescribeTaskRequest(BaseValidatorModel):
    TaskArn: str


class TaskScheduleDetails(BaseValidatorModel):
    StatusUpdateTime: Optional[datetime] = None
    DisabledReason: Optional[str] = None
    DisabledBy: Optional[ScheduleDisabledByType] = None


class DiscoveryJobListEntry(BaseValidatorModel):
    DiscoveryJobArn: Optional[str] = None
    Status: Optional[DiscoveryJobStatusType] = None


class Ec2Config(BaseValidatorModel):
    SubnetArn: str
    SecurityGroupArns: Sequence[str]


class GenerateRecommendationsRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceIds: Sequence[str]
    ResourceType: DiscoveryResourceTypeType


class IOPS(BaseValidatorModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None
    Total: Optional[float] = None


class Latency(BaseValidatorModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None


class ListAgentsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDiscoveryJobsRequest(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LocationFilter(BaseValidatorModel):
    Name: LocationFilterNameType
    Values: Sequence[str]
    Operator: OperatorType


class LocationListEntry(BaseValidatorModel):
    LocationArn: Optional[str] = None
    LocationUri: Optional[str] = None


class ListStorageSystemsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StorageSystemListEntry(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    Name: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTaskExecutionsRequest(BaseValidatorModel):
    TaskArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TaskExecutionListEntry(BaseValidatorModel):
    TaskExecutionArn: Optional[str] = None
    Status: Optional[TaskExecutionStatusType] = None
    TaskMode: Optional[TaskModeType] = None


class TaskFilter(BaseValidatorModel):
    Name: TaskFilterNameType
    Values: Sequence[str]
    Operator: OperatorType


class TaskListEntry(BaseValidatorModel):
    TaskArn: Optional[str] = None
    Status: Optional[TaskStatusType] = None
    Name: Optional[str] = None
    TaskMode: Optional[TaskModeType] = None


class MaxP95Performance(BaseValidatorModel):
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


class Recommendation(BaseValidatorModel):
    StorageType: Optional[str] = None
    StorageConfiguration: Optional[Dict[str, str]] = None
    EstimatedMonthlyStorageCost: Optional[str] = None


class OnPremConfig(BaseValidatorModel):
    AgentArns: Sequence[str]


class Throughput(BaseValidatorModel):
    Read: Optional[float] = None
    Write: Optional[float] = None
    Other: Optional[float] = None
    Total: Optional[float] = None


class RemoveStorageSystemRequest(BaseValidatorModel):
    StorageSystemArn: str


class ReportDestinationS3(BaseValidatorModel):
    S3BucketArn: str
    BucketAccessRoleArn: str
    Subdirectory: Optional[str] = None


class ReportOverride(BaseValidatorModel):
    ReportLevel: Optional[ReportLevelType] = None


class S3ManifestConfig(BaseValidatorModel):
    ManifestObjectPath: str
    BucketAccessRoleArn: str
    S3BucketArn: str
    ManifestObjectVersionId: Optional[str] = None


class StopDiscoveryJobRequest(BaseValidatorModel):
    DiscoveryJobArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Keys: Sequence[str]


class UpdateAgentRequest(BaseValidatorModel):
    AgentArn: str
    Name: Optional[str] = None


class UpdateDiscoveryJobRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    CollectionDurationMinutes: int


class UpdateLocationEfsRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    AccessPointArn: Optional[str] = None
    FileSystemAccessRoleArn: Optional[str] = None
    InTransitEncryption: Optional[EfsInTransitEncryptionType] = None


class UpdateLocationFsxLustreRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None


class UpdateLocationFsxWindowsRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    Domain: Optional[str] = None
    User: Optional[str] = None
    Password: Optional[str] = None


class UpdateStorageSystemRequest(BaseValidatorModel):
    StorageSystemArn: str
    ServerConfiguration: Optional[DiscoveryServerConfiguration] = None
    AgentArns: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Credentials: Optional[Credentials] = None


class AddStorageSystemRequest(BaseValidatorModel):
    ServerConfiguration: DiscoveryServerConfiguration
    SystemType: Literal["NetAppONTAP"]
    AgentArns: Sequence[str]
    ClientToken: str
    Credentials: Credentials
    CloudWatchLogGroupArn: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    Name: Optional[str] = None


class CreateAgentRequest(BaseValidatorModel):
    ActivationKey: str
    AgentName: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    VpcEndpointId: Optional[str] = None
    SubnetArns: Optional[Sequence[str]] = None
    SecurityGroupArns: Optional[Sequence[str]] = None


class CreateLocationFsxLustreRequest(BaseValidatorModel):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None


class CreateLocationFsxWindowsRequest(BaseValidatorModel):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    User: str
    Password: str
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    Domain: Optional[str] = None


class StartDiscoveryJobRequest(BaseValidatorModel):
    StorageSystemArn: str
    CollectionDurationMinutes: int
    ClientToken: str
    Tags: Optional[Sequence[TagListEntry]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagListEntry]


class AddStorageSystemResponse(BaseValidatorModel):
    StorageSystemArn: str
    ResponseMetadata: ResponseMetadata


class CreateAgentResponse(BaseValidatorModel):
    AgentArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationAzureBlobResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationEfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationFsxLustreResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationFsxOntapResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationFsxOpenZfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationFsxWindowsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationHdfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationNfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationObjectStorageResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationS3Response(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLocationSmbResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


class CreateTaskResponse(BaseValidatorModel):
    TaskArn: str
    ResponseMetadata: ResponseMetadata


class DescribeDiscoveryJobResponse(BaseValidatorModel):
    StorageSystemArn: str
    DiscoveryJobArn: str
    CollectionDurationMinutes: int
    Status: DiscoveryJobStatusType
    JobStartTime: datetime
    JobEndTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeLocationAzureBlobResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AuthenticationType: Literal["SAS"]
    BlobType: Literal["BLOCK"]
    AccessTier: AzureAccessTierType
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeLocationFsxLustreResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeLocationFsxWindowsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    User: str
    Domain: str
    ResponseMetadata: ResponseMetadata


class DescribeLocationObjectStorageResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AccessKey: str
    ServerPort: int
    ServerProtocol: ObjectStorageServerProtocolType
    AgentArns: List[str]
    CreationTime: datetime
    ServerCertificate: bytes
    ResponseMetadata: ResponseMetadata


class DescribeStorageSystemResponse(BaseValidatorModel):
    StorageSystemArn: str
    ServerConfiguration: DiscoveryServerConfiguration
    SystemType: Literal["NetAppONTAP"]
    AgentArns: List[str]
    Name: str
    ErrorMessage: str
    ConnectivityStatus: StorageSystemConnectivityStatusType
    CloudWatchLogGroupArn: str
    CreationTime: datetime
    SecretsManagerArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[TagListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartDiscoveryJobResponse(BaseValidatorModel):
    DiscoveryJobArn: str
    ResponseMetadata: ResponseMetadata


class StartTaskExecutionResponse(BaseValidatorModel):
    TaskExecutionArn: str
    ResponseMetadata: ResponseMetadata


class AgentListEntry(BaseValidatorModel):
    AgentArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AgentStatusType] = None
    Platform: Optional[Platform] = None


class CreateLocationAzureBlobRequest(BaseValidatorModel):
    ContainerUrl: str
    AuthenticationType: Literal["SAS"]
    AgentArns: Sequence[str]
    SasConfiguration: Optional[AzureBlobSasConfiguration] = None
    BlobType: Optional[Literal["BLOCK"]] = None
    AccessTier: Optional[AzureAccessTierType] = None
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None


class UpdateLocationAzureBlobRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    AuthenticationType: Optional[Literal["SAS"]] = None
    SasConfiguration: Optional[AzureBlobSasConfiguration] = None
    BlobType: Optional[Literal["BLOCK"]] = None
    AccessTier: Optional[AzureAccessTierType] = None
    AgentArns: Optional[Sequence[str]] = None


class Blob(BaseValidatorModel):
    pass


class CreateLocationObjectStorageRequest(BaseValidatorModel):
    ServerHostname: str
    BucketName: str
    AgentArns: Sequence[str]
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    ServerCertificate: Optional[Blob] = None


class UpdateLocationObjectStorageRequest(BaseValidatorModel):
    LocationArn: str
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    ServerHostname: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    AgentArns: Optional[Sequence[str]] = None
    ServerCertificate: Optional[Blob] = None


class CreateLocationHdfsRequest(BaseValidatorModel):
    NameNodes: Sequence[HdfsNameNode]
    AuthenticationType: HdfsAuthenticationTypeType
    AgentArns: Sequence[str]
    Subdirectory: Optional[str] = None
    BlockSize: Optional[int] = None
    ReplicationFactor: Optional[int] = None
    KmsKeyProviderUri: Optional[str] = None
    QopConfiguration: Optional[QopConfiguration] = None
    SimpleUser: Optional[str] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None
    Tags: Optional[Sequence[TagListEntry]] = None


class DescribeLocationHdfsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    NameNodes: List[HdfsNameNode]
    BlockSize: int
    ReplicationFactor: int
    KmsKeyProviderUri: str
    QopConfiguration: QopConfiguration
    AuthenticationType: HdfsAuthenticationTypeType
    SimpleUser: str
    KerberosPrincipal: str
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateLocationHdfsRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    NameNodes: Optional[Sequence[HdfsNameNode]] = None
    BlockSize: Optional[int] = None
    ReplicationFactor: Optional[int] = None
    KmsKeyProviderUri: Optional[str] = None
    QopConfiguration: Optional[QopConfiguration] = None
    AuthenticationType: Optional[HdfsAuthenticationTypeType] = None
    SimpleUser: Optional[str] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None
    AgentArns: Optional[Sequence[str]] = None


class FsxProtocolNfs(BaseValidatorModel):
    MountOptions: Optional[NfsMountOptions] = None


class CreateLocationS3Request(BaseValidatorModel):
    S3BucketArn: str
    S3Config: S3Config
    Subdirectory: Optional[str] = None
    S3StorageClass: Optional[S3StorageClassType] = None
    AgentArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagListEntry]] = None


class DescribeLocationS3Response(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    S3StorageClass: S3StorageClassType
    S3Config: S3Config
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateLocationS3Request(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    S3StorageClass: Optional[S3StorageClassType] = None
    S3Config: Optional[S3Config] = None


class CreateLocationSmbRequest(BaseValidatorModel):
    Subdirectory: str
    ServerHostname: str
    AgentArns: Sequence[str]
    User: Optional[str] = None
    Domain: Optional[str] = None
    Password: Optional[str] = None
    MountOptions: Optional[SmbMountOptions] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    AuthenticationType: Optional[SmbAuthenticationTypeType] = None
    DnsIpAddresses: Optional[Sequence[str]] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None


class DescribeLocationSmbResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AgentArns: List[str]
    User: str
    Domain: str
    MountOptions: SmbMountOptions
    CreationTime: datetime
    DnsIpAddresses: List[str]
    KerberosPrincipal: str
    AuthenticationType: SmbAuthenticationTypeType
    ResponseMetadata: ResponseMetadata


class FsxProtocolSmb(BaseValidatorModel):
    Password: str
    User: str
    Domain: Optional[str] = None
    MountOptions: Optional[SmbMountOptions] = None


class FsxUpdateProtocolSmb(BaseValidatorModel):
    Domain: Optional[str] = None
    MountOptions: Optional[SmbMountOptions] = None
    Password: Optional[str] = None
    User: Optional[str] = None


class UpdateLocationSmbRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    ServerHostname: Optional[str] = None
    User: Optional[str] = None
    Domain: Optional[str] = None
    Password: Optional[str] = None
    AgentArns: Optional[Sequence[str]] = None
    MountOptions: Optional[SmbMountOptions] = None
    AuthenticationType: Optional[SmbAuthenticationTypeType] = None
    DnsIpAddresses: Optional[Sequence[str]] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None


class UpdateTaskExecutionRequest(BaseValidatorModel):
    TaskExecutionArn: str
    Options: Options


class DescribeAgentResponse(BaseValidatorModel):
    AgentArn: str
    Name: str
    Status: AgentStatusType
    LastConnectionTime: datetime
    CreationTime: datetime
    EndpointType: EndpointTypeType
    PrivateLinkConfig: PrivateLinkConfig
    Platform: Platform
    ResponseMetadata: ResponseMetadata


class DescribeLocationEfsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    Ec2Config: Ec2ConfigOutput
    CreationTime: datetime
    AccessPointArn: str
    FileSystemAccessRoleArn: str
    InTransitEncryption: EfsInTransitEncryptionType
    ResponseMetadata: ResponseMetadata


class DescribeLocationNfsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    OnPremConfig: OnPremConfigOutput
    MountOptions: NfsMountOptions
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class ListAgentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDiscoveryJobsRequestPaginate(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStorageSystemsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTaskExecutionsRequestPaginate(BaseValidatorModel):
    TaskArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class DescribeStorageSystemResourceMetricsRequestPaginate(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStorageSystemResourceMetricsRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDiscoveryJobsResponse(BaseValidatorModel):
    DiscoveryJobs: List[DiscoveryJobListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLocationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLocationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[LocationFilter]] = None


class ListLocationsResponse(BaseValidatorModel):
    Locations: List[LocationListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStorageSystemsResponse(BaseValidatorModel):
    StorageSystems: List[StorageSystemListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTaskExecutionsResponse(BaseValidatorModel):
    TaskExecutions: List[TaskExecutionListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTasksRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[TaskFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTasksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[TaskFilter]] = None


class ListTasksResponse(BaseValidatorModel):
    Tasks: List[TaskListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NetAppONTAPCluster(BaseValidatorModel):
    CifsShareCount: Optional[int] = None
    NfsExportedVolumes: Optional[int] = None
    ResourceId: Optional[str] = None
    ClusterName: Optional[str] = None
    MaxP95Performance: Optional[MaxP95Performance] = None
    ClusterBlockStorageSize: Optional[int] = None
    ClusterBlockStorageUsed: Optional[int] = None
    ClusterBlockStorageLogicalUsed: Optional[int] = None
    Recommendations: Optional[List[Recommendation]] = None
    RecommendationStatus: Optional[RecommendationStatusType] = None
    LunCount: Optional[int] = None
    ClusterCloudStorageUsed: Optional[int] = None


class NetAppONTAPSVM(BaseValidatorModel):
    ClusterUuid: Optional[str] = None
    ResourceId: Optional[str] = None
    SvmName: Optional[str] = None
    CifsShareCount: Optional[int] = None
    EnabledProtocols: Optional[List[str]] = None
    TotalCapacityUsed: Optional[int] = None
    TotalCapacityProvisioned: Optional[int] = None
    TotalLogicalCapacityUsed: Optional[int] = None
    MaxP95Performance: Optional[MaxP95Performance] = None
    Recommendations: Optional[List[Recommendation]] = None
    NfsExportedVolumes: Optional[int] = None
    RecommendationStatus: Optional[RecommendationStatusType] = None
    TotalSnapshotCapacityUsed: Optional[int] = None
    LunCount: Optional[int] = None


class NetAppONTAPVolume(BaseValidatorModel):
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
    MaxP95Performance: Optional[MaxP95Performance] = None
    Recommendations: Optional[List[Recommendation]] = None
    RecommendationStatus: Optional[RecommendationStatusType] = None
    LunCount: Optional[int] = None


class P95Metrics(BaseValidatorModel):
    IOPS: Optional[IOPS] = None
    Throughput: Optional[Throughput] = None
    Latency: Optional[Latency] = None


class ReportDestination(BaseValidatorModel):
    S3: Optional[ReportDestinationS3] = None


class ReportOverrides(BaseValidatorModel):
    Transferred: Optional[ReportOverride] = None
    Verified: Optional[ReportOverride] = None
    Deleted: Optional[ReportOverride] = None
    Skipped: Optional[ReportOverride] = None


class SourceManifestConfig(BaseValidatorModel):
    S3: S3ManifestConfig


class ListAgentsResponse(BaseValidatorModel):
    Agents: List[AgentListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FsxProtocol(BaseValidatorModel):
    NFS: Optional[FsxProtocolNfs] = None
    SMB: Optional[FsxProtocolSmb] = None


class FsxUpdateProtocol(BaseValidatorModel):
    NFS: Optional[FsxProtocolNfs] = None
    SMB: Optional[FsxUpdateProtocolSmb] = None


class Ec2ConfigUnion(BaseValidatorModel):
    pass


class CreateLocationEfsRequest(BaseValidatorModel):
    EfsFilesystemArn: str
    Ec2Config: Ec2ConfigUnion
    Subdirectory: Optional[str] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    AccessPointArn: Optional[str] = None
    FileSystemAccessRoleArn: Optional[str] = None
    InTransitEncryption: Optional[EfsInTransitEncryptionType] = None


class ResourceDetails(BaseValidatorModel):
    NetAppONTAPSVMs: Optional[List[NetAppONTAPSVM]] = None
    NetAppONTAPVolumes: Optional[List[NetAppONTAPVolume]] = None
    NetAppONTAPClusters: Optional[List[NetAppONTAPCluster]] = None


class OnPremConfigUnion(BaseValidatorModel):
    pass


class CreateLocationNfsRequest(BaseValidatorModel):
    Subdirectory: str
    ServerHostname: str
    OnPremConfig: OnPremConfigUnion
    MountOptions: Optional[NfsMountOptions] = None
    Tags: Optional[Sequence[TagListEntry]] = None


class UpdateLocationNfsRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    ServerHostname: Optional[str] = None
    OnPremConfig: Optional[OnPremConfigUnion] = None
    MountOptions: Optional[NfsMountOptions] = None


class ResourceMetrics(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    P95Metrics: Optional[P95Metrics] = None
    Capacity: Optional[Capacity] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[DiscoveryResourceTypeType] = None


class TaskReportConfig(BaseValidatorModel):
    Destination: Optional[ReportDestination] = None
    OutputType: Optional[ReportOutputTypeType] = None
    ReportLevel: Optional[ReportLevelType] = None
    ObjectVersionIds: Optional[ObjectVersionIdsType] = None
    Overrides: Optional[ReportOverrides] = None


class ManifestConfig(BaseValidatorModel):
    Action: Optional[Literal["TRANSFER"]] = None
    Format: Optional[Literal["CSV"]] = None
    Source: Optional[SourceManifestConfig] = None


class DescribeStorageSystemResourcesResponse(BaseValidatorModel):
    ResourceDetails: ResourceDetails
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeStorageSystemResourceMetricsResponse(BaseValidatorModel):
    Metrics: List[ResourceMetrics]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateTaskRequest(BaseValidatorModel):
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    Options: Optional[Options] = None
    Excludes: Optional[Sequence[FilterRule]] = None
    Schedule: Optional[TaskSchedule] = None
    Tags: Optional[Sequence[TagListEntry]] = None
    Includes: Optional[Sequence[FilterRule]] = None
    ManifestConfig: Optional[ManifestConfig] = None
    TaskReportConfig: Optional[TaskReportConfig] = None
    TaskMode: Optional[TaskModeType] = None


class DescribeTaskExecutionResponse(BaseValidatorModel):
    TaskExecutionArn: str
    Status: TaskExecutionStatusType
    Options: Options
    Excludes: List[FilterRule]
    Includes: List[FilterRule]
    ManifestConfig: ManifestConfig
    StartTime: datetime
    EstimatedFilesToTransfer: int
    EstimatedBytesToTransfer: int
    FilesTransferred: int
    BytesWritten: int
    BytesTransferred: int
    BytesCompressed: int
    Result: TaskExecutionResultDetail
    TaskReportConfig: TaskReportConfig
    FilesDeleted: int
    FilesSkipped: int
    FilesVerified: int
    ReportResult: ReportResult
    EstimatedFilesToDelete: int
    TaskMode: TaskModeType
    FilesPrepared: int
    FilesListed: TaskExecutionFilesListedDetail
    FilesFailed: TaskExecutionFilesFailedDetail
    ResponseMetadata: ResponseMetadata


class DescribeTaskResponse(BaseValidatorModel):
    TaskArn: str
    Status: TaskStatusType
    Name: str
    CurrentTaskExecutionArn: str
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: str
    SourceNetworkInterfaceArns: List[str]
    DestinationNetworkInterfaceArns: List[str]
    Options: Options
    Excludes: List[FilterRule]
    Schedule: TaskSchedule
    ErrorCode: str
    ErrorDetail: str
    CreationTime: datetime
    Includes: List[FilterRule]
    ManifestConfig: ManifestConfig
    TaskReportConfig: TaskReportConfig
    ScheduleDetails: TaskScheduleDetails
    TaskMode: TaskModeType
    ResponseMetadata: ResponseMetadata


class StartTaskExecutionRequest(BaseValidatorModel):
    TaskArn: str
    OverrideOptions: Optional[Options] = None
    Includes: Optional[Sequence[FilterRule]] = None
    Excludes: Optional[Sequence[FilterRule]] = None
    ManifestConfig: Optional[ManifestConfig] = None
    TaskReportConfig: Optional[TaskReportConfig] = None
    Tags: Optional[Sequence[TagListEntry]] = None


class UpdateTaskRequest(BaseValidatorModel):
    TaskArn: str
    Options: Optional[Options] = None
    Excludes: Optional[Sequence[FilterRule]] = None
    Schedule: Optional[TaskSchedule] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Includes: Optional[Sequence[FilterRule]] = None
    ManifestConfig: Optional[ManifestConfig] = None
    TaskReportConfig: Optional[TaskReportConfig] = None


