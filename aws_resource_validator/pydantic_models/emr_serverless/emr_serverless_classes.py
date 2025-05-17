from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplicationSummary(BaseValidatorModel):
    id: str
    arn: str
    releaseLabel: str
    type: str
    state: ApplicationStateType
    createdAt: datetime
    updatedAt: datetime
    name: Optional[str] = None
    stateDetails: Optional[str] = None
    architecture: Optional[ArchitectureType] = None


class AutoStartConfig(BaseValidatorModel):
    enabled: Optional[bool] = None


class AutoStopConfig(BaseValidatorModel):
    enabled: Optional[bool] = None
    idleTimeoutMinutes: Optional[int] = None


class ConfigurationOutput(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class ImageConfiguration(BaseValidatorModel):
    imageUri: str
    resolvedImageDigest: Optional[str] = None


class InteractiveConfiguration(BaseValidatorModel):
    studioEnabled: Optional[bool] = None
    livyEndpointEnabled: Optional[bool] = None


class MaximumAllowedResources(BaseValidatorModel):
    cpu: str
    memory: str
    disk: Optional[str] = None


class NetworkConfigurationOutput(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class SchedulerConfiguration(BaseValidatorModel):
    queueTimeoutMinutes: Optional[int] = None
    maxConcurrentRuns: Optional[int] = None


# This class is the input for the 'cancel_job_run' function.
class CancelJobRunRequest(BaseValidatorModel):
    applicationId: str
    jobRunId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CloudWatchLoggingConfigurationOutput(BaseValidatorModel):
    enabled: bool
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    encryptionKeyArn: Optional[str] = None
    logTypes: Optional[Dict[str, List[str]]] = None


class CloudWatchLoggingConfiguration(BaseValidatorModel):
    enabled: bool
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    encryptionKeyArn: Optional[str] = None
    logTypes: Optional[Dict[str, List[str]]] = None


class Configuration(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class ImageConfigurationInput(BaseValidatorModel):
    imageUri: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    applicationId: str


# This class is the input for the 'get_application' function.
class GetApplicationRequest(BaseValidatorModel):
    applicationId: str


# This class is the input for the 'get_dashboard_for_job_run' function.
class GetDashboardForJobRunRequest(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None
    accessSystemProfileLogs: Optional[bool] = None


# This class is the input for the 'get_job_run' function.
class GetJobRunRequest(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None


class Hive(BaseValidatorModel):
    query: str
    initQueryFile: Optional[str] = None
    parameters: Optional[str] = None


class WorkerResourceConfig(BaseValidatorModel):
    cpu: str
    memory: str
    disk: Optional[str] = None
    diskType: Optional[str] = None


class SparkSubmitOutput(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None


class SparkSubmit(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None


class JobRunAttemptSummary(BaseValidatorModel):
    applicationId: str
    id: str
    arn: str
    createdBy: str
    jobCreatedAt: datetime
    createdAt: datetime
    updatedAt: datetime
    executionRole: str
    state: JobRunStateType
    stateDetails: str
    releaseLabel: str
    name: Optional[str] = None
    mode: Optional[JobRunModeType] = None
    type: Optional[str] = None
    attempt: Optional[int] = None


class JobRunSummary(BaseValidatorModel):
    applicationId: str
    id: str
    arn: str
    createdBy: str
    createdAt: datetime
    updatedAt: datetime
    executionRole: str
    state: JobRunStateType
    stateDetails: str
    releaseLabel: str
    name: Optional[str] = None
    mode: Optional[JobRunModeType] = None
    type: Optional[str] = None
    attempt: Optional[int] = None
    attemptCreatedAt: Optional[datetime] = None
    attemptUpdatedAt: Optional[datetime] = None


class ResourceUtilization(BaseValidatorModel):
    vCPUHour: Optional[float] = None
    memoryGBHour: Optional[float] = None
    storageGBHour: Optional[float] = None


class RetryPolicy(BaseValidatorModel):
    maxAttempts: Optional[int] = None
    maxFailedAttemptsPerHour: Optional[int] = None


class TotalResourceUtilization(BaseValidatorModel):
    vCPUHour: Optional[float] = None
    memoryGBHour: Optional[float] = None
    storageGBHour: Optional[float] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[List[ApplicationStateType]] = None


# This class is the input for the 'list_job_run_attempts' function.
class ListJobRunAttemptsRequest(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ManagedPersistenceMonitoringConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None
    encryptionKeyArn: Optional[str] = None


class PrometheusMonitoringConfiguration(BaseValidatorModel):
    remoteWriteUrl: Optional[str] = None


class S3MonitoringConfiguration(BaseValidatorModel):
    logUri: Optional[str] = None
    encryptionKeyArn: Optional[str] = None


class NetworkConfiguration(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class StartApplicationRequest(BaseValidatorModel):
    applicationId: str


class StopApplicationRequest(BaseValidatorModel):
    applicationId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class WorkerTypeSpecification(BaseValidatorModel):
    imageConfiguration: Optional[ImageConfiguration] = None


# This class is the output for the 'cancel_job_run' function.
class CancelJobRunResponse(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    applicationId: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_dashboard_for_job_run' function.
class GetDashboardForJobRunResponse(BaseValidatorModel):
    url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_job_run' function.
class StartJobRunResponse(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    arn: str
    ResponseMetadata: ResponseMetadata

ConfigurationUnion = Union[Configuration, ConfigurationOutput]


class WorkerTypeSpecificationInput(BaseValidatorModel):
    imageConfiguration: Optional[ImageConfigurationInput] = None


class InitialCapacityConfig(BaseValidatorModel):
    workerCount: int
    workerConfiguration: Optional[WorkerResourceConfig] = None


class JobDriverOutput(BaseValidatorModel):
    sparkSubmit: Optional[SparkSubmitOutput] = None
    hive: Optional[Hive] = None


class JobDriver(BaseValidatorModel):
    sparkSubmit: Optional[SparkSubmit] = None
    hive: Optional[Hive] = None


# This class is the output for the 'list_job_run_attempts' function.
class ListJobRunAttemptsResponse(BaseValidatorModel):
    jobRunAttempts: List[JobRunAttemptSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_job_runs' function.
class ListJobRunsResponse(BaseValidatorModel):
    jobRuns: List[JobRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    states: Optional[List[ApplicationStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunAttemptsRequestPaginate(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunsRequestPaginate(BaseValidatorModel):
    applicationId: str
    createdAtAfter: Optional[Timestamp] = None
    createdAtBefore: Optional[Timestamp] = None
    states: Optional[List[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_job_runs' function.
class ListJobRunsRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    createdAtAfter: Optional[Timestamp] = None
    createdAtBefore: Optional[Timestamp] = None
    states: Optional[List[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None


class MonitoringConfigurationOutput(BaseValidatorModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfiguration] = None
    managedPersistenceMonitoringConfiguration: Optional[ManagedPersistenceMonitoringConfiguration] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfigurationOutput] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfiguration] = None


class MonitoringConfiguration(BaseValidatorModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfiguration] = None
    managedPersistenceMonitoringConfiguration: Optional[ManagedPersistenceMonitoringConfiguration] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfiguration] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfiguration] = None

NetworkConfigurationUnion = Union[NetworkConfiguration, NetworkConfigurationOutput]

JobDriverUnion = Union[JobDriver, JobDriverOutput]


class Application(BaseValidatorModel):
    applicationId: str
    arn: str
    releaseLabel: str
    type: str
    state: ApplicationStateType
    createdAt: datetime
    updatedAt: datetime
    name: Optional[str] = None
    stateDetails: Optional[str] = None
    initialCapacity: Optional[Dict[str, InitialCapacityConfig]] = None
    maximumCapacity: Optional[MaximumAllowedResources] = None
    tags: Optional[Dict[str, str]] = None
    autoStartConfiguration: Optional[AutoStartConfig] = None
    autoStopConfiguration: Optional[AutoStopConfig] = None
    networkConfiguration: Optional[NetworkConfigurationOutput] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfiguration] = None
    workerTypeSpecifications: Optional[Dict[str, WorkerTypeSpecification]] = None
    runtimeConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationOutput] = None
    interactiveConfiguration: Optional[InteractiveConfiguration] = None
    schedulerConfiguration: Optional[SchedulerConfiguration] = None


class ConfigurationOverridesOutput(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationOutput] = None


class ConfigurationOverrides(BaseValidatorModel):
    applicationConfiguration: Optional[List[Configuration]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None

MonitoringConfigurationUnion = Union[MonitoringConfiguration, MonitoringConfigurationOutput]


# This class is the output for the 'get_application' function.
class GetApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_application' function.
class UpdateApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


class JobRun(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    arn: str
    createdBy: str
    createdAt: datetime
    updatedAt: datetime
    executionRole: str
    state: JobRunStateType
    stateDetails: str
    releaseLabel: str
    jobDriver: JobDriverOutput
    name: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesOutput] = None
    tags: Optional[Dict[str, str]] = None
    totalResourceUtilization: Optional[TotalResourceUtilization] = None
    networkConfiguration: Optional[NetworkConfigurationOutput] = None
    totalExecutionDurationSeconds: Optional[int] = None
    executionTimeoutMinutes: Optional[int] = None
    billedResourceUtilization: Optional[ResourceUtilization] = None
    mode: Optional[JobRunModeType] = None
    retryPolicy: Optional[RetryPolicy] = None
    attempt: Optional[int] = None
    attemptCreatedAt: Optional[datetime] = None
    attemptUpdatedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    queuedDurationMilliseconds: Optional[int] = None

ConfigurationOverridesUnion = Union[ConfigurationOverrides, ConfigurationOverridesOutput]


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    releaseLabel: str
    type: str
    clientToken: str
    name: Optional[str] = None
    initialCapacity: Optional[Dict[str, InitialCapacityConfig]] = None
    maximumCapacity: Optional[MaximumAllowedResources] = None
    tags: Optional[Dict[str, str]] = None
    autoStartConfiguration: Optional[AutoStartConfig] = None
    autoStopConfiguration: Optional[AutoStopConfig] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfigurationInput] = None
    workerTypeSpecifications: Optional[Dict[str, WorkerTypeSpecificationInput]] = None
    runtimeConfiguration: Optional[List[ConfigurationUnion]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationUnion] = None
    interactiveConfiguration: Optional[InteractiveConfiguration] = None
    schedulerConfiguration: Optional[SchedulerConfiguration] = None


# This class is the input for the 'update_application' function.
class UpdateApplicationRequest(BaseValidatorModel):
    applicationId: str
    clientToken: str
    initialCapacity: Optional[Dict[str, InitialCapacityConfig]] = None
    maximumCapacity: Optional[MaximumAllowedResources] = None
    autoStartConfiguration: Optional[AutoStartConfig] = None
    autoStopConfiguration: Optional[AutoStopConfig] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfigurationInput] = None
    workerTypeSpecifications: Optional[Dict[str, WorkerTypeSpecificationInput]] = None
    interactiveConfiguration: Optional[InteractiveConfiguration] = None
    releaseLabel: Optional[str] = None
    runtimeConfiguration: Optional[List[ConfigurationUnion]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationUnion] = None
    schedulerConfiguration: Optional[SchedulerConfiguration] = None


# This class is the output for the 'get_job_run' function.
class GetJobRunResponse(BaseValidatorModel):
    jobRun: JobRun
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_job_run' function.
class StartJobRunRequest(BaseValidatorModel):
    applicationId: str
    clientToken: str
    executionRoleArn: str
    jobDriver: Optional[JobDriverUnion] = None
    configurationOverrides: Optional[ConfigurationOverridesUnion] = None
    tags: Optional[Dict[str, str]] = None
    executionTimeoutMinutes: Optional[int] = None
    name: Optional[str] = None
    mode: Optional[JobRunModeType] = None
    retryPolicy: Optional[RetryPolicy] = None