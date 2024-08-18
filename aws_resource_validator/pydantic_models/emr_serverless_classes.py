from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ApplicationSummaryTypeDef(BaseValidatorModel):
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

class AutoStartConfigTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None

class AutoStopConfigTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    idleTimeoutMinutes: Optional[int] = None

class ImageConfigurationTypeDef(BaseValidatorModel):
    imageUri: str
    resolvedImageDigest: Optional[str] = None

class InteractiveConfigurationTypeDef(BaseValidatorModel):
    studioEnabled: Optional[bool] = None
    livyEndpointEnabled: Optional[bool] = None

class MaximumAllowedResourcesTypeDef(BaseValidatorModel):
    cpu: str
    memory: str
    disk: Optional[str] = None

class NetworkConfigurationOutputTypeDef(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None

class CancelJobRunRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CloudWatchLoggingConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: bool
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    encryptionKeyArn: Optional[str] = None
    logTypes: Optional[Dict[str, List[str]]] = None

class CloudWatchLoggingConfigurationTypeDef(BaseValidatorModel):
    enabled: bool
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    encryptionKeyArn: Optional[str] = None
    logTypes: Optional[Mapping[str, Sequence[str]]] = None

class ConfigurationOutputTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None

class ConfigurationTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Dict[str, Any]]] = None

class ImageConfigurationInputTypeDef(BaseValidatorModel):
    imageUri: Optional[str] = None

class NetworkConfigurationTypeDef(BaseValidatorModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class GetDashboardForJobRunRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None

class GetJobRunRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    attempt: Optional[int] = None

class HiveTypeDef(BaseValidatorModel):
    query: str
    initQueryFile: Optional[str] = None
    parameters: Optional[str] = None

class WorkerResourceConfigTypeDef(BaseValidatorModel):
    cpu: str
    memory: str
    disk: Optional[str] = None
    diskType: Optional[str] = None

class SparkSubmitOutputTypeDef(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None

class SparkSubmitTypeDef(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[Sequence[str]] = None
    sparkSubmitParameters: Optional[str] = None

class JobRunAttemptSummaryTypeDef(BaseValidatorModel):
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

class JobRunSummaryTypeDef(BaseValidatorModel):
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

class ResourceUtilizationTypeDef(BaseValidatorModel):
    vCPUHour: Optional[float] = None
    memoryGBHour: Optional[float] = None
    storageGBHour: Optional[float] = None

class RetryPolicyTypeDef(BaseValidatorModel):
    maxAttempts: Optional[int] = None
    maxFailedAttemptsPerHour: Optional[int] = None

class TotalResourceUtilizationTypeDef(BaseValidatorModel):
    vCPUHour: Optional[float] = None
    memoryGBHour: Optional[float] = None
    storageGBHour: Optional[float] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[Sequence[ApplicationStateType]] = None

class ListJobRunAttemptsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ManagedPersistenceMonitoringConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    encryptionKeyArn: Optional[str] = None

class PrometheusMonitoringConfigurationTypeDef(BaseValidatorModel):
    remoteWriteUrl: Optional[str] = None

class S3MonitoringConfigurationTypeDef(BaseValidatorModel):
    logUri: Optional[str] = None
    encryptionKeyArn: Optional[str] = None

class StartApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class StopApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkerTypeSpecificationTypeDef(BaseValidatorModel):
    imageConfiguration: Optional[ImageConfigurationTypeDef] = None

class CancelJobRunResponseTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    applicationId: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardForJobRunResponseTypeDef(BaseValidatorModel):
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    applications: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkerTypeSpecificationInputTypeDef(BaseValidatorModel):
    imageConfiguration: Optional[ImageConfigurationInputTypeDef] = None

class InitialCapacityConfigTypeDef(BaseValidatorModel):
    workerCount: int
    workerConfiguration: Optional[WorkerResourceConfigTypeDef] = None

class JobDriverOutputTypeDef(BaseValidatorModel):
    sparkSubmit: Optional[SparkSubmitOutputTypeDef] = None
    hive: Optional[HiveTypeDef] = None

class JobDriverTypeDef(BaseValidatorModel):
    sparkSubmit: Optional[SparkSubmitTypeDef] = None
    hive: Optional[HiveTypeDef] = None

class ListJobRunAttemptsResponseTypeDef(BaseValidatorModel):
    jobRunAttempts: List[JobRunAttemptSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(BaseValidatorModel):
    jobRuns: List[JobRunSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    states: Optional[Sequence[ApplicationStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunAttemptsRequestListJobRunAttemptsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    jobRunId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestListJobRunsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    createdAtAfter: Optional[TimestampTypeDef] = None
    createdAtBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    createdAtAfter: Optional[TimestampTypeDef] = None
    createdAtBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[JobRunStateType]] = None
    mode: Optional[JobRunModeType] = None

class MonitoringConfigurationOutputTypeDef(BaseValidatorModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    managedPersistenceMonitoringConfiguration: Optional[       ManagedPersistenceMonitoringConfigurationTypeDef     ] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfigurationOutputTypeDef] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfigurationTypeDef] = None

class MonitoringConfigurationTypeDef(BaseValidatorModel):
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    managedPersistenceMonitoringConfiguration: Optional[       ManagedPersistenceMonitoringConfigurationTypeDef     ] = None
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfigurationTypeDef] = None
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfigurationTypeDef] = None

class ApplicationTypeDef(BaseValidatorModel):
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

class ConfigurationOverridesOutputTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List["ConfigurationOutputTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationOutputTypeDef] = None

class ConfigurationOverridesTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence["ConfigurationTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
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

class GetApplicationResponseTypeDef(BaseValidatorModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseValidatorModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobRunTypeDef(BaseValidatorModel):
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

class StartJobRunRequestRequestTypeDef(BaseValidatorModel):
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

class GetJobRunResponseTypeDef(BaseValidatorModel):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

