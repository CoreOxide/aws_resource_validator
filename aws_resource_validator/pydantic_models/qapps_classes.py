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
from aws_resource_validator.pydantic_models.qapps_constants import *

class AssociateLibraryItemReviewInputRequestTypeDef(BaseModel):
    instanceId: str
    libraryItemId: str

class AssociateQAppWithUserInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str

class FileUploadCardInputTypeDef(BaseModel):
    title: str
    id: str
    type: CardTypeType
    filename: Optional[str] = None
    fileId: Optional[str] = None
    allowOverride: Optional[bool] = None

class QPluginCardInputTypeDef(BaseModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    pluginId: str

class QQueryCardInputTypeDef(BaseModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    outputSource: Optional[CardOutputSourceType] = None
    attributeFilter: Optional["AttributeFilterOutputTypeDef"] = None

class TextInputCardInputTypeDef(BaseModel):
    title: str
    id: str
    type: CardTypeType
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None

class CardStatusTypeDef(BaseModel):
    currentState: ExecutionStatusType
    currentValue: str

class FileUploadCardTypeDef(BaseModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    filename: Optional[str] = None
    fileId: Optional[str] = None
    allowOverride: Optional[bool] = None

class QPluginCardTypeDef(BaseModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    prompt: str
    pluginType: PluginTypeType
    pluginId: str

class QQueryCardTypeDef(BaseModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    prompt: str
    outputSource: CardOutputSourceType
    attributeFilter: Optional["AttributeFilterOutputTypeDef"] = None

class TextInputCardTypeDef(BaseModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None

class CardValueTypeDef(BaseModel):
    cardId: str
    value: str

class CategoryTypeDef(BaseModel):
    id: str
    title: str

class ConversationMessageTypeDef(BaseModel):
    body: str
    type: SenderType

class CreateLibraryItemInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str
    appVersion: int
    categories: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteLibraryItemInputRequestTypeDef(BaseModel):
    instanceId: str
    libraryItemId: str

class DeleteQAppInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str

class DisassociateLibraryItemReviewInputRequestTypeDef(BaseModel):
    instanceId: str
    libraryItemId: str

class DisassociateQAppFromUserInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str

class DocumentAttributeValueOutputTypeDef(BaseModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None

class GetLibraryItemInputRequestTypeDef(BaseModel):
    instanceId: str
    libraryItemId: str
    appId: Optional[str] = None

class GetQAppInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str

class GetQAppSessionInputRequestTypeDef(BaseModel):
    instanceId: str
    sessionId: str

class ImportDocumentInputRequestTypeDef(BaseModel):
    instanceId: str
    cardId: str
    appId: str
    fileContentsBase64: str
    fileName: str
    scope: DocumentScopeType
    sessionId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListLibraryItemsInputRequestTypeDef(BaseModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None
    categoryId: Optional[str] = None

class ListQAppsInputRequestTypeDef(BaseModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class UserAppItemTypeDef(BaseModel):
    appId: str
    appArn: str
    title: str
    createdAt: datetime
    description: Optional[str] = None
    canEdit: Optional[bool] = None
    status: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str

class StopQAppSessionInputRequestTypeDef(BaseModel):
    instanceId: str
    sessionId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateLibraryItemInputRequestTypeDef(BaseModel):
    instanceId: str
    libraryItemId: str
    status: Optional[LibraryItemStatusType] = None
    categories: Optional[Sequence[str]] = None

class CardInputTypeDef(BaseModel):
    textInput: Optional[TextInputCardInputTypeDef] = None
    qQuery: Optional[QQueryCardInputTypeDef] = None
    qPlugin: Optional[QPluginCardInputTypeDef] = None
    fileUpload: Optional[FileUploadCardInputTypeDef] = None

class CardTypeDef(BaseModel):
    textInput: Optional[TextInputCardTypeDef] = None
    qQuery: Optional[QQueryCardTypeDef] = None
    qPlugin: Optional[QPluginCardTypeDef] = None
    fileUpload: Optional[FileUploadCardTypeDef] = None

class StartQAppSessionInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str
    appVersion: int
    initialValues: Optional[Sequence[CardValueTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateQAppSessionInputRequestTypeDef(BaseModel):
    instanceId: str
    sessionId: str
    values: Optional[Sequence[CardValueTypeDef]] = None

class LibraryItemMemberTypeDef(BaseModel):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[CategoryTypeDef]
    status: str
    createdAt: datetime
    createdBy: str
    ratingCount: int
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    isRatedByUser: Optional[bool] = None
    userCount: Optional[int] = None

class PredictQAppInputOptionsTypeDef(BaseModel):
    conversation: Optional[Sequence[ConversationMessageTypeDef]] = None
    problemStatement: Optional[str] = None

class CreateLibraryItemOutputTypeDef(BaseModel):
    libraryItemId: str
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQAppOutputTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetLibraryItemOutputTypeDef(BaseModel):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[CategoryTypeDef]
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isRatedByUser: bool
    userCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetQAppSessionOutputTypeDef(BaseModel):
    sessionId: str
    sessionArn: str
    status: ExecutionStatusType
    cardStatus: Dict[str, CardStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportDocumentOutputTypeDef(BaseModel):
    fileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartQAppSessionOutputTypeDef(BaseModel):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLibraryItemOutputTypeDef(BaseModel):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[CategoryTypeDef]
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isRatedByUser: bool
    userCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQAppOutputTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQAppSessionOutputTypeDef(BaseModel):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentAttributeOutputTypeDef(BaseModel):
    name: str
    value: DocumentAttributeValueOutputTypeDef

class ListLibraryItemsInputListLibraryItemsPaginateTypeDef(BaseModel):
    instanceId: str
    categoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQAppsInputListQAppsPaginateTypeDef(BaseModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQAppsOutputTypeDef(BaseModel):
    apps: List[UserAppItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppDefinitionInputOutputTypeDef(BaseModel):
    cards: List[CardInputTypeDef]
    initialPrompt: Optional[str] = None

class AppDefinitionInputTypeDef(BaseModel):
    cards: Sequence[CardInputTypeDef]
    initialPrompt: Optional[str] = None

class AppDefinitionTypeDef(BaseModel):
    appDefinitionVersion: str
    cards: List[CardTypeDef]
    canEdit: Optional[bool] = None

class ListLibraryItemsOutputTypeDef(BaseModel):
    libraryItems: List[LibraryItemMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PredictQAppInputRequestTypeDef(BaseModel):
    instanceId: str
    options: Optional[PredictQAppInputOptionsTypeDef] = None

class AttributeFilterOutputTypeDef(BaseModel):
    andAllFilters: Optional[List[Dict[str, Any]]] = None
    orAllFilters: Optional[List[Dict[str, Any]]] = None
    notFilter: Optional[Dict[str, Any]] = None
    equalsTo: Optional[DocumentAttributeOutputTypeDef] = None
    containsAll: Optional[DocumentAttributeOutputTypeDef] = None
    containsAny: Optional[DocumentAttributeOutputTypeDef] = None
    greaterThan: Optional[DocumentAttributeOutputTypeDef] = None
    greaterThanOrEquals: Optional[DocumentAttributeOutputTypeDef] = None
    lessThan: Optional[DocumentAttributeOutputTypeDef] = None
    lessThanOrEquals: Optional[DocumentAttributeOutputTypeDef] = None

class PredictAppDefinitionTypeDef(BaseModel):
    title: str
    appDefinition: AppDefinitionInputOutputTypeDef
    description: Optional[str] = None

class CreateQAppInputRequestTypeDef(BaseModel):
    instanceId: str
    title: str
    appDefinition: AppDefinitionInputTypeDef
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateQAppInputRequestTypeDef(BaseModel):
    instanceId: str
    appId: str
    title: Optional[str] = None
    description: Optional[str] = None
    appDefinition: Optional[AppDefinitionInputTypeDef] = None

class GetQAppOutputTypeDef(BaseModel):
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
    appDefinition: AppDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PredictQAppOutputTypeDef(BaseModel):
    app: PredictAppDefinitionTypeDef
    problemStatement: str
    ResponseMetadata: ResponseMetadataTypeDef

