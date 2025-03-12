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
from aws_resource_validator.pydantic_models.macie2_constants import *

class AcceptInvitationRequestTypeDef(BaseValidatorModel):
    invitationId: str
    administratorAccountId: Optional[str] = None
    masterAccount: Optional[str] = None


class AccessControlListTypeDef(BaseValidatorModel):
    allowsPublicReadAccess: Optional[bool] = None
    allowsPublicWriteAccess: Optional[bool] = None


class AccountDetailTypeDef(BaseValidatorModel):
    accountId: str
    email: str


class BlockPublicAccessTypeDef(BaseValidatorModel):
    blockPublicAcls: Optional[bool] = None
    blockPublicPolicy: Optional[bool] = None
    ignorePublicAcls: Optional[bool] = None
    restrictPublicBuckets: Optional[bool] = None


class AdminAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[AdminStatusType] = None


class S3WordsListTypeDef(BaseValidatorModel):
    bucketName: str
    objectKey: str


class AllowListStatusTypeDef(BaseValidatorModel):
    code: AllowListStatusCodeType
    description: Optional[str] = None


class ApiCallDetailsTypeDef(BaseValidatorModel):
    api: Optional[str] = None
    apiServiceName: Optional[str] = None
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None


class AutomatedDiscoveryAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[AutomatedDiscoveryAccountStatusType] = None


class AutomatedDiscoveryAccountUpdateErrorTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    errorCode: Optional[AutomatedDiscoveryAccountUpdateErrorCodeType] = None


class AutomatedDiscoveryAccountUpdateTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[AutomatedDiscoveryAccountStatusType] = None


class AwsAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    principalId: Optional[str] = None


class AwsServiceTypeDef(BaseValidatorModel):
    invokedBy: Optional[str] = None


class BatchGetCustomDataIdentifiersRequestTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BucketCountByEffectivePermissionTypeDef(BaseValidatorModel):
    publiclyAccessible: Optional[int] = None
    publiclyReadable: Optional[int] = None
    publiclyWritable: Optional[int] = None
    unknown: Optional[int] = None


class BucketCountByEncryptionTypeTypeDef(BaseValidatorModel):
    kmsManaged: Optional[int] = None
    s3Managed: Optional[int] = None
    unencrypted: Optional[int] = None
    unknown: Optional[int] = None


class BucketCountBySharedAccessTypeTypeDef(BaseValidatorModel):
    external: Optional[int] = None
    internal: Optional[int] = None
    notShared: Optional[int] = None
    unknown: Optional[int] = None


class BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef(BaseValidatorModel):
    allowsUnencryptedObjectUploads: Optional[int] = None
    deniesUnencryptedObjectUploads: Optional[int] = None
    unknown: Optional[int] = None


