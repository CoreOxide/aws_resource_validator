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
from aws_resource_validator.pydantic_models.gamelift_constants import *

class AcceptMatchInputRequestTypeDef(BaseValidatorModel):
    TicketId: str
    PlayerIds: Sequence[str]
    AcceptanceType: AcceptanceTypeType

class RoutingStrategyTypeDef(BaseValidatorModel):
    Type: Optional[RoutingStrategyTypeType] = None
    FleetId: Optional[str] = None
    Message: Optional[str] = None

class AnywhereConfigurationTypeDef(BaseValidatorModel):
    Cost: str

class AttributeValueOutputTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[float] = None
    SL: Optional[List[str]] = None
    SDM: Optional[Dict[str, float]] = None

class AttributeValueTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[float] = None
    SL: Optional[Sequence[str]] = None
    SDM: Optional[Mapping[str, float]] = None

class AwsCredentialsTypeDef(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None

class BuildTypeDef(BaseValidatorModel):
    BuildId: Optional[str] = None
    BuildArn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[BuildStatusType] = None
    SizeOnDisk: Optional[int] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    CreationTime: Optional[datetime] = None
    ServerSdkVersion: Optional[str] = None

class CertificateConfigurationTypeDef(BaseValidatorModel):
    CertificateType: CertificateTypeType

class ClaimFilterOptionTypeDef(BaseValidatorModel):
    InstanceStatuses: Optional[Sequence[FilterInstanceStatusType]] = None

class GameServerTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConnectionPortRangeTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int

class ContainerPortMappingTypeDef(BaseValidatorModel):
    ContainerPort: Optional[int] = None
    ConnectionPort: Optional[int] = None
    Protocol: Optional[IpProtocolType] = None

class ContainerDependencyTypeDef(BaseValidatorModel):
    ContainerName: str
    Condition: ContainerDependencyConditionType

class ContainerEnvironmentTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class ContainerHealthCheckTypeDef(BaseValidatorModel):
    Command: Sequence[str]
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None

class ContainerMemoryLimitsTypeDef(BaseValidatorModel):
    SoftLimit: Optional[int] = None
    HardLimit: Optional[int] = None

class ContainerHealthCheckOutputTypeDef(BaseValidatorModel):
    Command: List[str]
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None

class ContainerGroupDefinitionPropertyTypeDef(BaseValidatorModel):
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    ContainerGroupDefinitionName: Optional[str] = None

class ContainerGroupsPerInstanceTypeDef(BaseValidatorModel):
    DesiredReplicaContainerGroupsPerInstance: Optional[int] = None
    MaxReplicaContainerGroupsPerInstance: Optional[int] = None

class ContainerPortRangeTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int
    Protocol: IpProtocolType

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class S3LocationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    RoleArn: Optional[str] = None
    ObjectVersion: Optional[str] = None

class IpPermissionTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int
    IpRange: str
    Protocol: IpProtocolType

class LocationConfigurationTypeDef(BaseValidatorModel):
    Location: str

class ResourceCreationLimitPolicyTypeDef(BaseValidatorModel):
    NewGameSessionsPerCreator: Optional[int] = None
    PolicyPeriodInMinutes: Optional[int] = None

class LocationStateTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[FleetStatusType] = None

class InstanceDefinitionTypeDef(BaseValidatorModel):
    InstanceType: GameServerGroupInstanceTypeType
    WeightedCapacity: Optional[str] = None

class LaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class GamePropertyTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class FilterConfigurationTypeDef(BaseValidatorModel):
    AllowedLocations: Optional[Sequence[str]] = None

class GameSessionQueueDestinationTypeDef(BaseValidatorModel):
    DestinationArn: Optional[str] = None

class PlayerLatencyPolicyTypeDef(BaseValidatorModel):
    MaximumIndividualPlayerLatencyMilliseconds: Optional[int] = None
    PolicyDurationSeconds: Optional[int] = None

class PriorityConfigurationTypeDef(BaseValidatorModel):
    PriorityOrder: Optional[Sequence[PriorityTypeType]] = None
    LocationOrder: Optional[Sequence[str]] = None

class LocationModelTypeDef(BaseValidatorModel):
    LocationName: Optional[str] = None
    LocationArn: Optional[str] = None

class MatchmakingRuleSetTypeDef(BaseValidatorModel):
    RuleSetBody: str
    RuleSetName: Optional[str] = None
    RuleSetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None

class CreatePlayerSessionInputRequestTypeDef(BaseValidatorModel):
    GameSessionId: str
    PlayerId: str
    PlayerData: Optional[str] = None

class PlayerSessionTypeDef(BaseValidatorModel):
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

class CreatePlayerSessionsInputRequestTypeDef(BaseValidatorModel):
    GameSessionId: str
    PlayerIds: Sequence[str]
    PlayerDataMap: Optional[Mapping[str, str]] = None

class CreateVpcPeeringAuthorizationInputRequestTypeDef(BaseValidatorModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str

class VpcPeeringAuthorizationTypeDef(BaseValidatorModel):
    GameLiftAwsAccountId: Optional[str] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None

class CreateVpcPeeringConnectionInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    PeerVpcAwsAccountId: str
    PeerVpcId: str

class DeleteAliasInputRequestTypeDef(BaseValidatorModel):
    AliasId: str

class DeleteBuildInputRequestTypeDef(BaseValidatorModel):
    BuildId: str

class DeleteContainerGroupDefinitionInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteFleetInputRequestTypeDef(BaseValidatorModel):
    FleetId: str

class DeleteFleetLocationsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Locations: Sequence[str]

class DeleteGameServerGroupInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    DeleteOption: Optional[GameServerGroupDeleteOptionType] = None

class DeleteGameSessionQueueInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteLocationInputRequestTypeDef(BaseValidatorModel):
    LocationName: str

class DeleteMatchmakingConfigurationInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteMatchmakingRuleSetInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteScalingPolicyInputRequestTypeDef(BaseValidatorModel):
    Name: str
    FleetId: str

class DeleteScriptInputRequestTypeDef(BaseValidatorModel):
    ScriptId: str

class DeleteVpcPeeringAuthorizationInputRequestTypeDef(BaseValidatorModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str

class DeleteVpcPeeringConnectionInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    VpcPeeringConnectionId: str

class DeregisterComputeInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str

class DeregisterGameServerInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str

class DescribeAliasInputRequestTypeDef(BaseValidatorModel):
    AliasId: str

class DescribeBuildInputRequestTypeDef(BaseValidatorModel):
    BuildId: str

class DescribeComputeInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str

class DescribeContainerGroupDefinitionInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeEC2InstanceLimitsInputRequestTypeDef(BaseValidatorModel):
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    Location: Optional[str] = None

class EC2InstanceLimitTypeDef(BaseValidatorModel):
    EC2InstanceType: Optional[EC2InstanceTypeType] = None
    CurrentInstances: Optional[int] = None
    InstanceLimit: Optional[int] = None
    Location: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeFleetAttributesInputRequestTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetCapacityInputRequestTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class EventTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    ResourceId: Optional[str] = None
    EventCode: Optional[EventCodeType] = None
    Message: Optional[str] = None
    EventTime: Optional[datetime] = None
    PreSignedLogUrl: Optional[str] = None
    Count: Optional[int] = None

class DescribeFleetLocationAttributesInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Locations: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetLocationCapacityInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Location: str

class DescribeFleetLocationUtilizationInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Location: str

class FleetUtilizationTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    ActiveServerProcessCount: Optional[int] = None
    ActiveGameSessionCount: Optional[int] = None
    CurrentPlayerSessionCount: Optional[int] = None
    MaximumPlayerSessionCount: Optional[int] = None
    Location: Optional[str] = None

class DescribeFleetPortSettingsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None

class DescribeFleetUtilizationInputRequestTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeGameServerGroupInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str

class DescribeGameServerInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str

class DescribeGameServerInstancesInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GameServerInstanceTypeDef(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[GameServerInstanceStatusType] = None

class DescribeGameSessionDetailsInputRequestTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeGameSessionPlacementInputRequestTypeDef(BaseValidatorModel):
    PlacementId: str

class DescribeGameSessionQueuesInputRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeGameSessionsInputRequestTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstancesInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None

class InstanceTypeDef(BaseValidatorModel):
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

class DescribeMatchmakingConfigurationsInputRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMatchmakingInputRequestTypeDef(BaseValidatorModel):
    TicketIds: Sequence[str]

class DescribeMatchmakingRuleSetsInputRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePlayerSessionsInputRequestTypeDef(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeRuntimeConfigurationInputRequestTypeDef(BaseValidatorModel):
    FleetId: str

class DescribeScalingPoliciesInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None

class DescribeScriptInputRequestTypeDef(BaseValidatorModel):
    ScriptId: str

class DescribeVpcPeeringConnectionsInputRequestTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None

class DesiredPlayerSessionTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerData: Optional[str] = None

class EC2InstanceCountsTypeDef(BaseValidatorModel):
    DESIRED: Optional[int] = None
    MINIMUM: Optional[int] = None
    MAXIMUM: Optional[int] = None
    PENDING: Optional[int] = None
    ACTIVE: Optional[int] = None
    IDLE: Optional[int] = None
    TERMINATING: Optional[int] = None

class FilterConfigurationExtraOutputTypeDef(BaseValidatorModel):
    AllowedLocations: Optional[List[str]] = None

class FilterConfigurationOutputTypeDef(BaseValidatorModel):
    AllowedLocations: Optional[List[str]] = None

class ReplicaContainerGroupCountsTypeDef(BaseValidatorModel):
    PENDING: Optional[int] = None
    ACTIVE: Optional[int] = None
    IDLE: Optional[int] = None
    TERMINATING: Optional[int] = None

class TargetTrackingConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float

class MatchedPlayerSessionTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None

class PlacedPlayerSessionTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None

class PlayerLatencyTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    RegionIdentifier: Optional[str] = None
    LatencyInMilliseconds: Optional[float] = None

class PriorityConfigurationOutputTypeDef(BaseValidatorModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None

class GetComputeAccessInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str

class GetComputeAuthTokenInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str

class GetGameSessionLogUrlInputRequestTypeDef(BaseValidatorModel):
    GameSessionId: str

class GetInstanceAccessInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    InstanceId: str

class InstanceCredentialsTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Secret: Optional[str] = None

class ListAliasesInputRequestTypeDef(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListBuildsInputRequestTypeDef(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListComputeInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListContainerGroupDefinitionsInputRequestTypeDef(BaseValidatorModel):
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListFleetsInputRequestTypeDef(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListGameServerGroupsInputRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListGameServersInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListLocationsInputRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListScriptsInputRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class PriorityConfigurationExtraOutputTypeDef(BaseValidatorModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None

class TargetConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float

class RegisterComputeInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str
    CertificatePath: Optional[str] = None
    DnsName: Optional[str] = None
    IpAddress: Optional[str] = None
    Location: Optional[str] = None

class RegisterGameServerInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    InstanceId: str
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None

class RequestUploadCredentialsInputRequestTypeDef(BaseValidatorModel):
    BuildId: str

class ResolveAliasInputRequestTypeDef(BaseValidatorModel):
    AliasId: str

class ResumeGameServerGroupInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    ResumeActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]

class ServerProcessTypeDef(BaseValidatorModel):
    LaunchPath: str
    ConcurrentExecutions: int
    Parameters: Optional[str] = None

class SearchGameSessionsInputRequestTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class StartFleetActionsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None

class StopFleetActionsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None

class StopGameSessionPlacementInputRequestTypeDef(BaseValidatorModel):
    PlacementId: str

class StopMatchmakingInputRequestTypeDef(BaseValidatorModel):
    TicketId: str

class SuspendGameServerGroupInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    SuspendActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateBuildInputRequestTypeDef(BaseValidatorModel):
    BuildId: str
    Name: Optional[str] = None
    Version: Optional[str] = None

class UpdateFleetCapacityInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    DesiredInstances: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Location: Optional[str] = None

class UpdateGameServerInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    GameServerData: Optional[str] = None
    UtilizationStatus: Optional[GameServerUtilizationStatusType] = None
    HealthCheck: Optional[Literal["HEALTHY"]] = None

class ValidateMatchmakingRuleSetInputRequestTypeDef(BaseValidatorModel):
    RuleSetBody: str

class VpcPeeringConnectionStatusTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class AliasTypeDef(BaseValidatorModel):
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    AliasArn: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategyTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class UpdateAliasInputRequestTypeDef(BaseValidatorModel):
    AliasId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategyTypeDef] = None

class PlayerOutputTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Dict[str, AttributeValueOutputTypeDef]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Dict[str, int]] = None

class PlayerTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Mapping[str, AttributeValueTypeDef]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Mapping[str, int]] = None

class ClaimGameServerInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: Optional[str] = None
    GameServerData: Optional[str] = None
    FilterOption: Optional[ClaimFilterOptionTypeDef] = None

class ClaimGameServerOutputTypeDef(BaseValidatorModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBuildOutputTypeDef(BaseValidatorModel):
    Build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameServerOutputTypeDef(BaseValidatorModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetComputeAccessOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    Credentials: AwsCredentialsTypeDef
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComputeAuthTokenOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    AuthToken: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetGameSessionLogUrlOutputTypeDef(BaseValidatorModel):
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildsOutputTypeDef(BaseValidatorModel):
    Builds: List[BuildTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFleetsOutputTypeDef(BaseValidatorModel):
    FleetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListGameServersOutputTypeDef(BaseValidatorModel):
    GameServers: List[GameServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutScalingPolicyOutputTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterGameServerOutputTypeDef(BaseValidatorModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveAliasOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFleetActionsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopFleetActionsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBuildOutputTypeDef(BaseValidatorModel):
    Build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetAttributesOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetCapacityOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetPortSettingsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGameServerOutputTypeDef(BaseValidatorModel):
    GameServer: GameServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateMatchmakingRuleSetOutputTypeDef(BaseValidatorModel):
    Valid: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerGroupsConfigurationTypeDef(BaseValidatorModel):
    ContainerGroupDefinitionNames: Sequence[str]
    ConnectionPortRange: ConnectionPortRangeTypeDef
    DesiredReplicaContainerGroupsPerInstance: Optional[int] = None

class ContainerAttributesTypeDef(BaseValidatorModel):
    ContainerPortMappings: Optional[List[ContainerPortMappingTypeDef]] = None

class ContainerGroupsAttributesTypeDef(BaseValidatorModel):
    ContainerGroupDefinitionProperties: Optional[       List[ContainerGroupDefinitionPropertyTypeDef]     ] = None
    ConnectionPortRange: Optional[ConnectionPortRangeTypeDef] = None
    ContainerGroupsPerInstance: Optional[ContainerGroupsPerInstanceTypeDef] = None

class ContainerPortConfigurationOutputTypeDef(BaseValidatorModel):
    ContainerPortRanges: List[ContainerPortRangeTypeDef]

class ContainerPortConfigurationTypeDef(BaseValidatorModel):
    ContainerPortRanges: Sequence[ContainerPortRangeTypeDef]

class CreateAliasInputRequestTypeDef(BaseValidatorModel):
    Name: str
    RoutingStrategy: RoutingStrategyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateLocationInputRequestTypeDef(BaseValidatorModel):
    LocationName: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMatchmakingRuleSetInputRequestTypeDef(BaseValidatorModel):
    Name: str
    RuleSetBody: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateBuildInputRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ServerSdkVersion: Optional[str] = None

class CreateBuildOutputTypeDef(BaseValidatorModel):
    Build: BuildTypeDef
    UploadCredentials: AwsCredentialsTypeDef
    StorageLocation: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScriptInputRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    ZipFile: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class RequestUploadCredentialsOutputTypeDef(BaseValidatorModel):
    UploadCredentials: AwsCredentialsTypeDef
    StorageLocation: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScriptTypeDef(BaseValidatorModel):
    ScriptId: Optional[str] = None
    ScriptArn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None
    SizeOnDisk: Optional[int] = None
    CreationTime: Optional[datetime] = None
    StorageLocation: Optional[S3LocationTypeDef] = None

class UpdateScriptInputRequestTypeDef(BaseValidatorModel):
    ScriptId: str
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    ZipFile: Optional[BlobTypeDef] = None

class DescribeFleetPortSettingsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    InboundPermissions: List[IpPermissionTypeDef]
    UpdateStatus: Literal["PENDING_UPDATE"]
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetPortSettingsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    InboundPermissionAuthorizations: Optional[Sequence[IpPermissionTypeDef]] = None
    InboundPermissionRevocations: Optional[Sequence[IpPermissionTypeDef]] = None

class CreateFleetLocationsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Locations: Sequence[LocationConfigurationTypeDef]

class UpdateFleetAttributesInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    ResourceCreationLimitPolicy: Optional[ResourceCreationLimitPolicyTypeDef] = None
    MetricGroups: Optional[Sequence[str]] = None
    AnywhereConfiguration: Optional[AnywhereConfigurationTypeDef] = None

class CreateFleetLocationsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFleetLocationsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LocationAttributesTypeDef(BaseValidatorModel):
    LocationState: Optional[LocationStateTypeDef] = None
    StoppedActions: Optional[List[Literal["AUTO_SCALING"]]] = None
    UpdateStatus: Optional[Literal["PENDING_UPDATE"]] = None

class GameServerGroupTypeDef(BaseValidatorModel):
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

class UpdateGameServerGroupInputRequestTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[Sequence[InstanceDefinitionTypeDef]] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None

class CreateGameSessionInputRequestTypeDef(BaseValidatorModel):
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

class CreateMatchmakingConfigurationInputRequestTypeDef(BaseValidatorModel):
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

class GameSessionTypeDef(BaseValidatorModel):
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

class MatchmakingConfigurationTypeDef(BaseValidatorModel):
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

class UpdateGameSessionInputRequestTypeDef(BaseValidatorModel):
    GameSessionId: str
    MaximumPlayerSessionCount: Optional[int] = None
    Name: Optional[str] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None

class UpdateMatchmakingConfigurationInputRequestTypeDef(BaseValidatorModel):
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

class CreateGameSessionQueueInputRequestTypeDef(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateGameSessionQueueInputRequestTypeDef(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None

class CreateLocationOutputTypeDef(BaseValidatorModel):
    Location: LocationModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLocationsOutputTypeDef(BaseValidatorModel):
    Locations: List[LocationModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateMatchmakingRuleSetOutputTypeDef(BaseValidatorModel):
    RuleSet: MatchmakingRuleSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMatchmakingRuleSetsOutputTypeDef(BaseValidatorModel):
    RuleSets: List[MatchmakingRuleSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePlayerSessionOutputTypeDef(BaseValidatorModel):
    PlayerSession: PlayerSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePlayerSessionsOutputTypeDef(BaseValidatorModel):
    PlayerSessions: List[PlayerSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePlayerSessionsOutputTypeDef(BaseValidatorModel):
    PlayerSessions: List[PlayerSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateVpcPeeringAuthorizationOutputTypeDef(BaseValidatorModel):
    VpcPeeringAuthorization: VpcPeeringAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcPeeringAuthorizationsOutputTypeDef(BaseValidatorModel):
    VpcPeeringAuthorizations: List[VpcPeeringAuthorizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEC2InstanceLimitsOutputTypeDef(BaseValidatorModel):
    EC2InstanceLimits: List[EC2InstanceLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAttributesInputDescribeFleetAttributesPaginateTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetCapacityInputDescribeFleetCapacityPaginateTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGameSessionsInputDescribeGameSessionsPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancesInputDescribeInstancesPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePlayerSessionsInputDescribePlayerSessionsPaginateTypeDef(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAliasesInputListAliasesPaginateTypeDef(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildsInputListBuildsPaginateTypeDef(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComputeInputListComputePaginateTypeDef(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContainerGroupDefinitionsInputListContainerGroupDefinitionsPaginateTypeDef(BaseValidatorModel):
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsInputListFleetsPaginateTypeDef(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGameServerGroupsInputListGameServerGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGameServersInputListGameServersPaginateTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLocationsInputListLocationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScriptsInputListScriptsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchGameSessionsInputSearchGameSessionsPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetEventsInputDescribeFleetEventsPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetEventsInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetEventsOutputTypeDef(BaseValidatorModel):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetLocationUtilizationOutputTypeDef(BaseValidatorModel):
    FleetUtilization: FleetUtilizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetUtilizationOutputTypeDef(BaseValidatorModel):
    FleetUtilization: List[FleetUtilizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeGameServerInstancesOutputTypeDef(BaseValidatorModel):
    GameServerInstances: List[GameServerInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancesOutputTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FleetCapacityTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    InstanceType: Optional[EC2InstanceTypeType] = None
    InstanceCounts: Optional[EC2InstanceCountsTypeDef] = None
    Location: Optional[str] = None
    ReplicaContainerGroupCounts: Optional[ReplicaContainerGroupCountsTypeDef] = None

class GameServerGroupAutoScalingPolicyTypeDef(BaseValidatorModel):
    TargetTrackingConfiguration: TargetTrackingConfigurationTypeDef
    EstimatedInstanceWarmup: Optional[int] = None

class GameSessionConnectionInfoTypeDef(BaseValidatorModel):
    GameSessionArn: Optional[str] = None
    IpAddress: Optional[str] = None
    DnsName: Optional[str] = None
    Port: Optional[int] = None
    MatchedPlayerSessions: Optional[List[MatchedPlayerSessionTypeDef]] = None

class GameSessionPlacementTypeDef(BaseValidatorModel):
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

class StartGameSessionPlacementInputRequestTypeDef(BaseValidatorModel):
    PlacementId: str
    GameSessionQueueName: str
    MaximumPlayerSessionCount: int
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None
    GameSessionName: Optional[str] = None
    PlayerLatencies: Optional[Sequence[PlayerLatencyTypeDef]] = None
    DesiredPlayerSessions: Optional[Sequence[DesiredPlayerSessionTypeDef]] = None
    GameSessionData: Optional[str] = None

class GameSessionQueueTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    GameSessionQueueArn: Optional[str] = None
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[List[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[List[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationOutputTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None

class InstanceAccessTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    InstanceId: Optional[str] = None
    IpAddress: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    Credentials: Optional[InstanceCredentialsTypeDef] = None

class PutScalingPolicyInputRequestTypeDef(BaseValidatorModel):
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

class ScalingPolicyTypeDef(BaseValidatorModel):
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

class RuntimeConfigurationOutputTypeDef(BaseValidatorModel):
    ServerProcesses: Optional[List[ServerProcessTypeDef]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None

class RuntimeConfigurationTypeDef(BaseValidatorModel):
    ServerProcesses: Optional[Sequence[ServerProcessTypeDef]] = None
    MaxConcurrentGameSessionActivations: Optional[int] = None
    GameSessionActivationTimeoutSeconds: Optional[int] = None

class VpcPeeringConnectionTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    IpV4CidrBlock: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    Status: Optional[VpcPeeringConnectionStatusTypeDef] = None
    PeerVpcId: Optional[str] = None
    GameLiftVpcId: Optional[str] = None

class CreateAliasOutputTypeDef(BaseValidatorModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAliasOutputTypeDef(BaseValidatorModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesOutputTypeDef(BaseValidatorModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateAliasOutputTypeDef(BaseValidatorModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComputeTypeDef(BaseValidatorModel):
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

class FleetAttributesTypeDef(BaseValidatorModel):
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

class ContainerDefinitionTypeDef(BaseValidatorModel):
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

class ContainerDefinitionInputTypeDef(BaseValidatorModel):
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

class CreateScriptOutputTypeDef(BaseValidatorModel):
    Script: ScriptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScriptOutputTypeDef(BaseValidatorModel):
    Script: ScriptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListScriptsOutputTypeDef(BaseValidatorModel):
    Scripts: List[ScriptTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateScriptOutputTypeDef(BaseValidatorModel):
    Script: ScriptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetLocationAttributesOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    LocationAttributes: List[LocationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGameServerGroupOutputTypeDef(BaseValidatorModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGameServerGroupOutputTypeDef(BaseValidatorModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameServerGroupOutputTypeDef(BaseValidatorModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGameServerGroupsOutputTypeDef(BaseValidatorModel):
    GameServerGroups: List[GameServerGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResumeGameServerGroupOutputTypeDef(BaseValidatorModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SuspendGameServerGroupOutputTypeDef(BaseValidatorModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGameServerGroupOutputTypeDef(BaseValidatorModel):
    GameServerGroup: GameServerGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGameSessionOutputTypeDef(BaseValidatorModel):
    GameSession: GameSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameSessionsOutputTypeDef(BaseValidatorModel):
    GameSessions: List[GameSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GameSessionDetailTypeDef(BaseValidatorModel):
    GameSession: Optional[GameSessionTypeDef] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None

class SearchGameSessionsOutputTypeDef(BaseValidatorModel):
    GameSessions: List[GameSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGameSessionOutputTypeDef(BaseValidatorModel):
    GameSession: GameSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMatchmakingConfigurationOutputTypeDef(BaseValidatorModel):
    Configuration: MatchmakingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMatchmakingConfigurationsOutputTypeDef(BaseValidatorModel):
    Configurations: List[MatchmakingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateMatchmakingConfigurationOutputTypeDef(BaseValidatorModel):
    Configuration: MatchmakingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetCapacityOutputTypeDef(BaseValidatorModel):
    FleetCapacity: List[FleetCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetLocationCapacityOutputTypeDef(BaseValidatorModel):
    FleetCapacity: FleetCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGameServerGroupInputRequestTypeDef(BaseValidatorModel):
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

class MatchmakingTicketTypeDef(BaseValidatorModel):
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

class DescribeGameSessionPlacementOutputTypeDef(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartGameSessionPlacementOutputTypeDef(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopGameSessionPlacementOutputTypeDef(BaseValidatorModel):
    GameSessionPlacement: GameSessionPlacementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGameSessionQueueOutputTypeDef(BaseValidatorModel):
    GameSessionQueue: GameSessionQueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGameSessionQueuesOutputTypeDef(BaseValidatorModel):
    GameSessionQueues: List[GameSessionQueueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGameSessionQueueOutputTypeDef(BaseValidatorModel):
    GameSessionQueue: GameSessionQueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceAccessOutputTypeDef(BaseValidatorModel):
    InstanceAccess: InstanceAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPoliciesOutputTypeDef(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRuntimeConfigurationOutputTypeDef(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuntimeConfigurationOutputTypeDef(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetInputRequestTypeDef(BaseValidatorModel):
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

class UpdateRuntimeConfigurationInputRequestTypeDef(BaseValidatorModel):
    FleetId: str
    RuntimeConfiguration: RuntimeConfigurationTypeDef

class DescribeVpcPeeringConnectionsOutputTypeDef(BaseValidatorModel):
    VpcPeeringConnections: List[VpcPeeringConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchBackfillInputRequestTypeDef(BaseValidatorModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnionTypeDef]
    TicketId: Optional[str] = None
    GameSessionArn: Optional[str] = None

class StartMatchmakingInputRequestTypeDef(BaseValidatorModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnionTypeDef]
    TicketId: Optional[str] = None

class DescribeComputeOutputTypeDef(BaseValidatorModel):
    Compute: ComputeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListComputeOutputTypeDef(BaseValidatorModel):
    ComputeList: List[ComputeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterComputeOutputTypeDef(BaseValidatorModel):
    Compute: ComputeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetOutputTypeDef(BaseValidatorModel):
    FleetAttributes: FleetAttributesTypeDef
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAttributesOutputTypeDef(BaseValidatorModel):
    FleetAttributes: List[FleetAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContainerGroupDefinitionTypeDef(BaseValidatorModel):
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

class CreateContainerGroupDefinitionInputRequestTypeDef(BaseValidatorModel):
    Name: str
    TotalMemoryLimit: int
    TotalCpuLimit: int
    ContainerDefinitions: Sequence[ContainerDefinitionInputTypeDef]
    OperatingSystem: Literal["AMAZON_LINUX_2023"]
    SchedulingStrategy: Optional[ContainerSchedulingStrategyType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeGameSessionDetailsOutputTypeDef(BaseValidatorModel):
    GameSessionDetails: List[GameSessionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMatchmakingOutputTypeDef(BaseValidatorModel):
    TicketList: List[MatchmakingTicketTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchBackfillOutputTypeDef(BaseValidatorModel):
    MatchmakingTicket: MatchmakingTicketTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchmakingOutputTypeDef(BaseValidatorModel):
    MatchmakingTicket: MatchmakingTicketTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerGroupDefinitionOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContainerGroupDefinitionOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainerGroupDefinitionsOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

