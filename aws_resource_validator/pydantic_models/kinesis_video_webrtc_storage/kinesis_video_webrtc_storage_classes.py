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


class JoinStorageSessionAsViewerInput(BaseValidatorModel):
    channelArn: str
    clientId: str


class JoinStorageSessionInput(BaseValidatorModel):
    channelArn: str


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata