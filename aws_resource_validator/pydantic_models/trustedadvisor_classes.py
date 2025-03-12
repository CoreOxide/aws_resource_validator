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

class AccountRecommendationLifecycleSummaryTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    accountRecommendationArn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None


class RecommendationResourceExclusionTypeDef(BaseValidatorModel):
    arn: str
    isExcluded: bool


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UpdateRecommendationResourceExclusionErrorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class GetOrganizationRecommendationRequestTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str


class GetRecommendationRequestTypeDef(BaseValidatorModel):
    recommendationIdentifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChecksRequestTypeDef(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None


class ListOrganizationRecommendationAccountsRequestTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListOrganizationRecommendationResourcesRequestTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None


class ListRecommendationResourcesRequestTypeDef(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None


class RecommendationResourcesAggregatesTypeDef(BaseValidatorModel):
    errorCount: int
    okCount: int
    warningCount: int


class RecommendationCostOptimizingAggregatesTypeDef(BaseValidatorModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float


class UpdateOrganizationRecommendationLifecycleRequestTypeDef(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    organizationRecommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None


class UpdateRecommendationLifecycleRequestTypeDef(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    recommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None


class BatchUpdateRecommendationResourceExclusionRequestTypeDef(BaseValidatorModel):
    recommendationResourceExclusions: Sequence[RecommendationResourceExclusionTypeDef]


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListOrganizationRecommendationAccountsResponseTypeDef(BaseValidatorModel):
    accountRecommendationLifecycleSummaries: List[AccountRecommendationLifecycleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchUpdateRecommendationResourceExclusionResponseTypeDef(BaseValidatorModel):
    batchUpdateRecommendationResourceExclusionErrors: List[ UpdateRecommendationResourceExclusionErrorTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef


class CheckSummaryTypeDef(BaseValidatorModel):
    pass


class ListChecksResponseTypeDef(BaseValidatorModel):
    checkSummaries: List[CheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListChecksRequestPaginateTypeDef(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationRecommendationAccountsRequestPaginateTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationRecommendationResourcesRequestPaginateTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecommendationResourcesRequestPaginateTypeDef(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class OrganizationRecommendationResourceSummaryTypeDef(BaseValidatorModel):
    pass


class ListOrganizationRecommendationResourcesResponseTypeDef(BaseValidatorModel):
    organizationRecommendationResourceSummaries: List[ OrganizationRecommendationResourceSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecommendationResourceSummaryTypeDef(BaseValidatorModel):
    pass


class ListRecommendationResourcesResponseTypeDef(BaseValidatorModel):
    recommendationResourceSummaries: List[RecommendationResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecommendationPillarSpecificAggregatesTypeDef(BaseValidatorModel):
    costOptimizing: Optional[RecommendationCostOptimizingAggregatesTypeDef] = None


class OrganizationRecommendationSummaryTypeDef(BaseValidatorModel):
    pass


class ListOrganizationRecommendationsResponseTypeDef(BaseValidatorModel):
    organizationRecommendationSummaries: List[OrganizationRecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class OrganizationRecommendationTypeDef(BaseValidatorModel):
    pass


class GetOrganizationRecommendationResponseTypeDef(BaseValidatorModel):
    organizationRecommendation: OrganizationRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RecommendationSummaryTypeDef(BaseValidatorModel):
    pass


class ListRecommendationsResponseTypeDef(BaseValidatorModel):
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecommendationTypeDef(BaseValidatorModel):
    pass


class GetRecommendationResponseTypeDef(BaseValidatorModel):
    recommendation: RecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


