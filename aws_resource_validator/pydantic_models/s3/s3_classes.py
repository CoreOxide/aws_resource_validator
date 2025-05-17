from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union, Callable
from datetime import datetime

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.s3.s3_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbortIncompleteMultipartUpload(BaseValidatorModel):
    DaysAfterInitiation: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class AccelerateConfiguration(BaseValidatorModel):
    Status: Optional[BucketAccelerateStatusType] = None


class Owner(BaseValidatorModel):
    DisplayName: Optional[str] = None
    ID: Optional[str] = None


class AccessControlTranslation(BaseValidatorModel):
    Owner: Literal['Destination']


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AnalyticsS3BucketDestination(BaseValidatorModel):
    Format: Literal['CSV']
    Bucket: str
    BucketAccountId: Optional[str] = None
    Prefix: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CopySource(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None


class BucketDownloadFileRequest(BaseValidatorModel):
    Key: str
    Filename: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None

Fileobj = Union[IO[Any], StreamingBody]


class BucketInfo(BaseValidatorModel):
    DataRedundancy: Optional[DataRedundancyType] = None
    Type: Optional[Literal['Directory']] = None


class Bucket(BaseValidatorModel):
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None
    BucketRegion: Optional[str] = None


class BucketUploadFileRequest(BaseValidatorModel):
    Filename: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class CORSRuleOutput(BaseValidatorModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAgeSeconds: Optional[int] = None


class CORSRule(BaseValidatorModel):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]
    ID: Optional[str] = None
    AllowedHeaders: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAgeSeconds: Optional[int] = None


class CSVInput(BaseValidatorModel):
    FileHeaderInfo: Optional[FileHeaderInfoType] = None
    Comments: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None
    AllowQuotedRecordDelimiter: Optional[bool] = None


class CSVOutput(BaseValidatorModel):
    QuoteFields: Optional[QuoteFieldsType] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None


class Checksum(BaseValidatorModel):
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class ClientDownloadFileRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    Filename: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class ClientGeneratePresignedPostRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    Fields: Optional[Dict[str, Any]] = None
    Conditions: Optional[Union[Any], Dict[str, List[Any]]] = None
    ExpiresIn: Optional[int] = None


class ClientUploadFileRequest(BaseValidatorModel):
    Filename: str
    Bucket: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class CloudFunctionConfigurationOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    CloudFunction: Optional[str] = None
    InvocationRole: Optional[str] = None


class CloudFunctionConfiguration(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    CloudFunction: Optional[str] = None
    InvocationRole: Optional[str] = None


class CommonPrefix(BaseValidatorModel):
    Prefix: Optional[str] = None


class CompletedPart(BaseValidatorModel):
    ETag: Optional[str] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    PartNumber: Optional[int] = None


class Condition(BaseValidatorModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None


class CopyObjectResult(BaseValidatorModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


class CopyPartResult(BaseValidatorModel):
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


class LocationInfo(BaseValidatorModel):
    Type: Optional[LocationTypeType] = None
    Name: Optional[str] = None


class SessionCredentials(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime


# This class is the input for the 'create_session' function.
class CreateSessionRequest(BaseValidatorModel):
    Bucket: str
    SessionMode: Optional[SessionModeType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None


class DefaultRetention(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    Days: Optional[int] = None
    Years: Optional[int] = None


# This class is the input for the 'delete_bucket_analytics_configuration' function.
class DeleteBucketAnalyticsConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketCorsRequestBucketCorsDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_cors' function.
class DeleteBucketCorsRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_encryption' function.
class DeleteBucketEncryptionRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_intelligent_tiering_configuration' function.
class DeleteBucketIntelligentTieringConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str


# This class is the input for the 'delete_bucket_inventory_configuration' function.
class DeleteBucketInventoryConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketLifecycleRequestBucketLifecycleConfigurationDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketLifecycleRequestBucketLifecycleDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_lifecycle' function.
class DeleteBucketLifecycleRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_metadata_table_configuration' function.
class DeleteBucketMetadataTableConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_metrics_configuration' function.
class DeleteBucketMetricsConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_ownership_controls' function.
class DeleteBucketOwnershipControlsRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketPolicyRequestBucketPolicyDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_policy' function.
class DeleteBucketPolicyRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_replication' function.
class DeleteBucketReplicationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketRequestBucketDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket' function.
class DeleteBucketRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketTaggingRequestBucketTaggingDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_tagging' function.
class DeleteBucketTaggingRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteBucketWebsiteRequestBucketWebsiteDelete(BaseValidatorModel):
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'delete_bucket_website' function.
class DeleteBucketWebsiteRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class DeleteMarkerReplication(BaseValidatorModel):
    Status: Optional[DeleteMarkerReplicationStatusType] = None


# This class is the input for the 'delete_object_tagging' function.
class DeleteObjectTaggingRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class DeletedObject(BaseValidatorModel):
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    DeleteMarker: Optional[bool] = None
    DeleteMarkerVersionId: Optional[str] = None


class Error(BaseValidatorModel):
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Code: Optional[str] = None
    Message: Optional[str] = None


# This class is the input for the 'delete_public_access_block' function.
class DeletePublicAccessBlockRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class EncryptionConfiguration(BaseValidatorModel):
    ReplicaKmsKeyID: Optional[str] = None


class Encryption(BaseValidatorModel):
    EncryptionType: ServerSideEncryptionType
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None


class ErrorDetails(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ErrorDocument(BaseValidatorModel):
    Key: str


class ExistingObjectReplication(BaseValidatorModel):
    Status: ExistingObjectReplicationStatusType


class FilterRule(BaseValidatorModel):
    Name: Optional[FilterRuleNameType] = None
    Value: Optional[str] = None


# This class is the input for the 'get_bucket_accelerate_configuration' function.
class GetBucketAccelerateConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None


# This class is the input for the 'get_bucket_acl' function.
class GetBucketAclRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_analytics_configuration' function.
class GetBucketAnalyticsConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_cors' function.
class GetBucketCorsRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_encryption' function.
class GetBucketEncryptionRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_intelligent_tiering_configuration' function.
class GetBucketIntelligentTieringConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str


# This class is the input for the 'get_bucket_inventory_configuration' function.
class GetBucketInventoryConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_lifecycle_configuration' function.
class GetBucketLifecycleConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_lifecycle' function.
class GetBucketLifecycleRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_location' function.
class GetBucketLocationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_logging' function.
class GetBucketLoggingRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_metadata_table_configuration' function.
class GetBucketMetadataTableConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_metrics_configuration' function.
class GetBucketMetricsConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_notification_configuration' function.
class GetBucketNotificationConfigurationRequestRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_notification' function.
class GetBucketNotificationConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_ownership_controls' function.
class GetBucketOwnershipControlsRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_policy' function.
class GetBucketPolicyRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class PolicyStatus(BaseValidatorModel):
    IsPublic: Optional[bool] = None


# This class is the input for the 'get_bucket_policy_status' function.
class GetBucketPolicyStatusRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_replication' function.
class GetBucketReplicationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_request_payment' function.
class GetBucketRequestPaymentRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_tagging' function.
class GetBucketTaggingRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_bucket_versioning' function.
class GetBucketVersioningRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class IndexDocument(BaseValidatorModel):
    Suffix: str


class RedirectAllRequestsTo(BaseValidatorModel):
    HostName: str
    Protocol: Optional[ProtocolType] = None


# This class is the input for the 'get_bucket_website' function.
class GetBucketWebsiteRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_object_acl' function.
class GetObjectAclRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


class ObjectPart(BaseValidatorModel):
    PartNumber: Optional[int] = None
    Size: Optional[int] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


# This class is the input for the 'get_object_attributes' function.
class GetObjectAttributesRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    ObjectAttributes: List[ObjectAttributesType]
    VersionId: Optional[str] = None
    MaxParts: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


class ObjectLockLegalHold(BaseValidatorModel):
    Status: Optional[ObjectLockLegalHoldStatusType] = None


# This class is the input for the 'get_object_legal_hold' function.
class GetObjectLegalHoldRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_object_lock_configuration' function.
class GetObjectLockConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class ObjectLockRetentionOutput(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[datetime] = None


# This class is the input for the 'get_object_retention' function.
class GetObjectRetentionRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'get_object_tagging' function.
class GetObjectTaggingRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None


# This class is the input for the 'get_object_torrent' function.
class GetObjectTorrentRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


class PublicAccessBlockConfiguration(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None


# This class is the input for the 'get_public_access_block' function.
class GetPublicAccessBlockRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class GlacierJobParameters(BaseValidatorModel):
    Tier: TierType


class Grantee(BaseValidatorModel):
    Type: TypeType
    DisplayName: Optional[str] = None
    EmailAddress: Optional[str] = None
    ID: Optional[str] = None
    URI: Optional[str] = None


# This class is the input for the 'head_bucket' function.
class HeadBucketRequest(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class Initiator(BaseValidatorModel):
    ID: Optional[str] = None
    DisplayName: Optional[str] = None


class JSONInput(BaseValidatorModel):
    Type: Optional[JSONTypeType] = None


class Tiering(BaseValidatorModel):
    Days: int
    AccessTier: IntelligentTieringAccessTierType


class InventoryFilter(BaseValidatorModel):
    Prefix: str


class InventorySchedule(BaseValidatorModel):
    Frequency: InventoryFrequencyType


class SSEKMS(BaseValidatorModel):
    KeyId: str


class JSONOutput(BaseValidatorModel):
    RecordDelimiter: Optional[str] = None


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
    NewerNoncurrentVersions: Optional[int] = None


class TransitionOutput(BaseValidatorModel):
    Date: Optional[datetime] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


# This class is the input for the 'list_bucket_analytics_configurations' function.
class ListBucketAnalyticsConfigurationsRequest(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'list_bucket_intelligent_tiering_configurations' function.
class ListBucketIntelligentTieringConfigurationsRequest(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None


# This class is the input for the 'list_bucket_inventory_configurations' function.
class ListBucketInventoryConfigurationsRequest(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'list_bucket_metrics_configurations' function.
class ListBucketMetricsConfigurationsRequest(BaseValidatorModel):
    Bucket: str
    ContinuationToken: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_buckets' function.
class ListBucketsRequest(BaseValidatorModel):
    MaxBuckets: Optional[int] = None
    ContinuationToken: Optional[str] = None
    Prefix: Optional[str] = None
    BucketRegion: Optional[str] = None


# This class is the input for the 'list_directory_buckets' function.
class ListDirectoryBucketsRequest(BaseValidatorModel):
    ContinuationToken: Optional[str] = None
    MaxDirectoryBuckets: Optional[int] = None


# This class is the input for the 'list_multipart_uploads' function.
class ListMultipartUploadsRequest(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    KeyMarker: Optional[str] = None
    MaxUploads: Optional[int] = None
    Prefix: Optional[str] = None
    UploadIdMarker: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None


# This class is the input for the 'list_object_versions' function.
class ListObjectVersionsRequest(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    KeyMarker: Optional[str] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    VersionIdMarker: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    OptionalObjectAttributes: Optional[List[Literal['RestoreStatus']]] = None


# This class is the input for the 'list_objects' function.
class ListObjectsRequest(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    Marker: Optional[str] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[List[Literal['RestoreStatus']]] = None


# This class is the input for the 'list_objects_v2' function.
class ListObjectsV2Request(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    MaxKeys: Optional[int] = None
    Prefix: Optional[str] = None
    ContinuationToken: Optional[str] = None
    FetchOwner: Optional[bool] = None
    StartAfter: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[List[Literal['RestoreStatus']]] = None


class Part(BaseValidatorModel):
    PartNumber: Optional[int] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None


# This class is the input for the 'list_parts' function.
class ListPartsRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    MaxParts: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None


class MetadataEntry(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class S3TablesDestinationResult(BaseValidatorModel):
    TableBucketArn: str
    TableName: str
    TableArn: str
    TableNamespace: str


class S3TablesDestination(BaseValidatorModel):
    TableBucketArn: str
    TableName: str


class ReplicationTimeValue(BaseValidatorModel):
    Minutes: Optional[int] = None


class QueueConfigurationDeprecatedOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    Queue: Optional[str] = None


class TopicConfigurationDeprecatedOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Events: Optional[List[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None


class ObjectDownloadFileRequest(BaseValidatorModel):
    Filename: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class RestoreStatus(BaseValidatorModel):
    IsRestoreInProgress: Optional[bool] = None
    RestoreExpiryDate: Optional[datetime] = None


class ObjectUploadFileRequest(BaseValidatorModel):
    Filename: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class OwnershipControlsRule(BaseValidatorModel):
    ObjectOwnership: ObjectOwnershipType


class PartitionedPrefix(BaseValidatorModel):
    PartitionDateSource: Optional[PartitionDateSourceType] = None


class Progress(BaseValidatorModel):
    BytesScanned: Optional[int] = None
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None


class PutBucketPolicyRequestBucketPolicyPut(BaseValidatorModel):
    Policy: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_policy' function.
class PutBucketPolicyRequest(BaseValidatorModel):
    Bucket: str
    Policy: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ConfirmRemoveSelfBucketAccess: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None


class RequestPaymentConfiguration(BaseValidatorModel):
    Payer: PayerType


class PutBucketVersioningRequestBucketVersioningEnable(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class VersioningConfiguration(BaseValidatorModel):
    MFADelete: Optional[MFADeleteType] = None
    Status: Optional[BucketVersioningStatusType] = None


class PutBucketVersioningRequestBucketVersioningSuspend(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class QueueConfigurationDeprecated(BaseValidatorModel):
    Id: Optional[str] = None
    Event: Optional[EventType] = None
    Events: Optional[List[EventType]] = None
    Queue: Optional[str] = None


class RecordsEvent(BaseValidatorModel):
    Payload: Optional[bytes] = None


class Redirect(BaseValidatorModel):
    HostName: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[ProtocolType] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None


class ReplicaModifications(BaseValidatorModel):
    Status: ReplicaModificationsStatusType


class RequestProgress(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ScanRange(BaseValidatorModel):
    Start: Optional[int] = None
    End: Optional[int] = None


class ServerSideEncryptionByDefault(BaseValidatorModel):
    SSEAlgorithm: ServerSideEncryptionType
    KMSMasterKeyID: Optional[str] = None


class SseKmsEncryptedObjects(BaseValidatorModel):
    Status: SseKmsEncryptedObjectsStatusType


class Stats(BaseValidatorModel):
    BytesScanned: Optional[int] = None
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None


class TopicConfigurationDeprecated(BaseValidatorModel):
    Id: Optional[str] = None
    Events: Optional[List[EventType]] = None
    Event: Optional[EventType] = None
    Topic: Optional[str] = None


# This class is the output for the 'abort_multipart_upload' function.
class AbortMultipartUploadOutput(BaseValidatorModel):
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'complete_multipart_upload' function.
class CompleteMultipartUploadOutput(BaseValidatorModel):
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
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_bucket' function.
class CreateBucketOutput(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_multipart_upload' function.
class CreateMultipartUploadOutput(BaseValidatorModel):
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
    RequestCharged: Literal['requester']
    ChecksumAlgorithm: ChecksumAlgorithmType
    ChecksumType: ChecksumTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_object' function.
class DeleteObjectOutput(BaseValidatorModel):
    DeleteMarker: bool
    VersionId: str
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_object_tagging' function.
class DeleteObjectTaggingOutput(BaseValidatorModel):
    VersionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'write_get_object_response' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bucket_accelerate_configuration' function.
class GetBucketAccelerateConfigurationOutput(BaseValidatorModel):
    Status: BucketAccelerateStatusType
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bucket_location' function.
class GetBucketLocationOutput(BaseValidatorModel):
    LocationConstraint: BucketLocationConstraintType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bucket_policy' function.
class GetBucketPolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bucket_request_payment' function.
class GetBucketRequestPaymentOutput(BaseValidatorModel):
    Payer: PayerType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bucket_versioning' function.
class GetBucketVersioningOutput(BaseValidatorModel):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object' function.
class GetObjectOutput(BaseValidatorModel):
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
    RequestCharged: Literal['requester']
    ReplicationStatus: ReplicationStatusType
    PartsCount: int
    TagCount: int
    ObjectLockMode: ObjectLockModeType
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object_torrent' function.
class GetObjectTorrentOutput(BaseValidatorModel):
    Body: StreamingBody
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'head_bucket' function.
class HeadBucketOutput(BaseValidatorModel):
    BucketLocationType: LocationTypeType
    BucketLocationName: str
    BucketRegion: str
    AccessPointAlias: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'head_object' function.
class HeadObjectOutput(BaseValidatorModel):
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
    RequestCharged: Literal['requester']
    ReplicationStatus: ReplicationStatusType
    PartsCount: int
    ObjectLockMode: ObjectLockModeType
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_bucket_lifecycle_configuration' function.
class PutBucketLifecycleConfigurationOutput(BaseValidatorModel):
    TransitionDefaultMinimumObjectSize: TransitionDefaultMinimumObjectSizeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_object_acl' function.
class PutObjectAclOutput(BaseValidatorModel):
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_object_legal_hold' function.
class PutObjectLegalHoldOutput(BaseValidatorModel):
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_object_lock_configuration' function.
class PutObjectLockConfigurationOutput(BaseValidatorModel):
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_object' function.
class PutObjectOutput(BaseValidatorModel):
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
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_object_retention' function.
class PutObjectRetentionOutput(BaseValidatorModel):
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_object_tagging' function.
class PutObjectTaggingOutput(BaseValidatorModel):
    VersionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_object' function.
class RestoreObjectOutput(BaseValidatorModel):
    RequestCharged: Literal['requester']
    RestoreOutputPath: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upload_part' function.
class UploadPartOutput(BaseValidatorModel):
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
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


class AbortMultipartUploadRequestMultipartUploadAbort(BaseValidatorModel):
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatchInitiatedTime: Optional[Timestamp] = None


# This class is the input for the 'abort_multipart_upload' function.
class AbortMultipartUploadRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatchInitiatedTime: Optional[Timestamp] = None


class CreateMultipartUploadRequestObjectInitiateMultipartUpload(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    Expires: Optional[Timestamp] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class CreateMultipartUploadRequestObjectSummaryInitiateMultipartUpload(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    Expires: Optional[Timestamp] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


# This class is the input for the 'create_multipart_upload' function.
class CreateMultipartUploadRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    Expires: Optional[Timestamp] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class DeleteObjectRequestObjectDelete(BaseValidatorModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[Timestamp] = None
    IfMatchSize: Optional[int] = None


class DeleteObjectRequestObjectSummaryDelete(BaseValidatorModel):
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[Timestamp] = None
    IfMatchSize: Optional[int] = None


class DeleteObjectRequestObjectVersionDelete(BaseValidatorModel):
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[Timestamp] = None
    IfMatchSize: Optional[int] = None


# This class is the input for the 'delete_object' function.
class DeleteObjectRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    MFA: Optional[str] = None
    VersionId: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfMatchLastModifiedTime: Optional[Timestamp] = None
    IfMatchSize: Optional[int] = None


class GetObjectRequestObjectGet(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None


class GetObjectRequestObjectSummaryGet(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None


class GetObjectRequestObjectVersionGet(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None


# This class is the input for the 'get_object' function.
class GetObjectRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None


class HeadObjectRequestObjectVersionHead(BaseValidatorModel):
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None


# This class is the input for the 'head_object' function.
class HeadObjectRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None


class LifecycleExpiration(BaseValidatorModel):
    Date: Optional[Timestamp] = None
    Days: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None


class ObjectIdentifier(BaseValidatorModel):
    Key: str
    VersionId: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[Timestamp] = None
    Size: Optional[int] = None


class ObjectLockRetention(BaseValidatorModel):
    Mode: Optional[ObjectLockRetentionModeType] = None
    RetainUntilDate: Optional[Timestamp] = None


class Transition(BaseValidatorModel):
    Date: Optional[Timestamp] = None
    Days: Optional[int] = None
    StorageClass: Optional[TransitionStorageClassType] = None


# This class is the input for the 'put_bucket_accelerate_configuration' function.
class PutBucketAccelerateConfigurationRequest(BaseValidatorModel):
    Bucket: str
    AccelerateConfiguration: AccelerateConfiguration
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None


class DeleteMarkerEntry(BaseValidatorModel):
    Owner: Optional[Owner] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    IsLatest: Optional[bool] = None
    LastModified: Optional[datetime] = None


class AnalyticsAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class AnalyticsAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'get_bucket_tagging' function.
class GetBucketTaggingOutput(BaseValidatorModel):
    TagSet: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object_tagging' function.
class GetObjectTaggingOutput(BaseValidatorModel):
    VersionId: str
    TagSet: List[Tag]
    ResponseMetadata: ResponseMetadata


class IntelligentTieringAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class IntelligentTieringAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class LifecycleRuleAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class LifecycleRuleAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None


class MetricsAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    AccessPointArn: Optional[str] = None


class MetricsAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    AccessPointArn: Optional[str] = None


class ReplicationRuleAndOperatorOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ReplicationRuleAndOperator(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class Tagging(BaseValidatorModel):
    TagSet: List[Tag]


class AnalyticsExportDestination(BaseValidatorModel):
    S3BucketDestination: AnalyticsS3BucketDestination


class PutObjectRequestBucketPutObject(BaseValidatorModel):
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[Blob] = None
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
    Expires: Optional[Timestamp] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectRequestObjectPut(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[Blob] = None
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
    Expires: Optional[Timestamp] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectRequestObjectSummaryPut(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[Blob] = None
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
    Expires: Optional[Timestamp] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_object' function.
class PutObjectRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    Body: Optional[Blob] = None
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
    Expires: Optional[Timestamp] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    WriteOffsetBytes: Optional[int] = None
    Metadata: Optional[Dict[str, str]] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None


class UploadPartRequestMultipartUploadPartUpload(BaseValidatorModel):
    Body: Optional[Blob] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'upload_part' function.
class UploadPartRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    PartNumber: int
    UploadId: str
    Body: Optional[Blob] = None
    ContentLength: Optional[int] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'write_get_object_response' function.
class WriteGetObjectResponseRequest(BaseValidatorModel):
    RequestRoute: str
    RequestToken: str
    Body: Optional[Blob] = None
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
    Expires: Optional[Timestamp] = None
    Expiration: Optional[str] = None
    LastModified: Optional[Timestamp] = None
    MissingMeta: Optional[int] = None
    Metadata: Optional[Dict[str, str]] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    PartsCount: Optional[int] = None
    ReplicationStatus: Optional[ReplicationStatusType] = None
    RequestCharged: Optional[Literal['requester']] = None
    Restore: Optional[str] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    TagCount: Optional[int] = None
    VersionId: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None


class BucketCopyRequest(BaseValidatorModel):
    CopySource: CopySource
    Key: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    SourceClient: Optional[BaseClient] = None
    Config: Optional[TransferConfig] = None


class ClientCopyRequest(BaseValidatorModel):
    CopySource: CopySource
    Bucket: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    SourceClient: Optional[BaseClient] = None
    Config: Optional[TransferConfig] = None

CopySourceOrStr = Union[str, CopySource]


class ObjectCopyRequest(BaseValidatorModel):
    CopySource: CopySource
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    SourceClient: Optional[BaseClient] = None
    Config: Optional[TransferConfig] = None


class BucketDownloadFileobjRequest(BaseValidatorModel):
    Key: str
    Fileobj: Fileobj
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class BucketUploadFileobjRequest(BaseValidatorModel):
    Fileobj: Fileobj
    Key: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class ClientDownloadFileobjRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    Fileobj: Fileobj
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class ClientUploadFileobjRequest(BaseValidatorModel):
    Fileobj: Fileobj
    Bucket: str
    Key: str
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class ObjectDownloadFileobjRequest(BaseValidatorModel):
    Fileobj: Fileobj
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


class ObjectUploadFileobjRequest(BaseValidatorModel):
    Fileobj: Fileobj
    ExtraArgs: Optional[Dict[str, Any]] = None
    Callback: Optional[Callable[[Ellipsis], Any]] = None
    Config: Optional[TransferConfig] = None


# This class is the output for the 'list_buckets' function.
class ListBucketsOutput(BaseValidatorModel):
    Buckets: List[Bucket]
    Owner: Owner
    ContinuationToken: str
    Prefix: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_directory_buckets' function.
class ListDirectoryBucketsOutput(BaseValidatorModel):
    Buckets: List[Bucket]
    ContinuationToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bucket_cors' function.
class GetBucketCorsOutput(BaseValidatorModel):
    CORSRules: List[CORSRuleOutput]
    ResponseMetadata: ResponseMetadata

CORSRuleUnion = Union[CORSRule, CORSRuleOutput]

CloudFunctionConfigurationUnion = Union[CloudFunctionConfiguration, CloudFunctionConfigurationOutput]


class CompletedMultipartUpload(BaseValidatorModel):
    Parts: Optional[List[CompletedPart]] = None


# This class is the output for the 'copy_object' function.
class CopyObjectOutput(BaseValidatorModel):
    CopyObjectResult: CopyObjectResult
    Expiration: str
    CopySourceVersionId: str
    VersionId: str
    ServerSideEncryption: ServerSideEncryptionType
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upload_part_copy' function.
class UploadPartCopyOutput(BaseValidatorModel):
    CopySourceVersionId: str
    CopyPartResult: CopyPartResult
    ServerSideEncryption: ServerSideEncryptionType
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


class CreateBucketConfiguration(BaseValidatorModel):
    LocationConstraint: Optional[BucketLocationConstraintType] = None
    Location: Optional[LocationInfo] = None
    Bucket: Optional[BucketInfo] = None


# This class is the output for the 'create_session' function.
class CreateSessionOutput(BaseValidatorModel):
    ServerSideEncryption: ServerSideEncryptionType
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    Credentials: SessionCredentials
    ResponseMetadata: ResponseMetadata


class ObjectLockRule(BaseValidatorModel):
    DefaultRetention: Optional[DefaultRetention] = None


# This class is the output for the 'delete_objects' function.
class DeleteObjectsOutput(BaseValidatorModel):
    Deleted: List[DeletedObject]
    RequestCharged: Literal['requester']
    Errors: List[Error]
    ResponseMetadata: ResponseMetadata


class S3KeyFilterOutput(BaseValidatorModel):
    FilterRules: Optional[List[FilterRule]] = None


class S3KeyFilter(BaseValidatorModel):
    FilterRules: Optional[List[FilterRule]] = None


# This class is the output for the 'get_bucket_policy_status' function.
class GetBucketPolicyStatusOutput(BaseValidatorModel):
    PolicyStatus: PolicyStatus
    ResponseMetadata: ResponseMetadata


class GetObjectAttributesParts(BaseValidatorModel):
    TotalPartsCount: Optional[int] = None
    PartNumberMarker: Optional[int] = None
    NextPartNumberMarker: Optional[int] = None
    MaxParts: Optional[int] = None
    IsTruncated: Optional[bool] = None
    Parts: Optional[List[ObjectPart]] = None


# This class is the output for the 'get_object_legal_hold' function.
class GetObjectLegalHoldOutput(BaseValidatorModel):
    LegalHold: ObjectLockLegalHold
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_object_legal_hold' function.
class PutObjectLegalHoldRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    LegalHold: Optional[ObjectLockLegalHold] = None
    RequestPayer: Optional[Literal['requester']] = None
    VersionId: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the output for the 'get_object_retention' function.
class GetObjectRetentionOutput(BaseValidatorModel):
    Retention: ObjectLockRetentionOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_public_access_block' function.
class GetPublicAccessBlockOutput(BaseValidatorModel):
    PublicAccessBlockConfiguration: PublicAccessBlockConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_public_access_block' function.
class PutPublicAccessBlockRequest(BaseValidatorModel):
    Bucket: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfiguration
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class Grant(BaseValidatorModel):
    Grantee: Optional[Grantee] = None
    Permission: Optional[PermissionType] = None


class TargetGrant(BaseValidatorModel):
    Grantee: Optional[Grantee] = None
    Permission: Optional[BucketLogsPermissionType] = None


class HeadBucketRequestWaitExtra(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class HeadBucketRequestWait(BaseValidatorModel):
    Bucket: str
    ExpectedBucketOwner: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class HeadObjectRequestWaitExtra(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None
    WaiterConfig: Optional[WaiterConfig] = None


class HeadObjectRequestWait(BaseValidatorModel):
    Bucket: str
    Key: str
    IfMatch: Optional[str] = None
    IfModifiedSince: Optional[Timestamp] = None
    IfNoneMatch: Optional[str] = None
    IfUnmodifiedSince: Optional[Timestamp] = None
    Range: Optional[str] = None
    ResponseCacheControl: Optional[str] = None
    ResponseContentDisposition: Optional[str] = None
    ResponseContentEncoding: Optional[str] = None
    ResponseContentLanguage: Optional[str] = None
    ResponseContentType: Optional[str] = None
    ResponseExpires: Optional[Timestamp] = None
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    PartNumber: Optional[int] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumMode: Optional[Literal['ENABLED']] = None
    WaiterConfig: Optional[WaiterConfig] = None


class MultipartUpload(BaseValidatorModel):
    UploadId: Optional[str] = None
    Key: Optional[str] = None
    Initiated: Optional[datetime] = None
    StorageClass: Optional[StorageClassType] = None
    Owner: Optional[Owner] = None
    Initiator: Optional[Initiator] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ChecksumType: Optional[ChecksumTypeType] = None


class InputSerialization(BaseValidatorModel):
    CSV: Optional[CSVInput] = None
    CompressionType: Optional[CompressionTypeType] = None
    JSON: Optional[JSONInput] = None
    Parquet: Optional[Dict[str, Any]] = None


class InventoryEncryptionOutput(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMS] = None


class InventoryEncryption(BaseValidatorModel):
    SSES3: Optional[Dict[str, Any]] = None
    SSEKMS: Optional[SSEKMS] = None


class OutputSerialization(BaseValidatorModel):
    CSV: Optional[CSVOutput] = None
    JSON: Optional[JSONOutput] = None


class RuleOutput(BaseValidatorModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutput] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionOutput] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransition] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload] = None


class ListBucketsRequestPaginate(BaseValidatorModel):
    Prefix: Optional[str] = None
    BucketRegion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDirectoryBucketsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultipartUploadsRequestPaginate(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectVersionsRequestPaginate(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    Prefix: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    OptionalObjectAttributes: Optional[List[Literal['RestoreStatus']]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectsRequestPaginate(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    Prefix: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[List[Literal['RestoreStatus']]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectsV2RequestPaginate(BaseValidatorModel):
    Bucket: str
    Delimiter: Optional[str] = None
    EncodingType: Optional[Literal['url']] = None
    Prefix: Optional[str] = None
    FetchOwner: Optional[bool] = None
    StartAfter: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    OptionalObjectAttributes: Optional[List[Literal['RestoreStatus']]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPartsRequestPaginate(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_parts' function.
class ListPartsOutput(BaseValidatorModel):
    AbortDate: datetime
    AbortRuleId: str
    Bucket: str
    Key: str
    UploadId: str
    PartNumberMarker: int
    NextPartNumberMarker: int
    MaxParts: int
    IsTruncated: bool
    Parts: List[Part]
    Initiator: Initiator
    Owner: Owner
    StorageClass: StorageClassType
    RequestCharged: Literal['requester']
    ChecksumAlgorithm: ChecksumAlgorithmType
    ChecksumType: ChecksumTypeType
    ResponseMetadata: ResponseMetadata


class MetadataTableConfigurationResult(BaseValidatorModel):
    S3TablesDestinationResult: S3TablesDestinationResult


class MetadataTableConfiguration(BaseValidatorModel):
    S3TablesDestination: S3TablesDestination


class Metrics(BaseValidatorModel):
    Status: MetricsStatusType
    EventThreshold: Optional[ReplicationTimeValue] = None


class ReplicationTime(BaseValidatorModel):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValue


# This class is the output for the 'get_bucket_notification' function.
class NotificationConfigurationDeprecatedResponse(BaseValidatorModel):
    TopicConfiguration: TopicConfigurationDeprecatedOutput
    QueueConfiguration: QueueConfigurationDeprecatedOutput
    CloudFunctionConfiguration: CloudFunctionConfigurationOutput
    ResponseMetadata: ResponseMetadata


class Object(BaseValidatorModel):
    Key: Optional[str] = None
    LastModified: Optional[datetime] = None
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    Size: Optional[int] = None
    StorageClass: Optional[ObjectStorageClassType] = None
    Owner: Optional[Owner] = None
    RestoreStatus: Optional[RestoreStatus] = None


class ObjectVersion(BaseValidatorModel):
    ETag: Optional[str] = None
    ChecksumAlgorithm: Optional[List[ChecksumAlgorithmType]] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    Size: Optional[int] = None
    StorageClass: Optional[Literal['STANDARD']] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    IsLatest: Optional[bool] = None
    LastModified: Optional[datetime] = None
    Owner: Optional[Owner] = None
    RestoreStatus: Optional[RestoreStatus] = None


class OwnershipControlsOutput(BaseValidatorModel):
    Rules: List[OwnershipControlsRule]


class OwnershipControls(BaseValidatorModel):
    Rules: List[OwnershipControlsRule]


class TargetObjectKeyFormatOutput(BaseValidatorModel):
    SimplePrefix: Optional[Dict[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefix] = None


class TargetObjectKeyFormat(BaseValidatorModel):
    SimplePrefix: Optional[Dict[str, Any]] = None
    PartitionedPrefix: Optional[PartitionedPrefix] = None


class ProgressEvent(BaseValidatorModel):
    Details: Optional[Progress] = None


class PutBucketRequestPaymentRequestBucketRequestPaymentPut(BaseValidatorModel):
    RequestPaymentConfiguration: RequestPaymentConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_request_payment' function.
class PutBucketRequestPaymentRequest(BaseValidatorModel):
    Bucket: str
    RequestPaymentConfiguration: RequestPaymentConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketVersioningRequestBucketVersioningPut(BaseValidatorModel):
    VersioningConfiguration: VersioningConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_versioning' function.
class PutBucketVersioningRequest(BaseValidatorModel):
    Bucket: str
    VersioningConfiguration: VersioningConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    MFA: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None

QueueConfigurationDeprecatedUnion = Union[QueueConfigurationDeprecated, QueueConfigurationDeprecatedOutput]


class RoutingRule(BaseValidatorModel):
    Redirect: Redirect
    Condition: Optional[Condition] = None


class ServerSideEncryptionRule(BaseValidatorModel):
    ApplyServerSideEncryptionByDefault: Optional[ServerSideEncryptionByDefault] = None
    BucketKeyEnabled: Optional[bool] = None


class SourceSelectionCriteria(BaseValidatorModel):
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjects] = None
    ReplicaModifications: Optional[ReplicaModifications] = None


class StatsEvent(BaseValidatorModel):
    Details: Optional[Stats] = None

TopicConfigurationDeprecatedUnion = Union[TopicConfigurationDeprecated, TopicConfigurationDeprecatedOutput]

LifecycleExpirationUnion = Union[LifecycleExpiration, LifecycleExpirationOutput]


class Delete(BaseValidatorModel):
    Objects: List[ObjectIdentifier]
    Quiet: Optional[bool] = None

ObjectLockRetentionUnion = Union[ObjectLockRetention, ObjectLockRetentionOutput]

TransitionUnion = Union[Transition, TransitionOutput]


class AnalyticsFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    And: Optional[AnalyticsAndOperatorOutput] = None


class AnalyticsFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    And: Optional[AnalyticsAndOperator] = None


class IntelligentTieringFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    And: Optional[IntelligentTieringAndOperatorOutput] = None


class IntelligentTieringFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    And: Optional[IntelligentTieringAndOperator] = None


class LifecycleRuleFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorOutput] = None

LifecycleRuleAndOperatorUnion = Union[LifecycleRuleAndOperator, LifecycleRuleAndOperatorOutput]


class MetricsFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperatorOutput] = None


class MetricsFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperator] = None


class ReplicationRuleFilterOutput(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    And: Optional[ReplicationRuleAndOperatorOutput] = None


class ReplicationRuleFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    And: Optional[ReplicationRuleAndOperator] = None


class PutBucketTaggingRequestBucketTaggingPut(BaseValidatorModel):
    Tagging: Tagging
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_tagging' function.
class PutBucketTaggingRequest(BaseValidatorModel):
    Bucket: str
    Tagging: Tagging
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_object_tagging' function.
class PutObjectTaggingRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    Tagging: Tagging
    VersionId: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None


class StorageClassAnalysisDataExport(BaseValidatorModel):
    OutputSchemaVersion: Literal['V_1']
    Destination: AnalyticsExportDestination


class CopyObjectRequestObjectCopyFrom(BaseValidatorModel):
    CopySource: CopySourceOrStr
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[Timestamp] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[Timestamp] = None
    Expires: Optional[Timestamp] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None
    MetadataDirective: Optional[MetadataDirectiveType] = None
    TaggingDirective: Optional[TaggingDirectiveType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class CopyObjectRequestObjectSummaryCopyFrom(BaseValidatorModel):
    CopySource: CopySourceOrStr
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[Timestamp] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[Timestamp] = None
    Expires: Optional[Timestamp] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None
    MetadataDirective: Optional[MetadataDirectiveType] = None
    TaggingDirective: Optional[TaggingDirectiveType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


# This class is the input for the 'copy_object' function.
class CopyObjectRequest(BaseValidatorModel):
    Bucket: str
    CopySource: CopySourceOrStr
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    CacheControl: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ContentDisposition: Optional[str] = None
    ContentEncoding: Optional[str] = None
    ContentLanguage: Optional[str] = None
    ContentType: Optional[str] = None
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[Timestamp] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[Timestamp] = None
    Expires: Optional[Timestamp] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None
    MetadataDirective: Optional[MetadataDirectiveType] = None
    TaggingDirective: Optional[TaggingDirectiveType] = None
    ServerSideEncryption: Optional[ServerSideEncryptionType] = None
    StorageClass: Optional[StorageClassType] = None
    WebsiteRedirectLocation: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    SSEKMSKeyId: Optional[str] = None
    SSEKMSEncryptionContext: Optional[str] = None
    BucketKeyEnabled: Optional[bool] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    Tagging: Optional[str] = None
    ObjectLockMode: Optional[ObjectLockModeType] = None
    ObjectLockRetainUntilDate: Optional[Timestamp] = None
    ObjectLockLegalHoldStatus: Optional[ObjectLockLegalHoldStatusType] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class UploadPartCopyRequestMultipartUploadPartCopyFrom(BaseValidatorModel):
    CopySource: CopySourceOrStr
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[Timestamp] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[Timestamp] = None
    CopySourceRange: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


# This class is the input for the 'upload_part_copy' function.
class UploadPartCopyRequest(BaseValidatorModel):
    Bucket: str
    CopySource: CopySourceOrStr
    Key: str
    PartNumber: int
    UploadId: str
    CopySourceIfMatch: Optional[str] = None
    CopySourceIfModifiedSince: Optional[Timestamp] = None
    CopySourceIfNoneMatch: Optional[str] = None
    CopySourceIfUnmodifiedSince: Optional[Timestamp] = None
    CopySourceRange: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    CopySourceSSECustomerAlgorithm: Optional[str] = None
    CopySourceSSECustomerKey: Optional[Union[bytes, str]] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    ExpectedSourceBucketOwner: Optional[str] = None


class CORSConfiguration(BaseValidatorModel):
    CORSRules: List[CORSRuleUnion]


class CompleteMultipartUploadRequestMultipartUploadComplete(BaseValidatorModel):
    MultipartUpload: Optional[CompletedMultipartUpload] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    MpuObjectSize: Optional[int] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None


# This class is the input for the 'complete_multipart_upload' function.
class CompleteMultipartUploadRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    UploadId: str
    MultipartUpload: Optional[CompletedMultipartUpload] = None
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[ChecksumTypeType] = None
    MpuObjectSize: Optional[int] = None
    RequestPayer: Optional[Literal['requester']] = None
    ExpectedBucketOwner: Optional[str] = None
    IfMatch: Optional[str] = None
    IfNoneMatch: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None


class CreateBucketRequestBucketCreate(BaseValidatorModel):
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfiguration] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    ObjectOwnership: Optional[ObjectOwnershipType] = None


class CreateBucketRequestServiceResourceCreateBucket(BaseValidatorModel):
    Bucket: str
    ACL: Optional[BucketCannedACLType] = None
    CreateBucketConfiguration: Optional[CreateBucketConfiguration] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ObjectLockEnabledForBucket: Optional[bool] = None
    ObjectOwnership: Optional[ObjectOwnershipType] = None


# This class is the input for the 'create_bucket' function.
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
    ObjectOwnership: Optional[ObjectOwnershipType] = None


class ObjectLockConfiguration(BaseValidatorModel):
    ObjectLockEnabled: Optional[Literal['Enabled']] = None
    Rule: Optional[ObjectLockRule] = None


class NotificationConfigurationFilterOutput(BaseValidatorModel):
    Key: Optional[S3KeyFilterOutput] = None

S3KeyFilterUnion = Union[S3KeyFilter, S3KeyFilterOutput]


# This class is the output for the 'get_object_attributes' function.
class GetObjectAttributesOutput(BaseValidatorModel):
    DeleteMarker: bool
    LastModified: datetime
    VersionId: str
    RequestCharged: Literal['requester']
    ETag: str
    Checksum: Checksum
    ObjectParts: GetObjectAttributesParts
    StorageClass: StorageClassType
    ObjectSize: int
    ResponseMetadata: ResponseMetadata


class AccessControlPolicy(BaseValidatorModel):
    Grants: Optional[List[Grant]] = None
    Owner: Optional[Owner] = None


# This class is the output for the 'get_bucket_acl' function.
class GetBucketAclOutput(BaseValidatorModel):
    Owner: Owner
    Grants: List[Grant]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object_acl' function.
class GetObjectAclOutput(BaseValidatorModel):
    Owner: Owner
    Grants: List[Grant]
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata


class S3Location(BaseValidatorModel):
    BucketName: str
    Prefix: str
    Encryption: Optional[Encryption] = None
    CannedACL: Optional[ObjectCannedACLType] = None
    AccessControlList: Optional[List[Grant]] = None
    Tagging: Optional[Tagging] = None
    UserMetadata: Optional[List[MetadataEntry]] = None
    StorageClass: Optional[StorageClassType] = None


# This class is the output for the 'list_multipart_uploads' function.
class ListMultipartUploadsOutput(BaseValidatorModel):
    Bucket: str
    KeyMarker: str
    UploadIdMarker: str
    NextKeyMarker: str
    Prefix: str
    Delimiter: str
    NextUploadIdMarker: str
    MaxUploads: int
    IsTruncated: bool
    Uploads: List[MultipartUpload]
    EncodingType: Literal['url']
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata
    CommonPrefixes: Optional[List[CommonPrefix]] = None


class InventoryS3BucketDestinationOutput(BaseValidatorModel):
    Bucket: str
    Format: InventoryFormatType
    AccountId: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[InventoryEncryptionOutput] = None


class InventoryS3BucketDestination(BaseValidatorModel):
    Bucket: str
    Format: InventoryFormatType
    AccountId: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[InventoryEncryption] = None


# This class is the input for the 'select_object_content' function.
class SelectObjectContentRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    Expression: str
    ExpressionType: Literal['SQL']
    InputSerialization: InputSerialization
    OutputSerialization: OutputSerialization
    SSECustomerAlgorithm: Optional[str] = None
    SSECustomerKey: Optional[Union[bytes, str]] = None
    RequestProgress: Optional[RequestProgress] = None
    ScanRange: Optional[ScanRange] = None
    ExpectedBucketOwner: Optional[str] = None


class SelectParameters(BaseValidatorModel):
    InputSerialization: InputSerialization
    ExpressionType: Literal['SQL']
    Expression: str
    OutputSerialization: OutputSerialization


# This class is the output for the 'get_bucket_lifecycle' function.
class GetBucketLifecycleOutput(BaseValidatorModel):
    Rules: List[RuleOutput]
    ResponseMetadata: ResponseMetadata


class GetBucketMetadataTableConfigurationResult(BaseValidatorModel):
    MetadataTableConfigurationResult: MetadataTableConfigurationResult
    Status: str
    Error: Optional[ErrorDetails] = None


# This class is the input for the 'create_bucket_metadata_table_configuration' function.
class CreateBucketMetadataTableConfigurationRequest(BaseValidatorModel):
    Bucket: str
    MetadataTableConfiguration: MetadataTableConfiguration
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class Destination(BaseValidatorModel):
    Bucket: str
    Account: Optional[str] = None
    StorageClass: Optional[StorageClassType] = None
    AccessControlTranslation: Optional[AccessControlTranslation] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    ReplicationTime: Optional[ReplicationTime] = None
    Metrics: Optional[Metrics] = None


# This class is the output for the 'list_objects' function.
class ListObjectsOutput(BaseValidatorModel):
    IsTruncated: bool
    Marker: str
    NextMarker: str
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    EncodingType: Literal['url']
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata
    Contents: Optional[List[Object]] = None
    CommonPrefixes: Optional[List[CommonPrefix]] = None


# This class is the output for the 'list_objects_v2' function.
class ListObjectsV2Output(BaseValidatorModel):
    IsTruncated: bool
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    EncodingType: Literal['url']
    KeyCount: int
    ContinuationToken: str
    NextContinuationToken: str
    StartAfter: str
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata
    Contents: Optional[List[Object]] = None
    CommonPrefixes: Optional[List[CommonPrefix]] = None


# This class is the output for the 'list_object_versions' function.
class ListObjectVersionsOutput(BaseValidatorModel):
    IsTruncated: bool
    KeyMarker: str
    VersionIdMarker: str
    NextKeyMarker: str
    NextVersionIdMarker: str
    Versions: List[ObjectVersion]
    DeleteMarkers: List[DeleteMarkerEntry]
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    EncodingType: Literal['url']
    RequestCharged: Literal['requester']
    ResponseMetadata: ResponseMetadata
    CommonPrefixes: Optional[List[CommonPrefix]] = None


# This class is the output for the 'get_bucket_ownership_controls' function.
class GetBucketOwnershipControlsOutput(BaseValidatorModel):
    OwnershipControls: OwnershipControlsOutput
    ResponseMetadata: ResponseMetadata

OwnershipControlsUnion = Union[OwnershipControls, OwnershipControlsOutput]


class LoggingEnabledOutput(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrant]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatOutput] = None

TargetObjectKeyFormatUnion = Union[TargetObjectKeyFormat, TargetObjectKeyFormatOutput]


# This class is the output for the 'get_bucket_website' function.
class GetBucketWebsiteOutput(BaseValidatorModel):
    RedirectAllRequestsTo: RedirectAllRequestsTo
    IndexDocument: IndexDocument
    ErrorDocument: ErrorDocument
    RoutingRules: List[RoutingRule]
    ResponseMetadata: ResponseMetadata


class WebsiteConfiguration(BaseValidatorModel):
    ErrorDocument: Optional[ErrorDocument] = None
    IndexDocument: Optional[IndexDocument] = None
    RedirectAllRequestsTo: Optional[RedirectAllRequestsTo] = None
    RoutingRules: Optional[List[RoutingRule]] = None


class ServerSideEncryptionConfigurationOutput(BaseValidatorModel):
    Rules: List[ServerSideEncryptionRule]


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    Rules: List[ServerSideEncryptionRule]


class SelectObjectContentEventStream(BaseValidatorModel):
    Records: Optional[RecordsEvent] = None
    Stats: Optional[StatsEvent] = None
    Progress: Optional[ProgressEvent] = None
    Cont: Optional[Dict[str, Any]] = None
    End: Optional[Dict[str, Any]] = None


class NotificationConfigurationDeprecated(BaseValidatorModel):
    TopicConfiguration: Optional[TopicConfigurationDeprecatedUnion] = None
    QueueConfiguration: Optional[QueueConfigurationDeprecatedUnion] = None
    CloudFunctionConfiguration: Optional[CloudFunctionConfigurationUnion] = None


class DeleteObjectsRequestBucketDeleteObjects(BaseValidatorModel):
    Delete: Delete
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None


# This class is the input for the 'delete_objects' function.
class DeleteObjectsRequest(BaseValidatorModel):
    Bucket: str
    Delete: Delete
    MFA: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    BypassGovernanceRetention: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None


# This class is the input for the 'put_object_retention' function.
class PutObjectRetentionRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    Retention: Optional[ObjectLockRetentionUnion] = None
    RequestPayer: Optional[Literal['requester']] = None
    VersionId: Optional[str] = None
    BypassGovernanceRetention: Optional[bool] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class Rule(BaseValidatorModel):
    Prefix: str
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationUnion] = None
    ID: Optional[str] = None
    Transition: Optional[TransitionUnion] = None
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransition] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload] = None


class IntelligentTieringConfigurationOutput(BaseValidatorModel):
    Id: str
    Status: IntelligentTieringStatusType
    Tierings: List[Tiering]
    Filter: Optional[IntelligentTieringFilterOutput] = None


class IntelligentTieringConfiguration(BaseValidatorModel):
    Id: str
    Status: IntelligentTieringStatusType
    Tierings: List[Tiering]
    Filter: Optional[IntelligentTieringFilter] = None


class LifecycleRuleOutput(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationOutput] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterOutput] = None
    Transitions: Optional[List[TransitionOutput]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransition]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload] = None


class LifecycleRuleFilter(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    And: Optional[LifecycleRuleAndOperatorUnion] = None


class MetricsConfigurationOutput(BaseValidatorModel):
    Id: str
    Filter: Optional[MetricsFilterOutput] = None


class MetricsConfiguration(BaseValidatorModel):
    Id: str
    Filter: Optional[MetricsFilter] = None


class StorageClassAnalysis(BaseValidatorModel):
    DataExport: Optional[StorageClassAnalysisDataExport] = None


class PutBucketCorsRequestBucketCorsPut(BaseValidatorModel):
    CORSConfiguration: CORSConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_cors' function.
class PutBucketCorsRequest(BaseValidatorModel):
    Bucket: str
    CORSConfiguration: CORSConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the output for the 'get_object_lock_configuration' function.
class GetObjectLockConfigurationOutput(BaseValidatorModel):
    ObjectLockConfiguration: ObjectLockConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_object_lock_configuration' function.
class PutObjectLockConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ObjectLockConfiguration: Optional[ObjectLockConfiguration] = None
    RequestPayer: Optional[Literal['requester']] = None
    Token: Optional[str] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class LambdaFunctionConfigurationOutput(BaseValidatorModel):
    LambdaFunctionArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutput] = None


class QueueConfigurationOutput(BaseValidatorModel):
    QueueArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutput] = None


class TopicConfigurationOutput(BaseValidatorModel):
    TopicArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterOutput] = None


class NotificationConfigurationFilter(BaseValidatorModel):
    Key: Optional[S3KeyFilterUnion] = None


class PutBucketAclRequestBucketAclPut(BaseValidatorModel):
    ACL: Optional[BucketCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicy] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_acl' function.
class PutBucketAclRequest(BaseValidatorModel):
    Bucket: str
    ACL: Optional[BucketCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicy] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutObjectAclRequestObjectAclPut(BaseValidatorModel):
    ACL: Optional[ObjectCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicy] = None
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_object_acl' function.
class PutObjectAclRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    ACL: Optional[ObjectCannedACLType] = None
    AccessControlPolicy: Optional[AccessControlPolicy] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    GrantFullControl: Optional[str] = None
    GrantRead: Optional[str] = None
    GrantReadACP: Optional[str] = None
    GrantWrite: Optional[str] = None
    GrantWriteACP: Optional[str] = None
    RequestPayer: Optional[Literal['requester']] = None
    VersionId: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class OutputLocation(BaseValidatorModel):
    S3: Optional[S3Location] = None


class InventoryDestinationOutput(BaseValidatorModel):
    S3BucketDestination: InventoryS3BucketDestinationOutput


class InventoryDestination(BaseValidatorModel):
    S3BucketDestination: InventoryS3BucketDestination


# This class is the output for the 'get_bucket_metadata_table_configuration' function.
class GetBucketMetadataTableConfigurationOutput(BaseValidatorModel):
    GetBucketMetadataTableConfigurationResult: GetBucketMetadataTableConfigurationResult
    ResponseMetadata: ResponseMetadata


class ReplicationRuleOutput(BaseValidatorModel):
    Status: ReplicationRuleStatusType
    Destination: Destination
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
    ID: Optional[str] = None
    Priority: Optional[int] = None
    Prefix: Optional[str] = None
    Filter: Optional[ReplicationRuleFilter] = None
    SourceSelectionCriteria: Optional[SourceSelectionCriteria] = None
    ExistingObjectReplication: Optional[ExistingObjectReplication] = None
    DeleteMarkerReplication: Optional[DeleteMarkerReplication] = None


# This class is the input for the 'put_bucket_ownership_controls' function.
class PutBucketOwnershipControlsRequest(BaseValidatorModel):
    Bucket: str
    OwnershipControls: OwnershipControlsUnion
    ContentMD5: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the output for the 'get_bucket_logging' function.
class GetBucketLoggingOutput(BaseValidatorModel):
    LoggingEnabled: LoggingEnabledOutput
    ResponseMetadata: ResponseMetadata


class LoggingEnabled(BaseValidatorModel):
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrant]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormatUnion] = None


class PutBucketWebsiteRequestBucketWebsitePut(BaseValidatorModel):
    WebsiteConfiguration: WebsiteConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_website' function.
class PutBucketWebsiteRequest(BaseValidatorModel):
    Bucket: str
    WebsiteConfiguration: WebsiteConfiguration
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the output for the 'get_bucket_encryption' function.
class GetBucketEncryptionOutput(BaseValidatorModel):
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationOutput
    ResponseMetadata: ResponseMetadata

ServerSideEncryptionConfigurationUnion = Union[ServerSideEncryptionConfiguration, ServerSideEncryptionConfigurationOutput]


# This class is the output for the 'select_object_content' function.
class SelectObjectContentOutput(BaseValidatorModel):
    Payload: EventStream[SelectObjectContentEventStream]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_bucket_notification' function.
class PutBucketNotificationRequest(BaseValidatorModel):
    Bucket: str
    NotificationConfiguration: NotificationConfigurationDeprecated
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None

RuleUnion = Union[Rule, RuleOutput]


# This class is the output for the 'get_bucket_intelligent_tiering_configuration' function.
class GetBucketIntelligentTieringConfigurationOutput(BaseValidatorModel):
    IntelligentTieringConfiguration: IntelligentTieringConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bucket_intelligent_tiering_configurations' function.
class ListBucketIntelligentTieringConfigurationsOutput(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    IntelligentTieringConfigurationList: List[IntelligentTieringConfigurationOutput]
    ResponseMetadata: ResponseMetadata

IntelligentTieringConfigurationUnion = Union[IntelligentTieringConfiguration, IntelligentTieringConfigurationOutput]


# This class is the output for the 'get_bucket_lifecycle_configuration' function.
class GetBucketLifecycleConfigurationOutput(BaseValidatorModel):
    Rules: List[LifecycleRuleOutput]
    TransitionDefaultMinimumObjectSize: TransitionDefaultMinimumObjectSizeType
    ResponseMetadata: ResponseMetadata

LifecycleRuleFilterUnion = Union[LifecycleRuleFilter, LifecycleRuleFilterOutput]


# This class is the output for the 'get_bucket_metrics_configuration' function.
class GetBucketMetricsConfigurationOutput(BaseValidatorModel):
    MetricsConfiguration: MetricsConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bucket_metrics_configurations' function.
class ListBucketMetricsConfigurationsOutput(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    MetricsConfigurationList: List[MetricsConfigurationOutput]
    ResponseMetadata: ResponseMetadata

MetricsConfigurationUnion = Union[MetricsConfiguration, MetricsConfigurationOutput]


class AnalyticsConfigurationOutput(BaseValidatorModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysis
    Filter: Optional[AnalyticsFilterOutput] = None


class AnalyticsConfiguration(BaseValidatorModel):
    Id: str
    StorageClassAnalysis: StorageClassAnalysis
    Filter: Optional[AnalyticsFilter] = None


# This class is the output for the 'get_bucket_notification_configuration' function.
class NotificationConfigurationResponse(BaseValidatorModel):
    TopicConfigurations: List[TopicConfigurationOutput]
    QueueConfigurations: List[QueueConfigurationOutput]
    LambdaFunctionConfigurations: List[LambdaFunctionConfigurationOutput]
    EventBridgeConfiguration: Dict[str, Any]
    ResponseMetadata: ResponseMetadata

NotificationConfigurationFilterUnion = Union[NotificationConfigurationFilter, NotificationConfigurationFilterOutput]


class RestoreRequest(BaseValidatorModel):
    Days: Optional[int] = None
    GlacierJobParameters: Optional[GlacierJobParameters] = None
    Type: Optional[Literal['SELECT']] = None
    Tier: Optional[TierType] = None
    Description: Optional[str] = None
    SelectParameters: Optional[SelectParameters] = None
    OutputLocation: Optional[OutputLocation] = None


class InventoryConfigurationOutput(BaseValidatorModel):
    Destination: InventoryDestinationOutput
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersionsType
    Schedule: InventorySchedule
    Filter: Optional[InventoryFilter] = None
    OptionalFields: Optional[List[InventoryOptionalFieldType]] = None


class InventoryConfiguration(BaseValidatorModel):
    Destination: InventoryDestination
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersionsType
    Schedule: InventorySchedule
    Filter: Optional[InventoryFilter] = None
    OptionalFields: Optional[List[InventoryOptionalFieldType]] = None


class ReplicationConfigurationOutput(BaseValidatorModel):
    Role: str
    Rules: List[ReplicationRuleOutput]


class ReplicationConfiguration(BaseValidatorModel):
    Role: str
    Rules: List[ReplicationRule]

LoggingEnabledUnion = Union[LoggingEnabled, LoggingEnabledOutput]


# This class is the input for the 'put_bucket_encryption' function.
class PutBucketEncryptionRequest(BaseValidatorModel):
    Bucket: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationUnion
    ContentMD5: Optional[str] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class LifecycleConfiguration(BaseValidatorModel):
    Rules: List[RuleUnion]


# This class is the input for the 'put_bucket_intelligent_tiering_configuration' function.
class PutBucketIntelligentTieringConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    IntelligentTieringConfiguration: IntelligentTieringConfigurationUnion


class LifecycleRule(BaseValidatorModel):
    Status: ExpirationStatusType
    Expiration: Optional[LifecycleExpirationUnion] = None
    ID: Optional[str] = None
    Prefix: Optional[str] = None
    Filter: Optional[LifecycleRuleFilterUnion] = None
    Transitions: Optional[List[TransitionUnion]] = None
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransition]] = None
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration] = None
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload] = None


# This class is the input for the 'put_bucket_metrics_configuration' function.
class PutBucketMetricsConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    MetricsConfiguration: MetricsConfigurationUnion
    ExpectedBucketOwner: Optional[str] = None


# This class is the output for the 'get_bucket_analytics_configuration' function.
class GetBucketAnalyticsConfigurationOutput(BaseValidatorModel):
    AnalyticsConfiguration: AnalyticsConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bucket_analytics_configurations' function.
class ListBucketAnalyticsConfigurationsOutput(BaseValidatorModel):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    AnalyticsConfigurationList: List[AnalyticsConfigurationOutput]
    ResponseMetadata: ResponseMetadata

AnalyticsConfigurationUnion = Union[AnalyticsConfiguration, AnalyticsConfigurationOutput]


class LambdaFunctionConfiguration(BaseValidatorModel):
    LambdaFunctionArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterUnion] = None


class QueueConfiguration(BaseValidatorModel):
    QueueArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterUnion] = None


class TopicConfiguration(BaseValidatorModel):
    TopicArn: str
    Events: List[EventType]
    Id: Optional[str] = None
    Filter: Optional[NotificationConfigurationFilterUnion] = None


class RestoreObjectRequestObjectRestoreObject(BaseValidatorModel):
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequest] = None
    RequestPayer: Optional[Literal['requester']] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class RestoreObjectRequestObjectSummaryRestoreObject(BaseValidatorModel):
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequest] = None
    RequestPayer: Optional[Literal['requester']] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'restore_object' function.
class RestoreObjectRequest(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    RestoreRequest: Optional[RestoreRequest] = None
    RequestPayer: Optional[Literal['requester']] = None
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the output for the 'get_bucket_inventory_configuration' function.
class GetBucketInventoryConfigurationOutput(BaseValidatorModel):
    InventoryConfiguration: InventoryConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bucket_inventory_configurations' function.
class ListBucketInventoryConfigurationsOutput(BaseValidatorModel):
    ContinuationToken: str
    InventoryConfigurationList: List[InventoryConfigurationOutput]
    IsTruncated: bool
    NextContinuationToken: str
    ResponseMetadata: ResponseMetadata

InventoryConfigurationUnion = Union[InventoryConfiguration, InventoryConfigurationOutput]


# This class is the output for the 'get_bucket_replication' function.
class GetBucketReplicationOutput(BaseValidatorModel):
    ReplicationConfiguration: ReplicationConfigurationOutput
    ResponseMetadata: ResponseMetadata

ReplicationConfigurationUnion = Union[ReplicationConfiguration, ReplicationConfigurationOutput]


class BucketLoggingStatus(BaseValidatorModel):
    LoggingEnabled: Optional[LoggingEnabledUnion] = None


class PutBucketLifecycleRequestBucketLifecyclePut(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfiguration] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_lifecycle' function.
class PutBucketLifecycleRequest(BaseValidatorModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[LifecycleConfiguration] = None
    ExpectedBucketOwner: Optional[str] = None

LifecycleRuleUnion = Union[LifecycleRule, LifecycleRuleOutput]


# This class is the input for the 'put_bucket_analytics_configuration' function.
class PutBucketAnalyticsConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    AnalyticsConfiguration: AnalyticsConfigurationUnion
    ExpectedBucketOwner: Optional[str] = None

LambdaFunctionConfigurationUnion = Union[LambdaFunctionConfiguration, LambdaFunctionConfigurationOutput]

QueueConfigurationUnion = Union[QueueConfiguration, QueueConfigurationOutput]

TopicConfigurationUnion = Union[TopicConfiguration, TopicConfigurationOutput]


# This class is the input for the 'put_bucket_inventory_configuration' function.
class PutBucketInventoryConfigurationRequest(BaseValidatorModel):
    Bucket: str
    Id: str
    InventoryConfiguration: InventoryConfigurationUnion
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_replication' function.
class PutBucketReplicationRequest(BaseValidatorModel):
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationUnion
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    Token: Optional[str] = None
    ExpectedBucketOwner: Optional[str] = None


class PutBucketLoggingRequestBucketLoggingPut(BaseValidatorModel):
    BucketLoggingStatus: BucketLoggingStatus
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


# This class is the input for the 'put_bucket_logging' function.
class PutBucketLoggingRequest(BaseValidatorModel):
    Bucket: str
    BucketLoggingStatus: BucketLoggingStatus
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    ExpectedBucketOwner: Optional[str] = None


class BucketLifecycleConfiguration(BaseValidatorModel):
    Rules: List[LifecycleRuleUnion]


class NotificationConfiguration(BaseValidatorModel):
    TopicConfigurations: Optional[List[TopicConfigurationUnion]] = None
    QueueConfigurations: Optional[List[QueueConfigurationUnion]] = None
    LambdaFunctionConfigurations: Optional[List[LambdaFunctionConfigurationUnion]] = None
    EventBridgeConfiguration: Optional[Dict[str, Any]] = None


class PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPut(BaseValidatorModel):
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfiguration] = None
    ExpectedBucketOwner: Optional[str] = None
    TransitionDefaultMinimumObjectSize: Optional[TransitionDefaultMinimumObjectSizeType] = None


# This class is the input for the 'put_bucket_lifecycle_configuration' function.
class PutBucketLifecycleConfigurationRequest(BaseValidatorModel):
    Bucket: str
    ChecksumAlgorithm: Optional[ChecksumAlgorithmType] = None
    LifecycleConfiguration: Optional[BucketLifecycleConfiguration] = None
    ExpectedBucketOwner: Optional[str] = None
    TransitionDefaultMinimumObjectSize: Optional[TransitionDefaultMinimumObjectSizeType] = None


class PutBucketNotificationConfigurationRequestBucketNotificationPut(BaseValidatorModel):
    NotificationConfiguration: NotificationConfiguration
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None


# This class is the input for the 'put_bucket_notification_configuration' function.
class PutBucketNotificationConfigurationRequest(BaseValidatorModel):
    Bucket: str
    NotificationConfiguration: NotificationConfiguration
    ExpectedBucketOwner: Optional[str] = None
    SkipDestinationValidation: Optional[bool] = None