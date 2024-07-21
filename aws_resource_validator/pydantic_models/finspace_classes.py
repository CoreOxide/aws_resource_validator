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
from aws_resource_validator.pydantic_models.finspace_constants import *

class AutoScalingConfigurationTypeDef(BaseModel):
    minNodeCount: Optional[int] = None
    maxNodeCount: Optional[int] = None
    autoScalingMetric: Optional[Literal["CPU_UTILIZATION_PERCENTAGE"]] = None
    metricTarget: Optional[float] = None
    scaleInCooldownSeconds: Optional[float] = None
    scaleOutCooldownSeconds: Optional[float] = None

class CapacityConfigurationTypeDef(BaseModel):
    nodeType: Optional[str] = None
    nodeCount: Optional[int] = None

class ChangeRequestTypeDef(BaseModel):
    changeType: ChangeTypeType
    dbPath: str
    s3Path: Optional[str] = None

class CodeConfigurationTypeDef(BaseModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    s3ObjectVersion: Optional[str] = None

class FederationParametersTypeDef(BaseModel):
    samlMetadataDocument: Optional[str] = None
    samlMetadataURL: Optional[str] = None
    applicationCallBackURL: Optional[str] = None
    federationURN: Optional[str] = None
    federationProviderName: Optional[str] = None
    attributeMap: Optional[Mapping[str, str]] = None

class SuperuserParametersTypeDef(BaseModel):
    emailAddress: str
    firstName: str
    lastName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ErrorInfoTypeDef(BaseModel):
    errorMessage: Optional[str] = None
    errorType: Optional[ErrorDetailsType] = None

class KxCacheStorageConfigurationTypeDef(BaseModel):
    type: str
    size: int

class KxCommandLineArgumentTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class KxSavedownStorageConfigurationTypeDef(BaseModel):
    type: Optional[Literal["SDS01"]] = None
    size: Optional[int] = None
    volumeName: Optional[str] = None

class KxScalingGroupConfigurationTypeDef(BaseModel):
    scalingGroupName: str
    memoryReservation: int
    nodeCount: int
    memoryLimit: Optional[int] = None
    cpu: Optional[float] = None

class TickerplantLogConfigurationTypeDef(BaseModel):
    tickerplantLogVolumes: Optional[Sequence[str]] = None

class VpcConfigurationTypeDef(BaseModel):
    vpcId: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    ipAddressType: Optional[Literal["IP_V4"]] = None

class VolumeTypeDef(BaseModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None

class CreateKxDatabaseRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class KxDataviewSegmentConfigurationTypeDef(BaseModel):
    dbPaths: Sequence[str]
    volumeName: str
    onDemand: Optional[bool] = None

class CreateKxEnvironmentRequestRequestTypeDef(BaseModel):
    name: str
    kmsKeyId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreateKxScalingGroupRequestRequestTypeDef(BaseModel):
    clientToken: str
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    tags: Optional[Mapping[str, str]] = None

class CreateKxUserRequestRequestTypeDef(BaseModel):
    environmentId: str
    userName: str
    iamRole: str
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class KxNAS1ConfigurationTypeDef(BaseModel):
    type: Optional[KxNAS1TypeType] = None
    size: Optional[int] = None

class CustomDNSServerTypeDef(BaseModel):
    customDNSServerName: str
    customDNSServerIP: str

class DeleteEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str

class DeleteKxClusterNodeRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str
    nodeId: str

class DeleteKxClusterRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str
    clientToken: Optional[str] = None

class DeleteKxDatabaseRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    clientToken: str

class DeleteKxDataviewRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str

class DeleteKxEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str
    clientToken: Optional[str] = None

class DeleteKxScalingGroupRequestRequestTypeDef(BaseModel):
    environmentId: str
    scalingGroupName: str
    clientToken: Optional[str] = None

class DeleteKxUserRequestRequestTypeDef(BaseModel):
    userName: str
    environmentId: str
    clientToken: Optional[str] = None

class DeleteKxVolumeRequestRequestTypeDef(BaseModel):
    environmentId: str
    volumeName: str
    clientToken: Optional[str] = None

class GetEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str

class GetKxChangesetRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    changesetId: str

class GetKxClusterRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str

class GetKxConnectionStringRequestRequestTypeDef(BaseModel):
    userArn: str
    environmentId: str
    clusterName: str

class GetKxDatabaseRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str

class GetKxDataviewRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    dataviewName: str

class GetKxEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str

class GetKxScalingGroupRequestRequestTypeDef(BaseModel):
    environmentId: str
    scalingGroupName: str

class GetKxUserRequestRequestTypeDef(BaseModel):
    userName: str
    environmentId: str

class GetKxVolumeRequestRequestTypeDef(BaseModel):
    environmentId: str
    volumeName: str

class KxAttachedClusterTypeDef(BaseModel):
    clusterName: Optional[str] = None
    clusterType: Optional[KxClusterTypeType] = None
    clusterStatus: Optional[KxClusterStatusType] = None

class IcmpTypeCodeTypeDef(BaseModel):
    type: int
    code: int

class KxChangesetListEntryTypeDef(BaseModel):
    changesetId: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    activeFromTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None
    status: Optional[ChangesetStatusType] = None

class KxClusterCodeDeploymentConfigurationTypeDef(BaseModel):
    deploymentStrategy: KxClusterCodeDeploymentStrategyType

class KxDatabaseCacheConfigurationTypeDef(BaseModel):
    cacheType: str
    dbPaths: Sequence[str]
    dataviewName: Optional[str] = None

class KxDatabaseListEntryTypeDef(BaseModel):
    databaseName: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None

class KxDeploymentConfigurationTypeDef(BaseModel):
    deploymentStrategy: KxDeploymentStrategyType

class KxNodeTypeDef(BaseModel):
    nodeId: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    launchTime: Optional[datetime] = None
    status: Optional[KxNodeStatusType] = None

class KxScalingGroupTypeDef(BaseModel):
    scalingGroupName: Optional[str] = None
    hostType: Optional[str] = None
    clusters: Optional[List[str]] = None
    availabilityZoneId: Optional[str] = None
    status: Optional[KxScalingGroupStatusType] = None
    statusReason: Optional[str] = None
    lastModifiedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None

class KxUserTypeDef(BaseModel):
    userArn: Optional[str] = None
    userName: Optional[str] = None
    iamRole: Optional[str] = None
    createTimestamp: Optional[datetime] = None
    updateTimestamp: Optional[datetime] = None

class KxVolumeTypeDef(BaseModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None
    status: Optional[KxVolumeStatusType] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneIds: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None

class ListEnvironmentsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxChangesetsRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxClusterNodesRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxClustersRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterType: Optional[KxClusterTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKxDatabasesRequestRequestTypeDef(BaseModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxDataviewsRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListKxEnvironmentsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxScalingGroupsRequestRequestTypeDef(BaseModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKxUsersRequestRequestTypeDef(BaseModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxVolumesRequestRequestTypeDef(BaseModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PortRangeTypeDef(BaseModel):
    from: int
    to: int

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateKxDatabaseRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None

class UpdateKxEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateKxUserRequestRequestTypeDef(BaseModel):
    environmentId: str
    userName: str
    iamRole: str
    clientToken: Optional[str] = None

class CreateKxChangesetRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    changeRequests: Sequence[ChangeRequestTypeDef]
    clientToken: str

class EnvironmentTypeDef(BaseModel):
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
    federationParameters: Optional[FederationParametersTypeDef] = None

class UpdateEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersTypeDef] = None

class CreateEnvironmentRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersTypeDef] = None
    superuserParameters: Optional[SuperuserParametersTypeDef] = None
    dataBundles: Optional[Sequence[str]] = None

class CreateEnvironmentResponseTypeDef(BaseModel):
    environmentId: str
    environmentArn: str
    environmentUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxDatabaseResponseTypeDef(BaseModel):
    databaseName: str
    databaseArn: str
    environmentId: str
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxEnvironmentResponseTypeDef(BaseModel):
    name: str
    status: EnvironmentStatusType
    environmentId: str
    description: str
    environmentArn: str
    kmsKeyId: str
    creationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxScalingGroupResponseTypeDef(BaseModel):
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    status: KxScalingGroupStatusType
    lastModifiedTimestamp: datetime
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxUserResponseTypeDef(BaseModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxConnectionStringResponseTypeDef(BaseModel):
    signedConnectionString: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxDatabaseResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxScalingGroupResponseTypeDef(BaseModel):
    scalingGroupName: str
    scalingGroupArn: str
    hostType: str
    clusters: List[str]
    availabilityZoneId: str
    status: KxScalingGroupStatusType
    statusReason: str
    lastModifiedTimestamp: datetime
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxUserResponseTypeDef(BaseModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxDatabaseResponseTypeDef(BaseModel):
    databaseName: str
    environmentId: str
    description: str
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxUserResponseTypeDef(BaseModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxChangesetResponseTypeDef(BaseModel):
    changesetId: str
    databaseName: str
    environmentId: str
    changeRequests: List[ChangeRequestTypeDef]
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: ChangesetStatusType
    errorInfo: ErrorInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxChangesetResponseTypeDef(BaseModel):
    changesetId: str
    databaseName: str
    environmentId: str
    changeRequests: List[ChangeRequestTypeDef]
    createdTimestamp: datetime
    activeFromTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: ChangesetStatusType
    errorInfo: ErrorInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KxClusterTypeDef(BaseModel):
    status: Optional[KxClusterStatusType] = None
    statusReason: Optional[str] = None
    clusterName: Optional[str] = None
    clusterType: Optional[KxClusterTypeType] = None
    clusterDescription: Optional[str] = None
    releaseLabel: Optional[str] = None
    volumes: Optional[List[VolumeTypeDef]] = None
    initializationScript: Optional[str] = None
    executionRole: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneId: Optional[str] = None
    lastModifiedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None

class CreateKxDataviewRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    clientToken: str
    availabilityZoneId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationTypeDef]] = None
    autoUpdate: Optional[bool] = None
    readWrite: Optional[bool] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateKxDataviewResponseTypeDef(BaseModel):
    dataviewName: str
    databaseName: str
    environmentId: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationTypeDef]
    description: str
    autoUpdate: bool
    readWrite: bool
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: KxDataviewStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class KxDataviewActiveVersionTypeDef(BaseModel):
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationTypeDef]] = None
    attachedClusters: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    versionId: Optional[str] = None

class KxDataviewConfigurationTypeDef(BaseModel):
    dataviewName: Optional[str] = None
    dataviewVersionId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationTypeDef]] = None

class UpdateKxDataviewRequestRequestTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str
    description: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationTypeDef]] = None

