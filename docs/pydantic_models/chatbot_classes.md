# chatbot_classes

# AccountPreferencesTypeDef

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### TrainingDataCollectionEnabled
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChimeWebhookConfigurationTypeDef

### WebhookDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArns
- **Type**: typing.List[str]
- **Required**: Yes

### ConfigurationName
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]


# ConfiguredTeamTypeDef

### TenantId
- **Type**: <class 'str'>
- **Required**: Yes

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### TeamName
- **Type**: typing.Optional[str]


# CreateChimeWebhookConfigurationRequestRequestTypeDef

### WebhookDescription
- **Type**: <class 'str'>
- **Required**: Yes

### WebhookUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingLevel
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]


# CreateChimeWebhookConfigurationResultTypeDef

### WebhookConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ChimeWebhookConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSlackChannelConfigurationRequestRequestTypeDef

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelName
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.Sequence[str]]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.Sequence[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]


# CreateSlackChannelConfigurationResultTypeDef

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.SlackChannelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTeamsChannelConfigurationRequestRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### TenantId
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: typing.Optional[str]

### TeamName
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.Sequence[str]]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.Sequence[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]


# CreateTeamsChannelConfigurationResultTypeDef

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.TeamsChannelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChimeWebhookConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackChannelConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackUserIdentityRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackUserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTeamsChannelConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTeamsConfiguredTeamRequestRequestTypeDef

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChimeWebhookConfigurationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChatConfigurationArn
- **Type**: typing.Optional[str]


# DescribeChimeWebhookConfigurationsResultTypeDef

### WebhookConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.ChimeWebhookConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackChannelConfigurationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChatConfigurationArn
- **Type**: typing.Optional[str]


# DescribeSlackChannelConfigurationsResultTypeDef

### SlackChannelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.SlackChannelConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackUserIdentitiesRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeSlackUserIdentitiesResultTypeDef

### SlackUserIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.SlackUserIdentityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackWorkspacesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackWorkspacesResultTypeDef

### SlackWorkspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.SlackWorkspaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAccountPreferencesResultTypeDef

### AccountPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.AccountPreferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTeamsChannelConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTeamsChannelConfigurationResultTypeDef

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.TeamsChannelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMicrosoftTeamsConfiguredTeamsResultTypeDef

### ConfiguredTeams
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.ConfiguredTeamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMicrosoftTeamsUserIdentitiesResultTypeDef

### TeamsUserIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.TeamsUserIdentityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTeamsChannelConfigurationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]


# ListTeamsChannelConfigurationsResultTypeDef

### TeamChannelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.TeamsChannelConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

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


# SlackChannelConfigurationTypeDef

### SlackTeamName
- **Type**: <class 'str'>
- **Required**: Yes

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArns
- **Type**: typing.List[str]
- **Required**: Yes

### ConfigurationName
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]


# SlackUserIdentityTypeDef

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackUserId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsUserIdentity
- **Type**: typing.Optional[str]


# SlackWorkspaceTypeDef

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackTeamName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes


# TeamsChannelConfigurationTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### TenantId
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArns
- **Type**: typing.List[str]
- **Required**: Yes

### ChannelName
- **Type**: typing.Optional[str]

### TeamName
- **Type**: typing.Optional[str]

### ConfigurationName
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]


# TeamsUserIdentityTypeDef

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### AwsUserIdentity
- **Type**: typing.Optional[str]

### TeamsChannelId
- **Type**: typing.Optional[str]

### TeamsTenantId
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountPreferencesRequestRequestTypeDef

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### TrainingDataCollectionEnabled
- **Type**: typing.Optional[bool]


# UpdateAccountPreferencesResultTypeDef

### AccountPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.AccountPreferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChimeWebhookConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### WebhookDescription
- **Type**: typing.Optional[str]

### WebhookUrl
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.Sequence[str]]

### IamRoleArn
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]


# UpdateChimeWebhookConfigurationResultTypeDef

### WebhookConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ChimeWebhookConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSlackChannelConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelName
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.Sequence[str]]

### IamRoleArn
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.Sequence[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]


# UpdateSlackChannelConfigurationResultTypeDef

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.SlackChannelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTeamsChannelConfigurationRequestRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.Sequence[str]]

### IamRoleArn
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.Sequence[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]


# UpdateTeamsChannelConfigurationResultTypeDef

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.TeamsChannelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


