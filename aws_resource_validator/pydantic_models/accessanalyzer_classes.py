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
from aws_resource_validator.pydantic_models.accessanalyzer_constants import *

class AccessPreviewStatusReasonTypeDef(BaseValidatorModel):
    code: AccessPreviewStatusReasonCodeType

class AccessTypeDef(BaseValidatorModel):
    actions: Optional[Sequence[str]] = None
    resources: Optional[Sequence[str]] = None

class AclGranteeTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    uri: Optional[str] = None

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

class UnusedAccessConfigurationTypeDef(BaseValidatorModel):
    unusedAccessAge: Optional[int] = None

class StatusReasonTypeDef(BaseValidatorModel):
    code: ReasonCodeType

class ApplyArchiveRuleRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    ruleName: str
    clientToken: Optional[str] = None

class CriterionOutputTypeDef(BaseValidatorModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None

class CancelPolicyGenerationRequestRequestTypeDef(BaseValidatorModel):
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

class CheckNoNewAccessRequestRequestTypeDef(BaseValidatorModel):
    newPolicyDocument: str
    existingPolicyDocument: str
    policyType: AccessCheckPolicyTypeType

class CheckNoPublicAccessRequestRequestTypeDef(BaseValidatorModel):
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

class EbsSnapshotConfigurationTypeDef(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    groups: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None

class CriterionExtraOutputTypeDef(BaseValidatorModel):
    eq: Optional[List[str]] = None
    neq: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    exists: Optional[bool] = None

class CriterionTypeDef(BaseValidatorModel):
    eq: Optional[Sequence[str]] = None
    neq: Optional[Sequence[str]] = None
    contains: Optional[Sequence[str]] = None
    exists: Optional[bool] = None

class DeleteAnalyzerRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    clientToken: Optional[str] = None

class DeleteArchiveRuleRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    clientToken: Optional[str] = None

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

class FindingSummaryV2TypeDef(BaseValidatorModel):
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

class GenerateFindingRecommendationRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    id: str

class GeneratedPolicyTypeDef(BaseValidatorModel):
    policy: str

class GetAccessPreviewRequestRequestTypeDef(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str

class GetAnalyzedResourceRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceArn: str

class GetAnalyzerRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str

class GetArchiveRuleRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    ruleName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetFindingRecommendationRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    id: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RecommendationErrorTypeDef(BaseValidatorModel):
    code: str
    message: str

class GetFindingRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    id: str

class GetFindingV2RequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    id: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetGeneratedPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class ListAccessPreviewsRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAnalyzedResourcesRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAnalyzersRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    type: Optional[TypeType] = None

class ListArchiveRulesRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class ListPolicyGenerationsRequestRequestTypeDef(BaseValidatorModel):
    principalArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PolicyGenerationTypeDef(BaseValidatorModel):
    jobId: str
    principalArn: str
    status: JobStatusType
    startedOn: datetime
    completedOn: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class StartResourceScanRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceArn: str
    resourceOwnerAccount: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UnusedActionTypeDef(BaseValidatorModel):
    action: str
    lastAccessed: Optional[datetime] = None

class UpdateFindingsRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    clientToken: Optional[str] = None

class ValidatePolicyRequestRequestTypeDef(BaseValidatorModel):
    policyDocument: str
    policyType: PolicyTypeType
    locale: Optional[LocaleType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    validatePolicyResourceType: Optional[ValidatePolicyResourceTypeType] = None

class AccessPreviewSummaryTypeDef(BaseValidatorModel):
    id: str
    analyzerArn: str
    createdAt: datetime
    status: AccessPreviewStatusType
    statusReason: Optional[AccessPreviewStatusReasonTypeDef] = None

class CheckAccessNotGrantedRequestRequestTypeDef(BaseValidatorModel):
    policyDocument: str
    access: Sequence[AccessTypeDef]
    policyType: AccessCheckPolicyTypeType

class S3BucketAclGrantConfigurationTypeDef(BaseValidatorModel):
    permission: AclPermissionType
    grantee: AclGranteeTypeDef

class AnalyzerConfigurationTypeDef(BaseValidatorModel):
    unusedAccess: Optional[UnusedAccessConfigurationTypeDef] = None

class ArchiveRuleSummaryTypeDef(BaseValidatorModel):
    ruleName: str
    filter: Dict[str, CriterionOutputTypeDef]
    createdAt: datetime
    updatedAt: datetime

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

class CreateAccessPreviewResponseTypeDef(BaseValidatorModel):
    id: str
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPolicyGenerationResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloudTrailDetailsTypeDef(BaseValidatorModel):
    trails: Sequence[TrailTypeDef]
    accessRole: str
    startTime: TimestampTypeDef
    endTime: Optional[TimestampTypeDef] = None

class CloudTrailPropertiesTypeDef(BaseValidatorModel):
    trailProperties: List[TrailPropertiesTypeDef]
    startTime: datetime
    endTime: datetime

class InlineArchiveRuleTypeDef(BaseValidatorModel):
    ruleName: str
    filter: Mapping[str, CriterionTypeDef]

class FindingSourceTypeDef(BaseValidatorModel):
    type: FindingSourceTypeType
    detail: Optional[FindingSourceDetailTypeDef] = None

class ListFindingsV2ResponseTypeDef(BaseValidatorModel):
    findings: List[FindingSummaryV2TypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingRecommendationRequestGetFindingRecommendationPaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingV2RequestGetFindingV2PaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    resourceType: Optional[ResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalyzersRequestListAnalyzersPaginateTypeDef(BaseValidatorModel):
    type: Optional[TypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchiveRulesRequestListArchiveRulesPaginateTypeDef(BaseValidatorModel):
    analyzerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef(BaseValidatorModel):
    principalArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ValidatePolicyRequestValidatePolicyPaginateTypeDef(BaseValidatorModel):
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

class KmsGrantConfigurationTypeDef(BaseValidatorModel):
    operations: Sequence[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: Optional[str] = None
    constraints: Optional[KmsGrantConstraintsTypeDef] = None

class ListPolicyGenerationsResponseTypeDef(BaseValidatorModel):
    policyGenerations: List[PolicyGenerationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class RdsDbClusterSnapshotConfigurationTypeDef(BaseValidatorModel):
    attributes: Optional[Mapping[str, RdsDbClusterSnapshotAttributeValueTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RdsDbSnapshotConfigurationOutputTypeDef(BaseValidatorModel):
    attributes: Optional[Dict[str, RdsDbSnapshotAttributeValueOutputTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RdsDbSnapshotConfigurationTypeDef(BaseValidatorModel):
    attributes: Optional[Mapping[str, RdsDbSnapshotAttributeValueTypeDef]] = None
    kmsKeyId: Optional[str] = None

class RecommendedStepTypeDef(BaseValidatorModel):
    unusedPermissionsRecommendedStep: Optional[UnusedPermissionsRecommendedStepTypeDef] = None

class UnusedPermissionDetailsTypeDef(BaseValidatorModel):
    serviceNamespace: str
    actions: Optional[List[UnusedActionTypeDef]] = None
    lastAccessed: Optional[datetime] = None

class ListAccessPreviewsResponseTypeDef(BaseValidatorModel):
    accessPreviews: List[AccessPreviewSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AnalyzerSummaryTypeDef(BaseValidatorModel):
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

class GetArchiveRuleResponseTypeDef(BaseValidatorModel):
    archiveRule: ArchiveRuleSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArchiveRulesResponseTypeDef(BaseValidatorModel):
    archiveRules: List[ArchiveRuleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPolicyGenerationRequestRequestTypeDef(BaseValidatorModel):
    policyGenerationDetails: PolicyGenerationDetailsTypeDef
    cloudTrailDetails: Optional[CloudTrailDetailsTypeDef] = None
    clientToken: Optional[str] = None

class GeneratedPolicyPropertiesTypeDef(BaseValidatorModel):
    principalArn: str
    isComplete: Optional[bool] = None
    cloudTrailProperties: Optional[CloudTrailPropertiesTypeDef] = None

class CreateArchiveRuleRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    filter: Mapping[str, CriterionUnionTypeDef]
    clientToken: Optional[str] = None

class ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPreviewFindingsRequestRequestTypeDef(BaseValidatorModel):
    accessPreviewId: str
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    sort: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    sort: Optional[SortCriteriaTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFindingsV2RequestListFindingsV2PaginateTypeDef(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    sort: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsV2RequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    filter: Optional[Mapping[str, CriterionUnionTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortCriteriaTypeDef] = None

class UpdateArchiveRuleRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    ruleName: str
    filter: Mapping[str, CriterionUnionTypeDef]
    clientToken: Optional[str] = None

class CreateAnalyzerRequestRequestTypeDef(BaseValidatorModel):
    analyzerName: str
    type: TypeType
    archiveRules: Optional[Sequence[InlineArchiveRuleTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    configuration: Optional[AnalyzerConfigurationTypeDef] = None

class AccessPreviewFindingTypeDef(BaseValidatorModel):
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

class ExternalAccessDetailsTypeDef(BaseValidatorModel):
    condition: Dict[str, str]
    action: Optional[List[str]] = None
    isPublic: Optional[bool] = None
    principal: Optional[Dict[str, str]] = None
    sources: Optional[List[FindingSourceTypeDef]] = None

class FindingSummaryTypeDef(BaseValidatorModel):
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

class FindingTypeDef(BaseValidatorModel):
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

class KmsKeyConfigurationOutputTypeDef(BaseValidatorModel):
    keyPolicies: Optional[Dict[str, str]] = None
    grants: Optional[List[KmsGrantConfigurationOutputTypeDef]] = None

class KmsKeyConfigurationTypeDef(BaseValidatorModel):
    keyPolicies: Optional[Mapping[str, str]] = None
    grants: Optional[Sequence[KmsGrantConfigurationTypeDef]] = None

class S3AccessPointConfigurationOutputTypeDef(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    networkOrigin: Optional[NetworkOriginConfigurationOutputTypeDef] = None

class S3AccessPointConfigurationTypeDef(BaseValidatorModel):
    accessPointPolicy: Optional[str] = None
    publicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    networkOrigin: Optional[NetworkOriginConfigurationTypeDef] = None

class LocationTypeDef(BaseValidatorModel):
    path: List[PathElementTypeDef]
    span: SpanTypeDef

class GetFindingRecommendationResponseTypeDef(BaseValidatorModel):
    startedAt: datetime
    completedAt: datetime
    nextToken: str
    error: RecommendationErrorTypeDef
    resourceArn: str
    recommendedSteps: List[RecommendedStepTypeDef]
    recommendationType: Literal["UnusedPermissionRecommendation"]
    status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalyzerResponseTypeDef(BaseValidatorModel):
    analyzer: AnalyzerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzersResponseTypeDef(BaseValidatorModel):
    analyzers: List[AnalyzerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GeneratedPolicyResultTypeDef(BaseValidatorModel):
    properties: GeneratedPolicyPropertiesTypeDef
    generatedPolicies: Optional[List[GeneratedPolicyTypeDef]] = None

class ListAccessPreviewFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[AccessPreviewFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FindingDetailsTypeDef(BaseValidatorModel):
    externalAccessDetails: Optional[ExternalAccessDetailsTypeDef] = None
    unusedPermissionDetails: Optional[UnusedPermissionDetailsTypeDef] = None
    unusedIamUserAccessKeyDetails: Optional[UnusedIamUserAccessKeyDetailsTypeDef] = None
    unusedIamRoleDetails: Optional[UnusedIamRoleDetailsTypeDef] = None
    unusedIamUserPasswordDetails: Optional[UnusedIamUserPasswordDetailsTypeDef] = None

class ListFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingResponseTypeDef(BaseValidatorModel):
    finding: FindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class S3BucketConfigurationOutputTypeDef(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[List[S3BucketAclGrantConfigurationTypeDef]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    accessPoints: Optional[Dict[str, S3AccessPointConfigurationOutputTypeDef]] = None

class S3BucketConfigurationTypeDef(BaseValidatorModel):
    bucketPolicy: Optional[str] = None
    bucketAclGrants: Optional[Sequence[S3BucketAclGrantConfigurationTypeDef]] = None
    bucketPublicAccessBlock: Optional[S3PublicAccessBlockConfigurationTypeDef] = None
    accessPoints: Optional[Mapping[str, S3AccessPointConfigurationTypeDef]] = None

class ValidatePolicyFindingTypeDef(BaseValidatorModel):
    findingDetails: str
    findingType: ValidatePolicyFindingTypeType
    issueCode: str
    learnMoreLink: str
    locations: List[LocationTypeDef]

class GetGeneratedPolicyResponseTypeDef(BaseValidatorModel):
    jobDetails: JobDetailsTypeDef
    generatedPolicyResult: GeneratedPolicyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingV2ResponseTypeDef(BaseValidatorModel):
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

class ConfigurationTypeDef(BaseValidatorModel):
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

class ValidatePolicyResponseTypeDef(BaseValidatorModel):
    findings: List[ValidatePolicyFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPreviewTypeDef(BaseValidatorModel):
    id: str
    analyzerArn: str
    configurations: Dict[str, ConfigurationOutputTypeDef]
    createdAt: datetime
    status: AccessPreviewStatusType
    statusReason: Optional[AccessPreviewStatusReasonTypeDef] = None

class GetAccessPreviewResponseTypeDef(BaseValidatorModel):
    accessPreview: AccessPreviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPreviewRequestRequestTypeDef(BaseValidatorModel):
    analyzerArn: str
    configurations: Mapping[str, ConfigurationUnionTypeDef]
    clientToken: Optional[str] = None

