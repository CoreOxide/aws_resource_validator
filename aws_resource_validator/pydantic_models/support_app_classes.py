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
from aws_resource_validator.pydantic_models.support_app_constants import *

class CreateSlackChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    channelId: str
    channelRoleArn: str
    notifyOnCaseSeverity: NotificationSeverityLevelType
    teamId: str
    channelName: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None

class DeleteSlackChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
    channelId: str
    teamId: str

class DeleteSlackWorkspaceConfigurationRequestRequestTypeDef(BaseValidatorModel):
    teamId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ListSlackChannelConfigurationsRequestRequestTypeDef(BaseValidatorModel):
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

class ListSlackWorkspaceConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class SlackWorkspaceConfigurationTypeDef(BaseValidatorModel):
    teamId: str
    allowOrganizationMemberAccount: Optional[bool] = None
    teamName: Optional[str] = None

class PutAccountAliasRequestRequestTypeDef(BaseValidatorModel):
    accountAlias: str

class RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    teamId: str

class UpdateSlackChannelConfigurationRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    slackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSlackWorkspaceConfigurationsResultTypeDef(BaseValidatorModel):
    nextToken: str
    slackWorkspaceConfigurations: List[SlackWorkspaceConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

