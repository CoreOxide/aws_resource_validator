# Lex Models Lex Models Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BotAliasMetadata

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ConversationLogsResponse]


# BotChannelAssociation

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


# BotMetadata

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


# BuiltinIntentMetadata

### signature
- **Type**: typing.Optional[str]

### supportedLocales
- **Type**: typing.Optional[typing.List[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]]


# BuiltinIntentSlot

### name
- **Type**: typing.Optional[str]


# BuiltinSlotTypeMetadata

### signature
- **Type**: typing.Optional[str]

### supportedLocales
- **Type**: typing.Optional[typing.List[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]]


# CodeHook

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### messageVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ConversationLogsRequest

### logSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.LogSettingsRequest]
- **Required**: Yes

### iamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConversationLogsResponse

### logSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.LogSettingsResponse]]

### iamRoleArn
- **Type**: typing.Optional[str]


# CreateBotVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: typing.Optional[str]


# CreateBotVersionResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Intent]
- **Required**: Yes

### clarificationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntentVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: typing.Optional[str]


# CreateIntentVersionResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotOutput]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FollowUpPromptOutput'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.CodeHook'>
- **Required**: Yes

### fulfillmentActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FulfillmentActivity'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.KendraConfiguration'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.InputContext]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.OutputContext]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSlotTypeVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: typing.Optional[str]


# CreateSlotTypeVersionResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enumerationValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.EnumerationValueOutput]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBotAliasRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotChannelAssociationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntentRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntentVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUtterancesRequest

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# EnumerationValue

### value
- **Type**: <class 'str'>
- **Required**: Yes

### synonyms
- **Type**: typing.Optional[typing.List[str]]


# EnumerationValueOutput

### value
- **Type**: <class 'str'>
- **Required**: Yes

### synonyms
- **Type**: typing.Optional[typing.List[str]]


# FollowUpPrompt

### prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Prompt'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Statement'>
- **Required**: Yes


# FollowUpPromptOutput

### prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes


# FulfillmentActivity

### type
- **Type**: typing.Literal['CodeHook', 'ReturnIntent']
- **Required**: Yes

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.CodeHook]


# GetBotAliasRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotAliasResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ConversationLogsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetBotAliasesRequest

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetBotAliasesRequestPaginate

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetBotAliasesResponse

### BotAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BotAliasMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBotChannelAssociationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotChannelAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetBotChannelAssociationsRequest

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


# GetBotChannelAssociationsRequestPaginate

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetBotChannelAssociationsResponse

### botChannelAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BotChannelAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBotRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionOrAlias
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Intent]
- **Required**: Yes

### enableModelImprovements
- **Type**: <class 'bool'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### clarificationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetBotVersionsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetBotVersionsRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetBotVersionsResponse

### bots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BotMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBotsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetBotsRequestPaginate

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetBotsResponse

### bots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BotMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBuiltinIntentRequest

### signature
- **Type**: <class 'str'>
- **Required**: Yes


# GetBuiltinIntentResponse

### signature
- **Type**: <class 'str'>
- **Required**: Yes

### supportedLocales
- **Type**: typing.List[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BuiltinIntentSlot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetBuiltinIntentsRequest

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetBuiltinIntentsRequestPaginate

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetBuiltinIntentsResponse

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BuiltinIntentMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBuiltinSlotTypesRequest

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetBuiltinSlotTypesRequestPaginate

### locale
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'es-419', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'ko-KR']]

### signatureContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetBuiltinSlotTypesResponse

### slotTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.BuiltinSlotTypeMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetExportRequest

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


# GetExportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportRequest

### importId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntentRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntentResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotOutput]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FollowUpPromptOutput'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.CodeHook'>
- **Required**: Yes

### fulfillmentActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FulfillmentActivity'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.KendraConfiguration'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.InputContext]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.OutputContext]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntentVersionsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetIntentVersionsRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetIntentVersionsResponse

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.IntentMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetIntentsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetIntentsRequestPaginate

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetIntentsResponse

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.IntentMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetMigrationRequest

### migrationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.MigrationAlert]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetMigrationsRequest

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


# GetMigrationsResponse

### migrationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.MigrationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSlotTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# GetSlotTypeResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enumerationValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.EnumerationValueOutput]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# GetSlotTypeVersionsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetSlotTypeVersionsRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetSlotTypeVersionsResponse

### slotTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSlotTypesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nameContains
- **Type**: typing.Optional[str]


# GetSlotTypesRequestPaginate

### nameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PaginatorConfig]


# GetSlotTypesResponse

### slotTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetUtterancesViewRequest

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botVersions
- **Type**: typing.List[str]
- **Required**: Yes

### statusType
- **Type**: typing.Literal['Detected', 'Missed']
- **Required**: Yes


# GetUtterancesViewResponse

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### utterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.UtteranceList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# InputContext

### name
- **Type**: <class 'str'>
- **Required**: Yes


