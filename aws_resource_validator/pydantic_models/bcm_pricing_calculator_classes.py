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

class AddReservedInstanceActionTypeDef(BaseValidatorModel):
    reservedInstancesOfferingId: Optional[str] = None
    instanceCount: Optional[int] = None


class AddSavingsPlanActionTypeDef(BaseValidatorModel):
    savingsPlanOfferingId: Optional[str] = None
    commitment: Optional[float] = None


class BatchCreateBillScenarioCommitmentModificationErrorTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[BatchCreateBillScenarioCommitmentModificationErrorCodeType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchCreateBillScenarioUsageModificationErrorTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[BatchCreateBillScenarioUsageModificationErrorCodeType] = None


class UsageQuantityTypeDef(BaseValidatorModel):
    startHour: Optional[datetime] = None
    unit: Optional[str] = None
    amount: Optional[float] = None


class BatchCreateWorkloadEstimateUsageErrorTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    errorCode: Optional[BatchCreateWorkloadEstimateUsageCodeType] = None
    errorMessage: Optional[str] = None


class WorkloadEstimateUsageQuantityTypeDef(BaseValidatorModel):
    unit: Optional[str] = None
    amount: Optional[float] = None


class BatchDeleteBillScenarioCommitmentModificationRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    ids: Sequence[str]


class BatchDeleteBillScenarioUsageModificationRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    ids: Sequence[str]


class BatchDeleteWorkloadEstimateUsageRequestTypeDef(BaseValidatorModel):
    workloadEstimateId: str
    ids: Sequence[str]


class CostAmountTypeDef(BaseValidatorModel):
    amount: Optional[float] = None
    currency: Optional[Literal["USD"]] = None


class UsageQuantityResultTypeDef(BaseValidatorModel):
    amount: Optional[float] = None
    unit: Optional[str] = None


class BillIntervalOutputTypeDef(BaseValidatorModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class NegateReservedInstanceActionTypeDef(BaseValidatorModel):
    reservedInstancesId: Optional[str] = None


class NegateSavingsPlanActionTypeDef(BaseValidatorModel):
    savingsPlanId: Optional[str] = None


class CreateBillEstimateRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateBillScenarioRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateWorkloadEstimateRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    rateType: Optional[WorkloadEstimateRateTypeType] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteBillEstimateRequestTypeDef(BaseValidatorModel):
    identifier: str


class DeleteBillScenarioRequestTypeDef(BaseValidatorModel):
    identifier: str


class DeleteWorkloadEstimateRequestTypeDef(BaseValidatorModel):
    identifier: str


class ExpressionFilterOutputTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    matchOptions: Optional[List[str]] = None
    values: Optional[List[str]] = None


class ExpressionFilterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    matchOptions: Optional[Sequence[str]] = None
    values: Optional[Sequence[str]] = None


class GetBillEstimateRequestTypeDef(BaseValidatorModel):
    identifier: str


class GetBillScenarioRequestTypeDef(BaseValidatorModel):
    identifier: str


class GetWorkloadEstimateRequestTypeDef(BaseValidatorModel):
    identifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBillEstimateCommitmentsRequestTypeDef(BaseValidatorModel):
    billEstimateId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillEstimateInputCommitmentModificationsRequestTypeDef(BaseValidatorModel):
    billEstimateId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListUsageFilterTypeDef(BaseValidatorModel):
    name: ListUsageFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillEstimateLineItemsFilterTypeDef(BaseValidatorModel):
    name: ListBillEstimateLineItemsFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillEstimatesFilterTypeDef(BaseValidatorModel):
    name: ListBillEstimatesFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListBillScenarioCommitmentModificationsRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenariosFilterTypeDef(BaseValidatorModel):
    name: ListBillScenariosFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    arn: str


class ListWorkloadEstimatesFilterTypeDef(BaseValidatorModel):
    name: ListWorkloadEstimatesFilterNameType
    values: Sequence[str]
    matchOption: Optional[MatchOptionType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class UpdatePreferencesRequestTypeDef(BaseValidatorModel):
    managementAccountRateTypeSelections: Optional[Sequence[RateTypeType]] = None
    memberAccountRateTypeSelections: Optional[Sequence[RateTypeType]] = None


class GetPreferencesResponseTypeDef(BaseValidatorModel):
    managementAccountRateTypeSelections: List[RateTypeType]
    memberAccountRateTypeSelections: List[RateTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePreferencesResponseTypeDef(BaseValidatorModel):
    managementAccountRateTypeSelections: List[RateTypeType]
    memberAccountRateTypeSelections: List[RateTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteBillScenarioCommitmentModificationErrorTypeDef(BaseValidatorModel):
    pass


class BatchDeleteBillScenarioCommitmentModificationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteBillScenarioCommitmentModificationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteBillScenarioUsageModificationErrorTypeDef(BaseValidatorModel):
    pass


class BatchDeleteBillScenarioUsageModificationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteBillScenarioUsageModificationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteWorkloadEstimateUsageErrorTypeDef(BaseValidatorModel):
    pass


class BatchDeleteWorkloadEstimateUsageResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteWorkloadEstimateUsageErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateBillScenarioCommitmentModificationEntryTypeDef(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioCommitmentModificationRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    commitmentModifications: Sequence[BatchUpdateBillScenarioCommitmentModificationEntryTypeDef]


class BatchUpdateWorkloadEstimateUsageEntryTypeDef(BaseValidatorModel):
    pass


class BatchUpdateWorkloadEstimateUsageRequestTypeDef(BaseValidatorModel):
    workloadEstimateId: str
    usage: Sequence[BatchUpdateWorkloadEstimateUsageEntryTypeDef]


class CostDifferenceTypeDef(BaseValidatorModel):
    historicalCost: Optional[CostAmountTypeDef] = None
    estimatedCost: Optional[CostAmountTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class BillIntervalTypeDef(BaseValidatorModel):
    start: Optional[TimestampTypeDef] = None
    end: Optional[TimestampTypeDef] = None


class FilterTimestampTypeDef(BaseValidatorModel):
    afterTimestamp: Optional[TimestampTypeDef] = None
    beforeTimestamp: Optional[TimestampTypeDef] = None


class UpdateBillEstimateRequestTypeDef(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[TimestampTypeDef] = None


class UpdateBillScenarioRequestTypeDef(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[TimestampTypeDef] = None


class UpdateWorkloadEstimateRequestTypeDef(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    expiresAt: Optional[TimestampTypeDef] = None


class UsageAmountTypeDef(BaseValidatorModel):
    startHour: TimestampTypeDef
    amount: float


class BillScenarioCommitmentModificationActionTypeDef(BaseValidatorModel):
    addReservedInstanceAction: Optional[AddReservedInstanceActionTypeDef] = None
    addSavingsPlanAction: Optional[AddSavingsPlanActionTypeDef] = None
    negateReservedInstanceAction: Optional[NegateReservedInstanceActionTypeDef] = None
    negateSavingsPlanAction: Optional[NegateSavingsPlanActionTypeDef] = None


class ListBillEstimateCommitmentsRequestPaginateTypeDef(BaseValidatorModel):
    billEstimateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillEstimateInputCommitmentModificationsRequestPaginateTypeDef(BaseValidatorModel):
    billEstimateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillScenarioCommitmentModificationsRequestPaginateTypeDef(BaseValidatorModel):
    billScenarioId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillEstimateInputUsageModificationsRequestPaginateTypeDef(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListUsageFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillEstimateInputUsageModificationsRequestTypeDef(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListUsageFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenarioUsageModificationsRequestPaginateTypeDef(BaseValidatorModel):
    billScenarioId: str
    filters: Optional[Sequence[ListUsageFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillScenarioUsageModificationsRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    filters: Optional[Sequence[ListUsageFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkloadEstimateUsageRequestPaginateTypeDef(BaseValidatorModel):
    workloadEstimateId: str
    filters: Optional[Sequence[ListUsageFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkloadEstimateUsageRequestTypeDef(BaseValidatorModel):
    workloadEstimateId: str
    filters: Optional[Sequence[ListUsageFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillEstimateLineItemsRequestPaginateTypeDef(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListBillEstimateLineItemsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillEstimateLineItemsRequestTypeDef(BaseValidatorModel):
    billEstimateId: str
    filters: Optional[Sequence[ListBillEstimateLineItemsFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadEstimateSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkloadEstimatesResponseTypeDef(BaseValidatorModel):
    items: List[WorkloadEstimateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BillEstimateCommitmentSummaryTypeDef(BaseValidatorModel):
    pass


class ListBillEstimateCommitmentsResponseTypeDef(BaseValidatorModel):
    items: List[BillEstimateCommitmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BillEstimateCostSummaryTypeDef(BaseValidatorModel):
    totalCostDifference: Optional[CostDifferenceTypeDef] = None
    serviceCostDifferences: Optional[Dict[str, CostDifferenceTypeDef]] = None


class BillEstimateLineItemSummaryTypeDef(BaseValidatorModel):
    pass


class ListBillEstimateLineItemsResponseTypeDef(BaseValidatorModel):
    items: List[BillEstimateLineItemSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BillEstimateSummaryTypeDef(BaseValidatorModel):
    pass


class ListBillEstimatesResponseTypeDef(BaseValidatorModel):
    items: List[BillEstimateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BillScenarioSummaryTypeDef(BaseValidatorModel):
    pass


class ListBillScenariosResponseTypeDef(BaseValidatorModel):
    items: List[BillScenarioSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBillEstimatesRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListBillEstimatesFilterTypeDef]] = None
    createdAtFilter: Optional[FilterTimestampTypeDef] = None
    expiresAtFilter: Optional[FilterTimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillEstimatesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListBillEstimatesFilterTypeDef]] = None
    createdAtFilter: Optional[FilterTimestampTypeDef] = None
    expiresAtFilter: Optional[FilterTimestampTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBillScenariosRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListBillScenariosFilterTypeDef]] = None
    createdAtFilter: Optional[FilterTimestampTypeDef] = None
    expiresAtFilter: Optional[FilterTimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillScenariosRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListBillScenariosFilterTypeDef]] = None
    createdAtFilter: Optional[FilterTimestampTypeDef] = None
    expiresAtFilter: Optional[FilterTimestampTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkloadEstimatesRequestPaginateTypeDef(BaseValidatorModel):
    createdAtFilter: Optional[FilterTimestampTypeDef] = None
    expiresAtFilter: Optional[FilterTimestampTypeDef] = None
    filters: Optional[Sequence[ListWorkloadEstimatesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkloadEstimatesRequestTypeDef(BaseValidatorModel):
    createdAtFilter: Optional[FilterTimestampTypeDef] = None
    expiresAtFilter: Optional[FilterTimestampTypeDef] = None
    filters: Optional[Sequence[ListWorkloadEstimatesFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchCreateBillScenarioCommitmentModificationEntryTypeDef(BaseValidatorModel):
    key: str
    usageAccountId: str
    commitmentAction: BillScenarioCommitmentModificationActionTypeDef
    group: Optional[str] = None


class ExpressionOutputTypeDef(BaseValidatorModel):
    pass


class HistoricalUsageEntityOutputTypeDef(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalOutputTypeDef
    filterExpression: ExpressionOutputTypeDef
    location: Optional[str] = None


class ExpressionPaginatorTypeDef(BaseValidatorModel):
    pass


class HistoricalUsageEntityPaginatorTypeDef(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalOutputTypeDef
    filterExpression: ExpressionPaginatorTypeDef
    location: Optional[str] = None


class BatchUpdateBillScenarioUsageModificationEntryTypeDef(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioUsageModificationRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    usageModifications: Sequence[BatchUpdateBillScenarioUsageModificationEntryTypeDef]


class BatchCreateBillScenarioCommitmentModificationRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    commitmentModifications: Sequence[BatchCreateBillScenarioCommitmentModificationEntryTypeDef]
    clientToken: Optional[str] = None


class BatchCreateBillScenarioCommitmentModificationItemTypeDef(BaseValidatorModel):
    pass


class BatchCreateBillScenarioCommitmentModificationResponseTypeDef(BaseValidatorModel):
    items: List[BatchCreateBillScenarioCommitmentModificationItemTypeDef]
    errors: List[BatchCreateBillScenarioCommitmentModificationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BillEstimateInputCommitmentModificationSummaryTypeDef(BaseValidatorModel):
    pass


class ListBillEstimateInputCommitmentModificationsResponseTypeDef(BaseValidatorModel):
    items: List[BillEstimateInputCommitmentModificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchUpdateBillScenarioCommitmentModificationErrorTypeDef(BaseValidatorModel):
    pass


class BillScenarioCommitmentModificationItemTypeDef(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioCommitmentModificationResponseTypeDef(BaseValidatorModel):
    items: List[BillScenarioCommitmentModificationItemTypeDef]
    errors: List[BatchUpdateBillScenarioCommitmentModificationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListBillScenarioCommitmentModificationsResponseTypeDef(BaseValidatorModel):
    items: List[BillScenarioCommitmentModificationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchCreateBillScenarioUsageModificationItemTypeDef(BaseValidatorModel):
    pass


class BatchCreateBillScenarioUsageModificationResponseTypeDef(BaseValidatorModel):
    items: List[BatchCreateBillScenarioUsageModificationItemTypeDef]
    errors: List[BatchCreateBillScenarioUsageModificationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchCreateWorkloadEstimateUsageItemTypeDef(BaseValidatorModel):
    pass


class BatchCreateWorkloadEstimateUsageResponseTypeDef(BaseValidatorModel):
    items: List[BatchCreateWorkloadEstimateUsageItemTypeDef]
    errors: List[BatchCreateWorkloadEstimateUsageErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BillEstimateInputUsageModificationSummaryTypeDef(BaseValidatorModel):
    pass


class ListBillEstimateInputUsageModificationsResponseTypeDef(BaseValidatorModel):
    items: List[BillEstimateInputUsageModificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchUpdateBillScenarioUsageModificationErrorTypeDef(BaseValidatorModel):
    pass


class BillScenarioUsageModificationItemTypeDef(BaseValidatorModel):
    pass


class BatchUpdateBillScenarioUsageModificationResponseTypeDef(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItemTypeDef]
    errors: List[BatchUpdateBillScenarioUsageModificationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListBillScenarioUsageModificationsResponseTypeDef(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkloadEstimateUsageItemTypeDef(BaseValidatorModel):
    pass


class BatchUpdateWorkloadEstimateUsageErrorTypeDef(BaseValidatorModel):
    pass


class BatchUpdateWorkloadEstimateUsageResponseTypeDef(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItemTypeDef]
    errors: List[BatchUpdateWorkloadEstimateUsageErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListWorkloadEstimateUsageResponseTypeDef(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BillEstimateInputUsageModificationSummaryPaginatorTypeDef(BaseValidatorModel):
    pass


class ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef(BaseValidatorModel):
    items: List[BillEstimateInputUsageModificationSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BillScenarioUsageModificationItemPaginatorTypeDef(BaseValidatorModel):
    pass


class ListBillScenarioUsageModificationsResponsePaginatorTypeDef(BaseValidatorModel):
    items: List[BillScenarioUsageModificationItemPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkloadEstimateUsageItemPaginatorTypeDef(BaseValidatorModel):
    pass


class ListWorkloadEstimateUsageResponsePaginatorTypeDef(BaseValidatorModel):
    items: List[WorkloadEstimateUsageItemPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExpressionUnionTypeDef(BaseValidatorModel):
    pass


class BillIntervalUnionTypeDef(BaseValidatorModel):
    pass


class HistoricalUsageEntityTypeDef(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    usageAccountId: str
    billInterval: BillIntervalUnionTypeDef
    filterExpression: ExpressionUnionTypeDef
    location: Optional[str] = None


class HistoricalUsageEntityUnionTypeDef(BaseValidatorModel):
    pass


class BatchCreateBillScenarioUsageModificationEntryTypeDef(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    key: str
    usageAccountId: str
    availabilityZone: Optional[str] = None
    group: Optional[str] = None
    amounts: Optional[Sequence[UsageAmountTypeDef]] = None
    historicalUsage: Optional[HistoricalUsageEntityUnionTypeDef] = None


class BatchCreateWorkloadEstimateUsageEntryTypeDef(BaseValidatorModel):
    serviceCode: str
    usageType: str
    operation: str
    key: str
    usageAccountId: str
    amount: float
    group: Optional[str] = None
    historicalUsage: Optional[HistoricalUsageEntityUnionTypeDef] = None


class BatchCreateBillScenarioUsageModificationRequestTypeDef(BaseValidatorModel):
    billScenarioId: str
    usageModifications: Sequence[BatchCreateBillScenarioUsageModificationEntryTypeDef]
    clientToken: Optional[str] = None


class BatchCreateWorkloadEstimateUsageRequestTypeDef(BaseValidatorModel):
    workloadEstimateId: str
    usage: Sequence[BatchCreateWorkloadEstimateUsageEntryTypeDef]
    clientToken: Optional[str] = None


