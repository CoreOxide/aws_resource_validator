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
from aws_resource_validator.pydantic_models.chime_sdk_identity_constants import *

class IdentityTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AppInstanceBotSummaryTypeDef(BaseModel):
    AppInstanceBotArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class ChannelRetentionSettingsTypeDef(BaseModel):
    RetentionDays: Optional[int] = None

class AppInstanceSummaryTypeDef(BaseModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class AppInstanceTypeDef(BaseModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None

class EndpointStateTypeDef(BaseModel):
    Status: EndpointStatusType
    StatusReason: Optional[EndpointStatusReasonType] = None

class EndpointAttributesTypeDef(BaseModel):
    DeviceToken: str
    VoipDeviceToken: Optional[str] = None

class AppInstanceUserSummaryTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class ExpirationSettingsTypeDef(BaseModel):
    ExpirationDays: int
    ExpirationCriterion: Literal["CREATED_TIMESTAMP"]

class CreateAppInstanceAdminRequestRequestTypeDef(BaseModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteAppInstanceAdminRequestRequestTypeDef(BaseModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DeleteAppInstanceBotRequestRequestTypeDef(BaseModel):
    AppInstanceBotArn: str

class DeleteAppInstanceRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class DeleteAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str

class DeregisterAppInstanceUserEndpointRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    EndpointId: str

class DescribeAppInstanceAdminRequestRequestTypeDef(BaseModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DescribeAppInstanceBotRequestRequestTypeDef(BaseModel):
    AppInstanceBotArn: str

class DescribeAppInstanceRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class DescribeAppInstanceUserEndpointRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    EndpointId: str

class DescribeAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str

class GetAppInstanceRetentionSettingsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class InvokedByTypeDef(BaseModel):
    StandardMessages: StandardMessagesType
    TargetedMessages: TargetedMessagesType

class ListAppInstanceAdminsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceBotsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceUserEndpointsRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceUsersRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstancesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAppInstanceRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    Name: str
    Metadata: str

class UpdateAppInstanceUserEndpointRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    EndpointId: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None

class UpdateAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    Name: str
    Metadata: str

class AppInstanceAdminSummaryTypeDef(BaseModel):
    Admin: Optional[IdentityTypeDef] = None

class AppInstanceAdminTypeDef(BaseModel):
    Admin: Optional[IdentityTypeDef] = None
    AppInstanceArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class AppInstanceRetentionSettingsTypeDef(BaseModel):
    ChannelRetentionSettings: Optional[ChannelRetentionSettingsTypeDef] = None

class AppInstanceUserEndpointSummaryTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    EndpointId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AppInstanceUserEndpointTypeType] = None
    AllowMessages: Optional[AllowMessagesType] = None
    EndpointState: Optional[EndpointStateTypeDef] = None

class AppInstanceUserEndpointTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    EndpointId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AppInstanceUserEndpointTypeType] = None
    ResourceArn: Optional[str] = None
    EndpointAttributes: Optional[EndpointAttributesTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    AllowMessages: Optional[AllowMessagesType] = None
    EndpointState: Optional[EndpointStateTypeDef] = None

class RegisterAppInstanceUserEndpointRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    Type: AppInstanceUserEndpointTypeType
    ResourceArn: str
    EndpointAttributes: EndpointAttributesTypeDef
    ClientRequestToken: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None

class AppInstanceUserTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class PutAppInstanceUserExpirationSettingsRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class CreateAppInstanceAdminResponseTypeDef(BaseModel):
    AppInstanceAdmin: IdentityTypeDef
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceBotResponseTypeDef(BaseModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceResponseTypeDef(BaseModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceUserResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceResponseTypeDef(BaseModel):
    AppInstance: AppInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceBotsResponseTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceBots: List[AppInstanceBotSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUsersResponseTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstancesResponseTypeDef(BaseModel):
    AppInstances: List[AppInstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceUserExpirationSettingsResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAppInstanceUserEndpointResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceBotResponseTypeDef(BaseModel):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceResponseTypeDef(BaseModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceUserEndpointResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceUserResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceRequestRequestTypeDef(BaseModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class LexConfigurationTypeDef(BaseModel):
    LexBotAliasArn: str
    LocaleId: str
    RespondsTo: Optional[Literal["STANDARD_MESSAGES"]] = None
    InvokedBy: Optional[InvokedByTypeDef] = None
    WelcomeIntent: Optional[str] = None

class ListAppInstanceAdminsResponseTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceAdminResponseTypeDef(BaseModel):
    AppInstanceAdmin: AppInstanceAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceRetentionSettingsResponseTypeDef(BaseModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceRetentionSettingsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef

class PutAppInstanceRetentionSettingsResponseTypeDef(BaseModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUserEndpointsResponseTypeDef(BaseModel):
    AppInstanceUserEndpoints: List[AppInstanceUserEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceUserEndpointResponseTypeDef(BaseModel):
    AppInstanceUserEndpoint: AppInstanceUserEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceUserResponseTypeDef(BaseModel):
    AppInstanceUser: AppInstanceUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationTypeDef(BaseModel):
    Lex: LexConfigurationTypeDef

class AppInstanceBotTypeDef(BaseModel):
    AppInstanceBotArn: Optional[str] = None
    Name: Optional[str] = None
    Configuration: Optional[ConfigurationTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None

class CreateAppInstanceBotRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    ClientRequestToken: str
    Configuration: ConfigurationTypeDef
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateAppInstanceBotRequestRequestTypeDef(BaseModel):
    AppInstanceBotArn: str
    Name: str
    Metadata: str
    Configuration: Optional[ConfigurationTypeDef] = None

class DescribeAppInstanceBotResponseTypeDef(BaseModel):
    AppInstanceBot: AppInstanceBotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

