from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pipes.pipes_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AwsVpcConfigurationOutput(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None


class AwsVpcConfiguration(BaseValidatorModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None


class BatchArrayProperties(BaseValidatorModel):
    Size: Optional[int] = None


class BatchEnvironmentVariable(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class BatchResourceRequirement(BaseValidatorModel):
    Type: BatchResourceRequirementTypeType
    Value: str


class BatchJobDependency(BaseValidatorModel):
    JobId: Optional[str] = None
    Type: Optional[BatchJobDependencyTypeType] = None


class BatchRetryStrategy(BaseValidatorModel):
    Attempts: Optional[int] = None


class CapacityProviderStrategyItem(BaseValidatorModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None


class CloudwatchLogsLogDestinationParameters(BaseValidatorModel):
    LogGroupArn: str


class CloudwatchLogsLogDestination(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeadLetterConfig(BaseValidatorModel):
    Arn: Optional[str] = None


class DeletePipeRequest(BaseValidatorModel):
    Name: str


class DescribePipeRequest(BaseValidatorModel):
    Name: str


class DimensionMapping(BaseValidatorModel):
    DimensionValue: str
    DimensionValueType: Literal['VARCHAR']
    DimensionName: str


class EcsEnvironmentFile(BaseValidatorModel):
    type: Literal['s3']
    value: str


class EcsEnvironmentVariable(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class EcsResourceRequirement(BaseValidatorModel):
    type: EcsResourceRequirementTypeType
    value: str


class EcsEphemeralStorage(BaseValidatorModel):
    sizeInGiB: int


class EcsInferenceAcceleratorOverride(BaseValidatorModel):
    deviceName: Optional[str] = None
    deviceType: Optional[str] = None


class Filter(BaseValidatorModel):
    Pattern: Optional[str] = None


class FirehoseLogDestinationParameters(BaseValidatorModel):
    DeliveryStreamArn: str


class FirehoseLogDestination(BaseValidatorModel):
    DeliveryStreamArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListPipesRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    SourcePrefix: Optional[str] = None
    TargetPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class Pipe(BaseValidatorModel):
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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class MQBrokerAccessCredentials(BaseValidatorModel):
    BasicAuth: Optional[str] = None


class MSKAccessCredentials(BaseValidatorModel):
    SaslScram512Auth: Optional[str] = None
    ClientCertificateTlsAuth: Optional[str] = None


class MultiMeasureAttributeMapping(BaseValidatorModel):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MultiMeasureAttributeName: str


class PipeEnrichmentHttpParametersOutput(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class PipeEnrichmentHttpParameters(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class S3LogDestinationParameters(BaseValidatorModel):
    BucketName: str
    BucketOwner: str
    OutputFormat: Optional[S3OutputFormatType] = None
    Prefix: Optional[str] = None


class S3LogDestination(BaseValidatorModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None
    OutputFormat: Optional[S3OutputFormatType] = None

Timestamp = Union[datetime, str]


class PipeSourceSqsQueueParameters(BaseValidatorModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class SelfManagedKafkaAccessConfigurationCredentials(BaseValidatorModel):
    BasicAuth: Optional[str] = None
    SaslScram512Auth: Optional[str] = None
    SaslScram256Auth: Optional[str] = None
    ClientCertificateTlsAuth: Optional[str] = None


class SelfManagedKafkaAccessConfigurationVpcOutput(BaseValidatorModel):
    Subnets: Optional[List[str]] = None
    SecurityGroup: Optional[List[str]] = None


class SelfManagedKafkaAccessConfigurationVpc(BaseValidatorModel):
    Subnets: Optional[List[str]] = None
    SecurityGroup: Optional[List[str]] = None


class PipeTargetCloudWatchLogsParameters(BaseValidatorModel):
    LogStreamName: Optional[str] = None
    Timestamp: Optional[str] = None


class PlacementConstraint(BaseValidatorModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None


class PlacementStrategy(BaseValidatorModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class PipeTargetEventBridgeEventBusParametersOutput(BaseValidatorModel):
    EndpointId: Optional[str] = None
    DetailType: Optional[str] = None
    Source: Optional[str] = None
    Resources: Optional[List[str]] = None
    Time: Optional[str] = None


class PipeTargetEventBridgeEventBusParameters(BaseValidatorModel):
    EndpointId: Optional[str] = None
    DetailType: Optional[str] = None
    Source: Optional[str] = None
    Resources: Optional[List[str]] = None
    Time: Optional[str] = None


class PipeTargetHttpParametersOutput(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class PipeTargetHttpParameters(BaseValidatorModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None


class PipeTargetKinesisStreamParameters(BaseValidatorModel):
    PartitionKey: str


class PipeTargetLambdaFunctionParameters(BaseValidatorModel):
    InvocationType: Optional[PipeTargetInvocationTypeType] = None


class PipeTargetRedshiftDataParametersOutput(BaseValidatorModel):
    Database: str
    Sqls: List[str]
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None


class PipeTargetSqsQueueParameters(BaseValidatorModel):
    MessageGroupId: Optional[str] = None
    MessageDeduplicationId: Optional[str] = None


class PipeTargetStateMachineParameters(BaseValidatorModel):
    InvocationType: Optional[PipeTargetInvocationTypeType] = None


class PipeTargetRedshiftDataParameters(BaseValidatorModel):
    Database: str
    Sqls: List[str]
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None


class SageMakerPipelineParameter(BaseValidatorModel):
    Name: str
    Value: str


class SingleMeasureMapping(BaseValidatorModel):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MeasureName: str


class StartPipeRequest(BaseValidatorModel):
    Name: str


class StopPipeRequest(BaseValidatorModel):
    Name: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdatePipeSourceSqsQueueParameters(BaseValidatorModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class NetworkConfigurationOutput(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutput] = None


class NetworkConfiguration(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfiguration] = None


class BatchContainerOverridesOutput(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Environment: Optional[List[BatchEnvironmentVariable]] = None
    InstanceType: Optional[str] = None
    ResourceRequirements: Optional[List[BatchResourceRequirement]] = None


class BatchContainerOverrides(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Environment: Optional[List[BatchEnvironmentVariable]] = None
    InstanceType: Optional[str] = None
    ResourceRequirements: Optional[List[BatchResourceRequirement]] = None


class CreatePipeResponse(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class DeletePipeResponse(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartPipeResponse(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class StopPipeResponse(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdatePipeResponse(BaseValidatorModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class PipeSourceDynamoDBStreamParameters(BaseValidatorModel):
    StartingPosition: DynamoDBStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    OnPartialBatchItemFailure: Optional[Literal['AUTOMATIC_BISECT']] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None


class PipeSourceKinesisStreamParametersOutput(BaseValidatorModel):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    OnPartialBatchItemFailure: Optional[Literal['AUTOMATIC_BISECT']] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPositionTimestamp: Optional[datetime] = None


class UpdatePipeSourceDynamoDBStreamParameters(BaseValidatorModel):
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    OnPartialBatchItemFailure: Optional[Literal['AUTOMATIC_BISECT']] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None


class UpdatePipeSourceKinesisStreamParameters(BaseValidatorModel):
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    OnPartialBatchItemFailure: Optional[Literal['AUTOMATIC_BISECT']] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None


class EcsContainerOverrideOutput(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    Environment: Optional[List[EcsEnvironmentVariable]] = None
    EnvironmentFiles: Optional[List[EcsEnvironmentFile]] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    Name: Optional[str] = None
    ResourceRequirements: Optional[List[EcsResourceRequirement]] = None


class EcsContainerOverride(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    Environment: Optional[List[EcsEnvironmentVariable]] = None
    EnvironmentFiles: Optional[List[EcsEnvironmentFile]] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    Name: Optional[str] = None
    ResourceRequirements: Optional[List[EcsResourceRequirement]] = None


class FilterCriteriaOutput(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None


class FilterCriteria(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None


class ListPipesRequestPaginate(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    SourcePrefix: Optional[str] = None
    TargetPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipesResponse(BaseValidatorModel):
    Pipes: List[Pipe]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PipeSourceActiveMQBrokerParameters(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentials
    QueueName: str
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class PipeSourceRabbitMQBrokerParameters(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentials
    QueueName: str
    VirtualHost: Optional[str] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class UpdatePipeSourceActiveMQBrokerParameters(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentials
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class UpdatePipeSourceRabbitMQBrokerParameters(BaseValidatorModel):
    Credentials: MQBrokerAccessCredentials
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class PipeSourceManagedStreamingKafkaParameters(BaseValidatorModel):
    TopicName: str
    StartingPosition: Optional[MSKStartPositionType] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[MSKAccessCredentials] = None


class UpdatePipeSourceManagedStreamingKafkaParameters(BaseValidatorModel):
    BatchSize: Optional[int] = None
    Credentials: Optional[MSKAccessCredentials] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None


class MultiMeasureMappingOutput(BaseValidatorModel):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMapping]


class MultiMeasureMapping(BaseValidatorModel):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMapping]


class PipeEnrichmentParametersOutput(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    HttpParameters: Optional[PipeEnrichmentHttpParametersOutput] = None


class PipeEnrichmentParameters(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    HttpParameters: Optional[PipeEnrichmentHttpParameters] = None


class PipeLogConfigurationParameters(BaseValidatorModel):
    Level: LogLevelType
    S3LogDestination: Optional[S3LogDestinationParameters] = None
    FirehoseLogDestination: Optional[FirehoseLogDestinationParameters] = None
    CloudwatchLogsLogDestination: Optional[CloudwatchLogsLogDestinationParameters] = None
    IncludeExecutionData: Optional[List[Literal['ALL']]] = None


class PipeLogConfiguration(BaseValidatorModel):
    S3LogDestination: Optional[S3LogDestination] = None
    FirehoseLogDestination: Optional[FirehoseLogDestination] = None
    CloudwatchLogsLogDestination: Optional[CloudwatchLogsLogDestination] = None
    Level: Optional[LogLevelType] = None
    IncludeExecutionData: Optional[List[Literal['ALL']]] = None


class PipeSourceKinesisStreamParameters(BaseValidatorModel):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    OnPartialBatchItemFailure: Optional[Literal['AUTOMATIC_BISECT']] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPositionTimestamp: Optional[Timestamp] = None


class PipeSourceSelfManagedKafkaParametersOutput(BaseValidatorModel):
    TopicName: str
    StartingPosition: Optional[SelfManagedKafkaStartPositionType] = None
    AdditionalBootstrapServers: Optional[List[str]] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentials] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcOutput] = None


class PipeSourceSelfManagedKafkaParameters(BaseValidatorModel):
    TopicName: str
    StartingPosition: Optional[SelfManagedKafkaStartPositionType] = None
    AdditionalBootstrapServers: Optional[List[str]] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentials] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpc] = None

SelfManagedKafkaAccessConfigurationVpcUnion = Union[SelfManagedKafkaAccessConfigurationVpc, SelfManagedKafkaAccessConfigurationVpcOutput]


class PipeTargetSageMakerPipelineParametersOutput(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameter]] = None


class PipeTargetSageMakerPipelineParameters(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameter]] = None


class PipeTargetBatchJobParametersOutput(BaseValidatorModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayProperties] = None
    RetryStrategy: Optional[BatchRetryStrategy] = None
    ContainerOverrides: Optional[BatchContainerOverridesOutput] = None
    DependsOn: Optional[List[BatchJobDependency]] = None
    Parameters: Optional[Dict[str, str]] = None


class PipeTargetBatchJobParameters(BaseValidatorModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayProperties] = None
    RetryStrategy: Optional[BatchRetryStrategy] = None
    ContainerOverrides: Optional[BatchContainerOverrides] = None
    DependsOn: Optional[List[BatchJobDependency]] = None
    Parameters: Optional[Dict[str, str]] = None


class EcsTaskOverrideOutput(BaseValidatorModel):
    ContainerOverrides: Optional[List[EcsContainerOverrideOutput]] = None
    Cpu: Optional[str] = None
    EphemeralStorage: Optional[EcsEphemeralStorage] = None
    ExecutionRoleArn: Optional[str] = None
    InferenceAcceleratorOverrides: Optional[List[EcsInferenceAcceleratorOverride]] = None
    Memory: Optional[str] = None
    TaskRoleArn: Optional[str] = None


class EcsTaskOverride(BaseValidatorModel):
    ContainerOverrides: Optional[List[EcsContainerOverride]] = None
    Cpu: Optional[str] = None
    EphemeralStorage: Optional[EcsEphemeralStorage] = None
    ExecutionRoleArn: Optional[str] = None
    InferenceAcceleratorOverrides: Optional[List[EcsInferenceAcceleratorOverride]] = None
    Memory: Optional[str] = None
    TaskRoleArn: Optional[str] = None

FilterCriteriaUnion = Union[FilterCriteria, FilterCriteriaOutput]


class PipeTargetTimestreamParametersOutput(BaseValidatorModel):
    TimeValue: str
    VersionValue: str
    DimensionMappings: List[DimensionMapping]
    EpochTimeUnit: Optional[EpochTimeUnitType] = None
    TimeFieldType: Optional[TimeFieldTypeType] = None
    TimestampFormat: Optional[str] = None
    SingleMeasureMappings: Optional[List[SingleMeasureMapping]] = None
    MultiMeasureMappings: Optional[List[MultiMeasureMappingOutput]] = None


class PipeTargetTimestreamParameters(BaseValidatorModel):
    TimeValue: str
    VersionValue: str
    DimensionMappings: List[DimensionMapping]
    EpochTimeUnit: Optional[EpochTimeUnitType] = None
    TimeFieldType: Optional[TimeFieldTypeType] = None
    TimestampFormat: Optional[str] = None
    SingleMeasureMappings: Optional[List[SingleMeasureMapping]] = None
    MultiMeasureMappings: Optional[List[MultiMeasureMapping]] = None

PipeEnrichmentParametersUnion = Union[PipeEnrichmentParameters, PipeEnrichmentParametersOutput]


class PipeSourceParametersOutput(BaseValidatorModel):
    FilterCriteria: Optional[FilterCriteriaOutput] = None
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParametersOutput] = None
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParameters] = None
    SqsQueueParameters: Optional[PipeSourceSqsQueueParameters] = None
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParameters] = None
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParameters] = None
    ManagedStreamingKafkaParameters: Optional[PipeSourceManagedStreamingKafkaParameters] = None
    SelfManagedKafkaParameters: Optional[PipeSourceSelfManagedKafkaParametersOutput] = None


class PipeSourceParameters(BaseValidatorModel):
    FilterCriteria: Optional[FilterCriteria] = None
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParameters] = None
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParameters] = None
    SqsQueueParameters: Optional[PipeSourceSqsQueueParameters] = None
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParameters] = None
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParameters] = None
    ManagedStreamingKafkaParameters: Optional[PipeSourceManagedStreamingKafkaParameters] = None
    SelfManagedKafkaParameters: Optional[PipeSourceSelfManagedKafkaParameters] = None


class UpdatePipeSourceSelfManagedKafkaParameters(BaseValidatorModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentials] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcUnion] = None


class PipeTargetEcsTaskParametersOutput(BaseValidatorModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationOutput] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraint]] = None
    PlacementStrategy: Optional[List[PlacementStrategy]] = None
    PropagateTags: Optional[Literal['TASK_DEFINITION']] = None
    ReferenceId: Optional[str] = None
    Overrides: Optional[EcsTaskOverrideOutput] = None
    Tags: Optional[List[Tag]] = None


class PipeTargetEcsTaskParameters(BaseValidatorModel):
    TaskDefinitionArn: str
    TaskCount: Optional[int] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfiguration] = None
    PlatformVersion: Optional[str] = None
    Group: Optional[str] = None
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    PlacementConstraints: Optional[List[PlacementConstraint]] = None
    PlacementStrategy: Optional[List[PlacementStrategy]] = None
    PropagateTags: Optional[Literal['TASK_DEFINITION']] = None
    ReferenceId: Optional[str] = None
    Overrides: Optional[EcsTaskOverride] = None
    Tags: Optional[List[Tag]] = None

PipeSourceParametersUnion = Union[PipeSourceParameters, PipeSourceParametersOutput]


class UpdatePipeSourceParameters(BaseValidatorModel):
    FilterCriteria: Optional[FilterCriteriaUnion] = None
    KinesisStreamParameters: Optional[UpdatePipeSourceKinesisStreamParameters] = None
    DynamoDBStreamParameters: Optional[UpdatePipeSourceDynamoDBStreamParameters] = None
    SqsQueueParameters: Optional[UpdatePipeSourceSqsQueueParameters] = None
    ActiveMQBrokerParameters: Optional[UpdatePipeSourceActiveMQBrokerParameters] = None
    RabbitMQBrokerParameters: Optional[UpdatePipeSourceRabbitMQBrokerParameters] = None
    ManagedStreamingKafkaParameters: Optional[UpdatePipeSourceManagedStreamingKafkaParameters] = None
    SelfManagedKafkaParameters: Optional[UpdatePipeSourceSelfManagedKafkaParameters] = None


class PipeTargetParametersOutput(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    LambdaFunctionParameters: Optional[PipeTargetLambdaFunctionParameters] = None
    StepFunctionStateMachineParameters: Optional[PipeTargetStateMachineParameters] = None
    KinesisStreamParameters: Optional[PipeTargetKinesisStreamParameters] = None
    EcsTaskParameters: Optional[PipeTargetEcsTaskParametersOutput] = None
    BatchJobParameters: Optional[PipeTargetBatchJobParametersOutput] = None
    SqsQueueParameters: Optional[PipeTargetSqsQueueParameters] = None
    HttpParameters: Optional[PipeTargetHttpParametersOutput] = None
    RedshiftDataParameters: Optional[PipeTargetRedshiftDataParametersOutput] = None
    SageMakerPipelineParameters: Optional[PipeTargetSageMakerPipelineParametersOutput] = None
    EventBridgeEventBusParameters: Optional[PipeTargetEventBridgeEventBusParametersOutput] = None
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParameters] = None
    TimestreamParameters: Optional[PipeTargetTimestreamParametersOutput] = None


class PipeTargetParameters(BaseValidatorModel):
    InputTemplate: Optional[str] = None
    LambdaFunctionParameters: Optional[PipeTargetLambdaFunctionParameters] = None
    StepFunctionStateMachineParameters: Optional[PipeTargetStateMachineParameters] = None
    KinesisStreamParameters: Optional[PipeTargetKinesisStreamParameters] = None
    EcsTaskParameters: Optional[PipeTargetEcsTaskParameters] = None
    BatchJobParameters: Optional[PipeTargetBatchJobParameters] = None
    SqsQueueParameters: Optional[PipeTargetSqsQueueParameters] = None
    HttpParameters: Optional[PipeTargetHttpParameters] = None
    RedshiftDataParameters: Optional[PipeTargetRedshiftDataParameters] = None
    SageMakerPipelineParameters: Optional[PipeTargetSageMakerPipelineParameters] = None
    EventBridgeEventBusParameters: Optional[PipeTargetEventBridgeEventBusParameters] = None
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParameters] = None
    TimestreamParameters: Optional[PipeTargetTimestreamParameters] = None


class DescribePipeResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    StateReason: str
    Source: str
    SourceParameters: PipeSourceParametersOutput
    Enrichment: str
    EnrichmentParameters: PipeEnrichmentParametersOutput
    Target: str
    TargetParameters: PipeTargetParametersOutput
    RoleArn: str
    Tags: Dict[str, str]
    CreationTime: datetime
    LastModifiedTime: datetime
    LogConfiguration: PipeLogConfiguration
    KmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadata

PipeTargetParametersUnion = Union[PipeTargetParameters, PipeTargetParametersOutput]


class CreatePipeRequest(BaseValidatorModel):
    Name: str
    Source: str
    Target: str
    RoleArn: str
    Description: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    SourceParameters: Optional[PipeSourceParametersUnion] = None
    Enrichment: Optional[str] = None
    EnrichmentParameters: Optional[PipeEnrichmentParametersUnion] = None
    TargetParameters: Optional[PipeTargetParametersUnion] = None
    Tags: Optional[Dict[str, str]] = None
    LogConfiguration: Optional[PipeLogConfigurationParameters] = None
    KmsKeyIdentifier: Optional[str] = None


class UpdatePipeRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    Description: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    SourceParameters: Optional[UpdatePipeSourceParameters] = None
    Enrichment: Optional[str] = None
    EnrichmentParameters: Optional[PipeEnrichmentParametersUnion] = None
    Target: Optional[str] = None
    TargetParameters: Optional[PipeTargetParametersUnion] = None
    LogConfiguration: Optional[PipeLogConfigurationParameters] = None
    KmsKeyIdentifier: Optional[str] = None