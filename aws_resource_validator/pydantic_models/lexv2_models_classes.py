from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ActiveContextTypeDef(BaseValidatorModel):
    name: str

class AdvancedRecognitionSettingTypeDef(BaseValidatorModel):
    audioRecognitionStrategy: Optional[Literal["UseSlotValuesAsCustomVocabulary"]] = None

class ExecutionErrorDetailsTypeDef(BaseValidatorModel):
    errorCode: str
    errorMessage: str

class AgentTurnSpecificationTypeDef(BaseValidatorModel):
    agentPrompt: str

class AggregatedUtterancesFilterTypeDef(BaseValidatorModel):
    name: Literal["Utterance"]
    values: Sequence[str]
    operator: AggregatedUtterancesFilterOperatorType

class AggregatedUtterancesSortByTypeDef(BaseValidatorModel):
    attribute: AggregatedUtterancesSortAttributeType
    order: SortOrderType

class AggregatedUtterancesSummaryTypeDef(BaseValidatorModel):
    utterance: Optional[str] = None
    hitCount: Optional[int] = None
    missedCount: Optional[int] = None
    utteranceFirstRecordedInAggregationDuration: Optional[datetime] = None
    utteranceLastRecordedInAggregationDuration: Optional[datetime] = None
    containsDataFromDeletedResources: Optional[bool] = None

class AllowedInputTypesTypeDef(BaseValidatorModel):
    allowAudioInput: bool
    allowDTMFInput: bool

class AnalyticsBinBySpecificationTypeDef(BaseValidatorModel):
    name: AnalyticsBinByNameType
    interval: AnalyticsIntervalType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsBinKeyTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsBinByNameType] = None
    value: Optional[int] = None

class AnalyticsIntentFilterTypeDef(BaseValidatorModel):
    name: AnalyticsIntentFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsIntentGroupByKeyTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsIntentFieldType] = None
    value: Optional[str] = None

class AnalyticsIntentGroupBySpecificationTypeDef(BaseValidatorModel):
    name: AnalyticsIntentFieldType

class AnalyticsIntentMetricResultTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsIntentMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsIntentMetricTypeDef(BaseValidatorModel):
    name: AnalyticsIntentMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsIntentNodeSummaryTypeDef(BaseValidatorModel):
    intentName: Optional[str] = None
    intentPath: Optional[str] = None
    intentCount: Optional[int] = None
    intentLevel: Optional[int] = None
    nodeType: Optional[AnalyticsNodeTypeType] = None

class AnalyticsIntentStageFilterTypeDef(BaseValidatorModel):
    name: AnalyticsIntentStageFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsIntentStageGroupByKeyTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsIntentStageFieldType] = None
    value: Optional[str] = None

class AnalyticsIntentStageGroupBySpecificationTypeDef(BaseValidatorModel):
    name: AnalyticsIntentStageFieldType

class AnalyticsIntentStageMetricResultTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsIntentStageMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsIntentStageMetricTypeDef(BaseValidatorModel):
    name: AnalyticsIntentStageMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsPathFilterTypeDef(BaseValidatorModel):
    name: AnalyticsCommonFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsSessionFilterTypeDef(BaseValidatorModel):
    name: AnalyticsSessionFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsSessionGroupByKeyTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsSessionFieldType] = None
    value: Optional[str] = None

class AnalyticsSessionGroupBySpecificationTypeDef(BaseValidatorModel):
    name: AnalyticsSessionFieldType

class AnalyticsSessionMetricResultTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsSessionMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsSessionMetricTypeDef(BaseValidatorModel):
    name: AnalyticsSessionMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AnalyticsUtteranceAttributeResultTypeDef(BaseValidatorModel):
    lastUsedIntent: Optional[str] = None

class AnalyticsUtteranceAttributeTypeDef(BaseValidatorModel):
    name: Literal["LastUsedIntent"]

class AnalyticsUtteranceFilterTypeDef(BaseValidatorModel):
    name: AnalyticsUtteranceFilterNameType
    operator: AnalyticsFilterOperatorType
    values: Sequence[str]

class AnalyticsUtteranceGroupByKeyTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsUtteranceFieldType] = None
    value: Optional[str] = None

class AnalyticsUtteranceGroupBySpecificationTypeDef(BaseValidatorModel):
    name: AnalyticsUtteranceFieldType

class AnalyticsUtteranceMetricResultTypeDef(BaseValidatorModel):
    name: Optional[AnalyticsUtteranceMetricNameType] = None
    statistic: Optional[AnalyticsMetricStatisticType] = None
    value: Optional[float] = None

class AnalyticsUtteranceMetricTypeDef(BaseValidatorModel):
    name: AnalyticsUtteranceMetricNameType
    statistic: AnalyticsMetricStatisticType
    order: Optional[AnalyticsSortOrderType] = None

class AssociatedTranscriptFilterTypeDef(BaseValidatorModel):
    name: AssociatedTranscriptFilterNameType
    values: Sequence[str]

class AssociatedTranscriptTypeDef(BaseValidatorModel):
    transcript: Optional[str] = None

class AudioSpecificationTypeDef(BaseValidatorModel):
    maxLengthMs: int
    endTimeoutMs: int

class DTMFSpecificationTypeDef(BaseValidatorModel):
    maxLength: int
    endTimeoutMs: int
    deletionCharacter: str
    endCharacter: str

class S3BucketLogDestinationTypeDef(BaseValidatorModel):
    s3BucketArn: str
    logPrefix: str
    kmsKeyArn: Optional[str] = None

class NewCustomVocabularyItemTypeDef(BaseValidatorModel):
    phrase: str
    weight: Optional[int] = None
    displayAs: Optional[str] = None

class CustomVocabularyItemTypeDef(BaseValidatorModel):
    itemId: str
    phrase: str
    weight: Optional[int] = None
    displayAs: Optional[str] = None

class FailedCustomVocabularyItemTypeDef(BaseValidatorModel):
    itemId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CustomVocabularyEntryIdTypeDef(BaseValidatorModel):
    itemId: str

class BedrockKnowledgeStoreConfigurationTypeDef(BaseValidatorModel):
    bedrockKnowledgeBaseArn: str

class BedrockModelSpecificationTypeDef(BaseValidatorModel):
    modelArn: str

class BotAliasHistoryEventTypeDef(BaseValidatorModel):
    botVersion: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None

class BotAliasReplicaSummaryTypeDef(BaseValidatorModel):
    botAliasId: Optional[str] = None
    botAliasReplicationStatus: Optional[BotAliasReplicationStatusType] = None
    botVersion: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReasons: Optional[List[str]] = None

