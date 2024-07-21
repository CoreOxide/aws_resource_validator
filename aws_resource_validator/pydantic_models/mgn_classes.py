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
from aws_resource_validator.pydantic_models.mgn_constants import *

class ApplicationAggregatedStatusTypeDef(BaseModel):
    healthStatus: Optional[ApplicationHealthStatusType] = None
    lastUpdateDateTime: Optional[str] = None
    progressStatus: Optional[ApplicationProgressStatusType] = None
    totalSourceServers: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ArchiveApplicationRequestRequestTypeDef(BaseModel):
    applicationID: str
    accountID: Optional[str] = None

class ArchiveWaveRequestRequestTypeDef(BaseModel):
    waveID: str
    accountID: Optional[str] = None

class AssociateApplicationsRequestRequestTypeDef(BaseModel):
    applicationIDs: Sequence[str]
    waveID: str
    accountID: Optional[str] = None

class AssociateSourceServersRequestRequestTypeDef(BaseModel):
    applicationID: str
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None

class CPUTypeDef(BaseModel):
    cores: Optional[int] = None
    modelName: Optional[str] = None

class ChangeServerLifeCycleStateSourceServerLifecycleTypeDef(BaseModel):
    state: ChangeServerLifeCycleStateSourceServerLifecycleStateType

class ConnectorSsmCommandConfigTypeDef(BaseModel):
    cloudWatchOutputEnabled: bool
    s3OutputEnabled: bool
    cloudWatchLogGroupName: Optional[str] = None
    outputS3BucketName: Optional[str] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    name: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class LaunchTemplateDiskConfTypeDef(BaseModel):
    iops: Optional[int] = None
    throughput: Optional[int] = None
    volumeType: Optional[VolumeTypeType] = None

class LicensingTypeDef(BaseModel):
    osByol: Optional[bool] = None

