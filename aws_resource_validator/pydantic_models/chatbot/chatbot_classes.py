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


class DescribeChimeWebhookConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None


class DescribeSlackChannelConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None


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


class GetCustomActionRequest(BaseValidatorModel):
    CustomActionArn: str


class GetTeamsChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str


class ListAssociationsRequest(BaseValidatorModel):
    ChatConfiguration: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomActionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMicrosoftTeamsConfiguredTeamsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class ListTeamsChannelConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TeamId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateAccountPreferencesRequest(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None


class UpdateChimeWebhookConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    WebhookDescription: Optional[str] = None
    WebhookUrl: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None


class UpdateSlackChannelConfigurationRequest(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackChannelId: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[List[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[List[str]] = None
    UserAuthorizationRequired: Optional[bool] = None


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


class CreateChimeWebhookConfigurationRequest(BaseValidatorModel):
    WebhookDescription: str
    WebhookUrl: str
    SnsTopicArns: List[str]
    IamRoleArn: str
    ConfigurationName: str
    LoggingLevel: Optional[str] = None
    Tags: Optional[List[Tag]] = None


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


class CreateCustomActionResult(BaseValidatorModel):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadata


class GetAccountPreferencesResult(BaseValidatorModel):
    AccountPreferences: AccountPreferences
    ResponseMetadata: ResponseMetadata


class ListAssociationsResult(BaseValidatorModel):
    Associations: List[AssociationListing]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCustomActionsResult(BaseValidatorModel):
    CustomActions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMicrosoftTeamsConfiguredTeamsResult(BaseValidatorModel):
    ConfiguredTeams: List[ConfiguredTeam]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateAccountPreferencesResult(BaseValidatorModel):
    AccountPreferences: AccountPreferences
    ResponseMetadata: ResponseMetadata


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


class DescribeSlackUserIdentitiesResult(BaseValidatorModel):
    SlackUserIdentities: List[SlackUserIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSlackWorkspacesResult(BaseValidatorModel):
    SlackWorkspaces: List[SlackWorkspace]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMicrosoftTeamsUserIdentitiesResult(BaseValidatorModel):
    TeamsUserIdentities: List[TeamsUserIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateChimeWebhookConfigurationResult(BaseValidatorModel):
    WebhookConfiguration: ChimeWebhookConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeChimeWebhookConfigurationsResult(BaseValidatorModel):
    WebhookConfigurations: List[ChimeWebhookConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateChimeWebhookConfigurationResult(BaseValidatorModel):
    WebhookConfiguration: ChimeWebhookConfiguration
    ResponseMetadata: ResponseMetadata


class CreateSlackChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: SlackChannelConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeSlackChannelConfigurationsResult(BaseValidatorModel):
    SlackChannelConfigurations: List[SlackChannelConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSlackChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: SlackChannelConfiguration
    ResponseMetadata: ResponseMetadata


class CreateTeamsChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfiguration
    ResponseMetadata: ResponseMetadata


class GetTeamsChannelConfigurationResult(BaseValidatorModel):
    ChannelConfiguration: TeamsChannelConfiguration
    ResponseMetadata: ResponseMetadata


class ListTeamsChannelConfigurationsResult(BaseValidatorModel):
    TeamChannelConfigurations: List[TeamsChannelConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class GetCustomActionResult(BaseValidatorModel):
    CustomAction: CustomAction
    ResponseMetadata: ResponseMetadata


class CreateCustomActionRequest(BaseValidatorModel):
    Definition: CustomActionDefinition
    ActionName: str
    AliasName: Optional[str] = None
    Attachments: Optional[List[CustomActionAttachmentUnion]] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class UpdateCustomActionRequest(BaseValidatorModel):
    CustomActionArn: str
    Definition: CustomActionDefinition
    AliasName: Optional[str] = None
    Attachments: Optional[List[CustomActionAttachmentUnion]] = None