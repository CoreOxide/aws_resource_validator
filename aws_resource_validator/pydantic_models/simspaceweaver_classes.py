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
from aws_resource_validator.pydantic_models.simspaceweaver_constants import *

class CloudWatchLogsLogGroupTypeDef(BaseModel):
    LogGroupArn: Optional[str] = None

class S3DestinationTypeDef(BaseModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None

class DeleteAppInputRequestTypeDef(BaseModel):
    App: str
    Domain: str
    Simulation: str

class DeleteSimulationInputRequestTypeDef(BaseModel):
    Simulation: str

class DescribeAppInputRequestTypeDef(BaseModel):
    App: str
    Domain: str
    Simulation: str

class LaunchOverridesTypeDef(BaseModel):
    LaunchCommands: Optional[List[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeSimulationInputRequestTypeDef(BaseModel):
    Simulation: str

class S3LocationTypeDef(BaseModel):
    BucketName: str
    ObjectKey: str

class DomainTypeDef(BaseModel):
    Lifecycle: Optional[LifecycleManagementStrategyType] = None
    Name: Optional[str] = None

class ListAppsInputRequestTypeDef(BaseModel):
    Simulation: str
    Domain: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SimulationAppMetadataTypeDef(BaseModel):
    Domain: Optional[str] = None
    Name: Optional[str] = None
    Simulation: Optional[str] = None
    Status: Optional[SimulationAppStatusType] = None
    TargetStatus: Optional[SimulationAppTargetStatusType] = None

class ListSimulationsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SimulationMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Name: Optional[str] = None
    Status: Optional[SimulationStatusType] = None
    TargetStatus: Optional[SimulationTargetStatusType] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class SimulationClockTypeDef(BaseModel):
    Status: Optional[ClockStatusType] = None
    TargetStatus: Optional[ClockTargetStatusType] = None

class SimulationAppPortMappingTypeDef(BaseModel):
    Actual: Optional[int] = None
    Declared: Optional[int] = None

class StartClockInputRequestTypeDef(BaseModel):
    Simulation: str

class StopAppInputRequestTypeDef(BaseModel):
    App: str
    Domain: str
    Simulation: str

class StopClockInputRequestTypeDef(BaseModel):
    Simulation: str

class StopSimulationInputRequestTypeDef(BaseModel):
    Simulation: str

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class LogDestinationTypeDef(BaseModel):
    CloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroupTypeDef] = None

class CreateSnapshotInputRequestTypeDef(BaseModel):
    Destination: S3DestinationTypeDef
    Simulation: str

class StartAppInputRequestTypeDef(BaseModel):
    Domain: str
    Name: str
    Simulation: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    LaunchOverrides: Optional[LaunchOverridesTypeDef] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAppOutputTypeDef(BaseModel):
    Domain: str
    Name: str
    Simulation: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSimulationOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    ExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSimulationInputRequestTypeDef(BaseModel):
    Name: str
    RoleArn: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    MaximumDuration: Optional[str] = None
    SchemaS3Location: Optional[S3LocationTypeDef] = None
    SnapshotS3Location: Optional[S3LocationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class ListAppsOutputTypeDef(BaseModel):
    Apps: List[SimulationAppMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSimulationsOutputTypeDef(BaseModel):
    NextToken: str
    Simulations: List[SimulationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LiveSimulationStateTypeDef(BaseModel):
    Clocks: Optional[List[SimulationClockTypeDef]] = None
    Domains: Optional[List[DomainTypeDef]] = None

class SimulationAppEndpointInfoTypeDef(BaseModel):
    Address: Optional[str] = None
    IngressPortMappings: Optional[List[SimulationAppPortMappingTypeDef]] = None

class LoggingConfigurationTypeDef(BaseModel):
    Destinations: Optional[List[LogDestinationTypeDef]] = None

class DescribeAppOutputTypeDef(BaseModel):
    Description: str
    Domain: str
    EndpointInfo: SimulationAppEndpointInfoTypeDef
    LaunchOverrides: LaunchOverridesTypeDef
    Name: str
    Simulation: str
    Status: SimulationAppStatusType
    TargetStatus: SimulationAppTargetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationOutputTypeDef(BaseModel):
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

