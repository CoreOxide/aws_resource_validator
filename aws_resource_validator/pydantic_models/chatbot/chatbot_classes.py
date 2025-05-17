from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.chatbot.chatbot_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountPreferences(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None


class AssociateToConfigurationRequest(BaseValidatorModel):
    Resource: str
    ChatConfiguration: str


class AssociationListing(BaseValidatorModel):
    Resource: str


class Tag(BaseValidatorModel):
    TagKey: str
    TagValue: str


class ConfiguredTeam(BaseValidatorModel):
    TenantId: str
    TeamId: str
    TeamName: Optional[str] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomActionDefinition(BaseValidatorModel):
    CommandText: str


class CustomActionAttachmentCriteria(BaseValidatorModel):
    Operator: CustomActionAttachmentCriteriaOperatorType
    VariableName: str
    Value: Optional[str] = None


class DeleteChimeWebhookConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str


class DeleteCustomActionRequest(BaseValidatorModel):
    CustomActionArn: str


class DeleteMicrosoftTeamsUserIdentityRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    UserId: str


class DeleteSlackChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str


class DeleteSlackUserIdentityRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str


class DeleteSlackWorkspaceAuthorizationRequest(BaseValidatorModel):
    SlackTeamId: str


class DeleteTeamsChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str


class DeleteTeamsConfiguredTeamRequest(BaseValidatorModel):
    TeamId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_chime_webhook_configurations' function.
class DescribeChimeWebhookConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None


# This class is the input for the 'describe_slack_channel_configurations' function.
class DescribeSlackChannelConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None


# This class is the input for the 'describe_slack_user_identities' function.
class DescribeSlackUserIdentitiesRequest(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SlackUserIdentity(BaseValidatorModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str
    AwsUserIdentity: Optional[str] = None


# This class is the input for the 'describe_slack_workspaces' function.
class DescribeSlackWorkspacesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SlackWorkspace(BaseValidatorModel):
    SlackTeamId: str
    SlackTeamName: str
    State: Optional[str] = None
    StateReason: Optional[str] = None


class DisassociateFromConfigurationRequest(BaseValidatorModel):
    Resource: str
    ChatConfiguration: str


# This class is the input for the 'get_custom_action' function.
class GetCustomActionRequest(BaseValidatorModel):
    CustomActionArn: str


# This class is the input for the 'get_microsoft_teams_channel_configuration' function.
class GetTeamsChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str


# This class is the input for the 'list_associations' function.
class ListAssociationsRequest(BaseValidatorModel):
    ChatConfiguration: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_custom_actions' function.
class ListCustomActionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_microsoft_teams_configured_teams' function.
class ListMicrosoftTeamsConfiguredTeamsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_microsoft_teams_user_identities' function.
class ListMicrosoftTeamsUserIdentitiesRequest(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TeamsUserIdentity(BaseValidatorModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    TeamId: str
    UserId: Optional[str] = None
    AwsUserIdentity: Optional[str] = None
    TeamsChannelId: Optional[str] = None
    TeamsTenantId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'list_microsoft_teams_channel_configurations' function.
class ListTeamsChannelConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TeamId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_account_preferences' function.
class UpdateAccountPreferencesRequest(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None


# This class is the input for the 'update_chime_webhook_configuration' function.
class UpdateChimeWebhookConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    WebhookDescription: Optional[str] = None
    WebhookUrl: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None


# This class is the input for the 'update_slack_channel_configuration' function.
class UpdateSlackChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackChannelId: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None


# This class is the input for the 'update_microsoft_teams_channel_configuration' function.
class UpdateTeamsChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    ChannelId: str
    ChannelName: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None


class ChimeWebhookConfiguration(BaseValidatorModel):
    WebhookDescription: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ConfigurationName: Optional[str] = None
    LoggingLevel: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


# This class is the input for the 'create_chime_webhook_configuration' function.
class CreateChimeWebhookConfigurationRequest(BaseValidatorModel):
    WebhookDescription: str
    WebhookUrl: str
    SnsTopicArns: List[str]
    IamRoleArn: str
    ConfigurationName: str
    LoggingLevel: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_slack_channel_configuration' function.
class CreateSlackChannelConfigurationRequest(BaseValidatorModel):
    SlackTeamId: str
    SlackChannelId: str
    IamRoleArn: str
    ConfigurationName: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_microsoft_teams_channel_configuration' function.
class CreateTeamsChannelConfigurationRequest(BaseValidatorModel):
    ChannelId: str
    TeamId: str
    TenantId: str
    IamRoleArn: str
    ConfigurationName: str
    ChannelName: Optional[str] = None
    TeamName: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class SlackChannelConfiguration(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class TeamsChannelConfiguration(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


# This class is the output for the 'create_custom_action' function.
class CreateCustomActionResult(BaseValidatorModel):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadata


class GetAccountPreferencesResult(BaseValidatorModel):
    AccountPreferences: AccountPreferences
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_associations' function.
class ListAssociationsResult(BaseValidatorModel):
    Associations: List[AssociationListing]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_custom_actions' function.
class ListCustomActionsResult(BaseValidatorModel):
    CustomActions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_microsoft_teams_configured_teams' function.
class ListMicrosoftTeamsConfiguredTeamsResult(BaseValidatorModel):
    ConfiguredTeams: List[ConfiguredTeam]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_account_preferences' function.
class UpdateAccountPreferencesResult(BaseValidatorModel):
    AccountPreferences: AccountPreferences
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_custom_action' function.
class UpdateCustomActionResult(BaseValidatorModel):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadata


class CustomActionAttachmentOutput(BaseValidatorModel):
    NotificationType: Optional[str] = None
    ButtonText: Optional[str] = None
    Criteria: Optional[List[CustomActionAttachmentCriteria]] = None
    Variables: Optional[Dict[str, str]] = None


class CustomActionAttachment(BaseValidatorModel):
    NotificationType: Optional[str] = None
    ButtonText: Optional[str] = None
    Criteria: Optional[List[CustomActionAttachmentCriteria]] = None
    Variables: Optional[Dict[str, str]] = None


class DescribeChimeWebhookConfigurationsRequestPaginate(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSlackChannelConfigurationsRequestPaginate(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSlackUserIdentitiesRequestPaginate(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSlackWorkspacesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociationsRequestPaginate(BaseValidatorModel):
    ChatConfiguration: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomActionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMicrosoftTeamsConfiguredTeamsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMicrosoftTeamsUserIdentitiesRequestPaginate(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTeamsChannelConfigurationsRequestPaginate(BaseValidatorModel):
    TeamId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_slack_user_identities' function.
class DescribeSlackUserIdentitiesResult(BaseValidatorModel):
    SlackUserIdentities: List[SlackUserIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_slack_workspaces' function.
class DescribeSlackWorkspacesResult(BaseValidatorModel):
    SlackWorkspaces: List[SlackWorkspace]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_microsoft_teams_user_identities' function.
class ListMicrosoftTeamsUserIdentitiesResult(BaseValidatorModel):
    TeamsUserIdentities: List[TeamsUserIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_chime_webhook_configuration' function.
class CreateChimeWebhookConfigurationResult(BaseValidatorModel):
    WebhookConfiguration: ChimeWebhookConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_chime_webhook_configurations' function.
class DescribeChimeWebhookConfigurationsResult(BaseValidatorModel):
    WebhookConfigurations: List[ChimeWebhookConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_chime_webhook_configuration' function.
class UpdateChimeWebhookConfigurationResult(BaseValidatorModel):
    WebhookConfiguration: ChimeWebhookConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_slack_channel_configuration' function.
class CreateSlackChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: SlackChannelConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_slack_channel_configurations' function.
class DescribeSlackChannelConfigurationsResult(BaseValidatorModel):
    SlackChannelConfigurations: List[SlackChannelConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_slack_channel_configuration' function.
class UpdateSlackChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: SlackChannelConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_microsoft_teams_channel_configuration' function.
class CreateTeamsChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_microsoft_teams_channel_configuration' function.
class GetTeamsChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_microsoft_teams_channel_configurations' function.
class ListTeamsChannelConfigurationsResult(BaseValidatorModel):
    TeamChannelConfigurations: List[TeamsChannelConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_microsoft_teams_channel_configuration' function.
class UpdateTeamsChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfiguration
    ResponseMetadata: ResponseMetadata


class CustomAction(BaseValidatorModel):
    CustomActionArn: str
    Definition: CustomActionDefinition
    AliasName: Optional[str] = None
    Attachments: Optional[List[CustomActionAttachmentOutput]] = None
    ActionName: Optional[str] = None

CustomActionAttachmentUnion = Union[CustomActionAttachment, CustomActionAttachmentOutput]


# This class is the output for the 'get_custom_action' function.
class GetCustomActionResult(BaseValidatorModel):
    CustomAction: CustomAction
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_custom_action' function.
class CreateCustomActionRequest(BaseValidatorModel):
    Definition: CustomActionDefinition
    ActionName: str
    AliasName: Optional[str] = None
    Attachments: Optional[List[CustomActionAttachmentUnion]] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_custom_action' function.
class UpdateCustomActionRequest(BaseValidatorModel):
    CustomActionArn: str
    Definition: CustomActionDefinition
    AliasName: Optional[str] = None
    Attachments: Optional[List[CustomActionAttachmentUnion]] = None