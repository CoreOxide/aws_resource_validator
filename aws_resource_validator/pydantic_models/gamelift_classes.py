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
from aws_resource_validator.pydantic_models.gamelift_constants import *

class AcceptMatchInput(BaseValidatorModel):
    TicketId: str
    PlayerIds: Sequence[str]
    AcceptanceType: AcceptanceTypeType


class AnywhereConfiguration(BaseValidatorModel):
    Cost: str


class AttributeValueOutput(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[float] = None
    SL: Optional[List[str]] = None
    SDM: Optional[Dict[str, float]] = None


class AttributeValue(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[float] = None
    SL: Optional[Sequence[str]] = None
    SDM: Optional[Mapping[str, float]] = None


class AwsCredentials(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None


class Build(BaseValidatorModel):
    BuildId: Optional[str] = None
    BuildArn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[BuildStatusType] = None
    SizeOnDisk: Optional[int] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    CreationTime: Optional[datetime] = None
    ServerSdkVersion: Optional[str] = None


class CertificateConfiguration(BaseValidatorModel):
    CertificateType: CertificateTypeType


class ClaimFilterOption(BaseValidatorModel):
    InstanceStatuses: Optional[Sequence[FilterInstanceStatusType]] = None


class GameServer(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    GameServerId: Optional[str] = None
    InstanceId: Optional[str] = None
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None
    ClaimStatus: Optional[Literal["CLAIMED"]] = None
    UtilizationStatus: Optional[GameServerUtilizationStatusType] = None
    RegistrationTime: Optional[datetime] = None
    LastClaimTime: Optional[datetime] = None
    LastHealthCheckTime: Optional[datetime] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ContainerAttribute(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerRuntimeId: Optional[str] = None


class ConnectionPortRange(BaseValidatorModel):
    FromPort: int
    ToPort: int


class ContainerDependency(BaseValidatorModel):
    ContainerName: str
    Condition: ContainerDependencyConditionType


class ContainerEnvironment(BaseValidatorModel):
    Name: str
    Value: str


class ContainerFleetLocationAttributes(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ContainerFleetLocationStatusType] = None


class DeploymentDetails(BaseValidatorModel):
    LatestDeploymentId: Optional[str] = None


class GameSessionCreationLimitPolicy(BaseValidatorModel):
    NewGameSessionsPerCreator: Optional[int] = None
    PolicyPeriodInMinutes: Optional[int] = None


class LogConfiguration(BaseValidatorModel):
    LogDestination: Optional[LogDestinationType] = None
    S3BucketName: Optional[str] = None
    LogGroupArn: Optional[str] = None


class ContainerHealthCheckOutput(BaseValidatorModel):
    Command: List[str]
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class ContainerHealthCheck(BaseValidatorModel):
    Command: Sequence[str]
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class ContainerIdentifier(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerRuntimeId: Optional[str] = None


class ContainerMountPoint(BaseValidatorModel):
    InstancePath: str
    ContainerPath: Optional[str] = None
    AccessLevel: Optional[ContainerMountPointAccessLevelType] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class S3Location(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    RoleArn: Optional[str] = None
    ObjectVersion: Optional[str] = None


class LocationConfiguration(BaseValidatorModel):
    Location: str


class ResourceCreationLimitPolicy(BaseValidatorModel):
    NewGameSessionsPerCreator: Optional[int] = None
    PolicyPeriodInMinutes: Optional[int] = None


class LocationState(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[FleetStatusType] = None


class InstanceDefinition(BaseValidatorModel):
    InstanceType: GameServerGroupInstanceTypeType
    WeightedCapacity: Optional[str] = None


class LaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class GameProperty(BaseValidatorModel):
    Key: str
    Value: str


class GameSessionQueueDestination(BaseValidatorModel):
    DestinationArn: Optional[str] = None


class PlayerLatencyPolicy(BaseValidatorModel):
    MaximumIndividualPlayerLatencyMilliseconds: Optional[int] = None
    PolicyDurationSeconds: Optional[int] = None


class LocationModel(BaseValidatorModel):
    LocationName: Optional[str] = None
    LocationArn: Optional[str] = None


class MatchmakingRuleSet(BaseValidatorModel):
    RuleSetBody: str
    RuleSetName: Optional[str] = None
    RuleSetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None


class CreatePlayerSessionInput(BaseValidatorModel):
    GameSessionId: str
    PlayerId: str
    PlayerData: Optional[str] = None


class PlayerSession(BaseValidatorModel):
    PlayerSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    GameSessionId: Optional[str] = None
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    TerminationTime: Optional[datetime] = None
    Status: Optional[PlayerSessionStatusType] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    PlayerData: Optional[str] = None


class CreatePlayerSessionsInput(BaseValidatorModel):
    GameSessionId: str
    PlayerIds: Sequence[str]
    PlayerDataMap: Optional[Mapping[str, str]] = None


class CreateVpcPeeringAuthorizationInput(BaseValidatorModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str


class VpcPeeringAuthorization(BaseValidatorModel):
    GameLiftAwsAccountId: Optional[str] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None


class CreateVpcPeeringConnectionInput(BaseValidatorModel):
    FleetId: str
    PeerVpcAwsAccountId: str
    PeerVpcId: str


class DeleteAliasInput(BaseValidatorModel):
    AliasId: str


class DeleteBuildInput(BaseValidatorModel):
    BuildId: str


class DeleteContainerFleetInput(BaseValidatorModel):
    FleetId: str


class DeleteContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    VersionNumber: Optional[int] = None
    VersionCountToRetain: Optional[int] = None


class DeleteFleetInput(BaseValidatorModel):
    FleetId: str


class DeleteFleetLocationsInput(BaseValidatorModel):
    FleetId: str
    Locations: Sequence[str]


class DeleteGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    DeleteOption: Optional[GameServerGroupDeleteOptionType] = None


class DeleteGameSessionQueueInput(BaseValidatorModel):
    Name: str


class DeleteLocationInput(BaseValidatorModel):
    LocationName: str


class DeleteMatchmakingConfigurationInput(BaseValidatorModel):
    Name: str


class DeleteMatchmakingRuleSetInput(BaseValidatorModel):
    Name: str


class DeleteScalingPolicyInput(BaseValidatorModel):
    Name: str
    FleetId: str


class DeleteScriptInput(BaseValidatorModel):
    ScriptId: str


class DeleteVpcPeeringAuthorizationInput(BaseValidatorModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str


class DeleteVpcPeeringConnectionInput(BaseValidatorModel):
    FleetId: str
    VpcPeeringConnectionId: str


class DeploymentConfiguration(BaseValidatorModel):
    ProtectionStrategy: Optional[DeploymentProtectionStrategyType] = None
    MinimumHealthyPercentage: Optional[int] = None
    ImpairmentStrategy: Optional[DeploymentImpairmentStrategyType] = None


class DeregisterComputeInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class DeregisterGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str


class DescribeAliasInput(BaseValidatorModel):
    AliasId: str


class DescribeBuildInput(BaseValidatorModel):
    BuildId: str


class DescribeComputeInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class DescribeContainerFleetInput(BaseValidatorModel):
    FleetId: str


class DescribeContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    VersionNumber: Optional[int] = None


class DescribeEC2InstanceLimitsInput(BaseValidatorModel):
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    Location: Optional[str] = None


class EC2InstanceLimit(BaseValidatorModel):
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    CurrentInstances: Optional[int] = None
    InstanceLimit: Optional[int] = None
    Location: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeFleetAttributesInput(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetCapacityInput(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetDeploymentInput(BaseValidatorModel):
    FleetId: str
    DeploymentId: Optional[str] = None


class LocationalDeployment(BaseValidatorModel):
    DeploymentStatus: Optional[DeploymentStatusType] = None


class Event(BaseValidatorModel):
    EventId: Optional[str] = None
    ResourceId: Optional[str] = None
    EventCode: Optional[EventCodeType] = None
    Message: Optional[str] = None
    EventTime: Optional[datetime] = None
    PreSignedLogUrl: Optional[str] = None
    Count: Optional[int] = None


class DescribeFleetLocationAttributesInput(BaseValidatorModel):
    FleetId: str
    Locations: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetLocationCapacityInput(BaseValidatorModel):
    FleetId: str
    Location: str


class DescribeFleetLocationUtilizationInput(BaseValidatorModel):
    FleetId: str
    Location: str


class FleetUtilization(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    ActiveServerProcessCount: Optional[int] = None
    ActiveGameSessionCount: Optional[int] = None
    CurrentPlayerSessionCount: Optional[int] = None
    MaximumPlayerSessionCount: Optional[int] = None
    Location: Optional[str] = None


class DescribeFleetPortSettingsInput(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None


class DescribeFleetUtilizationInput(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str


class DescribeGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str


class DescribeGameServerInstancesInput(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GameServerInstance(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[GameServerInstanceStatusType] = None


class DescribeGameSessionDetailsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeGameSessionPlacementInput(BaseValidatorModel):
    PlacementId: str


class DescribeGameSessionQueuesInput(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeGameSessionsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstancesInput(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None


class DescribeMatchmakingConfigurationsInput(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMatchmakingInput(BaseValidatorModel):
    TicketIds: Sequence[str]


class DescribeMatchmakingRuleSetsInput(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePlayerSessionsInput(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeRuntimeConfigurationInput(BaseValidatorModel):
    FleetId: str


class DescribeScalingPoliciesInput(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None


class DescribeScriptInput(BaseValidatorModel):
    ScriptId: str


class DescribeVpcPeeringConnectionsInput(BaseValidatorModel):
    FleetId: Optional[str] = None


class DesiredPlayerSession(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerData: Optional[str] = None


class EC2InstanceCounts(BaseValidatorModel):
    DESIRED: Optional[int] = None
    MINIMUM: Optional[int] = None
    MAXIMUM: Optional[int] = None
    PENDING: Optional[int] = None
    ACTIVE: Optional[int] = None
    IDLE: Optional[int] = None
    TERMINATING: Optional[int] = None


class FilterConfigurationOutput(BaseValidatorModel):
    AllowedLocations: Optional[List[str]] = None


class FilterConfiguration(BaseValidatorModel):
    AllowedLocations: Optional[Sequence[str]] = None


class GameServerContainerGroupCounts(BaseValidatorModel):
    PENDING: Optional[int] = None
    ACTIVE: Optional[int] = None
    IDLE: Optional[int] = None
    TERMINATING: Optional[int] = None


class TargetTrackingConfiguration(BaseValidatorModel):
    TargetValue: float


class MatchedPlayerSession(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None


class PlacedPlayerSession(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None


class PlayerLatency(BaseValidatorModel):
    PlayerId: Optional[str] = None
    RegionIdentifier: Optional[str] = None
    LatencyInMilliseconds: Optional[float] = None


class PriorityConfigurationOverrideOutput(BaseValidatorModel):
    LocationOrder: List[str]
    PlacementFallbackStrategy: Optional[PlacementFallbackStrategyType] = None


class PriorityConfigurationOutput(BaseValidatorModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None


class GetComputeAccessInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class GetComputeAuthTokenInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class GetGameSessionLogUrlInput(BaseValidatorModel):
    GameSessionId: str


class GetInstanceAccessInput(BaseValidatorModel):
    FleetId: str
    InstanceId: str


class InstanceCredentials(BaseValidatorModel):
    UserName: Optional[str] = None
    Secret: Optional[str] = None


class ListAliasesInput(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListBuildsInput(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListComputeInput(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    ComputeStatus: Optional[ListComputeInputStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListContainerFleetsInput(BaseValidatorModel):
    ContainerGroupDefinitionName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListContainerGroupDefinitionVersionsInput(BaseValidatorModel):
    Name: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListContainerGroupDefinitionsInput(BaseValidatorModel):
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListFleetDeploymentsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListFleetsInput(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListGameServerGroupsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListGameServersInput(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListLocationsInput(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListScriptsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class PriorityConfigurationOverride(BaseValidatorModel):
    LocationOrder: Sequence[str]
    PlacementFallbackStrategy: Optional[PlacementFallbackStrategyType] = None


class PriorityConfiguration(BaseValidatorModel):
    PriorityOrder: Optional[Sequence[PriorityTypeType]] = None
    LocationOrder: Optional[Sequence[str]] = None


class TargetConfiguration(BaseValidatorModel):
    TargetValue: float


class RegisterComputeInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str
    CertificatePath: Optional[str] = None
    DnsName: Optional[str] = None
    IpAddress: Optional[str] = None
    Location: Optional[str] = None


class RegisterGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    InstanceId: str
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None


class RequestUploadCredentialsInput(BaseValidatorModel):
    BuildId: str


class ResolveAliasInput(BaseValidatorModel):
    AliasId: str


class ResumeGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    ResumeActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]


class ServerProcess(BaseValidatorModel):
    LaunchPath: str
    ConcurrentExecutions: int
    Parameters: Optional[str] = None


class SearchGameSessionsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class StartFleetActionsInput(BaseValidatorModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None


class StopFleetActionsInput(BaseValidatorModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None


class StopGameSessionPlacementInput(BaseValidatorModel):
    PlacementId: str


class StopMatchmakingInput(BaseValidatorModel):
    TicketId: str


class SuspendGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    SuspendActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]


class TerminateGameSessionInput(BaseValidatorModel):
    GameSessionId: str
    TerminationMode: TerminationModeType


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateBuildInput(BaseValidatorModel):
    BuildId: str
    Name: Optional[str] = None
    Version: Optional[str] = None


class UpdateFleetCapacityInput(BaseValidatorModel):
    FleetId: str
    DesiredInstances: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Location: Optional[str] = None


class UpdateGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    GameServerData: Optional[str] = None
    UtilizationStatus: Optional[GameServerUtilizationStatusType] = None
    HealthCheck: Optional[Literal["HEALTHY"]] = None


class ValidateMatchmakingRuleSetInput(BaseValidatorModel):
    RuleSetBody: str


class VpcPeeringConnectionStatus(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class RoutingStrategy(BaseValidatorModel):
    pass


class Alias(BaseValidatorModel):
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    AliasArn: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategy] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class UpdateAliasInput(BaseValidatorModel):
    AliasId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategy] = None


class PlayerOutput(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Dict[str, AttributeValueOutput]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Dict[str, int]] = None


class ClaimGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: Optional[str] = None
    GameServerData: Optional[str] = None
    FilterOption: Optional[ClaimFilterOption] = None


class ClaimGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


class DescribeBuildOutput(BaseValidatorModel):
    Build: Build
    ResponseMetadata: ResponseMetadata


class DescribeGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetComputeAuthTokenOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    AuthToken: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetGameSessionLogUrlOutput(BaseValidatorModel):
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadata


class ListBuildsOutput(BaseValidatorModel):
    Builds: List[Build]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFleetsOutput(BaseValidatorModel):
    FleetIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGameServersOutput(BaseValidatorModel):
    GameServers: List[GameServer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutScalingPolicyOutput(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class RegisterGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


class ResolveAliasOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


class StartFleetActionsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


class StopFleetActionsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


class UpdateBuildOutput(BaseValidatorModel):
    Build: Build
    ResponseMetadata: ResponseMetadata


class UpdateFleetAttributesOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


class UpdateFleetCapacityOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    Location: str
    ResponseMetadata: ResponseMetadata


class UpdateFleetPortSettingsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


class UpdateGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


class ValidateMatchmakingRuleSetOutput(BaseValidatorModel):
    Valid: bool
    ResponseMetadata: ResponseMetadata


class IpPermission(BaseValidatorModel):
    pass


class DescribeFleetPortSettingsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    InboundPermissions: List[IpPermission]
    UpdateStatus: Literal["PENDING_UPDATE"]
    Location: str
    ResponseMetadata: ResponseMetadata


class UpdateFleetPortSettingsInput(BaseValidatorModel):
    FleetId: str
    InboundPermissionAuthorizations: Optional[Sequence[IpPermission]] = None
    InboundPermissionRevocations: Optional[Sequence[IpPermission]] = None


class ContainerFleet(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    FleetRoleArn: Optional[str] = None
    GameServerContainerGroupDefinitionName: Optional[str] = None
    GameServerContainerGroupDefinitionArn: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionArn: Optional[str] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRange] = None
    InstanceInboundPermissions: Optional[List[IpPermission]] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    MaximumGameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceType: Optional[str] = None
    BillingType: Optional[ContainerFleetBillingTypeType] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    MetricGroups: Optional[List[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicy] = None
    Status: Optional[ContainerFleetStatusType] = None
    DeploymentDetails: Optional[DeploymentDetails] = None
    LogConfiguration: Optional[LogConfiguration] = None
    LocationAttributes: Optional[List[ContainerFleetLocationAttributes]] = None


class GetComputeAccessOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    Credentials: AwsCredentials
    Target: str
    ContainerIdentifiers: List[ContainerIdentifier]
    ResponseMetadata: ResponseMetadata


class ContainerPortRange(BaseValidatorModel):
    pass


class ContainerPortConfigurationOutput(BaseValidatorModel):
    ContainerPortRanges: List[ContainerPortRange]


class ContainerPortConfiguration(BaseValidatorModel):
    ContainerPortRanges: Sequence[ContainerPortRange]


class CreateAliasInput(BaseValidatorModel):
    Name: str
    RoutingStrategy: RoutingStrategy
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateLocationInput(BaseValidatorModel):
    LocationName: str
    Tags: Optional[Sequence[Tag]] = None


class CreateMatchmakingRuleSetInput(BaseValidatorModel):
    Name: str
    RuleSetBody: str
    Tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateBuildInput(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3Location] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Tags: Optional[Sequence[Tag]] = None
    ServerSdkVersion: Optional[str] = None


class CreateBuildOutput(BaseValidatorModel):
    Build: Build
    UploadCredentials: AwsCredentials
    StorageLocation: S3Location
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class CreateScriptInput(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3Location] = None
    ZipFile: Optional[Blob] = None
    Tags: Optional[Sequence[Tag]] = None


class RequestUploadCredentialsOutput(BaseValidatorModel):
    UploadCredentials: AwsCredentials
    StorageLocation: S3Location
    ResponseMetadata: ResponseMetadata


class Script(BaseValidatorModel):
    ScriptId: Optional[str] = None
    ScriptArn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None
    SizeOnDisk: Optional[int] = None
    CreationTime: Optional[datetime] = None
    StorageLocation: Optional[S3Location] = None


class UpdateScriptInput(BaseValidatorModel):
    ScriptId: str
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3Location] = None
    ZipFile: Optional[Blob] = None


class CreateContainerFleetInput(BaseValidatorModel):
    FleetRoleArn: str
    Description: Optional[str] = None
    GameServerContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRange] = None
    InstanceInboundPermissions: Optional[Sequence[IpPermission]] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceType: Optional[str] = None
    BillingType: Optional[ContainerFleetBillingTypeType] = None
    Locations: Optional[Sequence[LocationConfiguration]] = None
    MetricGroups: Optional[Sequence[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicy] = None
    LogConfiguration: Optional[LogConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateFleetLocationsInput(BaseValidatorModel):
    FleetId: str
    Locations: Sequence[LocationConfiguration]


class FleetAttributes(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    InstanceType: Optional[EC2InstanceTypeType] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    CreationTime: Optional[datetime] = None
    TerminationTime: Optional[datetime] = None
    Status: Optional[FleetStatusType] = None
    BuildId: Optional[str] = None
    BuildArn: Optional[str] = None
    ScriptId: Optional[str] = None
    ScriptArn: Optional[str] = None
    ServerLaunchPath: Optional[str] = None
    ServerLaunchParameters: Optional[str] = None
    LogPaths: Optional[List[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicy] = None
    MetricGroups: Optional[List[str]] = None
    StoppedActions: Optional[List[Literal["AUTO_SCALING"]]] = None
    InstanceRoleArn: Optional[str] = None
    CertificateConfiguration: Optional[CertificateConfiguration] = None
    ComputeType: Optional[ComputeTypeType] = None
    AnywhereConfiguration: Optional[AnywhereConfiguration] = None
    InstanceRoleCredentialsProvider: Optional[Literal["SHARED_CREDENTIAL_FILE"]] = None


class UpdateFleetAttributesInput(BaseValidatorModel):
    FleetId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicy] = None
    MetricGroups: Optional[Sequence[str]] = None
    AnywhereConfiguration: Optional[AnywhereConfiguration] = None


class CreateFleetLocationsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationState]
    ResponseMetadata: ResponseMetadata


class DeleteFleetLocationsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationState]
    ResponseMetadata: ResponseMetadata


class LocationAttributes(BaseValidatorModel):
    LocationState: Optional[LocationState] = None
    StoppedActions: Optional[List[Literal["AUTO_SCALING"]]] = None
    UpdateStatus: Optional[Literal["PENDING_UPDATE"]] = None


class GameServerGroup(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[List[InstanceDefinition]] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    AutoScalingGroupArn: Optional[str] = None
    Status: Optional[GameServerGroupStatusType] = None
    StatusReason: Optional[str] = None
    SuspendedActions: Optional[List[Literal["REPLACE_INSTANCE_TYPES"]]] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class UpdateGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[Sequence[InstanceDefinition]] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None


class CreateGameSessionInput(BaseValidatorModel):
    MaximumPlayerSessionCount: int
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    GameProperties: Optional[Sequence[GameProperty]] = None
    CreatorId: Optional[str] = None
    GameSessionId: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    GameSessionData: Optional[str] = None
    Location: Optional[str] = None


class CreateMatchmakingConfigurationInput(BaseValidatorModel):
    Name: str
    RequestTimeoutSeconds: int
    AcceptanceRequired: bool
    RuleSetName: str
    Description: Optional[str] = None
    GameSessionQueueArns: Optional[Sequence[str]] = None
    AcceptanceTimeoutSeconds: Optional[int] = None
    NotificationTarget: Optional[str] = None
    AdditionalPlayerCount: Optional[int] = None
    CustomEventData: Optional[str] = None
    GameProperties: Optional[Sequence[GameProperty]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None
    Tags: Optional[Sequence[Tag]] = None


class GameSession(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    Name: Optional[str] = None
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    TerminationTime: Optional[datetime] = None
    CurrentPlayerSessionCount: Optional[int] = None
    MaximumPlayerSessionCount: Optional[int] = None
    Status: Optional[GameSessionStatusType] = None
    StatusReason: Optional[GameSessionStatusReasonType] = None
    GameProperties: Optional[List[GameProperty]] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    CreatorId: Optional[str] = None
    GameSessionData: Optional[str] = None
    MatchmakerData: Optional[str] = None
    Location: Optional[str] = None


class MatchmakingConfiguration(BaseValidatorModel):
    Name: Optional[str] = None
    ConfigurationArn: Optional[str] = None
    Description: Optional[str] = None
    GameSessionQueueArns: Optional[List[str]] = None
    RequestTimeoutSeconds: Optional[int] = None
    AcceptanceTimeoutSeconds: Optional[int] = None
    AcceptanceRequired: Optional[bool] = None
    RuleSetName: Optional[str] = None
    RuleSetArn: Optional[str] = None
    NotificationTarget: Optional[str] = None
    AdditionalPlayerCount: Optional[int] = None
    CustomEventData: Optional[str] = None
    CreationTime: Optional[datetime] = None
    GameProperties: Optional[List[GameProperty]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None


class UpdateGameSessionInput(BaseValidatorModel):
    GameSessionId: str
    MaximumPlayerSessionCount: Optional[int] = None
    Name: Optional[str] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameProperties: Optional[Sequence[GameProperty]] = None


class UpdateMatchmakingConfigurationInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    GameSessionQueueArns: Optional[Sequence[str]] = None
    RequestTimeoutSeconds: Optional[int] = None
    AcceptanceTimeoutSeconds: Optional[int] = None
    AcceptanceRequired: Optional[bool] = None
    RuleSetName: Optional[str] = None
    NotificationTarget: Optional[str] = None
    AdditionalPlayerCount: Optional[int] = None
    CustomEventData: Optional[str] = None
    GameProperties: Optional[Sequence[GameProperty]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None


class CreateLocationOutput(BaseValidatorModel):
    Location: LocationModel
    ResponseMetadata: ResponseMetadata


class ListLocationsOutput(BaseValidatorModel):
    Locations: List[LocationModel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateMatchmakingRuleSetOutput(BaseValidatorModel):
    RuleSet: MatchmakingRuleSet
    ResponseMetadata: ResponseMetadata


class DescribeMatchmakingRuleSetsOutput(BaseValidatorModel):
    RuleSets: List[MatchmakingRuleSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreatePlayerSessionOutput(BaseValidatorModel):
    PlayerSession: PlayerSession
    ResponseMetadata: ResponseMetadata


class CreatePlayerSessionsOutput(BaseValidatorModel):
    PlayerSessions: List[PlayerSession]
    ResponseMetadata: ResponseMetadata


class DescribePlayerSessionsOutput(BaseValidatorModel):
    PlayerSessions: List[PlayerSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateVpcPeeringAuthorizationOutput(BaseValidatorModel):
    VpcPeeringAuthorization: VpcPeeringAuthorization
    ResponseMetadata: ResponseMetadata


class DescribeVpcPeeringAuthorizationsOutput(BaseValidatorModel):
    VpcPeeringAuthorizations: List[VpcPeeringAuthorization]
    ResponseMetadata: ResponseMetadata


class FleetDeployment(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    FleetId: Optional[str] = None
    GameServerBinaryArn: Optional[str] = None
    RollbackGameServerBinaryArn: Optional[str] = None
    PerInstanceBinaryArn: Optional[str] = None
    RollbackPerInstanceBinaryArn: Optional[str] = None
    DeploymentStatus: Optional[DeploymentStatusType] = None
    DeploymentConfiguration: Optional[DeploymentConfiguration] = None
    CreationTime: Optional[datetime] = None


class UpdateContainerFleetInput(BaseValidatorModel):
    FleetId: str
    GameServerContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRange] = None
    InstanceInboundPermissionAuthorizations: Optional[Sequence[IpPermission]] = None
    InstanceInboundPermissionRevocations: Optional[Sequence[IpPermission]] = None
    DeploymentConfiguration: Optional[DeploymentConfiguration] = None
    Description: Optional[str] = None
    MetricGroups: Optional[Sequence[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicy] = None
    LogConfiguration: Optional[LogConfiguration] = None
    RemoveAttributes: Optional[Sequence[Literal["PER_INSTANCE_CONTAINER_GROUP_DEFINITION"]]] = None


class DescribeEC2InstanceLimitsOutput(BaseValidatorModel):
    EC2InstanceLimits: List[EC2InstanceLimit]
    ResponseMetadata: ResponseMetadata


class DescribeFleetAttributesInputPaginate(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetCapacityInputPaginate(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetUtilizationInputPaginate(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameServerInstancesInputPaginate(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameSessionDetailsInputPaginate(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameSessionQueuesInputPaginate(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameSessionsInputPaginate(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstancesInputPaginate(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMatchmakingConfigurationsInputPaginate(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMatchmakingRuleSetsInputPaginate(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePlayerSessionsInputPaginate(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScalingPoliciesInputPaginate(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAliasesInputPaginate(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBuildsInputPaginate(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComputeInputPaginate(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    ComputeStatus: Optional[ListComputeInputStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContainerFleetsInputPaginate(BaseValidatorModel):
    ContainerGroupDefinitionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContainerGroupDefinitionVersionsInputPaginate(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContainerGroupDefinitionsInputPaginate(BaseValidatorModel):
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetDeploymentsInputPaginate(BaseValidatorModel):
    FleetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsInputPaginate(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGameServerGroupsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGameServersInputPaginate(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLocationsInputPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScriptsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchGameSessionsInputPaginate(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class DescribeFleetEventsInputPaginate(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetEventsInput(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetEventsOutput(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFleetLocationUtilizationOutput(BaseValidatorModel):
    FleetUtilization: FleetUtilization
    ResponseMetadata: ResponseMetadata


class DescribeFleetUtilizationOutput(BaseValidatorModel):
    FleetUtilization: List[FleetUtilization]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeGameServerInstancesOutput(BaseValidatorModel):
    GameServerInstances: List[GameServerInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Instance(BaseValidatorModel):
    pass


class DescribeInstancesOutput(BaseValidatorModel):
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FleetCapacity(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    InstanceType: Optional[EC2InstanceTypeType] = None
    InstanceCounts: Optional[EC2InstanceCounts] = None
    Location: Optional[str] = None
    GameServerContainerGroupCounts: Optional[GameServerContainerGroupCounts] = None


class GameServerGroupAutoScalingPolicy(BaseValidatorModel):
    TargetTrackingConfiguration: TargetTrackingConfiguration
    EstimatedInstanceWarmup: Optional[int] = None


class GameSessionConnectionInfo(BaseValidatorModel):
    GameSessionArn: Optional[str] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    MatchedPlayerSessions: Optional[List[MatchedPlayerSession]] = None


class GameSessionPlacement(BaseValidatorModel):
    PlacementId: Optional[str] = None
    GameSessionQueueName: Optional[str] = None
    Status: Optional[GameSessionPlacementStateType] = None
    GameProperties: Optional[List[GameProperty]] = None
    MaximumPlayerSessionCount: Optional[int] = None
    GameSessionName: Optional[str] = None
    GameSessionId: Optional[str] = None
    GameSessionArn: Optional[str] = None
    GameSessionRegion: Optional[str] = None
    PlayerLatencies: Optional[List[PlayerLatency]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    PlacedPlayerSessions: Optional[List[PlacedPlayerSession]] = None
    GameSessionData: Optional[str] = None
    MatchmakerData: Optional[str] = None
    PriorityConfigurationOverride: Optional[PriorityConfigurationOverrideOutput] = None


class GameSessionQueue(BaseValidatorModel):
    Name: Optional[str] = None
    GameSessionQueueArn: Optional[str] = None
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[List[PlayerLatencyPolicy]] = None
    Destinations: Optional[List[GameSessionQueueDestination]] = None
    FilterConfiguration: Optional[FilterConfigurationOutput] = None
    PriorityConfiguration: Optional[PriorityConfigurationOutput] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None


class InstanceAccess(BaseValidatorModel):
    FleetId: Optional[str] = None
    InstanceId: Optional[str] = None
    IpAddress: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Credentials: Optional[InstanceCredentials] = None


class PutScalingPolicyInput(BaseValidatorModel):
    Name: str
    FleetId: str
    MetricName: MetricNameType
    ScalingAdjustment: Optional[int] = None
    ScalingAdjustmentType: Optional[ScalingAdjustmentTypeType] = None
    Threshold: Optional[float] = None
    ComparisonOperator: Optional[ComparisonOperatorTypeType] = None
    EvaluationPeriods: Optional[int] = None
    PolicyType: Optional[PolicyTypeType] = None
    TargetConfiguration: Optional[TargetConfiguration] = None


class ScalingPolicy(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ScalingStatusTypeType] = None
    ScalingAdjustment: Optional[int] = None
    ScalingAdjustmentType: Optional[ScalingAdjustmentTypeType] = None
    ComparisonOperator: Optional[ComparisonOperatorTypeType] = None
    Threshold: Optional[float] = None
    EvaluationPeriods: Optional[int] = None
    MetricName: Optional[MetricNameType] = None
    PolicyType: Optional[PolicyTypeType] = None
    TargetConfiguration: Optional[TargetConfiguration] = None
    UpdateStatus: Optional[Literal["PENDING_UPDATE"]] = None
    Location: Optional[str] = None


class RuntimeConfigurationOutput(BaseValidatorModel):
    ServerProcesses: Optional[List[ServerProcess]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None


class RuntimeConfiguration(BaseValidatorModel):
    ServerProcesses: Optional[Sequence[ServerProcess]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None


class VpcPeeringConnection(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    IpV4CidrBlock: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    Status: Optional[VpcPeeringConnectionStatus] = None
    PeerVpcId: Optional[str] = None
    GameLiftVpcId: Optional[str] = None


class CreateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class DescribeAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class ListAliasesOutput(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class AttributeValueUnion(BaseValidatorModel):
    pass


class Player(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Mapping[str, AttributeValueUnion]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Mapping[str, int]] = None


class Compute(BaseValidatorModel):
    pass


class DescribeComputeOutput(BaseValidatorModel):
    Compute: Compute
    ResponseMetadata: ResponseMetadata


class ListComputeOutput(BaseValidatorModel):
    ComputeList: List[Compute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RegisterComputeOutput(BaseValidatorModel):
    Compute: Compute
    ResponseMetadata: ResponseMetadata


class CreateContainerFleetOutput(BaseValidatorModel):
    ContainerFleet: ContainerFleet
    ResponseMetadata: ResponseMetadata


class DescribeContainerFleetOutput(BaseValidatorModel):
    ContainerFleet: ContainerFleet
    ResponseMetadata: ResponseMetadata


class ListContainerFleetsOutput(BaseValidatorModel):
    ContainerFleets: List[ContainerFleet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateContainerFleetOutput(BaseValidatorModel):
    ContainerFleet: ContainerFleet
    ResponseMetadata: ResponseMetadata


class GameServerContainerDefinition(BaseValidatorModel):
    ContainerName: Optional[str] = None
    DependsOn: Optional[List[ContainerDependency]] = None
    MountPoints: Optional[List[ContainerMountPoint]] = None
    EnvironmentOverride: Optional[List[ContainerEnvironment]] = None
    ImageUri: Optional[str] = None
    PortConfiguration: Optional[ContainerPortConfigurationOutput] = None
    ResolvedImageDigest: Optional[str] = None
    ServerSdkVersion: Optional[str] = None


class SupportContainerDefinition(BaseValidatorModel):
    ContainerName: Optional[str] = None
    DependsOn: Optional[List[ContainerDependency]] = None
    MountPoints: Optional[List[ContainerMountPoint]] = None
    EnvironmentOverride: Optional[List[ContainerEnvironment]] = None
    Essential: Optional[bool] = None
    HealthCheck: Optional[ContainerHealthCheckOutput] = None
    ImageUri: Optional[str] = None
    MemoryHardLimitMebibytes: Optional[int] = None
    PortConfiguration: Optional[ContainerPortConfigurationOutput] = None
    ResolvedImageDigest: Optional[str] = None
    Vcpu: Optional[float] = None


class CreateScriptOutput(BaseValidatorModel):
    Script: Script
    ResponseMetadata: ResponseMetadata


class DescribeScriptOutput(BaseValidatorModel):
    Script: Script
    ResponseMetadata: ResponseMetadata


class ListScriptsOutput(BaseValidatorModel):
    Scripts: List[Script]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateScriptOutput(BaseValidatorModel):
    Script: Script
    ResponseMetadata: ResponseMetadata


class CreateFleetOutput(BaseValidatorModel):
    FleetAttributes: FleetAttributes
    LocationStates: List[LocationState]
    ResponseMetadata: ResponseMetadata


class DescribeFleetAttributesOutput(BaseValidatorModel):
    FleetAttributes: List[FleetAttributes]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFleetLocationAttributesOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationAttributes: List[LocationAttributes]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


class DeleteGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


class DescribeGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


class ListGameServerGroupsOutput(BaseValidatorModel):
    GameServerGroups: List[GameServerGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResumeGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


class SuspendGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


class UpdateGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


class CreateGameSessionOutput(BaseValidatorModel):
    GameSession: GameSession
    ResponseMetadata: ResponseMetadata


class DescribeGameSessionsOutput(BaseValidatorModel):
    GameSessions: List[GameSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GameSessionDetail(BaseValidatorModel):
    GameSession: Optional[GameSession] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None


class SearchGameSessionsOutput(BaseValidatorModel):
    GameSessions: List[GameSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TerminateGameSessionOutput(BaseValidatorModel):
    GameSession: GameSession
    ResponseMetadata: ResponseMetadata


class UpdateGameSessionOutput(BaseValidatorModel):
    GameSession: GameSession
    ResponseMetadata: ResponseMetadata


class CreateMatchmakingConfigurationOutput(BaseValidatorModel):
    Configuration: MatchmakingConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeMatchmakingConfigurationsOutput(BaseValidatorModel):
    Configurations: List[MatchmakingConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateMatchmakingConfigurationOutput(BaseValidatorModel):
    Configuration: MatchmakingConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeFleetDeploymentOutput(BaseValidatorModel):
    FleetDeployment: FleetDeployment
    LocationalDeployments: Dict[str, LocationalDeployment]
    ResponseMetadata: ResponseMetadata


class ListFleetDeploymentsOutput(BaseValidatorModel):
    FleetDeployments: List[FleetDeployment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFleetCapacityOutput(BaseValidatorModel):
    FleetCapacity: List[FleetCapacity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFleetLocationCapacityOutput(BaseValidatorModel):
    FleetCapacity: FleetCapacity
    ResponseMetadata: ResponseMetadata


class CreateGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    RoleArn: str
    MinSize: int
    MaxSize: int
    LaunchTemplate: LaunchTemplateSpecification
    InstanceDefinitions: Sequence[InstanceDefinition]
    AutoScalingPolicy: Optional[GameServerGroupAutoScalingPolicy] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    VpcSubnets: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class MatchmakingTicket(BaseValidatorModel):
    TicketId: Optional[str] = None
    ConfigurationName: Optional[str] = None
    ConfigurationArn: Optional[str] = None
    Status: Optional[MatchmakingConfigurationStatusType] = None
    StatusReason: Optional[str] = None
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Players: Optional[List[PlayerOutput]] = None
    GameSessionConnectionInfo: Optional[GameSessionConnectionInfo] = None
    EstimatedWaitTime: Optional[int] = None


class DescribeGameSessionPlacementOutput(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacement
    ResponseMetadata: ResponseMetadata


class StartGameSessionPlacementOutput(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacement
    ResponseMetadata: ResponseMetadata


class StopGameSessionPlacementOutput(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacement
    ResponseMetadata: ResponseMetadata


class CreateGameSessionQueueOutput(BaseValidatorModel):
    GameSessionQueue: GameSessionQueue
    ResponseMetadata: ResponseMetadata


class DescribeGameSessionQueuesOutput(BaseValidatorModel):
    GameSessionQueues: List[GameSessionQueue]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateGameSessionQueueOutput(BaseValidatorModel):
    GameSessionQueue: GameSessionQueue
    ResponseMetadata: ResponseMetadata


class GetInstanceAccessOutput(BaseValidatorModel):
    InstanceAccess: InstanceAccess
    ResponseMetadata: ResponseMetadata


class PriorityConfigurationOverrideUnion(BaseValidatorModel):
    pass


class StartGameSessionPlacementInput(BaseValidatorModel):
    PlacementId: str
    GameSessionQueueName: str
    MaximumPlayerSessionCount: int
    GameProperties: Optional[Sequence[GameProperty]] = None
    GameSessionName: Optional[str] = None
    PlayerLatencies: Optional[Sequence[PlayerLatency]] = None
    DesiredPlayerSessions: Optional[Sequence[DesiredPlayerSession]] = None
    GameSessionData: Optional[str] = None
    PriorityConfigurationOverride: Optional[PriorityConfigurationOverrideUnion] = None


class FilterConfigurationUnion(BaseValidatorModel):
    pass


class PriorityConfigurationUnion(BaseValidatorModel):
    pass


class CreateGameSessionQueueInput(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicy]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestination]] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None
    PriorityConfiguration: Optional[PriorityConfigurationUnion] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class UpdateGameSessionQueueInput(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicy]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestination]] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None
    PriorityConfiguration: Optional[PriorityConfigurationUnion] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None


class DescribeScalingPoliciesOutput(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRuntimeConfigurationOutput(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationOutput
    ResponseMetadata: ResponseMetadata


class UpdateRuntimeConfigurationOutput(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationOutput
    ResponseMetadata: ResponseMetadata


class DescribeVpcPeeringConnectionsOutput(BaseValidatorModel):
    VpcPeeringConnections: List[VpcPeeringConnection]
    ResponseMetadata: ResponseMetadata


class ContainerGroupDefinition(BaseValidatorModel):
    Name: str
    ContainerGroupDefinitionArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    OperatingSystem: Optional[Literal["AMAZON_LINUX_2023"]] = None
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    TotalMemoryLimitMebibytes: Optional[int] = None
    TotalVcpuLimit: Optional[float] = None
    GameServerContainerDefinition: Optional[GameServerContainerDefinition] = None
    SupportContainerDefinitions: Optional[List[SupportContainerDefinition]] = None
    VersionNumber: Optional[int] = None
    VersionDescription: Optional[str] = None
    Status: Optional[ContainerGroupDefinitionStatusType] = None
    StatusReason: Optional[str] = None


class ContainerPortConfigurationUnion(BaseValidatorModel):
    pass


class GameServerContainerDefinitionInput(BaseValidatorModel):
    ContainerName: str
    ImageUri: str
    PortConfiguration: ContainerPortConfigurationUnion
    ServerSdkVersion: str
    DependsOn: Optional[Sequence[ContainerDependency]] = None
    MountPoints: Optional[Sequence[ContainerMountPoint]] = None
    EnvironmentOverride: Optional[Sequence[ContainerEnvironment]] = None


class ContainerHealthCheckUnion(BaseValidatorModel):
    pass


class SupportContainerDefinitionInput(BaseValidatorModel):
    ContainerName: str
    ImageUri: str
    DependsOn: Optional[Sequence[ContainerDependency]] = None
    MountPoints: Optional[Sequence[ContainerMountPoint]] = None
    EnvironmentOverride: Optional[Sequence[ContainerEnvironment]] = None
    Essential: Optional[bool] = None
    HealthCheck: Optional[ContainerHealthCheckUnion] = None
    MemoryHardLimitMebibytes: Optional[int] = None
    PortConfiguration: Optional[ContainerPortConfigurationUnion] = None
    Vcpu: Optional[float] = None


class DescribeGameSessionDetailsOutput(BaseValidatorModel):
    GameSessionDetails: List[GameSessionDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMatchmakingOutput(BaseValidatorModel):
    TicketList: List[MatchmakingTicket]
    ResponseMetadata: ResponseMetadata


class StartMatchBackfillOutput(BaseValidatorModel):
    MatchmakingTicket: MatchmakingTicket
    ResponseMetadata: ResponseMetadata


class StartMatchmakingOutput(BaseValidatorModel):
    MatchmakingTicket: MatchmakingTicket
    ResponseMetadata: ResponseMetadata


class RuntimeConfigurationUnion(BaseValidatorModel):
    pass


class CreateFleetInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ServerLaunchPath: Optional[str] = None
    ServerLaunchParameters: Optional[str] = None
    LogPaths: Optional[Sequence[str]] = None
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    EC2InboundPermissions: Optional[Sequence[IpPermission]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    RuntimeConfiguration: Optional[RuntimeConfigurationUnion] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicy] = None
    MetricGroups: Optional[Sequence[str]] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    InstanceRoleArn: Optional[str] = None
    CertificateConfiguration: Optional[CertificateConfiguration] = None
    Locations: Optional[Sequence[LocationConfiguration]] = None
    Tags: Optional[Sequence[Tag]] = None
    ComputeType: Optional[ComputeTypeType] = None
    AnywhereConfiguration: Optional[AnywhereConfiguration] = None
    InstanceRoleCredentialsProvider: Optional[Literal["SHARED_CREDENTIAL_FILE"]] = None


class UpdateRuntimeConfigurationInput(BaseValidatorModel):
    FleetId: str
    RuntimeConfiguration: RuntimeConfigurationUnion


class PlayerUnion(BaseValidatorModel):
    pass


class StartMatchBackfillInput(BaseValidatorModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnion]
    TicketId: Optional[str] = None
    GameSessionArn: Optional[str] = None


class StartMatchmakingInput(BaseValidatorModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnion]
    TicketId: Optional[str] = None


class CreateContainerGroupDefinitionOutput(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinition
    ResponseMetadata: ResponseMetadata


class DescribeContainerGroupDefinitionOutput(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinition
    ResponseMetadata: ResponseMetadata


class ListContainerGroupDefinitionVersionsOutput(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListContainerGroupDefinitionsOutput(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateContainerGroupDefinitionOutput(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinition
    ResponseMetadata: ResponseMetadata


class CreateContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    TotalMemoryLimitMebibytes: int
    TotalVcpuLimit: float
    OperatingSystem: Literal["AMAZON_LINUX_2023"]
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionInput] = None
    SupportContainerDefinitions: Optional[Sequence[SupportContainerDefinitionInput]] = None
    VersionDescription: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class UpdateContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionInput] = None
    SupportContainerDefinitions: Optional[Sequence[SupportContainerDefinitionInput]] = None
    TotalMemoryLimitMebibytes: Optional[int] = None
    TotalVcpuLimit: Optional[float] = None
    VersionDescription: Optional[str] = None
    SourceVersionNumber: Optional[int] = None
    OperatingSystem: Optional[Literal["AMAZON_LINUX_2023"]] = None


