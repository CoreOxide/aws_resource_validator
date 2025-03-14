# Qbusiness Classes

# APISchemaTypeDef

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.S3TypeDef]


# AccessConfigurationTypeDef

### accessControls
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.AccessControlTypeDef]
- **Required**: Yes

### memberRelation
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# AccessControlTypeDef

### principals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.PrincipalTypeDef]
- **Required**: Yes

### memberRelation
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# ActionConfigurationOutputTypeDef

### action
- **Type**: <class 'str'>
- **Required**: Yes

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionFilterConfigurationOutputTypeDef]


# ActionConfigurationTypeDef

### action
- **Type**: <class 'str'>
- **Required**: Yes

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionFilterConfigurationUnionTypeDef]


# ActionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionExecutionEventTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadFieldUnionTypeDef]
- **Required**: Yes

### payloadFieldNameSeparator
- **Type**: <class 'str'>
- **Required**: Yes


# ActionExecutionOutputTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadFieldOutputTypeDef]
- **Required**: Yes

### payloadFieldNameSeparator
- **Type**: <class 'str'>
- **Required**: Yes


# ActionExecutionPayloadFieldOutputTypeDef

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ActionExecutionPayloadFieldTypeDef

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# ActionExecutionPayloadFieldUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionExecutionTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadFieldTypeDef]
- **Required**: Yes

### payloadFieldNameSeparator
- **Type**: <class 'str'>
- **Required**: Yes


# ActionExecutionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionFilterConfigurationOutputTypeDef

### documentAttributeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterOutputTypeDef'>
- **Required**: Yes


# ActionFilterConfigurationTypeDef

### documentAttributeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnionTypeDef'>
- **Required**: Yes


# ActionFilterConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionReviewEventTypeDef

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### pluginId
- **Type**: typing.Optional[str]

### pluginType
- **Type**: typing.Optional[typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']]

### payload
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewPayloadFieldTypeDef]]

### payloadFieldNameSeparator
- **Type**: typing.Optional[str]


# ActionReviewPayloadFieldAllowedValueTypeDef

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### displayValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ActionReviewPayloadFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionReviewTypeDef

### pluginId
- **Type**: typing.Optional[str]

### pluginType
- **Type**: typing.Optional[typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']]

### payload
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewPayloadFieldTypeDef]]

### payloadFieldNameSeparator
- **Type**: typing.Optional[str]


# ActionSummaryTypeDef

### actionIdentifier
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### instructionExample
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ApplicationTypeDef

### displayName
- **Type**: typing.Optional[str]

### applicationId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### identityType
- **Type**: typing.Optional[typing.Literal['AWS_IAM_IDC', 'AWS_IAM_IDP_OIDC', 'AWS_IAM_IDP_SAML', 'AWS_QUICKSIGHT_IDP']]

### quickSightConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QuickSightConfigurationTypeDef]


# AppliedAttachmentsConfigurationTypeDef

### attachmentsControlMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AppliedCreatorModeConfigurationTypeDef

### creatorModeControl
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AppliedOrchestrationConfigurationTypeDef

### control
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AssociatePermissionRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePermissionResponseTypeDef

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachmentInputEventTypeDef

### attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentInputTypeDef]


# AttachmentInputTypeDef

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BlobTypeDef]

### name
- **Type**: typing.Optional[str]

### copyFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CopyFromSourceTypeDef]


# AttachmentOutputTypeDef

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCESS']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]

### attachmentId
- **Type**: typing.Optional[str]

### conversationId
- **Type**: typing.Optional[str]


# AttachmentTypeDef

### attachmentId
- **Type**: typing.Optional[str]

### conversationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### copyFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CopyFromSourceTypeDef]

### fileType
- **Type**: typing.Optional[str]

### fileSize
- **Type**: typing.Optional[int]

### md5chksum
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCESS']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]


# AttachmentsConfigurationTypeDef

### attachmentsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AttributeFilterOutputTypeDef

### andAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]


# AttributeFilterPaginatorTypeDef

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]


# AttributeFilterTypeDef

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnionTypeDef]


# AttributeFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioExtractionConfigurationTypeDef

### audioExtractionStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AudioSourceDetailsTypeDef

### mediaId
- **Type**: typing.Optional[str]

### mediaMimeType
- **Type**: typing.Optional[str]

### startTimeMilliseconds
- **Type**: typing.Optional[int]

### endTimeMilliseconds
- **Type**: typing.Optional[int]

### audioExtractionType
- **Type**: typing.Optional[typing.Literal['SUMMARY', 'TRANSCRIPT']]


# AuthChallengeRequestEventTypeDef

### authorizationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# AuthChallengeRequestTypeDef

### authorizationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# AuthChallengeResponseEventTypeDef

### responseMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# AuthChallengeResponseTypeDef

### responseMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# AutoSubscriptionConfigurationTypeDef

### autoSubscribe
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### defaultSubscriptionType
- **Type**: typing.Optional[typing.Literal['Q_BUSINESS', 'Q_LITE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthConfigurationTypeDef

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteDocumentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.DeleteDocumentTypeDef]
- **Required**: Yes

### dataSourceSyncId
- **Type**: typing.Optional[str]


# BatchDeleteDocumentResponseTypeDef

### failedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.FailedDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutDocumentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentTypeDef]
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### dataSourceSyncId
- **Type**: typing.Optional[str]


# BatchPutDocumentResponseTypeDef

### failedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.FailedDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockedPhrasesConfigurationTypeDef

### blockedPhrases
- **Type**: typing.Optional[typing.List[str]]

### systemMessageOverride
- **Type**: typing.Optional[str]


# BlockedPhrasesConfigurationUpdateTypeDef

### blockedPhrasesToCreateOrUpdate
- **Type**: typing.Optional[typing.Sequence[str]]

### blockedPhrasesToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### systemMessageOverride
- **Type**: typing.Optional[str]


# BrowserExtensionConfigurationOutputTypeDef

### enabledBrowserExtensions
- **Type**: typing.List[typing.Literal['CHROME', 'FIREFOX']]
- **Required**: Yes


# BrowserExtensionConfigurationTypeDef

### enabledBrowserExtensions
- **Type**: typing.Sequence[typing.Literal['CHROME', 'FIREFOX']]
- **Required**: Yes


# BrowserExtensionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSubscriptionRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionResponseTypeDef

### subscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef'>
- **Required**: Yes

### nextSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChatInputStreamTypeDef

### configurationEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ConfigurationEventTypeDef]

### textEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TextInputEventTypeDef]

### attachmentEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentInputEventTypeDef]

### actionExecutionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionEventTypeDef]

### endOfInputEvent
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### authChallengeResponseEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeResponseEventTypeDef]


# ChatInputTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### userGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### conversationId
- **Type**: typing.Optional[str]

### parentMessageId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### inputStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.qbusiness_classes.ChatInputStreamTypeDef]]


# ChatModeConfigurationTypeDef

### pluginConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PluginConfigurationTypeDef]


# ChatOutputStreamTypeDef

### textEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TextOutputEventTypeDef]

### metadataEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MetadataEventTypeDef]

### actionReviewEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewEventTypeDef]

### failedAttachmentEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.FailedAttachmentEventTypeDef]

### authChallengeRequestEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeRequestEventTypeDef]


# ChatOutputTypeDef

### outputStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.qbusiness_classes.ChatOutputStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChatSyncInputTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### userGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### userMessage
- **Type**: typing.Optional[str]

### attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentInputTypeDef]]

### actionExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionUnionTypeDef]

### authChallengeResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeResponseTypeDef]

### conversationId
- **Type**: typing.Optional[str]

### parentMessageId
- **Type**: typing.Optional[str]

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnionTypeDef]

### chatMode
- **Type**: typing.Optional[typing.Literal['CREATOR_MODE', 'PLUGIN_MODE', 'RETRIEVAL_MODE']]

### chatModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ChatModeConfigurationTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# ChatSyncOutputTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### systemMessage
- **Type**: <class 'str'>
- **Required**: Yes

### systemMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### userMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### actionReview
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewTypeDef'>
- **Required**: Yes

### authChallengeRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeRequestTypeDef'>
- **Required**: Yes

### sourceAttributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.SourceAttributionTypeDef]
- **Required**: Yes

### failedAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigurationEventTypeDef

### chatMode
- **Type**: typing.Optional[typing.Literal['CREATOR_MODE', 'PLUGIN_MODE', 'RETRIEVAL_MODE']]

### chatModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ChatModeConfigurationTypeDef]

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnionTypeDef]


# ContentBlockerRuleTypeDef

### systemMessageOverride
- **Type**: typing.Optional[str]


# ContentRetrievalRuleOutputTypeDef

### eligibleDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSourceTypeDef]]


# ContentRetrievalRuleTypeDef

### eligibleDataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSourceTypeDef]]


# ContentRetrievalRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContentSourceTypeDef

### retriever
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverContentSourceTypeDef]


# ConversationSourceTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# ConversationTypeDef

### conversationId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]


# CopyFromSourceTypeDef

### conversation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ConversationSourceTypeDef]


# CreateApplicationRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### identityType
- **Type**: typing.Optional[typing.Literal['AWS_IAM_IDC', 'AWS_IAM_IDP_OIDC', 'AWS_IAM_IDP_SAML', 'AWS_QUICKSIGHT_IDP']]

### iamIdentityProviderArn
- **Type**: typing.Optional[str]

### identityCenterInstanceArn
- **Type**: typing.Optional[str]

### clientIdsForOIDC
- **Type**: typing.Optional[typing.Sequence[str]]

### description
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.EncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### attachmentsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentsConfigurationTypeDef]

### qAppsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QAppsConfigurationTypeDef]

### personalizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PersonalizationConfigurationTypeDef]

### quickSightConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QuickSightConfigurationTypeDef]


# CreateApplicationResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataAccessorRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### actionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.ActionConfigurationUnionTypeDef]
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]


# CreateDataAccessorResponseTypeDef

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes

### idcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]

### syncSchedule
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### documentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationUnionTypeDef]

### mediaExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MediaExtractionConfigurationTypeDef]


# CreateDataSourceResponseTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIndexResponseTypeDef

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### indexArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePluginResponseTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### buildStatus
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRetrieverResponseTypeDef

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriptionResponseTypeDef

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef'>
- **Required**: Yes

### nextSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### userAliases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]]

### clientToken
- **Type**: typing.Optional[str]


# CreateWebExperienceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: typing.Optional[str]

### subtitle
- **Type**: typing.Optional[str]

### welcomeMessage
- **Type**: typing.Optional[str]

### samplePromptsControlMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### origins
- **Type**: typing.Optional[typing.Sequence[str]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### identityProviderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdentityProviderConfigurationTypeDef]

### browserExtensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BrowserExtensionConfigurationUnionTypeDef]

### customizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomizationConfigurationTypeDef]


# CreateWebExperienceResponseTypeDef

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatorModeConfigurationTypeDef

### creatorModeControl
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# CustomPluginConfigurationTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### apiSchemaType
- **Type**: typing.Literal['OPEN_API_V3']
- **Required**: Yes

### apiSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.APISchemaTypeDef'>
- **Required**: Yes


# CustomizationConfigurationTypeDef

### customCSSUrl
- **Type**: typing.Optional[str]

### logoUrl
- **Type**: typing.Optional[str]

### fontUrl
- **Type**: typing.Optional[str]

### faviconUrl
- **Type**: typing.Optional[str]


# DataAccessorTypeDef

### displayName
- **Type**: typing.Optional[str]

### dataAccessorId
- **Type**: typing.Optional[str]

### dataAccessorArn
- **Type**: typing.Optional[str]

### idcApplicationArn
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DataSourceSyncJobMetricsTypeDef

### documentsAdded
- **Type**: typing.Optional[str]

### documentsModified
- **Type**: typing.Optional[str]

### documentsDeleted
- **Type**: typing.Optional[str]

### documentsFailed
- **Type**: typing.Optional[str]

### documentsScanned
- **Type**: typing.Optional[str]


# DataSourceSyncJobTypeDef

### executionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]

### dataSourceErrorCode
- **Type**: typing.Optional[str]

### metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceSyncJobMetricsTypeDef]


# DataSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceVpcConfigurationOutputTypeDef

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# DataSourceVpcConfigurationTypeDef

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DataSourceVpcConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateAttributeBoostingConfigurationTypeDef

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### boostingDurationInSeconds
- **Type**: typing.Optional[int]


# DeleteApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttachmentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# DeleteChatControlsConfigurationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConversationRequestTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# DeleteDataAccessorRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentTypeDef

### documentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]


# DeleteIndexRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePluginRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetrieverRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebExperienceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePermissionRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentAttributeBoostingConfigurationOutputTypeDef

### numberConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NumberAttributeBoostingConfigurationTypeDef]

### stringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringAttributeBoostingConfigurationOutputTypeDef]

### dateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DateAttributeBoostingConfigurationTypeDef]

### stringListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringListAttributeBoostingConfigurationTypeDef]


# DocumentAttributeBoostingConfigurationTypeDef

### numberConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NumberAttributeBoostingConfigurationTypeDef]

### stringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringAttributeBoostingConfigurationTypeDef]

### dateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DateAttributeBoostingConfigurationTypeDef]

### stringListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringListAttributeBoostingConfigurationTypeDef]


# DocumentAttributeConditionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeConditionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueOutputTypeDef'>
- **Required**: Yes


# DocumentAttributeTargetOutputTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueOutputTypeDef]

### attributeValueOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# DocumentAttributeTargetTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueUnionTypeDef]

### attributeValueOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# DocumentAttributeTargetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueUnionTypeDef'>
- **Required**: Yes


# DocumentAttributeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeValueOutputTypeDef

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.List[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[datetime.datetime]


# DocumentAttributeValueTypeDef

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.Sequence[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef]


# DocumentAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentContentTypeDef

### blob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BlobTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.S3TypeDef]


# DocumentDetailsTypeDef

### documentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'DOCUMENT_FAILED_TO_INDEX', 'FAILED', 'INDEXED', 'PROCESSING', 'RECEIVED', 'UPDATED']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DocumentEnrichmentConfigurationOutputTypeDef

### inlineConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.InlineDocumentEnrichmentConfigurationOutputTypeDef]]

### preExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationOutputTypeDef]

### postExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationOutputTypeDef]


# DocumentEnrichmentConfigurationTypeDef

### inlineConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.InlineDocumentEnrichmentConfigurationUnionTypeDef]]

### preExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationUnionTypeDef]

### postExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationUnionTypeDef]


# DocumentEnrichmentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EligibleDataSourceTypeDef

### indexId
- **Type**: typing.Optional[str]

### dataSourceId
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigurationTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]


# ErrorDetailTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest', 'ResourceInactive', 'ResourceNotFound']]


# FailedAttachmentEventTypeDef

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentOutputTypeDef]


# FailedDocumentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponseTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityType
- **Type**: typing.Literal['AWS_IAM_IDC', 'AWS_IAM_IDP_OIDC', 'AWS_IAM_IDP_SAML', 'AWS_QUICKSIGHT_IDP']
- **Required**: Yes

### iamIdentityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef'>
- **Required**: Yes

### attachmentsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedAttachmentsConfigurationTypeDef'>
- **Required**: Yes

### qAppsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.QAppsConfigurationTypeDef'>
- **Required**: Yes

### personalizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.PersonalizationConfigurationTypeDef'>
- **Required**: Yes

### autoSubscriptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AutoSubscriptionConfigurationTypeDef'>
- **Required**: Yes

### clientIdsForOIDC
- **Type**: typing.List[str]
- **Required**: Yes

### quickSightConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.QuickSightConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChatControlsConfigurationRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# GetChatControlsConfigurationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetChatControlsConfigurationResponseTypeDef

