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
from aws_resource_validator.pydantic_models.simspaceweaver_constants import *

class CloudWatchLogsLogGroupTypeDef(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class S3DestinationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None


class DeleteAppInputTypeDef(BaseValidatorModel):
    App: str
    Domain: str
    Simulation: str


class DeleteSimulationInputTypeDef(BaseValidatorModel):
    Simulation: str


class DescribeAppInputTypeDef(BaseValidatorModel):
    App: str
    Domain: str
    Simulation: str


class LaunchOverridesOutputTypeDef(BaseValidatorModel):
    LaunchCommands: Optional[List[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeSimulationInputTypeDef(BaseValidatorModel):
    Simulation: str


class S3LocationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKey: str


class DomainTypeDef(BaseValidatorModel):
    Lifecycle: Optional[LifecycleManagementStrategyType] = None
    Name: Optional[str] = None


class LaunchOverridesTypeDef(BaseValidatorModel):
    LaunchCommands: Optional[Sequence[str]] = None


class ListAppsInputTypeDef(BaseValidatorModel):
    Simulation: str
    Domain: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SimulationAppMetadataTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    Name: Optional[str] = None
    Simulation: Optional[str] = None
    Status: Optional[SimulationAppStatusType] = None
    TargetStatus: Optional[SimulationAppTargetStatusType] = None


class ListSimulationsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SimulationMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[SimulationStatusType] = None
    TargetStatus: Optional[SimulationTargetStatusType] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class SimulationClockTypeDef(BaseValidatorModel):
    Status: Optional[ClockStatusType] = None
    TargetStatus: Optional[ClockTargetStatusType] = None


class SimulationAppPortMappingTypeDef(BaseValidatorModel):
    Actual: Optional[int] = None
    Declared: Optional[int] = None


class StartClockInputTypeDef(BaseValidatorModel):
    Simulation: str


class StopAppInputTypeDef(BaseValidatorModel):
    App: str
    Domain: str
    Simulation: str


class StopClockInputTypeDef(BaseValidatorModel):
    Simulation: str


class StopSimulationInputTypeDef(BaseValidatorModel):
    Simulation: str


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class LogDestinationTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroupTypeDef] = None


class CreateSnapshotInputTypeDef(BaseValidatorModel):
    Destination: S3DestinationTypeDef
    Simulation: str


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartAppOutputTypeDef(BaseValidatorModel):
    Domain: str
    Name: str
    Simulation: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartSimulationOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    ExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartSimulationInputTypeDef(BaseValidatorModel):
    Name: str
    RoleArn: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    MaximumDuration: Optional[str] = None
    SchemaS3Location: Optional[S3LocationTypeDef] = None
    SnapshotS3Location: Optional[S3LocationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class ListAppsOutputTypeDef(BaseValidatorModel):
    Apps: List[SimulationAppMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSimulationsOutputTypeDef(BaseValidatorModel):
    Simulations: List[SimulationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LiveSimulationStateTypeDef(BaseValidatorModel):
    Clocks: Optional[List[SimulationClockTypeDef]] = None
    Domains: Optional[List[DomainTypeDef]] = None


class SimulationAppEndpointInfoTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    IngressPortMappings: Optional[List[SimulationAppPortMappingTypeDef]] = None


class LoggingConfigurationTypeDef(BaseValidatorModel):
    Destinations: Optional[List[LogDestinationTypeDef]] = None


class LaunchOverridesUnionTypeDef(BaseValidatorModel):
    pass


class StartAppInputTypeDef(BaseValidatorModel):
    Domain: str
    Name: str
    Simulation: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    LaunchOverrides: Optional[LaunchOverridesUnionTypeDef] = None


class DescribeAppOutputTypeDef(BaseValidatorModel):
    Description: str
    Domain: str
    EndpointInfo: SimulationAppEndpointInfoTypeDef
    LaunchOverrides: LaunchOverridesOutputTypeDef
    Name: str
    Simulation: str
    Status: SimulationAppStatusType
    TargetStatus: SimulationAppTargetStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSimulationOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    ExecutionId: str
    LiveSimulationState: LiveSimulationStateTypeDef
    LoggingConfiguration: LoggingConfigurationTypeDef
    MaximumDuration: str
    Name: str
    RoleArn: str
    SchemaError: str
    SchemaS3Location: S3LocationTypeDef
    SnapshotS3Location: S3LocationTypeDef
    StartError: str
    Status: SimulationStatusType
    TargetStatus: SimulationTargetStatusType
    ResponseMetadata: ResponseMetadataTypeDef


