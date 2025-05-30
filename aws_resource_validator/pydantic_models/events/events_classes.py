from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.events.events_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'activate_event_source' function.
class ActivateEventSourceRequest(BaseValidatorModel):
    Name: str


class ApiDestination(BaseValidatorModel):
    ApiDestinationArn: Optional[str] = None
    Name: Optional[str] = None
    ApiDestinationState: Optional[ApiDestinationStateType] = None
    ConnectionArn: Optional[str] = None
    InvocationEndpoint: Optional[str] = None
    HttpMethod: Optional[ApiDestinationHttpMethodType] = None
    InvocationRateLimitPerSecond: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class AppSyncParameters(BaseValidatorModel):
    GraphQLOperation: Optional[str] = None


class Archive(BaseValidatorModel):
    ArchiveName: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ArchiveStateType] = None
    StateReason: Optional[str] = None
    RetentionDays: Optional[int] = None
    SizeBytes: Optional[int] = None
    EventCount: Optional[int] = None
    CreationTime: Optional[datetime] = None


class AwsVpcConfigurationOutput(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None


class AwsVpcConfiguration(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None


class BatchArrayProperties(BaseValidatorModel):
    Size: Optional[int] = None


class BatchRetryStrategy(BaseValidatorModel):
    Attempts: Optional[int] = None


# This class is the input for the 'cancel_replay' function.
class CancelReplayRequest(BaseValidatorModel):
    ReplayName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CapacityProviderStrategyItem(BaseValidatorModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None


class Condition(BaseValidatorModel):
    Type: str
    Key: str
    Value: str


class ConnectionApiKeyAuthResponseParameters(BaseValidatorModel):
    ApiKeyName: Optional[str] = None


class ConnectionBasicAuthResponseParameters(BaseValidatorModel):
    Username: Optional[str] = None


class ConnectionBodyParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None


class ConnectionHeaderParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None


class ConnectionQueryStringParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None


class ConnectionOAuthClientResponseParameters(BaseValidatorModel):
    ClientID: Optional[str] = None


class Connection(BaseValidatorModel):
    ConnectionArn: Optional[str] = None
    Name: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    StateReason: Optional[str] = None
    AuthorizationType: Optional[ConnectionAuthorizationTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastAuthorizedTime: Optional[datetime] = None


class ConnectivityResourceConfigurationArn(BaseValidatorModel):
    ResourceConfigurationArn: str


# This class is the input for the 'create_api_destination' function.
class CreateApiDestinationRequest(BaseValidatorModel):
    Name: str
    ConnectionArn: str
    InvocationEndpoint: str
    HttpMethod: ApiDestinationHttpMethodType
    Description: Optional[str] = None
    InvocationRateLimitPerSecond: Optional[int] = None


# This class is the input for the 'create_archive' function.
class CreateArchiveRequest(BaseValidatorModel):
    ArchiveName: str
    EventSourceArn: str
    Description: Optional[str] = None
    EventPattern: Optional[str] = None
    RetentionDays: Optional[int] = None


class CreateConnectionApiKeyAuthRequestParameters(BaseValidatorModel):
    ApiKeyName: str
    ApiKeyValue: str


class CreateConnectionBasicAuthRequestParameters(BaseValidatorModel):
    Username: str
    Password: str


class CreateConnectionOAuthClientRequestParameters(BaseValidatorModel):
    ClientID: str
    ClientSecret: str


class EndpointEventBus(BaseValidatorModel):
    EventBusArn: str


class ReplicationConfig(BaseValidatorModel):
    State: Optional[ReplicationStateType] = None


class DeadLetterConfig(BaseValidatorModel):
    Arn: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'create_partner_event_source' function.
class CreatePartnerEventSourceRequest(BaseValidatorModel):
    Name: str
    Account: str


# This class is the input for the 'deactivate_event_source' function.
class DeactivateEventSourceRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'deauthorize_connection' function.
class DeauthorizeConnectionRequest(BaseValidatorModel):
    Name: str


class DeleteApiDestinationRequest(BaseValidatorModel):
    Name: str


class DeleteArchiveRequest(BaseValidatorModel):
    ArchiveName: str


# This class is the input for the 'delete_connection' function.
class DeleteConnectionRequest(BaseValidatorModel):
    Name: str


class DeleteEndpointRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_event_bus' function.
class DeleteEventBusRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_partner_event_source' function.
class DeletePartnerEventSourceRequest(BaseValidatorModel):
    Name: str
    Account: str


# This class is the input for the 'delete_rule' function.
class DeleteRuleRequest(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None
    Force: Optional[bool] = None


# This class is the input for the 'describe_api_destination' function.
class DescribeApiDestinationRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_archive' function.
class DescribeArchiveRequest(BaseValidatorModel):
    ArchiveName: str


class DescribeConnectionResourceParameters(BaseValidatorModel):
    ResourceConfigurationArn: str
    ResourceAssociationArn: str


# This class is the input for the 'describe_connection' function.
class DescribeConnectionRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_endpoint' function.
class DescribeEndpointRequest(BaseValidatorModel):
    Name: str
    HomeRegion: Optional[str] = None


# This class is the input for the 'describe_event_bus' function.
class DescribeEventBusRequest(BaseValidatorModel):
    Name: Optional[str] = None


# This class is the input for the 'describe_event_source' function.
class DescribeEventSourceRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_partner_event_source' function.
class DescribePartnerEventSourceRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_replay' function.
class DescribeReplayRequest(BaseValidatorModel):
    ReplayName: str


class ReplayDestinationOutput(BaseValidatorModel):
    Arn: str
    FilterArns: Optional[List[str]] = None


# This class is the input for the 'describe_rule' function.
class DescribeRuleRequest(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None


# This class is the input for the 'disable_rule' function.
class DisableRuleRequest(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None


class PlacementConstraint(BaseValidatorModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None


class PlacementStrategy(BaseValidatorModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None


# This class is the input for the 'enable_rule' function.
class EnableRuleRequest(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None


class EventBus(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Policy: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class EventSource(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[EventSourceStateType] = None


class Primary(BaseValidatorModel):
    HealthCheck: str


class Secondary(BaseValidatorModel):
    Route: str


class HttpParametersOutput(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class HttpParameters(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class InputTransformerOutput(BaseValidatorModel):
    InputTemplate: str
    InputPathsMap: Optional[Dict[str, str]] = None


class InputTransformer(BaseValidatorModel):
    InputTemplate: str
    InputPathsMap: Optional[Dict[str, str]] = None


class KinesisParameters(BaseValidatorModel):
    PartitionKeyPath: str


# This class is the input for the 'list_api_destinations' function.
class ListApiDestinationsRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    ConnectionArn: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_archives' function.
class ListArchivesRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ArchiveStateType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_connections' function.
class ListConnectionsRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_endpoints' function.
class ListEndpointsRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    HomeRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_event_buses' function.
class ListEventBusesRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_event_sources' function.
class ListEventSourcesRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_partner_event_source_accounts' function.
class ListPartnerEventSourceAccountsRequest(BaseValidatorModel):
    EventSourceName: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class PartnerEventSourceAccount(BaseValidatorModel):
    Account: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    State: Optional[EventSourceStateType] = None


# This class is the input for the 'list_partner_event_sources' function.
class ListPartnerEventSourcesRequest(BaseValidatorModel):
    NamePrefix: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class PartnerEventSource(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'list_replays' function.
class ListReplaysRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    State: Optional[ReplayStateType] = None
    EventSourceArn: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class Replay(BaseValidatorModel):
    ReplayName: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ReplayStateType] = None
    StateReason: Optional[str] = None
    EventStartTime: Optional[datetime] = None
    EventEndTime: Optional[datetime] = None
    EventLastReplayedTime: Optional[datetime] = None
    ReplayStartTime: Optional[datetime] = None
    ReplayEndTime: Optional[datetime] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_rule_names_by_target' function.
class ListRuleNamesByTargetRequest(BaseValidatorModel):
    TargetArn: str
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_rules' function.
class ListRulesRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class Rule(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    EventPattern: Optional[str] = None
    State: Optional[RuleStateType] = None
    Description: Optional[str] = None
    ScheduleExpression: Optional[str] = None
    RoleArn: Optional[str] = None
    ManagedBy: Optional[str] = None
    EventBusName: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'list_targets_by_rule' function.
class ListTargetsByRuleRequest(BaseValidatorModel):
    Rule: str
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

Timestamp = Union[datetime, str]


class PutEventsResultEntry(BaseValidatorModel):
    EventId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class PutPartnerEventsResultEntry(BaseValidatorModel):
    EventId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class PutTargetsResultEntry(BaseValidatorModel):
    TargetId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class RedshiftDataParametersOutput(BaseValidatorModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[List[str]] = None


class RedshiftDataParameters(BaseValidatorModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[List[str]] = None


# This class is the input for the 'remove_permission' function.
class RemovePermissionRequest(BaseValidatorModel):
    StatementId: Optional[str] = None
    RemoveAllPermissions: Optional[bool] = None
    EventBusName: Optional[str] = None


# This class is the input for the 'remove_targets' function.
class RemoveTargetsRequest(BaseValidatorModel):
    Rule: str
    Ids: List[str]
    EventBusName: Optional[str] = None
    Force: Optional[bool] = None


class RemoveTargetsResultEntry(BaseValidatorModel):
    TargetId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ReplayDestination(BaseValidatorModel):
    Arn: str
    FilterArns: Optional[List[str]] = None


class RetryPolicy(BaseValidatorModel):
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None


class RunCommandTargetOutput(BaseValidatorModel):
    Key: str
    Values: List[str]


class RunCommandTarget(BaseValidatorModel):
    Key: str
    Values: List[str]


class SageMakerPipelineParameter(BaseValidatorModel):
    Name: str
    Value: str


class SqsParameters(BaseValidatorModel):
    MessageGroupId: Optional[str] = None


# This class is the input for the 'test_event_pattern' function.
class TestEventPatternRequest(BaseValidatorModel):
    EventPattern: str
    Event: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_api_destination' function.
class UpdateApiDestinationRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    ConnectionArn: Optional[str] = None
    InvocationEndpoint: Optional[str] = None
    HttpMethod: Optional[ApiDestinationHttpMethodType] = None
    InvocationRateLimitPerSecond: Optional[int] = None


# This class is the input for the 'update_archive' function.
class UpdateArchiveRequest(BaseValidatorModel):
    ArchiveName: str
    Description: Optional[str] = None
    EventPattern: Optional[str] = None
    RetentionDays: Optional[int] = None


class UpdateConnectionApiKeyAuthRequestParameters(BaseValidatorModel):
    ApiKeyName: Optional[str] = None
    ApiKeyValue: Optional[str] = None


class UpdateConnectionBasicAuthRequestParameters(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None


class UpdateConnectionOAuthClientRequestParameters(BaseValidatorModel):
    ClientID: Optional[str] = None
    ClientSecret: Optional[str] = None


class NetworkConfigurationOutput(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutput] = None

AwsVpcConfigurationUnion = Union[AwsVpcConfiguration, AwsVpcConfigurationOutput]


class BatchParameters(BaseValidatorModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayProperties] = None
    RetryStrategy: Optional[BatchRetryStrategy] = None


# This class is the output for the 'cancel_replay' function.
class CancelReplayResponse(BaseValidatorModel):
    ReplayArn: str
    State: ReplayStateType
    StateReason: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_api_destination' function.
class CreateApiDestinationResponse(BaseValidatorModel):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_archive' function.
class CreateArchiveResponse(BaseValidatorModel):
    ArchiveArn: str
    State: ArchiveStateType
    StateReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_connection' function.
class CreateConnectionResponse(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_partner_event_source' function.
class CreatePartnerEventSourceResponse(BaseValidatorModel):
    EventSourceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deauthorize_connection' function.
class DeauthorizeConnectionResponse(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_connection' function.
class DeleteConnectionResponse(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_api_destination' function.
class DescribeApiDestinationResponse(BaseValidatorModel):
    ApiDestinationArn: str
    Name: str
    Description: str
    ApiDestinationState: ApiDestinationStateType
    ConnectionArn: str
    InvocationEndpoint: str
    HttpMethod: ApiDestinationHttpMethodType
    InvocationRateLimitPerSecond: int
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_archive' function.
class DescribeArchiveResponse(BaseValidatorModel):
    ArchiveArn: str
    ArchiveName: str
    EventSourceArn: str
    Description: str
    EventPattern: str
    State: ArchiveStateType
    StateReason: str
    RetentionDays: int
    SizeBytes: int
    EventCount: int
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_source' function.
class DescribeEventSourceResponse(BaseValidatorModel):
    Arn: str
    CreatedBy: str
    CreationTime: datetime
    ExpirationTime: datetime
    Name: str
    State: EventSourceStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_partner_event_source' function.
class DescribePartnerEventSourceResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_rule' function.
class DescribeRuleResponse(BaseValidatorModel):
    Name: str
    Arn: str
    EventPattern: str
    ScheduleExpression: str
    State: RuleStateType
    Description: str
    RoleArn: str
    ManagedBy: str
    EventBusName: str
    CreatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_permission' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_api_destinations' function.
class ListApiDestinationsResponse(BaseValidatorModel):
    ApiDestinations: List[ApiDestination]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_archives' function.
class ListArchivesResponse(BaseValidatorModel):
    Archives: List[Archive]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_rule_names_by_target' function.
class ListRuleNamesByTargetResponse(BaseValidatorModel):
    RuleNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_rule' function.
class PutRuleResponse(BaseValidatorModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_replay' function.
class StartReplayResponse(BaseValidatorModel):
    ReplayArn: str
    State: ReplayStateType
    StateReason: str
    ReplayStartTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_event_pattern' function.
class TestEventPatternResponse(BaseValidatorModel):
    Result: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_api_destination' function.
class UpdateApiDestinationResponse(BaseValidatorModel):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_archive' function.
class UpdateArchiveResponse(BaseValidatorModel):
    ArchiveArn: str
    State: ArchiveStateType
    StateReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_connection' function.
class UpdateConnectionResponse(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_permission' function.
class PutPermissionRequest(BaseValidatorModel):
    EventBusName: Optional[str] = None
    Action: Optional[str] = None
    Principal: Optional[str] = None
    StatementId: Optional[str] = None
    Condition: Optional[Condition] = None
    Policy: Optional[str] = None


class ConnectionHttpParametersOutput(BaseValidatorModel):
    HeaderParameters: Optional[List[ConnectionHeaderParameter]] = None
    QueryStringParameters: Optional[List[ConnectionQueryStringParameter]] = None
    BodyParameters: Optional[List[ConnectionBodyParameter]] = None


class ConnectionHttpParameters(BaseValidatorModel):
    HeaderParameters: Optional[List[ConnectionHeaderParameter]] = None
    QueryStringParameters: Optional[List[ConnectionQueryStringParameter]] = None
    BodyParameters: Optional[List[ConnectionBodyParameter]] = None


# This class is the output for the 'list_connections' function.
class ListConnectionsResponse(BaseValidatorModel):
    Connections: List[Connection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConnectivityResourceParameters(BaseValidatorModel):
    ResourceParameters: ConnectivityResourceConfigurationArn


# This class is the output for the 'create_event_bus' function.
class CreateEventBusResponse(BaseValidatorModel):
    EventBusArn: str
    Description: str
    KmsKeyIdentifier: str
    DeadLetterConfig: DeadLetterConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_bus' function.
class DescribeEventBusResponse(BaseValidatorModel):
    Name: str
    Arn: str
    Description: str
    KmsKeyIdentifier: str
    DeadLetterConfig: DeadLetterConfig
    Policy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_event_bus' function.
class UpdateEventBusRequest(BaseValidatorModel):
    Name: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None
    Description: Optional[str] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None


# This class is the output for the 'update_event_bus' function.
class UpdateEventBusResponse(BaseValidatorModel):
    Arn: str
    Name: str
    KmsKeyIdentifier: str
    Description: str
    DeadLetterConfig: DeadLetterConfig
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_event_bus' function.
class CreateEventBusRequest(BaseValidatorModel):
    Name: str
    EventSourceName: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_rule' function.
class PutRuleRequest(BaseValidatorModel):
    Name: str
    ScheduleExpression: Optional[str] = None
    EventPattern: Optional[str] = None
    State: Optional[RuleStateType] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EventBusName: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class DescribeConnectionConnectivityParameters(BaseValidatorModel):
    ResourceParameters: DescribeConnectionResourceParameters


# This class is the output for the 'describe_replay' function.
class DescribeReplayResponse(BaseValidatorModel):
    ReplayName: str
    ReplayArn: str
    Description: str
    State: ReplayStateType
    StateReason: str
    EventSourceArn: str
    Destination: ReplayDestinationOutput
    EventStartTime: datetime
    EventEndTime: datetime
    EventLastReplayedTime: datetime
    ReplayStartTime: datetime
    ReplayEndTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_event_buses' function.
class ListEventBusesResponse(BaseValidatorModel):
    EventBuses: List[EventBus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_event_sources' function.
class ListEventSourcesResponse(BaseValidatorModel):
    EventSources: List[EventSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FailoverConfig(BaseValidatorModel):
    Primary: Primary
    Secondary: Secondary

HttpParametersUnion = Union[HttpParameters, HttpParametersOutput]

InputTransformerUnion = Union[InputTransformer, InputTransformerOutput]


# This class is the output for the 'list_partner_event_source_accounts' function.
class ListPartnerEventSourceAccountsResponse(BaseValidatorModel):
    PartnerEventSourceAccounts: List[PartnerEventSourceAccount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_partner_event_sources' function.
class ListPartnerEventSourcesResponse(BaseValidatorModel):
    PartnerEventSources: List[PartnerEventSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_replays' function.
class ListReplaysResponse(BaseValidatorModel):
    Replays: List[Replay]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRuleNamesByTargetRequestPaginate(BaseValidatorModel):
    TargetArn: str
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesRequestPaginate(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetsByRuleRequestPaginate(BaseValidatorModel):
    Rule: str
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_rules' function.
class ListRulesResponse(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutEventsRequestEntry(BaseValidatorModel):
    Time: Optional[Timestamp] = None
    Source: Optional[str] = None
    Resources: Optional[List[str]] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None
    EventBusName: Optional[str] = None
    TraceHeader: Optional[str] = None


class PutPartnerEventsRequestEntry(BaseValidatorModel):
    Time: Optional[Timestamp] = None
    Source: Optional[str] = None
    Resources: Optional[List[str]] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None


# This class is the output for the 'put_events' function.
class PutEventsResponse(BaseValidatorModel):
    FailedEntryCount: int
    Entries: List[PutEventsResultEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_partner_events' function.
class PutPartnerEventsResponse(BaseValidatorModel):
    FailedEntryCount: int
    Entries: List[PutPartnerEventsResultEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_targets' function.
class PutTargetsResponse(BaseValidatorModel):
    FailedEntryCount: int
    FailedEntries: List[PutTargetsResultEntry]
    ResponseMetadata: ResponseMetadata

RedshiftDataParametersUnion = Union[RedshiftDataParameters, RedshiftDataParametersOutput]


# This class is the output for the 'remove_targets' function.
class RemoveTargetsResponse(BaseValidatorModel):
    FailedEntryCount: int
    FailedEntries: List[RemoveTargetsResultEntry]
    ResponseMetadata: ResponseMetadata

ReplayDestinationUnion = Union[ReplayDestination, ReplayDestinationOutput]


class RunCommandParametersOutput(BaseValidatorModel):
    RunCommandTargets: List[RunCommandTargetOutput]

RunCommandTargetUnion = Union[RunCommandTarget, RunCommandTargetOutput]


class SageMakerPipelineParametersOutput(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameter]] = None


class SageMakerPipelineParameters(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameter]] = None


class EcsParametersOutput(BaseValidatorModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationOutput] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraint]] = None
    PlacementStrategy: Optional[List[PlacementStrategy]] = None
    PropagateTags: Optional[Literal['TASK_DEFINITION']] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class NetworkConfiguration(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationUnion] = None


class ConnectionOAuthResponseParameters(BaseValidatorModel):
    ClientParameters: Optional[ConnectionOAuthClientResponseParameters] = None
    AuthorizationEndpoint: Optional[str] = None
    HttpMethod: Optional[ConnectionOAuthHttpMethodType] = None
    OAuthHttpParameters: Optional[ConnectionHttpParametersOutput] = None

ConnectionHttpParametersUnion = Union[ConnectionHttpParameters, ConnectionHttpParametersOutput]


class RoutingConfig(BaseValidatorModel):
    FailoverConfig: FailoverConfig


# This class is the input for the 'put_events' function.
class PutEventsRequest(BaseValidatorModel):
    Entries: List[PutEventsRequestEntry]
    EndpointId: Optional[str] = None


# This class is the input for the 'put_partner_events' function.
class PutPartnerEventsRequest(BaseValidatorModel):
    Entries: List[PutPartnerEventsRequestEntry]


# This class is the input for the 'start_replay' function.
class StartReplayRequest(BaseValidatorModel):
    ReplayName: str
    EventSourceArn: str
    EventStartTime: Timestamp
    EventEndTime: Timestamp
    Destination: ReplayDestinationUnion
    Description: Optional[str] = None


class RunCommandParameters(BaseValidatorModel):
    RunCommandTargets: List[RunCommandTargetUnion]

SageMakerPipelineParametersUnion = Union[SageMakerPipelineParameters, SageMakerPipelineParametersOutput]


class TargetOutput(BaseValidatorModel):
    Id: str
    Arn: str
    RoleArn: Optional[str] = None
    Input: Optional[str] = None
    InputPath: Optional[str] = None
    InputTransformer: Optional[InputTransformerOutput] = None
    KinesisParameters: Optional[KinesisParameters] = None
    RunCommandParameters: Optional[RunCommandParametersOutput] = None
    EcsParameters: Optional[EcsParametersOutput] = None
    BatchParameters: Optional[BatchParameters] = None
    SqsParameters: Optional[SqsParameters] = None
    HttpParameters: Optional[HttpParametersOutput] = None
    RedshiftDataParameters: Optional[RedshiftDataParametersOutput] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersOutput] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    RetryPolicy: Optional[RetryPolicy] = None
    AppSyncParameters: Optional[AppSyncParameters] = None

NetworkConfigurationUnion = Union[NetworkConfiguration, NetworkConfigurationOutput]


class ConnectionAuthResponseParameters(BaseValidatorModel):
    BasicAuthParameters: Optional[ConnectionBasicAuthResponseParameters] = None
    OAuthParameters: Optional[ConnectionOAuthResponseParameters] = None
    ApiKeyAuthParameters: Optional[ConnectionApiKeyAuthResponseParameters] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersOutput] = None
    ConnectivityParameters: Optional[DescribeConnectionConnectivityParameters] = None


class CreateConnectionOAuthRequestParameters(BaseValidatorModel):
    ClientParameters: CreateConnectionOAuthClientRequestParameters
    AuthorizationEndpoint: str
    HttpMethod: ConnectionOAuthHttpMethodType
    OAuthHttpParameters: Optional[ConnectionHttpParametersUnion] = None


class UpdateConnectionOAuthRequestParameters(BaseValidatorModel):
    ClientParameters: Optional[UpdateConnectionOAuthClientRequestParameters] = None
    AuthorizationEndpoint: Optional[str] = None
    HttpMethod: Optional[ConnectionOAuthHttpMethodType] = None
    OAuthHttpParameters: Optional[ConnectionHttpParametersUnion] = None


# This class is the input for the 'create_endpoint' function.
class CreateEndpointRequest(BaseValidatorModel):
    Name: str
    RoutingConfig: RoutingConfig
    EventBuses: List[EndpointEventBus]
    Description: Optional[str] = None
    ReplicationConfig: Optional[ReplicationConfig] = None
    RoleArn: Optional[str] = None


# This class is the output for the 'create_endpoint' function.
class CreateEndpointResponse(BaseValidatorModel):
    Name: str
    Arn: str
    RoutingConfig: RoutingConfig
    ReplicationConfig: ReplicationConfig
    EventBuses: List[EndpointEventBus]
    RoleArn: str
    State: EndpointStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_endpoint' function.
class DescribeEndpointResponse(BaseValidatorModel):
    Name: str
    Description: str
    Arn: str
    RoutingConfig: RoutingConfig
    ReplicationConfig: ReplicationConfig
    EventBuses: List[EndpointEventBus]
    RoleArn: str
    EndpointId: str
    EndpointUrl: str
    State: EndpointStateType
    StateReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class Endpoint(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None
    RoutingConfig: Optional[RoutingConfig] = None
    ReplicationConfig: Optional[ReplicationConfig] = None
    EventBuses: Optional[List[EndpointEventBus]] = None
    RoleArn: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    State: Optional[EndpointStateType] = None
    StateReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


# This class is the input for the 'update_endpoint' function.
class UpdateEndpointRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    RoutingConfig: Optional[RoutingConfig] = None
    ReplicationConfig: Optional[ReplicationConfig] = None
    EventBuses: Optional[List[EndpointEventBus]] = None
    RoleArn: Optional[str] = None


# This class is the output for the 'update_endpoint' function.
class UpdateEndpointResponse(BaseValidatorModel):
    Name: str
    Arn: str
    RoutingConfig: RoutingConfig
    ReplicationConfig: ReplicationConfig
    EventBuses: List[EndpointEventBus]
    RoleArn: str
    EndpointId: str
    EndpointUrl: str
    State: EndpointStateType
    ResponseMetadata: ResponseMetadata

RunCommandParametersUnion = Union[RunCommandParameters, RunCommandParametersOutput]


# This class is the output for the 'list_targets_by_rule' function.
class ListTargetsByRuleResponse(BaseValidatorModel):
    Targets: List[TargetOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EcsParameters(BaseValidatorModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationUnion] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraint]] = None
    PlacementStrategy: Optional[List[PlacementStrategy]] = None
    PropagateTags: Optional[Literal['TASK_DEFINITION']] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_connection' function.
class DescribeConnectionResponse(BaseValidatorModel):
    ConnectionArn: str
    Name: str
    Description: str
    InvocationConnectivityParameters: DescribeConnectionConnectivityParameters
    ConnectionState: ConnectionStateType
    StateReason: str
    AuthorizationType: ConnectionAuthorizationTypeType
    SecretArn: str
    AuthParameters: ConnectionAuthResponseParameters
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateConnectionAuthRequestParameters(BaseValidatorModel):
    BasicAuthParameters: Optional[CreateConnectionBasicAuthRequestParameters] = None
    OAuthParameters: Optional[CreateConnectionOAuthRequestParameters] = None
    ApiKeyAuthParameters: Optional[CreateConnectionApiKeyAuthRequestParameters] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersUnion] = None
    ConnectivityParameters: Optional[ConnectivityResourceParameters] = None


class UpdateConnectionAuthRequestParameters(BaseValidatorModel):
    BasicAuthParameters: Optional[UpdateConnectionBasicAuthRequestParameters] = None
    OAuthParameters: Optional[UpdateConnectionOAuthRequestParameters] = None
    ApiKeyAuthParameters: Optional[UpdateConnectionApiKeyAuthRequestParameters] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersUnion] = None
    ConnectivityParameters: Optional[ConnectivityResourceParameters] = None


# This class is the output for the 'list_endpoints' function.
class ListEndpointsResponse(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

EcsParametersUnion = Union[EcsParameters, EcsParametersOutput]


# This class is the input for the 'create_connection' function.
class CreateConnectionRequest(BaseValidatorModel):
    Name: str
    AuthorizationType: ConnectionAuthorizationTypeType
    AuthParameters: CreateConnectionAuthRequestParameters
    Description: Optional[str] = None
    InvocationConnectivityParameters: Optional[ConnectivityResourceParameters] = None


# This class is the input for the 'update_connection' function.
class UpdateConnectionRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    AuthorizationType: Optional[ConnectionAuthorizationTypeType] = None
    AuthParameters: Optional[UpdateConnectionAuthRequestParameters] = None
    InvocationConnectivityParameters: Optional[ConnectivityResourceParameters] = None


class Target(BaseValidatorModel):
    Id: str
    Arn: str
    RoleArn: Optional[str] = None
    Input: Optional[str] = None
    InputPath: Optional[str] = None
    InputTransformer: Optional[InputTransformerUnion] = None
    KinesisParameters: Optional[KinesisParameters] = None
    RunCommandParameters: Optional[RunCommandParametersUnion] = None
    EcsParameters: Optional[EcsParametersUnion] = None
    BatchParameters: Optional[BatchParameters] = None
    SqsParameters: Optional[SqsParameters] = None
    HttpParameters: Optional[HttpParametersUnion] = None
    RedshiftDataParameters: Optional[RedshiftDataParametersUnion] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersUnion] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    RetryPolicy: Optional[RetryPolicy] = None
    AppSyncParameters: Optional[AppSyncParameters] = None

TargetUnion = Union[Target, TargetOutput]


# This class is the input for the 'put_targets' function.
class PutTargetsRequest(BaseValidatorModel):
    Rule: str
    Targets: List[TargetUnion]
    EventBusName: Optional[str] = None