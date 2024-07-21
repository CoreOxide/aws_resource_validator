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
from aws_resource_validator.pydantic_models.emr_serverless_constants import *

class ApplicationSummaryTypeDef(BaseModel):
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

class AutoStartConfigTypeDef(BaseModel):
    enabled: Optional[bool] = None

class AutoStopConfigTypeDef(BaseModel):
    enabled: Optional[bool] = None
    idleTimeoutMinutes: Optional[int] = None

class ImageConfigurationTypeDef(BaseModel):
    imageUri: str
    resolvedImageDigest: Optional[str] = None

class InteractiveConfigurationTypeDef(BaseModel):
    studioEnabled: Optional[bool] = None
    livyEndpointEnabled: Optional[bool] = None

class MaximumAllowedResourcesTypeDef(BaseModel):
    cpu: str
    memory: str
    disk: Optional[str] = None

class NetworkConfigurationOutputTypeDef(BaseModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None

class CancelJobRunRequestRequestTypeDef(BaseModel):
    applicationId: str
    jobRunId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CloudWatchLoggingConfigurationOutputTypeDef(BaseModel):
    enabled: bool
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    encryptionKeyArn: Optional[str] = None
    logTypes: Optional[Dict[str, List[str]]] = None

class CloudWatchLoggingConfigurationTypeDef(BaseModel):
    enabled: bool
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    encryptionKeyArn: Optional[str] = None
    logTypes: Optional[Mapping[str, Sequence[str]]] = None

class ConfigurationOutputTypeDef(BaseModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None

class ConfigurationTypeDef(BaseModel):
    classification: str
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Dict[str, Any]]] = None

class ImageConfigurationInputTypeDef(BaseModel):
    imageUri: Optional[str] = None

