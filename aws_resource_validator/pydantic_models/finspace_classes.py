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


class KxCommandLineArgumentTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class KxScalingGroupConfigurationTypeDef(BaseValidatorModel):
    scalingGroupName: str
    memoryReservation: int
    nodeCount: int
    memoryLimit: Optional[int] = None
    cpu: Optional[float] = None


class TickerplantLogConfigurationOutputTypeDef(BaseValidatorModel):
    tickerplantLogVolumes: Optional[List[str]] = None


class VolumeTypeDef(BaseValidatorModel):
    volumeName: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None


class VpcConfigurationOutputTypeDef(BaseValidatorModel):
    vpcId: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    ipAddressType: Optional[Literal["IP_V4"]] = None


class CreateKxDatabaseRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class KxDataviewSegmentConfigurationOutputTypeDef(BaseValidatorModel):
    dbPaths: List[str]
    volumeName: str
    onDemand: Optional[bool] = None


class CreateKxEnvironmentRequestTypeDef(BaseValidatorModel):
    name: str
    kmsKeyId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class CreateKxScalingGroupRequestTypeDef(BaseValidatorModel):
    clientToken: str
    environmentId: str
    scalingGroupName: str
    hostType: str
    availabilityZoneId: str
    tags: Optional[Mapping[str, str]] = None


class CreateKxUserRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userName: str
    iamRole: str
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class CustomDNSServerTypeDef(BaseValidatorModel):
    customDNSServerName: str
    customDNSServerIP: str


class DeleteEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str


class DeleteKxClusterNodeRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    nodeId: str


class DeleteKxClusterRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    clientToken: Optional[str] = None


class DeleteKxDatabaseRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str


class DeleteKxDataviewRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str


class DeleteKxEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clientToken: Optional[str] = None


class DeleteKxScalingGroupRequestTypeDef(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str
    clientToken: Optional[str] = None


class DeleteKxUserRequestTypeDef(BaseValidatorModel):
    userName: str
    environmentId: str
    clientToken: Optional[str] = None


class DeleteKxVolumeRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeName: str
    clientToken: Optional[str] = None


class FederationParametersOutputTypeDef(BaseValidatorModel):
    samlMetadataDocument: Optional[str] = None
    samlMetadataURL: Optional[str] = None
    applicationCallBackURL: Optional[str] = None
    federationURN: Optional[str] = None
    federationProviderName: Optional[str] = None
    attributeMap: Optional[Dict[str, str]] = None


class FederationParametersTypeDef(BaseValidatorModel):
    samlMetadataDocument: Optional[str] = None
    samlMetadataURL: Optional[str] = None
    applicationCallBackURL: Optional[str] = None
    federationURN: Optional[str] = None
    federationProviderName: Optional[str] = None
    attributeMap: Optional[Mapping[str, str]] = None


class GetEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str


class GetKxChangesetRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    changesetId: str


class GetKxClusterRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str


class GetKxConnectionStringRequestTypeDef(BaseValidatorModel):
    userArn: str
    environmentId: str
    clusterName: str


class GetKxDatabaseRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str


class GetKxDataviewRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str


class GetKxEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str


class GetKxScalingGroupRequestTypeDef(BaseValidatorModel):
    environmentId: str
    scalingGroupName: str


class GetKxUserRequestTypeDef(BaseValidatorModel):
    userName: str
    environmentId: str


class GetKxVolumeRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeName: str


class KxAttachedClusterTypeDef(BaseValidatorModel):
    clusterName: Optional[str] = None
    clusterType: Optional[KxClusterTypeType] = None
    clusterStatus: Optional[KxClusterStatusType] = None


class KxChangesetListEntryTypeDef(BaseValidatorModel):
    changesetId: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    activeFromTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None
    status: Optional[ChangesetStatusType] = None


class KxClusterCodeDeploymentConfigurationTypeDef(BaseValidatorModel):
    deploymentStrategy: KxClusterCodeDeploymentStrategyType


class KxDatabaseCacheConfigurationOutputTypeDef(BaseValidatorModel):
    cacheType: str
    dbPaths: List[str]
    dataviewName: Optional[str] = None


class KxDatabaseCacheConfigurationTypeDef(BaseValidatorModel):
    cacheType: str
    dbPaths: Sequence[str]
    dataviewName: Optional[str] = None


class KxDatabaseListEntryTypeDef(BaseValidatorModel):
    databaseName: Optional[str] = None
    createdTimestamp: Optional[datetime] = None
    lastModifiedTimestamp: Optional[datetime] = None


class KxDataviewSegmentConfigurationTypeDef(BaseValidatorModel):
    dbPaths: Sequence[str]
    volumeName: str
    onDemand: Optional[bool] = None


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


class ListEnvironmentsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxChangesetsRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxClusterNodesRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxClustersRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterType: Optional[KxClusterTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKxDatabasesRequestTypeDef(BaseValidatorModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxDataviewsRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListKxEnvironmentsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxScalingGroupsRequestTypeDef(BaseValidatorModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKxUsersRequestTypeDef(BaseValidatorModel):
    environmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListKxVolumesRequestTypeDef(BaseValidatorModel):
    environmentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    volumeType: Optional[Literal["NAS_1"]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TickerplantLogConfigurationTypeDef(BaseValidatorModel):
    tickerplantLogVolumes: Optional[Sequence[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateKxDatabaseRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    clientToken: str
    description: Optional[str] = None


class UpdateKxEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateKxUserRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userName: str
    iamRole: str
    clientToken: Optional[str] = None


class VpcConfigurationTypeDef(BaseValidatorModel):
    vpcId: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    ipAddressType: Optional[Literal["IP_V4"]] = None


class CreateKxChangesetRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    changeRequests: Sequence[ChangeRequestTypeDef]
    clientToken: str


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


class CreateKxDataviewResponseTypeDef(BaseValidatorModel):
    dataviewName: str
    databaseName: str
    environmentId: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationOutputTypeDef]
    description: str
    autoUpdate: bool
    readWrite: bool
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    status: KxDataviewStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class KxDataviewActiveVersionTypeDef(BaseValidatorModel):
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationOutputTypeDef]] = None
    attachedClusters: Optional[List[str]] = None
    createdTimestamp: Optional[datetime] = None
    versionId: Optional[str] = None


class KxDataviewConfigurationOutputTypeDef(BaseValidatorModel):
    dataviewName: Optional[str] = None
    dataviewVersionId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationOutputTypeDef]] = None


class KxNAS1ConfigurationTypeDef(BaseValidatorModel):
    pass


class CreateKxVolumeRequestTypeDef(BaseValidatorModel):
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


class UpdateKxVolumeRequestTypeDef(BaseValidatorModel):
    environmentId: str
    volumeName: str
    description: Optional[str] = None
    clientToken: Optional[str] = None
    nas1Configuration: Optional[KxNAS1ConfigurationTypeDef] = None


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
    federationParameters: Optional[FederationParametersOutputTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateKxClusterCodeConfigurationRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    code: CodeConfigurationTypeDef
    clientToken: Optional[str] = None
    initializationScript: Optional[str] = None
    commandLineArguments: Optional[Sequence[KxCommandLineArgumentTypeDef]] = None
    deploymentConfiguration: Optional[KxClusterCodeDeploymentConfigurationTypeDef] = None


class ListKxDatabasesResponseTypeDef(BaseValidatorModel):
    kxDatabases: List[KxDatabaseListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKxClusterNodesResponseTypeDef(BaseValidatorModel):
    nodes: List[KxNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKxScalingGroupsResponseTypeDef(BaseValidatorModel):
    scalingGroups: List[KxScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKxUsersResponseTypeDef(BaseValidatorModel):
    users: List[KxUserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKxVolumesResponseTypeDef(BaseValidatorModel):
    kxVolumeSummaries: List[KxVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKxEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class IcmpTypeCodeTypeDef(BaseValidatorModel):
    pass


class PortRangeTypeDef(BaseValidatorModel):
    pass


class NetworkACLEntryTypeDef(BaseValidatorModel):
    ruleNumber: int
    protocol: str
    ruleAction: RuleActionType
    cidrBlock: str
    portRange: Optional[PortRangeTypeDef] = None
    icmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None


class ListKxClustersResponseTypeDef(BaseValidatorModel):
    kxClusterSummaries: List[KxClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetKxDataviewResponseTypeDef(BaseValidatorModel):
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    availabilityZoneId: str
    changesetId: str
    segmentConfigurations: List[KxDataviewSegmentConfigurationOutputTypeDef]
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
    segmentConfigurations: Optional[List[KxDataviewSegmentConfigurationOutputTypeDef]] = None
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
    segmentConfigurations: List[KxDataviewSegmentConfigurationOutputTypeDef]
    activeVersions: List[KxDataviewActiveVersionTypeDef]
    status: KxDataviewStatusType
    autoUpdate: bool
    readWrite: bool
    description: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class KxDatabaseConfigurationOutputTypeDef(BaseValidatorModel):
    databaseName: str
    cacheConfigurations: Optional[List[KxDatabaseCacheConfigurationOutputTypeDef]] = None
    changesetId: Optional[str] = None
    dataviewName: Optional[str] = None
    dataviewConfiguration: Optional[KxDataviewConfigurationOutputTypeDef] = None


class GetEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FederationParametersUnionTypeDef(BaseValidatorModel):
    pass


class CreateEnvironmentRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersUnionTypeDef] = None
    superuserParameters: Optional[SuperuserParametersTypeDef] = None
    dataBundles: Optional[Sequence[str]] = None


class UpdateEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    federationMode: Optional[FederationModeType] = None
    federationParameters: Optional[FederationParametersUnionTypeDef] = None


class KxDataviewSegmentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateKxDataviewRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    azMode: KxAzModeType
    clientToken: str
    availabilityZoneId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationUnionTypeDef]] = None
    autoUpdate: Optional[bool] = None
    readWrite: Optional[bool] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class KxDataviewConfigurationTypeDef(BaseValidatorModel):
    dataviewName: Optional[str] = None
    dataviewVersionId: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationUnionTypeDef]] = None


class UpdateKxDataviewRequestTypeDef(BaseValidatorModel):
    environmentId: str
    databaseName: str
    dataviewName: str
    clientToken: str
    description: Optional[str] = None
    changesetId: Optional[str] = None
    segmentConfigurations: Optional[Sequence[KxDataviewSegmentConfigurationUnionTypeDef]] = None


class TransitGatewayConfigurationOutputTypeDef(BaseValidatorModel):
    transitGatewayID: str
    routableCIDRSpace: str
    attachmentNetworkAclConfiguration: Optional[List[NetworkACLEntryTypeDef]] = None


class TransitGatewayConfigurationTypeDef(BaseValidatorModel):
    transitGatewayID: str
    routableCIDRSpace: str
    attachmentNetworkAclConfiguration: Optional[Sequence[NetworkACLEntryTypeDef]] = None


class ListKxDataviewsResponseTypeDef(BaseValidatorModel):
    kxDataviews: List[KxDataviewListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class KxSavedownStorageConfigurationTypeDef(BaseValidatorModel):
    pass


class KxCacheStorageConfigurationTypeDef(BaseValidatorModel):
    pass


class CreateKxClusterResponseTypeDef(BaseValidatorModel):
    environmentId: str
    status: KxClusterStatusType
    statusReason: str
    clusterName: str
    clusterType: KxClusterTypeType
    tickerplantLogConfiguration: TickerplantLogConfigurationOutputTypeDef
    volumes: List[VolumeTypeDef]
    databases: List[KxDatabaseConfigurationOutputTypeDef]
    cacheStorageConfigurations: List[KxCacheStorageConfigurationTypeDef]
    autoScalingConfiguration: AutoScalingConfigurationTypeDef
    clusterDescription: str
    capacityConfiguration: CapacityConfigurationTypeDef
    releaseLabel: str
    vpcConfiguration: VpcConfigurationOutputTypeDef
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
    tickerplantLogConfiguration: TickerplantLogConfigurationOutputTypeDef
    volumes: List[VolumeTypeDef]
    databases: List[KxDatabaseConfigurationOutputTypeDef]
    cacheStorageConfigurations: List[KxCacheStorageConfigurationTypeDef]
    autoScalingConfiguration: AutoScalingConfigurationTypeDef
    clusterDescription: str
    capacityConfiguration: CapacityConfigurationTypeDef
    releaseLabel: str
    vpcConfiguration: VpcConfigurationOutputTypeDef
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


class GetKxEnvironmentResponseTypeDef(BaseValidatorModel):
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
    transitGatewayConfiguration: TransitGatewayConfigurationOutputTypeDef
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
    tgwStatus: Optional[TgwStatusType] = None
    dnsStatus: Optional[DnsStatusType] = None
    errorMessage: Optional[str] = None
    description: Optional[str] = None
    environmentArn: Optional[str] = None
    kmsKeyId: Optional[str] = None
    dedicatedServiceAccountId: Optional[str] = None
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationOutputTypeDef] = None
    customDNSConfiguration: Optional[List[CustomDNSServerTypeDef]] = None
    creationTimestamp: Optional[datetime] = None
    updateTimestamp: Optional[datetime] = None
    availabilityZoneIds: Optional[List[str]] = None
    certificateAuthorityArn: Optional[str] = None


class UpdateKxEnvironmentNetworkResponseTypeDef(BaseValidatorModel):
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
    transitGatewayConfiguration: TransitGatewayConfigurationOutputTypeDef
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
    tgwStatus: TgwStatusType
    dnsStatus: DnsStatusType
    errorMessage: str
    description: str
    environmentArn: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    transitGatewayConfiguration: TransitGatewayConfigurationOutputTypeDef
    customDNSConfiguration: List[CustomDNSServerTypeDef]
    creationTimestamp: datetime
    updateTimestamp: datetime
    availabilityZoneIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class KxDatabaseCacheConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class KxDataviewConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class KxDatabaseConfigurationTypeDef(BaseValidatorModel):
    databaseName: str
    cacheConfigurations: Optional[Sequence[KxDatabaseCacheConfigurationUnionTypeDef]] = None
    changesetId: Optional[str] = None
    dataviewName: Optional[str] = None
    dataviewConfiguration: Optional[KxDataviewConfigurationUnionTypeDef] = None


class ListKxEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[KxEnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TransitGatewayConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateKxEnvironmentNetworkRequestTypeDef(BaseValidatorModel):
    environmentId: str
    transitGatewayConfiguration: Optional[TransitGatewayConfigurationUnionTypeDef] = None
    customDNSConfiguration: Optional[Sequence[CustomDNSServerTypeDef]] = None
    clientToken: Optional[str] = None


class TickerplantLogConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class KxDatabaseConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class VpcConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateKxClusterRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    clusterType: KxClusterTypeType
    releaseLabel: str
    vpcConfiguration: VpcConfigurationUnionTypeDef
    azMode: KxAzModeType
    clientToken: Optional[str] = None
    tickerplantLogConfiguration: Optional[TickerplantLogConfigurationUnionTypeDef] = None
    databases: Optional[Sequence[KxDatabaseConfigurationUnionTypeDef]] = None
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


class UpdateKxClusterDatabasesRequestTypeDef(BaseValidatorModel):
    environmentId: str
    clusterName: str
    databases: Sequence[KxDatabaseConfigurationUnionTypeDef]
    clientToken: Optional[str] = None
    deploymentConfiguration: Optional[KxDeploymentConfigurationTypeDef] = None


