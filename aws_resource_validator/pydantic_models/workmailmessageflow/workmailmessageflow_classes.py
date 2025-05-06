from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workmailmessageflow.workmailmessageflow_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class GetRawMessageContentRequest(BaseValidatorModel):
    messageId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class S3Reference(BaseValidatorModel):
    bucket: str
    key: str
    objectVersion: Optional[str] = None


class GetRawMessageContentResponse(BaseValidatorModel):
    messageContent: StreamingBody
    ResponseMetadata: ResponseMetadata


class RawMessageContent(BaseValidatorModel):
    s3Reference: S3Reference


class PutRawMessageContentRequest(BaseValidatorModel):
    messageId: str
    content: RawMessageContent