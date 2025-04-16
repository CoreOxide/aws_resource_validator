# Lexv2 Models Classes

# ActiveContext

### name
- **Type**: <class 'str'>
- **Required**: Yes


# AdvancedRecognitionSetting

### audioRecognitionStrategy
- **Type**: typing.Optional[typing.Literal['UseSlotValuesAsCustomVocabulary']]


# AgentTurnResult

### expectedAgentPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### actualAgentPrompt
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExecutionErrorDetails]

### actualElicitedSlot
- **Type**: typing.Optional[str]

### actualIntent
- **Type**: typing.Optional[str]


# AgentTurnSpecification

### agentPrompt
- **Type**: <class 'str'>
- **Required**: Yes


# AggregatedUtterancesFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregatedUtterancesSortBy

### attribute
- **Type**: typing.Literal['HitCount', 'MissedCount']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# AggregatedUtterancesSummary

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


# AllowedInputTypes

### allowAudioInput
- **Type**: <class 'bool'>
- **Required**: Yes

### allowDTMFInput
- **Type**: <class 'bool'>
- **Required**: Yes


# AnalyticsBinBySpecification

### name
- **Type**: typing.Literal['ConversationStartTime', 'UtteranceTimestamp']
- **Required**: Yes

### interval
- **Type**: typing.Literal['OneDay', 'OneHour']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsBinKey

### name
- **Type**: typing.Optional[typing.Literal['ConversationStartTime', 'UtteranceTimestamp']]

### value
- **Type**: typing.Optional[int]


# AnalyticsIntentFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyticsIntentGroupByKey

### name
- **Type**: typing.Optional[typing.Literal['IntentEndState', 'IntentLevel', 'IntentName']]

### value
- **Type**: typing.Optional[str]


# AnalyticsIntentGroupBySpecification

### name
- **Type**: typing.Literal['IntentEndState', 'IntentLevel', 'IntentName']
- **Required**: Yes


# AnalyticsIntentMetric

### name
- **Type**: typing.Literal['Count', 'Dropped', 'Failure', 'Success', 'Switched']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsIntentMetricResult

### name
- **Type**: typing.Optional[typing.Literal['Count', 'Dropped', 'Failure', 'Success', 'Switched']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsIntentNodeSummary

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


# AnalyticsIntentResult

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKey]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentGroupByKey]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentMetricResult]]


# AnalyticsIntentStageFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyticsIntentStageGroupByKey

### name
- **Type**: typing.Optional[typing.Literal['IntentStageName', 'SwitchedToIntent']]

### value
- **Type**: typing.Optional[str]


# AnalyticsIntentStageGroupBySpecification

### name
- **Type**: typing.Literal['IntentStageName', 'SwitchedToIntent']
- **Required**: Yes


# AnalyticsIntentStageMetric

### name
- **Type**: typing.Literal['Count', 'Dropped', 'Failed', 'Retry', 'Success']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsIntentStageMetricResult

### name
- **Type**: typing.Optional[typing.Literal['Count', 'Dropped', 'Failed', 'Retry', 'Success']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsIntentStageResult

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKey]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageGroupByKey]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageMetricResult]]


# AnalyticsPathFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyticsSessionFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyticsSessionGroupByKey

### name
- **Type**: typing.Optional[typing.Literal['ConversationEndState', 'LocaleId']]

### value
- **Type**: typing.Optional[str]


# AnalyticsSessionGroupBySpecification

### name
- **Type**: typing.Literal['ConversationEndState', 'LocaleId']
- **Required**: Yes


# AnalyticsSessionMetric

### name
- **Type**: typing.Literal['Concurrency', 'Count', 'Dropped', 'Duration', 'Failure', 'Success', 'TurnsPerConversation']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsSessionMetricResult

### name
- **Type**: typing.Optional[typing.Literal['Concurrency', 'Count', 'Dropped', 'Duration', 'Failure', 'Success', 'TurnsPerConversation']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsSessionResult

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKey]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionGroupByKey]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionMetricResult]]


# AnalyticsUtteranceAttribute

### name
- **Type**: typing.Literal['LastUsedIntent']
- **Required**: Yes


# AnalyticsUtteranceAttributeResult

### lastUsedIntent
- **Type**: typing.Optional[str]


# AnalyticsUtteranceFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyticsUtteranceGroupByKey

### name
- **Type**: typing.Optional[typing.Literal['UtteranceState', 'UtteranceText']]

### value
- **Type**: typing.Optional[str]


# AnalyticsUtteranceGroupBySpecification

### name
- **Type**: typing.Literal['UtteranceState', 'UtteranceText']
- **Required**: Yes


# AnalyticsUtteranceMetric

### name
- **Type**: typing.Literal['Count', 'Detected', 'Missed', 'UtteranceTimestamp']
- **Required**: Yes

### statistic
- **Type**: typing.Literal['Avg', 'Max', 'Sum']
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# AnalyticsUtteranceMetricResult

### name
- **Type**: typing.Optional[typing.Literal['Count', 'Detected', 'Missed', 'UtteranceTimestamp']]

### statistic
- **Type**: typing.Optional[typing.Literal['Avg', 'Max', 'Sum']]

### value
- **Type**: typing.Optional[float]


# AnalyticsUtteranceResult

### binKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinKey]]

### groupByKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceGroupByKey]]

### metricsResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceMetricResult]]

### attributeResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceAttributeResult]]


# AssociatedTranscript

### transcript
- **Type**: typing.Optional[str]


# AssociatedTranscriptFilter

### name
- **Type**: typing.Literal['IntentId', 'SlotTypeId']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AudioAndDTMFInputSpecification

### startTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes

### audioSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioSpecification]

### dtmfSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DTMFSpecification]


# AudioLogDestination

### s3Bucket
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.S3BucketLogDestination'>
- **Required**: Yes


# AudioLogSetting

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.AudioLogDestination'>
- **Required**: Yes

### selectiveLoggingEnabled
- **Type**: typing.Optional[bool]


# AudioSpecification

### maxLengthMs
- **Type**: <class 'int'>
- **Required**: Yes

### endTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateCustomVocabularyItemRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.NewCustomVocabularyItem]
- **Required**: Yes


# BatchCreateCustomVocabularyItemResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.FailedCustomVocabularyItem]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteCustomVocabularyItemRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyEntryId]
- **Required**: Yes


# BatchDeleteCustomVocabularyItemResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.FailedCustomVocabularyItem]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateCustomVocabularyItemRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItem]
- **Required**: Yes


# BatchUpdateCustomVocabularyItemResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.FailedCustomVocabularyItem]
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# BedrockGuardrailConfiguration

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# BedrockKnowledgeStoreConfiguration

### bedrockKnowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### exactResponse
- **Type**: typing.Optional[bool]

### exactResponseFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockKnowledgeStoreExactResponseFields]


# BedrockKnowledgeStoreExactResponseFields

### answerField
- **Type**: typing.Optional[str]


# BedrockModelSpecification

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockGuardrailConfiguration]

### traceStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### customPrompt
- **Type**: typing.Optional[str]


# BotAliasHistoryEvent

### botVersion
- **Type**: typing.Optional[str]

### startDate
- **Type**: typing.Optional[datetime.datetime]

### endDate
- **Type**: typing.Optional[datetime.datetime]


# BotAliasLocaleSettings

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### codeHookSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CodeHookSpecification]


# BotAliasReplicaSummary

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


# BotAliasSummary

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


# BotAliasTestExecutionTarget

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# BotExportSpecification

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes


# BotFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BotImportSpecification

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### botTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### testBotAliasTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# BotImportSpecificationOutput

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### botTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### testBotAliasTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BotLocaleExportSpecification

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# BotLocaleFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BotLocaleHistoryEvent

### event
- **Type**: <class 'str'>
- **Required**: Yes

### eventDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BotLocaleImportSpecification

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettings]


# BotLocaleSortBy

### attribute
- **Type**: typing.Literal['BotLocaleName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotLocaleSummary

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


# BotMember

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


# BotRecommendationResultStatistics

### intents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentStatistics]

### slotTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeStatistics]


# BotRecommendationResults

### botLocaleExportUrl
- **Type**: typing.Optional[str]

### associatedTranscriptsUrl
- **Type**: typing.Optional[str]

### statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotRecommendationResultStatistics]


# BotRecommendationSummary

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


# BotReplicaSummary

### replicaRegion
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### botReplicaStatus
- **Type**: typing.Optional[typing.Literal['Deleting', 'Enabled', 'Enabling', 'Failed']]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# BotSortBy

### attribute
- **Type**: typing.Literal['BotName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotSummary

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


# BotVersionLocaleDetails

### sourceBotVersion
- **Type**: <class 'str'>
- **Required**: Yes


# BotVersionReplicaSortBy

### attribute
- **Type**: typing.Literal['BotVersion']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotVersionReplicaSummary

### botVersion
- **Type**: typing.Optional[str]

### botVersionReplicationStatus
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleting', 'Failed']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# BotVersionSortBy

### attribute
- **Type**: typing.Literal['BotVersion']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BotVersionSummary

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


# BuildBotLocaleRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# BuildBotLocaleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# BuildtimeSettings

### descriptiveBotBuilder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DescriptiveBotBuilderSpecification]

### sampleUtteranceGeneration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtteranceGenerationSpecification]


# BuiltInIntentSortBy

### attribute
- **Type**: typing.Literal['IntentSignature']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BuiltInIntentSummary

### intentSignature
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# BuiltInSlotTypeSortBy

### attribute
- **Type**: typing.Literal['SlotTypeSignature']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# BuiltInSlotTypeSummary

### slotTypeSignature
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# Button

### text
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLogGroupLogDestination

### cloudWatchLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### logPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# CodeHookSpecification

### lambdaCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.LambdaCodeHook'>
- **Required**: Yes


# CompositeSlotTypeSetting

### subSlots
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotTypeComposition]]


# CompositeSlotTypeSettingOutput

### subSlots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotTypeComposition]]


# CompositeSlotTypeSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Condition

### expressionString
- **Type**: <class 'str'>
- **Required**: Yes


# ConditionalBranch

### name
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Condition'>
- **Required**: Yes

### nextStep
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState'>
- **Required**: Yes

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]


# ConditionalBranchOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Condition'>
- **Required**: Yes

### nextStep
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput'>
- **Required**: Yes

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]


# ConditionalSpecification

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### conditionalBranches
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalBranch]
- **Required**: Yes

### defaultBranch
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DefaultConditionalBranch'>
- **Required**: Yes


# ConditionalSpecificationOutput

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### conditionalBranches
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalBranchOutput]
- **Required**: Yes

### defaultBranch
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DefaultConditionalBranchOutput'>
- **Required**: Yes


# ConversationLevelIntentClassificationResultItem

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### matchResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes


# ConversationLevelResultDetail

### endToEndResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes

### speechTranscriptionResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]


# ConversationLevelSlotResolutionResultItem

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### matchResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes


# ConversationLevelTestResultItem

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### endToEndResult
- **Type**: typing.Literal['ExecutionError', 'Matched', 'Mismatched']
- **Required**: Yes

### intentClassificationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelIntentClassificationResultItem]
- **Required**: Yes

### slotResolutionResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelSlotResolutionResultItem]
- **Required**: Yes

### speechTranscriptionResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]


# ConversationLevelTestResults

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelTestResultItem]
- **Required**: Yes


# ConversationLevelTestResultsFilterBy

### endToEndResult
- **Type**: typing.Optional[typing.Literal['ExecutionError', 'Matched', 'Mismatched']]


# ConversationLogSettings

### textLogSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.TextLogSetting]]

### audioLogSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioLogSetting]]


# ConversationLogSettingsOutput

### textLogSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TextLogSetting]]

### audioLogSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioLogSetting]]


# ConversationLogSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversationLogsDataSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversationLogsDataSourceFilterBy

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### inputMode
- **Type**: typing.Literal['Speech', 'Text']
- **Required**: Yes


# ConversationLogsDataSourceFilterByOutput

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputMode
- **Type**: typing.Literal['Speech', 'Text']
- **Required**: Yes


# ConversationLogsDataSourceOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateBotAliasRequest

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettings]]

### conversationLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsUnion]

### sentimentAnalysisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettings]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateBotAliasResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettings]
- **Required**: Yes

### conversationLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsOutput'>
- **Required**: Yes

### sentimentAnalysisSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBotLocaleRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettings]

### generativeAISettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettings]


# CreateBotLocaleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettings'>
- **Required**: Yes

### botLocaleStatus
- **Type**: typing.Literal['Building', 'Built', 'Creating', 'Deleting', 'Failed', 'Importing', 'NotBuilt', 'Processing', 'ReadyExpressTesting']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### generativeAISettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBotReplicaRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBotReplicaResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBotRequest

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataPrivacy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMember]]


# CreateBotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBotVersionRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersionLocaleSpecification
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionLocaleDetails]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateBotVersionResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionLocaleDetails]
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExportRequest

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecification'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['CSV', 'LexJson', 'TSV']
- **Required**: Yes

