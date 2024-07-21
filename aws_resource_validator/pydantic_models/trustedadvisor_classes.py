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
from aws_resource_validator.pydantic_models.trustedadvisor_constants import *

class AccountRecommendationLifecycleSummaryTypeDef(BaseModel):
    accountId: Optional[str] = None
    accountRecommendationArn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleStage: Optional[RecommendationLifecycleStageType] = None
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None
    updatedOnBehalfOf: Optional[str] = None
    updatedOnBehalfOfJobTitle: Optional[str] = None

class RecommendationResourceExclusionTypeDef(BaseModel):
    arn: str
    isExcluded: bool

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UpdateRecommendationResourceExclusionErrorTypeDef(BaseModel):
    arn: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class CheckSummaryTypeDef(BaseModel):
    arn: str
    awsServices: List[str]
    description: str
    id: str
    metadata: Dict[str, str]
    name: str
    pillars: List[RecommendationPillarType]
    source: RecommendationSourceType

class GetOrganizationRecommendationRequestRequestTypeDef(BaseModel):
    organizationRecommendationIdentifier: str

class GetRecommendationRequestRequestTypeDef(BaseModel):
    recommendationIdentifier: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChecksRequestRequestTypeDef(BaseModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None

class ListOrganizationRecommendationAccountsRequestRequestTypeDef(BaseModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListOrganizationRecommendationResourcesRequestRequestTypeDef(BaseModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None

class OrganizationRecommendationResourceSummaryTypeDef(BaseModel):
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

class ListRecommendationResourcesRequestRequestTypeDef(BaseModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None

class RecommendationResourceSummaryTypeDef(BaseModel):
    arn: str
    awsResourceId: str
    id: str
    lastUpdatedAt: datetime
    metadata: Dict[str, str]
    recommendationArn: str
    regionCode: str
    status: ResourceStatusType
    exclusionStatus: Optional[ExclusionStatusType] = None

class RecommendationResourcesAggregatesTypeDef(BaseModel):
    errorCount: int
    okCount: int
    warningCount: int

class RecommendationCostOptimizingAggregatesTypeDef(BaseModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float

class UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef(BaseModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    organizationRecommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None

class UpdateRecommendationLifecycleRequestRequestTypeDef(BaseModel):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    recommendationIdentifier: str
    updateReason: Optional[str] = None
    updateReasonCode: Optional[UpdateRecommendationLifecycleStageReasonCodeType] = None

class BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef(BaseModel):
    recommendationResourceExclusions: Sequence[RecommendationResourceExclusionTypeDef]

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationRecommendationAccountsResponseTypeDef(BaseModel):
    accountRecommendationLifecycleSummaries: List[       AccountRecommendationLifecycleSummaryTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationResourceExclusionResponseTypeDef(BaseModel):
    batchUpdateRecommendationResourceExclusionErrors: List[       UpdateRecommendationResourceExclusionErrorTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChecksResponseTypeDef(BaseModel):
    checkSummaries: List[CheckSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChecksRequestListChecksPaginateTypeDef(BaseModel):
    awsService: Optional[str] = None
    language: Optional[RecommendationLanguageType] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationAccountsRequestListOrganizationRecommendationAccountsPaginateTypeDef(BaseModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationResourcesRequestListOrganizationRecommendationResourcesPaginateTypeDef(BaseModel):
    organizationRecommendationIdentifier: str
    affectedAccountId: Optional[str] = None
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationResourcesRequestListRecommendationResourcesPaginateTypeDef(BaseModel):
    recommendationIdentifier: str
    exclusionStatus: Optional[ExclusionStatusType] = None
    regionCode: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationResourcesResponseTypeDef(BaseModel):
    nextToken: str
    organizationRecommendationResourceSummaries: List[       OrganizationRecommendationResourceSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationRecommendationsRequestListOrganizationRecommendationsPaginateTypeDef(BaseModel):
    afterLastUpdatedAt: Optional[TimestampTypeDef] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[TimestampTypeDef] = None
    checkIdentifier: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationRecommendationsRequestRequestTypeDef(BaseModel):
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

class ListRecommendationsRequestListRecommendationsPaginateTypeDef(BaseModel):
    afterLastUpdatedAt: Optional[TimestampTypeDef] = None
    awsService: Optional[str] = None
    beforeLastUpdatedAt: Optional[TimestampTypeDef] = None
    checkIdentifier: Optional[str] = None
    pillar: Optional[RecommendationPillarType] = None
    source: Optional[RecommendationSourceType] = None
    status: Optional[RecommendationStatusType] = None
    type: Optional[RecommendationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsRequestRequestTypeDef(BaseModel):
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

class ListRecommendationResourcesResponseTypeDef(BaseModel):
    nextToken: str
    recommendationResourceSummaries: List[RecommendationResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationPillarSpecificAggregatesTypeDef(BaseModel):
    costOptimizing: Optional[RecommendationCostOptimizingAggregatesTypeDef] = None

class OrganizationRecommendationSummaryTypeDef(BaseModel):
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

class OrganizationRecommendationTypeDef(BaseModel):
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

class RecommendationSummaryTypeDef(BaseModel):
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

class RecommendationTypeDef(BaseModel):
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

class ListOrganizationRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    organizationRecommendationSummaries: List[OrganizationRecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationRecommendationResponseTypeDef(BaseModel):
    organizationRecommendation: OrganizationRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationResponseTypeDef(BaseModel):
    recommendation: RecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

