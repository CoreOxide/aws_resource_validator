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
from aws_resource_validator.pydantic_models.qldb_session_constants import *

class TimingInformationTypeDef(BaseModel):
    ProcessingTimeMilliseconds: Optional[int] = None

class IOUsageTypeDef(BaseModel):
    ReadIOs: Optional[int] = None
    WriteIOs: Optional[int] = None

class FetchPageRequestTypeDef(BaseModel):
    TransactionId: str
    NextPageToken: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class StartSessionRequestTypeDef(BaseModel):
    LedgerName: str

class AbortTransactionResultTypeDef(BaseModel):
    TimingInformation: Optional[TimingInformationTypeDef] = None

class EndSessionResultTypeDef(BaseModel):
    TimingInformation: Optional[TimingInformationTypeDef] = None

class StartSessionResultTypeDef(BaseModel):
    SessionToken: Optional[str] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None

class StartTransactionResultTypeDef(BaseModel):
    TransactionId: Optional[str] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None

class CommitTransactionRequestTypeDef(BaseModel):
    TransactionId: str
    CommitDigest: BlobTypeDef

class ValueHolderTypeDef(BaseModel):
    IonBinary: Optional[BlobTypeDef] = None
    IonText: Optional[str] = None

class CommitTransactionResultTypeDef(BaseModel):
    TransactionId: Optional[str] = None
    CommitDigest: Optional[bytes] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None

class ExecuteStatementRequestTypeDef(BaseModel):
    TransactionId: str
    Statement: str
    Parameters: Optional[Sequence[ValueHolderTypeDef]] = None

class PageTypeDef(BaseModel):
    Values: Optional[List[ValueHolderTypeDef]] = None
    NextPageToken: Optional[str] = None

class SendCommandRequestRequestTypeDef(BaseModel):
    SessionToken: Optional[str] = None
    StartSession: Optional[StartSessionRequestTypeDef] = None
    StartTransaction: Optional[Mapping[str, Any]] = None
    EndSession: Optional[Mapping[str, Any]] = None
    CommitTransaction: Optional[CommitTransactionRequestTypeDef] = None
    AbortTransaction: Optional[Mapping[str, Any]] = None
    ExecuteStatement: Optional[ExecuteStatementRequestTypeDef] = None
    FetchPage: Optional[FetchPageRequestTypeDef] = None

class ExecuteStatementResultTypeDef(BaseModel):
    FirstPage: Optional[PageTypeDef] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None

class FetchPageResultTypeDef(BaseModel):
    Page: Optional[PageTypeDef] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None

class SendCommandResultTypeDef(BaseModel):
    StartSession: StartSessionResultTypeDef
    StartTransaction: StartTransactionResultTypeDef
    EndSession: EndSessionResultTypeDef
    CommitTransaction: CommitTransactionResultTypeDef
    AbortTransaction: AbortTransactionResultTypeDef
    ExecuteStatement: ExecuteStatementResultTypeDef
    FetchPage: FetchPageResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

