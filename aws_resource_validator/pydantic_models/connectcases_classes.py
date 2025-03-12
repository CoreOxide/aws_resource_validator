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

class AuditEventFieldValueUnionTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None
    userArnValue: Optional[str] = None


class UserUnionTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None


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


class OperandOneTypeDef(BaseValidatorModel):
    fieldId: Optional[str] = None


class OperandTwoOutputTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Dict[str, Any]] = None
    stringValue: Optional[str] = None


class OperandTwoTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    emptyValue: Optional[Mapping[str, Any]] = None
    stringValue: Optional[str] = None


class CaseRuleSummaryTypeDef(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
    name: str
    ruleType: Literal["Required"]
    description: Optional[str] = None


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


class CreateDomainRequestTypeDef(BaseValidatorModel):
    name: str


class LayoutConfigurationTypeDef(BaseValidatorModel):
    defaultLayout: Optional[str] = None


class RequiredFieldTypeDef(BaseValidatorModel):
    fieldId: str


class TemplateRuleTypeDef(BaseValidatorModel):
    caseRuleId: str
    fieldId: str


class DeleteCaseRuleRequestTypeDef(BaseValidatorModel):
    caseRuleId: str
    domainId: str


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    domainId: str


class DeleteFieldRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str


class DeleteLayoutRequestTypeDef(BaseValidatorModel):
    domainId: str
    layoutId: str


class DeleteTemplateRequestTypeDef(BaseValidatorModel):
    domainId: str
    templateId: str


class DomainSummaryTypeDef(BaseValidatorModel):
    domainArn: str
    domainId: str
    name: str


class RelatedItemEventIncludedDataTypeDef(BaseValidatorModel):
    includeContent: bool


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


class GetCaseAuditEventsRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetCaseEventConfigurationRequestTypeDef(BaseValidatorModel):
    domainId: str


class GetDomainRequestTypeDef(BaseValidatorModel):
    domainId: str


class GetLayoutRequestTypeDef(BaseValidatorModel):
    domainId: str
    layoutId: str


class GetTemplateRequestTypeDef(BaseValidatorModel):
    domainId: str
    templateId: str


class LayoutSummaryTypeDef(BaseValidatorModel):
    layoutArn: str
    layoutId: str
    name: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCaseRulesRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCasesForContactRequestTypeDef(BaseValidatorModel):
    contactArn: str
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDomainsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFieldOptionsRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    values: Optional[Sequence[str]] = None


class ListFieldsRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLayoutsRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    arn: str


class ListTemplatesRequestTypeDef(BaseValidatorModel):
    domainId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[Sequence[TemplateStatusType]] = None


class TemplateSummaryTypeDef(BaseValidatorModel):
    name: str
    status: TemplateStatusType
    templateArn: str
    templateId: str


class SortTypeDef(BaseValidatorModel):
    fieldId: str
    sortOrder: OrderType


class TagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class UpdateFieldRequestTypeDef(BaseValidatorModel):
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


class CaseRuleIdentifierTypeDef(BaseValidatorModel):
    pass


class BatchGetCaseRuleRequestTypeDef(BaseValidatorModel):
    caseRules: Sequence[CaseRuleIdentifierTypeDef]
    domainId: str


class CreateCaseResponseTypeDef(BaseValidatorModel):
    caseArn: str
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCaseRuleResponseTypeDef(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
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


class FieldIdentifierTypeDef(BaseValidatorModel):
    pass


class BatchGetFieldRequestTypeDef(BaseValidatorModel):
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]


class CaseEventIncludedDataOutputTypeDef(BaseValidatorModel):
    fields: List[FieldIdentifierTypeDef]


class CaseEventIncludedDataTypeDef(BaseValidatorModel):
    fields: Sequence[FieldIdentifierTypeDef]


class GetCaseRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]
    nextToken: Optional[str] = None


class FieldErrorTypeDef(BaseValidatorModel):
    pass


class GetFieldResponseTypeDef(BaseValidatorModel):
    pass


