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
from aws_resource_validator.pydantic_models.qldb_session_constants import *

class TimingInformationTypeDef(BaseValidatorModel):
    ProcessingTimeMilliseconds: Optional[int] = None


class IOUsageTypeDef(BaseValidatorModel):
    ReadIOs: Optional[int] = None
    WriteIOs: Optional[int] = None


class FetchPageRequestTypeDef(BaseValidatorModel):
    TransactionId: str
    NextPageToken: str


class ValueHolderOutputTypeDef(BaseValidatorModel):
    IonBinary: Optional[bytes] = None
    IonText: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class StartSessionRequestTypeDef(BaseValidatorModel):
    LedgerName: str


class AbortTransactionResultTypeDef(BaseValidatorModel):
    TimingInformation: Optional[TimingInformationTypeDef] = None


class EndSessionResultTypeDef(BaseValidatorModel):
    TimingInformation: Optional[TimingInformationTypeDef] = None


class StartSessionResultTypeDef(BaseValidatorModel):
    SessionToken: Optional[str] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None


class StartTransactionResultTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class CommitTransactionRequestTypeDef(BaseValidatorModel):
    TransactionId: str
    CommitDigest: BlobTypeDef


class ValueHolderTypeDef(BaseValidatorModel):
    IonBinary: Optional[BlobTypeDef] = None
    IonText: Optional[str] = None


class CommitTransactionResultTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None
    CommitDigest: Optional[bytes] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None


class PageTypeDef(BaseValidatorModel):
    Values: Optional[List[ValueHolderOutputTypeDef]] = None
    NextPageToken: Optional[str] = None


class ExecuteStatementResultTypeDef(BaseValidatorModel):
    FirstPage: Optional[PageTypeDef] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None


class FetchPageResultTypeDef(BaseValidatorModel):
    Page: Optional[PageTypeDef] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None


class ValueHolderUnionTypeDef(BaseValidatorModel):
    pass


class ExecuteStatementRequestTypeDef(BaseValidatorModel):
    TransactionId: str
    Statement: str
    Parameters: Optional[Sequence[ValueHolderUnionTypeDef]] = None


class SendCommandResultTypeDef(BaseValidatorModel):
    StartSession: StartSessionResultTypeDef
    StartTransaction: StartTransactionResultTypeDef
    EndSession: EndSessionResultTypeDef
    CommitTransaction: CommitTransactionResultTypeDef
    AbortTransaction: AbortTransactionResultTypeDef
    ExecuteStatement: ExecuteStatementResultTypeDef
    FetchPage: FetchPageResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SendCommandRequestTypeDef(BaseValidatorModel):
    SessionToken: Optional[str] = None
    StartSession: Optional[StartSessionRequestTypeDef] = None
    StartTransaction: Optional[Mapping[str, Any]] = None
    EndSession: Optional[Mapping[str, Any]] = None
    CommitTransaction: Optional[CommitTransactionRequestTypeDef] = None
    AbortTransaction: Optional[Mapping[str, Any]] = None
    ExecuteStatement: Optional[ExecuteStatementRequestTypeDef] = None
    FetchPage: Optional[FetchPageRequestTypeDef] = None


