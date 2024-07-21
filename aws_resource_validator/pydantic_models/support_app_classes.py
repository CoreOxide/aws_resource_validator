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
from aws_resource_validator.pydantic_models.support_app_constants import *

class CreateSlackChannelConfigurationRequestRequestTypeDef(BaseModel):
    channelId: str
    channelRoleArn: str
    notifyOnCaseSeverity: NotificationSeverityLevelType
    teamId: str
    channelName: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None

class DeleteSlackChannelConfigurationRequestRequestTypeDef(BaseModel):
    channelId: str
    teamId: str

class DeleteSlackWorkspaceConfigurationRequestRequestTypeDef(BaseModel):
    teamId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ListSlackChannelConfigurationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class SlackChannelConfigurationTypeDef(BaseModel):
    channelId: str
    teamId: str
    channelName: Optional[str] = None
    channelRoleArn: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCaseSeverity: Optional[NotificationSeverityLevelType] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None

class ListSlackWorkspaceConfigurationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class SlackWorkspaceConfigurationTypeDef(BaseModel):
    teamId: str
    allowOrganizationMemberAccount: Optional[bool] = None
    teamName: Optional[str] = None

class PutAccountAliasRequestRequestTypeDef(BaseModel):
    accountAlias: str

class RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef(BaseModel):
    teamId: str

class UpdateSlackChannelConfigurationRequestRequestTypeDef(BaseModel):
    channelId: str
    teamId: str
    channelName: Optional[str] = None
    channelRoleArn: Optional[str] = None
    notifyOnAddCorrespondenceToCase: Optional[bool] = None
    notifyOnCaseSeverity: Optional[NotificationSeverityLevelType] = None
    notifyOnCreateOrReopenCase: Optional[bool] = None
    notifyOnResolveCase: Optional[bool] = None

class GetAccountAliasResultTypeDef(BaseModel):
    accountAlias: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSlackWorkspaceForOrganizationResultTypeDef(BaseModel):
    accountType: AccountTypeType
    teamId: str
    teamName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSlackChannelConfigurationResultTypeDef(BaseModel):
    channelId: str
    channelName: str
    channelRoleArn: str
    notifyOnAddCorrespondenceToCase: bool
    notifyOnCaseSeverity: NotificationSeverityLevelType
    notifyOnCreateOrReopenCase: bool
    notifyOnResolveCase: bool
    teamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSlackChannelConfigurationsResultTypeDef(BaseModel):
    nextToken: str
    slackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSlackWorkspaceConfigurationsResultTypeDef(BaseModel):
    nextToken: str
    slackWorkspaceConfigurations: List[SlackWorkspaceConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