class BatchGetFieldResponseTypeDef(BaseValidatorModel):
    errors: List[FieldErrorTypeDef]
    fields: List[GetFieldResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutFieldOptionsRequestTypeDef(BaseValidatorModel):
    domainId: str
    fieldId: str
    options: Sequence[FieldOptionTypeDef]


class ListFieldOptionsResponseTypeDef(BaseValidatorModel):
    options: List[FieldOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchPutFieldOptionsResponseTypeDef(BaseValidatorModel):
    errors: List[FieldOptionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BooleanOperandsOutputTypeDef(BaseValidatorModel):
    operandOne: OperandOneTypeDef
    operandTwo: OperandTwoOutputTypeDef
    result: bool


class BooleanOperandsTypeDef(BaseValidatorModel):
    operandOne: OperandOneTypeDef
    operandTwo: OperandTwoTypeDef
    result: bool


class ListCaseRulesResponseTypeDef(BaseValidatorModel):
    caseRules: List[CaseRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCasesForContactResponseTypeDef(BaseValidatorModel):
    cases: List[CaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateTemplateRequestTypeDef(BaseValidatorModel):
    domainId: str
    name: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfigurationTypeDef] = None
    requiredFields: Optional[Sequence[RequiredFieldTypeDef]] = None
    rules: Optional[Sequence[TemplateRuleTypeDef]] = None
    status: Optional[TemplateStatusType] = None


class GetTemplateResponseTypeDef(BaseValidatorModel):
    createdTime: datetime
    deleted: bool
    description: str
    lastModifiedTime: datetime
    layoutConfiguration: LayoutConfigurationTypeDef
    name: str
    requiredFields: List[RequiredFieldTypeDef]
    rules: List[TemplateRuleTypeDef]
    status: TemplateStatusType
    tags: Dict[str, str]
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTemplateRequestTypeDef(BaseValidatorModel):
    domainId: str
    templateId: str
    description: Optional[str] = None
    layoutConfiguration: Optional[LayoutConfigurationTypeDef] = None
    name: Optional[str] = None
    requiredFields: Optional[Sequence[RequiredFieldTypeDef]] = None
    rules: Optional[Sequence[TemplateRuleTypeDef]] = None
    status: Optional[TemplateStatusType] = None


class ListDomainsResponseTypeDef(BaseValidatorModel):
    domains: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FieldItemTypeDef(BaseValidatorModel):
    pass


class FieldGroupOutputTypeDef(BaseValidatorModel):
    fields: List[FieldItemTypeDef]
    name: Optional[str] = None


class FieldGroupTypeDef(BaseValidatorModel):
    fields: Sequence[FieldItemTypeDef]
    name: Optional[str] = None


class FieldSummaryTypeDef(BaseValidatorModel):
    pass


class ListFieldsResponseTypeDef(BaseValidatorModel):
    fields: List[FieldSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCaseRulesRequestPaginateTypeDef(BaseValidatorModel):
    domainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTemplatesResponseTypeDef(BaseValidatorModel):
    templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EventIncludedDataOutputTypeDef(BaseValidatorModel):
    caseData: Optional[CaseEventIncludedDataOutputTypeDef] = None
    relatedItemData: Optional[RelatedItemEventIncludedDataTypeDef] = None


class EventIncludedDataTypeDef(BaseValidatorModel):
    caseData: Optional[CaseEventIncludedDataTypeDef] = None
    relatedItemData: Optional[RelatedItemEventIncludedDataTypeDef] = None


class BooleanConditionOutputTypeDef(BaseValidatorModel):
    equalTo: Optional[BooleanOperandsOutputTypeDef] = None
    notEqualTo: Optional[BooleanOperandsOutputTypeDef] = None


class BooleanConditionTypeDef(BaseValidatorModel):
    equalTo: Optional[BooleanOperandsTypeDef] = None
    notEqualTo: Optional[BooleanOperandsTypeDef] = None


class SectionOutputTypeDef(BaseValidatorModel):
    fieldGroup: Optional[FieldGroupOutputTypeDef] = None


class SectionTypeDef(BaseValidatorModel):
    fieldGroup: Optional[FieldGroupTypeDef] = None


class FieldValueOutputTypeDef(BaseValidatorModel):
    pass


class GetCaseResponseTypeDef(BaseValidatorModel):
    fields: List[FieldValueOutputTypeDef]
    tags: Dict[str, str]
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchCasesResponseItemTypeDef(BaseValidatorModel):
    caseId: str
    fields: List[FieldValueOutputTypeDef]
    templateId: str
    tags: Optional[Dict[str, str]] = None


class SearchRelatedItemsRequestPaginateTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchRelatedItemsRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    filters: Optional[Sequence[RelatedItemTypeFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class AuditEventTypeDef(BaseValidatorModel):
    pass


class GetCaseAuditEventsResponseTypeDef(BaseValidatorModel):
    auditEvents: List[AuditEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EventBridgeConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: bool
    includedData: Optional[EventIncludedDataOutputTypeDef] = None


class EventBridgeConfigurationTypeDef(BaseValidatorModel):
    enabled: bool
    includedData: Optional[EventIncludedDataTypeDef] = None


class RequiredCaseRuleOutputTypeDef(BaseValidatorModel):
    conditions: List[BooleanConditionOutputTypeDef]
    defaultValue: bool


class RequiredCaseRuleTypeDef(BaseValidatorModel):
    conditions: Sequence[BooleanConditionTypeDef]
    defaultValue: bool


class LayoutSectionsOutputTypeDef(BaseValidatorModel):
    sections: Optional[List[SectionOutputTypeDef]] = None


class LayoutSectionsTypeDef(BaseValidatorModel):
    sections: Optional[Sequence[SectionTypeDef]] = None


class SearchCasesResponseTypeDef(BaseValidatorModel):
    cases: List[SearchCasesResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchRelatedItemsResponseItemTypeDef(BaseValidatorModel):
    pass


class SearchRelatedItemsResponseTypeDef(BaseValidatorModel):
    relatedItems: List[SearchRelatedItemsResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetCaseEventConfigurationResponseTypeDef(BaseValidatorModel):
    eventBridge: EventBridgeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CaseRuleDetailsOutputTypeDef(BaseValidatorModel):
    required: Optional[RequiredCaseRuleOutputTypeDef] = None


class CaseRuleDetailsTypeDef(BaseValidatorModel):
    required: Optional[RequiredCaseRuleTypeDef] = None


class BasicLayoutOutputTypeDef(BaseValidatorModel):
    moreInfo: Optional[LayoutSectionsOutputTypeDef] = None
    topPanel: Optional[LayoutSectionsOutputTypeDef] = None


class BasicLayoutTypeDef(BaseValidatorModel):
    moreInfo: Optional[LayoutSectionsTypeDef] = None
    topPanel: Optional[LayoutSectionsTypeDef] = None


class FieldValueUnionExtraTypeDef(BaseValidatorModel):
    pass


class CreateCaseRequestTypeDef(BaseValidatorModel):
    domainId: str
    fields: Sequence[FieldValueUnionExtraTypeDef]
    templateId: str
    clientToken: Optional[str] = None
    performedBy: Optional[UserUnionTypeDef] = None


class FieldFilterTypeDef(BaseValidatorModel):
    contains: Optional[FieldValueUnionExtraTypeDef] = None
    equalTo: Optional[FieldValueUnionExtraTypeDef] = None
    greaterThan: Optional[FieldValueUnionExtraTypeDef] = None
    greaterThanOrEqualTo: Optional[FieldValueUnionExtraTypeDef] = None
    lessThan: Optional[FieldValueUnionExtraTypeDef] = None
    lessThanOrEqualTo: Optional[FieldValueUnionExtraTypeDef] = None


class UpdateCaseRequestTypeDef(BaseValidatorModel):
    caseId: str
    domainId: str
    fields: Sequence[FieldValueUnionExtraTypeDef]
    performedBy: Optional[UserUnionTypeDef] = None


class EventBridgeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutCaseEventConfigurationRequestTypeDef(BaseValidatorModel):
    domainId: str
    eventBridge: EventBridgeConfigurationUnionTypeDef


class GetCaseRuleResponseTypeDef(BaseValidatorModel):
    caseRuleArn: str
    caseRuleId: str
    name: str
    rule: CaseRuleDetailsOutputTypeDef
    createdTime: Optional[datetime] = None
    deleted: Optional[bool] = None
    description: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class LayoutContentOutputTypeDef(BaseValidatorModel):
    basic: Optional[BasicLayoutOutputTypeDef] = None


class LayoutContentTypeDef(BaseValidatorModel):
    basic: Optional[BasicLayoutTypeDef] = None


class CaseRuleErrorTypeDef(BaseValidatorModel):
    pass


class BatchGetCaseRuleResponseTypeDef(BaseValidatorModel):
    caseRules: List[GetCaseRuleResponseTypeDef]
    errors: List[CaseRuleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CaseRuleDetailsUnionTypeDef(BaseValidatorModel):
    pass


class CreateCaseRuleRequestTypeDef(BaseValidatorModel):
    domainId: str
    name: str
    rule: CaseRuleDetailsUnionTypeDef
    description: Optional[str] = None


class UpdateCaseRuleRequestTypeDef(BaseValidatorModel):
    caseRuleId: str
    domainId: str
    description: Optional[str] = None
    name: Optional[str] = None
    rule: Optional[CaseRuleDetailsUnionTypeDef] = None


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


class LayoutContentUnionTypeDef(BaseValidatorModel):
    pass


class CreateLayoutRequestTypeDef(BaseValidatorModel):
    content: LayoutContentUnionTypeDef
    domainId: str
    name: str


class UpdateLayoutRequestTypeDef(BaseValidatorModel):
    domainId: str
    layoutId: str
    content: Optional[LayoutContentUnionTypeDef] = None
    name: Optional[str] = None


