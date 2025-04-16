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
from aws_resource_validator.pydantic_models.emr_serverless_constants import *

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
    logTypes: Optional[Mapping[str, Sequence[str]]] = None


class Configuration(BaseValidatorModel):
    classification: str
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Mapping[str, Any]]] = None


class ImageConfigurationInput(BaseValidatorModel):
    imageUri: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    applicationId: str


class GetApplicationRequest(BaseValidatorModel):
    applicationId: str


class GetDashboardForJobRunRequest(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None
    accessSystemProfileLogs: Optional[bool] = None


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
    entryPointArguments: Optional[Sequence[str]] = None
    sparkSubmitParameters: Optional[str] = None


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


class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[Sequence[ApplicationStateType]] = None


class ListJobRunAttemptsRequest(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


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
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None


class StartApplicationRequest(BaseValidatorModel):
    applicationId: str


class StopApplicationRequest(BaseValidatorModel):
    applicationId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WorkerTypeSpecification(BaseValidatorModel):
    imageConfiguration: Optional[ImageConfiguration] = None


class CancelJobRunResponse(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    ResponseMetadata: ResponseMetadata


class CreateApplicationResponse(BaseValidatorModel):
    applicationId: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class GetDashboardForJobRunResponse(BaseValidatorModel):
    url: str
    ResponseMetadata: ResponseMetadata


class ApplicationSummary(BaseValidatorModel):
    pass


class ListApplicationsResponse(BaseValidatorModel):
    applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartJobRunResponse(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    arn: str
    ResponseMetadata: ResponseMetadata


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


class JobRunAttemptSummary(BaseValidatorModel):
    pass


class ListJobRunAttemptsResponse(BaseValidatorModel):
    jobRunAttempts: List[JobRunAttemptSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobRunSummary(BaseValidatorModel):
    pass


class ListJobRunsResponse(BaseValidatorModel):
    jobRuns: List[JobRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    states: Optional[Sequence[ApplicationStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunAttemptsRequestPaginate(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class ListJobRunsRequestPaginate(BaseValidatorModel):
    applicationId: str
    createdAtAfter: Optional[Timestamp] = None
    createdAtBefore: Optional[Timestamp] = None
    states: Optional[Sequence[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunsRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    createdAtAfter: Optional[Timestamp] = None
    createdAtBefore: Optional[Timestamp] = None
    states: Optional[Sequence[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None


class MonitoringConfigurationOutput(BaseValidatorModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfiguration] = None
    managedPersistenceMonitoringConfiguration: Optional[ ManagedPersistenceMonitoringConfiguration ] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfigurationOutput] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfiguration] = None


class MonitoringConfiguration(BaseValidatorModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfiguration] = None
    managedPersistenceMonitoringConfiguration: Optional[ ManagedPersistenceMonitoringConfiguration ] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfiguration] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfiguration] = None


class ConfigurationOverridesOutput(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationOutput] = None


class ConfigurationOverrides(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence[Configuration]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class Application(BaseValidatorModel):
    pass


class GetApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


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


class ConfigurationUnion(BaseValidatorModel):
    pass


class MonitoringConfigurationUnion(BaseValidatorModel):
    pass


class NetworkConfigurationUnion(BaseValidatorModel):
    pass


class UpdateApplicationRequest(BaseValidatorModel):
    applicationId: str
    clientToken: str
    initialCapacity: Optional[Mapping[str, InitialCapacityConfig]] = None
    maximumCapacity: Optional[MaximumAllowedResources] = None
    autoStartConfiguration: Optional[AutoStartConfig] = None
    autoStopConfiguration: Optional[AutoStopConfig] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfigurationInput] = None
    workerTypeSpecifications: Optional[Mapping[str, WorkerTypeSpecificationInput]] = None
    interactiveConfiguration: Optional[InteractiveConfiguration] = None
    releaseLabel: Optional[str] = None
    runtimeConfiguration: Optional[Sequence[ConfigurationUnion]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationUnion] = None
    schedulerConfiguration: Optional[SchedulerConfiguration] = None


class GetJobRunResponse(BaseValidatorModel):
    jobRun: JobRun
    ResponseMetadata: ResponseMetadata


class JobDriverUnion(BaseValidatorModel):
    pass


class ConfigurationOverridesUnion(BaseValidatorModel):
    pass


class StartJobRunRequest(BaseValidatorModel):
    applicationId: str
    clientToken: str
    executionRoleArn: str
    jobDriver: Optional[JobDriverUnion] = None
    configurationOverrides: Optional[ConfigurationOverridesUnion] = None
    tags: Optional[Mapping[str, str]] = None
    executionTimeoutMinutes: Optional[int] = None
    name: Optional[str] = None
    mode: Optional[JobRunModeType] = None
    retryPolicy: Optional[RetryPolicy] = None


