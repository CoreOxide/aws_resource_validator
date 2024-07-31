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
from aws_resource_validator.pydantic_models.s3control_constants import *

class AbortIncompleteMultipartUploadTypeDef(BaseModel):
    DaysAfterInitiation: Optional[int] = None

class AccessControlTranslationTypeDef(BaseModel):
    Owner: Literal["Destination"]

class AccessGrantsLocationConfigurationTypeDef(BaseModel):
    S3SubPrefix: Optional[str] = None

class VpcConfigurationTypeDef(BaseModel):
    VpcId: str

class ActivityMetricsTypeDef(BaseModel):
    IsEnabled: Optional[bool] = None

class AdvancedCostOptimizationMetricsTypeDef(BaseModel):
    IsEnabled: Optional[bool] = None

class AdvancedDataProtectionMetricsTypeDef(BaseModel):
    IsEnabled: Optional[bool] = None

class DetailedStatusCodesMetricsTypeDef(BaseModel):
    IsEnabled: Optional[bool] = None

class AssociateAccessGrantsIdentityCenterRequestRequestTypeDef(BaseModel):
    AccountId: str
    IdentityCenterArn: str

class AsyncErrorDetailsTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None
    Resource: Optional[str] = None
    RequestId: Optional[str] = None

class DeleteMultiRegionAccessPointInputTypeDef(BaseModel):
    Name: str

class PutMultiRegionAccessPointPolicyInputTypeDef(BaseModel):
    Name: str
    Policy: str

class AwsLambdaTransformationTypeDef(BaseModel):
    FunctionArn: str
    FunctionPayload: Optional[str] = None

class CloudWatchMetricsTypeDef(BaseModel):
    IsEnabled: bool

class GranteeTypeDef(BaseModel):
    GranteeType: Optional[GranteeTypeType] = None
    GranteeIdentifier: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ObjectLambdaAccessPointAliasTypeDef(BaseModel):
    Value: Optional[str] = None
    Status: Optional[ObjectLambdaAccessPointAliasStatusType] = None

