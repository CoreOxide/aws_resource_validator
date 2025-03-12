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
from aws_resource_validator.pydantic_models.mwaa_constants import *

class CreateCliTokenRequestTypeDef(BaseValidatorModel):
    Name: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateWebLoginTokenRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteEnvironmentInputTypeDef(BaseValidatorModel):
    Name: str


class DimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class NetworkConfigurationOutputTypeDef(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class GetEnvironmentInputTypeDef(BaseValidatorModel):
    Name: str


class InvokeRestApiRequestTypeDef(BaseValidatorModel):
    Name: str
    Path: str
    Method: RestApiMethodType
    QueryParameters: Optional[Mapping[str, Any]] = None
    Body: Optional[Mapping[str, Any]] = None


class UpdateErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEnvironmentsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class ModuleLoggingConfigurationInputTypeDef(BaseValidatorModel):
    Enabled: bool
    LogLevel: LoggingLevelType


class ModuleLoggingConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogLevel: Optional[LoggingLevelType] = None
    CloudWatchLogGroupArn: Optional[str] = None


class StatisticSetTypeDef(BaseValidatorModel):
    SampleCount: Optional[int] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None


class NetworkConfigurationTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    tagKeys: Sequence[str]


class UpdateNetworkConfigurationInputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]


class CreateCliTokenResponseTypeDef(BaseValidatorModel):
    CliToken: str
    WebServerHostname: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEnvironmentOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWebLoginTokenResponseTypeDef(BaseValidatorModel):
    WebToken: str
    WebServerHostname: str
    IamIdentity: str
    AirflowIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeRestApiResponseTypeDef(BaseValidatorModel):
    RestApiStatusCode: int
    RestApiResponse: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef


class ListEnvironmentsOutputTypeDef(BaseValidatorModel):
    Environments: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEnvironmentOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class LastUpdateTypeDef(BaseValidatorModel):
    Status: Optional[UpdateStatusType] = None
    CreatedAt: Optional[datetime] = None
    Error: Optional[UpdateErrorTypeDef] = None
    Source: Optional[str] = None


class ListEnvironmentsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LoggingConfigurationInputTypeDef(BaseValidatorModel):
    DagProcessingLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    SchedulerLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    WebserverLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    WorkerLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None
    TaskLogs: Optional[ModuleLoggingConfigurationInputTypeDef] = None


class LoggingConfigurationTypeDef(BaseValidatorModel):
    DagProcessingLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    SchedulerLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    WebserverLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    WorkerLogs: Optional[ModuleLoggingConfigurationTypeDef] = None
    TaskLogs: Optional[ModuleLoggingConfigurationTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class MetricDatumTypeDef(BaseValidatorModel):
    MetricName: str
    Timestamp: TimestampTypeDef
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Value: Optional[float] = None
    Unit: Optional[UnitType] = None
    StatisticValues: Optional[StatisticSetTypeDef] = None


class UpdateEnvironmentInputTypeDef(BaseValidatorModel):
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


class EnvironmentTypeDef(BaseValidatorModel):
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


class PublishMetricsInputTypeDef(BaseValidatorModel):
    EnvironmentName: str
    MetricData: Sequence[MetricDatumTypeDef]


class NetworkConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateEnvironmentInputTypeDef(BaseValidatorModel):
    Name: str
    ExecutionRoleArn: str
    SourceBucketArn: str
    DagS3Path: str
    NetworkConfiguration: NetworkConfigurationUnionTypeDef
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


class GetEnvironmentOutputTypeDef(BaseValidatorModel):
    Environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


