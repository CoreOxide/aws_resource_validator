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


# This class is the input for the 'create_app_instance_admin' function.
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


# This class is the input for the 'delete_app_instance_admin' function.
class DeleteAppInstanceAdminRequest(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


# This class is the input for the 'delete_app_instance_bot' function.
class DeleteAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceBotArn: str


# This class is the input for the 'delete_app_instance' function.
class DeleteAppInstanceRequest(BaseValidatorModel):
    AppInstanceArn: str


# This class is the input for the 'delete_app_instance_user' function.
class DeleteAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceUserArn: str


# This class is the input for the 'deregister_app_instance_user_endpoint' function.
class DeregisterAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str


# This class is the input for the 'describe_app_instance_admin' function.
class DescribeAppInstanceAdminRequest(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


# This class is the input for the 'describe_app_instance_bot' function.
class DescribeAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceBotArn: str


# This class is the input for the 'describe_app_instance' function.
class DescribeAppInstanceRequest(BaseValidatorModel):
    AppInstanceArn: str


# This class is the input for the 'describe_app_instance_user_endpoint' function.
class DescribeAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str


# This class is the input for the 'describe_app_instance_user' function.
class DescribeAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceUserArn: str


# This class is the input for the 'get_app_instance_retention_settings' function.
class GetAppInstanceRetentionSettingsRequest(BaseValidatorModel):
    AppInstanceArn: str


class InvokedBy(BaseValidatorModel):
    StandardMessages: StandardMessagesType
    TargetedMessages: TargetedMessagesType


# This class is the input for the 'list_app_instance_admins' function.
class ListAppInstanceAdminsRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_app_instance_bots' function.
class ListAppInstanceBotsRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_app_instance_user_endpoints' function.
class ListAppInstanceUserEndpointsRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_app_instance_users' function.
class ListAppInstanceUsersRequest(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_app_instances' function.
class ListAppInstancesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_app_instance' function.
class UpdateAppInstanceRequest(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    Metadata: str


# This class is the input for the 'update_app_instance_user_endpoint' function.
class UpdateAppInstanceUserEndpointRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None


# This class is the input for the 'update_app_instance_user' function.
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


# This class is the input for the 'register_app_instance_user_endpoint' function.
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


# This class is the input for the 'put_app_instance_user_expiration_settings' function.
class PutAppInstanceUserExpirationSettingsRequest(BaseValidatorModel):
    AppInstanceUserArn: str
    ExpirationSettings: Optional[ExpirationSettings] = None


# This class is the output for the 'create_app_instance_admin' function.
class CreateAppInstanceAdminResponse(BaseValidatorModel):
    AppInstanceAdmin: Identity
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_app_instance_bot' function.
class CreateAppInstanceBotResponse(BaseValidatorModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_app_instance' function.
class CreateAppInstanceResponse(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_app_instance_user' function.
class CreateAppInstanceUserResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_instance' function.
class DescribeAppInstanceResponse(BaseValidatorModel):
    AppInstance: AppInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_instance_bots' function.
class ListAppInstanceBotsResponse(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceBots: List[AppInstanceBotSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_app_instance_users' function.
class ListAppInstanceUsersResponse(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_app_instances' function.
class ListAppInstancesResponse(BaseValidatorModel):
    AppInstances: List[AppInstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_app_instance_user_expiration_settings' function.
class PutAppInstanceUserExpirationSettingsResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    ExpirationSettings: ExpirationSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_app_instance_user_endpoint' function.
class RegisterAppInstanceUserEndpointResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_instance_bot' function.
class UpdateAppInstanceBotResponse(BaseValidatorModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_instance' function.
class UpdateAppInstanceResponse(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_instance_user_endpoint' function.
class UpdateAppInstanceUserEndpointResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_instance_user' function.
class UpdateAppInstanceUserResponse(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_app_instance' function.
class CreateAppInstanceRequest(BaseValidatorModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_app_instance_user' function.
class CreateAppInstanceUserRequest(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ExpirationSettings: Optional[ExpirationSettings] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class LexConfiguration(BaseValidatorModel):
    LexBotAliasArn: str
    LocaleId: str
    RespondsTo: Optional[Literal['STANDARD_MESSAGES']] = None
    InvokedBy: Optional[InvokedBy] = None
    WelcomeIntent: Optional[str] = None


# This class is the output for the 'list_app_instance_admins' function.
class ListAppInstanceAdminsResponse(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_app_instance_admin' function.
class DescribeAppInstanceAdminResponse(BaseValidatorModel):
    AppInstanceAdmin: AppInstanceAdmin
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_app_instance_retention_settings' function.
class GetAppInstanceRetentionSettingsResponse(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_app_instance_retention_settings' function.
class PutAppInstanceRetentionSettingsRequest(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettings


# This class is the output for the 'put_app_instance_retention_settings' function.
class PutAppInstanceRetentionSettingsResponse(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_instance_user_endpoints' function.
class ListAppInstanceUserEndpointsResponse(BaseValidatorModel):
    AppInstanceUserEndpoints: List[AppInstanceUserEndpointSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_app_instance_user_endpoint' function.
class DescribeAppInstanceUserEndpointResponse(BaseValidatorModel):
    AppInstanceUserEndpoint: AppInstanceUserEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_instance_user' function.
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


# This class is the input for the 'create_app_instance_bot' function.
class CreateAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceArn: str
    ClientRequestToken: str
    Configuration: Configuration
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_app_instance_bot' function.
class UpdateAppInstanceBotRequest(BaseValidatorModel):
    AppInstanceBotArn: str
    Name: str
    Metadata: str
    Configuration: Optional[Configuration] = None


# This class is the output for the 'describe_app_instance_bot' function.
class DescribeAppInstanceBotResponse(BaseValidatorModel):
    AppInstanceBot: AppInstanceBot
    ResponseMetadata: ResponseMetadata