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

class DeploymentModel(BaseValidatorModel):
    ModelHandle: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    DesiredState: Optional[ModelStateType] = None
    State: Optional[ModelStateType] = None
    Status: Optional[DeploymentStatusType] = None
    StatusReason: Optional[str] = None
    RollbackFailureReason: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetDeploymentsRequest(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str


class GetDeviceRegistrationRequest(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str


class Checksum(BaseValidatorModel):
    pass


class Definition(BaseValidatorModel):
    ModelHandle: Optional[str] = None
    S3Url: Optional[str] = None
    Checksum: Optional[Checksum] = None
    State: Optional[ModelStateType] = None


class Timestamp(BaseValidatorModel):
    pass


class DeploymentResult(BaseValidatorModel):
    DeploymentName: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentStatusMessage: Optional[str] = None
    DeploymentStartTime: Optional[Timestamp] = None
    DeploymentEndTime: Optional[Timestamp] = None
    DeploymentModels: Optional[Sequence[DeploymentModel]] = None


class EdgeMetric(BaseValidatorModel):
    Dimension: Optional[str] = None
    MetricName: Optional[str] = None
    Value: Optional[float] = None
    Timestamp: Optional[Timestamp] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDeviceRegistrationResult(BaseValidatorModel):
    DeviceRegistration: str
    CacheTTL: str
    ResponseMetadata: ResponseMetadata


class Model(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    LatestSampleTime: Optional[Timestamp] = None
    LatestInference: Optional[Timestamp] = None
    ModelMetrics: Optional[Sequence[EdgeMetric]] = None


class EdgeDeployment(BaseValidatorModel):
    pass


class GetDeploymentsResult(BaseValidatorModel):
    Deployments: List[EdgeDeployment]
    ResponseMetadata: ResponseMetadata


class SendHeartbeatRequest(BaseValidatorModel):
    AgentVersion: str
    DeviceName: str
    DeviceFleetName: str
    AgentMetrics: Optional[Sequence[EdgeMetric]] = None
    Models: Optional[Sequence[Model]] = None
    DeploymentResult: Optional[DeploymentResult] = None


