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
from aws_resource_validator.pydantic_models.pipes_constants import *

class AwsVpcConfigurationOutputTypeDef(BaseModel):
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class AwsVpcConfigurationTypeDef(BaseModel):
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    AssignPublicIp: Optional[AssignPublicIpType] = None

class BatchArrayPropertiesTypeDef(BaseModel):
    Size: Optional[int] = None

class BatchEnvironmentVariableTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class BatchResourceRequirementTypeDef(BaseModel):
    Type: BatchResourceRequirementTypeType
    Value: str

class BatchJobDependencyTypeDef(BaseModel):
    JobId: Optional[str] = None
    Type: Optional[BatchJobDependencyTypeType] = None

class BatchRetryStrategyTypeDef(BaseModel):
    Attempts: Optional[int] = None

class CapacityProviderStrategyItemTypeDef(BaseModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None

class CloudwatchLogsLogDestinationParametersTypeDef(BaseModel):
    LogGroupArn: str

class CloudwatchLogsLogDestinationTypeDef(BaseModel):
    LogGroupArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeadLetterConfigTypeDef(BaseModel):
    Arn: Optional[str] = None

class DeletePipeRequestRequestTypeDef(BaseModel):
    Name: str

class DescribePipeRequestRequestTypeDef(BaseModel):
    Name: str

class DimensionMappingTypeDef(BaseModel):
    DimensionValue: str
    DimensionValueType: Literal["VARCHAR"]
    DimensionName: str

class EcsEnvironmentFileTypeDef(BaseModel):
    type: Literal["s3"]
    value: str

class EcsEnvironmentVariableTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class EcsResourceRequirementTypeDef(BaseModel):
    type: EcsResourceRequirementTypeType
    value: str

class EcsEphemeralStorageTypeDef(BaseModel):
    sizeInGiB: int

class EcsInferenceAcceleratorOverrideTypeDef(BaseModel):
    deviceName: Optional[str] = None
    deviceType: Optional[str] = None

class FilterTypeDef(BaseModel):
    Pattern: Optional[str] = None

class FirehoseLogDestinationParametersTypeDef(BaseModel):
    DeliveryStreamArn: str

class FirehoseLogDestinationTypeDef(BaseModel):
    DeliveryStreamArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPipesRequestRequestTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    SourcePrefix: Optional[str] = None
    TargetPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class PipeTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MQBrokerAccessCredentialsTypeDef(BaseModel):
    BasicAuth: Optional[str] = None

class MSKAccessCredentialsTypeDef(BaseModel):
    SaslScram512Auth: Optional[str] = None
    ClientCertificateTlsAuth: Optional[str] = None

class MultiMeasureAttributeMappingTypeDef(BaseModel):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MultiMeasureAttributeName: str

class PipeEnrichmentHttpParametersOutputTypeDef(BaseModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None

class PipeEnrichmentHttpParametersTypeDef(BaseModel):
    PathParameterValues: Optional[Sequence[str]] = None
    HeaderParameters: Optional[Mapping[str, str]] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None

class S3LogDestinationParametersTypeDef(BaseModel):
    BucketName: str
    BucketOwner: str
    OutputFormat: Optional[S3OutputFormatType] = None
    Prefix: Optional[str] = None

class S3LogDestinationTypeDef(BaseModel):
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None
    OutputFormat: Optional[S3OutputFormatType] = None

class PipeSourceSqsQueueParametersTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class SelfManagedKafkaAccessConfigurationCredentialsTypeDef(BaseModel):
    BasicAuth: Optional[str] = None
    SaslScram512Auth: Optional[str] = None
    SaslScram256Auth: Optional[str] = None
    ClientCertificateTlsAuth: Optional[str] = None

class SelfManagedKafkaAccessConfigurationVpcOutputTypeDef(BaseModel):
    Subnets: Optional[List[str]] = None
    SecurityGroup: Optional[List[str]] = None

class SelfManagedKafkaAccessConfigurationVpcTypeDef(BaseModel):
    Subnets: Optional[Sequence[str]] = None
    SecurityGroup: Optional[Sequence[str]] = None

class PipeTargetCloudWatchLogsParametersTypeDef(BaseModel):
    LogStreamName: Optional[str] = None
    Timestamp: Optional[str] = None

class PlacementConstraintTypeDef(BaseModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None

class PlacementStrategyTypeDef(BaseModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class PipeTargetEventBridgeEventBusParametersOutputTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    DetailType: Optional[str] = None
    Source: Optional[str] = None
    Resources: Optional[List[str]] = None
    Time: Optional[str] = None

class PipeTargetEventBridgeEventBusParametersTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    DetailType: Optional[str] = None
    Source: Optional[str] = None
    Resources: Optional[Sequence[str]] = None
    Time: Optional[str] = None

class PipeTargetHttpParametersOutputTypeDef(BaseModel):
    PathParameterValues: Optional[List[str]] = None
    HeaderParameters: Optional[Dict[str, str]] = None
    QueryStringParameters: Optional[Dict[str, str]] = None

class PipeTargetHttpParametersTypeDef(BaseModel):
    PathParameterValues: Optional[Sequence[str]] = None
    HeaderParameters: Optional[Mapping[str, str]] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None

class PipeTargetKinesisStreamParametersTypeDef(BaseModel):
    PartitionKey: str

class PipeTargetLambdaFunctionParametersTypeDef(BaseModel):
    InvocationType: Optional[PipeTargetInvocationTypeType] = None

class PipeTargetRedshiftDataParametersOutputTypeDef(BaseModel):
    Database: str
    Sqls: List[str]
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None

class PipeTargetSqsQueueParametersTypeDef(BaseModel):
    MessageGroupId: Optional[str] = None
    MessageDeduplicationId: Optional[str] = None

class PipeTargetStateMachineParametersTypeDef(BaseModel):
    InvocationType: Optional[PipeTargetInvocationTypeType] = None

class PipeTargetRedshiftDataParametersTypeDef(BaseModel):
    Database: str
    Sqls: Sequence[str]
    SecretManagerArn: Optional[str] = None
    DbUser: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None

class SageMakerPipelineParameterTypeDef(BaseModel):
    Name: str
    Value: str

class SingleMeasureMappingTypeDef(BaseModel):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MeasureName: str

class StartPipeRequestRequestTypeDef(BaseModel):
    Name: str

class StopPipeRequestRequestTypeDef(BaseModel):
    Name: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePipeSourceSqsQueueParametersTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class NetworkConfigurationOutputTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutputTypeDef] = None

class NetworkConfigurationTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None

class BatchContainerOverridesOutputTypeDef(BaseModel):
    Command: Optional[List[str]] = None
    Environment: Optional[List[BatchEnvironmentVariableTypeDef]] = None
    InstanceType: Optional[str] = None
    ResourceRequirements: Optional[List[BatchResourceRequirementTypeDef]] = None

class BatchContainerOverridesTypeDef(BaseModel):
    Command: Optional[Sequence[str]] = None
    Environment: Optional[Sequence[BatchEnvironmentVariableTypeDef]] = None
    InstanceType: Optional[str] = None
    ResourceRequirements: Optional[Sequence[BatchResourceRequirementTypeDef]] = None

class CreatePipeResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePipeResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipeResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipeResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipeResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PipeSourceDynamoDBStreamParametersTypeDef(BaseModel):
    StartingPosition: DynamoDBStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None

class PipeSourceKinesisStreamParametersOutputTypeDef(BaseModel):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPositionTimestamp: Optional[datetime] = None

class UpdatePipeSourceDynamoDBStreamParametersTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None

class UpdatePipeSourceKinesisStreamParametersTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None

class EcsContainerOverrideOutputTypeDef(BaseModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    Environment: Optional[List[EcsEnvironmentVariableTypeDef]] = None
    EnvironmentFiles: Optional[List[EcsEnvironmentFileTypeDef]] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    Name: Optional[str] = None
    ResourceRequirements: Optional[List[EcsResourceRequirementTypeDef]] = None

class EcsContainerOverrideTypeDef(BaseModel):
    Command: Optional[Sequence[str]] = None
    Cpu: Optional[int] = None
    Environment: Optional[Sequence[EcsEnvironmentVariableTypeDef]] = None
    EnvironmentFiles: Optional[Sequence[EcsEnvironmentFileTypeDef]] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    Name: Optional[str] = None
    ResourceRequirements: Optional[Sequence[EcsResourceRequirementTypeDef]] = None

class FilterCriteriaOutputTypeDef(BaseModel):
    Filters: Optional[List[FilterTypeDef]] = None

class FilterCriteriaTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListPipesRequestListPipesPaginateTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    CurrentState: Optional[PipeStateType] = None
    SourcePrefix: Optional[str] = None
    TargetPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipesResponseTypeDef(BaseModel):
    Pipes: List[PipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PipeSourceActiveMQBrokerParametersTypeDef(BaseModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    QueueName: str
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class PipeSourceRabbitMQBrokerParametersTypeDef(BaseModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    QueueName: str
    VirtualHost: Optional[str] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class UpdatePipeSourceActiveMQBrokerParametersTypeDef(BaseModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class UpdatePipeSourceRabbitMQBrokerParametersTypeDef(BaseModel):
    Credentials: MQBrokerAccessCredentialsTypeDef
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class PipeSourceManagedStreamingKafkaParametersTypeDef(BaseModel):
    TopicName: str
    StartingPosition: Optional[MSKStartPositionType] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[MSKAccessCredentialsTypeDef] = None

class UpdatePipeSourceManagedStreamingKafkaParametersTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    Credentials: Optional[MSKAccessCredentialsTypeDef] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None

class MultiMeasureMappingOutputTypeDef(BaseModel):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMappingTypeDef]

class MultiMeasureMappingTypeDef(BaseModel):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]

class PipeEnrichmentParametersOutputTypeDef(BaseModel):
    InputTemplate: Optional[str] = None
    HttpParameters: Optional[PipeEnrichmentHttpParametersOutputTypeDef] = None

class PipeEnrichmentParametersTypeDef(BaseModel):
    InputTemplate: Optional[str] = None
    HttpParameters: Optional[PipeEnrichmentHttpParametersTypeDef] = None

class PipeLogConfigurationParametersTypeDef(BaseModel):
    Level: LogLevelType
    S3LogDestination: Optional[S3LogDestinationParametersTypeDef] = None
    FirehoseLogDestination: Optional[FirehoseLogDestinationParametersTypeDef] = None
    CloudwatchLogsLogDestination: Optional[CloudwatchLogsLogDestinationParametersTypeDef] = None
    IncludeExecutionData: Optional[Sequence[Literal["ALL"]]] = None

class PipeLogConfigurationTypeDef(BaseModel):
    S3LogDestination: Optional[S3LogDestinationTypeDef] = None
    FirehoseLogDestination: Optional[FirehoseLogDestinationTypeDef] = None
    CloudwatchLogsLogDestination: Optional[CloudwatchLogsLogDestinationTypeDef] = None
    Level: Optional[LogLevelType] = None
    IncludeExecutionData: Optional[List[Literal["ALL"]]] = None

class PipeSourceKinesisStreamParametersTypeDef(BaseModel):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: Optional[int] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    OnPartialBatchItemFailure: Optional[Literal["AUTOMATIC_BISECT"]] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPositionTimestamp: Optional[TimestampTypeDef] = None

class PipeSourceSelfManagedKafkaParametersOutputTypeDef(BaseModel):
    TopicName: str
    StartingPosition: Optional[SelfManagedKafkaStartPositionType] = None
    AdditionalBootstrapServers: Optional[List[str]] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsTypeDef] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcOutputTypeDef] = None

class PipeSourceSelfManagedKafkaParametersTypeDef(BaseModel):
    TopicName: str
    StartingPosition: Optional[SelfManagedKafkaStartPositionType] = None
    AdditionalBootstrapServers: Optional[Sequence[str]] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ConsumerGroupID: Optional[str] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsTypeDef] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcTypeDef] = None

class UpdatePipeSourceSelfManagedKafkaParametersTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsTypeDef] = None
    ServerRootCaCertificate: Optional[str] = None
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpcTypeDef] = None

class PipeTargetSageMakerPipelineParametersOutputTypeDef(BaseModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameterTypeDef]] = None

class PipeTargetSageMakerPipelineParametersTypeDef(BaseModel):
    PipelineParameterList: Optional[Sequence[SageMakerPipelineParameterTypeDef]] = None

class PipeTargetBatchJobParametersOutputTypeDef(BaseModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayPropertiesTypeDef] = None
    RetryStrategy: Optional[BatchRetryStrategyTypeDef] = None
    ContainerOverrides: Optional[BatchContainerOverridesOutputTypeDef] = None
    DependsOn: Optional[List[BatchJobDependencyTypeDef]] = None
    Parameters: Optional[Dict[str, str]] = None

class PipeTargetBatchJobParametersTypeDef(BaseModel):
    JobDefinition: str
    JobName: str
    ArrayProperties: Optional[BatchArrayPropertiesTypeDef] = None
    RetryStrategy: Optional[BatchRetryStrategyTypeDef] = None
    ContainerOverrides: Optional[BatchContainerOverridesTypeDef] = None
    DependsOn: Optional[Sequence[BatchJobDependencyTypeDef]] = None
    Parameters: Optional[Mapping[str, str]] = None

class EcsTaskOverrideOutputTypeDef(BaseModel):
    ContainerOverrides: Optional[List[EcsContainerOverrideOutputTypeDef]] = None
    Cpu: Optional[str] = None
    EphemeralStorage: Optional[EcsEphemeralStorageTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    InferenceAcceleratorOverrides: Optional[List[EcsInferenceAcceleratorOverrideTypeDef]] = None
    Memory: Optional[str] = None
    TaskRoleArn: Optional[str] = None

class EcsTaskOverrideTypeDef(BaseModel):
    ContainerOverrides: Optional[Sequence[EcsContainerOverrideTypeDef]] = None
    Cpu: Optional[str] = None
    EphemeralStorage: Optional[EcsEphemeralStorageTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    InferenceAcceleratorOverrides: Optional[       Sequence[EcsInferenceAcceleratorOverrideTypeDef]     ] = None
    Memory: Optional[str] = None
    TaskRoleArn: Optional[str] = None

class PipeTargetTimestreamParametersOutputTypeDef(BaseModel):
    TimeValue: str
    VersionValue: str
    DimensionMappings: List[DimensionMappingTypeDef]
    EpochTimeUnit: Optional[EpochTimeUnitType] = None
    TimeFieldType: Optional[TimeFieldTypeType] = None
    TimestampFormat: Optional[str] = None
    SingleMeasureMappings: Optional[List[SingleMeasureMappingTypeDef]] = None
    MultiMeasureMappings: Optional[List[MultiMeasureMappingOutputTypeDef]] = None

class PipeTargetTimestreamParametersTypeDef(BaseModel):
    TimeValue: str
    VersionValue: str
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    EpochTimeUnit: Optional[EpochTimeUnitType] = None
    TimeFieldType: Optional[TimeFieldTypeType] = None
    TimestampFormat: Optional[str] = None
    SingleMeasureMappings: Optional[Sequence[SingleMeasureMappingTypeDef]] = None
    MultiMeasureMappings: Optional[Sequence[MultiMeasureMappingTypeDef]] = None

class PipeSourceParametersOutputTypeDef(BaseModel):
    FilterCriteria: Optional[FilterCriteriaOutputTypeDef] = None
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParametersOutputTypeDef] = None
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParametersTypeDef] = None
    SqsQueueParameters: Optional[PipeSourceSqsQueueParametersTypeDef] = None
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParametersTypeDef] = None
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParametersTypeDef] = None
    ManagedStreamingKafkaParameters: Optional[       PipeSourceManagedStreamingKafkaParametersTypeDef     ] = None
    SelfManagedKafkaParameters: Optional[       PipeSourceSelfManagedKafkaParametersOutputTypeDef     ] = None

