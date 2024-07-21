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
from aws_resource_validator.pydantic_models.sagemaker_runtime_constants import *

class InternalStreamFailureTypeDef(BaseModel):
    Message: Optional[str] = None

class InvokeEndpointAsyncInputRequestTypeDef(BaseModel):
    EndpointName: str
    InputLocation: str
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    InferenceId: Optional[str] = None
    RequestTTLSeconds: Optional[int] = None
    InvocationTimeoutSeconds: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ModelStreamErrorTypeDef(BaseModel):
    Message: Optional[str] = None
    ErrorCode: Optional[str] = None

class PayloadPartTypeDef(BaseModel):
    Bytes: Optional[bytes] = None

class InvokeEndpointInputRequestTypeDef(BaseModel):
    EndpointName: str
    Body: BlobTypeDef
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    TargetModel: Optional[str] = None
    TargetVariant: Optional[str] = None
    TargetContainerHostname: Optional[str] = None
    InferenceId: Optional[str] = None
    EnableExplanations: Optional[str] = None
    InferenceComponentName: Optional[str] = None

class InvokeEndpointWithResponseStreamInputRequestTypeDef(BaseModel):
    EndpointName: str
    Body: BlobTypeDef
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    TargetVariant: Optional[str] = None
    TargetContainerHostname: Optional[str] = None
    InferenceId: Optional[str] = None
    InferenceComponentName: Optional[str] = None

class InvokeEndpointAsyncOutputTypeDef(BaseModel):
    InferenceId: str
    OutputLocation: str
    FailureLocation: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeEndpointOutputTypeDef(BaseModel):
    Body: StreamingBody
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseStreamTypeDef(BaseModel):
    PayloadPart: Optional[PayloadPartTypeDef] = None
    ModelStreamError: Optional[ModelStreamErrorTypeDef] = None
    InternalStreamFailure: Optional[InternalStreamFailureTypeDef] = None

class InvokeEndpointWithResponseStreamOutputTypeDef(BaseModel):
    Body: "EventStream[ResponseStreamTypeDef]"
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    ResponseMetadata: ResponseMetadataTypeDef

