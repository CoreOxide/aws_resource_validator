from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudtrail_data.cloudtrail_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AuditEventResultEntry(BaseValidatorModel):
    eventID: str
    id: str


class AuditEvent(BaseValidatorModel):
    eventData: str
    id: str
    eventDataChecksum: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ResultErrorEntry(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    id: str


class PutAuditEventsRequest(BaseValidatorModel):
    auditEvents: List[AuditEvent]
    channelArn: str
    externalId: Optional[str] = None


class PutAuditEventsResponse(BaseValidatorModel):
    failed: List[ResultErrorEntry]
    successful: List[AuditEventResultEntry]
    ResponseMetadata: ResponseMetadata