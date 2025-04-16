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
from aws_resource_validator.pydantic_models.bcm_pricing_calculator_constants import *

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


class BatchDeleteBillScenarioCommitmentModificationRequest(BaseValidatorModel):
    billScenarioId: str
    ids: Sequence[str]


class BatchDeleteBillScenarioUsageModificationRequest(BaseValidatorModel):
    billScenarioId: str
    ids: Sequence[str]


class BatchDeleteWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    ids: Sequence[str]


class CostAmount(BaseValidatorModel):
    amount: Optional[float] = None
    currency: Optional[Literal["USD"]] = None


class UsageQuantityResult(BaseValidatorModel):
    amount: Optional[float] = None
    unit: Optional[str] = None


class BillIntervalOutput(BaseValidatorModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class NegateReservedInstanceAction(BaseValidatorModel):
    reservedInstancesId: Optional[str] = None


class NegateSavingsPlanAction(BaseValidatorModel):
    savingsPlanId: Optional[str] = None


class CreateBillEstimateRequest(BaseValidatorModel):
    billScenarioId: str
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateBillScenarioRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateWorkloadEstimateRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    rateType: Optional[WorkloadEstimateRateTypeType] = None
    tags: Optional[Mapping[str, str]] = None


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
    matchOptions: Optional[Sequence[str]] = None
    values: Optional[Sequence[str]] = None


class GetBillEstimateRequest(BaseValidatorModel):
    identifier: str


class GetBillScenarioRequest(BaseValidatorModel):
    identifier: str


class GetWorkloadEstimateRequest(BaseValidatorModel):
    identifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBillEstimateCommitmentsRequest(BaseValidatorModel):
    billEstimateId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillEstimateInputCommitmentModificationsRequest(BaseValidatorModel):
    billEstimateId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListUsageFilter(BaseValidatorModel):
    name: ListUsageFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillEstimateLineItemsFilter(BaseValidatorModel):
    name: ListBillEstimateLineItemsFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillEstimatesFilter(BaseValidatorModel):
    name: ListBillEstimatesFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillScenarioCommitmentModificationsRequest(BaseValidatorModel):
    billScenarioId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenariosFilter(BaseValidatorModel):
    name: ListBillScenariosFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class ListWorkloadEstimatesFilter(BaseValidatorModel):
    name: ListWorkloadEstimatesFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class UpdatePreferencesRequest(BaseValidatorModel):
    managementAccountRateTypeSelections: Optional[Sequence[RateTypeType]] = None
    memberAccountRateTypeSelections: Optional[Sequence[RateTypeType]] = None


class GetPreferencesResponse(BaseValidatorModel):
    managementAccountRateTypeSelections: List[RateTypeType]
    memberAccountRateTypeSelections: List[RateTypeType]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdatePreferencesResponse(BaseValidatorModel):
    managementAccountRateTypeSelections: List[RateTypeType]
    memberAccountRateTypeSelections: List[RateTypeType]
    ResponseMetadata: ResponseMetadata


class BatchDeleteBillScenarioCommitmentModificationError(BaseValidatorModel):
    pass


class BatchDeleteBillScenarioCommitmentModificationResponse(BaseValidatorModel):
    errors: List[BatchDeleteBillScenarioCommitmentModificationError]
    ResponseMetadata: ResponseMetadata


class BatchDeleteBillScenarioUsageModificationError(BaseValidatorModel):
    pass


class BatchDeleteBillScenarioUsageModificationResponse(BaseValidatorModel):
    errors: List[BatchDeleteBillScenarioUsageModificationError]
    ResponseMetadata: ResponseMetadata


class BatchDeleteWorkloadEstimateUsageError(BaseValidatorModel):
    pass


class BatchDeleteWorkloadEstimateUsageResponse(BaseValidatorModel):
    errors: List[BatchDeleteWorkloadEstimateUsageError]
    ResponseMetadata: ResponseMetadata


class BatchUpdateBillScenarioCommitmentModificationEntry(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioCommitmentModificationRequest(BaseValidatorModel):
    billScenarioId: str
    commitmentModifications: Sequence[BatchUpdateBillScenarioCommitmentModificationEntry]


class BatchUpdateWorkloadEstimateUsageEntry(BaseValidatorModel):
    pass


class BatchUpdateWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    usage: Sequence[BatchUpdateWorkloadEstimateUsageEntry]


class CostDifference(BaseValidatorModel):
    historicalCost: Optional[CostAmount] = None
    estimatedCost: Optional[CostAmount] = None


class Timestamp(BaseValidatorModel):
    pass


class BillInterval(BaseValidatorModel):
    start: Optional[Timestamp] = None
    end: Optional[Timestamp] = None


class FilterTimestamp(BaseValidatorModel):
    afterTimestamp: Optional[Timestamp] = None
    beforeTimestamp: Optional[Timestamp] = None


class UpdateBillEstimateRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[Timestamp] = None


class UpdateBillScenarioRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[Timestamp] = None


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
    filters: Optional[Sequence[ListUsageFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillEstimateInputUsageModificationsRequest(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListUsageFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenarioUsageModificationsRequestPaginate(BaseValidatorModel):
    billScenarioId: str
    filters: Optional[Sequence[ListUsageFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillScenarioUsageModificationsRequest(BaseValidatorModel):
    billScenarioId: str
    filters: Optional[Sequence[ListUsageFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkloadEstimateUsageRequestPaginate(BaseValidatorModel):
    workloadEstimateId: str
    filters: Optional[Sequence[ListUsageFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    filters: Optional[Sequence[ListUsageFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillEstimateLineItemsRequestPaginate(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListBillEstimateLineItemsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillEstimateLineItemsRequest(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListBillEstimateLineItemsFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadEstimateSummary(BaseValidatorModel):
    pass


class ListWorkloadEstimatesResponse(BaseValidatorModel):
    items: List[WorkloadEstimateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillEstimateCommitmentSummary(BaseValidatorModel):
    pass


class ListBillEstimateCommitmentsResponse(BaseValidatorModel):
    items: List[BillEstimateCommitmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillEstimateCostSummary(BaseValidatorModel):
    totalCostDifference: Optional[CostDifference] = None
    serviceCostDifferences: Optional[Dict[str, CostDifference]] = None


class BillEstimateLineItemSummary(BaseValidatorModel):
    pass


class ListBillEstimateLineItemsResponse(BaseValidatorModel):
    items: List[BillEstimateLineItemSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillEstimateSummary(BaseValidatorModel):
    pass


class ListBillEstimatesResponse(BaseValidatorModel):
    items: List[BillEstimateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillScenarioSummary(BaseValidatorModel):
    pass


class ListBillScenariosResponse(BaseValidatorModel):
    items: List[BillScenarioSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBillEstimatesRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[ListBillEstimatesFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillEstimatesRequest(BaseValidatorModel):
    filters: Optional[Sequence[ListBillEstimatesFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenariosRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[ListBillScenariosFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillScenariosRequest(BaseValidatorModel):
    filters: Optional[Sequence[ListBillScenariosFilter]] = None
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkloadEstimatesRequestPaginate(BaseValidatorModel):
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    filters: Optional[Sequence[ListWorkloadEstimatesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkloadEstimatesRequest(BaseValidatorModel):
    createdAtFilter: Optional[FilterTimestamp] = None
    expiresAtFilter: Optional[FilterTimestamp] = None
    filters: Optional[Sequence[ListWorkloadEstimatesFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchCreateBillScenarioCommitmentModificationEntry(BaseValidatorModel):
    key: str
    usageAccountId: str
    commitmentAction: BillScenarioCommitmentModificationAction
    group: Optional[str] = None


class ExpressionOutput(BaseValidatorModel):
    pass


class HistoricalUsageEntityOutput(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalOutput
    filterExpression: ExpressionOutput
    location: Optional[str] = None


class ExpressionPaginator(BaseValidatorModel):
    pass


class HistoricalUsageEntityPaginator(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalOutput
    filterExpression: ExpressionPaginator
    location: Optional[str] = None


class BatchUpdateBillScenarioUsageModificationEntry(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioUsageModificationRequest(BaseValidatorModel):
    billScenarioId: str
    usageModifications: Sequence[BatchUpdateBillScenarioUsageModificationEntry]


class BatchCreateBillScenarioCommitmentModificationRequest(BaseValidatorModel):
    billScenarioId: str
    commitmentModifications: Sequence[BatchCreateBillScenarioCommitmentModificationEntry]
    clientToken: Optional[str] = None


class BatchCreateBillScenarioCommitmentModificationItem(BaseValidatorModel):
    pass


class BatchCreateBillScenarioCommitmentModificationResponse(BaseValidatorModel):
    items: List[BatchCreateBillScenarioCommitmentModificationItem]
    errors: List[BatchCreateBillScenarioCommitmentModificationError]
    ResponseMetadata: ResponseMetadata


class BillEstimateInputCommitmentModificationSummary(BaseValidatorModel):
    pass


class ListBillEstimateInputCommitmentModificationsResponse(BaseValidatorModel):
    items: List[BillEstimateInputCommitmentModificationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchUpdateBillScenarioCommitmentModificationError(BaseValidatorModel):
    pass


class BillScenarioCommitmentModificationItem(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioCommitmentModificationResponse(BaseValidatorModel):
    items: List[BillScenarioCommitmentModificationItem]
    errors: List[BatchUpdateBillScenarioCommitmentModificationError]
    ResponseMetadata: ResponseMetadata


class ListBillScenarioCommitmentModificationsResponse(BaseValidatorModel):
    items: List[BillScenarioCommitmentModificationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchCreateBillScenarioUsageModificationItem(BaseValidatorModel):
    pass


class BatchCreateBillScenarioUsageModificationResponse(BaseValidatorModel):
    items: List[BatchCreateBillScenarioUsageModificationItem]
    errors: List[BatchCreateBillScenarioUsageModificationError]
    ResponseMetadata: ResponseMetadata


class BatchCreateWorkloadEstimateUsageItem(BaseValidatorModel):
    pass


class BatchCreateWorkloadEstimateUsageResponse(BaseValidatorModel):
    items: List[BatchCreateWorkloadEstimateUsageItem]
    errors: List[BatchCreateWorkloadEstimateUsageError]
    ResponseMetadata: ResponseMetadata


class BillEstimateInputUsageModificationSummary(BaseValidatorModel):
    pass


class ListBillEstimateInputUsageModificationsResponse(BaseValidatorModel):
    items: List[BillEstimateInputUsageModificationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchUpdateBillScenarioUsageModificationError(BaseValidatorModel):
    pass


class BillScenarioUsageModificationItem(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioUsageModificationResponse(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItem]
    errors: List[BatchUpdateBillScenarioUsageModificationError]
    ResponseMetadata: ResponseMetadata


class ListBillScenarioUsageModificationsResponse(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkloadEstimateUsageItem(BaseValidatorModel):
    pass


class BatchUpdateWorkloadEstimateUsageError(BaseValidatorModel):
    pass


class BatchUpdateWorkloadEstimateUsageResponse(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItem]
    errors: List[BatchUpdateWorkloadEstimateUsageError]
    ResponseMetadata: ResponseMetadata


class ListWorkloadEstimateUsageResponse(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillEstimateInputUsageModificationSummaryPaginator(BaseValidatorModel):
    pass


class ListBillEstimateInputUsageModificationsResponsePaginator(BaseValidatorModel):
    items: List[BillEstimateInputUsageModificationSummaryPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BillScenarioUsageModificationItemPaginator(BaseValidatorModel):
    pass


class ListBillScenarioUsageModificationsResponsePaginator(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItemPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkloadEstimateUsageItemPaginator(BaseValidatorModel):
    pass


class ListWorkloadEstimateUsageResponsePaginator(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItemPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExpressionUnion(BaseValidatorModel):
    pass


class BillIntervalUnion(BaseValidatorModel):
    pass


class HistoricalUsageEntity(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalUnion
    filterExpression: ExpressionUnion
    location: Optional[str] = None


class HistoricalUsageEntityUnion(BaseValidatorModel):
    pass


class BatchCreateBillScenarioUsageModificationEntry(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    key: str
    usageAccountId: str
    availabilityZone: Optional[str] = None
    group: Optional[str] = None
    amounts: Optional[Sequence[UsageAmount]] = None
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


class BatchCreateBillScenarioUsageModificationRequest(BaseValidatorModel):
    billScenarioId: str
    usageModifications: Sequence[BatchCreateBillScenarioUsageModificationEntry]
    clientToken: Optional[str] = None


class BatchCreateWorkloadEstimateUsageRequest(BaseValidatorModel):
    workloadEstimateId: str
    usage: Sequence[BatchCreateWorkloadEstimateUsageEntry]
    clientToken: Optional[str] = None


