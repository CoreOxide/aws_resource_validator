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
from aws_resource_validator.pydantic_models.sagemaker_runtime_constants import *

class InternalStreamFailureTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class InvokeEndpointAsyncInputTypeDef(BaseValidatorModel):
    EndpointName: str
    InputLocation: str
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    InferenceId: Optional[str] = None
    RequestTTLSeconds: Optional[int] = None
    InvocationTimeoutSeconds: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ModelStreamErrorTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    ErrorCode: Optional[str] = None


class PayloadPartTypeDef(BaseValidatorModel):
    Bytes: Optional[bytes] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class InvokeEndpointInputTypeDef(BaseValidatorModel):
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
    SessionId: Optional[str] = None


class InvokeEndpointWithResponseStreamInputTypeDef(BaseValidatorModel):
    EndpointName: str
    Body: BlobTypeDef
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    TargetVariant: Optional[str] = None
    TargetContainerHostname: Optional[str] = None
    InferenceId: Optional[str] = None
    InferenceComponentName: Optional[str] = None
    SessionId: Optional[str] = None


class InvokeEndpointAsyncOutputTypeDef(BaseValidatorModel):
    InferenceId: str
    OutputLocation: str
    FailureLocation: str
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeEndpointOutputTypeDef(BaseValidatorModel):
    Body: StreamingBody
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    NewSessionId: str
    ClosedSessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResponseStreamTypeDef(BaseValidatorModel):
    PayloadPart: Optional[PayloadPartTypeDef] = None
    ModelStreamError: Optional[ModelStreamErrorTypeDef] = None
    InternalStreamFailure: Optional[InternalStreamFailureTypeDef] = None


class InvokeEndpointWithResponseStreamOutputTypeDef(BaseValidatorModel):
    Body: EventStream[ResponseStreamTypeDef]
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    ResponseMetadata: ResponseMetadataTypeDef


