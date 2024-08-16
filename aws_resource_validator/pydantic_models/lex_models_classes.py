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
from aws_resource_validator.pydantic_models.lex_models_constants import *

class BotChannelAssociationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    botAlias: Optional[str] = None
    botName: Optional[str] = None
    createdDate: Optional[datetime] = None
    type: Optional[ChannelTypeType] = None
    botConfiguration: Optional[Dict[str, str]] = None
    status: Optional[ChannelStatusType] = None
    failureReason: Optional[str] = None

class BotMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusType] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None

class BuiltinIntentMetadataTypeDef(BaseValidatorModel):
    signature: Optional[str] = None
    supportedLocales: Optional[List[LocaleType]] = None

class BuiltinIntentSlotTypeDef(BaseValidatorModel):
    name: Optional[str] = None

class BuiltinSlotTypeMetadataTypeDef(BaseValidatorModel):
    signature: Optional[str] = None
    supportedLocales: Optional[List[LocaleType]] = None

class CodeHookTypeDef(BaseValidatorModel):
    uri: str
    messageVersion: str

class LogSettingsRequestTypeDef(BaseValidatorModel):
    logType: LogTypeType
    destination: DestinationType
    resourceArn: str
    kmsKeyArn: Optional[str] = None

class LogSettingsResponseTypeDef(BaseValidatorModel):
    logType: Optional[LogTypeType] = None
    destination: Optional[DestinationType] = None
    kmsKeyArn: Optional[str] = None
    resourceArn: Optional[str] = None
    resourcePrefix: Optional[str] = None

class CreateBotVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None

class IntentTypeDef(BaseValidatorModel):
    intentName: str
    intentVersion: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateIntentVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None

class InputContextTypeDef(BaseValidatorModel):
    name: str

class KendraConfigurationTypeDef(BaseValidatorModel):
    kendraIndex: str
    role: str
    queryFilterString: Optional[str] = None

class OutputContextTypeDef(BaseValidatorModel):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int

class CreateSlotTypeVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None

class EnumerationValueTypeDef(BaseValidatorModel):
    value: str
    synonyms: Optional[List[str]] = None

class DeleteBotAliasRequestRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str

class DeleteBotChannelAssociationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str
    botAlias: str

class DeleteBotRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteBotVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str

class DeleteIntentRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteIntentVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str

class DeleteSlotTypeRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteSlotTypeVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str

class DeleteUtterancesRequestRequestTypeDef(BaseValidatorModel):
    botName: str
    userId: str

class GetBotAliasRequestRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetBotAliasesRequestRequestTypeDef(BaseValidatorModel):
    botName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetBotChannelAssociationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str
    botAlias: str

class GetBotChannelAssociationsRequestRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetBotRequestRequestTypeDef(BaseValidatorModel):
    name: str
    versionOrAlias: str

class GetBotVersionsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetBotsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetBuiltinIntentRequestRequestTypeDef(BaseValidatorModel):
    signature: str

class GetBuiltinIntentsRequestRequestTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetBuiltinSlotTypesRequestRequestTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetExportRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType

class GetImportRequestRequestTypeDef(BaseValidatorModel):
    importId: str

class GetIntentRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str

class GetIntentVersionsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class IntentMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None

class GetIntentsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetMigrationRequestRequestTypeDef(BaseValidatorModel):
    migrationId: str

class MigrationAlertTypeDef(BaseValidatorModel):
    type: Optional[MigrationAlertTypeType] = None
    message: Optional[str] = None
    details: Optional[List[str]] = None
    referenceURLs: Optional[List[str]] = None

