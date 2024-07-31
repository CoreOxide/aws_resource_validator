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
from aws_resource_validator.pydantic_models.panorama_constants import *

class AlternateSoftwareMetadataTypeDef(BaseModel):
    Version: Optional[str] = None

class ReportedRuntimeContextStateTypeDef(BaseModel):
    DesiredState: DesiredStateType
    DeviceReportedStatus: DeviceReportedStatusType
    DeviceReportedTime: datetime
    RuntimeContextName: str

class ManifestOverridesPayloadTypeDef(BaseModel):
    PayloadData: Optional[str] = None

class ManifestPayloadTypeDef(BaseModel):
    PayloadData: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class JobTypeDef(BaseModel):
    DeviceId: Optional[str] = None
    JobId: Optional[str] = None

class JobResourceTagsTypeDef(BaseModel):
    ResourceType: Literal["PACKAGE"]
    Tags: Mapping[str, str]

class CreatePackageRequestRequestTypeDef(BaseModel):
    PackageName: str
    Tags: Optional[Mapping[str, str]] = None

class StorageLocationTypeDef(BaseModel):
    BinaryPrefixLocation: str
    Bucket: str
    GeneratedPrefixLocation: str
    ManifestPrefixLocation: str
    RepoPrefixLocation: str

class DeleteDeviceRequestRequestTypeDef(BaseModel):
    DeviceId: str

class DeletePackageRequestRequestTypeDef(BaseModel):
    PackageId: str
    ForceDelete: Optional[bool] = None

class DeregisterPackageVersionRequestRequestTypeDef(BaseModel):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    OwnerAccount: Optional[str] = None
    UpdatedLatestPatchVersion: Optional[str] = None

class DescribeApplicationInstanceDetailsRequestRequestTypeDef(BaseModel):
    ApplicationInstanceId: str

class DescribeApplicationInstanceRequestRequestTypeDef(BaseModel):
    ApplicationInstanceId: str

class DescribeDeviceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeDeviceRequestRequestTypeDef(BaseModel):
    DeviceId: str

class LatestDeviceJobTypeDef(BaseModel):
    ImageVersion: Optional[str] = None
    JobType: Optional[JobTypeType] = None
    Status: Optional[UpdateProgressType] = None

class DescribeNodeFromTemplateJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeNodeRequestRequestTypeDef(BaseModel):
    NodeId: str
    OwnerAccount: Optional[str] = None

class DescribePackageImportJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribePackageRequestRequestTypeDef(BaseModel):
    PackageId: str

class DescribePackageVersionRequestRequestTypeDef(BaseModel):
    PackageId: str
    PackageVersion: str
    OwnerAccount: Optional[str] = None
    PatchVersion: Optional[str] = None

class OTAJobConfigTypeDef(BaseModel):
    ImageVersion: str
    AllowMajorVersionUpdate: Optional[bool] = None

class DeviceJobTypeDef(BaseModel):
    CreatedTime: Optional[datetime] = None
    DeviceId: Optional[str] = None
    DeviceName: Optional[str] = None
    JobId: Optional[str] = None
    JobType: Optional[JobTypeType] = None

class StaticIpConnectionInfoTypeDef(BaseModel):
    DefaultGateway: str
    Dns: List[str]
    IpAddress: str
    Mask: str

class EthernetStatusTypeDef(BaseModel):
    ConnectionStatus: Optional[NetworkConnectionStatusType] = None
    HwAddress: Optional[str] = None
    IpAddress: Optional[str] = None

class ListApplicationInstanceDependenciesRequestRequestTypeDef(BaseModel):
    ApplicationInstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageObjectTypeDef(BaseModel):
    Name: str
    PackageVersion: str
    PatchVersion: str

class ListApplicationInstanceNodeInstancesRequestRequestTypeDef(BaseModel):
    ApplicationInstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NodeInstanceTypeDef(BaseModel):
    CurrentStatus: NodeInstanceStatusType
    NodeInstanceId: str
    NodeId: Optional[str] = None
    NodeName: Optional[str] = None
    PackageName: Optional[str] = None
    PackagePatchVersion: Optional[str] = None
    PackageVersion: Optional[str] = None

