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
from aws_resource_validator.pydantic_models.bedrock_data_automation_runtime_constants import *

class Blueprint(BaseValidatorModel):
    blueprintArn: str
    version: Optional[str] = None
    stage: Optional[BlueprintStageType] = None


class DataAutomationConfiguration(BaseValidatorModel):
    dataAutomationProjectArn: str
    stage: Optional[DataAutomationStageType] = None


class EncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: str
    kmsEncryptionContext: Optional[Mapping[str, str]] = None


class EventBridgeConfiguration(BaseValidatorModel):
    eventBridgeEnabled: bool


class GetDataAutomationStatusRequest(BaseValidatorModel):
    invocationArn: str


class OutputConfiguration(BaseValidatorModel):
    s3Uri: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InputConfiguration(BaseValidatorModel):
    s3Uri: str


class Tag(BaseValidatorModel):
    key: str
    value: str


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class NotificationConfiguration(BaseValidatorModel):
    eventBridgeConfiguration: EventBridgeConfiguration


class GetDataAutomationStatusResponse(BaseValidatorModel):
    status: AutomationJobStatusType
    errorType: str
    errorMessage: str
    outputConfiguration: OutputConfiguration
    ResponseMetadata: ResponseMetadata


class InvokeDataAutomationAsyncResponse(BaseValidatorModel):
    invocationArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[Tag]


class InvokeDataAutomationAsyncRequest(BaseValidatorModel):
    inputConfiguration: InputConfiguration
    outputConfiguration: OutputConfiguration
    dataAutomationProfileArn: str
    clientToken: Optional[str] = None
    dataAutomationConfiguration: Optional[DataAutomationConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None
    notificationConfiguration: Optional[NotificationConfiguration] = None
    blueprints: Optional[Sequence[Blueprint]] = None
    tags: Optional[Sequence[Tag]] = None


