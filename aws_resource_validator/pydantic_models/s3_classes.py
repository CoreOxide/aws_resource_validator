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
from aws_resource_validator.pydantic_models.s3_constants import *

class AbortIncompleteMultipartUploadTypeDef(BaseModel):
    DaysAfterInitiation: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AbortMultipartUploadRequestMultipartUploadAbortTypeDef(BaseModel):
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class AbortMultipartUploadRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class AccelerateConfigurationTypeDef(BaseModel):
    Status: Optional[BucketAccelerateStatusType] = None

class OwnerTypeDef(BaseModel):
    DisplayName: Optional[str] = None
    ID: Optional[str] = None

class AccessControlTranslationTypeDef(BaseModel):
    Owner: Literal["Destination"]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AnalyticsS3BucketDestinationTypeDef(BaseModel):
    Format: Literal["CSV"]
    Bucket: str
    BucketAccountId: Optional[str] = None
    Prefix: Optional[str] = None

class CopySourceTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None

class BucketDownloadFileRequestTypeDef(BaseModel):
    Key: str
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class BucketInfoTypeDef(BaseModel):
    DataRedundancy: Optional[Literal["SingleAvailabilityZone"]] = None
    Type: Optional[Literal["Directory"]] = None

class BucketTypeDef(BaseModel):
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None

