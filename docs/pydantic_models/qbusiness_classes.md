# Qbusiness Classes

# APISchema

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.S3]


# AccessConfiguration

### accessControls
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.AccessControl]
- **Required**: Yes

### memberRelation
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# AccessControl

### principals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Principal]
- **Required**: Yes

### memberRelation
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# ActionConfiguration

### action
- **Type**: <class 'str'>
- **Required**: Yes

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionFilterConfigurationUnion]


# ActionConfigurationOutput

### action
- **Type**: <class 'str'>
- **Required**: Yes

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionFilterConfigurationOutput]


# ActionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionExecution

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadField]
- **Required**: Yes

### payloadFieldNameSeparator
- **Type**: <class 'str'>
- **Required**: Yes


# ActionExecutionEvent

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadFieldUnion]
- **Required**: Yes

### payloadFieldNameSeparator
- **Type**: <class 'str'>
- **Required**: Yes


# ActionExecutionOutput

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadFieldOutput]
- **Required**: Yes

### payloadFieldNameSeparator
- **Type**: <class 'str'>
- **Required**: Yes


# ActionExecutionPayloadField

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# ActionExecutionPayloadFieldOutput

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ActionExecutionPayloadFieldUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionExecutionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionFilterConfiguration

### documentAttributeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnion'>
- **Required**: Yes


# ActionFilterConfigurationOutput

### documentAttributeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterOutput'>
- **Required**: Yes


# ActionFilterConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionReview

### pluginId
- **Type**: typing.Optional[str]

### pluginType
- **Type**: typing.Optional[typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']]

### payload
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewPayloadField]]

### payloadFieldNameSeparator
- **Type**: typing.Optional[str]


# ActionReviewEvent

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewPayloadField]]

### payloadFieldNameSeparator
- **Type**: typing.Optional[str]


# ActionReviewPayloadField

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionReviewPayloadFieldAllowedValue

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### displayValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ActionSummary

### actionIdentifier
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### instructionExample
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# Application

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QuickSightConfiguration]


# AppliedAttachmentsConfiguration

### attachmentsControlMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AppliedCreatorModeConfiguration

### creatorModeControl
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AppliedOrchestrationConfiguration

### control
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AssociatePermissionRequest

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


# AssociatePermissionResponse

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# Attachment

### attachmentId
- **Type**: typing.Optional[str]

### conversationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### copyFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CopyFromSource]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail]


# AttachmentInput

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Blob]

### name
- **Type**: typing.Optional[str]

### copyFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CopyFromSource]


# AttachmentInputEvent

### attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentInput]


# AttachmentOutput

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCESS']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail]

### attachmentId
- **Type**: typing.Optional[str]

### conversationId
- **Type**: typing.Optional[str]


# AttachmentsConfiguration

### attachmentsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AttributeFilter

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]


# AttributeFilterOutput

### andAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]


# AttributeFilterPaginator

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeUnion]


# AttributeFilterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioExtractionConfiguration

### audioExtractionStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AudioSourceDetails

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


# AuthChallengeRequest

### authorizationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# AuthChallengeRequestEvent

### authorizationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# AuthChallengeResponse

### responseMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# AuthChallengeResponseEvent

### responseMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# AutoSubscriptionConfiguration

