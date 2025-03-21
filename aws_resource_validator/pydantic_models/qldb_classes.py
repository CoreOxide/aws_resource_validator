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
from aws_resource_validator.pydantic_models.qldb_constants import *

class CancelJournalKinesisStreamRequestTypeDef(BaseValidatorModel):
    LedgerName: str
    StreamId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateLedgerRequestTypeDef(BaseValidatorModel):
    Name: str
    PermissionsMode: PermissionsModeType
    Tags: Optional[Mapping[str, str]] = None
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None


class DeleteLedgerRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeJournalKinesisStreamRequestTypeDef(BaseValidatorModel):
    LedgerName: str
    StreamId: str


class DescribeJournalS3ExportRequestTypeDef(BaseValidatorModel):
    Name: str
    ExportId: str


class DescribeLedgerRequestTypeDef(BaseValidatorModel):
    Name: str


class LedgerEncryptionDescriptionTypeDef(BaseValidatorModel):
    KmsKeyArn: str
    EncryptionStatus: EncryptionStatusType
    InaccessibleKmsKeyDateTime: Optional[datetime] = None


class ValueHolderTypeDef(BaseValidatorModel):
    IonText: Optional[str] = None


class GetDigestRequestTypeDef(BaseValidatorModel):
    Name: str


class KinesisConfigurationTypeDef(BaseValidatorModel):
    StreamArn: str
    AggregationEnabled: Optional[bool] = None


class LedgerSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[LedgerStateType] = None
    CreationDateTime: Optional[datetime] = None


class ListJournalKinesisStreamsForLedgerRequestTypeDef(BaseValidatorModel):
    LedgerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJournalS3ExportsForLedgerRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJournalS3ExportsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLedgersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class S3EncryptionConfigurationTypeDef(BaseValidatorModel):
    ObjectEncryptionType: S3ObjectEncryptionTypeType
    KmsKeyArn: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateLedgerPermissionsModeRequestTypeDef(BaseValidatorModel):
    Name: str
    PermissionsMode: PermissionsModeType


class UpdateLedgerRequestTypeDef(BaseValidatorModel):
    Name: str
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None


class CancelJournalKinesisStreamResponseTypeDef(BaseValidatorModel):
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLedgerResponseTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExportJournalToS3ResponseTypeDef(BaseValidatorModel):
    ExportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StreamJournalToKinesisResponseTypeDef(BaseValidatorModel):
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLedgerPermissionsModeResponseTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    PermissionsMode: PermissionsModeType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLedgerResponseTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLedgerResponseTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlockRequestTypeDef(BaseValidatorModel):
    Name: str
    BlockAddress: ValueHolderTypeDef
    DigestTipAddress: Optional[ValueHolderTypeDef] = None


class GetBlockResponseTypeDef(BaseValidatorModel):
    Block: ValueHolderTypeDef
    Proof: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDigestResponseTypeDef(BaseValidatorModel):
    Digest: bytes
    DigestTipAddress: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRevisionRequestTypeDef(BaseValidatorModel):
    Name: str
    BlockAddress: ValueHolderTypeDef
    DocumentId: str
    DigestTipAddress: Optional[ValueHolderTypeDef] = None


class GetRevisionResponseTypeDef(BaseValidatorModel):
    Proof: ValueHolderTypeDef
    Revision: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JournalKinesisStreamDescriptionTypeDef(BaseValidatorModel):
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


class TimestampTypeDef(BaseValidatorModel):
    pass


class StreamJournalToKinesisRequestTypeDef(BaseValidatorModel):
    LedgerName: str
    RoleArn: str
    InclusiveStartTime: TimestampTypeDef
    KinesisConfiguration: KinesisConfigurationTypeDef
    StreamName: str
    Tags: Optional[Mapping[str, str]] = None
    ExclusiveEndTime: Optional[TimestampTypeDef] = None


class ListLedgersResponseTypeDef(BaseValidatorModel):
    Ledgers: List[LedgerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class S3ExportConfigurationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: str
    EncryptionConfiguration: S3EncryptionConfigurationTypeDef


class DescribeJournalKinesisStreamResponseTypeDef(BaseValidatorModel):
    Stream: JournalKinesisStreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJournalKinesisStreamsForLedgerResponseTypeDef(BaseValidatorModel):
    Streams: List[JournalKinesisStreamDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExportJournalToS3RequestTypeDef(BaseValidatorModel):
    Name: str
    InclusiveStartTime: TimestampTypeDef
    ExclusiveEndTime: TimestampTypeDef
    S3ExportConfiguration: S3ExportConfigurationTypeDef
    RoleArn: str
    OutputFormat: Optional[OutputFormatType] = None


class JournalS3ExportDescriptionTypeDef(BaseValidatorModel):
    LedgerName: str
    ExportId: str
    ExportCreationTime: datetime
    Status: ExportStatusType
    InclusiveStartTime: datetime
    ExclusiveEndTime: datetime
    S3ExportConfiguration: S3ExportConfigurationTypeDef
    RoleArn: str
    OutputFormat: Optional[OutputFormatType] = None


class DescribeJournalS3ExportResponseTypeDef(BaseValidatorModel):
    ExportDescription: JournalS3ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJournalS3ExportsForLedgerResponseTypeDef(BaseValidatorModel):
    JournalS3Exports: List[JournalS3ExportDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListJournalS3ExportsResponseTypeDef(BaseValidatorModel):
    JournalS3Exports: List[JournalS3ExportDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


