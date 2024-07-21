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
from aws_resource_validator.pydantic_models.kinesis_video_media_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetMediaOutputTypeDef(BaseModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class StartSelectorTypeDef(BaseModel):
    StartSelectorType: StartSelectorTypeType
    AfterFragmentNumber: Optional[str] = None
    StartTimestamp: Optional[TimestampTypeDef] = None
    ContinuationToken: Optional[str] = None

class GetMediaInputRequestTypeDef(BaseModel):
    StartSelector: StartSelectorTypeDef
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

