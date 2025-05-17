from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lexv2_models.lexv2_models_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActiveContext(BaseValidatorModel):
    name: str


class AdvancedRecognitionSetting(BaseValidatorModel):
    audioRecognitionStrategy: Optional[Literal['UseSlotValuesAsCustomVocabulary']] = None


class ExecutionErrorDetails(BaseValidatorModel):
    errorCode: str
    errorMessage: str


class AgentTurnSpecification(BaseValidatorModel):
    agentPrompt: str


class AggregatedUtterancesFilter(BaseValidatorModel):
    name: Literal['Utterance']
    values: List[str]
    operator: AggregatedUtterancesFilterOperatorType


class AggregatedUtterancesSortBy(BaseValidatorModel):
    attribute: AggregatedUtterancesSortAttributeType
    order: SortOrderType


class AggregatedUtterancesSummary(BaseValidatorModel):
    utterance: Optional[str] = None
    hitCount: Optional[int] = None
    missedCount: Optional[int] = None
    utteranceFirstRecordedInAggregationDuration: Optional[datetime] = None
    utteranceLastRecordedInAggregationDuration: Optional[datetime] = None
    containsDataFromDeletedResources: Optional[bool] = None


class AllowedInputTypes(BaseValidatorModel):
    allowAudioInput: bool
    allowDTMFInput: bool


class AnalyticsBinBySpecification(BaseValidatorModel):
    name: AnalyticsBinByNameType
    interval: AnalyticsIntervalType
    order: Optional[AnalyticsSortOrderType] = None


class AnalyticsBinKey(BaseValidatorModel):
    name: Optional[AnalyticsBinByNameType] = None
    value: Optional[int] = None


class AnalyticsIntentFilter(BaseValidatorModel):
    name: AnalyticsIntentFilterNameType
    operator: AnalyticsFilterOperatorType
    values: List[str]


class AnalyticsIntentGroupByKey(BaseValidatorModel):
    name: Optional[AnalyticsIntentFieldType] = None
    value: Optional[str] = None


class AnalyticsIntentGroupBySpecification(BaseValidatorModel):
    name: AnalyticsIntentFieldType


