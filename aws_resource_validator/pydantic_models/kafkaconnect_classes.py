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
from aws_resource_validator.pydantic_models.kafkaconnect_constants import *

class VpcDescriptionTypeDef(BaseModel):
    securityGroups: Optional[List[str]] = None
    subnets: Optional[List[str]] = None

class VpcTypeDef(BaseModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None

class ScaleInPolicyDescriptionTypeDef(BaseModel):
    cpuUtilizationPercentage: Optional[int] = None

class ScaleOutPolicyDescriptionTypeDef(BaseModel):
    cpuUtilizationPercentage: Optional[int] = None

class ScaleInPolicyTypeDef(BaseModel):
    cpuUtilizationPercentage: int

class ScaleOutPolicyTypeDef(BaseModel):
    cpuUtilizationPercentage: int

class ScaleInPolicyUpdateTypeDef(BaseModel):
    cpuUtilizationPercentage: int

class ScaleOutPolicyUpdateTypeDef(BaseModel):
    cpuUtilizationPercentage: int

class ProvisionedCapacityDescriptionTypeDef(BaseModel):
    mcuCount: Optional[int] = None
    workerCount: Optional[int] = None

class ProvisionedCapacityTypeDef(BaseModel):
    mcuCount: int
    workerCount: int

class ProvisionedCapacityUpdateTypeDef(BaseModel):
    mcuCount: int
    workerCount: int

class CloudWatchLogsLogDeliveryDescriptionTypeDef(BaseModel):
    enabled: Optional[bool] = None
    logGroup: Optional[str] = None

class CloudWatchLogsLogDeliveryTypeDef(BaseModel):
    enabled: bool
    logGroup: Optional[str] = None

class KafkaClusterClientAuthenticationDescriptionTypeDef(BaseModel):
    authenticationType: Optional[KafkaClusterClientAuthenticationTypeType] = None

class KafkaClusterEncryptionInTransitDescriptionTypeDef(BaseModel):
    encryptionType: Optional[KafkaClusterEncryptionInTransitTypeType] = None

class WorkerConfigurationDescriptionTypeDef(BaseModel):
    revision: Optional[int] = None
    workerConfigurationArn: Optional[str] = None

class KafkaClusterClientAuthenticationTypeDef(BaseModel):
    authenticationType: KafkaClusterClientAuthenticationTypeType

class KafkaClusterEncryptionInTransitTypeDef(BaseModel):
    encryptionType: KafkaClusterEncryptionInTransitTypeType

class WorkerConfigurationTypeDef(BaseModel):
    revision: int
    workerConfigurationArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateWorkerConfigurationRequestRequestTypeDef(BaseModel):
    name: str
    propertiesFileContent: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class WorkerConfigurationRevisionSummaryTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    revision: Optional[int] = None

class CustomPluginDescriptionTypeDef(BaseModel):
    customPluginArn: Optional[str] = None
    revision: Optional[int] = None

class CustomPluginFileDescriptionTypeDef(BaseModel):
    fileMd5: Optional[str] = None
    fileSize: Optional[int] = None

class S3LocationDescriptionTypeDef(BaseModel):
    bucketArn: Optional[str] = None
    fileKey: Optional[str] = None
    objectVersion: Optional[str] = None

class S3LocationTypeDef(BaseModel):
    bucketArn: str
    fileKey: str
    objectVersion: Optional[str] = None

class CustomPluginTypeDef(BaseModel):
    customPluginArn: str
    revision: int

class DeleteConnectorRequestRequestTypeDef(BaseModel):
    connectorArn: str
    currentVersion: Optional[str] = None

class DeleteCustomPluginRequestRequestTypeDef(BaseModel):
    customPluginArn: str

class DeleteWorkerConfigurationRequestRequestTypeDef(BaseModel):
    workerConfigurationArn: str

class DescribeConnectorRequestRequestTypeDef(BaseModel):
    connectorArn: str

class StateDescriptionTypeDef(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

class DescribeCustomPluginRequestRequestTypeDef(BaseModel):
    customPluginArn: str

class DescribeWorkerConfigurationRequestRequestTypeDef(BaseModel):
    workerConfigurationArn: str

class WorkerConfigurationRevisionDescriptionTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    propertiesFileContent: Optional[str] = None
    revision: Optional[int] = None

class FirehoseLogDeliveryDescriptionTypeDef(BaseModel):
    deliveryStream: Optional[str] = None
    enabled: Optional[bool] = None

class FirehoseLogDeliveryTypeDef(BaseModel):
    enabled: bool
    deliveryStream: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseModel):
    connectorNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCustomPluginsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    namePrefix: Optional[str] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListWorkerConfigurationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    namePrefix: Optional[str] = None
    nextToken: Optional[str] = None

class S3LogDeliveryDescriptionTypeDef(BaseModel):
    bucket: Optional[str] = None
    enabled: Optional[bool] = None
    prefix: Optional[str] = None

class S3LogDeliveryTypeDef(BaseModel):
    enabled: bool
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class ApacheKafkaClusterDescriptionTypeDef(BaseModel):
    bootstrapServers: Optional[str] = None
    vpc: Optional[VpcDescriptionTypeDef] = None

class ApacheKafkaClusterTypeDef(BaseModel):
    bootstrapServers: str
    vpc: VpcTypeDef

class AutoScalingDescriptionTypeDef(BaseModel):
    maxWorkerCount: Optional[int] = None
    mcuCount: Optional[int] = None
    minWorkerCount: Optional[int] = None
    scaleInPolicy: Optional[ScaleInPolicyDescriptionTypeDef] = None
    scaleOutPolicy: Optional[ScaleOutPolicyDescriptionTypeDef] = None

class AutoScalingTypeDef(BaseModel):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: Optional[ScaleInPolicyTypeDef] = None
    scaleOutPolicy: Optional[ScaleOutPolicyTypeDef] = None

class AutoScalingUpdateTypeDef(BaseModel):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: ScaleInPolicyUpdateTypeDef
    scaleOutPolicy: ScaleOutPolicyUpdateTypeDef

class CreateConnectorResponseTypeDef(BaseModel):
    connectorArn: str
    connectorName: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomPluginResponseTypeDef(BaseModel):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    name: str
    revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectorResponseTypeDef(BaseModel):
    connectorArn: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomPluginResponseTypeDef(BaseModel):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkerConfigurationResponseTypeDef(BaseModel):
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorResponseTypeDef(BaseModel):
    connectorArn: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkerConfigurationResponseTypeDef(BaseModel):
    creationTime: datetime
    latestRevision: WorkerConfigurationRevisionSummaryTypeDef
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class WorkerConfigurationSummaryTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    latestRevision: Optional[WorkerConfigurationRevisionSummaryTypeDef] = None
    name: Optional[str] = None
    workerConfigurationArn: Optional[str] = None
    workerConfigurationState: Optional[WorkerConfigurationStateType] = None

class PluginDescriptionTypeDef(BaseModel):
    customPlugin: Optional[CustomPluginDescriptionTypeDef] = None

class CustomPluginLocationDescriptionTypeDef(BaseModel):
    s3Location: Optional[S3LocationDescriptionTypeDef] = None

class CustomPluginLocationTypeDef(BaseModel):
    s3Location: S3LocationTypeDef

class PluginTypeDef(BaseModel):
    customPlugin: CustomPluginTypeDef

class DescribeWorkerConfigurationResponseTypeDef(BaseModel):
    creationTime: datetime
    description: str
    latestRevision: WorkerConfigurationRevisionDescriptionTypeDef
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseModel):
    connectorNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomPluginsRequestListCustomPluginsPaginateTypeDef(BaseModel):
    namePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkerConfigurationsRequestListWorkerConfigurationsPaginateTypeDef(BaseModel):
    namePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class WorkerLogDeliveryDescriptionTypeDef(BaseModel):
    cloudWatchLogs: Optional[CloudWatchLogsLogDeliveryDescriptionTypeDef] = None
    firehose: Optional[FirehoseLogDeliveryDescriptionTypeDef] = None
    s3: Optional[S3LogDeliveryDescriptionTypeDef] = None