class NetworkConfigurationTypeDef(BaseModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class GetApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class GetDashboardForJobRunRequestRequestTypeDef(BaseModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None

class GetJobRunRequestRequestTypeDef(BaseModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None

class HiveTypeDef(BaseModel):
    query: str
    initQueryFile: Optional[str] = None
    parameters: Optional[str] = None

class WorkerResourceConfigTypeDef(BaseModel):
    cpu: str
    memory: str
    disk: Optional[str] = None
    diskType: Optional[str] = None

class SparkSubmitOutputTypeDef(BaseModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None

class SparkSubmitTypeDef(BaseModel):
    entryPoint: str
    entryPointArguments: Optional[Sequence[str]] = None
    sparkSubmitParameters: Optional[str] = None

class JobRunAttemptSummaryTypeDef(BaseModel):
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

class JobRunSummaryTypeDef(BaseModel):
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

class ResourceUtilizationTypeDef(BaseModel):
    vCPUHour: Optional[float] = None
    memoryGBHour: Optional[float] = None
    storageGBHour: Optional[float] = None

class RetryPolicyTypeDef(BaseModel):
    maxAttempts: Optional[int] = None
    maxFailedAttemptsPerHour: Optional[int] = None

class TotalResourceUtilizationTypeDef(BaseModel):
    vCPUHour: Optional[float] = None
    memoryGBHour: Optional[float] = None
    storageGBHour: Optional[float] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[Sequence[ApplicationStateType]] = None

class ListJobRunAttemptsRequestRequestTypeDef(BaseModel):
    applicationId: str
    jobRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ManagedPersistenceMonitoringConfigurationTypeDef(BaseModel):
    enabled: Optional[bool] = None
    encryptionKeyArn: Optional[str] = None

class PrometheusMonitoringConfigurationTypeDef(BaseModel):
    remoteWriteUrl: Optional[str] = None

class S3MonitoringConfigurationTypeDef(BaseModel):
    logUri: Optional[str] = None
    encryptionKeyArn: Optional[str] = None

class StartApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class StopApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkerTypeSpecificationTypeDef(BaseModel):
    imageConfiguration: Optional[ImageConfigurationTypeDef] = None

class CancelJobRunResponseTypeDef(BaseModel):
    applicationId: str
    jobRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseModel):
    applicationId: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardForJobRunResponseTypeDef(BaseModel):
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    applications: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(BaseModel):
    applicationId: str
    jobRunId: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkerTypeSpecificationInputTypeDef(BaseModel):
    imageConfiguration: Optional[ImageConfigurationInputTypeDef] = None

class InitialCapacityConfigTypeDef(BaseModel):
    workerCount: int
    workerConfiguration: Optional[WorkerResourceConfigTypeDef] = None

class JobDriverOutputTypeDef(BaseModel):
    sparkSubmit: Optional[SparkSubmitOutputTypeDef] = None
    hive: Optional[HiveTypeDef] = None

class JobDriverTypeDef(BaseModel):
    sparkSubmit: Optional[SparkSubmitTypeDef] = None
    hive: Optional[HiveTypeDef] = None

class ListJobRunAttemptsResponseTypeDef(BaseModel):
    jobRunAttempts: List[JobRunAttemptSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(BaseModel):
    jobRuns: List[JobRunSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    states: Optional[Sequence[ApplicationStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunAttemptsRequestListJobRunAttemptsPaginateTypeDef(BaseModel):
    applicationId: str
    jobRunId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestListJobRunsPaginateTypeDef(BaseModel):
    applicationId: str
    createdAtAfter: Optional[TimestampTypeDef] = None
    createdAtBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestRequestTypeDef(BaseModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    createdAtAfter: Optional[TimestampTypeDef] = None
    createdAtBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None

class MonitoringConfigurationOutputTypeDef(BaseModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    managedPersistenceMonitoringConfiguration: Optional[       ManagedPersistenceMonitoringConfigurationTypeDef     ] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfigurationOutputTypeDef] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfigurationTypeDef] = None

class MonitoringConfigurationTypeDef(BaseModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    managedPersistenceMonitoringConfiguration: Optional[       ManagedPersistenceMonitoringConfigurationTypeDef     ] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfigurationTypeDef] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfigurationTypeDef] = None

class ApplicationTypeDef(BaseModel):
    applicationId: str
    arn: str
    releaseLabel: str
    type: str
    state: ApplicationStateType
    createdAt: datetime
    updatedAt: datetime
    name: Optional[str] = None
    stateDetails: Optional[str] = None
    initialCapacity: Optional[Dict[str, InitialCapacityConfigTypeDef]] = None
    maximumCapacity: Optional[MaximumAllowedResourcesTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    autoStartConfiguration: Optional[AutoStartConfigTypeDef] = None
    autoStopConfiguration: Optional[AutoStopConfigTypeDef] = None
    networkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfigurationTypeDef] = None
    workerTypeSpecifications: Optional[Dict[str, WorkerTypeSpecificationTypeDef]] = None
    runtimeConfiguration: Optional[List["ConfigurationOutputTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationOutputTypeDef] = None
    interactiveConfiguration: Optional[InteractiveConfigurationTypeDef] = None

class ConfigurationOverridesOutputTypeDef(BaseModel):
    applicationConfiguration: Optional[List["ConfigurationOutputTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationOutputTypeDef] = None

class ConfigurationOverridesTypeDef(BaseModel):
    applicationConfiguration: Optional[Sequence["ConfigurationTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    releaseLabel: str
    type: str
    clientToken: str
    name: Optional[str] = None
    initialCapacity: Optional[Mapping[str, InitialCapacityConfigTypeDef]] = None
    maximumCapacity: Optional[MaximumAllowedResourcesTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    autoStartConfiguration: Optional[AutoStartConfigTypeDef] = None
    autoStopConfiguration: Optional[AutoStopConfigTypeDef] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfigurationInputTypeDef] = None
    workerTypeSpecifications: Optional[Mapping[str, WorkerTypeSpecificationInputTypeDef]] = None
    runtimeConfiguration: Optional[Sequence[ConfigurationUnionTypeDef]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None
    interactiveConfiguration: Optional[InteractiveConfigurationTypeDef] = None

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str
    clientToken: str
    initialCapacity: Optional[Mapping[str, InitialCapacityConfigTypeDef]] = None
    maximumCapacity: Optional[MaximumAllowedResourcesTypeDef] = None
    autoStartConfiguration: Optional[AutoStartConfigTypeDef] = None
    autoStopConfiguration: Optional[AutoStopConfigTypeDef] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    architecture: Optional[ArchitectureType] = None
    imageConfiguration: Optional[ImageConfigurationInputTypeDef] = None
    workerTypeSpecifications: Optional[Mapping[str, WorkerTypeSpecificationInputTypeDef]] = None
    interactiveConfiguration: Optional[InteractiveConfigurationTypeDef] = None
    releaseLabel: Optional[str] = None
    runtimeConfiguration: Optional[Sequence[ConfigurationUnionTypeDef]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class GetApplicationResponseTypeDef(BaseModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobRunTypeDef(BaseModel):
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
    jobDriver: JobDriverOutputTypeDef
    name: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    totalResourceUtilization: Optional[TotalResourceUtilizationTypeDef] = None
    networkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    totalExecutionDurationSeconds: Optional[int] = None
    executionTimeoutMinutes: Optional[int] = None
    billedResourceUtilization: Optional[ResourceUtilizationTypeDef] = None
    mode: Optional[JobRunModeType] = None
    retryPolicy: Optional[RetryPolicyTypeDef] = None
    attempt: Optional[int] = None
    attemptCreatedAt: Optional[datetime] = None
    attemptUpdatedAt: Optional[datetime] = None

class StartJobRunRequestRequestTypeDef(BaseModel):
    applicationId: str
    clientToken: str
    executionRoleArn: str
    jobDriver: Optional[JobDriverTypeDef] = None
    configurationOverrides: Optional[ConfigurationOverridesTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    executionTimeoutMinutes: Optional[int] = None
    name: Optional[str] = None
    mode: Optional[JobRunModeType] = None
    retryPolicy: Optional[RetryPolicyTypeDef] = None

class GetJobRunResponseTypeDef(BaseModel):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

