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
from aws_resource_validator.pydantic_models.qapps_constants import *

class AssociateLibraryItemReviewInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str

class AssociateQAppWithUserInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str

class FileUploadCardInputTypeDef(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    filename: Optional[str] = None
    fileId: Optional[str] = None
    allowOverride: Optional[bool] = None

class QPluginCardInputTypeDef(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    pluginId: str

class QQueryCardInputTypeDef(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    prompt: str
    outputSource: Optional[CardOutputSourceType] = None
    attributeFilter: Optional["AttributeFilterOutputTypeDef"] = None

class TextInputCardInputTypeDef(BaseValidatorModel):
    title: str
    id: str
    type: CardTypeType
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None

class CardStatusTypeDef(BaseValidatorModel):
    currentState: ExecutionStatusType
    currentValue: str

class FileUploadCardTypeDef(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    filename: Optional[str] = None
    fileId: Optional[str] = None
    allowOverride: Optional[bool] = None

class QPluginCardTypeDef(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    prompt: str
    pluginType: PluginTypeType
    pluginId: str

class QQueryCardTypeDef(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    prompt: str
    outputSource: CardOutputSourceType
    attributeFilter: Optional["AttributeFilterOutputTypeDef"] = None

class TextInputCardTypeDef(BaseValidatorModel):
    id: str
    title: str
    dependencies: List[str]
    type: CardTypeType
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None

class CardValueTypeDef(BaseValidatorModel):
    cardId: str
    value: str

class CategoryTypeDef(BaseValidatorModel):
    id: str
    title: str

class ConversationMessageTypeDef(BaseValidatorModel):
    body: str
    type: SenderType

class CreateLibraryItemInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: int
    categories: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteLibraryItemInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str

class DeleteQAppInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str

class DisassociateLibraryItemReviewInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str

class DisassociateQAppFromUserInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str

class DocumentAttributeValueOutputTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None

class GetLibraryItemInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    appId: Optional[str] = None

class GetQAppInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str

class GetQAppSessionInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str

class ImportDocumentInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    cardId: str
    appId: str
    fileContentsBase64: str
    fileName: str
    scope: DocumentScopeType
    sessionId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListLibraryItemsInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None
    categoryId: Optional[str] = None

class ListQAppsInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class UserAppItemTypeDef(BaseValidatorModel):
    appId: str
    appArn: str
    title: str
    createdAt: datetime
    description: Optional[str] = None
    canEdit: Optional[bool] = None
    status: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str

class StopQAppSessionInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateLibraryItemInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    status: Optional[LibraryItemStatusType] = None
    categories: Optional[Sequence[str]] = None

class CardInputTypeDef(BaseValidatorModel):
    textInput: Optional[TextInputCardInputTypeDef] = None
    qQuery: Optional[QQueryCardInputTypeDef] = None
    qPlugin: Optional[QPluginCardInputTypeDef] = None
    fileUpload: Optional[FileUploadCardInputTypeDef] = None

class CardTypeDef(BaseValidatorModel):
    textInput: Optional[TextInputCardTypeDef] = None
    qQuery: Optional[QQueryCardTypeDef] = None
    qPlugin: Optional[QPluginCardTypeDef] = None
    fileUpload: Optional[FileUploadCardTypeDef] = None

class StartQAppSessionInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: int
    initialValues: Optional[Sequence[CardValueTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateQAppSessionInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str
    values: Optional[Sequence[CardValueTypeDef]] = None

class LibraryItemMemberTypeDef(BaseValidatorModel):
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

class PredictQAppInputOptionsTypeDef(BaseValidatorModel):
    conversation: Optional[Sequence[ConversationMessageTypeDef]] = None
    problemStatement: Optional[str] = None

class CreateLibraryItemOutputTypeDef(BaseValidatorModel):
    libraryItemId: str
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQAppOutputTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetLibraryItemOutputTypeDef(BaseValidatorModel):
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

class GetQAppSessionOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    status: ExecutionStatusType
    cardStatus: Dict[str, CardStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportDocumentOutputTypeDef(BaseValidatorModel):
    fileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartQAppSessionOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLibraryItemOutputTypeDef(BaseValidatorModel):
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

class UpdateQAppOutputTypeDef(BaseValidatorModel):
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

class UpdateQAppSessionOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentAttributeOutputTypeDef(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueOutputTypeDef

class ListLibraryItemsInputListLibraryItemsPaginateTypeDef(BaseValidatorModel):
    instanceId: str
    categoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQAppsInputListQAppsPaginateTypeDef(BaseValidatorModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQAppsOutputTypeDef(BaseValidatorModel):
    apps: List[UserAppItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppDefinitionInputOutputTypeDef(BaseValidatorModel):
    cards: List[CardInputTypeDef]
    initialPrompt: Optional[str] = None

class AppDefinitionInputTypeDef(BaseValidatorModel):
    cards: Sequence[CardInputTypeDef]
    initialPrompt: Optional[str] = None

class AppDefinitionTypeDef(BaseValidatorModel):
    appDefinitionVersion: str
    cards: List[CardTypeDef]
    canEdit: Optional[bool] = None

class ListLibraryItemsOutputTypeDef(BaseValidatorModel):
    libraryItems: List[LibraryItemMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PredictQAppInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    options: Optional[PredictQAppInputOptionsTypeDef] = None

class AttributeFilterOutputTypeDef(BaseValidatorModel):
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

class PredictAppDefinitionTypeDef(BaseValidatorModel):
    title: str
    appDefinition: AppDefinitionInputOutputTypeDef
    description: Optional[str] = None

class CreateQAppInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    title: str
    appDefinition: AppDefinitionInputTypeDef
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateQAppInputRequestTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    title: Optional[str] = None
    description: Optional[str] = None
    appDefinition: Optional[AppDefinitionInputTypeDef] = None

class GetQAppOutputTypeDef(BaseValidatorModel):
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

class PredictQAppOutputTypeDef(BaseValidatorModel):
    app: PredictAppDefinitionTypeDef
    problemStatement: str
    ResponseMetadata: ResponseMetadataTypeDef

