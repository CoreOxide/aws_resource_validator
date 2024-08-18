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
from aws_resource_validator.pydantic_models.glacier_constants import *

class AbortMultipartUploadInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None

class AbortVaultLockInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class AddTagsToVaultInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class CompleteMultipartUploadInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None

class CompleteVaultLockInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    lockId: str
    accountId: Optional[str] = None

class CreateVaultInputAccountCreateVaultTypeDef(BaseValidatorModel):
    vaultName: str

class CreateVaultInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class CreateVaultInputServiceResourceCreateVaultTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class DataRetrievalRuleTypeDef(BaseValidatorModel):
    Strategy: Optional[str] = None
    BytesPerHour: Optional[int] = None

class DeleteArchiveInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    archiveId: str
    accountId: Optional[str] = None

class DeleteVaultAccessPolicyInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class DeleteVaultInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class DeleteVaultNotificationsInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class DescribeJobInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None

class DescribeVaultInputRequestTypeDef(BaseValidatorModel):
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

class GetDataRetrievalPolicyInputRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class GetJobOutputInputJobGetOutputTypeDef(BaseValidatorModel):
    range: Optional[str] = None

class GetJobOutputInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None
    range: Optional[str] = None

class GetVaultAccessPolicyInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class VaultAccessPolicyTypeDef(BaseValidatorModel):
    Policy: Optional[str] = None

class GetVaultLockInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class GetVaultNotificationsInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class VaultNotificationConfigTypeDef(BaseValidatorModel):
    SNSTopic: Optional[str] = None
    Events: Optional[List[str]] = None

class InventoryRetrievalJobDescriptionTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None

class GranteeTypeDef(BaseValidatorModel):
    Type: TypeType
    DisplayName: Optional[str] = None
    URI: Optional[str] = None
    ID: Optional[str] = None
    EmailAddress: Optional[str] = None

class InitiateMultipartUploadInputRequestTypeDef(BaseValidatorModel):
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

class ListJobsInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    limit: Optional[str] = None
    marker: Optional[str] = None
    statuscode: Optional[str] = None
    completed: Optional[str] = None

class ListMultipartUploadsInputRequestTypeDef(BaseValidatorModel):
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

class ListPartsInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None

class PartListElementTypeDef(BaseValidatorModel):
    RangeInBytes: Optional[str] = None
    SHA256TreeHash: Optional[str] = None

class ListProvisionedCapacityInputRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class ProvisionedCapacityDescriptionTypeDef(BaseValidatorModel):
    CapacityId: Optional[str] = None
    StartDate: Optional[str] = None
    ExpirationDate: Optional[str] = None

class ListTagsForVaultInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None

class ListVaultsInputRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None

class PurchaseProvisionedCapacityInputRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class RemoveTagsFromVaultInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None

class VaultNotificationConfigNotificationTypeDef(BaseValidatorModel):
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

class InventoryRetrievalJobDescriptionResponseTypeDef(BaseValidatorModel):
    Format: str
    StartDate: str
    EndDate: str
    Limit: str
    Marker: str
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

class UploadArchiveInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class UploadArchiveInputVaultUploadArchiveTypeDef(BaseValidatorModel):
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class UploadMultipartPartInputMultipartUploadUploadPartTypeDef(BaseValidatorModel):
    checksum: Optional[str] = None
    range: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class UploadMultipartPartInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    checksum: Optional[str] = None
    range: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class InputSerializationTypeDef(BaseValidatorModel):
    csv: Optional[CSVInputTypeDef] = None

class OutputSerializationTypeDef(BaseValidatorModel):
    csv: Optional[CSVOutputTypeDef] = None

class DataRetrievalPolicyTypeDef(BaseValidatorModel):
    Rules: Optional[List[DataRetrievalRuleTypeDef]] = None

class DescribeVaultInputVaultExistsWaitTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVaultInputVaultNotExistsWaitTypeDef(BaseValidatorModel):
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

class SetVaultAccessPolicyInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultAccessPolicyTypeDef] = None

class GetVaultNotificationsOutputTypeDef(BaseValidatorModel):
    vaultNotificationConfig: VaultNotificationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetVaultNotificationsInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    vaultNotificationConfig: Optional[VaultNotificationConfigTypeDef] = None

class GrantTypeDef(BaseValidatorModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None

class InitiateVaultLockInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultLockPolicyTypeDef] = None

class ListJobsInputListJobsPaginateTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    statuscode: Optional[str] = None
    completed: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartUploadsInputListMultipartUploadsPaginateTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartsInputListPartsPaginateTypeDef(BaseValidatorModel):
    accountId: str
    vaultName: str
    uploadId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVaultsInputListVaultsPaginateTypeDef(BaseValidatorModel):
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

class SetVaultNotificationsInputNotificationSetTypeDef(BaseValidatorModel):
    vaultNotificationConfig: Optional[VaultNotificationConfigNotificationTypeDef] = None

class SelectParametersResponseTypeDef(BaseValidatorModel):
    InputSerialization: InputSerializationTypeDef
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: OutputSerializationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SelectParametersTypeDef(BaseValidatorModel):
    InputSerialization: Optional[InputSerializationTypeDef] = None
    ExpressionType: Optional[Literal["SQL"]] = None
    Expression: Optional[str] = None
    OutputSerialization: Optional[OutputSerializationTypeDef] = None

class GetDataRetrievalPolicyOutputTypeDef(BaseValidatorModel):
    Policy: DataRetrievalPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetDataRetrievalPolicyInputRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    Policy: Optional[DataRetrievalPolicyTypeDef] = None

class S3LocationTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    CannedACL: Optional[CannedACLType] = None
    AccessControlList: Optional[List[GrantTypeDef]] = None
    Tagging: Optional[Dict[str, str]] = None
    UserMetadata: Optional[Dict[str, str]] = None
    StorageClass: Optional[StorageClassType] = None

class OutputLocationResponseTypeDef(BaseValidatorModel):
    S3: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OutputLocationTypeDef(BaseValidatorModel):
    S3: Optional[S3LocationTypeDef] = None

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
    OutputLocation: OutputLocationTypeDef
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
    OutputLocation: Optional[OutputLocationTypeDef] = None

class JobParametersTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    Type: Optional[str] = None
    ArchiveId: Optional[str] = None
    Description: Optional[str] = None
    SNSTopic: Optional[str] = None
    RetrievalByteRange: Optional[str] = None
    Tier: Optional[str] = None
    InventoryRetrievalParameters: Optional[InventoryRetrievalJobInputTypeDef] = None
    SelectParameters: Optional[SelectParametersTypeDef] = None
    OutputLocation: Optional[OutputLocationTypeDef] = None

class ListJobsOutputTypeDef(BaseValidatorModel):
    JobList: List[GlacierJobDescriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateJobInputRequestTypeDef(BaseValidatorModel):
    vaultName: str
    accountId: Optional[str] = None
    jobParameters: Optional[JobParametersTypeDef] = None

