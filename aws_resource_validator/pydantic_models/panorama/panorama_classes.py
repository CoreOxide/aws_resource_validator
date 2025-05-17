from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.panorama.panorama_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AlternateSoftwareMetadata(BaseValidatorModel):
    Version: Optional[str] = None


class ReportedRuntimeContextState(BaseValidatorModel):
    DesiredState: DesiredStateType
    DeviceReportedStatus: DeviceReportedStatusType
    DeviceReportedTime: datetime
    RuntimeContextName: str


class ManifestOverridesPayload(BaseValidatorModel):
    PayloadData: Optional[str] = None


class ManifestPayload(BaseValidatorModel):
    PayloadData: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Job(BaseValidatorModel):
    DeviceId: Optional[str] = None
    JobId: Optional[str] = None


# This class is the input for the 'create_package' function.
class CreatePackageRequest(BaseValidatorModel):
    PackageName: str
    Tags: Optional[Dict[str, str]] = None


class StorageLocation(BaseValidatorModel):
    BinaryPrefixLocation: str
    Bucket: str
    GeneratedPrefixLocation: str
    ManifestPrefixLocation: str
    RepoPrefixLocation: str


# This class is the input for the 'delete_device' function.
class DeleteDeviceRequest(BaseValidatorModel):
    DeviceId: str


class DeletePackageRequest(BaseValidatorModel):
    PackageId: str
    ForceDelete: Optional[bool] = None


class DeregisterPackageVersionRequest(BaseValidatorModel):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    OwnerAccount: Optional[str] = None
    UpdatedLatestPatchVersion: Optional[str] = None


# This class is the input for the 'describe_application_instance_details' function.
class DescribeApplicationInstanceDetailsRequest(BaseValidatorModel):
    ApplicationInstanceId: str


# This class is the input for the 'describe_application_instance' function.
class DescribeApplicationInstanceRequest(BaseValidatorModel):
    ApplicationInstanceId: str


# This class is the input for the 'describe_device_job' function.
class DescribeDeviceJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_device' function.
class DescribeDeviceRequest(BaseValidatorModel):
    DeviceId: str


class LatestDeviceJob(BaseValidatorModel):
    ImageVersion: Optional[str] = None
    JobType: Optional[JobTypeType] = None
    Status: Optional[UpdateProgressType] = None


# This class is the input for the 'describe_node_from_template_job' function.
class DescribeNodeFromTemplateJobRequest(BaseValidatorModel):
    JobId: str


class JobResourceTagsOutput(BaseValidatorModel):
    ResourceType: Literal['PACKAGE']
    Tags: Dict[str, str]


# This class is the input for the 'describe_node' function.
class DescribeNodeRequest(BaseValidatorModel):
    NodeId: str
    OwnerAccount: Optional[str] = None


# This class is the input for the 'describe_package_import_job' function.
class DescribePackageImportJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_package' function.
class DescribePackageRequest(BaseValidatorModel):
    PackageId: str


# This class is the input for the 'describe_package_version' function.
class DescribePackageVersionRequest(BaseValidatorModel):
    PackageId: str
    PackageVersion: str
    OwnerAccount: Optional[str] = None
    PatchVersion: Optional[str] = None


class OTAJobConfig(BaseValidatorModel):
    ImageVersion: str
    AllowMajorVersionUpdate: Optional[bool] = None


