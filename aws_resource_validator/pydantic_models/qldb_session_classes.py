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
from aws_resource_validator.pydantic_models.qldb_session_constants import *

class TimingInformationTypeDef(BaseValidatorModel):
    ProcessingTimeMilliseconds: Optional[int] = None

class IOUsageTypeDef(BaseValidatorModel):
    ReadIOs: Optional[int] = None
    WriteIOs: Optional[int] = None

class FetchPageRequestTypeDef(BaseValidatorModel):
    TransactionId: str
    NextPageToken: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class ExecuteStatementRequestTypeDef(BaseValidatorModel):
    TransactionId: str
    Statement: str
    Parameters: Optional[Sequence[ValueHolderTypeDef]] = None

class PageTypeDef(BaseValidatorModel):
    Values: Optional[List[ValueHolderTypeDef]] = None
    NextPageToken: Optional[str] = None

class SendCommandRequestRequestTypeDef(BaseValidatorModel):
    SessionToken: Optional[str] = None
    StartSession: Optional[StartSessionRequestTypeDef] = None
    StartTransaction: Optional[Mapping[str, Any]] = None
    EndSession: Optional[Mapping[str, Any]] = None
    CommitTransaction: Optional[CommitTransactionRequestTypeDef] = None
    AbortTransaction: Optional[Mapping[str, Any]] = None
    ExecuteStatement: Optional[ExecuteStatementRequestTypeDef] = None
    FetchPage: Optional[FetchPageRequestTypeDef] = None

class ExecuteStatementResultTypeDef(BaseValidatorModel):
    FirstPage: Optional[PageTypeDef] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None

class FetchPageResultTypeDef(BaseValidatorModel):
    Page: Optional[PageTypeDef] = None
    TimingInformation: Optional[TimingInformationTypeDef] = None
    ConsumedIOs: Optional[IOUsageTypeDef] = None

class SendCommandResultTypeDef(BaseValidatorModel):
    StartSession: StartSessionResultTypeDef
    StartTransaction: StartTransactionResultTypeDef
    EndSession: EndSessionResultTypeDef
    CommitTransaction: CommitTransactionResultTypeDef
    AbortTransaction: AbortTransactionResultTypeDef
    ExecuteStatement: ExecuteStatementResultTypeDef
    FetchPage: FetchPageResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

