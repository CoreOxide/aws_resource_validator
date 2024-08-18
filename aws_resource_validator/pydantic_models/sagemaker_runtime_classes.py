from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class InvokeEndpointAsyncInputRequestTypeDef(BaseValidatorModel):
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ModelStreamErrorTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    ErrorCode: Optional[str] = None

class PayloadPartTypeDef(BaseValidatorModel):
    Bytes: Optional[bytes] = None

class InvokeEndpointInputRequestTypeDef(BaseValidatorModel):
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

class InvokeEndpointWithResponseStreamInputRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    Body: BlobTypeDef
    ContentType: Optional[str] = None
    Accept: Optional[str] = None
    CustomAttributes: Optional[str] = None
    TargetVariant: Optional[str] = None
    TargetContainerHostname: Optional[str] = None
    InferenceId: Optional[str] = None
    InferenceComponentName: Optional[str] = None

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
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseStreamTypeDef(BaseValidatorModel):
    PayloadPart: Optional[PayloadPartTypeDef] = None
    ModelStreamError: Optional[ModelStreamErrorTypeDef] = None
    InternalStreamFailure: Optional[InternalStreamFailureTypeDef] = None

class InvokeEndpointWithResponseStreamOutputTypeDef(BaseValidatorModel):
    Body: "EventStream[ResponseStreamTypeDef]"
    ContentType: str
    InvokedProductionVariant: str
    CustomAttributes: str
    ResponseMetadata: ResponseMetadataTypeDef

