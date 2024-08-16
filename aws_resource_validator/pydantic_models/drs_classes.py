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
from aws_resource_validator.pydantic_models.drs_constants import *

class AccountTypeDef(BaseValidatorModel):
    accountID: Optional[str] = None

class AssociateSourceNetworkStackRequestRequestTypeDef(BaseValidatorModel):
    cfnStackName: str
    sourceNetworkID: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CPUTypeDef(BaseValidatorModel):
    cores: Optional[int] = None
    modelName: Optional[str] = None

class ProductCodeTypeDef(BaseValidatorModel):
    productCodeId: Optional[str] = None
    productCodeMode: Optional[ProductCodeModeType] = None

class CreateExtendedSourceServerRequestRequestTypeDef(BaseValidatorModel):
    sourceServerArn: str
    tags: Optional[Mapping[str, str]] = None

class LicensingTypeDef(BaseValidatorModel):
    osByol: Optional[bool] = None

class PITPolicyRuleTypeDef(BaseValidatorModel):
    interval: int
    retentionDuration: int
    units: PITPolicyRuleUnitsType
    enabled: Optional[bool] = None
    ruleID: Optional[int] = None

class CreateSourceNetworkRequestRequestTypeDef(BaseValidatorModel):
    originAccountID: str
    originRegion: str
    vpcID: str
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
    volumeStatus: Optional[VolumeStatusType] = None

class DataReplicationInitiationStepTypeDef(BaseValidatorModel):
    name: Optional[DataReplicationInitiationStepNameType] = None
    status: Optional[DataReplicationInitiationStepStatusType] = None

class DeleteJobRequestRequestTypeDef(BaseValidatorModel):
    jobID: str

class DeleteLaunchActionRequestRequestTypeDef(BaseValidatorModel):
    actionId: str
    resourceId: str

class DeleteLaunchConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str

class DeleteRecoveryInstanceRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceID: str

class DeleteReplicationConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateID: str

class DeleteSourceNetworkRequestRequestTypeDef(BaseValidatorModel):
    sourceNetworkID: str

class DeleteSourceServerRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeJobLogItemsRequestRequestTypeDef(BaseValidatorModel):
    jobID: str
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

class DescribeRecoveryInstancesRequestFiltersTypeDef(BaseValidatorModel):
    recoveryInstanceIDs: Optional[Sequence[str]] = None
    sourceServerIDs: Optional[Sequence[str]] = None

class DescribeRecoverySnapshotsRequestFiltersTypeDef(BaseValidatorModel):
    fromDateTime: Optional[str] = None
    toDateTime: Optional[str] = None

class RecoverySnapshotTypeDef(BaseValidatorModel):
    expectedTimestamp: str
    snapshotID: str
    sourceServerID: str
    ebsSnapshots: Optional[List[str]] = None
    timestamp: Optional[str] = None

class DescribeReplicationConfigurationTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None

class DescribeSourceNetworksRequestFiltersTypeDef(BaseValidatorModel):
    originAccountID: Optional[str] = None
    originRegion: Optional[str] = None
    sourceNetworkIDs: Optional[Sequence[str]] = None

class DescribeSourceServersRequestFiltersTypeDef(BaseValidatorModel):
    hardwareId: Optional[str] = None
    sourceServerIDs: Optional[Sequence[str]] = None
    stagingAccountIDs: Optional[Sequence[str]] = None

class DisconnectRecoveryInstanceRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceID: str

class DisconnectSourceServerRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class DiskTypeDef(BaseValidatorModel):
    bytes: Optional[int] = None
    deviceName: Optional[str] = None

class SourceNetworkDataTypeDef(BaseValidatorModel):
    sourceNetworkID: Optional[str] = None
    sourceVpc: Optional[str] = None
    stackName: Optional[str] = None
    targetVpc: Optional[str] = None

class ExportSourceNetworkCfnTemplateRequestRequestTypeDef(BaseValidatorModel):
    sourceNetworkID: str

class GetFailbackReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceID: str

class GetLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class GetReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class IdentificationHintsTypeDef(BaseValidatorModel):
    awsInstanceID: Optional[str] = None
    fqdn: Optional[str] = None
    hostname: Optional[str] = None
    vmWareUuid: Optional[str] = None

class LaunchActionParameterTypeDef(BaseValidatorModel):
    type: Optional[LaunchActionParameterTypeType] = None
    value: Optional[str] = None

class LaunchActionsRequestFiltersTypeDef(BaseValidatorModel):
    actionIds: Optional[Sequence[str]] = None

class LaunchIntoInstancePropertiesTypeDef(BaseValidatorModel):
    launchIntoEC2InstanceID: Optional[str] = None

class LifeCycleLastLaunchInitiatedTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[str] = None
    jobID: Optional[str] = None
    type: Optional[LastLaunchTypeType] = None

class ListExtensibleSourceServersRequestRequestTypeDef(BaseValidatorModel):
    stagingAccountID: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StagingSourceServerTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    hostname: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStagingAccountsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class NetworkInterfaceTypeDef(BaseValidatorModel):
    ips: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    macAddress: Optional[str] = None

class OSTypeDef(BaseValidatorModel):
    fullString: Optional[str] = None

class ParticipatingResourceIDTypeDef(BaseValidatorModel):
    sourceNetworkID: Optional[str] = None

class RecoveryInstanceDataReplicationErrorTypeDef(BaseValidatorModel):
    error: Optional[FailbackReplicationErrorType] = None
    rawError: Optional[str] = None

class RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef(BaseValidatorModel):
    backloggedStorageBytes: Optional[int] = None
    deviceName: Optional[str] = None
    replicatedStorageBytes: Optional[int] = None
    rescannedStorageBytes: Optional[int] = None
    totalStorageBytes: Optional[int] = None

class RecoveryInstanceDataReplicationInitiationStepTypeDef(BaseValidatorModel):
    name: Optional[RecoveryInstanceDataReplicationInitiationStepNameType] = None
    status: Optional[RecoveryInstanceDataReplicationInitiationStepStatusType] = None

class RecoveryInstanceDiskTypeDef(BaseValidatorModel):
    bytes: Optional[int] = None
    ebsVolumeID: Optional[str] = None
    internalDeviceName: Optional[str] = None

class RecoveryInstanceFailbackTypeDef(BaseValidatorModel):
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

class RecoveryLifeCycleTypeDef(BaseValidatorModel):
    apiCallDateTime: Optional[datetime] = None
    jobID: Optional[str] = None
    lastRecoveryResult: Optional[RecoveryResultType] = None

class ReplicationConfigurationReplicatedDiskTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    iops: Optional[int] = None
    isBootDisk: Optional[bool] = None
    optimizedStagingDiskType: Optional[       ReplicationConfigurationReplicatedDiskStagingDiskTypeType     ] = None
    stagingDiskType: Optional[ReplicationConfigurationReplicatedDiskStagingDiskTypeType] = None
    throughput: Optional[int] = None

class RetryDataReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class ReverseReplicationRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceID: str

class SourceCloudPropertiesTypeDef(BaseValidatorModel):
    originAccountID: Optional[str] = None
    originAvailabilityZone: Optional[str] = None
    originRegion: Optional[str] = None
    sourceOutpostArn: Optional[str] = None

class StagingAreaTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    stagingAccountID: Optional[str] = None
    stagingSourceServerArn: Optional[str] = None
    status: Optional[ExtensionStatusType] = None

class StartFailbackLaunchRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceIDs: Sequence[str]
    tags: Optional[Mapping[str, str]] = None

class StartRecoveryRequestSourceServerTypeDef(BaseValidatorModel):
    sourceServerID: str
    recoverySnapshotID: Optional[str] = None

class StartReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class StartSourceNetworkRecoveryRequestNetworkEntryTypeDef(BaseValidatorModel):
    sourceNetworkID: str
    cfnStackName: Optional[str] = None

class StartSourceNetworkReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceNetworkID: str

class StopFailbackRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceID: str

class StopReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str

class StopSourceNetworkReplicationRequestRequestTypeDef(BaseValidatorModel):
    sourceNetworkID: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateRecoveryInstancesRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceIDs: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateFailbackReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    recoveryInstanceID: str
    bandwidthThrottling: Optional[int] = None
    name: Optional[str] = None
    usePrivateIP: Optional[bool] = None

class CreateSourceNetworkResponseTypeDef(BaseValidatorModel):
    sourceNetworkID: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSourceNetworkCfnTemplateResponseTypeDef(BaseValidatorModel):
    s3DestinationUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFailbackReplicationConfigurationResponseTypeDef(BaseValidatorModel):
    bandwidthThrottling: int
    name: str
    recoveryInstanceID: str
    usePrivateIP: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListStagingAccountsResponseTypeDef(BaseValidatorModel):
    accounts: List[AccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReverseReplicationResponseTypeDef(BaseValidatorModel):
    reversedDirectionSourceServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConversionPropertiesTypeDef(BaseValidatorModel):
    dataTimestamp: Optional[str] = None
    forceUefi: Optional[bool] = None
    rootVolumeName: Optional[str] = None
    volumeToConversionMap: Optional[Dict[str, Dict[str, str]]] = None
    volumeToProductCodes: Optional[Dict[str, List[ProductCodeTypeDef]]] = None
    volumeToVolumeSize: Optional[Dict[str, int]] = None

class CreateLaunchConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[LicensingTypeDef] = None
    postLaunchEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class LaunchConfigurationTemplateTypeDef(BaseValidatorModel):
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

class UpdateLaunchConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
    launchConfigurationTemplateID: str
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    exportBucketArn: Optional[str] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoSourceInstance: Optional[bool] = None
    licensing: Optional[LicensingTypeDef] = None
    postLaunchEnabled: Optional[bool] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class CreateReplicationConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class ReplicationConfigurationTemplateResponseTypeDef(BaseValidatorModel):
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

class ReplicationConfigurationTemplateTypeDef(BaseValidatorModel):
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

class UpdateReplicationConfigurationTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class DataReplicationInitiationTypeDef(BaseValidatorModel):
    nextAttemptDateTime: Optional[str] = None
    startDateTime: Optional[str] = None
    steps: Optional[List[DataReplicationInitiationStepTypeDef]] = None

class DescribeJobLogItemsRequestDescribeJobLogItemsPaginateTypeDef(BaseValidatorModel):
    jobID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchConfigurationTemplatesRequestDescribeLaunchConfigurationTemplatesPaginateTypeDef(BaseValidatorModel):
    launchConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationConfigurationTemplatesRequestDescribeReplicationConfigurationTemplatesPaginateTypeDef(BaseValidatorModel):
    replicationConfigurationTemplateIDs: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExtensibleSourceServersRequestListExtensibleSourceServersPaginateTypeDef(BaseValidatorModel):
    stagingAccountID: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStagingAccountsRequestListStagingAccountsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestDescribeJobsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[DescribeJobsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeRecoveryInstancesRequestDescribeRecoveryInstancesPaginateTypeDef(BaseValidatorModel):
    filters: Optional[DescribeRecoveryInstancesRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRecoveryInstancesRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[DescribeRecoveryInstancesRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeRecoverySnapshotsRequestDescribeRecoverySnapshotsPaginateTypeDef(BaseValidatorModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFiltersTypeDef] = None
    order: Optional[RecoverySnapshotsOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRecoverySnapshotsRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    filters: Optional[DescribeRecoverySnapshotsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    order: Optional[RecoverySnapshotsOrderType] = None

class DescribeRecoverySnapshotsResponseTypeDef(BaseValidatorModel):
    items: List[RecoverySnapshotTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceNetworksRequestDescribeSourceNetworksPaginateTypeDef(BaseValidatorModel):
    filters: Optional[DescribeSourceNetworksRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceNetworksRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[DescribeSourceNetworksRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeSourceServersRequestDescribeSourceServersPaginateTypeDef(BaseValidatorModel):
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceServersRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[DescribeSourceServersRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class EventResourceDataTypeDef(BaseValidatorModel):
    sourceNetworkData: Optional[SourceNetworkDataTypeDef] = None

class LaunchActionTypeDef(BaseValidatorModel):
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

class PutLaunchActionRequestRequestTypeDef(BaseValidatorModel):
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

class PutLaunchActionResponseTypeDef(BaseValidatorModel):
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

class ListLaunchActionsRequestListLaunchActionsPaginateTypeDef(BaseValidatorModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchActionsRequestRequestTypeDef(BaseValidatorModel):
    resourceId: str
    filters: Optional[LaunchActionsRequestFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class LaunchConfigurationTypeDef(BaseValidatorModel):
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

class UpdateLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
    sourceServerID: str
    copyPrivateIp: Optional[bool] = None
    copyTags: Optional[bool] = None
    launchDisposition: Optional[LaunchDispositionType] = None
    launchIntoInstanceProperties: Optional[LaunchIntoInstancePropertiesTypeDef] = None
    licensing: Optional[LicensingTypeDef] = None
    name: Optional[str] = None
    postLaunchEnabled: Optional[bool] = None
    targetInstanceTypeRightSizingMethod: Optional[TargetInstanceTypeRightSizingMethodType] = None

class LifeCycleLastLaunchTypeDef(BaseValidatorModel):
    initiated: Optional[LifeCycleLastLaunchInitiatedTypeDef] = None
    status: Optional[LaunchStatusType] = None

class ListExtensibleSourceServersResponseTypeDef(BaseValidatorModel):
    items: List[StagingSourceServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourcePropertiesTypeDef(BaseValidatorModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[DiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None
    recommendedInstanceType: Optional[str] = None
    supportsNitroInstances: Optional[bool] = None

class ParticipatingResourceTypeDef(BaseValidatorModel):
    launchStatus: Optional[LaunchStatusType] = None
    participatingResourceID: Optional[ParticipatingResourceIDTypeDef] = None

class RecoveryInstanceDataReplicationInitiationTypeDef(BaseValidatorModel):
    startDateTime: Optional[str] = None
    steps: Optional[List[RecoveryInstanceDataReplicationInitiationStepTypeDef]] = None

class RecoveryInstancePropertiesTypeDef(BaseValidatorModel):
    cpus: Optional[List[CPUTypeDef]] = None
    disks: Optional[List[RecoveryInstanceDiskTypeDef]] = None
    identificationHints: Optional[IdentificationHintsTypeDef] = None
    lastUpdatedDateTime: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    os: Optional[OSTypeDef] = None
    ramBytes: Optional[int] = None

class SourceNetworkTypeDef(BaseValidatorModel):
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

class ReplicationConfigurationTypeDef(BaseValidatorModel):
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

class UpdateReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class StartRecoveryRequestRequestTypeDef(BaseValidatorModel):
    sourceServers: Sequence[StartRecoveryRequestSourceServerTypeDef]
    isDrill: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class StartSourceNetworkRecoveryRequestRequestTypeDef(BaseValidatorModel):
    sourceNetworks: Sequence[StartSourceNetworkRecoveryRequestNetworkEntryTypeDef]
    deployAsNew: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class CreateLaunchConfigurationTemplateResponseTypeDef(BaseValidatorModel):
    launchConfigurationTemplate: LaunchConfigurationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    items: List[LaunchConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchConfigurationTemplateResponseTypeDef(BaseValidatorModel):
    launchConfigurationTemplate: LaunchConfigurationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    items: List[ReplicationConfigurationTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataReplicationInfoTypeDef(BaseValidatorModel):
    dataReplicationError: Optional[DataReplicationErrorTypeDef] = None
    dataReplicationInitiation: Optional[DataReplicationInitiationTypeDef] = None
    dataReplicationState: Optional[DataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    replicatedDisks: Optional[List[DataReplicationInfoReplicatedDiskTypeDef]] = None
    stagingAvailabilityZone: Optional[str] = None
    stagingOutpostArn: Optional[str] = None

class JobLogEventDataTypeDef(BaseValidatorModel):
    conversionProperties: Optional[ConversionPropertiesTypeDef] = None
    conversionServerID: Optional[str] = None
    eventResourceData: Optional[EventResourceDataTypeDef] = None
    rawError: Optional[str] = None
    sourceServerID: Optional[str] = None
    targetInstanceID: Optional[str] = None

class LaunchActionRunTypeDef(BaseValidatorModel):
    action: Optional[LaunchActionTypeDef] = None
    failureReason: Optional[str] = None
    runId: Optional[str] = None
    status: Optional[LaunchActionRunStatusType] = None

class ListLaunchActionsResponseTypeDef(BaseValidatorModel):
    items: List[LaunchActionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifeCycleTypeDef(BaseValidatorModel):
    addedToServiceDateTime: Optional[str] = None
    elapsedReplicationDuration: Optional[str] = None
    firstByteDateTime: Optional[str] = None
    lastLaunch: Optional[LifeCycleLastLaunchTypeDef] = None
    lastSeenByServiceDateTime: Optional[str] = None

class RecoveryInstanceDataReplicationInfoTypeDef(BaseValidatorModel):
    dataReplicationError: Optional[RecoveryInstanceDataReplicationErrorTypeDef] = None
    dataReplicationInitiation: Optional[RecoveryInstanceDataReplicationInitiationTypeDef] = None
    dataReplicationState: Optional[RecoveryInstanceDataReplicationStateType] = None
    etaDateTime: Optional[str] = None
    lagDuration: Optional[str] = None
    replicatedDisks: Optional[       List[RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef]     ] = None
    stagingAvailabilityZone: Optional[str] = None
    stagingOutpostArn: Optional[str] = None

class DescribeSourceNetworksResponseTypeDef(BaseValidatorModel):
    items: List[SourceNetworkTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSourceNetworkReplicationResponseTypeDef(BaseValidatorModel):
    sourceNetwork: SourceNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopSourceNetworkReplicationResponseTypeDef(BaseValidatorModel):
    sourceNetwork: SourceNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobLogTypeDef(BaseValidatorModel):
    event: Optional[JobLogEventType] = None
    eventData: Optional[JobLogEventDataTypeDef] = None
    logDateTime: Optional[str] = None

class LaunchActionsStatusTypeDef(BaseValidatorModel):
    runs: Optional[List[LaunchActionRunTypeDef]] = None
    ssmAgentDiscoveryDatetime: Optional[str] = None

class SourceServerResponseTypeDef(BaseValidatorModel):
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

class SourceServerTypeDef(BaseValidatorModel):
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

class RecoveryInstanceTypeDef(BaseValidatorModel):
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

class DescribeJobLogItemsResponseTypeDef(BaseValidatorModel):
    items: List[JobLogTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipatingServerTypeDef(BaseValidatorModel):
    launchActionsStatus: Optional[LaunchActionsStatusTypeDef] = None
    launchStatus: Optional[LaunchStatusType] = None
    recoveryInstanceID: Optional[str] = None
    sourceServerID: Optional[str] = None

class CreateExtendedSourceServerResponseTypeDef(BaseValidatorModel):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceServersResponseTypeDef(BaseValidatorModel):
    items: List[SourceServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationResponseTypeDef(BaseValidatorModel):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationResponseTypeDef(BaseValidatorModel):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecoveryInstancesResponseTypeDef(BaseValidatorModel):
    items: List[RecoveryInstanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobTypeDef(BaseValidatorModel):
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

class AssociateSourceNetworkStackResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobsResponseTypeDef(BaseValidatorModel):
    items: List[JobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFailbackLaunchResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRecoveryResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSourceNetworkRecoveryResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateRecoveryInstancesResponseTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

