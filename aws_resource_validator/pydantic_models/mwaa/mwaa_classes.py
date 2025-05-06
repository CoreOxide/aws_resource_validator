from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mwaa.mwaa_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CreateCliTokenRequest(BaseValidatorModel):
    Name: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateWebLoginTokenRequest(BaseValidatorModel):
    Name: str


class DeleteEnvironmentInput(BaseValidatorModel):
    Name: str


class Dimension(BaseValidatorModel):
    Name: str
    Value: str


class NetworkConfigurationOutput(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class GetEnvironmentInput(BaseValidatorModel):
    Name: str


class InvokeRestApiRequest(BaseValidatorModel):
    Name: str
    Path: str
    Method: RestApiMethodType
    QueryParameters: Optional[Dict[str, Any]] = None
    Body: Optional[Dict[str, Any]] = None


class UpdateError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEnvironmentsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class ModuleLoggingConfigurationInput(BaseValidatorModel):
    Enabled: bool
    LogLevel: LoggingLevelType


class ModuleLoggingConfiguration(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogLevel: Optional[LoggingLevelType] = None
    CloudWatchLogGroupArn: Optional[str] = None


class StatisticSet(BaseValidatorModel):
    SampleCount: Optional[int] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None

Timestamp = Union[datetime, str]


class NetworkConfiguration(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    tagKeys: List[str]


class UpdateNetworkConfigurationInput(BaseValidatorModel):
    SecurityGroupIds: List[str]


class CreateCliTokenResponse(BaseValidatorModel):
    CliToken: str
    WebServerHostname: str
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateWebLoginTokenResponse(BaseValidatorModel):
    WebToken: str
    WebServerHostname: str
    IamIdentity: str
    AirflowIdentity: str
    ResponseMetadata: ResponseMetadata


class InvokeRestApiResponse(BaseValidatorModel):
    RestApiStatusCode: int
    RestApiResponse: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


class ListEnvironmentsOutput(BaseValidatorModel):
    Environments: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateEnvironmentOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class LastUpdate(BaseValidatorModel):
    Status: Optional[UpdateStatusType] = None
    CreatedAt: Optional[datetime] = None
    Error: Optional[UpdateError] = None
    Source: Optional[str] = None


class ListEnvironmentsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class LoggingConfigurationInput(BaseValidatorModel):
    DagProcessingLogs: Optional[ModuleLoggingConfigurationInput] = None
    SchedulerLogs: Optional[ModuleLoggingConfigurationInput] = None
    WebserverLogs: Optional[ModuleLoggingConfigurationInput] = None
    WorkerLogs: Optional[ModuleLoggingConfigurationInput] = None
    TaskLogs: Optional[ModuleLoggingConfigurationInput] = None


class LoggingConfiguration(BaseValidatorModel):
    DagProcessingLogs: Optional[ModuleLoggingConfiguration] = None
    SchedulerLogs: Optional[ModuleLoggingConfiguration] = None
    WebserverLogs: Optional[ModuleLoggingConfiguration] = None
    WorkerLogs: Optional[ModuleLoggingConfiguration] = None
    TaskLogs: Optional[ModuleLoggingConfiguration] = None


class MetricDatum(BaseValidatorModel):
    MetricName: str
    Timestamp: Timestamp
    Dimensions: Optional[List[Dimension]] = None
    Value: Optional[float] = None
    Unit: Optional[UnitType] = None
    StatisticValues: Optional[StatisticSet] = None

NetworkConfigurationUnion = Union[NetworkConfiguration, NetworkConfigurationOutput]


class UpdateEnvironmentInput(BaseValidatorModel):
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
    AirflowConfigurationOptions: Optional[Dict[str, str]] = None
    EnvironmentClass: Optional[str] = None
    MaxWorkers: Optional[int] = None
    NetworkConfiguration: Optional[UpdateNetworkConfigurationInput] = None
    LoggingConfiguration: Optional[LoggingConfigurationInput] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    WebserverAccessMode: Optional[WebserverAccessModeType] = None
    MinWorkers: Optional[int] = None
    Schedulers: Optional[int] = None
    MinWebservers: Optional[int] = None
    MaxWebservers: Optional[int] = None


class Environment(BaseValidatorModel):
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
    NetworkConfiguration: Optional[NetworkConfigurationOutput] = None
    LoggingConfiguration: Optional[LoggingConfiguration] = None
    LastUpdate: Optional[LastUpdate] = None
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


class PublishMetricsInput(BaseValidatorModel):
    EnvironmentName: str
    MetricData: List[MetricDatum]


class CreateEnvironmentInput(BaseValidatorModel):
    Name: str
    ExecutionRoleArn: str
    SourceBucketArn: str
    DagS3Path: str
    NetworkConfiguration: NetworkConfigurationUnion
    PluginsS3Path: Optional[str] = None
    PluginsS3ObjectVersion: Optional[str] = None
    RequirementsS3Path: Optional[str] = None
    RequirementsS3ObjectVersion: Optional[str] = None
    StartupScriptS3Path: Optional[str] = None
    StartupScriptS3ObjectVersion: Optional[str] = None
    AirflowConfigurationOptions: Optional[Dict[str, str]] = None
    EnvironmentClass: Optional[str] = None
    MaxWorkers: Optional[int] = None
    KmsKey: Optional[str] = None
    AirflowVersion: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationInput] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    WebserverAccessMode: Optional[WebserverAccessModeType] = None
    MinWorkers: Optional[int] = None
    Schedulers: Optional[int] = None
    EndpointManagement: Optional[EndpointManagementType] = None
    MinWebservers: Optional[int] = None
    MaxWebservers: Optional[int] = None


class GetEnvironmentOutput(BaseValidatorModel):
    Environment: Environment
    ResponseMetadata: ResponseMetadata