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
from aws_resource_validator.pydantic_models.emr_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ApplicationOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Args: Optional[List[str]] = None
    AdditionalInfo: Optional[Dict[str, str]] = None

class ApplicationTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Args: Optional[Sequence[str]] = None
    AdditionalInfo: Optional[Mapping[str, str]] = None

class ScalingConstraintsTypeDef(BaseModel):
    MinCapacity: int
    MaxCapacity: int

class AutoScalingPolicyStateChangeReasonTypeDef(BaseModel):
    Code: Optional[AutoScalingPolicyStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class AutoTerminationPolicyTypeDef(BaseModel):
    IdleTimeout: Optional[int] = None

class BlockPublicAccessConfigurationMetadataTypeDef(BaseModel):
    CreationDateTime: datetime
    CreatedByArn: str

class PortRangeTypeDef(BaseModel):
    MinRange: int
    MaxRange: Optional[int] = None

class ScriptBootstrapActionConfigOutputTypeDef(BaseModel):
    Path: str
    Args: Optional[List[str]] = None

class ScriptBootstrapActionConfigTypeDef(BaseModel):
    Path: str
    Args: Optional[Sequence[str]] = None

class CancelStepsInfoTypeDef(BaseModel):
    StepId: Optional[str] = None
    Status: Optional[CancelStepsRequestStatusType] = None
    Reason: Optional[str] = None

class CancelStepsInputRequestTypeDef(BaseModel):
    ClusterId: str
    StepIds: Sequence[str]
    StepCancellationOption: Optional[StepCancellationOptionType] = None

class MetricDimensionTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ClusterStateChangeReasonTypeDef(BaseModel):
    Code: Optional[ClusterStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class ClusterTimelineTypeDef(BaseModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class ErrorDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorData: Optional[List[Dict[str, str]]] = None
    ErrorMessage: Optional[str] = None

class Ec2InstanceAttributesTypeDef(BaseModel):
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

class KerberosAttributesTypeDef(BaseModel):
    Realm: str
    KdcAdminPassword: str
    CrossRealmTrustPrincipalPassword: Optional[str] = None
    ADDomainJoinUser: Optional[str] = None
    ADDomainJoinPassword: Optional[str] = None

class PlacementGroupConfigTypeDef(BaseModel):
    InstanceRole: InstanceRoleTypeType
    PlacementStrategy: Optional[PlacementGroupStrategyType] = None

class CommandTypeDef(BaseModel):
    Name: Optional[str] = None
    ScriptPath: Optional[str] = None
    Args: Optional[List[str]] = None

class ComputeLimitsTypeDef(BaseModel):
    UnitType: ComputeLimitsUnitTypeType
    MinimumCapacityUnits: int
    MaximumCapacityUnits: int
    MaximumOnDemandCapacityUnits: Optional[int] = None
    MaximumCoreCapacityUnits: Optional[int] = None

class ConfigurationExtraOutputTypeDef(BaseModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None

class ConfigurationOutputTypeDef(BaseModel):
    Classification: Optional[str] = None
    Configurations: Optional[List[Dict[str, Any]]] = None
    Properties: Optional[Dict[str, str]] = None

class ConfigurationTypeDef(BaseModel):
    Classification: Optional[str] = None
    Configurations: Optional[Sequence[Dict[str, Any]]] = None
    Properties: Optional[Mapping[str, str]] = None

class CreateSecurityConfigurationInputRequestTypeDef(BaseModel):
    Name: str
    SecurityConfiguration: str

class CreateStudioSessionMappingInputRequestTypeDef(BaseModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class UsernamePasswordTypeDef(BaseModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class DeleteSecurityConfigurationInputRequestTypeDef(BaseModel):
    Name: str

class DeleteStudioInputRequestTypeDef(BaseModel):
    StudioId: str

class DeleteStudioSessionMappingInputRequestTypeDef(BaseModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeClusterInputRequestTypeDef(BaseModel):
    ClusterId: str

class DescribeNotebookExecutionInputRequestTypeDef(BaseModel):
    NotebookExecutionId: str

class DescribeReleaseLabelInputRequestTypeDef(BaseModel):
    ReleaseLabel: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OSReleaseTypeDef(BaseModel):
    Label: Optional[str] = None

class SimplifiedApplicationTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class DescribeSecurityConfigurationInputRequestTypeDef(BaseModel):
    Name: str

class DescribeStepInputRequestTypeDef(BaseModel):
    ClusterId: str
    StepId: str

class DescribeStudioInputRequestTypeDef(BaseModel):
    StudioId: str

class VolumeSpecificationTypeDef(BaseModel):
    VolumeType: str
    SizeInGB: int
    Iops: Optional[int] = None
    Throughput: Optional[int] = None

class EbsVolumeTypeDef(BaseModel):
    Device: Optional[str] = None
    VolumeId: Optional[str] = None

class ExecutionEngineConfigTypeDef(BaseModel):
    Id: str
    Type: Optional[Literal["EMR"]] = None
    MasterInstanceSecurityGroupId: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None

class FailureDetailsTypeDef(BaseModel):
    Reason: Optional[str] = None
    Message: Optional[str] = None
    LogFile: Optional[str] = None

class GetAutoTerminationPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str

class GetClusterSessionCredentialsInputRequestTypeDef(BaseModel):
    ClusterId: str
    ExecutionRoleArn: Optional[str] = None

class GetManagedScalingPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str

class GetStudioSessionMappingInputRequestTypeDef(BaseModel):
    StudioId: str
    IdentityType: IdentityTypeType
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class SessionMappingDetailTypeDef(BaseModel):
    StudioId: Optional[str] = None
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    SessionPolicyArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class KeyValueTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class HadoopStepConfigTypeDef(BaseModel):
    Jar: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None

class SpotProvisioningSpecificationTypeDef(BaseModel):
    TimeoutDurationMinutes: int
    TimeoutAction: SpotProvisioningTimeoutActionType
    BlockDurationMinutes: Optional[int] = None
    AllocationStrategy: Optional[SpotProvisioningAllocationStrategyType] = None

class OnDemandResizingSpecificationTypeDef(BaseModel):
    TimeoutDurationMinutes: int

class SpotResizingSpecificationTypeDef(BaseModel):
    TimeoutDurationMinutes: int

class InstanceFleetStateChangeReasonTypeDef(BaseModel):
    Code: Optional[InstanceFleetStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class InstanceFleetTimelineTypeDef(BaseModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class InstanceGroupDetailTypeDef(BaseModel):
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

class InstanceGroupStateChangeReasonTypeDef(BaseModel):
    Code: Optional[InstanceGroupStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class InstanceGroupTimelineTypeDef(BaseModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class InstanceResizePolicyOutputTypeDef(BaseModel):
    InstancesToTerminate: Optional[List[str]] = None
    InstancesToProtect: Optional[List[str]] = None
    InstanceTerminationTimeout: Optional[int] = None

class InstanceResizePolicyTypeDef(BaseModel):
    InstancesToTerminate: Optional[Sequence[str]] = None
    InstancesToProtect: Optional[Sequence[str]] = None
    InstanceTerminationTimeout: Optional[int] = None

class InstanceStateChangeReasonTypeDef(BaseModel):
    Code: Optional[InstanceStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class InstanceTimelineTypeDef(BaseModel):
    CreationDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class JobFlowExecutionStatusDetailTypeDef(BaseModel):
    State: JobFlowExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    ReadyDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None

class PlacementTypeTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[Sequence[str]] = None

class PlacementTypeOutputTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBootstrapActionsInputRequestTypeDef(BaseModel):
    ClusterId: str
    Marker: Optional[str] = None

class ListInstanceFleetsInputRequestTypeDef(BaseModel):
    ClusterId: str
    Marker: Optional[str] = None

class ListInstanceGroupsInputRequestTypeDef(BaseModel):
    ClusterId: str
    Marker: Optional[str] = None

class ListInstancesInputRequestTypeDef(BaseModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[Sequence[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[Sequence[InstanceStateType]] = None
    Marker: Optional[str] = None

class ReleaseLabelFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Application: Optional[str] = None

class ListSecurityConfigurationsInputRequestTypeDef(BaseModel):
    Marker: Optional[str] = None

class SecurityConfigurationSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    CreationDateTime: Optional[datetime] = None

class ListStepsInputRequestTypeDef(BaseModel):
    ClusterId: str
    StepStates: Optional[Sequence[StepStateType]] = None
    StepIds: Optional[Sequence[str]] = None
    Marker: Optional[str] = None

class ListStudioSessionMappingsInputRequestTypeDef(BaseModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    Marker: Optional[str] = None

class SessionMappingSummaryTypeDef(BaseModel):
    StudioId: Optional[str] = None
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    SessionPolicyArn: Optional[str] = None
    CreationTime: Optional[datetime] = None

class ListStudiosInputRequestTypeDef(BaseModel):
    Marker: Optional[str] = None

class StudioSummaryTypeDef(BaseModel):
    StudioId: Optional[str] = None
    Name: Optional[str] = None
    VpcId: Optional[str] = None
    Description: Optional[str] = None
    Url: Optional[str] = None
    AuthMode: Optional[AuthModeType] = None
    CreationTime: Optional[datetime] = None

class ListSupportedInstanceTypesInputRequestTypeDef(BaseModel):
    ReleaseLabel: str
    Marker: Optional[str] = None

class SupportedInstanceTypeTypeDef(BaseModel):
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

class ModifyClusterInputRequestTypeDef(BaseModel):
    ClusterId: str
    StepConcurrencyLevel: Optional[int] = None

class NotebookS3LocationForOutputTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class OutputNotebookS3LocationForOutputTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class NotebookS3LocationFromInputTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class OnDemandCapacityReservationOptionsTypeDef(BaseModel):
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None
    CapacityReservationPreference: Optional[OnDemandCapacityReservationPreferenceType] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class OutputNotebookS3LocationFromInputTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class RemoveAutoScalingPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str
    InstanceGroupId: str

class RemoveAutoTerminationPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str

class RemoveManagedScalingPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str

class RemoveTagsInputRequestTypeDef(BaseModel):
    ResourceId: str
    TagKeys: Sequence[str]

class SupportedProductConfigTypeDef(BaseModel):
    Name: Optional[str] = None
    Args: Optional[Sequence[str]] = None

class SimpleScalingPolicyConfigurationTypeDef(BaseModel):
    ScalingAdjustment: int
    AdjustmentType: Optional[AdjustmentTypeType] = None
    CoolDown: Optional[int] = None

class SetKeepJobFlowAliveWhenNoStepsInputRequestTypeDef(BaseModel):
    JobFlowIds: Sequence[str]
    KeepJobFlowAliveWhenNoSteps: bool

class SetTerminationProtectionInputRequestTypeDef(BaseModel):
    JobFlowIds: Sequence[str]
    TerminationProtected: bool

class SetUnhealthyNodeReplacementInputRequestTypeDef(BaseModel):
    JobFlowIds: Sequence[str]
    UnhealthyNodeReplacement: bool

class SetVisibleToAllUsersInputRequestTypeDef(BaseModel):
    JobFlowIds: Sequence[str]
    VisibleToAllUsers: bool

class StepExecutionStatusDetailTypeDef(BaseModel):
    State: StepExecutionStateType
    CreationDateTime: datetime
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    LastStateChangeReason: Optional[str] = None

class StepStateChangeReasonTypeDef(BaseModel):
    Code: Optional[Literal["NONE"]] = None
    Message: Optional[str] = None

class StepTimelineTypeDef(BaseModel):
    CreationDateTime: Optional[datetime] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class StopNotebookExecutionInputRequestTypeDef(BaseModel):
    NotebookExecutionId: str

class TerminateJobFlowsInputRequestTypeDef(BaseModel):
    JobFlowIds: Sequence[str]

class UpdateStudioInputRequestTypeDef(BaseModel):
    StudioId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DefaultS3Location: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None

class UpdateStudioSessionMappingInputRequestTypeDef(BaseModel):
    StudioId: str
    IdentityType: IdentityTypeType
    SessionPolicyArn: str
    IdentityId: Optional[str] = None
    IdentityName: Optional[str] = None

class AddInstanceFleetOutputTypeDef(BaseModel):
    ClusterId: str
    InstanceFleetId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddInstanceGroupsOutputTypeDef(BaseModel):
    JobFlowId: str
    InstanceGroupIds: List[str]
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddJobFlowStepsOutputTypeDef(BaseModel):
    StepIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigurationOutputTypeDef(BaseModel):
    Name: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioOutputTypeDef(BaseModel):
    StudioId: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityConfigurationOutputTypeDef(BaseModel):
    Name: str
    SecurityConfiguration: str
    CreationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListReleaseLabelsOutputTypeDef(BaseModel):
    ReleaseLabels: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyClusterOutputTypeDef(BaseModel):
    StepConcurrencyLevel: int
    ResponseMetadata: ResponseMetadataTypeDef

class RunJobFlowOutputTypeDef(BaseModel):
    JobFlowId: str
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartNotebookExecutionOutputTypeDef(BaseModel):
    NotebookExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateStudioInputRequestTypeDef(BaseModel):
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

class StudioTypeDef(BaseModel):
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

class AutoScalingPolicyStatusTypeDef(BaseModel):
    State: Optional[AutoScalingPolicyStateType] = None
    StateChangeReason: Optional[AutoScalingPolicyStateChangeReasonTypeDef] = None

class GetAutoTerminationPolicyOutputTypeDef(BaseModel):
    AutoTerminationPolicy: AutoTerminationPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAutoTerminationPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str
    AutoTerminationPolicy: Optional[AutoTerminationPolicyTypeDef] = None

class BlockPublicAccessConfigurationOutputTypeDef(BaseModel):
    BlockPublicSecurityGroupRules: bool
    PermittedPublicSecurityGroupRuleRanges: Optional[List[PortRangeTypeDef]] = None

class BlockPublicAccessConfigurationTypeDef(BaseModel):
    BlockPublicSecurityGroupRules: bool
    PermittedPublicSecurityGroupRuleRanges: Optional[Sequence[PortRangeTypeDef]] = None

class BootstrapActionConfigOutputTypeDef(BaseModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigOutputTypeDef

class BootstrapActionConfigTypeDef(BaseModel):
    Name: str
    ScriptBootstrapAction: ScriptBootstrapActionConfigTypeDef

class CancelStepsOutputTypeDef(BaseModel):
    CancelStepsInfoList: List[CancelStepsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CloudWatchAlarmDefinitionOutputTypeDef(BaseModel):
    ComparisonOperator: ComparisonOperatorType
    MetricName: str
    Period: int
    Threshold: float
    EvaluationPeriods: Optional[int] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None

class CloudWatchAlarmDefinitionTypeDef(BaseModel):
    ComparisonOperator: ComparisonOperatorType
    MetricName: str
    Period: int
    Threshold: float
    EvaluationPeriods: Optional[int] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None

class ClusterStatusTypeDef(BaseModel):
    State: Optional[ClusterStateType] = None
    StateChangeReason: Optional[ClusterStateChangeReasonTypeDef] = None
    Timeline: Optional[ClusterTimelineTypeDef] = None
    ErrorDetails: Optional[List[ErrorDetailTypeDef]] = None

class ListBootstrapActionsOutputTypeDef(BaseModel):
    BootstrapActions: List[CommandTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedScalingPolicyTypeDef(BaseModel):
    ComputeLimits: Optional[ComputeLimitsTypeDef] = None

class CredentialsTypeDef(BaseModel):
    UsernamePassword: Optional[UsernamePasswordTypeDef] = None

class DescribeClusterInputClusterRunningWaitTypeDef(BaseModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterInputClusterTerminatedWaitTypeDef(BaseModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStepInputStepCompleteWaitTypeDef(BaseModel):
    ClusterId: str
    StepId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeJobFlowsInputRequestTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    JobFlowIds: Optional[Sequence[str]] = None
    JobFlowStates: Optional[Sequence[JobFlowExecutionStateType]] = None

class ListClustersInputRequestTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    ClusterStates: Optional[Sequence[ClusterStateType]] = None
    Marker: Optional[str] = None

class ListNotebookExecutionsInputRequestTypeDef(BaseModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[TimestampTypeDef] = None
    To: Optional[TimestampTypeDef] = None
    Marker: Optional[str] = None
    ExecutionEngineId: Optional[str] = None

class DescribeReleaseLabelOutputTypeDef(BaseModel):
    ReleaseLabel: str
    Applications: List[SimplifiedApplicationTypeDef]
    AvailableOSReleases: List[OSReleaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EbsBlockDeviceConfigTypeDef(BaseModel):
    VolumeSpecification: VolumeSpecificationTypeDef
    VolumesPerInstance: Optional[int] = None

class EbsBlockDeviceTypeDef(BaseModel):
    VolumeSpecification: Optional[VolumeSpecificationTypeDef] = None
    Device: Optional[str] = None

class GetStudioSessionMappingOutputTypeDef(BaseModel):
    SessionMapping: SessionMappingDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HadoopJarStepConfigOutputTypeDef(BaseModel):
    Jar: str
    Properties: Optional[List[KeyValueTypeDef]] = None
    MainClass: Optional[str] = None
    Args: Optional[List[str]] = None

class HadoopJarStepConfigTypeDef(BaseModel):
    Jar: str
    Properties: Optional[Sequence[KeyValueTypeDef]] = None
    MainClass: Optional[str] = None
    Args: Optional[Sequence[str]] = None

class InstanceFleetResizingSpecificationsTypeDef(BaseModel):
    SpotResizeSpecification: Optional[SpotResizingSpecificationTypeDef] = None
    OnDemandResizeSpecification: Optional[OnDemandResizingSpecificationTypeDef] = None

class InstanceFleetStatusTypeDef(BaseModel):
    State: Optional[InstanceFleetStateType] = None
    StateChangeReason: Optional[InstanceFleetStateChangeReasonTypeDef] = None
    Timeline: Optional[InstanceFleetTimelineTypeDef] = None

class InstanceGroupStatusTypeDef(BaseModel):
    State: Optional[InstanceGroupStateType] = None
    StateChangeReason: Optional[InstanceGroupStateChangeReasonTypeDef] = None
    Timeline: Optional[InstanceGroupTimelineTypeDef] = None

class ShrinkPolicyOutputTypeDef(BaseModel):
    DecommissionTimeout: Optional[int] = None
    InstanceResizePolicy: Optional[InstanceResizePolicyOutputTypeDef] = None

class ShrinkPolicyTypeDef(BaseModel):
    DecommissionTimeout: Optional[int] = None
    InstanceResizePolicy: Optional[InstanceResizePolicyTypeDef] = None

class InstanceStatusTypeDef(BaseModel):
    State: Optional[InstanceStateType] = None
    StateChangeReason: Optional[InstanceStateChangeReasonTypeDef] = None
    Timeline: Optional[InstanceTimelineTypeDef] = None

class JobFlowInstancesDetailTypeDef(BaseModel):
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

class ListBootstrapActionsInputListBootstrapActionsPaginateTypeDef(BaseModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersInputListClustersPaginateTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    ClusterStates: Optional[Sequence[ClusterStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceFleetsInputListInstanceFleetsPaginateTypeDef(BaseModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceGroupsInputListInstanceGroupsPaginateTypeDef(BaseModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesInputListInstancesPaginateTypeDef(BaseModel):
    ClusterId: str
    InstanceGroupId: Optional[str] = None
    InstanceGroupTypes: Optional[Sequence[InstanceGroupTypeType]] = None
    InstanceFleetId: Optional[str] = None
    InstanceFleetType: Optional[InstanceFleetTypeType] = None
    InstanceStates: Optional[Sequence[InstanceStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotebookExecutionsInputListNotebookExecutionsPaginateTypeDef(BaseModel):
    EditorId: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    From: Optional[TimestampTypeDef] = None
    To: Optional[TimestampTypeDef] = None
    ExecutionEngineId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityConfigurationsInputListSecurityConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepsInputListStepsPaginateTypeDef(BaseModel):
    ClusterId: str
    StepStates: Optional[Sequence[StepStateType]] = None
    StepIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioSessionMappingsInputListStudioSessionMappingsPaginateTypeDef(BaseModel):
    StudioId: Optional[str] = None
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudiosInputListStudiosPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReleaseLabelsInputRequestTypeDef(BaseModel):
    Filters: Optional[ReleaseLabelFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSecurityConfigurationsOutputTypeDef(BaseModel):
    SecurityConfigurations: List[SecurityConfigurationSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudioSessionMappingsOutputTypeDef(BaseModel):
    SessionMappings: List[SessionMappingSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudiosOutputTypeDef(BaseModel):
    Studios: List[StudioSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSupportedInstanceTypesOutputTypeDef(BaseModel):
    SupportedInstanceTypes: List[SupportedInstanceTypeTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotebookExecutionSummaryTypeDef(BaseModel):
    NotebookExecutionId: Optional[str] = None
    EditorId: Optional[str] = None
    NotebookExecutionName: Optional[str] = None
    Status: Optional[NotebookExecutionStatusType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    NotebookS3Location: Optional[NotebookS3LocationForOutputTypeDef] = None
    ExecutionEngineId: Optional[str] = None

class NotebookExecutionTypeDef(BaseModel):
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

class OnDemandProvisioningSpecificationTypeDef(BaseModel):
    AllocationStrategy: OnDemandProvisioningAllocationStrategyType
    CapacityReservationOptions: Optional[OnDemandCapacityReservationOptionsTypeDef] = None

class StartNotebookExecutionInputRequestTypeDef(BaseModel):
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

class ScalingActionTypeDef(BaseModel):
    SimpleScalingPolicyConfiguration: SimpleScalingPolicyConfigurationTypeDef
    Market: Optional[MarketTypeType] = None

class StepStatusTypeDef(BaseModel):
    State: Optional[StepStateType] = None
    StateChangeReason: Optional[StepStateChangeReasonTypeDef] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    Timeline: Optional[StepTimelineTypeDef] = None

class DescribeStudioOutputTypeDef(BaseModel):
    Studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlockPublicAccessConfigurationOutputTypeDef(BaseModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationOutputTypeDef
    BlockPublicAccessConfigurationMetadata: BlockPublicAccessConfigurationMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBlockPublicAccessConfigurationInputRequestTypeDef(BaseModel):
    BlockPublicAccessConfiguration: BlockPublicAccessConfigurationTypeDef

class BootstrapActionDetailTypeDef(BaseModel):
    BootstrapActionConfig: Optional[BootstrapActionConfigOutputTypeDef] = None

class ScalingTriggerOutputTypeDef(BaseModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionOutputTypeDef

class ScalingTriggerTypeDef(BaseModel):
    CloudWatchAlarmDefinition: CloudWatchAlarmDefinitionTypeDef

class ClusterSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ClusterStatusTypeDef] = None
    NormalizedInstanceHours: Optional[int] = None
    ClusterArn: Optional[str] = None
    OutpostArn: Optional[str] = None

class ClusterTypeDef(BaseModel):
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

class GetManagedScalingPolicyOutputTypeDef(BaseModel):
    ManagedScalingPolicy: ManagedScalingPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedScalingPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str
    ManagedScalingPolicy: ManagedScalingPolicyTypeDef

class GetClusterSessionCredentialsOutputTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    ExpiresAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EbsConfigurationTypeDef(BaseModel):
    EbsBlockDeviceConfigs: Optional[Sequence[EbsBlockDeviceConfigTypeDef]] = None
    EbsOptimized: Optional[bool] = None

class InstanceTypeSpecificationTypeDef(BaseModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    Configurations: Optional[List["ConfigurationOutputTypeDef"]] = None
    EbsBlockDevices: Optional[List[EbsBlockDeviceTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None

class StepConfigOutputTypeDef(BaseModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigOutputTypeDef
    ActionOnFailure: Optional[ActionOnFailureType] = None

class StepConfigTypeDef(BaseModel):
    Name: str
    HadoopJarStep: HadoopJarStepConfigTypeDef
    ActionOnFailure: Optional[ActionOnFailureType] = None

class InstanceFleetModifyConfigTypeDef(BaseModel):
    InstanceFleetId: str
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecificationsTypeDef] = None

class InstanceGroupModifyConfigTypeDef(BaseModel):
    InstanceGroupId: str
    InstanceCount: Optional[int] = None
    EC2InstanceIdsToTerminate: Optional[Sequence[str]] = None
    ShrinkPolicy: Optional[ShrinkPolicyTypeDef] = None
    ReconfigurationType: Optional[ReconfigurationTypeType] = None
    Configurations: Optional[Sequence["ConfigurationTypeDef"]] = None

class InstanceTypeDef(BaseModel):
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

class ListNotebookExecutionsOutputTypeDef(BaseModel):
    NotebookExecutions: List[NotebookExecutionSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotebookExecutionOutputTypeDef(BaseModel):
    NotebookExecution: NotebookExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceFleetProvisioningSpecificationsTypeDef(BaseModel):
    SpotSpecification: Optional[SpotProvisioningSpecificationTypeDef] = None
    OnDemandSpecification: Optional[OnDemandProvisioningSpecificationTypeDef] = None

class StepSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[HadoopStepConfigTypeDef] = None
    ActionOnFailure: Optional[ActionOnFailureType] = None
    Status: Optional[StepStatusTypeDef] = None

class StepTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[HadoopStepConfigTypeDef] = None
    ActionOnFailure: Optional[ActionOnFailureType] = None
    Status: Optional[StepStatusTypeDef] = None
    ExecutionRoleArn: Optional[str] = None

class ScalingRuleOutputTypeDef(BaseModel):
    Name: str
    Action: ScalingActionTypeDef
    Trigger: ScalingTriggerOutputTypeDef
    Description: Optional[str] = None

class ScalingRuleTypeDef(BaseModel):
    Name: str
    Action: ScalingActionTypeDef
    Trigger: ScalingTriggerTypeDef
    Description: Optional[str] = None

class ListClustersOutputTypeDef(BaseModel):
    Clusters: List[ClusterSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterOutputTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceTypeConfigTypeDef(BaseModel):
    InstanceType: str
    WeightedCapacity: Optional[int] = None
    BidPrice: Optional[str] = None
    BidPriceAsPercentageOfOnDemandPrice: Optional[float] = None
    EbsConfiguration: Optional[EbsConfigurationTypeDef] = None
    Configurations: Optional[Sequence["ConfigurationTypeDef"]] = None
    CustomAmiId: Optional[str] = None
    Priority: Optional[float] = None

class StepDetailTypeDef(BaseModel):
    StepConfig: StepConfigOutputTypeDef
    ExecutionStatusDetail: StepExecutionStatusDetailTypeDef

class ModifyInstanceFleetInputRequestTypeDef(BaseModel):
    ClusterId: str
    InstanceFleet: InstanceFleetModifyConfigTypeDef

class ModifyInstanceGroupsInputRequestTypeDef(BaseModel):
    ClusterId: Optional[str] = None
    InstanceGroups: Optional[Sequence[InstanceGroupModifyConfigTypeDef]] = None

class ListInstancesOutputTypeDef(BaseModel):
    Instances: List[InstanceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceFleetTypeDef(BaseModel):
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

class ListStepsOutputTypeDef(BaseModel):
    Steps: List[StepSummaryTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStepOutputTypeDef(BaseModel):
    Step: StepTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AutoScalingPolicyDescriptionTypeDef(BaseModel):
    Status: Optional[AutoScalingPolicyStatusTypeDef] = None
    Constraints: Optional[ScalingConstraintsTypeDef] = None
    Rules: Optional[List[ScalingRuleOutputTypeDef]] = None

class AutoScalingPolicyTypeDef(BaseModel):
    Constraints: ScalingConstraintsTypeDef
    Rules: Sequence[ScalingRuleTypeDef]

class InstanceFleetConfigTypeDef(BaseModel):
    InstanceFleetType: InstanceFleetTypeType
    Name: Optional[str] = None
    TargetOnDemandCapacity: Optional[int] = None
    TargetSpotCapacity: Optional[int] = None
    InstanceTypeConfigs: Optional[Sequence[InstanceTypeConfigTypeDef]] = None
    LaunchSpecifications: Optional[InstanceFleetProvisioningSpecificationsTypeDef] = None
    ResizeSpecifications: Optional[InstanceFleetResizingSpecificationsTypeDef] = None

class JobFlowDetailTypeDef(BaseModel):
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

class AddJobFlowStepsInputRequestTypeDef(BaseModel):
    JobFlowId: str
    Steps: Sequence[StepConfigUnionTypeDef]
    ExecutionRoleArn: Optional[str] = None

class ListInstanceFleetsOutputTypeDef(BaseModel):
    InstanceFleets: List[InstanceFleetTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceGroupTypeDef(BaseModel):
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

class PutAutoScalingPolicyOutputTypeDef(BaseModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicyDescriptionTypeDef
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceGroupConfigTypeDef(BaseModel):
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

class PutAutoScalingPolicyInputRequestTypeDef(BaseModel):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: AutoScalingPolicyTypeDef

class AddInstanceFleetInputRequestTypeDef(BaseModel):
    ClusterId: str
    InstanceFleet: InstanceFleetConfigTypeDef

class DescribeJobFlowsOutputTypeDef(BaseModel):
    JobFlows: List[JobFlowDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceGroupsOutputTypeDef(BaseModel):
    InstanceGroups: List[InstanceGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddInstanceGroupsInputRequestTypeDef(BaseModel):
    InstanceGroups: Sequence[InstanceGroupConfigTypeDef]
    JobFlowId: str

class JobFlowInstancesConfigTypeDef(BaseModel):
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

class RunJobFlowInputRequestTypeDef(BaseModel):
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

