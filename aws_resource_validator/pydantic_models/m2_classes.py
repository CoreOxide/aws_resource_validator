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
from aws_resource_validator.pydantic_models.m2_constants import *

class AlternateKeyTypeDef(BaseModel):
    length: int
    offset: int
    allowDuplicates: Optional[bool] = None
    name: Optional[str] = None

class ApplicationSummaryTypeDef(BaseModel):
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

class ApplicationVersionSummaryTypeDef(BaseModel):
    applicationVersion: int
    creationTime: datetime
    status: ApplicationVersionLifecycleType
    statusReason: Optional[str] = None

class FileBatchJobDefinitionTypeDef(BaseModel):
    fileName: str
    folderPath: Optional[str] = None

class ScriptBatchJobDefinitionTypeDef(BaseModel):
    scriptName: str

class FileBatchJobIdentifierTypeDef(BaseModel):
    fileName: str
    folderPath: Optional[str] = None

class ScriptBatchJobIdentifierTypeDef(BaseModel):
    scriptName: str

class CancelBatchJobExecutionRequestRequestTypeDef(BaseModel):
    applicationId: str
    executionId: str

class DefinitionTypeDef(BaseModel):
    content: Optional[str] = None
    s3Location: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    applicationId: str
    applicationVersion: int
    environmentId: str
    clientToken: Optional[str] = None

class HighAvailabilityConfigTypeDef(BaseModel):
    desiredCapacity: int

class ExternalLocationTypeDef(BaseModel):
    s3Location: Optional[str] = None

class DataSetImportSummaryTypeDef(BaseModel):
    failed: int
    inProgress: int
    pending: int
    succeeded: int
    total: int

class DataSetSummaryTypeDef(BaseModel):
    dataSetName: str
    creationTime: Optional[datetime] = None
    dataSetOrg: Optional[str] = None
    format: Optional[str] = None
    lastReferencedTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None

class RecordLengthTypeDef(BaseModel):
    max: int
    min: int

class GdgDetailAttributesTypeDef(BaseModel):
    limit: Optional[int] = None
    rollDisposition: Optional[str] = None

class PoDetailAttributesTypeDef(BaseModel):
    encoding: str
    format: str

class PsDetailAttributesTypeDef(BaseModel):
    encoding: str
    format: str

class GdgAttributesTypeDef(BaseModel):
    limit: Optional[int] = None
    rollDisposition: Optional[str] = None

class PoAttributesTypeDef(BaseModel):
    format: str
    memberFileExtensions: Sequence[str]
    encoding: Optional[str] = None

class PsAttributesTypeDef(BaseModel):
    format: str
    encoding: Optional[str] = None

class DeleteApplicationFromEnvironmentRequestRequestTypeDef(BaseModel):
    applicationId: str
    environmentId: str

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class DeleteEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str

class DeployedVersionSummaryTypeDef(BaseModel):
    applicationVersion: int
    status: DeploymentLifecycleType
    statusReason: Optional[str] = None

class DeploymentSummaryTypeDef(BaseModel):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: Optional[str] = None

class EfsStorageConfigurationTypeDef(BaseModel):
    fileSystemId: str
    mountPoint: str

class EngineVersionsSummaryTypeDef(BaseModel):
    engineType: str
    engineVersion: str

class EnvironmentSummaryTypeDef(BaseModel):
    creationTime: datetime
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    instanceType: str
    name: str
    status: EnvironmentLifecycleType

class FsxStorageConfigurationTypeDef(BaseModel):
    fileSystemId: str
    mountPoint: str

class GetApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class LogGroupSummaryTypeDef(BaseModel):
    logGroupName: str
    logType: str

class GetApplicationVersionRequestRequestTypeDef(BaseModel):
    applicationId: str
    applicationVersion: int

class GetBatchJobExecutionRequestRequestTypeDef(BaseModel):
    applicationId: str
    executionId: str

