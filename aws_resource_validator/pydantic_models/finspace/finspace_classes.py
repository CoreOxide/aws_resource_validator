from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.finspace.finspace_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AutoScalingConfiguration(BaseValidatorModel):
    minNodeCount: Optional[int] = None
    maxNodeCount: Optional[int] = None
    autoScalingMetric: Optional[Literal['CPU_UTILIZATION_PERCENTAGE']] = None
    metricTarget: Optional[float] = None
    scaleInCooldownSeconds: Optional[float] = None
    scaleOutCooldownSeconds: Optional[float] = None


class CapacityConfiguration(BaseValidatorModel):
    nodeType: Optional[str] = None
    nodeCount: Optional[int] = None


class ChangeRequest(BaseValidatorModel):
    changeType: ChangeTypeType
    dbPath: str
    s3Path: Optional[str] = None


class CodeConfiguration(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    s3ObjectVersion: Optional[str] = None


class SuperuserParameters(BaseValidatorModel):
    emailAddress: str
    firstName: str
    lastName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ErrorInfo(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorType: Optional[ErrorDetailsType] = None


class KxCacheStorageConfiguration(BaseValidatorModel):
    type: str
    size: int


class KxCommandLineArgument(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class KxSavedownStorageConfiguration(BaseValidatorModel):
    type: Optional[Literal['SDS01']] = None
    size: Optional[int] = None
    volumeName: Optional[str] = None


class KxScalingGroupConfiguration(BaseValidatorModel):
    scalingGroupName: str
    memoryReservation: int
    nodeCount: int
    memoryLimit: Optional[int] = None
    cpu: Optional[float] = None


class TickerplantLogConfigurationOutput(BaseValidatorModel):
    tickerplantLogVolumes: Optional[List[str]] = None


class Volume(BaseValidatorModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal['NAS_1']] = None


class VpcConfigurationOutput(BaseValidatorModel):
    vpcId: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    ipAddressType: Optional[Literal['IP_V4']] = None


class CreateKxDatabaseRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class KxDataviewSegmentConfigurationOutput(BaseValidatorModel):
    dbPaths: List[str]
    volumeName: str
    onDemand: Optional[bool] = None


class CreateKxEnvironmentRequest(BaseValidatorModel):
    name: str
    kmsKeyId: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


class CreateKxScalingGroupRequest(BaseValidatorModel):
    clientToken: str
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    tags: Optional[Dict[str, str]] = None


class CreateKxUserRequest(BaseValidatorModel):
    environmentId: str
    userName: str
    iamRole: str
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


class KxNAS1Configuration(BaseValidatorModel):
    type: Optional[KxNAS1TypeType] = None
    size: Optional[int] = None


class CustomDNSServer(BaseValidatorModel):
    customDNSServerName: str
    customDNSServerIP: str


class DeleteEnvironmentRequest(BaseValidatorModel):
    environmentId: str


class DeleteKxClusterNodeRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str
    nodeId: str


class DeleteKxClusterRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str
    clientToken: Optional[str] = None


class DeleteKxDatabaseRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str


class DeleteKxDataviewRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str


class DeleteKxEnvironmentRequest(BaseValidatorModel):
    environmentId: str
    clientToken: Optional[str] = None


class DeleteKxScalingGroupRequest(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str
    clientToken: Optional[str] = None


class DeleteKxUserRequest(BaseValidatorModel):
    userName: str
    environmentId: str
    clientToken: Optional[str] = None


class DeleteKxVolumeRequest(BaseValidatorModel):
    environmentId: str
    volumeName: str
    clientToken: Optional[str] = None


class FederationParametersOutput(BaseValidatorModel):
    samlMetadataDocument: Optional[str] = None
    samlMetadataURL: Optional[str] = None
    applicationCallBackURL: Optional[str] = None
    federationURN: Optional[str] = None
    federationProviderName: Optional[str] = None
    attributeMap: Optional[Dict[str, str]] = None


class FederationParameters(BaseValidatorModel):
    samlMetadataDocument: Optional[str] = None
    samlMetadataURL: Optional[str] = None
    applicationCallBackURL: Optional[str] = None
    federationURN: Optional[str] = None
    federationProviderName: Optional[str] = None
    attributeMap: Optional[Dict[str, str]] = None


class GetEnvironmentRequest(BaseValidatorModel):
    environmentId: str


class GetKxChangesetRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    changesetId: str


class GetKxClusterRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str


class GetKxConnectionStringRequest(BaseValidatorModel):
    userArn: str
    environmentId: str
    clusterName: str


class GetKxDatabaseRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str


class GetKxDataviewRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str


class GetKxEnvironmentRequest(BaseValidatorModel):
    environmentId: str


class GetKxScalingGroupRequest(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str


class GetKxUserRequest(BaseValidatorModel):
    userName: str
    environmentId: str


class GetKxVolumeRequest(BaseValidatorModel):
    environmentId: str
    volumeName: str


class KxAttachedCluster(BaseValidatorModel):
    clusterName: Optional[str] = None
    clusterType: Optional[KxClusterTypeType] = None
    clusterStatus: Optional[KxClusterStatusType] = None


class IcmpTypeCode(BaseValidatorModel):
    type: int
    code: int


class KxChangesetListEntry(BaseValidatorModel):
    changesetId: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    activeFromTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None
    status: Optional[ChangesetStatusType] = None


class KxClusterCodeDeploymentConfiguration(BaseValidatorModel):
    deploymentStrategy: KxClusterCodeDeploymentStrategyType


class KxDatabaseCacheConfigurationOutput(BaseValidatorModel):
    cacheType: str
    dbPaths: List[str]
    dataviewName: Optional[str] = None


class KxDatabaseCacheConfiguration(BaseValidatorModel):
    cacheType: str
    dbPaths: List[str]
    dataviewName: Optional[str] = None


class KxDatabaseListEntry(BaseValidatorModel):
    databaseName: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None


class KxDataviewSegmentConfiguration(BaseValidatorModel):
    dbPaths: List[str]
    volumeName: str
    onDemand: Optional[bool] = None


class KxDeploymentConfiguration(BaseValidatorModel):
    deploymentStrategy: KxDeploymentStrategyType


class KxNode(BaseValidatorModel):
    nodeId: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    launchTime: Optional[datetime] = None
    status: Optional[KxNodeStatusType] = None


class KxScalingGroup(BaseValidatorModel):
    scalingGroupName: Optional[str] = None
    hostType: Optional[str] = None
    clusters: Optional[List[str]] = None
    availabilityZoneId: Optional[str] = None
    status: Optional[KxScalingGroupStatusType] = None
    statusReason: Optional[str] = None
    lastModifiedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None


class KxUser(BaseValidatorModel):
    userArn: Optional[str] = None
    userName: Optional[str] = None
    iamRole: Optional[str] = None
    createTimestamp: Optional[datetime] = None
    updateTimestamp: Optional[datetime] = None


class KxVolume(BaseValidatorModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal['NAS_1']] = None
    status: Optional[KxVolumeStatusType] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneIds: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None


class ListEnvironmentsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxChangesetsRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxClusterNodesRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxClustersRequest(BaseValidatorModel):
    environmentId: str
    clusterType: Optional[KxClusterTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKxDatabasesRequest(BaseValidatorModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxDataviewsRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListKxEnvironmentsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxScalingGroupsRequest(BaseValidatorModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKxUsersRequest(BaseValidatorModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxVolumesRequest(BaseValidatorModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    volumeType: Optional[Literal['NAS_1']] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PortRange(BaseValidatorModel):
    from_: int
    to: int


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TickerplantLogConfiguration(BaseValidatorModel):
    tickerplantLogVolumes: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateKxDatabaseRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None


class UpdateKxEnvironmentRequest(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateKxUserRequest(BaseValidatorModel):
    environmentId: str
    userName: str
    iamRole: str
    clientToken: Optional[str] = None


class VpcConfiguration(BaseValidatorModel):
    vpcId: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    ipAddressType: Optional[Literal['IP_V4']] = None


class CreateKxChangesetRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    changeRequests: List[ChangeRequest]
    clientToken: str


class CreateEnvironmentResponse(BaseValidatorModel):
    environmentId: str
    environmentArn: str
    environmentUrl: str
    ResponseMetadata: ResponseMetadata


class CreateKxDatabaseResponse(BaseValidatorModel):
    databaseName: str
    databaseArn: str
    environmentId: str
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateKxEnvironmentResponse(BaseValidatorModel):
    name: str
    status: EnvironmentStatusType
    environmentId: str
    description: str
    environmentArn: str
    kmsKeyId: str
    creationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateKxScalingGroupResponse(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    status: KxScalingGroupStatusType
    lastModifiedTimestamp: datetime
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateKxUserResponse(BaseValidatorModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadata


class GetKxConnectionStringResponse(BaseValidatorModel):
    signedConnectionString: str
    ResponseMetadata: ResponseMetadata


class GetKxDatabaseResponse(BaseValidatorModel):
    databaseName: str
    databaseArn: str
    environmentId: str
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    lastCompletedChangesetId: str
    numBytes: int
    numChangesets: int
    numFiles: int
    ResponseMetadata: ResponseMetadata


class GetKxScalingGroupResponse(BaseValidatorModel):
    scalingGroupName: str
    scalingGroupArn: str
    hostType: str
    clusters: List[str]
    availabilityZoneId: str
    status: KxScalingGroupStatusType
    statusReason: str
    lastModifiedTimestamp: datetime
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetKxUserResponse(BaseValidatorModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateKxDatabaseResponse(BaseValidatorModel):
    databaseName: str
    environmentId: str
    description: str
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class UpdateKxUserResponse(BaseValidatorModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadata


class CreateKxChangesetResponse(BaseValidatorModel):
    changesetId: str
    databaseName: str
    environmentId: str
    changeRequests: List[ChangeRequest]
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: ChangesetStatusType
    errorInfo: ErrorInfo
    ResponseMetadata: ResponseMetadata


class GetKxChangesetResponse(BaseValidatorModel):
    changesetId: str
    databaseName: str
    environmentId: str
    changeRequests: List[ChangeRequest]
    createdTimestamp: datetime
    activeFromTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: ChangesetStatusType
    errorInfo: ErrorInfo
    ResponseMetadata: ResponseMetadata


class KxCluster(BaseValidatorModel):
    status: Optional[KxClusterStatusType] = None
    statusReason: Optional[str] = None
    clusterName: Optional[str] = None
    clusterType: Optional[KxClusterTypeType] = None
    clusterDescription: Optional[str] = None
    releaseLabel: Optional[str] = None
    volumes: Optional[List[Volume]] = None
    initializationScript: Optional[str] = None
    executionRole: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneId: Optional[str] = None
    lastModifiedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None


class CreateKxDataviewResponse(BaseValidatorModel):
    dataviewName: str
    databaseName: str
    environmentId: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationOutput]
    description: str
    autoUpdate: bool
    readWrite: bool
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: KxDataviewStatusType
    ResponseMetadata: ResponseMetadata


class KxDataviewActiveVersion(BaseValidatorModel):
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationOutput]] = None
    attachedClusters: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    versionId: Optional[str] = None


class KxDataviewConfigurationOutput(BaseValidatorModel):
    dataviewName: Optional[str] = None
    dataviewVersionId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationOutput]] = None


class CreateKxVolumeRequest(BaseValidatorModel):
    environmentId: str
    volumeType: Literal['NAS_1']
    volumeName: str
    azMode: KxAzModeType
    availabilityZoneIds: List[str]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    nas1Configuration: Optional[KxNAS1Configuration] = None
    tags: Optional[Dict[str, str]] = None


class CreateKxVolumeResponse(BaseValidatorModel):
    environmentId: str
    volumeName: str
    volumeType: Literal['NAS_1']
    volumeArn: str
    nas1Configuration: KxNAS1Configuration
    status: KxVolumeStatusType
    statusReason: str
    azMode: KxAzModeType
    description: str
    availabilityZoneIds: List[str]
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class UpdateKxVolumeRequest(BaseValidatorModel):
    environmentId: str
    volumeName: str
    description: Optional[str] = None
    clientToken: Optional[str] = None
    nas1Configuration: Optional[KxNAS1Configuration] = None


class Environment(BaseValidatorModel):
    name: Optional[str] = None
    environmentId: Optional[str] = None
    awsAccountId: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None
    environmentUrl: Optional[str] = None
    description: Optional[str] = None
    environmentArn: Optional[str] = None
    sageMakerStudioDomainUrl: Optional[str] = None
    kmsKeyId: Optional[str] = None
    dedicatedServiceAccountId: Optional[str] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersOutput] = None

FederationParametersUnion = Union[FederationParameters, FederationParametersOutput]


class GetKxVolumeResponse(BaseValidatorModel):
    environmentId: str
    volumeName: str
    volumeType: Literal['NAS_1']
    volumeArn: str
    nas1Configuration: KxNAS1Configuration
    status: KxVolumeStatusType
    statusReason: str
    createdTimestamp: datetime
    description: str
    azMode: KxAzModeType
    availabilityZoneIds: List[str]
    lastModifiedTimestamp: datetime
    attachedClusters: List[KxAttachedCluster]
    ResponseMetadata: ResponseMetadata


class UpdateKxVolumeResponse(BaseValidatorModel):
    environmentId: str
    volumeName: str
    volumeType: Literal['NAS_1']
    volumeArn: str
    nas1Configuration: KxNAS1Configuration
    status: KxVolumeStatusType
    description: str
    statusReason: str
    createdTimestamp: datetime
    azMode: KxAzModeType
    availabilityZoneIds: List[str]
    lastModifiedTimestamp: datetime
    attachedClusters: List[KxAttachedCluster]
    ResponseMetadata: ResponseMetadata


class ListKxChangesetsResponse(BaseValidatorModel):
    kxChangesets: List[KxChangesetListEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateKxClusterCodeConfigurationRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str
    code: CodeConfiguration
    clientToken: Optional[str] = None
    initializationScript: Optional[str] = None
    commandLineArguments: Optional[List[KxCommandLineArgument]] = None
    deploymentConfiguration: Optional[KxClusterCodeDeploymentConfiguration] = None

KxDatabaseCacheConfigurationUnion = Union[KxDatabaseCacheConfiguration, KxDatabaseCacheConfigurationOutput]


class ListKxDatabasesResponse(BaseValidatorModel):
    kxDatabases: List[KxDatabaseListEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

KxDataviewSegmentConfigurationUnion = Union[KxDataviewSegmentConfiguration, KxDataviewSegmentConfigurationOutput]


class ListKxClusterNodesResponse(BaseValidatorModel):
    nodes: List[KxNode]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListKxScalingGroupsResponse(BaseValidatorModel):
    scalingGroups: List[KxScalingGroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListKxUsersResponse(BaseValidatorModel):
    users: List[KxUser]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListKxVolumesResponse(BaseValidatorModel):
    kxVolumeSummaries: List[KxVolume]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListKxEnvironmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class NetworkACLEntry(BaseValidatorModel):
    ruleNumber: int
    protocol: str
    ruleAction: RuleActionType
    cidrBlock: str
    portRange: Optional[PortRange] = None
    icmpTypeCode: Optional[IcmpTypeCode] = None

TickerplantLogConfigurationUnion = Union[TickerplantLogConfiguration, TickerplantLogConfigurationOutput]

VpcConfigurationUnion = Union[VpcConfiguration, VpcConfigurationOutput]


class ListKxClustersResponse(BaseValidatorModel):
    kxClusterSummaries: List[KxCluster]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetKxDataviewResponse(BaseValidatorModel):
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationOutput]
    activeVersions: List[KxDataviewActiveVersion]
    description: str
    autoUpdate: bool
    readWrite: bool
    environmentId: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: KxDataviewStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadata


class KxDataviewListEntry(BaseValidatorModel):
    environmentId: Optional[str] = None
    databaseName: Optional[str] = None
    dataviewName: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationOutput]] = None
    activeVersions: Optional[List[KxDataviewActiveVersion]] = None
    status: Optional[KxDataviewStatusType] = None
    description: Optional[str] = None
    autoUpdate: Optional[bool] = None
    readWrite: Optional[bool] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None
    statusReason: Optional[str] = None


class UpdateKxDataviewResponse(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationOutput]
    activeVersions: List[KxDataviewActiveVersion]
    status: KxDataviewStatusType
    autoUpdate: bool
    readWrite: bool
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class KxDatabaseConfigurationOutput(BaseValidatorModel):
    databaseName: str
    cacheConfigurations: Optional[List[KxDatabaseCacheConfigurationOutput]] = None
    changesetId: Optional[str] = None
    dataviewName: Optional[str] = None
    dataviewConfiguration: Optional[KxDataviewConfigurationOutput] = None


class GetEnvironmentResponse(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class ListEnvironmentsResponse(BaseValidatorModel):
    environments: List[Environment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateEnvironmentResponse(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersUnion] = None
    superuserParameters: Optional[SuperuserParameters] = None
    dataBundles: Optional[List[str]] = None


class UpdateEnvironmentRequest(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersUnion] = None


class CreateKxDataviewRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    clientToken: str
    availabilityZoneId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationUnion]] = None
    autoUpdate: Optional[bool] = None
    readWrite: Optional[bool] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class KxDataviewConfiguration(BaseValidatorModel):
    dataviewName: Optional[str] = None
    dataviewVersionId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationUnion]] = None


class UpdateKxDataviewRequest(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str
    description: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationUnion]] = None


class TransitGatewayConfigurationOutput(BaseValidatorModel):
    transitGatewayID: str
    routableCIDRSpace: str
    attachmentNetworkAclConfiguration: Optional[List[NetworkACLEntry]] = None


class TransitGatewayConfiguration(BaseValidatorModel):
    transitGatewayID: str
    routableCIDRSpace: str
    attachmentNetworkAclConfiguration: Optional[List[NetworkACLEntry]] = None


class ListKxDataviewsResponse(BaseValidatorModel):
    kxDataviews: List[KxDataviewListEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateKxClusterResponse(BaseValidatorModel):
    environmentId: str
    status: KxClusterStatusType
    statusReason: str
    clusterName: str
    clusterType: KxClusterTypeType
    tickerplantLogConfiguration: TickerplantLogConfigurationOutput
    volumes: List[Volume]
    databases: List[KxDatabaseConfigurationOutput]
    cacheStorageConfigurations: List[KxCacheStorageConfiguration]
    autoScalingConfiguration: AutoScalingConfiguration
    clusterDescription: str
    capacityConfiguration: CapacityConfiguration
    releaseLabel: str
    vpcConfiguration: VpcConfigurationOutput
    initializationScript: str
    commandLineArguments: List[KxCommandLineArgument]
    code: CodeConfiguration
    executionRole: str
    lastModifiedTimestamp: datetime
    savedownStorageConfiguration: KxSavedownStorageConfiguration
    azMode: KxAzModeType
    availabilityZoneId: str
    createdTimestamp: datetime
    scalingGroupConfiguration: KxScalingGroupConfiguration
    ResponseMetadata: ResponseMetadata


class GetKxClusterResponse(BaseValidatorModel):
    status: KxClusterStatusType
    statusReason: str
    clusterName: str
    clusterType: KxClusterTypeType
    tickerplantLogConfiguration: TickerplantLogConfigurationOutput
    volumes: List[Volume]
    databases: List[KxDatabaseConfigurationOutput]
    cacheStorageConfigurations: List[KxCacheStorageConfiguration]
    autoScalingConfiguration: AutoScalingConfiguration
    clusterDescription: str
    capacityConfiguration: CapacityConfiguration
    releaseLabel: str
    vpcConfiguration: VpcConfigurationOutput
    initializationScript: str
    commandLineArguments: List[KxCommandLineArgument]
    code: CodeConfiguration
    executionRole: str
    lastModifiedTimestamp: datetime
    savedownStorageConfiguration: KxSavedownStorageConfiguration
    azMode: KxAzModeType
    availabilityZoneId: str
    createdTimestamp: datetime
    scalingGroupConfiguration: KxScalingGroupConfiguration
    ResponseMetadata: ResponseMetadata

KxDataviewConfigurationUnion = Union[KxDataviewConfiguration, KxDataviewConfigurationOutput]


class GetKxEnvironmentResponse(BaseValidatorModel):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatusType
    tgwStatus: TgwStatusType
    dnsStatus: DnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationOutput
    customDNSConfiguration: List[CustomDNSServer]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    certificateAuthorityArn: str
    ResponseMetadata: ResponseMetadata


class KxEnvironment(BaseValidatorModel):
    name: Optional[str] = None
    environmentId: Optional[str] = None
    awsAccountId: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None
    tgwStatus: Optional[TgwStatusType] = None
    dnsStatus: Optional[DnsStatusType] = None
    errorMessage: Optional[str] = None
    description: Optional[str] = None
    environmentArn: Optional[str] = None
    kmsKeyId: Optional[str] = None
    dedicatedServiceAccountId: Optional[str] = None
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationOutput] = None
    customDNSConfiguration: Optional[List[CustomDNSServer]] = None
    creationTimestamp: Optional[datetime] = None
    updateTimestamp: Optional[datetime] = None
    availabilityZoneIds: Optional[List[str]] = None
    certificateAuthorityArn: Optional[str] = None


class UpdateKxEnvironmentNetworkResponse(BaseValidatorModel):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatusType
    tgwStatus: TgwStatusType
    dnsStatus: DnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationOutput
    customDNSConfiguration: List[CustomDNSServer]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateKxEnvironmentResponse(BaseValidatorModel):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatusType
    tgwStatus: TgwStatusType
    dnsStatus: DnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationOutput
    customDNSConfiguration: List[CustomDNSServer]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    ResponseMetadata: ResponseMetadata

TransitGatewayConfigurationUnion = Union[TransitGatewayConfiguration, TransitGatewayConfigurationOutput]


class KxDatabaseConfiguration(BaseValidatorModel):
    databaseName: str
    cacheConfigurations: Optional[List[KxDatabaseCacheConfigurationUnion]] = None
    changesetId: Optional[str] = None
    dataviewName: Optional[str] = None
    dataviewConfiguration: Optional[KxDataviewConfigurationUnion] = None


class ListKxEnvironmentsResponse(BaseValidatorModel):
    environments: List[KxEnvironment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateKxEnvironmentNetworkRequest(BaseValidatorModel):
    environmentId: str
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationUnion] = None
    customDNSConfiguration: Optional[List[CustomDNSServer]] = None
    clientToken: Optional[str] = None

KxDatabaseConfigurationUnion = Union[KxDatabaseConfiguration, KxDatabaseConfigurationOutput]


class CreateKxClusterRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str
    clusterType: KxClusterTypeType
    releaseLabel: str
    vpcConfiguration: VpcConfigurationUnion
    azMode: KxAzModeType
    clientToken: Optional[str] = None
    tickerplantLogConfiguration: Optional[TickerplantLogConfigurationUnion] = None
    databases: Optional[List[KxDatabaseConfigurationUnion]] = None
    cacheStorageConfigurations: Optional[List[KxCacheStorageConfiguration]] = None
    autoScalingConfiguration: Optional[AutoScalingConfiguration] = None
    clusterDescription: Optional[str] = None
    capacityConfiguration: Optional[CapacityConfiguration] = None
    initializationScript: Optional[str] = None
    commandLineArguments: Optional[List[KxCommandLineArgument]] = None
    code: Optional[CodeConfiguration] = None
    executionRole: Optional[str] = None
    savedownStorageConfiguration: Optional[KxSavedownStorageConfiguration] = None
    availabilityZoneId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    scalingGroupConfiguration: Optional[KxScalingGroupConfiguration] = None


class UpdateKxClusterDatabasesRequest(BaseValidatorModel):
    environmentId: str
    clusterName: str
    databases: List[KxDatabaseConfigurationUnion]
    clientToken: Optional[str] = None
    deploymentConfiguration: Optional[KxDeploymentConfiguration] = None