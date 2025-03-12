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
from aws_resource_validator.pydantic_models.pipes_constants import *

class AwsVpcConfigurationOutputTypeDef(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None


class AwsVpcConfigurationTypeDef(BaseValidatorModel):
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None


class BatchArrayPropertiesTypeDef(BaseValidatorModel):
    Size: Optional[int] = None


class BatchEnvironmentVariableTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class BatchRetryStrategyTypeDef(BaseValidatorModel):
    Attempts: Optional[int] = None


class CapacityProviderStrategyItemTypeDef(BaseValidatorModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None


class CloudwatchLogsLogDestinationParametersTypeDef(BaseValidatorModel):
    LogGroupArn: str


class CloudwatchLogsLogDestinationTypeDef(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeadLetterConfigTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class DeletePipeRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribePipeRequestTypeDef(BaseValidatorModel):
    Name: str


class DimensionMappingTypeDef(BaseValidatorModel):
    DimensionValue: str
    DimensionValueType: Literal["VARCHAR"]
    DimensionName: str


class EcsEnvironmentVariableTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class EcsEphemeralStorageTypeDef(BaseValidatorModel):
    sizeInGiB: int


class EcsInferenceAcceleratorOverrideTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    deviceType: Optional[str] = None


class FirehoseLogDestinationParametersTypeDef(BaseValidatorModel):
    DeliveryStreamArn: str


class FirehoseLogDestinationTypeDef(BaseValidatorModel):
    DeliveryStreamArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListPipesRequestTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    SourcePrefix: Optional[str] = None
    TargetPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class PipeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    StateReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Source: Optional[str] = None
    Target: Optional[str] = None
    Enrichment: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class MQBrokerAccessCredentialsTypeDef(BaseValidatorModel):
    BasicAuth: Optional[str] = None


class MSKAccessCredentialsTypeDef(BaseValidatorModel):
    SaslScram512Auth: Optional[str] = None
    ClientCertificateTlsAuth: Optional[str] = None


class MultiMeasureAttributeMappingTypeDef(BaseValidatorModel):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MultiMeasureAttributeName: str


class PipeEnrichmentHttpParametersOutputTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class PipeEnrichmentHttpParametersTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[Sequence[str]] = None
    HeaderParameters: Optional[Mapping[str, str]] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None


class S3LogDestinationParametersTypeDef(BaseValidatorModel):
    BucketName: str
    BucketOwner: str
    OutputFormat: Optional[S3OutputFormatType] = None
    Prefix: Optional[str] = None


class S3LogDestinationTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None
    OutputFormat: Optional[S3OutputFormatType] = None


class PipeSourceSqsQueueParametersTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class SelfManagedKafkaAccessConfigurationCredentialsTypeDef(BaseValidatorModel):
    BasicAuth: Optional[str] = None
    SaslScram512Auth: Optional[str] = None
    SaslScram256Auth: Optional[str] = None
    ClientCertificateTlsAuth: Optional[str] = None


class SelfManagedKafkaAccessConfigurationVpcOutputTypeDef(BaseValidatorModel):
    Subnets: Optional[List[str]] = None
    SecurityGroup: Optional[List[str]] = None


class SelfManagedKafkaAccessConfigurationVpcTypeDef(BaseValidatorModel):
    Subnets: Optional[Sequence[str]] = None
    SecurityGroup: Optional[Sequence[str]] = None


class PipeTargetCloudWatchLogsParametersTypeDef(BaseValidatorModel):
    LogStreamName: Optional[str] = None
    Timestamp: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class PipeTargetEventBridgeEventBusParametersOutputTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    DetailType: Optional[str] = None
    Source: Optional[str] = None
    Resources: Optional[List[str]] = None
    Time: Optional[str] = None


class PipeTargetEventBridgeEventBusParametersTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    DetailType: Optional[str] = None
    Source: Optional[str] = None
    Resources: Optional[Sequence[str]] = None
    Time: Optional[str] = None


class PipeTargetHttpParametersOutputTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class PipeTargetHttpParametersTypeDef(BaseValidatorModel):
    PathParameterValues: Optional[Sequence[str]] = None
    HeaderParameters: Optional[Mapping[str, str]] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None


class PipeTargetKinesisStreamParametersTypeDef(BaseValidatorModel):
    PartitionKey: str


class PipeTargetLambdaFunctionParametersTypeDef(BaseValidatorModel):
    InvocationType: Optional[PipeTargetInvocationTypeType] = None


class PipeTargetRedshiftDataParametersOutputTypeDef(BaseValidatorModel):
    Database: str
    Sqls: List[str]
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None


class PipeTargetSqsQueueParametersTypeDef(BaseValidatorModel):
    MessageGroupId: Optional[str] = None
    MessageDeduplicationId: Optional[str] = None


class PipeTargetStateMachineParametersTypeDef(BaseValidatorModel):
    InvocationType: Optional[PipeTargetInvocationTypeType] = None


class PipeTargetRedshiftDataParametersTypeDef(BaseValidatorModel):
    Database: str
    Sqls: Sequence[str]
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None


class SageMakerPipelineParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class SingleMeasureMappingTypeDef(BaseValidatorModel):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MeasureName: str


class StartPipeRequestTypeDef(BaseValidatorModel):
    Name: str


class StopPipeRequestTypeDef(BaseValidatorModel):
    Name: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdatePipeSourceSqsQueueParametersTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class NetworkConfigurationOutputTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutputTypeDef] = None


class NetworkConfigurationTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None


class BatchResourceRequirementTypeDef(BaseValidatorModel):
    pass


class BatchContainerOverridesOutputTypeDef(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Environment: Optional[List[BatchEnvironmentVariableTypeDef]] = None
    InstanceType: Optional[str] = None
    ResourceRequirements: Optional[List[BatchResourceRequirementTypeDef]] = None


class BatchContainerOverridesTypeDef(BaseValidatorModel):
    Command: Optional[Sequence[str]] = None
    Environment: Optional[Sequence[BatchEnvironmentVariableTypeDef]] = None
    InstanceType: Optional[str] = None
    ResourceRequirements: Optional[Sequence[BatchResourceRequirementTypeDef]] = None


class CreatePipeResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePipeResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartPipeResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class StopPipeResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePipeResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PipeSourceDynamoDBStreamParametersTypeDef(BaseValidatorModel):
    StartingPosition: DynamoDBStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None


class PipeSourceKinesisStreamParametersOutputTypeDef(BaseValidatorModel):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPositionTimestamp: Optional[datetime] = None


class UpdatePipeSourceDynamoDBStreamParametersTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None


class UpdatePipeSourceKinesisStreamParametersTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None


class EcsResourceRequirementTypeDef(BaseValidatorModel):
    pass


class EcsEnvironmentFileTypeDef(BaseValidatorModel):
    pass


class EcsContainerOverrideOutputTypeDef(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    Environment: Optional[List[EcsEnvironmentVariableTypeDef]] = None
    EnvironmentFiles: Optional[List[EcsEnvironmentFileTypeDef]] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    Name: Optional[str] = None
    ResourceRequirements: Optional[List[EcsResourceRequirementTypeDef]] = None


class EcsContainerOverrideTypeDef(BaseValidatorModel):
    Command: Optional[Sequence[str]] = None
    Cpu: Optional[int] = None
    Environment: Optional[Sequence[EcsEnvironmentVariableTypeDef]] = None
    EnvironmentFiles: Optional[Sequence[EcsEnvironmentFileTypeDef]] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    Name: Optional[str] = None
    ResourceRequirements: Optional[Sequence[EcsResourceRequirementTypeDef]] = None


class FilterTypeDef(BaseValidatorModel):
    pass


class FilterCriteriaOutputTypeDef(BaseValidatorModel):
    Filters: Optional[List[FilterTypeDef]] = None


class FilterCriteriaTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListPipesRequestPaginateTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    SourcePrefix: Optional[str] = None
    TargetPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPipesResponseTypeDef(BaseValidatorModel):
    Pipes: List[PipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PipeSourceActiveMQBrokerParametersTypeDef(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    QueueName: str
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class PipeSourceRabbitMQBrokerParametersTypeDef(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    QueueName: str
    VirtualHost: Optional[str] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class UpdatePipeSourceActiveMQBrokerParametersTypeDef(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class UpdatePipeSourceRabbitMQBrokerParametersTypeDef(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class PipeSourceManagedStreamingKafkaParametersTypeDef(BaseValidatorModel):
    TopicName: str
    StartingPosition: Optional[MSKStartPositionType] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[MSKAccessCredentialsTypeDef] = None


class UpdatePipeSourceManagedStreamingKafkaParametersTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    Credentials: Optional[MSKAccessCredentialsTypeDef] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class MultiMeasureMappingOutputTypeDef(BaseValidatorModel):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMappingTypeDef]


class MultiMeasureMappingTypeDef(BaseValidatorModel):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]


class PipeEnrichmentParametersOutputTypeDef(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    HttpParameters: Optional[PipeEnrichmentHttpParametersOutputTypeDef] = None


class PipeEnrichmentParametersTypeDef(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    HttpParameters: Optional[PipeEnrichmentHttpParametersTypeDef] = None


class PipeLogConfigurationParametersTypeDef(BaseValidatorModel):
    Level: LogLevelType
    S3LogDestination: Optional[S3LogDestinationParametersTypeDef] = None
    FirehoseLogDestination: Optional[FirehoseLogDestinationParametersTypeDef] = None
    CloudwatchLogsLogDestination: Optional[CloudwatchLogsLogDestinationParametersTypeDef] = None
    IncludeExecutionData: Optional[Sequence[Literal["ALL"]]] = None


class PipeLogConfigurationTypeDef(BaseValidatorModel):
    S3LogDestination: Optional[S3LogDestinationTypeDef] = None
    FirehoseLogDestination: Optional[FirehoseLogDestinationTypeDef] = None
    CloudwatchLogsLogDestination: Optional[CloudwatchLogsLogDestinationTypeDef] = None
    Level: Optional[LogLevelType] = None
    IncludeExecutionData: Optional[List[Literal["ALL"]]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class PipeSourceKinesisStreamParametersTypeDef(BaseValidatorModel):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPositionTimestamp: Optional[TimestampTypeDef] = None


class PipeSourceSelfManagedKafkaParametersOutputTypeDef(BaseValidatorModel):
    TopicName: str
    StartingPosition: Optional[SelfManagedKafkaStartPositionType] = None
    AdditionalBootstrapServers: Optional[List[str]] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsTypeDef] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcOutputTypeDef] = None


class PipeSourceSelfManagedKafkaParametersTypeDef(BaseValidatorModel):
    TopicName: str
    StartingPosition: Optional[SelfManagedKafkaStartPositionType] = None
    AdditionalBootstrapServers: Optional[Sequence[str]] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsTypeDef] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcTypeDef] = None


class PipeTargetSageMakerPipelineParametersOutputTypeDef(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameterTypeDef]] = None


class PipeTargetSageMakerPipelineParametersTypeDef(BaseValidatorModel):
    PipelineParameterList: Optional[Sequence[SageMakerPipelineParameterTypeDef]] = None


class BatchJobDependencyTypeDef(BaseValidatorModel):
    pass


class PipeTargetBatchJobParametersOutputTypeDef(BaseValidatorModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayPropertiesTypeDef] = None
    RetryStrategy: Optional[BatchRetryStrategyTypeDef] = None
    ContainerOverrides: Optional[BatchContainerOverridesOutputTypeDef] = None
    DependsOn: Optional[List[BatchJobDependencyTypeDef]] = None
    Parameters: Optional[Dict[str, str]] = None


class PipeTargetBatchJobParametersTypeDef(BaseValidatorModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayPropertiesTypeDef] = None
    RetryStrategy: Optional[BatchRetryStrategyTypeDef] = None
    ContainerOverrides: Optional[BatchContainerOverridesTypeDef] = None
    DependsOn: Optional[Sequence[BatchJobDependencyTypeDef]] = None
    Parameters: Optional[Mapping[str, str]] = None


class EcsTaskOverrideOutputTypeDef(BaseValidatorModel):
    ContainerOverrides: Optional[List[EcsContainerOverrideOutputTypeDef]] = None
    Cpu: Optional[str] = None
    EphemeralStorage: Optional[EcsEphemeralStorageTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    InferenceAcceleratorOverrides: Optional[List[EcsInferenceAcceleratorOverrideTypeDef]] = None
    Memory: Optional[str] = None
    TaskRoleArn: Optional[str] = None


class EcsTaskOverrideTypeDef(BaseValidatorModel):
    ContainerOverrides: Optional[Sequence[EcsContainerOverrideTypeDef]] = None
    Cpu: Optional[str] = None
    EphemeralStorage: Optional[EcsEphemeralStorageTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    InferenceAcceleratorOverrides: Optional[Sequence[EcsInferenceAcceleratorOverrideTypeDef]] = None
    Memory: Optional[str] = None
    TaskRoleArn: Optional[str] = None


class PipeTargetTimestreamParametersOutputTypeDef(BaseValidatorModel):
    TimeValue: str
    VersionValue: str
    DimensionMappings: List[DimensionMappingTypeDef]
    EpochTimeUnit: Optional[EpochTimeUnitType] = None
    TimeFieldType: Optional[TimeFieldTypeType] = None
    TimestampFormat: Optional[str] = None
    SingleMeasureMappings: Optional[List[SingleMeasureMappingTypeDef]] = None
    MultiMeasureMappings: Optional[List[MultiMeasureMappingOutputTypeDef]] = None


class PipeTargetTimestreamParametersTypeDef(BaseValidatorModel):
    TimeValue: str
    VersionValue: str
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    EpochTimeUnit: Optional[EpochTimeUnitType] = None
    TimeFieldType: Optional[TimeFieldTypeType] = None
    TimestampFormat: Optional[str] = None
    SingleMeasureMappings: Optional[Sequence[SingleMeasureMappingTypeDef]] = None
    MultiMeasureMappings: Optional[Sequence[MultiMeasureMappingTypeDef]] = None


class PipeSourceParametersOutputTypeDef(BaseValidatorModel):
    FilterCriteria: Optional[FilterCriteriaOutputTypeDef] = None
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParametersOutputTypeDef] = None
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParametersTypeDef] = None
    SqsQueueParameters: Optional[PipeSourceSqsQueueParametersTypeDef] = None
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParametersTypeDef] = None
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParametersTypeDef] = None
    ManagedStreamingKafkaParameters: Optional[PipeSourceManagedStreamingKafkaParametersTypeDef] = None
    SelfManagedKafkaParameters: Optional[PipeSourceSelfManagedKafkaParametersOutputTypeDef] = None


class PipeSourceParametersTypeDef(BaseValidatorModel):
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParametersTypeDef] = None
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParametersTypeDef] = None
    SqsQueueParameters: Optional[PipeSourceSqsQueueParametersTypeDef] = None
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParametersTypeDef] = None
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParametersTypeDef] = None
    ManagedStreamingKafkaParameters: Optional[PipeSourceManagedStreamingKafkaParametersTypeDef] = None
    SelfManagedKafkaParameters: Optional[PipeSourceSelfManagedKafkaParametersTypeDef] = None