### autoSubscribe
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### defaultSubscriptionType
- **Type**: typing.Optional[typing.Literal['Q_BUSINESS', 'Q_LITE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthConfiguration

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteDocumentRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.DeleteDocument]
- **Required**: Yes

### dataSourceSyncId
- **Type**: typing.Optional[str]


# BatchDeleteDocumentResponse

### failedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.FailedDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutDocumentRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Document]
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### dataSourceSyncId
- **Type**: typing.Optional[str]


# BatchPutDocumentResponse

### failedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.FailedDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockedPhrasesConfiguration

### blockedPhrases
- **Type**: typing.Optional[typing.List[str]]

### systemMessageOverride
- **Type**: typing.Optional[str]


# BlockedPhrasesConfigurationUpdate

### blockedPhrasesToCreateOrUpdate
- **Type**: typing.Optional[typing.Sequence[str]]

### blockedPhrasesToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### systemMessageOverride
- **Type**: typing.Optional[str]


# BrowserExtensionConfiguration

### enabledBrowserExtensions
- **Type**: typing.Sequence[typing.Literal['CHROME', 'FIREFOX']]
- **Required**: Yes


# BrowserExtensionConfigurationOutput

### enabledBrowserExtensions
- **Type**: typing.List[typing.Literal['CHROME', 'FIREFOX']]
- **Required**: Yes


# BrowserExtensionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSubscriptionRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSubscriptionResponse

### subscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails'>
- **Required**: Yes

### nextSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# ChatInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.qbusiness_classes.ChatInputStream]]


# ChatInputStream

### configurationEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ConfigurationEvent]

### textEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TextInputEvent]

### attachmentEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentInputEvent]

### actionExecutionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionEvent]

### endOfInputEvent
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### authChallengeResponseEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeResponseEvent]


# ChatModeConfiguration

### pluginConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PluginConfiguration]


# ChatOutput

### outputStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.qbusiness_classes.ChatOutputStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# ChatOutputStream

### textEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TextOutputEvent]

### metadataEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MetadataEvent]

### actionReviewEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewEvent]

### failedAttachmentEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.FailedAttachmentEvent]

### authChallengeRequestEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeRequestEvent]


# ChatSyncInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentInput]]

### actionExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionUnion]

### authChallengeResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeResponse]

### conversationId
- **Type**: typing.Optional[str]

### parentMessageId
- **Type**: typing.Optional[str]

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnion]

### chatMode
- **Type**: typing.Optional[typing.Literal['CREATOR_MODE', 'PLUGIN_MODE', 'RETRIEVAL_MODE']]

### chatModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ChatModeConfiguration]

### clientToken
- **Type**: typing.Optional[str]


# ChatSyncOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ActionReview'>
- **Required**: Yes

### authChallengeRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeRequest'>
- **Required**: Yes

### sourceAttributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.SourceAttribution]
- **Required**: Yes

### failedAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationEvent

### chatMode
- **Type**: typing.Optional[typing.Literal['CREATOR_MODE', 'PLUGIN_MODE', 'RETRIEVAL_MODE']]

### chatModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ChatModeConfiguration]

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnion]


# ContentBlockerRule

### systemMessageOverride
- **Type**: typing.Optional[str]


# ContentRetrievalRule

### eligibleDataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSource]]


# ContentRetrievalRuleOutput

### eligibleDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSource]]


# ContentRetrievalRuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContentSource

### retriever
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverContentSource]


# Conversation

### conversationId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]


# ConversationSource

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# CopyFromSource

### conversation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ConversationSource]


# CreateApplicationRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.EncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Tag]]

### clientToken
- **Type**: typing.Optional[str]

### attachmentsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentsConfiguration]

### qAppsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QAppsConfiguration]

### personalizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PersonalizationConfiguration]

### quickSightConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QuickSightConfiguration]


# CreateApplicationResponse

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataAccessorRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### actionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.ActionConfigurationUnion]
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Tag]]


# CreateDataAccessorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationUnion]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Tag]]

### syncSchedule
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### documentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationUnion]

### mediaExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MediaExtractionConfiguration]


# CreateDataSourceResponse

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIndexResponse

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### indexArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePluginResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRetrieverResponse

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriptionResponse

### subscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails'>
- **Required**: Yes

### nextSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### userAliases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]]

### clientToken
- **Type**: typing.Optional[str]


# CreateWebExperienceRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Tag]]

### clientToken
- **Type**: typing.Optional[str]

### identityProviderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdentityProviderConfiguration]

### browserExtensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BrowserExtensionConfigurationUnion]

### customizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomizationConfiguration]


# CreateWebExperienceResponse

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreatorModeConfiguration

### creatorModeControl
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# CustomPluginConfiguration

### description
- **Type**: <class 'str'>
- **Required**: Yes

### apiSchemaType
- **Type**: typing.Literal['OPEN_API_V3']
- **Required**: Yes

### apiSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.APISchema'>
- **Required**: Yes


# CustomizationConfiguration

### customCSSUrl
- **Type**: typing.Optional[str]

### logoUrl
- **Type**: typing.Optional[str]

### fontUrl
- **Type**: typing.Optional[str]

### faviconUrl
- **Type**: typing.Optional[str]


# DataAccessor

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


# DataSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceSyncJob

### executionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail]

### dataSourceErrorCode
- **Type**: typing.Optional[str]

### metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceSyncJobMetrics]


