from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.drs.drs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Account(BaseValidatorModel):
    accountID: Optional[str] = None


# This class is the input for the 'associate_source_network_stack' function.
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


# This class is the input for the 'create_extended_source_server' function.
class CreateExtendedSourceServerRequest(BaseValidatorModel):
    sourceServerArn: str
    tags: Optional[Dict[str, str]] = None


class Licensing(BaseValidatorModel):
    osByol: Optional[bool] = None


class PITPolicyRule(BaseValidatorModel):
    interval: int
    retentionDuration: int
    units: PITPolicyRuleUnitsType
    enabled: Optional[bool] = None
    ruleID: Optional[int] = None


# This class is the input for the 'create_source_network' function.
class CreateSourceNetworkRequest(BaseValidatorModel):
    originAccountID: str
    originRegion: str
    vpcID: str
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


# This class is the input for the 'delete_recovery_instance' function.
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


# This class is the input for the 'describe_job_log_items' function.
class DescribeJobLogItemsRequest(BaseValidatorModel):
    jobID: str
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


class DescribeRecoveryInstancesRequestFilters(BaseValidatorModel):
    recoveryInstanceIDs: Optional[List[str]] = None
    sourceServerIDs: Optional[List[str]] = None


class DescribeRecoverySnapshotsRequestFilters(BaseValidatorModel):
    fromDateTime: Optional[str] = None
    toDateTime: Optional[str] = None


class RecoverySnapshot(BaseValidatorModel):
    expectedTimestamp: str
    snapshotID: str
    sourceServerID: str
    ebsSnapshots: Optional[List[str]] = None
    timestamp: Optional[str] = None


# This class is the input for the 'describe_replication_configuration_templates' function.
class DescribeReplicationConfigurationTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[List[str]] = None


class DescribeSourceNetworksRequestFilters(BaseValidatorModel):
    originAccountID: Optional[str] = None
    originRegion: Optional[str] = None
    sourceNetworkIDs: Optional[List[str]] = None


class DescribeSourceServersRequestFilters(BaseValidatorModel):
    hardwareId: Optional[str] = None
    sourceServerIDs: Optional[List[str]] = None
    stagingAccountIDs: Optional[List[str]] = None


# This class is the input for the 'disconnect_recovery_instance' function.
class DisconnectRecoveryInstanceRequest(BaseValidatorModel):
    recoveryInstanceID: str


# This class is the input for the 'disconnect_source_server' function.
class DisconnectSourceServerRequest(BaseValidatorModel):
    sourceServerID: str


class Disk(BaseValidatorModel):
    bytes: Optional[int] = None
    deviceName: Optional[str] = None


class SourceNetworkData(BaseValidatorModel):
    sourceNetworkID: Optional[str] = None
    sourceVpc: Optional[str] = None
    stackName: Optional[str] = None
    targetVpc: Optional[str] = None


# This class is the input for the 'export_source_network_cfn_template' function.
class ExportSourceNetworkCfnTemplateRequest(BaseValidatorModel):
    sourceNetworkID: str


# This class is the input for the 'get_failback_replication_configuration' function.
class GetFailbackReplicationConfigurationRequest(BaseValidatorModel):
    recoveryInstanceID: str


# This class is the input for the 'get_launch_configuration' function.
class GetLaunchConfigurationRequest(BaseValidatorModel):
    sourceServerID: str


# This class is the input for the 'get_replication_configuration' function.
class GetReplicationConfigurationRequest(BaseValidatorModel):
    sourceServerID: str


