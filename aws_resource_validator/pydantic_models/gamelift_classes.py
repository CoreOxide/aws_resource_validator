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
from aws_resource_validator.pydantic_models.gamelift_constants import *

class AcceptMatchInputRequestTypeDef(BaseModel):
    TicketId: str
    PlayerIds: Sequence[str]
    AcceptanceType: AcceptanceTypeType

class RoutingStrategyTypeDef(BaseModel):
    Type: Optional[RoutingStrategyTypeType] = None
    FleetId: Optional[str] = None
    Message: Optional[str] = None

class AnywhereConfigurationTypeDef(BaseModel):
    Cost: str

class AttributeValueOutputTypeDef(BaseModel):
    S: Optional[str] = None
    N: Optional[float] = None
    SL: Optional[List[str]] = None
    SDM: Optional[Dict[str, float]] = None

class AttributeValueTypeDef(BaseModel):
    S: Optional[str] = None
    N: Optional[float] = None
    SL: Optional[Sequence[str]] = None
    SDM: Optional[Mapping[str, float]] = None

class AwsCredentialsTypeDef(BaseModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None

class BuildTypeDef(BaseModel):
    BuildId: Optional[str] = None
    BuildArn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[BuildStatusType] = None
    SizeOnDisk: Optional[int] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    CreationTime: Optional[datetime] = None
    ServerSdkVersion: Optional[str] = None

class CertificateConfigurationTypeDef(BaseModel):
    CertificateType: CertificateTypeType

class ClaimFilterOptionTypeDef(BaseModel):
    InstanceStatuses: Optional[Sequence[FilterInstanceStatusType]] = None

class GameServerTypeDef(BaseModel):
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConnectionPortRangeTypeDef(BaseModel):
    FromPort: int
    ToPort: int

class ContainerPortMappingTypeDef(BaseModel):
    ContainerPort: Optional[int] = None
    ConnectionPort: Optional[int] = None
    Protocol: Optional[IpProtocolType] = None

class ContainerDependencyTypeDef(BaseModel):
    ContainerName: str
    Condition: ContainerDependencyConditionType

class ContainerEnvironmentTypeDef(BaseModel):
    Name: str
    Value: str

class ContainerHealthCheckTypeDef(BaseModel):
    Command: Sequence[str]
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None

class ContainerMemoryLimitsTypeDef(BaseModel):
    SoftLimit: Optional[int] = None
    HardLimit: Optional[int] = None

class ContainerHealthCheckOutputTypeDef(BaseModel):
    Command: List[str]
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None

class ContainerGroupDefinitionPropertyTypeDef(BaseModel):
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    ContainerGroupDefinitionName: Optional[str] = None

class ContainerGroupsPerInstanceTypeDef(BaseModel):
    DesiredReplicaContainerGroupsPerInstance: Optional[int] = None
    MaxReplicaContainerGroupsPerInstance: Optional[int] = None

class ContainerPortRangeTypeDef(BaseModel):
    FromPort: int
    ToPort: int
    Protocol: IpProtocolType

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class S3LocationTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    RoleArn: Optional[str] = None
    ObjectVersion: Optional[str] = None

class IpPermissionTypeDef(BaseModel):
    FromPort: int
    ToPort: int
    IpRange: str
    Protocol: IpProtocolType

class LocationConfigurationTypeDef(BaseModel):
    Location: str

class ResourceCreationLimitPolicyTypeDef(BaseModel):
    NewGameSessionsPerCreator: Optional[int] = None
    PolicyPeriodInMinutes: Optional[int] = None

class LocationStateTypeDef(BaseModel):
    Location: Optional[str] = None
    Status: Optional[FleetStatusType] = None

class InstanceDefinitionTypeDef(BaseModel):
    InstanceType: GameServerGroupInstanceTypeType
    WeightedCapacity: Optional[str] = None

class LaunchTemplateSpecificationTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class GamePropertyTypeDef(BaseModel):
    Key: str
    Value: str

class FilterConfigurationTypeDef(BaseModel):
    AllowedLocations: Optional[Sequence[str]] = None

class GameSessionQueueDestinationTypeDef(BaseModel):
    DestinationArn: Optional[str] = None

class PlayerLatencyPolicyTypeDef(BaseModel):
    MaximumIndividualPlayerLatencyMilliseconds: Optional[int] = None
    PolicyDurationSeconds: Optional[int] = None

class PriorityConfigurationTypeDef(BaseModel):
    PriorityOrder: Optional[Sequence[PriorityTypeType]] = None
    LocationOrder: Optional[Sequence[str]] = None

class LocationModelTypeDef(BaseModel):
    LocationName: Optional[str] = None
    LocationArn: Optional[str] = None

class MatchmakingRuleSetTypeDef(BaseModel):
    RuleSetBody: str
    RuleSetName: Optional[str] = None
    RuleSetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None

class CreatePlayerSessionInputRequestTypeDef(BaseModel):
    GameSessionId: str
    PlayerId: str
    PlayerData: Optional[str] = None

class PlayerSessionTypeDef(BaseModel):
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

class CreatePlayerSessionsInputRequestTypeDef(BaseModel):
    GameSessionId: str
    PlayerIds: Sequence[str]
    PlayerDataMap: Optional[Mapping[str, str]] = None

class CreateVpcPeeringAuthorizationInputRequestTypeDef(BaseModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str

class VpcPeeringAuthorizationTypeDef(BaseModel):
    GameLiftAwsAccountId: Optional[str] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None

class CreateVpcPeeringConnectionInputRequestTypeDef(BaseModel):
    FleetId: str
    PeerVpcAwsAccountId: str
    PeerVpcId: str

class DeleteAliasInputRequestTypeDef(BaseModel):
    AliasId: str

class DeleteBuildInputRequestTypeDef(BaseModel):
    BuildId: str

class DeleteContainerGroupDefinitionInputRequestTypeDef(BaseModel):
    Name: str

class DeleteFleetInputRequestTypeDef(BaseModel):
    FleetId: str

class DeleteFleetLocationsInputRequestTypeDef(BaseModel):
    FleetId: str
    Locations: Sequence[str]

class DeleteGameServerGroupInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    DeleteOption: Optional[GameServerGroupDeleteOptionType] = None

class DeleteGameSessionQueueInputRequestTypeDef(BaseModel):
    Name: str

class DeleteLocationInputRequestTypeDef(BaseModel):
    LocationName: str

class DeleteMatchmakingConfigurationInputRequestTypeDef(BaseModel):
    Name: str

class DeleteMatchmakingRuleSetInputRequestTypeDef(BaseModel):
    Name: str

class DeleteScalingPolicyInputRequestTypeDef(BaseModel):
    Name: str
    FleetId: str

class DeleteScriptInputRequestTypeDef(BaseModel):
    ScriptId: str

class DeleteVpcPeeringAuthorizationInputRequestTypeDef(BaseModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str

class DeleteVpcPeeringConnectionInputRequestTypeDef(BaseModel):
    FleetId: str
    VpcPeeringConnectionId: str

class DeregisterComputeInputRequestTypeDef(BaseModel):
    FleetId: str
    ComputeName: str

class DeregisterGameServerInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    GameServerId: str

class DescribeAliasInputRequestTypeDef(BaseModel):
    AliasId: str

class DescribeBuildInputRequestTypeDef(BaseModel):
    BuildId: str

class DescribeComputeInputRequestTypeDef(BaseModel):
    FleetId: str
    ComputeName: str

class DescribeContainerGroupDefinitionInputRequestTypeDef(BaseModel):
    Name: str

class DescribeEC2InstanceLimitsInputRequestTypeDef(BaseModel):
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    Location: Optional[str] = None

class EC2InstanceLimitTypeDef(BaseModel):
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    CurrentInstances: Optional[int] = None
    InstanceLimit: Optional[int] = None
    Location: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeFleetAttributesInputRequestTypeDef(BaseModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetCapacityInputRequestTypeDef(BaseModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class EventTypeDef(BaseModel):
    EventId: Optional[str] = None
    ResourceId: Optional[str] = None
    EventCode: Optional[EventCodeType] = None
    Message: Optional[str] = None
    EventTime: Optional[datetime] = None
    PreSignedLogUrl: Optional[str] = None
    Count: Optional[int] = None

class DescribeFleetLocationAttributesInputRequestTypeDef(BaseModel):
    FleetId: str
    Locations: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetLocationCapacityInputRequestTypeDef(BaseModel):
    FleetId: str
    Location: str

class DescribeFleetLocationUtilizationInputRequestTypeDef(BaseModel):
    FleetId: str
    Location: str

class FleetUtilizationTypeDef(BaseModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    ActiveServerProcessCount: Optional[int] = None
    ActiveGameSessionCount: Optional[int] = None
    CurrentPlayerSessionCount: Optional[int] = None
    MaximumPlayerSessionCount: Optional[int] = None
    Location: Optional[str] = None

class DescribeFleetPortSettingsInputRequestTypeDef(BaseModel):
    FleetId: str
    Location: Optional[str] = None

class DescribeFleetUtilizationInputRequestTypeDef(BaseModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeGameServerGroupInputRequestTypeDef(BaseModel):
    GameServerGroupName: str

class DescribeGameServerInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    GameServerId: str

class DescribeGameServerInstancesInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GameServerInstanceTypeDef(BaseModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[GameServerInstanceStatusType] = None

class DescribeGameSessionDetailsInputRequestTypeDef(BaseModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeGameSessionPlacementInputRequestTypeDef(BaseModel):
    PlacementId: str

class DescribeGameSessionQueuesInputRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeGameSessionsInputRequestTypeDef(BaseModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstancesInputRequestTypeDef(BaseModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None

class InstanceTypeDef(BaseModel):
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

class DescribeMatchmakingConfigurationsInputRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMatchmakingInputRequestTypeDef(BaseModel):
    TicketIds: Sequence[str]

class DescribeMatchmakingRuleSetsInputRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePlayerSessionsInputRequestTypeDef(BaseModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeRuntimeConfigurationInputRequestTypeDef(BaseModel):
    FleetId: str

class DescribeScalingPoliciesInputRequestTypeDef(BaseModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None

class DescribeScriptInputRequestTypeDef(BaseModel):
    ScriptId: str

class DescribeVpcPeeringConnectionsInputRequestTypeDef(BaseModel):
    FleetId: Optional[str] = None

class DesiredPlayerSessionTypeDef(BaseModel):
    PlayerId: Optional[str] = None
    PlayerData: Optional[str] = None

class EC2InstanceCountsTypeDef(BaseModel):
    DESIRED: Optional[int] = None
    MINIMUM: Optional[int] = None
    MAXIMUM: Optional[int] = None
    PENDING: Optional[int] = None
    ACTIVE: Optional[int] = None
    IDLE: Optional[int] = None
    TERMINATING: Optional[int] = None

class FilterConfigurationExtraOutputTypeDef(BaseModel):
    AllowedLocations: Optional[List[str]] = None

class FilterConfigurationOutputTypeDef(BaseModel):
    AllowedLocations: Optional[List[str]] = None

class ReplicaContainerGroupCountsTypeDef(BaseModel):
    PENDING: Optional[int] = None
    ACTIVE: Optional[int] = None
    IDLE: Optional[int] = None
    TERMINATING: Optional[int] = None

class TargetTrackingConfigurationTypeDef(BaseModel):
    TargetValue: float

class MatchedPlayerSessionTypeDef(BaseModel):
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None

class PlacedPlayerSessionTypeDef(BaseModel):
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None

class PlayerLatencyTypeDef(BaseModel):
    PlayerId: Optional[str] = None
    RegionIdentifier: Optional[str] = None
    LatencyInMilliseconds: Optional[float] = None

class PriorityConfigurationOutputTypeDef(BaseModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None

class GetComputeAccessInputRequestTypeDef(BaseModel):
    FleetId: str
    ComputeName: str

class GetComputeAuthTokenInputRequestTypeDef(BaseModel):
    FleetId: str
    ComputeName: str

class GetGameSessionLogUrlInputRequestTypeDef(BaseModel):
    GameSessionId: str

class GetInstanceAccessInputRequestTypeDef(BaseModel):
    FleetId: str
    InstanceId: str

class InstanceCredentialsTypeDef(BaseModel):
    UserName: Optional[str] = None
    Secret: Optional[str] = None

class ListAliasesInputRequestTypeDef(BaseModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListBuildsInputRequestTypeDef(BaseModel):
    Status: Optional[BuildStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListComputeInputRequestTypeDef(BaseModel):
    FleetId: str
    Location: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListContainerGroupDefinitionsInputRequestTypeDef(BaseModel):
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListFleetsInputRequestTypeDef(BaseModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListGameServerGroupsInputRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListGameServersInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListLocationsInputRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListScriptsInputRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class PriorityConfigurationExtraOutputTypeDef(BaseModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None

class TargetConfigurationTypeDef(BaseModel):
    TargetValue: float

class RegisterComputeInputRequestTypeDef(BaseModel):
    FleetId: str
    ComputeName: str
    CertificatePath: Optional[str] = None
    DnsName: Optional[str] = None
    IpAddress: Optional[str] = None
    Location: Optional[str] = None

class RegisterGameServerInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    GameServerId: str
    InstanceId: str
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None

class RequestUploadCredentialsInputRequestTypeDef(BaseModel):
    BuildId: str

class ResolveAliasInputRequestTypeDef(BaseModel):
    AliasId: str

class ResumeGameServerGroupInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    ResumeActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]

class ServerProcessTypeDef(BaseModel):
    LaunchPath: str
    ConcurrentExecutions: int
    Parameters: Optional[str] = None

class SearchGameSessionsInputRequestTypeDef(BaseModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class StartFleetActionsInputRequestTypeDef(BaseModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None

class StopFleetActionsInputRequestTypeDef(BaseModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None

class StopGameSessionPlacementInputRequestTypeDef(BaseModel):
    PlacementId: str

class StopMatchmakingInputRequestTypeDef(BaseModel):
    TicketId: str

class SuspendGameServerGroupInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    SuspendActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateBuildInputRequestTypeDef(BaseModel):
    BuildId: str
    Name: Optional[str] = None
    Version: Optional[str] = None

class UpdateFleetCapacityInputRequestTypeDef(BaseModel):
    FleetId: str
    DesiredInstances: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Location: Optional[str] = None

class UpdateGameServerInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    GameServerId: str
    GameServerData: Optional[str] = None
    UtilizationStatus: Optional[GameServerUtilizationStatusType] = None
    HealthCheck: Optional[Literal["HEALTHY"]] = None

class ValidateMatchmakingRuleSetInputRequestTypeDef(BaseModel):
    RuleSetBody: str

class VpcPeeringConnectionStatusTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class AliasTypeDef(BaseModel):
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    AliasArn: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategyTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class UpdateAliasInputRequestTypeDef(BaseModel):
    AliasId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategyTypeDef] = None

class PlayerOutputTypeDef(BaseModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Dict[str, AttributeValueOutputTypeDef]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Dict[str, int]] = None

class PlayerTypeDef(BaseModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Mapping[str, AttributeValueTypeDef]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Mapping[str, int]] = None

class ClaimGameServerInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    GameServerId: Optional[str] = None
    GameServerData: Optional[str] = None
    FilterOption: Optional[ClaimFilterOptionTypeDef] = None

class ClaimGameServerOutputTypeDef(BaseModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBuildOutputTypeDef(BaseModel):
    Build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameServerOutputTypeDef(BaseModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetComputeAccessOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    Credentials: AwsCredentialsTypeDef
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComputeAuthTokenOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    AuthToken: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetGameSessionLogUrlOutputTypeDef(BaseModel):
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildsOutputTypeDef(BaseModel):
    Builds: List[BuildTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFleetsOutputTypeDef(BaseModel):
    FleetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListGameServersOutputTypeDef(BaseModel):
    GameServers: List[GameServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutScalingPolicyOutputTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterGameServerOutputTypeDef(BaseModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveAliasOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFleetActionsOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopFleetActionsOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBuildOutputTypeDef(BaseModel):
    Build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetAttributesOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetCapacityOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetPortSettingsOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGameServerOutputTypeDef(BaseModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateMatchmakingRuleSetOutputTypeDef(BaseModel):
    Valid: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerGroupsConfigurationTypeDef(BaseModel):
    ContainerGroupDefinitionNames: Sequence[str]
    ConnectionPortRange: ConnectionPortRangeTypeDef
    DesiredReplicaContainerGroupsPerInstance: Optional[int] = None

class ContainerAttributesTypeDef(BaseModel):
    ContainerPortMappings: Optional[List[ContainerPortMappingTypeDef]] = None

class ContainerGroupsAttributesTypeDef(BaseModel):
    ContainerGroupDefinitionProperties: Optional[       List[ContainerGroupDefinitionPropertyTypeDef]     ] = None
    ConnectionPortRange: Optional[ConnectionPortRangeTypeDef] = None
    ContainerGroupsPerInstance: Optional[ContainerGroupsPerInstanceTypeDef] = None

class ContainerPortConfigurationOutputTypeDef(BaseModel):
    ContainerPortRanges: List[ContainerPortRangeTypeDef]

class ContainerPortConfigurationTypeDef(BaseModel):
    ContainerPortRanges: Sequence[ContainerPortRangeTypeDef]

class CreateAliasInputRequestTypeDef(BaseModel):
    Name: str
    RoutingStrategy: RoutingStrategyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateLocationInputRequestTypeDef(BaseModel):
    LocationName: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMatchmakingRuleSetInputRequestTypeDef(BaseModel):
    Name: str
    RuleSetBody: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateBuildInputRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ServerSdkVersion: Optional[str] = None

class CreateBuildOutputTypeDef(BaseModel):
    Build: BuildTypeDef
    UploadCredentials: AwsCredentialsTypeDef
    StorageLocation: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScriptInputRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    ZipFile: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class RequestUploadCredentialsOutputTypeDef(BaseModel):
    UploadCredentials: AwsCredentialsTypeDef
    StorageLocation: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScriptTypeDef(BaseModel):
    ScriptId: Optional[str] = None
    ScriptArn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None
    SizeOnDisk: Optional[int] = None
    CreationTime: Optional[datetime] = None
    StorageLocation: Optional[S3LocationTypeDef] = None

class UpdateScriptInputRequestTypeDef(BaseModel):
    ScriptId: str
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    ZipFile: Optional[BlobTypeDef] = None

class DescribeFleetPortSettingsOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    InboundPermissions: List[IpPermissionTypeDef]
    UpdateStatus: Literal["PENDING_UPDATE"]
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetPortSettingsInputRequestTypeDef(BaseModel):
    FleetId: str
    InboundPermissionAuthorizations: Optional[Sequence[IpPermissionTypeDef]] = None
    InboundPermissionRevocations: Optional[Sequence[IpPermissionTypeDef]] = None

class CreateFleetLocationsInputRequestTypeDef(BaseModel):
    FleetId: str
    Locations: Sequence[LocationConfigurationTypeDef]

class UpdateFleetAttributesInputRequestTypeDef(BaseModel):
    FleetId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicyTypeDef] = None
    MetricGroups: Optional[Sequence[str]] = None
    AnywhereConfiguration: Optional[AnywhereConfigurationTypeDef] = None

class CreateFleetLocationsOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFleetLocationsOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LocationAttributesTypeDef(BaseModel):
    LocationState: Optional[LocationStateTypeDef] = None
    StoppedActions: Optional[List[Literal["AUTO_SCALING"]]] = None
    UpdateStatus: Optional[Literal["PENDING_UPDATE"]] = None

class GameServerGroupTypeDef(BaseModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[List[InstanceDefinitionTypeDef]] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    AutoScalingGroupArn: Optional[str] = None
    Status: Optional[GameServerGroupStatusType] = None
    StatusReason: Optional[str] = None
    SuspendedActions: Optional[List[Literal["REPLACE_INSTANCE_TYPES"]]] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class UpdateGameServerGroupInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[Sequence[InstanceDefinitionTypeDef]] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None

class CreateGameSessionInputRequestTypeDef(BaseModel):
    MaximumPlayerSessionCount: int
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None
    CreatorId: Optional[str] = None
    GameSessionId: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    GameSessionData: Optional[str] = None
    Location: Optional[str] = None

class CreateMatchmakingConfigurationInputRequestTypeDef(BaseModel):
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
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GameSessionTypeDef(BaseModel):
    GameSessionId: Optional[str] = None
    Name: Optional[str] = None
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    TerminationTime: Optional[datetime] = None
    CurrentPlayerSessionCount: Optional[int] = None
    MaximumPlayerSessionCount: Optional[int] = None
    Status: Optional[GameSessionStatusType] = None
    StatusReason: Optional[Literal["INTERRUPTED"]] = None
    GameProperties: Optional[List[GamePropertyTypeDef]] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    CreatorId: Optional[str] = None
    GameSessionData: Optional[str] = None
    MatchmakerData: Optional[str] = None
    Location: Optional[str] = None

class MatchmakingConfigurationTypeDef(BaseModel):
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
    GameProperties: Optional[List[GamePropertyTypeDef]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None

class UpdateGameSessionInputRequestTypeDef(BaseModel):
    GameSessionId: str
    MaximumPlayerSessionCount: Optional[int] = None
    Name: Optional[str] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None

class UpdateMatchmakingConfigurationInputRequestTypeDef(BaseModel):
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
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None
    GameSessionData: Optional[str] = None
    BackfillMode: Optional[BackfillModeType] = None
    FlexMatchMode: Optional[FlexMatchModeType] = None

class CreateGameSessionQueueInputRequestTypeDef(BaseModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateGameSessionQueueInputRequestTypeDef(BaseModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None

class CreateLocationOutputTypeDef(BaseModel):
    Location: LocationModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLocationsOutputTypeDef(BaseModel):
    Locations: List[LocationModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateMatchmakingRuleSetOutputTypeDef(BaseModel):
    RuleSet: MatchmakingRuleSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMatchmakingRuleSetsOutputTypeDef(BaseModel):
    RuleSets: List[MatchmakingRuleSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePlayerSessionOutputTypeDef(BaseModel):
    PlayerSession: PlayerSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePlayerSessionsOutputTypeDef(BaseModel):
    PlayerSessions: List[PlayerSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePlayerSessionsOutputTypeDef(BaseModel):
    PlayerSessions: List[PlayerSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateVpcPeeringAuthorizationOutputTypeDef(BaseModel):
    VpcPeeringAuthorization: VpcPeeringAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcPeeringAuthorizationsOutputTypeDef(BaseModel):
    VpcPeeringAuthorizations: List[VpcPeeringAuthorizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEC2InstanceLimitsOutputTypeDef(BaseModel):
    EC2InstanceLimits: List[EC2InstanceLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAttributesInputDescribeFleetAttributesPaginateTypeDef(BaseModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetCapacityInputDescribeFleetCapacityPaginateTypeDef(BaseModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateTypeDef(BaseModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateTypeDef(BaseModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateTypeDef(BaseModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameSessionsInputDescribeGameSessionsPaginateTypeDef(BaseModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancesInputDescribeInstancesPaginateTypeDef(BaseModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePlayerSessionsInputDescribePlayerSessionsPaginateTypeDef(BaseModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateTypeDef(BaseModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAliasesInputListAliasesPaginateTypeDef(BaseModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildsInputListBuildsPaginateTypeDef(BaseModel):
    Status: Optional[BuildStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComputeInputListComputePaginateTypeDef(BaseModel):
    FleetId: str
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContainerGroupDefinitionsInputListContainerGroupDefinitionsPaginateTypeDef(BaseModel):
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsInputListFleetsPaginateTypeDef(BaseModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGameServerGroupsInputListGameServerGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGameServersInputListGameServersPaginateTypeDef(BaseModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLocationsInputListLocationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScriptsInputListScriptsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchGameSessionsInputSearchGameSessionsPaginateTypeDef(BaseModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetEventsInputDescribeFleetEventsPaginateTypeDef(BaseModel):
    FleetId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetEventsInputRequestTypeDef(BaseModel):
    FleetId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetEventsOutputTypeDef(BaseModel):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetLocationUtilizationOutputTypeDef(BaseModel):
    FleetUtilization: FleetUtilizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetUtilizationOutputTypeDef(BaseModel):
    FleetUtilization: List[FleetUtilizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeGameServerInstancesOutputTypeDef(BaseModel):
    GameServerInstances: List[GameServerInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancesOutputTypeDef(BaseModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FleetCapacityTypeDef(BaseModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    InstanceType: Optional[EC2InstanceTypeType] = None
    InstanceCounts: Optional[EC2InstanceCountsTypeDef] = None
    Location: Optional[str] = None
    ReplicaContainerGroupCounts: Optional[ReplicaContainerGroupCountsTypeDef] = None

class GameServerGroupAutoScalingPolicyTypeDef(BaseModel):
    TargetTrackingConfiguration: TargetTrackingConfigurationTypeDef
    EstimatedInstanceWarmup: Optional[int] = None

class GameSessionConnectionInfoTypeDef(BaseModel):
    GameSessionArn: Optional[str] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    MatchedPlayerSessions: Optional[List[MatchedPlayerSessionTypeDef]] = None

class GameSessionPlacementTypeDef(BaseModel):
    PlacementId: Optional[str] = None
    GameSessionQueueName: Optional[str] = None
    Status: Optional[GameSessionPlacementStateType] = None
    GameProperties: Optional[List[GamePropertyTypeDef]] = None
    MaximumPlayerSessionCount: Optional[int] = None
    GameSessionName: Optional[str] = None
    GameSessionId: Optional[str] = None
    GameSessionArn: Optional[str] = None
    GameSessionRegion: Optional[str] = None
    PlayerLatencies: Optional[List[PlayerLatencyTypeDef]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    PlacedPlayerSessions: Optional[List[PlacedPlayerSessionTypeDef]] = None
    GameSessionData: Optional[str] = None
    MatchmakerData: Optional[str] = None

class StartGameSessionPlacementInputRequestTypeDef(BaseModel):
    PlacementId: str
    GameSessionQueueName: str
    MaximumPlayerSessionCount: int
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None
    GameSessionName: Optional[str] = None
    PlayerLatencies: Optional[Sequence[PlayerLatencyTypeDef]] = None
    DesiredPlayerSessions: Optional[Sequence[DesiredPlayerSessionTypeDef]] = None
    GameSessionData: Optional[str] = None

class GameSessionQueueTypeDef(BaseModel):
    Name: Optional[str] = None
    GameSessionQueueArn: Optional[str] = None
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[List[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[List[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationOutputTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None

class InstanceAccessTypeDef(BaseModel):
    FleetId: Optional[str] = None
    InstanceId: Optional[str] = None
    IpAddress: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Credentials: Optional[InstanceCredentialsTypeDef] = None

class PutScalingPolicyInputRequestTypeDef(BaseModel):
    Name: str
    FleetId: str
    MetricName: MetricNameType
    ScalingAdjustment: Optional[int] = None
    ScalingAdjustmentType: Optional[ScalingAdjustmentTypeType] = None
    Threshold: Optional[float] = None
    ComparisonOperator: Optional[ComparisonOperatorTypeType] = None
    EvaluationPeriods: Optional[int] = None
    PolicyType: Optional[PolicyTypeType] = None
    TargetConfiguration: Optional[TargetConfigurationTypeDef] = None

class ScalingPolicyTypeDef(BaseModel):
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
    TargetConfiguration: Optional[TargetConfigurationTypeDef] = None
    UpdateStatus: Optional[Literal["PENDING_UPDATE"]] = None
    Location: Optional[str] = None

class RuntimeConfigurationOutputTypeDef(BaseModel):
    ServerProcesses: Optional[List[ServerProcessTypeDef]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None

class RuntimeConfigurationTypeDef(BaseModel):
    ServerProcesses: Optional[Sequence[ServerProcessTypeDef]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None

class VpcPeeringConnectionTypeDef(BaseModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    IpV4CidrBlock: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    Status: Optional[VpcPeeringConnectionStatusTypeDef] = None
    PeerVpcId: Optional[str] = None
    GameLiftVpcId: Optional[str] = None

class CreateAliasOutputTypeDef(BaseModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAliasOutputTypeDef(BaseModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesOutputTypeDef(BaseModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateAliasOutputTypeDef(BaseModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComputeTypeDef(BaseModel):
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
    ContainerAttributes: Optional[ContainerAttributesTypeDef] = None

class FleetAttributesTypeDef(BaseModel):
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
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicyTypeDef] = None
    MetricGroups: Optional[List[str]] = None
    StoppedActions: Optional[List[Literal["AUTO_SCALING"]]] = None
    InstanceRoleArn: Optional[str] = None
    CertificateConfiguration: Optional[CertificateConfigurationTypeDef] = None
    ComputeType: Optional[ComputeTypeType] = None
    AnywhereConfiguration: Optional[AnywhereConfigurationTypeDef] = None
    InstanceRoleCredentialsProvider: Optional[Literal["SHARED_CREDENTIAL_FILE"]] = None
    ContainerGroupsAttributes: Optional[ContainerGroupsAttributesTypeDef] = None

class ContainerDefinitionTypeDef(BaseModel):
    ContainerName: str
    ImageUri: str
    ResolvedImageDigest: Optional[str] = None
    MemoryLimits: Optional[ContainerMemoryLimitsTypeDef] = None
    PortConfiguration: Optional[ContainerPortConfigurationOutputTypeDef] = None
    Cpu: Optional[int] = None
    HealthCheck: Optional[ContainerHealthCheckOutputTypeDef] = None
    Command: Optional[List[str]] = None
    Essential: Optional[bool] = None
    EntryPoint: Optional[List[str]] = None
    WorkingDirectory: Optional[str] = None
    Environment: Optional[List[ContainerEnvironmentTypeDef]] = None
    DependsOn: Optional[List[ContainerDependencyTypeDef]] = None

class ContainerDefinitionInputTypeDef(BaseModel):
    ContainerName: str
    ImageUri: str
    MemoryLimits: Optional[ContainerMemoryLimitsTypeDef] = None
    PortConfiguration: Optional[ContainerPortConfigurationTypeDef] = None
    Cpu: Optional[int] = None
    HealthCheck: Optional[ContainerHealthCheckTypeDef] = None
    Command: Optional[Sequence[str]] = None
    Essential: Optional[bool] = None
    EntryPoint: Optional[Sequence[str]] = None
    WorkingDirectory: Optional[str] = None
    Environment: Optional[Sequence[ContainerEnvironmentTypeDef]] = None
    DependsOn: Optional[Sequence[ContainerDependencyTypeDef]] = None

class CreateScriptOutputTypeDef(BaseModel):
    Script: ScriptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScriptOutputTypeDef(BaseModel):
    Script: ScriptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListScriptsOutputTypeDef(BaseModel):
    Scripts: List[ScriptTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateScriptOutputTypeDef(BaseModel):
    Script: ScriptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetLocationAttributesOutputTypeDef(BaseModel):
    FleetId: str
    FleetArn: str
    LocationAttributes: List[LocationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGameServerGroupOutputTypeDef(BaseModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGameServerGroupOutputTypeDef(BaseModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameServerGroupOutputTypeDef(BaseModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGameServerGroupsOutputTypeDef(BaseModel):
    GameServerGroups: List[GameServerGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResumeGameServerGroupOutputTypeDef(BaseModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SuspendGameServerGroupOutputTypeDef(BaseModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGameServerGroupOutputTypeDef(BaseModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGameSessionOutputTypeDef(BaseModel):
    GameSession: GameSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameSessionsOutputTypeDef(BaseModel):
    GameSessions: List[GameSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GameSessionDetailTypeDef(BaseModel):
    GameSession: Optional[GameSessionTypeDef] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None

class SearchGameSessionsOutputTypeDef(BaseModel):
    GameSessions: List[GameSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGameSessionOutputTypeDef(BaseModel):
    GameSession: GameSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMatchmakingConfigurationOutputTypeDef(BaseModel):
    Configuration: MatchmakingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMatchmakingConfigurationsOutputTypeDef(BaseModel):
    Configurations: List[MatchmakingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateMatchmakingConfigurationOutputTypeDef(BaseModel):
    Configuration: MatchmakingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetCapacityOutputTypeDef(BaseModel):
    FleetCapacity: List[FleetCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetLocationCapacityOutputTypeDef(BaseModel):
    FleetCapacity: FleetCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGameServerGroupInputRequestTypeDef(BaseModel):
    GameServerGroupName: str
    RoleArn: str
    MinSize: int
    MaxSize: int
    LaunchTemplate: LaunchTemplateSpecificationTypeDef
    InstanceDefinitions: Sequence[InstanceDefinitionTypeDef]
    AutoScalingPolicy: Optional[GameServerGroupAutoScalingPolicyTypeDef] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    VpcSubnets: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MatchmakingTicketTypeDef(BaseModel):
    TicketId: Optional[str] = None
    ConfigurationName: Optional[str] = None
    ConfigurationArn: Optional[str] = None
    Status: Optional[MatchmakingConfigurationStatusType] = None
    StatusReason: Optional[str] = None
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Players: Optional[List[PlayerOutputTypeDef]] = None
    GameSessionConnectionInfo: Optional[GameSessionConnectionInfoTypeDef] = None
    EstimatedWaitTime: Optional[int] = None

class DescribeGameSessionPlacementOutputTypeDef(BaseModel):
    GameSessionPlacement: GameSessionPlacementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartGameSessionPlacementOutputTypeDef(BaseModel):
    GameSessionPlacement: GameSessionPlacementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopGameSessionPlacementOutputTypeDef(BaseModel):
    GameSessionPlacement: GameSessionPlacementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGameSessionQueueOutputTypeDef(BaseModel):
    GameSessionQueue: GameSessionQueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameSessionQueuesOutputTypeDef(BaseModel):
    GameSessionQueues: List[GameSessionQueueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGameSessionQueueOutputTypeDef(BaseModel):
    GameSessionQueue: GameSessionQueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceAccessOutputTypeDef(BaseModel):
    InstanceAccess: InstanceAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPoliciesOutputTypeDef(BaseModel):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRuntimeConfigurationOutputTypeDef(BaseModel):
    RuntimeConfiguration: RuntimeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuntimeConfigurationOutputTypeDef(BaseModel):
    RuntimeConfiguration: RuntimeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetInputRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ServerLaunchPath: Optional[str] = None
    ServerLaunchParameters: Optional[str] = None
    LogPaths: Optional[Sequence[str]] = None
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    EC2InboundPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    RuntimeConfiguration: Optional[RuntimeConfigurationTypeDef] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicyTypeDef] = None
    MetricGroups: Optional[Sequence[str]] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    InstanceRoleArn: Optional[str] = None
    CertificateConfiguration: Optional[CertificateConfigurationTypeDef] = None
    Locations: Optional[Sequence[LocationConfigurationTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ComputeType: Optional[ComputeTypeType] = None
    AnywhereConfiguration: Optional[AnywhereConfigurationTypeDef] = None
    InstanceRoleCredentialsProvider: Optional[Literal["SHARED_CREDENTIAL_FILE"]] = None
    ContainerGroupsConfiguration: Optional[ContainerGroupsConfigurationTypeDef] = None

class UpdateRuntimeConfigurationInputRequestTypeDef(BaseModel):
    FleetId: str
    RuntimeConfiguration: RuntimeConfigurationTypeDef

class DescribeVpcPeeringConnectionsOutputTypeDef(BaseModel):
    VpcPeeringConnections: List[VpcPeeringConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchBackfillInputRequestTypeDef(BaseModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnionTypeDef]
    TicketId: Optional[str] = None
    GameSessionArn: Optional[str] = None

class StartMatchmakingInputRequestTypeDef(BaseModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnionTypeDef]
    TicketId: Optional[str] = None

class DescribeComputeOutputTypeDef(BaseModel):
    Compute: ComputeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListComputeOutputTypeDef(BaseModel):
    ComputeList: List[ComputeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterComputeOutputTypeDef(BaseModel):
    Compute: ComputeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetOutputTypeDef(BaseModel):
    FleetAttributes: FleetAttributesTypeDef
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAttributesOutputTypeDef(BaseModel):
    FleetAttributes: List[FleetAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContainerGroupDefinitionTypeDef(BaseModel):
    ContainerGroupDefinitionArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    OperatingSystem: Optional[Literal["AMAZON_LINUX_2023"]] = None
    Name: Optional[str] = None
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    TotalMemoryLimit: Optional[int] = None
    TotalCpuLimit: Optional[int] = None
    ContainerDefinitions: Optional[List[ContainerDefinitionTypeDef]] = None
    Status: Optional[ContainerGroupDefinitionStatusType] = None
    StatusReason: Optional[str] = None

class CreateContainerGroupDefinitionInputRequestTypeDef(BaseModel):
    Name: str
    TotalMemoryLimit: int
    TotalCpuLimit: int
    ContainerDefinitions: Sequence[ContainerDefinitionInputTypeDef]
    OperatingSystem: Literal["AMAZON_LINUX_2023"]
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeGameSessionDetailsOutputTypeDef(BaseModel):
    GameSessionDetails: List[GameSessionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMatchmakingOutputTypeDef(BaseModel):
    TicketList: List[MatchmakingTicketTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchBackfillOutputTypeDef(BaseModel):
    MatchmakingTicket: MatchmakingTicketTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchmakingOutputTypeDef(BaseModel):
    MatchmakingTicket: MatchmakingTicketTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerGroupDefinitionOutputTypeDef(BaseModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContainerGroupDefinitionOutputTypeDef(BaseModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainerGroupDefinitionsOutputTypeDef(BaseModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

