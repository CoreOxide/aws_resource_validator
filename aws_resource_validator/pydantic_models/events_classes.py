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
from aws_resource_validator.pydantic_models.events_constants import *

class ActivateEventSourceRequestRequestTypeDef(BaseModel):
    Name: str

class ApiDestinationTypeDef(BaseModel):
    ApiDestinationArn: Optional[str] = None
    Name: Optional[str] = None
    ApiDestinationState: Optional[ApiDestinationStateType] = None
    ConnectionArn: Optional[str] = None
    InvocationEndpoint: Optional[str] = None
    HttpMethod: Optional[ApiDestinationHttpMethodType] = None
    InvocationRateLimitPerSecond: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class AppSyncParametersTypeDef(BaseModel):
    GraphQLOperation: Optional[str] = None

class ArchiveTypeDef(BaseModel):
    ArchiveName: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ArchiveStateType] = None
    StateReason: Optional[str] = None
    RetentionDays: Optional[int] = None
    SizeBytes: Optional[int] = None
    EventCount: Optional[int] = None
    CreationTime: Optional[datetime] = None

class AwsVpcConfigurationExtraOutputTypeDef(BaseModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class AwsVpcConfigurationOutputTypeDef(BaseModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class AwsVpcConfigurationTypeDef(BaseModel):
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class BatchArrayPropertiesTypeDef(BaseModel):
    Size: Optional[int] = None

class BatchRetryStrategyTypeDef(BaseModel):
    Attempts: Optional[int] = None

class CancelReplayRequestRequestTypeDef(BaseModel):
    ReplayName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CapacityProviderStrategyItemTypeDef(BaseModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None

class ConditionTypeDef(BaseModel):
    Type: str
    Key: str
    Value: str

class ConnectionApiKeyAuthResponseParametersTypeDef(BaseModel):
    ApiKeyName: Optional[str] = None

class ConnectionBasicAuthResponseParametersTypeDef(BaseModel):
    Username: Optional[str] = None

class ConnectionBodyParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None

class ConnectionHeaderParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None

class ConnectionQueryStringParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None

class ConnectionOAuthClientResponseParametersTypeDef(BaseModel):
    ClientID: Optional[str] = None

class ConnectionTypeDef(BaseModel):
    ConnectionArn: Optional[str] = None
    Name: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    StateReason: Optional[str] = None
    AuthorizationType: Optional[ConnectionAuthorizationTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastAuthorizedTime: Optional[datetime] = None

class CreateApiDestinationRequestRequestTypeDef(BaseModel):
    Name: str
    ConnectionArn: str
    InvocationEndpoint: str
    HttpMethod: ApiDestinationHttpMethodType
    Description: Optional[str] = None
    InvocationRateLimitPerSecond: Optional[int] = None

class CreateArchiveRequestRequestTypeDef(BaseModel):
    ArchiveName: str
    EventSourceArn: str
    Description: Optional[str] = None
    EventPattern: Optional[str] = None
    RetentionDays: Optional[int] = None

class CreateConnectionApiKeyAuthRequestParametersTypeDef(BaseModel):
    ApiKeyName: str
    ApiKeyValue: str

class CreateConnectionBasicAuthRequestParametersTypeDef(BaseModel):
    Username: str
    Password: str

class CreateConnectionOAuthClientRequestParametersTypeDef(BaseModel):
    ClientID: str
    ClientSecret: str

class EndpointEventBusTypeDef(BaseModel):
    EventBusArn: str

class ReplicationConfigTypeDef(BaseModel):
    State: Optional[ReplicationStateType] = None

class DeadLetterConfigTypeDef(BaseModel):
    Arn: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreatePartnerEventSourceRequestRequestTypeDef(BaseModel):
    Name: str
    Account: str

class DeactivateEventSourceRequestRequestTypeDef(BaseModel):
    Name: str

class DeauthorizeConnectionRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteApiDestinationRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteArchiveRequestRequestTypeDef(BaseModel):
    ArchiveName: str

class DeleteConnectionRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteEndpointRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteEventBusRequestRequestTypeDef(BaseModel):
    Name: str

class DeletePartnerEventSourceRequestRequestTypeDef(BaseModel):
    Name: str
    Account: str

class DeleteRuleRequestRequestTypeDef(BaseModel):
    Name: str
    EventBusName: Optional[str] = None
    Force: Optional[bool] = None

class DescribeApiDestinationRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeArchiveRequestRequestTypeDef(BaseModel):
    ArchiveName: str

class DescribeConnectionRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeEndpointRequestRequestTypeDef(BaseModel):
    Name: str
    HomeRegion: Optional[str] = None

class DescribeEventBusRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None

class DescribeEventSourceRequestRequestTypeDef(BaseModel):
    Name: str

class DescribePartnerEventSourceRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeReplayRequestRequestTypeDef(BaseModel):
    ReplayName: str

class ReplayDestinationOutputTypeDef(BaseModel):
    Arn: str
    FilterArns: Optional[List[str]] = None

class DescribeRuleRequestRequestTypeDef(BaseModel):
    Name: str
    EventBusName: Optional[str] = None

class DisableRuleRequestRequestTypeDef(BaseModel):
    Name: str
    EventBusName: Optional[str] = None

class PlacementConstraintTypeDef(BaseModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None

class PlacementStrategyTypeDef(BaseModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None

class EnableRuleRequestRequestTypeDef(BaseModel):
    Name: str
    EventBusName: Optional[str] = None

class EventBusTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Policy: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class EventSourceTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[EventSourceStateType] = None

class PrimaryTypeDef(BaseModel):
    HealthCheck: str

class SecondaryTypeDef(BaseModel):
    Route: str

class HttpParametersExtraOutputTypeDef(BaseModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None

class HttpParametersOutputTypeDef(BaseModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None

class HttpParametersTypeDef(BaseModel):
    PathParameterValues: Optional[Sequence[str]] = None
    HeaderParameters: Optional[Mapping[str, str]] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None

class InputTransformerExtraOutputTypeDef(BaseModel):
    InputTemplate: str
    InputPathsMap: Optional[Dict[str, str]] = None

class InputTransformerOutputTypeDef(BaseModel):
    InputTemplate: str
    InputPathsMap: Optional[Dict[str, str]] = None

class InputTransformerTypeDef(BaseModel):
    InputTemplate: str
    InputPathsMap: Optional[Mapping[str, str]] = None

class KinesisParametersTypeDef(BaseModel):
    PartitionKeyPath: str

class ListApiDestinationsRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    ConnectionArn: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListArchivesRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ArchiveStateType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListConnectionsRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListEndpointsRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    HomeRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventBusesRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListEventSourcesRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListPartnerEventSourceAccountsRequestRequestTypeDef(BaseModel):
    EventSourceName: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PartnerEventSourceAccountTypeDef(BaseModel):
    Account: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    State: Optional[EventSourceStateType] = None

class ListPartnerEventSourcesRequestRequestTypeDef(BaseModel):
    NamePrefix: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PartnerEventSourceTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ListReplaysRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    State: Optional[ReplayStateType] = None
    EventSourceArn: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ReplayTypeDef(BaseModel):
    ReplayName: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ReplayStateType] = None
    StateReason: Optional[str] = None
    EventStartTime: Optional[datetime] = None
    EventEndTime: Optional[datetime] = None
    EventLastReplayedTime: Optional[datetime] = None
    ReplayStartTime: Optional[datetime] = None
    ReplayEndTime: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRuleNamesByTargetRequestRequestTypeDef(BaseModel):
    TargetArn: str
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListRulesRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class RuleTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    EventPattern: Optional[str] = None
    State: Optional[RuleStateType] = None
    Description: Optional[str] = None
    ScheduleExpression: Optional[str] = None
    RoleArn: Optional[str] = None
    ManagedBy: Optional[str] = None
    EventBusName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListTargetsByRuleRequestRequestTypeDef(BaseModel):
    Rule: str
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PutEventsResultEntryTypeDef(BaseModel):
    EventId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PutPartnerEventsResultEntryTypeDef(BaseModel):
    EventId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PutTargetsResultEntryTypeDef(BaseModel):
    TargetId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class RedshiftDataParametersExtraOutputTypeDef(BaseModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[List[str]] = None

class RedshiftDataParametersOutputTypeDef(BaseModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[List[str]] = None

class RedshiftDataParametersTypeDef(BaseModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[Sequence[str]] = None

class RemovePermissionRequestRequestTypeDef(BaseModel):
    StatementId: Optional[str] = None
    RemoveAllPermissions: Optional[bool] = None
    EventBusName: Optional[str] = None

class RemoveTargetsRequestRequestTypeDef(BaseModel):
    Rule: str
    Ids: Sequence[str]
    EventBusName: Optional[str] = None
    Force: Optional[bool] = None

class RemoveTargetsResultEntryTypeDef(BaseModel):
    TargetId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ReplayDestinationTypeDef(BaseModel):
    Arn: str
    FilterArns: Optional[Sequence[str]] = None

class RetryPolicyTypeDef(BaseModel):
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None

class RunCommandTargetExtraOutputTypeDef(BaseModel):
    Key: str
    Values: List[str]

class RunCommandTargetOutputTypeDef(BaseModel):
    Key: str
    Values: List[str]

class RunCommandTargetTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]

class SageMakerPipelineParameterTypeDef(BaseModel):
    Name: str
    Value: str

class SqsParametersTypeDef(BaseModel):
    MessageGroupId: Optional[str] = None

class TestEventPatternRequestRequestTypeDef(BaseModel):
    EventPattern: str
    Event: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateApiDestinationRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    ConnectionArn: Optional[str] = None
    InvocationEndpoint: Optional[str] = None
    HttpMethod: Optional[ApiDestinationHttpMethodType] = None
    InvocationRateLimitPerSecond: Optional[int] = None

class UpdateArchiveRequestRequestTypeDef(BaseModel):
    ArchiveName: str
    Description: Optional[str] = None
    EventPattern: Optional[str] = None
    RetentionDays: Optional[int] = None

class UpdateConnectionApiKeyAuthRequestParametersTypeDef(BaseModel):
    ApiKeyName: Optional[str] = None
    ApiKeyValue: Optional[str] = None

class UpdateConnectionBasicAuthRequestParametersTypeDef(BaseModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class UpdateConnectionOAuthClientRequestParametersTypeDef(BaseModel):
    ClientID: Optional[str] = None
    ClientSecret: Optional[str] = None

class NetworkConfigurationExtraOutputTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationExtraOutputTypeDef] = None

class NetworkConfigurationOutputTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutputTypeDef] = None

class NetworkConfigurationTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None

class BatchParametersTypeDef(BaseModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayPropertiesTypeDef] = None
    RetryStrategy: Optional[BatchRetryStrategyTypeDef] = None

class CancelReplayResponseTypeDef(BaseModel):
    ReplayArn: str
    State: ReplayStateType
    StateReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiDestinationResponseTypeDef(BaseModel):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateArchiveResponseTypeDef(BaseModel):
    ArchiveArn: str
    State: ArchiveStateType
    StateReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionResponseTypeDef(BaseModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePartnerEventSourceResponseTypeDef(BaseModel):
    EventSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeauthorizeConnectionResponseTypeDef(BaseModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(BaseModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApiDestinationResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeArchiveResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventSourceResponseTypeDef(BaseModel):
    Arn: str
    CreatedBy: str
    CreationTime: datetime
    ExpirationTime: datetime
    Name: str
    State: EventSourceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePartnerEventSourceResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuleResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListApiDestinationsResponseTypeDef(BaseModel):
    ApiDestinations: List[ApiDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListArchivesResponseTypeDef(BaseModel):
    Archives: List[ArchiveTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRuleNamesByTargetResponseTypeDef(BaseModel):
    RuleNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutRuleResponseTypeDef(BaseModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplayResponseTypeDef(BaseModel):
    ReplayArn: str
    State: ReplayStateType
    StateReason: str
    ReplayStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TestEventPatternResponseTypeDef(BaseModel):
    Result: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiDestinationResponseTypeDef(BaseModel):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateArchiveResponseTypeDef(BaseModel):
    ArchiveArn: str
    State: ArchiveStateType
    StateReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectionResponseTypeDef(BaseModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutPermissionRequestRequestTypeDef(BaseModel):
    EventBusName: Optional[str] = None
    Action: Optional[str] = None
    Principal: Optional[str] = None
    StatementId: Optional[str] = None
    Condition: Optional[ConditionTypeDef] = None
    Policy: Optional[str] = None

class ConnectionHttpParametersOutputTypeDef(BaseModel):
    HeaderParameters: Optional[List[ConnectionHeaderParameterTypeDef]] = None
    QueryStringParameters: Optional[List[ConnectionQueryStringParameterTypeDef]] = None
    BodyParameters: Optional[List[ConnectionBodyParameterTypeDef]] = None

class ConnectionHttpParametersTypeDef(BaseModel):
    HeaderParameters: Optional[Sequence[ConnectionHeaderParameterTypeDef]] = None
    QueryStringParameters: Optional[Sequence[ConnectionQueryStringParameterTypeDef]] = None
    BodyParameters: Optional[Sequence[ConnectionBodyParameterTypeDef]] = None

class ListConnectionsResponseTypeDef(BaseModel):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEventBusResponseTypeDef(BaseModel):
    EventBusArn: str
    Description: str
    KmsKeyIdentifier: str
    DeadLetterConfig: DeadLetterConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventBusResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    Description: str
    KmsKeyIdentifier: str
    DeadLetterConfig: DeadLetterConfigTypeDef
    Policy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventBusRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None
    Description: Optional[str] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None

class UpdateEventBusResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    KmsKeyIdentifier: str
    Description: str
    DeadLetterConfig: DeadLetterConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventBusRequestRequestTypeDef(BaseModel):
    Name: str
    EventSourceName: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuleRequestRequestTypeDef(BaseModel):
    Name: str
    ScheduleExpression: Optional[str] = None
    EventPattern: Optional[str] = None
    State: Optional[RuleStateType] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EventBusName: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DescribeReplayResponseTypeDef(BaseModel):
    ReplayName: str
    ReplayArn: str
    Description: str
    State: ReplayStateType
    StateReason: str
    EventSourceArn: str
    Destination: ReplayDestinationOutputTypeDef
    EventStartTime: datetime
    EventEndTime: datetime
    EventLastReplayedTime: datetime
    ReplayStartTime: datetime
    ReplayEndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventBusesResponseTypeDef(BaseModel):
    EventBuses: List[EventBusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEventSourcesResponseTypeDef(BaseModel):
    EventSources: List[EventSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailoverConfigTypeDef(BaseModel):
    Primary: PrimaryTypeDef
    Secondary: SecondaryTypeDef

class ListPartnerEventSourceAccountsResponseTypeDef(BaseModel):
    PartnerEventSourceAccounts: List[PartnerEventSourceAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPartnerEventSourcesResponseTypeDef(BaseModel):
    PartnerEventSources: List[PartnerEventSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListReplaysResponseTypeDef(BaseModel):
    Replays: List[ReplayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef(BaseModel):
    TargetArn: str
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef(BaseModel):
    Rule: str
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesResponseTypeDef(BaseModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutEventsRequestEntryTypeDef(BaseModel):
    Time: Optional[TimestampTypeDef] = None
    Source: Optional[str] = None
    Resources: Optional[Sequence[str]] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None
    EventBusName: Optional[str] = None
    TraceHeader: Optional[str] = None

class PutPartnerEventsRequestEntryTypeDef(BaseModel):
    Time: Optional[TimestampTypeDef] = None
    Source: Optional[str] = None
    Resources: Optional[Sequence[str]] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None

class PutEventsResponseTypeDef(BaseModel):
    FailedEntryCount: int
    Entries: List[PutEventsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPartnerEventsResponseTypeDef(BaseModel):
    FailedEntryCount: int
    Entries: List[PutPartnerEventsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutTargetsResponseTypeDef(BaseModel):
    FailedEntryCount: int
    FailedEntries: List[PutTargetsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveTargetsResponseTypeDef(BaseModel):
    FailedEntryCount: int
    FailedEntries: List[RemoveTargetsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplayRequestRequestTypeDef(BaseModel):
    ReplayName: str
    EventSourceArn: str
    EventStartTime: TimestampTypeDef
    EventEndTime: TimestampTypeDef
    Destination: ReplayDestinationTypeDef
    Description: Optional[str] = None

class RunCommandParametersExtraOutputTypeDef(BaseModel):
    RunCommandTargets: List[RunCommandTargetExtraOutputTypeDef]

class RunCommandParametersOutputTypeDef(BaseModel):
    RunCommandTargets: List[RunCommandTargetOutputTypeDef]

class RunCommandParametersTypeDef(BaseModel):
    RunCommandTargets: Sequence[RunCommandTargetTypeDef]

class SageMakerPipelineParametersExtraOutputTypeDef(BaseModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameterTypeDef]] = None

class SageMakerPipelineParametersOutputTypeDef(BaseModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameterTypeDef]] = None

class SageMakerPipelineParametersTypeDef(BaseModel):
    PipelineParameterList: Optional[Sequence[SageMakerPipelineParameterTypeDef]] = None

class EcsParametersExtraOutputTypeDef(BaseModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationExtraOutputTypeDef] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraintTypeDef]] = None
    PlacementStrategy: Optional[List[PlacementStrategyTypeDef]] = None
    PropagateTags: Optional[Literal["TASK_DEFINITION"]] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EcsParametersOutputTypeDef(BaseModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraintTypeDef]] = None
    PlacementStrategy: Optional[List[PlacementStrategyTypeDef]] = None
    PropagateTags: Optional[Literal["TASK_DEFINITION"]] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EcsParametersTypeDef(BaseModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    PlacementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    PropagateTags: Optional[Literal["TASK_DEFINITION"]] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ConnectionOAuthResponseParametersTypeDef(BaseModel):
    ClientParameters: Optional[ConnectionOAuthClientResponseParametersTypeDef] = None
    AuthorizationEndpoint: Optional[str] = None
    HttpMethod: Optional[ConnectionOAuthHttpMethodType] = None
    OAuthHttpParameters: Optional[ConnectionHttpParametersOutputTypeDef] = None

class CreateConnectionOAuthRequestParametersTypeDef(BaseModel):
    ClientParameters: CreateConnectionOAuthClientRequestParametersTypeDef
    AuthorizationEndpoint: str
    HttpMethod: ConnectionOAuthHttpMethodType
    OAuthHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class UpdateConnectionOAuthRequestParametersTypeDef(BaseModel):
    ClientParameters: Optional[UpdateConnectionOAuthClientRequestParametersTypeDef] = None
    AuthorizationEndpoint: Optional[str] = None
    HttpMethod: Optional[ConnectionOAuthHttpMethodType] = None
    OAuthHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class RoutingConfigTypeDef(BaseModel):
    FailoverConfig: FailoverConfigTypeDef

class PutEventsRequestRequestTypeDef(BaseModel):
    Entries: Sequence[PutEventsRequestEntryTypeDef]
    EndpointId: Optional[str] = None

class PutPartnerEventsRequestRequestTypeDef(BaseModel):
    Entries: Sequence[PutPartnerEventsRequestEntryTypeDef]

class TargetExtraOutputTypeDef(BaseModel):
    Id: str
    Arn: str
    RoleArn: Optional[str] = None
    Input: Optional[str] = None
    InputPath: Optional[str] = None
    InputTransformer: Optional[InputTransformerExtraOutputTypeDef] = None
    KinesisParameters: Optional[KinesisParametersTypeDef] = None
    RunCommandParameters: Optional[RunCommandParametersExtraOutputTypeDef] = None
    EcsParameters: Optional[EcsParametersExtraOutputTypeDef] = None
    BatchParameters: Optional[BatchParametersTypeDef] = None
    SqsParameters: Optional[SqsParametersTypeDef] = None
    HttpParameters: Optional[HttpParametersExtraOutputTypeDef] = None
    RedshiftDataParameters: Optional[RedshiftDataParametersExtraOutputTypeDef] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersExtraOutputTypeDef] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    RetryPolicy: Optional[RetryPolicyTypeDef] = None
    AppSyncParameters: Optional[AppSyncParametersTypeDef] = None

class TargetOutputTypeDef(BaseModel):
    Id: str
    Arn: str
    RoleArn: Optional[str] = None
    Input: Optional[str] = None
    InputPath: Optional[str] = None
    InputTransformer: Optional[InputTransformerOutputTypeDef] = None
    KinesisParameters: Optional[KinesisParametersTypeDef] = None
    RunCommandParameters: Optional[RunCommandParametersOutputTypeDef] = None
    EcsParameters: Optional[EcsParametersOutputTypeDef] = None
    BatchParameters: Optional[BatchParametersTypeDef] = None
    SqsParameters: Optional[SqsParametersTypeDef] = None
    HttpParameters: Optional[HttpParametersOutputTypeDef] = None
    RedshiftDataParameters: Optional[RedshiftDataParametersOutputTypeDef] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersOutputTypeDef] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    RetryPolicy: Optional[RetryPolicyTypeDef] = None
    AppSyncParameters: Optional[AppSyncParametersTypeDef] = None

class TargetTypeDef(BaseModel):
    Id: str
    Arn: str
    RoleArn: Optional[str] = None
    Input: Optional[str] = None
    InputPath: Optional[str] = None
    InputTransformer: Optional[InputTransformerTypeDef] = None
    KinesisParameters: Optional[KinesisParametersTypeDef] = None
    RunCommandParameters: Optional[RunCommandParametersTypeDef] = None
    EcsParameters: Optional[EcsParametersTypeDef] = None
    BatchParameters: Optional[BatchParametersTypeDef] = None
    SqsParameters: Optional[SqsParametersTypeDef] = None
    HttpParameters: Optional[HttpParametersTypeDef] = None
    RedshiftDataParameters: Optional[RedshiftDataParametersTypeDef] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersTypeDef] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    RetryPolicy: Optional[RetryPolicyTypeDef] = None
    AppSyncParameters: Optional[AppSyncParametersTypeDef] = None

class ConnectionAuthResponseParametersTypeDef(BaseModel):
    BasicAuthParameters: Optional[ConnectionBasicAuthResponseParametersTypeDef] = None
    OAuthParameters: Optional[ConnectionOAuthResponseParametersTypeDef] = None
    ApiKeyAuthParameters: Optional[ConnectionApiKeyAuthResponseParametersTypeDef] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersOutputTypeDef] = None

class CreateConnectionAuthRequestParametersTypeDef(BaseModel):
    BasicAuthParameters: Optional[CreateConnectionBasicAuthRequestParametersTypeDef] = None
    OAuthParameters: Optional[CreateConnectionOAuthRequestParametersTypeDef] = None
    ApiKeyAuthParameters: Optional[CreateConnectionApiKeyAuthRequestParametersTypeDef] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class UpdateConnectionAuthRequestParametersTypeDef(BaseModel):
    BasicAuthParameters: Optional[UpdateConnectionBasicAuthRequestParametersTypeDef] = None
    OAuthParameters: Optional[UpdateConnectionOAuthRequestParametersTypeDef] = None
    ApiKeyAuthParameters: Optional[UpdateConnectionApiKeyAuthRequestParametersTypeDef] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class CreateEndpointRequestRequestTypeDef(BaseModel):
    Name: str
    RoutingConfig: RoutingConfigTypeDef
    EventBuses: Sequence[EndpointEventBusTypeDef]
    Description: Optional[str] = None
    ReplicationConfig: Optional[ReplicationConfigTypeDef] = None
    RoleArn: Optional[str] = None

class CreateEndpointResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    RoutingConfig: RoutingConfigTypeDef
    ReplicationConfig: ReplicationConfigTypeDef
    EventBuses: List[EndpointEventBusTypeDef]
    RoleArn: str
    State: EndpointStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointResponseTypeDef(BaseModel):
    Name: str
    Description: str
    Arn: str
    RoutingConfig: RoutingConfigTypeDef
    ReplicationConfig: ReplicationConfigTypeDef
    EventBuses: List[EndpointEventBusTypeDef]
    RoleArn: str
    EndpointId: str
    EndpointUrl: str
    State: EndpointStateType
    StateReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None
    RoutingConfig: Optional[RoutingConfigTypeDef] = None
    ReplicationConfig: Optional[ReplicationConfigTypeDef] = None
    EventBuses: Optional[List[EndpointEventBusTypeDef]] = None
    RoleArn: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    State: Optional[EndpointStateType] = None
    StateReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class UpdateEndpointRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    RoutingConfig: Optional[RoutingConfigTypeDef] = None
    ReplicationConfig: Optional[ReplicationConfigTypeDef] = None
    EventBuses: Optional[Sequence[EndpointEventBusTypeDef]] = None
    RoleArn: Optional[str] = None

class UpdateEndpointResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    RoutingConfig: RoutingConfigTypeDef
    ReplicationConfig: ReplicationConfigTypeDef
    EventBuses: List[EndpointEventBusTypeDef]
    RoleArn: str
    EndpointId: str
    EndpointUrl: str
    State: EndpointStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsByRuleResponseTypeDef(BaseModel):
    Targets: List[TargetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConnectionResponseTypeDef(BaseModel):
    ConnectionArn: str
    Name: str
    Description: str
    ConnectionState: ConnectionStateType
    StateReason: str
    AuthorizationType: ConnectionAuthorizationTypeType
    SecretArn: str
    AuthParameters: ConnectionAuthResponseParametersTypeDef
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionRequestRequestTypeDef(BaseModel):
    Name: str
    AuthorizationType: ConnectionAuthorizationTypeType
    AuthParameters: CreateConnectionAuthRequestParametersTypeDef
    Description: Optional[str] = None

class UpdateConnectionRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    AuthorizationType: Optional[ConnectionAuthorizationTypeType] = None
    AuthParameters: Optional[UpdateConnectionAuthRequestParametersTypeDef] = None

class ListEndpointsResponseTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutTargetsRequestRequestTypeDef(BaseModel):
    Rule: str
    Targets: Sequence[TargetUnionTypeDef]
    EventBusName: Optional[str] = None

