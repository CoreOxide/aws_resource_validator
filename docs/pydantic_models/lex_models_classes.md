# Lex Models Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BotAliasMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### botName
- **Type**: typing.Optional[str]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### checksum
- **Type**: typing.Optional[str]

### conversationLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.ConversationLogsResponseTypeDef]


# BotChannelAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BotMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['BUILDING', 'FAILED', 'NOT_BUILT', 'READY', 'READY_BASIC_TESTING']]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### version
- **Type**: typing.Optional[str]


# BuiltinIntentMetadataTypeDef

### signature
- **Type**: typing.Optional[str]

### supportedLocales
- **Type**: typing.Optional[typing.List[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]]


# BuiltinIntentSlotTypeDef

### name
- **Type**: typing.Optional[str]


# BuiltinSlotTypeMetadataTypeDef

### signature
- **Type**: typing.Optional[str]

### supportedLocales
- **Type**: typing.Optional[typing.List[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]]


# CodeHookTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### messageVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ConversationLogsRequestTypeDef

### logSettings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.LogSettingsRequestTypeDef]
- **Required**: Yes

### iamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConversationLogsResponseTypeDef

### logSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models_classes.LogSettingsResponseTypeDef]]

### iamRoleArn
- **Type**: typing.Optional[str]


# CreateBotVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: typing.Optional[str]


# CreateBotVersionResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.IntentTypeDef]
- **Required**: Yes

### clarificationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['BUILDING', 'FAILED', 'NOT_BUILT', 'READY', 'READY_BASIC_TESTING']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### voiceId
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']
- **Required**: Yes

### childDirected
- **Type**: <class 'bool'>
- **Required**: Yes

### enableModelImprovements
- **Type**: <class 'bool'>
- **Required**: Yes

### detectSentiment
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntentVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: typing.Optional[str]


# CreateIntentVersionResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotOutputTypeDef]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptOutputTypeDef'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.CodeHookTypeDef'>
- **Required**: Yes

### fulfillmentActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FulfillmentActivityTypeDef'>
- **Required**: Yes

### parentIntentSignature
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.KendraConfigurationTypeDef'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.InputContextTypeDef]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.OutputContextTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSlotTypeVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: typing.Optional[str]


# CreateSlotTypeVersionResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enumerationValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueOutputTypeDef]
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### valueSelectionStrategy
- **Type**: typing.Literal['ORIGINAL_VALUE', 'TOP_RESOLUTION']
- **Required**: Yes

### parentSlotTypeSignature
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBotAliasRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotChannelAssociationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntentRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntentVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUtterancesRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnumerationValueOutputTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### synonyms
- **Type**: typing.Optional[typing.List[str]]


# EnumerationValueTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### synonyms
- **Type**: typing.Optional[typing.Sequence[str]]


# EnumerationValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FollowUpPromptOutputTypeDef

### prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes


# FollowUpPromptTypeDef

### prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
- **Required**: Yes


# FollowUpPromptUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FulfillmentActivityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetBotAliasRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotAliasResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### conversationLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ConversationLogsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotAliasesRequestPaginateTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotAliasesRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetBotAliasesResponseTypeDef

### BotAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BotAliasMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBotChannelAssociationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotChannelAssociationsRequestPaginateTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotChannelAssociationsRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetBotChannelAssociationsResponseTypeDef

### botChannelAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BotChannelAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBotRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionOrAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.IntentTypeDef]
- **Required**: Yes

### enableModelImprovements
- **Type**: <class 'bool'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### clarificationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['BUILDING', 'FAILED', 'NOT_BUILT', 'READY', 'READY_BASIC_TESTING']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### voiceId
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']
- **Required**: Yes

### childDirected
- **Type**: <class 'bool'>
- **Required**: Yes

### detectSentiment
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotVersionsRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotVersionsRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetBotVersionsResponseTypeDef

### bots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BotMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBotsRequestPaginateTypeDef

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetBotsResponseTypeDef

### bots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BotMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBuiltinIntentRequestTypeDef

### signature
- **Type**: <class 'str'>
- **Required**: Yes


