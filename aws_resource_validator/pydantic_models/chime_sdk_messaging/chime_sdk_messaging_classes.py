from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.chime_sdk_messaging.chime_sdk_messaging_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AppInstanceUserMembershipSummary(BaseValidatorModel):
    Type: Optional[ChannelMembershipTypeType] = None
    ReadMarkerTimestamp: Optional[datetime] = None
    SubChannelId: Optional[str] = None


# This class is the input for the 'associate_channel_flow' function.
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


# This class is the input for the 'batch_create_channel_membership' function.
class BatchCreateChannelMembershipRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArns: List[str]
    ChimeBearer: str
    Type: Optional[ChannelMembershipTypeType] = None
    SubChannelId: Optional[str] = None


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


class PushNotificationConfiguration(BaseValidatorModel):
    Title: Optional[str] = None
    Body: Optional[str] = None
    Type: Optional[PushNotificationTypeType] = None


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


# This class is the input for the 'create_channel_ban' function.
class CreateChannelBanRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'create_channel_membership' function.
class CreateChannelMembershipRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    Type: ChannelMembershipTypeType
    ChimeBearer: str
    SubChannelId: Optional[str] = None


# This class is the input for the 'create_channel_moderator' function.
class CreateChannelModeratorRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


# This class is the input for the 'delete_channel_ban' function.
class DeleteChannelBanRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


# This class is the input for the 'delete_channel_flow' function.
class DeleteChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str


# This class is the input for the 'delete_channel_membership' function.
class DeleteChannelMembershipRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


# This class is the input for the 'delete_channel_message' function.
class DeleteChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


# This class is the input for the 'delete_channel_moderator' function.
class DeleteChannelModeratorRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


# This class is the input for the 'delete_channel' function.
class DeleteChannelRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


# This class is the input for the 'delete_messaging_streaming_configurations' function.
class DeleteMessagingStreamingConfigurationsRequest(BaseValidatorModel):
    AppInstanceArn: str


# This class is the input for the 'describe_channel_ban' function.
class DescribeChannelBanRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


# This class is the input for the 'describe_channel_flow' function.
class DescribeChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str


