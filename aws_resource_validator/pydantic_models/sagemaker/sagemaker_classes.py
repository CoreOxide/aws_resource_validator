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


# This class is the input for the 'add_association' function.
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


# This class is the input for the 'associate_trial_component' function.
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


# This class is the input for the 'batch_delete_cluster_nodes' function.
class BatchDeleteClusterNodesRequest(BaseValidatorModel):
    ClusterName: str
    NodeIds: List[str]


class BatchDescribeModelPackageError(BaseValidatorModel):
    ErrorCode: str
    ErrorResponse: str


# This class is the input for the 'batch_describe_model_package' function.
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


# This class is the input for the 'create_image_version' function.
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


# This class is the input for the 'create_partner_app_presigned_url' function.
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


# This class is the input for the 'create_presigned_domain_url' function.
class CreatePresignedDomainUrlRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    SessionExpirationDurationInSeconds: Optional[int] = None
    ExpiresInSeconds: Optional[int] = None
    SpaceName: Optional[str] = None
    LandingUri: Optional[str] = None


# This class is the input for the 'create_presigned_mlflow_tracking_server_url' function.
class CreatePresignedMlflowTrackingServerUrlRequest(BaseValidatorModel):
    TrackingServerName: str
    ExpiresInSeconds: Optional[int] = None
    SessionExpirationDurationInSeconds: Optional[int] = None


# This class is the input for the 'create_presigned_notebook_instance_url' function.
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


# This class is the input for the 'delete_action' function.
class DeleteActionRequest(BaseValidatorModel):
    ActionName: str


# This class is the input for the 'delete_algorithm' function.
class DeleteAlgorithmInput(BaseValidatorModel):
    AlgorithmName: str


# This class is the input for the 'delete_app_image_config' function.
class DeleteAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str


