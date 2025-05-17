from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kinesis_video_media.kinesis_video_media_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the output for the 'get_media' function.
class GetMediaOutput(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class StartSelector(BaseValidatorModel):
    StartSelectorType: StartSelectorTypeType
    AfterFragmentNumber: Optional[str] = None
    StartTimestamp: Optional[Timestamp] = None
    ContinuationToken: Optional[str] = None


# This class is the input for the 'get_media' function.
class GetMediaInput(BaseValidatorModel):
    StartSelector: StartSelector
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None