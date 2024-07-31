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
from aws_resource_validator.pydantic_models.macie2_constants import *

class AcceptInvitationRequestRequestTypeDef(BaseModel):
    invitationId: str
    administratorAccountId: Optional[str] = None
    masterAccount: Optional[str] = None

class AccessControlListTypeDef(BaseModel):
    allowsPublicReadAccess: Optional[bool] = None
    allowsPublicWriteAccess: Optional[bool] = None

class AccountDetailTypeDef(BaseModel):
    accountId: str
    email: str

class BlockPublicAccessTypeDef(BaseModel):
    blockPublicAcls: Optional[bool] = None
    blockPublicPolicy: Optional[bool] = None
    ignorePublicAcls: Optional[bool] = None
    restrictPublicBuckets: Optional[bool] = None

class AdminAccountTypeDef(BaseModel):
    accountId: Optional[str] = None
    status: Optional[AdminStatusType] = None

class S3WordsListTypeDef(BaseModel):
    bucketName: str
    objectKey: str

class AllowListStatusTypeDef(BaseModel):
    code: AllowListStatusCodeType
    description: Optional[str] = None

class AllowListSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None

class ApiCallDetailsTypeDef(BaseModel):
    api: Optional[str] = None
    apiServiceName: Optional[str] = None
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None

class AutomatedDiscoveryAccountTypeDef(BaseModel):
    accountId: Optional[str] = None
    status: Optional[AutomatedDiscoveryAccountStatusType] = None

class AutomatedDiscoveryAccountUpdateErrorTypeDef(BaseModel):
    accountId: Optional[str] = None
    errorCode: Optional[AutomatedDiscoveryAccountUpdateErrorCodeType] = None

class AutomatedDiscoveryAccountUpdateTypeDef(BaseModel):
    accountId: Optional[str] = None
    status: Optional[AutomatedDiscoveryAccountStatusType] = None

class AwsAccountTypeDef(BaseModel):
    accountId: Optional[str] = None
    principalId: Optional[str] = None

class AwsServiceTypeDef(BaseModel):
    invokedBy: Optional[str] = None

class BatchGetCustomDataIdentifierSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    deleted: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class BatchGetCustomDataIdentifiersRequestRequestTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BucketCountByEffectivePermissionTypeDef(BaseModel):
    publiclyAccessible: Optional[int] = None
    publiclyReadable: Optional[int] = None
    publiclyWritable: Optional[int] = None
    unknown: Optional[int] = None

class BucketCountByEncryptionTypeTypeDef(BaseModel):
    kmsManaged: Optional[int] = None
    s3Managed: Optional[int] = None
    unencrypted: Optional[int] = None
    unknown: Optional[int] = None

class BucketCountBySharedAccessTypeTypeDef(BaseModel):
    external: Optional[int] = None
    internal: Optional[int] = None
    notShared: Optional[int] = None
    unknown: Optional[int] = None

class BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef(BaseModel):
    allowsUnencryptedObjectUploads: Optional[int] = None
    deniesUnencryptedObjectUploads: Optional[int] = None
    unknown: Optional[int] = None

