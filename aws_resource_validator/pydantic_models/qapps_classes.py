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
from aws_resource_validator.pydantic_models.qapps_constants import *

class AssociateLibraryItemReviewInputTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str


class AssociateQAppWithUserInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str


class BatchDeleteCategoryInputTypeDef(BaseValidatorModel):
    instanceId: str
    categories: Sequence[str]


class SubmissionTypeDef(BaseValidatorModel):
    value: Optional[Dict[str, Any]] = None
    submissionId: Optional[str] = None
    timestamp: Optional[datetime] = None


class SubmissionMutationTypeDef(BaseValidatorModel):
    submissionId: str
    mutationType: SubmissionMutationKindType


class CreateLibraryItemInputTypeDef(BaseValidatorModel):
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


class CreatePresignedUrlInputTypeDef(BaseValidatorModel):
    instanceId: str
    cardId: str
    appId: str
    fileContentsSha256: str
    fileName: str
    scope: DocumentScopeType
    sessionId: Optional[str] = None


class DeleteLibraryItemInputTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str


class DeleteQAppInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str


class DescribeQAppPermissionsInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str


class DisassociateLibraryItemReviewInputTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str


class DisassociateQAppFromUserInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str


class DocumentAttributeValueOutputTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None


class ExportQAppSessionDataInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str


class FormInputCardMetadataOutputTypeDef(BaseValidatorModel):
    schema: Dict[str, Any]


class FormInputCardMetadataTypeDef(BaseValidatorModel):
    schema: Mapping[str, Any]


class GetLibraryItemInputTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    appId: Optional[str] = None


class GetQAppInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: Optional[int] = None


class GetQAppSessionInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str


class GetQAppSessionMetadataInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str


class SessionSharingConfigurationTypeDef(BaseValidatorModel):
    enabled: bool
    acceptResponses: Optional[bool] = None
    revealCards: Optional[bool] = None


class ImportDocumentInputTypeDef(BaseValidatorModel):
    instanceId: str
    cardId: str
    appId: str
    fileContentsBase64: str
    fileName: str
    scope: DocumentScopeType
    sessionId: Optional[str] = None


class ListCategoriesInputTypeDef(BaseValidatorModel):
    instanceId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListLibraryItemsInputTypeDef(BaseValidatorModel):
    instanceId: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None
    categoryId: Optional[str] = None


class ListQAppSessionDataInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str


class ListQAppsInputTypeDef(BaseValidatorModel):
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
    isVerified: Optional[bool] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str


class PermissionInputTypeDef(BaseValidatorModel):
    action: PermissionInputActionEnumType
    principal: str


class PrincipalOutputTypeDef(BaseValidatorModel):
    userId: Optional[str] = None
    userType: Optional[PrincipalOutputUserTypeEnumType] = None
    email: Optional[str] = None


class UserTypeDef(BaseValidatorModel):
    userId: Optional[str] = None


class StopQAppSessionInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UpdateLibraryItemInputTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    status: Optional[LibraryItemStatusType] = None
    categories: Optional[Sequence[str]] = None


class UpdateLibraryItemMetadataInputTypeDef(BaseValidatorModel):
    instanceId: str
    libraryItemId: str
    isVerified: Optional[bool] = None


class BatchCreateCategoryInputCategoryTypeDef(BaseValidatorModel):
    pass


class BatchCreateCategoryInputTypeDef(BaseValidatorModel):
    instanceId: str
    categories: Sequence[BatchCreateCategoryInputCategoryTypeDef]


class CategoryInputTypeDef(BaseValidatorModel):
    pass


class BatchUpdateCategoryInputTypeDef(BaseValidatorModel):
    instanceId: str
    categories: Sequence[CategoryInputTypeDef]


class CardStatusTypeDef(BaseValidatorModel):
    currentState: ExecutionStatusType
    currentValue: str
    submissions: Optional[List[SubmissionTypeDef]] = None