### filePassword
- **Type**: typing.Optional[str]


# CreateExportResponse

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecification'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntentRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]]

### dialogCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettings]

### fulfillmentCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsUnion]

### intentConfirmationSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingUnion]

### intentClosingSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingUnion]

### inputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContext]]

### outputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContext]]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfiguration]

### initialResponseSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingUnion]

### qnAIntentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationUnion]


# CreateIntentResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettings'>
- **Required**: Yes

### fulfillmentCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsOutput'>
- **Required**: Yes

### intentConfirmationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingOutput'>
- **Required**: Yes

### intentClosingSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingOutput'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContext]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContext]
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingOutput'>
- **Required**: Yes

### qnAIntentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# CreateResourcePolicyResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourcePolicyStatementRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.Principal]
- **Required**: Yes

### action
- **Type**: typing.Sequence[str]
- **Required**: Yes

### condition
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]

### expectedRevisionId
- **Type**: typing.Optional[str]


# CreateResourcePolicyStatementResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSlotRequest

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingUnion'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSetting]

### multipleValuesSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSetting]

### subSlotSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingUnion]


# CreateSlotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingOutput'>
- **Required**: Yes

### obfuscationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSetting'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSetting'>
- **Required**: Yes

### subSlotSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSlotTypeRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueUnion]]

### valueSelectionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSetting]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### externalSourceSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSetting]

### compositeSlotTypeSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingUnion]


# CreateSlotTypeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueOutput]
- **Required**: Yes

### valueSelectionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSetting'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSetting'>
- **Required**: Yes

### compositeSlotTypeSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTestSetDiscrepancyReportRequest

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportResourceTarget'>
- **Required**: Yes


# CreateTestSetDiscrepancyReportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportResourceTarget'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUploadUrlResponse

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# CustomPayload

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyEntryId

### itemId
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyExportSpecification

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyImportSpecification

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# CustomVocabularyItem

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


# DTMFSpecification

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


# DataPrivacy

### childDirected
- **Type**: <class 'bool'>
- **Required**: Yes


# DataSourceConfiguration

### opensearchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.OpensearchConfiguration]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAKendraConfiguration]

### bedrockKnowledgeStoreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockKnowledgeStoreConfiguration]


# DataSourceConfigurationOutput

### opensearchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.OpensearchConfigurationOutput]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAKendraConfiguration]

### bedrockKnowledgeStoreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockKnowledgeStoreConfiguration]


# DateRangeFilter

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes


# DateRangeFilterOutput

### startDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DefaultConditionalBranch

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]


# DefaultConditionalBranchOutput

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]


# DeleteBotAliasRequest

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteBotAliasResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBotLocaleRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotLocaleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBotReplicaRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBotReplicaResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBotRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteBotResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botStatus
- **Type**: typing.Literal['Available', 'Creating', 'Deleting', 'Failed', 'Importing', 'Inactive', 'Updating', 'Versioning']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBotVersionRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteBotVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomVocabularyRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteExportRequest

### exportId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExportResponse

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteImportRequest

### importId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportResponse

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### importStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIntentRequest

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


# DeleteResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### expectedRevisionId
- **Type**: typing.Optional[str]


# DeleteResourcePolicyResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyStatementRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### expectedRevisionId
- **Type**: typing.Optional[str]


# DeleteResourcePolicyStatementResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSlotRequest

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


# DeleteSlotTypeRequest

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


# DeleteTestSetRequest

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUtterancesRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]


# DescribeBotAliasRequest

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotAliasRequestWait

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeBotAliasResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettings]
- **Required**: Yes

### conversationLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsOutput'>
- **Required**: Yes

### sentimentAnalysisSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettings'>
- **Required**: Yes

### botAliasHistoryEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasHistoryEvent]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ParentBotNetwork]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBotLocaleRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotLocaleRequestWait

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
- **Type**: <class 'NoneType'>


# DescribeBotLocaleRequestWaitExtra

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
- **Type**: <class 'NoneType'>


# DescribeBotLocaleRequestWaitExtraExtra

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
- **Type**: <class 'NoneType'>


# DescribeBotLocaleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettings'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleHistoryEvent]
- **Required**: Yes

### recommendedActions
- **Type**: typing.List[str]
- **Required**: Yes

### generativeAISettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBotRecommendationRequest

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


# DescribeBotRecommendationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingOutput'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSetting'>
- **Required**: Yes

### botRecommendationResults
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.BotRecommendationResults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBotReplicaRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### replicaRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotReplicaResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBotRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotRequestWait

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeBotResourceGenerationRequest

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


# DescribeBotResourceGenerationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMember]
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBotVersionRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBotVersionRequestWait

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeBotVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ParentBotNetwork]
- **Required**: Yes

### botType
- **Type**: typing.Literal['Bot', 'BotNetwork']
- **Required**: Yes

### botMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomVocabularyMetadataRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomVocabularyMetadataResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExportRequest

### exportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExportRequestWait

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeExportResponse

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecification'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImportRequest

### importId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeImportRequestWait

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImportResponse

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ImportResourceSpecificationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIntentRequest

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


# DescribeIntentResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettings'>
- **Required**: Yes

### fulfillmentCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsOutput'>
- **Required**: Yes

### slotPriorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotPriority]
- **Required**: Yes

### intentConfirmationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingOutput'>
- **Required**: Yes

### intentClosingSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingOutput'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContext]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContext]
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingOutput'>
- **Required**: Yes

### qnAIntentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSlotRequest

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


# DescribeSlotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingOutput'>
- **Required**: Yes

### obfuscationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSetting'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSetting'>
- **Required**: Yes

### subSlotSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSlotTypeRequest

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


# DescribeSlotTypeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueOutput]
- **Required**: Yes

### valueSelectionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSetting'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSetting'>
- **Required**: Yes

### compositeSlotTypeSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTestExecutionRequest

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestExecutionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTarget'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTestSetDiscrepancyReportRequest

### testSetDiscrepancyReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestSetDiscrepancyReportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportResourceTarget'>
- **Required**: Yes

### testSetDiscrepancyReportStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### lastUpdatedDataTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testSetDiscrepancyTopErrors
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyErrors'>
- **Required**: Yes

### testSetDiscrepancyRawOutputUrl
- **Type**: <class 'str'>
- **Required**: Yes

### failureReasons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTestSetGenerationRequest

### testSetGenerationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestSetGenerationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### generationDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetGenerationDataSourceOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTestSetRequest

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTestSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# DescriptiveBotBuilderSpecification

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bedrockModelSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecification]


# DialogAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DialogCodeHookInvocationSetting

### enableCodeHookInvocation
- **Type**: <class 'bool'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### postCodeHookSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PostDialogCodeHookInvocationSpecification'>
- **Required**: Yes

### invocationLabel
- **Type**: typing.Optional[str]


# DialogCodeHookInvocationSettingOutput

### enableCodeHookInvocation
- **Type**: <class 'bool'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### postCodeHookSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PostDialogCodeHookInvocationSpecificationOutput'>
- **Required**: Yes

### invocationLabel
- **Type**: typing.Optional[str]


# DialogCodeHookSettings

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# DialogState

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogAction]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentOverride]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DialogStateOutput

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogAction]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentOverrideOutput]

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ElicitationCodeHookInvocationSetting

### enableCodeHookInvocation
- **Type**: <class 'bool'>
- **Required**: Yes

### invocationLabel
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionSetting

### kmsKeyArn
- **Type**: typing.Optional[str]

### botLocaleExportPassword
- **Type**: typing.Optional[str]

### associatedTranscriptsPassword
- **Type**: typing.Optional[str]


# ExactResponseFields

### questionField
- **Type**: <class 'str'>
- **Required**: Yes

### answerField
- **Type**: <class 'str'>
- **Required**: Yes


# ExecutionErrorDetails

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# ExportFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportResourceSpecification

### botExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotExportSpecification]

### botLocaleExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleExportSpecification]

### customVocabularyExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyExportSpecification]

### testSetExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetExportSpecification]


# ExportSortBy

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# ExportSummary

### exportId
- **Type**: typing.Optional[str]

### resourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecification]

### fileFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'LexJson', 'TSV']]

### exportStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# ExternalSourceSetting

### grammarSlotTypeSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GrammarSlotTypeSetting]


# FailedCustomVocabularyItem

### itemId
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['DUPLICATE_INPUT', 'INTERNAL_SERVER_FAILURE', 'RESOURCE_ALREADY_EXISTS', 'RESOURCE_DOES_NOT_EXIST']]


# FulfillmentCodeHookSettings

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### postFulfillmentStatusSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PostFulfillmentStatusSpecification]

### fulfillmentUpdatesSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentUpdatesSpecification]

### active
- **Type**: typing.Optional[bool]


# FulfillmentCodeHookSettingsOutput

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### postFulfillmentStatusSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PostFulfillmentStatusSpecificationOutput]

### fulfillmentUpdatesSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentUpdatesSpecificationOutput]

### active
- **Type**: typing.Optional[bool]


# FulfillmentCodeHookSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FulfillmentStartResponseSpecification

### delayInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroup]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# FulfillmentStartResponseSpecificationOutput

### delayInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### messageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupOutput]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# FulfillmentUpdateResponseSpecification

### frequencyInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroup]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# FulfillmentUpdateResponseSpecificationOutput

### frequencyInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### messageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupOutput]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# FulfillmentUpdatesSpecification

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### startResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentStartResponseSpecification]

### updateResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentUpdateResponseSpecification]

### timeoutInSeconds
- **Type**: typing.Optional[int]


# FulfillmentUpdatesSpecificationOutput

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### startResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentStartResponseSpecificationOutput]

### updateResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentUpdateResponseSpecificationOutput]

### timeoutInSeconds
- **Type**: typing.Optional[int]


# GenerateBotElementRequest

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


# GenerateBotElementResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# GenerationSortBy

### attribute
- **Type**: typing.Literal['creationStartTime', 'lastUpdatedTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# GenerationSummary

### generationId
- **Type**: typing.Optional[str]

### generationStatus
- **Type**: typing.Optional[typing.Literal['Complete', 'Failed', 'InProgress']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# GenerativeAISettings

### runtimeSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeSettings]

### buildtimeSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BuildtimeSettings]


# GetTestExecutionArtifactsUrlRequest

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestExecutionArtifactsUrlResponse

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### downloadArtifactsUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# GrammarSlotTypeSetting

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GrammarSlotTypeSource]


# GrammarSlotTypeSource

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# ImageResponseCard

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.Button]]


# ImageResponseCardOutput

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.Button]]


# ImportFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportResourceSpecification

### botImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotImportSpecification]

### botLocaleImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleImportSpecification]

### customVocabularyImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyImportSpecification]

### testSetImportResourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetImportResourceSpecification]


# ImportResourceSpecificationOutput

### botImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotImportSpecificationOutput]

### botLocaleImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleImportSpecification]

### customVocabularyImportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyImportSpecification]

### testSetImportResourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetImportResourceSpecificationOutput]


# ImportResourceSpecificationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportSortBy

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# ImportSummary

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


# InitialResponseSetting

### initialResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSetting]


# InitialResponseSettingOutput

### initialResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSettingOutput]


# InitialResponseSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputContext

### name
- **Type**: <class 'str'>
- **Required**: Yes


# InputSessionStateSpecification

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ActiveContext]]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeHints]


# IntentClassificationTestResultItem

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### multiTurnConversation
- **Type**: <class 'bool'>
- **Required**: Yes

### resultCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClassificationTestResultItemCounts'>
- **Required**: Yes


# IntentClassificationTestResultItemCounts

### totalResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### intentMatchResultCounts
- **Type**: typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]
- **Required**: Yes

### speechTranscriptionResultCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]]


# IntentClassificationTestResults

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClassificationTestResultItem]
- **Required**: Yes


# IntentClosingSetting

### closingResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### active
- **Type**: typing.Optional[bool]

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]


# IntentClosingSettingOutput

### closingResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### active
- **Type**: typing.Optional[bool]

### nextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]


# IntentClosingSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntentConfirmationSetting

### promptSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecification'>
- **Required**: Yes

### declinationResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### active
- **Type**: typing.Optional[bool]

### confirmationResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### confirmationNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### confirmationConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### declinationNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### declinationConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSetting]

### elicitationCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ElicitationCodeHookInvocationSetting]


# IntentConfirmationSettingOutput

### promptSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationOutput'>
- **Required**: Yes

### declinationResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### active
- **Type**: typing.Optional[bool]

### confirmationResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### confirmationNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### confirmationConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### declinationNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### declinationConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSettingOutput]

### elicitationCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ElicitationCodeHookInvocationSetting]


# IntentConfirmationSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntentFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntentLevelSlotResolutionTestResultItem

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### multiTurnConversation
- **Type**: <class 'bool'>
- **Required**: Yes

### slotResolutionResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionTestResultItem]
- **Required**: Yes


# IntentLevelSlotResolutionTestResults

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentLevelSlotResolutionTestResultItem]
- **Required**: Yes


# IntentOverride

### name
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueOverride]]


# IntentOverrideOutput

### name
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueOverrideOutput]]


# IntentSortBy

### attribute
- **Type**: typing.Literal['IntentName', 'LastUpdatedDateTime']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# IntentStatistics

### discoveredIntentCount
- **Type**: typing.Optional[int]


# IntentSummary

### intentId
- **Type**: typing.Optional[str]

### intentName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parentIntentSignature
- **Type**: typing.Optional[str]

### inputContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContext]]

### outputContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContext]]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# InvokedIntentSample

### intentName
- **Type**: typing.Optional[str]


# KendraConfiguration

### kendraIndex
- **Type**: <class 'str'>
- **Required**: Yes

### queryFilterStringEnabled
- **Type**: typing.Optional[bool]

### queryFilterString
- **Type**: typing.Optional[str]


# LambdaCodeHook

### lambdaARN
- **Type**: <class 'str'>
- **Required**: Yes

### codeHookInterfaceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# LexTranscriptFilter

### dateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DateRangeFilter]


# LexTranscriptFilterOutput

### dateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DateRangeFilterOutput]


# ListAggregatedUtterancesRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceAggregationDuration'>
- **Required**: Yes

### botAliasId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AggregatedUtterancesSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AggregatedUtterancesFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAggregatedUtterancesResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceAggregationDuration'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AggregatedUtterancesSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotAliasReplicasRequest

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


# ListBotAliasReplicasResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasReplicaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotAliasesRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotAliasesResponse

### botAliasSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasSummary]
- **Required**: Yes

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotLocalesRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotLocalesResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### botLocaleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotLocaleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotRecommendationsRequest

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


# ListBotRecommendationsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotRecommendationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotReplicasRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes


# ListBotReplicasResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### botReplicaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotReplicaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# ListBotResourceGenerationsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerationSortBy]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotResourceGenerationsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotVersionReplicasRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionReplicaSortBy]


# ListBotVersionReplicasResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionReplicaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotVersionsRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionSortBy]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotVersionsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBotsRequest

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBotsResponse

### botSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuiltInIntentsRequest

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInIntentSortBy]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBuiltInIntentsResponse

### builtInIntentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInIntentSummary]
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuiltInSlotTypesRequest

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInSlotTypeSortBy]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBuiltInSlotTypesResponse

### builtInSlotTypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BuiltInSlotTypeSummary]
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCustomVocabularyItemsRequest

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


# ListCustomVocabularyItemsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomVocabularyItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExportsRequest

### botId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### localeId
- **Type**: typing.Optional[str]


# ListExportsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### exportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ExportSummary]
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportsRequest

### botId
- **Type**: typing.Optional[str]

### botVersion
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImportSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.ImportFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### localeId
- **Type**: typing.Optional[str]


# ListImportsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### importSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ImportSummary]
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIntentMetricsRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentMetric]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecification]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentGroupBySpecification]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIntentMetricsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIntentPathsRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### intentPath
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsPathFilter]]


# ListIntentPathsResponse

### nodeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentNodeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# ListIntentStageMetricsRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageMetric]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecification]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageGroupBySpecification]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIntentStageMetricsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsIntentStageResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIntentsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIntentsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendedIntentsRequest

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


# ListRecommendedIntentsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.RecommendedIntentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionAnalyticsDataRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SessionDataSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionAnalyticsDataResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SessionSpecification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionMetricsRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionMetric]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecification]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionGroupBySpecification]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionMetricsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsSessionResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSlotTypesRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSlotTypesResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSlotsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSlotsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# ListTestExecutionResultItemsRequest

### testExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### resultFilterBy
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionResultFilterBy'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestExecutionResultItemsResponse

### testExecutionResults
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionResultItems'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestExecutionsRequest

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionSortBy]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestExecutionsResponse

### testExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestSetRecordsRequest

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestSetRecordsResponse

### testSetRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetTurnRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestSetsRequest

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetSortBy]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestSetsResponse

### testSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUtteranceAnalyticsDataRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceDataSortBy]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUtteranceAnalyticsDataResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### utterances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceSpecification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUtteranceMetricsRequest

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### startDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### endDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Timestamp'>
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceMetric]
- **Required**: Yes

### binBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsBinBySpecification]]

### groupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceGroupBySpecification]]

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceAttribute]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUtteranceMetricsResponse

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AnalyticsUtteranceResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Message

### plainTextMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PlainTextMessage]

### customPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomPayload]

### ssmlMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SSMLMessage]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImageResponseCard]


# MessageGroup

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.Message'>
- **Required**: Yes

### variations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.Message]]


# MessageGroupOutput

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MessageOutput'>
- **Required**: Yes

### variations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageOutput]]


# MessageOutput

### plainTextMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PlainTextMessage]

### customPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CustomPayload]

### ssmlMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SSMLMessage]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImageResponseCardOutput]


# MultipleValuesSetting

### allowMultipleValues
- **Type**: typing.Optional[bool]


# NewCustomVocabularyItem

### phrase
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### displayAs
- **Type**: typing.Optional[str]


# ObfuscationSetting

### obfuscationSettingType
- **Type**: typing.Literal['DefaultObfuscation', 'None']
- **Required**: Yes


# OpensearchConfiguration

### domainEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### exactResponse
- **Type**: typing.Optional[bool]

### exactResponseFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExactResponseFields]

### includeFields
- **Type**: typing.Optional[typing.Sequence[str]]


# OpensearchConfigurationOutput

### domainEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### indexName
- **Type**: <class 'str'>
- **Required**: Yes

### exactResponse
- **Type**: typing.Optional[bool]

### exactResponseFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExactResponseFields]

### includeFields
- **Type**: typing.Optional[typing.List[str]]


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


# OverallTestResultItem

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


# OverallTestResults

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OverallTestResultItem]
- **Required**: Yes


# ParentBotNetwork

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes


# PathFormat

### objectPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]


# PathFormatOutput

### objectPrefixes
- **Type**: typing.Optional[typing.List[str]]


# PlainTextMessage

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PostDialogCodeHookInvocationSpecification

### successResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### successNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### successConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### timeoutResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### timeoutNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### timeoutConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]


# PostDialogCodeHookInvocationSpecificationOutput

### successResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### successNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### successConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### timeoutResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### timeoutNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### timeoutConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]


# PostFulfillmentStatusSpecification

### successResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### timeoutResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### successNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### successConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### timeoutNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### timeoutConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]


# PostFulfillmentStatusSpecificationOutput

### successResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### timeoutResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### successNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### successConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### timeoutNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### timeoutConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]


# Principal

### service
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# PromptAttemptSpecification

### allowedInputTypes
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.AllowedInputTypes'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]

### audioAndDTMFInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AudioAndDTMFInputSpecification]

### textInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TextInputSpecification]


# PromptSpecification

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroup]
- **Required**: Yes

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]

### messageSelectionStrategy
- **Type**: typing.Optional[typing.Literal['Ordered', 'Random']]

### promptAttemptsSpecification
- **Type**: typing.Optional[typing.Mapping[typing.Literal['Initial', 'Retry1', 'Retry2', 'Retry3', 'Retry4', 'Retry5'], aws_resource_validator.pydantic_models.lexv2_models_classes.PromptAttemptSpecification]]


# PromptSpecificationOutput

### messageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupOutput]
- **Required**: Yes

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]

### messageSelectionStrategy
- **Type**: typing.Optional[typing.Literal['Ordered', 'Random']]

### promptAttemptsSpecification
- **Type**: typing.Optional[typing.Dict[typing.Literal['Initial', 'Retry1', 'Retry2', 'Retry3', 'Retry4', 'Retry5'], aws_resource_validator.pydantic_models.lexv2_models_classes.PromptAttemptSpecification]]


# QnAIntentConfiguration

### dataSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DataSourceConfiguration]

### bedrockModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecification]


# QnAIntentConfigurationOutput

### dataSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DataSourceConfigurationOutput]

### bedrockModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecification]


# QnAIntentConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QnAKendraConfiguration

### kendraIndex
- **Type**: <class 'str'>
- **Required**: Yes

### queryFilterStringEnabled
- **Type**: typing.Optional[bool]

### queryFilterString
- **Type**: typing.Optional[str]

### exactResponse
- **Type**: typing.Optional[bool]


# RecommendedIntentSummary

### intentId
- **Type**: typing.Optional[str]

### intentName
- **Type**: typing.Optional[str]

### sampleUtterancesCount
- **Type**: typing.Optional[int]


# RelativeAggregationDuration

### timeDimension
- **Type**: typing.Literal['Days', 'Hours', 'Weeks']
- **Required**: Yes

### timeValue
- **Type**: <class 'int'>
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


# ResponseSpecification

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroup]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# ResponseSpecificationOutput

### messageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupOutput]
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# RuntimeHintDetails

### runtimeHintValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeHintValue]]

### subSlotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# RuntimeHintValue

### phrase
- **Type**: <class 'str'>
- **Required**: Yes


# RuntimeHints

### slotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.RuntimeHintDetails]]]


# RuntimeSettings

### slotResolutionImprovement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionImprovementSpecification]


# S3BucketLogDestination

### s3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### logPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# S3BucketTranscriptSource

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### transcriptFormat
- **Type**: typing.Literal['Lex']
- **Required**: Yes

### pathFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PathFormat]

### transcriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptFilter]

### kmsKeyArn
- **Type**: typing.Optional[str]


# S3BucketTranscriptSourceOutput

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### transcriptFormat
- **Type**: typing.Literal['Lex']
- **Required**: Yes

### pathFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PathFormatOutput]

### transcriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptFilterOutput]

### kmsKeyArn
- **Type**: typing.Optional[str]


# SSMLMessage

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SampleUtterance

### utterance
- **Type**: <class 'str'>
- **Required**: Yes


# SampleUtteranceGenerationSpecification

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bedrockModelSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecification]


# SampleValue

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SearchAssociatedTranscriptsRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.AssociatedTranscriptFilter]
- **Required**: Yes

### searchOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### maxResults
- **Type**: typing.Optional[int]

### nextIndex
- **Type**: typing.Optional[int]


# SearchAssociatedTranscriptsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.AssociatedTranscript]
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# SentimentAnalysisSettings

### detectSentiment
- **Type**: <class 'bool'>
- **Required**: Yes


# SessionDataSortBy

### name
- **Type**: typing.Literal['ConversationStartTime', 'Duration', 'NumberOfTurns']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# SessionSpecification

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InvokedIntentSample]]

### originatingRequestId
- **Type**: typing.Optional[str]


# SlotCaptureSetting

### captureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### captureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### captureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogState]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecification]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSetting]

### elicitationCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ElicitationCodeHookInvocationSetting]


# SlotCaptureSettingOutput

### captureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### captureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### captureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### failureResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput]

### failureNextStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogStateOutput]

### failureConditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConditionalSpecificationOutput]

### codeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookInvocationSettingOutput]

### elicitationCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ElicitationCodeHookInvocationSetting]


# SlotDefaultValue

### defaultValue
- **Type**: <class 'str'>
- **Required**: Yes


# SlotDefaultValueSpecification

### defaultValueList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValue]
- **Required**: Yes


# SlotDefaultValueSpecificationOutput

### defaultValueList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValue]
- **Required**: Yes


# SlotFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SlotPriority

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### slotId
- **Type**: <class 'str'>
- **Required**: Yes


# SlotResolutionImprovementSpecification

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bedrockModelSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BedrockModelSpecification]


# SlotResolutionSetting

### slotResolutionStrategy
- **Type**: typing.Literal['Default', 'EnhancedFallback']
- **Required**: Yes


# SlotResolutionTestResultItem

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### resultCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionTestResultItemCounts'>
- **Required**: Yes


# SlotResolutionTestResultItemCounts

### totalResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### slotMatchResultCounts
- **Type**: typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]
- **Required**: Yes

### speechTranscriptionResultCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ExecutionError', 'Matched', 'Mismatched'], int]]


# SlotSortBy

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime', 'SlotName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# SlotSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationOutput]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# SlotTypeFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SlotTypeSortBy

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime', 'SlotTypeName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# SlotTypeStatistics

### discoveredSlotTypeCount
- **Type**: typing.Optional[int]


# SlotTypeSummary

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


# SlotTypeValue

### sampleValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleValue]

### synonyms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleValue]]


# SlotTypeValueOutput

### sampleValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleValue]

### synonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleValue]]


# SlotTypeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SlotValue

### interpretedValue
- **Type**: typing.Optional[str]


# SlotValueElicitationSetting

### slotConstraint
- **Type**: typing.Literal['Optional', 'Required']
- **Required**: Yes

### defaultValueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueSpecification]

### promptSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecification]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]]

### waitAndContinueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaitAndContinueSpecification]

### slotCaptureSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotCaptureSetting]

### slotResolutionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionSetting]


# SlotValueElicitationSettingOutput

### slotConstraint
- **Type**: typing.Literal['Optional', 'Required']
- **Required**: Yes

### defaultValueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueSpecificationOutput]

### promptSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationOutput]

### sampleUtterances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]]

### waitAndContinueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaitAndContinueSpecificationOutput]

### slotCaptureSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotCaptureSettingOutput]

### slotResolutionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotResolutionSetting]


# SlotValueElicitationSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SlotValueOverride

### shape
- **Type**: typing.Optional[typing.Literal['List', 'Scalar']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValue]

### values
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# SlotValueOverrideOutput

### shape
- **Type**: typing.Optional[typing.Literal['List', 'Scalar']]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValue]

### values
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# SlotValueRegexFilter

### pattern
- **Type**: <class 'str'>
- **Required**: Yes


# SlotValueSelectionSetting

### resolutionStrategy
- **Type**: typing.Literal['Concatenation', 'OriginalValue', 'TopResolution']
- **Required**: Yes

### regexFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueRegexFilter]

### advancedRecognitionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AdvancedRecognitionSetting]


# Specifications

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotValueElicitationSetting'>
- **Required**: Yes


# SpecificationsOutput

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotValueElicitationSettingOutput'>
- **Required**: Yes


# StartBotRecommendationRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingUnion'>
- **Required**: Yes

### encryptionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSetting]


# StartBotRecommendationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingOutput'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSetting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# StartBotResourceGenerationRequest

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


# StartBotResourceGenerationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportRequest

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ImportResourceSpecificationUnion'>
- **Required**: Yes

### mergeStrategy
- **Type**: typing.Literal['Append', 'FailOnConflict', 'Overwrite']
- **Required**: Yes

### filePassword
- **Type**: typing.Optional[str]


# StartImportResponse

### importId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ImportResourceSpecificationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# StartTestExecutionRequest

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTarget'>
- **Required**: Yes

### apiMode
- **Type**: typing.Literal['NonStreaming', 'Streaming']
- **Required**: Yes

### testExecutionModality
- **Type**: typing.Optional[typing.Literal['Audio', 'Text']]


# StartTestExecutionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTarget'>
- **Required**: Yes

### apiMode
- **Type**: typing.Literal['NonStreaming', 'Streaming']
- **Required**: Yes

### testExecutionModality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# StartTestSetGenerationRequest

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### generationDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetGenerationDataSourceUnion'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testSetTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartTestSetGenerationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### generationDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetGenerationDataSourceOutput'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### testSetTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# StillWaitingResponseSpecification

### messageGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroup]
- **Required**: Yes

### frequencyInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### timeoutInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# StillWaitingResponseSpecificationOutput

### messageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.MessageGroupOutput]
- **Required**: Yes

### frequencyInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### timeoutInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### allowInterrupt
- **Type**: typing.Optional[bool]


# StopBotRecommendationRequest

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


# StopBotRecommendationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# SubSlotSetting

### expression
- **Type**: typing.Optional[str]

### slotSpecifications
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.Specifications]]


# SubSlotSettingOutput

### expression
- **Type**: typing.Optional[str]

### slotSpecifications
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.SpecificationsOutput]]


# SubSlotSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubSlotTypeComposition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slotTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# SubSlotValueElicitationSetting

### promptSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecification'>
- **Required**: Yes

### defaultValueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueSpecification]

### sampleUtterances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]]

### waitAndContinueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaitAndContinueSpecification]


# SubSlotValueElicitationSettingOutput

### promptSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.PromptSpecificationOutput'>
- **Required**: Yes

### defaultValueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotDefaultValueSpecificationOutput]

### sampleUtterances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]]

### waitAndContinueSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.WaitAndContinueSpecificationOutput]


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestExecutionResultFilterBy

### resultTypeFilter
- **Type**: typing.Literal['ConversationLevelTestResults', 'IntentClassificationTestResults', 'OverallTestResults', 'SlotResolutionTestResults', 'UtteranceLevelResults']
- **Required**: Yes

### conversationLevelTestResultsFilterBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelTestResultsFilterBy]


# TestExecutionResultItems

### overallTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.OverallTestResults]

### conversationLevelTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLevelTestResults]

### intentClassificationTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClassificationTestResults]

### intentLevelSlotResolutionTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentLevelSlotResolutionTestResults]

### utteranceLevelTestResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceLevelTestResults]


# TestExecutionSortBy

### attribute
- **Type**: typing.Literal['CreationDateTime', 'TestSetName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# TestExecutionSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestExecutionTarget]

### apiMode
- **Type**: typing.Optional[typing.Literal['NonStreaming', 'Streaming']]

### testExecutionModality
- **Type**: typing.Optional[typing.Literal['Audio', 'Text']]


# TestExecutionTarget

### botAliasTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasTestExecutionTarget]


# TestSetDiscrepancyErrors

### intentDiscrepancies
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetIntentDiscrepancyItem]
- **Required**: Yes

### slotDiscrepancies
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetSlotDiscrepancyItem]
- **Required**: Yes


# TestSetDiscrepancyReportBotAliasTarget

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetDiscrepancyReportResourceTarget

### botAliasTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetDiscrepancyReportBotAliasTarget]


# TestSetExportSpecification

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetGenerationDataSource

### conversationLogsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogsDataSource]


# TestSetGenerationDataSourceOutput

### conversationLogsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogsDataSourceOutput]


# TestSetGenerationDataSourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestSetImportInputLocation

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetImportResourceSpecification

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### importInputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetImportInputLocation'>
- **Required**: Yes

### modality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testSetTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TestSetImportResourceSpecificationOutput

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### storageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### importInputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetImportInputLocation'>
- **Required**: Yes

### modality
- **Type**: typing.Literal['Audio', 'Text']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testSetTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TestSetIntentDiscrepancyItem

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetSlotDiscrepancyItem

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# TestSetSortBy

### attribute
- **Type**: typing.Literal['LastUpdatedDateTime', 'TestSetName']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# TestSetStorageLocation

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# TestSetSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# TestSetTurnRecord

### recordNumber
- **Type**: <class 'int'>
- **Required**: Yes

### turnSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TurnSpecification'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]

### turnNumber
- **Type**: typing.Optional[int]


# TestSetTurnResult

### agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AgentTurnResult]

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnResult]


# TextInputSpecification

### startTimeoutMs
- **Type**: <class 'int'>
- **Required**: Yes


# TextLogDestination

### cloudWatch
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CloudWatchLogGroupLogDestination'>
- **Required**: Yes


# TextLogSetting

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TextLogDestination'>
- **Required**: Yes

### selectiveLoggingEnabled
- **Type**: typing.Optional[bool]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TranscriptFilter

### lexTranscriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.LexTranscriptFilter]


# TranscriptFilterOutput

### lexTranscriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.LexTranscriptFilterOutput]


# TranscriptSourceSetting

### s3BucketTranscriptSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.S3BucketTranscriptSource]


# TranscriptSourceSettingOutput

### s3BucketTranscriptSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.S3BucketTranscriptSourceOutput]


# TranscriptSourceSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TurnSpecification

### agentTurn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.AgentTurnSpecification]

### userTurn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnSpecification]


# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBotAliasRequest

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettings]]

### conversationLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsUnion]

### sentimentAnalysisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettings]


# UpdateBotAliasResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.BotAliasLocaleSettings]
- **Required**: Yes

### conversationLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ConversationLogSettingsOutput'>
- **Required**: Yes

### sentimentAnalysisSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SentimentAnalysisSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBotLocaleRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettings]

### generativeAISettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettings]


# UpdateBotLocaleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.VoiceSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.GenerativeAISettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBotRecommendationRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSetting'>
- **Required**: Yes


# UpdateBotRecommendationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TranscriptSourceSettingOutput'>
- **Required**: Yes

### encryptionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.EncryptionSetting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBotRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### botType
- **Type**: typing.Optional[typing.Literal['Bot', 'BotNetwork']]

### botMembers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMember]]


# UpdateBotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DataPrivacy'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.BotMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateExportRequest

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### filePassword
- **Type**: typing.Optional[str]


# UpdateExportResponse

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExportResourceSpecification'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIntentRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]]

### dialogCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettings]

### fulfillmentCodeHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsUnion]

### slotPriorities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotPriority]]

### intentConfirmationSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingUnion]

### intentClosingSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingUnion]

### inputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContext]]

### outputContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContext]]

### kendraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfiguration]

### initialResponseSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingUnion]

### qnAIntentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationUnion]


# UpdateIntentResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SampleUtterance]
- **Required**: Yes

### dialogCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.DialogCodeHookSettings'>
- **Required**: Yes

### fulfillmentCodeHook
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.FulfillmentCodeHookSettingsOutput'>
- **Required**: Yes

### slotPriorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotPriority]
- **Required**: Yes

### intentConfirmationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentConfirmationSettingOutput'>
- **Required**: Yes

### intentClosingSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.IntentClosingSettingOutput'>
- **Required**: Yes

### inputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.InputContext]
- **Required**: Yes

### outputContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.OutputContext]
- **Required**: Yes

### kendraConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.KendraConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.InitialResponseSettingOutput'>
- **Required**: Yes

### qnAIntentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.QnAIntentConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### expectedRevisionId
- **Type**: typing.Optional[str]


# UpdateResourcePolicyResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSlotRequest

### slotId
- **Type**: <class 'str'>
- **Required**: Yes

### slotName
- **Type**: <class 'str'>
- **Required**: Yes

### valueElicitationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingUnion'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSetting]

### multipleValuesSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSetting]

### subSlotSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingUnion]


# UpdateSlotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueElicitationSettingOutput'>
- **Required**: Yes

### obfuscationSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ObfuscationSetting'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.MultipleValuesSetting'>
- **Required**: Yes

### subSlotSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SubSlotSettingOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSlotTypeRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueUnion]]

### valueSelectionSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSetting]

### parentSlotTypeSignature
- **Type**: typing.Optional[str]

### externalSourceSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSetting]

### compositeSlotTypeSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingUnion]


# UpdateSlotTypeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.SlotTypeValueOutput]
- **Required**: Yes

### valueSelectionSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.SlotValueSelectionSetting'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ExternalSourceSetting'>
- **Required**: Yes

### compositeSlotTypeSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.CompositeSlotTypeSettingOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTestSetRequest

### testSetId
- **Type**: <class 'str'>
- **Required**: Yes

### testSetName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateTestSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetStorageLocation'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseMetadata'>
- **Required**: Yes


# UserTurnInputSpecification

### utteranceInput
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceInputSpecification'>
- **Required**: Yes

### requestAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.InputSessionStateSpecification]


# UserTurnIntentOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnSlotOutput]]


# UserTurnOutputSpecification

### intent
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.UserTurnIntentOutput'>
- **Required**: Yes

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.ActiveContext]]

### transcript
- **Type**: typing.Optional[str]


# UserTurnResult

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UserTurnSlotOutput

### value
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# UserTurnSpecification

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UtteranceAggregationDuration

### relativeAggregationDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.RelativeAggregationDuration'>
- **Required**: Yes


# UtteranceAudioInputSpecification

### audioFileS3Location
- **Type**: <class 'str'>
- **Required**: Yes


# UtteranceBotResponse

### content
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.ImageResponseCardOutput]


# UtteranceDataSortBy

### name
- **Type**: typing.Literal['UtteranceTimestamp']
- **Required**: Yes

### order
- **Type**: typing.Literal['Ascending', 'Descending']
- **Required**: Yes


# UtteranceInputSpecification

### textInput
- **Type**: typing.Optional[str]

### audioInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceAudioInputSpecification]


# UtteranceLevelTestResultItem

### recordNumber
- **Type**: <class 'int'>
- **Required**: Yes

### turnResult
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.TestSetTurnResult'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]


# UtteranceLevelTestResults

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceLevelTestResultItem]
- **Required**: Yes


# UtteranceSpecification

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_models_classes.UtteranceBotResponse]]


# VoiceSettings

### voiceId
- **Type**: <class 'str'>
- **Required**: Yes

### engine
- **Type**: typing.Optional[typing.Literal['generative', 'long-form', 'neural', 'standard']]


# WaitAndContinueSpecification

### waitingResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification'>
- **Required**: Yes

### continueResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecification'>
- **Required**: Yes

### stillWaitingResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.StillWaitingResponseSpecification]

### active
- **Type**: typing.Optional[bool]


# WaitAndContinueSpecificationOutput

### waitingResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput'>
- **Required**: Yes

### continueResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_models_classes.ResponseSpecificationOutput'>
- **Required**: Yes

### stillWaitingResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_models_classes.StillWaitingResponseSpecificationOutput]

### active
- **Type**: typing.Optional[bool]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