### responseScope
- **Type**: typing.Literal['ENTERPRISE_CONTENT_ONLY', 'EXTENDED_KNOWLEDGE_ENABLED']
- **Required**: Yes

### orchestrationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedOrchestrationConfigurationTypeDef'>
- **Required**: Yes

### blockedPhrases
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.BlockedPhrasesConfigurationTypeDef'>
- **Required**: Yes

### topicConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationOutputTypeDef]
- **Required**: Yes

### creatorModeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedCreatorModeConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetDataAccessorRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataAccessorResponseTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorArn
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### idcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### actionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionConfigurationOutputTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]


# GetGroupResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.GroupStatusDetailTypeDef'>
- **Required**: Yes

### statusHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.GroupStatusDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIndexRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### mediaId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaResponseTypeDef

### mediaBytes
- **Type**: <class 'bytes'>
- **Required**: Yes

### mediaMimeType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPluginRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRetrieverRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponseTypeDef

### userAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWebExperienceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebExperienceResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceArn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_AUTH_CONFIG']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: <class 'str'>
- **Required**: Yes

### welcomeMessage
- **Type**: <class 'str'>
- **Required**: Yes

### samplePromptsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### origins
- **Type**: typing.List[str]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.IdentityProviderConfigurationTypeDef'>
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.WebExperienceAuthConfigurationTypeDef'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef'>
- **Required**: Yes

### browserExtensionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.BrowserExtensionConfigurationOutputTypeDef'>
- **Required**: Yes

### customizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.CustomizationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupMembersTypeDef

### memberGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.MemberGroupTypeDef]]

### memberUsers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.MemberUserTypeDef]]

### s3PathForGroupMembers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.S3TypeDef]


# GroupStatusDetailTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'FAILED', 'PROCESSING', 'SUCCEEDED']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### errorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]


# GroupSummaryTypeDef

### groupName
- **Type**: typing.Optional[str]


# HookConfigurationOutputTypeDef

### invocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionOutputTypeDef]

### lambdaArn
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# HookConfigurationTypeDef

### invocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionUnionTypeDef]

### lambdaArn
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# HookConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdcAuthConfigurationTypeDef

### idcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IdentityProviderConfigurationTypeDef

### samlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SamlProviderConfigurationTypeDef]

### openIDConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OpenIDConnectProviderConfigurationTypeDef]


# ImageExtractionConfigurationTypeDef

### imageExtractionStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ImageSourceDetailsTypeDef

### mediaId
- **Type**: typing.Optional[str]

### mediaMimeType
- **Type**: typing.Optional[str]


# IndexCapacityConfigurationTypeDef

### units
- **Type**: typing.Optional[int]


# IndexStatisticsTypeDef

### textDocumentStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TextDocumentStatisticsTypeDef]


# IndexTypeDef

### displayName
- **Type**: typing.Optional[str]

### indexId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# InlineDocumentEnrichmentConfigurationOutputTypeDef

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionOutputTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTargetOutputTypeDef]

### documentContentOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# InlineDocumentEnrichmentConfigurationTypeDef

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionUnionTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTargetUnionTypeDef]

### documentContentOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# InlineDocumentEnrichmentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KendraIndexConfigurationTypeDef

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# ListApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ApplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttachmentsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListAttachmentsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttachmentsResponseTypeDef

### attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConversationsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListConversationsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConversationsResponseTypeDef

### conversations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ConversationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataAccessorsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListDataAccessorsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataAccessorsResponseTypeDef

### dataAccessors
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataAccessorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourceSyncJobsRequestPaginateTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListDataSourceSyncJobsRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]


# ListDataSourceSyncJobsResponseTypeDef

### history
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceSyncJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataSourcesResponseTypeDef

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDocumentsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListDocumentsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDocumentsResponseTypeDef

### documentDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedEarlierThan
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedEarlierThan
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGroupsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.GroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIndicesRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListIndicesRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIndicesResponseTypeDef

### indices
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.IndexTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessagesRequestPaginateTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListMessagesRequestTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMessagesResponseTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.MessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginActionsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListPluginActionsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginActionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginTypeActionsRequestPaginateTypeDef

### pluginType
- **Type**: typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListPluginTypeActionsRequestTypeDef

### pluginType
- **Type**: typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginTypeActionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginTypeMetadataRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListPluginTypeMetadataRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginTypeMetadataResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.PluginTypeMetadataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListPluginsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginsResponseTypeDef

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.PluginTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRetrieversRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListRetrieversRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRetrieversResponseTypeDef

### retrievers
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListSubscriptionsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSubscriptionsResponseTypeDef

### subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWebExperiencesRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListWebExperiencesRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWebExperiencesResponseTypeDef

### webExperiences
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.WebExperienceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MediaExtractionConfigurationTypeDef

### imageExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ImageExtractionConfigurationTypeDef]

### audioExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AudioExtractionConfigurationTypeDef]

### videoExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.VideoExtractionConfigurationTypeDef]


# MemberGroupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MemberUserTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageUsefulnessFeedbackTypeDef

### usefulness
- **Type**: typing.Literal['NOT_USEFUL', 'USEFUL']
- **Required**: Yes

### submittedAt
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FACTUALLY_CORRECT', 'HARMFUL_OR_UNSAFE', 'HELPFUL', 'INCORRECT_OR_MISSING_SOURCES', 'NOT_BASED_ON_DOCUMENTS', 'NOT_COMPLETE', 'NOT_CONCISE', 'NOT_FACTUALLY_CORRECT', 'NOT_HELPFUL', 'OTHER', 'RELEVANT_SOURCES']]

### comment
- **Type**: typing.Optional[str]


# MetadataEventTypeDef

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### sourceAttributions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.SourceAttributionTypeDef]]

### finalTextMessage
- **Type**: typing.Optional[str]


# NativeIndexConfigurationOutputTypeDef

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### boostingOverride
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeBoostingConfigurationOutputTypeDef]]


# NativeIndexConfigurationTypeDef

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### boostingOverride
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeBoostingConfigurationTypeDef]]


# NumberAttributeBoostingConfigurationTypeDef

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### boostingType
- **Type**: typing.Optional[typing.Literal['PRIORITIZE_LARGER_VALUES', 'PRIORITIZE_SMALLER_VALUES']]


# OAuth2ClientCredentialConfigurationTypeDef

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### authorizationUrl
- **Type**: typing.Optional[str]

### tokenUrl
- **Type**: typing.Optional[str]


# OpenIDConnectProviderConfigurationTypeDef

### secretsArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretsRole
- **Type**: <class 'str'>
- **Required**: Yes


# OrchestrationConfigurationTypeDef

### control
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PersonalizationConfigurationTypeDef

### personalizationControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# PluginAuthConfigurationOutputTypeDef

### basicAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BasicAuthConfigurationTypeDef]

### oAuth2ClientCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OAuth2ClientCredentialConfigurationTypeDef]

### noAuthConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### idcAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdcAuthConfigurationTypeDef]


# PluginAuthConfigurationTypeDef

### basicAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BasicAuthConfigurationTypeDef]

### oAuth2ClientCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OAuth2ClientCredentialConfigurationTypeDef]

### noAuthConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### idcAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdcAuthConfigurationTypeDef]


# PluginAuthConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PluginConfigurationTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# PluginTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PluginTypeMetadataSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrincipalGroupTypeDef

### access
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### membershipType
- **Type**: typing.Optional[typing.Literal['DATASOURCE', 'INDEX']]


# PrincipalTypeDef

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PrincipalUserTypeDef]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PrincipalGroupTypeDef]


# PrincipalUserTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutFeedbackRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### messageCopiedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TimestampTypeDef]

### messageUsefulness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MessageUsefulnessFeedbackTypeDef]


# QAppsConfigurationTypeDef

### qAppsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# QuickSightConfigurationTypeDef

### clientNamespace
- **Type**: <class 'str'>
- **Required**: Yes


# RelevantContentTypeDef

### content
- **Type**: typing.Optional[str]

### documentId
- **Type**: typing.Optional[str]