class BotAliasSummaryTypeDef(BaseValidatorModel):
    botAliasId: Optional[str] = None
    botAliasName: Optional[str] = None
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasStatus: Optional[BotAliasStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class BotAliasTestExecutionTargetTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str

class BotExportSpecificationTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str

class BotFilterTypeDef(BaseValidatorModel):
    name: BotFilterNameType
    values: Sequence[str]
    operator: BotFilterOperatorType

class DataPrivacyTypeDef(BaseValidatorModel):
    childDirected: bool

class BotLocaleExportSpecificationTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class BotLocaleFilterTypeDef(BaseValidatorModel):
    name: Literal["BotLocaleName"]
    values: Sequence[str]
    operator: BotLocaleFilterOperatorType

class BotLocaleHistoryEventTypeDef(BaseValidatorModel):
    event: str
    eventDate: datetime

class VoiceSettingsTypeDef(BaseValidatorModel):
    voiceId: str
    engine: Optional[VoiceEngineType] = None

class BotLocaleSortByTypeDef(BaseValidatorModel):
    attribute: Literal["BotLocaleName"]
    order: SortOrderType

class BotLocaleSummaryTypeDef(BaseValidatorModel):
    localeId: Optional[str] = None
    localeName: Optional[str] = None
    description: Optional[str] = None
    botLocaleStatus: Optional[BotLocaleStatusType] = None
    lastUpdatedDateTime: Optional[datetime] = None
    lastBuildSubmittedDateTime: Optional[datetime] = None

class BotMemberTypeDef(BaseValidatorModel):
    botMemberId: str
    botMemberName: str
    botMemberAliasId: str
    botMemberAliasName: str
    botMemberVersion: str

class IntentStatisticsTypeDef(BaseValidatorModel):
    discoveredIntentCount: Optional[int] = None

class SlotTypeStatisticsTypeDef(BaseValidatorModel):
    discoveredSlotTypeCount: Optional[int] = None

class BotRecommendationSummaryTypeDef(BaseValidatorModel):
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class BotReplicaSummaryTypeDef(BaseValidatorModel):
    replicaRegion: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    botReplicaStatus: Optional[BotReplicaStatusType] = None
    failureReasons: Optional[List[str]] = None

class BotSortByTypeDef(BaseValidatorModel):
    attribute: Literal["BotName"]
    order: SortOrderType

class BotSummaryTypeDef(BaseValidatorModel):
    botId: Optional[str] = None
    botName: Optional[str] = None
    description: Optional[str] = None
    botStatus: Optional[BotStatusType] = None
    latestBotVersion: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None
    botType: Optional[BotTypeType] = None

class BotVersionLocaleDetailsTypeDef(BaseValidatorModel):
    sourceBotVersion: str

class BotVersionReplicaSortByTypeDef(BaseValidatorModel):
    attribute: Literal["BotVersion"]
    order: SortOrderType

class BotVersionReplicaSummaryTypeDef(BaseValidatorModel):
    botVersion: Optional[str] = None
    botVersionReplicationStatus: Optional[BotVersionReplicationStatusType] = None
    creationDateTime: Optional[datetime] = None
    failureReasons: Optional[List[str]] = None

class BotVersionSortByTypeDef(BaseValidatorModel):
    attribute: Literal["BotVersion"]
    order: SortOrderType

class BotVersionSummaryTypeDef(BaseValidatorModel):
    botName: Optional[str] = None
    botVersion: Optional[str] = None
    description: Optional[str] = None
    botStatus: Optional[BotStatusType] = None
    creationDateTime: Optional[datetime] = None

class BuildBotLocaleRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class BuiltInIntentSortByTypeDef(BaseValidatorModel):
    attribute: Literal["IntentSignature"]
    order: SortOrderType

class BuiltInIntentSummaryTypeDef(BaseValidatorModel):
    intentSignature: Optional[str] = None
    description: Optional[str] = None

class BuiltInSlotTypeSortByTypeDef(BaseValidatorModel):
    attribute: Literal["SlotTypeSignature"]
    order: SortOrderType

class BuiltInSlotTypeSummaryTypeDef(BaseValidatorModel):
    slotTypeSignature: Optional[str] = None
    description: Optional[str] = None

class ButtonTypeDef(BaseValidatorModel):
    text: str
    value: str

class CloudWatchLogGroupLogDestinationTypeDef(BaseValidatorModel):
    cloudWatchLogGroupArn: str
    logPrefix: str

class LambdaCodeHookTypeDef(BaseValidatorModel):
    lambdaARN: str
    codeHookInterfaceVersion: str

class SubSlotTypeCompositionTypeDef(BaseValidatorModel):
    name: str
    slotTypeId: str

class ConditionTypeDef(BaseValidatorModel):
    expressionString: str

class ConversationLevelIntentClassificationResultItemTypeDef(BaseValidatorModel):
    intentName: str
    matchResult: TestResultMatchStatusType

class ConversationLevelResultDetailTypeDef(BaseValidatorModel):
    endToEndResult: TestResultMatchStatusType
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None

class ConversationLevelSlotResolutionResultItemTypeDef(BaseValidatorModel):
    intentName: str
    slotName: str
    matchResult: TestResultMatchStatusType

class ConversationLevelTestResultsFilterByTypeDef(BaseValidatorModel):
    endToEndResult: Optional[TestResultMatchStatusType] = None

class ConversationLogsDataSourceFilterByTypeDef(BaseValidatorModel):
    startTime: datetime
    endTime: datetime
    inputMode: ConversationLogsInputModeFilterType

class SentimentAnalysisSettingsTypeDef(BaseValidatorModel):
    detectSentiment: bool

class CreateBotReplicaRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str

class DialogCodeHookSettingsTypeDef(BaseValidatorModel):
    enabled: bool

class InputContextTypeDef(BaseValidatorModel):
    name: str

class KendraConfigurationTypeDef(BaseValidatorModel):
    kendraIndex: str
    queryFilterStringEnabled: Optional[bool] = None
    queryFilterString: Optional[str] = None

class OutputContextTypeDef(BaseValidatorModel):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int

class SampleUtteranceTypeDef(BaseValidatorModel):
    utterance: str

class CreateResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    policy: str

class PrincipalTypeDef(BaseValidatorModel):
    service: Optional[str] = None
    arn: Optional[str] = None

class MultipleValuesSettingTypeDef(BaseValidatorModel):
    allowMultipleValues: Optional[bool] = None

class ObfuscationSettingTypeDef(BaseValidatorModel):
    obfuscationSettingType: ObfuscationSettingTypeType

class CustomPayloadTypeDef(BaseValidatorModel):
    value: str

class CustomVocabularyExportSpecificationTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class CustomVocabularyImportSpecificationTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class QnAKendraConfigurationTypeDef(BaseValidatorModel):
    kendraIndex: str
    queryFilterStringEnabled: Optional[bool] = None
    queryFilterString: Optional[str] = None
    exactResponse: Optional[bool] = None

class DateRangeFilterTypeDef(BaseValidatorModel):
    startDateTime: datetime
    endDateTime: datetime

class DeleteBotAliasRequestRequestTypeDef(BaseValidatorModel):
    botAliasId: str
    botId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteBotLocaleRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class DeleteBotReplicaRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str

class DeleteBotRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteBotVersionRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteCustomVocabularyRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class DeleteExportRequestRequestTypeDef(BaseValidatorModel):
    exportId: str

class DeleteImportRequestRequestTypeDef(BaseValidatorModel):
    importId: str

class DeleteIntentRequestRequestTypeDef(BaseValidatorModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    expectedRevisionId: Optional[str] = None

class DeleteResourcePolicyStatementRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    statementId: str
    expectedRevisionId: Optional[str] = None

class DeleteSlotRequestRequestTypeDef(BaseValidatorModel):
    slotId: str
    botId: str
    botVersion: str
    localeId: str
    intentId: str

class DeleteSlotTypeRequestRequestTypeDef(BaseValidatorModel):
    slotTypeId: str
    botId: str
    botVersion: str
    localeId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteTestSetRequestRequestTypeDef(BaseValidatorModel):
    testSetId: str

class DeleteUtterancesRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    localeId: Optional[str] = None
    sessionId: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeBotAliasRequestRequestTypeDef(BaseValidatorModel):
    botAliasId: str
    botId: str

class ParentBotNetworkTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str

class DescribeBotLocaleRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class DescribeBotRecommendationRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str

class EncryptionSettingTypeDef(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None
    botLocaleExportPassword: Optional[str] = None
    associatedTranscriptsPassword: Optional[str] = None

class DescribeBotReplicaRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str

class DescribeBotRequestRequestTypeDef(BaseValidatorModel):
    botId: str

class DescribeBotResourceGenerationRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    generationId: str

class DescribeBotVersionRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str

class DescribeCustomVocabularyMetadataRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str

class DescribeExportRequestRequestTypeDef(BaseValidatorModel):
    exportId: str

class DescribeImportRequestRequestTypeDef(BaseValidatorModel):
    importId: str

class DescribeIntentRequestRequestTypeDef(BaseValidatorModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str

class SlotPriorityTypeDef(BaseValidatorModel):
    priority: int
    slotId: str

class DescribeResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class DescribeSlotRequestRequestTypeDef(BaseValidatorModel):
    slotId: str
    botId: str
    botVersion: str
    localeId: str
    intentId: str

class DescribeSlotTypeRequestRequestTypeDef(BaseValidatorModel):
    slotTypeId: str
    botId: str
    botVersion: str
    localeId: str

class DescribeTestExecutionRequestRequestTypeDef(BaseValidatorModel):
    testExecutionId: str

class DescribeTestSetDiscrepancyReportRequestRequestTypeDef(BaseValidatorModel):
    testSetDiscrepancyReportId: str

class DescribeTestSetGenerationRequestRequestTypeDef(BaseValidatorModel):
    testSetGenerationId: str

class TestSetStorageLocationTypeDef(BaseValidatorModel):
    s3BucketName: str
    s3Path: str
    kmsKeyArn: Optional[str] = None

class DescribeTestSetRequestRequestTypeDef(BaseValidatorModel):
    testSetId: str

class DialogActionTypeDef(BaseValidatorModel):
    type: DialogActionTypeType
    slotToElicit: Optional[str] = None
    suppressNextMessage: Optional[bool] = None

class IntentOverrideTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    slots: Optional[Mapping[str, "SlotValueOverrideTypeDef"]] = None

class ElicitationCodeHookInvocationSettingTypeDef(BaseValidatorModel):
    enableCodeHookInvocation: bool
    invocationLabel: Optional[str] = None

class ExactResponseFieldsTypeDef(BaseValidatorModel):
    questionField: str
    answerField: str

class ExportFilterTypeDef(BaseValidatorModel):
    name: Literal["ExportResourceType"]
    values: Sequence[str]
    operator: ExportFilterOperatorType

class TestSetExportSpecificationTypeDef(BaseValidatorModel):
    testSetId: str

class ExportSortByTypeDef(BaseValidatorModel):
    attribute: Literal["LastUpdatedDateTime"]
    order: SortOrderType

class GenerateBotElementRequestRequestTypeDef(BaseValidatorModel):
    intentId: str
    botId: str
    botVersion: str
    localeId: str

class GenerationSortByTypeDef(BaseValidatorModel):
    attribute: GenerationSortByAttributeType
    order: SortOrderType

class GenerationSummaryTypeDef(BaseValidatorModel):
    generationId: Optional[str] = None
    generationStatus: Optional[GenerationStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class GetTestExecutionArtifactsUrlRequestRequestTypeDef(BaseValidatorModel):
    testExecutionId: str

class GrammarSlotTypeSourceTypeDef(BaseValidatorModel):
    s3BucketName: str
    s3ObjectKey: str
    kmsKeyArn: Optional[str] = None

class ImportFilterTypeDef(BaseValidatorModel):
    name: Literal["ImportResourceType"]
    values: Sequence[str]
    operator: ImportFilterOperatorType

class ImportSortByTypeDef(BaseValidatorModel):
    attribute: Literal["LastUpdatedDateTime"]
    order: SortOrderType

class ImportSummaryTypeDef(BaseValidatorModel):
    importId: Optional[str] = None
    importedResourceId: Optional[str] = None
    importedResourceName: Optional[str] = None
    importStatus: Optional[ImportStatusType] = None
    mergeStrategy: Optional[MergeStrategyType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    importedResourceType: Optional[ImportResourceTypeType] = None

class RuntimeHintsTypeDef(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]]] = None

class IntentClassificationTestResultItemCountsTypeDef(BaseValidatorModel):
    totalResultCount: int
    intentMatchResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None

class IntentFilterTypeDef(BaseValidatorModel):
    name: Literal["IntentName"]
    values: Sequence[str]
    operator: IntentFilterOperatorType

class IntentSortByTypeDef(BaseValidatorModel):
    attribute: IntentSortAttributeType
    order: SortOrderType

class InvokedIntentSampleTypeDef(BaseValidatorModel):
    intentName: Optional[str] = None

class ListBotAliasReplicasRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotAliasesRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotReplicasRequestRequestTypeDef(BaseValidatorModel):
    botId: str

class ListCustomVocabularyItemsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRecommendedIntentsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RecommendedIntentSummaryTypeDef(BaseValidatorModel):
    intentId: Optional[str] = None
    intentName: Optional[str] = None
    sampleUtterancesCount: Optional[int] = None

class SessionDataSortByTypeDef(BaseValidatorModel):
    name: AnalyticsSessionSortByNameType
    order: AnalyticsSortOrderType

class SlotTypeFilterTypeDef(BaseValidatorModel):
    name: SlotTypeFilterNameType
    values: Sequence[str]
    operator: SlotTypeFilterOperatorType

class SlotTypeSortByTypeDef(BaseValidatorModel):
    attribute: SlotTypeSortAttributeType
    order: SortOrderType

class SlotTypeSummaryTypeDef(BaseValidatorModel):
    slotTypeId: Optional[str] = None
    slotTypeName: Optional[str] = None
    description: Optional[str] = None
    parentSlotTypeSignature: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None
    slotTypeCategory: Optional[SlotTypeCategoryType] = None

class SlotFilterTypeDef(BaseValidatorModel):
    name: Literal["SlotName"]
    values: Sequence[str]
    operator: SlotFilterOperatorType

class SlotSortByTypeDef(BaseValidatorModel):
    attribute: SlotSortAttributeType
    order: SortOrderType

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str

class TestExecutionSortByTypeDef(BaseValidatorModel):
    attribute: TestExecutionSortAttributeType
    order: SortOrderType

class ListTestSetRecordsRequestRequestTypeDef(BaseValidatorModel):
    testSetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TestSetSortByTypeDef(BaseValidatorModel):
    attribute: TestSetSortAttributeType
    order: SortOrderType

class UtteranceDataSortByTypeDef(BaseValidatorModel):
    name: Literal["UtteranceTimestamp"]
    order: AnalyticsSortOrderType

class PlainTextMessageTypeDef(BaseValidatorModel):
    value: str

class SSMLMessageTypeDef(BaseValidatorModel):
    value: str

class OverallTestResultItemTypeDef(BaseValidatorModel):
    multiTurnConversation: bool
    totalResultCount: int
    endToEndResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None

class PathFormatTypeDef(BaseValidatorModel):
    objectPrefixes: Optional[List[str]] = None

class TextInputSpecificationTypeDef(BaseValidatorModel):
    startTimeoutMs: int

class RelativeAggregationDurationTypeDef(BaseValidatorModel):
    timeDimension: TimeDimensionType
    timeValue: int

class RuntimeHintValueTypeDef(BaseValidatorModel):
    phrase: str

class SampleValueTypeDef(BaseValidatorModel):
    value: str

class SlotDefaultValueTypeDef(BaseValidatorModel):
    defaultValue: str

class SlotResolutionSettingTypeDef(BaseValidatorModel):
    slotResolutionStrategy: SlotResolutionStrategyType

class SlotResolutionTestResultItemCountsTypeDef(BaseValidatorModel):
    totalResultCount: int
    slotMatchResultCounts: Dict[TestResultMatchStatusType, int]
    speechTranscriptionResultCounts: Optional[Dict[TestResultMatchStatusType, int]] = None

class SlotValueTypeDef(BaseValidatorModel):
    interpretedValue: Optional[str] = None

class SlotValueRegexFilterTypeDef(BaseValidatorModel):
    pattern: str

class StartBotResourceGenerationRequestRequestTypeDef(BaseValidatorModel):
    generationInputPrompt: str
    botId: str
    botVersion: str
    localeId: str

class StopBotRecommendationRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Mapping[str, str]

class TestSetIntentDiscrepancyItemTypeDef(BaseValidatorModel):
    intentName: str
    errorMessage: str

class TestSetSlotDiscrepancyItemTypeDef(BaseValidatorModel):
    intentName: str
    slotName: str
    errorMessage: str

class TestSetDiscrepancyReportBotAliasTargetTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str

class TestSetImportInputLocationTypeDef(BaseValidatorModel):
    s3BucketName: str
    s3Path: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateExportRequestRequestTypeDef(BaseValidatorModel):
    exportId: str
    filePassword: Optional[str] = None

class UpdateResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    policy: str
    expectedRevisionId: Optional[str] = None

class UpdateTestSetRequestRequestTypeDef(BaseValidatorModel):
    testSetId: str
    testSetName: str
    description: Optional[str] = None

class UserTurnIntentOutputTypeDef(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, "UserTurnSlotOutputTypeDef"]] = None

class UserTurnSlotOutputTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None

class UtteranceAudioInputSpecificationTypeDef(BaseValidatorModel):
    audioFileS3Location: str

class AgentTurnResultTypeDef(BaseValidatorModel):
    expectedAgentPrompt: str
    actualAgentPrompt: Optional[str] = None
    errorDetails: Optional[ExecutionErrorDetailsTypeDef] = None
    actualElicitedSlot: Optional[str] = None
    actualIntent: Optional[str] = None

class AnalyticsIntentResultTypeDef(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsIntentGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsIntentMetricResultTypeDef]] = None

class AnalyticsIntentStageResultTypeDef(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsIntentStageGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsIntentStageMetricResultTypeDef]] = None

class AnalyticsSessionResultTypeDef(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsSessionGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsSessionMetricResultTypeDef]] = None

