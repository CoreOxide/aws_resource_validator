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
from aws_resource_validator.pydantic_models.opsworks_constants import *

class StackConfigurationManagerTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class DataSourceTypeDef(BaseModel):
    Type: Optional[str] = None
    Arn: Optional[str] = None
    DatabaseName: Optional[str] = None

class EnvironmentVariableTypeDef(BaseModel):
    Key: str
    Value: str
    Secure: Optional[bool] = None

class SourceTypeDef(BaseModel):
    Type: Optional[SourceTypeType] = None
    Url: Optional[str] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    SshKey: Optional[str] = None
    Revision: Optional[str] = None

class SslConfigurationTypeDef(BaseModel):
    Certificate: str
    PrivateKey: str
    Chain: Optional[str] = None

class AssignInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LayerIds: Sequence[str]

class AssignVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    InstanceId: Optional[str] = None

class AssociateElasticIpRequestRequestTypeDef(BaseModel):
    ElasticIp: str
    InstanceId: Optional[str] = None

class AttachElasticLoadBalancerRequestRequestTypeDef(BaseModel):
    ElasticLoadBalancerName: str
    LayerId: str

class AutoScalingThresholdsOutputTypeDef(BaseModel):
    InstanceCount: Optional[int] = None
    ThresholdsWaitTime: Optional[int] = None
    IgnoreMetricsTime: Optional[int] = None
    CpuThreshold: Optional[float] = None
    MemoryThreshold: Optional[float] = None
    LoadThreshold: Optional[float] = None
    Alarms: Optional[List[str]] = None

class AutoScalingThresholdsTypeDef(BaseModel):
    InstanceCount: Optional[int] = None
    ThresholdsWaitTime: Optional[int] = None
    IgnoreMetricsTime: Optional[int] = None
    CpuThreshold: Optional[float] = None
    MemoryThreshold: Optional[float] = None
    LoadThreshold: Optional[float] = None
    Alarms: Optional[Sequence[str]] = None

class EbsBlockDeviceTypeDef(BaseModel):
    SnapshotId: Optional[str] = None
    Iops: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    DeleteOnTermination: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ChefConfigurationTypeDef(BaseModel):
    ManageBerkshelf: Optional[bool] = None
    BerkshelfVersion: Optional[str] = None

class CloudWatchLogsLogStreamTypeDef(BaseModel):
    LogGroupName: Optional[str] = None
    DatetimeFormat: Optional[str] = None
    TimeZone: Optional[CloudWatchLogsTimeZoneType] = None
    File: Optional[str] = None
    FileFingerprintLines: Optional[str] = None
    MultiLineStartPattern: Optional[str] = None
    InitialPosition: Optional[CloudWatchLogsInitialPositionType] = None
    Encoding: Optional[CloudWatchLogsEncodingType] = None
    BufferDuration: Optional[int] = None
    BatchCount: Optional[int] = None
    BatchSize: Optional[int] = None