# This class is the input for the 'delete_app' function.
class DeleteAppRequest(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None


# This class is the input for the 'delete_association' function.
class DeleteAssociationRequest(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str


# This class is the input for the 'delete_cluster' function.
class DeleteClusterRequest(BaseValidatorModel):
    ClusterName: str


# This class is the input for the 'delete_cluster_scheduler_config' function.
class DeleteClusterSchedulerConfigRequest(BaseValidatorModel):
    ClusterSchedulerConfigId: str


# This class is the input for the 'delete_code_repository' function.
class DeleteCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str


# This class is the input for the 'delete_compilation_job' function.
class DeleteCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str


# This class is the input for the 'delete_compute_quota' function.
class DeleteComputeQuotaRequest(BaseValidatorModel):
    ComputeQuotaId: str


# This class is the input for the 'delete_context' function.
class DeleteContextRequest(BaseValidatorModel):
    ContextName: str


# This class is the input for the 'delete_data_quality_job_definition' function.
class DeleteDataQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


# This class is the input for the 'delete_device_fleet' function.
class DeleteDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str


class RetentionPolicy(BaseValidatorModel):
    HomeEfsFileSystem: Optional[RetentionTypeType] = None


# This class is the input for the 'delete_edge_deployment_plan' function.
class DeleteEdgeDeploymentPlanRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str


# This class is the input for the 'delete_edge_deployment_stage' function.
class DeleteEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str


# This class is the input for the 'delete_endpoint_config' function.
class DeleteEndpointConfigInput(BaseValidatorModel):
    EndpointConfigName: str


# This class is the input for the 'delete_endpoint' function.
class DeleteEndpointInput(BaseValidatorModel):
    EndpointName: str


# This class is the input for the 'delete_experiment' function.
class DeleteExperimentRequest(BaseValidatorModel):
    ExperimentName: str


# This class is the input for the 'delete_feature_group' function.
class DeleteFeatureGroupRequest(BaseValidatorModel):
    FeatureGroupName: str


class DeleteFlowDefinitionRequest(BaseValidatorModel):
    FlowDefinitionName: str


# This class is the input for the 'delete_hub_content_reference' function.
class DeleteHubContentReferenceRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str


# This class is the input for the 'delete_hub_content' function.
class DeleteHubContentRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: str


# This class is the input for the 'delete_hub' function.
class DeleteHubRequest(BaseValidatorModel):
    HubName: str


class DeleteHumanTaskUiRequest(BaseValidatorModel):
    HumanTaskUiName: str


# This class is the input for the 'delete_hyper_parameter_tuning_job' function.
class DeleteHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str


class DeleteImageRequest(BaseValidatorModel):
    ImageName: str


class DeleteImageVersionRequest(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None


# This class is the input for the 'delete_inference_component' function.
class DeleteInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str


# This class is the input for the 'delete_inference_experiment' function.
class DeleteInferenceExperimentRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_mlflow_tracking_server' function.
class DeleteMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


# This class is the input for the 'delete_model_bias_job_definition' function.
class DeleteModelBiasJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


# This class is the input for the 'delete_model_card' function.
class DeleteModelCardRequest(BaseValidatorModel):
    ModelCardName: str


# This class is the input for the 'delete_model_explainability_job_definition' function.
class DeleteModelExplainabilityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


# This class is the input for the 'delete_model' function.
class DeleteModelInput(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'delete_model_package_group' function.
class DeleteModelPackageGroupInput(BaseValidatorModel):
    ModelPackageGroupName: str


# This class is the input for the 'delete_model_package_group_policy' function.
class DeleteModelPackageGroupPolicyInput(BaseValidatorModel):
    ModelPackageGroupName: str


# This class is the input for the 'delete_model_package' function.
class DeleteModelPackageInput(BaseValidatorModel):
    ModelPackageName: str


# This class is the input for the 'delete_model_quality_job_definition' function.
class DeleteModelQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


# This class is the input for the 'delete_monitoring_schedule' function.
class DeleteMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


# This class is the input for the 'delete_notebook_instance' function.
class DeleteNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


# This class is the input for the 'delete_notebook_instance_lifecycle_config' function.
class DeleteNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str


# This class is the input for the 'delete_optimization_job' function.
class DeleteOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str


# This class is the input for the 'delete_partner_app' function.
class DeletePartnerAppRequest(BaseValidatorModel):
    Arn: str
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_pipeline' function.
class DeletePipelineRequest(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str


# This class is the input for the 'delete_project' function.
class DeleteProjectInput(BaseValidatorModel):
    ProjectName: str


# This class is the input for the 'delete_space' function.
class DeleteSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str


# This class is the input for the 'delete_studio_lifecycle_config' function.
class DeleteStudioLifecycleConfigRequest(BaseValidatorModel):
    StudioLifecycleConfigName: str


class DeleteTagsInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'delete_trial_component' function.
class DeleteTrialComponentRequest(BaseValidatorModel):
    TrialComponentName: str


# This class is the input for the 'delete_trial' function.
class DeleteTrialRequest(BaseValidatorModel):
    TrialName: str


# This class is the input for the 'delete_user_profile' function.
class DeleteUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str


class DeleteWorkforceRequest(BaseValidatorModel):
    WorkforceName: str


# This class is the input for the 'delete_workteam' function.
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


# This class is the input for the 'deregister_devices' function.
class DeregisterDevicesRequest(BaseValidatorModel):
    DeviceFleetName: str
    DeviceNames: List[str]


class DerivedInformation(BaseValidatorModel):
    DerivedDataInputConfig: Optional[str] = None


# This class is the input for the 'describe_action' function.
class DescribeActionRequest(BaseValidatorModel):
    ActionName: str


# This class is the input for the 'describe_algorithm' function.
class DescribeAlgorithmInput(BaseValidatorModel):
    AlgorithmName: str


# This class is the input for the 'describe_app_image_config' function.
class DescribeAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str


# This class is the input for the 'describe_app' function.
class DescribeAppRequest(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None


# This class is the input for the 'describe_artifact' function.
class DescribeArtifactRequest(BaseValidatorModel):
    ArtifactArn: str


# This class is the input for the 'describe_auto_ml_job' function.
class DescribeAutoMLJobRequest(BaseValidatorModel):
    AutoMLJobName: str


class ModelDeployResult(BaseValidatorModel):
    EndpointName: Optional[str] = None


# This class is the input for the 'describe_auto_ml_job_v2' function.
class DescribeAutoMLJobV2Request(BaseValidatorModel):
    AutoMLJobName: str


# This class is the input for the 'describe_cluster_node' function.
class DescribeClusterNodeRequest(BaseValidatorModel):
    ClusterName: str
    NodeId: str


# This class is the input for the 'describe_cluster' function.
class DescribeClusterRequest(BaseValidatorModel):
    ClusterName: str


# This class is the input for the 'describe_cluster_scheduler_config' function.
class DescribeClusterSchedulerConfigRequest(BaseValidatorModel):
    ClusterSchedulerConfigId: str
    ClusterSchedulerConfigVersion: Optional[int] = None


# This class is the input for the 'describe_code_repository' function.
class DescribeCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str


# This class is the input for the 'describe_compilation_job' function.
class DescribeCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str


class ModelArtifacts(BaseValidatorModel):
    S3ModelArtifacts: str


class ModelDigests(BaseValidatorModel):
    ArtifactDigest: Optional[str] = None


class NeoVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


# This class is the input for the 'describe_compute_quota' function.
class DescribeComputeQuotaRequest(BaseValidatorModel):
    ComputeQuotaId: str
    ComputeQuotaVersion: Optional[int] = None


# This class is the input for the 'describe_context' function.
class DescribeContextRequest(BaseValidatorModel):
    ContextName: str


# This class is the input for the 'describe_data_quality_job_definition' function.
class DescribeDataQualityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


# This class is the input for the 'describe_device_fleet' function.
class DescribeDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str


# This class is the input for the 'describe_device' function.
class DescribeDeviceRequest(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str
    NextToken: Optional[str] = None


class EdgeModel(BaseValidatorModel):
    ModelName: str
    ModelVersion: str
    LatestSampleTime: Optional[datetime] = None
    LatestInference: Optional[datetime] = None


# This class is the input for the 'describe_domain' function.
class DescribeDomainRequest(BaseValidatorModel):
    DomainId: str


# This class is the input for the 'describe_edge_deployment_plan' function.
class DescribeEdgeDeploymentPlanRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_edge_packaging_job' function.
class DescribeEdgePackagingJobRequest(BaseValidatorModel):
    EdgePackagingJobName: str


class EdgePresetDeploymentOutput(BaseValidatorModel):
    Type: Literal['GreengrassV2Component']
    Artifact: Optional[str] = None
    Status: Optional[EdgePresetDeploymentStatusType] = None
    StatusMessage: Optional[str] = None


# This class is the input for the 'describe_endpoint_config' function.
class DescribeEndpointConfigInput(BaseValidatorModel):
    EndpointConfigName: str


# This class is the input for the 'describe_endpoint' function.
class DescribeEndpointInput(BaseValidatorModel):
    EndpointName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_experiment' function.
class DescribeExperimentRequest(BaseValidatorModel):
    ExperimentName: str


class ExperimentSource(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None


# This class is the input for the 'describe_feature_group' function.
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


# This class is the input for the 'describe_feature_metadata' function.
class DescribeFeatureMetadataRequest(BaseValidatorModel):
    FeatureGroupName: str
    FeatureName: str


class FeatureParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'describe_flow_definition' function.
class DescribeFlowDefinitionRequest(BaseValidatorModel):
    FlowDefinitionName: str


# This class is the input for the 'describe_hub_content' function.
class DescribeHubContentRequest(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: Optional[str] = None


class HubContentDependency(BaseValidatorModel):
    DependencyOriginPath: Optional[str] = None
    DependencyCopyPath: Optional[str] = None


# This class is the input for the 'describe_hub' function.
class DescribeHubRequest(BaseValidatorModel):
    HubName: str


# This class is the input for the 'describe_human_task_ui' function.
class DescribeHumanTaskUiRequest(BaseValidatorModel):
    HumanTaskUiName: str


class UiTemplateInfo(BaseValidatorModel):
    Url: Optional[str] = None
    ContentSha256: Optional[str] = None


# This class is the input for the 'describe_hyper_parameter_tuning_job' function.
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


# This class is the input for the 'describe_image' function.
class DescribeImageRequest(BaseValidatorModel):
    ImageName: str


# This class is the input for the 'describe_image_version' function.
class DescribeImageVersionRequest(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None


# This class is the input for the 'describe_inference_component' function.
class DescribeInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str


class InferenceComponentRuntimeConfigSummary(BaseValidatorModel):
    DesiredCopyCount: Optional[int] = None
    CurrentCopyCount: Optional[int] = None


# This class is the input for the 'describe_inference_experiment' function.
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


# This class is the input for the 'describe_inference_recommendations_job' function.
class DescribeInferenceRecommendationsJobRequest(BaseValidatorModel):
    JobName: str


# This class is the input for the 'describe_labeling_job' function.
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


# This class is the input for the 'describe_lineage_group' function.
class DescribeLineageGroupRequest(BaseValidatorModel):
    LineageGroupName: str


# This class is the input for the 'describe_mlflow_tracking_server' function.
class DescribeMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


# This class is the input for the 'describe_model_bias_job_definition' function.
class DescribeModelBiasJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class ModelBiasAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None


# This class is the input for the 'describe_model_card_export_job' function.
class DescribeModelCardExportJobRequest(BaseValidatorModel):
    ModelCardExportJobArn: str


class ModelCardExportArtifacts(BaseValidatorModel):
    S3ExportArtifacts: str


# This class is the input for the 'describe_model_card' function.
class DescribeModelCardRequest(BaseValidatorModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None


# This class is the input for the 'describe_model_explainability_job_definition' function.
class DescribeModelExplainabilityJobDefinitionRequest(BaseValidatorModel):
    JobDefinitionName: str


class ModelExplainabilityAppSpecificationOutput(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None


# This class is the input for the 'describe_model' function.
class DescribeModelInput(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'describe_model_package_group' function.
class DescribeModelPackageGroupInput(BaseValidatorModel):
    ModelPackageGroupName: str


# This class is the input for the 'describe_model_package' function.
class DescribeModelPackageInput(BaseValidatorModel):
    ModelPackageName: str


# This class is the input for the 'describe_model_quality_job_definition' function.
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


# This class is the input for the 'describe_monitoring_schedule' function.
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


# This class is the input for the 'describe_notebook_instance' function.
class DescribeNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


# This class is the input for the 'describe_notebook_instance_lifecycle_config' function.
class DescribeNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str


# This class is the input for the 'describe_optimization_job' function.
class DescribeOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str


class OptimizationOutput(BaseValidatorModel):
    RecommendedInferenceImage: Optional[str] = None


class OptimizationVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


# This class is the input for the 'describe_partner_app' function.
class DescribePartnerAppRequest(BaseValidatorModel):
    Arn: str


class ErrorInfo(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None


class PartnerAppConfigOutput(BaseValidatorModel):
    AdminUsers: Optional[List[str]] = None
    Arguments: Optional[Dict[str, str]] = None


# This class is the input for the 'describe_pipeline_definition_for_execution' function.
class DescribePipelineDefinitionForExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str


# This class is the input for the 'describe_pipeline_execution' function.
class DescribePipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str


class PipelineExperimentConfig(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None


# This class is the input for the 'describe_pipeline' function.
class DescribePipelineRequest(BaseValidatorModel):
    PipelineName: str


# This class is the input for the 'describe_processing_job' function.
class DescribeProcessingJobRequest(BaseValidatorModel):
    ProcessingJobName: str


# This class is the input for the 'describe_project' function.
class DescribeProjectInput(BaseValidatorModel):
    ProjectName: str


class ServiceCatalogProvisionedProductDetails(BaseValidatorModel):
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductStatusMessage: Optional[str] = None


# This class is the input for the 'describe_space' function.
class DescribeSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str


# This class is the input for the 'describe_studio_lifecycle_config' function.
class DescribeStudioLifecycleConfigRequest(BaseValidatorModel):
    StudioLifecycleConfigName: str


# This class is the input for the 'describe_subscribed_workteam' function.
class DescribeSubscribedWorkteamRequest(BaseValidatorModel):
    WorkteamArn: str


class SubscribedWorkteam(BaseValidatorModel):
    WorkteamArn: str
    MarketplaceTitle: Optional[str] = None
    SellerName: Optional[str] = None
    MarketplaceDescription: Optional[str] = None
    ListingId: Optional[str] = None


# This class is the input for the 'describe_training_job' function.
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


# This class is the input for the 'describe_training_plan' function.
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


# This class is the input for the 'describe_transform_job' function.
class DescribeTransformJobRequest(BaseValidatorModel):
    TransformJobName: str


# This class is the input for the 'describe_trial_component' function.
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


# This class is the input for the 'describe_trial' function.
class DescribeTrialRequest(BaseValidatorModel):
    TrialName: str


class TrialSource(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None


# This class is the input for the 'describe_user_profile' function.
class DescribeUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str


# This class is the input for the 'describe_workforce' function.
class DescribeWorkforceRequest(BaseValidatorModel):
    WorkforceName: str


# This class is the input for the 'describe_workteam' function.
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


# This class is the input for the 'disassociate_trial_component' function.
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


# This class is the input for the 'get_device_fleet_report' function.
class GetDeviceFleetReportRequest(BaseValidatorModel):
    DeviceFleetName: str


# This class is the input for the 'get_lineage_group_policy' function.
class GetLineageGroupPolicyRequest(BaseValidatorModel):
    LineageGroupName: str


# This class is the input for the 'get_model_package_group_policy' function.
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


# This class is the input for the 'list_aliases' function.
class ListAliasesRequest(BaseValidatorModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_apps' function.
class ListAppsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal['CreationTime']] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None


# This class is the input for the 'list_candidates_for_auto_ml_job' function.
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


# This class is the input for the 'list_domains' function.
class ListDomainsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_inference_recommendations_job_steps' function.
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


# This class is the input for the 'list_monitoring_alerts' function.
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


# This class is the input for the 'list_partner_apps' function.
class ListPartnerAppsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PartnerAppSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[PartnerAppTypeType] = None
    Status: Optional[PartnerAppStatusType] = None
    CreationTime: Optional[datetime] = None


# This class is the input for the 'list_pipeline_execution_steps' function.
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


# This class is the input for the 'list_pipeline_parameters_for_execution' function.
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


# This class is the input for the 'list_spaces' function.
class ListSpacesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None


# This class is the input for the 'list_stage_devices' function.
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


# This class is the input for the 'list_subscribed_workteams' function.
class ListSubscribedWorkteamsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags' function.
class ListTagsInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_training_jobs_for_hyper_parameter_tuning_job' function.
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


# This class is the input for the 'list_user_profiles' function.
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


# This class is the input for the 'list_workforces' function.
class ListWorkforcesRequest(BaseValidatorModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_workteams' function.
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


# This class is the input for the 'put_model_package_group_policy' function.
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


# This class is the input for the 'send_pipeline_execution_step_failure' function.
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


# This class is the input for the 'start_edge_deployment_stage' function.
class StartEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str


# This class is the input for the 'start_inference_experiment' function.
class StartInferenceExperimentRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'start_mlflow_tracking_server' function.
class StartMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


# This class is the input for the 'start_monitoring_schedule' function.
class StartMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


# This class is the input for the 'start_notebook_instance' function.
class StartNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


# This class is the input for the 'stop_auto_ml_job' function.
class StopAutoMLJobRequest(BaseValidatorModel):
    AutoMLJobName: str


# This class is the input for the 'stop_compilation_job' function.
class StopCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str


# This class is the input for the 'stop_edge_deployment_stage' function.
class StopEdgeDeploymentStageRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str


# This class is the input for the 'stop_edge_packaging_job' function.
class StopEdgePackagingJobRequest(BaseValidatorModel):
    EdgePackagingJobName: str


# This class is the input for the 'stop_hyper_parameter_tuning_job' function.
class StopHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str


# This class is the input for the 'stop_inference_recommendations_job' function.
class StopInferenceRecommendationsJobRequest(BaseValidatorModel):
    JobName: str


# This class is the input for the 'stop_labeling_job' function.
class StopLabelingJobRequest(BaseValidatorModel):
    LabelingJobName: str


# This class is the input for the 'stop_mlflow_tracking_server' function.
class StopMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str


# This class is the input for the 'stop_monitoring_schedule' function.
class StopMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str


# This class is the input for the 'stop_notebook_instance' function.
class StopNotebookInstanceInput(BaseValidatorModel):
    NotebookInstanceName: str


# This class is the input for the 'stop_optimization_job' function.
class StopOptimizationJobRequest(BaseValidatorModel):
    OptimizationJobName: str


# This class is the input for the 'stop_pipeline_execution' function.
class StopPipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    ClientRequestToken: str


# This class is the input for the 'stop_processing_job' function.
class StopProcessingJobRequest(BaseValidatorModel):
    ProcessingJobName: str


# This class is the input for the 'stop_training_job' function.
class StopTrainingJobRequest(BaseValidatorModel):
    TrainingJobName: str


# This class is the input for the 'stop_transform_job' function.
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


# This class is the input for the 'update_action' function.
class UpdateActionRequest(BaseValidatorModel):
    ActionName: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Dict[str, str]] = None
    PropertiesToRemove: Optional[List[str]] = None


# This class is the input for the 'update_artifact' function.
class UpdateArtifactRequest(BaseValidatorModel):
    ArtifactArn: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    PropertiesToRemove: Optional[List[str]] = None


# This class is the input for the 'update_cluster_software' function.
class UpdateClusterSoftwareRequest(BaseValidatorModel):
    ClusterName: str


# This class is the input for the 'update_context' function.
class UpdateContextRequest(BaseValidatorModel):
    ContextName: str
    Description: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    PropertiesToRemove: Optional[List[str]] = None


class VariantProperty(BaseValidatorModel):
    VariantPropertyType: VariantPropertyTypeType


# This class is the input for the 'update_experiment' function.
class UpdateExperimentRequest(BaseValidatorModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_hub_content_reference' function.
class UpdateHubContentReferenceRequest(BaseValidatorModel):
    HubName: str
    HubContentName: str
    HubContentType: HubContentTypeType
    MinVersion: Optional[str] = None


# This class is the input for the 'update_hub_content' function.
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


# This class is the input for the 'update_hub' function.
class UpdateHubRequest(BaseValidatorModel):
    HubName: str
    HubDescription: Optional[str] = None
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None


# This class is the input for the 'update_image' function.
class UpdateImageRequest(BaseValidatorModel):
    ImageName: str
    DeleteProperties: Optional[List[str]] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    RoleArn: Optional[str] = None


# This class is the input for the 'update_image_version' function.
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


# This class is the input for the 'update_mlflow_tracking_server' function.
class UpdateMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str
    ArtifactStoreUri: Optional[str] = None
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None


# This class is the input for the 'update_model_card' function.
class UpdateModelCardRequest(BaseValidatorModel):
    ModelCardName: str
    Content: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None


# This class is the input for the 'update_monitoring_alert' function.
class UpdateMonitoringAlertRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    DatapointsToAlert: int
    EvaluationPeriod: int


# This class is the input for the 'update_trial' function.
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


# This class is the output for the 'add_association' function.
class AddAssociationResponse(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_trial_component' function.
class AssociateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_action' function.
class CreateActionResponse(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_algorithm' function.
class CreateAlgorithmOutput(BaseValidatorModel):
    AlgorithmArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_app_image_config' function.
class CreateAppImageConfigResponse(BaseValidatorModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_app' function.
class CreateAppResponse(BaseValidatorModel):
    AppArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_artifact' function.
class CreateArtifactResponse(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_auto_ml_job' function.
class CreateAutoMLJobResponse(BaseValidatorModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_auto_ml_job_v2' function.
class CreateAutoMLJobV2Response(BaseValidatorModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster' function.
class CreateClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster_scheduler_config' function.
class CreateClusterSchedulerConfigResponse(BaseValidatorModel):
    ClusterSchedulerConfigArn: str
    ClusterSchedulerConfigId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_code_repository' function.
class CreateCodeRepositoryOutput(BaseValidatorModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_compilation_job' function.
class CreateCompilationJobResponse(BaseValidatorModel):
    CompilationJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_compute_quota' function.
class CreateComputeQuotaResponse(BaseValidatorModel):
    ComputeQuotaArn: str
    ComputeQuotaId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_context' function.
class CreateContextResponse(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_quality_job_definition' function.
class CreateDataQualityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain' function.
class CreateDomainResponse(BaseValidatorModel):
    DomainArn: str
    DomainId: str
    Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_edge_deployment_plan' function.
class CreateEdgeDeploymentPlanResponse(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_endpoint_config' function.
class CreateEndpointConfigOutput(BaseValidatorModel):
    EndpointConfigArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_endpoint' function.
class CreateEndpointOutput(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_experiment' function.
class CreateExperimentResponse(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_feature_group' function.
class CreateFeatureGroupResponse(BaseValidatorModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_flow_definition' function.
class CreateFlowDefinitionResponse(BaseValidatorModel):
    FlowDefinitionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hub_content_reference' function.
class CreateHubContentReferenceResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hub' function.
class CreateHubResponse(BaseValidatorModel):
    HubArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_human_task_ui' function.
class CreateHumanTaskUiResponse(BaseValidatorModel):
    HumanTaskUiArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hyper_parameter_tuning_job' function.
class CreateHyperParameterTuningJobResponse(BaseValidatorModel):
    HyperParameterTuningJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_image' function.
class CreateImageResponse(BaseValidatorModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_image_version' function.
class CreateImageVersionResponse(BaseValidatorModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_inference_component' function.
class CreateInferenceComponentOutput(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_inference_experiment' function.
class CreateInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_inference_recommendations_job' function.
class CreateInferenceRecommendationsJobResponse(BaseValidatorModel):
    JobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_labeling_job' function.
class CreateLabelingJobResponse(BaseValidatorModel):
    LabelingJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_mlflow_tracking_server' function.
class CreateMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_bias_job_definition' function.
class CreateModelBiasJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_card_export_job' function.
class CreateModelCardExportJobResponse(BaseValidatorModel):
    ModelCardExportJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_card' function.
class CreateModelCardResponse(BaseValidatorModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_explainability_job_definition' function.
class CreateModelExplainabilityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model' function.
class CreateModelOutput(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_package_group' function.
class CreateModelPackageGroupOutput(BaseValidatorModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_package' function.
class CreateModelPackageOutput(BaseValidatorModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_quality_job_definition' function.
class CreateModelQualityJobDefinitionResponse(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_monitoring_schedule' function.
class CreateMonitoringScheduleResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_notebook_instance_lifecycle_config' function.
class CreateNotebookInstanceLifecycleConfigOutput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_notebook_instance' function.
class CreateNotebookInstanceOutput(BaseValidatorModel):
    NotebookInstanceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_optimization_job' function.
class CreateOptimizationJobResponse(BaseValidatorModel):
    OptimizationJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_partner_app_presigned_url' function.
class CreatePartnerAppPresignedUrlResponse(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_partner_app' function.
class CreatePartnerAppResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_pipeline' function.
class CreatePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_presigned_domain_url' function.
class CreatePresignedDomainUrlResponse(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_presigned_mlflow_tracking_server_url' function.
class CreatePresignedMlflowTrackingServerUrlResponse(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_presigned_notebook_instance_url' function.
class CreatePresignedNotebookInstanceUrlOutput(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_processing_job' function.
class CreateProcessingJobResponse(BaseValidatorModel):
    ProcessingJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_project' function.
class CreateProjectOutput(BaseValidatorModel):
    ProjectArn: str
    ProjectId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_space' function.
class CreateSpaceResponse(BaseValidatorModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_studio_lifecycle_config' function.
class CreateStudioLifecycleConfigResponse(BaseValidatorModel):
    StudioLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_training_job' function.
class CreateTrainingJobResponse(BaseValidatorModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_training_plan' function.
class CreateTrainingPlanResponse(BaseValidatorModel):
    TrainingPlanArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transform_job' function.
class CreateTransformJobResponse(BaseValidatorModel):
    TransformJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_trial_component' function.
class CreateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_trial' function.
class CreateTrialResponse(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user_profile' function.
class CreateUserProfileResponse(BaseValidatorModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workforce' function.
class CreateWorkforceResponse(BaseValidatorModel):
    WorkforceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workteam' function.
class CreateWorkteamResponse(BaseValidatorModel):
    WorkteamArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_action' function.
class DeleteActionResponse(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_artifact' function.
class DeleteArtifactResponse(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_association' function.
class DeleteAssociationResponse(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_context' function.
class DeleteContextResponse(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_experiment' function.
class DeleteExperimentResponse(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_inference_experiment' function.
class DeleteInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_mlflow_tracking_server' function.
class DeleteMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_partner_app' function.
class DeletePartnerAppResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pipeline' function.
class DeletePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_trial_component' function.
class DeleteTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_trial' function.
class DeleteTrialResponse(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_workteam' function.
class DeleteWorkteamResponse(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_image' function.
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


# This class is the output for the 'describe_image_version' function.
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


# This class is the output for the 'describe_pipeline_definition_for_execution' function.
class DescribePipelineDefinitionForExecutionResponse(BaseValidatorModel):
    PipelineDefinition: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_studio_lifecycle_config' function.
class DescribeStudioLifecycleConfigResponse(BaseValidatorModel):
    StudioLifecycleConfigArn: str
    StudioLifecycleConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_trial_component' function.
class DisassociateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_feature_metadata' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_lineage_group_policy' function.
class GetLineageGroupPolicyResponse(BaseValidatorModel):
    LineageGroupArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_model_package_group_policy' function.
class GetModelPackageGroupPolicyOutput(BaseValidatorModel):
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadata


class GetSagemakerServicecatalogPortfolioStatusOutput(BaseValidatorModel):
    Status: SagemakerServicecatalogStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_hub_content' function.
class ImportHubContentResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_aliases' function.
class ListAliasesResponse(BaseValidatorModel):
    SageMakerImageVersionAliases: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_model_package_group_policy' function.
class PutModelPackageGroupPolicyOutput(BaseValidatorModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'retry_pipeline_execution' function.
class RetryPipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_pipeline_execution_step_failure' function.
class SendPipelineExecutionStepFailureResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_pipeline_execution_step_success' function.
class SendPipelineExecutionStepSuccessResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_inference_experiment' function.
class StartInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_mlflow_tracking_server' function.
class StartMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_pipeline_execution' function.
class StartPipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_inference_experiment' function.
class StopInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_mlflow_tracking_server' function.
class StopMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_pipeline_execution' function.
class StopPipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_action' function.
class UpdateActionResponse(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_image_config' function.
class UpdateAppImageConfigResponse(BaseValidatorModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_artifact' function.
class UpdateArtifactResponse(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster' function.
class UpdateClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster_scheduler_config' function.
class UpdateClusterSchedulerConfigResponse(BaseValidatorModel):
    ClusterSchedulerConfigArn: str
    ClusterSchedulerConfigVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster_software' function.
class UpdateClusterSoftwareResponse(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_code_repository' function.
class UpdateCodeRepositoryOutput(BaseValidatorModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_compute_quota' function.
class UpdateComputeQuotaResponse(BaseValidatorModel):
    ComputeQuotaArn: str
    ComputeQuotaVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_context' function.
class UpdateContextResponse(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain' function.
class UpdateDomainResponse(BaseValidatorModel):
    DomainArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_endpoint' function.
class UpdateEndpointOutput(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_endpoint_weights_and_capacities' function.
class UpdateEndpointWeightsAndCapacitiesOutput(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_experiment' function.
class UpdateExperimentResponse(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_feature_group' function.
class UpdateFeatureGroupResponse(BaseValidatorModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_hub_content_reference' function.
class UpdateHubContentReferenceResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_hub_content' function.
class UpdateHubContentResponse(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_hub' function.
class UpdateHubResponse(BaseValidatorModel):
    HubArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_image' function.
class UpdateImageResponse(BaseValidatorModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_image_version' function.
class UpdateImageVersionResponse(BaseValidatorModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_inference_component' function.
class UpdateInferenceComponentOutput(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_inference_component_runtime_config' function.
class UpdateInferenceComponentRuntimeConfigOutput(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_inference_experiment' function.
class UpdateInferenceExperimentResponse(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_mlflow_tracking_server' function.
class UpdateMlflowTrackingServerResponse(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_model_card' function.
class UpdateModelCardResponse(BaseValidatorModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_model_package' function.
class UpdateModelPackageOutput(BaseValidatorModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_monitoring_alert' function.
class UpdateMonitoringAlertResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    MonitoringAlertName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_monitoring_schedule' function.
class UpdateMonitoringScheduleResponse(BaseValidatorModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_partner_app' function.
class UpdatePartnerAppResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pipeline_execution' function.
class UpdatePipelineExecutionResponse(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pipeline' function.
class UpdatePipelineResponse(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project' function.
class UpdateProjectOutput(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_space' function.
class UpdateSpaceResponse(BaseValidatorModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_training_job' function.
class UpdateTrainingJobResponse(BaseValidatorModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trial_component' function.
class UpdateTrialComponentResponse(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trial' function.
class UpdateTrialResponse(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user_profile' function.
class UpdateUserProfileResponse(BaseValidatorModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_tags' function.
class AddTagsInput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'add_tags' function.
class AddTagsOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_experiment' function.
class CreateExperimentRequest(BaseValidatorModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_hub_content_reference' function.
class CreateHubContentReferenceRequest(BaseValidatorModel):
    HubName: str
    SageMakerPublicHubContentArn: str
    HubContentName: Optional[str] = None
    MinVersion: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_image' function.
class CreateImageRequest(BaseValidatorModel):
    ImageName: str
    RoleArn: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_mlflow_tracking_server' function.
class CreateMlflowTrackingServerRequest(BaseValidatorModel):
    TrackingServerName: str
    ArtifactStoreUri: str
    RoleArn: str
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    MlflowVersion: Optional[str] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_model_package_group' function.
class CreateModelPackageGroupInput(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_studio_lifecycle_config' function.
class CreateStudioLifecycleConfigRequest(BaseValidatorModel):
    StudioLifecycleConfigName: str
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_training_plan' function.
class CreateTrainingPlanRequest(BaseValidatorModel):
    TrainingPlanName: str
    TrainingPlanOfferingId: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'import_hub_content' function.
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


# This class is the output for the 'list_tags' function.
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


# This class is the output for the 'list_algorithms' function.
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


# This class is the input for the 'create_app' function.
class CreateAppRequest(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ResourceSpec: Optional[ResourceSpec] = None


# This class is the output for the 'describe_app' function.
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


# This class is the output for the 'batch_delete_cluster_nodes' function.
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


# This class is the input for the 'send_pipeline_execution_step_success' function.
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


# This class is the output for the 'list_cluster_scheduler_configs' function.
class ListClusterSchedulerConfigsResponse(BaseValidatorModel):
    ClusterSchedulerConfigSummaries: List[ClusterSchedulerConfigSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_clusters' function.
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


# This class is the input for the 'create_code_repository' function.
class CreateCodeRepositoryInput(BaseValidatorModel):
    CodeRepositoryName: str
    GitConfig: GitConfig
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_code_repository' function.
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


# This class is the output for the 'list_compilation_jobs' function.
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


# This class is the input for the 'create_context' function.
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


# This class is the input for the 'create_action' function.
class CreateActionRequest(BaseValidatorModel):
    ActionName: str
    Source: ActionSource
    ActionType: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Dict[str, str]] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_trial' function.
class CreateTrialRequest(BaseValidatorModel):
    TrialName: str
    ExperimentName: str
    DisplayName: Optional[str] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_device_fleet' function.
class CreateDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfig
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EnableIotRoleAlias: Optional[bool] = None


# This class is the input for the 'create_edge_packaging_job' function.
class CreateEdgePackagingJobRequest(BaseValidatorModel):
    EdgePackagingJobName: str
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: EdgeOutputConfig
    ResourceKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_device_fleet' function.
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


# This class is the input for the 'update_device_fleet' function.
class UpdateDeviceFleetRequest(BaseValidatorModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfig
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    EnableIotRoleAlias: Optional[bool] = None


# This class is the input for the 'create_hub' function.
class CreateHubRequest(BaseValidatorModel):
    HubName: str
    HubDescription: str
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None
    S3StorageConfig: Optional[HubS3StorageConfig] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_hub' function.
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


# This class is the input for the 'create_human_task_ui' function.
class CreateHumanTaskUiRequest(BaseValidatorModel):
    HumanTaskUiName: str
    UiTemplate: UiTemplate
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_inference_component_runtime_config' function.
class UpdateInferenceComponentRuntimeConfigInput(BaseValidatorModel):
    InferenceComponentName: str
    DesiredRuntimeConfig: InferenceComponentRuntimeConfig


# This class is the input for the 'create_model_card_export_job' function.
class CreateModelCardExportJobRequest(BaseValidatorModel):
    ModelCardName: str
    ModelCardExportJobName: str
    OutputConfig: ModelCardExportOutputConfig
    ModelCardVersion: Optional[int] = None


# This class is the input for the 'create_model_card' function.
class CreateModelCardRequest(BaseValidatorModel):
    ModelCardName: str
    Content: str
    ModelCardStatus: ModelCardStatusType
    SecurityConfig: Optional[ModelCardSecurityConfig] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_notebook_instance' function.
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


# This class is the output for the 'describe_notebook_instance' function.
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


# This class is the input for the 'create_notebook_instance_lifecycle_config' function.
class CreateNotebookInstanceLifecycleConfigInput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[List[NotebookInstanceLifecycleHook]] = None
    OnStart: Optional[List[NotebookInstanceLifecycleHook]] = None


# This class is the output for the 'describe_notebook_instance_lifecycle_config' function.
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


# This class is the input for the 'retry_pipeline_execution' function.
class RetryPipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    ClientRequestToken: str
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


# This class is the input for the 'update_pipeline_execution' function.
class UpdatePipelineExecutionRequest(BaseValidatorModel):
    PipelineExecutionArn: str
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


# This class is the input for the 'create_pipeline' function.
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


# This class is the input for the 'update_pipeline' function.
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


# This class is the input for the 'list_actions' function.
class ListActionsRequest(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_algorithms' function.
class ListAlgorithmsInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_app_image_configs' function.
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


# This class is the input for the 'list_artifacts' function.
class ListArtifactsRequest(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[Literal['CreationTime']] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_associations' function.
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


# This class is the input for the 'list_auto_ml_jobs' function.
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


# This class is the input for the 'list_cluster_nodes' function.
class ListClusterNodesRequest(BaseValidatorModel):
    ClusterName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    InstanceGroupNameContains: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_cluster_scheduler_configs' function.
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


# This class is the input for the 'list_clusters' function.
class ListClustersRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    TrainingPlanArn: Optional[str] = None


# This class is the input for the 'list_code_repositories' function.
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


# This class is the input for the 'list_compilation_jobs' function.
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


# This class is the input for the 'list_compute_quotas' function.
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


# This class is the input for the 'list_contexts' function.
class ListContextsRequest(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_data_quality_job_definitions' function.
class ListDataQualityJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


# This class is the input for the 'list_device_fleets' function.
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


# This class is the input for the 'list_devices' function.
class ListDevicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LatestHeartbeatAfter: Optional[Timestamp] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None


# This class is the input for the 'list_edge_deployment_plans' function.
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


# This class is the input for the 'list_edge_packaging_jobs' function.
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


# This class is the input for the 'list_endpoint_configs' function.
class ListEndpointConfigsInput(BaseValidatorModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


# This class is the input for the 'list_endpoints' function.
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


# This class is the input for the 'list_experiments' function.
class ListExperimentsRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_feature_groups' function.
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


# This class is the input for the 'list_flow_definitions' function.
class ListFlowDefinitionsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_hub_content_versions' function.
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


# This class is the input for the 'list_hub_contents' function.
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


# This class is the input for the 'list_hubs' function.
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


# This class is the input for the 'list_human_task_uis' function.
class ListHumanTaskUisRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_hyper_parameter_tuning_jobs' function.
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


# This class is the input for the 'list_image_versions' function.
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


# This class is the input for the 'list_images' function.
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


# This class is the input for the 'list_inference_components' function.
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


# This class is the input for the 'list_inference_experiments' function.
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


# This class is the input for the 'list_inference_recommendations_jobs' function.
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


# This class is the input for the 'list_labeling_jobs_for_workteam' function.
class ListLabelingJobsForWorkteamRequest(BaseValidatorModel):
    WorkteamArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal['CreationTime']] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_labeling_jobs' function.
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


# This class is the input for the 'list_lineage_groups' function.
class ListLineageGroupsRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_mlflow_tracking_servers' function.
class ListMlflowTrackingServersRequest(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_model_bias_job_definitions' function.
class ListModelBiasJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


# This class is the input for the 'list_model_card_export_jobs' function.
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


# This class is the input for the 'list_model_card_versions' function.
class ListModelCardVersionsRequest(BaseValidatorModel):
    ModelCardName: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[Literal['Version']] = None
    SortOrder: Optional[ModelCardSortOrderType] = None


# This class is the input for the 'list_model_cards' function.
class ListModelCardsRequest(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None


# This class is the input for the 'list_model_explainability_job_definitions' function.
class ListModelExplainabilityJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


# This class is the input for the 'list_model_package_groups' function.
class ListModelPackageGroupsInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None


# This class is the input for the 'list_model_packages' function.
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


# This class is the input for the 'list_model_quality_job_definitions' function.
class ListModelQualityJobDefinitionsRequest(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


# This class is the input for the 'list_models' function.
class ListModelsInput(BaseValidatorModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


# This class is the input for the 'list_monitoring_alert_history' function.
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


# This class is the input for the 'list_monitoring_executions' function.
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


# This class is the input for the 'list_monitoring_schedules' function.
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


# This class is the input for the 'list_notebook_instance_lifecycle_configs' function.
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


# This class is the input for the 'list_notebook_instances' function.
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


# This class is the input for the 'list_optimization_jobs' function.
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


# This class is the input for the 'list_pipeline_executions' function.
class ListPipelineExecutionsRequest(BaseValidatorModel):
    PipelineName: str
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_pipelines' function.
class ListPipelinesRequest(BaseValidatorModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_processing_jobs' function.
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


# This class is the input for the 'list_projects' function.
class ListProjectsInput(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ProjectSortByType] = None
    SortOrder: Optional[ProjectSortOrderType] = None


# This class is the input for the 'list_resource_catalogs' function.
class ListResourceCatalogsRequest(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal['CreationTime']] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_studio_lifecycle_configs' function.
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


# This class is the input for the 'list_training_jobs' function.
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


# This class is the input for the 'list_transform_jobs' function.
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


# This class is the input for the 'list_trial_components' function.
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


# This class is the input for the 'list_trials' function.
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


# This class is the input for the 'search_training_plan_offerings' function.
class SearchTrainingPlanOfferingsRequest(BaseValidatorModel):
    InstanceType: ReservedCapacityInstanceTypeType
    InstanceCount: int
    TargetResources: List[SageMakerResourceNameType]
    StartTimeAfter: Optional[Timestamp] = None
    EndTimeBefore: Optional[Timestamp] = None
    DurationHours: Optional[int] = None


# This class is the input for the 'create_trial_component' function.
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


# This class is the input for the 'update_trial_component' function.
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


# This class is the input for the 'delete_domain' function.
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


# This class is the output for the 'describe_device' function.
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


# This class is the output for the 'describe_edge_packaging_job' function.
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


# This class is the output for the 'describe_feature_metadata' function.
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


# This class is the input for the 'update_feature_metadata' function.
class UpdateFeatureMetadataRequest(BaseValidatorModel):
    FeatureGroupName: str
    FeatureName: str
    Description: Optional[str] = None
    ParameterAdditions: Optional[List[FeatureParameter]] = None
    ParameterRemovals: Optional[List[str]] = None


# This class is the output for the 'describe_hub_content' function.
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


# This class is the output for the 'describe_human_task_ui' function.
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


# This class is the output for the 'describe_model_card_export_job' function.
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


# This class is the output for the 'list_monitoring_executions' function.
class ListMonitoringExecutionsResponse(BaseValidatorModel):
    MonitoringExecutionSummaries: List[MonitoringExecutionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_partner_app' function.
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


# This class is the output for the 'describe_subscribed_workteam' function.
class DescribeSubscribedWorkteamResponse(BaseValidatorModel):
    SubscribedWorkteam: SubscribedWorkteam
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_subscribed_workteams' function.
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


# This class is the output for the 'describe_training_plan' function.
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


# This class is the output for the 'list_stage_devices' function.
class ListStageDevicesResponse(BaseValidatorModel):
    DeviceDeploymentSummaries: List[DeviceDeploymentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_device_fleets' function.
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


# This class is the input for the 'register_devices' function.
class RegisterDevicesRequest(BaseValidatorModel):
    DeviceFleetName: str
    Devices: List[Device]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_devices' function.
class UpdateDevicesRequest(BaseValidatorModel):
    DeviceFleetName: str
    Devices: List[Device]

DockerSettingsUnion = Union[DockerSettings, DockerSettingsOutput]


# This class is the output for the 'list_domains' function.
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


# This class is the output for the 'list_edge_deployment_plans' function.
class ListEdgeDeploymentPlansResponse(BaseValidatorModel):
    EdgeDeploymentPlanSummaries: List[EdgeDeploymentPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_device_fleet_report' function.
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


# This class is the output for the 'list_edge_packaging_jobs' function.
class ListEdgePackagingJobsResponse(BaseValidatorModel):
    EdgePackagingJobSummaries: List[EdgePackagingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_endpoint_configs' function.
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


# This class is the output for the 'list_endpoints' function.
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


# This class is the output for the 'list_flow_definitions' function.
class ListFlowDefinitionsResponse(BaseValidatorModel):
    FlowDefinitionSummaries: List[FlowDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'get_scaling_configuration_recommendation' function.
class GetScalingConfigurationRecommendationRequest(BaseValidatorModel):
    InferenceRecommendationsJobName: str
    RecommendationId: Optional[str] = None
    EndpointName: Optional[str] = None
    TargetCpuUtilizationPerCore: Optional[int] = None
    ScalingPolicyObjective: Optional[ScalingPolicyObjective] = None


# This class is the output for the 'get_search_suggestions' function.
class GetSearchSuggestionsResponse(BaseValidatorModel):
    PropertyNameSuggestions: List[PropertyNameSuggestion]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_code_repository' function.
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


# This class is the output for the 'list_hub_content_versions' function.
class ListHubContentVersionsResponse(BaseValidatorModel):
    HubContentSummaries: List[HubContentInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_hub_contents' function.
class ListHubContentsResponse(BaseValidatorModel):
    HubContentSummaries: List[HubContentInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_hubs' function.
class ListHubsResponse(BaseValidatorModel):
    HubSummaries: List[HubInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HumanLoopActivationConfig(BaseValidatorModel):
    HumanLoopActivationConditionsConfig: HumanLoopActivationConditionsConfig


# This class is the output for the 'list_human_task_uis' function.
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


# This class is the output for the 'list_images' function.
class ListImagesResponse(BaseValidatorModel):
    Images: List[Image]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_image_versions' function.
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


# This class is the output for the 'list_inference_components' function.
class ListInferenceComponentsOutput(BaseValidatorModel):
    InferenceComponents: List[InferenceComponentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_inference_recommendations_jobs' function.
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


# This class is the output for the 'list_lineage_groups' function.
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


# This class is the output for the 'list_data_quality_job_definitions' function.
class ListDataQualityJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_bias_job_definitions' function.
class ListModelBiasJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_explainability_job_definitions' function.
class ListModelExplainabilityJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_quality_job_definitions' function.
class ListModelQualityJobDefinitionsResponse(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_mlflow_tracking_servers' function.
class ListMlflowTrackingServersResponse(BaseValidatorModel):
    TrackingServerSummaries: List[TrackingServerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_card_export_jobs' function.
class ListModelCardExportJobsResponse(BaseValidatorModel):
    ModelCardExportJobSummaries: List[ModelCardExportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_card_versions' function.
class ListModelCardVersionsResponse(BaseValidatorModel):
    ModelCardVersionSummaryList: List[ModelCardVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_cards' function.
class ListModelCardsResponse(BaseValidatorModel):
    ModelCardSummaries: List[ModelCardSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_metadata' function.
class ListModelMetadataResponse(BaseValidatorModel):
    ModelMetadataSummaries: List[ModelMetadataSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_package_groups' function.
class ListModelPackageGroupsOutput(BaseValidatorModel):
    ModelPackageGroupSummaryList: List[ModelPackageGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_model_packages' function.
class ListModelPackagesOutput(BaseValidatorModel):
    ModelPackageSummaryList: List[ModelPackageSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_models' function.
class ListModelsOutput(BaseValidatorModel):
    Models: List[ModelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_monitoring_alert_history' function.
class ListMonitoringAlertHistoryResponse(BaseValidatorModel):
    MonitoringAlertHistory: List[MonitoringAlertHistorySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_monitoring_schedules' function.
class ListMonitoringSchedulesResponse(BaseValidatorModel):
    MonitoringScheduleSummaries: List[MonitoringScheduleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_notebook_instance_lifecycle_configs' function.
class ListNotebookInstanceLifecycleConfigsOutput(BaseValidatorModel):
    NotebookInstanceLifecycleConfigs: List[NotebookInstanceLifecycleConfigSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_notebook_instances' function.
class ListNotebookInstancesOutput(BaseValidatorModel):
    NotebookInstances: List[NotebookInstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_optimization_jobs' function.
class ListOptimizationJobsResponse(BaseValidatorModel):
    OptimizationJobSummaries: List[OptimizationJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_partner_apps' function.
class ListPartnerAppsResponse(BaseValidatorModel):
    Summaries: List[PartnerAppSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pipeline_executions' function.
class ListPipelineExecutionsResponse(BaseValidatorModel):
    PipelineExecutionSummaries: List[PipelineExecutionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pipeline_parameters_for_execution' function.
class ListPipelineParametersForExecutionResponse(BaseValidatorModel):
    PipelineParameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pipelines' function.
class ListPipelinesResponse(BaseValidatorModel):
    PipelineSummaries: List[PipelineSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_processing_jobs' function.
class ListProcessingJobsResponse(BaseValidatorModel):
    ProcessingJobSummaries: List[ProcessingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_projects' function.
class ListProjectsOutput(BaseValidatorModel):
    ProjectSummaryList: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_resource_catalogs' function.
class ListResourceCatalogsResponse(BaseValidatorModel):
    ResourceCatalogs: List[ResourceCatalog]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_studio_lifecycle_configs' function.
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


# This class is the input for the 'list_training_plans' function.
class ListTrainingPlansRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTimeAfter: Optional[Timestamp] = None
    StartTimeBefore: Optional[Timestamp] = None
    SortBy: Optional[TrainingPlanSortByType] = None
    SortOrder: Optional[TrainingPlanSortOrderType] = None
    Filters: Optional[List[TrainingPlanFilter]] = None


# This class is the output for the 'list_transform_jobs' function.
class ListTransformJobsResponse(BaseValidatorModel):
    TransformJobSummaries: List[TransformJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_user_profiles' function.
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


# This class is the output for the 'query_lineage' function.
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


# This class is the input for the 'render_ui_template' function.
class RenderUiTemplateRequest(BaseValidatorModel):
    Task: RenderableTask
    RoleArn: str
    UiTemplate: Optional[UiTemplate] = None
    HumanTaskUiArn: Optional[str] = None


# This class is the output for the 'render_ui_template' function.
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


# This class is the output for the 'list_actions' function.
class ListActionsResponse(BaseValidatorModel):
    ActionSummaries: List[ActionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

HyperParameterAlgorithmSpecificationUnion = Union[HyperParameterAlgorithmSpecification, HyperParameterAlgorithmSpecificationOutput]


# This class is the output for the 'list_apps' function.
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


# This class is the output for the 'list_auto_ml_jobs' function.
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


# This class is the output for the 'list_cluster_nodes' function.
class ListClusterNodesResponse(BaseValidatorModel):
    NextToken: str
    ClusterNodeSummaries: List[ClusterNodeSummary]
    ResponseMetadata: ResponseMetadata

CodeEditorAppImageConfigUnion = Union[CodeEditorAppImageConfig, CodeEditorAppImageConfigOutput]

JupyterLabAppImageConfigUnion = Union[JupyterLabAppImageConfig, JupyterLabAppImageConfigOutput]


# This class is the output for the 'list_code_repositories' function.
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


# This class is the output for the 'list_contexts' function.
class ListContextsResponse(BaseValidatorModel):
    ContextSummaries: List[ContextSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

InferenceExperimentScheduleUnion = Union[InferenceExperimentSchedule, InferenceExperimentScheduleOutput]


# This class is the input for the 'query_lineage' function.
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


# This class is the output for the 'describe_edge_deployment_plan' function.
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


# This class is the output for the 'list_experiments' function.
class ListExperimentsResponse(BaseValidatorModel):
    ExperimentSummaries: List[ExperimentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_feature_groups' function.
class ListFeatureGroupsResponse(BaseValidatorModel):
    FeatureGroupSummaries: List[FeatureGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_inference_experiments' function.
class ListInferenceExperimentsResponse(BaseValidatorModel):
    InferenceExperiments: List[InferenceExperimentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_training_jobs' function.
class ListTrainingJobsResponse(BaseValidatorModel):
    TrainingJobSummaries: List[TrainingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_training_plans' function.
class ListTrainingPlansResponse(BaseValidatorModel):
    TrainingPlanSummaries: List[TrainingPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_trials' function.
class ListTrialsResponse(BaseValidatorModel):
    TrialSummaries: List[TrialSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'update_endpoint_weights_and_capacities' function.
class UpdateEndpointWeightsAndCapacitiesInput(BaseValidatorModel):
    EndpointName: str
    DesiredWeightsAndCapacities: List[DesiredWeightAndCapacity]


class DeploymentStage(BaseValidatorModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigUnion
    DeploymentConfig: Optional[EdgeDeploymentConfig] = None


# This class is the output for the 'list_devices' function.
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


# This class is the output for the 'list_training_jobs_for_hyper_parameter_tuning_job' function.
class ListTrainingJobsForHyperParameterTuningJobResponse(BaseValidatorModel):
    TrainingJobSummaries: List[HyperParameterTrainingJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

HyperParameterTuningResourceConfigUnion = Union[HyperParameterTuningResourceConfig, HyperParameterTuningResourceConfigOutput]


# This class is the output for the 'list_hyper_parameter_tuning_jobs' function.
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


# This class is the output for the 'describe_action' function.
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


# This class is the output for the 'describe_artifact' function.
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


# This class is the output for the 'describe_compute_quota' function.
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


# This class is the output for the 'describe_context' function.
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


# This class is the output for the 'describe_experiment' function.
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


# This class is the output for the 'describe_lineage_group' function.
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


# This class is the output for the 'describe_mlflow_tracking_server' function.
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


# This class is the output for the 'describe_model_card' function.
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


# This class is the output for the 'describe_model_package_group' function.
class DescribeModelPackageGroupOutput(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    ModelPackageGroupDescription: str
    CreationTime: datetime
    CreatedBy: UserContext
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_pipeline' function.
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


# This class is the output for the 'describe_trial_component' function.
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


# This class is the output for the 'describe_trial' function.
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


# This class is the input for the 'create_inference_component' function.
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


# This class is the output for the 'describe_app_image_config' function.
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


# This class is the output for the 'list_labeling_jobs_for_workteam' function.
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


# This class is the input for the 'list_model_metadata' function.
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


# This class is the input for the 'create_compilation_job' function.
class CreateCompilationJobRequest(BaseValidatorModel):
    CompilationJobName: str
    RoleArn: str
    OutputConfig: OutputConfig
    StoppingCondition: StoppingCondition
    ModelPackageVersionArn: Optional[str] = None
    InputConfig: Optional[InputConfig] = None
    VpcConfig: Optional[NeoVpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_compilation_job' function.
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


# This class is the input for the 'create_partner_app' function.
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


# This class is the input for the 'update_partner_app' function.
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


# This class is the output for the 'describe_cluster_scheduler_config' function.
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


# This class is the input for the 'update_training_job' function.
class UpdateTrainingJobRequest(BaseValidatorModel):
    TrainingJobName: str
    ProfilerConfig: Optional[ProfilerConfigForUpdate] = None
    ProfilerRuleConfigurations: Optional[List[ProfilerRuleConfigurationUnion]] = None
    ResourceConfig: Optional[ResourceConfigForUpdate] = None
    RemoteDebugConfig: Optional[RemoteDebugConfigForUpdate] = None


# This class is the input for the 'get_search_suggestions' function.
class GetSearchSuggestionsRequest(BaseValidatorModel):
    Resource: ResourceTypeType
    SuggestionQuery: Optional[SuggestionQuery] = None


# This class is the output for the 'describe_project' function.
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


# This class is the input for the 'update_project' function.
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


# This class is the output for the 'search_training_plan_offerings' function.
class SearchTrainingPlanOfferingsResponse(BaseValidatorModel):
    TrainingPlanOfferings: List[TrainingPlanOffering]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_pipeline_execution' function.
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


# This class is the input for the 'create_workforce' function.
class CreateWorkforceRequest(BaseValidatorModel):
    WorkforceName: str
    CognitoConfig: Optional[CognitoConfig] = None
    OidcConfig: Optional[OidcConfig] = None
    SourceIpConfig: Optional[SourceIpConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequest] = None


# This class is the input for the 'update_workforce' function.
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


# This class is the output for the 'describe_workforce' function.
class DescribeWorkforceResponse(BaseValidatorModel):
    Workforce: Workforce
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_workforces' function.
class ListWorkforcesResponse(BaseValidatorModel):
    Workforces: List[Workforce]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_workforce' function.
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


# This class is the output for the 'list_artifacts' function.
class ListArtifactsResponse(BaseValidatorModel):
    ArtifactSummaries: List[ArtifactSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_artifact' function.
class CreateArtifactRequest(BaseValidatorModel):
    Source: ArtifactSourceUnion
    ArtifactType: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    MetadataProperties: Optional[MetadataProperties] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'delete_artifact' function.
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


# This class is the output for the 'describe_auto_ml_job' function.
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


# This class is the output for the 'list_candidates_for_auto_ml_job' function.
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


# This class is the output for the 'describe_cluster' function.
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


# This class is the input for the 'create_cluster' function.
class CreateClusterRequest(BaseValidatorModel):
    ClusterName: str
    InstanceGroups: List[ClusterInstanceGroupSpecification]
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    Orchestrator: Optional[ClusterOrchestrator] = None
    NodeRecovery: Optional[ClusterNodeRecoveryType] = None


# This class is the input for the 'update_cluster' function.
class UpdateClusterRequest(BaseValidatorModel):
    ClusterName: str
    InstanceGroups: List[ClusterInstanceGroupSpecification]
    NodeRecovery: Optional[ClusterNodeRecoveryType] = None
    InstanceGroupsToDelete: Optional[List[str]] = None


# This class is the output for the 'describe_cluster_node' function.
class DescribeClusterNodeResponse(BaseValidatorModel):
    NodeDetails: ClusterNodeDetails
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_feature_group' function.
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


# This class is the output for the 'describe_feature_group' function.
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


# This class is the input for the 'update_feature_group' function.
class UpdateFeatureGroupRequest(BaseValidatorModel):
    FeatureGroupName: str
    FeatureAdditions: Optional[List[FeatureDefinition]] = None
    OnlineStoreConfig: Optional[OnlineStoreConfigUpdate] = None
    ThroughputConfig: Optional[ThroughputConfigUpdate] = None


# This class is the output for the 'list_compute_quotas' function.
class ListComputeQuotasResponse(BaseValidatorModel):
    ComputeQuotaSummaries: List[ComputeQuotaSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_compute_quota' function.
class CreateComputeQuotaRequest(BaseValidatorModel):
    Name: str
    ClusterArn: str
    ComputeQuotaConfig: ComputeQuotaConfigUnion
    ComputeQuotaTarget: ComputeQuotaTarget
    Description: Optional[str] = None
    ActivationState: Optional[ActivationStateType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_compute_quota' function.
class UpdateComputeQuotaRequest(BaseValidatorModel):
    ComputeQuotaId: str
    TargetVersion: int
    ComputeQuotaConfig: Optional[ComputeQuotaConfigUnion] = None
    ComputeQuotaTarget: Optional[ComputeQuotaTarget] = None
    ActivationState: Optional[ActivationStateType] = None
    Description: Optional[str] = None


# This class is the input for the 'create_edge_deployment_plan' function.
class CreateEdgeDeploymentPlanRequest(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    ModelConfigs: List[EdgeDeploymentModelConfig]
    DeviceFleetName: str
    Stages: Optional[List[DeploymentStage]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_edge_deployment_stage' function.
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


# This class is the input for the 'search' function.
class SearchRequest(BaseValidatorModel):
    Resource: ResourceTypeType
    SearchExpression: Optional[SearchExpression] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[List[VisibilityConditions]] = None


# This class is the output for the 'list_associations' function.
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


# This class is the output for the 'list_trial_components' function.
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


# This class is the output for the 'describe_inference_component' function.
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


# This class is the output for the 'list_app_image_configs' function.
class ListAppImageConfigsResponse(BaseValidatorModel):
    AppImageConfigs: List[AppImageConfigDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_app_image_config' function.
class CreateAppImageConfigRequest(BaseValidatorModel):
    AppImageConfigName: str
    Tags: Optional[List[Tag]] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigUnion] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigUnion] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigUnion] = None


# This class is the input for the 'update_app_image_config' function.
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


# This class is the output for the 'list_monitoring_alerts' function.
class ListMonitoringAlertsResponse(BaseValidatorModel):
    MonitoringAlertSummaries: List[MonitoringAlertSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_inference_experiment' function.
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


# This class is the input for the 'stop_inference_experiment' function.
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


# This class is the output for the 'describe_optimization_job' function.
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


# This class is the input for the 'create_cluster_scheduler_config' function.
class CreateClusterSchedulerConfigRequest(BaseValidatorModel):
    Name: str
    ClusterArn: str
    SchedulerConfig: SchedulerConfigUnion
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_cluster_scheduler_config' function.
class UpdateClusterSchedulerConfigRequest(BaseValidatorModel):
    ClusterSchedulerConfigId: str
    TargetVersion: int
    SchedulerConfig: Optional[SchedulerConfigUnion] = None
    Description: Optional[str] = None


# This class is the output for the 'describe_processing_job' function.
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


# This class is the input for the 'create_project' function.
class CreateProjectInput(BaseValidatorModel):
    ProjectName: str
    ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsUnion
    ProjectDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_flow_definition' function.
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


# This class is the output for the 'describe_labeling_job' function.
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


# This class is the input for the 'start_pipeline_execution' function.
class StartPipelineExecutionRequest(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineParameters: Optional[List[Parameter]] = None
    PipelineExecutionDescription: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfigUnion] = None


# This class is the input for the 'create_inference_experiment' function.
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


# This class is the input for the 'update_inference_experiment' function.
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


# This class is the input for the 'create_transform_job' function.
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


# This class is the output for the 'describe_transform_job' function.
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


# This class is the output for the 'describe_domain' function.
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


# This class is the output for the 'describe_user_profile' function.
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


# This class is the output for the 'describe_auto_ml_job_v2' function.
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


# This class is the input for the 'create_auto_ml_job' function.
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


# This class is the output for the 'list_pipeline_execution_steps' function.
class ListPipelineExecutionStepsResponse(BaseValidatorModel):
    PipelineExecutionSteps: List[PipelineExecutionStep]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DeploymentConfigUnion = Union[DeploymentConfig, DeploymentConfigOutput]


# This class is the output for the 'describe_inference_recommendations_job' function.
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


# This class is the output for the 'describe_endpoint_config' function.
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


# This class is the output for the 'describe_endpoint' function.
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


# This class is the output for the 'list_spaces' function.
class ListSpacesResponse(BaseValidatorModel):
    Spaces: List[SpaceDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_inference_recommendations_job_steps' function.
class ListInferenceRecommendationsJobStepsResponse(BaseValidatorModel):
    Steps: List[InferenceRecommendationsJobStep]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_workteam' function.
class DescribeWorkteamResponse(BaseValidatorModel):
    Workteam: Workteam
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_workteams' function.
class ListWorkteamsResponse(BaseValidatorModel):
    Workteams: List[Workteam]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_workteam' function.
class UpdateWorkteamResponse(BaseValidatorModel):
    Workteam: Workteam
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_inference_component' function.
class UpdateInferenceComponentInput(BaseValidatorModel):
    InferenceComponentName: str
    Specification: Optional[InferenceComponentSpecification] = None
    RuntimeConfig: Optional[InferenceComponentRuntimeConfig] = None
    DeploymentConfig: Optional[InferenceComponentDeploymentConfigUnion] = None

TrainingSpecificationUnion = Union[TrainingSpecification, TrainingSpecificationOutput]


# This class is the output for the 'list_labeling_jobs' function.
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


# This class is the output for the 'describe_training_job' function.
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


# This class is the output for the 'describe_model' function.
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


# This class is the input for the 'create_optimization_job' function.
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


# This class is the output for the 'describe_data_quality_job_definition' function.
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


# This class is the output for the 'describe_model_bias_job_definition' function.
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


# This class is the output for the 'describe_model_explainability_job_definition' function.
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


# This class is the output for the 'describe_model_quality_job_definition' function.
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


# This class is the input for the 'create_workteam' function.
class CreateWorkteamRequest(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: List[MemberDefinitionUnion]
    Description: str
    WorkforceName: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_workteam' function.
class UpdateWorkteamRequest(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: Optional[List[MemberDefinitionUnion]] = None
    Description: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration] = None


# This class is the input for the 'create_processing_job' function.
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


# This class is the input for the 'create_flow_definition' function.
class CreateFlowDefinitionRequest(BaseValidatorModel):
    FlowDefinitionName: str
    OutputConfig: FlowDefinitionOutputConfig
    RoleArn: str
    HumanLoopRequestSource: Optional[HumanLoopRequestSource] = None
    HumanLoopActivationConfig: Optional[HumanLoopActivationConfig] = None
    HumanLoopConfig: Optional[HumanLoopConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_labeling_job' function.
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


# This class is the output for the 'describe_space' function.
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


# This class is the input for the 'create_domain' function.
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


# This class is the input for the 'create_user_profile' function.
class CreateUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    SingleSignOnUserIdentifier: Optional[str] = None
    SingleSignOnUserValue: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    UserSettings: Optional[UserSettingsUnion] = None


# This class is the input for the 'update_domain' function.
class UpdateDomainRequest(BaseValidatorModel):
    DomainId: str
    DefaultUserSettings: Optional[UserSettingsUnion] = None
    DomainSettingsForUpdate: Optional[DomainSettingsForUpdate] = None
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagementType] = None
    DefaultSpaceSettings: Optional[DefaultSpaceSettingsUnion] = None
    SubnetIds: Optional[List[str]] = None
    AppNetworkAccessType: Optional[AppNetworkAccessTypeType] = None
    TagPropagation: Optional[TagPropagationType] = None


# This class is the input for the 'update_user_profile' function.
class UpdateUserProfileRequest(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    UserSettings: Optional[UserSettingsUnion] = None


# This class is the input for the 'create_auto_ml_job_v2' function.
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


# This class is the input for the 'create_endpoint' function.
class CreateEndpointInput(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: str
    DeploymentConfig: Optional[DeploymentConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_endpoint' function.
class UpdateEndpointInput(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: str
    RetainAllVariantProperties: Optional[bool] = None
    ExcludeRetainedVariantProperties: Optional[List[VariantProperty]] = None
    DeploymentConfig: Optional[DeploymentConfigUnion] = None
    RetainDeploymentConfig: Optional[bool] = None


# This class is the input for the 'create_inference_recommendations_job' function.
class CreateInferenceRecommendationsJobRequest(BaseValidatorModel):
    JobName: str
    JobType: RecommendationJobTypeType
    RoleArn: str
    InputConfig: RecommendationJobInputConfigUnion
    JobDescription: Optional[str] = None
    StoppingConditions: Optional[RecommendationJobStoppingConditionsUnion] = None
    OutputConfig: Optional[RecommendationJobOutputConfig] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_endpoint_config' function.
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


# This class is the output for the 'get_scaling_configuration_recommendation' function.
class GetScalingConfigurationRecommendationResponse(BaseValidatorModel):
    InferenceRecommendationsJobName: str
    RecommendationId: str
    EndpointName: str
    TargetCpuUtilizationPerCore: int
    ScalingPolicyObjective: ScalingPolicyObjective
    Metric: ScalingPolicyMetric
    DynamicScalingConfiguration: DynamicScalingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_hyper_parameter_tuning_job' function.
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


# This class is the input for the 'create_model' function.
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


# This class is the input for the 'create_data_quality_job_definition' function.
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


# This class is the input for the 'create_model_bias_job_definition' function.
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


# This class is the input for the 'create_model_explainability_job_definition' function.
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


# This class is the input for the 'create_model_quality_job_definition' function.
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


# This class is the input for the 'create_space' function.
class CreateSpaceRequest(BaseValidatorModel):
    DomainId: str
    SpaceName: str
    Tags: Optional[List[Tag]] = None
    SpaceSettings: Optional[SpaceSettingsUnion] = None
    OwnershipSettings: Optional[OwnershipSettings] = None
    SpaceSharingSettings: Optional[SpaceSharingSettings] = None
    SpaceDisplayName: Optional[str] = None


# This class is the input for the 'update_space' function.
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


# This class is the output for the 'batch_describe_model_package' function.
class BatchDescribeModelPackageOutput(BaseValidatorModel):
    ModelPackageSummaries: Dict[str, BatchDescribeModelPackageSummary]
    BatchDescribeModelPackageErrorMap: Dict[str, BatchDescribeModelPackageError]
    ResponseMetadata: ResponseMetadata

AdditionalInferenceSpecificationDefinitionUnion = Union[AdditionalInferenceSpecificationDefinition, AdditionalInferenceSpecificationDefinitionOutput]


# This class is the output for the 'describe_monitoring_schedule' function.
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


# This class is the output for the 'describe_model_package' function.
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


# This class is the output for the 'describe_algorithm' function.
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


# This class is the input for the 'create_training_job' function.
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


# This class is the input for the 'update_model_package' function.
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


# This class is the input for the 'create_monitoring_schedule' function.
class CreateMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigUnion
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_monitoring_schedule' function.
class UpdateMonitoringScheduleRequest(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigUnion


# This class is the input for the 'create_model_package' function.
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


# This class is the input for the 'create_hyper_parameter_tuning_job' function.
class CreateHyperParameterTuningJobRequest(BaseValidatorModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfigUnion
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinitionUnion] = None
    TrainingJobDefinitions: Optional[List[HyperParameterTrainingJobDefinitionUnion]] = None
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    Autotune: Optional[Autotune] = None

AlgorithmValidationSpecificationUnion = Union[AlgorithmValidationSpecification, AlgorithmValidationSpecificationOutput]


# This class is the output for the 'search' function.
class SearchResponse(BaseValidatorModel):
    Results: List[SearchRecord]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_algorithm' function.
class CreateAlgorithmInput(BaseValidatorModel):
    AlgorithmName: str
    TrainingSpecification: TrainingSpecificationUnion
    AlgorithmDescription: Optional[str] = None
    InferenceSpecification: Optional[InferenceSpecificationUnion] = None
    ValidationSpecification: Optional[AlgorithmValidationSpecificationUnion] = None
    CertifyForMarketplace: Optional[bool] = None
    Tags: Optional[List[Tag]] = None