class PipeSourceParametersTypeDef(BaseModel):
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParametersTypeDef] = None
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParametersTypeDef] = None
    SqsQueueParameters: Optional[PipeSourceSqsQueueParametersTypeDef] = None
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParametersTypeDef] = None
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParametersTypeDef] = None
    ManagedStreamingKafkaParameters: Optional[       PipeSourceManagedStreamingKafkaParametersTypeDef     ] = None
    SelfManagedKafkaParameters: Optional[PipeSourceSelfManagedKafkaParametersTypeDef] = None

class UpdatePipeSourceParametersTypeDef(BaseModel):
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    KinesisStreamParameters: Optional[UpdatePipeSourceKinesisStreamParametersTypeDef] = None
    DynamoDBStreamParameters: Optional[UpdatePipeSourceDynamoDBStreamParametersTypeDef] = None
    SqsQueueParameters: Optional[UpdatePipeSourceSqsQueueParametersTypeDef] = None
    ActiveMQBrokerParameters: Optional[UpdatePipeSourceActiveMQBrokerParametersTypeDef] = None
    RabbitMQBrokerParameters: Optional[UpdatePipeSourceRabbitMQBrokerParametersTypeDef] = None
    ManagedStreamingKafkaParameters: Optional[       UpdatePipeSourceManagedStreamingKafkaParametersTypeDef     ] = None
    SelfManagedKafkaParameters: Optional[       UpdatePipeSourceSelfManagedKafkaParametersTypeDef     ] = None

