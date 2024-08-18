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

class CreateAppInstanceAdminRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class DeleteAppInstanceAdminRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DeleteAppInstanceBotRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str

class DeleteAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class DeleteAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str

class DeregisterAppInstanceUserEndpointRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str

class DescribeAppInstanceAdminRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DescribeAppInstanceBotRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str

class DescribeAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class DescribeAppInstanceUserEndpointRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str

class DescribeAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str

class GetAppInstanceRetentionSettingsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class InvokedByTypeDef(BaseValidatorModel):
    StandardMessages: StandardMessagesType
    TargetedMessages: TargetedMessagesType

class ListAppInstanceAdminsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceBotsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceUserEndpointsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceUsersRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstancesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    Metadata: str

class UpdateAppInstanceUserEndpointRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    EndpointId: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None

class UpdateAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
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

class AppInstanceUserEndpointSummaryTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    EndpointId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AppInstanceUserEndpointTypeType] = None
    AllowMessages: Optional[AllowMessagesType] = None
    EndpointState: Optional[EndpointStateTypeDef] = None

class AppInstanceUserEndpointTypeDef(BaseValidatorModel):
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

class RegisterAppInstanceUserEndpointRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    Type: AppInstanceUserEndpointTypeType
    ResourceArn: str
    EndpointAttributes: EndpointAttributesTypeDef
    ClientRequestToken: str
    Name: Optional[str] = None
    AllowMessages: Optional[AllowMessagesType] = None

class AppInstanceUserTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    ExpirationSettings: Optional[ExpirationSettingsTypeDef] = None

class PutAppInstanceUserExpirationSettingsRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUsersResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstancesResponseTypeDef(BaseValidatorModel):
    AppInstances: List[AppInstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceAdminResponseTypeDef(BaseValidatorModel):
    AppInstanceAdmin: AppInstanceAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceRetentionSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceRetentionSettingsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef

class PutAppInstanceRetentionSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUserEndpointsResponseTypeDef(BaseValidatorModel):
    AppInstanceUserEndpoints: List[AppInstanceUserEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateAppInstanceBotRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ClientRequestToken: str
    Configuration: ConfigurationTypeDef
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateAppInstanceBotRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceBotArn: str
    Name: str
    Metadata: str
    Configuration: Optional[ConfigurationTypeDef] = None

class DescribeAppInstanceBotResponseTypeDef(BaseValidatorModel):
    AppInstanceBot: AppInstanceBotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

