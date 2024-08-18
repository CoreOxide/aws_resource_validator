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
from aws_resource_validator.pydantic_models.secretsmanager_constants import *

class APIErrorTypeTypeDef(BaseValidatorModel):
    SecretId: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    Key: Optional[FilterNameStringTypeType] = None
    Values: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SecretValueEntryTypeDef(BaseValidatorModel):
    ARN: Optional[str] = None
    Name: Optional[str] = None
    VersionId: Optional[str] = None
    SecretBinary: Optional[bytes] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    CreatedDate: Optional[datetime] = None

class CancelRotateSecretRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str

class ReplicaRegionTypeTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    KmsKeyId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ReplicationStatusTypeTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Status: Optional[StatusTypeType] = None
    StatusMessage: Optional[str] = None
    LastAccessedDate: Optional[datetime] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str

class DeleteSecretRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None

class DescribeSecretRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str

class RotationRulesTypeTypeDef(BaseValidatorModel):
    AutomaticallyAfterDays: Optional[int] = None
    Duration: Optional[str] = None
    ScheduleExpression: Optional[str] = None

class GetRandomPasswordRequestRequestTypeDef(BaseValidatorModel):
    PasswordLength: Optional[int] = None
    ExcludeCharacters: Optional[str] = None
    ExcludeNumbers: Optional[bool] = None
    ExcludePunctuation: Optional[bool] = None
    ExcludeUppercase: Optional[bool] = None
    ExcludeLowercase: Optional[bool] = None
    IncludeSpace: Optional[bool] = None
    RequireEachIncludedType: Optional[bool] = None

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str

class GetSecretValueRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    VersionId: Optional[str] = None
    VersionStage: Optional[str] = None

class ListSecretVersionIdsRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeDeprecated: Optional[bool] = None

class SecretVersionsListEntryTypeDef(BaseValidatorModel):
    VersionId: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    LastAccessedDate: Optional[datetime] = None
    CreatedDate: Optional[datetime] = None
    KmsKeyIds: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    ResourcePolicy: str
    BlockPublicPolicy: Optional[bool] = None

class RemoveRegionsFromReplicationRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    RemoveReplicaRegions: Sequence[str]

class RestoreSecretRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str

class StopReplicationToReplicaRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    TagKeys: Sequence[str]

class UpdateSecretVersionStageRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    VersionStage: str
    RemoveFromVersionId: Optional[str] = None
    MoveToVersionId: Optional[str] = None

class ValidateResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourcePolicy: str
    SecretId: Optional[str] = None

class ValidationErrorsEntryTypeDef(BaseValidatorModel):
    CheckName: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchGetSecretValueRequestRequestTypeDef(BaseValidatorModel):
    SecretIdList: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSecretsRequestRequestTypeDef(BaseValidatorModel):
    IncludePlannedDeletion: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortOrder: Optional[SortOrderTypeType] = None

class CancelRotateSecretResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSecretResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    DeletionDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRandomPasswordResponseTypeDef(BaseValidatorModel):
    RandomPassword: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecretValueResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    SecretBinary: bytes
    SecretString: str
    VersionStages: List[str]
    CreatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSecretValueResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    VersionStages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSecretResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateSecretResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationToReplicaResponseTypeDef(BaseValidatorModel):
    ARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecretResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecretVersionStageResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetSecretValueResponseTypeDef(BaseValidatorModel):
    SecretValues: List[SecretValueEntryTypeDef]
    Errors: List[APIErrorTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutSecretValueRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    SecretBinary: Optional[BlobTypeDef] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[Sequence[str]] = None
    RotationToken: Optional[str] = None

class UpdateSecretRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[BlobTypeDef] = None
    SecretString: Optional[str] = None

class ReplicateSecretToRegionsRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    AddReplicaRegions: Sequence[ReplicaRegionTypeTypeDef]
    ForceOverwriteReplicaSecret: Optional[bool] = None

class CreateSecretRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[BlobTypeDef] = None
    SecretString: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AddReplicaRegions: Optional[Sequence[ReplicaRegionTypeTypeDef]] = None
    ForceOverwriteReplicaSecret: Optional[bool] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    Tags: Sequence[TagTypeDef]

class CreateSecretResponseTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveRegionsFromReplicationResponseTypeDef(BaseValidatorModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateSecretToRegionsResponseTypeDef(BaseValidatorModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecretResponseTypeDef(BaseValidatorModel):
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

class RotateSecretRequestRequestTypeDef(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    RotationLambdaARN: Optional[str] = None
    RotationRules: Optional[RotationRulesTypeTypeDef] = None
    RotateImmediately: Optional[bool] = None

class SecretListEntryTypeDef(BaseValidatorModel):
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

class ListSecretVersionIdsResponseTypeDef(BaseValidatorModel):
    Versions: List[SecretVersionsListEntryTypeDef]
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecretsRequestListSecretsPaginateTypeDef(BaseValidatorModel):
    IncludePlannedDeletion: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ValidateResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyValidationPassed: bool
    ValidationErrors: List[ValidationErrorsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecretsResponseTypeDef(BaseValidatorModel):
    SecretList: List[SecretListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