class PipeTargetEcsTaskParametersOutputTypeDef(BaseModel):
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

class PipeTargetEcsTaskParametersTypeDef(BaseModel):
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

class PipeTargetParametersOutputTypeDef(BaseModel):
    InputTemplate: Optional[str] = None
    LambdaFunctionParameters: Optional[PipeTargetLambdaFunctionParametersTypeDef] = None
    StepFunctionStateMachineParameters: Optional[PipeTargetStateMachineParametersTypeDef] = None
    KinesisStreamParameters: Optional[PipeTargetKinesisStreamParametersTypeDef] = None
    EcsTaskParameters: Optional[PipeTargetEcsTaskParametersOutputTypeDef] = None
    BatchJobParameters: Optional[PipeTargetBatchJobParametersOutputTypeDef] = None
    SqsQueueParameters: Optional[PipeTargetSqsQueueParametersTypeDef] = None
    HttpParameters: Optional[PipeTargetHttpParametersOutputTypeDef] = None
    RedshiftDataParameters: Optional[PipeTargetRedshiftDataParametersOutputTypeDef] = None
    SageMakerPipelineParameters: Optional[       PipeTargetSageMakerPipelineParametersOutputTypeDef     ] = None
    EventBridgeEventBusParameters: Optional[       PipeTargetEventBridgeEventBusParametersOutputTypeDef     ] = None
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParametersTypeDef] = None
    TimestreamParameters: Optional[PipeTargetTimestreamParametersOutputTypeDef] = None

