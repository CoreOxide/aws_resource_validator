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
from aws_resource_validator.pydantic_models.chime_sdk_messaging_constants import *

class AssociateChannelFlowRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str


class Identity(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class BatchCreateChannelMembershipError(BaseValidatorModel):
    MemberArn: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ChannelAssociatedWithFlowSummary(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None


class ChannelSummary(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    LastMessageTimestamp: Optional[datetime] = None


class PushNotificationPreferences(BaseValidatorModel):
    AllowNotifications: AllowNotificationsType
    FilterRule: Optional[str] = None


class ChannelMessageStatusStructure(BaseValidatorModel):
    Value: Optional[ChannelMessageStatusType] = None
    Detail: Optional[str] = None


class MessageAttributeValueOutput(BaseValidatorModel):
    StringValues: Optional[List[str]] = None


class Target(BaseValidatorModel):
    MemberArn: Optional[str] = None


class ElasticChannelConfiguration(BaseValidatorModel):
    MaximumSubChannels: int
    TargetMembershipsPerSubChannel: int
    MinimumMembershipPercentage: int


class ExpirationSettings(BaseValidatorModel):
    ExpirationDays: int
    ExpirationCriterion: ExpirationCriterionType


class CreateChannelBanRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateChannelModeratorRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


class DeleteChannelBanRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class DeleteChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str


class DeleteChannelMembershipRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class DeleteChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class DeleteChannelModeratorRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


class DeleteChannelRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


class DeleteMessagingStreamingConfigurationsRequest(BaseValidatorModel):
    AppInstanceArn: str


class DescribeChannelBanRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class DescribeChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str


class DescribeChannelMembershipForAppInstanceUserRequest(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str


class DescribeChannelMembershipRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class DescribeChannelModeratedByAppInstanceUserRequest(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str


class DescribeChannelModeratorRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


class DescribeChannelRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


class DisassociateChannelFlowRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str


class GetChannelMembershipPreferencesRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class GetChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class GetChannelMessageStatusRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class MessagingSessionEndpoint(BaseValidatorModel):
    Url: Optional[str] = None


class GetMessagingStreamingConfigurationsRequest(BaseValidatorModel):
    AppInstanceArn: str


class StreamingConfiguration(BaseValidatorModel):
    DataType: MessagingDataTypeType
    ResourceArn: str


class LambdaConfiguration(BaseValidatorModel):
    ResourceArn: str
    InvocationType: Literal["ASYNC"]


class ListChannelBansRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelFlowsRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelMembershipsForAppInstanceUserRequest(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelModeratorsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsAssociatedWithChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsModeratedByAppInstanceUserRequest(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequest(BaseValidatorModel):
    AppInstanceArn: str
    ChimeBearer: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSubChannelsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SubChannelSummary(BaseValidatorModel):
    SubChannelId: Optional[str] = None
    MembershipCount: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class MessageAttributeValue(BaseValidatorModel):
    StringValues: Optional[Sequence[str]] = None


class RedactChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class SearchField(BaseValidatorModel):
    Key: Literal["MEMBERS"]
    Values: Sequence[str]
    Operator: SearchFieldOperatorType


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Content: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None


class UpdateChannelReadMarkerRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


class UpdateChannelRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    Name: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Metadata: Optional[str] = None


class ChannelBanSummary(BaseValidatorModel):
    Member: Optional[Identity] = None


class ChannelBan(BaseValidatorModel):
    Member: Optional[Identity] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[Identity] = None


class ChannelMembershipSummary(BaseValidatorModel):
    Member: Optional[Identity] = None


class ChannelModeratorSummary(BaseValidatorModel):
    Moderator: Optional[Identity] = None


class ChannelModerator(BaseValidatorModel):
    Moderator: Optional[Identity] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[Identity] = None


class ChannelFlowCallbackResponse(BaseValidatorModel):
    ChannelArn: str
    CallbackId: str
    ResponseMetadata: ResponseMetadata


class CreateChannelBanResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    ResponseMetadata: ResponseMetadata


class CreateChannelFlowResponse(BaseValidatorModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadata


class CreateChannelMembershipResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


class CreateChannelModeratorResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelModerator: Identity
    ResponseMetadata: ResponseMetadata


class CreateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class RedactChannelMessageResponse(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


class UpdateChannelFlowResponse(BaseValidatorModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadata


class UpdateChannelReadMarkerResponse(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadata


class UpdateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadata


class ListChannelsAssociatedWithChannelFlowResponse(BaseValidatorModel):
    Channels: List[ChannelAssociatedWithFlowSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AppInstanceUserMembershipSummary(BaseValidatorModel):
    pass


class ChannelMembershipForAppInstanceUserSummary(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummary] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummary] = None


class ChannelModeratedByAppInstanceUserSummary(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummary] = None


class ListChannelsResponse(BaseValidatorModel):
    Channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchChannelsResponse(BaseValidatorModel):
    Channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChannelMembershipPreferences(BaseValidatorModel):
    PushNotifications: Optional[PushNotificationPreferences] = None


class GetChannelMessageStatusResponse(BaseValidatorModel):
    Status: ChannelMessageStatusStructure
    ResponseMetadata: ResponseMetadata


class SendChannelMessageResponse(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructure
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


class UpdateChannelMessageResponse(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructure
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


class Channel(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    CreatedBy: Optional[Identity] = None
    CreatedTimestamp: Optional[datetime] = None
    LastMessageTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    ChannelFlowArn: Optional[str] = None
    ElasticChannelConfiguration: Optional[ElasticChannelConfiguration] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


class PutChannelExpirationSettingsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


class PutChannelExpirationSettingsResponse(BaseValidatorModel):
    ChannelArn: str
    ExpirationSettings: ExpirationSettings
    ResponseMetadata: ResponseMetadata


class CreateChannelRequest(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    ClientRequestToken: str
    ChimeBearer: str
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    ChannelId: Optional[str] = None
    MemberArns: Optional[Sequence[str]] = None
    ModeratorArns: Optional[Sequence[str]] = None
    ElasticChannelConfiguration: Optional[ElasticChannelConfiguration] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class GetMessagingSessionEndpointResponse(BaseValidatorModel):
    Endpoint: MessagingSessionEndpoint
    ResponseMetadata: ResponseMetadata


class GetMessagingStreamingConfigurationsResponse(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfiguration]
    ResponseMetadata: ResponseMetadata


class PutMessagingStreamingConfigurationsRequest(BaseValidatorModel):
    AppInstanceArn: str
    StreamingConfigurations: Sequence[StreamingConfiguration]


class PutMessagingStreamingConfigurationsResponse(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfiguration]
    ResponseMetadata: ResponseMetadata


class ProcessorConfiguration(BaseValidatorModel):
    Lambda: LambdaConfiguration


class Timestamp(BaseValidatorModel):
    pass


class ListChannelMessagesRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    SortOrder: Optional[SortOrderType] = None
    NotBefore: Optional[Timestamp] = None
    NotAfter: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None


class ListSubChannelsResponse(BaseValidatorModel):
    ChannelArn: str
    SubChannels: List[SubChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchChannelsRequest(BaseValidatorModel):
    Fields: Sequence[SearchField]
    ChimeBearer: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class BatchChannelMemberships(BaseValidatorModel):
    pass


class BatchCreateChannelMembershipResponse(BaseValidatorModel):
    BatchChannelMemberships: BatchChannelMemberships
    Errors: List[BatchCreateChannelMembershipError]
    ResponseMetadata: ResponseMetadata


class ListChannelBansResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelBans: List[ChannelBanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeChannelBanResponse(BaseValidatorModel):
    ChannelBan: ChannelBan
    ResponseMetadata: ResponseMetadata


class ListChannelMembershipsResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChannelMembership(BaseValidatorModel):
    pass


class DescribeChannelMembershipResponse(BaseValidatorModel):
    ChannelMembership: ChannelMembership
    ResponseMetadata: ResponseMetadata


class ListChannelModeratorsResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelModerators: List[ChannelModeratorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeChannelModeratorResponse(BaseValidatorModel):
    ChannelModerator: ChannelModerator
    ResponseMetadata: ResponseMetadata


class DescribeChannelMembershipForAppInstanceUserResponse(BaseValidatorModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummary
    ResponseMetadata: ResponseMetadata


class ListChannelMembershipsForAppInstanceUserResponse(BaseValidatorModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeChannelModeratedByAppInstanceUserResponse(BaseValidatorModel):
    Channel: ChannelModeratedByAppInstanceUserSummary
    ResponseMetadata: ResponseMetadata


class ListChannelsModeratedByAppInstanceUserResponse(BaseValidatorModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetChannelMembershipPreferencesResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    Preferences: ChannelMembershipPreferences
    ResponseMetadata: ResponseMetadata


class PutChannelMembershipPreferencesRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    Preferences: ChannelMembershipPreferences


class PutChannelMembershipPreferencesResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    Preferences: ChannelMembershipPreferences
    ResponseMetadata: ResponseMetadata


class ChannelMessageSummary(BaseValidatorModel):
    pass


class ListChannelMessagesResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelMessages: List[ChannelMessageSummary]
    SubChannelId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChannelMessage(BaseValidatorModel):
    pass


class GetChannelMessageResponse(BaseValidatorModel):
    ChannelMessage: ChannelMessage
    ResponseMetadata: ResponseMetadata


class DescribeChannelResponse(BaseValidatorModel):
    Channel: Channel
    ResponseMetadata: ResponseMetadata


class Processor(BaseValidatorModel):
    Name: str
    Configuration: ProcessorConfiguration
    ExecutionOrder: int
    FallbackAction: FallbackActionType


class MessageAttributeValueUnion(BaseValidatorModel):
    pass


class PushNotificationConfiguration(BaseValidatorModel):
    pass


class ChannelMessageCallback(BaseValidatorModel):
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfiguration] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnion]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None


class ChannelFlowSummary(BaseValidatorModel):
    ChannelFlowArn: Optional[str] = None
    Name: Optional[str] = None
    Processors: Optional[List[Processor]] = None


class ChannelFlow(BaseValidatorModel):
    ChannelFlowArn: Optional[str] = None
    Processors: Optional[List[Processor]] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class CreateChannelFlowRequest(BaseValidatorModel):
    AppInstanceArn: str
    Processors: Sequence[Processor]
    Name: str
    ClientRequestToken: str
    Tags: Optional[Sequence[Tag]] = None


class UpdateChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str
    Processors: Sequence[Processor]
    Name: str


class ChannelFlowCallbackRequest(BaseValidatorModel):
    CallbackId: str
    ChannelArn: str
    ChannelMessage: ChannelMessageCallback
    DeleteResource: Optional[bool] = None


class ListChannelFlowsResponse(BaseValidatorModel):
    ChannelFlows: List[ChannelFlowSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeChannelFlowResponse(BaseValidatorModel):
    ChannelFlow: ChannelFlow
    ResponseMetadata: ResponseMetadata


