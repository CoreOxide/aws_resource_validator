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
from aws_resource_validator.pydantic_models.m2_constants import *

class AlternateKeyTypeDef(BaseValidatorModel):
    length: int
    offset: int
    allowDuplicates: Optional[bool] = None
    name: Optional[str] = None

class ApplicationSummaryTypeDef(BaseValidatorModel):
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

class ApplicationVersionSummaryTypeDef(BaseValidatorModel):
    applicationVersion: int
    creationTime: datetime
    status: ApplicationVersionLifecycleType
    statusReason: Optional[str] = None

class FileBatchJobDefinitionTypeDef(BaseValidatorModel):
    fileName: str
    folderPath: Optional[str] = None

class ScriptBatchJobDefinitionTypeDef(BaseValidatorModel):
    scriptName: str

class FileBatchJobIdentifierTypeDef(BaseValidatorModel):
    fileName: str
    folderPath: Optional[str] = None

class ScriptBatchJobIdentifierTypeDef(BaseValidatorModel):
    scriptName: str

class CancelBatchJobExecutionRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    executionId: str

class DefinitionTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    s3Location: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    applicationVersion: int
    environmentId: str
    clientToken: Optional[str] = None

class HighAvailabilityConfigTypeDef(BaseValidatorModel):
    desiredCapacity: int

class ExternalLocationTypeDef(BaseValidatorModel):
    s3Location: Optional[str] = None

class DataSetImportSummaryTypeDef(BaseValidatorModel):
    failed: int
    inProgress: int
    pending: int
    succeeded: int
    total: int

class DataSetSummaryTypeDef(BaseValidatorModel):
    dataSetName: str
    creationTime: Optional[datetime] = None
    dataSetOrg: Optional[str] = None
    format: Optional[str] = None
    lastReferencedTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None

class RecordLengthTypeDef(BaseValidatorModel):
    max: int
    min: int

class GdgDetailAttributesTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    rollDisposition: Optional[str] = None

class PoDetailAttributesTypeDef(BaseValidatorModel):
    encoding: str
    format: str

class PsDetailAttributesTypeDef(BaseValidatorModel):
    encoding: str
    format: str

class GdgAttributesTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    rollDisposition: Optional[str] = None

class PoAttributesTypeDef(BaseValidatorModel):
    format: str
    memberFileExtensions: Sequence[str]
    encoding: Optional[str] = None

class PsAttributesTypeDef(BaseValidatorModel):
    format: str
    encoding: Optional[str] = None

class DeleteApplicationFromEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    environmentId: str

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class DeleteEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class DeployedVersionSummaryTypeDef(BaseValidatorModel):
    applicationVersion: int
    status: DeploymentLifecycleType
    statusReason: Optional[str] = None

class DeploymentSummaryTypeDef(BaseValidatorModel):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: Optional[str] = None

class EfsStorageConfigurationTypeDef(BaseValidatorModel):
    fileSystemId: str
    mountPoint: str

class EngineVersionsSummaryTypeDef(BaseValidatorModel):
    engineType: str
    engineVersion: str

class EnvironmentSummaryTypeDef(BaseValidatorModel):
    creationTime: datetime
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    instanceType: str
    name: str
    status: EnvironmentLifecycleType

class FsxStorageConfigurationTypeDef(BaseValidatorModel):
    fileSystemId: str
    mountPoint: str

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class LogGroupSummaryTypeDef(BaseValidatorModel):
    logGroupName: str
    logType: str

class GetApplicationVersionRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    applicationVersion: int

class GetBatchJobExecutionRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    executionId: str

class JobStepRestartMarkerTypeDef(BaseValidatorModel):
    fromStep: str
    fromProcStep: Optional[str] = None
    toProcStep: Optional[str] = None
    toStep: Optional[str] = None

class GetDataSetDetailsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    dataSetName: str

class GetDataSetImportTaskRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    taskId: str

class GetDeploymentRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    deploymentId: str

class GetEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class JobIdentifierTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    scriptName: Optional[str] = None

class JobStepTypeDef(BaseValidatorModel):
    procStepName: Optional[str] = None
    procStepNumber: Optional[int] = None
    stepCondCode: Optional[str] = None
    stepName: Optional[str] = None
    stepNumber: Optional[int] = None
    stepRestartable: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationVersionsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    environmentId: Optional[str] = None
    maxResults: Optional[int] = None
    names: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListBatchJobDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

class ListBatchJobRestartPointsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    executionId: str

class ListDataSetImportHistoryRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataSetsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nameFilter: Optional[str] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEngineVersionsRequestRequestTypeDef(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    maxResults: Optional[int] = None
    names: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MaintenanceScheduleTypeDef(BaseValidatorModel):
    endTime: Optional[datetime] = None
    startTime: Optional[datetime] = None

class PrimaryKeyTypeDef(BaseValidatorModel):
    length: int
    offset: int
    name: Optional[str] = None

class StartApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class StopApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    forceStop: Optional[bool] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    applyDuringMaintenanceWindow: Optional[bool] = None
    desiredCapacity: Optional[int] = None
    engineVersion: Optional[str] = None
    forceUpdate: Optional[bool] = None
    instanceType: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None

class BatchJobDefinitionTypeDef(BaseValidatorModel):
    fileBatchJobDefinition: Optional[FileBatchJobDefinitionTypeDef] = None
    scriptBatchJobDefinition: Optional[ScriptBatchJobDefinitionTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    definition: DefinitionTypeDef
    engineType: EngineTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    currentApplicationVersion: int
    definition: Optional[DefinitionTypeDef] = None
    description: Optional[str] = None

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    applicationArn: str
    applicationId: str
    applicationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetImportTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseValidatorModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentResponseTypeDef(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationVersionResponseTypeDef(BaseValidatorModel):
    applicationVersion: int
    creationTime: datetime
    definitionContent: str
    description: str
    name: str
    status: ApplicationVersionLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentResponseTypeDef(BaseValidatorModel):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSignedBluinsightsUrlResponseTypeDef(BaseValidatorModel):
    signedBiUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationVersionsResponseTypeDef(BaseValidatorModel):
    applicationVersions: List[ApplicationVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    applications: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartBatchJobResponseTypeDef(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseValidatorModel):
    applicationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetImportTaskTypeDef(BaseValidatorModel):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummaryTypeDef
    taskId: str
    statusReason: Optional[str] = None

class GetDataSetImportTaskResponseTypeDef(BaseValidatorModel):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummaryTypeDef
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSetsResponseTypeDef(BaseValidatorModel):
    dataSets: List[DataSetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsResponseTypeDef(BaseValidatorModel):
    deployments: List[DeploymentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEngineVersionsResponseTypeDef(BaseValidatorModel):
    engineVersions: List[EngineVersionsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StorageConfigurationTypeDef(BaseValidatorModel):
    efs: Optional[EfsStorageConfigurationTypeDef] = None
    fsx: Optional[FsxStorageConfigurationTypeDef] = None

class GetApplicationResponseTypeDef(BaseValidatorModel):
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

class RestartBatchJobIdentifierTypeDef(BaseValidatorModel):
    executionId: str
    jobStepRestartMarker: JobStepRestartMarkerTypeDef

class S3BatchJobIdentifierTypeDef(BaseValidatorModel):
    bucket: str
    identifier: JobIdentifierTypeDef
    keyPrefix: Optional[str] = None

class ListBatchJobRestartPointsResponseTypeDef(BaseValidatorModel):
    batchJobSteps: List[JobStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    environmentId: Optional[str] = None
    names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchJobDefinitionsRequestListBatchJobDefinitionsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetImportHistoryRequestListDataSetImportHistoryPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetsRequestListDataSetsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    nameFilter: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEngineVersionsRequestListEngineVersionsPaginateTypeDef(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseValidatorModel):
    engineType: Optional[EngineTypeType] = None
    names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchJobExecutionsRequestListBatchJobExecutionsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    executionIds: Optional[Sequence[str]] = None
    jobName: Optional[str] = None
    startedAfter: Optional[TimestampTypeDef] = None
    startedBefore: Optional[TimestampTypeDef] = None
    status: Optional[BatchJobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchJobExecutionsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    executionIds: Optional[Sequence[str]] = None
    jobName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startedAfter: Optional[TimestampTypeDef] = None
    startedBefore: Optional[TimestampTypeDef] = None
    status: Optional[BatchJobExecutionStatusType] = None

class PendingMaintenanceTypeDef(BaseValidatorModel):
    engineVersion: Optional[str] = None
    schedule: Optional[MaintenanceScheduleTypeDef] = None

class VsamAttributesTypeDef(BaseValidatorModel):
    format: str
    alternateKeys: Optional[Sequence[AlternateKeyTypeDef]] = None
    compressed: Optional[bool] = None
    encoding: Optional[str] = None
    primaryKey: Optional[PrimaryKeyTypeDef] = None

class VsamDetailAttributesTypeDef(BaseValidatorModel):
    alternateKeys: Optional[List[AlternateKeyTypeDef]] = None
    cacheAtStartup: Optional[bool] = None
    compressed: Optional[bool] = None
    encoding: Optional[str] = None
    primaryKey: Optional[PrimaryKeyTypeDef] = None
    recordFormat: Optional[str] = None

class ListBatchJobDefinitionsResponseTypeDef(BaseValidatorModel):
    batchJobDefinitions: List[BatchJobDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSetImportHistoryResponseTypeDef(BaseValidatorModel):
    dataSetImportTasks: List[DataSetImportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
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

class BatchJobIdentifierTypeDef(BaseValidatorModel):
    fileBatchJobIdentifier: Optional[FileBatchJobIdentifierTypeDef] = None
    restartBatchJobIdentifier: Optional[RestartBatchJobIdentifierTypeDef] = None
    s3BatchJobIdentifier: Optional[S3BatchJobIdentifierTypeDef] = None
    scriptBatchJobIdentifier: Optional[ScriptBatchJobIdentifierTypeDef] = None

class GetEnvironmentResponseTypeDef(BaseValidatorModel):
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

class DatasetOrgAttributesTypeDef(BaseValidatorModel):
    gdg: Optional[GdgAttributesTypeDef] = None
    po: Optional[PoAttributesTypeDef] = None
    ps: Optional[PsAttributesTypeDef] = None
    vsam: Optional[VsamAttributesTypeDef] = None

class DatasetDetailOrgAttributesTypeDef(BaseValidatorModel):
    gdg: Optional[GdgDetailAttributesTypeDef] = None
    po: Optional[PoDetailAttributesTypeDef] = None
    ps: Optional[PsDetailAttributesTypeDef] = None
    vsam: Optional[VsamDetailAttributesTypeDef] = None

class BatchJobExecutionSummaryTypeDef(BaseValidatorModel):
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

class GetBatchJobExecutionResponseTypeDef(BaseValidatorModel):
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

class StartBatchJobRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifierTypeDef
    jobParams: Optional[Mapping[str, str]] = None

class DataSetTypeDef(BaseValidatorModel):
    datasetName: str
    datasetOrg: DatasetOrgAttributesTypeDef
    recordLength: RecordLengthTypeDef
    relativePath: Optional[str] = None
    storageType: Optional[str] = None

class GetDataSetDetailsResponseTypeDef(BaseValidatorModel):
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

class ListBatchJobExecutionsResponseTypeDef(BaseValidatorModel):
    batchJobExecutions: List[BatchJobExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetImportItemTypeDef(BaseValidatorModel):
    dataSet: DataSetTypeDef
    externalLocation: ExternalLocationTypeDef

class DataSetImportConfigTypeDef(BaseValidatorModel):
    dataSets: Optional[Sequence[DataSetImportItemTypeDef]] = None
    s3Location: Optional[str] = None

class CreateDataSetImportTaskRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    importConfig: DataSetImportConfigTypeDef
    clientToken: Optional[str] = None

