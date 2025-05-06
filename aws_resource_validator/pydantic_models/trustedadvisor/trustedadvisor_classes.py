from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.trustedadvisor.trustedadvisor_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class CheckSummary(BaseValidatorModel):
    arn: str
    awsServices: List[str]
    description: str
    id: str
    metadata: Dict[str, str]
    name: str
    pillars: List[RecommendationPillarType]
    source: RecommendationSourceType


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


class OrganizationRecommendationResourceSummary(BaseValidatorModel):
    arn: str
    awsResourceId: str
    id: str
    lastUpdatedAt: datetime
    metadata: Dict[str, str]
    recommendationArn: str
    regionCode: str
    status: ResourceStatusType
    accountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None

Timestamp = Union[datetime, str]


class ListRecommendationResourcesRequest(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None


class RecommendationResourceSummary(BaseValidatorModel):
    arn: str
    awsResourceId: str
    id: str
    lastUpdatedAt: datetime
    metadata: Dict[str, str]
    recommendationArn: str
    regionCode: str
    status: ResourceStatusType
    exclusionStatus: Optional[ExclusionStatusType] = None


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
    recommendationResourceExclusions: List[RecommendationResourceExclusion]


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListOrganizationRecommendationAccountsResponse(BaseValidatorModel):
    accountRecommendationLifecycleSummaries: List[AccountRecommendationLifecycleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchUpdateRecommendationResourceExclusionResponse(BaseValidatorModel):
    batchUpdateRecommendationResourceExclusionErrors: List[UpdateRecommendationResourceExclusionError]
    ResponseMetadata: ResponseMetadata


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


class ListOrganizationRecommendationResourcesResponse(BaseValidatorModel):
    organizationRecommendationResourceSummaries: List[OrganizationRecommendationResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListOrganizationRecommendationsRequestPaginate(BaseValidatorModel):
    afterLastUpdatedAt: Optional[Timestamp] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[Timestamp] = None
    checkIdentifier: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationRecommendationsRequest(BaseValidatorModel):
    afterLastUpdatedAt: Optional[Timestamp] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[Timestamp] = None
    checkIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None


class ListRecommendationsRequestPaginate(BaseValidatorModel):
    afterLastUpdatedAt: Optional[Timestamp] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[Timestamp] = None
    checkIdentifier: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecommendationsRequest(BaseValidatorModel):
    afterLastUpdatedAt: Optional[Timestamp] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[Timestamp] = None
    checkIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None


class ListRecommendationResourcesResponse(BaseValidatorModel):
    recommendationResourceSummaries: List[RecommendationResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecommendationPillarSpecificAggregates(BaseValidatorModel):
    costOptimizing: Optional[RecommendationCostOptimizingAggregates] = None


class OrganizationRecommendationSummary(BaseValidatorModel):
    arn: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregates
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregates] = None


class OrganizationRecommendation(BaseValidatorModel):
    arn: str
    description: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregates
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregates] = None
    resolvedAt: Optional[datetime] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None


class RecommendationSummary(BaseValidatorModel):
    arn: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregates
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregates] = None


class Recommendation(BaseValidatorModel):
    arn: str
    description: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregates
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregates] = None
    resolvedAt: Optional[datetime] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None


class ListOrganizationRecommendationsResponse(BaseValidatorModel):
    organizationRecommendationSummaries: List[OrganizationRecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetOrganizationRecommendationResponse(BaseValidatorModel):
    organizationRecommendation: OrganizationRecommendation
    ResponseMetadata: ResponseMetadata


class ListRecommendationsResponse(BaseValidatorModel):
    recommendationSummaries: List[RecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetRecommendationResponse(BaseValidatorModel):
    recommendation: Recommendation
    ResponseMetadata: ResponseMetadata