class SelfManagedKafkaAccessConfigurationVpcUnionTypeDef(BaseValidatorModel):
    pass


class UpdatePipeSourceSelfManagedKafkaParametersTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsTypeDef] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcUnionTypeDef] = None


class PlacementStrategyTypeDef(BaseValidatorModel):
    pass


class PlacementConstraintTypeDef(BaseValidatorModel):
    pass


class PipeTargetEcsTaskParametersOutputTypeDef(BaseValidatorModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraintTypeDef]] = None
    PlacementStrategy: Optional[List[PlacementStrategyTypeDef]] = None
    PropagateTags: Optional[Literal["TASK_DEFINITION"]] = None
    ReferenceId: Optional[str] = None
    Overrides: Optional[EcsTaskOverrideOutputTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None


class PipeTargetEcsTaskParametersTypeDef(BaseValidatorModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    PlacementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    PropagateTags: Optional[Literal["TASK_DEFINITION"]] = None
    ReferenceId: Optional[str] = None
    Overrides: Optional[EcsTaskOverrideTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class FilterCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class UpdatePipeSourceParametersTypeDef(BaseValidatorModel):
    FilterCriteria: Optional[FilterCriteriaUnionTypeDef] = None
    KinesisStreamParameters: Optional[UpdatePipeSourceKinesisStreamParametersTypeDef] = None
    DynamoDBStreamParameters: Optional[UpdatePipeSourceDynamoDBStreamParametersTypeDef] = None
    SqsQueueParameters: Optional[UpdatePipeSourceSqsQueueParametersTypeDef] = None
    ActiveMQBrokerParameters: Optional[UpdatePipeSourceActiveMQBrokerParametersTypeDef] = None
    RabbitMQBrokerParameters: Optional[UpdatePipeSourceRabbitMQBrokerParametersTypeDef] = None
    ManagedStreamingKafkaParameters: Optional[ UpdatePipeSourceManagedStreamingKafkaParametersTypeDef ] = None
    SelfManagedKafkaParameters: Optional[UpdatePipeSourceSelfManagedKafkaParametersTypeDef] = None


class PipeTargetParametersOutputTypeDef(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    LambdaFunctionParameters: Optional[PipeTargetLambdaFunctionParametersTypeDef] = None
    StepFunctionStateMachineParameters: Optional[PipeTargetStateMachineParametersTypeDef] = None
    KinesisStreamParameters: Optional[PipeTargetKinesisStreamParametersTypeDef] = None
    EcsTaskParameters: Optional[PipeTargetEcsTaskParametersOutputTypeDef] = None
    BatchJobParameters: Optional[PipeTargetBatchJobParametersOutputTypeDef] = None
    SqsQueueParameters: Optional[PipeTargetSqsQueueParametersTypeDef] = None
    HttpParameters: Optional[PipeTargetHttpParametersOutputTypeDef] = None
    RedshiftDataParameters: Optional[PipeTargetRedshiftDataParametersOutputTypeDef] = None
    SageMakerPipelineParameters: Optional[PipeTargetSageMakerPipelineParametersOutputTypeDef] = None
    EventBridgeEventBusParameters: Optional[PipeTargetEventBridgeEventBusParametersOutputTypeDef] = None
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParametersTypeDef] = None
    TimestreamParameters: Optional[PipeTargetTimestreamParametersOutputTypeDef] = None


class PipeTargetParametersTypeDef(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    LambdaFunctionParameters: Optional[PipeTargetLambdaFunctionParametersTypeDef] = None
    StepFunctionStateMachineParameters: Optional[PipeTargetStateMachineParametersTypeDef] = None
    KinesisStreamParameters: Optional[PipeTargetKinesisStreamParametersTypeDef] = None
    EcsTaskParameters: Optional[PipeTargetEcsTaskParametersTypeDef] = None
    BatchJobParameters: Optional[PipeTargetBatchJobParametersTypeDef] = None
    SqsQueueParameters: Optional[PipeTargetSqsQueueParametersTypeDef] = None
    HttpParameters: Optional[PipeTargetHttpParametersTypeDef] = None
    RedshiftDataParameters: Optional[PipeTargetRedshiftDataParametersTypeDef] = None
    SageMakerPipelineParameters: Optional[PipeTargetSageMakerPipelineParametersTypeDef] = None
    EventBridgeEventBusParameters: Optional[PipeTargetEventBridgeEventBusParametersTypeDef] = None
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParametersTypeDef] = None
    TimestreamParameters: Optional[PipeTargetTimestreamParametersTypeDef] = None


class DescribePipeResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    StateReason: str
    Source: str
    SourceParameters: PipeSourceParametersOutputTypeDef
    Enrichment: str
    EnrichmentParameters: PipeEnrichmentParametersOutputTypeDef
    Target: str
    TargetParameters: PipeTargetParametersOutputTypeDef
    RoleArn: str
    Tags: Dict[str, str]
    CreationTime: datetime
    LastModifiedTime: datetime
    LogConfiguration: PipeLogConfigurationTypeDef
    KmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class PipeEnrichmentParametersUnionTypeDef(BaseValidatorModel):
    pass


class PipeTargetParametersUnionTypeDef(BaseValidatorModel):
    pass


class PipeSourceParametersUnionTypeDef(BaseValidatorModel):
    pass


class CreatePipeRequestTypeDef(BaseValidatorModel):
    Name: str
    Source: str
    Target: str
    RoleArn: str
    Description: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    SourceParameters: Optional[PipeSourceParametersUnionTypeDef] = None
    Enrichment: Optional[str] = None
    EnrichmentParameters: Optional[PipeEnrichmentParametersUnionTypeDef] = None
    TargetParameters: Optional[PipeTargetParametersUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    LogConfiguration: Optional[PipeLogConfigurationParametersTypeDef] = None
    KmsKeyIdentifier: Optional[str] = None


class UpdatePipeRequestTypeDef(BaseValidatorModel):
    Name: str
    RoleArn: str
    Description: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    SourceParameters: Optional[UpdatePipeSourceParametersTypeDef] = None
    Enrichment: Optional[str] = None
    EnrichmentParameters: Optional[PipeEnrichmentParametersUnionTypeDef] = None
    Target: Optional[str] = None
    TargetParameters: Optional[PipeTargetParametersUnionTypeDef] = None
    LogConfiguration: Optional[PipeLogConfigurationParametersTypeDef] = None
    KmsKeyIdentifier: Optional[str] = None