class CommandTypeDef(BaseModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    DeploymentId: Optional[str] = None
    CreatedAt: Optional[str] = None
    AcknowledgedAt: Optional[str] = None
    CompletedAt: Optional[str] = None
    Status: Optional[str] = None
    ExitCode: Optional[int] = None
    LogUrl: Optional[str] = None
    Type: Optional[str] = None

class DeploymentCommandTypeDef(BaseModel):
    Name: DeploymentCommandNameType
    Args: Optional[Mapping[str, Sequence[str]]] = None

class RecipesTypeDef(BaseModel):
    Setup: Optional[Sequence[str]] = None
    Configure: Optional[Sequence[str]] = None
    Deploy: Optional[Sequence[str]] = None
    Undeploy: Optional[Sequence[str]] = None
    Shutdown: Optional[Sequence[str]] = None

class VolumeConfigurationTypeDef(BaseModel):
    MountPoint: str
    NumberOfDisks: int
    Size: int
    RaidLevel: Optional[int] = None
    VolumeType: Optional[str] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None

class CreateUserProfileRequestRequestTypeDef(BaseModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None

class DeleteAppRequestRequestTypeDef(BaseModel):
    AppId: str

class DeleteInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DeleteElasticIp: Optional[bool] = None
    DeleteVolumes: Optional[bool] = None

class DeleteLayerRequestRequestTypeDef(BaseModel):
    LayerId: str

class DeleteStackRequestRequestTypeDef(BaseModel):
    StackId: str

class DeleteUserProfileRequestRequestTypeDef(BaseModel):
    IamUserArn: str

class DeploymentCommandOutputTypeDef(BaseModel):
    Name: DeploymentCommandNameType
    Args: Optional[Dict[str, List[str]]] = None

class DeregisterEcsClusterRequestRequestTypeDef(BaseModel):
    EcsClusterArn: str

class DeregisterElasticIpRequestRequestTypeDef(BaseModel):
    ElasticIp: str

class DeregisterInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class DeregisterRdsDbInstanceRequestRequestTypeDef(BaseModel):
    RdsDbInstanceArn: str

class DeregisterVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAppsRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    AppIds: Optional[Sequence[str]] = None

class DescribeCommandsRequestRequestTypeDef(BaseModel):
    DeploymentId: Optional[str] = None
    InstanceId: Optional[str] = None
    CommandIds: Optional[Sequence[str]] = None

class DescribeDeploymentsRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeEcsClustersRequestRequestTypeDef(BaseModel):
    EcsClusterArns: Optional[Sequence[str]] = None
    StackId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class EcsClusterTypeDef(BaseModel):
    EcsClusterArn: Optional[str] = None
    EcsClusterName: Optional[str] = None
    StackId: Optional[str] = None
    RegisteredAt: Optional[str] = None

class DescribeElasticIpsRequestRequestTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    Ips: Optional[Sequence[str]] = None

class ElasticIpTypeDef(BaseModel):
    Ip: Optional[str] = None
    Name: Optional[str] = None
    Domain: Optional[str] = None
    Region: Optional[str] = None
    InstanceId: Optional[str] = None

class DescribeElasticLoadBalancersRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerIds: Optional[Sequence[str]] = None

class ElasticLoadBalancerTypeDef(BaseModel):
    ElasticLoadBalancerName: Optional[str] = None
    Region: Optional[str] = None
    DnsName: Optional[str] = None
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    Ec2InstanceIds: Optional[List[str]] = None

class DescribeInstancesRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None

class DescribeLayersRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerIds: Optional[Sequence[str]] = None

class DescribeLoadBasedAutoScalingRequestRequestTypeDef(BaseModel):
    LayerIds: Sequence[str]

class SelfUserProfileTypeDef(BaseModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None

class DescribePermissionsRequestRequestTypeDef(BaseModel):
    IamUserArn: Optional[str] = None
    StackId: Optional[str] = None

class PermissionTypeDef(BaseModel):
    StackId: Optional[str] = None
    IamUserArn: Optional[str] = None
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None

class DescribeRaidArraysRequestRequestTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    RaidArrayIds: Optional[Sequence[str]] = None

class RaidArrayTypeDef(BaseModel):
    RaidArrayId: Optional[str] = None
    InstanceId: Optional[str] = None
    Name: Optional[str] = None
    RaidLevel: Optional[int] = None
    NumberOfDisks: Optional[int] = None
    Size: Optional[int] = None
    Device: Optional[str] = None
    MountPoint: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CreatedAt: Optional[str] = None
    StackId: Optional[str] = None
    VolumeType: Optional[str] = None
    Iops: Optional[int] = None

class DescribeRdsDbInstancesRequestRequestTypeDef(BaseModel):
    StackId: str
    RdsDbInstanceArns: Optional[Sequence[str]] = None

class RdsDbInstanceTypeDef(BaseModel):
    RdsDbInstanceArn: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None
    Region: Optional[str] = None
    Address: Optional[str] = None
    Engine: Optional[str] = None
    StackId: Optional[str] = None
    MissingOnRds: Optional[bool] = None

class DescribeServiceErrorsRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    ServiceErrorIds: Optional[Sequence[str]] = None

class ServiceErrorTypeDef(BaseModel):
    ServiceErrorId: Optional[str] = None
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None
    CreatedAt: Optional[str] = None

class DescribeStackProvisioningParametersRequestRequestTypeDef(BaseModel):
    StackId: str

class DescribeStackSummaryRequestRequestTypeDef(BaseModel):
    StackId: str

class DescribeStacksRequestRequestTypeDef(BaseModel):
    StackIds: Optional[Sequence[str]] = None

class DescribeTimeBasedAutoScalingRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]

class DescribeUserProfilesRequestRequestTypeDef(BaseModel):
    IamUserArns: Optional[Sequence[str]] = None

class UserProfileTypeDef(BaseModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None

class DescribeVolumesRequestRequestTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    RaidArrayId: Optional[str] = None
    VolumeIds: Optional[Sequence[str]] = None

class VolumeTypeDef(BaseModel):
    VolumeId: Optional[str] = None
    Ec2VolumeId: Optional[str] = None
    Name: Optional[str] = None
    RaidArrayId: Optional[str] = None
    InstanceId: Optional[str] = None
    Status: Optional[str] = None
    Size: Optional[int] = None
    Device: Optional[str] = None
    MountPoint: Optional[str] = None
    Region: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    VolumeType: Optional[str] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None

class DetachElasticLoadBalancerRequestRequestTypeDef(BaseModel):
    ElasticLoadBalancerName: str
    LayerId: str

class DisassociateElasticIpRequestRequestTypeDef(BaseModel):
    ElasticIp: str

class GetHostnameSuggestionRequestRequestTypeDef(BaseModel):
    LayerId: str

class GrantAccessRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ValidForInMinutes: Optional[int] = None

class TemporaryCredentialTypeDef(BaseModel):
    Username: Optional[str] = None
    Password: Optional[str] = None
    ValidForInMinutes: Optional[int] = None
    InstanceId: Optional[str] = None

class InstanceIdentityTypeDef(BaseModel):
    Document: Optional[str] = None
    Signature: Optional[str] = None

class ReportedOsTypeDef(BaseModel):
    Family: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None

class InstancesCountTypeDef(BaseModel):
    Assigning: Optional[int] = None
    Booting: Optional[int] = None
    ConnectionLost: Optional[int] = None
    Deregistering: Optional[int] = None
    Online: Optional[int] = None
    Pending: Optional[int] = None
    Rebooting: Optional[int] = None
    Registered: Optional[int] = None
    Registering: Optional[int] = None
    Requested: Optional[int] = None
    RunningSetup: Optional[int] = None
    SetupFailed: Optional[int] = None
    ShuttingDown: Optional[int] = None
    StartFailed: Optional[int] = None
    StopFailed: Optional[int] = None
    Stopped: Optional[int] = None
    Stopping: Optional[int] = None
    Terminated: Optional[int] = None
    Terminating: Optional[int] = None
    Unassigning: Optional[int] = None

class RecipesOutputTypeDef(BaseModel):
    Setup: Optional[List[str]] = None
    Configure: Optional[List[str]] = None
    Deploy: Optional[List[str]] = None
    Undeploy: Optional[List[str]] = None
    Shutdown: Optional[List[str]] = None

class ShutdownEventConfigurationTypeDef(BaseModel):
    ExecutionTimeout: Optional[int] = None
    DelayUntilElbConnectionsDrained: Optional[bool] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class OperatingSystemConfigurationManagerTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class RebootInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class RegisterEcsClusterRequestRequestTypeDef(BaseModel):
    EcsClusterArn: str
    StackId: str

class RegisterElasticIpRequestRequestTypeDef(BaseModel):
    ElasticIp: str
    StackId: str

class RegisterRdsDbInstanceRequestRequestTypeDef(BaseModel):
    StackId: str
    RdsDbInstanceArn: str
    DbUser: str
    DbPassword: str

class RegisterVolumeRequestRequestTypeDef(BaseModel):
    StackId: str
    Ec2VolumeId: Optional[str] = None

class SetPermissionRequestRequestTypeDef(BaseModel):
    StackId: str
    IamUserArn: str
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None

class WeeklyAutoScalingScheduleTypeDef(BaseModel):
    Monday: Optional[Mapping[str, str]] = None
    Tuesday: Optional[Mapping[str, str]] = None
    Wednesday: Optional[Mapping[str, str]] = None
    Thursday: Optional[Mapping[str, str]] = None
    Friday: Optional[Mapping[str, str]] = None
    Saturday: Optional[Mapping[str, str]] = None
    Sunday: Optional[Mapping[str, str]] = None

class StartInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class StartStackRequestRequestTypeDef(BaseModel):
    StackId: str

class StopInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Force: Optional[bool] = None

class StopStackRequestRequestTypeDef(BaseModel):
    StackId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class WeeklyAutoScalingScheduleOutputTypeDef(BaseModel):
    Monday: Optional[Dict[str, str]] = None
    Tuesday: Optional[Dict[str, str]] = None
    Wednesday: Optional[Dict[str, str]] = None
    Thursday: Optional[Dict[str, str]] = None
    Friday: Optional[Dict[str, str]] = None
    Saturday: Optional[Dict[str, str]] = None
    Sunday: Optional[Dict[str, str]] = None

class UnassignInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class UnassignVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateElasticIpRequestRequestTypeDef(BaseModel):
    ElasticIp: str
    Name: Optional[str] = None

class UpdateInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LayerIds: Optional[Sequence[str]] = None
    InstanceType: Optional[str] = None
    AutoScalingType: Optional[AutoScalingTypeType] = None
    Hostname: Optional[str] = None
    Os: Optional[str] = None
    AmiId: Optional[str] = None
    SshKeyName: Optional[str] = None
    Architecture: Optional[ArchitectureType] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    AgentVersion: Optional[str] = None

class UpdateMyUserProfileRequestRequestTypeDef(BaseModel):
    SshPublicKey: Optional[str] = None

class UpdateRdsDbInstanceRequestRequestTypeDef(BaseModel):
    RdsDbInstanceArn: str
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None

class UpdateUserProfileRequestRequestTypeDef(BaseModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None

class UpdateVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    Name: Optional[str] = None
    MountPoint: Optional[str] = None

class AgentVersionTypeDef(BaseModel):
    Version: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None

class DescribeAgentVersionsRequestRequestTypeDef(BaseModel):
    StackId: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None

class AppTypeDef(BaseModel):
    AppId: Optional[str] = None
    StackId: Optional[str] = None
    Shortname: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DataSources: Optional[List[DataSourceTypeDef]] = None
    Type: Optional[AppTypeType] = None
    AppSource: Optional[SourceTypeDef] = None
    Domains: Optional[List[str]] = None
    EnableSsl: Optional[bool] = None
    SslConfiguration: Optional[SslConfigurationTypeDef] = None
    Attributes: Optional[Dict[AppAttributesKeysType, str]] = None
    CreatedAt: Optional[str] = None
    Environment: Optional[List[EnvironmentVariableTypeDef]] = None

class CreateAppRequestRequestTypeDef(BaseModel):
    StackId: str
    Name: str
    Type: AppTypeType
    Shortname: Optional[str] = None
    Description: Optional[str] = None
    DataSources: Optional[Sequence[DataSourceTypeDef]] = None
    AppSource: Optional[SourceTypeDef] = None
    Domains: Optional[Sequence[str]] = None
    EnableSsl: Optional[bool] = None
    SslConfiguration: Optional[SslConfigurationTypeDef] = None
    Attributes: Optional[Mapping[AppAttributesKeysType, str]] = None
    Environment: Optional[Sequence[EnvironmentVariableTypeDef]] = None

class UpdateAppRequestRequestTypeDef(BaseModel):
    AppId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    DataSources: Optional[Sequence[DataSourceTypeDef]] = None
    Type: Optional[AppTypeType] = None
    AppSource: Optional[SourceTypeDef] = None
    Domains: Optional[Sequence[str]] = None
    EnableSsl: Optional[bool] = None
    SslConfiguration: Optional[SslConfigurationTypeDef] = None
    Attributes: Optional[Mapping[AppAttributesKeysType, str]] = None
    Environment: Optional[Sequence[EnvironmentVariableTypeDef]] = None

class LoadBasedAutoScalingConfigurationTypeDef(BaseModel):
    LayerId: Optional[str] = None
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsOutputTypeDef] = None
    DownScaling: Optional[AutoScalingThresholdsOutputTypeDef] = None

class SetLoadBasedAutoScalingRequestRequestTypeDef(BaseModel):
    LayerId: str
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsTypeDef] = None
    DownScaling: Optional[AutoScalingThresholdsTypeDef] = None

class BlockDeviceMappingTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDeviceTypeDef] = None

class ChefConfigurationResponseTypeDef(BaseModel):
    ManageBerkshelf: bool
    BerkshelfVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloneStackResultTypeDef(BaseModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppResultTypeDef(BaseModel):
    AppId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResultTypeDef(BaseModel):
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceResultTypeDef(BaseModel):
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayerResultTypeDef(BaseModel):
    LayerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackResultTypeDef(BaseModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserProfileResultTypeDef(BaseModel):
    IamUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackProvisioningParametersResultTypeDef(BaseModel):
    AgentInstallerUrl: str
    Parameters: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostnameSuggestionResultTypeDef(BaseModel):
    LayerId: str
    Hostname: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstancesCountResponseTypeDef(BaseModel):
    Assigning: int
    Booting: int
    ConnectionLost: int
    Deregistering: int
    Online: int
    Pending: int
    Rebooting: int
    Registered: int
    Registering: int
    Requested: int
    RunningSetup: int
    SetupFailed: int
    ShuttingDown: int
    StartFailed: int
    StopFailed: int
    Stopped: int
    Stopping: int
    Terminated: int
    Terminating: int
    Unassigning: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResultTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RecipesResponseTypeDef(BaseModel):
    Setup: List[str]
    Configure: List[str]
    Deploy: List[str]
    Undeploy: List[str]
    Shutdown: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterEcsClusterResultTypeDef(BaseModel):
    EcsClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterElasticIpResultTypeDef(BaseModel):
    ElasticIp: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceResultTypeDef(BaseModel):
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterVolumeResultTypeDef(BaseModel):
    VolumeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourceResponseTypeDef(BaseModel):
    Type: SourceTypeType
    Url: str
    Username: str
    Password: str
    SshKey: str
    Revision: str
    ResponseMetadata: ResponseMetadataTypeDef

class StackConfigurationManagerResponseTypeDef(BaseModel):
    Name: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloneStackRequestRequestTypeDef(BaseModel):
    SourceStackId: str
    ServiceRoleArn: str
    Name: Optional[str] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None
    Attributes: Optional[Mapping[Literal["Color"], str]] = None
    DefaultInstanceProfileArn: Optional[str] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None
    ChefConfiguration: Optional[ChefConfigurationTypeDef] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[SourceTypeDef] = None
    DefaultSshKeyName: Optional[str] = None
    ClonePermissions: Optional[bool] = None
    CloneAppIds: Optional[Sequence[str]] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None

class CreateStackRequestRequestTypeDef(BaseModel):
    Name: str
    Region: str
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    VpcId: Optional[str] = None
    Attributes: Optional[Mapping[Literal["Color"], str]] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None
    ChefConfiguration: Optional[ChefConfigurationTypeDef] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[SourceTypeDef] = None
    DefaultSshKeyName: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None

class CreateStackRequestServiceResourceCreateStackTypeDef(BaseModel):
    Name: str
    Region: str
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    VpcId: Optional[str] = None
    Attributes: Optional[Mapping[Literal["Color"], str]] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None
    ChefConfiguration: Optional[ChefConfigurationTypeDef] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[SourceTypeDef] = None
    DefaultSshKeyName: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None

class StackTypeDef(BaseModel):
    StackId: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None
    Attributes: Optional[Dict[Literal["Color"], str]] = None
    ServiceRoleArn: Optional[str] = None
    DefaultInstanceProfileArn: Optional[str] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None
    ChefConfiguration: Optional[ChefConfigurationTypeDef] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[SourceTypeDef] = None
    DefaultSshKeyName: Optional[str] = None
    CreatedAt: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None

class UpdateStackRequestRequestTypeDef(BaseModel):
    StackId: str
    Name: Optional[str] = None
    Attributes: Optional[Mapping[Literal["Color"], str]] = None
    ServiceRoleArn: Optional[str] = None
    DefaultInstanceProfileArn: Optional[str] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None
    ChefConfiguration: Optional[ChefConfigurationTypeDef] = None
    UseCustomCookbooks: Optional[bool] = None
    CustomCookbooksSource: Optional[SourceTypeDef] = None
    DefaultSshKeyName: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    AgentVersion: Optional[str] = None

class CloudWatchLogsConfigurationOutputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[List[CloudWatchLogsLogStreamTypeDef]] = None

class CloudWatchLogsConfigurationResponseTypeDef(BaseModel):
    Enabled: bool
    LogStreams: List[CloudWatchLogsLogStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CloudWatchLogsConfigurationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[Sequence[CloudWatchLogsLogStreamTypeDef]] = None

class DescribeCommandsResultTypeDef(BaseModel):
    Commands: List[CommandTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    StackId: str
    Command: DeploymentCommandTypeDef
    AppId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    LayerIds: Optional[Sequence[str]] = None
    Comment: Optional[str] = None
    CustomJson: Optional[str] = None

class DeploymentTypeDef(BaseModel):
    DeploymentId: Optional[str] = None
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    CreatedAt: Optional[str] = None
    CompletedAt: Optional[str] = None
    Duration: Optional[int] = None
    IamUserArn: Optional[str] = None
    Comment: Optional[str] = None
    Command: Optional[DeploymentCommandOutputTypeDef] = None
    Status: Optional[str] = None
    CustomJson: Optional[str] = None
    InstanceIds: Optional[List[str]] = None

class DescribeAppsRequestAppExistsWaitTypeDef(BaseModel):
    StackId: Optional[str] = None
    AppIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef(BaseModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceOnlineWaitTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceRegisteredWaitTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceStoppedWaitTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceTerminatedWaitTypeDef(BaseModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef(BaseModel):
    EcsClusterArns: Optional[Sequence[str]] = None
    StackId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEcsClustersResultTypeDef(BaseModel):
    EcsClusters: List[EcsClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeElasticIpsResultTypeDef(BaseModel):
    ElasticIps: List[ElasticIpTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticLoadBalancersResultTypeDef(BaseModel):
    ElasticLoadBalancers: List[ElasticLoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMyUserProfileResultTypeDef(BaseModel):
    UserProfile: SelfUserProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePermissionsResultTypeDef(BaseModel):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRaidArraysResultTypeDef(BaseModel):
    RaidArrays: List[RaidArrayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRdsDbInstancesResultTypeDef(BaseModel):
    RdsDbInstances: List[RdsDbInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceErrorsResultTypeDef(BaseModel):
    ServiceErrors: List[ServiceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserProfilesResultTypeDef(BaseModel):
    UserProfiles: List[UserProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVolumesResultTypeDef(BaseModel):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GrantAccessResultTypeDef(BaseModel):
    TemporaryCredential: TemporaryCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceRequestRequestTypeDef(BaseModel):
    StackId: str
    Hostname: Optional[str] = None
    PublicIp: Optional[str] = None
    PrivateIp: Optional[str] = None
    RsaPublicKey: Optional[str] = None
    RsaPublicKeyFingerprint: Optional[str] = None
    InstanceIdentity: Optional[InstanceIdentityTypeDef] = None

class StackSummaryTypeDef(BaseModel):
    StackId: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    LayersCount: Optional[int] = None
    AppsCount: Optional[int] = None
    InstancesCount: Optional[InstancesCountTypeDef] = None

class LifecycleEventConfigurationResponseTypeDef(BaseModel):
    Shutdown: ShutdownEventConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleEventConfigurationTypeDef(BaseModel):
    Shutdown: Optional[ShutdownEventConfigurationTypeDef] = None

class OperatingSystemTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[str] = None
    ConfigurationManagers: Optional[List[OperatingSystemConfigurationManagerTypeDef]] = None
    ReportedName: Optional[str] = None
    ReportedVersion: Optional[str] = None
    Supported: Optional[bool] = None

class SetTimeBasedAutoScalingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleTypeDef] = None

class TimeBasedAutoScalingConfigurationTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleOutputTypeDef] = None

class DescribeAgentVersionsResultTypeDef(BaseModel):
    AgentVersions: List[AgentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppsResultTypeDef(BaseModel):
    Apps: List[AppTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBasedAutoScalingResultTypeDef(BaseModel):
    LoadBasedAutoScalingConfigurations: List[LoadBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceRequestRequestTypeDef(BaseModel):
    StackId: str
    LayerIds: Sequence[str]
    InstanceType: str
    AutoScalingType: Optional[AutoScalingTypeType] = None
    Hostname: Optional[str] = None
    Os: Optional[str] = None
    AmiId: Optional[str] = None
    SshKeyName: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    VirtualizationType: Optional[str] = None
    SubnetId: Optional[str] = None
    Architecture: Optional[ArchitectureType] = None
    RootDeviceType: Optional[RootDeviceTypeType] = None
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    AgentVersion: Optional[str] = None
    Tenancy: Optional[str] = None

class InstanceTypeDef(BaseModel):
    AgentVersion: Optional[str] = None
    AmiId: Optional[str] = None
    Architecture: Optional[ArchitectureType] = None
    Arn: Optional[str] = None
    AutoScalingType: Optional[AutoScalingTypeType] = None
    AvailabilityZone: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingTypeDef]] = None
    CreatedAt: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    Ec2InstanceId: Optional[str] = None
    EcsClusterArn: Optional[str] = None
    EcsContainerInstanceArn: Optional[str] = None
    ElasticIp: Optional[str] = None
    Hostname: Optional[str] = None
    InfrastructureClass: Optional[str] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    InstanceId: Optional[str] = None
    InstanceProfileArn: Optional[str] = None
    InstanceType: Optional[str] = None
    LastServiceErrorId: Optional[str] = None
    LayerIds: Optional[List[str]] = None
    Os: Optional[str] = None
    Platform: Optional[str] = None
    PrivateDns: Optional[str] = None
    PrivateIp: Optional[str] = None
    PublicDns: Optional[str] = None
    PublicIp: Optional[str] = None
    RegisteredBy: Optional[str] = None
    ReportedAgentVersion: Optional[str] = None
    ReportedOs: Optional[ReportedOsTypeDef] = None
    RootDeviceType: Optional[RootDeviceTypeType] = None
    RootDeviceVolumeId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SshHostDsaKeyFingerprint: Optional[str] = None
    SshHostRsaKeyFingerprint: Optional[str] = None
    SshKeyName: Optional[str] = None
    StackId: Optional[str] = None
    Status: Optional[str] = None
    SubnetId: Optional[str] = None
    Tenancy: Optional[str] = None
    VirtualizationType: Optional[VirtualizationTypeType] = None

class DescribeStacksResultTypeDef(BaseModel):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeploymentsResultTypeDef(BaseModel):
    Deployments: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackSummaryResultTypeDef(BaseModel):
    StackSummary: StackSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayerRequestRequestTypeDef(BaseModel):
    StackId: str
    Type: LayerTypeType
    Name: str
    Shortname: str
    Attributes: Optional[Mapping[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationTypeDef] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[Sequence[str]] = None
    Packages: Optional[Sequence[str]] = None
    VolumeConfigurations: Optional[Sequence[VolumeConfigurationTypeDef]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesTypeDef] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfigurationTypeDef] = None

class CreateLayerRequestStackCreateLayerTypeDef(BaseModel):
    Type: LayerTypeType
    Name: str
    Shortname: str
    Attributes: Optional[Mapping[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationTypeDef] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[Sequence[str]] = None
    Packages: Optional[Sequence[str]] = None
    VolumeConfigurations: Optional[Sequence[VolumeConfigurationTypeDef]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesTypeDef] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfigurationTypeDef] = None

class LayerTypeDef(BaseModel):
    Arn: Optional[str] = None
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    Type: Optional[LayerTypeType] = None
    Name: Optional[str] = None
    Shortname: Optional[str] = None
    Attributes: Optional[Dict[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationOutputTypeDef] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[List[str]] = None
    DefaultSecurityGroupNames: Optional[List[str]] = None
    Packages: Optional[List[str]] = None
    VolumeConfigurations: Optional[List[VolumeConfigurationTypeDef]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    DefaultRecipes: Optional[RecipesOutputTypeDef] = None
    CustomRecipes: Optional[RecipesOutputTypeDef] = None
    CreatedAt: Optional[str] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfigurationTypeDef] = None

class UpdateLayerRequestRequestTypeDef(BaseModel):
    LayerId: str
    Name: Optional[str] = None
    Shortname: Optional[str] = None
    Attributes: Optional[Mapping[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationTypeDef] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[Sequence[str]] = None
    Packages: Optional[Sequence[str]] = None
    VolumeConfigurations: Optional[Sequence[VolumeConfigurationTypeDef]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesTypeDef] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfigurationTypeDef] = None

class DescribeOperatingSystemsResponseTypeDef(BaseModel):
    OperatingSystems: List[OperatingSystemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTimeBasedAutoScalingResultTypeDef(BaseModel):
    TimeBasedAutoScalingConfigurations: List[TimeBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstancesResultTypeDef(BaseModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLayersResultTypeDef(BaseModel):
    Layers: List[LayerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

