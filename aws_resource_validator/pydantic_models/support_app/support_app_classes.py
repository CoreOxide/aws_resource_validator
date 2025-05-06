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


class ListSlackWorkspaceConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class SlackWorkspaceConfiguration(BaseValidatorModel):
    teamId: str
    allowOrganizationMemberAccount: Optional[bool] = None
    teamName: Optional[str] = None


class PutAccountAliasRequest(BaseValidatorModel):
    accountAlias: str


class RegisterSlackWorkspaceForOrganizationRequest(BaseValidatorModel):
    teamId: str


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


class RegisterSlackWorkspaceForOrganizationResult(BaseValidatorModel):
    accountType: AccountTypeType
    teamId: str
    teamName: str
    ResponseMetadata: ResponseMetadata


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


class ListSlackChannelConfigurationsResult(BaseValidatorModel):
    slackChannelConfigurations: List[SlackChannelConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSlackWorkspaceConfigurationsResult(BaseValidatorModel):
    slackWorkspaceConfigurations: List[SlackWorkspaceConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None