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
from aws_resource_validator.pydantic_models.chime_sdk_messaging_constants import *

class AppInstanceUserMembershipSummaryTypeDef(BaseModel):
    Type: Optional[ChannelMembershipTypeType] = None
    ReadMarkerTimestamp: Optional[datetime] = None
    SubChannelId: Optional[str] = None

class AssociateChannelFlowRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str

class IdentityTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class BatchCreateChannelMembershipErrorTypeDef(BaseModel):
    MemberArn: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchCreateChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArns: Sequence[str]
    ChimeBearer: str
    Type: Optional[ChannelMembershipTypeType] = None
    SubChannelId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ChannelAssociatedWithFlowSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None

class ChannelSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    LastMessageTimestamp: Optional[datetime] = None

class PushNotificationPreferencesTypeDef(BaseModel):
    AllowNotifications: AllowNotificationsType
    FilterRule: Optional[str] = None

class MessageAttributeValueTypeDef(BaseModel):
    StringValues: Optional[Sequence[str]] = None

class PushNotificationConfigurationTypeDef(BaseModel):
    Title: Optional[str] = None
    Body: Optional[str] = None
    Type: Optional[PushNotificationTypeType] = None

class ChannelMessageStatusStructureTypeDef(BaseModel):
    Value: Optional[ChannelMessageStatusType] = None
    Detail: Optional[str] = None

class TargetTypeDef(BaseModel):
    MemberArn: Optional[str] = None

class ElasticChannelConfigurationTypeDef(BaseModel):
    MaximumSubChannels: int
    TargetMembershipsPerSubChannel: int
    MinimumMembershipPercentage: int

class ExpirationSettingsTypeDef(BaseModel):
    ExpirationDays: int
    ExpirationCriterion: ExpirationCriterionType

class CreateChannelBanRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    Type: ChannelMembershipTypeType
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class CreateChannelModeratorRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DeleteChannelBanRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class DeleteChannelFlowRequestRequestTypeDef(BaseModel):
    ChannelFlowArn: str

class DeleteChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class DeleteChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class DeleteChannelModeratorRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DeleteChannelRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str

class DeleteMessagingStreamingConfigurationsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class DescribeChannelBanRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class DescribeChannelFlowRequestRequestTypeDef(BaseModel):
    ChannelFlowArn: str

class DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str

class DescribeChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str

class DescribeChannelModeratorRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DescribeChannelRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str

class DisassociateChannelFlowRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str

class GetChannelMembershipPreferencesRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class GetChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class GetChannelMessageStatusRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class MessagingSessionEndpointTypeDef(BaseModel):
    Url: Optional[str] = None

class GetMessagingStreamingConfigurationsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class StreamingConfigurationTypeDef(BaseModel):
    DataType: MessagingDataTypeType
    ResourceArn: str

class LambdaConfigurationTypeDef(BaseModel):
    ResourceArn: str
    InvocationType: Literal["ASYNC"]

class ListChannelBansRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelFlowsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef(BaseModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelMembershipsRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str
    Type: Optional[ChannelMembershipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None

class ListChannelModeratorsRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef(BaseModel):
    ChannelFlowArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef(BaseModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    ChimeBearer: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSubChannelsRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SubChannelSummaryTypeDef(BaseModel):
    SubChannelId: Optional[str] = None
    MembershipCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class RedactChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class SearchFieldTypeDef(BaseModel):
    Key: Literal["MEMBERS"]
    Values: Sequence[str]
    Operator: SearchFieldOperatorType

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    Content: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None

class UpdateChannelReadMarkerRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str

class UpdateChannelRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str
    Name: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Metadata: Optional[str] = None

class BatchChannelMembershipsTypeDef(BaseModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Members: Optional[List[IdentityTypeDef]] = None
    ChannelArn: Optional[str] = None
    SubChannelId: Optional[str] = None

class ChannelBanSummaryTypeDef(BaseModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelBanTypeDef(BaseModel):
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelMembershipSummaryTypeDef(BaseModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelMembershipTypeDef(BaseModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    SubChannelId: Optional[str] = None

class ChannelModeratorSummaryTypeDef(BaseModel):
    Moderator: Optional[IdentityTypeDef] = None

class ChannelModeratorTypeDef(BaseModel):
    Moderator: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelFlowCallbackResponseTypeDef(BaseModel):
    ChannelArn: str
    CallbackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelBanResponseTypeDef(BaseModel):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelFlowResponseTypeDef(BaseModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelMembershipResponseTypeDef(BaseModel):
    ChannelArn: str
    Member: IdentityTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelModeratorResponseTypeDef(BaseModel):
    ChannelArn: str
    ChannelModerator: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class RedactChannelMessageResponseTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelFlowResponseTypeDef(BaseModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelReadMarkerResponseTypeDef(BaseModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsAssociatedWithChannelFlowResponseTypeDef(BaseModel):
    Channels: List[ChannelAssociatedWithFlowSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMembershipForAppInstanceUserSummaryTypeDef(BaseModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummaryTypeDef] = None

class ChannelModeratedByAppInstanceUserSummaryTypeDef(BaseModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None

class ListChannelsResponseTypeDef(BaseModel):
    Channels: List[ChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchChannelsResponseTypeDef(BaseModel):
    Channels: List[ChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMembershipPreferencesTypeDef(BaseModel):
    PushNotifications: Optional[PushNotificationPreferencesTypeDef] = None

class ChannelMessageCallbackTypeDef(BaseModel):
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfigurationTypeDef] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None

class GetChannelMessageStatusResponseTypeDef(BaseModel):
    Status: ChannelMessageStatusStructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendChannelMessageResponseTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructureTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelMessageResponseTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructureTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMessageSummaryTypeDef(BaseModel):
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    Sender: Optional[IdentityTypeDef] = None
    Redacted: Optional[bool] = None
    Status: Optional[ChannelMessageStatusStructureTypeDef] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueTypeDef]] = None
    ContentType: Optional[str] = None
    Target: Optional[List[TargetTypeDef]] = None

class ChannelMessageTypeDef(BaseModel):
    ChannelArn: Optional[str] = None
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Sender: Optional[IdentityTypeDef] = None
    Redacted: Optional[bool] = None
    Persistence: Optional[ChannelMessagePersistenceTypeType] = None
    Status: Optional[ChannelMessageStatusStructureTypeDef] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueTypeDef]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None
    Target: Optional[List[TargetTypeDef]] = None

class SendChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    Content: str
    Type: ChannelMessageTypeType
    Persistence: ChannelMessagePersistenceTypeType
    ClientRequestToken: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfigurationTypeDef] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None
    Target: Optional[Sequence[TargetTypeDef]] = None

class ChannelTypeDef(BaseModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    CreatedBy: Optional[IdentityTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    LastMessageTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    ChannelFlowArn: Optional[str] = None
    ElasticChannelConfiguration: Optional[ElasticChannelConfigurationTypeDef] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class PutChannelExpirationSettingsRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class PutChannelExpirationSettingsResponseTypeDef(BaseModel):
    ChannelArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    Name: str
    ClientRequestToken: str
    ChimeBearer: str
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ChannelId: Optional[str] = None
    MemberArns: Optional[Sequence[str]] = None
    ModeratorArns: Optional[Sequence[str]] = None
    ElasticChannelConfiguration: Optional[ElasticChannelConfigurationTypeDef] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class GetMessagingSessionEndpointResponseTypeDef(BaseModel):
    Endpoint: MessagingSessionEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMessagingStreamingConfigurationsResponseTypeDef(BaseModel):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutMessagingStreamingConfigurationsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    StreamingConfigurations: Sequence[StreamingConfigurationTypeDef]

class PutMessagingStreamingConfigurationsResponseTypeDef(BaseModel):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorConfigurationTypeDef(BaseModel):
    Lambda: LambdaConfigurationTypeDef

class ListChannelMessagesRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: str
    SortOrder: Optional[SortOrderType] = None
    NotBefore: Optional[TimestampTypeDef] = None
    NotAfter: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None

class ListSubChannelsResponseTypeDef(BaseModel):
    ChannelArn: str
    SubChannels: List[SubChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchChannelsRequestRequestTypeDef(BaseModel):
    Fields: Sequence[SearchFieldTypeDef]
    ChimeBearer: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class BatchCreateChannelMembershipResponseTypeDef(BaseModel):
    BatchChannelMemberships: BatchChannelMembershipsTypeDef
    Errors: List[BatchCreateChannelMembershipErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelBansResponseTypeDef(BaseModel):
    ChannelArn: str
    NextToken: str
    ChannelBans: List[ChannelBanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelBanResponseTypeDef(BaseModel):
    ChannelBan: ChannelBanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsResponseTypeDef(BaseModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipResponseTypeDef(BaseModel):
    ChannelMembership: ChannelMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelModeratorsResponseTypeDef(BaseModel):
    ChannelArn: str
    NextToken: str
    ChannelModerators: List[ChannelModeratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratorResponseTypeDef(BaseModel):
    ChannelModerator: ChannelModeratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(BaseModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsForAppInstanceUserResponseTypeDef(BaseModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(BaseModel):
    Channel: ChannelModeratedByAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsModeratedByAppInstanceUserResponseTypeDef(BaseModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelMembershipPreferencesResponseTypeDef(BaseModel):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutChannelMembershipPreferencesRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    Preferences: ChannelMembershipPreferencesTypeDef

class PutChannelMembershipPreferencesResponseTypeDef(BaseModel):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelFlowCallbackRequestRequestTypeDef(BaseModel):
    CallbackId: str
    ChannelArn: str
    ChannelMessage: ChannelMessageCallbackTypeDef
    DeleteResource: Optional[bool] = None

class ListChannelMessagesResponseTypeDef(BaseModel):
    ChannelArn: str
    NextToken: str
    ChannelMessages: List[ChannelMessageSummaryTypeDef]
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelMessageResponseTypeDef(BaseModel):
    ChannelMessage: ChannelMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorTypeDef(BaseModel):
    Name: str
    Configuration: ProcessorConfigurationTypeDef
    ExecutionOrder: int
    FallbackAction: FallbackActionType

class ChannelFlowSummaryTypeDef(BaseModel):
    ChannelFlowArn: Optional[str] = None
    Name: Optional[str] = None
    Processors: Optional[List[ProcessorTypeDef]] = None

class ChannelFlowTypeDef(BaseModel):
    ChannelFlowArn: Optional[str] = None
    Processors: Optional[List[ProcessorTypeDef]] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class CreateChannelFlowRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str
    ClientRequestToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateChannelFlowRequestRequestTypeDef(BaseModel):
    ChannelFlowArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str

class ListChannelFlowsResponseTypeDef(BaseModel):
    ChannelFlows: List[ChannelFlowSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelFlowResponseTypeDef(BaseModel):
    ChannelFlow: ChannelFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

