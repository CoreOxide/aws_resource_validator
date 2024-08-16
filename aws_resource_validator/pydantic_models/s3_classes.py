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
from aws_resource_validator.pydantic_models.s3_constants import *

class AbortIncompleteMultipartUploadTypeDef(BaseValidatorModel):
    DaysAfterInitiation: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AbortMultipartUploadRequestMultipartUploadAbortTypeDef(BaseValidatorModel):
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class AbortMultipartUploadRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

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
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class BucketInfoTypeDef(BaseValidatorModel):
    DataRedundancy: Optional[Literal["SingleAvailabilityZone"]] = None
    Type: Optional[Literal["Directory"]] = None

class BucketTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None

class BucketUploadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class CORSRuleTypeDef(BaseValidatorModel):
    AllowedMethods: Sequence[str]
    AllowedOrigins: Sequence[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAgeSeconds: Optional[int] = None

class CORSRuleExtraOutputTypeDef(BaseValidatorModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAgeSeconds: Optional[int] = None

class CORSRuleOutputTypeDef(BaseValidatorModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class ClientDownloadFileRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientGeneratePresignedPostRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Fields: Optional[Optional[Dict[str, Any]]] = None
    Conditions: Optional[Union[List[Any], Dict[str, Any], None]] = None
    ExpiresIn: Optional[int] = None

class ClientUploadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    Bucket: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    PartNumber: Optional[int] = None

class ConditionTypeDef(BaseValidatorModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None

class CopyObjectResultTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class CopyPartResultTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class LocationInfoTypeDef(BaseValidatorModel):
    Type: Optional[Literal["AvailabilityZone"]] = None
    Name: Optional[str] = None

class SessionCredentialsTypeDef(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime

class CreateSessionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    SessionMode: Optional[SessionModeType] = None

class DefaultRetentionTypeDef(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    Days: Optional[int] = None
    Years: Optional[int] = None

class DeleteBucketAnalyticsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketCorsRequestBucketCorsDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketCorsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketEncryptionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str

class DeleteBucketInventoryConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketLifecycleRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketMetricsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketOwnershipControlsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketPolicyRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketReplicationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketRequestBucketDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketTaggingRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None

class DeleteBucketWebsiteRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class DeleteMarkerReplicationTypeDef(BaseValidatorModel):
    Status: Optional[DeleteMarkerReplicationStatusType] = None

class DeleteObjectRequestObjectDeleteTypeDef(BaseValidatorModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectRequestObjectSummaryDeleteTypeDef(BaseValidatorModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectRequestObjectVersionDeleteTypeDef(BaseValidatorModel):
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None

class DeleteObjectTaggingRequestRequestTypeDef(BaseValidatorModel):
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

class DeletePublicAccessBlockRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class ObjectIdentifierTypeDef(BaseValidatorModel):
    Key: str
    VersionId: Optional[str] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    ReplicaKmsKeyID: Optional[str] = None

class EncryptionTypeDef(BaseValidatorModel):
    EncryptionType: ServerSideEncryptionType
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None

class ErrorDocumentTypeDef(BaseValidatorModel):
    Key: str

class ExistingObjectReplicationTypeDef(BaseValidatorModel):
    Status: ExistingObjectReplicationStatusType

class FilterRuleTypeDef(BaseValidatorModel):
    Name: Optional[FilterRuleNameType] = None
    Value: Optional[str] = None

class GetBucketAccelerateConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class GetBucketAclRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketAnalyticsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketCorsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketEncryptionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketIntelligentTieringConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str

class GetBucketInventoryConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLifecycleConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLifecycleRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLocationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketLoggingRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketMetricsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketNotificationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketOwnershipControlsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketPolicyRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class PolicyStatusTypeDef(BaseValidatorModel):
    IsPublic: Optional[bool] = None

class GetBucketPolicyStatusRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketReplicationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketRequestPaymentRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketTaggingRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetBucketVersioningRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class IndexDocumentTypeDef(BaseValidatorModel):
    Suffix: str

class RedirectAllRequestsToTypeDef(BaseValidatorModel):
    HostName: str
    Protocol: Optional[ProtocolType] = None

class GetBucketWebsiteRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GetObjectAclRequestRequestTypeDef(BaseValidatorModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class GetObjectAttributesRequestRequestTypeDef(BaseValidatorModel):
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

class ObjectLockLegalHoldTypeDef(BaseValidatorModel):
    Status: Optional[ObjectLockLegalHoldStatusType] = None

class GetObjectLegalHoldRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class GetObjectLockConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class ObjectLockRetentionOutputTypeDef(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[datetime] = None

class GetObjectRetentionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class GetObjectTaggingRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class GetObjectTorrentRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None

class PublicAccessBlockConfigurationTypeDef(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None

class GetPublicAccessBlockRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class GlacierJobParametersTypeDef(BaseValidatorModel):
    Tier: TierType

class GranteeTypeDef(BaseValidatorModel):
    Type: TypeType
    DisplayName: Optional[str] = None
    EmailAddress: Optional[str] = None
    ID: Optional[str] = None
    URI: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class HeadBucketRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None

class InitiatorTypeDef(BaseValidatorModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None

class JSONInputTypeDef(BaseValidatorModel):
    Type: Optional[JSONTypeType] = None

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

class LifecycleExpirationExtraExtraOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class LifecycleExpirationExtraOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

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

class TransitionExtraOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class TransitionOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class ListBucketAnalyticsConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None

class ListBucketInventoryConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class ListBucketMetricsConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDirectoryBucketsRequestRequestTypeDef(BaseValidatorModel):
    ContinuationToken: Optional[str] = None
    MaxDirectoryBuckets: Optional[int] = None

class ListMultipartUploadsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    KeyMarker: Optional[str] = None
    MaxUploads: Optional[int] = None
    Prefix: Optional[str] = None
    UploadIdMarker: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None

class ListObjectVersionsRequestRequestTypeDef(BaseValidatorModel):
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

class ListObjectsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Marker: Optional[str] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None

class ListObjectsV2RequestRequestTypeDef(BaseValidatorModel):
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
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None

class ListPartsRequestRequestTypeDef(BaseValidatorModel):
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

class MetadataEntryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

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

class QueueConfigurationDeprecatedTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[Sequence[EventType]] = None
    Queue: Optional[str] = None

class TopicConfigurationDeprecatedTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Events: Optional[Sequence[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None

class ObjectDownloadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class RestoreStatusTypeDef(BaseValidatorModel):
    IsRestoreInProgress: Optional[bool] = None
    RestoreExpiryDate: Optional[datetime] = None

class ObjectUploadFileRequestTypeDef(BaseValidatorModel):
    Filename: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

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

class PutBucketPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class RecordsEventTypeDef(BaseValidatorModel):
    Payload: Optional[bytes] = None

class RedirectTypeDef(BaseValidatorModel):
    HostName: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[ProtocolType] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None

class ReplicaModificationsTypeDef(BaseValidatorModel):
    Status: ReplicaModificationsStatusType

class RequestProgressTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class TransitionExtraExtraOutputTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

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
    ChecksumSHA1: str
    ChecksumSHA256: str
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

class GetObjectTorrentOutputTypeDef(BaseValidatorModel):
    Body: StreamingBody
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class HeadBucketOutputTypeDef(BaseValidatorModel):
    BucketLocationType: Literal["AvailabilityZone"]
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
    ChecksumSHA1: str
    ChecksumSHA256: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketAccelerateConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class LifecycleRuleAndOperatorExtraOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None

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

class UploadPartRequestMultipartUploadPartUploadTypeDef(BaseValidatorModel):
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

class UploadPartRequestRequestTypeDef(BaseValidatorModel):
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

class BucketCopyRequestTypeDef(BaseValidatorModel):
    CopySource: CopySourceTypeDef
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    SourceClient: Optional[Optional[BaseClient]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientCopyRequestTypeDef(BaseValidatorModel):
    CopySource: CopySourceTypeDef
    Bucket: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    SourceClient: Optional[Optional[BaseClient]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ObjectCopyRequestTypeDef(BaseValidatorModel):
    CopySource: CopySourceTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    SourceClient: Optional[Optional[BaseClient]] = None
    Config: Optional[Optional[TransferConfig]] = None

class BucketDownloadFileobjRequestTypeDef(BaseValidatorModel):
    Key: str
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class BucketUploadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientDownloadFileobjRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ClientUploadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    Bucket: str
    Key: str
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ObjectDownloadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ObjectUploadFileobjRequestTypeDef(BaseValidatorModel):
    Fileobj: FileobjTypeDef
    ExtraArgs: Optional[Optional[Dict[str, Any]]] = None
    Callback: Optional[Optional[Callable[..., Any]]] = None
    Config: Optional[Optional[TransferConfig]] = None

class ListBucketsOutputTypeDef(BaseValidatorModel):
    Buckets: List[BucketTypeDef]
    Owner: OwnerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDirectoryBucketsOutputTypeDef(BaseValidatorModel):
    Buckets: List[BucketTypeDef]
    ContinuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CORSConfigurationTypeDef(BaseValidatorModel):
    CORSRules: Sequence[CORSRuleTypeDef]

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

class CopyObjectRequestObjectCopyFromTypeDef(BaseValidatorModel):
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

class CopyObjectRequestObjectSummaryCopyFromTypeDef(BaseValidatorModel):
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

class CreateMultipartUploadRequestRequestTypeDef(BaseValidatorModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class GetObjectRequestRequestTypeDef(BaseValidatorModel):
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
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal["ENABLED"]] = None

class HeadObjectRequestRequestTypeDef(BaseValidatorModel):
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

class LifecycleExpirationTypeDef(BaseValidatorModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None

class ObjectLockRetentionTypeDef(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[TimestampTypeDef] = None

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

class PutObjectRequestRequestTypeDef(BaseValidatorModel):
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

class TransitionTypeDef(BaseValidatorModel):
    Date: Optional[TimestampTypeDef] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None

class WriteGetObjectResponseRequestRequestTypeDef(BaseValidatorModel):
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

class CreateBucketConfigurationTypeDef(BaseValidatorModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None
    Location: Optional[LocationInfoTypeDef] = None
    Bucket: Optional[BucketInfoTypeDef] = None

class CreateSessionOutputTypeDef(BaseValidatorModel):
    Credentials: SessionCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ObjectLockRuleTypeDef(BaseValidatorModel):
    DefaultRetention: Optional[DefaultRetentionTypeDef] = None

class DeleteObjectsOutputTypeDef(BaseValidatorModel):
    Deleted: List[DeletedObjectTypeDef]
    RequestCharged: Literal["requester"]
    Errors: List[ErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTypeDef(BaseValidatorModel):
    Objects: Sequence[ObjectIdentifierTypeDef]
    Quiet: Optional[bool] = None

class S3KeyFilterExtraOutputTypeDef(BaseValidatorModel):
    FilterRules: Optional[List[FilterRuleTypeDef]] = None

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

class PutObjectLegalHoldRequestRequestTypeDef(BaseValidatorModel):
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

class PutPublicAccessBlockRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class GrantTypeDef(BaseValidatorModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None

class TargetGrantTypeDef(BaseValidatorModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[BucketLogsPermissionType] = None

class HeadBucketRequestBucketExistsWaitTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class HeadBucketRequestBucketNotExistsWaitTypeDef(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class HeadObjectRequestObjectExistsWaitTypeDef(BaseValidatorModel):
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

class HeadObjectRequestObjectNotExistsWaitTypeDef(BaseValidatorModel):
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

class MultipartUploadTypeDef(BaseValidatorModel):
    UploadId: Optional[str] = None
    Key: Optional[str] = None
    Initiated: Optional[datetime] = None
    StorageClass: Optional[StorageClassType] = None
    Owner: Optional[OwnerTypeDef] = None
    Initiator: Optional[InitiatorTypeDef] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

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

class ListDirectoryBucketsRequestListDirectoryBucketsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartUploadsRequestListMultipartUploadsPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectVersionsRequestListObjectVersionsPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectsRequestListObjectsPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal["url"]] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[Sequence[Literal["RestoreStatus"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectsV2RequestListObjectsV2PaginateTypeDef(BaseValidatorModel):
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

class ListPartsRequestListPartsPaginateTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal["requester"]] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[str] = None
    SSECustomerKeyMD5: Optional[str] = None
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
    ResponseMetadata: ResponseMetadataTypeDef

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

class NotificationConfigurationDeprecatedTypeDef(BaseValidatorModel):
    TopicConfiguration: Optional[TopicConfigurationDeprecatedTypeDef] = None
    QueueConfiguration: Optional[QueueConfigurationDeprecatedTypeDef] = None
    CloudFunctionConfiguration: Optional[CloudFunctionConfigurationTypeDef] = None

class ObjectTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    Size: Optional[int] = None
    StorageClass: Optional[ObjectStorageClassType] = None
    Owner: Optional[OwnerTypeDef] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None

class ObjectVersionTypeDef(BaseValidatorModel):
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

class OwnershipControlsOutputTypeDef(BaseValidatorModel):
    Rules: List[OwnershipControlsRuleTypeDef]

class OwnershipControlsTypeDef(BaseValidatorModel):
    Rules: Sequence[OwnershipControlsRuleTypeDef]

class TargetObjectKeyFormatExtraOutputTypeDef(BaseValidatorModel):
    SimplePrefix: Optional[Dict[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefixTypeDef] = None

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

class PutBucketRequestPaymentRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketVersioningRequestBucketVersioningPutTypeDef(BaseValidatorModel):
    VersioningConfiguration: VersioningConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketVersioningRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    VersioningConfiguration: VersioningConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class RoutingRuleTypeDef(BaseValidatorModel):
    Redirect: RedirectTypeDef
    Condition: Optional[ConditionTypeDef] = None

class RuleExtraOutputTypeDef(BaseValidatorModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationExtraExtraOutputTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionExtraExtraOutputTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class ServerSideEncryptionRuleTypeDef(BaseValidatorModel):
    ApplyServerSideEncryptionByDefault: Optional[ServerSideEncryptionByDefaultTypeDef] = None
    BucketKeyEnabled: Optional[bool] = None

class SourceSelectionCriteriaTypeDef(BaseValidatorModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjectsTypeDef] = None
    ReplicaModifications: Optional[ReplicaModificationsTypeDef] = None

class StatsEventTypeDef(BaseValidatorModel):
    Details: Optional[StatsTypeDef] = None

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

class LifecycleRuleFilterExtraOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorExtraOutputTypeDef] = None

class LifecycleRuleFilterOutputTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorOutputTypeDef] = None

class LifecycleRuleFilterTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[TagTypeDef] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorTypeDef] = None

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

class PutBucketTaggingRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Tagging: TaggingTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutObjectTaggingRequestRequestTypeDef(BaseValidatorModel):
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

class CopyObjectRequestRequestTypeDef(BaseValidatorModel):
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

class UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef(BaseValidatorModel):
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

class UploadPartCopyRequestRequestTypeDef(BaseValidatorModel):
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

class PutBucketCorsRequestBucketCorsPutTypeDef(BaseValidatorModel):
    CORSConfiguration: CORSConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketCorsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    CORSConfiguration: CORSConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef(BaseValidatorModel):
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

class CompleteMultipartUploadRequestRequestTypeDef(BaseValidatorModel):
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

class PutObjectRetentionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    Retention: Optional[ObjectLockRetentionTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    BypassGovernanceRetention: Optional[bool] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class RuleTypeDef(BaseValidatorModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationTypeDef] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionTypeDef] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransitionTypeDef] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

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

class CreateBucketRequestRequestTypeDef(BaseValidatorModel):
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

class ObjectLockConfigurationTypeDef(BaseValidatorModel):
    ObjectLockEnabled: Optional[Literal["Enabled"]] = None
    Rule: Optional[ObjectLockRuleTypeDef] = None

class DeleteObjectsRequestBucketDeleteObjectsTypeDef(BaseValidatorModel):
    Delete: DeleteTypeDef
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

class DeleteObjectsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Delete: DeleteTypeDef
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None

class NotificationConfigurationFilterExtraOutputTypeDef(BaseValidatorModel):
    Key: Optional[S3KeyFilterExtraOutputTypeDef] = None

class NotificationConfigurationFilterOutputTypeDef(BaseValidatorModel):
    Key: Optional[S3KeyFilterOutputTypeDef] = None

class NotificationConfigurationFilterTypeDef(BaseValidatorModel):
    Key: Optional[S3KeyFilterTypeDef] = None

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

class SelectObjectContentRequestRequestTypeDef(BaseValidatorModel):
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

class SelectParametersTypeDef(BaseValidatorModel):
    InputSerialization: InputSerializationTypeDef
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: OutputSerializationTypeDef

class GetBucketLifecycleOutputTypeDef(BaseValidatorModel):
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationTypeDef(BaseValidatorModel):
    Bucket: str
    Account: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    AccessControlTranslation: Optional[AccessControlTranslationTypeDef] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    ReplicationTime: Optional[ReplicationTimeTypeDef] = None
    Metrics: Optional[MetricsTypeDef] = None

class PutBucketNotificationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationDeprecatedTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

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

class PutBucketOwnershipControlsRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    OwnershipControls: OwnershipControlsTypeDef
    ContentMD5: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class LoggingEnabledExtraOutputTypeDef(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatExtraOutputTypeDef] = None

class LoggingEnabledOutputTypeDef(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatOutputTypeDef] = None

class LoggingEnabledTypeDef(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[Sequence[TargetGrantTypeDef]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatTypeDef] = None

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

class LifecycleRuleExtraOutputTypeDef(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationExtraOutputTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterExtraOutputTypeDef] = None
    Transitions: Optional[List[TransitionExtraOutputTypeDef]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

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

class LifecycleRuleTypeDef(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationTypeDef] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterTypeDef] = None
    Transitions: Optional[Sequence[TransitionTypeDef]] = None
    NoncurrentVersionTransitions: Optional[Sequence[NoncurrentVersionTransitionTypeDef]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpirationTypeDef] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUploadTypeDef] = None

class MetricsConfigurationOutputTypeDef(BaseValidatorModel):
    Id: str
    Filter: Optional[MetricsFilterOutputTypeDef] = None

class MetricsConfigurationTypeDef(BaseValidatorModel):
    Id: str
    Filter: Optional[MetricsFilterTypeDef] = None

class StorageClassAnalysisTypeDef(BaseValidatorModel):
    DataExport: Optional[StorageClassAnalysisDataExportTypeDef] = None

class LifecycleConfigurationTypeDef(BaseValidatorModel):
    Rules: Sequence[RuleTypeDef]

class GetObjectLockConfigurationOutputTypeDef(BaseValidatorModel):
    ObjectLockConfiguration: ObjectLockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectLockConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ObjectLockConfiguration: Optional[ObjectLockConfigurationTypeDef] = None
    RequestPayer: Optional[Literal["requester"]] = None
    Token: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class LambdaFunctionConfigurationExtraOutputTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterExtraOutputTypeDef] = None

class QueueConfigurationExtraOutputTypeDef(BaseValidatorModel):
    QueueArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterExtraOutputTypeDef] = None

class TopicConfigurationExtraOutputTypeDef(BaseValidatorModel):
    TopicArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterExtraOutputTypeDef] = None

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

class LambdaFunctionConfigurationTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterTypeDef] = None

class QueueConfigurationTypeDef(BaseValidatorModel):
    QueueArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterTypeDef] = None

class TopicConfigurationTypeDef(BaseValidatorModel):
    TopicArn: str
    Events: Sequence[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterTypeDef] = None

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

class PutBucketAclRequestRequestTypeDef(BaseValidatorModel):
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
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    RequestPayer: Optional[Literal["requester"]] = None
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

class PutObjectAclRequestRequestTypeDef(BaseValidatorModel):
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

class GetBucketLoggingOutputTypeDef(BaseValidatorModel):
    LoggingEnabled: LoggingEnabledOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BucketLoggingStatusTypeDef(BaseValidatorModel):
    LoggingEnabled: Optional[LoggingEnabledTypeDef] = None

class PutBucketWebsiteRequestBucketWebsitePutTypeDef(BaseValidatorModel):
    WebsiteConfiguration: WebsiteConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketWebsiteRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    WebsiteConfiguration: WebsiteConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class GetBucketEncryptionOutputTypeDef(BaseValidatorModel):
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketEncryptionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class SelectObjectContentOutputTypeDef(BaseValidatorModel):
    Payload: "EventStream[SelectObjectContentEventStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketIntelligentTieringConfigurationOutputTypeDef(BaseValidatorModel):
    IntelligentTieringConfiguration: IntelligentTieringConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBucketIntelligentTieringConfigurationsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    IntelligentTieringConfigurationList: List[IntelligentTieringConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketIntelligentTieringConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    IntelligentTieringConfiguration: IntelligentTieringConfigurationTypeDef

class GetBucketLifecycleConfigurationOutputTypeDef(BaseValidatorModel):
    Rules: List[LifecycleRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BucketLifecycleConfigurationTypeDef(BaseValidatorModel):
    Rules: Sequence[LifecycleRuleTypeDef]

class GetBucketMetricsConfigurationOutputTypeDef(BaseValidatorModel):
    MetricsConfiguration: MetricsConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBucketMetricsConfigurationsOutputTypeDef(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    MetricsConfigurationList: List[MetricsConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketMetricsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    MetricsConfiguration: MetricsConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None

class AnalyticsConfigurationOutputTypeDef(BaseValidatorModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysisTypeDef
    Filter: Optional[AnalyticsFilterOutputTypeDef] = None

class AnalyticsConfigurationTypeDef(BaseValidatorModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysisTypeDef
    Filter: Optional[AnalyticsFilterTypeDef] = None

class PutBucketLifecycleRequestBucketLifecyclePutTypeDef(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLifecycleRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class NotificationConfigurationResponseTypeDef(BaseValidatorModel):
    TopicConfigurations: List[TopicConfigurationOutputTypeDef]
    QueueConfigurations: List[QueueConfigurationOutputTypeDef]
    LambdaFunctionConfigurations: List[LambdaFunctionConfigurationOutputTypeDef]
    EventBridgeConfiguration: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class NotificationConfigurationTypeDef(BaseValidatorModel):
    TopicConfigurations: Optional[Sequence[TopicConfigurationTypeDef]] = None
    QueueConfigurations: Optional[Sequence[QueueConfigurationTypeDef]] = None
    LambdaFunctionConfigurations: Optional[Sequence[LambdaFunctionConfigurationTypeDef]] = None
    EventBridgeConfiguration: Optional[Mapping[str, Any]] = None

class RestoreRequestTypeDef(BaseValidatorModel):
    Days: Optional[int] = None
    GlacierJobParameters: Optional[GlacierJobParametersTypeDef] = None
    Type: Optional[Literal["SELECT"]] = None
    Tier: Optional[TierType] = None
    Description: Optional[str] = None
    SelectParameters: Optional[SelectParametersTypeDef] = None
    OutputLocation: Optional[OutputLocationTypeDef] = None

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

class PutBucketLoggingRequestBucketLoggingPutTypeDef(BaseValidatorModel):
    BucketLoggingStatus: BucketLoggingStatusTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLoggingRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    BucketLoggingStatus: BucketLoggingStatusTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None

class PutBucketLifecycleConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfigurationTypeDef] = None
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

class PutBucketAnalyticsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    AnalyticsConfiguration: AnalyticsConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None

class PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef(BaseValidatorModel):
    NotificationConfiguration: NotificationConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None

class PutBucketNotificationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None

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

class RestoreObjectRequestRequestTypeDef(BaseValidatorModel):
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

class PutBucketInventoryConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    Id: str
    InventoryConfiguration: InventoryConfigurationTypeDef
    ExpectedBucketOwner: Optional[str] = None

class GetBucketReplicationOutputTypeDef(BaseValidatorModel):
    ReplicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBucketReplicationRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationTypeDef
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    Token: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

