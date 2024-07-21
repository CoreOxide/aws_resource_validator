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
from aws_resource_validator.pydantic_models.workmailmessageflow_constants import *

class GetRawMessageContentRequestRequestTypeDef(BaseModel):
    messageId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class S3ReferenceTypeDef(BaseModel):
    bucket: str
    key: str
    objectVersion: Optional[str] = None

class GetRawMessageContentResponseTypeDef(BaseModel):
    messageContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class RawMessageContentTypeDef(BaseModel):
    s3Reference: S3ReferenceTypeDef

class PutRawMessageContentRequestRequestTypeDef(BaseModel):
    messageId: str
    content: RawMessageContentTypeDef