class JobStepRestartMarkerTypeDef(BaseModel):
    fromStep: str
    fromProcStep: Optional[str] = None
    toProcStep: Optional[str] = None
    toStep: Optional[str] = None

class GetDataSetDetailsRequestRequestTypeDef(BaseModel):
    applicationId: str
    dataSetName: str

class GetDataSetImportTaskRequestRequestTypeDef(BaseModel):
    applicationId: str
    taskId: str

class GetDeploymentRequestRequestTypeDef(BaseModel):
    applicationId: str
    deploymentId: str

class GetEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str

class JobIdentifierTypeDef(BaseModel):
    fileName: Optional[str] = None
    scriptName: Optional[str] = None

class JobStepTypeDef(BaseModel):
    procStepName: Optional[str] = None
    procStepNumber: Optional[int] = None
    stepCondCode: Optional[str] = None
    stepName: Optional[str] = None
    stepNumber: Optional[int] = None
    stepRestartable: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationVersionsRequestRequestTypeDef(BaseModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    environmentId: Optional[str] = None
    maxResults: Optional[int] = None
    names: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListBatchJobDefinitionsRequestRequestTypeDef(BaseModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

class ListBatchJobRestartPointsRequestRequestTypeDef(BaseModel):
    applicationId: str
    executionId: str

class ListDataSetImportHistoryRequestRequestTypeDef(BaseModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataSetsRequestRequestTypeDef(BaseModel):
    applicationId: str
    maxResults: Optional[int] = None
    nameFilter: Optional[str] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEngineVersionsRequestRequestTypeDef(BaseModel):
    engineType: Optional[EngineTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentsRequestRequestTypeDef(BaseModel):
    engineType: Optional[EngineTypeType] = None
    maxResults: Optional[int] = None
    names: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MaintenanceScheduleTypeDef(BaseModel):
    endTime: Optional[datetime] = None
    startTime: Optional[datetime] = None

class PrimaryKeyTypeDef(BaseModel):
    length: int
    offset: int
    name: Optional[str] = None

class StartApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class StopApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str
    forceStop: Optional[bool] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str
    applyDuringMaintenanceWindow: Optional[bool] = None
    desiredCapacity: Optional[int] = None
    engineVersion: Optional[str] = None
    forceUpdate: Optional[bool] = None
    instanceType: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None

class BatchJobDefinitionTypeDef(BaseModel):
    fileBatchJobDefinition: Optional[FileBatchJobDefinitionTypeDef] = None
    scriptBatchJobDefinition: Optional[ScriptBatchJobDefinitionTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    definition: DefinitionTypeDef
    engineType: EngineTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str
    currentApplicationVersion: int
    definition: Optional[DefinitionTypeDef] = None
    description: Optional[str] = None

class CreateApplicationResponseTypeDef(BaseModel):
    applicationArn: str
    applicationId: str
    applicationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetImportTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentResponseTypeDef(BaseModel):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationVersionResponseTypeDef(BaseModel):
    applicationVersion: int
    creationTime: datetime
    definitionContent: str
    description: str
    name: str
    status: ApplicationVersionLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentResponseTypeDef(BaseModel):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSignedBluinsightsUrlResponseTypeDef(BaseModel):
    signedBiUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationVersionsResponseTypeDef(BaseModel):
    applicationVersions: List[ApplicationVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    applications: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartBatchJobResponseTypeDef(BaseModel):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseModel):
    applicationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(BaseModel):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetImportTaskTypeDef(BaseModel):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummaryTypeDef
    taskId: str
    statusReason: Optional[str] = None

class GetDataSetImportTaskResponseTypeDef(BaseModel):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummaryTypeDef
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSetsResponseTypeDef(BaseModel):
    dataSets: List[DataSetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsResponseTypeDef(BaseModel):
    deployments: List[DeploymentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEngineVersionsResponseTypeDef(BaseModel):
    engineVersions: List[EngineVersionsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(BaseModel):
    environments: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StorageConfigurationTypeDef(BaseModel):
    efs: Optional[EfsStorageConfigurationTypeDef] = None
    fsx: Optional[FsxStorageConfigurationTypeDef] = None

class GetApplicationResponseTypeDef(BaseModel):
    applicationArn: str
    applicationId: str
    creationTime: datetime
    deployedVersion: DeployedVersionSummaryTypeDef
    description: str
    engineType: EngineTypeType
    environmentId: str
    kmsKeyId: str
    lastStartTime: datetime
    latestVersion: ApplicationVersionSummaryTypeDef
    listenerArns: List[str]
    listenerPorts: List[int]
    loadBalancerDnsName: str
    logGroups: List[LogGroupSummaryTypeDef]
    name: str
    roleArn: str
    status: ApplicationLifecycleType
    statusReason: str
    tags: Dict[str, str]
    targetGroupArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RestartBatchJobIdentifierTypeDef(BaseModel):
    executionId: str
    jobStepRestartMarker: JobStepRestartMarkerTypeDef

class S3BatchJobIdentifierTypeDef(BaseModel):
    bucket: str
    identifier: JobIdentifierTypeDef
    keyPrefix: Optional[str] = None

class ListBatchJobRestartPointsResponseTypeDef(BaseModel):
    batchJobSteps: List[JobStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    environmentId: Optional[str] = None
    names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchJobDefinitionsRequestListBatchJobDefinitionsPaginateTypeDef(BaseModel):
    applicationId: str
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetImportHistoryRequestListDataSetImportHistoryPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetsRequestListDataSetsPaginateTypeDef(BaseModel):
    applicationId: str
    nameFilter: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEngineVersionsRequestListEngineVersionsPaginateTypeDef(BaseModel):
    engineType: Optional[EngineTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseModel):
    engineType: Optional[EngineTypeType] = None
    names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchJobExecutionsRequestListBatchJobExecutionsPaginateTypeDef(BaseModel):
    applicationId: str
    executionIds: Optional[Sequence[str]] = None
    jobName: Optional[str] = None
    startedAfter: Optional[TimestampTypeDef] = None
    startedBefore: Optional[TimestampTypeDef] = None
    status: Optional[BatchJobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchJobExecutionsRequestRequestTypeDef(BaseModel):
    applicationId: str
    executionIds: Optional[Sequence[str]] = None
    jobName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startedAfter: Optional[TimestampTypeDef] = None
    startedBefore: Optional[TimestampTypeDef] = None
    status: Optional[BatchJobExecutionStatusType] = None

class PendingMaintenanceTypeDef(BaseModel):
    engineVersion: Optional[str] = None
    schedule: Optional[MaintenanceScheduleTypeDef] = None

class VsamAttributesTypeDef(BaseModel):
    format: str
    alternateKeys: Optional[Sequence[AlternateKeyTypeDef]] = None
    compressed: Optional[bool] = None
    encoding: Optional[str] = None
    primaryKey: Optional[PrimaryKeyTypeDef] = None

class VsamDetailAttributesTypeDef(BaseModel):
    alternateKeys: Optional[List[AlternateKeyTypeDef]] = None
    cacheAtStartup: Optional[bool] = None
    compressed: Optional[bool] = None
    encoding: Optional[str] = None
    primaryKey: Optional[PrimaryKeyTypeDef] = None
    recordFormat: Optional[str] = None

class ListBatchJobDefinitionsResponseTypeDef(BaseModel):
    batchJobDefinitions: List[BatchJobDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSetImportHistoryResponseTypeDef(BaseModel):
    dataSetImportTasks: List[DataSetImportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentRequestRequestTypeDef(BaseModel):
    engineType: EngineTypeType
    instanceType: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    engineVersion: Optional[str] = None
    highAvailabilityConfig: Optional[HighAvailabilityConfigTypeDef] = None
    kmsKeyId: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[Sequence[str]] = None
    storageConfigurations: Optional[Sequence[StorageConfigurationTypeDef]] = None
    subnetIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None

class BatchJobIdentifierTypeDef(BaseModel):
    fileBatchJobIdentifier: Optional[FileBatchJobIdentifierTypeDef] = None
    restartBatchJobIdentifier: Optional[RestartBatchJobIdentifierTypeDef] = None
    s3BatchJobIdentifier: Optional[S3BatchJobIdentifierTypeDef] = None
    scriptBatchJobIdentifier: Optional[ScriptBatchJobIdentifierTypeDef] = None

class GetEnvironmentResponseTypeDef(BaseModel):
    actualCapacity: int
    creationTime: datetime
    description: str
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    highAvailabilityConfig: HighAvailabilityConfigTypeDef
    instanceType: str
    kmsKeyId: str
    loadBalancerArn: str
    name: str
    pendingMaintenance: PendingMaintenanceTypeDef
    preferredMaintenanceWindow: str
    publiclyAccessible: bool
    securityGroupIds: List[str]
    status: EnvironmentLifecycleType
    statusReason: str
    storageConfigurations: List[StorageConfigurationTypeDef]
    subnetIds: List[str]
    tags: Dict[str, str]
    vpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetOrgAttributesTypeDef(BaseModel):
    gdg: Optional[GdgAttributesTypeDef] = None
    po: Optional[PoAttributesTypeDef] = None
    ps: Optional[PsAttributesTypeDef] = None
    vsam: Optional[VsamAttributesTypeDef] = None

class DatasetDetailOrgAttributesTypeDef(BaseModel):
    gdg: Optional[GdgDetailAttributesTypeDef] = None
    po: Optional[PoDetailAttributesTypeDef] = None
    ps: Optional[PsDetailAttributesTypeDef] = None
    vsam: Optional[VsamDetailAttributesTypeDef] = None

class BatchJobExecutionSummaryTypeDef(BaseModel):
    applicationId: str
    executionId: str
    startTime: datetime
    status: BatchJobExecutionStatusType
    batchJobIdentifier: Optional[BatchJobIdentifierTypeDef] = None
    endTime: Optional[datetime] = None
    jobId: Optional[str] = None
    jobName: Optional[str] = None
    jobType: Optional[BatchJobTypeType] = None
    returnCode: Optional[str] = None

class GetBatchJobExecutionResponseTypeDef(BaseModel):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifierTypeDef
    endTime: datetime
    executionId: str
    jobId: str
    jobName: str
    jobStepRestartMarker: JobStepRestartMarkerTypeDef
    jobType: BatchJobTypeType
    jobUser: str
    returnCode: str
    startTime: datetime
    status: BatchJobExecutionStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBatchJobRequestRequestTypeDef(BaseModel):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifierTypeDef
    jobParams: Optional[Mapping[str, str]] = None

class DataSetTypeDef(BaseModel):
    datasetName: str
    datasetOrg: DatasetOrgAttributesTypeDef
    recordLength: RecordLengthTypeDef
    relativePath: Optional[str] = None
    storageType: Optional[str] = None

class GetDataSetDetailsResponseTypeDef(BaseModel):
    blocksize: int
    creationTime: datetime
    dataSetName: str
    dataSetOrg: DatasetDetailOrgAttributesTypeDef
    fileSize: int
    lastReferencedTime: datetime
    lastUpdatedTime: datetime
    location: str
    recordLength: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListBatchJobExecutionsResponseTypeDef(BaseModel):
    batchJobExecutions: List[BatchJobExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetImportItemTypeDef(BaseModel):
    dataSet: DataSetTypeDef
    externalLocation: ExternalLocationTypeDef

class DataSetImportConfigTypeDef(BaseModel):
    dataSets: Optional[Sequence[DataSetImportItemTypeDef]] = None
    s3Location: Optional[str] = None

class CreateDataSetImportTaskRequestRequestTypeDef(BaseModel):
    applicationId: str
    importConfig: DataSetImportConfigTypeDef
    clientToken: Optional[str] = None