# DataSourceSyncJobMetrics

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


# DataSourceVpcConfiguration

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DataSourceVpcConfigurationOutput

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# DataSourceVpcConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateAttributeBoostingConfiguration

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### boostingDurationInSeconds
- **Type**: typing.Optional[int]


# DeleteApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttachmentRequest

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


# DeleteChatControlsConfigurationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConversationRequest

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# DeleteDataAccessorRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocument

### documentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequest

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


# DeleteIndexRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePluginRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetrieverRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebExperienceRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePermissionRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes


# Document

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttribute

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueUnion'>
- **Required**: Yes


# DocumentAttributeBoostingConfiguration

### numberConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NumberAttributeBoostingConfiguration]

### stringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringAttributeBoostingConfiguration]

### dateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DateAttributeBoostingConfiguration]

### stringListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringListAttributeBoostingConfiguration]


# DocumentAttributeBoostingConfigurationOutput

### numberConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NumberAttributeBoostingConfiguration]

### stringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringAttributeBoostingConfigurationOutput]

### dateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DateAttributeBoostingConfiguration]

### stringListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.StringListAttributeBoostingConfiguration]


# DocumentAttributeConditionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeConditionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueOutput'>
- **Required**: Yes


# DocumentAttributeTarget

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueUnion]

### attributeValueOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# DocumentAttributeTargetOutput

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueOutput]

### attributeValueOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# DocumentAttributeTargetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeValue

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.Sequence[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp]


# DocumentAttributeValueOutput

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.List[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[datetime.datetime]


# DocumentAttributeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentContent

### blob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Blob]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.S3]


# DocumentDetails

### documentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'DOCUMENT_FAILED_TO_INDEX', 'FAILED', 'INDEXED', 'PROCESSING', 'RECEIVED', 'UPDATED']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DocumentEnrichmentConfiguration

### inlineConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.InlineDocumentEnrichmentConfigurationUnion]]

### preExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationUnion]

### postExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationUnion]


# DocumentEnrichmentConfigurationOutput

### inlineConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.InlineDocumentEnrichmentConfigurationOutput]]

### preExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationOutput]

### postExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationOutput]


# DocumentEnrichmentConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EligibleDataSource

### indexId
- **Type**: typing.Optional[str]

### dataSourceId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfiguration

### kmsKeyId
- **Type**: typing.Optional[str]


# ErrorDetail

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest', 'ResourceInactive', 'ResourceNotFound']]


# FailedAttachmentEvent

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentOutput]


# FailedDocument

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.EncryptionConfiguration'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail'>
- **Required**: Yes

### attachmentsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedAttachmentsConfiguration'>
- **Required**: Yes

### qAppsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.QAppsConfiguration'>
- **Required**: Yes

### personalizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.PersonalizationConfiguration'>
- **Required**: Yes

### autoSubscriptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AutoSubscriptionConfiguration'>
- **Required**: Yes

### clientIdsForOIDC
- **Type**: typing.List[str]
- **Required**: Yes

### quickSightConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.QuickSightConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetChatControlsConfigurationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetChatControlsConfigurationRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# GetChatControlsConfigurationResponse

### responseScope
- **Type**: typing.Literal['ENTERPRISE_CONTENT_ONLY', 'EXTENDED_KNOWLEDGE_ENABLED']
- **Required**: Yes

### orchestrationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedOrchestrationConfiguration'>
- **Required**: Yes

### blockedPhrases
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.BlockedPhrasesConfiguration'>
- **Required**: Yes

### topicConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationOutput]
- **Required**: Yes

### creatorModeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedCreatorModeConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetDataAccessorRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataAccessorResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionConfigurationOutput]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupRequest

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


# GetGroupResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.GroupStatusDetail'>
- **Required**: Yes

### statusHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.GroupStatusDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetIndexRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaRequest

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


# GetMediaResponse

### mediaBytes
- **Type**: <class 'bytes'>
- **Required**: Yes

### mediaMimeType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetPluginRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponse

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetRetrieverRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponse

### userAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetWebExperienceRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebExperienceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.IdentityProviderConfiguration'>
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.WebExperienceAuthConfiguration'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail'>
- **Required**: Yes

### browserExtensionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.BrowserExtensionConfigurationOutput'>
- **Required**: Yes

### customizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.CustomizationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# GroupMembers

### memberGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.MemberGroup]]

### memberUsers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.MemberUser]]

### s3PathForGroupMembers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.S3]


# GroupStatusDetail

### status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'FAILED', 'PROCESSING', 'SUCCEEDED']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### errorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetail]


# GroupSummary

### groupName
- **Type**: typing.Optional[str]


# HookConfiguration

### invocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionUnion]

### lambdaArn
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# HookConfigurationOutput

### invocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionOutput]

### lambdaArn
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# HookConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdcAuthConfiguration

### idcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IdentityProviderConfiguration

### samlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SamlProviderConfiguration]

### openIDConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OpenIDConnectProviderConfiguration]


# ImageExtractionConfiguration

### imageExtractionStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ImageSourceDetails

### mediaId
- **Type**: typing.Optional[str]

### mediaMimeType
- **Type**: typing.Optional[str]


# Index

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


# IndexCapacityConfiguration

### units
- **Type**: typing.Optional[int]


# IndexStatistics

### textDocumentStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.TextDocumentStatistics]


# InlineDocumentEnrichmentConfiguration

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionUnion]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTargetUnion]

### documentContentOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# InlineDocumentEnrichmentConfigurationOutput

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionOutput]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTargetOutput]

### documentContentOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# InlineDocumentEnrichmentConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KendraIndexConfiguration

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# ListApplicationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListApplicationsResponse

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Application]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttachmentsRequest

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


# ListAttachmentsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListAttachmentsResponse

### attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Attachment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConversationsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConversationsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListConversationsResponse

### conversations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Conversation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataAccessorsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataAccessorsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListDataAccessorsResponse

### dataAccessors
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataAccessor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourceSyncJobsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]


# ListDataSourceSyncJobsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListDataSourceSyncJobsResponse

### history
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceSyncJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequest

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


# ListDataSourcesRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListDataSourcesResponse

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDocumentsRequest

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


# ListDocumentsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListDocumentsResponse

### documentDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedEarlierThan
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGroupsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedEarlierThan
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListGroupsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.GroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIndicesRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIndicesRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListIndicesResponse

### indices
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Index]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessagesRequest

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


# ListMessagesRequestPaginate

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListMessagesResponse

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Message]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginActionsRequest

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


# ListPluginActionsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListPluginActionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginTypeActionsRequest

### pluginType
- **Type**: typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginTypeActionsRequestPaginate

### pluginType
- **Type**: typing.Literal['ASANA', 'ATLASSIAN_CONFLUENCE', 'CUSTOM', 'GOOGLE_CALENDAR', 'JIRA', 'JIRA_CLOUD', 'MICROSOFT_EXCHANGE', 'MICROSOFT_TEAMS', 'PAGERDUTY_ADVANCE', 'QUICKSIGHT', 'SALESFORCE', 'SALESFORCE_CRM', 'SERVICENOW_NOW_PLATFORM', 'SERVICE_NOW', 'SMARTSHEET', 'ZENDESK', 'ZENDESK_SUITE']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListPluginTypeActionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginTypeMetadataRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginTypeMetadataRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListPluginTypeMetadataResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.PluginTypeMetadataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListPluginsResponse

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Plugin]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRetrieversRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRetrieversRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListRetrieversResponse

### retrievers
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Retriever]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSubscriptionsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListSubscriptionsResponse

### subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Subscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# ListWebExperiencesRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWebExperiencesRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# ListWebExperiencesResponse

### webExperiences
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.WebExperience]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MediaExtractionConfiguration

### imageExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ImageExtractionConfiguration]

### audioExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AudioExtractionConfiguration]

### videoExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.VideoExtractionConfiguration]


# MemberGroup

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MemberUser

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Message

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageUsefulnessFeedback

### usefulness
- **Type**: typing.Literal['NOT_USEFUL', 'USEFUL']
- **Required**: Yes

### submittedAt
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FACTUALLY_CORRECT', 'HARMFUL_OR_UNSAFE', 'HELPFUL', 'INCORRECT_OR_MISSING_SOURCES', 'NOT_BASED_ON_DOCUMENTS', 'NOT_COMPLETE', 'NOT_CONCISE', 'NOT_FACTUALLY_CORRECT', 'NOT_HELPFUL', 'OTHER', 'RELEVANT_SOURCES']]

