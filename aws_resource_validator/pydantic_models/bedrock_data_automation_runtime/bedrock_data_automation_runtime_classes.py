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
    tagKeys: List[str]


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
    tags: List[Tag]


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