class PublicAccessBlockConfigurationTypeDef(BaseModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None

class CreateBucketConfigurationTypeDef(BaseModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None

class JobReportTypeDef(BaseModel):
    Enabled: bool
    Bucket: Optional[str] = None
    Format: Optional[Literal["Report_CSV_20180820"]] = None
    Prefix: Optional[str] = None
    ReportScope: Optional[JobReportScopeType] = None

class S3TagTypeDef(BaseModel):
    Key: str
    Value: str

class RegionTypeDef(BaseModel):
    Bucket: str
    BucketAccountId: Optional[str] = None

class CredentialsTypeDef(BaseModel):
    AccessKeyId: Optional[str] = None
    SecretAccessKey: Optional[str] = None
    SessionToken: Optional[str] = None
    Expiration: Optional[datetime] = None

class DeleteAccessGrantRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccessGrantId: str

class DeleteAccessGrantsInstanceRequestRequestTypeDef(BaseModel):
    AccountId: str

class DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef(BaseModel):
    AccountId: str

class DeleteAccessGrantsLocationRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccessGrantsLocationId: str

class DeleteAccessPointForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class DeleteAccessPointPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class DeleteAccessPointRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class DeleteBucketLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class DeleteBucketPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class DeleteBucketReplicationRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class DeleteBucketRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class DeleteBucketTaggingRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class DeleteJobTaggingRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobId: str

class DeleteMarkerReplicationTypeDef(BaseModel):
    Status: DeleteMarkerReplicationStatusType

class DeletePublicAccessBlockRequestRequestTypeDef(BaseModel):
    AccountId: str

class DeleteStorageLensConfigurationRequestRequestTypeDef(BaseModel):
    ConfigId: str
    AccountId: str

class DeleteStorageLensConfigurationTaggingRequestRequestTypeDef(BaseModel):
    ConfigId: str
    AccountId: str

class DeleteStorageLensGroupRequestRequestTypeDef(BaseModel):
    Name: str
    AccountId: str

class DescribeJobRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobId: str

class DescribeMultiRegionAccessPointOperationRequestRequestTypeDef(BaseModel):
    AccountId: str
    RequestTokenARN: str

class EncryptionConfigurationTypeDef(BaseModel):
    ReplicaKmsKeyID: Optional[str] = None

class DissociateAccessGrantsIdentityCenterRequestRequestTypeDef(BaseModel):
    AccountId: str

class EstablishedMultiRegionAccessPointPolicyTypeDef(BaseModel):
    Policy: Optional[str] = None

class ExcludeTypeDef(BaseModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None

class ExistingObjectReplicationTypeDef(BaseModel):
    Status: ExistingObjectReplicationStatusType

class SSEKMSEncryptionTypeDef(BaseModel):
    KeyId: str

class GetAccessGrantRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccessGrantId: str

class GetAccessGrantsInstanceForPrefixRequestRequestTypeDef(BaseModel):
    AccountId: str
    S3Prefix: str

class GetAccessGrantsInstanceRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetAccessGrantsLocationRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccessGrantsLocationId: str

class GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetAccessPointForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetAccessPointPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class PolicyStatusTypeDef(BaseModel):
    IsPublic: Optional[bool] = None

class GetAccessPointPolicyStatusRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetAccessPointRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetBucketLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class GetBucketPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class GetBucketReplicationRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class GetBucketRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class GetBucketTaggingRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class GetBucketVersioningRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str

class GetDataAccessRequestRequestTypeDef(BaseModel):
    AccountId: str
    Target: str
    Permission: PermissionType
    DurationSeconds: Optional[int] = None
    Privilege: Optional[PrivilegeType] = None
    TargetType: Optional[Literal["Object"]] = None

class GetJobTaggingRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobId: str

class GetMultiRegionAccessPointPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetMultiRegionAccessPointRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str

class GetMultiRegionAccessPointRoutesRequestRequestTypeDef(BaseModel):
    AccountId: str
    Mrap: str

class MultiRegionAccessPointRouteTypeDef(BaseModel):
    TrafficDialPercentage: int
    Bucket: Optional[str] = None
    Region: Optional[str] = None

class GetPublicAccessBlockRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetStorageLensConfigurationRequestRequestTypeDef(BaseModel):
    ConfigId: str
    AccountId: str

class GetStorageLensConfigurationTaggingRequestRequestTypeDef(BaseModel):
    ConfigId: str
    AccountId: str

class StorageLensTagTypeDef(BaseModel):
    Key: str
    Value: str

class GetStorageLensGroupRequestRequestTypeDef(BaseModel):
    Name: str
    AccountId: str

class IncludeTypeDef(BaseModel):
    Buckets: Optional[List[str]] = None
    Regions: Optional[List[str]] = None

class JobFailureTypeDef(BaseModel):
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None

class KeyNameConstraintTypeDef(BaseModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnySubstring: Optional[Sequence[str]] = None

class JobManifestLocationTypeDef(BaseModel):
    ObjectArn: str
    ETag: str
    ObjectVersionId: Optional[str] = None

class JobManifestSpecTypeDef(BaseModel):
    Format: JobManifestFormatType
    Fields: Optional[Sequence[JobManifestFieldNameType]] = None

class LambdaInvokeOperationTypeDef(BaseModel):
    FunctionArn: Optional[str] = None
    InvocationSchemaVersion: Optional[str] = None
    UserArguments: Optional[Mapping[str, str]] = None

class S3InitiateRestoreObjectOperationTypeDef(BaseModel):
    ExpirationInDays: Optional[int] = None
    GlacierJobTier: Optional[S3GlacierJobTierType] = None

class JobTimersTypeDef(BaseModel):
    ElapsedTimeInActiveSeconds: Optional[int] = None

class LifecycleExpirationTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class NoncurrentVersionExpirationTypeDef(BaseModel):
    NoncurrentDays: Optional[int] = None
    NewerNoncurrentVersions: Optional[int] = None

class NoncurrentVersionTransitionTypeDef(BaseModel):
    NoncurrentDays: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class TransitionTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class ListAccessGrantsInstanceEntryTypeDef(BaseModel):
    AccessGrantsInstanceId: Optional[str] = None
    AccessGrantsInstanceArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    IdentityCenterArn: Optional[str] = None

class ListAccessGrantsInstancesRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAccessGrantsLocationsEntryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    AccessGrantsLocationId: Optional[str] = None
    AccessGrantsLocationArn: Optional[str] = None
    LocationScope: Optional[str] = None
    IAMRoleArn: Optional[str] = None

class ListAccessGrantsLocationsRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LocationScope: Optional[str] = None

class ListAccessGrantsRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    GranteeType: Optional[GranteeTypeType] = None
    GranteeIdentifier: Optional[str] = None
    Permission: Optional[PermissionType] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessPointsForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAccessPointsRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobStatuses: Optional[Sequence[JobStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMultiRegionAccessPointsRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRegionalBucketsRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OutpostId: Optional[str] = None

class RegionalBucketTypeDef(BaseModel):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    BucketArn: Optional[str] = None
    OutpostId: Optional[str] = None

class ListStorageLensConfigurationEntryTypeDef(BaseModel):
    Id: str
    StorageLensArn: str
    HomeRegion: str
    IsEnabled: Optional[bool] = None

class ListStorageLensConfigurationsRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None

class ListStorageLensGroupEntryTypeDef(BaseModel):
    Name: str
    StorageLensGroupArn: str
    HomeRegion: str

class ListStorageLensGroupsRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    AccountId: str
    ResourceArn: str

class MatchObjectAgeTypeDef(BaseModel):
    DaysGreaterThan: Optional[int] = None
    DaysLessThan: Optional[int] = None

class MatchObjectSizeTypeDef(BaseModel):
    BytesGreaterThan: Optional[int] = None
    BytesLessThan: Optional[int] = None

class ReplicationTimeValueTypeDef(BaseModel):
    Minutes: Optional[int] = None

class ProposedMultiRegionAccessPointPolicyTypeDef(BaseModel):
    Policy: Optional[str] = None

class MultiRegionAccessPointRegionalResponseTypeDef(BaseModel):
    Name: Optional[str] = None
    RequestStatus: Optional[str] = None

class RegionReportTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Region: Optional[str] = None
    BucketAccountId: Optional[str] = None

class SelectionCriteriaTypeDef(BaseModel):
    Delimiter: Optional[str] = None
    MaxDepth: Optional[int] = None
    MinStorageBytesPercentage: Optional[float] = None

class PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Policy: str
    Organization: Optional[str] = None

class PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str
    Policy: str

class PutAccessPointPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str
    Policy: str

class PutBucketPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str
    Policy: str
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None

class VersioningConfigurationTypeDef(BaseModel):
    MFADelete: Optional[MFADeleteType] = None
    Status: Optional[BucketVersioningStatusType] = None

class ReplicaModificationsTypeDef(BaseModel):
    Status: ReplicaModificationsStatusType

class S3ObjectOwnerTypeDef(BaseModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None

class S3GranteeTypeDef(BaseModel):
    TypeIdentifier: Optional[S3GranteeTypeIdentifierType] = None
    Identifier: Optional[str] = None
    DisplayName: Optional[str] = None

class S3ObjectLockLegalHoldTypeDef(BaseModel):
    Status: S3ObjectLockLegalHoldStatusType

class SSEKMSTypeDef(BaseModel):
    KeyId: str

class SseKmsEncryptedObjectsTypeDef(BaseModel):
    Status: SseKmsEncryptedObjectsStatusType

class StorageLensAwsOrgTypeDef(BaseModel):
    Arn: str

class StorageLensGroupLevelSelectionCriteriaTypeDef(BaseModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    AccountId: str
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAccessGrantsLocationRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccessGrantsLocationId: str
    IAMRoleArn: str

class UpdateJobPriorityRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobId: str
    Priority: int

class UpdateJobStatusRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobId: str
    RequestedJobStatus: RequestedJobStatusType
    StatusUpdateReason: Optional[str] = None

class AccessPointTypeDef(BaseModel):
    Name: str
    NetworkOrigin: NetworkOriginType
    Bucket: str
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    BucketAccountId: Optional[str] = None

class DeleteMultiRegionAccessPointRequestRequestTypeDef(BaseModel):
    AccountId: str
    ClientToken: str
    Details: DeleteMultiRegionAccessPointInputTypeDef

class PutMultiRegionAccessPointPolicyRequestRequestTypeDef(BaseModel):
    AccountId: str
    ClientToken: str
    Details: PutMultiRegionAccessPointPolicyInputTypeDef

class ObjectLambdaContentTransformationTypeDef(BaseModel):
    AwsLambda: Optional[AwsLambdaTransformationTypeDef] = None

class ListAccessGrantEntryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    AccessGrantId: Optional[str] = None
    AccessGrantArn: Optional[str] = None
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None
    AccessGrantsLocationId: Optional[str] = None
    AccessGrantsLocationConfiguration: Optional[AccessGrantsLocationConfigurationTypeDef] = None
    GrantScope: Optional[str] = None
    ApplicationArn: Optional[str] = None

class CreateAccessGrantRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccessGrantsLocationId: str
    Grantee: GranteeTypeDef
    Permission: PermissionType
    AccessGrantsLocationConfiguration: Optional[AccessGrantsLocationConfigurationTypeDef] = None
    ApplicationArn: Optional[str] = None
    S3PrefixType: Optional[Literal["Object"]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAccessGrantsInstanceRequestRequestTypeDef(BaseModel):
    AccountId: str
    IdentityCenterArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAccessGrantsLocationRequestRequestTypeDef(BaseModel):
    AccountId: str
    LocationScope: str
    IAMRoleArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    AccountId: str
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAccessGrantResultTypeDef(BaseModel):
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

class CreateAccessGrantsInstanceResultTypeDef(BaseModel):
    CreatedAt: datetime
    AccessGrantsInstanceId: str
    AccessGrantsInstanceArn: str
    IdentityCenterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessGrantsLocationResultTypeDef(BaseModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointResultTypeDef(BaseModel):
    AccessPointArn: str
    Alias: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBucketResultTypeDef(BaseModel):
    Location: str
    BucketArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResultTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultiRegionAccessPointResultTypeDef(BaseModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMultiRegionAccessPointResultTypeDef(BaseModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantResultTypeDef(BaseModel):
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

class GetAccessGrantsInstanceForPrefixResultTypeDef(BaseModel):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsInstanceResourcePolicyResultTypeDef(BaseModel):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsInstanceResultTypeDef(BaseModel):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    IdentityCenterArn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsLocationResultTypeDef(BaseModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointPolicyForObjectLambdaResultTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointPolicyResultTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketPolicyResultTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketResultTypeDef(BaseModel):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketVersioningResultTypeDef(BaseModel):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccessGrantsInstanceResourcePolicyResultTypeDef(BaseModel):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutMultiRegionAccessPointPolicyResultTypeDef(BaseModel):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessGrantsLocationResultTypeDef(BaseModel):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobPriorityResultTypeDef(BaseModel):
    JobId: str
    Priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobStatusResultTypeDef(BaseModel):
    JobId: str
    Status: JobStatusType
    StatusUpdateReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointForObjectLambdaResultTypeDef(BaseModel):
    ObjectLambdaAccessPointArn: str
    Alias: ObjectLambdaAccessPointAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ObjectLambdaAccessPointTypeDef(BaseModel):
    Name: str
    ObjectLambdaAccessPointArn: Optional[str] = None
    Alias: Optional[ObjectLambdaAccessPointAliasTypeDef] = None

class CreateAccessPointRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str
    Bucket: str
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    PublicAccessBlockConfiguration: Optional[PublicAccessBlockConfigurationTypeDef] = None
    BucketAccountId: Optional[str] = None

class GetAccessPointForObjectLambdaResultTypeDef(BaseModel):
    Name: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    CreationDate: datetime
    Alias: ObjectLambdaAccessPointAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointResultTypeDef(BaseModel):
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

class GetPublicAccessBlockOutputTypeDef(BaseModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPublicAccessBlockRequestRequestTypeDef(BaseModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    AccountId: str

class CreateBucketRequestRequestTypeDef(BaseModel):
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

class GetBucketTaggingResultTypeDef(BaseModel):
    TagSet: List[S3TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobTaggingResultTypeDef(BaseModel):
    Tags: List[S3TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleRuleAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

class PutJobTaggingRequestRequestTypeDef(BaseModel):
    AccountId: str
    JobId: str
    Tags: Sequence[S3TagTypeDef]

class ReplicationRuleAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[S3TagTypeDef]] = None

class S3SetObjectTaggingOperationTypeDef(BaseModel):
    TagSet: Optional[Sequence[S3TagTypeDef]] = None

class TaggingTypeDef(BaseModel):
    TagSet: Sequence[S3TagTypeDef]

class CreateMultiRegionAccessPointInputTypeDef(BaseModel):
    Name: str
    Regions: Sequence[RegionTypeDef]
    PublicAccessBlock: Optional[PublicAccessBlockConfigurationTypeDef] = None

class GetDataAccessResultTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    MatchedGrantTarget: str
    ResponseMetadata: ResponseMetadataTypeDef

class GeneratedManifestEncryptionTypeDef(BaseModel):
    SSES3: Optional[Mapping[str, Any]] = None
    SSEKMS: Optional[SSEKMSEncryptionTypeDef] = None

class GetAccessPointPolicyStatusForObjectLambdaResultTypeDef(BaseModel):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointPolicyStatusResultTypeDef(BaseModel):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMultiRegionAccessPointPolicyStatusResultTypeDef(BaseModel):
    Established: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMultiRegionAccessPointRoutesResultTypeDef(BaseModel):
    Mrap: str
    Routes: List[MultiRegionAccessPointRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef(BaseModel):
    AccountId: str
    Mrap: str
    RouteUpdates: Sequence[MultiRegionAccessPointRouteTypeDef]

class GetStorageLensConfigurationTaggingResultTypeDef(BaseModel):
    Tags: List[StorageLensTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutStorageLensConfigurationTaggingRequestRequestTypeDef(BaseModel):
    ConfigId: str
    AccountId: str
    Tags: Sequence[StorageLensTagTypeDef]

class JobManifestGeneratorFilterTypeDef(BaseModel):
    EligibleForReplication: Optional[bool] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    ObjectReplicationStatuses: Optional[Sequence[ReplicationStatusType]] = None
    KeyNameConstraint: Optional[KeyNameConstraintTypeDef] = None
    ObjectSizeGreaterThanBytes: Optional[int] = None
    ObjectSizeLessThanBytes: Optional[int] = None
    MatchAnyStorageClass: Optional[Sequence[S3StorageClassType]] = None

class S3ObjectMetadataTypeDef(BaseModel):
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

class S3RetentionTypeDef(BaseModel):
    RetainUntilDate: Optional[TimestampTypeDef] = None
    Mode: Optional[S3ObjectLockRetentionModeType] = None

class S3GeneratedManifestDescriptorTypeDef(BaseModel):
    Format: Optional[Literal["S3InventoryReport_CSV_20211130"]] = None
    Location: Optional[JobManifestLocationTypeDef] = None

class JobManifestTypeDef(BaseModel):
    Spec: JobManifestSpecTypeDef
    Location: JobManifestLocationTypeDef

class JobProgressSummaryTypeDef(BaseModel):
    TotalNumberOfTasks: Optional[int] = None
    NumberOfTasksSucceeded: Optional[int] = None
    NumberOfTasksFailed: Optional[int] = None
    Timers: Optional[JobTimersTypeDef] = None

class ListAccessGrantsInstancesResultTypeDef(BaseModel):
    NextToken: str
    AccessGrantsInstancesList: List[ListAccessGrantsInstanceEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessGrantsLocationsResultTypeDef(BaseModel):
    NextToken: str
    AccessGrantsLocationsList: List[ListAccessGrantsLocationsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef(BaseModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegionalBucketsResultTypeDef(BaseModel):
    RegionalBucketList: List[RegionalBucketTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageLensConfigurationsResultTypeDef(BaseModel):
    NextToken: str
    StorageLensConfigurationList: List[ListStorageLensConfigurationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageLensGroupsResultTypeDef(BaseModel):
    NextToken: str
    StorageLensGroupList: List[ListStorageLensGroupEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StorageLensGroupAndOperatorTypeDef(BaseModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnyTag: Optional[Sequence[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None

class StorageLensGroupOrOperatorTypeDef(BaseModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnyTag: Optional[Sequence[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None

class MetricsTypeDef(BaseModel):
    Status: MetricsStatusType
    EventThreshold: Optional[ReplicationTimeValueTypeDef] = None

class ReplicationTimeTypeDef(BaseModel):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValueTypeDef

class MultiRegionAccessPointPolicyDocumentTypeDef(BaseModel):
    Established: Optional[EstablishedMultiRegionAccessPointPolicyTypeDef] = None
    Proposed: Optional[ProposedMultiRegionAccessPointPolicyTypeDef] = None

class MultiRegionAccessPointsAsyncResponseTypeDef(BaseModel):
    Regions: Optional[List[MultiRegionAccessPointRegionalResponseTypeDef]] = None

class MultiRegionAccessPointReportTypeDef(BaseModel):
    Name: Optional[str] = None
    Alias: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PublicAccessBlock: Optional[PublicAccessBlockConfigurationTypeDef] = None
    Status: Optional[MultiRegionAccessPointStatusType] = None
    Regions: Optional[List[RegionReportTypeDef]] = None

class PrefixLevelStorageMetricsTypeDef(BaseModel):
    IsEnabled: Optional[bool] = None
    SelectionCriteria: Optional[SelectionCriteriaTypeDef] = None

class PutBucketVersioningRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str
    VersioningConfiguration: VersioningConfigurationTypeDef
    MFA: Optional[str] = None

class S3GrantTypeDef(BaseModel):
    Grantee: Optional[S3GranteeTypeDef] = None
    Permission: Optional[S3PermissionType] = None

class S3SetObjectLegalHoldOperationTypeDef(BaseModel):
    LegalHold: S3ObjectLockLegalHoldTypeDef

class StorageLensDataExportEncryptionTypeDef(BaseModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None

class SourceSelectionCriteriaTypeDef(BaseModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjectsTypeDef] = None
    ReplicaModifications: Optional[ReplicaModificationsTypeDef] = None

class StorageLensGroupLevelTypeDef(BaseModel):
    SelectionCriteria: Optional[StorageLensGroupLevelSelectionCriteriaTypeDef] = None

class ListAccessPointsResultTypeDef(BaseModel):
    AccessPointList: List[AccessPointTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ObjectLambdaTransformationConfigurationTypeDef(BaseModel):
    Actions: Sequence[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformationTypeDef

class ListAccessGrantsResultTypeDef(BaseModel):
    NextToken: str
    AccessGrantsList: List[ListAccessGrantEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPointsForObjectLambdaResultTypeDef(BaseModel):
    ObjectLambdaAccessPointList: List[ObjectLambdaAccessPointTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleRuleFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3TagTypeDef] = None
    And: Optional[LifecycleRuleAndOperatorTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

class ReplicationRuleFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[S3TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorTypeDef] = None

class PutBucketTaggingRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str
    Tagging: TaggingTypeDef

class AsyncRequestParametersTypeDef(BaseModel):
    CreateMultiRegionAccessPointRequest: Optional[       CreateMultiRegionAccessPointInputTypeDef     ] = None
    DeleteMultiRegionAccessPointRequest: Optional[       DeleteMultiRegionAccessPointInputTypeDef     ] = None
    PutMultiRegionAccessPointPolicyRequest: Optional[       PutMultiRegionAccessPointPolicyInputTypeDef     ] = None

class CreateMultiRegionAccessPointRequestRequestTypeDef(BaseModel):
    AccountId: str
    ClientToken: str
    Details: CreateMultiRegionAccessPointInputTypeDef

class S3ManifestOutputLocationTypeDef(BaseModel):
    Bucket: str
    ManifestFormat: Literal["S3InventoryReport_CSV_20211130"]
    ExpectedManifestBucketOwner: Optional[str] = None
    ManifestPrefix: Optional[str] = None
    ManifestEncryption: Optional[GeneratedManifestEncryptionTypeDef] = None

class S3SetObjectRetentionOperationTypeDef(BaseModel):
    Retention: S3RetentionTypeDef
    BypassGovernanceRetention: Optional[bool] = None

class JobListDescriptorTypeDef(BaseModel):
    JobId: Optional[str] = None
    Description: Optional[str] = None
    Operation: Optional[OperationNameType] = None
    Priority: Optional[int] = None
    Status: Optional[JobStatusType] = None
    CreationTime: Optional[datetime] = None
    TerminationDate: Optional[datetime] = None
    ProgressSummary: Optional[JobProgressSummaryTypeDef] = None

class StorageLensGroupFilterTypeDef(BaseModel):
    MatchAnyPrefix: Optional[Sequence[str]] = None
    MatchAnySuffix: Optional[Sequence[str]] = None
    MatchAnyTag: Optional[Sequence[S3TagTypeDef]] = None
    MatchObjectAge: Optional[MatchObjectAgeTypeDef] = None
    MatchObjectSize: Optional[MatchObjectSizeTypeDef] = None
    And: Optional[StorageLensGroupAndOperatorTypeDef] = None
    Or: Optional[StorageLensGroupOrOperatorTypeDef] = None

class DestinationTypeDef(BaseModel):
    Bucket: str
    Account: Optional[str] = None
    ReplicationTime: Optional[ReplicationTimeTypeDef] = None
    AccessControlTranslation: Optional[AccessControlTranslationTypeDef] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    Metrics: Optional[MetricsTypeDef] = None
    StorageClass: Optional[ReplicationStorageClassType] = None

class GetMultiRegionAccessPointPolicyResultTypeDef(BaseModel):
    Policy: MultiRegionAccessPointPolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AsyncResponseDetailsTypeDef(BaseModel):
    MultiRegionAccessPointDetails: Optional[MultiRegionAccessPointsAsyncResponseTypeDef] = None
    ErrorDetails: Optional[AsyncErrorDetailsTypeDef] = None

class GetMultiRegionAccessPointResultTypeDef(BaseModel):
    AccessPoint: MultiRegionAccessPointReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMultiRegionAccessPointsResultTypeDef(BaseModel):
    AccessPoints: List[MultiRegionAccessPointReportTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PrefixLevelTypeDef(BaseModel):
    StorageMetrics: PrefixLevelStorageMetricsTypeDef

class S3AccessControlListTypeDef(BaseModel):
    Owner: S3ObjectOwnerTypeDef
    Grants: Optional[Sequence[S3GrantTypeDef]] = None

class S3CopyObjectOperationTypeDef(BaseModel):
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

class S3BucketDestinationTypeDef(BaseModel):
    Format: FormatType
    OutputSchemaVersion: Literal["V_1"]
    AccountId: str
    Arn: str
    Prefix: Optional[str] = None
    Encryption: Optional[StorageLensDataExportEncryptionTypeDef] = None

class ObjectLambdaConfigurationTypeDef(BaseModel):
    SupportingAccessPoint: str
    TransformationConfigurations: Sequence[ObjectLambdaTransformationConfigurationTypeDef]
    CloudWatchMetricsEnabled: Optional[bool] = None
    AllowedFeatures: Optional[Sequence[ObjectLambdaAllowedFeatureType]] = None

class LifecycleRuleTypeDef(BaseModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationTypeDef] = None
    ID: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterTypeDef] = None
    Transitions: Optional[List[TransitionTypeDef]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class S3JobManifestGeneratorTypeDef(BaseModel):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: Optional[str] = None
    ManifestOutputLocation: Optional[S3ManifestOutputLocationTypeDef] = None
    Filter: Optional[JobManifestGeneratorFilterTypeDef] = None

class ListJobsResultTypeDef(BaseModel):
    NextToken: str
    Jobs: List[JobListDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StorageLensGroupTypeDef(BaseModel):
    Name: str
    Filter: StorageLensGroupFilterTypeDef
    StorageLensGroupArn: Optional[str] = None

class ReplicationRuleTypeDef(BaseModel):
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

class AsyncOperationTypeDef(BaseModel):
    CreationTime: Optional[datetime] = None
    Operation: Optional[AsyncOperationNameType] = None
    RequestTokenARN: Optional[str] = None
    RequestParameters: Optional[AsyncRequestParametersTypeDef] = None
    RequestStatus: Optional[str] = None
    ResponseDetails: Optional[AsyncResponseDetailsTypeDef] = None

class BucketLevelTypeDef(BaseModel):
    ActivityMetrics: Optional[ActivityMetricsTypeDef] = None
    PrefixLevel: Optional[PrefixLevelTypeDef] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetricsTypeDef] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetricsTypeDef] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetricsTypeDef] = None

class S3AccessControlPolicyTypeDef(BaseModel):
    AccessControlList: Optional[S3AccessControlListTypeDef] = None
    CannedAccessControlList: Optional[S3CannedAccessControlListType] = None

class StorageLensDataExportTypeDef(BaseModel):
    S3BucketDestination: Optional[S3BucketDestinationTypeDef] = None
    CloudWatchMetrics: Optional[CloudWatchMetricsTypeDef] = None

class CreateAccessPointForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationTypeDef

class GetAccessPointConfigurationForObjectLambdaResultTypeDef(BaseModel):
    Configuration: ObjectLambdaConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationTypeDef

class GetBucketLifecycleConfigurationResultTypeDef(BaseModel):
    Rules: List[LifecycleRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleConfigurationTypeDef(BaseModel):
    Rules: Optional[Sequence[LifecycleRuleTypeDef]] = None

class JobManifestGeneratorTypeDef(BaseModel):
    S3JobManifestGenerator: Optional[S3JobManifestGeneratorTypeDef] = None

class CreateStorageLensGroupRequestRequestTypeDef(BaseModel):
    AccountId: str
    StorageLensGroup: StorageLensGroupTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetStorageLensGroupResultTypeDef(BaseModel):
    StorageLensGroup: StorageLensGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStorageLensGroupRequestRequestTypeDef(BaseModel):
    Name: str
    AccountId: str
    StorageLensGroup: StorageLensGroupTypeDef

class ReplicationConfigurationTypeDef(BaseModel):
    Role: str
    Rules: List[ReplicationRuleTypeDef]

class DescribeMultiRegionAccessPointOperationResultTypeDef(BaseModel):
    AsyncOperation: AsyncOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountLevelTypeDef(BaseModel):
    BucketLevel: BucketLevelTypeDef
    ActivityMetrics: Optional[ActivityMetricsTypeDef] = None
    AdvancedCostOptimizationMetrics: Optional[AdvancedCostOptimizationMetricsTypeDef] = None
    AdvancedDataProtectionMetrics: Optional[AdvancedDataProtectionMetricsTypeDef] = None
    DetailedStatusCodesMetrics: Optional[DetailedStatusCodesMetricsTypeDef] = None
    StorageLensGroupLevel: Optional[StorageLensGroupLevelTypeDef] = None

class S3SetObjectAclOperationTypeDef(BaseModel):
    AccessControlPolicy: Optional[S3AccessControlPolicyTypeDef] = None

class PutBucketLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None

class GetBucketReplicationResultTypeDef(BaseModel):
    ReplicationConfiguration: ReplicationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketReplicationRequestRequestTypeDef(BaseModel):
    AccountId: str
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationTypeDef

class StorageLensConfigurationTypeDef(BaseModel):
    Id: str
    AccountLevel: AccountLevelTypeDef
    IsEnabled: bool
    Include: Optional[IncludeTypeDef] = None
    Exclude: Optional[ExcludeTypeDef] = None
    DataExport: Optional[StorageLensDataExportTypeDef] = None
    AwsOrg: Optional[StorageLensAwsOrgTypeDef] = None
    StorageLensArn: Optional[str] = None

class JobOperationTypeDef(BaseModel):
    LambdaInvoke: Optional[LambdaInvokeOperationTypeDef] = None
    S3PutObjectCopy: Optional[S3CopyObjectOperationTypeDef] = None
    S3PutObjectAcl: Optional[S3SetObjectAclOperationTypeDef] = None
    S3PutObjectTagging: Optional[S3SetObjectTaggingOperationTypeDef] = None
    S3DeleteObjectTagging: Optional[Mapping[str, Any]] = None
    S3InitiateRestoreObject: Optional[S3InitiateRestoreObjectOperationTypeDef] = None
    S3PutObjectLegalHold: Optional[S3SetObjectLegalHoldOperationTypeDef] = None
    S3PutObjectRetention: Optional[S3SetObjectRetentionOperationTypeDef] = None
    S3ReplicateObject: Optional[Mapping[str, Any]] = None

class GetStorageLensConfigurationResultTypeDef(BaseModel):
    StorageLensConfiguration: StorageLensConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutStorageLensConfigurationRequestRequestTypeDef(BaseModel):
    ConfigId: str
    AccountId: str
    StorageLensConfiguration: StorageLensConfigurationTypeDef
    Tags: Optional[Sequence[StorageLensTagTypeDef]] = None

class CreateJobRequestRequestTypeDef(BaseModel):
    AccountId: str
    Operation: JobOperationTypeDef
    Report: JobReportTypeDef
    ClientRequestToken: str
    Priority: int
    RoleArn: str
    ConfirmationRequired: Optional[bool] = None
    Manifest: Optional[JobManifestTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[S3TagTypeDef]] = None
    ManifestGenerator: Optional[JobManifestGeneratorTypeDef] = None

class JobDescriptorTypeDef(BaseModel):
    JobId: Optional[str] = None
    ConfirmationRequired: Optional[bool] = None
    Description: Optional[str] = None
    JobArn: Optional[str] = None
    Status: Optional[JobStatusType] = None
    Manifest: Optional[JobManifestTypeDef] = None
    Operation: Optional[JobOperationTypeDef] = None
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
    ManifestGenerator: Optional[JobManifestGeneratorTypeDef] = None
    GeneratedManifestDescriptor: Optional[S3GeneratedManifestDescriptorTypeDef] = None

class DescribeJobResultTypeDef(BaseModel):
    Job: JobDescriptorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

