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
from aws_resource_validator.pydantic_models.trustedadvisor_constants import *

class AccountRecommendationLifecycleSummary(BaseValidatorModel):
    accountId: Optional[str] = None
    accountRecommendationArn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None


class RecommendationResourceExclusion(BaseValidatorModel):
    arn: str
    isExcluded: bool


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UpdateRecommendationResourceExclusionError(BaseValidatorModel):
    arn: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class GetOrganizationRecommendationRequest(BaseValidatorModel):
    organizationRecommendationIdentifier: str


class GetRecommendationRequest(BaseValidatorModel):
    recommendationIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChecksRequest(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None


class ListOrganizationRecommendationAccountsRequest(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListOrganizationRecommendationResourcesRequest(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None


class ListRecommendationResourcesRequest(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None


class RecommendationResourcesAggregates(BaseValidatorModel):
    errorCount: int
    okCount: int
    warningCount: int


class RecommendationCostOptimizingAggregates(BaseValidatorModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float


class UpdateOrganizationRecommendationLifecycleRequest(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    organizationRecommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None


class UpdateRecommendationLifecycleRequest(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    recommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None


class BatchUpdateRecommendationResourceExclusionRequest(BaseValidatorModel):
    recommendationResourceExclusions: Sequence[RecommendationResourceExclusion]


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListOrganizationRecommendationAccountsResponse(BaseValidatorModel):
    accountRecommendationLifecycleSummaries: List[AccountRecommendationLifecycleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchUpdateRecommendationResourceExclusionResponse(BaseValidatorModel):
    batchUpdateRecommendationResourceExclusionErrors: List[ UpdateRecommendationResourceExclusionError ]
    ResponseMetadata: ResponseMetadata


class CheckSummary(BaseValidatorModel):
    pass


class ListChecksResponse(BaseValidatorModel):
    checkSummaries: List[CheckSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListChecksRequestPaginate(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationRecommendationAccountsRequestPaginate(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationRecommendationResourcesRequestPaginate(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecommendationResourcesRequestPaginate(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class OrganizationRecommendationResourceSummary(BaseValidatorModel):
    pass


class ListOrganizationRecommendationResourcesResponse(BaseValidatorModel):
    organizationRecommendationResourceSummaries: List[ OrganizationRecommendationResourceSummary ]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecommendationResourceSummary(BaseValidatorModel):
    pass


class ListRecommendationResourcesResponse(BaseValidatorModel):
    recommendationResourceSummaries: List[RecommendationResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecommendationPillarSpecificAggregates(BaseValidatorModel):
    costOptimizing: Optional[RecommendationCostOptimizingAggregates] = None


class OrganizationRecommendationSummary(BaseValidatorModel):
    pass


class ListOrganizationRecommendationsResponse(BaseValidatorModel):
    organizationRecommendationSummaries: List[OrganizationRecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class OrganizationRecommendation(BaseValidatorModel):
    pass


class GetOrganizationRecommendationResponse(BaseValidatorModel):
    organizationRecommendation: OrganizationRecommendation
    ResponseMetadata: ResponseMetadata


class RecommendationSummary(BaseValidatorModel):
    pass


class ListRecommendationsResponse(BaseValidatorModel):
    recommendationSummaries: List[RecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Recommendation(BaseValidatorModel):
    pass


class GetRecommendationResponse(BaseValidatorModel):
    recommendation: Recommendation
    ResponseMetadata: ResponseMetadata


