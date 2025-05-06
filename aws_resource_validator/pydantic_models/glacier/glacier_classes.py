from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.glacier.glacier_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbortMultipartUploadInput(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None


class AbortVaultLockInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class AddTagsToVaultInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CSVInput(BaseValidatorModel):
    FileHeaderInfo: Optional[FileHeaderInfoType] = None
    Comments: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None


class CSVOutput(BaseValidatorModel):
    QuoteFields: Optional[QuoteFieldsType] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None


class CompleteMultipartUploadInputMultipartUploadComplete(BaseValidatorModel):
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None


class CompleteMultipartUploadInput(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None


class CompleteVaultLockInput(BaseValidatorModel):
    vaultName: str
    lockId: str
    accountId: Optional[str] = None


class CreateVaultInputAccountCreateVault(BaseValidatorModel):
    vaultName: str


class CreateVaultInputServiceResourceCreateVault(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class CreateVaultInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DataRetrievalRule(BaseValidatorModel):
    Strategy: Optional[str] = None
    BytesPerHour: Optional[int] = None


class DeleteArchiveInput(BaseValidatorModel):
    vaultName: str
    archiveId: str
    accountId: Optional[str] = None


class DeleteVaultAccessPolicyInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DeleteVaultInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DeleteVaultNotificationsInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DescribeJobInput(BaseValidatorModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None


class DescribeVaultInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeVaultOutput(BaseValidatorModel):
    VaultARN: Optional[str] = None
    VaultName: Optional[str] = None
    CreationDate: Optional[str] = None
    LastInventoryDate: Optional[str] = None
    NumberOfArchives: Optional[int] = None
    SizeInBytes: Optional[int] = None


class Encryption(BaseValidatorModel):
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None


class GetDataRetrievalPolicyInput(BaseValidatorModel):
    accountId: Optional[str] = None


class GetJobOutputInputJobGetOutput(BaseValidatorModel):
    range: Optional[str] = None


class GetJobOutputInput(BaseValidatorModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None
    range: Optional[str] = None


class GetVaultAccessPolicyInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class VaultAccessPolicy(BaseValidatorModel):
    Policy: Optional[str] = None


class GetVaultLockInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class GetVaultNotificationsInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class VaultNotificationConfigOutput(BaseValidatorModel):
    SNSTopic: Optional[str] = None
    Events: Optional[List[str]] = None


class InventoryRetrievalJobDescription(BaseValidatorModel):
    Format: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None


class Grantee(BaseValidatorModel):
    Type: TypeType
    DisplayName: Optional[str] = None
    URI: Optional[str] = None
    ID: Optional[str] = None
    EmailAddress: Optional[str] = None


class InitiateMultipartUploadInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    partSize: Optional[str] = None


class InitiateMultipartUploadInputVaultInitiateMultipartUpload(BaseValidatorModel):
    archiveDescription: Optional[str] = None
    partSize: Optional[str] = None


class VaultLockPolicy(BaseValidatorModel):
    Policy: Optional[str] = None


class InventoryRetrievalJobInput(BaseValidatorModel):
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListJobsInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    limit: Optional[str] = None
    marker: Optional[str] = None
    statuscode: Optional[str] = None
    completed: Optional[str] = None


class ListMultipartUploadsInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None


class UploadListElement(BaseValidatorModel):
    MultipartUploadId: Optional[str] = None
    VaultARN: Optional[str] = None
    ArchiveDescription: Optional[str] = None
    PartSizeInBytes: Optional[int] = None
    CreationDate: Optional[str] = None


class ListPartsInputMultipartUploadParts(BaseValidatorModel):
    marker: Optional[str] = None
    limit: Optional[str] = None


class ListPartsInput(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None


class PartListElement(BaseValidatorModel):
    RangeInBytes: Optional[str] = None
    SHA256TreeHash: Optional[str] = None


class ListProvisionedCapacityInput(BaseValidatorModel):
    accountId: Optional[str] = None


class ProvisionedCapacityDescription(BaseValidatorModel):
    CapacityId: Optional[str] = None
    StartDate: Optional[str] = None
    ExpirationDate: Optional[str] = None


class ListTagsForVaultInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class ListVaultsInput(BaseValidatorModel):
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None


class PurchaseProvisionedCapacityInput(BaseValidatorModel):
    accountId: Optional[str] = None


class RemoveTagsFromVaultInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    TagKeys: Optional[List[str]] = None


class VaultNotificationConfig(BaseValidatorModel):
    SNSTopic: Optional[str] = None
    Events: Optional[List[str]] = None


class ArchiveCreationOutput(BaseValidatorModel):
    location: str
    checksum: str
    archiveId: str
    ResponseMetadata: ResponseMetadata


class CreateVaultOutput(BaseValidatorModel):
    location: str
    ResponseMetadata: ResponseMetadata


class DescribeVaultResponse(BaseValidatorModel):
    VaultARN: str
    VaultName: str
    CreationDate: str
    LastInventoryDate: str
    NumberOfArchives: int
    SizeInBytes: int
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetJobOutputOutput(BaseValidatorModel):
    body: StreamingBody
    checksum: str
    status: int
    contentRange: str
    acceptRanges: str
    contentType: str
    archiveDescription: str
    ResponseMetadata: ResponseMetadata


class GetVaultLockOutput(BaseValidatorModel):
    Policy: str
    State: str
    ExpirationDate: str
    CreationDate: str
    ResponseMetadata: ResponseMetadata


class InitiateJobOutput(BaseValidatorModel):
    location: str
    jobId: str
    jobOutputPath: str
    ResponseMetadata: ResponseMetadata


class InitiateMultipartUploadOutput(BaseValidatorModel):
    location: str
    uploadId: str
    ResponseMetadata: ResponseMetadata


class InitiateVaultLockOutput(BaseValidatorModel):
    lockId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForVaultOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PurchaseProvisionedCapacityOutput(BaseValidatorModel):
    capacityId: str
    ResponseMetadata: ResponseMetadata


class UploadMultipartPartOutput(BaseValidatorModel):
    checksum: str
    ResponseMetadata: ResponseMetadata


class UploadArchiveInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[Blob] = None


class UploadArchiveInputVaultUploadArchive(BaseValidatorModel):
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[Blob] = None


class UploadMultipartPartInputMultipartUploadUploadPart(BaseValidatorModel):
    checksum: Optional[str] = None
    range: Optional[str] = None
    body: Optional[Blob] = None


class UploadMultipartPartInput(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    checksum: Optional[str] = None
    range: Optional[str] = None
    body: Optional[Blob] = None


class InputSerialization(BaseValidatorModel):
    csv: Optional[CSVInput] = None


class OutputSerialization(BaseValidatorModel):
    csv: Optional[CSVOutput] = None


class DataRetrievalPolicyOutput(BaseValidatorModel):
    Rules: Optional[List[DataRetrievalRule]] = None


class DataRetrievalPolicy(BaseValidatorModel):
    Rules: Optional[List[DataRetrievalRule]] = None


class DescribeVaultInputWaitExtra(BaseValidatorModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVaultInputWait(BaseValidatorModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListVaultsOutput(BaseValidatorModel):
    VaultList: List[DescribeVaultOutput]
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetVaultAccessPolicyOutput(BaseValidatorModel):
    policy: VaultAccessPolicy
    ResponseMetadata: ResponseMetadata


class SetVaultAccessPolicyInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultAccessPolicy] = None


class GetVaultNotificationsOutput(BaseValidatorModel):
    vaultNotificationConfig: VaultNotificationConfigOutput
    ResponseMetadata: ResponseMetadata


class Grant(BaseValidatorModel):
    Grantee: Optional[Grantee] = None
    Permission: Optional[PermissionType] = None


class InitiateVaultLockInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultLockPolicy] = None


class ListJobsInputPaginate(BaseValidatorModel):
    accountId: str
    vaultName: str
    statuscode: Optional[str] = None
    completed: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultipartUploadsInputPaginate(BaseValidatorModel):
    accountId: str
    vaultName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPartsInputPaginate(BaseValidatorModel):
    accountId: str
    vaultName: str
    uploadId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVaultsInputPaginate(BaseValidatorModel):
    accountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultipartUploadsOutput(BaseValidatorModel):
    UploadsList: List[UploadListElement]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListPartsOutput(BaseValidatorModel):
    MultipartUploadId: str
    VaultARN: str
    ArchiveDescription: str
    PartSizeInBytes: int
    CreationDate: str
    Parts: List[PartListElement]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListProvisionedCapacityOutput(BaseValidatorModel):
    ProvisionedCapacityList: List[ProvisionedCapacityDescription]
    ResponseMetadata: ResponseMetadata

VaultNotificationConfigUnion = Union[VaultNotificationConfig, VaultNotificationConfigOutput]


class SelectParameters(BaseValidatorModel):
    InputSerialization: Optional[InputSerialization] = None
    ExpressionType: Optional[Literal['SQL']] = None
    Expression: Optional[str] = None
    OutputSerialization: Optional[OutputSerialization] = None


class GetDataRetrievalPolicyOutput(BaseValidatorModel):
    Policy: DataRetrievalPolicyOutput
    ResponseMetadata: ResponseMetadata

DataRetrievalPolicyUnion = Union[DataRetrievalPolicy, DataRetrievalPolicyOutput]


class S3LocationOutput(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[Encryption] = None
    CannedACL: Optional[CannedACLType] = None
    AccessControlList: Optional[List[Grant]] = None
    Tagging: Optional[Dict[str, str]] = None
    UserMetadata: Optional[Dict[str, str]] = None
    StorageClass: Optional[StorageClassType] = None


class S3Location(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[Encryption] = None
    CannedACL: Optional[CannedACLType] = None
    AccessControlList: Optional[List[Grant]] = None
    Tagging: Optional[Dict[str, str]] = None
    UserMetadata: Optional[Dict[str, str]] = None
    StorageClass: Optional[StorageClassType] = None


class SetVaultNotificationsInputNotificationSet(BaseValidatorModel):
    vaultNotificationConfig: Optional[VaultNotificationConfigUnion] = None


class SetVaultNotificationsInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    vaultNotificationConfig: Optional[VaultNotificationConfigUnion] = None


class SetDataRetrievalPolicyInput(BaseValidatorModel):
    accountId: Optional[str] = None
    Policy: Optional[DataRetrievalPolicyUnion] = None


class OutputLocationOutput(BaseValidatorModel):
    S3: Optional[S3LocationOutput] = None

S3LocationUnion = Union[S3Location, S3LocationOutput]


class GlacierJobDescriptionResponse(BaseValidatorModel):
    JobId: str
    JobDescription: str
    Action: ActionCodeType
    ArchiveId: str
    VaultARN: str
    CreationDate: str
    Completed: bool
    StatusCode: StatusCodeType
    StatusMessage: str
    ArchiveSizeInBytes: int
    InventorySizeInBytes: int
    SNSTopic: str
    CompletionDate: str
    SHA256TreeHash: str
    ArchiveSHA256TreeHash: str
    RetrievalByteRange: str
    Tier: str
    InventoryRetrievalParameters: InventoryRetrievalJobDescription
    JobOutputPath: str
    SelectParameters: SelectParameters
    OutputLocation: OutputLocationOutput
    ResponseMetadata: ResponseMetadata


class GlacierJobDescription(BaseValidatorModel):
    JobId: Optional[str] = None
    JobDescription: Optional[str] = None
    Action: Optional[ActionCodeType] = None
    ArchiveId: Optional[str] = None
    VaultARN: Optional[str] = None
    CreationDate: Optional[str] = None
    Completed: Optional[bool] = None
    StatusCode: Optional[StatusCodeType] = None
    StatusMessage: Optional[str] = None
    ArchiveSizeInBytes: Optional[int] = None
    InventorySizeInBytes: Optional[int] = None
    SNSTopic: Optional[str] = None
    CompletionDate: Optional[str] = None
    SHA256TreeHash: Optional[str] = None
    ArchiveSHA256TreeHash: Optional[str] = None
    RetrievalByteRange: Optional[str] = None
    Tier: Optional[str] = None
    InventoryRetrievalParameters: Optional[InventoryRetrievalJobDescription] = None
    JobOutputPath: Optional[str] = None
    SelectParameters: Optional[SelectParameters] = None
    OutputLocation: Optional[OutputLocationOutput] = None


class OutputLocation(BaseValidatorModel):
    S3: Optional[S3LocationUnion] = None


class ListJobsOutput(BaseValidatorModel):
    JobList: List[GlacierJobDescription]
    Marker: str
    ResponseMetadata: ResponseMetadata

OutputLocationUnion = Union[OutputLocation, OutputLocationOutput]


class JobParameters(BaseValidatorModel):
    Format: Optional[str] = None
    Type: Optional[str] = None
    ArchiveId: Optional[str] = None
    Description: Optional[str] = None
    SNSTopic: Optional[str] = None
    RetrievalByteRange: Optional[str] = None
    Tier: Optional[str] = None
    InventoryRetrievalParameters: Optional[InventoryRetrievalJobInput] = None
    SelectParameters: Optional[SelectParameters] = None
    OutputLocation: Optional[OutputLocationUnion] = None


class InitiateJobInput(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    jobParameters: Optional[JobParameters] = None