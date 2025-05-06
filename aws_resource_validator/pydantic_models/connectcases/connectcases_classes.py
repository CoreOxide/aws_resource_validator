from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connectcases.connectcases_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AuditEventFieldValueUnion(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None


class UserUnion(BaseValidatorModel):
    userArn: Optional[str] = None


class CaseRuleIdentifier(BaseValidatorModel):
    id: str


class CaseRuleError(BaseValidatorModel):
    errorCode: str
    id: str
    message: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FieldIdentifier(BaseValidatorModel):
    id: str


class FieldError(BaseValidatorModel):
    errorCode: str
    id: str
    message: Optional[str] = None


class GetFieldResponse(BaseValidatorModel):
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


class FieldOption(BaseValidatorModel):
    active: bool
    name: str
    value: str


class FieldOptionError(BaseValidatorModel):
    errorCode: str
    message: str
    value: str


class OperandOne(BaseValidatorModel):
    fieldId: Optional[str] = None


class OperandTwoOutput(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None


class OperandTwo(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None


class CaseRuleSummary(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
    name: str
    ruleType: Literal['Required']
    description: Optional[str] = None


class CaseSummary(BaseValidatorModel):
    caseId: str
    templateId: str


class CommentContent(BaseValidatorModel):
    body: str
    contentType: Literal['Text/Plain']


class ContactContent(BaseValidatorModel):
    channel: str
    connectedToSystemTime: datetime
    contactArn: str


class ContactFilter(BaseValidatorModel):
    channel: Optional[List[str]] = None
    contactArn: Optional[str] = None


class Contact(BaseValidatorModel):
    contactArn: str


class CreateDomainRequest(BaseValidatorModel):
    name: str


class CreateFieldRequest(BaseValidatorModel):
    domainId: str
    name: str
    type: FieldTypeType
    description: Optional[str] = None


class LayoutConfiguration(BaseValidatorModel):
    defaultLayout: Optional[str] = None


class RequiredField(BaseValidatorModel):
    fieldId: str


class TemplateRule(BaseValidatorModel):
    caseRuleId: str
    fieldId: str


class DeleteCaseRuleRequest(BaseValidatorModel):
    caseRuleId: str
    domainId: str


class DeleteDomainRequest(BaseValidatorModel):
    domainId: str


class DeleteFieldRequest(BaseValidatorModel):
    domainId: str
    fieldId: str


class DeleteLayoutRequest(BaseValidatorModel):
    domainId: str
    layoutId: str


class DeleteTemplateRequest(BaseValidatorModel):
    domainId: str
    templateId: str


class DomainSummary(BaseValidatorModel):
    domainArn: str
    domainId: str
    name: str


class RelatedItemEventIncludedData(BaseValidatorModel):
    includeContent: bool


class FieldItem(BaseValidatorModel):
    id: str


class FieldSummary(BaseValidatorModel):
    fieldArn: str
    fieldId: str
    name: str
    namespace: FieldNamespaceType
    type: FieldTypeType


class FieldValueUnionOutput(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None


class FieldValueUnion(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None


class FileContent(BaseValidatorModel):
    fileArn: str


class FileFilter(BaseValidatorModel):
    fileArn: Optional[str] = None


class GetCaseAuditEventsRequest(BaseValidatorModel):
    caseId: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetCaseEventConfigurationRequest(BaseValidatorModel):
    domainId: str


class GetDomainRequest(BaseValidatorModel):
    domainId: str


class GetLayoutRequest(BaseValidatorModel):
    domainId: str
    layoutId: str


class GetTemplateRequest(BaseValidatorModel):
    domainId: str
    templateId: str


class LayoutSummary(BaseValidatorModel):
    layoutArn: str
    layoutId: str
    name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCaseRulesRequest(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCasesForContactRequest(BaseValidatorModel):
    contactArn: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDomainsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFieldOptionsRequest(BaseValidatorModel):
    domainId: str
    fieldId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    values: Optional[List[str]] = None


class ListFieldsRequest(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLayoutsRequest(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class ListTemplatesRequest(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[List[TemplateStatusType]] = None


class TemplateSummary(BaseValidatorModel):
    name: str
    status: TemplateStatusType
    templateArn: str
    templateId: str


class Sort(BaseValidatorModel):
    fieldId: str
    sortOrder: OrderType


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


class UpdateFieldRequest(BaseValidatorModel):
    domainId: str
    fieldId: str
    description: Optional[str] = None
    name: Optional[str] = None


class AuditEventField(BaseValidatorModel):
    eventFieldId: str
    newValue: AuditEventFieldValueUnion
    oldValue: Optional[AuditEventFieldValueUnion] = None


class AuditEventPerformedBy(BaseValidatorModel):
    iamPrincipalArn: str
    user: Optional[UserUnion] = None


class BatchGetCaseRuleRequest(BaseValidatorModel):
    caseRules: List[CaseRuleIdentifier]
    domainId: str


class CreateCaseResponse(BaseValidatorModel):
    caseArn: str
    caseId: str
    ResponseMetadata: ResponseMetadata


class CreateCaseRuleResponse(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
    ResponseMetadata: ResponseMetadata


class CreateDomainResponse(BaseValidatorModel):
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    ResponseMetadata: ResponseMetadata


class CreateFieldResponse(BaseValidatorModel):
    fieldArn: str
    fieldId: str
    ResponseMetadata: ResponseMetadata


class CreateLayoutResponse(BaseValidatorModel):
    layoutArn: str
    layoutId: str
    ResponseMetadata: ResponseMetadata


class CreateRelatedItemResponse(BaseValidatorModel):
    relatedItemArn: str
    relatedItemId: str
    ResponseMetadata: ResponseMetadata


class CreateTemplateResponse(BaseValidatorModel):
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDomainResponse(BaseValidatorModel):
    createdTime: datetime
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class BatchGetFieldRequest(BaseValidatorModel):
    domainId: str
    fields: List[FieldIdentifier]


class CaseEventIncludedDataOutput(BaseValidatorModel):
    fields: List[FieldIdentifier]


class CaseEventIncludedData(BaseValidatorModel):
    fields: List[FieldIdentifier]


class GetCaseRequest(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: List[FieldIdentifier]
    nextToken: Optional[str] = None


class BatchGetFieldResponse(BaseValidatorModel):
    errors: List[FieldError]
    fields: List[GetFieldResponse]
    ResponseMetadata: ResponseMetadata


class BatchPutFieldOptionsRequest(BaseValidatorModel):
    domainId: str
    fieldId: str
    options: List[FieldOption]


class ListFieldOptionsResponse(BaseValidatorModel):
    options: List[FieldOption]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchPutFieldOptionsResponse(BaseValidatorModel):
    errors: List[FieldOptionError]
    ResponseMetadata: ResponseMetadata


class BooleanOperandsOutput(BaseValidatorModel):
    operandOne: OperandOne
    operandTwo: OperandTwoOutput
    result: bool


class BooleanOperands(BaseValidatorModel):
    operandOne: OperandOne
    operandTwo: OperandTwo
    result: bool


class ListCaseRulesResponse(BaseValidatorModel):
    caseRules: List[CaseRuleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCasesForContactResponse(BaseValidatorModel):
    cases: List[CaseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateTemplateRequest(BaseValidatorModel):
    domainId: str
    name: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfiguration] = None
    requiredFields: Optional[List[RequiredField]] = None
    rules: Optional[List[TemplateRule]] = None
    status: Optional[TemplateStatusType] = None


class GetTemplateResponse(BaseValidatorModel):
    createdTime: datetime
    deleted: bool
    description: str
    lastModifiedTime: datetime
    layoutConfiguration: LayoutConfiguration
    name: str
    requiredFields: List[RequiredField]
    rules: List[TemplateRule]
    status: TemplateStatusType
    tags: Dict[str, str]
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadata


class UpdateTemplateRequest(BaseValidatorModel):
    domainId: str
    templateId: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfiguration] = None
    name: Optional[str] = None
    requiredFields: Optional[List[RequiredField]] = None
    rules: Optional[List[TemplateRule]] = None
    status: Optional[TemplateStatusType] = None


class ListDomainsResponse(BaseValidatorModel):
    domains: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FieldGroupOutput(BaseValidatorModel):
    fields: List[FieldItem]
    name: Optional[str] = None


class FieldGroup(BaseValidatorModel):
    fields: List[FieldItem]
    name: Optional[str] = None


class ListFieldsResponse(BaseValidatorModel):
    fields: List[FieldSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FieldValueOutput(BaseValidatorModel):
    id: str
    value: FieldValueUnionOutput

FieldValueUnionUnion = Union[FieldValueUnion, FieldValueUnionOutput]


class RelatedItemContent(BaseValidatorModel):
    comment: Optional[CommentContent] = None
    contact: Optional[ContactContent] = None
    file: Optional[FileContent] = None


class RelatedItemInputContent(BaseValidatorModel):
    comment: Optional[CommentContent] = None
    contact: Optional[Contact] = None
    file: Optional[FileContent] = None


class RelatedItemTypeFilter(BaseValidatorModel):
    comment: Optional[Dict[str, Any]] = None
    contact: Optional[ContactFilter] = None
    file: Optional[FileFilter] = None


class ListLayoutsResponse(BaseValidatorModel):
    layouts: List[LayoutSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCaseRulesRequestPaginate(BaseValidatorModel):
    domainId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplatesResponse(BaseValidatorModel):
    templates: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AuditEvent(BaseValidatorModel):
    eventId: str
    fields: List[AuditEventField]
    performedTime: datetime
    type: AuditEventTypeType
    performedBy: Optional[AuditEventPerformedBy] = None
    relatedItemType: Optional[RelatedItemTypeType] = None


class EventIncludedDataOutput(BaseValidatorModel):
    caseData: Optional[CaseEventIncludedDataOutput] = None
    relatedItemData: Optional[RelatedItemEventIncludedData] = None


class EventIncludedData(BaseValidatorModel):
    caseData: Optional[CaseEventIncludedData] = None
    relatedItemData: Optional[RelatedItemEventIncludedData] = None


class BooleanConditionOutput(BaseValidatorModel):
    equalTo: Optional[BooleanOperandsOutput] = None
    notEqualTo: Optional[BooleanOperandsOutput] = None


class BooleanCondition(BaseValidatorModel):
    equalTo: Optional[BooleanOperands] = None
    notEqualTo: Optional[BooleanOperands] = None


class SectionOutput(BaseValidatorModel):
    fieldGroup: Optional[FieldGroupOutput] = None


class Section(BaseValidatorModel):
    fieldGroup: Optional[FieldGroup] = None


class GetCaseResponse(BaseValidatorModel):
    fields: List[FieldValueOutput]
    tags: Dict[str, str]
    templateId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchCasesResponseItem(BaseValidatorModel):
    caseId: str
    fields: List[FieldValueOutput]
    templateId: str
    tags: Optional[Dict[str, str]] = None


class FieldValue(BaseValidatorModel):
    id: str
    value: FieldValueUnionUnion


class SearchRelatedItemsResponseItem(BaseValidatorModel):
    associationTime: datetime
    content: RelatedItemContent
    relatedItemId: str
    type: RelatedItemTypeType
    performedBy: Optional[UserUnion] = None
    tags: Optional[Dict[str, str]] = None


class CreateRelatedItemRequest(BaseValidatorModel):
    caseId: str
    content: RelatedItemInputContent
    domainId: str
    type: RelatedItemTypeType
    performedBy: Optional[UserUnion] = None


class SearchRelatedItemsRequestPaginate(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[List[RelatedItemTypeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchRelatedItemsRequest(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[List[RelatedItemTypeFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetCaseAuditEventsResponse(BaseValidatorModel):
    auditEvents: List[AuditEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EventBridgeConfigurationOutput(BaseValidatorModel):
    enabled: bool
    includedData: Optional[EventIncludedDataOutput] = None


class EventBridgeConfiguration(BaseValidatorModel):
    enabled: bool
    includedData: Optional[EventIncludedData] = None


class RequiredCaseRuleOutput(BaseValidatorModel):
    conditions: List[BooleanConditionOutput]
    defaultValue: bool


class RequiredCaseRule(BaseValidatorModel):
    conditions: List[BooleanCondition]
    defaultValue: bool


class LayoutSectionsOutput(BaseValidatorModel):
    sections: Optional[List[SectionOutput]] = None


class LayoutSections(BaseValidatorModel):
    sections: Optional[List[Section]] = None


class SearchCasesResponse(BaseValidatorModel):
    cases: List[SearchCasesResponseItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

FieldValueUnionExtra = Union[FieldValue, FieldValueOutput]


class SearchRelatedItemsResponse(BaseValidatorModel):
    relatedItems: List[SearchRelatedItemsResponseItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetCaseEventConfigurationResponse(BaseValidatorModel):
    eventBridge: EventBridgeConfigurationOutput
    ResponseMetadata: ResponseMetadata

EventBridgeConfigurationUnion = Union[EventBridgeConfiguration, EventBridgeConfigurationOutput]


class CaseRuleDetailsOutput(BaseValidatorModel):
    required: Optional[RequiredCaseRuleOutput] = None


class CaseRuleDetails(BaseValidatorModel):
    required: Optional[RequiredCaseRule] = None


class BasicLayoutOutput(BaseValidatorModel):
    moreInfo: Optional[LayoutSectionsOutput] = None
    topPanel: Optional[LayoutSectionsOutput] = None


class BasicLayout(BaseValidatorModel):
    moreInfo: Optional[LayoutSections] = None
    topPanel: Optional[LayoutSections] = None


class CreateCaseRequest(BaseValidatorModel):
    domainId: str
    fields: List[FieldValueUnionExtra]
    templateId: str
    clientToken: Optional[str] = None
    performedBy: Optional[UserUnion] = None


class FieldFilter(BaseValidatorModel):
    contains: Optional[FieldValueUnionExtra] = None
    equalTo: Optional[FieldValueUnionExtra] = None
    greaterThan: Optional[FieldValueUnionExtra] = None
    greaterThanOrEqualTo: Optional[FieldValueUnionExtra] = None
    lessThan: Optional[FieldValueUnionExtra] = None
    lessThanOrEqualTo: Optional[FieldValueUnionExtra] = None


class UpdateCaseRequest(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: List[FieldValueUnionExtra]
    performedBy: Optional[UserUnion] = None


class PutCaseEventConfigurationRequest(BaseValidatorModel):
    domainId: str
    eventBridge: EventBridgeConfigurationUnion


class GetCaseRuleResponse(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
    name: str
    rule: CaseRuleDetailsOutput
    createdTime: Optional[datetime] = None
    deleted: Optional[bool] = None
    description: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

CaseRuleDetailsUnion = Union[CaseRuleDetails, CaseRuleDetailsOutput]


class LayoutContentOutput(BaseValidatorModel):
    basic: Optional[BasicLayoutOutput] = None


class LayoutContent(BaseValidatorModel):
    basic: Optional[BasicLayout] = None


class CaseFilterPaginator(BaseValidatorModel):
    andAll: Optional[List[Dict[str, Any]]] = None
    field: Optional[FieldFilter] = None
    not_: Optional[Dict[str, Any]] = None
    orAll: Optional[List[Dict[str, Any]]] = None


class CaseFilter(BaseValidatorModel):
    andAll: Optional[List[Dict[str, Any]]] = None
    field: Optional[FieldFilter] = None
    not_: Optional[Dict[str, Any]] = None
    orAll: Optional[List[Dict[str, Any]]] = None


class BatchGetCaseRuleResponse(BaseValidatorModel):
    caseRules: List[GetCaseRuleResponse]
    errors: List[CaseRuleError]
    ResponseMetadata: ResponseMetadata


class CreateCaseRuleRequest(BaseValidatorModel):
    domainId: str
    name: str
    rule: CaseRuleDetailsUnion
    description: Optional[str] = None


class UpdateCaseRuleRequest(BaseValidatorModel):
    caseRuleId: str
    domainId: str
    description: Optional[str] = None
    name: Optional[str] = None
    rule: Optional[CaseRuleDetailsUnion] = None


class GetLayoutResponse(BaseValidatorModel):
    content: LayoutContentOutput
    createdTime: datetime
    deleted: bool
    lastModifiedTime: datetime
    layoutArn: str
    layoutId: str
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

LayoutContentUnion = Union[LayoutContent, LayoutContentOutput]


class SearchCasesRequestPaginate(BaseValidatorModel):
    domainId: str
    fields: Optional[List[FieldIdentifier]] = None
    filter: Optional[CaseFilterPaginator] = None
    searchTerm: Optional[str] = None
    sorts: Optional[List[Sort]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchCasesRequest(BaseValidatorModel):
    domainId: str
    fields: Optional[List[FieldIdentifier]] = None
    filter: Optional[CaseFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchTerm: Optional[str] = None
    sorts: Optional[List[Sort]] = None


class CreateLayoutRequest(BaseValidatorModel):
    content: LayoutContentUnion
    domainId: str
    name: str


class UpdateLayoutRequest(BaseValidatorModel):
    domainId: str
    layoutId: str
    content: Optional[LayoutContentUnion] = None
    name: Optional[str] = None