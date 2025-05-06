from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.signer.signer_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddProfilePermissionRequest(BaseValidatorModel):
    profileName: str
    action: str
    principal: str
    statementId: str
    profileVersion: Optional[str] = None
    revisionId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelSigningProfileRequest(BaseValidatorModel):
    profileName: str


class DescribeSigningJobRequest(BaseValidatorModel):
    jobId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class SigningJobRevocationRecord(BaseValidatorModel):
    reason: Optional[str] = None
    revokedAt: Optional[datetime] = None
    revokedBy: Optional[str] = None


class SigningMaterial(BaseValidatorModel):
    certificateArn: str


class S3Destination(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class EncryptionAlgorithmOptions(BaseValidatorModel):
    allowedValues: List[EncryptionAlgorithmType]
    defaultValue: EncryptionAlgorithmType

Timestamp = Union[datetime, str]


class GetSigningPlatformRequest(BaseValidatorModel):
    platformId: str


class SigningImageFormat(BaseValidatorModel):
    supportedFormats: List[ImageFormatType]
    defaultFormat: ImageFormatType


class GetSigningProfileRequest(BaseValidatorModel):
    profileName: str
    profileOwner: Optional[str] = None


class SignatureValidityPeriod(BaseValidatorModel):
    value: Optional[int] = None
    type: Optional[ValidityTypeType] = None


class SigningProfileRevocationRecord(BaseValidatorModel):
    revocationEffectiveFrom: Optional[datetime] = None
    revokedAt: Optional[datetime] = None
    revokedBy: Optional[str] = None


class HashAlgorithmOptions(BaseValidatorModel):
    allowedValues: List[HashAlgorithmType]
    defaultValue: HashAlgorithmType


class ListProfilePermissionsRequest(BaseValidatorModel):
    profileName: str
    nextToken: Optional[str] = None


class Permission(BaseValidatorModel):
    action: Optional[str] = None
    principal: Optional[str] = None
    statementId: Optional[str] = None
    profileVersion: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSigningPlatformsRequest(BaseValidatorModel):
    category: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSigningProfilesRequest(BaseValidatorModel):
    includeCanceled: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    platformId: Optional[str] = None
    statuses: Optional[List[SigningProfileStatusType]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RemoveProfilePermissionRequest(BaseValidatorModel):
    profileName: str
    revisionId: str
    statementId: str


class RevokeSignatureRequest(BaseValidatorModel):
    jobId: str
    reason: str
    jobOwner: Optional[str] = None


class S3SignedObject(BaseValidatorModel):
    bucketName: Optional[str] = None
    key: Optional[str] = None


class S3Source(BaseValidatorModel):
    bucketName: str
    key: str
    version: str


class SigningConfigurationOverrides(BaseValidatorModel):
    encryptionAlgorithm: Optional[EncryptionAlgorithmType] = None
    hashAlgorithm: Optional[HashAlgorithmType] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AddProfilePermissionResponse(BaseValidatorModel):
    revisionId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetRevocationStatusResponse(BaseValidatorModel):
    revokedEntities: List[str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutSigningProfileResponse(BaseValidatorModel):
    arn: str
    profileVersion: str
    profileVersionArn: str
    ResponseMetadata: ResponseMetadata


class RemoveProfilePermissionResponse(BaseValidatorModel):
    revisionId: str
    ResponseMetadata: ResponseMetadata


class SignPayloadResponse(BaseValidatorModel):
    jobId: str
    jobOwner: str
    metadata: Dict[str, str]
    signature: bytes
    ResponseMetadata: ResponseMetadata


class StartSigningJobResponse(BaseValidatorModel):
    jobId: str
    jobOwner: str
    ResponseMetadata: ResponseMetadata


class SignPayloadRequest(BaseValidatorModel):
    profileName: str
    payload: Blob
    payloadFormat: str
    profileOwner: Optional[str] = None


class DescribeSigningJobRequestWait(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfig] = None


class Destination(BaseValidatorModel):
    s3: Optional[S3Destination] = None


class GetRevocationStatusRequest(BaseValidatorModel):
    signatureTimestamp: Timestamp
    platformId: str
    profileVersionArn: str
    jobArn: str
    certificateHashes: List[str]


class ListSigningJobsRequest(BaseValidatorModel):
    status: Optional[SigningStatusType] = None
    platformId: Optional[str] = None
    requestedBy: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    isRevoked: Optional[bool] = None
    signatureExpiresBefore: Optional[Timestamp] = None
    signatureExpiresAfter: Optional[Timestamp] = None
    jobInvoker: Optional[str] = None


class RevokeSigningProfileRequest(BaseValidatorModel):
    profileName: str
    profileVersion: str
    reason: str
    effectiveTime: Timestamp


class SigningProfile(BaseValidatorModel):
    profileName: Optional[str] = None
    profileVersion: Optional[str] = None
    profileVersionArn: Optional[str] = None
    signingMaterial: Optional[SigningMaterial] = None
    signatureValidityPeriod: Optional[SignatureValidityPeriod] = None
    platformId: Optional[str] = None
    platformDisplayName: Optional[str] = None
    signingParameters: Optional[Dict[str, str]] = None
    status: Optional[SigningProfileStatusType] = None
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class SigningConfiguration(BaseValidatorModel):
    encryptionAlgorithmOptions: EncryptionAlgorithmOptions
    hashAlgorithmOptions: HashAlgorithmOptions


class ListProfilePermissionsResponse(BaseValidatorModel):
    revisionId: str
    policySizeBytes: int
    permissions: List[Permission]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSigningJobsRequestPaginate(BaseValidatorModel):
    status: Optional[SigningStatusType] = None
    platformId: Optional[str] = None
    requestedBy: Optional[str] = None
    isRevoked: Optional[bool] = None
    signatureExpiresBefore: Optional[Timestamp] = None
    signatureExpiresAfter: Optional[Timestamp] = None
    jobInvoker: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSigningPlatformsRequestPaginate(BaseValidatorModel):
    category: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSigningProfilesRequestPaginate(BaseValidatorModel):
    includeCanceled: Optional[bool] = None
    platformId: Optional[str] = None
    statuses: Optional[List[SigningProfileStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SignedObject(BaseValidatorModel):
    s3: Optional[S3SignedObject] = None


class Source(BaseValidatorModel):
    s3: Optional[S3Source] = None


class SigningPlatformOverrides(BaseValidatorModel):
    signingConfiguration: Optional[SigningConfigurationOverrides] = None
    signingImageFormat: Optional[ImageFormatType] = None


class ListSigningProfilesResponse(BaseValidatorModel):
    profiles: List[SigningProfile]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetSigningPlatformResponse(BaseValidatorModel):
    platformId: str
    displayName: str
    partner: str
    target: str
    category: Literal['AWSIoT']
    signingConfiguration: SigningConfiguration
    signingImageFormat: SigningImageFormat
    maxSizeInMB: int
    revocationSupported: bool
    ResponseMetadata: ResponseMetadata


class SigningPlatform(BaseValidatorModel):
    platformId: Optional[str] = None
    displayName: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    category: Optional[Literal['AWSIoT']] = None
    signingConfiguration: Optional[SigningConfiguration] = None
    signingImageFormat: Optional[SigningImageFormat] = None
    maxSizeInMB: Optional[int] = None
    revocationSupported: Optional[bool] = None


class SigningJob(BaseValidatorModel):
    jobId: Optional[str] = None
    source: Optional[Source] = None
    signedObject: Optional[SignedObject] = None
    signingMaterial: Optional[SigningMaterial] = None
    createdAt: Optional[datetime] = None
    status: Optional[SigningStatusType] = None
    isRevoked: Optional[bool] = None
    profileName: Optional[str] = None
    profileVersion: Optional[str] = None
    platformId: Optional[str] = None
    platformDisplayName: Optional[str] = None
    signatureExpiresAt: Optional[datetime] = None
    jobOwner: Optional[str] = None
    jobInvoker: Optional[str] = None


class StartSigningJobRequest(BaseValidatorModel):
    source: Source
    destination: Destination
    profileName: str
    clientRequestToken: str
    profileOwner: Optional[str] = None


class DescribeSigningJobResponse(BaseValidatorModel):
    jobId: str
    source: Source
    signingMaterial: SigningMaterial
    platformId: str
    platformDisplayName: str
    profileName: str
    profileVersion: str
    overrides: SigningPlatformOverrides
    signingParameters: Dict[str, str]
    createdAt: datetime
    completedAt: datetime
    signatureExpiresAt: datetime
    requestedBy: str
    status: SigningStatusType
    statusReason: str
    revocationRecord: SigningJobRevocationRecord
    signedObject: SignedObject
    jobOwner: str
    jobInvoker: str
    ResponseMetadata: ResponseMetadata


class GetSigningProfileResponse(BaseValidatorModel):
    profileName: str
    profileVersion: str
    profileVersionArn: str
    revocationRecord: SigningProfileRevocationRecord
    signingMaterial: SigningMaterial
    platformId: str
    platformDisplayName: str
    signatureValidityPeriod: SignatureValidityPeriod
    overrides: SigningPlatformOverrides
    signingParameters: Dict[str, str]
    status: SigningProfileStatusType
    statusReason: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutSigningProfileRequest(BaseValidatorModel):
    profileName: str
    platformId: str
    signingMaterial: Optional[SigningMaterial] = None
    signatureValidityPeriod: Optional[SignatureValidityPeriod] = None
    overrides: Optional[SigningPlatformOverrides] = None
    signingParameters: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None


class ListSigningPlatformsResponse(BaseValidatorModel):
    platforms: List[SigningPlatform]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSigningJobsResponse(BaseValidatorModel):
    jobs: List[SigningJob]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None