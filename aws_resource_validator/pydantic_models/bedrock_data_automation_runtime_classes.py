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

class BlueprintTypeDef(BaseValidatorModel):
    blueprintArn: str
    version: Optional[str] = None
    stage: Optional[BlueprintStageType] = None


class DataAutomationConfigurationTypeDef(BaseValidatorModel):
    dataAutomationProjectArn: str
    stage: Optional[DataAutomationStageType] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: str
    kmsEncryptionContext: Optional[Mapping[str, str]] = None


class EventBridgeConfigurationTypeDef(BaseValidatorModel):
    eventBridgeEnabled: bool


class GetDataAutomationStatusRequestTypeDef(BaseValidatorModel):
    invocationArn: str


class OutputConfigurationTypeDef(BaseValidatorModel):
    s3Uri: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InputConfigurationTypeDef(BaseValidatorModel):
    s3Uri: str


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class NotificationConfigurationTypeDef(BaseValidatorModel):
    eventBridgeConfiguration: EventBridgeConfigurationTypeDef


class GetDataAutomationStatusResponseTypeDef(BaseValidatorModel):
    status: AutomationJobStatusType
    errorType: str
    errorMessage: str
    outputConfiguration: OutputConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeDataAutomationAsyncResponseTypeDef(BaseValidatorModel):
    invocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]


class InvokeDataAutomationAsyncRequestTypeDef(BaseValidatorModel):
    inputConfiguration: InputConfigurationTypeDef
    outputConfiguration: OutputConfigurationTypeDef
    dataAutomationProfileArn: str
    clientToken: Optional[str] = None
    dataAutomationConfiguration: Optional[DataAutomationConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    notificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    blueprints: Optional[Sequence[BlueprintTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