class CardValueTypeDef(BaseValidatorModel):
    cardId: str
    value: str
    submissionMutation: Optional[SubmissionMutationTypeDef] = None


class CategoryTypeDef(BaseValidatorModel):
    pass


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
    isVerified: Optional[bool] = None


class ConversationMessageTypeDef(BaseValidatorModel):
    pass


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
    isVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePresignedUrlOutputTypeDef(BaseValidatorModel):
    fileId: str
    presignedUrl: str
    presignedUrlFields: Dict[str, str]
    presignedUrlExpiration: datetime
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


class ExportQAppSessionDataOutputTypeDef(BaseValidatorModel):
    csvFileLink: str
    expiresAt: datetime
    sessionArn: str
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
    isVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ImportDocumentOutputTypeDef(BaseValidatorModel):
    fileId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListCategoriesOutputTypeDef(BaseValidatorModel):
    categories: List[CategoryTypeDef]
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
    isVerified: bool
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


class TimestampTypeDef(BaseValidatorModel):
    pass


class DocumentAttributeValueTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[Sequence[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[TimestampTypeDef] = None


class GetQAppSessionMetadataOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionName: str
    sharingConfiguration: SessionSharingConfigurationTypeDef
    sessionOwner: bool
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateQAppSessionMetadataInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str
    sharingConfiguration: SessionSharingConfigurationTypeDef
    sessionName: Optional[str] = None


class UpdateQAppSessionMetadataOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionName: str
    sharingConfiguration: SessionSharingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLibraryItemsInputPaginateTypeDef(BaseValidatorModel):
    instanceId: str
    categoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQAppsInputPaginateTypeDef(BaseValidatorModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQAppsOutputTypeDef(BaseValidatorModel):
    apps: List[UserAppItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateQAppPermissionsInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    grantPermissions: Optional[Sequence[PermissionInputTypeDef]] = None
    revokePermissions: Optional[Sequence[PermissionInputTypeDef]] = None


class PermissionOutputTypeDef(BaseValidatorModel):
    action: PermissionOutputActionEnumType
    principal: PrincipalOutputTypeDef


class QAppSessionDataTypeDef(BaseValidatorModel):
    cardId: str
    user: UserTypeDef
    value: Optional[Dict[str, Any]] = None
    submissionId: Optional[str] = None
    timestamp: Optional[datetime] = None


class GetQAppSessionOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionName: str
    appVersion: int
    latestPublishedAppVersion: int
    status: ExecutionStatusType
    cardStatus: Dict[str, CardStatusTypeDef]
    userIsHost: bool
    ResponseMetadata: ResponseMetadataTypeDef


class StartQAppSessionInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    appVersion: int
    initialValues: Optional[Sequence[CardValueTypeDef]] = None
    sessionId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateQAppSessionInputTypeDef(BaseValidatorModel):
    instanceId: str
    sessionId: str
    values: Optional[Sequence[CardValueTypeDef]] = None


class ListLibraryItemsOutputTypeDef(BaseValidatorModel):
    libraryItems: List[LibraryItemMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PredictQAppInputTypeDef(BaseValidatorModel):
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


class DocumentAttributeTypeDef(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueTypeDef


class DescribeQAppPermissionsOutputTypeDef(BaseValidatorModel):
    resourceArn: str
    appId: str
    permissions: List[PermissionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateQAppPermissionsOutputTypeDef(BaseValidatorModel):
    resourceArn: str
    appId: str
    permissions: List[PermissionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListQAppSessionDataOutputTypeDef(BaseValidatorModel):
    sessionId: str
    sessionArn: str
    sessionData: List[QAppSessionDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AttributeFilterTypeDef(BaseValidatorModel):
    andAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    orAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    notFilter: Optional[Mapping[str, Any]] = None
    equalsTo: Optional[DocumentAttributeTypeDef] = None
    containsAll: Optional[DocumentAttributeTypeDef] = None
    containsAny: Optional[DocumentAttributeTypeDef] = None
    greaterThan: Optional[DocumentAttributeTypeDef] = None
    greaterThanOrEquals: Optional[DocumentAttributeTypeDef] = None
    lessThan: Optional[DocumentAttributeTypeDef] = None
    lessThanOrEquals: Optional[DocumentAttributeTypeDef] = None


class TextInputCardInputTypeDef(BaseValidatorModel):
    pass


class QPluginCardInputTypeDef(BaseValidatorModel):
    pass


class FormInputCardInputOutputTypeDef(BaseValidatorModel):
    pass


class QQueryCardInputOutputTypeDef(BaseValidatorModel):
    pass


class FileUploadCardInputTypeDef(BaseValidatorModel):
    pass


class CardInputOutputTypeDef(BaseValidatorModel):
    textInput: Optional[TextInputCardInputTypeDef] = None
    qQuery: Optional[QQueryCardInputOutputTypeDef] = None
    qPlugin: Optional[QPluginCardInputTypeDef] = None
    fileUpload: Optional[FileUploadCardInputTypeDef] = None
    formInput: Optional[FormInputCardInputOutputTypeDef] = None


class FileUploadCardTypeDef(BaseValidatorModel):
    pass


class QPluginCardTypeDef(BaseValidatorModel):
    pass


class QQueryCardTypeDef(BaseValidatorModel):
    pass


class FormInputCardTypeDef(BaseValidatorModel):
    pass


class TextInputCardTypeDef(BaseValidatorModel):
    pass


class CardTypeDef(BaseValidatorModel):
    textInput: Optional[TextInputCardTypeDef] = None
    qQuery: Optional[QQueryCardTypeDef] = None
    qPlugin: Optional[QPluginCardTypeDef] = None
    fileUpload: Optional[FileUploadCardTypeDef] = None
    formInput: Optional[FormInputCardTypeDef] = None


class AppDefinitionInputOutputTypeDef(BaseValidatorModel):
    cards: List[CardInputOutputTypeDef]
    initialPrompt: Optional[str] = None


class AppDefinitionTypeDef(BaseValidatorModel):
    appDefinitionVersion: str
    cards: List[CardTypeDef]
    canEdit: Optional[bool] = None


class FormInputCardInputTypeDef(BaseValidatorModel):
    pass


class QQueryCardInputTypeDef(BaseValidatorModel):
    pass


class CardInputTypeDef(BaseValidatorModel):
    textInput: Optional[TextInputCardInputTypeDef] = None
    qQuery: Optional[QQueryCardInputTypeDef] = None
    qPlugin: Optional[QPluginCardInputTypeDef] = None
    fileUpload: Optional[FileUploadCardInputTypeDef] = None
    formInput: Optional[FormInputCardInputTypeDef] = None


class PredictAppDefinitionTypeDef(BaseValidatorModel):
    title: str
    appDefinition: AppDefinitionInputOutputTypeDef
    description: Optional[str] = None


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


class AppDefinitionInputTypeDef(BaseValidatorModel):
    cards: Sequence[CardInputTypeDef]
    initialPrompt: Optional[str] = None


class PredictQAppOutputTypeDef(BaseValidatorModel):
    app: PredictAppDefinitionTypeDef
    problemStatement: str
    ResponseMetadata: ResponseMetadataTypeDef


class AppDefinitionInputUnionTypeDef(BaseValidatorModel):
    pass


class CreateQAppInputTypeDef(BaseValidatorModel):
    instanceId: str
    title: str
    appDefinition: AppDefinitionInputUnionTypeDef
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateQAppInputTypeDef(BaseValidatorModel):
    instanceId: str
    appId: str
    title: Optional[str] = None
    description: Optional[str] = None
    appDefinition: Optional[AppDefinitionInputUnionTypeDef] = None


