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
from aws_resource_validator.pydantic_models.secretsmanager_constants import *

class APIErrorTypeTypeDef(BaseModel):
    SecretId: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class FilterTypeDef(BaseModel):
    Key: Optional[FilterNameStringTypeType] = None
    Values: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SecretValueEntryTypeDef(BaseModel):
    ARN: Optional[str] = None
    Name: Optional[str] = None
    VersionId: Optional[str] = None
    SecretBinary: Optional[bytes] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    CreatedDate: Optional[datetime] = None

class CancelRotateSecretRequestRequestTypeDef(BaseModel):
    SecretId: str

class ReplicaRegionTypeTypeDef(BaseModel):
    Region: Optional[str] = None
    KmsKeyId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ReplicationStatusTypeTypeDef(BaseModel):
    Region: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Status: Optional[StatusTypeType] = None
    StatusMessage: Optional[str] = None
    LastAccessedDate: Optional[datetime] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    SecretId: str

class DeleteSecretRequestRequestTypeDef(BaseModel):
    SecretId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None

class DescribeSecretRequestRequestTypeDef(BaseModel):
    SecretId: str

class RotationRulesTypeTypeDef(BaseModel):
    AutomaticallyAfterDays: Optional[int] = None
    Duration: Optional[str] = None
    ScheduleExpression: Optional[str] = None

class GetRandomPasswordRequestRequestTypeDef(BaseModel):
    PasswordLength: Optional[int] = None
    ExcludeCharacters: Optional[str] = None
    ExcludeNumbers: Optional[bool] = None
    ExcludePunctuation: Optional[bool] = None
    ExcludeUppercase: Optional[bool] = None
    ExcludeLowercase: Optional[bool] = None
    IncludeSpace: Optional[bool] = None
    RequireEachIncludedType: Optional[bool] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    SecretId: str

class GetSecretValueRequestRequestTypeDef(BaseModel):
    SecretId: str
    VersionId: Optional[str] = None
    VersionStage: Optional[str] = None

class ListSecretVersionIdsRequestRequestTypeDef(BaseModel):
    SecretId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeDeprecated: Optional[bool] = None

class SecretVersionsListEntryTypeDef(BaseModel):
    VersionId: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    LastAccessedDate: Optional[datetime] = None
    CreatedDate: Optional[datetime] = None
    KmsKeyIds: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    SecretId: str
    ResourcePolicy: str
    BlockPublicPolicy: Optional[bool] = None

class RemoveRegionsFromReplicationRequestRequestTypeDef(BaseModel):
    SecretId: str
    RemoveReplicaRegions: Sequence[str]

class RestoreSecretRequestRequestTypeDef(BaseModel):
    SecretId: str

class StopReplicationToReplicaRequestRequestTypeDef(BaseModel):
    SecretId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    SecretId: str
    TagKeys: Sequence[str]

class UpdateSecretVersionStageRequestRequestTypeDef(BaseModel):
    SecretId: str
    VersionStage: str
    RemoveFromVersionId: Optional[str] = None
    MoveToVersionId: Optional[str] = None

class ValidateResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourcePolicy: str
    SecretId: Optional[str] = None

class ValidationErrorsEntryTypeDef(BaseModel):
    CheckName: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchGetSecretValueRequestRequestTypeDef(BaseModel):
    SecretIdList: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSecretsRequestRequestTypeDef(BaseModel):
    IncludePlannedDeletion: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortOrder: Optional[SortOrderTypeType] = None

class CancelRotateSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    DeletionDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRandomPasswordResponseTypeDef(BaseModel):
    RandomPassword: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecretValueResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    VersionId: str
    SecretBinary: bytes
    SecretString: str
    VersionStages: List[str]
    CreatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSecretValueResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    VersionId: str
    VersionStages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationToReplicaResponseTypeDef(BaseModel):
    ARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecretVersionStageResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetSecretValueResponseTypeDef(BaseModel):
    SecretValues: List[SecretValueEntryTypeDef]
    Errors: List[APIErrorTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutSecretValueRequestRequestTypeDef(BaseModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    SecretBinary: Optional[BlobTypeDef] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[Sequence[str]] = None
    RotationToken: Optional[str] = None

class UpdateSecretRequestRequestTypeDef(BaseModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[BlobTypeDef] = None
    SecretString: Optional[str] = None

class ReplicateSecretToRegionsRequestRequestTypeDef(BaseModel):
    SecretId: str
    AddReplicaRegions: Sequence[ReplicaRegionTypeTypeDef]
    ForceOverwriteReplicaSecret: Optional[bool] = None

class CreateSecretRequestRequestTypeDef(BaseModel):
    Name: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[BlobTypeDef] = None
    SecretString: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AddReplicaRegions: Optional[Sequence[ReplicaRegionTypeTypeDef]] = None
    ForceOverwriteReplicaSecret: Optional[bool] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    SecretId: str
    Tags: Sequence[TagTypeDef]

class CreateSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    VersionId: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveRegionsFromReplicationResponseTypeDef(BaseModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateSecretToRegionsResponseTypeDef(BaseModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecretResponseTypeDef(BaseModel):
    ARN: str
    Name: str
    Description: str
    KmsKeyId: str
    RotationEnabled: bool
    RotationLambdaARN: str
    RotationRules: RotationRulesTypeTypeDef
    LastRotatedDate: datetime
    LastChangedDate: datetime
    LastAccessedDate: datetime
    DeletedDate: datetime
    NextRotationDate: datetime
    Tags: List[TagTypeDef]
    VersionIdsToStages: Dict[str, List[str]]
    OwningService: str
    CreatedDate: datetime
    PrimaryRegion: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RotateSecretRequestRequestTypeDef(BaseModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    RotationLambdaARN: Optional[str] = None
    RotationRules: Optional[RotationRulesTypeTypeDef] = None
    RotateImmediately: Optional[bool] = None

class SecretListEntryTypeDef(BaseModel):
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = None
    RotationLambdaARN: Optional[str] = None
    RotationRules: Optional[RotationRulesTypeTypeDef] = None
    LastRotatedDate: Optional[datetime] = None
    LastChangedDate: Optional[datetime] = None
    LastAccessedDate: Optional[datetime] = None
    DeletedDate: Optional[datetime] = None
    NextRotationDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    SecretVersionsToStages: Optional[Dict[str, List[str]]] = None
    OwningService: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    PrimaryRegion: Optional[str] = None

class ListSecretVersionIdsResponseTypeDef(BaseModel):
    Versions: List[SecretVersionsListEntryTypeDef]
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecretsRequestListSecretsPaginateTypeDef(BaseModel):
    IncludePlannedDeletion: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ValidateResourcePolicyResponseTypeDef(BaseModel):
    PolicyValidationPassed: bool
    ValidationErrors: List[ValidationErrorsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecretsResponseTypeDef(BaseModel):
    SecretList: List[SecretListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

