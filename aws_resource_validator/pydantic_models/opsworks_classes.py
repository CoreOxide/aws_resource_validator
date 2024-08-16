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
from aws_resource_validator.pydantic_models.opsworks_constants import *

class StackConfigurationManagerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class DataSourceTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Arn: Optional[str] = None
    DatabaseName: Optional[str] = None

class EnvironmentVariableTypeDef(BaseValidatorModel):
    Key: str
    Value: str
    Secure: Optional[bool] = None

class SourceTypeDef(BaseValidatorModel):
    Type: Optional[SourceTypeType] = None
    Url: Optional[str] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    SshKey: Optional[str] = None
    Revision: Optional[str] = None

class SslConfigurationTypeDef(BaseValidatorModel):
    Certificate: str
    PrivateKey: str
    Chain: Optional[str] = None

class AssignInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LayerIds: Sequence[str]

class AssignVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    InstanceId: Optional[str] = None

class AssociateElasticIpRequestRequestTypeDef(BaseValidatorModel):
    ElasticIp: str
    InstanceId: Optional[str] = None

class AttachElasticLoadBalancerRequestRequestTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ChefConfigurationTypeDef(BaseValidatorModel):
    ManageBerkshelf: Optional[bool] = None
    BerkshelfVersion: Optional[str] = None

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

class CommandTypeDef(BaseValidatorModel):
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

class DeploymentCommandTypeDef(BaseValidatorModel):
    Name: DeploymentCommandNameType
    Args: Optional[Mapping[str, Sequence[str]]] = None

class RecipesTypeDef(BaseValidatorModel):
    Setup: Optional[Sequence[str]] = None
    Configure: Optional[Sequence[str]] = None
    Deploy: Optional[Sequence[str]] = None
    Undeploy: Optional[Sequence[str]] = None
    Shutdown: Optional[Sequence[str]] = None

class VolumeConfigurationTypeDef(BaseValidatorModel):
    MountPoint: str
    NumberOfDisks: int
    Size: int
    RaidLevel: Optional[int] = None
    VolumeType: Optional[str] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None

