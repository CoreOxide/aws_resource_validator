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
from aws_resource_validator.pydantic_models.accessanalyzer_constants import *

class AccessPreviewStatusReason(BaseValidatorModel):
    code: AccessPreviewStatusReasonCodeType


class Access(BaseValidatorModel):
    actions: Optional[Sequence[str]] = None
    resources: Optional[Sequence[str]] = None


class AnalysisRuleCriteriaOutput(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    resourceTags: Optional[List[Dict[str, str]]] = None


class AnalysisRuleCriteria(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    resourceTags: Optional[Sequence[Mapping[str, str]]] = None


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


class Trail(BaseValidatorModel):
    cloudTrailArn: str
    regions: Optional[Sequence[str]] = None
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
    eq: Optional[Sequence[str]] = None
    neq: Optional[Sequence[str]] = None
    contains: Optional[Sequence[str]] = None
    exists: Optional[bool] = None


class DeleteAnalyzerRequest(BaseValidatorModel):
    analyzerName: str
    clientToken: Optional[str] = None


class DeleteArchiveRuleRequest(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    clientToken: Optional[str] = None


class EbsSnapshotConfiguration(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    groups: Optional[Sequence[str]] = None
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


class RecommendationError(BaseValidatorModel):
    code: str
    message: str


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
    encryptionContextEquals: Optional[Mapping[str, str]] = None
    encryptionContextSubset: Optional[Mapping[str, str]] = None


class ListAccessPreviewsRequest(BaseValidatorModel):
    analyzerArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAnalyzedResourcesRequest(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


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
    accountIds: Optional[Sequence[str]] = None


class RdsDbSnapshotAttributeValueOutput(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class RdsDbSnapshotAttributeValue(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None


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
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UnusedAccessTypeStatistics(BaseValidatorModel):
    unusedAccessType: Optional[str] = None
    total: Optional[int] = None


class UnusedAction(BaseValidatorModel):
    action: str
    lastAccessed: Optional[datetime] = None


class UpdateFindingsRequest(BaseValidatorModel):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    clientToken: Optional[str] = None


class ValidatePolicyRequest(BaseValidatorModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None


class CheckAccessNotGrantedRequest(BaseValidatorModel):
    policyDocument: str
    access: Sequence[Access]
    policyType: AccessCheckPolicyTypeType


class AclGrantee(BaseValidatorModel):
    pass


class S3BucketAclGrantConfiguration(BaseValidatorModel):
    permission: AclPermissionType
    grantee: AclGrantee


class AnalysisRuleOutput(BaseValidatorModel):
    exclusions: Optional[List[AnalysisRuleCriteriaOutput]] = None


class AnalysisRule(BaseValidatorModel):
    exclusions: Optional[Sequence[AnalysisRuleCriteria]] = None


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


class Timestamp(BaseValidatorModel):
    pass


class CloudTrailDetails(BaseValidatorModel):
    trails: Sequence[Trail]
    accessRole: str
    startTime: Timestamp
    endTime: Optional[Timestamp] = None


class CloudTrailProperties(BaseValidatorModel):
    trailProperties: List[TrailProperties]
    startTime: datetime
    endTime: datetime


class ExternalAccessFindingsStatistics(BaseValidatorModel):
    resourceTypeStatistics: Optional[Dict[ResourceTypeType, ResourceTypeDetails]] = None
    totalActiveFindings: Optional[int] = None
    totalArchivedFindings: Optional[int] = None
    totalResolvedFindings: Optional[int] = None


class FindingSummaryV2(BaseValidatorModel):
    pass


class ListFindingsV2Response(BaseValidatorModel):
    findings: List[FindingSummaryV2]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAccessPreviewsRequestPaginate(BaseValidatorModel):
    analyzerArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnalyzedResourcesRequestPaginate(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
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


class ListPolicyGenerationsResponse(BaseValidatorModel):
    policyGenerations: List[PolicyGeneration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NetworkOriginConfigurationOutput(BaseValidatorModel):
    vpcConfiguration: Optional[VpcConfiguration] = None
    internetConfiguration: Optional[Dict[str, Any]] = None


class NetworkOriginConfiguration(BaseValidatorModel):
    vpcConfiguration: Optional[VpcConfiguration] = None
    internetConfiguration: Optional[Mapping[str, Any]] = None


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


class RdsDbSnapshotConfigurationOutput(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbSnapshotAttributeValueOutput]] = None
    kmsKeyId: Optional[str] = None


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


class AccessPreviewSummary(BaseValidatorModel):
    pass


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


class ArchiveRuleSummary(BaseValidatorModel):
    pass


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


class FindingSource(BaseValidatorModel):
    pass


class ExternalAccessDetails(BaseValidatorModel):
    condition: Dict[str, str]
    action: Optional[List[str]] = None
    isPublic: Optional[bool] = None
    principal: Optional[Dict[str, str]] = None
    sources: Optional[List[FindingSource]] = None
    resourceControlPolicyRestriction: Optional[ResourceControlPolicyRestrictionType] = None


class KmsKeyConfigurationOutput(BaseValidatorModel):
    keyPolicies: Optional[Dict[str, str]] = None
    grants: Optional[List[KmsGrantConfigurationOutput]] = None


class KmsGrantConstraintsUnion(BaseValidatorModel):
    pass


class KmsGrantConfiguration(BaseValidatorModel):
    operations: Sequence[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsUnion] = None


class S3AccessPointConfigurationOutput(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    networkOrigin: Optional[NetworkOriginConfigurationOutput] = None


class Location(BaseValidatorModel):
    path: List[PathElement]
    span: Span


class RdsDbClusterSnapshotAttributeValueUnion(BaseValidatorModel):
    pass


class RdsDbClusterSnapshotConfiguration(BaseValidatorModel):
    attributes: Optional[Mapping[str, RdsDbClusterSnapshotAttributeValueUnion]] = None
    kmsKeyId: Optional[str] = None


class RdsDbSnapshotAttributeValueUnion(BaseValidatorModel):
    pass


class RdsDbSnapshotConfiguration(BaseValidatorModel):
    attributes: Optional[Mapping[str, RdsDbSnapshotAttributeValueUnion]] = None
    kmsKeyId: Optional[str] = None


class GetFindingRecommendationResponse(BaseValidatorModel):
    startedAt: datetime
    completedAt: datetime
    error: RecommendationError
    resourceArn: str
    recommendedSteps: List[RecommendedStep]
    recommendationType: Literal["UnusedPermissionRecommendation"]
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


class AccessPreviewFinding(BaseValidatorModel):
    pass


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


class FindingSummary(BaseValidatorModel):
    pass


class ListFindingsResponse(BaseValidatorModel):
    findings: List[FindingSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Finding(BaseValidatorModel):
    pass


class GetFindingResponse(BaseValidatorModel):
    finding: Finding
    ResponseMetadata: ResponseMetadata


class S3BucketConfigurationOutput(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[List[S3BucketAclGrantConfiguration]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    accessPoints: Optional[Dict[str, S3AccessPointConfigurationOutput]] = None


class NetworkOriginConfigurationUnion(BaseValidatorModel):
    pass


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


class GetFindingsStatisticsResponse(BaseValidatorModel):
    findingsStatistics: List[FindingsStatistics]
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateAnalyzerResponse(BaseValidatorModel):
    configuration: AnalyzerConfigurationOutput
    ResponseMetadata: ResponseMetadata


class GetGeneratedPolicyResponse(BaseValidatorModel):
    jobDetails: JobDetails
    generatedPolicyResult: GeneratedPolicyResult
    ResponseMetadata: ResponseMetadata


class KmsGrantConfigurationUnion(BaseValidatorModel):
    pass


class KmsKeyConfiguration(BaseValidatorModel):
    keyPolicies: Optional[Mapping[str, str]] = None
    grants: Optional[Sequence[KmsGrantConfigurationUnion]] = None


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


class ValidatePolicyResponse(BaseValidatorModel):
    findings: List[ValidatePolicyFinding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AnalyzerSummary(BaseValidatorModel):
    pass


class GetAnalyzerResponse(BaseValidatorModel):
    analyzer: AnalyzerSummary
    ResponseMetadata: ResponseMetadata


class ListAnalyzersResponse(BaseValidatorModel):
    analyzers: List[AnalyzerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AnalyzerConfigurationUnion(BaseValidatorModel):
    pass


class UpdateAnalyzerRequest(BaseValidatorModel):
    analyzerName: str
    configuration: Optional[AnalyzerConfigurationUnion] = None


class S3AccessPointConfigurationUnion(BaseValidatorModel):
    pass


class S3BucketConfiguration(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[Sequence[S3BucketAclGrantConfiguration]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfiguration] = None
    accessPoints: Optional[Mapping[str, S3AccessPointConfigurationUnion]] = None


class AccessPreview(BaseValidatorModel):
    pass


class GetAccessPreviewResponse(BaseValidatorModel):
    accessPreview: AccessPreview
    ResponseMetadata: ResponseMetadata


class EbsSnapshotConfigurationUnion(BaseValidatorModel):
    pass


class S3BucketConfigurationUnion(BaseValidatorModel):
    pass


class RdsDbClusterSnapshotConfigurationUnion(BaseValidatorModel):
    pass


class RdsDbSnapshotConfigurationUnion(BaseValidatorModel):
    pass


class KmsKeyConfigurationUnion(BaseValidatorModel):
    pass


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


class ConfigurationUnion(BaseValidatorModel):
    pass


class CreateAccessPreviewRequest(BaseValidatorModel):
    analyzerArn: str
    configurations: Mapping[str, ConfigurationUnion]
    clientToken: Optional[str] = None


