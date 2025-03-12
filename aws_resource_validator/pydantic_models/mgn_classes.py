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


class ArchiveApplicationRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None


class ArchiveWaveRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None


class AssociateApplicationsRequestTypeDef(BaseValidatorModel):
    applicationIDs: Sequence[str]
    waveID: str
    accountID: Optional[str] = None


class AssociateSourceServersRequestTypeDef(BaseValidatorModel):
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


class CreateApplicationRequestTypeDef(BaseValidatorModel):
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


class CreateReplicationConfigurationTemplateRequestTypeDef(BaseValidatorModel):
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


class CreateWaveRequestTypeDef(BaseValidatorModel):
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


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None


class DeleteConnectorRequestTypeDef(BaseValidatorModel):
    connectorID: str


class DeleteJobRequestTypeDef(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None


class DeleteLaunchConfigurationTemplateRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str


class DeleteReplicationConfigurationTemplateRequestTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateID: str


class DeleteSourceServerRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class DeleteVcenterClientRequestTypeDef(BaseValidatorModel):
    vcenterClientID: str


class DeleteWaveRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeJobLogItemsRequestTypeDef(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeJobsRequestFiltersTypeDef(BaseValidatorModel):
    fromDate: Optional[str] = None
    jobIDs: Optional[Sequence[str]] = None
    toDate: Optional[str] = None


class DescribeLaunchConfigurationTemplatesRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeReplicationConfigurationTemplatesRequestTypeDef(BaseValidatorModel):
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
    defaultLargeStagingDiskType: Optional[ ReplicationConfigurationDefaultLargeStagingDiskTypeType ] = None
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


class DescribeVcenterClientsRequestTypeDef(BaseValidatorModel):
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


class DisassociateApplicationsRequestTypeDef(BaseValidatorModel):
    applicationIDs: Sequence[str]
    waveID: str
    accountID: Optional[str] = None


class DisassociateSourceServersRequestTypeDef(BaseValidatorModel):
    applicationID: str
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None


class DisconnectFromServiceRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class ExportErrorDataTypeDef(BaseValidatorModel):
    rawError: Optional[str] = None


class ExportTaskSummaryTypeDef(BaseValidatorModel):
    applicationsCount: Optional[int] = None
    serversCount: Optional[int] = None
    wavesCount: Optional[int] = None


class FinalizeCutoverRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class GetLaunchConfigurationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class GetReplicationConfigurationRequestTypeDef(BaseValidatorModel):
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


class ListExportErrorsRequestTypeDef(BaseValidatorModel):
    exportID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExportsRequestFiltersTypeDef(BaseValidatorModel):
    exportIDs: Optional[Sequence[str]] = None


class ListImportErrorsRequestTypeDef(BaseValidatorModel):
    importID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportsRequestFiltersTypeDef(BaseValidatorModel):
    importIDs: Optional[Sequence[str]] = None


class ListManagedAccountsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class SourceServerActionsRequestFiltersTypeDef(BaseValidatorModel):
    actionIDs: Optional[Sequence[str]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class TemplateActionsRequestFiltersTypeDef(BaseValidatorModel):
    actionIDs: Optional[Sequence[str]] = None


class ListWavesRequestFiltersTypeDef(BaseValidatorModel):
    isArchived: Optional[bool] = None
    waveIDs: Optional[Sequence[str]] = None


class MarkAsArchivedRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None


class OSTypeDef(BaseValidatorModel):
    fullString: Optional[str] = None


class PauseReplicationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class SsmExternalParameterTypeDef(BaseValidatorModel):
    dynamicPath: Optional[str] = None


class SsmParameterStoreParameterTypeDef(BaseValidatorModel):
    parameterName: str
    parameterType: Literal["STRING"]


class RemoveSourceServerActionRequestTypeDef(BaseValidatorModel):
    actionID: str
    sourceServerID: str
    accountID: Optional[str] = None


class RemoveTemplateActionRequestTypeDef(BaseValidatorModel):
    actionID: str
    launchConfigurationTemplateID: str


class ReplicationConfigurationReplicatedDiskTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None


class ResumeReplicationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class RetryDataReplicationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class SourceServerConnectorActionTypeDef(BaseValidatorModel):
    connectorArn: Optional[str] = None
    credentialsSecretArn: Optional[str] = None


class StartCutoverRequestTypeDef(BaseValidatorModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StartExportRequestTypeDef(BaseValidatorModel):
    s3Bucket: str
    s3Key: str
    s3BucketOwner: Optional[str] = None


class StartReplicationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class StartTestRequestTypeDef(BaseValidatorModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StopReplicationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TerminateTargetInstancesRequestTypeDef(BaseValidatorModel):
    sourceServerIDs: Sequence[str]
    accountID: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UnarchiveApplicationRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None


class UnarchiveWaveRequestTypeDef(BaseValidatorModel):
    waveID: str
    accountID: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    applicationID: str
    accountID: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None


class UpdateReplicationConfigurationTemplateRequestTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ ReplicationConfigurationDefaultLargeStagingDiskTypeType ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None
    useFipsEndpoint: Optional[bool] = None


class UpdateSourceServerReplicationTypeRequestTypeDef(BaseValidatorModel):
    replicationType: ReplicationTypeType
    sourceServerID: str
    accountID: Optional[str] = None


class UpdateWaveRequestTypeDef(BaseValidatorModel):
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


class ChangeServerLifeCycleStateRequestTypeDef(BaseValidatorModel):
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


class CreateConnectorRequestTypeDef(BaseValidatorModel):
    name: str
    ssmInstanceID: str
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateConnectorRequestTypeDef(BaseValidatorModel):
    connectorID: str
    name: Optional[str] = None
    ssmCommandConfig: Optional[ConnectorSsmCommandConfigTypeDef] = None


class DataReplicationInitiationTypeDef(BaseValidatorModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStepTypeDef]] = None


class DescribeJobLogItemsRequestPaginateTypeDef(BaseValidatorModel):
    jobID: str
    accountID: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeVcenterClientsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExportErrorsRequestPaginateTypeDef(BaseValidatorModel):
    exportID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportErrorsRequestPaginateTypeDef(BaseValidatorModel):
    importID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedAccountsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeJobsRequestPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeJobsRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeReplicationConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    items: List[ReplicationConfigurationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeSourceServersRequestPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSourceServersRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeVcenterClientsResponseTypeDef(BaseValidatorModel):
    items: List[VcenterClientTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class StartImportRequestTypeDef(BaseValidatorModel):
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


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListApplicationsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListConnectorsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[ListConnectorsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorsRequestTypeDef(BaseValidatorModel):
    filters: Optional[ListConnectorsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExportsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[ListExportsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExportsRequestTypeDef(BaseValidatorModel):
    filters: Optional[ListExportsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[ListImportsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportsRequestTypeDef(BaseValidatorModel):
    filters: Optional[ListImportsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListManagedAccountsResponseTypeDef(BaseValidatorModel):
    items: List[ManagedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSourceServerActionsRequestPaginateTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceServerActionsRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    filters: Optional[SourceServerActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTemplateActionsRequestPaginateTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTemplateActionsRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str
    filters: Optional[TemplateActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWavesRequestPaginateTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWavesRequestTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None
    filters: Optional[ListWavesRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DiskTypeDef(BaseValidatorModel):
    pass


class SourcePropertiesTypeDef(BaseValidatorModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[DiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None


class PutSourceServerActionRequestTypeDef(BaseValidatorModel):
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


class PutTemplateActionRequestTypeDef(BaseValidatorModel):
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


class SsmDocumentOutputTypeDef(BaseValidatorModel):
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


class UpdateReplicationConfigurationRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    accountID: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ ReplicationConfigurationDefaultLargeStagingDiskTypeType ] = None
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


class UpdateSourceServerRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListConnectorsResponseTypeDef(BaseValidatorModel):
    items: List[ConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListExportsResponseTypeDef(BaseValidatorModel):
    items: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartExportResponseTypeDef(BaseValidatorModel):
    exportTask: ExportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListImportErrorsResponseTypeDef(BaseValidatorModel):
    items: List[ImportTaskErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobPostLaunchActionsLaunchStatusTypeDef(BaseValidatorModel):
    executionID: Optional[str] = None
    executionStatus: Optional[PostLaunchActionExecutionStatusType] = None
    failureReason: Optional[str] = None
    ssmDocument: Optional[SsmDocumentOutputTypeDef] = None
    ssmDocumentType: Optional[SsmDocumentTypeType] = None


class PostLaunchActionsOutputTypeDef(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[List[SsmDocumentOutputTypeDef]] = None


class PostLaunchActionsTypeDef(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    deployment: Optional[PostLaunchActionsDeploymentTypeType] = None
    s3LogBucket: Optional[str] = None
    s3OutputKeyPrefix: Optional[str] = None
    ssmDocuments: Optional[Sequence[SsmDocumentTypeDef]] = None


class ListTemplateActionsResponseTypeDef(BaseValidatorModel):
    items: List[TemplateActionDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListWavesResponseTypeDef(BaseValidatorModel):
    items: List[WaveTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListImportsResponseTypeDef(BaseValidatorModel):
    items: List[ImportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class PostLaunchActionsStatusTypeDef(BaseValidatorModel):
    postLaunchActionsLaunchStatusList: Optional[List[JobPostLaunchActionsLaunchStatusTypeDef]] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None


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
    postLaunchActions: PostLaunchActionsOutputTypeDef
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
    postLaunchActions: Optional[PostLaunchActionsOutputTypeDef] = None
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
    postLaunchActions: PostLaunchActionsOutputTypeDef
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSourceServersResponseTypeDef(BaseValidatorModel):
    items: List[SourceServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ParticipatingServerTypeDef(BaseValidatorModel):
    sourceServerID: str
    launchStatus: Optional[LaunchStatusType] = None
    launchedEc2InstanceID: Optional[str] = None
    postLaunchActionsStatus: Optional[PostLaunchActionsStatusTypeDef] = None


class DescribeLaunchConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    items: List[LaunchConfigurationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PostLaunchActionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateLaunchConfigurationTemplateRequestTypeDef(BaseValidatorModel):
    associatePublicIpAddress: Optional[bool] = None
    bootMode: Optional[BootModeType] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    enableMapAutoTagging: Optional[bool] = None
    largeVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    licensing: Optional[LicensingTypeDef] = None
    mapAutoTaggingMpeID: Optional[str] = None
    postLaunchActions: Optional[PostLaunchActionsUnionTypeDef] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    smallVolumeMaxSize: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class UpdateLaunchConfigurationRequestTypeDef(BaseValidatorModel):
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
    postLaunchActions: Optional[PostLaunchActionsUnionTypeDef] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class UpdateLaunchConfigurationTemplateRequestTypeDef(BaseValidatorModel):
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
    postLaunchActions: Optional[PostLaunchActionsUnionTypeDef] = None
    smallVolumeConf: Optional[LaunchTemplateDiskConfTypeDef] = None
    smallVolumeMaxSize: Optional[int] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class JobTypeDef(BaseValidatorModel):
    pass


class DescribeJobsResponseTypeDef(BaseValidatorModel):
    items: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartCutoverResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartTestResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TerminateTargetInstancesResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