class AnalyticsUtteranceResultTypeDef(BaseValidatorModel):
    binKeys: Optional[List[AnalyticsBinKeyTypeDef]] = None
    groupByKeys: Optional[List[AnalyticsUtteranceGroupByKeyTypeDef]] = None
    metricsResults: Optional[List[AnalyticsUtteranceMetricResultTypeDef]] = None
    attributeResults: Optional[List[AnalyticsUtteranceAttributeResultTypeDef]] = None

class SearchAssociatedTranscriptsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    filters: Sequence[AssociatedTranscriptFilterTypeDef]
    searchOrder: Optional[SearchOrderType] = None
    maxResults: Optional[int] = None
    nextIndex: Optional[int] = None

class AudioAndDTMFInputSpecificationTypeDef(BaseValidatorModel):
    startTimeoutMs: int
    audioSpecification: Optional[AudioSpecificationTypeDef] = None
    dtmfSpecification: Optional[DTMFSpecificationTypeDef] = None

class AudioLogDestinationTypeDef(BaseValidatorModel):
    s3Bucket: S3BucketLogDestinationTypeDef

class BatchCreateCustomVocabularyItemRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: Sequence[NewCustomVocabularyItemTypeDef]

class BatchUpdateCustomVocabularyItemRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: Sequence[CustomVocabularyItemTypeDef]

class BatchCreateCustomVocabularyItemResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItemTypeDef]
    resources: List[CustomVocabularyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteCustomVocabularyItemResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItemTypeDef]
    resources: List[CustomVocabularyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateCustomVocabularyItemResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    errors: List[FailedCustomVocabularyItemTypeDef]
    resources: List[CustomVocabularyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BuildBotLocaleResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatusType
    lastBuildSubmittedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotReplicaResponseTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str
    sourceRegion: str
    creationDateTime: datetime
    botReplicaStatus: BotReplicaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourcePolicyStatementResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUploadUrlResponseTypeDef(BaseValidatorModel):
    importId: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotAliasResponseTypeDef(BaseValidatorModel):
    botAliasId: str
    botId: str
    botAliasStatus: BotAliasStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotLocaleResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotReplicaResponseTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str
    botReplicaStatus: BotReplicaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotResponseTypeDef(BaseValidatorModel):
    botId: str
    botStatus: BotStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBotVersionResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    botStatus: BotStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomVocabularyResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyStatus: CustomVocabularyStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExportResponseTypeDef(BaseValidatorModel):
    exportId: str
    exportStatus: ExportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImportResponseTypeDef(BaseValidatorModel):
    importId: str
    importStatus: ImportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyStatementResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotReplicaResponseTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str
    sourceRegion: str
    creationDateTime: datetime
    botReplicaStatus: BotReplicaStatusType
    failureReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBotResourceGenerationResponseTypeDef(BaseValidatorModel):
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

class DescribeCustomVocabularyMetadataResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyStatus: CustomVocabularyStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestExecutionArtifactsUrlResponseTypeDef(BaseValidatorModel):
    testExecutionId: str
    downloadArtifactsUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomVocabularyItemsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItems: List[CustomVocabularyItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIntentPathsResponseTypeDef(BaseValidatorModel):
    nodeSummaries: List[AnalyticsIntentNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAssociatedTranscriptsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    nextIndex: int
    associatedTranscripts: List[AssociatedTranscriptTypeDef]
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartBotResourceGenerationResponseTypeDef(BaseValidatorModel):
    generationInputPrompt: str
    generationId: str
    botId: str
    botVersion: str
    localeId: str
    generationStatus: GenerationStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopBotRecommendationResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteCustomVocabularyItemRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    customVocabularyItemList: Sequence[CustomVocabularyEntryIdTypeDef]

class DescriptiveBotBuilderSpecificationTypeDef(BaseValidatorModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecificationTypeDef] = None

class SampleUtteranceGenerationSpecificationTypeDef(BaseValidatorModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecificationTypeDef] = None

class SlotResolutionImprovementSpecificationTypeDef(BaseValidatorModel):
    enabled: bool
    bedrockModelSpecification: Optional[BedrockModelSpecificationTypeDef] = None

class ListBotAliasReplicasResponseTypeDef(BaseValidatorModel):
    botId: str
    sourceRegion: str
    replicaRegion: str
    botAliasReplicaSummaries: List[BotAliasReplicaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotAliasesResponseTypeDef(BaseValidatorModel):
    botAliasSummaries: List[BotAliasSummaryTypeDef]
    nextToken: str
    botId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestExecutionTargetTypeDef(BaseValidatorModel):
    botAliasTarget: Optional[BotAliasTestExecutionTargetTypeDef] = None

class BotImportSpecificationTypeDef(BaseValidatorModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: Optional[int] = None
    botTags: Optional[Dict[str, str]] = None
    testBotAliasTags: Optional[Dict[str, str]] = None

class BotLocaleImportSpecificationTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: Optional[float] = None
    voiceSettings: Optional[VoiceSettingsTypeDef] = None

class ListBotLocalesRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    sortBy: Optional[BotLocaleSortByTypeDef] = None
    filters: Optional[Sequence[BotLocaleFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotLocalesResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    nextToken: str
    botLocaleSummaries: List[BotLocaleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotRequestRequestTypeDef(BaseValidatorModel):
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    description: Optional[str] = None
    botTags: Optional[Mapping[str, str]] = None
    testBotAliasTags: Optional[Mapping[str, str]] = None
    botType: Optional[BotTypeType] = None
    botMembers: Optional[Sequence[BotMemberTypeDef]] = None

class CreateBotResponseTypeDef(BaseValidatorModel):
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

class DescribeBotResponseTypeDef(BaseValidatorModel):
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

class UpdateBotRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botName: str
    roleArn: str
    dataPrivacy: DataPrivacyTypeDef
    idleSessionTTLInSeconds: int
    description: Optional[str] = None
    botType: Optional[BotTypeType] = None
    botMembers: Optional[Sequence[BotMemberTypeDef]] = None

class UpdateBotResponseTypeDef(BaseValidatorModel):
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

class BotRecommendationResultStatisticsTypeDef(BaseValidatorModel):
    intents: Optional[IntentStatisticsTypeDef] = None
    slotTypes: Optional[SlotTypeStatisticsTypeDef] = None

class ListBotRecommendationsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationSummaries: List[BotRecommendationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotReplicasResponseTypeDef(BaseValidatorModel):
    botId: str
    sourceRegion: str
    botReplicaSummaries: List[BotReplicaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotsRequestRequestTypeDef(BaseValidatorModel):
    sortBy: Optional[BotSortByTypeDef] = None
    filters: Optional[Sequence[BotFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotsResponseTypeDef(BaseValidatorModel):
    botSummaries: List[BotSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotVersionRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersionLocaleSpecification: Mapping[str, BotVersionLocaleDetailsTypeDef]
    description: Optional[str] = None

class CreateBotVersionResponseTypeDef(BaseValidatorModel):
    botId: str
    description: str
    botVersion: str
    botVersionLocaleSpecification: Dict[str, BotVersionLocaleDetailsTypeDef]
    botStatus: BotStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotVersionReplicasRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    replicaRegion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[BotVersionReplicaSortByTypeDef] = None

class ListBotVersionReplicasResponseTypeDef(BaseValidatorModel):
    botId: str
    sourceRegion: str
    replicaRegion: str
    botVersionReplicaSummaries: List[BotVersionReplicaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotVersionsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    sortBy: Optional[BotVersionSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotVersionsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersionSummaries: List[BotVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuiltInIntentsRequestRequestTypeDef(BaseValidatorModel):
    localeId: str
    sortBy: Optional[BuiltInIntentSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBuiltInIntentsResponseTypeDef(BaseValidatorModel):
    builtInIntentSummaries: List[BuiltInIntentSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuiltInSlotTypesRequestRequestTypeDef(BaseValidatorModel):
    localeId: str
    sortBy: Optional[BuiltInSlotTypeSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBuiltInSlotTypesResponseTypeDef(BaseValidatorModel):
    builtInSlotTypeSummaries: List[BuiltInSlotTypeSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageResponseCardTypeDef(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[Sequence[ButtonTypeDef]] = None

class TextLogDestinationTypeDef(BaseValidatorModel):
    cloudWatch: CloudWatchLogGroupLogDestinationTypeDef

class CodeHookSpecificationTypeDef(BaseValidatorModel):
    lambdaCodeHook: LambdaCodeHookTypeDef

class CompositeSlotTypeSettingTypeDef(BaseValidatorModel):
    subSlots: Optional[Sequence[SubSlotTypeCompositionTypeDef]] = None

class ConversationLevelTestResultItemTypeDef(BaseValidatorModel):
    conversationId: str
    endToEndResult: TestResultMatchStatusType
    intentClassificationResults: List[ConversationLevelIntentClassificationResultItemTypeDef]
    slotResolutionResults: List[ConversationLevelSlotResolutionResultItemTypeDef]
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None

class TestExecutionResultFilterByTypeDef(BaseValidatorModel):
    resultTypeFilter: TestResultTypeFilterType
    conversationLevelTestResultsFilterBy: Optional[       ConversationLevelTestResultsFilterByTypeDef     ] = None

class ConversationLogsDataSourceTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    filter: ConversationLogsDataSourceFilterByTypeDef

class IntentSummaryTypeDef(BaseValidatorModel):
    intentId: Optional[str] = None
    intentName: Optional[str] = None
    description: Optional[str] = None
    parentIntentSignature: Optional[str] = None
    inputContexts: Optional[List[InputContextTypeDef]] = None
    outputContexts: Optional[List[OutputContextTypeDef]] = None
    lastUpdatedDateTime: Optional[datetime] = None

class GenerateBotElementResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    sampleUtterances: List[SampleUtteranceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourcePolicyStatementRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    statementId: str
    effect: EffectType
    principal: Sequence[PrincipalTypeDef]
    action: Sequence[str]
    condition: Optional[Mapping[str, Mapping[str, str]]] = None
    expectedRevisionId: Optional[str] = None

class LexTranscriptFilterTypeDef(BaseValidatorModel):
    dateRangeFilter: Optional[DateRangeFilterTypeDef] = None

class DescribeBotAliasRequestBotAliasAvailableWaitTypeDef(BaseValidatorModel):
    botAliasId: str
    botId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotRequestBotAvailableWaitTypeDef(BaseValidatorModel):
    botId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotVersionRequestBotVersionAvailableWaitTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeExportRequestBotExportCompletedWaitTypeDef(BaseValidatorModel):
    exportId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImportRequestBotImportCompletedWaitTypeDef(BaseValidatorModel):
    importId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeBotVersionResponseTypeDef(BaseValidatorModel):
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

class UpdateBotRecommendationRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    encryptionSetting: EncryptionSettingTypeDef

class DescribeTestSetResponseTypeDef(BaseValidatorModel):
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

class TestSetSummaryTypeDef(BaseValidatorModel):
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

class UpdateTestSetResponseTypeDef(BaseValidatorModel):
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

class DialogStateTypeDef(BaseValidatorModel):
    dialogAction: Optional[DialogActionTypeDef] = None
    intent: Optional[IntentOverrideTypeDef] = None
    sessionAttributes: Optional[Mapping[str, str]] = None

class OpensearchConfigurationTypeDef(BaseValidatorModel):
    domainEndpoint: str
    indexName: str
    exactResponse: Optional[bool] = None
    exactResponseFields: Optional[ExactResponseFieldsTypeDef] = None
    includeFields: Optional[Sequence[str]] = None

class ExportResourceSpecificationTypeDef(BaseValidatorModel):
    botExportSpecification: Optional[BotExportSpecificationTypeDef] = None
    botLocaleExportSpecification: Optional[BotLocaleExportSpecificationTypeDef] = None
    customVocabularyExportSpecification: Optional[       CustomVocabularyExportSpecificationTypeDef     ] = None
    testSetExportSpecification: Optional[TestSetExportSpecificationTypeDef] = None

class ListExportsRequestRequestTypeDef(BaseValidatorModel):
    botId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[ExportSortByTypeDef] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    localeId: Optional[str] = None

class ListBotResourceGenerationsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[GenerationSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListBotResourceGenerationsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    generationSummaries: List[GenerationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GrammarSlotTypeSettingTypeDef(BaseValidatorModel):
    source: Optional[GrammarSlotTypeSourceTypeDef] = None

class ListImportsRequestRequestTypeDef(BaseValidatorModel):
    botId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[ImportSortByTypeDef] = None
    filters: Optional[Sequence[ImportFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    localeId: Optional[str] = None

class ListImportsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    importSummaries: List[ImportSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class InputSessionStateSpecificationTypeDef(BaseValidatorModel):
    sessionAttributes: Optional[Dict[str, str]] = None
    activeContexts: Optional[List[ActiveContextTypeDef]] = None
    runtimeHints: Optional[RuntimeHintsTypeDef] = None

class IntentClassificationTestResultItemTypeDef(BaseValidatorModel):
    intentName: str
    multiTurnConversation: bool
    resultCounts: IntentClassificationTestResultItemCountsTypeDef

class ListIntentsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[IntentSortByTypeDef] = None
    filters: Optional[Sequence[IntentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SessionSpecificationTypeDef(BaseValidatorModel):
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

class ListIntentMetricsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsIntentMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsIntentGroupBySpecificationTypeDef]] = None
    filters: Optional[Sequence[AnalyticsIntentFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIntentPathsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    intentPath: str
    filters: Optional[Sequence[AnalyticsPathFilterTypeDef]] = None

class ListIntentStageMetricsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsIntentStageMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsIntentStageGroupBySpecificationTypeDef]] = None
    filters: Optional[Sequence[AnalyticsIntentStageFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSessionMetricsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    metrics: Sequence[AnalyticsSessionMetricTypeDef]
    binBy: Optional[Sequence[AnalyticsBinBySpecificationTypeDef]] = None
    groupBy: Optional[Sequence[AnalyticsSessionGroupBySpecificationTypeDef]] = None
    filters: Optional[Sequence[AnalyticsSessionFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListUtteranceMetricsRequestRequestTypeDef(BaseValidatorModel):
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

class ListRecommendedIntentsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationId: str
    summaryList: List[RecommendedIntentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionAnalyticsDataRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    sortBy: Optional[SessionDataSortByTypeDef] = None
    filters: Optional[Sequence[AnalyticsSessionFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSlotTypesRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    sortBy: Optional[SlotTypeSortByTypeDef] = None
    filters: Optional[Sequence[SlotTypeFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSlotTypesResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    slotTypeSummaries: List[SlotTypeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSlotsRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    sortBy: Optional[SlotSortByTypeDef] = None
    filters: Optional[Sequence[SlotFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTestExecutionsRequestRequestTypeDef(BaseValidatorModel):
    sortBy: Optional[TestExecutionSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTestSetsRequestRequestTypeDef(BaseValidatorModel):
    sortBy: Optional[TestSetSortByTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListUtteranceAnalyticsDataRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    startDateTime: TimestampTypeDef
    endDateTime: TimestampTypeDef
    sortBy: Optional[UtteranceDataSortByTypeDef] = None
    filters: Optional[Sequence[AnalyticsUtteranceFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class OverallTestResultsTypeDef(BaseValidatorModel):
    items: List[OverallTestResultItemTypeDef]

class UtteranceAggregationDurationTypeDef(BaseValidatorModel):
    relativeAggregationDuration: RelativeAggregationDurationTypeDef

class RuntimeHintDetailsTypeDef(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValueTypeDef]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None

class SlotTypeValueTypeDef(BaseValidatorModel):
    sampleValue: Optional[SampleValueTypeDef] = None
    synonyms: Optional[Sequence[SampleValueTypeDef]] = None

class SlotDefaultValueSpecificationTypeDef(BaseValidatorModel):
    defaultValueList: Sequence[SlotDefaultValueTypeDef]

class SlotResolutionTestResultItemTypeDef(BaseValidatorModel):
    slotName: str
    resultCounts: SlotResolutionTestResultItemCountsTypeDef

class SlotValueOverrideTypeDef(BaseValidatorModel):
    shape: Optional[SlotShapeType] = None
    value: Optional[SlotValueTypeDef] = None
    values: Optional[Sequence[Dict[str, Any]]] = None

class SlotValueSelectionSettingTypeDef(BaseValidatorModel):
    resolutionStrategy: SlotValueResolutionStrategyType
    regexFilter: Optional[SlotValueRegexFilterTypeDef] = None
    advancedRecognitionSetting: Optional[AdvancedRecognitionSettingTypeDef] = None

class TestSetDiscrepancyErrorsTypeDef(BaseValidatorModel):
    intentDiscrepancies: List[TestSetIntentDiscrepancyItemTypeDef]
    slotDiscrepancies: List[TestSetSlotDiscrepancyItemTypeDef]

class TestSetDiscrepancyReportResourceTargetTypeDef(BaseValidatorModel):
    botAliasTarget: Optional[TestSetDiscrepancyReportBotAliasTargetTypeDef] = None

class TestSetImportResourceSpecificationTypeDef(BaseValidatorModel):
    testSetName: str
    roleArn: str
    storageLocation: TestSetStorageLocationTypeDef
    importInputLocation: TestSetImportInputLocationTypeDef
    modality: TestSetModalityType
    description: Optional[str] = None
    testSetTags: Optional[Dict[str, str]] = None

class UserTurnOutputSpecificationTypeDef(BaseValidatorModel):
    intent: UserTurnIntentOutputTypeDef
    activeContexts: Optional[List[ActiveContextTypeDef]] = None
    transcript: Optional[str] = None

class UtteranceInputSpecificationTypeDef(BaseValidatorModel):
    textInput: Optional[str] = None
    audioInput: Optional[UtteranceAudioInputSpecificationTypeDef] = None

class ListIntentMetricsResponseTypeDef(BaseValidatorModel):
    botId: str
    results: List[AnalyticsIntentResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIntentStageMetricsResponseTypeDef(BaseValidatorModel):
    botId: str
    results: List[AnalyticsIntentStageResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionMetricsResponseTypeDef(BaseValidatorModel):
    botId: str
    results: List[AnalyticsSessionResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUtteranceMetricsResponseTypeDef(BaseValidatorModel):
    botId: str
    results: List[AnalyticsUtteranceResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PromptAttemptSpecificationTypeDef(BaseValidatorModel):
    allowedInputTypes: AllowedInputTypesTypeDef
    allowInterrupt: Optional[bool] = None
    audioAndDTMFInputSpecification: Optional[AudioAndDTMFInputSpecificationTypeDef] = None
    textInputSpecification: Optional[TextInputSpecificationTypeDef] = None

class AudioLogSettingTypeDef(BaseValidatorModel):
    enabled: bool
    destination: AudioLogDestinationTypeDef
    selectiveLoggingEnabled: Optional[bool] = None

class BuildtimeSettingsTypeDef(BaseValidatorModel):
    descriptiveBotBuilder: Optional[DescriptiveBotBuilderSpecificationTypeDef] = None
    sampleUtteranceGeneration: Optional[SampleUtteranceGenerationSpecificationTypeDef] = None

class RuntimeSettingsTypeDef(BaseValidatorModel):
    slotResolutionImprovement: Optional[SlotResolutionImprovementSpecificationTypeDef] = None

class DescribeTestExecutionResponseTypeDef(BaseValidatorModel):
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

class StartTestExecutionRequestRequestTypeDef(BaseValidatorModel):
    testSetId: str
    target: TestExecutionTargetTypeDef
    apiMode: TestExecutionApiModeType
    testExecutionModality: Optional[TestExecutionModalityType] = None

class StartTestExecutionResponseTypeDef(BaseValidatorModel):
    testExecutionId: str
    creationDateTime: datetime
    testSetId: str
    target: TestExecutionTargetTypeDef
    apiMode: TestExecutionApiModeType
    testExecutionModality: TestExecutionModalityType
    ResponseMetadata: ResponseMetadataTypeDef

class TestExecutionSummaryTypeDef(BaseValidatorModel):
    testExecutionId: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    testExecutionStatus: Optional[TestExecutionStatusType] = None
    testSetId: Optional[str] = None
    testSetName: Optional[str] = None
    target: Optional[TestExecutionTargetTypeDef] = None
    apiMode: Optional[TestExecutionApiModeType] = None
    testExecutionModality: Optional[TestExecutionModalityType] = None

class BotRecommendationResultsTypeDef(BaseValidatorModel):
    botLocaleExportUrl: Optional[str] = None
    associatedTranscriptsUrl: Optional[str] = None
    statistics: Optional[BotRecommendationResultStatisticsTypeDef] = None

class MessageTypeDef(BaseValidatorModel):
    plainTextMessage: Optional[PlainTextMessageTypeDef] = None
    customPayload: Optional[CustomPayloadTypeDef] = None
    ssmlMessage: Optional[SSMLMessageTypeDef] = None
    imageResponseCard: Optional[ImageResponseCardTypeDef] = None

class UtteranceBotResponseTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    contentType: Optional[UtteranceContentTypeType] = None
    imageResponseCard: Optional[ImageResponseCardTypeDef] = None

class TextLogSettingTypeDef(BaseValidatorModel):
    enabled: bool
    destination: TextLogDestinationTypeDef
    selectiveLoggingEnabled: Optional[bool] = None

class BotAliasLocaleSettingsTypeDef(BaseValidatorModel):
    enabled: bool
    codeHookSpecification: Optional[CodeHookSpecificationTypeDef] = None

class ConversationLevelTestResultsTypeDef(BaseValidatorModel):
    items: List[ConversationLevelTestResultItemTypeDef]

class ListTestExecutionResultItemsRequestRequestTypeDef(BaseValidatorModel):
    testExecutionId: str
    resultFilterBy: TestExecutionResultFilterByTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TestSetGenerationDataSourceTypeDef(BaseValidatorModel):
    conversationLogsDataSource: Optional[ConversationLogsDataSourceTypeDef] = None

class ListIntentsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentSummaries: List[IntentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TranscriptFilterTypeDef(BaseValidatorModel):
    lexTranscriptFilter: Optional[LexTranscriptFilterTypeDef] = None

class ListTestSetsResponseTypeDef(BaseValidatorModel):
    testSets: List[TestSetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationTypeDef(BaseValidatorModel):
    opensearchConfiguration: Optional[OpensearchConfigurationTypeDef] = None
    kendraConfiguration: Optional[QnAKendraConfigurationTypeDef] = None
    bedrockKnowledgeStoreConfiguration: Optional[       BedrockKnowledgeStoreConfigurationTypeDef     ] = None

class CreateExportRequestRequestTypeDef(BaseValidatorModel):
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    filePassword: Optional[str] = None

class CreateExportResponseTypeDef(BaseValidatorModel):
    exportId: str
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportResponseTypeDef(BaseValidatorModel):
    exportId: str
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    failureReasons: List[str]
    downloadUrl: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSummaryTypeDef(BaseValidatorModel):
    exportId: Optional[str] = None
    resourceSpecification: Optional[ExportResourceSpecificationTypeDef] = None
    fileFormat: Optional[ImportExportFileFormatType] = None
    exportStatus: Optional[ExportStatusType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class UpdateExportResponseTypeDef(BaseValidatorModel):
    exportId: str
    resourceSpecification: ExportResourceSpecificationTypeDef
    fileFormat: ImportExportFileFormatType
    exportStatus: ExportStatusType
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ExternalSourceSettingTypeDef(BaseValidatorModel):
    grammarSlotTypeSetting: Optional[GrammarSlotTypeSettingTypeDef] = None

class IntentClassificationTestResultsTypeDef(BaseValidatorModel):
    items: List[IntentClassificationTestResultItemTypeDef]

class ListSessionAnalyticsDataResponseTypeDef(BaseValidatorModel):
    botId: str
    nextToken: str
    sessions: List[SessionSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregatedUtterancesRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    localeId: str
    aggregationDuration: UtteranceAggregationDurationTypeDef
    botAliasId: Optional[str] = None
    botVersion: Optional[str] = None
    sortBy: Optional[AggregatedUtterancesSortByTypeDef] = None
    filters: Optional[Sequence[AggregatedUtterancesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAggregatedUtterancesResponseTypeDef(BaseValidatorModel):
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

class IntentLevelSlotResolutionTestResultItemTypeDef(BaseValidatorModel):
    intentName: str
    multiTurnConversation: bool
    slotResolutionResults: List[SlotResolutionTestResultItemTypeDef]

class CreateTestSetDiscrepancyReportRequestRequestTypeDef(BaseValidatorModel):
    testSetId: str
    target: TestSetDiscrepancyReportResourceTargetTypeDef

class CreateTestSetDiscrepancyReportResponseTypeDef(BaseValidatorModel):
    testSetDiscrepancyReportId: str
    creationDateTime: datetime
    testSetId: str
    target: TestSetDiscrepancyReportResourceTargetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTestSetDiscrepancyReportResponseTypeDef(BaseValidatorModel):
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

class ImportResourceSpecificationTypeDef(BaseValidatorModel):
    botImportSpecification: Optional[BotImportSpecificationTypeDef] = None
    botLocaleImportSpecification: Optional[BotLocaleImportSpecificationTypeDef] = None
    customVocabularyImportSpecification: Optional[       CustomVocabularyImportSpecificationTypeDef     ] = None
    testSetImportResourceSpecification: Optional[       TestSetImportResourceSpecificationTypeDef     ] = None

class UserTurnInputSpecificationTypeDef(BaseValidatorModel):
    utteranceInput: UtteranceInputSpecificationTypeDef
    requestAttributes: Optional[Dict[str, str]] = None
    sessionState: Optional[InputSessionStateSpecificationTypeDef] = None

class GenerativeAISettingsTypeDef(BaseValidatorModel):
    runtimeSettings: Optional[RuntimeSettingsTypeDef] = None
    buildtimeSettings: Optional[BuildtimeSettingsTypeDef] = None

class ListTestExecutionsResponseTypeDef(BaseValidatorModel):
    testExecutions: List[TestExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageGroupTypeDef(BaseValidatorModel):
    message: MessageTypeDef
    variations: Optional[Sequence[MessageTypeDef]] = None

class UtteranceSpecificationTypeDef(BaseValidatorModel):
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

class ConversationLogSettingsTypeDef(BaseValidatorModel):
    textLogSettings: Optional[Sequence[TextLogSettingTypeDef]] = None
    audioLogSettings: Optional[Sequence[AudioLogSettingTypeDef]] = None

class DescribeTestSetGenerationResponseTypeDef(BaseValidatorModel):
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

class StartTestSetGenerationRequestRequestTypeDef(BaseValidatorModel):
    testSetName: str
    storageLocation: TestSetStorageLocationTypeDef
    generationDataSource: TestSetGenerationDataSourceTypeDef
    roleArn: str
    description: Optional[str] = None
    testSetTags: Optional[Mapping[str, str]] = None

class StartTestSetGenerationResponseTypeDef(BaseValidatorModel):
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

class S3BucketTranscriptSourceTypeDef(BaseValidatorModel):
    s3BucketName: str
    transcriptFormat: Literal["Lex"]
    pathFormat: Optional[PathFormatTypeDef] = None
    transcriptFilter: Optional[TranscriptFilterTypeDef] = None
    kmsKeyArn: Optional[str] = None

class QnAIntentConfigurationTypeDef(BaseValidatorModel):
    dataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None
    bedrockModelConfiguration: Optional[BedrockModelSpecificationTypeDef] = None

class ListExportsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    exportSummaries: List[ExportSummaryTypeDef]
    nextToken: str
    localeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSlotTypeRequestRequestTypeDef(BaseValidatorModel):
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

class CreateSlotTypeResponseTypeDef(BaseValidatorModel):
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

class DescribeSlotTypeResponseTypeDef(BaseValidatorModel):
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

class UpdateSlotTypeRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSlotTypeResponseTypeDef(BaseValidatorModel):
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

class IntentLevelSlotResolutionTestResultsTypeDef(BaseValidatorModel):
    items: List[IntentLevelSlotResolutionTestResultItemTypeDef]

class DescribeImportResponseTypeDef(BaseValidatorModel):
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

class StartImportRequestRequestTypeDef(BaseValidatorModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationTypeDef
    mergeStrategy: MergeStrategyType
    filePassword: Optional[str] = None

class StartImportResponseTypeDef(BaseValidatorModel):
    importId: str
    resourceSpecification: ImportResourceSpecificationTypeDef
    mergeStrategy: MergeStrategyType
    importStatus: ImportStatusType
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UserTurnResultTypeDef(BaseValidatorModel):
    input: UserTurnInputSpecificationTypeDef
    expectedOutput: UserTurnOutputSpecificationTypeDef
    actualOutput: Optional[UserTurnOutputSpecificationTypeDef] = None
    errorDetails: Optional[ExecutionErrorDetailsTypeDef] = None
    endToEndResult: Optional[TestResultMatchStatusType] = None
    intentMatchResult: Optional[TestResultMatchStatusType] = None
    slotMatchResult: Optional[TestResultMatchStatusType] = None
    speechTranscriptionResult: Optional[TestResultMatchStatusType] = None
    conversationLevelResult: Optional[ConversationLevelResultDetailTypeDef] = None

class UserTurnSpecificationTypeDef(BaseValidatorModel):
    input: UserTurnInputSpecificationTypeDef
    expected: UserTurnOutputSpecificationTypeDef

class CreateBotLocaleRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: float
    description: Optional[str] = None
    voiceSettings: Optional[VoiceSettingsTypeDef] = None
    generativeAISettings: Optional[GenerativeAISettingsTypeDef] = None

class CreateBotLocaleResponseTypeDef(BaseValidatorModel):
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

class DescribeBotLocaleResponseTypeDef(BaseValidatorModel):
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

class UpdateBotLocaleRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    nluIntentConfidenceThreshold: float
    description: Optional[str] = None
    voiceSettings: Optional[VoiceSettingsTypeDef] = None
    generativeAISettings: Optional[GenerativeAISettingsTypeDef] = None

class UpdateBotLocaleResponseTypeDef(BaseValidatorModel):
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

class FulfillmentStartResponseSpecificationTypeDef(BaseValidatorModel):
    delayInSeconds: int
    messageGroups: Sequence[MessageGroupTypeDef]
    allowInterrupt: Optional[bool] = None

class FulfillmentUpdateResponseSpecificationTypeDef(BaseValidatorModel):
    frequencyInSeconds: int
    messageGroups: Sequence[MessageGroupTypeDef]
    allowInterrupt: Optional[bool] = None

class PromptSpecificationTypeDef(BaseValidatorModel):
    messageGroups: Sequence[MessageGroupTypeDef]
    maxRetries: int
    allowInterrupt: Optional[bool] = None
    messageSelectionStrategy: Optional[MessageSelectionStrategyType] = None
    promptAttemptsSpecification: Optional[       Mapping[PromptAttemptType, PromptAttemptSpecificationTypeDef] = None

class ResponseSpecificationTypeDef(BaseValidatorModel):
    messageGroups: Sequence[MessageGroupTypeDef]
    allowInterrupt: Optional[bool] = None

class StillWaitingResponseSpecificationTypeDef(BaseValidatorModel):
    messageGroups: Sequence[MessageGroupTypeDef]
    frequencyInSeconds: int
    timeoutInSeconds: int
    allowInterrupt: Optional[bool] = None

class ListUtteranceAnalyticsDataResponseTypeDef(BaseValidatorModel):
    botId: str
    nextToken: str
    utterances: List[UtteranceSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotAliasRequestRequestTypeDef(BaseValidatorModel):
    botAliasName: str
    botId: str
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasLocaleSettings: Optional[Mapping[str, BotAliasLocaleSettingsTypeDef]] = None
    conversationLogSettings: Optional[ConversationLogSettingsTypeDef] = None
    sentimentAnalysisSettings: Optional[SentimentAnalysisSettingsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateBotAliasResponseTypeDef(BaseValidatorModel):
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

class DescribeBotAliasResponseTypeDef(BaseValidatorModel):
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

class UpdateBotAliasRequestRequestTypeDef(BaseValidatorModel):
    botAliasId: str
    botAliasName: str
    botId: str
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botAliasLocaleSettings: Optional[Mapping[str, BotAliasLocaleSettingsTypeDef]] = None
    conversationLogSettings: Optional[ConversationLogSettingsTypeDef] = None
    sentimentAnalysisSettings: Optional[SentimentAnalysisSettingsTypeDef] = None

class UpdateBotAliasResponseTypeDef(BaseValidatorModel):
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

class TranscriptSourceSettingTypeDef(BaseValidatorModel):
    s3BucketTranscriptSource: Optional[S3BucketTranscriptSourceTypeDef] = None

class TestSetTurnResultTypeDef(BaseValidatorModel):
    agent: Optional[AgentTurnResultTypeDef] = None
    user: Optional[UserTurnResultTypeDef] = None

class TurnSpecificationTypeDef(BaseValidatorModel):
    agentTurn: Optional[AgentTurnSpecificationTypeDef] = None
    userTurn: Optional[UserTurnSpecificationTypeDef] = None

class FulfillmentUpdatesSpecificationTypeDef(BaseValidatorModel):
    active: bool
    startResponse: Optional[FulfillmentStartResponseSpecificationTypeDef] = None
    updateResponse: Optional[FulfillmentUpdateResponseSpecificationTypeDef] = None
    timeoutInSeconds: Optional[int] = None

class SlotSummaryTypeDef(BaseValidatorModel):
    slotId: Optional[str] = None
    slotName: Optional[str] = None
    description: Optional[str] = None
    slotConstraint: Optional[SlotConstraintType] = None
    slotTypeId: Optional[str] = None
    valueElicitationPromptSpecification: Optional[PromptSpecificationTypeDef] = None
    lastUpdatedDateTime: Optional[datetime] = None

class ConditionalBranchTypeDef(BaseValidatorModel):
    name: str
    condition: ConditionTypeDef
    nextStep: DialogStateTypeDef
    response: Optional[ResponseSpecificationTypeDef] = None

class DefaultConditionalBranchTypeDef(BaseValidatorModel):
    nextStep: Optional[DialogStateTypeDef] = None
    response: Optional[ResponseSpecificationTypeDef] = None

class WaitAndContinueSpecificationTypeDef(BaseValidatorModel):
    waitingResponse: ResponseSpecificationTypeDef
    continueResponse: ResponseSpecificationTypeDef
    stillWaitingResponse: Optional[StillWaitingResponseSpecificationTypeDef] = None
    active: Optional[bool] = None

class DescribeBotRecommendationResponseTypeDef(BaseValidatorModel):
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

class StartBotRecommendationRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    transcriptSourceSetting: TranscriptSourceSettingTypeDef
    encryptionSetting: Optional[EncryptionSettingTypeDef] = None

class StartBotRecommendationResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    botRecommendationStatus: BotRecommendationStatusType
    botRecommendationId: str
    creationDateTime: datetime
    transcriptSourceSetting: TranscriptSourceSettingTypeDef
    encryptionSetting: EncryptionSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotRecommendationResponseTypeDef(BaseValidatorModel):
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

class UtteranceLevelTestResultItemTypeDef(BaseValidatorModel):
    recordNumber: int
    turnResult: TestSetTurnResultTypeDef
    conversationId: Optional[str] = None

class TestSetTurnRecordTypeDef(BaseValidatorModel):
    recordNumber: int
    turnSpecification: TurnSpecificationTypeDef
    conversationId: Optional[str] = None
    turnNumber: Optional[int] = None

class ListSlotsResponseTypeDef(BaseValidatorModel):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    slotSummaries: List[SlotSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConditionalSpecificationTypeDef(BaseValidatorModel):
    active: bool
    conditionalBranches: Sequence[ConditionalBranchTypeDef]
    defaultBranch: DefaultConditionalBranchTypeDef

class SubSlotValueElicitationSettingTypeDef(BaseValidatorModel):
    promptSpecification: PromptSpecificationTypeDef
    defaultValueSpecification: Optional[SlotDefaultValueSpecificationTypeDef] = None
    sampleUtterances: Optional[Sequence[SampleUtteranceTypeDef]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecificationTypeDef] = None

class UtteranceLevelTestResultsTypeDef(BaseValidatorModel):
    items: List[UtteranceLevelTestResultItemTypeDef]

class ListTestSetRecordsResponseTypeDef(BaseValidatorModel):
    testSetRecords: List[TestSetTurnRecordTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IntentClosingSettingTypeDef(BaseValidatorModel):
    closingResponse: Optional[ResponseSpecificationTypeDef] = None
    active: Optional[bool] = None
    nextStep: Optional[DialogStateTypeDef] = None
    conditional: Optional[ConditionalSpecificationTypeDef] = None

class PostDialogCodeHookInvocationSpecificationTypeDef(BaseValidatorModel):
    successResponse: Optional[ResponseSpecificationTypeDef] = None
    successNextStep: Optional[DialogStateTypeDef] = None
    successConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    timeoutResponse: Optional[ResponseSpecificationTypeDef] = None
    timeoutNextStep: Optional[DialogStateTypeDef] = None
    timeoutConditional: Optional[ConditionalSpecificationTypeDef] = None

class PostFulfillmentStatusSpecificationTypeDef(BaseValidatorModel):
    successResponse: Optional[ResponseSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    timeoutResponse: Optional[ResponseSpecificationTypeDef] = None
    successNextStep: Optional[DialogStateTypeDef] = None
    successConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    timeoutNextStep: Optional[DialogStateTypeDef] = None
    timeoutConditional: Optional[ConditionalSpecificationTypeDef] = None

class SpecificationsTypeDef(BaseValidatorModel):
    slotTypeId: str
    valueElicitationSetting: SubSlotValueElicitationSettingTypeDef

class TestExecutionResultItemsTypeDef(BaseValidatorModel):
    overallTestResults: Optional[OverallTestResultsTypeDef] = None
    conversationLevelTestResults: Optional[ConversationLevelTestResultsTypeDef] = None
    intentClassificationTestResults: Optional[IntentClassificationTestResultsTypeDef] = None
    intentLevelSlotResolutionTestResults: Optional[       IntentLevelSlotResolutionTestResultsTypeDef     ] = None
    utteranceLevelTestResults: Optional[UtteranceLevelTestResultsTypeDef] = None

class DialogCodeHookInvocationSettingTypeDef(BaseValidatorModel):
    enableCodeHookInvocation: bool
    active: bool
    postCodeHookSpecification: PostDialogCodeHookInvocationSpecificationTypeDef
    invocationLabel: Optional[str] = None

class FulfillmentCodeHookSettingsTypeDef(BaseValidatorModel):
    enabled: bool
    postFulfillmentStatusSpecification: Optional[       PostFulfillmentStatusSpecificationTypeDef     ] = None
    fulfillmentUpdatesSpecification: Optional[FulfillmentUpdatesSpecificationTypeDef] = None
    active: Optional[bool] = None

class SubSlotSettingTypeDef(BaseValidatorModel):
    expression: Optional[str] = None
    slotSpecifications: Optional[Mapping[str, SpecificationsTypeDef]] = None

class ListTestExecutionResultItemsResponseTypeDef(BaseValidatorModel):
    testExecutionResults: TestExecutionResultItemsTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitialResponseSettingTypeDef(BaseValidatorModel):
    initialResponse: Optional[ResponseSpecificationTypeDef] = None
    nextStep: Optional[DialogStateTypeDef] = None
    conditional: Optional[ConditionalSpecificationTypeDef] = None
    codeHook: Optional[DialogCodeHookInvocationSettingTypeDef] = None

class IntentConfirmationSettingTypeDef(BaseValidatorModel):
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

class SlotCaptureSettingTypeDef(BaseValidatorModel):
    captureResponse: Optional[ResponseSpecificationTypeDef] = None
    captureNextStep: Optional[DialogStateTypeDef] = None
    captureConditional: Optional[ConditionalSpecificationTypeDef] = None
    failureResponse: Optional[ResponseSpecificationTypeDef] = None
    failureNextStep: Optional[DialogStateTypeDef] = None
    failureConditional: Optional[ConditionalSpecificationTypeDef] = None
    codeHook: Optional[DialogCodeHookInvocationSettingTypeDef] = None
    elicitationCodeHook: Optional[ElicitationCodeHookInvocationSettingTypeDef] = None

class CreateIntentRequestRequestTypeDef(BaseValidatorModel):
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

class CreateIntentResponseTypeDef(BaseValidatorModel):
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

class DescribeIntentResponseTypeDef(BaseValidatorModel):
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

class UpdateIntentRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateIntentResponseTypeDef(BaseValidatorModel):
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

class SlotValueElicitationSettingTypeDef(BaseValidatorModel):
    slotConstraint: SlotConstraintType
    defaultValueSpecification: Optional[SlotDefaultValueSpecificationTypeDef] = None
    promptSpecification: Optional[PromptSpecificationTypeDef] = None
    sampleUtterances: Optional[Sequence[SampleUtteranceTypeDef]] = None
    waitAndContinueSpecification: Optional[WaitAndContinueSpecificationTypeDef] = None
    slotCaptureSetting: Optional[SlotCaptureSettingTypeDef] = None
    slotResolutionSetting: Optional[SlotResolutionSettingTypeDef] = None

class CreateSlotRequestRequestTypeDef(BaseValidatorModel):
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

class CreateSlotResponseTypeDef(BaseValidatorModel):
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

class DescribeSlotResponseTypeDef(BaseValidatorModel):
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

class UpdateSlotRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSlotResponseTypeDef(BaseValidatorModel):
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

