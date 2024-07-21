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
from aws_resource_validator.pydantic_models.cloudtrail_data_constants import *

class AuditEventResultEntryTypeDef(BaseModel):
    eventID: str
    id: str

class AuditEventTypeDef(BaseModel):
    eventData: str
    id: str
    eventDataChecksum: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ResultErrorEntryTypeDef(BaseModel):
    errorCode: str
    errorMessage: str
    id: str

class PutAuditEventsRequestRequestTypeDef(BaseModel):
    auditEvents: Sequence[AuditEventTypeDef]
    channelArn: str
    externalId: Optional[str] = None

class PutAuditEventsResponseTypeDef(BaseModel):
    failed: List[ResultErrorEntryTypeDef]
    successful: List[AuditEventResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