class BucketCriteriaAdditionalPropertiesTypeDef(BaseModel):
    eq: Optional[Sequence[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[Sequence[str]] = None
    prefix: Optional[str] = None

class BucketPolicyTypeDef(BaseModel):
    allowsPublicReadAccess: Optional[bool] = None
    allowsPublicWriteAccess: Optional[bool] = None

class BucketServerSideEncryptionTypeDef(BaseModel):
    kmsMasterKeyId: Optional[str] = None
    type: Optional[TypeType] = None

class JobDetailsTypeDef(BaseModel):
    isDefinedInJob: Optional[IsDefinedInJobType] = None
    isMonitoredByJob: Optional[IsMonitoredByJobType] = None
    lastJobId: Optional[str] = None
    lastJobRunTime: Optional[datetime] = None

class KeyValuePairTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ObjectCountByEncryptionTypeTypeDef(BaseModel):
    customerManaged: Optional[int] = None
    kmsManaged: Optional[int] = None
    s3Managed: Optional[int] = None
    unencrypted: Optional[int] = None
    unknown: Optional[int] = None

class ObjectLevelStatisticsTypeDef(BaseModel):
    fileType: Optional[int] = None
    storageClass: Optional[int] = None
    total: Optional[int] = None

class ReplicationDetailsTypeDef(BaseModel):
    replicated: Optional[bool] = None
    replicatedExternally: Optional[bool] = None
    replicationAccounts: Optional[List[str]] = None

class BucketSortCriteriaTypeDef(BaseModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class SensitivityAggregationsTypeDef(BaseModel):
    classifiableSizeInBytes: Optional[int] = None
    publiclyAccessibleCount: Optional[int] = None
    totalCount: Optional[int] = None
    totalSizeInBytes: Optional[int] = None

class CellTypeDef(BaseModel):
    cellReference: Optional[str] = None
    column: Optional[int] = None
    columnName: Optional[str] = None
    row: Optional[int] = None

class S3DestinationTypeDef(BaseModel):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: Optional[str] = None

class ClassificationResultStatusTypeDef(BaseModel):
    code: Optional[str] = None
    reason: Optional[str] = None

class ClassificationScopeSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class SeverityLevelTypeDef(BaseModel):
    occurrencesThreshold: int
    severity: DataIdentifierSeverityType

class CreateInvitationsRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[str]
    disableEmailNotification: Optional[bool] = None
    message: Optional[str] = None

class UnprocessedAccountTypeDef(BaseModel):
    accountId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class CreateSampleFindingsRequestRequestTypeDef(BaseModel):
    findingTypes: Optional[Sequence[FindingTypeType]] = None

class SimpleCriterionForJobOutputTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[SimpleCriterionKeyForJobType] = None
    values: Optional[List[str]] = None

class SimpleCriterionForJobTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[SimpleCriterionKeyForJobType] = None
    values: Optional[Sequence[str]] = None

class CriterionAdditionalPropertiesOutputTypeDef(BaseModel):
    eq: Optional[List[str]] = None
    eqExactMatch: Optional[List[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[List[str]] = None

class CriterionAdditionalPropertiesTypeDef(BaseModel):
    eq: Optional[Sequence[str]] = None
    eqExactMatch: Optional[Sequence[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[Sequence[str]] = None

class CustomDataIdentifierSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class DeclineInvitationsRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[str]

class DeleteAllowListRequestRequestTypeDef(BaseModel):
    id: str
    ignoreJobChecks: Optional[str] = None

class DeleteCustomDataIdentifierRequestRequestTypeDef(BaseModel):
    id: str

class DeleteFindingsFilterRequestRequestTypeDef(BaseModel):
    id: str

class DeleteInvitationsRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[str]

class DeleteMemberRequestRequestTypeDef(BaseModel):
    id: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClassificationJobRequestRequestTypeDef(BaseModel):
    jobId: str

class LastRunErrorStatusTypeDef(BaseModel):
    code: Optional[LastRunErrorStatusCodeType] = None

class StatisticsTypeDef(BaseModel):
    approximateNumberOfObjectsToProcess: Optional[float] = None
    numberOfRuns: Optional[float] = None

class UserPausedDetailsTypeDef(BaseModel):
    jobExpiresAt: Optional[datetime] = None
    jobImminentExpirationHealthEventArn: Optional[str] = None
    jobPausedAt: Optional[datetime] = None

class DetectedDataDetailsTypeDef(BaseModel):
    value: str

class DetectionTypeDef(BaseModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    suppressed: Optional[bool] = None
    type: Optional[DataIdentifierTypeType] = None

class DisableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    adminAccountId: str

class DisassociateMemberRequestRequestTypeDef(BaseModel):
    id: str

class DomainDetailsTypeDef(BaseModel):
    domainName: Optional[str] = None

class EnableMacieRequestRequestTypeDef(BaseModel):
    clientToken: Optional[str] = None
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    adminAccountId: str
    clientToken: Optional[str] = None

class FindingStatisticsSortCriteriaTypeDef(BaseModel):
    attributeName: Optional[FindingStatisticsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None

class SeverityTypeDef(BaseModel):
    description: Optional[SeverityDescriptionType] = None
    score: Optional[int] = None

class FindingsFilterListItemTypeDef(BaseModel):
    action: Optional[FindingsFilterActionType] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class InvitationTypeDef(BaseModel):
    accountId: Optional[str] = None
    invitationId: Optional[str] = None
    invitedAt: Optional[datetime] = None
    relationshipStatus: Optional[RelationshipStatusType] = None

class GetAllowListRequestRequestTypeDef(BaseModel):
    id: str

class GetBucketStatisticsRequestRequestTypeDef(BaseModel):
    accountId: Optional[str] = None

class GetClassificationScopeRequestRequestTypeDef(BaseModel):
    id: str

class GetCustomDataIdentifierRequestRequestTypeDef(BaseModel):
    id: str

class GroupCountTypeDef(BaseModel):
    count: Optional[int] = None
    groupKey: Optional[str] = None

class GetFindingsFilterRequestRequestTypeDef(BaseModel):
    id: str

class SecurityHubConfigurationTypeDef(BaseModel):
    publishClassificationFindings: bool
    publishPolicyFindings: bool

class SortCriteriaTypeDef(BaseModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class GetMemberRequestRequestTypeDef(BaseModel):
    id: str

class GetResourceProfileRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ResourceStatisticsTypeDef(BaseModel):
    totalBytesClassified: Optional[int] = None
    totalDetections: Optional[int] = None
    totalDetectionsSuppressed: Optional[int] = None
    totalItemsClassified: Optional[int] = None
    totalItemsSensitive: Optional[int] = None
    totalItemsSkipped: Optional[int] = None
    totalItemsSkippedInvalidEncryption: Optional[int] = None
    totalItemsSkippedInvalidKms: Optional[int] = None
    totalItemsSkippedPermissionDenied: Optional[int] = None

class RetrievalConfigurationTypeDef(BaseModel):
    retrievalMode: RetrievalModeType
    externalId: Optional[str] = None
    roleName: Optional[str] = None

class RevealConfigurationTypeDef(BaseModel):
    status: RevealStatusType
    kmsKeyId: Optional[str] = None

class GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef(BaseModel):
    findingId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetSensitiveDataOccurrencesRequestRequestTypeDef(BaseModel):
    findingId: str

class GetSensitivityInspectionTemplateRequestRequestTypeDef(BaseModel):
    id: str

class SensitivityInspectionTemplateExcludesOutputTypeDef(BaseModel):
    managedDataIdentifierIds: Optional[List[str]] = None

class SensitivityInspectionTemplateIncludesOutputTypeDef(BaseModel):
    allowListIds: Optional[List[str]] = None
    customDataIdentifierIds: Optional[List[str]] = None
    managedDataIdentifierIds: Optional[List[str]] = None

class UsageStatisticsFilterTypeDef(BaseModel):
    comparator: Optional[UsageStatisticsFilterComparatorType] = None
    key: Optional[UsageStatisticsFilterKeyType] = None
    values: Optional[Sequence[str]] = None

class UsageStatisticsSortByTypeDef(BaseModel):
    key: Optional[UsageStatisticsSortKeyType] = None
    orderBy: Optional[OrderByType] = None

class GetUsageTotalsRequestRequestTypeDef(BaseModel):
    timeRange: Optional[str] = None

class UsageTotalTypeDef(BaseModel):
    currency: Optional[Literal["USD"]] = None
    estimatedCost: Optional[str] = None
    type: Optional[UsageTypeType] = None

class IamUserTypeDef(BaseModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    userName: Optional[str] = None

class IpCityTypeDef(BaseModel):
    name: Optional[str] = None

class IpCountryTypeDef(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None

class IpGeoLocationTypeDef(BaseModel):
    lat: Optional[float] = None
    lon: Optional[float] = None

class IpOwnerTypeDef(BaseModel):
    asn: Optional[str] = None
    asnOrg: Optional[str] = None
    isp: Optional[str] = None
    org: Optional[str] = None

class MonthlyScheduleTypeDef(BaseModel):
    dayOfMonth: Optional[int] = None

class WeeklyScheduleTypeDef(BaseModel):
    dayOfWeek: Optional[DayOfWeekType] = None

class SimpleScopeTermOutputTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ScopeFilterKeyType] = None
    values: Optional[List[str]] = None

class SimpleScopeTermTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ScopeFilterKeyType] = None
    values: Optional[Sequence[str]] = None

class S3BucketDefinitionForJobOutputTypeDef(BaseModel):
    accountId: str
    buckets: List[str]

class ListAllowListsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAutomatedDiscoveryAccountsRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsSortCriteriaTypeDef(BaseModel):
    attributeName: Optional[ListJobsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None

class ListClassificationScopesRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListCustomDataIdentifiersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFindingsFiltersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListInvitationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsFilterTermTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ListJobsFilterKeyType] = None
    values: Optional[Sequence[str]] = None

class ListManagedDataIdentifiersRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ManagedDataIdentifierSummaryTypeDef(BaseModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    id: Optional[str] = None

class ListMembersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    onlyAssociated: Optional[str] = None

class MemberTypeDef(BaseModel):
    accountId: Optional[str] = None
    administratorAccountId: Optional[str] = None
    arn: Optional[str] = None
    email: Optional[str] = None
    invitedAt: Optional[datetime] = None
    masterAccountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListResourceProfileArtifactsRequestRequestTypeDef(BaseModel):
    resourceArn: str
    nextToken: Optional[str] = None

class ResourceProfileArtifactTypeDef(BaseModel):
    arn: str
    classificationResultStatus: str
    sensitive: Optional[bool] = None

class ListResourceProfileDetectionsRequestRequestTypeDef(BaseModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSensitivityInspectionTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SensitivityInspectionTemplatesEntryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RangeTypeDef(BaseModel):
    end: Optional[int] = None
    start: Optional[int] = None
    startColumn: Optional[int] = None

class RecordTypeDef(BaseModel):
    jsonPath: Optional[str] = None
    recordIndex: Optional[int] = None

class S3BucketDefinitionForJobTypeDef(BaseModel):
    accountId: str
    buckets: Sequence[str]

class S3BucketOwnerTypeDef(BaseModel):
    displayName: Optional[str] = None
    id: Optional[str] = None

class ServerSideEncryptionTypeDef(BaseModel):
    encryptionType: Optional[EncryptionTypeType] = None
    kmsMasterKeyId: Optional[str] = None

class S3ClassificationScopeExclusionTypeDef(BaseModel):
    bucketNames: List[str]

class S3ClassificationScopeExclusionUpdateTypeDef(BaseModel):
    bucketNames: Sequence[str]
    operation: ClassificationScopeUpdateOperationType

class SearchResourcesSimpleCriterionTypeDef(BaseModel):
    comparator: Optional[SearchResourcesComparatorType] = None
    key: Optional[SearchResourcesSimpleCriterionKeyType] = None
    values: Optional[Sequence[str]] = None

class SearchResourcesSortCriteriaTypeDef(BaseModel):
    attributeName: Optional[SearchResourcesSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None

class SearchResourcesTagCriterionPairTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class SensitivityInspectionTemplateExcludesTypeDef(BaseModel):
    managedDataIdentifierIds: Optional[Sequence[str]] = None

class SensitivityInspectionTemplateIncludesTypeDef(BaseModel):
    allowListIds: Optional[Sequence[str]] = None
    customDataIdentifierIds: Optional[Sequence[str]] = None
    managedDataIdentifierIds: Optional[Sequence[str]] = None

class ServiceLimitTypeDef(BaseModel):
    isServiceLimited: Optional[bool] = None
    unit: Optional[Literal["TERABYTES"]] = None
    value: Optional[int] = None

class SessionContextAttributesTypeDef(BaseModel):
    creationDate: Optional[datetime] = None
    mfaAuthenticated: Optional[bool] = None

class SessionIssuerTypeDef(BaseModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    type: Optional[str] = None
    userName: Optional[str] = None

class SuppressDataIdentifierTypeDef(BaseModel):
    id: Optional[str] = None
    type: Optional[DataIdentifierTypeType] = None

class TagCriterionPairForJobTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TagValuePairTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class TestCustomDataIdentifierRequestRequestTypeDef(BaseModel):
    regex: str
    sampleText: str
    ignoreWords: Optional[Sequence[str]] = None
    keywords: Optional[Sequence[str]] = None
    maximumMatchDistance: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef(BaseModel):
    status: AutomatedDiscoveryStatusType
    autoEnableOrganizationMembers: Optional[AutoEnableModeType] = None

class UpdateClassificationJobRequestRequestTypeDef(BaseModel):
    jobId: str
    jobStatus: JobStatusType

class UpdateMacieSessionRequestRequestTypeDef(BaseModel):
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None

class UpdateMemberSessionRequestRequestTypeDef(BaseModel):
    id: str
    status: MacieStatusType

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    autoEnable: bool

class UpdateResourceProfileRequestRequestTypeDef(BaseModel):
    resourceArn: str
    sensitivityScoreOverride: Optional[int] = None

class UpdateRetrievalConfigurationTypeDef(BaseModel):
    retrievalMode: RetrievalModeType
    roleName: Optional[str] = None

class UserIdentityRootTypeDef(BaseModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None

class CreateMemberRequestRequestTypeDef(BaseModel):
    account: AccountDetailTypeDef
    tags: Optional[Mapping[str, str]] = None

class AccountLevelPermissionsTypeDef(BaseModel):
    blockPublicAccess: Optional[BlockPublicAccessTypeDef] = None

class AllowListCriteriaTypeDef(BaseModel):
    regex: Optional[str] = None
    s3WordsList: Optional[S3WordsListTypeDef] = None

class FindingActionTypeDef(BaseModel):
    actionType: Optional[Literal["AWS_API_CALL"]] = None
    apiCallDetails: Optional[ApiCallDetailsTypeDef] = None

class BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef(BaseModel):
    accounts: Optional[Sequence[AutomatedDiscoveryAccountUpdateTypeDef]] = None

class BatchGetCustomDataIdentifiersResponseTypeDef(BaseModel):
    customDataIdentifiers: List[BatchGetCustomDataIdentifierSummaryTypeDef]
    notFoundIdentifierIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef(BaseModel):
    errors: List[AutomatedDiscoveryAccountUpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAllowListResponseTypeDef(BaseModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClassificationJobResponseTypeDef(BaseModel):
    jobArn: str
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDataIdentifierResponseTypeDef(BaseModel):
    customDataIdentifierId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingsFilterResponseTypeDef(BaseModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMemberResponseTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(BaseModel):
    autoEnable: bool
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutomatedDiscoveryConfigurationResponseTypeDef(BaseModel):
    autoEnableOrganizationMembers: AutoEnableModeType
    classificationScopeId: str
    disabledAt: datetime
    firstEnabledAt: datetime
    lastUpdatedAt: datetime
    sensitivityInspectionTemplateId: str
    status: AutomatedDiscoveryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvitationsCountResponseTypeDef(BaseModel):
    invitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetMacieSessionResponseTypeDef(BaseModel):
    createdAt: datetime
    findingPublishingFrequency: FindingPublishingFrequencyType
    serviceRole: str
    status: MacieStatusType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMemberResponseTypeDef(BaseModel):
    accountId: str
    administratorAccountId: str
    arn: str
    email: str
    invitedAt: datetime
    masterAccountId: str
    relationshipStatus: RelationshipStatusType
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSensitiveDataOccurrencesAvailabilityResponseTypeDef(BaseModel):
    code: AvailabilityCodeType
    reasons: List[UnavailabilityReasonCodeType]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAllowListsResponseTypeDef(BaseModel):
    allowLists: List[AllowListSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomatedDiscoveryAccountsResponseTypeDef(BaseModel):
    items: List[AutomatedDiscoveryAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsResponseTypeDef(BaseModel):
    findingIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationAdminAccountsResponseTypeDef(BaseModel):
    adminAccounts: List[AdminAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TestCustomDataIdentifierResponseTypeDef(BaseModel):
    matchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAllowListResponseTypeDef(BaseModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFindingsFilterResponseTypeDef(BaseModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class BucketLevelPermissionsTypeDef(BaseModel):
    accessControlList: Optional[AccessControlListTypeDef] = None
    blockPublicAccess: Optional[BlockPublicAccessTypeDef] = None
    bucketPolicy: Optional[BucketPolicyTypeDef] = None

class MatchingBucketTypeDef(BaseModel):
    accountId: Optional[str] = None
    automatedDiscoveryMonitoringStatus: Optional[AutomatedDiscoveryMonitoringStatusType] = None
    bucketName: Optional[str] = None
    classifiableObjectCount: Optional[int] = None
    classifiableSizeInBytes: Optional[int] = None
    errorCode: Optional[Literal["ACCESS_DENIED"]] = None
    errorMessage: Optional[str] = None
    jobDetails: Optional[JobDetailsTypeDef] = None
    lastAutomatedDiscoveryTime: Optional[datetime] = None
    objectCount: Optional[int] = None
    objectCountByEncryptionType: Optional[ObjectCountByEncryptionTypeTypeDef] = None
    sensitivityScore: Optional[int] = None
    sizeInBytes: Optional[int] = None
    sizeInBytesCompressed: Optional[int] = None
    unclassifiableObjectCount: Optional[ObjectLevelStatisticsTypeDef] = None
    unclassifiableObjectSizeInBytes: Optional[ObjectLevelStatisticsTypeDef] = None

class DescribeBucketsRequestRequestTypeDef(BaseModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[BucketSortCriteriaTypeDef] = None

class BucketStatisticsBySensitivityTypeDef(BaseModel):
    classificationError: Optional[SensitivityAggregationsTypeDef] = None
    notClassified: Optional[SensitivityAggregationsTypeDef] = None
    notSensitive: Optional[SensitivityAggregationsTypeDef] = None
    sensitive: Optional[SensitivityAggregationsTypeDef] = None

class ClassificationExportConfigurationTypeDef(BaseModel):
    s3Destination: Optional[S3DestinationTypeDef] = None

class ListClassificationScopesResponseTypeDef(BaseModel):
    classificationScopes: List[ClassificationScopeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDataIdentifierRequestRequestTypeDef(BaseModel):
    name: str
    regex: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    ignoreWords: Optional[Sequence[str]] = None
    keywords: Optional[Sequence[str]] = None
    maximumMatchDistance: Optional[int] = None
    severityLevels: Optional[Sequence[SeverityLevelTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class GetCustomDataIdentifierResponseTypeDef(BaseModel):
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
    severityLevels: List[SeverityLevelTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInvitationsResponseTypeDef(BaseModel):
    unprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineInvitationsResponseTypeDef(BaseModel):
    unprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvitationsResponseTypeDef(BaseModel):
    unprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FindingCriteriaOutputTypeDef(BaseModel):
    criterion: Optional[Dict[str, CriterionAdditionalPropertiesOutputTypeDef]] = None

class FindingCriteriaTypeDef(BaseModel):
    criterion: Optional[Mapping[str, CriterionAdditionalPropertiesTypeDef]] = None

class ListCustomDataIdentifiersResponseTypeDef(BaseModel):
    items: List[CustomDataIdentifierSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBucketsRequestDescribeBucketsPaginateTypeDef(BaseModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]] = None
    sortCriteria: Optional[BucketSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAllowListsRequestListAllowListsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAutomatedDiscoveryAccountsRequestListAutomatedDiscoveryAccountsPaginateTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClassificationScopesRequestListClassificationScopesPaginateTypeDef(BaseModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInvitationsRequestListInvitationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersRequestListMembersPaginateTypeDef(BaseModel):
    onlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSensitiveDataOccurrencesResponseTypeDef(BaseModel):
    error: str
    sensitiveDataOccurrences: Dict[str, List[DetectedDataDetailsTypeDef]]
    status: RevealRequestStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceProfileDetectionsResponseTypeDef(BaseModel):
    detections: List[DetectionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsFiltersResponseTypeDef(BaseModel):
    findingsFilterListItems: List[FindingsFilterListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdministratorAccountResponseTypeDef(BaseModel):
    administrator: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMasterAccountResponseTypeDef(BaseModel):
    master: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(BaseModel):
    invitations: List[InvitationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingStatisticsResponseTypeDef(BaseModel):
    countsByGroup: List[GroupCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsPublicationConfigurationResponseTypeDef(BaseModel):
    securityHubConfiguration: SecurityHubConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutFindingsPublicationConfigurationRequestRequestTypeDef(BaseModel):
    clientToken: Optional[str] = None
    securityHubConfiguration: Optional[SecurityHubConfigurationTypeDef] = None

class GetFindingsRequestRequestTypeDef(BaseModel):
    findingIds: Sequence[str]
    sortCriteria: Optional[SortCriteriaTypeDef] = None

class GetResourceProfileResponseTypeDef(BaseModel):
    profileUpdatedAt: datetime
    sensitivityScore: int
    sensitivityScoreOverridden: bool
    statistics: ResourceStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevealConfigurationResponseTypeDef(BaseModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: RetrievalConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRevealConfigurationResponseTypeDef(BaseModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: RetrievalConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef(BaseModel):
    findingId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSensitivityInspectionTemplateResponseTypeDef(BaseModel):
    description: str
    excludes: SensitivityInspectionTemplateExcludesOutputTypeDef
    includes: SensitivityInspectionTemplateIncludesOutputTypeDef
    name: str
    sensitivityInspectionTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef(BaseModel):
    filterBy: Optional[Sequence[UsageStatisticsFilterTypeDef]] = None
    sortBy: Optional[UsageStatisticsSortByTypeDef] = None
    timeRange: Optional[TimeRangeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsageStatisticsRequestRequestTypeDef(BaseModel):
    filterBy: Optional[Sequence[UsageStatisticsFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[UsageStatisticsSortByTypeDef] = None
    timeRange: Optional[TimeRangeType] = None

class GetUsageTotalsResponseTypeDef(BaseModel):
    timeRange: TimeRangeType
    usageTotals: List[UsageTotalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IpAddressDetailsTypeDef(BaseModel):
    ipAddressV4: Optional[str] = None
    ipCity: Optional[IpCityTypeDef] = None
    ipCountry: Optional[IpCountryTypeDef] = None
    ipGeoLocation: Optional[IpGeoLocationTypeDef] = None
    ipOwner: Optional[IpOwnerTypeDef] = None

class JobScheduleFrequencyOutputTypeDef(BaseModel):
    dailySchedule: Optional[Dict[str, Any]] = None
    monthlySchedule: Optional[MonthlyScheduleTypeDef] = None
    weeklySchedule: Optional[WeeklyScheduleTypeDef] = None

class JobScheduleFrequencyTypeDef(BaseModel):
    dailySchedule: Optional[Mapping[str, Any]] = None
    monthlySchedule: Optional[MonthlyScheduleTypeDef] = None
    weeklySchedule: Optional[WeeklyScheduleTypeDef] = None

class ListJobsFilterCriteriaTypeDef(BaseModel):
    excludes: Optional[Sequence[ListJobsFilterTermTypeDef]] = None
    includes: Optional[Sequence[ListJobsFilterTermTypeDef]] = None

class ListManagedDataIdentifiersResponseTypeDef(BaseModel):
    items: List[ManagedDataIdentifierSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseModel):
    members: List[MemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceProfileArtifactsResponseTypeDef(BaseModel):
    artifacts: List[ResourceProfileArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSensitivityInspectionTemplatesResponseTypeDef(BaseModel):
    nextToken: str
    sensitivityInspectionTemplates: List[SensitivityInspectionTemplatesEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PageTypeDef(BaseModel):
    lineRange: Optional[RangeTypeDef] = None
    offsetRange: Optional[RangeTypeDef] = None
    pageNumber: Optional[int] = None

class S3ObjectTypeDef(BaseModel):
    bucketArn: Optional[str] = None
    eTag: Optional[str] = None
    extension: Optional[str] = None
    key: Optional[str] = None
    lastModified: Optional[datetime] = None
    path: Optional[str] = None
    publicAccess: Optional[bool] = None
    serverSideEncryption: Optional[ServerSideEncryptionTypeDef] = None
    size: Optional[int] = None
    storageClass: Optional[StorageClassType] = None
    tags: Optional[List[KeyValuePairTypeDef]] = None
    versionId: Optional[str] = None

class S3ClassificationScopeTypeDef(BaseModel):
    excludes: S3ClassificationScopeExclusionTypeDef

class S3ClassificationScopeUpdateTypeDef(BaseModel):
    excludes: S3ClassificationScopeExclusionUpdateTypeDef

class SearchResourcesTagCriterionTypeDef(BaseModel):
    comparator: Optional[SearchResourcesComparatorType] = None
    tagValues: Optional[Sequence[SearchResourcesTagCriterionPairTypeDef]] = None

class UpdateSensitivityInspectionTemplateRequestRequestTypeDef(BaseModel):
    id: str
    description: Optional[str] = None
    excludes: Optional[SensitivityInspectionTemplateExcludesTypeDef] = None
    includes: Optional[SensitivityInspectionTemplateIncludesTypeDef] = None

class UsageByAccountTypeDef(BaseModel):
    currency: Optional[Literal["USD"]] = None
    estimatedCost: Optional[str] = None
    serviceLimit: Optional[ServiceLimitTypeDef] = None
    type: Optional[UsageTypeType] = None

class SessionContextTypeDef(BaseModel):
    attributes: Optional[SessionContextAttributesTypeDef] = None
    sessionIssuer: Optional[SessionIssuerTypeDef] = None

class UpdateResourceProfileDetectionsRequestRequestTypeDef(BaseModel):
    resourceArn: str
    suppressDataIdentifiers: Optional[Sequence[SuppressDataIdentifierTypeDef]] = None

class TagCriterionForJobOutputTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    tagValues: Optional[List[TagCriterionPairForJobTypeDef]] = None

class TagCriterionForJobTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    tagValues: Optional[Sequence[TagCriterionPairForJobTypeDef]] = None

class TagScopeTermOutputTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[str] = None
    tagValues: Optional[List[TagValuePairTypeDef]] = None
    target: Optional[Literal["S3_OBJECT"]] = None

class TagScopeTermTypeDef(BaseModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[str] = None
    tagValues: Optional[Sequence[TagValuePairTypeDef]] = None
    target: Optional[Literal["S3_OBJECT"]] = None

class UpdateRevealConfigurationRequestRequestTypeDef(BaseModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: Optional[UpdateRetrievalConfigurationTypeDef] = None

class CreateAllowListRequestRequestTypeDef(BaseModel):
    clientToken: str
    criteria: AllowListCriteriaTypeDef
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetAllowListResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    criteria: AllowListCriteriaTypeDef
    description: str
    id: str
    name: str
    status: AllowListStatusTypeDef
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAllowListRequestRequestTypeDef(BaseModel):
    criteria: AllowListCriteriaTypeDef
    id: str
    name: str
    description: Optional[str] = None

class BucketPermissionConfigurationTypeDef(BaseModel):
    accountLevelPermissions: Optional[AccountLevelPermissionsTypeDef] = None
    bucketLevelPermissions: Optional[BucketLevelPermissionsTypeDef] = None

class MatchingResourceTypeDef(BaseModel):
    matchingBucket: Optional[MatchingBucketTypeDef] = None

class GetBucketStatisticsResponseTypeDef(BaseModel):
    bucketCount: int
    bucketCountByEffectivePermission: BucketCountByEffectivePermissionTypeDef
    bucketCountByEncryptionType: BucketCountByEncryptionTypeTypeDef
    bucketCountByObjectEncryptionRequirement: BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef
    bucketCountBySharedAccessType: BucketCountBySharedAccessTypeTypeDef
    bucketStatisticsBySensitivity: BucketStatisticsBySensitivityTypeDef
    classifiableObjectCount: int
    classifiableSizeInBytes: int
    lastUpdated: datetime
    objectCount: int
    sizeInBytes: int
    sizeInBytesCompressed: int
    unclassifiableObjectCount: ObjectLevelStatisticsTypeDef
    unclassifiableObjectSizeInBytes: ObjectLevelStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClassificationExportConfigurationResponseTypeDef(BaseModel):
    configuration: ClassificationExportConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutClassificationExportConfigurationRequestRequestTypeDef(BaseModel):
    configuration: ClassificationExportConfigurationTypeDef

class PutClassificationExportConfigurationResponseTypeDef(BaseModel):
    configuration: ClassificationExportConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsFilterResponseTypeDef(BaseModel):
    action: FindingsFilterActionType
    arn: str
    description: str
    findingCriteria: FindingCriteriaOutputTypeDef
    id: str
    name: str
    position: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingsFilterRequestRequestTypeDef(BaseModel):
    action: FindingsFilterActionType
    findingCriteria: FindingCriteriaTypeDef
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    position: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class GetFindingStatisticsRequestRequestTypeDef(BaseModel):
    groupBy: GroupByType
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    size: Optional[int] = None
    sortCriteria: Optional[FindingStatisticsSortCriteriaTypeDef] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseModel):
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseModel):
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None

class UpdateFindingsFilterRequestRequestTypeDef(BaseModel):
    id: str
    action: Optional[FindingsFilterActionType] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    name: Optional[str] = None
    position: Optional[int] = None

class ListClassificationJobsRequestListClassificationJobsPaginateTypeDef(BaseModel):
    filterCriteria: Optional[ListJobsFilterCriteriaTypeDef] = None
    sortCriteria: Optional[ListJobsSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClassificationJobsRequestRequestTypeDef(BaseModel):
    filterCriteria: Optional[ListJobsFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[ListJobsSortCriteriaTypeDef] = None

class OccurrencesTypeDef(BaseModel):
    cells: Optional[List[CellTypeDef]] = None
    lineRanges: Optional[List[RangeTypeDef]] = None
    offsetRanges: Optional[List[RangeTypeDef]] = None
    pages: Optional[List[PageTypeDef]] = None
    records: Optional[List[RecordTypeDef]] = None

class GetClassificationScopeResponseTypeDef(BaseModel):
    id: str
    name: str
    s3: S3ClassificationScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClassificationScopeRequestRequestTypeDef(BaseModel):
    id: str
    s3: Optional[S3ClassificationScopeUpdateTypeDef] = None

class SearchResourcesCriteriaTypeDef(BaseModel):
    simpleCriterion: Optional[SearchResourcesSimpleCriterionTypeDef] = None
    tagCriterion: Optional[SearchResourcesTagCriterionTypeDef] = None

class UsageRecordTypeDef(BaseModel):
    accountId: Optional[str] = None
    automatedDiscoveryFreeTrialStartDate: Optional[datetime] = None
    freeTrialStartDate: Optional[datetime] = None
    usage: Optional[List[UsageByAccountTypeDef]] = None

class AssumedRoleTypeDef(BaseModel):
    accessKeyId: Optional[str] = None
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    sessionContext: Optional[SessionContextTypeDef] = None

class FederatedUserTypeDef(BaseModel):
    accessKeyId: Optional[str] = None
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    sessionContext: Optional[SessionContextTypeDef] = None

class CriteriaForJobOutputTypeDef(BaseModel):
    simpleCriterion: Optional[SimpleCriterionForJobOutputTypeDef] = None
    tagCriterion: Optional[TagCriterionForJobOutputTypeDef] = None

class CriteriaForJobTypeDef(BaseModel):
    simpleCriterion: Optional[SimpleCriterionForJobTypeDef] = None
    tagCriterion: Optional[TagCriterionForJobTypeDef] = None

class JobScopeTermOutputTypeDef(BaseModel):
    simpleScopeTerm: Optional[SimpleScopeTermOutputTypeDef] = None
    tagScopeTerm: Optional[TagScopeTermOutputTypeDef] = None

class JobScopeTermTypeDef(BaseModel):
    simpleScopeTerm: Optional[SimpleScopeTermTypeDef] = None
    tagScopeTerm: Optional[TagScopeTermTypeDef] = None

class BucketPublicAccessTypeDef(BaseModel):
    effectivePermission: Optional[EffectivePermissionType] = None
    permissionConfiguration: Optional[BucketPermissionConfigurationTypeDef] = None

class SearchResourcesResponseTypeDef(BaseModel):
    matchingResources: List[MatchingResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDetectionTypeDef(BaseModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    occurrences: Optional[OccurrencesTypeDef] = None

class DefaultDetectionTypeDef(BaseModel):
    count: Optional[int] = None
    occurrences: Optional[OccurrencesTypeDef] = None
    type: Optional[str] = None

class SearchResourcesCriteriaBlockTypeDef(BaseModel):
    and: Optional[Sequence[SearchResourcesCriteriaTypeDef]] = None

class GetUsageStatisticsResponseTypeDef(BaseModel):
    nextToken: str
    records: List[UsageRecordTypeDef]
    timeRange: TimeRangeType
    ResponseMetadata: ResponseMetadataTypeDef

class UserIdentityTypeDef(BaseModel):
    assumedRole: Optional[AssumedRoleTypeDef] = None
    awsAccount: Optional[AwsAccountTypeDef] = None
    awsService: Optional[AwsServiceTypeDef] = None
    federatedUser: Optional[FederatedUserTypeDef] = None
    iamUser: Optional[IamUserTypeDef] = None
    root: Optional[UserIdentityRootTypeDef] = None
    type: Optional[UserIdentityTypeType] = None

class CriteriaBlockForJobOutputTypeDef(BaseModel):
    and: Optional[List[CriteriaForJobOutputTypeDef]] = None

class CriteriaBlockForJobTypeDef(BaseModel):
    and: Optional[Sequence[CriteriaForJobTypeDef]] = None

class JobScopingBlockOutputTypeDef(BaseModel):
    and: Optional[List[JobScopeTermOutputTypeDef]] = None

class JobScopingBlockTypeDef(BaseModel):
    and: Optional[Sequence[JobScopeTermTypeDef]] = None

class BucketMetadataTypeDef(BaseModel):
    accountId: Optional[str] = None
    allowsUnencryptedObjectUploads: Optional[AllowsUnencryptedObjectUploadsType] = None
    automatedDiscoveryMonitoringStatus: Optional[AutomatedDiscoveryMonitoringStatusType] = None
    bucketArn: Optional[str] = None
    bucketCreatedAt: Optional[datetime] = None
    bucketName: Optional[str] = None
    classifiableObjectCount: Optional[int] = None
    classifiableSizeInBytes: Optional[int] = None
    errorCode: Optional[Literal["ACCESS_DENIED"]] = None
    errorMessage: Optional[str] = None
    jobDetails: Optional[JobDetailsTypeDef] = None
    lastAutomatedDiscoveryTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None
    objectCount: Optional[int] = None
    objectCountByEncryptionType: Optional[ObjectCountByEncryptionTypeTypeDef] = None
    publicAccess: Optional[BucketPublicAccessTypeDef] = None
    region: Optional[str] = None
    replicationDetails: Optional[ReplicationDetailsTypeDef] = None
    sensitivityScore: Optional[int] = None
    serverSideEncryption: Optional[BucketServerSideEncryptionTypeDef] = None
    sharedAccess: Optional[SharedAccessType] = None
    sizeInBytes: Optional[int] = None
    sizeInBytesCompressed: Optional[int] = None
    tags: Optional[List[KeyValuePairTypeDef]] = None
    unclassifiableObjectCount: Optional[ObjectLevelStatisticsTypeDef] = None
    unclassifiableObjectSizeInBytes: Optional[ObjectLevelStatisticsTypeDef] = None
    versioning: Optional[bool] = None

class S3BucketTypeDef(BaseModel):
    allowsUnencryptedObjectUploads: Optional[AllowsUnencryptedObjectUploadsType] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    defaultServerSideEncryption: Optional[ServerSideEncryptionTypeDef] = None
    name: Optional[str] = None
    owner: Optional[S3BucketOwnerTypeDef] = None
    publicAccess: Optional[BucketPublicAccessTypeDef] = None
    tags: Optional[List[KeyValuePairTypeDef]] = None

class CustomDataIdentifiersTypeDef(BaseModel):
    detections: Optional[List[CustomDetectionTypeDef]] = None
    totalCount: Optional[int] = None

class SensitiveDataItemTypeDef(BaseModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    detections: Optional[List[DefaultDetectionTypeDef]] = None
    totalCount: Optional[int] = None

class SearchResourcesBucketCriteriaTypeDef(BaseModel):
    excludes: Optional[SearchResourcesCriteriaBlockTypeDef] = None
    includes: Optional[SearchResourcesCriteriaBlockTypeDef] = None

class FindingActorTypeDef(BaseModel):
    domainDetails: Optional[DomainDetailsTypeDef] = None
    ipAddressDetails: Optional[IpAddressDetailsTypeDef] = None
    userIdentity: Optional[UserIdentityTypeDef] = None

class S3BucketCriteriaForJobOutputTypeDef(BaseModel):
    excludes: Optional[CriteriaBlockForJobOutputTypeDef] = None
    includes: Optional[CriteriaBlockForJobOutputTypeDef] = None

class S3BucketCriteriaForJobTypeDef(BaseModel):
    excludes: Optional[CriteriaBlockForJobTypeDef] = None
    includes: Optional[CriteriaBlockForJobTypeDef] = None

class ScopingOutputTypeDef(BaseModel):
    excludes: Optional[JobScopingBlockOutputTypeDef] = None
    includes: Optional[JobScopingBlockOutputTypeDef] = None

class ScopingTypeDef(BaseModel):
    excludes: Optional[JobScopingBlockTypeDef] = None
    includes: Optional[JobScopingBlockTypeDef] = None

class DescribeBucketsResponseTypeDef(BaseModel):
    buckets: List[BucketMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourcesAffectedTypeDef(BaseModel):
    s3Bucket: Optional[S3BucketTypeDef] = None
    s3Object: Optional[S3ObjectTypeDef] = None

class ClassificationResultTypeDef(BaseModel):
    additionalOccurrences: Optional[bool] = None
    customDataIdentifiers: Optional[CustomDataIdentifiersTypeDef] = None
    mimeType: Optional[str] = None
    sensitiveData: Optional[List[SensitiveDataItemTypeDef]] = None
    sizeClassified: Optional[int] = None
    status: Optional[ClassificationResultStatusTypeDef] = None

class SearchResourcesRequestRequestTypeDef(BaseModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SearchResourcesSortCriteriaTypeDef] = None

class SearchResourcesRequestSearchResourcesPaginateTypeDef(BaseModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteriaTypeDef] = None
    sortCriteria: Optional[SearchResourcesSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PolicyDetailsTypeDef(BaseModel):
    action: Optional[FindingActionTypeDef] = None
    actor: Optional[FindingActorTypeDef] = None

class JobSummaryTypeDef(BaseModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobOutputTypeDef] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJobOutputTypeDef]] = None
    createdAt: Optional[datetime] = None
    jobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    jobType: Optional[JobTypeType] = None
    lastRunErrorStatus: Optional[LastRunErrorStatusTypeDef] = None
    name: Optional[str] = None
    userPausedDetails: Optional[UserPausedDetailsTypeDef] = None

class S3JobDefinitionOutputTypeDef(BaseModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobOutputTypeDef] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJobOutputTypeDef]] = None
    scoping: Optional[ScopingOutputTypeDef] = None

class S3JobDefinitionTypeDef(BaseModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobTypeDef] = None
    bucketDefinitions: Optional[Sequence[S3BucketDefinitionForJobTypeDef]] = None
    scoping: Optional[ScopingTypeDef] = None

class ClassificationDetailsTypeDef(BaseModel):
    detailedResultsLocation: Optional[str] = None
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    originType: Optional[OriginTypeType] = None
    result: Optional[ClassificationResultTypeDef] = None

class ListClassificationJobsResponseTypeDef(BaseModel):
    items: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClassificationJobResponseTypeDef(BaseModel):
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
    lastRunErrorStatus: LastRunErrorStatusTypeDef
    lastRunTime: datetime
    managedDataIdentifierIds: List[str]
    managedDataIdentifierSelector: ManagedDataIdentifierSelectorType
    name: str
    s3JobDefinition: S3JobDefinitionOutputTypeDef
    samplingPercentage: int
    scheduleFrequency: JobScheduleFrequencyOutputTypeDef
    statistics: StatisticsTypeDef
    tags: Dict[str, str]
    userPausedDetails: UserPausedDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClassificationJobRequestRequestTypeDef(BaseModel):
    clientToken: str
    jobType: JobTypeType
    name: str
    s3JobDefinition: S3JobDefinitionTypeDef
    allowListIds: Optional[Sequence[str]] = None
    customDataIdentifierIds: Optional[Sequence[str]] = None
    description: Optional[str] = None
    initialRun: Optional[bool] = None
    managedDataIdentifierIds: Optional[Sequence[str]] = None
    managedDataIdentifierSelector: Optional[ManagedDataIdentifierSelectorType] = None
    samplingPercentage: Optional[int] = None
    scheduleFrequency: Optional[JobScheduleFrequencyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class FindingTypeDef(BaseModel):
    accountId: Optional[str] = None
    archived: Optional[bool] = None
    category: Optional[FindingCategoryType] = None
    classificationDetails: Optional[ClassificationDetailsTypeDef] = None
    count: Optional[int] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    partition: Optional[str] = None
    policyDetails: Optional[PolicyDetailsTypeDef] = None
    region: Optional[str] = None
    resourcesAffected: Optional[ResourcesAffectedTypeDef] = None
    sample: Optional[bool] = None
    schemaVersion: Optional[str] = None
    severity: Optional[SeverityTypeDef] = None
    title: Optional[str] = None
    type: Optional[FindingTypeType] = None
    updatedAt: Optional[datetime] = None

class GetFindingsResponseTypeDef(BaseModel):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

