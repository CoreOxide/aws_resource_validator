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
from aws_resource_validator.pydantic_models.panorama_constants import *

class AlternateSoftwareMetadataTypeDef(BaseValidatorModel):
    Version: Optional[str] = None

class ReportedRuntimeContextStateTypeDef(BaseValidatorModel):
    DesiredState: DesiredStateType
    DeviceReportedStatus: DeviceReportedStatusType
    DeviceReportedTime: datetime
    RuntimeContextName: str

class ManifestOverridesPayloadTypeDef(BaseValidatorModel):
    PayloadData: Optional[str] = None

class ManifestPayloadTypeDef(BaseValidatorModel):
    PayloadData: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class JobTypeDef(BaseValidatorModel):
    DeviceId: Optional[str] = None
    JobId: Optional[str] = None

class JobResourceTagsTypeDef(BaseValidatorModel):
    ResourceType: Literal["PACKAGE"]
    Tags: Mapping[str, str]

class CreatePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageName: str
    Tags: Optional[Mapping[str, str]] = None

class StorageLocationTypeDef(BaseValidatorModel):
    BinaryPrefixLocation: str
    Bucket: str
    GeneratedPrefixLocation: str
    ManifestPrefixLocation: str
    RepoPrefixLocation: str

class DeleteDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str

class DeletePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageId: str
    ForceDelete: Optional[bool] = None

class DeregisterPackageVersionRequestRequestTypeDef(BaseValidatorModel):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    OwnerAccount: Optional[str] = None
    UpdatedLatestPatchVersion: Optional[str] = None

class DescribeApplicationInstanceDetailsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str

class DescribeApplicationInstanceRequestRequestTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str

class DescribeDeviceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str

class LatestDeviceJobTypeDef(BaseValidatorModel):
    ImageVersion: Optional[str] = None
    JobType: Optional[JobTypeType] = None
    Status: Optional[UpdateProgressType] = None

class DescribeNodeFromTemplateJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeNodeRequestRequestTypeDef(BaseValidatorModel):
    NodeId: str
    OwnerAccount: Optional[str] = None

class DescribePackageImportJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribePackageRequestRequestTypeDef(BaseValidatorModel):
    PackageId: str

class DescribePackageVersionRequestRequestTypeDef(BaseValidatorModel):
    PackageId: str
    PackageVersion: str
    OwnerAccount: Optional[str] = None
    PatchVersion: Optional[str] = None

class OTAJobConfigTypeDef(BaseValidatorModel):
    ImageVersion: str
    AllowMajorVersionUpdate: Optional[bool] = None

