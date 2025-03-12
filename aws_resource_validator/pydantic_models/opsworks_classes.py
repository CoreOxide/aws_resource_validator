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
from aws_resource_validator.pydantic_models.opsworks_constants import *

class StackConfigurationManagerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class EnvironmentVariableTypeDef(BaseValidatorModel):
    Key: str
    Value: str
    Secure: Optional[bool] = None


class SslConfigurationTypeDef(BaseValidatorModel):
    Certificate: str
    PrivateKey: str
    Chain: Optional[str] = None


class AssignInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LayerIds: Sequence[str]


class AssignVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    InstanceId: Optional[str] = None


class AssociateElasticIpRequestTypeDef(BaseValidatorModel):
    ElasticIp: str
    InstanceId: Optional[str] = None


class AttachElasticLoadBalancerRequestTypeDef(BaseValidatorModel):
    ElasticLoadBalancerName: str
    LayerId: str


class AutoScalingThresholdsOutputTypeDef(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    ThresholdsWaitTime: Optional[int] = None
    IgnoreMetricsTime: Optional[int] = None
    CpuThreshold: Optional[float] = None
    MemoryThreshold: Optional[float] = None
    LoadThreshold: Optional[float] = None
    Alarms: Optional[List[str]] = None


class AutoScalingThresholdsTypeDef(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    ThresholdsWaitTime: Optional[int] = None
    IgnoreMetricsTime: Optional[int] = None
    CpuThreshold: Optional[float] = None
    MemoryThreshold: Optional[float] = None
    LoadThreshold: Optional[float] = None
    Alarms: Optional[Sequence[str]] = None


class EbsBlockDeviceTypeDef(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    Iops: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    DeleteOnTermination: Optional[bool] = None


class ChefConfigurationTypeDef(BaseValidatorModel):
    ManageBerkshelf: Optional[bool] = None
    BerkshelfVersion: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CloudWatchLogsLogStreamTypeDef(BaseValidatorModel):
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


class VolumeConfigurationTypeDef(BaseValidatorModel):
    MountPoint: str
    NumberOfDisks: int
    Size: int
    RaidLevel: Optional[int] = None
    VolumeType: Optional[str] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None


class CreateUserProfileRequestTypeDef(BaseValidatorModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None


class DeleteAppRequestTypeDef(BaseValidatorModel):
    AppId: str


class DeleteInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DeleteElasticIp: Optional[bool] = None
    DeleteVolumes: Optional[bool] = None


class DeleteLayerRequestTypeDef(BaseValidatorModel):
    LayerId: str


class DeleteStackRequestTypeDef(BaseValidatorModel):
    StackId: str


class DeleteUserProfileRequestTypeDef(BaseValidatorModel):
    IamUserArn: str


class DeploymentCommandOutputTypeDef(BaseValidatorModel):
    Name: DeploymentCommandNameType
    Args: Optional[Dict[str, List[str]]] = None


class DeploymentCommandTypeDef(BaseValidatorModel):
    Name: DeploymentCommandNameType
    Args: Optional[Mapping[str, Sequence[str]]] = None


class DeregisterEcsClusterRequestTypeDef(BaseValidatorModel):
    EcsClusterArn: str


class DeregisterElasticIpRequestTypeDef(BaseValidatorModel):
    ElasticIp: str


class DeregisterInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class DeregisterRdsDbInstanceRequestTypeDef(BaseValidatorModel):
    RdsDbInstanceArn: str


class DeregisterVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str


class DescribeAppsRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppIds: Optional[Sequence[str]] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeCommandsRequestTypeDef(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    InstanceId: Optional[str] = None
    CommandIds: Optional[Sequence[str]] = None


class DescribeDeploymentsRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEcsClustersRequestTypeDef(BaseValidatorModel):
    EcsClusterArns: Optional[Sequence[str]] = None
    StackId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class EcsClusterTypeDef(BaseValidatorModel):
    EcsClusterArn: Optional[str] = None
    EcsClusterName: Optional[str] = None
    StackId: Optional[str] = None
    RegisteredAt: Optional[str] = None


class DescribeElasticIpsRequestTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    Ips: Optional[Sequence[str]] = None


class ElasticIpTypeDef(BaseValidatorModel):
    Ip: Optional[str] = None
    Name: Optional[str] = None
    Domain: Optional[str] = None
    Region: Optional[str] = None
    InstanceId: Optional[str] = None


class DescribeElasticLoadBalancersRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerIds: Optional[Sequence[str]] = None


class ElasticLoadBalancerTypeDef(BaseValidatorModel):
    ElasticLoadBalancerName: Optional[str] = None
    Region: Optional[str] = None
    DnsName: Optional[str] = None
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    Ec2InstanceIds: Optional[List[str]] = None


class DescribeInstancesRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None


class DescribeLayersRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerIds: Optional[Sequence[str]] = None


class DescribeLoadBasedAutoScalingRequestTypeDef(BaseValidatorModel):
    LayerIds: Sequence[str]


class SelfUserProfileTypeDef(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None


class DescribePermissionsRequestTypeDef(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    StackId: Optional[str] = None


class PermissionTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    IamUserArn: Optional[str] = None
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None


class DescribeRaidArraysRequestTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    RaidArrayIds: Optional[Sequence[str]] = None


class RaidArrayTypeDef(BaseValidatorModel):
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


class DescribeRdsDbInstancesRequestTypeDef(BaseValidatorModel):
    StackId: str
    RdsDbInstanceArns: Optional[Sequence[str]] = None


class RdsDbInstanceTypeDef(BaseValidatorModel):
    RdsDbInstanceArn: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None
    Region: Optional[str] = None
    Address: Optional[str] = None
    Engine: Optional[str] = None
    StackId: Optional[str] = None
    MissingOnRds: Optional[bool] = None


class DescribeServiceErrorsRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    ServiceErrorIds: Optional[Sequence[str]] = None


class DescribeStackProvisioningParametersRequestTypeDef(BaseValidatorModel):
    StackId: str


class DescribeStackSummaryRequestTypeDef(BaseValidatorModel):
    StackId: str


class DescribeStacksRequestTypeDef(BaseValidatorModel):
    StackIds: Optional[Sequence[str]] = None


class DescribeTimeBasedAutoScalingRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]


class DescribeUserProfilesRequestTypeDef(BaseValidatorModel):
    IamUserArns: Optional[Sequence[str]] = None


class UserProfileTypeDef(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None


class DescribeVolumesRequestTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    RaidArrayId: Optional[str] = None
    VolumeIds: Optional[Sequence[str]] = None


class VolumeTypeDef(BaseValidatorModel):
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


class DetachElasticLoadBalancerRequestTypeDef(BaseValidatorModel):
    ElasticLoadBalancerName: str
    LayerId: str


class DisassociateElasticIpRequestTypeDef(BaseValidatorModel):
    ElasticIp: str


class GetHostnameSuggestionRequestTypeDef(BaseValidatorModel):
    LayerId: str


class GrantAccessRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ValidForInMinutes: Optional[int] = None


class TemporaryCredentialTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None
    ValidForInMinutes: Optional[int] = None
    InstanceId: Optional[str] = None


class InstanceIdentityTypeDef(BaseValidatorModel):
    Document: Optional[str] = None
    Signature: Optional[str] = None


class ReportedOsTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None


class InstancesCountTypeDef(BaseValidatorModel):
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


class RecipesOutputTypeDef(BaseValidatorModel):
    Setup: Optional[List[str]] = None
    Configure: Optional[List[str]] = None
    Deploy: Optional[List[str]] = None
    Undeploy: Optional[List[str]] = None
    Shutdown: Optional[List[str]] = None


class ShutdownEventConfigurationTypeDef(BaseValidatorModel):
    ExecutionTimeout: Optional[int] = None
    DelayUntilElbConnectionsDrained: Optional[bool] = None


class ListTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OperatingSystemConfigurationManagerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class RebootInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class RecipesTypeDef(BaseValidatorModel):
    Setup: Optional[Sequence[str]] = None
    Configure: Optional[Sequence[str]] = None
    Deploy: Optional[Sequence[str]] = None
    Undeploy: Optional[Sequence[str]] = None
    Shutdown: Optional[Sequence[str]] = None


class RegisterEcsClusterRequestTypeDef(BaseValidatorModel):
    EcsClusterArn: str
    StackId: str


class RegisterElasticIpRequestTypeDef(BaseValidatorModel):
    ElasticIp: str
    StackId: str


class RegisterRdsDbInstanceRequestTypeDef(BaseValidatorModel):
    StackId: str
    RdsDbInstanceArn: str
    DbUser: str
    DbPassword: str


class RegisterVolumeRequestTypeDef(BaseValidatorModel):
    StackId: str
    Ec2VolumeId: Optional[str] = None


class SetPermissionRequestTypeDef(BaseValidatorModel):
    StackId: str
    IamUserArn: str
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None


class StartInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class StartStackRequestTypeDef(BaseValidatorModel):
    StackId: str


class StopInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Force: Optional[bool] = None


class StopStackRequestTypeDef(BaseValidatorModel):
    StackId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class WeeklyAutoScalingScheduleOutputTypeDef(BaseValidatorModel):
    Monday: Optional[Dict[str, str]] = None
    Tuesday: Optional[Dict[str, str]] = None
    Wednesday: Optional[Dict[str, str]] = None
    Thursday: Optional[Dict[str, str]] = None
    Friday: Optional[Dict[str, str]] = None
    Saturday: Optional[Dict[str, str]] = None
    Sunday: Optional[Dict[str, str]] = None


class UnassignInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class UnassignVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateElasticIpRequestTypeDef(BaseValidatorModel):
    ElasticIp: str
    Name: Optional[str] = None


class UpdateInstanceRequestTypeDef(BaseValidatorModel):
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


class UpdateMyUserProfileRequestTypeDef(BaseValidatorModel):
    SshPublicKey: Optional[str] = None


class UpdateRdsDbInstanceRequestTypeDef(BaseValidatorModel):
    RdsDbInstanceArn: str
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None


class UpdateUserProfileRequestTypeDef(BaseValidatorModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None


class UpdateVolumeRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    Name: Optional[str] = None
    MountPoint: Optional[str] = None


class WeeklyAutoScalingScheduleTypeDef(BaseValidatorModel):
    Monday: Optional[Mapping[str, str]] = None
    Tuesday: Optional[Mapping[str, str]] = None
    Wednesday: Optional[Mapping[str, str]] = None
    Thursday: Optional[Mapping[str, str]] = None
    Friday: Optional[Mapping[str, str]] = None
    Saturday: Optional[Mapping[str, str]] = None
    Sunday: Optional[Mapping[str, str]] = None


class AgentVersionTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None


class DescribeAgentVersionsRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None


class LoadBasedAutoScalingConfigurationTypeDef(BaseValidatorModel):
    LayerId: Optional[str] = None
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsOutputTypeDef] = None
    DownScaling: Optional[AutoScalingThresholdsOutputTypeDef] = None


class BlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDeviceTypeDef] = None


class SourceTypeDef(BaseValidatorModel):
    pass


class CloneStackRequestTypeDef(BaseValidatorModel):
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


class CreateStackRequestServiceResourceCreateStackTypeDef(BaseValidatorModel):
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


class CreateStackRequestTypeDef(BaseValidatorModel):
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


class StackTypeDef(BaseValidatorModel):
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


class UpdateStackRequestTypeDef(BaseValidatorModel):
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


class CloneStackResultTypeDef(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAppResultTypeDef(BaseValidatorModel):
    AppId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDeploymentResultTypeDef(BaseValidatorModel):
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstanceResultTypeDef(BaseValidatorModel):
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLayerResultTypeDef(BaseValidatorModel):
    LayerId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStackResultTypeDef(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserProfileResultTypeDef(BaseValidatorModel):
    IamUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeStackProvisioningParametersResultTypeDef(BaseValidatorModel):
    AgentInstallerUrl: str
    Parameters: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetHostnameSuggestionResultTypeDef(BaseValidatorModel):
    LayerId: str
    Hostname: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsResultTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RegisterEcsClusterResultTypeDef(BaseValidatorModel):
    EcsClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterElasticIpResultTypeDef(BaseValidatorModel):
    ElasticIp: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterInstanceResultTypeDef(BaseValidatorModel):
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterVolumeResultTypeDef(BaseValidatorModel):
    VolumeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CloudWatchLogsConfigurationOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[List[CloudWatchLogsLogStreamTypeDef]] = None


class CloudWatchLogsConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[Sequence[CloudWatchLogsLogStreamTypeDef]] = None


class CommandTypeDef(BaseValidatorModel):
    pass


class DescribeCommandsResultTypeDef(BaseValidatorModel):
    Commands: List[CommandTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentTypeDef(BaseValidatorModel):
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


class DescribeAppsRequestWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeDeploymentsRequestWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeInstancesRequestWaitExtraExtraExtraTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeInstancesRequestWaitExtraExtraTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeInstancesRequestWaitExtraTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeInstancesRequestWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeEcsClustersRequestPaginateTypeDef(BaseValidatorModel):
    EcsClusterArns: Optional[Sequence[str]] = None
    StackId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEcsClustersResultTypeDef(BaseValidatorModel):
    EcsClusters: List[EcsClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeElasticIpsResultTypeDef(BaseValidatorModel):
    ElasticIps: List[ElasticIpTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeElasticLoadBalancersResultTypeDef(BaseValidatorModel):
    ElasticLoadBalancers: List[ElasticLoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMyUserProfileResultTypeDef(BaseValidatorModel):
    UserProfile: SelfUserProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePermissionsResultTypeDef(BaseValidatorModel):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRaidArraysResultTypeDef(BaseValidatorModel):
    RaidArrays: List[RaidArrayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRdsDbInstancesResultTypeDef(BaseValidatorModel):
    RdsDbInstances: List[RdsDbInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceErrorTypeDef(BaseValidatorModel):
    pass


class DescribeServiceErrorsResultTypeDef(BaseValidatorModel):
    ServiceErrors: List[ServiceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserProfilesResultTypeDef(BaseValidatorModel):
    UserProfiles: List[UserProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVolumesResultTypeDef(BaseValidatorModel):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GrantAccessResultTypeDef(BaseValidatorModel):
    TemporaryCredential: TemporaryCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterInstanceRequestTypeDef(BaseValidatorModel):
    StackId: str
    Hostname: Optional[str] = None
    PublicIp: Optional[str] = None
    PrivateIp: Optional[str] = None
    RsaPublicKey: Optional[str] = None
    RsaPublicKeyFingerprint: Optional[str] = None
    InstanceIdentity: Optional[InstanceIdentityTypeDef] = None


class StackSummaryTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    LayersCount: Optional[int] = None
    AppsCount: Optional[int] = None
    InstancesCount: Optional[InstancesCountTypeDef] = None


class LifecycleEventConfigurationTypeDef(BaseValidatorModel):
    Shutdown: Optional[ShutdownEventConfigurationTypeDef] = None


class TimeBasedAutoScalingConfigurationTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleOutputTypeDef] = None


class DescribeAgentVersionsResultTypeDef(BaseValidatorModel):
    AgentVersions: List[AgentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AppTypeDef(BaseValidatorModel):
    pass


class DescribeAppsResultTypeDef(BaseValidatorModel):
    Apps: List[AppTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBasedAutoScalingResultTypeDef(BaseValidatorModel):
    LoadBasedAutoScalingConfigurations: List[LoadBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AutoScalingThresholdsUnionTypeDef(BaseValidatorModel):
    pass


class SetLoadBasedAutoScalingRequestTypeDef(BaseValidatorModel):
    LayerId: str
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsUnionTypeDef] = None
    DownScaling: Optional[AutoScalingThresholdsUnionTypeDef] = None


class CreateInstanceRequestTypeDef(BaseValidatorModel):
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


class InstanceTypeDef(BaseValidatorModel):
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


class DescribeStacksResultTypeDef(BaseValidatorModel):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDeploymentsResultTypeDef(BaseValidatorModel):
    Deployments: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentCommandUnionTypeDef(BaseValidatorModel):
    pass


class CreateDeploymentRequestTypeDef(BaseValidatorModel):
    StackId: str
    Command: DeploymentCommandUnionTypeDef
    AppId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    LayerIds: Optional[Sequence[str]] = None
    Comment: Optional[str] = None
    CustomJson: Optional[str] = None


class DescribeStackSummaryResultTypeDef(BaseValidatorModel):
    StackSummary: StackSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OperatingSystemTypeDef(BaseValidatorModel):
    pass


class DescribeOperatingSystemsResponseTypeDef(BaseValidatorModel):
    OperatingSystems: List[OperatingSystemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTimeBasedAutoScalingResultTypeDef(BaseValidatorModel):
    TimeBasedAutoScalingConfigurations: List[TimeBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class WeeklyAutoScalingScheduleUnionTypeDef(BaseValidatorModel):
    pass


class SetTimeBasedAutoScalingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleUnionTypeDef] = None


class DescribeInstancesResultTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RecipesUnionTypeDef(BaseValidatorModel):
    pass


class CloudWatchLogsConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateLayerRequestTypeDef(BaseValidatorModel):
    LayerId: str
    Name: Optional[str] = None
    Shortname: Optional[str] = None
    Attributes: Optional[Mapping[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationUnionTypeDef] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[Sequence[str]] = None
    Packages: Optional[Sequence[str]] = None
    VolumeConfigurations: Optional[Sequence[VolumeConfigurationTypeDef]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesUnionTypeDef] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfigurationTypeDef] = None


class LayerTypeDef(BaseValidatorModel):
    pass


class DescribeLayersResultTypeDef(BaseValidatorModel):
    Layers: List[LayerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