class BucketUploadFileRequestTypeDef(BaseModel):
    Filename: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class CORSRuleTypeDef(BaseModel):
    AllowedMethods: Sequence[str]
    AllowedOrigins: Sequence[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAgeSeconds: Optional[int] = None

class CORSRuleExtraOutputTypeDef(BaseModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAgeSeconds: Optional[int] = None

class CORSRuleOutputTypeDef(BaseModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAgeSeconds: Optional[int] = None

class CSVInputTypeDef(BaseModel):
    FileHeaderInfo: Optional[FileHeaderInfoType] = None
    Comments: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None
    AllowQuotedRecordDelimiter: Optional[bool] = None

class CSVOutputTypeDef(BaseModel):
    QuoteFields: Optional[QuoteFieldsType] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None

class ChecksumTypeDef(BaseModel):
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class ClientDownloadFileRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientGeneratePresignedPostRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    Fields: Optional[Optional[Dict[str, Any]]] = None
    Conditions: Optional[Union[List[Any], Dict[str, Any], None]] = None
    ExpiresIn: Optional[int] = None

class ClientUploadFileRequestTypeDef(BaseModel):
    Filename: str
    Bucket: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class CloudFunctionConfigurationOutputTypeDef(BaseModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    CloudFunction: Optional[str] = None
    InvocationRole: Optional[str] = None

class CloudFunctionConfigurationTypeDef(BaseModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[Sequence[EventType]] = None
    CloudFunction: Optional[str] = None
    InvocationRole: Optional[str] = None

class CommonPrefixTypeDef(BaseModel):
    Prefix: Optional[str] = None

class CompletedPartTypeDef(BaseModel):
    ETag: Optional[str] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    PartNumber: Optional[int] = None

class ConditionTypeDef(BaseModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None

class CopyObjectResultTypeDef(BaseModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class CopyPartResultTypeDef(BaseModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class LocationInfoTypeDef(BaseModel):
    Type: Optional[Literal["AvailabilityZone"]] = None
    Name: Optional[str] = None

class SessionCredentialsTypeDef(BaseModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime

class CreateSessionRequestRequestTypeDef(BaseModel):
    Bucket: str
    SessionMode: Optional[SessionModeType] = None

class DefaultRetentionTypeDef(BaseModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    Days: Optional[int] = None
    Years: Optional[int] = None

class DeleteBucketAnalyticsConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketCorsRequestBucketCorsDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketCorsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketEncryptionRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str

class DeleteBucketInventoryConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketLifecycleRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketMetricsConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketOwnershipControlsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketPolicyRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketReplicationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketRequestBucketDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketTaggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef(BaseModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketWebsiteRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteMarkerReplicationTypeDef(BaseModel):
    Status: Optional[DeleteMarkerReplicationStatusType] = None

class DeleteObjectRequestObjectDeleteTypeDef(BaseModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectRequestObjectSummaryDeleteTypeDef(BaseModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectRequestObjectVersionDeleteTypeDef(BaseModel):
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectTaggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class DeletedObjectTypeDef(BaseModel):
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    DeleteMarker: Optional[bool] = None
    DeleteMarkerVersionId: Optional[str] = None

class ErrorTypeDef(BaseModel):
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Code: Optional[str] = None
    Message: Optional[str] = None

class DeletePublicAccessBlockRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class ObjectIdentifierTypeDef(BaseModel):
    Key: str
    VersionId: Optional[str] = None

class EncryptionConfigurationTypeDef(BaseModel):
    ReplicaKmsKeyID: Optional[str] = None

class EncryptionTypeDef(BaseModel):
    EncryptionType: ServerSideEncryptionType
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None

class ErrorDocumentTypeDef(BaseModel):
    Key: str

class ExistingObjectReplicationTypeDef(BaseModel):
    Status: ExistingObjectReplicationStatusType

class FilterRuleTypeDef(BaseModel):
    Name: Optional[FilterRuleNameType] = None
    Value: Optional[str] = None

class GetBucketAccelerateConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class GetBucketAclRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketAnalyticsConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketCorsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketEncryptionRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketIntelligentTieringConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str

class GetBucketInventoryConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLifecycleRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLocationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLoggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketMetricsConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketNotificationConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketOwnershipControlsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketPolicyRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class PolicyStatusTypeDef(BaseModel):
    IsPublic: Optional[bool] = None

class GetBucketPolicyStatusRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketReplicationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketRequestPaymentRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketTaggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketVersioningRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class IndexDocumentTypeDef(BaseModel):
    Suffix: str

class RedirectAllRequestsToTypeDef(BaseModel):
    HostName: str
    Protocol: Optional[ProtocolType] = None

class GetBucketWebsiteRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetObjectAclRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class ObjectPartTypeDef(BaseModel):
    PartNumber: Optional[int] = None
    Size: Optional[int] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class GetObjectAttributesRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    ObjectAttributes: Sequence[ObjectAttributesType]
    VersionId: Optional[str] = None
    MaxParts: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class ObjectLockLegalHoldTypeDef(BaseModel):
    Status: Optional[ObjectLockLegalHoldStatusType] = None

class GetObjectLegalHoldRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class GetObjectLockConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class ObjectLockRetentionOutputTypeDef(BaseModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[datetime] = None

class GetObjectRetentionRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class GetObjectTaggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class GetObjectTorrentRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class PublicAccessBlockConfigurationTypeDef(BaseModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None

class GetPublicAccessBlockRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GlacierJobParametersTypeDef(BaseModel):
    Tier: TierType

class GranteeTypeDef(BaseModel):
    Type: TypeType
    DisplayName: Optional[str] = None
    EmailAddress: Optional[str] = None
    ID: Optional[str] = None
    URI: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class HeadBucketRequestRequestTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class InitiatorTypeDef(BaseModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None

class JSONInputTypeDef(BaseModel):
    Type: Optional[JSONTypeType] = None

class TieringTypeDef(BaseModel):
    Days: int
    AccessTier: IntelligentTieringAccessTierType

class InventoryFilterTypeDef(BaseModel):
    Prefix: str

class InventoryScheduleTypeDef(BaseModel):
    Frequency: InventoryFrequencyType

class SSEKMSTypeDef(BaseModel):
    KeyId: str

class JSONOutputTypeDef(BaseModel):
    RecordDelimiter: Optional[str] = None

class LifecycleExpirationExtraExtraOutputTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class LifecycleExpirationExtraOutputTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class LifecycleExpirationOutputTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class NoncurrentVersionExpirationTypeDef(BaseModel):
    NoncurrentDays: Optional[int] = None
    NewerNoncurrentVersions: Optional[int] = None

class NoncurrentVersionTransitionTypeDef(BaseModel):
    NoncurrentDays: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None
    NewerNoncurrentVersions: Optional[int] = None

class TransitionExtraOutputTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class TransitionOutputTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class ListBucketAnalyticsConfigurationsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ContinuationToken: Optional[str] = None

class ListBucketInventoryConfigurationsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class ListBucketMetricsConfigurationsRequestRequestTypeDef(BaseModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDirectoryBucketsRequestRequestTypeDef(BaseModel):
    ContinuationToken: Optional[str] = None
    MaxDirectoryBuckets: Optional[int] = None

class ListMultipartUploadsRequestRequestTypeDef(BaseModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    KeyMarker: Optional[str] = None
    MaxUploads: Optional[int] = None
    Prefix: Optional[str] = None
    UploadIdMarker: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class ListObjectVersionsRequestRequestTypeDef(BaseModel):
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

class ListObjectsRequestRequestTypeDef(BaseModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Marker: Optional[str] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None

class ListObjectsV2RequestRequestTypeDef(BaseModel):
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

class PartTypeDef(BaseModel):
    PartNumber: Optional[int] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class ListPartsRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    UploadId: str
    MaxParts: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None

class MetadataEntryTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ReplicationTimeValueTypeDef(BaseModel):
    Minutes: Optional[int] = None

class QueueConfigurationDeprecatedOutputTypeDef(BaseModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    Queue: Optional[str] = None

class TopicConfigurationDeprecatedOutputTypeDef(BaseModel):
    Id: Optional[str] = None
    Events: Optional[List[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None

class QueueConfigurationDeprecatedTypeDef(BaseModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[Sequence[EventType]] = None
    Queue: Optional[str] = None

class TopicConfigurationDeprecatedTypeDef(BaseModel):
    Id: Optional[str] = None
    Events: Optional[Sequence[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None

class ObjectDownloadFileRequestTypeDef(BaseModel):
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class RestoreStatusTypeDef(BaseModel):
    IsRestoreInProgress: Optional[bool] = None
    RestoreExpiryDate: Optional[datetime] = None

class ObjectUploadFileRequestTypeDef(BaseModel):
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class OwnershipControlsRuleTypeDef(BaseModel):
    ObjectOwnership: ObjectOwnershipType

class PartitionedPrefixTypeDef(BaseModel):
    PartitionDateSource: Optional[PartitionDateSourceType] = None

class ProgressTypeDef(BaseModel):
    BytesScanned: Optional[int] = None
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None

class PutBucketPolicyRequestBucketPolicyPutTypeDef(BaseModel):
    Policy: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketPolicyRequestRequestTypeDef(BaseModel):
    Bucket: str
    Policy: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class RequestPaymentConfigurationTypeDef(BaseModel):
    Payer: PayerType

class PutBucketVersioningRequestBucketVersioningEnableTypeDef(BaseModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class VersioningConfigurationTypeDef(BaseModel):
    MFADelete: Optional[MFADeleteType] = None
    Status: Optional[BucketVersioningStatusType] = None

class PutBucketVersioningRequestBucketVersioningSuspendTypeDef(BaseModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class RecordsEventTypeDef(BaseModel):
    Payload: Optional[bytes] = None

class RedirectTypeDef(BaseModel):
    HostName: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[ProtocolType] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None

class ReplicaModificationsTypeDef(BaseModel):
    Status: ReplicaModificationsStatusType

class RequestProgressTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class TransitionExtraExtraOutputTypeDef(BaseModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class ScanRangeTypeDef(BaseModel):
    Start: Optional[int] = None
    End: Optional[int] = None

class ServerSideEncryptionByDefaultTypeDef(BaseModel):
    SSEAlgorithm: ServerSideEncryptionType
    KMSMasterKeyID: Optional[str] = None

class SseKmsEncryptedObjectsTypeDef(BaseModel):
    Status: SseKmsEncryptedObjectsStatusType

class StatsTypeDef(BaseModel):
    BytesScanned: Optional[int] = None
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None

class AbortMultipartUploadOutputTypeDef(BaseModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class CompleteMultipartUploadOutputTypeDef(BaseModel):
    Location: str
    Bucket: str
    Key: str
    Expiration: str
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ServerSideEncryption: ServerSideEncryptionType
    VersionId: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBucketOutputTypeDef(BaseModel):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultipartUploadOutputTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteObjectOutputTypeDef(BaseModel):
    DeleteMarker: bool
    VersionId: str
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteObjectTaggingOutputTypeDef(BaseModel):
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketAccelerateConfigurationOutputTypeDef(BaseModel):
    Status: BucketAccelerateStatusType
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketLocationOutputTypeDef(BaseModel):
    LocationConstraint: BucketLocationConstraintType
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketPolicyOutputTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketRequestPaymentOutputTypeDef(BaseModel):
    Payer: PayerType
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketVersioningOutputTypeDef(BaseModel):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectOutputTypeDef(BaseModel):
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
    ChecksumSHA1: str
    ChecksumSHA256: str
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

class GetObjectTorrentOutputTypeDef(BaseModel):
    Body: StreamingBody
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class HeadBucketOutputTypeDef(BaseModel):
    BucketLocationType: Literal["AvailabilityZone"]
    BucketLocationName: str
    BucketRegion: str
    AccessPointAlias: bool
    ResponseMetadata: ResponseMetadataTypeDef

class HeadObjectOutputTypeDef(BaseModel):
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    ArchiveStatus: ArchiveStatusType
    LastModified: datetime
    ContentLength: int
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ETag: str
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
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
    ObjectLockMode: ObjectLockModeType
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectAclOutputTypeDef(BaseModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectLegalHoldOutputTypeDef(BaseModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectLockConfigurationOutputTypeDef(BaseModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectOutputTypeDef(BaseModel):
    Expiration: str
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    ServerSideEncryption: ServerSideEncryptionType
    VersionId: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectRetentionOutputTypeDef(BaseModel):
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectTaggingOutputTypeDef(BaseModel):
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreObjectOutputTypeDef(BaseModel):
    RequestCharged: Literal["requester"]
    RestoreOutputPath: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadPartOutputTypeDef(BaseModel):
    ServerSideEncryption: ServerSideEncryptionType
    ETag: str
    ChecksumCRC32: str
    ChecksumCRC32C: str
    ChecksumSHA1: str
    ChecksumSHA256: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketAccelerateConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    AccelerateConfiguration: AccelerateConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

class DeleteMarkerEntryTypeDef(BaseModel):
    Owner: Optional[OwnerTypeDef] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    IsLatest: Optional[bool] = None
    LastModified: Optional[datetime] = None

class AnalyticsAndOperatorOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class AnalyticsAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetBucketTaggingOutputTypeDef(BaseModel):
    TagSet: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectTaggingOutputTypeDef(BaseModel):
    VersionId: str
    TagSet: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IntelligentTieringAndOperatorOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class IntelligentTieringAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LifecycleRuleAndOperatorExtraOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

class LifecycleRuleAndOperatorOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

class LifecycleRuleAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

class MetricsAndOperatorOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    AccessPointArn: Optional[str] = None

class MetricsAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AccessPointArn: Optional[str] = None

class ReplicationRuleAndOperatorOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ReplicationRuleAndOperatorTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TaggingTypeDef(BaseModel):
    TagSet: Sequence[TagTypeDef]

class AnalyticsExportDestinationTypeDef(BaseModel):
    S3BucketDestination: AnalyticsS3BucketDestinationTypeDef

class UploadPartRequestMultipartUploadPartUploadTypeDef(BaseModel):
    Body: Optional[BlobTypeDef] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class UploadPartRequestRequestTypeDef(BaseModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class BucketCopyRequestTypeDef(BaseModel):
    CopySource: CopySourceTypeDef
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    SourceClient: Optional[Optional[BaseClient]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientCopyRequestTypeDef(BaseModel):
    CopySource: CopySourceTypeDef
    Bucket: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    SourceClient: Optional[Optional[BaseClient]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ObjectCopyRequestTypeDef(BaseModel):
    CopySource: CopySourceTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    SourceClient: Optional[Optional[BaseClient]] = None
    Config: Optional[Optional[TransferConfig]] = None

class BucketDownloadFileobjRequestTypeDef(BaseModel):
    Key: str
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class BucketUploadFileobjRequestTypeDef(BaseModel):
    Fileobj: FileobjTypeDef
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientDownloadFileobjRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientUploadFileobjRequestTypeDef(BaseModel):
    Fileobj: FileobjTypeDef
    Bucket: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ObjectDownloadFileobjRequestTypeDef(BaseModel):
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ObjectUploadFileobjRequestTypeDef(BaseModel):
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ListBucketsOutputTypeDef(BaseModel):
    Buckets: List[BucketTypeDef]
    Owner: OwnerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDirectoryBucketsOutputTypeDef(BaseModel):
    Buckets: List[BucketTypeDef]
    ContinuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CORSConfigurationTypeDef(BaseModel):
    CORSRules: Sequence[CORSRuleTypeDef]

class GetBucketCorsOutputTypeDef(BaseModel):
    CORSRules: List[CORSRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CompletedMultipartUploadTypeDef(BaseModel):
    Parts: Optional[Sequence[CompletedPartTypeDef]] = None

class CopyObjectOutputTypeDef(BaseModel):
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

class CopyObjectRequestObjectCopyFromTypeDef(BaseModel):
    CopySource: str
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str] = None
    CopySourceSSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None

class CopyObjectRequestObjectSummaryCopyFromTypeDef(BaseModel):
    CopySource: str
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str] = None
    CopySourceSSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None

class CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
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

class CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
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

class CreateMultipartUploadRequestRequestTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
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

class GetObjectRequestObjectGetTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class GetObjectRequestObjectSummaryGetTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class GetObjectRequestObjectVersionGetTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class GetObjectRequestRequestTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class HeadObjectRequestObjectVersionHeadTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class HeadObjectRequestRequestTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class LifecycleExpirationTypeDef(BaseModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class ObjectLockRetentionTypeDef(BaseModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[TimestampTypeDef] = None

class PutObjectRequestBucketPutObjectTypeDef(BaseModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutObjectRequestObjectPutTypeDef(BaseModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutObjectRequestObjectSummaryPutTypeDef(BaseModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutObjectRequestRequestTypeDef(BaseModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None

class TransitionTypeDef(BaseModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class WriteGetObjectResponseRequestRequestTypeDef(BaseModel):
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
    SSECustomerKeyMD5: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    TagCount: Optional[int] = None
    VersionId: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None

class UploadPartCopyOutputTypeDef(BaseModel):
    CopySourceVersionId: str
    CopyPartResult: CopyPartResultTypeDef
    ServerSideEncryption: ServerSideEncryptionType
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBucketConfigurationTypeDef(BaseModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None
    Location: Optional[LocationInfoTypeDef] = None
    Bucket: Optional[BucketInfoTypeDef] = None

class CreateSessionOutputTypeDef(BaseModel):
    Credentials: SessionCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ObjectLockRuleTypeDef(BaseModel):
    DefaultRetention: Optional[DefaultRetentionTypeDef] = None

class DeleteObjectsOutputTypeDef(BaseModel):
    Deleted: List[DeletedObjectTypeDef]
    RequestCharged: Literal["requester"]
    Errors: List[ErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTypeDef(BaseModel):
    Objects: Sequence[ObjectIdentifierTypeDef]
    Quiet: Optional[bool] = None

class S3KeyFilterExtraOutputTypeDef(BaseModel):
    FilterRules: Optional[List[FilterRuleTypeDef]] = None

class S3KeyFilterOutputTypeDef(BaseModel):
    FilterRules: Optional[List[FilterRuleTypeDef]] = None

class S3KeyFilterTypeDef(BaseModel):
    FilterRules: Optional[Sequence[FilterRuleTypeDef]] = None

class GetBucketPolicyStatusOutputTypeDef(BaseModel):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectAttributesPartsTypeDef(BaseModel):
    TotalPartsCount: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    NextPartNumberMarker: Optional[int] = None
    MaxParts: Optional[int] = None
    IsTruncated: Optional[bool] = None
    Parts: Optional[List[ObjectPartTypeDef]] = None

class GetObjectLegalHoldOutputTypeDef(BaseModel):
    LegalHold: ObjectLockLegalHoldTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectLegalHoldRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    LegalHold: Optional[ObjectLockLegalHoldTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class GetObjectRetentionOutputTypeDef(BaseModel):
    Retention: ObjectLockRetentionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicAccessBlockOutputTypeDef(BaseModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPublicAccessBlockRequestRequestTypeDef(BaseModel):
    Bucket: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class GrantTypeDef(BaseModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None

class TargetGrantTypeDef(BaseModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[BucketLogsPermissionType] = None

class HeadBucketRequestBucketExistsWaitTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class HeadBucketRequestBucketNotExistsWaitTypeDef(BaseModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class HeadObjectRequestObjectExistsWaitTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class HeadObjectRequestObjectNotExistsWaitTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class MultipartUploadTypeDef(BaseModel):
    UploadId: Optional[str] = None
    Key: Optional[str] = None
    Initiated: Optional[datetime] = None
    StorageClass: Optional[StorageClassType] = None
    Owner: Optional[OwnerTypeDef] = None
    Initiator: Optional[InitiatorTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

class InputSerializationTypeDef(BaseModel):
    CSV: Optional[CSVInputTypeDef] = None
    CompressionType: Optional[CompressionTypeType] = None
    JSON: Optional[JSONInputTypeDef] = None
    Parquet: Optional[Mapping[str, Any]] = None

class InventoryEncryptionOutputTypeDef(BaseModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None

class InventoryEncryptionTypeDef(BaseModel):
    SSES3: Optional[Mapping[str, Any]] = None
    SSEKMS: Optional[SSEKMSTypeDef] = None

class OutputSerializationTypeDef(BaseModel):
    CSV: Optional[CSVOutputTypeDef] = None
    JSON: Optional[JSONOutputTypeDef] = None

class RuleOutputTypeDef(BaseModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutputTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionOutputTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class ListDirectoryBucketsRequestListDirectoryBucketsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartUploadsRequestListMultipartUploadsPaginateTypeDef(BaseModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectVersionsRequestListObjectVersionsPaginateTypeDef(BaseModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectsRequestListObjectsPaginateTypeDef(BaseModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectsV2RequestListObjectsV2PaginateTypeDef(BaseModel):
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

class ListPartsRequestListPartsPaginateTypeDef(BaseModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartsOutputTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class MetricsTypeDef(BaseModel):
    Status: MetricsStatusType
    EventThreshold: Optional[ReplicationTimeValueTypeDef] = None

class ReplicationTimeTypeDef(BaseModel):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValueTypeDef

class NotificationConfigurationDeprecatedResponseTypeDef(BaseModel):
    TopicConfiguration: TopicConfigurationDeprecatedOutputTypeDef
    QueueConfiguration: QueueConfigurationDeprecatedOutputTypeDef
    CloudFunctionConfiguration: CloudFunctionConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NotificationConfigurationDeprecatedTypeDef(BaseModel):
    TopicConfiguration: Optional[TopicConfigurationDeprecatedTypeDef] = None
    QueueConfiguration: Optional[QueueConfigurationDeprecatedTypeDef] = None
    CloudFunctionConfiguration: Optional[CloudFunctionConfigurationTypeDef] = None

class ObjectTypeDef(BaseModel):
    Key: Optional[str] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    Size: Optional[int] = None
    StorageClass: Optional[ObjectStorageClassType] = None
    Owner: Optional[OwnerTypeDef] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None

class ObjectVersionTypeDef(BaseModel):
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    Size: Optional[int] = None
    StorageClass: Optional[Literal["STANDARD"]] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    IsLatest: Optional[bool] = None
    LastModified: Optional[datetime] = None
    Owner: Optional[OwnerTypeDef] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None

class OwnershipControlsOutputTypeDef(BaseModel):
    Rules: List[OwnershipControlsRuleTypeDef]

class OwnershipControlsTypeDef(BaseModel):
    Rules: Sequence[OwnershipControlsRuleTypeDef]

class TargetObjectKeyFormatExtraOutputTypeDef(BaseModel):
    SimplePrefix: Optional[Dict[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefixTypeDef] = None

class TargetObjectKeyFormatOutputTypeDef(BaseModel):
    SimplePrefix: Optional[Dict[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefixTypeDef] = None

class TargetObjectKeyFormatTypeDef(BaseModel):
    SimplePrefix: Optional[Mapping[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefixTypeDef] = None

class ProgressEventTypeDef(BaseModel):
    Details: Optional[ProgressTypeDef] = None

class PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef(BaseModel):
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketRequestPaymentRequestRequestTypeDef(BaseModel):
    Bucket: str
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketVersioningRequestBucketVersioningPutTypeDef(BaseModel):
    VersioningConfiguration: VersioningConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketVersioningRequestRequestTypeDef(BaseModel):
    Bucket: str
    VersioningConfiguration: VersioningConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class RoutingRuleTypeDef(BaseModel):
    Redirect: RedirectTypeDef
    Condition: Optional[ConditionTypeDef] = None

class RuleExtraOutputTypeDef(BaseModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationExtraExtraOutputTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionExtraExtraOutputTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class ServerSideEncryptionRuleTypeDef(BaseModel):
    ApplyServerSideEncryptionByDefault: Optional[ServerSideEncryptionByDefaultTypeDef] = None
    BucketKeyEnabled: Optional[bool] = None

class SourceSelectionCriteriaTypeDef(BaseModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjectsTypeDef] = None
    ReplicaModifications: Optional[ReplicaModificationsTypeDef] = None

class StatsEventTypeDef(BaseModel):
    Details: Optional[StatsTypeDef] = None

class AnalyticsFilterOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[AnalyticsAndOperatorOutputTypeDef] = None

class AnalyticsFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[AnalyticsAndOperatorTypeDef] = None

class IntelligentTieringFilterOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[IntelligentTieringAndOperatorOutputTypeDef] = None

class IntelligentTieringFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[IntelligentTieringAndOperatorTypeDef] = None

class LifecycleRuleFilterExtraOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorExtraOutputTypeDef] = None

class LifecycleRuleFilterOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorOutputTypeDef] = None

class LifecycleRuleFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorTypeDef] = None

class MetricsFilterOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperatorOutputTypeDef] = None

class MetricsFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperatorTypeDef] = None

class ReplicationRuleFilterOutputTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorOutputTypeDef] = None

class ReplicationRuleFilterTypeDef(BaseModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    And: Optional[ReplicationRuleAndOperatorTypeDef] = None

class PutBucketTaggingRequestBucketTaggingPutTypeDef(BaseModel):
    Tagging: TaggingTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketTaggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    Tagging: TaggingTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutObjectTaggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    Tagging: TaggingTypeDef
    VersionId: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class StorageClassAnalysisDataExportTypeDef(BaseModel):
    OutputSchemaVersion: Literal["V_1"]
    Destination: AnalyticsExportDestinationTypeDef

class CopyObjectRequestRequestTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str] = None
    CopySourceSSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[TimestampTypeDef] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None

class UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef(BaseModel):
    CopySource: CopySourceOrStrTypeDef
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[TimestampTypeDef] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[TimestampTypeDef] = None
    CopySourceRange: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str] = None
    CopySourceSSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None

class UploadPartCopyRequestRequestTypeDef(BaseModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[str] = None
    CopySourceSSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None

class PutBucketCorsRequestBucketCorsPutTypeDef(BaseModel):
    CORSConfiguration: CORSConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketCorsRequestRequestTypeDef(BaseModel):
    Bucket: str
    CORSConfiguration: CORSConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef(BaseModel):
    MultipartUpload: Optional[CompletedMultipartUploadTypeDef] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None

class CompleteMultipartUploadRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    UploadId: str
    MultipartUpload: Optional[CompletedMultipartUploadTypeDef] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None

class PutObjectRetentionRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    Retention: Optional[ObjectLockRetentionTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    BypassGovernanceRetention: Optional[bool] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class RuleTypeDef(BaseModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class CreateBucketRequestBucketCreateTypeDef(BaseModel):
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfigurationTypeDef] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    ObjectOwnership: Optional[ObjectOwnershipType] = None

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
    ObjectOwnership: Optional[ObjectOwnershipType] = None

class CreateBucketRequestServiceResourceCreateBucketTypeDef(BaseModel):
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

class ObjectLockConfigurationTypeDef(BaseModel):
    ObjectLockEnabled: Optional[Literal["Enabled"]] = None
    Rule: Optional[ObjectLockRuleTypeDef] = None

class DeleteObjectsRequestBucketDeleteObjectsTypeDef(BaseModel):
    Delete: DeleteTypeDef
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

class DeleteObjectsRequestRequestTypeDef(BaseModel):
    Bucket: str
    Delete: DeleteTypeDef
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

class NotificationConfigurationFilterExtraOutputTypeDef(BaseModel):
    Key: Optional[S3KeyFilterExtraOutputTypeDef] = None

class NotificationConfigurationFilterOutputTypeDef(BaseModel):
    Key: Optional[S3KeyFilterOutputTypeDef] = None

class NotificationConfigurationFilterTypeDef(BaseModel):
    Key: Optional[S3KeyFilterTypeDef] = None

class GetObjectAttributesOutputTypeDef(BaseModel):
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

class AccessControlPolicyTypeDef(BaseModel):
    Grants: Optional[Sequence[GrantTypeDef]] = None
    Owner: Optional[OwnerTypeDef] = None

class GetBucketAclOutputTypeDef(BaseModel):
    Owner: OwnerTypeDef
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectAclOutputTypeDef(BaseModel):
    Owner: OwnerTypeDef
    Grants: List[GrantTypeDef]
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class S3LocationTypeDef(BaseModel):
    BucketName: str
    Prefix: str
    Encryption: Optional[EncryptionTypeDef] = None
    CannedACL: Optional[ObjectCannedACLType] = None
    AccessControlList: Optional[Sequence[GrantTypeDef]] = None
    Tagging: Optional[TaggingTypeDef] = None
    UserMetadata: Optional[Sequence[MetadataEntryTypeDef]] = None
    StorageClass: Optional[StorageClassType] = None

class ListMultipartUploadsOutputTypeDef(BaseModel):
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

class InventoryS3BucketDestinationOutputTypeDef(BaseModel):
    Bucket: str
    Format: InventoryFormatType
    AccountId: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[InventoryEncryptionOutputTypeDef] = None

class InventoryS3BucketDestinationTypeDef(BaseModel):
    Bucket: str
    Format: InventoryFormatType
    AccountId: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[InventoryEncryptionTypeDef] = None

class SelectObjectContentRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    Expression: str
    ExpressionType: Literal["SQL"]
    InputSerialization: InputSerializationTypeDef
    OutputSerialization: OutputSerializationTypeDef
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestProgress: Optional[RequestProgressTypeDef] = None
    ScanRange: Optional[ScanRangeTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class SelectParametersTypeDef(BaseModel):
    InputSerialization: InputSerializationTypeDef
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: OutputSerializationTypeDef

class GetBucketLifecycleOutputTypeDef(BaseModel):
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationTypeDef(BaseModel):
    Bucket: str
    Account: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    AccessControlTranslation: Optional[AccessControlTranslationTypeDef] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    ReplicationTime: Optional[ReplicationTimeTypeDef] = None
    Metrics: Optional[MetricsTypeDef] = None

class PutBucketNotificationRequestRequestTypeDef(BaseModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationDeprecatedTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class ListObjectsOutputTypeDef(BaseModel):
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

class ListObjectsV2OutputTypeDef(BaseModel):
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

class ListObjectVersionsOutputTypeDef(BaseModel):
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

class GetBucketOwnershipControlsOutputTypeDef(BaseModel):
    OwnershipControls: OwnershipControlsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketOwnershipControlsRequestRequestTypeDef(BaseModel):
    Bucket: str
    OwnershipControls: OwnershipControlsTypeDef
    ContentMD5: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class LoggingEnabledExtraOutputTypeDef(BaseModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatExtraOutputTypeDef] = None

class LoggingEnabledOutputTypeDef(BaseModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatOutputTypeDef] = None

class LoggingEnabledTypeDef(BaseModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[Sequence[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatTypeDef] = None

class GetBucketWebsiteOutputTypeDef(BaseModel):
    RedirectAllRequestsTo: RedirectAllRequestsToTypeDef
    IndexDocument: IndexDocumentTypeDef
    ErrorDocument: ErrorDocumentTypeDef
    RoutingRules: List[RoutingRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WebsiteConfigurationTypeDef(BaseModel):
    ErrorDocument: Optional[ErrorDocumentTypeDef] = None
    IndexDocument: Optional[IndexDocumentTypeDef] = None
    RedirectAllRequestsTo: Optional[RedirectAllRequestsToTypeDef] = None
    RoutingRules: Optional[Sequence[RoutingRuleTypeDef]] = None

class ServerSideEncryptionConfigurationOutputTypeDef(BaseModel):
    Rules: List[ServerSideEncryptionRuleTypeDef]

class ServerSideEncryptionConfigurationTypeDef(BaseModel):
    Rules: Sequence[ServerSideEncryptionRuleTypeDef]

class SelectObjectContentEventStreamTypeDef(BaseModel):
    Records: Optional[RecordsEventTypeDef] = None
    Stats: Optional[StatsEventTypeDef] = None
    Progress: Optional[ProgressEventTypeDef] = None
    Cont: Optional[Dict[str, Any]] = None
    End: Optional[Dict[str, Any]] = None

class IntelligentTieringConfigurationOutputTypeDef(BaseModel):
    Id: str
    Status: IntelligentTieringStatusType
    Tierings: List[TieringTypeDef]
    Filter: Optional[IntelligentTieringFilterOutputTypeDef] = None

class IntelligentTieringConfigurationTypeDef(BaseModel):
    Id: str
    Status: IntelligentTieringStatusType
    Tierings: Sequence[TieringTypeDef]
    Filter: Optional[IntelligentTieringFilterTypeDef] = None

class LifecycleRuleExtraOutputTypeDef(BaseModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationExtraOutputTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterExtraOutputTypeDef] = None
    Transitions: Optional[List[TransitionExtraOutputTypeDef]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class LifecycleRuleOutputTypeDef(BaseModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutputTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterOutputTypeDef] = None
    Transitions: Optional[List[TransitionOutputTypeDef]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class LifecycleRuleTypeDef(BaseModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterTypeDef] = None
    Transitions: Optional[Sequence[TransitionTypeDef]] = None
    NoncurrentVersionTransitions: Optional[Sequence[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class MetricsConfigurationOutputTypeDef(BaseModel):
    Id: str
    Filter: Optional[MetricsFilterOutputTypeDef] = None

class MetricsConfigurationTypeDef(BaseModel):
    Id: str
    Filter: Optional[MetricsFilterTypeDef] = None

class StorageClassAnalysisTypeDef(BaseModel):
    DataExport: Optional[StorageClassAnalysisDataExportTypeDef] = None

class LifecycleConfigurationTypeDef(BaseModel):
    Rules: Sequence[RuleTypeDef]

class GetObjectLockConfigurationOutputTypeDef(BaseModel):
    ObjectLockConfiguration: ObjectLockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectLockConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ObjectLockConfiguration: Optional[ObjectLockConfigurationTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Token: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class LambdaFunctionConfigurationExtraOutputTypeDef(BaseModel):
    LambdaFunctionArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterExtraOutputTypeDef] = None

class QueueConfigurationExtraOutputTypeDef(BaseModel):
    QueueArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterExtraOutputTypeDef] = None

class TopicConfigurationExtraOutputTypeDef(BaseModel):
    TopicArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterExtraOutputTypeDef] = None

class LambdaFunctionConfigurationOutputTypeDef(BaseModel):
    LambdaFunctionArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutputTypeDef] = None

class QueueConfigurationOutputTypeDef(BaseModel):
    QueueArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutputTypeDef] = None

class TopicConfigurationOutputTypeDef(BaseModel):
    TopicArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutputTypeDef] = None

class LambdaFunctionConfigurationTypeDef(BaseModel):
    LambdaFunctionArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterTypeDef] = None

class QueueConfigurationTypeDef(BaseModel):
    QueueArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterTypeDef] = None

class TopicConfigurationTypeDef(BaseModel):
    TopicArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterTypeDef] = None

class PutBucketAclRequestBucketAclPutTypeDef(BaseModel):
    ACL: Optional[BucketCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicyTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketAclRequestRequestTypeDef(BaseModel):
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

class PutObjectAclRequestObjectAclPutTypeDef(BaseModel):
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

class PutObjectAclRequestRequestTypeDef(BaseModel):
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

class OutputLocationTypeDef(BaseModel):
    S3: Optional[S3LocationTypeDef] = None

class InventoryDestinationOutputTypeDef(BaseModel):
    S3BucketDestination: InventoryS3BucketDestinationOutputTypeDef

class InventoryDestinationTypeDef(BaseModel):
    S3BucketDestination: InventoryS3BucketDestinationTypeDef

class ReplicationRuleOutputTypeDef(BaseModel):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilterOutputTypeDef] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteriaTypeDef] = None
    ExistingObjectReplication: Optional[ExistingObjectReplicationTypeDef] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplicationTypeDef] = None

class ReplicationRuleTypeDef(BaseModel):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilterTypeDef] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteriaTypeDef] = None
    ExistingObjectReplication: Optional[ExistingObjectReplicationTypeDef] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplicationTypeDef] = None

class GetBucketLoggingOutputTypeDef(BaseModel):
    LoggingEnabled: LoggingEnabledOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BucketLoggingStatusTypeDef(BaseModel):
    LoggingEnabled: Optional[LoggingEnabledTypeDef] = None

class PutBucketWebsiteRequestBucketWebsitePutTypeDef(BaseModel):
    WebsiteConfiguration: WebsiteConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketWebsiteRequestRequestTypeDef(BaseModel):
    Bucket: str
    WebsiteConfiguration: WebsiteConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class GetBucketEncryptionOutputTypeDef(BaseModel):
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketEncryptionRequestRequestTypeDef(BaseModel):
    Bucket: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class SelectObjectContentOutputTypeDef(BaseModel):
    Payload: "EventStream[SelectObjectContentEventStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketIntelligentTieringConfigurationOutputTypeDef(BaseModel):
    IntelligentTieringConfiguration: IntelligentTieringConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBucketIntelligentTieringConfigurationsOutputTypeDef(BaseModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    IntelligentTieringConfigurationList: List[IntelligentTieringConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketIntelligentTieringConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    IntelligentTieringConfiguration: IntelligentTieringConfigurationTypeDef

class GetBucketLifecycleConfigurationOutputTypeDef(BaseModel):
    Rules: List[LifecycleRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BucketLifecycleConfigurationTypeDef(BaseModel):
    Rules: Sequence[LifecycleRuleTypeDef]

class GetBucketMetricsConfigurationOutputTypeDef(BaseModel):
    MetricsConfiguration: MetricsConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBucketMetricsConfigurationsOutputTypeDef(BaseModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    MetricsConfigurationList: List[MetricsConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketMetricsConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    MetricsConfiguration: MetricsConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None

class AnalyticsConfigurationOutputTypeDef(BaseModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysisTypeDef
    Filter: Optional[AnalyticsFilterOutputTypeDef] = None

class AnalyticsConfigurationTypeDef(BaseModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysisTypeDef
    Filter: Optional[AnalyticsFilterTypeDef] = None

class PutBucketLifecycleRequestBucketLifecyclePutTypeDef(BaseModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLifecycleRequestRequestTypeDef(BaseModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class NotificationConfigurationResponseTypeDef(BaseModel):
    TopicConfigurations: List[TopicConfigurationOutputTypeDef]
    QueueConfigurations: List[QueueConfigurationOutputTypeDef]
    LambdaFunctionConfigurations: List[LambdaFunctionConfigurationOutputTypeDef]
    EventBridgeConfiguration: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class NotificationConfigurationTypeDef(BaseModel):
    TopicConfigurations: Optional[Sequence[TopicConfigurationTypeDef]] = None
    QueueConfigurations: Optional[Sequence[QueueConfigurationTypeDef]] = None
    LambdaFunctionConfigurations: Optional[Sequence[LambdaFunctionConfigurationTypeDef]] = None
    EventBridgeConfiguration: Optional[Mapping[str, Any]] = None

class RestoreRequestTypeDef(BaseModel):
    Days: Optional[int] = None
    GlacierJobParameters: Optional[GlacierJobParametersTypeDef] = None
    Type: Optional[Literal["SELECT"]] = None
    Tier: Optional[TierType] = None
    Description: Optional[str] = None
    SelectParameters: Optional[SelectParametersTypeDef] = None
    OutputLocation: Optional[OutputLocationTypeDef] = None

class InventoryConfigurationOutputTypeDef(BaseModel):
    Destination: InventoryDestinationOutputTypeDef
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersionsType
    Schedule: InventoryScheduleTypeDef
    Filter: Optional[InventoryFilterTypeDef] = None
    OptionalFields: Optional[List[InventoryOptionalFieldType]] = None

class InventoryConfigurationTypeDef(BaseModel):
    Destination: InventoryDestinationTypeDef
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersionsType
    Schedule: InventoryScheduleTypeDef
    Filter: Optional[InventoryFilterTypeDef] = None
    OptionalFields: Optional[Sequence[InventoryOptionalFieldType]] = None

class ReplicationConfigurationOutputTypeDef(BaseModel):
    Role: str
    Rules: List[ReplicationRuleOutputTypeDef]

class ReplicationConfigurationTypeDef(BaseModel):
    Role: str
    Rules: Sequence[ReplicationRuleTypeDef]

class PutBucketLoggingRequestBucketLoggingPutTypeDef(BaseModel):
    BucketLoggingStatus: BucketLoggingStatusTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLoggingRequestRequestTypeDef(BaseModel):
    Bucket: str
    BucketLoggingStatus: BucketLoggingStatusTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef(BaseModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLifecycleConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class GetBucketAnalyticsConfigurationOutputTypeDef(BaseModel):
    AnalyticsConfiguration: AnalyticsConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBucketAnalyticsConfigurationsOutputTypeDef(BaseModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    AnalyticsConfigurationList: List[AnalyticsConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketAnalyticsConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    AnalyticsConfiguration: AnalyticsConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None

class PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef(BaseModel):
    NotificationConfiguration: NotificationConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None

class PutBucketNotificationConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None

class RestoreObjectRequestObjectRestoreObjectTypeDef(BaseModel):
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequestTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class RestoreObjectRequestObjectSummaryRestoreObjectTypeDef(BaseModel):
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequestTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class RestoreObjectRequestRequestTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequestTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class GetBucketInventoryConfigurationOutputTypeDef(BaseModel):
    InventoryConfiguration: InventoryConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBucketInventoryConfigurationsOutputTypeDef(BaseModel):
    ContinuationToken: str
    InventoryConfigurationList: List[InventoryConfigurationOutputTypeDef]
    IsTruncated: bool
    NextContinuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketInventoryConfigurationRequestRequestTypeDef(BaseModel):
    Bucket: str
    Id: str
    InventoryConfiguration: InventoryConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None

class GetBucketReplicationOutputTypeDef(BaseModel):
    ReplicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketReplicationRequestRequestTypeDef(BaseModel):
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    Token: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

