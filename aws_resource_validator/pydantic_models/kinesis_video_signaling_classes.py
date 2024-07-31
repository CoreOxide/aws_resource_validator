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
from aws_resource_validator.pydantic_models.kinesis_video_signaling_constants import *

class GetIceServerConfigRequestRequestTypeDef(BaseModel):
    ChannelARN: str
    ClientId: Optional[str] = None
    Service: Optional[Literal["TURN"]] = None
    Username: Optional[str] = None

class IceServerTypeDef(BaseModel):
    Uris: Optional[List[str]] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    Ttl: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class SendAlexaOfferToMasterRequestRequestTypeDef(BaseModel):
    ChannelARN: str
    SenderClientId: str
    MessagePayload: str

class GetIceServerConfigResponseTypeDef(BaseModel):
    IceServerList: List[IceServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendAlexaOfferToMasterResponseTypeDef(BaseModel):
    Answer: str
    ResponseMetadata: ResponseMetadataTypeDef

