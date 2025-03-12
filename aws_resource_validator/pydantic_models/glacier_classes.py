from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.glacier_constants import *

class AbortMultipartUploadInputTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None


class AbortVaultLockInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class AddTagsToVaultInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CSVInputTypeDef(BaseValidatorModel):
    FileHeaderInfo: Optional[FileHeaderInfoType] = None
    Comments: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None


class CSVOutputTypeDef(BaseValidatorModel):
    QuoteFields: Optional[QuoteFieldsType] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None


class CompleteMultipartUploadInputMultipartUploadCompleteTypeDef(BaseValidatorModel):
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None


class CompleteMultipartUploadInputTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None


class CompleteVaultLockInputTypeDef(BaseValidatorModel):
    vaultName: str
    lockId: str
    accountId: Optional[str] = None


class CreateVaultInputAccountCreateVaultTypeDef(BaseValidatorModel):
    vaultName: str


class CreateVaultInputServiceResourceCreateVaultTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class CreateVaultInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DataRetrievalRuleTypeDef(BaseValidatorModel):
    Strategy: Optional[str] = None
    BytesPerHour: Optional[int] = None


class DeleteArchiveInputTypeDef(BaseValidatorModel):
    vaultName: str
    archiveId: str
    accountId: Optional[str] = None


class DeleteVaultAccessPolicyInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DeleteVaultInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DeleteVaultNotificationsInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class DescribeJobInputTypeDef(BaseValidatorModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None


class DescribeVaultInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeVaultOutputTypeDef(BaseValidatorModel):
    VaultARN: Optional[str] = None
    VaultName: Optional[str] = None
    CreationDate: Optional[str] = None
    LastInventoryDate: Optional[str] = None
    NumberOfArchives: Optional[int] = None
    SizeInBytes: Optional[int] = None


class EncryptionTypeDef(BaseValidatorModel):
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None


class GetDataRetrievalPolicyInputTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class GetVaultAccessPolicyInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class VaultAccessPolicyTypeDef(BaseValidatorModel):
    Policy: Optional[str] = None


class GetVaultLockInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class GetVaultNotificationsInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class VaultNotificationConfigOutputTypeDef(BaseValidatorModel):
    SNSTopic: Optional[str] = None
    Events: Optional[List[str]] = None


class InventoryRetrievalJobDescriptionTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None


class InitiateMultipartUploadInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    partSize: Optional[str] = None


class InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef(BaseValidatorModel):
    archiveDescription: Optional[str] = None
    partSize: Optional[str] = None


class VaultLockPolicyTypeDef(BaseValidatorModel):
    Policy: Optional[str] = None


class InventoryRetrievalJobInputTypeDef(BaseValidatorModel):
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListJobsInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    limit: Optional[str] = None
    marker: Optional[str] = None
    statuscode: Optional[str] = None
    completed: Optional[str] = None


class ListMultipartUploadsInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None


class UploadListElementTypeDef(BaseValidatorModel):
    MultipartUploadId: Optional[str] = None
    VaultARN: Optional[str] = None
    ArchiveDescription: Optional[str] = None
    PartSizeInBytes: Optional[int] = None
    CreationDate: Optional[str] = None


class ListPartsInputMultipartUploadPartsTypeDef(BaseValidatorModel):
    marker: Optional[str] = None
    limit: Optional[str] = None


class ListPartsInputTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None


class PartListElementTypeDef(BaseValidatorModel):
    RangeInBytes: Optional[str] = None
    SHA256TreeHash: Optional[str] = None


class ListProvisionedCapacityInputTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class ProvisionedCapacityDescriptionTypeDef(BaseValidatorModel):
    CapacityId: Optional[str] = None
    StartDate: Optional[str] = None
    ExpirationDate: Optional[str] = None


class ListTagsForVaultInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None


class ListVaultsInputTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None


class PurchaseProvisionedCapacityInputTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class RemoveTagsFromVaultInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None


class VaultNotificationConfigTypeDef(BaseValidatorModel):
    SNSTopic: Optional[str] = None
    Events: Optional[Sequence[str]] = None


class ArchiveCreationOutputTypeDef(BaseValidatorModel):
    location: str
    checksum: str
    archiveId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVaultOutputTypeDef(BaseValidatorModel):
    location: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVaultResponseTypeDef(BaseValidatorModel):
    VaultARN: str
    VaultName: str
    CreationDate: str
    LastInventoryDate: str
    NumberOfArchives: int
    SizeInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobOutputOutputTypeDef(BaseValidatorModel):
    body: StreamingBody
    checksum: str
    status: int
    contentRange: str
    acceptRanges: str
    contentType: str
    archiveDescription: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetVaultLockOutputTypeDef(BaseValidatorModel):
    Policy: str
    State: str
    ExpirationDate: str
    CreationDate: str
    ResponseMetadata: ResponseMetadataTypeDef


class InitiateJobOutputTypeDef(BaseValidatorModel):
    location: str
    jobId: str
    jobOutputPath: str
    ResponseMetadata: ResponseMetadataTypeDef


class InitiateMultipartUploadOutputTypeDef(BaseValidatorModel):
    location: str
    uploadId: str
    ResponseMetadata: ResponseMetadataTypeDef


class InitiateVaultLockOutputTypeDef(BaseValidatorModel):
    lockId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForVaultOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PurchaseProvisionedCapacityOutputTypeDef(BaseValidatorModel):
    capacityId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UploadMultipartPartOutputTypeDef(BaseValidatorModel):
    checksum: str
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class UploadArchiveInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[BlobTypeDef] = None


class UploadArchiveInputVaultUploadArchiveTypeDef(BaseValidatorModel):
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[BlobTypeDef] = None


class InputSerializationTypeDef(BaseValidatorModel):
    csv: Optional[CSVInputTypeDef] = None


class OutputSerializationTypeDef(BaseValidatorModel):
    csv: Optional[CSVOutputTypeDef] = None


class DataRetrievalPolicyOutputTypeDef(BaseValidatorModel):
    Rules: Optional[List[DataRetrievalRuleTypeDef]] = None


class DataRetrievalPolicyTypeDef(BaseValidatorModel):
    Rules: Optional[Sequence[DataRetrievalRuleTypeDef]] = None


class DescribeVaultInputWaitExtraTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeVaultInputWaitTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class ListVaultsOutputTypeDef(BaseValidatorModel):
    VaultList: List[DescribeVaultOutputTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetVaultAccessPolicyOutputTypeDef(BaseValidatorModel):
    policy: VaultAccessPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetVaultAccessPolicyInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultAccessPolicyTypeDef] = None


class GetVaultNotificationsOutputTypeDef(BaseValidatorModel):
    vaultNotificationConfig: VaultNotificationConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GranteeTypeDef(BaseValidatorModel):
    pass


class GrantTypeDef(BaseValidatorModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None


class InitiateVaultLockInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultLockPolicyTypeDef] = None


class ListJobsInputPaginateTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    statuscode: Optional[str] = None
    completed: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMultipartUploadsInputPaginateTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPartsInputPaginateTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    uploadId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVaultsInputPaginateTypeDef(BaseValidatorModel):
    accountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMultipartUploadsOutputTypeDef(BaseValidatorModel):
    UploadsList: List[UploadListElementTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPartsOutputTypeDef(BaseValidatorModel):
    MultipartUploadId: str
    VaultARN: str
    ArchiveDescription: str
    PartSizeInBytes: int
    CreationDate: str
    Parts: List[PartListElementTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListProvisionedCapacityOutputTypeDef(BaseValidatorModel):
    ProvisionedCapacityList: List[ProvisionedCapacityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SelectParametersTypeDef(BaseValidatorModel):
    InputSerialization: Optional[InputSerializationTypeDef] = None
    ExpressionType: Optional[Literal["SQL"]] = None
    Expression: Optional[str] = None
    OutputSerialization: Optional[OutputSerializationTypeDef] = None


class GetDataRetrievalPolicyOutputTypeDef(BaseValidatorModel):
    Policy: DataRetrievalPolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class S3LocationOutputTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    CannedACL: Optional[CannedACLType] = None
    AccessControlList: Optional[List[GrantTypeDef]] = None
    Tagging: Optional[Dict[str, str]] = None
    UserMetadata: Optional[Dict[str, str]] = None
    StorageClass: Optional[StorageClassType] = None


class S3LocationTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    CannedACL: Optional[CannedACLType] = None
    AccessControlList: Optional[Sequence[GrantTypeDef]] = None
    Tagging: Optional[Mapping[str, str]] = None
    UserMetadata: Optional[Mapping[str, str]] = None
    StorageClass: Optional[StorageClassType] = None


class VaultNotificationConfigUnionTypeDef(BaseValidatorModel):
    pass


class SetVaultNotificationsInputNotificationSetTypeDef(BaseValidatorModel):
    vaultNotificationConfig: Optional[VaultNotificationConfigUnionTypeDef] = None


class SetVaultNotificationsInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    vaultNotificationConfig: Optional[VaultNotificationConfigUnionTypeDef] = None


class DataRetrievalPolicyUnionTypeDef(BaseValidatorModel):
    pass


class SetDataRetrievalPolicyInputTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    Policy: Optional[DataRetrievalPolicyUnionTypeDef] = None


class OutputLocationOutputTypeDef(BaseValidatorModel):
    S3: Optional[S3LocationOutputTypeDef] = None


class GlacierJobDescriptionResponseTypeDef(BaseValidatorModel):
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
    InventoryRetrievalParameters: InventoryRetrievalJobDescriptionTypeDef
    JobOutputPath: str
    SelectParameters: SelectParametersTypeDef
    OutputLocation: OutputLocationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GlacierJobDescriptionTypeDef(BaseValidatorModel):
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
    InventoryRetrievalParameters: Optional[InventoryRetrievalJobDescriptionTypeDef] = None
    JobOutputPath: Optional[str] = None
    SelectParameters: Optional[SelectParametersTypeDef] = None
    OutputLocation: Optional[OutputLocationOutputTypeDef] = None


class S3LocationUnionTypeDef(BaseValidatorModel):
    pass


class OutputLocationTypeDef(BaseValidatorModel):
    S3: Optional[S3LocationUnionTypeDef] = None


class ListJobsOutputTypeDef(BaseValidatorModel):
    JobList: List[GlacierJobDescriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class JobParametersTypeDef(BaseValidatorModel):
    pass


class InitiateJobInputTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    jobParameters: Optional[JobParametersTypeDef] = None


