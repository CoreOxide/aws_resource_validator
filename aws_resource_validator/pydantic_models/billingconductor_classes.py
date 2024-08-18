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
from aws_resource_validator.pydantic_models.billingconductor_constants import *

class AccountAssociationsListElementTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    AccountName: Optional[str] = None
    AccountEmail: Optional[str] = None

class AccountGroupingTypeDef(BaseValidatorModel):
    LinkedAccountIds: Sequence[str]
    AutoAssociate: Optional[bool] = None

class AssociateAccountsInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociatePricingRulesInputRequestTypeDef(BaseValidatorModel):
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

class CreatePricingPlanInputRequestTypeDef(BaseValidatorModel):
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

class LineItemFilterTypeDef(BaseValidatorModel):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: Sequence[Literal["SAVINGS_PLAN_NEGATION"]]

class DeleteBillingGroupInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeletePricingPlanInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeletePricingRuleInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class DisassociateAccountsInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    AccountIds: Sequence[str]

class DisassociatePricingRulesInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    PricingRuleArns: Sequence[str]

class FreeTierConfigTypeDef(BaseValidatorModel):
    Activated: bool

class LineItemFilterPaginatorTypeDef(BaseValidatorModel):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: List[Literal["SAVINGS_PLAN_NEGATION"]]

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

class ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef(BaseValidatorModel):
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

class ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class UpdatePricingPlanInputRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingPlansAssociatedWithPricingRuleOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingRuleArn: str
    PricingPlanArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingRulesAssociatedToPricingPlanOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingPlanArn: str
    PricingRuleArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class BatchAssociateResourcesToCustomLineItemInputRequestTypeDef(BaseValidatorModel):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef(BaseValidatorModel):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class DeleteCustomLineItemInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class ListBillingGroupCostReportsOutputTypeDef(BaseValidatorModel):
    BillingGroupCostReports: List[BillingGroupCostReportElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBillingGroupInputRequestTypeDef(BaseValidatorModel):
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

class GetBillingGroupCostReportInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriodRange: Optional[BillingPeriodRangeTypeDef] = None
    GroupBy: Optional[Sequence[GroupByAttributeNameType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class CreateTieringInputTypeDef(BaseValidatorModel):
    FreeTier: CreateFreeTierConfigTypeDef

class CustomLineItemChargeDetailsTypeDef(BaseValidatorModel):
    Type: CustomLineItemTypeType
    Flat: Optional[CustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[CustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[Sequence[LineItemFilterTypeDef]] = None

class TieringTypeDef(BaseValidatorModel):
    FreeTier: FreeTierConfigTypeDef

class ListAccountAssociationsInputRequestTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilterTypeDef] = None
    NextToken: Optional[str] = None

class ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef(BaseValidatorModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef(BaseValidatorModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupCostReportsInputRequestTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilterTypeDef] = None

class ListBillingGroupsInputListBillingGroupsPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupsInputRequestTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilterTypeDef] = None

class ListCustomLineItemChargeDetailsPaginatorTypeDef(BaseValidatorModel):
    Type: CustomLineItemTypeType
    Flat: Optional[ListCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[ListCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[List[LineItemFilterPaginatorTypeDef]] = None

class ListCustomLineItemChargeDetailsTypeDef(BaseValidatorModel):
    Type: CustomLineItemTypeType
    Flat: Optional[ListCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[ListCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[List[LineItemFilterTypeDef]] = None

class ListCustomLineItemVersionsFilterTypeDef(BaseValidatorModel):
    BillingPeriodRange: Optional[       ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef     ] = None

class ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomLineItemsInputRequestTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilterTypeDef] = None

class ListPricingPlansInputListPricingPlansPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingPlansInputRequestTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPricingPlansOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingPlans: List[PricingPlanListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingRulesInputListPricingRulesPaginateTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingRulesInputRequestTypeDef(BaseValidatorModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesAssociatedToCustomLineItemInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilterTypeDef] = None

class ListResourcesAssociatedToCustomLineItemOutputTypeDef(BaseValidatorModel):
    Arn: str
    AssociatedResources: List[ListResourcesAssociatedToCustomLineItemResponseElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBillingGroupInputRequestTypeDef(BaseValidatorModel):
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

class UpdateCustomLineItemChargeDetailsTypeDef(BaseValidatorModel):
    Flat: Optional[UpdateCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[UpdateCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[Sequence[LineItemFilterTypeDef]] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBillingGroupsOutputTypeDef(BaseValidatorModel):
    BillingGroups: List[BillingGroupListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePricingRuleInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: PricingRuleScopeType
    Type: PricingRuleTypeType
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    ModifierPercentage: Optional[float] = None
    Service: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    BillingEntity: Optional[str] = None
    Tiering: Optional[CreateTieringInputTypeDef] = None
    UsageType: Optional[str] = None
    Operation: Optional[str] = None

class CreateCustomLineItemInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    BillingGroupArn: str
    ChargeDetails: CustomLineItemChargeDetailsTypeDef
    ClientToken: Optional[str] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    AccountId: Optional[str] = None

class PricingRuleListElementTypeDef(BaseValidatorModel):
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
    Tiering: Optional[TieringTypeDef] = None
    UsageType: Optional[str] = None
    Operation: Optional[str] = None

class CustomLineItemListElementPaginatorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ChargeDetails: Optional[ListCustomLineItemChargeDetailsPaginatorTypeDef] = None
    CurrencyCode: Optional[CurrencyCodeType] = None
    Description: Optional[str] = None
    ProductCode: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None
    AssociationSize: Optional[int] = None
    AccountId: Optional[str] = None

class CustomLineItemVersionListElementPaginatorTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ChargeDetails: Optional[ListCustomLineItemChargeDetailsPaginatorTypeDef] = None
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

class ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef(BaseValidatorModel):
    Arn: str
    Filters: Optional[ListCustomLineItemVersionsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomLineItemVersionsInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemVersionsFilterTypeDef] = None

class UpdateCustomLineItemInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ChargeDetails: Optional[UpdateCustomLineItemChargeDetailsTypeDef] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class UpdatePricingRuleInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PricingRuleTypeType] = None
    ModifierPercentage: Optional[float] = None
    Tiering: Optional[UpdateTieringInputTypeDef] = None

class UpdatePricingRuleOutputTypeDef(BaseValidatorModel):
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
    Tiering: UpdateTieringInputTypeDef
    UsageType: str
    Operation: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingRulesOutputTypeDef(BaseValidatorModel):
    BillingPeriod: str
    PricingRules: List[PricingRuleListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemsOutputPaginatorTypeDef(BaseValidatorModel):
    CustomLineItems: List[CustomLineItemListElementPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemVersionsOutputPaginatorTypeDef(BaseValidatorModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElementPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemsOutputTypeDef(BaseValidatorModel):
    CustomLineItems: List[CustomLineItemListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemVersionsOutputTypeDef(BaseValidatorModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

