from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddReservedInstanceAction(BaseValidatorModel):
    reservedInstancesOfferingId: Optional[str] = None
    instanceCount: Optional[int] = None


class AddSavingsPlanAction(BaseValidatorModel):
    savingsPlanOfferingId: Optional[str] = None
    commitment: Optional[float] = None


class BatchCreateBillScenarioCommitmentModificationError(BaseValidatorModel):
    key: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[BatchCreateBillScenarioCommitmentModificationErrorCodeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchCreateBillScenarioUsageModificationError(BaseValidatorModel):
    key: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[BatchCreateBillScenarioUsageModificationErrorCodeType] = None


class UsageQuantity(BaseValidatorModel):
    startHour: Optional[datetime] = None
    unit: Optional[str] = None
    amount: Optional[float] = None


class BatchCreateWorkloadEstimateUsageError(BaseValidatorModel):
    key: Optional[str] = None
    errorCode: Optional[BatchCreateWorkloadEstimateUsageCodeType] = None
    errorMessage: Optional[str] = None


class WorkloadEstimateUsageQuantity(BaseValidatorModel):
    unit: Optional[str] = None
    amount: Optional[float] = None


class BatchDeleteBillScenarioCommitmentModificationError(BaseValidatorModel):
    id: Optional[str] = None
    errorCode: Optional[BatchDeleteBillScenarioCommitmentModificationErrorCodeType] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'batch_delete_bill_scenario_commitment_modification' function.
class BatchDeleteBillScenarioCommitmentModificationRequest(BaseValidatorModel):
    billScenarioId: str
    ids: List[str]


class BatchDeleteBillScenarioUsageModificationError(BaseValidatorModel):
    id: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[BatchDeleteBillScenarioUsageModificationErrorCodeType] = None


# This class is the input for the 'batch_delete_bill_scenario_usage_modification' function.
class BatchDeleteBillScenarioUsageModificationRequest(BaseValidatorModel):
    billScenarioId: str
    ids: List[str]


class BatchDeleteWorkloadEstimateUsageError(BaseValidatorModel):
    id: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[WorkloadEstimateUpdateUsageErrorCodeType] = None


# This class is the input for the 'batch_delete_workload_estimate_usage' function.
class BatchDeleteWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    ids: List[str]


class BatchUpdateBillScenarioCommitmentModificationEntry(BaseValidatorModel):
    id: str
    group: Optional[str] = None


class BatchUpdateBillScenarioCommitmentModificationError(BaseValidatorModel):
    id: Optional[str] = None
    errorCode: Optional[BatchUpdateBillScenarioCommitmentModificationErrorCodeType] = None
    errorMessage: Optional[str] = None


class BatchUpdateBillScenarioUsageModificationError(BaseValidatorModel):
    id: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[BatchUpdateBillScenarioUsageModificationErrorCodeType] = None


class BatchUpdateWorkloadEstimateUsageEntry(BaseValidatorModel):
    id: str
    group: Optional[str] = None
    amount: Optional[float] = None


class BatchUpdateWorkloadEstimateUsageError(BaseValidatorModel):
    id: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[WorkloadEstimateUpdateUsageErrorCodeType] = None


class CostAmount(BaseValidatorModel):
    amount: Optional[float] = None
    currency: Optional[Literal['USD']] = None


class UsageQuantityResult(BaseValidatorModel):
    amount: Optional[float] = None
    unit: Optional[str] = None


class BillIntervalOutput(BaseValidatorModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

Timestamp = Union[datetime, str]


class NegateReservedInstanceAction(BaseValidatorModel):
    reservedInstancesId: Optional[str] = None


class NegateSavingsPlanAction(BaseValidatorModel):
    savingsPlanId: Optional[str] = None


# This class is the input for the 'create_bill_estimate' function.
class CreateBillEstimateRequest(BaseValidatorModel):
    billScenarioId: str
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_bill_scenario' function.
class CreateBillScenarioRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_workload_estimate' function.
class CreateWorkloadEstimateRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    rateType: Optional[WorkloadEstimateRateTypeType] = None
    tags: Optional[Dict[str, str]] = None


class DeleteBillEstimateRequest(BaseValidatorModel):
    identifier: str


class DeleteBillScenarioRequest(BaseValidatorModel):
    identifier: str


class DeleteWorkloadEstimateRequest(BaseValidatorModel):
    identifier: str


class ExpressionFilterOutput(BaseValidatorModel):
    key: Optional[str] = None
    matchOptions: Optional[List[str]] = None
    values: Optional[List[str]] = None


class ExpressionFilter(BaseValidatorModel):
    key: Optional[str] = None
    matchOptions: Optional[List[str]] = None
    values: Optional[List[str]] = None


# This class is the input for the 'get_bill_estimate' function.
class GetBillEstimateRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'get_bill_scenario' function.
class GetBillScenarioRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'get_workload_estimate' function.
class GetWorkloadEstimateRequest(BaseValidatorModel):
    identifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_bill_estimate_commitments' function.
class ListBillEstimateCommitmentsRequest(BaseValidatorModel):
    billEstimateId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_bill_estimate_input_commitment_modifications' function.
class ListBillEstimateInputCommitmentModificationsRequest(BaseValidatorModel):
    billEstimateId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListUsageFilter(BaseValidatorModel):
    name: ListUsageFilterNameType
    values: List[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillEstimateLineItemsFilter(BaseValidatorModel):
    name: ListBillEstimateLineItemsFilterNameType
    values: List[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillEstimatesFilter(BaseValidatorModel):
    name: ListBillEstimatesFilterNameType
    values: List[str]
    matchOption: Optional[MatchOptionType] = None


# This class is the input for the 'list_bill_scenario_commitment_modifications' function.
class ListBillScenarioCommitmentModificationsRequest(BaseValidatorModel):
    billScenarioId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenariosFilter(BaseValidatorModel):
    name: ListBillScenariosFilterNameType
    values: List[str]
    matchOption: Optional[MatchOptionType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class ListWorkloadEstimatesFilter(BaseValidatorModel):
    name: ListWorkloadEstimatesFilterNameType
    values: List[str]
    matchOption: Optional[MatchOptionType] = None


class WorkloadEstimateSummary(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    createdAt: Optional[datetime] = None
    expiresAt: Optional[datetime] = None
    rateType: Optional[WorkloadEstimateRateTypeType] = None
    rateTimestamp: Optional[datetime] = None
    status: Optional[WorkloadEstimateStatusType] = None
    totalCost: Optional[float] = None
    costCurrency: Optional[Literal['USD']] = None
    failureMessage: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


# This class is the input for the 'update_preferences' function.
class UpdatePreferencesRequest(BaseValidatorModel):
    managementAccountRateTypeSelections: Optional[List[RateTypeType]] = None
    memberAccountRateTypeSelections: Optional[List[RateTypeType]] = None


# This class is the output for the 'create_workload_estimate' function.
class CreateWorkloadEstimateResponse(BaseValidatorModel):
    id: str
    name: str
    createdAt: datetime
    expiresAt: datetime
    rateType: WorkloadEstimateRateTypeType
    rateTimestamp: datetime
    status: WorkloadEstimateStatusType
    totalCost: float
    costCurrency: Literal['USD']
    failureMessage: str
    ResponseMetadata: ResponseMetadata


class GetPreferencesResponse(BaseValidatorModel):
    managementAccountRateTypeSelections: List[RateTypeType]
    memberAccountRateTypeSelections: List[RateTypeType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_workload_estimate' function.
class GetWorkloadEstimateResponse(BaseValidatorModel):
    id: str
    name: str
    createdAt: datetime
    expiresAt: datetime
    rateType: WorkloadEstimateRateTypeType
    rateTimestamp: datetime
    status: WorkloadEstimateStatusType
    totalCost: float
    costCurrency: Literal['USD']
    failureMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_preferences' function.
class UpdatePreferencesResponse(BaseValidatorModel):
    managementAccountRateTypeSelections: List[RateTypeType]
    memberAccountRateTypeSelections: List[RateTypeType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_workload_estimate' function.
class UpdateWorkloadEstimateResponse(BaseValidatorModel):
    id: str
    name: str
    createdAt: datetime
    expiresAt: datetime
    rateType: WorkloadEstimateRateTypeType
    rateTimestamp: datetime
    status: WorkloadEstimateStatusType
    totalCost: float
    costCurrency: Literal['USD']
    failureMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_bill_scenario_commitment_modification' function.
class BatchDeleteBillScenarioCommitmentModificationResponse(BaseValidatorModel):
    errors: List[BatchDeleteBillScenarioCommitmentModificationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_bill_scenario_usage_modification' function.
class BatchDeleteBillScenarioUsageModificationResponse(BaseValidatorModel):
    errors: List[BatchDeleteBillScenarioUsageModificationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_workload_estimate_usage' function.
class BatchDeleteWorkloadEstimateUsageResponse(BaseValidatorModel):
    errors: List[BatchDeleteWorkloadEstimateUsageError]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_update_bill_scenario_commitment_modification' function.
class BatchUpdateBillScenarioCommitmentModificationRequest(BaseValidatorModel):
    billScenarioId: str
    commitmentModifications: List[BatchUpdateBillScenarioCommitmentModificationEntry]


# This class is the input for the 'batch_update_workload_estimate_usage' function.
class BatchUpdateWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    usage: List[BatchUpdateWorkloadEstimateUsageEntry]


class BillEstimateCommitmentSummary(BaseValidatorModel):
    id: Optional[str] = None
    purchaseAgreementType: Optional[PurchaseAgreementTypeType] = None
    offeringId: Optional[str] = None
    usageAccountId: Optional[str] = None
    region: Optional[str] = None
    termLength: Optional[str] = None
    paymentOption: Optional[str] = None
    upfrontPayment: Optional[CostAmount] = None
    monthlyPayment: Optional[CostAmount] = None


class CostDifference(BaseValidatorModel):
    historicalCost: Optional[CostAmount] = None
    estimatedCost: Optional[CostAmount] = None


class BillEstimateLineItemSummary(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    availabilityZone: Optional[str] = None
    id: Optional[str] = None
    lineItemId: Optional[str] = None
    lineItemType: Optional[str] = None
    payerAccountId: Optional[str] = None
    usageAccountId: Optional[str] = None
    estimatedUsageQuantity: Optional[UsageQuantityResult] = None
    estimatedCost: Optional[CostAmount] = None
    historicalUsageQuantity: Optional[UsageQuantityResult] = None
    historicalCost: Optional[CostAmount] = None
    savingsPlanArns: Optional[List[str]] = None


class BillEstimateSummary(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    status: Optional[BillEstimateStatusType] = None
    billInterval: Optional[BillIntervalOutput] = None
    createdAt: Optional[datetime] = None
    expiresAt: Optional[datetime] = None


class BillScenarioSummary(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    billInterval: Optional[BillIntervalOutput] = None
    status: Optional[BillScenarioStatusType] = None
    createdAt: Optional[datetime] = None
    expiresAt: Optional[datetime] = None
    failureMessage: Optional[str] = None


# This class is the output for the 'create_bill_scenario' function.
class CreateBillScenarioResponse(BaseValidatorModel):
    id: str
    name: str
    billInterval: BillIntervalOutput
    status: BillScenarioStatusType
    createdAt: datetime
    expiresAt: datetime
    failureMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bill_scenario' function.
class GetBillScenarioResponse(BaseValidatorModel):
    id: str
    name: str
    billInterval: BillIntervalOutput
    status: BillScenarioStatusType
    createdAt: datetime
    expiresAt: datetime
    failureMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bill_scenario' function.
class UpdateBillScenarioResponse(BaseValidatorModel):
    id: str
    name: str
    billInterval: BillIntervalOutput
    status: BillScenarioStatusType
    createdAt: datetime
    expiresAt: datetime
    failureMessage: str
    ResponseMetadata: ResponseMetadata


class BillInterval(BaseValidatorModel):
    start: Optional[Timestamp] = None
    end: Optional[Timestamp] = None


class FilterTimestamp(BaseValidatorModel):
    afterTimestamp: Optional[Timestamp] = None
    beforeTimestamp: Optional[Timestamp] = None


# This class is the input for the 'update_bill_estimate' function.
class UpdateBillEstimateRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[Timestamp] = None


# This class is the input for the 'update_bill_scenario' function.
class UpdateBillScenarioRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[Timestamp] = None


# This class is the input for the 'update_workload_estimate' function.
class UpdateWorkloadEstimateRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[Timestamp] = None


class UsageAmount(BaseValidatorModel):
    startHour: Timestamp
    amount: float


class BillScenarioCommitmentModificationAction(BaseValidatorModel):
    addReservedInstanceAction: Optional[AddReservedInstanceAction] = None
    addSavingsPlanAction: Optional[AddSavingsPlanAction] = None
    negateReservedInstanceAction: Optional[NegateReservedInstanceAction] = None
    negateSavingsPlanAction: Optional[NegateSavingsPlanAction] = None


class ExpressionOutput(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    or_: Optional[List[Dict[str, Any]]] = None
    not_: Optional[Dict[str, Any]] = None
    costCategories: Optional[ExpressionFilterOutput] = None
    dimensions: Optional[ExpressionFilterOutput] = None
    tags: Optional[ExpressionFilterOutput] = None


class ExpressionPaginator(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    or_: Optional[List[Dict[str, Any]]] = None
    not_: Optional[Dict[str, Any]] = None
    costCategories: Optional[ExpressionFilterOutput] = None
    dimensions: Optional[ExpressionFilterOutput] = None
    tags: Optional[ExpressionFilterOutput] = None

ExpressionFilterUnion = Union[ExpressionFilter, ExpressionFilterOutput]


class ListBillEstimateCommitmentsRequestPaginate(BaseValidatorModel):
    billEstimateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillEstimateInputCommitmentModificationsRequestPaginate(BaseValidatorModel):
    billEstimateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillScenarioCommitmentModificationsRequestPaginate(BaseValidatorModel):
    billScenarioId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillEstimateInputUsageModificationsRequestPaginate(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[List[ListUsageFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_bill_estimate_input_usage_modifications' function.
class ListBillEstimateInputUsageModificationsRequest(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[List[ListUsageFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenarioUsageModificationsRequestPaginate(BaseValidatorModel):
    billScenarioId: str
    filters: Optional[List[ListUsageFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_bill_scenario_usage_modifications' function.
class ListBillScenarioUsageModificationsRequest(BaseValidatorModel):
    billScenarioId: str
    filters: Optional[List[ListUsageFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkloadEstimateUsageRequestPaginate(BaseValidatorModel):
    workloadEstimateId: str
    filters: Optional[List[ListUsageFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_workload_estimate_usage' function.
class ListWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    filters: Optional[List[ListUsageFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillEstimateLineItemsRequestPaginate(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[List[ListBillEstimateLineItemsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_bill_estimate_line_items' function.
class ListBillEstimateLineItemsRequest(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[List[ListBillEstimateLineItemsFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'list_workload_estimates' function.
class ListWorkloadEstimatesResponse(BaseValidatorModel):
    items: List[WorkloadEstimateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_bill_estimate_commitments' function.
class ListBillEstimateCommitmentsResponse(BaseValidatorModel):
    items: List[BillEstimateCommitmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillEstimateCostSummary(BaseValidatorModel):
    totalCostDifference: Optional[CostDifference] = None
    serviceCostDifferences: Optional[Dict[str, CostDifference]] = None


# This class is the output for the 'list_bill_estimate_line_items' function.
class ListBillEstimateLineItemsResponse(BaseValidatorModel):
    items: List[BillEstimateLineItemSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_bill_estimates' function.
class ListBillEstimatesResponse(BaseValidatorModel):
    items: List[BillEstimateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_bill_scenarios' function.
class ListBillScenariosResponse(BaseValidatorModel):
    items: List[BillScenarioSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

BillIntervalUnion = Union[BillInterval, BillIntervalOutput]


class ListBillEstimatesRequestPaginate(BaseValidatorModel):
    filters: Optional[List[ListBillEstimatesFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_bill_estimates' function.
class ListBillEstimatesRequest(BaseValidatorModel):
    filters: Optional[List[ListBillEstimatesFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenariosRequestPaginate(BaseValidatorModel):
    filters: Optional[List[ListBillScenariosFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_bill_scenarios' function.
class ListBillScenariosRequest(BaseValidatorModel):
    filters: Optional[List[ListBillScenariosFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkloadEstimatesRequestPaginate(BaseValidatorModel):
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    filters: Optional[List[ListWorkloadEstimatesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_workload_estimates' function.
class ListWorkloadEstimatesRequest(BaseValidatorModel):
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    filters: Optional[List[ListWorkloadEstimatesFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchUpdateBillScenarioUsageModificationEntry(BaseValidatorModel):
    id: str
    group: Optional[str] = None
    amounts: Optional[List[UsageAmount]] = None


class BatchCreateBillScenarioCommitmentModificationEntry(BaseValidatorModel):
    key: str
    usageAccountId: str
    commitmentAction: BillScenarioCommitmentModificationAction
    group: Optional[str] = None


class BatchCreateBillScenarioCommitmentModificationItem(BaseValidatorModel):
    key: Optional[str] = None
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    commitmentAction: Optional[BillScenarioCommitmentModificationAction] = None


class BillEstimateInputCommitmentModificationSummary(BaseValidatorModel):
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    commitmentAction: Optional[BillScenarioCommitmentModificationAction] = None


class BillScenarioCommitmentModificationItem(BaseValidatorModel):
    id: Optional[str] = None
    usageAccountId: Optional[str] = None
    group: Optional[str] = None
    commitmentAction: Optional[BillScenarioCommitmentModificationAction] = None


class HistoricalUsageEntityOutput(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalOutput
    filterExpression: ExpressionOutput
    location: Optional[str] = None


class HistoricalUsageEntityPaginator(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalOutput
    filterExpression: ExpressionPaginator
    location: Optional[str] = None


class Expression(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    or_: Optional[List[Dict[str, Any]]] = None
    not_: Optional[Dict[str, Any]] = None
    costCategories: Optional[ExpressionFilterUnion] = None
    dimensions: Optional[ExpressionFilterUnion] = None
    tags: Optional[ExpressionFilterUnion] = None


# This class is the output for the 'create_bill_estimate' function.
class CreateBillEstimateResponse(BaseValidatorModel):
    id: str
    name: str
    status: BillEstimateStatusType
    failureMessage: str
    billInterval: BillIntervalOutput
    costSummary: BillEstimateCostSummary
    createdAt: datetime
    expiresAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bill_estimate' function.
class GetBillEstimateResponse(BaseValidatorModel):
    id: str
    name: str
    status: BillEstimateStatusType
    failureMessage: str
    billInterval: BillIntervalOutput
    costSummary: BillEstimateCostSummary
    createdAt: datetime
    expiresAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bill_estimate' function.
class UpdateBillEstimateResponse(BaseValidatorModel):
    id: str
    name: str
    status: BillEstimateStatusType
    failureMessage: str
    billInterval: BillIntervalOutput
    costSummary: BillEstimateCostSummary
    createdAt: datetime
    expiresAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_update_bill_scenario_usage_modification' function.
class BatchUpdateBillScenarioUsageModificationRequest(BaseValidatorModel):
    billScenarioId: str
    usageModifications: List[BatchUpdateBillScenarioUsageModificationEntry]


# This class is the input for the 'batch_create_bill_scenario_commitment_modification' function.
class BatchCreateBillScenarioCommitmentModificationRequest(BaseValidatorModel):
    billScenarioId: str
    commitmentModifications: List[BatchCreateBillScenarioCommitmentModificationEntry]
    clientToken: Optional[str] = None


# This class is the output for the 'batch_create_bill_scenario_commitment_modification' function.
class BatchCreateBillScenarioCommitmentModificationResponse(BaseValidatorModel):
    items: List[BatchCreateBillScenarioCommitmentModificationItem]
    errors: List[BatchCreateBillScenarioCommitmentModificationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bill_estimate_input_commitment_modifications' function.
class ListBillEstimateInputCommitmentModificationsResponse(BaseValidatorModel):
    items: List[BillEstimateInputCommitmentModificationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_update_bill_scenario_commitment_modification' function.
class BatchUpdateBillScenarioCommitmentModificationResponse(BaseValidatorModel):
    items: List[BillScenarioCommitmentModificationItem]
    errors: List[BatchUpdateBillScenarioCommitmentModificationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bill_scenario_commitment_modifications' function.
class ListBillScenarioCommitmentModificationsResponse(BaseValidatorModel):
    items: List[BillScenarioCommitmentModificationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchCreateBillScenarioUsageModificationItem(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    availabilityZone: Optional[str] = None
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    quantities: Optional[List[UsageQuantity]] = None
    historicalUsage: Optional[HistoricalUsageEntityOutput] = None
    key: Optional[str] = None


class BatchCreateWorkloadEstimateUsageItem(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    id: Optional[str] = None
    usageAccountId: Optional[str] = None
    group: Optional[str] = None
    quantity: Optional[WorkloadEstimateUsageQuantity] = None
    cost: Optional[float] = None
    currency: Optional[Literal['USD']] = None
    status: Optional[WorkloadEstimateCostStatusType] = None
    historicalUsage: Optional[HistoricalUsageEntityOutput] = None
    key: Optional[str] = None


class BillEstimateInputUsageModificationSummary(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    availabilityZone: Optional[str] = None
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    quantities: Optional[List[UsageQuantity]] = None
    historicalUsage: Optional[HistoricalUsageEntityOutput] = None


class BillScenarioUsageModificationItem(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    availabilityZone: Optional[str] = None
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    quantities: Optional[List[UsageQuantity]] = None
    historicalUsage: Optional[HistoricalUsageEntityOutput] = None


class WorkloadEstimateUsageItem(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    id: Optional[str] = None
    usageAccountId: Optional[str] = None
    group: Optional[str] = None
    quantity: Optional[WorkloadEstimateUsageQuantity] = None
    cost: Optional[float] = None
    currency: Optional[Literal['USD']] = None
    status: Optional[WorkloadEstimateCostStatusType] = None
    historicalUsage: Optional[HistoricalUsageEntityOutput] = None


class BillEstimateInputUsageModificationSummaryPaginator(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    availabilityZone: Optional[str] = None
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    quantities: Optional[List[UsageQuantity]] = None
    historicalUsage: Optional[HistoricalUsageEntityPaginator] = None


class BillScenarioUsageModificationItemPaginator(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    availabilityZone: Optional[str] = None
    id: Optional[str] = None
    group: Optional[str] = None
    usageAccountId: Optional[str] = None
    quantities: Optional[List[UsageQuantity]] = None
    historicalUsage: Optional[HistoricalUsageEntityPaginator] = None


class WorkloadEstimateUsageItemPaginator(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    location: Optional[str] = None
    id: Optional[str] = None
    usageAccountId: Optional[str] = None
    group: Optional[str] = None
    quantity: Optional[WorkloadEstimateUsageQuantity] = None
    cost: Optional[float] = None
    currency: Optional[Literal['USD']] = None
    status: Optional[WorkloadEstimateCostStatusType] = None
    historicalUsage: Optional[HistoricalUsageEntityPaginator] = None

ExpressionUnion = Union[Expression, ExpressionOutput]


# This class is the output for the 'batch_create_bill_scenario_usage_modification' function.
class BatchCreateBillScenarioUsageModificationResponse(BaseValidatorModel):
    items: List[BatchCreateBillScenarioUsageModificationItem]
    errors: List[BatchCreateBillScenarioUsageModificationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_create_workload_estimate_usage' function.
class BatchCreateWorkloadEstimateUsageResponse(BaseValidatorModel):
    items: List[BatchCreateWorkloadEstimateUsageItem]
    errors: List[BatchCreateWorkloadEstimateUsageError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bill_estimate_input_usage_modifications' function.
class ListBillEstimateInputUsageModificationsResponse(BaseValidatorModel):
    items: List[BillEstimateInputUsageModificationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_update_bill_scenario_usage_modification' function.
class BatchUpdateBillScenarioUsageModificationResponse(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItem]
    errors: List[BatchUpdateBillScenarioUsageModificationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bill_scenario_usage_modifications' function.
class ListBillScenarioUsageModificationsResponse(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_update_workload_estimate_usage' function.
class BatchUpdateWorkloadEstimateUsageResponse(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItem]
    errors: List[BatchUpdateWorkloadEstimateUsageError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_workload_estimate_usage' function.
class ListWorkloadEstimateUsageResponse(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBillEstimateInputUsageModificationsResponsePaginator(BaseValidatorModel):
    items: List[BillEstimateInputUsageModificationSummaryPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBillScenarioUsageModificationsResponsePaginator(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItemPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkloadEstimateUsageResponsePaginator(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItemPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class HistoricalUsageEntity(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalUnion
    filterExpression: ExpressionUnion
    location: Optional[str] = None

HistoricalUsageEntityUnion = Union[HistoricalUsageEntity, HistoricalUsageEntityOutput]


class BatchCreateBillScenarioUsageModificationEntry(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    key: str
    usageAccountId: str
    availabilityZone: Optional[str] = None
    group: Optional[str] = None
    amounts: Optional[List[UsageAmount]] = None
    historicalUsage: Optional[HistoricalUsageEntityUnion] = None


class BatchCreateWorkloadEstimateUsageEntry(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    key: str
    usageAccountId: str
    amount: float
    group: Optional[str] = None
    historicalUsage: Optional[HistoricalUsageEntityUnion] = None


# This class is the input for the 'batch_create_bill_scenario_usage_modification' function.
class BatchCreateBillScenarioUsageModificationRequest(BaseValidatorModel):
    billScenarioId: str
    usageModifications: List[BatchCreateBillScenarioUsageModificationEntry]
    clientToken: Optional[str] = None


# This class is the input for the 'batch_create_workload_estimate_usage' function.
class BatchCreateWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    usage: List[BatchCreateWorkloadEstimateUsageEntry]
    clientToken: Optional[str] = None