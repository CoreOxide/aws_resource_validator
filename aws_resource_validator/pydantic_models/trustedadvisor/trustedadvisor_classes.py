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


# This class is the input for the 'get_organization_recommendation' function.
class GetOrganizationRecommendationRequest(BaseValidatorModel):
    organizationRecommendationIdentifier: str


# This class is the input for the 'get_recommendation' function.
class GetRecommendationRequest(BaseValidatorModel):
    recommendationIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_checks' function.
class ListChecksRequest(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None


# This class is the input for the 'list_organization_recommendation_accounts' function.
class ListOrganizationRecommendationAccountsRequest(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_organization_recommendation_resources' function.
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


# This class is the input for the 'list_recommendation_resources' function.
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


# This class is the input for the 'update_organization_recommendation_lifecycle' function.
class UpdateOrganizationRecommendationLifecycleRequest(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    organizationRecommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None


# This class is the input for the 'update_recommendation_lifecycle' function.
class UpdateRecommendationLifecycleRequest(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    recommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None


# This class is the input for the 'batch_update_recommendation_resource_exclusion' function.
class BatchUpdateRecommendationResourceExclusionRequest(BaseValidatorModel):
    recommendationResourceExclusions: List[RecommendationResourceExclusion]


# This class is the output for the 'update_recommendation_lifecycle' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_organization_recommendation_accounts' function.
class ListOrganizationRecommendationAccountsResponse(BaseValidatorModel):
    accountRecommendationLifecycleSummaries: List[AccountRecommendationLifecycleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_update_recommendation_resource_exclusion' function.
class BatchUpdateRecommendationResourceExclusionResponse(BaseValidatorModel):
    batchUpdateRecommendationResourceExclusionErrors: List[UpdateRecommendationResourceExclusionError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_checks' function.
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


# This class is the output for the 'list_organization_recommendation_resources' function.
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


# This class is the input for the 'list_organization_recommendations' function.
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


# This class is the input for the 'list_recommendations' function.
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


# This class is the output for the 'list_recommendation_resources' function.
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


# This class is the output for the 'list_organization_recommendations' function.
class ListOrganizationRecommendationsResponse(BaseValidatorModel):
    organizationRecommendationSummaries: List[OrganizationRecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_organization_recommendation' function.
class GetOrganizationRecommendationResponse(BaseValidatorModel):
    organizationRecommendation: OrganizationRecommendation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_recommendations' function.
class ListRecommendationsResponse(BaseValidatorModel):
    recommendationSummaries: List[RecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_recommendation' function.
class GetRecommendationResponse(BaseValidatorModel):
    recommendation: Recommendation
    ResponseMetadata: ResponseMetadata