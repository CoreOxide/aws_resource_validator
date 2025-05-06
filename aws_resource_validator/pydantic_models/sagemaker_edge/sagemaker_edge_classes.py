from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Checksum(BaseValidatorModel):
    Type: Optional[Literal['SHA1']] = None
    Sum: Optional[str] = None


class DeploymentModel(BaseValidatorModel):
    ModelHandle: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    DesiredState: Optional[ModelStateType] = None
    State: Optional[ModelStateType] = None
    Status: Optional[DeploymentStatusType] = None
    StatusReason: Optional[str] = None
    RollbackFailureReason: Optional[str] = None

Timestamp = Union[datetime, str]


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


class Definition(BaseValidatorModel):
    ModelHandle: Optional[str] = None
    S3Url: Optional[str] = None
    Checksum: Optional[Checksum] = None
    State: Optional[ModelStateType] = None


class DeploymentResult(BaseValidatorModel):
    DeploymentName: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentStatusMessage: Optional[str] = None
    DeploymentStartTime: Optional[Timestamp] = None
    DeploymentEndTime: Optional[Timestamp] = None
    DeploymentModels: Optional[List[DeploymentModel]] = None


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


class EdgeDeployment(BaseValidatorModel):
    DeploymentName: Optional[str] = None
    Type: Optional[Literal['Model']] = None
    FailureHandlingPolicy: Optional[FailureHandlingPolicyType] = None
    Definitions: Optional[List[Definition]] = None


class Model(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    LatestSampleTime: Optional[Timestamp] = None
    LatestInference: Optional[Timestamp] = None
    ModelMetrics: Optional[List[EdgeMetric]] = None


class GetDeploymentsResult(BaseValidatorModel):
    Deployments: List[EdgeDeployment]
    ResponseMetadata: ResponseMetadata


class SendHeartbeatRequest(BaseValidatorModel):
    AgentVersion: str
    DeviceName: str
    DeviceFleetName: str
    AgentMetrics: Optional[List[EdgeMetric]] = None
    Models: Optional[List[Model]] = None
    DeploymentResult: Optional[DeploymentResult] = None