from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Blueprint(BaseValidatorModel):
    blueprintArn: str
    version: Optional[str] = None
    stage: Optional[BlueprintStageType] = None


class DataAutomationConfiguration(BaseValidatorModel):
    dataAutomationProjectArn: str
    stage: Optional[DataAutomationStageType] = None


class EncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: str
    kmsEncryptionContext: Optional[Dict[str, str]] = None


class EventBridgeConfiguration(BaseValidatorModel):
    eventBridgeEnabled: bool


# This class is the input for the 'get_data_automation_status' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


class NotificationConfiguration(BaseValidatorModel):
    eventBridgeConfiguration: EventBridgeConfiguration


# This class is the output for the 'get_data_automation_status' function.
class GetDataAutomationStatusResponse(BaseValidatorModel):
    status: AutomationJobStatusType
    errorType: str
    errorMessage: str
    outputConfiguration: OutputConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'invoke_data_automation_async' function.
class InvokeDataAutomationAsyncResponse(BaseValidatorModel):
    invocationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: List[Tag]


# This class is the input for the 'invoke_data_automation_async' function.
class InvokeDataAutomationAsyncRequest(BaseValidatorModel):
    inputConfiguration: InputConfiguration
    outputConfiguration: OutputConfiguration
    dataAutomationProfileArn: str
    clientToken: Optional[str] = None
    dataAutomationConfiguration: Optional[DataAutomationConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None
    notificationConfiguration: Optional[NotificationConfiguration] = None
    blueprints: Optional[List[Blueprint]] = None
    tags: Optional[List[Tag]] = None