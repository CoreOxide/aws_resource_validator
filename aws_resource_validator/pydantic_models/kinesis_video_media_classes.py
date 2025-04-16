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
from aws_resource_validator.pydantic_models.kinesis_video_media_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetMediaOutput(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class StartSelector(BaseValidatorModel):
    StartSelectorType: StartSelectorTypeType
    AfterFragmentNumber: Optional[str] = None
    StartTimestamp: Optional[Timestamp] = None
    ContinuationToken: Optional[str] = None


class GetMediaInput(BaseValidatorModel):
    StartSelector: StartSelector
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


