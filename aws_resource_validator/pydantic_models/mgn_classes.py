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
from aws_resource_validator.pydantic_models.mgn_constants import *

class ApplicationAggregatedStatusTypeDef(BaseValidatorModel):
    healthStatus: Optional[ApplicationHealthStatusType] = None
    lastUpdateDateTime: Optional[str] = None
    progressStatus: Optional[ApplicationProgressStatusType] = None
    totalSourceServers: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ArchiveApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None

class ArchiveWaveRequestRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None

class AssociateApplicationsRequestRequestTypeDef(BaseValidatorModel):
    applicationIDs: Sequence[str]
    waveID: str
    accountID: Optional[str] = None

class AssociateSourceServersRequestRequestTypeDef(BaseValidatorModel):
    applicationID: str
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None

class CPUTypeDef(BaseValidatorModel):
    cores: Optional[int] = None
    modelName: Optional[str] = None

class ChangeServerLifeCycleStateSourceServerLifecycleTypeDef(BaseValidatorModel):
    state: ChangeServerLifeCycleStateSourceServerLifecycleStateType

class ConnectorSsmCommandConfigTypeDef(BaseValidatorModel):
    cloudWatchOutputEnabled: bool
    s3OutputEnabled: bool
    cloudWatchLogGroupName: Optional[str] = None
    outputS3BucketName: Optional[str] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class LaunchTemplateDiskConfTypeDef(BaseValidatorModel):
    iops: Optional[int] = None
    throughput: Optional[int] = None
    volumeType: Optional[VolumeTypeType] = None

class LicensingTypeDef(BaseValidatorModel):
    osByol: Optional[bool] = None

class CreateReplicationConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class CreateWaveRequestRequestTypeDef(BaseValidatorModel):
    name: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DataReplicationErrorTypeDef(BaseValidatorModel):
    error: Optional[DataReplicationErrorStringType] = None
    rawError: Optional[str] = None

class DataReplicationInfoReplicatedDiskTypeDef(BaseValidatorModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None

class DataReplicationInitiationStepTypeDef(BaseValidatorModel):
    name: Optional[DataReplicationInitiationStepNameType] = None
    status: Optional[DataReplicationInitiationStepStatusType] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None

class DeleteConnectorRequestRequestTypeDef(BaseValidatorModel):
    connectorID: str

class DeleteJobRequestRequestTypeDef(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None

class DeleteLaunchConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str

class DeleteReplicationConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateID: str

class DeleteSourceServerRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class DeleteVcenterClientRequestRequestTypeDef(BaseValidatorModel):
    vcenterClientID: str

class DeleteWaveRequestRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeJobLogItemsRequestRequestTypeDef(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeJobsRequestFiltersTypeDef(BaseValidatorModel):
    fromDate: Optional[str] = None
    jobIDs: Optional[Sequence[str]] = None
    toDate: Optional[str] = None

class DescribeLaunchConfigurationTemplatesRequestRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeReplicationConfigurationTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None

class ReplicationConfigurationTemplateTypeDef(BaseValidatorModel):
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

class DescribeSourceServersRequestFiltersTypeDef(BaseValidatorModel):
    applicationIDs: Optional[Sequence[str]] = None
    isArchived: Optional[bool] = None
    lifeCycleStates: Optional[Sequence[LifeCycleStateType]] = None
    replicationTypes: Optional[Sequence[ReplicationTypeType]] = None
    sourceServerIDs: Optional[Sequence[str]] = None

class DescribeVcenterClientsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class VcenterClientTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    datacenterName: Optional[str] = None
    hostname: Optional[str] = None
    lastSeenDatetime: Optional[str] = None
    sourceServerTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    vcenterClientID: Optional[str] = None
    vcenterUUID: Optional[str] = None

class DisassociateApplicationsRequestRequestTypeDef(BaseValidatorModel):
    applicationIDs: Sequence[str]
    waveID: str
    accountID: Optional[str] = None

class DisassociateSourceServersRequestRequestTypeDef(BaseValidatorModel):
    applicationID: str
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None

class DisconnectFromServiceRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class DiskTypeDef(BaseValidatorModel):
    bytes: Optional[int] = None
    deviceName: Optional[str] = None

class ExportErrorDataTypeDef(BaseValidatorModel):
    rawError: Optional[str] = None

class ExportTaskSummaryTypeDef(BaseValidatorModel):
    applicationsCount: Optional[int] = None
    serversCount: Optional[int] = None
    wavesCount: Optional[int] = None

class FinalizeCutoverRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class GetLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class GetReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class IdentificationHintsTypeDef(BaseValidatorModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmPath: Optional[str] = None
    vmWareUuid: Optional[str] = None

class ImportErrorDataTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    applicationID: Optional[str] = None
    ec2LaunchTemplateID: Optional[str] = None
    rawError: Optional[str] = None
    rowNumber: Optional[int] = None
    sourceServerID: Optional[str] = None
    waveID: Optional[str] = None

class ImportTaskSummaryApplicationsTypeDef(BaseValidatorModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None

class ImportTaskSummaryServersTypeDef(BaseValidatorModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None

class ImportTaskSummaryWavesTypeDef(BaseValidatorModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None

class S3BucketSourceTypeDef(BaseValidatorModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None

class JobLogEventDataTypeDef(BaseValidatorModel):
    conversionServerID: Optional[str] = None
    rawError: Optional[str] = None
    sourceServerID: Optional[str] = None
    targetInstanceID: Optional[str] = None

class LaunchedInstanceTypeDef(BaseValidatorModel):
    ec2InstanceID: Optional[str] = None
    firstBoot: Optional[FirstBootType] = None
    jobID: Optional[str] = None

class LifeCycleLastCutoverFinalizedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None

class LifeCycleLastCutoverInitiatedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None

class LifeCycleLastCutoverRevertedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None

class LifeCycleLastTestFinalizedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None

class LifeCycleLastTestInitiatedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None

class LifeCycleLastTestRevertedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None

class ListApplicationsRequestFiltersTypeDef(BaseValidatorModel):
    applicationIDs: Optional[Sequence[str]] = None
    isArchived: Optional[bool] = None
    waveIDs: Optional[Sequence[str]] = None

class ListConnectorsRequestFiltersTypeDef(BaseValidatorModel):
    connectorIDs: Optional[Sequence[str]] = None

class ListExportErrorsRequestRequestTypeDef(BaseValidatorModel):
    exportID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExportsRequestFiltersTypeDef(BaseValidatorModel):
    exportIDs: Optional[Sequence[str]] = None

class ListImportErrorsRequestRequestTypeDef(BaseValidatorModel):
    importID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportsRequestFiltersTypeDef(BaseValidatorModel):
    importIDs: Optional[Sequence[str]] = None

class ListManagedAccountsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ManagedAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class SourceServerActionsRequestFiltersTypeDef(BaseValidatorModel):
    actionIDs: Optional[Sequence[str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TemplateActionsRequestFiltersTypeDef(BaseValidatorModel):
    actionIDs: Optional[Sequence[str]] = None

class ListWavesRequestFiltersTypeDef(BaseValidatorModel):
    isArchived: Optional[bool] = None
    waveIDs: Optional[Sequence[str]] = None

class MarkAsArchivedRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class NetworkInterfaceTypeDef(BaseValidatorModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None

class OSTypeDef(BaseValidatorModel):
    fullString: Optional[str] = None

class PauseReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class SsmExternalParameterTypeDef(BaseValidatorModel):
    dynamicPath: Optional[str] = None

class SsmParameterStoreParameterTypeDef(BaseValidatorModel):
    parameterName: str
    parameterType: Literal["STRING"]

class RemoveSourceServerActionRequestRequestTypeDef(BaseValidatorModel):
    actionID: str
    sourceServerID: str
    accountID: Optional[str] = None

class RemoveTemplateActionRequestRequestTypeDef(BaseValidatorModel):
    actionID: str
    launchConfigurationTemplateID: str

class ReplicationConfigurationReplicatedDiskTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None

class ResumeReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class RetryDataReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class SourceServerConnectorActionTypeDef(BaseValidatorModel):
    connectorArn: Optional[str] = None
    credentialsSecretArn: Optional[str] = None

class StartCutoverRequestRequestTypeDef(BaseValidatorModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StartExportRequestRequestTypeDef(BaseValidatorModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None

class StartReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class StartTestRequestRequestTypeDef(BaseValidatorModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StopReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateTargetInstancesRequestRequestTypeDef(BaseValidatorModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UnarchiveApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None

class UnarchiveWaveRequestRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None

class UpdateReplicationConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSourceServerReplicationTypeRequestRequestTypeDef(BaseValidatorModel):
    replicationType: ReplicationTypeType
    sourceServerID: str
    accountID: Optional[str] = None

class UpdateWaveRequestRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None

class WaveAggregatedStatusTypeDef(BaseValidatorModel):
    healthStatus: Optional[WaveHealthStatusType] = None
    lastUpdateDateTime: Optional[str] = None
    progressStatus: Optional[WaveProgressStatusType] = None
    replicationStartedDateTime: Optional[str] = None
    totalApplications: Optional[int] = None

class ApplicationTypeDef(BaseValidatorModel):
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

class ApplicationResponseTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationTemplateResponseTypeDef(BaseValidatorModel):
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

class ChangeServerLifeCycleStateRequestRequestTypeDef(BaseValidatorModel):
    lifeCycle: ChangeServerLifeCycleStateSourceServerLifecycleTypeDef
    sourceServerID: str
    accountID: Optional[str] = None

class ConnectorResponseTypeDef(BaseValidatorModel):
    arn: str
    connectorID: str
    name: str
    ssmCommandConfig: ConnectorSsmCommandConfigTypeDef
    ssmInstanceID: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    connectorID: Optional[str] = None
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None
    ssmInstanceID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateConnectorRequestRequestTypeDef(BaseValidatorModel):
    name: str
    ssmInstanceID: str
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateConnectorRequestRequestTypeDef(BaseValidatorModel):
    connectorID: str
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None

class DataReplicationInitiationTypeDef(BaseValidatorModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStepTypeDef]] = None

class DescribeJobLogItemsRequestDescribeJobLogItemsPaginateTypeDef(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchConfigurationTemplatesRequestDescribeLaunchConfigurationTemplatesPaginateTypeDef(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationConfigurationTemplatesRequestDescribeReplicationConfigurationTemplatesPaginateTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVcenterClientsRequestDescribeVcenterClientsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportErrorsRequestListExportErrorsPaginateTypeDef(BaseValidatorModel):
    exportID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportErrorsRequestListImportErrorsPaginateTypeDef(BaseValidatorModel):
    importID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedAccountsRequestListManagedAccountsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestDescribeJobsPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeReplicationConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    items: List[ReplicationConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceServersRequestDescribeSourceServersPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceServersRequestRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeVcenterClientsResponseTypeDef(BaseValidatorModel):
    items: List[VcenterClientTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTaskErrorTypeDef(BaseValidatorModel):
    errorData: Optional[ExportErrorDataTypeDef] = None
    errorDateTime: Optional[str] = None

class ExportTaskTypeDef(BaseValidatorModel):
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    exportID: Optional[str] = None
    progressPercentage: Optional[float] = None
    s3Bucket: Optional[str] = None
    s3BucketOwner: Optional[str] = None
    s3Key: Optional[str] = None
    status: Optional[ExportStatusType] = None
    summary: Optional[ExportTaskSummaryTypeDef] = None

class ImportTaskErrorTypeDef(BaseValidatorModel):
    errorData: Optional[ImportErrorDataTypeDef] = None
    errorDateTime: Optional[str] = None
    errorType: Optional[ImportErrorTypeType] = None

class ImportTaskSummaryTypeDef(BaseValidatorModel):
    applications: Optional[ImportTaskSummaryApplicationsTypeDef] = None
    servers: Optional[ImportTaskSummaryServersTypeDef] = None
    waves: Optional[ImportTaskSummaryWavesTypeDef] = None

class StartImportRequestRequestTypeDef(BaseValidatorModel):
    s3BucketSource: S3BucketSourceTypeDef
    clientToken: Optional[str] = None

class JobLogTypeDef(BaseValidatorModel):
    event: Optional[JobLogEventType] = None
    eventData: Optional[JobLogEventDataTypeDef] = None
    logDateTime: Optional[str] = None

class LifeCycleLastCutoverTypeDef(BaseValidatorModel):
    finalized: Optional[LifeCycleLastCutoverFinalizedTypeDef] = None
    initiated: Optional[LifeCycleLastCutoverInitiatedTypeDef] = None
    reverted: Optional[LifeCycleLastCutoverRevertedTypeDef] = None

class LifeCycleLastTestTypeDef(BaseValidatorModel):
    finalized: Optional[LifeCycleLastTestFinalizedTypeDef] = None
    initiated: Optional[LifeCycleLastTestInitiatedTypeDef] = None
    reverted: Optional[LifeCycleLastTestRevertedTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[ListConnectorsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[ListConnectorsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExportsRequestListExportsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[ListExportsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[ListExportsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportsRequestListImportsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[ListImportsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[ListImportsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListManagedAccountsResponseTypeDef(BaseValidatorModel):
    items: List[ManagedAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSourceServerActionsRequestListSourceServerActionsPaginateTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceServerActionsRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTemplateActionsRequestListTemplateActionsPaginateTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateActionsRequestRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWavesRequestListWavesPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWavesRequestRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SourcePropertiesTypeDef(BaseValidatorModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[DiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None

class PutSourceServerActionRequestRequestTypeDef(BaseValidatorModel):
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

class PutTemplateActionRequestRequestTypeDef(BaseValidatorModel):
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

class SourceServerActionDocumentResponseTypeDef(BaseValidatorModel):
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

class SourceServerActionDocumentTypeDef(BaseValidatorModel):
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

class SsmDocumentPaginatorTypeDef(BaseValidatorModel):
    actionName: str
    ssmDocumentName: str
    externalParameters: Optional[Dict[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class SsmDocumentTypeDef(BaseValidatorModel):
    actionName: str
    ssmDocumentName: str
    externalParameters: Optional[Mapping[str, SsmExternalParameterTypeDef]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Mapping[str, Sequence[SsmParameterStoreParameterTypeDef]]] = None
    timeoutSeconds: Optional[int] = None

class TemplateActionDocumentResponseTypeDef(BaseValidatorModel):
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

class TemplateActionDocumentTypeDef(BaseValidatorModel):
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

class ReplicationConfigurationTypeDef(BaseValidatorModel):
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

class UpdateReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSourceServerRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    connectorAction: Optional[SourceServerConnectorActionTypeDef] = None

class WaveResponseTypeDef(BaseValidatorModel):
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

class WaveTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    description: Optional[str] = None
    isArchived: Optional[bool] = None
    lastModifiedDateTime: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    waveAggregatedStatus: Optional[WaveAggregatedStatusTypeDef] = None
    waveID: Optional[str] = None

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    items: List[ApplicationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponseTypeDef(BaseValidatorModel):
    items: List[ConnectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataReplicationInfoTypeDef(BaseValidatorModel):
    dataReplicationError: Optional[DataReplicationErrorTypeDef] = None
    dataReplicationInitiation: Optional[DataReplicationInitiationTypeDef] = None
    dataReplicationState: Optional[DataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    lastSnapshotDateTime: Optional[str] = None
    replicatedDisks: Optional[List[DataReplicationInfoReplicatedDiskTypeDef]] = None

class ListExportErrorsResponseTypeDef(BaseValidatorModel):
    items: List[ExportTaskErrorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExportsResponseTypeDef(BaseValidatorModel):
    items: List[ExportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExportResponseTypeDef(BaseValidatorModel):
    exportTask: ExportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportErrorsResponseTypeDef(BaseValidatorModel):
    items: List[ImportTaskErrorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTaskTypeDef(BaseValidatorModel):
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    importID: Optional[str] = None
    progressPercentage: Optional[float] = None
    s3BucketSource: Optional[S3BucketSourceTypeDef] = None
    status: Optional[ImportStatusType] = None
    summary: Optional[ImportTaskSummaryTypeDef] = None

class DescribeJobLogItemsResponseTypeDef(BaseValidatorModel):
    items: List[JobLogTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifeCycleTypeDef(BaseValidatorModel):
    addedToServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    firstByteDateTime: Optional[str] = None
    lastCutover: Optional[LifeCycleLastCutoverTypeDef] = None
    lastSeenByServiceDateTime: Optional[str] = None
    lastTest: Optional[LifeCycleLastTestTypeDef] = None
    state: Optional[LifeCycleStateType] = None

class ListSourceServerActionsResponseTypeDef(BaseValidatorModel):
    items: List[SourceServerActionDocumentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobPostLaunchActionsLaunchStatusPaginatorTypeDef(BaseValidatorModel):
    executionID: Optional[str] = None
    executionStatus: Optional[PostLaunchActionExecutionStatusType] = None
    failureReason: Optional[str] = None
    ssmDocument: Optional[SsmDocumentPaginatorTypeDef] = None
    ssmDocumentType: Optional[SsmDocumentTypeType] = None

class PostLaunchActionsPaginatorTypeDef(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[List[SsmDocumentPaginatorTypeDef]] = None

class JobPostLaunchActionsLaunchStatusTypeDef(BaseValidatorModel):
    executionID: Optional[str] = None
    executionStatus: Optional[PostLaunchActionExecutionStatusType] = None
    failureReason: Optional[str] = None
    ssmDocument: Optional[SsmDocumentTypeDef] = None
    ssmDocumentType: Optional[SsmDocumentTypeType] = None

class PostLaunchActionsTypeDef(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[Sequence[SsmDocumentTypeDef]] = None

class ListTemplateActionsResponseTypeDef(BaseValidatorModel):
    items: List[TemplateActionDocumentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWavesResponseTypeDef(BaseValidatorModel):
    items: List[WaveTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportsResponseTypeDef(BaseValidatorModel):
    items: List[ImportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportResponseTypeDef(BaseValidatorModel):
    importTask: ImportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SourceServerResponseTypeDef(BaseValidatorModel):
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

class SourceServerTypeDef(BaseValidatorModel):
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

class PostLaunchActionsStatusPaginatorTypeDef(BaseValidatorModel):
    postLaunchActionsLaunchStatusList: Optional[       List[JobPostLaunchActionsLaunchStatusPaginatorTypeDef]     ] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None

class LaunchConfigurationTemplatePaginatorTypeDef(BaseValidatorModel):
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

class PostLaunchActionsStatusTypeDef(BaseValidatorModel):
    postLaunchActionsLaunchStatusList: Optional[       List[JobPostLaunchActionsLaunchStatusTypeDef]     ] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None

class CreateLaunchConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class LaunchConfigurationTemplateResponseTypeDef(BaseValidatorModel):
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

class LaunchConfigurationTemplateTypeDef(BaseValidatorModel):
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

class LaunchConfigurationTypeDef(BaseValidatorModel):
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

class UpdateLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateLaunchConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeSourceServersResponseTypeDef(BaseValidatorModel):
    items: List[SourceServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipatingServerPaginatorTypeDef(BaseValidatorModel):
    sourceServerID: str
    launchStatus: Optional[LaunchStatusType] = None
    launchedEc2InstanceID: Optional[str] = None
    postLaunchActionsStatus: Optional[PostLaunchActionsStatusPaginatorTypeDef] = None

class DescribeLaunchConfigurationTemplatesResponsePaginatorTypeDef(BaseValidatorModel):
    items: List[LaunchConfigurationTemplatePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipatingServerTypeDef(BaseValidatorModel):
    sourceServerID: str
    launchStatus: Optional[LaunchStatusType] = None
    launchedEc2InstanceID: Optional[str] = None
    postLaunchActionsStatus: Optional[PostLaunchActionsStatusTypeDef] = None

class DescribeLaunchConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    items: List[LaunchConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobPaginatorTypeDef(BaseValidatorModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingServers: Optional[List[ParticipatingServerPaginatorTypeDef]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None

class JobTypeDef(BaseValidatorModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingServers: Optional[List[ParticipatingServerTypeDef]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None

class DescribeJobsResponsePaginatorTypeDef(BaseValidatorModel):
    items: List[JobPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobsResponseTypeDef(BaseValidatorModel):
    items: List[JobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCutoverResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTestResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateTargetInstancesResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

