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
from aws_resource_validator.pydantic_models.drs_constants import *

class Account(BaseValidatorModel):
    accountID: Optional[str] = None


class AssociateSourceNetworkStackRequest(BaseValidatorModel):
    cfnStackName: str
    sourceNetworkID: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CPU(BaseValidatorModel):
    cores: Optional[int] = None
    modelName: Optional[str] = None


class ProductCode(BaseValidatorModel):
    productCodeId: Optional[str] = None
    productCodeMode: Optional[ProductCodeModeType] = None


class CreateExtendedSourceServerRequest(BaseValidatorModel):
    sourceServerArn: str
    tags: Optional[Mapping[str, str]] = None


class Licensing(BaseValidatorModel):
    osByol: Optional[bool] = None


class PITPolicyRule(BaseValidatorModel):
    interval: int
    retentionDuration: int
    units: PITPolicyRuleUnitsType
    enabled: Optional[bool] = None
    ruleID: Optional[int] = None


class CreateSourceNetworkRequest(BaseValidatorModel):
    originAccountID: str
    originRegion: str
    vpcID: str
    tags: Optional[Mapping[str, str]] = None


class DataReplicationError(BaseValidatorModel):
    error: Optional[DataReplicationErrorStringType] = None
    rawError: Optional[str] = None


class DataReplicationInfoReplicatedDisk(BaseValidatorModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None
    volumeStatus: Optional[VolumeStatusType] = None


class DataReplicationInitiationStep(BaseValidatorModel):
    name: Optional[DataReplicationInitiationStepNameType] = None
    status: Optional[DataReplicationInitiationStepStatusType] = None


class DeleteJobRequest(BaseValidatorModel):
    jobID: str


class DeleteLaunchActionRequest(BaseValidatorModel):
    actionId: str
    resourceId: str


class DeleteLaunchConfigurationTemplateRequest(BaseValidatorModel):
    launchConfigurationTemplateID: str


class DeleteRecoveryInstanceRequest(BaseValidatorModel):
    recoveryInstanceID: str


class DeleteReplicationConfigurationTemplateRequest(BaseValidatorModel):
    replicationConfigurationTemplateID: str


class DeleteSourceNetworkRequest(BaseValidatorModel):
    sourceNetworkID: str


class DeleteSourceServerRequest(BaseValidatorModel):
    sourceServerID: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeJobLogItemsRequest(BaseValidatorModel):
    jobID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeJobsRequestFilters(BaseValidatorModel):
    fromDate: Optional[str] = None
    jobIDs: Optional[Sequence[str]] = None
    toDate: Optional[str] = None


class DescribeLaunchConfigurationTemplatesRequest(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeRecoveryInstancesRequestFilters(BaseValidatorModel):
    recoveryInstanceIDs: Optional[Sequence[str]] = None
    sourceServerIDs: Optional[Sequence[str]] = None


class DescribeRecoverySnapshotsRequestFilters(BaseValidatorModel):
    fromDateTime: Optional[str] = None
    toDateTime: Optional[str] = None


class RecoverySnapshot(BaseValidatorModel):
    expectedTimestamp: str
    snapshotID: str
    sourceServerID: str
    ebsSnapshots: Optional[List[str]] = None
    timestamp: Optional[str] = None


class DescribeReplicationConfigurationTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None


class DescribeSourceNetworksRequestFilters(BaseValidatorModel):
    originAccountID: Optional[str] = None
    originRegion: Optional[str] = None
    sourceNetworkIDs: Optional[Sequence[str]] = None


class DescribeSourceServersRequestFilters(BaseValidatorModel):
    hardwareId: Optional[str] = None
    sourceServerIDs: Optional[Sequence[str]] = None
    stagingAccountIDs: Optional[Sequence[str]] = None


class DisconnectRecoveryInstanceRequest(BaseValidatorModel):
    recoveryInstanceID: str


class DisconnectSourceServerRequest(BaseValidatorModel):
    sourceServerID: str


class SourceNetworkData(BaseValidatorModel):
    sourceNetworkID: Optional[str] = None
    sourceVpc: Optional[str] = None
    stackName: Optional[str] = None
    targetVpc: Optional[str] = None


class ExportSourceNetworkCfnTemplateRequest(BaseValidatorModel):
    sourceNetworkID: str


class GetFailbackReplicationConfigurationRequest(BaseValidatorModel):
    recoveryInstanceID: str


class GetLaunchConfigurationRequest(BaseValidatorModel):
    sourceServerID: str


class GetReplicationConfigurationRequest(BaseValidatorModel):
    sourceServerID: str


class IdentificationHints(BaseValidatorModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmWareUuid: Optional[str] = None


class LaunchActionsRequestFilters(BaseValidatorModel):
    actionIds: Optional[Sequence[str]] = None


class LaunchIntoInstanceProperties(BaseValidatorModel):
    launchIntoEC2InstanceID: Optional[str] = None


class ListExtensibleSourceServersRequest(BaseValidatorModel):
    stagingAccountID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StagingSourceServer(BaseValidatorModel):
    arn: Optional[str] = None
    hostname: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStagingAccountsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class NetworkInterface(BaseValidatorModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None


class OS(BaseValidatorModel):
    fullString: Optional[str] = None


class ParticipatingResourceID(BaseValidatorModel):
    sourceNetworkID: Optional[str] = None


class RecoveryInstanceDataReplicationError(BaseValidatorModel):
    error: Optional[FailbackReplicationErrorType] = None
    rawError: Optional[str] = None


class RecoveryInstanceDataReplicationInfoReplicatedDisk(BaseValidatorModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None


class RecoveryInstanceDataReplicationInitiationStep(BaseValidatorModel):
    name: Optional[RecoveryInstanceDataReplicationInitiationStepNameType] = None
    status: Optional[RecoveryInstanceDataReplicationInitiationStepStatusType] = None


class RecoveryInstanceFailback(BaseValidatorModel):
    agentLastSeenByServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    failbackClientID: Optional[str] = None
    failbackClientLastSeenByServiceDateTime: Optional[str] = None
    failbackInitiationTime: Optional[str] = None
    failbackJobID: Optional[str] = None
    failbackLaunchType: Optional[FailbackLaunchTypeType] = None
    failbackToOriginalServer: Optional[bool] = None
    firstByteDateTime: Optional[str] = None
    state: Optional[FailbackStateType] = None


class RecoveryLifeCycle(BaseValidatorModel):
    apiCallDateTime: Optional[datetime] = None
    jobID: Optional[str] = None
    lastRecoveryResult: Optional[RecoveryResultType] = None


class ReplicationConfigurationReplicatedDisk(BaseValidatorModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    optimizedStagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None


class RetryDataReplicationRequest(BaseValidatorModel):
    sourceServerID: str


class ReverseReplicationRequest(BaseValidatorModel):
    recoveryInstanceID: str


class SourceCloudProperties(BaseValidatorModel):
    originAccountID: Optional[str] = None
    originAvailabilityZone: Optional[str] = None
    originRegion: Optional[str] = None
    sourceOutpostArn: Optional[str] = None


class StagingArea(BaseValidatorModel):
    errorMessage: Optional[str] = None
    stagingAccountID: Optional[str] = None
    stagingSourceServerArn: Optional[str] = None
    status: Optional[ExtensionStatusType] = None


class StartFailbackLaunchRequest(BaseValidatorModel):
    recoveryInstanceIDs: Sequence[str]
    tags: Optional[Mapping[str, str]] = None


class StartRecoveryRequestSourceServer(BaseValidatorModel):
    sourceServerID: str
    recoverySnapshotID: Optional[str] = None


class StartReplicationRequest(BaseValidatorModel):
    sourceServerID: str


class StartSourceNetworkRecoveryRequestNetworkEntry(BaseValidatorModel):
    sourceNetworkID: str
    cfnStackName: Optional[str] = None


class StartSourceNetworkReplicationRequest(BaseValidatorModel):
    sourceNetworkID: str


class StopFailbackRequest(BaseValidatorModel):
    recoveryInstanceID: str


class StopReplicationRequest(BaseValidatorModel):
    sourceServerID: str


class StopSourceNetworkReplicationRequest(BaseValidatorModel):
    sourceNetworkID: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TerminateRecoveryInstancesRequest(BaseValidatorModel):
    recoveryInstanceIDs: Sequence[str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateFailbackReplicationConfigurationRequest(BaseValidatorModel):
    recoveryInstanceID: str
    bandwidthThrottling: Optional[int] = None
    name: Optional[str] = None
    usePrivateIP: Optional[bool] = None


class CreateSourceNetworkResponse(BaseValidatorModel):
    sourceNetworkID: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExportSourceNetworkCfnTemplateResponse(BaseValidatorModel):
    s3DestinationUrl: str
    ResponseMetadata: ResponseMetadata


class GetFailbackReplicationConfigurationResponse(BaseValidatorModel):
    bandwidthThrottling: int
    name: str
    recoveryInstanceID: str
    usePrivateIP: bool
    ResponseMetadata: ResponseMetadata


class ListStagingAccountsResponse(BaseValidatorModel):
    accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ReverseReplicationResponse(BaseValidatorModel):
    reversedDirectionSourceServerArn: str
    ResponseMetadata: ResponseMetadata


class ConversionProperties(BaseValidatorModel):
    dataTimestamp: Optional[str] = None
    forceUefi: Optional[bool] = None
    rootVolumeName: Optional[str] = None
    volumeToConversionMap: Optional[Dict[str, Dict[str, str]]] = None
    volumeToProductCodes: Optional[Dict[str, List[ProductCode]]] = None
    volumeToVolumeSize: Optional[Dict[str, int]] = None


class CreateLaunchConfigurationTemplateRequest(BaseValidatorModel):
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[Licensing] = None
    postLaunchEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class LaunchConfigurationTemplate(BaseValidatorModel):
    arn: Optional[str] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchConfigurationTemplateID: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[Licensing] = None
    postLaunchEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class UpdateLaunchConfigurationTemplateRequest(BaseValidatorModel):
    launchConfigurationTemplateID: str
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[Licensing] = None
    postLaunchEnabled: Optional[bool] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class CreateReplicationConfigurationTemplateRequest(BaseValidatorModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    pitPolicy: Sequence[PITPolicyRule]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: Sequence[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Mapping[str, str]
    useDedicatedReplicationServer: bool
    autoReplicateNewDisks: Optional[bool] = None
    ebsEncryptionKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ReplicationConfigurationTemplateResponse(BaseValidatorModel):
    arn: str
    associateDefaultSecurityGroup: bool
    autoReplicateNewDisks: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    pitPolicy: List[PITPolicyRule]
    replicationConfigurationTemplateID: str
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    tags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ResponseMetadata: ResponseMetadata


class ReplicationConfigurationTemplate(BaseValidatorModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ ReplicationConfigurationDefaultLargeStagingDiskTypeType ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    pitPolicy: Optional[List[PITPolicyRule]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None


class UpdateReplicationConfigurationTemplateRequest(BaseValidatorModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ ReplicationConfigurationDefaultLargeStagingDiskTypeType ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    pitPolicy: Optional[Sequence[PITPolicyRule]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None


class DataReplicationInitiation(BaseValidatorModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStep]] = None


class DescribeJobLogItemsRequestPaginate(BaseValidatorModel):
    jobID: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLaunchConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExtensibleSourceServersRequestPaginate(BaseValidatorModel):
    stagingAccountID: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStagingAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeJobsRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeJobsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeJobsRequest(BaseValidatorModel):
    filters: Optional[DescribeJobsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeRecoveryInstancesRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeRecoveryInstancesRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRecoveryInstancesRequest(BaseValidatorModel):
    filters: Optional[DescribeRecoveryInstancesRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeRecoverySnapshotsRequestPaginate(BaseValidatorModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFilters] = None
    order: Optional[RecoverySnapshotsOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRecoverySnapshotsRequest(BaseValidatorModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    order: Optional[RecoverySnapshotsOrderType] = None


class DescribeRecoverySnapshotsResponse(BaseValidatorModel):
    items: List[RecoverySnapshot]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeSourceNetworksRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeSourceNetworksRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSourceNetworksRequest(BaseValidatorModel):
    filters: Optional[DescribeSourceNetworksRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeSourceServersRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeSourceServersRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSourceServersRequest(BaseValidatorModel):
    filters: Optional[DescribeSourceServersRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class EventResourceData(BaseValidatorModel):
    sourceNetworkData: Optional[SourceNetworkData] = None


class LaunchActionParameter(BaseValidatorModel):
    pass


class PutLaunchActionRequest(BaseValidatorModel):
    actionCode: str
    actionId: str
    actionVersion: str
    active: bool
    category: LaunchActionCategoryType
    description: str
    name: str
    optional: bool
    order: int
    resourceId: str
    parameters: Optional[Mapping[str, LaunchActionParameter]] = None


class ListLaunchActionsRequestPaginate(BaseValidatorModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLaunchActionsRequest(BaseValidatorModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class LaunchConfiguration(BaseValidatorModel):
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    launchDisposition: LaunchDispositionType
    launchIntoInstanceProperties: LaunchIntoInstanceProperties
    licensing: Licensing
    name: str
    postLaunchEnabled: bool
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadata


class UpdateLaunchConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoInstanceProperties: Optional[LaunchIntoInstanceProperties] = None
    licensing: Optional[Licensing] = None
    name: Optional[str] = None
    postLaunchEnabled: Optional[bool] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None


class LifeCycleLastLaunchInitiated(BaseValidatorModel):
    pass


class LifeCycleLastLaunch(BaseValidatorModel):
    initiated: Optional[LifeCycleLastLaunchInitiated] = None
    status: Optional[LaunchStatusType] = None


class ListExtensibleSourceServersResponse(BaseValidatorModel):
    items: List[StagingSourceServer]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Disk(BaseValidatorModel):
    pass


class SourceProperties(BaseValidatorModel):
    cpus: Optional[List[CPU]] = None
    disks: Optional[List[Disk]] = None
    identificationHints: Optional[IdentificationHints] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None
    os: Optional[OS] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None
    supportsNitroInstances: Optional[bool] = None


class ParticipatingResource(BaseValidatorModel):
    launchStatus: Optional[LaunchStatusType] = None
    participatingResourceID: Optional[ParticipatingResourceID] = None


class RecoveryInstanceDataReplicationInitiation(BaseValidatorModel):
    startDateTime: Optional[str] = None
    steps: Optional[List[RecoveryInstanceDataReplicationInitiationStep]] = None


class RecoveryInstanceDisk(BaseValidatorModel):
    pass


class RecoveryInstanceProperties(BaseValidatorModel):
    cpus: Optional[List[CPU]] = None
    disks: Optional[List[RecoveryInstanceDisk]] = None
    identificationHints: Optional[IdentificationHints] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None
    os: Optional[OS] = None
    ramBytes: Optional[int] = None


class SourceNetwork(BaseValidatorModel):
    arn: Optional[str] = None
    cfnStackName: Optional[str] = None
    lastRecovery: Optional[RecoveryLifeCycle] = None
    launchedVpcID: Optional[str] = None
    replicationStatus: Optional[ReplicationStatusType] = None
    replicationStatusDetails: Optional[str] = None
    sourceAccountID: Optional[str] = None
    sourceNetworkID: Optional[str] = None
    sourceRegion: Optional[str] = None
    sourceVpcID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ReplicationConfiguration(BaseValidatorModel):
    associateDefaultSecurityGroup: bool
    autoReplicateNewDisks: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    name: str
    pitPolicy: List[PITPolicyRule]
    replicatedDisks: List[ReplicationConfigurationReplicatedDisk]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    sourceServerID: str
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ResponseMetadata: ResponseMetadata


class UpdateReplicationConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ ReplicationConfigurationDefaultLargeStagingDiskTypeType ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    name: Optional[str] = None
    pitPolicy: Optional[Sequence[PITPolicyRule]] = None
    replicatedDisks: Optional[Sequence[ReplicationConfigurationReplicatedDisk]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None


class StartRecoveryRequest(BaseValidatorModel):
    sourceServers: Sequence[StartRecoveryRequestSourceServer]
    isDrill: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class StartSourceNetworkRecoveryRequest(BaseValidatorModel):
    sourceNetworks: Sequence[StartSourceNetworkRecoveryRequestNetworkEntry]
    deployAsNew: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class CreateLaunchConfigurationTemplateResponse(BaseValidatorModel):
    launchConfigurationTemplate: LaunchConfigurationTemplate
    ResponseMetadata: ResponseMetadata


class DescribeLaunchConfigurationTemplatesResponse(BaseValidatorModel):
    items: List[LaunchConfigurationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateLaunchConfigurationTemplateResponse(BaseValidatorModel):
    launchConfigurationTemplate: LaunchConfigurationTemplate
    ResponseMetadata: ResponseMetadata


class DescribeReplicationConfigurationTemplatesResponse(BaseValidatorModel):
    items: List[ReplicationConfigurationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataReplicationInfo(BaseValidatorModel):
    dataReplicationError: Optional[DataReplicationError] = None
    dataReplicationInitiation: Optional[DataReplicationInitiation] = None
    dataReplicationState: Optional[DataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    replicatedDisks: Optional[List[DataReplicationInfoReplicatedDisk]] = None
    stagingAvailabilityZone: Optional[str] = None
    stagingOutpostArn: Optional[str] = None


class JobLogEventData(BaseValidatorModel):
    conversionProperties: Optional[ConversionProperties] = None
    conversionServerID: Optional[str] = None
    eventResourceData: Optional[EventResourceData] = None
    rawError: Optional[str] = None
    sourceServerID: Optional[str] = None
    targetInstanceID: Optional[str] = None


class LaunchAction(BaseValidatorModel):
    pass


class LaunchActionRun(BaseValidatorModel):
    action: Optional[LaunchAction] = None
    failureReason: Optional[str] = None
    runId: Optional[str] = None
    status: Optional[LaunchActionRunStatusType] = None


class ListLaunchActionsResponse(BaseValidatorModel):
    items: List[LaunchAction]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LifeCycle(BaseValidatorModel):
    addedToServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    firstByteDateTime: Optional[str] = None
    lastLaunch: Optional[LifeCycleLastLaunch] = None
    lastSeenByServiceDateTime: Optional[str] = None


class RecoveryInstanceDataReplicationInfo(BaseValidatorModel):
    dataReplicationError: Optional[RecoveryInstanceDataReplicationError] = None
    dataReplicationInitiation: Optional[RecoveryInstanceDataReplicationInitiation] = None
    dataReplicationState: Optional[RecoveryInstanceDataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    replicatedDisks: Optional[List[RecoveryInstanceDataReplicationInfoReplicatedDisk]] = None
    stagingAvailabilityZone: Optional[str] = None
    stagingOutpostArn: Optional[str] = None


class DescribeSourceNetworksResponse(BaseValidatorModel):
    items: List[SourceNetwork]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartSourceNetworkReplicationResponse(BaseValidatorModel):
    sourceNetwork: SourceNetwork
    ResponseMetadata: ResponseMetadata


class StopSourceNetworkReplicationResponse(BaseValidatorModel):
    sourceNetwork: SourceNetwork
    ResponseMetadata: ResponseMetadata


class JobLog(BaseValidatorModel):
    event: Optional[JobLogEventType] = None
    eventData: Optional[JobLogEventData] = None
    logDateTime: Optional[str] = None


class LaunchActionsStatus(BaseValidatorModel):
    runs: Optional[List[LaunchActionRun]] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None


class SourceServerResponse(BaseValidatorModel):
    agentVersion: str
    arn: str
    dataReplicationInfo: DataReplicationInfo
    lastLaunchResult: LastLaunchResultType
    lifeCycle: LifeCycle
    recoveryInstanceId: str
    replicationDirection: ReplicationDirectionType
    reversedDirectionSourceServerArn: str
    sourceCloudProperties: SourceCloudProperties
    sourceNetworkID: str
    sourceProperties: SourceProperties
    sourceServerID: str
    stagingArea: StagingArea
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SourceServer(BaseValidatorModel):
    agentVersion: Optional[str] = None
    arn: Optional[str] = None
    dataReplicationInfo: Optional[DataReplicationInfo] = None
    lastLaunchResult: Optional[LastLaunchResultType] = None
    lifeCycle: Optional[LifeCycle] = None
    recoveryInstanceId: Optional[str] = None
    replicationDirection: Optional[ReplicationDirectionType] = None
    reversedDirectionSourceServerArn: Optional[str] = None
    sourceCloudProperties: Optional[SourceCloudProperties] = None
    sourceNetworkID: Optional[str] = None
    sourceProperties: Optional[SourceProperties] = None
    sourceServerID: Optional[str] = None
    stagingArea: Optional[StagingArea] = None
    tags: Optional[Dict[str, str]] = None


class RecoveryInstance(BaseValidatorModel):
    agentVersion: Optional[str] = None
    arn: Optional[str] = None
    dataReplicationInfo: Optional[RecoveryInstanceDataReplicationInfo] = None
    ec2InstanceID: Optional[str] = None
    ec2InstanceState: Optional[EC2InstanceStateType] = None
    failback: Optional[RecoveryInstanceFailback] = None
    isDrill: Optional[bool] = None
    jobID: Optional[str] = None
    originAvailabilityZone: Optional[str] = None
    originEnvironment: Optional[OriginEnvironmentType] = None
    pointInTimeSnapshotDateTime: Optional[str] = None
    recoveryInstanceID: Optional[str] = None
    recoveryInstanceProperties: Optional[RecoveryInstanceProperties] = None
    sourceOutpostArn: Optional[str] = None
    sourceServerID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeJobLogItemsResponse(BaseValidatorModel):
    items: List[JobLog]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParticipatingServer(BaseValidatorModel):
    launchActionsStatus: Optional[LaunchActionsStatus] = None
    launchStatus: Optional[LaunchStatusType] = None
    recoveryInstanceID: Optional[str] = None
    sourceServerID: Optional[str] = None


class CreateExtendedSourceServerResponse(BaseValidatorModel):
    sourceServer: SourceServer
    ResponseMetadata: ResponseMetadata


class DescribeSourceServersResponse(BaseValidatorModel):
    items: List[SourceServer]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartReplicationResponse(BaseValidatorModel):
    sourceServer: SourceServer
    ResponseMetadata: ResponseMetadata


class StopReplicationResponse(BaseValidatorModel):
    sourceServer: SourceServer
    ResponseMetadata: ResponseMetadata


class DescribeRecoveryInstancesResponse(BaseValidatorModel):
    items: List[RecoveryInstance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Job(BaseValidatorModel):
    pass


class AssociateSourceNetworkStackResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class DescribeJobsResponse(BaseValidatorModel):
    items: List[Job]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartFailbackLaunchResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class StartRecoveryResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class StartSourceNetworkRecoveryResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class TerminateRecoveryInstancesResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


