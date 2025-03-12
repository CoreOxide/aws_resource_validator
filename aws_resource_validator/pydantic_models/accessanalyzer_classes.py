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

class AccessPreviewStatusReasonTypeDef(BaseValidatorModel):
    code: AccessPreviewStatusReasonCodeType


class AccessTypeDef(BaseValidatorModel):
    actions: Optional[Sequence[str]] = None
    resources: Optional[Sequence[str]] = None


class AnalysisRuleCriteriaOutputTypeDef(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    resourceTags: Optional[List[Dict[str, str]]] = None


class AnalysisRuleCriteriaTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    resourceTags: Optional[Sequence[Mapping[str, str]]] = None


class AnalyzedResourceSummaryTypeDef(BaseValidatorModel):
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceTypeType


class AnalyzedResourceTypeDef(BaseValidatorModel):
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


class StatusReasonTypeDef(BaseValidatorModel):
    code: ReasonCodeType


class ApplyArchiveRuleRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    ruleName: str
    clientToken: Optional[str] = None


class CriterionOutputTypeDef(BaseValidatorModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None


class CancelPolicyGenerationRequestTypeDef(BaseValidatorModel):
    jobId: str


class ReasonSummaryTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    statementIndex: Optional[int] = None
    statementId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CheckNoNewAccessRequestTypeDef(BaseValidatorModel):
    newPolicyDocument: str
    existingPolicyDocument: str
    policyType: AccessCheckPolicyTypeType


class CheckNoPublicAccessRequestTypeDef(BaseValidatorModel):
    policyDocument: str
    resourceType: AccessCheckResourceTypeType


class TrailTypeDef(BaseValidatorModel):
    cloudTrailArn: str
    regions: Optional[Sequence[str]] = None
    allRegions: Optional[bool] = None


class TrailPropertiesTypeDef(BaseValidatorModel):
    cloudTrailArn: str
    regions: Optional[List[str]] = None
    allRegions: Optional[bool] = None


class DynamodbStreamConfigurationTypeDef(BaseValidatorModel):
    streamPolicy: Optional[str] = None


class DynamodbTableConfigurationTypeDef(BaseValidatorModel):
    tablePolicy: Optional[str] = None


class EbsSnapshotConfigurationOutputTypeDef(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None


class EcrRepositoryConfigurationTypeDef(BaseValidatorModel):
    repositoryPolicy: Optional[str] = None


class EfsFileSystemConfigurationTypeDef(BaseValidatorModel):
    fileSystemPolicy: Optional[str] = None


class IamRoleConfigurationTypeDef(BaseValidatorModel):
    trustPolicy: Optional[str] = None


class S3ExpressDirectoryBucketConfigurationTypeDef(BaseValidatorModel):
    bucketPolicy: Optional[str] = None


class SecretsManagerSecretConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None
    secretPolicy: Optional[str] = None


class SnsTopicConfigurationTypeDef(BaseValidatorModel):
    topicPolicy: Optional[str] = None


class SqsQueueConfigurationTypeDef(BaseValidatorModel):
    queuePolicy: Optional[str] = None


class CriterionTypeDef(BaseValidatorModel):
    eq: Optional[Sequence[str]] = None
    neq: Optional[Sequence[str]] = None
    contains: Optional[Sequence[str]] = None
    exists: Optional[bool] = None


class DeleteAnalyzerRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    clientToken: Optional[str] = None


class DeleteArchiveRuleRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    clientToken: Optional[str] = None


class EbsSnapshotConfigurationTypeDef(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    groups: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None


class ResourceTypeDetailsTypeDef(BaseValidatorModel):
    totalActivePublic: Optional[int] = None
    totalActiveCrossAccount: Optional[int] = None


class FindingAggregationAccountDetailsTypeDef(BaseValidatorModel):
    account: Optional[str] = None
    numberOfActiveFindings: Optional[int] = None
    details: Optional[Dict[str, int]] = None


class UnusedIamRoleDetailsTypeDef(BaseValidatorModel):
    lastAccessed: Optional[datetime] = None


class UnusedIamUserAccessKeyDetailsTypeDef(BaseValidatorModel):
    accessKeyId: str
    lastAccessed: Optional[datetime] = None


class UnusedIamUserPasswordDetailsTypeDef(BaseValidatorModel):
    lastAccessed: Optional[datetime] = None


class FindingSourceDetailTypeDef(BaseValidatorModel):
    accessPointArn: Optional[str] = None
    accessPointAccount: Optional[str] = None


class GeneratedPolicyTypeDef(BaseValidatorModel):
    policy: str


class GetAccessPreviewRequestTypeDef(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str


class GetAnalyzedResourceRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceArn: str


class GetAnalyzerRequestTypeDef(BaseValidatorModel):
    analyzerName: str


class GetArchiveRuleRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    ruleName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class RecommendationErrorTypeDef(BaseValidatorModel):
    code: str
    message: str


class GetFindingsStatisticsRequestTypeDef(BaseValidatorModel):
    analyzerArn: str


class GetGeneratedPolicyRequestTypeDef(BaseValidatorModel):
    jobId: str
    includeResourcePlaceholders: Optional[bool] = None
    includeServiceLevelTemplate: Optional[bool] = None


class JobErrorTypeDef(BaseValidatorModel):
    code: JobErrorCodeType
    message: str


class KmsGrantConstraintsOutputTypeDef(BaseValidatorModel):
    encryptionContextEquals: Optional[Dict[str, str]] = None
    encryptionContextSubset: Optional[Dict[str, str]] = None


class KmsGrantConstraintsTypeDef(BaseValidatorModel):
    encryptionContextEquals: Optional[Mapping[str, str]] = None
    encryptionContextSubset: Optional[Mapping[str, str]] = None


class ListAccessPreviewsRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAnalyzedResourcesRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListArchiveRulesRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class ListPolicyGenerationsRequestTypeDef(BaseValidatorModel):
    principalArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PolicyGenerationTypeDef(BaseValidatorModel):
    jobId: str
    principalArn: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class VpcConfigurationTypeDef(BaseValidatorModel):
    vpcId: str


class SubstringTypeDef(BaseValidatorModel):
    start: int
    length: int


class PolicyGenerationDetailsTypeDef(BaseValidatorModel):
    principalArn: str


class PositionTypeDef(BaseValidatorModel):
    line: int
    column: int
    offset: int


class RdsDbClusterSnapshotAttributeValueOutputTypeDef(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class RdsDbClusterSnapshotAttributeValueTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None


class RdsDbSnapshotAttributeValueOutputTypeDef(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class RdsDbSnapshotAttributeValueTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None


class UnusedPermissionsRecommendedStepTypeDef(BaseValidatorModel):
    recommendedAction: RecommendedRemediationActionType
    policyUpdatedAt: Optional[datetime] = None
    recommendedPolicy: Optional[str] = None
    existingPolicyId: Optional[str] = None


class S3PublicAccessBlockConfigurationTypeDef(BaseValidatorModel):
    ignorePublicAcls: bool
    restrictPublicBuckets: bool


class StartResourceScanRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceArn: str
    resourceOwnerAccount: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UnusedAccessTypeStatisticsTypeDef(BaseValidatorModel):
    unusedAccessType: Optional[str] = None
    total: Optional[int] = None


class UnusedActionTypeDef(BaseValidatorModel):
    action: str
    lastAccessed: Optional[datetime] = None


class UpdateFindingsRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    clientToken: Optional[str] = None


class ValidatePolicyRequestTypeDef(BaseValidatorModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None


class CheckAccessNotGrantedRequestTypeDef(BaseValidatorModel):
    policyDocument: str
    access: Sequence[AccessTypeDef]
    policyType: AccessCheckPolicyTypeType


class AclGranteeTypeDef(BaseValidatorModel):
    pass


class S3BucketAclGrantConfigurationTypeDef(BaseValidatorModel):
    permission: AclPermissionType
    grantee: AclGranteeTypeDef


class AnalysisRuleOutputTypeDef(BaseValidatorModel):
    exclusions: Optional[List[AnalysisRuleCriteriaOutputTypeDef]] = None


class AnalysisRuleTypeDef(BaseValidatorModel):
    exclusions: Optional[Sequence[AnalysisRuleCriteriaTypeDef]] = None


class CheckAccessNotGrantedResponseTypeDef(BaseValidatorModel):
    result: CheckAccessNotGrantedResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CheckNoNewAccessResponseTypeDef(BaseValidatorModel):
    result: CheckNoNewAccessResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CheckNoPublicAccessResponseTypeDef(BaseValidatorModel):
    result: CheckNoPublicAccessResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAnalyzerResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAnalyzedResourceResponseTypeDef(BaseValidatorModel):
    resource: AnalyzedResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAnalyzedResourcesResponseTypeDef(BaseValidatorModel):
    analyzedResources: List[AnalyzedResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartPolicyGenerationResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class CloudTrailDetailsTypeDef(BaseValidatorModel):
    trails: Sequence[TrailTypeDef]
    accessRole: str
    startTime: TimestampTypeDef
    endTime: Optional[TimestampTypeDef] = None


class CloudTrailPropertiesTypeDef(BaseValidatorModel):
    trailProperties: List[TrailPropertiesTypeDef]
    startTime: datetime
    endTime: datetime


class ExternalAccessFindingsStatisticsTypeDef(BaseValidatorModel):
    resourceTypeStatistics: Optional[Dict[ResourceTypeType, ResourceTypeDetailsTypeDef]] = None
    totalActiveFindings: Optional[int] = None
    totalArchivedFindings: Optional[int] = None
    totalResolvedFindings: Optional[int] = None


class FindingSummaryV2TypeDef(BaseValidatorModel):
    pass


class ListFindingsV2ResponseTypeDef(BaseValidatorModel):
    findings: List[FindingSummaryV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAccessPreviewsRequestPaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAnalyzedResourcesRequestPaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListArchiveRulesRequestPaginateTypeDef(BaseValidatorModel):
    analyzerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyGenerationsRequestPaginateTypeDef(BaseValidatorModel):
    principalArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ValidatePolicyRequestPaginateTypeDef(BaseValidatorModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class JobDetailsTypeDef(BaseValidatorModel):
    jobId: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None
    jobError: Optional[JobErrorTypeDef] = None


class KmsGrantConfigurationOutputTypeDef(BaseValidatorModel):
    operations: List[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsOutputTypeDef] = None


class ListPolicyGenerationsResponseTypeDef(BaseValidatorModel):
    policyGenerations: List[PolicyGenerationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NetworkOriginConfigurationOutputTypeDef(BaseValidatorModel):
    vpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    internetConfiguration: Optional[Dict[str, Any]] = None


class NetworkOriginConfigurationTypeDef(BaseValidatorModel):
    vpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    internetConfiguration: Optional[Mapping[str, Any]] = None


class PathElementTypeDef(BaseValidatorModel):
    index: Optional[int] = None
    key: Optional[str] = None
    substring: Optional[SubstringTypeDef] = None
    value: Optional[str] = None


class SpanTypeDef(BaseValidatorModel):
    start: PositionTypeDef
    end: PositionTypeDef


class RdsDbClusterSnapshotConfigurationOutputTypeDef(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbClusterSnapshotAttributeValueOutputTypeDef]] = None
    kmsKeyId: Optional[str] = None


class RdsDbSnapshotConfigurationOutputTypeDef(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbSnapshotAttributeValueOutputTypeDef]] = None
    kmsKeyId: Optional[str] = None


class RecommendedStepTypeDef(BaseValidatorModel):
    unusedPermissionsRecommendedStep: Optional[UnusedPermissionsRecommendedStepTypeDef] = None


class UnusedAccessFindingsStatisticsTypeDef(BaseValidatorModel):
    unusedAccessTypeStatistics: Optional[List[UnusedAccessTypeStatisticsTypeDef]] = None
    topAccounts: Optional[List[FindingAggregationAccountDetailsTypeDef]] = None
    totalActiveFindings: Optional[int] = None
    totalArchivedFindings: Optional[int] = None
    totalResolvedFindings: Optional[int] = None


class UnusedPermissionDetailsTypeDef(BaseValidatorModel):
    serviceNamespace: str
    actions: Optional[List[UnusedActionTypeDef]] = None
    lastAccessed: Optional[datetime] = None


class AccessPreviewSummaryTypeDef(BaseValidatorModel):
    pass


class ListAccessPreviewsResponseTypeDef(BaseValidatorModel):
    accessPreviews: List[AccessPreviewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UnusedAccessConfigurationOutputTypeDef(BaseValidatorModel):
    unusedAccessAge: Optional[int] = None
    analysisRule: Optional[AnalysisRuleOutputTypeDef] = None


class UnusedAccessConfigurationTypeDef(BaseValidatorModel):
    unusedAccessAge: Optional[int] = None
    analysisRule: Optional[AnalysisRuleTypeDef] = None


class ArchiveRuleSummaryTypeDef(BaseValidatorModel):
    pass


class GetArchiveRuleResponseTypeDef(BaseValidatorModel):
    archiveRule: ArchiveRuleSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListArchiveRulesResponseTypeDef(BaseValidatorModel):
    archiveRules: List[ArchiveRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartPolicyGenerationRequestTypeDef(BaseValidatorModel):
    policyGenerationDetails: PolicyGenerationDetailsTypeDef
    cloudTrailDetails: Optional[CloudTrailDetailsTypeDef] = None
    clientToken: Optional[str] = None


class GeneratedPolicyPropertiesTypeDef(BaseValidatorModel):
    principalArn: str
    isComplete: Optional[bool] = None
    cloudTrailProperties: Optional[CloudTrailPropertiesTypeDef] = None


class FindingSourceTypeDef(BaseValidatorModel):
    pass


class ExternalAccessDetailsTypeDef(BaseValidatorModel):
    condition: Dict[str, str]
    action: Optional[List[str]] = None
    isPublic: Optional[bool] = None
    principal: Optional[Dict[str, str]] = None
    sources: Optional[List[FindingSourceTypeDef]] = None
    resourceControlPolicyRestriction: Optional[ResourceControlPolicyRestrictionType] = None


class KmsKeyConfigurationOutputTypeDef(BaseValidatorModel):
    keyPolicies: Optional[Dict[str, str]] = None
    grants: Optional[List[KmsGrantConfigurationOutputTypeDef]] = None


class KmsGrantConstraintsUnionTypeDef(BaseValidatorModel):
    pass


class KmsGrantConfigurationTypeDef(BaseValidatorModel):
    operations: Sequence[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsUnionTypeDef] = None


class S3AccessPointConfigurationOutputTypeDef(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    networkOrigin: Optional[NetworkOriginConfigurationOutputTypeDef] = None


class LocationTypeDef(BaseValidatorModel):
    path: List[PathElementTypeDef]
    span: SpanTypeDef


class RdsDbClusterSnapshotAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class RdsDbClusterSnapshotConfigurationTypeDef(BaseValidatorModel):
    attributes: Optional[Mapping[str, RdsDbClusterSnapshotAttributeValueUnionTypeDef]] = None
    kmsKeyId: Optional[str] = None


class RdsDbSnapshotAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class RdsDbSnapshotConfigurationTypeDef(BaseValidatorModel):
    attributes: Optional[Mapping[str, RdsDbSnapshotAttributeValueUnionTypeDef]] = None
    kmsKeyId: Optional[str] = None


class GetFindingRecommendationResponseTypeDef(BaseValidatorModel):
    startedAt: datetime
    completedAt: datetime
    error: RecommendationErrorTypeDef
    resourceArn: str
    recommendedSteps: List[RecommendedStepTypeDef]
    recommendationType: Literal["UnusedPermissionRecommendation"]
    status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FindingsStatisticsTypeDef(BaseValidatorModel):
    externalAccessFindingsStatistics: Optional[ExternalAccessFindingsStatisticsTypeDef] = None
    unusedAccessFindingsStatistics: Optional[UnusedAccessFindingsStatisticsTypeDef] = None


class AnalyzerConfigurationOutputTypeDef(BaseValidatorModel):
    unusedAccess: Optional[UnusedAccessConfigurationOutputTypeDef] = None


class AnalyzerConfigurationTypeDef(BaseValidatorModel):
    unusedAccess: Optional[UnusedAccessConfigurationTypeDef] = None


class GeneratedPolicyResultTypeDef(BaseValidatorModel):
    properties: GeneratedPolicyPropertiesTypeDef
    generatedPolicies: Optional[List[GeneratedPolicyTypeDef]] = None


class AccessPreviewFindingTypeDef(BaseValidatorModel):
    pass


class ListAccessPreviewFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[AccessPreviewFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FindingDetailsTypeDef(BaseValidatorModel):
    externalAccessDetails: Optional[ExternalAccessDetailsTypeDef] = None
    unusedPermissionDetails: Optional[UnusedPermissionDetailsTypeDef] = None
    unusedIamUserAccessKeyDetails: Optional[UnusedIamUserAccessKeyDetailsTypeDef] = None
    unusedIamRoleDetails: Optional[UnusedIamRoleDetailsTypeDef] = None
    unusedIamUserPasswordDetails: Optional[UnusedIamUserPasswordDetailsTypeDef] = None


class FindingSummaryTypeDef(BaseValidatorModel):
    pass


class ListFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FindingTypeDef(BaseValidatorModel):
    pass


class GetFindingResponseTypeDef(BaseValidatorModel):
    finding: FindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class S3BucketConfigurationOutputTypeDef(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[List[S3BucketAclGrantConfigurationTypeDef]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    accessPoints: Optional[Dict[str, S3AccessPointConfigurationOutputTypeDef]] = None


class NetworkOriginConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class S3AccessPointConfigurationTypeDef(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    networkOrigin: Optional[NetworkOriginConfigurationUnionTypeDef] = None


class ValidatePolicyFindingTypeDef(BaseValidatorModel):
    findingDetails: str
    findingType: ValidatePolicyFindingTypeType
    issueCode: str
    learnMoreLink: str
    locations: List[LocationTypeDef]


class GetFindingsStatisticsResponseTypeDef(BaseValidatorModel):
    findingsStatistics: List[FindingsStatisticsTypeDef]
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAnalyzerResponseTypeDef(BaseValidatorModel):
    configuration: AnalyzerConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetGeneratedPolicyResponseTypeDef(BaseValidatorModel):
    jobDetails: JobDetailsTypeDef
    generatedPolicyResult: GeneratedPolicyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class KmsGrantConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class KmsKeyConfigurationTypeDef(BaseValidatorModel):
    keyPolicies: Optional[Mapping[str, str]] = None
    grants: Optional[Sequence[KmsGrantConfigurationUnionTypeDef]] = None


class ConfigurationOutputTypeDef(BaseValidatorModel):
    ebsSnapshot: Optional[EbsSnapshotConfigurationOutputTypeDef] = None
    ecrRepository: Optional[EcrRepositoryConfigurationTypeDef] = None
    iamRole: Optional[IamRoleConfigurationTypeDef] = None
    efsFileSystem: Optional[EfsFileSystemConfigurationTypeDef] = None
    kmsKey: Optional[KmsKeyConfigurationOutputTypeDef] = None
    rdsDbClusterSnapshot: Optional[RdsDbClusterSnapshotConfigurationOutputTypeDef] = None
    rdsDbSnapshot: Optional[RdsDbSnapshotConfigurationOutputTypeDef] = None
    secretsManagerSecret: Optional[SecretsManagerSecretConfigurationTypeDef] = None
    s3Bucket: Optional[S3BucketConfigurationOutputTypeDef] = None
    snsTopic: Optional[SnsTopicConfigurationTypeDef] = None
    sqsQueue: Optional[SqsQueueConfigurationTypeDef] = None
    s3ExpressDirectoryBucket: Optional[S3ExpressDirectoryBucketConfigurationTypeDef] = None
    dynamodbStream: Optional[DynamodbStreamConfigurationTypeDef] = None
    dynamodbTable: Optional[DynamodbTableConfigurationTypeDef] = None


class ValidatePolicyResponseTypeDef(BaseValidatorModel):
    findings: List[ValidatePolicyFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AnalyzerSummaryTypeDef(BaseValidatorModel):
    pass


class GetAnalyzerResponseTypeDef(BaseValidatorModel):
    analyzer: AnalyzerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAnalyzersResponseTypeDef(BaseValidatorModel):
    analyzers: List[AnalyzerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AnalyzerConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateAnalyzerRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    configuration: Optional[AnalyzerConfigurationUnionTypeDef] = None


class S3AccessPointConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class S3BucketConfigurationTypeDef(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[Sequence[S3BucketAclGrantConfigurationTypeDef]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    accessPoints: Optional[Mapping[str, S3AccessPointConfigurationUnionTypeDef]] = None


class AccessPreviewTypeDef(BaseValidatorModel):
    pass


class GetAccessPreviewResponseTypeDef(BaseValidatorModel):
    accessPreview: AccessPreviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EbsSnapshotConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class S3BucketConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class RdsDbClusterSnapshotConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class RdsDbSnapshotConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class KmsKeyConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ConfigurationTypeDef(BaseValidatorModel):
    ebsSnapshot: Optional[EbsSnapshotConfigurationUnionTypeDef] = None
    ecrRepository: Optional[EcrRepositoryConfigurationTypeDef] = None
    iamRole: Optional[IamRoleConfigurationTypeDef] = None
    efsFileSystem: Optional[EfsFileSystemConfigurationTypeDef] = None
    kmsKey: Optional[KmsKeyConfigurationUnionTypeDef] = None
    rdsDbClusterSnapshot: Optional[RdsDbClusterSnapshotConfigurationUnionTypeDef] = None
    rdsDbSnapshot: Optional[RdsDbSnapshotConfigurationUnionTypeDef] = None
    secretsManagerSecret: Optional[SecretsManagerSecretConfigurationTypeDef] = None
    s3Bucket: Optional[S3BucketConfigurationUnionTypeDef] = None
    snsTopic: Optional[SnsTopicConfigurationTypeDef] = None
    sqsQueue: Optional[SqsQueueConfigurationTypeDef] = None
    s3ExpressDirectoryBucket: Optional[S3ExpressDirectoryBucketConfigurationTypeDef] = None
    dynamodbStream: Optional[DynamodbStreamConfigurationTypeDef] = None
    dynamodbTable: Optional[DynamodbTableConfigurationTypeDef] = None


class ConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAccessPreviewRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    configurations: Mapping[str, ConfigurationUnionTypeDef]
    clientToken: Optional[str] = None