class CreateReplicationConfigurationTemplateRequestRequestTypeDef(BaseModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: Sequence[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Mapping[str, str]
    useDedicatedReplicationServer: bool
    ebsEncryptionKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    useFipsEndpoint: Optional[bool] = None

class CreateWaveRequestRequestTypeDef(BaseModel):
    name: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DataReplicationErrorTypeDef(BaseModel):
    error: Optional[DataReplicationErrorStringType] = None
    rawError: Optional[str] = None

class DataReplicationInfoReplicatedDiskTypeDef(BaseModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None

class DataReplicationInitiationStepTypeDef(BaseModel):
    name: Optional[DataReplicationInitiationStepNameType] = None
    status: Optional[DataReplicationInitiationStepStatusType] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    applicationID: str
    accountID: Optional[str] = None

class DeleteConnectorRequestRequestTypeDef(BaseModel):
    connectorID: str

class DeleteJobRequestRequestTypeDef(BaseModel):
    jobID: str
    accountID: Optional[str] = None

class DeleteLaunchConfigurationTemplateRequestRequestTypeDef(BaseModel):
    launchConfigurationTemplateID: str

class DeleteReplicationConfigurationTemplateRequestRequestTypeDef(BaseModel):
    replicationConfigurationTemplateID: str

class DeleteSourceServerRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class DeleteVcenterClientRequestRequestTypeDef(BaseModel):
    vcenterClientID: str

class DeleteWaveRequestRequestTypeDef(BaseModel):
    waveID: str
    accountID: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeJobLogItemsRequestRequestTypeDef(BaseModel):
    jobID: str
    accountID: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeJobsRequestFiltersTypeDef(BaseModel):
    fromDate: Optional[str] = None
    jobIDs: Optional[Sequence[str]] = None
    toDate: Optional[str] = None

class DescribeLaunchConfigurationTemplatesRequestRequestTypeDef(BaseModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeReplicationConfigurationTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None

class ReplicationConfigurationTemplateTypeDef(BaseModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[       ReplicationConfigurationDefaultLargeStagingDiskTypeType     ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None

class DescribeSourceServersRequestFiltersTypeDef(BaseModel):
    applicationIDs: Optional[Sequence[str]] = None
    isArchived: Optional[bool] = None
    lifeCycleStates: Optional[Sequence[LifeCycleStateType]] = None
    replicationTypes: Optional[Sequence[ReplicationTypeType]] = None
    sourceServerIDs: Optional[Sequence[str]] = None

class DescribeVcenterClientsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class VcenterClientTypeDef(BaseModel):
    arn: Optional[str] = None
    datacenterName: Optional[str] = None
    hostname: Optional[str] = None
    lastSeenDatetime: Optional[str] = None
    sourceServerTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    vcenterClientID: Optional[str] = None
    vcenterUUID: Optional[str] = None

class DisassociateApplicationsRequestRequestTypeDef(BaseModel):
    applicationIDs: Sequence[str]
    waveID: str
    accountID: Optional[str] = None

class DisassociateSourceServersRequestRequestTypeDef(BaseModel):
    applicationID: str
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None

class DisconnectFromServiceRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class DiskTypeDef(BaseModel):
    bytes: Optional[int] = None
    deviceName: Optional[str] = None

class ExportErrorDataTypeDef(BaseModel):
    rawError: Optional[str] = None

class ExportTaskSummaryTypeDef(BaseModel):
    applicationsCount: Optional[int] = None
    serversCount: Optional[int] = None
    wavesCount: Optional[int] = None

class FinalizeCutoverRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class GetLaunchConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class GetReplicationConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class IdentificationHintsTypeDef(BaseModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmPath: Optional[str] = None
    vmWareUuid: Optional[str] = None

class ImportErrorDataTypeDef(BaseModel):
    accountID: Optional[str] = None
    applicationID: Optional[str] = None
    ec2LaunchTemplateID: Optional[str] = None
    rawError: Optional[str] = None
    rowNumber: Optional[int] = None
    sourceServerID: Optional[str] = None
    waveID: Optional[str] = None

class ImportTaskSummaryApplicationsTypeDef(BaseModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None

class ImportTaskSummaryServersTypeDef(BaseModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None

class ImportTaskSummaryWavesTypeDef(BaseModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None

class S3BucketSourceTypeDef(BaseModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None

class JobLogEventDataTypeDef(BaseModel):
    conversionServerID: Optional[str] = None
    rawError: Optional[str] = None
    sourceServerID: Optional[str] = None
    targetInstanceID: Optional[str] = None

class LaunchedInstanceTypeDef(BaseModel):
    ec2InstanceID: Optional[str] = None
    firstBoot: Optional[FirstBootType] = None
    jobID: Optional[str] = None

class LifeCycleLastCutoverFinalizedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None

class LifeCycleLastCutoverInitiatedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None

class LifeCycleLastCutoverRevertedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None

class LifeCycleLastTestFinalizedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None

class LifeCycleLastTestInitiatedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None

class LifeCycleLastTestRevertedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None

class ListApplicationsRequestFiltersTypeDef(BaseModel):
    applicationIDs: Optional[Sequence[str]] = None
    isArchived: Optional[bool] = None
    waveIDs: Optional[Sequence[str]] = None

class ListConnectorsRequestFiltersTypeDef(BaseModel):
    connectorIDs: Optional[Sequence[str]] = None

class ListExportErrorsRequestRequestTypeDef(BaseModel):
    exportID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExportsRequestFiltersTypeDef(BaseModel):
    exportIDs: Optional[Sequence[str]] = None

class ListImportErrorsRequestRequestTypeDef(BaseModel):
    importID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportsRequestFiltersTypeDef(BaseModel):
    importIDs: Optional[Sequence[str]] = None

class ListManagedAccountsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ManagedAccountTypeDef(BaseModel):
    accountId: Optional[str] = None

class SourceServerActionsRequestFiltersTypeDef(BaseModel):
    actionIDs: Optional[Sequence[str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TemplateActionsRequestFiltersTypeDef(BaseModel):
    actionIDs: Optional[Sequence[str]] = None

class ListWavesRequestFiltersTypeDef(BaseModel):
    isArchived: Optional[bool] = None
    waveIDs: Optional[Sequence[str]] = None

class MarkAsArchivedRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class NetworkInterfaceTypeDef(BaseModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None

class OSTypeDef(BaseModel):
    fullString: Optional[str] = None

class PauseReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class SsmExternalParameterTypeDef(BaseModel):
    dynamicPath: Optional[str] = None

class SsmParameterStoreParameterTypeDef(BaseModel):
    parameterName: str
    parameterType: Literal["STRING"]

class RemoveSourceServerActionRequestRequestTypeDef(BaseModel):
    actionID: str
    sourceServerID: str
    accountID: Optional[str] = None

class RemoveTemplateActionRequestRequestTypeDef(BaseModel):
    actionID: str
    launchConfigurationTemplateID: str

class ReplicationConfigurationReplicatedDiskTypeDef(BaseModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None

class ResumeReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class RetryDataReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class SourceServerConnectorActionTypeDef(BaseModel):
    connectorArn: Optional[str] = None
    credentialsSecretArn: Optional[str] = None

class StartCutoverRequestRequestTypeDef(BaseModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StartExportRequestRequestTypeDef(BaseModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None

class StartReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class StartTestRequestRequestTypeDef(BaseModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StopReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateTargetInstancesRequestRequestTypeDef(BaseModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UnarchiveApplicationRequestRequestTypeDef(BaseModel):
    applicationID: str
    accountID: Optional[str] = None

class UnarchiveWaveRequestRequestTypeDef(BaseModel):
    waveID: str
    accountID: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    applicationID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None

class UpdateReplicationConfigurationTemplateRequestRequestTypeDef(BaseModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[       ReplicationConfigurationDefaultLargeStagingDiskTypeType     ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None

class UpdateSourceServerReplicationTypeRequestRequestTypeDef(BaseModel):
    replicationType: ReplicationTypeType
    sourceServerID: str
    accountID: Optional[str] = None

class UpdateWaveRequestRequestTypeDef(BaseModel):
    waveID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None

class WaveAggregatedStatusTypeDef(BaseModel):
    healthStatus: Optional[WaveHealthStatusType] = None
    lastUpdateDateTime: Optional[str] = None
    progressStatus: Optional[WaveProgressStatusType] = None
    replicationStartedDateTime: Optional[str] = None
    totalApplications: Optional[int] = None

class ApplicationTypeDef(BaseModel):
    applicationAggregatedStatus: Optional[ApplicationAggregatedStatusTypeDef] = None
    applicationID: Optional[str] = None
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    description: Optional[str] = None
    isArchived: Optional[bool] = None
    lastModifiedDateTime: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    waveID: Optional[str] = None

class ApplicationResponseTypeDef(BaseModel):
    applicationAggregatedStatus: ApplicationAggregatedStatusTypeDef
    applicationID: str
    arn: str
    creationDateTime: str
    description: str
    isArchived: bool
    lastModifiedDateTime: str
    name: str
    tags: Dict[str, str]
    waveID: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationTemplateResponseTypeDef(BaseModel):
    arn: str
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    replicationConfigurationTemplateID: str
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    tags: Dict[str, str]
    useDedicatedReplicationServer: bool
    useFipsEndpoint: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeServerLifeCycleStateRequestRequestTypeDef(BaseModel):
    lifeCycle: ChangeServerLifeCycleStateSourceServerLifecycleTypeDef
    sourceServerID: str
    accountID: Optional[str] = None

class ConnectorResponseTypeDef(BaseModel):
    arn: str
    connectorID: str
    name: str
    ssmCommandConfig: ConnectorSsmCommandConfigTypeDef
    ssmInstanceID: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorTypeDef(BaseModel):
    arn: Optional[str] = None
    connectorID: Optional[str] = None
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None
    ssmInstanceID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateConnectorRequestRequestTypeDef(BaseModel):
    name: str
    ssmInstanceID: str
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateConnectorRequestRequestTypeDef(BaseModel):
    connectorID: str
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None

class DataReplicationInitiationTypeDef(BaseModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStepTypeDef]] = None

class DescribeJobLogItemsRequestDescribeJobLogItemsPaginateTypeDef(BaseModel):
    jobID: str
    accountID: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchConfigurationTemplatesRequestDescribeLaunchConfigurationTemplatesPaginateTypeDef(BaseModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationConfigurationTemplatesRequestDescribeReplicationConfigurationTemplatesPaginateTypeDef(BaseModel):
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVcenterClientsRequestDescribeVcenterClientsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportErrorsRequestListExportErrorsPaginateTypeDef(BaseModel):
    exportID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportErrorsRequestListImportErrorsPaginateTypeDef(BaseModel):
    importID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedAccountsRequestListManagedAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestDescribeJobsPaginateTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestRequestTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeReplicationConfigurationTemplatesResponseTypeDef(BaseModel):
    items: List[ReplicationConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceServersRequestDescribeSourceServersPaginateTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceServersRequestRequestTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeVcenterClientsResponseTypeDef(BaseModel):
    items: List[VcenterClientTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTaskErrorTypeDef(BaseModel):
    errorData: Optional[ExportErrorDataTypeDef] = None
    errorDateTime: Optional[str] = None

class ExportTaskTypeDef(BaseModel):
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    exportID: Optional[str] = None
    progressPercentage: Optional[float] = None
    s3Bucket: Optional[str] = None
    s3BucketOwner: Optional[str] = None
    s3Key: Optional[str] = None
    status: Optional[ExportStatusType] = None
    summary: Optional[ExportTaskSummaryTypeDef] = None

class ImportTaskErrorTypeDef(BaseModel):
    errorData: Optional[ImportErrorDataTypeDef] = None
    errorDateTime: Optional[str] = None
    errorType: Optional[ImportErrorTypeType] = None

class ImportTaskSummaryTypeDef(BaseModel):
    applications: Optional[ImportTaskSummaryApplicationsTypeDef] = None
    servers: Optional[ImportTaskSummaryServersTypeDef] = None
    waves: Optional[ImportTaskSummaryWavesTypeDef] = None

class StartImportRequestRequestTypeDef(BaseModel):
    s3BucketSource: S3BucketSourceTypeDef
    clientToken: Optional[str] = None

class JobLogTypeDef(BaseModel):
    event: Optional[JobLogEventType] = None
    eventData: Optional[JobLogEventDataTypeDef] = None
    logDateTime: Optional[str] = None

class LifeCycleLastCutoverTypeDef(BaseModel):
    finalized: Optional[LifeCycleLastCutoverFinalizedTypeDef] = None
    initiated: Optional[LifeCycleLastCutoverInitiatedTypeDef] = None
    reverted: Optional[LifeCycleLastCutoverRevertedTypeDef] = None

class LifeCycleLastTestTypeDef(BaseModel):
    finalized: Optional[LifeCycleLastTestFinalizedTypeDef] = None
    initiated: Optional[LifeCycleLastTestInitiatedTypeDef] = None
    reverted: Optional[LifeCycleLastTestRevertedTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseModel):
    filters: Optional[ListConnectorsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorsRequestRequestTypeDef(BaseModel):
    filters: Optional[ListConnectorsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExportsRequestListExportsPaginateTypeDef(BaseModel):
    filters: Optional[ListExportsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportsRequestRequestTypeDef(BaseModel):
    filters: Optional[ListExportsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportsRequestListImportsPaginateTypeDef(BaseModel):
    filters: Optional[ListImportsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportsRequestRequestTypeDef(BaseModel):
    filters: Optional[ListImportsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListManagedAccountsResponseTypeDef(BaseModel):
    items: List[ManagedAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSourceServerActionsRequestListSourceServerActionsPaginateTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceServerActionsRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTemplateActionsRequestListTemplateActionsPaginateTypeDef(BaseModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateActionsRequestRequestTypeDef(BaseModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWavesRequestListWavesPaginateTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWavesRequestRequestTypeDef(BaseModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SourcePropertiesTypeDef(BaseModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[DiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None

class PutSourceServerActionRequestRequestTypeDef(BaseModel):
    actionID: str
    actionName: str
    documentIdentifier: str
    order: int
    sourceServerID: str
    accountID: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Mapping[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Mapping[str, Sequence[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class PutTemplateActionRequestRequestTypeDef(BaseModel):
    actionID: str
    actionName: str
    documentIdentifier: str
    launchConfigurationTemplateID: str
    order: int
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Mapping[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    operatingSystem: Optional[str] = None
    parameters: Optional[Mapping[str, Sequence[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class SourceServerActionDocumentResponseTypeDef(BaseModel):
    actionID: str
    actionName: str
    active: bool
    category: ActionCategoryType
    description: str
    documentIdentifier: str
    documentVersion: str
    externalParameters: Dict[str, SsmExternalParameterTypeDef]
    mustSucceedForCutover: bool
    order: int
    parameters: Dict[str, List[SsmParameterStoreParameterTypeDef]]
    timeoutSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class SourceServerActionDocumentTypeDef(BaseModel):
    actionID: Optional[str] = None
    actionName: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentIdentifier: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Dict[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    order: Optional[int] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class SsmDocumentPaginatorTypeDef(BaseModel):
    actionName: str
    ssmDocumentName: str
    externalParameters: Optional[Dict[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class SsmDocumentTypeDef(BaseModel):
    actionName: str
    ssmDocumentName: str
    externalParameters: Optional[Mapping[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Mapping[str, Sequence[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class TemplateActionDocumentResponseTypeDef(BaseModel):
    actionID: str
    actionName: str
    active: bool
    category: ActionCategoryType
    description: str
    documentIdentifier: str
    documentVersion: str
    externalParameters: Dict[str, SsmExternalParameterTypeDef]
    mustSucceedForCutover: bool
    operatingSystem: str
    order: int
    parameters: Dict[str, List[SsmParameterStoreParameterTypeDef]]
    timeoutSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class TemplateActionDocumentTypeDef(BaseModel):
    actionID: Optional[str] = None
    actionName: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentIdentifier: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Dict[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    operatingSystem: Optional[str] = None
    order: Optional[int] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class ReplicationConfigurationTypeDef(BaseModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    name: str
    replicatedDisks: List[ReplicationConfigurationReplicatedDiskTypeDef]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    sourceServerID: str
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    useFipsEndpoint: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[       ReplicationConfigurationDefaultLargeStagingDiskTypeType     ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    name: Optional[str] = None
    replicatedDisks: Optional[Sequence[ReplicationConfigurationReplicatedDiskTypeDef]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None

class UpdateSourceServerRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None
    connectorAction: Optional[SourceServerConnectorActionTypeDef] = None

class WaveResponseTypeDef(BaseModel):
    arn: str
    creationDateTime: str
    description: str
    isArchived: bool
    lastModifiedDateTime: str
    name: str
    tags: Dict[str, str]
    waveAggregatedStatus: WaveAggregatedStatusTypeDef
    waveID: str
    ResponseMetadata: ResponseMetadataTypeDef

class WaveTypeDef(BaseModel):
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    description: Optional[str] = None
    isArchived: Optional[bool] = None
    lastModifiedDateTime: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    waveAggregatedStatus: Optional[WaveAggregatedStatusTypeDef] = None
    waveID: Optional[str] = None

class ListApplicationsResponseTypeDef(BaseModel):
    items: List[ApplicationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponseTypeDef(BaseModel):
    items: List[ConnectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataReplicationInfoTypeDef(BaseModel):
    dataReplicationError: Optional[DataReplicationErrorTypeDef] = None
    dataReplicationInitiation: Optional[DataReplicationInitiationTypeDef] = None
    dataReplicationState: Optional[DataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    lastSnapshotDateTime: Optional[str] = None
    replicatedDisks: Optional[List[DataReplicationInfoReplicatedDiskTypeDef]] = None

class ListExportErrorsResponseTypeDef(BaseModel):
    items: List[ExportTaskErrorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExportsResponseTypeDef(BaseModel):
    items: List[ExportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExportResponseTypeDef(BaseModel):
    exportTask: ExportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportErrorsResponseTypeDef(BaseModel):
    items: List[ImportTaskErrorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTaskTypeDef(BaseModel):
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    importID: Optional[str] = None
    progressPercentage: Optional[float] = None
    s3BucketSource: Optional[S3BucketSourceTypeDef] = None
    status: Optional[ImportStatusType] = None
    summary: Optional[ImportTaskSummaryTypeDef] = None

class DescribeJobLogItemsResponseTypeDef(BaseModel):
    items: List[JobLogTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifeCycleTypeDef(BaseModel):
    addedToServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    firstByteDateTime: Optional[str] = None
    lastCutover: Optional[LifeCycleLastCutoverTypeDef] = None
    lastSeenByServiceDateTime: Optional[str] = None
    lastTest: Optional[LifeCycleLastTestTypeDef] = None
    state: Optional[LifeCycleStateType] = None

class ListSourceServerActionsResponseTypeDef(BaseModel):
    items: List[SourceServerActionDocumentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobPostLaunchActionsLaunchStatusPaginatorTypeDef(BaseModel):
    executionID: Optional[str] = None
    executionStatus: Optional[PostLaunchActionExecutionStatusType] = None
    failureReason: Optional[str] = None
    ssmDocument: Optional[SsmDocumentPaginatorTypeDef] = None
    ssmDocumentType: Optional[SsmDocumentTypeType] = None

class PostLaunchActionsPaginatorTypeDef(BaseModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[List[SsmDocumentPaginatorTypeDef]] = None

class JobPostLaunchActionsLaunchStatusTypeDef(BaseModel):
    executionID: Optional[str] = None
    executionStatus: Optional[PostLaunchActionExecutionStatusType] = None
    failureReason: Optional[str] = None
    ssmDocument: Optional[SsmDocumentTypeDef] = None
    ssmDocumentType: Optional[SsmDocumentTypeType] = None

class PostLaunchActionsTypeDef(BaseModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[Sequence[SsmDocumentTypeDef]] = None

class ListTemplateActionsResponseTypeDef(BaseModel):
    items: List[TemplateActionDocumentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWavesResponseTypeDef(BaseModel):
    items: List[WaveTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportsResponseTypeDef(BaseModel):
    items: List[ImportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportResponseTypeDef(BaseModel):
    importTask: ImportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SourceServerResponseTypeDef(BaseModel):
    applicationID: str
    arn: str
    connectorAction: SourceServerConnectorActionTypeDef
    dataReplicationInfo: DataReplicationInfoTypeDef
    fqdnForActionFramework: str
    isArchived: bool
    launchedInstance: LaunchedInstanceTypeDef
    lifeCycle: LifeCycleTypeDef
    replicationType: ReplicationTypeType
    sourceProperties: SourcePropertiesTypeDef
    sourceServerID: str
    tags: Dict[str, str]
    userProvidedID: str
    vcenterClientID: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourceServerTypeDef(BaseModel):
    applicationID: Optional[str] = None
    arn: Optional[str] = None
    connectorAction: Optional[SourceServerConnectorActionTypeDef] = None
    dataReplicationInfo: Optional[DataReplicationInfoTypeDef] = None
    fqdnForActionFramework: Optional[str] = None
    isArchived: Optional[bool] = None
    launchedInstance: Optional[LaunchedInstanceTypeDef] = None
    lifeCycle: Optional[LifeCycleTypeDef] = None
    replicationType: Optional[ReplicationTypeType] = None
    sourceProperties: Optional[SourcePropertiesTypeDef] = None
    sourceServerID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    userProvidedID: Optional[str] = None
    vcenterClientID: Optional[str] = None

class PostLaunchActionsStatusPaginatorTypeDef(BaseModel):
    postLaunchActionsLaunchStatusList: Optional[       List[JobPostLaunchActionsLaunchStatusPaginatorTypeDef]     ] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None

class LaunchConfigurationTemplatePaginatorTypeDef(BaseModel):
    launchConfigurationTemplateID: str
    arn: Optional[str] = None
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    ec2LaunchTemplateID: Optional[str] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[LicensingTypeDef] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsPaginatorTypeDef] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    smallVolumeMaxSize: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class PostLaunchActionsStatusTypeDef(BaseModel):
    postLaunchActionsLaunchStatusList: Optional[       List[JobPostLaunchActionsLaunchStatusTypeDef]     ] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None

class CreateLaunchConfigurationTemplateRequestRequestTypeDef(BaseModel):
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[LicensingTypeDef] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsTypeDef] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    smallVolumeMaxSize: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class LaunchConfigurationTemplateResponseTypeDef(BaseModel):
    arn: str
    associatePublicIpAddress: bool
    bootMode: BootModeType
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    enableMapAutoTagging: bool
    largeVolumeConf: LaunchTemplateDiskConfTypeDef
    launchConfigurationTemplateID: str
    launchDisposition: LaunchDispositionType
    licensing: LicensingTypeDef
    mapAutoTaggingMpeID: str
    postLaunchActions: PostLaunchActionsTypeDef
    smallVolumeConf: LaunchTemplateDiskConfTypeDef
    smallVolumeMaxSize: int
    tags: Dict[str, str]
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchConfigurationTemplateTypeDef(BaseModel):
    launchConfigurationTemplateID: str
    arn: Optional[str] = None
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    ec2LaunchTemplateID: Optional[str] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[LicensingTypeDef] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsTypeDef] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    smallVolumeMaxSize: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class LaunchConfigurationTypeDef(BaseModel):
    bootMode: BootModeType
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    enableMapAutoTagging: bool
    launchDisposition: LaunchDispositionType
    licensing: LicensingTypeDef
    mapAutoTaggingMpeID: str
    name: str
    postLaunchActions: PostLaunchActionsTypeDef
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    accountID: Optional[str] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[LicensingTypeDef] = None
    mapAutoTaggingMpeID: Optional[str] = None
    name: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsTypeDef] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class UpdateLaunchConfigurationTemplateRequestRequestTypeDef(BaseModel):
    launchConfigurationTemplateID: str
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[LicensingTypeDef] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsTypeDef] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    smallVolumeMaxSize: Optional[int] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class DescribeSourceServersResponseTypeDef(BaseModel):
    items: List[SourceServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipatingServerPaginatorTypeDef(BaseModel):
    sourceServerID: str
    launchStatus: Optional[LaunchStatusType] = None
    launchedEc2InstanceID: Optional[str] = None
    postLaunchActionsStatus: Optional[PostLaunchActionsStatusPaginatorTypeDef] = None

class DescribeLaunchConfigurationTemplatesResponsePaginatorTypeDef(BaseModel):
    items: List[LaunchConfigurationTemplatePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipatingServerTypeDef(BaseModel):
    sourceServerID: str
    launchStatus: Optional[LaunchStatusType] = None
    launchedEc2InstanceID: Optional[str] = None
    postLaunchActionsStatus: Optional[PostLaunchActionsStatusTypeDef] = None

class DescribeLaunchConfigurationTemplatesResponseTypeDef(BaseModel):
    items: List[LaunchConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobPaginatorTypeDef(BaseModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingServers: Optional[List[ParticipatingServerPaginatorTypeDef]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None

class JobTypeDef(BaseModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingServers: Optional[List[ParticipatingServerTypeDef]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None

class DescribeJobsResponsePaginatorTypeDef(BaseModel):
    items: List[JobPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobsResponseTypeDef(BaseModel):
    items: List[JobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCutoverResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTestResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateTargetInstancesResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

