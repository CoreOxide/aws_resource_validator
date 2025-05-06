from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kinesis_video_signaling.kinesis_video_signaling_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class GetIceServerConfigRequest(BaseValidatorModel):
    ChannelARN: str
    ClientId: Optional[str] = None
    Service: Optional[Literal['TURN']] = None
    Username: Optional[str] = None


class IceServer(BaseValidatorModel):
    Uris: Optional[List[str]] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    Ttl: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SendAlexaOfferToMasterRequest(BaseValidatorModel):
    ChannelARN: str
    SenderClientId: str
    MessagePayload: str


class GetIceServerConfigResponse(BaseValidatorModel):
    IceServerList: List[IceServer]
    ResponseMetadata: ResponseMetadata


class SendAlexaOfferToMasterResponse(BaseValidatorModel):
    Answer: str
    ResponseMetadata: ResponseMetadata