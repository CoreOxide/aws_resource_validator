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
from aws_resource_validator.pydantic_models.s3_constants import *

class AbortIncompleteMultipartUploadTypeDef(BaseValidatorModel):
    DaysAfterInitiation: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AccelerateConfigurationTypeDef(BaseValidatorModel):
    Status: Optional[BucketAccelerateStatusType] = None


class OwnerTypeDef(BaseValidatorModel):
    DisplayName: Optional[str] = None
    ID: Optional[str] = None


class AccessControlTranslationTypeDef(BaseValidatorModel):
    Owner: Literal["Destination"]


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class AnalyticsS3BucketDestinationTypeDef(BaseValidatorModel):
    Format: Literal["CSV"]
    Bucket: str
    BucketAccountId: Optional[str] = None
    Prefix: Optional[str] = None


class CopySourceTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None


class BucketDownloadFileRequestTypeDef(BaseValidatorModel):
    Key: str
    Filename: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class BucketTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None
    BucketRegion: Optional[str] = None


class BucketUploadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class CORSRuleOutputTypeDef(BaseValidatorModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAgeSeconds: Optional[int] = None


class CORSRuleTypeDef(BaseValidatorModel):
    AllowedMethods: Sequence[str]
    AllowedOrigins: Sequence[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAgeSeconds: Optional[int] = None


class CSVInputTypeDef(BaseValidatorModel):
    FileHeaderInfo: Optional[FileHeaderInfoType] = None
    Comments: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None
    AllowQuotedRecordDelimiter: Optional[bool] = None


class CSVOutputTypeDef(BaseValidatorModel):
    QuoteFields: Optional[QuoteFieldsType] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None


class ChecksumTypeDef(BaseValidatorModel):
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class ClientDownloadFileRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Filename: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class ClientGeneratePresignedPostRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Fields: Optional[Dict[str, Any] | None] = None
    Conditions: Optional[List[Any] | Dict[str, Any] | None] = None
    ExpiresIn: Optional[int] = None


class ClientUploadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    Bucket: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class CloudFunctionConfigurationOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    CloudFunction: Optional[str] = None
    InvocationRole: Optional[str] = None


class CloudFunctionConfigurationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[Sequence[EventType]] = None
    CloudFunction: Optional[str] = None
    InvocationRole: Optional[str] = None


class CommonPrefixTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None


class CompletedPartTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    PartNumber: Optional[int] = None


class ConditionTypeDef(BaseValidatorModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None


class CopyObjectResultTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


class CopyPartResultTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


class SessionCredentialsTypeDef(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime


class CreateSessionRequestTypeDef(BaseValidatorModel):
    Bucket: str
    SessionMode: Optional[SessionModeType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None


class DefaultRetentionTypeDef(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    Days: Optional[int] = None
    Years: Optional[int] = None


class DeleteBucketAnalyticsConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketCorsRequestBucketCorsDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketCorsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketEncryptionRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketIntelligentTieringConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str


class DeleteBucketInventoryConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketLifecycleRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketMetadataTableConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketMetricsConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketOwnershipControlsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketPolicyRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketReplicationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketRequestBucketDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketTaggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketWebsiteRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteMarkerReplicationTypeDef(BaseValidatorModel):
    Status: Optional[DeleteMarkerReplicationStatusType] = None


class DeleteObjectTaggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class DeletedObjectTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    DeleteMarker: Optional[bool] = None
    DeleteMarkerVersionId: Optional[str] = None


class ErrorTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Code: Optional[str] = None
    Message: Optional[str] = None


class DeletePublicAccessBlockRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    ReplicaKmsKeyID: Optional[str] = None


class EncryptionTypeDef(BaseValidatorModel):
    EncryptionType: ServerSideEncryptionType
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None


class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ErrorDocumentTypeDef(BaseValidatorModel):
    Key: str


class ExistingObjectReplicationTypeDef(BaseValidatorModel):
    Status: ExistingObjectReplicationStatusType


class FilterRuleTypeDef(BaseValidatorModel):
    Name: Optional[FilterRuleNameType] = None
    Value: Optional[str] = None


class GetBucketAccelerateConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None


class GetBucketAclRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketAnalyticsConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketCorsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketEncryptionRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketIntelligentTieringConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str


class GetBucketInventoryConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketLifecycleConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketLifecycleRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketLocationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketLoggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketMetadataTableConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketMetricsConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketNotificationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketOwnershipControlsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketPolicyRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class PolicyStatusTypeDef(BaseValidatorModel):
    IsPublic: Optional[bool] = None


class GetBucketPolicyStatusRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketReplicationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketRequestPaymentRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketTaggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetBucketVersioningRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class IndexDocumentTypeDef(BaseValidatorModel):
    Suffix: str


class GetBucketWebsiteRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GetObjectAclRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class ObjectPartTypeDef(BaseValidatorModel):
    PartNumber: Optional[int] = None
    Size: Optional[int] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


class GetObjectAttributesRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    ObjectAttributes: Sequence[ObjectAttributesType]
    VersionId: Optional[str] = None
    MaxParts: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class ObjectLockLegalHoldTypeDef(BaseValidatorModel):
    Status: Optional[ObjectLockLegalHoldStatusType] = None


class GetObjectLegalHoldRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class GetObjectLockConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class ObjectLockRetentionOutputTypeDef(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[datetime] = None


class GetObjectRetentionRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class GetObjectTaggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None


class GetObjectTorrentRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class PublicAccessBlockConfigurationTypeDef(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None


class GetPublicAccessBlockRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GlacierJobParametersTypeDef(BaseValidatorModel):
    Tier: TierType


class HeadBucketRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class InitiatorTypeDef(BaseValidatorModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None


class TieringTypeDef(BaseValidatorModel):
    Days: int
    AccessTier: IntelligentTieringAccessTierType


class InventoryFilterTypeDef(BaseValidatorModel):
    Prefix: str


class InventoryScheduleTypeDef(BaseValidatorModel):
    Frequency: InventoryFrequencyType


class SSEKMSTypeDef(BaseValidatorModel):
    KeyId: str


class JSONOutputTypeDef(BaseValidatorModel):
    RecordDelimiter: Optional[str] = None


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
    NewerNoncurrentVersions: Optional[int] = None


class TransitionOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class ListBucketAnalyticsConfigurationsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class ListBucketIntelligentTieringConfigurationsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None


class ListBucketInventoryConfigurationsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class ListBucketMetricsConfigurationsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBucketsRequestTypeDef(BaseValidatorModel):
    MaxBuckets: Optional[int] = None
    ContinuationToken: Optional[str] = None
    Prefix: Optional[str] = None
    BucketRegion: Optional[str] = None


class ListDirectoryBucketsRequestTypeDef(BaseValidatorModel):
    ContinuationToken: Optional[str] = None
    MaxDirectoryBuckets: Optional[int] = None


class ListMultipartUploadsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    KeyMarker: Optional[str] = None
    MaxUploads: Optional[int] = None
    Prefix: Optional[str] = None
    UploadIdMarker: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None


class ListObjectVersionsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    KeyMarker: Optional[str] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    VersionIdMarker: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None


class ListObjectsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Marker: Optional[str] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None


class ListObjectsV2RequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    ContinuationToken: Optional[str] = None
    FetchOwner: Optional[bool] = None
    StartAfter: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None


class PartTypeDef(BaseValidatorModel):
    PartNumber: Optional[int] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


class ListPartsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    MaxParts: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None


class MetadataEntryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class S3TablesDestinationResultTypeDef(BaseValidatorModel):
    TableBucketArn: str
    TableName: str
    TableArn: str
    TableNamespace: str


class S3TablesDestinationTypeDef(BaseValidatorModel):
    TableBucketArn: str
    TableName: str


class ReplicationTimeValueTypeDef(BaseValidatorModel):
    Minutes: Optional[int] = None


class QueueConfigurationDeprecatedOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    Queue: Optional[str] = None


class TopicConfigurationDeprecatedOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Events: Optional[List[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None


class ObjectDownloadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class RestoreStatusTypeDef(BaseValidatorModel):
    IsRestoreInProgress: Optional[bool] = None
    RestoreExpiryDate: Optional[datetime] = None


class ObjectUploadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class OwnershipControlsRuleTypeDef(BaseValidatorModel):
    ObjectOwnership: ObjectOwnershipType


class PartitionedPrefixTypeDef(BaseValidatorModel):
    PartitionDateSource: Optional[PartitionDateSourceType] = None


class ProgressTypeDef(BaseValidatorModel):
    BytesScanned: Optional[int] = None
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None


class PutBucketPolicyRequestBucketPolicyPutTypeDef(BaseValidatorModel):
    Policy: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketPolicyRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Policy: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None


class RequestPaymentConfigurationTypeDef(BaseValidatorModel):
    Payer: PayerType


class PutBucketVersioningRequestBucketVersioningEnableTypeDef(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class VersioningConfigurationTypeDef(BaseValidatorModel):
    MFADelete: Optional[MFADeleteType] = None
    Status: Optional[BucketVersioningStatusType] = None


class PutBucketVersioningRequestBucketVersioningSuspendTypeDef(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class QueueConfigurationDeprecatedTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[Sequence[EventType]] = None
    Queue: Optional[str] = None


class RecordsEventTypeDef(BaseValidatorModel):
    Payload: Optional[bytes] = None


class ReplicaModificationsTypeDef(BaseValidatorModel):
    Status: ReplicaModificationsStatusType


class RequestProgressTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ScanRangeTypeDef(BaseValidatorModel):
    Start: Optional[int] = None
    End: Optional[int] = None


class ServerSideEncryptionByDefaultTypeDef(BaseValidatorModel):
    SSEAlgorithm: ServerSideEncryptionType
    KMSMasterKeyID: Optional[str] = None


class SseKmsEncryptedObjectsTypeDef(BaseValidatorModel):
    Status: SseKmsEncryptedObjectsStatusType


class StatsTypeDef(BaseValidatorModel):
    BytesScanned: Optional[int] = None
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None


class TopicConfigurationDeprecatedTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Events: Optional[Sequence[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None


class AbortMultipartUploadOutputTypeDef(BaseValidatorModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class CompleteMultipartUploadOutputTypeDef(BaseValidatorModel):
    Location: str
    Bucket: str
    Key: str
    Expiration: str
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumCRC64NVME: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ChecksumType: ChecksumTypeType
    ServerSideEncryption: ServerSideEncryptionType
    VersionId: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBucketOutputTypeDef(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultipartUploadOutputTypeDef(BaseValidatorModel):
    AbortDate: datetime
    AbortRuleId: str
    Bucket: str
    Key: str
    UploadId: str
    ServerSideEncryption: ServerSideEncryptionType
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ChecksumAlgorithm: ChecksumAlgorithmType
    ChecksumType: ChecksumTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteObjectOutputTypeDef(BaseValidatorModel):
    DeleteMarker: bool
    VersionId: str
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteObjectTaggingOutputTypeDef(BaseValidatorModel):
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketAccelerateConfigurationOutputTypeDef(BaseValidatorModel):
    Status: BucketAccelerateStatusType
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketLocationOutputTypeDef(BaseValidatorModel):
    LocationConstraint: BucketLocationConstraintType
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketPolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketRequestPaymentOutputTypeDef(BaseValidatorModel):
    Payer: PayerType
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketVersioningOutputTypeDef(BaseValidatorModel):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectOutputTypeDef(BaseValidatorModel):
    Body: StreamingBody
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    LastModified: datetime
    ContentLength: int
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumCRC64NVME: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ChecksumType: ChecksumTypeType
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    ContentRange: str
    ContentType: str
    Expires: datetime
    WebsiteRedirectLocation: str
    ServerSideEncryption: ServerSideEncryptionType
    Metadata: Dict[str, str]
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    StorageClass: StorageClassType
    RequestCharged: Literal["requester"]
    ReplicationStatus: ReplicationStatusType
    PartsCount: int
    TagCount: int
    ObjectLockMode: ObjectLockModeType
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectTorrentOutputTypeDef(BaseValidatorModel):
    Body: StreamingBody
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class HeadBucketOutputTypeDef(BaseValidatorModel):
    BucketLocationType: LocationTypeType
    BucketLocationName: str
    BucketRegion: str
    AccessPointAlias: bool
    ResponseMetadata: ResponseMetadataTypeDef


class HeadObjectOutputTypeDef(BaseValidatorModel):
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    ArchiveStatus: ArchiveStatusType
    LastModified: datetime
    ContentLength: int
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumCRC64NVME: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ChecksumType: ChecksumTypeType
    ETag: str
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    ContentType: str
    ContentRange: str
    Expires: datetime
    WebsiteRedirectLocation: str
    ServerSideEncryption: ServerSideEncryptionType
    Metadata: Dict[str, str]
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    StorageClass: StorageClassType
    RequestCharged: Literal["requester"]
    ReplicationStatus: ReplicationStatusType
    PartsCount: int
    ObjectLockMode: ObjectLockModeType
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class PutBucketLifecycleConfigurationOutputTypeDef(BaseValidatorModel):
    TransitionDefaultMinimumObjectSize: TransitionDefaultMinimumObjectSizeType
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectAclOutputTypeDef(BaseValidatorModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectLegalHoldOutputTypeDef(BaseValidatorModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectLockConfigurationOutputTypeDef(BaseValidatorModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectOutputTypeDef(BaseValidatorModel):
    Expiration: str
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumCRC64NVME: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ChecksumType: ChecksumTypeType
    ServerSideEncryption: ServerSideEncryptionType
    VersionId: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    Size: int
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectRetentionOutputTypeDef(BaseValidatorModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectTaggingOutputTypeDef(BaseValidatorModel):
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreObjectOutputTypeDef(BaseValidatorModel):
    RequestCharged: Literal["requester"]
    RestoreOutputPath: str
    ResponseMetadata: ResponseMetadataTypeDef


class UploadPartOutputTypeDef(BaseValidatorModel):
    ServerSideEncryption: ServerSideEncryptionType
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumCRC64NVME: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class AbortMultipartUploadRequestMultipartUploadAbortTypeDef(BaseValidatorModel):
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatchInitiatedTime: Optional[TimestampTypeDef] = None


class AbortMultipartUploadRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatchInitiatedTime: Optional[TimestampTypeDef] = None


class CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class CreateMultipartUploadRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class DeleteObjectRequestObjectDeleteTypeDef(BaseValidatorModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[TimestampTypeDef] = None
    IfMatchSize: Optional[int] = None


class DeleteObjectRequestObjectSummaryDeleteTypeDef(BaseValidatorModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[TimestampTypeDef] = None
    IfMatchSize: Optional[int] = None


class DeleteObjectRequestObjectVersionDeleteTypeDef(BaseValidatorModel):
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[TimestampTypeDef] = None
    IfMatchSize: Optional[int] = None


class DeleteObjectRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[TimestampTypeDef] = None
    IfMatchSize: Optional[int] = None


class GetObjectRequestObjectGetTypeDef(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None


class GetObjectRequestObjectSummaryGetTypeDef(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None


class GetObjectRequestObjectVersionGetTypeDef(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None


class GetObjectRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None


class HeadObjectRequestObjectVersionHeadTypeDef(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None


class HeadObjectRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None


class LifecycleExpirationTypeDef(BaseValidatorModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None


class ObjectIdentifierTypeDef(BaseValidatorModel):
    Key: str
    VersionId: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[TimestampTypeDef] = None
    Size: Optional[int] = None


class ObjectLockRetentionTypeDef(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[TimestampTypeDef] = None


class TransitionTypeDef(BaseValidatorModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


class PutBucketAccelerateConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    AccelerateConfiguration: AccelerateConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None


class DeleteMarkerEntryTypeDef(BaseValidatorModel):
    Owner: Optional[OwnerTypeDef] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    IsLatest: Optional[bool] = None
    LastModified: Optional[datetime] = None


class AnalyticsAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class AnalyticsAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class GetBucketTaggingOutputTypeDef(BaseValidatorModel):
    TagSet: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectTaggingOutputTypeDef(BaseValidatorModel):
    VersionId: str
    TagSet: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IntelligentTieringAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class IntelligentTieringAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class LifecycleRuleAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class LifecycleRuleAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class MetricsAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    AccessPointArn: Optional[str] = None


class MetricsAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AccessPointArn: Optional[str] = None


class ReplicationRuleAndOperatorOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class ReplicationRuleAndOperatorTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TaggingTypeDef(BaseValidatorModel):
    TagSet: Sequence[TagTypeDef]


class AnalyticsExportDestinationTypeDef(BaseValidatorModel):
    S3BucketDestination: AnalyticsS3BucketDestinationTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class PutObjectRequestBucketPutObjectTypeDef(BaseValidatorModel):
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[BlobTypeDef] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectRequestObjectPutTypeDef(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[BlobTypeDef] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectRequestObjectSummaryPutTypeDef(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[BlobTypeDef] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[BlobTypeDef] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ContentType: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Mapping[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class UploadPartRequestMultipartUploadPartUploadTypeDef(BaseValidatorModel):
    Body: Optional[BlobTypeDef] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class UploadPartRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    PartNumber: int
    UploadId: str
    Body: Optional[BlobTypeDef] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None


class WriteGetObjectResponseRequestTypeDef(BaseValidatorModel):
    RequestRoute: str
    RequestToken: str
    Body: Optional[BlobTypeDef] = None
    StatusCode: Optional[int] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    AcceptRanges: Optional[str] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentLength: Optional[int] = None
    ContentRange: Optional[str] = None
    ContentType: Optional[str] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    DeleteMarker: Optional[bool] = None
    ETag: Optional[str] = None
    Expires: Optional[TimestampTypeDef] = None
    Expiration: Optional[str] = None
    LastModified: Optional[TimestampTypeDef] = None
    MissingMeta: Optional[int] = None
    Metadata: Optional[Mapping[str, str]] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    PartsCount: Optional[int] = None
    ReplicationStatus: Optional[ReplicationStatusType] = None
    RequestCharged: Optional[Literal["requester"]] = None
    Restore: Optional[str] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    TagCount: Optional[int] = None
    VersionId: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None


class BucketCopyRequestTypeDef(BaseValidatorModel):
    CopySource: CopySourceTypeDef
    Key: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    SourceClient: Optional[BaseClient | None] = None
    Config: Optional[TransferConfig | None] = None


class ClientCopyRequestTypeDef(BaseValidatorModel):
    CopySource: CopySourceTypeDef
    Bucket: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    SourceClient: Optional[BaseClient | None] = None
    Config: Optional[TransferConfig | None] = None


class ObjectCopyRequestTypeDef(BaseValidatorModel):
    CopySource: CopySourceTypeDef
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    SourceClient: Optional[BaseClient | None] = None
    Config: Optional[TransferConfig | None] = None


class FileobjTypeDef(BaseValidatorModel):
    pass


class BucketDownloadFileobjRequestTypeDef(BaseValidatorModel):
    Key: str
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class BucketUploadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    Key: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class ClientDownloadFileobjRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class ClientUploadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    Bucket: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class ObjectDownloadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class ObjectUploadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Dict[str, Any] | None] = None
    Callback: Optional[Callable[..., Any] | None] = None
    Config: Optional[TransferConfig | None] = None


class ListBucketsOutputTypeDef(BaseValidatorModel):
    Buckets: List[BucketTypeDef]
    Owner: OwnerTypeDef
    ContinuationToken: str
    Prefix: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListDirectoryBucketsOutputTypeDef(BaseValidatorModel):
    Buckets: List[BucketTypeDef]
    ContinuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketCorsOutputTypeDef(BaseValidatorModel):
    CORSRules: List[CORSRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CompletedMultipartUploadTypeDef(BaseValidatorModel):
    Parts: Optional[Sequence[CompletedPartTypeDef]] = None


class CopyObjectOutputTypeDef(BaseValidatorModel):
    CopyObjectResult: CopyObjectResultTypeDef
    Expiration: str
    CopySourceVersionId: str
    VersionId: str
    ServerSideEncryption: ServerSideEncryptionType
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class UploadPartCopyOutputTypeDef(BaseValidatorModel):
    CopySourceVersionId: str
    CopyPartResult: CopyPartResultTypeDef
    ServerSideEncryption: ServerSideEncryptionType
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class LocationInfoTypeDef(BaseValidatorModel):
    pass


class BucketInfoTypeDef(BaseValidatorModel):
    pass


class CreateBucketConfigurationTypeDef(BaseValidatorModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None
    Location: Optional[LocationInfoTypeDef] = None
    Bucket: Optional[BucketInfoTypeDef] = None


class CreateSessionOutputTypeDef(BaseValidatorModel):
    ServerSideEncryption: ServerSideEncryptionType
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    Credentials: SessionCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ObjectLockRuleTypeDef(BaseValidatorModel):
    DefaultRetention: Optional[DefaultRetentionTypeDef] = None


class DeleteObjectsOutputTypeDef(BaseValidatorModel):
    Deleted: List[DeletedObjectTypeDef]
    RequestCharged: Literal["requester"]
    Errors: List[ErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class S3KeyFilterOutputTypeDef(BaseValidatorModel):
    FilterRules: Optional[List[FilterRuleTypeDef]] = None


class S3KeyFilterTypeDef(BaseValidatorModel):
    FilterRules: Optional[Sequence[FilterRuleTypeDef]] = None


class GetBucketPolicyStatusOutputTypeDef(BaseValidatorModel):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectAttributesPartsTypeDef(BaseValidatorModel):
    TotalPartsCount: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    NextPartNumberMarker: Optional[int] = None
    MaxParts: Optional[int] = None
    IsTruncated: Optional[bool] = None
    Parts: Optional[List[ObjectPartTypeDef]] = None


class GetObjectLegalHoldOutputTypeDef(BaseValidatorModel):
    LegalHold: ObjectLockLegalHoldTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectLegalHoldRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    LegalHold: Optional[ObjectLockLegalHoldTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class GetObjectRetentionOutputTypeDef(BaseValidatorModel):
    Retention: ObjectLockRetentionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPublicAccessBlockOutputTypeDef(BaseValidatorModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutPublicAccessBlockRequestTypeDef(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class GranteeTypeDef(BaseValidatorModel):
    pass


class GrantTypeDef(BaseValidatorModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None


class TargetGrantTypeDef(BaseValidatorModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[BucketLogsPermissionType] = None


class HeadBucketRequestWaitExtraTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class HeadBucketRequestWaitTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class HeadObjectRequestWaitExtraTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class HeadObjectRequestWaitTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[TimestampTypeDef] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[TimestampTypeDef] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class MultipartUploadTypeDef(BaseValidatorModel):
    UploadId: Optional[str] = None
    Key: Optional[str] = None
    Initiated: Optional[datetime] = None
    StorageClass: Optional[StorageClassType] = None
    Owner: Optional[OwnerTypeDef] = None
    Initiator: Optional[InitiatorTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class JSONInputTypeDef(BaseValidatorModel):
    pass


class InputSerializationTypeDef(BaseValidatorModel):
    CSV: Optional[CSVInputTypeDef] = None
    CompressionType: Optional[CompressionTypeType] = None
    JSON: Optional[JSONInputTypeDef] = None
    Parquet: Optional[Mapping[str, Any]] = None


class InventoryEncryptionOutputTypeDef(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None


class InventoryEncryptionTypeDef(BaseValidatorModel):
    SSES3: Optional[Mapping[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None


class OutputSerializationTypeDef(BaseValidatorModel):
    CSV: Optional[CSVOutputTypeDef] = None
    JSON: Optional[JSONOutputTypeDef] = None


class RuleOutputTypeDef(BaseValidatorModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutputTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionOutputTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None


class ListBucketsRequestPaginateTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    BucketRegion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDirectoryBucketsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMultipartUploadsRequestPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectVersionsRequestPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectsRequestPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectsV2RequestPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    FetchOwner: Optional[bool] = None
    StartAfter: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPartsRequestPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPartsOutputTypeDef(BaseValidatorModel):
    AbortDate: datetime
    AbortRuleId: str
    Bucket: str
    Key: str
    UploadId: str
    PartNumberMarker: int
    NextPartNumberMarker: int
    MaxParts: int
    IsTruncated: bool
    Parts: List[PartTypeDef]
    Initiator: InitiatorTypeDef
    Owner: OwnerTypeDef
    StorageClass: StorageClassType
    RequestCharged: Literal["requester"]
    ChecksumAlgorithm: ChecksumAlgorithmType
    ChecksumType: ChecksumTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class MetadataTableConfigurationResultTypeDef(BaseValidatorModel):
    S3TablesDestinationResult: S3TablesDestinationResultTypeDef


class MetadataTableConfigurationTypeDef(BaseValidatorModel):
    S3TablesDestination: S3TablesDestinationTypeDef


class MetricsTypeDef(BaseValidatorModel):
    Status: MetricsStatusType
    EventThreshold: Optional[ReplicationTimeValueTypeDef] = None


class ReplicationTimeTypeDef(BaseValidatorModel):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValueTypeDef


class NotificationConfigurationDeprecatedResponseTypeDef(BaseValidatorModel):
    TopicConfiguration: TopicConfigurationDeprecatedOutputTypeDef
    QueueConfiguration: QueueConfigurationDeprecatedOutputTypeDef
    CloudFunctionConfiguration: CloudFunctionConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ObjectTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    Size: Optional[int] = None
    StorageClass: Optional[ObjectStorageClassType] = None
    Owner: Optional[OwnerTypeDef] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None


class ObjectVersionTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    Size: Optional[int] = None
    StorageClass: Optional[Literal["STANDARD"]] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    IsLatest: Optional[bool] = None
    LastModified: Optional[datetime] = None
    Owner: Optional[OwnerTypeDef] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None


class OwnershipControlsOutputTypeDef(BaseValidatorModel):
    Rules: List[OwnershipControlsRuleTypeDef]


class OwnershipControlsTypeDef(BaseValidatorModel):
    Rules: Sequence[OwnershipControlsRuleTypeDef]


class TargetObjectKeyFormatOutputTypeDef(BaseValidatorModel):
    SimplePrefix: Optional[Dict[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefixTypeDef] = None


class TargetObjectKeyFormatTypeDef(BaseValidatorModel):
    SimplePrefix: Optional[Mapping[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefixTypeDef] = None


class ProgressEventTypeDef(BaseValidatorModel):
    Details: Optional[ProgressTypeDef] = None


class PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef(BaseValidatorModel):
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketRequestPaymentRequestTypeDef(BaseValidatorModel):
    Bucket: str
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketVersioningRequestBucketVersioningPutTypeDef(BaseValidatorModel):
    VersioningConfiguration: VersioningConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketVersioningRequestTypeDef(BaseValidatorModel):
    Bucket: str
    VersioningConfiguration: VersioningConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class RedirectTypeDef(BaseValidatorModel):
    pass


class RoutingRuleTypeDef(BaseValidatorModel):
    Redirect: RedirectTypeDef
    Condition: Optional[ConditionTypeDef] = None


class ServerSideEncryptionRuleTypeDef(BaseValidatorModel):
    ApplyServerSideEncryptionByDefault: Optional[ServerSideEncryptionByDefaultTypeDef] = None
    BucketKeyEnabled: Optional[bool] = None


class SourceSelectionCriteriaTypeDef(BaseValidatorModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjectsTypeDef] = None
    ReplicaModifications: Optional[ReplicaModificationsTypeDef] = None


class StatsEventTypeDef(BaseValidatorModel):
    Details: Optional[StatsTypeDef] = None


class DeleteTypeDef(BaseValidatorModel):
    Objects: Sequence[ObjectIdentifierTypeDef]
    Quiet: Optional[bool] = None


class AnalyticsFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[AnalyticsAndOperatorOutputTypeDef] = None


class AnalyticsFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[AnalyticsAndOperatorTypeDef] = None


class IntelligentTieringFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[IntelligentTieringAndOperatorOutputTypeDef] = None


class IntelligentTieringFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[IntelligentTieringAndOperatorTypeDef] = None


class LifecycleRuleFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorOutputTypeDef] = None


class MetricsFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperatorOutputTypeDef] = None


class MetricsFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperatorTypeDef] = None


class ReplicationRuleFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorOutputTypeDef] = None


class ReplicationRuleFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorTypeDef] = None


class PutBucketTaggingRequestBucketTaggingPutTypeDef(BaseValidatorModel):
    Tagging: TaggingTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketTaggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Tagging: TaggingTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectTaggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Tagging: TaggingTypeDef
    VersionId: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None


class StorageClassAnalysisDataExportTypeDef(BaseValidatorModel):
    OutputSchemaVersion: Literal["V_1"]
    Destination: AnalyticsExportDestinationTypeDef


class CopySourceOrStrTypeDef(BaseValidatorModel):
    pass


class CopyObjectRequestObjectCopyFromTypeDef(BaseValidatorModel):
    CopySource: CopySourceOrStrTypeDef
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[TimestampTypeDef] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Expires: Optional[TimestampTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Mapping[str, str]] = None
    MetadataDirective: Optional[MetadataDirectiveType] = None
    TaggingDirective: Optional[TaggingDirectiveType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class CopyObjectRequestObjectSummaryCopyFromTypeDef(BaseValidatorModel):
    CopySource: CopySourceOrStrTypeDef
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[TimestampTypeDef] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Expires: Optional[TimestampTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Mapping[str, str]] = None
    MetadataDirective: Optional[MetadataDirectiveType] = None
    TaggingDirective: Optional[TaggingDirectiveType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class CopyObjectRequestTypeDef(BaseValidatorModel):
    Bucket: str
    CopySource: CopySourceOrStrTypeDef
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[TimestampTypeDef] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[TimestampTypeDef] = None
    Expires: Optional[TimestampTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Mapping[str, str]] = None
    MetadataDirective: Optional[MetadataDirectiveType] = None
    TaggingDirective: Optional[TaggingDirectiveType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef(BaseValidatorModel):
    CopySource: CopySourceOrStrTypeDef
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[TimestampTypeDef] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[TimestampTypeDef] = None
    CopySourceRange: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class UploadPartCopyRequestTypeDef(BaseValidatorModel):
    Bucket: str
    CopySource: CopySourceOrStrTypeDef
    Key: str
    PartNumber: int
    UploadId: str
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[TimestampTypeDef] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[TimestampTypeDef] = None
    CopySourceRange: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str | bytes] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class CORSRuleUnionTypeDef(BaseValidatorModel):
    pass


class CORSConfigurationTypeDef(BaseValidatorModel):
    CORSRules: Sequence[CORSRuleUnionTypeDef]


class CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef(BaseValidatorModel):
    MultipartUpload: Optional[CompletedMultipartUploadTypeDef] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    MpuObjectSize: Optional[int] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None


class CompleteMultipartUploadRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    MultipartUpload: Optional[CompletedMultipartUploadTypeDef] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    MpuObjectSize: Optional[int] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None


class CreateBucketRequestBucketCreateTypeDef(BaseValidatorModel):
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfigurationTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    ObjectOwnership: Optional[ObjectOwnershipType] = None


class CreateBucketRequestServiceResourceCreateBucketTypeDef(BaseValidatorModel):
    Bucket: str
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfigurationTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    ObjectOwnership: Optional[ObjectOwnershipType] = None


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
    ObjectOwnership: Optional[ObjectOwnershipType] = None


class ObjectLockConfigurationTypeDef(BaseValidatorModel):
    ObjectLockEnabled: Optional[Literal["Enabled"]] = None
    Rule: Optional[ObjectLockRuleTypeDef] = None


class NotificationConfigurationFilterOutputTypeDef(BaseValidatorModel):
    Key: Optional[S3KeyFilterOutputTypeDef] = None


class GetObjectAttributesOutputTypeDef(BaseValidatorModel):
    DeleteMarker: bool
    LastModified: datetime
    VersionId: str
    RequestCharged: Literal["requester"]
    ETag: str
    Checksum: ChecksumTypeDef
    ObjectParts: GetObjectAttributesPartsTypeDef
    StorageClass: StorageClassType
    ObjectSize: int
    ResponseMetadata: ResponseMetadataTypeDef


class AccessControlPolicyTypeDef(BaseValidatorModel):
    Grants: Optional[Sequence[GrantTypeDef]] = None
    Owner: Optional[OwnerTypeDef] = None


class GetBucketAclOutputTypeDef(BaseValidatorModel):
    Owner: OwnerTypeDef
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectAclOutputTypeDef(BaseValidatorModel):
    Owner: OwnerTypeDef
    Grants: List[GrantTypeDef]
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef


class S3LocationTypeDef(BaseValidatorModel):
    BucketName: str
    Prefix: str
    Encryption: Optional[EncryptionTypeDef] = None
    CannedACL: Optional[ObjectCannedACLType] = None
    AccessControlList: Optional[Sequence[GrantTypeDef]] = None
    Tagging: Optional[TaggingTypeDef] = None
    UserMetadata: Optional[Sequence[MetadataEntryTypeDef]] = None
    StorageClass: Optional[StorageClassType] = None


class ListMultipartUploadsOutputTypeDef(BaseValidatorModel):
    Bucket: str
    KeyMarker: str
    UploadIdMarker: str
    NextKeyMarker: str
    Prefix: str
    Delimiter: str
    NextUploadIdMarker: str
    MaxUploads: int
    IsTruncated: bool
    Uploads: List[MultipartUploadTypeDef]
    EncodingType: Literal["url"]
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef
    CommonPrefixes: Optional[List[CommonPrefixTypeDef]] = None


class InventoryS3BucketDestinationOutputTypeDef(BaseValidatorModel):
    Bucket: str
    Format: InventoryFormatType
    AccountId: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[InventoryEncryptionOutputTypeDef] = None


class InventoryS3BucketDestinationTypeDef(BaseValidatorModel):
    Bucket: str
    Format: InventoryFormatType
    AccountId: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[InventoryEncryptionTypeDef] = None


class SelectObjectContentRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Expression: str
    ExpressionType: Literal["SQL"]
    InputSerialization: InputSerializationTypeDef
    OutputSerialization: OutputSerializationTypeDef
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str | bytes] = None
    RequestProgress: Optional[RequestProgressTypeDef] = None
    ScanRange: Optional[ScanRangeTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None


class SelectParametersTypeDef(BaseValidatorModel):
    InputSerialization: InputSerializationTypeDef
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: OutputSerializationTypeDef


class GetBucketLifecycleOutputTypeDef(BaseValidatorModel):
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketMetadataTableConfigurationResultTypeDef(BaseValidatorModel):
    MetadataTableConfigurationResult: MetadataTableConfigurationResultTypeDef
    Status: str
    Error: Optional[ErrorDetailsTypeDef] = None


class CreateBucketMetadataTableConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    MetadataTableConfiguration: MetadataTableConfigurationTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class DestinationTypeDef(BaseValidatorModel):
    Bucket: str
    Account: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    AccessControlTranslation: Optional[AccessControlTranslationTypeDef] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    ReplicationTime: Optional[ReplicationTimeTypeDef] = None
    Metrics: Optional[MetricsTypeDef] = None


class ListObjectsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    Marker: str
    NextMarker: str
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    EncodingType: Literal["url"]
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef
    Contents: Optional[List[ObjectTypeDef]] = None
    CommonPrefixes: Optional[List[CommonPrefixTypeDef]] = None


class ListObjectsV2OutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    EncodingType: Literal["url"]
    KeyCount: int
    ContinuationToken: str
    NextContinuationToken: str
    StartAfter: str
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef
    Contents: Optional[List[ObjectTypeDef]] = None
    CommonPrefixes: Optional[List[CommonPrefixTypeDef]] = None


class ListObjectVersionsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    KeyMarker: str
    VersionIdMarker: str
    NextKeyMarker: str
    NextVersionIdMarker: str
    Versions: List[ObjectVersionTypeDef]
    DeleteMarkers: List[DeleteMarkerEntryTypeDef]
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    EncodingType: Literal["url"]
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef
    CommonPrefixes: Optional[List[CommonPrefixTypeDef]] = None


class GetBucketOwnershipControlsOutputTypeDef(BaseValidatorModel):
    OwnershipControls: OwnershipControlsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoggingEnabledOutputTypeDef(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatOutputTypeDef] = None


class RedirectAllRequestsToTypeDef(BaseValidatorModel):
    pass


class GetBucketWebsiteOutputTypeDef(BaseValidatorModel):
    RedirectAllRequestsTo: RedirectAllRequestsToTypeDef
    IndexDocument: IndexDocumentTypeDef
    ErrorDocument: ErrorDocumentTypeDef
    RoutingRules: List[RoutingRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class WebsiteConfigurationTypeDef(BaseValidatorModel):
    ErrorDocument: Optional[ErrorDocumentTypeDef] = None
    IndexDocument: Optional[IndexDocumentTypeDef] = None
    RedirectAllRequestsTo: Optional[RedirectAllRequestsToTypeDef] = None
    RoutingRules: Optional[Sequence[RoutingRuleTypeDef]] = None


class ServerSideEncryptionConfigurationOutputTypeDef(BaseValidatorModel):
    Rules: List[ServerSideEncryptionRuleTypeDef]


class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    Rules: Sequence[ServerSideEncryptionRuleTypeDef]


class SelectObjectContentEventStreamTypeDef(BaseValidatorModel):
    Records: Optional[RecordsEventTypeDef] = None
    Stats: Optional[StatsEventTypeDef] = None
    Progress: Optional[ProgressEventTypeDef] = None
    Cont: Optional[Dict[str, Any]] = None
    End: Optional[Dict[str, Any]] = None


class CloudFunctionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class TopicConfigurationDeprecatedUnionTypeDef(BaseValidatorModel):
    pass


class QueueConfigurationDeprecatedUnionTypeDef(BaseValidatorModel):
    pass


class NotificationConfigurationDeprecatedTypeDef(BaseValidatorModel):
    TopicConfiguration: Optional[TopicConfigurationDeprecatedUnionTypeDef] = None
    QueueConfiguration: Optional[QueueConfigurationDeprecatedUnionTypeDef] = None
    CloudFunctionConfiguration: Optional[CloudFunctionConfigurationUnionTypeDef] = None


class DeleteObjectsRequestBucketDeleteObjectsTypeDef(BaseValidatorModel):
    Delete: DeleteTypeDef
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None


class DeleteObjectsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delete: DeleteTypeDef
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None


class ObjectLockRetentionUnionTypeDef(BaseValidatorModel):
    pass


class PutObjectRetentionRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Retention: Optional[ObjectLockRetentionUnionTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    BypassGovernanceRetention: Optional[bool] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class LifecycleExpirationUnionTypeDef(BaseValidatorModel):
    pass


class TransitionUnionTypeDef(BaseValidatorModel):
    pass


class RuleTypeDef(BaseValidatorModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationUnionTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionUnionTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None


class IntelligentTieringConfigurationOutputTypeDef(BaseValidatorModel):
    Id: str
    Status: IntelligentTieringStatusType
    Tierings: List[TieringTypeDef]
    Filter: Optional[IntelligentTieringFilterOutputTypeDef] = None


class IntelligentTieringConfigurationTypeDef(BaseValidatorModel):
    Id: str
    Status: IntelligentTieringStatusType
    Tierings: Sequence[TieringTypeDef]
    Filter: Optional[IntelligentTieringFilterTypeDef] = None


class LifecycleRuleOutputTypeDef(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutputTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterOutputTypeDef] = None
    Transitions: Optional[List[TransitionOutputTypeDef]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None


class LifecycleRuleAndOperatorUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleRuleFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorUnionTypeDef] = None


class MetricsConfigurationOutputTypeDef(BaseValidatorModel):
    Id: str
    Filter: Optional[MetricsFilterOutputTypeDef] = None


class MetricsConfigurationTypeDef(BaseValidatorModel):
    Id: str
    Filter: Optional[MetricsFilterTypeDef] = None


class StorageClassAnalysisTypeDef(BaseValidatorModel):
    DataExport: Optional[StorageClassAnalysisDataExportTypeDef] = None


class PutBucketCorsRequestBucketCorsPutTypeDef(BaseValidatorModel):
    CORSConfiguration: CORSConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketCorsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    CORSConfiguration: CORSConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class GetObjectLockConfigurationOutputTypeDef(BaseValidatorModel):
    ObjectLockConfiguration: ObjectLockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutObjectLockConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ObjectLockConfiguration: Optional[ObjectLockConfigurationTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Token: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class LambdaFunctionConfigurationOutputTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutputTypeDef] = None


class QueueConfigurationOutputTypeDef(BaseValidatorModel):
    QueueArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutputTypeDef] = None


class TopicConfigurationOutputTypeDef(BaseValidatorModel):
    TopicArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutputTypeDef] = None


class S3KeyFilterUnionTypeDef(BaseValidatorModel):
    pass


class NotificationConfigurationFilterTypeDef(BaseValidatorModel):
    Key: Optional[S3KeyFilterUnionTypeDef] = None


class PutBucketAclRequestBucketAclPutTypeDef(BaseValidatorModel):
    ACL: Optional[BucketCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicyTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketAclRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ACL: Optional[BucketCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicyTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectAclRequestObjectAclPutTypeDef(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicyTypeDef] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectAclRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicyTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class OutputLocationTypeDef(BaseValidatorModel):
    S3: Optional[S3LocationTypeDef] = None


class InventoryDestinationOutputTypeDef(BaseValidatorModel):
    S3BucketDestination: InventoryS3BucketDestinationOutputTypeDef


class InventoryDestinationTypeDef(BaseValidatorModel):
    S3BucketDestination: InventoryS3BucketDestinationTypeDef


class GetBucketMetadataTableConfigurationOutputTypeDef(BaseValidatorModel):
    GetBucketMetadataTableConfigurationResult: GetBucketMetadataTableConfigurationResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReplicationRuleOutputTypeDef(BaseValidatorModel):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
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
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilterTypeDef] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteriaTypeDef] = None
    ExistingObjectReplication: Optional[ExistingObjectReplicationTypeDef] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplicationTypeDef] = None


class OwnershipControlsUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketOwnershipControlsRequestTypeDef(BaseValidatorModel):
    Bucket: str
    OwnershipControls: OwnershipControlsUnionTypeDef
    ContentMD5: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class GetBucketLoggingOutputTypeDef(BaseValidatorModel):
    LoggingEnabled: LoggingEnabledOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TargetObjectKeyFormatUnionTypeDef(BaseValidatorModel):
    pass


class LoggingEnabledTypeDef(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[Sequence[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatUnionTypeDef] = None


class PutBucketWebsiteRequestBucketWebsitePutTypeDef(BaseValidatorModel):
    WebsiteConfiguration: WebsiteConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketWebsiteRequestTypeDef(BaseValidatorModel):
    Bucket: str
    WebsiteConfiguration: WebsiteConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class GetBucketEncryptionOutputTypeDef(BaseValidatorModel):
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SelectObjectContentOutputTypeDef(BaseValidatorModel):
    Payload: EventStream[SelectObjectContentEventStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutBucketNotificationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationDeprecatedTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class GetBucketIntelligentTieringConfigurationOutputTypeDef(BaseValidatorModel):
    IntelligentTieringConfiguration: IntelligentTieringConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBucketIntelligentTieringConfigurationsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    IntelligentTieringConfigurationList: List[IntelligentTieringConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketLifecycleConfigurationOutputTypeDef(BaseValidatorModel):
    Rules: List[LifecycleRuleOutputTypeDef]
    TransitionDefaultMinimumObjectSize: TransitionDefaultMinimumObjectSizeType
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketMetricsConfigurationOutputTypeDef(BaseValidatorModel):
    MetricsConfiguration: MetricsConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBucketMetricsConfigurationsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    MetricsConfigurationList: List[MetricsConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AnalyticsConfigurationOutputTypeDef(BaseValidatorModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysisTypeDef
    Filter: Optional[AnalyticsFilterOutputTypeDef] = None


class AnalyticsConfigurationTypeDef(BaseValidatorModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysisTypeDef
    Filter: Optional[AnalyticsFilterTypeDef] = None


class NotificationConfigurationResponseTypeDef(BaseValidatorModel):
    TopicConfigurations: List[TopicConfigurationOutputTypeDef]
    QueueConfigurations: List[QueueConfigurationOutputTypeDef]
    LambdaFunctionConfigurations: List[LambdaFunctionConfigurationOutputTypeDef]
    EventBridgeConfiguration: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef


class InventoryConfigurationOutputTypeDef(BaseValidatorModel):
    Destination: InventoryDestinationOutputTypeDef
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersionsType
    Schedule: InventoryScheduleTypeDef
    Filter: Optional[InventoryFilterTypeDef] = None
    OptionalFields: Optional[List[InventoryOptionalFieldType]] = None


class InventoryConfigurationTypeDef(BaseValidatorModel):
    Destination: InventoryDestinationTypeDef
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersionsType
    Schedule: InventoryScheduleTypeDef
    Filter: Optional[InventoryFilterTypeDef] = None
    OptionalFields: Optional[Sequence[InventoryOptionalFieldType]] = None


class ReplicationConfigurationOutputTypeDef(BaseValidatorModel):
    Role: str
    Rules: List[ReplicationRuleOutputTypeDef]


class ReplicationConfigurationTypeDef(BaseValidatorModel):
    Role: str
    Rules: Sequence[ReplicationRuleTypeDef]


class ServerSideEncryptionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketEncryptionRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationUnionTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleConfigurationTypeDef(BaseValidatorModel):
    Rules: Sequence[RuleUnionTypeDef]


class IntelligentTieringConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketIntelligentTieringConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    IntelligentTieringConfiguration: IntelligentTieringConfigurationUnionTypeDef


class LifecycleRuleFilterUnionTypeDef(BaseValidatorModel):
    pass


class LifecycleRuleTypeDef(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationUnionTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterUnionTypeDef] = None
    Transitions: Optional[Sequence[TransitionUnionTypeDef]] = None
    NoncurrentVersionTransitions: Optional[Sequence[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None


class MetricsConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketMetricsConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    MetricsConfiguration: MetricsConfigurationUnionTypeDef
    ExpectedBucketOwner: Optional[str] = None


class GetBucketAnalyticsConfigurationOutputTypeDef(BaseValidatorModel):
    AnalyticsConfiguration: AnalyticsConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBucketAnalyticsConfigurationsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    AnalyticsConfigurationList: List[AnalyticsConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class NotificationConfigurationFilterUnionTypeDef(BaseValidatorModel):
    pass


class LambdaFunctionConfigurationTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterUnionTypeDef] = None


class QueueConfigurationTypeDef(BaseValidatorModel):
    QueueArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterUnionTypeDef] = None


class TopicConfigurationTypeDef(BaseValidatorModel):
    TopicArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterUnionTypeDef] = None


class RestoreRequestTypeDef(BaseValidatorModel):
    pass


class RestoreObjectRequestObjectRestoreObjectTypeDef(BaseValidatorModel):
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequestTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class RestoreObjectRequestObjectSummaryRestoreObjectTypeDef(BaseValidatorModel):
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequestTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class RestoreObjectRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequestTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class GetBucketInventoryConfigurationOutputTypeDef(BaseValidatorModel):
    InventoryConfiguration: InventoryConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBucketInventoryConfigurationsOutputTypeDef(BaseValidatorModel):
    ContinuationToken: str
    InventoryConfigurationList: List[InventoryConfigurationOutputTypeDef]
    IsTruncated: bool
    NextContinuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketReplicationOutputTypeDef(BaseValidatorModel):
    ReplicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoggingEnabledUnionTypeDef(BaseValidatorModel):
    pass


class BucketLoggingStatusTypeDef(BaseValidatorModel):
    LoggingEnabled: Optional[LoggingEnabledUnionTypeDef] = None


class PutBucketLifecycleRequestBucketLifecyclePutTypeDef(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketLifecycleRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None


class AnalyticsConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketAnalyticsConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    AnalyticsConfiguration: AnalyticsConfigurationUnionTypeDef
    ExpectedBucketOwner: Optional[str] = None


class InventoryConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketInventoryConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    InventoryConfiguration: InventoryConfigurationUnionTypeDef
    ExpectedBucketOwner: Optional[str] = None


class ReplicationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutBucketReplicationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationUnionTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    Token: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketLoggingRequestBucketLoggingPutTypeDef(BaseValidatorModel):
    BucketLoggingStatus: BucketLoggingStatusTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketLoggingRequestTypeDef(BaseValidatorModel):
    Bucket: str
    BucketLoggingStatus: BucketLoggingStatusTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class LifecycleRuleUnionTypeDef(BaseValidatorModel):
    pass


class BucketLifecycleConfigurationTypeDef(BaseValidatorModel):
    Rules: Sequence[LifecycleRuleUnionTypeDef]


class QueueConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class TopicConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class LambdaFunctionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class NotificationConfigurationTypeDef(BaseValidatorModel):
    TopicConfigurations: Optional[Sequence[TopicConfigurationUnionTypeDef]] = None
    QueueConfigurations: Optional[Sequence[QueueConfigurationUnionTypeDef]] = None
    LambdaFunctionConfigurations: Optional[Sequence[LambdaFunctionConfigurationUnionTypeDef]] = None
    EventBridgeConfiguration: Optional[Mapping[str, Any]] = None


class PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None
    TransitionDefaultMinimumObjectSize: Optional[TransitionDefaultMinimumObjectSizeType] = None


class PutBucketLifecycleConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None
    TransitionDefaultMinimumObjectSize: Optional[TransitionDefaultMinimumObjectSizeType] = None


class PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef(BaseValidatorModel):
    NotificationConfiguration: NotificationConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None


class PutBucketNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None


