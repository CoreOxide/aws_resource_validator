from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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


class CreateBotVersionRequestTypeDef(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None


class IntentTypeDef(BaseValidatorModel):
    intentName: str
    intentVersion: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateIntentVersionRequestTypeDef(BaseValidatorModel):
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


class CreateSlotTypeVersionRequestTypeDef(BaseValidatorModel):
    name: str
    checksum: Optional[str] = None


class EnumerationValueOutputTypeDef(BaseValidatorModel):
    value: str
    synonyms: Optional[List[str]] = None


class DeleteBotAliasRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str


class DeleteBotChannelAssociationRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str
    botAlias: str


class DeleteBotRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteBotVersionRequestTypeDef(BaseValidatorModel):
    name: str
    version: str


class DeleteIntentRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteIntentVersionRequestTypeDef(BaseValidatorModel):
    name: str
    version: str


class DeleteSlotTypeRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteSlotTypeVersionRequestTypeDef(BaseValidatorModel):
    name: str
    version: str


class DeleteUtterancesRequestTypeDef(BaseValidatorModel):
    botName: str
    userId: str


class EnumerationValueTypeDef(BaseValidatorModel):
    value: str
    synonyms: Optional[Sequence[str]] = None


class GetBotAliasRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetBotAliasesRequestTypeDef(BaseValidatorModel):
    botName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetBotChannelAssociationRequestTypeDef(BaseValidatorModel):
    name: str
    botName: str
    botAlias: str


class GetBotChannelAssociationsRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetBotRequestTypeDef(BaseValidatorModel):
    name: str
    versionOrAlias: str


class GetBotVersionsRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetBotsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetBuiltinIntentRequestTypeDef(BaseValidatorModel):
    signature: str


class GetBuiltinIntentsRequestTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetBuiltinSlotTypesRequestTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetExportRequestTypeDef(BaseValidatorModel):
    name: str
    version: str
    resourceType: ResourceTypeType
    exportType: ExportTypeType


class GetImportRequestTypeDef(BaseValidatorModel):
    importId: str


class GetIntentRequestTypeDef(BaseValidatorModel):
    name: str
    version: str


class GetIntentVersionsRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class IntentMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None


class GetIntentsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetMigrationRequestTypeDef(BaseValidatorModel):
    migrationId: str


class GetMigrationsRequestTypeDef(BaseValidatorModel):
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


class GetSlotTypeRequestTypeDef(BaseValidatorModel):
    name: str
    version: str


class GetSlotTypeVersionsRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SlotTypeMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None


class GetSlotTypesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    nameContains: Optional[str] = None


class GetUtterancesViewRequestTypeDef(BaseValidatorModel):
    botName: str
    botVersions: Sequence[str]
    statusType: StatusTypeType


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
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


class StartMigrationRequestTypeDef(BaseValidatorModel):
    v1BotName: str
    v1BotVersion: str
    v2BotName: str
    v2BotRole: str
    migrationStrategy: MigrationStrategyType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UtteranceDataTypeDef(BaseValidatorModel):
    utteranceString: Optional[str] = None
    count: Optional[int] = None
    distinctUsers: Optional[int] = None
    firstUtteredDate: Optional[datetime] = None
    lastUtteredDate: Optional[datetime] = None


class ConversationLogsRequestTypeDef(BaseValidatorModel):
    logSettings: Sequence[LogSettingsRequestTypeDef]
    iamRoleArn: str


class ConversationLogsResponseTypeDef(BaseValidatorModel):
    logSettings: Optional[List[LogSettingsResponseTypeDef]] = None
    iamRoleArn: Optional[str] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class BotChannelAssociationTypeDef(BaseValidatorModel):
    pass


class GetBotChannelAssociationsResponseTypeDef(BaseValidatorModel):
    botChannelAssociations: List[BotChannelAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBotVersionsResponseTypeDef(BaseValidatorModel):
    bots: List[BotMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBotsResponseTypeDef(BaseValidatorModel):
    bots: List[BotMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBuiltinIntentResponseTypeDef(BaseValidatorModel):
    signature: str
    supportedLocales: List[LocaleType]
    slots: List[BuiltinIntentSlotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBuiltinIntentsResponseTypeDef(BaseValidatorModel):
    intents: List[BuiltinIntentMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBuiltinSlotTypesResponseTypeDef(BaseValidatorModel):
    slotTypes: List[BuiltinSlotTypeMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class GetBotAliasesRequestPaginateTypeDef(BaseValidatorModel):
    botName: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBotChannelAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBotVersionsRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBotsRequestPaginateTypeDef(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBuiltinIntentsRequestPaginateTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBuiltinSlotTypesRequestPaginateTypeDef(BaseValidatorModel):
    locale: Optional[LocaleType] = None
    signatureContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetIntentVersionsRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetIntentsRequestPaginateTypeDef(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSlotTypeVersionsRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSlotTypesRequestPaginateTypeDef(BaseValidatorModel):
    nameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetIntentVersionsResponseTypeDef(BaseValidatorModel):
    intents: List[IntentMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetIntentsResponseTypeDef(BaseValidatorModel):
    intents: List[IntentMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MigrationAlertTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetSlotTypeVersionsResponseTypeDef(BaseValidatorModel):
    slotTypes: List[SlotTypeMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetSlotTypesResponseTypeDef(BaseValidatorModel):
    slotTypes: List[SlotTypeMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class StartImportRequestTypeDef(BaseValidatorModel):
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


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class PromptOutputTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    maxAttempts: int
    responseCard: Optional[str] = None


class PromptTypeDef(BaseValidatorModel):
    messages: Sequence[MessageTypeDef]
    maxAttempts: int
    responseCard: Optional[str] = None


class StatementOutputTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    responseCard: Optional[str] = None


class StatementTypeDef(BaseValidatorModel):
    messages: Sequence[MessageTypeDef]
    responseCard: Optional[str] = None


class SlotDefaultValueSpecOutputTypeDef(BaseValidatorModel):
    defaultValueList: List[SlotDefaultValueTypeDef]


class SlotDefaultValueSpecTypeDef(BaseValidatorModel):
    defaultValueList: Sequence[SlotDefaultValueTypeDef]


class SlotTypeConfigurationTypeDef(BaseValidatorModel):
    regexConfiguration: Optional[SlotTypeRegexConfigurationTypeDef] = None


class UtteranceListTypeDef(BaseValidatorModel):
    botVersion: Optional[str] = None
    utterances: Optional[List[UtteranceDataTypeDef]] = None


class PutBotAliasRequestTypeDef(BaseValidatorModel):
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
    clarificationPrompt: PromptOutputTypeDef
    abortStatement: StatementOutputTypeDef
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


class FollowUpPromptOutputTypeDef(BaseValidatorModel):
    prompt: PromptOutputTypeDef
    rejectionStatement: StatementOutputTypeDef


class GetBotResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    intents: List[IntentTypeDef]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: PromptOutputTypeDef
    abortStatement: StatementOutputTypeDef
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


class PutBotResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    intents: List[IntentTypeDef]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: PromptOutputTypeDef
    abortStatement: StatementOutputTypeDef
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


class FollowUpPromptTypeDef(BaseValidatorModel):
    prompt: PromptTypeDef
    rejectionStatement: StatementTypeDef


class SlotOutputTypeDef(BaseValidatorModel):
    name: str
    slotConstraint: SlotConstraintType
    description: Optional[str] = None
    slotType: Optional[str] = None
    slotTypeVersion: Optional[str] = None
    valueElicitationPrompt: Optional[PromptOutputTypeDef] = None
    priority: Optional[int] = None
    sampleUtterances: Optional[List[str]] = None
    responseCard: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingType] = None
    defaultValueSpec: Optional[SlotDefaultValueSpecOutputTypeDef] = None


class CreateSlotTypeVersionResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueOutputTypeDef]
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
    enumerationValues: List[EnumerationValueOutputTypeDef]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategyType
    parentSlotTypeSignature: str
    slotTypeConfigurations: List[SlotTypeConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EnumerationValueUnionTypeDef(BaseValidatorModel):
    pass


class PutSlotTypeRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    enumerationValues: Optional[Sequence[EnumerationValueUnionTypeDef]] = None
    checksum: Optional[str] = None
    valueSelectionStrategy: Optional[SlotValueSelectionStrategyType] = None
    createVersion: Optional[bool] = None
    parentSlotTypeSignature: Optional[str] = None
    slotTypeConfigurations: Optional[Sequence[SlotTypeConfigurationTypeDef]] = None


class PutSlotTypeResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    enumerationValues: List[EnumerationValueOutputTypeDef]
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StatementUnionTypeDef(BaseValidatorModel):
    pass


class PromptUnionTypeDef(BaseValidatorModel):
    pass


class PutBotRequestTypeDef(BaseValidatorModel):
    name: str
    locale: LocaleType
    childDirected: bool
    description: Optional[str] = None
    intents: Optional[Sequence[IntentTypeDef]] = None
    enableModelImprovements: Optional[bool] = None
    nluIntentConfidenceThreshold: Optional[float] = None
    clarificationPrompt: Optional[PromptUnionTypeDef] = None
    abortStatement: Optional[StatementUnionTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    voiceId: Optional[str] = None
    checksum: Optional[str] = None
    processBehavior: Optional[ProcessBehaviorType] = None
    detectSentiment: Optional[bool] = None
    createVersion: Optional[bool] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class FulfillmentActivityTypeDef(BaseValidatorModel):
    pass


class CreateIntentVersionResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    slots: List[SlotOutputTypeDef]
    sampleUtterances: List[str]
    confirmationPrompt: PromptOutputTypeDef
    rejectionStatement: StatementOutputTypeDef
    followUpPrompt: FollowUpPromptOutputTypeDef
    conclusionStatement: StatementOutputTypeDef
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
    slots: List[SlotOutputTypeDef]
    sampleUtterances: List[str]
    confirmationPrompt: PromptOutputTypeDef
    rejectionStatement: StatementOutputTypeDef
    followUpPrompt: FollowUpPromptOutputTypeDef
    conclusionStatement: StatementOutputTypeDef
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


class PutIntentResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    slots: List[SlotOutputTypeDef]
    sampleUtterances: List[str]
    confirmationPrompt: PromptOutputTypeDef
    rejectionStatement: StatementOutputTypeDef
    followUpPrompt: FollowUpPromptOutputTypeDef
    conclusionStatement: StatementOutputTypeDef
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


class SlotDefaultValueSpecUnionTypeDef(BaseValidatorModel):
    pass


class SlotTypeDef(BaseValidatorModel):
    name: str
    slotConstraint: SlotConstraintType
    description: Optional[str] = None
    slotType: Optional[str] = None
    slotTypeVersion: Optional[str] = None
    valueElicitationPrompt: Optional[PromptUnionTypeDef] = None
    priority: Optional[int] = None
    sampleUtterances: Optional[Sequence[str]] = None
    responseCard: Optional[str] = None
    obfuscationSetting: Optional[ObfuscationSettingType] = None
    defaultValueSpec: Optional[SlotDefaultValueSpecUnionTypeDef] = None


class SlotUnionTypeDef(BaseValidatorModel):
    pass


class FollowUpPromptUnionTypeDef(BaseValidatorModel):
    pass


class PutIntentRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    slots: Optional[Sequence[SlotUnionTypeDef]] = None
    sampleUtterances: Optional[Sequence[str]] = None
    confirmationPrompt: Optional[PromptUnionTypeDef] = None
    rejectionStatement: Optional[StatementUnionTypeDef] = None
    followUpPrompt: Optional[FollowUpPromptUnionTypeDef] = None
    conclusionStatement: Optional[StatementUnionTypeDef] = None
    dialogCodeHook: Optional[CodeHookTypeDef] = None
    fulfillmentActivity: Optional[FulfillmentActivityTypeDef] = None
    parentIntentSignature: Optional[str] = None
    checksum: Optional[str] = None
    createVersion: Optional[bool] = None
    kendraConfiguration: Optional[KendraConfigurationTypeDef] = None
    inputContexts: Optional[Sequence[InputContextTypeDef]] = None
    outputContexts: Optional[Sequence[OutputContextTypeDef]] = None


