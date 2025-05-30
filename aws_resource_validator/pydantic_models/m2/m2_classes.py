from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.m2.m2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AlternateKey(BaseValidatorModel):
    length: int
    offset: int
    allowDuplicates: Optional[bool] = None
    name: Optional[str] = None


class ApplicationSummary(BaseValidatorModel):
    applicationArn: str
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    engineType: EngineTypeType
    name: str
    status: ApplicationLifecycleType
    deploymentStatus: Optional[ApplicationDeploymentLifecycleType] = None
    description: Optional[str] = None
    environmentId: Optional[str] = None
    lastStartTime: Optional[datetime] = None
    roleArn: Optional[str] = None
    versionStatus: Optional[ApplicationVersionLifecycleType] = None


class ApplicationVersionSummary(BaseValidatorModel):
    applicationVersion: int
    creationTime: datetime
    status: ApplicationVersionLifecycleType
    statusReason: Optional[str] = None


class FileBatchJobDefinition(BaseValidatorModel):
    fileName: str
    folderPath: Optional[str] = None


class ScriptBatchJobDefinition(BaseValidatorModel):
    scriptName: str


class FileBatchJobIdentifier(BaseValidatorModel):
    fileName: str
    folderPath: Optional[str] = None


class ScriptBatchJobIdentifier(BaseValidatorModel):
    scriptName: str


class CancelBatchJobExecutionRequest(BaseValidatorModel):
    applicationId: str
    executionId: str
    authSecretsManagerArn: Optional[str] = None


class Definition(BaseValidatorModel):
    content: Optional[str] = None
    s3Location: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_deployment' function.
class CreateDeploymentRequest(BaseValidatorModel):
    applicationId: str
    applicationVersion: int
    environmentId: str
    clientToken: Optional[str] = None


class HighAvailabilityConfig(BaseValidatorModel):
    desiredCapacity: int


class ExternalLocation(BaseValidatorModel):
    s3Location: Optional[str] = None


class DataSetImportSummary(BaseValidatorModel):
    failed: int
    inProgress: int
    pending: int
    succeeded: int
    total: int


class DataSetSummary(BaseValidatorModel):
    dataSetName: str
    creationTime: Optional[datetime] = None
    dataSetOrg: Optional[str] = None
    format: Optional[str] = None
    lastReferencedTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None


class RecordLength(BaseValidatorModel):
    max: int
    min: int


class GdgDetailAttributes(BaseValidatorModel):
    limit: Optional[int] = None
    rollDisposition: Optional[str] = None


class PoDetailAttributes(BaseValidatorModel):
    encoding: str
    format: str


class PsDetailAttributes(BaseValidatorModel):
    encoding: str
    format: str


class GdgAttributes(BaseValidatorModel):
    limit: Optional[int] = None
    rollDisposition: Optional[str] = None


class PoAttributes(BaseValidatorModel):
    format: str
    memberFileExtensions: List[str]
    encoding: Optional[str] = None


class PsAttributes(BaseValidatorModel):
    format: str
    encoding: Optional[str] = None


class DeleteApplicationFromEnvironmentRequest(BaseValidatorModel):
    applicationId: str
    environmentId: str


class DeleteApplicationRequest(BaseValidatorModel):
    applicationId: str


class DeleteEnvironmentRequest(BaseValidatorModel):
    environmentId: str


class DeployedVersionSummary(BaseValidatorModel):
    applicationVersion: int
    status: DeploymentLifecycleType
    statusReason: Optional[str] = None


class DeploymentSummary(BaseValidatorModel):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: Optional[str] = None


class EfsStorageConfiguration(BaseValidatorModel):
    fileSystemId: str
    mountPoint: str


class EngineVersionsSummary(BaseValidatorModel):
    engineType: str
    engineVersion: str


class EnvironmentSummary(BaseValidatorModel):
    creationTime: datetime
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    instanceType: str
    name: str
    status: EnvironmentLifecycleType
    networkType: Optional[NetworkTypeType] = None


class FsxStorageConfiguration(BaseValidatorModel):
    fileSystemId: str
    mountPoint: str


# This class is the input for the 'get_application' function.
class GetApplicationRequest(BaseValidatorModel):
    applicationId: str


class LogGroupSummary(BaseValidatorModel):
    logGroupName: str
    logType: str


# This class is the input for the 'get_application_version' function.
class GetApplicationVersionRequest(BaseValidatorModel):
    applicationId: str
    applicationVersion: int