class CreateKxVolumeRequestRequestTypeDef(BaseModel):
    environmentId: str
    volumeType: Literal["NAS_1"]
    volumeName: str
    azMode: KxAzModeType
    availabilityZoneIds: Sequence[str]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    nas1Configuration: Optional[KxNAS1ConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateKxVolumeResponseTypeDef(BaseModel):
    environmentId: str
    volumeName: str
    volumeType: Literal["NAS_1"]
    volumeArn: str
    nas1Configuration: KxNAS1ConfigurationTypeDef
    status: KxVolumeStatusType
    statusReason: str
    azMode: KxAzModeType
    description: str
    availabilityZoneIds: List[str]
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxVolumeRequestRequestTypeDef(BaseModel):
    environmentId: str
    volumeName: str
    description: Optional[str] = None
    clientToken: Optional[str] = None
    nas1Configuration: Optional[KxNAS1ConfigurationTypeDef] = None

class GetKxVolumeResponseTypeDef(BaseModel):
    environmentId: str
    volumeName: str
    volumeType: Literal["NAS_1"]
    volumeArn: str
    nas1Configuration: KxNAS1ConfigurationTypeDef
    status: KxVolumeStatusType
    statusReason: str
    createdTimestamp: datetime
    description: str
    azMode: KxAzModeType
    availabilityZoneIds: List[str]
    lastModifiedTimestamp: datetime
    attachedClusters: List[KxAttachedClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxVolumeResponseTypeDef(BaseModel):
    environmentId: str
    volumeName: str
    volumeType: Literal["NAS_1"]
    volumeArn: str
    nas1Configuration: KxNAS1ConfigurationTypeDef
    status: KxVolumeStatusType
    description: str
    statusReason: str
    createdTimestamp: datetime
    azMode: KxAzModeType
    availabilityZoneIds: List[str]
    lastModifiedTimestamp: datetime
    attachedClusters: List[KxAttachedClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxChangesetsResponseTypeDef(BaseModel):
    kxChangesets: List[KxChangesetListEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxClusterCodeConfigurationRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str
    code: CodeConfigurationTypeDef
    clientToken: Optional[str] = None
    initializationScript: Optional[str] = None
    commandLineArguments: Optional[Sequence[KxCommandLineArgumentTypeDef]] = None
    deploymentConfiguration: Optional[KxClusterCodeDeploymentConfigurationTypeDef] = None

class ListKxDatabasesResponseTypeDef(BaseModel):
    kxDatabases: List[KxDatabaseListEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxClusterNodesResponseTypeDef(BaseModel):
    nodes: List[KxNodeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxScalingGroupsResponseTypeDef(BaseModel):
    scalingGroups: List[KxScalingGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxUsersResponseTypeDef(BaseModel):
    users: List[KxUserTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxVolumesResponseTypeDef(BaseModel):
    kxVolumeSummaries: List[KxVolumeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxEnvironmentsRequestListKxEnvironmentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NetworkACLEntryTypeDef(BaseModel):
    ruleNumber: int
    protocol: str
    ruleAction: RuleActionType
    cidrBlock: str
    portRange: Optional[PortRangeTypeDef] = None
    icmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None

class GetEnvironmentResponseTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(BaseModel):
    environments: List[EnvironmentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxClustersResponseTypeDef(BaseModel):
    kxClusterSummaries: List[KxClusterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxDataviewResponseTypeDef(BaseModel):
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationTypeDef]
    activeVersions: List[KxDataviewActiveVersionTypeDef]
    description: str
    autoUpdate: bool
    readWrite: bool
    environmentId: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: KxDataviewStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class KxDataviewListEntryTypeDef(BaseModel):
    environmentId: Optional[str] = None
    databaseName: Optional[str] = None
    dataviewName: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationTypeDef]] = None
    activeVersions: Optional[List[KxDataviewActiveVersionTypeDef]] = None
    status: Optional[KxDataviewStatusType] = None
    description: Optional[str] = None
    autoUpdate: Optional[bool] = None
    readWrite: Optional[bool] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None
    statusReason: Optional[str] = None

class UpdateKxDataviewResponseTypeDef(BaseModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationTypeDef]
    activeVersions: List[KxDataviewActiveVersionTypeDef]
    status: KxDataviewStatusType
    autoUpdate: bool
    readWrite: bool
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class KxDatabaseConfigurationTypeDef(BaseModel):
    databaseName: str
    cacheConfigurations: Optional[Sequence[KxDatabaseCacheConfigurationTypeDef]] = None
    changesetId: Optional[str] = None
    dataviewName: Optional[str] = None
    dataviewConfiguration: Optional[KxDataviewConfigurationTypeDef] = None

class TransitGatewayConfigurationTypeDef(BaseModel):
    transitGatewayID: str
    routableCIDRSpace: str
    attachmentNetworkAclConfiguration: Optional[List[NetworkACLEntryTypeDef]] = None

class ListKxDataviewsResponseTypeDef(BaseModel):
    kxDataviews: List[KxDataviewListEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxClusterRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str
    clusterType: KxClusterTypeType
    releaseLabel: str
    vpcConfiguration: VpcConfigurationTypeDef
    azMode: KxAzModeType
    clientToken: Optional[str] = None
    tickerplantLogConfiguration: Optional[TickerplantLogConfigurationTypeDef] = None
    databases: Optional[Sequence[KxDatabaseConfigurationTypeDef]] = None
    cacheStorageConfigurations: Optional[Sequence[KxCacheStorageConfigurationTypeDef]] = None
    autoScalingConfiguration: Optional[AutoScalingConfigurationTypeDef] = None
    clusterDescription: Optional[str] = None
    capacityConfiguration: Optional[CapacityConfigurationTypeDef] = None
    initializationScript: Optional[str] = None
    commandLineArguments: Optional[Sequence[KxCommandLineArgumentTypeDef]] = None
    code: Optional[CodeConfigurationTypeDef] = None
    executionRole: Optional[str] = None
    savedownStorageConfiguration: Optional[KxSavedownStorageConfigurationTypeDef] = None
    availabilityZoneId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    scalingGroupConfiguration: Optional[KxScalingGroupConfigurationTypeDef] = None

class CreateKxClusterResponseTypeDef(BaseModel):
    environmentId: str
    status: KxClusterStatusType
    statusReason: str
    clusterName: str
    clusterType: KxClusterTypeType
    tickerplantLogConfiguration: TickerplantLogConfigurationTypeDef
    volumes: List[VolumeTypeDef]
    databases: List[KxDatabaseConfigurationTypeDef]
    cacheStorageConfigurations: List[KxCacheStorageConfigurationTypeDef]
    autoScalingConfiguration: AutoScalingConfigurationTypeDef
    clusterDescription: str
    capacityConfiguration: CapacityConfigurationTypeDef
    releaseLabel: str
    vpcConfiguration: VpcConfigurationTypeDef
    initializationScript: str
    commandLineArguments: List[KxCommandLineArgumentTypeDef]
    code: CodeConfigurationTypeDef
    executionRole: str
    lastModifiedTimestamp: datetime
    savedownStorageConfiguration: KxSavedownStorageConfigurationTypeDef
    azMode: KxAzModeType
    availabilityZoneId: str
    createdTimestamp: datetime
    scalingGroupConfiguration: KxScalingGroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxClusterResponseTypeDef(BaseModel):
    status: KxClusterStatusType
    statusReason: str
    clusterName: str
    clusterType: KxClusterTypeType
    tickerplantLogConfiguration: TickerplantLogConfigurationTypeDef
    volumes: List[VolumeTypeDef]
    databases: List[KxDatabaseConfigurationTypeDef]
    cacheStorageConfigurations: List[KxCacheStorageConfigurationTypeDef]
    autoScalingConfiguration: AutoScalingConfigurationTypeDef
    clusterDescription: str
    capacityConfiguration: CapacityConfigurationTypeDef
    releaseLabel: str
    vpcConfiguration: VpcConfigurationTypeDef
    initializationScript: str
    commandLineArguments: List[KxCommandLineArgumentTypeDef]
    code: CodeConfigurationTypeDef
    executionRole: str
    lastModifiedTimestamp: datetime
    savedownStorageConfiguration: KxSavedownStorageConfigurationTypeDef
    azMode: KxAzModeType
    availabilityZoneId: str
    createdTimestamp: datetime
    scalingGroupConfiguration: KxScalingGroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxClusterDatabasesRequestRequestTypeDef(BaseModel):
    environmentId: str
    clusterName: str
    databases: Sequence[KxDatabaseConfigurationTypeDef]
    clientToken: Optional[str] = None
    deploymentConfiguration: Optional[KxDeploymentConfigurationTypeDef] = None

class GetKxEnvironmentResponseTypeDef(BaseModel):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatusType
    tgwStatus: tgwStatusType
    dnsStatus: dnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationTypeDef
    customDNSConfiguration: List[CustomDNSServerTypeDef]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    certificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class KxEnvironmentTypeDef(BaseModel):
    name: Optional[str] = None
    environmentId: Optional[str] = None
    awsAccountId: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None
    tgwStatus: Optional[tgwStatusType] = None
    dnsStatus: Optional[dnsStatusType] = None
    errorMessage: Optional[str] = None
    description: Optional[str] = None
    environmentArn: Optional[str] = None
    kmsKeyId: Optional[str] = None
    dedicatedServiceAccountId: Optional[str] = None
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationTypeDef] = None
    customDNSConfiguration: Optional[List[CustomDNSServerTypeDef]] = None
    creationTimestamp: Optional[datetime] = None
    updateTimestamp: Optional[datetime] = None
    availabilityZoneIds: Optional[List[str]] = None
    certificateAuthorityArn: Optional[str] = None

class UpdateKxEnvironmentNetworkRequestRequestTypeDef(BaseModel):
    environmentId: str
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationTypeDef] = None
    customDNSConfiguration: Optional[Sequence[CustomDNSServerTypeDef]] = None
    clientToken: Optional[str] = None

class UpdateKxEnvironmentNetworkResponseTypeDef(BaseModel):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatusType
    tgwStatus: tgwStatusType
    dnsStatus: dnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationTypeDef
    customDNSConfiguration: List[CustomDNSServerTypeDef]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxEnvironmentResponseTypeDef(BaseModel):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatusType
    tgwStatus: tgwStatusType
    dnsStatus: dnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationTypeDef
    customDNSConfiguration: List[CustomDNSServerTypeDef]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxEnvironmentsResponseTypeDef(BaseModel):
    environments: List[KxEnvironmentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

