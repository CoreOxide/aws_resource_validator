from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.support_app.support_app_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CreateSlackChannelConfigurationRequest(BaseValidatorModel):
    channelId: str
    channelRoleArn: str
    notifyOnCaseSeverity: NotificationSeverityLevelType
    teamId: str
    channelName: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None


class DeleteSlackChannelConfigurationRequest(BaseValidatorModel):
    channelId: str
    teamId: str


class DeleteSlackWorkspaceConfigurationRequest(BaseValidatorModel):
    teamId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'list_slack_channel_configurations' function.
class ListSlackChannelConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class SlackChannelConfiguration(BaseValidatorModel):
    channelId: str
    teamId: str
    channelName: Optional[str] = None
    channelRoleArn: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCaseSeverity: Optional[NotificationSeverityLevelType] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None


# This class is the input for the 'list_slack_workspace_configurations' function.
class ListSlackWorkspaceConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class SlackWorkspaceConfiguration(BaseValidatorModel):
    teamId: str
    allowOrganizationMemberAccount: Optional[bool] = None
    teamName: Optional[str] = None


class PutAccountAliasRequest(BaseValidatorModel):
    accountAlias: str


# This class is the input for the 'register_slack_workspace_for_organization' function.
class RegisterSlackWorkspaceForOrganizationRequest(BaseValidatorModel):
    teamId: str


# This class is the input for the 'update_slack_channel_configuration' function.
class UpdateSlackChannelConfigurationRequest(BaseValidatorModel):
    channelId: str
    teamId: str
    channelName: Optional[str] = None
    channelRoleArn: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCaseSeverity: Optional[NotificationSeverityLevelType] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None


class GetAccountAliasResult(BaseValidatorModel):
    accountAlias: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_slack_workspace_for_organization' function.
class RegisterSlackWorkspaceForOrganizationResult(BaseValidatorModel):
    accountType: AccountTypeType
    teamId: str
    teamName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_slack_channel_configuration' function.
class UpdateSlackChannelConfigurationResult(BaseValidatorModel):
    channelId: str
    channelName: str
    channelRoleArn: str
    notifyOnAddCorrespondenceToCase: bool
    notifyOnCaseSeverity: NotificationSeverityLevelType
    notifyOnCreateOrReopenCase: bool
    notifyOnResolveCase: bool
    teamId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_slack_channel_configurations' function.
class ListSlackChannelConfigurationsResult(BaseValidatorModel):
    slackChannelConfigurations: List[SlackChannelConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_slack_workspace_configurations' function.
class ListSlackWorkspaceConfigurationsResult(BaseValidatorModel):
    slackWorkspaceConfigurations: List[SlackWorkspaceConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None