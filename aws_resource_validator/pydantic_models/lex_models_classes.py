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
from aws_resource_validator.pydantic_models.lex_models_constants import *

class BotChannelAssociationTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    botAlias: Optional[str] = None
    botName: Optional[str] = None
    createdDate: Optional[datetime] = None
    type: Optional[ChannelTypeType] = None
    botConfiguration: Optional[Dict[str, str]] = None
    status: Optional[ChannelStatusType] = None
    failureReason: Optional[str] = None

class BotMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusType] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None

class BuiltinIntentMetadataTypeDef(BaseModel):
    signature: Optional[str] = None
    supportedLocales: Optional[List[LocaleType]] = None

class BuiltinIntentSlotTypeDef(BaseModel):
    name: Optional[str] = None

class BuiltinSlotTypeMetadataTypeDef(BaseModel):
    signature: Optional[str] = None
    supportedLocales: Optional[List[LocaleType]] = None

class CodeHookTypeDef(BaseModel):
    uri: str
    messageVersion: str

class LogSettingsRequestTypeDef(BaseModel):
    logType: LogTypeType
    destination: DestinationType
    resourceArn: str
    kmsKeyArn: Optional[str] = None

class LogSettingsResponseTypeDef(BaseModel):
    logType: Optional[LogTypeType] = None
    destination: Optional[DestinationType] = None
    kmsKeyArn: Optional[str] = None
    resourceArn: Optional[str] = None
    resourcePrefix: Optional[str] = None

class CreateBotVersionRequestRequestTypeDef(BaseModel):
    name: str
    checksum: Optional[str] = None

class IntentTypeDef(BaseModel):
    intentName: str
    intentVersion: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateIntentVersionRequestRequestTypeDef(BaseModel):
    name: str
    checksum: Optional[str] = None

class InputContextTypeDef(BaseModel):
    name: str

class KendraConfigurationTypeDef(BaseModel):
    kendraIndex: str
    role: str
    queryFilterString: Optional[str] = None

class OutputContextTypeDef(BaseModel):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int

class CreateSlotTypeVersionRequestRequestTypeDef(BaseModel):
    name: str
    checksum: Optional[str] = None

class EnumerationValueTypeDef(BaseModel):
    value: str
    synonyms: Optional[List[str]] = None

class DeleteBotAliasRequestRequestTypeDef(BaseModel):
    name: str
    botName: str

class DeleteBotChannelAssociationRequestRequestTypeDef(BaseModel):
    name: str
    botName: str
    botAlias: str

class DeleteBotRequestRequestTypeDef(BaseModel):
    name: str

class DeleteBotVersionRequestRequestTypeDef(BaseModel):
    name: str
    version: str

class DeleteIntentRequestRequestTypeDef(BaseModel):
    name: str

class DeleteIntentVersionRequestRequestTypeDef(BaseModel):
    name: str
    version: str

class DeleteSlotTypeRequestRequestTypeDef(BaseModel):
    name: str

class DeleteSlotTypeVersionRequestRequestTypeDef(BaseModel):
    name: str
    version: str

class DeleteUtterancesRequestRequestTypeDef(BaseModel):
    botName: str
    userId: str

class GetBotAliasRequestRequestTypeDef(BaseModel):
    name: str
    botName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetBotAliasesRequestRequestTypeDef(BaseModel):
    botName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetBotChannelAssociationRequestRequestTypeDef(BaseModel):
    name: str
    botName: str
    botAlias: str

class GetBotChannelAssociationsRequestRequestTypeDef(BaseModel):
    botName: str
    botAlias: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetBotRequestRequestTypeDef(BaseModel):
    name: str
    versionOrAlias: str

class GetBotVersionsRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetBotsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetBuiltinIntentRequestRequestTypeDef(BaseModel):
    signature: str