# This class is the input for the 'get_batch_job_execution' function.
class GetBatchJobExecutionRequest(BaseValidatorModel):
    applicationId: str
    executionId: str


class JobStepRestartMarker(BaseValidatorModel):
    fromStep: str
    fromProcStep: Optional[str] = None
    toProcStep: Optional[str] = None
    toStep: Optional[str] = None


# This class is the input for the 'get_data_set_details' function.
class GetDataSetDetailsRequest(BaseValidatorModel):
    applicationId: str
    dataSetName: str


# This class is the input for the 'get_data_set_import_task' function.
class GetDataSetImportTaskRequest(BaseValidatorModel):
    applicationId: str
    taskId: str


# This class is the input for the 'get_deployment' function.
class GetDeploymentRequest(BaseValidatorModel):
    applicationId: str
    deploymentId: str


# This class is the input for the 'get_environment' function.
class GetEnvironmentRequest(BaseValidatorModel):
    environmentId: str


class JobIdentifier(BaseValidatorModel):
    fileName: Optional[str] = None
    scriptName: Optional[str] = None


class JobStep(BaseValidatorModel):
    procStepName: Optional[str] = None
    procStepNumber: Optional[int] = None
    stepCondCode: Optional[str] = None
    stepName: Optional[str] = None
    stepNumber: Optional[int] = None
    stepRestartable: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_application_versions' function.
