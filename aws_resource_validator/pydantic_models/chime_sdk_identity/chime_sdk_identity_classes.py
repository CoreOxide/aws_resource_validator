from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Identity(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class AppInstanceBotSummary(BaseValidatorModel):
    AppInstanceBotArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None


class ChannelRetentionSettings(BaseValidatorModel):
    RetentionDays: Optional[int] = None


class AppInstanceSummary(BaseValidatorModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None


class AppInstance(BaseValidatorModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None


class EndpointState(BaseValidatorModel):
    Status: EndpointStatusType
    StatusReason: Optional[EndpointStatusReasonType] = None


class EndpointAttributes(BaseValidatorModel):
    DeviceToken: str
    VoipDeviceToken: Optional[str] = None


class AppInstanceUserSummary(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None


class ExpirationSettings(BaseValidatorModel):
    ExpirationDays: int
    ExpirationCriterion: Literal['CREATED_TIMESTAMP']


class CreateAppInstanceAdminRequest(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteAppInstanceAdminRequest(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


class DeleteAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceBotArn: str


class DeleteAppInstanceRequest(BaseValidatorModel):
    AppInstanceArn: str


class DeleteAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceUserArn: str


class DeregisterAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str


class DescribeAppInstanceAdminRequest(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


class DescribeAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceBotArn: str


class DescribeAppInstanceRequest(BaseValidatorModel):
    AppInstanceArn: str


class DescribeAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str


class DescribeAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceUserArn: str


class GetAppInstanceRetentionSettingsRequest(BaseValidatorModel):
    AppInstanceArn: str


class InvokedBy(BaseValidatorModel):
    StandardMessages: StandardMessagesType
    TargetedMessages: TargetedMessagesType


class ListAppInstanceAdminsRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstanceBotsRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstanceUserEndpointsRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstanceUsersRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstancesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateAppInstanceRequest(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    Metadata: str


class UpdateAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None


class UpdateAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    Name: str
    Metadata: str


class AppInstanceAdminSummary(BaseValidatorModel):
    Admin: Optional[Identity] = None


class AppInstanceAdmin(BaseValidatorModel):
    Admin: Optional[Identity] = None
    AppInstanceArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class AppInstanceRetentionSettings(BaseValidatorModel):
    ChannelRetentionSettings: Optional[ChannelRetentionSettings] = None


class AppInstanceUserEndpointSummary(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    EndpointId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AppInstanceUserEndpointTypeType] = None
    AllowMessages: Optional[AllowMessagesType] = None
    EndpointState: Optional[EndpointState] = None


class AppInstanceUserEndpoint(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    EndpointId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AppInstanceUserEndpointTypeType] = None
    ResourceArn: Optional[str] = None
    EndpointAttributes: Optional[EndpointAttributes] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    AllowMessages: Optional[AllowMessagesType] = None
    EndpointState: Optional[EndpointState] = None


class RegisterAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    Type: AppInstanceUserEndpointTypeType
    ResourceArn: str
    EndpointAttributes: EndpointAttributes
    ClientRequestToken: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None


class AppInstanceUser(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


class PutAppInstanceUserExpirationSettingsRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    ExpirationSettings: Optional[ExpirationSettings] = None


class CreateAppInstanceAdminResponse(BaseValidatorModel):
    AppInstanceAdmin: Identity
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadata


class CreateAppInstanceBotResponse(BaseValidatorModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadata


class CreateAppInstanceResponse(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadata


class CreateAppInstanceUserResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadata


class DescribeAppInstanceResponse(BaseValidatorModel):
    AppInstance: AppInstance
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListAppInstanceBotsResponse(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceBots: List[AppInstanceBotSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAppInstanceUsersResponse(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAppInstancesResponse(BaseValidatorModel):
    AppInstances: List[AppInstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutAppInstanceUserExpirationSettingsResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    ExpirationSettings: ExpirationSettings
    ResponseMetadata: ResponseMetadata


class RegisterAppInstanceUserEndpointResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadata


class UpdateAppInstanceBotResponse(BaseValidatorModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadata


class UpdateAppInstanceResponse(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadata


class UpdateAppInstanceUserEndpointResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadata


class UpdateAppInstanceUserResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadata


class CreateAppInstanceRequest(BaseValidatorModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class LexConfiguration(BaseValidatorModel):
    LexBotAliasArn: str
    LocaleId: str
    RespondsTo: Optional[Literal['STANDARD_MESSAGES']] = None
    InvokedBy: Optional[InvokedBy] = None
    WelcomeIntent: Optional[str] = None


class ListAppInstanceAdminsResponse(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAppInstanceAdminResponse(BaseValidatorModel):
    AppInstanceAdmin: AppInstanceAdmin
    ResponseMetadata: ResponseMetadata


class GetAppInstanceRetentionSettingsResponse(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class PutAppInstanceRetentionSettingsRequest(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettings


class PutAppInstanceRetentionSettingsResponse(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ListAppInstanceUserEndpointsResponse(BaseValidatorModel):
    AppInstanceUserEndpoints: List[AppInstanceUserEndpointSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAppInstanceUserEndpointResponse(BaseValidatorModel):
    AppInstanceUserEndpoint: AppInstanceUserEndpoint
    ResponseMetadata: ResponseMetadata


class DescribeAppInstanceUserResponse(BaseValidatorModel):
    AppInstanceUser: AppInstanceUser
    ResponseMetadata: ResponseMetadata


class Configuration(BaseValidatorModel):
    Lex: LexConfiguration


class AppInstanceBot(BaseValidatorModel):
    AppInstanceBotArn: Optional[str] = None
    Name: Optional[str] = None
    Configuration: Optional[Configuration] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None


class CreateAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceArn: str
    ClientRequestToken: str
    Configuration: Configuration
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceBotArn: str
    Name: str
    Metadata: str
    Configuration: Optional[Configuration] = None


class DescribeAppInstanceBotResponse(BaseValidatorModel):
    AppInstanceBot: AppInstanceBot
    ResponseMetadata: ResponseMetadata