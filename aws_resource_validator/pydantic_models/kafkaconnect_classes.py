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
from aws_resource_validator.pydantic_models.kafkaconnect_constants import *

class VpcDescriptionTypeDef(BaseValidatorModel):
    securityGroups: Optional[List[str]] = None
    subnets: Optional[List[str]] = None


class VpcTypeDef(BaseValidatorModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None


class ScaleInPolicyDescriptionTypeDef(BaseValidatorModel):
    cpuUtilizationPercentage: Optional[int] = None


class ScaleOutPolicyDescriptionTypeDef(BaseValidatorModel):
    cpuUtilizationPercentage: Optional[int] = None


class ScaleInPolicyTypeDef(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ScaleOutPolicyTypeDef(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ScaleInPolicyUpdateTypeDef(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ScaleOutPolicyUpdateTypeDef(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ProvisionedCapacityDescriptionTypeDef(BaseValidatorModel):
    mcuCount: Optional[int] = None
    workerCount: Optional[int] = None


class ProvisionedCapacityTypeDef(BaseValidatorModel):
    mcuCount: int
    workerCount: int


class ProvisionedCapacityUpdateTypeDef(BaseValidatorModel):
    mcuCount: int
    workerCount: int


class CloudWatchLogsLogDeliveryDescriptionTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    logGroup: Optional[str] = None


class CloudWatchLogsLogDeliveryTypeDef(BaseValidatorModel):
    enabled: bool
    logGroup: Optional[str] = None


class ConnectorOperationStepTypeDef(BaseValidatorModel):
    stepType: Optional[ConnectorOperationStepTypeType] = None
    stepState: Optional[ConnectorOperationStepStateType] = None


class ConnectorOperationSummaryTypeDef(BaseValidatorModel):
    connectorOperationArn: Optional[str] = None
    connectorOperationType: Optional[ConnectorOperationTypeType] = None
    connectorOperationState: Optional[ConnectorOperationStateType] = None
    creationTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class KafkaClusterClientAuthenticationDescriptionTypeDef(BaseValidatorModel):
    authenticationType: Optional[KafkaClusterClientAuthenticationTypeType] = None


class KafkaClusterEncryptionInTransitDescriptionTypeDef(BaseValidatorModel):
    encryptionType: Optional[KafkaClusterEncryptionInTransitTypeType] = None


class WorkerConfigurationDescriptionTypeDef(BaseValidatorModel):
    revision: Optional[int] = None
    workerConfigurationArn: Optional[str] = None


class KafkaClusterClientAuthenticationTypeDef(BaseValidatorModel):
    authenticationType: KafkaClusterClientAuthenticationTypeType


class KafkaClusterEncryptionInTransitTypeDef(BaseValidatorModel):
    encryptionType: KafkaClusterEncryptionInTransitTypeType


class WorkerConfigurationTypeDef(BaseValidatorModel):
    revision: int
    workerConfigurationArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateWorkerConfigurationRequestTypeDef(BaseValidatorModel):
    name: str
    propertiesFileContent: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class WorkerConfigurationRevisionSummaryTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    revision: Optional[int] = None


class CustomPluginDescriptionTypeDef(BaseValidatorModel):
    customPluginArn: Optional[str] = None
    revision: Optional[int] = None


class CustomPluginFileDescriptionTypeDef(BaseValidatorModel):
    fileMd5: Optional[str] = None
    fileSize: Optional[int] = None


class S3LocationDescriptionTypeDef(BaseValidatorModel):
    bucketArn: Optional[str] = None
    fileKey: Optional[str] = None
    objectVersion: Optional[str] = None


class S3LocationTypeDef(BaseValidatorModel):
    bucketArn: str
    fileKey: str
    objectVersion: Optional[str] = None


class CustomPluginTypeDef(BaseValidatorModel):
    customPluginArn: str
    revision: int


class DeleteConnectorRequestTypeDef(BaseValidatorModel):
    connectorArn: str
    currentVersion: Optional[str] = None


class DeleteCustomPluginRequestTypeDef(BaseValidatorModel):
    customPluginArn: str


class DeleteWorkerConfigurationRequestTypeDef(BaseValidatorModel):
    workerConfigurationArn: str


class DescribeConnectorOperationRequestTypeDef(BaseValidatorModel):
    connectorOperationArn: str


class StateDescriptionTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class DescribeConnectorRequestTypeDef(BaseValidatorModel):
    connectorArn: str


class DescribeCustomPluginRequestTypeDef(BaseValidatorModel):
    customPluginArn: str


class DescribeWorkerConfigurationRequestTypeDef(BaseValidatorModel):
    workerConfigurationArn: str


class WorkerConfigurationRevisionDescriptionTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    propertiesFileContent: Optional[str] = None
    revision: Optional[int] = None


class FirehoseLogDeliveryDescriptionTypeDef(BaseValidatorModel):
    deliveryStream: Optional[str] = None
    enabled: Optional[bool] = None


class FirehoseLogDeliveryTypeDef(BaseValidatorModel):
    enabled: bool
    deliveryStream: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConnectorOperationsRequestTypeDef(BaseValidatorModel):
    connectorArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListConnectorsRequestTypeDef(BaseValidatorModel):
    connectorNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCustomPluginsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namePrefix: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListWorkerConfigurationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namePrefix: Optional[str] = None


class S3LogDeliveryDescriptionTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    enabled: Optional[bool] = None
    prefix: Optional[str] = None


class S3LogDeliveryTypeDef(BaseValidatorModel):
    enabled: bool
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ApacheKafkaClusterDescriptionTypeDef(BaseValidatorModel):
    bootstrapServers: Optional[str] = None
    vpc: Optional[VpcDescriptionTypeDef] = None


class ApacheKafkaClusterTypeDef(BaseValidatorModel):
    bootstrapServers: str
    vpc: VpcTypeDef


class AutoScalingDescriptionTypeDef(BaseValidatorModel):
    maxWorkerCount: Optional[int] = None
    mcuCount: Optional[int] = None
    minWorkerCount: Optional[int] = None
    scaleInPolicy: Optional[ScaleInPolicyDescriptionTypeDef] = None
    scaleOutPolicy: Optional[ScaleOutPolicyDescriptionTypeDef] = None


class AutoScalingTypeDef(BaseValidatorModel):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: Optional[ScaleInPolicyTypeDef] = None
    scaleOutPolicy: Optional[ScaleOutPolicyTypeDef] = None


class AutoScalingUpdateTypeDef(BaseValidatorModel):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: ScaleInPolicyUpdateTypeDef
    scaleOutPolicy: ScaleOutPolicyUpdateTypeDef


class CreateConnectorResponseTypeDef(BaseValidatorModel):
    connectorArn: str
    connectorName: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomPluginResponseTypeDef(BaseValidatorModel):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    name: str
    revision: int
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteConnectorResponseTypeDef(BaseValidatorModel):
    connectorArn: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCustomPluginResponseTypeDef(BaseValidatorModel):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteWorkerConfigurationResponseTypeDef(BaseValidatorModel):
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ListConnectorOperationsResponseTypeDef(BaseValidatorModel):
    connectorOperations: List[ConnectorOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConnectorResponseTypeDef(BaseValidatorModel):
    connectorArn: str
    connectorState: ConnectorStateType
    connectorOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkerConfigurationResponseTypeDef(BaseValidatorModel):
    creationTime: datetime
    latestRevision: WorkerConfigurationRevisionSummaryTypeDef
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef


class WorkerConfigurationSummaryTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    latestRevision: Optional[WorkerConfigurationRevisionSummaryTypeDef] = None
    name: Optional[str] = None
    workerConfigurationArn: Optional[str] = None
    workerConfigurationState: Optional[WorkerConfigurationStateType] = None


class PluginDescriptionTypeDef(BaseValidatorModel):
    customPlugin: Optional[CustomPluginDescriptionTypeDef] = None


class CustomPluginLocationDescriptionTypeDef(BaseValidatorModel):
    s3Location: Optional[S3LocationDescriptionTypeDef] = None


class CustomPluginLocationTypeDef(BaseValidatorModel):
    s3Location: S3LocationTypeDef


class PluginTypeDef(BaseValidatorModel):
    customPlugin: CustomPluginTypeDef


class DescribeWorkerConfigurationResponseTypeDef(BaseValidatorModel):
    creationTime: datetime
    description: str
    latestRevision: WorkerConfigurationRevisionDescriptionTypeDef
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ListConnectorOperationsRequestPaginateTypeDef(BaseValidatorModel):
    connectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorsRequestPaginateTypeDef(BaseValidatorModel):
    connectorNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomPluginsRequestPaginateTypeDef(BaseValidatorModel):
    namePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkerConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    namePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class WorkerLogDeliveryDescriptionTypeDef(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsLogDeliveryDescriptionTypeDef] = None
    firehose: Optional[FirehoseLogDeliveryDescriptionTypeDef] = None
    s3: Optional[S3LogDeliveryDescriptionTypeDef] = None


class WorkerLogDeliveryTypeDef(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsLogDeliveryTypeDef] = None
    firehose: Optional[FirehoseLogDeliveryTypeDef] = None
    s3: Optional[S3LogDeliveryTypeDef] = None


class KafkaClusterDescriptionTypeDef(BaseValidatorModel):
    apacheKafkaCluster: Optional[ApacheKafkaClusterDescriptionTypeDef] = None


class KafkaClusterTypeDef(BaseValidatorModel):
    apacheKafkaCluster: ApacheKafkaClusterTypeDef


class CapacityDescriptionTypeDef(BaseValidatorModel):
    autoScaling: Optional[AutoScalingDescriptionTypeDef] = None
    provisionedCapacity: Optional[ProvisionedCapacityDescriptionTypeDef] = None


class CapacityTypeDef(BaseValidatorModel):
    autoScaling: Optional[AutoScalingTypeDef] = None
    provisionedCapacity: Optional[ProvisionedCapacityTypeDef] = None


class CapacityUpdateTypeDef(BaseValidatorModel):
    autoScaling: Optional[AutoScalingUpdateTypeDef] = None
    provisionedCapacity: Optional[ProvisionedCapacityUpdateTypeDef] = None


class ListWorkerConfigurationsResponseTypeDef(BaseValidatorModel):
    workerConfigurations: List[WorkerConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CustomPluginRevisionSummaryTypeDef(BaseValidatorModel):
    contentType: Optional[CustomPluginContentTypeType] = None
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    fileDescription: Optional[CustomPluginFileDescriptionTypeDef] = None
    location: Optional[CustomPluginLocationDescriptionTypeDef] = None
    revision: Optional[int] = None


class CreateCustomPluginRequestTypeDef(BaseValidatorModel):
    contentType: CustomPluginContentTypeType
    location: CustomPluginLocationTypeDef
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LogDeliveryDescriptionTypeDef(BaseValidatorModel):
    workerLogDelivery: Optional[WorkerLogDeliveryDescriptionTypeDef] = None


class LogDeliveryTypeDef(BaseValidatorModel):
    workerLogDelivery: WorkerLogDeliveryTypeDef


class WorkerSettingTypeDef(BaseValidatorModel):
    capacity: Optional[CapacityDescriptionTypeDef] = None


class UpdateConnectorRequestTypeDef(BaseValidatorModel):
    connectorArn: str
    currentVersion: str
    capacity: Optional[CapacityUpdateTypeDef] = None
    connectorConfiguration: Optional[Mapping[str, str]] = None


class CustomPluginSummaryTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    customPluginArn: Optional[str] = None
    customPluginState: Optional[CustomPluginStateType] = None
    description: Optional[str] = None
    latestRevision: Optional[CustomPluginRevisionSummaryTypeDef] = None
    name: Optional[str] = None


class DescribeCustomPluginResponseTypeDef(BaseValidatorModel):
    creationTime: datetime
    customPluginArn: str
    customPluginState: CustomPluginStateType
    description: str
    latestRevision: CustomPluginRevisionSummaryTypeDef
    name: str
    stateDescription: StateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConnectorSummaryTypeDef(BaseValidatorModel):
    capacity: Optional[CapacityDescriptionTypeDef] = None
    connectorArn: Optional[str] = None
    connectorDescription: Optional[str] = None
    connectorName: Optional[str] = None
    connectorState: Optional[ConnectorStateType] = None
    creationTime: Optional[datetime] = None
    currentVersion: Optional[str] = None
    kafkaCluster: Optional[KafkaClusterDescriptionTypeDef] = None
    kafkaClusterClientAuthentication: Optional[ KafkaClusterClientAuthenticationDescriptionTypeDef ] = None
    kafkaClusterEncryptionInTransit: Optional[KafkaClusterEncryptionInTransitDescriptionTypeDef] = None
    kafkaConnectVersion: Optional[str] = None
    logDelivery: Optional[LogDeliveryDescriptionTypeDef] = None
    plugins: Optional[List[PluginDescriptionTypeDef]] = None
    serviceExecutionRoleArn: Optional[str] = None
    workerConfiguration: Optional[WorkerConfigurationDescriptionTypeDef] = None


class DescribeConnectorResponseTypeDef(BaseValidatorModel):
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
    workerConfiguration: WorkerConfigurationDescriptionTypeDef
    stateDescription: StateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConnectorRequestTypeDef(BaseValidatorModel):
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
    workerConfiguration: Optional[WorkerConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeConnectorOperationResponseTypeDef(BaseValidatorModel):
    connectorArn: str
    connectorOperationArn: str
    connectorOperationState: ConnectorOperationStateType
    connectorOperationType: ConnectorOperationTypeType
    operationSteps: List[ConnectorOperationStepTypeDef]
    originWorkerSetting: WorkerSettingTypeDef
    originConnectorConfiguration: Dict[str, str]
    targetWorkerSetting: WorkerSettingTypeDef
    targetConnectorConfiguration: Dict[str, str]
    errorInfo: StateDescriptionTypeDef
    creationTime: datetime
    endTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomPluginsResponseTypeDef(BaseValidatorModel):
    customPlugins: List[CustomPluginSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListConnectorsResponseTypeDef(BaseValidatorModel):
    connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


