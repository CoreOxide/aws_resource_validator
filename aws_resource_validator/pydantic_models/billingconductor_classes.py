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
from aws_resource_validator.pydantic_models.billingconductor_constants import *

class AccountAssociationsListElementTypeDef(BaseModel):
    AccountId: Optional[str] = None
    BillingGroupArn: Optional[str] = None
    AccountName: Optional[str] = None
    AccountEmail: Optional[str] = None

class AccountGroupingTypeDef(BaseModel):
    LinkedAccountIds: Sequence[str]
    AutoAssociate: Optional[bool] = None

class AssociateAccountsInputRequestTypeDef(BaseModel):
    Arn: str
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociatePricingRulesInputRequestTypeDef(BaseModel):
    Arn: str
    PricingRuleArns: Sequence[str]

class AssociateResourceErrorTypeDef(BaseModel):
    Message: Optional[str] = None
    Reason: Optional[AssociateResourceErrorReasonType] = None

class AttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class CustomLineItemBillingPeriodRangeTypeDef(BaseModel):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: Optional[str] = None

class BillingGroupCostReportElementTypeDef(BaseModel):
    Arn: Optional[str] = None
    AWSCost: Optional[str] = None
    ProformaCost: Optional[str] = None
    Margin: Optional[str] = None
    MarginPercentage: Optional[str] = None
    Currency: Optional[str] = None

class ComputationPreferenceTypeDef(BaseModel):
    PricingPlanArn: str

class ListBillingGroupAccountGroupingTypeDef(BaseModel):
    AutoAssociate: Optional[bool] = None

class BillingPeriodRangeTypeDef(BaseModel):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: str

class CreateFreeTierConfigTypeDef(BaseModel):
    Activated: bool

class CreatePricingPlanInputRequestTypeDef(BaseModel):
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PricingRuleArns: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class CustomLineItemFlatChargeDetailsTypeDef(BaseModel):
    ChargeValue: float

class CustomLineItemPercentageChargeDetailsTypeDef(BaseModel):
    PercentageValue: float
    AssociatedValues: Optional[Sequence[str]] = None

class LineItemFilterTypeDef(BaseModel):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: Sequence[Literal["SAVINGS_PLAN_NEGATION"]]

class DeleteBillingGroupInputRequestTypeDef(BaseModel):
    Arn: str

class DeletePricingPlanInputRequestTypeDef(BaseModel):
    Arn: str

class DeletePricingRuleInputRequestTypeDef(BaseModel):
    Arn: str

class DisassociateAccountsInputRequestTypeDef(BaseModel):
    Arn: str
    AccountIds: Sequence[str]

class DisassociatePricingRulesInputRequestTypeDef(BaseModel):
    Arn: str
    PricingRuleArns: Sequence[str]

class FreeTierConfigTypeDef(BaseModel):
    Activated: bool

class LineItemFilterPaginatorTypeDef(BaseModel):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: List[Literal["SAVINGS_PLAN_NEGATION"]]

class ListAccountAssociationsFilterTypeDef(BaseModel):
    Association: Optional[str] = None
    AccountId: Optional[str] = None
    AccountIds: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBillingGroupCostReportsFilterTypeDef(BaseModel):
    BillingGroupArns: Optional[Sequence[str]] = None

class ListBillingGroupsFilterTypeDef(BaseModel):
    Arns: Optional[Sequence[str]] = None
    PricingPlan: Optional[str] = None
    Statuses: Optional[Sequence[BillingGroupStatusType]] = None
    AutoAssociate: Optional[bool] = None

class ListCustomLineItemFlatChargeDetailsTypeDef(BaseModel):
    ChargeValue: float

class ListCustomLineItemPercentageChargeDetailsTypeDef(BaseModel):
    PercentageValue: float

class ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef(BaseModel):
    StartBillingPeriod: Optional[str] = None
    EndBillingPeriod: Optional[str] = None

class ListCustomLineItemsFilterTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    BillingGroups: Optional[Sequence[str]] = None
    Arns: Optional[Sequence[str]] = None
    AccountIds: Optional[Sequence[str]] = None

class ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef(BaseModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPricingPlansFilterTypeDef(BaseModel):
    Arns: Optional[Sequence[str]] = None

class PricingPlanListElementTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Size: Optional[int] = None
    CreationTime: Optional[int] = None
    LastModifiedTime: Optional[int] = None

class ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef(BaseModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPricingRulesFilterTypeDef(BaseModel):
    Arns: Optional[Sequence[str]] = None

class ListResourcesAssociatedToCustomLineItemFilterTypeDef(BaseModel):
    Relationship: Optional[CustomLineItemRelationshipType] = None

class ListResourcesAssociatedToCustomLineItemResponseElementTypeDef(BaseModel):
    Arn: Optional[str] = None
    Relationship: Optional[CustomLineItemRelationshipType] = None
    EndBillingPeriod: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateBillingGroupAccountGroupingTypeDef(BaseModel):
    AutoAssociate: Optional[bool] = None

class UpdateCustomLineItemFlatChargeDetailsTypeDef(BaseModel):
    ChargeValue: float

class UpdateCustomLineItemPercentageChargeDetailsTypeDef(BaseModel):
    PercentageValue: float

class UpdateFreeTierConfigTypeDef(BaseModel):
    Activated: bool

class UpdatePricingPlanInputRequestTypeDef(BaseModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class AssociateAccountsOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePricingRulesOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBillingGroupOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomLineItemOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePricingPlanOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePricingRuleOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBillingGroupOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomLineItemOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePricingPlanOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePricingRuleOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateAccountsOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePricingRulesOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssociationsOutputTypeDef(BaseModel):
    LinkedAccounts: List[AccountAssociationsListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingPlansAssociatedWithPricingRuleOutputTypeDef(BaseModel):
    BillingPeriod: str
    PricingRuleArn: str
    PricingPlanArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingRulesAssociatedToPricingPlanOutputTypeDef(BaseModel):
    BillingPeriod: str
    PricingPlanArn: str
    PricingRuleArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePricingPlanOutputTypeDef(BaseModel):
    Arn: str
    Name: str
    Description: str
    Size: int
    LastModifiedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceResponseElementTypeDef(BaseModel):
    Arn: Optional[str] = None
    Error: Optional[AssociateResourceErrorTypeDef] = None

class DisassociateResourceResponseElementTypeDef(BaseModel):
    Arn: Optional[str] = None
    Error: Optional[AssociateResourceErrorTypeDef] = None

class BillingGroupCostReportResultElementTypeDef(BaseModel):
    Arn: Optional[str] = None
    AWSCost: Optional[str] = None
    ProformaCost: Optional[str] = None
    Margin: Optional[str] = None
    MarginPercentage: Optional[str] = None
    Currency: Optional[str] = None
    Attributes: Optional[List[AttributeTypeDef]] = None

class BatchAssociateResourcesToCustomLineItemInputRequestTypeDef(BaseModel):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef(BaseModel):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class DeleteCustomLineItemInputRequestTypeDef(BaseModel):
    Arn: str
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class ListBillingGroupCostReportsOutputTypeDef(BaseModel):
    BillingGroupCostReports: List[BillingGroupCostReportElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBillingGroupInputRequestTypeDef(BaseModel):
    Name: str
    AccountGrouping: AccountGroupingTypeDef
    ComputationPreference: ComputationPreferenceTypeDef
    ClientToken: Optional[str] = None
    PrimaryAccountId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class BillingGroupListElementTypeDef(BaseModel):
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

class GetBillingGroupCostReportInputRequestTypeDef(BaseModel):
    Arn: str
    BillingPeriodRange: Optional[BillingPeriodRangeTypeDef] = None
    GroupBy: Optional[Sequence[GroupByAttributeNameType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class CreateTieringInputTypeDef(BaseModel):
    FreeTier: CreateFreeTierConfigTypeDef

class CustomLineItemChargeDetailsTypeDef(BaseModel):
    Type: CustomLineItemTypeType
    Flat: Optional[CustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[CustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[Sequence[LineItemFilterTypeDef]] = None

class TieringTypeDef(BaseModel):
    FreeTier: FreeTierConfigTypeDef

class ListAccountAssociationsInputRequestTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilterTypeDef] = None
    NextToken: Optional[str] = None

class ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListAccountAssociationsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef(BaseModel):
    PricingRuleArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef(BaseModel):
    PricingPlanArn: str
    BillingPeriod: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupCostReportsInputRequestTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupCostReportsFilterTypeDef] = None

class ListBillingGroupsInputListBillingGroupsPaginateTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupsInputRequestTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListBillingGroupsFilterTypeDef] = None

class ListCustomLineItemChargeDetailsPaginatorTypeDef(BaseModel):
    Type: CustomLineItemTypeType
    Flat: Optional[ListCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[ListCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[List[LineItemFilterPaginatorTypeDef]] = None

class ListCustomLineItemChargeDetailsTypeDef(BaseModel):
    Type: CustomLineItemTypeType
    Flat: Optional[ListCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[ListCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[List[LineItemFilterTypeDef]] = None

class ListCustomLineItemVersionsFilterTypeDef(BaseModel):
    BillingPeriodRange: Optional[       ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef     ] = None

class ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomLineItemsInputRequestTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemsFilterTypeDef] = None

class ListPricingPlansInputListPricingPlansPaginateTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingPlansInputRequestTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingPlansFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPricingPlansOutputTypeDef(BaseModel):
    BillingPeriod: str
    PricingPlans: List[PricingPlanListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricingRulesInputListPricingRulesPaginateTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPricingRulesInputRequestTypeDef(BaseModel):
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListPricingRulesFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef(BaseModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesAssociatedToCustomLineItemInputRequestTypeDef(BaseModel):
    Arn: str
    BillingPeriod: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListResourcesAssociatedToCustomLineItemFilterTypeDef] = None

class ListResourcesAssociatedToCustomLineItemOutputTypeDef(BaseModel):
    Arn: str
    AssociatedResources: List[ListResourcesAssociatedToCustomLineItemResponseElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBillingGroupInputRequestTypeDef(BaseModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[BillingGroupStatusType] = None
    ComputationPreference: Optional[ComputationPreferenceTypeDef] = None
    Description: Optional[str] = None
    AccountGrouping: Optional[UpdateBillingGroupAccountGroupingTypeDef] = None

class UpdateBillingGroupOutputTypeDef(BaseModel):
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

class UpdateCustomLineItemChargeDetailsTypeDef(BaseModel):
    Flat: Optional[UpdateCustomLineItemFlatChargeDetailsTypeDef] = None
    Percentage: Optional[UpdateCustomLineItemPercentageChargeDetailsTypeDef] = None
    LineItemFilters: Optional[Sequence[LineItemFilterTypeDef]] = None

class UpdateTieringInputTypeDef(BaseModel):
    FreeTier: UpdateFreeTierConfigTypeDef

class BatchAssociateResourcesToCustomLineItemOutputTypeDef(BaseModel):
    SuccessfullyAssociatedResources: List[AssociateResourceResponseElementTypeDef]
    FailedAssociatedResources: List[AssociateResourceResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateResourcesFromCustomLineItemOutputTypeDef(BaseModel):
    SuccessfullyDisassociatedResources: List[DisassociateResourceResponseElementTypeDef]
    FailedDisassociatedResources: List[DisassociateResourceResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBillingGroupCostReportOutputTypeDef(BaseModel):
    BillingGroupCostReportResults: List[BillingGroupCostReportResultElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBillingGroupsOutputTypeDef(BaseModel):
    BillingGroups: List[BillingGroupListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePricingRuleInputRequestTypeDef(BaseModel):
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

class CreateCustomLineItemInputRequestTypeDef(BaseModel):
    Name: str
    Description: str
    BillingGroupArn: str
    ChargeDetails: CustomLineItemChargeDetailsTypeDef
    ClientToken: Optional[str] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    AccountId: Optional[str] = None

class PricingRuleListElementTypeDef(BaseModel):
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

class CustomLineItemListElementPaginatorTypeDef(BaseModel):
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

class CustomLineItemVersionListElementPaginatorTypeDef(BaseModel):
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

class CustomLineItemListElementTypeDef(BaseModel):
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

class CustomLineItemVersionListElementTypeDef(BaseModel):
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

class UpdateCustomLineItemOutputTypeDef(BaseModel):
    Arn: str
    BillingGroupArn: str
    Name: str
    Description: str
    ChargeDetails: ListCustomLineItemChargeDetailsTypeDef
    LastModifiedTime: int
    AssociationSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef(BaseModel):
    Arn: str
    Filters: Optional[ListCustomLineItemVersionsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomLineItemVersionsInputRequestTypeDef(BaseModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[ListCustomLineItemVersionsFilterTypeDef] = None

class UpdateCustomLineItemInputRequestTypeDef(BaseModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ChargeDetails: Optional[UpdateCustomLineItemChargeDetailsTypeDef] = None
    BillingPeriodRange: Optional[CustomLineItemBillingPeriodRangeTypeDef] = None

class UpdatePricingRuleInputRequestTypeDef(BaseModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PricingRuleTypeType] = None
    ModifierPercentage: Optional[float] = None
    Tiering: Optional[UpdateTieringInputTypeDef] = None

class UpdatePricingRuleOutputTypeDef(BaseModel):
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

class ListPricingRulesOutputTypeDef(BaseModel):
    BillingPeriod: str
    PricingRules: List[PricingRuleListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemsOutputPaginatorTypeDef(BaseModel):
    CustomLineItems: List[CustomLineItemListElementPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemVersionsOutputPaginatorTypeDef(BaseModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElementPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemsOutputTypeDef(BaseModel):
    CustomLineItems: List[CustomLineItemListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemVersionsOutputTypeDef(BaseModel):
    CustomLineItemVersions: List[CustomLineItemVersionListElementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

