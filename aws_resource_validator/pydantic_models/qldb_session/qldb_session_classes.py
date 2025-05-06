from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.qldb_session.qldb_session_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class TimingInformation(BaseValidatorModel):
    ProcessingTimeMilliseconds: Optional[int] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class IOUsage(BaseValidatorModel):
    ReadIOs: Optional[int] = None
    WriteIOs: Optional[int] = None


class FetchPageRequest(BaseValidatorModel):
    TransactionId: str
    NextPageToken: str


class ValueHolderOutput(BaseValidatorModel):
    IonBinary: Optional[bytes] = None
    IonText: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class StartSessionRequest(BaseValidatorModel):
    LedgerName: str


class AbortTransactionResult(BaseValidatorModel):
    TimingInformation: Optional[TimingInformation] = None


class EndSessionResult(BaseValidatorModel):
    TimingInformation: Optional[TimingInformation] = None


class StartSessionResult(BaseValidatorModel):
    SessionToken: Optional[str] = None
    TimingInformation: Optional[TimingInformation] = None


class StartTransactionResult(BaseValidatorModel):
    TransactionId: Optional[str] = None
    TimingInformation: Optional[TimingInformation] = None


class CommitTransactionRequest(BaseValidatorModel):
    TransactionId: str
    CommitDigest: Blob


class ValueHolder(BaseValidatorModel):
    IonBinary: Optional[Blob] = None
    IonText: Optional[str] = None


class CommitTransactionResult(BaseValidatorModel):
    TransactionId: Optional[str] = None
    CommitDigest: Optional[bytes] = None
    TimingInformation: Optional[TimingInformation] = None
    ConsumedIOs: Optional[IOUsage] = None


class Page(BaseValidatorModel):
    Values: Optional[List[ValueHolderOutput]] = None
    NextPageToken: Optional[str] = None

ValueHolderUnion = Union[ValueHolder, ValueHolderOutput]


class ExecuteStatementResult(BaseValidatorModel):
    FirstPage: Optional[Page] = None
    TimingInformation: Optional[TimingInformation] = None
    ConsumedIOs: Optional[IOUsage] = None


class FetchPageResult(BaseValidatorModel):
    Page: Optional[Page] = None
    TimingInformation: Optional[TimingInformation] = None
    ConsumedIOs: Optional[IOUsage] = None


class ExecuteStatementRequest(BaseValidatorModel):
    TransactionId: str
    Statement: str
    Parameters: Optional[List[ValueHolderUnion]] = None


class SendCommandResult(BaseValidatorModel):
    StartSession: StartSessionResult
    StartTransaction: StartTransactionResult
    EndSession: EndSessionResult
    CommitTransaction: CommitTransactionResult
    AbortTransaction: AbortTransactionResult
    ExecuteStatement: ExecuteStatementResult
    FetchPage: FetchPageResult
    ResponseMetadata: ResponseMetadata


class SendCommandRequest(BaseValidatorModel):
    SessionToken: Optional[str] = None
    StartSession: Optional[StartSessionRequest] = None
    StartTransaction: Optional[Dict[str, Any]] = None
    EndSession: Optional[Dict[str, Any]] = None
    CommitTransaction: Optional[CommitTransactionRequest] = None
    AbortTransaction: Optional[Dict[str, Any]] = None
    ExecuteStatement: Optional[ExecuteStatementRequest] = None
    FetchPage: Optional[FetchPageRequest] = None