class DeviceJob(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    DeviceId: Optional[str] = None
    DeviceName: Optional[str] = None
    JobId: Optional[str] = None
    JobType: Optional[JobTypeType] = None


class StaticIpConnectionInfoOutput(BaseValidatorModel):
    DefaultGateway: str
    Dns: List[str]
    IpAddress: str
    Mask: str


class StaticIpConnectionInfo(BaseValidatorModel):
    DefaultGateway: str
    Dns: List[str]
    IpAddress: str
    Mask: str


class EthernetStatus(BaseValidatorModel):
    ConnectionStatus: Optional[NetworkConnectionStatusType] = None
    HwAddress: Optional[str] = None
    IpAddress: Optional[str] = None


class JobResourceTags(BaseValidatorModel):
    ResourceType: Literal['PACKAGE']
    Tags: Dict[str, str]


# This class is the input for the 'list_application_instance_dependencies' function.
class ListApplicationInstanceDependenciesRequest(BaseValidatorModel):
    ApplicationInstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PackageObject(BaseValidatorModel):
    Name: str
    PackageVersion: str
    PatchVersion: str


# This class is the input for the 'list_application_instance_node_instances' function.
class ListApplicationInstanceNodeInstancesRequest(BaseValidatorModel):
    ApplicationInstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NodeInstance(BaseValidatorModel):
    CurrentStatus: NodeInstanceStatusType
    NodeInstanceId: str
    NodeId: Optional[str] = None
    NodeName: Optional[str] = None
    PackageName: Optional[str] = None
    PackagePatchVersion: Optional[str] = None
    PackageVersion: Optional[str] = None


# This class is the input for the 'list_application_instances' function.
class ListApplicationInstancesRequest(BaseValidatorModel):
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[StatusFilterType] = None


# This class is the input for the 'list_devices_jobs' function.
class ListDevicesJobsRequest(BaseValidatorModel):
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_devices' function.
class ListDevicesRequest(BaseValidatorModel):
    DeviceAggregatedStatusFilter: Optional[DeviceAggregatedStatusType] = None
    MaxResults: Optional[int] = None
    NameFilter: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ListDevicesSortByType] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_node_from_template_jobs' function.
class ListNodeFromTemplateJobsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NodeFromTemplateJob(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    JobId: Optional[str] = None
    NodeName: Optional[str] = None
    Status: Optional[NodeFromTemplateJobStatusType] = None
    StatusMessage: Optional[str] = None
    TemplateType: Optional[Literal['RTSP_CAMERA_STREAM']] = None


# This class is the input for the 'list_nodes' function.
class ListNodesRequest(BaseValidatorModel):
    Category: Optional[NodeCategoryType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerAccount: Optional[str] = None
    PackageName: Optional[str] = None
    PackageVersion: Optional[str] = None
    PatchVersion: Optional[str] = None


class Node(BaseValidatorModel):
    Category: NodeCategoryType
    CreatedTime: datetime
    Name: str
    NodeId: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    Description: Optional[str] = None
    OwnerAccount: Optional[str] = None
    PackageArn: Optional[str] = None


# This class is the input for the 'list_package_import_jobs' function.
class ListPackageImportJobsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PackageImportJob(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    JobId: Optional[str] = None
    JobType: Optional[PackageImportJobTypeType] = None
    LastUpdatedTime: Optional[datetime] = None
    Status: Optional[PackageImportJobStatusType] = None
    StatusMessage: Optional[str] = None


# This class is the input for the 'list_packages' function.
class ListPackagesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PackageListItem(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    PackageId: Optional[str] = None
    PackageName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class NtpPayloadOutput(BaseValidatorModel):
    NtpServers: List[str]


class NtpPayload(BaseValidatorModel):
    NtpServers: List[str]


class NtpStatus(BaseValidatorModel):
    ConnectionStatus: Optional[NetworkConnectionStatusType] = None
    IpAddress: Optional[str] = None
    NtpServerName: Optional[str] = None


class NodeInputPort(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    MaxConnections: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[PortTypeType] = None


class NodeOutputPort(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[PortTypeType] = None


class NodeSignal(BaseValidatorModel):
    NodeInstanceId: str
    Signal: NodeSignalValueType


class OutPutS3Location(BaseValidatorModel):
    BucketName: str
    ObjectKey: str


class PackageVersionOutputConfig(BaseValidatorModel):
    PackageName: str
    PackageVersion: str
    MarkLatest: Optional[bool] = None


class S3Location(BaseValidatorModel):
    BucketName: str
    ObjectKey: str
    Region: Optional[str] = None


class RegisterPackageVersionRequest(BaseValidatorModel):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    MarkLatest: Optional[bool] = None
    OwnerAccount: Optional[str] = None


class RemoveApplicationInstanceRequest(BaseValidatorModel):
    ApplicationInstanceId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_device_metadata' function.
class UpdateDeviceMetadataRequest(BaseValidatorModel):
    DeviceId: str
    Description: Optional[str] = None


class ApplicationInstance(BaseValidatorModel):
    ApplicationInstanceId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    DefaultRuntimeContextDevice: Optional[str] = None
    DefaultRuntimeContextDeviceName: Optional[str] = None
    Description: Optional[str] = None
    HealthStatus: Optional[ApplicationInstanceHealthStatusType] = None
    Name: Optional[str] = None
    RuntimeContextStates: Optional[List[ReportedRuntimeContextState]] = None
    Status: Optional[ApplicationInstanceStatusType] = None
    StatusDescription: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_application_instance' function.
class CreateApplicationInstanceRequest(BaseValidatorModel):
    DefaultRuntimeContextDevice: str
    ManifestPayload: ManifestPayload
    ApplicationInstanceIdToReplace: Optional[str] = None
    Description: Optional[str] = None
    ManifestOverridesPayload: Optional[ManifestOverridesPayload] = None
    Name: Optional[str] = None
    RuntimeRoleArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_application_instance' function.
class CreateApplicationInstanceResponse(BaseValidatorModel):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_node_from_template_job' function.
class CreateNodeFromTemplateJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_package_import_job' function.
class CreatePackageImportJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_device' function.
class DeleteDeviceResponse(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_application_instance_details' function.
class DescribeApplicationInstanceDetailsResponse(BaseValidatorModel):
    ApplicationInstanceId: str
    ApplicationInstanceIdToReplace: str
    CreatedTime: datetime
    DefaultRuntimeContextDevice: str
    Description: str
    ManifestOverridesPayload: ManifestOverridesPayload
    ManifestPayload: ManifestPayload
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_application_instance' function.
class DescribeApplicationInstanceResponse(BaseValidatorModel):
    ApplicationInstanceId: str
    ApplicationInstanceIdToReplace: str
    Arn: str
    CreatedTime: datetime
    DefaultRuntimeContextDevice: str
    DefaultRuntimeContextDeviceName: str
    Description: str
    HealthStatus: ApplicationInstanceHealthStatusType
    LastUpdatedTime: datetime
    Name: str
    RuntimeContextStates: List[ReportedRuntimeContextState]
    RuntimeRoleArn: str
    Status: ApplicationInstanceStatusType
    StatusDescription: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_device_job' function.
class DescribeDeviceJobResponse(BaseValidatorModel):
    CreatedTime: datetime
    DeviceArn: str
    DeviceId: str
    DeviceName: str
    DeviceType: DeviceTypeType
    ImageVersion: str
    JobId: str
    JobType: JobTypeType
    Status: UpdateProgressType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_package_version' function.
class DescribePackageVersionResponse(BaseValidatorModel):
    IsLatestPatch: bool
    OwnerAccount: str
    PackageArn: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    RegisteredTime: datetime
    Status: PackageVersionStatusType
    StatusDescription: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'provision_device' function.
class ProvisionDeviceResponse(BaseValidatorModel):
    Arn: str
    Certificates: bytes
    DeviceId: str
    IotThingName: str
    Status: DeviceStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'signal_application_instance_node_instances' function.
class SignalApplicationInstanceNodeInstancesResponse(BaseValidatorModel):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_device_metadata' function.
class UpdateDeviceMetadataResponse(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_job_for_devices' function.
class CreateJobForDevicesResponse(BaseValidatorModel):
    Jobs: List[Job]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_package' function.
class CreatePackageResponse(BaseValidatorModel):
    Arn: str
    PackageId: str
    StorageLocation: StorageLocation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_package' function.
class DescribePackageResponse(BaseValidatorModel):
    Arn: str
    CreatedTime: datetime
    PackageId: str
    PackageName: str
    ReadAccessPrincipalArns: List[str]
    StorageLocation: StorageLocation
    Tags: Dict[str, str]
    WriteAccessPrincipalArns: List[str]
    ResponseMetadata: ResponseMetadata


class Device(BaseValidatorModel):
    Brand: Optional[DeviceBrandType] = None
    CreatedTime: Optional[datetime] = None
    CurrentSoftware: Optional[str] = None
    Description: Optional[str] = None
    DeviceAggregatedStatus: Optional[DeviceAggregatedStatusType] = None
    DeviceId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    LatestDeviceJob: Optional[LatestDeviceJob] = None
    LeaseExpirationTime: Optional[datetime] = None
    Name: Optional[str] = None
    ProvisioningStatus: Optional[DeviceStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    Type: Optional[DeviceTypeType] = None


# This class is the output for the 'describe_node_from_template_job' function.
class DescribeNodeFromTemplateJobResponse(BaseValidatorModel):
    CreatedTime: datetime
    JobId: str
    JobTags: List[JobResourceTagsOutput]
    LastUpdatedTime: datetime
    NodeDescription: str
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    Status: NodeFromTemplateJobStatusType
    StatusMessage: str
    TemplateParameters: Dict[str, str]
    TemplateType: Literal['RTSP_CAMERA_STREAM']
    ResponseMetadata: ResponseMetadata


class DeviceJobConfig(BaseValidatorModel):
    OTAJobConfig: Optional[OTAJobConfig] = None


# This class is the output for the 'list_devices_jobs' function.
class ListDevicesJobsResponse(BaseValidatorModel):
    DeviceJobs: List[DeviceJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EthernetPayloadOutput(BaseValidatorModel):
    ConnectionType: ConnectionTypeType
    StaticIpConnectionInfo: Optional[StaticIpConnectionInfoOutput] = None


class EthernetPayload(BaseValidatorModel):
    ConnectionType: ConnectionTypeType
    StaticIpConnectionInfo: Optional[StaticIpConnectionInfo] = None

JobResourceTagsUnion = Union[JobResourceTags, JobResourceTagsOutput]


# This class is the output for the 'list_application_instance_dependencies' function.
class ListApplicationInstanceDependenciesResponse(BaseValidatorModel):
    PackageObjects: List[PackageObject]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_application_instance_node_instances' function.
class ListApplicationInstanceNodeInstancesResponse(BaseValidatorModel):
    NodeInstances: List[NodeInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_node_from_template_jobs' function.
class ListNodeFromTemplateJobsResponse(BaseValidatorModel):
    NodeFromTemplateJobs: List[NodeFromTemplateJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_nodes' function.
class ListNodesResponse(BaseValidatorModel):
    Nodes: List[Node]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_package_import_jobs' function.
class ListPackageImportJobsResponse(BaseValidatorModel):
    PackageImportJobs: List[PackageImportJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_packages' function.
class ListPackagesResponse(BaseValidatorModel):
    Packages: List[PackageListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NetworkStatus(BaseValidatorModel):
    Ethernet0Status: Optional[EthernetStatus] = None
    Ethernet1Status: Optional[EthernetStatus] = None
    LastUpdatedTime: Optional[datetime] = None
    NtpStatus: Optional[NtpStatus] = None


class NodeInterface(BaseValidatorModel):
    Inputs: List[NodeInputPort]
    Outputs: List[NodeOutputPort]


# This class is the input for the 'signal_application_instance_node_instances' function.
class SignalApplicationInstanceNodeInstancesRequest(BaseValidatorModel):
    ApplicationInstanceId: str
    NodeSignals: List[NodeSignal]


class PackageImportJobOutput(BaseValidatorModel):
    OutputS3Location: OutPutS3Location
    PackageId: str
    PackageVersion: str
    PatchVersion: str


class PackageImportJobOutputConfig(BaseValidatorModel):
    PackageVersionOutputConfig: Optional[PackageVersionOutputConfig] = None


class PackageVersionInputConfig(BaseValidatorModel):
    S3Location: S3Location


# This class is the output for the 'list_application_instances' function.
class ListApplicationInstancesResponse(BaseValidatorModel):
    ApplicationInstances: List[ApplicationInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_devices' function.
class ListDevicesResponse(BaseValidatorModel):
    Devices: List[Device]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_job_for_devices' function.
class CreateJobForDevicesRequest(BaseValidatorModel):
    DeviceIds: List[str]
    JobType: JobTypeType
    DeviceJobConfig: Optional[DeviceJobConfig] = None


class NetworkPayloadOutput(BaseValidatorModel):
    Ethernet0: Optional[EthernetPayloadOutput] = None
    Ethernet1: Optional[EthernetPayloadOutput] = None
    Ntp: Optional[NtpPayloadOutput] = None


class NetworkPayload(BaseValidatorModel):
    Ethernet0: Optional[EthernetPayload] = None
    Ethernet1: Optional[EthernetPayload] = None
    Ntp: Optional[NtpPayload] = None


# This class is the input for the 'create_node_from_template_job' function.
class CreateNodeFromTemplateJobRequest(BaseValidatorModel):
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    TemplateParameters: Dict[str, str]
    TemplateType: Literal['RTSP_CAMERA_STREAM']
    JobTags: Optional[List[JobResourceTagsUnion]] = None
    NodeDescription: Optional[str] = None


# This class is the output for the 'describe_node' function.
class DescribeNodeResponse(BaseValidatorModel):
    AssetName: str
    Category: NodeCategoryType
    CreatedTime: datetime
    Description: str
    LastUpdatedTime: datetime
    Name: str
    NodeId: str
    NodeInterface: NodeInterface
    OwnerAccount: str
    PackageArn: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    ResponseMetadata: ResponseMetadata


class PackageImportJobInputConfig(BaseValidatorModel):
    PackageVersionInputConfig: Optional[PackageVersionInputConfig] = None


# This class is the output for the 'describe_device' function.
class DescribeDeviceResponse(BaseValidatorModel):
    AlternateSoftwares: List[AlternateSoftwareMetadata]
    Arn: str
    Brand: DeviceBrandType
    CreatedTime: datetime
    CurrentNetworkingStatus: NetworkStatus
    CurrentSoftware: str
    Description: str
    DeviceAggregatedStatus: DeviceAggregatedStatusType
    DeviceConnectionStatus: DeviceConnectionStatusType
    DeviceId: str
    LatestAlternateSoftware: str
    LatestDeviceJob: LatestDeviceJob
    LatestSoftware: str
    LeaseExpirationTime: datetime
    Name: str
    NetworkingConfiguration: NetworkPayloadOutput
    ProvisioningStatus: DeviceStatusType
    SerialNumber: str
    Tags: Dict[str, str]
    Type: DeviceTypeType
    ResponseMetadata: ResponseMetadata

NetworkPayloadUnion = Union[NetworkPayload, NetworkPayloadOutput]


# This class is the input for the 'create_package_import_job' function.
class CreatePackageImportJobRequest(BaseValidatorModel):
    ClientToken: str
    InputConfig: PackageImportJobInputConfig
    JobType: PackageImportJobTypeType
    OutputConfig: PackageImportJobOutputConfig
    JobTags: Optional[List[JobResourceTagsUnion]] = None


# This class is the output for the 'describe_package_import_job' function.
class DescribePackageImportJobResponse(BaseValidatorModel):
    ClientToken: str
    CreatedTime: datetime
    InputConfig: PackageImportJobInputConfig
    JobId: str
    JobTags: List[JobResourceTagsOutput]
    JobType: PackageImportJobTypeType
    LastUpdatedTime: datetime
    Output: PackageImportJobOutput
    OutputConfig: PackageImportJobOutputConfig
    Status: PackageImportJobStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'provision_device' function.
class ProvisionDeviceRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    NetworkingConfiguration: Optional[NetworkPayloadUnion] = None
    Tags: Optional[Dict[str, str]] = None