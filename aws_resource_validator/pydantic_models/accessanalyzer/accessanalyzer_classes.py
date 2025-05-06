from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.accessanalyzer.accessanalyzer_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessPreviewStatusReason(BaseValidatorModel):
    code: AccessPreviewStatusReasonCodeType


class Access(BaseValidatorModel):
    actions: Optional[List[str]] = None
    resources: Optional[List[str]] = None


class AclGrantee(BaseValidatorModel):
    id: Optional[str] = None
    uri: Optional[str] = None


class AnalysisRuleCriteriaOutput(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    resourceTags: Optional[List[Dict[str, str]]] = None


class AnalysisRuleCriteria(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    resourceTags: Optional[List[Dict[str, str]]] = None


class AnalyzedResourceSummary(BaseValidatorModel):
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceTypeType


class AnalyzedResource(BaseValidatorModel):
    resourceArn: str
    resourceType: ResourceTypeType
    createdAt: datetime
    analyzedAt: datetime
    updatedAt: datetime
    isPublic: bool
    resourceOwnerAccount: str
    actions: Optional[List[str]] = None
    sharedVia: Optional[List[str]] = None
    status: Optional[FindingStatusType] = None
    error: Optional[str] = None


class StatusReason(BaseValidatorModel):
    code: ReasonCodeType


class ApplyArchiveRuleRequest(BaseValidatorModel):
    analyzerArn: str
    ruleName: str
    clientToken: Optional[str] = None


class CriterionOutput(BaseValidatorModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None


class CancelPolicyGenerationRequest(BaseValidatorModel):
    jobId: str


class ReasonSummary(BaseValidatorModel):
    description: Optional[str] = None
    statementIndex: Optional[int] = None
    statementId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CheckNoNewAccessRequest(BaseValidatorModel):
    newPolicyDocument: str
    existingPolicyDocument: str
    policyType: AccessCheckPolicyTypeType


class CheckNoPublicAccessRequest(BaseValidatorModel):
    policyDocument: str
    resourceType: AccessCheckResourceTypeType

Timestamp = Union[datetime, str]


class Trail(BaseValidatorModel):
    cloudTrailArn: str
    regions: Optional[List[str]] = None
    allRegions: Optional[bool] = None


class TrailProperties(BaseValidatorModel):
    cloudTrailArn: str
    regions: Optional[List[str]] = None
    allRegions: Optional[bool] = None


class DynamodbStreamConfiguration(BaseValidatorModel):
    streamPolicy: Optional[str] = None


class DynamodbTableConfiguration(BaseValidatorModel):
    tablePolicy: Optional[str] = None


class EbsSnapshotConfigurationOutput(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None


class EcrRepositoryConfiguration(BaseValidatorModel):
    repositoryPolicy: Optional[str] = None


class EfsFileSystemConfiguration(BaseValidatorModel):
    fileSystemPolicy: Optional[str] = None


class IamRoleConfiguration(BaseValidatorModel):
    trustPolicy: Optional[str] = None


class S3ExpressDirectoryBucketConfiguration(BaseValidatorModel):
    bucketPolicy: Optional[str] = None


class SecretsManagerSecretConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None
    secretPolicy: Optional[str] = None


class SnsTopicConfiguration(BaseValidatorModel):
    topicPolicy: Optional[str] = None


class SqsQueueConfiguration(BaseValidatorModel):
    queuePolicy: Optional[str] = None


class Criterion(BaseValidatorModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None


class DeleteAnalyzerRequest(BaseValidatorModel):
    analyzerName: str
    clientToken: Optional[str] = None


class DeleteArchiveRuleRequest(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    clientToken: Optional[str] = None


class EbsSnapshotConfiguration(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None


class ResourceTypeDetails(BaseValidatorModel):
    totalActivePublic: Optional[int] = None
    totalActiveCrossAccount: Optional[int] = None


class FindingAggregationAccountDetails(BaseValidatorModel):
    account: Optional[str] = None
    numberOfActiveFindings: Optional[int] = None
    details: Optional[Dict[str, int]] = None


class UnusedIamRoleDetails(BaseValidatorModel):
    lastAccessed: Optional[datetime] = None


class UnusedIamUserAccessKeyDetails(BaseValidatorModel):
    accessKeyId: str
    lastAccessed: Optional[datetime] = None


class UnusedIamUserPasswordDetails(BaseValidatorModel):
    lastAccessed: Optional[datetime] = None


class FindingSourceDetail(BaseValidatorModel):
    accessPointArn: Optional[str] = None
    accessPointAccount: Optional[str] = None


class FindingSummaryV2(BaseValidatorModel):
    analyzedAt: datetime
    createdAt: datetime
    id: str
    resourceType: ResourceTypeType
    resourceOwnerAccount: str
    status: FindingStatusType
    updatedAt: datetime
    error: Optional[str] = None
    resource: Optional[str] = None
    findingType: Optional[FindingTypeType] = None


class GenerateFindingRecommendationRequest(BaseValidatorModel):
    analyzerArn: str
    id: str


class GeneratedPolicy(BaseValidatorModel):
    policy: str


class GetAccessPreviewRequest(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str


class GetAnalyzedResourceRequest(BaseValidatorModel):
    analyzerArn: str
    resourceArn: str


class GetAnalyzerRequest(BaseValidatorModel):
    analyzerName: str


class GetArchiveRuleRequest(BaseValidatorModel):
    analyzerName: str
    ruleName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetFindingRecommendationRequest(BaseValidatorModel):
    analyzerArn: str
    id: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RecommendationError(BaseValidatorModel):
    code: str
    message: str


class GetFindingRequest(BaseValidatorModel):
    analyzerArn: str
    id: str


class GetFindingV2Request(BaseValidatorModel):
    analyzerArn: str
    id: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetFindingsStatisticsRequest(BaseValidatorModel):
    analyzerArn: str


class GetGeneratedPolicyRequest(BaseValidatorModel):
    jobId: str
    includeResourcePlaceholders: Optional[bool] = None
    includeServiceLevelTemplate: Optional[bool] = None


class JobError(BaseValidatorModel):
    code: JobErrorCodeType
    message: str


class KmsGrantConstraintsOutput(BaseValidatorModel):
    encryptionContextEquals: Optional[Dict[str, str]] = None
    encryptionContextSubset: Optional[Dict[str, str]] = None


class KmsGrantConstraints(BaseValidatorModel):
    encryptionContextEquals: Optional[Dict[str, str]] = None
    encryptionContextSubset: Optional[Dict[str, str]] = None


class ListAccessPreviewsRequest(BaseValidatorModel):
    analyzerArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAnalyzedResourcesRequest(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAnalyzersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    type: Optional[TypeType] = None


class ListArchiveRulesRequest(BaseValidatorModel):
    analyzerName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SortCriteria(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class ListPolicyGenerationsRequest(BaseValidatorModel):
    principalArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PolicyGeneration(BaseValidatorModel):
    jobId: str
    principalArn: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class VpcConfiguration(BaseValidatorModel):
    vpcId: str


class Substring(BaseValidatorModel):
    start: int
    length: int


class PolicyGenerationDetails(BaseValidatorModel):
    principalArn: str


class Position(BaseValidatorModel):
    line: int
    column: int
    offset: int


class RdsDbClusterSnapshotAttributeValueOutput(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class RdsDbClusterSnapshotAttributeValue(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class RdsDbSnapshotAttributeValueOutput(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class RdsDbSnapshotAttributeValue(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class UnusedPermissionsRecommendedStep(BaseValidatorModel):
    recommendedAction: RecommendedRemediationActionType
    policyUpdatedAt: Optional[datetime] = None
    recommendedPolicy: Optional[str] = None
    existingPolicyId: Optional[str] = None


class S3PublicAccessBlockConfiguration(BaseValidatorModel):
    ignorePublicAcls: bool
    restrictPublicBuckets: bool


class StartResourceScanRequest(BaseValidatorModel):
    analyzerArn: str
    resourceArn: str
    resourceOwnerAccount: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UnusedAccessTypeStatistics(BaseValidatorModel):
    unusedAccessType: Optional[str] = None
    total: Optional[int] = None


class UnusedAction(BaseValidatorModel):
    action: str
    lastAccessed: Optional[datetime] = None


class UpdateFindingsRequest(BaseValidatorModel):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: Optional[List[str]] = None
    resourceArn: Optional[str] = None
    clientToken: Optional[str] = None


class ValidatePolicyRequest(BaseValidatorModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None


class AccessPreviewSummary(BaseValidatorModel):
    id: str
    analyzerArn: str
    createdAt: datetime
    status: AccessPreviewStatusType
    statusReason: Optional[AccessPreviewStatusReason] = None


class CheckAccessNotGrantedRequest(BaseValidatorModel):
    policyDocument: str
    access: List[Access]
    policyType: AccessCheckPolicyTypeType


class S3BucketAclGrantConfiguration(BaseValidatorModel):
    permission: AclPermissionType
    grantee: AclGrantee


class AnalysisRuleOutput(BaseValidatorModel):
    exclusions: Optional[List[AnalysisRuleCriteriaOutput]] = None


class AnalysisRule(BaseValidatorModel):
    exclusions: Optional[List[AnalysisRuleCriteria]] = None


class ArchiveRuleSummary(BaseValidatorModel):
    ruleName: str
    filter: Dict[str, CriterionOutput]
    createdAt: datetime
    updatedAt: datetime


class CheckAccessNotGrantedResponse(BaseValidatorModel):
    result: CheckAccessNotGrantedResultType
    message: str
    reasons: List[ReasonSummary]
    ResponseMetadata: ResponseMetadata


class CheckNoNewAccessResponse(BaseValidatorModel):
    result: CheckNoNewAccessResultType
    message: str
    reasons: List[ReasonSummary]
    ResponseMetadata: ResponseMetadata


class CheckNoPublicAccessResponse(BaseValidatorModel):
    result: CheckNoPublicAccessResultType
    message: str
    reasons: List[ReasonSummary]
    ResponseMetadata: ResponseMetadata


class CreateAccessPreviewResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


class CreateAnalyzerResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAnalyzedResourceResponse(BaseValidatorModel):
    resource: AnalyzedResource
    ResponseMetadata: ResponseMetadata


class ListAnalyzedResourcesResponse(BaseValidatorModel):
    analyzedResources: List[AnalyzedResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartPolicyGenerationResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class CloudTrailDetails(BaseValidatorModel):
    trails: List[Trail]
    accessRole: str
    startTime: Timestamp
    endTime: Optional[Timestamp] = None


class CloudTrailProperties(BaseValidatorModel):
    trailProperties: List[TrailProperties]
    startTime: datetime
    endTime: datetime

CriterionUnion = Union[Criterion, CriterionOutput]

EbsSnapshotConfigurationUnion = Union[EbsSnapshotConfiguration, EbsSnapshotConfigurationOutput]


class ExternalAccessFindingsStatistics(BaseValidatorModel):
    resourceTypeStatistics: Optional[Dict[ResourceTypeType, ResourceTypeDetails]] = None
    totalActiveFindings: Optional[int] = None
    totalArchivedFindings: Optional[int] = None
    totalResolvedFindings: Optional[int] = None


class FindingSource(BaseValidatorModel):
    type: FindingSourceTypeType
    detail: Optional[FindingSourceDetail] = None


class ListFindingsV2Response(BaseValidatorModel):
    findings: List[FindingSummaryV2]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFindingRecommendationRequestPaginate(BaseValidatorModel):
    analyzerArn: str
    id: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFindingV2RequestPaginate(BaseValidatorModel):
    analyzerArn: str
    id: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessPreviewsRequestPaginate(BaseValidatorModel):
    analyzerArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnalyzedResourcesRequestPaginate(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnalyzersRequestPaginate(BaseValidatorModel):
    type: Optional[TypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListArchiveRulesRequestPaginate(BaseValidatorModel):
    analyzerName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyGenerationsRequestPaginate(BaseValidatorModel):
    principalArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ValidatePolicyRequestPaginate(BaseValidatorModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class JobDetails(BaseValidatorModel):
    jobId: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None
    jobError: Optional[JobError] = None


class KmsGrantConfigurationOutput(BaseValidatorModel):
    operations: List[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsOutput] = None

KmsGrantConstraintsUnion = Union[KmsGrantConstraints, KmsGrantConstraintsOutput]


class ListPolicyGenerationsResponse(BaseValidatorModel):
    policyGenerations: List[PolicyGeneration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NetworkOriginConfigurationOutput(BaseValidatorModel):
    vpcConfiguration: Optional[VpcConfiguration] = None
    internetConfiguration: Optional[Dict[str, Any]] = None


class NetworkOriginConfiguration(BaseValidatorModel):
    vpcConfiguration: Optional[VpcConfiguration] = None
    internetConfiguration: Optional[Dict[str, Any]] = None


class PathElement(BaseValidatorModel):
    index: Optional[int] = None
    key: Optional[str] = None
    substring: Optional[Substring] = None
    value: Optional[str] = None


class Span(BaseValidatorModel):
    start: Position
    end: Position


class RdsDbClusterSnapshotConfigurationOutput(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbClusterSnapshotAttributeValueOutput]] = None
    kmsKeyId: Optional[str] = None

RdsDbClusterSnapshotAttributeValueUnion = Union[RdsDbClusterSnapshotAttributeValue, RdsDbClusterSnapshotAttributeValueOutput]


class RdsDbSnapshotConfigurationOutput(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbSnapshotAttributeValueOutput]] = None
    kmsKeyId: Optional[str] = None

RdsDbSnapshotAttributeValueUnion = Union[RdsDbSnapshotAttributeValue, RdsDbSnapshotAttributeValueOutput]


class RecommendedStep(BaseValidatorModel):
    unusedPermissionsRecommendedStep: Optional[UnusedPermissionsRecommendedStep] = None


class UnusedAccessFindingsStatistics(BaseValidatorModel):
    unusedAccessTypeStatistics: Optional[List[UnusedAccessTypeStatistics]] = None
    topAccounts: Optional[List[FindingAggregationAccountDetails]] = None
    totalActiveFindings: Optional[int] = None
    totalArchivedFindings: Optional[int] = None
    totalResolvedFindings: Optional[int] = None


class UnusedPermissionDetails(BaseValidatorModel):
    serviceNamespace: str
    actions: Optional[List[UnusedAction]] = None
    lastAccessed: Optional[datetime] = None


class ListAccessPreviewsResponse(BaseValidatorModel):
    accessPreviews: List[AccessPreviewSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UnusedAccessConfigurationOutput(BaseValidatorModel):
    unusedAccessAge: Optional[int] = None
    analysisRule: Optional[AnalysisRuleOutput] = None


class UnusedAccessConfiguration(BaseValidatorModel):
    unusedAccessAge: Optional[int] = None
    analysisRule: Optional[AnalysisRule] = None


class GetArchiveRuleResponse(BaseValidatorModel):
    archiveRule: ArchiveRuleSummary
    ResponseMetadata: ResponseMetadata


class ListArchiveRulesResponse(BaseValidatorModel):
    archiveRules: List[ArchiveRuleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartPolicyGenerationRequest(BaseValidatorModel):
    policyGenerationDetails: PolicyGenerationDetails
    cloudTrailDetails: Optional[CloudTrailDetails] = None
    clientToken: Optional[str] = None


class GeneratedPolicyProperties(BaseValidatorModel):
    principalArn: str
    isComplete: Optional[bool] = None
    cloudTrailProperties: Optional[CloudTrailProperties] = None


class CreateArchiveRuleRequest(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    filter: Dict[str, CriterionUnion]
    clientToken: Optional[str] = None


class InlineArchiveRule(BaseValidatorModel):
    ruleName: str
    filter: Dict[str, CriterionUnion]


class ListAccessPreviewFindingsRequestPaginate(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str
    filter: Optional[Dict[str, CriterionUnion]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessPreviewFindingsRequest(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str
    filter: Optional[Dict[str, CriterionUnion]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFindingsRequestPaginate(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Dict[str, CriterionUnion]] = None
    sort: Optional[SortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsRequest(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Dict[str, CriterionUnion]] = None
    sort: Optional[SortCriteria] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFindingsV2RequestPaginate(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Dict[str, CriterionUnion]] = None
    sort: Optional[SortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsV2Request(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Dict[str, CriterionUnion]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortCriteria] = None


class UpdateArchiveRuleRequest(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    filter: Dict[str, CriterionUnion]
    clientToken: Optional[str] = None


class AccessPreviewFinding(BaseValidatorModel):
    id: str
    resourceType: ResourceTypeType
    createdAt: datetime
    changeType: FindingChangeTypeType
    status: FindingStatusType
    resourceOwnerAccount: str
    existingFindingId: Optional[str] = None
    existingFindingStatus: Optional[FindingStatusType] = None
    principal: Optional[Dict[str, str]] = None
    action: Optional[List[str]] = None
    condition: Optional[Dict[str, str]] = None
    resource: Optional[str] = None
    isPublic: Optional[bool] = None
    error: Optional[str] = None
    sources: Optional[List[FindingSource]] = None
    resourceControlPolicyRestriction: Optional[ResourceControlPolicyRestrictionType] = None


class ExternalAccessDetails(BaseValidatorModel):
    condition: Dict[str, str]
    action: Optional[List[str]] = None
    isPublic: Optional[bool] = None
    principal: Optional[Dict[str, str]] = None
    sources: Optional[List[FindingSource]] = None
    resourceControlPolicyRestriction: Optional[ResourceControlPolicyRestrictionType] = None


class FindingSummary(BaseValidatorModel):
    id: str
    resourceType: ResourceTypeType
    condition: Dict[str, str]
    createdAt: datetime
    analyzedAt: datetime
    updatedAt: datetime
    status: FindingStatusType
    resourceOwnerAccount: str
    principal: Optional[Dict[str, str]] = None
    action: Optional[List[str]] = None
    resource: Optional[str] = None
    isPublic: Optional[bool] = None
    error: Optional[str] = None
    sources: Optional[List[FindingSource]] = None
    resourceControlPolicyRestriction: Optional[ResourceControlPolicyRestrictionType] = None


class Finding(BaseValidatorModel):
    id: str
    resourceType: ResourceTypeType
    condition: Dict[str, str]
    createdAt: datetime
    analyzedAt: datetime
    updatedAt: datetime
    status: FindingStatusType
    resourceOwnerAccount: str
    principal: Optional[Dict[str, str]] = None
    action: Optional[List[str]] = None
    resource: Optional[str] = None
    isPublic: Optional[bool] = None
    error: Optional[str] = None
    sources: Optional[List[FindingSource]] = None
    resourceControlPolicyRestriction: Optional[ResourceControlPolicyRestrictionType] = None


class KmsKeyConfigurationOutput(BaseValidatorModel):
    keyPolicies: Optional[Dict[str, str]] = None
    grants: Optional[List[KmsGrantConfigurationOutput]] = None


class KmsGrantConfiguration(BaseValidatorModel):
    operations: List[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsUnion] = None


class S3AccessPointConfigurationOutput(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    networkOrigin: Optional[NetworkOriginConfigurationOutput] = None

NetworkOriginConfigurationUnion = Union[NetworkOriginConfiguration, NetworkOriginConfigurationOutput]


class Location(BaseValidatorModel):
    path: List[PathElement]
    span: Span


class RdsDbClusterSnapshotConfiguration(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbClusterSnapshotAttributeValueUnion]] = None
    kmsKeyId: Optional[str] = None


class RdsDbSnapshotConfiguration(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbSnapshotAttributeValueUnion]] = None
    kmsKeyId: Optional[str] = None


class GetFindingRecommendationResponse(BaseValidatorModel):
    startedAt: datetime
    completedAt: datetime
    error: RecommendationError
    resourceArn: str
    recommendedSteps: List[RecommendedStep]
    recommendationType: Literal['UnusedPermissionRecommendation']
    status: StatusType
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FindingsStatistics(BaseValidatorModel):
    externalAccessFindingsStatistics: Optional[ExternalAccessFindingsStatistics] = None
    unusedAccessFindingsStatistics: Optional[UnusedAccessFindingsStatistics] = None


class AnalyzerConfigurationOutput(BaseValidatorModel):
    unusedAccess: Optional[UnusedAccessConfigurationOutput] = None


class AnalyzerConfiguration(BaseValidatorModel):
    unusedAccess: Optional[UnusedAccessConfiguration] = None


class GeneratedPolicyResult(BaseValidatorModel):
    properties: GeneratedPolicyProperties
    generatedPolicies: Optional[List[GeneratedPolicy]] = None


class ListAccessPreviewFindingsResponse(BaseValidatorModel):
    findings: List[AccessPreviewFinding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FindingDetails(BaseValidatorModel):
    externalAccessDetails: Optional[ExternalAccessDetails] = None
    unusedPermissionDetails: Optional[UnusedPermissionDetails] = None
    unusedIamUserAccessKeyDetails: Optional[UnusedIamUserAccessKeyDetails] = None
    unusedIamRoleDetails: Optional[UnusedIamRoleDetails] = None
    unusedIamUserPasswordDetails: Optional[UnusedIamUserPasswordDetails] = None


class ListFindingsResponse(BaseValidatorModel):
    findings: List[FindingSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFindingResponse(BaseValidatorModel):
    finding: Finding
    ResponseMetadata: ResponseMetadata

KmsGrantConfigurationUnion = Union[KmsGrantConfiguration, KmsGrantConfigurationOutput]


class S3BucketConfigurationOutput(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[List[S3BucketAclGrantConfiguration]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    accessPoints: Optional[Dict[str, S3AccessPointConfigurationOutput]] = None


class S3AccessPointConfiguration(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    networkOrigin: Optional[NetworkOriginConfigurationUnion] = None


class ValidatePolicyFinding(BaseValidatorModel):
    findingDetails: str
    findingType: ValidatePolicyFindingTypeType
    issueCode: str
    learnMoreLink: str
    locations: List[Location]

RdsDbClusterSnapshotConfigurationUnion = Union[RdsDbClusterSnapshotConfiguration, RdsDbClusterSnapshotConfigurationOutput]

RdsDbSnapshotConfigurationUnion = Union[RdsDbSnapshotConfiguration, RdsDbSnapshotConfigurationOutput]


class GetFindingsStatisticsResponse(BaseValidatorModel):
    findingsStatistics: List[FindingsStatistics]
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class AnalyzerSummary(BaseValidatorModel):
    arn: str
    name: str
    type: TypeType
    createdAt: datetime
    status: AnalyzerStatusType
    lastResourceAnalyzed: Optional[str] = None
    lastResourceAnalyzedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    statusReason: Optional[StatusReason] = None
    configuration: Optional[AnalyzerConfigurationOutput] = None


class UpdateAnalyzerResponse(BaseValidatorModel):
    configuration: AnalyzerConfigurationOutput
    ResponseMetadata: ResponseMetadata

AnalyzerConfigurationUnion = Union[AnalyzerConfiguration, AnalyzerConfigurationOutput]


class GetGeneratedPolicyResponse(BaseValidatorModel):
    jobDetails: JobDetails
    generatedPolicyResult: GeneratedPolicyResult
    ResponseMetadata: ResponseMetadata


class GetFindingV2Response(BaseValidatorModel):
    analyzedAt: datetime
    createdAt: datetime
    error: str
    id: str
    resource: str
    resourceType: ResourceTypeType
    resourceOwnerAccount: str
    status: FindingStatusType
    updatedAt: datetime
    findingDetails: List[FindingDetails]
    findingType: FindingTypeType
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class KmsKeyConfiguration(BaseValidatorModel):
    keyPolicies: Optional[Dict[str, str]] = None
    grants: Optional[List[KmsGrantConfigurationUnion]] = None


class ConfigurationOutput(BaseValidatorModel):
    ebsSnapshot: Optional[EbsSnapshotConfigurationOutput] = None
    ecrRepository: Optional[EcrRepositoryConfiguration] = None
    iamRole: Optional[IamRoleConfiguration] = None
    efsFileSystem: Optional[EfsFileSystemConfiguration] = None
    kmsKey: Optional[KmsKeyConfigurationOutput] = None
    rdsDbClusterSnapshot: Optional[RdsDbClusterSnapshotConfigurationOutput] = None
    rdsDbSnapshot: Optional[RdsDbSnapshotConfigurationOutput] = None
    secretsManagerSecret: Optional[SecretsManagerSecretConfiguration] = None
    s3Bucket: Optional[S3BucketConfigurationOutput] = None
    snsTopic: Optional[SnsTopicConfiguration] = None
    sqsQueue: Optional[SqsQueueConfiguration] = None
    s3ExpressDirectoryBucket: Optional[S3ExpressDirectoryBucketConfiguration] = None
    dynamodbStream: Optional[DynamodbStreamConfiguration] = None
    dynamodbTable: Optional[DynamodbTableConfiguration] = None

S3AccessPointConfigurationUnion = Union[S3AccessPointConfiguration, S3AccessPointConfigurationOutput]


class ValidatePolicyResponse(BaseValidatorModel):
    findings: List[ValidatePolicyFinding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetAnalyzerResponse(BaseValidatorModel):
    analyzer: AnalyzerSummary
    ResponseMetadata: ResponseMetadata


class ListAnalyzersResponse(BaseValidatorModel):
    analyzers: List[AnalyzerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAnalyzerRequest(BaseValidatorModel):
    analyzerName: str
    type: TypeType
    archiveRules: Optional[List[InlineArchiveRule]] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    configuration: Optional[AnalyzerConfigurationUnion] = None


class UpdateAnalyzerRequest(BaseValidatorModel):
    analyzerName: str
    configuration: Optional[AnalyzerConfigurationUnion] = None

KmsKeyConfigurationUnion = Union[KmsKeyConfiguration, KmsKeyConfigurationOutput]


class AccessPreview(BaseValidatorModel):
    id: str
    analyzerArn: str
    configurations: Dict[str, ConfigurationOutput]
    createdAt: datetime
    status: AccessPreviewStatusType
    statusReason: Optional[AccessPreviewStatusReason] = None


class S3BucketConfiguration(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[List[S3BucketAclGrantConfiguration]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    accessPoints: Optional[Dict[str, S3AccessPointConfigurationUnion]] = None


class GetAccessPreviewResponse(BaseValidatorModel):
    accessPreview: AccessPreview
    ResponseMetadata: ResponseMetadata

S3BucketConfigurationUnion = Union[S3BucketConfiguration, S3BucketConfigurationOutput]


class Configuration(BaseValidatorModel):
    ebsSnapshot: Optional[EbsSnapshotConfigurationUnion] = None
    ecrRepository: Optional[EcrRepositoryConfiguration] = None
    iamRole: Optional[IamRoleConfiguration] = None
    efsFileSystem: Optional[EfsFileSystemConfiguration] = None
    kmsKey: Optional[KmsKeyConfigurationUnion] = None
    rdsDbClusterSnapshot: Optional[RdsDbClusterSnapshotConfigurationUnion] = None
    rdsDbSnapshot: Optional[RdsDbSnapshotConfigurationUnion] = None
    secretsManagerSecret: Optional[SecretsManagerSecretConfiguration] = None
    s3Bucket: Optional[S3BucketConfigurationUnion] = None
    snsTopic: Optional[SnsTopicConfiguration] = None
    sqsQueue: Optional[SqsQueueConfiguration] = None
    s3ExpressDirectoryBucket: Optional[S3ExpressDirectoryBucketConfiguration] = None
    dynamodbStream: Optional[DynamodbStreamConfiguration] = None
    dynamodbTable: Optional[DynamodbTableConfiguration] = None

ConfigurationUnion = Union[Configuration, ConfigurationOutput]


class CreateAccessPreviewRequest(BaseValidatorModel):
    analyzerArn: str
    configurations: Dict[str, ConfigurationUnion]
    clientToken: Optional[str] = None