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

class AcceptMatchInputTypeDef(BaseValidatorModel):
    TicketId: str
    PlayerIds: Sequence[str]
    AcceptanceType: AcceptanceTypeType


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


class ContainerAttributeTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerRuntimeId: Optional[str] = None


class ConnectionPortRangeTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int


class ContainerDependencyTypeDef(BaseValidatorModel):
    ContainerName: str
    Condition: ContainerDependencyConditionType


class ContainerEnvironmentTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class ContainerFleetLocationAttributesTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ContainerFleetLocationStatusType] = None


class DeploymentDetailsTypeDef(BaseValidatorModel):
    LatestDeploymentId: Optional[str] = None


class GameSessionCreationLimitPolicyTypeDef(BaseValidatorModel):
    NewGameSessionsPerCreator: Optional[int] = None
    PolicyPeriodInMinutes: Optional[int] = None


class LogConfigurationTypeDef(BaseValidatorModel):
    LogDestination: Optional[LogDestinationType] = None
    S3BucketName: Optional[str] = None
    LogGroupArn: Optional[str] = None


class ContainerHealthCheckOutputTypeDef(BaseValidatorModel):
    Command: List[str]
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class ContainerHealthCheckTypeDef(BaseValidatorModel):
    Command: Sequence[str]
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class ContainerIdentifierTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerRuntimeId: Optional[str] = None


class ContainerMountPointTypeDef(BaseValidatorModel):
    InstancePath: str
    ContainerPath: Optional[str] = None
    AccessLevel: Optional[ContainerMountPointAccessLevelType] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class S3LocationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    RoleArn: Optional[str] = None
    ObjectVersion: Optional[str] = None


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


class GameSessionQueueDestinationTypeDef(BaseValidatorModel):
    DestinationArn: Optional[str] = None


class PlayerLatencyPolicyTypeDef(BaseValidatorModel):
    MaximumIndividualPlayerLatencyMilliseconds: Optional[int] = None
    PolicyDurationSeconds: Optional[int] = None


class LocationModelTypeDef(BaseValidatorModel):
    LocationName: Optional[str] = None
    LocationArn: Optional[str] = None


class MatchmakingRuleSetTypeDef(BaseValidatorModel):
    RuleSetBody: str
    RuleSetName: Optional[str] = None
    RuleSetArn: Optional[str] = None
    CreationTime: Optional[datetime] = None


class CreatePlayerSessionInputTypeDef(BaseValidatorModel):
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


class CreatePlayerSessionsInputTypeDef(BaseValidatorModel):
    GameSessionId: str
    PlayerIds: Sequence[str]
    PlayerDataMap: Optional[Mapping[str, str]] = None


