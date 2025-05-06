from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lex_models.lex_models_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class BotChannelAssociation(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    botAlias: Optional[str] = None
    botName: Optional[str] = None
    createdDate: Optional[datetime] = None
    type: Optional[ChannelTypeType] = None
    botConfiguration: Optional[Dict[str, str]] = None
    status: Optional[ChannelStatusType] = None
    failureReason: Optional[str] = None


class BotMetadata(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusType] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None


class BuiltinIntentMetadata(BaseValidatorModel):
    signature: Optional[str] = None
    supportedLocales: Optional[List[LocaleType]] = None


class BuiltinIntentSlot(BaseValidatorModel):
    name: Optional[str] = None


class BuiltinSlotTypeMetadata(BaseValidatorModel):
    signature: Optional[str] = None
    supportedLocales: Optional[List[LocaleType]] = None


class CodeHook(BaseValidatorModel):
    uri: str
    messageVersion: str


class LogSettingsRequest(BaseValidatorModel):
    logType: LogTypeType
    destination: DestinationType
    resourceArn: str
    kmsKeyArn: Optional[str] = None


class LogSettingsResponse(BaseValidatorModel):
    logType: Optional[LogTypeType] = None
    destination: Optional[DestinationType] = None
    kmsKeyArn: Optional[str] = None
    resourceArn: Optional[str] = None
    resourcePrefix: Optional[str] = None


class CreateBotVersionRequest(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None


class Intent(BaseValidatorModel):
    intentName: str
    intentVersion: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateIntentVersionRequest(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None


class InputContext(BaseValidatorModel):
    name: str


class KendraConfiguration(BaseValidatorModel):
    kendraIndex: str
    role: str
    queryFilterString: Optional[str] = None


class OutputContext(BaseValidatorModel):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int


class CreateSlotTypeVersionRequest(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None


class EnumerationValueOutput(BaseValidatorModel):
    value: str
    synonyms: Optional[List[str]] = None


class DeleteBotAliasRequest(BaseValidatorModel):
    name: str
    botName: str


class DeleteBotChannelAssociationRequest(BaseValidatorModel):
    name: str
    botName: str
    botAlias: str


class DeleteBotRequest(BaseValidatorModel):
    name: str


class DeleteBotVersionRequest(BaseValidatorModel):
    name: str
    version: str


class DeleteIntentRequest(BaseValidatorModel):
    name: str


class DeleteIntentVersionRequest(BaseValidatorModel):
    name: str
    version: str


class DeleteSlotTypeRequest(BaseValidatorModel):
    name: str


class DeleteSlotTypeVersionRequest(BaseValidatorModel):
    name: str
    version: str


class DeleteUtterancesRequest(BaseValidatorModel):
    botName: str
    userId: str


class EnumerationValue(BaseValidatorModel):
    value: str
    synonyms: Optional[List[str]] = None


class GetBotAliasRequest(BaseValidatorModel):
    name: str
    botName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetBotAliasesRequest(BaseValidatorModel):
    botName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetBotChannelAssociationRequest(BaseValidatorModel):
    name: str
    botName: str
    botAlias: str


class GetBotChannelAssociationsRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetBotRequest(BaseValidatorModel):
    name: str
    versionOrAlias: str


class GetBotVersionsRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetBotsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetBuiltinIntentRequest(BaseValidatorModel):
    signature: str


class GetBuiltinIntentsRequest(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetBuiltinSlotTypesRequest(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetExportRequest(BaseValidatorModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType


class GetImportRequest(BaseValidatorModel):
    importId: str


class GetIntentRequest(BaseValidatorModel):
    name: str
    version: str


class GetIntentVersionsRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class IntentMetadata(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None


class GetIntentsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetMigrationRequest(BaseValidatorModel):
    migrationId: str


class MigrationAlert(BaseValidatorModel):
    type: Optional[MigrationAlertTypeType] = None
    message: Optional[str] = None
    details: Optional[List[str]] = None
    referenceURLs: Optional[List[str]] = None


class GetMigrationsRequest(BaseValidatorModel):
    sortByAttribute: Optional[MigrationSortAttributeType] = None
    sortByOrder: Optional[SortOrderType] = None
    v1BotNameContains: Optional[str] = None
    migrationStatusEquals: Optional[MigrationStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MigrationSummary(BaseValidatorModel):
    migrationId: Optional[str] = None
    v1BotName: Optional[str] = None
    v1BotVersion: Optional[str] = None
    v1BotLocale: Optional[LocaleType] = None
    v2BotId: Optional[str] = None
    v2BotRole: Optional[str] = None
    migrationStatus: Optional[MigrationStatusType] = None
    migrationStrategy: Optional[MigrationStrategyType] = None
    migrationTimestamp: Optional[datetime] = None


class GetSlotTypeRequest(BaseValidatorModel):
    name: str
    version: str


class GetSlotTypeVersionsRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SlotTypeMetadata(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None


class GetSlotTypesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetUtterancesViewRequest(BaseValidatorModel):
    botName: str
    botVersions: List[str]
    statusType: StatusTypeType


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Tag(BaseValidatorModel):
    key: str
    value: str


class Message(BaseValidatorModel):
    contentType: ContentTypeType
    content: str
    groupNumber: Optional[int] = None


class SlotDefaultValue(BaseValidatorModel):
    defaultValue: str


class SlotTypeRegexConfiguration(BaseValidatorModel):
    pattern: str


class StartMigrationRequest(BaseValidatorModel):
    v1BotName: str
    v1BotVersion: str
    v2BotName: str
    v2BotRole: str
    migrationStrategy: MigrationStrategyType


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UtteranceData(BaseValidatorModel):
    utteranceString: Optional[str] = None
    count: Optional[int] = None
    distinctUsers: Optional[int] = None
    firstUtteredDate: Optional[datetime] = None
    lastUtteredDate: Optional[datetime] = None


class FulfillmentActivity(BaseValidatorModel):
    type: FulfillmentActivityTypeType
    codeHook: Optional[CodeHook] = None


class ConversationLogsRequest(BaseValidatorModel):
    logSettings: List[LogSettingsRequest]
    iamRoleArn: str


class ConversationLogsResponse(BaseValidatorModel):
    logSettings: Optional[List[LogSettingsResponse]] = None
    iamRoleArn: Optional[str] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetBotChannelAssociationResponse(BaseValidatorModel):
    name: str
    description: str
    botAlias: str
    botName: str
    createdDate: datetime
    type: ChannelTypeType
    botConfiguration: Dict[str, str]
    status: ChannelStatusType
    failureReason: str
    ResponseMetadata: ResponseMetadata


class GetBotChannelAssociationsResponse(BaseValidatorModel):
    botChannelAssociations: List[BotChannelAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetBotVersionsResponse(BaseValidatorModel):
    bots: List[BotMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetBotsResponse(BaseValidatorModel):
    bots: List[BotMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetBuiltinIntentResponse(BaseValidatorModel):
    signature: str
    supportedLocales: List[LocaleType]
    slots: List[BuiltinIntentSlot]
    ResponseMetadata: ResponseMetadata


class GetBuiltinIntentsResponse(BaseValidatorModel):
    intents: List[BuiltinIntentMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetBuiltinSlotTypesResponse(BaseValidatorModel):
    slotTypes: List[BuiltinSlotTypeMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetExportResponse(BaseValidatorModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType
    exportStatus: ExportStatusType
    failureReason: str
    url: str
    ResponseMetadata: ResponseMetadata


class GetImportResponse(BaseValidatorModel):
    name: str
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    importId: str
    importStatus: ImportStatusType
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadata


class StartMigrationResponse(BaseValidatorModel):
    v1BotName: str
    v1BotVersion: str
    v1BotLocale: LocaleType
    v2BotId: str
    v2BotRole: str
    migrationId: str
    migrationStrategy: MigrationStrategyType
    migrationTimestamp: datetime
    ResponseMetadata: ResponseMetadata

EnumerationValueUnion = Union[EnumerationValue, EnumerationValueOutput]


class GetBotAliasesRequestPaginate(BaseValidatorModel):
    botName: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBotChannelAssociationsRequestPaginate(BaseValidatorModel):
    botName: str
    botAlias: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBotVersionsRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBotsRequestPaginate(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBuiltinIntentsRequestPaginate(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBuiltinSlotTypesRequestPaginate(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetIntentVersionsRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetIntentsRequestPaginate(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSlotTypeVersionsRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSlotTypesRequestPaginate(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetIntentVersionsResponse(BaseValidatorModel):
    intents: List[IntentMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetIntentsResponse(BaseValidatorModel):
    intents: List[IntentMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetMigrationResponse(BaseValidatorModel):
    migrationId: str
    v1BotName: str
    v1BotVersion: str
    v1BotLocale: LocaleType
    v2BotId: str
    v2BotRole: str
    migrationStatus: MigrationStatusType
    migrationStrategy: MigrationStrategyType
    migrationTimestamp: datetime
    alerts: List[MigrationAlert]
    ResponseMetadata: ResponseMetadata


class GetMigrationsResponse(BaseValidatorModel):
    migrationSummaries: List[MigrationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetSlotTypeVersionsResponse(BaseValidatorModel):
    slotTypes: List[SlotTypeMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetSlotTypesResponse(BaseValidatorModel):
    slotTypes: List[SlotTypeMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartImportRequest(BaseValidatorModel):
    payload: Blob
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    tags: Optional[List[Tag]] = None


class StartImportResponse(BaseValidatorModel):
    name: str
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    importId: str
    importStatus: ImportStatusType
    tags: List[Tag]
    createdDate: datetime
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class PromptOutput(BaseValidatorModel):
    messages: List[Message]
    maxAttempts: int
    responseCard: Optional[str] = None


class Prompt(BaseValidatorModel):
    messages: List[Message]
    maxAttempts: int
    responseCard: Optional[str] = None


class StatementOutput(BaseValidatorModel):
    messages: List[Message]
    responseCard: Optional[str] = None


class Statement(BaseValidatorModel):
    messages: List[Message]
    responseCard: Optional[str] = None


class SlotDefaultValueSpecOutput(BaseValidatorModel):
    defaultValueList: List[SlotDefaultValue]


class SlotDefaultValueSpec(BaseValidatorModel):
    defaultValueList: List[SlotDefaultValue]


class SlotTypeConfiguration(BaseValidatorModel):
    regexConfiguration: Optional[SlotTypeRegexConfiguration] = None


class UtteranceList(BaseValidatorModel):
    botVersion: Optional[str] = None
    utterances: Optional[List[UtteranceData]] = None


class PutBotAliasRequest(BaseValidatorModel):
    name: str
    botVersion: str
    botName: str
    description: Optional[str] = None
    checksum: Optional[str] = None
    conversationLogs: Optional[ConversationLogsRequest] = None
    tags: Optional[List[Tag]] = None


class BotAliasMetadata(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botName: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    checksum: Optional[str] = None
    conversationLogs: Optional[ConversationLogsResponse] = None


class GetBotAliasResponse(BaseValidatorModel):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: ConversationLogsResponse
    ResponseMetadata: ResponseMetadata


class PutBotAliasResponse(BaseValidatorModel):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: ConversationLogsResponse
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata

PromptUnion = Union[Prompt, PromptOutput]


class CreateBotVersionResponse(BaseValidatorModel):
    name: str
    description: str
    intents: List[Intent]
    clarificationPrompt: PromptOutput
    abortStatement: StatementOutput
    status: StatusType
    failureReason: str
    lastUpdatedDate: datetime
    createdDate: datetime
    idleSessionTTLInSeconds: int
    voiceId: str
    checksum: str
    version: str
    locale: LocaleType
    childDirected: bool
    enableModelImprovements: bool
    detectSentiment: bool
    ResponseMetadata: ResponseMetadata


class FollowUpPromptOutput(BaseValidatorModel):
    prompt: PromptOutput
    rejectionStatement: StatementOutput


class GetBotResponse(BaseValidatorModel):
    name: str
    description: str
    intents: List[Intent]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: PromptOutput
    abortStatement: StatementOutput
    status: StatusType
    failureReason: str
    lastUpdatedDate: datetime
    createdDate: datetime
    idleSessionTTLInSeconds: int
    voiceId: str
    checksum: str
    version: str
    locale: LocaleType
    childDirected: bool
    detectSentiment: bool
    ResponseMetadata: ResponseMetadata


class PutBotResponse(BaseValidatorModel):
    name: str
    description: str
    intents: List[Intent]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: PromptOutput
    abortStatement: StatementOutput
    status: StatusType
    failureReason: str
    lastUpdatedDate: datetime
    createdDate: datetime
    idleSessionTTLInSeconds: int
    voiceId: str
    checksum: str
    version: str
    locale: LocaleType
    childDirected: bool
    createVersion: bool
    detectSentiment: bool
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class FollowUpPrompt(BaseValidatorModel):
    prompt: Prompt
    rejectionStatement: Statement

StatementUnion = Union[Statement, StatementOutput]


class SlotOutput(BaseValidatorModel):
    name: str
    slotConstraint: SlotConstraintType
    description: Optional[str] = None
    slotType: Optional[str] = None
    slotTypeVersion: Optional[str] = None
    valueElicitationPrompt: Optional[PromptOutput] = None
    priority: Optional[int] = None
    sampleUtterances: Optional[List[str]] = None
    responseCard: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingType] = None
    defaultValueSpec: Optional[SlotDefaultValueSpecOutput] = None

SlotDefaultValueSpecUnion = Union[SlotDefaultValueSpec, SlotDefaultValueSpecOutput]


class CreateSlotTypeVersionResponse(BaseValidatorModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueOutput]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfiguration]
    ResponseMetadata: ResponseMetadata


class GetSlotTypeResponse(BaseValidatorModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueOutput]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfiguration]
    ResponseMetadata: ResponseMetadata


class PutSlotTypeRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    enumerationValues: Optional[List[EnumerationValueUnion]] = None
    checksum: Optional[str] = None
    valueSelectionStrategy: Optional[SlotValueSelectionStrategyType] = None
    createVersion: Optional[bool] = None
    parentSlotTypeSignature: Optional[str] = None
    slotTypeConfigurations: Optional[List[SlotTypeConfiguration]] = None


class PutSlotTypeResponse(BaseValidatorModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueOutput]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    createVersion: bool
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfiguration]
    ResponseMetadata: ResponseMetadata


class GetUtterancesViewResponse(BaseValidatorModel):
    botName: str
    utterances: List[UtteranceList]
    ResponseMetadata: ResponseMetadata


class GetBotAliasesResponse(BaseValidatorModel):
    BotAliases: List[BotAliasMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

FollowUpPromptUnion = Union[FollowUpPrompt, FollowUpPromptOutput]


class PutBotRequest(BaseValidatorModel):
    name: str
    locale: LocaleType
    childDirected: bool
    description: Optional[str] = None
    intents: Optional[List[Intent]] = None
    enableModelImprovements: Optional[bool] = None
    nluIntentConfidenceThreshold: Optional[float] = None
    clarificationPrompt: Optional[PromptUnion] = None
    abortStatement: Optional[StatementUnion] = None
    idleSessionTTLInSeconds: Optional[int] = None
    voiceId: Optional[str] = None
    checksum: Optional[str] = None
    processBehavior: Optional[ProcessBehaviorType] = None
    detectSentiment: Optional[bool] = None
    createVersion: Optional[bool] = None
    tags: Optional[List[Tag]] = None


class CreateIntentVersionResponse(BaseValidatorModel):
    name: str
    description: str
    slots: List[SlotOutput]
    sampleUtterances: List[str]
    confirmationPrompt: PromptOutput
    rejectionStatement: StatementOutput
    followUpPrompt: FollowUpPromptOutput
    conclusionStatement: StatementOutput
    dialogCodeHook: CodeHook
    fulfillmentActivity: FulfillmentActivity
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    kendraConfiguration: KendraConfiguration
    inputContexts: List[InputContext]
    outputContexts: List[OutputContext]
    ResponseMetadata: ResponseMetadata


class GetIntentResponse(BaseValidatorModel):
    name: str
    description: str
    slots: List[SlotOutput]
    sampleUtterances: List[str]
    confirmationPrompt: PromptOutput
    rejectionStatement: StatementOutput
    followUpPrompt: FollowUpPromptOutput
    conclusionStatement: StatementOutput
    dialogCodeHook: CodeHook
    fulfillmentActivity: FulfillmentActivity
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    kendraConfiguration: KendraConfiguration
    inputContexts: List[InputContext]
    outputContexts: List[OutputContext]
    ResponseMetadata: ResponseMetadata


class PutIntentResponse(BaseValidatorModel):
    name: str
    description: str
    slots: List[SlotOutput]
    sampleUtterances: List[str]
    confirmationPrompt: PromptOutput
    rejectionStatement: StatementOutput
    followUpPrompt: FollowUpPromptOutput
    conclusionStatement: StatementOutput
    dialogCodeHook: CodeHook
    fulfillmentActivity: FulfillmentActivity
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    createVersion: bool
    kendraConfiguration: KendraConfiguration
    inputContexts: List[InputContext]
    outputContexts: List[OutputContext]
    ResponseMetadata: ResponseMetadata


class Slot(BaseValidatorModel):
    name: str
    slotConstraint: SlotConstraintType
    description: Optional[str] = None
    slotType: Optional[str] = None
    slotTypeVersion: Optional[str] = None
    valueElicitationPrompt: Optional[PromptUnion] = None
    priority: Optional[int] = None
    sampleUtterances: Optional[List[str]] = None
    responseCard: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingType] = None
    defaultValueSpec: Optional[SlotDefaultValueSpecUnion] = None

SlotUnion = Union[Slot, SlotOutput]


class PutIntentRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    slots: Optional[List[SlotUnion]] = None
    sampleUtterances: Optional[List[str]] = None
    confirmationPrompt: Optional[PromptUnion] = None
    rejectionStatement: Optional[StatementUnion] = None
    followUpPrompt: Optional[FollowUpPromptUnion] = None
    conclusionStatement: Optional[StatementUnion] = None
    dialogCodeHook: Optional[CodeHook] = None
    fulfillmentActivity: Optional[FulfillmentActivity] = None
    parentIntentSignature: Optional[str] = None
    checksum: Optional[str] = None
    createVersion: Optional[bool] = None
    kendraConfiguration: Optional[KendraConfiguration] = None
    inputContexts: Optional[List[InputContext]] = None
    outputContexts: Optional[List[OutputContext]] = None