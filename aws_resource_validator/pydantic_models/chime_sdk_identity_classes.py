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
from aws_resource_validator.pydantic_models.chime_sdk_identity_constants import *

class IdentityTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class AppInstanceBotSummaryTypeDef(BaseValidatorModel):
    AppInstanceBotArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None


class ChannelRetentionSettingsTypeDef(BaseValidatorModel):
    RetentionDays: Optional[int] = None


class AppInstanceSummaryTypeDef(BaseValidatorModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None


class AppInstanceTypeDef(BaseValidatorModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None


class EndpointStateTypeDef(BaseValidatorModel):
    Status: EndpointStatusType
    StatusReason: Optional[EndpointStatusReasonType] = None


class EndpointAttributesTypeDef(BaseValidatorModel):
    DeviceToken: str
    VoipDeviceToken: Optional[str] = None


class AppInstanceUserSummaryTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None


class ExpirationSettingsTypeDef(BaseValidatorModel):
    ExpirationDays: int
    ExpirationCriterion: Literal["CREATED_TIMESTAMP"]


class CreateAppInstanceAdminRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DeleteAppInstanceAdminRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


class DeleteAppInstanceBotRequestTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str


class DeleteAppInstanceRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str


class DeleteAppInstanceUserRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str


class DeregisterAppInstanceUserEndpointRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str


class DescribeAppInstanceAdminRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str


class DescribeAppInstanceBotRequestTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str


class DescribeAppInstanceRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str


class DescribeAppInstanceUserEndpointRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str


class DescribeAppInstanceUserRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str


class GetAppInstanceRetentionSettingsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str


class InvokedByTypeDef(BaseValidatorModel):
    StandardMessages: StandardMessagesType
    TargetedMessages: TargetedMessagesType


class ListAppInstanceAdminsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstanceBotsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstanceUserEndpointsRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstanceUsersRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppInstancesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateAppInstanceRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    Metadata: str


class UpdateAppInstanceUserEndpointRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None


class UpdateAppInstanceUserRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    Name: str
    Metadata: str


class AppInstanceAdminSummaryTypeDef(BaseValidatorModel):
    Admin: Optional[IdentityTypeDef] = None


class AppInstanceAdminTypeDef(BaseValidatorModel):
    Admin: Optional[IdentityTypeDef] = None
    AppInstanceArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class AppInstanceRetentionSettingsTypeDef(BaseValidatorModel):
    ChannelRetentionSettings: Optional[ChannelRetentionSettingsTypeDef] = None


class AppInstanceUserTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None


class PutAppInstanceUserExpirationSettingsRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None


class CreateAppInstanceAdminResponseTypeDef(BaseValidatorModel):
    AppInstanceAdmin: IdentityTypeDef
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAppInstanceBotResponseTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAppInstanceResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAppInstanceUserResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppInstanceResponseTypeDef(BaseValidatorModel):
    AppInstance: AppInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppInstanceBotsResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceBots: List[AppInstanceBotSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAppInstanceUsersResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAppInstancesResponseTypeDef(BaseValidatorModel):
    AppInstances: List[AppInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutAppInstanceUserExpirationSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterAppInstanceUserEndpointResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppInstanceBotResponseTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppInstanceResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppInstanceUserEndpointResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppInstanceUserResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAppInstanceRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateAppInstanceUserRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class LexConfigurationTypeDef(BaseValidatorModel):
    LexBotAliasArn: str
    LocaleId: str
    RespondsTo: Optional[Literal["STANDARD_MESSAGES"]] = None
    InvokedBy: Optional[InvokedByTypeDef] = None
    WelcomeIntent: Optional[str] = None


class ListAppInstanceAdminsResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeAppInstanceAdminResponseTypeDef(BaseValidatorModel):
    AppInstanceAdmin: AppInstanceAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppInstanceRetentionSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PutAppInstanceRetentionSettingsRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef


class PutAppInstanceRetentionSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class AppInstanceUserEndpointSummaryTypeDef(BaseValidatorModel):
    pass


class ListAppInstanceUserEndpointsResponseTypeDef(BaseValidatorModel):
    AppInstanceUserEndpoints: List[AppInstanceUserEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AppInstanceUserEndpointTypeDef(BaseValidatorModel):
    pass


class DescribeAppInstanceUserEndpointResponseTypeDef(BaseValidatorModel):
    AppInstanceUserEndpoint: AppInstanceUserEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppInstanceUserResponseTypeDef(BaseValidatorModel):
    AppInstanceUser: AppInstanceUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConfigurationTypeDef(BaseValidatorModel):
    Lex: LexConfigurationTypeDef


class AppInstanceBotTypeDef(BaseValidatorModel):
    AppInstanceBotArn: Optional[str] = None
    Name: Optional[str] = None
    Configuration: Optional[ConfigurationTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None


class CreateAppInstanceBotRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ClientRequestToken: str
    Configuration: ConfigurationTypeDef
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateAppInstanceBotRequestTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str
    Name: str
    Metadata: str
    Configuration: Optional[ConfigurationTypeDef] = None


class DescribeAppInstanceBotResponseTypeDef(BaseValidatorModel):
    AppInstanceBot: AppInstanceBotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


