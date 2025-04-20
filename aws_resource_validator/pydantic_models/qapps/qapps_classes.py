from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.qapps.qapps_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateLibraryItemReviewInput(BaseValidatorModel):
    instanceId: str
    libraryItemId: str


class AssociateQAppWithUserInput(BaseValidatorModel):
    instanceId: str
    appId: str


class BatchCreateCategoryInputCategory(BaseValidatorModel):
    title: str
    id: Optional[str] = None
    color: Optional[str] = None


class BatchDeleteCategoryInput(BaseValidatorModel):
    instanceId: str
    categories: List[str]


class CategoryInput(BaseValidatorModel):
    id: str
    title: str
    color: Optional[str] = None


class FileUploadCardInput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    filename: Optional[str] = None
    fileId: Optional[str] = None
    allowOverride: Optional[bool] = None


class QPluginCardInput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    pluginId: str
    actionIdentifier: Optional[str] = None


class TextInputCardInput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None


class Submission(BaseValidatorModel):
    value: Optional[Dict[str, Any]] = None
    submissionId: Optional[str] = None
    timestamp: Optional[datetime] = None


class FileUploadCard(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    filename: Optional[str] = None
    fileId: Optional[str] = None
    allowOverride: Optional[bool] = None


class QPluginCard(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    prompt: str
    pluginType: PluginTypeType
    pluginId: str
    actionIdentifier: Optional[str] = None


class TextInputCard(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None


class SubmissionMutation(BaseValidatorModel):
    submissionId: str
    mutationType: SubmissionMutationKindType


class Category(BaseValidatorModel):
    id: str
    title: str
    color: Optional[str] = None
    appCount: Optional[int] = None


class ConversationMessage(BaseValidatorModel):
    body: str
    type: SenderType


class CreateLibraryItemInput(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: int
    categories: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreatePresignedUrlInput(BaseValidatorModel):
    instanceId: str
    cardId: str
    appId: str
    fileContentsSha256: str
    fileName: str
    scope: DocumentScopeType
    sessionId: Optional[str] = None


class DeleteLibraryItemInput(BaseValidatorModel):
    instanceId: str
    libraryItemId: str


class DeleteQAppInput(BaseValidatorModel):
    instanceId: str
    appId: str


class DescribeQAppPermissionsInput(BaseValidatorModel):
    instanceId: str
    appId: str


class DisassociateLibraryItemReviewInput(BaseValidatorModel):
    instanceId: str
    libraryItemId: str


class DisassociateQAppFromUserInput(BaseValidatorModel):
    instanceId: str
    appId: str


class DocumentAttributeValueOutput(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None

Timestamp = Union[datetime, str]


class ExportQAppSessionDataInput(BaseValidatorModel):
    instanceId: str
    sessionId: str


class FormInputCardMetadataOutput(BaseValidatorModel):
    schema: Dict[str, Any]


class FormInputCardMetadata(BaseValidatorModel):
    schema: Dict[str, Any]


class GetLibraryItemInput(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    appId: Optional[str] = None


class GetQAppInput(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: Optional[int] = None


class GetQAppSessionInput(BaseValidatorModel):
    instanceId: str
    sessionId: str


class GetQAppSessionMetadataInput(BaseValidatorModel):
    instanceId: str
    sessionId: str


class SessionSharingConfiguration(BaseValidatorModel):
    enabled: bool
    acceptResponses: Optional[bool] = None
    revealCards: Optional[bool] = None


class ImportDocumentInput(BaseValidatorModel):
    instanceId: str
    cardId: str
    appId: str
    fileContentsBase64: str
    fileName: str
    scope: DocumentScopeType
    sessionId: Optional[str] = None


class ListCategoriesInput(BaseValidatorModel):
    instanceId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListLibraryItemsInput(BaseValidatorModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None
    categoryId: Optional[str] = None


class ListQAppSessionDataInput(BaseValidatorModel):
    instanceId: str
    sessionId: str


class ListQAppsInput(BaseValidatorModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class UserAppItem(BaseValidatorModel):
    appId: str
    appArn: str
    title: str
    createdAt: datetime
    description: Optional[str] = None
    canEdit: Optional[bool] = None
    status: Optional[str] = None
    isVerified: Optional[bool] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class PermissionInput(BaseValidatorModel):
    action: PermissionInputActionEnumType
    principal: str


class PrincipalOutput(BaseValidatorModel):
    userId: Optional[str] = None
    userType: Optional[PrincipalOutputUserTypeEnumType] = None
    email: Optional[str] = None


class User(BaseValidatorModel):
    userId: Optional[str] = None


class StopQAppSessionInput(BaseValidatorModel):
    instanceId: str
    sessionId: str


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


class UpdateLibraryItemInput(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    status: Optional[LibraryItemStatusType] = None
    categories: Optional[List[str]] = None


class UpdateLibraryItemMetadataInput(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    isVerified: Optional[bool] = None


class BatchCreateCategoryInput(BaseValidatorModel):
    instanceId: str
    categories: List[BatchCreateCategoryInputCategory]


class BatchUpdateCategoryInput(BaseValidatorModel):
    instanceId: str
    categories: List[CategoryInput]


class CardStatus(BaseValidatorModel):
    currentState: ExecutionStatusType
    currentValue: str
    submissions: Optional[List[Submission]] = None


class CardValue(BaseValidatorModel):
    cardId: str
    value: str
    submissionMutation: Optional[SubmissionMutation] = None


class LibraryItemMember(BaseValidatorModel):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[Category]
    status: str
    createdAt: datetime
    createdBy: str
    ratingCount: int
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    isRatedByUser: Optional[bool] = None
    userCount: Optional[int] = None
    isVerified: Optional[bool] = None


class PredictQAppInputOptions(BaseValidatorModel):
    conversation: Optional[List[ConversationMessage]] = None
    problemStatement: Optional[str] = None


class CreateLibraryItemOutput(BaseValidatorModel):
    libraryItemId: str
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isVerified: bool
    ResponseMetadata: ResponseMetadata


class CreatePresignedUrlOutput(BaseValidatorModel):
    fileId: str
    presignedUrl: str
    presignedUrlFields: Dict[str, str]
    presignedUrlExpiration: datetime
    ResponseMetadata: ResponseMetadata


class CreateQAppOutput(BaseValidatorModel):
    appId: str
    appArn: str
    title: str
    description: str
    initialPrompt: str
    appVersion: int
    status: AppStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    requiredCapabilities: List[AppRequiredCapabilityType]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExportQAppSessionDataOutput(BaseValidatorModel):
    csvFileLink: str
    expiresAt: datetime
    sessionArn: str
    ResponseMetadata: ResponseMetadata


class GetLibraryItemOutput(BaseValidatorModel):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[Category]
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isRatedByUser: bool
    userCount: int
    isVerified: bool
    ResponseMetadata: ResponseMetadata


class ImportDocumentOutput(BaseValidatorModel):
    fileId: str
    ResponseMetadata: ResponseMetadata


class ListCategoriesOutput(BaseValidatorModel):
    categories: List[Category]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartQAppSessionOutput(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadata


class UpdateLibraryItemOutput(BaseValidatorModel):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[Category]
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isRatedByUser: bool
    userCount: int
    isVerified: bool
    ResponseMetadata: ResponseMetadata


class UpdateQAppOutput(BaseValidatorModel):
    appId: str
    appArn: str
    title: str
    description: str
    initialPrompt: str
    appVersion: int
    status: AppStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    requiredCapabilities: List[AppRequiredCapabilityType]
    ResponseMetadata: ResponseMetadata


class UpdateQAppSessionOutput(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadata


class DocumentAttributeOutput(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueOutput


class DocumentAttributeValue(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[Timestamp] = None


class FormInputCardInputOutput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    metadata: FormInputCardMetadataOutput
    computeMode: Optional[InputCardComputeModeType] = None


class FormInputCard(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    metadata: FormInputCardMetadataOutput
    computeMode: Optional[InputCardComputeModeType] = None


class FormInputCardInput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    metadata: FormInputCardMetadata
    computeMode: Optional[InputCardComputeModeType] = None


class GetQAppSessionMetadataOutput(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionName: str
    sharingConfiguration: SessionSharingConfiguration
    sessionOwner: bool
    ResponseMetadata: ResponseMetadata


class UpdateQAppSessionMetadataInput(BaseValidatorModel):
    instanceId: str
    sessionId: str
    sharingConfiguration: SessionSharingConfiguration
    sessionName: Optional[str] = None


class UpdateQAppSessionMetadataOutput(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionName: str
    sharingConfiguration: SessionSharingConfiguration
    ResponseMetadata: ResponseMetadata


class ListLibraryItemsInputPaginate(BaseValidatorModel):
    instanceId: str
    categoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQAppsInputPaginate(BaseValidatorModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQAppsOutput(BaseValidatorModel):
    apps: List[UserAppItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateQAppPermissionsInput(BaseValidatorModel):
    instanceId: str
    appId: str
    grantPermissions: Optional[List[PermissionInput]] = None
    revokePermissions: Optional[List[PermissionInput]] = None


class PermissionOutput(BaseValidatorModel):
    action: PermissionOutputActionEnumType
    principal: PrincipalOutput


class QAppSessionData(BaseValidatorModel):
    cardId: str
    user: User
    value: Optional[Dict[str, Any]] = None
    submissionId: Optional[str] = None
    timestamp: Optional[datetime] = None


class GetQAppSessionOutput(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionName: str
    appVersion: int
    latestPublishedAppVersion: int
    status: ExecutionStatusType
    cardStatus: Dict[str, CardStatus]
    userIsHost: bool
    ResponseMetadata: ResponseMetadata


class StartQAppSessionInput(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: int
    initialValues: Optional[List[CardValue]] = None
    sessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateQAppSessionInput(BaseValidatorModel):
    instanceId: str
    sessionId: str
    values: Optional[List[CardValue]] = None


class ListLibraryItemsOutput(BaseValidatorModel):
    libraryItems: List[LibraryItemMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PredictQAppInput(BaseValidatorModel):
    instanceId: str
    options: Optional[PredictQAppInputOptions] = None


class AttributeFilterOutput(BaseValidatorModel):
    andAllFilters: Optional[List[Dict[str, Any]]] = None
    orAllFilters: Optional[List[Dict[str, Any]]] = None
    notFilter: Optional[Dict[str, Any]] = None
    equalsTo: Optional[DocumentAttributeOutput] = None
    containsAll: Optional[DocumentAttributeOutput] = None
    containsAny: Optional[DocumentAttributeOutput] = None
    greaterThan: Optional[DocumentAttributeOutput] = None
    greaterThanOrEquals: Optional[DocumentAttributeOutput] = None
    lessThan: Optional[DocumentAttributeOutput] = None
    lessThanOrEquals: Optional[DocumentAttributeOutput] = None


class DocumentAttribute(BaseValidatorModel):
    name: str
    value: DocumentAttributeValue


class DescribeQAppPermissionsOutput(BaseValidatorModel):
    resourceArn: str
    appId: str
    permissions: List[PermissionOutput]
    ResponseMetadata: ResponseMetadata


class UpdateQAppPermissionsOutput(BaseValidatorModel):
    resourceArn: str
    appId: str
    permissions: List[PermissionOutput]
    ResponseMetadata: ResponseMetadata


class ListQAppSessionDataOutput(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionData: List[QAppSessionData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class QQueryCardInputOutput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    outputSource: Optional[CardOutputSourceType] = None
    attributeFilter: Optional[AttributeFilterOutput] = None


class QQueryCard(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    prompt: str
    outputSource: CardOutputSourceType
    attributeFilter: Optional[AttributeFilterOutput] = None
    memoryReferences: Optional[List[str]] = None


class AttributeFilter(BaseValidatorModel):
    andAllFilters: Optional[List[Dict[str, Any]]] = None
    orAllFilters: Optional[List[Dict[str, Any]]] = None
    notFilter: Optional[Dict[str, Any]] = None
    equalsTo: Optional[DocumentAttribute] = None
    containsAll: Optional[DocumentAttribute] = None
    containsAny: Optional[DocumentAttribute] = None
    greaterThan: Optional[DocumentAttribute] = None
    greaterThanOrEquals: Optional[DocumentAttribute] = None
    lessThan: Optional[DocumentAttribute] = None
    lessThanOrEquals: Optional[DocumentAttribute] = None


class CardInputOutput(BaseValidatorModel):
    textInput: Optional[TextInputCardInput] = None
    qQuery: Optional[QQueryCardInputOutput] = None
    qPlugin: Optional[QPluginCardInput] = None
    fileUpload: Optional[FileUploadCardInput] = None
    formInput: Optional[FormInputCardInputOutput] = None


class Card(BaseValidatorModel):
    textInput: Optional[TextInputCard] = None
    qQuery: Optional[QQueryCard] = None
    qPlugin: Optional[QPluginCard] = None
    fileUpload: Optional[FileUploadCard] = None
    formInput: Optional[FormInputCard] = None


class QQueryCardInput(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    outputSource: Optional[CardOutputSourceType] = None
    attributeFilter: Optional[AttributeFilter] = None


class AppDefinitionInputOutput(BaseValidatorModel):
    cards: List[CardInputOutput]
    initialPrompt: Optional[str] = None


class AppDefinition(BaseValidatorModel):
    appDefinitionVersion: str
    cards: List[Card]
    canEdit: Optional[bool] = None


class CardInput(BaseValidatorModel):
    textInput: Optional[TextInputCardInput] = None
    qQuery: Optional[QQueryCardInput] = None
    qPlugin: Optional[QPluginCardInput] = None
    fileUpload: Optional[FileUploadCardInput] = None
    formInput: Optional[FormInputCardInput] = None


class PredictAppDefinition(BaseValidatorModel):
    title: str
    appDefinition: AppDefinitionInputOutput
    description: Optional[str] = None


class GetQAppOutput(BaseValidatorModel):
    appId: str
    appArn: str
    title: str
    description: str
    initialPrompt: str
    appVersion: int
    status: AppStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    requiredCapabilities: List[AppRequiredCapabilityType]
    appDefinition: AppDefinition
    ResponseMetadata: ResponseMetadata


class AppDefinitionInput(BaseValidatorModel):
    cards: List[CardInput]
    initialPrompt: Optional[str] = None


class PredictQAppOutput(BaseValidatorModel):
    app: PredictAppDefinition
    problemStatement: str
    ResponseMetadata: ResponseMetadata

AppDefinitionInputUnion = Union[AppDefinitionInput, AppDefinitionInputOutput]


class CreateQAppInput(BaseValidatorModel):
    instanceId: str
    title: str
    appDefinition: AppDefinitionInputUnion
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateQAppInput(BaseValidatorModel):
    instanceId: str
    appId: str
    title: Optional[str] = None
    description: Optional[str] = None
    appDefinition: Optional[AppDefinitionInputUnion] = None