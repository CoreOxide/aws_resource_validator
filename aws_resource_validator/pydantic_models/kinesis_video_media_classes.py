from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.kinesis_video_media_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetMediaOutputTypeDef(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class StartSelectorTypeDef(BaseValidatorModel):
    StartSelectorType: StartSelectorTypeType
    AfterFragmentNumber: Optional[str] = None
    StartTimestamp: Optional[TimestampTypeDef] = None
    ContinuationToken: Optional[str] = None

class GetMediaInputRequestTypeDef(BaseValidatorModel):
    StartSelector: StartSelectorTypeDef
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

