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
from aws_resource_validator.pydantic_models.signer_constants import *

class AddProfilePermissionRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    action: str
    principal: str
    statementId: str
    profileVersion: Optional[str] = None
    revisionId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelSigningProfileRequestRequestTypeDef(BaseValidatorModel):
    profileName: str

class DescribeSigningJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class SigningJobRevocationRecordTypeDef(BaseValidatorModel):
    reason: Optional[str] = None
    revokedAt: Optional[datetime] = None
    revokedBy: Optional[str] = None

class SigningMaterialTypeDef(BaseValidatorModel):
    certificateArn: str

class S3DestinationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None

class EncryptionAlgorithmOptionsTypeDef(BaseValidatorModel):
    allowedValues: List[EncryptionAlgorithmType]
    defaultValue: EncryptionAlgorithmType

class GetSigningPlatformRequestRequestTypeDef(BaseValidatorModel):
    platformId: str

class SigningImageFormatTypeDef(BaseValidatorModel):
    supportedFormats: List[ImageFormatType]
    defaultFormat: ImageFormatType

class GetSigningProfileRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    profileOwner: Optional[str] = None

class SignatureValidityPeriodTypeDef(BaseValidatorModel):
    value: Optional[int] = None
    type: Optional[ValidityTypeType] = None

class SigningProfileRevocationRecordTypeDef(BaseValidatorModel):
    revocationEffectiveFrom: Optional[datetime] = None
    revokedAt: Optional[datetime] = None
    revokedBy: Optional[str] = None

class HashAlgorithmOptionsTypeDef(BaseValidatorModel):
    allowedValues: List[HashAlgorithmType]
    defaultValue: HashAlgorithmType

class ListProfilePermissionsRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    nextToken: Optional[str] = None

class PermissionTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    principal: Optional[str] = None
    statementId: Optional[str] = None
    profileVersion: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSigningPlatformsRequestRequestTypeDef(BaseValidatorModel):
    category: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSigningProfilesRequestRequestTypeDef(BaseValidatorModel):
    includeCanceled: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    platformId: Optional[str] = None
    statuses: Optional[Sequence[SigningProfileStatusType]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class RemoveProfilePermissionRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    revisionId: str
    statementId: str

class RevokeSignatureRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    reason: str
    jobOwner: Optional[str] = None

class S3SignedObjectTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    key: Optional[str] = None

class S3SourceTypeDef(BaseValidatorModel):
    bucketName: str
    key: str
    version: str

class SigningConfigurationOverridesTypeDef(BaseValidatorModel):
    encryptionAlgorithm: Optional[EncryptionAlgorithmType] = None
    hashAlgorithm: Optional[HashAlgorithmType] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AddProfilePermissionResponseTypeDef(BaseValidatorModel):
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevocationStatusResponseTypeDef(BaseValidatorModel):
    revokedEntities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSigningProfileResponseTypeDef(BaseValidatorModel):
    arn: str
    profileVersion: str
    profileVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveProfilePermissionResponseTypeDef(BaseValidatorModel):
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SignPayloadResponseTypeDef(BaseValidatorModel):
    jobId: str
    jobOwner: str
    metadata: Dict[str, str]
    signature: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class StartSigningJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    jobOwner: str
    ResponseMetadata: ResponseMetadataTypeDef

class SignPayloadRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    payload: BlobTypeDef
    payloadFormat: str
    profileOwner: Optional[str] = None

class DescribeSigningJobRequestSuccessfulSigningJobWaitTypeDef(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DestinationTypeDef(BaseValidatorModel):
    s3: Optional[S3DestinationTypeDef] = None

class GetRevocationStatusRequestRequestTypeDef(BaseValidatorModel):
    signatureTimestamp: TimestampTypeDef
    platformId: str
    profileVersionArn: str
    jobArn: str
    certificateHashes: Sequence[str]

class ListSigningJobsRequestRequestTypeDef(BaseValidatorModel):
    status: Optional[SigningStatusType] = None
    platformId: Optional[str] = None
    requestedBy: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    isRevoked: Optional[bool] = None
    signatureExpiresBefore: Optional[TimestampTypeDef] = None
    signatureExpiresAfter: Optional[TimestampTypeDef] = None
    jobInvoker: Optional[str] = None

class RevokeSigningProfileRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    profileVersion: str
    reason: str
    effectiveTime: TimestampTypeDef

class SigningProfileTypeDef(BaseValidatorModel):
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

class SigningConfigurationTypeDef(BaseValidatorModel):
    encryptionAlgorithmOptions: EncryptionAlgorithmOptionsTypeDef
    hashAlgorithmOptions: HashAlgorithmOptionsTypeDef

class ListProfilePermissionsResponseTypeDef(BaseValidatorModel):
    revisionId: str
    policySizeBytes: int
    permissions: List[PermissionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningJobsRequestListSigningJobsPaginateTypeDef(BaseValidatorModel):
    status: Optional[SigningStatusType] = None
    platformId: Optional[str] = None
    requestedBy: Optional[str] = None
    isRevoked: Optional[bool] = None
    signatureExpiresBefore: Optional[TimestampTypeDef] = None
    signatureExpiresAfter: Optional[TimestampTypeDef] = None
    jobInvoker: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSigningPlatformsRequestListSigningPlatformsPaginateTypeDef(BaseValidatorModel):
    category: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSigningProfilesRequestListSigningProfilesPaginateTypeDef(BaseValidatorModel):
    includeCanceled: Optional[bool] = None
    platformId: Optional[str] = None
    statuses: Optional[Sequence[SigningProfileStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SignedObjectTypeDef(BaseValidatorModel):
    s3: Optional[S3SignedObjectTypeDef] = None

class SourceTypeDef(BaseValidatorModel):
    s3: Optional[S3SourceTypeDef] = None

class SigningPlatformOverridesTypeDef(BaseValidatorModel):
    signingConfiguration: Optional[SigningConfigurationOverridesTypeDef] = None
    signingImageFormat: Optional[ImageFormatType] = None

class ListSigningProfilesResponseTypeDef(BaseValidatorModel):
    profiles: List[SigningProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSigningPlatformResponseTypeDef(BaseValidatorModel):
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

class SigningPlatformTypeDef(BaseValidatorModel):
    platformId: Optional[str] = None
    displayName: Optional[str] = None
    partner: Optional[str] = None
    target: Optional[str] = None
    category: Optional[Literal["AWSIoT"]] = None
    signingConfiguration: Optional[SigningConfigurationTypeDef] = None
    signingImageFormat: Optional[SigningImageFormatTypeDef] = None
    maxSizeInMB: Optional[int] = None
    revocationSupported: Optional[bool] = None

class SigningJobTypeDef(BaseValidatorModel):
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

class StartSigningJobRequestRequestTypeDef(BaseValidatorModel):
    source: SourceTypeDef
    destination: DestinationTypeDef
    profileName: str
    clientRequestToken: str
    profileOwner: Optional[str] = None

class DescribeSigningJobResponseTypeDef(BaseValidatorModel):
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

class GetSigningProfileResponseTypeDef(BaseValidatorModel):
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

class PutSigningProfileRequestRequestTypeDef(BaseValidatorModel):
    profileName: str
    platformId: str
    signingMaterial: Optional[SigningMaterialTypeDef] = None
    signatureValidityPeriod: Optional[SignatureValidityPeriodTypeDef] = None
    overrides: Optional[SigningPlatformOverridesTypeDef] = None
    signingParameters: Optional[Mapping[str, str]] = None
    tags: Optional[Mapping[str, str]] = None

class ListSigningPlatformsResponseTypeDef(BaseValidatorModel):
    platforms: List[SigningPlatformTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[SigningJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

