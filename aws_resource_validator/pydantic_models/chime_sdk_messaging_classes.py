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
from aws_resource_validator.pydantic_models.chime_sdk_messaging_constants import *

class AppInstanceUserMembershipSummaryTypeDef(BaseValidatorModel):
    Type: Optional[ChannelMembershipTypeType] = None
    ReadMarkerTimestamp: Optional[datetime] = None
    SubChannelId: Optional[str] = None

class AssociateChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str

class IdentityTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class BatchCreateChannelMembershipErrorTypeDef(BaseValidatorModel):
    MemberArn: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchCreateChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArns: Sequence[str]
    ChimeBearer: str
    Type: Optional[ChannelMembershipTypeType] = None
    SubChannelId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ChannelAssociatedWithFlowSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None

class ChannelSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    LastMessageTimestamp: Optional[datetime] = None

class PushNotificationPreferencesTypeDef(BaseValidatorModel):
    AllowNotifications: AllowNotificationsType
    FilterRule: Optional[str] = None

class MessageAttributeValueTypeDef(BaseValidatorModel):
    StringValues: Optional[Sequence[str]] = None

class PushNotificationConfigurationTypeDef(BaseValidatorModel):
    Title: Optional[str] = None
    Body: Optional[str] = None
    Type: Optional[PushNotificationTypeType] = None

class ChannelMessageStatusStructureTypeDef(BaseValidatorModel):
    Value: Optional[ChannelMessageStatusType] = None
    Detail: Optional[str] = None

class TargetTypeDef(BaseValidatorModel):
    MemberArn: Optional[str] = None

class ElasticChannelConfigurationTypeDef(BaseValidatorModel):
    MaximumSubChannels: int
    TargetMembershipsPerSubChannel: int
    MinimumMembershipPercentage: int

class ExpirationSettingsTypeDef(BaseValidatorModel):
    ExpirationDays: int
    ExpirationCriterion: ExpirationCriterionType

class CreateChannelBanRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    Type: ChannelMembershipTypeType
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class CreateChannelModeratorRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DeleteChannelBanRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class DeleteChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str

class DeleteChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class DeleteChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class DeleteChannelModeratorRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str

class DeleteMessagingStreamingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class DescribeChannelBanRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class DescribeChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str

class DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str

class DescribeChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str

class DescribeChannelModeratorRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DescribeChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str

class DisassociateChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str

class GetChannelMembershipPreferencesRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class GetChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class GetChannelMessageStatusRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class MessagingSessionEndpointTypeDef(BaseValidatorModel):
    Url: Optional[str] = None

class GetMessagingStreamingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class StreamingConfigurationTypeDef(BaseValidatorModel):
    DataType: MessagingDataTypeType
    ResourceArn: str

class LambdaConfigurationTypeDef(BaseValidatorModel):
    ResourceArn: str
    InvocationType: Literal["ASYNC"]

class ListChannelBansRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelFlowsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelMembershipsRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    Type: Optional[ChannelMembershipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None

class ListChannelModeratorsRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ChimeBearer: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSubChannelsRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SubChannelSummaryTypeDef(BaseValidatorModel):
    SubChannelId: Optional[str] = None
    MembershipCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class RedactChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None

class SearchFieldTypeDef(BaseValidatorModel):
    Key: Literal["MEMBERS"]
    Values: Sequence[str]
    Operator: SearchFieldOperatorType

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Content: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None

class UpdateChannelReadMarkerRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    Name: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Metadata: Optional[str] = None

class BatchChannelMembershipsTypeDef(BaseValidatorModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Members: Optional[List[IdentityTypeDef]] = None
    ChannelArn: Optional[str] = None
    SubChannelId: Optional[str] = None

class ChannelBanSummaryTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelBanTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelMembershipSummaryTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelMembershipTypeDef(BaseValidatorModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    SubChannelId: Optional[str] = None

class ChannelModeratorSummaryTypeDef(BaseValidatorModel):
    Moderator: Optional[IdentityTypeDef] = None

class ChannelModeratorTypeDef(BaseValidatorModel):
    Moderator: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelFlowCallbackResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    CallbackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelBanResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelFlowResponseTypeDef(BaseValidatorModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelMembershipResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelModeratorResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModerator: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class RedactChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelFlowResponseTypeDef(BaseValidatorModel):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelReadMarkerResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsAssociatedWithChannelFlowResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelAssociatedWithFlowSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMembershipForAppInstanceUserSummaryTypeDef(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummaryTypeDef] = None

class ChannelModeratedByAppInstanceUserSummaryTypeDef(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMembershipPreferencesTypeDef(BaseValidatorModel):
    PushNotifications: Optional[PushNotificationPreferencesTypeDef] = None

class ChannelMessageCallbackTypeDef(BaseValidatorModel):
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfigurationTypeDef] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None

class GetChannelMessageStatusResponseTypeDef(BaseValidatorModel):
    Status: ChannelMessageStatusStructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructureTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructureTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMessageSummaryTypeDef(BaseValidatorModel):
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

class ChannelMessageTypeDef(BaseValidatorModel):
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

class SendChannelMessageRequestRequestTypeDef(BaseValidatorModel):
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

class ChannelTypeDef(BaseValidatorModel):
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

class PutChannelExpirationSettingsRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class PutChannelExpirationSettingsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class GetMessagingSessionEndpointResponseTypeDef(BaseValidatorModel):
    Endpoint: MessagingSessionEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMessagingStreamingConfigurationsResponseTypeDef(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutMessagingStreamingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    StreamingConfigurations: Sequence[StreamingConfigurationTypeDef]

class PutMessagingStreamingConfigurationsResponseTypeDef(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorConfigurationTypeDef(BaseValidatorModel):
    Lambda: LambdaConfigurationTypeDef

class ListChannelMessagesRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    SortOrder: Optional[SortOrderType] = None
    NotBefore: Optional[TimestampTypeDef] = None
    NotAfter: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubChannelId: Optional[str] = None

class ListSubChannelsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    SubChannels: List[SubChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchChannelsRequestRequestTypeDef(BaseValidatorModel):
    Fields: Sequence[SearchFieldTypeDef]
    ChimeBearer: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class BatchCreateChannelMembershipResponseTypeDef(BaseValidatorModel):
    BatchChannelMemberships: BatchChannelMembershipsTypeDef
    Errors: List[BatchCreateChannelMembershipErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelBansResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    NextToken: str
    ChannelBans: List[ChannelBanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelBanResponseTypeDef(BaseValidatorModel):
    ChannelBan: ChannelBanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipResponseTypeDef(BaseValidatorModel):
    ChannelMembership: ChannelMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelModeratorsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    NextToken: str
    ChannelModerators: List[ChannelModeratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratorResponseTypeDef(BaseValidatorModel):
    ChannelModerator: ChannelModeratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(BaseValidatorModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsForAppInstanceUserResponseTypeDef(BaseValidatorModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(BaseValidatorModel):
    Channel: ChannelModeratedByAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsModeratedByAppInstanceUserResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelMembershipPreferencesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutChannelMembershipPreferencesRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    Preferences: ChannelMembershipPreferencesTypeDef

class PutChannelMembershipPreferencesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelFlowCallbackRequestRequestTypeDef(BaseValidatorModel):
    CallbackId: str
    ChannelArn: str
    ChannelMessage: ChannelMessageCallbackTypeDef
    DeleteResource: Optional[bool] = None

class ListChannelMessagesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    NextToken: str
    ChannelMessages: List[ChannelMessageSummaryTypeDef]
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelMessage: ChannelMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseValidatorModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorTypeDef(BaseValidatorModel):
    Name: str
    Configuration: ProcessorConfigurationTypeDef
    ExecutionOrder: int
    FallbackAction: FallbackActionType

class ChannelFlowSummaryTypeDef(BaseValidatorModel):
    ChannelFlowArn: Optional[str] = None
    Name: Optional[str] = None
    Processors: Optional[List[ProcessorTypeDef]] = None

class ChannelFlowTypeDef(BaseValidatorModel):
    ChannelFlowArn: Optional[str] = None
    Processors: Optional[List[ProcessorTypeDef]] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class CreateChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str
    ClientRequestToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateChannelFlowRequestRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str

class ListChannelFlowsResponseTypeDef(BaseValidatorModel):
    ChannelFlows: List[ChannelFlowSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelFlowResponseTypeDef(BaseValidatorModel):
    ChannelFlow: ChannelFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

