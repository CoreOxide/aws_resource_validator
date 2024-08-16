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

class CheckSummaryTypeDef(BaseValidatorModel):
    arn: str
    awsServices: List[str]
    description: str
    id: str
    metadata: Dict[str, str]
    name: str
    pillars: List[RecommendationPillarType]
    source: RecommendationSourceType

class GetOrganizationRecommendationRequestRequestTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str

class GetRecommendationRequestRequestTypeDef(BaseValidatorModel):
    recommendationIdentifier: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChecksRequestRequestTypeDef(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None

class ListOrganizationRecommendationAccountsRequestRequestTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListOrganizationRecommendationResourcesRequestRequestTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None

class OrganizationRecommendationResourceSummaryTypeDef(BaseValidatorModel):
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

class ListRecommendationResourcesRequestRequestTypeDef(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None

class RecommendationResourceSummaryTypeDef(BaseValidatorModel):
    arn: str
    awsResourceId: str
    id: str
    lastUpdatedAt: datetime
    metadata: Dict[str, str]
    recommendationArn: str
    regionCode: str
    status: ResourceStatusType
    exclusionStatus: Optional[ExclusionStatusType] = None

class RecommendationResourcesAggregatesTypeDef(BaseValidatorModel):
    errorCount: int
    okCount: int
    warningCount: int

class RecommendationCostOptimizingAggregatesTypeDef(BaseValidatorModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float

class UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    organizationRecommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None

class UpdateRecommendationLifecycleRequestRequestTypeDef(BaseValidatorModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    recommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None

class BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef(BaseValidatorModel):
    recommendationResourceExclusions: Sequence[RecommendationResourceExclusionTypeDef]

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationRecommendationAccountsResponseTypeDef(BaseValidatorModel):
    accountRecommendationLifecycleSummaries: List[       AccountRecommendationLifecycleSummaryTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationResourceExclusionResponseTypeDef(BaseValidatorModel):
    batchUpdateRecommendationResourceExclusionErrors: List[       UpdateRecommendationResourceExclusionErrorTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChecksResponseTypeDef(BaseValidatorModel):
    checkSummaries: List[CheckSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChecksRequestListChecksPaginateTypeDef(BaseValidatorModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationAccountsRequestListOrganizationRecommendationAccountsPaginateTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationResourcesRequestListOrganizationRecommendationResourcesPaginateTypeDef(BaseValidatorModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationResourcesRequestListRecommendationResourcesPaginateTypeDef(BaseValidatorModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationResourcesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    organizationRecommendationResourceSummaries: List[       OrganizationRecommendationResourceSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationRecommendationsRequestListOrganizationRecommendationsPaginateTypeDef(BaseValidatorModel):
    afterLastUpdatedAt: Optional[TimestampTypeDef] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[TimestampTypeDef] = None
    checkIdentifier: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    afterLastUpdatedAt: Optional[TimestampTypeDef] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[TimestampTypeDef] = None
    checkIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None

class ListRecommendationsRequestListRecommendationsPaginateTypeDef(BaseValidatorModel):
    afterLastUpdatedAt: Optional[TimestampTypeDef] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[TimestampTypeDef] = None
    checkIdentifier: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    afterLastUpdatedAt: Optional[TimestampTypeDef] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[TimestampTypeDef] = None
    checkIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None

class ListRecommendationResourcesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    recommendationResourceSummaries: List[RecommendationResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationPillarSpecificAggregatesTypeDef(BaseValidatorModel):
    costOptimizing: Optional[RecommendationCostOptimizingAggregatesTypeDef] = None

class OrganizationRecommendationSummaryTypeDef(BaseValidatorModel):
    arn: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregatesTypeDef
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregatesTypeDef] = None

class OrganizationRecommendationTypeDef(BaseValidatorModel):
    arn: str
    description: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregatesTypeDef
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregatesTypeDef] = None
    resolvedAt: Optional[datetime] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None

class RecommendationSummaryTypeDef(BaseValidatorModel):
    arn: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregatesTypeDef
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregatesTypeDef] = None

class RecommendationTypeDef(BaseValidatorModel):
    arn: str
    description: str
    id: str
    name: str
    pillars: List[RecommendationPillarType]
    resourcesAggregates: RecommendationResourcesAggregatesTypeDef
    source: RecommendationSourceType
    status: RecommendationStatusType
    type: RecommendationTypeType
    awsServices: Optional[List[str]] = None
    checkArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    pillarSpecificAggregates: Optional[RecommendationPillarSpecificAggregatesTypeDef] = None
    resolvedAt: Optional[datetime] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None

class ListOrganizationRecommendationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    organizationRecommendationSummaries: List[OrganizationRecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationRecommendationResponseTypeDef(BaseValidatorModel):
    organizationRecommendation: OrganizationRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommendationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationResponseTypeDef(BaseValidatorModel):
    recommendation: RecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