### comment
- **Type**: typing.Optional[str]


# MetadataEvent

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### sourceAttributions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.SourceAttribution]]

### finalTextMessage
- **Type**: typing.Optional[str]


# NativeIndexConfiguration

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### boostingOverride
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeBoostingConfiguration]]


# NativeIndexConfigurationOutput

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### boostingOverride
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeBoostingConfigurationOutput]]


# NumberAttributeBoostingConfiguration

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### boostingType
- **Type**: typing.Optional[typing.Literal['PRIORITIZE_LARGER_VALUES', 'PRIORITIZE_SMALLER_VALUES']]


# OAuth2ClientCredentialConfiguration

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


# OpenIDConnectProviderConfiguration

### secretsArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretsRole
- **Type**: <class 'str'>
- **Required**: Yes


# OrchestrationConfiguration

### control
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PersonalizationConfiguration

### personalizationControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# Plugin

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PluginAuthConfiguration

### basicAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BasicAuthConfiguration]

### oAuth2ClientCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OAuth2ClientCredentialConfiguration]

### noAuthConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### idcAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdcAuthConfiguration]


# PluginAuthConfigurationOutput

### basicAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BasicAuthConfiguration]

### oAuth2ClientCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OAuth2ClientCredentialConfiguration]

### noAuthConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### idcAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdcAuthConfiguration]


# PluginAuthConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PluginConfiguration

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# PluginTypeMetadataSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Principal

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PrincipalUser]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PrincipalGroup]


# PrincipalGroup

### access
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### membershipType
- **Type**: typing.Optional[typing.Literal['DATASOURCE', 'INDEX']]


# PrincipalUser

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutFeedbackRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.Timestamp]

### messageUsefulness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MessageUsefulnessFeedback]


# QAppsConfiguration

### qAppsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# QuickSightConfiguration

### clientNamespace
- **Type**: <class 'str'>
- **Required**: Yes


# RelevantContent

### content
- **Type**: typing.Optional[str]

### documentId
- **Type**: typing.Optional[str]

### documentTitle
- **Type**: typing.Optional[str]

### documentUri
- **Type**: typing.Optional[str]

### documentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeOutput]]

### scoreAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ScoreAttributes]


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


# Retriever

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrieverConfiguration

### nativeIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NativeIndexConfiguration]

### kendraIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.KendraIndexConfiguration]


# RetrieverConfigurationOutput

### nativeIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.NativeIndexConfigurationOutput]

### kendraIndexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.KendraIndexConfiguration]


# RetrieverConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrieverContentSource

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# Rule

### ruleType
- **Type**: typing.Literal['CONTENT_BLOCKER_RULE', 'CONTENT_RETRIEVAL_RULE']
- **Required**: Yes

### includedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsUnion]

### excludedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsUnion]

### ruleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RuleConfigurationUnion]


# RuleConfiguration

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRule]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleUnion]


# RuleConfigurationOutput

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRule]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleOutput]


# RuleConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleOutput

### ruleType
- **Type**: typing.Literal['CONTENT_BLOCKER_RULE', 'CONTENT_RETRIEVAL_RULE']
- **Required**: Yes

### includedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsOutput]

### excludedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsOutput]

### ruleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RuleConfigurationOutput]


# RuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SamlConfiguration

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


# SamlProviderConfiguration

### authenticationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ScoreAttributes

### scoreConfidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NOT_AVAILABLE', 'VERY_HIGH']]


# SearchRelevantContentRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### contentSource
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ContentSource'>
- **Required**: Yes

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterUnion]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchRelevantContentRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### contentSource
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ContentSource'>
- **Required**: Yes

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttributeFilterPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfig]


# SearchRelevantContentResponse

### relevantContent
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.RelevantContent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SnippetExcerpt

### text
- **Type**: typing.Optional[str]


# SourceAttribution

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.TextSegment]]


# SourceDetails

### imageSourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ImageSourceDetails]

### audioSourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AudioSourceDetails]

### videoSourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.VideoSourceDetails]


# StartDataSourceSyncJobRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataSourceSyncJobResponse

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# StopDataSourceSyncJobRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# StringAttributeBoostingConfiguration

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### attributeValueBoosting
- **Type**: typing.Optional[typing.Mapping[str, typing.Literal['HIGH', 'LOW', 'MEDIUM', 'VERY_HIGH']]]