class DeviceJobTypeDef(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    DeviceId: Optional[str] = None
    DeviceName: Optional[str] = None
    JobId: Optional[str] = None
    JobType: Optional[JobTypeType] = None

class StaticIpConnectionInfoTypeDef(BaseValidatorModel):
    DefaultGateway: str
    Dns: List[str]
    IpAddress: str
    Mask: str

class EthernetStatusTypeDef(BaseValidatorModel):
    ConnectionStatus: Optional[NetworkConnectionStatusType] = None
    HwAddress: Optional[str] = None
    IpAddress: Optional[str] = None

class ListApplicationInstanceDependenciesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageObjectTypeDef(BaseValidatorModel):
    Name: str
    PackageVersion: str
    PatchVersion: str

class ListApplicationInstanceNodeInstancesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NodeInstanceTypeDef(BaseValidatorModel):
    CurrentStatus: NodeInstanceStatusType
    NodeInstanceId: str
    NodeId: Optional[str] = None
    NodeName: Optional[str] = None
    PackageName: Optional[str] = None
    PackagePatchVersion: Optional[str] = None
    PackageVersion: Optional[str] = None

class ListApplicationInstancesRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[StatusFilterType] = None

class ListDevicesJobsRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    DeviceAggregatedStatusFilter: Optional[DeviceAggregatedStatusType] = None
    MaxResults: Optional[int] = None
    NameFilter: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ListDevicesSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListNodeFromTemplateJobsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NodeFromTemplateJobTypeDef(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    JobId: Optional[str] = None
    NodeName: Optional[str] = None
    Status: Optional[NodeFromTemplateJobStatusType] = None
    StatusMessage: Optional[str] = None
    TemplateType: Optional[Literal["RTSP_CAMERA_STREAM"]] = None

class ListNodesRequestRequestTypeDef(BaseValidatorModel):
    Category: Optional[NodeCategoryType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerAccount: Optional[str] = None
    PackageName: Optional[str] = None
    PackageVersion: Optional[str] = None
    PatchVersion: Optional[str] = None

class NodeTypeDef(BaseValidatorModel):
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

class ListPackageImportJobsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageImportJobTypeDef(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    JobId: Optional[str] = None
    JobType: Optional[PackageImportJobTypeType] = None
    LastUpdatedTime: Optional[datetime] = None
    Status: Optional[PackageImportJobStatusType] = None
    StatusMessage: Optional[str] = None

class ListPackagesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PackageListItemTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    PackageId: Optional[str] = None
    PackageName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class NtpPayloadTypeDef(BaseValidatorModel):
    NtpServers: List[str]

class NtpStatusTypeDef(BaseValidatorModel):
    ConnectionStatus: Optional[NetworkConnectionStatusType] = None
    IpAddress: Optional[str] = None
    NtpServerName: Optional[str] = None

class NodeInputPortTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    MaxConnections: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[PortTypeType] = None

class NodeOutputPortTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[PortTypeType] = None

class NodeSignalTypeDef(BaseValidatorModel):
    NodeInstanceId: str
    Signal: NodeSignalValueType

class OutPutS3LocationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKey: str

class PackageVersionOutputConfigTypeDef(BaseValidatorModel):
    PackageName: str
    PackageVersion: str
    MarkLatest: Optional[bool] = None

class S3LocationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKey: str
    Region: Optional[str] = None

class RegisterPackageVersionRequestRequestTypeDef(BaseValidatorModel):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    MarkLatest: Optional[bool] = None
    OwnerAccount: Optional[str] = None

class RemoveApplicationInstanceRequestRequestTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDeviceMetadataRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str
    Description: Optional[str] = None

class ApplicationInstanceTypeDef(BaseValidatorModel):
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

class CreateApplicationInstanceRequestRequestTypeDef(BaseValidatorModel):
    DefaultRuntimeContextDevice: str
    ManifestPayload: ManifestPayloadTypeDef
    ApplicationInstanceIdToReplace: Optional[str] = None
    Description: Optional[str] = None
    ManifestOverridesPayload: Optional[ManifestOverridesPayloadTypeDef] = None
    Name: Optional[str] = None
    RuntimeRoleArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateApplicationInstanceResponseTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeFromTemplateJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageImportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeviceResponseTypeDef(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationInstanceDetailsResponseTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str
    ApplicationInstanceIdToReplace: str
    CreatedTime: datetime
    DefaultRuntimeContextDevice: str
    Description: str
    ManifestOverridesPayload: ManifestOverridesPayloadTypeDef
    ManifestPayload: ManifestPayloadTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationInstanceResponseTypeDef(BaseValidatorModel):
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

class DescribeDeviceJobResponseTypeDef(BaseValidatorModel):
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

class DescribePackageVersionResponseTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionDeviceResponseTypeDef(BaseValidatorModel):
    Arn: str
    Certificates: bytes
    DeviceId: str
    IotThingName: str
    Status: DeviceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class SignalApplicationInstanceNodeInstancesResponseTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceMetadataResponseTypeDef(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobForDevicesResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeFromTemplateJobRequestRequestTypeDef(BaseValidatorModel):
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    TemplateParameters: Mapping[str, str]
    TemplateType: Literal["RTSP_CAMERA_STREAM"]
    JobTags: Optional[Sequence[JobResourceTagsTypeDef]] = None
    NodeDescription: Optional[str] = None

class DescribeNodeFromTemplateJobResponseTypeDef(BaseValidatorModel):
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

class CreatePackageResponseTypeDef(BaseValidatorModel):
    Arn: str
    PackageId: str
    StorageLocation: StorageLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedTime: datetime
    PackageId: str
    PackageName: str
    ReadAccessPrincipalArns: List[str]
    StorageLocation: StorageLocationTypeDef
    Tags: Dict[str, str]
    WriteAccessPrincipalArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceTypeDef(BaseValidatorModel):
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

class DeviceJobConfigTypeDef(BaseValidatorModel):
    OTAJobConfig: Optional[OTAJobConfigTypeDef] = None

class ListDevicesJobsResponseTypeDef(BaseValidatorModel):
    DeviceJobs: List[DeviceJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EthernetPayloadTypeDef(BaseValidatorModel):
    ConnectionType: ConnectionTypeType
    StaticIpConnectionInfo: Optional[StaticIpConnectionInfoTypeDef] = None

class ListApplicationInstanceDependenciesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PackageObjects: List[PackageObjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationInstanceNodeInstancesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NodeInstances: List[NodeInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNodeFromTemplateJobsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NodeFromTemplateJobs: List[NodeFromTemplateJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNodesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Nodes: List[NodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageImportJobsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PackageImportJobs: List[PackageImportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Packages: List[PackageListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkStatusTypeDef(BaseValidatorModel):
    Ethernet0Status: Optional[EthernetStatusTypeDef] = None
    Ethernet1Status: Optional[EthernetStatusTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    NtpStatus: Optional[NtpStatusTypeDef] = None

class NodeInterfaceTypeDef(BaseValidatorModel):
    Inputs: List[NodeInputPortTypeDef]
    Outputs: List[NodeOutputPortTypeDef]

class SignalApplicationInstanceNodeInstancesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationInstanceId: str
    NodeSignals: Sequence[NodeSignalTypeDef]

class PackageImportJobOutputTypeDef(BaseValidatorModel):
    OutputS3Location: OutPutS3LocationTypeDef
    PackageId: str
    PackageVersion: str
    PatchVersion: str

class PackageImportJobOutputConfigTypeDef(BaseValidatorModel):
    PackageVersionOutputConfig: Optional[PackageVersionOutputConfigTypeDef] = None

class PackageVersionInputConfigTypeDef(BaseValidatorModel):
    S3Location: S3LocationTypeDef

class ListApplicationInstancesResponseTypeDef(BaseValidatorModel):
    ApplicationInstances: List[ApplicationInstanceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseValidatorModel):
    Devices: List[DeviceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobForDevicesRequestRequestTypeDef(BaseValidatorModel):
    DeviceIds: Sequence[str]
    JobType: JobTypeType
    DeviceJobConfig: Optional[DeviceJobConfigTypeDef] = None

class NetworkPayloadTypeDef(BaseValidatorModel):
    Ethernet0: Optional[EthernetPayloadTypeDef] = None
    Ethernet1: Optional[EthernetPayloadTypeDef] = None
    Ntp: Optional[NtpPayloadTypeDef] = None

class DescribeNodeResponseTypeDef(BaseValidatorModel):
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

class PackageImportJobInputConfigTypeDef(BaseValidatorModel):
    PackageVersionInputConfig: Optional[PackageVersionInputConfigTypeDef] = None

class DescribeDeviceResponseTypeDef(BaseValidatorModel):
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

class ProvisionDeviceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    NetworkingConfiguration: Optional[NetworkPayloadTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreatePackageImportJobRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    InputConfig: PackageImportJobInputConfigTypeDef
    JobType: PackageImportJobTypeType
    OutputConfig: PackageImportJobOutputConfigTypeDef
    JobTags: Optional[Sequence[JobResourceTagsTypeDef]] = None

class DescribePackageImportJobResponseTypeDef(BaseValidatorModel):
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

