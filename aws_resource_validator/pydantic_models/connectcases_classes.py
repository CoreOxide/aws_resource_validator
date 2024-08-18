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
from aws_resource_validator.pydantic_models.connectcases_constants import *

class AuditEventFieldValueUnionTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class UserUnionTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None

class FieldIdentifierTypeDef(BaseValidatorModel):
    id: str

class FieldErrorTypeDef(BaseValidatorModel):
    errorCode: str
    id: str
    message: Optional[str] = None

class GetFieldResponseTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class FieldOptionTypeDef(BaseValidatorModel):
    active: bool
    name: str
    value: str

class FieldOptionErrorTypeDef(BaseValidatorModel):
    errorCode: str
    message: str
    value: str

class CaseSummaryTypeDef(BaseValidatorModel):
    caseId: str
    templateId: str

class CommentContentTypeDef(BaseValidatorModel):
    body: str
    contentType: Literal["Text/Plain"]

class ContactContentTypeDef(BaseValidatorModel):
    channel: str
    connectedToSystemTime: datetime
    contactArn: str

class ContactFilterTypeDef(BaseValidatorModel):
    channel: Optional[Sequence[str]] = None
    contactArn: Optional[str] = None

class ContactTypeDef(BaseValidatorModel):
    contactArn: str

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
    name: str

class CreateFieldRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    name: str
    type: FieldTypeType
    description: Optional[str] = None

class LayoutConfigurationTypeDef(BaseValidatorModel):
    defaultLayout: Optional[str] = None

class RequiredFieldTypeDef(BaseValidatorModel):
    fieldId: str

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    domainId: str

class DeleteFieldRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str

class DeleteLayoutRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    layoutId: str

class DeleteTemplateRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    templateId: str

class DomainSummaryTypeDef(BaseValidatorModel):
    domainArn: str
    domainId: str
    name: str

class RelatedItemEventIncludedDataTypeDef(BaseValidatorModel):
    includeContent: bool

class FieldItemTypeDef(BaseValidatorModel):
    id: str

class FieldSummaryTypeDef(BaseValidatorModel):
    fieldArn: str
    fieldId: str
    name: str
    namespace: FieldNamespaceType
    type: FieldTypeType

class FieldValueUnionExtraOutputTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class FieldValueUnionOutputTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class FieldValueUnionTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Mapping[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None

class FileContentTypeDef(BaseValidatorModel):
    fileArn: str

class FileFilterTypeDef(BaseValidatorModel):
    fileArn: Optional[str] = None

class GetCaseAuditEventsRequestRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetCaseEventConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domainId: str

class GetDomainRequestRequestTypeDef(BaseValidatorModel):
    domainId: str

class GetLayoutRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    layoutId: str

class GetTemplateRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    templateId: str

class LayoutSummaryTypeDef(BaseValidatorModel):
    layoutArn: str
    layoutId: str
    name: str

class ListCasesForContactRequestRequestTypeDef(BaseValidatorModel):
    contactArn: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFieldOptionsRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    values: Optional[Sequence[str]] = None

class ListFieldsRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLayoutsRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class ListTemplatesRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[Sequence[TemplateStatusType]] = None

class TemplateSummaryTypeDef(BaseValidatorModel):
    name: str
    status: TemplateStatusType
    templateArn: str
    templateId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SortTypeDef(BaseValidatorModel):
    fieldId: str
    sortOrder: OrderType

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]

class UpdateFieldRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str
    description: Optional[str] = None
    name: Optional[str] = None

class AuditEventFieldTypeDef(BaseValidatorModel):
    eventFieldId: str
    newValue: AuditEventFieldValueUnionTypeDef
    oldValue: Optional[AuditEventFieldValueUnionTypeDef] = None

class AuditEventPerformedByTypeDef(BaseValidatorModel):
    iamPrincipalArn: str
    user: Optional[UserUnionTypeDef] = None

class BatchGetFieldRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]

class CaseEventIncludedDataOutputTypeDef(BaseValidatorModel):
    fields: List[FieldIdentifierTypeDef]

class CaseEventIncludedDataTypeDef(BaseValidatorModel):
    fields: Sequence[FieldIdentifierTypeDef]

class GetCaseRequestRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]
    nextToken: Optional[str] = None

class BatchGetFieldResponseTypeDef(BaseValidatorModel):
    errors: List[FieldErrorTypeDef]
    fields: List[GetFieldResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseResponseTypeDef(BaseValidatorModel):
    caseArn: str
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseValidatorModel):
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldResponseTypeDef(BaseValidatorModel):
    fieldArn: str
    fieldId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayoutResponseTypeDef(BaseValidatorModel):
    layoutArn: str
    layoutId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelatedItemResponseTypeDef(BaseValidatorModel):
    relatedItemArn: str
    relatedItemId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(BaseValidatorModel):
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainResponseTypeDef(BaseValidatorModel):
    createdTime: datetime
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutFieldOptionsRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str
    options: Sequence[FieldOptionTypeDef]

class ListFieldOptionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    options: List[FieldOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutFieldOptionsResponseTypeDef(BaseValidatorModel):
    errors: List[FieldOptionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCasesForContactResponseTypeDef(BaseValidatorModel):
    cases: List[CaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    name: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfigurationTypeDef] = None
    requiredFields: Optional[Sequence[RequiredFieldTypeDef]] = None
    status: Optional[TemplateStatusType] = None

class GetTemplateResponseTypeDef(BaseValidatorModel):
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

class UpdateTemplateRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    templateId: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfigurationTypeDef] = None
    name: Optional[str] = None
    requiredFields: Optional[Sequence[RequiredFieldTypeDef]] = None
    status: Optional[TemplateStatusType] = None

class ListDomainsResponseTypeDef(BaseValidatorModel):
    domains: List[DomainSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldGroupOutputTypeDef(BaseValidatorModel):
    fields: List[FieldItemTypeDef]
    name: Optional[str] = None

class FieldGroupTypeDef(BaseValidatorModel):
    fields: Sequence[FieldItemTypeDef]
    name: Optional[str] = None

class ListFieldsResponseTypeDef(BaseValidatorModel):
    fields: List[FieldSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldValueExtraOutputTypeDef(BaseValidatorModel):
    id: str
    value: FieldValueUnionExtraOutputTypeDef

class FieldValueOutputTypeDef(BaseValidatorModel):
    id: str
    value: FieldValueUnionOutputTypeDef

class FieldValueTypeDef(BaseValidatorModel):
    id: str
    value: FieldValueUnionTypeDef

class RelatedItemContentTypeDef(BaseValidatorModel):
    comment: Optional[CommentContentTypeDef] = None
    contact: Optional[ContactContentTypeDef] = None
    file: Optional[FileContentTypeDef] = None

class RelatedItemInputContentTypeDef(BaseValidatorModel):
    comment: Optional[CommentContentTypeDef] = None
    contact: Optional[ContactTypeDef] = None
    file: Optional[FileContentTypeDef] = None

class RelatedItemTypeFilterTypeDef(BaseValidatorModel):
    comment: Optional[Mapping[str, Any]] = None
    contact: Optional[ContactFilterTypeDef] = None
    file: Optional[FileFilterTypeDef] = None

class ListLayoutsResponseTypeDef(BaseValidatorModel):
    layouts: List[LayoutSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplatesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchCasesRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fields: Optional[Sequence[FieldIdentifierTypeDef]] = None
    filter: Optional["CaseFilterTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchTerm: Optional[str] = None
    sorts: Optional[Sequence[SortTypeDef]] = None

class AuditEventTypeDef(BaseValidatorModel):
    eventId: str
    fields: List[AuditEventFieldTypeDef]
    performedTime: datetime
    type: AuditEventTypeType
    performedBy: Optional[AuditEventPerformedByTypeDef] = None
    relatedItemType: Optional[RelatedItemTypeType] = None

class EventIncludedDataOutputTypeDef(BaseValidatorModel):
    caseData: Optional[CaseEventIncludedDataOutputTypeDef] = None
    relatedItemData: Optional[RelatedItemEventIncludedDataTypeDef] = None

class EventIncludedDataTypeDef(BaseValidatorModel):
    caseData: Optional[CaseEventIncludedDataTypeDef] = None
    relatedItemData: Optional[RelatedItemEventIncludedDataTypeDef] = None

class SectionOutputTypeDef(BaseValidatorModel):
    fieldGroup: Optional[FieldGroupOutputTypeDef] = None

class SectionTypeDef(BaseValidatorModel):
    fieldGroup: Optional[FieldGroupTypeDef] = None

class GetCaseResponseTypeDef(BaseValidatorModel):
    fields: List[FieldValueOutputTypeDef]
    nextToken: str
    tags: Dict[str, str]
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchCasesResponseItemTypeDef(BaseValidatorModel):
    caseId: str
    fields: List[FieldValueOutputTypeDef]
    templateId: str
    tags: Optional[Dict[str, str]] = None

class FieldFilterTypeDef(BaseValidatorModel):
    contains: Optional[FieldValueTypeDef] = None
    equalTo: Optional[FieldValueTypeDef] = None
    greaterThan: Optional[FieldValueTypeDef] = None
    greaterThanOrEqualTo: Optional[FieldValueTypeDef] = None
    lessThan: Optional[FieldValueTypeDef] = None
    lessThanOrEqualTo: Optional[FieldValueTypeDef] = None

class SearchRelatedItemsResponseItemTypeDef(BaseValidatorModel):
    associationTime: datetime
    content: RelatedItemContentTypeDef
    relatedItemId: str
    type: RelatedItemTypeType
    performedBy: Optional[UserUnionTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateRelatedItemRequestRequestTypeDef(BaseValidatorModel):
    caseId: str
    content: RelatedItemInputContentTypeDef
    domainId: str
    type: RelatedItemTypeType
    performedBy: Optional[UserUnionTypeDef] = None

class SearchRelatedItemsRequestRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCaseAuditEventsResponseTypeDef(BaseValidatorModel):
    auditEvents: List[AuditEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventBridgeConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: bool
    includedData: Optional[EventIncludedDataOutputTypeDef] = None

class EventBridgeConfigurationTypeDef(BaseValidatorModel):
    enabled: bool
    includedData: Optional[EventIncludedDataTypeDef] = None

class LayoutSectionsOutputTypeDef(BaseValidatorModel):
    sections: Optional[List[SectionOutputTypeDef]] = None

class LayoutSectionsTypeDef(BaseValidatorModel):
    sections: Optional[Sequence[SectionTypeDef]] = None

class SearchCasesResponseTypeDef(BaseValidatorModel):
    cases: List[SearchCasesResponseItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CaseFilterTypeDef(BaseValidatorModel):
    andAll: Optional[Sequence[Dict[str, Any]]] = None
    field: Optional[FieldFilterTypeDef] = None
    not: Optional[Dict[str, Any]] = None
    orAll: Optional[Sequence[Dict[str, Any]]] = None

class CreateCaseRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    fields: Sequence[FieldValueExtraUnionTypeDef]
    templateId: str
    clientToken: Optional[str] = None
    performedBy: Optional[UserUnionTypeDef] = None

class UpdateCaseRequestRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldValueExtraUnionTypeDef]
    performedBy: Optional[UserUnionTypeDef] = None

class SearchRelatedItemsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    relatedItems: List[SearchRelatedItemsResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCaseEventConfigurationResponseTypeDef(BaseValidatorModel):
    eventBridge: EventBridgeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCaseEventConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    eventBridge: EventBridgeConfigurationTypeDef

class BasicLayoutOutputTypeDef(BaseValidatorModel):
    moreInfo: Optional[LayoutSectionsOutputTypeDef] = None
    topPanel: Optional[LayoutSectionsOutputTypeDef] = None

class BasicLayoutTypeDef(BaseValidatorModel):
    moreInfo: Optional[LayoutSectionsTypeDef] = None
    topPanel: Optional[LayoutSectionsTypeDef] = None

class SearchCasesRequestSearchCasesPaginateTypeDef(BaseValidatorModel):
    domainId: str
    fields: Optional[Sequence[FieldIdentifierTypeDef]] = None
    filter: Optional[CaseFilterTypeDef] = None
    searchTerm: Optional[str] = None
    sorts: Optional[Sequence[SortTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LayoutContentOutputTypeDef(BaseValidatorModel):
    basic: Optional[BasicLayoutOutputTypeDef] = None

class LayoutContentTypeDef(BaseValidatorModel):
    basic: Optional[BasicLayoutTypeDef] = None

class GetLayoutResponseTypeDef(BaseValidatorModel):
    content: LayoutContentOutputTypeDef
    createdTime: datetime
    deleted: bool
    lastModifiedTime: datetime
    layoutArn: str
    layoutId: str
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayoutRequestRequestTypeDef(BaseValidatorModel):
    content: LayoutContentTypeDef
    domainId: str
    name: str

class UpdateLayoutRequestRequestTypeDef(BaseValidatorModel):
    domainId: str
    layoutId: str
    content: Optional[LayoutContentTypeDef] = None
    name: Optional[str] = None

