# Chatbot Classes

# AccountPreferencesTypeDef

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### TrainingDataCollectionEnabled
- **Type**: typing.Optional[bool]


# AssociateToConfigurationRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationListingTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


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

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# ConfiguredTeamTypeDef

### TenantId
- **Type**: <class 'str'>
- **Required**: Yes

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### TeamName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# CreateChimeWebhookConfigurationRequestTypeDef

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


# CreateCustomActionRequestTypeDef

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.CustomActionDefinitionTypeDef'>
- **Required**: Yes

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.CustomActionAttachmentUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateCustomActionResultTypeDef

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSlackChannelConfigurationRequestTypeDef

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


# CreateTeamsChannelConfigurationRequestTypeDef

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


# CustomActionAttachmentCriteriaTypeDef

### Operator
- **Type**: typing.Literal['EQUALS', 'HAS_VALUE']
- **Required**: Yes

### VariableName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# CustomActionAttachmentOutputTypeDef

### NotificationType
- **Type**: typing.Optional[str]

### ButtonText
- **Type**: typing.Optional[str]

### Criteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot_classes.CustomActionAttachmentCriteriaTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# CustomActionAttachmentTypeDef

### NotificationType
- **Type**: typing.Optional[str]

### ButtonText
- **Type**: typing.Optional[str]

### Criteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.CustomActionAttachmentCriteriaTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CustomActionAttachmentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomActionDefinitionTypeDef

### CommandText
- **Type**: <class 'str'>
- **Required**: Yes


# CustomActionTypeDef

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.CustomActionDefinitionTypeDef'>
- **Required**: Yes

### AliasName
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot_classes.CustomActionAttachmentOutputTypeDef]]

### ActionName
- **Type**: typing.Optional[str]


# DeleteChimeWebhookConfigurationRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomActionRequestTypeDef

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMicrosoftTeamsUserIdentityRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackChannelConfigurationRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackUserIdentityRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackUserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackWorkspaceAuthorizationRequestTypeDef

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTeamsChannelConfigurationRequestTypeDef

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTeamsConfiguredTeamRequestTypeDef

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChimeWebhookConfigurationsRequestPaginateTypeDef

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# DescribeChimeWebhookConfigurationsRequestTypeDef

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


# DescribeSlackChannelConfigurationsRequestPaginateTypeDef

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# DescribeSlackChannelConfigurationsRequestTypeDef

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


# DescribeSlackUserIdentitiesRequestPaginateTypeDef

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# DescribeSlackUserIdentitiesRequestTypeDef

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


# DescribeSlackWorkspacesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# DescribeSlackWorkspacesRequestTypeDef

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


# DisassociateFromConfigurationRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountPreferencesResultTypeDef

### AccountPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.AccountPreferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCustomActionRequestTypeDef

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomActionResultTypeDef

### CustomAction
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.CustomActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTeamsChannelConfigurationRequestTypeDef

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


# ListAssociationsRequestPaginateTypeDef

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# ListAssociationsRequestTypeDef

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot_classes.AssociationListingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomActionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# ListCustomActionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomActionsResultTypeDef

### CustomActions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMicrosoftTeamsConfiguredTeamsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# ListMicrosoftTeamsConfiguredTeamsRequestTypeDef

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


# ListMicrosoftTeamsUserIdentitiesRequestPaginateTypeDef

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# ListMicrosoftTeamsUserIdentitiesRequestTypeDef

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


# ListTagsForResourceRequestTypeDef

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


# ListTeamsChannelConfigurationsRequestPaginateTypeDef

### TeamId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot_classes.PaginatorConfigTypeDef]


# ListTeamsChannelConfigurationsRequestTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


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

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

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

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


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


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountPreferencesRequestTypeDef

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


# UpdateChimeWebhookConfigurationRequestTypeDef

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


# UpdateCustomActionRequestTypeDef

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.CustomActionDefinitionTypeDef'>
- **Required**: Yes

### AliasName
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chatbot_classes.CustomActionAttachmentUnionTypeDef]]


# UpdateCustomActionResultTypeDef

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSlackChannelConfigurationRequestTypeDef

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


# UpdateTeamsChannelConfigurationRequestTypeDef

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


