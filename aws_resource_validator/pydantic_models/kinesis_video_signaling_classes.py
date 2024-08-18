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
from aws_resource_validator.pydantic_models.kinesis_video_signaling_constants import *

class GetIceServerConfigRequestRequestTypeDef(BaseValidatorModel):
    ChannelARN: str
    ClientId: Optional[str] = None
    Service: Optional[Literal["TURN"]] = None
    Username: Optional[str] = None

class IceServerTypeDef(BaseValidatorModel):
    Uris: Optional[List[str]] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    Ttl: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class SendAlexaOfferToMasterRequestRequestTypeDef(BaseValidatorModel):
    ChannelARN: str
    SenderClientId: str
    MessagePayload: str

class GetIceServerConfigResponseTypeDef(BaseValidatorModel):
    IceServerList: List[IceServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendAlexaOfferToMasterResponseTypeDef(BaseValidatorModel):
    Answer: str
    ResponseMetadata: ResponseMetadataTypeDef

