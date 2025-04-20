from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.opsworks.opsworks_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class StackConfigurationManager(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class DataSource(BaseValidatorModel):
    Type: Optional[str] = None
    Arn: Optional[str] = None
    DatabaseName: Optional[str] = None


class EnvironmentVariable(BaseValidatorModel):
    Key: str
    Value: str
    Secure: Optional[bool] = None


class Source(BaseValidatorModel):
    Type: Optional[SourceTypeType] = None
    Url: Optional[str] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    SshKey: Optional[str] = None
    Revision: Optional[str] = None


class SslConfiguration(BaseValidatorModel):
    Certificate: str
    PrivateKey: str
    Chain: Optional[str] = None


class AssignInstanceRequest(BaseValidatorModel):
    InstanceId: str
    LayerIds: List[str]


class AssignVolumeRequest(BaseValidatorModel):
    VolumeId: str
    InstanceId: Optional[str] = None


class AssociateElasticIpRequest(BaseValidatorModel):
    ElasticIp: str
    InstanceId: Optional[str] = None


class AttachElasticLoadBalancerRequest(BaseValidatorModel):
    ElasticLoadBalancerName: str
    LayerId: str


class AutoScalingThresholdsOutput(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    ThresholdsWaitTime: Optional[int] = None
    IgnoreMetricsTime: Optional[int] = None
    CpuThreshold: Optional[float] = None
    MemoryThreshold: Optional[float] = None
    LoadThreshold: Optional[float] = None
    Alarms: Optional[List[str]] = None


class AutoScalingThresholds(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    ThresholdsWaitTime: Optional[int] = None
    IgnoreMetricsTime: Optional[int] = None
    CpuThreshold: Optional[float] = None
    MemoryThreshold: Optional[float] = None
    LoadThreshold: Optional[float] = None
    Alarms: Optional[List[str]] = None


class EbsBlockDevice(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    Iops: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    DeleteOnTermination: Optional[bool] = None


class ChefConfiguration(BaseValidatorModel):
    ManageBerkshelf: Optional[bool] = None
    BerkshelfVersion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CloudWatchLogsLogStream(BaseValidatorModel):
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


class Command(BaseValidatorModel):
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


class VolumeConfiguration(BaseValidatorModel):
    MountPoint: str
    NumberOfDisks: int
    Size: int
    RaidLevel: Optional[int] = None
    VolumeType: Optional[str] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None


class CreateUserProfileRequest(BaseValidatorModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None


class DeleteAppRequest(BaseValidatorModel):
    AppId: str


class DeleteInstanceRequest(BaseValidatorModel):
    InstanceId: str
    DeleteElasticIp: Optional[bool] = None
    DeleteVolumes: Optional[bool] = None


class DeleteLayerRequest(BaseValidatorModel):
    LayerId: str


class DeleteStackRequest(BaseValidatorModel):
    StackId: str


class DeleteUserProfileRequest(BaseValidatorModel):
    IamUserArn: str


class DeploymentCommandOutput(BaseValidatorModel):
    Name: DeploymentCommandNameType
    Args: Optional[Dict[str, List[str]]] = None


class DeploymentCommand(BaseValidatorModel):
    Name: DeploymentCommandNameType
    Args: Optional[Dict[str, List[str]]] = None


class DeregisterEcsClusterRequest(BaseValidatorModel):
    EcsClusterArn: str


class DeregisterElasticIpRequest(BaseValidatorModel):
    ElasticIp: str


class DeregisterInstanceRequest(BaseValidatorModel):
    InstanceId: str


class DeregisterRdsDbInstanceRequest(BaseValidatorModel):
    RdsDbInstanceArn: str


class DeregisterVolumeRequest(BaseValidatorModel):
    VolumeId: str


class DescribeAppsRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    AppIds: Optional[List[str]] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeCommandsRequest(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    InstanceId: Optional[str] = None
    CommandIds: Optional[List[str]] = None


class DescribeDeploymentsRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEcsClustersRequest(BaseValidatorModel):
    EcsClusterArns: Optional[List[str]] = None
    StackId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class EcsCluster(BaseValidatorModel):
    EcsClusterArn: Optional[str] = None
    EcsClusterName: Optional[str] = None
    StackId: Optional[str] = None
    RegisteredAt: Optional[str] = None


class DescribeElasticIpsRequest(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    Ips: Optional[List[str]] = None


class ElasticIp(BaseValidatorModel):
    Ip: Optional[str] = None
    Name: Optional[str] = None
    Domain: Optional[str] = None
    Region: Optional[str] = None
    InstanceId: Optional[str] = None


class DescribeElasticLoadBalancersRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerIds: Optional[List[str]] = None


class ElasticLoadBalancer(BaseValidatorModel):
    ElasticLoadBalancerName: Optional[str] = None
    Region: Optional[str] = None
    DnsName: Optional[str] = None
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    Ec2InstanceIds: Optional[List[str]] = None


class DescribeInstancesRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[List[str]] = None


class DescribeLayersRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerIds: Optional[List[str]] = None


class DescribeLoadBasedAutoScalingRequest(BaseValidatorModel):
    LayerIds: List[str]


class SelfUserProfile(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None


class DescribePermissionsRequest(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    StackId: Optional[str] = None


class Permission(BaseValidatorModel):
    StackId: Optional[str] = None
    IamUserArn: Optional[str] = None
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None


class DescribeRaidArraysRequest(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    RaidArrayIds: Optional[List[str]] = None


class RaidArray(BaseValidatorModel):
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


class DescribeRdsDbInstancesRequest(BaseValidatorModel):
    StackId: str
    RdsDbInstanceArns: Optional[List[str]] = None


class RdsDbInstance(BaseValidatorModel):
    RdsDbInstanceArn: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None
    Region: Optional[str] = None
    Address: Optional[str] = None
    Engine: Optional[str] = None
    StackId: Optional[str] = None
    MissingOnRds: Optional[bool] = None


class DescribeServiceErrorsRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    ServiceErrorIds: Optional[List[str]] = None


class ServiceError(BaseValidatorModel):
    ServiceErrorId: Optional[str] = None
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None
    CreatedAt: Optional[str] = None


class DescribeStackProvisioningParametersRequest(BaseValidatorModel):
    StackId: str


class DescribeStackSummaryRequest(BaseValidatorModel):
    StackId: str


class DescribeStacksRequest(BaseValidatorModel):
    StackIds: Optional[List[str]] = None


class DescribeTimeBasedAutoScalingRequest(BaseValidatorModel):
    InstanceIds: List[str]


class DescribeUserProfilesRequest(BaseValidatorModel):
    IamUserArns: Optional[List[str]] = None


class UserProfile(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None


class DescribeVolumesRequest(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    RaidArrayId: Optional[str] = None
    VolumeIds: Optional[List[str]] = None


class Volume(BaseValidatorModel):
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


class DetachElasticLoadBalancerRequest(BaseValidatorModel):
    ElasticLoadBalancerName: str
    LayerId: str


class DisassociateElasticIpRequest(BaseValidatorModel):
    ElasticIp: str


class GetHostnameSuggestionRequest(BaseValidatorModel):
    LayerId: str


class GrantAccessRequest(BaseValidatorModel):
    InstanceId: str
    ValidForInMinutes: Optional[int] = None


class TemporaryCredential(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None
    ValidForInMinutes: Optional[int] = None
    InstanceId: Optional[str] = None


class InstanceIdentity(BaseValidatorModel):
    Document: Optional[str] = None
    Signature: Optional[str] = None


class ReportedOs(BaseValidatorModel):
    Family: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None


class InstancesCount(BaseValidatorModel):
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


class RecipesOutput(BaseValidatorModel):
    Setup: Optional[List[str]] = None
    Configure: Optional[List[str]] = None
    Deploy: Optional[List[str]] = None
    Undeploy: Optional[List[str]] = None
    Shutdown: Optional[List[str]] = None


class ShutdownEventConfiguration(BaseValidatorModel):
    ExecutionTimeout: Optional[int] = None
    DelayUntilElbConnectionsDrained: Optional[bool] = None


class ListTagsRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OperatingSystemConfigurationManager(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class RebootInstanceRequest(BaseValidatorModel):
    InstanceId: str


class Recipes(BaseValidatorModel):
    Setup: Optional[List[str]] = None
    Configure: Optional[List[str]] = None
    Deploy: Optional[List[str]] = None
    Undeploy: Optional[List[str]] = None
    Shutdown: Optional[List[str]] = None


class RegisterEcsClusterRequest(BaseValidatorModel):
    EcsClusterArn: str
    StackId: str


class RegisterElasticIpRequest(BaseValidatorModel):
    ElasticIp: str
    StackId: str


class RegisterRdsDbInstanceRequest(BaseValidatorModel):
    StackId: str
    RdsDbInstanceArn: str
    DbUser: str
    DbPassword: str


class RegisterVolumeRequest(BaseValidatorModel):
    StackId: str
    Ec2VolumeId: Optional[str] = None


class SetPermissionRequest(BaseValidatorModel):
    StackId: str
    IamUserArn: str
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None


class StartInstanceRequest(BaseValidatorModel):
    InstanceId: str


class StartStackRequest(BaseValidatorModel):
    StackId: str


class StopInstanceRequest(BaseValidatorModel):
    InstanceId: str
    Force: Optional[bool] = None


class StopStackRequest(BaseValidatorModel):
    StackId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class WeeklyAutoScalingScheduleOutput(BaseValidatorModel):
    Monday: Optional[Dict[str, str]] = None
    Tuesday: Optional[Dict[str, str]] = None
    Wednesday: Optional[Dict[str, str]] = None
    Thursday: Optional[Dict[str, str]] = None
    Friday: Optional[Dict[str, str]] = None
    Saturday: Optional[Dict[str, str]] = None
    Sunday: Optional[Dict[str, str]] = None


class UnassignInstanceRequest(BaseValidatorModel):
    InstanceId: str


class UnassignVolumeRequest(BaseValidatorModel):
    VolumeId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateElasticIpRequest(BaseValidatorModel):
    ElasticIp: str
    Name: Optional[str] = None


class UpdateInstanceRequest(BaseValidatorModel):
    InstanceId: str
    LayerIds: Optional[List[str]] = None
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


class UpdateMyUserProfileRequest(BaseValidatorModel):
    SshPublicKey: Optional[str] = None


class UpdateRdsDbInstanceRequest(BaseValidatorModel):
    RdsDbInstanceArn: str
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None


class UpdateUserProfileRequest(BaseValidatorModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None


class UpdateVolumeRequest(BaseValidatorModel):
    VolumeId: str
    Name: Optional[str] = None
    MountPoint: Optional[str] = None


class WeeklyAutoScalingSchedule(BaseValidatorModel):
    Monday: Optional[Dict[str, str]] = None
    Tuesday: Optional[Dict[str, str]] = None
    Wednesday: Optional[Dict[str, str]] = None
    Thursday: Optional[Dict[str, str]] = None
    Friday: Optional[Dict[str, str]] = None
    Saturday: Optional[Dict[str, str]] = None
    Sunday: Optional[Dict[str, str]] = None


class AgentVersion(BaseValidatorModel):
    Version: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None


class DescribeAgentVersionsRequest(BaseValidatorModel):
    StackId: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None


class App(BaseValidatorModel):
    AppId: Optional[str] = None
    StackId: Optional[str] = None
    Shortname: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DataSources: Optional[List[DataSource]] = None
    Type: Optional[AppTypeType] = None
    AppSource: Optional[Source] = None
    Domains: Optional[List[str]] = None
    EnableSsl: Optional[bool] = None
    SslConfiguration: Optional[SslConfiguration] = None
    Attributes: Optional[Dict[AppAttributesKeysType, str]] = None
    CreatedAt: Optional[str] = None
    Environment: Optional[List[EnvironmentVariable]] = None


class CreateAppRequest(BaseValidatorModel):
    StackId: str
    Name: str
    Type: AppTypeType
    Shortname: Optional[str] = None
    Description: Optional[str] = None
    DataSources: Optional[List[DataSource]] = None
    AppSource: Optional[Source] = None
    Domains: Optional[List[str]] = None
    EnableSsl: Optional[bool] = None
    SslConfiguration: Optional[SslConfiguration] = None
    Attributes: Optional[Dict[AppAttributesKeysType, str]] = None
    Environment: Optional[List[EnvironmentVariable]] = None


class UpdateAppRequest(BaseValidatorModel):
    AppId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    DataSources: Optional[List[DataSource]] = None
    Type: Optional[AppTypeType] = None
    AppSource: Optional[Source] = None
    Domains: Optional[List[str]] = None
    EnableSsl: Optional[bool] = None
    SslConfiguration: Optional[SslConfiguration] = None
    Attributes: Optional[Dict[AppAttributesKeysType, str]] = None
    Environment: Optional[List[EnvironmentVariable]] = None


class LoadBasedAutoScalingConfiguration(BaseValidatorModel):
    LayerId: Optional[str] = None
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsOutput] = None
    DownScaling: Optional[AutoScalingThresholdsOutput] = None

AutoScalingThresholdsUnion = Union[AutoScalingThresholds, AutoScalingThresholdsOutput]


class BlockDeviceMapping(BaseValidatorModel):
    DeviceName: Optional[str] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDevice] = None


class CloneStackRequest(BaseValidatorModel):
    SourceStackId: str
    ServiceRoleArn: str
    Name: Optional[str] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None
    Attributes: Optional[Dict[Literal['Color'], str]] = None
    DefaultInstanceProfileArn: Optional[str] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None
    ChefConfiguration: Optional[ChefConfiguration] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[Source] = None
    DefaultSshKeyName: Optional[str] = None
    ClonePermissions: Optional[bool] = None
    CloneAppIds: Optional[List[str]] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None


class CreateStackRequestServiceResourceCreateStack(BaseValidatorModel):
    Name: str
    Region: str
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    VpcId: Optional[str] = None
    Attributes: Optional[Dict[Literal['Color'], str]] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None
    ChefConfiguration: Optional[ChefConfiguration] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[Source] = None
    DefaultSshKeyName: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None


class CreateStackRequest(BaseValidatorModel):
    Name: str
    Region: str
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    VpcId: Optional[str] = None
    Attributes: Optional[Dict[Literal['Color'], str]] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None
    ChefConfiguration: Optional[ChefConfiguration] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[Source] = None
    DefaultSshKeyName: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None


class Stack(BaseValidatorModel):
    StackId: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None
    Attributes: Optional[Dict[Literal['Color'], str]] = None
    ServiceRoleArn: Optional[str] = None
    DefaultInstanceProfileArn: Optional[str] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None
    ChefConfiguration: Optional[ChefConfiguration] = None
    UseCustomCookbooks: Optional[bool] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    CustomCookbooksSource: Optional[Source] = None
    DefaultSshKeyName: Optional[str] = None
    CreatedAt: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    AgentVersion: Optional[str] = None


class UpdateStackRequest(BaseValidatorModel):
    StackId: str
    Name: Optional[str] = None
    Attributes: Optional[Dict[Literal['Color'], str]] = None
    ServiceRoleArn: Optional[str] = None
    DefaultInstanceProfileArn: Optional[str] = None
    DefaultOs: Optional[str] = None
    HostnameTheme: Optional[str] = None
    DefaultAvailabilityZone: Optional[str] = None
    DefaultSubnetId: Optional[str] = None
    CustomJson: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManager] = None
    ChefConfiguration: Optional[ChefConfiguration] = None
    UseCustomCookbooks: Optional[bool] = None
    CustomCookbooksSource: Optional[Source] = None
    DefaultSshKeyName: Optional[str] = None
    DefaultRootDeviceType: Optional[RootDeviceTypeType] = None
    UseOpsworksSecurityGroups: Optional[bool] = None
    AgentVersion: Optional[str] = None


class CloneStackResult(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadata


class CreateAppResult(BaseValidatorModel):
    AppId: str
    ResponseMetadata: ResponseMetadata


class CreateDeploymentResult(BaseValidatorModel):
    DeploymentId: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceResult(BaseValidatorModel):
    InstanceId: str
    ResponseMetadata: ResponseMetadata


class CreateLayerResult(BaseValidatorModel):
    LayerId: str
    ResponseMetadata: ResponseMetadata


class CreateStackResult(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadata


class CreateUserProfileResult(BaseValidatorModel):
    IamUserArn: str
    ResponseMetadata: ResponseMetadata


class DescribeStackProvisioningParametersResult(BaseValidatorModel):
    AgentInstallerUrl: str
    Parameters: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetHostnameSuggestionResult(BaseValidatorModel):
    LayerId: str
    Hostname: str
    ResponseMetadata: ResponseMetadata


class ListTagsResult(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RegisterEcsClusterResult(BaseValidatorModel):
    EcsClusterArn: str
    ResponseMetadata: ResponseMetadata


class RegisterElasticIpResult(BaseValidatorModel):
    ElasticIp: str
    ResponseMetadata: ResponseMetadata


class RegisterInstanceResult(BaseValidatorModel):
    InstanceId: str
    ResponseMetadata: ResponseMetadata


class RegisterVolumeResult(BaseValidatorModel):
    VolumeId: str
    ResponseMetadata: ResponseMetadata


class CloudWatchLogsConfigurationOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[List[CloudWatchLogsLogStream]] = None


class CloudWatchLogsConfiguration(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[List[CloudWatchLogsLogStream]] = None


class DescribeCommandsResult(BaseValidatorModel):
    Commands: List[Command]
    ResponseMetadata: ResponseMetadata


class Deployment(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    CreatedAt: Optional[str] = None
    CompletedAt: Optional[str] = None
    Duration: Optional[int] = None
    IamUserArn: Optional[str] = None
    Comment: Optional[str] = None
    Command: Optional[DeploymentCommandOutput] = None
    Status: Optional[str] = None
    CustomJson: Optional[str] = None
    InstanceIds: Optional[List[str]] = None

DeploymentCommandUnion = Union[DeploymentCommand, DeploymentCommandOutput]


class DescribeAppsRequestWait(BaseValidatorModel):
    StackId: Optional[str] = None
    AppIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDeploymentsRequestWait(BaseValidatorModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWaitExtraExtraExtra(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWaitExtraExtra(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWaitExtra(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWait(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEcsClustersRequestPaginate(BaseValidatorModel):
    EcsClusterArns: Optional[List[str]] = None
    StackId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEcsClustersResult(BaseValidatorModel):
    EcsClusters: List[EcsCluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeElasticIpsResult(BaseValidatorModel):
    ElasticIps: List[ElasticIp]
    ResponseMetadata: ResponseMetadata


class DescribeElasticLoadBalancersResult(BaseValidatorModel):
    ElasticLoadBalancers: List[ElasticLoadBalancer]
    ResponseMetadata: ResponseMetadata


class DescribeMyUserProfileResult(BaseValidatorModel):
    UserProfile: SelfUserProfile
    ResponseMetadata: ResponseMetadata


class DescribePermissionsResult(BaseValidatorModel):
    Permissions: List[Permission]
    ResponseMetadata: ResponseMetadata


class DescribeRaidArraysResult(BaseValidatorModel):
    RaidArrays: List[RaidArray]
    ResponseMetadata: ResponseMetadata


class DescribeRdsDbInstancesResult(BaseValidatorModel):
    RdsDbInstances: List[RdsDbInstance]
    ResponseMetadata: ResponseMetadata


class DescribeServiceErrorsResult(BaseValidatorModel):
    ServiceErrors: List[ServiceError]
    ResponseMetadata: ResponseMetadata


class DescribeUserProfilesResult(BaseValidatorModel):
    UserProfiles: List[UserProfile]
    ResponseMetadata: ResponseMetadata


class DescribeVolumesResult(BaseValidatorModel):
    Volumes: List[Volume]
    ResponseMetadata: ResponseMetadata


class GrantAccessResult(BaseValidatorModel):
    TemporaryCredential: TemporaryCredential
    ResponseMetadata: ResponseMetadata


class RegisterInstanceRequest(BaseValidatorModel):
    StackId: str
    Hostname: Optional[str] = None
    PublicIp: Optional[str] = None
    PrivateIp: Optional[str] = None
    RsaPublicKey: Optional[str] = None
    RsaPublicKeyFingerprint: Optional[str] = None
    InstanceIdentity: Optional[InstanceIdentity] = None


class StackSummary(BaseValidatorModel):
    StackId: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    LayersCount: Optional[int] = None
    AppsCount: Optional[int] = None
    InstancesCount: Optional[InstancesCount] = None


class LifecycleEventConfiguration(BaseValidatorModel):
    Shutdown: Optional[ShutdownEventConfiguration] = None


class OperatingSystem(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[str] = None
    ConfigurationManagers: Optional[List[OperatingSystemConfigurationManager]] = None
    ReportedName: Optional[str] = None
    ReportedVersion: Optional[str] = None
    Supported: Optional[bool] = None

RecipesUnion = Union[Recipes, RecipesOutput]


class TimeBasedAutoScalingConfiguration(BaseValidatorModel):
    InstanceId: Optional[str] = None
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleOutput] = None

WeeklyAutoScalingScheduleUnion = Union[WeeklyAutoScalingSchedule, WeeklyAutoScalingScheduleOutput]


class DescribeAgentVersionsResult(BaseValidatorModel):
    AgentVersions: List[AgentVersion]
    ResponseMetadata: ResponseMetadata


class DescribeAppsResult(BaseValidatorModel):
    Apps: List[App]
    ResponseMetadata: ResponseMetadata


class DescribeLoadBasedAutoScalingResult(BaseValidatorModel):
    LoadBasedAutoScalingConfigurations: List[LoadBasedAutoScalingConfiguration]
    ResponseMetadata: ResponseMetadata


class SetLoadBasedAutoScalingRequest(BaseValidatorModel):
    LayerId: str
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsUnion] = None
    DownScaling: Optional[AutoScalingThresholdsUnion] = None


class CreateInstanceRequest(BaseValidatorModel):
    StackId: str
    LayerIds: List[str]
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
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    AgentVersion: Optional[str] = None
    Tenancy: Optional[str] = None


class Instance(BaseValidatorModel):
    AgentVersion: Optional[str] = None
    AmiId: Optional[str] = None
    Architecture: Optional[ArchitectureType] = None
    Arn: Optional[str] = None
    AutoScalingType: Optional[AutoScalingTypeType] = None
    AvailabilityZone: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
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
    ReportedOs: Optional[ReportedOs] = None
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


class DescribeStacksResult(BaseValidatorModel):
    Stacks: List[Stack]
    ResponseMetadata: ResponseMetadata

CloudWatchLogsConfigurationUnion = Union[CloudWatchLogsConfiguration, CloudWatchLogsConfigurationOutput]


class DescribeDeploymentsResult(BaseValidatorModel):
    Deployments: List[Deployment]
    ResponseMetadata: ResponseMetadata


class CreateDeploymentRequest(BaseValidatorModel):
    StackId: str
    Command: DeploymentCommandUnion
    AppId: Optional[str] = None
    InstanceIds: Optional[List[str]] = None
    LayerIds: Optional[List[str]] = None
    Comment: Optional[str] = None
    CustomJson: Optional[str] = None


class DescribeStackSummaryResult(BaseValidatorModel):
    StackSummary: StackSummary
    ResponseMetadata: ResponseMetadata


class Layer(BaseValidatorModel):
    Arn: Optional[str] = None
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    Type: Optional[LayerTypeType] = None
    Name: Optional[str] = None
    Shortname: Optional[str] = None
    Attributes: Optional[Dict[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationOutput] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[List[str]] = None
    DefaultSecurityGroupNames: Optional[List[str]] = None
    Packages: Optional[List[str]] = None
    VolumeConfigurations: Optional[List[VolumeConfiguration]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    DefaultRecipes: Optional[RecipesOutput] = None
    CustomRecipes: Optional[RecipesOutput] = None
    CreatedAt: Optional[str] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfiguration] = None


class DescribeOperatingSystemsResponse(BaseValidatorModel):
    OperatingSystems: List[OperatingSystem]
    ResponseMetadata: ResponseMetadata


class DescribeTimeBasedAutoScalingResult(BaseValidatorModel):
    TimeBasedAutoScalingConfigurations: List[TimeBasedAutoScalingConfiguration]
    ResponseMetadata: ResponseMetadata


class SetTimeBasedAutoScalingRequest(BaseValidatorModel):
    InstanceId: str
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleUnion] = None


class DescribeInstancesResult(BaseValidatorModel):
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata


class CreateLayerRequestStackCreateLayer(BaseValidatorModel):
    Type: LayerTypeType
    Name: str
    Shortname: str
    Attributes: Optional[Dict[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationUnion] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[List[str]] = None
    Packages: Optional[List[str]] = None
    VolumeConfigurations: Optional[List[VolumeConfiguration]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesUnion] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfiguration] = None


class CreateLayerRequest(BaseValidatorModel):
    StackId: str
    Type: LayerTypeType
    Name: str
    Shortname: str
    Attributes: Optional[Dict[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationUnion] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[List[str]] = None
    Packages: Optional[List[str]] = None
    VolumeConfigurations: Optional[List[VolumeConfiguration]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesUnion] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfiguration] = None


class UpdateLayerRequest(BaseValidatorModel):
    LayerId: str
    Name: Optional[str] = None
    Shortname: Optional[str] = None
    Attributes: Optional[Dict[LayerAttributesKeysType, str]] = None
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationUnion] = None
    CustomInstanceProfileArn: Optional[str] = None
    CustomJson: Optional[str] = None
    CustomSecurityGroupIds: Optional[List[str]] = None
    Packages: Optional[List[str]] = None
    VolumeConfigurations: Optional[List[VolumeConfiguration]] = None
    EnableAutoHealing: Optional[bool] = None
    AutoAssignElasticIps: Optional[bool] = None
    AutoAssignPublicIps: Optional[bool] = None
    CustomRecipes: Optional[RecipesUnion] = None
    InstallUpdatesOnBoot: Optional[bool] = None
    UseEbsOptimizedInstances: Optional[bool] = None
    LifecycleEventConfiguration: Optional[LifecycleEventConfiguration] = None


class DescribeLayersResult(BaseValidatorModel):
    Layers: List[Layer]
    ResponseMetadata: ResponseMetadata