from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.emr.emr_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ApplicationOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Args: Optional[List[str]] = None
    AdditionalInfo: Optional[Dict[str, str]] = None


class Application(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Args: Optional[List[str]] = None
    AdditionalInfo: Optional[Dict[str, str]] = None


class ScalingConstraints(BaseValidatorModel):
    MinCapacity: int
    MaxCapacity: int


class AutoScalingPolicyStateChangeReason(BaseValidatorModel):
    Code: Optional[AutoScalingPolicyStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class AutoTerminationPolicy(BaseValidatorModel):
    IdleTimeout: Optional[int] = None


class BlockPublicAccessConfigurationMetadata(BaseValidatorModel):
    CreationDateTime: datetime
    CreatedByArn: str


class PortRange(BaseValidatorModel):
    MinRange: int
    MaxRange: Optional[int] = None


class ScriptBootstrapActionConfigOutput(BaseValidatorModel):
    Path: str
    Args: Optional[List[str]] = None


class CancelStepsInfo(BaseValidatorModel):
    StepId: Optional[str] = None
    Status: Optional[CancelStepsRequestStatusType] = None
    Reason: Optional[str] = None


# This class is the input for the 'cancel_steps' function.
class CancelStepsInput(BaseValidatorModel):
    ClusterId: str
    StepIds: List[str]
    StepCancellationOption: Optional[StepCancellationOptionType] = None


class MetricDimension(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ClusterStateChangeReason(BaseValidatorModel):
    Code: Optional[ClusterStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class ClusterTimeline(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


class ErrorDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorData: Optional[List[Dict[str, str]]] = None
    ErrorMessage: Optional[str] = None


class ConfigurationOutput(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None


class Ec2InstanceAttributes(BaseValidatorModel):
    Ec2KeyName: Optional[str] = None
    Ec2SubnetId: Optional[str] = None
    RequestedEc2SubnetIds: Optional[List[str]] = None
    Ec2AvailabilityZone: Optional[str] = None
    RequestedEc2AvailabilityZones: Optional[List[str]] = None
    IamInstanceProfile: Optional[str] = None
    EmrManagedMasterSecurityGroup: Optional[str] = None
    EmrManagedSlaveSecurityGroup: Optional[str] = None
    ServiceAccessSecurityGroup: Optional[str] = None
    AdditionalMasterSecurityGroups: Optional[List[str]] = None
    AdditionalSlaveSecurityGroups: Optional[List[str]] = None


class KerberosAttributes(BaseValidatorModel):
    Realm: str
    KdcAdminPassword: str
    CrossRealmTrustPrincipalPassword: Optional[str] = None
    ADDomainJoinUser: Optional[str] = None
    ADDomainJoinPassword: Optional[str] = None


class PlacementGroupConfig(BaseValidatorModel):
    InstanceRole: InstanceRoleTypeType
    PlacementStrategy: Optional[PlacementGroupStrategyType] = None


class Command(BaseValidatorModel):
    Name: Optional[str] = None
    ScriptPath: Optional[str] = None
    Args: Optional[List[str]] = None


class ComputeLimits(BaseValidatorModel):
    UnitType: ComputeLimitsUnitTypeType
    MinimumCapacityUnits: int
    MaximumCapacityUnits: int
    MaximumOnDemandCapacityUnits: Optional[int] = None
    MaximumCoreCapacityUnits: Optional[int] = None


class ConfigurationPaginator(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None


class Configuration(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None


# This class is the input for the 'create_security_configuration' function.
class CreateSecurityConfigurationInput(BaseValidatorModel):
    Name: str
    SecurityConfiguration: str


# This class is the input for the 'create_studio_session_mapping' function.
class CreateStudioSessionMappingInput(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None


class UsernamePassword(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None


class DeleteSecurityConfigurationInput(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_studio' function.
class DeleteStudioInput(BaseValidatorModel):
    StudioId: str


# This class is the input for the 'delete_studio_session_mapping' function.
class DeleteStudioSessionMappingInput(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None


# This class is the input for the 'describe_cluster' function.
class DescribeClusterInput(BaseValidatorModel):
    ClusterId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'describe_notebook_execution' function.
class DescribeNotebookExecutionInput(BaseValidatorModel):
    NotebookExecutionId: str


# This class is the input for the 'describe_release_label' function.
class DescribeReleaseLabelInput(BaseValidatorModel):
    ReleaseLabel: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OSRelease(BaseValidatorModel):
    Label: Optional[str] = None


class SimplifiedApplication(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


# This class is the input for the 'describe_security_configuration' function.
class DescribeSecurityConfigurationInput(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_step' function.
class DescribeStepInput(BaseValidatorModel):
    ClusterId: str
    StepId: str


# This class is the input for the 'describe_studio' function.
class DescribeStudioInput(BaseValidatorModel):
    StudioId: str


class VolumeSpecification(BaseValidatorModel):
    VolumeType: str
    SizeInGB: int
    Iops: Optional[int] = None
    Throughput: Optional[int] = None


class EbsVolume(BaseValidatorModel):
    Device: Optional[str] = None
    VolumeId: Optional[str] = None


class ExecutionEngineConfig(BaseValidatorModel):
    Id: str
    Type: Optional[Literal['EMR']] = None
    MasterInstanceSecurityGroupId: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None


class FailureDetails(BaseValidatorModel):
    Reason: Optional[str] = None
    Message: Optional[str] = None
    LogFile: Optional[str] = None


# This class is the input for the 'get_auto_termination_policy' function.
class GetAutoTerminationPolicyInput(BaseValidatorModel):
    ClusterId: str


# This class is the input for the 'get_cluster_session_credentials' function.
class GetClusterSessionCredentialsInput(BaseValidatorModel):
    ClusterId: str
    ExecutionRoleArn: Optional[str] = None


# This class is the input for the 'get_managed_scaling_policy' function.
class GetManagedScalingPolicyInput(BaseValidatorModel):
    ClusterId: str


# This class is the input for the 'get_studio_session_mapping' function.
class GetStudioSessionMappingInput(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None


class SessionMappingDetail(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    SessionPolicyArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class KeyValue(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class HadoopStepConfig(BaseValidatorModel):
    Jar: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None


class SpotProvisioningSpecification(BaseValidatorModel):
    TimeoutDurationMinutes: int
    TimeoutAction: SpotProvisioningTimeoutActionType
    BlockDurationMinutes: Optional[int] = None
    AllocationStrategy: Optional[SpotProvisioningAllocationStrategyType] = None


class SpotResizingSpecification(BaseValidatorModel):
    TimeoutDurationMinutes: Optional[int] = None
    AllocationStrategy: Optional[SpotProvisioningAllocationStrategyType] = None


class InstanceFleetStateChangeReason(BaseValidatorModel):
    Code: Optional[InstanceFleetStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class InstanceFleetTimeline(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


class InstanceGroupDetail(BaseValidatorModel):
    Market: MarketTypeType
    InstanceRole: InstanceRoleTypeType
    InstanceType: str
    InstanceRequestCount: int
    InstanceRunningCount: int
    State: InstanceGroupStateType
    CreationDateTime: datetime
    InstanceGroupId: Optional[str] = None
    Name: Optional[str] = None
    BidPrice: Optional[str] = None
    LastStateChangeReason: Optional[str] = None
    StartDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    CustomAmiId: Optional[str] = None


class InstanceGroupStateChangeReason(BaseValidatorModel):
    Code: Optional[InstanceGroupStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class InstanceGroupTimeline(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


class InstanceResizePolicyOutput(BaseValidatorModel):
    InstancesToTerminate: Optional[List[str]] = None
    InstancesToProtect: Optional[List[str]] = None
    InstanceTerminationTimeout: Optional[int] = None


class InstanceResizePolicy(BaseValidatorModel):
    InstancesToTerminate: Optional[List[str]] = None
    InstancesToProtect: Optional[List[str]] = None
    InstanceTerminationTimeout: Optional[int] = None


class InstanceStateChangeReason(BaseValidatorModel):
    Code: Optional[InstanceStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class InstanceTimeline(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


class JobFlowExecutionStatusDetail(BaseValidatorModel):
    State: JobFlowExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None


class PlacementTypeOutput(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_bootstrap_actions' function.
class ListBootstrapActionsInput(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None


# This class is the input for the 'list_instance_fleets' function.
class ListInstanceFleetsInput(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None


# This class is the input for the 'list_instance_groups' function.
class ListInstanceGroupsInput(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None


# This class is the input for the 'list_instances' function.
class ListInstancesInput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[List[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[List[InstanceStateType]] = None
    Marker: Optional[str] = None


class ReleaseLabelFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Application: Optional[str] = None


# This class is the input for the 'list_security_configurations' function.
class ListSecurityConfigurationsInput(BaseValidatorModel):
    Marker: Optional[str] = None


class SecurityConfigurationSummary(BaseValidatorModel):
    Name: Optional[str] = None
    CreationDateTime: Optional[datetime] = None


# This class is the input for the 'list_steps' function.
class ListStepsInput(BaseValidatorModel):
    ClusterId: str
    StepStates: Optional[List[StepStateType]] = None
    StepIds: Optional[List[str]] = None
    Marker: Optional[str] = None


# This class is the input for the 'list_studio_session_mappings' function.
class ListStudioSessionMappingsInput(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    Marker: Optional[str] = None


class SessionMappingSummary(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    SessionPolicyArn: Optional[str] = None
    CreationTime: Optional[datetime] = None


# This class is the input for the 'list_studios' function.
class ListStudiosInput(BaseValidatorModel):
    Marker: Optional[str] = None


class StudioSummary(BaseValidatorModel):
    StudioId: Optional[str] = None
    Name: Optional[str] = None
    VpcId: Optional[str] = None
    Description: Optional[str] = None
    Url: Optional[str] = None
    AuthMode: Optional[AuthModeType] = None
    CreationTime: Optional[datetime] = None


# This class is the input for the 'list_supported_instance_types' function.
class ListSupportedInstanceTypesInput(BaseValidatorModel):
    ReleaseLabel: str
    Marker: Optional[str] = None


class SupportedInstanceType(BaseValidatorModel):
    Type: Optional[str] = None
    MemoryGB: Optional[float] = None
    StorageGB: Optional[int] = None
    VCPU: Optional[int] = None
    Is64BitsOnly: Optional[bool] = None
    InstanceFamilyId: Optional[str] = None
    EbsOptimizedAvailable: Optional[bool] = None
    EbsOptimizedByDefault: Optional[bool] = None
    NumberOfDisks: Optional[int] = None
    EbsStorageOnly: Optional[bool] = None
    Architecture: Optional[str] = None


# This class is the input for the 'modify_cluster' function.
class ModifyClusterInput(BaseValidatorModel):
    ClusterId: str
    StepConcurrencyLevel: Optional[int] = None


class NotebookS3LocationForOutput(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class OutputNotebookS3LocationForOutput(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class NotebookS3LocationFromInput(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class OnDemandCapacityReservationOptions(BaseValidatorModel):
    UsageStrategy: Optional[Literal['use-capacity-reservations-first']] = None
    CapacityReservationPreference: Optional[OnDemandCapacityReservationPreferenceType] = None
    CapacityReservationResourceGroupArn: Optional[str] = None


class OutputNotebookS3LocationFromInput(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class PlacementType(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None


class RemoveAutoScalingPolicyInput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str


class RemoveAutoTerminationPolicyInput(BaseValidatorModel):
    ClusterId: str


class RemoveManagedScalingPolicyInput(BaseValidatorModel):
    ClusterId: str


class RemoveTagsInput(BaseValidatorModel):
    ResourceId: str
    TagKeys: List[str]


class SupportedProductConfig(BaseValidatorModel):
    Name: Optional[str] = None
    Args: Optional[List[str]] = None


class SimpleScalingPolicyConfiguration(BaseValidatorModel):
    ScalingAdjustment: int
    AdjustmentType: Optional[AdjustmentTypeType] = None
    CoolDown: Optional[int] = None


class ScriptBootstrapActionConfig(BaseValidatorModel):
    Path: str
    Args: Optional[List[str]] = None


# This class is the input for the 'set_keep_job_flow_alive_when_no_steps' function.
class SetKeepJobFlowAliveWhenNoStepsInput(BaseValidatorModel):
    JobFlowIds: List[str]
    KeepJobFlowAliveWhenNoSteps: bool


# This class is the input for the 'set_termination_protection' function.
class SetTerminationProtectionInput(BaseValidatorModel):
    JobFlowIds: List[str]
    TerminationProtected: bool


# This class is the input for the 'set_unhealthy_node_replacement' function.
class SetUnhealthyNodeReplacementInput(BaseValidatorModel):
    JobFlowIds: List[str]
    UnhealthyNodeReplacement: bool


# This class is the input for the 'set_visible_to_all_users' function.
class SetVisibleToAllUsersInput(BaseValidatorModel):
    JobFlowIds: List[str]
    VisibleToAllUsers: bool


class StepExecutionStatusDetail(BaseValidatorModel):
    State: StepExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None


class StepStateChangeReason(BaseValidatorModel):
    Code: Optional[Literal['NONE']] = None
    Message: Optional[str] = None


class StepTimeline(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


# This class is the input for the 'stop_notebook_execution' function.
class StopNotebookExecutionInput(BaseValidatorModel):
    NotebookExecutionId: str


# This class is the input for the 'terminate_job_flows' function.
class TerminateJobFlowsInput(BaseValidatorModel):
    JobFlowIds: List[str]


# This class is the input for the 'update_studio' function.
class UpdateStudioInput(BaseValidatorModel):
    StudioId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    DefaultS3Location: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None


# This class is the input for the 'update_studio_session_mapping' function.
class UpdateStudioSessionMappingInput(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None


# This class is the output for the 'add_instance_fleet' function.
class AddInstanceFleetOutput(BaseValidatorModel):
    ClusterId: str
    InstanceFleetId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_instance_groups' function.
class AddInstanceGroupsOutput(BaseValidatorModel):
    JobFlowId: str
    InstanceGroupIds: List[str]
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_job_flow_steps' function.
class AddJobFlowStepsOutput(BaseValidatorModel):
    StepIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_security_configuration' function.
class CreateSecurityConfigurationOutput(BaseValidatorModel):
    Name: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_studio' function.
class CreateStudioOutput(BaseValidatorModel):
    StudioId: str
    Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_security_configuration' function.
class DescribeSecurityConfigurationOutput(BaseValidatorModel):
    Name: str
    SecurityConfiguration: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_studio_session_mapping' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_release_labels' function.
class ListReleaseLabelsOutput(BaseValidatorModel):
    ReleaseLabels: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_cluster' function.
class ModifyClusterOutput(BaseValidatorModel):
    StepConcurrencyLevel: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'run_job_flow' function.
class RunJobFlowOutput(BaseValidatorModel):
    JobFlowId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_notebook_execution' function.
class StartNotebookExecutionOutput(BaseValidatorModel):
    NotebookExecutionId: str
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    ResourceId: str
    Tags: List[Tag]


# This class is the input for the 'create_studio' function.
class CreateStudioInput(BaseValidatorModel):
    Name: str
    AuthMode: AuthModeType
    VpcId: str
    SubnetIds: List[str]
    ServiceRole: str
    WorkspaceSecurityGroupId: str
    EngineSecurityGroupId: str
    DefaultS3Location: str
    Description: Optional[str] = None
    UserRole: Optional[str] = None
    IdpAuthUrl: Optional[str] = None
    IdpRelayStateParameterName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    TrustedIdentityPropagationEnabled: Optional[bool] = None
    IdcUserAssignment: Optional[IdcUserAssignmentType] = None
    IdcInstanceArn: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None


class Studio(BaseValidatorModel):
    StudioId: Optional[str] = None
    StudioArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    AuthMode: Optional[AuthModeType] = None
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    ServiceRole: Optional[str] = None
    UserRole: Optional[str] = None
    WorkspaceSecurityGroupId: Optional[str] = None
    EngineSecurityGroupId: Optional[str] = None
    Url: Optional[str] = None
    CreationTime: Optional[datetime] = None
    DefaultS3Location: Optional[str] = None
    IdpAuthUrl: Optional[str] = None
    IdpRelayStateParameterName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    IdcInstanceArn: Optional[str] = None
    TrustedIdentityPropagationEnabled: Optional[bool] = None
    IdcUserAssignment: Optional[IdcUserAssignmentType] = None
    EncryptionKeyArn: Optional[str] = None

ApplicationUnion = Union[Application, ApplicationOutput]


class AutoScalingPolicyStatus(BaseValidatorModel):
    State: Optional[AutoScalingPolicyStateType] = None
    StateChangeReason: Optional[AutoScalingPolicyStateChangeReason] = None


# This class is the output for the 'get_auto_termination_policy' function.
class GetAutoTerminationPolicyOutput(BaseValidatorModel):
    AutoTerminationPolicy: AutoTerminationPolicy
    ResponseMetadata: ResponseMetadata


class PutAutoTerminationPolicyInput(BaseValidatorModel):
    ClusterId: str
    AutoTerminationPolicy: Optional[AutoTerminationPolicy] = None


class BlockPublicAccessConfigurationOutput(BaseValidatorModel):
    BlockPublicSecurityGroupRules: bool
    PermittedPublicSecurityGroupRuleRanges: Optional[List[PortRange]] = None


class BlockPublicAccessConfiguration(BaseValidatorModel):
    BlockPublicSecurityGroupRules: bool
    PermittedPublicSecurityGroupRuleRanges: Optional[List[PortRange]] = None


class BootstrapActionConfigOutput(BaseValidatorModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigOutput


# This class is the output for the 'cancel_steps' function.
class CancelStepsOutput(BaseValidatorModel):
    CancelStepsInfoList: List[CancelStepsInfo]
    ResponseMetadata: ResponseMetadata


class CloudWatchAlarmDefinitionOutput(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    MetricName: str
    Period: int
    Threshold: float
    EvaluationPeriods: Optional[int] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None
    Dimensions: Optional[List[MetricDimension]] = None


class CloudWatchAlarmDefinition(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    MetricName: str
    Period: int
    Threshold: float
    EvaluationPeriods: Optional[int] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None
    Dimensions: Optional[List[MetricDimension]] = None


class ClusterStatus(BaseValidatorModel):
    State: Optional[ClusterStateType] = None
    StateChangeReason: Optional[ClusterStateChangeReason] = None
    Timeline: Optional[ClusterTimeline] = None
    ErrorDetails: Optional[List[ErrorDetail]] = None


# This class is the output for the 'list_bootstrap_actions' function.
class ListBootstrapActionsOutput(BaseValidatorModel):
    BootstrapActions: List[Command]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ManagedScalingPolicy(BaseValidatorModel):
    ComputeLimits: Optional[ComputeLimits] = None
    UtilizationPerformanceIndex: Optional[int] = None
    ScalingStrategy: Optional[ScalingStrategyType] = None

ConfigurationUnion = Union[Configuration, ConfigurationOutput]


class Credentials(BaseValidatorModel):
    UsernamePassword: Optional[UsernamePassword] = None


class DescribeClusterInputWaitExtra(BaseValidatorModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClusterInputWait(BaseValidatorModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStepInputWait(BaseValidatorModel):
    ClusterId: str
    StepId: str
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the input for the 'describe_job_flows' function.
class DescribeJobFlowsInput(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    JobFlowIds: Optional[List[str]] = None
    JobFlowStates: Optional[List[JobFlowExecutionStateType]] = None


# This class is the input for the 'list_clusters' function.
class ListClustersInput(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    ClusterStates: Optional[List[ClusterStateType]] = None
    Marker: Optional[str] = None


# This class is the input for the 'list_notebook_executions' function.
class ListNotebookExecutionsInput(BaseValidatorModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[Timestamp] = None
    To: Optional[Timestamp] = None
    Marker: Optional[str] = None
    ExecutionEngineId: Optional[str] = None


# This class is the output for the 'describe_release_label' function.
class DescribeReleaseLabelOutput(BaseValidatorModel):
    ReleaseLabel: str
    Applications: List[SimplifiedApplication]
    AvailableOSReleases: List[OSRelease]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EbsBlockDeviceConfig(BaseValidatorModel):
    VolumeSpecification: VolumeSpecification
    VolumesPerInstance: Optional[int] = None


class EbsBlockDevice(BaseValidatorModel):
    VolumeSpecification: Optional[VolumeSpecification] = None
    Device: Optional[str] = None


# This class is the output for the 'get_studio_session_mapping' function.
class GetStudioSessionMappingOutput(BaseValidatorModel):
    SessionMapping: SessionMappingDetail
    ResponseMetadata: ResponseMetadata


class HadoopJarStepConfigOutput(BaseValidatorModel):
    Jar: str
    Properties: Optional[List[KeyValue]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None


class HadoopJarStepConfig(BaseValidatorModel):
    Jar: str
    Properties: Optional[List[KeyValue]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None


class InstanceFleetStatus(BaseValidatorModel):
    State: Optional[InstanceFleetStateType] = None
    StateChangeReason: Optional[InstanceFleetStateChangeReason] = None
    Timeline: Optional[InstanceFleetTimeline] = None


class InstanceGroupStatus(BaseValidatorModel):
    State: Optional[InstanceGroupStateType] = None
    StateChangeReason: Optional[InstanceGroupStateChangeReason] = None
    Timeline: Optional[InstanceGroupTimeline] = None


class ShrinkPolicyOutput(BaseValidatorModel):
    DecommissionTimeout: Optional[int] = None
    InstanceResizePolicy: Optional[InstanceResizePolicyOutput] = None

InstanceResizePolicyUnion = Union[InstanceResizePolicy, InstanceResizePolicyOutput]


class InstanceStatus(BaseValidatorModel):
    State: Optional[InstanceStateType] = None
    StateChangeReason: Optional[InstanceStateChangeReason] = None
    Timeline: Optional[InstanceTimeline] = None


class JobFlowInstancesDetail(BaseValidatorModel):
    MasterInstanceType: str
    SlaveInstanceType: str
    InstanceCount: int
    MasterPublicDnsName: Optional[str] = None
    MasterInstanceId: Optional[str] = None
    InstanceGroups: Optional[List[InstanceGroupDetail]] = None
    NormalizedInstanceHours: Optional[int] = None
    Ec2KeyName: Optional[str] = None
    Ec2SubnetId: Optional[str] = None
    Placement: Optional[PlacementTypeOutput] = None
    KeepJobFlowAliveWhenNoSteps: Optional[bool] = None
    TerminationProtected: Optional[bool] = None
    UnhealthyNodeReplacement: Optional[bool] = None
    HadoopVersion: Optional[str] = None


class ListBootstrapActionsInputPaginate(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersInputPaginate(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    ClusterStates: Optional[List[ClusterStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceFleetsInputPaginate(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceGroupsInputPaginate(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesInputPaginate(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[List[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[List[InstanceStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotebookExecutionsInputPaginate(BaseValidatorModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[Timestamp] = None
    To: Optional[Timestamp] = None
    ExecutionEngineId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityConfigurationsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStepsInputPaginate(BaseValidatorModel):
    ClusterId: str
    StepStates: Optional[List[StepStateType]] = None
    StepIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStudioSessionMappingsInputPaginate(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStudiosInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_release_labels' function.
class ListReleaseLabelsInput(BaseValidatorModel):
    Filters: Optional[ReleaseLabelFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_security_configurations' function.
class ListSecurityConfigurationsOutput(BaseValidatorModel):
    SecurityConfigurations: List[SecurityConfigurationSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_studio_session_mappings' function.
class ListStudioSessionMappingsOutput(BaseValidatorModel):
    SessionMappings: List[SessionMappingSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_studios' function.
class ListStudiosOutput(BaseValidatorModel):
    Studios: List[StudioSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_supported_instance_types' function.
class ListSupportedInstanceTypesOutput(BaseValidatorModel):
    SupportedInstanceTypes: List[SupportedInstanceType]
    Marker: str
    ResponseMetadata: ResponseMetadata


class NotebookExecutionSummary(BaseValidatorModel):
    NotebookExecutionId: Optional[str] = None
    EditorId: Optional[str] = None
    NotebookExecutionName: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    NotebookS3Location: Optional[NotebookS3LocationForOutput] = None
    ExecutionEngineId: Optional[str] = None


class NotebookExecution(BaseValidatorModel):
    NotebookExecutionId: Optional[str] = None
    EditorId: Optional[str] = None
    ExecutionEngine: Optional[ExecutionEngineConfig] = None
    NotebookExecutionName: Optional[str] = None
    NotebookParams: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Arn: Optional[str] = None
    OutputNotebookURI: Optional[str] = None
    LastStateChangeReason: Optional[str] = None
    NotebookInstanceSecurityGroupId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    NotebookS3Location: Optional[NotebookS3LocationForOutput] = None
    OutputNotebookS3Location: Optional[OutputNotebookS3LocationForOutput] = None
    OutputNotebookFormat: Optional[Literal['HTML']] = None
    EnvironmentVariables: Optional[Dict[str, str]] = None


class OnDemandProvisioningSpecification(BaseValidatorModel):
    AllocationStrategy: OnDemandProvisioningAllocationStrategyType
    CapacityReservationOptions: Optional[OnDemandCapacityReservationOptions] = None


class OnDemandResizingSpecification(BaseValidatorModel):
    TimeoutDurationMinutes: Optional[int] = None
    AllocationStrategy: Optional[OnDemandProvisioningAllocationStrategyType] = None
    CapacityReservationOptions: Optional[OnDemandCapacityReservationOptions] = None


# This class is the input for the 'start_notebook_execution' function.
class StartNotebookExecutionInput(BaseValidatorModel):
    ExecutionEngine: ExecutionEngineConfig
    ServiceRole: str
    EditorId: Optional[str] = None
    RelativePath: Optional[str] = None
    NotebookExecutionName: Optional[str] = None
    NotebookParams: Optional[str] = None
    NotebookInstanceSecurityGroupId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    NotebookS3Location: Optional[NotebookS3LocationFromInput] = None
    OutputNotebookS3Location: Optional[OutputNotebookS3LocationFromInput] = None
    OutputNotebookFormat: Optional[Literal['HTML']] = None
    EnvironmentVariables: Optional[Dict[str, str]] = None

PlacementTypeUnion = Union[PlacementType, PlacementTypeOutput]


class ScalingAction(BaseValidatorModel):
    SimpleScalingPolicyConfiguration: SimpleScalingPolicyConfiguration
    Market: Optional[MarketTypeType] = None

ScriptBootstrapActionConfigUnion = Union[ScriptBootstrapActionConfig, ScriptBootstrapActionConfigOutput]


class StepStatus(BaseValidatorModel):
    State: Optional[StepStateType] = None
    StateChangeReason: Optional[StepStateChangeReason] = None
    FailureDetails: Optional[FailureDetails] = None
    Timeline: Optional[StepTimeline] = None


# This class is the output for the 'describe_studio' function.
class DescribeStudioOutput(BaseValidatorModel):
    Studio: Studio
    ResponseMetadata: ResponseMetadata


class GetBlockPublicAccessConfigurationOutput(BaseValidatorModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationOutput
    BlockPublicAccessConfigurationMetadata: BlockPublicAccessConfigurationMetadata
    ResponseMetadata: ResponseMetadata

BlockPublicAccessConfigurationUnion = Union[BlockPublicAccessConfiguration, BlockPublicAccessConfigurationOutput]


class BootstrapActionDetail(BaseValidatorModel):
    BootstrapActionConfig: Optional[BootstrapActionConfigOutput] = None


class ScalingTriggerOutput(BaseValidatorModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionOutput

CloudWatchAlarmDefinitionUnion = Union[CloudWatchAlarmDefinition, CloudWatchAlarmDefinitionOutput]


class ClusterSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ClusterStatus] = None
    NormalizedInstanceHours: Optional[int] = None
    ClusterArn: Optional[str] = None
    OutpostArn: Optional[str] = None


class Cluster(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ClusterStatus] = None
    Ec2InstanceAttributes: Optional[Ec2InstanceAttributes] = None
    InstanceCollectionType: Optional[InstanceCollectionTypeType] = None
    LogUri: Optional[str] = None
    LogEncryptionKmsKeyId: Optional[str] = None
    RequestedAmiVersion: Optional[str] = None
    RunningAmiVersion: Optional[str] = None
    ReleaseLabel: Optional[str] = None
    AutoTerminate: Optional[bool] = None
    TerminationProtected: Optional[bool] = None
    UnhealthyNodeReplacement: Optional[bool] = None
    VisibleToAllUsers: Optional[bool] = None
    Applications: Optional[List[ApplicationOutput]] = None
    Tags: Optional[List[Tag]] = None
    ServiceRole: Optional[str] = None
    NormalizedInstanceHours: Optional[int] = None
    MasterPublicDnsName: Optional[str] = None
    Configurations: Optional[List[ConfigurationOutput]] = None
    SecurityConfiguration: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None
    CustomAmiId: Optional[str] = None
    EbsRootVolumeSize: Optional[int] = None
    RepoUpgradeOnBoot: Optional[RepoUpgradeOnBootType] = None
    KerberosAttributes: Optional[KerberosAttributes] = None
    ClusterArn: Optional[str] = None
    OutpostArn: Optional[str] = None
    StepConcurrencyLevel: Optional[int] = None
    PlacementGroups: Optional[List[PlacementGroupConfig]] = None
    OSReleaseLabel: Optional[str] = None
    EbsRootVolumeIops: Optional[int] = None
    EbsRootVolumeThroughput: Optional[int] = None


# This class is the output for the 'get_managed_scaling_policy' function.
class GetManagedScalingPolicyOutput(BaseValidatorModel):
    ManagedScalingPolicy: ManagedScalingPolicy
    ResponseMetadata: ResponseMetadata


class PutManagedScalingPolicyInput(BaseValidatorModel):
    ClusterId: str
    ManagedScalingPolicy: ManagedScalingPolicy


# This class is the output for the 'get_cluster_session_credentials' function.
class GetClusterSessionCredentialsOutput(BaseValidatorModel):
    Credentials: Credentials
    ExpiresAt: datetime
    ResponseMetadata: ResponseMetadata


class EbsConfiguration(BaseValidatorModel):
    EbsBlockDeviceConfigs: Optional[List[EbsBlockDeviceConfig]] = None
    EbsOptimized: Optional[bool] = None


class InstanceTypeSpecificationPaginator(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    Configurations: Optional[List[ConfigurationPaginator]] = None
    EbsBlockDevices: Optional[List[EbsBlockDevice]] = None
    EbsOptimized: Optional[bool] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None


class InstanceTypeSpecification(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    Configurations: Optional[List[ConfigurationOutput]] = None
    EbsBlockDevices: Optional[List[EbsBlockDevice]] = None
    EbsOptimized: Optional[bool] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None


class StepConfigOutput(BaseValidatorModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigOutput
    ActionOnFailure: Optional[ActionOnFailureType] = None

HadoopJarStepConfigUnion = Union[HadoopJarStepConfig, HadoopJarStepConfigOutput]


class ShrinkPolicy(BaseValidatorModel):
    DecommissionTimeout: Optional[int] = None
    InstanceResizePolicy: Optional[InstanceResizePolicyUnion] = None


class Instance(BaseValidatorModel):
    Id: Optional[str] = None
    Ec2InstanceId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIpAddress: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Status: Optional[InstanceStatus] = None
    InstanceGroupId: Optional[str] = None
    InstanceFleetId: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    InstanceType: Optional[str] = None
    EbsVolumes: Optional[List[EbsVolume]] = None


# This class is the output for the 'list_notebook_executions' function.
class ListNotebookExecutionsOutput(BaseValidatorModel):
    NotebookExecutions: List[NotebookExecutionSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_notebook_execution' function.
class DescribeNotebookExecutionOutput(BaseValidatorModel):
    NotebookExecution: NotebookExecution
    ResponseMetadata: ResponseMetadata


class InstanceFleetProvisioningSpecifications(BaseValidatorModel):
    SpotSpecification: Optional[SpotProvisioningSpecification] = None
    OnDemandSpecification: Optional[OnDemandProvisioningSpecification] = None


class InstanceFleetResizingSpecifications(BaseValidatorModel):
    SpotResizeSpecification: Optional[SpotResizingSpecification] = None
    OnDemandResizeSpecification: Optional[OnDemandResizingSpecification] = None


class BootstrapActionConfig(BaseValidatorModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigUnion


class StepSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[HadoopStepConfig] = None
    ActionOnFailure: Optional[ActionOnFailureType] = None
    Status: Optional[StepStatus] = None


class Step(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[HadoopStepConfig] = None
    ActionOnFailure: Optional[ActionOnFailureType] = None
    Status: Optional[StepStatus] = None
    ExecutionRoleArn: Optional[str] = None


class PutBlockPublicAccessConfigurationInput(BaseValidatorModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationUnion


class ScalingRuleOutput(BaseValidatorModel):
    Name: str
    Action: ScalingAction
    Trigger: ScalingTriggerOutput
    Description: Optional[str] = None


class ScalingTrigger(BaseValidatorModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionUnion


# This class is the output for the 'list_clusters' function.
class ListClustersOutput(BaseValidatorModel):
    Clusters: List[ClusterSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster' function.
class DescribeClusterOutput(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class InstanceTypeConfig(BaseValidatorModel):
    InstanceType: str
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    EbsConfiguration: Optional[EbsConfiguration] = None
    Configurations: Optional[List[ConfigurationUnion]] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None


class StepDetail(BaseValidatorModel):
    StepConfig: StepConfigOutput
    ExecutionStatusDetail: StepExecutionStatusDetail


class StepConfig(BaseValidatorModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigUnion
    ActionOnFailure: Optional[ActionOnFailureType] = None

ShrinkPolicyUnion = Union[ShrinkPolicy, ShrinkPolicyOutput]


# This class is the output for the 'list_instances' function.
class ListInstancesOutput(BaseValidatorModel):
    Instances: List[Instance]
    Marker: str
    ResponseMetadata: ResponseMetadata


class InstanceFleetPaginator(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[InstanceFleetStatus] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ProvisionedOnDemandCapacity: Optional[int] = None
    ProvisionedSpotCapacity: Optional[int] = None
    InstanceTypeSpecifications: Optional[List[InstanceTypeSpecificationPaginator]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecifications] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecifications] = None
    Context: Optional[str] = None


class InstanceFleet(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[InstanceFleetStatus] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ProvisionedOnDemandCapacity: Optional[int] = None
    ProvisionedSpotCapacity: Optional[int] = None
    InstanceTypeSpecifications: Optional[List[InstanceTypeSpecification]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecifications] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecifications] = None
    Context: Optional[str] = None

BootstrapActionConfigUnion = Union[BootstrapActionConfig, BootstrapActionConfigOutput]


# This class is the output for the 'list_steps' function.
class ListStepsOutput(BaseValidatorModel):
    Steps: List[StepSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_step' function.
class DescribeStepOutput(BaseValidatorModel):
    Step: Step
    ResponseMetadata: ResponseMetadata


class AutoScalingPolicyDescription(BaseValidatorModel):
    Status: Optional[AutoScalingPolicyStatus] = None
    Constraints: Optional[ScalingConstraints] = None
    Rules: Optional[List[ScalingRuleOutput]] = None

ScalingTriggerUnion = Union[ScalingTrigger, ScalingTriggerOutput]


class InstanceFleetConfig(BaseValidatorModel):
    InstanceFleetType: InstanceFleetTypeType
    Name: Optional[str] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    InstanceTypeConfigs: Optional[List[InstanceTypeConfig]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecifications] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecifications] = None
    Context: Optional[str] = None


class InstanceFleetModifyConfig(BaseValidatorModel):
    InstanceFleetId: str
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecifications] = None
    InstanceTypeConfigs: Optional[List[InstanceTypeConfig]] = None
    Context: Optional[str] = None


class JobFlowDetail(BaseValidatorModel):
    JobFlowId: str
    Name: str
    ExecutionStatusDetail: JobFlowExecutionStatusDetail
    Instances: JobFlowInstancesDetail
    LogUri: Optional[str] = None
    LogEncryptionKmsKeyId: Optional[str] = None
    AmiVersion: Optional[str] = None
    Steps: Optional[List[StepDetail]] = None
    BootstrapActions: Optional[List[BootstrapActionDetail]] = None
    SupportedProducts: Optional[List[str]] = None
    VisibleToAllUsers: Optional[bool] = None
    JobFlowRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None

StepConfigUnion = Union[StepConfig, StepConfigOutput]


class InstanceGroupModifyConfig(BaseValidatorModel):
    InstanceGroupId: str
    InstanceCount: Optional[int] = None
    EC2InstanceIdsToTerminate: Optional[List[str]] = None
    ShrinkPolicy: Optional[ShrinkPolicyUnion] = None
    ReconfigurationType: Optional[ReconfigurationTypeType] = None
    Configurations: Optional[List[ConfigurationUnion]] = None


class ListInstanceFleetsOutputPaginator(BaseValidatorModel):
    InstanceFleets: List[InstanceFleetPaginator]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_fleets' function.
class ListInstanceFleetsOutput(BaseValidatorModel):
    InstanceFleets: List[InstanceFleet]
    Marker: str
    ResponseMetadata: ResponseMetadata


class InstanceGroupPaginator(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    InstanceGroupType: Optional[InstanceGroupTypeType] = None
    BidPrice: Optional[str] = None
    InstanceType: Optional[str] = None
    RequestedInstanceCount: Optional[int] = None
    RunningInstanceCount: Optional[int] = None
    Status: Optional[InstanceGroupStatus] = None
    Configurations: Optional[List[ConfigurationPaginator]] = None
    ConfigurationsVersion: Optional[int] = None
    LastSuccessfullyAppliedConfigurations: Optional[List[ConfigurationPaginator]] = None
    LastSuccessfullyAppliedConfigurationsVersion: Optional[int] = None
    EbsBlockDevices: Optional[List[EbsBlockDevice]] = None
    EbsOptimized: Optional[bool] = None
    ShrinkPolicy: Optional[ShrinkPolicyOutput] = None
    AutoScalingPolicy: Optional[AutoScalingPolicyDescription] = None
    CustomAmiId: Optional[str] = None


class InstanceGroup(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    InstanceGroupType: Optional[InstanceGroupTypeType] = None
    BidPrice: Optional[str] = None
    InstanceType: Optional[str] = None
    RequestedInstanceCount: Optional[int] = None
    RunningInstanceCount: Optional[int] = None
    Status: Optional[InstanceGroupStatus] = None
    Configurations: Optional[List[ConfigurationOutput]] = None
    ConfigurationsVersion: Optional[int] = None
    LastSuccessfullyAppliedConfigurations: Optional[List[ConfigurationOutput]] = None
    LastSuccessfullyAppliedConfigurationsVersion: Optional[int] = None
    EbsBlockDevices: Optional[List[EbsBlockDevice]] = None
    EbsOptimized: Optional[bool] = None
    ShrinkPolicy: Optional[ShrinkPolicyOutput] = None
    AutoScalingPolicy: Optional[AutoScalingPolicyDescription] = None
    CustomAmiId: Optional[str] = None


# This class is the output for the 'put_auto_scaling_policy' function.
class PutAutoScalingPolicyOutput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicyDescription
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class ScalingRule(BaseValidatorModel):
    Name: str
    Action: ScalingAction
    Trigger: ScalingTriggerUnion
    Description: Optional[str] = None


# This class is the input for the 'add_instance_fleet' function.
class AddInstanceFleetInput(BaseValidatorModel):
    ClusterId: str
    InstanceFleet: InstanceFleetConfig


# This class is the input for the 'modify_instance_fleet' function.
class ModifyInstanceFleetInput(BaseValidatorModel):
    ClusterId: str
    InstanceFleet: InstanceFleetModifyConfig


# This class is the output for the 'describe_job_flows' function.
class DescribeJobFlowsOutput(BaseValidatorModel):
    JobFlows: List[JobFlowDetail]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_job_flow_steps' function.
class AddJobFlowStepsInput(BaseValidatorModel):
    JobFlowId: str
    Steps: List[StepConfigUnion]
    ExecutionRoleArn: Optional[str] = None


# This class is the input for the 'modify_instance_groups' function.
class ModifyInstanceGroupsInput(BaseValidatorModel):
    ClusterId: Optional[str] = None
    InstanceGroups: Optional[List[InstanceGroupModifyConfig]] = None


class ListInstanceGroupsOutputPaginator(BaseValidatorModel):
    InstanceGroups: List[InstanceGroupPaginator]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_groups' function.
class ListInstanceGroupsOutput(BaseValidatorModel):
    InstanceGroups: List[InstanceGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata

ScalingRuleUnion = Union[ScalingRule, ScalingRuleOutput]


class AutoScalingPolicy(BaseValidatorModel):
    Constraints: ScalingConstraints
    Rules: List[ScalingRuleUnion]


class InstanceGroupConfig(BaseValidatorModel):
    InstanceRole: InstanceRoleTypeType
    InstanceType: str
    InstanceCount: int
    Name: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    BidPrice: Optional[str] = None
    Configurations: Optional[List[ConfigurationUnion]] = None
    EbsConfiguration: Optional[EbsConfiguration] = None
    AutoScalingPolicy: Optional[AutoScalingPolicy] = None
    CustomAmiId: Optional[str] = None


# This class is the input for the 'put_auto_scaling_policy' function.
class PutAutoScalingPolicyInput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicy


# This class is the input for the 'add_instance_groups' function.
class AddInstanceGroupsInput(BaseValidatorModel):
    InstanceGroups: List[InstanceGroupConfig]
    JobFlowId: str


class JobFlowInstancesConfig(BaseValidatorModel):
    MasterInstanceType: Optional[str] = None
    SlaveInstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroupConfig]] = None
    InstanceFleets: Optional[List[InstanceFleetConfig]] = None
    Ec2KeyName: Optional[str] = None
    Placement: Optional[PlacementTypeUnion] = None
    KeepJobFlowAliveWhenNoSteps: Optional[bool] = None
    TerminationProtected: Optional[bool] = None
    UnhealthyNodeReplacement: Optional[bool] = None
    HadoopVersion: Optional[str] = None
    Ec2SubnetId: Optional[str] = None
    Ec2SubnetIds: Optional[List[str]] = None
    EmrManagedMasterSecurityGroup: Optional[str] = None
    EmrManagedSlaveSecurityGroup: Optional[str] = None
    ServiceAccessSecurityGroup: Optional[str] = None
    AdditionalMasterSecurityGroups: Optional[List[str]] = None
    AdditionalSlaveSecurityGroups: Optional[List[str]] = None


# This class is the input for the 'run_job_flow' function.
class RunJobFlowInput(BaseValidatorModel):
    Name: str
    Instances: JobFlowInstancesConfig
    LogUri: Optional[str] = None
    LogEncryptionKmsKeyId: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    AmiVersion: Optional[str] = None
    ReleaseLabel: Optional[str] = None
    Steps: Optional[List[StepConfigUnion]] = None
    BootstrapActions: Optional[List[BootstrapActionConfigUnion]] = None
    SupportedProducts: Optional[List[str]] = None
    NewSupportedProducts: Optional[List[SupportedProductConfig]] = None
    Applications: Optional[List[ApplicationUnion]] = None
    Configurations: Optional[List[ConfigurationUnion]] = None
    VisibleToAllUsers: Optional[bool] = None
    JobFlowRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SecurityConfiguration: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None
    CustomAmiId: Optional[str] = None
    EbsRootVolumeSize: Optional[int] = None
    RepoUpgradeOnBoot: Optional[RepoUpgradeOnBootType] = None
    KerberosAttributes: Optional[KerberosAttributes] = None
    StepConcurrencyLevel: Optional[int] = None
    ManagedScalingPolicy: Optional[ManagedScalingPolicy] = None
    PlacementGroupConfigs: Optional[List[PlacementGroupConfig]] = None
    AutoTerminationPolicy: Optional[AutoTerminationPolicy] = None
    OSReleaseLabel: Optional[str] = None
    EbsRootVolumeIops: Optional[int] = None
    EbsRootVolumeThroughput: Optional[int] = None