from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.datasync.datasync_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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

Blob = Union[str, bytes, IO[Any], StreamingBody]


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
    FilterType: Optional[Literal['SIMPLE_PATTERN']] = None
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


# This class is the input for the 'describe_agent' function.
class DescribeAgentRequest(BaseValidatorModel):
    AgentArn: str


class PrivateLinkConfig(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    PrivateLinkEndpoint: Optional[str] = None
    SubnetArns: Optional[List[str]] = None
    SecurityGroupArns: Optional[List[str]] = None


# This class is the input for the 'describe_discovery_job' function.
class DescribeDiscoveryJobRequest(BaseValidatorModel):
    DiscoveryJobArn: str


# This class is the input for the 'describe_location_azure_blob' function.
class DescribeLocationAzureBlobRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_efs' function.
class DescribeLocationEfsRequest(BaseValidatorModel):
    LocationArn: str


class Ec2ConfigOutput(BaseValidatorModel):
    SubnetArn: str
    SecurityGroupArns: List[str]


# This class is the input for the 'describe_location_fsx_lustre' function.
class DescribeLocationFsxLustreRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_fsx_ontap' function.
class DescribeLocationFsxOntapRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_fsx_open_zfs' function.
class DescribeLocationFsxOpenZfsRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_fsx_windows' function.
class DescribeLocationFsxWindowsRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_hdfs' function.
class DescribeLocationHdfsRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_nfs' function.
class DescribeLocationNfsRequest(BaseValidatorModel):
    LocationArn: str


class OnPremConfigOutput(BaseValidatorModel):
    AgentArns: List[str]


# This class is the input for the 'describe_location_object_storage' function.
class DescribeLocationObjectStorageRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_s3' function.
class DescribeLocationS3Request(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_location_smb' function.
class DescribeLocationSmbRequest(BaseValidatorModel):
    LocationArn: str


# This class is the input for the 'describe_storage_system' function.
class DescribeStorageSystemRequest(BaseValidatorModel):
    StorageSystemArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'describe_storage_system_resources' function.
class DescribeStorageSystemResourcesRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceIds: Optional[List[str]] = None
    Filter: Optional[Dict[Literal['SVM'], List[str]]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_task_execution' function.
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


# This class is the input for the 'describe_task' function.
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
    SecurityGroupArns: List[str]


class GenerateRecommendationsRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceIds: List[str]
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


# This class is the input for the 'list_agents' function.
class ListAgentsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_discovery_jobs' function.
class ListDiscoveryJobsRequest(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LocationFilter(BaseValidatorModel):
    Name: LocationFilterNameType
    Values: List[str]
    Operator: OperatorType


class LocationListEntry(BaseValidatorModel):
    LocationArn: Optional[str] = None
    LocationUri: Optional[str] = None


# This class is the input for the 'list_storage_systems' function.
class ListStorageSystemsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StorageSystemListEntry(BaseValidatorModel):
    StorageSystemArn: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_task_executions' function.
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
    Values: List[str]
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
    AgentArns: List[str]


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
    Keys: List[str]


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
    AgentArns: Optional[List[str]] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Credentials: Optional[Credentials] = None


# This class is the input for the 'add_storage_system' function.
class AddStorageSystemRequest(BaseValidatorModel):
    ServerConfiguration: DiscoveryServerConfiguration
    SystemType: Literal['NetAppONTAP']
    AgentArns: List[str]
    ClientToken: str
    Credentials: Credentials
    CloudWatchLogGroupArn: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None
    Name: Optional[str] = None


# This class is the input for the 'create_agent' function.
class CreateAgentRequest(BaseValidatorModel):
    ActivationKey: str
    AgentName: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None
    VpcEndpointId: Optional[str] = None
    SubnetArns: Optional[List[str]] = None
    SecurityGroupArns: Optional[List[str]] = None


# This class is the input for the 'create_location_fsx_lustre' function.
class CreateLocationFsxLustreRequest(BaseValidatorModel):
    FsxFilesystemArn: str
    SecurityGroupArns: List[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None


# This class is the input for the 'create_location_fsx_windows' function.
class CreateLocationFsxWindowsRequest(BaseValidatorModel):
    FsxFilesystemArn: str
    SecurityGroupArns: List[str]
    User: str
    Password: str
    Subdirectory: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None
    Domain: Optional[str] = None


# This class is the input for the 'start_discovery_job' function.
class StartDiscoveryJobRequest(BaseValidatorModel):
    StorageSystemArn: str
    CollectionDurationMinutes: int
    ClientToken: str
    Tags: Optional[List[TagListEntry]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[TagListEntry]


# This class is the output for the 'add_storage_system' function.
class AddStorageSystemResponse(BaseValidatorModel):
    StorageSystemArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_agent' function.
class CreateAgentResponse(BaseValidatorModel):
    AgentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_azure_blob' function.
class CreateLocationAzureBlobResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_efs' function.
class CreateLocationEfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_fsx_lustre' function.
class CreateLocationFsxLustreResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_fsx_ontap' function.
class CreateLocationFsxOntapResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_fsx_open_zfs' function.
class CreateLocationFsxOpenZfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_fsx_windows' function.
class CreateLocationFsxWindowsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_hdfs' function.
class CreateLocationHdfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_nfs' function.
class CreateLocationNfsResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_object_storage' function.
class CreateLocationObjectStorageResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_s3' function.
class CreateLocationS3Response(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_location_smb' function.
class CreateLocationSmbResponse(BaseValidatorModel):
    LocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_task' function.
class CreateTaskResponse(BaseValidatorModel):
    TaskArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_discovery_job' function.
class DescribeDiscoveryJobResponse(BaseValidatorModel):
    StorageSystemArn: str
    DiscoveryJobArn: str
    CollectionDurationMinutes: int
    Status: DiscoveryJobStatusType
    JobStartTime: datetime
    JobEndTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_location_azure_blob' function.
class DescribeLocationAzureBlobResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    AuthenticationType: Literal['SAS']
    BlobType: Literal['BLOCK']
    AccessTier: AzureAccessTierType
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_location_fsx_lustre' function.
class DescribeLocationFsxLustreResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_location_fsx_windows' function.
class DescribeLocationFsxWindowsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    User: str
    Domain: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_location_object_storage' function.
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


# This class is the output for the 'describe_storage_system' function.
class DescribeStorageSystemResponse(BaseValidatorModel):
    StorageSystemArn: str
    ServerConfiguration: DiscoveryServerConfiguration
    SystemType: Literal['NetAppONTAP']
    AgentArns: List[str]
    Name: str
    ErrorMessage: str
    ConnectivityStatus: StorageSystemConnectivityStatusType
    CloudWatchLogGroupArn: str
    CreationTime: datetime
    SecretsManagerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[TagListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_discovery_job' function.
class StartDiscoveryJobResponse(BaseValidatorModel):
    DiscoveryJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_task_execution' function.
class StartTaskExecutionResponse(BaseValidatorModel):
    TaskExecutionArn: str
    ResponseMetadata: ResponseMetadata


class AgentListEntry(BaseValidatorModel):
    AgentArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AgentStatusType] = None
    Platform: Optional[Platform] = None


# This class is the input for the 'create_location_azure_blob' function.
class CreateLocationAzureBlobRequest(BaseValidatorModel):
    ContainerUrl: str
    AuthenticationType: Literal['SAS']
    AgentArns: List[str]
    SasConfiguration: Optional[AzureBlobSasConfiguration] = None
    BlobType: Optional[Literal['BLOCK']] = None
    AccessTier: Optional[AzureAccessTierType] = None
    Subdirectory: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None


class UpdateLocationAzureBlobRequest(BaseValidatorModel):
    LocationArn: str
    Subdirectory: Optional[str] = None
    AuthenticationType: Optional[Literal['SAS']] = None
    SasConfiguration: Optional[AzureBlobSasConfiguration] = None
    BlobType: Optional[Literal['BLOCK']] = None
    AccessTier: Optional[AzureAccessTierType] = None
    AgentArns: Optional[List[str]] = None


# This class is the input for the 'create_location_object_storage' function.
class CreateLocationObjectStorageRequest(BaseValidatorModel):
    ServerHostname: str
    BucketName: str
    AgentArns: List[str]
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None
    ServerCertificate: Optional[Blob] = None


class UpdateLocationObjectStorageRequest(BaseValidatorModel):
    LocationArn: str
    ServerPort: Optional[int] = None
    ServerProtocol: Optional[ObjectStorageServerProtocolType] = None
    Subdirectory: Optional[str] = None
    ServerHostname: Optional[str] = None
    AccessKey: Optional[str] = None
    SecretKey: Optional[str] = None
    AgentArns: Optional[List[str]] = None
    ServerCertificate: Optional[Blob] = None


# This class is the input for the 'create_location_hdfs' function.
class CreateLocationHdfsRequest(BaseValidatorModel):
    NameNodes: List[HdfsNameNode]
    AuthenticationType: HdfsAuthenticationTypeType
    AgentArns: List[str]
    Subdirectory: Optional[str] = None
    BlockSize: Optional[int] = None
    ReplicationFactor: Optional[int] = None
    KmsKeyProviderUri: Optional[str] = None
    QopConfiguration: Optional[QopConfiguration] = None
    SimpleUser: Optional[str] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None
    Tags: Optional[List[TagListEntry]] = None


# This class is the output for the 'describe_location_hdfs' function.
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
    NameNodes: Optional[List[HdfsNameNode]] = None
    BlockSize: Optional[int] = None
    ReplicationFactor: Optional[int] = None
    KmsKeyProviderUri: Optional[str] = None
    QopConfiguration: Optional[QopConfiguration] = None
    AuthenticationType: Optional[HdfsAuthenticationTypeType] = None
    SimpleUser: Optional[str] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None
    AgentArns: Optional[List[str]] = None


class FsxProtocolNfs(BaseValidatorModel):
    MountOptions: Optional[NfsMountOptions] = None


# This class is the input for the 'create_location_s3' function.
class CreateLocationS3Request(BaseValidatorModel):
    S3BucketArn: str
    S3Config: S3Config
    Subdirectory: Optional[str] = None
    S3StorageClass: Optional[S3StorageClassType] = None
    AgentArns: Optional[List[str]] = None
    Tags: Optional[List[TagListEntry]] = None


# This class is the output for the 'describe_location_s3' function.
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


# This class is the input for the 'create_location_smb' function.
class CreateLocationSmbRequest(BaseValidatorModel):
    Subdirectory: str
    ServerHostname: str
    AgentArns: List[str]
    User: Optional[str] = None
    Domain: Optional[str] = None
    Password: Optional[str] = None
    MountOptions: Optional[SmbMountOptions] = None
    Tags: Optional[List[TagListEntry]] = None
    AuthenticationType: Optional[SmbAuthenticationTypeType] = None
    DnsIpAddresses: Optional[List[str]] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None


# This class is the output for the 'describe_location_smb' function.
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
    AgentArns: Optional[List[str]] = None
    MountOptions: Optional[SmbMountOptions] = None
    AuthenticationType: Optional[SmbAuthenticationTypeType] = None
    DnsIpAddresses: Optional[List[str]] = None
    KerberosPrincipal: Optional[str] = None
    KerberosKeytab: Optional[Blob] = None
    KerberosKrb5Conf: Optional[Blob] = None


class UpdateTaskExecutionRequest(BaseValidatorModel):
    TaskExecutionArn: str
    Options: Options


# This class is the output for the 'describe_agent' function.
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


# This class is the output for the 'describe_location_efs' function.
class DescribeLocationEfsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    Ec2Config: Ec2ConfigOutput
    CreationTime: datetime
    AccessPointArn: str
    FileSystemAccessRoleArn: str
    InTransitEncryption: EfsInTransitEncryptionType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_location_nfs' function.
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


class DescribeStorageSystemResourceMetricsRequestPaginate(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_storage_system_resource_metrics' function.
class DescribeStorageSystemResourceMetricsRequest(BaseValidatorModel):
    DiscoveryJobArn: str
    ResourceType: DiscoveryResourceTypeType
    ResourceId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_discovery_jobs' function.
class ListDiscoveryJobsResponse(BaseValidatorModel):
    DiscoveryJobs: List[DiscoveryJobListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

Ec2ConfigUnion = Union[Ec2Config, Ec2ConfigOutput]


class ListLocationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[LocationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_locations' function.
class ListLocationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[LocationFilter]] = None


# This class is the output for the 'list_locations' function.
class ListLocationsResponse(BaseValidatorModel):
    Locations: List[LocationListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_storage_systems' function.
class ListStorageSystemsResponse(BaseValidatorModel):
    StorageSystems: List[StorageSystemListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_task_executions' function.
class ListTaskExecutionsResponse(BaseValidatorModel):
    TaskExecutions: List[TaskExecutionListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTasksRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[TaskFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_tasks' function.
class ListTasksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[TaskFilter]] = None


# This class is the output for the 'list_tasks' function.
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

OnPremConfigUnion = Union[OnPremConfig, OnPremConfigOutput]


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


# This class is the output for the 'list_agents' function.
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


# This class is the input for the 'create_location_efs' function.
class CreateLocationEfsRequest(BaseValidatorModel):
    EfsFilesystemArn: str
    Ec2Config: Ec2ConfigUnion
    Subdirectory: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None
    AccessPointArn: Optional[str] = None
    FileSystemAccessRoleArn: Optional[str] = None
    InTransitEncryption: Optional[EfsInTransitEncryptionType] = None


class ResourceDetails(BaseValidatorModel):
    NetAppONTAPSVMs: Optional[List[NetAppONTAPSVM]] = None
    NetAppONTAPVolumes: Optional[List[NetAppONTAPVolume]] = None
    NetAppONTAPClusters: Optional[List[NetAppONTAPCluster]] = None


# This class is the input for the 'create_location_nfs' function.
class CreateLocationNfsRequest(BaseValidatorModel):
    Subdirectory: str
    ServerHostname: str
    OnPremConfig: OnPremConfigUnion
    MountOptions: Optional[NfsMountOptions] = None
    Tags: Optional[List[TagListEntry]] = None


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
    Action: Optional[Literal['TRANSFER']] = None
    Format: Optional[Literal['CSV']] = None
    Source: Optional[SourceManifestConfig] = None


# This class is the input for the 'create_location_fsx_ontap' function.
class CreateLocationFsxOntapRequest(BaseValidatorModel):
    Protocol: FsxProtocol
    SecurityGroupArns: List[str]
    StorageVirtualMachineArn: str
    Subdirectory: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None


# This class is the input for the 'create_location_fsx_open_zfs' function.
class CreateLocationFsxOpenZfsRequest(BaseValidatorModel):
    FsxFilesystemArn: str
    Protocol: FsxProtocol
    SecurityGroupArns: List[str]
    Subdirectory: Optional[str] = None
    Tags: Optional[List[TagListEntry]] = None


# This class is the output for the 'describe_location_fsx_ontap' function.
class DescribeLocationFsxOntapResponse(BaseValidatorModel):
    CreationTime: datetime
    LocationArn: str
    LocationUri: str
    Protocol: FsxProtocol
    SecurityGroupArns: List[str]
    StorageVirtualMachineArn: str
    FsxFilesystemArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_location_fsx_open_zfs' function.
class DescribeLocationFsxOpenZfsResponse(BaseValidatorModel):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    Protocol: FsxProtocol
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateLocationFsxOpenZfsRequest(BaseValidatorModel):
    LocationArn: str
    Protocol: Optional[FsxProtocol] = None
    Subdirectory: Optional[str] = None


class UpdateLocationFsxOntapRequest(BaseValidatorModel):
    LocationArn: str
    Protocol: Optional[FsxUpdateProtocol] = None
    Subdirectory: Optional[str] = None


# This class is the output for the 'describe_storage_system_resources' function.
class DescribeStorageSystemResourcesResponse(BaseValidatorModel):
    ResourceDetails: ResourceDetails
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_storage_system_resource_metrics' function.
class DescribeStorageSystemResourceMetricsResponse(BaseValidatorModel):
    Metrics: List[ResourceMetrics]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_task' function.
class CreateTaskRequest(BaseValidatorModel):
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: Optional[str] = None
    Name: Optional[str] = None
    Options: Optional[Options] = None
    Excludes: Optional[List[FilterRule]] = None
    Schedule: Optional[TaskSchedule] = None
    Tags: Optional[List[TagListEntry]] = None
    Includes: Optional[List[FilterRule]] = None
    ManifestConfig: Optional[ManifestConfig] = None
    TaskReportConfig: Optional[TaskReportConfig] = None
    TaskMode: Optional[TaskModeType] = None


# This class is the output for the 'describe_task_execution' function.
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


# This class is the output for the 'describe_task' function.
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


# This class is the input for the 'start_task_execution' function.
class StartTaskExecutionRequest(BaseValidatorModel):
    TaskArn: str
    OverrideOptions: Optional[Options] = None
    Includes: Optional[List[FilterRule]] = None
    Excludes: Optional[List[FilterRule]] = None
    ManifestConfig: Optional[ManifestConfig] = None
    TaskReportConfig: Optional[TaskReportConfig] = None
    Tags: Optional[List[TagListEntry]] = None


class UpdateTaskRequest(BaseValidatorModel):
    TaskArn: str
    Options: Optional[Options] = None
    Excludes: Optional[List[FilterRule]] = None
    Schedule: Optional[TaskSchedule] = None
    Name: Optional[str] = None
    CloudWatchLogGroupArn: Optional[str] = None
    Includes: Optional[List[FilterRule]] = None
    ManifestConfig: Optional[ManifestConfig] = None
    TaskReportConfig: Optional[TaskReportConfig] = None