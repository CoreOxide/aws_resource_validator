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
from aws_resource_validator.pydantic_models.connectcases_constants import *

class AuditEventFieldValueUnion(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None


class UserUnion(BaseValidatorModel):
    userArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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
    emptyValue: Optional[Mapping[str, Any]] = None
    stringValue: Optional[str] = None


class CaseRuleSummary(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
    name: str
    ruleType: Literal["Required"]
    description: Optional[str] = None


class CaseSummary(BaseValidatorModel):
    caseId: str
    templateId: str


class CommentContent(BaseValidatorModel):
    body: str
    contentType: Literal["Text/Plain"]


class ContactContent(BaseValidatorModel):
    channel: str
    connectedToSystemTime: datetime
    contactArn: str


class ContactFilter(BaseValidatorModel):
    channel: Optional[Sequence[str]] = None
    contactArn: Optional[str] = None


class Contact(BaseValidatorModel):
    contactArn: str


class CreateDomainRequest(BaseValidatorModel):
    name: str


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


class FieldValueUnionOutput(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None


class FieldValueUnion(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Mapping[str, Any]] = None
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
    values: Optional[Sequence[str]] = None


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
    status: Optional[Sequence[TemplateStatusType]] = None


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
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


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


class CaseRuleIdentifier(BaseValidatorModel):
    pass


class BatchGetCaseRuleRequest(BaseValidatorModel):
    caseRules: Sequence[CaseRuleIdentifier]
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


class FieldIdentifier(BaseValidatorModel):
    pass


class BatchGetFieldRequest(BaseValidatorModel):
    domainId: str
    fields: Sequence[FieldIdentifier]


class CaseEventIncludedDataOutput(BaseValidatorModel):
    fields: List[FieldIdentifier]


class CaseEventIncludedData(BaseValidatorModel):
    fields: Sequence[FieldIdentifier]


class GetCaseRequest(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldIdentifier]
    nextToken: Optional[str] = None


class FieldError(BaseValidatorModel):
    pass


class GetFieldResponse(BaseValidatorModel):
    pass


class BatchGetFieldResponse(BaseValidatorModel):
    errors: List[FieldError]
    fields: List[GetFieldResponse]
    ResponseMetadata: ResponseMetadata


class BatchPutFieldOptionsRequest(BaseValidatorModel):
    domainId: str
    fieldId: str
    options: Sequence[FieldOption]


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
    requiredFields: Optional[Sequence[RequiredField]] = None
    rules: Optional[Sequence[TemplateRule]] = None
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
    requiredFields: Optional[Sequence[RequiredField]] = None
    rules: Optional[Sequence[TemplateRule]] = None
    status: Optional[TemplateStatusType] = None


class ListDomainsResponse(BaseValidatorModel):
    domains: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FieldItem(BaseValidatorModel):
    pass


class FieldGroupOutput(BaseValidatorModel):
    fields: List[FieldItem]
    name: Optional[str] = None


class FieldGroup(BaseValidatorModel):
    fields: Sequence[FieldItem]
    name: Optional[str] = None


class FieldSummary(BaseValidatorModel):
    pass


class ListFieldsResponse(BaseValidatorModel):
    fields: List[FieldSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RelatedItemContent(BaseValidatorModel):
    comment: Optional[CommentContent] = None
    contact: Optional[ContactContent] = None
    file: Optional[FileContent] = None


class RelatedItemInputContent(BaseValidatorModel):
    comment: Optional[CommentContent] = None
    contact: Optional[Contact] = None
    file: Optional[FileContent] = None


class RelatedItemTypeFilter(BaseValidatorModel):
    comment: Optional[Mapping[str, Any]] = None
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


class FieldValueOutput(BaseValidatorModel):
    pass


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


class SearchRelatedItemsRequestPaginate(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchRelatedItemsRequest(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class AuditEvent(BaseValidatorModel):
    pass


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
    conditions: Sequence[BooleanCondition]
    defaultValue: bool


class LayoutSectionsOutput(BaseValidatorModel):
    sections: Optional[List[SectionOutput]] = None


class LayoutSections(BaseValidatorModel):
    sections: Optional[Sequence[Section]] = None


class SearchCasesResponse(BaseValidatorModel):
    cases: List[SearchCasesResponseItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchRelatedItemsResponseItem(BaseValidatorModel):
    pass


class SearchRelatedItemsResponse(BaseValidatorModel):
    relatedItems: List[SearchRelatedItemsResponseItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetCaseEventConfigurationResponse(BaseValidatorModel):
    eventBridge: EventBridgeConfigurationOutput
    ResponseMetadata: ResponseMetadata


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


class FieldValueUnionExtra(BaseValidatorModel):
    pass


class CreateCaseRequest(BaseValidatorModel):
    domainId: str
    fields: Sequence[FieldValueUnionExtra]
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
    fields: Sequence[FieldValueUnionExtra]
    performedBy: Optional[UserUnion] = None


class EventBridgeConfigurationUnion(BaseValidatorModel):
    pass


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


class LayoutContentOutput(BaseValidatorModel):
    basic: Optional[BasicLayoutOutput] = None


class LayoutContent(BaseValidatorModel):
    basic: Optional[BasicLayout] = None


class CaseRuleError(BaseValidatorModel):
    pass


class BatchGetCaseRuleResponse(BaseValidatorModel):
    caseRules: List[GetCaseRuleResponse]
    errors: List[CaseRuleError]
    ResponseMetadata: ResponseMetadata


class CaseRuleDetailsUnion(BaseValidatorModel):
    pass


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


class LayoutContentUnion(BaseValidatorModel):
    pass


class CreateLayoutRequest(BaseValidatorModel):
    content: LayoutContentUnion
    domainId: str
    name: str


class UpdateLayoutRequest(BaseValidatorModel):
    domainId: str
    layoutId: str
    content: Optional[LayoutContentUnion] = None
    name: Optional[str] = None


