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
from aws_resource_validator.pydantic_models.support_app_constants import *

class CreateSlackChannelConfigurationRequestTypeDef(BaseValidatorModel):
    channelId: str
    channelRoleArn: str
    notifyOnCaseSeverity: NotificationSeverityLevelType
    teamId: str
    channelName: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None


class DeleteSlackChannelConfigurationRequestTypeDef(BaseValidatorModel):
    channelId: str
    teamId: str


class DeleteSlackWorkspaceConfigurationRequestTypeDef(BaseValidatorModel):
    teamId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ListSlackChannelConfigurationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class SlackChannelConfigurationTypeDef(BaseValidatorModel):
    channelId: str
    teamId: str
    channelName: Optional[str] = None
    channelRoleArn: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCaseSeverity: Optional[NotificationSeverityLevelType] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None


class ListSlackWorkspaceConfigurationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class SlackWorkspaceConfigurationTypeDef(BaseValidatorModel):
    teamId: str
    allowOrganizationMemberAccount: Optional[bool] = None
    teamName: Optional[str] = None


class PutAccountAliasRequestTypeDef(BaseValidatorModel):
    accountAlias: str


class RegisterSlackWorkspaceForOrganizationRequestTypeDef(BaseValidatorModel):
    teamId: str


class UpdateSlackChannelConfigurationRequestTypeDef(BaseValidatorModel):
    channelId: str
    teamId: str
    channelName: Optional[str] = None
    channelRoleArn: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCaseSeverity: Optional[NotificationSeverityLevelType] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None


class GetAccountAliasResultTypeDef(BaseValidatorModel):
    accountAlias: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterSlackWorkspaceForOrganizationResultTypeDef(BaseValidatorModel):
    accountType: AccountTypeType
    teamId: str
    teamName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSlackChannelConfigurationResultTypeDef(BaseValidatorModel):
    channelId: str
    channelName: str
    channelRoleArn: str
    notifyOnAddCorrespondenceToCase: bool
    notifyOnCaseSeverity: NotificationSeverityLevelType
    notifyOnCreateOrReopenCase: bool
    notifyOnResolveCase: bool
    teamId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListSlackChannelConfigurationsResultTypeDef(BaseValidatorModel):
    slackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSlackWorkspaceConfigurationsResultTypeDef(BaseValidatorModel):
    slackWorkspaceConfigurations: List[SlackWorkspaceConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


