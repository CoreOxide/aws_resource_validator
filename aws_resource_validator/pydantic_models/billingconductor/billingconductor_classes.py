from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.billingconductor.billingconductor_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountAssociationsListElement(BaseValidatorModel):
    AccountId: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    AccountName: Optional[str] = None
    AccountEmail: Optional[str] = None


class AccountGrouping(BaseValidatorModel):
    LinkedAccountIds: List[str]
    AutoAssociate: Optional[bool] = None


class AssociateAccountsInput(BaseValidatorModel):
    Arn: str
    AccountIds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociatePricingRulesInput(BaseValidatorModel):
    Arn: str
    PricingRuleArns: List[str]


class AssociateResourceError(BaseValidatorModel):
    Message: Optional[str] = None
    Reason: Optional[AssociateResourceErrorReasonType] = None


class Attribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class CustomLineItemBillingPeriodRange(BaseValidatorModel):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: Optional[str] = None


class BillingGroupCostReportElement(BaseValidatorModel):
    Arn: Optional[str] = None
    AWSCost: Optional[str] = None
    ProformaCost: Optional[str] = None
    Margin: Optional[str] = None
    MarginPercentage: Optional[str] = None
    Currency: Optional[str] = None


class ComputationPreference(BaseValidatorModel):
    PricingPlanArn: str


class ListBillingGroupAccountGrouping(BaseValidatorModel):
    AutoAssociate: Optional[bool] = None


class BillingPeriodRange(BaseValidatorModel):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: str


class CreateFreeTierConfig(BaseValidatorModel):
    Activated: bool


class CreatePricingPlanInput(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PricingRuleArns: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


class CustomLineItemFlatChargeDetails(BaseValidatorModel):
    ChargeValue: float


class CustomLineItemPercentageChargeDetails(BaseValidatorModel):
    PercentageValue: float
    AssociatedValues: Optional[List[str]] = None


class DeleteBillingGroupInput(BaseValidatorModel):
    Arn: str


class DeletePricingPlanInput(BaseValidatorModel):
    Arn: str


class DeletePricingRuleInput(BaseValidatorModel):
    Arn: str


class DisassociateAccountsInput(BaseValidatorModel):
    Arn: str
    AccountIds: List[str]


class DisassociatePricingRulesInput(BaseValidatorModel):
    Arn: str
    PricingRuleArns: List[str]


class FreeTierConfig(BaseValidatorModel):
    Activated: bool


class LineItemFilterOutput(BaseValidatorModel):
    Attribute: Literal['LINE_ITEM_TYPE']
    MatchOption: Literal['NOT_EQUAL']
    Values: List[Literal['SAVINGS_PLAN_NEGATION']]


class LineItemFilter(BaseValidatorModel):
    Attribute: Literal['LINE_ITEM_TYPE']
    MatchOption: Literal['NOT_EQUAL']
    Values: List[Literal['SAVINGS_PLAN_NEGATION']]


class ListAccountAssociationsFilter(BaseValidatorModel):
    Association: Optional[str] = None
    AccountId: Optional[str] = None
    AccountIds: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBillingGroupCostReportsFilter(BaseValidatorModel):
    BillingGroupArns: Optional[List[str]] = None


class ListBillingGroupsFilter(BaseValidatorModel):
    Arns: Optional[List[str]] = None
    PricingPlan: Optional[str] = None
    Statuses: Optional[List[BillingGroupStatusType]] = None
    AutoAssociate: Optional[bool] = None


class ListCustomLineItemFlatChargeDetails(BaseValidatorModel):
    ChargeValue: float


class ListCustomLineItemPercentageChargeDetails(BaseValidatorModel):
    PercentageValue: float


class ListCustomLineItemVersionsBillingPeriodRangeFilter(BaseValidatorModel):
    StartBillingPeriod: Optional[str] = None
    EndBillingPeriod: Optional[str] = None


class ListCustomLineItemsFilter(BaseValidatorModel):
    Names: Optional[List[str]] = None
    BillingGroups: Optional[List[str]] = None
    Arns: Optional[List[str]] = None
    AccountIds: Optional[List[str]] = None


class ListPricingPlansAssociatedWithPricingRuleInput(BaseValidatorModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPricingPlansFilter(BaseValidatorModel):
    Arns: Optional[List[str]] = None


class PricingPlanListElement(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Size: Optional[int] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None


class ListPricingRulesAssociatedToPricingPlanInput(BaseValidatorModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPricingRulesFilter(BaseValidatorModel):
    Arns: Optional[List[str]] = None


class ListResourcesAssociatedToCustomLineItemFilter(BaseValidatorModel):
    Relationship: Optional[CustomLineItemRelationshipType] = None


class ListResourcesAssociatedToCustomLineItemResponseElement(BaseValidatorModel):
    Arn: Optional[str] = None
    Relationship: Optional[CustomLineItemRelationshipType] = None
    EndBillingPeriod: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateBillingGroupAccountGrouping(BaseValidatorModel):
    AutoAssociate: Optional[bool] = None


class UpdateCustomLineItemFlatChargeDetails(BaseValidatorModel):
    ChargeValue: float


class UpdateCustomLineItemPercentageChargeDetails(BaseValidatorModel):
    PercentageValue: float


class UpdateFreeTierConfig(BaseValidatorModel):
    Activated: bool


class UpdatePricingPlanInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class AssociateAccountsOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class AssociatePricingRulesOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateBillingGroupOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreatePricingPlanOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreatePricingRuleOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeleteBillingGroupOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeleteCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeletePricingPlanOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeletePricingRuleOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DisassociateAccountsOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DisassociatePricingRulesOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class ListAccountAssociationsOutput(BaseValidatorModel):
    LinkedAccounts: List[AccountAssociationsListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPricingPlansAssociatedWithPricingRuleOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingRuleArn: str
    PricingPlanArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPricingRulesAssociatedToPricingPlanOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingPlanArn: str
    PricingRuleArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdatePricingPlanOutput(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Size: int
    LastModifiedTime: int
    ResponseMetadata: ResponseMetadata


class AssociateResourceResponseElement(BaseValidatorModel):
    Arn: Optional[str] = None
    Error: Optional[AssociateResourceError] = None


class DisassociateResourceResponseElement(BaseValidatorModel):
    Arn: Optional[str] = None
    Error: Optional[AssociateResourceError] = None


class BillingGroupCostReportResultElement(BaseValidatorModel):
    Arn: Optional[str] = None
    AWSCost: Optional[str] = None
    ProformaCost: Optional[str] = None
    Margin: Optional[str] = None
    MarginPercentage: Optional[str] = None
    Currency: Optional[str] = None
    Attributes: Optional[List[Attribute]] = None


class BatchAssociateResourcesToCustomLineItemInput(BaseValidatorModel):
    TargetArn: str
    ResourceArns: List[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


class BatchDisassociateResourcesFromCustomLineItemInput(BaseValidatorModel):
    TargetArn: str
    ResourceArns: List[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


class DeleteCustomLineItemInput(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


class ListBillingGroupCostReportsOutput(BaseValidatorModel):
    BillingGroupCostReports: List[BillingGroupCostReportElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateBillingGroupInput(BaseValidatorModel):
    Name: str
    AccountGrouping: AccountGrouping
    ComputationPreference: ComputationPreference
    ClientToken: Optional[str] = None
    PrimaryAccountId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class BillingGroupListElement(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    PrimaryAccountId: Optional[str] = None
    ComputationPreference: Optional[ComputationPreference] = None
    Size: Optional[int] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    Status: Optional[BillingGroupStatusType] = None
    StatusReason: Optional[str] = None
    AccountGrouping: Optional[ListBillingGroupAccountGrouping] = None


class GetBillingGroupCostReportInput(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[BillingPeriodRange] = None
    GroupBy: Optional[List[GroupByAttributeNameType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class CreateTieringInput(BaseValidatorModel):
    FreeTier: CreateFreeTierConfig


class Tiering(BaseValidatorModel):
    FreeTier: FreeTierConfig

LineItemFilterUnion = Union[LineItemFilter, LineItemFilterOutput]


class ListAccountAssociationsInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilter] = None
    NextToken: Optional[str] = None


class ListAccountAssociationsInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPricingPlansAssociatedWithPricingRuleInputPaginate(BaseValidatorModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPricingRulesAssociatedToPricingPlanInputPaginate(BaseValidatorModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillingGroupCostReportsInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillingGroupCostReportsInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilter] = None


class ListBillingGroupsInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillingGroupsInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilter] = None


class ListCustomLineItemChargeDetails(BaseValidatorModel):
    Type: CustomLineItemTypeType
    Flat: Optional[ListCustomLineItemFlatChargeDetails] = None
    Percentage: Optional[ListCustomLineItemPercentageChargeDetails] = None
    LineItemFilters: Optional[List[LineItemFilterOutput]] = None


class ListCustomLineItemVersionsFilter(BaseValidatorModel):
    BillingPeriodRange: Optional[ListCustomLineItemVersionsBillingPeriodRangeFilter] = None


class ListCustomLineItemsInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomLineItemsInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilter] = None


class ListPricingPlansInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPricingPlansInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPricingPlansOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingPlans: List[PricingPlanListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPricingRulesInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPricingRulesInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListResourcesAssociatedToCustomLineItemInputPaginate(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourcesAssociatedToCustomLineItemInput(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilter] = None


class ListResourcesAssociatedToCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    AssociatedResources: List[ListResourcesAssociatedToCustomLineItemResponseElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateBillingGroupInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[BillingGroupStatusType] = None
    ComputationPreference: Optional[ComputationPreference] = None
    Description: Optional[str] = None
    AccountGrouping: Optional[UpdateBillingGroupAccountGrouping] = None


class UpdateBillingGroupOutput(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    PrimaryAccountId: str
    PricingPlanArn: str
    Size: int
    LastModifiedTime: int
    Status: BillingGroupStatusType
    StatusReason: str
    AccountGrouping: UpdateBillingGroupAccountGrouping
    ResponseMetadata: ResponseMetadata


class UpdateTieringInput(BaseValidatorModel):
    FreeTier: UpdateFreeTierConfig


class BatchAssociateResourcesToCustomLineItemOutput(BaseValidatorModel):
    SuccessfullyAssociatedResources: List[AssociateResourceResponseElement]
    FailedAssociatedResources: List[AssociateResourceResponseElement]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateResourcesFromCustomLineItemOutput(BaseValidatorModel):
    SuccessfullyDisassociatedResources: List[DisassociateResourceResponseElement]
    FailedDisassociatedResources: List[DisassociateResourceResponseElement]
    ResponseMetadata: ResponseMetadata


class GetBillingGroupCostReportOutput(BaseValidatorModel):
    BillingGroupCostReportResults: List[BillingGroupCostReportResultElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBillingGroupsOutput(BaseValidatorModel):
    BillingGroups: List[BillingGroupListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreatePricingRuleInput(BaseValidatorModel):
    Name: str
    Scope: PricingRuleScopeType
    Type: PricingRuleTypeType
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    ModifierPercentage: Optional[float] = None
    Service: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    BillingEntity: Optional[str] = None
    Tiering: Optional[CreateTieringInput] = None
    UsageType: Optional[str] = None
    Operation: Optional[str] = None


class PricingRuleListElement(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Scope: Optional[PricingRuleScopeType] = None
    Type: Optional[PricingRuleTypeType] = None
    ModifierPercentage: Optional[float] = None
    Service: Optional[str] = None
    AssociatedPricingPlanCount: Optional[int] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    BillingEntity: Optional[str] = None
    Tiering: Optional[Tiering] = None
    UsageType: Optional[str] = None
    Operation: Optional[str] = None


class CustomLineItemChargeDetails(BaseValidatorModel):
    Type: CustomLineItemTypeType
    Flat: Optional[CustomLineItemFlatChargeDetails] = None
    Percentage: Optional[CustomLineItemPercentageChargeDetails] = None
    LineItemFilters: Optional[List[LineItemFilterUnion]] = None


class UpdateCustomLineItemChargeDetails(BaseValidatorModel):
    Flat: Optional[UpdateCustomLineItemFlatChargeDetails] = None
    Percentage: Optional[UpdateCustomLineItemPercentageChargeDetails] = None
    LineItemFilters: Optional[List[LineItemFilterUnion]] = None


class CustomLineItemListElement(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ChargeDetails: Optional[ListCustomLineItemChargeDetails] = None
    CurrencyCode: Optional[CurrencyCodeType] = None
    Description: Optional[str] = None
    ProductCode: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    AssociationSize: Optional[int] = None
    AccountId: Optional[str] = None


class CustomLineItemVersionListElement(BaseValidatorModel):
    Name: Optional[str] = None
    ChargeDetails: Optional[ListCustomLineItemChargeDetails] = None
    CurrencyCode: Optional[CurrencyCodeType] = None
    Description: Optional[str] = None
    ProductCode: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    AssociationSize: Optional[int] = None
    StartBillingPeriod: Optional[str] = None
    EndBillingPeriod: Optional[str] = None
    Arn: Optional[str] = None
    StartTime: Optional[int] = None
    AccountId: Optional[str] = None


class UpdateCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    BillingGroupArn: str
    Name: str
    Description: str
    ChargeDetails: ListCustomLineItemChargeDetails
    LastModifiedTime: int
    AssociationSize: int
    ResponseMetadata: ResponseMetadata


class ListCustomLineItemVersionsInputPaginate(BaseValidatorModel):
    Arn: str
    Filters: Optional[ListCustomLineItemVersionsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomLineItemVersionsInput(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemVersionsFilter] = None


class UpdatePricingRuleInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PricingRuleTypeType] = None
    ModifierPercentage: Optional[float] = None
    Tiering: Optional[UpdateTieringInput] = None


class UpdatePricingRuleOutput(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Scope: PricingRuleScopeType
    Type: PricingRuleTypeType
    ModifierPercentage: float
    Service: str
    AssociatedPricingPlanCount: int
    LastModifiedTime: int
    BillingEntity: str
    Tiering: UpdateTieringInput
    UsageType: str
    Operation: str
    ResponseMetadata: ResponseMetadata


class ListPricingRulesOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingRules: List[PricingRuleListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateCustomLineItemInput(BaseValidatorModel):
    Name: str
    Description: str
    BillingGroupArn: str
    ChargeDetails: CustomLineItemChargeDetails
    ClientToken: Optional[str] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None
    Tags: Optional[Dict[str, str]] = None
    AccountId: Optional[str] = None


class UpdateCustomLineItemInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ChargeDetails: Optional[UpdateCustomLineItemChargeDetails] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


class ListCustomLineItemsOutput(BaseValidatorModel):
    CustomLineItems: List[CustomLineItemListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCustomLineItemVersionsOutput(BaseValidatorModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None