class WorkerLogDeliveryTypeDef(BaseModel):
    cloudWatchLogs: Optional[CloudWatchLogsLogDeliveryTypeDef] = None
    firehose: Optional[FirehoseLogDeliveryTypeDef] = None
    s3: Optional[S3LogDeliveryTypeDef] = None

class KafkaClusterDescriptionTypeDef(BaseModel):
    apacheKafkaCluster: Optional[ApacheKafkaClusterDescriptionTypeDef] = None

class KafkaClusterTypeDef(BaseModel):
    apacheKafkaCluster: ApacheKafkaClusterTypeDef

class CapacityDescriptionTypeDef(BaseModel):
    autoScaling: Optional[AutoScalingDescriptionTypeDef] = None
    provisionedCapacity: Optional[ProvisionedCapacityDescriptionTypeDef] = None

class CapacityTypeDef(BaseModel):
    autoScaling: Optional[AutoScalingTypeDef] = None
    provisionedCapacity: Optional[ProvisionedCapacityTypeDef] = None

class CapacityUpdateTypeDef(BaseModel):
    autoScaling: Optional[AutoScalingUpdateTypeDef] = None
    provisionedCapacity: Optional[ProvisionedCapacityUpdateTypeDef] = None

class ListWorkerConfigurationsResponseTypeDef(BaseModel):
    nextToken: str
    workerConfigurations: List[WorkerConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomPluginRevisionSummaryTypeDef(BaseModel):
    contentType: Optional[CustomPluginContentTypeType] = None
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    fileDescription: Optional[CustomPluginFileDescriptionTypeDef] = None
    location: Optional[CustomPluginLocationDescriptionTypeDef] = None
    revision: Optional[int] = None

class CreateCustomPluginRequestRequestTypeDef(BaseModel):
    contentType: CustomPluginContentTypeType
    location: CustomPluginLocationTypeDef
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class LogDeliveryDescriptionTypeDef(BaseModel):
    workerLogDelivery: Optional[WorkerLogDeliveryDescriptionTypeDef] = None

class LogDeliveryTypeDef(BaseModel):
    workerLogDelivery: WorkerLogDeliveryTypeDef

class UpdateConnectorRequestRequestTypeDef(BaseModel):
    capacity: CapacityUpdateTypeDef
    connectorArn: str
    currentVersion: str

class CustomPluginSummaryTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    customPluginArn: Optional[str] = None
    customPluginState: Optional[CustomPluginStateType] = None
    description: Optional[str] = None
    latestRevision: Optional[CustomPluginRevisionSummaryTypeDef] = None
    name: Optional[str] = None

class DescribeCustomPluginResponseTypeDef(BaseModel):
    creationTime: datetime
    customPluginArn: str
    customPluginState: CustomPluginStateType
    description: str
    latestRevision: CustomPluginRevisionSummaryTypeDef
    name: str
    stateDescription: StateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorSummaryTypeDef(BaseModel):
    capacity: Optional[CapacityDescriptionTypeDef] = None
    connectorArn: Optional[str] = None
    connectorDescription: Optional[str] = None
    connectorName: Optional[str] = None
    connectorState: Optional[ConnectorStateType] = None
    creationTime: Optional[datetime] = None
    currentVersion: Optional[str] = None
    kafkaCluster: Optional[KafkaClusterDescriptionTypeDef] = None
    kafkaClusterClientAuthentication: Optional[       KafkaClusterClientAuthenticationDescriptionTypeDef     ] = None
    kafkaClusterEncryptionInTransit: Optional[       KafkaClusterEncryptionInTransitDescriptionTypeDef     ] = None
    kafkaConnectVersion: Optional[str] = None
    logDelivery: Optional[LogDeliveryDescriptionTypeDef] = None
    plugins: Optional[List[PluginDescriptionTypeDef]] = None
    serviceExecutionRoleArn: Optional[str] = None
    workerConfiguration: Optional[WorkerConfigurationDescriptionTypeDef] = None

class DescribeConnectorResponseTypeDef(BaseModel):
    capacity: CapacityDescriptionTypeDef
    connectorArn: str
    connectorConfiguration: Dict[str, str]
    connectorDescription: str
    connectorName: str
    connectorState: ConnectorStateType
    creationTime: datetime
    currentVersion: str
    kafkaCluster: KafkaClusterDescriptionTypeDef
    kafkaClusterClientAuthentication: KafkaClusterClientAuthenticationDescriptionTypeDef
    kafkaClusterEncryptionInTransit: KafkaClusterEncryptionInTransitDescriptionTypeDef
    kafkaConnectVersion: str
    logDelivery: LogDeliveryDescriptionTypeDef
    plugins: List[PluginDescriptionTypeDef]
    serviceExecutionRoleArn: str
    stateDescription: StateDescriptionTypeDef
    workerConfiguration: WorkerConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorRequestRequestTypeDef(BaseModel):
    capacity: CapacityTypeDef
    connectorConfiguration: Mapping[str, str]
    connectorName: str
    kafkaCluster: KafkaClusterTypeDef
    kafkaClusterClientAuthentication: KafkaClusterClientAuthenticationTypeDef
    kafkaClusterEncryptionInTransit: KafkaClusterEncryptionInTransitTypeDef
    kafkaConnectVersion: str
    plugins: Sequence[PluginTypeDef]
    serviceExecutionRoleArn: str
    connectorDescription: Optional[str] = None
    logDelivery: Optional[LogDeliveryTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    workerConfiguration: Optional[WorkerConfigurationTypeDef] = None

class ListCustomPluginsResponseTypeDef(BaseModel):
    customPlugins: List[CustomPluginSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponseTypeDef(BaseModel):
    connectors: List[ConnectorSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

