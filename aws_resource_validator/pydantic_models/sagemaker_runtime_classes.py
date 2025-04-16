from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream
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
from aws_resource_validator.pydantic_models.sagemaker_runtime_constants import *

class InternalStreamFailure(BaseValidatorModel):
    Message: Optional[str] = None


class InvokeEndpointAsyncInput(BaseValidatorModel):
    EndpointName: str
    InputLocation: str
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    InferenceId: Optional[str] = None
    RequestTTLSeconds: Optional[int] = None
    InvocationTimeoutSeconds: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ModelStreamError(BaseValidatorModel):
    Message: Optional[str] = None
    ErrorCode: Optional[str] = None


class PayloadPart(BaseValidatorModel):
    Bytes: Optional[bytes] = None


class Blob(BaseValidatorModel):
    pass


class InvokeEndpointInput(BaseValidatorModel):
    EndpointName: str
    Body: Blob
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    TargetModel: Optional[str] = None
    TargetVariant: Optional[str] = None
    TargetContainerHostname: Optional[str] = None
    InferenceId: Optional[str] = None
    EnableExplanations: Optional[str] = None
    InferenceComponentName: Optional[str] = None
    SessionId: Optional[str] = None


class InvokeEndpointWithResponseStreamInput(BaseValidatorModel):
    EndpointName: str
    Body: Blob
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    TargetVariant: Optional[str] = None
    TargetContainerHostname: Optional[str] = None
    InferenceId: Optional[str] = None
    InferenceComponentName: Optional[str] = None
    SessionId: Optional[str] = None


class InvokeEndpointAsyncOutput(BaseValidatorModel):
    InferenceId: str
    OutputLocation: str
    FailureLocation: str
    ResponseMetadata: ResponseMetadata


class InvokeEndpointOutput(BaseValidatorModel):
    Body: StreamingBody
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    NewSessionId: str
    ClosedSessionId: str
    ResponseMetadata: ResponseMetadata


class ResponseStream(BaseValidatorModel):
    PayloadPart: Optional[PayloadPart] = None
    ModelStreamError: Optional[ModelStreamError] = None
    InternalStreamFailure: Optional[InternalStreamFailure] = None


class InvokeEndpointWithResponseStreamOutput(BaseValidatorModel):
    Body: EventStream[ResponseStream]
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    ResponseMetadata: ResponseMetadata