class PipeTargetParametersTypeDef(BaseModel):
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
    EventBridgeEventBusParameters: Optional[       PipeTargetEventBridgeEventBusParametersTypeDef     ] = None
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParametersTypeDef] = None
    TimestreamParameters: Optional[PipeTargetTimestreamParametersTypeDef] = None

class DescribePipeResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipeRequestRequestTypeDef(BaseModel):
    Name: str
    Source: str
    Target: str
    RoleArn: str
    Description: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    SourceParameters: Optional[PipeSourceParametersTypeDef] = None
    Enrichment: Optional[str] = None
    EnrichmentParameters: Optional[PipeEnrichmentParametersTypeDef] = None
    TargetParameters: Optional[PipeTargetParametersTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    LogConfiguration: Optional[PipeLogConfigurationParametersTypeDef] = None

class UpdatePipeRequestRequestTypeDef(BaseModel):
    Name: str
    RoleArn: str
    Description: Optional[str] = None
    DesiredState: Optional[RequestedPipeStateType] = None
    SourceParameters: Optional[UpdatePipeSourceParametersTypeDef] = None
    Enrichment: Optional[str] = None
    EnrichmentParameters: Optional[PipeEnrichmentParametersTypeDef] = None
    Target: Optional[str] = None
    TargetParameters: Optional[PipeTargetParametersTypeDef] = None
    LogConfiguration: Optional[PipeLogConfigurationParametersTypeDef] = None

