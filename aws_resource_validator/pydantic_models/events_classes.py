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
from aws_resource_validator.pydantic_models.events_constants import *

class ActivateEventSourceRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class ApiDestinationTypeDef(BaseValidatorModel):
    ApiDestinationArn: Optional[str] = None
    Name: Optional[str] = None
    ApiDestinationState: Optional[ApiDestinationStateType] = None
    ConnectionArn: Optional[str] = None
    InvocationEndpoint: Optional[str] = None
    HttpMethod: Optional[ApiDestinationHttpMethodType] = None
    InvocationRateLimitPerSecond: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class AppSyncParametersTypeDef(BaseValidatorModel):
    GraphQLOperation: Optional[str] = None

class ArchiveTypeDef(BaseValidatorModel):
    ArchiveName: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ArchiveStateType] = None
    StateReason: Optional[str] = None
    RetentionDays: Optional[int] = None
    SizeBytes: Optional[int] = None
    EventCount: Optional[int] = None
    CreationTime: Optional[datetime] = None

class AwsVpcConfigurationExtraOutputTypeDef(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class AwsVpcConfigurationOutputTypeDef(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class AwsVpcConfigurationTypeDef(BaseValidatorModel):
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class BatchArrayPropertiesTypeDef(BaseValidatorModel):
    Size: Optional[int] = None

class BatchRetryStrategyTypeDef(BaseValidatorModel):
    Attempts: Optional[int] = None

class CancelReplayRequestRequestTypeDef(BaseValidatorModel):
    ReplayName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CapacityProviderStrategyItemTypeDef(BaseValidatorModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None

class ConditionTypeDef(BaseValidatorModel):
    Type: str
    Key: str
    Value: str

class ConnectionApiKeyAuthResponseParametersTypeDef(BaseValidatorModel):
    ApiKeyName: Optional[str] = None

class ConnectionBasicAuthResponseParametersTypeDef(BaseValidatorModel):
    Username: Optional[str] = None

class ConnectionBodyParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None

class ConnectionHeaderParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None

class ConnectionQueryStringParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    IsValueSecret: Optional[bool] = None

class ConnectionOAuthClientResponseParametersTypeDef(BaseValidatorModel):
    ClientID: Optional[str] = None

class ConnectionTypeDef(BaseValidatorModel):
    ConnectionArn: Optional[str] = None
    Name: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    StateReason: Optional[str] = None
    AuthorizationType: Optional[ConnectionAuthorizationTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastAuthorizedTime: Optional[datetime] = None

class CreateApiDestinationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ConnectionArn: str
    InvocationEndpoint: str
    HttpMethod: ApiDestinationHttpMethodType
    Description: Optional[str] = None
    InvocationRateLimitPerSecond: Optional[int] = None

class CreateArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveName: str
    EventSourceArn: str
    Description: Optional[str] = None
    EventPattern: Optional[str] = None
    RetentionDays: Optional[int] = None

class CreateConnectionApiKeyAuthRequestParametersTypeDef(BaseValidatorModel):
    ApiKeyName: str
    ApiKeyValue: str

class CreateConnectionBasicAuthRequestParametersTypeDef(BaseValidatorModel):
    Username: str
    Password: str

class CreateConnectionOAuthClientRequestParametersTypeDef(BaseValidatorModel):
    ClientID: str
    ClientSecret: str

class EndpointEventBusTypeDef(BaseValidatorModel):
    EventBusArn: str

class ReplicationConfigTypeDef(BaseValidatorModel):
    State: Optional[ReplicationStateType] = None

class DeadLetterConfigTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreatePartnerEventSourceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Account: str

class DeactivateEventSourceRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeauthorizeConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteApiDestinationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveName: str

class DeleteConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteEndpointRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteEventBusRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeletePartnerEventSourceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Account: str

class DeleteRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None
    Force: Optional[bool] = None

class DescribeApiDestinationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveName: str

class DescribeConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeEndpointRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    HomeRegion: Optional[str] = None

class DescribeEventBusRequestRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class DescribeEventSourceRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribePartnerEventSourceRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeReplayRequestRequestTypeDef(BaseValidatorModel):
    ReplayName: str

class ReplayDestinationOutputTypeDef(BaseValidatorModel):
    Arn: str
    FilterArns: Optional[List[str]] = None

class DescribeRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None

class DisableRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None

class PlacementConstraintTypeDef(BaseValidatorModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None

class PlacementStrategyTypeDef(BaseValidatorModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None

class EnableRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventBusName: Optional[str] = None

class EventBusTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Policy: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class EventSourceTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[EventSourceStateType] = None

class PrimaryTypeDef(BaseValidatorModel):
    HealthCheck: str

class SecondaryTypeDef(BaseValidatorModel):
    Route: str

class HttpParametersExtraOutputTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None

class HttpParametersOutputTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None

class HttpParametersTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[Sequence[str]] = None
    HeaderParameters: Optional[Mapping[str, str]] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None

class InputTransformerExtraOutputTypeDef(BaseValidatorModel):
    InputTemplate: str
    InputPathsMap: Optional[Dict[str, str]] = None

class InputTransformerOutputTypeDef(BaseValidatorModel):
    InputTemplate: str
    InputPathsMap: Optional[Dict[str, str]] = None

class InputTransformerTypeDef(BaseValidatorModel):
    InputTemplate: str
    InputPathsMap: Optional[Mapping[str, str]] = None

class KinesisParametersTypeDef(BaseValidatorModel):
    PartitionKeyPath: str

class ListApiDestinationsRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    ConnectionArn: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListArchivesRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ArchiveStateType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListConnectionsRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListEndpointsRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    HomeRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventBusesRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListEventSourcesRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListPartnerEventSourceAccountsRequestRequestTypeDef(BaseValidatorModel):
    EventSourceName: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PartnerEventSourceAccountTypeDef(BaseValidatorModel):
    Account: Optional[str] = None
    CreationTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    State: Optional[EventSourceStateType] = None

class ListPartnerEventSourcesRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PartnerEventSourceTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ListReplaysRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    State: Optional[ReplayStateType] = None
    EventSourceArn: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ReplayTypeDef(BaseValidatorModel):
    ReplayName: Optional[str] = None
    EventSourceArn: Optional[str] = None
    State: Optional[ReplayStateType] = None
    StateReason: Optional[str] = None
    EventStartTime: Optional[datetime] = None
    EventEndTime: Optional[datetime] = None
    EventLastReplayedTime: Optional[datetime] = None
    ReplayStartTime: Optional[datetime] = None
    ReplayEndTime: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRuleNamesByTargetRequestRequestTypeDef(BaseValidatorModel):
    TargetArn: str
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListRulesRequestRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class RuleTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    EventPattern: Optional[str] = None
    State: Optional[RuleStateType] = None
    Description: Optional[str] = None
    ScheduleExpression: Optional[str] = None
    RoleArn: Optional[str] = None
    ManagedBy: Optional[str] = None
    EventBusName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListTargetsByRuleRequestRequestTypeDef(BaseValidatorModel):
    Rule: str
    EventBusName: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PutEventsResultEntryTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PutPartnerEventsResultEntryTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PutTargetsResultEntryTypeDef(BaseValidatorModel):
    TargetId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class RedshiftDataParametersExtraOutputTypeDef(BaseValidatorModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[List[str]] = None

class RedshiftDataParametersOutputTypeDef(BaseValidatorModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[List[str]] = None

class RedshiftDataParametersTypeDef(BaseValidatorModel):
    Database: str
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    Sql: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    Sqls: Optional[Sequence[str]] = None

class RemovePermissionRequestRequestTypeDef(BaseValidatorModel):
    StatementId: Optional[str] = None
    RemoveAllPermissions: Optional[bool] = None
    EventBusName: Optional[str] = None

class RemoveTargetsRequestRequestTypeDef(BaseValidatorModel):
    Rule: str
    Ids: Sequence[str]
    EventBusName: Optional[str] = None
    Force: Optional[bool] = None

class RemoveTargetsResultEntryTypeDef(BaseValidatorModel):
    TargetId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ReplayDestinationTypeDef(BaseValidatorModel):
    Arn: str
    FilterArns: Optional[Sequence[str]] = None

class RetryPolicyTypeDef(BaseValidatorModel):
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None

class RunCommandTargetExtraOutputTypeDef(BaseValidatorModel):
    Key: str
    Values: List[str]

class RunCommandTargetOutputTypeDef(BaseValidatorModel):
    Key: str
    Values: List[str]

class RunCommandTargetTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]

class SageMakerPipelineParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class SqsParametersTypeDef(BaseValidatorModel):
    MessageGroupId: Optional[str] = None

class TestEventPatternRequestRequestTypeDef(BaseValidatorModel):
    EventPattern: str
    Event: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateApiDestinationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    ConnectionArn: Optional[str] = None
    InvocationEndpoint: Optional[str] = None
    HttpMethod: Optional[ApiDestinationHttpMethodType] = None
    InvocationRateLimitPerSecond: Optional[int] = None

class UpdateArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveName: str
    Description: Optional[str] = None
    EventPattern: Optional[str] = None
    RetentionDays: Optional[int] = None

class UpdateConnectionApiKeyAuthRequestParametersTypeDef(BaseValidatorModel):
    ApiKeyName: Optional[str] = None
    ApiKeyValue: Optional[str] = None

class UpdateConnectionBasicAuthRequestParametersTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class UpdateConnectionOAuthClientRequestParametersTypeDef(BaseValidatorModel):
    ClientID: Optional[str] = None
    ClientSecret: Optional[str] = None

class NetworkConfigurationExtraOutputTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationExtraOutputTypeDef] = None

class NetworkConfigurationOutputTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutputTypeDef] = None

class NetworkConfigurationTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None

class BatchParametersTypeDef(BaseValidatorModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayPropertiesTypeDef] = None
    RetryStrategy: Optional[BatchRetryStrategyTypeDef] = None

class CancelReplayResponseTypeDef(BaseValidatorModel):
    ReplayArn: str
    State: ReplayStateType
    StateReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiDestinationResponseTypeDef(BaseValidatorModel):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateArchiveResponseTypeDef(BaseValidatorModel):
    ArchiveArn: str
    State: ArchiveStateType
    StateReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionResponseTypeDef(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePartnerEventSourceResponseTypeDef(BaseValidatorModel):
    EventSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeauthorizeConnectionResponseTypeDef(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApiDestinationResponseTypeDef(BaseValidatorModel):
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

class DescribeArchiveResponseTypeDef(BaseValidatorModel):
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

class DescribeEventSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedBy: str
    CreationTime: datetime
    ExpirationTime: datetime
    Name: str
    State: EventSourceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePartnerEventSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuleResponseTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListApiDestinationsResponseTypeDef(BaseValidatorModel):
    ApiDestinations: List[ApiDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListArchivesResponseTypeDef(BaseValidatorModel):
    Archives: List[ArchiveTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRuleNamesByTargetResponseTypeDef(BaseValidatorModel):
    RuleNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutRuleResponseTypeDef(BaseValidatorModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplayResponseTypeDef(BaseValidatorModel):
    ReplayArn: str
    State: ReplayStateType
    StateReason: str
    ReplayStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TestEventPatternResponseTypeDef(BaseValidatorModel):
    Result: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiDestinationResponseTypeDef(BaseValidatorModel):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateArchiveResponseTypeDef(BaseValidatorModel):
    ArchiveArn: str
    State: ArchiveStateType
    StateReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectionResponseTypeDef(BaseValidatorModel):
    ConnectionArn: str
    ConnectionState: ConnectionStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutPermissionRequestRequestTypeDef(BaseValidatorModel):
    EventBusName: Optional[str] = None
    Action: Optional[str] = None
    Principal: Optional[str] = None
    StatementId: Optional[str] = None
    Condition: Optional[ConditionTypeDef] = None
    Policy: Optional[str] = None

class ConnectionHttpParametersOutputTypeDef(BaseValidatorModel):
    HeaderParameters: Optional[List[ConnectionHeaderParameterTypeDef]] = None
    QueryStringParameters: Optional[List[ConnectionQueryStringParameterTypeDef]] = None
    BodyParameters: Optional[List[ConnectionBodyParameterTypeDef]] = None

class ConnectionHttpParametersTypeDef(BaseValidatorModel):
    HeaderParameters: Optional[Sequence[ConnectionHeaderParameterTypeDef]] = None
    QueryStringParameters: Optional[Sequence[ConnectionQueryStringParameterTypeDef]] = None
    BodyParameters: Optional[Sequence[ConnectionBodyParameterTypeDef]] = None

class ListConnectionsResponseTypeDef(BaseValidatorModel):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEventBusResponseTypeDef(BaseValidatorModel):
    EventBusArn: str
    Description: str
    KmsKeyIdentifier: str
    DeadLetterConfig: DeadLetterConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventBusResponseTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    Description: str
    KmsKeyIdentifier: str
    DeadLetterConfig: DeadLetterConfigTypeDef
    Policy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventBusRequestRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None
    Description: Optional[str] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None

class UpdateEventBusResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    KmsKeyIdentifier: str
    Description: str
    DeadLetterConfig: DeadLetterConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventBusRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventSourceName: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ScheduleExpression: Optional[str] = None
    EventPattern: Optional[str] = None
    State: Optional[RuleStateType] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EventBusName: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DescribeReplayResponseTypeDef(BaseValidatorModel):
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

class ListEventBusesResponseTypeDef(BaseValidatorModel):
    EventBuses: List[EventBusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEventSourcesResponseTypeDef(BaseValidatorModel):
    EventSources: List[EventSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailoverConfigTypeDef(BaseValidatorModel):
    Primary: PrimaryTypeDef
    Secondary: SecondaryTypeDef

class ListPartnerEventSourceAccountsResponseTypeDef(BaseValidatorModel):
    PartnerEventSourceAccounts: List[PartnerEventSourceAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPartnerEventSourcesResponseTypeDef(BaseValidatorModel):
    PartnerEventSources: List[PartnerEventSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListReplaysResponseTypeDef(BaseValidatorModel):
    Replays: List[ReplayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef(BaseValidatorModel):
    TargetArn: str
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef(BaseValidatorModel):
    Rule: str
    EventBusName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutEventsRequestEntryTypeDef(BaseValidatorModel):
    Time: Optional[TimestampTypeDef] = None
    Source: Optional[str] = None
    Resources: Optional[Sequence[str]] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None
    EventBusName: Optional[str] = None
    TraceHeader: Optional[str] = None

class PutPartnerEventsRequestEntryTypeDef(BaseValidatorModel):
    Time: Optional[TimestampTypeDef] = None
    Source: Optional[str] = None
    Resources: Optional[Sequence[str]] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None

class PutEventsResponseTypeDef(BaseValidatorModel):
    FailedEntryCount: int
    Entries: List[PutEventsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPartnerEventsResponseTypeDef(BaseValidatorModel):
    FailedEntryCount: int
    Entries: List[PutPartnerEventsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutTargetsResponseTypeDef(BaseValidatorModel):
    FailedEntryCount: int
    FailedEntries: List[PutTargetsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveTargetsResponseTypeDef(BaseValidatorModel):
    FailedEntryCount: int
    FailedEntries: List[RemoveTargetsResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplayRequestRequestTypeDef(BaseValidatorModel):
    ReplayName: str
    EventSourceArn: str
    EventStartTime: TimestampTypeDef
    EventEndTime: TimestampTypeDef
    Destination: ReplayDestinationTypeDef
    Description: Optional[str] = None

class RunCommandParametersExtraOutputTypeDef(BaseValidatorModel):
    RunCommandTargets: List[RunCommandTargetExtraOutputTypeDef]

class RunCommandParametersOutputTypeDef(BaseValidatorModel):
    RunCommandTargets: List[RunCommandTargetOutputTypeDef]

class RunCommandParametersTypeDef(BaseValidatorModel):
    RunCommandTargets: Sequence[RunCommandTargetTypeDef]

class SageMakerPipelineParametersExtraOutputTypeDef(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameterTypeDef]] = None

class SageMakerPipelineParametersOutputTypeDef(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameterTypeDef]] = None

class SageMakerPipelineParametersTypeDef(BaseValidatorModel):
    PipelineParameterList: Optional[Sequence[SageMakerPipelineParameterTypeDef]] = None

class EcsParametersExtraOutputTypeDef(BaseValidatorModel):
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

class EcsParametersOutputTypeDef(BaseValidatorModel):
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

class EcsParametersTypeDef(BaseValidatorModel):
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

class ConnectionOAuthResponseParametersTypeDef(BaseValidatorModel):
    ClientParameters: Optional[ConnectionOAuthClientResponseParametersTypeDef] = None
    AuthorizationEndpoint: Optional[str] = None
    HttpMethod: Optional[ConnectionOAuthHttpMethodType] = None
    OAuthHttpParameters: Optional[ConnectionHttpParametersOutputTypeDef] = None

class CreateConnectionOAuthRequestParametersTypeDef(BaseValidatorModel):
    ClientParameters: CreateConnectionOAuthClientRequestParametersTypeDef
    AuthorizationEndpoint: str
    HttpMethod: ConnectionOAuthHttpMethodType
    OAuthHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class UpdateConnectionOAuthRequestParametersTypeDef(BaseValidatorModel):
    ClientParameters: Optional[UpdateConnectionOAuthClientRequestParametersTypeDef] = None
    AuthorizationEndpoint: Optional[str] = None
    HttpMethod: Optional[ConnectionOAuthHttpMethodType] = None
    OAuthHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class RoutingConfigTypeDef(BaseValidatorModel):
    FailoverConfig: FailoverConfigTypeDef

class PutEventsRequestRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[PutEventsRequestEntryTypeDef]
    EndpointId: Optional[str] = None

class PutPartnerEventsRequestRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[PutPartnerEventsRequestEntryTypeDef]

class TargetExtraOutputTypeDef(BaseValidatorModel):
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

class TargetOutputTypeDef(BaseValidatorModel):
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

class TargetTypeDef(BaseValidatorModel):
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

class ConnectionAuthResponseParametersTypeDef(BaseValidatorModel):
    BasicAuthParameters: Optional[ConnectionBasicAuthResponseParametersTypeDef] = None
    OAuthParameters: Optional[ConnectionOAuthResponseParametersTypeDef] = None
    ApiKeyAuthParameters: Optional[ConnectionApiKeyAuthResponseParametersTypeDef] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersOutputTypeDef] = None

class CreateConnectionAuthRequestParametersTypeDef(BaseValidatorModel):
    BasicAuthParameters: Optional[CreateConnectionBasicAuthRequestParametersTypeDef] = None
    OAuthParameters: Optional[CreateConnectionOAuthRequestParametersTypeDef] = None
    ApiKeyAuthParameters: Optional[CreateConnectionApiKeyAuthRequestParametersTypeDef] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class UpdateConnectionAuthRequestParametersTypeDef(BaseValidatorModel):
    BasicAuthParameters: Optional[UpdateConnectionBasicAuthRequestParametersTypeDef] = None
    OAuthParameters: Optional[UpdateConnectionOAuthRequestParametersTypeDef] = None
    ApiKeyAuthParameters: Optional[UpdateConnectionApiKeyAuthRequestParametersTypeDef] = None
    InvocationHttpParameters: Optional[ConnectionHttpParametersTypeDef] = None

class CreateEndpointRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RoutingConfig: RoutingConfigTypeDef
    EventBuses: Sequence[EndpointEventBusTypeDef]
    Description: Optional[str] = None
    ReplicationConfig: Optional[ReplicationConfigTypeDef] = None
    RoleArn: Optional[str] = None

class CreateEndpointResponseTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    RoutingConfig: RoutingConfigTypeDef
    ReplicationConfig: ReplicationConfigTypeDef
    EventBuses: List[EndpointEventBusTypeDef]
    RoleArn: str
    State: EndpointStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointResponseTypeDef(BaseValidatorModel):
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

class EndpointTypeDef(BaseValidatorModel):
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

class UpdateEndpointRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    RoutingConfig: Optional[RoutingConfigTypeDef] = None
    ReplicationConfig: Optional[ReplicationConfigTypeDef] = None
    EventBuses: Optional[Sequence[EndpointEventBusTypeDef]] = None
    RoleArn: Optional[str] = None

class UpdateEndpointResponseTypeDef(BaseValidatorModel):
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

class ListTargetsByRuleResponseTypeDef(BaseValidatorModel):
    Targets: List[TargetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConnectionResponseTypeDef(BaseValidatorModel):
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

class CreateConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    AuthorizationType: ConnectionAuthorizationTypeType
    AuthParameters: CreateConnectionAuthRequestParametersTypeDef
    Description: Optional[str] = None

class UpdateConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    AuthorizationType: Optional[ConnectionAuthorizationTypeType] = None
    AuthParameters: Optional[UpdateConnectionAuthRequestParametersTypeDef] = None

class ListEndpointsResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutTargetsRequestRequestTypeDef(BaseValidatorModel):
    Rule: str
    Targets: Sequence[TargetUnionTypeDef]
    EventBusName: Optional[str] = None