# Intent

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### intentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# IntentMetadata

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


# KendraConfiguration

### kendraIndex
- **Type**: <class 'str'>
- **Required**: Yes

### role
- **Type**: <class 'str'>
- **Required**: Yes

### queryFilterString
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# LogSettingsRequest

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


# LogSettingsResponse

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


# Message

### contentType
- **Type**: typing.Literal['CustomPayload', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes

### groupNumber
- **Type**: typing.Optional[int]


# MigrationAlert

### type
- **Type**: typing.Optional[typing.Literal['ERROR', 'WARN']]

### message
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[typing.List[str]]

### referenceURLs
- **Type**: typing.Optional[typing.List[str]]


# MigrationSummary

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


# OutputContext

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLiveInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### turnsToLive
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Prompt

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Message]
- **Required**: Yes

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# PromptOutput

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Message]
- **Required**: Yes

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# PutBotAliasRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ConversationLogsRequest]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]]


# PutBotAliasResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ConversationLogsResponse'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# PutBotRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Intent]]

### enableModelImprovements
- **Type**: typing.Optional[bool]

### nluIntentConfidenceThreshold
- **Type**: typing.Optional[float]

### clarificationPrompt
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Prompt, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput, NoneType]

### abortStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Statement, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput, NoneType]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]]


# PutBotResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### intents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Intent]
- **Required**: Yes

### enableModelImprovements
- **Type**: <class 'bool'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### clarificationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### abortStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# PutIntentRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Slot, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotOutput]]]

### sampleUtterances
- **Type**: typing.Optional[typing.List[str]]

### confirmationPrompt
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Prompt, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput, NoneType]

### rejectionStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Statement, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput, NoneType]

### followUpPrompt
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FollowUpPrompt, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FollowUpPromptOutput, NoneType]

### conclusionStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Statement, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput, NoneType]

### dialogCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.CodeHook]

### fulfillmentActivity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FulfillmentActivity]

### parentIntentSignature
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### createVersion
- **Type**: typing.Optional[bool]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.KendraConfiguration]

### inputContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.InputContext]]

### outputContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.OutputContext]]


# PutIntentResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotOutput]
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[str]
- **Required**: Yes

### confirmationPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput'>
- **Required**: Yes

### rejectionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes

### followUpPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FollowUpPromptOutput'>
- **Required**: Yes

### conclusionStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.StatementOutput'>
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.CodeHook'>
- **Required**: Yes

### fulfillmentActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.FulfillmentActivity'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.KendraConfiguration'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.InputContext]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.OutputContext]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# PutSlotTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### enumerationValues
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.EnumerationValue, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.EnumerationValueOutput]]]

### checksum
- **Type**: typing.Optional[str]

### valueSelectionStrategy
- **Type**: typing.Optional[typing.Literal['ORIGINAL_VALUE', 'TOP_RESOLUTION']]

### createVersion
- **Type**: typing.Optional[bool]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### slotTypeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeConfiguration]]


# PutSlotTypeResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enumerationValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.EnumerationValueOutput]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
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


# Slot

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Prompt, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput, NoneType]

### priority
- **Type**: typing.Optional[int]

### sampleUtterances
- **Type**: typing.Optional[typing.List[str]]

### responseCard
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[typing.Literal['DEFAULT_OBFUSCATION', 'NONE']]

### defaultValueSpec
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotDefaultValueSpec, aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotDefaultValueSpecOutput, NoneType]


# SlotDefaultValue

### defaultValue
- **Type**: <class 'str'>
- **Required**: Yes


# SlotDefaultValueSpec

### defaultValueList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotDefaultValue]
- **Required**: Yes


# SlotDefaultValueSpecOutput

### defaultValueList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotDefaultValue]
- **Required**: Yes


# SlotOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.PromptOutput]

### priority
- **Type**: typing.Optional[int]

### sampleUtterances
- **Type**: typing.Optional[typing.List[str]]

### responseCard
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[typing.Literal['DEFAULT_OBFUSCATION', 'NONE']]

### defaultValueSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotDefaultValueSpecOutput]


# SlotTypeConfiguration

### regexConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.SlotTypeRegexConfiguration]


# SlotTypeMetadata

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


# SlotTypeRegexConfiguration

### pattern
- **Type**: <class 'str'>
- **Required**: Yes


# StartImportRequest

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['BOT', 'INTENT', 'SLOT_TYPE']
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['FAIL_ON_CONFLICT', 'OVERWRITE_LATEST']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]]


# StartImportResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# StartMigrationRequest

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


# StartMigrationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_models.lex_models_classes.ResponseMetadata'>
- **Required**: Yes


# Statement

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Message]
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# StatementOutput

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Message]
- **Required**: Yes

### responseCard
- **Type**: typing.Optional[str]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UtteranceData

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


# UtteranceList

### botVersion
- **Type**: typing.Optional[str]

### utterances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_models.lex_models_classes.UtteranceData]]


