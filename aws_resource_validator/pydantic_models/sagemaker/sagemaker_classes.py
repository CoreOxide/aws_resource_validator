from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker.sagemaker_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActionSource(BaseValidatorModel):
    SourceUri: str
    SourceType: Optional[str] = None
    SourceId: Optional[str] = None


class AddAssociationRequest(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    AssociationType: Optional[AssociationEdgeTypeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AdditionalS3DataSource(BaseValidatorModel):
    S3DataType: AdditionalS3DataSourceDataTypeType
    S3Uri: str
    CompressionType: Optional[CompressionTypeType] = None
    ETag: Optional[str] = None


class AgentVersion(BaseValidatorModel):
    Version: str
    AgentCount: int


class Alarm(BaseValidatorModel):
    AlarmName: Optional[str] = None


class MetricDefinition(BaseValidatorModel):
    Name: str
    Regex: str


class AlgorithmStatusItem(BaseValidatorModel):
    Name: str
    Status: DetailedAlgorithmStatusType
    FailureReason: Optional[str] = None


class AlgorithmSummary(BaseValidatorModel):
    AlgorithmName: str
    AlgorithmArn: str
    CreationTime: datetime
    AlgorithmStatus: AlgorithmStatusType
    AlgorithmDescription: Optional[str] = None


class AmazonQSettings(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None
    QProfileArn: Optional[str] = None


class AnnotationConsolidationConfig(BaseValidatorModel):
    AnnotationConsolidationLambdaArn: str


class ResourceSpec(BaseValidatorModel):
    SageMakerImageArn: Optional[str] = None
    SageMakerImageVersionArn: Optional[str] = None
    SageMakerImageVersionAlias: Optional[str] = None
    InstanceType: Optional[AppInstanceTypeType] = None
    LifecycleConfigArn: Optional[str] = None


class IdleSettings(BaseValidatorModel):
    LifecycleManagement: Optional[LifecycleManagementType] = None
    IdleTimeoutInMinutes: Optional[int] = None
    MinIdleTimeoutInMinutes: Optional[int] = None
    MaxIdleTimeoutInMinutes: Optional[int] = None


class AppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None


class AppSpecification(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None


class ArtifactSourceType(BaseValidatorModel):
    SourceIdType: ArtifactSourceIdTypeType
    Value: str


class AssociateTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str
    TrialName: str


class AsyncInferenceClientConfig(BaseValidatorModel):
    MaxConcurrentInvocationsPerInstance: Optional[int] = None


class AsyncInferenceNotificationConfigOutput(BaseValidatorModel):
    SuccessTopic: Optional[str] = None
    ErrorTopic: Optional[str] = None
    IncludeInferenceResponseIn: Optional[List[AsyncNotificationTopicTypesType]] = None


class AsyncInferenceNotificationConfig(BaseValidatorModel):
    SuccessTopic: Optional[str] = None
    ErrorTopic: Optional[str] = None
    IncludeInferenceResponseIn: Optional[List[AsyncNotificationTopicTypesType]] = None


class AthenaDatasetDefinition(BaseValidatorModel):
    Catalog: str
    Database: str
    QueryString: str
    OutputS3Uri: str
    OutputFormat: AthenaResultFormatType
    WorkGroup: Optional[str] = None
    KmsKeyId: Optional[str] = None
    OutputCompression: Optional[AthenaResultCompressionTypeType] = None


class AutoMLAlgorithmConfigOutput(BaseValidatorModel):
    AutoMLAlgorithms: List[AutoMLAlgorithmType]


class AutoMLAlgorithmConfig(BaseValidatorModel):
    AutoMLAlgorithms: List[AutoMLAlgorithmType]


class AutoMLCandidateStep(BaseValidatorModel):
    CandidateStepType: CandidateStepTypeType
    CandidateStepArn: str
    CandidateStepName: str


class AutoMLContainerDefinition(BaseValidatorModel):
    Image: str
    ModelDataUrl: str
    Environment: Optional[Dict[str, str]] = None


class FinalAutoMLJobObjectiveMetric(BaseValidatorModel):
    MetricName: AutoMLMetricEnumType
    Value: float
    Type: Optional[AutoMLJobObjectiveTypeType] = None
    StandardMetricName: Optional[AutoMLMetricEnumType] = None


class EmrServerlessComputeConfig(BaseValidatorModel):
    ExecutionRoleARN: str


class AutoMLS3DataSource(BaseValidatorModel):
    S3DataType: AutoMLS3DataTypeType
    S3Uri: str


class AutoMLDataSplitConfig(BaseValidatorModel):
    ValidationFraction: Optional[float] = None


class AutoMLJobArtifacts(BaseValidatorModel):
    CandidateDefinitionNotebookLocation: Optional[str] = None
    DataExplorationNotebookLocation: Optional[str] = None


class AutoMLJobCompletionCriteria(BaseValidatorModel):
    MaxCandidates: Optional[int] = None
    MaxRuntimePerTrainingJobInSeconds: Optional[int] = None
    MaxAutoMLJobRuntimeInSeconds: Optional[int] = None


class AutoMLJobObjective(BaseValidatorModel):
    MetricName: AutoMLMetricEnumType


class AutoMLJobStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class AutoMLPartialFailureReason(BaseValidatorModel):
    PartialFailureMessage: Optional[str] = None


class AutoMLOutputDataConfig(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None


class TabularResolvedAttributes(BaseValidatorModel):
    ProblemType: Optional[ProblemTypeType] = None


class TextGenerationResolvedAttributes(BaseValidatorModel):
    BaseModelName: Optional[str] = None


class VpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class VpcConfig(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class AutoParameter(BaseValidatorModel):
    Name: str
    ValueHint: str


class Autotune(BaseValidatorModel):
    Mode: Literal['Enabled']


class BatchDataCaptureConfig(BaseValidatorModel):
    DestinationS3Uri: str
    KmsKeyId: Optional[str] = None
    GenerateInferenceId: Optional[bool] = None


class BatchDeleteClusterNodesError(BaseValidatorModel):
    Code: BatchDeleteClusterNodesErrorCodeType
    Message: str
    NodeId: str


class BatchDeleteClusterNodesRequest(BaseValidatorModel):
    ClusterName: str
    NodeIds: List[str]


class BatchDescribeModelPackageError(BaseValidatorModel):
    ErrorCode: str
    ErrorResponse: str


class BatchDescribeModelPackageInput(BaseValidatorModel):
    ModelPackageArnList: List[str]


class BestObjectiveNotImproving(BaseValidatorModel):
    MaxNumberOfTrainingJobsNotImproving: Optional[int] = None


class MetricsSource(BaseValidatorModel):
    ContentType: str
    S3Uri: str
    ContentDigest: Optional[str] = None


class CacheHitResult(BaseValidatorModel):
    SourcePipelineExecutionArn: Optional[str] = None


class OutputParameter(BaseValidatorModel):
    Name: str
    Value: str


class CandidateArtifactLocations(BaseValidatorModel):
    Explainability: str
    ModelInsights: Optional[str] = None
    BacktestResults: Optional[str] = None


class MetricDatum(BaseValidatorModel):
    MetricName: Optional[AutoMLMetricEnumType] = None
    Value: Optional[float] = None
    Set: Optional[MetricSetSourceType] = None
    StandardMetricName: Optional[AutoMLMetricExtendedEnumType] = None


class DirectDeploySettings(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None


class EmrServerlessSettings(BaseValidatorModel):
    ExecutionRoleArn: Optional[str] = None
    Status: Optional[FeatureStatusType] = None


class GenerativeAiSettings(BaseValidatorModel):
    AmazonBedrockRoleArn: Optional[str] = None


class IdentityProviderOAuthSetting(BaseValidatorModel):
    DataSourceName: Optional[DataSourceNameType] = None
    Status: Optional[FeatureStatusType] = None
    SecretArn: Optional[str] = None


class KendraSettings(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None


class ModelRegisterSettings(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None
    CrossAccountModelRegisterRoleArn: Optional[str] = None


class TimeSeriesForecastingSettings(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None
    AmazonForecastRoleArn: Optional[str] = None


class WorkspaceSettings(BaseValidatorModel):
    S3ArtifactPath: Optional[str] = None
    S3KmsKeyId: Optional[str] = None


class CapacitySize(BaseValidatorModel):
    Type: CapacitySizeTypeType
    Value: int


class CaptureContentTypeHeaderOutput(BaseValidatorModel):
    CsvContentTypes: Optional[List[str]] = None
    JsonContentTypes: Optional[List[str]] = None


class CaptureContentTypeHeader(BaseValidatorModel):
    CsvContentTypes: Optional[List[str]] = None
    JsonContentTypes: Optional[List[str]] = None


class CaptureOption(BaseValidatorModel):
    CaptureMode: CaptureModeType


class CategoricalParameterOutput(BaseValidatorModel):
    Name: str
    Value: List[str]


class CategoricalParameterRangeOutput(BaseValidatorModel):
    Name: str
    Values: List[str]


class CategoricalParameterRangeSpecificationOutput(BaseValidatorModel):
    Values: List[str]


class CategoricalParameterRangeSpecification(BaseValidatorModel):
    Values: List[str]


class CategoricalParameterRange(BaseValidatorModel):
    Name: str
    Values: List[str]


class CategoricalParameter(BaseValidatorModel):
    Name: str
    Value: List[str]


class ShuffleConfig(BaseValidatorModel):
    Seed: int


class ChannelSpecificationOutput(BaseValidatorModel):
    Name: str
    SupportedContentTypes: List[str]
    SupportedInputModes: List[TrainingInputModeType]
    Description: Optional[str] = None
    IsRequired: Optional[bool] = None
    SupportedCompressionTypes: Optional[List[CompressionTypeType]] = None


class ChannelSpecification(BaseValidatorModel):
    Name: str
    SupportedContentTypes: List[str]
    SupportedInputModes: List[TrainingInputModeType]
    Description: Optional[str] = None
    IsRequired: Optional[bool] = None
    SupportedCompressionTypes: Optional[List[CompressionTypeType]] = None


class CheckpointConfig(BaseValidatorModel):
    S3Uri: str
    LocalPath: Optional[str] = None


class ClarifyCheckStepMetadata(BaseValidatorModel):
    CheckType: Optional[str] = None
    BaselineUsedForDriftCheckConstraints: Optional[str] = None
    CalculatedBaselineConstraints: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ViolationReport: Optional[str] = None
    CheckJobArn: Optional[str] = None
    SkipCheck: Optional[bool] = None
    RegisterNewBaseline: Optional[bool] = None


class ClarifyInferenceConfigOutput(BaseValidatorModel):
    FeaturesAttribute: Optional[str] = None
    ContentTemplate: Optional[str] = None
    MaxRecordCount: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    ProbabilityIndex: Optional[int] = None
    LabelIndex: Optional[int] = None
    ProbabilityAttribute: Optional[str] = None
    LabelAttribute: Optional[str] = None
    LabelHeaders: Optional[List[str]] = None
    FeatureHeaders: Optional[List[str]] = None
    FeatureTypes: Optional[List[ClarifyFeatureTypeType]] = None


class ClarifyInferenceConfig(BaseValidatorModel):
    FeaturesAttribute: Optional[str] = None
    ContentTemplate: Optional[str] = None
    MaxRecordCount: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    ProbabilityIndex: Optional[int] = None
    LabelIndex: Optional[int] = None
    ProbabilityAttribute: Optional[str] = None
    LabelAttribute: Optional[str] = None
    LabelHeaders: Optional[List[str]] = None
    FeatureHeaders: Optional[List[str]] = None
    FeatureTypes: Optional[List[ClarifyFeatureTypeType]] = None


class ClarifyShapBaselineConfig(BaseValidatorModel):
    MimeType: Optional[str] = None
    ShapBaseline: Optional[str] = None
    ShapBaselineUri: Optional[str] = None


class ClarifyTextConfig(BaseValidatorModel):
    Language: ClarifyTextLanguageType
    Granularity: ClarifyTextGranularityType


class ClusterEbsVolumeConfig(BaseValidatorModel):
    VolumeSizeInGB: int


class ClusterLifeCycleConfig(BaseValidatorModel):
    SourceS3Uri: str
    OnCreate: str


class ClusterInstancePlacement(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None


class ClusterInstanceStatusDetails(BaseValidatorModel):
    Status: ClusterInstanceStatusType
    Message: Optional[str] = None


class ClusterOrchestratorEksConfig(BaseValidatorModel):
    ClusterArn: str


class ClusterSchedulerConfigSummary(BaseValidatorModel):
    ClusterSchedulerConfigArn: str
    ClusterSchedulerConfigId: str
    Name: str
    CreationTime: datetime
    Status: SchedulerResourceStatusType
    ClusterSchedulerConfigVersion: Optional[int] = None
    LastModifiedTime: Optional[datetime] = None
    ClusterArn: Optional[str] = None


class ClusterSummary(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    CreationTime: datetime
    ClusterStatus: ClusterStatusType
    TrainingPlanArns: Optional[List[str]] = None


class ContainerConfigOutput(BaseValidatorModel):
    ContainerArguments: Optional[List[str]] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerEnvironmentVariables: Optional[Dict[str, str]] = None


class FileSystemConfig(BaseValidatorModel):
    MountPath: Optional[str] = None
    DefaultUid: Optional[int] = None
    DefaultGid: Optional[int] = None


class ContainerConfig(BaseValidatorModel):
    ContainerArguments: Optional[List[str]] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerEnvironmentVariables: Optional[Dict[str, str]] = None


class CustomImage(BaseValidatorModel):
    ImageName: str
    AppImageConfigName: str
    ImageVersionNumber: Optional[int] = None


class GitConfig(BaseValidatorModel):
    RepositoryUrl: str
    Branch: Optional[str] = None
    SecretArn: Optional[str] = None


class CodeRepository(BaseValidatorModel):
    RepositoryUrl: str


class CognitoConfig(BaseValidatorModel):
    UserPool: str
    ClientId: str


class CognitoMemberDefinition(BaseValidatorModel):
    UserPool: str
    UserGroup: str
    ClientId: str


class VectorConfig(BaseValidatorModel):
    Dimension: int


class CollectionConfigurationOutput(BaseValidatorModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Dict[str, str]] = None


class CollectionConfiguration(BaseValidatorModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Dict[str, str]] = None


class CompilationJobSummary(BaseValidatorModel):
    CompilationJobName: str
    CompilationJobArn: str
    CreationTime: datetime
    CompilationJobStatus: CompilationJobStatusType
    CompilationStartTime: Optional[datetime] = None
    CompilationEndTime: Optional[datetime] = None
    CompilationTargetDevice: Optional[TargetDeviceType] = None
    CompilationTargetPlatformOs: Optional[TargetPlatformOsType] = None
    CompilationTargetPlatformArch: Optional[TargetPlatformArchType] = None
    CompilationTargetPlatformAccelerator: Optional[TargetPlatformAcceleratorType] = None
    LastModifiedTime: Optional[datetime] = None


class ComputeQuotaResourceConfig(BaseValidatorModel):
    InstanceType: ClusterInstanceTypeType
    Count: int


class ResourceSharingConfig(BaseValidatorModel):
    Strategy: ResourceSharingStrategyType
    BorrowLimit: Optional[int] = None


class ComputeQuotaTarget(BaseValidatorModel):
    TeamName: str
    FairShareWeight: Optional[int] = None


class ConditionStepMetadata(BaseValidatorModel):
    Outcome: Optional[ConditionOutcomeType] = None


class MultiModelConfig(BaseValidatorModel):
    ModelCacheSetting: Optional[ModelCacheSettingType] = None


class ContextSource(BaseValidatorModel):
    SourceUri: str
    SourceType: Optional[str] = None
    SourceId: Optional[str] = None


class ContinuousParameterRangeSpecification(BaseValidatorModel):
    MinValue: str
    MaxValue: str


class ContinuousParameterRange(BaseValidatorModel):
    Name: str
    MinValue: str
    MaxValue: str
    ScalingType: Optional[HyperParameterScalingTypeType] = None


class ConvergenceDetected(BaseValidatorModel):
    CompleteOnConvergence: Optional[CompleteOnConvergenceType] = None


class MetadataProperties(BaseValidatorModel):
    CommitId: Optional[str] = None
    Repository: Optional[str] = None
    GeneratedBy: Optional[str] = None
    ProjectId: Optional[str] = None


class ModelDeployConfig(BaseValidatorModel):
    AutoGenerateEndpointName: Optional[bool] = None
    EndpointName: Optional[str] = None


class InputConfig(BaseValidatorModel):
    S3Uri: str
    Framework: FrameworkType
    DataInputConfig: Optional[str] = None
    FrameworkVersion: Optional[str] = None


class StoppingCondition(BaseValidatorModel):
    MaxRuntimeInSeconds: Optional[int] = None
    MaxWaitTimeInSeconds: Optional[int] = None
    MaxPendingTimeInSeconds: Optional[int] = None


class MonitoringStoppingCondition(BaseValidatorModel):
    MaxRuntimeInSeconds: int


class EdgeOutputConfig(BaseValidatorModel):
    S3OutputLocation: str
    KmsKeyId: Optional[str] = None
    PresetDeploymentType: Optional[Literal['GreengrassV2Component']] = None
    PresetDeploymentConfig: Optional[str] = None


class EdgeDeploymentModelConfig(BaseValidatorModel):
    ModelHandle: str
    EdgePackagingJobName: str


class ThroughputConfig(BaseValidatorModel):
    ThroughputMode: ThroughputModeType
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None


class FlowDefinitionOutputConfig(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None


class HumanLoopRequestSource(BaseValidatorModel):
    AwsManagedHumanLoopRequestSource: AwsManagedHumanLoopRequestSourceType


class HubS3StorageConfig(BaseValidatorModel):
    S3OutputPath: Optional[str] = None


class UiTemplate(BaseValidatorModel):
    Content: str


class CreateImageVersionRequest(BaseValidatorModel):
    BaseImage: str
    ClientToken: str
    ImageName: str
    Aliases: Optional[List[str]] = None
    VendorGuidance: Optional[VendorGuidanceType] = None
    JobType: Optional[JobTypeType] = None
    MLFramework: Optional[str] = None
    ProgrammingLang: Optional[str] = None
    Processor: Optional[ProcessorType] = None
    Horovod: Optional[bool] = None
    ReleaseNotes: Optional[str] = None


class InferenceComponentRuntimeConfig(BaseValidatorModel):
    CopyCount: int


class LabelingJobOutputConfig(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None
    SnsTopicArn: Optional[str] = None


class LabelingJobStoppingConditions(BaseValidatorModel):
    MaxHumanLabeledObjectCount: Optional[int] = None
    MaxPercentageOfInputDatasetLabeled: Optional[int] = None


class ModelCardExportOutputConfig(BaseValidatorModel):
    S3OutputPath: str


class ModelCardSecurityConfig(BaseValidatorModel):
    KmsKeyId: Optional[str] = None


class InferenceExecutionConfig(BaseValidatorModel):
    Mode: InferenceExecutionModeType


class ModelLifeCycle(BaseValidatorModel):
    Stage: str
    StageStatus: str
    StageDescription: Optional[str] = None


class ModelPackageModelCard(BaseValidatorModel):
    ModelCardContent: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None


class ModelPackageSecurityConfig(BaseValidatorModel):
    KmsKeyId: str


class InstanceMetadataServiceConfiguration(BaseValidatorModel):
    MinimumInstanceMetadataServiceVersion: str


class NotebookInstanceLifecycleHook(BaseValidatorModel):
    Content: Optional[str] = None


class OptimizationJobOutputConfig(BaseValidatorModel):
    S3OutputLocation: str
    KmsKeyId: Optional[str] = None


class CreatePartnerAppPresignedUrlRequest(BaseValidatorModel):
    Arn: str
    ExpiresInSeconds: Optional[int] = None
    SessionExpirationDurationInSeconds: Optional[int] = None


class PartnerAppMaintenanceConfig(BaseValidatorModel):
    MaintenanceWindowStart: Optional[str] = None


class ParallelismConfiguration(BaseValidatorModel):
    MaxParallelExecutionSteps: int


class PipelineDefinitionS3Location(BaseValidatorModel):
    Bucket: str
    ObjectKey: str
    VersionId: Optional[str] = None


class CreatePresignedDomainUrlRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    SessionExpirationDurationInSeconds: Optional[int] = None
    ExpiresInSeconds: Optional[int] = None
    SpaceName: Optional[str] = None
    LandingUri: Optional[str] = None


class CreatePresignedMlflowTrackingServerUrlRequest(BaseValidatorModel):
    TrackingServerName: str
    ExpiresInSeconds: Optional[int] = None
    SessionExpirationDurationInSeconds: Optional[int] = None


class CreatePresignedNotebookInstanceUrlInput(BaseValidatorModel):
    NotebookInstanceName: str
    SessionExpirationDurationInSeconds: Optional[int] = None


class ExperimentConfig(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    TrialComponentDisplayName: Optional[str] = None
    RunName: Optional[str] = None


class ProcessingStoppingCondition(BaseValidatorModel):
    MaxRuntimeInSeconds: int


class OwnershipSettings(BaseValidatorModel):
    OwnerUserProfileName: str


class SpaceSharingSettings(BaseValidatorModel):
    SharingType: SharingTypeType


class InfraCheckConfig(BaseValidatorModel):
    EnableInfraCheck: Optional[bool] = None


class OutputDataConfig(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None
    CompressionType: Optional[OutputCompressionTypeType] = None


class RemoteDebugConfig(BaseValidatorModel):
    EnableRemoteDebug: Optional[bool] = None


class RetryStrategy(BaseValidatorModel):
    MaximumRetryAttempts: int


class SessionChainingConfig(BaseValidatorModel):
    EnableSessionTagChaining: Optional[bool] = None


class TensorBoardOutputConfig(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None


class DataProcessing(BaseValidatorModel):
    InputFilter: Optional[str] = None
    OutputFilter: Optional[str] = None
    JoinSource: Optional[JoinSourceType] = None


class ModelClientConfig(BaseValidatorModel):
    InvocationsTimeoutInSeconds: Optional[int] = None
    InvocationsMaxRetries: Optional[int] = None


class TransformOutput(BaseValidatorModel):
    S3OutputPath: str
    Accept: Optional[str] = None
    AssembleWith: Optional[AssemblyTypeType] = None
    KmsKeyId: Optional[str] = None


class TransformResources(BaseValidatorModel):
    InstanceType: TransformInstanceTypeType
    InstanceCount: int
    VolumeKmsKeyId: Optional[str] = None

Timestamp = Union[datetime, str]


class TrialComponentArtifact(BaseValidatorModel):
    Value: str
    MediaType: Optional[str] = None


class TrialComponentParameterValue(BaseValidatorModel):
    StringValue: Optional[str] = None
    NumberValue: Optional[float] = None


class TrialComponentStatus(BaseValidatorModel):
    PrimaryStatus: Optional[TrialComponentPrimaryStatusType] = None
    Message: Optional[str] = None


class OidcConfig(BaseValidatorModel):
    ClientId: str
    ClientSecret: str
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    LogoutEndpoint: str
    JwksUri: str
    Scope: Optional[str] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None


class WorkforceVpcConfigRequest(BaseValidatorModel):
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None


class NotificationConfiguration(BaseValidatorModel):
    NotificationTopicArn: Optional[str] = None


class EFSFileSystemConfig(BaseValidatorModel):
    FileSystemId: str
    FileSystemPath: Optional[str] = None


class FSxLustreFileSystemConfig(BaseValidatorModel):
    FileSystemId: str
    FileSystemPath: Optional[str] = None


class EFSFileSystem(BaseValidatorModel):
    FileSystemId: str


class FSxLustreFileSystem(BaseValidatorModel):
    FileSystemId: str


class CustomPosixUserConfig(BaseValidatorModel):
    Uid: int
    Gid: int


class CustomizedMetricSpecification(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None


class DataCaptureConfigSummary(BaseValidatorModel):
    EnableCapture: bool
    CaptureStatus: CaptureStatusType
    CurrentSamplingPercentage: int
    DestinationS3Uri: str
    KmsKeyId: str


class DataCatalogConfig(BaseValidatorModel):
    TableName: str
    Catalog: str
    Database: str


class DataQualityAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None


class DataQualityAppSpecification(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None


class MonitoringConstraintsResource(BaseValidatorModel):
    S3Uri: Optional[str] = None


class MonitoringStatisticsResource(BaseValidatorModel):
    S3Uri: Optional[str] = None


class EndpointInput(BaseValidatorModel):
    EndpointName: str
    LocalPath: str
    S3InputMode: Optional[ProcessingS3InputModeType] = None
    S3DataDistributionType: Optional[ProcessingS3DataDistributionTypeType] = None
    FeaturesAttribute: Optional[str] = None
    InferenceAttribute: Optional[str] = None
    ProbabilityAttribute: Optional[str] = None
    ProbabilityThresholdAttribute: Optional[float] = None
    StartTimeOffset: Optional[str] = None
    EndTimeOffset: Optional[str] = None
    ExcludeFeaturesAttribute: Optional[str] = None


class FileSystemDataSource(BaseValidatorModel):
    FileSystemId: str
    FileSystemAccessMode: FileSystemAccessModeType
    FileSystemType: FileSystemTypeType
    DirectoryPath: str


class RedshiftDatasetDefinition(BaseValidatorModel):
    ClusterId: str
    Database: str
    DbUser: str
    QueryString: str
    ClusterRoleArn: str
    OutputS3Uri: str
    OutputFormat: RedshiftResultFormatType
    KmsKeyId: Optional[str] = None
    OutputCompression: Optional[RedshiftResultCompressionTypeType] = None


class DebugRuleConfigurationOutput(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None


class DebugRuleConfiguration(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None


class DebugRuleEvaluationStatus(BaseValidatorModel):
    RuleConfigurationName: Optional[str] = None
    RuleEvaluationJobArn: Optional[str] = None
    RuleEvaluationStatus: Optional[RuleEvaluationStatusType] = None
    StatusDetails: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None


class DefaultEbsStorageSettings(BaseValidatorModel):
    DefaultEbsVolumeSizeInGb: int
    MaximumEbsVolumeSizeInGb: int


class DeleteActionRequest(BaseValidatorModel):
    ActionName: str


class DeleteAlgorithmInput(BaseValidatorModel):
    AlgorithmName: str


class DeleteAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str


class DeleteAppRequest(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None


class DeleteAssociationRequest(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str


class DeleteClusterRequest(BaseValidatorModel):
    ClusterName: str


class DeleteClusterSchedulerConfigRequest(BaseValidatorModel):
    ClusterSchedulerConfigId: str


class DeleteCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str


class DeleteCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str


class DeleteComputeQuotaRequest(BaseValidatorModel):
    ComputeQuotaId: str


class DeleteContextRequest(BaseValidatorModel):
    ContextName: str


class DeleteDataQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class DeleteDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str


class RetentionPolicy(BaseValidatorModel):
    HomeEfsFileSystem: Optional[RetentionTypeType] = None


class DeleteEdgeDeploymentPlanRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str


class DeleteEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str


class DeleteEndpointConfigInput(BaseValidatorModel):
    EndpointConfigName: str


class DeleteEndpointInput(BaseValidatorModel):
    EndpointName: str


class DeleteExperimentRequest(BaseValidatorModel):
    ExperimentName: str


class DeleteFeatureGroupRequest(BaseValidatorModel):
    FeatureGroupName: str


class DeleteFlowDefinitionRequest(BaseValidatorModel):
    FlowDefinitionName: str


class DeleteHubContentReferenceRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str


class DeleteHubContentRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: str


class DeleteHubRequest(BaseValidatorModel):
    HubName: str


class DeleteHumanTaskUiRequest(BaseValidatorModel):
    HumanTaskUiName: str


class DeleteHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str


class DeleteImageRequest(BaseValidatorModel):
    ImageName: str


class DeleteImageVersionRequest(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None


class DeleteInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str


class DeleteInferenceExperimentRequest(BaseValidatorModel):
    Name: str


class DeleteMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


class DeleteModelBiasJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class DeleteModelCardRequest(BaseValidatorModel):
    ModelCardName: str


class DeleteModelExplainabilityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class DeleteModelInput(BaseValidatorModel):
    ModelName: str


class DeleteModelPackageGroupInput(BaseValidatorModel):
    ModelPackageGroupName: str


class DeleteModelPackageGroupPolicyInput(BaseValidatorModel):
    ModelPackageGroupName: str


class DeleteModelPackageInput(BaseValidatorModel):
    ModelPackageName: str


class DeleteModelQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class DeleteMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


class DeleteNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


class DeleteNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str


class DeleteOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str


class DeletePartnerAppRequest(BaseValidatorModel):
    Arn: str
    ClientToken: Optional[str] = None


class DeletePipelineRequest(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str


class DeleteProjectInput(BaseValidatorModel):
    ProjectName: str


class DeleteSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str


class DeleteStudioLifecycleConfigRequest(BaseValidatorModel):
    StudioLifecycleConfigName: str


class DeleteTagsInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class DeleteTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str


class DeleteTrialRequest(BaseValidatorModel):
    TrialName: str


class DeleteUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str


class DeleteWorkforceRequest(BaseValidatorModel):
    WorkforceName: str


class DeleteWorkteamRequest(BaseValidatorModel):
    WorkteamName: str


class DeployedImage(BaseValidatorModel):
    SpecifiedImage: Optional[str] = None
    ResolvedImage: Optional[str] = None
    ResolutionTime: Optional[datetime] = None


class RealTimeInferenceRecommendation(BaseValidatorModel):
    RecommendationId: str
    InstanceType: ProductionVariantInstanceTypeType
    Environment: Optional[Dict[str, str]] = None


class DeviceSelectionConfigOutput(BaseValidatorModel):
    DeviceSubsetType: DeviceSubsetTypeType
    Percentage: Optional[int] = None
    DeviceNames: Optional[List[str]] = None
    DeviceNameContains: Optional[str] = None


class EdgeDeploymentConfig(BaseValidatorModel):
    FailureHandlingPolicy: FailureHandlingPolicyType


class EdgeDeploymentStatus(BaseValidatorModel):
    StageStatus: StageStatusType
    EdgeDeploymentSuccessInStage: int
    EdgeDeploymentPendingInStage: int
    EdgeDeploymentFailedInStage: int
    EdgeDeploymentStatusMessage: Optional[str] = None
    EdgeDeploymentStageStartTime: Optional[datetime] = None


class DeregisterDevicesRequest(BaseValidatorModel):
    DeviceFleetName: str
    DeviceNames: List[str]


class DerivedInformation(BaseValidatorModel):
    DerivedDataInputConfig: Optional[str] = None


class DescribeActionRequest(BaseValidatorModel):
    ActionName: str


class DescribeAlgorithmInput(BaseValidatorModel):
    AlgorithmName: str


class DescribeAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str


class DescribeAppRequest(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None


class DescribeArtifactRequest(BaseValidatorModel):
    ArtifactArn: str


class DescribeAutoMLJobRequest(BaseValidatorModel):
    AutoMLJobName: str


class ModelDeployResult(BaseValidatorModel):
    EndpointName: Optional[str] = None


class DescribeAutoMLJobV2Request(BaseValidatorModel):
    AutoMLJobName: str


class DescribeClusterNodeRequest(BaseValidatorModel):
    ClusterName: str
    NodeId: str


class DescribeClusterRequest(BaseValidatorModel):
    ClusterName: str


class DescribeClusterSchedulerConfigRequest(BaseValidatorModel):
    ClusterSchedulerConfigId: str
    ClusterSchedulerConfigVersion: Optional[int] = None


class DescribeCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str


class DescribeCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str


class ModelArtifacts(BaseValidatorModel):
    S3ModelArtifacts: str


class ModelDigests(BaseValidatorModel):
    ArtifactDigest: Optional[str] = None


class NeoVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class DescribeComputeQuotaRequest(BaseValidatorModel):
    ComputeQuotaId: str
    ComputeQuotaVersion: Optional[int] = None


class DescribeContextRequest(BaseValidatorModel):
    ContextName: str


class DescribeDataQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class DescribeDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str


class DescribeDeviceRequest(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str
    NextToken: Optional[str] = None


class EdgeModel(BaseValidatorModel):
    ModelName: str
    ModelVersion: str
    LatestSampleTime: Optional[datetime] = None
    LatestInference: Optional[datetime] = None


class DescribeDomainRequest(BaseValidatorModel):
    DomainId: str


class DescribeEdgeDeploymentPlanRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeEdgePackagingJobRequest(BaseValidatorModel):
    EdgePackagingJobName: str


class EdgePresetDeploymentOutput(BaseValidatorModel):
    Type: Literal['GreengrassV2Component']
    Artifact: Optional[str] = None
    Status: Optional[EdgePresetDeploymentStatusType] = None
    StatusMessage: Optional[str] = None


class DescribeEndpointConfigInput(BaseValidatorModel):
    EndpointConfigName: str


class DescribeEndpointInput(BaseValidatorModel):
    EndpointName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeExperimentRequest(BaseValidatorModel):
    ExperimentName: str


class ExperimentSource(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None


class DescribeFeatureGroupRequest(BaseValidatorModel):
    FeatureGroupName: str
    NextToken: Optional[str] = None


class LastUpdateStatus(BaseValidatorModel):
    Status: LastUpdateStatusValueType
    FailureReason: Optional[str] = None


class OfflineStoreStatus(BaseValidatorModel):
    Status: OfflineStoreStatusValueType
    BlockedReason: Optional[str] = None


class ThroughputConfigDescription(BaseValidatorModel):
    ThroughputMode: ThroughputModeType
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None


class DescribeFeatureMetadataRequest(BaseValidatorModel):
    FeatureGroupName: str
    FeatureName: str


class FeatureParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeFlowDefinitionRequest(BaseValidatorModel):
    FlowDefinitionName: str


class DescribeHubContentRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: Optional[str] = None


class HubContentDependency(BaseValidatorModel):
    DependencyOriginPath: Optional[str] = None
    DependencyCopyPath: Optional[str] = None


class DescribeHubRequest(BaseValidatorModel):
    HubName: str


class DescribeHumanTaskUiRequest(BaseValidatorModel):
    HumanTaskUiName: str


class UiTemplateInfo(BaseValidatorModel):
    Url: Optional[str] = None
    ContentSha256: Optional[str] = None


class DescribeHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str


class HyperParameterTuningJobCompletionDetails(BaseValidatorModel):
    NumberOfTrainingJobsObjectiveNotImproving: Optional[int] = None
    ConvergenceDetectedTime: Optional[datetime] = None


class HyperParameterTuningJobConsumedResources(BaseValidatorModel):
    RuntimeInSeconds: Optional[int] = None


class ObjectiveStatusCounters(BaseValidatorModel):
    Succeeded: Optional[int] = None
    Pending: Optional[int] = None
    Failed: Optional[int] = None


class TrainingJobStatusCounters(BaseValidatorModel):
    Completed: Optional[int] = None
    InProgress: Optional[int] = None
    RetryableError: Optional[int] = None
    NonRetryableError: Optional[int] = None
    Stopped: Optional[int] = None


class DescribeImageRequest(BaseValidatorModel):
    ImageName: str


class DescribeImageVersionRequest(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None


class DescribeInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str


class InferenceComponentRuntimeConfigSummary(BaseValidatorModel):
    DesiredCopyCount: Optional[int] = None
    CurrentCopyCount: Optional[int] = None


class DescribeInferenceExperimentRequest(BaseValidatorModel):
    Name: str


class EndpointMetadata(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: Optional[str] = None
    EndpointStatus: Optional[EndpointStatusType] = None
    FailureReason: Optional[str] = None


class InferenceExperimentScheduleOutput(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class DescribeInferenceRecommendationsJobRequest(BaseValidatorModel):
    JobName: str


class DescribeLabelingJobRequest(BaseValidatorModel):
    LabelingJobName: str


class LabelCounters(BaseValidatorModel):
    TotalLabeled: Optional[int] = None
    HumanLabeled: Optional[int] = None
    MachineLabeled: Optional[int] = None
    FailedNonRetryableError: Optional[int] = None
    Unlabeled: Optional[int] = None


class LabelingJobOutput(BaseValidatorModel):
    OutputDatasetS3Uri: str
    FinalActiveLearningModelArn: Optional[str] = None


class DescribeLineageGroupRequest(BaseValidatorModel):
    LineageGroupName: str


class DescribeMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


class DescribeModelBiasJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class ModelBiasAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None


class DescribeModelCardExportJobRequest(BaseValidatorModel):
    ModelCardExportJobArn: str


class ModelCardExportArtifacts(BaseValidatorModel):
    S3ExportArtifacts: str


class DescribeModelCardRequest(BaseValidatorModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None


class DescribeModelExplainabilityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class ModelExplainabilityAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None


class DescribeModelInput(BaseValidatorModel):
    ModelName: str


class DescribeModelPackageGroupInput(BaseValidatorModel):
    ModelPackageGroupName: str


class DescribeModelPackageInput(BaseValidatorModel):
    ModelPackageName: str


class DescribeModelQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class ModelQualityAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    ProblemType: Optional[MonitoringProblemTypeType] = None
    Environment: Optional[Dict[str, str]] = None


class DescribeMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


class MonitoringExecutionSummary(BaseValidatorModel):
    MonitoringScheduleName: str
    ScheduledTime: datetime
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringExecutionStatus: ExecutionStatusType
    ProcessingJobArn: Optional[str] = None
    EndpointName: Optional[str] = None
    FailureReason: Optional[str] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None


class DescribeNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


class DescribeNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str


class DescribeOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str


class OptimizationOutput(BaseValidatorModel):
    RecommendedInferenceImage: Optional[str] = None


class OptimizationVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class DescribePartnerAppRequest(BaseValidatorModel):
    Arn: str


class ErrorInfo(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None


class PartnerAppConfigOutput(BaseValidatorModel):
    AdminUsers: Optional[List[str]] = None
    Arguments: Optional[Dict[str, str]] = None


class DescribePipelineDefinitionForExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str


class DescribePipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str


class PipelineExperimentConfig(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None


class DescribePipelineRequest(BaseValidatorModel):
    PipelineName: str


class DescribeProcessingJobRequest(BaseValidatorModel):
    ProcessingJobName: str


class DescribeProjectInput(BaseValidatorModel):
    ProjectName: str


class ServiceCatalogProvisionedProductDetails(BaseValidatorModel):
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductStatusMessage: Optional[str] = None


class DescribeSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str


class DescribeStudioLifecycleConfigRequest(BaseValidatorModel):
    StudioLifecycleConfigName: str


class DescribeSubscribedWorkteamRequest(BaseValidatorModel):
    WorkteamArn: str


class SubscribedWorkteam(BaseValidatorModel):
    WorkteamArn: str
    MarketplaceTitle: Optional[str] = None
    SellerName: Optional[str] = None
    MarketplaceDescription: Optional[str] = None
    ListingId: Optional[str] = None


class DescribeTrainingJobRequest(BaseValidatorModel):
    TrainingJobName: str


class MetricData(BaseValidatorModel):
    MetricName: Optional[str] = None
    Value: Optional[float] = None
    Timestamp: Optional[datetime] = None


class ProfilerConfigOutput(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None


class ProfilerRuleConfigurationOutput(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None


class ProfilerRuleEvaluationStatus(BaseValidatorModel):
    RuleConfigurationName: Optional[str] = None
    RuleEvaluationJobArn: Optional[str] = None
    RuleEvaluationStatus: Optional[RuleEvaluationStatusType] = None
    StatusDetails: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None


class SecondaryStatusTransition(BaseValidatorModel):
    Status: SecondaryStatusType
    StartTime: datetime
    EndTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None


class WarmPoolStatus(BaseValidatorModel):
    Status: WarmPoolResourceStatusType
    ResourceRetainedBillableTimeInSeconds: Optional[int] = None
    ReusedByJob: Optional[str] = None


class DescribeTrainingPlanRequest(BaseValidatorModel):
    TrainingPlanName: str


class ReservedCapacitySummary(BaseValidatorModel):
    ReservedCapacityArn: str
    InstanceType: ReservedCapacityInstanceTypeType
    TotalInstanceCount: int
    Status: ReservedCapacityStatusType
    AvailabilityZone: Optional[str] = None
    DurationHours: Optional[int] = None
    DurationMinutes: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class DescribeTransformJobRequest(BaseValidatorModel):
    TransformJobName: str


class DescribeTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str


class TrialComponentMetricSummary(BaseValidatorModel):
    MetricName: Optional[str] = None
    SourceArn: Optional[str] = None
    TimeStamp: Optional[datetime] = None
    Max: Optional[float] = None
    Min: Optional[float] = None
    Last: Optional[float] = None
    Count: Optional[int] = None
    Avg: Optional[float] = None
    StdDev: Optional[float] = None


class TrialComponentSource(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None


class DescribeTrialRequest(BaseValidatorModel):
    TrialName: str


class TrialSource(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None


class DescribeUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str


class DescribeWorkforceRequest(BaseValidatorModel):
    WorkforceName: str


class DescribeWorkteamRequest(BaseValidatorModel):
    WorkteamName: str


class ProductionVariantServerlessUpdateConfig(BaseValidatorModel):
    MaxConcurrency: Optional[int] = None
    ProvisionedConcurrency: Optional[int] = None


class DeviceDeploymentSummary(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    EdgeDeploymentPlanName: str
    StageName: str
    DeviceName: str
    DeviceArn: str
    DeployedStageName: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    DeviceDeploymentStatus: Optional[DeviceDeploymentStatusType] = None
    DeviceDeploymentStatusMessage: Optional[str] = None
    Description: Optional[str] = None
    DeploymentStartTime: Optional[datetime] = None


class DeviceFleetSummary(BaseValidatorModel):
    DeviceFleetArn: str
    DeviceFleetName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class DeviceSelectionConfig(BaseValidatorModel):
    DeviceSubsetType: DeviceSubsetTypeType
    Percentage: Optional[int] = None
    DeviceNames: Optional[List[str]] = None
    DeviceNameContains: Optional[str] = None


class DeviceStats(BaseValidatorModel):
    ConnectedDeviceCount: int
    RegisteredDeviceCount: int


class EdgeModelSummary(BaseValidatorModel):
    ModelName: str
    ModelVersion: str


class Device(BaseValidatorModel):
    DeviceName: str
    Description: Optional[str] = None
    IotThingName: Optional[str] = None


class DisassociateTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str
    TrialName: str


class DockerSettingsOutput(BaseValidatorModel):
    EnableDockerAccess: Optional[FeatureStatusType] = None
    VpcOnlyTrustedAccounts: Optional[List[str]] = None


class DockerSettings(BaseValidatorModel):
    EnableDockerAccess: Optional[FeatureStatusType] = None
    VpcOnlyTrustedAccounts: Optional[List[str]] = None


class DomainDetails(BaseValidatorModel):
    DomainArn: Optional[str] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Status: Optional[DomainStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Url: Optional[str] = None


class FileSource(BaseValidatorModel):
    S3Uri: str
    ContentType: Optional[str] = None
    ContentDigest: Optional[str] = None


class EMRStepMetadata(BaseValidatorModel):
    ClusterId: Optional[str] = None
    StepId: Optional[str] = None
    StepName: Optional[str] = None
    LogFilePath: Optional[str] = None


class EbsStorageSettings(BaseValidatorModel):
    EbsVolumeSizeInGb: int


class EdgeDeploymentPlanSummary(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    EdgeDeploymentPlanName: str
    DeviceFleetName: str
    EdgeDeploymentSuccess: int
    EdgeDeploymentPending: int
    EdgeDeploymentFailed: int
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class EdgeModelStat(BaseValidatorModel):
    ModelName: str
    ModelVersion: str
    OfflineDeviceCount: int
    ConnectedDeviceCount: int
    ActiveDeviceCount: int
    SamplingDeviceCount: int


class EdgePackagingJobSummary(BaseValidatorModel):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    EdgePackagingJobStatus: EdgePackagingJobStatusType
    CompilationJobName: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class Edge(BaseValidatorModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None


class EmrSettingsOutput(BaseValidatorModel):
    AssumableRoleArns: Optional[List[str]] = None
    ExecutionRoleArns: Optional[List[str]] = None


class EmrSettings(BaseValidatorModel):
    AssumableRoleArns: Optional[List[str]] = None
    ExecutionRoleArns: Optional[List[str]] = None


class EndpointConfigStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class EndpointConfigSummary(BaseValidatorModel):
    EndpointConfigName: str
    EndpointConfigArn: str
    CreationTime: datetime


class EndpointInfo(BaseValidatorModel):
    EndpointName: Optional[str] = None


class ProductionVariantServerlessConfig(BaseValidatorModel):
    MemorySizeInMB: int
    MaxConcurrency: int
    ProvisionedConcurrency: Optional[int] = None


class InferenceMetrics(BaseValidatorModel):
    MaxInvocations: int
    ModelLatency: int


class EndpointStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class EndpointSummary(BaseValidatorModel):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatusType


class EnvironmentParameter(BaseValidatorModel):
    Key: str
    ValueType: str
    Value: str


class FailStepMetadata(BaseValidatorModel):
    ErrorMessage: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Operator: Optional[OperatorType] = None
    Value: Optional[str] = None


class FinalHyperParameterTuningJobObjectiveMetric(BaseValidatorModel):
    MetricName: str
    Value: float
    Type: Optional[HyperParameterTuningJobObjectiveTypeType] = None


class FlowDefinitionSummary(BaseValidatorModel):
    FlowDefinitionName: str
    FlowDefinitionArn: str
    FlowDefinitionStatus: FlowDefinitionStatusType
    CreationTime: datetime
    FailureReason: Optional[str] = None


class GetDeviceFleetReportRequest(BaseValidatorModel):
    DeviceFleetName: str


class GetLineageGroupPolicyRequest(BaseValidatorModel):
    LineageGroupName: str


class GetModelPackageGroupPolicyInput(BaseValidatorModel):
    ModelPackageGroupName: str


class ScalingPolicyObjective(BaseValidatorModel):
    MinInvocationsPerMinute: Optional[int] = None
    MaxInvocationsPerMinute: Optional[int] = None


class ScalingPolicyMetric(BaseValidatorModel):
    InvocationsPerInstance: Optional[int] = None
    ModelLatency: Optional[int] = None


class PropertyNameSuggestion(BaseValidatorModel):
    PropertyName: Optional[str] = None


class GitConfigForUpdate(BaseValidatorModel):
    SecretArn: Optional[str] = None


class HiddenSageMakerImageOutput(BaseValidatorModel):
    SageMakerImageName: Optional[Literal['sagemaker_distribution']] = None
    VersionAliases: Optional[List[str]] = None


class HiddenSageMakerImage(BaseValidatorModel):
    SageMakerImageName: Optional[Literal['sagemaker_distribution']] = None
    VersionAliases: Optional[List[str]] = None


class HolidayConfigAttributes(BaseValidatorModel):
    CountryCode: Optional[str] = None


class HubAccessConfig(BaseValidatorModel):
    HubContentArn: str


class HubContentInfo(BaseValidatorModel):
    HubContentName: str
    HubContentArn: str
    HubContentVersion: str
    HubContentType: HubContentTypeType
    DocumentSchemaVersion: str
    HubContentStatus: HubContentStatusType
    CreationTime: datetime
    SageMakerPublicHubContentArn: Optional[str] = None
    HubContentDisplayName: Optional[str] = None
    HubContentDescription: Optional[str] = None
    SupportStatus: Optional[HubContentSupportStatusType] = None
    HubContentSearchKeywords: Optional[List[str]] = None
    OriginalCreationTime: Optional[datetime] = None


class HubInfo(BaseValidatorModel):
    HubName: str
    HubArn: str
    HubStatus: HubStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    HubDisplayName: Optional[str] = None
    HubDescription: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None


class HumanLoopActivationConditionsConfig(BaseValidatorModel):
    HumanLoopActivationConditions: str


class UiConfig(BaseValidatorModel):
    UiTemplateS3Uri: Optional[str] = None
    HumanTaskUiArn: Optional[str] = None


class HumanTaskUiSummary(BaseValidatorModel):
    HumanTaskUiName: str
    HumanTaskUiArn: str
    CreationTime: datetime


class HyperParameterTuningJobObjective(BaseValidatorModel):
    Type: HyperParameterTuningJobObjectiveTypeType
    MetricName: str


class HyperParameterTuningInstanceConfig(BaseValidatorModel):
    InstanceType: TrainingInstanceTypeType
    InstanceCount: int
    VolumeSizeInGB: int


class ResourceLimits(BaseValidatorModel):
    MaxParallelTrainingJobs: int
    MaxNumberOfTrainingJobs: Optional[int] = None
    MaxRuntimeInSeconds: Optional[int] = None


class HyperbandStrategyConfig(BaseValidatorModel):
    MinResource: Optional[int] = None
    MaxResource: Optional[int] = None


class ParentHyperParameterTuningJob(BaseValidatorModel):
    HyperParameterTuningJobName: Optional[str] = None


class IamIdentity(BaseValidatorModel):
    Arn: Optional[str] = None
    PrincipalId: Optional[str] = None
    SourceIdentity: Optional[str] = None


class IamPolicyConstraints(BaseValidatorModel):
    SourceIp: Optional[EnabledOrDisabledType] = None
    VpcSourceIp: Optional[EnabledOrDisabledType] = None


class RepositoryAuthConfig(BaseValidatorModel):
    RepositoryCredentialsProviderArn: str


class Image(BaseValidatorModel):
    CreationTime: datetime
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatusType
    LastModifiedTime: datetime
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    FailureReason: Optional[str] = None


class ImageVersion(BaseValidatorModel):
    CreationTime: datetime
    ImageArn: str
    ImageVersionArn: str
    ImageVersionStatus: ImageVersionStatusType
    LastModifiedTime: datetime
    Version: int
    FailureReason: Optional[str] = None


class InferenceComponentCapacitySize(BaseValidatorModel):
    Type: InferenceComponentCapacitySizeTypeType
    Value: int


class InferenceComponentComputeResourceRequirements(BaseValidatorModel):
    MinMemoryRequiredInMb: int
    NumberOfCpuCoresRequired: Optional[float] = None
    NumberOfAcceleratorDevicesRequired: Optional[float] = None
    MaxMemoryRequiredInMb: Optional[int] = None


class InferenceComponentContainerSpecification(BaseValidatorModel):
    Image: Optional[str] = None
    ArtifactUrl: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None


class InferenceComponentStartupParameters(BaseValidatorModel):
    ModelDataDownloadTimeoutInSeconds: Optional[int] = None
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int] = None


class InferenceComponentSummary(BaseValidatorModel):
    CreationTime: datetime
    InferenceComponentArn: str
    InferenceComponentName: str
    EndpointArn: str
    EndpointName: str
    VariantName: str
    LastModifiedTime: datetime
    InferenceComponentStatus: Optional[InferenceComponentStatusType] = None


class InferenceHubAccessConfig(BaseValidatorModel):
    HubContentArn: str


class RecommendationMetrics(BaseValidatorModel):
    CostPerHour: Optional[float] = None
    CostPerInference: Optional[float] = None
    MaxInvocations: Optional[int] = None
    ModelLatency: Optional[int] = None
    CpuUtilization: Optional[float] = None
    MemoryUtilization: Optional[float] = None
    ModelSetupTime: Optional[int] = None


class InferenceRecommendationsJob(BaseValidatorModel):
    JobName: str
    JobDescription: str
    JobType: RecommendationJobTypeType
    JobArn: str
    Status: RecommendationJobStatusType
    CreationTime: datetime
    RoleArn: str
    LastModifiedTime: datetime
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    ModelName: Optional[str] = None
    SamplePayloadUrl: Optional[str] = None
    ModelPackageVersionArn: Optional[str] = None


class InstanceGroup(BaseValidatorModel):
    InstanceType: TrainingInstanceTypeType
    InstanceCount: int
    InstanceGroupName: str


class IntegerParameterRangeSpecification(BaseValidatorModel):
    MinValue: str
    MaxValue: str


class IntegerParameterRange(BaseValidatorModel):
    Name: str
    MinValue: str
    MaxValue: str
    ScalingType: Optional[HyperParameterScalingTypeType] = None


class KernelSpec(BaseValidatorModel):
    Name: str
    DisplayName: Optional[str] = None


class LabelCountersForWorkteam(BaseValidatorModel):
    HumanLabeled: Optional[int] = None
    PendingHuman: Optional[int] = None
    Total: Optional[int] = None


class LabelingJobDataAttributesOutput(BaseValidatorModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None


class LabelingJobDataAttributes(BaseValidatorModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None


class LabelingJobS3DataSource(BaseValidatorModel):
    ManifestS3Uri: str


class LabelingJobSnsDataSource(BaseValidatorModel):
    SnsTopicArn: str


class LineageGroupSummary(BaseValidatorModel):
    LineageGroupArn: Optional[str] = None
    LineageGroupName: Optional[str] = None
    DisplayName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAliasesRequest(BaseValidatorModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAppsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal['CreationTime']] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None


class ListCandidatesForAutoMLJobRequest(BaseValidatorModel):
    AutoMLJobName: str
    StatusEquals: Optional[CandidateStatusType] = None
    CandidateNameEquals: Optional[str] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[CandidateSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MonitoringJobDefinitionSummary(BaseValidatorModel):
    MonitoringJobDefinitionName: str
    MonitoringJobDefinitionArn: str
    CreationTime: datetime
    EndpointName: str


class ListDomainsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInferenceRecommendationsJobStepsRequest(BaseValidatorModel):
    JobName: str
    Status: Optional[RecommendationJobStatusType] = None
    StepType: Optional[Literal['BENCHMARK']] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TrackingServerSummary(BaseValidatorModel):
    TrackingServerArn: Optional[str] = None
    TrackingServerName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    IsActive: Optional[IsTrackingServerActiveType] = None
    MlflowVersion: Optional[str] = None


class ModelCardExportJobSummary(BaseValidatorModel):
    ModelCardExportJobName: str
    ModelCardExportJobArn: str
    Status: ModelCardExportJobStatusType
    ModelCardName: str
    ModelCardVersion: int
    CreatedAt: datetime
    LastModifiedAt: datetime


class ModelCardVersionSummary(BaseValidatorModel):
    ModelCardName: str
    ModelCardArn: str
    ModelCardStatus: ModelCardStatusType
    ModelCardVersion: int
    CreationTime: datetime
    LastModifiedTime: Optional[datetime] = None


class ModelCardSummary(BaseValidatorModel):
    ModelCardName: str
    ModelCardArn: str
    ModelCardStatus: ModelCardStatusType
    CreationTime: datetime
    LastModifiedTime: Optional[datetime] = None


class ModelMetadataSummary(BaseValidatorModel):
    Domain: str
    Framework: str
    Task: str
    Model: str
    FrameworkVersion: str


class ModelPackageGroupSummary(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    CreationTime: datetime
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ModelPackageGroupDescription: Optional[str] = None


class ModelPackageSummary(BaseValidatorModel):
    ModelPackageArn: str
    CreationTime: datetime
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageVersion: Optional[int] = None
    ModelPackageDescription: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None


class ModelSummary(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    CreationTime: datetime


class MonitoringAlertHistorySummary(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    CreationTime: datetime
    AlertStatus: MonitoringAlertStatusType


class ListMonitoringAlertsRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MonitoringScheduleSummary(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleStatus: ScheduleStatusType
    EndpointName: Optional[str] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None


class NotebookInstanceLifecycleConfigSummary(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    NotebookInstanceLifecycleConfigArn: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class NotebookInstanceSummary(BaseValidatorModel):
    NotebookInstanceName: str
    NotebookInstanceArn: str
    NotebookInstanceStatus: Optional[NotebookInstanceStatusType] = None
    Url: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    NotebookInstanceLifecycleConfigName: Optional[str] = None
    DefaultCodeRepository: Optional[str] = None
    AdditionalCodeRepositories: Optional[List[str]] = None


class OptimizationJobSummary(BaseValidatorModel):
    OptimizationJobName: str
    OptimizationJobArn: str
    CreationTime: datetime
    OptimizationJobStatus: OptimizationJobStatusType
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationTypes: List[str]
    OptimizationStartTime: Optional[datetime] = None
    OptimizationEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class ListPartnerAppsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PartnerAppSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[PartnerAppTypeType] = None
    Status: Optional[PartnerAppStatusType] = None
    CreationTime: Optional[datetime] = None


class ListPipelineExecutionStepsRequest(BaseValidatorModel):
    PipelineExecutionArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None


class PipelineExecutionSummary(BaseValidatorModel):
    PipelineExecutionArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    PipelineExecutionStatus: Optional[PipelineExecutionStatusType] = None
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineExecutionFailureReason: Optional[str] = None


class ListPipelineParametersForExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Parameter(BaseValidatorModel):
    Name: str
    Value: str


class PipelineSummary(BaseValidatorModel):
    PipelineArn: Optional[str] = None
    PipelineName: Optional[str] = None
    PipelineDisplayName: Optional[str] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastExecutionTime: Optional[datetime] = None


class ProcessingJobSummary(BaseValidatorModel):
    ProcessingJobName: str
    ProcessingJobArn: str
    CreationTime: datetime
    ProcessingJobStatus: ProcessingJobStatusType
    ProcessingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    ExitMessage: Optional[str] = None


class ProjectSummary(BaseValidatorModel):
    ProjectName: str
    ProjectArn: str
    ProjectId: str
    CreationTime: datetime
    ProjectStatus: ProjectStatusType
    ProjectDescription: Optional[str] = None


class ResourceCatalog(BaseValidatorModel):
    ResourceCatalogArn: str
    ResourceCatalogName: str
    Description: str
    CreationTime: datetime


class ListSpacesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None


class ListStageDevicesRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ExcludeDevicesDeployedInOtherStage: Optional[bool] = None


class StudioLifecycleConfigDetails(BaseValidatorModel):
    StudioLifecycleConfigArn: Optional[str] = None
    StudioLifecycleConfigName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    StudioLifecycleConfigAppType: Optional[StudioLifecycleConfigAppTypeType] = None


class ListSubscribedWorkteamsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTrainingJobsForHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[TrainingJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None


class TrainingPlanFilter(BaseValidatorModel):
    Name: Literal['Status']
    Value: str


class TransformJobSummary(BaseValidatorModel):
    TransformJobName: str
    TransformJobArn: str
    CreationTime: datetime
    TransformJobStatus: TransformJobStatusType
    TransformEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    FailureReason: Optional[str] = None


class ListUserProfilesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[UserProfileSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameContains: Optional[str] = None


class UserProfileDetails(BaseValidatorModel):
    DomainId: Optional[str] = None
    UserProfileName: Optional[str] = None
    Status: Optional[UserProfileStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class ListWorkforcesRequest(BaseValidatorModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListWorkteamsRequest(BaseValidatorModel):
    SortBy: Optional[ListWorkteamsSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OidcMemberDefinitionOutput(BaseValidatorModel):
    Groups: Optional[List[str]] = None


class PredefinedMetricSpecification(BaseValidatorModel):
    PredefinedMetricType: Optional[str] = None


class ModelAccessConfig(BaseValidatorModel):
    AcceptEula: bool


class ModelBiasAppSpecification(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None


class MonitoringGroundTruthS3Input(BaseValidatorModel):
    S3Uri: Optional[str] = None


class ModelCompilationConfigOutput(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None


class ModelCompilationConfig(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None


class ModelDashboardEndpoint(BaseValidatorModel):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatusType


class ModelDashboardIndicatorAction(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ModelExplainabilityAppSpecification(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None


class RealTimeInferenceConfig(BaseValidatorModel):
    InstanceType: InstanceTypeType
    InstanceCount: int


class ModelInput(BaseValidatorModel):
    DataInputConfig: str


class ModelLatencyThreshold(BaseValidatorModel):
    Percentile: Optional[str] = None
    ValueInMilliseconds: Optional[int] = None


class ModelMetadataFilter(BaseValidatorModel):
    Name: ModelMetadataFilterTypeType
    Value: str


class ModelPackageStatusItem(BaseValidatorModel):
    Name: str
    Status: DetailedModelPackageStatusType
    FailureReason: Optional[str] = None


class ModelQualityAppSpecification(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    ProblemType: Optional[MonitoringProblemTypeType] = None
    Environment: Optional[Dict[str, str]] = None


class ModelQuantizationConfigOutput(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None


class ModelQuantizationConfig(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None


class ModelShardingConfigOutput(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None


class ModelShardingConfig(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None


class ModelStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class MonitoringAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None


class MonitoringAppSpecification(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None


class MonitoringClusterConfig(BaseValidatorModel):
    InstanceCount: int
    InstanceType: ProcessingInstanceTypeType
    VolumeSizeInGB: int
    VolumeKmsKeyId: Optional[str] = None


class MonitoringCsvDatasetFormat(BaseValidatorModel):
    Header: Optional[bool] = None


class MonitoringJsonDatasetFormat(BaseValidatorModel):
    Line: Optional[bool] = None


class MonitoringS3Output(BaseValidatorModel):
    S3Uri: str
    LocalPath: str
    S3UploadMode: Optional[ProcessingS3UploadModeType] = None


class ScheduleConfig(BaseValidatorModel):
    ScheduleExpression: str
    DataAnalysisStartTime: Optional[str] = None
    DataAnalysisEndTime: Optional[str] = None


class NeoVpcConfig(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class S3StorageConfig(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None
    ResolvedOutputS3Uri: Optional[str] = None


class OidcConfigForResponse(BaseValidatorModel):
    ClientId: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    LogoutEndpoint: Optional[str] = None
    JwksUri: Optional[str] = None
    Scope: Optional[str] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None


class OidcMemberDefinition(BaseValidatorModel):
    Groups: Optional[List[str]] = None


class OnlineStoreSecurityConfig(BaseValidatorModel):
    KmsKeyId: Optional[str] = None


class TtlDuration(BaseValidatorModel):
    Unit: Optional[TtlDurationUnitType] = None
    Value: Optional[int] = None


class OptimizationModelAccessConfig(BaseValidatorModel):
    AcceptEula: bool


class OptimizationVpcConfig(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class TargetPlatform(BaseValidatorModel):
    Os: TargetPlatformOsType
    Arch: TargetPlatformArchType
    Accelerator: Optional[TargetPlatformAcceleratorType] = None


class OwnershipSettingsSummary(BaseValidatorModel):
    OwnerUserProfileName: Optional[str] = None


class Parent(BaseValidatorModel):
    TrialName: Optional[str] = None
    ExperimentName: Optional[str] = None


class PartnerAppConfig(BaseValidatorModel):
    AdminUsers: Optional[List[str]] = None
    Arguments: Optional[Dict[str, str]] = None


class ProductionVariantManagedInstanceScaling(BaseValidatorModel):
    Status: Optional[ManagedInstanceScalingStatusType] = None
    MinInstanceCount: Optional[int] = None
    MaxInstanceCount: Optional[int] = None


class ProductionVariantRoutingConfig(BaseValidatorModel):
    RoutingStrategy: RoutingStrategyType


class ProductionVariantStatus(BaseValidatorModel):
    Status: VariantStatusType
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None


class Phase(BaseValidatorModel):
    InitialNumberOfUsers: Optional[int] = None
    SpawnRate: Optional[int] = None
    DurationInSeconds: Optional[int] = None


class ProcessingJobStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class QualityCheckStepMetadata(BaseValidatorModel):
    CheckType: Optional[str] = None
    BaselineUsedForDriftCheckStatistics: Optional[str] = None
    BaselineUsedForDriftCheckConstraints: Optional[str] = None
    CalculatedBaselineStatistics: Optional[str] = None
    CalculatedBaselineConstraints: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ViolationReport: Optional[str] = None
    CheckJobArn: Optional[str] = None
    SkipCheck: Optional[bool] = None
    RegisterNewBaseline: Optional[bool] = None


class RegisterModelStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class TrainingJobStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class TransformJobStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None


class TuningJobStepMetaData(BaseValidatorModel):
    Arn: Optional[str] = None


class SelectiveExecutionResult(BaseValidatorModel):
    SourcePipelineExecutionArn: Optional[str] = None


class PriorityClass(BaseValidatorModel):
    Name: str
    Weight: int


class ProcessingClusterConfig(BaseValidatorModel):
    InstanceCount: int
    InstanceType: ProcessingInstanceTypeType
    VolumeSizeInGB: int
    VolumeKmsKeyId: Optional[str] = None


class ProcessingFeatureStoreOutput(BaseValidatorModel):
    FeatureGroupName: str


class ProcessingS3Input(BaseValidatorModel):
    S3Uri: str
    S3DataType: ProcessingS3DataTypeType
    LocalPath: Optional[str] = None
    S3InputMode: Optional[ProcessingS3InputModeType] = None
    S3DataDistributionType: Optional[ProcessingS3DataDistributionTypeType] = None
    S3CompressionType: Optional[ProcessingS3CompressionTypeType] = None


class ProcessingS3Output(BaseValidatorModel):
    S3Uri: str
    S3UploadMode: ProcessingS3UploadModeType
    LocalPath: Optional[str] = None


class ProductionVariantCoreDumpConfig(BaseValidatorModel):
    DestinationS3Uri: str
    KmsKeyId: Optional[str] = None


class ProfilerConfigForUpdate(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None


class ProfilerConfig(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None


class ProfilerRuleConfiguration(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None


class PropertyNameQuery(BaseValidatorModel):
    PropertyNameHint: str


class ProvisioningParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class USD(BaseValidatorModel):
    Dollars: Optional[int] = None
    Cents: Optional[int] = None
    TenthFractionsOfACent: Optional[int] = None


class PutModelPackageGroupPolicyInput(BaseValidatorModel):
    ModelPackageGroupName: str
    ResourcePolicy: str


class Vertex(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    LineageType: Optional[LineageTypeType] = None


class RStudioServerProAppSettings(BaseValidatorModel):
    AccessStatus: Optional[RStudioServerProAccessStatusType] = None
    UserGroup: Optional[RStudioServerProUserGroupType] = None


class RecommendationJobCompiledOutputConfig(BaseValidatorModel):
    S3OutputUri: Optional[str] = None


class RecommendationJobPayloadConfigOutput(BaseValidatorModel):
    SamplePayloadUrl: Optional[str] = None
    SupportedContentTypes: Optional[List[str]] = None


class RecommendationJobPayloadConfig(BaseValidatorModel):
    SamplePayloadUrl: Optional[str] = None
    SupportedContentTypes: Optional[List[str]] = None


class RecommendationJobResourceLimit(BaseValidatorModel):
    MaxNumberOfTests: Optional[int] = None
    MaxParallelOfTests: Optional[int] = None


class RecommendationJobVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class RecommendationJobVpcConfig(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class RemoteDebugConfigForUpdate(BaseValidatorModel):
    EnableRemoteDebug: Optional[bool] = None


class RenderableTask(BaseValidatorModel):
    Input: str


class RenderingError(BaseValidatorModel):
    Code: str
    Message: str


class ReservedCapacityOffering(BaseValidatorModel):
    InstanceType: ReservedCapacityInstanceTypeType
    InstanceCount: int
    AvailabilityZone: Optional[str] = None
    DurationHours: Optional[int] = None
    DurationMinutes: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ResourceConfigForUpdate(BaseValidatorModel):
    KeepAlivePeriodInSeconds: int


class VisibilityConditions(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class SelectedStep(BaseValidatorModel):
    StepName: str


class SendPipelineExecutionStepFailureRequest(BaseValidatorModel):
    CallbackToken: str
    FailureReason: Optional[str] = None
    ClientRequestToken: Optional[str] = None


class ShadowModelVariantConfig(BaseValidatorModel):
    ShadowModelVariantName: str
    SamplingPercentage: int


class SharingSettings(BaseValidatorModel):
    NotebookOutputOption: Optional[NotebookOutputOptionType] = None
    S3OutputPath: Optional[str] = None
    S3KmsKeyId: Optional[str] = None


class SourceIpConfigOutput(BaseValidatorModel):
    Cidrs: List[str]


class SourceIpConfig(BaseValidatorModel):
    Cidrs: List[str]


class SpaceIdleSettings(BaseValidatorModel):
    IdleTimeoutInMinutes: Optional[int] = None


class SpaceSharingSettingsSummary(BaseValidatorModel):
    SharingType: Optional[SharingTypeType] = None


class Stairs(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None
    NumberOfSteps: Optional[int] = None
    UsersPerStep: Optional[int] = None


class StartEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str


class StartInferenceExperimentRequest(BaseValidatorModel):
    Name: str


class StartMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


class StartMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


class StartNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


class StopAutoMLJobRequest(BaseValidatorModel):
    AutoMLJobName: str


class StopCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str


class StopEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str


class StopEdgePackagingJobRequest(BaseValidatorModel):
    EdgePackagingJobName: str


class StopHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str


class StopInferenceRecommendationsJobRequest(BaseValidatorModel):
    JobName: str


class StopLabelingJobRequest(BaseValidatorModel):
    LabelingJobName: str


class StopMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


class StopMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


class StopNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


class StopOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str


class StopPipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    ClientRequestToken: str


class StopProcessingJobRequest(BaseValidatorModel):
    ProcessingJobName: str


class StopTrainingJobRequest(BaseValidatorModel):
    TrainingJobName: str


class StopTransformJobRequest(BaseValidatorModel):
    TransformJobName: str


class ThroughputConfigUpdate(BaseValidatorModel):
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None


class TimeSeriesConfigOutput(BaseValidatorModel):
    TargetAttributeName: str
    TimestampAttributeName: str
    ItemIdentifierAttributeName: str
    GroupingAttributeNames: Optional[List[str]] = None


class TimeSeriesConfig(BaseValidatorModel):
    TargetAttributeName: str
    TimestampAttributeName: str
    ItemIdentifierAttributeName: str
    GroupingAttributeNames: Optional[List[str]] = None


class TimeSeriesTransformationsOutput(BaseValidatorModel):
    Filling: Optional[Dict[str, Dict[FillingTypeType, str]]] = None
    Aggregation: Optional[Dict[str, AggregationTransformationValueType]] = None


class TimeSeriesTransformations(BaseValidatorModel):
    Filling: Optional[Dict[str, Dict[FillingTypeType, str]]] = None
    Aggregation: Optional[Dict[str, AggregationTransformationValueType]] = None


class TrainingRepositoryAuthConfig(BaseValidatorModel):
    TrainingRepositoryCredentialsProviderArn: str


class TransformS3DataSource(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str


class UpdateActionRequest(BaseValidatorModel):
    ActionName: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Dict[str, str]] = None
    PropertiesToRemove: Optional[List[str]] = None


class UpdateArtifactRequest(BaseValidatorModel):
    ArtifactArn: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    PropertiesToRemove: Optional[List[str]] = None


class UpdateClusterSoftwareRequest(BaseValidatorModel):
    ClusterName: str


class UpdateContextRequest(BaseValidatorModel):
    ContextName: str
    Description: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    PropertiesToRemove: Optional[List[str]] = None


class VariantProperty(BaseValidatorModel):
    VariantPropertyType: VariantPropertyTypeType


class UpdateExperimentRequest(BaseValidatorModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None


class UpdateHubContentReferenceRequest(BaseValidatorModel):
    HubName: str
    HubContentName: str
    HubContentType: HubContentTypeType
    MinVersion: Optional[str] = None


class UpdateHubContentRequest(BaseValidatorModel):
    HubName: str
    HubContentName: str
    HubContentType: HubContentTypeType
    HubContentVersion: str
    HubContentDisplayName: Optional[str] = None
    HubContentDescription: Optional[str] = None
    HubContentMarkdown: Optional[str] = None
    HubContentSearchKeywords: Optional[List[str]] = None
    SupportStatus: Optional[HubContentSupportStatusType] = None


class UpdateHubRequest(BaseValidatorModel):
    HubName: str
    HubDescription: Optional[str] = None
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None


class UpdateImageRequest(BaseValidatorModel):
    ImageName: str
    DeleteProperties: Optional[List[str]] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    RoleArn: Optional[str] = None


class UpdateImageVersionRequest(BaseValidatorModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    AliasesToAdd: Optional[List[str]] = None
    AliasesToDelete: Optional[List[str]] = None
    VendorGuidance: Optional[VendorGuidanceType] = None
    JobType: Optional[JobTypeType] = None
    MLFramework: Optional[str] = None
    ProgrammingLang: Optional[str] = None
    Processor: Optional[ProcessorType] = None
    Horovod: Optional[bool] = None
    ReleaseNotes: Optional[str] = None


class UpdateMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str
    ArtifactStoreUri: Optional[str] = None
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None


class UpdateModelCardRequest(BaseValidatorModel):
    ModelCardName: str
    Content: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None


class UpdateMonitoringAlertRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    DatapointsToAlert: int
    EvaluationPeriod: int


class UpdateTrialRequest(BaseValidatorModel):
    TrialName: str
    DisplayName: Optional[str] = None


class WorkforceVpcConfigResponse(BaseValidatorModel):
    VpcId: str
    SecurityGroupIds: List[str]
    Subnets: List[str]
    VpcEndpointId: Optional[str] = None


class ActionSummary(BaseValidatorModel):
    ActionArn: Optional[str] = None
    ActionName: Optional[str] = None
    Source: Optional[ActionSource] = None
    ActionType: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class AddAssociationResponse(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadata


class AssociateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadata


class CreateActionResponse(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadata


class CreateAlgorithmOutput(BaseValidatorModel):
    AlgorithmArn: str
    ResponseMetadata: ResponseMetadata


class CreateAppImageConfigResponse(BaseValidatorModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadata


class CreateAppResponse(BaseValidatorModel):
    AppArn: str
    ResponseMetadata: ResponseMetadata


class CreateArtifactResponse(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadata


class CreateAutoMLJobResponse(BaseValidatorModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateAutoMLJobV2Response(BaseValidatorModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class CreateClusterSchedulerConfigResponse(BaseValidatorModel):
    ClusterSchedulerConfigArn: str
    ClusterSchedulerConfigId: str
    ResponseMetadata: ResponseMetadata


class CreateCodeRepositoryOutput(BaseValidatorModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadata


class CreateCompilationJobResponse(BaseValidatorModel):
    CompilationJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateComputeQuotaResponse(BaseValidatorModel):
    ComputeQuotaArn: str
    ComputeQuotaId: str
    ResponseMetadata: ResponseMetadata


class CreateContextResponse(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadata


class CreateDataQualityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


class CreateDomainResponse(BaseValidatorModel):
    DomainArn: str
    DomainId: str
    Url: str
    ResponseMetadata: ResponseMetadata


class CreateEdgeDeploymentPlanResponse(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    ResponseMetadata: ResponseMetadata


class CreateEndpointConfigOutput(BaseValidatorModel):
    EndpointConfigArn: str
    ResponseMetadata: ResponseMetadata


class CreateEndpointOutput(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


class CreateExperimentResponse(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadata


class CreateFeatureGroupResponse(BaseValidatorModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateFlowDefinitionResponse(BaseValidatorModel):
    FlowDefinitionArn: str
    ResponseMetadata: ResponseMetadata


class CreateHubContentReferenceResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


class CreateHubResponse(BaseValidatorModel):
    HubArn: str
    ResponseMetadata: ResponseMetadata


class CreateHumanTaskUiResponse(BaseValidatorModel):
    HumanTaskUiArn: str
    ResponseMetadata: ResponseMetadata


class CreateHyperParameterTuningJobResponse(BaseValidatorModel):
    HyperParameterTuningJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateImageResponse(BaseValidatorModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadata


class CreateImageVersionResponse(BaseValidatorModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadata


class CreateInferenceComponentOutput(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadata


class CreateInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


class CreateInferenceRecommendationsJobResponse(BaseValidatorModel):
    JobArn: str
    ResponseMetadata: ResponseMetadata


class CreateLabelingJobResponse(BaseValidatorModel):
    LabelingJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelBiasJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelCardExportJobResponse(BaseValidatorModel):
    ModelCardExportJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelCardResponse(BaseValidatorModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelExplainabilityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelOutput(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelPackageGroupOutput(BaseValidatorModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelPackageOutput(BaseValidatorModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelQualityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


class CreateMonitoringScheduleResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadata


class CreateNotebookInstanceLifecycleConfigOutput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadata


class CreateNotebookInstanceOutput(BaseValidatorModel):
    NotebookInstanceArn: str
    ResponseMetadata: ResponseMetadata


class CreateOptimizationJobResponse(BaseValidatorModel):
    OptimizationJobArn: str
    ResponseMetadata: ResponseMetadata


class CreatePartnerAppPresignedUrlResponse(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


class CreatePartnerAppResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreatePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadata


class CreatePresignedDomainUrlResponse(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


class CreatePresignedMlflowTrackingServerUrlResponse(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


class CreatePresignedNotebookInstanceUrlOutput(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


class CreateProcessingJobResponse(BaseValidatorModel):
    ProcessingJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateProjectOutput(BaseValidatorModel):
    ProjectArn: str
    ProjectId: str
    ResponseMetadata: ResponseMetadata


class CreateSpaceResponse(BaseValidatorModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadata


class CreateStudioLifecycleConfigResponse(BaseValidatorModel):
    StudioLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrainingJobResponse(BaseValidatorModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrainingPlanResponse(BaseValidatorModel):
    TrainingPlanArn: str
    ResponseMetadata: ResponseMetadata


class CreateTransformJobResponse(BaseValidatorModel):
    TransformJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrialResponse(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadata


class CreateUserProfileResponse(BaseValidatorModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadata


class CreateWorkforceResponse(BaseValidatorModel):
    WorkforceArn: str
    ResponseMetadata: ResponseMetadata


class CreateWorkteamResponse(BaseValidatorModel):
    WorkteamArn: str
    ResponseMetadata: ResponseMetadata


class DeleteActionResponse(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadata


class DeleteArtifactResponse(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadata


class DeleteAssociationResponse(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class DeleteContextResponse(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadata


class DeleteExperimentResponse(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadata


class DeleteInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


class DeleteMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


class DeletePartnerAppResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeletePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadata


class DeleteTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadata


class DeleteTrialResponse(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadata


class DeleteWorkteamResponse(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


class DescribeImageResponse(BaseValidatorModel):
    CreationTime: datetime
    Description: str
    DisplayName: str
    FailureReason: str
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatusType
    LastModifiedTime: datetime
    RoleArn: str
    ResponseMetadata: ResponseMetadata


class DescribeImageVersionResponse(BaseValidatorModel):
    BaseImage: str
    ContainerImage: str
    CreationTime: datetime
    FailureReason: str
    ImageArn: str
    ImageVersionArn: str
    ImageVersionStatus: ImageVersionStatusType
    LastModifiedTime: datetime
    Version: int
    VendorGuidance: VendorGuidanceType
    JobType: JobTypeType
    MLFramework: str
    ProgrammingLang: str
    Processor: ProcessorType
    Horovod: bool
    ReleaseNotes: str
    ResponseMetadata: ResponseMetadata


class DescribePipelineDefinitionForExecutionResponse(BaseValidatorModel):
    PipelineDefinition: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeStudioLifecycleConfigResponse(BaseValidatorModel):
    StudioLifecycleConfigArn: str
    StudioLifecycleConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    ResponseMetadata: ResponseMetadata


class DisassociateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetLineageGroupPolicyResponse(BaseValidatorModel):
    LineageGroupArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadata


class GetModelPackageGroupPolicyOutput(BaseValidatorModel):
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadata


class GetSagemakerServicecatalogPortfolioStatusOutput(BaseValidatorModel):
    Status: SagemakerServicecatalogStatusType
    ResponseMetadata: ResponseMetadata


class ImportHubContentResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


class ListAliasesResponse(BaseValidatorModel):
    SageMakerImageVersionAliases: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutModelPackageGroupPolicyOutput(BaseValidatorModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadata


class RetryPipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


class SendPipelineExecutionStepFailureResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


class SendPipelineExecutionStepSuccessResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


class StartInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


class StartMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


class StartPipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


class StopInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


class StopMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


class StopPipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


class UpdateActionResponse(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadata


class UpdateAppImageConfigResponse(BaseValidatorModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadata


class UpdateArtifactResponse(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadata


class UpdateClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class UpdateClusterSchedulerConfigResponse(BaseValidatorModel):
    ClusterSchedulerConfigArn: str
    ClusterSchedulerConfigVersion: int
    ResponseMetadata: ResponseMetadata


class UpdateClusterSoftwareResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


class UpdateCodeRepositoryOutput(BaseValidatorModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadata


class UpdateComputeQuotaResponse(BaseValidatorModel):
    ComputeQuotaArn: str
    ComputeQuotaVersion: int
    ResponseMetadata: ResponseMetadata


class UpdateContextResponse(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadata


class UpdateDomainResponse(BaseValidatorModel):
    DomainArn: str
    ResponseMetadata: ResponseMetadata


class UpdateEndpointOutput(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


class UpdateEndpointWeightsAndCapacitiesOutput(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


class UpdateExperimentResponse(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateFeatureGroupResponse(BaseValidatorModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadata


class UpdateHubContentReferenceResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateHubContentResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateHubResponse(BaseValidatorModel):
    HubArn: str
    ResponseMetadata: ResponseMetadata


class UpdateImageResponse(BaseValidatorModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadata


class UpdateImageVersionResponse(BaseValidatorModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadata


class UpdateInferenceComponentOutput(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateInferenceComponentRuntimeConfigOutput(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


class UpdateModelCardResponse(BaseValidatorModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadata


class UpdateModelPackageOutput(BaseValidatorModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadata


class UpdateMonitoringAlertResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    MonitoringAlertName: str
    ResponseMetadata: ResponseMetadata


class UpdateMonitoringScheduleResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadata


class UpdatePartnerAppResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class UpdatePipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


class UpdatePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadata


class UpdateProjectOutput(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadata


class UpdateSpaceResponse(BaseValidatorModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadata


class UpdateTrainingJobResponse(BaseValidatorModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadata


class UpdateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateTrialResponse(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadata


class UpdateUserProfileResponse(BaseValidatorModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class AddTagsOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateExperimentRequest(BaseValidatorModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateHubContentReferenceRequest(BaseValidatorModel):
    HubName: str
    SageMakerPublicHubContentArn: str
    HubContentName: Optional[str] = None
    MinVersion: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateImageRequest(BaseValidatorModel):
    ImageName: str
    RoleArn: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str
    ArtifactStoreUri: str
    RoleArn: str
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    MlflowVersion: Optional[str] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateModelPackageGroupInput(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateStudioLifecycleConfigRequest(BaseValidatorModel):
    StudioLifecycleConfigName: str
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    Tags: Optional[List[Tag]] = None


class CreateTrainingPlanRequest(BaseValidatorModel):
    TrainingPlanName: str
    TrainingPlanOfferingId: str
    Tags: Optional[List[Tag]] = None


class ImportHubContentRequest(BaseValidatorModel):
    HubContentName: str
    HubContentType: HubContentTypeType
    DocumentSchemaVersion: str
    HubName: str
    HubContentDocument: str
    HubContentVersion: Optional[str] = None
    HubContentDisplayName: Optional[str] = None
    HubContentDescription: Optional[str] = None
    HubContentMarkdown: Optional[str] = None
    SupportStatus: Optional[HubContentSupportStatusType] = None
    HubContentSearchKeywords: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class ListTagsOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AutoRollbackConfigOutput(BaseValidatorModel):
    Alarms: Optional[List[Alarm]] = None


class AutoRollbackConfig(BaseValidatorModel):
    Alarms: Optional[List[Alarm]] = None


class HyperParameterAlgorithmSpecificationOutput(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinition]] = None


class HyperParameterAlgorithmSpecification(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinition]] = None


class AlgorithmStatusDetails(BaseValidatorModel):
    ValidationStatuses: Optional[List[AlgorithmStatusItem]] = None
    ImageScanStatuses: Optional[List[AlgorithmStatusItem]] = None


class ListAlgorithmsOutput(BaseValidatorModel):
    AlgorithmSummaryList: List[AlgorithmSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AppDetails(BaseValidatorModel):
    DomainId: Optional[str] = None
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    AppType: Optional[AppTypeType] = None
    AppName: Optional[str] = None
    Status: Optional[AppStatusType] = None
    CreationTime: Optional[datetime] = None
    ResourceSpec: Optional[ResourceSpec] = None


class CreateAppRequest(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ResourceSpec: Optional[ResourceSpec] = None


class DescribeAppResponse(BaseValidatorModel):
    AppArn: str
    AppType: AppTypeType
    AppName: str
    DomainId: str
    UserProfileName: str
    SpaceName: str
    Status: AppStatusType
    LastHealthCheckTimestamp: datetime
    LastUserActivityTimestamp: datetime
    CreationTime: datetime
    FailureReason: str
    ResourceSpec: ResourceSpec
    BuiltInLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadata


class RStudioServerProDomainSettingsForUpdate(BaseValidatorModel):
    DomainExecutionRoleArn: str
    DefaultResourceSpec: Optional[ResourceSpec] = None
    RStudioConnectUrl: Optional[str] = None
    RStudioPackageManagerUrl: Optional[str] = None


class RStudioServerProDomainSettings(BaseValidatorModel):
    DomainExecutionRoleArn: str
    RStudioConnectUrl: Optional[str] = None
    RStudioPackageManagerUrl: Optional[str] = None
    DefaultResourceSpec: Optional[ResourceSpec] = None


class TensorBoardAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None


class AppLifecycleManagement(BaseValidatorModel):
    IdleSettings: Optional[IdleSettings] = None

AppSpecificationUnion = Union[AppSpecification, AppSpecificationOutput]


class ArtifactSourceOutput(BaseValidatorModel):
    SourceUri: str
    SourceTypes: Optional[List[ArtifactSourceType]] = None


class ArtifactSource(BaseValidatorModel):
    SourceUri: str
    SourceTypes: Optional[List[ArtifactSourceType]] = None


class AsyncInferenceOutputConfigOutput(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    S3OutputPath: Optional[str] = None
    NotificationConfig: Optional[AsyncInferenceNotificationConfigOutput] = None
    S3FailurePath: Optional[str] = None


class AsyncInferenceOutputConfig(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    S3OutputPath: Optional[str] = None
    NotificationConfig: Optional[AsyncInferenceNotificationConfig] = None
    S3FailurePath: Optional[str] = None


class AutoMLCandidateGenerationConfigOutput(BaseValidatorModel):
    FeatureSpecificationS3Uri: Optional[str] = None
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfigOutput]] = None


class CandidateGenerationConfigOutput(BaseValidatorModel):
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfigOutput]] = None


class AutoMLCandidateGenerationConfig(BaseValidatorModel):
    FeatureSpecificationS3Uri: Optional[str] = None
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfig]] = None


class CandidateGenerationConfig(BaseValidatorModel):
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfig]] = None


class AutoMLComputeConfig(BaseValidatorModel):
    EmrServerlessComputeConfig: Optional[EmrServerlessComputeConfig] = None


class AutoMLDataSource(BaseValidatorModel):
    S3DataSource: AutoMLS3DataSource


class ImageClassificationJobConfig(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None


class TextClassificationJobConfig(BaseValidatorModel):
    ContentColumn: str
    TargetLabelColumn: str
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None


class ResolvedAttributes(BaseValidatorModel):
    AutoMLJobObjective: Optional[AutoMLJobObjective] = None
    ProblemType: Optional[ProblemTypeType] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None


class AutoMLJobSummary(BaseValidatorModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    EndTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PartialFailureReasons: Optional[List[AutoMLPartialFailureReason]] = None


class AutoMLProblemTypeResolvedAttributes(BaseValidatorModel):
    TabularResolvedAttributes: Optional[TabularResolvedAttributes] = None
    TextGenerationResolvedAttributes: Optional[TextGenerationResolvedAttributes] = None


class AutoMLSecurityConfigOutput(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class LabelingJobResourceConfigOutput(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class MonitoringNetworkConfigOutput(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class NetworkConfigOutput(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class AutoMLSecurityConfig(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    VpcConfig: Optional[VpcConfig] = None


class LabelingJobResourceConfig(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfig] = None


class MonitoringNetworkConfig(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfig] = None


class NetworkConfig(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfig] = None

VpcConfigUnion = Union[VpcConfig, VpcConfigOutput]


class BatchDeleteClusterNodesResponse(BaseValidatorModel):
    Failed: List[BatchDeleteClusterNodesError]
    Successful: List[str]
    ResponseMetadata: ResponseMetadata


class Bias(BaseValidatorModel):
    Report: Optional[MetricsSource] = None
    PreTrainingReport: Optional[MetricsSource] = None
    PostTrainingReport: Optional[MetricsSource] = None


class DriftCheckModelDataQuality(BaseValidatorModel):
    Statistics: Optional[MetricsSource] = None
    Constraints: Optional[MetricsSource] = None


class DriftCheckModelQuality(BaseValidatorModel):
    Statistics: Optional[MetricsSource] = None
    Constraints: Optional[MetricsSource] = None


class Explainability(BaseValidatorModel):
    Report: Optional[MetricsSource] = None


class ModelDataQuality(BaseValidatorModel):
    Statistics: Optional[MetricsSource] = None
    Constraints: Optional[MetricsSource] = None


class ModelQuality(BaseValidatorModel):
    Statistics: Optional[MetricsSource] = None
    Constraints: Optional[MetricsSource] = None


class CallbackStepMetadata(BaseValidatorModel):
    CallbackToken: Optional[str] = None
    SqsQueueUrl: Optional[str] = None
    OutputParameters: Optional[List[OutputParameter]] = None


class LambdaStepMetadata(BaseValidatorModel):
    Arn: Optional[str] = None
    OutputParameters: Optional[List[OutputParameter]] = None


class SendPipelineExecutionStepSuccessRequest(BaseValidatorModel):
    CallbackToken: str
    OutputParameters: Optional[List[OutputParameter]] = None
    ClientRequestToken: Optional[str] = None


class CandidateProperties(BaseValidatorModel):
    CandidateArtifactLocations: Optional[CandidateArtifactLocations] = None
    CandidateMetrics: Optional[List[MetricDatum]] = None


class CanvasAppSettingsOutput(BaseValidatorModel):
    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettings] = None
    ModelRegisterSettings: Optional[ModelRegisterSettings] = None
    WorkspaceSettings: Optional[WorkspaceSettings] = None
    IdentityProviderOAuthSettings: Optional[List[IdentityProviderOAuthSetting]] = None
    DirectDeploySettings: Optional[DirectDeploySettings] = None
    KendraSettings: Optional[KendraSettings] = None
    GenerativeAiSettings: Optional[GenerativeAiSettings] = None
    EmrServerlessSettings: Optional[EmrServerlessSettings] = None


class CanvasAppSettings(BaseValidatorModel):
    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettings] = None
    ModelRegisterSettings: Optional[ModelRegisterSettings] = None
    WorkspaceSettings: Optional[WorkspaceSettings] = None
    IdentityProviderOAuthSettings: Optional[List[IdentityProviderOAuthSetting]] = None
    DirectDeploySettings: Optional[DirectDeploySettings] = None
    KendraSettings: Optional[KendraSettings] = None
    GenerativeAiSettings: Optional[GenerativeAiSettings] = None
    EmrServerlessSettings: Optional[EmrServerlessSettings] = None


class RollingUpdatePolicy(BaseValidatorModel):
    MaximumBatchSize: CapacitySize
    WaitIntervalInSeconds: int
    MaximumExecutionTimeoutInSeconds: Optional[int] = None
    RollbackMaximumBatchSize: Optional[CapacitySize] = None


class TrafficRoutingConfig(BaseValidatorModel):
    Type: TrafficRoutingConfigTypeType
    WaitIntervalInSeconds: int
    CanarySize: Optional[CapacitySize] = None
    LinearStepSize: Optional[CapacitySize] = None


class InferenceExperimentDataStorageConfigOutput(BaseValidatorModel):
    Destination: str
    KmsKey: Optional[str] = None
    ContentType: Optional[CaptureContentTypeHeaderOutput] = None


class InferenceExperimentDataStorageConfig(BaseValidatorModel):
    Destination: str
    KmsKey: Optional[str] = None
    ContentType: Optional[CaptureContentTypeHeader] = None


class DataCaptureConfigOutput(BaseValidatorModel):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: List[CaptureOption]
    EnableCapture: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeaderOutput] = None


class DataCaptureConfig(BaseValidatorModel):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: List[CaptureOption]
    EnableCapture: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeader] = None


class EnvironmentParameterRangesOutput(BaseValidatorModel):
    CategoricalParameterRanges: Optional[List[CategoricalParameterOutput]] = None

CategoricalParameterRangeUnion = Union[CategoricalParameterRange, CategoricalParameterRangeOutput]


class EnvironmentParameterRanges(BaseValidatorModel):
    CategoricalParameterRanges: Optional[List[CategoricalParameter]] = None


class ClarifyShapConfig(BaseValidatorModel):
    ShapBaselineConfig: ClarifyShapBaselineConfig
    NumberOfSamples: Optional[int] = None
    UseLogit: Optional[bool] = None
    Seed: Optional[int] = None
    TextConfig: Optional[ClarifyTextConfig] = None


class ClusterInstanceStorageConfig(BaseValidatorModel):
    EbsVolumeConfig: Optional[ClusterEbsVolumeConfig] = None


class ClusterNodeSummary(BaseValidatorModel):
    InstanceGroupName: str
    InstanceId: str
    InstanceType: ClusterInstanceTypeType
    LaunchTime: datetime
    InstanceStatus: ClusterInstanceStatusDetails


class ClusterOrchestrator(BaseValidatorModel):
    Eks: ClusterOrchestratorEksConfig


class ListClusterSchedulerConfigsResponse(BaseValidatorModel):
    ClusterSchedulerConfigSummaries: List[ClusterSchedulerConfigSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListClustersResponse(BaseValidatorModel):
    NextToken: str
    ClusterSummaries: List[ClusterSummary]
    ResponseMetadata: ResponseMetadata


class CodeEditorAppImageConfigOutput(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfig] = None
    ContainerConfig: Optional[ContainerConfigOutput] = None


class JupyterLabAppImageConfigOutput(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfig] = None
    ContainerConfig: Optional[ContainerConfigOutput] = None


class CodeEditorAppImageConfig(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfig] = None
    ContainerConfig: Optional[ContainerConfig] = None


class JupyterLabAppImageConfig(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfig] = None
    ContainerConfig: Optional[ContainerConfig] = None


class KernelGatewayAppSettingsOutput(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None
    LifecycleConfigArns: Optional[List[str]] = None


class KernelGatewayAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None
    LifecycleConfigArns: Optional[List[str]] = None


class RSessionAppSettingsOutput(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None


class RSessionAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None


class CodeRepositorySummary(BaseValidatorModel):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: Optional[GitConfig] = None


class CreateCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str
    GitConfig: GitConfig
    Tags: Optional[List[Tag]] = None


class DescribeCodeRepositoryOutput(BaseValidatorModel):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: GitConfig
    ResponseMetadata: ResponseMetadata


class JupyterServerAppSettingsOutput(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepository]] = None


class JupyterServerAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepository]] = None


class CollectionConfig(BaseValidatorModel):
    VectorConfig: Optional[VectorConfig] = None


class DebugHookConfigOutput(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Dict[str, str]] = None
    CollectionConfigurations: Optional[List[CollectionConfigurationOutput]] = None


class DebugHookConfig(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Dict[str, str]] = None
    CollectionConfigurations: Optional[List[CollectionConfiguration]] = None


class ListCompilationJobsResponse(BaseValidatorModel):
    CompilationJobSummaries: List[CompilationJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ComputeQuotaConfigOutput(BaseValidatorModel):
    ComputeQuotaResources: Optional[List[ComputeQuotaResourceConfig]] = None
    ResourceSharingConfig: Optional[ResourceSharingConfig] = None
    PreemptTeamTasks: Optional[PreemptTeamTasksType] = None


class ComputeQuotaConfig(BaseValidatorModel):
    ComputeQuotaResources: Optional[List[ComputeQuotaResourceConfig]] = None
    ResourceSharingConfig: Optional[ResourceSharingConfig] = None
    PreemptTeamTasks: Optional[PreemptTeamTasksType] = None


class ContextSummary(BaseValidatorModel):
    ContextArn: Optional[str] = None
    ContextName: Optional[str] = None
    Source: Optional[ContextSource] = None
    ContextType: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class CreateContextRequest(BaseValidatorModel):
    ContextName: str
    Source: ContextSource
    ContextType: str
    Description: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None


class TuningJobCompletionCriteria(BaseValidatorModel):
    TargetObjectiveMetricValue: Optional[float] = None
    BestObjectiveNotImproving: Optional[BestObjectiveNotImproving] = None
    ConvergenceDetected: Optional[ConvergenceDetected] = None


class CreateActionRequest(BaseValidatorModel):
    ActionName: str
    Source: ActionSource
    ActionType: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Dict[str, str]] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


class CreateTrialRequest(BaseValidatorModel):
    TrialName: str
    ExperimentName: str
    DisplayName: Optional[str] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


class CreateDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfig
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EnableIotRoleAlias: Optional[bool] = None


class CreateEdgePackagingJobRequest(BaseValidatorModel):
    EdgePackagingJobName: str
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: EdgeOutputConfig
    ResourceKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DescribeDeviceFleetResponse(BaseValidatorModel):
    DeviceFleetName: str
    DeviceFleetArn: str
    OutputConfig: EdgeOutputConfig
    Description: str
    CreationTime: datetime
    LastModifiedTime: datetime
    RoleArn: str
    IotRoleAlias: str
    ResponseMetadata: ResponseMetadata


class UpdateDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfig
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    EnableIotRoleAlias: Optional[bool] = None


class CreateHubRequest(BaseValidatorModel):
    HubName: str
    HubDescription: str
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None
    S3StorageConfig: Optional[HubS3StorageConfig] = None
    Tags: Optional[List[Tag]] = None


class DescribeHubResponse(BaseValidatorModel):
    HubName: str
    HubArn: str
    HubDisplayName: str
    HubDescription: str
    HubSearchKeywords: List[str]
    S3StorageConfig: HubS3StorageConfig
    HubStatus: HubStatusType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateHumanTaskUiRequest(BaseValidatorModel):
    HumanTaskUiName: str
    UiTemplate: UiTemplate
    Tags: Optional[List[Tag]] = None


class UpdateInferenceComponentRuntimeConfigInput(BaseValidatorModel):
    InferenceComponentName: str
    DesiredRuntimeConfig: InferenceComponentRuntimeConfig


class CreateModelCardExportJobRequest(BaseValidatorModel):
    ModelCardName: str
    ModelCardExportJobName: str
    OutputConfig: ModelCardExportOutputConfig
    ModelCardVersion: Optional[int] = None


class CreateModelCardRequest(BaseValidatorModel):
    ModelCardName: str
    Content: str
    ModelCardStatus: ModelCardStatusType
    SecurityConfig: Optional[ModelCardSecurityConfig] = None
    Tags: Optional[List[Tag]] = None


class CreateNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str
    InstanceType: InstanceTypeType
    RoleArn: str
    SubnetId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    LifecycleConfigName: Optional[str] = None
    DirectInternetAccess: Optional[DirectInternetAccessType] = None
    VolumeSizeInGB: Optional[int] = None
    AcceleratorTypes: Optional[List[NotebookInstanceAcceleratorTypeType]] = None
    DefaultCodeRepository: Optional[str] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    RootAccess: Optional[RootAccessType] = None
    PlatformIdentifier: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[InstanceMetadataServiceConfiguration] = None


class DescribeNotebookInstanceOutput(BaseValidatorModel):
    NotebookInstanceArn: str
    NotebookInstanceName: str
    NotebookInstanceStatus: NotebookInstanceStatusType
    FailureReason: str
    Url: str
    InstanceType: InstanceTypeType
    SubnetId: str
    SecurityGroups: List[str]
    RoleArn: str
    KmsKeyId: str
    NetworkInterfaceId: str
    LastModifiedTime: datetime
    CreationTime: datetime
    NotebookInstanceLifecycleConfigName: str
    DirectInternetAccess: DirectInternetAccessType
    VolumeSizeInGB: int
    AcceleratorTypes: List[NotebookInstanceAcceleratorTypeType]
    DefaultCodeRepository: str
    AdditionalCodeRepositories: List[str]
    RootAccess: RootAccessType
    PlatformIdentifier: str
    InstanceMetadataServiceConfiguration: InstanceMetadataServiceConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str
    InstanceType: Optional[InstanceTypeType] = None
    RoleArn: Optional[str] = None
    LifecycleConfigName: Optional[str] = None
    DisassociateLifecycleConfig: Optional[bool] = None
    VolumeSizeInGB: Optional[int] = None
    DefaultCodeRepository: Optional[str] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    AcceleratorTypes: Optional[List[NotebookInstanceAcceleratorTypeType]] = None
    DisassociateAcceleratorTypes: Optional[bool] = None
    DisassociateDefaultCodeRepository: Optional[bool] = None
    DisassociateAdditionalCodeRepositories: Optional[bool] = None
    RootAccess: Optional[RootAccessType] = None
    InstanceMetadataServiceConfiguration: Optional[InstanceMetadataServiceConfiguration] = None


class CreateNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[List[NotebookInstanceLifecycleHook]] = None
    OnStart: Optional[List[NotebookInstanceLifecycleHook]] = None


class DescribeNotebookInstanceLifecycleConfigOutput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigArn: str
    NotebookInstanceLifecycleConfigName: str
    OnCreate: List[NotebookInstanceLifecycleHook]
    OnStart: List[NotebookInstanceLifecycleHook]
    LastModifiedTime: datetime
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[List[NotebookInstanceLifecycleHook]] = None
    OnStart: Optional[List[NotebookInstanceLifecycleHook]] = None


class RetryPipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    ClientRequestToken: str
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


class UpdatePipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


class CreatePipelineRequest(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str
    RoleArn: str
    PipelineDisplayName: Optional[str] = None
    PipelineDefinition: Optional[str] = None
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3Location] = None
    PipelineDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


class UpdatePipelineRequest(BaseValidatorModel):
    PipelineName: str
    PipelineDisplayName: Optional[str] = None
    PipelineDefinition: Optional[str] = None
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3Location] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


class InferenceExperimentSchedule(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class ListActionsRequest(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAlgorithmsInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListAppImageConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    ModifiedTimeBefore: Optional[Timestamp] = None
    ModifiedTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[AppImageConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None


class ListArtifactsRequest(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[Literal['CreationTime']] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAssociationsRequest(BaseValidatorModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortAssociationsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAutoMLJobsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[AutoMLJobStatusType] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[AutoMLSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClusterNodesRequest(BaseValidatorModel):
    ClusterName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    InstanceGroupNameContains: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListClusterSchedulerConfigsRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    ClusterArn: Optional[str] = None
    Status: Optional[SchedulerResourceStatusType] = None
    SortBy: Optional[SortClusterSchedulerConfigByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListClustersRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    TrainingPlanArn: Optional[str] = None


class ListCodeRepositoriesInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[CodeRepositorySortByType] = None
    SortOrder: Optional[CodeRepositorySortOrderType] = None


class ListCompilationJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[CompilationJobStatusType] = None
    SortBy: Optional[ListCompilationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListComputeQuotasRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    Status: Optional[SchedulerResourceStatusType] = None
    ClusterArn: Optional[str] = None
    SortBy: Optional[SortQuotaByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContextsRequest(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataQualityJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class ListDeviceFleetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ListDeviceFleetsSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListDevicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LatestHeartbeatAfter: Optional[Timestamp] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None


class ListEdgeDeploymentPlansRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    DeviceFleetNameContains: Optional[str] = None
    SortBy: Optional[ListEdgeDeploymentPlansSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListEdgePackagingJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    ModelNameContains: Optional[str] = None
    StatusEquals: Optional[EdgePackagingJobStatusType] = None
    SortBy: Optional[ListEdgePackagingJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListEndpointConfigsInput(BaseValidatorModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class ListEndpointsInput(BaseValidatorModel):
    SortBy: Optional[EndpointSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[EndpointStatusType] = None


class ListExperimentsRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFeatureGroupsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    FeatureGroupStatusEquals: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValueType] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[FeatureGroupSortOrderType] = None
    SortBy: Optional[FeatureGroupSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFlowDefinitionsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHubContentVersionsRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    MinVersion: Optional[str] = None
    MaxSchemaVersion: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[HubContentSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHubContentsRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    NameContains: Optional[str] = None
    MaxSchemaVersion: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[HubContentSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHubsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[HubSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHumanTaskUisRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHyperParameterTuningJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[HyperParameterTuningJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    StatusEquals: Optional[HyperParameterTuningJobStatusType] = None


class ListImageVersionsRequest(BaseValidatorModel):
    ImageName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ImageVersionSortByType] = None
    SortOrder: Optional[ImageVersionSortOrderType] = None


class ListImagesRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ImageSortByType] = None
    SortOrder: Optional[ImageSortOrderType] = None


class ListInferenceComponentsInput(BaseValidatorModel):
    SortBy: Optional[InferenceComponentSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[InferenceComponentStatusType] = None
    EndpointNameEquals: Optional[str] = None
    VariantNameEquals: Optional[str] = None


class ListInferenceExperimentsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    Type: Optional[Literal['ShadowMode']] = None
    StatusEquals: Optional[InferenceExperimentStatusType] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    SortBy: Optional[SortInferenceExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInferenceRecommendationsJobsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[RecommendationJobStatusType] = None
    SortBy: Optional[ListInferenceRecommendationsJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ModelNameEquals: Optional[str] = None
    ModelPackageVersionArnEquals: Optional[str] = None


class ListLabelingJobsForWorkteamRequest(BaseValidatorModel):
    WorkteamArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal['CreationTime']] = None
    SortOrder: Optional[SortOrderType] = None


class ListLabelingJobsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[LabelingJobStatusType] = None


class ListLineageGroupsRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMlflowTrackingServersRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListModelBiasJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class ListModelCardExportJobsRequest(BaseValidatorModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    ModelCardExportJobNameContains: Optional[str] = None
    StatusEquals: Optional[ModelCardExportJobStatusType] = None
    SortBy: Optional[ModelCardExportJobSortByType] = None
    SortOrder: Optional[ModelCardExportJobSortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListModelCardVersionsRequest(BaseValidatorModel):
    ModelCardName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[Literal['Version']] = None
    SortOrder: Optional[ModelCardSortOrderType] = None


class ListModelCardsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None


class ListModelExplainabilityJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class ListModelPackageGroupsInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None


class ListModelPackagesInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageType: Optional[ModelPackageTypeType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelPackageSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListModelQualityJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class ListModelsInput(BaseValidatorModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class ListMonitoringAlertHistoryRequest(BaseValidatorModel):
    MonitoringScheduleName: Optional[str] = None
    MonitoringAlertName: Optional[str] = None
    SortBy: Optional[MonitoringAlertHistorySortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[MonitoringAlertStatusType] = None


class ListMonitoringExecutionsRequest(BaseValidatorModel):
    MonitoringScheduleName: Optional[str] = None
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringExecutionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ScheduledTimeBefore: Optional[Timestamp] = None
    ScheduledTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[ExecutionStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None


class ListMonitoringSchedulesRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringScheduleSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[ScheduleStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None


class ListNotebookInstanceLifecycleConfigsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKeyType] = None
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None


class ListNotebookInstancesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[NotebookInstanceSortKeyType] = None
    SortOrder: Optional[NotebookInstanceSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[NotebookInstanceStatusType] = None
    NotebookInstanceLifecycleConfigNameContains: Optional[str] = None
    DefaultCodeRepositoryContains: Optional[str] = None
    AdditionalCodeRepositoryEquals: Optional[str] = None


class ListOptimizationJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    OptimizationContains: Optional[str] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[OptimizationJobStatusType] = None
    SortBy: Optional[ListOptimizationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ListPipelineExecutionsRequest(BaseValidatorModel):
    PipelineName: str
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPipelinesRequest(BaseValidatorModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProcessingJobsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[ProcessingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProjectsInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ProjectSortByType] = None
    SortOrder: Optional[ProjectSortOrderType] = None


class ListResourceCatalogsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal['CreationTime']] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListStudioLifecycleConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    AppTypeEquals: Optional[StudioLifecycleConfigAppTypeType] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    ModifiedTimeBefore: Optional[Timestamp] = None
    ModifiedTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[StudioLifecycleConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None


class ListTrainingJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    WarmPoolStatusEquals: Optional[WarmPoolResourceStatusType] = None
    TrainingPlanArnEquals: Optional[str] = None


class ListTransformJobsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TransformJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTrialComponentsRequest(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    SourceArn: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortTrialComponentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTrialsRequest(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialComponentName: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortTrialsByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class QueryFilters(BaseValidatorModel):
    Types: Optional[List[str]] = None
    LineageTypes: Optional[List[LineageTypeType]] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None
    ModifiedBefore: Optional[Timestamp] = None
    ModifiedAfter: Optional[Timestamp] = None
    Properties: Optional[Dict[str, str]] = None


class SearchTrainingPlanOfferingsRequest(BaseValidatorModel):
    InstanceType: ReservedCapacityInstanceTypeType
    InstanceCount: int
    TargetResources: List[SageMakerResourceNameType]
    StartTimeAfter: Optional[Timestamp] = None
    EndTimeBefore: Optional[Timestamp] = None
    DurationHours: Optional[int] = None


class CreateTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str
    DisplayName: Optional[str] = None
    Status: Optional[TrialComponentStatus] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Parameters: Optional[Dict[str, TrialComponentParameterValue]] = None
    InputArtifacts: Optional[Dict[str, TrialComponentArtifact]] = None
    OutputArtifacts: Optional[Dict[str, TrialComponentArtifact]] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


class UpdateTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str
    DisplayName: Optional[str] = None
    Status: Optional[TrialComponentStatus] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Parameters: Optional[Dict[str, TrialComponentParameterValue]] = None
    ParametersToRemove: Optional[List[str]] = None
    InputArtifacts: Optional[Dict[str, TrialComponentArtifact]] = None
    InputArtifactsToRemove: Optional[List[str]] = None
    OutputArtifacts: Optional[Dict[str, TrialComponentArtifact]] = None
    OutputArtifactsToRemove: Optional[List[str]] = None


class CustomFileSystemConfig(BaseValidatorModel):
    EFSFileSystemConfig: Optional[EFSFileSystemConfig] = None
    FSxLustreFileSystemConfig: Optional[FSxLustreFileSystemConfig] = None


class CustomFileSystem(BaseValidatorModel):
    EFSFileSystem: Optional[EFSFileSystem] = None
    FSxLustreFileSystem: Optional[FSxLustreFileSystem] = None

DataQualityAppSpecificationUnion = Union[DataQualityAppSpecification, DataQualityAppSpecificationOutput]


class ModelBiasBaselineConfig(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResource] = None


class ModelExplainabilityBaselineConfig(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResource] = None


class ModelQualityBaselineConfig(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResource] = None


class DataQualityBaselineConfig(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResource] = None
    StatisticsResource: Optional[MonitoringStatisticsResource] = None


class MonitoringBaselineConfig(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResource] = None
    StatisticsResource: Optional[MonitoringStatisticsResource] = None


class DatasetDefinition(BaseValidatorModel):
    AthenaDatasetDefinition: Optional[AthenaDatasetDefinition] = None
    RedshiftDatasetDefinition: Optional[RedshiftDatasetDefinition] = None
    LocalPath: Optional[str] = None
    DataDistributionType: Optional[DataDistributionTypeType] = None
    InputMode: Optional[InputModeType] = None

DebugRuleConfigurationUnion = Union[DebugRuleConfiguration, DebugRuleConfigurationOutput]


class DefaultSpaceStorageSettings(BaseValidatorModel):
    DefaultEbsStorageSettings: Optional[DefaultEbsStorageSettings] = None


class DeleteDomainRequest(BaseValidatorModel):
    DomainId: str
    RetentionPolicy: Optional[RetentionPolicy] = None


class InferenceComponentContainerSpecificationSummary(BaseValidatorModel):
    DeployedImage: Optional[DeployedImage] = None
    ArtifactUrl: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None


class DeploymentRecommendation(BaseValidatorModel):
    RecommendationStatus: RecommendationStatusType
    RealTimeInferenceRecommendations: Optional[List[RealTimeInferenceRecommendation]] = None


class DeploymentStageStatusSummary(BaseValidatorModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigOutput
    DeploymentConfig: EdgeDeploymentConfig
    DeploymentStatus: EdgeDeploymentStatus


class DescribeDeviceResponse(BaseValidatorModel):
    DeviceArn: str
    DeviceName: str
    Description: str
    DeviceFleetName: str
    IotThingName: str
    RegistrationTime: datetime
    LatestHeartbeat: datetime
    Models: List[EdgeModel]
    MaxModels: int
    AgentVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEdgePackagingJobResponse(BaseValidatorModel):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: EdgeOutputConfig
    ResourceKey: str
    EdgePackagingJobStatus: EdgePackagingJobStatusType
    EdgePackagingJobStatusMessage: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ModelArtifact: str
    ModelSignature: str
    PresetDeploymentOutput: EdgePresetDeploymentOutput
    ResponseMetadata: ResponseMetadata


class DescribeEndpointInputWaitExtra(BaseValidatorModel):
    EndpointName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEndpointInputWait(BaseValidatorModel):
    EndpointName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImageRequestWaitExtraExtra(BaseValidatorModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImageRequestWaitExtra(BaseValidatorModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImageRequestWait(BaseValidatorModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImageVersionRequestWaitExtra(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImageVersionRequestWait(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNotebookInstanceInputWaitExtraExtra(BaseValidatorModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNotebookInstanceInputWaitExtra(BaseValidatorModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNotebookInstanceInputWait(BaseValidatorModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeProcessingJobRequestWait(BaseValidatorModel):
    ProcessingJobName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTrainingJobRequestWait(BaseValidatorModel):
    TrainingJobName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTransformJobRequestWait(BaseValidatorModel):
    TransformJobName: str
    WaiterConfig: Optional[WaiterConfig] = None


class ExperimentSummary(BaseValidatorModel):
    ExperimentArn: Optional[str] = None
    ExperimentName: Optional[str] = None
    DisplayName: Optional[str] = None
    ExperimentSource: Optional[ExperimentSource] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class FeatureGroupSummary(BaseValidatorModel):
    FeatureGroupName: str
    FeatureGroupArn: str
    CreationTime: datetime
    FeatureGroupStatus: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatus: Optional[OfflineStoreStatus] = None


class DescribeFeatureMetadataResponse(BaseValidatorModel):
    FeatureGroupArn: str
    FeatureGroupName: str
    FeatureName: str
    FeatureType: FeatureTypeType
    CreationTime: datetime
    LastModifiedTime: datetime
    Description: str
    Parameters: List[FeatureParameter]
    ResponseMetadata: ResponseMetadata


class FeatureMetadata(BaseValidatorModel):
    FeatureGroupArn: Optional[str] = None
    FeatureGroupName: Optional[str] = None
    FeatureName: Optional[str] = None
    FeatureType: Optional[FeatureTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Description: Optional[str] = None
    Parameters: Optional[List[FeatureParameter]] = None


class UpdateFeatureMetadataRequest(BaseValidatorModel):
    FeatureGroupName: str
    FeatureName: str
    Description: Optional[str] = None
    ParameterAdditions: Optional[List[FeatureParameter]] = None
    ParameterRemovals: Optional[List[str]] = None


class DescribeHubContentResponse(BaseValidatorModel):
    HubContentName: str
    HubContentArn: str
    HubContentVersion: str
    HubContentType: HubContentTypeType
    DocumentSchemaVersion: str
    HubName: str
    HubArn: str
    HubContentDisplayName: str
    HubContentDescription: str
    HubContentMarkdown: str
    HubContentDocument: str
    SageMakerPublicHubContentArn: str
    ReferenceMinVersion: str
    SupportStatus: HubContentSupportStatusType
    HubContentSearchKeywords: List[str]
    HubContentDependencies: List[HubContentDependency]
    HubContentStatus: HubContentStatusType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeHumanTaskUiResponse(BaseValidatorModel):
    HumanTaskUiArn: str
    HumanTaskUiName: str
    HumanTaskUiStatus: HumanTaskUiStatusType
    CreationTime: datetime
    UiTemplate: UiTemplateInfo
    ResponseMetadata: ResponseMetadata


class InferenceExperimentSummary(BaseValidatorModel):
    Name: str
    Type: Literal['ShadowMode']
    Status: InferenceExperimentStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    Schedule: Optional[InferenceExperimentScheduleOutput] = None
    StatusReason: Optional[str] = None
    Description: Optional[str] = None
    CompletionTime: Optional[datetime] = None
    RoleArn: Optional[str] = None


class DescribeModelCardExportJobResponse(BaseValidatorModel):
    ModelCardExportJobName: str
    ModelCardExportJobArn: str
    Status: ModelCardExportJobStatusType
    ModelCardName: str
    ModelCardVersion: int
    OutputConfig: ModelCardExportOutputConfig
    CreatedAt: datetime
    LastModifiedAt: datetime
    FailureReason: str
    ExportArtifacts: ModelCardExportArtifacts
    ResponseMetadata: ResponseMetadata


class ListMonitoringExecutionsResponse(BaseValidatorModel):
    MonitoringExecutionSummaries: List[MonitoringExecutionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePartnerAppResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Type: PartnerAppTypeType
    Status: PartnerAppStatusType
    CreationTime: datetime
    ExecutionRoleArn: str
    BaseUrl: str
    MaintenanceConfig: PartnerAppMaintenanceConfig
    Tier: str
    Version: str
    ApplicationConfig: PartnerAppConfigOutput
    AuthType: Literal['IAM']
    EnableIamSessionBasedIdentity: bool
    Error: ErrorInfo
    ResponseMetadata: ResponseMetadata


class DescribeSubscribedWorkteamResponse(BaseValidatorModel):
    SubscribedWorkteam: SubscribedWorkteam
    ResponseMetadata: ResponseMetadata


class ListSubscribedWorkteamsResponse(BaseValidatorModel):
    SubscribedWorkteams: List[SubscribedWorkteam]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TrainingJobSummary(BaseValidatorModel):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime
    TrainingJobStatus: TrainingJobStatusType
    TrainingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    SecondaryStatus: Optional[SecondaryStatusType] = None
    WarmPoolStatus: Optional[WarmPoolStatus] = None
    TrainingPlanArn: Optional[str] = None


class DescribeTrainingPlanResponse(BaseValidatorModel):
    TrainingPlanArn: str
    TrainingPlanName: str
    Status: TrainingPlanStatusType
    StatusMessage: str
    DurationHours: int
    DurationMinutes: int
    StartTime: datetime
    EndTime: datetime
    UpfrontFee: str
    CurrencyCode: str
    TotalInstanceCount: int
    AvailableInstanceCount: int
    InUseInstanceCount: int
    TargetResources: List[SageMakerResourceNameType]
    ReservedCapacitySummaries: List[ReservedCapacitySummary]
    ResponseMetadata: ResponseMetadata


class TrainingPlanSummary(BaseValidatorModel):
    TrainingPlanArn: str
    TrainingPlanName: str
    Status: TrainingPlanStatusType
    StatusMessage: Optional[str] = None
    DurationHours: Optional[int] = None
    DurationMinutes: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    UpfrontFee: Optional[str] = None
    CurrencyCode: Optional[str] = None
    TotalInstanceCount: Optional[int] = None
    AvailableInstanceCount: Optional[int] = None
    InUseInstanceCount: Optional[int] = None
    TargetResources: Optional[List[SageMakerResourceNameType]] = None
    ReservedCapacitySummaries: Optional[List[ReservedCapacitySummary]] = None


class TrialSummary(BaseValidatorModel):
    TrialArn: Optional[str] = None
    TrialName: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialSource: Optional[TrialSource] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class DesiredWeightAndCapacity(BaseValidatorModel):
    VariantName: str
    DesiredWeight: Optional[float] = None
    DesiredInstanceCount: Optional[int] = None
    ServerlessUpdateConfig: Optional[ProductionVariantServerlessUpdateConfig] = None


class ListStageDevicesResponse(BaseValidatorModel):
    DeviceDeploymentSummaries: List[DeviceDeploymentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDeviceFleetsResponse(BaseValidatorModel):
    DeviceFleetSummaries: List[DeviceFleetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DeviceSelectionConfigUnion = Union[DeviceSelectionConfig, DeviceSelectionConfigOutput]


class DeviceSummary(BaseValidatorModel):
    DeviceName: str
    DeviceArn: str
    Description: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    IotThingName: Optional[str] = None
    RegistrationTime: Optional[datetime] = None
    LatestHeartbeat: Optional[datetime] = None
    Models: Optional[List[EdgeModelSummary]] = None
    AgentVersion: Optional[str] = None


class RegisterDevicesRequest(BaseValidatorModel):
    DeviceFleetName: str
    Devices: List[Device]
    Tags: Optional[List[Tag]] = None


class UpdateDevicesRequest(BaseValidatorModel):
    DeviceFleetName: str
    Devices: List[Device]

DockerSettingsUnion = Union[DockerSettings, DockerSettingsOutput]


class ListDomainsResponse(BaseValidatorModel):
    Domains: List[DomainDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DriftCheckBias(BaseValidatorModel):
    ConfigFile: Optional[FileSource] = None
    PreTrainingConstraints: Optional[MetricsSource] = None
    PostTrainingConstraints: Optional[MetricsSource] = None


class DriftCheckExplainability(BaseValidatorModel):
    Constraints: Optional[MetricsSource] = None
    ConfigFile: Optional[FileSource] = None


class SpaceStorageSettings(BaseValidatorModel):
    EbsStorageSettings: Optional[EbsStorageSettings] = None


class ListEdgeDeploymentPlansResponse(BaseValidatorModel):
    EdgeDeploymentPlanSummaries: List[EdgeDeploymentPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDeviceFleetReportResponse(BaseValidatorModel):
    DeviceFleetArn: str
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfig
    Description: str
    ReportGenerated: datetime
    DeviceStats: DeviceStats
    AgentVersions: List[AgentVersion]
    ModelStats: List[EdgeModelStat]
    ResponseMetadata: ResponseMetadata


class ListEdgePackagingJobsResponse(BaseValidatorModel):
    EdgePackagingJobSummaries: List[EdgePackagingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEndpointConfigsOutput(BaseValidatorModel):
    EndpointConfigs: List[EndpointConfigSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EndpointOutputConfiguration(BaseValidatorModel):
    EndpointName: str
    VariantName: str
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    InitialInstanceCount: Optional[int] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfig] = None


class EndpointPerformance(BaseValidatorModel):
    Metrics: InferenceMetrics
    EndpointInfo: EndpointInfo


class ListEndpointsOutput(BaseValidatorModel):
    Endpoints: List[EndpointSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModelConfiguration(BaseValidatorModel):
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameters: Optional[List[EnvironmentParameter]] = None
    CompilationJobName: Optional[str] = None


class NestedFilters(BaseValidatorModel):
    NestedPropertyName: str
    Filters: List[Filter]


class HyperParameterTrainingJobSummary(BaseValidatorModel):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime
    TrainingJobStatus: TrainingJobStatusType
    TunedHyperParameters: Dict[str, str]
    TrainingJobDefinitionName: Optional[str] = None
    TuningJobName: Optional[str] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    FinalHyperParameterTuningJobObjectiveMetric: Optional[FinalHyperParameterTuningJobObjectiveMetric] = None
    ObjectiveStatus: Optional[ObjectiveStatusType] = None


class ListFlowDefinitionsResponse(BaseValidatorModel):
    FlowDefinitionSummaries: List[FlowDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetScalingConfigurationRecommendationRequest(BaseValidatorModel):
    InferenceRecommendationsJobName: str
    RecommendationId: Optional[str] = None
    EndpointName: Optional[str] = None
    TargetCpuUtilizationPerCore: Optional[int] = None
    ScalingPolicyObjective: Optional[ScalingPolicyObjective] = None


class GetSearchSuggestionsResponse(BaseValidatorModel):
    PropertyNameSuggestions: List[PropertyNameSuggestion]
    ResponseMetadata: ResponseMetadata


class UpdateCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str
    GitConfig: Optional[GitConfigForUpdate] = None


class StudioWebPortalSettingsOutput(BaseValidatorModel):
    HiddenMlTools: Optional[List[MlToolsType]] = None
    HiddenAppTypes: Optional[List[AppTypeType]] = None
    HiddenInstanceTypes: Optional[List[AppInstanceTypeType]] = None
    HiddenSageMakerImageVersionAliases: Optional[List[HiddenSageMakerImageOutput]] = None


class StudioWebPortalSettings(BaseValidatorModel):
    HiddenMlTools: Optional[List[MlToolsType]] = None
    HiddenAppTypes: Optional[List[AppTypeType]] = None
    HiddenInstanceTypes: Optional[List[AppInstanceTypeType]] = None
    HiddenSageMakerImageVersionAliases: Optional[List[HiddenSageMakerImage]] = None


class ListHubContentVersionsResponse(BaseValidatorModel):
    HubContentSummaries: List[HubContentInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHubContentsResponse(BaseValidatorModel):
    HubContentSummaries: List[HubContentInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHubsResponse(BaseValidatorModel):
    HubSummaries: List[HubInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HumanLoopActivationConfig(BaseValidatorModel):
    HumanLoopActivationConditionsConfig: HumanLoopActivationConditionsConfig


class ListHumanTaskUisResponse(BaseValidatorModel):
    HumanTaskUiSummaries: List[HumanTaskUiSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HyperParameterTuningResourceConfigOutput(BaseValidatorModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal['Prioritized']] = None
    InstanceConfigs: Optional[List[HyperParameterTuningInstanceConfig]] = None


class HyperParameterTuningResourceConfig(BaseValidatorModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal['Prioritized']] = None
    InstanceConfigs: Optional[List[HyperParameterTuningInstanceConfig]] = None


class HyperParameterTuningJobSummary(BaseValidatorModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobArn: str
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatusType
    Strategy: HyperParameterTuningJobStrategyTypeType
    CreationTime: datetime
    TrainingJobStatusCounters: TrainingJobStatusCounters
    ObjectiveStatusCounters: ObjectiveStatusCounters
    HyperParameterTuningEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    ResourceLimits: Optional[ResourceLimits] = None


class HyperParameterTuningJobStrategyConfig(BaseValidatorModel):
    HyperbandStrategyConfig: Optional[HyperbandStrategyConfig] = None


class HyperParameterTuningJobWarmStartConfigOutput(BaseValidatorModel):
    ParentHyperParameterTuningJobs: List[ParentHyperParameterTuningJob]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType


class HyperParameterTuningJobWarmStartConfig(BaseValidatorModel):
    ParentHyperParameterTuningJobs: List[ParentHyperParameterTuningJob]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType


class UserContext(BaseValidatorModel):
    UserProfileArn: Optional[str] = None
    UserProfileName: Optional[str] = None
    DomainId: Optional[str] = None
    IamIdentity: Optional[IamIdentity] = None


class S3Presign(BaseValidatorModel):
    IamPolicyConstraints: Optional[IamPolicyConstraints] = None


class ImageConfig(BaseValidatorModel):
    RepositoryAccessMode: RepositoryAccessModeType
    RepositoryAuthConfig: Optional[RepositoryAuthConfig] = None


class ListImagesResponse(BaseValidatorModel):
    Images: List[Image]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListImageVersionsResponse(BaseValidatorModel):
    ImageVersions: List[ImageVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InferenceComponentRollingUpdatePolicy(BaseValidatorModel):
    MaximumBatchSize: InferenceComponentCapacitySize
    WaitIntervalInSeconds: int
    MaximumExecutionTimeoutInSeconds: Optional[int] = None
    RollbackMaximumBatchSize: Optional[InferenceComponentCapacitySize] = None


class InferenceComponentSpecification(BaseValidatorModel):
    ModelName: Optional[str] = None
    Container: Optional[InferenceComponentContainerSpecification] = None
    StartupParameters: Optional[InferenceComponentStartupParameters] = None
    ComputeResourceRequirements: Optional[InferenceComponentComputeResourceRequirements] = None
    BaseInferenceComponentName: Optional[str] = None


class ListInferenceComponentsOutput(BaseValidatorModel):
    InferenceComponents: List[InferenceComponentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInferenceRecommendationsJobsResponse(BaseValidatorModel):
    InferenceRecommendationsJobs: List[InferenceRecommendationsJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResourceConfigOutput(BaseValidatorModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroup]] = None
    TrainingPlanArn: Optional[str] = None


class ResourceConfig(BaseValidatorModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroup]] = None
    TrainingPlanArn: Optional[str] = None


class ParameterRangeOutput(BaseValidatorModel):
    IntegerParameterRangeSpecification: Optional[IntegerParameterRangeSpecification] = None
    ContinuousParameterRangeSpecification: Optional[ContinuousParameterRangeSpecification] = None
    CategoricalParameterRangeSpecification: Optional[CategoricalParameterRangeSpecificationOutput] = None


class ParameterRange(BaseValidatorModel):
    IntegerParameterRangeSpecification: Optional[IntegerParameterRangeSpecification] = None
    ContinuousParameterRangeSpecification: Optional[ContinuousParameterRangeSpecification] = None
    CategoricalParameterRangeSpecification: Optional[CategoricalParameterRangeSpecification] = None


class ParameterRangesOutput(BaseValidatorModel):
    IntegerParameterRanges: Optional[List[IntegerParameterRange]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRange]] = None
    CategoricalParameterRanges: Optional[List[CategoricalParameterRangeOutput]] = None
    AutoParameters: Optional[List[AutoParameter]] = None


class KernelGatewayImageConfigOutput(BaseValidatorModel):
    KernelSpecs: List[KernelSpec]
    FileSystemConfig: Optional[FileSystemConfig] = None


class KernelGatewayImageConfig(BaseValidatorModel):
    KernelSpecs: List[KernelSpec]
    FileSystemConfig: Optional[FileSystemConfig] = None


class LabelingJobForWorkteamSummary(BaseValidatorModel):
    JobReferenceCode: str
    WorkRequesterAccountId: str
    CreationTime: datetime
    LabelingJobName: Optional[str] = None
    LabelCounters: Optional[LabelCountersForWorkteam] = None
    NumberOfHumanWorkersPerDataObject: Optional[int] = None


class LabelingJobDataSource(BaseValidatorModel):
    S3DataSource: Optional[LabelingJobS3DataSource] = None
    SnsDataSource: Optional[LabelingJobSnsDataSource] = None


class ListLineageGroupsResponse(BaseValidatorModel):
    LineageGroupSummaries: List[LineageGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListActionsRequestPaginate(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAlgorithmsInputPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAliasesRequestPaginate(BaseValidatorModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAppImageConfigsRequestPaginate(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    ModifiedTimeBefore: Optional[Timestamp] = None
    ModifiedTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[AppImageConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAppsRequestPaginate(BaseValidatorModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal['CreationTime']] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListArtifactsRequestPaginate(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[Literal['CreationTime']] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociationsRequestPaginate(BaseValidatorModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortAssociationsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAutoMLJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[AutoMLJobStatusType] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[AutoMLSortByType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCandidatesForAutoMLJobRequestPaginate(BaseValidatorModel):
    AutoMLJobName: str
    StatusEquals: Optional[CandidateStatusType] = None
    CandidateNameEquals: Optional[str] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[CandidateSortByType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClusterNodesRequestPaginate(BaseValidatorModel):
    ClusterName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    InstanceGroupNameContains: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClusterSchedulerConfigsRequestPaginate(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    ClusterArn: Optional[str] = None
    Status: Optional[SchedulerResourceStatusType] = None
    SortBy: Optional[SortClusterSchedulerConfigByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    TrainingPlanArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCodeRepositoriesInputPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[CodeRepositorySortByType] = None
    SortOrder: Optional[CodeRepositorySortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCompilationJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[CompilationJobStatusType] = None
    SortBy: Optional[ListCompilationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComputeQuotasRequestPaginate(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    Status: Optional[SchedulerResourceStatusType] = None
    ClusterArn: Optional[str] = None
    SortBy: Optional[SortQuotaByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContextsRequestPaginate(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataQualityJobDefinitionsRequestPaginate(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeviceFleetsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ListDeviceFleetsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDevicesRequestPaginate(BaseValidatorModel):
    LatestHeartbeatAfter: Optional[Timestamp] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEdgeDeploymentPlansRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    DeviceFleetNameContains: Optional[str] = None
    SortBy: Optional[ListEdgeDeploymentPlansSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEdgePackagingJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    ModelNameContains: Optional[str] = None
    StatusEquals: Optional[EdgePackagingJobStatusType] = None
    SortBy: Optional[ListEdgePackagingJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEndpointConfigsInputPaginate(BaseValidatorModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEndpointsInputPaginate(BaseValidatorModel):
    SortBy: Optional[EndpointSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[EndpointStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExperimentsRequestPaginate(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFeatureGroupsRequestPaginate(BaseValidatorModel):
    NameContains: Optional[str] = None
    FeatureGroupStatusEquals: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValueType] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[FeatureGroupSortOrderType] = None
    SortBy: Optional[FeatureGroupSortByType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowDefinitionsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHumanTaskUisRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHyperParameterTuningJobsRequestPaginate(BaseValidatorModel):
    SortBy: Optional[HyperParameterTuningJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    StatusEquals: Optional[HyperParameterTuningJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImageVersionsRequestPaginate(BaseValidatorModel):
    ImageName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    SortBy: Optional[ImageVersionSortByType] = None
    SortOrder: Optional[ImageVersionSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImagesRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ImageSortByType] = None
    SortOrder: Optional[ImageSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInferenceComponentsInputPaginate(BaseValidatorModel):
    SortBy: Optional[InferenceComponentSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[InferenceComponentStatusType] = None
    EndpointNameEquals: Optional[str] = None
    VariantNameEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInferenceExperimentsRequestPaginate(BaseValidatorModel):
    NameContains: Optional[str] = None
    Type: Optional[Literal['ShadowMode']] = None
    StatusEquals: Optional[InferenceExperimentStatusType] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    SortBy: Optional[SortInferenceExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInferenceRecommendationsJobStepsRequestPaginate(BaseValidatorModel):
    JobName: str
    Status: Optional[RecommendationJobStatusType] = None
    StepType: Optional[Literal['BENCHMARK']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInferenceRecommendationsJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[RecommendationJobStatusType] = None
    SortBy: Optional[ListInferenceRecommendationsJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    ModelNameEquals: Optional[str] = None
    ModelPackageVersionArnEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLabelingJobsForWorkteamRequestPaginate(BaseValidatorModel):
    WorkteamArn: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal['CreationTime']] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLabelingJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[LabelingJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLineageGroupsRequestPaginate(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMlflowTrackingServersRequestPaginate(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelBiasJobDefinitionsRequestPaginate(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelCardExportJobsRequestPaginate(BaseValidatorModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    ModelCardExportJobNameContains: Optional[str] = None
    StatusEquals: Optional[ModelCardExportJobStatusType] = None
    SortBy: Optional[ModelCardExportJobSortByType] = None
    SortOrder: Optional[ModelCardExportJobSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelCardVersionsRequestPaginate(BaseValidatorModel):
    ModelCardName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SortBy: Optional[Literal['Version']] = None
    SortOrder: Optional[ModelCardSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelCardsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelExplainabilityJobDefinitionsRequestPaginate(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelPackageGroupsInputPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelPackagesInputPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageType: Optional[ModelPackageTypeType] = None
    SortBy: Optional[ModelPackageSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelQualityJobDefinitionsRequestPaginate(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelsInputPaginate(BaseValidatorModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitoringAlertHistoryRequestPaginate(BaseValidatorModel):
    MonitoringScheduleName: Optional[str] = None
    MonitoringAlertName: Optional[str] = None
    SortBy: Optional[MonitoringAlertHistorySortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[MonitoringAlertStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitoringAlertsRequestPaginate(BaseValidatorModel):
    MonitoringScheduleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitoringExecutionsRequestPaginate(BaseValidatorModel):
    MonitoringScheduleName: Optional[str] = None
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringExecutionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    ScheduledTimeBefore: Optional[Timestamp] = None
    ScheduledTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[ExecutionStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitoringSchedulesRequestPaginate(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringScheduleSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[ScheduleStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotebookInstanceLifecycleConfigsInputPaginate(BaseValidatorModel):
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKeyType] = None
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotebookInstancesInputPaginate(BaseValidatorModel):
    SortBy: Optional[NotebookInstanceSortKeyType] = None
    SortOrder: Optional[NotebookInstanceSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    StatusEquals: Optional[NotebookInstanceStatusType] = None
    NotebookInstanceLifecycleConfigNameContains: Optional[str] = None
    DefaultCodeRepositoryContains: Optional[str] = None
    AdditionalCodeRepositoryEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOptimizationJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    OptimizationContains: Optional[str] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[OptimizationJobStatusType] = None
    SortBy: Optional[ListOptimizationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPartnerAppsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelineExecutionStepsRequestPaginate(BaseValidatorModel):
    PipelineExecutionArn: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelineExecutionsRequestPaginate(BaseValidatorModel):
    PipelineName: str
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelineParametersForExecutionRequestPaginate(BaseValidatorModel):
    PipelineExecutionArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelinesRequestPaginate(BaseValidatorModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProcessingJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[ProcessingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceCatalogsRequestPaginate(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal['CreationTime']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSpacesRequestPaginate(BaseValidatorModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStageDevicesRequestPaginate(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str
    ExcludeDevicesDeployedInOtherStage: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStudioLifecycleConfigsRequestPaginate(BaseValidatorModel):
    NameContains: Optional[str] = None
    AppTypeEquals: Optional[StudioLifecycleConfigAppTypeType] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None
    ModifiedTimeBefore: Optional[Timestamp] = None
    ModifiedTimeAfter: Optional[Timestamp] = None
    SortBy: Optional[StudioLifecycleConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscribedWorkteamsRequestPaginate(BaseValidatorModel):
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsInputPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrainingJobsForHyperParameterTuningJobRequestPaginate(BaseValidatorModel):
    HyperParameterTuningJobName: str
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[TrainingJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrainingJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    WarmPoolStatusEquals: Optional[WarmPoolResourceStatusType] = None
    TrainingPlanArnEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTransformJobsRequestPaginate(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    LastModifiedTimeAfter: Optional[Timestamp] = None
    LastModifiedTimeBefore: Optional[Timestamp] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TransformJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrialComponentsRequestPaginate(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    SourceArn: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortTrialComponentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrialsRequestPaginate(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialComponentName: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortTrialsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserProfilesRequestPaginate(BaseValidatorModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[UserProfileSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkforcesRequestPaginate(BaseValidatorModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkteamsRequestPaginate(BaseValidatorModel):
    SortBy: Optional[ListWorkteamsSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataQualityJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelBiasJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelExplainabilityJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelQualityJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMlflowTrackingServersResponse(BaseValidatorModel):
    TrackingServerSummaries: List[TrackingServerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelCardExportJobsResponse(BaseValidatorModel):
    ModelCardExportJobSummaries: List[ModelCardExportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelCardVersionsResponse(BaseValidatorModel):
    ModelCardVersionSummaryList: List[ModelCardVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelCardsResponse(BaseValidatorModel):
    ModelCardSummaries: List[ModelCardSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelMetadataResponse(BaseValidatorModel):
    ModelMetadataSummaries: List[ModelMetadataSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelPackageGroupsOutput(BaseValidatorModel):
    ModelPackageGroupSummaryList: List[ModelPackageGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelPackagesOutput(BaseValidatorModel):
    ModelPackageSummaryList: List[ModelPackageSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListModelsOutput(BaseValidatorModel):
    Models: List[ModelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMonitoringAlertHistoryResponse(BaseValidatorModel):
    MonitoringAlertHistory: List[MonitoringAlertHistorySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMonitoringSchedulesResponse(BaseValidatorModel):
    MonitoringScheduleSummaries: List[MonitoringScheduleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNotebookInstanceLifecycleConfigsOutput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigs: List[NotebookInstanceLifecycleConfigSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNotebookInstancesOutput(BaseValidatorModel):
    NotebookInstances: List[NotebookInstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOptimizationJobsResponse(BaseValidatorModel):
    OptimizationJobSummaries: List[OptimizationJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPartnerAppsResponse(BaseValidatorModel):
    Summaries: List[PartnerAppSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPipelineExecutionsResponse(BaseValidatorModel):
    PipelineExecutionSummaries: List[PipelineExecutionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPipelineParametersForExecutionResponse(BaseValidatorModel):
    PipelineParameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPipelinesResponse(BaseValidatorModel):
    PipelineSummaries: List[PipelineSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProcessingJobsResponse(BaseValidatorModel):
    ProcessingJobSummaries: List[ProcessingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProjectsOutput(BaseValidatorModel):
    ProjectSummaryList: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceCatalogsResponse(BaseValidatorModel):
    ResourceCatalogs: List[ResourceCatalog]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStudioLifecycleConfigsResponse(BaseValidatorModel):
    StudioLifecycleConfigs: List[StudioLifecycleConfigDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrainingPlansRequestPaginate(BaseValidatorModel):
    StartTimeAfter: Optional[Timestamp] = None
    StartTimeBefore: Optional[Timestamp] = None
    SortBy: Optional[TrainingPlanSortByType] = None
    SortOrder: Optional[TrainingPlanSortOrderType] = None
    Filters: Optional[List[TrainingPlanFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrainingPlansRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeAfter: Optional[Timestamp] = None
    StartTimeBefore: Optional[Timestamp] = None
    SortBy: Optional[TrainingPlanSortByType] = None
    SortOrder: Optional[TrainingPlanSortOrderType] = None
    Filters: Optional[List[TrainingPlanFilter]] = None


class ListTransformJobsResponse(BaseValidatorModel):
    TransformJobSummaries: List[TransformJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUserProfilesResponse(BaseValidatorModel):
    UserProfiles: List[UserProfileDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MemberDefinitionOutput(BaseValidatorModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinition] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionOutput] = None


class MetricSpecification(BaseValidatorModel):
    Predefined: Optional[PredefinedMetricSpecification] = None
    Customized: Optional[CustomizedMetricSpecification] = None


class S3DataSourceOutput(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[List[str]] = None
    InstanceGroupNames: Optional[List[str]] = None
    ModelAccessConfig: Optional[ModelAccessConfig] = None
    HubAccessConfig: Optional[HubAccessConfig] = None


class S3DataSource(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[List[str]] = None
    InstanceGroupNames: Optional[List[str]] = None
    ModelAccessConfig: Optional[ModelAccessConfig] = None
    HubAccessConfig: Optional[HubAccessConfig] = None


class S3ModelDataSource(BaseValidatorModel):
    S3Uri: str
    S3DataType: S3ModelDataTypeType
    CompressionType: ModelCompressionTypeType
    ModelAccessConfig: Optional[ModelAccessConfig] = None
    HubAccessConfig: Optional[InferenceHubAccessConfig] = None
    ManifestS3Uri: Optional[str] = None
    ETag: Optional[str] = None
    ManifestEtag: Optional[str] = None


class TextGenerationJobConfigOutput(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    BaseModelName: Optional[str] = None
    TextGenerationHyperParameters: Optional[Dict[str, str]] = None
    ModelAccessConfig: Optional[ModelAccessConfig] = None


class TextGenerationJobConfig(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    BaseModelName: Optional[str] = None
    TextGenerationHyperParameters: Optional[Dict[str, str]] = None
    ModelAccessConfig: Optional[ModelAccessConfig] = None

ModelBiasAppSpecificationUnion = Union[ModelBiasAppSpecification, ModelBiasAppSpecificationOutput]

ModelCompilationConfigUnion = Union[ModelCompilationConfig, ModelCompilationConfigOutput]


class MonitoringAlertActions(BaseValidatorModel):
    ModelDashboardIndicator: Optional[ModelDashboardIndicatorAction] = None

ModelExplainabilityAppSpecificationUnion = Union[ModelExplainabilityAppSpecification, ModelExplainabilityAppSpecificationOutput]


class ModelInfrastructureConfig(BaseValidatorModel):
    InfrastructureType: Literal['RealTimeInference']
    RealTimeInferenceConfig: RealTimeInferenceConfig


class RecommendationJobStoppingConditionsOutput(BaseValidatorModel):
    MaxInvocations: Optional[int] = None
    ModelLatencyThresholds: Optional[List[ModelLatencyThreshold]] = None
    FlatInvocations: Optional[FlatInvocationsType] = None


class RecommendationJobStoppingConditions(BaseValidatorModel):
    MaxInvocations: Optional[int] = None
    ModelLatencyThresholds: Optional[List[ModelLatencyThreshold]] = None
    FlatInvocations: Optional[FlatInvocationsType] = None


class ModelMetadataSearchExpression(BaseValidatorModel):
    Filters: Optional[List[ModelMetadataFilter]] = None


class ModelPackageStatusDetails(BaseValidatorModel):
    ValidationStatuses: List[ModelPackageStatusItem]
    ImageScanStatuses: Optional[List[ModelPackageStatusItem]] = None

ModelQualityAppSpecificationUnion = Union[ModelQualityAppSpecification, ModelQualityAppSpecificationOutput]

ModelQuantizationConfigUnion = Union[ModelQuantizationConfig, ModelQuantizationConfigOutput]


class OptimizationConfigOutput(BaseValidatorModel):
    ModelQuantizationConfig: Optional[ModelQuantizationConfigOutput] = None
    ModelCompilationConfig: Optional[ModelCompilationConfigOutput] = None
    ModelShardingConfig: Optional[ModelShardingConfigOutput] = None

ModelShardingConfigUnion = Union[ModelShardingConfig, ModelShardingConfigOutput]


class MonitoringResources(BaseValidatorModel):
    ClusterConfig: MonitoringClusterConfig


class MonitoringDatasetFormatOutput(BaseValidatorModel):
    Csv: Optional[MonitoringCsvDatasetFormat] = None
    Json: Optional[MonitoringJsonDatasetFormat] = None
    Parquet: Optional[Dict[str, Any]] = None


class MonitoringDatasetFormat(BaseValidatorModel):
    Csv: Optional[MonitoringCsvDatasetFormat] = None
    Json: Optional[MonitoringJsonDatasetFormat] = None
    Parquet: Optional[Dict[str, Any]] = None


class MonitoringOutput(BaseValidatorModel):
    S3Output: MonitoringS3Output

NeoVpcConfigUnion = Union[NeoVpcConfig, NeoVpcConfigOutput]


class OfflineStoreConfig(BaseValidatorModel):
    S3StorageConfig: S3StorageConfig
    DisableGlueTableCreation: Optional[bool] = None
    DataCatalogConfig: Optional[DataCatalogConfig] = None
    TableFormat: Optional[TableFormatType] = None

OidcMemberDefinitionUnion = Union[OidcMemberDefinition, OidcMemberDefinitionOutput]


class OnlineStoreConfig(BaseValidatorModel):
    SecurityConfig: Optional[OnlineStoreSecurityConfig] = None
    EnableOnlineStore: Optional[bool] = None
    TtlDuration: Optional[TtlDuration] = None
    StorageType: Optional[StorageTypeType] = None


class OnlineStoreConfigUpdate(BaseValidatorModel):
    TtlDuration: Optional[TtlDuration] = None


class OptimizationJobModelSourceS3(BaseValidatorModel):
    S3Uri: Optional[str] = None
    ModelAccessConfig: Optional[OptimizationModelAccessConfig] = None

OptimizationVpcConfigUnion = Union[OptimizationVpcConfig, OptimizationVpcConfigOutput]


class OutputConfig(BaseValidatorModel):
    S3OutputLocation: str
    TargetDevice: Optional[TargetDeviceType] = None
    TargetPlatform: Optional[TargetPlatform] = None
    CompilerOptions: Optional[str] = None
    KmsKeyId: Optional[str] = None

PartnerAppConfigUnion = Union[PartnerAppConfig, PartnerAppConfigOutput]


class PendingProductionVariantSummary(BaseValidatorModel):
    VariantName: str
    DeployedImages: Optional[List[DeployedImage]] = None
    CurrentWeight: Optional[float] = None
    DesiredWeight: Optional[float] = None
    CurrentInstanceCount: Optional[int] = None
    DesiredInstanceCount: Optional[int] = None
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    AcceleratorType: Optional[ProductionVariantAcceleratorTypeType] = None
    VariantStatus: Optional[List[ProductionVariantStatus]] = None
    CurrentServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    DesiredServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScaling] = None
    RoutingConfig: Optional[ProductionVariantRoutingConfig] = None


class ProductionVariantSummary(BaseValidatorModel):
    VariantName: str
    DeployedImages: Optional[List[DeployedImage]] = None
    CurrentWeight: Optional[float] = None
    DesiredWeight: Optional[float] = None
    CurrentInstanceCount: Optional[int] = None
    DesiredInstanceCount: Optional[int] = None
    VariantStatus: Optional[List[ProductionVariantStatus]] = None
    CurrentServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    DesiredServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScaling] = None
    RoutingConfig: Optional[ProductionVariantRoutingConfig] = None


class SchedulerConfigOutput(BaseValidatorModel):
    PriorityClasses: Optional[List[PriorityClass]] = None
    FairShare: Optional[FairShareType] = None


class SchedulerConfig(BaseValidatorModel):
    PriorityClasses: Optional[List[PriorityClass]] = None
    FairShare: Optional[FairShareType] = None


class ProcessingResources(BaseValidatorModel):
    ClusterConfig: ProcessingClusterConfig


class ProcessingOutput(BaseValidatorModel):
    OutputName: str
    S3Output: Optional[ProcessingS3Output] = None
    FeatureStoreOutput: Optional[ProcessingFeatureStoreOutput] = None
    AppManaged: Optional[bool] = None


class ProductionVariant(BaseValidatorModel):
    VariantName: str
    ModelName: Optional[str] = None
    InitialInstanceCount: Optional[int] = None
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    InitialVariantWeight: Optional[float] = None
    AcceleratorType: Optional[ProductionVariantAcceleratorTypeType] = None
    CoreDumpConfig: Optional[ProductionVariantCoreDumpConfig] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    VolumeSizeInGB: Optional[int] = None
    ModelDataDownloadTimeoutInSeconds: Optional[int] = None
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int] = None
    EnableSSMAccess: Optional[bool] = None
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScaling] = None
    RoutingConfig: Optional[ProductionVariantRoutingConfig] = None
    InferenceAmiVersion: Optional[ProductionVariantInferenceAmiVersionType] = None

ProfilerConfigUnion = Union[ProfilerConfig, ProfilerConfigOutput]

ProfilerRuleConfigurationUnion = Union[ProfilerRuleConfiguration, ProfilerRuleConfigurationOutput]


class SuggestionQuery(BaseValidatorModel):
    PropertyNameQuery: Optional[PropertyNameQuery] = None


class ServiceCatalogProvisioningDetailsOutput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameter]] = None


class ServiceCatalogProvisioningDetails(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameter]] = None


class ServiceCatalogProvisioningUpdateDetails(BaseValidatorModel):
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameter]] = None


class PublicWorkforceTaskPrice(BaseValidatorModel):
    AmountInUsd: Optional[USD] = None


class QueryLineageResponse(BaseValidatorModel):
    Vertices: List[Vertex]
    Edges: List[Edge]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RecommendationJobOutputConfig(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    CompiledOutputConfig: Optional[RecommendationJobCompiledOutputConfig] = None


class RecommendationJobContainerConfigOutput(BaseValidatorModel):
    Domain: Optional[str] = None
    Task: Optional[str] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    PayloadConfig: Optional[RecommendationJobPayloadConfigOutput] = None
    NearestModelName: Optional[str] = None
    SupportedInstanceTypes: Optional[List[str]] = None
    SupportedEndpointType: Optional[RecommendationJobSupportedEndpointTypeType] = None
    DataInputConfig: Optional[str] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None


class RecommendationJobContainerConfig(BaseValidatorModel):
    Domain: Optional[str] = None
    Task: Optional[str] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    PayloadConfig: Optional[RecommendationJobPayloadConfig] = None
    NearestModelName: Optional[str] = None
    SupportedInstanceTypes: Optional[List[str]] = None
    SupportedEndpointType: Optional[RecommendationJobSupportedEndpointTypeType] = None
    DataInputConfig: Optional[str] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None


class RenderUiTemplateRequest(BaseValidatorModel):
    Task: RenderableTask
    RoleArn: str
    UiTemplate: Optional[UiTemplate] = None
    HumanTaskUiArn: Optional[str] = None


class RenderUiTemplateResponse(BaseValidatorModel):
    RenderedContent: str
    Errors: List[RenderingError]
    ResponseMetadata: ResponseMetadata


class TrainingPlanOffering(BaseValidatorModel):
    TrainingPlanOfferingId: str
    TargetResources: List[SageMakerResourceNameType]
    RequestedStartTimeAfter: Optional[datetime] = None
    RequestedEndTimeBefore: Optional[datetime] = None
    DurationHours: Optional[int] = None
    DurationMinutes: Optional[int] = None
    UpfrontFee: Optional[str] = None
    CurrencyCode: Optional[str] = None
    ReservedCapacityOfferings: Optional[List[ReservedCapacityOffering]] = None


class SelectiveExecutionConfigOutput(BaseValidatorModel):
    SelectedSteps: List[SelectedStep]
    SourcePipelineExecutionArn: Optional[str] = None


class SelectiveExecutionConfig(BaseValidatorModel):
    SelectedSteps: List[SelectedStep]
    SourcePipelineExecutionArn: Optional[str] = None


class ShadowModeConfigOutput(BaseValidatorModel):
    SourceModelVariantName: str
    ShadowModelVariants: List[ShadowModelVariantConfig]


class ShadowModeConfig(BaseValidatorModel):
    SourceModelVariantName: str
    ShadowModelVariants: List[ShadowModelVariantConfig]

SourceIpConfigUnion = Union[SourceIpConfig, SourceIpConfigOutput]


class SpaceAppLifecycleManagement(BaseValidatorModel):
    IdleSettings: Optional[SpaceIdleSettings] = None


class TrafficPatternOutput(BaseValidatorModel):
    TrafficType: Optional[TrafficTypeType] = None
    Phases: Optional[List[Phase]] = None
    Stairs: Optional[Stairs] = None


class TrafficPattern(BaseValidatorModel):
    TrafficType: Optional[TrafficTypeType] = None
    Phases: Optional[List[Phase]] = None
    Stairs: Optional[Stairs] = None


class TrainingImageConfig(BaseValidatorModel):
    TrainingRepositoryAccessMode: TrainingRepositoryAccessModeType
    TrainingRepositoryAuthConfig: Optional[TrainingRepositoryAuthConfig] = None


class TransformDataSource(BaseValidatorModel):
    S3DataSource: TransformS3DataSource


class Workforce(BaseValidatorModel):
    WorkforceName: str
    WorkforceArn: str
    LastUpdatedDate: Optional[datetime] = None
    SourceIpConfig: Optional[SourceIpConfigOutput] = None
    SubDomain: Optional[str] = None
    CognitoConfig: Optional[CognitoConfig] = None
    OidcConfig: Optional[OidcConfigForResponse] = None
    CreateDate: Optional[datetime] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigResponse] = None
    Status: Optional[WorkforceStatusType] = None
    FailureReason: Optional[str] = None


class ListActionsResponse(BaseValidatorModel):
    ActionSummaries: List[ActionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

HyperParameterAlgorithmSpecificationUnion = Union[HyperParameterAlgorithmSpecification, HyperParameterAlgorithmSpecificationOutput]


class ListAppsResponse(BaseValidatorModel):
    Apps: List[AppDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DomainSettingsOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettings] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    DockerSettings: Optional[DockerSettingsOutput] = None
    AmazonQSettings: Optional[AmazonQSettings] = None


class DomainSettings(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettings] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    DockerSettings: Optional[DockerSettings] = None
    AmazonQSettings: Optional[AmazonQSettings] = None


class CodeEditorAppSettingsOutput(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None
    LifecycleConfigArns: Optional[List[str]] = None
    AppLifecycleManagement: Optional[AppLifecycleManagement] = None
    BuiltInLifecycleConfigArn: Optional[str] = None


class CodeEditorAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None
    LifecycleConfigArns: Optional[List[str]] = None
    AppLifecycleManagement: Optional[AppLifecycleManagement] = None
    BuiltInLifecycleConfigArn: Optional[str] = None


class JupyterLabAppSettingsOutput(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepository]] = None
    AppLifecycleManagement: Optional[AppLifecycleManagement] = None
    EmrSettings: Optional[EmrSettingsOutput] = None
    BuiltInLifecycleConfigArn: Optional[str] = None


class JupyterLabAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CustomImages: Optional[List[CustomImage]] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepository]] = None
    AppLifecycleManagement: Optional[AppLifecycleManagement] = None
    EmrSettings: Optional[EmrSettings] = None
    BuiltInLifecycleConfigArn: Optional[str] = None


class ArtifactSummary(BaseValidatorModel):
    ArtifactArn: Optional[str] = None
    ArtifactName: Optional[str] = None
    Source: Optional[ArtifactSourceOutput] = None
    ArtifactType: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

ArtifactSourceUnion = Union[ArtifactSource, ArtifactSourceOutput]


class AsyncInferenceConfigOutput(BaseValidatorModel):
    OutputConfig: AsyncInferenceOutputConfigOutput
    ClientConfig: Optional[AsyncInferenceClientConfig] = None


class AsyncInferenceConfig(BaseValidatorModel):
    OutputConfig: AsyncInferenceOutputConfig
    ClientConfig: Optional[AsyncInferenceClientConfig] = None


class TabularJobConfigOutput(BaseValidatorModel):
    TargetAttributeName: str
    CandidateGenerationConfig: Optional[CandidateGenerationConfigOutput] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    FeatureSpecificationS3Uri: Optional[str] = None
    Mode: Optional[AutoMLModeType] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    ProblemType: Optional[ProblemTypeType] = None
    SampleWeightAttributeName: Optional[str] = None


class TimeSeriesForecastingJobConfigOutput(BaseValidatorModel):
    ForecastFrequency: str
    ForecastHorizon: int
    TimeSeriesConfig: TimeSeriesConfigOutput
    FeatureSpecificationS3Uri: Optional[str] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    ForecastQuantiles: Optional[List[str]] = None
    Transformations: Optional[TimeSeriesTransformationsOutput] = None
    HolidayConfig: Optional[List[HolidayConfigAttributes]] = None
    CandidateGenerationConfig: Optional[CandidateGenerationConfigOutput] = None


class TabularJobConfig(BaseValidatorModel):
    TargetAttributeName: str
    CandidateGenerationConfig: Optional[CandidateGenerationConfig] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    FeatureSpecificationS3Uri: Optional[str] = None
    Mode: Optional[AutoMLModeType] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    ProblemType: Optional[ProblemTypeType] = None
    SampleWeightAttributeName: Optional[str] = None


class TimeSeriesForecastingJobConfig(BaseValidatorModel):
    ForecastFrequency: str
    ForecastHorizon: int
    TimeSeriesConfig: TimeSeriesConfig
    FeatureSpecificationS3Uri: Optional[str] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    ForecastQuantiles: Optional[List[str]] = None
    Transformations: Optional[TimeSeriesTransformations] = None
    HolidayConfig: Optional[List[HolidayConfigAttributes]] = None
    CandidateGenerationConfig: Optional[CandidateGenerationConfig] = None


class AutoMLChannel(BaseValidatorModel):
    TargetAttributeName: str
    DataSource: Optional[AutoMLDataSource] = None
    CompressionType: Optional[CompressionTypeType] = None
    ContentType: Optional[str] = None
    ChannelType: Optional[AutoMLChannelTypeType] = None
    SampleWeightAttributeName: Optional[str] = None


class AutoMLJobChannel(BaseValidatorModel):
    ChannelType: Optional[AutoMLChannelTypeType] = None
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    DataSource: Optional[AutoMLDataSource] = None


class ListAutoMLJobsResponse(BaseValidatorModel):
    AutoMLJobSummaries: List[AutoMLJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AutoMLResolvedAttributes(BaseValidatorModel):
    AutoMLJobObjective: Optional[AutoMLJobObjective] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    AutoMLProblemTypeResolvedAttributes: Optional[AutoMLProblemTypeResolvedAttributes] = None


class AutoMLJobConfigOutput(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    SecurityConfig: Optional[AutoMLSecurityConfigOutput] = None
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfigOutput] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfig] = None
    Mode: Optional[AutoMLModeType] = None


class LabelingJobAlgorithmsConfigOutput(BaseValidatorModel):
    LabelingJobAlgorithmSpecificationArn: str
    InitialActiveLearningModelArn: Optional[str] = None
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfigOutput] = None


class AutoMLJobConfig(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria] = None
    SecurityConfig: Optional[AutoMLSecurityConfig] = None
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfig] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfig] = None
    Mode: Optional[AutoMLModeType] = None

AutoMLSecurityConfigUnion = Union[AutoMLSecurityConfig, AutoMLSecurityConfigOutput]


class LabelingJobAlgorithmsConfig(BaseValidatorModel):
    LabelingJobAlgorithmSpecificationArn: str
    InitialActiveLearningModelArn: Optional[str] = None
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfig] = None

MonitoringNetworkConfigUnion = Union[MonitoringNetworkConfig, MonitoringNetworkConfigOutput]

NetworkConfigUnion = Union[NetworkConfig, NetworkConfigOutput]


class ModelMetrics(BaseValidatorModel):
    ModelQuality: Optional[ModelQuality] = None
    ModelDataQuality: Optional[ModelDataQuality] = None
    Bias: Optional[Bias] = None
    Explainability: Optional[Explainability] = None


class PipelineExecutionStepMetadata(BaseValidatorModel):
    TrainingJob: Optional[TrainingJobStepMetadata] = None
    ProcessingJob: Optional[ProcessingJobStepMetadata] = None
    TransformJob: Optional[TransformJobStepMetadata] = None
    TuningJob: Optional[TuningJobStepMetaData] = None
    Model: Optional[ModelStepMetadata] = None
    RegisterModel: Optional[RegisterModelStepMetadata] = None
    Condition: Optional[ConditionStepMetadata] = None
    Callback: Optional[CallbackStepMetadata] = None
    Lambda: Optional[LambdaStepMetadata] = None
    EMR: Optional[EMRStepMetadata] = None
    QualityCheck: Optional[QualityCheckStepMetadata] = None
    ClarifyCheck: Optional[ClarifyCheckStepMetadata] = None
    Fail: Optional[FailStepMetadata] = None
    AutoMLJob: Optional[AutoMLJobStepMetadata] = None
    Endpoint: Optional[EndpointStepMetadata] = None
    EndpointConfig: Optional[EndpointConfigStepMetadata] = None


class AutoMLCandidate(BaseValidatorModel):
    CandidateName: str
    ObjectiveStatus: ObjectiveStatusType
    CandidateSteps: List[AutoMLCandidateStep]
    CandidateStatus: CandidateStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    FinalAutoMLJobObjectiveMetric: Optional[FinalAutoMLJobObjectiveMetric] = None
    InferenceContainers: Optional[List[AutoMLContainerDefinition]] = None
    EndTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    CandidateProperties: Optional[CandidateProperties] = None
    InferenceContainerDefinitions: Optional[Dict[AutoMLProcessingUnitType, List[AutoMLContainerDefinition]]] = None


class BlueGreenUpdatePolicy(BaseValidatorModel):
    TrafficRoutingConfiguration: TrafficRoutingConfig
    TerminationWaitInSeconds: Optional[int] = None
    MaximumExecutionTimeoutInSeconds: Optional[int] = None

InferenceExperimentDataStorageConfigUnion = Union[InferenceExperimentDataStorageConfig, InferenceExperimentDataStorageConfigOutput]

DataCaptureConfigUnion = Union[DataCaptureConfig, DataCaptureConfigOutput]


class EndpointInputConfigurationOutput(BaseValidatorModel):
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameterRanges: Optional[EnvironmentParameterRangesOutput] = None


class ParameterRanges(BaseValidatorModel):
    IntegerParameterRanges: Optional[List[IntegerParameterRange]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRange]] = None
    CategoricalParameterRanges: Optional[List[CategoricalParameterRangeUnion]] = None
    AutoParameters: Optional[List[AutoParameter]] = None


class EndpointInputConfiguration(BaseValidatorModel):
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfig] = None
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameterRanges: Optional[EnvironmentParameterRanges] = None


class ClarifyExplainerConfigOutput(BaseValidatorModel):
    ShapConfig: ClarifyShapConfig
    EnableExplanations: Optional[str] = None
    InferenceConfig: Optional[ClarifyInferenceConfigOutput] = None


class ClarifyExplainerConfig(BaseValidatorModel):
    ShapConfig: ClarifyShapConfig
    EnableExplanations: Optional[str] = None
    InferenceConfig: Optional[ClarifyInferenceConfig] = None


class ClusterInstanceGroupDetails(BaseValidatorModel):
    CurrentCount: Optional[int] = None
    TargetCount: Optional[int] = None
    InstanceGroupName: Optional[str] = None
    InstanceType: Optional[ClusterInstanceTypeType] = None
    LifeCycleConfig: Optional[ClusterLifeCycleConfig] = None
    ExecutionRole: Optional[str] = None
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[List[ClusterInstanceStorageConfig]] = None
    OnStartDeepHealthChecks: Optional[List[DeepHealthCheckTypeType]] = None
    Status: Optional[InstanceGroupStatusType] = None
    TrainingPlanArn: Optional[str] = None
    TrainingPlanStatus: Optional[str] = None
    OverrideVpcConfig: Optional[VpcConfigOutput] = None


class ClusterInstanceGroupSpecification(BaseValidatorModel):
    InstanceCount: int
    InstanceGroupName: str
    InstanceType: ClusterInstanceTypeType
    LifeCycleConfig: ClusterLifeCycleConfig
    ExecutionRole: str
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[List[ClusterInstanceStorageConfig]] = None
    OnStartDeepHealthChecks: Optional[List[DeepHealthCheckTypeType]] = None
    TrainingPlanArn: Optional[str] = None
    OverrideVpcConfig: Optional[VpcConfigUnion] = None


class ClusterNodeDetails(BaseValidatorModel):
    InstanceGroupName: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[ClusterInstanceStatusDetails] = None
    InstanceType: Optional[ClusterInstanceTypeType] = None
    LaunchTime: Optional[datetime] = None
    LifeCycleConfig: Optional[ClusterLifeCycleConfig] = None
    OverrideVpcConfig: Optional[VpcConfigOutput] = None
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[List[ClusterInstanceStorageConfig]] = None
    PrivatePrimaryIp: Optional[str] = None
    PrivatePrimaryIpv6: Optional[str] = None
    PrivateDnsHostname: Optional[str] = None
    Placement: Optional[ClusterInstancePlacement] = None


class ListClusterNodesResponse(BaseValidatorModel):
    NextToken: str
    ClusterNodeSummaries: List[ClusterNodeSummary]
    ResponseMetadata: ResponseMetadata

CodeEditorAppImageConfigUnion = Union[CodeEditorAppImageConfig, CodeEditorAppImageConfigOutput]

JupyterLabAppImageConfigUnion = Union[JupyterLabAppImageConfig, JupyterLabAppImageConfigOutput]


class ListCodeRepositoriesOutput(BaseValidatorModel):
    CodeRepositorySummaryList: List[CodeRepositorySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FeatureDefinition(BaseValidatorModel):
    FeatureName: str
    FeatureType: FeatureTypeType
    CollectionType: Optional[CollectionTypeType] = None
    CollectionConfig: Optional[CollectionConfig] = None

DebugHookConfigUnion = Union[DebugHookConfig, DebugHookConfigOutput]


class ComputeQuotaSummary(BaseValidatorModel):
    ComputeQuotaArn: str
    ComputeQuotaId: str
    Name: str
    Status: SchedulerResourceStatusType
    ComputeQuotaTarget: ComputeQuotaTarget
    CreationTime: datetime
    ComputeQuotaVersion: Optional[int] = None
    ClusterArn: Optional[str] = None
    ComputeQuotaConfig: Optional[ComputeQuotaConfigOutput] = None
    ActivationState: Optional[ActivationStateType] = None
    LastModifiedTime: Optional[datetime] = None

ComputeQuotaConfigUnion = Union[ComputeQuotaConfig, ComputeQuotaConfigOutput]


class ListContextsResponse(BaseValidatorModel):
    ContextSummaries: List[ContextSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

InferenceExperimentScheduleUnion = Union[InferenceExperimentSchedule, InferenceExperimentScheduleOutput]


class QueryLineageRequest(BaseValidatorModel):
    StartArns: Optional[List[str]] = None
    Direction: Optional[DirectionType] = None
    IncludeEdges: Optional[bool] = None
    Filters: Optional[QueryFilters] = None
    MaxDepth: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProcessingInput(BaseValidatorModel):
    InputName: str
    AppManaged: Optional[bool] = None
    S3Input: Optional[ProcessingS3Input] = None
    DatasetDefinition: Optional[DatasetDefinition] = None


class InferenceComponentSpecificationSummary(BaseValidatorModel):
    ModelName: Optional[str] = None
    Container: Optional[InferenceComponentContainerSpecificationSummary] = None
    StartupParameters: Optional[InferenceComponentStartupParameters] = None
    ComputeResourceRequirements: Optional[InferenceComponentComputeResourceRequirements] = None
    BaseInferenceComponentName: Optional[str] = None


class DescribeEdgeDeploymentPlanResponse(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    EdgeDeploymentPlanName: str
    ModelConfigs: List[EdgeDeploymentModelConfig]
    DeviceFleetName: str
    EdgeDeploymentSuccess: int
    EdgeDeploymentPending: int
    EdgeDeploymentFailed: int
    Stages: List[DeploymentStageStatusSummary]
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListExperimentsResponse(BaseValidatorModel):
    ExperimentSummaries: List[ExperimentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFeatureGroupsResponse(BaseValidatorModel):
    FeatureGroupSummaries: List[FeatureGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInferenceExperimentsResponse(BaseValidatorModel):
    InferenceExperiments: List[InferenceExperimentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrainingJobsResponse(BaseValidatorModel):
    TrainingJobSummaries: List[TrainingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrainingPlansResponse(BaseValidatorModel):
    TrainingPlanSummaries: List[TrainingPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrialsResponse(BaseValidatorModel):
    TrialSummaries: List[TrialSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateEndpointWeightsAndCapacitiesInput(BaseValidatorModel):
    EndpointName: str
    DesiredWeightsAndCapacities: List[DesiredWeightAndCapacity]


class DeploymentStage(BaseValidatorModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigUnion
    DeploymentConfig: Optional[EdgeDeploymentConfig] = None


class ListDevicesResponse(BaseValidatorModel):
    DeviceSummaries: List[DeviceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DomainSettingsForUpdate(BaseValidatorModel):
    RStudioServerProDomainSettingsForUpdate: Optional[RStudioServerProDomainSettingsForUpdate] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    SecurityGroupIds: Optional[List[str]] = None
    DockerSettings: Optional[DockerSettingsUnion] = None
    AmazonQSettings: Optional[AmazonQSettings] = None


class DriftCheckBaselines(BaseValidatorModel):
    Bias: Optional[DriftCheckBias] = None
    Explainability: Optional[DriftCheckExplainability] = None
    ModelQuality: Optional[DriftCheckModelQuality] = None
    ModelDataQuality: Optional[DriftCheckModelDataQuality] = None


class SpaceSettingsSummary(BaseValidatorModel):
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettings] = None


class InferenceRecommendation(BaseValidatorModel):
    EndpointConfiguration: EndpointOutputConfiguration
    ModelConfiguration: ModelConfiguration
    RecommendationId: Optional[str] = None
    Metrics: Optional[RecommendationMetrics] = None
    InvocationEndTime: Optional[datetime] = None
    InvocationStartTime: Optional[datetime] = None


class RecommendationJobInferenceBenchmark(BaseValidatorModel):
    ModelConfiguration: ModelConfiguration
    Metrics: Optional[RecommendationMetrics] = None
    EndpointMetrics: Optional[InferenceMetrics] = None
    EndpointConfiguration: Optional[EndpointOutputConfiguration] = None
    FailureReason: Optional[str] = None
    InvocationEndTime: Optional[datetime] = None
    InvocationStartTime: Optional[datetime] = None


class SearchExpressionPaginator(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    NestedFilters: Optional[List[NestedFilters]] = None
    SubExpressions: Optional[List[Dict[str, Any]]] = None
    Operator: Optional[BooleanOperatorType] = None


class SearchExpression(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    NestedFilters: Optional[List[NestedFilters]] = None
    SubExpressions: Optional[List[Dict[str, Any]]] = None
    Operator: Optional[BooleanOperatorType] = None


class ListTrainingJobsForHyperParameterTuningJobResponse(BaseValidatorModel):
    TrainingJobSummaries: List[HyperParameterTrainingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

HyperParameterTuningResourceConfigUnion = Union[HyperParameterTuningResourceConfig, HyperParameterTuningResourceConfigOutput]


class ListHyperParameterTuningJobsResponse(BaseValidatorModel):
    HyperParameterTuningJobSummaries: List[HyperParameterTuningJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

HyperParameterTuningJobWarmStartConfigUnion = Union[HyperParameterTuningJobWarmStartConfig, HyperParameterTuningJobWarmStartConfigOutput]


class AssociationSummary(BaseValidatorModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    SourceName: Optional[str] = None
    DestinationName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None


class DescribeActionResponse(BaseValidatorModel):
    ActionName: str
    ActionArn: str
    Source: ActionSource
    ActionType: str
    Description: str
    Status: ActionStatusType
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    MetadataProperties: MetadataProperties
    LineageGroupArn: str
    ResponseMetadata: ResponseMetadata


class DescribeArtifactResponse(BaseValidatorModel):
    ArtifactName: str
    ArtifactArn: str
    Source: ArtifactSourceOutput
    ArtifactType: str
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    MetadataProperties: MetadataProperties
    LineageGroupArn: str
    ResponseMetadata: ResponseMetadata


class DescribeComputeQuotaResponse(BaseValidatorModel):
    ComputeQuotaArn: str
    ComputeQuotaId: str
    Name: str
    Description: str
    ComputeQuotaVersion: int
    Status: SchedulerResourceStatusType
    FailureReason: str
    ClusterArn: str
    ComputeQuotaConfig: ComputeQuotaConfigOutput
    ComputeQuotaTarget: ComputeQuotaTarget
    ActivationState: ActivationStateType
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ResponseMetadata: ResponseMetadata


class DescribeContextResponse(BaseValidatorModel):
    ContextName: str
    ContextArn: str
    Source: ContextSource
    ContextType: str
    Description: str
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    LineageGroupArn: str
    ResponseMetadata: ResponseMetadata


class DescribeExperimentResponse(BaseValidatorModel):
    ExperimentName: str
    ExperimentArn: str
    DisplayName: str
    Source: ExperimentSource
    Description: str
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ResponseMetadata: ResponseMetadata


class DescribeLineageGroupResponse(BaseValidatorModel):
    LineageGroupName: str
    LineageGroupArn: str
    DisplayName: str
    Description: str
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ResponseMetadata: ResponseMetadata


class DescribeMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    TrackingServerName: str
    ArtifactStoreUri: str
    TrackingServerSize: TrackingServerSizeType
    MlflowVersion: str
    RoleArn: str
    TrackingServerStatus: TrackingServerStatusType
    IsActive: IsTrackingServerActiveType
    TrackingServerUrl: str
    WeeklyMaintenanceWindowStart: str
    AutomaticModelRegistration: bool
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ResponseMetadata: ResponseMetadata


class DescribeModelCardResponse(BaseValidatorModel):
    ModelCardArn: str
    ModelCardName: str
    ModelCardVersion: int
    Content: str
    ModelCardStatus: ModelCardStatusType
    SecurityConfig: ModelCardSecurityConfig
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ModelCardProcessingStatus: ModelCardProcessingStatusType
    ResponseMetadata: ResponseMetadata


class DescribeModelPackageGroupOutput(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    ModelPackageGroupDescription: str
    CreationTime: datetime
    CreatedBy: UserContext
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ResponseMetadata: ResponseMetadata


class DescribePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    PipelineName: str
    PipelineDisplayName: str
    PipelineDefinition: str
    PipelineDescription: str
    RoleArn: str
    PipelineStatus: PipelineStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastRunTime: datetime
    CreatedBy: UserContext
    LastModifiedBy: UserContext
    ParallelismConfiguration: ParallelismConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeTrialComponentResponse(BaseValidatorModel):
    TrialComponentName: str
    TrialComponentArn: str
    DisplayName: str
    Source: TrialComponentSource
    Status: TrialComponentStatus
    StartTime: datetime
    EndTime: datetime
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    Parameters: Dict[str, TrialComponentParameterValue]
    InputArtifacts: Dict[str, TrialComponentArtifact]
    OutputArtifacts: Dict[str, TrialComponentArtifact]
    MetadataProperties: MetadataProperties
    Metrics: List[TrialComponentMetricSummary]
    LineageGroupArn: str
    Sources: List[TrialComponentSource]
    ResponseMetadata: ResponseMetadata


class DescribeTrialResponse(BaseValidatorModel):
    TrialName: str
    TrialArn: str
    DisplayName: str
    ExperimentName: str
    Source: TrialSource
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    MetadataProperties: MetadataProperties
    ResponseMetadata: ResponseMetadata


class Experiment(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    ExperimentArn: Optional[str] = None
    DisplayName: Optional[str] = None
    Source: Optional[ExperimentSource] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None
    Tags: Optional[List[Tag]] = None


class ModelCard(BaseValidatorModel):
    ModelCardArn: Optional[str] = None
    ModelCardName: Optional[str] = None
    ModelCardVersion: Optional[int] = None
    Content: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SecurityConfig: Optional[ModelCardSecurityConfig] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None
    Tags: Optional[List[Tag]] = None
    ModelId: Optional[str] = None
    RiskRating: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None


class ModelDashboardModelCard(BaseValidatorModel):
    ModelCardArn: Optional[str] = None
    ModelCardName: Optional[str] = None
    ModelCardVersion: Optional[int] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SecurityConfig: Optional[ModelCardSecurityConfig] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None
    Tags: Optional[List[Tag]] = None
    ModelId: Optional[str] = None
    RiskRating: Optional[str] = None


class ModelPackageGroup(BaseValidatorModel):
    ModelPackageGroupName: Optional[str] = None
    ModelPackageGroupArn: Optional[str] = None
    ModelPackageGroupDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    ModelPackageGroupStatus: Optional[ModelPackageGroupStatusType] = None
    Tags: Optional[List[Tag]] = None


class Pipeline(BaseValidatorModel):
    PipelineArn: Optional[str] = None
    PipelineName: Optional[str] = None
    PipelineDisplayName: Optional[str] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    PipelineStatus: Optional[PipelineStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastRunTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedBy: Optional[UserContext] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None
    Tags: Optional[List[Tag]] = None


class TrialComponentSimpleSummary(BaseValidatorModel):
    TrialComponentName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    TrialComponentSource: Optional[TrialComponentSource] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None


class TrialComponentSummary(BaseValidatorModel):
    TrialComponentName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialComponentSource: Optional[TrialComponentSource] = None
    Status: Optional[TrialComponentStatus] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None


class WorkerAccessConfiguration(BaseValidatorModel):
    S3Presign: Optional[S3Presign] = None


class InferenceComponentDeploymentConfigOutput(BaseValidatorModel):
    RollingUpdatePolicy: InferenceComponentRollingUpdatePolicy
    AutoRollbackConfiguration: Optional[AutoRollbackConfigOutput] = None


class InferenceComponentDeploymentConfig(BaseValidatorModel):
    RollingUpdatePolicy: InferenceComponentRollingUpdatePolicy
    AutoRollbackConfiguration: Optional[AutoRollbackConfig] = None


class CreateInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str
    EndpointName: str
    Specification: InferenceComponentSpecification
    VariantName: Optional[str] = None
    RuntimeConfig: Optional[InferenceComponentRuntimeConfig] = None
    Tags: Optional[List[Tag]] = None

ResourceConfigUnion = Union[ResourceConfig, ResourceConfigOutput]


class HyperParameterSpecificationOutput(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    Description: Optional[str] = None
    Range: Optional[ParameterRangeOutput] = None
    IsTunable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    DefaultValue: Optional[str] = None


class HyperParameterSpecification(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    Description: Optional[str] = None
    Range: Optional[ParameterRange] = None
    IsTunable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    DefaultValue: Optional[str] = None


class HyperParameterTuningJobConfigOutput(BaseValidatorModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimits
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfig] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjective] = None
    ParameterRanges: Optional[ParameterRangesOutput] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteria] = None
    RandomSeed: Optional[int] = None


class AppImageConfigDetails(BaseValidatorModel):
    AppImageConfigArn: Optional[str] = None
    AppImageConfigName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigOutput] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigOutput] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigOutput] = None


class DescribeAppImageConfigResponse(BaseValidatorModel):
    AppImageConfigArn: str
    AppImageConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    KernelGatewayImageConfig: KernelGatewayImageConfigOutput
    JupyterLabAppImageConfig: JupyterLabAppImageConfigOutput
    CodeEditorAppImageConfig: CodeEditorAppImageConfigOutput
    ResponseMetadata: ResponseMetadata

KernelGatewayImageConfigUnion = Union[KernelGatewayImageConfig, KernelGatewayImageConfigOutput]


class ListLabelingJobsForWorkteamResponse(BaseValidatorModel):
    LabelingJobSummaryList: List[LabelingJobForWorkteamSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LabelingJobInputConfigOutput(BaseValidatorModel):
    DataSource: LabelingJobDataSource
    DataAttributes: Optional[LabelingJobDataAttributesOutput] = None


class LabelingJobInputConfig(BaseValidatorModel):
    DataSource: LabelingJobDataSource
    DataAttributes: Optional[LabelingJobDataAttributes] = None


class TargetTrackingScalingPolicyConfiguration(BaseValidatorModel):
    MetricSpecification: Optional[MetricSpecification] = None
    TargetValue: Optional[float] = None


class DataSourceOutput(BaseValidatorModel):
    S3DataSource: Optional[S3DataSourceOutput] = None
    FileSystemDataSource: Optional[FileSystemDataSource] = None

S3DataSourceUnion = Union[S3DataSource, S3DataSourceOutput]


class AdditionalModelDataSource(BaseValidatorModel):
    ChannelName: str
    S3DataSource: S3ModelDataSource


class ModelDataSource(BaseValidatorModel):
    S3DataSource: Optional[S3ModelDataSource] = None


class MonitoringAlertSummary(BaseValidatorModel):
    MonitoringAlertName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    AlertStatus: MonitoringAlertStatusType
    DatapointsToAlert: int
    EvaluationPeriod: int
    Actions: MonitoringAlertActions


class ModelVariantConfigSummary(BaseValidatorModel):
    ModelName: str
    VariantName: str
    InfrastructureConfig: ModelInfrastructureConfig
    Status: ModelVariantStatusType


class ModelVariantConfig(BaseValidatorModel):
    ModelName: str
    VariantName: str
    InfrastructureConfig: ModelInfrastructureConfig

RecommendationJobStoppingConditionsUnion = Union[RecommendationJobStoppingConditions, RecommendationJobStoppingConditionsOutput]


class ListModelMetadataRequestPaginate(BaseValidatorModel):
    SearchExpression: Optional[ModelMetadataSearchExpression] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelMetadataRequest(BaseValidatorModel):
    SearchExpression: Optional[ModelMetadataSearchExpression] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OptimizationConfig(BaseValidatorModel):
    ModelQuantizationConfig: Optional[ModelQuantizationConfigUnion] = None
    ModelCompilationConfig: Optional[ModelCompilationConfigUnion] = None
    ModelShardingConfig: Optional[ModelShardingConfigUnion] = None


class BatchTransformInputOutput(BaseValidatorModel):
    DataCapturedDestinationS3Uri: str
    DatasetFormat: MonitoringDatasetFormatOutput
    LocalPath: str
    S3InputMode: Optional[ProcessingS3InputModeType] = None
    S3DataDistributionType: Optional[ProcessingS3DataDistributionTypeType] = None
    FeaturesAttribute: Optional[str] = None
    InferenceAttribute: Optional[str] = None
    ProbabilityAttribute: Optional[str] = None
    ProbabilityThresholdAttribute: Optional[float] = None
    StartTimeOffset: Optional[str] = None
    EndTimeOffset: Optional[str] = None
    ExcludeFeaturesAttribute: Optional[str] = None


class BatchTransformInput(BaseValidatorModel):
    DataCapturedDestinationS3Uri: str
    DatasetFormat: MonitoringDatasetFormat
    LocalPath: str
    S3InputMode: Optional[ProcessingS3InputModeType] = None
    S3DataDistributionType: Optional[ProcessingS3DataDistributionTypeType] = None
    FeaturesAttribute: Optional[str] = None
    InferenceAttribute: Optional[str] = None
    ProbabilityAttribute: Optional[str] = None
    ProbabilityThresholdAttribute: Optional[float] = None
    StartTimeOffset: Optional[str] = None
    EndTimeOffset: Optional[str] = None
    ExcludeFeaturesAttribute: Optional[str] = None


class MonitoringOutputConfigOutput(BaseValidatorModel):
    MonitoringOutputs: List[MonitoringOutput]
    KmsKeyId: Optional[str] = None


class MonitoringOutputConfig(BaseValidatorModel):
    MonitoringOutputs: List[MonitoringOutput]
    KmsKeyId: Optional[str] = None


class MemberDefinition(BaseValidatorModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinition] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionUnion] = None


class OptimizationJobModelSource(BaseValidatorModel):
    S3: Optional[OptimizationJobModelSourceS3] = None


class CreateCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str
    RoleArn: str
    OutputConfig: OutputConfig
    StoppingCondition: StoppingCondition
    ModelPackageVersionArn: Optional[str] = None
    InputConfig: Optional[InputConfig] = None
    VpcConfig: Optional[NeoVpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


class DescribeCompilationJobResponse(BaseValidatorModel):
    CompilationJobName: str
    CompilationJobArn: str
    CompilationJobStatus: CompilationJobStatusType
    CompilationStartTime: datetime
    CompilationEndTime: datetime
    StoppingCondition: StoppingCondition
    InferenceImage: str
    ModelPackageVersionArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    ModelArtifacts: ModelArtifacts
    ModelDigests: ModelDigests
    RoleArn: str
    InputConfig: InputConfig
    OutputConfig: OutputConfig
    VpcConfig: NeoVpcConfigOutput
    DerivedInformation: DerivedInformation
    ResponseMetadata: ResponseMetadata


class CreatePartnerAppRequest(BaseValidatorModel):
    Name: str
    Type: PartnerAppTypeType
    ExecutionRoleArn: str
    Tier: str
    AuthType: Literal['IAM']
    MaintenanceConfig: Optional[PartnerAppMaintenanceConfig] = None
    ApplicationConfig: Optional[PartnerAppConfigUnion] = None
    EnableIamSessionBasedIdentity: Optional[bool] = None
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdatePartnerAppRequest(BaseValidatorModel):
    Arn: str
    MaintenanceConfig: Optional[PartnerAppMaintenanceConfig] = None
    Tier: Optional[str] = None
    ApplicationConfig: Optional[PartnerAppConfigUnion] = None
    EnableIamSessionBasedIdentity: Optional[bool] = None
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class PendingDeploymentSummary(BaseValidatorModel):
    EndpointConfigName: str
    ProductionVariants: Optional[List[PendingProductionVariantSummary]] = None
    StartTime: Optional[datetime] = None
    ShadowProductionVariants: Optional[List[PendingProductionVariantSummary]] = None


class DescribeClusterSchedulerConfigResponse(BaseValidatorModel):
    ClusterSchedulerConfigArn: str
    ClusterSchedulerConfigId: str
    Name: str
    ClusterSchedulerConfigVersion: int
    Status: SchedulerResourceStatusType
    FailureReason: str
    ClusterArn: str
    SchedulerConfig: SchedulerConfigOutput
    Description: str
    CreationTime: datetime
    CreatedBy: UserContext
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ResponseMetadata: ResponseMetadata

SchedulerConfigUnion = Union[SchedulerConfig, SchedulerConfigOutput]


class ProcessingOutputConfigOutput(BaseValidatorModel):
    Outputs: List[ProcessingOutput]
    KmsKeyId: Optional[str] = None


class ProcessingOutputConfig(BaseValidatorModel):
    Outputs: List[ProcessingOutput]
    KmsKeyId: Optional[str] = None


class UpdateTrainingJobRequest(BaseValidatorModel):
    TrainingJobName: str
    ProfilerConfig: Optional[ProfilerConfigForUpdate] = None
    ProfilerRuleConfigurations: Optional[List[ProfilerRuleConfigurationUnion]] = None
    ResourceConfig: Optional[ResourceConfigForUpdate] = None
    RemoteDebugConfig: Optional[RemoteDebugConfigForUpdate] = None


class GetSearchSuggestionsRequest(BaseValidatorModel):
    Resource: ResourceTypeType
    SuggestionQuery: Optional[SuggestionQuery] = None


class DescribeProjectOutput(BaseValidatorModel):
    ProjectArn: str
    ProjectName: str
    ProjectId: str
    ProjectDescription: str
    ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsOutput
    ServiceCatalogProvisionedProductDetails: ServiceCatalogProvisionedProductDetails
    ProjectStatus: ProjectStatusType
    CreatedBy: UserContext
    CreationTime: datetime
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ResponseMetadata: ResponseMetadata


class Project(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    ProjectId: Optional[str] = None
    ProjectDescription: Optional[str] = None
    ServiceCatalogProvisioningDetails: Optional[ServiceCatalogProvisioningDetailsOutput] = None
    ServiceCatalogProvisionedProductDetails: Optional[ServiceCatalogProvisionedProductDetails] = None
    ProjectStatus: Optional[ProjectStatusType] = None
    CreatedBy: Optional[UserContext] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None

ServiceCatalogProvisioningDetailsUnion = Union[ServiceCatalogProvisioningDetails, ServiceCatalogProvisioningDetailsOutput]


class UpdateProjectInput(BaseValidatorModel):
    ProjectName: str
    ProjectDescription: Optional[str] = None
    ServiceCatalogProvisioningUpdateDetails: Optional[ServiceCatalogProvisioningUpdateDetails] = None
    Tags: Optional[List[Tag]] = None


class HumanLoopConfigOutput(BaseValidatorModel):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    TaskTimeLimitInSeconds: Optional[int] = None
    TaskKeywords: Optional[List[str]] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPrice] = None


class HumanLoopConfig(BaseValidatorModel):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    TaskTimeLimitInSeconds: Optional[int] = None
    TaskKeywords: Optional[List[str]] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPrice] = None


class HumanTaskConfigOutput(BaseValidatorModel):
    WorkteamArn: str
    UiConfig: UiConfig
    TaskTitle: str
    TaskDescription: str
    NumberOfHumanWorkersPerDataObject: int
    TaskTimeLimitInSeconds: int
    PreHumanTaskLambdaArn: Optional[str] = None
    TaskKeywords: Optional[List[str]] = None
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    MaxConcurrentTaskCount: Optional[int] = None
    AnnotationConsolidationConfig: Optional[AnnotationConsolidationConfig] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPrice] = None


class HumanTaskConfig(BaseValidatorModel):
    WorkteamArn: str
    UiConfig: UiConfig
    TaskTitle: str
    TaskDescription: str
    NumberOfHumanWorkersPerDataObject: int
    TaskTimeLimitInSeconds: int
    PreHumanTaskLambdaArn: Optional[str] = None
    TaskKeywords: Optional[List[str]] = None
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    MaxConcurrentTaskCount: Optional[int] = None
    AnnotationConsolidationConfig: Optional[AnnotationConsolidationConfig] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPrice] = None


class SearchTrainingPlanOfferingsResponse(BaseValidatorModel):
    TrainingPlanOfferings: List[TrainingPlanOffering]
    ResponseMetadata: ResponseMetadata


class DescribePipelineExecutionResponse(BaseValidatorModel):
    PipelineArn: str
    PipelineExecutionArn: str
    PipelineExecutionDisplayName: str
    PipelineExecutionStatus: PipelineExecutionStatusType
    PipelineExecutionDescription: str
    PipelineExperimentConfig: PipelineExperimentConfig
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    CreatedBy: UserContext
    LastModifiedBy: UserContext
    ParallelismConfiguration: ParallelismConfiguration
    SelectiveExecutionConfig: SelectiveExecutionConfigOutput
    ResponseMetadata: ResponseMetadata


class PipelineExecution(BaseValidatorModel):
    PipelineArn: Optional[str] = None
    PipelineExecutionArn: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineExecutionStatus: Optional[PipelineExecutionStatusType] = None
    PipelineExecutionDescription: Optional[str] = None
    PipelineExperimentConfig: Optional[PipelineExperimentConfig] = None
    FailureReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedBy: Optional[UserContext] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfigOutput] = None
    PipelineParameters: Optional[List[Parameter]] = None

SelectiveExecutionConfigUnion = Union[SelectiveExecutionConfig, SelectiveExecutionConfigOutput]

ShadowModeConfigUnion = Union[ShadowModeConfig, ShadowModeConfigOutput]


class CreateWorkforceRequest(BaseValidatorModel):
    WorkforceName: str
    CognitoConfig: Optional[CognitoConfig] = None
    OidcConfig: Optional[OidcConfig] = None
    SourceIpConfig: Optional[SourceIpConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequest] = None


class UpdateWorkforceRequest(BaseValidatorModel):
    WorkforceName: str
    SourceIpConfig: Optional[SourceIpConfigUnion] = None
    OidcConfig: Optional[OidcConfig] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequest] = None


class SpaceCodeEditorAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    AppLifecycleManagement: Optional[SpaceAppLifecycleManagement] = None


class SpaceJupyterLabAppSettingsOutput(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CodeRepositories: Optional[List[CodeRepository]] = None
    AppLifecycleManagement: Optional[SpaceAppLifecycleManagement] = None


class SpaceJupyterLabAppSettings(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpec] = None
    CodeRepositories: Optional[List[CodeRepository]] = None
    AppLifecycleManagement: Optional[SpaceAppLifecycleManagement] = None


class AlgorithmSpecificationOutput(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinition]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfig] = None


class AlgorithmSpecification(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinition]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfig] = None


class TransformInput(BaseValidatorModel):
    DataSource: TransformDataSource
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    SplitType: Optional[SplitTypeType] = None


class DescribeWorkforceResponse(BaseValidatorModel):
    Workforce: Workforce
    ResponseMetadata: ResponseMetadata


class ListWorkforcesResponse(BaseValidatorModel):
    Workforces: List[Workforce]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateWorkforceResponse(BaseValidatorModel):
    Workforce: Workforce
    ResponseMetadata: ResponseMetadata

DomainSettingsUnion = Union[DomainSettings, DomainSettingsOutput]


class DefaultSpaceSettingsOutput(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutput] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutput] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsOutput] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettings] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfig] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfig]] = None


class UserSettingsOutput(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SharingSettings: Optional[SharingSettings] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutput] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutput] = None
    TensorBoardAppSettings: Optional[TensorBoardAppSettings] = None
    RStudioServerProAppSettings: Optional[RStudioServerProAppSettings] = None
    RSessionAppSettings: Optional[RSessionAppSettingsOutput] = None
    CanvasAppSettings: Optional[CanvasAppSettingsOutput] = None
    CodeEditorAppSettings: Optional[CodeEditorAppSettingsOutput] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsOutput] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettings] = None
    DefaultLandingUri: Optional[str] = None
    StudioWebPortal: Optional[StudioWebPortalType] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfig] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfig]] = None
    StudioWebPortalSettings: Optional[StudioWebPortalSettingsOutput] = None
    AutoMountHomeEFS: Optional[AutoMountHomeEFSType] = None


class DefaultSpaceSettings(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettings] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettings] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettings] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettings] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfig] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfig]] = None


class UserSettings(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SharingSettings: Optional[SharingSettings] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettings] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettings] = None
    TensorBoardAppSettings: Optional[TensorBoardAppSettings] = None
    RStudioServerProAppSettings: Optional[RStudioServerProAppSettings] = None
    RSessionAppSettings: Optional[RSessionAppSettings] = None
    CanvasAppSettings: Optional[CanvasAppSettings] = None
    CodeEditorAppSettings: Optional[CodeEditorAppSettings] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettings] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettings] = None
    DefaultLandingUri: Optional[str] = None
    StudioWebPortal: Optional[StudioWebPortalType] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfig] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfig]] = None
    StudioWebPortalSettings: Optional[StudioWebPortalSettings] = None
    AutoMountHomeEFS: Optional[AutoMountHomeEFSType] = None


class ListArtifactsResponse(BaseValidatorModel):
    ArtifactSummaries: List[ArtifactSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateArtifactRequest(BaseValidatorModel):
    Source: ArtifactSourceUnion
    ArtifactType: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


class DeleteArtifactRequest(BaseValidatorModel):
    ArtifactArn: Optional[str] = None
    Source: Optional[ArtifactSourceUnion] = None

AsyncInferenceConfigUnion = Union[AsyncInferenceConfig, AsyncInferenceConfigOutput]


class AutoMLProblemTypeConfigOutput(BaseValidatorModel):
    ImageClassificationJobConfig: Optional[ImageClassificationJobConfig] = None
    TextClassificationJobConfig: Optional[TextClassificationJobConfig] = None
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfigOutput] = None
    TabularJobConfig: Optional[TabularJobConfigOutput] = None
    TextGenerationJobConfig: Optional[TextGenerationJobConfigOutput] = None


class AutoMLProblemTypeConfig(BaseValidatorModel):
    ImageClassificationJobConfig: Optional[ImageClassificationJobConfig] = None
    TextClassificationJobConfig: Optional[TextClassificationJobConfig] = None
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfig] = None
    TabularJobConfig: Optional[TabularJobConfig] = None
    TextGenerationJobConfig: Optional[TextGenerationJobConfig] = None

AutoMLJobConfigUnion = Union[AutoMLJobConfig, AutoMLJobConfigOutput]

LabelingJobAlgorithmsConfigUnion = Union[LabelingJobAlgorithmsConfig, LabelingJobAlgorithmsConfigOutput]


class PipelineExecutionStep(BaseValidatorModel):
    StepName: Optional[str] = None
    StepDisplayName: Optional[str] = None
    StepDescription: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    StepStatus: Optional[StepStatusType] = None
    CacheHitResult: Optional[CacheHitResult] = None
    FailureReason: Optional[str] = None
    Metadata: Optional[PipelineExecutionStepMetadata] = None
    AttemptCount: Optional[int] = None
    SelectiveExecutionResult: Optional[SelectiveExecutionResult] = None


class DescribeAutoMLJobResponse(BaseValidatorModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    InputDataConfig: List[AutoMLChannel]
    OutputDataConfig: AutoMLOutputDataConfig
    RoleArn: str
    AutoMLJobObjective: AutoMLJobObjective
    ProblemType: ProblemTypeType
    AutoMLJobConfig: AutoMLJobConfigOutput
    CreationTime: datetime
    EndTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    PartialFailureReasons: List[AutoMLPartialFailureReason]
    BestCandidate: AutoMLCandidate
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    GenerateCandidateDefinitionsOnly: bool
    AutoMLJobArtifacts: AutoMLJobArtifacts
    ResolvedAttributes: ResolvedAttributes
    ModelDeployConfig: ModelDeployConfig
    ModelDeployResult: ModelDeployResult
    ResponseMetadata: ResponseMetadata


class ListCandidatesForAutoMLJobResponse(BaseValidatorModel):
    Candidates: List[AutoMLCandidate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeploymentConfigOutput(BaseValidatorModel):
    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicy] = None
    RollingUpdatePolicy: Optional[RollingUpdatePolicy] = None
    AutoRollbackConfiguration: Optional[AutoRollbackConfigOutput] = None


class DeploymentConfig(BaseValidatorModel):
    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicy] = None
    RollingUpdatePolicy: Optional[RollingUpdatePolicy] = None
    AutoRollbackConfiguration: Optional[AutoRollbackConfig] = None


class RecommendationJobInputConfigOutput(BaseValidatorModel):
    ModelPackageVersionArn: Optional[str] = None
    ModelName: Optional[str] = None
    JobDurationInSeconds: Optional[int] = None
    TrafficPattern: Optional[TrafficPatternOutput] = None
    ResourceLimit: Optional[RecommendationJobResourceLimit] = None
    EndpointConfigurations: Optional[List[EndpointInputConfigurationOutput]] = None
    VolumeKmsKeyId: Optional[str] = None
    ContainerConfig: Optional[RecommendationJobContainerConfigOutput] = None
    Endpoints: Optional[List[EndpointInfo]] = None
    VpcConfig: Optional[RecommendationJobVpcConfigOutput] = None


class HyperParameterTuningJobConfig(BaseValidatorModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimits
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfig] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjective] = None
    ParameterRanges: Optional[ParameterRanges] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteria] = None
    RandomSeed: Optional[int] = None

ParameterRangesUnion = Union[ParameterRanges, ParameterRangesOutput]


class RecommendationJobInputConfig(BaseValidatorModel):
    ModelPackageVersionArn: Optional[str] = None
    ModelName: Optional[str] = None
    JobDurationInSeconds: Optional[int] = None
    TrafficPattern: Optional[TrafficPattern] = None
    ResourceLimit: Optional[RecommendationJobResourceLimit] = None
    EndpointConfigurations: Optional[List[EndpointInputConfiguration]] = None
    VolumeKmsKeyId: Optional[str] = None
    ContainerConfig: Optional[RecommendationJobContainerConfig] = None
    Endpoints: Optional[List[EndpointInfo]] = None
    VpcConfig: Optional[RecommendationJobVpcConfig] = None


class ExplainerConfigOutput(BaseValidatorModel):
    ClarifyExplainerConfig: Optional[ClarifyExplainerConfigOutput] = None


class ExplainerConfig(BaseValidatorModel):
    ClarifyExplainerConfig: Optional[ClarifyExplainerConfig] = None


class DescribeClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    ClusterStatus: ClusterStatusType
    CreationTime: datetime
    FailureMessage: str
    InstanceGroups: List[ClusterInstanceGroupDetails]
    VpcConfig: VpcConfigOutput
    Orchestrator: ClusterOrchestrator
    NodeRecovery: ClusterNodeRecoveryType
    ResponseMetadata: ResponseMetadata


class CreateClusterRequest(BaseValidatorModel):
    ClusterName: str
    InstanceGroups: List[ClusterInstanceGroupSpecification]
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    Orchestrator: Optional[ClusterOrchestrator] = None
    NodeRecovery: Optional[ClusterNodeRecoveryType] = None


class UpdateClusterRequest(BaseValidatorModel):
    ClusterName: str
    InstanceGroups: List[ClusterInstanceGroupSpecification]
    NodeRecovery: Optional[ClusterNodeRecoveryType] = None
    InstanceGroupsToDelete: Optional[List[str]] = None


class DescribeClusterNodeResponse(BaseValidatorModel):
    NodeDetails: ClusterNodeDetails
    ResponseMetadata: ResponseMetadata


class CreateFeatureGroupRequest(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierFeatureName: str
    EventTimeFeatureName: str
    FeatureDefinitions: List[FeatureDefinition]
    OnlineStoreConfig: Optional[OnlineStoreConfig] = None
    OfflineStoreConfig: Optional[OfflineStoreConfig] = None
    ThroughputConfig: Optional[ThroughputConfig] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DescribeFeatureGroupResponse(BaseValidatorModel):
    FeatureGroupArn: str
    FeatureGroupName: str
    RecordIdentifierFeatureName: str
    EventTimeFeatureName: str
    FeatureDefinitions: List[FeatureDefinition]
    CreationTime: datetime
    LastModifiedTime: datetime
    OnlineStoreConfig: OnlineStoreConfig
    OfflineStoreConfig: OfflineStoreConfig
    ThroughputConfig: ThroughputConfigDescription
    RoleArn: str
    FeatureGroupStatus: FeatureGroupStatusType
    OfflineStoreStatus: OfflineStoreStatus
    LastUpdateStatus: LastUpdateStatus
    FailureReason: str
    Description: str
    NextToken: str
    OnlineStoreTotalSizeBytes: int
    ResponseMetadata: ResponseMetadata


class FeatureGroup(BaseValidatorModel):
    FeatureGroupArn: Optional[str] = None
    FeatureGroupName: Optional[str] = None
    RecordIdentifierFeatureName: Optional[str] = None
    EventTimeFeatureName: Optional[str] = None
    FeatureDefinitions: Optional[List[FeatureDefinition]] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    OnlineStoreConfig: Optional[OnlineStoreConfig] = None
    OfflineStoreConfig: Optional[OfflineStoreConfig] = None
    RoleArn: Optional[str] = None
    FeatureGroupStatus: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatus: Optional[OfflineStoreStatus] = None
    LastUpdateStatus: Optional[LastUpdateStatus] = None
    FailureReason: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateFeatureGroupRequest(BaseValidatorModel):
    FeatureGroupName: str
    FeatureAdditions: Optional[List[FeatureDefinition]] = None
    OnlineStoreConfig: Optional[OnlineStoreConfigUpdate] = None
    ThroughputConfig: Optional[ThroughputConfigUpdate] = None


class ListComputeQuotasResponse(BaseValidatorModel):
    ComputeQuotaSummaries: List[ComputeQuotaSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateComputeQuotaRequest(BaseValidatorModel):
    Name: str
    ClusterArn: str
    ComputeQuotaConfig: ComputeQuotaConfigUnion
    ComputeQuotaTarget: ComputeQuotaTarget
    Description: Optional[str] = None
    ActivationState: Optional[ActivationStateType] = None
    Tags: Optional[List[Tag]] = None


class UpdateComputeQuotaRequest(BaseValidatorModel):
    ComputeQuotaId: str
    TargetVersion: int
    ComputeQuotaConfig: Optional[ComputeQuotaConfigUnion] = None
    ComputeQuotaTarget: Optional[ComputeQuotaTarget] = None
    ActivationState: Optional[ActivationStateType] = None
    Description: Optional[str] = None


class CreateEdgeDeploymentPlanRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    ModelConfigs: List[EdgeDeploymentModelConfig]
    DeviceFleetName: str
    Stages: Optional[List[DeploymentStage]] = None
    Tags: Optional[List[Tag]] = None


class CreateEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    Stages: List[DeploymentStage]


class SpaceDetails(BaseValidatorModel):
    DomainId: Optional[str] = None
    SpaceName: Optional[str] = None
    Status: Optional[SpaceStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    SpaceSettingsSummary: Optional[SpaceSettingsSummary] = None
    SpaceSharingSettingsSummary: Optional[SpaceSharingSettingsSummary] = None
    OwnershipSettingsSummary: Optional[OwnershipSettingsSummary] = None
    SpaceDisplayName: Optional[str] = None


class InferenceRecommendationsJobStep(BaseValidatorModel):
    StepType: Literal['BENCHMARK']
    JobName: str
    Status: RecommendationJobStatusType
    InferenceBenchmark: Optional[RecommendationJobInferenceBenchmark] = None


class SearchRequestPaginate(BaseValidatorModel):
    Resource: ResourceTypeType
    SearchExpression: Optional[SearchExpressionPaginator] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[List[VisibilityConditions]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchRequest(BaseValidatorModel):
    Resource: ResourceTypeType
    SearchExpression: Optional[SearchExpression] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[List[VisibilityConditions]] = None


class ListAssociationsResponse(BaseValidatorModel):
    AssociationSummaries: List[AssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Trial(BaseValidatorModel):
    TrialName: Optional[str] = None
    TrialArn: Optional[str] = None
    DisplayName: Optional[str] = None
    ExperimentName: Optional[str] = None
    Source: Optional[TrialSource] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None
    TrialComponentSummaries: Optional[List[TrialComponentSimpleSummary]] = None


class ListTrialComponentsResponse(BaseValidatorModel):
    TrialComponentSummaries: List[TrialComponentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Workteam(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: List[MemberDefinitionOutput]
    WorkteamArn: str
    Description: str
    WorkforceArn: Optional[str] = None
    ProductListingIds: Optional[List[str]] = None
    SubDomain: Optional[str] = None
    CreateDate: Optional[datetime] = None
    LastUpdatedDate: Optional[datetime] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration] = None


class DescribeInferenceComponentOutput(BaseValidatorModel):
    InferenceComponentName: str
    InferenceComponentArn: str
    EndpointName: str
    EndpointArn: str
    VariantName: str
    FailureReason: str
    Specification: InferenceComponentSpecificationSummary
    RuntimeConfig: InferenceComponentRuntimeConfigSummary
    CreationTime: datetime
    LastModifiedTime: datetime
    InferenceComponentStatus: InferenceComponentStatusType
    LastDeploymentConfig: InferenceComponentDeploymentConfigOutput
    ResponseMetadata: ResponseMetadata

InferenceComponentDeploymentConfigUnion = Union[InferenceComponentDeploymentConfig, InferenceComponentDeploymentConfigOutput]


class TrainingSpecificationOutput(BaseValidatorModel):
    TrainingImage: str
    SupportedTrainingInstanceTypes: List[TrainingInstanceTypeType]
    TrainingChannels: List[ChannelSpecificationOutput]
    TrainingImageDigest: Optional[str] = None
    SupportedHyperParameters: Optional[List[HyperParameterSpecificationOutput]] = None
    SupportsDistributedTraining: Optional[bool] = None
    MetricDefinitions: Optional[List[MetricDefinition]] = None
    SupportedTuningJobObjectiveMetrics: Optional[List[HyperParameterTuningJobObjective]] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSource] = None


class TrainingSpecification(BaseValidatorModel):
    TrainingImage: str
    SupportedTrainingInstanceTypes: List[TrainingInstanceTypeType]
    TrainingChannels: List[ChannelSpecification]
    TrainingImageDigest: Optional[str] = None
    SupportedHyperParameters: Optional[List[HyperParameterSpecification]] = None
    SupportsDistributedTraining: Optional[bool] = None
    MetricDefinitions: Optional[List[MetricDefinition]] = None
    SupportedTuningJobObjectiveMetrics: Optional[List[HyperParameterTuningJobObjective]] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSource] = None


class ListAppImageConfigsResponse(BaseValidatorModel):
    AppImageConfigs: List[AppImageConfigDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str
    Tags: Optional[List[Tag]] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigUnion] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigUnion] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigUnion] = None


class UpdateAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigUnion] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigUnion] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigUnion] = None


class LabelingJobSummary(BaseValidatorModel):
    LabelingJobName: str
    LabelingJobArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LabelingJobStatus: LabelingJobStatusType
    LabelCounters: LabelCounters
    WorkteamArn: str
    PreHumanTaskLambdaArn: Optional[str] = None
    AnnotationConsolidationLambdaArn: Optional[str] = None
    FailureReason: Optional[str] = None
    LabelingJobOutput: Optional[LabelingJobOutput] = None
    InputConfig: Optional[LabelingJobInputConfigOutput] = None

LabelingJobInputConfigUnion = Union[LabelingJobInputConfig, LabelingJobInputConfigOutput]


class ScalingPolicy(BaseValidatorModel):
    TargetTracking: Optional[TargetTrackingScalingPolicyConfiguration] = None


class ChannelOutput(BaseValidatorModel):
    ChannelName: str
    DataSource: DataSourceOutput
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfig] = None


class DataSource(BaseValidatorModel):
    S3DataSource: Optional[S3DataSourceUnion] = None
    FileSystemDataSource: Optional[FileSystemDataSource] = None


class ContainerDefinitionOutput(BaseValidatorModel):
    ContainerHostname: Optional[str] = None
    Image: Optional[str] = None
    ImageConfig: Optional[ImageConfig] = None
    Mode: Optional[ContainerModeType] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSource] = None
    AdditionalModelDataSources: Optional[List[AdditionalModelDataSource]] = None
    Environment: Optional[Dict[str, str]] = None
    ModelPackageName: Optional[str] = None
    InferenceSpecificationName: Optional[str] = None
    MultiModelConfig: Optional[MultiModelConfig] = None


class ContainerDefinition(BaseValidatorModel):
    ContainerHostname: Optional[str] = None
    Image: Optional[str] = None
    ImageConfig: Optional[ImageConfig] = None
    Mode: Optional[ContainerModeType] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSource] = None
    AdditionalModelDataSources: Optional[List[AdditionalModelDataSource]] = None
    Environment: Optional[Dict[str, str]] = None
    ModelPackageName: Optional[str] = None
    InferenceSpecificationName: Optional[str] = None
    MultiModelConfig: Optional[MultiModelConfig] = None


class ModelPackageContainerDefinitionOutput(BaseValidatorModel):
    Image: str
    ContainerHostname: Optional[str] = None
    ImageDigest: Optional[str] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSource] = None
    ProductId: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None
    ModelInput: Optional[ModelInput] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    NearestModelName: Optional[str] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSource] = None
    ModelDataETag: Optional[str] = None


class ModelPackageContainerDefinition(BaseValidatorModel):
    Image: str
    ContainerHostname: Optional[str] = None
    ImageDigest: Optional[str] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSource] = None
    ProductId: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None
    ModelInput: Optional[ModelInput] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    NearestModelName: Optional[str] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSource] = None
    ModelDataETag: Optional[str] = None


class SourceAlgorithm(BaseValidatorModel):
    AlgorithmName: str
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSource] = None
    ModelDataETag: Optional[str] = None


class ListMonitoringAlertsResponse(BaseValidatorModel):
    MonitoringAlertSummaries: List[MonitoringAlertSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInferenceExperimentResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Type: Literal['ShadowMode']
    Schedule: InferenceExperimentScheduleOutput
    Status: InferenceExperimentStatusType
    StatusReason: str
    Description: str
    CreationTime: datetime
    CompletionTime: datetime
    LastModifiedTime: datetime
    RoleArn: str
    EndpointMetadata: EndpointMetadata
    ModelVariants: List[ModelVariantConfigSummary]
    DataStorageConfig: InferenceExperimentDataStorageConfigOutput
    ShadowModeConfig: ShadowModeConfigOutput
    KmsKey: str
    ResponseMetadata: ResponseMetadata


class StopInferenceExperimentRequest(BaseValidatorModel):
    Name: str
    ModelVariantActions: Dict[str, ModelVariantActionType]
    DesiredModelVariants: Optional[List[ModelVariantConfig]] = None
    DesiredState: Optional[InferenceExperimentStopDesiredStateType] = None
    Reason: Optional[str] = None

OptimizationConfigUnion = Union[OptimizationConfig, OptimizationConfigOutput]


class DataQualityJobInputOutput(BaseValidatorModel):
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInputOutput] = None


class ModelBiasJobInputOutput(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3Input
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInputOutput] = None


class ModelExplainabilityJobInputOutput(BaseValidatorModel):
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInputOutput] = None


class ModelQualityJobInputOutput(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3Input
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInputOutput] = None


class MonitoringInputOutput(BaseValidatorModel):
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInputOutput] = None


class DataQualityJobInput(BaseValidatorModel):
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInput] = None


class ModelBiasJobInput(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3Input
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInput] = None


class ModelExplainabilityJobInput(BaseValidatorModel):
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInput] = None


class ModelQualityJobInput(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3Input
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInput] = None


class MonitoringInput(BaseValidatorModel):
    EndpointInput: Optional[EndpointInput] = None
    BatchTransformInput: Optional[BatchTransformInput] = None

MonitoringOutputConfigUnion = Union[MonitoringOutputConfig, MonitoringOutputConfigOutput]

MemberDefinitionUnion = Union[MemberDefinition, MemberDefinitionOutput]


class DescribeOptimizationJobResponse(BaseValidatorModel):
    OptimizationJobArn: str
    OptimizationJobStatus: OptimizationJobStatusType
    OptimizationStartTime: datetime
    OptimizationEndTime: datetime
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    OptimizationJobName: str
    ModelSource: OptimizationJobModelSource
    OptimizationEnvironment: Dict[str, str]
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationConfigs: List[OptimizationConfigOutput]
    OutputConfig: OptimizationJobOutputConfig
    OptimizationOutput: OptimizationOutput
    RoleArn: str
    StoppingCondition: StoppingCondition
    VpcConfig: OptimizationVpcConfigOutput
    ResponseMetadata: ResponseMetadata


class CreateClusterSchedulerConfigRequest(BaseValidatorModel):
    Name: str
    ClusterArn: str
    SchedulerConfig: SchedulerConfigUnion
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateClusterSchedulerConfigRequest(BaseValidatorModel):
    ClusterSchedulerConfigId: str
    TargetVersion: int
    SchedulerConfig: Optional[SchedulerConfigUnion] = None
    Description: Optional[str] = None


class DescribeProcessingJobResponse(BaseValidatorModel):
    ProcessingInputs: List[ProcessingInput]
    ProcessingOutputConfig: ProcessingOutputConfigOutput
    ProcessingJobName: str
    ProcessingResources: ProcessingResources
    StoppingCondition: ProcessingStoppingCondition
    AppSpecification: AppSpecificationOutput
    Environment: Dict[str, str]
    NetworkConfig: NetworkConfigOutput
    RoleArn: str
    ExperimentConfig: ExperimentConfig
    ProcessingJobArn: str
    ProcessingJobStatus: ProcessingJobStatusType
    ExitMessage: str
    FailureReason: str
    ProcessingEndTime: datetime
    ProcessingStartTime: datetime
    LastModifiedTime: datetime
    CreationTime: datetime
    MonitoringScheduleArn: str
    AutoMLJobArn: str
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadata


class ProcessingJob(BaseValidatorModel):
    ProcessingInputs: Optional[List[ProcessingInput]] = None
    ProcessingOutputConfig: Optional[ProcessingOutputConfigOutput] = None
    ProcessingJobName: Optional[str] = None
    ProcessingResources: Optional[ProcessingResources] = None
    StoppingCondition: Optional[ProcessingStoppingCondition] = None
    AppSpecification: Optional[AppSpecificationOutput] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigOutput] = None
    RoleArn: Optional[str] = None
    ExperimentConfig: Optional[ExperimentConfig] = None
    ProcessingJobArn: Optional[str] = None
    ProcessingJobStatus: Optional[ProcessingJobStatusType] = None
    ExitMessage: Optional[str] = None
    FailureReason: Optional[str] = None
    ProcessingEndTime: Optional[datetime] = None
    ProcessingStartTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    MonitoringScheduleArn: Optional[str] = None
    AutoMLJobArn: Optional[str] = None
    TrainingJobArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None

ProcessingOutputConfigUnion = Union[ProcessingOutputConfig, ProcessingOutputConfigOutput]


class CreateProjectInput(BaseValidatorModel):
    ProjectName: str
    ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsUnion
    ProjectDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DescribeFlowDefinitionResponse(BaseValidatorModel):
    FlowDefinitionArn: str
    FlowDefinitionName: str
    FlowDefinitionStatus: FlowDefinitionStatusType
    CreationTime: datetime
    HumanLoopRequestSource: HumanLoopRequestSource
    HumanLoopActivationConfig: HumanLoopActivationConfig
    HumanLoopConfig: HumanLoopConfigOutput
    OutputConfig: FlowDefinitionOutputConfig
    RoleArn: str
    FailureReason: str
    ResponseMetadata: ResponseMetadata

HumanLoopConfigUnion = Union[HumanLoopConfig, HumanLoopConfigOutput]


class DescribeLabelingJobResponse(BaseValidatorModel):
    LabelingJobStatus: LabelingJobStatusType
    LabelCounters: LabelCounters
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    JobReferenceCode: str
    LabelingJobName: str
    LabelingJobArn: str
    LabelAttributeName: str
    InputConfig: LabelingJobInputConfigOutput
    OutputConfig: LabelingJobOutputConfig
    RoleArn: str
    LabelCategoryConfigS3Uri: str
    StoppingConditions: LabelingJobStoppingConditions
    LabelingJobAlgorithmsConfig: LabelingJobAlgorithmsConfigOutput
    HumanTaskConfig: HumanTaskConfigOutput
    Tags: List[Tag]
    LabelingJobOutput: LabelingJobOutput
    ResponseMetadata: ResponseMetadata

HumanTaskConfigUnion = Union[HumanTaskConfig, HumanTaskConfigOutput]


class StartPipelineExecutionRequest(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineParameters: Optional[List[Parameter]] = None
    PipelineExecutionDescription: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfigUnion] = None


class CreateInferenceExperimentRequest(BaseValidatorModel):
    Name: str
    Type: Literal['ShadowMode']
    RoleArn: str
    EndpointName: str
    ModelVariants: List[ModelVariantConfig]
    ShadowModeConfig: ShadowModeConfigUnion
    Schedule: Optional[InferenceExperimentScheduleUnion] = None
    Description: Optional[str] = None
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfigUnion] = None
    KmsKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateInferenceExperimentRequest(BaseValidatorModel):
    Name: str
    Schedule: Optional[InferenceExperimentScheduleUnion] = None
    Description: Optional[str] = None
    ModelVariants: Optional[List[ModelVariantConfig]] = None
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfigUnion] = None
    ShadowModeConfig: Optional[ShadowModeConfigUnion] = None


class SpaceSettingsOutput(BaseValidatorModel):
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutput] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutput] = None
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettings] = None
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettingsOutput] = None
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettings] = None
    CustomFileSystems: Optional[List[CustomFileSystem]] = None


class SpaceSettings(BaseValidatorModel):
    JupyterServerAppSettings: Optional[JupyterServerAppSettings] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettings] = None
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettings] = None
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettings] = None
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettings] = None
    CustomFileSystems: Optional[List[CustomFileSystem]] = None

AlgorithmSpecificationUnion = Union[AlgorithmSpecification, AlgorithmSpecificationOutput]


class CreateTransformJobRequest(BaseValidatorModel):
    TransformJobName: str
    ModelName: str
    TransformInput: TransformInput
    TransformOutput: TransformOutput
    TransformResources: TransformResources
    MaxConcurrentTransforms: Optional[int] = None
    ModelClientConfig: Optional[ModelClientConfig] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None
    DataCaptureConfig: Optional[BatchDataCaptureConfig] = None
    DataProcessing: Optional[DataProcessing] = None
    Tags: Optional[List[Tag]] = None
    ExperimentConfig: Optional[ExperimentConfig] = None


class DescribeTransformJobResponse(BaseValidatorModel):
    TransformJobName: str
    TransformJobArn: str
    TransformJobStatus: TransformJobStatusType
    FailureReason: str
    ModelName: str
    MaxConcurrentTransforms: int
    ModelClientConfig: ModelClientConfig
    MaxPayloadInMB: int
    BatchStrategy: BatchStrategyType
    Environment: Dict[str, str]
    TransformInput: TransformInput
    TransformOutput: TransformOutput
    DataCaptureConfig: BatchDataCaptureConfig
    TransformResources: TransformResources
    CreationTime: datetime
    TransformStartTime: datetime
    TransformEndTime: datetime
    LabelingJobArn: str
    AutoMLJobArn: str
    DataProcessing: DataProcessing
    ExperimentConfig: ExperimentConfig
    ResponseMetadata: ResponseMetadata


class TransformJobDefinitionOutput(BaseValidatorModel):
    TransformInput: TransformInput
    TransformOutput: TransformOutput
    TransformResources: TransformResources
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None


class TransformJobDefinition(BaseValidatorModel):
    TransformInput: TransformInput
    TransformOutput: TransformOutput
    TransformResources: TransformResources
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None


class TransformJob(BaseValidatorModel):
    TransformJobName: Optional[str] = None
    TransformJobArn: Optional[str] = None
    TransformJobStatus: Optional[TransformJobStatusType] = None
    FailureReason: Optional[str] = None
    ModelName: Optional[str] = None
    MaxConcurrentTransforms: Optional[int] = None
    ModelClientConfig: Optional[ModelClientConfig] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None
    TransformInput: Optional[TransformInput] = None
    TransformOutput: Optional[TransformOutput] = None
    DataCaptureConfig: Optional[BatchDataCaptureConfig] = None
    TransformResources: Optional[TransformResources] = None
    CreationTime: Optional[datetime] = None
    TransformStartTime: Optional[datetime] = None
    TransformEndTime: Optional[datetime] = None
    LabelingJobArn: Optional[str] = None
    AutoMLJobArn: Optional[str] = None
    DataProcessing: Optional[DataProcessing] = None
    ExperimentConfig: Optional[ExperimentConfig] = None
    Tags: Optional[List[Tag]] = None


class DescribeDomainResponse(BaseValidatorModel):
    DomainArn: str
    DomainId: str
    DomainName: str
    HomeEfsFileSystemId: str
    SingleSignOnManagedApplicationInstanceId: str
    SingleSignOnApplicationArn: str
    Status: DomainStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    SecurityGroupIdForDomainBoundary: str
    AuthMode: AuthModeType
    DefaultUserSettings: UserSettingsOutput
    DomainSettings: DomainSettingsOutput
    AppNetworkAccessType: AppNetworkAccessTypeType
    HomeEfsFileSystemKmsKeyId: str
    SubnetIds: List[str]
    Url: str
    VpcId: str
    KmsKeyId: str
    AppSecurityGroupManagement: AppSecurityGroupManagementType
    TagPropagation: TagPropagationType
    DefaultSpaceSettings: DefaultSpaceSettingsOutput
    ResponseMetadata: ResponseMetadata


class DescribeUserProfileResponse(BaseValidatorModel):
    DomainId: str
    UserProfileArn: str
    UserProfileName: str
    HomeEfsFileSystemUid: str
    Status: UserProfileStatusType
    LastModifiedTime: datetime
    CreationTime: datetime
    FailureReason: str
    SingleSignOnUserIdentifier: str
    SingleSignOnUserValue: str
    UserSettings: UserSettingsOutput
    ResponseMetadata: ResponseMetadata

DefaultSpaceSettingsUnion = Union[DefaultSpaceSettings, DefaultSpaceSettingsOutput]

UserSettingsUnion = Union[UserSettings, UserSettingsOutput]


class DescribeAutoMLJobV2Response(BaseValidatorModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    AutoMLJobInputDataConfig: List[AutoMLJobChannel]
    OutputDataConfig: AutoMLOutputDataConfig
    RoleArn: str
    AutoMLJobObjective: AutoMLJobObjective
    AutoMLProblemTypeConfig: AutoMLProblemTypeConfigOutput
    AutoMLProblemTypeConfigName: AutoMLProblemTypeConfigNameType
    CreationTime: datetime
    EndTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    PartialFailureReasons: List[AutoMLPartialFailureReason]
    BestCandidate: AutoMLCandidate
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    AutoMLJobArtifacts: AutoMLJobArtifacts
    ResolvedAttributes: AutoMLResolvedAttributes
    ModelDeployConfig: ModelDeployConfig
    ModelDeployResult: ModelDeployResult
    DataSplitConfig: AutoMLDataSplitConfig
    SecurityConfig: AutoMLSecurityConfigOutput
    AutoMLComputeConfig: AutoMLComputeConfig
    ResponseMetadata: ResponseMetadata

AutoMLProblemTypeConfigUnion = Union[AutoMLProblemTypeConfig, AutoMLProblemTypeConfigOutput]


class CreateAutoMLJobRequest(BaseValidatorModel):
    AutoMLJobName: str
    InputDataConfig: List[AutoMLChannel]
    OutputDataConfig: AutoMLOutputDataConfig
    RoleArn: str
    ProblemType: Optional[ProblemTypeType] = None
    AutoMLJobObjective: Optional[AutoMLJobObjective] = None
    AutoMLJobConfig: Optional[AutoMLJobConfigUnion] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ModelDeployConfig: Optional[ModelDeployConfig] = None


class ListPipelineExecutionStepsResponse(BaseValidatorModel):
    PipelineExecutionSteps: List[PipelineExecutionStep]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DeploymentConfigUnion = Union[DeploymentConfig, DeploymentConfigOutput]


class DescribeInferenceRecommendationsJobResponse(BaseValidatorModel):
    JobName: str
    JobDescription: str
    JobType: RecommendationJobTypeType
    JobArn: str
    RoleArn: str
    Status: RecommendationJobStatusType
    CreationTime: datetime
    CompletionTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    InputConfig: RecommendationJobInputConfigOutput
    StoppingConditions: RecommendationJobStoppingConditionsOutput
    InferenceRecommendations: List[InferenceRecommendation]
    EndpointPerformances: List[EndpointPerformance]
    ResponseMetadata: ResponseMetadata

HyperParameterTuningJobConfigUnion = Union[HyperParameterTuningJobConfig, HyperParameterTuningJobConfigOutput]

RecommendationJobInputConfigUnion = Union[RecommendationJobInputConfig, RecommendationJobInputConfigOutput]


class DescribeEndpointConfigOutput(BaseValidatorModel):
    EndpointConfigName: str
    EndpointConfigArn: str
    ProductionVariants: List[ProductionVariant]
    DataCaptureConfig: DataCaptureConfigOutput
    KmsKeyId: str
    CreationTime: datetime
    AsyncInferenceConfig: AsyncInferenceConfigOutput
    ExplainerConfig: ExplainerConfigOutput
    ShadowProductionVariants: List[ProductionVariant]
    ExecutionRoleArn: str
    VpcConfig: VpcConfigOutput
    EnableNetworkIsolation: bool
    ResponseMetadata: ResponseMetadata


class DescribeEndpointOutput(BaseValidatorModel):
    EndpointName: str
    EndpointArn: str
    EndpointConfigName: str
    ProductionVariants: List[ProductionVariantSummary]
    DataCaptureConfig: DataCaptureConfigSummary
    EndpointStatus: EndpointStatusType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LastDeploymentConfig: DeploymentConfigOutput
    AsyncInferenceConfig: AsyncInferenceConfigOutput
    PendingDeploymentSummary: PendingDeploymentSummary
    ExplainerConfig: ExplainerConfigOutput
    ShadowProductionVariants: List[ProductionVariantSummary]
    ResponseMetadata: ResponseMetadata

ExplainerConfigUnion = Union[ExplainerConfig, ExplainerConfigOutput]


class ListSpacesResponse(BaseValidatorModel):
    Spaces: List[SpaceDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInferenceRecommendationsJobStepsResponse(BaseValidatorModel):
    Steps: List[InferenceRecommendationsJobStep]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeWorkteamResponse(BaseValidatorModel):
    Workteam: Workteam
    ResponseMetadata: ResponseMetadata


class ListWorkteamsResponse(BaseValidatorModel):
    Workteams: List[Workteam]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateWorkteamResponse(BaseValidatorModel):
    Workteam: Workteam
    ResponseMetadata: ResponseMetadata


class UpdateInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str
    Specification: Optional[InferenceComponentSpecification] = None
    RuntimeConfig: Optional[InferenceComponentRuntimeConfig] = None
    DeploymentConfig: Optional[InferenceComponentDeploymentConfigUnion] = None

TrainingSpecificationUnion = Union[TrainingSpecification, TrainingSpecificationOutput]


class ListLabelingJobsResponse(BaseValidatorModel):
    LabelingJobSummaryList: List[LabelingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DynamicScalingConfiguration(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None
    ScalingPolicies: Optional[List[ScalingPolicy]] = None


class DescribeTrainingJobResponse(BaseValidatorModel):
    TrainingJobName: str
    TrainingJobArn: str
    TuningJobArn: str
    LabelingJobArn: str
    AutoMLJobArn: str
    ModelArtifacts: ModelArtifacts
    TrainingJobStatus: TrainingJobStatusType
    SecondaryStatus: SecondaryStatusType
    FailureReason: str
    HyperParameters: Dict[str, str]
    AlgorithmSpecification: AlgorithmSpecificationOutput
    RoleArn: str
    InputDataConfig: List[ChannelOutput]
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfigOutput
    WarmPoolStatus: WarmPoolStatus
    VpcConfig: VpcConfigOutput
    StoppingCondition: StoppingCondition
    CreationTime: datetime
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    LastModifiedTime: datetime
    SecondaryStatusTransitions: List[SecondaryStatusTransition]
    FinalMetricDataList: List[MetricData]
    EnableNetworkIsolation: bool
    EnableInterContainerTrafficEncryption: bool
    EnableManagedSpotTraining: bool
    CheckpointConfig: CheckpointConfig
    TrainingTimeInSeconds: int
    BillableTimeInSeconds: int
    DebugHookConfig: DebugHookConfigOutput
    ExperimentConfig: ExperimentConfig
    DebugRuleConfigurations: List[DebugRuleConfigurationOutput]
    TensorBoardOutputConfig: TensorBoardOutputConfig
    DebugRuleEvaluationStatuses: List[DebugRuleEvaluationStatus]
    ProfilerConfig: ProfilerConfigOutput
    ProfilerRuleConfigurations: List[ProfilerRuleConfigurationOutput]
    ProfilerRuleEvaluationStatuses: List[ProfilerRuleEvaluationStatus]
    ProfilingStatus: ProfilingStatusType
    Environment: Dict[str, str]
    RetryStrategy: RetryStrategy
    RemoteDebugConfig: RemoteDebugConfig
    InfraCheckConfig: InfraCheckConfig
    ResponseMetadata: ResponseMetadata


class HyperParameterTrainingJobDefinitionOutput(BaseValidatorModel):
    AlgorithmSpecification: HyperParameterAlgorithmSpecificationOutput
    RoleArn: str
    OutputDataConfig: OutputDataConfig
    StoppingCondition: StoppingCondition
    DefinitionName: Optional[str] = None
    TuningObjective: Optional[HyperParameterTuningJobObjective] = None
    HyperParameterRanges: Optional[ParameterRangesOutput] = None
    StaticHyperParameters: Optional[Dict[str, str]] = None
    InputDataConfig: Optional[List[ChannelOutput]] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    ResourceConfig: Optional[ResourceConfigOutput] = None
    HyperParameterTuningResourceConfig: Optional[HyperParameterTuningResourceConfigOutput] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfig] = None
    RetryStrategy: Optional[RetryStrategy] = None
    Environment: Optional[Dict[str, str]] = None


class TrainingJobDefinitionOutput(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    InputDataConfig: List[ChannelOutput]
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfigOutput
    StoppingCondition: StoppingCondition
    HyperParameters: Optional[Dict[str, str]] = None


class TrainingJob(BaseValidatorModel):
    TrainingJobName: Optional[str] = None
    TrainingJobArn: Optional[str] = None
    TuningJobArn: Optional[str] = None
    LabelingJobArn: Optional[str] = None
    AutoMLJobArn: Optional[str] = None
    ModelArtifacts: Optional[ModelArtifacts] = None
    TrainingJobStatus: Optional[TrainingJobStatusType] = None
    SecondaryStatus: Optional[SecondaryStatusType] = None
    FailureReason: Optional[str] = None
    HyperParameters: Optional[Dict[str, str]] = None
    AlgorithmSpecification: Optional[AlgorithmSpecificationOutput] = None
    RoleArn: Optional[str] = None
    InputDataConfig: Optional[List[ChannelOutput]] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    ResourceConfig: Optional[ResourceConfigOutput] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    StoppingCondition: Optional[StoppingCondition] = None
    CreationTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    SecondaryStatusTransitions: Optional[List[SecondaryStatusTransition]] = None
    FinalMetricDataList: Optional[List[MetricData]] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfig] = None
    TrainingTimeInSeconds: Optional[int] = None
    BillableTimeInSeconds: Optional[int] = None
    DebugHookConfig: Optional[DebugHookConfigOutput] = None
    ExperimentConfig: Optional[ExperimentConfig] = None
    DebugRuleConfigurations: Optional[List[DebugRuleConfigurationOutput]] = None
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfig] = None
    DebugRuleEvaluationStatuses: Optional[List[DebugRuleEvaluationStatus]] = None
    ProfilerConfig: Optional[ProfilerConfigOutput] = None
    Environment: Optional[Dict[str, str]] = None
    RetryStrategy: Optional[RetryStrategy] = None
    Tags: Optional[List[Tag]] = None

DataSourceUnion = Union[DataSource, DataSourceOutput]


class DescribeModelOutput(BaseValidatorModel):
    ModelName: str
    PrimaryContainer: ContainerDefinitionOutput
    Containers: List[ContainerDefinitionOutput]
    InferenceExecutionConfig: InferenceExecutionConfig
    ExecutionRoleArn: str
    VpcConfig: VpcConfigOutput
    CreationTime: datetime
    ModelArn: str
    EnableNetworkIsolation: bool
    DeploymentRecommendation: DeploymentRecommendation
    ResponseMetadata: ResponseMetadata


class Model(BaseValidatorModel):
    ModelName: Optional[str] = None
    PrimaryContainer: Optional[ContainerDefinitionOutput] = None
    Containers: Optional[List[ContainerDefinitionOutput]] = None
    InferenceExecutionConfig: Optional[InferenceExecutionConfig] = None
    ExecutionRoleArn: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    CreationTime: Optional[datetime] = None
    ModelArn: Optional[str] = None
    EnableNetworkIsolation: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    DeploymentRecommendation: Optional[DeploymentRecommendation] = None

ContainerDefinitionUnion = Union[ContainerDefinition, ContainerDefinitionOutput]


class AdditionalInferenceSpecificationDefinitionOutput(BaseValidatorModel):
    Name: str
    Containers: List[ModelPackageContainerDefinitionOutput]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[List[ProductionVariantInstanceTypeType]] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None


class InferenceSpecificationOutput(BaseValidatorModel):
    Containers: List[ModelPackageContainerDefinitionOutput]
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[List[ProductionVariantInstanceTypeType]] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None


class InferenceSpecification(BaseValidatorModel):
    Containers: List[ModelPackageContainerDefinition]
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[List[ProductionVariantInstanceTypeType]] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

ModelPackageContainerDefinitionUnion = Union[ModelPackageContainerDefinition, ModelPackageContainerDefinitionOutput]


class SourceAlgorithmSpecificationOutput(BaseValidatorModel):
    SourceAlgorithms: List[SourceAlgorithm]


class SourceAlgorithmSpecification(BaseValidatorModel):
    SourceAlgorithms: List[SourceAlgorithm]


class CreateOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str
    RoleArn: str
    ModelSource: OptimizationJobModelSource
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationConfigs: List[OptimizationConfigUnion]
    OutputConfig: OptimizationJobOutputConfig
    StoppingCondition: StoppingCondition
    OptimizationEnvironment: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    VpcConfig: Optional[OptimizationVpcConfigUnion] = None


class DescribeDataQualityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    DataQualityBaselineConfig: DataQualityBaselineConfig
    DataQualityAppSpecification: DataQualityAppSpecificationOutput
    DataQualityJobInput: DataQualityJobInputOutput
    DataQualityJobOutputConfig: MonitoringOutputConfigOutput
    JobResources: MonitoringResources
    NetworkConfig: MonitoringNetworkConfigOutput
    RoleArn: str
    StoppingCondition: MonitoringStoppingCondition
    ResponseMetadata: ResponseMetadata


class DescribeModelBiasJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelBiasBaselineConfig: ModelBiasBaselineConfig
    ModelBiasAppSpecification: ModelBiasAppSpecificationOutput
    ModelBiasJobInput: ModelBiasJobInputOutput
    ModelBiasJobOutputConfig: MonitoringOutputConfigOutput
    JobResources: MonitoringResources
    NetworkConfig: MonitoringNetworkConfigOutput
    RoleArn: str
    StoppingCondition: MonitoringStoppingCondition
    ResponseMetadata: ResponseMetadata


class DescribeModelExplainabilityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelExplainabilityBaselineConfig: ModelExplainabilityBaselineConfig
    ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecificationOutput
    ModelExplainabilityJobInput: ModelExplainabilityJobInputOutput
    ModelExplainabilityJobOutputConfig: MonitoringOutputConfigOutput
    JobResources: MonitoringResources
    NetworkConfig: MonitoringNetworkConfigOutput
    RoleArn: str
    StoppingCondition: MonitoringStoppingCondition
    ResponseMetadata: ResponseMetadata


class DescribeModelQualityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelQualityBaselineConfig: ModelQualityBaselineConfig
    ModelQualityAppSpecification: ModelQualityAppSpecificationOutput
    ModelQualityJobInput: ModelQualityJobInputOutput
    ModelQualityJobOutputConfig: MonitoringOutputConfigOutput
    JobResources: MonitoringResources
    NetworkConfig: MonitoringNetworkConfigOutput
    RoleArn: str
    StoppingCondition: MonitoringStoppingCondition
    ResponseMetadata: ResponseMetadata


class MonitoringJobDefinitionOutput(BaseValidatorModel):
    MonitoringInputs: List[MonitoringInputOutput]
    MonitoringOutputConfig: MonitoringOutputConfigOutput
    MonitoringResources: MonitoringResources
    MonitoringAppSpecification: MonitoringAppSpecificationOutput
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfig] = None
    StoppingCondition: Optional[MonitoringStoppingCondition] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigOutput] = None

DataQualityJobInputUnion = Union[DataQualityJobInput, DataQualityJobInputOutput]

ModelBiasJobInputUnion = Union[ModelBiasJobInput, ModelBiasJobInputOutput]

ModelExplainabilityJobInputUnion = Union[ModelExplainabilityJobInput, ModelExplainabilityJobInputOutput]

ModelQualityJobInputUnion = Union[ModelQualityJobInput, ModelQualityJobInputOutput]


class MonitoringJobDefinition(BaseValidatorModel):
    MonitoringInputs: List[MonitoringInput]
    MonitoringOutputConfig: MonitoringOutputConfig
    MonitoringResources: MonitoringResources
    MonitoringAppSpecification: MonitoringAppSpecification
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfig] = None
    StoppingCondition: Optional[MonitoringStoppingCondition] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfig] = None


class CreateWorkteamRequest(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: List[MemberDefinitionUnion]
    Description: str
    WorkforceName: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration] = None
    Tags: Optional[List[Tag]] = None


class UpdateWorkteamRequest(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: Optional[List[MemberDefinitionUnion]] = None
    Description: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration] = None


class CreateProcessingJobRequest(BaseValidatorModel):
    ProcessingJobName: str
    ProcessingResources: ProcessingResources
    AppSpecification: AppSpecificationUnion
    RoleArn: str
    ProcessingInputs: Optional[List[ProcessingInput]] = None
    ProcessingOutputConfig: Optional[ProcessingOutputConfigUnion] = None
    StoppingCondition: Optional[ProcessingStoppingCondition] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    ExperimentConfig: Optional[ExperimentConfig] = None


class CreateFlowDefinitionRequest(BaseValidatorModel):
    FlowDefinitionName: str
    OutputConfig: FlowDefinitionOutputConfig
    RoleArn: str
    HumanLoopRequestSource: Optional[HumanLoopRequestSource] = None
    HumanLoopActivationConfig: Optional[HumanLoopActivationConfig] = None
    HumanLoopConfig: Optional[HumanLoopConfigUnion] = None
    Tags: Optional[List[Tag]] = None


class CreateLabelingJobRequest(BaseValidatorModel):
    LabelingJobName: str
    LabelAttributeName: str
    InputConfig: LabelingJobInputConfigUnion
    OutputConfig: LabelingJobOutputConfig
    RoleArn: str
    HumanTaskConfig: HumanTaskConfigUnion
    LabelCategoryConfigS3Uri: Optional[str] = None
    StoppingConditions: Optional[LabelingJobStoppingConditions] = None
    LabelingJobAlgorithmsConfig: Optional[LabelingJobAlgorithmsConfigUnion] = None
    Tags: Optional[List[Tag]] = None


class DescribeSpaceResponse(BaseValidatorModel):
    DomainId: str
    SpaceArn: str
    SpaceName: str
    HomeEfsFileSystemUid: str
    Status: SpaceStatusType
    LastModifiedTime: datetime
    CreationTime: datetime
    FailureReason: str
    SpaceSettings: SpaceSettingsOutput
    OwnershipSettings: OwnershipSettings
    SpaceSharingSettings: SpaceSharingSettings
    SpaceDisplayName: str
    Url: str
    ResponseMetadata: ResponseMetadata

SpaceSettingsUnion = Union[SpaceSettings, SpaceSettingsOutput]


class ModelPackageValidationProfileOutput(BaseValidatorModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionOutput


class ModelPackageValidationProfile(BaseValidatorModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinition


class CreateDomainRequest(BaseValidatorModel):
    DomainName: str
    AuthMode: AuthModeType
    DefaultUserSettings: UserSettingsUnion
    SubnetIds: List[str]
    VpcId: str
    DomainSettings: Optional[DomainSettingsUnion] = None
    Tags: Optional[List[Tag]] = None
    AppNetworkAccessType: Optional[AppNetworkAccessTypeType] = None
    HomeEfsFileSystemKmsKeyId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagementType] = None
    TagPropagation: Optional[TagPropagationType] = None
    DefaultSpaceSettings: Optional[DefaultSpaceSettingsUnion] = None


class CreateUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    SingleSignOnUserIdentifier: Optional[str] = None
    SingleSignOnUserValue: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    UserSettings: Optional[UserSettingsUnion] = None


class UpdateDomainRequest(BaseValidatorModel):
    DomainId: str
    DefaultUserSettings: Optional[UserSettingsUnion] = None
    DomainSettingsForUpdate: Optional[DomainSettingsForUpdate] = None
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagementType] = None
    DefaultSpaceSettings: Optional[DefaultSpaceSettingsUnion] = None
    SubnetIds: Optional[List[str]] = None
    AppNetworkAccessType: Optional[AppNetworkAccessTypeType] = None
    TagPropagation: Optional[TagPropagationType] = None


class UpdateUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    UserSettings: Optional[UserSettingsUnion] = None


class CreateAutoMLJobV2Request(BaseValidatorModel):
    AutoMLJobName: str
    AutoMLJobInputDataConfig: List[AutoMLJobChannel]
    OutputDataConfig: AutoMLOutputDataConfig
    AutoMLProblemTypeConfig: AutoMLProblemTypeConfigUnion
    RoleArn: str
    Tags: Optional[List[Tag]] = None
    SecurityConfig: Optional[AutoMLSecurityConfigUnion] = None
    AutoMLJobObjective: Optional[AutoMLJobObjective] = None
    ModelDeployConfig: Optional[ModelDeployConfig] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfig] = None
    AutoMLComputeConfig: Optional[AutoMLComputeConfig] = None


class CreateEndpointInput(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: str
    DeploymentConfig: Optional[DeploymentConfigUnion] = None
    Tags: Optional[List[Tag]] = None


class UpdateEndpointInput(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: str
    RetainAllVariantProperties: Optional[bool] = None
    ExcludeRetainedVariantProperties: Optional[List[VariantProperty]] = None
    DeploymentConfig: Optional[DeploymentConfigUnion] = None
    RetainDeploymentConfig: Optional[bool] = None


class CreateInferenceRecommendationsJobRequest(BaseValidatorModel):
    JobName: str
    JobType: RecommendationJobTypeType
    RoleArn: str
    InputConfig: RecommendationJobInputConfigUnion
    JobDescription: Optional[str] = None
    StoppingConditions: Optional[RecommendationJobStoppingConditionsUnion] = None
    OutputConfig: Optional[RecommendationJobOutputConfig] = None
    Tags: Optional[List[Tag]] = None


class CreateEndpointConfigInput(BaseValidatorModel):
    EndpointConfigName: str
    ProductionVariants: List[ProductionVariant]
    DataCaptureConfig: Optional[DataCaptureConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    AsyncInferenceConfig: Optional[AsyncInferenceConfigUnion] = None
    ExplainerConfig: Optional[ExplainerConfigUnion] = None
    ShadowProductionVariants: Optional[List[ProductionVariant]] = None
    ExecutionRoleArn: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    EnableNetworkIsolation: Optional[bool] = None


class GetScalingConfigurationRecommendationResponse(BaseValidatorModel):
    InferenceRecommendationsJobName: str
    RecommendationId: str
    EndpointName: str
    TargetCpuUtilizationPerCore: int
    ScalingPolicyObjective: ScalingPolicyObjective
    Metric: ScalingPolicyMetric
    DynamicScalingConfiguration: DynamicScalingConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeHyperParameterTuningJobResponse(BaseValidatorModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobArn: str
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfigOutput
    TrainingJobDefinition: HyperParameterTrainingJobDefinitionOutput
    TrainingJobDefinitions: List[HyperParameterTrainingJobDefinitionOutput]
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatusType
    CreationTime: datetime
    HyperParameterTuningEndTime: datetime
    LastModifiedTime: datetime
    TrainingJobStatusCounters: TrainingJobStatusCounters
    ObjectiveStatusCounters: ObjectiveStatusCounters
    BestTrainingJob: HyperParameterTrainingJobSummary
    OverallBestTrainingJob: HyperParameterTrainingJobSummary
    WarmStartConfig: HyperParameterTuningJobWarmStartConfigOutput
    Autotune: Autotune
    FailureReason: str
    TuningJobCompletionDetails: HyperParameterTuningJobCompletionDetails
    ConsumedResources: HyperParameterTuningJobConsumedResources
    ResponseMetadata: ResponseMetadata


class HyperParameterTuningJobSearchEntity(BaseValidatorModel):
    HyperParameterTuningJobName: Optional[str] = None
    HyperParameterTuningJobArn: Optional[str] = None
    HyperParameterTuningJobConfig: Optional[HyperParameterTuningJobConfigOutput] = None
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinitionOutput] = None
    TrainingJobDefinitions: Optional[List[HyperParameterTrainingJobDefinitionOutput]] = None
    HyperParameterTuningJobStatus: Optional[HyperParameterTuningJobStatusType] = None
    CreationTime: Optional[datetime] = None
    HyperParameterTuningEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    TrainingJobStatusCounters: Optional[TrainingJobStatusCounters] = None
    ObjectiveStatusCounters: Optional[ObjectiveStatusCounters] = None
    BestTrainingJob: Optional[HyperParameterTrainingJobSummary] = None
    OverallBestTrainingJob: Optional[HyperParameterTrainingJobSummary] = None
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfigOutput] = None
    FailureReason: Optional[str] = None
    TuningJobCompletionDetails: Optional[HyperParameterTuningJobCompletionDetails] = None
    ConsumedResources: Optional[HyperParameterTuningJobConsumedResources] = None
    Tags: Optional[List[Tag]] = None


class AlgorithmValidationProfileOutput(BaseValidatorModel):
    ProfileName: str
    TrainingJobDefinition: TrainingJobDefinitionOutput
    TransformJobDefinition: Optional[TransformJobDefinitionOutput] = None


class TrialComponentSourceDetail(BaseValidatorModel):
    SourceArn: Optional[str] = None
    TrainingJob: Optional[TrainingJob] = None
    ProcessingJob: Optional[ProcessingJob] = None
    TransformJob: Optional[TransformJob] = None


class Channel(BaseValidatorModel):
    ChannelName: str
    DataSource: DataSourceUnion
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfig] = None


class CreateModelInput(BaseValidatorModel):
    ModelName: str
    PrimaryContainer: Optional[ContainerDefinitionUnion] = None
    Containers: Optional[List[ContainerDefinitionUnion]] = None
    InferenceExecutionConfig: Optional[InferenceExecutionConfig] = None
    ExecutionRoleArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    EnableNetworkIsolation: Optional[bool] = None


class BatchDescribeModelPackageSummary(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageArn: str
    CreationTime: datetime
    InferenceSpecification: InferenceSpecificationOutput
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageVersion: Optional[int] = None
    ModelPackageDescription: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None

InferenceSpecificationUnion = Union[InferenceSpecification, InferenceSpecificationOutput]


class AdditionalInferenceSpecificationDefinition(BaseValidatorModel):
    Name: str
    Containers: List[ModelPackageContainerDefinitionUnion]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[List[ProductionVariantInstanceTypeType]] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

SourceAlgorithmSpecificationUnion = Union[SourceAlgorithmSpecification, SourceAlgorithmSpecificationOutput]


class MonitoringScheduleConfigOutput(BaseValidatorModel):
    ScheduleConfig: Optional[ScheduleConfig] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionOutput] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None


class CreateDataQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str
    DataQualityAppSpecification: DataQualityAppSpecificationUnion
    DataQualityJobInput: DataQualityJobInputUnion
    DataQualityJobOutputConfig: MonitoringOutputConfigUnion
    JobResources: MonitoringResources
    RoleArn: str
    DataQualityBaselineConfig: Optional[DataQualityBaselineConfig] = None
    NetworkConfig: Optional[MonitoringNetworkConfigUnion] = None
    StoppingCondition: Optional[MonitoringStoppingCondition] = None
    Tags: Optional[List[Tag]] = None


class CreateModelBiasJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str
    ModelBiasAppSpecification: ModelBiasAppSpecificationUnion
    ModelBiasJobInput: ModelBiasJobInputUnion
    ModelBiasJobOutputConfig: MonitoringOutputConfigUnion
    JobResources: MonitoringResources
    RoleArn: str
    ModelBiasBaselineConfig: Optional[ModelBiasBaselineConfig] = None
    NetworkConfig: Optional[MonitoringNetworkConfigUnion] = None
    StoppingCondition: Optional[MonitoringStoppingCondition] = None
    Tags: Optional[List[Tag]] = None


class CreateModelExplainabilityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str
    ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecificationUnion
    ModelExplainabilityJobInput: ModelExplainabilityJobInputUnion
    ModelExplainabilityJobOutputConfig: MonitoringOutputConfigUnion
    JobResources: MonitoringResources
    RoleArn: str
    ModelExplainabilityBaselineConfig: Optional[ModelExplainabilityBaselineConfig] = None
    NetworkConfig: Optional[MonitoringNetworkConfigUnion] = None
    StoppingCondition: Optional[MonitoringStoppingCondition] = None
    Tags: Optional[List[Tag]] = None


class CreateModelQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str
    ModelQualityAppSpecification: ModelQualityAppSpecificationUnion
    ModelQualityJobInput: ModelQualityJobInputUnion
    ModelQualityJobOutputConfig: MonitoringOutputConfigUnion
    JobResources: MonitoringResources
    RoleArn: str
    ModelQualityBaselineConfig: Optional[ModelQualityBaselineConfig] = None
    NetworkConfig: Optional[MonitoringNetworkConfigUnion] = None
    StoppingCondition: Optional[MonitoringStoppingCondition] = None
    Tags: Optional[List[Tag]] = None


class MonitoringScheduleConfig(BaseValidatorModel):
    ScheduleConfig: Optional[ScheduleConfig] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinition] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None


class CreateSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str
    Tags: Optional[List[Tag]] = None
    SpaceSettings: Optional[SpaceSettingsUnion] = None
    OwnershipSettings: Optional[OwnershipSettings] = None
    SpaceSharingSettings: Optional[SpaceSharingSettings] = None
    SpaceDisplayName: Optional[str] = None


class UpdateSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str
    SpaceSettings: Optional[SpaceSettingsUnion] = None
    SpaceDisplayName: Optional[str] = None


class ModelPackageValidationSpecificationOutput(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[ModelPackageValidationProfileOutput]


class ModelPackageValidationSpecification(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[ModelPackageValidationProfile]


class AlgorithmValidationSpecificationOutput(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[AlgorithmValidationProfileOutput]


class TrialComponent(BaseValidatorModel):
    TrialComponentName: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    Source: Optional[TrialComponentSource] = None
    Status: Optional[TrialComponentStatus] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContext] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None
    Parameters: Optional[Dict[str, TrialComponentParameterValue]] = None
    InputArtifacts: Optional[Dict[str, TrialComponentArtifact]] = None
    OutputArtifacts: Optional[Dict[str, TrialComponentArtifact]] = None
    Metrics: Optional[List[TrialComponentMetricSummary]] = None
    MetadataProperties: Optional[MetadataProperties] = None
    SourceDetail: Optional[TrialComponentSourceDetail] = None
    LineageGroupArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Parents: Optional[List[Parent]] = None
    RunName: Optional[str] = None

ChannelUnion = Union[Channel, ChannelOutput]


class TrainingJobDefinition(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    InputDataConfig: List[Channel]
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfig
    StoppingCondition: StoppingCondition
    HyperParameters: Optional[Dict[str, str]] = None


class BatchDescribeModelPackageOutput(BaseValidatorModel):
    ModelPackageSummaries: Dict[str, BatchDescribeModelPackageSummary]
    BatchDescribeModelPackageErrorMap: Dict[str, BatchDescribeModelPackageError]
    ResponseMetadata: ResponseMetadata

AdditionalInferenceSpecificationDefinitionUnion = Union[AdditionalInferenceSpecificationDefinition, AdditionalInferenceSpecificationDefinitionOutput]


class DescribeMonitoringScheduleResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    MonitoringScheduleName: str
    MonitoringScheduleStatus: ScheduleStatusType
    MonitoringType: MonitoringTypeType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleConfig: MonitoringScheduleConfigOutput
    EndpointName: str
    LastMonitoringExecutionSummary: MonitoringExecutionSummary
    ResponseMetadata: ResponseMetadata


class ModelDashboardMonitoringSchedule(BaseValidatorModel):
    MonitoringScheduleArn: Optional[str] = None
    MonitoringScheduleName: Optional[str] = None
    MonitoringScheduleStatus: Optional[ScheduleStatusType] = None
    MonitoringType: Optional[MonitoringTypeType] = None
    FailureReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    MonitoringScheduleConfig: Optional[MonitoringScheduleConfigOutput] = None
    EndpointName: Optional[str] = None
    MonitoringAlertSummaries: Optional[List[MonitoringAlertSummary]] = None
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummary] = None
    BatchTransformInput: Optional[BatchTransformInputOutput] = None


class MonitoringSchedule(BaseValidatorModel):
    MonitoringScheduleArn: Optional[str] = None
    MonitoringScheduleName: Optional[str] = None
    MonitoringScheduleStatus: Optional[ScheduleStatusType] = None
    MonitoringType: Optional[MonitoringTypeType] = None
    FailureReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    MonitoringScheduleConfig: Optional[MonitoringScheduleConfigOutput] = None
    EndpointName: Optional[str] = None
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummary] = None
    Tags: Optional[List[Tag]] = None

MonitoringScheduleConfigUnion = Union[MonitoringScheduleConfig, MonitoringScheduleConfigOutput]


class DescribeModelPackageOutput(BaseValidatorModel):
    ModelPackageName: str
    ModelPackageGroupName: str
    ModelPackageVersion: int
    ModelPackageArn: str
    ModelPackageDescription: str
    CreationTime: datetime
    InferenceSpecification: InferenceSpecificationOutput
    SourceAlgorithmSpecification: SourceAlgorithmSpecificationOutput
    ValidationSpecification: ModelPackageValidationSpecificationOutput
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageStatusDetails: ModelPackageStatusDetails
    CertifyForMarketplace: bool
    ModelApprovalStatus: ModelApprovalStatusType
    CreatedBy: UserContext
    MetadataProperties: MetadataProperties
    ModelMetrics: ModelMetrics
    LastModifiedTime: datetime
    LastModifiedBy: UserContext
    ApprovalDescription: str
    Domain: str
    Task: str
    SamplePayloadUrl: str
    CustomerMetadataProperties: Dict[str, str]
    DriftCheckBaselines: DriftCheckBaselines
    AdditionalInferenceSpecifications: List[AdditionalInferenceSpecificationDefinitionOutput]
    SkipModelValidation: SkipModelValidationType
    SourceUri: str
    SecurityConfig: ModelPackageSecurityConfig
    ModelCard: ModelPackageModelCard
    ModelLifeCycle: ModelLifeCycle
    ResponseMetadata: ResponseMetadata


class ModelPackage(BaseValidatorModel):
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageVersion: Optional[int] = None
    ModelPackageArn: Optional[str] = None
    ModelPackageDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    InferenceSpecification: Optional[InferenceSpecificationOutput] = None
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecificationOutput] = None
    ValidationSpecification: Optional[ModelPackageValidationSpecificationOutput] = None
    ModelPackageStatus: Optional[ModelPackageStatusType] = None
    ModelPackageStatusDetails: Optional[ModelPackageStatusDetails] = None
    CertifyForMarketplace: Optional[bool] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    CreatedBy: Optional[UserContext] = None
    MetadataProperties: Optional[MetadataProperties] = None
    ModelMetrics: Optional[ModelMetrics] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContext] = None
    ApprovalDescription: Optional[str] = None
    Domain: Optional[str] = None
    Task: Optional[str] = None
    SamplePayloadUrl: Optional[str] = None
    AdditionalInferenceSpecifications: Optional[List[AdditionalInferenceSpecificationDefinitionOutput]] = None
    SourceUri: Optional[str] = None
    SecurityConfig: Optional[ModelPackageSecurityConfig] = None
    ModelCard: Optional[ModelPackageModelCard] = None
    ModelLifeCycle: Optional[ModelLifeCycle] = None
    Tags: Optional[List[Tag]] = None
    CustomerMetadataProperties: Optional[Dict[str, str]] = None
    DriftCheckBaselines: Optional[DriftCheckBaselines] = None
    SkipModelValidation: Optional[SkipModelValidationType] = None

ModelPackageValidationSpecificationUnion = Union[ModelPackageValidationSpecification, ModelPackageValidationSpecificationOutput]


class DescribeAlgorithmOutput(BaseValidatorModel):
    AlgorithmName: str
    AlgorithmArn: str
    AlgorithmDescription: str
    CreationTime: datetime
    TrainingSpecification: TrainingSpecificationOutput
    InferenceSpecification: InferenceSpecificationOutput
    ValidationSpecification: AlgorithmValidationSpecificationOutput
    AlgorithmStatus: AlgorithmStatusType
    AlgorithmStatusDetails: AlgorithmStatusDetails
    ProductId: str
    CertifyForMarketplace: bool
    ResponseMetadata: ResponseMetadata


class CreateTrainingJobRequest(BaseValidatorModel):
    TrainingJobName: str
    AlgorithmSpecification: AlgorithmSpecificationUnion
    RoleArn: str
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfigUnion
    StoppingCondition: StoppingCondition
    HyperParameters: Optional[Dict[str, str]] = None
    InputDataConfig: Optional[List[ChannelUnion]] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfig] = None
    DebugHookConfig: Optional[DebugHookConfigUnion] = None
    DebugRuleConfigurations: Optional[List[DebugRuleConfigurationUnion]] = None
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfig] = None
    ExperimentConfig: Optional[ExperimentConfig] = None
    ProfilerConfig: Optional[ProfilerConfigUnion] = None
    ProfilerRuleConfigurations: Optional[List[ProfilerRuleConfigurationUnion]] = None
    Environment: Optional[Dict[str, str]] = None
    RetryStrategy: Optional[RetryStrategy] = None
    RemoteDebugConfig: Optional[RemoteDebugConfig] = None
    InfraCheckConfig: Optional[InfraCheckConfig] = None
    SessionChainingConfig: Optional[SessionChainingConfig] = None


class HyperParameterTrainingJobDefinition(BaseValidatorModel):
    AlgorithmSpecification: HyperParameterAlgorithmSpecificationUnion
    RoleArn: str
    OutputDataConfig: OutputDataConfig
    StoppingCondition: StoppingCondition
    DefinitionName: Optional[str] = None
    TuningObjective: Optional[HyperParameterTuningJobObjective] = None
    HyperParameterRanges: Optional[ParameterRangesUnion] = None
    StaticHyperParameters: Optional[Dict[str, str]] = None
    InputDataConfig: Optional[List[ChannelUnion]] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    ResourceConfig: Optional[ResourceConfigUnion] = None
    HyperParameterTuningResourceConfig: Optional[HyperParameterTuningResourceConfigUnion] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfig] = None
    RetryStrategy: Optional[RetryStrategy] = None
    Environment: Optional[Dict[str, str]] = None


class AlgorithmValidationProfile(BaseValidatorModel):
    ProfileName: str
    TrainingJobDefinition: TrainingJobDefinition
    TransformJobDefinition: Optional[TransformJobDefinition] = None


class UpdateModelPackageInput(BaseValidatorModel):
    ModelPackageArn: str
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ApprovalDescription: Optional[str] = None
    CustomerMetadataProperties: Optional[Dict[str, str]] = None
    CustomerMetadataPropertiesToRemove: Optional[List[str]] = None
    AdditionalInferenceSpecificationsToAdd: Optional[List[AdditionalInferenceSpecificationDefinitionUnion]] = None
    InferenceSpecification: Optional[InferenceSpecificationUnion] = None
    SourceUri: Optional[str] = None
    ModelCard: Optional[ModelPackageModelCard] = None
    ModelLifeCycle: Optional[ModelLifeCycle] = None
    ClientToken: Optional[str] = None


class ModelDashboardModel(BaseValidatorModel):
    Model: Optional[Model] = None
    Endpoints: Optional[List[ModelDashboardEndpoint]] = None
    LastBatchTransformJob: Optional[TransformJob] = None
    MonitoringSchedules: Optional[List[ModelDashboardMonitoringSchedule]] = None
    ModelCard: Optional[ModelDashboardModelCard] = None


class Endpoint(BaseValidatorModel):
    EndpointName: str
    EndpointArn: str
    EndpointConfigName: str
    EndpointStatus: EndpointStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    ProductionVariants: Optional[List[ProductionVariantSummary]] = None
    DataCaptureConfig: Optional[DataCaptureConfigSummary] = None
    FailureReason: Optional[str] = None
    MonitoringSchedules: Optional[List[MonitoringSchedule]] = None
    Tags: Optional[List[Tag]] = None
    ShadowProductionVariants: Optional[List[ProductionVariantSummary]] = None


class CreateMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigUnion
    Tags: Optional[List[Tag]] = None


class UpdateMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigUnion


class CreateModelPackageInput(BaseValidatorModel):
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageDescription: Optional[str] = None
    InferenceSpecification: Optional[InferenceSpecificationUnion] = None
    ValidationSpecification: Optional[ModelPackageValidationSpecificationUnion] = None
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecificationUnion] = None
    CertifyForMarketplace: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    MetadataProperties: Optional[MetadataProperties] = None
    ModelMetrics: Optional[ModelMetrics] = None
    ClientToken: Optional[str] = None
    Domain: Optional[str] = None
    Task: Optional[str] = None
    SamplePayloadUrl: Optional[str] = None
    CustomerMetadataProperties: Optional[Dict[str, str]] = None
    DriftCheckBaselines: Optional[DriftCheckBaselines] = None
    AdditionalInferenceSpecifications: Optional[List[AdditionalInferenceSpecificationDefinitionUnion]] = None
    SkipModelValidation: Optional[SkipModelValidationType] = None
    SourceUri: Optional[str] = None
    SecurityConfig: Optional[ModelPackageSecurityConfig] = None
    ModelCard: Optional[ModelPackageModelCard] = None
    ModelLifeCycle: Optional[ModelLifeCycle] = None

HyperParameterTrainingJobDefinitionUnion = Union[HyperParameterTrainingJobDefinition, HyperParameterTrainingJobDefinitionOutput]


class AlgorithmValidationSpecification(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[AlgorithmValidationProfile]


class SearchRecord(BaseValidatorModel):
    TrainingJob: Optional[TrainingJob] = None
    Experiment: Optional[Experiment] = None
    Trial: Optional[Trial] = None
    TrialComponent: Optional[TrialComponent] = None
    Endpoint: Optional[Endpoint] = None
    ModelPackage: Optional[ModelPackage] = None
    ModelPackageGroup: Optional[ModelPackageGroup] = None
    Pipeline: Optional[Pipeline] = None
    PipelineExecution: Optional[PipelineExecution] = None
    FeatureGroup: Optional[FeatureGroup] = None
    FeatureMetadata: Optional[FeatureMetadata] = None
    Project: Optional[Project] = None
    HyperParameterTuningJob: Optional[HyperParameterTuningJobSearchEntity] = None
    ModelCard: Optional[ModelCard] = None
    Model: Optional[ModelDashboardModel] = None


class CreateHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfigUnion
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinitionUnion] = None
    TrainingJobDefinitions: Optional[List[HyperParameterTrainingJobDefinitionUnion]] = None
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    Autotune: Optional[Autotune] = None

AlgorithmValidationSpecificationUnion = Union[AlgorithmValidationSpecification, AlgorithmValidationSpecificationOutput]


class SearchResponse(BaseValidatorModel):
    Results: List[SearchRecord]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateAlgorithmInput(BaseValidatorModel):
    AlgorithmName: str
    TrainingSpecification: TrainingSpecificationUnion
    AlgorithmDescription: Optional[str] = None
    InferenceSpecification: Optional[InferenceSpecificationUnion] = None
    ValidationSpecification: Optional[AlgorithmValidationSpecificationUnion] = None
    CertifyForMarketplace: Optional[bool] = None
    Tags: Optional[List[Tag]] = None