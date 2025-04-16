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

class CancelJournalKinesisStreamRequest(BaseValidatorModel):
    LedgerName: str
    StreamId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateLedgerRequest(BaseValidatorModel):
    Name: str
    PermissionsMode: PermissionsModeType
    Tags: Optional[Mapping[str, str]] = None
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None


class DeleteLedgerRequest(BaseValidatorModel):
    Name: str


class DescribeJournalKinesisStreamRequest(BaseValidatorModel):
    LedgerName: str
    StreamId: str


class DescribeJournalS3ExportRequest(BaseValidatorModel):
    Name: str
    ExportId: str


class DescribeLedgerRequest(BaseValidatorModel):
    Name: str


class LedgerEncryptionDescription(BaseValidatorModel):
    KmsKeyArn: str
    EncryptionStatus: EncryptionStatusType
    InaccessibleKmsKeyDateTime: Optional[datetime] = None


class ValueHolder(BaseValidatorModel):
    IonText: Optional[str] = None


class GetDigestRequest(BaseValidatorModel):
    Name: str


class KinesisConfiguration(BaseValidatorModel):
    StreamArn: str
    AggregationEnabled: Optional[bool] = None


class LedgerSummary(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[LedgerStateType] = None
    CreationDateTime: Optional[datetime] = None


class ListJournalKinesisStreamsForLedgerRequest(BaseValidatorModel):
    LedgerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJournalS3ExportsForLedgerRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJournalS3ExportsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLedgersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class S3EncryptionConfiguration(BaseValidatorModel):
    ObjectEncryptionType: S3ObjectEncryptionTypeType
    KmsKeyArn: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateLedgerPermissionsModeRequest(BaseValidatorModel):
    Name: str
    PermissionsMode: PermissionsModeType


class UpdateLedgerRequest(BaseValidatorModel):
    Name: str
    DeletionProtection: Optional[bool] = None
    KmsKey: Optional[str] = None


class CancelJournalKinesisStreamResponse(BaseValidatorModel):
    StreamId: str
    ResponseMetadata: ResponseMetadata


class CreateLedgerResponse(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExportJournalToS3Response(BaseValidatorModel):
    ExportId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StreamJournalToKinesisResponse(BaseValidatorModel):
    StreamId: str
    ResponseMetadata: ResponseMetadata


class UpdateLedgerPermissionsModeResponse(BaseValidatorModel):
    Name: str
    Arn: str
    PermissionsMode: PermissionsModeType
    ResponseMetadata: ResponseMetadata


class DescribeLedgerResponse(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescription
    ResponseMetadata: ResponseMetadata


class UpdateLedgerResponse(BaseValidatorModel):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescription
    ResponseMetadata: ResponseMetadata


class GetBlockRequest(BaseValidatorModel):
    Name: str
    BlockAddress: ValueHolder
    DigestTipAddress: Optional[ValueHolder] = None


class GetBlockResponse(BaseValidatorModel):
    Block: ValueHolder
    Proof: ValueHolder
    ResponseMetadata: ResponseMetadata


class GetDigestResponse(BaseValidatorModel):
    Digest: bytes
    DigestTipAddress: ValueHolder
    ResponseMetadata: ResponseMetadata


class GetRevisionRequest(BaseValidatorModel):
    Name: str
    BlockAddress: ValueHolder
    DocumentId: str
    DigestTipAddress: Optional[ValueHolder] = None


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


class Timestamp(BaseValidatorModel):
    pass


class StreamJournalToKinesisRequest(BaseValidatorModel):
    LedgerName: str
    RoleArn: str
    InclusiveStartTime: Timestamp
    KinesisConfiguration: KinesisConfiguration
    StreamName: str
    Tags: Optional[Mapping[str, str]] = None
    ExclusiveEndTime: Optional[Timestamp] = None


class ListLedgersResponse(BaseValidatorModel):
    Ledgers: List[LedgerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class S3ExportConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: str
    EncryptionConfiguration: S3EncryptionConfiguration


class DescribeJournalKinesisStreamResponse(BaseValidatorModel):
    Stream: JournalKinesisStreamDescription
    ResponseMetadata: ResponseMetadata


class ListJournalKinesisStreamsForLedgerResponse(BaseValidatorModel):
    Streams: List[JournalKinesisStreamDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class DescribeJournalS3ExportResponse(BaseValidatorModel):
    ExportDescription: JournalS3ExportDescription
    ResponseMetadata: ResponseMetadata


class ListJournalS3ExportsForLedgerResponse(BaseValidatorModel):
    JournalS3Exports: List[JournalS3ExportDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListJournalS3ExportsResponse(BaseValidatorModel):
    JournalS3Exports: List[JournalS3ExportDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


