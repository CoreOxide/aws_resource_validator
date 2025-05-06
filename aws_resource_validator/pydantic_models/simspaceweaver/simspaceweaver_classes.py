from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.simspaceweaver.simspaceweaver_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CloudWatchLogsLogGroup(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class S3Destination(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None


class DeleteAppInput(BaseValidatorModel):
    App: str
    Domain: str
    Simulation: str


class DeleteSimulationInput(BaseValidatorModel):
    Simulation: str


class DescribeAppInput(BaseValidatorModel):
    App: str
    Domain: str
    Simulation: str


class LaunchOverridesOutput(BaseValidatorModel):
    LaunchCommands: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeSimulationInput(BaseValidatorModel):
    Simulation: str


class S3Location(BaseValidatorModel):
    BucketName: str
    ObjectKey: str


class Domain(BaseValidatorModel):
    Lifecycle: Optional[LifecycleManagementStrategyType] = None
    Name: Optional[str] = None


class LaunchOverrides(BaseValidatorModel):
    LaunchCommands: Optional[List[str]] = None


class ListAppsInput(BaseValidatorModel):
    Simulation: str
    Domain: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SimulationAppMetadata(BaseValidatorModel):
    Domain: Optional[str] = None
    Name: Optional[str] = None
    Simulation: Optional[str] = None
    Status: Optional[SimulationAppStatusType] = None
    TargetStatus: Optional[SimulationAppTargetStatusType] = None


class ListSimulationsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SimulationMetadata(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[SimulationStatusType] = None
    TargetStatus: Optional[SimulationTargetStatusType] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class SimulationClock(BaseValidatorModel):
    Status: Optional[ClockStatusType] = None
    TargetStatus: Optional[ClockTargetStatusType] = None


class SimulationAppPortMapping(BaseValidatorModel):
    Actual: Optional[int] = None
    Declared: Optional[int] = None


class StartClockInput(BaseValidatorModel):
    Simulation: str


class StopAppInput(BaseValidatorModel):
    App: str
    Domain: str
    Simulation: str


class StopClockInput(BaseValidatorModel):
    Simulation: str


class StopSimulationInput(BaseValidatorModel):
    Simulation: str


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class LogDestination(BaseValidatorModel):
    CloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroup] = None


class CreateSnapshotInput(BaseValidatorModel):
    Destination: S3Destination
    Simulation: str


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartAppOutput(BaseValidatorModel):
    Domain: str
    Name: str
    Simulation: str
    ResponseMetadata: ResponseMetadata


class StartSimulationOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    ExecutionId: str
    ResponseMetadata: ResponseMetadata


class StartSimulationInput(BaseValidatorModel):
    Name: str
    RoleArn: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    MaximumDuration: Optional[str] = None
    SchemaS3Location: Optional[S3Location] = None
    SnapshotS3Location: Optional[S3Location] = None
    Tags: Optional[Dict[str, str]] = None

LaunchOverridesUnion = Union[LaunchOverrides, LaunchOverridesOutput]


class ListAppsOutput(BaseValidatorModel):
    Apps: List[SimulationAppMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSimulationsOutput(BaseValidatorModel):
    Simulations: List[SimulationMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LiveSimulationState(BaseValidatorModel):
    Clocks: Optional[List[SimulationClock]] = None
    Domains: Optional[List[Domain]] = None


class SimulationAppEndpointInfo(BaseValidatorModel):
    Address: Optional[str] = None
    IngressPortMappings: Optional[List[SimulationAppPortMapping]] = None


class LoggingConfiguration(BaseValidatorModel):
    Destinations: Optional[List[LogDestination]] = None


class StartAppInput(BaseValidatorModel):
    Domain: str
    Name: str
    Simulation: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    LaunchOverrides: Optional[LaunchOverridesUnion] = None


class DescribeAppOutput(BaseValidatorModel):
    Description: str
    Domain: str
    EndpointInfo: SimulationAppEndpointInfo
    LaunchOverrides: LaunchOverridesOutput
    Name: str
    Simulation: str
    Status: SimulationAppStatusType
    TargetStatus: SimulationAppTargetStatusType
    ResponseMetadata: ResponseMetadata


class DescribeSimulationOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    ExecutionId: str
    LiveSimulationState: LiveSimulationState
    LoggingConfiguration: LoggingConfiguration
    MaximumDuration: str
    Name: str
    RoleArn: str
    SchemaError: str
    SchemaS3Location: S3Location
    SnapshotS3Location: S3Location
    StartError: str
    Status: SimulationStatusType
    TargetStatus: SimulationTargetStatusType
    ResponseMetadata: ResponseMetadata