class CreateVpcPeeringAuthorizationInputTypeDef(BaseValidatorModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str


class VpcPeeringAuthorizationTypeDef(BaseValidatorModel):
    GameLiftAwsAccountId: Optional[str] = None
    PeerVpcAwsAccountId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None


class CreateVpcPeeringConnectionInputTypeDef(BaseValidatorModel):
    FleetId: str
    PeerVpcAwsAccountId: str
    PeerVpcId: str


class DeleteAliasInputTypeDef(BaseValidatorModel):
    AliasId: str


class DeleteBuildInputTypeDef(BaseValidatorModel):
    BuildId: str


class DeleteContainerFleetInputTypeDef(BaseValidatorModel):
    FleetId: str


class DeleteContainerGroupDefinitionInputTypeDef(BaseValidatorModel):
    Name: str
    VersionNumber: Optional[int] = None
    VersionCountToRetain: Optional[int] = None


class DeleteFleetInputTypeDef(BaseValidatorModel):
    FleetId: str


class DeleteFleetLocationsInputTypeDef(BaseValidatorModel):
    FleetId: str
    Locations: Sequence[str]


class DeleteGameServerGroupInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    DeleteOption: Optional[GameServerGroupDeleteOptionType] = None


class DeleteGameSessionQueueInputTypeDef(BaseValidatorModel):
    Name: str


class DeleteLocationInputTypeDef(BaseValidatorModel):
    LocationName: str


class DeleteMatchmakingConfigurationInputTypeDef(BaseValidatorModel):
    Name: str


class DeleteMatchmakingRuleSetInputTypeDef(BaseValidatorModel):
    Name: str


class DeleteScalingPolicyInputTypeDef(BaseValidatorModel):
    Name: str
    FleetId: str


class DeleteScriptInputTypeDef(BaseValidatorModel):
    ScriptId: str


class DeleteVpcPeeringAuthorizationInputTypeDef(BaseValidatorModel):
    GameLiftAwsAccountId: str
    PeerVpcId: str


class DeleteVpcPeeringConnectionInputTypeDef(BaseValidatorModel):
    FleetId: str
    VpcPeeringConnectionId: str


class DeploymentConfigurationTypeDef(BaseValidatorModel):
    ProtectionStrategy: Optional[DeploymentProtectionStrategyType] = None
    MinimumHealthyPercentage: Optional[int] = None
    ImpairmentStrategy: Optional[DeploymentImpairmentStrategyType] = None


class DeregisterComputeInputTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class DeregisterGameServerInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str


class DescribeAliasInputTypeDef(BaseValidatorModel):
    AliasId: str


class DescribeBuildInputTypeDef(BaseValidatorModel):
    BuildId: str


class DescribeComputeInputTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class DescribeContainerFleetInputTypeDef(BaseValidatorModel):
    FleetId: str


class DescribeContainerGroupDefinitionInputTypeDef(BaseValidatorModel):
    Name: str
    VersionNumber: Optional[int] = None


class DescribeEC2InstanceLimitsInputTypeDef(BaseValidatorModel):
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


class DescribeFleetAttributesInputTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetCapacityInputTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetDeploymentInputTypeDef(BaseValidatorModel):
    FleetId: str
    DeploymentId: Optional[str] = None


class LocationalDeploymentTypeDef(BaseValidatorModel):
    DeploymentStatus: Optional[DeploymentStatusType] = None


class EventTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    ResourceId: Optional[str] = None
    EventCode: Optional[EventCodeType] = None
    Message: Optional[str] = None
    EventTime: Optional[datetime] = None
    PreSignedLogUrl: Optional[str] = None
    Count: Optional[int] = None


class DescribeFleetLocationAttributesInputTypeDef(BaseValidatorModel):
    FleetId: str
    Locations: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetLocationCapacityInputTypeDef(BaseValidatorModel):
    FleetId: str
    Location: str


class DescribeFleetLocationUtilizationInputTypeDef(BaseValidatorModel):
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


class DescribeFleetPortSettingsInputTypeDef(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None


class DescribeFleetUtilizationInputTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeGameServerGroupInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str


class DescribeGameServerInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str


class DescribeGameServerInstancesInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GameServerInstanceTypeDef(BaseValidatorModel):
    GameServerGroupName: Optional[str] = None
    GameServerGroupArn: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[GameServerInstanceStatusType] = None


class DescribeGameSessionDetailsInputTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeGameSessionPlacementInputTypeDef(BaseValidatorModel):
    PlacementId: str


class DescribeGameSessionQueuesInputTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeGameSessionsInputTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstancesInputTypeDef(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None


class DescribeMatchmakingConfigurationsInputTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMatchmakingInputTypeDef(BaseValidatorModel):
    TicketIds: Sequence[str]


class DescribeMatchmakingRuleSetsInputTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePlayerSessionsInputTypeDef(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeRuntimeConfigurationInputTypeDef(BaseValidatorModel):
    FleetId: str


class DescribeScalingPoliciesInputTypeDef(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Location: Optional[str] = None


class DescribeScriptInputTypeDef(BaseValidatorModel):
    ScriptId: str


class DescribeVpcPeeringConnectionsInputTypeDef(BaseValidatorModel):
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


class FilterConfigurationOutputTypeDef(BaseValidatorModel):
    AllowedLocations: Optional[List[str]] = None


class FilterConfigurationTypeDef(BaseValidatorModel):
    AllowedLocations: Optional[Sequence[str]] = None


class GameServerContainerGroupCountsTypeDef(BaseValidatorModel):
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


class PriorityConfigurationOverrideOutputTypeDef(BaseValidatorModel):
    LocationOrder: List[str]
    PlacementFallbackStrategy: Optional[PlacementFallbackStrategyType] = None


class PriorityConfigurationOutputTypeDef(BaseValidatorModel):
    PriorityOrder: Optional[List[PriorityTypeType]] = None
    LocationOrder: Optional[List[str]] = None


class GetComputeAccessInputTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class GetComputeAuthTokenInputTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str


class GetGameSessionLogUrlInputTypeDef(BaseValidatorModel):
    GameSessionId: str


class GetInstanceAccessInputTypeDef(BaseValidatorModel):
    FleetId: str
    InstanceId: str


class InstanceCredentialsTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Secret: Optional[str] = None


class ListAliasesInputTypeDef(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListBuildsInputTypeDef(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListComputeInputTypeDef(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    ComputeStatus: Optional[ListComputeInputStatusType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListContainerFleetsInputTypeDef(BaseValidatorModel):
    ContainerGroupDefinitionName: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListContainerGroupDefinitionVersionsInputTypeDef(BaseValidatorModel):
    Name: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListContainerGroupDefinitionsInputTypeDef(BaseValidatorModel):
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListFleetDeploymentsInputTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListFleetsInputTypeDef(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListGameServerGroupsInputTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListGameServersInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListLocationsInputTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListScriptsInputTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class PriorityConfigurationOverrideTypeDef(BaseValidatorModel):
    LocationOrder: Sequence[str]
    PlacementFallbackStrategy: Optional[PlacementFallbackStrategyType] = None


class PriorityConfigurationTypeDef(BaseValidatorModel):
    PriorityOrder: Optional[Sequence[PriorityTypeType]] = None
    LocationOrder: Optional[Sequence[str]] = None


class TargetConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float


class RegisterComputeInputTypeDef(BaseValidatorModel):
    FleetId: str
    ComputeName: str
    CertificatePath: Optional[str] = None
    DnsName: Optional[str] = None
    IpAddress: Optional[str] = None
    Location: Optional[str] = None


class RegisterGameServerInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    InstanceId: str
    ConnectionInfo: Optional[str] = None
    GameServerData: Optional[str] = None


class RequestUploadCredentialsInputTypeDef(BaseValidatorModel):
    BuildId: str


class ResolveAliasInputTypeDef(BaseValidatorModel):
    AliasId: str


class ResumeGameServerGroupInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    ResumeActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]


class ServerProcessTypeDef(BaseValidatorModel):
    LaunchPath: str
    ConcurrentExecutions: int
    Parameters: Optional[str] = None


class SearchGameSessionsInputTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class StartFleetActionsInputTypeDef(BaseValidatorModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None


class StopFleetActionsInputTypeDef(BaseValidatorModel):
    FleetId: str
    Actions: Sequence[Literal["AUTO_SCALING"]]
    Location: Optional[str] = None


class StopGameSessionPlacementInputTypeDef(BaseValidatorModel):
    PlacementId: str


class StopMatchmakingInputTypeDef(BaseValidatorModel):
    TicketId: str


class SuspendGameServerGroupInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    SuspendActions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]]


class TerminateGameSessionInputTypeDef(BaseValidatorModel):
    GameSessionId: str
    TerminationMode: TerminationModeType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateBuildInputTypeDef(BaseValidatorModel):
    BuildId: str
    Name: Optional[str] = None
    Version: Optional[str] = None


class UpdateFleetCapacityInputTypeDef(BaseValidatorModel):
    FleetId: str
    DesiredInstances: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Location: Optional[str] = None


class UpdateGameServerInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    GameServerId: str
    GameServerData: Optional[str] = None
    UtilizationStatus: Optional[GameServerUtilizationStatusType] = None
    HealthCheck: Optional[Literal["HEALTHY"]] = None


class ValidateMatchmakingRuleSetInputTypeDef(BaseValidatorModel):
    RuleSetBody: str


class VpcPeeringConnectionStatusTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class RoutingStrategyTypeDef(BaseValidatorModel):
    pass


class AliasTypeDef(BaseValidatorModel):
    AliasId: Optional[str] = None
    Name: Optional[str] = None
    AliasArn: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategyTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class UpdateAliasInputTypeDef(BaseValidatorModel):
    AliasId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RoutingStrategy: Optional[RoutingStrategyTypeDef] = None


class PlayerOutputTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Dict[str, AttributeValueOutputTypeDef]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Dict[str, int]] = None


class ClaimGameServerInputTypeDef(BaseValidatorModel):
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


class IpPermissionTypeDef(BaseValidatorModel):
    pass


class DescribeFleetPortSettingsOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    InboundPermissions: List[IpPermissionTypeDef]
    UpdateStatus: Literal["PENDING_UPDATE"]
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFleetPortSettingsInputTypeDef(BaseValidatorModel):
    FleetId: str
    InboundPermissionAuthorizations: Optional[Sequence[IpPermissionTypeDef]] = None
    InboundPermissionRevocations: Optional[Sequence[IpPermissionTypeDef]] = None


class ContainerFleetTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    FleetArn: Optional[str] = None
    FleetRoleArn: Optional[str] = None
    GameServerContainerGroupDefinitionName: Optional[str] = None
    GameServerContainerGroupDefinitionArn: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionArn: Optional[str] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRangeTypeDef] = None
    InstanceInboundPermissions: Optional[List[IpPermissionTypeDef]] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    MaximumGameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceType: Optional[str] = None
    BillingType: Optional[ContainerFleetBillingTypeType] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    MetricGroups: Optional[List[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicyTypeDef] = None
    Status: Optional[ContainerFleetStatusType] = None
    DeploymentDetails: Optional[DeploymentDetailsTypeDef] = None
    LogConfiguration: Optional[LogConfigurationTypeDef] = None
    LocationAttributes: Optional[List[ContainerFleetLocationAttributesTypeDef]] = None


class GetComputeAccessOutputTypeDef(BaseValidatorModel):
    FleetId: str
    FleetArn: str
    ComputeName: str
    ComputeArn: str
    Credentials: AwsCredentialsTypeDef
    Target: str
    ContainerIdentifiers: List[ContainerIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ContainerPortRangeTypeDef(BaseValidatorModel):
    pass


class ContainerPortConfigurationOutputTypeDef(BaseValidatorModel):
    ContainerPortRanges: List[ContainerPortRangeTypeDef]


class ContainerPortConfigurationTypeDef(BaseValidatorModel):
    ContainerPortRanges: Sequence[ContainerPortRangeTypeDef]


class CreateAliasInputTypeDef(BaseValidatorModel):
    Name: str
    RoutingStrategy: RoutingStrategyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateLocationInputTypeDef(BaseValidatorModel):
    LocationName: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateMatchmakingRuleSetInputTypeDef(BaseValidatorModel):
    Name: str
    RuleSetBody: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateBuildInputTypeDef(BaseValidatorModel):
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


class BlobTypeDef(BaseValidatorModel):
    pass


class CreateScriptInputTypeDef(BaseValidatorModel):
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


class UpdateScriptInputTypeDef(BaseValidatorModel):
    ScriptId: str
    Name: Optional[str] = None
    Version: Optional[str] = None
    StorageLocation: Optional[S3LocationTypeDef] = None
    ZipFile: Optional[BlobTypeDef] = None


class CreateContainerFleetInputTypeDef(BaseValidatorModel):
    FleetRoleArn: str
    Description: Optional[str] = None
    GameServerContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRangeTypeDef] = None
    InstanceInboundPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceType: Optional[str] = None
    BillingType: Optional[ContainerFleetBillingTypeType] = None
    Locations: Optional[Sequence[LocationConfigurationTypeDef]] = None
    MetricGroups: Optional[Sequence[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicyTypeDef] = None
    LogConfiguration: Optional[LogConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateFleetLocationsInputTypeDef(BaseValidatorModel):
    FleetId: str
    Locations: Sequence[LocationConfigurationTypeDef]


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


class UpdateFleetAttributesInputTypeDef(BaseValidatorModel):
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


class UpdateGameServerGroupInputTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    RoleArn: Optional[str] = None
    InstanceDefinitions: Optional[Sequence[InstanceDefinitionTypeDef]] = None
    GameServerProtectionPolicy: Optional[GameServerProtectionPolicyType] = None
    BalancingStrategy: Optional[BalancingStrategyType] = None


class CreateGameSessionInputTypeDef(BaseValidatorModel):
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


class CreateMatchmakingConfigurationInputTypeDef(BaseValidatorModel):
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
    StatusReason: Optional[GameSessionStatusReasonType] = None
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


class UpdateGameSessionInputTypeDef(BaseValidatorModel):
    GameSessionId: str
    MaximumPlayerSessionCount: Optional[int] = None
    Name: Optional[str] = None
    PlayerSessionCreationPolicy: Optional[PlayerSessionCreationPolicyType] = None
    ProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None


class UpdateMatchmakingConfigurationInputTypeDef(BaseValidatorModel):
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


class FleetDeploymentTypeDef(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    FleetId: Optional[str] = None
    GameServerBinaryArn: Optional[str] = None
    RollbackGameServerBinaryArn: Optional[str] = None
    PerInstanceBinaryArn: Optional[str] = None
    RollbackPerInstanceBinaryArn: Optional[str] = None
    DeploymentStatus: Optional[DeploymentStatusType] = None
    DeploymentConfiguration: Optional[DeploymentConfigurationTypeDef] = None
    CreationTime: Optional[datetime] = None


class UpdateContainerFleetInputTypeDef(BaseValidatorModel):
    FleetId: str
    GameServerContainerGroupDefinitionName: Optional[str] = None
    PerInstanceContainerGroupDefinitionName: Optional[str] = None
    GameServerContainerGroupsPerInstance: Optional[int] = None
    InstanceConnectionPortRange: Optional[ConnectionPortRangeTypeDef] = None
    InstanceInboundPermissionAuthorizations: Optional[Sequence[IpPermissionTypeDef]] = None
    InstanceInboundPermissionRevocations: Optional[Sequence[IpPermissionTypeDef]] = None
    DeploymentConfiguration: Optional[DeploymentConfigurationTypeDef] = None
    Description: Optional[str] = None
    MetricGroups: Optional[Sequence[str]] = None
    NewGameSessionProtectionPolicy: Optional[ProtectionPolicyType] = None
    GameSessionCreationLimitPolicy: Optional[GameSessionCreationLimitPolicyTypeDef] = None
    LogConfiguration: Optional[LogConfigurationTypeDef] = None
    RemoveAttributes: Optional[Sequence[Literal["PER_INSTANCE_CONTAINER_GROUP_DEFINITION"]]] = None


class DescribeEC2InstanceLimitsOutputTypeDef(BaseValidatorModel):
    EC2InstanceLimits: List[EC2InstanceLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFleetAttributesInputPaginateTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeFleetCapacityInputPaginateTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeFleetUtilizationInputPaginateTypeDef(BaseValidatorModel):
    FleetIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGameServerInstancesInputPaginateTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGameSessionDetailsInputPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGameSessionQueuesInputPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGameSessionsInputPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    GameSessionId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    StatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstancesInputPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    InstanceId: Optional[str] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMatchmakingConfigurationsInputPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    RuleSetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMatchmakingRuleSetsInputPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePlayerSessionsInputPaginateTypeDef(BaseValidatorModel):
    GameSessionId: Optional[str] = None
    PlayerId: Optional[str] = None
    PlayerSessionId: Optional[str] = None
    PlayerSessionStatusFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeScalingPoliciesInputPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    StatusFilter: Optional[ScalingStatusTypeType] = None
    Location: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAliasesInputPaginateTypeDef(BaseValidatorModel):
    RoutingStrategyType: Optional[RoutingStrategyTypeType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBuildsInputPaginateTypeDef(BaseValidatorModel):
    Status: Optional[BuildStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComputeInputPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    Location: Optional[str] = None
    ContainerGroupDefinitionName: Optional[str] = None
    ComputeStatus: Optional[ListComputeInputStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContainerFleetsInputPaginateTypeDef(BaseValidatorModel):
    ContainerGroupDefinitionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContainerGroupDefinitionVersionsInputPaginateTypeDef(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContainerGroupDefinitionsInputPaginateTypeDef(BaseValidatorModel):
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetDeploymentsInputPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetsInputPaginateTypeDef(BaseValidatorModel):
    BuildId: Optional[str] = None
    ScriptId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGameServerGroupsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGameServersInputPaginateTypeDef(BaseValidatorModel):
    GameServerGroupName: str
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLocationsInputPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[LocationFilterType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListScriptsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchGameSessionsInputPaginateTypeDef(BaseValidatorModel):
    FleetId: Optional[str] = None
    AliasId: Optional[str] = None
    Location: Optional[str] = None
    FilterExpression: Optional[str] = None
    SortExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DescribeFleetEventsInputPaginateTypeDef(BaseValidatorModel):
    FleetId: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeFleetEventsInputTypeDef(BaseValidatorModel):
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


class InstanceTypeDef(BaseValidatorModel):
    pass


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
    GameServerContainerGroupCounts: Optional[GameServerContainerGroupCountsTypeDef] = None


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
    PriorityConfigurationOverride: Optional[PriorityConfigurationOverrideOutputTypeDef] = None


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


class PutScalingPolicyInputTypeDef(BaseValidatorModel):
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


class AttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class PlayerTypeDef(BaseValidatorModel):
    PlayerId: Optional[str] = None
    PlayerAttributes: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None
    Team: Optional[str] = None
    LatencyInMs: Optional[Mapping[str, int]] = None


class ComputeTypeDef(BaseValidatorModel):
    pass


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


class CreateContainerFleetOutputTypeDef(BaseValidatorModel):
    ContainerFleet: ContainerFleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeContainerFleetOutputTypeDef(BaseValidatorModel):
    ContainerFleet: ContainerFleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListContainerFleetsOutputTypeDef(BaseValidatorModel):
    ContainerFleets: List[ContainerFleetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateContainerFleetOutputTypeDef(BaseValidatorModel):
    ContainerFleet: ContainerFleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GameServerContainerDefinitionTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    DependsOn: Optional[List[ContainerDependencyTypeDef]] = None
    MountPoints: Optional[List[ContainerMountPointTypeDef]] = None
    EnvironmentOverride: Optional[List[ContainerEnvironmentTypeDef]] = None
    ImageUri: Optional[str] = None
    PortConfiguration: Optional[ContainerPortConfigurationOutputTypeDef] = None
    ResolvedImageDigest: Optional[str] = None
    ServerSdkVersion: Optional[str] = None


class SupportContainerDefinitionTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    DependsOn: Optional[List[ContainerDependencyTypeDef]] = None
    MountPoints: Optional[List[ContainerMountPointTypeDef]] = None
    EnvironmentOverride: Optional[List[ContainerEnvironmentTypeDef]] = None
    Essential: Optional[bool] = None
    HealthCheck: Optional[ContainerHealthCheckOutputTypeDef] = None
    ImageUri: Optional[str] = None
    MemoryHardLimitMebibytes: Optional[int] = None
    PortConfiguration: Optional[ContainerPortConfigurationOutputTypeDef] = None
    ResolvedImageDigest: Optional[str] = None
    Vcpu: Optional[float] = None


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


class CreateFleetOutputTypeDef(BaseValidatorModel):
    FleetAttributes: FleetAttributesTypeDef
    LocationStates: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFleetAttributesOutputTypeDef(BaseValidatorModel):
    FleetAttributes: List[FleetAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class TerminateGameSessionOutputTypeDef(BaseValidatorModel):
    GameSession: GameSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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


class DescribeFleetDeploymentOutputTypeDef(BaseValidatorModel):
    FleetDeployment: FleetDeploymentTypeDef
    LocationalDeployments: Dict[str, LocationalDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListFleetDeploymentsOutputTypeDef(BaseValidatorModel):
    FleetDeployments: List[FleetDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeFleetCapacityOutputTypeDef(BaseValidatorModel):
    FleetCapacity: List[FleetCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeFleetLocationCapacityOutputTypeDef(BaseValidatorModel):
    FleetCapacity: FleetCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGameServerGroupInputTypeDef(BaseValidatorModel):
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


class PriorityConfigurationOverrideUnionTypeDef(BaseValidatorModel):
    pass


class StartGameSessionPlacementInputTypeDef(BaseValidatorModel):
    PlacementId: str
    GameSessionQueueName: str
    MaximumPlayerSessionCount: int
    GameProperties: Optional[Sequence[GamePropertyTypeDef]] = None
    GameSessionName: Optional[str] = None
    PlayerLatencies: Optional[Sequence[PlayerLatencyTypeDef]] = None
    DesiredPlayerSessions: Optional[Sequence[DesiredPlayerSessionTypeDef]] = None
    GameSessionData: Optional[str] = None
    PriorityConfigurationOverride: Optional[PriorityConfigurationOverrideUnionTypeDef] = None


class FilterConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PriorityConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateGameSessionQueueInputTypeDef(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationUnionTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationUnionTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateGameSessionQueueInputTypeDef(BaseValidatorModel):
    Name: str
    TimeoutInSeconds: Optional[int] = None
    PlayerLatencyPolicies: Optional[Sequence[PlayerLatencyPolicyTypeDef]] = None
    Destinations: Optional[Sequence[GameSessionQueueDestinationTypeDef]] = None
    FilterConfiguration: Optional[FilterConfigurationUnionTypeDef] = None
    PriorityConfiguration: Optional[PriorityConfigurationUnionTypeDef] = None
    CustomEventData: Optional[str] = None
    NotificationTarget: Optional[str] = None


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


class DescribeVpcPeeringConnectionsOutputTypeDef(BaseValidatorModel):
    VpcPeeringConnections: List[VpcPeeringConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ContainerGroupDefinitionTypeDef(BaseValidatorModel):
    Name: str
    ContainerGroupDefinitionArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    OperatingSystem: Optional[Literal["AMAZON_LINUX_2023"]] = None
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    TotalMemoryLimitMebibytes: Optional[int] = None
    TotalVcpuLimit: Optional[float] = None
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionTypeDef] = None
    SupportContainerDefinitions: Optional[List[SupportContainerDefinitionTypeDef]] = None
    VersionNumber: Optional[int] = None
    VersionDescription: Optional[str] = None
    Status: Optional[ContainerGroupDefinitionStatusType] = None
    StatusReason: Optional[str] = None


class ContainerPortConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class GameServerContainerDefinitionInputTypeDef(BaseValidatorModel):
    ContainerName: str
    ImageUri: str
    PortConfiguration: ContainerPortConfigurationUnionTypeDef
    ServerSdkVersion: str
    DependsOn: Optional[Sequence[ContainerDependencyTypeDef]] = None
    MountPoints: Optional[Sequence[ContainerMountPointTypeDef]] = None
    EnvironmentOverride: Optional[Sequence[ContainerEnvironmentTypeDef]] = None


class ContainerHealthCheckUnionTypeDef(BaseValidatorModel):
    pass


class SupportContainerDefinitionInputTypeDef(BaseValidatorModel):
    ContainerName: str
    ImageUri: str
    DependsOn: Optional[Sequence[ContainerDependencyTypeDef]] = None
    MountPoints: Optional[Sequence[ContainerMountPointTypeDef]] = None
    EnvironmentOverride: Optional[Sequence[ContainerEnvironmentTypeDef]] = None
    Essential: Optional[bool] = None
    HealthCheck: Optional[ContainerHealthCheckUnionTypeDef] = None
    MemoryHardLimitMebibytes: Optional[int] = None
    PortConfiguration: Optional[ContainerPortConfigurationUnionTypeDef] = None
    Vcpu: Optional[float] = None


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


class RuntimeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateFleetInputTypeDef(BaseValidatorModel):
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
    RuntimeConfiguration: Optional[RuntimeConfigurationUnionTypeDef] = None
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


class UpdateRuntimeConfigurationInputTypeDef(BaseValidatorModel):
    FleetId: str
    RuntimeConfiguration: RuntimeConfigurationUnionTypeDef


class PlayerUnionTypeDef(BaseValidatorModel):
    pass


class StartMatchBackfillInputTypeDef(BaseValidatorModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnionTypeDef]
    TicketId: Optional[str] = None
    GameSessionArn: Optional[str] = None


class StartMatchmakingInputTypeDef(BaseValidatorModel):
    ConfigurationName: str
    Players: Sequence[PlayerUnionTypeDef]
    TicketId: Optional[str] = None


class CreateContainerGroupDefinitionOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeContainerGroupDefinitionOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListContainerGroupDefinitionVersionsOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListContainerGroupDefinitionsOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinitions: List[ContainerGroupDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateContainerGroupDefinitionOutputTypeDef(BaseValidatorModel):
    ContainerGroupDefinition: ContainerGroupDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContainerGroupDefinitionInputTypeDef(BaseValidatorModel):
    Name: str
    TotalMemoryLimitMebibytes: int
    TotalVcpuLimit: float
    OperatingSystem: Literal["AMAZON_LINUX_2023"]
    ContainerGroupType: Optional[ContainerGroupTypeType] = None
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionInputTypeDef] = None
    SupportContainerDefinitions: Optional[Sequence[SupportContainerDefinitionInputTypeDef]] = None
    VersionDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateContainerGroupDefinitionInputTypeDef(BaseValidatorModel):
    Name: str
    GameServerContainerDefinition: Optional[GameServerContainerDefinitionInputTypeDef] = None
    SupportContainerDefinitions: Optional[Sequence[SupportContainerDefinitionInputTypeDef]] = None
    TotalMemoryLimitMebibytes: Optional[int] = None
    TotalVcpuLimit: Optional[float] = None
    VersionDescription: Optional[str] = None
    SourceVersionNumber: Optional[int] = None
    OperatingSystem: Optional[Literal["AMAZON_LINUX_2023"]] = None


