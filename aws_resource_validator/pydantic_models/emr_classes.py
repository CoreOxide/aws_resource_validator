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
from aws_resource_validator.pydantic_models.emr_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ApplicationOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Args: Optional[List[str]] = None
    AdditionalInfo: Optional[Dict[str, str]] = None

class ApplicationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Args: Optional[Sequence[str]] = None
    AdditionalInfo: Optional[Mapping[str, str]] = None

class ScalingConstraintsTypeDef(BaseValidatorModel):
    MinCapacity: int
    MaxCapacity: int

class AutoScalingPolicyStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[AutoScalingPolicyStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class AutoTerminationPolicyTypeDef(BaseValidatorModel):
    IdleTimeout: Optional[int] = None

class BlockPublicAccessConfigurationMetadataTypeDef(BaseValidatorModel):
    CreationDateTime: datetime
    CreatedByArn: str

class PortRangeTypeDef(BaseValidatorModel):
    MinRange: int
    MaxRange: Optional[int] = None

class ScriptBootstrapActionConfigOutputTypeDef(BaseValidatorModel):
    Path: str
    Args: Optional[List[str]] = None

class ScriptBootstrapActionConfigTypeDef(BaseValidatorModel):
    Path: str
    Args: Optional[Sequence[str]] = None

class CancelStepsInfoTypeDef(BaseValidatorModel):
    StepId: Optional[str] = None
    Status: Optional[CancelStepsRequestStatusType] = None
    Reason: Optional[str] = None

class CancelStepsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    StepIds: Sequence[str]
    StepCancellationOption: Optional[StepCancellationOptionType] = None

class MetricDimensionTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ClusterStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[ClusterStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class ClusterTimelineTypeDef(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class ErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorData: Optional[List[Dict[str, str]]] = None
    ErrorMessage: Optional[str] = None

class Ec2InstanceAttributesTypeDef(BaseValidatorModel):
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

class KerberosAttributesTypeDef(BaseValidatorModel):
    Realm: str
    KdcAdminPassword: str
    CrossRealmTrustPrincipalPassword: Optional[str] = None
    ADDomainJoinUser: Optional[str] = None
    ADDomainJoinPassword: Optional[str] = None

class PlacementGroupConfigTypeDef(BaseValidatorModel):
    InstanceRole: InstanceRoleTypeType
    PlacementStrategy: Optional[PlacementGroupStrategyType] = None

class CommandTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ScriptPath: Optional[str] = None
    Args: Optional[List[str]] = None

class ComputeLimitsTypeDef(BaseValidatorModel):
    UnitType: ComputeLimitsUnitTypeType
    MinimumCapacityUnits: int
    MaximumCapacityUnits: int
    MaximumOnDemandCapacityUnits: Optional[int] = None
    MaximumCoreCapacityUnits: Optional[int] = None

class ConfigurationExtraOutputTypeDef(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None

class ConfigurationOutputTypeDef(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None

class ConfigurationTypeDef(BaseValidatorModel):
    Classification: Optional[str] = None
    Configurations: Optional[Sequence[Dict[str, Any]]] = None
    Properties: Optional[Mapping[str, str]] = None

class CreateSecurityConfigurationInputRequestTypeDef(BaseValidatorModel):
    Name: str
    SecurityConfiguration: str

class CreateStudioSessionMappingInputRequestTypeDef(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class UsernamePasswordTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class DeleteSecurityConfigurationInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteStudioInputRequestTypeDef(BaseValidatorModel):
    StudioId: str

class DeleteStudioSessionMappingInputRequestTypeDef(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeClusterInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str

class DescribeNotebookExecutionInputRequestTypeDef(BaseValidatorModel):
    NotebookExecutionId: str

class DescribeReleaseLabelInputRequestTypeDef(BaseValidatorModel):
    ReleaseLabel: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OSReleaseTypeDef(BaseValidatorModel):
    Label: Optional[str] = None

class SimplifiedApplicationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class DescribeSecurityConfigurationInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeStepInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    StepId: str

class DescribeStudioInputRequestTypeDef(BaseValidatorModel):
    StudioId: str

class VolumeSpecificationTypeDef(BaseValidatorModel):
    VolumeType: str
    SizeInGB: int
    Iops: Optional[int] = None
    Throughput: Optional[int] = None

class EbsVolumeTypeDef(BaseValidatorModel):
    Device: Optional[str] = None
    VolumeId: Optional[str] = None

class ExecutionEngineConfigTypeDef(BaseValidatorModel):
    Id: str
    Type: Optional[Literal["EMR"]] = None
    MasterInstanceSecurityGroupId: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None

class FailureDetailsTypeDef(BaseValidatorModel):
    Reason: Optional[str] = None
    Message: Optional[str] = None
    LogFile: Optional[str] = None

class GetAutoTerminationPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str

class GetClusterSessionCredentialsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    ExecutionRoleArn: Optional[str] = None

class GetManagedScalingPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str

class GetStudioSessionMappingInputRequestTypeDef(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class SessionMappingDetailTypeDef(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    SessionPolicyArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class KeyValueTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class HadoopStepConfigTypeDef(BaseValidatorModel):
    Jar: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None

class SpotProvisioningSpecificationTypeDef(BaseValidatorModel):
    TimeoutDurationMinutes: int
    TimeoutAction: SpotProvisioningTimeoutActionType
    BlockDurationMinutes: Optional[int] = None
    AllocationStrategy: Optional[SpotProvisioningAllocationStrategyType] = None

class OnDemandResizingSpecificationTypeDef(BaseValidatorModel):
    TimeoutDurationMinutes: int

class SpotResizingSpecificationTypeDef(BaseValidatorModel):
    TimeoutDurationMinutes: int

class InstanceFleetStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[InstanceFleetStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class InstanceFleetTimelineTypeDef(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class InstanceGroupDetailTypeDef(BaseValidatorModel):
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

class InstanceGroupStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[InstanceGroupStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class InstanceGroupTimelineTypeDef(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class InstanceResizePolicyOutputTypeDef(BaseValidatorModel):
    InstancesToTerminate: Optional[List[str]] = None
    InstancesToProtect: Optional[List[str]] = None
    InstanceTerminationTimeout: Optional[int] = None

class InstanceResizePolicyTypeDef(BaseValidatorModel):
    InstancesToTerminate: Optional[Sequence[str]] = None
    InstancesToProtect: Optional[Sequence[str]] = None
    InstanceTerminationTimeout: Optional[int] = None

class InstanceStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[InstanceStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class InstanceTimelineTypeDef(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class JobFlowExecutionStatusDetailTypeDef(BaseValidatorModel):
    State: JobFlowExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None

class PlacementTypeTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[Sequence[str]] = None

class PlacementTypeOutputTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBootstrapActionsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None

class ListInstanceFleetsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None

class ListInstanceGroupsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    Marker: Optional[str] = None

class ListInstancesInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[Sequence[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[Sequence[InstanceStateType]] = None
    Marker: Optional[str] = None

class ReleaseLabelFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Application: Optional[str] = None

class ListSecurityConfigurationsInputRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None

class SecurityConfigurationSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreationDateTime: Optional[datetime] = None

class ListStepsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    StepStates: Optional[Sequence[StepStateType]] = None
    StepIds: Optional[Sequence[str]] = None
    Marker: Optional[str] = None

class ListStudioSessionMappingsInputRequestTypeDef(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    Marker: Optional[str] = None

class SessionMappingSummaryTypeDef(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    SessionPolicyArn: Optional[str] = None
    CreationTime: Optional[datetime] = None

class ListStudiosInputRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None

class StudioSummaryTypeDef(BaseValidatorModel):
    StudioId: Optional[str] = None
    Name: Optional[str] = None
    VpcId: Optional[str] = None
    Description: Optional[str] = None
    Url: Optional[str] = None
    AuthMode: Optional[AuthModeType] = None
    CreationTime: Optional[datetime] = None

class ListSupportedInstanceTypesInputRequestTypeDef(BaseValidatorModel):
    ReleaseLabel: str
    Marker: Optional[str] = None

class SupportedInstanceTypeTypeDef(BaseValidatorModel):
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

class ModifyClusterInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    StepConcurrencyLevel: Optional[int] = None

class NotebookS3LocationForOutputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class OutputNotebookS3LocationForOutputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class NotebookS3LocationFromInputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class OnDemandCapacityReservationOptionsTypeDef(BaseValidatorModel):
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None
    CapacityReservationPreference: Optional[OnDemandCapacityReservationPreferenceType] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class OutputNotebookS3LocationFromInputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class RemoveAutoScalingPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str

class RemoveAutoTerminationPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str

class RemoveManagedScalingPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str

class RemoveTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]

class SupportedProductConfigTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Args: Optional[Sequence[str]] = None

class SimpleScalingPolicyConfigurationTypeDef(BaseValidatorModel):
    ScalingAdjustment: int
    AdjustmentType: Optional[AdjustmentTypeType] = None
    CoolDown: Optional[int] = None

class SetKeepJobFlowAliveWhenNoStepsInputRequestTypeDef(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    KeepJobFlowAliveWhenNoSteps: bool

class SetTerminationProtectionInputRequestTypeDef(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    TerminationProtected: bool

class SetUnhealthyNodeReplacementInputRequestTypeDef(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    UnhealthyNodeReplacement: bool

class SetVisibleToAllUsersInputRequestTypeDef(BaseValidatorModel):
    JobFlowIds: Sequence[str]
    VisibleToAllUsers: bool

class StepExecutionStatusDetailTypeDef(BaseValidatorModel):
    State: StepExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None

class StepStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[Literal["NONE"]] = None
    Message: Optional[str] = None

class StepTimelineTypeDef(BaseValidatorModel):
    CreationDateTime: Optional[datetime] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class StopNotebookExecutionInputRequestTypeDef(BaseValidatorModel):
    NotebookExecutionId: str

class TerminateJobFlowsInputRequestTypeDef(BaseValidatorModel):
    JobFlowIds: Sequence[str]

class UpdateStudioInputRequestTypeDef(BaseValidatorModel):
    StudioId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DefaultS3Location: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None

class UpdateStudioSessionMappingInputRequestTypeDef(BaseValidatorModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class AddInstanceFleetOutputTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceFleetId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddInstanceGroupsOutputTypeDef(BaseValidatorModel):
    JobFlowId: str
    InstanceGroupIds: List[str]
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddJobFlowStepsOutputTypeDef(BaseValidatorModel):
    StepIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigurationOutputTypeDef(BaseValidatorModel):
    Name: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioOutputTypeDef(BaseValidatorModel):
    StudioId: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityConfigurationOutputTypeDef(BaseValidatorModel):
    Name: str
    SecurityConfiguration: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListReleaseLabelsOutputTypeDef(BaseValidatorModel):
    ReleaseLabels: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyClusterOutputTypeDef(BaseValidatorModel):
    StepConcurrencyLevel: int
    ResponseMetadata: ResponseMetadataTypeDef

class RunJobFlowOutputTypeDef(BaseValidatorModel):
    JobFlowId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartNotebookExecutionOutputTypeDef(BaseValidatorModel):
    NotebookExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateStudioInputRequestTypeDef(BaseValidatorModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    TrustedIdentityPropagationEnabled: Optional[bool] = None
    IdcUserAssignment: Optional[IdcUserAssignmentType] = None
    IdcInstanceArn: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None

class StudioTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None
    IdcInstanceArn: Optional[str] = None
    TrustedIdentityPropagationEnabled: Optional[bool] = None
    IdcUserAssignment: Optional[IdcUserAssignmentType] = None
    EncryptionKeyArn: Optional[str] = None

class AutoScalingPolicyStatusTypeDef(BaseValidatorModel):
    State: Optional[AutoScalingPolicyStateType] = None
    StateChangeReason: Optional[AutoScalingPolicyStateChangeReasonTypeDef] = None

class GetAutoTerminationPolicyOutputTypeDef(BaseValidatorModel):
    AutoTerminationPolicy: AutoTerminationPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAutoTerminationPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    AutoTerminationPolicy: Optional[AutoTerminationPolicyTypeDef] = None

class BlockPublicAccessConfigurationOutputTypeDef(BaseValidatorModel):
    BlockPublicSecurityGroupRules: bool
    PermittedPublicSecurityGroupRuleRanges: Optional[List[PortRangeTypeDef]] = None

class BlockPublicAccessConfigurationTypeDef(BaseValidatorModel):
    BlockPublicSecurityGroupRules: bool
    PermittedPublicSecurityGroupRuleRanges: Optional[Sequence[PortRangeTypeDef]] = None

class BootstrapActionConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigOutputTypeDef

class BootstrapActionConfigTypeDef(BaseValidatorModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigTypeDef

class CancelStepsOutputTypeDef(BaseValidatorModel):
    CancelStepsInfoList: List[CancelStepsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CloudWatchAlarmDefinitionOutputTypeDef(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    MetricName: str
    Period: int
    Threshold: float
    EvaluationPeriods: Optional[int] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None

class CloudWatchAlarmDefinitionTypeDef(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    MetricName: str
    Period: int
    Threshold: float
    EvaluationPeriods: Optional[int] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None

class ClusterStatusTypeDef(BaseValidatorModel):
    State: Optional[ClusterStateType] = None
    StateChangeReason: Optional[ClusterStateChangeReasonTypeDef] = None
    Timeline: Optional[ClusterTimelineTypeDef] = None
    ErrorDetails: Optional[List[ErrorDetailTypeDef]] = None

class ListBootstrapActionsOutputTypeDef(BaseValidatorModel):
    BootstrapActions: List[CommandTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedScalingPolicyTypeDef(BaseValidatorModel):
    ComputeLimits: Optional[ComputeLimitsTypeDef] = None

class CredentialsTypeDef(BaseValidatorModel):
    UsernamePassword: Optional[UsernamePasswordTypeDef] = None

class DescribeClusterInputClusterRunningWaitTypeDef(BaseValidatorModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterInputClusterTerminatedWaitTypeDef(BaseValidatorModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStepInputStepCompleteWaitTypeDef(BaseValidatorModel):
    ClusterId: str
    StepId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeJobFlowsInputRequestTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    JobFlowIds: Optional[Sequence[str]] = None
    JobFlowStates: Optional[Sequence[JobFlowExecutionStateType]] = None

class ListClustersInputRequestTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    ClusterStates: Optional[Sequence[ClusterStateType]] = None
    Marker: Optional[str] = None

class ListNotebookExecutionsInputRequestTypeDef(BaseValidatorModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[TimestampTypeDef] = None
    To: Optional[TimestampTypeDef] = None
    Marker: Optional[str] = None
    ExecutionEngineId: Optional[str] = None

class DescribeReleaseLabelOutputTypeDef(BaseValidatorModel):
    ReleaseLabel: str
    Applications: List[SimplifiedApplicationTypeDef]
    AvailableOSReleases: List[OSReleaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EbsBlockDeviceConfigTypeDef(BaseValidatorModel):
    VolumeSpecification: VolumeSpecificationTypeDef
    VolumesPerInstance: Optional[int] = None

class EbsBlockDeviceTypeDef(BaseValidatorModel):
    VolumeSpecification: Optional[VolumeSpecificationTypeDef] = None
    Device: Optional[str] = None

class GetStudioSessionMappingOutputTypeDef(BaseValidatorModel):
    SessionMapping: SessionMappingDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HadoopJarStepConfigOutputTypeDef(BaseValidatorModel):
    Jar: str
    Properties: Optional[List[KeyValueTypeDef]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None

class HadoopJarStepConfigTypeDef(BaseValidatorModel):
    Jar: str
    Properties: Optional[Sequence[KeyValueTypeDef]] = None
    MainClass: Optional[str] = None
    Args: Optional[Sequence[str]] = None

class InstanceFleetResizingSpecificationsTypeDef(BaseValidatorModel):
    SpotResizeSpecification: Optional[SpotResizingSpecificationTypeDef] = None
    OnDemandResizeSpecification: Optional[OnDemandResizingSpecificationTypeDef] = None

class InstanceFleetStatusTypeDef(BaseValidatorModel):
    State: Optional[InstanceFleetStateType] = None
    StateChangeReason: Optional[InstanceFleetStateChangeReasonTypeDef] = None
    Timeline: Optional[InstanceFleetTimelineTypeDef] = None

class InstanceGroupStatusTypeDef(BaseValidatorModel):
    State: Optional[InstanceGroupStateType] = None
    StateChangeReason: Optional[InstanceGroupStateChangeReasonTypeDef] = None
    Timeline: Optional[InstanceGroupTimelineTypeDef] = None

class ShrinkPolicyOutputTypeDef(BaseValidatorModel):
    DecommissionTimeout: Optional[int] = None
    InstanceResizePolicy: Optional[InstanceResizePolicyOutputTypeDef] = None

class ShrinkPolicyTypeDef(BaseValidatorModel):
    DecommissionTimeout: Optional[int] = None
    InstanceResizePolicy: Optional[InstanceResizePolicyTypeDef] = None

class InstanceStatusTypeDef(BaseValidatorModel):
    State: Optional[InstanceStateType] = None
    StateChangeReason: Optional[InstanceStateChangeReasonTypeDef] = None
    Timeline: Optional[InstanceTimelineTypeDef] = None

class JobFlowInstancesDetailTypeDef(BaseValidatorModel):
    MasterInstanceType: str
    SlaveInstanceType: str
    InstanceCount: int
    MasterPublicDnsName: Optional[str] = None
    MasterInstanceId: Optional[str] = None
    InstanceGroups: Optional[List[InstanceGroupDetailTypeDef]] = None
    NormalizedInstanceHours: Optional[int] = None
    Ec2KeyName: Optional[str] = None
    Ec2SubnetId: Optional[str] = None
    Placement: Optional[PlacementTypeOutputTypeDef] = None
    KeepJobFlowAliveWhenNoSteps: Optional[bool] = None
    TerminationProtected: Optional[bool] = None
    UnhealthyNodeReplacement: Optional[bool] = None
    HadoopVersion: Optional[str] = None

class ListBootstrapActionsInputListBootstrapActionsPaginateTypeDef(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersInputListClustersPaginateTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    ClusterStates: Optional[Sequence[ClusterStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceFleetsInputListInstanceFleetsPaginateTypeDef(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceGroupsInputListInstanceGroupsPaginateTypeDef(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesInputListInstancesPaginateTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[Sequence[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[Sequence[InstanceStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotebookExecutionsInputListNotebookExecutionsPaginateTypeDef(BaseValidatorModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[TimestampTypeDef] = None
    To: Optional[TimestampTypeDef] = None
    ExecutionEngineId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityConfigurationsInputListSecurityConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepsInputListStepsPaginateTypeDef(BaseValidatorModel):
    ClusterId: str
    StepStates: Optional[Sequence[StepStateType]] = None
    StepIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioSessionMappingsInputListStudioSessionMappingsPaginateTypeDef(BaseValidatorModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudiosInputListStudiosPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReleaseLabelsInputRequestTypeDef(BaseValidatorModel):
    Filters: Optional[ReleaseLabelFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSecurityConfigurationsOutputTypeDef(BaseValidatorModel):
    SecurityConfigurations: List[SecurityConfigurationSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudioSessionMappingsOutputTypeDef(BaseValidatorModel):
    SessionMappings: List[SessionMappingSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudiosOutputTypeDef(BaseValidatorModel):
    Studios: List[StudioSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSupportedInstanceTypesOutputTypeDef(BaseValidatorModel):
    SupportedInstanceTypes: List[SupportedInstanceTypeTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotebookExecutionSummaryTypeDef(BaseValidatorModel):
    NotebookExecutionId: Optional[str] = None
    EditorId: Optional[str] = None
    NotebookExecutionName: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    NotebookS3Location: Optional[NotebookS3LocationForOutputTypeDef] = None
    ExecutionEngineId: Optional[str] = None

class NotebookExecutionTypeDef(BaseValidatorModel):
    NotebookExecutionId: Optional[str] = None
    EditorId: Optional[str] = None
    ExecutionEngine: Optional[ExecutionEngineConfigTypeDef] = None
    NotebookExecutionName: Optional[str] = None
    NotebookParams: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Arn: Optional[str] = None
    OutputNotebookURI: Optional[str] = None
    LastStateChangeReason: Optional[str] = None
    NotebookInstanceSecurityGroupId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    NotebookS3Location: Optional[NotebookS3LocationForOutputTypeDef] = None
    OutputNotebookS3Location: Optional[OutputNotebookS3LocationForOutputTypeDef] = None
    OutputNotebookFormat: Optional[Literal["HTML"]] = None
    EnvironmentVariables: Optional[Dict[str, str]] = None

class OnDemandProvisioningSpecificationTypeDef(BaseValidatorModel):
    AllocationStrategy: OnDemandProvisioningAllocationStrategyType
    CapacityReservationOptions: Optional[OnDemandCapacityReservationOptionsTypeDef] = None

class StartNotebookExecutionInputRequestTypeDef(BaseValidatorModel):
    ExecutionEngine: ExecutionEngineConfigTypeDef
    ServiceRole: str
    EditorId: Optional[str] = None
    RelativePath: Optional[str] = None
    NotebookExecutionName: Optional[str] = None
    NotebookParams: Optional[str] = None
    NotebookInstanceSecurityGroupId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NotebookS3Location: Optional[NotebookS3LocationFromInputTypeDef] = None
    OutputNotebookS3Location: Optional[OutputNotebookS3LocationFromInputTypeDef] = None
    OutputNotebookFormat: Optional[Literal["HTML"]] = None
    EnvironmentVariables: Optional[Mapping[str, str]] = None

class ScalingActionTypeDef(BaseValidatorModel):
    SimpleScalingPolicyConfiguration: SimpleScalingPolicyConfigurationTypeDef
    Market: Optional[MarketTypeType] = None

class StepStatusTypeDef(BaseValidatorModel):
    State: Optional[StepStateType] = None
    StateChangeReason: Optional[StepStateChangeReasonTypeDef] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    Timeline: Optional[StepTimelineTypeDef] = None

class DescribeStudioOutputTypeDef(BaseValidatorModel):
    Studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlockPublicAccessConfigurationOutputTypeDef(BaseValidatorModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationOutputTypeDef
    BlockPublicAccessConfigurationMetadata: BlockPublicAccessConfigurationMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBlockPublicAccessConfigurationInputRequestTypeDef(BaseValidatorModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationTypeDef

class BootstrapActionDetailTypeDef(BaseValidatorModel):
    BootstrapActionConfig: Optional[BootstrapActionConfigOutputTypeDef] = None

class ScalingTriggerOutputTypeDef(BaseValidatorModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionOutputTypeDef

class ScalingTriggerTypeDef(BaseValidatorModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionTypeDef

class ClusterSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ClusterStatusTypeDef] = None
    NormalizedInstanceHours: Optional[int] = None
    ClusterArn: Optional[str] = None
    OutpostArn: Optional[str] = None

class ClusterTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ClusterStatusTypeDef] = None
    Ec2InstanceAttributes: Optional[Ec2InstanceAttributesTypeDef] = None
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
    Applications: Optional[List[ApplicationOutputTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    ServiceRole: Optional[str] = None
    NormalizedInstanceHours: Optional[int] = None
    MasterPublicDnsName: Optional[str] = None
    Configurations: Optional[List["ConfigurationOutputTypeDef"]] = None
    SecurityConfiguration: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None
    CustomAmiId: Optional[str] = None
    EbsRootVolumeSize: Optional[int] = None
    RepoUpgradeOnBoot: Optional[RepoUpgradeOnBootType] = None
    KerberosAttributes: Optional[KerberosAttributesTypeDef] = None
    ClusterArn: Optional[str] = None
    OutpostArn: Optional[str] = None
    StepConcurrencyLevel: Optional[int] = None
    PlacementGroups: Optional[List[PlacementGroupConfigTypeDef]] = None
    OSReleaseLabel: Optional[str] = None
    EbsRootVolumeIops: Optional[int] = None
    EbsRootVolumeThroughput: Optional[int] = None

class GetManagedScalingPolicyOutputTypeDef(BaseValidatorModel):
    ManagedScalingPolicy: ManagedScalingPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedScalingPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    ManagedScalingPolicy: ManagedScalingPolicyTypeDef

class GetClusterSessionCredentialsOutputTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    ExpiresAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EbsConfigurationTypeDef(BaseValidatorModel):
    EbsBlockDeviceConfigs: Optional[Sequence[EbsBlockDeviceConfigTypeDef]] = None
    EbsOptimized: Optional[bool] = None

class InstanceTypeSpecificationTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    Configurations: Optional[List["ConfigurationOutputTypeDef"]] = None
    EbsBlockDevices: Optional[List[EbsBlockDeviceTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None

class StepConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigOutputTypeDef
    ActionOnFailure: Optional[ActionOnFailureType] = None

class StepConfigTypeDef(BaseValidatorModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigTypeDef
    ActionOnFailure: Optional[ActionOnFailureType] = None

class InstanceFleetModifyConfigTypeDef(BaseValidatorModel):
    InstanceFleetId: str
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecificationsTypeDef] = None

class InstanceGroupModifyConfigTypeDef(BaseValidatorModel):
    InstanceGroupId: str
    InstanceCount: Optional[int] = None
    EC2InstanceIdsToTerminate: Optional[Sequence[str]] = None
    ShrinkPolicy: Optional[ShrinkPolicyTypeDef] = None
    ReconfigurationType: Optional[ReconfigurationTypeType] = None
    Configurations: Optional[Sequence["ConfigurationTypeDef"]] = None

class InstanceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Ec2InstanceId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIpAddress: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Status: Optional[InstanceStatusTypeDef] = None
    InstanceGroupId: Optional[str] = None
    InstanceFleetId: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    InstanceType: Optional[str] = None
    EbsVolumes: Optional[List[EbsVolumeTypeDef]] = None

class ListNotebookExecutionsOutputTypeDef(BaseValidatorModel):
    NotebookExecutions: List[NotebookExecutionSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotebookExecutionOutputTypeDef(BaseValidatorModel):
    NotebookExecution: NotebookExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceFleetProvisioningSpecificationsTypeDef(BaseValidatorModel):
    SpotSpecification: Optional[SpotProvisioningSpecificationTypeDef] = None
    OnDemandSpecification: Optional[OnDemandProvisioningSpecificationTypeDef] = None

class StepSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[HadoopStepConfigTypeDef] = None
    ActionOnFailure: Optional[ActionOnFailureType] = None
    Status: Optional[StepStatusTypeDef] = None

class StepTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[HadoopStepConfigTypeDef] = None
    ActionOnFailure: Optional[ActionOnFailureType] = None
    Status: Optional[StepStatusTypeDef] = None
    ExecutionRoleArn: Optional[str] = None

class ScalingRuleOutputTypeDef(BaseValidatorModel):
    Name: str
    Action: ScalingActionTypeDef
    Trigger: ScalingTriggerOutputTypeDef
    Description: Optional[str] = None

class ScalingRuleTypeDef(BaseValidatorModel):
    Name: str
    Action: ScalingActionTypeDef
    Trigger: ScalingTriggerTypeDef
    Description: Optional[str] = None

class ListClustersOutputTypeDef(BaseValidatorModel):
    Clusters: List[ClusterSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterOutputTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceTypeConfigTypeDef(BaseValidatorModel):
    InstanceType: str
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    EbsConfiguration: Optional[EbsConfigurationTypeDef] = None
    Configurations: Optional[Sequence["ConfigurationTypeDef"]] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None

class StepDetailTypeDef(BaseValidatorModel):
    StepConfig: StepConfigOutputTypeDef
    ExecutionStatusDetail: StepExecutionStatusDetailTypeDef

class ModifyInstanceFleetInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceFleet: InstanceFleetModifyConfigTypeDef

class ModifyInstanceGroupsInputRequestTypeDef(BaseValidatorModel):
    ClusterId: Optional[str] = None
    InstanceGroups: Optional[Sequence[InstanceGroupModifyConfigTypeDef]] = None

class ListInstancesOutputTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceFleetTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[InstanceFleetStatusTypeDef] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ProvisionedOnDemandCapacity: Optional[int] = None
    ProvisionedSpotCapacity: Optional[int] = None
    InstanceTypeSpecifications: Optional[List[InstanceTypeSpecificationTypeDef]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecificationsTypeDef] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecificationsTypeDef] = None

class ListStepsOutputTypeDef(BaseValidatorModel):
    Steps: List[StepSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStepOutputTypeDef(BaseValidatorModel):
    Step: StepTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AutoScalingPolicyDescriptionTypeDef(BaseValidatorModel):
    Status: Optional[AutoScalingPolicyStatusTypeDef] = None
    Constraints: Optional[ScalingConstraintsTypeDef] = None
    Rules: Optional[List[ScalingRuleOutputTypeDef]] = None

class AutoScalingPolicyTypeDef(BaseValidatorModel):
    Constraints: ScalingConstraintsTypeDef
    Rules: Sequence[ScalingRuleTypeDef]

class InstanceFleetConfigTypeDef(BaseValidatorModel):
    InstanceFleetType: InstanceFleetTypeType
    Name: Optional[str] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    InstanceTypeConfigs: Optional[Sequence[InstanceTypeConfigTypeDef]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecificationsTypeDef] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecificationsTypeDef] = None

class JobFlowDetailTypeDef(BaseValidatorModel):
    JobFlowId: str
    Name: str
    ExecutionStatusDetail: JobFlowExecutionStatusDetailTypeDef
    Instances: JobFlowInstancesDetailTypeDef
    LogUri: Optional[str] = None
    LogEncryptionKmsKeyId: Optional[str] = None
    AmiVersion: Optional[str] = None
    Steps: Optional[List[StepDetailTypeDef]] = None
    BootstrapActions: Optional[List[BootstrapActionDetailTypeDef]] = None
    SupportedProducts: Optional[List[str]] = None
    VisibleToAllUsers: Optional[bool] = None
    JobFlowRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None

class AddJobFlowStepsInputRequestTypeDef(BaseValidatorModel):
    JobFlowId: str
    Steps: Sequence[StepConfigUnionTypeDef]
    ExecutionRoleArn: Optional[str] = None

class ListInstanceFleetsOutputTypeDef(BaseValidatorModel):
    InstanceFleets: List[InstanceFleetTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceGroupTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    InstanceGroupType: Optional[InstanceGroupTypeType] = None
    BidPrice: Optional[str] = None
    InstanceType: Optional[str] = None
    RequestedInstanceCount: Optional[int] = None
    RunningInstanceCount: Optional[int] = None
    Status: Optional[InstanceGroupStatusTypeDef] = None
    Configurations: Optional[List["ConfigurationOutputTypeDef"]] = None
    ConfigurationsVersion: Optional[int] = None
    LastSuccessfullyAppliedConfigurations: Optional[List["ConfigurationOutputTypeDef"]] = None
    LastSuccessfullyAppliedConfigurationsVersion: Optional[int] = None
    EbsBlockDevices: Optional[List[EbsBlockDeviceTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    ShrinkPolicy: Optional[ShrinkPolicyOutputTypeDef] = None
    AutoScalingPolicy: Optional[AutoScalingPolicyDescriptionTypeDef] = None
    CustomAmiId: Optional[str] = None

class PutAutoScalingPolicyOutputTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicyDescriptionTypeDef
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceGroupConfigTypeDef(BaseValidatorModel):
    InstanceRole: InstanceRoleTypeType
    InstanceType: str
    InstanceCount: int
    Name: Optional[str] = None
    Market: Optional[MarketTypeType] = None
    BidPrice: Optional[str] = None
    Configurations: Optional[Sequence["ConfigurationTypeDef"]] = None
    EbsConfiguration: Optional[EbsConfigurationTypeDef] = None
    AutoScalingPolicy: Optional[AutoScalingPolicyTypeDef] = None
    CustomAmiId: Optional[str] = None

class PutAutoScalingPolicyInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicyTypeDef

class AddInstanceFleetInputRequestTypeDef(BaseValidatorModel):
    ClusterId: str
    InstanceFleet: InstanceFleetConfigTypeDef

class DescribeJobFlowsOutputTypeDef(BaseValidatorModel):
    JobFlows: List[JobFlowDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceGroupsOutputTypeDef(BaseValidatorModel):
    InstanceGroups: List[InstanceGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddInstanceGroupsInputRequestTypeDef(BaseValidatorModel):
    InstanceGroups: Sequence[InstanceGroupConfigTypeDef]
    JobFlowId: str

class JobFlowInstancesConfigTypeDef(BaseValidatorModel):
    MasterInstanceType: Optional[str] = None
    SlaveInstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceGroups: Optional[Sequence[InstanceGroupConfigTypeDef]] = None
    InstanceFleets: Optional[Sequence[InstanceFleetConfigTypeDef]] = None
    Ec2KeyName: Optional[str] = None
    Placement: Optional[PlacementTypeTypeDef] = None
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

class RunJobFlowInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Instances: JobFlowInstancesConfigTypeDef
    LogUri: Optional[str] = None
    LogEncryptionKmsKeyId: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    AmiVersion: Optional[str] = None
    ReleaseLabel: Optional[str] = None
    Steps: Optional[Sequence[StepConfigUnionTypeDef]] = None
    BootstrapActions: Optional[Sequence[BootstrapActionConfigUnionTypeDef]] = None
    SupportedProducts: Optional[Sequence[str]] = None
    NewSupportedProducts: Optional[Sequence[SupportedProductConfigTypeDef]] = None
    Applications: Optional[Sequence[ApplicationUnionTypeDef]] = None
    Configurations: Optional[Sequence[ConfigurationUnionTypeDef]] = None
    VisibleToAllUsers: Optional[bool] = None
    JobFlowRole: Optional[str] = None
    ServiceRole: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SecurityConfiguration: Optional[str] = None
    AutoScalingRole: Optional[str] = None
    ScaleDownBehavior: Optional[ScaleDownBehaviorType] = None
    CustomAmiId: Optional[str] = None
    EbsRootVolumeSize: Optional[int] = None
    RepoUpgradeOnBoot: Optional[RepoUpgradeOnBootType] = None
    KerberosAttributes: Optional[KerberosAttributesTypeDef] = None
    StepConcurrencyLevel: Optional[int] = None
    ManagedScalingPolicy: Optional[ManagedScalingPolicyTypeDef] = None
    PlacementGroupConfigs: Optional[Sequence[PlacementGroupConfigTypeDef]] = None
    AutoTerminationPolicy: Optional[AutoTerminationPolicyTypeDef] = None
    OSReleaseLabel: Optional[str] = None
    EbsRootVolumeIops: Optional[int] = None
    EbsRootVolumeThroughput: Optional[int] = None

