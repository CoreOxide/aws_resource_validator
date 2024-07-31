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
from aws_resource_validator.pydantic_models.drs_constants import *

class AccountTypeDef(BaseModel):
    accountID: Optional[str] = None

class AssociateSourceNetworkStackRequestRequestTypeDef(BaseModel):
    cfnStackName: str
    sourceNetworkID: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CPUTypeDef(BaseModel):
    cores: Optional[int] = None
    modelName: Optional[str] = None

class ProductCodeTypeDef(BaseModel):
    productCodeId: Optional[str] = None
    productCodeMode: Optional[ProductCodeModeType] = None

class CreateExtendedSourceServerRequestRequestTypeDef(BaseModel):
    sourceServerArn: str
    tags: Optional[Mapping[str, str]] = None

class LicensingTypeDef(BaseModel):
    osByol: Optional[bool] = None

class PITPolicyRuleTypeDef(BaseModel):
    interval: int
    retentionDuration: int
    units: PITPolicyRuleUnitsType
    enabled: Optional[bool] = None
    ruleID: Optional[int] = None

class CreateSourceNetworkRequestRequestTypeDef(BaseModel):
    originAccountID: str
    originRegion: str
    vpcID: str
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
    volumeStatus: Optional[VolumeStatusType] = None

class DataReplicationInitiationStepTypeDef(BaseModel):
    name: Optional[DataReplicationInitiationStepNameType] = None
    status: Optional[DataReplicationInitiationStepStatusType] = None

class DeleteJobRequestRequestTypeDef(BaseModel):
    jobID: str

class DeleteLaunchActionRequestRequestTypeDef(BaseModel):
    actionId: str
    resourceId: str

class DeleteLaunchConfigurationTemplateRequestRequestTypeDef(BaseModel):
    launchConfigurationTemplateID: str

class DeleteRecoveryInstanceRequestRequestTypeDef(BaseModel):
    recoveryInstanceID: str

class DeleteReplicationConfigurationTemplateRequestRequestTypeDef(BaseModel):
    replicationConfigurationTemplateID: str

class DeleteSourceNetworkRequestRequestTypeDef(BaseModel):
    sourceNetworkID: str

class DeleteSourceServerRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeJobLogItemsRequestRequestTypeDef(BaseModel):
    jobID: str
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

class DescribeRecoveryInstancesRequestFiltersTypeDef(BaseModel):
    recoveryInstanceIDs: Optional[Sequence[str]] = None
    sourceServerIDs: Optional[Sequence[str]] = None

class DescribeRecoverySnapshotsRequestFiltersTypeDef(BaseModel):
    fromDateTime: Optional[str] = None
    toDateTime: Optional[str] = None

class RecoverySnapshotTypeDef(BaseModel):
    expectedTimestamp: str
    snapshotID: str
    sourceServerID: str
    ebsSnapshots: Optional[List[str]] = None
    timestamp: Optional[str] = None

class DescribeReplicationConfigurationTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None

class DescribeSourceNetworksRequestFiltersTypeDef(BaseModel):
    originAccountID: Optional[str] = None
    originRegion: Optional[str] = None
    sourceNetworkIDs: Optional[Sequence[str]] = None

class DescribeSourceServersRequestFiltersTypeDef(BaseModel):
    hardwareId: Optional[str] = None
    sourceServerIDs: Optional[Sequence[str]] = None
    stagingAccountIDs: Optional[Sequence[str]] = None

class DisconnectRecoveryInstanceRequestRequestTypeDef(BaseModel):
    recoveryInstanceID: str

class DisconnectSourceServerRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class DiskTypeDef(BaseModel):
    bytes: Optional[int] = None
    deviceName: Optional[str] = None

class SourceNetworkDataTypeDef(BaseModel):
    sourceNetworkID: Optional[str] = None
    sourceVpc: Optional[str] = None
    stackName: Optional[str] = None
    targetVpc: Optional[str] = None

class ExportSourceNetworkCfnTemplateRequestRequestTypeDef(BaseModel):
    sourceNetworkID: str

class GetFailbackReplicationConfigurationRequestRequestTypeDef(BaseModel):
    recoveryInstanceID: str

class GetLaunchConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class GetReplicationConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class IdentificationHintsTypeDef(BaseModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmWareUuid: Optional[str] = None

class LaunchActionParameterTypeDef(BaseModel):
    type: Optional[LaunchActionParameterTypeType] = None
    value: Optional[str] = None

class LaunchActionsRequestFiltersTypeDef(BaseModel):
    actionIds: Optional[Sequence[str]] = None

class LaunchIntoInstancePropertiesTypeDef(BaseModel):
    launchIntoEC2InstanceID: Optional[str] = None

class LifeCycleLastLaunchInitiatedTypeDef(BaseModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None
    type: Optional[LastLaunchTypeType] = None

class ListExtensibleSourceServersRequestRequestTypeDef(BaseModel):
    stagingAccountID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StagingSourceServerTypeDef(BaseModel):
    arn: Optional[str] = None
    hostname: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStagingAccountsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class NetworkInterfaceTypeDef(BaseModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None

class OSTypeDef(BaseModel):
    fullString: Optional[str] = None

class ParticipatingResourceIDTypeDef(BaseModel):
    sourceNetworkID: Optional[str] = None

class RecoveryInstanceDataReplicationErrorTypeDef(BaseModel):
    error: Optional[FailbackReplicationErrorType] = None
    rawError: Optional[str] = None

class RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef(BaseModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None

class RecoveryInstanceDataReplicationInitiationStepTypeDef(BaseModel):
    name: Optional[RecoveryInstanceDataReplicationInitiationStepNameType] = None
    status: Optional[RecoveryInstanceDataReplicationInitiationStepStatusType] = None

class RecoveryInstanceDiskTypeDef(BaseModel):
    bytes: Optional[int] = None
    ebsVolumeID: Optional[str] = None
    internalDeviceName: Optional[str] = None

class RecoveryInstanceFailbackTypeDef(BaseModel):
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

class RecoveryLifeCycleTypeDef(BaseModel):
    apiCallDateTime: Optional[datetime] = None
    jobID: Optional[str] = None
    lastRecoveryResult: Optional[RecoveryResultType] = None

class ReplicationConfigurationReplicatedDiskTypeDef(BaseModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    optimizedStagingDiskType: Optional[       ReplicationConfigurationReplicatedDiskStagingDiskTypeType     ] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None

class RetryDataReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class ReverseReplicationRequestRequestTypeDef(BaseModel):
    recoveryInstanceID: str

class SourceCloudPropertiesTypeDef(BaseModel):
    originAccountID: Optional[str] = None
    originAvailabilityZone: Optional[str] = None
    originRegion: Optional[str] = None
    sourceOutpostArn: Optional[str] = None

class StagingAreaTypeDef(BaseModel):
    errorMessage: Optional[str] = None
    stagingAccountID: Optional[str] = None
    stagingSourceServerArn: Optional[str] = None
    status: Optional[ExtensionStatusType] = None

class StartFailbackLaunchRequestRequestTypeDef(BaseModel):
    recoveryInstanceIDs: Sequence[str]
    tags: Optional[Mapping[str, str]] = None

class StartRecoveryRequestSourceServerTypeDef(BaseModel):
    sourceServerID: str
    recoverySnapshotID: Optional[str] = None

class StartReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class StartSourceNetworkRecoveryRequestNetworkEntryTypeDef(BaseModel):
    sourceNetworkID: str
    cfnStackName: Optional[str] = None

class StartSourceNetworkReplicationRequestRequestTypeDef(BaseModel):
    sourceNetworkID: str

class StopFailbackRequestRequestTypeDef(BaseModel):
    recoveryInstanceID: str

class StopReplicationRequestRequestTypeDef(BaseModel):
    sourceServerID: str

class StopSourceNetworkReplicationRequestRequestTypeDef(BaseModel):
    sourceNetworkID: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateRecoveryInstancesRequestRequestTypeDef(BaseModel):
    recoveryInstanceIDs: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateFailbackReplicationConfigurationRequestRequestTypeDef(BaseModel):
    recoveryInstanceID: str
    bandwidthThrottling: Optional[int] = None
    name: Optional[str] = None
    usePrivateIP: Optional[bool] = None

class CreateSourceNetworkResponseTypeDef(BaseModel):
    sourceNetworkID: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSourceNetworkCfnTemplateResponseTypeDef(BaseModel):
    s3DestinationUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFailbackReplicationConfigurationResponseTypeDef(BaseModel):
    bandwidthThrottling: int
    name: str
    recoveryInstanceID: str
    usePrivateIP: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListStagingAccountsResponseTypeDef(BaseModel):
    accounts: List[AccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReverseReplicationResponseTypeDef(BaseModel):
    reversedDirectionSourceServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConversionPropertiesTypeDef(BaseModel):
    dataTimestamp: Optional[str] = None
    forceUefi: Optional[bool] = None
    rootVolumeName: Optional[str] = None
    volumeToConversionMap: Optional[Dict[str, Dict[str, str]]] = None
    volumeToProductCodes: Optional[Dict[str, List[ProductCodeTypeDef]]] = None
    volumeToVolumeSize: Optional[Dict[str, int]] = None

class CreateLaunchConfigurationTemplateRequestRequestTypeDef(BaseModel):
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[LicensingTypeDef] = None
    postLaunchEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class LaunchConfigurationTemplateTypeDef(BaseModel):
    arn: Optional[str] = None
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchConfigurationTemplateID: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[LicensingTypeDef] = None
    postLaunchEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class UpdateLaunchConfigurationTemplateRequestRequestTypeDef(BaseModel):
    launchConfigurationTemplateID: str
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[LicensingTypeDef] = None
    postLaunchEnabled: Optional[bool] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class CreateReplicationConfigurationTemplateRequestRequestTypeDef(BaseModel):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    pitPolicy: Sequence[PITPolicyRuleTypeDef]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: Sequence[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Mapping[str, str]
    useDedicatedReplicationServer: bool
    autoReplicateNewDisks: Optional[bool] = None
    ebsEncryptionKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ReplicationConfigurationTemplateResponseTypeDef(BaseModel):
    arn: str
    associateDefaultSecurityGroup: bool
    autoReplicateNewDisks: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    pitPolicy: List[PITPolicyRuleTypeDef]
    replicationConfigurationTemplateID: str
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    tags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationTemplateTypeDef(BaseModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[       ReplicationConfigurationDefaultLargeStagingDiskTypeType     ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    pitPolicy: Optional[List[PITPolicyRuleTypeDef]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[List[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None

class UpdateReplicationConfigurationTemplateRequestRequestTypeDef(BaseModel):
    replicationConfigurationTemplateID: str
    arn: Optional[str] = None
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[       ReplicationConfigurationDefaultLargeStagingDiskTypeType     ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    pitPolicy: Optional[Sequence[PITPolicyRuleTypeDef]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None

class DataReplicationInitiationTypeDef(BaseModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStepTypeDef]] = None

class DescribeJobLogItemsRequestDescribeJobLogItemsPaginateTypeDef(BaseModel):
    jobID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchConfigurationTemplatesRequestDescribeLaunchConfigurationTemplatesPaginateTypeDef(BaseModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationConfigurationTemplatesRequestDescribeReplicationConfigurationTemplatesPaginateTypeDef(BaseModel):
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExtensibleSourceServersRequestListExtensibleSourceServersPaginateTypeDef(BaseModel):
    stagingAccountID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStagingAccountsRequestListStagingAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestDescribeJobsPaginateTypeDef(BaseModel):
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestRequestTypeDef(BaseModel):
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeRecoveryInstancesRequestDescribeRecoveryInstancesPaginateTypeDef(BaseModel):
    filters: Optional[DescribeRecoveryInstancesRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRecoveryInstancesRequestRequestTypeDef(BaseModel):
    filters: Optional[DescribeRecoveryInstancesRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeRecoverySnapshotsRequestDescribeRecoverySnapshotsPaginateTypeDef(BaseModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFiltersTypeDef] = None
    order: Optional[RecoverySnapshotsOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRecoverySnapshotsRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    order: Optional[RecoverySnapshotsOrderType] = None

class DescribeRecoverySnapshotsResponseTypeDef(BaseModel):
    items: List[RecoverySnapshotTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceNetworksRequestDescribeSourceNetworksPaginateTypeDef(BaseModel):
    filters: Optional[DescribeSourceNetworksRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceNetworksRequestRequestTypeDef(BaseModel):
    filters: Optional[DescribeSourceNetworksRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeSourceServersRequestDescribeSourceServersPaginateTypeDef(BaseModel):
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceServersRequestRequestTypeDef(BaseModel):
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class EventResourceDataTypeDef(BaseModel):
    sourceNetworkData: Optional[SourceNetworkDataTypeDef] = None

class LaunchActionTypeDef(BaseModel):
    actionCode: Optional[str] = None
    actionId: Optional[str] = None
    actionVersion: Optional[str] = None
    active: Optional[bool] = None
    category: Optional[LaunchActionCategoryType] = None
    description: Optional[str] = None
    name: Optional[str] = None
    optional: Optional[bool] = None
    order: Optional[int] = None
    parameters: Optional[Dict[str, LaunchActionParameterTypeDef]] = None
    type: Optional[LaunchActionTypeType] = None

class PutLaunchActionRequestRequestTypeDef(BaseModel):
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
    parameters: Optional[Mapping[str, LaunchActionParameterTypeDef]] = None

class PutLaunchActionResponseTypeDef(BaseModel):
    actionCode: str
    actionId: str
    actionVersion: str
    active: bool
    category: LaunchActionCategoryType
    description: str
    name: str
    optional: bool
    order: int
    parameters: Dict[str, LaunchActionParameterTypeDef]
    resourceId: str
    type: LaunchActionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchActionsRequestListLaunchActionsPaginateTypeDef(BaseModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchActionsRequestRequestTypeDef(BaseModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class LaunchConfigurationTypeDef(BaseModel):
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    launchDisposition: LaunchDispositionType
    launchIntoInstanceProperties: LaunchIntoInstancePropertiesTypeDef
    licensing: LicensingTypeDef
    name: str
    postLaunchEnabled: bool
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoInstanceProperties: Optional[LaunchIntoInstancePropertiesTypeDef] = None
    licensing: Optional[LicensingTypeDef] = None
    name: Optional[str] = None
    postLaunchEnabled: Optional[bool] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class LifeCycleLastLaunchTypeDef(BaseModel):
    initiated: Optional[LifeCycleLastLaunchInitiatedTypeDef] = None
    status: Optional[LaunchStatusType] = None

class ListExtensibleSourceServersResponseTypeDef(BaseModel):
    items: List[StagingSourceServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourcePropertiesTypeDef(BaseModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[DiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None
    supportsNitroInstances: Optional[bool] = None

class ParticipatingResourceTypeDef(BaseModel):
    launchStatus: Optional[LaunchStatusType] = None
    participatingResourceID: Optional[ParticipatingResourceIDTypeDef] = None

class RecoveryInstanceDataReplicationInitiationTypeDef(BaseModel):
    startDateTime: Optional[str] = None
    steps: Optional[List[RecoveryInstanceDataReplicationInitiationStepTypeDef]] = None

class RecoveryInstancePropertiesTypeDef(BaseModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[RecoveryInstanceDiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None

class SourceNetworkTypeDef(BaseModel):
    arn: Optional[str] = None
    cfnStackName: Optional[str] = None
    lastRecovery: Optional[RecoveryLifeCycleTypeDef] = None
    launchedVpcID: Optional[str] = None
    replicationStatus: Optional[ReplicationStatusType] = None
    replicationStatusDetails: Optional[str] = None
    sourceAccountID: Optional[str] = None
    sourceNetworkID: Optional[str] = None
    sourceRegion: Optional[str] = None
    sourceVpcID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ReplicationConfigurationTypeDef(BaseModel):
    associateDefaultSecurityGroup: bool
    autoReplicateNewDisks: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    name: str
    pitPolicy: List[PITPolicyRuleTypeDef]
    replicatedDisks: List[ReplicationConfigurationReplicatedDiskTypeDef]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    sourceServerID: str
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationConfigurationRequestRequestTypeDef(BaseModel):
    sourceServerID: str
    associateDefaultSecurityGroup: Optional[bool] = None
    autoReplicateNewDisks: Optional[bool] = None
    bandwidthThrottling: Optional[int] = None
    createPublicIP: Optional[bool] = None
    dataPlaneRouting: Optional[ReplicationConfigurationDataPlaneRoutingType] = None
    defaultLargeStagingDiskType: Optional[       ReplicationConfigurationDefaultLargeStagingDiskTypeType     ] = None
    ebsEncryption: Optional[ReplicationConfigurationEbsEncryptionType] = None
    ebsEncryptionKeyArn: Optional[str] = None
    name: Optional[str] = None
    pitPolicy: Optional[Sequence[PITPolicyRuleTypeDef]] = None
    replicatedDisks: Optional[Sequence[ReplicationConfigurationReplicatedDiskTypeDef]] = None
    replicationServerInstanceType: Optional[str] = None
    replicationServersSecurityGroupsIDs: Optional[Sequence[str]] = None
    stagingAreaSubnetId: Optional[str] = None
    stagingAreaTags: Optional[Mapping[str, str]] = None
    useDedicatedReplicationServer: Optional[bool] = None

class StartRecoveryRequestRequestTypeDef(BaseModel):
    sourceServers: Sequence[StartRecoveryRequestSourceServerTypeDef]
    isDrill: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class StartSourceNetworkRecoveryRequestRequestTypeDef(BaseModel):
    sourceNetworks: Sequence[StartSourceNetworkRecoveryRequestNetworkEntryTypeDef]
    deployAsNew: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class CreateLaunchConfigurationTemplateResponseTypeDef(BaseModel):
    launchConfigurationTemplate: LaunchConfigurationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchConfigurationTemplatesResponseTypeDef(BaseModel):
    items: List[LaunchConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchConfigurationTemplateResponseTypeDef(BaseModel):
    launchConfigurationTemplate: LaunchConfigurationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationConfigurationTemplatesResponseTypeDef(BaseModel):
    items: List[ReplicationConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataReplicationInfoTypeDef(BaseModel):
    dataReplicationError: Optional[DataReplicationErrorTypeDef] = None
    dataReplicationInitiation: Optional[DataReplicationInitiationTypeDef] = None
    dataReplicationState: Optional[DataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    replicatedDisks: Optional[List[DataReplicationInfoReplicatedDiskTypeDef]] = None
    stagingAvailabilityZone: Optional[str] = None
    stagingOutpostArn: Optional[str] = None

class JobLogEventDataTypeDef(BaseModel):
    conversionProperties: Optional[ConversionPropertiesTypeDef] = None
    conversionServerID: Optional[str] = None
    eventResourceData: Optional[EventResourceDataTypeDef] = None
    rawError: Optional[str] = None
    sourceServerID: Optional[str] = None
    targetInstanceID: Optional[str] = None

class LaunchActionRunTypeDef(BaseModel):
    action: Optional[LaunchActionTypeDef] = None
    failureReason: Optional[str] = None
    runId: Optional[str] = None
    status: Optional[LaunchActionRunStatusType] = None

class ListLaunchActionsResponseTypeDef(BaseModel):
    items: List[LaunchActionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifeCycleTypeDef(BaseModel):
    addedToServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    firstByteDateTime: Optional[str] = None
    lastLaunch: Optional[LifeCycleLastLaunchTypeDef] = None
    lastSeenByServiceDateTime: Optional[str] = None

class RecoveryInstanceDataReplicationInfoTypeDef(BaseModel):
    dataReplicationError: Optional[RecoveryInstanceDataReplicationErrorTypeDef] = None
    dataReplicationInitiation: Optional[RecoveryInstanceDataReplicationInitiationTypeDef] = None
    dataReplicationState: Optional[RecoveryInstanceDataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    replicatedDisks: Optional[       List[RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef]     ] = None
    stagingAvailabilityZone: Optional[str] = None
    stagingOutpostArn: Optional[str] = None

class DescribeSourceNetworksResponseTypeDef(BaseModel):
    items: List[SourceNetworkTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSourceNetworkReplicationResponseTypeDef(BaseModel):
    sourceNetwork: SourceNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopSourceNetworkReplicationResponseTypeDef(BaseModel):
    sourceNetwork: SourceNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobLogTypeDef(BaseModel):
    event: Optional[JobLogEventType] = None
    eventData: Optional[JobLogEventDataTypeDef] = None
    logDateTime: Optional[str] = None

class LaunchActionsStatusTypeDef(BaseModel):
    runs: Optional[List[LaunchActionRunTypeDef]] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None

class SourceServerResponseTypeDef(BaseModel):
    agentVersion: str
    arn: str
    dataReplicationInfo: DataReplicationInfoTypeDef
    lastLaunchResult: LastLaunchResultType
    lifeCycle: LifeCycleTypeDef
    recoveryInstanceId: str
    replicationDirection: ReplicationDirectionType
    reversedDirectionSourceServerArn: str
    sourceCloudProperties: SourceCloudPropertiesTypeDef
    sourceNetworkID: str
    sourceProperties: SourcePropertiesTypeDef
    sourceServerID: str
    stagingArea: StagingAreaTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SourceServerTypeDef(BaseModel):
    agentVersion: Optional[str] = None
    arn: Optional[str] = None
    dataReplicationInfo: Optional[DataReplicationInfoTypeDef] = None
    lastLaunchResult: Optional[LastLaunchResultType] = None
    lifeCycle: Optional[LifeCycleTypeDef] = None
    recoveryInstanceId: Optional[str] = None
    replicationDirection: Optional[ReplicationDirectionType] = None
    reversedDirectionSourceServerArn: Optional[str] = None
    sourceCloudProperties: Optional[SourceCloudPropertiesTypeDef] = None
    sourceNetworkID: Optional[str] = None
    sourceProperties: Optional[SourcePropertiesTypeDef] = None
    sourceServerID: Optional[str] = None
    stagingArea: Optional[StagingAreaTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class RecoveryInstanceTypeDef(BaseModel):
    agentVersion: Optional[str] = None
    arn: Optional[str] = None
    dataReplicationInfo: Optional[RecoveryInstanceDataReplicationInfoTypeDef] = None
    ec2InstanceID: Optional[str] = None
    ec2InstanceState: Optional[EC2InstanceStateType] = None
    failback: Optional[RecoveryInstanceFailbackTypeDef] = None
    isDrill: Optional[bool] = None
    jobID: Optional[str] = None
    originAvailabilityZone: Optional[str] = None
    originEnvironment: Optional[OriginEnvironmentType] = None
    pointInTimeSnapshotDateTime: Optional[str] = None
    recoveryInstanceID: Optional[str] = None
    recoveryInstanceProperties: Optional[RecoveryInstancePropertiesTypeDef] = None
    sourceOutpostArn: Optional[str] = None
    sourceServerID: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class DescribeJobLogItemsResponseTypeDef(BaseModel):
    items: List[JobLogTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipatingServerTypeDef(BaseModel):
    launchActionsStatus: Optional[LaunchActionsStatusTypeDef] = None
    launchStatus: Optional[LaunchStatusType] = None
    recoveryInstanceID: Optional[str] = None
    sourceServerID: Optional[str] = None

class CreateExtendedSourceServerResponseTypeDef(BaseModel):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceServersResponseTypeDef(BaseModel):
    items: List[SourceServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationResponseTypeDef(BaseModel):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationResponseTypeDef(BaseModel):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecoveryInstancesResponseTypeDef(BaseModel):
    items: List[RecoveryInstanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobTypeDef(BaseModel):
    jobID: str
    arn: Optional[str] = None
    creationDateTime: Optional[str] = None
    endDateTime: Optional[str] = None
    initiatedBy: Optional[InitiatedByType] = None
    participatingResources: Optional[List[ParticipatingResourceTypeDef]] = None
    participatingServers: Optional[List[ParticipatingServerTypeDef]] = None
    status: Optional[JobStatusType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[JobTypeType] = None

class AssociateSourceNetworkStackResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobsResponseTypeDef(BaseModel):
    items: List[JobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFailbackLaunchResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRecoveryResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSourceNetworkRecoveryResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateRecoveryInstancesResponseTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

