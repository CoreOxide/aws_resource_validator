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


# This class is the input for the 'associate_accounts' function.
class AssociateAccountsInput(BaseValidatorModel):
    Arn: str
    AccountIds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_pricing_rules' function.
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


# This class is the input for the 'create_pricing_plan' function.
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


# This class is the input for the 'delete_billing_group' function.
class DeleteBillingGroupInput(BaseValidatorModel):
    Arn: str


# This class is the input for the 'delete_pricing_plan' function.
class DeletePricingPlanInput(BaseValidatorModel):
    Arn: str


# This class is the input for the 'delete_pricing_rule' function.
class DeletePricingRuleInput(BaseValidatorModel):
    Arn: str


# This class is the input for the 'disassociate_accounts' function.
class DisassociateAccountsInput(BaseValidatorModel):
    Arn: str
    AccountIds: List[str]


# This class is the input for the 'disassociate_pricing_rules' function.
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


# This class is the input for the 'list_pricing_plans_associated_with_pricing_rule' function.
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


# This class is the input for the 'list_pricing_rules_associated_to_pricing_plan' function.
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


# This class is the input for the 'list_tags_for_resource' function.
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


# This class is the input for the 'update_pricing_plan' function.
class UpdatePricingPlanInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None


# This class is the output for the 'associate_accounts' function.
class AssociateAccountsOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_pricing_rules' function.
class AssociatePricingRulesOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_billing_group' function.
class CreateBillingGroupOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_custom_line_item' function.
class CreateCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_pricing_plan' function.
class CreatePricingPlanOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_pricing_rule' function.
class CreatePricingRuleOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_billing_group' function.
class DeleteBillingGroupOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_custom_line_item' function.
class DeleteCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pricing_plan' function.
class DeletePricingPlanOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pricing_rule' function.
class DeletePricingRuleOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_accounts' function.
class DisassociateAccountsOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_pricing_rules' function.
class DisassociatePricingRulesOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_account_associations' function.
class ListAccountAssociationsOutput(BaseValidatorModel):
    LinkedAccounts: List[AccountAssociationsListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pricing_plans_associated_with_pricing_rule' function.
class ListPricingPlansAssociatedWithPricingRuleOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingRuleArn: str
    PricingPlanArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pricing_rules_associated_to_pricing_plan' function.
class ListPricingRulesAssociatedToPricingPlanOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingPlanArn: str
    PricingRuleArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pricing_plan' function.
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


# This class is the input for the 'batch_associate_resources_to_custom_line_item' function.
class BatchAssociateResourcesToCustomLineItemInput(BaseValidatorModel):
    TargetArn: str
    ResourceArns: List[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


# This class is the input for the 'batch_disassociate_resources_from_custom_line_item' function.
class BatchDisassociateResourcesFromCustomLineItemInput(BaseValidatorModel):
    TargetArn: str
    ResourceArns: List[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


# This class is the input for the 'delete_custom_line_item' function.
class DeleteCustomLineItemInput(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


# This class is the output for the 'list_billing_group_cost_reports' function.
class ListBillingGroupCostReportsOutput(BaseValidatorModel):
    BillingGroupCostReports: List[BillingGroupCostReportElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_billing_group' function.
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


# This class is the input for the 'get_billing_group_cost_report' function.
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


# This class is the input for the 'list_account_associations' function.
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


# This class is the input for the 'list_billing_group_cost_reports' function.
class ListBillingGroupCostReportsInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilter] = None


class ListBillingGroupsInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_billing_groups' function.
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


# This class is the input for the 'list_custom_line_items' function.
class ListCustomLineItemsInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilter] = None


class ListPricingPlansInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_pricing_plans' function.
class ListPricingPlansInput(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_pricing_plans' function.
class ListPricingPlansOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingPlans: List[PricingPlanListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPricingRulesInputPaginate(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_pricing_rules' function.
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


# This class is the input for the 'list_resources_associated_to_custom_line_item' function.
class ListResourcesAssociatedToCustomLineItemInput(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilter] = None


# This class is the output for the 'list_resources_associated_to_custom_line_item' function.
class ListResourcesAssociatedToCustomLineItemOutput(BaseValidatorModel):
    Arn: str
    AssociatedResources: List[ListResourcesAssociatedToCustomLineItemResponseElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'update_billing_group' function.
class UpdateBillingGroupInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[BillingGroupStatusType] = None
    ComputationPreference: Optional[ComputationPreference] = None
    Description: Optional[str] = None
    AccountGrouping: Optional[UpdateBillingGroupAccountGrouping] = None


# This class is the output for the 'update_billing_group' function.
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


# This class is the output for the 'batch_associate_resources_to_custom_line_item' function.
class BatchAssociateResourcesToCustomLineItemOutput(BaseValidatorModel):
    SuccessfullyAssociatedResources: List[AssociateResourceResponseElement]
    FailedAssociatedResources: List[AssociateResourceResponseElement]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_resources_from_custom_line_item' function.
class BatchDisassociateResourcesFromCustomLineItemOutput(BaseValidatorModel):
    SuccessfullyDisassociatedResources: List[DisassociateResourceResponseElement]
    FailedDisassociatedResources: List[DisassociateResourceResponseElement]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_billing_group_cost_report' function.
class GetBillingGroupCostReportOutput(BaseValidatorModel):
    BillingGroupCostReportResults: List[BillingGroupCostReportResultElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_billing_groups' function.
class ListBillingGroupsOutput(BaseValidatorModel):
    BillingGroups: List[BillingGroupListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_pricing_rule' function.
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


# This class is the output for the 'update_custom_line_item' function.
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


# This class is the input for the 'list_custom_line_item_versions' function.
class ListCustomLineItemVersionsInput(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemVersionsFilter] = None


# This class is the input for the 'update_pricing_rule' function.
class UpdatePricingRuleInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PricingRuleTypeType] = None
    ModifierPercentage: Optional[float] = None
    Tiering: Optional[UpdateTieringInput] = None


# This class is the output for the 'update_pricing_rule' function.
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


# This class is the output for the 'list_pricing_rules' function.
class ListPricingRulesOutput(BaseValidatorModel):
    BillingPeriod: str
    PricingRules: List[PricingRuleListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_custom_line_item' function.
class CreateCustomLineItemInput(BaseValidatorModel):
    Name: str
    Description: str
    BillingGroupArn: str
    ChargeDetails: CustomLineItemChargeDetails
    ClientToken: Optional[str] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None
    Tags: Optional[Dict[str, str]] = None
    AccountId: Optional[str] = None


# This class is the input for the 'update_custom_line_item' function.
class UpdateCustomLineItemInput(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ChargeDetails: Optional[UpdateCustomLineItemChargeDetails] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRange] = None


# This class is the output for the 'list_custom_line_items' function.
class ListCustomLineItemsOutput(BaseValidatorModel):
    CustomLineItems: List[CustomLineItemListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_custom_line_item_versions' function.
class ListCustomLineItemVersionsOutput(BaseValidatorModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None