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
from aws_resource_validator.pydantic_models.qldb_constants import *

class CancelJournalKinesisStreamRequestRequestTypeDef(BaseModel):
    LedgerName: str
    StreamId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateLedgerRequestRequestTypeDef(BaseModel):
    Name: str
    PermissionsMode: PermissionsModeType
    Tags: Optional[Mapping[str, str]] = None
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None

class DeleteLedgerRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeJournalKinesisStreamRequestRequestTypeDef(BaseModel):
    LedgerName: str
    StreamId: str

class DescribeJournalS3ExportRequestRequestTypeDef(BaseModel):
    Name: str
    ExportId: str

class DescribeLedgerRequestRequestTypeDef(BaseModel):
    Name: str

class LedgerEncryptionDescriptionTypeDef(BaseModel):
    KmsKeyArn: str
    EncryptionStatus: EncryptionStatusType
    InaccessibleKmsKeyDateTime: Optional[datetime] = None

class ValueHolderTypeDef(BaseModel):
    IonText: Optional[str] = None

class GetDigestRequestRequestTypeDef(BaseModel):
    Name: str

class KinesisConfigurationTypeDef(BaseModel):
    StreamArn: str
    AggregationEnabled: Optional[bool] = None

class LedgerSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    State: Optional[LedgerStateType] = None
    CreationDateTime: Optional[datetime] = None

class ListJournalKinesisStreamsForLedgerRequestRequestTypeDef(BaseModel):
    LedgerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJournalS3ExportsForLedgerRequestRequestTypeDef(BaseModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJournalS3ExportsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLedgersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class S3EncryptionConfigurationTypeDef(BaseModel):
    ObjectEncryptionType: S3ObjectEncryptionTypeType
    KmsKeyArn: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateLedgerPermissionsModeRequestRequestTypeDef(BaseModel):
    Name: str
    PermissionsMode: PermissionsModeType

class UpdateLedgerRequestRequestTypeDef(BaseModel):
    Name: str
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None

class CancelJournalKinesisStreamResponseTypeDef(BaseModel):
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLedgerResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportJournalToS3ResponseTypeDef(BaseModel):
    ExportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StreamJournalToKinesisResponseTypeDef(BaseModel):
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLedgerPermissionsModeResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    PermissionsMode: PermissionsModeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLedgerResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLedgerResponseTypeDef(BaseModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlockRequestRequestTypeDef(BaseModel):
    Name: str
    BlockAddress: ValueHolderTypeDef
    DigestTipAddress: Optional[ValueHolderTypeDef] = None

class GetBlockResponseTypeDef(BaseModel):
    Block: ValueHolderTypeDef
    Proof: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDigestResponseTypeDef(BaseModel):
    Digest: bytes
    DigestTipAddress: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevisionRequestRequestTypeDef(BaseModel):
    Name: str
    BlockAddress: ValueHolderTypeDef
    DocumentId: str
    DigestTipAddress: Optional[ValueHolderTypeDef] = None

class GetRevisionResponseTypeDef(BaseModel):
    Proof: ValueHolderTypeDef
    Revision: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JournalKinesisStreamDescriptionTypeDef(BaseModel):
    LedgerName: str
    RoleArn: str
    StreamId: str
    Status: StreamStatusType
    KinesisConfiguration: KinesisConfigurationTypeDef
    StreamName: str
    CreationTime: Optional[datetime] = None
    InclusiveStartTime: Optional[datetime] = None
    ExclusiveEndTime: Optional[datetime] = None
    Arn: Optional[str] = None
    ErrorCause: Optional[ErrorCauseType] = None

class StreamJournalToKinesisRequestRequestTypeDef(BaseModel):
    LedgerName: str
    RoleArn: str
    InclusiveStartTime: TimestampTypeDef
    KinesisConfiguration: KinesisConfigurationTypeDef
    StreamName: str
    Tags: Optional[Mapping[str, str]] = None
    ExclusiveEndTime: Optional[TimestampTypeDef] = None

class ListLedgersResponseTypeDef(BaseModel):
    Ledgers: List[LedgerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class S3ExportConfigurationTypeDef(BaseModel):
    Bucket: str
    Prefix: str
    EncryptionConfiguration: S3EncryptionConfigurationTypeDef

class DescribeJournalKinesisStreamResponseTypeDef(BaseModel):
    Stream: JournalKinesisStreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJournalKinesisStreamsForLedgerResponseTypeDef(BaseModel):
    Streams: List[JournalKinesisStreamDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportJournalToS3RequestRequestTypeDef(BaseModel):
    Name: str
    InclusiveStartTime: TimestampTypeDef
    ExclusiveEndTime: TimestampTypeDef
    S3ExportConfiguration: S3ExportConfigurationTypeDef
    RoleArn: str
    OutputFormat: Optional[OutputFormatType] = None

class JournalS3ExportDescriptionTypeDef(BaseModel):
    LedgerName: str
    ExportId: str
    ExportCreationTime: datetime
    Status: ExportStatusType
    InclusiveStartTime: datetime
    ExclusiveEndTime: datetime
    S3ExportConfiguration: S3ExportConfigurationTypeDef
    RoleArn: str
    OutputFormat: Optional[OutputFormatType] = None

class DescribeJournalS3ExportResponseTypeDef(BaseModel):
    ExportDescription: JournalS3ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJournalS3ExportsForLedgerResponseTypeDef(BaseModel):
    JournalS3Exports: List[JournalS3ExportDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJournalS3ExportsResponseTypeDef(BaseModel):
    JournalS3Exports: List[JournalS3ExportDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

