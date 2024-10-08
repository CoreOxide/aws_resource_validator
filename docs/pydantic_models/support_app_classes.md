# Pydantic Models in support_app_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateSlackChannelConfigurationRequestRequestTypeDef

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### channelRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### notifyOnCaseSeverity
- **Type**: typing.Literal['all', 'high', 'none']
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: typing.Optional[str]

### notifyOnAddCorrespondenceToCase
- **Type**: typing.Optional[bool]

### notifyOnCreateOrReopenCase
- **Type**: typing.Optional[bool]

### notifyOnResolveCase
- **Type**: typing.Optional[bool]


# DeleteSlackChannelConfigurationRequestRequestTypeDef

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackWorkspaceConfigurationRequestRequestTypeDef

### teamId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountAliasResultTypeDef

### accountAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSlackChannelConfigurationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListSlackChannelConfigurationsResultTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### slackChannelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_app_classes.SlackChannelConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSlackWorkspaceConfigurationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListSlackWorkspaceConfigurationsResultTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### slackWorkspaceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_app_classes.SlackWorkspaceConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAccountAliasRequestRequestTypeDef

### accountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef

### teamId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterSlackWorkspaceForOrganizationResultTypeDef

### accountType
- **Type**: typing.Literal['management', 'member']
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### teamName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# SlackChannelConfigurationTypeDef

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: typing.Optional[str]

### channelRoleArn
- **Type**: typing.Optional[str]

### notifyOnAddCorrespondenceToCase
- **Type**: typing.Optional[bool]

### notifyOnCaseSeverity
- **Type**: typing.Optional[typing.Literal['all', 'high', 'none']]

### notifyOnCreateOrReopenCase
- **Type**: typing.Optional[bool]

### notifyOnResolveCase
- **Type**: typing.Optional[bool]


# SlackWorkspaceConfigurationTypeDef

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### allowOrganizationMemberAccount
- **Type**: typing.Optional[bool]

### teamName
- **Type**: typing.Optional[str]


# UpdateSlackChannelConfigurationRequestRequestTypeDef

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: typing.Optional[str]

### channelRoleArn
- **Type**: typing.Optional[str]

### notifyOnAddCorrespondenceToCase
- **Type**: typing.Optional[bool]

### notifyOnCaseSeverity
- **Type**: typing.Optional[typing.Literal['all', 'high', 'none']]

### notifyOnCreateOrReopenCase
- **Type**: typing.Optional[bool]

### notifyOnResolveCase
- **Type**: typing.Optional[bool]


# UpdateSlackChannelConfigurationResultTypeDef

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### notifyOnAddCorrespondenceToCase
- **Type**: <class 'bool'>
- **Required**: Yes

### notifyOnCaseSeverity
- **Type**: typing.Literal['all', 'high', 'none']
- **Required**: Yes

### notifyOnCreateOrReopenCase
- **Type**: <class 'bool'>
- **Required**: Yes

### notifyOnResolveCase
- **Type**: <class 'bool'>
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


