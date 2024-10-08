# Pydantic Models in lex_models_classes

# BaseValidatorModel

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

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### botAlias
- **Type**: typing.Optional[str]

### botName
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### type
- **Type**: typing.Optional[typing.Literal['Facebook', 'Kik', 'Slack', 'Twilio-Sms']]

### botConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS']]

### failureReason
- **Type**: typing.Optional[str]


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


# CreateBotVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
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


# CreateIntentVersionRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeDef]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptTypeDef'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
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


# CreateSlotTypeVersionRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueTypeDef]
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


# DeleteBotAliasRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotChannelAssociationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotVersionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntentRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntentVersionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeVersionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUtterancesRequestRequestTypeDef

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


# EnumerationValueTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### synonyms
- **Type**: typing.Optional[typing.List[str]]


# FollowUpPromptTypeDef

### prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
- **Required**: Yes


# FulfillmentActivityTypeDef

### type
- **Type**: typing.Literal['CodeHook', 'ReturnIntent']
- **Required**: Yes

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.CodeHookTypeDef]


# GetBotAliasRequestRequestTypeDef

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


# GetBotAliasesRequestGetBotAliasesPaginateTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotAliasesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotChannelAssociationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotChannelAssociationResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Facebook', 'Kik', 'Slack', 'Twilio-Sms']
- **Required**: Yes

### botConfiguration
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef

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


# GetBotChannelAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
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


# GetBotVersionsRequestGetBotVersionsPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotsRequestGetBotsPaginateTypeDef

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBotsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBuiltinIntentRequestRequestTypeDef

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


# GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBuiltinIntentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetBuiltinSlotTypesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportRequestRequestTypeDef

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


# GetImportRequestRequestTypeDef

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


# GetIntentRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeDef]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptTypeDef'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
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


# GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetIntentVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntentsRequestGetIntentsPaginateTypeDef

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetIntentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMigrationRequestRequestTypeDef

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


# GetMigrationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSlotTypeRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueTypeDef]
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


# GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetSlotTypeVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSlotTypesRequestGetSlotTypesPaginateTypeDef

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PaginatorConfigTypeDef]


# GetSlotTypesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUtterancesViewRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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

### type
- **Type**: typing.Optional[typing.Literal['ERROR', 'WARN']]

### message
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[typing.List[str]]

### referenceURLs
- **Type**: typing.Optional[typing.List[str]]


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


# PromptTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.MessageTypeDef]
- **Required**: Yes

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# PutBotAliasRequestRequestTypeDef

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


# PutBotRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef]

### abortStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
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


# PutIntentRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeDef]]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[str]]

### confirmationPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef]

### rejectionStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef]

### followUpPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptTypeDef]

### conclusionStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotTypeDef]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.FollowUpPromptTypeDef'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models_classes.StatementTypeDef'>
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


# PutSlotTypeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### enumerationValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueTypeDef]]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.EnumerationValueTypeDef]
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


# SlotDefaultValueSpecTypeDef

### defaultValueList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.SlotDefaultValueTypeDef]
- **Required**: Yes


# SlotDefaultValueTypeDef

### defaultValue
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.PromptTypeDef]

### priority
- **Type**: typing.Optional[int]

### sampleUtterances
- **Type**: typing.Optional[typing.List[str]]

### responseCard
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[typing.Literal['DEFAULT_OBFUSCATION', 'NONE']]

### defaultValueSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models_classes.SlotDefaultValueSpecTypeDef]


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


# StartImportRequestRequestTypeDef

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# StartMigrationRequestRequestTypeDef

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


# StatementTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models_classes.MessageTypeDef]
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

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