# StringAttributeBoostingConfigurationOutput

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### attributeValueBoosting
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['HIGH', 'LOW', 'MEDIUM', 'VERY_HIGH']]]


# StringListAttributeBoostingConfiguration

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes


# Subscription

### subscriptionId
- **Type**: typing.Optional[str]

### subscriptionArn
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionPrincipal]

### currentSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails]

### nextSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails]


# SubscriptionDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubscriptionPrincipal

### user
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.Tag]
- **Required**: Yes


# TextDocumentStatistics

### indexedTextBytes
- **Type**: typing.Optional[int]

### indexedTextDocumentCount
- **Type**: typing.Optional[int]


# TextInputEvent

### userMessage
- **Type**: <class 'str'>
- **Required**: Yes


# TextOutputEvent

### conversationId
- **Type**: typing.Optional[str]

### userMessageId
- **Type**: typing.Optional[str]

### systemMessageId
- **Type**: typing.Optional[str]

### systemMessage
- **Type**: typing.Optional[str]


# TextSegment

### beginOffset
- **Type**: typing.Optional[int]

### endOffset
- **Type**: typing.Optional[int]

### snippetExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SnippetExcerpt]

### mediaId
- **Type**: typing.Optional[str]

### mediaMimeType
- **Type**: typing.Optional[str]

### sourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SourceDetails]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicConfiguration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.RuleUnion]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### exampleChatMessages
- **Type**: typing.Optional[typing.Sequence[str]]


# TopicConfigurationOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.RuleOutput]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### exampleChatMessages
- **Type**: typing.Optional[typing.List[str]]


# TopicConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentsConfiguration]

### qAppsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.QAppsConfiguration]

### personalizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PersonalizationConfiguration]

### autoSubscriptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AutoSubscriptionConfiguration]


# UpdateChatControlsConfigurationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### responseScope
- **Type**: typing.Optional[typing.Literal['ENTERPRISE_CONTENT_ONLY', 'EXTENDED_KNOWLEDGE_ENABLED']]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OrchestrationConfiguration]

### blockedPhrasesConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BlockedPhrasesConfigurationUpdate]

### topicConfigurationsToCreateOrUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationUnion]]

### topicConfigurationsToDelete
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationUnion]]

### creatorModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CreatorModeConfiguration]


# UpdateDataAccessorRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessorId
- **Type**: <class 'str'>
- **Required**: Yes

### actionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.ActionConfigurationUnion]
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]


# UpdateDataSourceRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationUnion]

### description
- **Type**: typing.Optional[str]

### syncSchedule
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### documentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationUnion]

### mediaExtractionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MediaExtractionConfiguration]


# UpdateIndexRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IndexCapacityConfiguration]

### documentAttributeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConfiguration]]


# UpdatePluginRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomPluginConfiguration]

### authConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PluginAuthConfigurationUnion]


# UpdateRetrieverRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverConfigurationUnion]

### displayName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateSubscriptionResponse

### subscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails'>
- **Required**: Yes

### nextSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.SubscriptionDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### userAliasesToUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]]

### userAliasesToDelete
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]]


# UpdateUserResponse

### userAliasesAdded
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]
- **Required**: Yes

### userAliasesUpdated
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]
- **Required**: Yes

### userAliasesDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.UserAlias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebExperienceRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### authenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.WebExperienceAuthConfiguration]

### title
- **Type**: typing.Optional[str]

### subtitle
- **Type**: typing.Optional[str]

### welcomeMessage
- **Type**: typing.Optional[str]

### samplePromptsControlMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### identityProviderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IdentityProviderConfiguration]

### origins
- **Type**: typing.Optional[typing.Sequence[str]]

### browserExtensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BrowserExtensionConfigurationUnion]

### customizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomizationConfiguration]


# UserAlias

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: typing.Optional[str]

### dataSourceId
- **Type**: typing.Optional[str]


# UsersAndGroups

### userIds
- **Type**: typing.Optional[typing.Sequence[str]]

### userGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# UsersAndGroupsOutput

### userIds
- **Type**: typing.Optional[typing.List[str]]

### userGroups
- **Type**: typing.Optional[typing.List[str]]


# UsersAndGroupsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VideoExtractionConfiguration

### videoExtractionStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# VideoSourceDetails

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


# WebExperience

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


# WebExperienceAuthConfiguration

### samlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SamlConfiguration]


