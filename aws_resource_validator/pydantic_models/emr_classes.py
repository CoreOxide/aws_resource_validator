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
from aws_resource_validator.pydantic_models.emr_constants import *

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
    Args: Optional[Sequence[str]] = None
    AdditionalInfo: Optional[Mapping[str, str]] = None


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


class CancelStepsInput(BaseValidatorModel):
    ClusterId: str
    StepIds: Sequence[str]
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


class ConfigurationPaginator(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None


class Configuration(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[Sequence[Mapping[str, Any]]] = None
    Properties: Optional[Mapping[str, str]] = None


class CreateSecurityConfigurationInput(BaseValidatorModel):
    Name: str
    SecurityConfiguration: str


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


class DeleteStudioInput(BaseValidatorModel):
    StudioId: str


class DeleteStudioSessionMappingInput(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None


class DescribeClusterInput(BaseValidatorModel):
    ClusterId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeNotebookExecutionInput(BaseValidatorModel):
    NotebookExecutionId: str


class DescribeReleaseLabelInput(BaseValidatorModel):
    ReleaseLabel: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OSRelease(BaseValidatorModel):
    Label: Optional[str] = None


class SimplifiedApplication(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class DescribeSecurityConfigurationInput(BaseValidatorModel):
    Name: str


class DescribeStepInput(BaseValidatorModel):
    ClusterId: str
    StepId: str


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


class FailureDetails(BaseValidatorModel):
    Reason: Optional[str] = None
    Message: Optional[str] = None
    LogFile: Optional[str] = None


class GetAutoTerminationPolicyInput(BaseValidatorModel):
    ClusterId: str


class GetClusterSessionCredentialsInput(BaseValidatorModel):
    ClusterId: str
    ExecutionRoleArn: Optional[str] = None


class GetManagedScalingPolicyInput(BaseValidatorModel):
    ClusterId: str


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
    InstancesToTerminate: Optional[Sequence[str]] = None
    InstancesToProtect: Optional[Sequence[str]] = None
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


class ListBootstrapActionsInput(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None


class ListInstanceFleetsInput(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None


class ListInstanceGroupsInput(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None


class ListInstancesInput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[Sequence[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[Sequence[InstanceStateType]] = None
    Marker: Optional[str] = None


class ReleaseLabelFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Application: Optional[str] = None


class ListSecurityConfigurationsInput(BaseValidatorModel):
    Marker: Optional[str] = None


class SecurityConfigurationSummary(BaseValidatorModel):
    Name: Optional[str] = None
    CreationDateTime: Optional[datetime] = None


class ListStepsInput(BaseValidatorModel):
    ClusterId: str
    StepStates: Optional[Sequence[StepStateType]] = None
    StepIds: Optional[Sequence[str]] = None
    Marker: Optional[str] = None


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


class ListSupportedInstanceTypesInput(BaseValidatorModel):
    ReleaseLabel: str
    Marker: Optional[str] = None


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
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None
    CapacityReservationPreference: Optional[OnDemandCapacityReservationPreferenceType] = None
    CapacityReservationResourceGroupArn: Optional[str] = None


class OutputNotebookS3LocationFromInput(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class PlacementType(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[Sequence[str]] = None


class RemoveAutoScalingPolicyInput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str


class RemoveAutoTerminationPolicyInput(BaseValidatorModel):
    ClusterId: str


class RemoveManagedScalingPolicyInput(BaseValidatorModel):
    ClusterId: str


class RemoveTagsInput(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]


class SupportedProductConfig(BaseValidatorModel):
    Name: Optional[str] = None
    Args: Optional[Sequence[str]] = None


class SimpleScalingPolicyConfiguration(BaseValidatorModel):
    ScalingAdjustment: int
    AdjustmentType: Optional[AdjustmentTypeType] = None
    CoolDown: Optional[int] = None


class ScriptBootstrapActionConfig(BaseValidatorModel):
    Path: str
    Args: Optional[Sequence[str]] = None


class SetKeepJobFlowAliveWhenNoStepsInput(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    KeepJobFlowAliveWhenNoSteps: bool


class SetTerminationProtectionInput(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    TerminationProtected: bool


class SetUnhealthyNodeReplacementInput(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    UnhealthyNodeReplacement: bool


class SetVisibleToAllUsersInput(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    VisibleToAllUsers: bool


class StepExecutionStatusDetail(BaseValidatorModel):
    State: StepExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None


class StepStateChangeReason(BaseValidatorModel):
    Code: Optional[Literal["NONE"]] = None
    Message: Optional[str] = None


class StepTimeline(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


class StopNotebookExecutionInput(BaseValidatorModel):
    NotebookExecutionId: str


class TerminateJobFlowsInput(BaseValidatorModel):
    JobFlowIds: Sequence[str]


class UpdateStudioInput(BaseValidatorModel):
    StudioId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DefaultS3Location: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None


class UpdateStudioSessionMappingInput(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None


class AddInstanceFleetOutput(BaseValidatorModel):
    ClusterId: str
    InstanceFleetId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class AddInstanceGroupsOutput(BaseValidatorModel):
    JobFlowId: str
    InstanceGroupIds: List[str]
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class AddJobFlowStepsOutput(BaseValidatorModel):
    StepIds: List[str]
    ResponseMetadata: ResponseMetadata


class CreateSecurityConfigurationOutput(BaseValidatorModel):
    Name: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateStudioOutput(BaseValidatorModel):
    StudioId: str
    Url: str
    ResponseMetadata: ResponseMetadata


class DescribeSecurityConfigurationOutput(BaseValidatorModel):
    Name: str
    SecurityConfiguration: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListReleaseLabelsOutput(BaseValidatorModel):
    ReleaseLabels: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyClusterOutput(BaseValidatorModel):
    StepConcurrencyLevel: int
    ResponseMetadata: ResponseMetadata


class RunJobFlowOutput(BaseValidatorModel):
    JobFlowId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class StartNotebookExecutionOutput(BaseValidatorModel):
    NotebookExecutionId: str
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[Tag]


class CreateStudioInput(BaseValidatorModel):
    Name: str
    AuthMode: AuthModeType
    VpcId: str
    SubnetIds: Sequence[str]
    ServiceRole: str
    WorkspaceSecurityGroupId: str
    EngineSecurityGroupId: str
    DefaultS3Location: str
    Description: Optional[str] = None
    UserRole: Optional[str] = None
    IdpAuthUrl: Optional[str] = None
    IdpRelayStateParameterName: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
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


class AutoScalingPolicyStatus(BaseValidatorModel):
    State: Optional[AutoScalingPolicyStateType] = None
    StateChangeReason: Optional[AutoScalingPolicyStateChangeReason] = None


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
    PermittedPublicSecurityGroupRuleRanges: Optional[Sequence[PortRange]] = None


class BootstrapActionConfigOutput(BaseValidatorModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigOutput


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
    Dimensions: Optional[Sequence[MetricDimension]] = None


class ClusterStatus(BaseValidatorModel):
    State: Optional[ClusterStateType] = None
    StateChangeReason: Optional[ClusterStateChangeReason] = None
    Timeline: Optional[ClusterTimeline] = None
    ErrorDetails: Optional[List[ErrorDetail]] = None


class ListBootstrapActionsOutput(BaseValidatorModel):
    BootstrapActions: List[Command]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ComputeLimits(BaseValidatorModel):
    pass


class ManagedScalingPolicy(BaseValidatorModel):
    ComputeLimits: Optional[ComputeLimits] = None
    UtilizationPerformanceIndex: Optional[int] = None
    ScalingStrategy: Optional[ScalingStrategyType] = None


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


class Timestamp(BaseValidatorModel):
    pass


class DescribeJobFlowsInput(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    JobFlowIds: Optional[Sequence[str]] = None
    JobFlowStates: Optional[Sequence[JobFlowExecutionStateType]] = None


class ListClustersInput(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    ClusterStates: Optional[Sequence[ClusterStateType]] = None
    Marker: Optional[str] = None


class ListNotebookExecutionsInput(BaseValidatorModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[Timestamp] = None
    To: Optional[Timestamp] = None
    Marker: Optional[str] = None
    ExecutionEngineId: Optional[str] = None


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
    Properties: Optional[Sequence[KeyValue]] = None
    MainClass: Optional[str] = None
    Args: Optional[Sequence[str]] = None


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
    ClusterStates: Optional[Sequence[ClusterStateType]] = None
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
    InstanceGroupTypes: Optional[Sequence[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[Sequence[InstanceStateType]] = None
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
    StepStates: Optional[Sequence[StepStateType]] = None
    StepIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStudioSessionMappingsInputPaginate(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStudiosInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReleaseLabelsInput(BaseValidatorModel):
    Filters: Optional[ReleaseLabelFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSecurityConfigurationsOutput(BaseValidatorModel):
    SecurityConfigurations: List[SecurityConfigurationSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListStudioSessionMappingsOutput(BaseValidatorModel):
    SessionMappings: List[SessionMappingSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListStudiosOutput(BaseValidatorModel):
    Studios: List[StudioSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


class SupportedInstanceType(BaseValidatorModel):
    pass


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


class ExecutionEngineConfig(BaseValidatorModel):
    pass


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
    OutputNotebookFormat: Optional[Literal["HTML"]] = None
    EnvironmentVariables: Optional[Dict[str, str]] = None


class OnDemandProvisioningSpecification(BaseValidatorModel):
    AllocationStrategy: OnDemandProvisioningAllocationStrategyType
    CapacityReservationOptions: Optional[OnDemandCapacityReservationOptions] = None


class OnDemandResizingSpecification(BaseValidatorModel):
    TimeoutDurationMinutes: Optional[int] = None
    AllocationStrategy: Optional[OnDemandProvisioningAllocationStrategyType] = None
    CapacityReservationOptions: Optional[OnDemandCapacityReservationOptions] = None


class StartNotebookExecutionInput(BaseValidatorModel):
    ExecutionEngine: ExecutionEngineConfig
    ServiceRole: str
    EditorId: Optional[str] = None
    RelativePath: Optional[str] = None
    NotebookExecutionName: Optional[str] = None
    NotebookParams: Optional[str] = None
    NotebookInstanceSecurityGroupId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    NotebookS3Location: Optional[NotebookS3LocationFromInput] = None
    OutputNotebookS3Location: Optional[OutputNotebookS3LocationFromInput] = None
    OutputNotebookFormat: Optional[Literal["HTML"]] = None
    EnvironmentVariables: Optional[Mapping[str, str]] = None


class ScalingAction(BaseValidatorModel):
    SimpleScalingPolicyConfiguration: SimpleScalingPolicyConfiguration
    Market: Optional[MarketTypeType] = None


class StepStatus(BaseValidatorModel):
    State: Optional[StepStateType] = None
    StateChangeReason: Optional[StepStateChangeReason] = None
    FailureDetails: Optional[FailureDetails] = None
    Timeline: Optional[StepTimeline] = None


class DescribeStudioOutput(BaseValidatorModel):
    Studio: Studio
    ResponseMetadata: ResponseMetadata


class GetBlockPublicAccessConfigurationOutput(BaseValidatorModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationOutput
    BlockPublicAccessConfigurationMetadata: BlockPublicAccessConfigurationMetadata
    ResponseMetadata: ResponseMetadata


class BootstrapActionDetail(BaseValidatorModel):
    BootstrapActionConfig: Optional[BootstrapActionConfigOutput] = None


class ScalingTriggerOutput(BaseValidatorModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionOutput


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


class GetManagedScalingPolicyOutput(BaseValidatorModel):
    ManagedScalingPolicy: ManagedScalingPolicy
    ResponseMetadata: ResponseMetadata


class PutManagedScalingPolicyInput(BaseValidatorModel):
    ClusterId: str
    ManagedScalingPolicy: ManagedScalingPolicy


class GetClusterSessionCredentialsOutput(BaseValidatorModel):
    Credentials: Credentials
    ExpiresAt: datetime
    ResponseMetadata: ResponseMetadata


class EbsConfiguration(BaseValidatorModel):
    EbsBlockDeviceConfigs: Optional[Sequence[EbsBlockDeviceConfig]] = None
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


class InstanceResizePolicyUnion(BaseValidatorModel):
    pass


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


class ListNotebookExecutionsOutput(BaseValidatorModel):
    NotebookExecutions: List[NotebookExecutionSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeNotebookExecutionOutput(BaseValidatorModel):
    NotebookExecution: NotebookExecution
    ResponseMetadata: ResponseMetadata


class InstanceFleetProvisioningSpecifications(BaseValidatorModel):
    SpotSpecification: Optional[SpotProvisioningSpecification] = None
    OnDemandSpecification: Optional[OnDemandProvisioningSpecification] = None


class InstanceFleetResizingSpecifications(BaseValidatorModel):
    SpotResizeSpecification: Optional[SpotResizingSpecification] = None
    OnDemandResizeSpecification: Optional[OnDemandResizingSpecification] = None


class ScriptBootstrapActionConfigUnion(BaseValidatorModel):
    pass


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


class BlockPublicAccessConfigurationUnion(BaseValidatorModel):
    pass


class PutBlockPublicAccessConfigurationInput(BaseValidatorModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationUnion


class ScalingRuleOutput(BaseValidatorModel):
    Name: str
    Action: ScalingAction
    Trigger: ScalingTriggerOutput
    Description: Optional[str] = None


class CloudWatchAlarmDefinitionUnion(BaseValidatorModel):
    pass


class ScalingTrigger(BaseValidatorModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionUnion


class ListClustersOutput(BaseValidatorModel):
    Clusters: List[ClusterSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeClusterOutput(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ConfigurationUnion(BaseValidatorModel):
    pass


class InstanceTypeConfig(BaseValidatorModel):
    InstanceType: str
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    EbsConfiguration: Optional[EbsConfiguration] = None
    Configurations: Optional[Sequence[ConfigurationUnion]] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None


class StepDetail(BaseValidatorModel):
    StepConfig: StepConfigOutput
    ExecutionStatusDetail: StepExecutionStatusDetail


class HadoopJarStepConfigUnion(BaseValidatorModel):
    pass


class StepConfig(BaseValidatorModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigUnion
    ActionOnFailure: Optional[ActionOnFailureType] = None


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


class ListStepsOutput(BaseValidatorModel):
    Steps: List[StepSummary]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeStepOutput(BaseValidatorModel):
    Step: Step
    ResponseMetadata: ResponseMetadata


class AutoScalingPolicyDescription(BaseValidatorModel):
    Status: Optional[AutoScalingPolicyStatus] = None
    Constraints: Optional[ScalingConstraints] = None
    Rules: Optional[List[ScalingRuleOutput]] = None


class InstanceFleetConfig(BaseValidatorModel):
    InstanceFleetType: InstanceFleetTypeType
    Name: Optional[str] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    InstanceTypeConfigs: Optional[Sequence[InstanceTypeConfig]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecifications] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecifications] = None
    Context: Optional[str] = None


class InstanceFleetModifyConfig(BaseValidatorModel):
    InstanceFleetId: str
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecifications] = None
    InstanceTypeConfigs: Optional[Sequence[InstanceTypeConfig]] = None
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


class ShrinkPolicyUnion(BaseValidatorModel):
    pass


class InstanceGroupModifyConfig(BaseValidatorModel):
    InstanceGroupId: str
    InstanceCount: Optional[int] = None
    EC2InstanceIdsToTerminate: Optional[Sequence[str]] = None
    ShrinkPolicy: Optional[ShrinkPolicyUnion] = None
    ReconfigurationType: Optional[ReconfigurationTypeType] = None
    Configurations: Optional[Sequence[ConfigurationUnion]] = None


class ListInstanceFleetsOutputPaginator(BaseValidatorModel):
    InstanceFleets: List[InstanceFleetPaginator]
    Marker: str
    ResponseMetadata: ResponseMetadata


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


class PutAutoScalingPolicyOutput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicyDescription
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class ScalingTriggerUnion(BaseValidatorModel):
    pass


class ScalingRule(BaseValidatorModel):
    Name: str
    Action: ScalingAction
    Trigger: ScalingTriggerUnion
    Description: Optional[str] = None


class AddInstanceFleetInput(BaseValidatorModel):
    ClusterId: str
    InstanceFleet: InstanceFleetConfig


class ModifyInstanceFleetInput(BaseValidatorModel):
    ClusterId: str
    InstanceFleet: InstanceFleetModifyConfig


class DescribeJobFlowsOutput(BaseValidatorModel):
    JobFlows: List[JobFlowDetail]
    ResponseMetadata: ResponseMetadata


class StepConfigUnion(BaseValidatorModel):
    pass


class AddJobFlowStepsInput(BaseValidatorModel):
    JobFlowId: str
    Steps: Sequence[StepConfigUnion]
    ExecutionRoleArn: Optional[str] = None


class ModifyInstanceGroupsInput(BaseValidatorModel):
    ClusterId: Optional[str] = None
    InstanceGroups: Optional[Sequence[InstanceGroupModifyConfig]] = None


class ListInstanceGroupsOutputPaginator(BaseValidatorModel):
    InstanceGroups: List[InstanceGroupPaginator]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListInstanceGroupsOutput(BaseValidatorModel):
    InstanceGroups: List[InstanceGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ScalingRuleUnion(BaseValidatorModel):
    pass


class AutoScalingPolicy(BaseValidatorModel):
    Constraints: ScalingConstraints
    Rules: Sequence[ScalingRuleUnion]


class InstanceGroupConfig(BaseValidatorModel):
    InstanceRole: InstanceRoleTypeType
    InstanceType: str
    InstanceCount: int
    Name: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    BidPrice: Optional[str] = None
    Configurations: Optional[Sequence[ConfigurationUnion]] = None
    EbsConfiguration: Optional[EbsConfiguration] = None
    AutoScalingPolicy: Optional[AutoScalingPolicy] = None
    CustomAmiId: Optional[str] = None


class PutAutoScalingPolicyInput(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicy


class AddInstanceGroupsInput(BaseValidatorModel):
    InstanceGroups: Sequence[InstanceGroupConfig]
    JobFlowId: str


class PlacementTypeUnion(BaseValidatorModel):
    pass


class JobFlowInstancesConfig(BaseValidatorModel):
    MasterInstanceType: Optional[str] = None
    SlaveInstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceGroups: Optional[Sequence[InstanceGroupConfig]] = None
    InstanceFleets: Optional[Sequence[InstanceFleetConfig]] = None
    Ec2KeyName: Optional[str] = None
    Placement: Optional[PlacementTypeUnion] = None
    KeepJobFlowAliveWhenNoSteps: Optional[bool] = None
    TerminationProtected: Optional[bool] = None
    UnhealthyNodeReplacement: Optional[bool] = None
    HadoopVersion: Optional[str] = None
    Ec2SubnetId: Optional[str] = None
    Ec2SubnetIds: Optional[Sequence[str]] = None
    EmrManagedMasterSecurityGroup: Optional[str] = None
    EmrManagedSlaveSecurityGroup: Optional[str] = None
    ServiceAccessSecurityGroup: Optional[str] = None
    AdditionalMasterSecurityGroups: Optional[Sequence[str]] = None
    AdditionalSlaveSecurityGroups: Optional[Sequence[str]] = None


class ApplicationUnion(BaseValidatorModel):
    pass


class BootstrapActionConfigUnion(BaseValidatorModel):
    pass


class RunJobFlowInput(BaseValidatorModel):
    Name: str
    Instances: JobFlowInstancesConfig
    LogUri: Optional[str] = None
    LogEncryptionKmsKeyId: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    AmiVersion: Optional[str] = None
    ReleaseLabel: Optional[str] = None
    Steps: Optional[Sequence[StepConfigUnion]] = None
    BootstrapActions: Optional[Sequence[BootstrapActionConfigUnion]] = None
    SupportedProducts: Optional[Sequence[str]] = None
    NewSupportedProducts: Optional[Sequence[SupportedProductConfig]] = None
    Applications: Optional[Sequence[ApplicationUnion]] = None
    Configurations: Optional[Sequence[ConfigurationUnion]] = None
    VisibleToAllUsers: Optional[bool] = None
    JobFlowRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    SecurityConfiguration: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None
    CustomAmiId: Optional[str] = None
    EbsRootVolumeSize: Optional[int] = None
    RepoUpgradeOnBoot: Optional[RepoUpgradeOnBootType] = None
    KerberosAttributes: Optional[KerberosAttributes] = None
    StepConcurrencyLevel: Optional[int] = None
    ManagedScalingPolicy: Optional[ManagedScalingPolicy] = None
    PlacementGroupConfigs: Optional[Sequence[PlacementGroupConfig]] = None
    AutoTerminationPolicy: Optional[AutoTerminationPolicy] = None
    OSReleaseLabel: Optional[str] = None
    EbsRootVolumeIops: Optional[int] = None
    EbsRootVolumeThroughput: Optional[int] = None


