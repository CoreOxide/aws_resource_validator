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
from aws_resource_validator.pydantic_models.connectcases_constants import *

class AuditEventFieldValueUnionTypeDef(BaseModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class UserUnionTypeDef(BaseModel):
    userArn: Optional[str] = None

class FieldIdentifierTypeDef(BaseModel):
    id: str

class FieldErrorTypeDef(BaseModel):
    errorCode: str
    id: str
    message: Optional[str] = None

class GetFieldResponseTypeDef(BaseModel):
    fieldArn: str
    fieldId: str
    name: str
    namespace: FieldNamespaceType
    type: FieldTypeType
    createdTime: Optional[datetime] = None
    deleted: Optional[bool] = None
    description: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class FieldOptionTypeDef(BaseModel):
    active: bool
    name: str
    value: str

class FieldOptionErrorTypeDef(BaseModel):
    errorCode: str
    message: str
    value: str

class CaseSummaryTypeDef(BaseModel):
    caseId: str
    templateId: str

class CommentContentTypeDef(BaseModel):
    body: str
    contentType: Literal["Text/Plain"]

class ContactContentTypeDef(BaseModel):
    channel: str
    connectedToSystemTime: datetime
    contactArn: str

class ContactFilterTypeDef(BaseModel):
    channel: Optional[Sequence[str]] = None
    contactArn: Optional[str] = None

class ContactTypeDef(BaseModel):
    contactArn: str

class CreateDomainRequestRequestTypeDef(BaseModel):
    name: str

class CreateFieldRequestRequestTypeDef(BaseModel):
    domainId: str
    name: str
    type: FieldTypeType
    description: Optional[str] = None

class LayoutConfigurationTypeDef(BaseModel):
    defaultLayout: Optional[str] = None

class RequiredFieldTypeDef(BaseModel):
    fieldId: str

class DeleteDomainRequestRequestTypeDef(BaseModel):
    domainId: str

class DeleteFieldRequestRequestTypeDef(BaseModel):
    domainId: str
    fieldId: str

class DeleteLayoutRequestRequestTypeDef(BaseModel):
    domainId: str
    layoutId: str

class DeleteTemplateRequestRequestTypeDef(BaseModel):
    domainId: str
    templateId: str

class DomainSummaryTypeDef(BaseModel):
    domainArn: str
    domainId: str
    name: str

class RelatedItemEventIncludedDataTypeDef(BaseModel):
    includeContent: bool

class FieldItemTypeDef(BaseModel):
    id: str

class FieldSummaryTypeDef(BaseModel):
    fieldArn: str
    fieldId: str
    name: str
    namespace: FieldNamespaceType
    type: FieldTypeType

class FieldValueUnionExtraOutputTypeDef(BaseModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class FieldValueUnionOutputTypeDef(BaseModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class FieldValueUnionTypeDef(BaseModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Mapping[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class FileContentTypeDef(BaseModel):
    fileArn: str

class FileFilterTypeDef(BaseModel):
    fileArn: Optional[str] = None

class GetCaseAuditEventsRequestRequestTypeDef(BaseModel):
    caseId: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetCaseEventConfigurationRequestRequestTypeDef(BaseModel):
    domainId: str

class GetDomainRequestRequestTypeDef(BaseModel):
    domainId: str

class GetLayoutRequestRequestTypeDef(BaseModel):
    domainId: str
    layoutId: str

class GetTemplateRequestRequestTypeDef(BaseModel):
    domainId: str
    templateId: str

class LayoutSummaryTypeDef(BaseModel):
    layoutArn: str
    layoutId: str
    name: str

class ListCasesForContactRequestRequestTypeDef(BaseModel):
    contactArn: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFieldOptionsRequestRequestTypeDef(BaseModel):
    domainId: str
    fieldId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    values: Optional[Sequence[str]] = None

class ListFieldsRequestRequestTypeDef(BaseModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLayoutsRequestRequestTypeDef(BaseModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    arn: str

class ListTemplatesRequestRequestTypeDef(BaseModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[Sequence[TemplateStatusType]] = None

class TemplateSummaryTypeDef(BaseModel):
    name: str
    status: TemplateStatusType
    templateArn: str
    templateId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SortTypeDef(BaseModel):
    fieldId: str
    sortOrder: OrderType

class TagResourceRequestRequestTypeDef(BaseModel):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    arn: str
    tagKeys: Sequence[str]

class UpdateFieldRequestRequestTypeDef(BaseModel):
    domainId: str
    fieldId: str
    description: Optional[str] = None
    name: Optional[str] = None

class AuditEventFieldTypeDef(BaseModel):
    eventFieldId: str
    newValue: AuditEventFieldValueUnionTypeDef
    oldValue: Optional[AuditEventFieldValueUnionTypeDef] = None

class AuditEventPerformedByTypeDef(BaseModel):
    iamPrincipalArn: str
    user: Optional[UserUnionTypeDef] = None

class BatchGetFieldRequestRequestTypeDef(BaseModel):
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]

class CaseEventIncludedDataOutputTypeDef(BaseModel):
    fields: List[FieldIdentifierTypeDef]

class CaseEventIncludedDataTypeDef(BaseModel):
    fields: Sequence[FieldIdentifierTypeDef]

class GetCaseRequestRequestTypeDef(BaseModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]
    nextToken: Optional[str] = None

class BatchGetFieldResponseTypeDef(BaseModel):
    errors: List[FieldErrorTypeDef]
    fields: List[GetFieldResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseResponseTypeDef(BaseModel):
    caseArn: str
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseModel):
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldResponseTypeDef(BaseModel):
    fieldArn: str
    fieldId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayoutResponseTypeDef(BaseModel):
    layoutArn: str
    layoutId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelatedItemResponseTypeDef(BaseModel):
    relatedItemArn: str
    relatedItemId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(BaseModel):
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainResponseTypeDef(BaseModel):
    createdTime: datetime
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutFieldOptionsRequestRequestTypeDef(BaseModel):
    domainId: str
    fieldId: str
    options: Sequence[FieldOptionTypeDef]

class ListFieldOptionsResponseTypeDef(BaseModel):
    nextToken: str
    options: List[FieldOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutFieldOptionsResponseTypeDef(BaseModel):
    errors: List[FieldOptionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCasesForContactResponseTypeDef(BaseModel):
    cases: List[CaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateRequestRequestTypeDef(BaseModel):
    domainId: str
    name: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfigurationTypeDef] = None
    requiredFields: Optional[Sequence[RequiredFieldTypeDef]] = None
    status: Optional[TemplateStatusType] = None

class GetTemplateResponseTypeDef(BaseModel):
    createdTime: datetime
    deleted: bool
    description: str
    lastModifiedTime: datetime
    layoutConfiguration: LayoutConfigurationTypeDef
    name: str
    requiredFields: List[RequiredFieldTypeDef]
    status: TemplateStatusType
    tags: Dict[str, str]
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateRequestRequestTypeDef(BaseModel):
    domainId: str
    templateId: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfigurationTypeDef] = None
    name: Optional[str] = None
    requiredFields: Optional[Sequence[RequiredFieldTypeDef]] = None
    status: Optional[TemplateStatusType] = None

class ListDomainsResponseTypeDef(BaseModel):
    domains: List[DomainSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldGroupOutputTypeDef(BaseModel):
    fields: List[FieldItemTypeDef]
    name: Optional[str] = None

class FieldGroupTypeDef(BaseModel):
    fields: Sequence[FieldItemTypeDef]
    name: Optional[str] = None

class ListFieldsResponseTypeDef(BaseModel):
    fields: List[FieldSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldValueExtraOutputTypeDef(BaseModel):
    id: str
    value: FieldValueUnionExtraOutputTypeDef

class FieldValueOutputTypeDef(BaseModel):
    id: str
    value: FieldValueUnionOutputTypeDef

class FieldValueTypeDef(BaseModel):
    id: str
    value: FieldValueUnionTypeDef

class RelatedItemContentTypeDef(BaseModel):
    comment: Optional[CommentContentTypeDef] = None
    contact: Optional[ContactContentTypeDef] = None
    file: Optional[FileContentTypeDef] = None

class RelatedItemInputContentTypeDef(BaseModel):
    comment: Optional[CommentContentTypeDef] = None
    contact: Optional[ContactTypeDef] = None
    file: Optional[FileContentTypeDef] = None

class RelatedItemTypeFilterTypeDef(BaseModel):
    comment: Optional[Mapping[str, Any]] = None
    contact: Optional[ContactFilterTypeDef] = None
    file: Optional[FileFilterTypeDef] = None

class ListLayoutsResponseTypeDef(BaseModel):
    layouts: List[LayoutSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplatesResponseTypeDef(BaseModel):
    nextToken: str
    templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchCasesRequestRequestTypeDef(BaseModel):
    domainId: str
    fields: Optional[Sequence[FieldIdentifierTypeDef]] = None
    filter: Optional["CaseFilterTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchTerm: Optional[str] = None
    sorts: Optional[Sequence[SortTypeDef]] = None

class AuditEventTypeDef(BaseModel):
    eventId: str
    fields: List[AuditEventFieldTypeDef]
    performedTime: datetime
    type: AuditEventTypeType
    performedBy: Optional[AuditEventPerformedByTypeDef] = None
    relatedItemType: Optional[RelatedItemTypeType] = None

class EventIncludedDataOutputTypeDef(BaseModel):
    caseData: Optional[CaseEventIncludedDataOutputTypeDef] = None
    relatedItemData: Optional[RelatedItemEventIncludedDataTypeDef] = None

class EventIncludedDataTypeDef(BaseModel):
    caseData: Optional[CaseEventIncludedDataTypeDef] = None
    relatedItemData: Optional[RelatedItemEventIncludedDataTypeDef] = None

class SectionOutputTypeDef(BaseModel):
    fieldGroup: Optional[FieldGroupOutputTypeDef] = None

class SectionTypeDef(BaseModel):
    fieldGroup: Optional[FieldGroupTypeDef] = None

class GetCaseResponseTypeDef(BaseModel):
    fields: List[FieldValueOutputTypeDef]
    nextToken: str
    tags: Dict[str, str]
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchCasesResponseItemTypeDef(BaseModel):
    caseId: str
    fields: List[FieldValueOutputTypeDef]
    templateId: str
    tags: Optional[Dict[str, str]] = None

class FieldFilterTypeDef(BaseModel):
    contains: Optional[FieldValueTypeDef] = None
    equalTo: Optional[FieldValueTypeDef] = None
    greaterThan: Optional[FieldValueTypeDef] = None
    greaterThanOrEqualTo: Optional[FieldValueTypeDef] = None
    lessThan: Optional[FieldValueTypeDef] = None
    lessThanOrEqualTo: Optional[FieldValueTypeDef] = None

class SearchRelatedItemsResponseItemTypeDef(BaseModel):
    associationTime: datetime
    content: RelatedItemContentTypeDef
    relatedItemId: str
    type: RelatedItemTypeType
    performedBy: Optional[UserUnionTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateRelatedItemRequestRequestTypeDef(BaseModel):
    caseId: str
    content: RelatedItemInputContentTypeDef
    domainId: str
    type: RelatedItemTypeType
    performedBy: Optional[UserUnionTypeDef] = None

class SearchRelatedItemsRequestRequestTypeDef(BaseModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef(BaseModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCaseAuditEventsResponseTypeDef(BaseModel):
    auditEvents: List[AuditEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventBridgeConfigurationOutputTypeDef(BaseModel):
    enabled: bool
    includedData: Optional[EventIncludedDataOutputTypeDef] = None

class EventBridgeConfigurationTypeDef(BaseModel):
    enabled: bool
    includedData: Optional[EventIncludedDataTypeDef] = None

class LayoutSectionsOutputTypeDef(BaseModel):
    sections: Optional[List[SectionOutputTypeDef]] = None

class LayoutSectionsTypeDef(BaseModel):
    sections: Optional[Sequence[SectionTypeDef]] = None

class SearchCasesResponseTypeDef(BaseModel):
    cases: List[SearchCasesResponseItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CaseFilterTypeDef(BaseModel):
    andAll: Optional[Sequence[Dict[str, Any]]] = None
    field: Optional[FieldFilterTypeDef] = None
    not: Optional[Dict[str, Any]] = None
    orAll: Optional[Sequence[Dict[str, Any]]] = None

class CreateCaseRequestRequestTypeDef(BaseModel):
    domainId: str
    fields: Sequence[FieldValueExtraUnionTypeDef]
    templateId: str
    clientToken: Optional[str] = None
    performedBy: Optional[UserUnionTypeDef] = None

class UpdateCaseRequestRequestTypeDef(BaseModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldValueExtraUnionTypeDef]
    performedBy: Optional[UserUnionTypeDef] = None

class SearchRelatedItemsResponseTypeDef(BaseModel):
    nextToken: str
    relatedItems: List[SearchRelatedItemsResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCaseEventConfigurationResponseTypeDef(BaseModel):
    eventBridge: EventBridgeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCaseEventConfigurationRequestRequestTypeDef(BaseModel):
    domainId: str
    eventBridge: EventBridgeConfigurationTypeDef

class BasicLayoutOutputTypeDef(BaseModel):
    moreInfo: Optional[LayoutSectionsOutputTypeDef] = None
    topPanel: Optional[LayoutSectionsOutputTypeDef] = None

class BasicLayoutTypeDef(BaseModel):
    moreInfo: Optional[LayoutSectionsTypeDef] = None
    topPanel: Optional[LayoutSectionsTypeDef] = None

class SearchCasesRequestSearchCasesPaginateTypeDef(BaseModel):
    domainId: str
    fields: Optional[Sequence[FieldIdentifierTypeDef]] = None
    filter: Optional[CaseFilterTypeDef] = None
    searchTerm: Optional[str] = None
    sorts: Optional[Sequence[SortTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LayoutContentOutputTypeDef(BaseModel):
    basic: Optional[BasicLayoutOutputTypeDef] = None

class LayoutContentTypeDef(BaseModel):
    basic: Optional[BasicLayoutTypeDef] = None

class GetLayoutResponseTypeDef(BaseModel):
    content: LayoutContentOutputTypeDef
    createdTime: datetime
    deleted: bool
    lastModifiedTime: datetime
    layoutArn: str
    layoutId: str
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayoutRequestRequestTypeDef(BaseModel):
    content: LayoutContentTypeDef
    domainId: str
    name: str

class UpdateLayoutRequestRequestTypeDef(BaseModel):
    domainId: str
    layoutId: str
    content: Optional[LayoutContentTypeDef] = None
    name: Optional[str] = None

