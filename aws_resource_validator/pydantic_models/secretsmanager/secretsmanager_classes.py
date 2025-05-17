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


# This class is the input for the 'cancel_rotate_secret' function.
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


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    SecretId: str


# This class is the input for the 'delete_secret' function.
class DeleteSecretRequest(BaseValidatorModel):
    SecretId: str
    RecoveryWindowInDays: Optional[int] = None
    ForceDeleteWithoutRecovery: Optional[bool] = None


# This class is the input for the 'describe_secret' function.
class DescribeSecretRequest(BaseValidatorModel):
    SecretId: str


class RotationRulesType(BaseValidatorModel):
    AutomaticallyAfterDays: Optional[int] = None
    Duration: Optional[str] = None
    ScheduleExpression: Optional[str] = None


# This class is the input for the 'get_random_password' function.
class GetRandomPasswordRequest(BaseValidatorModel):
    PasswordLength: Optional[int] = None
    ExcludeCharacters: Optional[str] = None
    ExcludeNumbers: Optional[bool] = None
    ExcludePunctuation: Optional[bool] = None
    ExcludeUppercase: Optional[bool] = None
    ExcludeLowercase: Optional[bool] = None
    IncludeSpace: Optional[bool] = None
    RequireEachIncludedType: Optional[bool] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    SecretId: str


# This class is the input for the 'get_secret_value' function.
class GetSecretValueRequest(BaseValidatorModel):
    SecretId: str
    VersionId: Optional[str] = None
    VersionStage: Optional[str] = None


# This class is the input for the 'list_secret_version_ids' function.
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


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    SecretId: str
    ResourcePolicy: str
    BlockPublicPolicy: Optional[bool] = None


# This class is the input for the 'remove_regions_from_replication' function.
class RemoveRegionsFromReplicationRequest(BaseValidatorModel):
    SecretId: str
    RemoveReplicaRegions: List[str]


# This class is the input for the 'restore_secret' function.
class RestoreSecretRequest(BaseValidatorModel):
    SecretId: str


# This class is the input for the 'stop_replication_to_replica' function.
class StopReplicationToReplicaRequest(BaseValidatorModel):
    SecretId: str


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    SecretId: str
    TagKeys: List[str]


# This class is the input for the 'update_secret_version_stage' function.
class UpdateSecretVersionStageRequest(BaseValidatorModel):
    SecretId: str
    VersionStage: str
    RemoveFromVersionId: Optional[str] = None
    MoveToVersionId: Optional[str] = None


# This class is the input for the 'validate_resource_policy' function.
class ValidateResourcePolicyRequest(BaseValidatorModel):
    ResourcePolicy: str
    SecretId: Optional[str] = None


class ValidationErrorsEntry(BaseValidatorModel):
    CheckName: Optional[str] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'batch_get_secret_value' function.
class BatchGetSecretValueRequest(BaseValidatorModel):
    SecretIdList: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_secrets' function.
class ListSecretsRequest(BaseValidatorModel):
    IncludePlannedDeletion: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SortOrder: Optional[SortOrderTypeType] = None


# This class is the output for the 'cancel_rotate_secret' function.
class CancelRotateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_policy' function.
class DeleteResourcePolicyResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_secret' function.
class DeleteSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    DeletionDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_random_password' function.
class GetRandomPasswordResponse(BaseValidatorModel):
    RandomPassword: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_secret_value' function.
class GetSecretValueResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    SecretBinary: bytes
    SecretString: str
    VersionStages: List[str]
    CreatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_secret_value' function.
class PutSecretValueResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    VersionStages: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_secret' function.
class RestoreSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rotate_secret' function.
class RotateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_replication_to_replica' function.
class StopReplicationToReplicaResponse(BaseValidatorModel):
    ARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_secret' function.
class UpdateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_secret_version_stage' function.
class UpdateSecretVersionStageResponse(BaseValidatorModel):
    ARN: str
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_secret_value' function.
class BatchGetSecretValueResponse(BaseValidatorModel):
    SecretValues: List[SecretValueEntry]
    Errors: List[APIErrorType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'put_secret_value' function.
class PutSecretValueRequest(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    SecretBinary: Optional[Blob] = None
    SecretString: Optional[str] = None
    VersionStages: Optional[List[str]] = None
    RotationToken: Optional[str] = None


# This class is the input for the 'update_secret' function.
class UpdateSecretRequest(BaseValidatorModel):
    SecretId: str
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretBinary: Optional[Blob] = None
    SecretString: Optional[str] = None


# This class is the input for the 'replicate_secret_to_regions' function.
class ReplicateSecretToRegionsRequest(BaseValidatorModel):
    SecretId: str
    AddReplicaRegions: List[ReplicaRegionType]
    ForceOverwriteReplicaSecret: Optional[bool] = None


# This class is the input for the 'create_secret' function.
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


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    SecretId: str
    Tags: List[Tag]


# This class is the output for the 'create_secret' function.
class CreateSecretResponse(BaseValidatorModel):
    ARN: str
    Name: str
    VersionId: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_regions_from_replication' function.
class RemoveRegionsFromReplicationResponse(BaseValidatorModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replicate_secret_to_regions' function.
class ReplicateSecretToRegionsResponse(BaseValidatorModel):
    ARN: str
    ReplicationStatus: List[ReplicationStatusType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_secret' function.
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


# This class is the input for the 'rotate_secret' function.
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


# This class is the output for the 'list_secret_version_ids' function.
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


# This class is the output for the 'validate_resource_policy' function.
class ValidateResourcePolicyResponse(BaseValidatorModel):
    PolicyValidationPassed: bool
    ValidationErrors: List[ValidationErrorsEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_secrets' function.
class ListSecretsResponse(BaseValidatorModel):
    SecretList: List[SecretListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None