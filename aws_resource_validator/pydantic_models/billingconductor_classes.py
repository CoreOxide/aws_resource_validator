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
from aws_resource_validator.pydantic_models.billingconductor_constants import *

class AccountAssociationsListElementTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    AccountName: Optional[str] = None
    AccountEmail: Optional[str] = None


class AccountGroupingTypeDef(BaseValidatorModel):
    LinkedAccountIds: Sequence[str]
    AutoAssociate: Optional[bool] = None


class AssociateAccountsInputTypeDef(BaseValidatorModel):
    Arn: str
    AccountIds: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociatePricingRulesInputTypeDef(BaseValidatorModel):
    Arn: str
    PricingRuleArns: Sequence[str]


class AssociateResourceErrorTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Reason: Optional[AssociateResourceErrorReasonType] = None


class AttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class CustomLineItemBillingPeriodRangeTypeDef(BaseValidatorModel):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: Optional[str] = None


class BillingGroupCostReportElementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AWSCost: Optional[str] = None
    ProformaCost: Optional[str] = None
    Margin: Optional[str] = None
    MarginPercentage: Optional[str] = None
    Currency: Optional[str] = None


class ComputationPreferenceTypeDef(BaseValidatorModel):
    PricingPlanArn: str


class ListBillingGroupAccountGroupingTypeDef(BaseValidatorModel):
    AutoAssociate: Optional[bool] = None


class BillingPeriodRangeTypeDef(BaseValidatorModel):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: str


class CreateFreeTierConfigTypeDef(BaseValidatorModel):
    Activated: bool


