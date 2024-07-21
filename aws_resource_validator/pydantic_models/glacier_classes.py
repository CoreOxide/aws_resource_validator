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
from aws_resource_validator.pydantic_models.glacier_constants import *

class AbortMultipartUploadInputRequestTypeDef(BaseModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None

class AbortVaultLockInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class AddTagsToVaultInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CSVInputTypeDef(BaseModel):
    FileHeaderInfo: Optional[FileHeaderInfoType] = None
    Comments: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None

class CSVOutputTypeDef(BaseModel):
    QuoteFields: Optional[QuoteFieldsType] = None
    QuoteEscapeCharacter: Optional[str] = None
    RecordDelimiter: Optional[str] = None
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None

class CompleteMultipartUploadInputMultipartUploadCompleteTypeDef(BaseModel):
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None

class CompleteMultipartUploadInputRequestTypeDef(BaseModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    archiveSize: Optional[str] = None
    checksum: Optional[str] = None

class CompleteVaultLockInputRequestTypeDef(BaseModel):
    vaultName: str
    lockId: str
    accountId: Optional[str] = None

class CreateVaultInputAccountCreateVaultTypeDef(BaseModel):
    vaultName: str

class CreateVaultInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class CreateVaultInputServiceResourceCreateVaultTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class DataRetrievalRuleTypeDef(BaseModel):
    Strategy: Optional[str] = None
    BytesPerHour: Optional[int] = None

class DeleteArchiveInputRequestTypeDef(BaseModel):
    vaultName: str
    archiveId: str
    accountId: Optional[str] = None

class DeleteVaultAccessPolicyInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class DeleteVaultInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class DeleteVaultNotificationsInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class DescribeJobInputRequestTypeDef(BaseModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None

class DescribeVaultInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeVaultOutputTypeDef(BaseModel):
    VaultARN: Optional[str] = None
    VaultName: Optional[str] = None
    CreationDate: Optional[str] = None
    LastInventoryDate: Optional[str] = None
    NumberOfArchives: Optional[int] = None
    SizeInBytes: Optional[int] = None

class EncryptionTypeDef(BaseModel):
    EncryptionType: Optional[EncryptionTypeType] = None
    KMSKeyId: Optional[str] = None
    KMSContext: Optional[str] = None

class GetDataRetrievalPolicyInputRequestTypeDef(BaseModel):
    accountId: Optional[str] = None

class GetJobOutputInputJobGetOutputTypeDef(BaseModel):
    range: Optional[str] = None

class GetJobOutputInputRequestTypeDef(BaseModel):
    vaultName: str
    jobId: str
    accountId: Optional[str] = None
    range: Optional[str] = None

class GetVaultAccessPolicyInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class VaultAccessPolicyTypeDef(BaseModel):
    Policy: Optional[str] = None

class GetVaultLockInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class GetVaultNotificationsInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class VaultNotificationConfigTypeDef(BaseModel):
    SNSTopic: Optional[str] = None
    Events: Optional[List[str]] = None

class InventoryRetrievalJobDescriptionTypeDef(BaseModel):
    Format: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None

class GranteeTypeDef(BaseModel):
    Type: TypeType
    DisplayName: Optional[str] = None
    URI: Optional[str] = None
    ID: Optional[str] = None
    EmailAddress: Optional[str] = None

class InitiateMultipartUploadInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    partSize: Optional[str] = None

class InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef(BaseModel):
    archiveDescription: Optional[str] = None
    partSize: Optional[str] = None

class VaultLockPolicyTypeDef(BaseModel):
    Policy: Optional[str] = None

class InventoryRetrievalJobInputTypeDef(BaseModel):
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Limit: Optional[str] = None
    Marker: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListJobsInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    limit: Optional[str] = None
    marker: Optional[str] = None
    statuscode: Optional[str] = None
    completed: Optional[str] = None

class ListMultipartUploadsInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None

class UploadListElementTypeDef(BaseModel):
    MultipartUploadId: Optional[str] = None
    VaultARN: Optional[str] = None
    ArchiveDescription: Optional[str] = None
    PartSizeInBytes: Optional[int] = None
    CreationDate: Optional[str] = None

class ListPartsInputMultipartUploadPartsTypeDef(BaseModel):
    marker: Optional[str] = None
    limit: Optional[str] = None

class ListPartsInputRequestTypeDef(BaseModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None

class PartListElementTypeDef(BaseModel):
    RangeInBytes: Optional[str] = None
    SHA256TreeHash: Optional[str] = None

class ListProvisionedCapacityInputRequestTypeDef(BaseModel):
    accountId: Optional[str] = None

class ProvisionedCapacityDescriptionTypeDef(BaseModel):
    CapacityId: Optional[str] = None
    StartDate: Optional[str] = None
    ExpirationDate: Optional[str] = None

class ListTagsForVaultInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None

class ListVaultsInputRequestTypeDef(BaseModel):
    accountId: Optional[str] = None
    marker: Optional[str] = None
    limit: Optional[str] = None

class PurchaseProvisionedCapacityInputRequestTypeDef(BaseModel):
    accountId: Optional[str] = None

class RemoveTagsFromVaultInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None

class VaultNotificationConfigNotificationTypeDef(BaseModel):
    SNSTopic: Optional[str] = None
    Events: Optional[Sequence[str]] = None

class ArchiveCreationOutputTypeDef(BaseModel):
    location: str
    checksum: str
    archiveId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVaultOutputTypeDef(BaseModel):
    location: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVaultResponseTypeDef(BaseModel):
    VaultARN: str
    VaultName: str
    CreationDate: str
    LastInventoryDate: str
    NumberOfArchives: int
    SizeInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobOutputOutputTypeDef(BaseModel):
    body: StreamingBody
    checksum: str
    status: int
    contentRange: str
    acceptRanges: str
    contentType: str
    archiveDescription: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVaultLockOutputTypeDef(BaseModel):
    Policy: str
    State: str
    ExpirationDate: str
    CreationDate: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateJobOutputTypeDef(BaseModel):
    location: str
    jobId: str
    jobOutputPath: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateMultipartUploadOutputTypeDef(BaseModel):
    location: str
    uploadId: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateVaultLockOutputTypeDef(BaseModel):
    lockId: str
    ResponseMetadata: ResponseMetadataTypeDef

class InventoryRetrievalJobDescriptionResponseTypeDef(BaseModel):
    Format: str
    StartDate: str
    EndDate: str
    Limit: str
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForVaultOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseProvisionedCapacityOutputTypeDef(BaseModel):
    capacityId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadMultipartPartOutputTypeDef(BaseModel):
    checksum: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadArchiveInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class UploadArchiveInputVaultUploadArchiveTypeDef(BaseModel):
    archiveDescription: Optional[str] = None
    checksum: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class UploadMultipartPartInputMultipartUploadUploadPartTypeDef(BaseModel):
    checksum: Optional[str] = None
    range: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class UploadMultipartPartInputRequestTypeDef(BaseModel):
    vaultName: str
    uploadId: str
    accountId: Optional[str] = None
    checksum: Optional[str] = None
    range: Optional[str] = None
    body: Optional[BlobTypeDef] = None

class InputSerializationTypeDef(BaseModel):
    csv: Optional[CSVInputTypeDef] = None

class OutputSerializationTypeDef(BaseModel):
    csv: Optional[CSVOutputTypeDef] = None

class DataRetrievalPolicyTypeDef(BaseModel):
    Rules: Optional[List[DataRetrievalRuleTypeDef]] = None

class DescribeVaultInputVaultExistsWaitTypeDef(BaseModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVaultInputVaultNotExistsWaitTypeDef(BaseModel):
    accountId: str
    vaultName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListVaultsOutputTypeDef(BaseModel):
    VaultList: List[DescribeVaultOutputTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVaultAccessPolicyOutputTypeDef(BaseModel):
    policy: VaultAccessPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetVaultAccessPolicyInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultAccessPolicyTypeDef] = None

class GetVaultNotificationsOutputTypeDef(BaseModel):
    vaultNotificationConfig: VaultNotificationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetVaultNotificationsInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    vaultNotificationConfig: Optional[VaultNotificationConfigTypeDef] = None

class GrantTypeDef(BaseModel):
    Grantee: Optional[GranteeTypeDef] = None
    Permission: Optional[PermissionType] = None

class InitiateVaultLockInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    policy: Optional[VaultLockPolicyTypeDef] = None

class ListJobsInputListJobsPaginateTypeDef(BaseModel):
    accountId: str
    vaultName: str
    statuscode: Optional[str] = None
    completed: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartUploadsInputListMultipartUploadsPaginateTypeDef(BaseModel):
    accountId: str
    vaultName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartsInputListPartsPaginateTypeDef(BaseModel):
    accountId: str
    vaultName: str
    uploadId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVaultsInputListVaultsPaginateTypeDef(BaseModel):
    accountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartUploadsOutputTypeDef(BaseModel):
    UploadsList: List[UploadListElementTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPartsOutputTypeDef(BaseModel):
    MultipartUploadId: str
    VaultARN: str
    ArchiveDescription: str
    PartSizeInBytes: int
    CreationDate: str
    Parts: List[PartListElementTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisionedCapacityOutputTypeDef(BaseModel):
    ProvisionedCapacityList: List[ProvisionedCapacityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetVaultNotificationsInputNotificationSetTypeDef(BaseModel):
    vaultNotificationConfig: Optional[VaultNotificationConfigNotificationTypeDef] = None

class SelectParametersResponseTypeDef(BaseModel):
    InputSerialization: InputSerializationTypeDef
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: OutputSerializationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SelectParametersTypeDef(BaseModel):
    InputSerialization: Optional[InputSerializationTypeDef] = None
    ExpressionType: Optional[Literal["SQL"]] = None
    Expression: Optional[str] = None
    OutputSerialization: Optional[OutputSerializationTypeDef] = None

class GetDataRetrievalPolicyOutputTypeDef(BaseModel):
    Policy: DataRetrievalPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetDataRetrievalPolicyInputRequestTypeDef(BaseModel):
    accountId: Optional[str] = None
    Policy: Optional[DataRetrievalPolicyTypeDef] = None

class S3LocationTypeDef(BaseModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    CannedACL: Optional[CannedACLType] = None
    AccessControlList: Optional[List[GrantTypeDef]] = None
    Tagging: Optional[Dict[str, str]] = None
    UserMetadata: Optional[Dict[str, str]] = None
    StorageClass: Optional[StorageClassType] = None

class OutputLocationResponseTypeDef(BaseModel):
    S3: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OutputLocationTypeDef(BaseModel):
    S3: Optional[S3LocationTypeDef] = None

class GlacierJobDescriptionResponseTypeDef(BaseModel):
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

class GlacierJobDescriptionTypeDef(BaseModel):
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

class JobParametersTypeDef(BaseModel):
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

class ListJobsOutputTypeDef(BaseModel):
    JobList: List[GlacierJobDescriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateJobInputRequestTypeDef(BaseModel):
    vaultName: str
    accountId: Optional[str] = None
    jobParameters: Optional[JobParametersTypeDef] = None

