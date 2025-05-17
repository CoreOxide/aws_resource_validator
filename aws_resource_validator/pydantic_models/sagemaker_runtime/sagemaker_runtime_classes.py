from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker_runtime.sagemaker_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class InternalStreamFailure(BaseValidatorModel):
    Message: Optional[str] = None


# This class is the input for the 'invoke_endpoint_async' function.
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


# This class is the input for the 'invoke_endpoint' function.
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


# This class is the input for the 'invoke_endpoint_with_response_stream' function.
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


# This class is the output for the 'invoke_endpoint_async' function.
class InvokeEndpointAsyncOutput(BaseValidatorModel):
    InferenceId: str
    OutputLocation: str
    FailureLocation: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'invoke_endpoint' function.
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


# This class is the output for the 'invoke_endpoint_with_response_stream' function.
class InvokeEndpointWithResponseStreamOutput(BaseValidatorModel):
    Body: EventStream[ResponseStream]
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    ResponseMetadata: ResponseMetadata