class BucketCriteriaAdditionalPropertiesTypeDef(BaseValidatorModel):
    eq: Optional[Sequence[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[Sequence[str]] = None
    prefix: Optional[str] = None


class BucketPolicyTypeDef(BaseValidatorModel):
    allowsPublicReadAccess: Optional[bool] = None
    allowsPublicWriteAccess: Optional[bool] = None


class JobDetailsTypeDef(BaseValidatorModel):
    isDefinedInJob: Optional[IsDefinedInJobType] = None
    isMonitoredByJob: Optional[IsMonitoredByJobType] = None
    lastJobId: Optional[str] = None
    lastJobRunTime: Optional[datetime] = None


class KeyValuePairTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ObjectCountByEncryptionTypeTypeDef(BaseValidatorModel):
    customerManaged: Optional[int] = None
    kmsManaged: Optional[int] = None
    s3Managed: Optional[int] = None
    unencrypted: Optional[int] = None
    unknown: Optional[int] = None


class ObjectLevelStatisticsTypeDef(BaseValidatorModel):
    fileType: Optional[int] = None
    storageClass: Optional[int] = None
    total: Optional[int] = None


class ReplicationDetailsTypeDef(BaseValidatorModel):
    replicated: Optional[bool] = None
    replicatedExternally: Optional[bool] = None
    replicationAccounts: Optional[List[str]] = None


class BucketSortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class SensitivityAggregationsTypeDef(BaseValidatorModel):
    classifiableSizeInBytes: Optional[int] = None
    publiclyAccessibleCount: Optional[int] = None
    totalCount: Optional[int] = None
    totalSizeInBytes: Optional[int] = None


class CellTypeDef(BaseValidatorModel):
    cellReference: Optional[str] = None
    column: Optional[int] = None
    columnName: Optional[str] = None
    row: Optional[int] = None


class S3DestinationTypeDef(BaseValidatorModel):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: Optional[str] = None


class ClassificationResultStatusTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    reason: Optional[str] = None


class SeverityLevelTypeDef(BaseValidatorModel):
    occurrencesThreshold: int
    severity: DataIdentifierSeverityType


class CreateInvitationsRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]
    disableEmailNotification: Optional[bool] = None
    message: Optional[str] = None


class UnprocessedAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None


class CreateSampleFindingsRequestTypeDef(BaseValidatorModel):
    findingTypes: Optional[Sequence[FindingTypeType]] = None


class SimpleCriterionForJobOutputTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[SimpleCriterionKeyForJobType] = None
    values: Optional[List[str]] = None


class SimpleCriterionForJobTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[SimpleCriterionKeyForJobType] = None
    values: Optional[Sequence[str]] = None


class CriterionAdditionalPropertiesOutputTypeDef(BaseValidatorModel):
    eq: Optional[List[str]] = None
    eqExactMatch: Optional[List[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[List[str]] = None


class CriterionAdditionalPropertiesTypeDef(BaseValidatorModel):
    eq: Optional[Sequence[str]] = None
    eqExactMatch: Optional[Sequence[str]] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    neq: Optional[Sequence[str]] = None


class DeclineInvitationsRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]


class DeleteInvitationsRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeClassificationJobRequestTypeDef(BaseValidatorModel):
    jobId: str


class LastRunErrorStatusTypeDef(BaseValidatorModel):
    code: Optional[LastRunErrorStatusCodeType] = None


class StatisticsTypeDef(BaseValidatorModel):
    approximateNumberOfObjectsToProcess: Optional[float] = None
    numberOfRuns: Optional[float] = None


class UserPausedDetailsTypeDef(BaseValidatorModel):
    jobExpiresAt: Optional[datetime] = None
    jobImminentExpirationHealthEventArn: Optional[str] = None
    jobPausedAt: Optional[datetime] = None


class DetectedDataDetailsTypeDef(BaseValidatorModel):
    value: str


class DisableOrganizationAdminAccountRequestTypeDef(BaseValidatorModel):
    adminAccountId: str


class DomainDetailsTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None


class EnableMacieRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None


class EnableOrganizationAdminAccountRequestTypeDef(BaseValidatorModel):
    adminAccountId: str
    clientToken: Optional[str] = None


class FindingStatisticsSortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[FindingStatisticsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None


class SeverityTypeDef(BaseValidatorModel):
    description: Optional[SeverityDescriptionType] = None
    score: Optional[int] = None


class InvitationTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    invitationId: Optional[str] = None
    invitedAt: Optional[datetime] = None
    relationshipStatus: Optional[RelationshipStatusType] = None


class GetBucketStatisticsRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class GroupCountTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    groupKey: Optional[str] = None


class SecurityHubConfigurationTypeDef(BaseValidatorModel):
    publishClassificationFindings: bool
    publishPolicyFindings: bool


class SortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class GetResourceProfileRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ResourceStatisticsTypeDef(BaseValidatorModel):
    totalBytesClassified: Optional[int] = None
    totalDetections: Optional[int] = None
    totalDetectionsSuppressed: Optional[int] = None
    totalItemsClassified: Optional[int] = None
    totalItemsSensitive: Optional[int] = None
    totalItemsSkipped: Optional[int] = None
    totalItemsSkippedInvalidEncryption: Optional[int] = None
    totalItemsSkippedInvalidKms: Optional[int] = None
    totalItemsSkippedPermissionDenied: Optional[int] = None


class RetrievalConfigurationTypeDef(BaseValidatorModel):
    retrievalMode: RetrievalModeType
    externalId: Optional[str] = None
    roleName: Optional[str] = None


class RevealConfigurationTypeDef(BaseValidatorModel):
    status: RevealStatusType
    kmsKeyId: Optional[str] = None


class GetSensitiveDataOccurrencesAvailabilityRequestTypeDef(BaseValidatorModel):
    findingId: str


class GetSensitiveDataOccurrencesRequestTypeDef(BaseValidatorModel):
    findingId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class SensitivityInspectionTemplateExcludesOutputTypeDef(BaseValidatorModel):
    managedDataIdentifierIds: Optional[List[str]] = None


class SensitivityInspectionTemplateIncludesOutputTypeDef(BaseValidatorModel):
    allowListIds: Optional[List[str]] = None
    customDataIdentifierIds: Optional[List[str]] = None
    managedDataIdentifierIds: Optional[List[str]] = None


class UsageStatisticsFilterTypeDef(BaseValidatorModel):
    comparator: Optional[UsageStatisticsFilterComparatorType] = None
    key: Optional[UsageStatisticsFilterKeyType] = None
    values: Optional[Sequence[str]] = None


class UsageStatisticsSortByTypeDef(BaseValidatorModel):
    key: Optional[UsageStatisticsSortKeyType] = None
    orderBy: Optional[OrderByType] = None


class GetUsageTotalsRequestTypeDef(BaseValidatorModel):
    timeRange: Optional[str] = None


class IamUserTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    userName: Optional[str] = None


class IpCityTypeDef(BaseValidatorModel):
    name: Optional[str] = None


class IpCountryTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None


class IpGeoLocationTypeDef(BaseValidatorModel):
    lat: Optional[float] = None
    lon: Optional[float] = None


class IpOwnerTypeDef(BaseValidatorModel):
    asn: Optional[str] = None
    asnOrg: Optional[str] = None
    isp: Optional[str] = None
    org: Optional[str] = None


class MonthlyScheduleTypeDef(BaseValidatorModel):
    dayOfMonth: Optional[int] = None


class WeeklyScheduleTypeDef(BaseValidatorModel):
    dayOfWeek: Optional[DayOfWeekType] = None


class SimpleScopeTermOutputTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ScopeFilterKeyType] = None
    values: Optional[List[str]] = None


class SimpleScopeTermTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ScopeFilterKeyType] = None
    values: Optional[Sequence[str]] = None


class S3BucketDefinitionForJobOutputTypeDef(BaseValidatorModel):
    accountId: str
    buckets: List[str]


class ListAllowListsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAutomatedDiscoveryAccountsRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsSortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[ListJobsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None


class ListClassificationScopesRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None


class ListCustomDataIdentifiersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFindingsFiltersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInvitationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsFilterTermTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ListJobsFilterKeyType] = None
    values: Optional[Sequence[str]] = None


class ListManagedDataIdentifiersRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListMembersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    onlyAssociated: Optional[str] = None


class MemberTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    administratorAccountId: Optional[str] = None
    arn: Optional[str] = None
    email: Optional[str] = None
    invitedAt: Optional[datetime] = None
    masterAccountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None


class ListOrganizationAdminAccountsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListResourceProfileArtifactsRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


class ResourceProfileArtifactTypeDef(BaseValidatorModel):
    arn: str
    classificationResultStatus: str
    sensitive: Optional[bool] = None


class ListResourceProfileDetectionsRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSensitivityInspectionTemplatesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class RangeTypeDef(BaseValidatorModel):
    end: Optional[int] = None
    start: Optional[int] = None
    startColumn: Optional[int] = None


class RecordTypeDef(BaseValidatorModel):
    jsonPath: Optional[str] = None
    recordIndex: Optional[int] = None


class S3BucketDefinitionForJobTypeDef(BaseValidatorModel):
    accountId: str
    buckets: Sequence[str]


class ServerSideEncryptionTypeDef(BaseValidatorModel):
    encryptionType: Optional[EncryptionTypeType] = None
    kmsMasterKeyId: Optional[str] = None


class S3ClassificationScopeExclusionTypeDef(BaseValidatorModel):
    bucketNames: List[str]


class S3ClassificationScopeExclusionUpdateTypeDef(BaseValidatorModel):
    bucketNames: Sequence[str]
    operation: ClassificationScopeUpdateOperationType


class SearchResourcesSimpleCriterionTypeDef(BaseValidatorModel):
    comparator: Optional[SearchResourcesComparatorType] = None
    key: Optional[SearchResourcesSimpleCriterionKeyType] = None
    values: Optional[Sequence[str]] = None


class SearchResourcesSortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[SearchResourcesSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None


class SearchResourcesTagCriterionPairTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class SensitivityInspectionTemplateExcludesTypeDef(BaseValidatorModel):
    managedDataIdentifierIds: Optional[Sequence[str]] = None


class SensitivityInspectionTemplateIncludesTypeDef(BaseValidatorModel):
    allowListIds: Optional[Sequence[str]] = None
    customDataIdentifierIds: Optional[Sequence[str]] = None
    managedDataIdentifierIds: Optional[Sequence[str]] = None


class ServiceLimitTypeDef(BaseValidatorModel):
    isServiceLimited: Optional[bool] = None
    unit: Optional[Literal["TERABYTES"]] = None
    value: Optional[int] = None


class SessionContextAttributesTypeDef(BaseValidatorModel):
    creationDate: Optional[datetime] = None
    mfaAuthenticated: Optional[bool] = None


class TagCriterionPairForJobTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TagValuePairTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class TestCustomDataIdentifierRequestTypeDef(BaseValidatorModel):
    regex: str
    sampleText: str
    ignoreWords: Optional[Sequence[str]] = None
    keywords: Optional[Sequence[str]] = None
    maximumMatchDistance: Optional[int] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAutomatedDiscoveryConfigurationRequestTypeDef(BaseValidatorModel):
    status: AutomatedDiscoveryStatusType
    autoEnableOrganizationMembers: Optional[AutoEnableModeType] = None


class UpdateClassificationJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    jobStatus: JobStatusType


class UpdateMacieSessionRequestTypeDef(BaseValidatorModel):
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None


class UpdateOrganizationConfigurationRequestTypeDef(BaseValidatorModel):
    autoEnable: bool


class UpdateResourceProfileRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    sensitivityScoreOverride: Optional[int] = None


class UpdateRetrievalConfigurationTypeDef(BaseValidatorModel):
    retrievalMode: RetrievalModeType
    roleName: Optional[str] = None


class UserIdentityRootTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None


class CreateMemberRequestTypeDef(BaseValidatorModel):
    account: AccountDetailTypeDef
    tags: Optional[Mapping[str, str]] = None


class AccountLevelPermissionsTypeDef(BaseValidatorModel):
    blockPublicAccess: Optional[BlockPublicAccessTypeDef] = None


class AllowListCriteriaTypeDef(BaseValidatorModel):
    regex: Optional[str] = None
    s3WordsList: Optional[S3WordsListTypeDef] = None


class FindingActionTypeDef(BaseValidatorModel):
    actionType: Optional[Literal["AWS_API_CALL"]] = None
    apiCallDetails: Optional[ApiCallDetailsTypeDef] = None


class BatchUpdateAutomatedDiscoveryAccountsRequestTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[AutomatedDiscoveryAccountUpdateTypeDef]] = None


class BatchGetCustomDataIdentifierSummaryTypeDef(BaseValidatorModel):
    pass


class BatchGetCustomDataIdentifiersResponseTypeDef(BaseValidatorModel):
    customDataIdentifiers: List[BatchGetCustomDataIdentifierSummaryTypeDef]
    notFoundIdentifierIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef(BaseValidatorModel):
    errors: List[AutomatedDiscoveryAccountUpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateClassificationJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomDataIdentifierResponseTypeDef(BaseValidatorModel):
    customDataIdentifierId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMemberResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    autoEnable: bool
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetAutomatedDiscoveryConfigurationResponseTypeDef(BaseValidatorModel):
    autoEnableOrganizationMembers: AutoEnableModeType
    classificationScopeId: str
    disabledAt: datetime
    firstEnabledAt: datetime
    lastUpdatedAt: datetime
    sensitivityInspectionTemplateId: str
    status: AutomatedDiscoveryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetInvitationsCountResponseTypeDef(BaseValidatorModel):
    invitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetMacieSessionResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    findingPublishingFrequency: FindingPublishingFrequencyType
    serviceRole: str
    status: MacieStatusType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetMemberResponseTypeDef(BaseValidatorModel):
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


class GetSensitiveDataOccurrencesAvailabilityResponseTypeDef(BaseValidatorModel):
    code: AvailabilityCodeType
    reasons: List[UnavailabilityReasonCodeType]
    ResponseMetadata: ResponseMetadataTypeDef


class AllowListSummaryTypeDef(BaseValidatorModel):
    pass


class ListAllowListsResponseTypeDef(BaseValidatorModel):
    allowLists: List[AllowListSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAutomatedDiscoveryAccountsResponseTypeDef(BaseValidatorModel):
    items: List[AutomatedDiscoveryAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFindingsResponseTypeDef(BaseValidatorModel):
    findingIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListOrganizationAdminAccountsResponseTypeDef(BaseValidatorModel):
    adminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class TestCustomDataIdentifierResponseTypeDef(BaseValidatorModel):
    matchCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class BucketLevelPermissionsTypeDef(BaseValidatorModel):
    accessControlList: Optional[AccessControlListTypeDef] = None
    blockPublicAccess: Optional[BlockPublicAccessTypeDef] = None
    bucketPolicy: Optional[BucketPolicyTypeDef] = None


class MatchingBucketTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    automatedDiscoveryMonitoringStatus: Optional[AutomatedDiscoveryMonitoringStatusType] = None
    bucketName: Optional[str] = None
    classifiableObjectCount: Optional[int] = None
    classifiableSizeInBytes: Optional[int] = None
    errorCode: Optional[BucketMetadataErrorCodeType] = None
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


class DescribeBucketsRequestTypeDef(BaseValidatorModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[BucketSortCriteriaTypeDef] = None


class BucketStatisticsBySensitivityTypeDef(BaseValidatorModel):
    classificationError: Optional[SensitivityAggregationsTypeDef] = None
    notClassified: Optional[SensitivityAggregationsTypeDef] = None
    notSensitive: Optional[SensitivityAggregationsTypeDef] = None
    sensitive: Optional[SensitivityAggregationsTypeDef] = None


class ClassificationExportConfigurationTypeDef(BaseValidatorModel):
    s3Destination: Optional[S3DestinationTypeDef] = None


class ClassificationScopeSummaryTypeDef(BaseValidatorModel):
    pass


class ListClassificationScopesResponseTypeDef(BaseValidatorModel):
    classificationScopes: List[ClassificationScopeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateCustomDataIdentifierRequestTypeDef(BaseValidatorModel):
    name: str
    regex: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    ignoreWords: Optional[Sequence[str]] = None
    keywords: Optional[Sequence[str]] = None
    maximumMatchDistance: Optional[int] = None
    severityLevels: Optional[Sequence[SeverityLevelTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class CreateInvitationsResponseTypeDef(BaseValidatorModel):
    unprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeclineInvitationsResponseTypeDef(BaseValidatorModel):
    unprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInvitationsResponseTypeDef(BaseValidatorModel):
    unprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FindingCriteriaOutputTypeDef(BaseValidatorModel):
    criterion: Optional[Dict[str, CriterionAdditionalPropertiesOutputTypeDef]] = None


class FindingCriteriaTypeDef(BaseValidatorModel):
    criterion: Optional[Mapping[str, CriterionAdditionalPropertiesTypeDef]] = None


class CustomDataIdentifierSummaryTypeDef(BaseValidatorModel):
    pass


class ListCustomDataIdentifiersResponseTypeDef(BaseValidatorModel):
    items: List[CustomDataIdentifierSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeBucketsRequestPaginateTypeDef(BaseValidatorModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]] = None
    sortCriteria: Optional[BucketSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAllowListsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAutomatedDiscoveryAccountsRequestPaginateTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClassificationScopesRequestPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomDataIdentifiersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFindingsFiltersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInvitationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedDataIdentifiersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembersRequestPaginateTypeDef(BaseValidatorModel):
    onlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationAdminAccountsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceProfileArtifactsRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceProfileDetectionsRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSensitivityInspectionTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSensitiveDataOccurrencesResponseTypeDef(BaseValidatorModel):
    error: str
    sensitiveDataOccurrences: Dict[str, List[DetectedDataDetailsTypeDef]]
    status: RevealRequestStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DetectionTypeDef(BaseValidatorModel):
    pass


class ListResourceProfileDetectionsResponseTypeDef(BaseValidatorModel):
    detections: List[DetectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FindingsFilterListItemTypeDef(BaseValidatorModel):
    pass


class ListFindingsFiltersResponseTypeDef(BaseValidatorModel):
    findingsFilterListItems: List[FindingsFilterListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetAdministratorAccountResponseTypeDef(BaseValidatorModel):
    administrator: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMasterAccountResponseTypeDef(BaseValidatorModel):
    master: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListInvitationsResponseTypeDef(BaseValidatorModel):
    invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetFindingStatisticsResponseTypeDef(BaseValidatorModel):
    countsByGroup: List[GroupCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetFindingsPublicationConfigurationResponseTypeDef(BaseValidatorModel):
    securityHubConfiguration: SecurityHubConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutFindingsPublicationConfigurationRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    securityHubConfiguration: Optional[SecurityHubConfigurationTypeDef] = None


class GetFindingsRequestTypeDef(BaseValidatorModel):
    findingIds: Sequence[str]
    sortCriteria: Optional[SortCriteriaTypeDef] = None


class GetResourceProfileResponseTypeDef(BaseValidatorModel):
    profileUpdatedAt: datetime
    sensitivityScore: int
    sensitivityScoreOverridden: bool
    statistics: ResourceStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRevealConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: RetrievalConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRevealConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: RetrievalConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSensitiveDataOccurrencesRequestWaitTypeDef(BaseValidatorModel):
    findingId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetSensitivityInspectionTemplateResponseTypeDef(BaseValidatorModel):
    description: str
    excludes: SensitivityInspectionTemplateExcludesOutputTypeDef
    includes: SensitivityInspectionTemplateIncludesOutputTypeDef
    name: str
    sensitivityInspectionTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetUsageStatisticsRequestPaginateTypeDef(BaseValidatorModel):
    filterBy: Optional[Sequence[UsageStatisticsFilterTypeDef]] = None
    sortBy: Optional[UsageStatisticsSortByTypeDef] = None
    timeRange: Optional[TimeRangeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetUsageStatisticsRequestTypeDef(BaseValidatorModel):
    filterBy: Optional[Sequence[UsageStatisticsFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[UsageStatisticsSortByTypeDef] = None
    timeRange: Optional[TimeRangeType] = None


class UsageTotalTypeDef(BaseValidatorModel):
    pass


class GetUsageTotalsResponseTypeDef(BaseValidatorModel):
    timeRange: TimeRangeType
    usageTotals: List[UsageTotalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IpAddressDetailsTypeDef(BaseValidatorModel):
    ipAddressV4: Optional[str] = None
    ipCity: Optional[IpCityTypeDef] = None
    ipCountry: Optional[IpCountryTypeDef] = None
    ipGeoLocation: Optional[IpGeoLocationTypeDef] = None
    ipOwner: Optional[IpOwnerTypeDef] = None


class JobScheduleFrequencyOutputTypeDef(BaseValidatorModel):
    dailySchedule: Optional[Dict[str, Any]] = None
    monthlySchedule: Optional[MonthlyScheduleTypeDef] = None
    weeklySchedule: Optional[WeeklyScheduleTypeDef] = None


class JobScheduleFrequencyTypeDef(BaseValidatorModel):
    dailySchedule: Optional[Mapping[str, Any]] = None
    monthlySchedule: Optional[MonthlyScheduleTypeDef] = None
    weeklySchedule: Optional[WeeklyScheduleTypeDef] = None


class ListJobsFilterCriteriaTypeDef(BaseValidatorModel):
    excludes: Optional[Sequence[ListJobsFilterTermTypeDef]] = None
    includes: Optional[Sequence[ListJobsFilterTermTypeDef]] = None


class ManagedDataIdentifierSummaryTypeDef(BaseValidatorModel):
    pass


class ListManagedDataIdentifiersResponseTypeDef(BaseValidatorModel):
    items: List[ManagedDataIdentifierSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMembersResponseTypeDef(BaseValidatorModel):
    members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListResourceProfileArtifactsResponseTypeDef(BaseValidatorModel):
    artifacts: List[ResourceProfileArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SensitivityInspectionTemplatesEntryTypeDef(BaseValidatorModel):
    pass


class ListSensitivityInspectionTemplatesResponseTypeDef(BaseValidatorModel):
    sensitivityInspectionTemplates: List[SensitivityInspectionTemplatesEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PageTypeDef(BaseValidatorModel):
    lineRange: Optional[RangeTypeDef] = None
    offsetRange: Optional[RangeTypeDef] = None
    pageNumber: Optional[int] = None


class S3ObjectTypeDef(BaseValidatorModel):
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


class S3ClassificationScopeTypeDef(BaseValidatorModel):
    excludes: S3ClassificationScopeExclusionTypeDef


class S3ClassificationScopeUpdateTypeDef(BaseValidatorModel):
    excludes: S3ClassificationScopeExclusionUpdateTypeDef


class SearchResourcesTagCriterionTypeDef(BaseValidatorModel):
    comparator: Optional[SearchResourcesComparatorType] = None
    tagValues: Optional[Sequence[SearchResourcesTagCriterionPairTypeDef]] = None


class SessionIssuerTypeDef(BaseValidatorModel):
    pass


class SessionContextTypeDef(BaseValidatorModel):
    attributes: Optional[SessionContextAttributesTypeDef] = None
    sessionIssuer: Optional[SessionIssuerTypeDef] = None


class SuppressDataIdentifierTypeDef(BaseValidatorModel):
    pass


class UpdateResourceProfileDetectionsRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    suppressDataIdentifiers: Optional[Sequence[SuppressDataIdentifierTypeDef]] = None


class TagCriterionForJobOutputTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    tagValues: Optional[List[TagCriterionPairForJobTypeDef]] = None


class TagCriterionForJobTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    tagValues: Optional[Sequence[TagCriterionPairForJobTypeDef]] = None


class TagScopeTermOutputTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[str] = None
    tagValues: Optional[List[TagValuePairTypeDef]] = None
    target: Optional[Literal["S3_OBJECT"]] = None


class TagScopeTermTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[str] = None
    tagValues: Optional[Sequence[TagValuePairTypeDef]] = None
    target: Optional[Literal["S3_OBJECT"]] = None


class UpdateRevealConfigurationRequestTypeDef(BaseValidatorModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: Optional[UpdateRetrievalConfigurationTypeDef] = None


class CreateAllowListRequestTypeDef(BaseValidatorModel):
    clientToken: str
    criteria: AllowListCriteriaTypeDef
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class BucketPermissionConfigurationTypeDef(BaseValidatorModel):
    accountLevelPermissions: Optional[AccountLevelPermissionsTypeDef] = None
    bucketLevelPermissions: Optional[BucketLevelPermissionsTypeDef] = None


class MatchingResourceTypeDef(BaseValidatorModel):
    matchingBucket: Optional[MatchingBucketTypeDef] = None


class GetBucketStatisticsResponseTypeDef(BaseValidatorModel):
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


class GetClassificationExportConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: ClassificationExportConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutClassificationExportConfigurationRequestTypeDef(BaseValidatorModel):
    configuration: ClassificationExportConfigurationTypeDef


class PutClassificationExportConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: ClassificationExportConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListClassificationJobsRequestPaginateTypeDef(BaseValidatorModel):
    filterCriteria: Optional[ListJobsFilterCriteriaTypeDef] = None
    sortCriteria: Optional[ListJobsSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClassificationJobsRequestTypeDef(BaseValidatorModel):
    filterCriteria: Optional[ListJobsFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[ListJobsSortCriteriaTypeDef] = None


class OccurrencesTypeDef(BaseValidatorModel):
    cells: Optional[List[CellTypeDef]] = None
    lineRanges: Optional[List[RangeTypeDef]] = None
    offsetRanges: Optional[List[RangeTypeDef]] = None
    pages: Optional[List[PageTypeDef]] = None
    records: Optional[List[RecordTypeDef]] = None


class SearchResourcesCriteriaTypeDef(BaseValidatorModel):
    simpleCriterion: Optional[SearchResourcesSimpleCriterionTypeDef] = None
    tagCriterion: Optional[SearchResourcesTagCriterionTypeDef] = None


class UsageByAccountTypeDef(BaseValidatorModel):
    pass


class UsageRecordTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    automatedDiscoveryFreeTrialStartDate: Optional[datetime] = None
    freeTrialStartDate: Optional[datetime] = None
    usage: Optional[List[UsageByAccountTypeDef]] = None


class AssumedRoleTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    sessionContext: Optional[SessionContextTypeDef] = None


class FederatedUserTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    sessionContext: Optional[SessionContextTypeDef] = None


class CriteriaForJobOutputTypeDef(BaseValidatorModel):
    simpleCriterion: Optional[SimpleCriterionForJobOutputTypeDef] = None
    tagCriterion: Optional[TagCriterionForJobOutputTypeDef] = None


class CriteriaForJobTypeDef(BaseValidatorModel):
    simpleCriterion: Optional[SimpleCriterionForJobTypeDef] = None
    tagCriterion: Optional[TagCriterionForJobTypeDef] = None


class JobScopeTermOutputTypeDef(BaseValidatorModel):
    simpleScopeTerm: Optional[SimpleScopeTermOutputTypeDef] = None
    tagScopeTerm: Optional[TagScopeTermOutputTypeDef] = None


class JobScopeTermTypeDef(BaseValidatorModel):
    simpleScopeTerm: Optional[SimpleScopeTermTypeDef] = None
    tagScopeTerm: Optional[TagScopeTermTypeDef] = None


class BucketPublicAccessTypeDef(BaseValidatorModel):
    effectivePermission: Optional[EffectivePermissionType] = None
    permissionConfiguration: Optional[BucketPermissionConfigurationTypeDef] = None


class SearchResourcesResponseTypeDef(BaseValidatorModel):
    matchingResources: List[MatchingResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FindingCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class CreateFindingsFilterRequestTypeDef(BaseValidatorModel):
    action: FindingsFilterActionType
    findingCriteria: FindingCriteriaUnionTypeDef
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    position: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class GetFindingStatisticsRequestTypeDef(BaseValidatorModel):
    groupBy: GroupByType
    findingCriteria: Optional[FindingCriteriaUnionTypeDef] = None
    size: Optional[int] = None
    sortCriteria: Optional[FindingStatisticsSortCriteriaTypeDef] = None


class ListFindingsRequestPaginateTypeDef(BaseValidatorModel):
    findingCriteria: Optional[FindingCriteriaUnionTypeDef] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFindingsRequestTypeDef(BaseValidatorModel):
    findingCriteria: Optional[FindingCriteriaUnionTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None


class CustomDetectionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    occurrences: Optional[OccurrencesTypeDef] = None


class GetUsageStatisticsResponseTypeDef(BaseValidatorModel):
    records: List[UsageRecordTypeDef]
    timeRange: TimeRangeType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BucketServerSideEncryptionTypeDef(BaseValidatorModel):
    pass


class BucketMetadataTypeDef(BaseValidatorModel):
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


class S3BucketOwnerTypeDef(BaseValidatorModel):
    pass


class S3BucketTypeDef(BaseValidatorModel):
    allowsUnencryptedObjectUploads: Optional[AllowsUnencryptedObjectUploadsType] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    defaultServerSideEncryption: Optional[ServerSideEncryptionTypeDef] = None
    name: Optional[str] = None
    owner: Optional[S3BucketOwnerTypeDef] = None
    publicAccess: Optional[BucketPublicAccessTypeDef] = None
    tags: Optional[List[KeyValuePairTypeDef]] = None


class CustomDataIdentifiersTypeDef(BaseValidatorModel):
    detections: Optional[List[CustomDetectionTypeDef]] = None
    totalCount: Optional[int] = None


class DefaultDetectionTypeDef(BaseValidatorModel):
    pass


class SensitiveDataItemTypeDef(BaseValidatorModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    detections: Optional[List[DefaultDetectionTypeDef]] = None
    totalCount: Optional[int] = None


class SearchResourcesCriteriaBlockTypeDef(BaseValidatorModel):
    pass


class SearchResourcesBucketCriteriaTypeDef(BaseValidatorModel):
    excludes: Optional[SearchResourcesCriteriaBlockTypeDef] = None
    includes: Optional[SearchResourcesCriteriaBlockTypeDef] = None


class UserIdentityTypeDef(BaseValidatorModel):
    pass


class FindingActorTypeDef(BaseValidatorModel):
    domainDetails: Optional[DomainDetailsTypeDef] = None
    ipAddressDetails: Optional[IpAddressDetailsTypeDef] = None
    userIdentity: Optional[UserIdentityTypeDef] = None


class CriteriaBlockForJobOutputTypeDef(BaseValidatorModel):
    pass


class S3BucketCriteriaForJobOutputTypeDef(BaseValidatorModel):
    excludes: Optional[CriteriaBlockForJobOutputTypeDef] = None
    includes: Optional[CriteriaBlockForJobOutputTypeDef] = None


class CriteriaBlockForJobTypeDef(BaseValidatorModel):
    pass


class S3BucketCriteriaForJobTypeDef(BaseValidatorModel):
    excludes: Optional[CriteriaBlockForJobTypeDef] = None
    includes: Optional[CriteriaBlockForJobTypeDef] = None


class JobScopingBlockOutputTypeDef(BaseValidatorModel):
    pass


class ScopingOutputTypeDef(BaseValidatorModel):
    excludes: Optional[JobScopingBlockOutputTypeDef] = None
    includes: Optional[JobScopingBlockOutputTypeDef] = None


class JobScopingBlockTypeDef(BaseValidatorModel):
    pass


class ScopingTypeDef(BaseValidatorModel):
    excludes: Optional[JobScopingBlockTypeDef] = None
    includes: Optional[JobScopingBlockTypeDef] = None


class DescribeBucketsResponseTypeDef(BaseValidatorModel):
    buckets: List[BucketMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourcesAffectedTypeDef(BaseValidatorModel):
    s3Bucket: Optional[S3BucketTypeDef] = None
    s3Object: Optional[S3ObjectTypeDef] = None


class ClassificationResultTypeDef(BaseValidatorModel):
    additionalOccurrences: Optional[bool] = None
    customDataIdentifiers: Optional[CustomDataIdentifiersTypeDef] = None
    mimeType: Optional[str] = None
    sensitiveData: Optional[List[SensitiveDataItemTypeDef]] = None
    sizeClassified: Optional[int] = None
    status: Optional[ClassificationResultStatusTypeDef] = None


class SearchResourcesRequestPaginateTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteriaTypeDef] = None
    sortCriteria: Optional[SearchResourcesSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchResourcesRequestTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SearchResourcesSortCriteriaTypeDef] = None


class PolicyDetailsTypeDef(BaseValidatorModel):
    action: Optional[FindingActionTypeDef] = None
    actor: Optional[FindingActorTypeDef] = None


class JobSummaryTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobOutputTypeDef] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJobOutputTypeDef]] = None
    createdAt: Optional[datetime] = None
    jobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    jobType: Optional[JobTypeType] = None
    lastRunErrorStatus: Optional[LastRunErrorStatusTypeDef] = None
    name: Optional[str] = None
    userPausedDetails: Optional[UserPausedDetailsTypeDef] = None


class S3JobDefinitionOutputTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobOutputTypeDef] = None
    bucketDefinitions: Optional[List[S3BucketDefinitionForJobOutputTypeDef]] = None
    scoping: Optional[ScopingOutputTypeDef] = None


class S3JobDefinitionTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[S3BucketCriteriaForJobTypeDef] = None
    bucketDefinitions: Optional[Sequence[S3BucketDefinitionForJobTypeDef]] = None
    scoping: Optional[ScopingTypeDef] = None


class ClassificationDetailsTypeDef(BaseValidatorModel):
    detailedResultsLocation: Optional[str] = None
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    originType: Optional[OriginTypeType] = None
    result: Optional[ClassificationResultTypeDef] = None


class ListClassificationJobsResponseTypeDef(BaseValidatorModel):
    items: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeClassificationJobResponseTypeDef(BaseValidatorModel):
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


class S3JobDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class JobScheduleFrequencyUnionTypeDef(BaseValidatorModel):
    pass


class CreateClassificationJobRequestTypeDef(BaseValidatorModel):
    clientToken: str
    jobType: JobTypeType
    name: str
    s3JobDefinition: S3JobDefinitionUnionTypeDef
    allowListIds: Optional[Sequence[str]] = None
    customDataIdentifierIds: Optional[Sequence[str]] = None
    description: Optional[str] = None
    initialRun: Optional[bool] = None
    managedDataIdentifierIds: Optional[Sequence[str]] = None
    managedDataIdentifierSelector: Optional[ManagedDataIdentifierSelectorType] = None
    samplingPercentage: Optional[int] = None
    scheduleFrequency: Optional[JobScheduleFrequencyUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class FindingTypeDef(BaseValidatorModel):
    pass


class GetFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


