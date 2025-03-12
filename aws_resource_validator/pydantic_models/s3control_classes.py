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
from aws_resource_validator.pydantic_models.s3control_constants import *

class AbortIncompleteMultipartUploadTypeDef(BaseValidatorModel):
    DaysAfterInitiation: Optional[int] = None


class AccessControlTranslationTypeDef(BaseValidatorModel):
    Owner: Literal["Destination"]


class AccessGrantsLocationConfigurationTypeDef(BaseValidatorModel):
    S3SubPrefix: Optional[str] = None


class VpcConfigurationTypeDef(BaseValidatorModel):
    VpcId: str


class ActivityMetricsTypeDef(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class AdvancedCostOptimizationMetricsTypeDef(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class AdvancedDataProtectionMetricsTypeDef(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class DetailedStatusCodesMetricsTypeDef(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class AssociateAccessGrantsIdentityCenterRequestTypeDef(BaseValidatorModel):
    AccountId: str
    IdentityCenterArn: str


class AsyncErrorDetailsTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None
    Resource: Optional[str] = None
    RequestId: Optional[str] = None


class DeleteMultiRegionAccessPointInputTypeDef(BaseValidatorModel):
    Name: str


class PutMultiRegionAccessPointPolicyInputTypeDef(BaseValidatorModel):
    Name: str
    Policy: str


class AwsLambdaTransformationTypeDef(BaseValidatorModel):
    FunctionArn: str
    FunctionPayload: Optional[str] = None


class CloudWatchMetricsTypeDef(BaseValidatorModel):
    IsEnabled: bool


class GranteeTypeDef(BaseValidatorModel):
    GranteeType: Optional[GranteeTypeType] = None
    GranteeIdentifier: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ObjectLambdaAccessPointAliasTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Status: Optional[ObjectLambdaAccessPointAliasStatusType] = None


class PublicAccessBlockConfigurationTypeDef(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None


class CreateBucketConfigurationTypeDef(BaseValidatorModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None


class JobReportTypeDef(BaseValidatorModel):
    Enabled: bool
    Bucket: Optional[str] = None
    Format: Optional[Literal["Report_CSV_20180820"]] = None
    Prefix: Optional[str] = None
    ReportScope: Optional[JobReportScopeType] = None


class S3TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class RegionTypeDef(BaseValidatorModel):
    Bucket: str
    BucketAccountId: Optional[str] = None


class CredentialsTypeDef(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None
    Expiration: Optional[datetime] = None


class DeleteAccessGrantRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccessGrantId: str


class DeleteAccessGrantsInstanceRequestTypeDef(BaseValidatorModel):
    AccountId: str


class DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str


class DeleteAccessGrantsLocationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str


class DeleteAccessPointForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteAccessPointPolicyForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteAccessPointPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteAccessPointRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteBucketLifecycleConfigurationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketReplicationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketTaggingRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteJobTaggingRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobId: str


class DeleteMarkerReplicationTypeDef(BaseValidatorModel):
    Status: DeleteMarkerReplicationStatusType


class DeletePublicAccessBlockRequestTypeDef(BaseValidatorModel):
    AccountId: str


class DeleteStorageLensConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class DeleteStorageLensConfigurationTaggingRequestTypeDef(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class DeleteStorageLensGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    AccountId: str


class DescribeJobRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobId: str


class DescribeMultiRegionAccessPointOperationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RequestTokenARN: str


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    ReplicaKmsKeyID: Optional[str] = None


class DissociateAccessGrantsIdentityCenterRequestTypeDef(BaseValidatorModel):
    AccountId: str


class EstablishedMultiRegionAccessPointPolicyTypeDef(BaseValidatorModel):
    Policy: Optional[str] = None


class ExcludeOutputTypeDef(BaseValidatorModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class ExcludeTypeDef(BaseValidatorModel):
    Buckets: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None


class ExistingObjectReplicationTypeDef(BaseValidatorModel):
    Status: ExistingObjectReplicationStatusType


class SSEKMSEncryptionTypeDef(BaseValidatorModel):
    KeyId: str


class GetAccessGrantRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccessGrantId: str


class GetAccessGrantsInstanceForPrefixRequestTypeDef(BaseValidatorModel):
    AccountId: str
    S3Prefix: str


class GetAccessGrantsInstanceRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetAccessGrantsInstanceResourcePolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetAccessGrantsLocationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str


class GetAccessPointConfigurationForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointPolicyForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class PolicyStatusTypeDef(BaseValidatorModel):
    IsPublic: Optional[bool] = None


class GetAccessPointPolicyStatusRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetBucketLifecycleConfigurationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketReplicationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketTaggingRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketVersioningRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetDataAccessRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Target: str
    Permission: PermissionType
    DurationSeconds: Optional[int] = None
    Privilege: Optional[PrivilegeType] = None
    TargetType: Optional[Literal["Object"]] = None


class GetJobTaggingRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobId: str


class GetMultiRegionAccessPointPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetMultiRegionAccessPointPolicyStatusRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetMultiRegionAccessPointRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str


class GetMultiRegionAccessPointRoutesRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Mrap: str


class MultiRegionAccessPointRouteTypeDef(BaseValidatorModel):
    TrafficDialPercentage: int
    Bucket: Optional[str] = None
    Region: Optional[str] = None


class GetPublicAccessBlockRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetStorageLensConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class GetStorageLensConfigurationTaggingRequestTypeDef(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class StorageLensTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class GetStorageLensGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    AccountId: str


class IncludeOutputTypeDef(BaseValidatorModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class IncludeTypeDef(BaseValidatorModel):
    Buckets: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None


class JobFailureTypeDef(BaseValidatorModel):
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None


class KeyNameConstraintOutputTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnySubstring: Optional[List[str]] = None


class KeyNameConstraintTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnySubstring: Optional[Sequence[str]] = None


class JobManifestLocationTypeDef(BaseValidatorModel):
    ObjectArn: str
    ETag: str
    ObjectVersionId: Optional[str] = None


class JobManifestSpecOutputTypeDef(BaseValidatorModel):
    Format: JobManifestFormatType
    Fields: Optional[List[JobManifestFieldNameType]] = None


class JobManifestSpecTypeDef(BaseValidatorModel):
    Format: JobManifestFormatType
    Fields: Optional[Sequence[JobManifestFieldNameType]] = None


class LambdaInvokeOperationOutputTypeDef(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    InvocationSchemaVersion: Optional[str] = None
    UserArguments: Optional[Dict[str, str]] = None


class S3InitiateRestoreObjectOperationTypeDef(BaseValidatorModel):
    ExpirationInDays: Optional[int] = None
    GlacierJobTier: Optional[S3GlacierJobTierType] = None


class LambdaInvokeOperationTypeDef(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    InvocationSchemaVersion: Optional[str] = None
    UserArguments: Optional[Mapping[str, str]] = None


class JobTimersTypeDef(BaseValidatorModel):
    ElapsedTimeInActiveSeconds: Optional[int] = None


class LifecycleExpirationOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None


class NoncurrentVersionExpirationTypeDef(BaseValidatorModel):
    NoncurrentDays: Optional[int] = None
    NewerNoncurrentVersions: Optional[int] = None


class NoncurrentVersionTransitionTypeDef(BaseValidatorModel):
    NoncurrentDays: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class TransitionOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class ListAccessGrantsInstanceEntryTypeDef(BaseValidatorModel):
    AccessGrantsInstanceId: Optional[str] = None
    AccessGrantsInstanceArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    IdentityCenterArn: Optional[str] = None
    IdentityCenterInstanceArn: Optional[str] = None
    IdentityCenterApplicationArn: Optional[str] = None


class ListAccessGrantsInstancesRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccessGrantsLocationsEntryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    AccessGrantsLocationId: Optional[str] = None
    AccessGrantsLocationArn: Optional[str] = None
    LocationScope: Optional[str] = None
    IAMRoleArn: Optional[str] = None


class ListAccessGrantsLocationsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LocationScope: Optional[str] = None


class ListAccessGrantsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    GranteeType: Optional[GranteeTypeType] = None
    GranteeIdentifier: Optional[str] = None
    Permission: Optional[PermissionType] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessPointsForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccessPointsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCallerAccessGrantsEntryTypeDef(BaseValidatorModel):
    Permission: Optional[PermissionType] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None


class ListCallerAccessGrantsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    GrantScope: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AllowedByApplication: Optional[bool] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobStatuses: Optional[Sequence[JobStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMultiRegionAccessPointsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRegionalBucketsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OutpostId: Optional[str] = None


class RegionalBucketTypeDef(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    BucketArn: Optional[str] = None
    OutpostId: Optional[str] = None


class ListStorageLensConfigurationEntryTypeDef(BaseValidatorModel):
    Id: str
    StorageLensArn: str
    HomeRegion: str
    IsEnabled: Optional[bool] = None


class ListStorageLensConfigurationsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None


class ListStorageLensGroupEntryTypeDef(BaseValidatorModel):
    Name: str
    StorageLensGroupArn: str
    HomeRegion: str


class ListStorageLensGroupsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ResourceArn: str


class MatchObjectAgeTypeDef(BaseValidatorModel):
    DaysGreaterThan: Optional[int] = None
    DaysLessThan: Optional[int] = None


class MatchObjectSizeTypeDef(BaseValidatorModel):
    BytesGreaterThan: Optional[int] = None
    BytesLessThan: Optional[int] = None


class ReplicationTimeValueTypeDef(BaseValidatorModel):
    Minutes: Optional[int] = None


class ProposedMultiRegionAccessPointPolicyTypeDef(BaseValidatorModel):
    Policy: Optional[str] = None


class MultiRegionAccessPointRegionalResponseTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    RequestStatus: Optional[str] = None


class RegionReportTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Region: Optional[str] = None
    BucketAccountId: Optional[str] = None


class SelectionCriteriaTypeDef(BaseValidatorModel):
    Delimiter: Optional[str] = None
    MaxDepth: Optional[int] = None
    MinStorageBytesPercentage: Optional[float] = None


class PutAccessGrantsInstanceResourcePolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Policy: str
    Organization: Optional[str] = None


class PutAccessPointPolicyForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str
    Policy: str


class PutAccessPointPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str
    Policy: str


class PutBucketPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str
    Policy: str
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None


class VersioningConfigurationTypeDef(BaseValidatorModel):
    MFADelete: Optional[MFADeleteType] = None
    Status: Optional[BucketVersioningStatusType] = None


class ReplicaModificationsTypeDef(BaseValidatorModel):
    Status: ReplicaModificationsStatusType


class S3ObjectOwnerTypeDef(BaseValidatorModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None


class S3ObjectMetadataOutputTypeDef(BaseValidatorModel):
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    UserMetadata: Optional[Dict[str, str]] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    HttpExpiresDate: Optional[datetime] = None
    RequesterCharged: Optional[bool] = None
    SSEAlgorithm: Optional[S3SSEAlgorithmType] = None


class S3GranteeTypeDef(BaseValidatorModel):
    TypeIdentifier: Optional[S3GranteeTypeIdentifierType] = None
    Identifier: Optional[str] = None
    DisplayName: Optional[str] = None


class S3ObjectLockLegalHoldTypeDef(BaseValidatorModel):
    Status: S3ObjectLockLegalHoldStatusType


class S3RetentionOutputTypeDef(BaseValidatorModel):
    RetainUntilDate: Optional[datetime] = None
    Mode: Optional[S3ObjectLockRetentionModeType] = None


class SSEKMSTypeDef(BaseValidatorModel):
    KeyId: str


class SseKmsEncryptedObjectsTypeDef(BaseValidatorModel):
    Status: SseKmsEncryptedObjectsStatusType


class StorageLensAwsOrgTypeDef(BaseValidatorModel):
    Arn: str


class StorageLensGroupLevelSelectionCriteriaOutputTypeDef(BaseValidatorModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None


class StorageLensGroupLevelSelectionCriteriaTypeDef(BaseValidatorModel):
    Include: Optional[Sequence[str]] = None
    Exclude: Optional[Sequence[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateAccessGrantsLocationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str
    IAMRoleArn: str


class UpdateJobPriorityRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobId: str
    Priority: int


class UpdateJobStatusRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobId: str
    RequestedJobStatus: RequestedJobStatusType
    StatusUpdateReason: Optional[str] = None


class AccessPointTypeDef(BaseValidatorModel):
    Name: str
    NetworkOrigin: NetworkOriginType
    Bucket: str
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    BucketAccountId: Optional[str] = None


class DeleteMultiRegionAccessPointRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ClientToken: str
    Details: DeleteMultiRegionAccessPointInputTypeDef


class PutMultiRegionAccessPointPolicyRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ClientToken: str
    Details: PutMultiRegionAccessPointPolicyInputTypeDef


class ObjectLambdaContentTransformationTypeDef(BaseValidatorModel):
    AwsLambda: Optional[AwsLambdaTransformationTypeDef] = None


class ListAccessGrantEntryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    AccessGrantId: Optional[str] = None
    AccessGrantArn: Optional[str] = None
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None
    AccessGrantsLocationId: Optional[str] = None
    AccessGrantsLocationConfiguration: Optional[AccessGrantsLocationConfigurationTypeDef] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None


class CreateAccessGrantRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str
    Grantee: GranteeTypeDef
    Permission: PermissionType
    AccessGrantsLocationConfiguration: Optional[AccessGrantsLocationConfigurationTypeDef] = None
    ApplicationArn: Optional[str] = None
    S3PrefixType: Optional[Literal["Object"]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateAccessGrantsInstanceRequestTypeDef(BaseValidatorModel):
    AccountId: str
    IdentityCenterArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateAccessGrantsLocationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    LocationScope: str
    IAMRoleArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateAccessGrantResultTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantId: str
    AccessGrantArn: str
    Grantee: GranteeTypeDef
    AccessGrantsLocationId: str
    AccessGrantsLocationConfiguration: AccessGrantsLocationConfigurationTypeDef
    Permission: PermissionType
    ApplicationArn: str
    GrantScope: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccessGrantsInstanceResultTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsInstanceId: str
    AccessGrantsInstanceArn: str
    IdentityCenterArn: str
    IdentityCenterInstanceArn: str
    IdentityCenterApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccessGrantsLocationResultTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccessPointResultTypeDef(BaseValidatorModel):
    AccessPointArn: str
    Alias: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBucketResultTypeDef(BaseValidatorModel):
    Location: str
    BucketArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobResultTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultiRegionAccessPointResultTypeDef(BaseValidatorModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMultiRegionAccessPointResultTypeDef(BaseValidatorModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessGrantResultTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantId: str
    AccessGrantArn: str
    Grantee: GranteeTypeDef
    Permission: PermissionType
    AccessGrantsLocationId: str
    AccessGrantsLocationConfiguration: AccessGrantsLocationConfigurationTypeDef
    GrantScope: str
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessGrantsInstanceForPrefixResultTypeDef(BaseValidatorModel):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessGrantsInstanceResourcePolicyResultTypeDef(BaseValidatorModel):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessGrantsInstanceResultTypeDef(BaseValidatorModel):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    IdentityCenterArn: str
    IdentityCenterInstanceArn: str
    IdentityCenterApplicationArn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessGrantsLocationResultTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessPointPolicyForObjectLambdaResultTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessPointPolicyResultTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketPolicyResultTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketResultTypeDef(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketVersioningResultTypeDef(BaseValidatorModel):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutAccessGrantsInstanceResourcePolicyResultTypeDef(BaseValidatorModel):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PutMultiRegionAccessPointPolicyResultTypeDef(BaseValidatorModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAccessGrantsLocationResultTypeDef(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJobPriorityResultTypeDef(BaseValidatorModel):
    JobId: str
    Priority: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJobStatusResultTypeDef(BaseValidatorModel):
    JobId: str
    Status: JobStatusType
    StatusUpdateReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccessPointForObjectLambdaResultTypeDef(BaseValidatorModel):
    ObjectLambdaAccessPointArn: str
    Alias: ObjectLambdaAccessPointAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ObjectLambdaAccessPointTypeDef(BaseValidatorModel):
    Name: str
    ObjectLambdaAccessPointArn: Optional[str] = None
    Alias: Optional[ObjectLambdaAccessPointAliasTypeDef] = None


class CreateAccessPointRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str
    Bucket: str
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    PublicAccessBlockConfiguration: Optional[PublicAccessBlockConfigurationTypeDef] = None
    BucketAccountId: Optional[str] = None


class GetAccessPointForObjectLambdaResultTypeDef(BaseValidatorModel):
    Name: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    CreationDate: datetime
    Alias: ObjectLambdaAccessPointAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessPointResultTypeDef(BaseValidatorModel):
    Name: str
    Bucket: str
    NetworkOrigin: NetworkOriginType
    VpcConfiguration: VpcConfigurationTypeDef
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    CreationDate: datetime
    Alias: str
    AccessPointArn: str
    Endpoints: Dict[str, str]
    BucketAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPublicAccessBlockOutputTypeDef(BaseValidatorModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutPublicAccessBlockRequestTypeDef(BaseValidatorModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    AccountId: str


class CreateBucketRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfigurationTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    OutpostId: Optional[str] = None


class GetBucketTaggingResultTypeDef(BaseValidatorModel):
    TagSet: List[S3TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobTaggingResultTypeDef(BaseValidatorModel):
    Tags: List[S3TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LifecycleRuleAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class LifecycleRuleAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[S3TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class PutJobTaggingRequestTypeDef(BaseValidatorModel):
    AccountId: str
    JobId: str
    Tags: Sequence[S3TagTypeDef]


class ReplicationRuleAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3TagTypeDef]] = None


class ReplicationRuleAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[S3TagTypeDef]] = None


class S3SetObjectTaggingOperationOutputTypeDef(BaseValidatorModel):
    TagSet: Optional[List[S3TagTypeDef]] = None


class S3SetObjectTaggingOperationTypeDef(BaseValidatorModel):
    TagSet: Optional[Sequence[S3TagTypeDef]] = None


class TaggingTypeDef(BaseValidatorModel):
    TagSet: Sequence[S3TagTypeDef]


class CreateMultiRegionAccessPointInputOutputTypeDef(BaseValidatorModel):
    Name: str
    Regions: List[RegionTypeDef]
    PublicAccessBlock: Optional[PublicAccessBlockConfigurationTypeDef] = None


class CreateMultiRegionAccessPointInputTypeDef(BaseValidatorModel):
    Name: str
    Regions: Sequence[RegionTypeDef]
    PublicAccessBlock: Optional[PublicAccessBlockConfigurationTypeDef] = None


class GetDataAccessResultTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    MatchedGrantTarget: str
    ResponseMetadata: ResponseMetadataTypeDef


class GeneratedManifestEncryptionOutputTypeDef(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSEncryptionTypeDef] = None


class GeneratedManifestEncryptionTypeDef(BaseValidatorModel):
    SSES3: Optional[Mapping[str, Any]] = None
    SSEKMS: Optional[SSEKMSEncryptionTypeDef] = None


class GetAccessPointPolicyStatusForObjectLambdaResultTypeDef(BaseValidatorModel):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessPointPolicyStatusResultTypeDef(BaseValidatorModel):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMultiRegionAccessPointPolicyStatusResultTypeDef(BaseValidatorModel):
    Established: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMultiRegionAccessPointRoutesResultTypeDef(BaseValidatorModel):
    Mrap: str
    Routes: List[MultiRegionAccessPointRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SubmitMultiRegionAccessPointRoutesRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Mrap: str
    RouteUpdates: Sequence[MultiRegionAccessPointRouteTypeDef]


class GetStorageLensConfigurationTaggingResultTypeDef(BaseValidatorModel):
    Tags: List[StorageLensTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutStorageLensConfigurationTaggingRequestTypeDef(BaseValidatorModel):
    ConfigId: str
    AccountId: str
    Tags: Sequence[StorageLensTagTypeDef]


class JobManifestGeneratorFilterOutputTypeDef(BaseValidatorModel):
    EligibleForReplication: Optional[bool] = None
    CreatedAfter: Optional[datetime] = None
    CreatedBefore: Optional[datetime] = None
    ObjectReplicationStatuses: Optional[List[ReplicationStatusType]] = None
    KeyNameConstraint: Optional[KeyNameConstraintOutputTypeDef] = None
    ObjectSizeGreaterThanBytes: Optional[int] = None
    ObjectSizeLessThanBytes: Optional[int] = None
    MatchAnyStorageClass: Optional[List[S3StorageClassType]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class JobManifestGeneratorFilterTypeDef(BaseValidatorModel):
    EligibleForReplication: Optional[bool] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    ObjectReplicationStatuses: Optional[Sequence[ReplicationStatusType]] = None
    KeyNameConstraint: Optional[KeyNameConstraintTypeDef] = None
    ObjectSizeGreaterThanBytes: Optional[int] = None
    ObjectSizeLessThanBytes: Optional[int] = None
    MatchAnyStorageClass: Optional[Sequence[S3StorageClassType]] = None


class LifecycleExpirationTypeDef(BaseValidatorModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None


class S3ObjectMetadataTypeDef(BaseValidatorModel):
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    UserMetadata: Optional[Mapping[str, str]] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    HttpExpiresDate: Optional[TimestampTypeDef] = None
    RequesterCharged: Optional[bool] = None
    SSEAlgorithm: Optional[S3SSEAlgorithmType] = None


class S3RetentionTypeDef(BaseValidatorModel):
    RetainUntilDate: Optional[TimestampTypeDef] = None
    Mode: Optional[S3ObjectLockRetentionModeType] = None


class TransitionTypeDef(BaseValidatorModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class S3GeneratedManifestDescriptorTypeDef(BaseValidatorModel):
    Format: Optional[Literal["S3InventoryReport_CSV_20211130"]] = None
    Location: Optional[JobManifestLocationTypeDef] = None


class JobManifestOutputTypeDef(BaseValidatorModel):
    Spec: JobManifestSpecOutputTypeDef
    Location: JobManifestLocationTypeDef


class JobManifestTypeDef(BaseValidatorModel):
    Spec: JobManifestSpecTypeDef
    Location: JobManifestLocationTypeDef


class JobProgressSummaryTypeDef(BaseValidatorModel):
    TotalNumberOfTasks: Optional[int] = None
    NumberOfTasksSucceeded: Optional[int] = None
    NumberOfTasksFailed: Optional[int] = None
    Timers: Optional[JobTimersTypeDef] = None


class ListAccessGrantsInstancesResultTypeDef(BaseValidatorModel):
    AccessGrantsInstancesList: List[ListAccessGrantsInstanceEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccessGrantsLocationsResultTypeDef(BaseValidatorModel):
    AccessGrantsLocationsList: List[ListAccessGrantsLocationsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccessPointsForObjectLambdaRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCallerAccessGrantsRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    GrantScope: Optional[str] = None
    AllowedByApplication: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCallerAccessGrantsResultTypeDef(BaseValidatorModel):
    CallerAccessGrantsList: List[ListCallerAccessGrantsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRegionalBucketsResultTypeDef(BaseValidatorModel):
    RegionalBucketList: List[RegionalBucketTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListStorageLensConfigurationsResultTypeDef(BaseValidatorModel):
    StorageLensConfigurationList: List[ListStorageLensConfigurationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListStorageLensGroupsResultTypeDef(BaseValidatorModel):
    StorageLensGroupList: List[ListStorageLensGroupEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StorageLensGroupAndOperatorOutputTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None


class StorageLensGroupAndOperatorTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnyTag: Optional[Sequence[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None


class StorageLensGroupOrOperatorOutputTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None


class StorageLensGroupOrOperatorTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnyTag: Optional[Sequence[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None


class MetricsTypeDef(BaseValidatorModel):
    Status: MetricsStatusType
    EventThreshold: Optional[ReplicationTimeValueTypeDef] = None


class ReplicationTimeTypeDef(BaseValidatorModel):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValueTypeDef


class MultiRegionAccessPointPolicyDocumentTypeDef(BaseValidatorModel):
    Established: Optional[EstablishedMultiRegionAccessPointPolicyTypeDef] = None
    Proposed: Optional[ProposedMultiRegionAccessPointPolicyTypeDef] = None


class MultiRegionAccessPointsAsyncResponseTypeDef(BaseValidatorModel):
    Regions: Optional[List[MultiRegionAccessPointRegionalResponseTypeDef]] = None


class MultiRegionAccessPointReportTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Alias: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PublicAccessBlock: Optional[PublicAccessBlockConfigurationTypeDef] = None
    Status: Optional[MultiRegionAccessPointStatusType] = None
    Regions: Optional[List[RegionReportTypeDef]] = None


class PrefixLevelStorageMetricsTypeDef(BaseValidatorModel):
    IsEnabled: Optional[bool] = None
    SelectionCriteria: Optional[SelectionCriteriaTypeDef] = None


class PutBucketVersioningRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str
    VersioningConfiguration: VersioningConfigurationTypeDef
    MFA: Optional[str] = None


class S3GrantTypeDef(BaseValidatorModel):
    Grantee: Optional[S3GranteeTypeDef] = None
    Permission: Optional[S3PermissionType] = None


class S3SetObjectLegalHoldOperationTypeDef(BaseValidatorModel):
    LegalHold: S3ObjectLockLegalHoldTypeDef


class S3SetObjectRetentionOperationOutputTypeDef(BaseValidatorModel):
    Retention: S3RetentionOutputTypeDef
    BypassGovernanceRetention: Optional[bool] = None


class StorageLensDataExportEncryptionOutputTypeDef(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None


class StorageLensDataExportEncryptionTypeDef(BaseValidatorModel):
    SSES3: Optional[Mapping[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None


class SourceSelectionCriteriaTypeDef(BaseValidatorModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjectsTypeDef] = None
    ReplicaModifications: Optional[ReplicaModificationsTypeDef] = None


class StorageLensGroupLevelOutputTypeDef(BaseValidatorModel):
    SelectionCriteria: Optional[StorageLensGroupLevelSelectionCriteriaOutputTypeDef] = None


class StorageLensGroupLevelTypeDef(BaseValidatorModel):
    SelectionCriteria: Optional[StorageLensGroupLevelSelectionCriteriaTypeDef] = None


class ListAccessPointsResultTypeDef(BaseValidatorModel):
    AccessPointList: List[AccessPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ObjectLambdaTransformationConfigurationOutputTypeDef(BaseValidatorModel):
    Actions: List[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformationTypeDef


class ObjectLambdaTransformationConfigurationTypeDef(BaseValidatorModel):
    Actions: Sequence[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformationTypeDef


class ListAccessGrantsResultTypeDef(BaseValidatorModel):
    AccessGrantsList: List[ListAccessGrantEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccessPointsForObjectLambdaResultTypeDef(BaseValidatorModel):
    ObjectLambdaAccessPointList: List[ObjectLambdaAccessPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LifecycleRuleFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3TagTypeDef] = None
    And: Optional[LifecycleRuleAndOperatorOutputTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class ReplicationRuleFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorOutputTypeDef] = None


class ReplicationRuleFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorTypeDef] = None


class PutBucketTaggingRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str
    Tagging: TaggingTypeDef


class AsyncRequestParametersTypeDef(BaseValidatorModel):
    CreateMultiRegionAccessPointRequest: Optional[CreateMultiRegionAccessPointInputOutputTypeDef] = None
    DeleteMultiRegionAccessPointRequest: Optional[DeleteMultiRegionAccessPointInputTypeDef] = None
    PutMultiRegionAccessPointPolicyRequest: Optional[PutMultiRegionAccessPointPolicyInputTypeDef] = None


class S3ManifestOutputLocationOutputTypeDef(BaseValidatorModel):
    Bucket: str
    ManifestFormat: Literal["S3InventoryReport_CSV_20211130"]
    ExpectedManifestBucketOwner: Optional[str] = None
    ManifestPrefix: Optional[str] = None
    ManifestEncryption: Optional[GeneratedManifestEncryptionOutputTypeDef] = None


class S3ManifestOutputLocationTypeDef(BaseValidatorModel):
    Bucket: str
    ManifestFormat: Literal["S3InventoryReport_CSV_20211130"]
    ExpectedManifestBucketOwner: Optional[str] = None
    ManifestPrefix: Optional[str] = None
    ManifestEncryption: Optional[GeneratedManifestEncryptionTypeDef] = None


class S3SetObjectRetentionOperationTypeDef(BaseValidatorModel):
    Retention: S3RetentionTypeDef
    BypassGovernanceRetention: Optional[bool] = None


class JobListDescriptorTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    Description: Optional[str] = None
    Operation: Optional[OperationNameType] = None
    Priority: Optional[int] = None
    Status: Optional[JobStatusType] = None
    CreationTime: Optional[datetime] = None
    TerminationDate: Optional[datetime] = None
    ProgressSummary: Optional[JobProgressSummaryTypeDef] = None


class StorageLensGroupFilterOutputTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None
    And: Optional[StorageLensGroupAndOperatorOutputTypeDef] = None
    Or: Optional[StorageLensGroupOrOperatorOutputTypeDef] = None


class StorageLensGroupFilterTypeDef(BaseValidatorModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnyTag: Optional[Sequence[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None
    And: Optional[StorageLensGroupAndOperatorTypeDef] = None
    Or: Optional[StorageLensGroupOrOperatorTypeDef] = None


class DestinationTypeDef(BaseValidatorModel):
    Bucket: str
    Account: Optional[str] = None
    ReplicationTime: Optional[ReplicationTimeTypeDef] = None
    AccessControlTranslation: Optional[AccessControlTranslationTypeDef] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    Metrics: Optional[MetricsTypeDef] = None
    StorageClass: Optional[ReplicationStorageClassType] = None


class GetMultiRegionAccessPointPolicyResultTypeDef(BaseValidatorModel):
    Policy: MultiRegionAccessPointPolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AsyncResponseDetailsTypeDef(BaseValidatorModel):
    MultiRegionAccessPointDetails: Optional[MultiRegionAccessPointsAsyncResponseTypeDef] = None
    ErrorDetails: Optional[AsyncErrorDetailsTypeDef] = None


class GetMultiRegionAccessPointResultTypeDef(BaseValidatorModel):
    AccessPoint: MultiRegionAccessPointReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListMultiRegionAccessPointsResultTypeDef(BaseValidatorModel):
    AccessPoints: List[MultiRegionAccessPointReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PrefixLevelTypeDef(BaseValidatorModel):
    StorageMetrics: PrefixLevelStorageMetricsTypeDef


class S3AccessControlListOutputTypeDef(BaseValidatorModel):
    Owner: S3ObjectOwnerTypeDef
    Grants: Optional[List[S3GrantTypeDef]] = None


class S3AccessControlListTypeDef(BaseValidatorModel):
    Owner: S3ObjectOwnerTypeDef
    Grants: Optional[Sequence[S3GrantTypeDef]] = None


class S3CopyObjectOperationOutputTypeDef(BaseValidatorModel):
    TargetResource: Optional[str] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None
    AccessControlGrants: Optional[List[S3GrantTypeDef]] = None
    MetadataDirective: Optional[S3MetadataDirectiveType] = None
    ModifiedSinceConstraint: Optional[datetime] = None
    NewObjectMetadata: Optional[S3ObjectMetadataOutputTypeDef] = None
    NewObjectTagging: Optional[List[S3TagTypeDef]] = None
    RedirectLocation: Optional[str] = None
    RequesterPays: Optional[bool] = None
    StorageClass: Optional[S3StorageClassType] = None
    UnModifiedSinceConstraint: Optional[datetime] = None
    SSEAwsKmsKeyId: Optional[str] = None
    TargetKeyPrefix: Optional[str] = None
    ObjectLockLegalHoldStatus: Optional[S3ObjectLockLegalHoldStatusType] = None
    ObjectLockMode: Optional[S3ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[datetime] = None
    BucketKeyEnabled: Optional[bool] = None
    ChecksumAlgorithm: Optional[S3ChecksumAlgorithmType] = None


class S3CopyObjectOperationTypeDef(BaseValidatorModel):
    TargetResource: Optional[str] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None
    AccessControlGrants: Optional[Sequence[S3GrantTypeDef]] = None
    MetadataDirective: Optional[S3MetadataDirectiveType] = None
    ModifiedSinceConstraint: Optional[TimestampTypeDef] = None
    NewObjectMetadata: Optional[S3ObjectMetadataTypeDef] = None
    NewObjectTagging: Optional[Sequence[S3TagTypeDef]] = None
    RedirectLocation: Optional[str] = None
    RequesterPays: Optional[bool] = None
    StorageClass: Optional[S3StorageClassType] = None
    UnModifiedSinceConstraint: Optional[TimestampTypeDef] = None
    SSEAwsKmsKeyId: Optional[str] = None
    TargetKeyPrefix: Optional[str] = None
    ObjectLockLegalHoldStatus: Optional[S3ObjectLockLegalHoldStatusType] = None
    ObjectLockMode: Optional[S3ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    BucketKeyEnabled: Optional[bool] = None
    ChecksumAlgorithm: Optional[S3ChecksumAlgorithmType] = None


class S3BucketDestinationOutputTypeDef(BaseValidatorModel):
    Format: FormatType
    OutputSchemaVersion: Literal["V_1"]
    AccountId: str
    Arn: str
    Prefix: Optional[str] = None
    Encryption: Optional[StorageLensDataExportEncryptionOutputTypeDef] = None


class S3BucketDestinationTypeDef(BaseValidatorModel):
    Format: FormatType
    OutputSchemaVersion: Literal["V_1"]
    AccountId: str
    Arn: str
    Prefix: Optional[str] = None
    Encryption: Optional[StorageLensDataExportEncryptionTypeDef] = None


class ObjectLambdaConfigurationOutputTypeDef(BaseValidatorModel):
    SupportingAccessPoint: str
    TransformationConfigurations: List[ObjectLambdaTransformationConfigurationOutputTypeDef]
    CloudWatchMetricsEnabled: Optional[bool] = None
    AllowedFeatures: Optional[List[ObjectLambdaAllowedFeatureType]] = None


class ObjectLambdaConfigurationTypeDef(BaseValidatorModel):
    SupportingAccessPoint: str
    TransformationConfigurations: Sequence[ObjectLambdaTransformationConfigurationTypeDef]
    CloudWatchMetricsEnabled: Optional[bool] = None
    AllowedFeatures: Optional[Sequence[ObjectLambdaAllowedFeatureType]] = None


class LifecycleRuleOutputTypeDef(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutputTypeDef] = None
    ID: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterOutputTypeDef] = None
    Transitions: Optional[List[TransitionOutputTypeDef]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None


class LifecycleRuleAndOperatorUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleRuleFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3TagTypeDef] = None
    And: Optional[LifecycleRuleAndOperatorUnionTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class CreateMultiRegionAccessPointInputUnionTypeDef(BaseValidatorModel):
    pass


class CreateMultiRegionAccessPointRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ClientToken: str
    Details: CreateMultiRegionAccessPointInputUnionTypeDef


class S3JobManifestGeneratorOutputTypeDef(BaseValidatorModel):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: Optional[str] = None
    ManifestOutputLocation: Optional[S3ManifestOutputLocationOutputTypeDef] = None
    Filter: Optional[JobManifestGeneratorFilterOutputTypeDef] = None


class S3JobManifestGeneratorTypeDef(BaseValidatorModel):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: Optional[str] = None
    ManifestOutputLocation: Optional[S3ManifestOutputLocationTypeDef] = None
    Filter: Optional[JobManifestGeneratorFilterTypeDef] = None


class ListJobsResultTypeDef(BaseValidatorModel):
    Jobs: List[JobListDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StorageLensGroupOutputTypeDef(BaseValidatorModel):
    Name: str
    Filter: StorageLensGroupFilterOutputTypeDef
    StorageLensGroupArn: Optional[str] = None


class StorageLensGroupTypeDef(BaseValidatorModel):
    Name: str
    Filter: StorageLensGroupFilterTypeDef
    StorageLensGroupArn: Optional[str] = None


class ReplicationRuleOutputTypeDef(BaseValidatorModel):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
    Bucket: str
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilterOutputTypeDef] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteriaTypeDef] = None
    ExistingObjectReplication: Optional[ExistingObjectReplicationTypeDef] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplicationTypeDef] = None


class ReplicationRuleTypeDef(BaseValidatorModel):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
    Bucket: str
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilterTypeDef] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteriaTypeDef] = None
    ExistingObjectReplication: Optional[ExistingObjectReplicationTypeDef] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplicationTypeDef] = None


class AsyncOperationTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    Operation: Optional[AsyncOperationNameType] = None
    RequestTokenARN: Optional[str] = None
    RequestParameters: Optional[AsyncRequestParametersTypeDef] = None
    RequestStatus: Optional[str] = None
    ResponseDetails: Optional[AsyncResponseDetailsTypeDef] = None


class BucketLevelTypeDef(BaseValidatorModel):
    ActivityMetrics: Optional[ActivityMetricsTypeDef] = None
    PrefixLevel: Optional[PrefixLevelTypeDef] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetricsTypeDef] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetricsTypeDef] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetricsTypeDef] = None


class S3AccessControlPolicyOutputTypeDef(BaseValidatorModel):
    AccessControlList: Optional[S3AccessControlListOutputTypeDef] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None


class S3AccessControlPolicyTypeDef(BaseValidatorModel):
    AccessControlList: Optional[S3AccessControlListTypeDef] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None


class StorageLensDataExportOutputTypeDef(BaseValidatorModel):
    S3BucketDestination: Optional[S3BucketDestinationOutputTypeDef] = None
    CloudWatchMetrics: Optional[CloudWatchMetricsTypeDef] = None


class StorageLensDataExportTypeDef(BaseValidatorModel):
    S3BucketDestination: Optional[S3BucketDestinationTypeDef] = None
    CloudWatchMetrics: Optional[CloudWatchMetricsTypeDef] = None


class GetAccessPointConfigurationForObjectLambdaResultTypeDef(BaseValidatorModel):
    Configuration: ObjectLambdaConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketLifecycleConfigurationResultTypeDef(BaseValidatorModel):
    Rules: List[LifecycleRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class JobManifestGeneratorOutputTypeDef(BaseValidatorModel):
    S3JobManifestGenerator: Optional[S3JobManifestGeneratorOutputTypeDef] = None


class JobManifestGeneratorTypeDef(BaseValidatorModel):
    S3JobManifestGenerator: Optional[S3JobManifestGeneratorTypeDef] = None


class GetStorageLensGroupResultTypeDef(BaseValidatorModel):
    StorageLensGroup: StorageLensGroupOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReplicationConfigurationOutputTypeDef(BaseValidatorModel):
    Role: str
    Rules: List[ReplicationRuleOutputTypeDef]


class ReplicationConfigurationTypeDef(BaseValidatorModel):
    Role: str
    Rules: Sequence[ReplicationRuleTypeDef]


class DescribeMultiRegionAccessPointOperationResultTypeDef(BaseValidatorModel):
    AsyncOperation: AsyncOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AccountLevelOutputTypeDef(BaseValidatorModel):
    BucketLevel: BucketLevelTypeDef
    ActivityMetrics: Optional[ActivityMetricsTypeDef] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetricsTypeDef] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetricsTypeDef] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetricsTypeDef] = None
    StorageLensGroupLevel: Optional[StorageLensGroupLevelOutputTypeDef] = None


class AccountLevelTypeDef(BaseValidatorModel):
    BucketLevel: BucketLevelTypeDef
    ActivityMetrics: Optional[ActivityMetricsTypeDef] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetricsTypeDef] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetricsTypeDef] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetricsTypeDef] = None
    StorageLensGroupLevel: Optional[StorageLensGroupLevelTypeDef] = None


class S3SetObjectAclOperationOutputTypeDef(BaseValidatorModel):
    AccessControlPolicy: Optional[S3AccessControlPolicyOutputTypeDef] = None


class S3SetObjectAclOperationTypeDef(BaseValidatorModel):
    AccessControlPolicy: Optional[S3AccessControlPolicyTypeDef] = None


class ObjectLambdaConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAccessPointForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationUnionTypeDef


class PutAccessPointConfigurationForObjectLambdaRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationUnionTypeDef


class LifecycleExpirationUnionTypeDef(BaseValidatorModel):
    pass


class TransitionUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleRuleFilterUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleRuleTypeDef(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationUnionTypeDef] = None
    ID: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterUnionTypeDef] = None
    Transitions: Optional[Sequence[TransitionUnionTypeDef]] = None
    NoncurrentVersionTransitions: Optional[Sequence[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None


class StorageLensGroupUnionTypeDef(BaseValidatorModel):
    pass


class CreateStorageLensGroupRequestTypeDef(BaseValidatorModel):
    AccountId: str
    StorageLensGroup: StorageLensGroupUnionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateStorageLensGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    AccountId: str
    StorageLensGroup: StorageLensGroupUnionTypeDef


class GetBucketReplicationResultTypeDef(BaseValidatorModel):
    ReplicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StorageLensConfigurationOutputTypeDef(BaseValidatorModel):
    Id: str
    AccountLevel: AccountLevelOutputTypeDef
    IsEnabled: bool
    Include: Optional[IncludeOutputTypeDef] = None
    Exclude: Optional[ExcludeOutputTypeDef] = None
    DataExport: Optional[StorageLensDataExportOutputTypeDef] = None
    AwsOrg: Optional[StorageLensAwsOrgTypeDef] = None
    StorageLensArn: Optional[str] = None


class StorageLensConfigurationTypeDef(BaseValidatorModel):
    Id: str
    AccountLevel: AccountLevelTypeDef
    IsEnabled: bool
    Include: Optional[IncludeTypeDef] = None
    Exclude: Optional[ExcludeTypeDef] = None
    DataExport: Optional[StorageLensDataExportTypeDef] = None
    AwsOrg: Optional[StorageLensAwsOrgTypeDef] = None
    StorageLensArn: Optional[str] = None


class JobOperationOutputTypeDef(BaseValidatorModel):
    LambdaInvoke: Optional[LambdaInvokeOperationOutputTypeDef] = None
    S3PutObjectCopy: Optional[S3CopyObjectOperationOutputTypeDef] = None
    S3PutObjectAcl: Optional[S3SetObjectAclOperationOutputTypeDef] = None
    S3PutObjectTagging: Optional[S3SetObjectTaggingOperationOutputTypeDef] = None
    S3DeleteObjectTagging: Optional[Dict[str, Any]] = None
    S3InitiateRestoreObject: Optional[S3InitiateRestoreObjectOperationTypeDef] = None
    S3PutObjectLegalHold: Optional[S3SetObjectLegalHoldOperationTypeDef] = None
    S3PutObjectRetention: Optional[S3SetObjectRetentionOperationOutputTypeDef] = None
    S3ReplicateObject: Optional[Dict[str, Any]] = None


class JobOperationTypeDef(BaseValidatorModel):
    LambdaInvoke: Optional[LambdaInvokeOperationTypeDef] = None
    S3PutObjectCopy: Optional[S3CopyObjectOperationTypeDef] = None
    S3PutObjectAcl: Optional[S3SetObjectAclOperationTypeDef] = None
    S3PutObjectTagging: Optional[S3SetObjectTaggingOperationTypeDef] = None
    S3DeleteObjectTagging: Optional[Mapping[str, Any]] = None
    S3InitiateRestoreObject: Optional[S3InitiateRestoreObjectOperationTypeDef] = None
    S3PutObjectLegalHold: Optional[S3SetObjectLegalHoldOperationTypeDef] = None
    S3PutObjectRetention: Optional[S3SetObjectRetentionOperationTypeDef] = None
    S3ReplicateObject: Optional[Mapping[str, Any]] = None


class ReplicationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketReplicationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationUnionTypeDef


class GetStorageLensConfigurationResultTypeDef(BaseValidatorModel):
    StorageLensConfiguration: StorageLensConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobDescriptorTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    ConfirmationRequired: Optional[bool] = None
    Description: Optional[str] = None
    JobArn: Optional[str] = None
    Status: Optional[JobStatusType] = None
    Manifest: Optional[JobManifestOutputTypeDef] = None
    Operation: Optional[JobOperationOutputTypeDef] = None
    Priority: Optional[int] = None
    ProgressSummary: Optional[JobProgressSummaryTypeDef] = None
    StatusUpdateReason: Optional[str] = None
    FailureReasons: Optional[List[JobFailureTypeDef]] = None
    Report: Optional[JobReportTypeDef] = None
    CreationTime: Optional[datetime] = None
    TerminationDate: Optional[datetime] = None
    RoleArn: Optional[str] = None
    SuspendedDate: Optional[datetime] = None
    SuspendedCause: Optional[str] = None
    ManifestGenerator: Optional[JobManifestGeneratorOutputTypeDef] = None
    GeneratedManifestDescriptor: Optional[S3GeneratedManifestDescriptorTypeDef] = None


class LifecycleRuleUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleConfigurationTypeDef(BaseValidatorModel):
    Rules: Optional[Sequence[LifecycleRuleUnionTypeDef]] = None


class StorageLensConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutStorageLensConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigId: str
    AccountId: str
    StorageLensConfiguration: StorageLensConfigurationUnionTypeDef
    Tags: Optional[Sequence[StorageLensTagTypeDef]] = None


class DescribeJobResultTypeDef(BaseValidatorModel):
    Job: JobDescriptorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobManifestGeneratorUnionTypeDef(BaseValidatorModel):
    pass


class JobOperationUnionTypeDef(BaseValidatorModel):
    pass


class JobManifestUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Operation: JobOperationUnionTypeDef
    Report: JobReportTypeDef
    ClientRequestToken: str
    Priority: int
    RoleArn: str
    ConfirmationRequired: Optional[bool] = None
    Manifest: Optional[JobManifestUnionTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[S3TagTypeDef]] = None
    ManifestGenerator: Optional[JobManifestGeneratorUnionTypeDef] = None


class PutBucketLifecycleConfigurationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Bucket: str
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None


