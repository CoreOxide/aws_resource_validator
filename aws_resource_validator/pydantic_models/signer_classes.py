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
from aws_resource_validator.pydantic_models.signer_constants import *

class AddProfilePermissionRequestRequestTypeDef(BaseModel):
    profileName: str
    action: str
    principal: str
    statementId: str
    profileVersion: Optional[str] = None
    revisionId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelSigningProfileRequestRequestTypeDef(BaseModel):
    profileName: str

class DescribeSigningJobRequestRequestTypeDef(BaseModel):
    jobId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class SigningJobRevocationRecordTypeDef(BaseModel):
    reason: Optional[str] = None
    revokedAt: Optional[datetime] = None
    revokedBy: Optional[str] = None

class SigningMaterialTypeDef(BaseModel):
    certificateArn: str

class S3DestinationTypeDef(BaseModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None

class EncryptionAlgorithmOptionsTypeDef(BaseModel):
    allowedValues: List[EncryptionAlgorithmType]
    defaultValue: EncryptionAlgorithmType

class GetSigningPlatformRequestRequestTypeDef(BaseModel):
    platformId: str

class SigningImageFormatTypeDef(BaseModel):
    supportedFormats: List[ImageFormatType]
    defaultFormat: ImageFormatType

class GetSigningProfileRequestRequestTypeDef(BaseModel):
    profileName: str
    profileOwner: Optional[str] = None

class SignatureValidityPeriodTypeDef(BaseModel):
    value: Optional[int] = None
    type: Optional[ValidityTypeType] = None

class SigningProfileRevocationRecordTypeDef(BaseModel):
    revocationEffectiveFrom: Optional[datetime] = None
    revokedAt: Optional[datetime] = None
    revokedBy: Optional[str] = None

class HashAlgorithmOptionsTypeDef(BaseModel):
    allowedValues: List[HashAlgorithmType]
    defaultValue: HashAlgorithmType

class ListProfilePermissionsRequestRequestTypeDef(BaseModel):
    profileName: str
    nextToken: Optional[str] = None

class PermissionTypeDef(BaseModel):
    action: Optional[str] = None
    principal: Optional[str] = None
    statementId: Optional[str] = None
    profileVersion: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSigningPlatformsRequestRequestTypeDef(BaseModel):
    category: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSigningProfilesRequestRequestTypeDef(BaseModel):
    includeCanceled: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    platformId: Optional[str] = None
    statuses: Optional[Sequence[SigningProfileStatusType]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RemoveProfilePermissionRequestRequestTypeDef(BaseModel):
    profileName: str
    revisionId: str
    statementId: str

class RevokeSignatureRequestRequestTypeDef(BaseModel):
    jobId: str
    reason: str
    jobOwner: Optional[str] = None

class S3SignedObjectTypeDef(BaseModel):
    bucketName: Optional[str] = None
    key: Optional[str] = None

class S3SourceTypeDef(BaseModel):
    bucketName: str
    key: str
    version: str

class SigningConfigurationOverridesTypeDef(BaseModel):
    encryptionAlgorithm: Optional[EncryptionAlgorithmType] = None
    hashAlgorithm: Optional[HashAlgorithmType] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AddProfilePermissionResponseTypeDef(BaseModel):
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevocationStatusResponseTypeDef(BaseModel):
    revokedEntities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSigningProfileResponseTypeDef(BaseModel):
    arn: str
    profileVersion: str
    profileVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveProfilePermissionResponseTypeDef(BaseModel):
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SignPayloadResponseTypeDef(BaseModel):
    jobId: str
    jobOwner: str
    metadata: Dict[str, str]
    signature: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class StartSigningJobResponseTypeDef(BaseModel):
    jobId: str
    jobOwner: str
    ResponseMetadata: ResponseMetadataTypeDef

class SignPayloadRequestRequestTypeDef(BaseModel):
    profileName: str
    payload: BlobTypeDef
    payloadFormat: str
    profileOwner: Optional[str] = None

class DescribeSigningJobRequestSuccessfulSigningJobWaitTypeDef(BaseModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DestinationTypeDef(BaseModel):
    s3: Optional[S3DestinationTypeDef] = None

class GetRevocationStatusRequestRequestTypeDef(BaseModel):
    signatureTimestamp: TimestampTypeDef
    platformId: str
    profileVersionArn: str
    jobArn: str
    certificateHashes: Sequence[str]

class ListSigningJobsRequestRequestTypeDef(BaseModel):
    status: Optional[SigningStatusType] = None
    platformId: Optional[str] = None
    requestedBy: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    isRevoked: Optional[bool] = None
    signatureExpiresBefore: Optional[TimestampTypeDef] = None
    signatureExpiresAfter: Optional[TimestampTypeDef] = None
    jobInvoker: Optional[str] = None

class RevokeSigningProfileRequestRequestTypeDef(BaseModel):
    profileName: str
    profileVersion: str
    reason: str
    effectiveTime: TimestampTypeDef

class SigningProfileTypeDef(BaseModel):
    profileName: Optional[str] = None
    profileVersion: Optional[str] = None
    profileVersionArn: Optional[str] = None
    signingMaterial: Optional[SigningMaterialTypeDef] = None
    signatureValidityPeriod: Optional[SignatureValidityPeriodTypeDef] = None
    platformId: Optional[str] = None
    platformDisplayName: Optional[str] = None
    signingParameters: Optional[Dict[str, str]] = None
    status: Optional[SigningProfileStatusType] = None
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class SigningConfigurationTypeDef(BaseModel):
    encryptionAlgorithmOptions: EncryptionAlgorithmOptionsTypeDef
    hashAlgorithmOptions: HashAlgorithmOptionsTypeDef

class ListProfilePermissionsResponseTypeDef(BaseModel):
    revisionId: str
    policySizeBytes: int
    permissions: List[PermissionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningJobsRequestListSigningJobsPaginateTypeDef(BaseModel):
    status: Optional[SigningStatusType] = None
    platformId: Optional[str] = None
    requestedBy: Optional[str] = None
    isRevoked: Optional[bool] = None
    signatureExpiresBefore: Optional[TimestampTypeDef] = None
    signatureExpiresAfter: Optional[TimestampTypeDef] = None
    jobInvoker: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSigningPlatformsRequestListSigningPlatformsPaginateTypeDef(BaseModel):
    category: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSigningProfilesRequestListSigningProfilesPaginateTypeDef(BaseModel):
    includeCanceled: Optional[bool] = None
    platformId: Optional[str] = None
    statuses: Optional[Sequence[SigningProfileStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SignedObjectTypeDef(BaseModel):
    s3: Optional[S3SignedObjectTypeDef] = None

class SourceTypeDef(BaseModel):
    s3: Optional[S3SourceTypeDef] = None

class SigningPlatformOverridesTypeDef(BaseModel):
    signingConfiguration: Optional[SigningConfigurationOverridesTypeDef] = None
    signingImageFormat: Optional[ImageFormatType] = None

class ListSigningProfilesResponseTypeDef(BaseModel):
    profiles: List[SigningProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSigningPlatformResponseTypeDef(BaseModel):
    platformId: str
    displayName: str
    partner: str
    target: str
    category: Literal["AWSIoT"]
    signingConfiguration: SigningConfigurationTypeDef
    signingImageFormat: SigningImageFormatTypeDef
    maxSizeInMB: int
    revocationSupported: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SigningPlatformTypeDef(BaseModel):
    platformId: Optional[str] = None
    displayName: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    category: Optional[Literal["AWSIoT"]] = None
    signingConfiguration: Optional[SigningConfigurationTypeDef] = None
    signingImageFormat: Optional[SigningImageFormatTypeDef] = None
    maxSizeInMB: Optional[int] = None
    revocationSupported: Optional[bool] = None

class SigningJobTypeDef(BaseModel):
    jobId: Optional[str] = None
    source: Optional[SourceTypeDef] = None
    signedObject: Optional[SignedObjectTypeDef] = None
    signingMaterial: Optional[SigningMaterialTypeDef] = None
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

class StartSigningJobRequestRequestTypeDef(BaseModel):
    source: SourceTypeDef
    destination: DestinationTypeDef
    profileName: str
    clientRequestToken: str
    profileOwner: Optional[str] = None

class DescribeSigningJobResponseTypeDef(BaseModel):
    jobId: str
    source: SourceTypeDef
    signingMaterial: SigningMaterialTypeDef
    platformId: str
    platformDisplayName: str
    profileName: str
    profileVersion: str
    overrides: SigningPlatformOverridesTypeDef
    signingParameters: Dict[str, str]
    createdAt: datetime
    completedAt: datetime
    signatureExpiresAt: datetime
    requestedBy: str
    status: SigningStatusType
    statusReason: str
    revocationRecord: SigningJobRevocationRecordTypeDef
    signedObject: SignedObjectTypeDef
    jobOwner: str
    jobInvoker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSigningProfileResponseTypeDef(BaseModel):
    profileName: str
    profileVersion: str
    profileVersionArn: str
    revocationRecord: SigningProfileRevocationRecordTypeDef
    signingMaterial: SigningMaterialTypeDef
    platformId: str
    platformDisplayName: str
    signatureValidityPeriod: SignatureValidityPeriodTypeDef
    overrides: SigningPlatformOverridesTypeDef
    signingParameters: Dict[str, str]
    status: SigningProfileStatusType
    statusReason: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSigningProfileRequestRequestTypeDef(BaseModel):
    profileName: str
    platformId: str
    signingMaterial: Optional[SigningMaterialTypeDef] = None
    signatureValidityPeriod: Optional[SignatureValidityPeriodTypeDef] = None
    overrides: Optional[SigningPlatformOverridesTypeDef] = None
    signingParameters: Optional[Mapping[str, str]] = None
    tags: Optional[Mapping[str, str]] = None

class ListSigningPlatformsResponseTypeDef(BaseModel):
    platforms: List[SigningPlatformTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningJobsResponseTypeDef(BaseModel):
    jobs: List[SigningJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

