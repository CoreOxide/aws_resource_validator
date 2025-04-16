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
from aws_resource_validator.pydantic_models.kinesis_video_signaling_constants import *

class GetIceServerConfigRequest(BaseValidatorModel):
    ChannelARN: str
    ClientId: Optional[str] = None
    Service: Optional[Literal["TURN"]] = None
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