class ListApplicationVersionsRequest(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    environmentId: Optional[str] = None
    maxResults: Optional[int] = None
    names: Optional[List[str]] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_batch_job_definitions' function.
class ListBatchJobDefinitionsRequest(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_batch_job_restart_points' function.
class ListBatchJobRestartPointsRequest(BaseValidatorModel):
    applicationId: str
    executionId: str
    authSecretsManagerArn: Optional[str] = None


# This class is the input for the 'list_data_set_import_history' function.
class ListDataSetImportHistoryRequest(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_data_sets' function.
class ListDataSetsRequest(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nameFilter: Optional[str] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None


# This class is the input for the 'list_deployments' function.
class ListDeploymentsRequest(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_engine_versions' function.
class ListEngineVersionsRequest(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environments' function.
class ListEnvironmentsRequest(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    maxResults: Optional[int] = None
    names: Optional[List[str]] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class MaintenanceSchedule(BaseValidatorModel):
    endTime: Optional[datetime] = None
    startTime: Optional[datetime] = None


class PrimaryKey(BaseValidatorModel):
    length: int
    offset: int
    name: Optional[str] = None


class StartApplicationRequest(BaseValidatorModel):
    applicationId: str


class StopApplicationRequest(BaseValidatorModel):
    applicationId: str
    forceStop: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_environment' function.
class UpdateEnvironmentRequest(BaseValidatorModel):
    environmentId: str
    applyDuringMaintenanceWindow: Optional[bool] = None
    desiredCapacity: Optional[int] = None
    engineVersion: Optional[str] = None
    forceUpdate: Optional[bool] = None
    instanceType: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None


class BatchJobDefinition(BaseValidatorModel):
    fileBatchJobDefinition: Optional[FileBatchJobDefinition] = None
    scriptBatchJobDefinition: Optional[ScriptBatchJobDefinition] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    definition: Definition
    engineType: EngineTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_application' function.
class UpdateApplicationRequest(BaseValidatorModel):
    applicationId: str
    currentApplicationVersion: int
    definition: Optional[Definition] = None
    description: Optional[str] = None


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    applicationArn: str
    applicationId: str
    applicationVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_set_import_task' function.
class CreateDataSetImportTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_deployment' function.
class CreateDeploymentResponse(BaseValidatorModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_environment' function.
class CreateEnvironmentResponse(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_application_version' function.
class GetApplicationVersionResponse(BaseValidatorModel):
    applicationVersion: int
    creationTime: datetime
    definitionContent: str
    description: str
    name: str
    status: ApplicationVersionLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_deployment' function.
class GetDeploymentResponse(BaseValidatorModel):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadata


class GetSignedBluinsightsUrlResponse(BaseValidatorModel):
    signedBiUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_application_versions' function.
class ListApplicationVersionsResponse(BaseValidatorModel):
    applicationVersions: List[ApplicationVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_batch_job' function.
class StartBatchJobResponse(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_application' function.
class UpdateApplicationResponse(BaseValidatorModel):
    applicationVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment' function.
class UpdateEnvironmentResponse(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadata


class DataSetImportTask(BaseValidatorModel):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummary
    taskId: str
    statusReason: Optional[str] = None


# This class is the output for the 'get_data_set_import_task' function.
class GetDataSetImportTaskResponse(BaseValidatorModel):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummary
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_sets' function.
class ListDataSetsResponse(BaseValidatorModel):
    dataSets: List[DataSetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_deployments' function.
class ListDeploymentsResponse(BaseValidatorModel):
    deployments: List[DeploymentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_engine_versions' function.
class ListEngineVersionsResponse(BaseValidatorModel):
    engineVersions: List[EngineVersionsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environments' function.
class ListEnvironmentsResponse(BaseValidatorModel):
    environments: List[EnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StorageConfiguration(BaseValidatorModel):
    efs: Optional[EfsStorageConfiguration] = None
    fsx: Optional[FsxStorageConfiguration] = None


# This class is the output for the 'get_application' function.
class GetApplicationResponse(BaseValidatorModel):
    applicationArn: str
    applicationId: str
    creationTime: datetime
    deployedVersion: DeployedVersionSummary
    description: str
    engineType: EngineTypeType
    environmentId: str
    kmsKeyId: str
    lastStartTime: datetime
    latestVersion: ApplicationVersionSummary
    listenerArns: List[str]
    listenerPorts: List[int]
    loadBalancerDnsName: str
    logGroups: List[LogGroupSummary]
    name: str
    roleArn: str
    status: ApplicationLifecycleType
    statusReason: str
    tags: Dict[str, str]
    targetGroupArns: List[str]
    ResponseMetadata: ResponseMetadata


class RestartBatchJobIdentifier(BaseValidatorModel):
    executionId: str
    jobStepRestartMarker: JobStepRestartMarker


class S3BatchJobIdentifier(BaseValidatorModel):
    bucket: str
    identifier: JobIdentifier
    keyPrefix: Optional[str] = None


# This class is the output for the 'list_batch_job_restart_points' function.
class ListBatchJobRestartPointsResponse(BaseValidatorModel):
    batchJobSteps: List[JobStep]
    ResponseMetadata: ResponseMetadata


class ListApplicationVersionsRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    environmentId: Optional[str] = None
    names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBatchJobDefinitionsRequestPaginate(BaseValidatorModel):
    applicationId: str
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSetImportHistoryRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSetsRequestPaginate(BaseValidatorModel):
    applicationId: str
    nameFilter: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngineVersionsRequestPaginate(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBatchJobExecutionsRequestPaginate(BaseValidatorModel):
    applicationId: str
    executionIds: Optional[List[str]] = None
    jobName: Optional[str] = None
    startedAfter: Optional[Timestamp] = None
    startedBefore: Optional[Timestamp] = None
    status: Optional[BatchJobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_batch_job_executions' function.
class ListBatchJobExecutionsRequest(BaseValidatorModel):
    applicationId: str
    executionIds: Optional[List[str]] = None
    jobName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startedAfter: Optional[Timestamp] = None
    startedBefore: Optional[Timestamp] = None
    status: Optional[BatchJobExecutionStatusType] = None


class PendingMaintenance(BaseValidatorModel):
    engineVersion: Optional[str] = None
    schedule: Optional[MaintenanceSchedule] = None


class VsamAttributes(BaseValidatorModel):
    format: str
    alternateKeys: Optional[List[AlternateKey]] = None
    compressed: Optional[bool] = None
    encoding: Optional[str] = None
    primaryKey: Optional[PrimaryKey] = None


class VsamDetailAttributes(BaseValidatorModel):
    alternateKeys: Optional[List[AlternateKey]] = None
    cacheAtStartup: Optional[bool] = None
    compressed: Optional[bool] = None
    encoding: Optional[str] = None
    primaryKey: Optional[PrimaryKey] = None
    recordFormat: Optional[str] = None


# This class is the output for the 'list_batch_job_definitions' function.
class ListBatchJobDefinitionsResponse(BaseValidatorModel):
    batchJobDefinitions: List[BatchJobDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_data_set_import_history' function.
class ListDataSetImportHistoryResponse(BaseValidatorModel):
    dataSetImportTasks: List[DataSetImportTask]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_environment' function.
class CreateEnvironmentRequest(BaseValidatorModel):
    engineType: EngineTypeType
    instanceType: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    engineVersion: Optional[str] = None
    highAvailabilityConfig: Optional[HighAvailabilityConfig] = None
    kmsKeyId: Optional[str] = None
    networkType: Optional[NetworkTypeType] = None
    preferredMaintenanceWindow: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[List[str]] = None
    storageConfigurations: Optional[List[StorageConfiguration]] = None
    subnetIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None


class BatchJobIdentifier(BaseValidatorModel):
    fileBatchJobIdentifier: Optional[FileBatchJobIdentifier] = None
    restartBatchJobIdentifier: Optional[RestartBatchJobIdentifier] = None
    s3BatchJobIdentifier: Optional[S3BatchJobIdentifier] = None
    scriptBatchJobIdentifier: Optional[ScriptBatchJobIdentifier] = None


# This class is the output for the 'get_environment' function.
class GetEnvironmentResponse(BaseValidatorModel):
    actualCapacity: int
    creationTime: datetime
    description: str
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    highAvailabilityConfig: HighAvailabilityConfig
    instanceType: str
    kmsKeyId: str
    loadBalancerArn: str
    name: str
    networkType: NetworkTypeType
    pendingMaintenance: PendingMaintenance
    preferredMaintenanceWindow: str
    publiclyAccessible: bool
    securityGroupIds: List[str]
    status: EnvironmentLifecycleType
    statusReason: str
    storageConfigurations: List[StorageConfiguration]
    subnetIds: List[str]
    tags: Dict[str, str]
    vpcId: str
    ResponseMetadata: ResponseMetadata


class DatasetOrgAttributes(BaseValidatorModel):
    gdg: Optional[GdgAttributes] = None
    po: Optional[PoAttributes] = None
    ps: Optional[PsAttributes] = None
    vsam: Optional[VsamAttributes] = None


class DatasetDetailOrgAttributes(BaseValidatorModel):
    gdg: Optional[GdgDetailAttributes] = None
    po: Optional[PoDetailAttributes] = None
    ps: Optional[PsDetailAttributes] = None
    vsam: Optional[VsamDetailAttributes] = None


class BatchJobExecutionSummary(BaseValidatorModel):
    applicationId: str
    executionId: str
    startTime: datetime
    status: BatchJobExecutionStatusType
    batchJobIdentifier: Optional[BatchJobIdentifier] = None
    endTime: Optional[datetime] = None
    jobId: Optional[str] = None
    jobName: Optional[str] = None
    jobType: Optional[BatchJobTypeType] = None
    returnCode: Optional[str] = None


# This class is the output for the 'get_batch_job_execution' function.
class GetBatchJobExecutionResponse(BaseValidatorModel):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifier
    endTime: datetime
    executionId: str
    jobId: str
    jobName: str
    jobStepRestartMarker: JobStepRestartMarker
    jobType: BatchJobTypeType
    jobUser: str
    returnCode: str
    startTime: datetime
    status: BatchJobExecutionStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_batch_job' function.
class StartBatchJobRequest(BaseValidatorModel):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifier
    authSecretsManagerArn: Optional[str] = None
    jobParams: Optional[Dict[str, str]] = None


class DataSet(BaseValidatorModel):
    datasetName: str
    datasetOrg: DatasetOrgAttributes
    recordLength: RecordLength
    relativePath: Optional[str] = None
    storageType: Optional[str] = None


# This class is the output for the 'get_data_set_details' function.
class GetDataSetDetailsResponse(BaseValidatorModel):
    blocksize: int
    creationTime: datetime
    dataSetName: str
    dataSetOrg: DatasetDetailOrgAttributes
    fileSize: int
    lastReferencedTime: datetime
    lastUpdatedTime: datetime
    location: str
    recordLength: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_batch_job_executions' function.
class ListBatchJobExecutionsResponse(BaseValidatorModel):
    batchJobExecutions: List[BatchJobExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataSetImportItem(BaseValidatorModel):
    dataSet: DataSet
    externalLocation: ExternalLocation


class DataSetImportConfig(BaseValidatorModel):
    dataSets: Optional[List[DataSetImportItem]] = None
    s3Location: Optional[str] = None


# This class is the input for the 'create_data_set_import_task' function.
class CreateDataSetImportTaskRequest(BaseValidatorModel):
    applicationId: str
    importConfig: DataSetImportConfig
    clientToken: Optional[str] = None