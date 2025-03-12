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
from aws_resource_validator.pydantic_models.sagemaker_edge_constants import *

class DeploymentModelTypeDef(BaseValidatorModel):
    ModelHandle: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    DesiredState: Optional[ModelStateType] = None
    State: Optional[ModelStateType] = None
    Status: Optional[DeploymentStatusType] = None
    StatusReason: Optional[str] = None
    RollbackFailureReason: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetDeploymentsRequestTypeDef(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str


class GetDeviceRegistrationRequestTypeDef(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str


class ChecksumTypeDef(BaseValidatorModel):
    pass


class DefinitionTypeDef(BaseValidatorModel):
    ModelHandle: Optional[str] = None
    S3Url: Optional[str] = None
    Checksum: Optional[ChecksumTypeDef] = None
    State: Optional[ModelStateType] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DeploymentResultTypeDef(BaseValidatorModel):
    DeploymentName: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentStatusMessage: Optional[str] = None
    DeploymentStartTime: Optional[TimestampTypeDef] = None
    DeploymentEndTime: Optional[TimestampTypeDef] = None
    DeploymentModels: Optional[Sequence[DeploymentModelTypeDef]] = None


class EdgeMetricTypeDef(BaseValidatorModel):
    Dimension: Optional[str] = None
    MetricName: Optional[str] = None
    Value: Optional[float] = None
    Timestamp: Optional[TimestampTypeDef] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeviceRegistrationResultTypeDef(BaseValidatorModel):
    DeviceRegistration: str
    CacheTTL: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModelTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    LatestSampleTime: Optional[TimestampTypeDef] = None
    LatestInference: Optional[TimestampTypeDef] = None
    ModelMetrics: Optional[Sequence[EdgeMetricTypeDef]] = None


class EdgeDeploymentTypeDef(BaseValidatorModel):
    pass


class GetDeploymentsResultTypeDef(BaseValidatorModel):
    Deployments: List[EdgeDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SendHeartbeatRequestTypeDef(BaseValidatorModel):
    AgentVersion: str
    DeviceName: str
    DeviceFleetName: str
    AgentMetrics: Optional[Sequence[EdgeMetricTypeDef]] = None
    Models: Optional[Sequence[ModelTypeDef]] = None
    DeploymentResult: Optional[DeploymentResultTypeDef] = None


