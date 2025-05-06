# Chatbot Classes

# AccountPreferences

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### TrainingDataCollectionEnabled
- **Type**: typing.Optional[bool]


# AssociateToConfigurationRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationListing

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChimeWebhookConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# ConfiguredTeam

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


# CreateChimeWebhookConfigurationRequest

### WebhookDescription
- **Type**: <class 'str'>
- **Required**: Yes

### WebhookUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArns
- **Type**: typing.List[str]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]


# CreateChimeWebhookConfigurationResult

### WebhookConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ChimeWebhookConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomActionRequest

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionDefinition'>
- **Required**: Yes

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachment, aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachmentOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateCustomActionResult

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSlackChannelConfigurationRequest

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
- **Type**: typing.Optional[typing.List[str]]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]


# CreateSlackChannelConfigurationResult

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.SlackChannelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTeamsChannelConfigurationRequest

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
- **Type**: typing.Optional[typing.List[str]]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]


# CreateTeamsChannelConfigurationResult

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.TeamsChannelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# CustomAction

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionDefinition'>
- **Required**: Yes

### AliasName
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachmentOutput]]

### ActionName
- **Type**: typing.Optional[str]


# CustomActionAttachment

### NotificationType
- **Type**: typing.Optional[str]

### ButtonText
- **Type**: typing.Optional[str]

### Criteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachmentCriteria]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# CustomActionAttachmentCriteria

### Operator
- **Type**: typing.Literal['EQUALS', 'HAS_VALUE']
- **Required**: Yes

### VariableName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# CustomActionAttachmentOutput

### NotificationType
- **Type**: typing.Optional[str]

### ButtonText
- **Type**: typing.Optional[str]

### Criteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachmentCriteria]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# CustomActionDefinition

### CommandText
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChimeWebhookConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomActionRequest

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMicrosoftTeamsUserIdentityRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackChannelConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackUserIdentityRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackUserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlackWorkspaceAuthorizationRequest

### SlackTeamId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTeamsChannelConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTeamsConfiguredTeamRequest

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChimeWebhookConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChatConfigurationArn
- **Type**: typing.Optional[str]


# DescribeChimeWebhookConfigurationsRequestPaginate

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# DescribeChimeWebhookConfigurationsResult

### WebhookConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ChimeWebhookConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackChannelConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChatConfigurationArn
- **Type**: typing.Optional[str]


# DescribeSlackChannelConfigurationsRequestPaginate

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# DescribeSlackChannelConfigurationsResult

### SlackChannelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.SlackChannelConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackUserIdentitiesRequest

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeSlackUserIdentitiesRequestPaginate

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# DescribeSlackUserIdentitiesResult

### SlackUserIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.SlackUserIdentity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackWorkspacesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSlackWorkspacesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# DescribeSlackWorkspacesResult

### SlackWorkspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.SlackWorkspace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateFromConfigurationRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountPreferencesResult

### AccountPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.AccountPreferences'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# GetCustomActionRequest

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomActionResult

### CustomAction
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomAction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# GetTeamsChannelConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTeamsChannelConfigurationResult

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.TeamsChannelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# ListAssociationsRequest

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsRequestPaginate

### ChatConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# ListAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.AssociationListing]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomActionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomActionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# ListCustomActionsResult

### CustomActions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMicrosoftTeamsConfiguredTeamsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMicrosoftTeamsConfiguredTeamsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# ListMicrosoftTeamsConfiguredTeamsResult

### ConfiguredTeams
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ConfiguredTeam]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMicrosoftTeamsUserIdentitiesRequest

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMicrosoftTeamsUserIdentitiesRequestPaginate

### ChatConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# ListMicrosoftTeamsUserIdentitiesResult

### TeamsUserIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.TeamsUserIdentity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# ListTeamsChannelConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]


# ListTeamsChannelConfigurationsRequestPaginate

### TeamId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.PaginatorConfig]


# ListTeamsChannelConfigurationsResult

### TeamChannelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.TeamsChannelConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# SlackUserIdentity

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


# SlackWorkspace

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


# Tag

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]
- **Required**: Yes


# TeamsChannelConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.Tag]]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# TeamsUserIdentity

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


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccountPreferencesRequest

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]

### TrainingDataCollectionEnabled
- **Type**: typing.Optional[bool]


# UpdateAccountPreferencesResult

### AccountPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.AccountPreferences'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChimeWebhookConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### WebhookDescription
- **Type**: typing.Optional[str]

### WebhookUrl
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.List[str]]

### IamRoleArn
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]


# UpdateChimeWebhookConfigurationResult

### WebhookConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ChimeWebhookConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomActionRequest

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionDefinition'>
- **Required**: Yes

### AliasName
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachment, aws_resource_validator.pydantic_models.chatbot.chatbot_classes.CustomActionAttachmentOutput]]]


# UpdateCustomActionResult

### CustomActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSlackChannelConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### SlackChannelName
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.List[str]]

### IamRoleArn
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]


# UpdateSlackChannelConfigurationResult

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.SlackChannelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTeamsChannelConfigurationRequest

### ChatConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: typing.Optional[str]

### SnsTopicArns
- **Type**: typing.Optional[typing.List[str]]

### IamRoleArn
- **Type**: typing.Optional[str]

### LoggingLevel
- **Type**: typing.Optional[str]

### GuardrailPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### UserAuthorizationRequired
- **Type**: typing.Optional[bool]


# UpdateTeamsChannelConfigurationResult

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.TeamsChannelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chatbot.chatbot_classes.ResponseMetadata'>
- **Required**: Yes