class ListApplicationInstancesRequestRequestTypeDef(BaseModel):
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[StatusFilterType] = None

class ListDevicesJobsRequestRequestTypeDef(BaseModel):
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDevicesRequestRequestTypeDef(BaseModel):
    DeviceAggregatedStatusFilter: Optional[DeviceAggregatedStatusType] = None
    MaxResults: Optional[int] = None
    NameFilter: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ListDevicesSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListNodeFromTemplateJobsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NodeFromTemplateJobTypeDef(BaseModel):
    CreatedTime: Optional[datetime] = None
    JobId: Optional[str] = None
    NodeName: Optional[str] = None
    Status: Optional[NodeFromTemplateJobStatusType] = None
    StatusMessage: Optional[str] = None
    TemplateType: Optional[Literal["RTSP_CAMERA_STREAM"]] = None

class ListNodesRequestRequestTypeDef(BaseModel):
    Category: Optional[NodeCategoryType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerAccount: Optional[str] = None
    PackageName: Optional[str] = None
    PackageVersion: Optional[str] = None
    PatchVersion: Optional[str] = None

class NodeTypeDef(BaseModel):
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

class ListPackageImportJobsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageImportJobTypeDef(BaseModel):
    CreatedTime: Optional[datetime] = None
    JobId: Optional[str] = None
    JobType: Optional[PackageImportJobTypeType] = None
    LastUpdatedTime: Optional[datetime] = None
    Status: Optional[PackageImportJobStatusType] = None
    StatusMessage: Optional[str] = None

class ListPackagesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageListItemTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    PackageId: Optional[str] = None
    PackageName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class NtpPayloadTypeDef(BaseModel):
    NtpServers: List[str]

class NtpStatusTypeDef(BaseModel):
    ConnectionStatus: Optional[NetworkConnectionStatusType] = None
    IpAddress: Optional[str] = None
    NtpServerName: Optional[str] = None

class NodeInputPortTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    MaxConnections: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[PortTypeType] = None

class NodeOutputPortTypeDef(BaseModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[PortTypeType] = None

class NodeSignalTypeDef(BaseModel):
    NodeInstanceId: str
    Signal: NodeSignalValueType

class OutPutS3LocationTypeDef(BaseModel):
    BucketName: str
    ObjectKey: str

class PackageVersionOutputConfigTypeDef(BaseModel):
    PackageName: str
    PackageVersion: str
    MarkLatest: Optional[bool] = None

class S3LocationTypeDef(BaseModel):
    BucketName: str
    ObjectKey: str
    Region: Optional[str] = None

class RegisterPackageVersionRequestRequestTypeDef(BaseModel):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    MarkLatest: Optional[bool] = None
    OwnerAccount: Optional[str] = None

class RemoveApplicationInstanceRequestRequestTypeDef(BaseModel):
    ApplicationInstanceId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDeviceMetadataRequestRequestTypeDef(BaseModel):
    DeviceId: str
    Description: Optional[str] = None

class ApplicationInstanceTypeDef(BaseModel):
    ApplicationInstanceId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    DefaultRuntimeContextDevice: Optional[str] = None
    DefaultRuntimeContextDeviceName: Optional[str] = None
    Description: Optional[str] = None
    HealthStatus: Optional[ApplicationInstanceHealthStatusType] = None
    Name: Optional[str] = None
    RuntimeContextStates: Optional[List[ReportedRuntimeContextStateTypeDef]] = None
    Status: Optional[ApplicationInstanceStatusType] = None
    StatusDescription: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class CreateApplicationInstanceRequestRequestTypeDef(BaseModel):
    DefaultRuntimeContextDevice: str
    ManifestPayload: ManifestPayloadTypeDef
    ApplicationInstanceIdToReplace: Optional[str] = None
    Description: Optional[str] = None
    ManifestOverridesPayload: Optional[ManifestOverridesPayloadTypeDef] = None
    Name: Optional[str] = None
    RuntimeRoleArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateApplicationInstanceResponseTypeDef(BaseModel):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeFromTemplateJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageImportJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeviceResponseTypeDef(BaseModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationInstanceDetailsResponseTypeDef(BaseModel):
    ApplicationInstanceId: str
    ApplicationInstanceIdToReplace: str
    CreatedTime: datetime
    DefaultRuntimeContextDevice: str
    Description: str
    ManifestOverridesPayload: ManifestOverridesPayloadTypeDef
    ManifestPayload: ManifestPayloadTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationInstanceResponseTypeDef(BaseModel):
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
    RuntimeContextStates: List[ReportedRuntimeContextStateTypeDef]
    RuntimeRoleArn: str
    Status: ApplicationInstanceStatusType
    StatusDescription: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeviceJobResponseTypeDef(BaseModel):
    CreatedTime: datetime
    DeviceArn: str
    DeviceId: str
    DeviceName: str
    DeviceType: DeviceTypeType
    ImageVersion: str
    JobId: str
    JobType: JobTypeType
    Status: UpdateProgressType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageVersionResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionDeviceResponseTypeDef(BaseModel):
    Arn: str
    Certificates: bytes
    DeviceId: str
    IotThingName: str
    Status: DeviceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class SignalApplicationInstanceNodeInstancesResponseTypeDef(BaseModel):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceMetadataResponseTypeDef(BaseModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobForDevicesResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeFromTemplateJobRequestRequestTypeDef(BaseModel):
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    TemplateParameters: Mapping[str, str]
    TemplateType: Literal["RTSP_CAMERA_STREAM"]
    JobTags: Optional[Sequence[JobResourceTagsTypeDef]] = None
    NodeDescription: Optional[str] = None

class DescribeNodeFromTemplateJobResponseTypeDef(BaseModel):
    CreatedTime: datetime
    JobId: str
    JobTags: List[JobResourceTagsTypeDef]
    LastUpdatedTime: datetime
    NodeDescription: str
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    Status: NodeFromTemplateJobStatusType
    StatusMessage: str
    TemplateParameters: Dict[str, str]
    TemplateType: Literal["RTSP_CAMERA_STREAM"]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageResponseTypeDef(BaseModel):
    Arn: str
    PackageId: str
    StorageLocation: StorageLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageResponseTypeDef(BaseModel):
    Arn: str
    CreatedTime: datetime
    PackageId: str
    PackageName: str
    ReadAccessPrincipalArns: List[str]
    StorageLocation: StorageLocationTypeDef
    Tags: Dict[str, str]
    WriteAccessPrincipalArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceTypeDef(BaseModel):
    Brand: Optional[DeviceBrandType] = None
    CreatedTime: Optional[datetime] = None
    CurrentSoftware: Optional[str] = None
    Description: Optional[str] = None
    DeviceAggregatedStatus: Optional[DeviceAggregatedStatusType] = None
    DeviceId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    LatestDeviceJob: Optional[LatestDeviceJobTypeDef] = None
    LeaseExpirationTime: Optional[datetime] = None
    Name: Optional[str] = None
    ProvisioningStatus: Optional[DeviceStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    Type: Optional[DeviceTypeType] = None

class DeviceJobConfigTypeDef(BaseModel):
    OTAJobConfig: Optional[OTAJobConfigTypeDef] = None

class ListDevicesJobsResponseTypeDef(BaseModel):
    DeviceJobs: List[DeviceJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EthernetPayloadTypeDef(BaseModel):
    ConnectionType: ConnectionTypeType
    StaticIpConnectionInfo: Optional[StaticIpConnectionInfoTypeDef] = None

class ListApplicationInstanceDependenciesResponseTypeDef(BaseModel):
    NextToken: str
    PackageObjects: List[PackageObjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationInstanceNodeInstancesResponseTypeDef(BaseModel):
    NextToken: str
    NodeInstances: List[NodeInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNodeFromTemplateJobsResponseTypeDef(BaseModel):
    NextToken: str
    NodeFromTemplateJobs: List[NodeFromTemplateJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNodesResponseTypeDef(BaseModel):
    NextToken: str
    Nodes: List[NodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageImportJobsResponseTypeDef(BaseModel):
    NextToken: str
    PackageImportJobs: List[PackageImportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResponseTypeDef(BaseModel):
    NextToken: str
    Packages: List[PackageListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkStatusTypeDef(BaseModel):
    Ethernet0Status: Optional[EthernetStatusTypeDef] = None
    Ethernet1Status: Optional[EthernetStatusTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    NtpStatus: Optional[NtpStatusTypeDef] = None

class NodeInterfaceTypeDef(BaseModel):
    Inputs: List[NodeInputPortTypeDef]
    Outputs: List[NodeOutputPortTypeDef]

class SignalApplicationInstanceNodeInstancesRequestRequestTypeDef(BaseModel):
    ApplicationInstanceId: str
    NodeSignals: Sequence[NodeSignalTypeDef]

class PackageImportJobOutputTypeDef(BaseModel):
    OutputS3Location: OutPutS3LocationTypeDef
    PackageId: str
    PackageVersion: str
    PatchVersion: str

class PackageImportJobOutputConfigTypeDef(BaseModel):
    PackageVersionOutputConfig: Optional[PackageVersionOutputConfigTypeDef] = None

class PackageVersionInputConfigTypeDef(BaseModel):
    S3Location: S3LocationTypeDef

class ListApplicationInstancesResponseTypeDef(BaseModel):
    ApplicationInstances: List[ApplicationInstanceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseModel):
    Devices: List[DeviceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobForDevicesRequestRequestTypeDef(BaseModel):
    DeviceIds: Sequence[str]
    JobType: JobTypeType
    DeviceJobConfig: Optional[DeviceJobConfigTypeDef] = None

class NetworkPayloadTypeDef(BaseModel):
    Ethernet0: Optional[EthernetPayloadTypeDef] = None
    Ethernet1: Optional[EthernetPayloadTypeDef] = None
    Ntp: Optional[NtpPayloadTypeDef] = None

class DescribeNodeResponseTypeDef(BaseModel):
    AssetName: str
    Category: NodeCategoryType
    CreatedTime: datetime
    Description: str
    LastUpdatedTime: datetime
    Name: str
    NodeId: str
    NodeInterface: NodeInterfaceTypeDef
    OwnerAccount: str
    PackageArn: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class PackageImportJobInputConfigTypeDef(BaseModel):
    PackageVersionInputConfig: Optional[PackageVersionInputConfigTypeDef] = None

class DescribeDeviceResponseTypeDef(BaseModel):
    AlternateSoftwares: List[AlternateSoftwareMetadataTypeDef]
    Arn: str
    Brand: DeviceBrandType
    CreatedTime: datetime
    CurrentNetworkingStatus: NetworkStatusTypeDef
    CurrentSoftware: str
    Description: str
    DeviceAggregatedStatus: DeviceAggregatedStatusType
    DeviceConnectionStatus: DeviceConnectionStatusType
    DeviceId: str
    LatestAlternateSoftware: str
    LatestDeviceJob: LatestDeviceJobTypeDef
    LatestSoftware: str
    LeaseExpirationTime: datetime
    Name: str
    NetworkingConfiguration: NetworkPayloadTypeDef
    ProvisioningStatus: DeviceStatusType
    SerialNumber: str
    Tags: Dict[str, str]
    Type: DeviceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionDeviceRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    NetworkingConfiguration: Optional[NetworkPayloadTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreatePackageImportJobRequestRequestTypeDef(BaseModel):
    ClientToken: str
    InputConfig: PackageImportJobInputConfigTypeDef
    JobType: PackageImportJobTypeType
    OutputConfig: PackageImportJobOutputConfigTypeDef
    JobTags: Optional[Sequence[JobResourceTagsTypeDef]] = None

class DescribePackageImportJobResponseTypeDef(BaseModel):
    ClientToken: str
    CreatedTime: datetime
    InputConfig: PackageImportJobInputConfigTypeDef
    JobId: str
    JobTags: List[JobResourceTagsTypeDef]
    JobType: PackageImportJobTypeType
    LastUpdatedTime: datetime
    Output: PackageImportJobOutputTypeDef
    OutputConfig: PackageImportJobOutputConfigTypeDef
    Status: PackageImportJobStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