### documentTitle
- **Type**: typing.Optional[str]

### documentUri
- **Type**: typing.Optional[str]

### documentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutputTypeDef]]

### scoreAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ScoreAttributesTypeDef]


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


# RetrieverConfigurationOutputTypeDef

### nativeIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NativeIndexConfigurationOutputTypeDef]

### kendraIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.KendraIndexConfigurationTypeDef]


# RetrieverConfigurationTypeDef

### nativeIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NativeIndexConfigurationTypeDef]

### kendraIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.KendraIndexConfigurationTypeDef]


# RetrieverConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrieverContentSourceTypeDef

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieverTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleConfigurationOutputTypeDef

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRuleTypeDef]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleOutputTypeDef]


# RuleConfigurationTypeDef

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRuleTypeDef]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleUnionTypeDef]


# RuleConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleOutputTypeDef

### ruleType
- **Type**: typing.Literal['CONTENT_BLOCKER_RULE', 'CONTENT_RETRIEVAL_RULE']
- **Required**: Yes

### includedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsOutputTypeDef]

### excludedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsOutputTypeDef]

### ruleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RuleConfigurationOutputTypeDef]


# RuleTypeDef

### ruleType
- **Type**: typing.Literal['CONTENT_BLOCKER_RULE', 'CONTENT_RETRIEVAL_RULE']
- **Required**: Yes

### includedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsUnionTypeDef]

### excludedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsUnionTypeDef]

### ruleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RuleConfigurationUnionTypeDef]


# RuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3TypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SamlConfigurationTypeDef

### metadataXML
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### userIdAttribute
- **Type**: <class 'str'>
- **Required**: Yes

### userGroupAttribute
- **Type**: typing.Optional[str]


# SamlProviderConfigurationTypeDef

### authenticationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ScoreAttributesTypeDef

### scoreConfidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NOT_AVAILABLE', 'VERY_HIGH']]


# SearchRelevantContentRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### contentSource
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ContentSourceTypeDef'>
- **Required**: Yes

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# SearchRelevantContentRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### contentSource
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ContentSourceTypeDef'>
- **Required**: Yes

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnionTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchRelevantContentResponseTypeDef

### relevantContent
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.RelevantContentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SnippetExcerptTypeDef

### text
- **Type**: typing.Optional[str]


# SourceAttributionTypeDef

### title
- **Type**: typing.Optional[str]

### snippet
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### citationNumber
- **Type**: typing.Optional[int]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### textMessageSegments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.TextSegmentTypeDef]]


# SourceDetailsTypeDef

### imageSourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ImageSourceDetailsTypeDef]

### audioSourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AudioSourceDetailsTypeDef]

### videoSourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.VideoSourceDetailsTypeDef]


# StartDataSourceSyncJobRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataSourceSyncJobResponseTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDataSourceSyncJobRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# StringAttributeBoostingConfigurationOutputTypeDef

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### attributeValueBoosting
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['HIGH', 'LOW', 'MEDIUM', 'VERY_HIGH']]]


# StringAttributeBoostingConfigurationTypeDef

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### attributeValueBoosting
- **Type**: typing.Optional[typing.Mapping[str, typing.Literal['HIGH', 'LOW', 'MEDIUM', 'VERY_HIGH']]]


# StringListAttributeBoostingConfigurationTypeDef

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes


# SubscriptionDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionPrincipalTypeDef

### user
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]


# SubscriptionTypeDef

### subscriptionId
- **Type**: typing.Optional[str]

### subscriptionArn
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionPrincipalTypeDef]

### currentSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef]

### nextSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef]


# TagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TextDocumentStatisticsTypeDef

### indexedTextBytes
- **Type**: typing.Optional[int]

### indexedTextDocumentCount
- **Type**: typing.Optional[int]


# TextInputEventTypeDef

### userMessage
- **Type**: <class 'str'>
- **Required**: Yes


# TextOutputEventTypeDef

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### systemMessage
- **Type**: typing.Optional[str]


# TextSegmentTypeDef

### beginOffset
- **Type**: typing.Optional[int]

