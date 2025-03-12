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
from aws_resource_validator.pydantic_models.workmailmessageflow_constants import *

class GetRawMessageContentRequestTypeDef(BaseValidatorModel):
    messageId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class S3ReferenceTypeDef(BaseValidatorModel):
    bucket: str
    key: str
    objectVersion: Optional[str] = None


class GetRawMessageContentResponseTypeDef(BaseValidatorModel):
    messageContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class RawMessageContentTypeDef(BaseValidatorModel):
    s3Reference: S3ReferenceTypeDef


class PutRawMessageContentRequestTypeDef(BaseValidatorModel):
    messageId: str
    content: RawMessageContentTypeDef


