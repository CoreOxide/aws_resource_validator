# lexv2_models_classes

# ActiveContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# AdvancedRecognitionSettingTypeDef

### audioRecognitionStrategy
- **Type**: typing.Optional[typing.Literal['UseSlotValuesAsCustomVocabulary']]


# AgentTurnResultTypeDef

### expectedAgentPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### actualAgentPrompt
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExecutionErrorDetailsTypeDef]

### actualElicitedSlot
- **Type**: typing.Optional[str]

### actualIntent
- **Type**: typing.Optional[str]


# AgentTurnSpecificationTypeDef

### agentPrompt
- **Type**: <class 'str'>
- **Required**: Yes


# AggregatedUtterancesFilterTypeDef

### name
- **Type**: typing.Literal['Utterance']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# AggregatedUtterancesSortByTypeDef

### attribute
- **Type**: typing.Literal['HitCount', 'MissedCount']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# AggregatedUtterancesSummaryTypeDef

### utterance
- **Type**: typing.Optional[str]

### hitCount
- **Type**: typing.Optional[int]

### missedCount
- **Type**: typing.Optional[int]

### utteranceFirstRecordedInAggregationDuration
- **Type**: typing.Optional[datetime.datetime]

### utteranceLastRecordedInAggregationDuration
- **Type**: typing.Optional[datetime.datetime]

### containsDataFromDeletedResources
- **Type**: typing.Optional[bool]


# AllowedInputTypesTypeDef

### allowAudioInput
- **Type**: <class 'bool'>
- **Required**: Yes

### allowDTMFInput
- **Type**: <class 'bool'>
- **Required**: Yes


# AnalyticsBinBySpecificationTypeDef

### name
- **Type**: typing.Literal['ConversationStartTime', 'UtteranceTimestamp']
- **Required**: Yes

### interval
- **Type**: typing.Literal['OneDay', 'OneHour']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsBinKeyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['ConversationStartTime', 'UtteranceTimestamp']]

### value
- **Type**: typing.Optional[int]


# AnalyticsIntentFilterTypeDef

### name
- **Type**: typing.Literal['BotAliasId', 'BotVersion', 'Channel', 'IntentEndState', 'IntentName', 'LocaleId', 'Modality', 'OriginatingRequestId', 'SessionId']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQ', 'GT', 'LT']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AnalyticsIntentGroupByKeyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['IntentEndState', 'IntentLevel', 'IntentName']]

### value
- **Type**: typing.Optional[str]


# AnalyticsIntentGroupBySpecificationTypeDef

### name
- **Type**: typing.Literal['IntentEndState', 'IntentLevel', 'IntentName']
- **Required**: Yes


# AnalyticsIntentMetricResultTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Count', 'Dropped', 'Failure', 'Success', 'Switched']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsIntentMetricTypeDef

### name
- **Type**: typing.Literal['Count', 'Dropped', 'Failure', 'Success', 'Switched']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsIntentNodeSummaryTypeDef

### intentName
- **Type**: typing.Optional[str]

### intentPath
- **Type**: typing.Optional[str]

### intentCount
- **Type**: typing.Optional[int]

### intentLevel
- **Type**: typing.Optional[int]

### nodeType
- **Type**: typing.Optional[typing.Literal['Exit', 'Inner']]


# AnalyticsIntentResultTypeDef

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKeyTypeDef]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentGroupByKeyTypeDef]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentMetricResultTypeDef]]


# AnalyticsIntentStageFilterTypeDef

### name
- **Type**: typing.Literal['BotAliasId', 'BotVersion', 'Channel', 'IntentName', 'IntentStageName', 'LocaleId', 'Modality', 'OriginatingRequestId', 'SessionId']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQ', 'GT', 'LT']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AnalyticsIntentStageGroupByKeyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['IntentStageName', 'SwitchedToIntent']]

### value
- **Type**: typing.Optional[str]


# AnalyticsIntentStageGroupBySpecificationTypeDef

### name
- **Type**: typing.Literal['IntentStageName', 'SwitchedToIntent']
- **Required**: Yes


# AnalyticsIntentStageMetricResultTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Count', 'Dropped', 'Failed', 'Retry', 'Success']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsIntentStageMetricTypeDef

### name
- **Type**: typing.Literal['Count', 'Dropped', 'Failed', 'Retry', 'Success']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsIntentStageResultTypeDef

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKeyTypeDef]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageGroupByKeyTypeDef]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageMetricResultTypeDef]]


# AnalyticsPathFilterTypeDef

### name
- **Type**: typing.Literal['BotAliasId', 'BotVersion', 'Channel', 'LocaleId', 'Modality']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQ', 'GT', 'LT']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AnalyticsSessionFilterTypeDef

### name
- **Type**: typing.Literal['BotAliasId', 'BotVersion', 'Channel', 'ConversationEndState', 'Duration', 'IntentPath', 'LocaleId', 'Modality', 'OriginatingRequestId', 'SessionId']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQ', 'GT', 'LT']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AnalyticsSessionGroupByKeyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['ConversationEndState', 'LocaleId']]

### value
- **Type**: typing.Optional[str]


# AnalyticsSessionGroupBySpecificationTypeDef

### name
- **Type**: typing.Literal['ConversationEndState', 'LocaleId']
- **Required**: Yes


# AnalyticsSessionMetricResultTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Concurrency', 'Count', 'Dropped', 'Duration', 'Failure', 'Success', 'TurnsPerConversation']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsSessionMetricTypeDef

### name
- **Type**: typing.Literal['Concurrency', 'Count', 'Dropped', 'Duration', 'Failure', 'Success', 'TurnsPerConversation']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsSessionResultTypeDef

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKeyTypeDef]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionGroupByKeyTypeDef]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionMetricResultTypeDef]]


# AnalyticsUtteranceAttributeResultTypeDef

### lastUsedIntent
- **Type**: typing.Optional[str]


# AnalyticsUtteranceAttributeTypeDef

### name
- **Type**: typing.Literal['LastUsedIntent']
- **Required**: Yes


# AnalyticsUtteranceFilterTypeDef

### name
- **Type**: typing.Literal['BotAliasId', 'BotVersion', 'Channel', 'LocaleId', 'Modality', 'OriginatingRequestId', 'SessionId', 'UtteranceState', 'UtteranceText']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQ', 'GT', 'LT']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AnalyticsUtteranceGroupByKeyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['UtteranceState', 'UtteranceText']]

### value
- **Type**: typing.Optional[str]


# AnalyticsUtteranceGroupBySpecificationTypeDef

### name
- **Type**: typing.Literal['UtteranceState', 'UtteranceText']
- **Required**: Yes


# AnalyticsUtteranceMetricResultTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Count', 'Detected', 'Missed', 'UtteranceTimestamp']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsUtteranceMetricTypeDef

### name
- **Type**: typing.Literal['Count', 'Detected', 'Missed', 'UtteranceTimestamp']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsUtteranceResultTypeDef

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKeyTypeDef]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceGroupByKeyTypeDef]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceMetricResultTypeDef]]

### attributeResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceAttributeResultTypeDef]]


# AssociatedTranscriptFilterTypeDef

### name
- **Type**: typing.Literal['IntentId', 'SlotTypeId']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociatedTranscriptTypeDef

### transcript
- **Type**: typing.Optional[str]


# AudioAndDTMFInputSpecificationTypeDef

### startTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes

### audioSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioSpecificationTypeDef]

### dtmfSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DTMFSpecificationTypeDef]


# AudioLogDestinationTypeDef

### s3Bucket
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.S3BucketLogDestinationTypeDef'>
- **Required**: Yes


# AudioLogSettingTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.AudioLogDestinationTypeDef'>
- **Required**: Yes

### selectiveLoggingEnabled
- **Type**: typing.Optional[bool]


# AudioSpecificationTypeDef

### maxLengthMs
- **Type**: <class 'int'>
- **Required**: Yes

### endTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateCustomVocabularyItemRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### customVocabularyItemList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.NewCustomVocabularyItemTypeDef]
- **Required**: Yes


# BatchCreateCustomVocabularyItemResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.FailedCustomVocabularyItemTypeDef]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteCustomVocabularyItemRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### customVocabularyItemList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyEntryIdTypeDef]
- **Required**: Yes


# BatchDeleteCustomVocabularyItemResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.FailedCustomVocabularyItemTypeDef]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateCustomVocabularyItemRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### customVocabularyItemList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItemTypeDef]
- **Required**: Yes


# BatchUpdateCustomVocabularyItemResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.FailedCustomVocabularyItemTypeDef]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BedrockKnowledgeStoreConfigurationTypeDef

### bedrockKnowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes


# BedrockModelSpecificationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# BotAliasHistoryEventTypeDef

### botVersion
- **Type**: typing.Optional[str]

### startDate
- **Type**: typing.Optional[datetime.datetime]

### endDate
- **Type**: typing.Optional[datetime.datetime]


# BotAliasLocaleSettingsTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### codeHookSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CodeHookSpecificationTypeDef]


# BotAliasReplicaSummaryTypeDef

### botAliasId
- **Type**: typing.Optional[str]

### botAliasReplicationStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Updating']]

### botVersion
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# BotAliasSummaryTypeDef

### botAliasId
- **Type**: typing.Optional[str]

### botAliasName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### botAliasStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleting', 'Failed']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# BotAliasTestExecutionTargetTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# BotExportSpecificationTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes


# BotFilterTypeDef

### name
- **Type**: typing.Literal['BotName', 'BotType']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ', 'NE']
- **Required**: Yes


# BotImportSpecificationTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### botTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### testBotAliasTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BotLocaleExportSpecificationTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# BotLocaleFilterTypeDef

### name
- **Type**: typing.Literal['BotLocaleName']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# BotLocaleHistoryEventTypeDef

### event
- **Type**: <class 'str'>
- **Required**: Yes

### eventDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BotLocaleImportSpecificationTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: typing.Optional[float]

### voiceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettingsTypeDef]


# BotLocaleSortByTypeDef

### attribute
- **Type**: typing.Literal['BotLocaleName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotLocaleSummaryTypeDef

### localeId
- **Type**: typing.Optional[str]

### localeName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### botLocaleStatus
- **Type**: typing.Optional[typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastBuildSubmittedDateTime
- **Type**: typing.Optional[datetime.datetime]


# BotMemberTypeDef

### botMemberId
- **Type**: <class 'str'>
- **Required**: Yes

### botMemberName
- **Type**: <class 'str'>
- **Required**: Yes

### botMemberAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botMemberAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### botMemberVersion
- **Type**: <class 'str'>
- **Required**: Yes


# BotRecommendationResultStatisticsTypeDef

### intents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentStatisticsTypeDef]

### slotTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeStatisticsTypeDef]


# BotRecommendationResultsTypeDef

### botLocaleExportUrl
- **Type**: typing.Optional[str]

### associatedTranscriptsUrl
- **Type**: typing.Optional[str]

### statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotRecommendationResultStatisticsTypeDef]


# BotRecommendationSummaryTypeDef

### botRecommendationStatus
- **Type**: typing.Literal['Available', 'Deleted', 'Deleting', 'Downloading', 'Failed', 'Processing', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# BotReplicaSummaryTypeDef

### replicaRegion
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### botReplicaStatus
- **Type**: typing.Optional[typing.Literal['Deleting', 'Enabled', 'Enabling', 'Failed']]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# BotSortByTypeDef

### attribute
- **Type**: typing.Literal['BotName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotSummaryTypeDef

### botId
- **Type**: typing.Optional[str]

### botName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### botStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']]

### latestBotVersion
- **Type**: typing.Optional[str]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### botType
- **Type**: typing.Optional[typing.Literal['Bot', 'BotNetwork']]


# BotVersionLocaleDetailsTypeDef

### sourceBotVersion
- **Type**: <class 'str'>
- **Required**: Yes


# BotVersionReplicaSortByTypeDef

### attribute
- **Type**: typing.Literal['BotVersion']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotVersionReplicaSummaryTypeDef

### botVersion
- **Type**: typing.Optional[str]

### botVersionReplicationStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleting', 'Failed']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# BotVersionSortByTypeDef

### attribute
- **Type**: typing.Literal['BotVersion']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotVersionSummaryTypeDef

### botName
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### botStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]


# BuildBotLocaleRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# BuildBotLocaleResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botLocaleStatus
- **Type**: typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']
- **Required**: Yes

### lastBuildSubmittedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BuildtimeSettingsTypeDef

### descriptiveBotBuilder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DescriptiveBotBuilderSpecificationTypeDef]

### sampleUtteranceGeneration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceGenerationSpecificationTypeDef]


# BuiltInIntentSortByTypeDef

### attribute
- **Type**: typing.Literal['IntentSignature']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BuiltInIntentSummaryTypeDef

### intentSignature
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# BuiltInSlotTypeSortByTypeDef

### attribute
- **Type**: typing.Literal['SlotTypeSignature']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BuiltInSlotTypeSummaryTypeDef

### slotTypeSignature
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ButtonTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLogGroupLogDestinationTypeDef

### cloudWatchLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### logPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# CodeHookSpecificationTypeDef

### lambdaCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.LambdaCodeHookTypeDef'>
- **Required**: Yes


# CompositeSlotTypeSettingTypeDef

### subSlots
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotTypeCompositionTypeDef]]


# ConditionTypeDef

### expressionString
- **Type**: <class 'str'>
- **Required**: Yes


# ConditionalBranchTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionTypeDef'>
- **Required**: Yes

### nextStep
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef'>
- **Required**: Yes

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]


# ConditionalSpecificationTypeDef

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### conditionalBranches
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalBranchTypeDef]
- **Required**: Yes

### defaultBranch
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DefaultConditionalBranchTypeDef'>
- **Required**: Yes


# ConversationLevelIntentClassificationResultItemTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### matchResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes


# ConversationLevelResultDetailTypeDef

### endToEndResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes

### speechTranscriptionResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]


# ConversationLevelSlotResolutionResultItemTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### matchResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes


# ConversationLevelTestResultItemTypeDef

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### endToEndResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes

### intentClassificationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelIntentClassificationResultItemTypeDef]
- **Required**: Yes

### slotResolutionResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelSlotResolutionResultItemTypeDef]
- **Required**: Yes

### speechTranscriptionResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]


# ConversationLevelTestResultsFilterByTypeDef

### endToEndResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]


# ConversationLevelTestResultsTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelTestResultItemTypeDef]
- **Required**: Yes


# ConversationLogSettingsTypeDef

### textLogSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.TextLogSettingTypeDef]]

### audioLogSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioLogSettingTypeDef]]


# ConversationLogsDataSourceFilterByTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputMode
- **Type**: typing.Literal['Speech', 'Text']
- **Required**: Yes


# ConversationLogsDataSourceTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogsDataSourceFilterByTypeDef'>
- **Required**: Yes


# CreateBotAliasRequestRequestTypeDef

### botAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### botAliasLocaleSettings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettingsTypeDef]]

### conversationLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsTypeDef]

### sentimentAnalysisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettingsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateBotAliasResponseTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasLocaleSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettingsTypeDef]
- **Required**: Yes

### conversationLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsTypeDef'>
- **Required**: Yes

### sentimentAnalysisSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettingsTypeDef'>
- **Required**: Yes

### botAliasStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed']
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBotLocaleRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### voiceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettingsTypeDef]

### generativeAISettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettingsTypeDef]


# CreateBotLocaleResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeName
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### voiceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettingsTypeDef'>
- **Required**: Yes

### botLocaleStatus
- **Type**: typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### generativeAISettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBotReplicaRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBotReplicaResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### botReplicaStatus
- **Type**: typing.Literal['Deleting', 'Enabled', 'Enabling', 'Failed']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBotRequestRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### botTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### testBotAliasTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### botType
- **Type**: typing.Optional[typing.Literal['Bot', 'BotNetwork']]

### botMembers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMemberTypeDef]]


# CreateBotResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### botTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### testBotAliasTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### botType
- **Type**: typing.Literal['Bot', 'BotNetwork']
- **Required**: Yes

### botMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBotVersionRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersionLocaleSpecification
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionLocaleDetailsTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateBotVersionResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botVersionLocaleSpecification
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionLocaleDetailsTypeDef]
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExportRequestRequestTypeDef

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecificationTypeDef'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['CSV', 'LexJson', 'TSV']
- **Required**: Yes

### filePassword
- **Type**: typing.Optional[str]


# CreateExportResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecificationTypeDef'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['CSV', 'LexJson', 'TSV']
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntentRequestRequestTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parentIntentSignature
- **Type**: typing.Optional[str]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]]

### dialogCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettingsTypeDef]

### fulfillmentCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsTypeDef]

### intentConfirmationSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingTypeDef]

### intentClosingSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingTypeDef]

### inputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContextTypeDef]]

### outputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContextTypeDef]]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfigurationTypeDef]

### initialResponseSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingTypeDef]

### qnAIntentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationTypeDef]


# CreateIntentResponseTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### parentIntentSignature
- **Type**: <class 'str'>
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettingsTypeDef'>
- **Required**: Yes

### fulfillmentCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsTypeDef'>
- **Required**: Yes

### intentConfirmationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingTypeDef'>
- **Required**: Yes

### intentClosingSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingTypeDef'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContextTypeDef]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContextTypeDef]
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfigurationTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### initialResponseSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingTypeDef'>
- **Required**: Yes

### qnAIntentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourcePolicyRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# CreateResourcePolicyResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourcePolicyStatementRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Allow', 'Deny']
- **Required**: Yes

### principal
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.PrincipalTypeDef]
- **Required**: Yes

### action
- **Type**: typing.Sequence[str]
- **Required**: Yes

### condition
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]

### expectedRevisionId
- **Type**: typing.Optional[str]


# CreateResourcePolicyStatementResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSlotRequestRequestTypeDef

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slotTypeId
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSettingTypeDef]

### multipleValuesSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSettingTypeDef]

### subSlotSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingTypeDef]


# CreateSlotResponseTypeDef

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingTypeDef'>
- **Required**: Yes

### obfuscationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSettingTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### multipleValuesSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSettingTypeDef'>
- **Required**: Yes

### subSlotSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSlotTypeRequestRequestTypeDef

### slotTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slotTypeValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueTypeDef]]

### valueSelectionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSettingTypeDef]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### externalSourceSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSettingTypeDef]

### compositeSlotTypeSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingTypeDef]


# CreateSlotTypeResponseTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueTypeDef]
- **Required**: Yes

### valueSelectionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSettingTypeDef'>
- **Required**: Yes

### parentSlotTypeSignature
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### externalSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSettingTypeDef'>
- **Required**: Yes

### compositeSlotTypeSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTestSetDiscrepancyReportRequestRequestTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportResourceTargetTypeDef'>
- **Required**: Yes


# CreateTestSetDiscrepancyReportResponseTypeDef

### testSetDiscrepancyReportId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportResourceTargetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUploadUrlResponseTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomPayloadTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyEntryIdTypeDef

### itemId
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyExportSpecificationTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyImportSpecificationTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyItemTypeDef

### itemId
- **Type**: <class 'str'>
- **Required**: Yes

### phrase
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### displayAs
- **Type**: typing.Optional[str]


# DTMFSpecificationTypeDef

### maxLength
- **Type**: <class 'int'>
- **Required**: Yes

### endTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes

### deletionCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### endCharacter
- **Type**: <class 'str'>
- **Required**: Yes


# DataPrivacyTypeDef

### childDirected
- **Type**: <class 'bool'>
- **Required**: Yes


# DataSourceConfigurationTypeDef

### opensearchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.OpensearchConfigurationTypeDef]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAKendraConfigurationTypeDef]

### bedrockKnowledgeStoreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockKnowledgeStoreConfigurationTypeDef]


# DateRangeFilterTypeDef

### startDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DefaultConditionalBranchTypeDef

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]


# DeleteBotAliasRequestRequestTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteBotAliasResponseTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBotLocaleRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotLocaleResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botLocaleStatus
- **Type**: typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBotReplicaRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotReplicaResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### botReplicaStatus
- **Type**: typing.Literal['Deleting', 'Enabled', 'Enabling', 'Failed']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBotRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteBotResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBotVersionRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteBotVersionResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomVocabularyRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVocabularyResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### customVocabularyStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Exporting', 'Importing', 'Ready']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteExportRequestRequestTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExportResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteImportRequestRequestTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportResponseTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### importStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIntentRequestRequestTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### expectedRevisionId
- **Type**: typing.Optional[str]


# DeleteResourcePolicyResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyStatementRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### expectedRevisionId
- **Type**: typing.Optional[str]


# DeleteResourcePolicyStatementResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSlotRequestRequestTypeDef

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSlotTypeRequestRequestTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteTestSetRequestRequestTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUtterancesRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]


# DescribeBotAliasRequestBotAliasAvailableWaitTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeBotAliasRequestRequestTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotAliasResponseTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasLocaleSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettingsTypeDef]
- **Required**: Yes

### conversationLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsTypeDef'>
- **Required**: Yes

### sentimentAnalysisSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettingsTypeDef'>
- **Required**: Yes

### botAliasHistoryEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasHistoryEventTypeDef]
- **Required**: Yes

### botAliasStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed']
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### parentBotNetworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ParentBotNetworkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeBotLocaleRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotLocaleResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### localeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### voiceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettingsTypeDef'>
- **Required**: Yes

### intentsCount
- **Type**: <class 'int'>
- **Required**: Yes

### slotTypesCount
- **Type**: <class 'int'>
- **Required**: Yes

### botLocaleStatus
- **Type**: typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastBuildSubmittedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### botLocaleHistoryEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleHistoryEventTypeDef]
- **Required**: Yes

### recommendedActions
- **Type**: typing.List[str]
- **Required**: Yes

### generativeAISettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBotRecommendationRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotRecommendationResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationStatus
- **Type**: typing.Literal['Available', 'Deleted', 'Deleting', 'Downloading', 'Failed', 'Processing', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transcriptSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingTypeDef'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSettingTypeDef'>
- **Required**: Yes

### botRecommendationResults
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.BotRecommendationResultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBotReplicaRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotReplicaResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### botReplicaStatus
- **Type**: typing.Literal['Deleting', 'Enabled', 'Enabling', 'Failed']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBotRequestBotAvailableWaitTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeBotRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotResourceGenerationRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### generationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotResourceGenerationResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### generationId
- **Type**: <class 'str'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### generationStatus
- **Type**: typing.Literal['Complete', 'Failed', 'InProgress']
- **Required**: Yes

### generationInputPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### generatedBotLocaleUrl
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBotResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### botType
- **Type**: typing.Literal['Bot', 'BotNetwork']
- **Required**: Yes

### botMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMemberTypeDef]
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBotVersionRequestBotVersionAvailableWaitTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeBotVersionRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotVersionResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### parentBotNetworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ParentBotNetworkTypeDef]
- **Required**: Yes

### botType
- **Type**: typing.Literal['Bot', 'BotNetwork']
- **Required**: Yes

### botMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomVocabularyMetadataRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomVocabularyMetadataResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### customVocabularyStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Exporting', 'Importing', 'Ready']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExportRequestBotExportCompletedWaitTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeExportRequestRequestTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExportResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecificationTypeDef'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['CSV', 'LexJson', 'TSV']
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### downloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImportRequestBotImportCompletedWaitTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaiterConfigTypeDef]


# DescribeImportRequestRequestTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeImportResponseTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ImportResourceSpecificationTypeDef'>
- **Required**: Yes

### importedResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### importedResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['Append', 'FailOnConflict', 'Overwrite']
- **Required**: Yes

### importStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIntentRequestRequestTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIntentResponseTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### parentIntentSignature
- **Type**: <class 'str'>
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettingsTypeDef'>
- **Required**: Yes

### fulfillmentCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsTypeDef'>
- **Required**: Yes

### slotPriorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotPriorityTypeDef]
- **Required**: Yes

### intentConfirmationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingTypeDef'>
- **Required**: Yes

### intentClosingSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingTypeDef'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContextTypeDef]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContextTypeDef]
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfigurationTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### initialResponseSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingTypeDef'>
- **Required**: Yes

### qnAIntentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePolicyRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSlotRequestRequestTypeDef

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSlotResponseTypeDef

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingTypeDef'>
- **Required**: Yes

### obfuscationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSettingTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### multipleValuesSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSettingTypeDef'>
- **Required**: Yes

### subSlotSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSlotTypeRequestRequestTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSlotTypeResponseTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueTypeDef]
- **Required**: Yes

### valueSelectionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSettingTypeDef'>
- **Required**: Yes

### parentSlotTypeSignature
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### externalSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSettingTypeDef'>
- **Required**: Yes

### compositeSlotTypeSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTestExecutionRequestRequestTypeDef

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestExecutionResponseTypeDef

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testExecutionStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping', 'Waiting']
- **Required**: Yes

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTargetTypeDef'>
- **Required**: Yes

### apiMode
- **Type**: typing.Literal['NonStreaming', 'Streaming']
- **Required**: Yes

### testExecutionModality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTestSetDiscrepancyReportRequestRequestTypeDef

### testSetDiscrepancyReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestSetDiscrepancyReportResponseTypeDef

### testSetDiscrepancyReportId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportResourceTargetTypeDef'>
- **Required**: Yes

### testSetDiscrepancyReportStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### lastUpdatedDataTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testSetDiscrepancyTopErrors
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyErrorsTypeDef'>
- **Required**: Yes

### testSetDiscrepancyRawOutputUrl
- **Type**: <class 'str'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTestSetGenerationRequestRequestTypeDef

### testSetGenerationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestSetGenerationResponseTypeDef

### testSetGenerationId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetGenerationStatus
- **Type**: typing.Literal['Failed', 'Generating', 'Pending', 'Ready']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef'>
- **Required**: Yes

### generationDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetGenerationDataSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTestSetRequestRequestTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestSetResponseTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### modality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleting', 'Importing', 'PendingAnnotation', 'Ready', 'ValidationError']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### numTurns
- **Type**: <class 'int'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescriptiveBotBuilderSpecificationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bedrockModelSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecificationTypeDef]


# DialogActionTypeDef

### type
- **Type**: typing.Literal['CloseIntent', 'ConfirmIntent', 'ElicitIntent', 'ElicitSlot', 'EndConversation', 'EvaluateConditional', 'FulfillIntent', 'InvokeDialogCodeHook', 'StartIntent']
- **Required**: Yes

### slotToElicit
- **Type**: typing.Optional[str]

### suppressNextMessage
- **Type**: typing.Optional[bool]


# DialogCodeHookInvocationSettingTypeDef

### enableCodeHookInvocation
- **Type**: <class 'bool'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### postCodeHookSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PostDialogCodeHookInvocationSpecificationTypeDef'>
- **Required**: Yes

### invocationLabel
- **Type**: typing.Optional[str]


# DialogCodeHookSettingsTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# DialogStateTypeDef

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogActionTypeDef]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentOverrideTypeDef]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ElicitationCodeHookInvocationSettingTypeDef

### enableCodeHookInvocation
- **Type**: <class 'bool'>
- **Required**: Yes

### invocationLabel
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionSettingTypeDef

### kmsKeyArn
- **Type**: typing.Optional[str]

### botLocaleExportPassword
- **Type**: typing.Optional[str]

### associatedTranscriptsPassword
- **Type**: typing.Optional[str]


# ExactResponseFieldsTypeDef

### questionField
- **Type**: <class 'str'>
- **Required**: Yes

### answerField
- **Type**: <class 'str'>
- **Required**: Yes


# ExecutionErrorDetailsTypeDef

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# ExportFilterTypeDef

### name
- **Type**: typing.Literal['ExportResourceType']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# ExportResourceSpecificationTypeDef

### botExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotExportSpecificationTypeDef]

### botLocaleExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleExportSpecificationTypeDef]

### customVocabularyExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyExportSpecificationTypeDef]

### testSetExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetExportSpecificationTypeDef]


# ExportSortByTypeDef

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# ExportSummaryTypeDef

### exportId
- **Type**: typing.Optional[str]

### resourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecificationTypeDef]

### fileFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'LexJson', 'TSV']]

### exportStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# ExternalSourceSettingTypeDef

### grammarSlotTypeSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GrammarSlotTypeSettingTypeDef]


# FailedCustomVocabularyItemTypeDef

### itemId
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['DUPLICATE_INPUT', 'INTERNAL_SERVER_FAILURE', 'RESOURCE_ALREADY_EXISTS', 'RESOURCE_DOES_NOT_EXIST']]


# FulfillmentCodeHookSettingsTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### postFulfillmentStatusSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PostFulfillmentStatusSpecificationTypeDef]

### fulfillmentUpdatesSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentUpdatesSpecificationTypeDef]

### active
- **Type**: typing.Optional[bool]


# FulfillmentStartResponseSpecificationTypeDef

### delayInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupTypeDef]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# FulfillmentUpdateResponseSpecificationTypeDef

### frequencyInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupTypeDef]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# FulfillmentUpdatesSpecificationTypeDef

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### startResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentStartResponseSpecificationTypeDef]

### updateResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentUpdateResponseSpecificationTypeDef]

### timeoutInSeconds
- **Type**: typing.Optional[int]


# GenerateBotElementRequestRequestTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateBotElementResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerationSortByTypeDef

### attribute
- **Type**: typing.Literal['creationStartTime', 'lastUpdatedTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# GenerationSummaryTypeDef

### generationId
- **Type**: typing.Optional[str]

### generationStatus
- **Type**: typing.Optional[typing.Literal['Complete', 'Failed', 'InProgress']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# GenerativeAISettingsTypeDef

### runtimeSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeSettingsTypeDef]

### buildtimeSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BuildtimeSettingsTypeDef]


# GetTestExecutionArtifactsUrlRequestRequestTypeDef

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestExecutionArtifactsUrlResponseTypeDef

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### downloadArtifactsUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrammarSlotTypeSettingTypeDef

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GrammarSlotTypeSourceTypeDef]


# GrammarSlotTypeSourceTypeDef

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# ImageResponseCardTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ButtonTypeDef]]


# ImportFilterTypeDef

### name
- **Type**: typing.Literal['ImportResourceType']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# ImportResourceSpecificationTypeDef

### botImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotImportSpecificationTypeDef]

### botLocaleImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleImportSpecificationTypeDef]

### customVocabularyImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyImportSpecificationTypeDef]

### testSetImportResourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetImportResourceSpecificationTypeDef]


# ImportSortByTypeDef

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# ImportSummaryTypeDef

### importId
- **Type**: typing.Optional[str]

### importedResourceId
- **Type**: typing.Optional[str]

### importedResourceName
- **Type**: typing.Optional[str]

### importStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']]

### mergeStrategy
- **Type**: typing.Optional[typing.Literal['Append', 'FailOnConflict', 'Overwrite']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### importedResourceType
- **Type**: typing.Optional[typing.Literal['Bot', 'BotLocale', 'CustomVocabulary', 'TestSet']]


# InitialResponseSettingTypeDef

### initialResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSettingTypeDef]


# InputContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# InputSessionStateSpecificationTypeDef

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ActiveContextTypeDef]]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeHintsTypeDef]


# IntentClassificationTestResultItemCountsTypeDef

### totalResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### intentMatchResultCounts
- **Type**: typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]
- **Required**: Yes

### speechTranscriptionResultCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]]


# IntentClassificationTestResultItemTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### multiTurnConversation
- **Type**: <class 'bool'>
- **Required**: Yes

### resultCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClassificationTestResultItemCountsTypeDef'>
- **Required**: Yes


# IntentClassificationTestResultsTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClassificationTestResultItemTypeDef]
- **Required**: Yes


# IntentClosingSettingTypeDef

### closingResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### active
- **Type**: typing.Optional[bool]

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]


# IntentConfirmationSettingTypeDef

### promptSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationTypeDef'>
- **Required**: Yes

### declinationResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### active
- **Type**: typing.Optional[bool]

### confirmationResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### confirmationNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### confirmationConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### declinationNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### declinationConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSettingTypeDef]

### elicitationCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ElicitationCodeHookInvocationSettingTypeDef]


# IntentFilterTypeDef

### name
- **Type**: typing.Literal['IntentName']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# IntentLevelSlotResolutionTestResultItemTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### multiTurnConversation
- **Type**: <class 'bool'>
- **Required**: Yes

### slotResolutionResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionTestResultItemTypeDef]
- **Required**: Yes


# IntentLevelSlotResolutionTestResultsTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentLevelSlotResolutionTestResultItemTypeDef]
- **Required**: Yes


# IntentOverrideTypeDef

### name
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueOverrideTypeDef]]


# IntentSortByTypeDef

### attribute
- **Type**: typing.Literal['IntentName', 'LastUpdatedDateTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# IntentStatisticsTypeDef

### discoveredIntentCount
- **Type**: typing.Optional[int]


# IntentSummaryTypeDef

### intentId
- **Type**: typing.Optional[str]

### intentName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parentIntentSignature
- **Type**: typing.Optional[str]

### inputContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContextTypeDef]]

### outputContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContextTypeDef]]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# InvokedIntentSampleTypeDef

### intentName
- **Type**: typing.Optional[str]


# KendraConfigurationTypeDef

### kendraIndex
- **Type**: <class 'str'>
- **Required**: Yes

### queryFilterStringEnabled
- **Type**: typing.Optional[bool]

### queryFilterString
- **Type**: typing.Optional[str]


# LambdaCodeHookTypeDef

### lambdaARN
- **Type**: <class 'str'>
- **Required**: Yes

### codeHookInterfaceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# LexTranscriptFilterTypeDef

### dateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DateRangeFilterTypeDef]


# ListAggregatedUtterancesRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceAggregationDurationTypeDef'>
- **Required**: Yes

### botAliasId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AggregatedUtterancesSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AggregatedUtterancesFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAggregatedUtterancesResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceAggregationDurationTypeDef'>
- **Required**: Yes

### aggregationWindowStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### aggregationWindowEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### aggregationLastRefreshedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### aggregatedUtterancesSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AggregatedUtterancesSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotAliasReplicasRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotAliasReplicasResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasReplicaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasReplicaSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotAliasesRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotAliasesResponseTypeDef

### botAliasSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotLocalesRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotLocalesResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### botLocaleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotRecommendationsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotRecommendationsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotRecommendationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotReplicasRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes


# ListBotReplicasResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### botReplicaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotReplicaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotResourceGenerationsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerationSortByTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotResourceGenerationsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### generationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotVersionReplicasRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionReplicaSortByTypeDef]


# ListBotVersionReplicasResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### botVersionReplicaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionReplicaSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotVersionsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionSortByTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotVersionsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotsRequestRequestTypeDef

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotsResponseTypeDef

### botSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBuiltInIntentsRequestRequestTypeDef

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInIntentSortByTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBuiltInIntentsResponseTypeDef

### builtInIntentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInIntentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBuiltInSlotTypesRequestRequestTypeDef

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInSlotTypeSortByTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBuiltInSlotTypesResponseTypeDef

### builtInSlotTypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInSlotTypeSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomVocabularyItemsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomVocabularyItemsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### customVocabularyItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExportsRequestRequestTypeDef

### botId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### localeId
- **Type**: typing.Optional[str]


# ListExportsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### exportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportsRequestRequestTypeDef

### botId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImportSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ImportFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### localeId
- **Type**: typing.Optional[str]


# ListImportsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### importSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ImportSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIntentMetricsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentMetricTypeDef]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecificationTypeDef]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentGroupBySpecificationTypeDef]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIntentMetricsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentResultTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIntentPathsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### intentPath
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsPathFilterTypeDef]]


# ListIntentPathsResponseTypeDef

### nodeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentNodeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIntentStageMetricsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageMetricTypeDef]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecificationTypeDef]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageGroupBySpecificationTypeDef]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIntentStageMetricsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageResultTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIntentsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIntentsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendedIntentsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRecommendedIntentsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### summaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.RecommendedIntentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSessionAnalyticsDataRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SessionDataSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionAnalyticsDataResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SessionSpecificationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSessionMetricsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionMetricTypeDef]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecificationTypeDef]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionGroupBySpecificationTypeDef]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionMetricsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionResultTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSlotTypesRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSlotTypesResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSlotsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSlotsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### slotSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestExecutionResultItemsRequestRequestTypeDef

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### resultFilterBy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionResultFilterByTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestExecutionResultItemsResponseTypeDef

### testExecutionResults
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionResultItemsTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestExecutionsRequestRequestTypeDef

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionSortByTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestExecutionsResponseTypeDef

### testExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestSetRecordsRequestRequestTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestSetRecordsResponseTypeDef

### testSetRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetTurnRecordTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestSetsRequestRequestTypeDef

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetSortByTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestSetsResponseTypeDef

### testSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUtteranceAnalyticsDataRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceDataSortByTypeDef]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUtteranceAnalyticsDataResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### utterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceSpecificationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUtteranceMetricsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceMetricTypeDef]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecificationTypeDef]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceGroupBySpecificationTypeDef]]

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceAttributeTypeDef]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUtteranceMetricsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceResultTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MessageGroupTypeDef

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MessageTypeDef'>
- **Required**: Yes

### variations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageTypeDef]]


# MessageTypeDef

### plainTextMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PlainTextMessageTypeDef]

### customPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomPayloadTypeDef]

### ssmlMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SSMLMessageTypeDef]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImageResponseCardTypeDef]


# MultipleValuesSettingTypeDef

### allowMultipleValues
- **Type**: typing.Optional[bool]


# NewCustomVocabularyItemTypeDef

### phrase
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### displayAs
- **Type**: typing.Optional[str]


# ObfuscationSettingTypeDef

### obfuscationSettingType
- **Type**: typing.Literal['DefaultObfuscation', 'None']
- **Required**: Yes


# OpensearchConfigurationTypeDef

### domainEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### exactResponse
- **Type**: typing.Optional[bool]

### exactResponseFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExactResponseFieldsTypeDef]

### includeFields
- **Type**: typing.Optional[typing.Sequence[str]]


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


# OverallTestResultItemTypeDef

### multiTurnConversation
- **Type**: <class 'bool'>
- **Required**: Yes

### totalResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### endToEndResultCounts
- **Type**: typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]
- **Required**: Yes

### speechTranscriptionResultCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]]


# OverallTestResultsTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OverallTestResultItemTypeDef]
- **Required**: Yes


# ParentBotNetworkTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes


# PathFormatTypeDef

### objectPrefixes
- **Type**: typing.Optional[typing.List[str]]


# PlainTextMessageTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PostDialogCodeHookInvocationSpecificationTypeDef

### successResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### successNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### successConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### timeoutResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### timeoutNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### timeoutConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]


# PostFulfillmentStatusSpecificationTypeDef

### successResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### timeoutResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### successNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### successConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### timeoutNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### timeoutConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]


# PrincipalTypeDef

### service
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# PromptAttemptSpecificationTypeDef

### allowedInputTypes
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.AllowedInputTypesTypeDef'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]

### audioAndDTMFInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioAndDTMFInputSpecificationTypeDef]

### textInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TextInputSpecificationTypeDef]


# PromptSpecificationTypeDef

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupTypeDef]
- **Required**: Yes

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]

### messageSelectionStrategy
- **Type**: typing.Optional[typing.Literal['Ordered', 'Random']]

### promptAttemptsSpecification
- **Type**: typing.Optional[typing.Mapping[typing.Literal['Initial', 'Retry1', 'Retry2', 'Retry3', 'Retry4', 'Retry5'], aws_resource_validator.pydantic_models.lexv2_models_classes.PromptAttemptSpecificationTypeDef]]


# QnAIntentConfigurationTypeDef

### dataSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DataSourceConfigurationTypeDef]

### bedrockModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecificationTypeDef]


# QnAKendraConfigurationTypeDef

### kendraIndex
- **Type**: <class 'str'>
- **Required**: Yes

### queryFilterStringEnabled
- **Type**: typing.Optional[bool]

### queryFilterString
- **Type**: typing.Optional[str]

### exactResponse
- **Type**: typing.Optional[bool]


# RecommendedIntentSummaryTypeDef

### intentId
- **Type**: typing.Optional[str]

### intentName
- **Type**: typing.Optional[str]

### sampleUtterancesCount
- **Type**: typing.Optional[int]


# RelativeAggregationDurationTypeDef

### timeDimension
- **Type**: typing.Literal['Days', 'Hours', 'Weeks']
- **Required**: Yes

### timeValue
- **Type**: <class 'int'>
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


# ResponseSpecificationTypeDef

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupTypeDef]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# RuntimeHintDetailsTypeDef

### runtimeHintValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeHintValueTypeDef]]

### subSlotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# RuntimeHintValueTypeDef

### phrase
- **Type**: <class 'str'>
- **Required**: Yes


# RuntimeHintsTypeDef

### slotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeHintDetailsTypeDef]]]


# RuntimeSettingsTypeDef

### slotResolutionImprovement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionImprovementSpecificationTypeDef]


# S3BucketLogDestinationTypeDef

### s3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### logPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# S3BucketTranscriptSourceTypeDef

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### transcriptFormat
- **Type**: typing.Literal['Lex']
- **Required**: Yes

### pathFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PathFormatTypeDef]

### transcriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptFilterTypeDef]

### kmsKeyArn
- **Type**: typing.Optional[str]


# SSMLMessageTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SampleUtteranceGenerationSpecificationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bedrockModelSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecificationTypeDef]


# SampleUtteranceTypeDef

### utterance
- **Type**: <class 'str'>
- **Required**: Yes


# SampleValueTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SearchAssociatedTranscriptsRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AssociatedTranscriptFilterTypeDef]
- **Required**: Yes

### searchOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### maxResults
- **Type**: typing.Optional[int]

### nextIndex
- **Type**: typing.Optional[int]


# SearchAssociatedTranscriptsResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextIndex
- **Type**: <class 'int'>
- **Required**: Yes

### associatedTranscripts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AssociatedTranscriptTypeDef]
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SentimentAnalysisSettingsTypeDef

### detectSentiment
- **Type**: <class 'bool'>
- **Required**: Yes


# SessionDataSortByTypeDef

### name
- **Type**: typing.Literal['ConversationStartTime', 'Duration', 'NumberOfTurns']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# SessionSpecificationTypeDef

### botAliasId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### localeId
- **Type**: typing.Optional[str]

### channel
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### conversationStartTime
- **Type**: typing.Optional[datetime.datetime]

### conversationEndTime
- **Type**: typing.Optional[datetime.datetime]

### conversationDurationSeconds
- **Type**: typing.Optional[int]

### conversationEndState
- **Type**: typing.Optional[typing.Literal['Dropped', 'Failure', 'Success']]

### mode
- **Type**: typing.Optional[typing.Literal['DTMF', 'MultiMode', 'Speech', 'Text']]

### numberOfTurns
- **Type**: typing.Optional[int]

### invokedIntentSamples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InvokedIntentSampleTypeDef]]

### originatingRequestId
- **Type**: typing.Optional[str]


# SlotCaptureSettingTypeDef

### captureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### captureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### captureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateTypeDef]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationTypeDef]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSettingTypeDef]

### elicitationCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ElicitationCodeHookInvocationSettingTypeDef]


# SlotDefaultValueSpecificationTypeDef

### defaultValueList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueTypeDef]
- **Required**: Yes


# SlotDefaultValueTypeDef

### defaultValue
- **Type**: <class 'str'>
- **Required**: Yes


# SlotFilterTypeDef

### name
- **Type**: typing.Literal['SlotName']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# SlotPriorityTypeDef

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### slotId
- **Type**: <class 'str'>
- **Required**: Yes


# SlotResolutionImprovementSpecificationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bedrockModelSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecificationTypeDef]


# SlotResolutionSettingTypeDef

### slotResolutionStrategy
- **Type**: typing.Literal['Default', 'EnhancedFallback']
- **Required**: Yes


# SlotResolutionTestResultItemCountsTypeDef

### totalResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### slotMatchResultCounts
- **Type**: typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]
- **Required**: Yes

### speechTranscriptionResultCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]]


# SlotResolutionTestResultItemTypeDef

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### resultCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionTestResultItemCountsTypeDef'>
- **Required**: Yes


# SlotSortByTypeDef

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime', 'SlotName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# SlotSummaryTypeDef

### slotId
- **Type**: typing.Optional[str]

### slotName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### slotConstraint
- **Type**: typing.Optional[typing.Literal['Optional', 'Required']]

### slotTypeId
- **Type**: typing.Optional[str]

### valueElicitationPromptSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationTypeDef]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# SlotTypeFilterTypeDef

### name
- **Type**: typing.Literal['ExternalSourceType', 'SlotTypeName']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operator
- **Type**: typing.Literal['CO', 'EQ']
- **Required**: Yes


# SlotTypeSortByTypeDef

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime', 'SlotTypeName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# SlotTypeStatisticsTypeDef

### discoveredSlotTypeCount
- **Type**: typing.Optional[int]


# SlotTypeSummaryTypeDef

### slotTypeId
- **Type**: typing.Optional[str]

### slotTypeName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### slotTypeCategory
- **Type**: typing.Optional[typing.Literal['Composite', 'Custom', 'Extended', 'ExternalGrammar']]


# SlotTypeValueTypeDef

### sampleValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleValueTypeDef]

### synonyms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleValueTypeDef]]


# SlotValueElicitationSettingTypeDef

### slotConstraint
- **Type**: typing.Literal['Optional', 'Required']
- **Required**: Yes

### defaultValueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueSpecificationTypeDef]

### promptSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationTypeDef]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]]

### waitAndContinueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaitAndContinueSpecificationTypeDef]

### slotCaptureSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotCaptureSettingTypeDef]

### slotResolutionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionSettingTypeDef]


# SlotValueOverrideTypeDef

### shape
- **Type**: typing.Optional[typing.Literal['List', 'Scalar']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueTypeDef]

### values
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]


# SlotValueRegexFilterTypeDef

### pattern
- **Type**: <class 'str'>
- **Required**: Yes


# SlotValueSelectionSettingTypeDef

### resolutionStrategy
- **Type**: typing.Literal['Concatenation', 'OriginalValue', 'TopResolution']
- **Required**: Yes

### regexFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueRegexFilterTypeDef]

### advancedRecognitionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AdvancedRecognitionSettingTypeDef]


# SlotValueTypeDef

### interpretedValue
- **Type**: typing.Optional[str]


# SpecificationsTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotValueElicitationSettingTypeDef'>
- **Required**: Yes


# StartBotRecommendationRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### transcriptSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingTypeDef'>
- **Required**: Yes

### encryptionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSettingTypeDef]


# StartBotRecommendationResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationStatus
- **Type**: typing.Literal['Available', 'Deleted', 'Deleting', 'Downloading', 'Failed', 'Processing', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transcriptSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingTypeDef'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartBotResourceGenerationRequestRequestTypeDef

### generationInputPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# StartBotResourceGenerationResponseTypeDef

### generationInputPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### generationId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### generationStatus
- **Type**: typing.Literal['Complete', 'Failed', 'InProgress']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportRequestRequestTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ImportResourceSpecificationTypeDef'>
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['Append', 'FailOnConflict', 'Overwrite']
- **Required**: Yes

### filePassword
- **Type**: typing.Optional[str]


# StartImportResponseTypeDef

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ImportResourceSpecificationTypeDef'>
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['Append', 'FailOnConflict', 'Overwrite']
- **Required**: Yes

### importStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTestExecutionRequestRequestTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTargetTypeDef'>
- **Required**: Yes

### apiMode
- **Type**: typing.Literal['NonStreaming', 'Streaming']
- **Required**: Yes

### testExecutionModality
- **Type**: typing.Optional[typing.Literal['Audio', 'Text']]


# StartTestExecutionResponseTypeDef

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTargetTypeDef'>
- **Required**: Yes

### apiMode
- **Type**: typing.Literal['NonStreaming', 'Streaming']
- **Required**: Yes

### testExecutionModality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTestSetGenerationRequestRequestTypeDef

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef'>
- **Required**: Yes

### generationDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetGenerationDataSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testSetTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartTestSetGenerationResponseTypeDef

### testSetGenerationId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testSetGenerationStatus
- **Type**: typing.Literal['Failed', 'Generating', 'Pending', 'Ready']
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef'>
- **Required**: Yes

### generationDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetGenerationDataSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### testSetTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StillWaitingResponseSpecificationTypeDef

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupTypeDef]
- **Required**: Yes

### frequencyInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### timeoutInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# StopBotRecommendationRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# StopBotRecommendationResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationStatus
- **Type**: typing.Literal['Available', 'Deleted', 'Deleting', 'Downloading', 'Failed', 'Processing', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubSlotSettingTypeDef

### expression
- **Type**: typing.Optional[str]

### slotSpecifications
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.SpecificationsTypeDef]]


# SubSlotTypeCompositionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# SubSlotValueElicitationSettingTypeDef

### promptSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationTypeDef'>
- **Required**: Yes

### defaultValueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueSpecificationTypeDef]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]]

### waitAndContinueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaitAndContinueSpecificationTypeDef]


# TagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestExecutionResultFilterByTypeDef

### resultTypeFilter
- **Type**: typing.Literal['ConversationLevelTestResults', 'IntentClassificationTestResults', 'OverallTestResults', 'SlotResolutionTestResults', 'UtteranceLevelResults']
- **Required**: Yes

### conversationLevelTestResultsFilterBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelTestResultsFilterByTypeDef]


# TestExecutionResultItemsTypeDef

### overallTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.OverallTestResultsTypeDef]

### conversationLevelTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelTestResultsTypeDef]

### intentClassificationTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClassificationTestResultsTypeDef]

### intentLevelSlotResolutionTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentLevelSlotResolutionTestResultsTypeDef]

### utteranceLevelTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceLevelTestResultsTypeDef]


# TestExecutionSortByTypeDef

### attribute
- **Type**: typing.Literal['CreationDateTime', 'TestSetName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# TestExecutionSummaryTypeDef

### testExecutionId
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### testExecutionStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping', 'Waiting']]

### testSetId
- **Type**: typing.Optional[str]

### testSetName
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTargetTypeDef]

### apiMode
- **Type**: typing.Optional[typing.Literal['NonStreaming', 'Streaming']]

### testExecutionModality
- **Type**: typing.Optional[typing.Literal['Audio', 'Text']]


# TestExecutionTargetTypeDef

### botAliasTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasTestExecutionTargetTypeDef]


# TestSetDiscrepancyErrorsTypeDef

### intentDiscrepancies
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetIntentDiscrepancyItemTypeDef]
- **Required**: Yes

### slotDiscrepancies
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetSlotDiscrepancyItemTypeDef]
- **Required**: Yes


# TestSetDiscrepancyReportBotAliasTargetTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetDiscrepancyReportResourceTargetTypeDef

### botAliasTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportBotAliasTargetTypeDef]


# TestSetExportSpecificationTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetGenerationDataSourceTypeDef

### conversationLogsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogsDataSourceTypeDef]


# TestSetImportInputLocationTypeDef

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetImportResourceSpecificationTypeDef

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef'>
- **Required**: Yes

### importInputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetImportInputLocationTypeDef'>
- **Required**: Yes

### modality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testSetTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TestSetIntentDiscrepancyItemTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetSlotDiscrepancyItemTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetSortByTypeDef

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime', 'TestSetName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# TestSetStorageLocationTypeDef

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# TestSetSummaryTypeDef

### testSetId
- **Type**: typing.Optional[str]

### testSetName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### modality
- **Type**: typing.Optional[typing.Literal['Audio', 'Text']]

### status
- **Type**: typing.Optional[typing.Literal['Deleting', 'Importing', 'PendingAnnotation', 'Ready', 'ValidationError']]

### roleArn
- **Type**: typing.Optional[str]

### numTurns
- **Type**: typing.Optional[int]

### storageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# TestSetTurnRecordTypeDef

### recordNumber
- **Type**: <class 'int'>
- **Required**: Yes

### turnSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TurnSpecificationTypeDef'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]

### turnNumber
- **Type**: typing.Optional[int]


# TestSetTurnResultTypeDef

### agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AgentTurnResultTypeDef]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnResultTypeDef]


# TextInputSpecificationTypeDef

### startTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes


# TextLogDestinationTypeDef

### cloudWatch
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CloudWatchLogGroupLogDestinationTypeDef'>
- **Required**: Yes


# TextLogSettingTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TextLogDestinationTypeDef'>
- **Required**: Yes

### selectiveLoggingEnabled
- **Type**: typing.Optional[bool]


# TranscriptFilterTypeDef

### lexTranscriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.LexTranscriptFilterTypeDef]


# TranscriptSourceSettingTypeDef

### s3BucketTranscriptSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.S3BucketTranscriptSourceTypeDef]


# TurnSpecificationTypeDef

### agentTurn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AgentTurnSpecificationTypeDef]

### userTurn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnSpecificationTypeDef]


# UntagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBotAliasRequestRequestTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### botAliasLocaleSettings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettingsTypeDef]]

### conversationLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsTypeDef]

### sentimentAnalysisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettingsTypeDef]


# UpdateBotAliasResponseTypeDef

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasLocaleSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettingsTypeDef]
- **Required**: Yes

### conversationLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsTypeDef'>
- **Required**: Yes

### sentimentAnalysisSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettingsTypeDef'>
- **Required**: Yes

### botAliasStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed']
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBotLocaleRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### voiceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettingsTypeDef]

### generativeAISettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettingsTypeDef]


# UpdateBotLocaleResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### localeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidenceThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### voiceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettingsTypeDef'>
- **Required**: Yes

### botLocaleStatus
- **Type**: typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### recommendedActions
- **Type**: typing.List[str]
- **Required**: Yes

### generativeAISettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBotRecommendationRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSettingTypeDef'>
- **Required**: Yes


# UpdateBotRecommendationResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### botRecommendationStatus
- **Type**: typing.Literal['Available', 'Deleted', 'Deleting', 'Downloading', 'Failed', 'Processing', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### botRecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transcriptSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingTypeDef'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBotRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### botType
- **Type**: typing.Optional[typing.Literal['Bot', 'BotNetwork']]

### botMembers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMemberTypeDef]]


# UpdateBotResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacyTypeDef'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### botType
- **Type**: typing.Literal['Bot', 'BotNetwork']
- **Required**: Yes

### botMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateExportRequestRequestTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### filePassword
- **Type**: typing.Optional[str]


# UpdateExportResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecificationTypeDef'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['CSV', 'LexJson', 'TSV']
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIntentRequestRequestTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parentIntentSignature
- **Type**: typing.Optional[str]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]]

### dialogCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettingsTypeDef]

### fulfillmentCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsTypeDef]

### slotPriorities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotPriorityTypeDef]]

### intentConfirmationSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingTypeDef]

### intentClosingSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingTypeDef]

### inputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContextTypeDef]]

### outputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContextTypeDef]]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfigurationTypeDef]

### initialResponseSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingTypeDef]

### qnAIntentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationTypeDef]


# UpdateIntentResponseTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### parentIntentSignature
- **Type**: <class 'str'>
- **Required**: Yes

### sampleUtterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceTypeDef]
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettingsTypeDef'>
- **Required**: Yes

### fulfillmentCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsTypeDef'>
- **Required**: Yes

### slotPriorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotPriorityTypeDef]
- **Required**: Yes

### intentConfirmationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingTypeDef'>
- **Required**: Yes

### intentClosingSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingTypeDef'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContextTypeDef]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContextTypeDef]
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfigurationTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### initialResponseSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingTypeDef'>
- **Required**: Yes

### qnAIntentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResourcePolicyRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### expectedRevisionId
- **Type**: typing.Optional[str]


# UpdateResourcePolicyResponseTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSlotRequestRequestTypeDef

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slotTypeId
- **Type**: typing.Optional[str]

### obfuscationSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSettingTypeDef]

### multipleValuesSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSettingTypeDef]

### subSlotSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingTypeDef]


# UpdateSlotResponseTypeDef

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingTypeDef'>
- **Required**: Yes

### obfuscationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSettingTypeDef'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### multipleValuesSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSettingTypeDef'>
- **Required**: Yes

### subSlotSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSlotTypeRequestRequestTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### slotTypeValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueTypeDef]]

### valueSelectionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSettingTypeDef]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### externalSourceSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSettingTypeDef]

### compositeSlotTypeSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingTypeDef]


# UpdateSlotTypeResponseTypeDef

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueTypeDef]
- **Required**: Yes

### valueSelectionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSettingTypeDef'>
- **Required**: Yes

### parentSlotTypeSignature
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### externalSourceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSettingTypeDef'>
- **Required**: Yes

### compositeSlotTypeSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTestSetRequestRequestTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateTestSetResponseTypeDef

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### modality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleting', 'Importing', 'PendingAnnotation', 'Ready', 'ValidationError']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### numTurns
- **Type**: <class 'int'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocationTypeDef'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserTurnInputSpecificationTypeDef

### utteranceInput
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceInputSpecificationTypeDef'>
- **Required**: Yes

### requestAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.InputSessionStateSpecificationTypeDef]


# UserTurnIntentOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnSlotOutputTypeDef]]


# UserTurnOutputSpecificationTypeDef

### intent
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnIntentOutputTypeDef'>
- **Required**: Yes

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ActiveContextTypeDef]]

### transcript
- **Type**: typing.Optional[str]


# UserTurnResultTypeDef

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnInputSpecificationTypeDef'>
- **Required**: Yes

### expectedOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnOutputSpecificationTypeDef'>
- **Required**: Yes

### actualOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnOutputSpecificationTypeDef]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExecutionErrorDetailsTypeDef]

### endToEndResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]

### intentMatchResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]

### slotMatchResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]

### speechTranscriptionResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]

### conversationLevelResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelResultDetailTypeDef]


# UserTurnSlotOutputTypeDef

### value
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# UserTurnSpecificationTypeDef

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnInputSpecificationTypeDef'>
- **Required**: Yes

### expected
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnOutputSpecificationTypeDef'>
- **Required**: Yes


# UtteranceAggregationDurationTypeDef

### relativeAggregationDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.RelativeAggregationDurationTypeDef'>
- **Required**: Yes


# UtteranceAudioInputSpecificationTypeDef

### audioFileS3Location
- **Type**: <class 'str'>
- **Required**: Yes


# UtteranceBotResponseTypeDef

### content
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImageResponseCardTypeDef]


# UtteranceDataSortByTypeDef

### name
- **Type**: typing.Literal['UtteranceTimestamp']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# UtteranceInputSpecificationTypeDef

### textInput
- **Type**: typing.Optional[str]

### audioInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceAudioInputSpecificationTypeDef]


# UtteranceLevelTestResultItemTypeDef

### recordNumber
- **Type**: <class 'int'>
- **Required**: Yes

### turnResult
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetTurnResultTypeDef'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]


# UtteranceLevelTestResultsTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceLevelTestResultItemTypeDef]
- **Required**: Yes


# UtteranceSpecificationTypeDef

### botAliasId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### localeId
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### channel
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[typing.Literal['DTMF', 'MultiMode', 'Speech', 'Text']]

### conversationStartTime
- **Type**: typing.Optional[datetime.datetime]

### conversationEndTime
- **Type**: typing.Optional[datetime.datetime]

### utterance
- **Type**: typing.Optional[str]

### utteranceTimestamp
- **Type**: typing.Optional[datetime.datetime]

### audioVoiceDurationMillis
- **Type**: typing.Optional[int]

### utteranceUnderstood
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[str]

### outputType
- **Type**: typing.Optional[str]

### associatedIntentName
- **Type**: typing.Optional[str]

### associatedSlotName
- **Type**: typing.Optional[str]

### intentState
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'FulfillmentInProgress', 'InProgress', 'ReadyForFulfillment', 'Waiting']]

### dialogActionType
- **Type**: typing.Optional[str]

### botResponseAudioVoiceId
- **Type**: typing.Optional[str]

### slotsFilledInSession
- **Type**: typing.Optional[str]

### utteranceRequestId
- **Type**: typing.Optional[str]

### botResponses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceBotResponseTypeDef]]


# VoiceSettingsTypeDef

### voiceId
- **Type**: <class 'str'>
- **Required**: Yes

### engine
- **Type**: typing.Optional[typing.Literal['neural', 'standard']]


# WaitAndContinueSpecificationTypeDef

### waitingResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef'>
- **Required**: Yes

### continueResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationTypeDef'>
- **Required**: Yes

### stillWaitingResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.StillWaitingResponseSpecificationTypeDef]

### active
- **Type**: typing.Optional[bool]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