### endOffset
- **Type**: typing.Optional[int]

### snippetExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SnippetExcerptTypeDef]

### mediaId
- **Type**: typing.Optional[str]

### mediaMimeType
- **Type**: typing.Optional[str]

### sourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SourceDetailsTypeDef]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicConfigurationOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.RuleOutputTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### exampleChatMessages
- **Type**: typing.Optional[typing.List[str]]


# TopicConfigurationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.RuleUnionTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### exampleChatMessages
- **Type**: typing.Optional[typing.Sequence[str]]


# TopicConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### attachmentsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentsConfigurationTypeDef]

### qAppsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QAppsConfigurationTypeDef]

### personalizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PersonalizationConfigurationTypeDef]

### autoSubscriptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AutoSubscriptionConfigurationTypeDef]


# UpdateChatControlsConfigurationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### responseScope
- **Type**: typing.Optional[typing.Literal['ENTERPRISE_CONTENT_ONLY', 'EXTENDED_KNOWLEDGE_ENABLED']]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OrchestrationConfigurationTypeDef]

### blockedPhrasesConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BlockedPhrasesConfigurationUpdateTypeDef]

### topicConfigurationsToCreateOrUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationUnionTypeDef]]

### topicConfigurationsToDelete
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationUnionTypeDef]]

### creatorModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CreatorModeConfigurationTypeDef]


# UpdateDataAccessorRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes

### actionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.ActionConfigurationUnionTypeDef]
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]


# UpdateDataSourceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### syncSchedule
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### documentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationUnionTypeDef]

### mediaExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MediaExtractionConfigurationTypeDef]


# UpdateIndexRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### capacityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IndexCapacityConfigurationTypeDef]

### documentAttributeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConfigurationTypeDef]]


# UpdatePluginRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### serverUrl
- **Type**: typing.Optional[str]

### customPluginConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomPluginConfigurationTypeDef]

### authConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PluginAuthConfigurationUnionTypeDef]


# UpdateRetrieverRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverConfigurationUnionTypeDef]

### displayName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateSubscriptionResponseTypeDef

### subscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef'>
- **Required**: Yes

### nextSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### userAliasesToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]]

### userAliasesToDelete
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]]


# UpdateUserResponseTypeDef

### userAliasesAdded
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]
- **Required**: Yes

### userAliasesUpdated
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]
- **Required**: Yes

### userAliasesDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWebExperienceRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.WebExperienceAuthConfigurationTypeDef]

### title
- **Type**: typing.Optional[str]

### subtitle
- **Type**: typing.Optional[str]

### welcomeMessage
- **Type**: typing.Optional[str]

### samplePromptsControlMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### identityProviderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdentityProviderConfigurationTypeDef]

### origins
- **Type**: typing.Optional[typing.Sequence[str]]

### browserExtensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BrowserExtensionConfigurationUnionTypeDef]

### customizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomizationConfigurationTypeDef]


# UserAliasTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: typing.Optional[str]

### dataSourceId
- **Type**: typing.Optional[str]


# UsersAndGroupsOutputTypeDef

### userIds
- **Type**: typing.Optional[typing.List[str]]

### userGroups
- **Type**: typing.Optional[typing.List[str]]


# UsersAndGroupsTypeDef

### userIds
- **Type**: typing.Optional[typing.Sequence[str]]

### userGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# UsersAndGroupsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VideoExtractionConfigurationTypeDef

### videoExtractionStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# VideoSourceDetailsTypeDef

### mediaId
- **Type**: typing.Optional[str]

### mediaMimeType
- **Type**: typing.Optional[str]

### startTimeMilliseconds
- **Type**: typing.Optional[int]

### endTimeMilliseconds
- **Type**: typing.Optional[int]

### videoExtractionType
- **Type**: typing.Optional[typing.Literal['SUMMARY', 'TRANSCRIPT']]


# WebExperienceAuthConfigurationTypeDef

### samlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SamlConfigurationTypeDef]


# WebExperienceTypeDef

### webExperienceId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### defaultEndpoint
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_AUTH_CONFIG']]