# GetBuiltinIntentResponseTypeDef

### signature
- **Type**: <class 'str'>
- **Required**: Yes

### supportedLocales
- **Type**: typing.List[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BuiltinIntentSlotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBuiltinIntentsRequestPaginateTypeDef

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBuiltinIntentsRequestTypeDef

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetBuiltinIntentsResponseTypeDef

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BuiltinIntentMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBuiltinSlotTypesRequestPaginateTypeDef

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBuiltinSlotTypesRequestTypeDef

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetBuiltinSlotTypesResponseTypeDef

### slotTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.BuiltinSlotTypeMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetExportRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['BOT', 'INTENT', 'SLOT_TYPE']
- **Required**: Yes

### exportType
- **Type**: typing.Literal['ALEXA_SKILLS_KIT', 'LEX']
- **Required**: Yes


# GetExportResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['BOT', 'INTENT', 'SLOT_TYPE']
- **Required**: Yes

### exportType
- **Type**: typing.Literal['ALEXA_SKILLS_KIT', 'LEX']
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'READY']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportRequestTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['BOT', 'INTENT', 'SLOT_TYPE']
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['FAIL_ON_CONFLICT', 'OVERWRITE_LATEST']
- **Required**: Yes

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### importStatus
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### failureReason
- **Type**: typing.List[str]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntentRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntentResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotOutputTypeDef]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptOutputTypeDef'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.CodeHookTypeDef'>
- **Required**: Yes

### fulfillmentActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FulfillmentActivityTypeDef'>
- **Required**: Yes

### parentIntentSignature
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.KendraConfigurationTypeDef'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.InputContextTypeDef]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.OutputContextTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntentVersionsRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetIntentVersionsRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetIntentVersionsResponseTypeDef

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.IntentMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetIntentsRequestPaginateTypeDef

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetIntentsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetIntentsResponseTypeDef

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.IntentMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetMigrationRequestTypeDef

### migrationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationResponseTypeDef

### migrationId
- **Type**: <class 'str'>
- **Required**: Yes

### v1BotName
- **Type**: <class 'str'>
- **Required**: Yes

### v1BotVersion
- **Type**: <class 'str'>
- **Required**: Yes

### v1BotLocale
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']
- **Required**: Yes

### v2BotId
- **Type**: <class 'str'>
- **Required**: Yes

### v2BotRole
- **Type**: <class 'str'>
- **Required**: Yes

### migrationStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### migrationStrategy
- **Type**: typing.Literal['CREATE_NEW', 'UPDATE_EXISTING']
- **Required**: Yes

### migrationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### alerts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.MigrationAlertTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMigrationsRequestTypeDef

### sortByAttribute
- **Type**: typing.Optional[typing.Literal['MIGRATION_DATE_TIME', 'V1_BOT_NAME']]

### sortByOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### v1BotNameContains
- **Type**: typing.Optional[str]

### migrationStatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetMigrationsResponseTypeDef

### migrationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.MigrationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSlotTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# GetSlotTypeResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enumerationValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueOutputTypeDef]
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### valueSelectionStrategy
- **Type**: typing.Literal['ORIGINAL_VALUE', 'TOP_RESOLUTION']
- **Required**: Yes

### parentSlotTypeSignature
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSlotTypeVersionsRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetSlotTypeVersionsRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetSlotTypeVersionsResponseTypeDef

### slotTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSlotTypesRequestPaginateTypeDef

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetSlotTypesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetSlotTypesResponseTypeDef

### slotTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetUtterancesViewRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botVersions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### statusType
- **Type**: typing.Literal['Detected', 'Missed']
- **Required**: Yes


# GetUtterancesViewResponseTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### utterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.UtteranceListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# IntentMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### version
- **Type**: typing.Optional[str]


# IntentTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### intentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# KendraConfigurationTypeDef

### kendraIndex
- **Type**: <class 'str'>
- **Required**: Yes

### role
- **Type**: <class 'str'>
- **Required**: Yes

### queryFilterString
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogSettingsRequestTypeDef

### logType
- **Type**: typing.Literal['AUDIO', 'TEXT']
- **Required**: Yes

### destination
- **Type**: typing.Literal['CLOUDWATCH_LOGS', 'S3']
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# LogSettingsResponseTypeDef

### logType
- **Type**: typing.Optional[typing.Literal['AUDIO', 'TEXT']]

### destination
- **Type**: typing.Optional[typing.Literal['CLOUDWATCH_LOGS', 'S3']]

### kmsKeyArn
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]

### resourcePrefix
- **Type**: typing.Optional[str]


# MessageTypeDef

### contentType
- **Type**: typing.Literal['CustomPayload', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes

### groupNumber
- **Type**: typing.Optional[int]


# MigrationAlertTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MigrationSummaryTypeDef

### migrationId
- **Type**: typing.Optional[str]

### v1BotName
- **Type**: typing.Optional[str]

### v1BotVersion
- **Type**: typing.Optional[str]

### v1BotLocale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### v2BotId
- **Type**: typing.Optional[str]

### v2BotRole
- **Type**: typing.Optional[str]

### migrationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### migrationStrategy
- **Type**: typing.Optional[typing.Literal['CREATE_NEW', 'UPDATE_EXISTING']]

### migrationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# OutputContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLiveInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### turnsToLive
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PromptOutputTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.MessageTypeDef]
- **Required**: Yes

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# PromptTypeDef

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.MessageTypeDef]
- **Required**: Yes

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# PromptUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutBotAliasRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### conversationLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.ConversationLogsRequestTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]]


# PutBotAliasResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### conversationLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ConversationLogsResponseTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutBotRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']
- **Required**: Yes

### childDirected
- **Type**: <class 'bool'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### intents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.IntentTypeDef]]

### enableModelImprovements
- **Type**: typing.Optional[bool]

### nluIntentConfidenceThreshold
- **Type**: typing.Optional[float]

### clarificationPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptUnionTypeDef]

### abortStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.StatementUnionTypeDef]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### voiceId
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### processBehavior
- **Type**: typing.Optional[typing.Literal['BUILD', 'SAVE']]

### detectSentiment
- **Type**: typing.Optional[bool]

### createVersion
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]]


# PutBotResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.IntentTypeDef]
- **Required**: Yes

### enableModelImprovements
- **Type**: <class 'bool'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### clarificationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['BUILDING', 'FAILED', 'NOT_BUILT', 'READY', 'READY_BASIC_TESTING']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### voiceId
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']
- **Required**: Yes

### childDirected
- **Type**: <class 'bool'>
- **Required**: Yes

### createVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### detectSentiment
- **Type**: <class 'bool'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutIntentRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.SlotUnionTypeDef]]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[str]]

### confirmationPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptUnionTypeDef]

### rejectionStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.StatementUnionTypeDef]

### followUpPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptUnionTypeDef]

### conclusionStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.StatementUnionTypeDef]

### dialogCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.CodeHookTypeDef]

### fulfillmentActivity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.FulfillmentActivityTypeDef]

### parentIntentSignature
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### createVersion
- **Type**: typing.Optional[bool]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.KendraConfigurationTypeDef]

### inputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.InputContextTypeDef]]

### outputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.OutputContextTypeDef]]


# PutIntentResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotOutputTypeDef]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptOutputTypeDef'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementOutputTypeDef'>
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.CodeHookTypeDef'>
- **Required**: Yes

### fulfillmentActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FulfillmentActivityTypeDef'>
- **Required**: Yes

### parentIntentSignature
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### createVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.KendraConfigurationTypeDef'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.InputContextTypeDef]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.OutputContextTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSlotTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### enumerationValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueUnionTypeDef]]

### checksum
- **Type**: typing.Optional[str]

### valueSelectionStrategy
- **Type**: typing.Optional[typing.Literal['ORIGINAL_VALUE', 'TOP_RESOLUTION']]

### createVersion
- **Type**: typing.Optional[bool]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### slotTypeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeConfigurationTypeDef]]


# PutSlotTypeResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enumerationValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueOutputTypeDef]
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### valueSelectionStrategy
- **Type**: typing.Literal['ORIGINAL_VALUE', 'TOP_RESOLUTION']
- **Required**: Yes

### createVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### parentSlotTypeSignature
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
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


# SlotDefaultValueSpecOutputTypeDef

### defaultValueList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotDefaultValueTypeDef]
- **Required**: Yes


# SlotDefaultValueSpecTypeDef

### defaultValueList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.SlotDefaultValueTypeDef]
- **Required**: Yes


# SlotDefaultValueSpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SlotDefaultValueTypeDef

### defaultValue
- **Type**: <class 'str'>
- **Required**: Yes


# SlotOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slotConstraint
- **Type**: typing.Literal['Optional', 'Required']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slotType
- **Type**: typing.Optional[str]

### slotTypeVersion
- **Type**: typing.Optional[str]

### valueElicitationPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptOutputTypeDef]

### priority
- **Type**: typing.Optional[int]

### sampleUtterances
- **Type**: typing.Optional[typing.List[str]]

### responseCard
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[typing.Literal['DEFAULT_OBFUSCATION', 'NONE']]

### defaultValueSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.SlotDefaultValueSpecOutputTypeDef]


# SlotTypeConfigurationTypeDef

### regexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeRegexConfigurationTypeDef]


# SlotTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slotConstraint
- **Type**: typing.Literal['Optional', 'Required']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slotType
- **Type**: typing.Optional[str]

### slotTypeVersion
- **Type**: typing.Optional[str]

### valueElicitationPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptUnionTypeDef]

### priority
- **Type**: typing.Optional[int]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[str]]

### responseCard
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[typing.Literal['DEFAULT_OBFUSCATION', 'NONE']]

### defaultValueSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.SlotDefaultValueSpecUnionTypeDef]


# SlotTypeMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### version
- **Type**: typing.Optional[str]


# SlotTypeRegexConfigurationTypeDef

### pattern
- **Type**: <class 'str'>
- **Required**: Yes


# SlotUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartImportRequestTypeDef

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.BlobTypeDef'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['BOT', 'INTENT', 'SLOT_TYPE']
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['FAIL_ON_CONFLICT', 'OVERWRITE_LATEST']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]]


# StartImportResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['BOT', 'INTENT', 'SLOT_TYPE']
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['FAIL_ON_CONFLICT', 'OVERWRITE_LATEST']
- **Required**: Yes

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### importStatus
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMigrationRequestTypeDef

### v1BotName
- **Type**: <class 'str'>
- **Required**: Yes

### v1BotVersion
- **Type**: <class 'str'>
- **Required**: Yes

### v2BotName
- **Type**: <class 'str'>
- **Required**: Yes

### v2BotRole
- **Type**: <class 'str'>
- **Required**: Yes

### migrationStrategy
- **Type**: typing.Literal['CREATE_NEW', 'UPDATE_EXISTING']
- **Required**: Yes


# StartMigrationResponseTypeDef

### v1BotName
- **Type**: <class 'str'>
- **Required**: Yes

### v1BotVersion
- **Type**: <class 'str'>
- **Required**: Yes

### v1BotLocale
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']
- **Required**: Yes

### v2BotId
- **Type**: <class 'str'>
- **Required**: Yes

### v2BotRole
- **Type**: <class 'str'>
- **Required**: Yes

### migrationId
- **Type**: <class 'str'>
- **Required**: Yes

### migrationStrategy
- **Type**: typing.Literal['CREATE_NEW', 'UPDATE_EXISTING']
- **Required**: Yes

### migrationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatementOutputTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.MessageTypeDef]
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# StatementTypeDef

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.MessageTypeDef]
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# StatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UtteranceDataTypeDef

### utteranceString
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### distinctUsers
- **Type**: typing.Optional[int]

### firstUtteredDate
- **Type**: typing.Optional[datetime.datetime]

### lastUtteredDate
- **Type**: typing.Optional[datetime.datetime]


# UtteranceListTypeDef

### botVersion
- **Type**: typing.Optional[str]

### utterances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models_classes.UtteranceDataTypeDef]]


