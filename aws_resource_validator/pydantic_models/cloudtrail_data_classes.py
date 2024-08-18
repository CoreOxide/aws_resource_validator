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
from aws_resource_validator.pydantic_models.cloudtrail_data_constants import *

class AuditEventResultEntryTypeDef(BaseValidatorModel):
    eventID: str
    id: str

class AuditEventTypeDef(BaseValidatorModel):
    eventData: str
    id: str
    eventDataChecksum: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ResultErrorEntryTypeDef(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    id: str

class PutAuditEventsRequestRequestTypeDef(BaseValidatorModel):
    auditEvents: Sequence[AuditEventTypeDef]
    channelArn: str
    externalId: Optional[str] = None

class PutAuditEventsResponseTypeDef(BaseValidatorModel):
    failed: List[ResultErrorEntryTypeDef]
    successful: List[AuditEventResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

