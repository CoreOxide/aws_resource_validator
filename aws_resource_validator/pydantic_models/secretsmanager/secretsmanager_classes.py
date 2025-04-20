from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.secretsmanager.secretsmanager_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class APIErrorType(BaseValidatorModel):
    SecretId: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class Filter(BaseValidatorModel):
    Key: Optional[FilterNameStringTypeType] = None
    Values: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SecretValueEntry(BaseValidatorModel):
    ARN: Optional[str] = None
    Name: Optional[str] = None
    VersionId: Optional[str] = None
    SecretBinary: Optional[bytes] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    CreatedDate: Optional[datetime] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelRotateSecretRequest(BaseValidatorModel):
    SecretId: str


class ReplicaRegionType(BaseValidatorModel):
    Region: Optional[str] = None
    KmsKeyId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ReplicationStatusType(BaseValidatorModel):
    Region: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Status: Optional[StatusTypeType] = None
    StatusMessage: Optional[str] = None
    LastAccessedDate: Optional[datetime] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    SecretId: str


class DeleteSecretRequest(BaseValidatorModel):
    SecretId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None


class DescribeSecretRequest(BaseValidatorModel):
    SecretId: str


class RotationRulesType(BaseValidatorModel):
    AutomaticallyAfterDays: Optional[int] = None
    Duration: Optional[str] = None
    ScheduleExpression: Optional[str] = None


class GetRandomPasswordRequest(BaseValidatorModel):
    PasswordLength: Optional[int] = None
    ExcludeCharacters: Optional[str] = None
    ExcludeNumbers: Optional[bool] = None
    ExcludePunctuation: Optional[bool] = None
    ExcludeUppercase: Optional[bool] = None
    ExcludeLowercase: Optional[bool] = None
    IncludeSpace: Optional[bool] = None
    RequireEachIncludedType: Optional[bool] = None


class GetResourcePolicyRequest(BaseValidatorModel):
    SecretId: str


class GetSecretValueRequest(BaseValidatorModel):
    SecretId: str
    VersionId: Optional[str] = None
    VersionStage: Optional[str] = None


class ListSecretVersionIdsRequest(BaseValidatorModel):
    SecretId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeDeprecated: Optional[bool] = None


class SecretVersionsListEntry(BaseValidatorModel):
    VersionId: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    LastAccessedDate: Optional[datetime] = None
    CreatedDate: Optional[datetime] = None
    KmsKeyIds: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    SecretId: str
    ResourcePolicy: str
    BlockPublicPolicy: Optional[bool] = None


class RemoveRegionsFromReplicationRequest(BaseValidatorModel):
    SecretId: str
    RemoveReplicaRegions: List[str]


class RestoreSecretRequest(BaseValidatorModel):
    SecretId: str


class StopReplicationToReplicaRequest(BaseValidatorModel):
    SecretId: str


class UntagResourceRequest(BaseValidatorModel):
    SecretId: str
    TagKeys: List[str]


class UpdateSecretVersionStageRequest(BaseValidatorModel):
    SecretId: str
    VersionStage: str
    RemoveFromVersionId: Optional[str] = None
    MoveToVersionId: Optional[str] = None


class ValidateResourcePolicyRequest(BaseValidatorModel):
    ResourcePolicy: str
    SecretId: Optional[str] = None


class ValidationErrorsEntry(BaseValidatorModel):
    CheckName: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchGetSecretValueRequest(BaseValidatorModel):
    SecretIdList: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSecretsRequest(BaseValidatorModel):
    IncludePlannedDeletion: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SortOrder: Optional[SortOrderTypeType] = None


class CancelRotateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


class DeleteResourcePolicyResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    DeletionDate: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetRandomPasswordResponse(BaseValidatorModel):
    RandomPassword: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadata


class GetSecretValueResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    SecretBinary: bytes
    SecretString: str
    VersionStages: List[str]
    CreatedDate: datetime
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


class PutSecretValueResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    VersionStages: List[str]
    ResponseMetadata: ResponseMetadata


class RestoreSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


class RotateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


class StopReplicationToReplicaResponse(BaseValidatorModel):
    ARN: str
    ResponseMetadata: ResponseMetadata


class UpdateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


class UpdateSecretVersionStageResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


class BatchGetSecretValueResponse(BaseValidatorModel):
    SecretValues: List[SecretValueEntry]
    Errors: List[APIErrorType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutSecretValueRequest(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    SecretBinary: Optional[Blob] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    RotationToken: Optional[str] = None


class UpdateSecretRequest(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[Blob] = None
    SecretString: Optional[str] = None


class ReplicateSecretToRegionsRequest(BaseValidatorModel):
    SecretId: str
    AddReplicaRegions: List[ReplicaRegionType]
    ForceOverwriteReplicaSecret: Optional[bool] = None


class CreateSecretRequest(BaseValidatorModel):
    Name: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[Blob] = None
    SecretString: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    AddReplicaRegions: Optional[List[ReplicaRegionType]] = None
    ForceOverwriteReplicaSecret: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    SecretId: str
    Tags: List[Tag]


class CreateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


class RemoveRegionsFromReplicationResponse(BaseValidatorModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


class ReplicateSecretToRegionsResponse(BaseValidatorModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


class DescribeSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    Description: str
    KmsKeyId: str
    RotationEnabled: bool
    RotationLambdaARN: str
    RotationRules: RotationRulesType
    LastRotatedDate: datetime
    LastChangedDate: datetime
    LastAccessedDate: datetime
    DeletedDate: datetime
    NextRotationDate: datetime
    Tags: List[Tag]
    VersionIdsToStages: Dict[str, List[str]]
    OwningService: str
    CreatedDate: datetime
    PrimaryRegion: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


class RotateSecretRequest(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    RotationLambdaARN: Optional[str] = None
    RotationRules: Optional[RotationRulesType] = None
    RotateImmediately: Optional[bool] = None


class SecretListEntry(BaseValidatorModel):
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = None
    RotationLambdaARN: Optional[str] = None
    RotationRules: Optional[RotationRulesType] = None
    LastRotatedDate: Optional[datetime] = None
    LastChangedDate: Optional[datetime] = None
    LastAccessedDate: Optional[datetime] = None
    DeletedDate: Optional[datetime] = None
    NextRotationDate: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    SecretVersionsToStages: Optional[Dict[str, List[str]]] = None
    OwningService: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    PrimaryRegion: Optional[str] = None


class ListSecretVersionIdsResponse(BaseValidatorModel):
    Versions: List[SecretVersionsListEntry]
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSecretsRequestPaginate(BaseValidatorModel):
    IncludePlannedDeletion: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    SortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ValidateResourcePolicyResponse(BaseValidatorModel):
    PolicyValidationPassed: bool
    ValidationErrors: List[ValidationErrorsEntry]
    ResponseMetadata: ResponseMetadata


class ListSecretsResponse(BaseValidatorModel):
    SecretList: List[SecretListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None