class IdentificationHints(BaseValidatorModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmWareUuid: Optional[str] = None


class LaunchActionParameter(BaseValidatorModel):
    type: Optional[LaunchActionParameterTypeType] = None
    value: Optional[str] = None


class LaunchActionsRequestFilters(BaseValidatorModel):
    actionIds: Optional[List[str]] = None


class LaunchIntoInstanceProperties(BaseValidatorModel):
    launchIntoEC2InstanceID: Optional[str] = None


class LifeCycleLastLaunchInitiated(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None
    type: Optional[LastLaunchTypeType] = None


# This class is the input for the 'list_extensible_source_servers' function.
class ListExtensibleSourceServersRequest(BaseValidatorModel):
    stagingAccountID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StagingSourceServer(BaseValidatorModel):
    arn: Optional[str] = None
    hostname: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_staging_accounts' function.
class ListStagingAccountsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
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


class RecoveryInstanceDisk(BaseValidatorModel):
    bytes: Optional[int] = None
    ebsVolumeID: Optional[str] = None
    internalDeviceName: Optional[str] = None


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


# This class is the input for the 'retry_data_replication' function.
class RetryDataReplicationRequest(BaseValidatorModel):
    sourceServerID: str


# This class is the input for the 'reverse_replication' function.
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


# This class is the input for the 'start_failback_launch' function.
class StartFailbackLaunchRequest(BaseValidatorModel):
    recoveryInstanceIDs: List[str]
    tags: Optional[Dict[str, str]] = None


class StartRecoveryRequestSourceServer(BaseValidatorModel):
    sourceServerID: str
    recoverySnapshotID: Optional[str] = None


# This class is the input for the 'start_replication' function.
class StartReplicationRequest(BaseValidatorModel):
    sourceServerID: str


class StartSourceNetworkRecoveryRequestNetworkEntry(BaseValidatorModel):
    sourceNetworkID: str
    cfnStackName: Optional[str] = None


# This class is the input for the 'start_source_network_replication' function.
class StartSourceNetworkReplicationRequest(BaseValidatorModel):
    sourceNetworkID: str


# This class is the input for the 'stop_failback' function.
class StopFailbackRequest(BaseValidatorModel):
    recoveryInstanceID: str


# This class is the input for the 'stop_replication' function.
class StopReplicationRequest(BaseValidatorModel):
    sourceServerID: str


# This class is the input for the 'stop_source_network_replication' function.
class StopSourceNetworkReplicationRequest(BaseValidatorModel):
    sourceNetworkID: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'terminate_recovery_instances' function.
class TerminateRecoveryInstancesRequest(BaseValidatorModel):
    recoveryInstanceIDs: List[str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_failback_replication_configuration' function.
class UpdateFailbackReplicationConfigurationRequest(BaseValidatorModel):
    recoveryInstanceID: str
    bandwidthThrottling: Optional[int] = None
    name: Optional[str] = None
    usePrivateIP: Optional[bool] = None


# This class is the output for the 'create_source_network' function.
class CreateSourceNetworkResponse(BaseValidatorModel):
    sourceNetworkID: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_failback_replication_configuration' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_source_network_cfn_template' function.
class ExportSourceNetworkCfnTemplateResponse(BaseValidatorModel):
    s3DestinationUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_failback_replication_configuration' function.
class GetFailbackReplicationConfigurationResponse(BaseValidatorModel):
    bandwidthThrottling: int
    name: str
    recoveryInstanceID: str
    usePrivateIP: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_staging_accounts' function.
class ListStagingAccountsResponse(BaseValidatorModel):
    accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reverse_replication' function.
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


# This class is the input for the 'create_launch_configuration_template' function.
class CreateLaunchConfigurationTemplateRequest(BaseValidatorModel):
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[Licensing] = None
    postLaunchEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
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


# This class is the input for the 'update_launch_configuration_template' function.
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


# This class is the input for the 'create_replication_configuration_template' function.
class CreateReplicationConfigurationTemplateRequest(BaseValidatorModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    pitPolicy: List[PITPolicyRule]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    autoReplicateNewDisks: Optional[bool] = None
    ebsEncryptionKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'update_replication_configuration_template' function.
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
    defaultLargeStagingDiskType: Optional[ReplicationConfigurationDefaultLargeStagingDiskTypeType] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    pitPolicy: Optional[List[PITPolicyRule]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None


# This class is the input for the 'update_replication_configuration_template' function.
class UpdateReplicationConfigurationTemplateRequest(BaseValidatorModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ReplicationConfigurationDefaultLargeStagingDiskTypeType] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    pitPolicy: Optional[List[PITPolicyRule]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None


class DataReplicationInitiation(BaseValidatorModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStep]] = None


class DescribeJobLogItemsRequestPaginate(BaseValidatorModel):
    jobID: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLaunchConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    replicationConfigurationTemplateIDs: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExtensibleSourceServersRequestPaginate(BaseValidatorModel):
    stagingAccountID: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStagingAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeJobsRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeJobsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_jobs' function.
class DescribeJobsRequest(BaseValidatorModel):
    filters: Optional[DescribeJobsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeRecoveryInstancesRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeRecoveryInstancesRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_recovery_instances' function.
class DescribeRecoveryInstancesRequest(BaseValidatorModel):
    filters: Optional[DescribeRecoveryInstancesRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeRecoverySnapshotsRequestPaginate(BaseValidatorModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFilters] = None
    order: Optional[RecoverySnapshotsOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_recovery_snapshots' function.
class DescribeRecoverySnapshotsRequest(BaseValidatorModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    order: Optional[RecoverySnapshotsOrderType] = None


# This class is the output for the 'describe_recovery_snapshots' function.
class DescribeRecoverySnapshotsResponse(BaseValidatorModel):
    items: List[RecoverySnapshot]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeSourceNetworksRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeSourceNetworksRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_source_networks' function.
class DescribeSourceNetworksRequest(BaseValidatorModel):
    filters: Optional[DescribeSourceNetworksRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeSourceServersRequestPaginate(BaseValidatorModel):
    filters: Optional[DescribeSourceServersRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_source_servers' function.
class DescribeSourceServersRequest(BaseValidatorModel):
    filters: Optional[DescribeSourceServersRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class EventResourceData(BaseValidatorModel):
    sourceNetworkData: Optional[SourceNetworkData] = None


class LaunchAction(BaseValidatorModel):
    actionCode: Optional[str] = None
    actionId: Optional[str] = None
    actionVersion: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[LaunchActionCategoryType] = None
    description: Optional[str] = None
    name: Optional[str] = None
    optional: Optional[bool] = None
    order: Optional[int] = None
    parameters: Optional[Dict[str, LaunchActionParameter]] = None
    type: Optional[LaunchActionTypeType] = None


# This class is the input for the 'put_launch_action' function.
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
    parameters: Optional[Dict[str, LaunchActionParameter]] = None


# This class is the output for the 'put_launch_action' function.
class PutLaunchActionResponse(BaseValidatorModel):
    actionCode: str
    actionId: str
    actionVersion: str
    active: bool
    category: LaunchActionCategoryType
    description: str
    name: str
    optional: bool
    order: int
    parameters: Dict[str, LaunchActionParameter]
    resourceId: str
    type: LaunchActionTypeType
    ResponseMetadata: ResponseMetadata


class ListLaunchActionsRequestPaginate(BaseValidatorModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_launch_actions' function.
class ListLaunchActionsRequest(BaseValidatorModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'update_launch_configuration' function.
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


# This class is the input for the 'update_launch_configuration' function.
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


class LifeCycleLastLaunch(BaseValidatorModel):
    initiated: Optional[LifeCycleLastLaunchInitiated] = None
    status: Optional[LaunchStatusType] = None


# This class is the output for the 'list_extensible_source_servers' function.
class ListExtensibleSourceServersResponse(BaseValidatorModel):
    items: List[StagingSourceServer]
    ResponseMetadata: ResponseMetadata
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
    supportsNitroInstances: Optional[bool] = None


class ParticipatingResource(BaseValidatorModel):
    launchStatus: Optional[LaunchStatusType] = None
    participatingResourceID: Optional[ParticipatingResourceID] = None


class RecoveryInstanceDataReplicationInitiation(BaseValidatorModel):
    startDateTime: Optional[str] = None
    steps: Optional[List[RecoveryInstanceDataReplicationInitiationStep]] = None


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


# This class is the output for the 'update_replication_configuration' function.
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


# This class is the input for the 'update_replication_configuration' function.
class UpdateReplicationConfigurationRequest(BaseValidatorModel):
    sourceServerID: str
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[ReplicationConfigurationDefaultLargeStagingDiskTypeType] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    name: Optional[str] = None
    pitPolicy: Optional[List[PITPolicyRule]] = None
    replicatedDisks: Optional[List[ReplicationConfigurationReplicatedDisk]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None


# This class is the input for the 'start_recovery' function.
class StartRecoveryRequest(BaseValidatorModel):
    sourceServers: List[StartRecoveryRequestSourceServer]
    isDrill: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'start_source_network_recovery' function.
class StartSourceNetworkRecoveryRequest(BaseValidatorModel):
    sourceNetworks: List[StartSourceNetworkRecoveryRequestNetworkEntry]
    deployAsNew: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_launch_configuration_template' function.
class CreateLaunchConfigurationTemplateResponse(BaseValidatorModel):
    launchConfigurationTemplate: LaunchConfigurationTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_launch_configuration_templates' function.
class DescribeLaunchConfigurationTemplatesResponse(BaseValidatorModel):
    items: List[LaunchConfigurationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_launch_configuration_template' function.
class UpdateLaunchConfigurationTemplateResponse(BaseValidatorModel):
    launchConfigurationTemplate: LaunchConfigurationTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_replication_configuration_templates' function.
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


class LaunchActionRun(BaseValidatorModel):
    action: Optional[LaunchAction] = None
    failureReason: Optional[str] = None
    runId: Optional[str] = None
    status: Optional[LaunchActionRunStatusType] = None


# This class is the output for the 'list_launch_actions' function.
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


# This class is the output for the 'describe_source_networks' function.
class DescribeSourceNetworksResponse(BaseValidatorModel):
    items: List[SourceNetwork]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_source_network_replication' function.
class StartSourceNetworkReplicationResponse(BaseValidatorModel):
    sourceNetwork: SourceNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_source_network_replication' function.
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


# This class is the output for the 'retry_data_replication' function.
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


# This class is the output for the 'describe_job_log_items' function.
class DescribeJobLogItemsResponse(BaseValidatorModel):
    items: List[JobLog]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParticipatingServer(BaseValidatorModel):
    launchActionsStatus: Optional[LaunchActionsStatus] = None
    launchStatus: Optional[LaunchStatusType] = None
    recoveryInstanceID: Optional[str] = None
    sourceServerID: Optional[str] = None


# This class is the output for the 'create_extended_source_server' function.
class CreateExtendedSourceServerResponse(BaseValidatorModel):
    sourceServer: SourceServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_source_servers' function.
class DescribeSourceServersResponse(BaseValidatorModel):
    items: List[SourceServer]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_replication' function.
class StartReplicationResponse(BaseValidatorModel):
    sourceServer: SourceServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_replication' function.
class StopReplicationResponse(BaseValidatorModel):
    sourceServer: SourceServer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_recovery_instances' function.
class DescribeRecoveryInstancesResponse(BaseValidatorModel):
    items: List[RecoveryInstance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Job(BaseValidatorModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingResources: Optional[List[ParticipatingResource]] = None
    participatingServers: Optional[List[ParticipatingServer]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None


# This class is the output for the 'associate_source_network_stack' function.
class AssociateSourceNetworkStackResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_jobs' function.
class DescribeJobsResponse(BaseValidatorModel):
    items: List[Job]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_failback_launch' function.
class StartFailbackLaunchResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_recovery' function.
class StartRecoveryResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_source_network_recovery' function.
class StartSourceNetworkRecoveryResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_recovery_instances' function.
class TerminateRecoveryInstancesResponse(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata