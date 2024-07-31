from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.lexv2_models_constants import *

class ActiveContextTypeDef(BaseModel):
    name: str

class AdvancedRecognitionSettingTypeDef(BaseModel):
    audioRecognitionStrategy: Optional[Literal["UseSlotValuesAsCustomVocabulary"]] = None

class ExecutionErrorDetailsTypeDef(BaseModel):
    errorCode: str
    errorMessage: str

class AgentTurnSpecificationTypeDef(BaseModel):
    agentPrompt: str

class AggregatedUtterancesFilterTypeDef(BaseModel):
    name: Literal["Utterance"]
    values: Sequence[str]
    operator: AggregatedUtterancesFilterOperatorType

class AggregatedUtterancesSortByTypeDef(BaseModel):
    attribute: AggregatedUtterancesSortAttributeType
    order: SortOrderType

class AggregatedUtterancesSummaryTypeDef(BaseModel):
    utterance: Optional[str] = None
    hitCount: Optional[int] = None
    missedCount: Optional[int] = None
    utteranceFirstRecordedInAggregationDuration: Optional[datetime] = None
    utteranceLastRecordedInAggregationDuration: Optional[datetime] = None
    containsDataFromDeletedResources: Optional[bool] = None

class AllowedInputTypesTypeDef(BaseModel):
    allowAudioInput: bool
    allowDTMFInput: bool

class AnalyticsBinBySpecificationTypeDef(BaseModel):
    name: AnalyticsBinByNameType
    interval: AnalyticsIntervalType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsBinKeyTypeDef(BaseModel):
    name: Optional[AnalyticsBinByNameType] = None
    value: Optional[int] = None

class AnalyticsIntentFilterTypeDef(BaseModel):
    name: AnalyticsIntentFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsIntentGroupByKeyTypeDef(BaseModel):
    name: Optional[AnalyticsIntentFieldType] = None
    value: Optional[str] = None

class AnalyticsIntentGroupBySpecificationTypeDef(BaseModel):
    name: AnalyticsIntentFieldType

class AnalyticsIntentMetricResultTypeDef(BaseModel):
    name: Optional[AnalyticsIntentMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsIntentMetricTypeDef(BaseModel):
    name: AnalyticsIntentMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsIntentNodeSummaryTypeDef(BaseModel):
    intentName: Optional[str] = None
    intentPath: Optional[str] = None
    intentCount: Optional[int] = None
    intentLevel: Optional[int] = None
    nodeType: Optional[AnalyticsNodeTypeType] = None

class AnalyticsIntentStageFilterTypeDef(BaseModel):
    name: AnalyticsIntentStageFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsIntentStageGroupByKeyTypeDef(BaseModel):
    name: Optional[AnalyticsIntentStageFieldType] = None
    value: Optional[str] = None

class AnalyticsIntentStageGroupBySpecificationTypeDef(BaseModel):
    name: AnalyticsIntentStageFieldType

class AnalyticsIntentStageMetricResultTypeDef(BaseModel):
    name: Optional[AnalyticsIntentStageMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsIntentStageMetricTypeDef(BaseModel):
    name: AnalyticsIntentStageMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsPathFilterTypeDef(BaseModel):
    name: AnalyticsCommonFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsSessionFilterTypeDef(BaseModel):
    name: AnalyticsSessionFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsSessionGroupByKeyTypeDef(BaseModel):
    name: Optional[AnalyticsSessionFieldType] = None
    value: Optional[str] = None

class AnalyticsSessionGroupBySpecificationTypeDef(BaseModel):
    name: AnalyticsSessionFieldType

class AnalyticsSessionMetricResultTypeDef(BaseModel):
    name: Optional[AnalyticsSessionMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsSessionMetricTypeDef(BaseModel):
    name: AnalyticsSessionMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsUtteranceAttributeResultTypeDef(BaseModel):
    lastUsedIntent: Optional[str] = None

class AnalyticsUtteranceAttributeTypeDef(BaseModel):
    name: Literal["LastUsedIntent"]

class AnalyticsUtteranceFilterTypeDef(BaseModel):
    name: AnalyticsUtteranceFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsUtteranceGroupByKeyTypeDef(BaseModel):
    name: Optional[AnalyticsUtteranceFieldType] = None
    value: Optional[str] = None

class AnalyticsUtteranceGroupBySpecificationTypeDef(BaseModel):
    name: AnalyticsUtteranceFieldType

class AnalyticsUtteranceMetricResultTypeDef(BaseModel):
    name: Optional[AnalyticsUtteranceMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsUtteranceMetricTypeDef(BaseModel):
    name: AnalyticsUtteranceMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AssociatedTranscriptFilterTypeDef(BaseModel):
    name: AssociatedTranscriptFilterNameType
    values: Sequence[str]

class AssociatedTranscriptTypeDef(BaseModel):
    transcript: Optional[str] = None

class AudioSpecificationTypeDef(BaseModel):
    maxLengthMs: int
    endTimeoutMs: int

class DTMFSpecificationTypeDef(BaseModel):
    maxLength: int
    endTimeoutMs: int
    deletionCharacter: str
    endCharacter: str

class S3BucketLogDestinationTypeDef(BaseModel):
    s3BucketArn: str
    logPrefix: str
    kmsKeyArn: Optional[str] = None

class NewCustomVocabularyItemTypeDef(BaseModel):
    phrase: str
    weight: Optional[int] = None
    displayAs: Optional[str] = None

class CustomVocabularyItemTypeDef(BaseModel):
    itemId: str
    phrase: str
    weight: Optional[int] = None
    displayAs: Optional[str] = None

class FailedCustomVocabularyItemTypeDef(BaseModel):
    itemId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CustomVocabularyEntryIdTypeDef(BaseModel):
    itemId: str

class BedrockKnowledgeStoreConfigurationTypeDef(BaseModel):
    bedrockKnowledgeBaseArn: str

class BedrockModelSpecificationTypeDef(BaseModel):
    modelArn: str

class BotAliasHistoryEventTypeDef(BaseModel):
    botVersion: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None

class BotAliasReplicaSummaryTypeDef(BaseModel):
    botAliasId: Optional[str] = None
    botAliasReplicationStatus: Optional[BotAliasReplicationStatusType] = None
    botVersion: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReasons: Optional[List[str]] = None

class BotAliasSummaryTypeDef(BaseModel):
    botAliasId: Optional[str] = None
    botAliasName: Optional[str] = None
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasStatus: Optional[BotAliasStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class BotAliasTestExecutionTargetTypeDef(BaseModel):
    botId: str
    botAliasId: str
    localeId: str

class BotExportSpecificationTypeDef(BaseModel):
    botId: str
    botVersion: str

class BotFilterTypeDef(BaseModel):
    name: BotFilterNameType
    values: Sequence[str]
    operator: BotFilterOperatorType

class DataPrivacyTypeDef(BaseModel):
    childDirected: bool

class BotLocaleExportSpecificationTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class BotLocaleFilterTypeDef(BaseModel):
    name: Literal["BotLocaleName"]
    values: Sequence[str]
    operator: BotLocaleFilterOperatorType

class BotLocaleHistoryEventTypeDef(BaseModel):
    event: str
    eventDate: datetime

class VoiceSettingsTypeDef(BaseModel):
    voiceId: str
    engine: Optional[VoiceEngineType] = None

class BotLocaleSortByTypeDef(BaseModel):
    attribute: Literal["BotLocaleName"]
    order: SortOrderType

class BotLocaleSummaryTypeDef(BaseModel):
    localeId: Optional[str] = None
    localeName: Optional[str] = None
    description: Optional[str] = None
    botLocaleStatus: Optional[BotLocaleStatusType] = None
    lastUpdatedDateTime: Optional[datetime] = None
    lastBuildSubmittedDateTime: Optional[datetime] = None

class BotMemberTypeDef(BaseModel):
    botMemberId: str
    botMemberName: str
    botMemberAliasId: str
    botMemberAliasName: str
    botMemberVersion: str

class IntentStatisticsTypeDef(BaseModel):
    discoveredIntentCount: Optional[int] = None

class SlotTypeStatisticsTypeDef(BaseModel):
    discoveredSlotTypeCount: Optional[int] = None

class BotRecommendationSummaryTypeDef(BaseModel):
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class BotReplicaSummaryTypeDef(BaseModel):
    replicaRegion: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    botReplicaStatus: Optional[BotReplicaStatusType] = None
    failureReasons: Optional[List[str]] = None

class BotSortByTypeDef(BaseModel):
    attribute: Literal["BotName"]
    order: SortOrderType

class BotSummaryTypeDef(BaseModel):
    botId: Optional[str] = None
    botName: Optional[str] = None
    description: Optional[str] = None
    botStatus: Optional[BotStatusType] = None
    latestBotVersion: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None
    botType: Optional[BotTypeType] = None

class BotVersionLocaleDetailsTypeDef(BaseModel):
    sourceBotVersion: str

class BotVersionReplicaSortByTypeDef(BaseModel):
    attribute: Literal["BotVersion"]
    order: SortOrderType

class BotVersionReplicaSummaryTypeDef(BaseModel):
    botVersion: Optional[str] = None
    botVersionReplicationStatus: Optional[BotVersionReplicationStatusType] = None
    creationDateTime: Optional[datetime] = None
    failureReasons: Optional[List[str]] = None

class BotVersionSortByTypeDef(BaseModel):
    attribute: Literal["BotVersion"]
    order: SortOrderType

class BotVersionSummaryTypeDef(BaseModel):
    botName: Optional[str] = None
    botVersion: Optional[str] = None
    description: Optional[str] = None
    botStatus: Optional[BotStatusType] = None
    creationDateTime: Optional[datetime] = None

class BuildBotLocaleRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class BuiltInIntentSortByTypeDef(BaseModel):
    attribute: Literal["IntentSignature"]
    order: SortOrderType

class BuiltInIntentSummaryTypeDef(BaseModel):
    intentSignature: Optional[str] = None
    description: Optional[str] = None

class BuiltInSlotTypeSortByTypeDef(BaseModel):
    attribute: Literal["SlotTypeSignature"]
    order: SortOrderType

class BuiltInSlotTypeSummaryTypeDef(BaseModel):
    slotTypeSignature: Optional[str] = None
    description: Optional[str] = None

class ButtonTypeDef(BaseModel):
    text: str
    value: str

class CloudWatchLogGroupLogDestinationTypeDef(BaseModel):
    cloudWatchLogGroupArn: str
    logPrefix: str

class LambdaCodeHookTypeDef(BaseModel):
    lambdaARN: str
    codeHookInterfaceVersion: str

class SubSlotTypeCompositionTypeDef(BaseModel):
    name: str
    slotTypeId: str

class ConditionTypeDef(BaseModel):
    expressionString: str

class ConversationLevelIntentClassificationResultItemTypeDef(BaseModel):
    intentName: str
    matchResult: TestResultMatchStatusType

class ConversationLevelResultDetailTypeDef(BaseModel):
    endToEndResult: TestResultMatchStatusType
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None

class ConversationLevelSlotResolutionResultItemTypeDef(BaseModel):
    intentName: str
    slotName: str
    matchResult: TestResultMatchStatusType

class ConversationLevelTestResultsFilterByTypeDef(BaseModel):
    endToEndResult: Optional[TestResultMatchStatusType] = None

class ConversationLogsDataSourceFilterByTypeDef(BaseModel):
    startTime: datetime
    endTime: datetime
    inputMode: ConversationLogsInputModeFilterType

class SentimentAnalysisSettingsTypeDef(BaseModel):
    detectSentiment: bool

class CreateBotReplicaRequestRequestTypeDef(BaseModel):
    botId: str
    replicaRegion: str

class DialogCodeHookSettingsTypeDef(BaseModel):
    enabled: bool

class InputContextTypeDef(BaseModel):
    name: str

class KendraConfigurationTypeDef(BaseModel):
    kendraIndex: str
    queryFilterStringEnabled: Optional[bool] = None
    queryFilterString: Optional[str] = None

class OutputContextTypeDef(BaseModel):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int

class SampleUtteranceTypeDef(BaseModel):
    utterance: str

class CreateResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str
    policy: str

class PrincipalTypeDef(BaseModel):
    service: Optional[str] = None
    arn: Optional[str] = None

class MultipleValuesSettingTypeDef(BaseModel):
    allowMultipleValues: Optional[bool] = None

class ObfuscationSettingTypeDef(BaseModel):
    obfuscationSettingType: ObfuscationSettingTypeType

class CustomPayloadTypeDef(BaseModel):
    value: str

class CustomVocabularyExportSpecificationTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class CustomVocabularyImportSpecificationTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class QnAKendraConfigurationTypeDef(BaseModel):
    kendraIndex: str
    queryFilterStringEnabled: Optional[bool] = None
    queryFilterString: Optional[str] = None
    exactResponse: Optional[bool] = None

class DateRangeFilterTypeDef(BaseModel):
    startDateTime: datetime
    endDateTime: datetime

class DeleteBotAliasRequestRequestTypeDef(BaseModel):
    botAliasId: str
    botId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteBotLocaleRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class DeleteBotReplicaRequestRequestTypeDef(BaseModel):
    botId: str
    replicaRegion: str

class DeleteBotRequestRequestTypeDef(BaseModel):
    botId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteBotVersionRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteCustomVocabularyRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class DeleteExportRequestRequestTypeDef(BaseModel):
    exportId: str

class DeleteImportRequestRequestTypeDef(BaseModel):
    importId: str

class DeleteIntentRequestRequestTypeDef(BaseModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str
    expectedRevisionId: Optional[str] = None

class DeleteResourcePolicyStatementRequestRequestTypeDef(BaseModel):
    resourceArn: str
    statementId: str
    expectedRevisionId: Optional[str] = None

class DeleteSlotRequestRequestTypeDef(BaseModel):
    slotId: str
    botId: str
    botVersion: str
    localeId: str
    intentId: str

class DeleteSlotTypeRequestRequestTypeDef(BaseModel):
    slotTypeId: str
    botId: str
    botVersion: str
    localeId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteTestSetRequestRequestTypeDef(BaseModel):
    testSetId: str

class DeleteUtterancesRequestRequestTypeDef(BaseModel):
    botId: str
    localeId: Optional[str] = None
    sessionId: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeBotAliasRequestRequestTypeDef(BaseModel):
    botAliasId: str
    botId: str

class ParentBotNetworkTypeDef(BaseModel):
    botId: str
    botVersion: str

class DescribeBotLocaleRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class DescribeBotRecommendationRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str

class EncryptionSettingTypeDef(BaseModel):
    kmsKeyArn: Optional[str] = None
    botLocaleExportPassword: Optional[str] = None
    associatedTranscriptsPassword: Optional[str] = None

class DescribeBotReplicaRequestRequestTypeDef(BaseModel):
    botId: str
    replicaRegion: str

class DescribeBotRequestRequestTypeDef(BaseModel):
    botId: str

class DescribeBotResourceGenerationRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    generationId: str

class DescribeBotVersionRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str

class DescribeCustomVocabularyMetadataRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str

class DescribeExportRequestRequestTypeDef(BaseModel):
    exportId: str

class DescribeImportRequestRequestTypeDef(BaseModel):
    importId: str

class DescribeIntentRequestRequestTypeDef(BaseModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str

class SlotPriorityTypeDef(BaseModel):
    priority: int
    slotId: str

class DescribeResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str

class DescribeSlotRequestRequestTypeDef(BaseModel):
    slotId: str
    botId: str
    botVersion: str
    localeId: str
    intentId: str

class DescribeSlotTypeRequestRequestTypeDef(BaseModel):
    slotTypeId: str
    botId: str
    botVersion: str
    localeId: str

class DescribeTestExecutionRequestRequestTypeDef(BaseModel):
    testExecutionId: str

class DescribeTestSetDiscrepancyReportRequestRequestTypeDef(BaseModel):
    testSetDiscrepancyReportId: str

class DescribeTestSetGenerationRequestRequestTypeDef(BaseModel):
    testSetGenerationId: str

class TestSetStorageLocationTypeDef(BaseModel):
    s3BucketName: str
    s3Path: str
    kmsKeyArn: Optional[str] = None

class DescribeTestSetRequestRequestTypeDef(BaseModel):
    testSetId: str

class DialogActionTypeDef(BaseModel):
    type: DialogActionTypeType
    slotToElicit: Optional[str] = None
    suppressNextMessage: Optional[bool] = None

class IntentOverrideTypeDef(BaseModel):
    name: Optional[str] = None
    slots: Optional[Mapping[str, "SlotValueOverrideTypeDef"]] = None

class ElicitationCodeHookInvocationSettingTypeDef(BaseModel):
    enableCodeHookInvocation: bool
    invocationLabel: Optional[str] = None

class ExactResponseFieldsTypeDef(BaseModel):
    questionField: str
    answerField: str

class ExportFilterTypeDef(BaseModel):
    name: Literal["ExportResourceType"]
    values: Sequence[str]
    operator: ExportFilterOperatorType

class TestSetExportSpecificationTypeDef(BaseModel):
    testSetId: str

class ExportSortByTypeDef(BaseModel):
    attribute: Literal["LastUpdatedDateTime"]
    order: SortOrderType

class GenerateBotElementRequestRequestTypeDef(BaseModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str

class GenerationSortByTypeDef(BaseModel):
    attribute: GenerationSortByAttributeType
    order: SortOrderType

class GenerationSummaryTypeDef(BaseModel):
    generationId: Optional[str] = None
    generationStatus: Optional[GenerationStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class GetTestExecutionArtifactsUrlRequestRequestTypeDef(BaseModel):
    testExecutionId: str

class GrammarSlotTypeSourceTypeDef(BaseModel):
    s3BucketName: str
    s3ObjectKey: str
    kmsKeyArn: Optional[str] = None

class ImportFilterTypeDef(BaseModel):
    name: Literal["ImportResourceType"]
    values: Sequence[str]
    operator: ImportFilterOperatorType

class ImportSortByTypeDef(BaseModel):
    attribute: Literal["LastUpdatedDateTime"]
    order: SortOrderType

class ImportSummaryTypeDef(BaseModel):
    importId: Optional[str] = None
    importedResourceId: Optional[str] = None
    importedResourceName: Optional[str] = None
    importStatus: Optional[ImportStatusType] = None
    mergeStrategy: Optional[MergeStrategyType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    importedResourceType: Optional[ImportResourceTypeType] = None

class RuntimeHintsTypeDef(BaseModel):
    slotHints: Optional[Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]]] = None

class IntentClassificationTestResultItemCountsTypeDef(BaseModel):
    totalResultCount: int
    intentMatchResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None

class IntentFilterTypeDef(BaseModel):
    name: Literal["IntentName"]
    values: Sequence[str]
    operator: IntentFilterOperatorType

class IntentSortByTypeDef(BaseModel):
    attribute: IntentSortAttributeType
    order: SortOrderType

class InvokedIntentSampleTypeDef(BaseModel):
    intentName: Optional[str] = None

class ListBotAliasReplicasRequestRequestTypeDef(BaseModel):
    botId: str
    replicaRegion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotAliasesRequestRequestTypeDef(BaseModel):
    botId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotRecommendationsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotReplicasRequestRequestTypeDef(BaseModel):
    botId: str

class ListCustomVocabularyItemsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRecommendedIntentsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RecommendedIntentSummaryTypeDef(BaseModel):
    intentId: Optional[str] = None
    intentName: Optional[str] = None
    sampleUtterancesCount: Optional[int] = None

class SessionDataSortByTypeDef(BaseModel):
    name: AnalyticsSessionSortByNameType
    order: AnalyticsSortOrderType

class SlotTypeFilterTypeDef(BaseModel):
    name: SlotTypeFilterNameType
    values: Sequence[str]
    operator: SlotTypeFilterOperatorType

class SlotTypeSortByTypeDef(BaseModel):
    attribute: SlotTypeSortAttributeType
    order: SortOrderType

class SlotTypeSummaryTypeDef(BaseModel):
    slotTypeId: Optional[str] = None
    slotTypeName: Optional[str] = None
    description: Optional[str] = None
    parentSlotTypeSignature: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None
    slotTypeCategory: Optional[SlotTypeCategoryType] = None

class SlotFilterTypeDef(BaseModel):
    name: Literal["SlotName"]
    values: Sequence[str]
    operator: SlotFilterOperatorType

class SlotSortByTypeDef(BaseModel):
    attribute: SlotSortAttributeType
    order: SortOrderType

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str

class TestExecutionSortByTypeDef(BaseModel):
    attribute: TestExecutionSortAttributeType
    order: SortOrderType

class ListTestSetRecordsRequestRequestTypeDef(BaseModel):
    testSetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TestSetSortByTypeDef(BaseModel):
    attribute: TestSetSortAttributeType
    order: SortOrderType

class UtteranceDataSortByTypeDef(BaseModel):
    name: Literal["UtteranceTimestamp"]
    order: AnalyticsSortOrderType

class PlainTextMessageTypeDef(BaseModel):
    value: str

class SSMLMessageTypeDef(BaseModel):
    value: str

class OverallTestResultItemTypeDef(BaseModel):
    multiTurnConversation: bool
    totalResultCount: int
    endToEndResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None

class PathFormatTypeDef(BaseModel):
    objectPrefixes: Optional[List[str]] = None

class TextInputSpecificationTypeDef(BaseModel):
    startTimeoutMs: int

class RelativeAggregationDurationTypeDef(BaseModel):
    timeDimension: TimeDimensionType
    timeValue: int

class RuntimeHintValueTypeDef(BaseModel):
    phrase: str

class SampleValueTypeDef(BaseModel):
    value: str

class SlotDefaultValueTypeDef(BaseModel):
    defaultValue: str

class SlotResolutionSettingTypeDef(BaseModel):
    slotResolutionStrategy: SlotResolutionStrategyType

class SlotResolutionTestResultItemCountsTypeDef(BaseModel):
    totalResultCount: int
    slotMatchResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None

class SlotValueTypeDef(BaseModel):
    interpretedValue: Optional[str] = None

class SlotValueRegexFilterTypeDef(BaseModel):
    pattern: str

class StartBotResourceGenerationRequestRequestTypeDef(BaseModel):
    generationInputPrompt: str
    botId: str
    botVersion: str
    localeId: str

class StopBotRecommendationRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tags: Mapping[str, str]

class TestSetIntentDiscrepancyItemTypeDef(BaseModel):
    intentName: str
    errorMessage: str

class TestSetSlotDiscrepancyItemTypeDef(BaseModel):
    intentName: str
    slotName: str
    errorMessage: str

class TestSetDiscrepancyReportBotAliasTargetTypeDef(BaseModel):
    botId: str
    botAliasId: str
    localeId: str

class TestSetImportInputLocationTypeDef(BaseModel):
    s3BucketName: str
    s3Path: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateExportRequestRequestTypeDef(BaseModel):
    exportId: str
    filePassword: Optional[str] = None

class UpdateResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str
    policy: str
    expectedRevisionId: Optional[str] = None

class UpdateTestSetRequestRequestTypeDef(BaseModel):
    testSetId: str
    testSetName: str
    description: Optional[str] = None

class UserTurnIntentOutputTypeDef(BaseModel):
    name: str
    slots: Optional[Dict[str, "UserTurnSlotOutputTypeDef"]] = None

class UserTurnSlotOutputTypeDef(BaseModel):
    value: Optional[str] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None

class UtteranceAudioInputSpecificationTypeDef(BaseModel):
    audioFileS3Location: str

class AgentTurnResultTypeDef(BaseModel):
    expectedAgentPrompt: str
    actualAgentPrompt: Optional[str] = None
    errorDetails: Optional[ExecutionErrorDetailsTypeDef] = None
    actualElicitedSlot: Optional[str] = None
    actualIntent: Optional[str] = None

class AnalyticsIntentResultTypeDef(BaseModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsIntentGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsIntentMetricResultTypeDef]] = None

class AnalyticsIntentStageResultTypeDef(BaseModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsIntentStageGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsIntentStageMetricResultTypeDef]] = None

class AnalyticsSessionResultTypeDef(BaseModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsSessionGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsSessionMetricResultTypeDef]] = None

class AnalyticsUtteranceResultTypeDef(BaseModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsUtteranceGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsUtteranceMetricResultTypeDef]] = None
    attributeResults: Optional[List[AnalyticsUtteranceAttributeResultTypeDef]] = None

class SearchAssociatedTranscriptsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    filters: Sequence[AssociatedTranscriptFilterTypeDef]
    searchOrder: Optional[SearchOrderType] = None
    maxResults: Optional[int] = None
    nextIndex: Optional[int] = None

class AudioAndDTMFInputSpecificationTypeDef(BaseModel):
    startTimeoutMs: int
    audioSpecification: Optional[AudioSpecificationTypeDef] = None
    dtmfSpecification: Optional[DTMFSpecificationTypeDef] = None

class AudioLogDestinationTypeDef(BaseModel):
    s3Bucket: S3BucketLogDestinationTypeDef

class BatchCreateCustomVocabularyItemRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: Sequence[NewCustomVocabularyItemTypeDef]

class BatchUpdateCustomVocabularyItemRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: Sequence[CustomVocabularyItemTypeDef]

class BatchCreateCustomVocabularyItemResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItemTypeDef]
    resources: List[CustomVocabularyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteCustomVocabularyItemResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItemTypeDef]
    resources: List[CustomVocabularyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateCustomVocabularyItemResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItemTypeDef]
    resources: List[CustomVocabularyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BuildBotLocaleResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatusType
    lastBuildSubmittedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotReplicaResponseTypeDef(BaseModel):
    botId: str
    replicaRegion: str
    sourceRegion: str
    creationDateTime: datetime
    botReplicaStatus: BotReplicaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourcePolicyResponseTypeDef(BaseModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourcePolicyStatementResponseTypeDef(BaseModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUploadUrlResponseTypeDef(BaseModel):
    importId: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotAliasResponseTypeDef(BaseModel):
    botAliasId: str
    botId: str
    botAliasStatus: BotAliasStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotLocaleResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotReplicaResponseTypeDef(BaseModel):
    botId: str
    replicaRegion: str
    botReplicaStatus: BotReplicaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotResponseTypeDef(BaseModel):
    botId: str
    botStatus: BotStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotVersionResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    botStatus: BotStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomVocabularyResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyStatus: CustomVocabularyStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExportResponseTypeDef(BaseModel):
    exportId: str
    exportStatus: ExportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImportResponseTypeDef(BaseModel):
    importId: str
    importStatus: ImportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(BaseModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyStatementResponseTypeDef(BaseModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotReplicaResponseTypeDef(BaseModel):
    botId: str
    replicaRegion: str
    sourceRegion: str
    creationDateTime: datetime
    botReplicaStatus: BotReplicaStatusType
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotResourceGenerationResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    generationId: str
    failureReasons: List[str]
    generationStatus: GenerationStatusType
    generationInputPrompt: str
    generatedBotLocaleUrl: str
    creationDateTime: datetime
    modelArn: str
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomVocabularyMetadataResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyStatus: CustomVocabularyStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(BaseModel):
    resourceArn: str
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestExecutionArtifactsUrlResponseTypeDef(BaseModel):
    testExecutionId: str
    downloadArtifactsUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomVocabularyItemsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItems: List[CustomVocabularyItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIntentPathsResponseTypeDef(BaseModel):
    nodeSummaries: List[AnalyticsIntentNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAssociatedTranscriptsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    nextIndex: int
    associatedTranscripts: List[AssociatedTranscriptTypeDef]
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartBotResourceGenerationResponseTypeDef(BaseModel):
    generationInputPrompt: str
    generationId: str
    botId: str
    botVersion: str
    localeId: str
    generationStatus: GenerationStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopBotRecommendationResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourcePolicyResponseTypeDef(BaseModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteCustomVocabularyItemRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: Sequence[CustomVocabularyEntryIdTypeDef]

class DescriptiveBotBuilderSpecificationTypeDef(BaseModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecificationTypeDef] = None

class SampleUtteranceGenerationSpecificationTypeDef(BaseModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecificationTypeDef] = None

class SlotResolutionImprovementSpecificationTypeDef(BaseModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecificationTypeDef] = None

class ListBotAliasReplicasResponseTypeDef(BaseModel):
    botId: str
    sourceRegion: str
    replicaRegion: str
    botAliasReplicaSummaries: List[BotAliasReplicaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotAliasesResponseTypeDef(BaseModel):
    botAliasSummaries: List[BotAliasSummaryTypeDef]
    nextToken: str
    botId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestExecutionTargetTypeDef(BaseModel):
    botAliasTarget: Optional[BotAliasTestExecutionTargetTypeDef] = None

class BotImportSpecificationTypeDef(BaseModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: Optional[int] = None
    botTags: Optional[Dict[str, str]] = None
    testBotAliasTags: Optional[Dict[str, str]] = None

class BotLocaleImportSpecificationTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: Optional[float] = None
    voiceSettings: Optional[VoiceSettingsTypeDef] = None

class ListBotLocalesRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    sortBy: Optional[BotLocaleSortByTypeDef] = None
    filters: Optional[Sequence[BotLocaleFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotLocalesResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    nextToken: str
    botLocaleSummaries: List[BotLocaleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotRequestRequestTypeDef(BaseModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    description: Optional[str] = None
    botTags: Optional[Mapping[str, str]] = None
    testBotAliasTags: Optional[Mapping[str, str]] = None
    botType: Optional[BotTypeType] = None
    botMembers: Optional[Sequence[BotMemberTypeDef]] = None

class CreateBotResponseTypeDef(BaseModel):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    creationDateTime: datetime
    botTags: Dict[str, str]
    testBotAliasTags: Dict[str, str]
    botType: BotTypeType
    botMembers: List[BotMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotResponseTypeDef(BaseModel):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    botType: BotTypeType
    botMembers: List[BotMemberTypeDef]
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotRequestRequestTypeDef(BaseModel):
    botId: str
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    description: Optional[str] = None
    botType: Optional[BotTypeType] = None
    botMembers: Optional[Sequence[BotMemberTypeDef]] = None

class UpdateBotResponseTypeDef(BaseModel):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    botType: BotTypeType
    botMembers: List[BotMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BotRecommendationResultStatisticsTypeDef(BaseModel):
    intents: Optional[IntentStatisticsTypeDef] = None
    slotTypes: Optional[SlotTypeStatisticsTypeDef] = None

class ListBotRecommendationsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationSummaries: List[BotRecommendationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotReplicasResponseTypeDef(BaseModel):
    botId: str
    sourceRegion: str
    botReplicaSummaries: List[BotReplicaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotsRequestRequestTypeDef(BaseModel):
    sortBy: Optional[BotSortByTypeDef] = None
    filters: Optional[Sequence[BotFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotsResponseTypeDef(BaseModel):
    botSummaries: List[BotSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotVersionRequestRequestTypeDef(BaseModel):
    botId: str
    botVersionLocaleSpecification: Mapping[str, BotVersionLocaleDetailsTypeDef]
    description: Optional[str] = None

class CreateBotVersionResponseTypeDef(BaseModel):
    botId: str
    description: str
    botVersion: str
    botVersionLocaleSpecification: Dict[str, BotVersionLocaleDetailsTypeDef]
    botStatus: BotStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotVersionReplicasRequestRequestTypeDef(BaseModel):
    botId: str
    replicaRegion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[BotVersionReplicaSortByTypeDef] = None

class ListBotVersionReplicasResponseTypeDef(BaseModel):
    botId: str
    sourceRegion: str
    replicaRegion: str
    botVersionReplicaSummaries: List[BotVersionReplicaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotVersionsRequestRequestTypeDef(BaseModel):
    botId: str
    sortBy: Optional[BotVersionSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotVersionsResponseTypeDef(BaseModel):
    botId: str
    botVersionSummaries: List[BotVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuiltInIntentsRequestRequestTypeDef(BaseModel):
    localeId: str
    sortBy: Optional[BuiltInIntentSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBuiltInIntentsResponseTypeDef(BaseModel):
    builtInIntentSummaries: List[BuiltInIntentSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuiltInSlotTypesRequestRequestTypeDef(BaseModel):
    localeId: str
    sortBy: Optional[BuiltInSlotTypeSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBuiltInSlotTypesResponseTypeDef(BaseModel):
    builtInSlotTypeSummaries: List[BuiltInSlotTypeSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageResponseCardTypeDef(BaseModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[Sequence[ButtonTypeDef]] = None

class TextLogDestinationTypeDef(BaseModel):
    cloudWatch: CloudWatchLogGroupLogDestinationTypeDef

class CodeHookSpecificationTypeDef(BaseModel):
    lambdaCodeHook: LambdaCodeHookTypeDef

class CompositeSlotTypeSettingTypeDef(BaseModel):
    subSlots: Optional[Sequence[SubSlotTypeCompositionTypeDef]] = None

class ConversationLevelTestResultItemTypeDef(BaseModel):
    conversationId: str
    endToEndResult: TestResultMatchStatusType
    intentClassificationResults: List[ConversationLevelIntentClassificationResultItemTypeDef]
    slotResolutionResults: List[ConversationLevelSlotResolutionResultItemTypeDef]
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None

class TestExecutionResultFilterByTypeDef(BaseModel):
    resultTypeFilter: TestResultTypeFilterType
    conversationLevelTestResultsFilterBy: Optional[       ConversationLevelTestResultsFilterByTypeDef     ] = None

class ConversationLogsDataSourceTypeDef(BaseModel):
    botId: str
    botAliasId: str
    localeId: str
    filter: ConversationLogsDataSourceFilterByTypeDef

class IntentSummaryTypeDef(BaseModel):
    intentId: Optional[str] = None
    intentName: Optional[str] = None
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    inputContexts: Optional[List[InputContextTypeDef]] = None
    outputContexts: Optional[List[OutputContextTypeDef]] = None
    lastUpdatedDateTime: Optional[datetime] = None

class GenerateBotElementResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    sampleUtterances: List[SampleUtteranceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourcePolicyStatementRequestRequestTypeDef(BaseModel):
    resourceArn: str
    statementId: str
    effect: EffectType
    principal: Sequence[PrincipalTypeDef]
    action: Sequence[str]
    condition: Optional[Mapping[str, Mapping[str, str]]] = None
    expectedRevisionId: Optional[str] = None

class LexTranscriptFilterTypeDef(BaseModel):
    dateRangeFilter: Optional[DateRangeFilterTypeDef] = None

class DescribeBotAliasRequestBotAliasAvailableWaitTypeDef(BaseModel):
    botAliasId: str
    botId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotRequestBotAvailableWaitTypeDef(BaseModel):
    botId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotVersionRequestBotVersionAvailableWaitTypeDef(BaseModel):
    botId: str
    botVersion: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeExportRequestBotExportCompletedWaitTypeDef(BaseModel):
    exportId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImportRequestBotImportCompletedWaitTypeDef(BaseModel):
    importId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotVersionResponseTypeDef(BaseModel):
    botId: str
    botName: str
    botVersion: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    parentBotNetworks: List[ParentBotNetworkTypeDef]
    botType: BotTypeType
    botMembers: List[BotMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotRecommendationRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    encryptionSetting: EncryptionSettingTypeDef

class DescribeTestSetResponseTypeDef(BaseModel):
    testSetId: str
    testSetName: str
    description: str
    modality: TestSetModalityType
    status: TestSetStatusType
    roleArn: str
    numTurns: int
    storageLocation: TestSetStorageLocationTypeDef
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TestSetSummaryTypeDef(BaseModel):
    testSetId: Optional[str] = None
    testSetName: Optional[str] = None
    description: Optional[str] = None
    modality: Optional[TestSetModalityType] = None
    status: Optional[TestSetStatusType] = None
    roleArn: Optional[str] = None
    numTurns: Optional[int] = None
    storageLocation: Optional[TestSetStorageLocationTypeDef] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class UpdateTestSetResponseTypeDef(BaseModel):
    testSetId: str
    testSetName: str
    description: str
    modality: TestSetModalityType
    status: TestSetStatusType
    roleArn: str
    numTurns: int
    storageLocation: TestSetStorageLocationTypeDef
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DialogStateTypeDef(BaseModel):
    dialogAction: Optional[DialogActionTypeDef] = None
    intent: Optional[IntentOverrideTypeDef] = None
    sessionAttributes: Optional[Mapping[str, str]] = None

class OpensearchConfigurationTypeDef(BaseModel):
    domainEndpoint: str
    indexName: str
    exactResponse: Optional[bool] = None
    exactResponseFields: Optional[ExactResponseFieldsTypeDef] = None
    includeFields: Optional[Sequence[str]] = None

class ExportResourceSpecificationTypeDef(BaseModel):
    botExportSpecification: Optional[BotExportSpecificationTypeDef] = None
    botLocaleExportSpecification: Optional[BotLocaleExportSpecificationTypeDef] = None
    customVocabularyExportSpecification: Optional[       CustomVocabularyExportSpecificationTypeDef     ] = None
    testSetExportSpecification: Optional[TestSetExportSpecificationTypeDef] = None

class ListExportsRequestRequestTypeDef(BaseModel):
    botId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[ExportSortByTypeDef] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    localeId: Optional[str] = None

class ListBotResourceGenerationsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[GenerationSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotResourceGenerationsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    generationSummaries: List[GenerationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GrammarSlotTypeSettingTypeDef(BaseModel):
    source: Optional[GrammarSlotTypeSourceTypeDef] = None

class ListImportsRequestRequestTypeDef(BaseModel):
    botId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[ImportSortByTypeDef] = None
    filters: Optional[Sequence[ImportFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    localeId: Optional[str] = None

class ListImportsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    importSummaries: List[ImportSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class InputSessionStateSpecificationTypeDef(BaseModel):
    sessionAttributes: Optional[Dict[str, str]] = None
    activeContexts: Optional[List[ActiveContextTypeDef]] = None
    runtimeHints: Optional[RuntimeHintsTypeDef] = None

class IntentClassificationTestResultItemTypeDef(BaseModel):
    intentName: str
    multiTurnConversation: bool
    resultCounts: IntentClassificationTestResultItemCountsTypeDef

class ListIntentsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[IntentSortByTypeDef] = None
    filters: Optional[Sequence[IntentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SessionSpecificationTypeDef(BaseModel):
    botAliasId: Optional[str] = None
    botVersion: Optional[str] = None
    localeId: Optional[str] = None
    channel: Optional[str] = None
    sessionId: Optional[str] = None
    conversationStartTime: Optional[datetime] = None
    conversationEndTime: Optional[datetime] = None
    conversationDurationSeconds: Optional[int] = None
    conversationEndState: Optional[ConversationEndStateType] = None
    mode: Optional[AnalyticsModalityType] = None
    numberOfTurns: Optional[int] = None
    invokedIntentSamples: Optional[List[InvokedIntentSampleTypeDef]] = None
    originatingRequestId: Optional[str] = None

class ListIntentMetricsRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsIntentMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsIntentGroupBySpecificationTypeDef]] = None
    filters: Optional[Sequence[AnalyticsIntentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIntentPathsRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    intentPath: str
    filters: Optional[Sequence[AnalyticsPathFilterTypeDef]] = None

class ListIntentStageMetricsRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsIntentStageMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsIntentStageGroupBySpecificationTypeDef]] = None
    filters: Optional[Sequence[AnalyticsIntentStageFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSessionMetricsRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsSessionMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsSessionGroupBySpecificationTypeDef]] = None
    filters: Optional[Sequence[AnalyticsSessionFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListUtteranceMetricsRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsUtteranceMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsUtteranceGroupBySpecificationTypeDef]] = None
    attributes: Optional[Sequence[AnalyticsUtteranceAttributeTypeDef]] = None
    filters: Optional[Sequence[AnalyticsUtteranceFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRecommendedIntentsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    summaryList: List[RecommendedIntentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionAnalyticsDataRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    sortBy: Optional[SessionDataSortByTypeDef] = None
    filters: Optional[Sequence[AnalyticsSessionFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSlotTypesRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[SlotTypeSortByTypeDef] = None
    filters: Optional[Sequence[SlotTypeFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSlotTypesResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    slotTypeSummaries: List[SlotTypeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSlotsRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    sortBy: Optional[SlotSortByTypeDef] = None
    filters: Optional[Sequence[SlotFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTestExecutionsRequestRequestTypeDef(BaseModel):
    sortBy: Optional[TestExecutionSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTestSetsRequestRequestTypeDef(BaseModel):
    sortBy: Optional[TestSetSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListUtteranceAnalyticsDataRequestRequestTypeDef(BaseModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    sortBy: Optional[UtteranceDataSortByTypeDef] = None
    filters: Optional[Sequence[AnalyticsUtteranceFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class OverallTestResultsTypeDef(BaseModel):
    items: List[OverallTestResultItemTypeDef]

class UtteranceAggregationDurationTypeDef(BaseModel):
    relativeAggregationDuration: RelativeAggregationDurationTypeDef

class RuntimeHintDetailsTypeDef(BaseModel):
    runtimeHintValues: Optional[List[RuntimeHintValueTypeDef]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None

class SlotTypeValueTypeDef(BaseModel):
    sampleValue: Optional[SampleValueTypeDef] = None
    synonyms: Optional[Sequence[SampleValueTypeDef]] = None

class SlotDefaultValueSpecificationTypeDef(BaseModel):
    defaultValueList: Sequence[SlotDefaultValueTypeDef]

class SlotResolutionTestResultItemTypeDef(BaseModel):
    slotName: str
    resultCounts: SlotResolutionTestResultItemCountsTypeDef

class SlotValueOverrideTypeDef(BaseModel):
    shape: Optional[SlotShapeType] = None
    value: Optional[SlotValueTypeDef] = None
    values: Optional[Sequence[Dict[str, Any]]] = None

class SlotValueSelectionSettingTypeDef(BaseModel):
    resolutionStrategy: SlotValueResolutionStrategyType
    regexFilter: Optional[SlotValueRegexFilterTypeDef] = None
    advancedRecognitionSetting: Optional[AdvancedRecognitionSettingTypeDef] = None

class TestSetDiscrepancyErrorsTypeDef(BaseModel):
    intentDiscrepancies: List[TestSetIntentDiscrepancyItemTypeDef]
    slotDiscrepancies: List[TestSetSlotDiscrepancyItemTypeDef]

class TestSetDiscrepancyReportResourceTargetTypeDef(BaseModel):
    botAliasTarget: Optional[TestSetDiscrepancyReportBotAliasTargetTypeDef] = None

class TestSetImportResourceSpecificationTypeDef(BaseModel):
    testSetName: str
    roleArn: str
    storageLocation: TestSetStorageLocationTypeDef
    importInputLocation: TestSetImportInputLocationTypeDef
    modality: TestSetModalityType
    description: Optional[str] = None
    testSetTags: Optional[Dict[str, str]] = None

class UserTurnOutputSpecificationTypeDef(BaseModel):
    intent: UserTurnIntentOutputTypeDef
    activeContexts: Optional[List[ActiveContextTypeDef]] = None
    transcript: Optional[str] = None

class UtteranceInputSpecificationTypeDef(BaseModel):
    textInput: Optional[str] = None
    audioInput: Optional[UtteranceAudioInputSpecificationTypeDef] = None

class ListIntentMetricsResponseTypeDef(BaseModel):
    botId: str
    results: List[AnalyticsIntentResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIntentStageMetricsResponseTypeDef(BaseModel):
    botId: str
    results: List[AnalyticsIntentStageResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionMetricsResponseTypeDef(BaseModel):
    botId: str
    results: List[AnalyticsSessionResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUtteranceMetricsResponseTypeDef(BaseModel):
    botId: str
    results: List[AnalyticsUtteranceResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PromptAttemptSpecificationTypeDef(BaseModel):
    allowedInputTypes: AllowedInputTypesTypeDef
    allowInterrupt: Optional[bool] = None
    audioAndDTMFInputSpecification: Optional[AudioAndDTMFInputSpecificationTypeDef] = None
    textInputSpecification: Optional[TextInputSpecificationTypeDef] = None

class AudioLogSettingTypeDef(BaseModel):
    enabled: bool
    destination: AudioLogDestinationTypeDef
    selectiveLoggingEnabled: Optional[bool] = None

class BuildtimeSettingsTypeDef(BaseModel):
    descriptiveBotBuilder: Optional[DescriptiveBotBuilderSpecificationTypeDef] = None
    sampleUtteranceGeneration: Optional[SampleUtteranceGenerationSpecificationTypeDef] = None

class RuntimeSettingsTypeDef(BaseModel):
    slotResolutionImprovement: Optional[SlotResolutionImprovementSpecificationTypeDef] = None

class DescribeTestExecutionResponseTypeDef(BaseModel):
    testExecutionId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    testExecutionStatus: TestExecutionStatusType
    testSetId: str
    testSetName: str
    target: TestExecutionTargetTypeDef
    apiMode: TestExecutionApiModeType
    testExecutionModality: TestExecutionModalityType
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTestExecutionRequestRequestTypeDef(BaseModel):
    testSetId: str
    target: TestExecutionTargetTypeDef
    apiMode: TestExecutionApiModeType
    testExecutionModality: Optional[TestExecutionModalityType] = None

class StartTestExecutionResponseTypeDef(BaseModel):
    testExecutionId: str
    creationDateTime: datetime
    testSetId: str
    target: TestExecutionTargetTypeDef
    apiMode: TestExecutionApiModeType
    testExecutionModality: TestExecutionModalityType
    ResponseMetadata: ResponseMetadataTypeDef

class TestExecutionSummaryTypeDef(BaseModel):
    testExecutionId: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    testExecutionStatus: Optional[TestExecutionStatusType] = None
    testSetId: Optional[str] = None
    testSetName: Optional[str] = None
    target: Optional[TestExecutionTargetTypeDef] = None
    apiMode: Optional[TestExecutionApiModeType] = None
    testExecutionModality: Optional[TestExecutionModalityType] = None

class BotRecommendationResultsTypeDef(BaseModel):
    botLocaleExportUrl: Optional[str] = None
    associatedTranscriptsUrl: Optional[str] = None
    statistics: Optional[BotRecommendationResultStatisticsTypeDef] = None

class MessageTypeDef(BaseModel):
    plainTextMessage: Optional[PlainTextMessageTypeDef] = None
    customPayload: Optional[CustomPayloadTypeDef] = None
    ssmlMessage: Optional[SSMLMessageTypeDef] = None
    imageResponseCard: Optional[ImageResponseCardTypeDef] = None

class UtteranceBotResponseTypeDef(BaseModel):
    content: Optional[str] = None
    contentType: Optional[UtteranceContentTypeType] = None
    imageResponseCard: Optional[ImageResponseCardTypeDef] = None

class TextLogSettingTypeDef(BaseModel):
    enabled: bool
    destination: TextLogDestinationTypeDef
    selectiveLoggingEnabled: Optional[bool] = None

class BotAliasLocaleSettingsTypeDef(BaseModel):
    enabled: bool
    codeHookSpecification: Optional[CodeHookSpecificationTypeDef] = None

class ConversationLevelTestResultsTypeDef(BaseModel):
    items: List[ConversationLevelTestResultItemTypeDef]

class ListTestExecutionResultItemsRequestRequestTypeDef(BaseModel):
    testExecutionId: str
    resultFilterBy: TestExecutionResultFilterByTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TestSetGenerationDataSourceTypeDef(BaseModel):
    conversationLogsDataSource: Optional[ConversationLogsDataSourceTypeDef] = None

class ListIntentsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    intentSummaries: List[IntentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TranscriptFilterTypeDef(BaseModel):
    lexTranscriptFilter: Optional[LexTranscriptFilterTypeDef] = None

class ListTestSetsResponseTypeDef(BaseModel):
    testSets: List[TestSetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationTypeDef(BaseModel):
    opensearchConfiguration: Optional[OpensearchConfigurationTypeDef] = None
    kendraConfiguration: Optional[QnAKendraConfigurationTypeDef] = None
    bedrockKnowledgeStoreConfiguration: Optional[       BedrockKnowledgeStoreConfigurationTypeDef     ] = None

class CreateExportRequestRequestTypeDef(BaseModel):
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    filePassword: Optional[str] = None

class CreateExportResponseTypeDef(BaseModel):
    exportId: str
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportResponseTypeDef(BaseModel):
    exportId: str
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    failureReasons: List[str]
    downloadUrl: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSummaryTypeDef(BaseModel):
    exportId: Optional[str] = None
    resourceSpecification: Optional[ExportResourceSpecificationTypeDef] = None
    fileFormat: Optional[ImportExportFileFormatType] = None
    exportStatus: Optional[ExportStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class UpdateExportResponseTypeDef(BaseModel):
    exportId: str
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ExternalSourceSettingTypeDef(BaseModel):
    grammarSlotTypeSetting: Optional[GrammarSlotTypeSettingTypeDef] = None

class IntentClassificationTestResultsTypeDef(BaseModel):
    items: List[IntentClassificationTestResultItemTypeDef]

class ListSessionAnalyticsDataResponseTypeDef(BaseModel):
    botId: str
    nextToken: str
    sessions: List[SessionSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregatedUtterancesRequestRequestTypeDef(BaseModel):
    botId: str
    localeId: str
    aggregationDuration: UtteranceAggregationDurationTypeDef
    botAliasId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[AggregatedUtterancesSortByTypeDef] = None
    filters: Optional[Sequence[AggregatedUtterancesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAggregatedUtterancesResponseTypeDef(BaseModel):
    botId: str
    botAliasId: str
    botVersion: str
    localeId: str
    aggregationDuration: UtteranceAggregationDurationTypeDef
    aggregationWindowStartTime: datetime
    aggregationWindowEndTime: datetime
    aggregationLastRefreshedDateTime: datetime
    aggregatedUtterancesSummaries: List[AggregatedUtterancesSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IntentLevelSlotResolutionTestResultItemTypeDef(BaseModel):
    intentName: str
    multiTurnConversation: bool
    slotResolutionResults: List[SlotResolutionTestResultItemTypeDef]

class CreateTestSetDiscrepancyReportRequestRequestTypeDef(BaseModel):
    testSetId: str
    target: TestSetDiscrepancyReportResourceTargetTypeDef

class CreateTestSetDiscrepancyReportResponseTypeDef(BaseModel):
    testSetDiscrepancyReportId: str
    creationDateTime: datetime
    testSetId: str
    target: TestSetDiscrepancyReportResourceTargetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTestSetDiscrepancyReportResponseTypeDef(BaseModel):
    testSetDiscrepancyReportId: str
    testSetId: str
    creationDateTime: datetime
    target: TestSetDiscrepancyReportResourceTargetTypeDef
    testSetDiscrepancyReportStatus: TestSetDiscrepancyReportStatusType
    lastUpdatedDataTime: datetime
    testSetDiscrepancyTopErrors: TestSetDiscrepancyErrorsTypeDef
    testSetDiscrepancyRawOutputUrl: str
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportResourceSpecificationTypeDef(BaseModel):
    botImportSpecification: Optional[BotImportSpecificationTypeDef] = None
    botLocaleImportSpecification: Optional[BotLocaleImportSpecificationTypeDef] = None
    customVocabularyImportSpecification: Optional[       CustomVocabularyImportSpecificationTypeDef     ] = None
    testSetImportResourceSpecification: Optional[       TestSetImportResourceSpecificationTypeDef     ] = None

class UserTurnInputSpecificationTypeDef(BaseModel):
    utteranceInput: UtteranceInputSpecificationTypeDef
    requestAttributes: Optional[Dict[str, str]] = None
    sessionState: Optional[InputSessionStateSpecificationTypeDef] = None

class GenerativeAISettingsTypeDef(BaseModel):
    runtimeSettings: Optional[RuntimeSettingsTypeDef] = None
    buildtimeSettings: Optional[BuildtimeSettingsTypeDef] = None

class ListTestExecutionsResponseTypeDef(BaseModel):
    testExecutions: List[TestExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageGroupTypeDef(BaseModel):
    message: MessageTypeDef
    variations: Optional[Sequence[MessageTypeDef]] = None

class UtteranceSpecificationTypeDef(BaseModel):
    botAliasId: Optional[str] = None
    botVersion: Optional[str] = None
    localeId: Optional[str] = None
    sessionId: Optional[str] = None
    channel: Optional[str] = None
    mode: Optional[AnalyticsModalityType] = None
    conversationStartTime: Optional[datetime] = None
    conversationEndTime: Optional[datetime] = None
    utterance: Optional[str] = None
    utteranceTimestamp: Optional[datetime] = None
    audioVoiceDurationMillis: Optional[int] = None
    utteranceUnderstood: Optional[bool] = None
    inputType: Optional[str] = None
    outputType: Optional[str] = None
    associatedIntentName: Optional[str] = None
    associatedSlotName: Optional[str] = None
    intentState: Optional[IntentStateType] = None
    dialogActionType: Optional[str] = None
    botResponseAudioVoiceId: Optional[str] = None
    slotsFilledInSession: Optional[str] = None
    utteranceRequestId: Optional[str] = None
    botResponses: Optional[List[UtteranceBotResponseTypeDef]] = None

class ConversationLogSettingsTypeDef(BaseModel):
    textLogSettings: Optional[Sequence[TextLogSettingTypeDef]] = None
    audioLogSettings: Optional[Sequence[AudioLogSettingTypeDef]] = None

class DescribeTestSetGenerationResponseTypeDef(BaseModel):
    testSetGenerationId: str
    testSetGenerationStatus: TestSetGenerationStatusType
    failureReasons: List[str]
    testSetId: str
    testSetName: str
    description: str
    storageLocation: TestSetStorageLocationTypeDef
    generationDataSource: TestSetGenerationDataSourceTypeDef
    roleArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartTestSetGenerationRequestRequestTypeDef(BaseModel):
    testSetName: str
    storageLocation: TestSetStorageLocationTypeDef
    generationDataSource: TestSetGenerationDataSourceTypeDef
    roleArn: str
    description: Optional[str] = None
    testSetTags: Optional[Mapping[str, str]] = None

class StartTestSetGenerationResponseTypeDef(BaseModel):
    testSetGenerationId: str
    creationDateTime: datetime
    testSetGenerationStatus: TestSetGenerationStatusType
    testSetName: str
    description: str
    storageLocation: TestSetStorageLocationTypeDef
    generationDataSource: TestSetGenerationDataSourceTypeDef
    roleArn: str
    testSetTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class S3BucketTranscriptSourceTypeDef(BaseModel):
    s3BucketName: str
    transcriptFormat: Literal["Lex"]
    pathFormat: Optional[PathFormatTypeDef] = None
    transcriptFilter: Optional[TranscriptFilterTypeDef] = None
    kmsKeyArn: Optional[str] = None

class QnAIntentConfigurationTypeDef(BaseModel):
    dataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None
    bedrockModelConfiguration: Optional[BedrockModelSpecificationTypeDef] = None

class ListExportsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    exportSummaries: List[ExportSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSlotTypeRequestRequestTypeDef(BaseModel):
    slotTypeName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    slotTypeValues: Optional[Sequence[SlotTypeValueTypeDef]] = None
    valueSelectionSetting: Optional[SlotValueSelectionSettingTypeDef] = None
    parentSlotTypeSignature: Optional[str] = None
    externalSourceSetting: Optional[ExternalSourceSettingTypeDef] = None
    compositeSlotTypeSetting: Optional[CompositeSlotTypeSettingTypeDef] = None

class CreateSlotTypeResponseTypeDef(BaseModel):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List[SlotTypeValueTypeDef]
    valueSelectionSetting: SlotValueSelectionSettingTypeDef
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    externalSourceSetting: ExternalSourceSettingTypeDef
    compositeSlotTypeSetting: CompositeSlotTypeSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlotTypeResponseTypeDef(BaseModel):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List[SlotTypeValueTypeDef]
    valueSelectionSetting: SlotValueSelectionSettingTypeDef
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    externalSourceSetting: ExternalSourceSettingTypeDef
    compositeSlotTypeSetting: CompositeSlotTypeSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSlotTypeRequestRequestTypeDef(BaseModel):
    slotTypeId: str
    slotTypeName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    slotTypeValues: Optional[Sequence[SlotTypeValueTypeDef]] = None
    valueSelectionSetting: Optional[SlotValueSelectionSettingTypeDef] = None
    parentSlotTypeSignature: Optional[str] = None
    externalSourceSetting: Optional[ExternalSourceSettingTypeDef] = None
    compositeSlotTypeSetting: Optional[CompositeSlotTypeSettingTypeDef] = None

class UpdateSlotTypeResponseTypeDef(BaseModel):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List[SlotTypeValueTypeDef]
    valueSelectionSetting: SlotValueSelectionSettingTypeDef
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    externalSourceSetting: ExternalSourceSettingTypeDef
    compositeSlotTypeSetting: CompositeSlotTypeSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntentLevelSlotResolutionTestResultsTypeDef(BaseModel):
    items: List[IntentLevelSlotResolutionTestResultItemTypeDef]

class DescribeImportResponseTypeDef(BaseModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationTypeDef
    importedResourceId: str
    importedResourceName: str
    mergeStrategy: MergeStrategyType
    importStatus: ImportStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportRequestRequestTypeDef(BaseModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationTypeDef
    mergeStrategy: MergeStrategyType
    filePassword: Optional[str] = None

class StartImportResponseTypeDef(BaseModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationTypeDef
    mergeStrategy: MergeStrategyType
    importStatus: ImportStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UserTurnResultTypeDef(BaseModel):
    input: UserTurnInputSpecificationTypeDef
    expectedOutput: UserTurnOutputSpecificationTypeDef
    actualOutput: Optional[UserTurnOutputSpecificationTypeDef] = None
    errorDetails: Optional[ExecutionErrorDetailsTypeDef] = None
    endToEndResult: Optional[TestResultMatchStatusType] = None
    intentMatchResult: Optional[TestResultMatchStatusType] = None
    slotMatchResult: Optional[TestResultMatchStatusType] = None
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None
    conversationLevelResult: Optional[ConversationLevelResultDetailTypeDef] = None

class UserTurnSpecificationTypeDef(BaseModel):
    input: UserTurnInputSpecificationTypeDef
    expected: UserTurnOutputSpecificationTypeDef

class CreateBotLocaleRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: float
    description: Optional[str] = None
    voiceSettings: Optional[VoiceSettingsTypeDef] = None
    generativeAISettings: Optional[GenerativeAISettingsTypeDef] = None

class CreateBotLocaleResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeName: str
    localeId: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: VoiceSettingsTypeDef
    botLocaleStatus: BotLocaleStatusType
    creationDateTime: datetime
    generativeAISettings: GenerativeAISettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotLocaleResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    localeName: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: VoiceSettingsTypeDef
    intentsCount: int
    slotTypesCount: int
    botLocaleStatus: BotLocaleStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    lastBuildSubmittedDateTime: datetime
    botLocaleHistoryEvents: List[BotLocaleHistoryEventTypeDef]
    recommendedActions: List[str]
    generativeAISettings: GenerativeAISettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotLocaleRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: float
    description: Optional[str] = None
    voiceSettings: Optional[VoiceSettingsTypeDef] = None
    generativeAISettings: Optional[GenerativeAISettingsTypeDef] = None

class UpdateBotLocaleResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    localeName: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: VoiceSettingsTypeDef
    botLocaleStatus: BotLocaleStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    recommendedActions: List[str]
    generativeAISettings: GenerativeAISettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FulfillmentStartResponseSpecificationTypeDef(BaseModel):
    delayInSeconds: int
    messageGroups: Sequence[MessageGroupTypeDef]
    allowInterrupt: Optional[bool] = None

class FulfillmentUpdateResponseSpecificationTypeDef(BaseModel):
    frequencyInSeconds: int
    messageGroups: Sequence[MessageGroupTypeDef]
    allowInterrupt: Optional[bool] = None

class PromptSpecificationTypeDef(BaseModel):
    messageGroups: Sequence[MessageGroupTypeDef]
    maxRetries: int
    allowInterrupt: Optional[bool] = None
    messageSelectionStrategy: Optional[MessageSelectionStrategyType] = None
    promptAttemptsSpecification: Optional[       Mapping[PromptAttemptType, PromptAttemptSpecificationTypeDef] = None

class ResponseSpecificationTypeDef(BaseModel):
    messageGroups: Sequence[MessageGroupTypeDef]
    allowInterrupt: Optional[bool] = None

class StillWaitingResponseSpecificationTypeDef(BaseModel):
    messageGroups: Sequence[MessageGroupTypeDef]
    frequencyInSeconds: int
    timeoutInSeconds: int
    allowInterrupt: Optional[bool] = None

class ListUtteranceAnalyticsDataResponseTypeDef(BaseModel):
    botId: str
    nextToken: str
    utterances: List[UtteranceSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotAliasRequestRequestTypeDef(BaseModel):
    botAliasName: str
    botId: str
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasLocaleSettings: Optional[Mapping[str, BotAliasLocaleSettingsTypeDef]] = None
    conversationLogSettings: Optional[ConversationLogSettingsTypeDef] = None
    sentimentAnalysisSettings: Optional[SentimentAnalysisSettingsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateBotAliasResponseTypeDef(BaseModel):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, BotAliasLocaleSettingsTypeDef]
    conversationLogSettings: ConversationLogSettingsTypeDef
    sentimentAnalysisSettings: SentimentAnalysisSettingsTypeDef
    botAliasStatus: BotAliasStatusType
    botId: str
    creationDateTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotAliasResponseTypeDef(BaseModel):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, BotAliasLocaleSettingsTypeDef]
    conversationLogSettings: ConversationLogSettingsTypeDef
    sentimentAnalysisSettings: SentimentAnalysisSettingsTypeDef
    botAliasHistoryEvents: List[BotAliasHistoryEventTypeDef]
    botAliasStatus: BotAliasStatusType
    botId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    parentBotNetworks: List[ParentBotNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotAliasRequestRequestTypeDef(BaseModel):
    botAliasId: str
    botAliasName: str
    botId: str
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasLocaleSettings: Optional[Mapping[str, BotAliasLocaleSettingsTypeDef]] = None
    conversationLogSettings: Optional[ConversationLogSettingsTypeDef] = None
    sentimentAnalysisSettings: Optional[SentimentAnalysisSettingsTypeDef] = None

class UpdateBotAliasResponseTypeDef(BaseModel):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, BotAliasLocaleSettingsTypeDef]
    conversationLogSettings: ConversationLogSettingsTypeDef
    sentimentAnalysisSettings: SentimentAnalysisSettingsTypeDef
    botAliasStatus: BotAliasStatusType
    botId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TranscriptSourceSettingTypeDef(BaseModel):
    s3BucketTranscriptSource: Optional[S3BucketTranscriptSourceTypeDef] = None

class TestSetTurnResultTypeDef(BaseModel):
    agent: Optional[AgentTurnResultTypeDef] = None
    user: Optional[UserTurnResultTypeDef] = None

class TurnSpecificationTypeDef(BaseModel):
    agentTurn: Optional[AgentTurnSpecificationTypeDef] = None
    userTurn: Optional[UserTurnSpecificationTypeDef] = None

class FulfillmentUpdatesSpecificationTypeDef(BaseModel):
    active: bool
    startResponse: Optional[FulfillmentStartResponseSpecificationTypeDef] = None
    updateResponse: Optional[FulfillmentUpdateResponseSpecificationTypeDef] = None
    timeoutInSeconds: Optional[int] = None

class SlotSummaryTypeDef(BaseModel):
    slotId: Optional[str] = None
    slotName: Optional[str] = None
    description: Optional[str] = None
    slotConstraint: Optional[SlotConstraintType] = None
    slotTypeId: Optional[str] = None
    valueElicitationPromptSpecification: Optional[PromptSpecificationTypeDef] = None
    lastUpdatedDateTime: Optional[datetime] = None

class ConditionalBranchTypeDef(BaseModel):
    name: str
    condition: ConditionTypeDef
    nextStep: DialogStateTypeDef
    response: Optional[ResponseSpecificationTypeDef] = None

class DefaultConditionalBranchTypeDef(BaseModel):
    nextStep: Optional[DialogStateTypeDef] = None
    response: Optional[ResponseSpecificationTypeDef] = None

class WaitAndContinueSpecificationTypeDef(BaseModel):
    waitingResponse: ResponseSpecificationTypeDef
    continueResponse: ResponseSpecificationTypeDef
    stillWaitingResponse: Optional[StillWaitingResponseSpecificationTypeDef] = None
    active: Optional[bool] = None

class DescribeBotRecommendationResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingTypeDef
    encryptionSetting: EncryptionSettingTypeDef
    botRecommendationResults: BotRecommendationResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartBotRecommendationRequestRequestTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    transcriptSourceSetting: TranscriptSourceSettingTypeDef
    encryptionSetting: Optional[EncryptionSettingTypeDef] = None

class StartBotRecommendationResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingTypeDef
    encryptionSetting: EncryptionSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotRecommendationResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingTypeDef
    encryptionSetting: EncryptionSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UtteranceLevelTestResultItemTypeDef(BaseModel):
    recordNumber: int
    turnResult: TestSetTurnResultTypeDef
    conversationId: Optional[str] = None

class TestSetTurnRecordTypeDef(BaseModel):
    recordNumber: int
    turnSpecification: TurnSpecificationTypeDef
    conversationId: Optional[str] = None
    turnNumber: Optional[int] = None

class ListSlotsResponseTypeDef(BaseModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    slotSummaries: List[SlotSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConditionalSpecificationTypeDef(BaseModel):
    active: bool
    conditionalBranches: Sequence[ConditionalBranchTypeDef]
    defaultBranch: DefaultConditionalBranchTypeDef

class SubSlotValueElicitationSettingTypeDef(BaseModel):
    promptSpecification: PromptSpecificationTypeDef
    defaultValueSpecification: Optional[SlotDefaultValueSpecificationTypeDef] = None
    sampleUtterances: Optional[Sequence[SampleUtteranceTypeDef]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecificationTypeDef] = None

class UtteranceLevelTestResultsTypeDef(BaseModel):
    items: List[UtteranceLevelTestResultItemTypeDef]

class ListTestSetRecordsResponseTypeDef(BaseModel):
    testSetRecords: List[TestSetTurnRecordTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IntentClosingSettingTypeDef(BaseModel):
    closingResponse: Optional[ResponseSpecificationTypeDef] = None
    active: Optional[bool] = None
    nextStep: Optional[DialogStateTypeDef] = None
    conditional: Optional[ConditionalSpecificationTypeDef] = None

class PostDialogCodeHookInvocationSpecificationTypeDef(BaseModel):
    successResponse: Optional[ResponseSpecificationTypeDef] = None
    successNextStep: Optional[DialogStateTypeDef] = None
    successConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    timeoutResponse: Optional[ResponseSpecificationTypeDef] = None
    timeoutNextStep: Optional[DialogStateTypeDef] = None
    timeoutConditional: Optional[ConditionalSpecificationTypeDef] = None

class PostFulfillmentStatusSpecificationTypeDef(BaseModel):
    successResponse: Optional[ResponseSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    timeoutResponse: Optional[ResponseSpecificationTypeDef] = None
    successNextStep: Optional[DialogStateTypeDef] = None
    successConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    timeoutNextStep: Optional[DialogStateTypeDef] = None
    timeoutConditional: Optional[ConditionalSpecificationTypeDef] = None

class SpecificationsTypeDef(BaseModel):
    slotTypeId: str
    valueElicitationSetting: SubSlotValueElicitationSettingTypeDef

class TestExecutionResultItemsTypeDef(BaseModel):
    overallTestResults: Optional[OverallTestResultsTypeDef] = None
    conversationLevelTestResults: Optional[ConversationLevelTestResultsTypeDef] = None
    intentClassificationTestResults: Optional[IntentClassificationTestResultsTypeDef] = None
    intentLevelSlotResolutionTestResults: Optional[       IntentLevelSlotResolutionTestResultsTypeDef     ] = None
    utteranceLevelTestResults: Optional[UtteranceLevelTestResultsTypeDef] = None

class DialogCodeHookInvocationSettingTypeDef(BaseModel):
    enableCodeHookInvocation: bool
    active: bool
    postCodeHookSpecification: PostDialogCodeHookInvocationSpecificationTypeDef
    invocationLabel: Optional[str] = None

class FulfillmentCodeHookSettingsTypeDef(BaseModel):
    enabled: bool
    postFulfillmentStatusSpecification: Optional[       PostFulfillmentStatusSpecificationTypeDef     ] = None
    fulfillmentUpdatesSpecification: Optional[FulfillmentUpdatesSpecificationTypeDef] = None
    active: Optional[bool] = None

class SubSlotSettingTypeDef(BaseModel):
    expression: Optional[str] = None
    slotSpecifications: Optional[Mapping[str, SpecificationsTypeDef]] = None

class ListTestExecutionResultItemsResponseTypeDef(BaseModel):
    testExecutionResults: TestExecutionResultItemsTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitialResponseSettingTypeDef(BaseModel):
    initialResponse: Optional[ResponseSpecificationTypeDef] = None
    nextStep: Optional[DialogStateTypeDef] = None
    conditional: Optional[ConditionalSpecificationTypeDef] = None
    codeHook: Optional[DialogCodeHookInvocationSettingTypeDef] = None

class IntentConfirmationSettingTypeDef(BaseModel):
    promptSpecification: PromptSpecificationTypeDef
    declinationResponse: Optional[ResponseSpecificationTypeDef] = None
    active: Optional[bool] = None
    confirmationResponse: Optional[ResponseSpecificationTypeDef] = None
    confirmationNextStep: Optional[DialogStateTypeDef] = None
    confirmationConditional: Optional[ConditionalSpecificationTypeDef] = None
    declinationNextStep: Optional[DialogStateTypeDef] = None
    declinationConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    codeHook: Optional[DialogCodeHookInvocationSettingTypeDef] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSettingTypeDef] = None

class SlotCaptureSettingTypeDef(BaseModel):
    captureResponse: Optional[ResponseSpecificationTypeDef] = None
    captureNextStep: Optional[DialogStateTypeDef] = None
    captureConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    codeHook: Optional[DialogCodeHookInvocationSettingTypeDef] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSettingTypeDef] = None

class CreateIntentRequestRequestTypeDef(BaseModel):
    intentName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    sampleUtterances: Optional[Sequence[SampleUtteranceTypeDef]] = None
    dialogCodeHook: Optional[DialogCodeHookSettingsTypeDef] = None
    fulfillmentCodeHook: Optional[FulfillmentCodeHookSettingsTypeDef] = None
    intentConfirmationSetting: Optional[IntentConfirmationSettingTypeDef] = None
    intentClosingSetting: Optional[IntentClosingSettingTypeDef] = None
    inputContexts: Optional[Sequence[InputContextTypeDef]] = None
    outputContexts: Optional[Sequence[OutputContextTypeDef]] = None
    kendraConfiguration: Optional[KendraConfigurationTypeDef] = None
    initialResponseSetting: Optional[InitialResponseSettingTypeDef] = None
    qnAIntentConfiguration: Optional[QnAIntentConfigurationTypeDef] = None

class CreateIntentResponseTypeDef(BaseModel):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List[SampleUtteranceTypeDef]
    dialogCodeHook: DialogCodeHookSettingsTypeDef
    fulfillmentCodeHook: FulfillmentCodeHookSettingsTypeDef
    intentConfirmationSetting: IntentConfirmationSettingTypeDef
    intentClosingSetting: IntentClosingSettingTypeDef
    inputContexts: List[InputContextTypeDef]
    outputContexts: List[OutputContextTypeDef]
    kendraConfiguration: KendraConfigurationTypeDef
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    initialResponseSetting: InitialResponseSettingTypeDef
    qnAIntentConfiguration: QnAIntentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIntentResponseTypeDef(BaseModel):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List[SampleUtteranceTypeDef]
    dialogCodeHook: DialogCodeHookSettingsTypeDef
    fulfillmentCodeHook: FulfillmentCodeHookSettingsTypeDef
    slotPriorities: List[SlotPriorityTypeDef]
    intentConfirmationSetting: IntentConfirmationSettingTypeDef
    intentClosingSetting: IntentClosingSettingTypeDef
    inputContexts: List[InputContextTypeDef]
    outputContexts: List[OutputContextTypeDef]
    kendraConfiguration: KendraConfigurationTypeDef
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    initialResponseSetting: InitialResponseSettingTypeDef
    qnAIntentConfiguration: QnAIntentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIntentRequestRequestTypeDef(BaseModel):
    intentId: str
    intentName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    sampleUtterances: Optional[Sequence[SampleUtteranceTypeDef]] = None
    dialogCodeHook: Optional[DialogCodeHookSettingsTypeDef] = None
    fulfillmentCodeHook: Optional[FulfillmentCodeHookSettingsTypeDef] = None
    slotPriorities: Optional[Sequence[SlotPriorityTypeDef]] = None
    intentConfirmationSetting: Optional[IntentConfirmationSettingTypeDef] = None
    intentClosingSetting: Optional[IntentClosingSettingTypeDef] = None
    inputContexts: Optional[Sequence[InputContextTypeDef]] = None
    outputContexts: Optional[Sequence[OutputContextTypeDef]] = None
    kendraConfiguration: Optional[KendraConfigurationTypeDef] = None
    initialResponseSetting: Optional[InitialResponseSettingTypeDef] = None
    qnAIntentConfiguration: Optional[QnAIntentConfigurationTypeDef] = None

class UpdateIntentResponseTypeDef(BaseModel):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List[SampleUtteranceTypeDef]
    dialogCodeHook: DialogCodeHookSettingsTypeDef
    fulfillmentCodeHook: FulfillmentCodeHookSettingsTypeDef
    slotPriorities: List[SlotPriorityTypeDef]
    intentConfirmationSetting: IntentConfirmationSettingTypeDef
    intentClosingSetting: IntentClosingSettingTypeDef
    inputContexts: List[InputContextTypeDef]
    outputContexts: List[OutputContextTypeDef]
    kendraConfiguration: KendraConfigurationTypeDef
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    initialResponseSetting: InitialResponseSettingTypeDef
    qnAIntentConfiguration: QnAIntentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SlotValueElicitationSettingTypeDef(BaseModel):
    slotConstraint: SlotConstraintType
    defaultValueSpecification: Optional[SlotDefaultValueSpecificationTypeDef] = None
    promptSpecification: Optional[PromptSpecificationTypeDef] = None
    sampleUtterances: Optional[Sequence[SampleUtteranceTypeDef]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecificationTypeDef] = None
    slotCaptureSetting: Optional[SlotCaptureSettingTypeDef] = None
    slotResolutionSetting: Optional[SlotResolutionSettingTypeDef] = None

class CreateSlotRequestRequestTypeDef(BaseModel):
    slotName: str
    valueElicitationSetting: SlotValueElicitationSettingTypeDef
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    description: Optional[str] = None
    slotTypeId: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingTypeDef] = None
    multipleValuesSetting: Optional[MultipleValuesSettingTypeDef] = None
    subSlotSetting: Optional[SubSlotSettingTypeDef] = None

class CreateSlotResponseTypeDef(BaseModel):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: SlotValueElicitationSettingTypeDef
    obfuscationSetting: ObfuscationSettingTypeDef
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    multipleValuesSetting: MultipleValuesSettingTypeDef
    subSlotSetting: SubSlotSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlotResponseTypeDef(BaseModel):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: SlotValueElicitationSettingTypeDef
    obfuscationSetting: ObfuscationSettingTypeDef
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    multipleValuesSetting: MultipleValuesSettingTypeDef
    subSlotSetting: SubSlotSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSlotRequestRequestTypeDef(BaseModel):
    slotId: str
    slotName: str
    valueElicitationSetting: SlotValueElicitationSettingTypeDef
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    description: Optional[str] = None
    slotTypeId: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingTypeDef] = None
    multipleValuesSetting: Optional[MultipleValuesSettingTypeDef] = None
    subSlotSetting: Optional[SubSlotSettingTypeDef] = None

class UpdateSlotResponseTypeDef(BaseModel):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: SlotValueElicitationSettingTypeDef
    obfuscationSetting: ObfuscationSettingTypeDef
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    multipleValuesSetting: MultipleValuesSettingTypeDef
    subSlotSetting: SubSlotSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

