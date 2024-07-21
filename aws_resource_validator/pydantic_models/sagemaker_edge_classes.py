from datetime import datetime
from pydantic import BaseModel
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

class ChecksumTypeDef(BaseModel):
    Type: Optional[Literal["SHA1"]] = None
    Sum: Optional[str] = None

class DeploymentModelTypeDef(BaseModel):
    ModelHandle: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    DesiredState: Optional[ModelStateType] = None
    State: Optional[ModelStateType] = None
    Status: Optional[DeploymentStatusType] = None
    StatusReason: Optional[str] = None
    RollbackFailureReason: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetDeploymentsRequestRequestTypeDef(BaseModel):
    DeviceName: str
    DeviceFleetName: str

class GetDeviceRegistrationRequestRequestTypeDef(BaseModel):
    DeviceName: str
    DeviceFleetName: str

class DefinitionTypeDef(BaseModel):
    ModelHandle: Optional[str] = None
    S3Url: Optional[str] = None
    Checksum: Optional[ChecksumTypeDef] = None
    State: Optional[ModelStateType] = None

class DeploymentResultTypeDef(BaseModel):
    DeploymentName: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentStatusMessage: Optional[str] = None
    DeploymentStartTime: Optional[TimestampTypeDef] = None
    DeploymentEndTime: Optional[TimestampTypeDef] = None
    DeploymentModels: Optional[Sequence[DeploymentModelTypeDef]] = None

class EdgeMetricTypeDef(BaseModel):
    Dimension: Optional[str] = None
    MetricName: Optional[str] = None
    Value: Optional[float] = None
    Timestamp: Optional[TimestampTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceRegistrationResultTypeDef(BaseModel):
    DeviceRegistration: str
    CacheTTL: str
    ResponseMetadata: ResponseMetadataTypeDef

class EdgeDeploymentTypeDef(BaseModel):
    DeploymentName: Optional[str] = None
    Type: Optional[Literal["Model"]] = None
    FailureHandlingPolicy: Optional[FailureHandlingPolicyType] = None
    Definitions: Optional[List[DefinitionTypeDef]] = None

class ModelTypeDef(BaseModel):
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    LatestSampleTime: Optional[TimestampTypeDef] = None
    LatestInference: Optional[TimestampTypeDef] = None
    ModelMetrics: Optional[Sequence[EdgeMetricTypeDef]] = None

class GetDeploymentsResultTypeDef(BaseModel):
    Deployments: List[EdgeDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendHeartbeatRequestRequestTypeDef(BaseModel):
    AgentVersion: str
    DeviceName: str
    DeviceFleetName: str
    AgentMetrics: Optional[Sequence[EdgeMetricTypeDef]] = None
    Models: Optional[Sequence[ModelTypeDef]] = None
    DeploymentResult: Optional[DeploymentResultTypeDef] = None

