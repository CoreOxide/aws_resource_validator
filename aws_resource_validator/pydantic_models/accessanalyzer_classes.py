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
from aws_resource_validator.pydantic_models.accessanalyzer_constants import *

class AccessPreviewStatusReasonTypeDef(BaseModel):
    code: AccessPreviewStatusReasonCodeType

class AccessTypeDef(BaseModel):
    actions: Optional[Sequence[str]] = None
    resources: Optional[Sequence[str]] = None

class AclGranteeTypeDef(BaseModel):
    id: Optional[str] = None
    uri: Optional[str] = None

class AnalyzedResourceSummaryTypeDef(BaseModel):
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceTypeType

class AnalyzedResourceTypeDef(BaseModel):
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

class UnusedAccessConfigurationTypeDef(BaseModel):
    unusedAccessAge: Optional[int] = None

class StatusReasonTypeDef(BaseModel):
    code: ReasonCodeType

class ApplyArchiveRuleRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    ruleName: str
    clientToken: Optional[str] = None

class CriterionOutputTypeDef(BaseModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None

class CancelPolicyGenerationRequestRequestTypeDef(BaseModel):
    jobId: str

class ReasonSummaryTypeDef(BaseModel):
    description: Optional[str] = None
    statementIndex: Optional[int] = None
    statementId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CheckNoNewAccessRequestRequestTypeDef(BaseModel):
    newPolicyDocument: str
    existingPolicyDocument: str
    policyType: AccessCheckPolicyTypeType

class CheckNoPublicAccessRequestRequestTypeDef(BaseModel):
    policyDocument: str
    resourceType: AccessCheckResourceTypeType

class TrailTypeDef(BaseModel):
    cloudTrailArn: str
    regions: Optional[Sequence[str]] = None
    allRegions: Optional[bool] = None

class TrailPropertiesTypeDef(BaseModel):
    cloudTrailArn: str
    regions: Optional[List[str]] = None
    allRegions: Optional[bool] = None

class DynamodbStreamConfigurationTypeDef(BaseModel):
    streamPolicy: Optional[str] = None

class DynamodbTableConfigurationTypeDef(BaseModel):
    tablePolicy: Optional[str] = None

class EbsSnapshotConfigurationOutputTypeDef(BaseModel):
    userIds: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None

class EcrRepositoryConfigurationTypeDef(BaseModel):
    repositoryPolicy: Optional[str] = None

class EfsFileSystemConfigurationTypeDef(BaseModel):
    fileSystemPolicy: Optional[str] = None

class IamRoleConfigurationTypeDef(BaseModel):
    trustPolicy: Optional[str] = None

class S3ExpressDirectoryBucketConfigurationTypeDef(BaseModel):
    bucketPolicy: Optional[str] = None

class SecretsManagerSecretConfigurationTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None
    secretPolicy: Optional[str] = None

class SnsTopicConfigurationTypeDef(BaseModel):
    topicPolicy: Optional[str] = None

class SqsQueueConfigurationTypeDef(BaseModel):
    queuePolicy: Optional[str] = None

class EbsSnapshotConfigurationTypeDef(BaseModel):
    userIds: Optional[Sequence[str]] = None
    groups: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None

class CriterionExtraOutputTypeDef(BaseModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None

class CriterionTypeDef(BaseModel):
    eq: Optional[Sequence[str]] = None
    neq: Optional[Sequence[str]] = None
    contains: Optional[Sequence[str]] = None
    exists: Optional[bool] = None

class DeleteAnalyzerRequestRequestTypeDef(BaseModel):
    analyzerName: str
    clientToken: Optional[str] = None

class DeleteArchiveRuleRequestRequestTypeDef(BaseModel):
    analyzerName: str
    ruleName: str
    clientToken: Optional[str] = None

class UnusedIamRoleDetailsTypeDef(BaseModel):
    lastAccessed: Optional[datetime] = None

class UnusedIamUserAccessKeyDetailsTypeDef(BaseModel):
    accessKeyId: str
    lastAccessed: Optional[datetime] = None

class UnusedIamUserPasswordDetailsTypeDef(BaseModel):
    lastAccessed: Optional[datetime] = None

class FindingSourceDetailTypeDef(BaseModel):
    accessPointArn: Optional[str] = None
    accessPointAccount: Optional[str] = None

class FindingSummaryV2TypeDef(BaseModel):
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

class GenerateFindingRecommendationRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    id: str

class GeneratedPolicyTypeDef(BaseModel):
    policy: str

class GetAccessPreviewRequestRequestTypeDef(BaseModel):
    accessPreviewId: str
    analyzerArn: str

class GetAnalyzedResourceRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    resourceArn: str

class GetAnalyzerRequestRequestTypeDef(BaseModel):
    analyzerName: str

class GetArchiveRuleRequestRequestTypeDef(BaseModel):
    analyzerName: str
    ruleName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetFindingRecommendationRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    id: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RecommendationErrorTypeDef(BaseModel):
    code: str
    message: str

class GetFindingRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    id: str

class GetFindingV2RequestRequestTypeDef(BaseModel):
    analyzerArn: str
    id: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetGeneratedPolicyRequestRequestTypeDef(BaseModel):
    jobId: str
    includeResourcePlaceholders: Optional[bool] = None
    includeServiceLevelTemplate: Optional[bool] = None

class JobErrorTypeDef(BaseModel):
    code: JobErrorCodeType
    message: str

class KmsGrantConstraintsOutputTypeDef(BaseModel):
    encryptionContextEquals: Optional[Dict[str, str]] = None
    encryptionContextSubset: Optional[Dict[str, str]] = None

class KmsGrantConstraintsTypeDef(BaseModel):
    encryptionContextEquals: Optional[Mapping[str, str]] = None
    encryptionContextSubset: Optional[Mapping[str, str]] = None

class ListAccessPreviewsRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAnalyzedResourcesRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAnalyzersRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    type: Optional[TypeType] = None

class ListArchiveRulesRequestRequestTypeDef(BaseModel):
    analyzerName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SortCriteriaTypeDef(BaseModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class ListPolicyGenerationsRequestRequestTypeDef(BaseModel):
    principalArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PolicyGenerationTypeDef(BaseModel):
    jobId: str
    principalArn: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class VpcConfigurationTypeDef(BaseModel):
    vpcId: str

class SubstringTypeDef(BaseModel):
    start: int
    length: int

class PolicyGenerationDetailsTypeDef(BaseModel):
    principalArn: str

class PositionTypeDef(BaseModel):
    line: int
    column: int
    offset: int

class RdsDbClusterSnapshotAttributeValueOutputTypeDef(BaseModel):
    accountIds: Optional[List[str]] = None

class RdsDbClusterSnapshotAttributeValueTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None

class RdsDbSnapshotAttributeValueOutputTypeDef(BaseModel):
    accountIds: Optional[List[str]] = None

class RdsDbSnapshotAttributeValueTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None

class UnusedPermissionsRecommendedStepTypeDef(BaseModel):
    recommendedAction: RecommendedRemediationActionType
    policyUpdatedAt: Optional[datetime] = None
    recommendedPolicy: Optional[str] = None
    existingPolicyId: Optional[str] = None

class S3PublicAccessBlockConfigurationTypeDef(BaseModel):
    ignorePublicAcls: bool
    restrictPublicBuckets: bool

class StartResourceScanRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    resourceArn: str
    resourceOwnerAccount: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UnusedActionTypeDef(BaseModel):
    action: str
    lastAccessed: Optional[datetime] = None

class UpdateFindingsRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    clientToken: Optional[str] = None

class ValidatePolicyRequestRequestTypeDef(BaseModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None

class AccessPreviewSummaryTypeDef(BaseModel):
    id: str
    analyzerArn: str
    createdAt: datetime
    status: AccessPreviewStatusType
    statusReason: Optional[AccessPreviewStatusReasonTypeDef] = None

class CheckAccessNotGrantedRequestRequestTypeDef(BaseModel):
    policyDocument: str
    access: Sequence[AccessTypeDef]
    policyType: AccessCheckPolicyTypeType

class S3BucketAclGrantConfigurationTypeDef(BaseModel):
    permission: AclPermissionType
    grantee: AclGranteeTypeDef

class AnalyzerConfigurationTypeDef(BaseModel):
    unusedAccess: Optional[UnusedAccessConfigurationTypeDef] = None

class ArchiveRuleSummaryTypeDef(BaseModel):
    ruleName: str
    filter: Dict[str, CriterionOutputTypeDef]
    createdAt: datetime
    updatedAt: datetime

class CheckAccessNotGrantedResponseTypeDef(BaseModel):
    result: CheckAccessNotGrantedResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckNoNewAccessResponseTypeDef(BaseModel):
    result: CheckNoNewAccessResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckNoPublicAccessResponseTypeDef(BaseModel):
    result: CheckNoPublicAccessResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPreviewResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnalyzerResponseTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalyzedResourceResponseTypeDef(BaseModel):
    resource: AnalyzedResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzedResourcesResponseTypeDef(BaseModel):
    analyzedResources: List[AnalyzedResourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPolicyGenerationResponseTypeDef(BaseModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloudTrailDetailsTypeDef(BaseModel):
    trails: Sequence[TrailTypeDef]
    accessRole: str
    startTime: TimestampTypeDef
    endTime: Optional[TimestampTypeDef] = None

class CloudTrailPropertiesTypeDef(BaseModel):
    trailProperties: List[TrailPropertiesTypeDef]
    startTime: datetime
    endTime: datetime

class InlineArchiveRuleTypeDef(BaseModel):
    ruleName: str
    filter: Mapping[str, CriterionTypeDef]

class FindingSourceTypeDef(BaseModel):
    type: FindingSourceTypeType
    detail: Optional[FindingSourceDetailTypeDef] = None

class ListFindingsV2ResponseTypeDef(BaseModel):
    findings: List[FindingSummaryV2TypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingRecommendationRequestGetFindingRecommendationPaginateTypeDef(BaseModel):
    analyzerArn: str
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingV2RequestGetFindingV2PaginateTypeDef(BaseModel):
    analyzerArn: str
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef(BaseModel):
    analyzerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef(BaseModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalyzersRequestListAnalyzersPaginateTypeDef(BaseModel):
    type: Optional[TypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchiveRulesRequestListArchiveRulesPaginateTypeDef(BaseModel):
    analyzerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef(BaseModel):
    principalArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ValidatePolicyRequestValidatePolicyPaginateTypeDef(BaseModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class JobDetailsTypeDef(BaseModel):
    jobId: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None
    jobError: Optional[JobErrorTypeDef] = None

class KmsGrantConfigurationOutputTypeDef(BaseModel):
    operations: List[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsOutputTypeDef] = None

class KmsGrantConfigurationTypeDef(BaseModel):
    operations: Sequence[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsTypeDef] = None

class ListPolicyGenerationsResponseTypeDef(BaseModel):
    policyGenerations: List[PolicyGenerationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkOriginConfigurationOutputTypeDef(BaseModel):
    vpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    internetConfiguration: Optional[Dict[str, Any]] = None

class NetworkOriginConfigurationTypeDef(BaseModel):
    vpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    internetConfiguration: Optional[Mapping[str, Any]] = None

class PathElementTypeDef(BaseModel):
    index: Optional[int] = None
    key: Optional[str] = None
    substring: Optional[SubstringTypeDef] = None
    value: Optional[str] = None

class SpanTypeDef(BaseModel):
    start: PositionTypeDef
    end: PositionTypeDef

class RdsDbClusterSnapshotConfigurationOutputTypeDef(BaseModel):
    attributes: Optional[Dict[str, RdsDbClusterSnapshotAttributeValueOutputTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RdsDbClusterSnapshotConfigurationTypeDef(BaseModel):
    attributes: Optional[Mapping[str, RdsDbClusterSnapshotAttributeValueTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RdsDbSnapshotConfigurationOutputTypeDef(BaseModel):
    attributes: Optional[Dict[str, RdsDbSnapshotAttributeValueOutputTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RdsDbSnapshotConfigurationTypeDef(BaseModel):
    attributes: Optional[Mapping[str, RdsDbSnapshotAttributeValueTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RecommendedStepTypeDef(BaseModel):
    unusedPermissionsRecommendedStep: Optional[UnusedPermissionsRecommendedStepTypeDef] = None

class UnusedPermissionDetailsTypeDef(BaseModel):
    serviceNamespace: str
    actions: Optional[List[UnusedActionTypeDef]] = None
    lastAccessed: Optional[datetime] = None

class ListAccessPreviewsResponseTypeDef(BaseModel):
    accessPreviews: List[AccessPreviewSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AnalyzerSummaryTypeDef(BaseModel):
    arn: str
    name: str
    type: TypeType
    createdAt: datetime
    status: AnalyzerStatusType
    lastResourceAnalyzed: Optional[str] = None
    lastResourceAnalyzedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    statusReason: Optional[StatusReasonTypeDef] = None
    configuration: Optional[AnalyzerConfigurationTypeDef] = None

class GetArchiveRuleResponseTypeDef(BaseModel):
    archiveRule: ArchiveRuleSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArchiveRulesResponseTypeDef(BaseModel):
    archiveRules: List[ArchiveRuleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPolicyGenerationRequestRequestTypeDef(BaseModel):
    policyGenerationDetails: PolicyGenerationDetailsTypeDef
    cloudTrailDetails: Optional[CloudTrailDetailsTypeDef] = None
    clientToken: Optional[str] = None

class GeneratedPolicyPropertiesTypeDef(BaseModel):
    principalArn: str
    isComplete: Optional[bool] = None
    cloudTrailProperties: Optional[CloudTrailPropertiesTypeDef] = None

class CreateArchiveRuleRequestRequestTypeDef(BaseModel):
    analyzerName: str
    ruleName: str
    filter: Mapping[str, CriterionUnionTypeDef]
    clientToken: Optional[str] = None

class ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef(BaseModel):
    accessPreviewId: str
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPreviewFindingsRequestRequestTypeDef(BaseModel):
    accessPreviewId: str
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    sort: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    sort: Optional[SortCriteriaTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFindingsV2RequestListFindingsV2PaginateTypeDef(BaseModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    sort: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsV2RequestRequestTypeDef(BaseModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortCriteriaTypeDef] = None

class UpdateArchiveRuleRequestRequestTypeDef(BaseModel):
    analyzerName: str
    ruleName: str
    filter: Mapping[str, CriterionUnionTypeDef]
    clientToken: Optional[str] = None

class CreateAnalyzerRequestRequestTypeDef(BaseModel):
    analyzerName: str
    type: TypeType
    archiveRules: Optional[Sequence[InlineArchiveRuleTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    configuration: Optional[AnalyzerConfigurationTypeDef] = None

class AccessPreviewFindingTypeDef(BaseModel):
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
    sources: Optional[List[FindingSourceTypeDef]] = None

class ExternalAccessDetailsTypeDef(BaseModel):
    condition: Dict[str, str]
    action: Optional[List[str]] = None
    isPublic: Optional[bool] = None
    principal: Optional[Dict[str, str]] = None
    sources: Optional[List[FindingSourceTypeDef]] = None

class FindingSummaryTypeDef(BaseModel):
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
    sources: Optional[List[FindingSourceTypeDef]] = None

class FindingTypeDef(BaseModel):
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
    sources: Optional[List[FindingSourceTypeDef]] = None

class KmsKeyConfigurationOutputTypeDef(BaseModel):
    keyPolicies: Optional[Dict[str, str]] = None
    grants: Optional[List[KmsGrantConfigurationOutputTypeDef]] = None

class KmsKeyConfigurationTypeDef(BaseModel):
    keyPolicies: Optional[Mapping[str, str]] = None
    grants: Optional[Sequence[KmsGrantConfigurationTypeDef]] = None

class S3AccessPointConfigurationOutputTypeDef(BaseModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    networkOrigin: Optional[NetworkOriginConfigurationOutputTypeDef] = None

class S3AccessPointConfigurationTypeDef(BaseModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    networkOrigin: Optional[NetworkOriginConfigurationTypeDef] = None

class LocationTypeDef(BaseModel):
    path: List[PathElementTypeDef]
    span: SpanTypeDef

class GetFindingRecommendationResponseTypeDef(BaseModel):
    startedAt: datetime
    completedAt: datetime
    nextToken: str
    error: RecommendationErrorTypeDef
    resourceArn: str
    recommendedSteps: List[RecommendedStepTypeDef]
    recommendationType: Literal["UnusedPermissionRecommendation"]
    status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalyzerResponseTypeDef(BaseModel):
    analyzer: AnalyzerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzersResponseTypeDef(BaseModel):
    analyzers: List[AnalyzerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GeneratedPolicyResultTypeDef(BaseModel):
    properties: GeneratedPolicyPropertiesTypeDef
    generatedPolicies: Optional[List[GeneratedPolicyTypeDef]] = None

class ListAccessPreviewFindingsResponseTypeDef(BaseModel):
    findings: List[AccessPreviewFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FindingDetailsTypeDef(BaseModel):
    externalAccessDetails: Optional[ExternalAccessDetailsTypeDef] = None
    unusedPermissionDetails: Optional[UnusedPermissionDetailsTypeDef] = None
    unusedIamUserAccessKeyDetails: Optional[UnusedIamUserAccessKeyDetailsTypeDef] = None
    unusedIamRoleDetails: Optional[UnusedIamRoleDetailsTypeDef] = None
    unusedIamUserPasswordDetails: Optional[UnusedIamUserPasswordDetailsTypeDef] = None

class ListFindingsResponseTypeDef(BaseModel):
    findings: List[FindingSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingResponseTypeDef(BaseModel):
    finding: FindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class S3BucketConfigurationOutputTypeDef(BaseModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[List[S3BucketAclGrantConfigurationTypeDef]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    accessPoints: Optional[Dict[str, S3AccessPointConfigurationOutputTypeDef]] = None

class S3BucketConfigurationTypeDef(BaseModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[Sequence[S3BucketAclGrantConfigurationTypeDef]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    accessPoints: Optional[Mapping[str, S3AccessPointConfigurationTypeDef]] = None

class ValidatePolicyFindingTypeDef(BaseModel):
    findingDetails: str
    findingType: ValidatePolicyFindingTypeType
    issueCode: str
    learnMoreLink: str
    locations: List[LocationTypeDef]

class GetGeneratedPolicyResponseTypeDef(BaseModel):
    jobDetails: JobDetailsTypeDef
    generatedPolicyResult: GeneratedPolicyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingV2ResponseTypeDef(BaseModel):
    analyzedAt: datetime
    createdAt: datetime
    error: str
    id: str
    nextToken: str
    resource: str
    resourceType: ResourceTypeType
    resourceOwnerAccount: str
    status: FindingStatusType
    updatedAt: datetime
    findingDetails: List[FindingDetailsTypeDef]
    findingType: FindingTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationOutputTypeDef(BaseModel):
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

class ConfigurationTypeDef(BaseModel):
    ebsSnapshot: Optional[EbsSnapshotConfigurationTypeDef] = None
    ecrRepository: Optional[EcrRepositoryConfigurationTypeDef] = None
    iamRole: Optional[IamRoleConfigurationTypeDef] = None
    efsFileSystem: Optional[EfsFileSystemConfigurationTypeDef] = None
    kmsKey: Optional[KmsKeyConfigurationTypeDef] = None
    rdsDbClusterSnapshot: Optional[RdsDbClusterSnapshotConfigurationTypeDef] = None
    rdsDbSnapshot: Optional[RdsDbSnapshotConfigurationTypeDef] = None
    secretsManagerSecret: Optional[SecretsManagerSecretConfigurationTypeDef] = None
    s3Bucket: Optional[S3BucketConfigurationTypeDef] = None
    snsTopic: Optional[SnsTopicConfigurationTypeDef] = None
    sqsQueue: Optional[SqsQueueConfigurationTypeDef] = None
    s3ExpressDirectoryBucket: Optional[S3ExpressDirectoryBucketConfigurationTypeDef] = None
    dynamodbStream: Optional[DynamodbStreamConfigurationTypeDef] = None
    dynamodbTable: Optional[DynamodbTableConfigurationTypeDef] = None

class ValidatePolicyResponseTypeDef(BaseModel):
    findings: List[ValidatePolicyFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPreviewTypeDef(BaseModel):
    id: str
    analyzerArn: str
    configurations: Dict[str, ConfigurationOutputTypeDef]
    createdAt: datetime
    status: AccessPreviewStatusType
    statusReason: Optional[AccessPreviewStatusReasonTypeDef] = None

class GetAccessPreviewResponseTypeDef(BaseModel):
    accessPreview: AccessPreviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPreviewRequestRequestTypeDef(BaseModel):
    analyzerArn: str
    configurations: Mapping[str, ConfigurationUnionTypeDef]
    clientToken: Optional[str] = None

