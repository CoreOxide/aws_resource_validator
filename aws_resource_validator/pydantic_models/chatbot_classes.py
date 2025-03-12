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
from aws_resource_validator.pydantic_models.chatbot_constants import *

class AccountPreferencesTypeDef(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None


class AssociateToConfigurationRequestTypeDef(BaseValidatorModel):
    Resource: str
    ChatConfiguration: str


class AssociationListingTypeDef(BaseValidatorModel):
    Resource: str


class TagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValue: str


class ConfiguredTeamTypeDef(BaseValidatorModel):
    TenantId: str
    TeamId: str
    TeamName: Optional[str] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomActionDefinitionTypeDef(BaseValidatorModel):
    CommandText: str


class CustomActionAttachmentCriteriaTypeDef(BaseValidatorModel):
    Operator: CustomActionAttachmentCriteriaOperatorType
    VariableName: str
    Value: Optional[str] = None


class DeleteChimeWebhookConfigurationRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str


class DeleteCustomActionRequestTypeDef(BaseValidatorModel):
    CustomActionArn: str


class DeleteMicrosoftTeamsUserIdentityRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    UserId: str


class DeleteSlackChannelConfigurationRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str


class DeleteSlackUserIdentityRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str


class DeleteSlackWorkspaceAuthorizationRequestTypeDef(BaseValidatorModel):
    SlackTeamId: str


class DeleteTeamsChannelConfigurationRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str


class DeleteTeamsConfiguredTeamRequestTypeDef(BaseValidatorModel):
    TeamId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeChimeWebhookConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None


class DescribeSlackChannelConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChatConfigurationArn: Optional[str] = None


class DescribeSlackUserIdentitiesRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SlackUserIdentityTypeDef(BaseValidatorModel):
    IamRoleArn: str
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str
    AwsUserIdentity: Optional[str] = None


class DescribeSlackWorkspacesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SlackWorkspaceTypeDef(BaseValidatorModel):
    SlackTeamId: str
    SlackTeamName: str
    State: Optional[str] = None
    StateReason: Optional[str] = None


class DisassociateFromConfigurationRequestTypeDef(BaseValidatorModel):
    Resource: str
    ChatConfiguration: str


class GetCustomActionRequestTypeDef(BaseValidatorModel):
    CustomActionArn: str


class GetTeamsChannelConfigurationRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str


class ListAssociationsRequestTypeDef(BaseValidatorModel):
    ChatConfiguration: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomActionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMicrosoftTeamsConfiguredTeamsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMicrosoftTeamsUserIdentitiesRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class ListTeamsChannelConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TeamId: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateAccountPreferencesRequestTypeDef(BaseValidatorModel):
    UserAuthorizationRequired: Optional[bool] = None
    TrainingDataCollectionEnabled: Optional[bool] = None


class UpdateChimeWebhookConfigurationRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    WebhookDescription: Optional[str] = None
    WebhookUrl: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None


class UpdateSlackChannelConfigurationRequestTypeDef(BaseValidatorModel):
    ChatConfigurationArn: str
    SlackChannelId: str
    SlackChannelName: Optional[str] = None
    SnsTopicArns: Optional[Sequence[str]] = None
    IamRoleArn: Optional[str] = None
    LoggingLevel: Optional[str] = None
    GuardrailPolicyArns: Optional[Sequence[str]] = None
    UserAuthorizationRequired: Optional[bool] = None


class UpdateTeamsChannelConfigurationRequestTypeDef(BaseValidatorModel):
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
    State: Optional[str] = None
    StateReason: Optional[str] = None


class CreateChimeWebhookConfigurationRequestTypeDef(BaseValidatorModel):
    WebhookDescription: str
    WebhookUrl: str
    SnsTopicArns: Sequence[str]
    IamRoleArn: str
    ConfigurationName: str
    LoggingLevel: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateSlackChannelConfigurationRequestTypeDef(BaseValidatorModel):
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


class CreateTeamsChannelConfigurationRequestTypeDef(BaseValidatorModel):
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
    State: Optional[str] = None
    StateReason: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
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
    State: Optional[str] = None
    StateReason: Optional[str] = None


class CreateCustomActionResultTypeDef(BaseValidatorModel):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountPreferencesResultTypeDef(BaseValidatorModel):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[AssociationListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCustomActionsResultTypeDef(BaseValidatorModel):
    CustomActions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class UpdateCustomActionResultTypeDef(BaseValidatorModel):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CustomActionAttachmentOutputTypeDef(BaseValidatorModel):
    NotificationType: Optional[str] = None
    ButtonText: Optional[str] = None
    Criteria: Optional[List[CustomActionAttachmentCriteriaTypeDef]] = None
    Variables: Optional[Dict[str, str]] = None


class CustomActionAttachmentTypeDef(BaseValidatorModel):
    NotificationType: Optional[str] = None
    ButtonText: Optional[str] = None
    Criteria: Optional[Sequence[CustomActionAttachmentCriteriaTypeDef]] = None
    Variables: Optional[Mapping[str, str]] = None


class DescribeChimeWebhookConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSlackChannelConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSlackUserIdentitiesRequestPaginateTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSlackWorkspacesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    ChatConfiguration: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomActionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMicrosoftTeamsConfiguredTeamsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMicrosoftTeamsUserIdentitiesRequestPaginateTypeDef(BaseValidatorModel):
    ChatConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTeamsChannelConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    TeamId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


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


class CustomActionTypeDef(BaseValidatorModel):
    CustomActionArn: str
    Definition: CustomActionDefinitionTypeDef
    AliasName: Optional[str] = None
    Attachments: Optional[List[CustomActionAttachmentOutputTypeDef]] = None
    ActionName: Optional[str] = None


class GetCustomActionResultTypeDef(BaseValidatorModel):
    CustomAction: CustomActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CustomActionAttachmentUnionTypeDef(BaseValidatorModel):
    pass


class CreateCustomActionRequestTypeDef(BaseValidatorModel):
    Definition: CustomActionDefinitionTypeDef
    ActionName: str
    AliasName: Optional[str] = None
    Attachments: Optional[Sequence[CustomActionAttachmentUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class UpdateCustomActionRequestTypeDef(BaseValidatorModel):
    CustomActionArn: str
    Definition: CustomActionDefinitionTypeDef
    AliasName: Optional[str] = None
    Attachments: Optional[Sequence[CustomActionAttachmentUnionTypeDef]] = None


