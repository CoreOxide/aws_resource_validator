from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mgn.mgn_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplicationAggregatedStatus(BaseValidatorModel):
    healthStatus: Optional[ApplicationHealthStatusType] = None
    lastUpdateDateTime: Optional[str] = None
    progressStatus: Optional[ApplicationProgressStatusType] = None
    totalSourceServers: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'archive_application' function.
class ArchiveApplicationRequest(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None


# This class is the input for the 'archive_wave' function.
class ArchiveWaveRequest(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None


class AssociateApplicationsRequest(BaseValidatorModel):
    applicationIDs: List[str]
    waveID: str
    accountID: Optional[str] = None


class AssociateSourceServersRequest(BaseValidatorModel):
    applicationID: str
    sourceServerIDs: List[str]
    accountID: Optional[str] = None


class CPU(BaseValidatorModel):
    cores: Optional[int] = None
    modelName: Optional[str] = None


class ChangeServerLifeCycleStateSourceServerLifecycle(BaseValidatorModel):
    state: ChangeServerLifeCycleStateSourceServerLifecycleStateType


class ConnectorSsmCommandConfig(BaseValidatorModel):
    cloudWatchOutputEnabled: bool
    s3OutputEnabled: bool
    cloudWatchLogGroupName: Optional[str] = None
    outputS3BucketName: Optional[str] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    name: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class LaunchTemplateDiskConf(BaseValidatorModel):
    iops: Optional[int] = None
    throughput: Optional[int] = None
    volumeType: Optional[VolumeTypeType] = None


class Licensing(BaseValidatorModel):
    osByol: Optional[bool] = None


# This class is the input for the 'create_replication_configuration_template' function.
class CreateReplicationConfigurationTemplateRequest(BaseValidatorModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ebsEncryptionKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    useFipsEndpoint: Optional[bool] = None


# This class is the input for the 'create_wave' function.
class CreateWaveRequest(BaseValidatorModel):
    name: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DataReplicationError(BaseValidatorModel):
    error: Optional[DataReplicationErrorStringType] = None
    rawError: Optional[str] = None


class DataReplicationInfoReplicatedDisk(BaseValidatorModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None


class DataReplicationInitiationStep(BaseValidatorModel):
    name: Optional[DataReplicationInitiationStepNameType] = None
    status: Optional[DataReplicationInitiationStepStatusType] = None


class DeleteApplicationRequest(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None


# This class is the input for the 'delete_connector' function.
class DeleteConnectorRequest(BaseValidatorModel):
    connectorID: str


class DeleteJobRequest(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None


class DeleteLaunchConfigurationTemplateRequest(BaseValidatorModel):
    launchConfigurationTemplateID: str


class DeleteReplicationConfigurationTemplateRequest(BaseValidatorModel):
    replicationConfigurationTemplateID: str


class DeleteSourceServerRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'delete_vcenter_client' function.
class DeleteVcenterClientRequest(BaseValidatorModel):
    vcenterClientID: str


class DeleteWaveRequest(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_job_log_items' function.
class DescribeJobLogItemsRequest(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeJobsRequestFilters(BaseValidatorModel):
    fromDate: Optional[str] = None
    jobIDs: Optional[List[str]] = None
    toDate: Optional[str] = None


# This class is the input for the 'describe_launch_configuration_templates' function.
class DescribeLaunchConfigurationTemplatesRequest(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_replication_configuration_templates' function.
class DescribeReplicationConfigurationTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[List[str]] = None


class ReplicationConfigurationTemplate(BaseValidatorModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ReplicationConfigurationDefaultLargeStagingDiskTypeType] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None


class DescribeSourceServersRequestFilters(BaseValidatorModel):
    applicationIDs: Optional[List[str]] = None
    isArchived: Optional[bool] = None
    lifeCycleStates: Optional[List[LifeCycleStateType]] = None
    replicationTypes: Optional[List[ReplicationTypeType]] = None
    sourceServerIDs: Optional[List[str]] = None


# This class is the input for the 'describe_vcenter_clients' function.
class DescribeVcenterClientsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class VcenterClient(BaseValidatorModel):
    arn: Optional[str] = None
    datacenterName: Optional[str] = None
    hostname: Optional[str] = None
    lastSeenDatetime: Optional[str] = None
    sourceServerTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    vcenterClientID: Optional[str] = None
    vcenterUUID: Optional[str] = None


class DisassociateApplicationsRequest(BaseValidatorModel):
    applicationIDs: List[str]
    waveID: str
    accountID: Optional[str] = None


class DisassociateSourceServersRequest(BaseValidatorModel):
    applicationID: str
    sourceServerIDs: List[str]
    accountID: Optional[str] = None


# This class is the input for the 'disconnect_from_service' function.
class DisconnectFromServiceRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class Disk(BaseValidatorModel):
    bytes: Optional[int] = None
    deviceName: Optional[str] = None


class ExportErrorData(BaseValidatorModel):
    rawError: Optional[str] = None


class ExportTaskSummary(BaseValidatorModel):
    applicationsCount: Optional[int] = None
    serversCount: Optional[int] = None
    wavesCount: Optional[int] = None


# This class is the input for the 'finalize_cutover' function.
class FinalizeCutoverRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'get_launch_configuration' function.
class GetLaunchConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'get_replication_configuration' function.
class GetReplicationConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class IdentificationHints(BaseValidatorModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmPath: Optional[str] = None
    vmWareUuid: Optional[str] = None


class ImportErrorData(BaseValidatorModel):
    accountID: Optional[str] = None
    applicationID: Optional[str] = None
    ec2LaunchTemplateID: Optional[str] = None
    rawError: Optional[str] = None
    rowNumber: Optional[int] = None
    sourceServerID: Optional[str] = None
    waveID: Optional[str] = None


class ImportTaskSummaryApplications(BaseValidatorModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None


class ImportTaskSummaryServers(BaseValidatorModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None


class ImportTaskSummaryWaves(BaseValidatorModel):
    createdCount: Optional[int] = None
    modifiedCount: Optional[int] = None


class S3BucketSource(BaseValidatorModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None


class JobLogEventData(BaseValidatorModel):
    conversionServerID: Optional[str] = None
    rawError: Optional[str] = None
    sourceServerID: Optional[str] = None
    targetInstanceID: Optional[str] = None


class LaunchedInstance(BaseValidatorModel):
    ec2InstanceID: Optional[str] = None
    firstBoot: Optional[FirstBootType] = None
    jobID: Optional[str] = None


class LifeCycleLastCutoverFinalized(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None


class LifeCycleLastCutoverInitiated(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None


class LifeCycleLastCutoverReverted(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None


class LifeCycleLastTestFinalized(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None


class LifeCycleLastTestInitiated(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None


class LifeCycleLastTestReverted(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None


class ListApplicationsRequestFilters(BaseValidatorModel):
    applicationIDs: Optional[List[str]] = None
    isArchived: Optional[bool] = None
    waveIDs: Optional[List[str]] = None


class ListConnectorsRequestFilters(BaseValidatorModel):
    connectorIDs: Optional[List[str]] = None


# This class is the input for the 'list_export_errors' function.
class ListExportErrorsRequest(BaseValidatorModel):
    exportID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExportsRequestFilters(BaseValidatorModel):
    exportIDs: Optional[List[str]] = None


# This class is the input for the 'list_import_errors' function.
class ListImportErrorsRequest(BaseValidatorModel):
    importID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportsRequestFilters(BaseValidatorModel):
    importIDs: Optional[List[str]] = None


# This class is the input for the 'list_managed_accounts' function.
class ListManagedAccountsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedAccount(BaseValidatorModel):
    accountId: Optional[str] = None


class SourceServerActionsRequestFilters(BaseValidatorModel):
    actionIDs: Optional[List[str]] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TemplateActionsRequestFilters(BaseValidatorModel):
    actionIDs: Optional[List[str]] = None


class ListWavesRequestFilters(BaseValidatorModel):
    isArchived: Optional[bool] = None
    waveIDs: Optional[List[str]] = None


# This class is the input for the 'mark_as_archived' function.
class MarkAsArchivedRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None


class OS(BaseValidatorModel):
    fullString: Optional[str] = None


# This class is the input for the 'pause_replication' function.
class PauseReplicationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class SsmExternalParameter(BaseValidatorModel):
    dynamicPath: Optional[str] = None


class SsmParameterStoreParameter(BaseValidatorModel):
    parameterName: str
    parameterType: Literal['STRING']


class RemoveSourceServerActionRequest(BaseValidatorModel):
    actionID: str
    sourceServerID: str
    accountID: Optional[str] = None


class RemoveTemplateActionRequest(BaseValidatorModel):
    actionID: str
    launchConfigurationTemplateID: str


class ReplicationConfigurationReplicatedDisk(BaseValidatorModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None


# This class is the input for the 'resume_replication' function.
class ResumeReplicationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'retry_data_replication' function.
class RetryDataReplicationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class SourceServerConnectorAction(BaseValidatorModel):
    connectorArn: Optional[str] = None
    credentialsSecretArn: Optional[str] = None


# This class is the input for the 'start_cutover' function.
class StartCutoverRequest(BaseValidatorModel):
    sourceServerIDs: List[str]
    accountID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'start_export' function.
class StartExportRequest(BaseValidatorModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None


# This class is the input for the 'start_replication' function.
class StartReplicationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'start_test' function.
class StartTestRequest(BaseValidatorModel):
    sourceServerIDs: List[str]
    accountID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'stop_replication' function.
class StopReplicationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'terminate_target_instances' function.
class TerminateTargetInstancesRequest(BaseValidatorModel):
    sourceServerIDs: List[str]
    accountID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'unarchive_application' function.
class UnarchiveApplicationRequest(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None


# This class is the input for the 'unarchive_wave' function.
class UnarchiveWaveRequest(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_application' function.
class UpdateApplicationRequest(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None


# This class is the input for the 'update_replication_configuration_template' function.
class UpdateReplicationConfigurationTemplateRequest(BaseValidatorModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ReplicationConfigurationDefaultLargeStagingDiskTypeType] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None


# This class is the input for the 'update_source_server_replication_type' function.
class UpdateSourceServerReplicationTypeRequest(BaseValidatorModel):
    replicationType: ReplicationTypeType
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the input for the 'update_wave' function.
class UpdateWaveRequest(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None


class WaveAggregatedStatus(BaseValidatorModel):
    healthStatus: Optional[WaveHealthStatusType] = None
    lastUpdateDateTime: Optional[str] = None
    progressStatus: Optional[WaveProgressStatusType] = None
    replicationStartedDateTime: Optional[str] = None
    totalApplications: Optional[int] = None


class Application(BaseValidatorModel):
    applicationAggregatedStatus: Optional[ApplicationAggregatedStatus] = None
    applicationID: Optional[str] = None
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    description: Optional[str] = None
    isArchived: Optional[bool] = None
    lastModifiedDateTime: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    waveID: Optional[str] = None


# This class is the output for the 'update_application' function.
class ApplicationResponse(BaseValidatorModel):
    applicationAggregatedStatus: ApplicationAggregatedStatus
    applicationID: str
    arn: str
    creationDateTime: str
    description: str
    isArchived: bool
    lastModifiedDateTime: str
    name: str
    tags: Dict[str, str]
    waveID: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_replication_configuration_template' function.
class ReplicationConfigurationTemplateResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'change_server_life_cycle_state' function.
class ChangeServerLifeCycleStateRequest(BaseValidatorModel):
    lifeCycle: ChangeServerLifeCycleStateSourceServerLifecycle
    sourceServerID: str
    accountID: Optional[str] = None


# This class is the output for the 'update_connector' function.
class ConnectorResponse(BaseValidatorModel):
    arn: str
    connectorID: str
    name: str
    ssmCommandConfig: ConnectorSsmCommandConfig
    ssmInstanceID: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Connector(BaseValidatorModel):
    arn: Optional[str] = None
    connectorID: Optional[str] = None
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfig] = None
    ssmInstanceID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_connector' function.
class CreateConnectorRequest(BaseValidatorModel):
    name: str
    ssmInstanceID: str
    ssmCommandConfig: Optional[ConnectorSsmCommandConfig] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_connector' function.
class UpdateConnectorRequest(BaseValidatorModel):
    connectorID: str
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfig] = None


class DataReplicationInitiation(BaseValidatorModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStep]] = None


class DescribeJobLogItemsRequestPaginate(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLaunchConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    replicationConfigurationTemplateIDs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeVcenterClientsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExportErrorsRequestPaginate(BaseValidatorModel):
    exportID: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportErrorsRequestPaginate(BaseValidatorModel):
    importID: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeJobsRequestPaginate(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_jobs' function.
class DescribeJobsRequest(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'describe_replication_configuration_templates' function.
class DescribeReplicationConfigurationTemplatesResponse(BaseValidatorModel):
    items: List[ReplicationConfigurationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeSourceServersRequestPaginate(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_source_servers' function.
class DescribeSourceServersRequest(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'describe_vcenter_clients' function.
class DescribeVcenterClientsResponse(BaseValidatorModel):
    items: List[VcenterClient]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExportTaskError(BaseValidatorModel):
    errorData: Optional[ExportErrorData] = None
    errorDateTime: Optional[str] = None


class ExportTask(BaseValidatorModel):
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    exportID: Optional[str] = None
    progressPercentage: Optional[float] = None
    s3Bucket: Optional[str] = None
    s3BucketOwner: Optional[str] = None
    s3Key: Optional[str] = None
    status: Optional[ExportStatusType] = None
    summary: Optional[ExportTaskSummary] = None


class ImportTaskError(BaseValidatorModel):
    errorData: Optional[ImportErrorData] = None
    errorDateTime: Optional[str] = None
    errorType: Optional[ImportErrorTypeType] = None


class ImportTaskSummary(BaseValidatorModel):
    applications: Optional[ImportTaskSummaryApplications] = None
    servers: Optional[ImportTaskSummaryServers] = None
    waves: Optional[ImportTaskSummaryWaves] = None


# This class is the input for the 'start_import' function.
class StartImportRequest(BaseValidatorModel):
    s3BucketSource: S3BucketSource
    clientToken: Optional[str] = None


class JobLog(BaseValidatorModel):
    event: Optional[JobLogEventType] = None
    eventData: Optional[JobLogEventData] = None
    logDateTime: Optional[str] = None


class LifeCycleLastCutover(BaseValidatorModel):
    finalized: Optional[LifeCycleLastCutoverFinalized] = None
    initiated: Optional[LifeCycleLastCutoverInitiated] = None
    reverted: Optional[LifeCycleLastCutoverReverted] = None


class LifeCycleLastTest(BaseValidatorModel):
    finalized: Optional[LifeCycleLastTestFinalized] = None
    initiated: Optional[LifeCycleLastTestInitiated] = None
    reverted: Optional[LifeCycleLastTestReverted] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListConnectorsRequestPaginate(BaseValidatorModel):
    filters: Optional[ListConnectorsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_connectors' function.
class ListConnectorsRequest(BaseValidatorModel):
    filters: Optional[ListConnectorsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExportsRequestPaginate(BaseValidatorModel):
    filters: Optional[ListExportsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_exports' function.
class ListExportsRequest(BaseValidatorModel):
    filters: Optional[ListExportsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportsRequestPaginate(BaseValidatorModel):
    filters: Optional[ListImportsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_imports' function.
class ListImportsRequest(BaseValidatorModel):
    filters: Optional[ListImportsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_managed_accounts' function.
class ListManagedAccountsResponse(BaseValidatorModel):
    items: List[ManagedAccount]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSourceServerActionsRequestPaginate(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_source_server_actions' function.
class ListSourceServerActionsRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTemplateActionsRequestPaginate(BaseValidatorModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_template_actions' function.
class ListTemplateActionsRequest(BaseValidatorModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWavesRequestPaginate(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_waves' function.
class ListWavesRequest(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SourceProperties(BaseValidatorModel):
    cpus: Optional[List[CPU]] = None
    disks: Optional[List[Disk]] = None
    identificationHints: Optional[IdentificationHints] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None
    os: Optional[OS] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None


# This class is the input for the 'put_source_server_action' function.
class PutSourceServerActionRequest(BaseValidatorModel):
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
    externalParameters: Optional[Dict[str, SsmExternalParameter]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameter]]] = None
    timeoutSeconds: Optional[int] = None


# This class is the input for the 'put_template_action' function.
class PutTemplateActionRequest(BaseValidatorModel):
    actionID: str
    actionName: str
    documentIdentifier: str
    launchConfigurationTemplateID: str
    order: int
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Dict[str, SsmExternalParameter]] = None
    mustSucceedForCutover: Optional[bool] = None
    operatingSystem: Optional[str] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameter]]] = None
    timeoutSeconds: Optional[int] = None


# This class is the output for the 'put_source_server_action' function.
class SourceServerActionDocumentResponse(BaseValidatorModel):
    actionID: str
    actionName: str
    active: bool
    category: ActionCategoryType
    description: str
    documentIdentifier: str
    documentVersion: str
    externalParameters: Dict[str, SsmExternalParameter]
    mustSucceedForCutover: bool
    order: int
    parameters: Dict[str, List[SsmParameterStoreParameter]]
    timeoutSeconds: int
    ResponseMetadata: ResponseMetadata


class SourceServerActionDocument(BaseValidatorModel):
    actionID: Optional[str] = None
    actionName: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentIdentifier: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Dict[str, SsmExternalParameter]] = None
    mustSucceedForCutover: Optional[bool] = None
    order: Optional[int] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameter]]] = None
    timeoutSeconds: Optional[int] = None


class SsmDocumentOutput(BaseValidatorModel):
    actionName: str
    ssmDocumentName: str
    externalParameters: Optional[Dict[str, SsmExternalParameter]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameter]]] = None
    timeoutSeconds: Optional[int] = None


class SsmDocument(BaseValidatorModel):
    actionName: str
    ssmDocumentName: str
    externalParameters: Optional[Dict[str, SsmExternalParameter]] = None
    mustSucceedForCutover: Optional[bool] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameter]]] = None
    timeoutSeconds: Optional[int] = None


# This class is the output for the 'put_template_action' function.
class TemplateActionDocumentResponse(BaseValidatorModel):
    actionID: str
    actionName: str
    active: bool
    category: ActionCategoryType
    description: str
    documentIdentifier: str
    documentVersion: str
    externalParameters: Dict[str, SsmExternalParameter]
    mustSucceedForCutover: bool
    operatingSystem: str
    order: int
    parameters: Dict[str, List[SsmParameterStoreParameter]]
    timeoutSeconds: int
    ResponseMetadata: ResponseMetadata


class TemplateActionDocument(BaseValidatorModel):
    actionID: Optional[str] = None
    actionName: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[ActionCategoryType] = None
    description: Optional[str] = None
    documentIdentifier: Optional[str] = None
    documentVersion: Optional[str] = None
    externalParameters: Optional[Dict[str, SsmExternalParameter]] = None
    mustSucceedForCutover: Optional[bool] = None
    operatingSystem: Optional[str] = None
    order: Optional[int] = None
    parameters: Optional[Dict[str, List[SsmParameterStoreParameter]]] = None
    timeoutSeconds: Optional[int] = None


# This class is the output for the 'update_replication_configuration' function.
class ReplicationConfiguration(BaseValidatorModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    name: str
    replicatedDisks: List[ReplicationConfigurationReplicatedDisk]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    sourceServerID: str
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    useFipsEndpoint: bool
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_replication_configuration' function.
class UpdateReplicationConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ReplicationConfigurationDefaultLargeStagingDiskTypeType] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    name: Optional[str] = None
    replicatedDisks: Optional[List[ReplicationConfigurationReplicatedDisk]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None


# This class is the input for the 'update_source_server' function.
class UpdateSourceServerRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    connectorAction: Optional[SourceServerConnectorAction] = None


# This class is the output for the 'update_wave' function.
class WaveResponse(BaseValidatorModel):
    arn: str
    creationDateTime: str
    description: str
    isArchived: bool
    lastModifiedDateTime: str
    name: str
    tags: Dict[str, str]
    waveAggregatedStatus: WaveAggregatedStatus
    waveID: str
    ResponseMetadata: ResponseMetadata


class Wave(BaseValidatorModel):
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    description: Optional[str] = None
    isArchived: Optional[bool] = None
    lastModifiedDateTime: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    waveAggregatedStatus: Optional[WaveAggregatedStatus] = None
    waveID: Optional[str] = None


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    items: List[Application]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_connectors' function.
class ListConnectorsResponse(BaseValidatorModel):
    items: List[Connector]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataReplicationInfo(BaseValidatorModel):
    dataReplicationError: Optional[DataReplicationError] = None
    dataReplicationInitiation: Optional[DataReplicationInitiation] = None
    dataReplicationState: Optional[DataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    lastSnapshotDateTime: Optional[str] = None
    replicatedDisks: Optional[List[DataReplicationInfoReplicatedDisk]] = None


# This class is the output for the 'list_export_errors' function.
class ListExportErrorsResponse(BaseValidatorModel):
    items: List[ExportTaskError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_exports' function.
class ListExportsResponse(BaseValidatorModel):
    items: List[ExportTask]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_export' function.
class StartExportResponse(BaseValidatorModel):
    exportTask: ExportTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_import_errors' function.
class ListImportErrorsResponse(BaseValidatorModel):
    items: List[ImportTaskError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImportTask(BaseValidatorModel):
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    importID: Optional[str] = None
    progressPercentage: Optional[float] = None
    s3BucketSource: Optional[S3BucketSource] = None
    status: Optional[ImportStatusType] = None
    summary: Optional[ImportTaskSummary] = None


# This class is the output for the 'describe_job_log_items' function.
class DescribeJobLogItemsResponse(BaseValidatorModel):
    items: List[JobLog]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LifeCycle(BaseValidatorModel):
    addedToServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    firstByteDateTime: Optional[str] = None
    lastCutover: Optional[LifeCycleLastCutover] = None
    lastSeenByServiceDateTime: Optional[str] = None
    lastTest: Optional[LifeCycleLastTest] = None
    state: Optional[LifeCycleStateType] = None


# This class is the output for the 'list_source_server_actions' function.
class ListSourceServerActionsResponse(BaseValidatorModel):
    items: List[SourceServerActionDocument]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobPostLaunchActionsLaunchStatus(BaseValidatorModel):
    executionID: Optional[str] = None
    executionStatus: Optional[PostLaunchActionExecutionStatusType] = None
    failureReason: Optional[str] = None
    ssmDocument: Optional[SsmDocumentOutput] = None
    ssmDocumentType: Optional[SsmDocumentTypeType] = None


class PostLaunchActionsOutput(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[List[SsmDocumentOutput]] = None


class PostLaunchActions(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[List[SsmDocument]] = None


# This class is the output for the 'list_template_actions' function.
class ListTemplateActionsResponse(BaseValidatorModel):
    items: List[TemplateActionDocument]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_waves' function.
class ListWavesResponse(BaseValidatorModel):
    items: List[Wave]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_imports' function.
class ListImportsResponse(BaseValidatorModel):
    items: List[ImportTask]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_import' function.
class StartImportResponse(BaseValidatorModel):
    importTask: ImportTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_source_server_replication_type' function.
class SourceServerResponse(BaseValidatorModel):
    applicationID: str
    arn: str
    connectorAction: SourceServerConnectorAction
    dataReplicationInfo: DataReplicationInfo
    fqdnForActionFramework: str
    isArchived: bool
    launchedInstance: LaunchedInstance
    lifeCycle: LifeCycle
    replicationType: ReplicationTypeType
    sourceProperties: SourceProperties
    sourceServerID: str
    tags: Dict[str, str]
    userProvidedID: str
    vcenterClientID: str
    ResponseMetadata: ResponseMetadata


class SourceServer(BaseValidatorModel):
    applicationID: Optional[str] = None
    arn: Optional[str] = None
    connectorAction: Optional[SourceServerConnectorAction] = None
    dataReplicationInfo: Optional[DataReplicationInfo] = None
    fqdnForActionFramework: Optional[str] = None
    isArchived: Optional[bool] = None
    launchedInstance: Optional[LaunchedInstance] = None
    lifeCycle: Optional[LifeCycle] = None
    replicationType: Optional[ReplicationTypeType] = None
    sourceProperties: Optional[SourceProperties] = None
    sourceServerID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    userProvidedID: Optional[str] = None
    vcenterClientID: Optional[str] = None


class PostLaunchActionsStatus(BaseValidatorModel):
    postLaunchActionsLaunchStatusList: Optional[List[JobPostLaunchActionsLaunchStatus]] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None


# This class is the output for the 'update_launch_configuration_template' function.
class LaunchConfigurationTemplateResponse(BaseValidatorModel):
    arn: str
    associatePublicIpAddress: bool
    bootMode: BootModeType
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    enableMapAutoTagging: bool
    largeVolumeConf: LaunchTemplateDiskConf
    launchConfigurationTemplateID: str
    launchDisposition: LaunchDispositionType
    licensing: Licensing
    mapAutoTaggingMpeID: str
    postLaunchActions: PostLaunchActionsOutput
    smallVolumeConf: LaunchTemplateDiskConf
    smallVolumeMaxSize: int
    tags: Dict[str, str]
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadata


class LaunchConfigurationTemplate(BaseValidatorModel):
    launchConfigurationTemplateID: str
    arn: Optional[str] = None
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    ec2LaunchTemplateID: Optional[str] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConf] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[Licensing] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsOutput] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConf] = None
    smallVolumeMaxSize: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


# This class is the output for the 'update_launch_configuration' function.
class LaunchConfiguration(BaseValidatorModel):
    bootMode: BootModeType
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    enableMapAutoTagging: bool
    launchDisposition: LaunchDispositionType
    licensing: Licensing
    mapAutoTaggingMpeID: str
    name: str
    postLaunchActions: PostLaunchActionsOutput
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadata

PostLaunchActionsUnion = Union[PostLaunchActions, PostLaunchActionsOutput]


# This class is the output for the 'describe_source_servers' function.
class DescribeSourceServersResponse(BaseValidatorModel):
    items: List[SourceServer]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParticipatingServer(BaseValidatorModel):
    sourceServerID: str
    launchStatus: Optional[LaunchStatusType] = None
    launchedEc2InstanceID: Optional[str] = None
    postLaunchActionsStatus: Optional[PostLaunchActionsStatus] = None


# This class is the output for the 'describe_launch_configuration_templates' function.
class DescribeLaunchConfigurationTemplatesResponse(BaseValidatorModel):
    items: List[LaunchConfigurationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_launch_configuration_template' function.
class CreateLaunchConfigurationTemplateRequest(BaseValidatorModel):
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConf] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[Licensing] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsUnion] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConf] = None
    smallVolumeMaxSize: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


# This class is the input for the 'update_launch_configuration' function.
class UpdateLaunchConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[Licensing] = None
    mapAutoTaggingMpeID: Optional[str] = None
    name: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsUnion] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


# This class is the input for the 'update_launch_configuration_template' function.
class UpdateLaunchConfigurationTemplateRequest(BaseValidatorModel):
    launchConfigurationTemplateID: str
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConf] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[Licensing] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsUnion] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConf] = None
    smallVolumeMaxSize: Optional[int] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class Job(BaseValidatorModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingServers: Optional[List[ParticipatingServer]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None


# This class is the output for the 'describe_jobs' function.
class DescribeJobsResponse(BaseValidatorModel):
    items: List[Job]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_cutover' function.
class StartCutoverResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_test' function.
class StartTestResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_target_instances' function.
class TerminateTargetInstancesResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata