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
from aws_resource_validator.pydantic_models.chatbot_constants import *

class AccountPreferencesTypeDef(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None

class TagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValue: str

class ConfiguredTeamTypeDef(BaseValidatorModel):
    TenantId: str
    TeamId: str
    TeamName: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteChimeWebhookConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str

class DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    UserId: str

class DeleteSlackChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str

class DeleteSlackUserIdentityRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str

class DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    SlackTeamId: str

class DeleteTeamsChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str

class DeleteTeamsConfiguredTeamRequestRequestTypeDef(BaseValidatorModel):
    TeamId: str

class DescribeChimeWebhookConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None

class DescribeSlackChannelConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None

class DescribeSlackUserIdentitiesRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SlackUserIdentityTypeDef(BaseValidatorModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str
    AwsUserIdentity: Optional[str] = None

class DescribeSlackWorkspacesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SlackWorkspaceTypeDef(BaseValidatorModel):
    SlackTeamId: str
    SlackTeamName: str

class GetTeamsChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str

class ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TeamsUserIdentityTypeDef(BaseValidatorModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    TeamId: str
    UserId: Optional[str] = None
    AwsUserIdentity: Optional[str] = None
    TeamsChannelId: Optional[str] = None
    TeamsTenantId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListTeamsChannelConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TeamId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountPreferencesRequestRequestTypeDef(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None

class UpdateChimeWebhookConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    WebhookDescription: Optional[str] = None
    WebhookUrl: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None

class UpdateSlackChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackChannelId: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None

class UpdateTeamsChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    ChannelId: str
    ChannelName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None

class ChimeWebhookConfigurationTypeDef(BaseValidatorModel):
    WebhookDescription: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ConfigurationName: Optional[str] = None
    LoggingLevel: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateChimeWebhookConfigurationRequestRequestTypeDef(BaseValidatorModel):
    WebhookDescription: str
    WebhookUrl: str
    SnsTopicArns: Sequence[str]
    IamRoleArn: str
    ConfigurationName: str
    LoggingLevel: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSlackChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class CreateTeamsChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class SlackChannelConfigurationTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class TeamsChannelConfigurationTypeDef(BaseValidatorModel):
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

class GetAccountPreferencesResultTypeDef(BaseValidatorModel):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMicrosoftTeamsConfiguredTeamsResultTypeDef(BaseValidatorModel):
    ConfiguredTeams: List[ConfiguredTeamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountPreferencesResultTypeDef(BaseValidatorModel):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlackUserIdentitiesResultTypeDef(BaseValidatorModel):
    SlackUserIdentities: List[SlackUserIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSlackWorkspacesResultTypeDef(BaseValidatorModel):
    SlackWorkspaces: List[SlackWorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMicrosoftTeamsUserIdentitiesResultTypeDef(BaseValidatorModel):
    TeamsUserIdentities: List[TeamsUserIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateChimeWebhookConfigurationResultTypeDef(BaseValidatorModel):
    WebhookConfiguration: ChimeWebhookConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChimeWebhookConfigurationsResultTypeDef(BaseValidatorModel):
    WebhookConfigurations: List[ChimeWebhookConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateChimeWebhookConfigurationResultTypeDef(BaseValidatorModel):
    WebhookConfiguration: ChimeWebhookConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSlackChannelConfigurationResultTypeDef(BaseValidatorModel):
    ChannelConfiguration: SlackChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlackChannelConfigurationsResultTypeDef(BaseValidatorModel):
    SlackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSlackChannelConfigurationResultTypeDef(BaseValidatorModel):
    ChannelConfiguration: SlackChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTeamsChannelConfigurationResultTypeDef(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTeamsChannelConfigurationResultTypeDef(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTeamsChannelConfigurationsResultTypeDef(BaseValidatorModel):
    TeamChannelConfigurations: List[TeamsChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateTeamsChannelConfigurationResultTypeDef(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

