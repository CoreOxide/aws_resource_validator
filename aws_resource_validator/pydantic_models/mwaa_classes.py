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
from aws_resource_validator.pydantic_models.mwaa_constants import *

class CreateCliTokenRequestRequestTypeDef(BaseModel):
    Name: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class NetworkConfigurationTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class CreateWebLoginTokenRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteEnvironmentInputRequestTypeDef(BaseModel):
    Name: str

class DimensionTypeDef(BaseModel):
    Name: str
    Value: str

class NetworkConfigurationOutputTypeDef(BaseModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class GetEnvironmentInputRequestTypeDef(BaseModel):
    Name: str

class UpdateErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEnvironmentsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class ModuleLoggingConfigurationInputTypeDef(BaseModel):
    Enabled: bool
    LogLevel: LoggingLevelType

class ModuleLoggingConfigurationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LogLevel: Optional[LoggingLevelType] = None
    CloudWatchLogGroupArn: Optional[str] = None

class StatisticSetTypeDef(BaseModel):
    SampleCount: Optional[int] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    tagKeys: Sequence[str]

class UpdateNetworkConfigurationInputTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]

class CreateCliTokenResponseTypeDef(BaseModel):
    CliToken: str
    WebServerHostname: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebLoginTokenResponseTypeDef(BaseModel):
    WebToken: str
    WebServerHostname: str
    IamIdentity: str
    AirflowIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsOutputTypeDef(BaseModel):
    Environments: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class LastUpdateTypeDef(BaseModel):
    Status: Optional[UpdateStatusType] = None
    CreatedAt: Optional[datetime] = None
    Error: Optional[UpdateErrorTypeDef] = None
    Source: Optional[str] = None

class ListEnvironmentsInputListEnvironmentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LoggingConfigurationInputTypeDef(BaseModel):
    DagProcessingLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    SchedulerLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    WebserverLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    WorkerLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    TaskLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None

class LoggingConfigurationTypeDef(BaseModel):
    DagProcessingLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    SchedulerLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    WebserverLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    WorkerLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    TaskLogs: Optional[ModuleLoggingConfigurationTypeDef] = None

class MetricDatumTypeDef(BaseModel):
    MetricName: str
    Timestamp: TimestampTypeDef
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Value: Optional[float] = None
    Unit: Optional[UnitType] = None
    StatisticValues: Optional[StatisticSetTypeDef] = None

class CreateEnvironmentInputRequestTypeDef(BaseModel):
    Name: str
    ExecutionRoleArn: str
    SourceBucketArn: str
    DagS3Path: str
    NetworkConfiguration: NetworkConfigurationTypeDef
    PluginsS3Path: Optional[str] = None
    PluginsS3ObjectVersion: Optional[str] = None
    RequirementsS3Path: Optional[str] = None
    RequirementsS3ObjectVersion: Optional[str] = None
    StartupScriptS3Path: Optional[str] = None
    StartupScriptS3ObjectVersion: Optional[str] = None
    AirflowConfigurationOptions: Optional[Mapping[str, str]] = None
    EnvironmentClass: Optional[str] = None
    MaxWorkers: Optional[int] = None
    KmsKey: Optional[str] = None
    AirflowVersion: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationInputTypeDef] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    WebserverAccessMode: Optional[WebserverAccessModeType] = None
    MinWorkers: Optional[int] = None
    Schedulers: Optional[int] = None
    EndpointManagement: Optional[EndpointManagementType] = None
    MinWebservers: Optional[int] = None
    MaxWebservers: Optional[int] = None

class UpdateEnvironmentInputRequestTypeDef(BaseModel):
    Name: str
    ExecutionRoleArn: Optional[str] = None
    AirflowVersion: Optional[str] = None
    SourceBucketArn: Optional[str] = None
    DagS3Path: Optional[str] = None
    PluginsS3Path: Optional[str] = None
    PluginsS3ObjectVersion: Optional[str] = None
    RequirementsS3Path: Optional[str] = None
    RequirementsS3ObjectVersion: Optional[str] = None
    StartupScriptS3Path: Optional[str] = None
    StartupScriptS3ObjectVersion: Optional[str] = None
    AirflowConfigurationOptions: Optional[Mapping[str, str]] = None
    EnvironmentClass: Optional[str] = None
    MaxWorkers: Optional[int] = None
    NetworkConfiguration: Optional[UpdateNetworkConfigurationInputTypeDef] = None
    LoggingConfiguration: Optional[LoggingConfigurationInputTypeDef] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    WebserverAccessMode: Optional[WebserverAccessModeType] = None
    MinWorkers: Optional[int] = None
    Schedulers: Optional[int] = None
    MinWebservers: Optional[int] = None
    MaxWebservers: Optional[int] = None

class EnvironmentTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[EnvironmentStatusType] = None
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    WebserverUrl: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    ServiceRoleArn: Optional[str] = None
    KmsKey: Optional[str] = None
    AirflowVersion: Optional[str] = None
    SourceBucketArn: Optional[str] = None
    DagS3Path: Optional[str] = None
    PluginsS3Path: Optional[str] = None
    PluginsS3ObjectVersion: Optional[str] = None
    RequirementsS3Path: Optional[str] = None
    RequirementsS3ObjectVersion: Optional[str] = None
    StartupScriptS3Path: Optional[str] = None
    StartupScriptS3ObjectVersion: Optional[str] = None
    AirflowConfigurationOptions: Optional[Dict[str, str]] = None
    EnvironmentClass: Optional[str] = None
    MaxWorkers: Optional[int] = None
    NetworkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    LoggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    LastUpdate: Optional[LastUpdateTypeDef] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    WebserverAccessMode: Optional[WebserverAccessModeType] = None
    MinWorkers: Optional[int] = None
    Schedulers: Optional[int] = None
    WebserverVpcEndpointService: Optional[str] = None
    DatabaseVpcEndpointService: Optional[str] = None
    CeleryExecutorQueue: Optional[str] = None
    EndpointManagement: Optional[EndpointManagementType] = None
    MinWebservers: Optional[int] = None
    MaxWebservers: Optional[int] = None

class PublishMetricsInputRequestTypeDef(BaseModel):
    EnvironmentName: str
    MetricData: Sequence[MetricDatumTypeDef]

class GetEnvironmentOutputTypeDef(BaseModel):
    Environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

