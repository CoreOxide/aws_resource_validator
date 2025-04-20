# Support App Support App Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateSlackChannelConfigurationRequest

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


# DeleteSlackChannelConfigurationRequest

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### teamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackWorkspaceConfigurationRequest

### teamId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountAliasResult

### accountAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app.support_app_classes.ResponseMetadata'>
- **Required**: Yes


# ListSlackChannelConfigurationsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListSlackChannelConfigurationsResult

### slackChannelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_app.support_app_classes.SlackChannelConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app.support_app_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSlackWorkspaceConfigurationsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListSlackWorkspaceConfigurationsResult

### slackWorkspaceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.support_app.support_app_classes.SlackWorkspaceConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app.support_app_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PutAccountAliasRequest

### accountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterSlackWorkspaceForOrganizationRequest

### teamId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterSlackWorkspaceForOrganizationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app.support_app_classes.ResponseMetadata'>
- **Required**: Yes


# ResponseMetadata

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


# SlackChannelConfiguration

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


# SlackWorkspaceConfiguration

### teamId
- **Type**: <class 'str'>
- **Required**: Yes

### allowOrganizationMemberAccount
- **Type**: typing.Optional[bool]

### teamName
- **Type**: typing.Optional[str]


# UpdateSlackChannelConfigurationRequest

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


# UpdateSlackChannelConfigurationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.support_app.support_app_classes.ResponseMetadata'>
- **Required**: Yes