class CreatePricingPlanInputTypeDef(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PricingRuleArns: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class CustomLineItemFlatChargeDetailsTypeDef(BaseValidatorModel):
    ChargeValue: float


class CustomLineItemPercentageChargeDetailsTypeDef(BaseValidatorModel):
    PercentageValue: float
    AssociatedValues: Optional[Sequence[str]] = None


class DeleteBillingGroupInputTypeDef(BaseValidatorModel):
    Arn: str


class DeletePricingPlanInputTypeDef(BaseValidatorModel):
    Arn: str


class DeletePricingRuleInputTypeDef(BaseValidatorModel):
    Arn: str


class DisassociateAccountsInputTypeDef(BaseValidatorModel):
    Arn: str
    AccountIds: Sequence[str]


class DisassociatePricingRulesInputTypeDef(BaseValidatorModel):
    Arn: str
    PricingRuleArns: Sequence[str]


class FreeTierConfigTypeDef(BaseValidatorModel):
    Activated: bool


class LineItemFilterOutputTypeDef(BaseValidatorModel):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: List[Literal["SAVINGS_PLAN_NEGATION"]]


class LineItemFilterTypeDef(BaseValidatorModel):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: Sequence[Literal["SAVINGS_PLAN_NEGATION"]]


class ListAccountAssociationsFilterTypeDef(BaseValidatorModel):
    Association: Optional[str] = None
    AccountId: Optional[str] = None
    AccountIds: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBillingGroupCostReportsFilterTypeDef(BaseValidatorModel):
    BillingGroupArns: Optional[Sequence[str]] = None


class ListBillingGroupsFilterTypeDef(BaseValidatorModel):
    Arns: Optional[Sequence[str]] = None
    PricingPlan: Optional[str] = None
    Statuses: Optional[Sequence[BillingGroupStatusType]] = None
    AutoAssociate: Optional[bool] = None


class ListCustomLineItemFlatChargeDetailsTypeDef(BaseValidatorModel):
    ChargeValue: float


class ListCustomLineItemPercentageChargeDetailsTypeDef(BaseValidatorModel):
    PercentageValue: float


class ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef(BaseValidatorModel):
    StartBillingPeriod: Optional[str] = None
    EndBillingPeriod: Optional[str] = None


class ListCustomLineItemsFilterTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    BillingGroups: Optional[Sequence[str]] = None
    Arns: Optional[Sequence[str]] = None
    AccountIds: Optional[Sequence[str]] = None


class ListPricingPlansAssociatedWithPricingRuleInputTypeDef(BaseValidatorModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPricingPlansFilterTypeDef(BaseValidatorModel):
    Arns: Optional[Sequence[str]] = None


class PricingPlanListElementTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Size: Optional[int] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None


class ListPricingRulesAssociatedToPricingPlanInputTypeDef(BaseValidatorModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPricingRulesFilterTypeDef(BaseValidatorModel):
    Arns: Optional[Sequence[str]] = None


class ListResourcesAssociatedToCustomLineItemFilterTypeDef(BaseValidatorModel):
    Relationship: Optional[CustomLineItemRelationshipType] = None


class ListResourcesAssociatedToCustomLineItemResponseElementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Relationship: Optional[CustomLineItemRelationshipType] = None
    EndBillingPeriod: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateBillingGroupAccountGroupingTypeDef(BaseValidatorModel):
    AutoAssociate: Optional[bool] = None


class UpdateCustomLineItemFlatChargeDetailsTypeDef(BaseValidatorModel):
    ChargeValue: float


class UpdateCustomLineItemPercentageChargeDetailsTypeDef(BaseValidatorModel):
    PercentageValue: float


class UpdateFreeTierConfigTypeDef(BaseValidatorModel):
    Activated: bool


class UpdatePricingPlanInputTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class AssociateAccountsOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatePricingRulesOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBillingGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomLineItemOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePricingPlanOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePricingRuleOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBillingGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCustomLineItemOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePricingPlanOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePricingRuleOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateAccountsOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociatePricingRulesOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountAssociationsOutputTypeDef(BaseValidatorModel):
    LinkedAccounts: List[AccountAssociationsListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPricingPlansAssociatedWithPricingRuleOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingRuleArn: str
    PricingPlanArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPricingRulesAssociatedToPricingPlanOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingPlanArn: str
    PricingRuleArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePricingPlanOutputTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Size: int
    LastModifiedTime: int
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateResourceResponseElementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Error: Optional[AssociateResourceErrorTypeDef] = None


class DisassociateResourceResponseElementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Error: Optional[AssociateResourceErrorTypeDef] = None


class BillingGroupCostReportResultElementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AWSCost: Optional[str] = None
    ProformaCost: Optional[str] = None
    Margin: Optional[str] = None
    MarginPercentage: Optional[str] = None
    Currency: Optional[str] = None
    Attributes: Optional[List[AttributeTypeDef]] = None


class BatchAssociateResourcesToCustomLineItemInputTypeDef(BaseValidatorModel):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None


class BatchDisassociateResourcesFromCustomLineItemInputTypeDef(BaseValidatorModel):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None


class DeleteCustomLineItemInputTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None


class ListBillingGroupCostReportsOutputTypeDef(BaseValidatorModel):
    BillingGroupCostReports: List[BillingGroupCostReportElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateBillingGroupInputTypeDef(BaseValidatorModel):
    Name: str
    AccountGrouping: AccountGroupingTypeDef
    ComputationPreference: ComputationPreferenceTypeDef
    ClientToken: Optional[str] = None
    PrimaryAccountId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class BillingGroupListElementTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    PrimaryAccountId: Optional[str] = None
    ComputationPreference: Optional[ComputationPreferenceTypeDef] = None
    Size: Optional[int] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    Status: Optional[BillingGroupStatusType] = None
    StatusReason: Optional[str] = None
    AccountGrouping: Optional[ListBillingGroupAccountGroupingTypeDef] = None


class GetBillingGroupCostReportInputTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[BillingPeriodRangeTypeDef] = None
    GroupBy: Optional[Sequence[GroupByAttributeNameType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class CreateTieringInputTypeDef(BaseValidatorModel):
    FreeTier: CreateFreeTierConfigTypeDef


class TieringTypeDef(BaseValidatorModel):
    FreeTier: FreeTierConfigTypeDef


class ListAccountAssociationsInputTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilterTypeDef] = None
    NextToken: Optional[str] = None


class ListAccountAssociationsInputPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef(BaseValidatorModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef(BaseValidatorModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillingGroupCostReportsInputPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillingGroupCostReportsInputTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilterTypeDef] = None


class ListBillingGroupsInputPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillingGroupsInputTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilterTypeDef] = None


class ListCustomLineItemVersionsFilterTypeDef(BaseValidatorModel):
    BillingPeriodRange: Optional[ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef] = None


class ListCustomLineItemsInputPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomLineItemsInputTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilterTypeDef] = None


class ListPricingPlansInputPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPricingPlansInputTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPricingPlansOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingPlans: List[PricingPlanListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPricingRulesInputPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPricingRulesInputTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourcesAssociatedToCustomLineItemInputTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilterTypeDef] = None


class ListResourcesAssociatedToCustomLineItemOutputTypeDef(BaseValidatorModel):
    Arn: str
    AssociatedResources: List[ListResourcesAssociatedToCustomLineItemResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateBillingGroupInputTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[BillingGroupStatusType] = None
    ComputationPreference: Optional[ComputationPreferenceTypeDef] = None
    Description: Optional[str] = None
    AccountGrouping: Optional[UpdateBillingGroupAccountGroupingTypeDef] = None


class UpdateBillingGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    PrimaryAccountId: str
    PricingPlanArn: str
    Size: int
    LastModifiedTime: int
    Status: BillingGroupStatusType
    StatusReason: str
    AccountGrouping: UpdateBillingGroupAccountGroupingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTieringInputTypeDef(BaseValidatorModel):
    FreeTier: UpdateFreeTierConfigTypeDef


class BatchAssociateResourcesToCustomLineItemOutputTypeDef(BaseValidatorModel):
    SuccessfullyAssociatedResources: List[AssociateResourceResponseElementTypeDef]
    FailedAssociatedResources: List[AssociateResourceResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDisassociateResourcesFromCustomLineItemOutputTypeDef(BaseValidatorModel):
    SuccessfullyDisassociatedResources: List[DisassociateResourceResponseElementTypeDef]
    FailedDisassociatedResources: List[DisassociateResourceResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBillingGroupCostReportOutputTypeDef(BaseValidatorModel):
    BillingGroupCostReportResults: List[BillingGroupCostReportResultElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBillingGroupsOutputTypeDef(BaseValidatorModel):
    BillingGroups: List[BillingGroupListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LineItemFilterUnionTypeDef(BaseValidatorModel):
    pass


class UpdateCustomLineItemChargeDetailsTypeDef(BaseValidatorModel):
    Flat: Optional[UpdateCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[UpdateCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[Sequence[LineItemFilterUnionTypeDef]] = None


class ListCustomLineItemChargeDetailsTypeDef(BaseValidatorModel):
    pass


class CustomLineItemListElementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ChargeDetails: Optional[ListCustomLineItemChargeDetailsTypeDef] = None
    CurrencyCode: Optional[CurrencyCodeType] = None
    Description: Optional[str] = None
    ProductCode: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    AssociationSize: Optional[int] = None
    AccountId: Optional[str] = None


class CustomLineItemVersionListElementTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ChargeDetails: Optional[ListCustomLineItemChargeDetailsTypeDef] = None
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


class UpdateCustomLineItemOutputTypeDef(BaseValidatorModel):
    Arn: str
    BillingGroupArn: str
    Name: str
    Description: str
    ChargeDetails: ListCustomLineItemChargeDetailsTypeDef
    LastModifiedTime: int
    AssociationSize: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomLineItemVersionsInputPaginateTypeDef(BaseValidatorModel):
    Arn: str
    Filters: Optional[ListCustomLineItemVersionsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomLineItemVersionsInputTypeDef(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemVersionsFilterTypeDef] = None


class PricingRuleListElementTypeDef(BaseValidatorModel):
    pass


class ListPricingRulesOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingRules: List[PricingRuleListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CustomLineItemChargeDetailsTypeDef(BaseValidatorModel):
    pass


class CreateCustomLineItemInputTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    BillingGroupArn: str
    ChargeDetails: CustomLineItemChargeDetailsTypeDef
    ClientToken: Optional[str] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    AccountId: Optional[str] = None


class UpdateCustomLineItemInputTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ChargeDetails: Optional[UpdateCustomLineItemChargeDetailsTypeDef] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None


class ListCustomLineItemsOutputTypeDef(BaseValidatorModel):
    CustomLineItems: List[CustomLineItemListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCustomLineItemVersionsOutputTypeDef(BaseValidatorModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