class CreateUserProfileRequestRequestTypeDef(BaseValidatorModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None

class DeleteAppRequestRequestTypeDef(BaseValidatorModel):
    AppId: str

class DeleteInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DeleteElasticIp: Optional[bool] = None
    DeleteVolumes: Optional[bool] = None

class DeleteLayerRequestRequestTypeDef(BaseValidatorModel):
    LayerId: str

class DeleteStackRequestRequestTypeDef(BaseValidatorModel):
    StackId: str

class DeleteUserProfileRequestRequestTypeDef(BaseValidatorModel):
    IamUserArn: str

class DeploymentCommandOutputTypeDef(BaseValidatorModel):
    Name: DeploymentCommandNameType
    Args: Optional[Dict[str, List[str]]] = None

class DeregisterEcsClusterRequestRequestTypeDef(BaseValidatorModel):
    EcsClusterArn: str

class DeregisterElasticIpRequestRequestTypeDef(BaseValidatorModel):
    ElasticIp: str

class DeregisterInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class DeregisterRdsDbInstanceRequestRequestTypeDef(BaseValidatorModel):
    RdsDbInstanceArn: str

class DeregisterVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAppsRequestRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppIds: Optional[Sequence[str]] = None

class DescribeCommandsRequestRequestTypeDef(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    InstanceId: Optional[str] = None
    CommandIds: Optional[Sequence[str]] = None

class DescribeDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeEcsClustersRequestRequestTypeDef(BaseValidatorModel):
    EcsClusterArns: Optional[Sequence[str]] = None
    StackId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class EcsClusterTypeDef(BaseValidatorModel):
    EcsClusterArn: Optional[str] = None
    EcsClusterName: Optional[str] = None
    StackId: Optional[str] = None
    RegisteredAt: Optional[str] = None

class DescribeElasticIpsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    StackId: Optional[str] = None
    Ips: Optional[Sequence[str]] = None

class ElasticIpTypeDef(BaseValidatorModel):
    Ip: Optional[str] = None
    Name: Optional[str] = None
    Domain: Optional[str] = None
    Region: Optional[str] = None
    InstanceId: Optional[str] = None

class DescribeElasticLoadBalancersRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeInstancesRequestRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None

class DescribeLayersRequestRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerIds: Optional[Sequence[str]] = None

class DescribeLoadBasedAutoScalingRequestRequestTypeDef(BaseValidatorModel):
    LayerIds: Sequence[str]

class SelfUserProfileTypeDef(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None

class DescribePermissionsRequestRequestTypeDef(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    StackId: Optional[str] = None

class PermissionTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    IamUserArn: Optional[str] = None
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None

class DescribeRaidArraysRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeRdsDbInstancesRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeServiceErrorsRequestRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    ServiceErrorIds: Optional[Sequence[str]] = None

class ServiceErrorTypeDef(BaseValidatorModel):
    ServiceErrorId: Optional[str] = None
    StackId: Optional[str] = None
    InstanceId: Optional[str] = None
    Type: Optional[str] = None
    Message: Optional[str] = None
    CreatedAt: Optional[str] = None

class DescribeStackProvisioningParametersRequestRequestTypeDef(BaseValidatorModel):
    StackId: str

class DescribeStackSummaryRequestRequestTypeDef(BaseValidatorModel):
    StackId: str

class DescribeStacksRequestRequestTypeDef(BaseValidatorModel):
    StackIds: Optional[Sequence[str]] = None

class DescribeTimeBasedAutoScalingRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]

class DescribeUserProfilesRequestRequestTypeDef(BaseValidatorModel):
    IamUserArns: Optional[Sequence[str]] = None

class UserProfileTypeDef(BaseValidatorModel):
    IamUserArn: Optional[str] = None
    Name: Optional[str] = None
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None

class DescribeVolumesRequestRequestTypeDef(BaseValidatorModel):
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

class DetachElasticLoadBalancerRequestRequestTypeDef(BaseValidatorModel):
    ElasticLoadBalancerName: str
    LayerId: str

class DisassociateElasticIpRequestRequestTypeDef(BaseValidatorModel):
    ElasticIp: str

class GetHostnameSuggestionRequestRequestTypeDef(BaseValidatorModel):
    LayerId: str

class GrantAccessRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class OperatingSystemConfigurationManagerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class RebootInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class RegisterEcsClusterRequestRequestTypeDef(BaseValidatorModel):
    EcsClusterArn: str
    StackId: str

class RegisterElasticIpRequestRequestTypeDef(BaseValidatorModel):
    ElasticIp: str
    StackId: str

class RegisterRdsDbInstanceRequestRequestTypeDef(BaseValidatorModel):
    StackId: str
    RdsDbInstanceArn: str
    DbUser: str
    DbPassword: str

class RegisterVolumeRequestRequestTypeDef(BaseValidatorModel):
    StackId: str
    Ec2VolumeId: Optional[str] = None

class SetPermissionRequestRequestTypeDef(BaseValidatorModel):
    StackId: str
    IamUserArn: str
    AllowSsh: Optional[bool] = None
    AllowSudo: Optional[bool] = None
    Level: Optional[str] = None

class WeeklyAutoScalingScheduleTypeDef(BaseValidatorModel):
    Monday: Optional[Mapping[str, str]] = None
    Tuesday: Optional[Mapping[str, str]] = None
    Wednesday: Optional[Mapping[str, str]] = None
    Thursday: Optional[Mapping[str, str]] = None
    Friday: Optional[Mapping[str, str]] = None
    Saturday: Optional[Mapping[str, str]] = None
    Sunday: Optional[Mapping[str, str]] = None

class StartInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class StartStackRequestRequestTypeDef(BaseValidatorModel):
    StackId: str

class StopInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Force: Optional[bool] = None

class StopStackRequestRequestTypeDef(BaseValidatorModel):
    StackId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class UnassignInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class UnassignVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateElasticIpRequestRequestTypeDef(BaseValidatorModel):
    ElasticIp: str
    Name: Optional[str] = None

class UpdateInstanceRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateMyUserProfileRequestRequestTypeDef(BaseValidatorModel):
    SshPublicKey: Optional[str] = None

class UpdateRdsDbInstanceRequestRequestTypeDef(BaseValidatorModel):
    RdsDbInstanceArn: str
    DbUser: Optional[str] = None
    DbPassword: Optional[str] = None

class UpdateUserProfileRequestRequestTypeDef(BaseValidatorModel):
    IamUserArn: str
    SshUsername: Optional[str] = None
    SshPublicKey: Optional[str] = None
    AllowSelfManagement: Optional[bool] = None

class UpdateVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    Name: Optional[str] = None
    MountPoint: Optional[str] = None

class AgentVersionTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None

class DescribeAgentVersionsRequestRequestTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    ConfigurationManager: Optional[StackConfigurationManagerTypeDef] = None

class AppTypeDef(BaseValidatorModel):
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

class CreateAppRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAppRequestRequestTypeDef(BaseValidatorModel):
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

class LoadBasedAutoScalingConfigurationTypeDef(BaseValidatorModel):
    LayerId: Optional[str] = None
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsOutputTypeDef] = None
    DownScaling: Optional[AutoScalingThresholdsOutputTypeDef] = None

class SetLoadBasedAutoScalingRequestRequestTypeDef(BaseValidatorModel):
    LayerId: str
    Enable: Optional[bool] = None
    UpScaling: Optional[AutoScalingThresholdsTypeDef] = None
    DownScaling: Optional[AutoScalingThresholdsTypeDef] = None

class BlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDeviceTypeDef] = None

class ChefConfigurationResponseTypeDef(BaseValidatorModel):
    ManageBerkshelf: bool
    BerkshelfVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class InstancesCountResponseTypeDef(BaseValidatorModel):
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

class ListTagsResultTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RecipesResponseTypeDef(BaseValidatorModel):
    Setup: List[str]
    Configure: List[str]
    Deploy: List[str]
    Undeploy: List[str]
    Shutdown: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

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

class SourceResponseTypeDef(BaseValidatorModel):
    Type: SourceTypeType
    Url: str
    Username: str
    Password: str
    SshKey: str
    Revision: str
    ResponseMetadata: ResponseMetadataTypeDef

class StackConfigurationManagerResponseTypeDef(BaseValidatorModel):
    Name: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloneStackRequestRequestTypeDef(BaseValidatorModel):
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

class CreateStackRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateStackRequestRequestTypeDef(BaseValidatorModel):
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

class CloudWatchLogsConfigurationOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[List[CloudWatchLogsLogStreamTypeDef]] = None

class CloudWatchLogsConfigurationResponseTypeDef(BaseValidatorModel):
    Enabled: bool
    LogStreams: List[CloudWatchLogsLogStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CloudWatchLogsConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogStreams: Optional[Sequence[CloudWatchLogsLogStreamTypeDef]] = None

class DescribeCommandsResultTypeDef(BaseValidatorModel):
    Commands: List[CommandTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    StackId: str
    Command: DeploymentCommandTypeDef
    AppId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    LayerIds: Optional[Sequence[str]] = None
    Comment: Optional[str] = None
    CustomJson: Optional[str] = None

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

class DescribeAppsRequestAppExistsWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    AppId: Optional[str] = None
    DeploymentIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceOnlineWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceRegisteredWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceStoppedWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceTerminatedWaitTypeDef(BaseValidatorModel):
    StackId: Optional[str] = None
    LayerId: Optional[str] = None
    InstanceIds: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef(BaseValidatorModel):
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

class RegisterInstanceRequestRequestTypeDef(BaseValidatorModel):
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

class LifecycleEventConfigurationResponseTypeDef(BaseValidatorModel):
    Shutdown: ShutdownEventConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleEventConfigurationTypeDef(BaseValidatorModel):
    Shutdown: Optional[ShutdownEventConfigurationTypeDef] = None

class OperatingSystemTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[str] = None
    ConfigurationManagers: Optional[List[OperatingSystemConfigurationManagerTypeDef]] = None
    ReportedName: Optional[str] = None
    ReportedVersion: Optional[str] = None
    Supported: Optional[bool] = None

class SetTimeBasedAutoScalingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleTypeDef] = None

class TimeBasedAutoScalingConfigurationTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    AutoScalingSchedule: Optional[WeeklyAutoScalingScheduleOutputTypeDef] = None

class DescribeAgentVersionsResultTypeDef(BaseValidatorModel):
    AgentVersions: List[AgentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppsResultTypeDef(BaseValidatorModel):
    Apps: List[AppTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBasedAutoScalingResultTypeDef(BaseValidatorModel):
    LoadBasedAutoScalingConfigurations: List[LoadBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeStackSummaryResultTypeDef(BaseValidatorModel):
    StackSummary: StackSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayerRequestRequestTypeDef(BaseValidatorModel):
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

class CreateLayerRequestStackCreateLayerTypeDef(BaseValidatorModel):
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

class LayerTypeDef(BaseValidatorModel):
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

class UpdateLayerRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeOperatingSystemsResponseTypeDef(BaseValidatorModel):
    OperatingSystems: List[OperatingSystemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTimeBasedAutoScalingResultTypeDef(BaseValidatorModel):
    TimeBasedAutoScalingConfigurations: List[TimeBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstancesResultTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLayersResultTypeDef(BaseValidatorModel):
    Layers: List[LayerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

