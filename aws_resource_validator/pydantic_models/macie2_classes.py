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
from aws_resource_validator.pydantic_models.macie2_constants import *

class AcceptInvitationRequestRequestTypeDef(BaseValidatorModel):
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

class AllowListSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None

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

class BatchGetCustomDataIdentifierSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    deleted: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class BatchGetCustomDataIdentifiersRequestRequestTypeDef(BaseValidatorModel):
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

class BucketServerSideEncryptionTypeDef(BaseValidatorModel):
    kmsMasterKeyId: Optional[str] = None
    type: Optional[TypeType] = None

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

class ClassificationScopeSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class SeverityLevelTypeDef(BaseValidatorModel):
    occurrencesThreshold: int
    severity: DataIdentifierSeverityType

class CreateInvitationsRequestRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]
    disableEmailNotification: Optional[bool] = None
    message: Optional[str] = None

class UnprocessedAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class CreateSampleFindingsRequestRequestTypeDef(BaseValidatorModel):
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

class CustomDataIdentifierSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class DeclineInvitationsRequestRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]

class DeleteAllowListRequestRequestTypeDef(BaseValidatorModel):
    id: str
    ignoreJobChecks: Optional[str] = None

class DeleteCustomDataIdentifierRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteFindingsFilterRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteInvitationsRequestRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]

class DeleteMemberRequestRequestTypeDef(BaseValidatorModel):
    id: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClassificationJobRequestRequestTypeDef(BaseValidatorModel):
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

class DetectionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    suppressed: Optional[bool] = None
    type: Optional[DataIdentifierTypeType] = None

class DisableOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    adminAccountId: str

class DisassociateMemberRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DomainDetailsTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None

class EnableMacieRequestRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    adminAccountId: str
    clientToken: Optional[str] = None

class FindingStatisticsSortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[FindingStatisticsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None

class SeverityTypeDef(BaseValidatorModel):
    description: Optional[SeverityDescriptionType] = None
    score: Optional[int] = None

class FindingsFilterListItemTypeDef(BaseValidatorModel):
    action: Optional[FindingsFilterActionType] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class InvitationTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    invitationId: Optional[str] = None
    invitedAt: Optional[datetime] = None
    relationshipStatus: Optional[RelationshipStatusType] = None

class GetAllowListRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetBucketStatisticsRequestRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class GetClassificationScopeRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetCustomDataIdentifierRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GroupCountTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    groupKey: Optional[str] = None

class GetFindingsFilterRequestRequestTypeDef(BaseValidatorModel):
    id: str

class SecurityHubConfigurationTypeDef(BaseValidatorModel):
    publishClassificationFindings: bool
    publishPolicyFindings: bool

class SortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class GetMemberRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetResourceProfileRequestRequestTypeDef(BaseValidatorModel):
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

class GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef(BaseValidatorModel):
    findingId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetSensitiveDataOccurrencesRequestRequestTypeDef(BaseValidatorModel):
    findingId: str

class GetSensitivityInspectionTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

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

class GetUsageTotalsRequestRequestTypeDef(BaseValidatorModel):
    timeRange: Optional[str] = None

class UsageTotalTypeDef(BaseValidatorModel):
    currency: Optional[Literal["USD"]] = None
    estimatedCost: Optional[str] = None
    type: Optional[UsageTypeType] = None

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

class ListAllowListsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAutomatedDiscoveryAccountsRequestRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsSortCriteriaTypeDef(BaseValidatorModel):
    attributeName: Optional[ListJobsSortAttributeNameType] = None
    orderBy: Optional[OrderByType] = None

class ListClassificationScopesRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListCustomDataIdentifiersRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFindingsFiltersRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListInvitationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsFilterTermTypeDef(BaseValidatorModel):
    comparator: Optional[JobComparatorType] = None
    key: Optional[ListJobsFilterKeyType] = None
    values: Optional[Sequence[str]] = None

class ListManagedDataIdentifiersRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ManagedDataIdentifierSummaryTypeDef(BaseValidatorModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    id: Optional[str] = None

class ListMembersRequestRequestTypeDef(BaseValidatorModel):
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

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListResourceProfileArtifactsRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None

class ResourceProfileArtifactTypeDef(BaseValidatorModel):
    arn: str
    classificationResultStatus: str
    sensitive: Optional[bool] = None

class ListResourceProfileDetectionsRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSensitivityInspectionTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SensitivityInspectionTemplatesEntryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class S3BucketOwnerTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    id: Optional[str] = None

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

class SessionIssuerTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None
    type: Optional[str] = None
    userName: Optional[str] = None

class SuppressDataIdentifierTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[DataIdentifierTypeType] = None

class TagCriterionPairForJobTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TagValuePairTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class TestCustomDataIdentifierRequestRequestTypeDef(BaseValidatorModel):
    regex: str
    sampleText: str
    ignoreWords: Optional[Sequence[str]] = None
    keywords: Optional[Sequence[str]] = None
    maximumMatchDistance: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef(BaseValidatorModel):
    status: AutomatedDiscoveryStatusType
    autoEnableOrganizationMembers: Optional[AutoEnableModeType] = None

class UpdateClassificationJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    jobStatus: JobStatusType

class UpdateMacieSessionRequestRequestTypeDef(BaseValidatorModel):
    findingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    status: Optional[MacieStatusType] = None

class UpdateMemberSessionRequestRequestTypeDef(BaseValidatorModel):
    id: str
    status: MacieStatusType

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    autoEnable: bool

class UpdateResourceProfileRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    sensitivityScoreOverride: Optional[int] = None

class UpdateRetrievalConfigurationTypeDef(BaseValidatorModel):
    retrievalMode: RetrievalModeType
    roleName: Optional[str] = None

class UserIdentityRootTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    arn: Optional[str] = None
    principalId: Optional[str] = None

class CreateMemberRequestRequestTypeDef(BaseValidatorModel):
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

class BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[AutomatedDiscoveryAccountUpdateTypeDef]] = None

class BatchGetCustomDataIdentifiersResponseTypeDef(BaseValidatorModel):
    customDataIdentifiers: List[BatchGetCustomDataIdentifierSummaryTypeDef]
    notFoundIdentifierIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef(BaseValidatorModel):
    errors: List[AutomatedDiscoveryAccountUpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAllowListResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClassificationJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDataIdentifierResponseTypeDef(BaseValidatorModel):
    customDataIdentifierId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingsFilterResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
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

class ListAllowListsResponseTypeDef(BaseValidatorModel):
    allowLists: List[AllowListSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomatedDiscoveryAccountsResponseTypeDef(BaseValidatorModel):
    items: List[AutomatedDiscoveryAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsResponseTypeDef(BaseValidatorModel):
    findingIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationAdminAccountsResponseTypeDef(BaseValidatorModel):
    adminAccounts: List[AdminAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TestCustomDataIdentifierResponseTypeDef(BaseValidatorModel):
    matchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAllowListResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFindingsFilterResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
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

class DescribeBucketsRequestRequestTypeDef(BaseValidatorModel):
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

class ListClassificationScopesResponseTypeDef(BaseValidatorModel):
    classificationScopes: List[ClassificationScopeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDataIdentifierRequestRequestTypeDef(BaseValidatorModel):
    name: str
    regex: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    ignoreWords: Optional[Sequence[str]] = None
    keywords: Optional[Sequence[str]] = None
    maximumMatchDistance: Optional[int] = None
    severityLevels: Optional[Sequence[SeverityLevelTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class GetCustomDataIdentifierResponseTypeDef(BaseValidatorModel):
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

class ListCustomDataIdentifiersResponseTypeDef(BaseValidatorModel):
    items: List[CustomDataIdentifierSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBucketsRequestDescribeBucketsPaginateTypeDef(BaseValidatorModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]] = None
    sortCriteria: Optional[BucketSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAllowListsRequestListAllowListsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAutomatedDiscoveryAccountsRequestListAutomatedDiscoveryAccountsPaginateTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClassificationScopesRequestListClassificationScopesPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInvitationsRequestListInvitationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersRequestListMembersPaginateTypeDef(BaseValidatorModel):
    onlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSensitiveDataOccurrencesResponseTypeDef(BaseValidatorModel):
    error: str
    sensitiveDataOccurrences: Dict[str, List[DetectedDataDetailsTypeDef]]
    status: RevealRequestStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceProfileDetectionsResponseTypeDef(BaseValidatorModel):
    detections: List[DetectionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsFiltersResponseTypeDef(BaseValidatorModel):
    findingsFilterListItems: List[FindingsFilterListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdministratorAccountResponseTypeDef(BaseValidatorModel):
    administrator: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMasterAccountResponseTypeDef(BaseValidatorModel):
    master: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(BaseValidatorModel):
    invitations: List[InvitationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingStatisticsResponseTypeDef(BaseValidatorModel):
    countsByGroup: List[GroupCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsPublicationConfigurationResponseTypeDef(BaseValidatorModel):
    securityHubConfiguration: SecurityHubConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutFindingsPublicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    securityHubConfiguration: Optional[SecurityHubConfigurationTypeDef] = None

class GetFindingsRequestRequestTypeDef(BaseValidatorModel):
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

class GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef(BaseValidatorModel):
    findingId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSensitivityInspectionTemplateResponseTypeDef(BaseValidatorModel):
    description: str
    excludes: SensitivityInspectionTemplateExcludesOutputTypeDef
    includes: SensitivityInspectionTemplateIncludesOutputTypeDef
    name: str
    sensitivityInspectionTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef(BaseValidatorModel):
    filterBy: Optional[Sequence[UsageStatisticsFilterTypeDef]] = None
    sortBy: Optional[UsageStatisticsSortByTypeDef] = None
    timeRange: Optional[TimeRangeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsageStatisticsRequestRequestTypeDef(BaseValidatorModel):
    filterBy: Optional[Sequence[UsageStatisticsFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[UsageStatisticsSortByTypeDef] = None
    timeRange: Optional[TimeRangeType] = None

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

class ListManagedDataIdentifiersResponseTypeDef(BaseValidatorModel):
    items: List[ManagedDataIdentifierSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseValidatorModel):
    members: List[MemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceProfileArtifactsResponseTypeDef(BaseValidatorModel):
    artifacts: List[ResourceProfileArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSensitivityInspectionTemplatesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sensitivityInspectionTemplates: List[SensitivityInspectionTemplatesEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class UpdateSensitivityInspectionTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    description: Optional[str] = None
    excludes: Optional[SensitivityInspectionTemplateExcludesTypeDef] = None
    includes: Optional[SensitivityInspectionTemplateIncludesTypeDef] = None

class UsageByAccountTypeDef(BaseValidatorModel):
    currency: Optional[Literal["USD"]] = None
    estimatedCost: Optional[str] = None
    serviceLimit: Optional[ServiceLimitTypeDef] = None
    type: Optional[UsageTypeType] = None

class SessionContextTypeDef(BaseValidatorModel):
    attributes: Optional[SessionContextAttributesTypeDef] = None
    sessionIssuer: Optional[SessionIssuerTypeDef] = None

class UpdateResourceProfileDetectionsRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateRevealConfigurationRequestRequestTypeDef(BaseValidatorModel):
    configuration: RevealConfigurationTypeDef
    retrievalConfiguration: Optional[UpdateRetrievalConfigurationTypeDef] = None

class CreateAllowListRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    criteria: AllowListCriteriaTypeDef
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetAllowListResponseTypeDef(BaseValidatorModel):
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

class UpdateAllowListRequestRequestTypeDef(BaseValidatorModel):
    criteria: AllowListCriteriaTypeDef
    id: str
    name: str
    description: Optional[str] = None

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

class PutClassificationExportConfigurationRequestRequestTypeDef(BaseValidatorModel):
    configuration: ClassificationExportConfigurationTypeDef

class PutClassificationExportConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: ClassificationExportConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsFilterResponseTypeDef(BaseValidatorModel):
    action: FindingsFilterActionType
    arn: str
    description: str
    findingCriteria: FindingCriteriaOutputTypeDef
    id: str
    name: str
    position: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingsFilterRequestRequestTypeDef(BaseValidatorModel):
    action: FindingsFilterActionType
    findingCriteria: FindingCriteriaTypeDef
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    position: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class GetFindingStatisticsRequestRequestTypeDef(BaseValidatorModel):
    groupBy: GroupByType
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    size: Optional[int] = None
    sortCriteria: Optional[FindingStatisticsSortCriteriaTypeDef] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseValidatorModel):
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseValidatorModel):
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None

class UpdateFindingsFilterRequestRequestTypeDef(BaseValidatorModel):
    id: str
    action: Optional[FindingsFilterActionType] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    findingCriteria: Optional[FindingCriteriaTypeDef] = None
    name: Optional[str] = None
    position: Optional[int] = None

class ListClassificationJobsRequestListClassificationJobsPaginateTypeDef(BaseValidatorModel):
    filterCriteria: Optional[ListJobsFilterCriteriaTypeDef] = None
    sortCriteria: Optional[ListJobsSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClassificationJobsRequestRequestTypeDef(BaseValidatorModel):
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

class GetClassificationScopeResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    s3: S3ClassificationScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClassificationScopeRequestRequestTypeDef(BaseValidatorModel):
    id: str
    s3: Optional[S3ClassificationScopeUpdateTypeDef] = None

class SearchResourcesCriteriaTypeDef(BaseValidatorModel):
    simpleCriterion: Optional[SearchResourcesSimpleCriterionTypeDef] = None
    tagCriterion: Optional[SearchResourcesTagCriterionTypeDef] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDetectionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    occurrences: Optional[OccurrencesTypeDef] = None

class DefaultDetectionTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    occurrences: Optional[OccurrencesTypeDef] = None
    type: Optional[str] = None

class SearchResourcesCriteriaBlockTypeDef(BaseValidatorModel):
    and: Optional[Sequence[SearchResourcesCriteriaTypeDef]] = None

class GetUsageStatisticsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    records: List[UsageRecordTypeDef]
    timeRange: TimeRangeType
    ResponseMetadata: ResponseMetadataTypeDef

class UserIdentityTypeDef(BaseValidatorModel):
    assumedRole: Optional[AssumedRoleTypeDef] = None
    awsAccount: Optional[AwsAccountTypeDef] = None
    awsService: Optional[AwsServiceTypeDef] = None
    federatedUser: Optional[FederatedUserTypeDef] = None
    iamUser: Optional[IamUserTypeDef] = None
    root: Optional[UserIdentityRootTypeDef] = None
    type: Optional[UserIdentityTypeType] = None

class CriteriaBlockForJobOutputTypeDef(BaseValidatorModel):
    and: Optional[List[CriteriaForJobOutputTypeDef]] = None

class CriteriaBlockForJobTypeDef(BaseValidatorModel):
    and: Optional[Sequence[CriteriaForJobTypeDef]] = None

class JobScopingBlockOutputTypeDef(BaseValidatorModel):
    and: Optional[List[JobScopeTermOutputTypeDef]] = None

class JobScopingBlockTypeDef(BaseValidatorModel):
    and: Optional[Sequence[JobScopeTermTypeDef]] = None

class BucketMetadataTypeDef(BaseValidatorModel):
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

class SensitiveDataItemTypeDef(BaseValidatorModel):
    category: Optional[SensitiveDataItemCategoryType] = None
    detections: Optional[List[DefaultDetectionTypeDef]] = None
    totalCount: Optional[int] = None

class SearchResourcesBucketCriteriaTypeDef(BaseValidatorModel):
    excludes: Optional[SearchResourcesCriteriaBlockTypeDef] = None
    includes: Optional[SearchResourcesCriteriaBlockTypeDef] = None

class FindingActorTypeDef(BaseValidatorModel):
    domainDetails: Optional[DomainDetailsTypeDef] = None
    ipAddressDetails: Optional[IpAddressDetailsTypeDef] = None
    userIdentity: Optional[UserIdentityTypeDef] = None

class S3BucketCriteriaForJobOutputTypeDef(BaseValidatorModel):
    excludes: Optional[CriteriaBlockForJobOutputTypeDef] = None
    includes: Optional[CriteriaBlockForJobOutputTypeDef] = None

class S3BucketCriteriaForJobTypeDef(BaseValidatorModel):
    excludes: Optional[CriteriaBlockForJobTypeDef] = None
    includes: Optional[CriteriaBlockForJobTypeDef] = None

class ScopingOutputTypeDef(BaseValidatorModel):
    excludes: Optional[JobScopingBlockOutputTypeDef] = None
    includes: Optional[JobScopingBlockOutputTypeDef] = None

class ScopingTypeDef(BaseValidatorModel):
    excludes: Optional[JobScopingBlockTypeDef] = None
    includes: Optional[JobScopingBlockTypeDef] = None

class DescribeBucketsResponseTypeDef(BaseValidatorModel):
    buckets: List[BucketMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class SearchResourcesRequestRequestTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SearchResourcesSortCriteriaTypeDef] = None

class SearchResourcesRequestSearchResourcesPaginateTypeDef(BaseValidatorModel):
    bucketCriteria: Optional[SearchResourcesBucketCriteriaTypeDef] = None
    sortCriteria: Optional[SearchResourcesSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateClassificationJobRequestRequestTypeDef(BaseValidatorModel):
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

class FindingTypeDef(BaseValidatorModel):
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

class GetFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