# This class is the input for the 'describe_channel_membership_for_app_instance_user' function.
class DescribeChannelMembershipForAppInstanceUserRequest(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str


# This class is the input for the 'describe_channel_membership' function.
class DescribeChannelMembershipRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


# This class is the input for the 'describe_channel_moderated_by_app_instance_user' function.
class DescribeChannelModeratedByAppInstanceUserRequest(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str


# This class is the input for the 'describe_channel_moderator' function.
class DescribeChannelModeratorRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


# This class is the input for the 'describe_channel' function.
class DescribeChannelRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


# This class is the input for the 'disassociate_channel_flow' function.
class DisassociateChannelFlowRequest(BaseValidatorModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str


# This class is the input for the 'get_channel_membership_preferences' function.
class GetChannelMembershipPreferencesRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


# This class is the input for the 'get_channel_message' function.
class GetChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


# This class is the input for the 'get_channel_message_status' function.
class GetChannelMessageStatusRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class MessagingSessionEndpoint(BaseValidatorModel):
    Url: Optional[str] = None


# This class is the input for the 'get_messaging_streaming_configurations' function.
class GetMessagingStreamingConfigurationsRequest(BaseValidatorModel):
    AppInstanceArn: str


class StreamingConfiguration(BaseValidatorModel):
    DataType: MessagingDataTypeType
    ResourceArn: str


class LambdaConfiguration(BaseValidatorModel):
    ResourceArn: str
    InvocationType: Literal['ASYNC']


# This class is the input for the 'list_channel_bans' function.
class ListChannelBansRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_channel_flows' function.
class ListChannelFlowsRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_channel_memberships_for_app_instance_user' function.
class ListChannelMembershipsForAppInstanceUserRequest(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_channel_memberships' function.
class ListChannelMembershipsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    Type: Optional[ChannelMembershipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_channel_moderators' function.
class ListChannelModeratorsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_channels_associated_with_channel_flow' function.
class ListChannelsAssociatedWithChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_channels_moderated_by_app_instance_user' function.
class ListChannelsModeratedByAppInstanceUserRequest(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_channels' function.
class ListChannelsRequest(BaseValidatorModel):
    AppInstanceArn: str
    ChimeBearer: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_sub_channels' function.
class ListSubChannelsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SubChannelSummary(BaseValidatorModel):
    SubChannelId: Optional[str] = None
    MembershipCount: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class MessageAttributeValue(BaseValidatorModel):
    StringValues: Optional[List[str]] = None


# This class is the input for the 'redact_channel_message' function.
class RedactChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class SearchField(BaseValidatorModel):
    Key: Literal['MEMBERS']
    Values: List[str]
    Operator: SearchFieldOperatorType


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_channel_message' function.
class UpdateChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Content: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None


# This class is the input for the 'update_channel_read_marker' function.
class UpdateChannelReadMarkerRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


# This class is the input for the 'update_channel' function.
class UpdateChannelRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    Name: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Metadata: Optional[str] = None


class BatchChannelMemberships(BaseValidatorModel):
    InvitedBy: Optional[Identity] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Members: Optional[List[Identity]] = None
    ChannelArn: Optional[str] = None
    SubChannelId: Optional[str] = None


class ChannelBanSummary(BaseValidatorModel):
    Member: Optional[Identity] = None


class ChannelBan(BaseValidatorModel):
    Member: Optional[Identity] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[Identity] = None


class ChannelMembershipSummary(BaseValidatorModel):
    Member: Optional[Identity] = None


class ChannelMembership(BaseValidatorModel):
    InvitedBy: Optional[Identity] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Member: Optional[Identity] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    SubChannelId: Optional[str] = None


class ChannelModeratorSummary(BaseValidatorModel):
    Moderator: Optional[Identity] = None


class ChannelModerator(BaseValidatorModel):
    Moderator: Optional[Identity] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[Identity] = None


# This class is the output for the 'channel_flow_callback' function.
class ChannelFlowCallbackResponse(BaseValidatorModel):
    ChannelArn: str
    CallbackId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel_ban' function.
class CreateChannelBanResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel_flow' function.
class CreateChannelFlowResponse(BaseValidatorModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel_membership' function.
class CreateChannelMembershipResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel_moderator' function.
class CreateChannelModeratorResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelModerator: Identity
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel' function.
class CreateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'redact_channel_message' function.
class RedactChannelMessageResponse(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_channel_flow' function.
class UpdateChannelFlowResponse(BaseValidatorModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_channel_read_marker' function.
class UpdateChannelReadMarkerResponse(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_channel' function.
class UpdateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channels_associated_with_channel_flow' function.
class ListChannelsAssociatedWithChannelFlowResponse(BaseValidatorModel):
    Channels: List[ChannelAssociatedWithFlowSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChannelMembershipForAppInstanceUserSummary(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummary] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummary] = None


class ChannelModeratedByAppInstanceUserSummary(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummary] = None


# This class is the output for the 'list_channels' function.
class ListChannelsResponse(BaseValidatorModel):
    Channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'search_channels' function.
class SearchChannelsResponse(BaseValidatorModel):
    Channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChannelMembershipPreferences(BaseValidatorModel):
    PushNotifications: Optional[PushNotificationPreferences] = None


# This class is the output for the 'get_channel_message_status' function.
class GetChannelMessageStatusResponse(BaseValidatorModel):
    Status: ChannelMessageStatusStructure
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_channel_message' function.
class SendChannelMessageResponse(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructure
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_channel_message' function.
class UpdateChannelMessageResponse(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructure
    SubChannelId: str
    ResponseMetadata: ResponseMetadata


class ChannelMessageSummary(BaseValidatorModel):
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    Sender: Optional[Identity] = None
    Redacted: Optional[bool] = None
    Status: Optional[ChannelMessageStatusStructure] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueOutput]] = None
    ContentType: Optional[str] = None
    Target: Optional[List[Target]] = None


class ChannelMessage(BaseValidatorModel):
    ChannelArn: Optional[str] = None
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Sender: Optional[Identity] = None
    Redacted: Optional[bool] = None
    Persistence: Optional[ChannelMessagePersistenceTypeType] = None
    Status: Optional[ChannelMessageStatusStructure] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueOutput]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None
    Target: Optional[List[Target]] = None


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


# This class is the input for the 'put_channel_expiration_settings' function.
class PutChannelExpirationSettingsRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


# This class is the output for the 'put_channel_expiration_settings' function.
class PutChannelExpirationSettingsResponse(BaseValidatorModel):
    ChannelArn: str
    ExpirationSettings: ExpirationSettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_channel' function.
class CreateChannelRequest(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    ClientRequestToken: str
    ChimeBearer: str
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ChannelId: Optional[str] = None
    MemberArns: Optional[List[str]] = None
    ModeratorArns: Optional[List[str]] = None
    ElasticChannelConfiguration: Optional[ElasticChannelConfiguration] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class GetMessagingSessionEndpointResponse(BaseValidatorModel):
    Endpoint: MessagingSessionEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_messaging_streaming_configurations' function.
class GetMessagingStreamingConfigurationsResponse(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfiguration]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_messaging_streaming_configurations' function.
class PutMessagingStreamingConfigurationsRequest(BaseValidatorModel):
    AppInstanceArn: str
    StreamingConfigurations: List[StreamingConfiguration]


# This class is the output for the 'put_messaging_streaming_configurations' function.
class PutMessagingStreamingConfigurationsResponse(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfiguration]
    ResponseMetadata: ResponseMetadata


class ProcessorConfiguration(BaseValidatorModel):
    Lambda: LambdaConfiguration


# This class is the input for the 'list_channel_messages' function.
class ListChannelMessagesRequest(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    SortOrder: Optional[SortOrderType] = None
    NotBefore: Optional[Timestamp] = None
    NotAfter: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None


# This class is the output for the 'list_sub_channels' function.
class ListSubChannelsResponse(BaseValidatorModel):
    ChannelArn: str
    SubChannels: List[SubChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MessageAttributeValueUnion = Union[MessageAttributeValue, MessageAttributeValueOutput]


# This class is the input for the 'search_channels' function.
class SearchChannelsRequest(BaseValidatorModel):
    Fields: List[SearchField]
    ChimeBearer: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'batch_create_channel_membership' function.
class BatchCreateChannelMembershipResponse(BaseValidatorModel):
    BatchChannelMemberships: BatchChannelMemberships
    Errors: List[BatchCreateChannelMembershipError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channel_bans' function.
class ListChannelBansResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelBans: List[ChannelBanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_channel_ban' function.
class DescribeChannelBanResponse(BaseValidatorModel):
    ChannelBan: ChannelBan
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channel_memberships' function.
class ListChannelMembershipsResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_channel_membership' function.
class DescribeChannelMembershipResponse(BaseValidatorModel):
    ChannelMembership: ChannelMembership
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channel_moderators' function.
class ListChannelModeratorsResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelModerators: List[ChannelModeratorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_channel_moderator' function.
class DescribeChannelModeratorResponse(BaseValidatorModel):
    ChannelModerator: ChannelModerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_channel_membership_for_app_instance_user' function.
class DescribeChannelMembershipForAppInstanceUserResponse(BaseValidatorModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channel_memberships_for_app_instance_user' function.
class ListChannelMembershipsForAppInstanceUserResponse(BaseValidatorModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_channel_moderated_by_app_instance_user' function.
class DescribeChannelModeratedByAppInstanceUserResponse(BaseValidatorModel):
    Channel: ChannelModeratedByAppInstanceUserSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channels_moderated_by_app_instance_user' function.
class ListChannelsModeratedByAppInstanceUserResponse(BaseValidatorModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_channel_membership_preferences' function.
class GetChannelMembershipPreferencesResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    Preferences: ChannelMembershipPreferences
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_channel_membership_preferences' function.
class PutChannelMembershipPreferencesRequest(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    Preferences: ChannelMembershipPreferences


# This class is the output for the 'put_channel_membership_preferences' function.
class PutChannelMembershipPreferencesResponse(BaseValidatorModel):
    ChannelArn: str
    Member: Identity
    Preferences: ChannelMembershipPreferences
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channel_messages' function.
class ListChannelMessagesResponse(BaseValidatorModel):
    ChannelArn: str
    ChannelMessages: List[ChannelMessageSummary]
    SubChannelId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_channel_message' function.
class GetChannelMessageResponse(BaseValidatorModel):
    ChannelMessage: ChannelMessage
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_channel' function.
class DescribeChannelResponse(BaseValidatorModel):
    Channel: Channel
    ResponseMetadata: ResponseMetadata


class Processor(BaseValidatorModel):
    Name: str
    Configuration: ProcessorConfiguration
    ExecutionOrder: int
    FallbackAction: FallbackActionType


class ChannelMessageCallback(BaseValidatorModel):
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfiguration] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueUnion]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None


# This class is the input for the 'send_channel_message' function.
class SendChannelMessageRequest(BaseValidatorModel):
    ChannelArn: str
    Content: str
    Type: ChannelMessageTypeType
    Persistence: ChannelMessagePersistenceTypeType
    ClientRequestToken: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfiguration] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueUnion]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None
    Target: Optional[List[Target]] = None


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


# This class is the input for the 'create_channel_flow' function.
class CreateChannelFlowRequest(BaseValidatorModel):
    AppInstanceArn: str
    Processors: List[Processor]
    Name: str
    ClientRequestToken: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_channel_flow' function.
class UpdateChannelFlowRequest(BaseValidatorModel):
    ChannelFlowArn: str
    Processors: List[Processor]
    Name: str


# This class is the input for the 'channel_flow_callback' function.
class ChannelFlowCallbackRequest(BaseValidatorModel):
    CallbackId: str
    ChannelArn: str
    ChannelMessage: ChannelMessageCallback
    DeleteResource: Optional[bool] = None


# This class is the output for the 'list_channel_flows' function.
class ListChannelFlowsResponse(BaseValidatorModel):
    ChannelFlows: List[ChannelFlowSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_channel_flow' function.
class DescribeChannelFlowResponse(BaseValidatorModel):
    ChannelFlow: ChannelFlow
    ResponseMetadata: ResponseMetadata