class GetMigrationsRequestRequestTypeDef(BaseValidatorModel):
    sortByAttribute: Optional[MigrationSortAttributeType] = None
    sortByOrder: Optional[SortOrderType] = None
    v1BotNameContains: Optional[str] = None
    migrationStatusEquals: Optional[MigrationStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MigrationSummaryTypeDef(BaseValidatorModel):
    migrationId: Optional[str] = None
    v1BotName: Optional[str] = None
    v1BotVersion: Optional[str] = None
    v1BotLocale: Optional[LocaleType] = None
    v2BotId: Optional[str] = None
    v2BotRole: Optional[str] = None
    migrationStatus: Optional[MigrationStatusType] = None
    migrationStrategy: Optional[MigrationStrategyType] = None
    migrationTimestamp: Optional[datetime] = None

class GetSlotTypeRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str

class GetSlotTypeVersionsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SlotTypeMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None

class GetSlotTypesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None

class GetUtterancesViewRequestRequestTypeDef(BaseValidatorModel):
    botName: str
    botVersions: Sequence[str]
    statusType: StatusTypeType

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class MessageTypeDef(BaseValidatorModel):
    contentType: ContentTypeType
    content: str
    groupNumber: Optional[int] = None

class SlotDefaultValueTypeDef(BaseValidatorModel):
    defaultValue: str

class SlotTypeRegexConfigurationTypeDef(BaseValidatorModel):
    pattern: str

class StartMigrationRequestRequestTypeDef(BaseValidatorModel):
    v1BotName: str
    v1BotVersion: str
    v2BotName: str
    v2BotRole: str
    migrationStrategy: MigrationStrategyType

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UtteranceDataTypeDef(BaseValidatorModel):
    utteranceString: Optional[str] = None
    count: Optional[int] = None
    distinctUsers: Optional[int] = None
    firstUtteredDate: Optional[datetime] = None
    lastUtteredDate: Optional[datetime] = None

class FulfillmentActivityTypeDef(BaseValidatorModel):
    type: FulfillmentActivityTypeType
    codeHook: Optional[CodeHookTypeDef] = None

class ConversationLogsRequestTypeDef(BaseValidatorModel):
    logSettings: Sequence[LogSettingsRequestTypeDef]
    iamRoleArn: str

class ConversationLogsResponseTypeDef(BaseValidatorModel):
    logSettings: Optional[List[LogSettingsResponseTypeDef]] = None
    iamRoleArn: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotChannelAssociationResponseTypeDef(BaseValidatorModel):
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

class GetBotChannelAssociationsResponseTypeDef(BaseValidatorModel):
    botChannelAssociations: List[BotChannelAssociationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotVersionsResponseTypeDef(BaseValidatorModel):
    bots: List[BotMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotsResponseTypeDef(BaseValidatorModel):
    bots: List[BotMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBuiltinIntentResponseTypeDef(BaseValidatorModel):
    signature: str
    supportedLocales: List[LocaleType]
    slots: List[BuiltinIntentSlotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBuiltinIntentsResponseTypeDef(BaseValidatorModel):
    intents: List[BuiltinIntentMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBuiltinSlotTypesResponseTypeDef(BaseValidatorModel):
    slotTypes: List[BuiltinSlotTypeMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExportResponseTypeDef(BaseValidatorModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType
    exportStatus: ExportStatusType
    failureReason: str
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportResponseTypeDef(BaseValidatorModel):
    name: str
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    importId: str
    importStatus: ImportStatusType
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartMigrationResponseTypeDef(BaseValidatorModel):
    v1BotName: str
    v1BotVersion: str
    v1BotLocale: LocaleType
    v2BotId: str
    v2BotRole: str
    migrationId: str
    migrationStrategy: MigrationStrategyType
    migrationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotAliasesRequestGetBotAliasesPaginateTypeDef(BaseValidatorModel):
    botName: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBotVersionsRequestGetBotVersionsPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBotsRequestGetBotsPaginateTypeDef(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntentsRequestGetIntentsPaginateTypeDef(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSlotTypesRequestGetSlotTypesPaginateTypeDef(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntentVersionsResponseTypeDef(BaseValidatorModel):
    intents: List[IntentMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntentsResponseTypeDef(BaseValidatorModel):
    intents: List[IntentMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMigrationResponseTypeDef(BaseValidatorModel):
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

class GetMigrationsResponseTypeDef(BaseValidatorModel):
    migrationSummaries: List[MigrationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSlotTypeVersionsResponseTypeDef(BaseValidatorModel):
    slotTypes: List[SlotTypeMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSlotTypesResponseTypeDef(BaseValidatorModel):
    slotTypes: List[SlotTypeMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportRequestRequestTypeDef(BaseValidatorModel):
    payload: BlobTypeDef
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    tags: Optional[Sequence[TagTypeDef]] = None

class StartImportResponseTypeDef(BaseValidatorModel):
    name: str
    resourceType: ResourceTypeType
    mergeStrategy: MergeStrategyType
    importId: str
    importStatus: ImportStatusType
    tags: List[TagTypeDef]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class PromptTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    maxAttempts: int
    responseCard: Optional[str] = None

class StatementTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    responseCard: Optional[str] = None

class SlotDefaultValueSpecTypeDef(BaseValidatorModel):
    defaultValueList: List[SlotDefaultValueTypeDef]

class SlotTypeConfigurationTypeDef(BaseValidatorModel):
    regexConfiguration: Optional[SlotTypeRegexConfigurationTypeDef] = None

class UtteranceListTypeDef(BaseValidatorModel):
    botVersion: Optional[str] = None
    utterances: Optional[List[UtteranceDataTypeDef]] = None

class PutBotAliasRequestRequestTypeDef(BaseValidatorModel):
    name: str
    botVersion: str
    botName: str
    description: Optional[str] = None
    checksum: Optional[str] = None
    conversationLogs: Optional[ConversationLogsRequestTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class BotAliasMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    botVersion: Optional[str] = None
    botName: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    checksum: Optional[str] = None
    conversationLogs: Optional[ConversationLogsResponseTypeDef] = None

class GetBotAliasResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: ConversationLogsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBotAliasResponseTypeDef(BaseValidatorModel):
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

class CreateBotVersionResponseTypeDef(BaseValidatorModel):
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

class FollowUpPromptTypeDef(BaseValidatorModel):
    prompt: PromptTypeDef
    rejectionStatement: StatementTypeDef

class GetBotResponseTypeDef(BaseValidatorModel):
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

class PutBotRequestRequestTypeDef(BaseValidatorModel):
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

class PutBotResponseTypeDef(BaseValidatorModel):
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

class SlotTypeDef(BaseValidatorModel):
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

class CreateSlotTypeVersionResponseTypeDef(BaseValidatorModel):
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

class GetSlotTypeResponseTypeDef(BaseValidatorModel):
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

class PutSlotTypeRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    enumerationValues: Optional[Sequence[EnumerationValueTypeDef]] = None
    checksum: Optional[str] = None
    valueSelectionStrategy: Optional[SlotValueSelectionStrategyType] = None
    createVersion: Optional[bool] = None
    parentSlotTypeSignature: Optional[str] = None
    slotTypeConfigurations: Optional[Sequence[SlotTypeConfigurationTypeDef]] = None

class PutSlotTypeResponseTypeDef(BaseValidatorModel):
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

class GetUtterancesViewResponseTypeDef(BaseValidatorModel):
    botName: str
    utterances: List[UtteranceListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotAliasesResponseTypeDef(BaseValidatorModel):
    BotAliases: List[BotAliasMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntentVersionResponseTypeDef(BaseValidatorModel):
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

class GetIntentResponseTypeDef(BaseValidatorModel):
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

class PutIntentRequestRequestTypeDef(BaseValidatorModel):
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

class PutIntentResponseTypeDef(BaseValidatorModel):
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

