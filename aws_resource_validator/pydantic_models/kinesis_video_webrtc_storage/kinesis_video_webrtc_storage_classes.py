from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kinesis_video_webrtc_storage.kinesis_video_webrtc_storage_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'join_storage_session_as_viewer' function.
class JoinStorageSessionAsViewerInput(BaseValidatorModel):
    channelArn: str
    clientId: str


# This class is the input for the 'join_storage_session' function.
class JoinStorageSessionInput(BaseValidatorModel):
    channelArn: str


# This class is the output for the 'join_storage_session_as_viewer' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata