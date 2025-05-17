from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.gamelift.gamelift_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptMatchInput(BaseValidatorModel):
    TicketId: str
    PlayerIds: List[str]
    AcceptanceType: AcceptanceTypeType


class RoutingStrategy(BaseValidatorModel):
    Type: Optional[RoutingStrategyTypeType] = None
    FleetId: Optional[str] = None
    Message: Optional[str] = None


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
    SL: Optional[List[str]] = None
    SDM: Optional[Dict[str, float]] = None


class AwsCredentials(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


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
    InstanceStatuses: Optional[List[FilterInstanceStatusType]] = None


class GameServer(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    GameServerId: Optional[str] = None
    InstanceId: Optional[str] = None
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None
    ClaimStatus: Optional[Literal['CLAIMED']] = None
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


class IpPermission(BaseValidatorModel):
    FromPort: int
    ToPort: int
    IpRange: str
    Protocol: IpProtocolType


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
    Command: List[str]
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


class ContainerPortRange(BaseValidatorModel):
    FromPort: int
    ToPort: int
    Protocol: IpProtocolType


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


# This class is the input for the 'create_player_session' function.
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


# This class is the input for the 'create_player_sessions' function.
class CreatePlayerSessionsInput(BaseValidatorModel):
    GameSessionId: str
    PlayerIds: List[str]
    PlayerDataMap: Optional[Dict[str, str]] = None


# This class is the input for the 'create_vpc_peering_authorization' function.
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


# This class is the input for the 'delete_alias' function.
class DeleteAliasInput(BaseValidatorModel):
    AliasId: str


# This class is the input for the 'delete_build' function.
class DeleteBuildInput(BaseValidatorModel):
    BuildId: str


class DeleteContainerFleetInput(BaseValidatorModel):
    FleetId: str


class DeleteContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    VersionNumber: Optional[int] = None
    VersionCountToRetain: Optional[int] = None


# This class is the input for the 'delete_fleet' function.
class DeleteFleetInput(BaseValidatorModel):
    FleetId: str


# This class is the input for the 'delete_fleet_locations' function.
class DeleteFleetLocationsInput(BaseValidatorModel):
    FleetId: str
    Locations: List[str]


# This class is the input for the 'delete_game_server_group' function.
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


# This class is the input for the 'delete_scaling_policy' function.
class DeleteScalingPolicyInput(BaseValidatorModel):
    Name: str
    FleetId: str


# This class is the input for the 'delete_script' function.
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


# This class is the input for the 'deregister_game_server' function.
class DeregisterGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str


# This class is the input for the 'describe_alias' function.
class DescribeAliasInput(BaseValidatorModel):
    AliasId: str


# This class is the input for the 'describe_build' function.
class DescribeBuildInput(BaseValidatorModel):
    BuildId: str


# This class is the input for the 'describe_compute' function.
class DescribeComputeInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


# This class is the input for the 'describe_container_fleet' function.
class DescribeContainerFleetInput(BaseValidatorModel):
    FleetId: str


# This class is the input for the 'describe_container_group_definition' function.
class DescribeContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    VersionNumber: Optional[int] = None


# This class is the input for the 'describe_ec2_instance_limits' function.
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


# This class is the input for the 'describe_fleet_attributes' function.
class DescribeFleetAttributesInput(BaseValidatorModel):
    FleetIds: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_fleet_capacity' function.
class DescribeFleetCapacityInput(BaseValidatorModel):
    FleetIds: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_fleet_deployment' function.
class DescribeFleetDeploymentInput(BaseValidatorModel):
    FleetId: str
    DeploymentId: Optional[str] = None


class LocationalDeployment(BaseValidatorModel):
    DeploymentStatus: Optional[DeploymentStatusType] = None

Timestamp = Union[datetime, str]


class Event(BaseValidatorModel):
    EventId: Optional[str] = None
    ResourceId: Optional[str] = None
    EventCode: Optional[EventCodeType] = None
    Message: Optional[str] = None
    EventTime: Optional[datetime] = None
    PreSignedLogUrl: Optional[str] = None
    Count: Optional[int] = None


# This class is the input for the 'describe_fleet_location_attributes' function.
class DescribeFleetLocationAttributesInput(BaseValidatorModel):
    FleetId: str
    Locations: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_fleet_location_capacity' function.
class DescribeFleetLocationCapacityInput(BaseValidatorModel):
    FleetId: str
    Location: str


# This class is the input for the 'describe_fleet_location_utilization' function.
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


# This class is the input for the 'describe_fleet_port_settings' function.
class DescribeFleetPortSettingsInput(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None


# This class is the input for the 'describe_fleet_utilization' function.
class DescribeFleetUtilizationInput(BaseValidatorModel):
    FleetIds: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_game_server_group' function.
class DescribeGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str


# This class is the input for the 'describe_game_server' function.
class DescribeGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str


# This class is the input for the 'describe_game_server_instances' function.
class DescribeGameServerInstancesInput(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GameServerInstance(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[GameServerInstanceStatusType] = None


# This class is the input for the 'describe_game_session_details' function.
class DescribeGameSessionDetailsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_game_session_placement' function.
class DescribeGameSessionPlacementInput(BaseValidatorModel):
    PlacementId: str


# This class is the input for the 'describe_game_session_queues' function.
class DescribeGameSessionQueuesInput(BaseValidatorModel):
    Names: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_game_sessions' function.
class DescribeGameSessionsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_instances' function.
class DescribeInstancesInput(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None


class Instance(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Type: Optional[EC2InstanceTypeType] = None
    Status: Optional[InstanceStatusType] = None
    CreationTime: Optional[datetime] = None
    Location: Optional[str] = None


# This class is the input for the 'describe_matchmaking_configurations' function.
class DescribeMatchmakingConfigurationsInput(BaseValidatorModel):
    Names: Optional[List[str]] = None
    RuleSetName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_matchmaking' function.
class DescribeMatchmakingInput(BaseValidatorModel):
    TicketIds: List[str]


# This class is the input for the 'describe_matchmaking_rule_sets' function.
class DescribeMatchmakingRuleSetsInput(BaseValidatorModel):
    Names: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_player_sessions' function.
class DescribePlayerSessionsInput(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_runtime_configuration' function.
class DescribeRuntimeConfigurationInput(BaseValidatorModel):
    FleetId: str


# This class is the input for the 'describe_scaling_policies' function.
class DescribeScalingPoliciesInput(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None


# This class is the input for the 'describe_script' function.
class DescribeScriptInput(BaseValidatorModel):
    ScriptId: str


# This class is the input for the 'describe_vpc_peering_connections' function.
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
    AllowedLocations: Optional[List[str]] = None


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


# This class is the input for the 'get_compute_access' function.
class GetComputeAccessInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


# This class is the input for the 'get_compute_auth_token' function.
class GetComputeAuthTokenInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str


# This class is the input for the 'get_game_session_log_url' function.
class GetGameSessionLogUrlInput(BaseValidatorModel):
    GameSessionId: str


# This class is the input for the 'get_instance_access' function.
class GetInstanceAccessInput(BaseValidatorModel):
    FleetId: str
    InstanceId: str


class InstanceCredentials(BaseValidatorModel):
    UserName: Optional[str] = None
    Secret: Optional[str] = None


# This class is the input for the 'list_aliases' function.
class ListAliasesInput(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_builds' function.
class ListBuildsInput(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_compute' function.
class ListComputeInput(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    ComputeStatus: Optional[ListComputeInputStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_container_fleets' function.
class ListContainerFleetsInput(BaseValidatorModel):
    ContainerGroupDefinitionName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_container_group_definition_versions' function.
class ListContainerGroupDefinitionVersionsInput(BaseValidatorModel):
    Name: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_container_group_definitions' function.
class ListContainerGroupDefinitionsInput(BaseValidatorModel):
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_fleet_deployments' function.
class ListFleetDeploymentsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_fleets' function.
class ListFleetsInput(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_game_server_groups' function.
class ListGameServerGroupsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_game_servers' function.
class ListGameServersInput(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_locations' function.
class ListLocationsInput(BaseValidatorModel):
    Filters: Optional[List[LocationFilterType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_scripts' function.
class ListScriptsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class PriorityConfigurationOverride(BaseValidatorModel):
    LocationOrder: List[str]
    PlacementFallbackStrategy: Optional[PlacementFallbackStrategyType] = None


class PriorityConfiguration(BaseValidatorModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None


class TargetConfiguration(BaseValidatorModel):
    TargetValue: float


# This class is the input for the 'register_compute' function.
class RegisterComputeInput(BaseValidatorModel):
    FleetId: str
    ComputeName: str
    CertificatePath: Optional[str] = None
    DnsName: Optional[str] = None
    IpAddress: Optional[str] = None
    Location: Optional[str] = None


# This class is the input for the 'register_game_server' function.
class RegisterGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    InstanceId: str
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None


# This class is the input for the 'request_upload_credentials' function.
class RequestUploadCredentialsInput(BaseValidatorModel):
    BuildId: str


# This class is the input for the 'resolve_alias' function.
class ResolveAliasInput(BaseValidatorModel):
    AliasId: str


# This class is the input for the 'resume_game_server_group' function.
class ResumeGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    ResumeActions: List[Literal['REPLACE_INSTANCE_TYPES']]


class ServerProcess(BaseValidatorModel):
    LaunchPath: str
    ConcurrentExecutions: int
    Parameters: Optional[str] = None


# This class is the input for the 'search_game_sessions' function.
class SearchGameSessionsInput(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'start_fleet_actions' function.
class StartFleetActionsInput(BaseValidatorModel):
    FleetId: str
    Actions: List[Literal['AUTO_SCALING']]
    Location: Optional[str] = None


# This class is the input for the 'stop_fleet_actions' function.
class StopFleetActionsInput(BaseValidatorModel):
    FleetId: str
    Actions: List[Literal['AUTO_SCALING']]
    Location: Optional[str] = None


# This class is the input for the 'stop_game_session_placement' function.
class StopGameSessionPlacementInput(BaseValidatorModel):
    PlacementId: str


class StopMatchmakingInput(BaseValidatorModel):
    TicketId: str


# This class is the input for the 'suspend_game_server_group' function.
class SuspendGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    SuspendActions: List[Literal['REPLACE_INSTANCE_TYPES']]


# This class is the input for the 'terminate_game_session' function.
class TerminateGameSessionInput(BaseValidatorModel):
    GameSessionId: str
    TerminationMode: TerminationModeType


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_build' function.
class UpdateBuildInput(BaseValidatorModel):
    BuildId: str
    Name: Optional[str] = None
    Version: Optional[str] = None


# This class is the input for the 'update_fleet_capacity' function.
class UpdateFleetCapacityInput(BaseValidatorModel):
    FleetId: str
    DesiredInstances: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Location: Optional[str] = None


# This class is the input for the 'update_game_server' function.
class UpdateGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    GameServerData: Optional[str] = None
    UtilizationStatus: Optional[GameServerUtilizationStatusType] = None
    HealthCheck: Optional[Literal['HEALTHY']] = None


# This class is the input for the 'validate_matchmaking_rule_set' function.
class ValidateMatchmakingRuleSetInput(BaseValidatorModel):
    RuleSetBody: str


class VpcPeeringConnectionStatus(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class Alias(BaseValidatorModel):
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    AliasArn: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategy] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


# This class is the input for the 'update_alias' function.
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

AttributeValueUnion = Union[AttributeValue, AttributeValueOutput]


# This class is the input for the 'claim_game_server' function.
class ClaimGameServerInput(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: Optional[str] = None
    GameServerData: Optional[str] = None
    FilterOption: Optional[ClaimFilterOption] = None


# This class is the output for the 'claim_game_server' function.
class ClaimGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_build' function.
class DescribeBuildOutput(BaseValidatorModel):
    Build: Build
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_game_server' function.
class DescribeGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_game_server' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_compute_auth_token' function.
class GetComputeAuthTokenOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    AuthToken: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_game_session_log_url' function.
class GetGameSessionLogUrlOutput(BaseValidatorModel):
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_builds' function.
class ListBuildsOutput(BaseValidatorModel):
    Builds: List[Build]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_fleets' function.
class ListFleetsOutput(BaseValidatorModel):
    FleetIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_game_servers' function.
class ListGameServersOutput(BaseValidatorModel):
    GameServers: List[GameServer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_scaling_policy' function.
class PutScalingPolicyOutput(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_game_server' function.
class RegisterGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resolve_alias' function.
class ResolveAliasOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_fleet_actions' function.
class StartFleetActionsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_fleet_actions' function.
class StopFleetActionsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_build' function.
class UpdateBuildOutput(BaseValidatorModel):
    Build: Build
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_fleet_attributes' function.
class UpdateFleetAttributesOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_fleet_capacity' function.
class UpdateFleetCapacityOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_fleet_port_settings' function.
class UpdateFleetPortSettingsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_game_server' function.
class UpdateGameServerOutput(BaseValidatorModel):
    GameServer: GameServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'validate_matchmaking_rule_set' function.
class ValidateMatchmakingRuleSetOutput(BaseValidatorModel):
    Valid: bool
    ResponseMetadata: ResponseMetadata


class Compute(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    ComputeName: Optional[str] = None
    ComputeArn: Optional[str] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    ComputeStatus: Optional[ComputeStatusType] = None
    Location: Optional[str] = None
    CreationTime: Optional[datetime] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Type: Optional[EC2InstanceTypeType] = None
    GameLiftServiceSdkEndpoint: Optional[str] = None
    GameLiftAgentEndpoint: Optional[str] = None
    InstanceId: Optional[str] = None
    ContainerAttributes: Optional[List[ContainerAttribute]] = None
    GameServerContainerGroupDefinitionArn: Optional[str] = None


# This class is the output for the 'describe_fleet_port_settings' function.
class DescribeFleetPortSettingsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    InboundPermissions: List[IpPermission]
    UpdateStatus: Literal['PENDING_UPDATE']
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_fleet_port_settings' function.
class UpdateFleetPortSettingsInput(BaseValidatorModel):
    FleetId: str
    InboundPermissionAuthorizations: Optional[List[IpPermission]] = None
    InboundPermissionRevocations: Optional[List[IpPermission]] = None


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

ContainerHealthCheckUnion = Union[ContainerHealthCheck, ContainerHealthCheckOutput]


# This class is the output for the 'get_compute_access' function.
class GetComputeAccessOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    Credentials: AwsCredentials
    Target: str
    ContainerIdentifiers: List[ContainerIdentifier]
    ResponseMetadata: ResponseMetadata


class ContainerPortConfigurationOutput(BaseValidatorModel):
    ContainerPortRanges: List[ContainerPortRange]


class ContainerPortConfiguration(BaseValidatorModel):
    ContainerPortRanges: List[ContainerPortRange]


# This class is the input for the 'create_alias' function.
class CreateAliasInput(BaseValidatorModel):
    Name: str
    RoutingStrategy: RoutingStrategy
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_location' function.
class CreateLocationInput(BaseValidatorModel):
    LocationName: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_matchmaking_rule_set' function.
class CreateMatchmakingRuleSetInput(BaseValidatorModel):
    Name: str
    RuleSetBody: str
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the input for the 'create_build' function.
class CreateBuildInput(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3Location] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Tags: Optional[List[Tag]] = None
    ServerSdkVersion: Optional[str] = None


# This class is the output for the 'create_build' function.
class CreateBuildOutput(BaseValidatorModel):
    Build: Build
    UploadCredentials: AwsCredentials
    StorageLocation: S3Location
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_script' function.
class CreateScriptInput(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3Location] = None
    ZipFile: Optional[Blob] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'request_upload_credentials' function.
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


# This class is the input for the 'update_script' function.
class UpdateScriptInput(BaseValidatorModel):
    ScriptId: str
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3Location] = None
    ZipFile: Optional[Blob] = None


# This class is the input for the 'create_container_fleet' function.
class CreateContainerFleetInput(BaseValidatorModel):
    FleetRoleArn: str
    Description: Optional[str] = None
    GameServerContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRange] = None
    InstanceInboundPermissions: Optional[List[IpPermission]] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceType: Optional[str] = None
    BillingType: Optional[ContainerFleetBillingTypeType] = None
    Locations: Optional[List[LocationConfiguration]] = None
    MetricGroups: Optional[List[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicy] = None
    LogConfiguration: Optional[LogConfiguration] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_fleet_locations' function.
class CreateFleetLocationsInput(BaseValidatorModel):
    FleetId: str
    Locations: List[LocationConfiguration]


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
    StoppedActions: Optional[List[Literal['AUTO_SCALING']]] = None
    InstanceRoleArn: Optional[str] = None
    CertificateConfiguration: Optional[CertificateConfiguration] = None
    ComputeType: Optional[ComputeTypeType] = None
    AnywhereConfiguration: Optional[AnywhereConfiguration] = None
    InstanceRoleCredentialsProvider: Optional[Literal['SHARED_CREDENTIAL_FILE']] = None


# This class is the input for the 'update_fleet_attributes' function.
class UpdateFleetAttributesInput(BaseValidatorModel):
    FleetId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicy] = None
    MetricGroups: Optional[List[str]] = None
    AnywhereConfiguration: Optional[AnywhereConfiguration] = None


# This class is the output for the 'create_fleet_locations' function.
class CreateFleetLocationsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationState]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_fleet_locations' function.
class DeleteFleetLocationsOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationState]
    ResponseMetadata: ResponseMetadata


class LocationAttributes(BaseValidatorModel):
    LocationState: Optional[LocationState] = None
    StoppedActions: Optional[List[Literal['AUTO_SCALING']]] = None
    UpdateStatus: Optional[Literal['PENDING_UPDATE']] = None


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
    SuspendedActions: Optional[List[Literal['REPLACE_INSTANCE_TYPES']]] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


# This class is the input for the 'update_game_server_group' function.
class UpdateGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[List[InstanceDefinition]] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None


# This class is the input for the 'create_game_session' function.
class CreateGameSessionInput(BaseValidatorModel):
    MaximumPlayerSessionCount: int
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    GameProperties: Optional[List[GameProperty]] = None
    CreatorId: Optional[str] = None
    GameSessionId: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    GameSessionData: Optional[str] = None
    Location: Optional[str] = None


# This class is the input for the 'create_matchmaking_configuration' function.
class CreateMatchmakingConfigurationInput(BaseValidatorModel):
    Name: str
    RequestTimeoutSeconds: int
    AcceptanceRequired: bool
    RuleSetName: str
    Description: Optional[str] = None
    GameSessionQueueArns: Optional[List[str]] = None
    AcceptanceTimeoutSeconds: Optional[int] = None
    NotificationTarget: Optional[str] = None
    AdditionalPlayerCount: Optional[int] = None
    CustomEventData: Optional[str] = None
    GameProperties: Optional[List[GameProperty]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None
    Tags: Optional[List[Tag]] = None


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


# This class is the input for the 'update_game_session' function.
class UpdateGameSessionInput(BaseValidatorModel):
    GameSessionId: str
    MaximumPlayerSessionCount: Optional[int] = None
    Name: Optional[str] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameProperties: Optional[List[GameProperty]] = None


# This class is the input for the 'update_matchmaking_configuration' function.
class UpdateMatchmakingConfigurationInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    GameSessionQueueArns: Optional[List[str]] = None
    RequestTimeoutSeconds: Optional[int] = None
    AcceptanceTimeoutSeconds: Optional[int] = None
    AcceptanceRequired: Optional[bool] = None
    RuleSetName: Optional[str] = None
    NotificationTarget: Optional[str] = None
    AdditionalPlayerCount: Optional[int] = None
    CustomEventData: Optional[str] = None
    GameProperties: Optional[List[GameProperty]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None


# This class is the output for the 'create_location' function.
class CreateLocationOutput(BaseValidatorModel):
    Location: LocationModel
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_locations' function.
class ListLocationsOutput(BaseValidatorModel):
    Locations: List[LocationModel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_matchmaking_rule_set' function.
class CreateMatchmakingRuleSetOutput(BaseValidatorModel):
    RuleSet: MatchmakingRuleSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_matchmaking_rule_sets' function.
class DescribeMatchmakingRuleSetsOutput(BaseValidatorModel):
    RuleSets: List[MatchmakingRuleSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_player_session' function.
class CreatePlayerSessionOutput(BaseValidatorModel):
    PlayerSession: PlayerSession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_player_sessions' function.
class CreatePlayerSessionsOutput(BaseValidatorModel):
    PlayerSessions: List[PlayerSession]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_player_sessions' function.
class DescribePlayerSessionsOutput(BaseValidatorModel):
    PlayerSessions: List[PlayerSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_vpc_peering_authorization' function.
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


# This class is the input for the 'update_container_fleet' function.
class UpdateContainerFleetInput(BaseValidatorModel):
    FleetId: str
    GameServerContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRange] = None
    InstanceInboundPermissionAuthorizations: Optional[List[IpPermission]] = None
    InstanceInboundPermissionRevocations: Optional[List[IpPermission]] = None
    DeploymentConfiguration: Optional[DeploymentConfiguration] = None
    Description: Optional[str] = None
    MetricGroups: Optional[List[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicy] = None
    LogConfiguration: Optional[LogConfiguration] = None
    RemoveAttributes: Optional[List[Literal['PER_INSTANCE_CONTAINER_GROUP_DEFINITION']]] = None


# This class is the output for the 'describe_ec2_instance_limits' function.
class DescribeEC2InstanceLimitsOutput(BaseValidatorModel):
    EC2InstanceLimits: List[EC2InstanceLimit]
    ResponseMetadata: ResponseMetadata


class DescribeFleetAttributesInputPaginate(BaseValidatorModel):
    FleetIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetCapacityInputPaginate(BaseValidatorModel):
    FleetIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetUtilizationInputPaginate(BaseValidatorModel):
    FleetIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameServerInstancesInputPaginate(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameSessionDetailsInputPaginate(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGameSessionQueuesInputPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
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
    Names: Optional[List[str]] = None
    RuleSetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMatchmakingRuleSetsInputPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
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
    Filters: Optional[List[LocationFilterType]] = None
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


class DescribeFleetEventsInputPaginate(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_fleet_events' function.
class DescribeFleetEventsInput(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fleet_events' function.
class DescribeFleetEventsOutput(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fleet_location_utilization' function.
class DescribeFleetLocationUtilizationOutput(BaseValidatorModel):
    FleetUtilization: FleetUtilization
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fleet_utilization' function.
class DescribeFleetUtilizationOutput(BaseValidatorModel):
    FleetUtilization: List[FleetUtilization]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_game_server_instances' function.
class DescribeGameServerInstancesOutput(BaseValidatorModel):
    GameServerInstances: List[GameServerInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_instances' function.
class DescribeInstancesOutput(BaseValidatorModel):
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

FilterConfigurationUnion = Union[FilterConfiguration, FilterConfigurationOutput]


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

PriorityConfigurationOverrideUnion = Union[PriorityConfigurationOverride, PriorityConfigurationOverrideOutput]

PriorityConfigurationUnion = Union[PriorityConfiguration, PriorityConfigurationOutput]


# This class is the input for the 'put_scaling_policy' function.
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
    UpdateStatus: Optional[Literal['PENDING_UPDATE']] = None
    Location: Optional[str] = None


class RuntimeConfigurationOutput(BaseValidatorModel):
    ServerProcesses: Optional[List[ServerProcess]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None


class RuntimeConfiguration(BaseValidatorModel):
    ServerProcesses: Optional[List[ServerProcess]] = None
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


# This class is the output for the 'create_alias' function.
class CreateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_alias' function.
class DescribeAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_aliases' function.
class ListAliasesOutput(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_alias' function.
class UpdateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class Player(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Dict[str, AttributeValueUnion]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Dict[str, int]] = None


# This class is the output for the 'describe_compute' function.
class DescribeComputeOutput(BaseValidatorModel):
    Compute: Compute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_compute' function.
class ListComputeOutput(BaseValidatorModel):
    ComputeList: List[Compute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'register_compute' function.
class RegisterComputeOutput(BaseValidatorModel):
    Compute: Compute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_container_fleet' function.
class CreateContainerFleetOutput(BaseValidatorModel):
    ContainerFleet: ContainerFleet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_container_fleet' function.
class DescribeContainerFleetOutput(BaseValidatorModel):
    ContainerFleet: ContainerFleet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_container_fleets' function.
class ListContainerFleetsOutput(BaseValidatorModel):
    ContainerFleets: List[ContainerFleet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_container_fleet' function.
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

ContainerPortConfigurationUnion = Union[ContainerPortConfiguration, ContainerPortConfigurationOutput]


# This class is the output for the 'create_script' function.
class CreateScriptOutput(BaseValidatorModel):
    Script: Script
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_script' function.
class DescribeScriptOutput(BaseValidatorModel):
    Script: Script
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_scripts' function.
class ListScriptsOutput(BaseValidatorModel):
    Scripts: List[Script]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_script' function.
class UpdateScriptOutput(BaseValidatorModel):
    Script: Script
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_fleet' function.
class CreateFleetOutput(BaseValidatorModel):
    FleetAttributes: FleetAttributes
    LocationStates: List[LocationState]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fleet_attributes' function.
class DescribeFleetAttributesOutput(BaseValidatorModel):
    FleetAttributes: List[FleetAttributes]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fleet_location_attributes' function.
class DescribeFleetLocationAttributesOutput(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationAttributes: List[LocationAttributes]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_game_server_group' function.
class CreateGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_game_server_group' function.
class DeleteGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_game_server_group' function.
class DescribeGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_game_server_groups' function.
class ListGameServerGroupsOutput(BaseValidatorModel):
    GameServerGroups: List[GameServerGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'resume_game_server_group' function.
class ResumeGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'suspend_game_server_group' function.
class SuspendGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_game_server_group' function.
class UpdateGameServerGroupOutput(BaseValidatorModel):
    GameServerGroup: GameServerGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_game_session' function.
class CreateGameSessionOutput(BaseValidatorModel):
    GameSession: GameSession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_game_sessions' function.
class DescribeGameSessionsOutput(BaseValidatorModel):
    GameSessions: List[GameSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GameSessionDetail(BaseValidatorModel):
    GameSession: Optional[GameSession] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None


# This class is the output for the 'search_game_sessions' function.
class SearchGameSessionsOutput(BaseValidatorModel):
    GameSessions: List[GameSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'terminate_game_session' function.
class TerminateGameSessionOutput(BaseValidatorModel):
    GameSession: GameSession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_game_session' function.
class UpdateGameSessionOutput(BaseValidatorModel):
    GameSession: GameSession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_matchmaking_configuration' function.
class CreateMatchmakingConfigurationOutput(BaseValidatorModel):
    Configuration: MatchmakingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_matchmaking_configurations' function.
class DescribeMatchmakingConfigurationsOutput(BaseValidatorModel):
    Configurations: List[MatchmakingConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_matchmaking_configuration' function.
class UpdateMatchmakingConfigurationOutput(BaseValidatorModel):
    Configuration: MatchmakingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fleet_deployment' function.
class DescribeFleetDeploymentOutput(BaseValidatorModel):
    FleetDeployment: FleetDeployment
    LocationalDeployments: Dict[str, LocationalDeployment]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_fleet_deployments' function.
class ListFleetDeploymentsOutput(BaseValidatorModel):
    FleetDeployments: List[FleetDeployment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fleet_capacity' function.
class DescribeFleetCapacityOutput(BaseValidatorModel):
    FleetCapacity: List[FleetCapacity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fleet_location_capacity' function.
class DescribeFleetLocationCapacityOutput(BaseValidatorModel):
    FleetCapacity: FleetCapacity
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_game_server_group' function.
class CreateGameServerGroupInput(BaseValidatorModel):
    GameServerGroupName: str
    RoleArn: str
    MinSize: int
    MaxSize: int
    LaunchTemplate: LaunchTemplateSpecification
    InstanceDefinitions: List[InstanceDefinition]
    AutoScalingPolicy: Optional[GameServerGroupAutoScalingPolicy] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    VpcSubnets: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


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


# This class is the output for the 'describe_game_session_placement' function.
class DescribeGameSessionPlacementOutput(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_game_session_placement' function.
class StartGameSessionPlacementOutput(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_game_session_placement' function.
class StopGameSessionPlacementOutput(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_game_session_queue' function.
class CreateGameSessionQueueOutput(BaseValidatorModel):
    GameSessionQueue: GameSessionQueue
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_game_session_queues' function.
class DescribeGameSessionQueuesOutput(BaseValidatorModel):
    GameSessionQueues: List[GameSessionQueue]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_game_session_queue' function.
class UpdateGameSessionQueueOutput(BaseValidatorModel):
    GameSessionQueue: GameSessionQueue
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_access' function.
class GetInstanceAccessOutput(BaseValidatorModel):
    InstanceAccess: InstanceAccess
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_game_session_placement' function.
class StartGameSessionPlacementInput(BaseValidatorModel):
    PlacementId: str
    GameSessionQueueName: str
    MaximumPlayerSessionCount: int
    GameProperties: Optional[List[GameProperty]] = None
    GameSessionName: Optional[str] = None
    PlayerLatencies: Optional[List[PlayerLatency]] = None
    DesiredPlayerSessions: Optional[List[DesiredPlayerSession]] = None
    GameSessionData: Optional[str] = None
    PriorityConfigurationOverride: Optional[PriorityConfigurationOverrideUnion] = None


# This class is the input for the 'create_game_session_queue' function.
class CreateGameSessionQueueInput(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[List[PlayerLatencyPolicy]] = None
    Destinations: Optional[List[GameSessionQueueDestination]] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None
    PriorityConfiguration: Optional[PriorityConfigurationUnion] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_game_session_queue' function.
class UpdateGameSessionQueueInput(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[List[PlayerLatencyPolicy]] = None
    Destinations: Optional[List[GameSessionQueueDestination]] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None
    PriorityConfiguration: Optional[PriorityConfigurationUnion] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None


# This class is the output for the 'describe_scaling_policies' function.
class DescribeScalingPoliciesOutput(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_runtime_configuration' function.
class DescribeRuntimeConfigurationOutput(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_runtime_configuration' function.
class UpdateRuntimeConfigurationOutput(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationOutput
    ResponseMetadata: ResponseMetadata

RuntimeConfigurationUnion = Union[RuntimeConfiguration, RuntimeConfigurationOutput]


# This class is the output for the 'describe_vpc_peering_connections' function.
class DescribeVpcPeeringConnectionsOutput(BaseValidatorModel):
    VpcPeeringConnections: List[VpcPeeringConnection]
    ResponseMetadata: ResponseMetadata

PlayerUnion = Union[Player, PlayerOutput]


class ContainerGroupDefinition(BaseValidatorModel):
    Name: str
    ContainerGroupDefinitionArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    OperatingSystem: Optional[Literal['AMAZON_LINUX_2023']] = None
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    TotalMemoryLimitMebibytes: Optional[int] = None
    TotalVcpuLimit: Optional[float] = None
    GameServerContainerDefinition: Optional[GameServerContainerDefinition] = None
    SupportContainerDefinitions: Optional[List[SupportContainerDefinition]] = None
    VersionNumber: Optional[int] = None
    VersionDescription: Optional[str] = None
    Status: Optional[ContainerGroupDefinitionStatusType] = None
    StatusReason: Optional[str] = None


class GameServerContainerDefinitionInput(BaseValidatorModel):
    ContainerName: str
    ImageUri: str
    PortConfiguration: ContainerPortConfigurationUnion
    ServerSdkVersion: str
    DependsOn: Optional[List[ContainerDependency]] = None
    MountPoints: Optional[List[ContainerMountPoint]] = None
    EnvironmentOverride: Optional[List[ContainerEnvironment]] = None


class SupportContainerDefinitionInput(BaseValidatorModel):
    ContainerName: str
    ImageUri: str
    DependsOn: Optional[List[ContainerDependency]] = None
    MountPoints: Optional[List[ContainerMountPoint]] = None
    EnvironmentOverride: Optional[List[ContainerEnvironment]] = None
    Essential: Optional[bool] = None
    HealthCheck: Optional[ContainerHealthCheckUnion] = None
    MemoryHardLimitMebibytes: Optional[int] = None
    PortConfiguration: Optional[ContainerPortConfigurationUnion] = None
    Vcpu: Optional[float] = None


# This class is the output for the 'describe_game_session_details' function.
class DescribeGameSessionDetailsOutput(BaseValidatorModel):
    GameSessionDetails: List[GameSessionDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_matchmaking' function.
class DescribeMatchmakingOutput(BaseValidatorModel):
    TicketList: List[MatchmakingTicket]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_match_backfill' function.
class StartMatchBackfillOutput(BaseValidatorModel):
    MatchmakingTicket: MatchmakingTicket
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_matchmaking' function.
class StartMatchmakingOutput(BaseValidatorModel):
    MatchmakingTicket: MatchmakingTicket
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_fleet' function.
class CreateFleetInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ServerLaunchPath: Optional[str] = None
    ServerLaunchParameters: Optional[str] = None
    LogPaths: Optional[List[str]] = None
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    EC2InboundPermissions: Optional[List[IpPermission]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    RuntimeConfiguration: Optional[RuntimeConfigurationUnion] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicy] = None
    MetricGroups: Optional[List[str]] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    InstanceRoleArn: Optional[str] = None
    CertificateConfiguration: Optional[CertificateConfiguration] = None
    Locations: Optional[List[LocationConfiguration]] = None
    Tags: Optional[List[Tag]] = None
    ComputeType: Optional[ComputeTypeType] = None
    AnywhereConfiguration: Optional[AnywhereConfiguration] = None
    InstanceRoleCredentialsProvider: Optional[Literal['SHARED_CREDENTIAL_FILE']] = None


# This class is the input for the 'update_runtime_configuration' function.
class UpdateRuntimeConfigurationInput(BaseValidatorModel):
    FleetId: str
    RuntimeConfiguration: RuntimeConfigurationUnion


# This class is the input for the 'start_match_backfill' function.
class StartMatchBackfillInput(BaseValidatorModel):
    ConfigurationName: str
    Players: List[PlayerUnion]
    TicketId: Optional[str] = None
    GameSessionArn: Optional[str] = None


# This class is the input for the 'start_matchmaking' function.
class StartMatchmakingInput(BaseValidatorModel):
    ConfigurationName: str
    Players: List[PlayerUnion]
    TicketId: Optional[str] = None


# This class is the output for the 'create_container_group_definition' function.
class CreateContainerGroupDefinitionOutput(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinition
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_container_group_definition' function.
class DescribeContainerGroupDefinitionOutput(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinition
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_container_group_definition_versions' function.
class ListContainerGroupDefinitionVersionsOutput(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_container_group_definitions' function.
class ListContainerGroupDefinitionsOutput(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_container_group_definition' function.
class UpdateContainerGroupDefinitionOutput(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinition
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_container_group_definition' function.
class CreateContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    TotalMemoryLimitMebibytes: int
    TotalVcpuLimit: float
    OperatingSystem: Literal['AMAZON_LINUX_2023']
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionInput] = None
    SupportContainerDefinitions: Optional[List[SupportContainerDefinitionInput]] = None
    VersionDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_container_group_definition' function.
class UpdateContainerGroupDefinitionInput(BaseValidatorModel):
    Name: str
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionInput] = None
    SupportContainerDefinitions: Optional[List[SupportContainerDefinitionInput]] = None
    TotalMemoryLimitMebibytes: Optional[int] = None
    TotalVcpuLimit: Optional[float] = None
    VersionDescription: Optional[str] = None
    SourceVersionNumber: Optional[int] = None
    OperatingSystem: Optional[Literal['AMAZON_LINUX_2023']] = None