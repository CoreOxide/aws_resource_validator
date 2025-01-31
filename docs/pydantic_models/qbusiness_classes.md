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


# ActionExecutionExtraOutputTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionPayloadFieldExtraOutputTypeDef]
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


# ActionExecutionPayloadFieldExtraOutputTypeDef

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ActionExecutionPayloadFieldOutputTypeDef

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ActionExecutionPayloadFieldTypeDef

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


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


# ActionReviewPayloadFieldAllowedValueTypeDef

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### displayValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ActionReviewPayloadFieldTypeDef

### displayName
- **Type**: typing.Optional[str]

### displayOrder
- **Type**: typing.Optional[int]

### displayDescription
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ARRAY', 'BOOLEAN', 'NUMBER', 'STRING']]

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### allowedValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewPayloadFieldAllowedValueTypeDef]]

### allowedFormat
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# ActionReviewTypeDef

### pluginId
- **Type**: typing.Optional[str]

### pluginType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'JIRA', 'SALESFORCE', 'SERVICE_NOW', 'ZENDESK']]

### payload
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewPayloadFieldTypeDef]]

### payloadFieldNameSeparator
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


# AppliedAttachmentsConfigurationTypeDef

### attachmentsControlMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AppliedCreatorModeConfigurationTypeDef

### creatorModeControl
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AttachmentInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# AttachmentOutputTypeDef

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]


# AttachmentsConfigurationTypeDef

### attachmentsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# AttributeFilterTypeDef

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]


# AuthChallengeRequestTypeDef

### authorizationUrl
- **Type**: <class 'str'>
- **Required**: Yes


# AuthChallengeResponseTypeDef

### responseMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


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


# BatchDeleteDocumentRequestRequestTypeDef

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


# BatchPutDocumentRequestRequestTypeDef

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


# ChatModeConfigurationTypeDef

### pluginConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PluginConfigurationTypeDef]


# ChatSyncInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionTypeDef]

### authChallengeResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AuthChallengeResponseTypeDef]

### conversationId
- **Type**: typing.Optional[str]

### parentMessageId
- **Type**: typing.Optional[str]

### attributeFilter
- **Type**: typing.Optional[ForwardRef('AttributeFilterTypeDef')]

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


# ContentBlockerRuleTypeDef

### systemMessageOverride
- **Type**: typing.Optional[str]


# ContentRetrievalRuleExtraOutputTypeDef

### eligibleDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSourceTypeDef]]


# ContentRetrievalRuleOutputTypeDef

### eligibleDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSourceTypeDef]]


# ContentRetrievalRuleTypeDef

### eligibleDataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.EligibleDataSourceTypeDef]]


# ConversationTypeDef

### conversationId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]


# CreateApplicationRequestRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### identityCenterInstanceArn
- **Type**: typing.Optional[str]

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


# CreateDataSourceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationTypeDef]


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


# CreateIndexRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'STARTER']]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]

### capacityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.IndexCapacityConfigurationTypeDef]

### clientToken
- **Type**: typing.Optional[str]


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


# CreatePluginRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CUSTOM', 'JIRA', 'SALESFORCE', 'SERVICE_NOW', 'ZENDESK']
- **Required**: Yes

### authConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.PluginAuthConfigurationTypeDef'>
- **Required**: Yes

### serverUrl
- **Type**: typing.Optional[str]

### customPluginConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CustomPluginConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]

### clientToken
- **Type**: typing.Optional[str]


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


# CreateRetrieverRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['KENDRA_INDEX', 'NATIVE_INDEX']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverConfigurationTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]


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


# CreateUserRequestRequestTypeDef

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


# CreateWebExperienceRequestRequestTypeDef

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

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.TagTypeDef]]

### clientToken
- **Type**: typing.Optional[str]


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

### displayName
- **Type**: typing.Optional[str]

### dataSourceId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_CREATION', 'UPDATING']]


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


# DateAttributeBoostingConfigurationTypeDef

### boostingLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH']
- **Required**: Yes

### boostingDurationInSeconds
- **Type**: typing.Optional[int]


# DeleteApplicationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChatControlsConfigurationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConversationRequestRequestTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# DeleteDataSourceRequestRequestTypeDef

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


# DeleteGroupRequestRequestTypeDef

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


# DeleteIndexRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePluginRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetrieverRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebExperienceRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### webExperienceId
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

### key
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'EQUALS', 'EXISTS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS', 'NOT_EXISTS']
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueOutputTypeDef]


# DocumentAttributeConditionTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'EQUALS', 'EXISTS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS', 'NOT_EXISTS']
- **Required**: Yes

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueTypeDef]


# DocumentAttributeConfigurationTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['DATE', 'NUMBER', 'STRING', 'STRING_LIST']]

### search
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueTypeDef]

### attributeValueOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# DocumentAttributeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeValueTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DocumentContentTypeDef

### blob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.InlineDocumentEnrichmentConfigurationTypeDef]]

### preExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationTypeDef]

### postExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.HookConfigurationTypeDef]


# DocumentTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTypeDef]]

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentContentTypeDef]

### contentType
- **Type**: typing.Optional[typing.Literal['CSV', 'HTML', 'JSON', 'MD', 'MS_EXCEL', 'MS_WORD', 'PDF', 'PLAIN_TEXT', 'PPT', 'RTF', 'XML', 'XSLT']]

### title
- **Type**: typing.Optional[str]

### accessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.AccessConfigurationTypeDef]

### documentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationTypeDef]


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


# FailedDocumentTypeDef

### id
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef]

### dataSourceId
- **Type**: typing.Optional[str]


# GetApplicationRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# GetChatControlsConfigurationRequestRequestTypeDef

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

### blockedPhrases
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.BlockedPhrasesConfigurationTypeDef'>
- **Required**: Yes

### topicConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationExtraOutputTypeDef]
- **Required**: Yes

### creatorModeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.AppliedCreatorModeConfigurationTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### vpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationOutputTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_CREATION', 'UPDATING']
- **Required**: Yes

### syncSchedule
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef'>
- **Required**: Yes

### documentEnrichmentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupRequestRequestTypeDef

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


# GetIndexRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIndexResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ENTERPRISE', 'STARTER']
- **Required**: Yes

### indexArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### capacityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.IndexCapacityConfigurationTypeDef'>
- **Required**: Yes

### documentAttributeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConfigurationTypeDef]
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef'>
- **Required**: Yes

### indexStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.IndexStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPluginRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPluginResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CUSTOM', 'JIRA', 'SALESFORCE', 'SERVICE_NOW', 'ZENDESK']
- **Required**: Yes

### serverUrl
- **Type**: <class 'str'>
- **Required**: Yes

### authConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.PluginAuthConfigurationOutputTypeDef'>
- **Required**: Yes

### customPluginConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.CustomPluginConfigurationTypeDef'>
- **Required**: Yes

### buildStatus
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### pluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
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


# GetRetrieverRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRetrieverResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['KENDRA_INDEX', 'NATIVE_INDEX']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'FAILED']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverConfigurationOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
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


# GetUserRequestRequestTypeDef

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


# GetWebExperienceRequestRequestTypeDef

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

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.WebExperienceAuthConfigurationTypeDef'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ErrorDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupMembersTypeDef

### memberGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.MemberGroupTypeDef]]

### memberUsers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.MemberUserTypeDef]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionTypeDef]

### lambdaArn
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### roleArn
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeConditionTypeDef]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentAttributeTargetTypeDef]

### documentContentOperator
- **Type**: typing.Optional[typing.Literal['DELETE']]


# KendraIndexConfigurationTypeDef

### indexId
- **Type**: <class 'str'>
- **Required**: Yes


# ListApplicationsRequestListApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ApplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConversationsRequestListConversationsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListConversationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### conversations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.ConversationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListDataSourceSyncJobsRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]


# ListDataSourceSyncJobsResponseTypeDef

### history
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceSyncJobTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourcesRequestListDataSourcesPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDocumentsRequestListDocumentsPaginateTypeDef

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


# ListDocumentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsRequestListGroupsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedEarlierThan
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListGroupsRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedEarlierThan
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGroupsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.GroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIndicesRequestListIndicesPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListIndicesRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIndicesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### indices
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.IndexTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMessagesRequestListMessagesPaginateTypeDef

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


# ListMessagesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPluginsRequestListPluginsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListPluginsRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPluginsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.PluginTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRetrieversRequestListRetrieversPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListRetrieversRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListWebExperiencesRequestListWebExperiencesPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PaginatorConfigTypeDef]


# ListWebExperiencesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MemberGroupTypeDef

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['DATASOURCE', 'INDEX']]


# MemberUserTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['DATASOURCE', 'INDEX']]


# MessageTypeDef

### messageId
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]

### time
- **Type**: typing.Optional[datetime.datetime]

### type
- **Type**: typing.Optional[typing.Literal['SYSTEM', 'USER']]

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.AttachmentOutputTypeDef]]

### sourceAttribution
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.SourceAttributionTypeDef]]

### actionReview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionReviewTypeDef]

### actionExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ActionExecutionOutputTypeDef]


# MessageUsefulnessFeedbackTypeDef

### usefulness
- **Type**: typing.Literal['NOT_USEFUL', 'USEFUL']
- **Required**: Yes

### submittedAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### reason
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FACTUALLY_CORRECT', 'HARMFUL_OR_UNSAFE', 'HELPFUL', 'INCORRECT_OR_MISSING_SOURCES', 'NOT_BASED_ON_DOCUMENTS', 'NOT_COMPLETE', 'NOT_CONCISE', 'NOT_FACTUALLY_CORRECT', 'NOT_HELPFUL', 'OTHER', 'RELEVANT_SOURCES']]

### comment
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


# PluginAuthConfigurationTypeDef

### basicAuthConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BasicAuthConfigurationTypeDef]

### oAuth2ClientCredentialConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.OAuth2ClientCredentialConfigurationTypeDef]

### noAuthConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# PluginConfigurationTypeDef

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# PluginTypeDef

### pluginId
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'JIRA', 'SALESFORCE', 'SERVICE_NOW', 'ZENDESK']]

### serverUrl
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### buildStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


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

### access
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### membershipType
- **Type**: typing.Optional[typing.Literal['DATASOURCE', 'INDEX']]


# PutFeedbackRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### messageUsefulness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.MessageUsefulnessFeedbackTypeDef]


# PutGroupRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: <class 'str'>
- **Required**: Yes

### groupName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DATASOURCE', 'INDEX']
- **Required**: Yes

### groupMembers
- **Type**: <class 'aws_resource_validator.pydantic_models.qbusiness_classes.GroupMembersTypeDef'>
- **Required**: Yes

### dataSourceId
- **Type**: typing.Optional[str]


# QAppsConfigurationTypeDef

### qAppsControlMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


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


# RetrieverTypeDef

### applicationId
- **Type**: typing.Optional[str]

### retrieverId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['KENDRA_INDEX', 'NATIVE_INDEX']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'FAILED']]

### displayName
- **Type**: typing.Optional[str]


# RuleConfigurationExtraOutputTypeDef

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRuleTypeDef]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleExtraOutputTypeDef]


# RuleConfigurationOutputTypeDef

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRuleTypeDef]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleOutputTypeDef]


# RuleConfigurationTypeDef

### contentBlockerRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentBlockerRuleTypeDef]

### contentRetrievalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.ContentRetrievalRuleTypeDef]


# RuleExtraOutputTypeDef

### ruleType
- **Type**: typing.Literal['CONTENT_BLOCKER_RULE', 'CONTENT_RETRIEVAL_RULE']
- **Required**: Yes

### includedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsExtraOutputTypeDef]

### excludedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsExtraOutputTypeDef]

### ruleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RuleConfigurationExtraOutputTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsTypeDef]

### excludedUsersAndGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.UsersAndGroupsTypeDef]

### ruleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RuleConfigurationTypeDef]


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


# StartDataSourceSyncJobRequestRequestTypeDef

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


# StopDataSourceSyncJobRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# TextSegmentTypeDef

### beginOffset
- **Type**: typing.Optional[int]

### endOffset
- **Type**: typing.Optional[int]

### snippetExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.SnippetExcerptTypeDef]


# TopicConfigurationExtraOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.qbusiness_classes.RuleExtraOutputTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### exampleChatMessages
- **Type**: typing.Optional[typing.List[str]]


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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qbusiness_classes.RuleTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### exampleChatMessages
- **Type**: typing.Optional[typing.Sequence[str]]


# UntagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

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


# UpdateChatControlsConfigurationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### responseScope
- **Type**: typing.Optional[typing.Literal['ENTERPRISE_CONTENT_ONLY', 'EXTENDED_KNOWLEDGE_ENABLED']]

### blockedPhrasesConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.BlockedPhrasesConfigurationUpdateTypeDef]

### topicConfigurationsToCreateOrUpdate
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationTypeDef, aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationExtraOutputTypeDef]]]

### topicConfigurationsToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationTypeDef, aws_resource_validator.pydantic_models.qbusiness_classes.TopicConfigurationExtraOutputTypeDef]]]

### creatorModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.CreatorModeConfigurationTypeDef]


# UpdateDataSourceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DataSourceVpcConfigurationTypeDef]

### description
- **Type**: typing.Optional[str]

### syncSchedule
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### documentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.DocumentEnrichmentConfigurationTypeDef]


# UpdateIndexRequestRequestTypeDef

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


# UpdatePluginRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.PluginAuthConfigurationTypeDef]


# UpdateRetrieverRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### retrieverId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qbusiness_classes.RetrieverConfigurationTypeDef]

### displayName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateUserRequestRequestTypeDef

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


# UpdateWebExperienceRequestRequestTypeDef

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


# UserAliasTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### indexId
- **Type**: typing.Optional[str]

### dataSourceId
- **Type**: typing.Optional[str]


# UsersAndGroupsExtraOutputTypeDef

### userIds
- **Type**: typing.Optional[typing.List[str]]

### userGroups
- **Type**: typing.Optional[typing.List[str]]


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


