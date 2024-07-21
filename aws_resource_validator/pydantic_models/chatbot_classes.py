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
from aws_resource_validator.pydantic_models.chatbot_constants import *

class AccountPreferencesTypeDef(BaseModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None

class TagTypeDef(BaseModel):
    TagKey: str
    TagValue: str

class ConfiguredTeamTypeDef(BaseModel):
    TenantId: str
    TeamId: str
    TeamName: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteChimeWebhookConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str

class DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str
    UserId: str

class DeleteSlackChannelConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str

class DeleteSlackUserIdentityRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str

class DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef(BaseModel):
    SlackTeamId: str

class DeleteTeamsChannelConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str

class DeleteTeamsConfiguredTeamRequestRequestTypeDef(BaseModel):
    TeamId: str

class DescribeChimeWebhookConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None

class DescribeSlackChannelConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None

class DescribeSlackUserIdentitiesRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SlackUserIdentityTypeDef(BaseModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str
    AwsUserIdentity: Optional[str] = None

class DescribeSlackWorkspacesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SlackWorkspaceTypeDef(BaseModel):
    SlackTeamId: str
    SlackTeamName: str

class GetTeamsChannelConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str

class ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TeamsUserIdentityTypeDef(BaseModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    TeamId: str
    UserId: Optional[str] = None
    AwsUserIdentity: Optional[str] = None
    TeamsChannelId: Optional[str] = None
    TeamsTenantId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListTeamsChannelConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TeamId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountPreferencesRequestRequestTypeDef(BaseModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None

class UpdateChimeWebhookConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str
    WebhookDescription: Optional[str] = None
    WebhookUrl: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None

class UpdateSlackChannelConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str
    SlackChannelId: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None

class UpdateTeamsChannelConfigurationRequestRequestTypeDef(BaseModel):
    ChatConfigurationArn: str
    ChannelId: str
    ChannelName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None

class ChimeWebhookConfigurationTypeDef(BaseModel):
    WebhookDescription: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ConfigurationName: Optional[str] = None
    LoggingLevel: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateChimeWebhookConfigurationRequestRequestTypeDef(BaseModel):
    WebhookDescription: str
    WebhookUrl: str
    SnsTopicArns: Sequence[str]
    IamRoleArn: str
    ConfigurationName: str
    LoggingLevel: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSlackChannelConfigurationRequestRequestTypeDef(BaseModel):
    SlackTeamId: str
    SlackChannelId: str
    IamRoleArn: str
    ConfigurationName: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTeamsChannelConfigurationRequestRequestTypeDef(BaseModel):
    ChannelId: str
    TeamId: str
    TenantId: str
    IamRoleArn: str
    ConfigurationName: str
    ChannelName: Optional[str] = None
    TeamName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SlackChannelConfigurationTypeDef(BaseModel):
    SlackTeamName: str
    SlackTeamId: str
    SlackChannelId: str
    SlackChannelName: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ConfigurationName: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class TeamsChannelConfigurationTypeDef(BaseModel):
    ChannelId: str
    TeamId: str
    TenantId: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ChannelName: Optional[str] = None
    TeamName: Optional[str] = None
    ConfigurationName: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None
    Tags: Optional[List[TagTypeDef]] = None

class GetAccountPreferencesResultTypeDef(BaseModel):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMicrosoftTeamsConfiguredTeamsResultTypeDef(BaseModel):
    ConfiguredTeams: List[ConfiguredTeamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountPreferencesResultTypeDef(BaseModel):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlackUserIdentitiesResultTypeDef(BaseModel):
    SlackUserIdentities: List[SlackUserIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSlackWorkspacesResultTypeDef(BaseModel):
    SlackWorkspaces: List[SlackWorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMicrosoftTeamsUserIdentitiesResultTypeDef(BaseModel):
    TeamsUserIdentities: List[TeamsUserIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateChimeWebhookConfigurationResultTypeDef(BaseModel):
    WebhookConfiguration: ChimeWebhookConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChimeWebhookConfigurationsResultTypeDef(BaseModel):
    WebhookConfigurations: List[ChimeWebhookConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateChimeWebhookConfigurationResultTypeDef(BaseModel):
    WebhookConfiguration: ChimeWebhookConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSlackChannelConfigurationResultTypeDef(BaseModel):
    ChannelConfiguration: SlackChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlackChannelConfigurationsResultTypeDef(BaseModel):
    SlackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSlackChannelConfigurationResultTypeDef(BaseModel):
    ChannelConfiguration: SlackChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTeamsChannelConfigurationResultTypeDef(BaseModel):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTeamsChannelConfigurationResultTypeDef(BaseModel):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTeamsChannelConfigurationsResultTypeDef(BaseModel):
    TeamChannelConfigurations: List[TeamsChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateTeamsChannelConfigurationResultTypeDef(BaseModel):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

