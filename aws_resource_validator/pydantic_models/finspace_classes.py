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
from aws_resource_validator.pydantic_models.finspace_constants import *

class AutoScalingConfigurationTypeDef(BaseValidatorModel):
    minNodeCount: Optional[int] = None
    maxNodeCount: Optional[int] = None
    autoScalingMetric: Optional[Literal["CPU_UTILIZATION_PERCENTAGE"]] = None
    metricTarget: Optional[float] = None
    scaleInCooldownSeconds: Optional[float] = None
    scaleOutCooldownSeconds: Optional[float] = None

class CapacityConfigurationTypeDef(BaseValidatorModel):
    nodeType: Optional[str] = None
    nodeCount: Optional[int] = None

class ChangeRequestTypeDef(BaseValidatorModel):
    changeType: ChangeTypeType
    dbPath: str
    s3Path: Optional[str] = None

class CodeConfigurationTypeDef(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    s3ObjectVersion: Optional[str] = None

class FederationParametersTypeDef(BaseValidatorModel):
    samlMetadataDocument: Optional[str] = None
    samlMetadataURL: Optional[str] = None
    applicationCallBackURL: Optional[str] = None
    federationURN: Optional[str] = None
    federationProviderName: Optional[str] = None
    attributeMap: Optional[Mapping[str, str]] = None

class SuperuserParametersTypeDef(BaseValidatorModel):
    emailAddress: str
    firstName: str
    lastName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ErrorInfoTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorType: Optional[ErrorDetailsType] = None

class KxCacheStorageConfigurationTypeDef(BaseValidatorModel):
    type: str
    size: int

class KxCommandLineArgumentTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class KxSavedownStorageConfigurationTypeDef(BaseValidatorModel):
    type: Optional[Literal["SDS01"]] = None
    size: Optional[int] = None
    volumeName: Optional[str] = None

class KxScalingGroupConfigurationTypeDef(BaseValidatorModel):
    scalingGroupName: str
    memoryReservation: int
    nodeCount: int
    memoryLimit: Optional[int] = None
    cpu: Optional[float] = None

class TickerplantLogConfigurationTypeDef(BaseValidatorModel):
    tickerplantLogVolumes: Optional[Sequence[str]] = None

class VpcConfigurationTypeDef(BaseValidatorModel):
    vpcId: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    ipAddressType: Optional[Literal["IP_V4"]] = None

class VolumeTypeDef(BaseValidatorModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None

class CreateKxDatabaseRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class KxDataviewSegmentConfigurationTypeDef(BaseValidatorModel):
    dbPaths: Sequence[str]
    volumeName: str
    onDemand: Optional[bool] = None

class CreateKxEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    name: str
    kmsKeyId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreateKxScalingGroupRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    tags: Optional[Mapping[str, str]] = None

class CreateKxUserRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userName: str
    iamRole: str
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class KxNAS1ConfigurationTypeDef(BaseValidatorModel):
    type: Optional[KxNAS1TypeType] = None
    size: Optional[int] = None

class CustomDNSServerTypeDef(BaseValidatorModel):
    customDNSServerName: str
    customDNSServerIP: str

class DeleteEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class DeleteKxClusterNodeRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    nodeId: str

class DeleteKxClusterRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    clientToken: Optional[str] = None

class DeleteKxDatabaseRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str

class DeleteKxDataviewRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str

class DeleteKxEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clientToken: Optional[str] = None

class DeleteKxScalingGroupRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str
    clientToken: Optional[str] = None

class DeleteKxUserRequestRequestTypeDef(BaseValidatorModel):
    userName: str
    environmentId: str
    clientToken: Optional[str] = None

class DeleteKxVolumeRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeName: str
    clientToken: Optional[str] = None

class GetEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class GetKxChangesetRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    changesetId: str

class GetKxClusterRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str

class GetKxConnectionStringRequestRequestTypeDef(BaseValidatorModel):
    userArn: str
    environmentId: str
    clusterName: str

class GetKxDatabaseRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str

class GetKxDataviewRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str

class GetKxEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class GetKxScalingGroupRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str

class GetKxUserRequestRequestTypeDef(BaseValidatorModel):
    userName: str
    environmentId: str

class GetKxVolumeRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeName: str

class KxAttachedClusterTypeDef(BaseValidatorModel):
    clusterName: Optional[str] = None
    clusterType: Optional[KxClusterTypeType] = None
    clusterStatus: Optional[KxClusterStatusType] = None

class IcmpTypeCodeTypeDef(BaseValidatorModel):
    type: int
    code: int

class KxChangesetListEntryTypeDef(BaseValidatorModel):
    changesetId: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    activeFromTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None
    status: Optional[ChangesetStatusType] = None

class KxClusterCodeDeploymentConfigurationTypeDef(BaseValidatorModel):
    deploymentStrategy: KxClusterCodeDeploymentStrategyType

class KxDatabaseCacheConfigurationTypeDef(BaseValidatorModel):
    cacheType: str
    dbPaths: Sequence[str]
    dataviewName: Optional[str] = None

class KxDatabaseListEntryTypeDef(BaseValidatorModel):
    databaseName: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None

class KxDeploymentConfigurationTypeDef(BaseValidatorModel):
    deploymentStrategy: KxDeploymentStrategyType

class KxNodeTypeDef(BaseValidatorModel):
    nodeId: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    launchTime: Optional[datetime] = None
    status: Optional[KxNodeStatusType] = None

class KxScalingGroupTypeDef(BaseValidatorModel):
    scalingGroupName: Optional[str] = None
    hostType: Optional[str] = None
    clusters: Optional[List[str]] = None
    availabilityZoneId: Optional[str] = None
    status: Optional[KxScalingGroupStatusType] = None
    statusReason: Optional[str] = None
    lastModifiedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None

class KxUserTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    userName: Optional[str] = None
    iamRole: Optional[str] = None
    createTimestamp: Optional[datetime] = None
    updateTimestamp: Optional[datetime] = None

class KxVolumeTypeDef(BaseValidatorModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None
    status: Optional[KxVolumeStatusType] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None
    azMode: Optional[KxAzModeType] = None
    availabilityZoneIds: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None

class ListEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxChangesetsRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxClusterNodesRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxClustersRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterType: Optional[KxClusterTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKxDatabasesRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxDataviewsRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListKxEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxScalingGroupsRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKxUsersRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListKxVolumesRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class PortRangeTypeDef(BaseValidatorModel):
    _from: int
    to: int

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateKxDatabaseRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None

class UpdateKxEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateKxUserRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userName: str
    iamRole: str
    clientToken: Optional[str] = None

class CreateKxChangesetRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    changeRequests: Sequence[ChangeRequestTypeDef]
    clientToken: str

class EnvironmentTypeDef(BaseValidatorModel):
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

class UpdateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersTypeDef] = None

class CreateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersTypeDef] = None
    superuserParameters: Optional[SuperuserParametersTypeDef] = None
    dataBundles: Optional[Sequence[str]] = None

class CreateEnvironmentResponseTypeDef(BaseValidatorModel):
    environmentId: str
    environmentArn: str
    environmentUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxDatabaseResponseTypeDef(BaseValidatorModel):
    databaseName: str
    databaseArn: str
    environmentId: str
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxEnvironmentResponseTypeDef(BaseValidatorModel):
    name: str
    status: EnvironmentStatusType
    environmentId: str
    description: str
    environmentArn: str
    kmsKeyId: str
    creationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxScalingGroupResponseTypeDef(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    status: KxScalingGroupStatusType
    lastModifiedTimestamp: datetime
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxUserResponseTypeDef(BaseValidatorModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxConnectionStringResponseTypeDef(BaseValidatorModel):
    signedConnectionString: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxDatabaseResponseTypeDef(BaseValidatorModel):
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

class GetKxScalingGroupResponseTypeDef(BaseValidatorModel):
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

class GetKxUserResponseTypeDef(BaseValidatorModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxDatabaseResponseTypeDef(BaseValidatorModel):
    databaseName: str
    environmentId: str
    description: str
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxUserResponseTypeDef(BaseValidatorModel):
    userName: str
    userArn: str
    environmentId: str
    iamRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxChangesetResponseTypeDef(BaseValidatorModel):
    changesetId: str
    databaseName: str
    environmentId: str
    changeRequests: List[ChangeRequestTypeDef]
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: ChangesetStatusType
    errorInfo: ErrorInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxChangesetResponseTypeDef(BaseValidatorModel):
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

class KxClusterTypeDef(BaseValidatorModel):
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

class CreateKxDataviewRequestRequestTypeDef(BaseValidatorModel):
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

class CreateKxDataviewResponseTypeDef(BaseValidatorModel):
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

class KxDataviewActiveVersionTypeDef(BaseValidatorModel):
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationTypeDef]] = None
    attachedClusters: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    versionId: Optional[str] = None

class KxDataviewConfigurationTypeDef(BaseValidatorModel):
    dataviewName: Optional[str] = None
    dataviewVersionId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationTypeDef]] = None

class UpdateKxDataviewRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str
    description: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationTypeDef]] = None

class CreateKxVolumeRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeType: Literal["NAS_1"]
    volumeName: str
    azMode: KxAzModeType
    availabilityZoneIds: Sequence[str]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    nas1Configuration: Optional[KxNAS1ConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateKxVolumeResponseTypeDef(BaseValidatorModel):
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

class UpdateKxVolumeRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeName: str
    description: Optional[str] = None
    clientToken: Optional[str] = None
    nas1Configuration: Optional[KxNAS1ConfigurationTypeDef] = None

class GetKxVolumeResponseTypeDef(BaseValidatorModel):
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

class UpdateKxVolumeResponseTypeDef(BaseValidatorModel):
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

class ListKxChangesetsResponseTypeDef(BaseValidatorModel):
    kxChangesets: List[KxChangesetListEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKxClusterCodeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    code: CodeConfigurationTypeDef
    clientToken: Optional[str] = None
    initializationScript: Optional[str] = None
    commandLineArguments: Optional[Sequence[KxCommandLineArgumentTypeDef]] = None
    deploymentConfiguration: Optional[KxClusterCodeDeploymentConfigurationTypeDef] = None

class ListKxDatabasesResponseTypeDef(BaseValidatorModel):
    kxDatabases: List[KxDatabaseListEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxClusterNodesResponseTypeDef(BaseValidatorModel):
    nodes: List[KxNodeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxScalingGroupsResponseTypeDef(BaseValidatorModel):
    scalingGroups: List[KxScalingGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxUsersResponseTypeDef(BaseValidatorModel):
    users: List[KxUserTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxVolumesResponseTypeDef(BaseValidatorModel):
    kxVolumeSummaries: List[KxVolumeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxEnvironmentsRequestListKxEnvironmentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NetworkACLEntryTypeDef(BaseValidatorModel):
    ruleNumber: int
    protocol: str
    ruleAction: RuleActionType
    cidrBlock: str
    portRange: Optional[PortRangeTypeDef] = None
    icmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None

class GetEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[EnvironmentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKxClustersResponseTypeDef(BaseValidatorModel):
    kxClusterSummaries: List[KxClusterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKxDataviewResponseTypeDef(BaseValidatorModel):
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

class KxDataviewListEntryTypeDef(BaseValidatorModel):
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

class UpdateKxDataviewResponseTypeDef(BaseValidatorModel):
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

class KxDatabaseConfigurationTypeDef(BaseValidatorModel):
    databaseName: str
    cacheConfigurations: Optional[Sequence[KxDatabaseCacheConfigurationTypeDef]] = None
    changesetId: Optional[str] = None
    dataviewName: Optional[str] = None
    dataviewConfiguration: Optional[KxDataviewConfigurationTypeDef] = None

class TransitGatewayConfigurationTypeDef(BaseValidatorModel):
    transitGatewayID: str
    routableCIDRSpace: str
    attachmentNetworkAclConfiguration: Optional[List[NetworkACLEntryTypeDef]] = None

class ListKxDataviewsResponseTypeDef(BaseValidatorModel):
    kxDataviews: List[KxDataviewListEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKxClusterRequestRequestTypeDef(BaseValidatorModel):
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

class CreateKxClusterResponseTypeDef(BaseValidatorModel):
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

class GetKxClusterResponseTypeDef(BaseValidatorModel):
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

class UpdateKxClusterDatabasesRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    databases: Sequence[KxDatabaseConfigurationTypeDef]
    clientToken: Optional[str] = None
    deploymentConfiguration: Optional[KxDeploymentConfigurationTypeDef] = None

class GetKxEnvironmentResponseTypeDef(BaseValidatorModel):
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

class KxEnvironmentTypeDef(BaseValidatorModel):
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

class UpdateKxEnvironmentNetworkRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationTypeDef] = None
    customDNSConfiguration: Optional[Sequence[CustomDNSServerTypeDef]] = None
    clientToken: Optional[str] = None

class UpdateKxEnvironmentNetworkResponseTypeDef(BaseValidatorModel):
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

class UpdateKxEnvironmentResponseTypeDef(BaseValidatorModel):
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

class ListKxEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[KxEnvironmentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

