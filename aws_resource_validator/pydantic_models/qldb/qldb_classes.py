from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.qldb.qldb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'cancel_journal_kinesis_stream' function.
class CancelJournalKinesisStreamRequest(BaseValidatorModel):
    LedgerName: str
    StreamId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_ledger' function.
class CreateLedgerRequest(BaseValidatorModel):
    Name: str
    PermissionsMode: PermissionsModeType
    Tags: Optional[Dict[str, str]] = None
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None


# This class is the input for the 'delete_ledger' function.
class DeleteLedgerRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'describe_journal_kinesis_stream' function.
class DescribeJournalKinesisStreamRequest(BaseValidatorModel):
    LedgerName: str
    StreamId: str


# This class is the input for the 'describe_journal_s3_export' function.
class DescribeJournalS3ExportRequest(BaseValidatorModel):
    Name: str
    ExportId: str


# This class is the input for the 'describe_ledger' function.
class DescribeLedgerRequest(BaseValidatorModel):
    Name: str


class LedgerEncryptionDescription(BaseValidatorModel):
    KmsKeyArn: str
    EncryptionStatus: EncryptionStatusType
    InaccessibleKmsKeyDateTime: Optional[datetime] = None

Timestamp = Union[datetime, str]


class ValueHolder(BaseValidatorModel):
    IonText: Optional[str] = None


# This class is the input for the 'get_digest' function.
class GetDigestRequest(BaseValidatorModel):
    Name: str


class KinesisConfiguration(BaseValidatorModel):
    StreamArn: str
    AggregationEnabled: Optional[bool] = None


class LedgerSummary(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[LedgerStateType] = None
    CreationDateTime: Optional[datetime] = None


# This class is the input for the 'list_journal_kinesis_streams_for_ledger' function.
class ListJournalKinesisStreamsForLedgerRequest(BaseValidatorModel):
    LedgerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_journal_s3_exports_for_ledger' function.
class ListJournalS3ExportsForLedgerRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_journal_s3_exports' function.
class ListJournalS3ExportsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_ledgers' function.
class ListLedgersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class S3EncryptionConfiguration(BaseValidatorModel):
    ObjectEncryptionType: S3ObjectEncryptionTypeType
    KmsKeyArn: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_ledger_permissions_mode' function.
class UpdateLedgerPermissionsModeRequest(BaseValidatorModel):
    Name: str
    PermissionsMode: PermissionsModeType


# This class is the input for the 'update_ledger' function.
class UpdateLedgerRequest(BaseValidatorModel):
    Name: str
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None


# This class is the output for the 'cancel_journal_kinesis_stream' function.
class CancelJournalKinesisStreamResponse(BaseValidatorModel):
    StreamId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ledger' function.
class CreateLedgerResponse(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ledger' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_journal_to_s3' function.
class ExportJournalToS3Response(BaseValidatorModel):
    ExportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stream_journal_to_kinesis' function.
class StreamJournalToKinesisResponse(BaseValidatorModel):
    StreamId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ledger_permissions_mode' function.
class UpdateLedgerPermissionsModeResponse(BaseValidatorModel):
    Name: str
    Arn: str
    PermissionsMode: PermissionsModeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ledger' function.
class DescribeLedgerResponse(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ledger' function.
class UpdateLedgerResponse(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'get_block' function.
class GetBlockRequest(BaseValidatorModel):
    Name: str
    BlockAddress: ValueHolder
    DigestTipAddress: Optional[ValueHolder] = None


# This class is the output for the 'get_block' function.
class GetBlockResponse(BaseValidatorModel):
    Block: ValueHolder
    Proof: ValueHolder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_digest' function.
class GetDigestResponse(BaseValidatorModel):
    Digest: bytes
    DigestTipAddress: ValueHolder
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'get_revision' function.
class GetRevisionRequest(BaseValidatorModel):
    Name: str
    BlockAddress: ValueHolder
    DocumentId: str
    DigestTipAddress: Optional[ValueHolder] = None


# This class is the output for the 'get_revision' function.
class GetRevisionResponse(BaseValidatorModel):
    Proof: ValueHolder
    Revision: ValueHolder
    ResponseMetadata: ResponseMetadata


class JournalKinesisStreamDescription(BaseValidatorModel):
    LedgerName: str
    RoleArn: str
    StreamId: str
    Status: StreamStatusType
    KinesisConfiguration: KinesisConfiguration
    StreamName: str
    CreationTime: Optional[datetime] = None
    InclusiveStartTime: Optional[datetime] = None
    ExclusiveEndTime: Optional[datetime] = None
    Arn: Optional[str] = None
    ErrorCause: Optional[ErrorCauseType] = None


# This class is the input for the 'stream_journal_to_kinesis' function.
class StreamJournalToKinesisRequest(BaseValidatorModel):
    LedgerName: str
    RoleArn: str
    InclusiveStartTime: Timestamp
    KinesisConfiguration: KinesisConfiguration
    StreamName: str
    Tags: Optional[Dict[str, str]] = None
    ExclusiveEndTime: Optional[Timestamp] = None


# This class is the output for the 'list_ledgers' function.
class ListLedgersResponse(BaseValidatorModel):
    Ledgers: List[LedgerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class S3ExportConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: str
    EncryptionConfiguration: S3EncryptionConfiguration


# This class is the output for the 'describe_journal_kinesis_stream' function.
class DescribeJournalKinesisStreamResponse(BaseValidatorModel):
    Stream: JournalKinesisStreamDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_journal_kinesis_streams_for_ledger' function.
class ListJournalKinesisStreamsForLedgerResponse(BaseValidatorModel):
    Streams: List[JournalKinesisStreamDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'export_journal_to_s3' function.
class ExportJournalToS3Request(BaseValidatorModel):
    Name: str
    InclusiveStartTime: Timestamp
    ExclusiveEndTime: Timestamp
    S3ExportConfiguration: S3ExportConfiguration
    RoleArn: str
    OutputFormat: Optional[OutputFormatType] = None


class JournalS3ExportDescription(BaseValidatorModel):
    LedgerName: str
    ExportId: str
    ExportCreationTime: datetime
    Status: ExportStatusType
    InclusiveStartTime: datetime
    ExclusiveEndTime: datetime
    S3ExportConfiguration: S3ExportConfiguration
    RoleArn: str
    OutputFormat: Optional[OutputFormatType] = None


# This class is the output for the 'describe_journal_s3_export' function.
class DescribeJournalS3ExportResponse(BaseValidatorModel):
    ExportDescription: JournalS3ExportDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_journal_s3_exports_for_ledger' function.
class ListJournalS3ExportsForLedgerResponse(BaseValidatorModel):
    JournalS3Exports: List[JournalS3ExportDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_journal_s3_exports' function.
class ListJournalS3ExportsResponse(BaseValidatorModel):
    JournalS3Exports: List[JournalS3ExportDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None