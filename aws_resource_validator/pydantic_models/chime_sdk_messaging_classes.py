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

class AssociateChannelFlowRequestTypeDef(BaseValidatorModel):
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


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class ChannelMessageStatusStructureTypeDef(BaseValidatorModel):
    Value: Optional[ChannelMessageStatusType] = None
    Detail: Optional[str] = None


class MessageAttributeValueOutputTypeDef(BaseValidatorModel):
    StringValues: Optional[List[str]] = None


class TargetTypeDef(BaseValidatorModel):
    MemberArn: Optional[str] = None


class ElasticChannelConfigurationTypeDef(BaseValidatorModel):
    MaximumSubChannels: int
    TargetMembershipsPerSubChannel: int
    MinimumMembershipPercentage: int


class ExpirationSettingsTypeDef(BaseValidatorModel):
    ExpirationDays: int
    ExpirationCriterion: ExpirationCriterionType


class CreateChannelBanRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateChannelModeratorRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


class DeleteChannelBanRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class DeleteChannelFlowRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str


class DeleteChannelMembershipRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class DeleteChannelMessageRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class DeleteChannelModeratorRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


class DeleteChannelRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


class DeleteMessagingStreamingConfigurationsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str


class DescribeChannelBanRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class DescribeChannelFlowRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str


class DescribeChannelMembershipForAppInstanceUserRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str


class DescribeChannelMembershipRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class DescribeChannelModeratedByAppInstanceUserRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str


class DescribeChannelModeratorRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str


class DescribeChannelRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


class DisassociateChannelFlowRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str


class GetChannelMembershipPreferencesRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str


class GetChannelMessageRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class GetChannelMessageStatusRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class MessagingSessionEndpointTypeDef(BaseValidatorModel):
    Url: Optional[str] = None


class GetMessagingStreamingConfigurationsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str


class StreamingConfigurationTypeDef(BaseValidatorModel):
    DataType: MessagingDataTypeType
    ResourceArn: str


class LambdaConfigurationTypeDef(BaseValidatorModel):
    ResourceArn: str
    InvocationType: Literal["ASYNC"]


class ListChannelBansRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelFlowsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelMembershipsForAppInstanceUserRequestTypeDef(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelModeratorsRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsAssociatedWithChannelFlowRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsModeratedByAppInstanceUserRequestTypeDef(BaseValidatorModel):
    ChimeBearer: str
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ChimeBearer: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSubChannelsRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SubChannelSummaryTypeDef(BaseValidatorModel):
    SubChannelId: Optional[str] = None
    MembershipCount: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class MessageAttributeValueTypeDef(BaseValidatorModel):
    StringValues: Optional[Sequence[str]] = None


class RedactChannelMessageRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: Optional[str] = None


class SearchFieldTypeDef(BaseValidatorModel):
    Key: Literal["MEMBERS"]
    Values: Sequence[str]
    Operator: SearchFieldOperatorType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateChannelMessageRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Content: str
    ChimeBearer: str
    Metadata: Optional[str] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None


class UpdateChannelReadMarkerRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str


class UpdateChannelRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: str
    Name: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Metadata: Optional[str] = None


class ChannelBanSummaryTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None


class ChannelBanTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None


class ChannelMembershipSummaryTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AppInstanceUserMembershipSummaryTypeDef(BaseValidatorModel):
    pass


class ChannelMembershipForAppInstanceUserSummaryTypeDef(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummaryTypeDef] = None


class ChannelModeratedByAppInstanceUserSummaryTypeDef(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None


class ListChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ChannelMembershipPreferencesTypeDef(BaseValidatorModel):
    PushNotifications: Optional[PushNotificationPreferencesTypeDef] = None


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


class PutChannelExpirationSettingsRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None


class PutChannelExpirationSettingsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateChannelRequestTypeDef(BaseValidatorModel):
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


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class GetMessagingSessionEndpointResponseTypeDef(BaseValidatorModel):
    Endpoint: MessagingSessionEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMessagingStreamingConfigurationsResponseTypeDef(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutMessagingStreamingConfigurationsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    StreamingConfigurations: Sequence[StreamingConfigurationTypeDef]


class PutMessagingStreamingConfigurationsResponseTypeDef(BaseValidatorModel):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProcessorConfigurationTypeDef(BaseValidatorModel):
    Lambda: LambdaConfigurationTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListChannelMessagesRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchChannelsRequestTypeDef(BaseValidatorModel):
    Fields: Sequence[SearchFieldTypeDef]
    ChimeBearer: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class BatchChannelMembershipsTypeDef(BaseValidatorModel):
    pass


class BatchCreateChannelMembershipResponseTypeDef(BaseValidatorModel):
    BatchChannelMemberships: BatchChannelMembershipsTypeDef
    Errors: List[BatchCreateChannelMembershipErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelBansResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelBans: List[ChannelBanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeChannelBanResponseTypeDef(BaseValidatorModel):
    ChannelBan: ChannelBanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelMembershipsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ChannelMembershipTypeDef(BaseValidatorModel):
    pass


class DescribeChannelMembershipResponseTypeDef(BaseValidatorModel):
    ChannelMembership: ChannelMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelModeratorsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModerators: List[ChannelModeratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeChannelModeratorResponseTypeDef(BaseValidatorModel):
    ChannelModerator: ChannelModeratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(BaseValidatorModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelMembershipsForAppInstanceUserResponseTypeDef(BaseValidatorModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(BaseValidatorModel):
    Channel: ChannelModeratedByAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelsModeratedByAppInstanceUserResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetChannelMembershipPreferencesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutChannelMembershipPreferencesRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    Preferences: ChannelMembershipPreferencesTypeDef


class PutChannelMembershipPreferencesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChannelMessageSummaryTypeDef(BaseValidatorModel):
    pass


class ListChannelMessagesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelMessages: List[ChannelMessageSummaryTypeDef]
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ChannelMessageTypeDef(BaseValidatorModel):
    pass


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


class MessageAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class PushNotificationConfigurationTypeDef(BaseValidatorModel):
    pass


class ChannelMessageCallbackTypeDef(BaseValidatorModel):
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    PushNotification: Optional[PushNotificationConfigurationTypeDef] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnionTypeDef]] = None
    SubChannelId: Optional[str] = None
    ContentType: Optional[str] = None


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


class CreateChannelFlowRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str
    ClientRequestToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateChannelFlowRequestTypeDef(BaseValidatorModel):
    ChannelFlowArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str


class ChannelFlowCallbackRequestTypeDef(BaseValidatorModel):
    CallbackId: str
    ChannelArn: str
    ChannelMessage: ChannelMessageCallbackTypeDef
    DeleteResource: Optional[bool] = None


class ListChannelFlowsResponseTypeDef(BaseValidatorModel):
    ChannelFlows: List[ChannelFlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeChannelFlowResponseTypeDef(BaseValidatorModel):
    ChannelFlow: ChannelFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