class GetBuiltinIntentsRequestRequestTypeDef(BaseModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetBuiltinSlotTypesRequestRequestTypeDef(BaseModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetExportRequestRequestTypeDef(BaseModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType

class GetImportRequestRequestTypeDef(BaseModel):
    importId: str

class GetIntentRequestRequestTypeDef(BaseModel):
    name: str
    version: str

class GetIntentVersionsRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class IntentMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None

class GetIntentsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetMigrationRequestRequestTypeDef(BaseModel):
    migrationId: str

class MigrationAlertTypeDef(BaseModel):
    type: Optional[MigrationAlertTypeType] = None
    message: Optional[str] = None
    details: Optional[List[str]] = None
    referenceURLs: Optional[List[str]] = None

class GetMigrationsRequestRequestTypeDef(BaseModel):
    sortByAttribute: Optional[MigrationSortAttributeType] = None
    sortByOrder: Optional[SortOrderType] = None
    v1BotNameContains: Optional[str] = None
    migrationStatusEquals: Optional[MigrationStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MigrationSummaryTypeDef(BaseModel):
    migrationId: Optional[str] = None
    v1BotName: Optional[str] = None
    v1BotVersion: Optional[str] = None
    v1BotLocale: Optional[LocaleType] = None
    v2BotId: Optional[str] = None
    v2BotRole: Optional[str] = None
    migrationStatus: Optional[MigrationStatusType] = None
    migrationStrategy: Optional[MigrationStrategyType] = None
    migrationTimestamp: Optional[datetime] = None

class GetSlotTypeRequestRequestTypeDef(BaseModel):
    name: str
    version: str

class GetSlotTypeVersionsRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SlotTypeMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None

class GetSlotTypesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetUtterancesViewRequestRequestTypeDef(BaseModel):
    botName: str
    botVersions: Sequence[str]
    statusType: StatusTypeType

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagTypeDef(BaseModel):
    key: str
    value: str

class MessageTypeDef(BaseModel):
    contentType: ContentTypeType
    content: str
    groupNumber: Optional[int] = None

class SlotDefaultValueTypeDef(BaseModel):
    defaultValue: str

class SlotTypeRegexConfigurationTypeDef(BaseModel):
    pattern: str

class StartMigrationRequestRequestTypeDef(BaseModel):
    v1BotName: str
    v1BotVersion: str
    v2BotName: str
    v2BotRole: str
    migrationStrategy: MigrationStrategyType

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UtteranceDataTypeDef(BaseModel):
    utteranceString: Optional[str] = None
    count: Optional[int] = None
    distinctUsers: Optional[int] = None
    firstUtteredDate: Optional[datetime] = None
    lastUtteredDate: Optional[datetime] = None

class FulfillmentActivityTypeDef(BaseModel):
    type: FulfillmentActivityTypeType
    codeHook: Optional[CodeHookTypeDef] = None

class ConversationLogsRequestTypeDef(BaseModel):
    logSettings: Sequence[LogSettingsRequestTypeDef]
    iamRoleArn: str

class ConversationLogsResponseTypeDef(BaseModel):
    logSettings: Optional[List[LogSettingsResponseTypeDef]] = None
    iamRoleArn: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotChannelAssociationResponseTypeDef(BaseModel):
    name: str
    description: str
    botAlias: str
    botName: str
    createdDate: datetime
    type: ChannelTypeType
    botConfiguration: Dict[str, str]
    status: ChannelStatusType
    failureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotChannelAssociationsResponseTypeDef(BaseModel):
    botChannelAssociations: List[BotChannelAssociationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotVersionsResponseTypeDef(BaseModel):
    bots: List[BotMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotsResponseTypeDef(BaseModel):
    bots: List[BotMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBuiltinIntentResponseTypeDef(BaseModel):
    signature: str
    supportedLocales: List[LocaleType]
    slots: List[BuiltinIntentSlotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBuiltinIntentsResponseTypeDef(BaseModel):
    intents: List[BuiltinIntentMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBuiltinSlotTypesResponseTypeDef(BaseModel):
    slotTypes: List[BuiltinSlotTypeMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExportResponseTypeDef(BaseModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType
    exportStatus: ExportStatusType
    failureReason: str
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportResponseTypeDef(BaseModel):
    name: str
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    importId: str
    importStatus: ImportStatusType
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartMigrationResponseTypeDef(BaseModel):
    v1BotName: str
    v1BotVersion: str
    v1BotLocale: LocaleType
    v2BotId: str
    v2BotRole: str
    migrationId: str
    migrationStrategy: MigrationStrategyType
    migrationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotAliasesRequestGetBotAliasesPaginateTypeDef(BaseModel):
    botName: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef(BaseModel):
    botName: str
    botAlias: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBotVersionsRequestGetBotVersionsPaginateTypeDef(BaseModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBotsRequestGetBotsPaginateTypeDef(BaseModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef(BaseModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef(BaseModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef(BaseModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntentsRequestGetIntentsPaginateTypeDef(BaseModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef(BaseModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSlotTypesRequestGetSlotTypesPaginateTypeDef(BaseModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntentVersionsResponseTypeDef(BaseModel):
    intents: List[IntentMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntentsResponseTypeDef(BaseModel):
    intents: List[IntentMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationResponseTypeDef(BaseModel):
    migrationId: str
    v1BotName: str
    v1BotVersion: str
    v1BotLocale: LocaleType
    v2BotId: str
    v2BotRole: str
    migrationStatus: MigrationStatusType
    migrationStrategy: MigrationStrategyType
    migrationTimestamp: datetime
    alerts: List[MigrationAlertTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationsResponseTypeDef(BaseModel):
    migrationSummaries: List[MigrationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSlotTypeVersionsResponseTypeDef(BaseModel):
    slotTypes: List[SlotTypeMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSlotTypesResponseTypeDef(BaseModel):
    slotTypes: List[SlotTypeMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportRequestRequestTypeDef(BaseModel):
    payload: BlobTypeDef
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    tags: Optional[Sequence[TagTypeDef]] = None

class StartImportResponseTypeDef(BaseModel):
    name: str
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    importId: str
    importStatus: ImportStatusType
    tags: List[TagTypeDef]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class PromptTypeDef(BaseModel):
    messages: List[MessageTypeDef]
    maxAttempts: int
    responseCard: Optional[str] = None

class StatementTypeDef(BaseModel):
    messages: List[MessageTypeDef]
    responseCard: Optional[str] = None

class SlotDefaultValueSpecTypeDef(BaseModel):
    defaultValueList: List[SlotDefaultValueTypeDef]

class SlotTypeConfigurationTypeDef(BaseModel):
    regexConfiguration: Optional[SlotTypeRegexConfigurationTypeDef] = None

class UtteranceListTypeDef(BaseModel):
    botVersion: Optional[str] = None
    utterances: Optional[List[UtteranceDataTypeDef]] = None

class PutBotAliasRequestRequestTypeDef(BaseModel):
    name: str
    botVersion: str
    botName: str
    description: Optional[str] = None
    checksum: Optional[str] = None
    conversationLogs: Optional[ConversationLogsRequestTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class BotAliasMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botName: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    checksum: Optional[str] = None
    conversationLogs: Optional[ConversationLogsResponseTypeDef] = None

class GetBotAliasResponseTypeDef(BaseModel):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: ConversationLogsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBotAliasResponseTypeDef(BaseModel):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: ConversationLogsResponseTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBotVersionResponseTypeDef(BaseModel):
    name: str
    description: str
    intents: List[IntentTypeDef]
    clarificationPrompt: PromptTypeDef
    abortStatement: StatementTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class FollowUpPromptTypeDef(BaseModel):
    prompt: PromptTypeDef
    rejectionStatement: StatementTypeDef

class GetBotResponseTypeDef(BaseModel):
    name: str
    description: str
    intents: List[IntentTypeDef]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: PromptTypeDef
    abortStatement: StatementTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class PutBotRequestRequestTypeDef(BaseModel):
    name: str
    locale: LocaleType
    childDirected: bool
    description: Optional[str] = None
    intents: Optional[Sequence[IntentTypeDef]] = None
    enableModelImprovements: Optional[bool] = None
    nluIntentConfidenceThreshold: Optional[float] = None
    clarificationPrompt: Optional[PromptTypeDef] = None
    abortStatement: Optional[StatementTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    voiceId: Optional[str] = None
    checksum: Optional[str] = None
    processBehavior: Optional[ProcessBehaviorType] = None
    detectSentiment: Optional[bool] = None
    createVersion: Optional[bool] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutBotResponseTypeDef(BaseModel):
    name: str
    description: str
    intents: List[IntentTypeDef]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: PromptTypeDef
    abortStatement: StatementTypeDef
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
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SlotTypeDef(BaseModel):
    name: str
    slotConstraint: SlotConstraintType
    description: Optional[str] = None
    slotType: Optional[str] = None
    slotTypeVersion: Optional[str] = None
    valueElicitationPrompt: Optional[PromptTypeDef] = None
    priority: Optional[int] = None
    sampleUtterances: Optional[List[str]] = None
    responseCard: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingType] = None
    defaultValueSpec: Optional[SlotDefaultValueSpecTypeDef] = None

class CreateSlotTypeVersionResponseTypeDef(BaseModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueTypeDef]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSlotTypeResponseTypeDef(BaseModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueTypeDef]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSlotTypeRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    enumerationValues: Optional[Sequence[EnumerationValueTypeDef]] = None
    checksum: Optional[str] = None
    valueSelectionStrategy: Optional[SlotValueSelectionStrategyType] = None
    createVersion: Optional[bool] = None
    parentSlotTypeSignature: Optional[str] = None
    slotTypeConfigurations: Optional[Sequence[SlotTypeConfigurationTypeDef]] = None

class PutSlotTypeResponseTypeDef(BaseModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueTypeDef]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    createVersion: bool
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUtterancesViewResponseTypeDef(BaseModel):
    botName: str
    utterances: List[UtteranceListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotAliasesResponseTypeDef(BaseModel):
    BotAliases: List[BotAliasMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntentVersionResponseTypeDef(BaseModel):
    name: str
    description: str
    slots: List[SlotTypeDef]
    sampleUtterances: List[str]
    confirmationPrompt: PromptTypeDef
    rejectionStatement: StatementTypeDef
    followUpPrompt: FollowUpPromptTypeDef
    conclusionStatement: StatementTypeDef
    dialogCodeHook: CodeHookTypeDef
    fulfillmentActivity: FulfillmentActivityTypeDef
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    kendraConfiguration: KendraConfigurationTypeDef
    inputContexts: List[InputContextTypeDef]
    outputContexts: List[OutputContextTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntentResponseTypeDef(BaseModel):
    name: str
    description: str
    slots: List[SlotTypeDef]
    sampleUtterances: List[str]
    confirmationPrompt: PromptTypeDef
    rejectionStatement: StatementTypeDef
    followUpPrompt: FollowUpPromptTypeDef
    conclusionStatement: StatementTypeDef
    dialogCodeHook: CodeHookTypeDef
    fulfillmentActivity: FulfillmentActivityTypeDef
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    kendraConfiguration: KendraConfigurationTypeDef
    inputContexts: List[InputContextTypeDef]
    outputContexts: List[OutputContextTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutIntentRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    slots: Optional[Sequence[SlotTypeDef]] = None
    sampleUtterances: Optional[Sequence[str]] = None
    confirmationPrompt: Optional[PromptTypeDef] = None
    rejectionStatement: Optional[StatementTypeDef] = None
    followUpPrompt: Optional[FollowUpPromptTypeDef] = None
    conclusionStatement: Optional[StatementTypeDef] = None
    dialogCodeHook: Optional[CodeHookTypeDef] = None
    fulfillmentActivity: Optional[FulfillmentActivityTypeDef] = None
    parentIntentSignature: Optional[str] = None
    checksum: Optional[str] = None
    createVersion: Optional[bool] = None
    kendraConfiguration: Optional[KendraConfigurationTypeDef] = None
    inputContexts: Optional[Sequence[InputContextTypeDef]] = None
    outputContexts: Optional[Sequence[OutputContextTypeDef]] = None

class PutIntentResponseTypeDef(BaseModel):
    name: str
    description: str
    slots: List[SlotTypeDef]
    sampleUtterances: List[str]
    confirmationPrompt: PromptTypeDef
    rejectionStatement: StatementTypeDef
    followUpPrompt: FollowUpPromptTypeDef
    conclusionStatement: StatementTypeDef
    dialogCodeHook: CodeHookTypeDef
    fulfillmentActivity: FulfillmentActivityTypeDef
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    createVersion: bool
    kendraConfiguration: KendraConfigurationTypeDef
    inputContexts: List[InputContextTypeDef]
    outputContexts: List[OutputContextTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

