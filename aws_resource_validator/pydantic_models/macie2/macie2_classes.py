from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.macie2.macie2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptInvitationRequest(BaseValidatorModel):
    invitationId: str
    administratorAccountId: Optional[str] = None
    masterAccount: Optional[str] = None


class AccessControlList(BaseValidatorModel):
    allowsPublicReadAccess: Optional[bool] = None
    allowsPublicWriteAccess: Optional[bool] = None


class AccountDetail(BaseValidatorModel):
    accountId: str
    email: str


class BlockPublicAccess(BaseValidatorModel):
    blockPublicAcls: Optional[bool] = None
    blockPublicPolicy: Optional[bool] = None
    ignorePublicAcls: Optional[bool] = None
    restrictPublicBuckets: Optional[bool] = None


class AdminAccount(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[AdminStatusType] = None


class S3WordsList(BaseValidatorModel):
    bucketName: str
    objectKey: str


class AllowListStatus(BaseValidatorModel):
    code: AllowListStatusCodeType
    description: Optional[str] = None


class AllowListSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None


class ApiCallDetails(BaseValidatorModel):
    api: Optional[str] = None
    apiServiceName: Optional[str] = None
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None


class AutomatedDiscoveryAccount(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[AutomatedDiscoveryAccountStatusType] = None


class AutomatedDiscoveryAccountUpdateError(BaseValidatorModel):
    accountId: Optional[str] = None
    errorCode: Optional[AutomatedDiscoveryAccountUpdateErrorCodeType] = None


class AutomatedDiscoveryAccountUpdate(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[AutomatedDiscoveryAccountStatusType] = None


class AwsAccount(BaseValidatorModel):
    accountId: Optional[str] = None
    principalId: Optional[str] = None


class AwsService(BaseValidatorModel):
    invokedBy: Optional[str] = None


class BatchGetCustomDataIdentifierSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    deleted: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None


class BatchGetCustomDataIdentifiersRequest(BaseValidatorModel):
    ids: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BucketCountByEffectivePermission(BaseValidatorModel):
    publiclyAccessible: Optional[int] = None
    publiclyReadable: Optional[int] = None
    publiclyWritable: Optional[int] = None
    unknown: Optional[int] = None


class BucketCountByEncryptionType(BaseValidatorModel):
    kmsManaged: Optional[int] = None
    s3Managed: Optional[int] = None
    unencrypted: Optional[int] = None
    unknown: Optional[int] = None


class BucketCountBySharedAccessType(BaseValidatorModel):
    external: Optional[int] = None
    internal: Optional[int] = None
    notShared: Optional[int] = None
    unknown: Optional[int] = None


class BucketCountPolicyAllowsUnencryptedObjectUploads(BaseValidatorModel):
    allowsUnencryptedObjectUploads: Optional[int] = None
    deniesUnencryptedObjectUploads: Optional[int] = None
    unknown: Optional[int] = None


class BucketCriteriaAdditionalProperties(BaseValidatorModel):
    eq: Optional[List[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[List[str]] = None
    prefix: Optional[str] = None


class BucketPolicy(BaseValidatorModel):
    allowsPublicReadAccess: Optional[bool] = None
    allowsPublicWriteAccess: Optional[bool] = None


class BucketServerSideEncryption(BaseValidatorModel):
    kmsMasterKeyId: Optional[str] = None
    type: Optional[TypeType] = None


class JobDetails(BaseValidatorModel):
    isDefinedInJob: Optional[IsDefinedInJobType] = None
    isMonitoredByJob: Optional[IsMonitoredByJobType] = None
    lastJobId: Optional[str] = None
    lastJobRunTime: Optional[datetime] = None


class KeyValuePair(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ObjectCountByEncryptionType(BaseValidatorModel):
    customerManaged: Optional[int] = None
    kmsManaged: Optional[int] = None
    s3Managed: Optional[int] = None
    unencrypted: Optional[int] = None
    unknown: Optional[int] = None


class ObjectLevelStatistics(BaseValidatorModel):
    fileType: Optional[int] = None
    storageClass: Optional[int] = None
    total: Optional[int] = None


class ReplicationDetails(BaseValidatorModel):
    replicated: Optional[bool] = None
    replicatedExternally: Optional[bool] = None
    replicationAccounts: Optional[List[str]] = None


class BucketSortCriteria(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class SensitivityAggregations(BaseValidatorModel):
    classifiableSizeInBytes: Optional[int] = None
    publiclyAccessibleCount: Optional[int] = None
    totalCount: Optional[int] = None
    totalSizeInBytes: Optional[int] = None


class Cell(BaseValidatorModel):
    cellReference: Optional[str] = None
    column: Optional[int] = None
    columnName: Optional[str] = None
    row: Optional[int] = None


class S3Destination(BaseValidatorModel):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: Optional[str] = None


class ClassificationResultStatus(BaseValidatorModel):
    code: Optional[str] = None
    reason: Optional[str] = None


class ClassificationScopeSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class SeverityLevel(BaseValidatorModel):
    occurrencesThreshold: int
    severity: DataIdentifierSeverityType


class CreateInvitationsRequest(BaseValidatorModel):
    accountIds: List[str]
    disableEmailNotification: Optional[bool] = None
    message: Optional[str] = None


class UnprocessedAccount(BaseValidatorModel):
    accountId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None


class CreateSampleFindingsRequest(BaseValidatorModel):
    findingTypes: Optional[List[FindingTypeType]] = None


class SimpleCriterionForJobOutput(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[SimpleCriterionKeyForJobType] = None
    values: Optional[List[str]] = None


class SimpleCriterionForJob(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[SimpleCriterionKeyForJobType] = None
    values: Optional[List[str]] = None


class CriterionAdditionalPropertiesOutput(BaseValidatorModel):
    eq: Optional[List[str]] = None
    eqExactMatch: Optional[List[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[List[str]] = None


class CriterionAdditionalProperties(BaseValidatorModel):
    eq: Optional[List[str]] = None
    eqExactMatch: Optional[List[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[List[str]] = None


class CustomDataIdentifierSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None


class DeclineInvitationsRequest(BaseValidatorModel):
    accountIds: List[str]


class DeleteAllowListRequest(BaseValidatorModel):
    id: str
    ignoreJobChecks: Optional[str] = None


class DeleteCustomDataIdentifierRequest(BaseValidatorModel):
    id: str


class DeleteFindingsFilterRequest(BaseValidatorModel):
    id: str


class DeleteInvitationsRequest(BaseValidatorModel):
    accountIds: List[str]


class DeleteMemberRequest(BaseValidatorModel):
    id: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeClassificationJobRequest(BaseValidatorModel):
    jobId: str


class LastRunErrorStatus(BaseValidatorModel):
    code: Optional[LastRunErrorStatusCodeType] = None


class Statistics(BaseValidatorModel):
    approximateNumberOfObjectsToProcess: Optional[float] = None
    numberOfRuns: Optional[float] = None


class UserPausedDetails(BaseValidatorModel):
    jobExpiresAt: Optional[datetime] = None
    jobImminentExpirationHealthEventArn: Optional[str] = None
    jobPausedAt: Optional[datetime] = None


class DetectedDataDetails(BaseValidatorModel):
    value: str


class Detection(BaseValidatorModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    suppressed: Optional[bool] = None
    type: Optional[DataIdentifierTypeType] = None


class DisableOrganizationAdminAccountRequest(BaseValidatorModel):
    adminAccountId: str


class DisassociateMemberRequest(BaseValidatorModel):
    id: str


class DomainDetails(BaseValidatorModel):
    domainName: Optional[str] = None


class EnableMacieRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None


class EnableOrganizationAdminAccountRequest(BaseValidatorModel):
    adminAccountId: str
    clientToken: Optional[str] = None


class FindingStatisticsSortCriteria(BaseValidatorModel):
    attributeName: Optional[FindingStatisticsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None


class Severity(BaseValidatorModel):
    description: Optional[SeverityDescriptionType] = None
    score: Optional[int] = None


class FindingsFilterListItem(BaseValidatorModel):
    action: Optional[FindingsFilterActionType] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Invitation(BaseValidatorModel):
    accountId: Optional[str] = None
    invitationId: Optional[str] = None
    invitedAt: Optional[datetime] = None
    relationshipStatus: Optional[RelationshipStatusType] = None


class GetAllowListRequest(BaseValidatorModel):
    id: str


class GetBucketStatisticsRequest(BaseValidatorModel):
    accountId: Optional[str] = None


class GetClassificationScopeRequest(BaseValidatorModel):
    id: str


class GetCustomDataIdentifierRequest(BaseValidatorModel):
    id: str


class GroupCount(BaseValidatorModel):
    count: Optional[int] = None
    groupKey: Optional[str] = None


class GetFindingsFilterRequest(BaseValidatorModel):
    id: str


class SecurityHubConfiguration(BaseValidatorModel):
    publishClassificationFindings: bool
    publishPolicyFindings: bool


class SortCriteria(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class GetMemberRequest(BaseValidatorModel):
    id: str


class GetResourceProfileRequest(BaseValidatorModel):
    resourceArn: str


class ResourceStatistics(BaseValidatorModel):
    totalBytesClassified: Optional[int] = None
    totalDetections: Optional[int] = None
    totalDetectionsSuppressed: Optional[int] = None
    totalItemsClassified: Optional[int] = None
    totalItemsSensitive: Optional[int] = None
    totalItemsSkipped: Optional[int] = None
    totalItemsSkippedInvalidEncryption: Optional[int] = None
    totalItemsSkippedInvalidKms: Optional[int] = None
    totalItemsSkippedPermissionDenied: Optional[int] = None


class RetrievalConfiguration(BaseValidatorModel):
    retrievalMode: RetrievalModeType
    externalId: Optional[str] = None
    roleName: Optional[str] = None


class RevealConfiguration(BaseValidatorModel):
    status: RevealStatusType
    kmsKeyId: Optional[str] = None


class GetSensitiveDataOccurrencesAvailabilityRequest(BaseValidatorModel):
    findingId: str


class GetSensitiveDataOccurrencesRequest(BaseValidatorModel):
    findingId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetSensitivityInspectionTemplateRequest(BaseValidatorModel):
    id: str


class SensitivityInspectionTemplateExcludesOutput(BaseValidatorModel):
    managedDataIdentifierIds: Optional[List[str]] = None


class SensitivityInspectionTemplateIncludesOutput(BaseValidatorModel):
    allowListIds: Optional[List[str]] = None
    customDataIdentifierIds: Optional[List[str]] = None
    managedDataIdentifierIds: Optional[List[str]] = None


class UsageStatisticsFilter(BaseValidatorModel):
    comparator: Optional[UsageStatisticsFilterComparatorType] = None
    key: Optional[UsageStatisticsFilterKeyType] = None
    values: Optional[List[str]] = None


class UsageStatisticsSortBy(BaseValidatorModel):
    key: Optional[UsageStatisticsSortKeyType] = None
    orderBy: Optional[OrderByType] = None


class GetUsageTotalsRequest(BaseValidatorModel):
    timeRange: Optional[str] = None


class UsageTotal(BaseValidatorModel):
    currency: Optional[Literal['USD']] = None
    estimatedCost: Optional[str] = None
    type: Optional[UsageTypeType] = None


class IamUser(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    userName: Optional[str] = None


class IpCity(BaseValidatorModel):
    name: Optional[str] = None


class IpCountry(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None


class IpGeoLocation(BaseValidatorModel):
    lat: Optional[float] = None
    lon: Optional[float] = None


class IpOwner(BaseValidatorModel):
    asn: Optional[str] = None
    asnOrg: Optional[str] = None
    isp: Optional[str] = None
    org: Optional[str] = None


class MonthlySchedule(BaseValidatorModel):
    dayOfMonth: Optional[int] = None


class WeeklySchedule(BaseValidatorModel):
    dayOfWeek: Optional[DayOfWeekType] = None


class SimpleScopeTermOutput(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ScopeFilterKeyType] = None
    values: Optional[List[str]] = None


class SimpleScopeTerm(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ScopeFilterKeyType] = None
    values: Optional[List[str]] = None


class S3BucketDefinitionForJobOutput(BaseValidatorModel):
    accountId: str
    buckets: List[str]


class ListAllowListsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAutomatedDiscoveryAccountsRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsSortCriteria(BaseValidatorModel):
    attributeName: Optional[ListJobsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None


class ListClassificationScopesRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None


class ListCustomDataIdentifiersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFindingsFiltersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInvitationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsFilterTerm(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ListJobsFilterKeyType] = None
    values: Optional[List[str]] = None


class ListManagedDataIdentifiersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class ManagedDataIdentifierSummary(BaseValidatorModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    id: Optional[str] = None


class ListMembersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    onlyAssociated: Optional[str] = None


class Member(BaseValidatorModel):
    accountId: Optional[str] = None
    administratorAccountId: Optional[str] = None
    arn: Optional[str] = None
    email: Optional[str] = None
    invitedAt: Optional[datetime] = None
    masterAccountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None


class ListOrganizationAdminAccountsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListResourceProfileArtifactsRequest(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


class ResourceProfileArtifact(BaseValidatorModel):
    arn: str
    classificationResultStatus: str
    sensitive: Optional[bool] = None


class ListResourceProfileDetectionsRequest(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSensitivityInspectionTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SensitivityInspectionTemplatesEntry(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Range(BaseValidatorModel):
    end: Optional[int] = None
    start: Optional[int] = None
    startColumn: Optional[int] = None


class Record(BaseValidatorModel):
    jsonPath: Optional[str] = None
    recordIndex: Optional[int] = None


class S3BucketDefinitionForJob(BaseValidatorModel):
    accountId: str
    buckets: List[str]


class S3BucketOwner(BaseValidatorModel):
    displayName: Optional[str] = None
    id: Optional[str] = None


class ServerSideEncryption(BaseValidatorModel):
    encryptionType: Optional[EncryptionTypeType] = None
    kmsMasterKeyId: Optional[str] = None


class S3ClassificationScopeExclusion(BaseValidatorModel):
    bucketNames: List[str]


class S3ClassificationScopeExclusionUpdate(BaseValidatorModel):
    bucketNames: List[str]
    operation: ClassificationScopeUpdateOperationType


class SearchResourcesSimpleCriterion(BaseValidatorModel):
    comparator: Optional[SearchResourcesComparatorType] = None
    key: Optional[SearchResourcesSimpleCriterionKeyType] = None
    values: Optional[List[str]] = None


class SearchResourcesSortCriteria(BaseValidatorModel):
    attributeName: Optional[SearchResourcesSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None


class SearchResourcesTagCriterionPair(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class SensitivityInspectionTemplateExcludes(BaseValidatorModel):
    managedDataIdentifierIds: Optional[List[str]] = None


class SensitivityInspectionTemplateIncludes(BaseValidatorModel):
    allowListIds: Optional[List[str]] = None
    customDataIdentifierIds: Optional[List[str]] = None
    managedDataIdentifierIds: Optional[List[str]] = None


class ServiceLimit(BaseValidatorModel):
    isServiceLimited: Optional[bool] = None
    unit: Optional[Literal['TERABYTES']] = None
    value: Optional[int] = None


class SessionContextAttributes(BaseValidatorModel):
    creationDate: Optional[datetime] = None
    mfaAuthenticated: Optional[bool] = None


class SessionIssuer(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    type: Optional[str] = None
    userName: Optional[str] = None


class SuppressDataIdentifier(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[DataIdentifierTypeType] = None


class TagCriterionPairForJob(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TagValuePair(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class TestCustomDataIdentifierRequest(BaseValidatorModel):
    regex: str
    sampleText: str
    ignoreWords: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    maximumMatchDistance: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateAutomatedDiscoveryConfigurationRequest(BaseValidatorModel):
    status: AutomatedDiscoveryStatusType
    autoEnableOrganizationMembers: Optional[AutoEnableModeType] = None


class UpdateClassificationJobRequest(BaseValidatorModel):
    jobId: str
    jobStatus: JobStatusType


class UpdateMacieSessionRequest(BaseValidatorModel):
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None


class UpdateMemberSessionRequest(BaseValidatorModel):
    id: str
    status: MacieStatusType


class UpdateOrganizationConfigurationRequest(BaseValidatorModel):
    autoEnable: bool


class UpdateResourceProfileRequest(BaseValidatorModel):
    resourceArn: str
    sensitivityScoreOverride: Optional[int] = None


class UpdateRetrievalConfiguration(BaseValidatorModel):
    retrievalMode: RetrievalModeType
    roleName: Optional[str] = None


class UserIdentityRoot(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None


class CreateMemberRequest(BaseValidatorModel):
    account: AccountDetail
    tags: Optional[Dict[str, str]] = None


class AccountLevelPermissions(BaseValidatorModel):
    blockPublicAccess: Optional[BlockPublicAccess] = None


class AllowListCriteria(BaseValidatorModel):
    regex: Optional[str] = None
    s3WordsList: Optional[S3WordsList] = None


class FindingAction(BaseValidatorModel):
    actionType: Optional[Literal['AWS_API_CALL']] = None
    apiCallDetails: Optional[ApiCallDetails] = None


class BatchUpdateAutomatedDiscoveryAccountsRequest(BaseValidatorModel):
    accounts: Optional[List[AutomatedDiscoveryAccountUpdate]] = None


class BatchGetCustomDataIdentifiersResponse(BaseValidatorModel):
    customDataIdentifiers: List[BatchGetCustomDataIdentifierSummary]
    notFoundIdentifierIds: List[str]
    ResponseMetadata: ResponseMetadata


class BatchUpdateAutomatedDiscoveryAccountsResponse(BaseValidatorModel):
    errors: List[AutomatedDiscoveryAccountUpdateError]
    ResponseMetadata: ResponseMetadata


class CreateAllowListResponse(BaseValidatorModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


class CreateClassificationJobResponse(BaseValidatorModel):
    jobArn: str
    jobId: str
    ResponseMetadata: ResponseMetadata


class CreateCustomDataIdentifierResponse(BaseValidatorModel):
    customDataIdentifierId: str
    ResponseMetadata: ResponseMetadata


class CreateFindingsFilterResponse(BaseValidatorModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


class CreateMemberResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationConfigurationResponse(BaseValidatorModel):
    autoEnable: bool
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadata


class GetAutomatedDiscoveryConfigurationResponse(BaseValidatorModel):
    autoEnableOrganizationMembers: AutoEnableModeType
    classificationScopeId: str
    disabledAt: datetime
    firstEnabledAt: datetime
    lastUpdatedAt: datetime
    sensitivityInspectionTemplateId: str
    status: AutomatedDiscoveryStatusType
    ResponseMetadata: ResponseMetadata


class GetInvitationsCountResponse(BaseValidatorModel):
    invitationsCount: int
    ResponseMetadata: ResponseMetadata


class GetMacieSessionResponse(BaseValidatorModel):
    createdAt: datetime
    findingPublishingFrequency: FindingPublishingFrequencyType
    serviceRole: str
    status: MacieStatusType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetMemberResponse(BaseValidatorModel):
    accountId: str
    administratorAccountId: str
    arn: str
    email: str
    invitedAt: datetime
    masterAccountId: str
    relationshipStatus: RelationshipStatusType
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetSensitiveDataOccurrencesAvailabilityResponse(BaseValidatorModel):
    code: AvailabilityCodeType
    reasons: List[UnavailabilityReasonCodeType]
    ResponseMetadata: ResponseMetadata


class ListAllowListsResponse(BaseValidatorModel):
    allowLists: List[AllowListSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAutomatedDiscoveryAccountsResponse(BaseValidatorModel):
    items: List[AutomatedDiscoveryAccount]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFindingsResponse(BaseValidatorModel):
    findingIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListOrganizationAdminAccountsResponse(BaseValidatorModel):
    adminAccounts: List[AdminAccount]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class TestCustomDataIdentifierResponse(BaseValidatorModel):
    matchCount: int
    ResponseMetadata: ResponseMetadata


class UpdateAllowListResponse(BaseValidatorModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


class UpdateFindingsFilterResponse(BaseValidatorModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


class BucketLevelPermissions(BaseValidatorModel):
    accessControlList: Optional[AccessControlList] = None
    blockPublicAccess: Optional[BlockPublicAccess] = None
    bucketPolicy: Optional[BucketPolicy] = None


class MatchingBucket(BaseValidatorModel):
    accountId: Optional[str] = None
    automatedDiscoveryMonitoringStatus: Optional[AutomatedDiscoveryMonitoringStatusType] = None
    bucketName: Optional[str] = None
    classifiableObjectCount: Optional[int] = None
    classifiableSizeInBytes: Optional[int] = None
    errorCode: Optional[BucketMetadataErrorCodeType] = None
    errorMessage: Optional[str] = None
    jobDetails: Optional[JobDetails] = None
    lastAutomatedDiscoveryTime: Optional[datetime] = None
    objectCount: Optional[int] = None
    objectCountByEncryptionType: Optional[ObjectCountByEncryptionType] = None
    sensitivityScore: Optional[int] = None
    sizeInBytes: Optional[int] = None
    sizeInBytesCompressed: Optional[int] = None
    unclassifiableObjectCount: Optional[ObjectLevelStatistics] = None
    unclassifiableObjectSizeInBytes: Optional[ObjectLevelStatistics] = None


class DescribeBucketsRequest(BaseValidatorModel):
    criteria: Optional[Dict[str, BucketCriteriaAdditionalProperties]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[BucketSortCriteria] = None


class BucketStatisticsBySensitivity(BaseValidatorModel):
    classificationError: Optional[SensitivityAggregations] = None
    notClassified: Optional[SensitivityAggregations] = None
    notSensitive: Optional[SensitivityAggregations] = None
    sensitive: Optional[SensitivityAggregations] = None


class ClassificationExportConfiguration(BaseValidatorModel):
    s3Destination: Optional[S3Destination] = None


class ListClassificationScopesResponse(BaseValidatorModel):
    classificationScopes: List[ClassificationScopeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateCustomDataIdentifierRequest(BaseValidatorModel):
    name: str
    regex: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    ignoreWords: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    maximumMatchDistance: Optional[int] = None
    severityLevels: Optional[List[SeverityLevel]] = None
    tags: Optional[Dict[str, str]] = None


class GetCustomDataIdentifierResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deleted: bool
    description: str
    id: str
    ignoreWords: List[str]
    keywords: List[str]
    maximumMatchDistance: int
    name: str
    regex: str
    severityLevels: List[SeverityLevel]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateInvitationsResponse(BaseValidatorModel):
    unprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DeclineInvitationsResponse(BaseValidatorModel):
    unprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DeleteInvitationsResponse(BaseValidatorModel):
    unprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class FindingCriteriaOutput(BaseValidatorModel):
    criterion: Optional[Dict[str, CriterionAdditionalPropertiesOutput]] = None


class FindingCriteria(BaseValidatorModel):
    criterion: Optional[Dict[str, CriterionAdditionalProperties]] = None


class ListCustomDataIdentifiersResponse(BaseValidatorModel):
    items: List[CustomDataIdentifierSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeBucketsRequestPaginate(BaseValidatorModel):
    criteria: Optional[Dict[str, BucketCriteriaAdditionalProperties]] = None
    sortCriteria: Optional[BucketSortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAllowListsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAutomatedDiscoveryAccountsRequestPaginate(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClassificationScopesRequestPaginate(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomDataIdentifiersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsFiltersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvitationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedDataIdentifiersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersRequestPaginate(BaseValidatorModel):
    onlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationAdminAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceProfileArtifactsRequestPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceProfileDetectionsRequestPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSensitivityInspectionTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSensitiveDataOccurrencesResponse(BaseValidatorModel):
    error: str
    sensitiveDataOccurrences: Dict[str, List[DetectedDataDetails]]
    status: RevealRequestStatusType
    ResponseMetadata: ResponseMetadata


class ListResourceProfileDetectionsResponse(BaseValidatorModel):
    detections: List[Detection]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFindingsFiltersResponse(BaseValidatorModel):
    findingsFilterListItems: List[FindingsFilterListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetAdministratorAccountResponse(BaseValidatorModel):
    administrator: Invitation
    ResponseMetadata: ResponseMetadata


class GetMasterAccountResponse(BaseValidatorModel):
    master: Invitation
    ResponseMetadata: ResponseMetadata


class ListInvitationsResponse(BaseValidatorModel):
    invitations: List[Invitation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFindingStatisticsResponse(BaseValidatorModel):
    countsByGroup: List[GroupCount]
    ResponseMetadata: ResponseMetadata


class GetFindingsPublicationConfigurationResponse(BaseValidatorModel):
    securityHubConfiguration: SecurityHubConfiguration
    ResponseMetadata: ResponseMetadata


class PutFindingsPublicationConfigurationRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    securityHubConfiguration: Optional[SecurityHubConfiguration] = None


class GetFindingsRequest(BaseValidatorModel):
    findingIds: List[str]
    sortCriteria: Optional[SortCriteria] = None


class GetResourceProfileResponse(BaseValidatorModel):
    profileUpdatedAt: datetime
    sensitivityScore: int
    sensitivityScoreOverridden: bool
    statistics: ResourceStatistics
    ResponseMetadata: ResponseMetadata


class GetRevealConfigurationResponse(BaseValidatorModel):
    configuration: RevealConfiguration
    retrievalConfiguration: RetrievalConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateRevealConfigurationResponse(BaseValidatorModel):
    configuration: RevealConfiguration
    retrievalConfiguration: RetrievalConfiguration
    ResponseMetadata: ResponseMetadata


class GetSensitiveDataOccurrencesRequestWait(BaseValidatorModel):
    findingId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetSensitivityInspectionTemplateResponse(BaseValidatorModel):
    description: str
    excludes: SensitivityInspectionTemplateExcludesOutput
    includes: SensitivityInspectionTemplateIncludesOutput
    name: str
    sensitivityInspectionTemplateId: str
    ResponseMetadata: ResponseMetadata


class GetUsageStatisticsRequestPaginate(BaseValidatorModel):
    filterBy: Optional[List[UsageStatisticsFilter]] = None
    sortBy: Optional[UsageStatisticsSortBy] = None
    timeRange: Optional[TimeRangeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetUsageStatisticsRequest(BaseValidatorModel):
    filterBy: Optional[List[UsageStatisticsFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[UsageStatisticsSortBy] = None
    timeRange: Optional[TimeRangeType] = None


class GetUsageTotalsResponse(BaseValidatorModel):
    timeRange: TimeRangeType
    usageTotals: List[UsageTotal]
    ResponseMetadata: ResponseMetadata


class IpAddressDetails(BaseValidatorModel):
    ipAddressV4: Optional[str] = None
    ipCity: Optional[IpCity] = None
    ipCountry: Optional[IpCountry] = None
    ipGeoLocation: Optional[IpGeoLocation] = None
    ipOwner: Optional[IpOwner] = None


class JobScheduleFrequencyOutput(BaseValidatorModel):
    dailySchedule: Optional[Dict[str, Any]] = None
    monthlySchedule: Optional[MonthlySchedule] = None
    weeklySchedule: Optional[WeeklySchedule] = None


class JobScheduleFrequency(BaseValidatorModel):
    dailySchedule: Optional[Dict[str, Any]] = None
    monthlySchedule: Optional[MonthlySchedule] = None
    weeklySchedule: Optional[WeeklySchedule] = None


class ListJobsFilterCriteria(BaseValidatorModel):
    excludes: Optional[List[ListJobsFilterTerm]] = None
    includes: Optional[List[ListJobsFilterTerm]] = None


class ListManagedDataIdentifiersResponse(BaseValidatorModel):
    items: List[ManagedDataIdentifierSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMembersResponse(BaseValidatorModel):
    members: List[Member]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListResourceProfileArtifactsResponse(BaseValidatorModel):
    artifacts: List[ResourceProfileArtifact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSensitivityInspectionTemplatesResponse(BaseValidatorModel):
    sensitivityInspectionTemplates: List[SensitivityInspectionTemplatesEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Page(BaseValidatorModel):
    lineRange: Optional[Range] = None
    offsetRange: Optional[Range] = None
    pageNumber: Optional[int] = None


class S3Object(BaseValidatorModel):
    bucketArn: Optional[str] = None
    eTag: Optional[str] = None
    extension: Optional[str] = None
    key: Optional[str] = None
    lastModified: Optional[datetime] = None
    path: Optional[str] = None
    publicAccess: Optional[bool] = None
    serverSideEncryption: Optional[ServerSideEncryption] = None
    size: Optional[int] = None
    storageClass: Optional[StorageClassType] = None
    tags: Optional[List[KeyValuePair]] = None
    versionId: Optional[str] = None


class S3ClassificationScope(BaseValidatorModel):
    excludes: S3ClassificationScopeExclusion


class S3ClassificationScopeUpdate(BaseValidatorModel):
    excludes: S3ClassificationScopeExclusionUpdate


class SearchResourcesTagCriterion(BaseValidatorModel):
    comparator: Optional[SearchResourcesComparatorType] = None
    tagValues: Optional[List[SearchResourcesTagCriterionPair]] = None

SensitivityInspectionTemplateExcludesUnion = Union[SensitivityInspectionTemplateExcludes, SensitivityInspectionTemplateExcludesOutput]

SensitivityInspectionTemplateIncludesUnion = Union[SensitivityInspectionTemplateIncludes, SensitivityInspectionTemplateIncludesOutput]


class UsageByAccount(BaseValidatorModel):
    currency: Optional[Literal['USD']] = None
    estimatedCost: Optional[str] = None
    serviceLimit: Optional[ServiceLimit] = None
    type: Optional[UsageTypeType] = None


class SessionContext(BaseValidatorModel):
    attributes: Optional[SessionContextAttributes] = None
    sessionIssuer: Optional[SessionIssuer] = None


class UpdateResourceProfileDetectionsRequest(BaseValidatorModel):
    resourceArn: str
    suppressDataIdentifiers: Optional[List[SuppressDataIdentifier]] = None


class TagCriterionForJobOutput(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    tagValues: Optional[List[TagCriterionPairForJob]] = None


class TagCriterionForJob(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    tagValues: Optional[List[TagCriterionPairForJob]] = None


class TagScopeTermOutput(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[str] = None
    tagValues: Optional[List[TagValuePair]] = None
    target: Optional[Literal['S3_OBJECT']] = None


class TagScopeTerm(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[str] = None
    tagValues: Optional[List[TagValuePair]] = None
    target: Optional[Literal['S3_OBJECT']] = None


class UpdateRevealConfigurationRequest(BaseValidatorModel):
    configuration: RevealConfiguration
    retrievalConfiguration: Optional[UpdateRetrievalConfiguration] = None


class CreateAllowListRequest(BaseValidatorModel):
    clientToken: str
    criteria: AllowListCriteria
    name: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetAllowListResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    criteria: AllowListCriteria
    description: str
    id: str
    name: str
    status: AllowListStatus
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateAllowListRequest(BaseValidatorModel):
    criteria: AllowListCriteria
    id: str
    name: str
    description: Optional[str] = None


class BucketPermissionConfiguration(BaseValidatorModel):
    accountLevelPermissions: Optional[AccountLevelPermissions] = None
    bucketLevelPermissions: Optional[BucketLevelPermissions] = None


class MatchingResource(BaseValidatorModel):
    matchingBucket: Optional[MatchingBucket] = None


class GetBucketStatisticsResponse(BaseValidatorModel):
    bucketCount: int
    bucketCountByEffectivePermission: BucketCountByEffectivePermission
    bucketCountByEncryptionType: BucketCountByEncryptionType
    bucketCountByObjectEncryptionRequirement: BucketCountPolicyAllowsUnencryptedObjectUploads
    bucketCountBySharedAccessType: BucketCountBySharedAccessType
    bucketStatisticsBySensitivity: BucketStatisticsBySensitivity
    classifiableObjectCount: int
    classifiableSizeInBytes: int
    lastUpdated: datetime
    objectCount: int
    sizeInBytes: int
    sizeInBytesCompressed: int
    unclassifiableObjectCount: ObjectLevelStatistics
    unclassifiableObjectSizeInBytes: ObjectLevelStatistics
    ResponseMetadata: ResponseMetadata


class GetClassificationExportConfigurationResponse(BaseValidatorModel):
    configuration: ClassificationExportConfiguration
    ResponseMetadata: ResponseMetadata


class PutClassificationExportConfigurationRequest(BaseValidatorModel):
    configuration: ClassificationExportConfiguration


class PutClassificationExportConfigurationResponse(BaseValidatorModel):
    configuration: ClassificationExportConfiguration
    ResponseMetadata: ResponseMetadata


class GetFindingsFilterResponse(BaseValidatorModel):
    action: FindingsFilterActionType
    arn: str
    description: str
    findingCriteria: FindingCriteriaOutput
    id: str
    name: str
    position: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

FindingCriteriaUnion = Union[FindingCriteria, FindingCriteriaOutput]

JobScheduleFrequencyUnion = Union[JobScheduleFrequency, JobScheduleFrequencyOutput]


class ListClassificationJobsRequestPaginate(BaseValidatorModel):
    filterCriteria: Optional[ListJobsFilterCriteria] = None
    sortCriteria: Optional[ListJobsSortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClassificationJobsRequest(BaseValidatorModel):
    filterCriteria: Optional[ListJobsFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[ListJobsSortCriteria] = None


class Occurrences(BaseValidatorModel):
    cells: Optional[List[Cell]] = None
    lineRanges: Optional[List[Range]] = None
    offsetRanges: Optional[List[Range]] = None
    pages: Optional[List[Page]] = None
    records: Optional[List[Record]] = None


class GetClassificationScopeResponse(BaseValidatorModel):
    id: str
    name: str
    s3: S3ClassificationScope
    ResponseMetadata: ResponseMetadata


class UpdateClassificationScopeRequest(BaseValidatorModel):
    id: str
    s3: Optional[S3ClassificationScopeUpdate] = None


class SearchResourcesCriteria(BaseValidatorModel):
    simpleCriterion: Optional[SearchResourcesSimpleCriterion] = None
    tagCriterion: Optional[SearchResourcesTagCriterion] = None


class UpdateSensitivityInspectionTemplateRequest(BaseValidatorModel):
    id: str
    description: Optional[str] = None
    excludes: Optional[SensitivityInspectionTemplateExcludesUnion] = None
    includes: Optional[SensitivityInspectionTemplateIncludesUnion] = None


class UsageRecord(BaseValidatorModel):
    accountId: Optional[str] = None
    automatedDiscoveryFreeTrialStartDate: Optional[datetime] = None
    freeTrialStartDate: Optional[datetime] = None
    usage: Optional[List[UsageByAccount]] = None


class AssumedRole(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    sessionContext: Optional[SessionContext] = None


class FederatedUser(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    sessionContext: Optional[SessionContext] = None


class CriteriaForJobOutput(BaseValidatorModel):
    simpleCriterion: Optional[SimpleCriterionForJobOutput] = None
    tagCriterion: Optional[TagCriterionForJobOutput] = None


class CriteriaForJob(BaseValidatorModel):
    simpleCriterion: Optional[SimpleCriterionForJob] = None
    tagCriterion: Optional[TagCriterionForJob] = None


class JobScopeTermOutput(BaseValidatorModel):
    simpleScopeTerm: Optional[SimpleScopeTermOutput] = None
    tagScopeTerm: Optional[TagScopeTermOutput] = None


class JobScopeTerm(BaseValidatorModel):
    simpleScopeTerm: Optional[SimpleScopeTerm] = None
    tagScopeTerm: Optional[TagScopeTerm] = None


class BucketPublicAccess(BaseValidatorModel):
    effectivePermission: Optional[EffectivePermissionType] = None
    permissionConfiguration: Optional[BucketPermissionConfiguration] = None


class SearchResourcesResponse(BaseValidatorModel):
    matchingResources: List[MatchingResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateFindingsFilterRequest(BaseValidatorModel):
    action: FindingsFilterActionType
    findingCriteria: FindingCriteriaUnion
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    position: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class GetFindingStatisticsRequest(BaseValidatorModel):
    groupBy: GroupByType
    findingCriteria: Optional[FindingCriteriaUnion] = None
    size: Optional[int] = None
    sortCriteria: Optional[FindingStatisticsSortCriteria] = None


class ListFindingsRequestPaginate(BaseValidatorModel):
    findingCriteria: Optional[FindingCriteriaUnion] = None
    sortCriteria: Optional[SortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsRequest(BaseValidatorModel):
    findingCriteria: Optional[FindingCriteriaUnion] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteria] = None


class UpdateFindingsFilterRequest(BaseValidatorModel):
    id: str
    action: Optional[FindingsFilterActionType] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    findingCriteria: Optional[FindingCriteriaUnion] = None
    name: Optional[str] = None
    position: Optional[int] = None


class CustomDetection(BaseValidatorModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    occurrences: Optional[Occurrences] = None


class DefaultDetection(BaseValidatorModel):
    count: Optional[int] = None
    occurrences: Optional[Occurrences] = None
    type: Optional[str] = None


class SearchResourcesCriteriaBlock(BaseValidatorModel):
    and_: Optional[List[SearchResourcesCriteria]] = None


class GetUsageStatisticsResponse(BaseValidatorModel):
    records: List[UsageRecord]
    timeRange: TimeRangeType
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UserIdentity(BaseValidatorModel):
    assumedRole: Optional[AssumedRole] = None
    awsAccount: Optional[AwsAccount] = None
    awsService: Optional[AwsService] = None
    federatedUser: Optional[FederatedUser] = None
    iamUser: Optional[IamUser] = None
    root: Optional[UserIdentityRoot] = None
    type: Optional[UserIdentityTypeType] = None


class CriteriaBlockForJobOutput(BaseValidatorModel):
    and_: Optional[List[CriteriaForJobOutput]] = None


class CriteriaBlockForJob(BaseValidatorModel):
    and_: Optional[List[CriteriaForJob]] = None


class JobScopingBlockOutput(BaseValidatorModel):
    and_: Optional[List[JobScopeTermOutput]] = None


class JobScopingBlock(BaseValidatorModel):
    and_: Optional[List[JobScopeTerm]] = None


class BucketMetadata(BaseValidatorModel):
    accountId: Optional[str] = None
    allowsUnencryptedObjectUploads: Optional[AllowsUnencryptedObjectUploadsType] = None
    automatedDiscoveryMonitoringStatus: Optional[AutomatedDiscoveryMonitoringStatusType] = None
    bucketArn: Optional[str] = None
    bucketCreatedAt: Optional[datetime] = None
    bucketName: Optional[str] = None
    classifiableObjectCount: Optional[int] = None
    classifiableSizeInBytes: Optional[int] = None
    errorCode: Optional[BucketMetadataErrorCodeType] = None
    errorMessage: Optional[str] = None
    jobDetails: Optional[JobDetails] = None
    lastAutomatedDiscoveryTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None
    objectCount: Optional[int] = None
    objectCountByEncryptionType: Optional[ObjectCountByEncryptionType] = None
    publicAccess: Optional[BucketPublicAccess] = None
    region: Optional[str] = None
    replicationDetails: Optional[ReplicationDetails] = None
    sensitivityScore: Optional[int] = None
    serverSideEncryption: Optional[BucketServerSideEncryption] = None
    sharedAccess: Optional[SharedAccessType] = None
    sizeInBytes: Optional[int] = None
    sizeInBytesCompressed: Optional[int] = None
    tags: Optional[List[KeyValuePair]] = None
    unclassifiableObjectCount: Optional[ObjectLevelStatistics] = None
    unclassifiableObjectSizeInBytes: Optional[ObjectLevelStatistics] = None
    versioning: Optional[bool] = None


class S3Bucket(BaseValidatorModel):
    allowsUnencryptedObjectUploads: Optional[AllowsUnencryptedObjectUploadsType] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    defaultServerSideEncryption: Optional[ServerSideEncryption] = None
    name: Optional[str] = None
    owner: Optional[S3BucketOwner] = None
    publicAccess: Optional[BucketPublicAccess] = None
    tags: Optional[List[KeyValuePair]] = None


class CustomDataIdentifiers(BaseValidatorModel):
    detections: Optional[List[CustomDetection]] = None
    totalCount: Optional[int] = None


class SensitiveDataItem(BaseValidatorModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    detections: Optional[List[DefaultDetection]] = None
    totalCount: Optional[int] = None


class SearchResourcesBucketCriteria(BaseValidatorModel):
    excludes: Optional[SearchResourcesCriteriaBlock] = None
    includes: Optional[SearchResourcesCriteriaBlock] = None


class FindingActor(BaseValidatorModel):
    domainDetails: Optional[DomainDetails] = None
    ipAddressDetails: Optional[IpAddressDetails] = None
    userIdentity: Optional[UserIdentity] = None


class S3BucketCriteriaForJobOutput(BaseValidatorModel):
    excludes: Optional[CriteriaBlockForJobOutput] = None
    includes: Optional[CriteriaBlockForJobOutput] = None


class S3BucketCriteriaForJob(BaseValidatorModel):
    excludes: Optional[CriteriaBlockForJob] = None
    includes: Optional[CriteriaBlockForJob] = None


class ScopingOutput(BaseValidatorModel):
    excludes: Optional[JobScopingBlockOutput] = None
    includes: Optional[JobScopingBlockOutput] = None


class Scoping(BaseValidatorModel):
    excludes: Optional[JobScopingBlock] = None
    includes: Optional[JobScopingBlock] = None


class DescribeBucketsResponse(BaseValidatorModel):
    buckets: List[BucketMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResourcesAffected(BaseValidatorModel):
    s3Bucket: Optional[S3Bucket] = None
    s3Object: Optional[S3Object] = None


class ClassificationResult(BaseValidatorModel):
    additionalOccurrences: Optional[bool] = None
    customDataIdentifiers: Optional[CustomDataIdentifiers] = None
    mimeType: Optional[str] = None
    sensitiveData: Optional[List[SensitiveDataItem]] = None
    sizeClassified: Optional[int] = None
    status: Optional[ClassificationResultStatus] = None


class SearchResourcesRequestPaginate(BaseValidatorModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteria] = None
    sortCriteria: Optional[SearchResourcesSortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchResourcesRequest(BaseValidatorModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SearchResourcesSortCriteria] = None


class PolicyDetails(BaseValidatorModel):
    action: Optional[FindingAction] = None
    actor: Optional[FindingActor] = None


class JobSummary(BaseValidatorModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobOutput] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJobOutput]] = None
    createdAt: Optional[datetime] = None
    jobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    jobType: Optional[JobTypeType] = None
    lastRunErrorStatus: Optional[LastRunErrorStatus] = None
    name: Optional[str] = None
    userPausedDetails: Optional[UserPausedDetails] = None


class S3JobDefinitionOutput(BaseValidatorModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobOutput] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJobOutput]] = None
    scoping: Optional[ScopingOutput] = None


class S3JobDefinition(BaseValidatorModel):
    bucketCriteria: Optional[S3BucketCriteriaForJob] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJob]] = None
    scoping: Optional[Scoping] = None


class ClassificationDetails(BaseValidatorModel):
    detailedResultsLocation: Optional[str] = None
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    originType: Optional[OriginTypeType] = None
    result: Optional[ClassificationResult] = None


class ListClassificationJobsResponse(BaseValidatorModel):
    items: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeClassificationJobResponse(BaseValidatorModel):
    allowListIds: List[str]
    clientToken: str
    createdAt: datetime
    customDataIdentifierIds: List[str]
    description: str
    initialRun: bool
    jobArn: str
    jobId: str
    jobStatus: JobStatusType
    jobType: JobTypeType
    lastRunErrorStatus: LastRunErrorStatus
    lastRunTime: datetime
    managedDataIdentifierIds: List[str]
    managedDataIdentifierSelector: ManagedDataIdentifierSelectorType
    name: str
    s3JobDefinition: S3JobDefinitionOutput
    samplingPercentage: int
    scheduleFrequency: JobScheduleFrequencyOutput
    statistics: Statistics
    tags: Dict[str, str]
    userPausedDetails: UserPausedDetails
    ResponseMetadata: ResponseMetadata

S3JobDefinitionUnion = Union[S3JobDefinition, S3JobDefinitionOutput]


class Finding(BaseValidatorModel):
    accountId: Optional[str] = None
    archived: Optional[bool] = None
    category: Optional[FindingCategoryType] = None
    classificationDetails: Optional[ClassificationDetails] = None
    count: Optional[int] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    partition: Optional[str] = None
    policyDetails: Optional[PolicyDetails] = None
    region: Optional[str] = None
    resourcesAffected: Optional[ResourcesAffected] = None
    sample: Optional[bool] = None
    schemaVersion: Optional[str] = None
    severity: Optional[Severity] = None
    title: Optional[str] = None
    type: Optional[FindingTypeType] = None
    updatedAt: Optional[datetime] = None


class CreateClassificationJobRequest(BaseValidatorModel):
    clientToken: str
    jobType: JobTypeType
    name: str
    s3JobDefinition: S3JobDefinitionUnion
    allowListIds: Optional[List[str]] = None
    customDataIdentifierIds: Optional[List[str]] = None
    description: Optional[str] = None
    initialRun: Optional[bool] = None
    managedDataIdentifierIds: Optional[List[str]] = None
    managedDataIdentifierSelector: Optional[ManagedDataIdentifierSelectorType] = None
    samplingPercentage: Optional[int] = None
    scheduleFrequency: Optional[JobScheduleFrequencyUnion] = None
    tags: Optional[Dict[str, str]] = None


class GetFindingsResponse(BaseValidatorModel):
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata