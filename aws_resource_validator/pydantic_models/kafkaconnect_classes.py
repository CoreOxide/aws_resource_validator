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

class VpcDescription(BaseValidatorModel):
    securityGroups: Optional[List[str]] = None
    subnets: Optional[List[str]] = None


class Vpc(BaseValidatorModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None


class ScaleInPolicyDescription(BaseValidatorModel):
    cpuUtilizationPercentage: Optional[int] = None


class ScaleOutPolicyDescription(BaseValidatorModel):
    cpuUtilizationPercentage: Optional[int] = None


class ScaleInPolicy(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ScaleOutPolicy(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ScaleInPolicyUpdate(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ScaleOutPolicyUpdate(BaseValidatorModel):
    cpuUtilizationPercentage: int


class ProvisionedCapacityDescription(BaseValidatorModel):
    mcuCount: Optional[int] = None
    workerCount: Optional[int] = None


class ProvisionedCapacity(BaseValidatorModel):
    mcuCount: int
    workerCount: int


class ProvisionedCapacityUpdate(BaseValidatorModel):
    mcuCount: int
    workerCount: int


class CloudWatchLogsLogDeliveryDescription(BaseValidatorModel):
    enabled: Optional[bool] = None
    logGroup: Optional[str] = None


class CloudWatchLogsLogDelivery(BaseValidatorModel):
    enabled: bool
    logGroup: Optional[str] = None


class ConnectorOperationStep(BaseValidatorModel):
    stepType: Optional[ConnectorOperationStepTypeType] = None
    stepState: Optional[ConnectorOperationStepStateType] = None


class ConnectorOperationSummary(BaseValidatorModel):
    connectorOperationArn: Optional[str] = None
    connectorOperationType: Optional[ConnectorOperationTypeType] = None
    connectorOperationState: Optional[ConnectorOperationStateType] = None
    creationTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class KafkaClusterClientAuthenticationDescription(BaseValidatorModel):
    authenticationType: Optional[KafkaClusterClientAuthenticationTypeType] = None


class KafkaClusterEncryptionInTransitDescription(BaseValidatorModel):
    encryptionType: Optional[KafkaClusterEncryptionInTransitTypeType] = None


class WorkerConfigurationDescription(BaseValidatorModel):
    revision: Optional[int] = None
    workerConfigurationArn: Optional[str] = None


class KafkaClusterClientAuthentication(BaseValidatorModel):
    authenticationType: KafkaClusterClientAuthenticationTypeType


class KafkaClusterEncryptionInTransit(BaseValidatorModel):
    encryptionType: KafkaClusterEncryptionInTransitTypeType


class WorkerConfiguration(BaseValidatorModel):
    revision: int
    workerConfigurationArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateWorkerConfigurationRequest(BaseValidatorModel):
    name: str
    propertiesFileContent: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class WorkerConfigurationRevisionSummary(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    revision: Optional[int] = None


class CustomPluginDescription(BaseValidatorModel):
    customPluginArn: Optional[str] = None
    revision: Optional[int] = None


class CustomPluginFileDescription(BaseValidatorModel):
    fileMd5: Optional[str] = None
    fileSize: Optional[int] = None


class S3LocationDescription(BaseValidatorModel):
    bucketArn: Optional[str] = None
    fileKey: Optional[str] = None
    objectVersion: Optional[str] = None


class S3Location(BaseValidatorModel):
    bucketArn: str
    fileKey: str
    objectVersion: Optional[str] = None


class CustomPlugin(BaseValidatorModel):
    customPluginArn: str
    revision: int


class DeleteConnectorRequest(BaseValidatorModel):
    connectorArn: str
    currentVersion: Optional[str] = None


class DeleteCustomPluginRequest(BaseValidatorModel):
    customPluginArn: str


class DeleteWorkerConfigurationRequest(BaseValidatorModel):
    workerConfigurationArn: str


class DescribeConnectorOperationRequest(BaseValidatorModel):
    connectorOperationArn: str


class StateDescription(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class DescribeConnectorRequest(BaseValidatorModel):
    connectorArn: str


class DescribeCustomPluginRequest(BaseValidatorModel):
    customPluginArn: str


class DescribeWorkerConfigurationRequest(BaseValidatorModel):
    workerConfigurationArn: str


class WorkerConfigurationRevisionDescription(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    propertiesFileContent: Optional[str] = None
    revision: Optional[int] = None


class FirehoseLogDeliveryDescription(BaseValidatorModel):
    deliveryStream: Optional[str] = None
    enabled: Optional[bool] = None


class FirehoseLogDelivery(BaseValidatorModel):
    enabled: bool
    deliveryStream: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConnectorOperationsRequest(BaseValidatorModel):
    connectorArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListConnectorsRequest(BaseValidatorModel):
    connectorNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCustomPluginsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namePrefix: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListWorkerConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namePrefix: Optional[str] = None


class S3LogDeliveryDescription(BaseValidatorModel):
    bucket: Optional[str] = None
    enabled: Optional[bool] = None
    prefix: Optional[str] = None


class S3LogDelivery(BaseValidatorModel):
    enabled: bool
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ApacheKafkaClusterDescription(BaseValidatorModel):
    bootstrapServers: Optional[str] = None
    vpc: Optional[VpcDescription] = None


class ApacheKafkaCluster(BaseValidatorModel):
    bootstrapServers: str
    vpc: Vpc


class AutoScalingDescription(BaseValidatorModel):
    maxWorkerCount: Optional[int] = None
    mcuCount: Optional[int] = None
    minWorkerCount: Optional[int] = None
    scaleInPolicy: Optional[ScaleInPolicyDescription] = None
    scaleOutPolicy: Optional[ScaleOutPolicyDescription] = None


class AutoScaling(BaseValidatorModel):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: Optional[ScaleInPolicy] = None
    scaleOutPolicy: Optional[ScaleOutPolicy] = None


class AutoScalingUpdate(BaseValidatorModel):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: ScaleInPolicyUpdate
    scaleOutPolicy: ScaleOutPolicyUpdate


class CreateConnectorResponse(BaseValidatorModel):
    connectorArn: str
    connectorName: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadata


class CreateCustomPluginResponse(BaseValidatorModel):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    name: str
    revision: int
    ResponseMetadata: ResponseMetadata


class DeleteConnectorResponse(BaseValidatorModel):
    connectorArn: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadata


class DeleteCustomPluginResponse(BaseValidatorModel):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    ResponseMetadata: ResponseMetadata


class DeleteWorkerConfigurationResponse(BaseValidatorModel):
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadata


class ListConnectorOperationsResponse(BaseValidatorModel):
    connectorOperations: List[ConnectorOperationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateConnectorResponse(BaseValidatorModel):
    connectorArn: str
    connectorState: ConnectorStateType
    connectorOperationArn: str
    ResponseMetadata: ResponseMetadata


class CreateWorkerConfigurationResponse(BaseValidatorModel):
    creationTime: datetime
    latestRevision: WorkerConfigurationRevisionSummary
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadata


class WorkerConfigurationSummary(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    latestRevision: Optional[WorkerConfigurationRevisionSummary] = None
    name: Optional[str] = None
    workerConfigurationArn: Optional[str] = None
    workerConfigurationState: Optional[WorkerConfigurationStateType] = None


class PluginDescription(BaseValidatorModel):
    customPlugin: Optional[CustomPluginDescription] = None


class CustomPluginLocationDescription(BaseValidatorModel):
    s3Location: Optional[S3LocationDescription] = None


class CustomPluginLocation(BaseValidatorModel):
    s3Location: S3Location


class Plugin(BaseValidatorModel):
    customPlugin: CustomPlugin


class DescribeWorkerConfigurationResponse(BaseValidatorModel):
    creationTime: datetime
    description: str
    latestRevision: WorkerConfigurationRevisionDescription
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadata


class ListConnectorOperationsRequestPaginate(BaseValidatorModel):
    connectorArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectorsRequestPaginate(BaseValidatorModel):
    connectorNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomPluginsRequestPaginate(BaseValidatorModel):
    namePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkerConfigurationsRequestPaginate(BaseValidatorModel):
    namePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class WorkerLogDeliveryDescription(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsLogDeliveryDescription] = None
    firehose: Optional[FirehoseLogDeliveryDescription] = None
    s3: Optional[S3LogDeliveryDescription] = None


class WorkerLogDelivery(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsLogDelivery] = None
    firehose: Optional[FirehoseLogDelivery] = None
    s3: Optional[S3LogDelivery] = None


class KafkaClusterDescription(BaseValidatorModel):
    apacheKafkaCluster: Optional[ApacheKafkaClusterDescription] = None


class KafkaCluster(BaseValidatorModel):
    apacheKafkaCluster: ApacheKafkaCluster


class CapacityDescription(BaseValidatorModel):
    autoScaling: Optional[AutoScalingDescription] = None
    provisionedCapacity: Optional[ProvisionedCapacityDescription] = None


class Capacity(BaseValidatorModel):
    autoScaling: Optional[AutoScaling] = None
    provisionedCapacity: Optional[ProvisionedCapacity] = None


class CapacityUpdate(BaseValidatorModel):
    autoScaling: Optional[AutoScalingUpdate] = None
    provisionedCapacity: Optional[ProvisionedCapacityUpdate] = None


class ListWorkerConfigurationsResponse(BaseValidatorModel):
    workerConfigurations: List[WorkerConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CustomPluginRevisionSummary(BaseValidatorModel):
    contentType: Optional[CustomPluginContentTypeType] = None
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    fileDescription: Optional[CustomPluginFileDescription] = None
    location: Optional[CustomPluginLocationDescription] = None
    revision: Optional[int] = None


class CreateCustomPluginRequest(BaseValidatorModel):
    contentType: CustomPluginContentTypeType
    location: CustomPluginLocation
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LogDeliveryDescription(BaseValidatorModel):
    workerLogDelivery: Optional[WorkerLogDeliveryDescription] = None


class LogDelivery(BaseValidatorModel):
    workerLogDelivery: WorkerLogDelivery


class WorkerSetting(BaseValidatorModel):
    capacity: Optional[CapacityDescription] = None


class UpdateConnectorRequest(BaseValidatorModel):
    connectorArn: str
    currentVersion: str
    capacity: Optional[CapacityUpdate] = None
    connectorConfiguration: Optional[Mapping[str, str]] = None


class CustomPluginSummary(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    customPluginArn: Optional[str] = None
    customPluginState: Optional[CustomPluginStateType] = None
    description: Optional[str] = None
    latestRevision: Optional[CustomPluginRevisionSummary] = None
    name: Optional[str] = None


class DescribeCustomPluginResponse(BaseValidatorModel):
    creationTime: datetime
    customPluginArn: str
    customPluginState: CustomPluginStateType
    description: str
    latestRevision: CustomPluginRevisionSummary
    name: str
    stateDescription: StateDescription
    ResponseMetadata: ResponseMetadata


class ConnectorSummary(BaseValidatorModel):
    capacity: Optional[CapacityDescription] = None
    connectorArn: Optional[str] = None
    connectorDescription: Optional[str] = None
    connectorName: Optional[str] = None
    connectorState: Optional[ConnectorStateType] = None
    creationTime: Optional[datetime] = None
    currentVersion: Optional[str] = None
    kafkaCluster: Optional[KafkaClusterDescription] = None
    kafkaClusterClientAuthentication: Optional[ KafkaClusterClientAuthenticationDescription ] = None
    kafkaClusterEncryptionInTransit: Optional[KafkaClusterEncryptionInTransitDescription] = None
    kafkaConnectVersion: Optional[str] = None
    logDelivery: Optional[LogDeliveryDescription] = None
    plugins: Optional[List[PluginDescription]] = None
    serviceExecutionRoleArn: Optional[str] = None
    workerConfiguration: Optional[WorkerConfigurationDescription] = None


class DescribeConnectorResponse(BaseValidatorModel):
    capacity: CapacityDescription
    connectorArn: str
    connectorConfiguration: Dict[str, str]
    connectorDescription: str
    connectorName: str
    connectorState: ConnectorStateType
    creationTime: datetime
    currentVersion: str
    kafkaCluster: KafkaClusterDescription
    kafkaClusterClientAuthentication: KafkaClusterClientAuthenticationDescription
    kafkaClusterEncryptionInTransit: KafkaClusterEncryptionInTransitDescription
    kafkaConnectVersion: str
    logDelivery: LogDeliveryDescription
    plugins: List[PluginDescription]
    serviceExecutionRoleArn: str
    workerConfiguration: WorkerConfigurationDescription
    stateDescription: StateDescription
    ResponseMetadata: ResponseMetadata


class CreateConnectorRequest(BaseValidatorModel):
    capacity: Capacity
    connectorConfiguration: Mapping[str, str]
    connectorName: str
    kafkaCluster: KafkaCluster
    kafkaClusterClientAuthentication: KafkaClusterClientAuthentication
    kafkaClusterEncryptionInTransit: KafkaClusterEncryptionInTransit
    kafkaConnectVersion: str
    plugins: Sequence[Plugin]
    serviceExecutionRoleArn: str
    connectorDescription: Optional[str] = None
    logDelivery: Optional[LogDelivery] = None
    workerConfiguration: Optional[WorkerConfiguration] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeConnectorOperationResponse(BaseValidatorModel):
    connectorArn: str
    connectorOperationArn: str
    connectorOperationState: ConnectorOperationStateType
    connectorOperationType: ConnectorOperationTypeType
    operationSteps: List[ConnectorOperationStep]
    originWorkerSetting: WorkerSetting
    originConnectorConfiguration: Dict[str, str]
    targetWorkerSetting: WorkerSetting
    targetConnectorConfiguration: Dict[str, str]
    errorInfo: StateDescription
    creationTime: datetime
    endTime: datetime
    ResponseMetadata: ResponseMetadata


class ListCustomPluginsResponse(BaseValidatorModel):
    customPlugins: List[CustomPluginSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListConnectorsResponse(BaseValidatorModel):
    connectors: List[ConnectorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


