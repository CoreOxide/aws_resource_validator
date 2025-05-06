from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.s3control.s3control_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbortIncompleteMultipartUpload(BaseValidatorModel):
    DaysAfterInitiation: Optional[int] = None


class AccessControlTranslation(BaseValidatorModel):
    Owner: Literal['Destination']


class AccessGrantsLocationConfiguration(BaseValidatorModel):
    S3SubPrefix: Optional[str] = None


class VpcConfiguration(BaseValidatorModel):
    VpcId: str


class ActivityMetrics(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class AdvancedCostOptimizationMetrics(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class AdvancedDataProtectionMetrics(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class DetailedStatusCodesMetrics(BaseValidatorModel):
    IsEnabled: Optional[bool] = None


class AssociateAccessGrantsIdentityCenterRequest(BaseValidatorModel):
    AccountId: str
    IdentityCenterArn: str


class AsyncErrorDetails(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None
    Resource: Optional[str] = None
    RequestId: Optional[str] = None


class DeleteMultiRegionAccessPointInput(BaseValidatorModel):
    Name: str


class PutMultiRegionAccessPointPolicyInput(BaseValidatorModel):
    Name: str
    Policy: str


class AwsLambdaTransformation(BaseValidatorModel):
    FunctionArn: str
    FunctionPayload: Optional[str] = None


class CloudWatchMetrics(BaseValidatorModel):
    IsEnabled: bool


class Grantee(BaseValidatorModel):
    GranteeType: Optional[GranteeTypeType] = None
    GranteeIdentifier: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ObjectLambdaAccessPointAlias(BaseValidatorModel):
    Value: Optional[str] = None
    Status: Optional[ObjectLambdaAccessPointAliasStatusType] = None


class PublicAccessBlockConfiguration(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None


class CreateBucketConfiguration(BaseValidatorModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None


class JobReport(BaseValidatorModel):
    Enabled: bool
    Bucket: Optional[str] = None
    Format: Optional[Literal['Report_CSV_20180820']] = None
    Prefix: Optional[str] = None
    ReportScope: Optional[JobReportScopeType] = None


class S3Tag(BaseValidatorModel):
    Key: str
    Value: str


class Region(BaseValidatorModel):
    Bucket: str
    BucketAccountId: Optional[str] = None


class Credentials(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None
    Expiration: Optional[datetime] = None


class DeleteAccessGrantRequest(BaseValidatorModel):
    AccountId: str
    AccessGrantId: str


class DeleteAccessGrantsInstanceRequest(BaseValidatorModel):
    AccountId: str


class DeleteAccessGrantsInstanceResourcePolicyRequest(BaseValidatorModel):
    AccountId: str


class DeleteAccessGrantsLocationRequest(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str


class DeleteAccessPointForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteAccessPointPolicyForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteAccessPointPolicyRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteAccessPointRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class DeleteBucketLifecycleConfigurationRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketPolicyRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketReplicationRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteBucketTaggingRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class DeleteJobTaggingRequest(BaseValidatorModel):
    AccountId: str
    JobId: str


class DeleteMarkerReplication(BaseValidatorModel):
    Status: DeleteMarkerReplicationStatusType


class DeletePublicAccessBlockRequest(BaseValidatorModel):
    AccountId: str


class DeleteStorageLensConfigurationRequest(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class DeleteStorageLensConfigurationTaggingRequest(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class DeleteStorageLensGroupRequest(BaseValidatorModel):
    Name: str
    AccountId: str


class DescribeJobRequest(BaseValidatorModel):
    AccountId: str
    JobId: str


class DescribeMultiRegionAccessPointOperationRequest(BaseValidatorModel):
    AccountId: str
    RequestTokenARN: str


class EncryptionConfiguration(BaseValidatorModel):
    ReplicaKmsKeyID: Optional[str] = None


class DissociateAccessGrantsIdentityCenterRequest(BaseValidatorModel):
    AccountId: str


class EstablishedMultiRegionAccessPointPolicy(BaseValidatorModel):
    Policy: Optional[str] = None


class ExcludeOutput(BaseValidatorModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class Exclude(BaseValidatorModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class ExistingObjectReplication(BaseValidatorModel):
    Status: ExistingObjectReplicationStatusType


class SSEKMSEncryption(BaseValidatorModel):
    KeyId: str


class GetAccessGrantRequest(BaseValidatorModel):
    AccountId: str
    AccessGrantId: str


class GetAccessGrantsInstanceForPrefixRequest(BaseValidatorModel):
    AccountId: str
    S3Prefix: str


class GetAccessGrantsInstanceRequest(BaseValidatorModel):
    AccountId: str


class GetAccessGrantsInstanceResourcePolicyRequest(BaseValidatorModel):
    AccountId: str


class GetAccessGrantsLocationRequest(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str


class GetAccessPointConfigurationForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointPolicyForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointPolicyRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointPolicyStatusForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class PolicyStatus(BaseValidatorModel):
    IsPublic: Optional[bool] = None


class GetAccessPointPolicyStatusRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetAccessPointRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetBucketLifecycleConfigurationRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketPolicyRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketReplicationRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketTaggingRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetBucketVersioningRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str


class GetDataAccessRequest(BaseValidatorModel):
    AccountId: str
    Target: str
    Permission: PermissionType
    DurationSeconds: Optional[int] = None
    Privilege: Optional[PrivilegeType] = None
    TargetType: Optional[Literal['Object']] = None


class GetJobTaggingRequest(BaseValidatorModel):
    AccountId: str
    JobId: str


class GetMultiRegionAccessPointPolicyRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetMultiRegionAccessPointPolicyStatusRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetMultiRegionAccessPointRequest(BaseValidatorModel):
    AccountId: str
    Name: str


class GetMultiRegionAccessPointRoutesRequest(BaseValidatorModel):
    AccountId: str
    Mrap: str


class MultiRegionAccessPointRoute(BaseValidatorModel):
    TrafficDialPercentage: int
    Bucket: Optional[str] = None
    Region: Optional[str] = None


class GetPublicAccessBlockRequest(BaseValidatorModel):
    AccountId: str


class GetStorageLensConfigurationRequest(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class GetStorageLensConfigurationTaggingRequest(BaseValidatorModel):
    ConfigId: str
    AccountId: str


class StorageLensTag(BaseValidatorModel):
    Key: str
    Value: str


class GetStorageLensGroupRequest(BaseValidatorModel):
    Name: str
    AccountId: str


class IncludeOutput(BaseValidatorModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class Include(BaseValidatorModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class JobFailure(BaseValidatorModel):
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None


class KeyNameConstraintOutput(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnySubstring: Optional[List[str]] = None


class KeyNameConstraint(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnySubstring: Optional[List[str]] = None

Timestamp = Union[datetime, str]


class JobManifestLocation(BaseValidatorModel):
    ObjectArn: str
    ETag: str
    ObjectVersionId: Optional[str] = None


class JobManifestSpecOutput(BaseValidatorModel):
    Format: JobManifestFormatType
    Fields: Optional[List[JobManifestFieldNameType]] = None


class JobManifestSpec(BaseValidatorModel):
    Format: JobManifestFormatType
    Fields: Optional[List[JobManifestFieldNameType]] = None


class LambdaInvokeOperationOutput(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    InvocationSchemaVersion: Optional[str] = None
    UserArguments: Optional[Dict[str, str]] = None


class S3InitiateRestoreObjectOperation(BaseValidatorModel):
    ExpirationInDays: Optional[int] = None
    GlacierJobTier: Optional[S3GlacierJobTierType] = None


class LambdaInvokeOperation(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    InvocationSchemaVersion: Optional[str] = None
    UserArguments: Optional[Dict[str, str]] = None


class JobTimers(BaseValidatorModel):
    ElapsedTimeInActiveSeconds: Optional[int] = None


class LifecycleExpirationOutput(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None


class NoncurrentVersionExpiration(BaseValidatorModel):
    NoncurrentDays: Optional[int] = None
    NewerNoncurrentVersions: Optional[int] = None


class NoncurrentVersionTransition(BaseValidatorModel):
    NoncurrentDays: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class TransitionOutput(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class ListAccessGrantsInstanceEntry(BaseValidatorModel):
    AccessGrantsInstanceId: Optional[str] = None
    AccessGrantsInstanceArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    IdentityCenterArn: Optional[str] = None
    IdentityCenterInstanceArn: Optional[str] = None
    IdentityCenterApplicationArn: Optional[str] = None


class ListAccessGrantsInstancesRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccessGrantsLocationsEntry(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    AccessGrantsLocationId: Optional[str] = None
    AccessGrantsLocationArn: Optional[str] = None
    LocationScope: Optional[str] = None
    IAMRoleArn: Optional[str] = None


class ListAccessGrantsLocationsRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LocationScope: Optional[str] = None


class ListAccessGrantsRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    GranteeType: Optional[GranteeTypeType] = None
    GranteeIdentifier: Optional[str] = None
    Permission: Optional[PermissionType] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessPointsForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccessPointsRequest(BaseValidatorModel):
    AccountId: str
    Bucket: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCallerAccessGrantsEntry(BaseValidatorModel):
    Permission: Optional[PermissionType] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None


class ListCallerAccessGrantsRequest(BaseValidatorModel):
    AccountId: str
    GrantScope: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AllowedByApplication: Optional[bool] = None


class ListJobsRequest(BaseValidatorModel):
    AccountId: str
    JobStatuses: Optional[List[JobStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMultiRegionAccessPointsRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRegionalBucketsRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OutpostId: Optional[str] = None


class RegionalBucket(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    BucketArn: Optional[str] = None
    OutpostId: Optional[str] = None


class ListStorageLensConfigurationEntry(BaseValidatorModel):
    Id: str
    StorageLensArn: str
    HomeRegion: str
    IsEnabled: Optional[bool] = None


class ListStorageLensConfigurationsRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None


class ListStorageLensGroupEntry(BaseValidatorModel):
    Name: str
    StorageLensGroupArn: str
    HomeRegion: str


class ListStorageLensGroupsRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    AccountId: str
    ResourceArn: str


class MatchObjectAge(BaseValidatorModel):
    DaysGreaterThan: Optional[int] = None
    DaysLessThan: Optional[int] = None


class MatchObjectSize(BaseValidatorModel):
    BytesGreaterThan: Optional[int] = None
    BytesLessThan: Optional[int] = None


class ReplicationTimeValue(BaseValidatorModel):
    Minutes: Optional[int] = None


class ProposedMultiRegionAccessPointPolicy(BaseValidatorModel):
    Policy: Optional[str] = None


class MultiRegionAccessPointRegionalResponse(BaseValidatorModel):
    Name: Optional[str] = None
    RequestStatus: Optional[str] = None


class RegionReport(BaseValidatorModel):
    Bucket: Optional[str] = None
    Region: Optional[str] = None
    BucketAccountId: Optional[str] = None


class SelectionCriteria(BaseValidatorModel):
    Delimiter: Optional[str] = None
    MaxDepth: Optional[int] = None
    MinStorageBytesPercentage: Optional[float] = None


class PutAccessGrantsInstanceResourcePolicyRequest(BaseValidatorModel):
    AccountId: str
    Policy: str
    Organization: Optional[str] = None


class PutAccessPointPolicyForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str
    Policy: str


class PutAccessPointPolicyRequest(BaseValidatorModel):
    AccountId: str
    Name: str
    Policy: str


class PutBucketPolicyRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str
    Policy: str
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None


class VersioningConfiguration(BaseValidatorModel):
    MFADelete: Optional[MFADeleteType] = None
    Status: Optional[BucketVersioningStatusType] = None


class ReplicaModifications(BaseValidatorModel):
    Status: ReplicaModificationsStatusType


class S3ObjectOwner(BaseValidatorModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None


class S3ObjectMetadataOutput(BaseValidatorModel):
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


class S3Grantee(BaseValidatorModel):
    TypeIdentifier: Optional[S3GranteeTypeIdentifierType] = None
    Identifier: Optional[str] = None
    DisplayName: Optional[str] = None


class S3ObjectLockLegalHold(BaseValidatorModel):
    Status: S3ObjectLockLegalHoldStatusType


class S3RetentionOutput(BaseValidatorModel):
    RetainUntilDate: Optional[datetime] = None
    Mode: Optional[S3ObjectLockRetentionModeType] = None


class SSEKMS(BaseValidatorModel):
    KeyId: str


class SseKmsEncryptedObjects(BaseValidatorModel):
    Status: SseKmsEncryptedObjectsStatusType


class StorageLensAwsOrg(BaseValidatorModel):
    Arn: str


class StorageLensGroupLevelSelectionCriteriaOutput(BaseValidatorModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None


class StorageLensGroupLevelSelectionCriteria(BaseValidatorModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    AccountId: str
    ResourceArn: str
    TagKeys: List[str]


class UpdateAccessGrantsLocationRequest(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str
    IAMRoleArn: str


class UpdateJobPriorityRequest(BaseValidatorModel):
    AccountId: str
    JobId: str
    Priority: int


class UpdateJobStatusRequest(BaseValidatorModel):
    AccountId: str
    JobId: str
    RequestedJobStatus: RequestedJobStatusType
    StatusUpdateReason: Optional[str] = None


class AccessPoint(BaseValidatorModel):
    Name: str
    NetworkOrigin: NetworkOriginType
    Bucket: str
    VpcConfiguration: Optional[VpcConfiguration] = None
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    BucketAccountId: Optional[str] = None


class DeleteMultiRegionAccessPointRequest(BaseValidatorModel):
    AccountId: str
    ClientToken: str
    Details: DeleteMultiRegionAccessPointInput


class PutMultiRegionAccessPointPolicyRequest(BaseValidatorModel):
    AccountId: str
    ClientToken: str
    Details: PutMultiRegionAccessPointPolicyInput


class ObjectLambdaContentTransformation(BaseValidatorModel):
    AwsLambda: Optional[AwsLambdaTransformation] = None


class ListAccessGrantEntry(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    AccessGrantId: Optional[str] = None
    AccessGrantArn: Optional[str] = None
    Grantee: Optional[Grantee] = None
    Permission: Optional[PermissionType] = None
    AccessGrantsLocationId: Optional[str] = None
    AccessGrantsLocationConfiguration: Optional[AccessGrantsLocationConfiguration] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None


class CreateAccessGrantRequest(BaseValidatorModel):
    AccountId: str
    AccessGrantsLocationId: str
    Grantee: Grantee
    Permission: PermissionType
    AccessGrantsLocationConfiguration: Optional[AccessGrantsLocationConfiguration] = None
    ApplicationArn: Optional[str] = None
    S3PrefixType: Optional[Literal['Object']] = None
    Tags: Optional[List[Tag]] = None


class CreateAccessGrantsInstanceRequest(BaseValidatorModel):
    AccountId: str
    IdentityCenterArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateAccessGrantsLocationRequest(BaseValidatorModel):
    AccountId: str
    LocationScope: str
    IAMRoleArn: str
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    AccountId: str
    ResourceArn: str
    Tags: List[Tag]


class CreateAccessGrantResult(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantId: str
    AccessGrantArn: str
    Grantee: Grantee
    AccessGrantsLocationId: str
    AccessGrantsLocationConfiguration: AccessGrantsLocationConfiguration
    Permission: PermissionType
    ApplicationArn: str
    GrantScope: str
    ResponseMetadata: ResponseMetadata


class CreateAccessGrantsInstanceResult(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsInstanceId: str
    AccessGrantsInstanceArn: str
    IdentityCenterArn: str
    IdentityCenterInstanceArn: str
    IdentityCenterApplicationArn: str
    ResponseMetadata: ResponseMetadata


class CreateAccessGrantsLocationResult(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadata


class CreateAccessPointResult(BaseValidatorModel):
    AccessPointArn: str
    Alias: str
    ResponseMetadata: ResponseMetadata


class CreateBucketResult(BaseValidatorModel):
    Location: str
    BucketArn: str
    ResponseMetadata: ResponseMetadata


class CreateJobResult(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class CreateMultiRegionAccessPointResult(BaseValidatorModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadata


class DeleteMultiRegionAccessPointResult(BaseValidatorModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccessGrantResult(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantId: str
    AccessGrantArn: str
    Grantee: Grantee
    Permission: PermissionType
    AccessGrantsLocationId: str
    AccessGrantsLocationConfiguration: AccessGrantsLocationConfiguration
    GrantScope: str
    ApplicationArn: str
    ResponseMetadata: ResponseMetadata


class GetAccessGrantsInstanceForPrefixResult(BaseValidatorModel):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    ResponseMetadata: ResponseMetadata


class GetAccessGrantsInstanceResourcePolicyResult(BaseValidatorModel):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetAccessGrantsInstanceResult(BaseValidatorModel):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    IdentityCenterArn: str
    IdentityCenterInstanceArn: str
    IdentityCenterApplicationArn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetAccessGrantsLocationResult(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadata


class GetAccessPointPolicyForObjectLambdaResult(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetAccessPointPolicyResult(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetBucketPolicyResult(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetBucketResult(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    ResponseMetadata: ResponseMetadata


class GetBucketVersioningResult(BaseValidatorModel):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResult(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class PutAccessGrantsInstanceResourcePolicyResult(BaseValidatorModel):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class PutMultiRegionAccessPointPolicyResult(BaseValidatorModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadata


class UpdateAccessGrantsLocationResult(BaseValidatorModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadata


class UpdateJobPriorityResult(BaseValidatorModel):
    JobId: str
    Priority: int
    ResponseMetadata: ResponseMetadata


class UpdateJobStatusResult(BaseValidatorModel):
    JobId: str
    Status: JobStatusType
    StatusUpdateReason: str
    ResponseMetadata: ResponseMetadata


class CreateAccessPointForObjectLambdaResult(BaseValidatorModel):
    ObjectLambdaAccessPointArn: str
    Alias: ObjectLambdaAccessPointAlias
    ResponseMetadata: ResponseMetadata


class ObjectLambdaAccessPoint(BaseValidatorModel):
    Name: str
    ObjectLambdaAccessPointArn: Optional[str] = None
    Alias: Optional[ObjectLambdaAccessPointAlias] = None


class CreateAccessPointRequest(BaseValidatorModel):
    AccountId: str
    Name: str
    Bucket: str
    VpcConfiguration: Optional[VpcConfiguration] = None
    PublicAccessBlockConfiguration: Optional[PublicAccessBlockConfiguration] = None
    BucketAccountId: Optional[str] = None


class GetAccessPointForObjectLambdaResult(BaseValidatorModel):
    Name: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfiguration
    CreationDate: datetime
    Alias: ObjectLambdaAccessPointAlias
    ResponseMetadata: ResponseMetadata


class GetAccessPointResult(BaseValidatorModel):
    Name: str
    Bucket: str
    NetworkOrigin: NetworkOriginType
    VpcConfiguration: VpcConfiguration
    PublicAccessBlockConfiguration: PublicAccessBlockConfiguration
    CreationDate: datetime
    Alias: str
    AccessPointArn: str
    Endpoints: Dict[str, str]
    BucketAccountId: str
    ResponseMetadata: ResponseMetadata


class GetPublicAccessBlockOutput(BaseValidatorModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfiguration
    ResponseMetadata: ResponseMetadata


class PutPublicAccessBlockRequest(BaseValidatorModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfiguration
    AccountId: str


class CreateBucketRequest(BaseValidatorModel):
    Bucket: str
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfiguration] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    OutpostId: Optional[str] = None


class GetBucketTaggingResult(BaseValidatorModel):
    TagSet: List[S3Tag]
    ResponseMetadata: ResponseMetadata


class GetJobTaggingResult(BaseValidatorModel):
    Tags: List[S3Tag]
    ResponseMetadata: ResponseMetadata


class LifecycleRuleAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class LifecycleRuleAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class PutJobTaggingRequest(BaseValidatorModel):
    AccountId: str
    JobId: str
    Tags: List[S3Tag]


class ReplicationRuleAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None


class ReplicationRuleAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None


class S3SetObjectTaggingOperationOutput(BaseValidatorModel):
    TagSet: Optional[List[S3Tag]] = None


class S3SetObjectTaggingOperation(BaseValidatorModel):
    TagSet: Optional[List[S3Tag]] = None


class Tagging(BaseValidatorModel):
    TagSet: List[S3Tag]


class CreateMultiRegionAccessPointInputOutput(BaseValidatorModel):
    Name: str
    Regions: List[Region]
    PublicAccessBlock: Optional[PublicAccessBlockConfiguration] = None


class CreateMultiRegionAccessPointInput(BaseValidatorModel):
    Name: str
    Regions: List[Region]
    PublicAccessBlock: Optional[PublicAccessBlockConfiguration] = None


class GetDataAccessResult(BaseValidatorModel):
    Credentials: Credentials
    MatchedGrantTarget: str
    ResponseMetadata: ResponseMetadata


class GeneratedManifestEncryptionOutput(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSEncryption] = None


class GeneratedManifestEncryption(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSEncryption] = None


class GetAccessPointPolicyStatusForObjectLambdaResult(BaseValidatorModel):
    PolicyStatus: PolicyStatus
    ResponseMetadata: ResponseMetadata


class GetAccessPointPolicyStatusResult(BaseValidatorModel):
    PolicyStatus: PolicyStatus
    ResponseMetadata: ResponseMetadata


class GetMultiRegionAccessPointPolicyStatusResult(BaseValidatorModel):
    Established: PolicyStatus
    ResponseMetadata: ResponseMetadata


class GetMultiRegionAccessPointRoutesResult(BaseValidatorModel):
    Mrap: str
    Routes: List[MultiRegionAccessPointRoute]
    ResponseMetadata: ResponseMetadata


class SubmitMultiRegionAccessPointRoutesRequest(BaseValidatorModel):
    AccountId: str
    Mrap: str
    RouteUpdates: List[MultiRegionAccessPointRoute]


class GetStorageLensConfigurationTaggingResult(BaseValidatorModel):
    Tags: List[StorageLensTag]
    ResponseMetadata: ResponseMetadata


class PutStorageLensConfigurationTaggingRequest(BaseValidatorModel):
    ConfigId: str
    AccountId: str
    Tags: List[StorageLensTag]


class JobManifestGeneratorFilterOutput(BaseValidatorModel):
    EligibleForReplication: Optional[bool] = None
    CreatedAfter: Optional[datetime] = None
    CreatedBefore: Optional[datetime] = None
    ObjectReplicationStatuses: Optional[List[ReplicationStatusType]] = None
    KeyNameConstraint: Optional[KeyNameConstraintOutput] = None
    ObjectSizeGreaterThanBytes: Optional[int] = None
    ObjectSizeLessThanBytes: Optional[int] = None
    MatchAnyStorageClass: Optional[List[S3StorageClassType]] = None


class JobManifestGeneratorFilter(BaseValidatorModel):
    EligibleForReplication: Optional[bool] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    ObjectReplicationStatuses: Optional[List[ReplicationStatusType]] = None
    KeyNameConstraint: Optional[KeyNameConstraint] = None
    ObjectSizeGreaterThanBytes: Optional[int] = None
    ObjectSizeLessThanBytes: Optional[int] = None
    MatchAnyStorageClass: Optional[List[S3StorageClassType]] = None


class LifecycleExpiration(BaseValidatorModel):
    Date: Optional[Timestamp] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None


class S3ObjectMetadata(BaseValidatorModel):
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    UserMetadata: Optional[Dict[str, str]] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    HttpExpiresDate: Optional[Timestamp] = None
    RequesterCharged: Optional[bool] = None
    SSEAlgorithm: Optional[S3SSEAlgorithmType] = None


class S3Retention(BaseValidatorModel):
    RetainUntilDate: Optional[Timestamp] = None
    Mode: Optional[S3ObjectLockRetentionModeType] = None


class Transition(BaseValidatorModel):
    Date: Optional[Timestamp] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class S3GeneratedManifestDescriptor(BaseValidatorModel):
    Format: Optional[Literal['S3InventoryReport_CSV_20211130']] = None
    Location: Optional[JobManifestLocation] = None


class JobManifestOutput(BaseValidatorModel):
    Spec: JobManifestSpecOutput
    Location: JobManifestLocation


class JobManifest(BaseValidatorModel):
    Spec: JobManifestSpec
    Location: JobManifestLocation


class JobProgressSummary(BaseValidatorModel):
    TotalNumberOfTasks: Optional[int] = None
    NumberOfTasksSucceeded: Optional[int] = None
    NumberOfTasksFailed: Optional[int] = None
    Timers: Optional[JobTimers] = None


class ListAccessGrantsInstancesResult(BaseValidatorModel):
    AccessGrantsInstancesList: List[ListAccessGrantsInstanceEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccessGrantsLocationsResult(BaseValidatorModel):
    AccessGrantsLocationsList: List[ListAccessGrantsLocationsEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccessPointsForObjectLambdaRequestPaginate(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCallerAccessGrantsRequestPaginate(BaseValidatorModel):
    AccountId: str
    GrantScope: Optional[str] = None
    AllowedByApplication: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCallerAccessGrantsResult(BaseValidatorModel):
    CallerAccessGrantsList: List[ListCallerAccessGrantsEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRegionalBucketsResult(BaseValidatorModel):
    RegionalBucketList: List[RegionalBucket]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStorageLensConfigurationsResult(BaseValidatorModel):
    StorageLensConfigurationList: List[ListStorageLensConfigurationEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStorageLensGroupsResult(BaseValidatorModel):
    StorageLensGroupList: List[ListStorageLensGroupEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StorageLensGroupAndOperatorOutput(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3Tag]] = None
    MatchObjectAge: Optional[MatchObjectAge] = None
    MatchObjectSize: Optional[MatchObjectSize] = None


class StorageLensGroupAndOperator(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3Tag]] = None
    MatchObjectAge: Optional[MatchObjectAge] = None
    MatchObjectSize: Optional[MatchObjectSize] = None


class StorageLensGroupOrOperatorOutput(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3Tag]] = None
    MatchObjectAge: Optional[MatchObjectAge] = None
    MatchObjectSize: Optional[MatchObjectSize] = None


class StorageLensGroupOrOperator(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3Tag]] = None
    MatchObjectAge: Optional[MatchObjectAge] = None
    MatchObjectSize: Optional[MatchObjectSize] = None


class Metrics(BaseValidatorModel):
    Status: MetricsStatusType
    EventThreshold: Optional[ReplicationTimeValue] = None


class ReplicationTime(BaseValidatorModel):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValue


class MultiRegionAccessPointPolicyDocument(BaseValidatorModel):
    Established: Optional[EstablishedMultiRegionAccessPointPolicy] = None
    Proposed: Optional[ProposedMultiRegionAccessPointPolicy] = None


class MultiRegionAccessPointsAsyncResponse(BaseValidatorModel):
    Regions: Optional[List[MultiRegionAccessPointRegionalResponse]] = None


class MultiRegionAccessPointReport(BaseValidatorModel):
    Name: Optional[str] = None
    Alias: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PublicAccessBlock: Optional[PublicAccessBlockConfiguration] = None
    Status: Optional[MultiRegionAccessPointStatusType] = None
    Regions: Optional[List[RegionReport]] = None


class PrefixLevelStorageMetrics(BaseValidatorModel):
    IsEnabled: Optional[bool] = None
    SelectionCriteria: Optional[SelectionCriteria] = None


class PutBucketVersioningRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str
    VersioningConfiguration: VersioningConfiguration
    MFA: Optional[str] = None


class S3Grant(BaseValidatorModel):
    Grantee: Optional[S3Grantee] = None
    Permission: Optional[S3PermissionType] = None


class S3SetObjectLegalHoldOperation(BaseValidatorModel):
    LegalHold: S3ObjectLockLegalHold


class S3SetObjectRetentionOperationOutput(BaseValidatorModel):
    Retention: S3RetentionOutput
    BypassGovernanceRetention: Optional[bool] = None


class StorageLensDataExportEncryptionOutput(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMS] = None


class StorageLensDataExportEncryption(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMS] = None


class SourceSelectionCriteria(BaseValidatorModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjects] = None
    ReplicaModifications: Optional[ReplicaModifications] = None


class StorageLensGroupLevelOutput(BaseValidatorModel):
    SelectionCriteria: Optional[StorageLensGroupLevelSelectionCriteriaOutput] = None


class StorageLensGroupLevel(BaseValidatorModel):
    SelectionCriteria: Optional[StorageLensGroupLevelSelectionCriteria] = None


class ListAccessPointsResult(BaseValidatorModel):
    AccessPointList: List[AccessPoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ObjectLambdaTransformationConfigurationOutput(BaseValidatorModel):
    Actions: List[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformation


class ObjectLambdaTransformationConfiguration(BaseValidatorModel):
    Actions: List[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformation


class ListAccessGrantsResult(BaseValidatorModel):
    AccessGrantsList: List[ListAccessGrantEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccessPointsForObjectLambdaResult(BaseValidatorModel):
    ObjectLambdaAccessPointList: List[ObjectLambdaAccessPoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LifecycleRuleFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3Tag] = None
    And: Optional[LifecycleRuleAndOperatorOutput] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

LifecycleRuleAndOperatorUnion = Union[LifecycleRuleAndOperator, LifecycleRuleAndOperatorOutput]


class ReplicationRuleFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3Tag] = None
    And: Optional[ReplicationRuleAndOperatorOutput] = None


class ReplicationRuleFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3Tag] = None
    And: Optional[ReplicationRuleAndOperator] = None


class PutBucketTaggingRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str
    Tagging: Tagging


class AsyncRequestParameters(BaseValidatorModel):
    CreateMultiRegionAccessPointRequest: Optional[CreateMultiRegionAccessPointInputOutput] = None
    DeleteMultiRegionAccessPointRequest: Optional[DeleteMultiRegionAccessPointInput] = None
    PutMultiRegionAccessPointPolicyRequest: Optional[PutMultiRegionAccessPointPolicyInput] = None

CreateMultiRegionAccessPointInputUnion = Union[CreateMultiRegionAccessPointInput, CreateMultiRegionAccessPointInputOutput]


class S3ManifestOutputLocationOutput(BaseValidatorModel):
    Bucket: str
    ManifestFormat: Literal['S3InventoryReport_CSV_20211130']
    ExpectedManifestBucketOwner: Optional[str] = None
    ManifestPrefix: Optional[str] = None
    ManifestEncryption: Optional[GeneratedManifestEncryptionOutput] = None


class S3ManifestOutputLocation(BaseValidatorModel):
    Bucket: str
    ManifestFormat: Literal['S3InventoryReport_CSV_20211130']
    ExpectedManifestBucketOwner: Optional[str] = None
    ManifestPrefix: Optional[str] = None
    ManifestEncryption: Optional[GeneratedManifestEncryption] = None

LifecycleExpirationUnion = Union[LifecycleExpiration, LifecycleExpirationOutput]


class S3SetObjectRetentionOperation(BaseValidatorModel):
    Retention: S3Retention
    BypassGovernanceRetention: Optional[bool] = None

TransitionUnion = Union[Transition, TransitionOutput]

JobManifestUnion = Union[JobManifest, JobManifestOutput]


class JobListDescriptor(BaseValidatorModel):
    JobId: Optional[str] = None
    Description: Optional[str] = None
    Operation: Optional[OperationNameType] = None
    Priority: Optional[int] = None
    Status: Optional[JobStatusType] = None
    CreationTime: Optional[datetime] = None
    TerminationDate: Optional[datetime] = None
    ProgressSummary: Optional[JobProgressSummary] = None


class StorageLensGroupFilterOutput(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3Tag]] = None
    MatchObjectAge: Optional[MatchObjectAge] = None
    MatchObjectSize: Optional[MatchObjectSize] = None
    And: Optional[StorageLensGroupAndOperatorOutput] = None
    or_: Optional[StorageLensGroupOrOperatorOutput] = None


class StorageLensGroupFilter(BaseValidatorModel):
    MatchAnyPrefix: Optional[List[str]] = None
    MatchAnySuffix: Optional[List[str]] = None
    MatchAnyTag: Optional[List[S3Tag]] = None
    MatchObjectAge: Optional[MatchObjectAge] = None
    MatchObjectSize: Optional[MatchObjectSize] = None
    And: Optional[StorageLensGroupAndOperator] = None
    or_: Optional[StorageLensGroupOrOperator] = None


class Destination(BaseValidatorModel):
    Bucket: str
    Account: Optional[str] = None
    ReplicationTime: Optional[ReplicationTime] = None
    AccessControlTranslation: Optional[AccessControlTranslation] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    Metrics: Optional[Metrics] = None
    StorageClass: Optional[ReplicationStorageClassType] = None


class GetMultiRegionAccessPointPolicyResult(BaseValidatorModel):
    Policy: MultiRegionAccessPointPolicyDocument
    ResponseMetadata: ResponseMetadata


class AsyncResponseDetails(BaseValidatorModel):
    MultiRegionAccessPointDetails: Optional[MultiRegionAccessPointsAsyncResponse] = None
    ErrorDetails: Optional[AsyncErrorDetails] = None


class GetMultiRegionAccessPointResult(BaseValidatorModel):
    AccessPoint: MultiRegionAccessPointReport
    ResponseMetadata: ResponseMetadata


class ListMultiRegionAccessPointsResult(BaseValidatorModel):
    AccessPoints: List[MultiRegionAccessPointReport]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PrefixLevel(BaseValidatorModel):
    StorageMetrics: PrefixLevelStorageMetrics


class S3AccessControlListOutput(BaseValidatorModel):
    Owner: S3ObjectOwner
    Grants: Optional[List[S3Grant]] = None


class S3AccessControlList(BaseValidatorModel):
    Owner: S3ObjectOwner
    Grants: Optional[List[S3Grant]] = None


class S3CopyObjectOperationOutput(BaseValidatorModel):
    TargetResource: Optional[str] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None
    AccessControlGrants: Optional[List[S3Grant]] = None
    MetadataDirective: Optional[S3MetadataDirectiveType] = None
    ModifiedSinceConstraint: Optional[datetime] = None
    NewObjectMetadata: Optional[S3ObjectMetadataOutput] = None
    NewObjectTagging: Optional[List[S3Tag]] = None
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


class S3CopyObjectOperation(BaseValidatorModel):
    TargetResource: Optional[str] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None
    AccessControlGrants: Optional[List[S3Grant]] = None
    MetadataDirective: Optional[S3MetadataDirectiveType] = None
    ModifiedSinceConstraint: Optional[Timestamp] = None
    NewObjectMetadata: Optional[S3ObjectMetadata] = None
    NewObjectTagging: Optional[List[S3Tag]] = None
    RedirectLocation: Optional[str] = None
    RequesterPays: Optional[bool] = None
    StorageClass: Optional[S3StorageClassType] = None
    UnModifiedSinceConstraint: Optional[Timestamp] = None
    SSEAwsKmsKeyId: Optional[str] = None
    TargetKeyPrefix: Optional[str] = None
    ObjectLockLegalHoldStatus: Optional[S3ObjectLockLegalHoldStatusType] = None
    ObjectLockMode: Optional[S3ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    BucketKeyEnabled: Optional[bool] = None
    ChecksumAlgorithm: Optional[S3ChecksumAlgorithmType] = None


class S3BucketDestinationOutput(BaseValidatorModel):
    Format: FormatType
    OutputSchemaVersion: Literal['V_1']
    AccountId: str
    Arn: str
    Prefix: Optional[str] = None
    Encryption: Optional[StorageLensDataExportEncryptionOutput] = None


class S3BucketDestination(BaseValidatorModel):
    Format: FormatType
    OutputSchemaVersion: Literal['V_1']
    AccountId: str
    Arn: str
    Prefix: Optional[str] = None
    Encryption: Optional[StorageLensDataExportEncryption] = None


class ObjectLambdaConfigurationOutput(BaseValidatorModel):
    SupportingAccessPoint: str
    TransformationConfigurations: List[ObjectLambdaTransformationConfigurationOutput]
    CloudWatchMetricsEnabled: Optional[bool] = None
    AllowedFeatures: Optional[List[ObjectLambdaAllowedFeatureType]] = None


class ObjectLambdaConfiguration(BaseValidatorModel):
    SupportingAccessPoint: str
    TransformationConfigurations: List[ObjectLambdaTransformationConfiguration]
    CloudWatchMetricsEnabled: Optional[bool] = None
    AllowedFeatures: Optional[List[ObjectLambdaAllowedFeatureType]] = None


class LifecycleRuleOutput(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutput] = None
    ID: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterOutput] = None
    Transitions: Optional[List[TransitionOutput]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransition]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload] = None


class LifecycleRuleFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3Tag] = None
    And: Optional[LifecycleRuleAndOperatorUnion] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class CreateMultiRegionAccessPointRequest(BaseValidatorModel):
    AccountId: str
    ClientToken: str
    Details: CreateMultiRegionAccessPointInputUnion


class S3JobManifestGeneratorOutput(BaseValidatorModel):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: Optional[str] = None
    ManifestOutputLocation: Optional[S3ManifestOutputLocationOutput] = None
    Filter: Optional[JobManifestGeneratorFilterOutput] = None


class S3JobManifestGenerator(BaseValidatorModel):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: Optional[str] = None
    ManifestOutputLocation: Optional[S3ManifestOutputLocation] = None
    Filter: Optional[JobManifestGeneratorFilter] = None


class ListJobsResult(BaseValidatorModel):
    Jobs: List[JobListDescriptor]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StorageLensGroupOutput(BaseValidatorModel):
    Name: str
    Filter: StorageLensGroupFilterOutput
    StorageLensGroupArn: Optional[str] = None


class StorageLensGroup(BaseValidatorModel):
    Name: str
    Filter: StorageLensGroupFilter
    StorageLensGroupArn: Optional[str] = None


class ReplicationRuleOutput(BaseValidatorModel):
    Status: ReplicationRuleStatusType
    Destination: Destination
    Bucket: str
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilterOutput] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteria] = None
    ExistingObjectReplication: Optional[ExistingObjectReplication] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplication] = None


class ReplicationRule(BaseValidatorModel):
    Status: ReplicationRuleStatusType
    Destination: Destination
    Bucket: str
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilter] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteria] = None
    ExistingObjectReplication: Optional[ExistingObjectReplication] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplication] = None


class AsyncOperation(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    Operation: Optional[AsyncOperationNameType] = None
    RequestTokenARN: Optional[str] = None
    RequestParameters: Optional[AsyncRequestParameters] = None
    RequestStatus: Optional[str] = None
    ResponseDetails: Optional[AsyncResponseDetails] = None


class BucketLevel(BaseValidatorModel):
    ActivityMetrics: Optional[ActivityMetrics] = None
    PrefixLevel: Optional[PrefixLevel] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetrics] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetrics] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetrics] = None


class S3AccessControlPolicyOutput(BaseValidatorModel):
    AccessControlList: Optional[S3AccessControlListOutput] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None


class S3AccessControlPolicy(BaseValidatorModel):
    AccessControlList: Optional[S3AccessControlList] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None


class StorageLensDataExportOutput(BaseValidatorModel):
    S3BucketDestination: Optional[S3BucketDestinationOutput] = None
    CloudWatchMetrics: Optional[CloudWatchMetrics] = None


class StorageLensDataExport(BaseValidatorModel):
    S3BucketDestination: Optional[S3BucketDestination] = None
    CloudWatchMetrics: Optional[CloudWatchMetrics] = None


class GetAccessPointConfigurationForObjectLambdaResult(BaseValidatorModel):
    Configuration: ObjectLambdaConfigurationOutput
    ResponseMetadata: ResponseMetadata

ObjectLambdaConfigurationUnion = Union[ObjectLambdaConfiguration, ObjectLambdaConfigurationOutput]


class GetBucketLifecycleConfigurationResult(BaseValidatorModel):
    Rules: List[LifecycleRuleOutput]
    ResponseMetadata: ResponseMetadata

LifecycleRuleFilterUnion = Union[LifecycleRuleFilter, LifecycleRuleFilterOutput]


class JobManifestGeneratorOutput(BaseValidatorModel):
    S3JobManifestGenerator: Optional[S3JobManifestGeneratorOutput] = None


class JobManifestGenerator(BaseValidatorModel):
    S3JobManifestGenerator: Optional[S3JobManifestGenerator] = None


class GetStorageLensGroupResult(BaseValidatorModel):
    StorageLensGroup: StorageLensGroupOutput
    ResponseMetadata: ResponseMetadata

StorageLensGroupUnion = Union[StorageLensGroup, StorageLensGroupOutput]


class ReplicationConfigurationOutput(BaseValidatorModel):
    Role: str
    Rules: List[ReplicationRuleOutput]


class ReplicationConfiguration(BaseValidatorModel):
    Role: str
    Rules: List[ReplicationRule]


class DescribeMultiRegionAccessPointOperationResult(BaseValidatorModel):
    AsyncOperation: AsyncOperation
    ResponseMetadata: ResponseMetadata


class AccountLevelOutput(BaseValidatorModel):
    BucketLevel: BucketLevel
    ActivityMetrics: Optional[ActivityMetrics] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetrics] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetrics] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetrics] = None
    StorageLensGroupLevel: Optional[StorageLensGroupLevelOutput] = None


class AccountLevel(BaseValidatorModel):
    BucketLevel: BucketLevel
    ActivityMetrics: Optional[ActivityMetrics] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetrics] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetrics] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetrics] = None
    StorageLensGroupLevel: Optional[StorageLensGroupLevel] = None


class S3SetObjectAclOperationOutput(BaseValidatorModel):
    AccessControlPolicy: Optional[S3AccessControlPolicyOutput] = None


class S3SetObjectAclOperation(BaseValidatorModel):
    AccessControlPolicy: Optional[S3AccessControlPolicy] = None


class CreateAccessPointForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationUnion


class PutAccessPointConfigurationForObjectLambdaRequest(BaseValidatorModel):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationUnion


class LifecycleRule(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationUnion] = None
    ID: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterUnion] = None
    Transitions: Optional[List[TransitionUnion]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransition]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload] = None

JobManifestGeneratorUnion = Union[JobManifestGenerator, JobManifestGeneratorOutput]


class CreateStorageLensGroupRequest(BaseValidatorModel):
    AccountId: str
    StorageLensGroup: StorageLensGroupUnion
    Tags: Optional[List[Tag]] = None


class UpdateStorageLensGroupRequest(BaseValidatorModel):
    Name: str
    AccountId: str
    StorageLensGroup: StorageLensGroupUnion


class GetBucketReplicationResult(BaseValidatorModel):
    ReplicationConfiguration: ReplicationConfigurationOutput
    ResponseMetadata: ResponseMetadata

ReplicationConfigurationUnion = Union[ReplicationConfiguration, ReplicationConfigurationOutput]


class StorageLensConfigurationOutput(BaseValidatorModel):
    Id: str
    AccountLevel: AccountLevelOutput
    IsEnabled: bool
    Include: Optional[IncludeOutput] = None
    Exclude: Optional[ExcludeOutput] = None
    DataExport: Optional[StorageLensDataExportOutput] = None
    AwsOrg: Optional[StorageLensAwsOrg] = None
    StorageLensArn: Optional[str] = None


class StorageLensConfiguration(BaseValidatorModel):
    Id: str
    AccountLevel: AccountLevel
    IsEnabled: bool
    Include: Optional[Include] = None
    Exclude: Optional[Exclude] = None
    DataExport: Optional[StorageLensDataExport] = None
    AwsOrg: Optional[StorageLensAwsOrg] = None
    StorageLensArn: Optional[str] = None


class JobOperationOutput(BaseValidatorModel):
    LambdaInvoke: Optional[LambdaInvokeOperationOutput] = None
    S3PutObjectCopy: Optional[S3CopyObjectOperationOutput] = None
    S3PutObjectAcl: Optional[S3SetObjectAclOperationOutput] = None
    S3PutObjectTagging: Optional[S3SetObjectTaggingOperationOutput] = None
    S3DeleteObjectTagging: Optional[Dict[str, Any]] = None
    S3InitiateRestoreObject: Optional[S3InitiateRestoreObjectOperation] = None
    S3PutObjectLegalHold: Optional[S3SetObjectLegalHoldOperation] = None
    S3PutObjectRetention: Optional[S3SetObjectRetentionOperationOutput] = None
    S3ReplicateObject: Optional[Dict[str, Any]] = None


class JobOperation(BaseValidatorModel):
    LambdaInvoke: Optional[LambdaInvokeOperation] = None
    S3PutObjectCopy: Optional[S3CopyObjectOperation] = None
    S3PutObjectAcl: Optional[S3SetObjectAclOperation] = None
    S3PutObjectTagging: Optional[S3SetObjectTaggingOperation] = None
    S3DeleteObjectTagging: Optional[Dict[str, Any]] = None
    S3InitiateRestoreObject: Optional[S3InitiateRestoreObjectOperation] = None
    S3PutObjectLegalHold: Optional[S3SetObjectLegalHoldOperation] = None
    S3PutObjectRetention: Optional[S3SetObjectRetentionOperation] = None
    S3ReplicateObject: Optional[Dict[str, Any]] = None

LifecycleRuleUnion = Union[LifecycleRule, LifecycleRuleOutput]


class PutBucketReplicationRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationUnion


class GetStorageLensConfigurationResult(BaseValidatorModel):
    StorageLensConfiguration: StorageLensConfigurationOutput
    ResponseMetadata: ResponseMetadata

StorageLensConfigurationUnion = Union[StorageLensConfiguration, StorageLensConfigurationOutput]


class JobDescriptor(BaseValidatorModel):
    JobId: Optional[str] = None
    ConfirmationRequired: Optional[bool] = None
    Description: Optional[str] = None
    JobArn: Optional[str] = None
    Status: Optional[JobStatusType] = None
    Manifest: Optional[JobManifestOutput] = None
    Operation: Optional[JobOperationOutput] = None
    Priority: Optional[int] = None
    ProgressSummary: Optional[JobProgressSummary] = None
    StatusUpdateReason: Optional[str] = None
    FailureReasons: Optional[List[JobFailure]] = None
    Report: Optional[JobReport] = None
    CreationTime: Optional[datetime] = None
    TerminationDate: Optional[datetime] = None
    RoleArn: Optional[str] = None
    SuspendedDate: Optional[datetime] = None
    SuspendedCause: Optional[str] = None
    ManifestGenerator: Optional[JobManifestGeneratorOutput] = None
    GeneratedManifestDescriptor: Optional[S3GeneratedManifestDescriptor] = None

JobOperationUnion = Union[JobOperation, JobOperationOutput]


class LifecycleConfiguration(BaseValidatorModel):
    Rules: Optional[List[LifecycleRuleUnion]] = None


class PutStorageLensConfigurationRequest(BaseValidatorModel):
    ConfigId: str
    AccountId: str
    StorageLensConfiguration: StorageLensConfigurationUnion
    Tags: Optional[List[StorageLensTag]] = None


class DescribeJobResult(BaseValidatorModel):
    Job: JobDescriptor
    ResponseMetadata: ResponseMetadata


class CreateJobRequest(BaseValidatorModel):
    AccountId: str
    Operation: JobOperationUnion
    Report: JobReport
    ClientRequestToken: str
    Priority: int
    RoleArn: str
    ConfirmationRequired: Optional[bool] = None
    Manifest: Optional[JobManifestUnion] = None
    Description: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None
    ManifestGenerator: Optional[JobManifestGeneratorUnion] = None


class PutBucketLifecycleConfigurationRequest(BaseValidatorModel):
    AccountId: str
    Bucket: str
    LifecycleConfiguration: Optional[LifecycleConfiguration] = None