class AnalyticsIntentMetricResult(BaseValidatorModel):
    name: Optional[AnalyticsIntentMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None


class AnalyticsIntentMetric(BaseValidatorModel):
    name: AnalyticsIntentMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None


class AnalyticsIntentNodeSummary(BaseValidatorModel):
    intentName: Optional[str] = None
    intentPath: Optional[str] = None
    intentCount: Optional[int] = None
    intentLevel: Optional[int] = None
    nodeType: Optional[AnalyticsNodeTypeType] = None


class AnalyticsIntentStageFilter(BaseValidatorModel):
    name: AnalyticsIntentStageFilterNameType
    operator: AnalyticsFilterOperatorType
    values: List[str]


class AnalyticsIntentStageGroupByKey(BaseValidatorModel):
    name: Optional[AnalyticsIntentStageFieldType] = None
    value: Optional[str] = None


class AnalyticsIntentStageGroupBySpecification(BaseValidatorModel):
    name: AnalyticsIntentStageFieldType


class AnalyticsIntentStageMetricResult(BaseValidatorModel):
    name: Optional[AnalyticsIntentStageMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None


class AnalyticsIntentStageMetric(BaseValidatorModel):
    name: AnalyticsIntentStageMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None


class AnalyticsPathFilter(BaseValidatorModel):
    name: AnalyticsCommonFilterNameType
    operator: AnalyticsFilterOperatorType
    values: List[str]


class AnalyticsSessionFilter(BaseValidatorModel):
    name: AnalyticsSessionFilterNameType
    operator: AnalyticsFilterOperatorType
    values: List[str]


class AnalyticsSessionGroupByKey(BaseValidatorModel):
    name: Optional[AnalyticsSessionFieldType] = None
    value: Optional[str] = None


class AnalyticsSessionGroupBySpecification(BaseValidatorModel):
    name: AnalyticsSessionFieldType


class AnalyticsSessionMetricResult(BaseValidatorModel):
    name: Optional[AnalyticsSessionMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None


class AnalyticsSessionMetric(BaseValidatorModel):
    name: AnalyticsSessionMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None


class AnalyticsUtteranceAttributeResult(BaseValidatorModel):
    lastUsedIntent: Optional[str] = None


class AnalyticsUtteranceAttribute(BaseValidatorModel):
    name: Literal['LastUsedIntent']


class AnalyticsUtteranceFilter(BaseValidatorModel):
    name: AnalyticsUtteranceFilterNameType
    operator: AnalyticsFilterOperatorType
    values: List[str]


class AnalyticsUtteranceGroupByKey(BaseValidatorModel):
    name: Optional[AnalyticsUtteranceFieldType] = None
    value: Optional[str] = None


class AnalyticsUtteranceGroupBySpecification(BaseValidatorModel):
    name: AnalyticsUtteranceFieldType


class AnalyticsUtteranceMetricResult(BaseValidatorModel):
    name: Optional[AnalyticsUtteranceMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None


class AnalyticsUtteranceMetric(BaseValidatorModel):
    name: AnalyticsUtteranceMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None


class AssociatedTranscriptFilter(BaseValidatorModel):
    name: AssociatedTranscriptFilterNameType
    values: List[str]


class AssociatedTranscript(BaseValidatorModel):
    transcript: Optional[str] = None


class AudioSpecification(BaseValidatorModel):
    maxLengthMs: int
    endTimeoutMs: int


class DTMFSpecification(BaseValidatorModel):
    maxLength: int
    endTimeoutMs: int
    deletionCharacter: str
    endCharacter: str


class S3BucketLogDestination(BaseValidatorModel):
    s3BucketArn: str
    logPrefix: str
    kmsKeyArn: Optional[str] = None


class NewCustomVocabularyItem(BaseValidatorModel):
    phrase: str
    weight: Optional[int] = None
    displayAs: Optional[str] = None


class CustomVocabularyItem(BaseValidatorModel):
    itemId: str
    phrase: str
    weight: Optional[int] = None
    displayAs: Optional[str] = None


class FailedCustomVocabularyItem(BaseValidatorModel):
    itemId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomVocabularyEntryId(BaseValidatorModel):
    itemId: str


class BedrockGuardrailConfiguration(BaseValidatorModel):
    identifier: str
    version: str


class BedrockKnowledgeStoreExactResponseFields(BaseValidatorModel):
    answerField: Optional[str] = None


class BotAliasHistoryEvent(BaseValidatorModel):
    botVersion: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class BotAliasReplicaSummary(BaseValidatorModel):
    botAliasId: Optional[str] = None
    botAliasReplicationStatus: Optional[BotAliasReplicationStatusType] = None
    botVersion: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReasons: Optional[List[str]] = None


class BotAliasSummary(BaseValidatorModel):
    botAliasId: Optional[str] = None
    botAliasName: Optional[str] = None
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasStatus: Optional[BotAliasStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class BotAliasTestExecutionTarget(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str


class BotExportSpecification(BaseValidatorModel):
    botId: str
    botVersion: str


class BotFilter(BaseValidatorModel):
    name: BotFilterNameType
    values: List[str]
    operator: BotFilterOperatorType


class DataPrivacy(BaseValidatorModel):
    childDirected: bool


class BotLocaleExportSpecification(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


class BotLocaleFilter(BaseValidatorModel):
    name: Literal['BotLocaleName']
    values: List[str]
    operator: BotLocaleFilterOperatorType


class BotLocaleHistoryEvent(BaseValidatorModel):
    event: str
    eventDate: datetime


class VoiceSettings(BaseValidatorModel):
    voiceId: str
    engine: Optional[VoiceEngineType] = None


class BotLocaleSortBy(BaseValidatorModel):
    attribute: Literal['BotLocaleName']
    order: SortOrderType


class BotLocaleSummary(BaseValidatorModel):
    localeId: Optional[str] = None
    localeName: Optional[str] = None
    description: Optional[str] = None
    botLocaleStatus: Optional[BotLocaleStatusType] = None
    lastUpdatedDateTime: Optional[datetime] = None
    lastBuildSubmittedDateTime: Optional[datetime] = None


class BotMember(BaseValidatorModel):
    botMemberId: str
    botMemberName: str
    botMemberAliasId: str
    botMemberAliasName: str
    botMemberVersion: str


class IntentStatistics(BaseValidatorModel):
    discoveredIntentCount: Optional[int] = None


class SlotTypeStatistics(BaseValidatorModel):
    discoveredSlotTypeCount: Optional[int] = None


class BotRecommendationSummary(BaseValidatorModel):
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class BotReplicaSummary(BaseValidatorModel):
    replicaRegion: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    botReplicaStatus: Optional[BotReplicaStatusType] = None
    failureReasons: Optional[List[str]] = None


class BotSortBy(BaseValidatorModel):
    attribute: Literal['BotName']
    order: SortOrderType


class BotSummary(BaseValidatorModel):
    botId: Optional[str] = None
    botName: Optional[str] = None
    description: Optional[str] = None
    botStatus: Optional[BotStatusType] = None
    latestBotVersion: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None
    botType: Optional[BotTypeType] = None


class BotVersionLocaleDetails(BaseValidatorModel):
    sourceBotVersion: str


class BotVersionReplicaSortBy(BaseValidatorModel):
    attribute: Literal['BotVersion']
    order: SortOrderType


class BotVersionReplicaSummary(BaseValidatorModel):
    botVersion: Optional[str] = None
    botVersionReplicationStatus: Optional[BotVersionReplicationStatusType] = None
    creationDateTime: Optional[datetime] = None
    failureReasons: Optional[List[str]] = None


class BotVersionSortBy(BaseValidatorModel):
    attribute: Literal['BotVersion']
    order: SortOrderType


class BotVersionSummary(BaseValidatorModel):
    botName: Optional[str] = None
    botVersion: Optional[str] = None
    description: Optional[str] = None
    botStatus: Optional[BotStatusType] = None
    creationDateTime: Optional[datetime] = None


# This class is the input for the 'build_bot_locale' function.
class BuildBotLocaleRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


class BuiltInIntentSortBy(BaseValidatorModel):
    attribute: Literal['IntentSignature']
    order: SortOrderType


class BuiltInIntentSummary(BaseValidatorModel):
    intentSignature: Optional[str] = None
    description: Optional[str] = None


class BuiltInSlotTypeSortBy(BaseValidatorModel):
    attribute: Literal['SlotTypeSignature']
    order: SortOrderType


class BuiltInSlotTypeSummary(BaseValidatorModel):
    slotTypeSignature: Optional[str] = None
    description: Optional[str] = None


class Button(BaseValidatorModel):
    text: str
    value: str


class CloudWatchLogGroupLogDestination(BaseValidatorModel):
    cloudWatchLogGroupArn: str
    logPrefix: str


class LambdaCodeHook(BaseValidatorModel):
    lambdaARN: str
    codeHookInterfaceVersion: str


class SubSlotTypeComposition(BaseValidatorModel):
    name: str
    slotTypeId: str


class Condition(BaseValidatorModel):
    expressionString: str


class ConversationLevelIntentClassificationResultItem(BaseValidatorModel):
    intentName: str
    matchResult: TestResultMatchStatusType


class ConversationLevelResultDetail(BaseValidatorModel):
    endToEndResult: TestResultMatchStatusType
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None


class ConversationLevelSlotResolutionResultItem(BaseValidatorModel):
    intentName: str
    slotName: str
    matchResult: TestResultMatchStatusType


class ConversationLevelTestResultsFilterBy(BaseValidatorModel):
    endToEndResult: Optional[TestResultMatchStatusType] = None


class ConversationLogsDataSourceFilterByOutput(BaseValidatorModel):
    startTime: datetime
    endTime: datetime
    inputMode: ConversationLogsInputModeFilterType

Timestamp = Union[datetime, str]


class SentimentAnalysisSettings(BaseValidatorModel):
    detectSentiment: bool


# This class is the input for the 'create_bot_replica' function.
class CreateBotReplicaRequest(BaseValidatorModel):
    botId: str
    replicaRegion: str


class DialogCodeHookSettings(BaseValidatorModel):
    enabled: bool


class InputContext(BaseValidatorModel):
    name: str


class KendraConfiguration(BaseValidatorModel):
    kendraIndex: str
    queryFilterStringEnabled: Optional[bool] = None
    queryFilterString: Optional[str] = None


class OutputContext(BaseValidatorModel):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int


class SampleUtterance(BaseValidatorModel):
    utterance: str


# This class is the input for the 'create_resource_policy' function.
class CreateResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str
    policy: str


class Principal(BaseValidatorModel):
    service: Optional[str] = None
    arn: Optional[str] = None


class MultipleValuesSetting(BaseValidatorModel):
    allowMultipleValues: Optional[bool] = None


class ObfuscationSetting(BaseValidatorModel):
    obfuscationSettingType: ObfuscationSettingTypeType


class CustomPayload(BaseValidatorModel):
    value: str


class CustomVocabularyExportSpecification(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


class CustomVocabularyImportSpecification(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


class QnAKendraConfiguration(BaseValidatorModel):
    kendraIndex: str
    queryFilterStringEnabled: Optional[bool] = None
    queryFilterString: Optional[str] = None
    exactResponse: Optional[bool] = None


class DateRangeFilterOutput(BaseValidatorModel):
    startDateTime: datetime
    endDateTime: datetime


# This class is the input for the 'delete_bot_alias' function.
class DeleteBotAliasRequest(BaseValidatorModel):
    botAliasId: str
    botId: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_bot_locale' function.
class DeleteBotLocaleRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'delete_bot_replica' function.
class DeleteBotReplicaRequest(BaseValidatorModel):
    botId: str
    replicaRegion: str


# This class is the input for the 'delete_bot' function.
class DeleteBotRequest(BaseValidatorModel):
    botId: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_bot_version' function.
class DeleteBotVersionRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_custom_vocabulary' function.
class DeleteCustomVocabularyRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'delete_export' function.
class DeleteExportRequest(BaseValidatorModel):
    exportId: str


# This class is the input for the 'delete_import' function.
class DeleteImportRequest(BaseValidatorModel):
    importId: str


# This class is the input for the 'delete_intent' function.
class DeleteIntentRequest(BaseValidatorModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str
    expectedRevisionId: Optional[str] = None


# This class is the input for the 'delete_resource_policy_statement' function.
class DeleteResourcePolicyStatementRequest(BaseValidatorModel):
    resourceArn: str
    statementId: str
    expectedRevisionId: Optional[str] = None


# This class is the input for the 'delete_slot' function.
class DeleteSlotRequest(BaseValidatorModel):
    slotId: str
    botId: str
    botVersion: str
    localeId: str
    intentId: str


# This class is the input for the 'delete_slot_type' function.
class DeleteSlotTypeRequest(BaseValidatorModel):
    slotTypeId: str
    botId: str
    botVersion: str
    localeId: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_test_set' function.
class DeleteTestSetRequest(BaseValidatorModel):
    testSetId: str


class DeleteUtterancesRequest(BaseValidatorModel):
    botId: str
    localeId: Optional[str] = None
    sessionId: Optional[str] = None


# This class is the input for the 'describe_bot_alias' function.
class DescribeBotAliasRequest(BaseValidatorModel):
    botAliasId: str
    botId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ParentBotNetwork(BaseValidatorModel):
    botId: str
    botVersion: str


# This class is the input for the 'describe_bot_locale' function.
class DescribeBotLocaleRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'describe_bot_recommendation' function.
class DescribeBotRecommendationRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str


class EncryptionSetting(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None
    botLocaleExportPassword: Optional[str] = None
    associatedTranscriptsPassword: Optional[str] = None


# This class is the input for the 'describe_bot_replica' function.
class DescribeBotReplicaRequest(BaseValidatorModel):
    botId: str
    replicaRegion: str


# This class is the input for the 'describe_bot' function.
class DescribeBotRequest(BaseValidatorModel):
    botId: str


# This class is the input for the 'describe_bot_resource_generation' function.
class DescribeBotResourceGenerationRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    generationId: str


# This class is the input for the 'describe_bot_version' function.
class DescribeBotVersionRequest(BaseValidatorModel):
    botId: str
    botVersion: str


# This class is the input for the 'describe_custom_vocabulary_metadata' function.
class DescribeCustomVocabularyMetadataRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'describe_export' function.
class DescribeExportRequest(BaseValidatorModel):
    exportId: str


# This class is the input for the 'describe_import' function.
class DescribeImportRequest(BaseValidatorModel):
    importId: str


# This class is the input for the 'describe_intent' function.
class DescribeIntentRequest(BaseValidatorModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str


class SlotPriority(BaseValidatorModel):
    priority: int
    slotId: str


# This class is the input for the 'describe_resource_policy' function.
class DescribeResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'describe_slot' function.
class DescribeSlotRequest(BaseValidatorModel):
    slotId: str
    botId: str
    botVersion: str
    localeId: str
    intentId: str


# This class is the input for the 'describe_slot_type' function.
class DescribeSlotTypeRequest(BaseValidatorModel):
    slotTypeId: str
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'describe_test_execution' function.
class DescribeTestExecutionRequest(BaseValidatorModel):
    testExecutionId: str


# This class is the input for the 'describe_test_set_discrepancy_report' function.
class DescribeTestSetDiscrepancyReportRequest(BaseValidatorModel):
    testSetDiscrepancyReportId: str


# This class is the input for the 'describe_test_set_generation' function.
class DescribeTestSetGenerationRequest(BaseValidatorModel):
    testSetGenerationId: str


class TestSetStorageLocation(BaseValidatorModel):
    s3BucketName: str
    s3Path: str
    kmsKeyArn: Optional[str] = None


# This class is the input for the 'describe_test_set' function.
class DescribeTestSetRequest(BaseValidatorModel):
    testSetId: str


class DialogAction(BaseValidatorModel):
    type: DialogActionTypeType
    slotToElicit: Optional[str] = None
    suppressNextMessage: Optional[bool] = None


class ElicitationCodeHookInvocationSetting(BaseValidatorModel):
    enableCodeHookInvocation: bool
    invocationLabel: Optional[str] = None


class ExactResponseFields(BaseValidatorModel):
    questionField: str
    answerField: str


class ExportFilter(BaseValidatorModel):
    name: Literal['ExportResourceType']
    values: List[str]
    operator: ExportFilterOperatorType


class TestSetExportSpecification(BaseValidatorModel):
    testSetId: str


class ExportSortBy(BaseValidatorModel):
    attribute: Literal['LastUpdatedDateTime']
    order: SortOrderType


# This class is the input for the 'generate_bot_element' function.
class GenerateBotElementRequest(BaseValidatorModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str


class GenerationSortBy(BaseValidatorModel):
    attribute: GenerationSortByAttributeType
    order: SortOrderType


class GenerationSummary(BaseValidatorModel):
    generationId: Optional[str] = None
    generationStatus: Optional[GenerationStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


# This class is the input for the 'get_test_execution_artifacts_url' function.
class GetTestExecutionArtifactsUrlRequest(BaseValidatorModel):
    testExecutionId: str


class GrammarSlotTypeSource(BaseValidatorModel):
    s3BucketName: str
    s3ObjectKey: str
    kmsKeyArn: Optional[str] = None


class ImportFilter(BaseValidatorModel):
    name: Literal['ImportResourceType']
    values: List[str]
    operator: ImportFilterOperatorType


class ImportSortBy(BaseValidatorModel):
    attribute: Literal['LastUpdatedDateTime']
    order: SortOrderType


class ImportSummary(BaseValidatorModel):
    importId: Optional[str] = None
    importedResourceId: Optional[str] = None
    importedResourceName: Optional[str] = None
    importStatus: Optional[ImportStatusType] = None
    mergeStrategy: Optional[MergeStrategyType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    importedResourceType: Optional[ImportResourceTypeType] = None


class IntentClassificationTestResultItemCounts(BaseValidatorModel):
    totalResultCount: int
    intentMatchResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None


class IntentFilter(BaseValidatorModel):
    name: Literal['IntentName']
    values: List[str]
    operator: IntentFilterOperatorType


class IntentSortBy(BaseValidatorModel):
    attribute: IntentSortAttributeType
    order: SortOrderType


class InvokedIntentSample(BaseValidatorModel):
    intentName: Optional[str] = None


# This class is the input for the 'list_bot_alias_replicas' function.
class ListBotAliasReplicasRequest(BaseValidatorModel):
    botId: str
    replicaRegion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_bot_aliases' function.
class ListBotAliasesRequest(BaseValidatorModel):
    botId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_bot_recommendations' function.
class ListBotRecommendationsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_bot_replicas' function.
class ListBotReplicasRequest(BaseValidatorModel):
    botId: str


# This class is the input for the 'list_custom_vocabulary_items' function.
class ListCustomVocabularyItemsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_recommended_intents' function.
class ListRecommendedIntentsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RecommendedIntentSummary(BaseValidatorModel):
    intentId: Optional[str] = None
    intentName: Optional[str] = None
    sampleUtterancesCount: Optional[int] = None


class SessionDataSortBy(BaseValidatorModel):
    name: AnalyticsSessionSortByNameType
    order: AnalyticsSortOrderType


class SlotTypeFilter(BaseValidatorModel):
    name: SlotTypeFilterNameType
    values: List[str]
    operator: SlotTypeFilterOperatorType


class SlotTypeSortBy(BaseValidatorModel):
    attribute: SlotTypeSortAttributeType
    order: SortOrderType


class SlotTypeSummary(BaseValidatorModel):
    slotTypeId: Optional[str] = None
    slotTypeName: Optional[str] = None
    description: Optional[str] = None
    parentSlotTypeSignature: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None
    slotTypeCategory: Optional[SlotTypeCategoryType] = None


class SlotFilter(BaseValidatorModel):
    name: Literal['SlotName']
    values: List[str]
    operator: SlotFilterOperatorType


class SlotSortBy(BaseValidatorModel):
    attribute: SlotSortAttributeType
    order: SortOrderType


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class TestExecutionSortBy(BaseValidatorModel):
    attribute: TestExecutionSortAttributeType
    order: SortOrderType


# This class is the input for the 'list_test_set_records' function.
class ListTestSetRecordsRequest(BaseValidatorModel):
    testSetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TestSetSortBy(BaseValidatorModel):
    attribute: TestSetSortAttributeType
    order: SortOrderType


class UtteranceDataSortBy(BaseValidatorModel):
    name: Literal['UtteranceTimestamp']
    order: AnalyticsSortOrderType


class PlainTextMessage(BaseValidatorModel):
    value: str


class SSMLMessage(BaseValidatorModel):
    value: str


class OverallTestResultItem(BaseValidatorModel):
    multiTurnConversation: bool
    totalResultCount: int
    endToEndResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None


class PathFormatOutput(BaseValidatorModel):
    objectPrefixes: Optional[List[str]] = None


class PathFormat(BaseValidatorModel):
    objectPrefixes: Optional[List[str]] = None


class TextInputSpecification(BaseValidatorModel):
    startTimeoutMs: int


class RelativeAggregationDuration(BaseValidatorModel):
    timeDimension: TimeDimensionType
    timeValue: int


class RuntimeHintValue(BaseValidatorModel):
    phrase: str


class SampleValue(BaseValidatorModel):
    value: str


class SlotDefaultValue(BaseValidatorModel):
    defaultValue: str


class SlotResolutionSetting(BaseValidatorModel):
    slotResolutionStrategy: SlotResolutionStrategyType


class SlotResolutionTestResultItemCounts(BaseValidatorModel):
    totalResultCount: int
    slotMatchResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None


class SlotValue(BaseValidatorModel):
    interpretedValue: Optional[str] = None


class SlotValueRegexFilter(BaseValidatorModel):
    pattern: str


# This class is the input for the 'start_bot_resource_generation' function.
class StartBotResourceGenerationRequest(BaseValidatorModel):
    generationInputPrompt: str
    botId: str
    botVersion: str
    localeId: str


# This class is the input for the 'stop_bot_recommendation' function.
class StopBotRecommendationRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: Dict[str, str]


class TestSetIntentDiscrepancyItem(BaseValidatorModel):
    intentName: str
    errorMessage: str


class TestSetSlotDiscrepancyItem(BaseValidatorModel):
    intentName: str
    slotName: str
    errorMessage: str


class TestSetDiscrepancyReportBotAliasTarget(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str


class TestSetImportInputLocation(BaseValidatorModel):
    s3BucketName: str
    s3Path: str


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


# This class is the input for the 'update_export' function.
class UpdateExportRequest(BaseValidatorModel):
    exportId: str
    filePassword: Optional[str] = None


# This class is the input for the 'update_resource_policy' function.
class UpdateResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str
    policy: str
    expectedRevisionId: Optional[str] = None


# This class is the input for the 'update_test_set' function.
class UpdateTestSetRequest(BaseValidatorModel):
    testSetId: str
    testSetName: str
    description: Optional[str] = None


class UserTurnSlotOutput(BaseValidatorModel):
    value: Optional[str] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None


class UtteranceAudioInputSpecification(BaseValidatorModel):
    audioFileS3Location: str


class AgentTurnResult(BaseValidatorModel):
    expectedAgentPrompt: str
    actualAgentPrompt: Optional[str] = None
    errorDetails: Optional[ExecutionErrorDetails] = None
    actualElicitedSlot: Optional[str] = None
    actualIntent: Optional[str] = None


class AnalyticsIntentResult(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKey]] = None
    groupByKeys: Optional[List[AnalyticsIntentGroupByKey]] = None
    metricsResults: Optional[List[AnalyticsIntentMetricResult]] = None


class AnalyticsIntentStageResult(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKey]] = None
    groupByKeys: Optional[List[AnalyticsIntentStageGroupByKey]] = None
    metricsResults: Optional[List[AnalyticsIntentStageMetricResult]] = None


class AnalyticsSessionResult(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKey]] = None
    groupByKeys: Optional[List[AnalyticsSessionGroupByKey]] = None
    metricsResults: Optional[List[AnalyticsSessionMetricResult]] = None


class AnalyticsUtteranceResult(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKey]] = None
    groupByKeys: Optional[List[AnalyticsUtteranceGroupByKey]] = None
    metricsResults: Optional[List[AnalyticsUtteranceMetricResult]] = None
    attributeResults: Optional[List[AnalyticsUtteranceAttributeResult]] = None


# This class is the input for the 'search_associated_transcripts' function.
class SearchAssociatedTranscriptsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    filters: List[AssociatedTranscriptFilter]
    searchOrder: Optional[SearchOrderType] = None
    maxResults: Optional[int] = None
    nextIndex: Optional[int] = None


class AudioAndDTMFInputSpecification(BaseValidatorModel):
    startTimeoutMs: int
    audioSpecification: Optional[AudioSpecification] = None
    dtmfSpecification: Optional[DTMFSpecification] = None


class AudioLogDestination(BaseValidatorModel):
    s3Bucket: S3BucketLogDestination


# This class is the input for the 'batch_create_custom_vocabulary_item' function.
class BatchCreateCustomVocabularyItemRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: List[NewCustomVocabularyItem]


# This class is the input for the 'batch_update_custom_vocabulary_item' function.
class BatchUpdateCustomVocabularyItemRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: List[CustomVocabularyItem]


# This class is the output for the 'batch_create_custom_vocabulary_item' function.
class BatchCreateCustomVocabularyItemResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItem]
    resources: List[CustomVocabularyItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_custom_vocabulary_item' function.
class BatchDeleteCustomVocabularyItemResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItem]
    resources: List[CustomVocabularyItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_custom_vocabulary_item' function.
class BatchUpdateCustomVocabularyItemResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItem]
    resources: List[CustomVocabularyItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'build_bot_locale' function.
class BuildBotLocaleResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatusType
    lastBuildSubmittedDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_bot_replica' function.
class CreateBotReplicaResponse(BaseValidatorModel):
    botId: str
    replicaRegion: str
    sourceRegion: str
    creationDateTime: datetime
    botReplicaStatus: BotReplicaStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resource_policy' function.
class CreateResourcePolicyResponse(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resource_policy_statement' function.
class CreateResourcePolicyStatementResponse(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


class CreateUploadUrlResponse(BaseValidatorModel):
    importId: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bot_alias' function.
class DeleteBotAliasResponse(BaseValidatorModel):
    botAliasId: str
    botId: str
    botAliasStatus: BotAliasStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bot_locale' function.
class DeleteBotLocaleResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bot_replica' function.
class DeleteBotReplicaResponse(BaseValidatorModel):
    botId: str
    replicaRegion: str
    botReplicaStatus: BotReplicaStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bot' function.
class DeleteBotResponse(BaseValidatorModel):
    botId: str
    botStatus: BotStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bot_version' function.
class DeleteBotVersionResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    botStatus: BotStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_custom_vocabulary' function.
class DeleteCustomVocabularyResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyStatus: CustomVocabularyStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_export' function.
class DeleteExportResponse(BaseValidatorModel):
    exportId: str
    exportStatus: ExportStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_import' function.
class DeleteImportResponse(BaseValidatorModel):
    importId: str
    importStatus: ImportStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_policy' function.
class DeleteResourcePolicyResponse(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_policy_statement' function.
class DeleteResourcePolicyStatementResponse(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bot_replica' function.
class DescribeBotReplicaResponse(BaseValidatorModel):
    botId: str
    replicaRegion: str
    sourceRegion: str
    creationDateTime: datetime
    botReplicaStatus: BotReplicaStatusType
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bot_resource_generation' function.
class DescribeBotResourceGenerationResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_vocabulary_metadata' function.
class DescribeCustomVocabularyMetadataResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyStatus: CustomVocabularyStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource_policy' function.
class DescribeResourcePolicyResponse(BaseValidatorModel):
    resourceArn: str
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_test_set' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_test_execution_artifacts_url' function.
class GetTestExecutionArtifactsUrlResponse(BaseValidatorModel):
    testExecutionId: str
    downloadArtifactsUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_custom_vocabulary_items' function.
class ListCustomVocabularyItemsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItems: List[CustomVocabularyItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_intent_paths' function.
class ListIntentPathsResponse(BaseValidatorModel):
    nodeSummaries: List[AnalyticsIntentNodeSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_associated_transcripts' function.
class SearchAssociatedTranscriptsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    nextIndex: int
    associatedTranscripts: List[AssociatedTranscript]
    totalResults: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_bot_resource_generation' function.
class StartBotResourceGenerationResponse(BaseValidatorModel):
    generationInputPrompt: str
    generationId: str
    botId: str
    botVersion: str
    localeId: str
    generationStatus: GenerationStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_bot_recommendation' function.
class StopBotRecommendationResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_resource_policy' function.
class UpdateResourcePolicyResponse(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_delete_custom_vocabulary_item' function.
class BatchDeleteCustomVocabularyItemRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: List[CustomVocabularyEntryId]


class BedrockModelSpecification(BaseValidatorModel):
    modelArn: str
    guardrail: Optional[BedrockGuardrailConfiguration] = None
    traceStatus: Optional[BedrockTraceStatusType] = None
    customPrompt: Optional[str] = None


class BedrockKnowledgeStoreConfiguration(BaseValidatorModel):
    bedrockKnowledgeBaseArn: str
    exactResponse: Optional[bool] = None
    exactResponseFields: Optional[BedrockKnowledgeStoreExactResponseFields] = None


# This class is the output for the 'list_bot_alias_replicas' function.
class ListBotAliasReplicasResponse(BaseValidatorModel):
    botId: str
    sourceRegion: str
    replicaRegion: str
    botAliasReplicaSummaries: List[BotAliasReplicaSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_bot_aliases' function.
class ListBotAliasesResponse(BaseValidatorModel):
    botAliasSummaries: List[BotAliasSummary]
    botId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TestExecutionTarget(BaseValidatorModel):
    botAliasTarget: Optional[BotAliasTestExecutionTarget] = None


class BotImportSpecificationOutput(BaseValidatorModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: Optional[int] = None
    botTags: Optional[Dict[str, str]] = None
    testBotAliasTags: Optional[Dict[str, str]] = None


class BotImportSpecification(BaseValidatorModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: Optional[int] = None
    botTags: Optional[Dict[str, str]] = None
    testBotAliasTags: Optional[Dict[str, str]] = None


class BotLocaleImportSpecification(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: Optional[float] = None
    voiceSettings: Optional[VoiceSettings] = None


# This class is the input for the 'list_bot_locales' function.
class ListBotLocalesRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    sortBy: Optional[BotLocaleSortBy] = None
    filters: Optional[List[BotLocaleFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_bot_locales' function.
class ListBotLocalesResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    botLocaleSummaries: List[BotLocaleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_bot' function.
class CreateBotRequest(BaseValidatorModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: int
    description: Optional[str] = None
    botTags: Optional[Dict[str, str]] = None
    testBotAliasTags: Optional[Dict[str, str]] = None
    botType: Optional[BotTypeType] = None
    botMembers: Optional[List[BotMember]] = None


# This class is the output for the 'create_bot' function.
class CreateBotResponse(BaseValidatorModel):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    creationDateTime: datetime
    botTags: Dict[str, str]
    testBotAliasTags: Dict[str, str]
    botType: BotTypeType
    botMembers: List[BotMember]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bot' function.
class DescribeBotResponse(BaseValidatorModel):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    botType: BotTypeType
    botMembers: List[BotMember]
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_bot' function.
class UpdateBotRequest(BaseValidatorModel):
    botId: str
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: int
    description: Optional[str] = None
    botType: Optional[BotTypeType] = None
    botMembers: Optional[List[BotMember]] = None


# This class is the output for the 'update_bot' function.
class UpdateBotResponse(BaseValidatorModel):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    botType: BotTypeType
    botMembers: List[BotMember]
    ResponseMetadata: ResponseMetadata


class BotRecommendationResultStatistics(BaseValidatorModel):
    intents: Optional[IntentStatistics] = None
    slotTypes: Optional[SlotTypeStatistics] = None


# This class is the output for the 'list_bot_recommendations' function.
class ListBotRecommendationsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationSummaries: List[BotRecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_bot_replicas' function.
class ListBotReplicasResponse(BaseValidatorModel):
    botId: str
    sourceRegion: str
    botReplicaSummaries: List[BotReplicaSummary]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'list_bots' function.
class ListBotsRequest(BaseValidatorModel):
    sortBy: Optional[BotSortBy] = None
    filters: Optional[List[BotFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_bots' function.
class ListBotsResponse(BaseValidatorModel):
    botSummaries: List[BotSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_bot_version' function.
class CreateBotVersionRequest(BaseValidatorModel):
    botId: str
    botVersionLocaleSpecification: Dict[str, BotVersionLocaleDetails]
    description: Optional[str] = None


# This class is the output for the 'create_bot_version' function.
class CreateBotVersionResponse(BaseValidatorModel):
    botId: str
    description: str
    botVersion: str
    botVersionLocaleSpecification: Dict[str, BotVersionLocaleDetails]
    botStatus: BotStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'list_bot_version_replicas' function.
class ListBotVersionReplicasRequest(BaseValidatorModel):
    botId: str
    replicaRegion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[BotVersionReplicaSortBy] = None


# This class is the output for the 'list_bot_version_replicas' function.
class ListBotVersionReplicasResponse(BaseValidatorModel):
    botId: str
    sourceRegion: str
    replicaRegion: str
    botVersionReplicaSummaries: List[BotVersionReplicaSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_bot_versions' function.
class ListBotVersionsRequest(BaseValidatorModel):
    botId: str
    sortBy: Optional[BotVersionSortBy] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_bot_versions' function.
class ListBotVersionsResponse(BaseValidatorModel):
    botId: str
    botVersionSummaries: List[BotVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_built_in_intents' function.
class ListBuiltInIntentsRequest(BaseValidatorModel):
    localeId: str
    sortBy: Optional[BuiltInIntentSortBy] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_built_in_intents' function.
class ListBuiltInIntentsResponse(BaseValidatorModel):
    builtInIntentSummaries: List[BuiltInIntentSummary]
    localeId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_built_in_slot_types' function.
class ListBuiltInSlotTypesRequest(BaseValidatorModel):
    localeId: str
    sortBy: Optional[BuiltInSlotTypeSortBy] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_built_in_slot_types' function.
class ListBuiltInSlotTypesResponse(BaseValidatorModel):
    builtInSlotTypeSummaries: List[BuiltInSlotTypeSummary]
    localeId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImageResponseCardOutput(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[Button]] = None


class ImageResponseCard(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[Button]] = None


class TextLogDestination(BaseValidatorModel):
    cloudWatch: CloudWatchLogGroupLogDestination


class CodeHookSpecification(BaseValidatorModel):
    lambdaCodeHook: LambdaCodeHook


class CompositeSlotTypeSettingOutput(BaseValidatorModel):
    subSlots: Optional[List[SubSlotTypeComposition]] = None


class CompositeSlotTypeSetting(BaseValidatorModel):
    subSlots: Optional[List[SubSlotTypeComposition]] = None


class ConversationLevelTestResultItem(BaseValidatorModel):
    conversationId: str
    endToEndResult: TestResultMatchStatusType
    intentClassificationResults: List[ConversationLevelIntentClassificationResultItem]
    slotResolutionResults: List[ConversationLevelSlotResolutionResultItem]
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None


class TestExecutionResultFilterBy(BaseValidatorModel):
    resultTypeFilter: TestResultTypeFilterType
    conversationLevelTestResultsFilterBy: Optional[ConversationLevelTestResultsFilterBy] = None


class ConversationLogsDataSourceOutput(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    filter: ConversationLogsDataSourceFilterByOutput


class ConversationLogsDataSourceFilterBy(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    inputMode: ConversationLogsInputModeFilterType


class DateRangeFilter(BaseValidatorModel):
    startDateTime: Timestamp
    endDateTime: Timestamp


# This class is the input for the 'list_intent_metrics' function.
class ListIntentMetricsRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    metrics: List[AnalyticsIntentMetric]
    binBy: Optional[List[AnalyticsBinBySpecification]] = None
    groupBy: Optional[List[AnalyticsIntentGroupBySpecification]] = None
    filters: Optional[List[AnalyticsIntentFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_intent_paths' function.
class ListIntentPathsRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    intentPath: str
    filters: Optional[List[AnalyticsPathFilter]] = None


# This class is the input for the 'list_intent_stage_metrics' function.
class ListIntentStageMetricsRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    metrics: List[AnalyticsIntentStageMetric]
    binBy: Optional[List[AnalyticsBinBySpecification]] = None
    groupBy: Optional[List[AnalyticsIntentStageGroupBySpecification]] = None
    filters: Optional[List[AnalyticsIntentStageFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_session_metrics' function.
class ListSessionMetricsRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    metrics: List[AnalyticsSessionMetric]
    binBy: Optional[List[AnalyticsBinBySpecification]] = None
    groupBy: Optional[List[AnalyticsSessionGroupBySpecification]] = None
    filters: Optional[List[AnalyticsSessionFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_utterance_metrics' function.
class ListUtteranceMetricsRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    metrics: List[AnalyticsUtteranceMetric]
    binBy: Optional[List[AnalyticsBinBySpecification]] = None
    groupBy: Optional[List[AnalyticsUtteranceGroupBySpecification]] = None
    attributes: Optional[List[AnalyticsUtteranceAttribute]] = None
    filters: Optional[List[AnalyticsUtteranceFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class IntentSummary(BaseValidatorModel):
    intentId: Optional[str] = None
    intentName: Optional[str] = None
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    inputContexts: Optional[List[InputContext]] = None
    outputContexts: Optional[List[OutputContext]] = None
    lastUpdatedDateTime: Optional[datetime] = None


# This class is the output for the 'generate_bot_element' function.
class GenerateBotElementResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    sampleUtterances: List[SampleUtterance]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_resource_policy_statement' function.
class CreateResourcePolicyStatementRequest(BaseValidatorModel):
    resourceArn: str
    statementId: str
    effect: EffectType
    principal: List[Principal]
    action: List[str]
    condition: Optional[Dict[str, Dict[str, str]]] = None
    expectedRevisionId: Optional[str] = None


class LexTranscriptFilterOutput(BaseValidatorModel):
    dateRangeFilter: Optional[DateRangeFilterOutput] = None


class DescribeBotAliasRequestWait(BaseValidatorModel):
    botAliasId: str
    botId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeBotLocaleRequestWaitExtraExtra(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeBotLocaleRequestWaitExtra(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeBotLocaleRequestWait(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeBotRequestWait(BaseValidatorModel):
    botId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeBotVersionRequestWait(BaseValidatorModel):
    botId: str
    botVersion: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeExportRequestWait(BaseValidatorModel):
    exportId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImportRequestWait(BaseValidatorModel):
    importId: str
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_bot_version' function.
class DescribeBotVersionResponse(BaseValidatorModel):
    botId: str
    botName: str
    botVersion: str
    description: str
    roleArn: str
    dataPrivacy: DataPrivacy
    idleSessionTTLInSeconds: int
    botStatus: BotStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    parentBotNetworks: List[ParentBotNetwork]
    botType: BotTypeType
    botMembers: List[BotMember]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_bot_recommendation' function.
class UpdateBotRecommendationRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    encryptionSetting: EncryptionSetting


# This class is the output for the 'describe_test_set' function.
class DescribeTestSetResponse(BaseValidatorModel):
    testSetId: str
    testSetName: str
    description: str
    modality: TestSetModalityType
    status: TestSetStatusType
    roleArn: str
    numTurns: int
    storageLocation: TestSetStorageLocation
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


class TestSetSummary(BaseValidatorModel):
    testSetId: Optional[str] = None
    testSetName: Optional[str] = None
    description: Optional[str] = None
    modality: Optional[TestSetModalityType] = None
    status: Optional[TestSetStatusType] = None
    roleArn: Optional[str] = None
    numTurns: Optional[int] = None
    storageLocation: Optional[TestSetStorageLocation] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


# This class is the output for the 'update_test_set' function.
class UpdateTestSetResponse(BaseValidatorModel):
    testSetId: str
    testSetName: str
    description: str
    modality: TestSetModalityType
    status: TestSetStatusType
    roleArn: str
    numTurns: int
    storageLocation: TestSetStorageLocation
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


class OpensearchConfigurationOutput(BaseValidatorModel):
    domainEndpoint: str
    indexName: str
    exactResponse: Optional[bool] = None
    exactResponseFields: Optional[ExactResponseFields] = None
    includeFields: Optional[List[str]] = None


class OpensearchConfiguration(BaseValidatorModel):
    domainEndpoint: str
    indexName: str
    exactResponse: Optional[bool] = None
    exactResponseFields: Optional[ExactResponseFields] = None
    includeFields: Optional[List[str]] = None


class ExportResourceSpecification(BaseValidatorModel):
    botExportSpecification: Optional[BotExportSpecification] = None
    botLocaleExportSpecification: Optional[BotLocaleExportSpecification] = None
    customVocabularyExportSpecification: Optional[CustomVocabularyExportSpecification] = None
    testSetExportSpecification: Optional[TestSetExportSpecification] = None


# This class is the input for the 'list_exports' function.
class ListExportsRequest(BaseValidatorModel):
    botId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[ExportSortBy] = None
    filters: Optional[List[ExportFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    localeId: Optional[str] = None


# This class is the input for the 'list_bot_resource_generations' function.
class ListBotResourceGenerationsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[GenerationSortBy] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_bot_resource_generations' function.
class ListBotResourceGenerationsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    generationSummaries: List[GenerationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GrammarSlotTypeSetting(BaseValidatorModel):
    source: Optional[GrammarSlotTypeSource] = None


# This class is the input for the 'list_imports' function.
class ListImportsRequest(BaseValidatorModel):
    botId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[ImportSortBy] = None
    filters: Optional[List[ImportFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    localeId: Optional[str] = None


# This class is the output for the 'list_imports' function.
class ListImportsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    importSummaries: List[ImportSummary]
    localeId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IntentClassificationTestResultItem(BaseValidatorModel):
    intentName: str
    multiTurnConversation: bool
    resultCounts: IntentClassificationTestResultItemCounts


# This class is the input for the 'list_intents' function.
class ListIntentsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[IntentSortBy] = None
    filters: Optional[List[IntentFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SessionSpecification(BaseValidatorModel):
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
    invokedIntentSamples: Optional[List[InvokedIntentSample]] = None
    originatingRequestId: Optional[str] = None


# This class is the output for the 'list_recommended_intents' function.
class ListRecommendedIntentsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    summaryList: List[RecommendedIntentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_session_analytics_data' function.
class ListSessionAnalyticsDataRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    sortBy: Optional[SessionDataSortBy] = None
    filters: Optional[List[AnalyticsSessionFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_slot_types' function.
class ListSlotTypesRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[SlotTypeSortBy] = None
    filters: Optional[List[SlotTypeFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_slot_types' function.
class ListSlotTypesResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    slotTypeSummaries: List[SlotTypeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_slots' function.
class ListSlotsRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    sortBy: Optional[SlotSortBy] = None
    filters: Optional[List[SlotFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_test_executions' function.
class ListTestExecutionsRequest(BaseValidatorModel):
    sortBy: Optional[TestExecutionSortBy] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_test_sets' function.
class ListTestSetsRequest(BaseValidatorModel):
    sortBy: Optional[TestSetSortBy] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_utterance_analytics_data' function.
class ListUtteranceAnalyticsDataRequest(BaseValidatorModel):
    botId: str
    startDateTime: Timestamp
    endDateTime: Timestamp
    sortBy: Optional[UtteranceDataSortBy] = None
    filters: Optional[List[AnalyticsUtteranceFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class OverallTestResults(BaseValidatorModel):
    items: List[OverallTestResultItem]


class UtteranceAggregationDuration(BaseValidatorModel):
    relativeAggregationDuration: RelativeAggregationDuration


class RuntimeHintDetails(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValue]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None


class SlotTypeValueOutput(BaseValidatorModel):
    sampleValue: Optional[SampleValue] = None
    synonyms: Optional[List[SampleValue]] = None


class SlotTypeValue(BaseValidatorModel):
    sampleValue: Optional[SampleValue] = None
    synonyms: Optional[List[SampleValue]] = None


class SlotDefaultValueSpecificationOutput(BaseValidatorModel):
    defaultValueList: List[SlotDefaultValue]


class SlotDefaultValueSpecification(BaseValidatorModel):
    defaultValueList: List[SlotDefaultValue]


class SlotResolutionTestResultItem(BaseValidatorModel):
    slotName: str
    resultCounts: SlotResolutionTestResultItemCounts


class SlotValueOverrideOutput(BaseValidatorModel):
    shape: Optional[SlotShapeType] = None
    value: Optional[SlotValue] = None
    values: Optional[List[Dict[str, Any]]] = None


class SlotValueOverride(BaseValidatorModel):
    shape: Optional[SlotShapeType] = None
    value: Optional[SlotValue] = None
    values: Optional[List[Dict[str, Any]]] = None


class SlotValueSelectionSetting(BaseValidatorModel):
    resolutionStrategy: SlotValueResolutionStrategyType
    regexFilter: Optional[SlotValueRegexFilter] = None
    advancedRecognitionSetting: Optional[AdvancedRecognitionSetting] = None


class TestSetDiscrepancyErrors(BaseValidatorModel):
    intentDiscrepancies: List[TestSetIntentDiscrepancyItem]
    slotDiscrepancies: List[TestSetSlotDiscrepancyItem]


class TestSetDiscrepancyReportResourceTarget(BaseValidatorModel):
    botAliasTarget: Optional[TestSetDiscrepancyReportBotAliasTarget] = None


class TestSetImportResourceSpecificationOutput(BaseValidatorModel):
    testSetName: str
    roleArn: str
    storageLocation: TestSetStorageLocation
    importInputLocation: TestSetImportInputLocation
    modality: TestSetModalityType
    description: Optional[str] = None
    testSetTags: Optional[Dict[str, str]] = None


class TestSetImportResourceSpecification(BaseValidatorModel):
    testSetName: str
    roleArn: str
    storageLocation: TestSetStorageLocation
    importInputLocation: TestSetImportInputLocation
    modality: TestSetModalityType
    description: Optional[str] = None
    testSetTags: Optional[Dict[str, str]] = None


class UserTurnIntentOutput(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, UserTurnSlotOutput]] = None


class UtteranceInputSpecification(BaseValidatorModel):
    textInput: Optional[str] = None
    audioInput: Optional[UtteranceAudioInputSpecification] = None


# This class is the output for the 'list_intent_metrics' function.
class ListIntentMetricsResponse(BaseValidatorModel):
    botId: str
    results: List[AnalyticsIntentResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_intent_stage_metrics' function.
class ListIntentStageMetricsResponse(BaseValidatorModel):
    botId: str
    results: List[AnalyticsIntentStageResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_session_metrics' function.
class ListSessionMetricsResponse(BaseValidatorModel):
    botId: str
    results: List[AnalyticsSessionResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_utterance_metrics' function.
class ListUtteranceMetricsResponse(BaseValidatorModel):
    botId: str
    results: List[AnalyticsUtteranceResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PromptAttemptSpecification(BaseValidatorModel):
    allowedInputTypes: AllowedInputTypes
    allowInterrupt: Optional[bool] = None
    audioAndDTMFInputSpecification: Optional[AudioAndDTMFInputSpecification] = None
    textInputSpecification: Optional[TextInputSpecification] = None


class AudioLogSetting(BaseValidatorModel):
    enabled: bool
    destination: AudioLogDestination
    selectiveLoggingEnabled: Optional[bool] = None


class DescriptiveBotBuilderSpecification(BaseValidatorModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecification] = None


class SampleUtteranceGenerationSpecification(BaseValidatorModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecification] = None


class SlotResolutionImprovementSpecification(BaseValidatorModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecification] = None


# This class is the output for the 'describe_test_execution' function.
class DescribeTestExecutionResponse(BaseValidatorModel):
    testExecutionId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    testExecutionStatus: TestExecutionStatusType
    testSetId: str
    testSetName: str
    target: TestExecutionTarget
    apiMode: TestExecutionApiModeType
    testExecutionModality: TestExecutionModalityType
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_test_execution' function.
class StartTestExecutionRequest(BaseValidatorModel):
    testSetId: str
    target: TestExecutionTarget
    apiMode: TestExecutionApiModeType
    testExecutionModality: Optional[TestExecutionModalityType] = None


# This class is the output for the 'start_test_execution' function.
class StartTestExecutionResponse(BaseValidatorModel):
    testExecutionId: str
    creationDateTime: datetime
    testSetId: str
    target: TestExecutionTarget
    apiMode: TestExecutionApiModeType
    testExecutionModality: TestExecutionModalityType
    ResponseMetadata: ResponseMetadata


class TestExecutionSummary(BaseValidatorModel):
    testExecutionId: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    testExecutionStatus: Optional[TestExecutionStatusType] = None
    testSetId: Optional[str] = None
    testSetName: Optional[str] = None
    target: Optional[TestExecutionTarget] = None
    apiMode: Optional[TestExecutionApiModeType] = None
    testExecutionModality: Optional[TestExecutionModalityType] = None


class BotRecommendationResults(BaseValidatorModel):
    botLocaleExportUrl: Optional[str] = None
    associatedTranscriptsUrl: Optional[str] = None
    statistics: Optional[BotRecommendationResultStatistics] = None


class MessageOutput(BaseValidatorModel):
    plainTextMessage: Optional[PlainTextMessage] = None
    customPayload: Optional[CustomPayload] = None
    ssmlMessage: Optional[SSMLMessage] = None
    imageResponseCard: Optional[ImageResponseCardOutput] = None


class UtteranceBotResponse(BaseValidatorModel):
    content: Optional[str] = None
    contentType: Optional[UtteranceContentTypeType] = None
    imageResponseCard: Optional[ImageResponseCardOutput] = None


class Message(BaseValidatorModel):
    plainTextMessage: Optional[PlainTextMessage] = None
    customPayload: Optional[CustomPayload] = None
    ssmlMessage: Optional[SSMLMessage] = None
    imageResponseCard: Optional[ImageResponseCard] = None


class TextLogSetting(BaseValidatorModel):
    enabled: bool
    destination: TextLogDestination
    selectiveLoggingEnabled: Optional[bool] = None


class BotAliasLocaleSettings(BaseValidatorModel):
    enabled: bool
    codeHookSpecification: Optional[CodeHookSpecification] = None

CompositeSlotTypeSettingUnion = Union[CompositeSlotTypeSetting, CompositeSlotTypeSettingOutput]


class ConversationLevelTestResults(BaseValidatorModel):
    items: List[ConversationLevelTestResultItem]


# This class is the input for the 'list_test_execution_result_items' function.
class ListTestExecutionResultItemsRequest(BaseValidatorModel):
    testExecutionId: str
    resultFilterBy: TestExecutionResultFilterBy
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TestSetGenerationDataSourceOutput(BaseValidatorModel):
    conversationLogsDataSource: Optional[ConversationLogsDataSourceOutput] = None


class ConversationLogsDataSource(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    filter: ConversationLogsDataSourceFilterBy


class LexTranscriptFilter(BaseValidatorModel):
    dateRangeFilter: Optional[DateRangeFilter] = None


# This class is the output for the 'list_intents' function.
class ListIntentsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentSummaries: List[IntentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TranscriptFilterOutput(BaseValidatorModel):
    lexTranscriptFilter: Optional[LexTranscriptFilterOutput] = None


# This class is the output for the 'list_test_sets' function.
class ListTestSetsResponse(BaseValidatorModel):
    testSets: List[TestSetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataSourceConfigurationOutput(BaseValidatorModel):
    opensearchConfiguration: Optional[OpensearchConfigurationOutput] = None
    kendraConfiguration: Optional[QnAKendraConfiguration] = None
    bedrockKnowledgeStoreConfiguration: Optional[BedrockKnowledgeStoreConfiguration] = None


class DataSourceConfiguration(BaseValidatorModel):
    opensearchConfiguration: Optional[OpensearchConfiguration] = None
    kendraConfiguration: Optional[QnAKendraConfiguration] = None
    bedrockKnowledgeStoreConfiguration: Optional[BedrockKnowledgeStoreConfiguration] = None


# This class is the input for the 'create_export' function.
class CreateExportRequest(BaseValidatorModel):
    resourceSpecification: ExportResourceSpecification
    fileFormat: ImportExportFileFormatType
    filePassword: Optional[str] = None


# This class is the output for the 'create_export' function.
class CreateExportResponse(BaseValidatorModel):
    exportId: str
    resourceSpecification: ExportResourceSpecification
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_export' function.
class DescribeExportResponse(BaseValidatorModel):
    exportId: str
    resourceSpecification: ExportResourceSpecification
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    failureReasons: List[str]
    downloadUrl: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


class ExportSummary(BaseValidatorModel):
    exportId: Optional[str] = None
    resourceSpecification: Optional[ExportResourceSpecification] = None
    fileFormat: Optional[ImportExportFileFormatType] = None
    exportStatus: Optional[ExportStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


# This class is the output for the 'update_export' function.
class UpdateExportResponse(BaseValidatorModel):
    exportId: str
    resourceSpecification: ExportResourceSpecification
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


class ExternalSourceSetting(BaseValidatorModel):
    grammarSlotTypeSetting: Optional[GrammarSlotTypeSetting] = None


class IntentClassificationTestResults(BaseValidatorModel):
    items: List[IntentClassificationTestResultItem]


# This class is the output for the 'list_session_analytics_data' function.
class ListSessionAnalyticsDataResponse(BaseValidatorModel):
    botId: str
    sessions: List[SessionSpecification]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_aggregated_utterances' function.
class ListAggregatedUtterancesRequest(BaseValidatorModel):
    botId: str
    localeId: str
    aggregationDuration: UtteranceAggregationDuration
    botAliasId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[AggregatedUtterancesSortBy] = None
    filters: Optional[List[AggregatedUtterancesFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_aggregated_utterances' function.
class ListAggregatedUtterancesResponse(BaseValidatorModel):
    botId: str
    botAliasId: str
    botVersion: str
    localeId: str
    aggregationDuration: UtteranceAggregationDuration
    aggregationWindowStartTime: datetime
    aggregationWindowEndTime: datetime
    aggregationLastRefreshedDateTime: datetime
    aggregatedUtterancesSummaries: List[AggregatedUtterancesSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RuntimeHints(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, RuntimeHintDetails]]] = None

SlotTypeValueUnion = Union[SlotTypeValue, SlotTypeValueOutput]


class IntentLevelSlotResolutionTestResultItem(BaseValidatorModel):
    intentName: str
    multiTurnConversation: bool
    slotResolutionResults: List[SlotResolutionTestResultItem]


class IntentOverrideOutput(BaseValidatorModel):
    name: Optional[str] = None
    slots: Optional[Dict[str, SlotValueOverrideOutput]] = None


class IntentOverride(BaseValidatorModel):
    name: Optional[str] = None
    slots: Optional[Dict[str, SlotValueOverride]] = None


# This class is the input for the 'create_test_set_discrepancy_report' function.
class CreateTestSetDiscrepancyReportRequest(BaseValidatorModel):
    testSetId: str
    target: TestSetDiscrepancyReportResourceTarget


# This class is the output for the 'create_test_set_discrepancy_report' function.
class CreateTestSetDiscrepancyReportResponse(BaseValidatorModel):
    testSetDiscrepancyReportId: str
    creationDateTime: datetime
    testSetId: str
    target: TestSetDiscrepancyReportResourceTarget
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_test_set_discrepancy_report' function.
class DescribeTestSetDiscrepancyReportResponse(BaseValidatorModel):
    testSetDiscrepancyReportId: str
    testSetId: str
    creationDateTime: datetime
    target: TestSetDiscrepancyReportResourceTarget
    testSetDiscrepancyReportStatus: TestSetDiscrepancyReportStatusType
    lastUpdatedDataTime: datetime
    testSetDiscrepancyTopErrors: TestSetDiscrepancyErrors
    testSetDiscrepancyRawOutputUrl: str
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadata


class ImportResourceSpecificationOutput(BaseValidatorModel):
    botImportSpecification: Optional[BotImportSpecificationOutput] = None
    botLocaleImportSpecification: Optional[BotLocaleImportSpecification] = None
    customVocabularyImportSpecification: Optional[CustomVocabularyImportSpecification] = None
    testSetImportResourceSpecification: Optional[TestSetImportResourceSpecificationOutput] = None


class ImportResourceSpecification(BaseValidatorModel):
    botImportSpecification: Optional[BotImportSpecification] = None
    botLocaleImportSpecification: Optional[BotLocaleImportSpecification] = None
    customVocabularyImportSpecification: Optional[CustomVocabularyImportSpecification] = None
    testSetImportResourceSpecification: Optional[TestSetImportResourceSpecification] = None


class UserTurnOutputSpecification(BaseValidatorModel):
    intent: UserTurnIntentOutput
    activeContexts: Optional[List[ActiveContext]] = None
    transcript: Optional[str] = None


class BuildtimeSettings(BaseValidatorModel):
    descriptiveBotBuilder: Optional[DescriptiveBotBuilderSpecification] = None
    sampleUtteranceGeneration: Optional[SampleUtteranceGenerationSpecification] = None


class RuntimeSettings(BaseValidatorModel):
    slotResolutionImprovement: Optional[SlotResolutionImprovementSpecification] = None


# This class is the output for the 'list_test_executions' function.
class ListTestExecutionsResponse(BaseValidatorModel):
    testExecutions: List[TestExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MessageGroupOutput(BaseValidatorModel):
    message: MessageOutput
    variations: Optional[List[MessageOutput]] = None


class UtteranceSpecification(BaseValidatorModel):
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
    botResponses: Optional[List[UtteranceBotResponse]] = None


class MessageGroup(BaseValidatorModel):
    message: Message
    variations: Optional[List[Message]] = None


class ConversationLogSettingsOutput(BaseValidatorModel):
    textLogSettings: Optional[List[TextLogSetting]] = None
    audioLogSettings: Optional[List[AudioLogSetting]] = None


class ConversationLogSettings(BaseValidatorModel):
    textLogSettings: Optional[List[TextLogSetting]] = None
    audioLogSettings: Optional[List[AudioLogSetting]] = None


# This class is the output for the 'describe_test_set_generation' function.
class DescribeTestSetGenerationResponse(BaseValidatorModel):
    testSetGenerationId: str
    testSetGenerationStatus: TestSetGenerationStatusType
    failureReasons: List[str]
    testSetId: str
    testSetName: str
    description: str
    storageLocation: TestSetStorageLocation
    generationDataSource: TestSetGenerationDataSourceOutput
    roleArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_test_set_generation' function.
class StartTestSetGenerationResponse(BaseValidatorModel):
    testSetGenerationId: str
    creationDateTime: datetime
    testSetGenerationStatus: TestSetGenerationStatusType
    testSetName: str
    description: str
    storageLocation: TestSetStorageLocation
    generationDataSource: TestSetGenerationDataSourceOutput
    roleArn: str
    testSetTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class TestSetGenerationDataSource(BaseValidatorModel):
    conversationLogsDataSource: Optional[ConversationLogsDataSource] = None


class TranscriptFilter(BaseValidatorModel):
    lexTranscriptFilter: Optional[LexTranscriptFilter] = None


class S3BucketTranscriptSourceOutput(BaseValidatorModel):
    s3BucketName: str
    transcriptFormat: Literal['Lex']
    pathFormat: Optional[PathFormatOutput] = None
    transcriptFilter: Optional[TranscriptFilterOutput] = None
    kmsKeyArn: Optional[str] = None


class QnAIntentConfigurationOutput(BaseValidatorModel):
    dataSourceConfiguration: Optional[DataSourceConfigurationOutput] = None
    bedrockModelConfiguration: Optional[BedrockModelSpecification] = None


class QnAIntentConfiguration(BaseValidatorModel):
    dataSourceConfiguration: Optional[DataSourceConfiguration] = None
    bedrockModelConfiguration: Optional[BedrockModelSpecification] = None


# This class is the output for the 'list_exports' function.
class ListExportsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    exportSummaries: List[ExportSummary]
    localeId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_slot_type' function.
class CreateSlotTypeResponse(BaseValidatorModel):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List[SlotTypeValueOutput]
    valueSelectionSetting: SlotValueSelectionSetting
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    externalSourceSetting: ExternalSourceSetting
    compositeSlotTypeSetting: CompositeSlotTypeSettingOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_slot_type' function.
class DescribeSlotTypeResponse(BaseValidatorModel):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List[SlotTypeValueOutput]
    valueSelectionSetting: SlotValueSelectionSetting
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    externalSourceSetting: ExternalSourceSetting
    compositeSlotTypeSetting: CompositeSlotTypeSettingOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_slot_type' function.
class UpdateSlotTypeResponse(BaseValidatorModel):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List[SlotTypeValueOutput]
    valueSelectionSetting: SlotValueSelectionSetting
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    externalSourceSetting: ExternalSourceSetting
    compositeSlotTypeSetting: CompositeSlotTypeSettingOutput
    ResponseMetadata: ResponseMetadata


class InputSessionStateSpecification(BaseValidatorModel):
    sessionAttributes: Optional[Dict[str, str]] = None
    activeContexts: Optional[List[ActiveContext]] = None
    runtimeHints: Optional[RuntimeHints] = None


# This class is the input for the 'create_slot_type' function.
class CreateSlotTypeRequest(BaseValidatorModel):
    slotTypeName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    slotTypeValues: Optional[List[SlotTypeValueUnion]] = None
    valueSelectionSetting: Optional[SlotValueSelectionSetting] = None
    parentSlotTypeSignature: Optional[str] = None
    externalSourceSetting: Optional[ExternalSourceSetting] = None
    compositeSlotTypeSetting: Optional[CompositeSlotTypeSettingUnion] = None


# This class is the input for the 'update_slot_type' function.
class UpdateSlotTypeRequest(BaseValidatorModel):
    slotTypeId: str
    slotTypeName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    slotTypeValues: Optional[List[SlotTypeValueUnion]] = None
    valueSelectionSetting: Optional[SlotValueSelectionSetting] = None
    parentSlotTypeSignature: Optional[str] = None
    externalSourceSetting: Optional[ExternalSourceSetting] = None
    compositeSlotTypeSetting: Optional[CompositeSlotTypeSettingUnion] = None


class IntentLevelSlotResolutionTestResults(BaseValidatorModel):
    items: List[IntentLevelSlotResolutionTestResultItem]


class DialogStateOutput(BaseValidatorModel):
    dialogAction: Optional[DialogAction] = None
    intent: Optional[IntentOverrideOutput] = None
    sessionAttributes: Optional[Dict[str, str]] = None


class DialogState(BaseValidatorModel):
    dialogAction: Optional[DialogAction] = None
    intent: Optional[IntentOverride] = None
    sessionAttributes: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_import' function.
class DescribeImportResponse(BaseValidatorModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationOutput
    importedResourceId: str
    importedResourceName: str
    mergeStrategy: MergeStrategyType
    importStatus: ImportStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_import' function.
class StartImportResponse(BaseValidatorModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationOutput
    mergeStrategy: MergeStrategyType
    importStatus: ImportStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata

ImportResourceSpecificationUnion = Union[ImportResourceSpecification, ImportResourceSpecificationOutput]


class GenerativeAISettings(BaseValidatorModel):
    runtimeSettings: Optional[RuntimeSettings] = None
    buildtimeSettings: Optional[BuildtimeSettings] = None


class FulfillmentStartResponseSpecificationOutput(BaseValidatorModel):
    delayInSeconds: int
    messageGroups: List[MessageGroupOutput]
    allowInterrupt: Optional[bool] = None


class FulfillmentUpdateResponseSpecificationOutput(BaseValidatorModel):
    frequencyInSeconds: int
    messageGroups: List[MessageGroupOutput]
    allowInterrupt: Optional[bool] = None


class PromptSpecificationOutput(BaseValidatorModel):
    messageGroups: List[MessageGroupOutput]
    maxRetries: int
    allowInterrupt: Optional[bool] = None
    messageSelectionStrategy: Optional[MessageSelectionStrategyType] = None
    promptAttemptsSpecification: Optional[Dict[PromptAttemptType, PromptAttemptSpecification]] = None


class ResponseSpecificationOutput(BaseValidatorModel):
    messageGroups: List[MessageGroupOutput]
    allowInterrupt: Optional[bool] = None


class StillWaitingResponseSpecificationOutput(BaseValidatorModel):
    messageGroups: List[MessageGroupOutput]
    frequencyInSeconds: int
    timeoutInSeconds: int
    allowInterrupt: Optional[bool] = None


# This class is the output for the 'list_utterance_analytics_data' function.
class ListUtteranceAnalyticsDataResponse(BaseValidatorModel):
    botId: str
    utterances: List[UtteranceSpecification]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FulfillmentStartResponseSpecification(BaseValidatorModel):
    delayInSeconds: int
    messageGroups: List[MessageGroup]
    allowInterrupt: Optional[bool] = None


class FulfillmentUpdateResponseSpecification(BaseValidatorModel):
    frequencyInSeconds: int
    messageGroups: List[MessageGroup]
    allowInterrupt: Optional[bool] = None


class PromptSpecification(BaseValidatorModel):
    messageGroups: List[MessageGroup]
    maxRetries: int
    allowInterrupt: Optional[bool] = None
    messageSelectionStrategy: Optional[MessageSelectionStrategyType] = None
    promptAttemptsSpecification: Optional[Dict[PromptAttemptType, PromptAttemptSpecification]] = None


class ResponseSpecification(BaseValidatorModel):
    messageGroups: List[MessageGroup]
    allowInterrupt: Optional[bool] = None


class StillWaitingResponseSpecification(BaseValidatorModel):
    messageGroups: List[MessageGroup]
    frequencyInSeconds: int
    timeoutInSeconds: int
    allowInterrupt: Optional[bool] = None


# This class is the output for the 'create_bot_alias' function.
class CreateBotAliasResponse(BaseValidatorModel):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, BotAliasLocaleSettings]
    conversationLogSettings: ConversationLogSettingsOutput
    sentimentAnalysisSettings: SentimentAnalysisSettings
    botAliasStatus: BotAliasStatusType
    botId: str
    creationDateTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bot_alias' function.
class DescribeBotAliasResponse(BaseValidatorModel):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, BotAliasLocaleSettings]
    conversationLogSettings: ConversationLogSettingsOutput
    sentimentAnalysisSettings: SentimentAnalysisSettings
    botAliasHistoryEvents: List[BotAliasHistoryEvent]
    botAliasStatus: BotAliasStatusType
    botId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    parentBotNetworks: List[ParentBotNetwork]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bot_alias' function.
class UpdateBotAliasResponse(BaseValidatorModel):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, BotAliasLocaleSettings]
    conversationLogSettings: ConversationLogSettingsOutput
    sentimentAnalysisSettings: SentimentAnalysisSettings
    botAliasStatus: BotAliasStatusType
    botId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadata

ConversationLogSettingsUnion = Union[ConversationLogSettings, ConversationLogSettingsOutput]

TestSetGenerationDataSourceUnion = Union[TestSetGenerationDataSource, TestSetGenerationDataSourceOutput]


class S3BucketTranscriptSource(BaseValidatorModel):
    s3BucketName: str
    transcriptFormat: Literal['Lex']
    pathFormat: Optional[PathFormat] = None
    transcriptFilter: Optional[TranscriptFilter] = None
    kmsKeyArn: Optional[str] = None


class TranscriptSourceSettingOutput(BaseValidatorModel):
    s3BucketTranscriptSource: Optional[S3BucketTranscriptSourceOutput] = None

QnAIntentConfigurationUnion = Union[QnAIntentConfiguration, QnAIntentConfigurationOutput]


class UserTurnInputSpecification(BaseValidatorModel):
    utteranceInput: UtteranceInputSpecification
    requestAttributes: Optional[Dict[str, str]] = None
    sessionState: Optional[InputSessionStateSpecification] = None


# This class is the input for the 'start_import' function.
class StartImportRequest(BaseValidatorModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationUnion
    mergeStrategy: MergeStrategyType
    filePassword: Optional[str] = None


# This class is the input for the 'create_bot_locale' function.
class CreateBotLocaleRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: float
    description: Optional[str] = None
    voiceSettings: Optional[VoiceSettings] = None
    generativeAISettings: Optional[GenerativeAISettings] = None


# This class is the output for the 'create_bot_locale' function.
class CreateBotLocaleResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeName: str
    localeId: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: VoiceSettings
    botLocaleStatus: BotLocaleStatusType
    creationDateTime: datetime
    generativeAISettings: GenerativeAISettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bot_locale' function.
class DescribeBotLocaleResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    localeName: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: VoiceSettings
    intentsCount: int
    slotTypesCount: int
    botLocaleStatus: BotLocaleStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    lastBuildSubmittedDateTime: datetime
    botLocaleHistoryEvents: List[BotLocaleHistoryEvent]
    recommendedActions: List[str]
    generativeAISettings: GenerativeAISettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_bot_locale' function.
class UpdateBotLocaleRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: float
    description: Optional[str] = None
    voiceSettings: Optional[VoiceSettings] = None
    generativeAISettings: Optional[GenerativeAISettings] = None


# This class is the output for the 'update_bot_locale' function.
class UpdateBotLocaleResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    localeName: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: VoiceSettings
    botLocaleStatus: BotLocaleStatusType
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    recommendedActions: List[str]
    generativeAISettings: GenerativeAISettings
    ResponseMetadata: ResponseMetadata


class FulfillmentUpdatesSpecificationOutput(BaseValidatorModel):
    active: bool
    startResponse: Optional[FulfillmentStartResponseSpecificationOutput] = None
    updateResponse: Optional[FulfillmentUpdateResponseSpecificationOutput] = None
    timeoutInSeconds: Optional[int] = None


class SlotSummary(BaseValidatorModel):
    slotId: Optional[str] = None
    slotName: Optional[str] = None
    description: Optional[str] = None
    slotConstraint: Optional[SlotConstraintType] = None
    slotTypeId: Optional[str] = None
    valueElicitationPromptSpecification: Optional[PromptSpecificationOutput] = None
    lastUpdatedDateTime: Optional[datetime] = None


class ConditionalBranchOutput(BaseValidatorModel):
    name: str
    condition: Condition
    nextStep: DialogStateOutput
    response: Optional[ResponseSpecificationOutput] = None


class DefaultConditionalBranchOutput(BaseValidatorModel):
    nextStep: Optional[DialogStateOutput] = None
    response: Optional[ResponseSpecificationOutput] = None


class WaitAndContinueSpecificationOutput(BaseValidatorModel):
    waitingResponse: ResponseSpecificationOutput
    continueResponse: ResponseSpecificationOutput
    stillWaitingResponse: Optional[StillWaitingResponseSpecificationOutput] = None
    active: Optional[bool] = None


class FulfillmentUpdatesSpecification(BaseValidatorModel):
    active: bool
    startResponse: Optional[FulfillmentStartResponseSpecification] = None
    updateResponse: Optional[FulfillmentUpdateResponseSpecification] = None
    timeoutInSeconds: Optional[int] = None


class ConditionalBranch(BaseValidatorModel):
    name: str
    condition: Condition
    nextStep: DialogState
    response: Optional[ResponseSpecification] = None


class DefaultConditionalBranch(BaseValidatorModel):
    nextStep: Optional[DialogState] = None
    response: Optional[ResponseSpecification] = None


class WaitAndContinueSpecification(BaseValidatorModel):
    waitingResponse: ResponseSpecification
    continueResponse: ResponseSpecification
    stillWaitingResponse: Optional[StillWaitingResponseSpecification] = None
    active: Optional[bool] = None


# This class is the input for the 'create_bot_alias' function.
class CreateBotAliasRequest(BaseValidatorModel):
    botAliasName: str
    botId: str
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasLocaleSettings: Optional[Dict[str, BotAliasLocaleSettings]] = None
    conversationLogSettings: Optional[ConversationLogSettingsUnion] = None
    sentimentAnalysisSettings: Optional[SentimentAnalysisSettings] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_bot_alias' function.
class UpdateBotAliasRequest(BaseValidatorModel):
    botAliasId: str
    botAliasName: str
    botId: str
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasLocaleSettings: Optional[Dict[str, BotAliasLocaleSettings]] = None
    conversationLogSettings: Optional[ConversationLogSettingsUnion] = None
    sentimentAnalysisSettings: Optional[SentimentAnalysisSettings] = None


# This class is the input for the 'start_test_set_generation' function.
class StartTestSetGenerationRequest(BaseValidatorModel):
    testSetName: str
    storageLocation: TestSetStorageLocation
    generationDataSource: TestSetGenerationDataSourceUnion
    roleArn: str
    description: Optional[str] = None
    testSetTags: Optional[Dict[str, str]] = None


class TranscriptSourceSetting(BaseValidatorModel):
    s3BucketTranscriptSource: Optional[S3BucketTranscriptSource] = None


# This class is the output for the 'describe_bot_recommendation' function.
class DescribeBotRecommendationResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingOutput
    encryptionSetting: EncryptionSetting
    botRecommendationResults: BotRecommendationResults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_bot_recommendation' function.
class StartBotRecommendationResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingOutput
    encryptionSetting: EncryptionSetting
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bot_recommendation' function.
class UpdateBotRecommendationResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingOutput
    encryptionSetting: EncryptionSetting
    ResponseMetadata: ResponseMetadata


class UserTurnResult(BaseValidatorModel):
    input: UserTurnInputSpecification
    expectedOutput: UserTurnOutputSpecification
    actualOutput: Optional[UserTurnOutputSpecification] = None
    errorDetails: Optional[ExecutionErrorDetails] = None
    endToEndResult: Optional[TestResultMatchStatusType] = None
    intentMatchResult: Optional[TestResultMatchStatusType] = None
    slotMatchResult: Optional[TestResultMatchStatusType] = None
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None
    conversationLevelResult: Optional[ConversationLevelResultDetail] = None


class UserTurnSpecification(BaseValidatorModel):
    input: UserTurnInputSpecification
    expected: UserTurnOutputSpecification


# This class is the output for the 'list_slots' function.
class ListSlotsResponse(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    slotSummaries: List[SlotSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConditionalSpecificationOutput(BaseValidatorModel):
    active: bool
    conditionalBranches: List[ConditionalBranchOutput]
    defaultBranch: DefaultConditionalBranchOutput


class SubSlotValueElicitationSettingOutput(BaseValidatorModel):
    promptSpecification: PromptSpecificationOutput
    defaultValueSpecification: Optional[SlotDefaultValueSpecificationOutput] = None
    sampleUtterances: Optional[List[SampleUtterance]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecificationOutput] = None


class ConditionalSpecification(BaseValidatorModel):
    active: bool
    conditionalBranches: List[ConditionalBranch]
    defaultBranch: DefaultConditionalBranch


class SubSlotValueElicitationSetting(BaseValidatorModel):
    promptSpecification: PromptSpecification
    defaultValueSpecification: Optional[SlotDefaultValueSpecification] = None
    sampleUtterances: Optional[List[SampleUtterance]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecification] = None

TranscriptSourceSettingUnion = Union[TranscriptSourceSetting, TranscriptSourceSettingOutput]


class TestSetTurnResult(BaseValidatorModel):
    agent: Optional[AgentTurnResult] = None
    user: Optional[UserTurnResult] = None


class TurnSpecification(BaseValidatorModel):
    agentTurn: Optional[AgentTurnSpecification] = None
    userTurn: Optional[UserTurnSpecification] = None


class IntentClosingSettingOutput(BaseValidatorModel):
    closingResponse: Optional[ResponseSpecificationOutput] = None
    active: Optional[bool] = None
    nextStep: Optional[DialogStateOutput] = None
    conditional: Optional[ConditionalSpecificationOutput] = None


class PostDialogCodeHookInvocationSpecificationOutput(BaseValidatorModel):
    successResponse: Optional[ResponseSpecificationOutput] = None
    successNextStep: Optional[DialogStateOutput] = None
    successConditional: Optional[ConditionalSpecificationOutput] = None
    failureResponse: Optional[ResponseSpecificationOutput] = None
    failureNextStep: Optional[DialogStateOutput] = None
    failureConditional: Optional[ConditionalSpecificationOutput] = None
    timeoutResponse: Optional[ResponseSpecificationOutput] = None
    timeoutNextStep: Optional[DialogStateOutput] = None
    timeoutConditional: Optional[ConditionalSpecificationOutput] = None


class PostFulfillmentStatusSpecificationOutput(BaseValidatorModel):
    successResponse: Optional[ResponseSpecificationOutput] = None
    failureResponse: Optional[ResponseSpecificationOutput] = None
    timeoutResponse: Optional[ResponseSpecificationOutput] = None
    successNextStep: Optional[DialogStateOutput] = None
    successConditional: Optional[ConditionalSpecificationOutput] = None
    failureNextStep: Optional[DialogStateOutput] = None
    failureConditional: Optional[ConditionalSpecificationOutput] = None
    timeoutNextStep: Optional[DialogStateOutput] = None
    timeoutConditional: Optional[ConditionalSpecificationOutput] = None


class SpecificationsOutput(BaseValidatorModel):
    slotTypeId: str
    valueElicitationSetting: SubSlotValueElicitationSettingOutput


class IntentClosingSetting(BaseValidatorModel):
    closingResponse: Optional[ResponseSpecification] = None
    active: Optional[bool] = None
    nextStep: Optional[DialogState] = None
    conditional: Optional[ConditionalSpecification] = None


class PostDialogCodeHookInvocationSpecification(BaseValidatorModel):
    successResponse: Optional[ResponseSpecification] = None
    successNextStep: Optional[DialogState] = None
    successConditional: Optional[ConditionalSpecification] = None
    failureResponse: Optional[ResponseSpecification] = None
    failureNextStep: Optional[DialogState] = None
    failureConditional: Optional[ConditionalSpecification] = None
    timeoutResponse: Optional[ResponseSpecification] = None
    timeoutNextStep: Optional[DialogState] = None
    timeoutConditional: Optional[ConditionalSpecification] = None


class PostFulfillmentStatusSpecification(BaseValidatorModel):
    successResponse: Optional[ResponseSpecification] = None
    failureResponse: Optional[ResponseSpecification] = None
    timeoutResponse: Optional[ResponseSpecification] = None
    successNextStep: Optional[DialogState] = None
    successConditional: Optional[ConditionalSpecification] = None
    failureNextStep: Optional[DialogState] = None
    failureConditional: Optional[ConditionalSpecification] = None
    timeoutNextStep: Optional[DialogState] = None
    timeoutConditional: Optional[ConditionalSpecification] = None


class Specifications(BaseValidatorModel):
    slotTypeId: str
    valueElicitationSetting: SubSlotValueElicitationSetting


# This class is the input for the 'start_bot_recommendation' function.
class StartBotRecommendationRequest(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    transcriptSourceSetting: TranscriptSourceSettingUnion
    encryptionSetting: Optional[EncryptionSetting] = None


class UtteranceLevelTestResultItem(BaseValidatorModel):
    recordNumber: int
    turnResult: TestSetTurnResult
    conversationId: Optional[str] = None


class TestSetTurnRecord(BaseValidatorModel):
    recordNumber: int
    turnSpecification: TurnSpecification
    conversationId: Optional[str] = None
    turnNumber: Optional[int] = None


class DialogCodeHookInvocationSettingOutput(BaseValidatorModel):
    enableCodeHookInvocation: bool
    active: bool
    postCodeHookSpecification: PostDialogCodeHookInvocationSpecificationOutput
    invocationLabel: Optional[str] = None


class FulfillmentCodeHookSettingsOutput(BaseValidatorModel):
    enabled: bool
    postFulfillmentStatusSpecification: Optional[PostFulfillmentStatusSpecificationOutput] = None
    fulfillmentUpdatesSpecification: Optional[FulfillmentUpdatesSpecificationOutput] = None
    active: Optional[bool] = None


class SubSlotSettingOutput(BaseValidatorModel):
    expression: Optional[str] = None
    slotSpecifications: Optional[Dict[str, SpecificationsOutput]] = None

IntentClosingSettingUnion = Union[IntentClosingSetting, IntentClosingSettingOutput]


class DialogCodeHookInvocationSetting(BaseValidatorModel):
    enableCodeHookInvocation: bool
    active: bool
    postCodeHookSpecification: PostDialogCodeHookInvocationSpecification
    invocationLabel: Optional[str] = None


class FulfillmentCodeHookSettings(BaseValidatorModel):
    enabled: bool
    postFulfillmentStatusSpecification: Optional[PostFulfillmentStatusSpecification] = None
    fulfillmentUpdatesSpecification: Optional[FulfillmentUpdatesSpecification] = None
    active: Optional[bool] = None


class SubSlotSetting(BaseValidatorModel):
    expression: Optional[str] = None
    slotSpecifications: Optional[Dict[str, Specifications]] = None


class UtteranceLevelTestResults(BaseValidatorModel):
    items: List[UtteranceLevelTestResultItem]


# This class is the output for the 'list_test_set_records' function.
class ListTestSetRecordsResponse(BaseValidatorModel):
    testSetRecords: List[TestSetTurnRecord]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InitialResponseSettingOutput(BaseValidatorModel):
    initialResponse: Optional[ResponseSpecificationOutput] = None
    nextStep: Optional[DialogStateOutput] = None
    conditional: Optional[ConditionalSpecificationOutput] = None
    codeHook: Optional[DialogCodeHookInvocationSettingOutput] = None


class IntentConfirmationSettingOutput(BaseValidatorModel):
    promptSpecification: PromptSpecificationOutput
    declinationResponse: Optional[ResponseSpecificationOutput] = None
    active: Optional[bool] = None
    confirmationResponse: Optional[ResponseSpecificationOutput] = None
    confirmationNextStep: Optional[DialogStateOutput] = None
    confirmationConditional: Optional[ConditionalSpecificationOutput] = None
    declinationNextStep: Optional[DialogStateOutput] = None
    declinationConditional: Optional[ConditionalSpecificationOutput] = None
    failureResponse: Optional[ResponseSpecificationOutput] = None
    failureNextStep: Optional[DialogStateOutput] = None
    failureConditional: Optional[ConditionalSpecificationOutput] = None
    codeHook: Optional[DialogCodeHookInvocationSettingOutput] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSetting] = None


class SlotCaptureSettingOutput(BaseValidatorModel):
    captureResponse: Optional[ResponseSpecificationOutput] = None
    captureNextStep: Optional[DialogStateOutput] = None
    captureConditional: Optional[ConditionalSpecificationOutput] = None
    failureResponse: Optional[ResponseSpecificationOutput] = None
    failureNextStep: Optional[DialogStateOutput] = None
    failureConditional: Optional[ConditionalSpecificationOutput] = None
    codeHook: Optional[DialogCodeHookInvocationSettingOutput] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSetting] = None


class InitialResponseSetting(BaseValidatorModel):
    initialResponse: Optional[ResponseSpecification] = None
    nextStep: Optional[DialogState] = None
    conditional: Optional[ConditionalSpecification] = None
    codeHook: Optional[DialogCodeHookInvocationSetting] = None


class IntentConfirmationSetting(BaseValidatorModel):
    promptSpecification: PromptSpecification
    declinationResponse: Optional[ResponseSpecification] = None
    active: Optional[bool] = None
    confirmationResponse: Optional[ResponseSpecification] = None
    confirmationNextStep: Optional[DialogState] = None
    confirmationConditional: Optional[ConditionalSpecification] = None
    declinationNextStep: Optional[DialogState] = None
    declinationConditional: Optional[ConditionalSpecification] = None
    failureResponse: Optional[ResponseSpecification] = None
    failureNextStep: Optional[DialogState] = None
    failureConditional: Optional[ConditionalSpecification] = None
    codeHook: Optional[DialogCodeHookInvocationSetting] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSetting] = None


class SlotCaptureSetting(BaseValidatorModel):
    captureResponse: Optional[ResponseSpecification] = None
    captureNextStep: Optional[DialogState] = None
    captureConditional: Optional[ConditionalSpecification] = None
    failureResponse: Optional[ResponseSpecification] = None
    failureNextStep: Optional[DialogState] = None
    failureConditional: Optional[ConditionalSpecification] = None
    codeHook: Optional[DialogCodeHookInvocationSetting] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSetting] = None

FulfillmentCodeHookSettingsUnion = Union[FulfillmentCodeHookSettings, FulfillmentCodeHookSettingsOutput]

SubSlotSettingUnion = Union[SubSlotSetting, SubSlotSettingOutput]


class TestExecutionResultItems(BaseValidatorModel):
    overallTestResults: Optional[OverallTestResults] = None
    conversationLevelTestResults: Optional[ConversationLevelTestResults] = None
    intentClassificationTestResults: Optional[IntentClassificationTestResults] = None
    intentLevelSlotResolutionTestResults: Optional[IntentLevelSlotResolutionTestResults] = None
    utteranceLevelTestResults: Optional[UtteranceLevelTestResults] = None


# This class is the output for the 'create_intent' function.
class CreateIntentResponse(BaseValidatorModel):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List[SampleUtterance]
    dialogCodeHook: DialogCodeHookSettings
    fulfillmentCodeHook: FulfillmentCodeHookSettingsOutput
    intentConfirmationSetting: IntentConfirmationSettingOutput
    intentClosingSetting: IntentClosingSettingOutput
    inputContexts: List[InputContext]
    outputContexts: List[OutputContext]
    kendraConfiguration: KendraConfiguration
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    initialResponseSetting: InitialResponseSettingOutput
    qnAIntentConfiguration: QnAIntentConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_intent' function.
class DescribeIntentResponse(BaseValidatorModel):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List[SampleUtterance]
    dialogCodeHook: DialogCodeHookSettings
    fulfillmentCodeHook: FulfillmentCodeHookSettingsOutput
    slotPriorities: List[SlotPriority]
    intentConfirmationSetting: IntentConfirmationSettingOutput
    intentClosingSetting: IntentClosingSettingOutput
    inputContexts: List[InputContext]
    outputContexts: List[OutputContext]
    kendraConfiguration: KendraConfiguration
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    initialResponseSetting: InitialResponseSettingOutput
    qnAIntentConfiguration: QnAIntentConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_intent' function.
class UpdateIntentResponse(BaseValidatorModel):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List[SampleUtterance]
    dialogCodeHook: DialogCodeHookSettings
    fulfillmentCodeHook: FulfillmentCodeHookSettingsOutput
    slotPriorities: List[SlotPriority]
    intentConfirmationSetting: IntentConfirmationSettingOutput
    intentClosingSetting: IntentClosingSettingOutput
    inputContexts: List[InputContext]
    outputContexts: List[OutputContext]
    kendraConfiguration: KendraConfiguration
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    initialResponseSetting: InitialResponseSettingOutput
    qnAIntentConfiguration: QnAIntentConfigurationOutput
    ResponseMetadata: ResponseMetadata


class SlotValueElicitationSettingOutput(BaseValidatorModel):
    slotConstraint: SlotConstraintType
    defaultValueSpecification: Optional[SlotDefaultValueSpecificationOutput] = None
    promptSpecification: Optional[PromptSpecificationOutput] = None
    sampleUtterances: Optional[List[SampleUtterance]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecificationOutput] = None
    slotCaptureSetting: Optional[SlotCaptureSettingOutput] = None
    slotResolutionSetting: Optional[SlotResolutionSetting] = None

InitialResponseSettingUnion = Union[InitialResponseSetting, InitialResponseSettingOutput]

IntentConfirmationSettingUnion = Union[IntentConfirmationSetting, IntentConfirmationSettingOutput]


class SlotValueElicitationSetting(BaseValidatorModel):
    slotConstraint: SlotConstraintType
    defaultValueSpecification: Optional[SlotDefaultValueSpecification] = None
    promptSpecification: Optional[PromptSpecification] = None
    sampleUtterances: Optional[List[SampleUtterance]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecification] = None
    slotCaptureSetting: Optional[SlotCaptureSetting] = None
    slotResolutionSetting: Optional[SlotResolutionSetting] = None


# This class is the output for the 'list_test_execution_result_items' function.
class ListTestExecutionResultItemsResponse(BaseValidatorModel):
    testExecutionResults: TestExecutionResultItems
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_slot' function.
class CreateSlotResponse(BaseValidatorModel):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: SlotValueElicitationSettingOutput
    obfuscationSetting: ObfuscationSetting
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    multipleValuesSetting: MultipleValuesSetting
    subSlotSetting: SubSlotSettingOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_slot' function.
class DescribeSlotResponse(BaseValidatorModel):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: SlotValueElicitationSettingOutput
    obfuscationSetting: ObfuscationSetting
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    multipleValuesSetting: MultipleValuesSetting
    subSlotSetting: SubSlotSettingOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_slot' function.
class UpdateSlotResponse(BaseValidatorModel):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: SlotValueElicitationSettingOutput
    obfuscationSetting: ObfuscationSetting
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    multipleValuesSetting: MultipleValuesSetting
    subSlotSetting: SubSlotSettingOutput
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_intent' function.
class CreateIntentRequest(BaseValidatorModel):
    intentName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    sampleUtterances: Optional[List[SampleUtterance]] = None
    dialogCodeHook: Optional[DialogCodeHookSettings] = None
    fulfillmentCodeHook: Optional[FulfillmentCodeHookSettingsUnion] = None
    intentConfirmationSetting: Optional[IntentConfirmationSettingUnion] = None
    intentClosingSetting: Optional[IntentClosingSettingUnion] = None
    inputContexts: Optional[List[InputContext]] = None
    outputContexts: Optional[List[OutputContext]] = None
    kendraConfiguration: Optional[KendraConfiguration] = None
    initialResponseSetting: Optional[InitialResponseSettingUnion] = None
    qnAIntentConfiguration: Optional[QnAIntentConfigurationUnion] = None


# This class is the input for the 'update_intent' function.
class UpdateIntentRequest(BaseValidatorModel):
    intentId: str
    intentName: str
    botId: str
    botVersion: str
    localeId: str
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    sampleUtterances: Optional[List[SampleUtterance]] = None
    dialogCodeHook: Optional[DialogCodeHookSettings] = None
    fulfillmentCodeHook: Optional[FulfillmentCodeHookSettingsUnion] = None
    slotPriorities: Optional[List[SlotPriority]] = None
    intentConfirmationSetting: Optional[IntentConfirmationSettingUnion] = None
    intentClosingSetting: Optional[IntentClosingSettingUnion] = None
    inputContexts: Optional[List[InputContext]] = None
    outputContexts: Optional[List[OutputContext]] = None
    kendraConfiguration: Optional[KendraConfiguration] = None
    initialResponseSetting: Optional[InitialResponseSettingUnion] = None
    qnAIntentConfiguration: Optional[QnAIntentConfigurationUnion] = None

SlotValueElicitationSettingUnion = Union[SlotValueElicitationSetting, SlotValueElicitationSettingOutput]


# This class is the input for the 'create_slot' function.
class CreateSlotRequest(BaseValidatorModel):
    slotName: str
    valueElicitationSetting: SlotValueElicitationSettingUnion
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    description: Optional[str] = None
    slotTypeId: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSetting] = None
    multipleValuesSetting: Optional[MultipleValuesSetting] = None
    subSlotSetting: Optional[SubSlotSettingUnion] = None


# This class is the input for the 'update_slot' function.
class UpdateSlotRequest(BaseValidatorModel):
    slotId: str
    slotName: str
    valueElicitationSetting: SlotValueElicitationSettingUnion
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    description: Optional[str] = None
    slotTypeId: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSetting] = None
    multipleValuesSetting: Optional[MultipleValuesSetting] = None
    subSlotSetting: Optional[SubSlotSettingUnion] = None